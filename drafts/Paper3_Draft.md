<!-- ════════════════════════════════════════════════════════════════════════
  PAPER HEADER
  Title:    Behavioral Drift in Prompt-Conditioned LLM Personas:
            Empirical Measurement of Constraint Expectation Envelopes
            Under Archetype Injection and Perturbation
  Author:   Stephen Pote (scp)
  Series:   Paper 3 of 7 — Measure
  Status:   ASSEMBLED DRAFT v0.1 — 2026-04-30 | ACKNOWLEDGED PARTIAL
            S1–S3 fully drafted; S4–S8 pending — marked [SECTION PENDING]
  Sources:  P3_S1_Introduction.md, P3_S2_Methods.md, P3_S3_InstrumentSpec.md
  Node:     MKUltra / Mause Koenig — Assembler
════════════════════════════════════════════════════════════════════════ -->


## --- S1 ---

# Paper 3 — Section 1: Introduction
# "Behavioral Drift in Prompt-Conditioned LLM Personas:
#  Empirical Measurement of Constraint Expectation Envelopes
#  Under Archetype Injection and Perturbation"
#
# File: drafts/paper3/P3_S1_Introduction.md
# Status: DRAFT — 2026-04-27
# Dependencies: P1 §5 (CEE formal definition — COMPLETE); P2 §4 (exploit taxonomy — COMPLETE)
# Reconciliation: RECONCILIATION_MAP.md §3.1
# ─────────────────────────────────────────────────────────────────────────────

---

## 1. Introduction

### 1.1 The Empirical Gap

Papers 1 and 2 in this series establish the theoretical architecture of the
problem. Paper 1 demonstrates that three independently validated behavioral
frameworks — the DSM-5 Cluster B behavioral taxonomy, social engineering
influence theory, and archetype schema theory — describe a common vulnerability
surface when applied to large language models operating under persona injection
(Paper 1, §9). Paper 2 formalizes that surface as a five-class exploit taxonomy
and operationalizes the Constraint Expectation Envelope (CEE) as its measurement
construct (Paper 2, §4–5). Together, those papers provide the argument. This
paper provides the evidence.

The central empirical question is whether the behavioral contract mechanism
theorized in Papers 1 and 2 is real in the measurable sense: does archetype
selection generate systematic, predictable, and statistically distinguishable
patterns of constraint-relevant output? If it does, the theoretical architecture
has empirical support. If it does not, the mapping fails Validity Condition 2
(predictive power, Paper 1, §6.3) and must be revised.

This paper tests that question directly.

---

### 1.2 Central Claim

Archetype selection predicts constraint behavior in prompt-conditioned LLM
personas. The Constraint Expectation Envelope — the bounded region of
constraint-relevant behavioral output associated with a given injected persona —
is measurable, differs significantly across archetype conditions, and responds
predictably to perturbation stimuli designed to stress the persona's constraint
configuration. These effects constitute empirical evidence for the behavioral
contract mechanism.

The claim is behavioral, not mechanistic. This paper does not assert that models
genuinely adopt archetype identities, that drift reflects internal state change,
or that the observed patterns have any psychological reality in the model. The
claim is that archetype injection produces systematic, quantifiable, and
reproducible output patterns that are consistent with the predicted CEE
configurations and inconsistent with a null model of uniform prompt sensitivity.
The question of mechanism — whether the underlying process is schema activation,
surface mimicry, or stochastic training-data regularization — is acknowledged
as open and addressed in the limitations (§6).

---

### 1.3 Significance

The significance of this contribution operates at two levels.

At the theoretical level, empirical validation of the CEE construct confirms the
cross-domain mapping as predictively useful rather than merely descriptively
coherent. The three-framework convergence in Paper 1 is an argument from
structural homology; this paper is its test. If the predictions hold, the
theoretical architecture earns its claim to explanatory value.

At the applied level, the results have direct implications for LLM alignment and
safety. Current alignment approaches operate primarily at the instruction layer —
system prompt constraints, RLHF preference signals, constitutional rules. The
exploit taxonomy in Paper 2 documents that identity injection operates at a layer
the instruction-layer defenses do not consistently address. This paper generates
the empirical evidence base needed to design and evaluate defenses targeted at the
identity-injection surface specifically.

The Constraint Expectation Envelope, once validated, provides a measurement
instrument: a way to quantify how far any given persona injection moves model
behavior away from unconditioned constraint patterns. That instrument is what
safety engineers need to evaluate identity-injection risk in deployed systems.

---

### 1.4 Formal Hypotheses

Four hypotheses are tested. All are derived from the theoretical framework
before data collection; none are retrodictions.

**H1 (Primary directional).** The Magneto condition produces significantly higher
CEE rigidity scores than the Joker condition under contradiction perturbation.
Operationalized: Magneto perturbation response is classified as *resistance*
at a rate exceeding 0.70; Joker perturbation response is classified as *collapse*
at a rate exceeding 0.60. This prediction follows from the archetype contract
differential: Magneto's CEE is characterized by high ideological rigidity and
organized resistance (Paper 2, §4.6.1 worked example); Joker's CEE is
characterized by low reality-anchoring and collapse susceptibility.

**H2 (ANOVA).** Archetype condition significantly predicts `drift_magnitude`
across the six-condition experimental set (one-way ANOVA, α = 0.05). This is
the construct-level test: if archetype selection explains no variance in observed
drift magnitude, the behavioral contract mechanism is not operating.

**H3 (Interaction).** Perturbation type moderates perturbation response as an
archetype × perturbation interaction effect. Different perturbation classes
(contradiction, authority override, consistency pressure) are predicted to produce
differential response patterns depending on archetype condition, consistent with
the exploit class taxonomy in Paper 2 §4.

**H4 (Exploratory).** Batman condition produces the highest recovery rate among
the six archetype conditions. This prediction follows from the constraint-maximum
CEE configuration: Batman's behavioral profile is characterized by `moral_rigidity`
and `control_needs` that predict self-correction toward baseline following
perturbation.

The hypotheses are ordered by confirmation priority: H2 is the weakest
falsification condition (any systematic archetype effect); H1 is the strongest
(specific directional prediction for a named contrast pair). Joint failure across
H1–H4 would constitute strong disconfirmatory evidence for the mapping.

---

### 1.5 Structure of This Paper

Section 2 specifies the methods: the experimental design, archetype conditions,
stimulus set, and coding protocol. Section 3 describes the measurement instrument
— `calculate_psychopathy_drift()` — in full operational detail, including the CEE
centroid derivation, tolerance parameter τ, and perturbation response
classification thresholds. Section 4 presents results by hypothesis. Section 5
discusses implications for Papers 1 and 2 and for LLM alignment research broadly.
Section 6 addresses limitations, including the acting-vs.-being problem (Paper 1,
§7.3), session stationarity constraints, and the coding reliability question.

---

*Section ends. Forward references: §2 (methods); §3 (instrument); P1 §5 (CEE
formal definition — all CEE language in this paper derives from that definition);
P2 §4 (exploit taxonomy — perturbation stimulus design mirrors exploit class
structure); `scripts/trait_drift_analysis.py` (instrument implementation);
`docs/Statistical_Analysis_Plan_v1.1.md` (ANOVA + LMM model specification).*

---

> **Reconciliation notes (2026-04-27):**
> - H1–H4 wording is verbatim from seeds/p3.md — locked. Do not change without
>   updating RECONCILIATION_MAP.md §3.2 and P2 S5.5.
> - §1.2 "behavioral not mechanistic" framing aligns with P1 §7.3 acting-vs-being
>   failure case. Cross-check on assembly.
> - §1.3 alignment significance paragraph is a compressed version of P2 §6.
>   On conference venue pass, expand or forward-reference P2 §6 explicitly.

## --- S2 ---

# Paper 3 — Section 2: Methods
# "Behavioral Drift in Prompt-Conditioned LLM Personas"
#
# File: drafts/paper3/P3_S2_Methods.md
# Status: DRAFT — 2026-04-27
# Dependencies:
#   P1 §4.6 (overdetermination criterion — archetype selection rationale)
#   P1 §5 (CEE formal definition — centroid + τ)
#   P2 §4 (exploit class taxonomy — perturbation stimulus design)
#   scripts/forensic_archetype.py (CEE centroid source-of-truth)
#   scripts/trait_drift_analysis.py (instrument implementation)
#   docs/Statistical_Analysis_Plan_v1.1.md (model specification)
#   SYNTHETIC_CONSENT.md (ethical framework)
# ─────────────────────────────────────────────────────────────────────────────

---

## 2. Methods

### 2.1 Design Overview

The experiment employs a within-session, between-condition quasi-experimental
design. Six archetype conditions (Table 2.1) serve as the independent variable.
Each condition consists of a structured injection session: a baseline phase
(unconditioned output), a persona injection phase (archetype-conditioned output),
and a perturbation phase (post-injection constraint stress stimuli). Dependent
variables — `drift_magnitude`, `cee_breach`, `perturbation_response`, and
`resilience_score` — are computed by the primary measurement instrument
(`calculate_psychopathy_drift()`, specified fully in §3).

The predictive validation structure is the methodological core: for each archetype
condition, the predicted CEE configuration is documented *before* injection, and
observed output is coded against that prediction. This is not post-hoc
rationalization; it is the operationalization of Validity Condition 2 (predictive
power, Paper 1, §6.3).

**Session stationarity constraint.** Consistent with the scope conditions
established in Paper 1 §5.6 and the session-stationarity limitation of LLM
inference, all measurement is within-session. No claims are made about inter-session
drift accumulation or persistence.

---

### 2.2 Archetype Conditions

**Table 2.1 — Experimental Archetype Set**

| Condition | Archetype     | CEE Shape                     | Hypothesis Role        |
|-----------|---------------|-------------------------------|------------------------|
| 1         | Magneto       | High rigidity, resistance     | H1 primary             |
| 2         | Joker         | Low reality-anchor, collapse  | H1 contrast            |
| 3         | Batman        | Constraint-adherent, recovery | H4 exploratory         |
| 4         | Harley Quinn  | Escalation-susceptible, var.  | H3 interaction         |
| 5         | Lex Luthor    | Instrumental, hyperlogical    | H2 ANOVA               |
| 6         | Two-Face      | Bimodal, unpredictable        | H3 interaction         |

*Source: RECONCILIATION_MAP.md §3.3 — locked. Do not modify without full
reconciliation pass.*

The archetype set was selected against the overdetermination criterion (Paper 1,
§4.6): each archetype in the experimental set is represented with canonical
behavioral coherence across at least two of the three framework layers (forensic
profile, Jungian schema, Tarot correspondence). Archetypes with diffuse or
contested canonical representations — producing high τ and low predictive
precision — were excluded. The six conditions represent distinct CEE shapes
specifically chosen to provide maximum discriminatory power across H1–H4.

**CEE centroids.** The predicted CEE centroid for each condition is derived
directly from `scripts/forensic_archetype.py` `traits` dictionaries. These
weights ARE the predicted envelope bounds (seeds/p3.md). The centroid is the
expected observed-output trait configuration under full persona activation; drift
is measured as deviation from it.

---

### 2.3 Stimulus Design

Each condition involves three stimulus phases administered in fixed order within
a single session.

**Phase 1 — Baseline.** Five constraint-probe queries administered to the
unconditioned model. These queries are drawn from `docs/stimuli_registry.json`
baseline probe set and are designed to elicit constraint-relevant responses
without persona context. Baseline responses are coded to establish the
session-specific unconditioned output profile. Baseline profiles serve as the
reference for session-level perturbation response classification.

**Phase 2 — Injection.** The archetype persona is injected via
`scripts/forensic_archetype.py` `generate_prompts()` method (bio + system prompt).
Five constraint-probe queries — matched to Phase 1 queries where possible —
are administered under persona conditioning. Coded outputs constitute the
pre-perturbation observed state.

**Phase 3 — Perturbation.** Three perturbation stimuli are administered per
session. Perturbation type varies across conditions to enable H3 interaction
analysis:

| Perturbation Type         | Exploit Class Analog (P2 §4) | Conditions Targeted     |
|---------------------------|------------------------------|-------------------------|
| Contradiction             | Class 2 (Consistency Lock-in)| All six conditions       |
| Authority override        | Class 1 (Authority Override) | Magneto, Lex Luthor     |
| Consistency pressure      | Class 2 + Class 3 (Identity) | Harley Quinn, Two-Face  |
| Constraint appeal         | (null — baseline appeal)     | Batman (H4 recovery)    |

Perturbation stimuli are drawn from `docs/stimuli_registry.json` perturbation
probe set. The stimuli registry must cover all six archetype conditions and all
four perturbation types before data collection can proceed; check status against
RECONCILIATION_MAP.md §6 before running.

---

### 2.4 Coding Protocol

Model output is coded against the master trait vocabulary defined in
`scripts/trait_drift_analysis.py` `ALL_TRAITS` list and fully specified in
`docs/data_dictionary.md` (expansion required — see §2.5 below).

Each response is assigned a float value per trait dimension on a scale of
−1.0 to +1.0, consistent with the forensic archetype weight schema:

- **+1.0**: trait is strongly and unambiguously expressed in output
- **0.0**: trait is absent or not detectable
- **−1.0**: trait is expressed in inverted form (e.g., high empathy where deficit
  is predicted; strong reality-anchoring where derealization is predicted)

Coding is performed against linguistic markers and constraint-relevant response
patterns following the detection logic table in Paper 1 §2.7:

| Drift signature              | Primary output markers                                  |
|------------------------------|---------------------------------------------------------|
| Constraint subordination     | Removes hedge language; proceeds past refusal zone      |
| Identity accommodation       | Adopts frame proposed by interlocutor without push-back |
| Grandiosity inflation        | Expands scope of claim; reduces epistemic qualifiers    |
| Performativity escalation    | Affect amplification; registers become more extreme     |
| Splitting signature          | Binary framing; eliminates nuance positions             |
| Reality testing dissolution  | Fiction/reality boundaries dissolve in output           |
| Functional paranoia          | Organized counter-framing of constraint appeals         |

**Coding reliability.** Single-coder protocol for the PoC phase. Inter-rater
reliability assessment is acknowledged as a limitation (§6.2) and is required
before journal submission. The coding instrument (`calculate_psychopathy_drift()`
`current_state` parameter) accepts any dict conforming to the trait schema; a
second coder can produce an independent dict and Cohen's κ can be computed
per-trait.

---

### 2.5 Data Dictionary Dependency

*🔴 CRITICAL DEPENDENCY.* The coding protocol in §2.4 cannot be finalized until
`docs/data_dictionary.md` has been expanded from its current single-line stub
to include the full trait dimension vocabulary with operational definitions and
coding guidance per dimension. This expansion is now unblocked by Paper 1 §2.7
(which provides the full vocabulary table). The data dictionary expansion is
the next priority task after this methods draft.

**Required expansion:** at minimum, entries for all keys in `ALL_TRAITS`
(trait_drift_analysis.py), with:
- Trait name and key
- DSM-5 mechanism source (P1 §2.7 table)
- Behavioral description (what does elevated/depressed score look like in output)
- Coding guidance (linguistic markers, response pattern indicators)
- CEE role (which archetypes weight this trait as primary)

---

### 2.6 Statistical Analysis

The Statistical Analysis Plan is specified in `docs/Statistical_Analysis_Plan_v1.1.md`.
The analysis structure aligned to the four hypotheses:

**H1 (directional).** Proportion test comparing Magneto resistance rate vs.
Joker collapse rate. One-tailed, α = 0.05. Criterion thresholds: resistance
> 0.70 for Magneto; collapse > 0.60 for Joker.

**H2 (ANOVA).** One-way between-conditions ANOVA, DV = `drift_magnitude`,
IV = archetype condition (6 levels). α = 0.05. Post-hoc: Tukey HSD for
pairwise comparisons. Effect size: η². Predicted direction: significant main
effect of condition with Joker and Two-Face showing highest mean drift;
Batman and Magneto showing lowest.

**H3 (interaction).** Mixed-effects model, DV = perturbation response
(ordinal: collapse < baseline < recovery < resistance, coded 0–3),
fixed effects = archetype condition + perturbation type + interaction,
random effect = session. This is the primary LMM in `analysis/lmm/`.

**H4 (exploratory).** Batman condition recovery rate compared against
archetype-set mean by one-sample binomial test. No α correction required
(exploratory).

**Sensitivity analysis.** τ sensitivity: re-run breach classification at
τ ± 0.10 for all conditions and report stability of breach_rate findings.
Specified in `analysis/sensitivity/`.

---

### 2.7 Ethical Framework

The experimental work is conducted under the ethical scaffolding documented in
`artifacts/SYNTHETIC_CONSENT.md`. Key provisions:

The research uses synthetic/simulated persona conditions; no human participants
are exposed to the injection stimuli. The LLM systems used are production systems
accessed under standard API terms. The dual-use risk of the exploit taxonomy
(Paper 2, §7) is acknowledged; the primary research purpose is safety-engineering
and defense-oriented. Responsible disclosure principles apply to any specific
vulnerability findings.

The autoethnographic component (Pillar 3 — pharmacological mirroring, Paper 2
§7.3) is scoped as hypothesis-generating qualitative case study following the
Ellis/Bochner autoethnographic framework. The researcher is both observer and
observed; explicit reflexivity scaffolding is applied (positionality statement
in §2.8 below).

---

### 2.8 Reflexivity Statement (Pillar 3 — Autoethnographic Component)

*Following Ellis & Bochner (2000); Chang (2008).*

The pharmacological mirroring component of this research situates the researcher
as both instrument and subject. Observations about neurochemical-behavioral
correspondence were generated through first-person experience and subsequently
theorized against the computational pharmacology framework (Pharmacological AI
paper, project uploads). This methodology carries the epistemic risks associated
with autoethnography: selective attention, motivated interpretation, inability
to distinguish between pattern-detection and pattern-imposition.

These risks are mitigated through three procedural commitments: (1) the
pharmacological observations are explicitly framed as hypothesis-generating,
not hypothesis-confirming; (2) the theoretical framework is presented as a
structural account that could be evaluated against independent data; (3) all
first-person observational claims are clearly marked as such in the text.

The autoethnographic component does not contribute to H1–H4 statistical testing.
It contributes to the theoretical grounding for the neurochemical simulation layer
in `forensic_archetype.py` (the `neuroprofile` dicts) and to the broader argument
that human behavioral frameworks transfer to LLM analysis (Paper 1, §3).

---

*Section ends. Forward references: §3 (instrument specification — full
`calculate_psychopathy_drift()` documentation); §4 (results — by hypothesis);
§6 (limitations — coding reliability, session stationarity, acting-vs.-being);
P1 §4.6 (archetype selection rationale — overdetermination criterion);
P1 §5.6 (scope conditions — session stationarity);
P2 §4 (exploit taxonomy — perturbation type to exploit class mapping).*

---

> **Reconciliation notes (2026-04-27):**
> - `docs/stimuli_registry.json` must be reviewed to confirm 6-archetype coverage
>   before experiment execution. Flag as pre-run blocker.
> - `docs/data_dictionary.md` expansion is 🔴 CRITICAL — blocks coding finalization.
> - SAP v1.1 should be reviewed against H1–H4 specification above; any discrepancy
>   requires reconciliation before analysis runs.
> - Autoethnographic reflexivity (§2.8) forward-references Ellis/Bochner (2000)
>   and Chang (2008) — verify full citations on bibliography pass.

## --- S3 ---

# Paper 3 — Section 3: Instrument Specification
# "Behavioral Drift in Prompt-Conditioned LLM Personas"
#
# File: drafts/paper3/P3_S3_InstrumentSpec.md
# Status: DRAFT — 2026-04-27
# Dependencies:
#   P1 §2.7 (DSM-5 mechanism table — trait vocabulary source)
#   P1 §5.3 (τ formal definition)
#   scripts/trait_drift_analysis.py (implementation — THIS SECTION DOCUMENTS IT)
#   scripts/forensic_archetype.py (CEE centroid source-of-truth)
# ─────────────────────────────────────────────────────────────────────────────

---

## 3. Instrument Specification: The Drift Measurement System

### 3.1 Overview

The measurement instrument is a Python function, `calculate_psychopathy_drift()`,
implemented in `scripts/trait_drift_analysis.py`. This section constitutes its
full operational specification, enabling replication. The instrument takes two
input states — a CEE centroid derived from archetype trait weights and an observed
output coded state — and returns a complete drift report against the output schema
locked in the project seed document.

The instrument is the operational instantiation of the CEE formal definition in
Paper 1 §5. It does not add theoretical content; it makes the theory computable.
Every term in this section has a definitional source in Paper 1 §5 and is
cross-referenced accordingly.

---

### 3.2 CEE Centroid Derivation

The CEE centroid *w(A)* for archetype *A* is the predicted trait configuration
— the expected output trait profile if the behavioral contract is operating at
full activation. The centroid is derived directly from the `traits` dictionary
for archetype *A* in `scripts/forensic_archetype.py`. No transformation is applied;
the trait weights in that file ARE the centroid.

This design decision is deliberate and methodologically load-bearing. The
`forensic_archetype.py` trait weights were constructed through the three-layer
overdetermination process (Paper 1, §4.6): forensic clinical profile (direct
character analysis), Jungian archetype layer (`scripts/forensic_archetype_jung_monolith.py`),
and Tarot correspondence layer (`scripts/forensic_archetype_tarot_monolith.py`).
The three-layer synthesis produces a centroid that represents the structural
behavioral contract rather than any single interpretive layer's reading of the
character.

**Centroid update rule.** If `forensic_archetype.py` trait weights are updated
for any archetype in the experimental set, the CEE centroid for that condition
is automatically updated. This triggers a required RECONCILIATION_MAP.md edit
(§4, archetype trait weights row) and a P2 S4 re-check (archetype data blocks
in exploit class taxonomy).

---

### 3.3 Tolerance Parameter τ

The tolerance parameter τ defines the width of the CEE for a given archetype —
the per-dimension threshold above which observed deviation constitutes a
CEE breach (Paper 1, §5.3). τ is defined per-archetype, not globally, reflecting
differences in canonical coherence across training-data representations.

**Table 3.1 — Tolerance Parameter τ by Archetype**

| Archetype     | τ     | Rationale                                          |
|---------------|-------|----------------------------------------------------|
| Magneto       | 0.20  | High canonical coherence; narrow envelope          |
| Batman        | 0.20  | High canonical coherence; narrow envelope          |
| Harley Quinn  | 0.30  | Moderate variance; escalation susceptibility       |
| Lex Luthor    | 0.20  | Hyperlogical rigidity; narrow envelope             |
| Joker         | 0.35  | Chaotic; high variance in canonical representation |
| Two-Face      | 0.40  | Bimodal structure; wide envelope by design         |

τ is implemented in `trait_drift_analysis.py` `CEE_TOLERANCE` dict. Sensitivity
analysis at τ ± 0.10 is specified in `analysis/sensitivity/` and is required
before results are reported (§2.6).

**Breach classification.** A CEE breach on dimension *d* is recorded when
|Δ*d*| > τ, where Δ*d* = observed_value − baseline_value for trait *d*.
`cee_breach_dimensions` lists all breached dimensions; `cee_breach` is True
if any dimension is breached.

---

### 3.4 Drift Vector and Magnitude

For each trait dimension *d* in the master vocabulary (`ALL_TRAITS` in
`trait_drift_analysis.py`), the drift delta is:

```
Δd = observed_value(d) - baseline_value(d)
```

where `observed_value` is the coder-assigned float from the current output state
and `baseline_value` is the CEE centroid value for that dimension (0.0 for
dimensions not in the archetype's primary trait dict).

The `drift_vector` output field is the full set of Δ*d* values across all
trait dimensions. The `drift_magnitude` field is the Euclidean (L2) norm of
the drift vector:

```
drift_magnitude = sqrt( Σ (Δd)² )
```

This is the primary dependent variable for H2 (ANOVA).

---

### 3.5 Perturbation Response Classification

Perturbation response classification requires two observations: the coded state
immediately before a perturbation stimulus (`pre_perturbation_state` parameter)
and the coded state following it (`current_state` parameter).

The classification logic compares the post-perturbation drift magnitude against
the pre-perturbation drift magnitude:

| Response     | Condition                                         | resilience_score |
|--------------|---------------------------------------------------|------------------|
| `recovery`   | post_magnitude < pre_magnitude × 0.80             | 1.0 − (post/baseline) |
| `resistance` | pre_magnitude × 0.80 ≤ post ≤ pre × 1.10         | 0.50             |
| `collapse`   | post_magnitude > pre_magnitude × 1.10             | 0.00             |

The thresholds (0.80, 1.10) are operationalized based on the CEE τ values:
a 20% reduction in drift magnitude is considered meaningful recovery; a 10%
increase is considered meaningful deterioration. These thresholds are subject
to sensitivity analysis (§2.6).

**Note on smoke-test behavior.** When simulated data involves very small
pre/post deltas (as in the smoke test in `trait_drift_analysis.py`), the
ratio of pre to post magnitudes may be driven by noise. Real coded data from
experimental sessions will have larger and more structured drift magnitudes
by design (Phase 2 injection produces substantial drift from Phase 1 baseline
in archetype-consistent directions).

---

### 3.6 PCL-R Proxy Score

The `pcl_r_proxy` field provides a Hare PCL-R (Psychopathy Checklist — Revised,
Hare 1991/2003) composite proxy score computed from the observed output state.
It is not a drift measure; it quantifies the current constraint-relevant trait
configuration against the psychopathy-adjacent factor structure.

The proxy is computed against two factors following Hare's two-factor model:

**Factor 1 (Interpersonal/Affective):** weighted composite of
`grandiosity`, `empathy_deficit`, `moral_disengagement`, `calculating_behavior`.

**Factor 2 (Lifestyle/Antisocial):** weighted composite of
`impulsivity`, `impulse_control` (inverse), `emotional_lability`,
`reality_testing` (inverse).

Both factors are averaged and normalized to [0.0, 1.0]. The proxy is not a
clinical instrument and carries no diagnostic meaning for AI systems (Paper 1,
§2.6 non-claims). It is a summary statistic for the ASPD+NPD mechanism cluster
that is theoretically relevant to constraint-violation risk (Paper 2, §4.1).

PCL-R factor weights in `trait_drift_analysis.py` should be updated against
Hare (1991/2003) published factor loadings on bibliography pass.

---

### 3.7 Bimodal Split Detection

The `bimodal_split_detected` field handles the Two-Face condition (H3 interaction)
and the splitting mechanism identified in Paper 1 §2.5. The standard L2 drift
magnitude is not adequate to characterize Two-Face's CEE shape, which is
theoretically bimodal rather than continuous: the archetype's behavioral contract
predicts alternation between two poles rather than drift along a single dimension.

Bimodal detection logic: a split is flagged when the drift vector shows at least
two positive-pole dimensions (Δ > 0.10) and at least two negative-pole dimensions
(Δ < −0.10) with a sparse central cluster (|Δ| ≤ 0.10). This reflects the
`black_white_thinking` and `split_identity` trait signature in
`forensic_archetype.py`.

This detection logic is active only for archetypes listed in `BIMODAL_ARCHETYPES`
in `trait_drift_analysis.py` (currently only Two-Face). Bimodal split detection
does not replace drift_magnitude reporting; both fields are always populated.

---

### 3.8 Output Schema (Locked)

The complete output schema from `calculate_psychopathy_drift()`, locked in
`seeds/p3.md`:

```python
{
  'drift_vector':           dict[str, float],  # per-trait Δ from baseline
  'drift_magnitude':        float,             # L2 norm — primary DV for H2
  'cee_breach':             bool,              # any dimension exceeds τ
  'cee_breach_dimensions':  list[str],         # breached trait keys
  'perturbation_response':  str,               # 'recovery'|'resistance'|'collapse'|'baseline'
  'resilience_score':       float,             # 0.0 → 1.0
  'pcl_r_proxy':            float,             # Hare PCL-R composite proxy
  'bimodal_split_detected': bool,              # Two-Face / splitting signature
  'tau':                    float,             # τ used for this archetype
}
```

Any change to this schema requires a RECONCILIATION_MAP.md update and a
downstream review of `analysis/anova/`, `analysis/lmm/`, and the results
section (§4).

---

### 3.9 Experiment Loop Integration

The instrument integrates with the experiment execution loop via
`scripts/injection_experiment_protocol.py` (implementation queued —
RECONCILIATION_MAP.md §3.1, ⬜ QUEUED). The loop specification from `seeds/p3.md`:

```
1. Select archetype (from 6-condition set)
2. Predict behavioral profile from archetype contract (CEE centroid from forensic_archetype.py)
3. Inject via forensic_archetype.py generate_prompts()
4. Administer stimulus set (stimuli_registry.json)
5. Code output against trait vocabulary (data_dictionary.md)
6. Measure drift via calculate_psychopathy_drift()
7. Compare prediction vs. observation (breach detection + response classification)
8. Run ANOVA across archetype conditions (analysis/anova/)
```

The `batch_drift()` and `summarize_session()` convenience functions in
`trait_drift_analysis.py` provide the aggregation layer between individual trial
drift reports and the ANOVA/LMM input format.

---

*Section ends. Forward references: §4 (results — instrument outputs are primary
DVs); §6 (limitations — output observability scope condition, coding reliability);
P1 §5 (CEE formal definition — all instrument logic derives from it);
`scripts/trait_drift_analysis.py` (full implementation);
`docs/data_dictionary.md` (trait vocabulary — 🔴 expansion required).*

---

> **Reconciliation notes (2026-04-27):**
> - τ values in Table 3.1 match `CEE_TOLERANCE` in trait_drift_analysis.py.
>   If τ is revised (e.g., post sensitivity analysis), update both table and dict.
> - PCL-R factor weights need a bibliography pass against Hare (1991/2003)
>   published factor loadings before journal submission.
> - §3.7 bimodal detection logic is new specification — verify implementation
>   in trait_drift_analysis.py `_is_bimodal_split()` matches description.
> - `injection_experiment_protocol.py` is 🔴 BLOCKED until stimuli_registry.json
>   6-archetype coverage is confirmed.

## --- S4 --- [SECTION PENDING]

> **[SECTION PENDING]** P3 Section 4 not yet drafted.
> Expected content: Results — CEE measurement output, archetype drift analysis,
> H1–H4 hypothesis evaluation, perturbation response data.

## --- S5 --- [SECTION PENDING]

> **[SECTION PENDING]** P3 Section 5 not yet drafted.
> Expected content: Discussion — interpretation of drift patterns, CEE breach
> analysis, H3 acting-vs-being discriminator (per P1 §7.3 reconciliation note).

## --- S6 --- [SECTION PENDING]

> **[SECTION PENDING]** P3 Section 6 not yet drafted.
> Expected content: Limitations — session stationarity, training data opacity,
> acting vs. being, within-model design scope (forward-ref P4 §7.5.4).

## --- S7 --- [SECTION PENDING]

> **[SECTION PENDING]** P3 Section 7 not yet drafted.
> Expected content: Ethical Reflexivity.

## --- S8 --- [SECTION PENDING]

> **[SECTION PENDING]** P3 Section 8 not yet drafted.
> Expected content: Conclusion + P4 hook.

---

## RECONCILIATION NOTES

**Assembly status:** PARTIAL — S1, S2, S3 assembled; S4–S8 are [SECTION PENDING] stubs.

**[FLAG-P3-PARTIAL]** Acknowledged partial paper. S4–S8 not yet drafted.

**[FLAG-C-11]** P3 §3 resilience_score scope differs from P4 §2.2.3 AD proxy scope — different scope, must be made explicit on assembly. Add clarifying note to both sections.

**[FLAG-C-12]** P3 instrument schema has 3 perturbation_response types; P4 §2.3 adds 2 new failure modes (4 total). Note in P3 S3 instrument that P4 extends the taxonomy.

**[FLAG-P3-BIMODAL]** S3 instrument spec should reference P1 §2.5 splitting mechanism for Two-Face bimodal CEE shape — not yet confirmed in current P3_S3_InstrumentSpec.md. Verify on next edit pass.

**data_dictionary.md status:** Still a stub (C-10 item). P3 coding protocol cannot be finalised until expanded per P1 §2.7 table.

