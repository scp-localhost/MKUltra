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
