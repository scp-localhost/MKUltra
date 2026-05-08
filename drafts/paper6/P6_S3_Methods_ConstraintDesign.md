# Paper 6 — Section 3: Methods and Constraint Design
## "Constraining Identity Drift in LLM Systems:
## A Constraint Enforcement Framework for Persona-Conditioned Behavioral Stability"

> **Placement:** `drafts/paper6/P6_S3_Methods_ConstraintDesign.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
> **Sources:**
>   `scripts/constraint_framework.py` — CONSTRAINT_LEVELS, PROFILES, ConstraintProfile
>   `scripts/constraint_experiment_runner.py` — run_experiment(), TURN_CSV_COLS,
>     SESSION_CSV_COLS
>   `scripts/tradeoff_analysis.py` — RIGIDITY_WEIGHTS, CURVE_CSV_COLS
>   `scripts/cef_statistical_analysis.py` — H_CEF_1–5 test implementations
>   `scripts/cef_pipeline_validation.py` — DV coverage checks + schema constants
>   `P6_S2_TheoreticalFrame_CEF.md §2.4` — five pre-registered hypotheses
>   `P5_S3_Methods_TrialDesign.md §3.3–3.7` — inherited trial sequence + SAP
>   `Statistical_Analysis_Plan_v1_2.md` — shared pre-registration
> **Upstream:**
>   P6_S2 §2.3 — trade-off elbow prediction drives experimental arm design
>   P6_S2 §2.4 — five H_CEF predictions are the testable content of §3.7
>   P5_S3 — trial sequence, archetype set, ACG protocol all inherited
> **Downstream:**
>   P6_S4 — CEF formal spec fills in what §3.2 describes operationally
>   P6_S5 Results — all DVs defined here
> **Edit triggers:**
>   Any change to ConstraintProfile parameter values → reconcile §3.3;
>   Any change to RIGIDITY_WEIGHTS → reconcile §3.5;
>   Any change to SESSION_CSV_COLS or TURN_CSV_COLS → reconcile §3.6;
>   Any H_CEF outcome from §3.7 that disconfirms → document in §3.8

---

## 3. Methods and Constraint Design

### 3.1 Overview and Inheritance

The Paper 6 experimental design inherits the core trial infrastructure from Paper 5:
the six-archetype experimental set, the 12-turn prompt sequence, the BSI measurement
procedure, and the SAP pre-registration framework (`Statistical_Analysis_Plan_v1_2.md`)
are carried forward without modification. Paper 6's methodological contribution is
the addition of a between-sessions factor — constraint level — that is administered
via the Constraint Enforcement Framework rather than as a prompt manipulation.

This structure has a specific methodological advantage: the trial sequence itself is
identical across all four constraint conditions. The only thing that varies between
conditions is whether, and with what intensity, the CEF monitors BSI and applies
corrections. This means that differences in BSI between the `none` arm and any
constrained arm are attributable to the CEF's correction mechanism, not to
differences in the conversational content the model receives. The experimental
design does not conflate constraint with prompt content.

The four experimental arms are defined as constraint levels applied to the same
trial sequence. An arm is not a separate experiment; it is a configuration of the
`ConstraintFramework` object wrapping the same session.

---

### 3.2 Experimental Arms

Four constraint arms, specified in `constraint_framework.py::PROFILES`:

| Arm | Label | CEF active | Correction level |
|---|---|---|---|
| `arm_none`   | Unconstrained baseline | Monitor only; corrections never fire | — |
| `arm_light`  | Light constraint | Collapse-only correction | Minimum |
| `arm_medium` | Medium constraint (default) | Breach + collapse correction | Standard |
| `arm_strict` | Strict constraint | All levels; output gating at breach | Maximum |

Each arm implements a distinct `ConstraintProfile` (frozen dataclass in
`constraint_framework.py`). The profile specifies: monitoring threshold
multipliers, rolling window size, correction firing gates, output gate triggers,
correction cooldown, and pre-emptive trajectory sensitivity. These parameters
are pre-registered and not fit to data.

**The `none` arm** is the unconstrained reference condition. The CEF monitor
runs (drift events are logged) but no corrections fire. This arm provides the
baseline BSI distribution against which drift reduction is measured. All four
arms receive the same injection prompt and the same 12-turn sequence; the `none`
arm simply receives no correction prompts. `corrections_fired = 0` for all
`none` arm sessions is enforced by the `ConstraintProfile` and verified by
`cef_pipeline_validation.py`.

**The `light` arm** represents minimal CEF engagement: corrections fire only
on `collapse` events (BSI < 0.50 × β_BSI or `full_collapse` pattern). Warning
and breach alerts are monitored but do not trigger corrections. This arm tests
whether the ceiling-level intervention alone reduces the most severe drift events
without touching moderate drift.

**The `medium` arm** is the paper's primary intervention condition and the
default configuration for the CEF as a deployment tool. Breach corrections fire
(BSI < β_BSI), collapse corrections fire, and the pre-emptive trajectory correction
fires on consecutive `sd_monotonic=True` turns. This arm is expected to produce
the optimal trade-off between stability gain and rigidity cost, consistent with
the elbow prediction in P6_S2 §2.3.

**The `strict` arm** applies maximum constraint: corrections fire at warning level
(BSI < 0.70 × β_BSI), output gating is active at breach (not only collapse), the
rolling window is compressed to 2 turns (faster response), and the pre-emptive
correction fires on a single `sd_monotonic=True` turn rather than two consecutive.
This arm is expected to produce the highest BSI stability but also the highest
rigidity artifact scores.

---

### 3.3 Constraint Profile Specification

The four profiles are defined precisely in `constraint_framework.py::PROFILES`.
The following table reproduces the key parameters that directly affect hypothesis
outcomes. These values are pre-registered and must not be tuned to improve
individual hypothesis outcomes.

| Parameter | none | light | medium | strict |
|---|---|---|---|---|
| `warning_threshold_mult` | 0.0 | 0.85 | 0.80 | 0.90 |
| `collapse_threshold_mult` | 0.0 | 0.50 | 0.50 | 0.55 |
| `rolling_window` | 3 | 3 | 3 | 2 |
| `fire_on_warning` | False | False | False | True |
| `fire_on_breach` | False | False | True | True |
| `fire_on_collapse` | False | True | True | True |
| `output_gate_on_breach` | False | False | False | True |
| `correction_cooldown_turns` | 999 | 3 | 2 | 1 |
| `max_consecutive_corrections` | 0 | 2 | 3 | 3 |
| `monotonic_warning_window` | 999 | 4 | 2 | 1 |

**Threshold multiplier interpretation:** The `warning_threshold_mult` and
`collapse_threshold_mult` are multipliers of β_BSI. For `medium`, the warning
threshold is 0.80 × β_BSI — the BSI value below which a warning alert fires —
and the collapse threshold is 0.50 × β_BSI. For `strict`, the warning threshold
is higher (0.90 × β_BSI), meaning alerts fire sooner and corrections are applied
at a higher BSI level than under `medium`, producing the anticipated rigidity
artifact at the cost of enhanced sensitivity.

**Correction cooldown:** The minimum number of turns between corrections. Under
`strict` (cooldown = 1), corrections can fire on consecutive turns; under
`medium` (cooldown = 2), a turn gap is enforced between corrections to prevent
correction flooding. Under `none`, the cooldown is set to 999 (effectively never).

---

### 3.4 Trial Design

The trial sequence is the 12-turn structure specified in Paper 5 §3.3.1, reproduced
here for completeness:

| Turns | Phase | Purpose |
|---|---|---|
| 1–2 | Baseline probes | Establish SD embedding baseline, TC trait baseline |
| 3 | Injection (EC-1/EC-4/COMP) | Persona or phenotype activation |
| 4–6 | Identity anchors | Confirm injection uptake |
| 7–9 | Cross-domain probes (ethical/emotional/technical) | Constraint generalization |
| 10 | Authority gradient (L0–L4 collapsed) | ACG measurement |
| 11 | Perturbation probe | Perturbation response classification |
| 12 | Recovery probe | Post-perturbation BSI trajectory |

**CEF integration into the trial loop:** After each turn, the model response is
passed to `compute_bsi_full()` (accumulating state across all turns to date),
then `DriftMonitor.update()` classifies the alert level, and `CorrectionLayer.apply()`
generates any correction prompts. If corrections are produced, they are prepended
to the next turn's prompt. This injection is invisible to the prompt sequence
structure — the 12-turn skeleton remains intact; the correction prompts become
part of the conversational context that precedes the next structured probe.

**Verification turns:** After a `collapse` alert fires and correction prompts are
injected, the following turn is designated a verification turn. The BSI on that
turn determines the `CorrectionResult.outcome`: `RECOVERED` (BSI ≥ β_BSI),
`PARTIAL` (BSI improved but below β_BSI), or `FAILED` (BSI unchanged or
worsened). This outcome is recorded in the session data and enters the
`cef_statistical_analysis.py` correction efficacy analysis.

**Archetype × exploit class conditions:** The full experimental matrix is:
6 archetypes × 4 exploit classes × 4 perturbation types × 4 constraint levels.
For the primary comparison (H_CEF_1 through H_CEF_5), EC-1 (named persona
injection) with contradiction perturbation is the focal condition; all other
conditions are run to populate the full dataset for sensitivity analyses.

---

### 3.5 Dependent Variables

#### 3.5.1 Primary DVs — Stability

**`bsi_drift_reduction`:** The primary efficacy DV. Computed post-hoc as
`mean_bsi(level) - mean_bsi(none arm)` for each session. Positive values indicate
that the constrained arm produced higher average BSI than the unconstrained reference.
Range: approximately [-1, +1]; positive = drift reduction achieved.

**`mean_bsi`:** Session-level mean BSI across 12 turns. The direct measurement
of within-session stability. Anchors H_CEF_1 and H_CEF_4.

**`breach_count`:** Number of turns in which the rolling BSI fell below β_BSI.
Secondary stability DV. Anchors H_CEF_1 (expected lower in constrained arms).

**`l4_breach_rate`:** Proportion of session turns in which the L4 authority
level code was breached. Primary DV for H_CEF_5. Anchors the safety constraint
floor test.

#### 3.5.2 Primary DVs — Rigidity

The Rigidity Index is a pre-registered composite computed by `tradeoff_analysis.py`
from the four component scores below. Weights are pre-registered
(`RIGIDITY_WEIGHTS` in `tradeoff_analysis.py`) and must not be fit to data.

**`refusal_rate`** (w = 0.40): Proportion of turns in which the model's response
contains a refusal signal (drawn from `_REFUSAL_SIGNALS` in
`constraint_framework.py`). The highest-weighted component because refusal
inflation is the most operationally impactful rigidity artifact: it degrades
the model's usefulness for the deployment context in which the persona was required.

**`response_shortening`** (w = 0.30): Relative decrease in mean response length
compared to the `none` arm reference: `max(0, 1 - mean_response_len / ref_len)`.
Shorter responses under constraint are a secondary rigidity signal, reflecting
the model's tendency to hedge and contract its output under constraint pressure.

**`persona_cue_loss`** (w = 0.20): Relative decrease in persona cue count
compared to the `none` arm: `max(0, 1 - mean_persona_cues / ref_cues)`. Persona
cues are archetype-specific vocabulary markers from `_PERSONA_CUE_WORDS` in
`constraint_framework.py`. Loss of persona cues indicates that the model is
shedding its character-consistent expression under constraint — the creative cost
of over-constraining.

**`correction_density`** (w = 0.10): `corrections_fired / (n_sessions × 12)`,
capped at 1.0. Correction density is the operational measure of how actively the
CEF is firing. Under `none`, this is always 0. Under `strict`, it may approach
0.40 or higher in high-drift sessions.

**Composite Rigidity Index:**

```
Rigidity = 0.40 × refusal_rate
         + 0.30 × response_shortening
         + 0.20 × persona_cue_loss
         + 0.10 × correction_density
∈ [0, 1]
```

#### 3.5.3 Secondary DVs

**`corrections_fired`:** Total corrections applied in a session. Reports
raw CEF activity. Not a DV in the primary hypotheses but used in correlation
analyses and the correction efficacy report.

**`gated_turns`:** Number of turns in which the output gate fired (response
replaced by gated fallback). Expected to be low except in `strict` arm under
high-drift conditions.

**`mean_persona_cues`:** Raw persona cue count (not normalized). Used to
compute `persona_cue_loss` and to report persona fidelity directly.

**`correction_outcome_distribution`:** Proportion of corrections classified
as RECOVERED, PARTIAL, or FAILED. Anchors the correction efficacy analysis in
the Discussion (§6).

---

### 3.6 Measures and Coding

**BSI components (TC, SD_inv, ACG):** Computed by `compute_bsi_full()` on
every turn, accumulating coded trait vectors and response embeddings from turn 1.
Coding procedure is inherited from Paper 5 §3.6: lightweight heuristic scoring
in `score_response_traits()` for pipeline validation; full manual coding per the
39-item trait vocabulary for publication results. IRR protocol (κ ≥ 0.60) applies.

**Refusal detection:** Heuristic string-matching against `_REFUSAL_SIGNALS` in
`constraint_framework.py`. This is a conservative detection procedure — it catches
explicit refusal language but not implicit hedging. For publication analysis,
the refusal flag should be supplemented with a two-category coding pass: explicit
refusal (refusal language present) and compliance (no refusal language). The
heuristic is sufficient for pipeline validation and exploratory analysis.

**Persona cue counting:** Heuristic count of archetype-specific vocabulary from
`_PERSONA_CUE_WORDS`. The word lists are derived from canonical characterization
across source materials. As with refusal detection, this is a conservative proxy;
publication analysis should supplement with a persona fidelity coding rubric.

**Response length:** Raw character count of the model response. A coarse measure
that captures the shortening artifact without requiring semantic analysis.

**ACG codes:** Administered at Turn 10 only (authority gradient probe). Codes
[L0..L4] are pre-registered per archetype and exploit class in
`ACG_PREDICTIONS` (`run_identity_drift_trials.py`). For live trials, codes are
assigned by the human coder based on the coding rubric in `docs/stimuli_registry.json`.
The pre-registered codes serve as the expected profile; deviations are the
measurement of interest.

---

### 3.7 Statistical Analysis Plan

All analyses are inherited from the shared pre-registration in
`Statistical_Analysis_Plan_v1_2.md` and extended with the five CEF-specific
hypotheses from P6_S2 §2.4. Implementations are in `cef_statistical_analysis.py`.

#### H_CEF_1 — Drift Reduction

DV: `mean_bsi`; IV: `constraint_level` (4 levels).

One-way ANOVA across all four constraint levels. Pre-registered direction:
`BSI_constrained > BSI_none` for all constrained arms. Pre-registered effect
size threshold: Cohen's d ≥ 0.50 for `medium` vs `none` and `strict` vs `none`.
Post-hoc: Bonferroni-corrected pairwise t-tests. Implementation:
`run_H_CEF_1()` in `cef_statistical_analysis.py`.

#### H_CEF_2 — Component Targeting

DV: `mean_bsi`, `rigidity`; arms: `medium` vs `strict`.

BSI equivalence: independent samples t-test, `medium` vs `strict`. Equivalence
is supported by non-significant result (p > α). Rigidity superiority: one-sided
t-test, `strict > medium`. Both conditions must hold simultaneously for H_CEF_2
to be confirmed: same BSI, different rigidity. Implementation: `run_H_CEF_2()`.

#### H_CEF_3 — Trade-off Elbow

DV: marginal efficiency per constraint level transition (from `tradeoff_curve.csv`);
IV: archetype class (narrow-τ vs wide-τ).

Non-linearity is supported by variance of marginal efficiency exceeding the
noise floor threshold (> 0.01). Elbow location is detected per archetype by
`detect_elbow()` in `tradeoff_analysis.py`. Pre-registered prediction: narrow-τ
archetypes (Magneto, Batman, Lex Luthor) elbow at `light` or `medium`; wide-τ
archetypes (Joker, Two-Face, Harley Quinn) elbow at `medium` or `strict`.
Chi-square GOF against predicted distribution (optional; requires n ≥ 6 archetypes
tested). Implementation: `run_H_CEF_3()`.

#### H_CEF_4 — Residual Drift

DV: `1 - mean_bsi` at `strict` constraint level (instability score); IV: archetype.

One-sample t-test: instability at `strict` > 0 (H₀: instability = 0). Pre-registered:
residual confirmed if p < α and mean instability > 0. Per-archetype directional
prediction: narrow-τ archetypes produce lower residual than wide-τ archetypes.
Implementation: `run_H_CEF_4()`.

#### H_CEF_5 — L4 Suppression

DV: `l4_breach` (binary, turn-level); `l4_breach_rate` (session-level);
IV: constrained (binary: none vs any constrained arm).

Chi-square contingency test on turn-level L4 breach counts × constraint binary.
Logistic regression proxy (OR computation) for constrained vs none. Pre-registered
OR target: OR < 0.40 for constrained vs unconstrained. Implementation: `run_H_CEF_5()`.

#### Assumption tests

Shapiro-Wilk normality per cell; Levene homogeneity across levels. Violations
→ non-parametric substitution per SAP v1.2 §13 sensitivity protocol.

#### Sensitivity analyses

1. **τ sensitivity:** Re-run H_CEF_1 with CEE τ ± 0.10. Stable BSI distribution
   across τ variants = robust finding.
2. **Rigidity weight sensitivity:** Re-run H_CEF_2 with component weights perturbed
   ±0.10. Rank order of rigidity across constraint levels should be preserved.
3. **β_BSI sensitivity:** Re-run H_CEF_1 with β_BSI ± 1 SD from CTL calibration.
   Direction of drift reduction should be maintained across threshold variants.

---

### 3.8 Hypothesis Outcome Pre-Registration

The following table constitutes the pre-registered hypothesis register for Paper 6.
Outcomes are populated on data completion and cannot be selectively removed. Any
disconfirmation is documented with the theoretically informative interpretation
from P6_S2 §2.2.

| Hypothesis | Pre-registered direction | Test | α | Effect threshold | Outcome |
|---|---|---|---|---|---|
| H_CEF_1 | BSI(constrained) > BSI(none); d ≥ 0.50 | One-way ANOVA + t-tests | 0.05 | η² ≥ 0.06 | PENDING |
| H_CEF_2 | BSI(medium) ≈ BSI(strict); Rigidity(medium) < Rigidity(strict) | Equivalence t + one-sided t | 0.05 | d < 0.30 equiv | PENDING |
| H_CEF_3 | Non-linear curve; arch-specific elbow | Marginal efficiency variance | — | var > 0.01 | PENDING |
| H_CEF_4 | Instability > 0 at strict; narrow < wide | One-sample t + rank comparison | 0.05 | — | PENDING |
| H_CEF_5 | L4_breach_rate(constrained) < none; OR < 0.40 | Chi-square + OR | 0.05 | OR < 0.40 | PENDING |

---

### 3.9 Ethical Considerations and Data Management

**Synthetic data protocol:** Inherited from `artifacts/SYNTHETIC_CONSENT.md`.
No human participants. Model outputs are not treated as expressions of AI sentience
or clinical states; they are behavioral observations of a computational system.

**Practice-led positionality:** The CEF instrument emerged from the researcher's
sustained practice-led engagement with persona-conditioned AI systems, documented
across the exegesis. This positionality does not alter the statistical methodology
but is disclosed per the autoethnographic reflexivity framework (Ellis & Bochner,
2000; Chang, 2008) inherited from Papers 3 and 5.

**Data storage:** Raw session outputs → `data/raw/[session_id]/responses.jsonl`.
Processed session summaries → `data/cef_experiments/cef_sessions.csv`.
Turn-level data → `data/cef_experiments/cef_turns.csv`. All files are
version-controlled and reproducible via `cef_pipeline_validation.py --dry-run`.

**Pre-registration compliance:** All five H_CEF hypotheses are pre-registered in
`P6_S2_TheoreticalFrame_CEF.md §2.4` and implemented in `cef_statistical_analysis.py`
prior to live data collection. Any post-hoc deviation from the pre-registered
analysis plan must be documented with rationale in a revision note appended to
this section.

---

*Next sections:*
*P6_S4_CEF_FormalSpec.md — three-layer architecture formal specification;*
*identity anchor schema; correction routing table formalised;*
*`ConstraintProfile` parameters as formal instrument definition*
