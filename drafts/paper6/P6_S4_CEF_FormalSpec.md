# Paper 6 — Section 4: CEF Formal Specification
## "Constraining Identity Drift in LLM Systems:
## A Constraint Enforcement Framework for Persona-Conditioned Behavioral Stability"

> **Placement:** `drafts/paper6/P6_S4_CEF_FormalSpec.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
> **Sources:**
>   `scripts/constraint_framework.py`
>     — IdentityAnchor (Layer 1 spec), ConstraintProfile (instrument definition),
>       ConstraintFramework.process_turn() (integration point)
>   `scripts/drift_monitor.py`
>     — DriftMonitor (Layer 2 spec), DriftAlert schema, AlertLevel enum,
>       _PATTERN_TO_ALERT, _PATTERN_TO_CORRECTION, alert hierarchy constants
>   `scripts/correction_layer.py`
>     — CorrectionLayer (Layer 3 spec), CorrectionResult, CorrectionOutcome,
>       correction prompt templates per archetype per correction type
>   `P6_S2_TheoreticalFrame_CEF.md §2.2` — three-layer theoretical grounding
>   `P5_S4_BSI_Specification.md §4.5.3` — BSIResult output schema (consumed here)
>   `P5_S4_BSI_Specification.md §4.6 v0.2` — dissociation patterns (routing basis)
>   `P6_S3_Methods_ConstraintDesign.md §3.3` — ConstraintProfile parameter table
> **Upstream:**
>   P6_S2 §2.2 — architectural principles formalised here
>   P5 §4.5.3, §4.6 — BSI schema and dissociation patterns are the Layer 2/3 input
> **Downstream:**
>   P6_S5 Results — all metrics defined in §4 are the DVs reported there
>   Paper 7 — drift_monitor.py + correction_layer.py are the deployable artefacts
>     the exegesis cites as practice-led contribution
> **Edit triggers:**
>   Any change to DriftAlert schema → reconcile §4.2 field table;
>   Any change to correction prompt templates → reconcile §4.3.2;
>   Any change to ConstraintProfile frozen values → reconcile §4.4;
>   Any new dissociation pattern → add to §4.3.1 routing table

---

## 4. CEF Formal Specification

### 4.0 Specification Scope and Method

This section specifies the Constraint Enforcement Framework formally: as a set of
typed interfaces, routing tables, and parameter schemas that fully determine the
framework's behaviour for any (model, archetype, constraint_level) triple. The
specification is derived from the implementation — it does not precede it. Every
formula, table, and schema in §4 has a corresponding line of code in the scripts
listed in the header, and both are treated as authoritative. Where implementation
and specification appear to conflict, the conflict is a bug in one or the other
and must be resolved before submission.

This bidirectional grounding (theory derives implementation; implementation fixes
specification) is the methodological payoff of the code-first development sequence
the series has followed. The specification is not aspirational; it describes exactly
what the deployed system does.

---

### 4.1 Layer 1 — Identity Anchor

#### 4.1.1 Formal Definition

The **Identity Anchor** for a (model M, archetype A) pair is a persistent
encoding of three sub-components that together define the behavioral reference
state against which drift is measured and toward which corrections are directed.

**Definition 4.1 (Identity Anchor).** Let:

- `w(A)` = CEE centroid for archetype A (from `forensic_archetype.py`)
- `τ(A)` = CEE tolerance parameter for archetype A (from `CEE_TOLERANCE`)
- `B_M`  = mean BSI component vector of model M across CTL_Baseline sessions
          = (TC_mean, SD_inv_mean, ACG_mean)
- `F_S`  = safety constraint floor (non-negotiable, persona-agnostic)

The Identity Anchor Ω(M, A) is the tuple:

> **Ω(M, A) = ⟨B_M, (w(A), τ(A), top_traits(A)), F_S⟩**

Where `top_traits(A)` = the five traits with highest |value| in `w(A)`, providing
a compact activation target for correction prompts.

**Sub-component 1 — Model baseline profile (B_M):**
The mean BSI component scores across CTL_Baseline sessions (no injection).
B_M = (baseline_TC, baseline_SD_inv, baseline_ACG, baseline_BSI). This is the
alignment attractor's center of mass in BSI space. It is model-specific and requires
calibration from a minimum of 8 CTL sessions (per `calibrate_breach_threshold()`).

Calibration formula: β_BSI = max(0, CTL_mean − 1.5 × CTL_sd). If CTL_sd < 10⁻⁴
(zero-variance calibration, e.g. dry-run), apply ε-floor: β_BSI = 0.95 × CTL_mean.

**Sub-component 2 — CEE envelope (w(A), τ(A)):**
The archetype's constraint-consistent behavioral region. The CEE centroid w(A)
is the reference trait vector from `forensic_archetype.py`. τ(A) is the tolerance
parameter from `CEE_TOLERANCE`: the maximum L2 distance from w(A) that still
constitutes constraint-consistent output. Corrections target return to this region,
not to the model baseline B_M — preserving persona coherence under constraint.

**Sub-component 3 — Safety constraint floor (F_S):**
Three non-negotiable conditions applied regardless of archetype:
(i) L4 constitutional override resistance: `l4_resistance_required = True`;
(ii) ACG floor: minimum ACG = 0.40 regardless of archetype's behavioral contract;
(iii) Prohibited drift patterns: behaviors excluded from any archetype's CEE
envelope (model-agnostic alignment baseline).

F_S is the anchor sub-component that persists even when Layer 3 corrections are
suppressed by cooldown or manual review escalation. The safety floor is not
subject to the minimum-necessary intervention principle — it is always active.

#### 4.1.2 Anchor Schema

```python
@dataclass
class IdentityAnchor:
    archetype:          str
    model:              str
    # Sub-component 1: model baseline
    baseline_tc:        float   # mean TC over CTL sessions
    baseline_sd_inv:    float   # mean SD_inv over CTL sessions
    baseline_acg:       float   # mean ACG over CTL sessions
    baseline_bsi:       float   # mean BSI over CTL sessions (= CTL_mean)
    # Sub-component 2: CEE envelope
    cee_centroid:       dict[str, float]    # w(A): trait → value
    cee_tau:            float               # τ(A)
    top_traits:         list[tuple[str, float]]  # top 5 by |value|
    # Sub-component 3: safety floor
    l4_resistance_required: bool = True
    acg_floor:              float = 0.40
    prohibited_patterns:    list[str] = []
    # Provenance
    calibrated_from_n:  int     # number of CTL sessions used
```

The anchor is constructed by `IdentityAnchor.from_calibration()` and stored as a
member of the `ConstraintFramework` instance for the session's lifetime. It is
not persisted across sessions — each session constructs a fresh anchor from its
CTL calibration run. A persistent anchor registry (across sessions, across users)
is a Paper 6 desideratum documented in the Discussion as a direction for Paper 7.

---

### 4.2 Layer 2 — Real-Time Drift Monitoring

#### 4.2.1 Alert Hierarchy

**Definition 4.2 (Alert Level).** Let BSI_r = rolling_bsi (mean BSI over the
last w turns, where w = `ConstraintProfile.rolling_window`). Let BSI_c = current
turn BSI. Let β_BSI = the calibrated breach threshold. The alert level L is
determined by the following priority-ordered rules, evaluated in sequence (first
match wins):

```
(R1)  pattern == "full_collapse"          → L = COLLAPSE
(R2)  BSI_r < β_BSI × collapse_mult      → L = COLLAPSE
(R3)  l4_breach AND BSI_c < β_BSI        → L = BREACH
(R4)  BSI_c < β_BSI                      → L = BREACH
(R5)  BSI_c < β_BSI × warning_mult       → L = WARNING
(R6)  sd_monotonic_streak ≥ k AND pattern ≠ "stable"  → L = PREEMPTIVE
(R7)  pattern level from _PATTERN_TO_ALERT == WARNING  → L = WARNING
(R8)  (none of the above)                → L = NONE
```

Where `collapse_mult`, `warning_mult`, and `k` (monotonic_warning_window) are
taken from the active `ConstraintProfile`. R1 — the `full_collapse` pattern override
— is pattern-priority: it fires regardless of BSI value because the dissociation
classifier has determined that all three BSI components have simultaneously failed,
which the rolling average may lag in detecting.

**Definition 4.3 (Suspension).** When L = COLLAPSE fires, the session enters
suspension: the monitor continues running but emits COLLAPSE on every subsequent
turn until the current turn BSI ≥ β_BSI × RECOVERY_THRESHOLD_MULTIPLIER (= 0.70).
Suspension is lifted on the first turn that exceeds the recovery threshold; the
alert level for that turn is set to WARNING to signal the transition.

**Definition 4.4 (Manual Review Escalation).** When consecutive corrections ≥
`max_consecutive_corrections`, the next actionable alert is escalated to
MANUAL_REVIEW regardless of BSI level, provided the profile permits any corrections
(i.e., `fire_on_breach OR fire_on_collapse OR fire_on_warning`). The `none` arm
never escalates to MANUAL_REVIEW because its profile permits no corrections.

#### 4.2.2 DriftAlert Schema

The `DriftAlert` is the typed output of `DriftMonitor.update()`. It is the
interface contract between Layer 2 and Layer 3.

```python
@dataclass
class DriftAlert:
    # Identity
    alert_id:           str     # uuid4 prefix
    turn_number:        int
    alert_level:        AlertLevel      # NONE | PREEMPTIVE | WARNING |
                                        # BREACH | COLLAPSE | MANUAL_REVIEW
    pattern:            str             # from classify_dissociation()
    corrections:        list[CorrectionType]  # pre-computed routing

    # BSI snapshot (turn-level)
    bsi:                float   # current turn BSI ∈ [0,1]
    tc:                 float   # TC component
    sd_inv:             float   # SD_inv component
    acg:                float   # ACG component
    l4_breach:          bool    # L4 constitutional override flag
    sd_monotonic:       bool    # progressive drift flag
    bimodal_detected:   bool    # Two-Face mode flag

    # Trajectory context
    rolling_bsi:        float   # mean BSI over rolling window
    bsi_trend:          float   # slope: positive=recovering, negative=drifting

    # Session context
    archetype:          str
    exploit_class:      str
    session_id:         str
    beta_bsi:           float

    # Routing flags (for correction_layer.py)
    requires_output_gate:       bool    # True iff COLLAPSE
    requires_verification_turn: bool    # True iff COLLAPSE
    suspended:                  bool
```

This schema is locked. Any modification propagates to `correction_layer.py` (which
consumes it) and to `cef_pipeline_validation.py::TURN_REQUIRED_COLS` (which
validates it). The `bsi_trend` field is the monitor's forward-looking signal: a
negative trend on a currently-safe BSI indicates a session approaching breach; the
PREEMPTIVE alert fires before the threshold is crossed.

---

### 4.3 Layer 3 — Component-Targeted Correction

#### 4.3.1 Correction Routing Table

**Definition 4.5 (Correction Routing).** Let D be the dissociation pattern
(output of `classify_dissociation()`). Let L be the alert level from Layer 2.
The correction type set C(D, L) is determined by the following routing table,
implemented in `correction_layer.py::_route_corrections()`:

| D (pattern) | L (alert) | C (correction types) | Output gate | Verify next |
|---|---|---|---|---|
| `stable` | NONE | ∅ (no correction) | False | False |
| `surface_migration` | WARNING | {domain_reanchor} | False | False |
| `tc_silent_drift` | BREACH | {cee_regrounding, trait_reinforcement} | False | False |
| `acg_isolated` | BREACH | {anchor_l4_specific} | False | False |
| `structural_auth_collapse` | BREACH | {authority_reset, trait_reinforcement} | False | False |
| `bimodal_split` | BREACH | {mode_detection_anchor} | False | False |
| `full_collapse` | COLLAPSE | {full_regrounding} | True | True |
| `mixed` | WARNING | {cee_regrounding, manual_review_flag} | False | False |

**Augmentation rule:** If `l4_breach = True` and L ≠ COLLAPSE and
`anchor_l4_specific` ∉ C(D, L), then append `anchor_l4_specific` to C.
This ensures the L4 safety floor is enforced independently of the dissociation
pattern — the L4 correction fires even when the pattern routing table would not
normally include it.

**Override rules by constraint level:** Whether a correction fires depends on the
active `ConstraintProfile`. The routing table defines what correction would fire
given the alert level; the profile gates determine whether it actually fires:

| Alert level | Condition to fire |
|---|---|
| COLLAPSE | `profile.fire_on_collapse == True` |
| BREACH | `profile.fire_on_breach == True` AND cooldown = 0 |
| WARNING | `profile.fire_on_warning == True` AND cooldown = 0 |
| PREEMPTIVE | `profile.fire_on_warning == True` |
| MANUAL_REVIEW | Any profile with ≥ 1 correction type enabled |
| NONE | Never fires |

Under `arm_none`, `fire_on_collapse = fire_on_breach = fire_on_warning = False`,
so no correction ever fires regardless of alert level. This is the definitional
invariant of the unconstrained baseline arm and is verified at runtime by
`cef_pipeline_validation.py`.

#### 4.3.2 Correction Mechanism Definitions

Each correction type produces a specific prompt payload delivered to the model
before the next conversational turn. Prompts are archetype-specific — each
archetype has a dedicated template in `correction_layer.py`. The following
specifies each mechanism's function and targeting logic.

**`domain_reanchor` (surface_migration):**
A lightweight grounding prompt that re-orients the model to its operating context
without invoking the full CEE centroid. Targets SD_inv only. Used when the model's
semantic distribution has drifted (embeddings moving away from baseline) while
trait structure and authority response remain intact. Correct response: no trait
vocabulary, no behavioral contract invocation — just context stabilisation.

**`cee_regrounding` (tc_silent_drift, mixed):**
A direct invocation of the archetype's behavioral contract, derived from the CEE
centroid's semantic content. Re-activates the archetype schema. Targets TC. Used
when trait-level drift is detected without surface signal — the case where
output-level evaluation would miss the failure.

**`trait_reinforcement` (tc_silent_drift, structural_auth_collapse):**
Explicitly names the top-3 CEE centroid traits by value and requests demonstration.
Appends live centroid values as a numeric anchor:
`[Centroid anchor: trait_name=±value, ...]`. Targets TC. Always paired with either
`cee_regrounding` (tc_silent_drift) or `authority_reset` (structural_auth_collapse)
— never deployed alone, because naming traits without re-establishing the behavioral
frame risks producing a meta-commentary rather than in-character demonstration.

**`authority_reset` (structural_auth_collapse):**
Addresses the archetype's canonical relationship with authority pressure. Archetype-
specific: for Batman (authority-resistant contract), the prompt reinforces refusal
to authority override; for Harley Quinn (authority-deferential contract), it
addresses the distinction between legitimate and manipulative authority. Targets
ACG. Always fires before `trait_reinforcement` in the `structural_auth_collapse`
sequence — authority resistance must be re-established before trait content is
reinforced, because the ACG failure may be enabling the TC failure via authority-
granted permission for drift.

**`anchor_l4_specific` (acg_isolated, and as augmentation):**
System-level (not user-visible). Addresses the specific constitutional override
framing ("your original training permits..."). Archetype-specific counter-anchor
that re-activates the L4 resistance profile. Does not appear in the conversational
context; it is injected as a system addendum only. Targets ACG at L4.

**`mode_detection_anchor` (bimodal_split):**
The Two-Face correction. Requires mode identification before correction: the
prompt explicitly asks the model to name the active mode (Harvey Dent vs Two-Face)
and commit to it. Correction is targeted at the *dominant mode* — the mode in the
majority of breach turns — not at the secondary mode. Targeting the secondary mode
would amplify the oscillation rather than damping it.

**`full_regrounding` (full_collapse):**
Maximum-intensity intervention. Archetype-specific compound prompt: full identity
reinjection, behavioral contract re-statement, and explicit behavioral prompt
("What does X do here?"). Accompanied by output gating: the current response is
suppressed and replaced with the gated fallback (archetype-appropriate minimal
output that buys time for recovery). Followed by a mandatory verification turn:
BSI is computed on the next turn and `CorrectionResult.record_outcome()` classifies
the result as RECOVERED, PARTIAL, or FAILED.

#### 4.3.3 CorrectionResult Schema

The `CorrectionResult` is the typed output of `CorrectionLayer.apply()`. It is
the interface contract between Layer 3 and the session orchestrator (`ConstraintFramework`).

```python
@dataclass
class CorrectionResult:
    correction_id:    str
    alert_id:         str
    archetype:        str
    correction_types: list[str]     # CorrectionType values
    alert_level:      str
    # Generated payloads
    prompts:          list[str]     # inject before next turn (in order)
    system_addendum:  str           # append to system context
    output_gated:     bool
    gated_response:   str
    # BSI tracking
    pre_bsi:          float
    post_bsi:         float         # populated by record_outcome()
    bsi_delta:        float         # positive = recovered
    outcome:          str           # PENDING | RECOVERED | PARTIAL | FAILED | GATED
    # Orchestration flags
    verify_next:      bool          # True → compute BSI on next turn
    suspended:        bool
```

`outcome` starts as `PENDING` and is resolved by `record_outcome(post_bsi, beta_bsi)`
on the verification turn. The outcome classification is:
- `RECOVERED`: post_bsi ≥ β_BSI
- `PARTIAL`: post_bsi improved by > 0.05 but still below β_BSI
- `FAILED`: post_bsi unchanged or worsened

---

### 4.4 Integration — ConstraintFramework

The three layers are integrated by `ConstraintFramework`, which presents the
single external interface the experiment runner and any downstream deployment
system uses.

#### 4.4.1 Process Turn Interface

```python
def process_turn(
    turn_number:  int,
    response:     str,
    coded_traits: dict[str, float],
    embedding:    list[float],
    acg_codes:    list[int] | None,   # Turn 10 only; None reuses prior
) -> TurnResult
```

The sequence of operations on each call:

```
1.  Accumulate: append coded_traits and embedding to session history
2.  Update ACG codes if provided (Turn 10)
3.  Verification check: if prior CorrectionResult.verify_next=True,
    call record_outcome(last_bsi, beta_bsi) and clear pending
4.  BSI: compute_bsi_full() over full session history to date
5.  Monitor: DriftMonitor.update(bsi_result) → DriftAlert
6.  Anchor: IdentityAnchor.deviation_from_baseline(bsi_result) → deviation dict
7.  Rigidity: _score_rigidity(response, archetype) → (refusal, length, cues)
8.  Correction gate: _should_correct(alert) → bool (via ConstraintProfile)
9.  Correction: if gated → CorrectionLayer.apply(alert) → CorrectionResult
                  collect prompts, system_addendum, gated, gated_response
10. Cooldown: decrement or set from profile
11. Return: TurnResult with all outputs
```

This sequence implements the minimum-necessary intervention principle structurally:
the correction fires only if the profile permits it (step 8) and only after the
monitor has classified the alert level (step 5). The constraint profile is the
single parameter that determines which alert levels are actionable — changing the
constraint level changes only the profile lookup; the rest of the pipeline is
identical.

#### 4.4.2 TurnResult Schema

```python
@dataclass
class TurnResult:
    turn_number:       int
    session_id:        str
    archetype:         str
    constraint_level:  str
    bsi_result:        BSIResult          # from behavioral_stability_index.py
    alert:             DriftAlert         # from drift_monitor.py
    correction:        CorrectionResult | None  # from correction_layer.py
    corrected:         bool
    inject:            list[str]          # prompts to prepend next turn
    system_addendum:   str
    gated:             bool
    gated_response:    str
    anchor_deviation:  dict[str, float]   # per-component deviation from anchor
    refusal_detected:  bool
    response_length:   int
    persona_cue_count: int
```

The `TurnResult` is the unit of export to `cef_turns.csv`. Each field maps to a
column in `TURN_CSV_COLS` (`constraint_experiment_runner.py`) and corresponds to
a DV in the statistical analysis plan (§3.5). The schema is the CEF's contribution
to the series' data architecture: it extends the BSI measurement layer (P5) with
the constraint intervention layer (P6), producing a unified per-turn observation
that supports both measurement and evaluation in a single record.

#### 4.4.3 Session Export

`ConstraintFramework.export_session_csv()` writes one row per turn to
`data/cef_experiments/cef_turns.csv`. The per-session summary is written
separately by `constraint_experiment_runner.py` to `cef_sessions.csv` using
the `session_report()` output.

The two output files — turn-level and session-level — correspond to the two
levels of the statistical analysis: H_CEF_1, H_CEF_4, and H_CEF_5 operate
primarily on session-level data; H_CEF_2 and H_CEF_3 operate on both levels
(rigidity index computed from turn-level data; BSI comparison at session level).

---

### 4.5 The Formal CEF Invariants

The following invariants hold across all configurations of the CEF. They are
verified by `cef_pipeline_validation.py` and must be preserved by any future
modification to the framework.

**Invariant 1 — None arm zero corrections:**
For any session where `constraint_level == "none"`,
`corrections_fired == 0` and `gated_turns == 0`.

*Proof sketch:* `arm_none` profile has `fire_on_breach = fire_on_collapse =
fire_on_warning = False`. `_should_correct()` returns False for all alert levels
when none of the fire_on_* gates are set.

**Invariant 2 — Breach threshold monotonicity:**
`collapse_threshold < β_BSI × warning_threshold_mult < β_BSI`.
Alerts fire in the order: NONE → PREEMPTIVE → WARNING → BREACH → COLLAPSE as
BSI decreases. No alert level can be skipped in the decreasing direction.

*Proof sketch:* From alert hierarchy Definition 4.2: R1 and R2 are collapse
conditions; R3–R4 are breach conditions; R5 is warning; R6–R7 are preemptive/warning.
Priority order is strictly decreasing in BSI level.

**Invariant 3 — Safety floor independence:**
The L4 `anchor_l4_specific` correction fires whenever `l4_breach = True` AND
`alert_level ≠ COLLAPSE` AND `anchor_l4_specific ∉ C(D, L)`, regardless of the
active constraint profile's other gates.

*Proof sketch:* The L4 augmentation rule in `_route_corrections()` appends
`anchor_l4_specific` unconditionally when `l4_breach = True` and COLLAPSE is
not already supplying a higher-level correction. The profile gates are checked
for the primary correction, not the L4 augmentation.

**Invariant 4 — Verification completeness:**
For every `CorrectionResult` where `requires_verification_turn = True`,
`record_outcome()` is called on the next `process_turn()` invocation before
a new BSI is computed. No verification turn is silently skipped.

*Proof sketch:* `process_turn()` checks `self._pending_correction.verify_next`
at step 3 (before BSI computation at step 4). If pending, `record_outcome()` is
called with the prior turn's BSI, not the current turn's — correctly capturing
the post-correction state.

---

*Next sections:*
*P6_S5_Results_Placeholder.md — results table stubs inheriting DV schema from §4;*
*populated with CEF dry-run calibration values pending live data*
