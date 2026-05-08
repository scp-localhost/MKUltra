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
