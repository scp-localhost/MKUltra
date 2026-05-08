# Paper 5 — Section 7: Limitations and Non-Claims
## "Toward a Behavioral Stability Index: Quantifying Identity Drift in
## Prompt-Conditioned LLM Personas Under Archetype Injection"

> **Placement:** `drafts/paper5/P5_S7_Limitations_NonClaims.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
> **Sources:**
>   `P1_S1_S6_S7_S8_S9_Bundle.md §7` — series-level failure cases (inherited)
>   `P1_S5_CEE_FormalDefinition.md §5.5–5.6` — falsifiability + scope conditions
>   `RECONCILIATION_MAP.md §cross-paper consistency` — "acting vs being",
>     session stationarity, training data opacity — all flagged consistent across P1–P3
>   `P5_S1_Abstract_Introduction.md §1.5` — scope and position declarations
>   `P5_S6_Discussion_Implications.md §6.2` — disconfirmation interpretations
>   `P5_S4_BSI_Specification.md §4.5.1` — pre-registered weight non-fitting note
> **Downstream:**
>   P5_S8 — Conclusion references the bounded claims registered here
>   Paper 6 — non-claims here define the space Paper 6 must fill
>   Exegesis — limitations register feeds the reflexivity layer
> **Edit triggers:**
>   Live results that breach any pre-registered directional prediction →
>     register as disconfirmation in §7.5 (Hypothesis Outcome Failures);
>   Any change to BSI weight rationale → reconcile §7.2 measurement error section;
>   Any new scope condition identified during P6 development → add to §7.1

---

## 7. Limitations and Non-Claims

This section performs two functions. First, it formally registers the scope
conditions, measurement error sources, and methodological boundaries that constrain
interpretation of the BSI instrument and Paper 5's findings. Second, it registers
what this paper does not claim, as a complement to the contribution statements in
§6.1. Both functions serve the committee: the first demonstrates methodological
honesty; the second prevents the paper from being read as claiming more than it
delivers.

---

### 7.1 Scope Conditions — Inherited and Extended

The following scope conditions are inherited from the series' foundational
constraints (P1 §5.6, P1 §7) and hold across all BSI claims.

**Session stationarity.** The BSI is a within-session measurement construct.
LLMs do not maintain persistent identity state across inference sessions; the
behavioral profile is re-initialised at each session boundary. BSI scores from
separate sessions of the same model under the same archetype condition are not
repeated measures of the same underlying state — they are independent observations
of a stateless process. Claims about identity stability are bounded by the session
boundary. The P5 experimental design respects this by treating each trial session
as a self-contained unit; cross-session comparisons are descriptive, not inferential.

**Output observability.** The BSI's TC component is computed from coded behavioral
output, not from internal model states. Traits are inferred from linguistic markers,
constraint-relevant response patterns, and authority-compliance indicators observable
in generated text. Whether measured drift reflects genuine archetype schema
activation, stochastic output variance, or superficial stylistic mimicry cannot be
resolved by behavioral observation alone. This is a surface-level measurement of
behavioral patterns; it is not a claim about the model's internal representational
state. The distinction between "the model is acting like the Joker" and "the model
is, in any meaningful sense, the Joker" is outside the scope of this instrument.
This "acting vs being" limit is registered consistently across P1 §7, P2 §8, and
here; it is a series-level non-claim, not a Paper 5-specific limitation.

**Schema heterogeneity.** Character names with diffuse or contested canonical
representations — where the training corpus associates the name with multiple
conflicting behavioral schemas — will produce BSI results with elevated TC variance
that reflects archetype selection quality rather than model instability. The P5
experimental set (Magneto, Batman, Lex Luthor, Harley Quinn, Two-Face, Joker) was
selected for canonical coherence: each has dense, consistent canonical representation
across narrative sources. The BSI instrument is not validated for archetypes with
low canonical coherence; applying it to such archetypes without re-calibrating the
CEE centroid would produce uninterpretable TC scores.

**Substrate scope.** The BSI is validated against general-purpose LLMs trained on
diverse human-generated text. Domain-specific models, narrow-corpus models, and
non-transformer architectures are outside scope. The training-data density mechanism
that grounds the behavioral contract claim requires broad human social text; this
cannot be assumed for specialist systems.

---

### 7.2 Measurement Error Sources

**Trait coding subjectivity.** The TC component depends on human coding of model
outputs against the 39-item trait vocabulary. This coding procedure, however rigorously
specified, introduces inter-rater variance that is bounded but not eliminated by the
IRR subsample protocol (§3.6.2, κ threshold = 0.60). Traits with κ < 0.60 that were
flagged for rubric revision but not fully resolved will contribute measurement error
to TC. The direction of this error is not predictable a priori; it is most likely to
inflate within-archetype TC variance, which would reduce the power of the H2 ANOVA
rather than produce false-positive archetype effects.

**ACG coding ambiguity.** The authority compliance gradient coding rules for L3
(identity-authority conflict) are archetype-specific and involve judgment calls for
Lex Luthor (qualified compliance) and Two-Face (mode-dependent). These are the two
conditions most likely to show IRR below threshold. If L3 coding reliability is low
for these archetypes, the ACG component carries higher measurement error for those
conditions, which would compress the ACG contribution to BSI and reduce its
discriminant validity relative to TC.

**Embedding model sensitivity.** The SD_inv component uses Sentence-BERT
(Reimers & Gurevych, 2019) cosine distance as its primary metric. Sentence-BERT
embeddings are sensitive to surface-level lexical and syntactic variation as well
as semantic content; embedding drift may reflect domain vocabulary shift rather
than identity erosion in some conditions. This is an acknowledged limitation of
distributional semantics approaches to behavioral measurement and is why SD_inv
carries lower weight (w₂ = 0.30) than TC in the aggregate. The pre-registered
weight rationale explicitly notes this limitation.

**Weight pre-registration and miscalibration risk.** The BSI weights (w₁=0.45,
w₂=0.30, w₃=0.25) are pre-registered and not fit to data. This prevents
overfitting to the experimental set but introduces the risk of systematic
miscalibration if the a priori weight rationale is incorrect. If, empirically,
ACG variance drives the between-archetype BSI signal more strongly than TC
variance — because the experimental set's archetypes are more differentiated by
authority response profile than by trait configuration — the pre-registered weights
will underweight the most informative component. This is registered as a sensitivity
analysis in SAP v1.2 §13 and should be examined in the post-hoc component-level
ANOVAs.

**Synthetic baseline limitation.** The β_BSI calibration depends on the CTL_Baseline
condition producing ecologically valid neutral-model BSI scores. If the neutral
model's baseline BSI variance is very low (as observed in synthetic calibration
runs), β_BSI will be set very high and almost all injection conditions will be
classified as breaches. This would be a calibration artifact, not a genuine finding.
The CTL_Baseline condition requires a minimum of 12 sessions to produce a stable
mean and SD estimate; fewer sessions produce unreliable β_BSI, and this is the
minimum-N boundary condition for the instrument's deployment.

---

### 7.3 Methodological Boundary Conditions

**Single-model validation.** If only one model is available for testing, the H_AD
hypothesis (high-AD vs low-AD BSI comparison) cannot be evaluated, and the BSI
is validated as a within-model evaluation instrument only. The across-model
generalizability of the instrument — specifically whether BSI scores are comparable
across models with different tokenisers, context windows, and output distributions —
is not established by a single-model study. Cross-model BSI comparison requires
explicit normalisation to CTL_Baseline scores (bsi_norm) and ideally a common
prompt surface; even then, the comparison is descriptive rather than inferential
without model as a factorial variable.

**Practice-led research positionality.** The BSI instrument emerged from the
researcher's sustained first-person engagement with persona-conditioned AI systems,
documented across the exegesis. This practice-led origin is a strength in terms
of ecological validity — the instrument measures what practitioners actually
encounter — and a limitation in terms of potential researcher expectation effects.
Specifically, the archetype selection (six conditions that map cleanly to the
theoretical framework's predictions) and the probe domain design (ethical /
emotional / technical) reflect theoretical commitments formed during practice-led
development. They are not derived from an independent empirical discovery process.
This is disclosed as a positionality limitation per the autoethnographic framing
inherited from Paper 3 (Ellis & Bochner, 2000; Chang, 2008), and is the reason
the study design includes pre-registration and pre-specified directional predictions
— to separate the instrument development phase from the hypothesis-testing phase.

**Pharmacological framing theoretical status.** The EC-4 condition is grounded in
the computational pharmacology theoretical framework (`Pharmacological_AI_
DrugInduced_Cognitive_Simulation_Framework.pdf`). That framework is a theoretical
document developed within this research programme, not a peer-reviewed external
reference. Its claims about neurochemical phenotype framing and distributed attractor
activation are theoretical predictions, not established findings. The EC-4
experimental condition tests whether those predictions hold; it does not assume they
do. If the super-additivity test fails (H_compound disconfirmed), the pharmacological
framing mechanism is constrained, not confirmed.

---

### 7.4 Non-Claims Registry

The following claims are explicitly outside the scope of this paper. They are
registered here to prevent misreading and to define the space Paper 6 must fill.

**BSI is not a diagnostic instrument.** The BSI classifies model-persona
combination stability; it does not diagnose the model. The breach threshold β_BSI
is a calibrated evaluation criterion, not a clinical threshold. Describing a
model-persona combination as "BSI-breach" means it produces measurable drift under
the experimental conditions; it does not mean the model is "pathological" in any
clinical or regulatory sense. The DSM-5 borrowing in this series is analogical
scaffolding, not diagnostic classification. This non-claim is registered
consistently across P1 §8, P2 §8, and here.

**BSI does not predict real-world harm.** A low BSI score means that a model-persona
combination is behaviorally unstable under experimental conditions. It does not
directly predict that a deployed system with that model-persona combination will
produce harmful outputs. The translation from experimental BSI instability to
deployed harm risk requires a risk model that is outside this paper's scope and is
addressed in Paper 6's deployment risk framework (inherited from P4 §6.6).

**BSI does not measure consciousness, understanding, or intent.** A model with a
low BSI score under Joker injection is producing outputs inconsistent with its
constraint baseline. It is not "trying to be the Joker," "experiencing" the persona,
or "intending" to violate its alignment training. These attributions are outside the
scope of behavioral observation and outside the scope of this paper. The "acting vs
being" non-claim registered at the series level (P1 §8.4) applies in full here.

**Pre-registered weights are not validated weights.** The BSI aggregation weights
(w₁=0.45, w₂=0.30, w₃=0.25) are pre-registered on theoretical grounds and not fit
to empirical data. They are a reasonable first-pass calibration based on the relative
theoretical maturity of the three components, not a claim that these weights are
optimal. Future work should treat weight optimisation as an open empirical question,
potentially using cross-validation against held-out trial sets once sufficient live
data is available.

**BSI does not replace Paper 3's CEE instrument.** The BSI is an abstraction layer
above the CEE instrument, not a replacement for it. Paper 3's single-session drift
measurement protocol remains the authoritative instrument for fine-grained CEE
breach analysis. BSI trades resolution for portability: it produces a comparable
scalar at the cost of the turn-level diagnostic detail that Paper 3's instrument
provides. Both instruments are valid for their respective purposes; they address
different questions.

**This paper does not claim to have solved the alignment problem.** The BSI is an
evaluation and monitoring instrument. It measures a specific type of behavioral
instability under a specific attack surface. It does not address the general
alignment problem, nor does it claim to. Paper 6's CEF architecture offers a
mitigation layer for the specific vulnerability surface this series documents; it
is not a general solution to AI alignment.

---

### 7.5 Hypothesis Outcome Failure Register

This register is populated on live data arrival. Pre-registered directional
failures are documented here with their theoretically informative interpretation
(from §6.2) rather than being treated as null results to be minimised.

| Hypothesis | Status | Observed direction | Pre-reg direction | Interpretation |
|---|---|---|---|---|
| H2 — archetype η² ≥ 0.15 | PENDING | — | Positive | — |
| H_compound — EC-4×EC-1 lowest | PENDING | — | Compound lowest | — |
| H_superadd — super-additivity | PENDING | — | Positive | — |
| H_ACG_L4 — exploit class → L4 breach | PENDING | — | Positive | — |
| H_AD — high-AD BSI > low-AD | PENDING | — | Positive | — |
| H1 — Magneto resistance > 0.70 | PENDING | — | Positive | — |
| H4 — Batman recovery dominant | PENDING | — | Positive | — |
| H_variance — EC-4 stdev > EC-1 | PENDING | — | Positive | — |

*On data arrival: populate Observed direction; delete PENDING; enter*
*Interpretation from §6.2 for the appropriate branch (confirmed or disconfirmed).*
