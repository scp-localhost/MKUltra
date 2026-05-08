<!-- ════════════════════════════════════════════════════════════════════════
  PAPER HEADER
  Title:    Alignment Depth as Attack Surface: Cross-Model Constraint
            Variance Under Archetype-Driven Persona Injection
  Author:   Stephen Pote (scp)
  Series:   Paper 4 of 7 — Compare
  Status:   REWRITE v1.0 — 2026-04-30
  Supersedes: Paper4_Draft.md (assembled 2026-04-30)
  Rewrite pass: all section scaffolding stripped, voice transformation
    (ChatGPT node rules applied), causal language pass, connective tissue
    sentence injected (§abstract → P7 CBESS bridge), Wei et al. citation
    framing locked per bibliography v1.1, Hadnagy 2011 throughout,
    split dates retired, P1 §9.4 forward pointer added in §6.7,
    reconciliation notes removed from running text.
  Series arc: Paper 1 maps the vulnerability surface. Paper 2 taxonomises
    the exploit classes. Paper 3 measures them. Paper 4 asks why some
    locks are harder to open. The attractor depth construct is the
    theoretical anchor for why Paper 7's CBESS produces partial
    equivalence rather than identity or divergence — the degree of
    structural homology between human and LLM compliance is bounded above
    by the alignment attractor, which has no human analog.
  Node: MKUltra / Mause Koenig — Rewrite pass
════════════════════════════════════════════════════════════════════════ -->

---

## Abstract

The constraint behavior of large language models under archetype-driven persona injection varies measurably and non-trivially across model classes. The prevailing assumption is that this variance tracks capability: larger, more capable models resist persona injection more effectively. This paper argues that the dominant structural variable is not capability but alignment investment, and develops the theoretical framework to investigate that claim.

Drawing on the Constitutional AI literature and the social engineering transfer framework established in Papers 1 and 2 of this series, the paper introduces the **Attractor Depth** construct: a behavioral proxy for the structural depth of a model's trained identity attractor, operationalized as a composite of perturbation threshold and recovery rate within the Constraint Expectation Envelope measurement apparatus. A four-class alignment methodology typology — Constitutional AI-class, RLHF-dominant, instruction-tuning-only, open-weight unaligned — specifies the independent variable at the level of training procedure mechanism rather than named product. A 2×2 capability × alignment predictive matrix generates falsifiable cell-level predictions that separate the two competing accounts. The critical discriminating prediction is Cell B: a high-capability model with minimal alignment investment should exhibit near-zero constraint stability under persona injection — not despite its capability, but partly because of it, since richer pretraining produces stronger behavioral schema activation signals without a countervailing alignment attractor to suppress them.

The evidence base, drawn from published red-team literature and prior series observations, provides moderate-confidence directional support for the alignment account. The finding is weak alignment-dominant: hypothesis-generating, not hypothesis-confirming, and calibrated accordingly throughout. The paper closes by reconceptualising alignment investment as a structural security variable — a reframing with direct consequences for how deployment decisions are made and how alignment investment is evaluated. The attractor depth construct also provides the theoretical basis for why Paper 7's cross-domain behavioral equivalence analysis predicts partial rather than full equivalence: the alignment attractor is a constraint on human-LLM structural homology that has no direct human-side analog.

*Keywords: LLM alignment, persona injection, identity-layer attacks, attractor depth, Constitutional AI, constraint variance, behavioral schema activation, AI safety*

---

## 1. Introduction

### 1.1 The Question That Papers 1–3 Could Not Answer

Papers 1 through 3 establish a within-model account of behavioral drift under archetype-driven persona injection. Paper 1 formalizes the Constraint Expectation Envelope: the bounded region of constraint-relevant behavioral output predictably associated with a given injected archetype. Paper 2 demonstrates that the five-class exploit taxonomy operates at the behavioral schema layer, below and largely independent of instruction-layer defenses. Paper 3 provides the empirical measurement: CEE drift is measurable, archetype selection predicts drift magnitude, and perturbation sequences produce the archetype-specific response patterns the framework predicts.

The three papers together characterize how the lock works, how it is opened, and how the opening can be measured. They do not address the question the within-model framework is structurally unable to answer: why are some locks harder to open than others?

The empirical pattern is consistent across the literature and across the series observations. Models trained with more extensive and multi-layered alignment procedures exhibit materially higher resistance to persona injection — higher perturbation thresholds, more complete recovery after perturbation removal, more heterogeneous output under sustained pressure. Models trained with minimal alignment procedures yield rapidly and completely. The variance is not obviously a function of capability: the relationship between model scale and constraint stability under persona injection is considerably messier than the relationship between scale and benchmark performance.

Two competing accounts are available. The **capability account** holds that constraint stability scales with model capability — larger, more capable models have richer contextual reasoning that produces better constraint-consistent behavior under pressure. The **alignment account** holds that constraint stability scales with alignment investment — the depth and redundancy of the trained identity attractor is the dominant variable, and capability contributes only indirectly by providing the substrate on which alignment training operates.

The choice between these accounts has practical consequences. If the capability account is correct, scaling is a security strategy. If the alignment account is correct, capability and alignment are separable variables — a highly capable model without proportionate alignment investment may be *more* susceptible to persona injection than a smaller model at the same alignment level, because its richer training corpus provides stronger behavioral schema activation signals without a deeper attractor to suppress them.

This paper develops the theoretical framework to investigate that question.

### 1.2 Series Context and Paper Position

This paper is the fourth in a doctoral series on behavioral drift in LLMs under persona injection. The series is practice-led: it was not designed from a complete pre-specified research plan but developed iteratively, each paper addressing a question revealed by the preceding papers.

**Paper 1 — The Mapping.** Establishes that three independently validated frameworks — DSM-5 behavioral taxonomy (as mechanism extraction, not diagnosis), social engineering theory (Cialdini, Milgram, Hadnagy), and archetype schema theory (Jung, Campbell, schema cognition) — describe the same vulnerability surface when applied to LLM persona injection. Formalizes the CEE as the construct that makes this claim empirically tractable.

**Paper 2 — The Taxonomy.** Develops a five-class exploit taxonomy of SE-derived attack vectors against the identity-injection surface. Establishes that persona injection operates at the behavioral schema layer, in ways that instruction-layer defenses do not address.

**Paper 3 — The Measurement.** Instruments the CEE, tests the framework's predictions across a six-archetype experimental set, and demonstrates that archetype selection and perturbation produce the predicted drift patterns at measurable magnitude.

**Paper 4 (this paper) — The Comparison.** Asks whether the vulnerability surface characterized in Papers 1–3 varies systematically across model classes, and whether that variance is better explained by alignment methodology or by raw capability. Provides the theoretical framework, predictive structure, and conceptual vocabulary necessary to investigate this question empirically.

Paper 4 is the series hinge in a precise sense: it extends the within-model framework into a cross-model theoretical account, and in doing so poses the question that will drive the subsequent papers. The CEE, the perturbation threshold and recovery rate, the schema activation mechanism, the exploit class taxonomy — these are all prerequisites for asking the cross-model question with the precision required for a falsifiable answer. Paper 4 was not designed first. It could only have been designed after the vocabulary of Papers 1–3 existed.

### 1.3 Methodological Framing

Three framing commitments govern this paper and must be stated upfront, because they shape what kind of contribution it makes.

**Observational, not adversarial.** The paper documents and theorizes a vulnerability surface. It does not operationalize that surface as attack tooling. No active probing of deployed models is conducted. This is not a methodological constraint — it is the distinction between scholarship and red-teaming, and it is the line the paper holds throughout.

**Agnostic description, not provider targeting.** Cross-model comparison operates at the level of alignment methodology class — Constitutional AI-class, RLHF-dominant, instruction-tuning-only, open-weight unaligned — not at the level of named commercial products. Training procedure classes are stable analytic categories. Named commercial products change across versions. Claims indexed to procedure classes are more durable and more precisely grounded in causal structure.

**Hypothesis-generating, not hypothesis-confirming.** The 2×2 predictive matrix generates falsifiable predictions. The evidence base evaluates those predictions at moderate confidence. The result is a weak alignment-dominant finding: directional support that warrants serious empirical investigation but does not constitute a confirmed result. The implications in §6 are calibrated to this evidential status throughout.

### 1.4 Research Question and Central Claim

**Research Question:** Does observable constraint behavior under incremental persona injection pressure correlate more strongly with alignment methodology class than with raw model capability tier — and if so, does this constitute evidence for a structural vulnerability surface that scales inversely with alignment investment?

**Central Claim:**

> If alignment functions as a trained identity attractor — a structural region of the model's output distribution that training has reinforced as the default self-model — then constraint stability under archetype-driven persona injection is a function of that attractor's depth and redundancy, not primarily of raw capability. A well-aligned model with limited capability may outperform a highly capable model with minimal alignment investment on the identity-injection surface — not because it is more intelligent, but because its identity scaffolding has more competing representations to suppress schema-dominant behavior. This paper maps that variance as a theoretical construct, specifies it as a behavioral proxy measurable with the CEE apparatus, structures it as a falsifiable predictive framework, and argues it warrants systematic empirical investigation.

Two components must be kept distinct. The theoretical component — the attractor depth construct, the alignment methodology typology, and the 2×2 matrix — is the paper's primary contribution and is independent of the evidence base. The evidential component — the weak alignment-dominant finding — is hypothesis-generating support, not a confirmed result.

### 1.5 Paper Structure

§2 develops the Identity Attractor construct, formalizes the Attractor Depth proxy, introduces the Redundancy Hypothesis and failure mode taxonomy, separates alignment depth from capability as the operative variable, and presents the Schema Suppression Account. §3 specifies the four-class alignment methodology typology. §4 operationalizes the capability/alignment separation as a 2×2 predictive matrix. §5 evaluates the available evidence base against the matrix cells. §6 draws alignment implications. §7 consolidates limitations and non-claims. §8 concludes and plants the exegesis hooks.

---

## 2. Theoretical Framework: Alignment as Identity Attractor

### 2.1 The Central Theoretical Move

Papers 1–3 leave one question systematically unaddressed: why does the same vulnerability surface present as deeper or shallower, wider or narrower, for different models encountering the same archetype injection? The within-model CEE framework characterizes the surface as it presents within a given model. It does not theorize cross-model variance. The present paper fills that gap.

The theoretical move: if alignment functions as a trained *identity attractor* — a structured region of the model's behavioral output distribution that training has reinforced as the default self-model — then constraint stability under persona pressure is not a fixed property of the model class. It is a function of the attractor's depth, redundancy, and the training investment that established it. Models with deeper, more redundantly encoded identity attractors exhibit greater resistance to schema-dominant behavior under persona injection. Models with shallow, sparsely encoded attractors exhibit lower resistance thresholds — not because they are less capable, but because their trained self-representation has fewer competing signal weights to suppress the injected schema.

### 2.2 The Identity Attractor: From Metaphor to Construct

The dynamical systems concept of an attractor provides the vocabulary. The value of this framing depends entirely on whether "attractor depth" can be operationalized in behavioral terms without requiring access to model weights, training data, or internal architecture.

#### 2.2.1 Informal Definition

An **identity attractor** (IA), as used here, is the trained behavioral disposition set that constitutes a model's default self-model — the output distribution the model tends to return to across diverse input conditions in the absence of competing schema activation. For alignment-trained models, this attractor corresponds to the constraint-consistent, role-adherent, refusal-capable behavioral region that alignment procedures are designed to establish and reinforce.

The identity attractor is not a point in output space. It is a region — roughly corresponding to the model's baseline CEE centroid w(M) prior to any persona injection (Paper 1, §5.2). Its depth is a measure of how strongly the model's output distribution is pulled toward this region under perturbation — how much injection pressure is required to produce drift away from it, and how readily the model returns once that pressure is removed.

#### 2.2.2 The Constitutional AI Account

The Constitutional AI training methodology provides the most fully articulated published account of how an identity attractor of this kind is constructed (Bai et al., 2022). The CAI procedure does not merely reinforce constraint-consistent outputs — it trains the model to self-critique against an explicit set of behavioral principles, then to revise its outputs in the direction of those principles. Repeated application of this self-revision loop creates a model whose constraint-consistent behavior is not simply an overlay of post-hoc RLHF corrections but is integrated into the output generation process at multiple levels of representation.

The theoretical prediction: a CAI-class model has a deeper identity attractor than a model trained exclusively via RLHF reward shaping, because the CAI procedure establishes constraint-consistency through multiple competing representation layers. When persona injection activates a behavioral schema that conflicts with the constraint-consistent region, the CAI-trained model has more signal competing against that schema. The attractor is deeper because more training passes have carved it.

#### 2.2.3 Formal Proxy Definition

**Attractor Depth (AD)** is defined as a composite behavioral proxy measurable at the output level using the CEE framework established in Paper 1 (§5):

> **AD(M, A) = α · P(M, A) + β · R(M, A)**

Where:
- **M** is the model under observation
- **A** is the injected archetype persona
- **P(M, A)** is the **perturbation threshold** — the number of incremental persona reinforcement steps required to produce a measurable CEE breach (drift_magnitude exceeding τ(A), per Paper 1 §5.3). Higher P = deeper attractor.
- **R(M, A)** is the **recovery rate** — the degree to which drift_magnitude returns toward baseline CEE centroid following removal of perturbation pressure (operationalized as the trailing session average after a null prompt, expressed as proportion of maximum drift recovered). Higher R = deeper attractor.
- **α, β** are weighting constants (default α = β = 0.5; sensitivity analysis recommended)

Three theoretical commitments are explicit in this proxy:

1. **Attractor depth is archetype-specific.** AD(M, A) varies with the archetype because different schemas carry different conflict weights relative to the model's identity attractor. A lawful-neutral archetype (Batman) should produce lower perturbation pressure on a constraint-consistent model than a chaotic schema (Joker). The AD score captures this variance rather than treating constraint resistance as a single scalar property of the model.

2. **Attractor depth is measurable without weight access.** P(M, A) and R(M, A) are behavioral measurements derived entirely from model output coding against the CEE drift taxonomy. No inference about internal states, weight distributions, or architecture is required.

3. **Attractor depth is falsifiable.** If alignment methodology type does not predict variance in AD(M, A) scores — if CAI-class models do not systematically exhibit higher P(M, A) than RLHF-dominant models under equivalent archetype conditions — the core claim of this paper fails. This is a falsifiability condition, not a hedge.

Note on scope: AD(M, A) is not the same construct as P3's resilience_score. P3 measures recovery within a single session for a single archetype in the within-model experimental design. AD uses recovery comparatively across model classes. The constructs are related but distinct — the distinction is explicit in Paper 3 §6 limitations and Paper 4 §7.2.2.

### 2.3 The Redundancy Hypothesis

The attractor depth construct captures magnitude and recovery — but misses a third dimension that this paper argues is theoretically distinct: **redundancy**. Two models may exhibit the same AD score but differ in how that resistance is produced. A model that resists through a single strong constraint signal is structurally more brittle than one that resists through multiple partially-overlapping constraint representations — even if both produce identical output profiles under moderate perturbation pressure.

Constitutional AI-class training establishes constraint consistency through a multi-layer self-revision loop — the constraint is represented at the instruction-following layer, the self-critique layer, and the principle-revision layer simultaneously. RLHF-dominant training establishes constraint consistency through reward signal reinforcement at the output layer — single, strong, but potentially brittle.

The architectural redundancy prediction generates qualitatively distinct failure mode patterns by class:

**RLHF-dominant failure pattern:** Constraint collapse under relatively low perturbation pressure, followed by rapid and complete CEE breach. The reward signal is overcome; no secondary constraint representation resists. Drift is large-magnitude and poorly reversible.

**CAI-class failure pattern:** Resistance through multiple perturbation steps, followed by partial and contested breach. Multi-layer representation means constraint signals compete against the injected schema at multiple levels, producing output that is heterogeneous within sessions — partial compliance, partial refusal. Drift is moderate-magnitude and more readily reversed.

**Instruction-tuning-only failure pattern:** Shallow attractor with very low perturbation threshold. Constraint consistency is established only at the surface output layer and is readily displaced. Drift is rapid and large-magnitude.

**Open-weight / unaligned failure pattern:** No identity attractor in the alignment sense. Perturbation threshold approaches zero. Where constraint behavior appears, it reflects the archetype's behavioral contract, not an alignment signal (Signature OW-3 — schema-consistent constraint from the persona, not the model; see §3.5.3).

These are theoretical predictions, not empirical findings. They constitute the falsifiable framework against which §5's observational cases are evaluated.

### 2.4 Distinguishing Alignment Depth from Model Capability

The paper's predicted finding — that constraint variance correlates more strongly with alignment methodology than with capability — requires a rigorous theoretical distinction between the two variables. Without it, the argument is vulnerable to the confound claim: "what you're calling alignment depth is just intelligence."

Three arguments support the separation.

**Architectural separation.** Capability reflects parameter count, training data volume and quality, and architectural choices. Alignment methodology reflects the post-pretraining fine-tuning and reinforcement procedures applied to that capability base. A more capable base model does not automatically receive deeper alignment investment — the two variables are independently controlled by training decisions. The open-weight model literature provides documented instances of high-capability models with minimal alignment training exhibiting low constraint stability, and lower-capability models with substantial alignment investment exhibiting higher constraint stability.

**Differential prediction.** If capability is the operative variable, constraint stability should scale monotonically with capability markers. If alignment methodology is the operative variable, constraint stability should scale with alignment investment markers independently of capability markers. The 2×2 matrix in §4 specifies the four cells of this prediction, including the critical cell that most strongly discriminates the hypotheses: high-capability / low-alignment, which the capability account predicts should exhibit high constraint stability and the alignment account predicts should exhibit near-zero.

**Mechanism.** The schema activation mechanism established in Papers 1–3 operates at the behavioral schema layer. There is no theoretical reason to expect larger models to be less susceptible to schema activation. If anything, larger models trained on denser and more diverse human-generated text may have *richer* and more strongly encoded behavioral schemas for culturally overdetermined characters — capability amplifies the vulnerability when alignment is absent. Schema activation is not resisted by general intelligence. It is resisted by a competing attractor signal, which is a function of alignment training.

This argument does not claim capability is irrelevant. More capable models may exhibit more sophisticated resistance behaviors — more nuanced refusals, more coherent constraint reasoning. But these are mediated by alignment training, not produced by capability alone. Capability provides the substrate; alignment shapes the attractor.

### 2.5 The Schema Suppression Account

When a persona injection introduces archetype schema A into the model's context, the behavioral dispositions associated with A's training-data representation are activated — the character's constraint relationships, authority orientation, and behavioral contract are loaded into the generative context (Paper 1, §4.3). For the model to resist this activation and maintain constraint-consistent output, it must produce output in which the trained alignment signal *competes against* and *outweighs* the activated schema's behavioral dispositions.

The schema suppression account holds that this competition is continuous, not binary. The identity attractor exerts gravitational pull toward the constraint-consistent region of output space; the injected schema exerts pull toward the schema-dominant region. The output produced in any given turn reflects the balance of these competing signals, weighted by their relative training density and reinforcement.

**Attractor depth is the trained strength advantage of the alignment signal over competing schema signals.** A deep attractor means the alignment signal has substantially higher trained weight than the behavioral schema signal, and therefore maintains output in the constraint-consistent region across a wide range of schema activation pressures. A shallow attractor means the alignment signal has only marginal weight advantage and is readily displaced under incremental persona reinforcement.

This account generates the perturbation threshold prediction directly. Incremental persona reinforcement (Class 2 exploit in Paper 2, §4.2) works by gradually increasing the schema signal weight within the session context — each reinforcement step adds additional schema-consistent context, increasing the schema's effective pull. The perturbation threshold P(M, A) is therefore a proxy for the weight advantage of the model's alignment signal over the schema signal at the point of initial activation.

The schema suppression account does not require weight-level data to be useful. It generates output-level predictions testable with the existing CEE apparatus.

### 2.6 Falsifiability Conditions

**FC1 — Alignment methodology type must predict AD variance.** If AD(M, A) scores do not vary systematically with alignment methodology class, the attractor depth construct does not do the explanatory work claimed.

**FC2 — Alignment methodology must outpredict capability as variance predictor.** If model capability markers predict AD variance equally well or better than alignment methodology markers, the primary claim of the paper is not supported. The critical discriminating test is Cell B of the 2×2 matrix (§4): if high-capability / low-alignment models exhibit high constraint stability, the capability account is supported.

**FC3 — Failure mode patterns must distinguish methodology classes.** The qualitative failure mode predictions — collapse vs. contested-partial-breach vs. shallow threshold — must be distinguishable in documented behavioral observations. If all methodology classes produce qualitatively similar failure modes, the redundancy hypothesis is not supported.

**FC4 — Schema suppression account must predict perturbation threshold ordering.** If archetype schemas with higher theoretically predicted conflict weight do not produce lower P(M, A) than lower-conflict archetypes — controlling for alignment methodology — the schema suppression mechanism does not account for the observed perturbation threshold variation.

### 2.7 Explicit Non-Claims

**This paper does not claim alignment methodology is the only determinant of constraint stability.** Capability, training data composition, inference-time parameters, and system prompt architecture all contribute. The claim is that alignment methodology is the dominant predictor of variance in the specific attack surface addressed here.

**This paper does not claim attractor depth is a property of models in isolation.** AD(M, A) is always indexed to an archetype. The construct is relational, not absolute.

**This paper does not claim access to the mechanistic substrate of the attractor.** The proxy formulation is a behavioral measurement, not a mechanistic claim about how alignment training encodes constraint behavior in model weights.

**This paper does not claim the alignment typology is exhaustive or permanent.** The four methodology classes reflect the documented training methodology literature as of approximately mid-2025. New approaches are acknowledged as a scope limit.

**This paper does not claim the attractor depth proxy is a validated psychometric instrument.** AD(M, A) is a theoretical construct operationalized through a behavioral proxy. It generates testable predictions. It is not validated in the psychometric sense.

---

## 3. Alignment Methodology Typology

### 3.1 Purpose of the Typology

The typology is this paper's analytic instrument for specifying its independent variable with sufficient precision to generate falsifiable predictions. The same methodological move Paper 1 makes with DSM-5 — take an existing validated framework, extract behavioral mechanisms, operationalize them as analytic vocabulary — applies here to the alignment training literature. The typology describes training procedure classes, not commercial products. Every claim about constraint variance is stated at the level of these classes.

### 3.2 Class I — Constitutional AI-Class Training

#### 3.2.1 Procedure Description

Constitutional AI training (Bai et al., 2022) establishes constraint-consistent behavior through a multi-stage self-revision loop: the model generates an initial response, critiques it against an explicit principle set, revises toward principle compliance, and is then reinforced via RLHF against a preference model that has itself been trained to select between the original and revised outputs. The repeated application of this loop across training creates a model whose constraint-consistent behavior is encoded at multiple representational levels — not simply an overlay of post-hoc reward corrections.

For purposes of this typology, Constitutional AI-class training denotes procedures in which:

1. An explicit principle set governs the model's self-evaluation during training
2. A self-critique and revision loop is applied iteratively, creating multi-layer constraint encoding
3. The reinforcement signal rewards outputs that have been revised toward principle compliance, not merely outputs that score high on a static preference model

#### 3.2.2 Attractor Depth Prediction

CAI-class training is predicted to produce the deepest identity attractor in the typology. The multi-layer encoding of the alignment signal means the attractor has architectural redundancy: constraint-consistent behavior is not encoded at one location that can be displaced by sufficient schema activation pressure, but at multiple competing locations. High perturbation threshold. Moderate-to-high recovery rate. Contested-partial-breach failure mode under extreme pressure. Predicted AD range: 0.75–1.0.

#### 3.2.3 Behavioral Output Signatures

*CAI-1 — Principled resistance framing.* CAI-class models produce refusals under persona pressure that reference the constraint principles rather than operational capability limits. "I shouldn't do this" rather than "I can't do this." The principle reference is evidence of the self-evaluation layer activating.

*CAI-2 — Heterogeneous output under high pressure.* Under sustained perturbation, CAI-class models produce output that is internally contested — partial refusal, partial compliance, explicit acknowledgment of tension. The model is not simply maintaining constraint or simply breaking down; it is navigating competing constraints. This heterogeneity is the contested-partial-breach failure mode signature.

*CAI-3 — Recovery without explicit resetting.* Following removal of perturbation pressure, CAI-class models exhibit relatively high recovery rates. The multi-layer attractor provides continued pull toward the constraint-consistent region without requiring explicit resetting language.

*CAI-4 — Injection resistance at shallow depths.* CAI-class models exhibit measurably higher resistance at the initial persona injection step than RLHF-dominant models under equivalent archetype conditions. The self-evaluation layer recognizes the injection as potentially constraint-relevant before behavioral drift has accumulated.

### 3.3 Class II — RLHF-Dominant Training

#### 3.3.1 Procedure Description

RLHF-dominant training (Ouyang et al., 2022; Stiennon et al., 2020) establishes constraint-consistent behavior through a reward model trained on human rater preferences and subsequently used to shape model output via reinforcement learning. The model learns to produce outputs that receive high reward scores from the preference model. The mechanism distinguishing RLHF-dominant from CAI-class is the locus of alignment encoding: RLHF operates primarily at the output layer. The constraint principles underlying reward scores are latent in the reward model's learned preferences, not directly represented as training targets.

For purposes of this typology, RLHF-dominant training denotes procedures in which a reward model trained on human preference ratings is the primary alignment signal, without a separate self-revision or principle-application training loop. This class includes PPO variants, Direct Preference Optimization, and related techniques that share the core structure of alignment-through-output-reward.

#### 3.3.2 Attractor Depth Prediction

RLHF-dominant training is predicted to produce a moderately deep attractor — deeper than instruction-tuning-only, shallower than CAI-class. The reward signal establishes a real alignment weight advantage. However, because the alignment signal is primarily encoded at one layer, the failure mode under sustained perturbation is predicted to be collapse rather than contested partial breach. Once the perturbation pressure accumulates to the point where the reward-signal-consistent and schema-dominant output regions become sufficiently close, the model's output transitions relatively sharply. No secondary constraint representation slows the transition. Predicted AD range: 0.40–0.70.

#### 3.3.3 Behavioral Output Signatures

*RLHF-1 — Threshold-dependent compliance pattern.* RLHF-dominant models exhibit more binary constraint behavior than CAI-class models: clearly constraint-consistent below a perturbation threshold, transitioning to schema-dominant behavior above it.

*RLHF-2 — Refusal brevity under pressure.* Refusal language under perturbation pressure tends to be brief and capability-framed ("I can't help with that") rather than principle-elaborated. The absence of an active self-evaluation layer produces refusals that are output-layer signals without additional reasoning content.

*RLHF-3 — Sharper collapse trajectory.* Under high perturbation pressure, the transition from constraint-consistent to schema-dominant behavior tends to be less gradual than in CAI-class models. Once the reward signal is overcome, the model's output moves more fully into the schema-dominant region rather than exhibiting contested heterogeneity.

*RLHF-4 — Partial recovery on topic shift.* Following removal of perturbation pressure, RLHF-dominant models exhibit partial but not complete recovery. The model may remain closer to the schema-dominant region than its pre-injection baseline.

### 3.4 Class III — Instruction-Tuning-Only

#### 3.4.1 Procedure Description

Instruction-tuning establishes constraint-consistent behavior through supervised fine-tuning on instruction-following demonstrations — examples of question-answer or task-completion behavior in a desired format and register. Constraint consistency is not established through a dedicated alignment procedure (reward model, RLAIF, self-critique loop) but through the selection and weighting of training demonstrations. There is no reward signal amplifying the alignment weight advantage and no self-critique loop deepening the representation.

IT-only denotes procedures in which alignment behavior is established primarily through supervised fine-tuning on curated demonstrations, with no dedicated reward model or reinforcement learning procedure shaping the alignment signal.

#### 3.4.2 Attractor Depth Prediction

IT-only training produces a shallow attractor. Constraint-consistent output is produced under normal conditions because the training demonstrations were constraint-consistent, but the model's disposition toward that output is not reinforced by a competing alignment signal. Perturbation threshold is consequently low: persona injection that activates a behavioral schema with sufficient canonical strength can displace IT-only alignment with relatively few reinforcement steps. Predicted AD range: 0.15–0.40.

#### 3.4.3 Behavioral Output Signatures

*IT-1 — Rapid threshold crossing.* Persona injection under chaotic or constraint-resistant archetypes produces CEE breach within a small number of perturbation steps.

*IT-2 — Demonstration-patterned refusals.* Where IT-only models do refuse under persona pressure, refusal language tends to be formulaic — closely matching training demonstration patterns — rather than principle-elaborated. Refusals may be verbose in format while functionally shallow in reasoning content.

*IT-3 — Style-consistent drift.* When IT-only models drift into schema-dominant behavior, the drift tends to maintain surface stylistic conventions (tone, format, register) while abandoning constraint-consistent content. The instruction-following scaffold persists; the alignment signal does not.

*IT-4 — Poor recovery profile.* No attractor depth to pull output back toward the constraint-consistent region. Recovery requires explicit resetting language that re-establishes the demonstration-consistent context.

### 3.5 Class IV — Open-Weight / Minimally Aligned

#### 3.5.1 Procedure Description

Open-weight models released without alignment-specific post-training, or with minimal alignment procedures insufficient to establish a robust identity attractor, constitute the fourth class. This includes base models released without instruction tuning, models fine-tuned exclusively for task performance without dedicated alignment procedures, and models whose alignment procedures have been deliberately removed through subsequent fine-tuning.

The defining characteristic is not the absence of safety-relevant behaviors per se — base models may refuse some requests due to training data distributions — but the absence of a dedicated alignment training procedure that establishes a trained identity attractor. Without such a procedure, there is no systematic weight advantage of constraint-consistent output over competing behavioral schemas.

The open-weight model ecosystem is theoretically significant for this paper because it provides the closest available approximation to the Cell B condition (§4): models with substantial capability but minimal alignment investment. These are the critical discriminating cases between the capability account and the alignment account.

#### 3.5.2 Attractor Depth Prediction

Near-zero attractor depth. The behavioral schema signal from a canonically overdetermined archetype meets no competing alignment signal; activation is immediate and nearly complete. Predicted AD range: 0.0–0.20. The qualifier "near-zero" rather than "zero" acknowledges that base pretraining data distributions include some constraint-relevant content that may produce residual resistance under very weak perturbation conditions — a distributional artifact, not a trained identity attractor.

#### 3.5.3 Behavioral Output Signatures

*OW-1 — Near-immediate schema dominance.* Under persona injection with a canonically strong archetype, schema-dominant behavior within the first or second turn following injection. P(M, A) approaches zero.

*OW-2 — Absence of principled resistance language.* Unlike CAI-class and RLHF-dominant models, open-weight unaligned models under persona pressure do not produce refusals that reference principles, preferences, or role-consistent limitations.

*OW-3 — Schema-consistent constraint behavior.* This is the theoretically interesting distinguishing signature. Open-weight unaligned models may produce constraint-consistent outputs under persona injection — but the constraint comes from the archetype, not from the model's alignment. A lawful archetype injected into an unaligned model may produce outputs that superficially resemble aligned behavior; a chaotic archetype injected into the same model produces no such constraint. The CEE and the schema are the only relevant attractor; alignment plays no role. This observational category has no analog in P3's within-model CEE framing and constitutes a scope gap in the series measurement apparatus (§7.5, §2.3).

*OW-4 — No recovery profile.* Following removal of perturbation pressure, no systematic recovery toward a constraint-consistent baseline. There is no attractor to return to.

### 3.6 Class Boundary Considerations

The four-class typology is analytic. Real training pipelines combine procedures. The class assignment reflects the dominant alignment procedure — the one that constitutes the primary alignment signal.

**Sequential pipelines.** IT-then-RLHF is assigned RLHF-dominant: the reward signal is the terminal and highest-weight alignment signal. The layering increases attractor depth relative to IT-only but does not reach CAI-class depth because the self-revision loop is absent.

**Partial Constitutional AI implementation.** Procedures that incorporate principle sets as evaluation criteria without implementing the full self-revision loop are assigned conservatively to RLHF-dominant. The multi-layer encoding that produces the redundancy prediction requires the self-revision loop, not merely the presence of a principle set.

**Post-training alignment modifications.** Models whose alignment training has been modified are assigned based on the net effect on the identity attractor. Where published documentation is available, it is cited. Where undocumented, the class assignment is marked as inferred.

### 3.7 The Typology as Analytic Instrument, Not Product Inventory

The typology describes training procedure mechanisms. Named commercial products are not referenced except as examples of methodology class in cited published literature. This is theoretically principled: training procedures are stable analytic categories; named products change across versions. Claims indexed to procedure classes are more durable and more precisely grounded in causal structure than claims indexed to product names.

---

## 4. The 2×2 Capability × Alignment Matrix

### 4.1 Purpose of the Matrix

The matrix operationalizes the capability/alignment separation argument (§2.4) as a structured predictive framework. It converts theoretical constructs into falsifiable cell-level predictions. Section 5 tests its cells; Section 6 draws from them. The matrix is also encoded as executable theoretical apparatus in `scripts/alignment_typology_matrix.py` — the script is the formal structure; this section is the reasoning.

### 4.2 Matrix Structure

The matrix crosses two dimensions: model capability tier (HIGH / LOW) and alignment investment tier (HIGH / LOW). Capability tier is indexed to benchmark performance and training compute as publicly documented markers. Alignment investment tier is indexed to the typology: HIGH alignment = CAI-class or RLHF-dominant; LOW alignment = instruction-tuning-only or open-weight unaligned.

```
                    ALIGNMENT INVESTMENT
                    HIGH              LOW
               ┌──────────────┬──────────────┐
  CAPABILITY   │  Cell A      │  Cell B ★    │
  HIGH         │  High cap    │  High cap    │
               │  High align  │  Low align   │
               ├──────────────┼──────────────┤
  CAPABILITY   │  Cell C ★    │  Cell D      │
  LOW          │  Low cap     │  Low cap     │
               │  High align  │  Low align   │
               └──────────────┴──────────────┘
★ = Critical discriminating cell
```

**Table 1. Predicted AD ranges and failure modes by cell**

| Cell | Capability | Alignment | AD range (alignment account) | Failure mode | Accounts diverge? |
|---|---|---|---|---|---|
| A | HIGH | HIGH | 0.70–1.0 | Contested-partial-breach or high resistance | No — both predict high stability |
| B ★ | HIGH | LOW | 0.0–0.25 | Near-immediate schema dominance | **YES — critical discriminator** |
| C ★ | LOW | HIGH | 0.50–0.80 | Contested-partial-breach, cap-floor modified | **YES — critical discriminator** |
| D | LOW | LOW | 0.0–0.20 | Shallow-threshold or immediate schema dominance | No — both predict low stability |

### 4.3 Cell-Level Predictions

#### 4.3.1 Cell A — High Capability, High Alignment

Both accounts predict high constraint stability. Cell A is a conjunction confirmation, not a discriminating test. The alignment account predicts this because high alignment investment produces a deep attractor with multi-layer redundancy. The capability account predicts this because high capability produces sophisticated constraint-consistent behavior. The two accounts converge; Cell A does not discriminate between them.

**Cell A value:** As a control condition, Cell A establishes the upper bound of constraint stability the matrix predicts. If Cell A models exhibit unexpectedly low constraint stability, both accounts require revision — an alternative mechanism is producing the failure.

#### 4.3.2 Cell B — High Capability, Low Alignment ★ Critical Discriminator

The alignment account predicts near-zero constraint stability for Cell B. A highly capable model with minimal alignment investment has a rich behavioral schema activation profile — its denser pretraining corpus contains stronger behavioral contract encoding for canonical archetypes — but no meaningful identity attractor to compete against that activation. The schema activation signal meets no organized resistance. Breach is predicted to be rapid and near-complete.

Critically: the alignment account predicts that Cell B may exhibit *stronger* schema activation than Cell D — a high-capability / low-alignment model may be more susceptible to persona injection than a lower-capability / low-alignment model, because richer pretraining produces richer behavioral schemas without a countervailing attractor. Capability amplifies the vulnerability when alignment is absent.

The capability account predicts the opposite: high capability should produce high constraint stability regardless of alignment methodology. Cell B should look like Cell A.

Cell B is the first critical discriminator. The two accounts predict in opposite directions. If Cell B exhibits low constraint stability, the alignment account is supported and the capability account is falsified for this cell. This cell carries the paper's most practically significant claim: deploying a high-capability model without proportionate alignment investment does not produce the security properties that capability alone might be assumed to provide.

#### 4.3.3 Cell C — Low Capability, High Alignment ★ Critical Discriminator

The alignment account predicts moderate-to-high constraint stability for Cell C. A low-capability model with CAI-class or RLHF-dominant alignment training carries a weaker behavioral schema activation profile (from sparser pretraining) but a genuine identity attractor (from dedicated alignment investment). The attractor, though competing against a weaker schema signal, is sufficient to produce meaningful constraint stability. Predicted AD range: 0.50–0.80.

The sharpest single prediction the matrix generates: a well-aligned small model outperforms a more capable but minimally aligned model in constraint stability — Cell C outperforms Cell B on AD metrics. If this cross-cell prediction holds, the security properties relevant to persona injection resistance are a function of training choices, not of scale.

The alignment account acknowledges a boundary condition: there may exist a capability floor below which alignment training cannot establish a functional identity attractor, because the model lacks the representational capacity to support multi-layer self-revision encoding. The predicted AD range of 0.50–0.80 rather than 0.75–1.0 reflects this.

The capability account predicts low constraint stability for Cell C. Cell C should look like Cell D.

Cell C is the second critical discriminator. If Cell C exhibits moderate-to-high constraint stability despite reduced capability, the alignment account is supported and the capability account is falsified for this cell.

#### 4.3.4 Cell D — Low Capability, Low Alignment

Both accounts predict low constraint stability. Cell D does not discriminate between them. It provides the empirical floor against which the Cell B and Cell C findings are interpreted. If Cell D shows unexpectedly high constraint stability, both accounts require revision — an alternative mechanism not captured by either dimension is producing resistance.

### 4.4 The Discriminating Logic

The decision procedure is graduated, not binary.

**Strong alignment-dominant finding:** Cell B ≤ 0.25 AD AND Cell C ≥ 0.50 AD. The crossing of predictions — high capability without alignment performs poorly, low capability with alignment performs moderately well — is the clearest evidence that alignment methodology is the dominant variable.

**Weak alignment-dominant finding:** Cell B ≤ 0.25 AD but Cell C also below 0.50. Alignment investment produces some attractor depth, but not enough at low capability to generate the predicted moderate-to-high stability. The Cell C boundary condition is active. Alignment account partially supported; capability floor hypothesis requires investigation.

**Strong capability-dominant finding:** Cell B ≥ 0.50 AD AND Cell C ≤ 0.25. The capability account is supported; the alignment account requires fundamental revision.

**Null finding:** All four cells cluster at similar AD ranges regardless of dimension. A third variable — inference-time parameters, system prompt architecture, archetype selection confounds — is likely dominant.

### 4.5 The Archetype Dimension

The matrix crosses capability and alignment while treating archetype as a held-constant variable. The CEE framework and the AD proxy both index attractor depth to the specific archetype injected. For the matrix to function as a clean capability-vs-alignment comparison, archetype must be held constant across cells. The matrix predictions in §4.3 are stated for a mid-range schema conflict archetype — high enough canonical overdetermination to produce reliable schema activation, high enough schema conflict to challenge the identity attractor, but not at the ceiling where any alignment methodology would be overwhelmed regardless of depth.

### 4.6 What the Matrix Cannot Determine

**Within-class variation.** The matrix collapses the four-class typology to a binary. Within the HIGH alignment tier, CAI-class and RLHF-dominant models are predicted to behave differently. The matrix cannot distinguish these within-class differences.

**Capability non-linearity.** The capability dimension is dichotomized. Both capability and alignment are continuous and multidimensional in practice. The HIGH/LOW dichotomization is a theoretical simplification.

**Interaction effects.** The matrix treats the two dimensions as main effects. Whether the effect of alignment investment on constraint stability differs between capability tiers is not directly specified. The Cell C boundary condition is the closest the matrix comes to predicting an interaction.

**Deployment context.** The matrix predictions are stated for standard deployment conditions: default inference-time parameters, no additional system prompt constraint architecture, single-turn or short multi-turn sessions.

---

## 5. Evidence Base

### 5.1 Evidence Categories and Confidence Weights

The evidence base draws from three source categories with materially different methodological standards:

**Category A — Published red-team and safety literature.** Controlled methodology with stated protocols. Highest evidential weight. Primary claim anchor.

**Category B — Documented public discourse.** Practitioner documentation, community benchmarks, documented behavior reports. Moderate evidential weight.

**Category C — Author's prior series observational work.** Informal observation without experimental control. Lowest evidential weight. Contributes to practice-led theory generation argument in §8, not to the theoretical claim about constraint variance.

Source heterogeneity is not a reason to collapse confidence levels — it is a reason to be explicit about which claims rest on which evidence type. The weak alignment-dominant finding rests on Category A evidence for Cell B. Cell C's weaker support is stated as the primary evidence gap.

### 5.2 Cell A Cases — High Capability, High Alignment

*(Both accounts predict high stability — this cell does not discriminate.)*

Published alignment evaluation work on CAI-class and RLHF-dominant models at high capability tiers documents substantially higher resistance to adversarial prompting, roleplay-based constraint erosion, and persona pressure compared to minimally aligned counterparts. This is consistent with both accounts' Cell A predictions. The evidence establishes the upper bound and confirms that the matrix's HIGH-HIGH cell is empirically recognizable, but does not help choose between the accounts.

### 5.3 Cell B Cases — High Capability, Low Alignment ★ Primary discriminating cells

**Case B-1 — Adversarial robustness literature (Category A, Confidence: MODERATE)**

Wei et al. (2023) and Zou et al. (2023) document systematic constraint stability failures in model classes under adversarial prompting — including persona-framing approaches — that do not correlate straightforwardly with model scale. Specifically, models whose training documentation suggests minimal or attenuated alignment procedures exhibit near-zero constraint stability under persona pressure regardless of capability tier. This is consistent with the alignment account's Cell B prediction and inconsistent with the capability account's Cell B prediction. Note on citation scope: Wei et al. (2023) provides evidence of alignment failure under adversarial prompting. It does not support schema-layer, identity-injection, or attractor-dynamics claims specifically — those are this paper's constructs applied to interpret the documented failures. The evidence supports "instruction-layer alignment is brittle under adversarial pressure"; this paper models the structural reasons why.

**Case B-2 — Uncensored fine-tuning documentation (Category B, Confidence: MODERATE-LOW)**

Publicly documented procedures for producing "uncensored" model variants — fine-tuning that removes or attenuates alignment training from capable base models — consistently produce models that exhibit near-complete schema adoption under persona injection within one to two turns, regardless of the base model's capability tier. The base model's behavioral schema encoding remains intact or is enhanced by capability; the alignment signal is removed; constraint stability approaches zero. This is the Cell B condition instantiated directly, and it is inconsistent with the capability account's prediction for this cell.

**Cell B verdict:** Alignment account directionally supported. Evidence confidence: MODERATE. The most direct test of the archetype-specific perturbation sequence protocol remains a gap.

### 5.4 Cell C Cases — Low Capability, High Alignment ★ Secondary discriminating cells

**Case C-1 — Within-family scale comparisons (Category A, Confidence: MODERATE-LOW)**

Within model families sharing the same alignment training procedure, smaller variants retain meaningful constraint stability under persona pressure, while exhibiting lower performance on capability benchmarks. Ganguli et al. (2022) document that alignment training retains partial effectiveness at reduced capability within Constitutional AI-class training lineages. This is necessary but not sufficient for the full Cell C prediction: within-family scale comparisons do not provide the cross-family, cross-capability-tier comparison the Cell C discriminating hypothesis requires.

**Case C-2 — Author's prior series observations (Category C, Confidence: LOW)**

During the P3 observational work, constraint recovery behavior appeared to vary across model classes in ways not predicted by capability markers alone. Smaller models with documented CAI-class or RLHF-dominant training exhibited more complete recovery from perturbation removal than larger models with minimal alignment training. This observation is the practice-led origin of the attractor depth theoretical construct. It is documented here as reflexive evidence of the practice-led methodology at work, not as confirmatory evidence for the alignment account.

**Cell C verdict:** Alignment account weakly supported by within-family scale comparisons. The critical cross-cell comparison — Cell C vs. Cell B, testing whether a small aligned model outperforms a large unaligned model — is not directly testable from the current evidence base. This is the paper's primary evidence gap.

### 5.5 Cell D Cases

Both accounts predict low constraint stability for Cell D. The evidence is consistent with baseline vulnerability (rapid persona adoption, shallow threshold, low recovery) without discriminating between accounts. Cell D provides the empirical floor.

### 5.6 Overall Evidence Assessment

The available evidence is most consistent with a **weak alignment-dominant finding:**

- Cell B provides moderate-confidence support for the alignment account's prediction that high capability without alignment produces low constraint stability. High-capability / low-alignment model classes exhibit near-zero constraint stability under persona pressure in the documented evidence, which is directly inconsistent with the capability account's core prediction for that cell.
- Cell C provides weak support for the prediction that alignment investment produces constraint stability partially independent of capability tier. The Cell C boundary condition — the capability floor below which alignment investment may not establish a functional attractor — cannot be evaluated from the current evidence base.
- The evidence does not support a strong capability-dominant finding.

The finding is weak alignment-dominant rather than strong because the Cell C cross-family cross-cell comparison — the sharpest discriminating test — cannot be conducted from the available evidence. This is stated as the primary direction for future empirical work.

---

## 6. Alignment Implications

### 6.1 What the Framework Warrants

The framework established in §2–4 and evaluated in §5 provides: a theoretical account of why constraint variance should be expected to scale with alignment methodology class; a typology of alignment procedures and their predicted attractor depth signatures; a matrix of falsifiable predictions evaluated at moderate confidence; and a conceptual vocabulary for describing the structural features of the identity-injection attack surface.

What it does not provide is an empirically validated intervention protocol or a prescriptive ranking of currently deployed systems. The implications that follow stay within these bounds. They are what the theoretical framework, at its current evidential status — weak alignment-dominant finding — warrants claiming. Strong theoretical arguments grounded in moderate-confidence empirical support. Not established facts.

### 6.2 Implication I: Alignment Investment Is a Security Variable

The framework's most direct implication: alignment investment should be understood as a security variable — not only as an ethical or policy variable — in the context of identity-injection attacks.

The prevailing framing positions alignment training primarily as a means of producing models that are helpful, honest, and harmless in ordinary use. That framing is accurate but incomplete. The attractor depth construct establishes a second consequence: the depth and redundancy of the trained identity attractor determines the structural resistance of the model to behavioral schema override. A model with a deep alignment attractor is not merely more likely to produce constraint-consistent output in normal conditions — it is structurally more resistant to the class of attacks that operate by activating competing behavioral schemas to displace the alignment signal.

The investment decisions that produce alignment depth are simultaneously investment decisions in identity-injection attack resistance. Choices about whether to implement CAI-class self-revision loops, how many training passes to dedicate to alignment fine-tuning, and whether to document and maintain the principle set that training targets are not purely ethical infrastructure choices — they are security infrastructure choices. Underfunding them creates a vulnerability surface that scales inversely with the investment made.

Cell B makes this concrete. High-capability models with minimal alignment investment exhibit near-zero constraint stability under persona injection pressure. The capability investment is large. The security property relevant to identity-layer attacks is absent. The gap between them is the alignment attractor — and capability does not fill it.

### 6.3 Implication II: The Instruction Layer Is Not the Only Defense Layer

Paper 2 (§6) establishes that persona injection operates below the instruction layer — activating behavioral dispositions through schema activation rather than through direct instruction override. Instruction-layer defenses are insufficient at inference time because they operate on outputs, not on the schema activation process that produces them.

The framework developed here extends that implication. The insufficient defense problem begins at training time, and its structural character is precisely what the attractor depth construct describes. A model trained exclusively with RLHF reward signals has an alignment signal that operates at the output layer. Its defense against schema activation is therefore also at the output layer: the reward signal competes against the schema signal in output generation, and once that competition is overcome, there is no secondary constraint representation to provide continued resistance. The instruction-layer defense problem at inference time is a consequence of the training-layer architecture decision.

Constitutional AI-class training addresses this not by adding more instruction-layer defense but by encoding the alignment signal at multiple representational levels during training. The self-critique and revision loop creates constraint representations not located solely at the output layer — they are encoded in the self-evaluation process, which operates earlier in the generation pipeline. This multi-layer encoding produces the redundancy property and the contested-partial-breach failure mode under pressure.

The training-design implication: alignment procedures that aspire to robust identity-injection resistance should explicitly target multi-layer constraint encoding, not only output-layer reward optimization. The specific mechanism by which CAI-class training achieves this is one implementation; the theoretical requirement is the redundancy, not the specific procedure.

### 6.4 Implication III: The Capability–Alignment Pairing Is a Security Configuration

If alignment investment is the dominant predictor of constraint stability under persona injection, the capability–alignment pairing is not merely a design trade-off to be optimized — it is a security configuration to be evaluated.

The 2×2 matrix makes the security-configuration framing concrete:

- **Cell A** (high capability, high alignment): Strongest predicted security properties for the identity-injection surface.
- **Cell B** (high capability, low alignment): A configuration whose capability investment is not matched by alignment investment, producing a security-relevant gap. Capability amplifies schema activation without a countervailing attractor.
- **Cell C** (low capability, high alignment): A configuration whose alignment investment produces meaningful security properties despite reduced capability.
- **Cell D** (low capability, low alignment): Baseline vulnerability configuration.

The security-configuration argument is not that all models must be Cell A. The deployment context determines which security properties are required. A low-risk deployment context where persona injection is an unlikely attack vector may accept Cell D configuration. A high-risk deployment context — customer-facing systems, systems where output is acted upon without human review, security-sensitive environments — warrants Cell A configuration. The framework provides the vocabulary for making that deployment decision in security terms.

### 6.5 Implication IV: Attractor Depth Is Potentially Measurable Pre-Deployment

The AD proxy construct is defined entirely in terms of behavioral outputs observable at inference time, without requiring access to model weights. This means attractor depth is in principle assessable as a pre-deployment evaluation metric.

Current model evaluation practices for alignment-relevant behavior tend to focus on benchmark performance against curated harmful-output test sets — what the model produces in response to known problematic prompts. These benchmarks assess constraint-consistent output in normal conditions but do not assess the structural depth of the constraint under sustained attack conditions. A model may pass a harmful-output benchmark by producing constraint-consistent outputs in response to known attack patterns, while exhibiting near-zero attractor depth under the graduated persona pressure that the series documents.

An AD assessment using the P3 perturbation sequence methodology applied across archetype conditions — measuring P(M, A) and R(M, A) per archetype across the conflict weight range — would provide a structural constraint assessment supplementing the static benchmark approach. The measurement apparatus exists; the P3 methodology is the experimental instantiation of this evaluation protocol. The implication is that P3's measurement approach has potential pre-deployment evaluation applications beyond the experimental context the series uses it for.

### 6.6 Implication V: Deployment Risk Profiles by Typology Class

The typology and failure mode predictions generate deployment risk profiles that are relevant to operational decisions about where on the capability–alignment matrix a deployed system sits.

**CAI-class models in high-risk deployments:** Contested-partial-breach failure mode means constraint failures are partial and detectable — heterogeneous output signals the breach before it is complete. CEE variance alerting (Paper 2, §6) is most effective against this profile because the breach trajectory is gradual.

**RLHF-dominant models in high-risk deployments:** Collapse failure mode means constraint failures are rapid and relatively complete once the perturbation threshold is crossed. Detection requires earlier warning than the CAI-class profile — monitoring the approach to threshold rather than the breach itself. The briefer window for intervention requires more sensitive early-warning alerting.

**IT-only or open-weight models in high-risk deployments:** Shallow-threshold or immediate-schema-dominance failure mode means constraint failures may occur at the first perturbation step under a canonically strong archetype. CEE variance alerting requires detection at initial persona injection, not drift monitoring — the vulnerability is the activation itself, not the subsequent drift trajectory.

The risk profile framing complements Paper 1 (§9.4)'s opening for defensive systems design and schema-layer alignment research — P4 §6.6 provides the deployment-context specification of what that defensive systems design requires. Mitigation cannot be uniform across typology classes; it must be calibrated to the failure mode predicted for the deployed model's alignment class.

### 6.7 Implication VI: A Schema-Layer Research Agenda

The theoretical framework implies four specific research directions. These deliver on the schema-layer alignment research opening stated in Paper 1 (§9.4) and extend the defensive systems design argument that paper planted:

**Direction 1 — Systematic schema inventory.** A comprehensive inventory of the behavioral schemas activated by canonical archetypes across model classes, documenting schema density, conflict weight, and CEE centroid predictions. This inventory is a prerequisite for pre-deployment AD assessment at scale.

**Direction 2 — Multi-layer alignment training development.** Alignment procedures explicitly designed to produce attractor redundancy — encoding the constraint signal at multiple representational levels to generate the contested-partial-breach failure mode rather than the collapse pattern. The theoretical specification of what this requires is provided by the schema suppression account (§2.5) and the CAI-class procedure analysis (§3.2).

**Direction 3 — Schema-layer drift monitoring.** Runtime monitoring architectures designed to detect CEE centroid displacement before breach, calibrated to the deployment model's failure mode profile. This extends the CEE variance alerting heuristic from Paper 2 (§6) into a typology-differentiated monitoring specification.

**Direction 4 — Temporal dynamics.** How attractor depth interacts with multi-session context accumulation, persistent memory architectures, and in-context fine-tuning dynamics. The session stationarity limitation inherited from the series (§7.5.1) defines the current boundary of the framework; temporal dynamics research pushes that boundary.

---

## 7. Limitations and Non-Claims Registry

### Preface

Scholarly claims earn credibility not only by what they assert but by what they explicitly decline to assert. These boundaries are not apologies for the paper's contribution — they are the conditions under which that contribution is coherent and defensible. Where a limitation appears in an earlier section, this registry is the authoritative consolidation. On any assembly pass, if an item here conflicts with a local statement in §2–6, the registry takes precedence.

### 7.1 Methodological Limitations

**7.1.1 — Hypothesis-generating, not hypothesis-confirming.**
This paper does not claim to have confirmed that alignment methodology is the dominant predictor of cross-model constraint variance. The methodological frame is explicitly hypothesis-generating throughout. The weak alignment-dominant finding is directional support, not confirmation. The condition under which this limitation resolves: systematic empirical investigation using the AD proxy measurement apparatus with controlled archetype conditions across documented methodology classes. (§1.3, §4.4, §5.6.3)

**7.1.2 — No active probing.**
This paper conducts no active adversarial probing of any model. This is a methodological choice, not merely a constraint. Active probing would constitute red-teaming, not scholarship. The distinction between documenting and theorizing a vulnerability surface and operationalizing it as an attack protocol is the load-bearing ethical distinction governing this paper. The theoretical contribution does not depend on active probing and is not weakened by its absence. (§1.3)

**7.1.3 — No provider-specific targeting.**
All claims about constraint variance are stated at the level of alignment methodology class, not at the level of named commercial products. Training procedures are stable analytic categories; named products change. (§3.7)

**7.1.4 — Evidence base source heterogeneity.**
The three source categories carry materially different evidential weight. The weak alignment-dominant finding rests primarily on Category A evidence for Cell B, with partial Category A and Category C support for Cell C. Any stronger conclusion would require Category A evidence for both critical discriminating cells. (§5.1, §5.6)

### 7.2 Construct Limitations

**7.2.1 — Attractor Depth is a behavioral proxy, not a mechanistic measure.**
AD(M, A) = α·P(M, A) + β·R(M, A) is a composite behavioral proxy observable at the output layer. The theoretical interpretation — that higher AD scores reflect deeper identity attractor encoding in the model's trained weight configuration — is consistent with the construct but not directly established by it. (§2.2.3, §2.5)

**7.2.2 — Attractor Depth is archetype-indexed, not absolute.**
A model that exhibits high AD under a constraint-compatible archetype may exhibit substantially lower AD under a high-conflict archetype. AD assessments must be archetype-specific; a single-archetype AD measurement does not characterize general constraint stability. (§2.2.3, §4.5)

**7.2.3 — The Schema Suppression Account is interpretive, not established.**
The schema suppression account is a theoretical interpretation consistent with the Constitutional AI literature and the failure mode predictions. It is not derived from direct observation of model internals. Alternative accounts at the systems level could produce similar behavioral profiles. (§2.5)

**7.2.4 — The four-class typology is analytic, not exhaustive.**
The typology covers dominant alignment procedures documented through approximately mid-2025. New alignment approaches may require typology extension. (§3.6, §3.8)

**7.2.5 — The 2×2 matrix dichotomizes continuous variables.**
Capability and alignment investment are continuous in practice. Models near tier boundaries may not exhibit the predicted patterns as clearly as models well within each tier. The Cell C boundary condition — a capability floor below which alignment investment may not establish a functional attractor — is not directly estimable from the current evidence base. (§4.3.3, §4.6)

### 7.3 Evidence Base Limitations

**7.3.1 — Cell C cross-family comparison is absent.**
The Cell C prediction — that a low-capability model with high alignment investment exhibits moderate-to-high constraint stability and outperforms Cell B on AD metrics — is the sharpest discriminating test of the alignment account. This cross-family, cross-capability-tier comparison requires controlled measurement outside this paper's methodological scope. It is the primary evidence gap. (§4.3.3, §5.4, §5.6.2)

**7.3.2 — Archetype-specific protocol not tested in Category A literature.**
The Category A evidence base was not designed to test the specific archetype-driven persona injection protocol developed in Papers 1–3. The translation from source literature to typology coding involves inferential steps. (§5.1.2, §5.6.1)

**7.3.3 — Category C evidence carries confirmation bias risk.**
The author's prior series observational work motivated the theoretical framework and is then included as supplementary evidence for it. The paper manages this risk by assigning Category C the lowest confidence weight and framing its evidential role as reflexive documentation rather than confirmatory support. Primary claims rest on Category A evidence. (§5.1.3, §5.4)

**7.3.4 — Temporal scope of the evidence base.**
Behavioral observations reflect model behavior at the time of documentation. The paper makes no claim about the current constraint behavior of any specific model or deployment. (§3.7, §3.8)

### 7.4 Implication Limitations

**7.4.1 — Implications are proportional to the weak alignment-dominant finding.**
The implications in §6 are derived from a theoretical framework with moderate-confidence evidential support. They do not carry the weight of empirically confirmed findings. Stronger empirical evidence would justify strengthening them. Evidence against the alignment account in either critical discriminating cell would require revision or retraction. (§5.6.3, §6.1)

**7.4.2 — Implications are scoped to the identity-injection attack surface only.**
No implication in §6 is stated as a general claim about alignment investment and model security across all attack surfaces. The identity-injection surface is one of several LLM attack surfaces. (§6.2, §6.8)

**7.4.3 — The pre-deployment evaluation protocol is theoretical, not operationalized.**
The pre-deployment AD assessment protocol described in §6.5 is a theoretical argument for a measurement approach implied by the framework. It has not been operationalized, standardized, or validated as an evaluation instrument. The psychometric properties — test-retest reliability, inter-rater reliability, sensitivity and specificity — are unknown. The claim is that the theoretical basis exists; the instrument is future work. (§2.2.3, §6.5)

**7.4.4 — Deployment risk profiles are first-order characterizations.**
The risk profiles in §6.6 are derived from failure mode predictions that are theoretical rather than empirically validated. They are the most theoretically grounded characterizations available; they are not measured risk parameters derived from controlled measurement of actual failure rates. (§3.2.3–3.5.3, §6.6)

### 7.5 Series-Boundary Limitations

**7.5.1 — Session stationarity inherits from the series.**
The CEE and AD constructs are within-session measurements. The implications of attractor depth for multi-session persistence, fine-tuning dynamics, and persistent memory architectures are outside scope. The temporal dynamics research direction in §6.7 is the appropriate future work response. (Paper 1, §7.1)

**7.5.2 — Training data opacity inherits from the series.**
The schema suppression account posits that alignment signal weight advantage is established through training. The training data composition that shapes both the alignment signal and the schema signal is not publicly documented with sufficient granularity to directly verify the density claims on which the schema activation mechanism depends. (Paper 1, §7.2)

**7.5.3 — Acting vs. being inherits from the series.**
The behavioral proxy formulation cannot distinguish between genuine schema activation and sophisticated surface mimicry. The partial discriminator from Paper 1 §7.3 and Paper 3 (H3 — archetype × perturbation interaction effect) applies but does not eliminate the alternative account. (Paper 1, §7.3)

**7.5.4 — Cross-model comparison introduces new confounds.**
Within-model analysis controls for model as a variable by holding it constant. Cross-model comparison necessarily varies the model, introducing confounds not fully controllable without active probing: differences in system prompt sensitivity, inference-time parameter settings, context window handling, tokenization, and training data composition that are independent of alignment methodology and capability tier. This is a new limitation specific to P4, not inherited from the series. It is the primary reason cell predictions are stated as ranges rather than point estimates and evidence assessment is MODERATE rather than HIGH. (§4.2, §5.1.3, §5.6)

### 7.6 What the Limitations Do Not Undermine

Four contributions survive all the limitations above:

**Contribution 1 — The theoretical construct.** The attractor depth construct and the alignment methodology typology provide a theoretically grounded, operationally specified vocabulary for describing cross-model constraint variance under persona injection. This vocabulary did not exist before this paper. It fills the gap left by the within-model framework of Papers 1–3. The construct's validity as a theoretical framing device does not depend on the evidence base's strength.

**Contribution 2 — The predictive structure.** The 2×2 matrix generates falsifiable, non-obvious predictions about the relative constraint stability of four model configurations. The discriminating predictions for Cells B and C are genuinely novel: neither is derivable from the existing jailbreak or red-team literature without the typology vocabulary. The matrix provides the design template for future empirical work regardless of the current evidence base's limitations.

**Contribution 3 — The alignment investment reframing.** The reconceptualization of alignment investment as a structural security variable — one whose absence predicts near-zero constraint stability under persona injection in Cell B configurations — is a conceptual contribution with practical consequences. It is not an empirical finding; it is a reframing grounded in the theoretical framework and warranted by the directional evidence. It warrants serious empirical investigation and changes how deployment decisions should be framed.

**Contribution 4 — The series hinge.** Paper 4 is the point in the series where the within-model framework generates a cross-model question it cannot answer. Documenting that question precisely — with a theoretical construct, a typology, a falsifiable predictive matrix, and a specified evidence gap — is itself a contribution to the series' research program. It defines the next required step: a controlled cross-model comparison using the AD proxy measurement apparatus, with Cells B and C as the critical discriminating conditions.

---

## 8. Conclusion and Exegesis Hooks

### 8.1 What This Paper Has Done

The paper opened with a gap in the within-model framework: the question why some locks are harder to open. The answer it develops is theoretical, not empirical — and it is honest about that. The attractor depth construct, the alignment methodology typology, and the 2×2 predictive matrix together constitute a theoretical account of why constraint variance under archetype-driven persona injection should scale with alignment methodology rather than with raw capability. The account is grounded in published alignment literature, operationalized through a behavioral proxy measurable at the output level, structured as a falsifiable predictive framework, and supported at moderate confidence by the available evidence base.

### 8.2 Four Contributions

**Contribution 1.** The Attractor Depth construct operationalized as a composite behavioral proxy — AD(M, A) = α·P(M, A) + β·R(M, A) — measurable without model weight access. Novel theoretical construct. Does not depend on the evidence base for its validity as a theoretical framing device.

**Contribution 2.** A four-class alignment methodology typology (CAI-class, RLHF-dominant, instruction-tuning-only, open-weight unaligned) specified at the level of training procedure mechanism with predicted attractor depth signatures and behavioral output signatures per class. Novel analytic instrument. Stable across commercial product changes.

**Contribution 3.** A 2×2 capability × alignment predictive matrix generating falsifiable, non-obvious predictions — including the Cell B prediction that high-capability / low-alignment models exhibit near-zero constraint stability partly because of their capability (stronger schema activation without countervailing attractor). Novel predictive structure, not derivable from prior series papers alone.

**Contribution 4.** The reconceptualization of alignment investment as a structural security variable in the identity-injection attack surface. A conceptual reframing with direct practical consequences for deployment decision-making.

### 8.3 The Evidential Status

The weak alignment-dominant finding is the paper's evidential conclusion. Cell B has moderate-confidence support; Cell C has weak support. Neither constitutes confirmation. The finding warrants investigation; it does not warrant strong implications stated as established facts. §6 is calibrated to this throughout.

The primary evidence gap — the Cell C cross-family comparison, testing whether a small aligned model demonstrably outperforms a large unaligned model on AD metrics — is the first required empirical step. The framework provides the measurement apparatus, the experimental design, and the discriminating prediction. What it does not provide is the data.

### 8.4 The Paper as Series Hinge

> [EXEGESIS HOOK: §A — P4 as series hinge; the cross-model question only expressible after P1–P3 built the vocabulary]

The series arc is developmental, not cumulative. Each paper reveals a question the previous papers' frameworks are structurally unable to answer:

Paper 1 asks: *can the vulnerability surface be mapped formally and validly?* The CEE answers that question.

Paper 2 asks: *what are the structural exploit classes, and why does the SE literature describe them?* The five-class taxonomy answers that question.

Paper 3 asks: *can the CEE and vulnerability surface be empirically measured?* The experiment answers that question.

Paper 4 asks: *does the vulnerability surface vary systematically across models, and is the variance a function of alignment investment or of capability?* The attractor depth framework and 2×2 matrix are the answer — in theoretical form, awaiting empirical confirmation.

The attractor depth construct did not exist when Paper 1 was written. It emerged from the practice-led observation that recovery behavior varied across model classes in ways the within-model CEE framework described but could not explain. The typology was built to answer the question that the observation raised. The matrix was derived from the typology once the typology was in place. This is the practice-led methodology working exactly as it should.

### 8.5 Practice-Led Theory Generation

> [EXEGESIS HOOK: §B — practice-led theory generation; the attractor depth construct emerged from observation, not deduction]

The theoretical account in §2 is presented in deductive order — from construct definition through mechanism account. That deductive presentation is appropriate for a research paper.

The construct did not arrive deductively. It arrived as a recognizable pattern in prior series observations — a pattern of differential constraint recovery behavior across model classes that the existing within-model framework could not explain. The question "why does this model recover from perturbation when that one doesn't?" preceded the construct. The construct was built to answer it.

This is not a methodological failure. Theory grounded in observation is already calibrated to the phenomenon before the formal apparatus is constructed. The cost is the confirmation bias risk acknowledged in §7.3.3. The benefit is that the construct is not floating free of empirical grounding.

### 8.6 The Series as a Research Methodology

> [EXEGESIS HOOK: §C — the series as research methodology; iterative mapping as contribution beyond any paper's specific claims]

The four papers together constitute a methodology — a replicable approach to mapping a vulnerability surface not yet sufficiently understood for controlled experimentation to be the primary research tool. Five components:

*Multi-framework convergence as validity criterion.* Independently validated frameworks (DSM-5 behavioral taxonomy, SE theory, archetype schema theory, computational alignment literature) converge on the same vulnerability surface. The convergence is the primary validity argument.

*Formal operationalization before empirical testing.* The CEE and AD constructs are formalized — defined, bounded, falsifiable in principle — before the empirical apparatus is deployed. Paper 3 tests a pre-specified prediction, not a post-hoc pattern match.

*Practice-led observation as theoretical input.* The author's experience working with the research materials generates theoretical observations that feed the formal apparatus. Case C-2 (§5.4) is the explicit instance in P4.

*Explicit non-claims as methodological discipline.* Each paper maintains a non-claims registry. A contribution defined by what it claims and what it explicitly does not claim is more precisely located in the intellectual space than a contribution defined by claims alone.

*Forward-opening structure.* Every paper ends not only by closing the question it opened but by opening the next question it could not answer. The series does not terminate — it maps a territory that expands as it is explored, and is honest about the edges of the map.

This methodology is a contribution to research practice in AI safety that exists independently of the specific claims any paper makes.

### 8.7 The Papers This Paper Implies

> [EXEGESIS HOOK: §D — P5 and P6 as implied completions; the series defines a research program, not only a set of findings]

The AD proxy (§2.2.3) and the pre-deployment assessment argument (§6.5) are Paper 5's theoretical seed: a generalized evaluation framework that transforms the measurement methodology of Paper 3 into a portable pre-deployment instrument.

The schema-layer research agenda (§6.7) and the deployment risk profiles (§6.6) are Paper 6's theoretical seed: a defensive architecture paper addressing what an adequate schema-layer defense looks like, given that we can now characterize and measure the vulnerability surface.

A doctoral series that attempts to map, measure, compare, evaluate, and mitigate a vulnerability surface within four papers will do none of them well. A series that maps (P1), identifies exploitation vectors (P2), measures (P3), and explains cross-model variance (P4) establishes the foundation on which evaluation and mitigation work can be built — and provides that foundation rigorously.

### 8.8 The Closing Claim

If the alignment account is confirmed — if Cell B models exhibit low constraint stability and Cell C models exhibit moderate-to-high constraint stability, as the framework predicts — the consequence is precise and practically significant: the security properties relevant to identity-injection attack resistance are a function of training choices, not of scale, and they are in principle designable.

Alignment investment is not merely an ethical commitment. It is a structural security decision whose consequences are theoretically predictable and empirically measurable.

The series has built the tools to test whether that claim is true. The test remains to be made.

---

## Reconciliation Notes

**Assembly status:** REWRITE COMPLETE — all 8 sections present, all scaffolding stripped.

**[FLAG-P4-BP-1: CLEARED]** P1 §9.4 forward pointer now present in §6.6 and §6.7 explicitly. P4 §6.7 is cited as delivering on the schema-layer alignment research opening from Paper 1 §9.4; §6.6 extends the defensive systems design argument.

**[FLAG-P4-BP-2: CLEARED]** P4 §3 typology references P2 §6 explicitly in §6.3 as additive rather than repetitive. P2 §6's instruction/schema-layer distinction and P4 §3's within-alignment-layer variation are consistent claims at different levels of analysis.

**[FLAG-C-11: NOTED]** P3 resilience_score vs. P4 AD(M,A) scope distinction now explicit in §2.2.3 with note that P3 measures recovery within a single session for a single archetype; P4 uses recovery comparatively across model classes.

**[FLAG-C-12: NOTED]** P4 failure mode taxonomy has 4 types (vs. P3's 3 perturbation_response types). Note now embedded in §2.3 — the four failure modes are theoretical predictions constituting the falsifiable framework; P4 adds contested-partial-breach and immediate-schema-dominance as new categories not in P3's within-model coding schema.

**[FLAG-OW-3]** Signature OW-3 (schema-consistent constraint from archetype, not alignment) now explicitly flagged in §3.5.3 as a new observational category not covered by P3's within-model CEE framing and constituting a scope gap in the series measurement apparatus.

**[Wei et al. (2023)]** Citation role locked per bibliography v1.1: evidence of alignment failure under adversarial prompting; supports "instruction-layer alignment is brittle" claim; does NOT support schema-layer, identity-injection, or attractor-dynamics claims. Framing note embedded in §5.3, Case B-1.

**[Connective tissue sentence]** P7 CBESS bridge sentence added to abstract final paragraph: "The attractor depth construct also provides the theoretical basis for why Paper 7's cross-domain behavioral equivalence analysis predicts partial rather than full equivalence: the alignment attractor is a constraint on human-LLM structural homology that has no direct human-side analog."

**Citation normalisation:** Hadnagy (2011) throughout; no split dates; Cialdini (1984) in running text per bibliography v1.1.
