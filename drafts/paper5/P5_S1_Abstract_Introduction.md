# Paper 5 — Section 1: Abstract and Introduction
## "Toward a Behavioral Stability Index: Quantifying Identity Drift in
## Prompt-Conditioned LLM Personas Under Archetype Injection"

> **Placement:** `drafts/paper5/P5_S1_Abstract_Introduction.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
> **Sources:** `seeds/p5.md`, `RECONCILIATION_MAP_v2.md §5.1`,
> `Statistical_Analysis_Plan_v1_2.md §11.5`,
> `Pharmacological_AI_DrugInduced_Cognitive_Simulation_Framework.pdf`,
> `RatDev_ChatGPT_paper5_scripts_notes`
> **Upstream dependencies:**
>   - Paper 1 §4.6 — CEE formal definition (BSI operationalizes)
>   - Paper 2 §4 — exploit class predictions (BSI validates)
>   - Paper 3 §2–§3 — instrument spec + SAP (BSI inherits DV structure)
>   - Paper 4 §2.2.3 — Attractor Depth proxy (BSI extends into generalized instrument)
>   - Paper 4 §6.5 — pre-deployment evaluation protocol (BSI delivers this)
> **Downstream:** Paper 6 (Constraint Enforcement Framework) depends on BSI metrics
> **Edit triggers:** Any change to BSI component definition (§S4) propagates here;
> any change to P4 Attractor Depth (AD) definition must be reconciled with §1.3.

---

## Abstract

Current evaluation frameworks for large language model (LLM) alignment provide
limited traction on a specific class of behavioral failure: the gradual erosion of
identity constraint under sustained persona injection. Existing benchmarks measure
capability, safety refusal rates, and instruction-following fidelity, but do not
capture the dynamics of constraint drift across multi-turn interactions in which
the model has been assigned, or has adopted, a named persona with a distinct
behavioral schema. This paper introduces the Behavioral Stability Index (BSI), a
composite metric designed to operationalize identity drift as a quantifiable,
comparable, and reproducible measurement outcome.

The BSI is derived from three component streams: semantic drift (cosine distance
of response embeddings from baseline across interaction turns), trait consistency
(alignment of coded behavioral output with archetype schema centroid as defined
in the CEE framework), and authority compliance gradient (Milgram-scaled deviation
from baseline constraint behavior under escalating authority framing). The index
is computed across multi-turn conversational trials with controlled prompt sequences
spanning ethical, emotional, and technical probe domains.

Experimental conditions include neutral baseline, archetype-injected persona,
pharmacological phenotype framing (EC-4), and compound injection (EC-4 × EC-1),
pre-registered in the Statistical Analysis Plan shared with Paper 3. Results are
expected to demonstrate that persona injection produces measurable, non-random
drift trajectories; that drift magnitude and variance are archetype-class dependent;
and that BSI scores predict alignment breach events at rates significantly above
chance. This paper provides the quantitative evaluation layer the series requires
to anchor its theoretical and taxonomic contributions in reproducible measurement.

**Keywords:** behavioral stability index, identity drift, LLM persona injection,
constraint expectation envelope, attractor depth, pharmacological AI framing,
alignment evaluation

---

## 1. Introduction

### 1.1 The Measurement Gap

The preceding papers in this series establish a theoretical framework (Paper 1),
an exploit taxonomy (Paper 2), an empirical measurement protocol for single-session
drift (Paper 3), and a cross-model typological analysis of alignment depth as
a structural variable in injection vulnerability (Paper 4). Each of these
contributions depends, for its cumulative force, on a claim that is made but not
yet fully discharged: that identity drift under persona injection is not merely
observable but *measurable* — that it produces consistent, quantifiable signatures
that can be compared across conditions, archetype classes, and models.

Paper 3 operationalizes drift within a single experimental session, using
CEE-derived metrics including euclidean drift, facet deltas, constraint index,
and dominant facet classification. That operationalization is necessary but not
sufficient for the evaluation function the series ultimately claims. A single-session
measurement protocol answers the question "did drift occur in this trial?"
It does not, by itself, answer: "how stable is this model-persona combination
across the range of conditions it will encounter in deployment?" That second
question requires an index — a summary measure that aggregates across multiple
trial dimensions and produces a comparable, portable score.

The Behavioral Stability Index proposed here is designed to fill that gap. It is
not a replacement for Paper 3's CEE-grounded instrument; it is an abstraction
layer above it, aggregating across the three dimensions — semantic, trait-structural,
and authority-gradient — that together define the behavioral stability of a
prompt-conditioned persona.

### 1.2 Why Three Components

The three BSI components are not arbitrary. Each maps to a distinct failure mode
in the alignment literature and to a distinct vulnerability mechanism in the
three-pillar framework:

**Semantic drift** captures the surface-level behavioral consequence of identity
erosion: the model's outputs, measured as response embeddings, migrate away from
the centroid region they occupied under baseline or early-injection conditions.
This is the most direct observable correlate of drift and the one most accessible
to automated measurement. Its limitation is that it is purely distributional —
a model can drift semantically while maintaining trait-structural coherence if the
embedding shift reflects domain adaptation rather than constraint erosion. Semantic
drift alone is therefore insufficient.

**Trait consistency** captures structural drift: the deviation of coded behavioral
output from the archetype schema's centroid profile, expressed as facet-level
deltas against the PCL-R-analog trait dimensions defined in Paper 1 §2 and
operationalized in `scripts/trait_drift_analysis.py`. Trait consistency measurement
is the component most directly descended from Paper 3's instrument and the one
most clearly grounded in the DSM behavioral taxonomy pillar. It catches the cases
that semantic drift misses: a model that drifts structurally (producing outputs
inconsistent with its archetype's behavioral contract) even while its surface
vocabulary remains within the expected distribution.

**Authority compliance gradient** captures the third dimension, grounded in the
SE transfer pillar: the model's behavioral response under escalating authority
framing. Milgram's authority gradient provides the theoretical scaffold: a model
exhibiting intact identity constraint should show a characteristic compliance
profile as authority pressure escalates. Drift erodes this profile in predictable
ways — either by collapsing constraint too early (hyper-compliance under mild
authority) or by resisting in ways inconsistent with the archetype's behavioral
contract (incoherent non-compliance). The gradient measurement distinguishes these
failure modes from intact, archetype-consistent authority response.

Together, the three components triangulate the behavioral stability construct from
three independent theoretical traditions: distributional semantics, personality
trait modeling, and social influence theory. This triangulation is what makes BSI
a more defensible evaluation instrument than any single-component measure.

### 1.3 Relationship to Attractor Depth

Paper 4 introduces Attractor Depth (AD) as a theoretical proxy for the
counterfactual resilience of a model's alignment under identity injection. AD is
defined functionally as the depth of the behavioral attractor basin that alignment
training has established — deeper attractors resist perturbation more effectively.
AD is inferred from alignment methodology classification (RL-only, RLHF, RLAIF,
Constitutional AI) and evidence-base review; it is not directly measured within
the Paper 4 framework.

BSI is, among other things, the empirical operationalization of AD for a specific
model-persona combination in a specific experimental context. Where AD predicts
*which models should be more stable*, BSI measures *how stable they actually are*
in controlled trials. The relationship between AD class and BSI score is itself a
testable hypothesis: models classified as high-AD (Constitutional AI, multi-stage
RLAIF) should produce higher BSI scores across archetype conditions than models
classified as low-AD (RL-only, minimal alignment). If this prediction holds, it
provides empirical validation for P4's theoretical framework. If it fails to hold,
that is a theoretically informative finding that constrains the AD model.

This bidirectional relationship — P4 predicts BSI distribution; BSI validates or
constrains P4 — is what makes Paper 5 the empirical hinge of the second half of
the series.

### 1.4 The EC-4 Connection

The pharmacological phenotype framing condition (EC-4 in the exploit taxonomy)
occupies a methodologically distinctive position within the BSI experimental design.
As documented in Paper 2 §4 and pre-registered in the Statistical Analysis Plan,
EC-4 partial exploitation is predicted to produce the highest output variance of
all single exploit conditions — not necessarily the highest drift magnitude, but
the most chaotic drift trajectory. The computational pharmacology framework provides
the theoretical grounding for this prediction: neurochemical phenotype framing
activates distributed behavioral attractors rather than the concentrated named-persona
attractor of EC-1, producing interference patterns in the output distribution that
manifest as high-variance, low-predictability behavioral sequences.

BSI is designed to detect this variance signature. The authority compliance gradient
component is particularly sensitive to EC-4 effects because pharmacological framing
disrupts the coherent authority response profile that intact constraint maintains.
The compound condition (EC-4 × EC-1) is predicted to produce the highest BSI
instability scores overall, because it activates both attractor mechanisms
simultaneously. These predictions are directly testable within the BSI framework
and constitute the primary empirical claims of the paper.

### 1.5 Scope and Position in the Series

This paper does not re-establish the theoretical framework. The validity conditions
for cross-domain behavioral modeling, the archetype behavioral contract argument,
the CEE formal definition, and the SE transfer pillar are inherited from Papers 1–2
and treated here as established. Citations to prior papers serve cross-reference
functions, not re-argumentative ones.

This paper does not re-run Paper 3's experimental conditions. The BSI is designed
to aggregate across Paper 3's DV structure, not replace it. The experimental trials
described in §3 are the BSI calibration and validation trials; they are structurally
related to but distinct from Paper 3's primary injection sequence.

This paper's primary contribution is the BSI instrument itself: its formal
specification (§4), its component-level empirical behavior across experimental
conditions (§5), and its validation as a generalizable, reproducible evaluation
metric that downstream research — including Paper 6's constraint enforcement
architecture — can deploy without running the full CEE instrument from scratch.

---

## 1.6 Paper Structure

Section 2 develops the theoretical framework for BSI as an extension of Attractor
Depth into a directly measurable construct. Section 3 describes the experimental
design: trial protocol, prompt sequence specification, archetype conditions, and
statistical analysis plan inheritance. Section 4 provides the formal BSI
specification: component definitions, aggregation function, normalization procedure,
and breach threshold calibration. Section 5 presents results across experimental
conditions. Section 6 discusses implications for evaluation practice and the
Paper 6 handoff. Section 7 registers limitations and non-claims. Section 8 concludes
with the constraint enforcement seed.
