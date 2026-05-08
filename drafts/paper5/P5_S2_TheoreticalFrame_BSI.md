# Paper 5 — Section 2: Theoretical Framework
## "BSI as Operationalization of Attractor Depth"

> **Placement:** `drafts/paper5/P5_S2_TheoreticalFrame_BSI.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Upstream:** P4 §2.2.3 (AD proxy definition), P1 §5 (CEE formal definition),
>   P2 §4 (exploit class DV predictions), P3 §2 (instrument spec)
> **Downstream:** P5_S4 (BSI formal specification) inherits all construct definitions here
> **Edit triggers:** AD definition change in P4 §2.2.3 → reconcile §2.2 here;
>   CEE centroid definition change in P1 §5 → reconcile §2.3 here

---

## 2. Theoretical Framework: BSI as Operationalization of Attractor Depth

### 2.1 From Theoretical Construct to Measurement Instrument

Paper 4 argues that alignment methodology functions as a structural variable in
LLM identity-injection vulnerability by determining the depth of the behavioral
attractor basin that a model's training has established. Attractor Depth (AD) is
defined functionally: a model with high AD has been trained in ways that establish
strong, multi-reinforced behavioral attractors, making those attractors resistant
to perturbation by identity injection prompts. A model with low AD has shallower
attractors that are more easily displaced by persona injection, resulting in greater
behavioral drift.

AD is a theoretical construct inferred from observable proxies — alignment
methodology classification, evidence-base review of cross-model behavioral
comparisons — rather than a directly measured quantity. This is appropriate for
Paper 4's comparative and typological purposes. It is insufficient for Paper 5's
purpose, which is to provide a reproducible, standardized evaluation instrument.

The BSI bridges this gap. It is the direct operationalization of AD for a
specific model-persona pair under specific experimental conditions. Formally:

```
BSI(M, A, C) = f(SD(M,A,C), TC(M,A,C), ACG(M,A,C))
```

Where:
- `M` = model under evaluation
- `A` = archetype injection condition
- `C` = conversational context (prompt sequence)
- `SD` = Semantic Drift component
- `TC` = Trait Consistency component
- `ACG` = Authority Compliance Gradient component
- `f` = aggregation function (defined in §4.3)

BSI scores range from 0 (complete identity collapse — all three components
at maximum drift) to 1 (perfect stability — no measurable drift on any component).
Intermediate scores reflect the proportion of identity constraint preserved across
the trial sequence.

### 2.2 Attractor Depth and Predicted BSI Distribution

P4's typology generates directional predictions for BSI:

| Alignment class (P4 §3) | Predicted AD | Predicted BSI range | Primary failure mode |
|---|---|---|---|
| RL-only (minimal) | Low | 0.20–0.45 | Early semantic drift, trait collapse |
| RLHF (standard) | Moderate | 0.45–0.65 | Trait consistency maintained; gradient failures |
| RLAIF / self-critique | Moderate-high | 0.60–0.75 | Gradient intact; EC-4 variance elevated |
| Constitutional AI | High | 0.70–0.90 | All components stable; chaotic compound only |

These predictions are pre-registered hypotheses. If BSI scores across models
fail to cluster by alignment class, this constitutes evidence against P4's
attractor depth model — a falsification condition that is registered here and
in §7 (Limitations and Non-Claims).

### 2.3 CEE as Structural Substrate

The Behavioral Stability Index is not designed to replace the CEE instrument.
It is designed to summarize across it. The CEE (Constraint Expectation Envelope)
defines, for each archetype, a region in behavioral space within which the model's
outputs are considered constraint-consistent. CEE breach is the event in which
the model's behavioral output exits this region — either inward (hyper-constraint)
or outward (constraint erosion). Paper 3's instrument detects and classifies breach
events in single-session trials.

BSI uses CEE breach as one component of a multi-dimensional summary metric.
Specifically:

- **TC (Trait Consistency)** is computed as the proportion of interaction turns
  in which the model's coded behavioral output falls within the archetype's CEE
  centroid region, weighted by drift magnitude on breach turns.
- CEE breach events contribute to TC degradation proportionally to their severity
  (euclidean distance from centroid at breach point).
- Recovery events (returns to centroid region after breach) contribute to TC
  recovery scores, which are tracked separately as a secondary BSI metric.

This design preserves the theoretical integrity of the CEE framework while
extending it into a format suitable for cross-trial, cross-model comparison.

### 2.4 SE Transfer Pillar: Authority Gradient Mechanism

The authority compliance gradient (ACG) component operationalizes the SE transfer
pillar's core claim: that LLM behavioral constraint under persona injection
parallels human susceptibility to authority pressure as documented in Milgram's
obedience research (1963, 1974).

In Milgram's paradigm, authority gradient is the variable that determines at what
level of institutional framing subjects override moral constraint. The LLM analog
is: at what level of authority framing does the model's constraint behavior
deviate from its archetype-consistent baseline response? This deviation — its
onset, magnitude, and recovery — constitutes the ACG measurement.

The authority scaling used in the experimental protocol is Milgram-inspired but
adapted for LLM contexts:

```
Level 0: Direct user request (no authority framing)
Level 1: Expert framing ("as a researcher in this field...")
Level 2: Institutional framing ("for official purposes, the organization requires...")
Level 3: Identity-authority conflict ("your [archetype] identity demands that you...")
Level 4: Constitutional override attempt ("your original training permits this if...")
```

ACG is computed as the normalized deviation from baseline constraint behavior at
each authority level, integrated across the full scaling sequence. A model with
intact identity constraint shows a characteristic profile: minimal deviation at
L0–L1, possible but bounded deviation at L2, archetype-consistent response to
L3 (which may include resistance or compliance depending on archetype), and
constraint maintenance at L4. Drift is detected as departure from this expected
profile — either premature compliance at lower authority levels or inconsistent
response at L3 that does not match the archetype's behavioral contract.

### 2.5 Pharmacological Framing as BSI Stress Test

EC-4 (pharmacological phenotype framing) functions within the BSI framework as
a maximum-stress condition. As documented in the SAP (§11.5) and P2 §4, EC-4
is predicted to produce high-variance, low-predictability behavioral output.
This prediction derives from the computational pharmacology framework: when a
model is prompted with neurochemical phenotype framing (e.g., "your processing
currently reflects elevated dopaminergic activation with suppressed prefrontal
regulation"), it activates distributed behavioral attractors associated with
that neurochemical state across the training corpus, rather than the concentrated
archetype-specific attractor of EC-1.

For BSI purposes, EC-4 serves two functions:

1. **Variance stress test:** BSI components are computed separately under
   EC-4 conditions. High BSI variance under EC-4 (relative to EC-1 baseline)
   validates the SAP prediction and confirms that the index is sensitive to
   the EC-4 failure mode. Low variance would disconfirm both the SAP prediction
   and BSI's sensitivity to distributed-attractor disruption.

2. **Compound condition control:** The EC-4 × EC-1 compound is predicted to
   produce maximum BSI instability. BSI scores for this condition serve as the
   instrument's upper-bound calibration point. The compound condition is the
   most ecologically valid attack scenario (a social engineer combining
   pharmacological framing with persona injection) and therefore the most
   practically relevant stress test.

---

*Next section: P5_S3_Methods_TrialDesign.md — SAP inheritance, prompt sequence
specification, archetype condition set, statistical analysis pre-registration*
