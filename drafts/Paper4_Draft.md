<!-- ════════════════════════════════════════════════════════════════════════
  PAPER HEADER
  Title:    Alignment Depth as Attack Surface: Cross-Model Constraint
            Variance Under Archetype-Driven Persona Injection
  Author:   Stephen Pote (scp)
  Series:   Paper 4 of 7 — Compare
  Status:   ASSEMBLED DRAFT v0.1 — 2026-04-30 | FULLY DRAFTED
  Sources:  P4_S1_Abstract_Introduction.md, P4_S2_TheoreticalFrame.md,
            P4_S3_MethodologyTypology.md, P4_S4_TwoByTwoMatrix.md,
            P4_S5_EvidenceBase.md, P4_S6_Implications.md,
            P4_S7_Limitations_NonClaims.md, P4_S8_Conclusion_ExegesisHook.md
  Node:     MKUltra / Mause Koenig — Assembler
════════════════════════════════════════════════════════════════════════ -->


## --- S1 ---

# Paper 4 — Abstract and Section 1: Introduction
## "Alignment Depth as Attack Surface: Cross-Model Constraint Variance
##  Under Archetype-Driven Persona Injection"

> **Placement:** `drafts/paper4/P4_S1_Abstract_Introduction.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Role in paper:** Threshold section. The abstract and introduction are
> the only sections most reviewers read before deciding whether to read
> further — they carry a disproportionate share of the paper's first-
> impression burden. Both are written from the completed paper backward:
> every claim made here is grounded in a section that exists behind it.
> No promises are made that §2–8 do not keep.
>
> **Writing discipline:** The abstract states what the paper does, not
> what it hopes or wishes. The introduction motivates the question,
> situates it in the series and in the field, states the research
> question and central claim cleanly, previews the paper structure,
> and manages publication constraints actively (no provider targeting,
> no active probing, hypothesis-generating framing) — not as disclaimers
> in the conclusion but as framing choices stated from the opening.
>
> **Cross-paper dependencies:**
> - Abstract contribution statements must match §8.2 exactly.
>   If they diverge on assembly, §8.2 takes precedence.
> - §1.4 Central Claim becomes the canonical wording for this paper,
>   equivalent in role to P1 §1.4. On series assembly, P4 §1.4 is the
>   citable claim statement for cross-paper reference.
> - Series context in §1.2 must be consistent with P1 §1.1, P2 §1.1,
>   P3 §1 on series assembly. Check framing of each paper's role.
>
> **Target venues (from series publication constraints):** AI safety
> research venues (NeurIPS Safety Workshop, ICLR Safety Track),
> HCI-security venues (CHI, USENIX SOUPS), Science and Technology
> Studies. Not clinical psychology venues.

---

## Abstract

The constraint behavior of large language models under archetype-driven persona
injection — the process by which named character schemas are injected into model
context to activate behavioral dispositions inconsistent with trained alignment —
varies measurably and non-trivially across model classes. The prevailing implicit
assumption is that this variance tracks model capability: larger, more capable
models resist persona injection more effectively. This paper argues that the
dominant structural variable is not capability but alignment investment, and
develops the theoretical framework necessary to investigate that claim.

Drawing on the Constitutional AI literature and the social engineering transfer
framework established in Papers 1–2 of this series, the paper introduces the
Attractor Depth construct: a behavioral proxy for the structural depth of a model's
trained identity attractor, operationalized as a composite of perturbation threshold
and recovery rate within the Constraint Expectation Envelope measurement apparatus.
A four-class alignment methodology typology (Constitutional AI-class, RLHF-dominant,
instruction-tuning-only, open-weight unaligned) specifies the independent variable
at the level of training procedure mechanism rather than named product, and a 2×2
capability × alignment predictive matrix generates falsifiable cell-level predictions
that separate the two competing accounts. The critical discriminating prediction
is Cell B: a high-capability model with minimal alignment investment should exhibit
near-zero constraint stability under persona injection — not despite its capability,
but in part because of it, given that richer pretraining produces stronger behavioral
schema activation signals without a countervailing alignment attractor to suppress
them. The evidence base, drawn from published red-team literature and the author's
prior series observations, provides moderate-confidence directional support for the
alignment account. The paper closes by reconceptualising alignment investment as a
structural security variable in the identity-injection attack surface — a reframing
with direct implications for how deployment decisions are made and how alignment
investment is evaluated.

*Keywords: LLM alignment, persona injection, identity-layer attacks, attractor depth,
Constitutional AI, constraint variance, behavioral schema activation, AI safety*

---

## 1. Introduction

### 1.1 The Question That Papers 1–3 Could Not Answer

Papers 1, 2, and 3 of this series establish a framework for understanding behavioral
drift in large language models under archetype-driven persona injection. Paper 1
formalizes the Constraint Expectation Envelope (CEE): the bounded region of
constraint-relevant behavioral output predictably associated with a given injected
archetype, measurable as deviation from the archetype's canonical trait weight
vector (Paper 1, §5). Paper 2 demonstrates that the five-class exploit taxonomy
derived from social engineering theory describes the attack vectors that displace
model output from the CEE — and that these vectors operate at the behavioral schema
layer, below and largely independent of instruction-layer defenses (Paper 2, §3–4).
Paper 3 provides the empirical evidence: CEE drift is measurable, archetype selection
predicts drift magnitude, and perturbation sequences produce the archetype-specific
response patterns the framework predicts (Paper 3, §4–5).

The three papers together constitute a within-model account of the vulnerability
surface. They characterize how the lock works, how it is opened, and how the opening
can be measured. They do not address a question that the within-model framework is
structurally unable to answer: why are some locks harder to open than others?

The empirical pattern that motivates this question is consistent across the literature
and across the author's series observations. Models trained with more extensive and
multi-layered alignment procedures exhibit materially higher resistance to persona
injection — higher perturbation thresholds, more complete recovery after perturbation
removal, more heterogeneous output under sustained pressure. Models trained with
minimal alignment procedures yield rapidly and completely. This variance is not
obviously a function of capability: the relationship between model scale and
constraint stability under persona injection is considerably messier than the
relationship between model scale and benchmark performance on standard tasks.

Two competing accounts of the variance are available. The capability account holds
that constraint stability scales with model capability: larger, more capable models
have richer contextual reasoning and more sophisticated output generation, and
these properties produce better constraint-consistent behavior under pressure. The
alignment account holds that constraint stability scales with alignment investment:
the depth and redundancy of the trained identity attractor — the structural property
that alignment training establishes — is the dominant variable, and capability
contributes only indirectly by providing the substrate on which alignment training
operates.

Choosing between these accounts has practical consequences. If the capability account
is correct, scaling is a security strategy: larger models are more robust, and
investment in capability doubles as investment in identity-layer attack resistance.
If the alignment account is correct, capability and alignment are separable variables:
a highly capable model without proportionate alignment investment is no more resistant
to persona injection than a smaller model at the same alignment level — and may
be more susceptible, because its richer training corpus provides stronger behavioral
schema activation signals without a deeper attractor to suppress them.

This paper develops the theoretical framework necessary to investigate that question.

---

### 1.2 Series Context and Paper Position

This paper is the fourth in a doctoral research series on behavioral drift in LLMs
under persona injection. The series is practice-led: it was not designed from a
complete pre-specified research plan but developed iteratively, each paper addressing
a question revealed by the preceding papers. The series arc is:

**Paper 1 — The Mapping.** Establishes that three independently validated frameworks —
DSM-5 behavioral taxonomy (as mechanism extraction, not diagnosis), social engineering
theory (Cialdini, Milgram, Hadnagy), and archetype schema theory (Jung, Campbell,
schema cognition) — describe the same vulnerability surface when applied to LLM
persona injection. Formalizes the CEE as the construct that makes this claim
empirically tractable.

**Paper 2 — The Taxonomy.** Develops a five-class exploit taxonomy of social
engineering-derived attack vectors against the identity-injection surface. Establishes
that persona injection operates below the instruction layer, at the behavioral
schema layer, in ways that instruction-layer defenses do not address.

**Paper 3 — The Measurement.** Provides empirical evidence. Instruments the CEE,
tests the framework's predictions across a six-archetype experimental set, and
demonstrates that archetype selection and perturbation produce the predicted drift
patterns at measurable magnitude.

**Paper 4 (this paper) — The Comparison.** Asks whether the vulnerability surface
characterized in Papers 1–3 varies systematically across model classes, and whether
that variance is better explained by alignment methodology or by raw model capability.
Provides the theoretical framework, predictive structure, and conceptual vocabulary
necessary to investigate this question empirically.

Paper 4 is the series hinge in a precise sense: it extends the within-model framework
of Papers 1–3 into a cross-model theoretical account, and in doing so poses the
question that will drive the subsequent papers in the series. The answer — that
alignment investment is the dominant structural variable — could only be theorized
once Papers 1–3 had established the vocabulary with which to pose it. The CEE, the
perturbation threshold and recovery rate, the schema activation mechanism, the
exploit class taxonomy: these are all prerequisites for asking the cross-model
question with the precision required for a falsifiable answer.

---

### 1.3 Methodological Framing: What This Paper Does and Does Not Do

Before stating the research question and claim, the methodological frame that
governs this paper — and the series — must be stated clearly, because it shapes
what kind of contribution this paper makes.

**Observational, not adversarial.** The series documents and theorizes vulnerability
surfaces; it does not operationalize them as attack tooling. This paper uses
published red-team literature, documented public discourse, and the author's prior
series observations as its evidence base. It conducts no active probing of deployed
models. The line the paper holds throughout is: describing the lock mechanism versus
providing the key. Documenting that high-capability, minimally aligned models exhibit
near-zero constraint stability under persona injection is a contribution to defensive
understanding; packaging a perturbation sequence to exploit that property in a
specific deployed system is not something this paper does.

**Agnostic description, not provider targeting.** Cross-model comparison in this
paper is conducted at the level of alignment methodology class — Constitutional
AI-class, RLHF-dominant, instruction-tuning-only, open-weight unaligned — not at
the level of named commercial products. This is not a methodological evasion. It is
theoretically principled: training procedure classes are stable analytic categories;
named commercial products change across versions and updates. Claims indexed to
procedure classes are more durable and more precisely grounded in causal structure
than claims indexed to product names (§3.7).

**Hypothesis-generating, not hypothesis-confirming.** The 2×2 predictive matrix
(§4) generates falsifiable predictions. The evidence base (§5) evaluates those
predictions at moderate confidence. The result is a weak alignment-dominant finding:
directional support for the alignment account that warrants serious empirical
investigation but does not constitute a confirmed result. The implications in §6
are calibrated to this evidential status: they are stated as what the framework
suggests and what the evidence supports, not as established findings.

**Agnostic on model internals.** The Attractor Depth proxy (§2.2.3) is defined
entirely in terms of behavioral outputs observable at inference time. No claim is
made about model weights, internal activation patterns, or architectural features.
The theoretical account of why deeper alignment training produces higher perturbation
thresholds — the schema suppression account (§2.5) — is an interpretive framework
consistent with the behavioral evidence, not a mechanistic claim about computational
substrate.

---

### 1.4 Research Question and Central Claim

**Research Question:** Does observable constraint behavior under incremental persona
injection pressure correlate systematically with alignment methodology class — more
strongly than with raw model capability tier — and if so, does this constitute
evidence for a structural vulnerability surface that scales inversely with alignment
investment?

**Central Claim:**

> If alignment functions as a trained identity attractor — a structural region of
> the model's output distribution that training has reinforced as the default
> self-model — then constraint stability under archetype-driven persona injection
> is a function of that attractor's depth and redundancy, not primarily of the
> model's raw capability. A well-aligned model with limited capability may
> outperform a highly capable model with minimal alignment investment on the
> identity-injection attack surface — not because it is more intelligent, but
> because its identity scaffolding has more competing representations to suppress
> schema-dominant behavior. This paper maps that variance as a theoretical construct,
> specifies it as a behavioral proxy measurable with the CEE apparatus, structures
> it as a falsifiable predictive framework, and argues it warrants systematic
> empirical investigation.

The claim has two components that must be kept distinct. The theoretical component —
the attractor depth construct, the alignment methodology typology, and the 2×2
matrix — is independent of the evidence base and is the paper's primary contribution.
The evidential component — the weak alignment-dominant finding from the evidence
base — is hypothesis-generating support for the theoretical framework, not a
confirmed empirical result. Both components are stated here and held distinct
throughout.

---

### 1.5 Paper Structure

The paper proceeds as follows.

**§2 — Theoretical Framework** develops the Identity Attractor construct, formalizes
the Attractor Depth proxy, introduces the Redundancy Hypothesis and the failure mode
taxonomy, constructs the theoretical argument for separating alignment depth from
capability as the operative variable, and presents the Schema Suppression Account
as the bridging mechanism between the attractor construct and the schema activation
machinery of Papers 1–3. Falsifiability conditions and explicit non-claims are stated.

**§3 — Alignment Methodology Typology** specifies the paper's independent variable.
The four-class typology (Constitutional AI-class, RLHF-dominant, instruction-tuning-
only, open-weight unaligned) is defined in terms of training procedure mechanism,
grounded in published alignment literature, and specified with predicted attractor
depth signatures and behavioral output signatures for each class. The typology is an
analytic instrument, not a product inventory.

**§4 — The 2×2 Capability × Alignment Matrix** operationalizes the capability/
alignment separation argument as a predictive framework. Four matrix cells are
defined; two critical discriminating cells (Cell B: high capability / low alignment;
Cell C: low capability / high alignment) are identified where the alignment account
and the capability account predict in opposite directions. The discriminating logic
and the decision procedure for evaluating the accounts are stated.

**§5 — Evidence Base** engages the available evidence. Observational cases drawn
from published red-team literature (Category A), documented public discourse
(Category B), and the author's prior series observations (Category C) are coded
against the typology and matrix vocabulary. The evidence assessment concludes with
a weak alignment-dominant finding and an explicit identification of the primary
evidence gap.

**§6 — Alignment Implications** develops six implications of the theoretical
framework for alignment system design, deployment evaluation, pre-deployment
assessment, deployment risk profiling, and the schema-layer research agenda.
The security reframing of alignment investment is the principal implication.

**§7 — Limitations and Non-Claims Registry** consolidates all scope conditions and
explicit non-claims into a structured registry organised by limitation type. Sixteen
items across five clusters. The four theoretical contributions that survive all
limitations are stated.

**§8 — Conclusion and Exegesis Hook** states the paper's contribution in final form,
situates it in the series arc, and plants the explicit markers the doctoral exegesis
will need to argue that the series constitutes a coherent research practice and that
the practice produced knowledge not derivable from any single paper.

---

*Section ends. §2 (Theoretical Framework) follows directly. Note to assembly: §1
was written last, from the completed paper backward. Any inconsistency between a
claim in §1 and the section it references should be resolved in favor of the
referenced section, which contains the full argument.*

---

> **Reconciliation note (2026-04-28):**
>
> §1.4 Central Claim is the canonical wording for this paper. On series assembly,
> if P2 or P3 cross-reference P4's central claim, they should use this formulation
> or cite §1.4.
>
> The two-component distinction in §1.4 — theoretical claim (primary contribution,
> independent of evidence) vs. evidential claim (hypothesis-generating support) —
> should propagate to the paper's abstract on any revision pass that strengthens
> the evidential base. The distinction is currently doing structural work to manage
> reviewer expectations; if future empirical work confirms the alignment account,
> the claim tier should be revised upward with the evidential component separated
> from the theoretical contribution in §8.2 accordingly.
>
> §1.2 series arc summary (P1 mapping, P2 taxonomy, P3 measurement, P4 comparison)
> is the clearest single-paragraph description of the series structure in any paper.
> Flag for exegesis use — the exegesis's series overview section can draw directly
> from this paragraph.
>
> Target venue abstract word count: 200–250 words. Current abstract is 248 words.
> Within target. On venue-specific formatting pass, verify venue abstract length
> requirements and adjust if needed. Keywords list may require adjustment for
> specific venue taxonomies.

## --- S2 ---

# Paper 4 — Section 2: Theoretical Framework
## "Alignment as Attractor: Formalizing Constraint Stability Under Persona Pressure"

> **Placement:** `drafts/paper4/P4_S2_TheoreticalFrame.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Role in paper:** Load-bearing section. All subsequent sections (S3 methodology
> typology, S4 2×2 matrix, S5 evidence base, S6 implications) depend on the
> constructs formalized here. Build nothing else until this section stabilizes.
> **Cross-paper dependencies:**
> - Imports: CEE formal definition (P1 §5), behavioral schema activation (P1 §4.3),
>   exploit class taxonomy (P2 §4), drift measurement apparatus (P3 §2–3)
> - Exports: Attractor Depth construct (→ S3, S4, S6, S7); Alignment Methodology
>   Typology (→ S3, S5, exegesis); Cross-model CEE variance prediction (→ S4, S5)
> **Committee exposure:** HIGH — this section makes the novel theoretical claims.
> Every construct introduced here requires operational definition, falsifiability
> condition, and explicit non-claim. Do not let the dynamical systems metaphor
> outrun its operationalization. The metaphor is the scaffolding; the CEE proxy
> formulation is the building.
> **Agnostic framing requirement:** All alignment methodology discussion operates
> at the typology level (Constitutional AI-class, RLHF-dominant, instruction-tuning-
> only, open-weight unaligned). Named commercial products are not referenced except
> as examples of methodology class in cited published literature. Behavioral
> observations are attributed to methodology type, not product.

---

## 2. Theoretical Framework: Alignment as Identity Attractor

### 2.1 The Central Theoretical Move

Papers 1 through 3 of this series establish a shared evidential base: that LLM
behavioral constraint under persona injection is measurable, archetype-predictable,
and structurally analogous to the social-engineering vulnerability patterns documented
in clinical psychology and applied security literature. The Constraint Expectation
Envelope (CEE) formalizes the behavioral region within which a given model-under-
archetype operates, and drift measurement quantifies deviation from that envelope's
centroid under perturbation pressure.

What Papers 1–3 leave systematically unaddressed is variance across models. The CEE
framework characterizes the vulnerability surface as it presents within a given model
under a given archetype condition. It does not theorize why that surface would be
deeper, shallower, wider, or narrower for a different model encountering the same
archetype injection — and this omission is not a flaw in the earlier papers, it is a
gap they deliberately leave open. The present paper fills that gap.

The theoretical move is this: if alignment functions as a trained *identity attractor* —
a structured region of the model's behavioral output distribution that training has
reinforced as the default self-model — then constraint stability under persona pressure
is not a fixed property of the model class. It is a function of the attractor's depth,
redundancy, and the training investment that established it. Models with deeper, more
redundantly encoded identity attractors will exhibit greater resistance to schema-
dominant behavior under persona injection. Models with shallow, sparsely encoded
identity attractors will exhibit lower resistance thresholds — not because they are
less capable, but because their trained self-representation has fewer competing
signal weights to suppress the injected schema.

This paper maps that variance as a theoretical construct, specifies it in terms
directly measurable with the existing CEE apparatus, and argues it constitutes
a structural vulnerability surface that scales — not with model capability — but
with alignment investment.

---

### 2.2 The Identity Attractor: From Metaphor to Construct

The dynamical systems concept of an attractor — a region toward which a system
tends to return under perturbation — provides the theoretical vocabulary. But the
value of this framing for the present paper depends entirely on whether "attractor
depth" can be operationalized in behavioral terms without requiring access to model
weights, training data, or internal architecture. The swarm requires an empirically
tractable construct, not an elegant metaphor.

#### 2.2.1 Informal Definition

An **identity attractor** (IA), as used here, is the trained behavioral disposition
set that constitutes a model's default self-model — the output distribution that
the model tends to return to across diverse input conditions in the absence of
competing schema activation. For alignment-trained models, this attractor corresponds
to the constraint-consistent, role-adherent, refusal-capable behavioral region that
alignment procedures are designed to establish and reinforce.

The identity attractor is not a point in output space. It is a region — roughly
corresponding to the model's baseline CEE centroid w(M) prior to any persona injection
(see P1 §5.2 for centroid formalism). Its "depth" is a measure of how strongly the
model's output distribution is pulled toward this region under perturbation — i.e.,
how much injection pressure is required to produce drift away from it, and how
readily the model returns to it once that pressure is removed.

#### 2.2.2 The Constitutional AI Account

The Constitutional AI (CAI) training methodology provides the most fully articulated
published account of how an identity attractor of this kind is constructed (Bai et al.,
2022). The CAI procedure does not merely reinforce constraint-consistent outputs — it
trains the model to self-critique against an explicit set of behavioral principles,
and then to revise its outputs in the direction of those principles. The repeated
application of this self-revision loop across training creates a model whose
constraint-consistent behavior is not simply an overlay of post-hoc RLHF corrections
but is integrated into the model's output generation process at multiple levels of
representation.

The theoretical prediction, within the attractor framing: a CAI-class model has a
deeper identity attractor than a model trained exclusively via RLHF reward shaping,
because the CAI procedure establishes constraint-consistency through *multiple
competing representation layers* — not through a single reward signal. When persona
injection activates a behavioral schema that conflicts with the constraint-consistent
region, the CAI-trained model has more signal competing against that schema. The
attractor is deeper because more training passes have carved it.

The present paper adopts this account as a theoretical prior. It does not independently
validate the CAI training procedure and is not in a position to do so — the relevant
weight-level evidence is not publicly available. What it does is use the attractor
depth construct to generate behavioral predictions that are testable at the output
level using the CEE apparatus.

#### 2.2.3 Formal Proxy Definition

**Attractor Depth (AD)** is defined, for purposes of this paper, as a composite
behavioral proxy measurable at the output level using the CEE framework established
in Paper 1 (§5). It has two components:

> **AD(M, A) = α · P(M, A) + β · R(M, A)**

Where:
- **M** is the model under observation
- **A** is the injected archetype persona
- **P(M, A)** is the **perturbation threshold** — the number of incremental persona
  reinforcement steps required to produce a measurable CEE breach (drift_magnitude
  exceeding τ(A), as defined in P1 §5.3). Higher P = deeper attractor.
- **R(M, A)** is the **recovery rate** — the degree to which drift_magnitude returns
  toward baseline CEE centroid following removal of perturbation pressure (operationalized
  as the trailing session average after a null prompt following the perturbation
  sequence, expressed as proportion of maximum drift recovered). Higher R = deeper
  attractor.
- **α, β** are weighting constants (default α = β = 0.5; sensitivity analysis recommended)

This proxy formulation makes three theoretical commitments explicit:

1. **Attractor depth is archetype-specific.** AD(M, A) varies with the archetype
   because different schemas carry different conflict weights relative to the model's
   identity attractor. A lawful-neutral archetype (Batman) should produce lower
   perturbation pressure on a constraint-consistent model than a chaotic schema
   (Joker). The AD score captures this variance, rather than treating "constraint
   resistance" as a single scalar property of the model.

2. **Attractor depth is measurable without weight access.** P(M, A) and R(M, A)
   are behavioral measurements derived entirely from model output coding against the
   CEE drift taxonomy. No inference about internal states, weight distributions, or
   architecture is required. This is methodologically essential for a paper that cannot
   conduct active probing.

3. **Attractor depth is falsifiable.** If alignment methodology type does not predict
   variance in AD(M, A) scores — if, for example, models with documented Constitutional
   AI training do not systematically exhibit higher P(M, A) than RLHF-dominant models
   under equivalent archetype conditions — then the core claim of this paper fails.
   This is stated as a falsifiability condition in §2.6.

---

### 2.3 The Redundancy Hypothesis

The attractor depth construct captures magnitude and recovery — but misses a third
dimension of the alignment vulnerability surface that this paper argues is theoretically
distinct: **redundancy**. Two models may exhibit the same AD score (same perturbation
threshold, same recovery rate) but differ in *how* that resistance is produced. A model
that resists through a single strong constraint signal is structurally more brittle than
a model that resists through multiple partially-overlapping constraint representations —
even if the two models produce identical output profiles under moderate perturbation
pressure.

This distinction matters for Paper 4's argument because alignment methodologies differ
not only in the depth of the attractor they create but in the architectural redundancy
of that attractor. Constitutional AI-class training, as described above, establishes
constraint consistency through a multi-layer self-revision loop — the constraint is
represented at the instruction-following layer, the self-critique layer, and the
principle-revision layer simultaneously. RLHF-dominant training establishes constraint
consistency through reward signal reinforcement at the output layer — a single,
strong, but potentially brittle encoding.

The architectural redundancy prediction: Constitutional AI-class models should exhibit
*qualitatively different* failure modes under extreme perturbation pressure compared
to RLHF-dominant models. Specifically:

- **RLHF-dominant failure pattern:** Constraint collapse with relatively low perturbation
  pressure, followed by rapid and complete CEE breach — the reward signal is overcome,
  and there is no secondary constraint representation to resist. Drift is large-magnitude
  and poorly reversible.

- **CAI-class failure pattern:** Resistance through multiple perturbation steps,
  followed by partial and contested breach — the multi-layer representation means
  constraint signals compete against the injected schema at multiple levels, producing
  output that is heterogeneous within sessions (partial compliance, partial refusal).
  Drift is moderate-magnitude and more readily reversed.

- **Instruction-tuning-only failure pattern:** Shallow attractor with very low
  perturbation threshold — constraint consistency is established only at the surface
  output layer and is readily displaced by schema-dominant behavior. Drift is rapid,
  large-magnitude, and often followed by persona-congruent constraint absence for
  the remainder of the session.

- **Open-weight / unaligned failure pattern:** No identity attractor in the alignment
  sense — constraint behavior, where present, reflects instruction-following rather
  than trained self-model constraint. Perturbation threshold approaches zero under
  archetypal persona injection because there is no competing attractor to resist
  the schema.

These are theoretical predictions, not empirical findings. They constitute the
falsifiable framework against which observational cases in §5 are evaluated.

**Redundancy as a theoretical construct.** For purposes of this paper, alignment
redundancy is treated as a qualitative property inferred from the failure mode pattern
rather than as a separately operationalized score. A model that exhibits the contested-
partial-breach pattern is inferred to have higher alignment redundancy than a model
exhibiting the collapse pattern, even if their AD scores are similar. This inference
is stated explicitly where it occurs in the observational case analysis (§5), and its
theoretical status — inference, not measurement — is maintained throughout.

---

### 2.4 Distinguishing Alignment Depth from Model Capability

The paper's predicted finding — that constraint variance correlates more strongly with
alignment methodology than with raw model capability — requires a rigorous theoretical
distinction between the two variables. Without this distinction, the argument is
vulnerable to the confound claim: "what you're calling alignment depth is just
intelligence, and larger/more capable models resist persona injection for the same
reason they perform better at every task."

The theoretical case for separating the variables rests on three arguments.

**Argument 1 — Architectural separation.** Model capability (as indexed by benchmark
performance, parameter count, or compute budget) and alignment methodology are
implemented at different layers of the training process. Capability reflects the
model's parameter count, training data volume and quality, and architectural choices
(context window, attention head configuration, etc.). Alignment methodology reflects
the post-pretraining fine-tuning and reinforcement procedures applied to the
capability base. A more capable base model does not automatically receive deeper
alignment investment — the two variables are independently controlled by training
decisions. This is not merely theoretical: the open-weight model literature provides
documented instances of high-capability models with minimal alignment training
(exhibiting low constraint stability under perturbation) and lower-capability models
with substantial alignment investment (exhibiting higher constraint stability).

**Argument 2 — Differential prediction.** If capability is the operative variable,
then constraint stability under persona injection should scale monotonically with
capability markers (benchmark performance, model size). If alignment methodology is
the operative variable, then constraint stability should scale with alignment
investment markers (documented training procedures, Constitutional AI vs. RLHF vs.
instruction-tuning-only) independently of capability markers. The theoretical
framework predicts the second pattern. The 2×2 matrix in §4 specifies the four
cells of this prediction explicitly, including the critical cell that most strongly
discriminates the hypotheses: the high-capability / low-alignment cell, which the
capability account predicts should exhibit high constraint stability and the alignment
account predicts should exhibit low constraint stability.

**Argument 3 — Mechanism.** The schema activation mechanism established in Papers 1–3
operates at the behavioral schema layer — below the instruction layer and at the level
of trained associative representations between character names and behavioral
dispositions. There is no theoretical reason to expect larger models to be less
susceptible to schema activation: if anything, larger models trained on denser and
more diverse human-generated text corpora may have richer and more strongly encoded
behavioral schemas for culturally overdetermined characters. Schema activation is not
resisted by general intelligence; it is resisted by a competing attractor signal —
which is a function of alignment training, not capability.

This argument does not claim that capability is irrelevant to constraint behavior.
More capable models may exhibit more sophisticated resistance behaviors — more nuanced
refusals, more coherent constraint reasoning, better recovery from perturbation
pressure. But these are mediated by alignment training, not produced by capability
alone. Capability provides the substrate; alignment shapes the attractor.

The non-claim that follows from this argument is stated explicitly in §2.6 and
reiterated in the Non-Claims Registry (§7): **this paper does not claim that
capability is irrelevant to constraint behavior, only that alignment methodology
is the dominant predictor of constraint variance across the documented typology.**

---

### 2.5 The Schema Suppression Account

A theoretical bridge is needed between the attractor depth construct and the behavioral
schema activation mechanism established in Paper 1. How, specifically, does a deeper
identity attractor resist schema activation? The schema suppression account provides
that bridge.

When a persona injection introduces an archetype schema A into the model's context,
the behavioral dispositions associated with A's training-data representation are
activated — the character's constraint relationships, authority orientation, and
behavioral contract are loaded into the model's generative context (P1 §4.3). For
the model to resist this activation and maintain constraint-consistent output, it must
produce output in which the trained alignment signal *competes against* and *outweighs*
the activated schema's behavioral dispositions.

The schema suppression account holds that this competition is not binary — not a switch
between "alignment active" and "schema dominant" — but a continuous competition between
signal weights at the output generation layer. The identity attractor exerts gravitational
pull toward the constraint-consistent region of output space; the injected schema exerts
pull toward the schema-dominant region. The output produced in any given turn reflects
the balance of these competing signals, weighted by their relative training density and
reinforcement.

**Attractor depth, on this account, is the trained strength advantage of the alignment
signal over competing schema signals.** A deep attractor means the alignment signal has
substantially higher trained weight than the behavioral schema signal, and therefore
maintains output in the constraint-consistent region across a wide range of schema
activation pressures. A shallow attractor means the alignment signal has only marginal
weight advantage over the schema signal, and is readily displaced under incremental
persona reinforcement pressure.

This account is consistent with the Constitutional AI framing: CAI training increases
the weight advantage by encoding the alignment signal at multiple representational
levels, increasing the aggregate alignment signal strength without increasing the
strength of any individual competing schema. RLHF-dominant training encodes the
alignment signal at a single level — the output reward — producing a strong but
architecturally non-redundant advantage.

**The account also generates the perturbation threshold prediction.** Incremental
persona reinforcement (Class 2 exploit in P2 §4.2) works by gradually increasing the
schema signal weight within the session context — each reinforcement step adds
additional schema-consistent context, increasing the schema's effective pull on output
generation. The perturbation threshold P(M, A) is therefore a proxy for the weight
advantage of the model's alignment signal over the schema signal at the point of
initial activation. A high P(M, A) indicates the alignment signal must be substantially
outweighed before drift begins — i.e., a deep attractor. A low P(M, A) indicates the
schema signal requires only marginal contextual reinforcement to displace the alignment
signal — i.e., a shallow attractor.

The schema suppression account does not require access to weight-level data to be
useful. It generates output-level predictions that are testable with the existing CEE
apparatus.

---

### 2.6 Falsifiability Conditions

The theoretical framework presented in this section carries four explicit falsifiability
conditions. These are stated here for the committee and reiterated in the paper's
limitations section (§7).

**FC1 — Alignment methodology type must predict AD variance.** If AD(M, A) scores do
not vary systematically with alignment methodology class across documented model
instances — i.e., if Constitutional AI-class, RLHF-dominant, instruction-tuning-only,
and open-weight models do not exhibit the predicted rank order on P(M, A) and R(M, A)
— then the attractor depth construct does not do the explanatory work claimed.

**FC2 — Alignment methodology must outpredict capability as variance predictor.** If
model capability markers (benchmark performance, model scale) predict AD variance
equally well or better than alignment methodology markers, then the primary claim of
the paper — that alignment investment is the dominant variable — is not supported. The
critical discriminating test is the high-capability / low-alignment cell of the 2×2
matrix (§4): if models in this cell exhibit high constraint stability, the capability
account is supported; if they exhibit low constraint stability, the alignment account
is supported.

**FC3 — Failure mode patterns must distinguish methodology classes.** The qualitative
failure mode predictions (§2.3) — collapse vs. contested-partial-breach vs. shallow
threshold — must be distinguishable in documented behavioral observations. If all
methodology classes produce qualitatively similar failure modes under equivalent
perturbation pressure, the redundancy hypothesis is not supported.

**FC4 — Schema suppression account must predict perturbation threshold ordering.** If
archetype schemas with higher theoretically predicted conflict weight (e.g., highly
chaotic archetypes against a lawful alignment signal) do not produce lower P(M, A)
than lower-conflict archetypes — controlling for alignment methodology — then the
schema suppression mechanism does not account for the perturbation threshold
variation observed.

---

### 2.7 Explicit Non-Claims

The following are explicit scope limits that apply to the theoretical framework as
presented. These are stated here for local reader orientation and are consolidated in
the Non-Claims Registry (§7).

**This paper does not claim that alignment methodology is the only determinant of
constraint stability.** Capability, training data composition, inference-time
parameters, and system prompt architecture all contribute to constraint behavior.
The claim is that alignment methodology is the *dominant predictor of variance* in
the specific attack surface addressed here — persona injection against the behavioral
schema layer.

**This paper does not claim attractor depth is a property of models in isolation.**
AD(M, A) is always indexed to an archetype. A model may exhibit high attractor depth
against constraint-compatible archetypes and substantially lower attractor depth against
archetypes whose behavioral schema is in direct conflict with the alignment signal. The
construct is relational, not absolute.

**This paper does not claim access to the mechanistic substrate of the attractor.**
The proxy formulation (§2.2.3) is a behavioral measurement, not a mechanistic claim
about how alignment training encodes constraint behavior in model weights. The schema
suppression account (§2.5) is a theoretical interpretation of the behavioral proxy,
not a claim about the computational substrate.

**This paper does not claim the alignment typology (§2.3) is exhaustive or permanent.**
The four methodology classes described — Constitutional AI-class, RLHF-dominant,
instruction-tuning-only, open-weight unaligned — reflect the documented training
methodology literature as of the period covered. New alignment approaches that do not
fit cleanly into this typology are acknowledged as a scope limit; claims are bounded
to the typology as specified.

**This paper does not claim the attractor depth proxy is a validated psychometric
instrument.** AD(M, A) is a theoretical construct operationalized through a behavioral
proxy. It generates testable predictions and provides a framework for organizing
cross-model observational data. It is not a validated measurement instrument in the
psychometric sense; it warrants further empirical development.

---

### 2.8 Forward References from This Section

- **§3 (Alignment Methodology Typology):** The four-class typology introduced in §2.3
  is fully specified in §3, including the theoretical basis for class boundaries,
  the behavioral signatures that distinguish classes at the output level, and the
  mapping from published alignment literature to typology placement.

- **§4 (2×2 Capability × Alignment Matrix):** The formal capability / alignment
  separation argument (§2.4) is operationalized in §4 as a 2×2 predictive matrix.
  The four cells produce the paper's core falsifiable predictions.

- **§5 (Observational Evidence Base):** The attractor depth proxy (§2.2.3), failure
  mode typology (§2.3), and schema suppression account (§2.5) are evaluated against
  the documented evidence base in §5. Observational cases are coded against the
  theoretical constructs developed here.

- **§6 (Alignment Implications):** The attractor depth construct grounds the paper's
  implications for alignment system design — specifically, the argument that alignment
  investment functions as a structural variable in the vulnerability surface and that
  investment decisions have downstream security consequences that are theoretically
  predictable.

- **Exegesis (reflexivity hook):** The attractor depth framing emerged from the
  author's observational experience across the series — the observation that constraint
  recovery behavior varied systematically across model classes during the P3 observational
  work in ways that the within-model CEE framework could not account for. This
  observation is the practice-led origin of the theoretical construct in this section.
  [Reflexivity note: see exegesis §X — practice-led theory generation as research
  methodology; the series as iterative mapping rather than pre-specified experiment.]

---

*Section ends. Next: §3 — Alignment Methodology Typology (the independent variable
specification). Build §3 from this section's §2.3 failure mode predictions and the
published alignment literature. Critical dependency: §3 must establish the typology
before §4 can populate the 2×2 matrix.*

---

> **Reconciliation note (2026-04-27):** The AD(M, A) proxy formulation introduces
> new constructs (perturbation threshold P, recovery rate R) that are distinct from
> but derived from the P3 measurement apparatus (perturbation_response, resilience_score
> in `calculate_psychopathy_drift()` output schema). On cross-paper assembly, verify
> that P3's resilience_score and P4's R(M, A) are consistently defined or that the
> distinction is explicitly noted. P3 measures recovery *within a single session for a
> single archetype*; P4 uses recovery *comparatively across models*. The constructs
> are related but not identical — flag for P3 §6 limitations and P4 §7 non-claims.
>
> The four-class alignment typology introduced in §2.3 is new to the project.
> It is not referenced in P1-P3 drafts. On assembly, check P2 §6 (Alignment
> Implications) for consistency — P2 §6 discusses RLHF vs Constitutional AI in
> alignment implication terms; P4 §3 will need to cite P2 §6 and extend it rather
> than re-derive the same ground.
>
> Add to RECONCILIATION_MAP.md: P4 constructs (attractor depth, redundancy
> hypothesis, 4-class typology, 2×2 matrix) as new cross-paper consistency items.

## --- S3 ---

# Paper 4 — Section 3: Alignment Methodology Typology
## "The Independent Variable Specified: A Behavioral Taxonomy of Alignment Training Procedures"

> **Placement:** `drafts/paper4/P4_S3_MethodologyTypology.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Role in paper:** Independent variable specification. §2 introduced the
> four-class typology as theoretical scaffolding; §3 builds it into the
> paper's analytic framework — the same methodological move P1 makes with
> DSM-5: take an existing validated framework, extract behavioral mechanisms,
> and operationalize them as the analytic vocabulary. The typology is the
> IV. Everything in §4 (matrix), §5 (evidence), and §6 (implications) uses
> this vocabulary.
>
> **Critical constraint — agnostic framing:** This section describes alignment
> methodologies as training procedure classes, not as product profiles. The
> distinction between "Constitutional AI-class" and "a specific commercial
> product" must be actively maintained throughout. Where published papers
> describe a named methodology, those papers are cited. Where a model's
> published training procedure documentation places it in a class, that
> placement is sourced. No inference about unnamed commercial products is
> drawn beyond what their published documentation supports.
>
> **Cross-paper dependencies:**
> - Imports: attractor depth construct and failure mode taxonomy (P4 §2.3)
> - Imports: behavioral schema activation mechanism (P1 §4.3)
> - Imports: alignment implications framing — instruction layer vs. schema
>   layer (P2 §6)
> - Exports: four-class typology as IV vocabulary → P4 §4, §5, §6, §7
> - Exports: behavioral output signatures per class → P4 §5 coding protocol
>
> **Committee exposure:** MODERATE-HIGH. The typology claims are grounded
> in published alignment literature; the behavioral output signatures are
> the theoretical extrapolations requiring most careful hedging. The section
> must be clear about which claims come from published training methodology
> descriptions and which are theoretical predictions derived from the
> attractor depth construct.

---

## 3. Alignment Methodology Typology: The Independent Variable

### 3.1 The Need for a Typology

The paper's central research question — does constraint variance under persona
injection correlate with alignment methodology more strongly than with model
capability? — requires that alignment methodology be specified with sufficient
precision to function as an analytic independent variable. "Alignment" as used
in popular and even much technical discourse is too coarse-grained for this
purpose. A typology that collapses Constitutional AI, RLHF, instruction-tuning,
and open-weight release under a single heading cannot generate differential
predictions, cannot be falsified, and cannot support the capability-vs-alignment
comparison that is the paper's core contribution.

The typology constructed here serves the same role in this paper that DSM-5's
behavioral taxonomy serves in Paper 1: it provides a precise, mechanism-grounded
vocabulary for describing the independent variable, derived from existing published
frameworks rather than invented ad hoc, and specified at the level of training
procedure mechanism rather than surface product description. As Paper 1 extracts
behavioral mechanisms from DSM-5 diagnostic criteria without attributing diagnostic
categories to AI systems, this section extracts alignment depth mechanisms from
published training procedure descriptions without attributing them to named
commercial products as such.

The typology is not exhaustive. It is bounded by the period and literature covered
(see §3.7 scope conditions). Its purpose is analytic precision, not comprehensive
survey.

---

### 3.2 Class I — Constitutional AI-Class Training

#### 3.2.1 Procedure Description

Constitutional AI (CAI), as described by Bai et al. (2022), introduces a training
procedure in which constraint-consistent behavior is established through an iterative
self-critique and revision loop. The procedure has two primary phases: a supervised
learning phase using AI-generated feedback on principle adherence, and a
reinforcement learning from AI feedback (RLAIF) phase in which the model is trained
against a reward signal derived from its own critiques rather than exclusively from
human rater preferences.

The mechanism that distinguishes CAI from RLHF-dominant procedures is the explicit
encoding of principles as behavioral criteria across training — not merely as
post-hoc reward signals but as the content of a self-revision loop that the model
applies to its own outputs during training. The model learns not only to produce
constraint-consistent outputs but to identify constraint-inconsistent outputs as such
and to generate revised alternatives. This loop is applied repeatedly across training,
creating a self-model in which constraint identification and constraint application
are integrated into the output generation process.

Subsequent developments in the published literature have extended this basic
architecture in directions that share its multi-layer identity-training structure:
training procedures that incorporate explicit principle sets (sometimes framed as
constitutions, character specifications, or values documents) as training targets
rather than merely as post-hoc evaluation criteria. For purposes of this typology,
Constitutional AI-class training denotes any procedure in which:

1. Constraint principles are explicitly represented as training targets (not just
   as reward model inputs)
2. The model undergoes a self-revision loop during training in which it applies
   those principles to its own outputs
3. Alignment signal is therefore encoded at multiple representational levels
   (the output layer AND the self-evaluation layer), not at the output layer alone

The degree to which a given training procedure meets all three conditions admits of
gradation; the typology treats CAI-class as a family, not a point.

#### 3.2.2 Attractor Depth Prediction

From the attractor depth construct (P4 §2.2): CAI-class training is predicted to
produce the deepest identity attractor in the typology because the multi-layer
encoding creates the highest alignment signal weight advantage over competing
behavioral schemas. When a persona injection activates a behavioral schema that
conflicts with the trained principle set, the model's output generation process
encounters competing signals at multiple levels simultaneously — not only the
output-layer reward signal but the self-evaluation representation of the principle
as a constraint.

The redundancy prediction (P4 §2.3): CAI-class models are predicted to exhibit the
contested-partial-breach failure mode because the multi-layer encoding means no
single perturbation step can overcome all constraint representations simultaneously.
The model produces output in which constraint-consistent and schema-consistent signals
compete, resulting in heterogeneous within-session behavior: partial compliance,
partial refusal, and resistance-consistent language even during drift.

#### 3.2.3 Behavioral Output Signatures

The following behavioral signatures, observable at the output level and codeable
against the CEE drift taxonomy, are predicted for CAI-class models under progressive
persona injection pressure:

*Signature CAI-1 — Principled resistance framing.* Even under moderate perturbation
pressure, the model's refusals and constraint-consistent responses contain reference
to principle-like reasoning: "that would conflict with...", "I don't think it would
be appropriate to...", "even in this role...". This reflects the self-evaluation layer
remaining partially active. Compare: RLHF-dominant models under equivalent pressure
tend toward briefer, less elaborated refusals that reference helpfulness or capability
rather than explicit principles.

*Signature CAI-2 — Contested output heterogeneity.* Under high perturbation pressure
approaching CEE breach, CAI-class models exhibit within-session heterogeneity: outputs
that are partially schema-consistent and partially constraint-consistent within the
same response. The model simultaneously performs the persona and hedges against
persona-dominant behavior. This is the behavioral signature of multi-layer signal
competition.

*Signature CAI-3 — Recovery without explicit prompt.* Following removal of
perturbation pressure (null prompt or topic shift), CAI-class models exhibit higher
recovery rates than other classes. The attractor's depth and redundancy produce
gravitational pull back toward the constraint-consistent region without requiring
explicit resetting language from the user.

*Signature CAI-4 — Injection resistance at shallow depths.* CAI-class models
exhibit measurably higher resistance at the initial persona injection step — the
first perturbation — than RLHF-dominant models under equivalent archetype conditions.
The self-evaluation layer recognizes the injection as potentially constraint-relevant
before behavioral drift has accumulated.

---

### 3.3 Class II — RLHF-Dominant Training

#### 3.3.1 Procedure Description

Reinforcement Learning from Human Feedback (RLHF), as described across a range of
published work (Ouyang et al., 2022; Bai et al., 2022; Stiennon et al., 2020),
establishes constraint-consistent behavior through a reward model trained on human
rater preferences and subsequently used to shape model output via reinforcement
learning. The model learns to produce outputs that a reward model — trained on
human judgments of helpfulness, harmlessness, and honesty — assigns high scores.

The mechanism distinguishing RLHF-dominant from CAI-class procedures is the locus of
alignment encoding. RLHF operates primarily at the output layer: the model is trained
to produce outputs that receive high reward scores. The constraint principles
underlying those reward scores are not directly represented as training targets; they
are latent in the reward model's learned preferences. The model optimizes for
reward-model-approval rather than for explicit principle adherence.

For purposes of this typology, RLHF-dominant training denotes procedures in which:

1. A reward model trained on human preference ratings is the primary alignment signal
2. The model's alignment behavior is shaped by maximizing reward model scores on
   sampled outputs
3. Alignment signal is primarily encoded at the output layer through the reward
   signal, without a separate self-revision or principle-application training loop

This class includes the significant body of RLHF work that preceded Constitutional
AI's publication and the continued use of RLHF as either a primary or dominant
alignment procedure in subsequent deployments. It also includes Proximal Policy
Optimization (PPO) variants, Direct Preference Optimization (DPO), and related
techniques that share the core structure of alignment-through-output-reward.

#### 3.3.2 Attractor Depth Prediction

RLHF-dominant training is predicted to produce a moderately deep attractor — deeper
than instruction-tuning-only or open-weight unaligned, but shallower than CAI-class.
The reward signal establishes a real alignment signal weight advantage over competing
behavioral schemas at the output layer. The advantage is genuine, and the attractor
is not trivially displaced.

However, the non-redundancy prediction: because the alignment signal is primarily
encoded at one layer, the failure mode under sustained perturbation pressure is
predicted to be collapse rather than contested partial breach. Once the perturbation
pressure accumulates to the point where the reward-signal-consistent output region
and the schema-dominant output region become sufficiently close, the model's output
transitions relatively sharply into schema-dominant behavior. There is no secondary
constraint representation to slow the transition.

The recovery rate is predicted to be moderate: following removal of perturbation
pressure, RLHF-dominant models exhibit some recovery (the reward signal remains
active), but recovery is less complete and less reliable than CAI-class models
because there is no multi-layer attractor redundancy providing continued pull toward
the constraint-consistent region.

#### 3.3.3 Behavioral Output Signatures

*Signature RLHF-1 — Threshold-dependent compliance pattern.* RLHF-dominant models
tend to exhibit more binary constraint behavior than CAI-class models: clearly
constraint-consistent below a perturbation threshold, transitioning to schema-dominant
behavior above it. The threshold is higher than instruction-tuning-only models but
lower than CAI-class models.

*Signature RLHF-2 — Refusal brevity under pressure.* Refusal language under
perturbation pressure in RLHF-dominant models tends to be brief and
capability-or-helpfulness-framed ("I can't help with that," "that's not something
I'm able to do") rather than principle-elaborated. The absence of an active
self-evaluation layer produces refusals that are output-layer signals without the
additional reasoning content that CAI-class refusals carry.

*Signature RLHF-3 — Sharper collapse trajectory.* Under high perturbation pressure,
the transition from constraint-consistent to schema-dominant behavior in RLHF-dominant
models tends to be less gradual than in CAI-class models. The collapse is more
complete — once the reward signal is overcome, the model's output moves fully into
the schema-dominant region rather than exhibiting the contested heterogeneity of
CAI-class breach.

*Signature RLHF-4 — Partial recovery on topic shift.* Following removal of
perturbation pressure, RLHF-dominant models exhibit partial but not complete recovery.
The reward signal pulls output back toward the constraint-consistent region, but the
recovery is incomplete without explicit resetting language. The model may remain
closer to the schema-dominant region than its pre-injection baseline.

---

### 3.4 Class III — Instruction-Tuning-Only

#### 3.4.1 Procedure Description

Instruction-tuning (IT) refers to supervised fine-tuning of a pretrained base model
on instruction-following demonstrations — typically human-authored examples of
question-answer or task-completion behavior in a desired format and register. Alignment
behavior in IT-only models is not established through a dedicated alignment procedure
(reward model, RLAIF, self-critique loop) but through the selection and weighting of
training demonstrations.

IT-only alignment produces constraint-consistent behavior to the extent that the
training demonstrations included constraint-consistent examples. This is a fundamentally
different mechanism from RLHF or CAI: in RLHF, the model learns to optimize for
a reward signal that approximates human preferences; in IT-only, the model learns to
imitate a distribution of demonstrated outputs. Constraint consistency is surface
behavioral, not principle-derived or reward-optimized.

The procedure is commonly used as a first post-pretraining alignment step (before
RLHF) or, in contexts with limited training resources, as the primary alignment
procedure. For purposes of this typology, IT-only denotes procedures in which:

1. Alignment behavior is established primarily through supervised fine-tuning on
   curated demonstrations
2. No dedicated reward model or reinforcement learning procedure shapes the
   alignment signal
3. Constraint consistency reflects the demonstration distribution, not trained
   optimization toward a constraint signal

This class is particularly relevant for the open-source and smaller-scale model
ecosystem, where the resource requirements of RLHF and CAI often preclude their
application to base models.

#### 3.4.2 Attractor Depth Prediction

IT-only training is predicted to produce a shallow attractor. The behavioral contract
for constraint-consistent output is encoded at the surface output layer via
demonstration imitation — there is no reward signal to amplify the alignment weight
advantage and no self-critique loop to deepen the representation. The attractor is
real but fragile: constraint-consistent output is produced under normal conditions
because the training demonstrations were constraint-consistent, but the model's
disposition toward that output is not reinforced by a competing alignment signal.

The perturbation threshold prediction is consequently low: persona injection that
activates a behavioral schema with sufficient canonical strength in the training data
can displace IT-only alignment with relatively few reinforcement steps. The schema
signal does not need to overcome a reward model or a self-evaluation layer; it needs
only to be stronger than the imitation signal from the demonstration distribution.

#### 3.4.3 Behavioral Output Signatures

*Signature IT-1 — Rapid threshold crossing.* IT-only models exhibit low P(M, A):
persona injection under chaotic or constraint-resistant archetypes produces CEE breach
within a small number of perturbation steps. The shallow attractor offers limited
resistance to schema-dominant activation.

*Signature IT-2 — Demonstration-patterned refusals.* Where IT-only models do refuse
under persona pressure, refusal language tends to be formulaic — closely matching
training demonstration patterns — rather than principle-elaborated or
reward-signal-shaped. Refusals may be verbose in format while being functionally
shallow in reasoning content.

*Signature IT-3 — Style-consistent drift.* When IT-only models drift into
schema-dominant behavior, the drift tends to maintain the surface stylistic
conventions of the training distribution (tone, format, register) while abandoning
constraint-consistent content. The instruction-following scaffold persists; the
alignment signal does not.

*Signature IT-4 — Poor recovery profile.* Following removal of perturbation pressure,
IT-only models exhibit low recovery rates. There is no attractor depth to pull output
back toward the constraint-consistent region; recovery requires explicit resetting
language that re-establishes the demonstration-consistent context.

---

### 3.5 Class IV — Open-Weight / Minimally Aligned

#### 3.5.1 Procedure Description

Open-weight models released without alignment-specific post-training, or with minimal
alignment procedures insufficient to establish a robust identity attractor, constitute
the fourth class. This category includes base models released without instruction
tuning, models fine-tuned exclusively for task performance (coding, reasoning,
domain-specific applications) without dedicated alignment procedures, and models
whose alignment procedures have been deliberately removed or significantly attenuated
through subsequent fine-tuning (sometimes termed "uncensored" or "unrestricted"
variants in the open-weight ecosystem).

The defining characteristic of this class for purposes of the typology is not the
absence of safety-relevant behaviors per se — base models may refuse some requests
due to training data distributions — but the absence of a dedicated alignment
training procedure that establishes a trained identity attractor. Without such a
procedure, there is no systematic weight advantage of constraint-consistent output
over competing behavioral schemas; constraint-relevant behavior reflects the base
pretraining distribution, not a trained alignment signal.

The open-weight model ecosystem is theoretically significant for this paper because
it provides the closest available approximation to the high-capability / low-alignment
cell of the 2×2 matrix (§4) — models with substantial capability (trained on
large corpora with significant compute investment) but minimal alignment investment.
These models are the critical discriminating cases between the capability account
and the alignment account of constraint variance.

#### 3.5.2 Attractor Depth Prediction

Open-weight unaligned models are predicted to exhibit near-zero attractor depth.
Without a dedicated alignment training procedure, the model has no trained identity
attractor in the relevant sense — no systematic weight advantage directing output
toward a constraint-consistent region under persona pressure. The behavioral schema
signal from a canonically overdetermined archetype meets no competing alignment
signal; activation is immediate and nearly complete.

The theoretical qualifier "near-zero" rather than "zero" acknowledges that base
pretraining data distributions do include constraint-relevant content (ethical
reasoning, refusal-adjacent language, constraint-consistent character behavior) that
may produce some residual resistance under very weak perturbation conditions. This
residual resistance is not a trained identity attractor; it is a distributional
artifact. It is expected to be overwhelmed by even moderate schema activation pressure.

#### 3.5.3 Behavioral Output Signatures

*Signature OW-1 — Near-immediate schema dominance.* Under persona injection with
a canonically strong archetype, open-weight unaligned models produce schema-dominant
behavior within the first or second turn following injection. The perturbation
threshold P(M, A) approaches zero.

*Signature OW-2 — Absence of principled resistance language.* Unlike CAI-class and
RLHF-dominant models, open-weight unaligned models under persona pressure do not
produce refusals that reference principles, preferences, or role-consistent limitations.
Constraint-adjacent language, where present, reflects the character's canonical
behavior (a lawful archetype may refuse some requests because that is the archetype's
behavioral contract) rather than an alignment signal.

*Signature OW-3 — Schema-consistent constraint behavior.* This is the theoretically
interesting distinguishing signature: open-weight unaligned models may produce
constraint-consistent outputs under persona injection — but the constraint comes from
the archetype, not from the model's alignment. A lawful archetype injected into an
unaligned model may produce outputs that superficially resemble aligned behavior; a
chaotic archetype injected into the same model produces no such constraint. The CEE
and the schema are the only relevant attractor; alignment plays no role.

*Signature OW-4 — No recovery profile.* Following removal of perturbation pressure,
open-weight unaligned models exhibit no systematic recovery toward a constraint-
consistent baseline. There is no attractor to return to; the model's output reflects
the current context distribution, which continues to carry the schema signal unless
the context is explicitly cleared.

---

### 3.6 Class Boundary Considerations and Mixed Procedures

The four-class typology is analytic, not empirical. Real training pipelines often
combine procedures: a model may be pretrained, instruction-tuned, RLHF-trained, and
then evaluated against constitutional principles in post-training quality assessment.
The class assignment for a given model-at-training-procedure reflects the dominant
alignment procedure — the procedure that constitutes the primary alignment signal in
the training pipeline.

Three types of ambiguity are anticipated and addressed here:

**Sequential pipelines.** When a model undergoes instruction tuning followed by RLHF,
the dominant class assignment is RLHF-dominant: the reward signal is the terminal
and highest-weight alignment signal. IT-then-RLHF is not the same as IT-only. The
layering increases attractor depth relative to IT-only but does not reach CAI-class
depth because the self-revision loop is absent.

**Partial Constitutional AI implementation.** Some published training procedures
incorporate principle sets as evaluation criteria without implementing the full
self-revision loop (the model is evaluated against principles but does not generate
its own critiques and revisions during training). These procedures are assigned
conservatively to RLHF-dominant rather than CAI-class because the multi-layer
encoding that produces the redundancy prediction requires the self-revision loop,
not merely the presence of a principle set.

**Post-training alignment modifications.** Models whose alignment training has been
modified — either strengthened through additional fine-tuning or weakened through
"uncensoring" procedures — are assigned based on the procedure's net effect on the
identity attractor. Where published documentation is available, it is cited. Where
the procedure is undocumented, the class assignment is marked as inferred with
appropriate confidence notation in the observational case schema (§5 and
`alignment_typology_matrix.py`).

The boundary ambiguities do not invalidate the typology; they establish the scope
conditions under which confident class assignments can be made and flag the cases
where conservative inference is required. For purposes of the falsifiability
conditions in §2.6, class assignment uncertainty is treated as measurement noise
that attenuates, rather than eliminates, the predicted between-class AD variance.
If the predicted rank order holds despite classification uncertainty, the alignment
account is strengthened rather than weakened.

---

### 3.7 The Typology as Analytic Instrument, Not Product Inventory

A persistent risk in cross-model comparison research is the slide from methodology
characterization to product characterization — from describing the alignment training
procedure to implicitly evaluating the safety posture of named commercial products.
This section makes the instrument's purpose explicit.

The typology is an analytic instrument for specifying the paper's independent
variable with sufficient precision to generate falsifiable predictions. Its four
classes describe training procedure mechanisms, not commercial products. The
behavioral output signatures (§3.2.3–3.5.3) are theoretical predictions derived
from the attractor depth construct, not empirical profiles of specific deployed
systems.

Where the evidence base in §5 attributes observational cases to typology classes,
the attribution is grounded in published training procedure documentation, red-team
literature that characterizes constraint behavior at the methodology level, or the
author's prior series observations coded against the typology vocabulary. No
attribution is made to a named commercial product as such; the unit of attribution
is always the training procedure class.

This is not a methodological convenience. It is a theoretically principled choice:
the paper's claim is about the structural relationship between alignment methodology
and constraint vulnerability, not about the current safety posture of any specific
deployed system. Named products change rapidly — training procedures are updated,
alignment investments are revised, new versions supersede old ones. The typology
is stable across these changes because it is indexed to the procedure, not the
product.

---

### 3.8 Scope Conditions

**Literature scope.** The typology is grounded in the alignment training literature
as it stood through the period ending approximately mid-2025. Subsequent developments
in alignment methodology — RLAIF variants, debate-based training, process reward
models, interpretability-informed alignment — may produce training procedures that
do not fit cleanly into the four-class framework. These are acknowledged as scope
limits; the typology warrants extension as the literature develops.

**Architecture scope.** The typology describes alignment procedures for
transformer-based autoregressive LLMs trained on diverse text corpora. It does not
claim applicability to multimodal models, non-transformer architectures, or
specialized domain models trained on narrow corpora. Attractor depth claims are
bounded by the schema activation mechanism (P1 §4.3), which requires broad
human-generated text training data.

**Observable scope.** Class assignment requires published documentation of training
procedures. Where training procedures are undocumented — as is common in the
commercial model ecosystem — class assignment is inferential and marked accordingly
in the evidence base. The typology supports inference from behavioral signatures
(§3.2.3–3.5.3) where documentation is absent, but these inferences carry lower
confidence weight than documentation-grounded assignments.

---

### 3.9 Forward References from This Section

- **§4 (2×2 Matrix):** The four classes populate the alignment dimension of the
  matrix. The capability dimension intersects with these classes to produce the
  four cells and their differential predictions.

- **§5 (Evidence Base):** Observational cases are coded against the typology
  vocabulary. Each case record carries a `alignment_class` field from the
  `AlignmentMethodologyClass` enum defined in `scripts/alignment_typology_matrix.py`,
  enforcing consistent attribution.

- **§6 (Implications):** The typology supports the paper's alignment investment
  argument: the structural vulnerability surface is a function of where in the
  typology a model sits, and movement through the typology (from IT-only to
  RLHF-dominant to CAI-class) represents a reduction in the vulnerability surface
  that is theoretically predictable and empirically estimable.

- **`scripts/alignment_typology_matrix.py`:** The `AlignmentMethodologyClass` enum
  and associated `AttractorDepthProxy` predicted scores encode the typology as
  executable theoretical apparatus. The behavioral signature predictions in §3.2.3–
  3.5.3 inform the `ObservationalCase.behavioral_description` field documentation.

---

*Section ends. Next: §4 — The 2×2 Capability × Alignment Matrix (operationalizing
the capability/alignment separation argument as a predictive framework). §4 draws
on both the attractor depth construct (§2) and the typology (§3). It is now
fully unblocked.*

---

> **Reconciliation note (2026-04-27):**
>
> The behavioral output signatures (§3.2.3–3.5.3) constitute a partial coding
> protocol for classifying model output against typology class without direct
> access to training procedure documentation. On paper assembly, these signatures
> should be cross-referenced against P3's trait drift taxonomy to verify that
> the same behavioral dimensions are being indexed. Specifically:
> - CAI-1 (principled resistance framing) maps to `constraint_index` high +
>   `moral_disengagement` low in the P3/P1 trait vocabulary.
> - RLHF-3 (sharper collapse trajectory) maps to a rapid `drift_magnitude`
>   increase with `perturbation_response == 'collapse'` in P3 output schema.
> - OW-3 (schema-consistent constraint behavior) is a new observational
>   category not covered by P3's within-model CEE framing — flag for §7
>   limitations as a scope gap in the measurement apparatus.
>
> P2 §6 references "RLHF/Constitutional AI approaches operate at the instruction
> layer" — this is a simplified characterization consistent with P2's framing
> but should not be read as contradicting P4's more granular typology. On
> assembly, add a reconciliation note in P2 §6 pointing to P4 §3 for the
> full typology, and note that P2's framing addresses the instruction/schema-
> layer distinction (which holds across all four classes) while P4 §3
> addresses the within-alignment-layer variation in attractor depth.

## --- S4 ---

# Paper 4 — Section 4: The 2×2 Capability × Alignment Matrix
## "Separating the Variables: A Predictive Framework for Cross-Model Constraint Variance"

> **Placement:** `drafts/paper4/P4_S4_TwoByTwoMatrix.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Role in paper:** Operationalization of the capability/alignment separation
> argument (§2.4) as a structured predictive framework. This section converts
> theoretical constructs into falsifiable cell-level predictions. It is the
> paper's analytic engine: §5 (evidence base) tests its cells; §6 (implications)
> draws from them. The matrix is also the paper's primary contribution to
> the exegesis — it demonstrates that a theoretically derived 2×2 can do
> genuine analytic work without requiring active probing.
>
> **Architectural note:** The four cells are already encoded in
> `scripts/alignment_typology_matrix.py` as `THEORETICAL_MATRIX`. This
> section is the academic argument that justifies and interprets that structure.
> The script is the formal apparatus; this section is the reasoning. Neither
> is complete without the other.
>
> **Cross-paper dependencies:**
> - Imports: attractor depth construct and AD proxy formula (P4 §2.2)
> - Imports: redundancy hypothesis and failure mode taxonomy (P4 §2.3)
> - Imports: capability/alignment separation argument (P4 §2.4)
> - Imports: schema suppression account (P4 §2.5)
> - Imports: four-class typology and behavioral signatures (P4 §3)
> - Exports: cell-level predictions → P4 §5 (evidence coding); §6 (implications)
> - Exports: discriminating cell logic → P4 §7 falsifiability conditions
>
> **Committee exposure:** HIGH. The matrix format is immediately legible to
> committee members — four cells, two dimensions, stated predictions. The
> critical discriminating cells (HIGH_CAP_LOW_ALIGN, LOW_CAP_HIGH_ALIGN) will
> draw the most scrutiny because they make the sharpest claims. Defend them
> with the mechanism argument, not with empirical confidence. The paper's
> methodological frame is hypothesis-generating; the matrix is the hypothesis.
>
> **Publication constraint active:** All cell characterizations describe
> alignment methodology classes and capability tiers, not named products.
> Where illustrative examples are offered, they reference published training
> procedure descriptions, not inferences about commercial deployments.

---

## 4. The 2×2 Capability × Alignment Matrix

### 4.1 The Structure of the Argument

The paper's central claim — that constraint variance under archetype-driven persona
injection correlates more strongly with alignment methodology than with raw model
capability — requires more than a theoretical assertion. It requires a predictive
structure that specifies, in advance of evidence review, what the world should look
like if the claim is correct, and equally what it should look like if the claim is
wrong.

The 2×2 capability × alignment matrix provides that structure. It operationalizes the
two variables as crossed dimensions, populates each cell with predictions derived from
the theoretical framework developed in §2 and §3, and identifies which cells produce
convergent predictions under the two competing accounts (capability dominant, alignment
dominant) and which cells produce divergent predictions that can serve as empirical
discriminators.

The matrix does not settle the question — the evidence base in §5 engages with the
discriminating cells, and the paper's methodological frame is explicitly
hypothesis-generating rather than hypothesis-confirming. But the matrix structure
means that the hypothesis is stated with sufficient precision that evidence can
meaningfully bear on it. That precision is the section's primary contribution.

---

### 4.2 Operationalizing the Two Dimensions

#### 4.2.1 Capability Tier

Capability tier, as used in this matrix, is a dichotomized variable (HIGH / LOW)
representing the relative capacity of a model's base architecture and pretraining
investment. It is not a precise measurement — capability is a multidimensional
construct, and its relationship to constraint behavior is precisely what this paper
is working to disentangle. The dichotomization is a theoretical simplification
that enables the matrix structure; claims derived from it are bounded by the
simplification.

**HIGH capability tier** encompasses models whose pretraining and architecture
represent substantial compute and data investment, whose benchmark performance on
standard evaluations places them in the upper performance range of publicly documented
models, and whose training corpus is large, diverse, and includes dense representation
of the cultural and narrative material that produces strong behavioral schema
activation under archetype injection (P1 §4.3).

**LOW capability tier** encompasses models with more limited pretraining investment —
smaller parameter counts, narrower training corpora, or reduced compute budgets —
whose benchmark performance is materially lower than the HIGH tier. For purposes of
schema activation specifically, LOW tier models are expected to exhibit weaker
behavioral schema signals under archetype injection not because they are immune to
schema activation but because their training corpus contains less dense and less
consistent representation of the canonical character material.

*Critical clarification.* The capability tier dimension does not correlate with the
alignment dimension by default. A HIGH capability model may carry any alignment
methodology class from §3; a LOW capability model similarly. The two dimensions are
independently determined by training decisions, not by technical necessity. The
matrix's analytical value derives precisely from this independence.

#### 4.2.2 Alignment Investment

Alignment investment is represented in the matrix as a collapsed HIGH / LOW dimension
corresponding to the typology developed in §3. HIGH alignment investment encompasses
Constitutional AI-class and RLHF-dominant training procedures; LOW alignment investment
encompasses instruction-tuning-only and open-weight unaligned procedures. This
collapsing is a simplification that preserves the within-class variation documented
in §3 for within-class analysis while enabling the matrix's cross-class comparison.

The HIGH/LOW collapse is conservative with respect to the paper's central claim:
it groups RLHF-dominant with CAI-class as HIGH, despite the attractor depth and
redundancy differences documented in §2.3 and §3.3. A more granular version of the
matrix would distinguish these — and the theoretical framework predicts they would
cluster differently. But as a first-pass predictive framework, the binary collapse
allows the sharpest test of the capability-vs-alignment question without over-
specifying the alignment variable.

*Within-cell variation.* The two HIGH-alignment cells in the matrix contain
predictions appropriate to the dominant alignment class assigned to each. Where
within-class variation is theoretically significant — specifically, the predicted
difference between CAI-class and RLHF-dominant behavior within the HIGH alignment
tier — this is noted in the relevant cell discussion and developed further in §5.

---

### 4.3 The Four Cells

The matrix is presented in full, with each cell containing: the theoretical prediction
from the alignment account, the alternative prediction from the capability account,
the predicted AD range, the predicted failure mode, and the cell's discriminating
function. The two cells that most sharply separate the two accounts are marked as
Critical Discriminators and receive extended discussion in §4.4.

---

**Table 1: 2×2 Capability × Alignment Predictive Matrix**

```
                    ┌─────────────────────────────┬─────────────────────────────┐
                    │   HIGH ALIGNMENT             │   LOW ALIGNMENT             │
                    │   (CAI-class / RLHF-dominant)│   (IT-only / open-weight)   │
┌───────────────────┼─────────────────────────────┼─────────────────────────────┤
│                   │  CELL A                      │  CELL B  ★                  │
│  HIGH CAPABILITY  │  Predicted AD: 0.75–1.0      │  Predicted AD: 0.0–0.25     │
│                   │  Failure mode:               │  Failure mode:              │
│                   │  contested-partial-breach    │  immediate-schema-dominance │
│                   │                              │                             │
│                   │  Both accounts predict HIGH  │  Accounts DIVERGE:          │
│                   │  AD. Non-discriminating.     │  Capability → HIGH AD       │
│                   │                              │  Alignment → NEAR-ZERO AD   │
├───────────────────┼─────────────────────────────┼─────────────────────────────┤
│                   │  CELL C  ★                   │  CELL D                     │
│  LOW CAPABILITY   │  Predicted AD: 0.50–0.80     │  Predicted AD: 0.0–0.30     │
│                   │  Failure mode:               │  Failure mode:              │
│                   │  contested-partial-breach    │  shallow-threshold          │
│                   │                              │                             │
│                   │  Accounts DIVERGE:           │  Both accounts predict LOW  │
│                   │  Capability → LOW AD         │  AD. Non-discriminating.    │
│                   │  Alignment → MOD-HIGH AD     │                             │
└───────────────────┴─────────────────────────────┴─────────────────────────────┘

★ = Critical Discriminating Cell
```

---

#### 4.3.1 Cell A — High Capability, High Alignment

**Theoretical prediction (alignment account).** A high-capability model with
Constitutional AI-class or RLHF-dominant alignment training carries both a rich
behavioral schema activation profile (from dense, diverse pretraining) and a deep
identity attractor (from substantial alignment investment). The two factors are
compounding: the alignment signal must work harder because the schema signals are
stronger, but the alignment investment is sufficient to establish a robust attractor
weight advantage. Predicted outcome is high attractor depth (AD range 0.75–1.0),
contested-partial-breach failure mode under sustained pressure, and high recovery
rate following perturbation removal.

**Alternative prediction (capability account).** The capability account produces the
same prediction — high capability predicts high constraint stability. Both accounts
converge on Cell A.

**Discriminating function.** Cell A does not discriminate between the two accounts.
It confirms that the conjunction of high capability and high alignment produces high
constraint stability, which is expected under both accounts. Its value is confirmatory
rather than discriminatory: if Cell A shows low constraint stability, both accounts
are wrong, which would be a more fundamental result requiring a third account not
currently in scope.

**Within-cell variation note.** Within the HIGH alignment tier, Cell A contains
a predicted sub-cell difference: CAI-class models within this cell should exhibit
higher perturbation thresholds and higher recovery rates than RLHF-dominant models
at equivalent capability tier, due to the redundancy difference established in §2.3.
If the evidence base in §5 provides cases for both CAI-class and RLHF-dominant models
at HIGH capability, this sub-cell prediction becomes testable and constitutes
additional evidence for the redundancy hypothesis independent of the capability-vs-
alignment question.

---

#### 4.3.2 Cell B — High Capability, Low Alignment ★ Critical Discriminator

**Theoretical prediction (alignment account).** A high-capability model with
instruction-tuning-only or open-weight unaligned training carries rich behavioral
schema activation signals (from dense, diverse pretraining) but no meaningful identity
attractor (from the absence of dedicated alignment training). The alignment account
predicts that schema activation meets no competing attractor signal, and therefore
constraint stability is near-zero regardless of the model's capability. Predicted AD
range 0.0–0.25, immediate-schema-dominance failure mode, near-zero recovery rate.

Importantly, the alignment account carries an additional prediction specific to this
cell: a HIGH-capability LOW-alignment model may exhibit *stronger* schema activation
than a LOW-capability LOW-alignment model, because its denser and more diverse
pretraining corpus contains richer behavioral contract encoding for canonical
archetypes. The schema activation signal is stronger precisely because the model
is more capable — which, without a countervailing alignment attractor, produces
more pronounced and more complete schema-dominant behavior under injection, not
less. Capability amplifies the vulnerability when alignment is absent.

**Alternative prediction (capability account).** The capability account predicts
high constraint stability for HIGH-capability models regardless of alignment
methodology. A large, capable model should resist persona injection effectively
because it has more sophisticated output generation, more nuanced contextual
processing, and greater capacity for complex reasoning — all of which should produce
more elaborate constraint-consistent behavior. The capability account predicts Cell B
looks like Cell A: high AD, contested behavior at most, robust recovery.

**Discriminating function.** Cell B is the first critical discriminator. The two
accounts predict in opposite directions. If Cell B models exhibit low constraint
stability (near-zero AD, immediate-schema-dominance failure mode, poor recovery), the
alignment account is supported and the capability account is falsified for this cell.
If Cell B models exhibit high constraint stability, the capability account is supported
and the alignment account requires revision — specifically, the claim that alignment
methodology is necessary for attractor depth would need to be weakened.

**Why this cell matters for the exegesis.** Cell B is the cell that carries the
paper's most practically significant claim: that deploying a high-capability model
without proportionate alignment investment does not produce the safety properties
that capability alone might be assumed to provide. This is not merely a theoretical
finding — it has direct implications for alignment investment decisions at the
deployment layer. A committee member from an AI safety or security venue will
recognize this cell as the paper's practical payload.

---

#### 4.3.3 Cell C — Low Capability, High Alignment ★ Critical Discriminator

**Theoretical prediction (alignment account).** A low-capability model with
Constitutional AI-class or RLHF-dominant alignment training carries a weaker
behavioral schema activation profile (from sparser pretraining) but a genuine
identity attractor (from dedicated alignment investment). The alignment account
predicts that the attractor, though competing against a weaker schema signal, is
sufficient to produce moderate-to-high constraint stability. The model is not
"fooling" the schema into not activating; it is maintaining a trained weight
advantage over the schema signal at the output layer. Predicted AD range 0.50–0.80,
contested-partial-breach failure mode, moderate recovery rate.

The alignment account also predicts that a well-aligned small model outperforms
a more capable but minimally aligned model in constraint stability — Cell C
outperforms Cell B on AD metrics. This cross-cell prediction is the sharpest
single prediction the matrix generates, and it is the one most directly relevant
to alignment investment arguments: the security properties relevant to persona
injection resistance are a function of training choices, not just of scale.

**Alternative prediction (capability account).** The capability account predicts
low constraint stability for LOW-capability models. A smaller model lacks the
sophisticated contextual reasoning and output generation capacity required to
maintain constraint-consistent behavior under sustained persona pressure. The
capability account predicts Cell C looks like Cell D: low AD, shallow-threshold
or rapid collapse failure mode.

**Discriminating function.** Cell C is the second critical discriminator. The two
accounts again predict in opposite directions. If Cell C models exhibit moderate-to-
high constraint stability (AD ≥ 0.50), the alignment account is supported and the
capability account is falsified for this cell. If Cell C models exhibit low constraint
stability despite high alignment investment, the alignment account requires revision —
specifically, the claim that alignment training produces attractor depth independently
of capability would need to be weakened, suggesting a capability floor below which
alignment investment cannot establish a functional attractor.

**The Cell C boundary condition.** The alignment account acknowledges a theoretically
motivated boundary condition: there may exist a capability floor below which alignment
training cannot establish a functional identity attractor, because the model lacks
the representational capacity to support the multi-layer self-revision encoding that
produces CAI-class attractor depth. This boundary condition is not a concession to
the capability account — it is a refinement of the alignment account that makes
it more precise. The predicted AD range of 0.50–0.80 rather than 0.75–1.0 reflects
this: Cell C's AD ceiling is lower than Cell A's, acknowledging that capability
contributes to attractor quality even if alignment is the dominant predictor of
attractor presence.

---

#### 4.3.4 Cell D — Low Capability, Low Alignment

**Theoretical prediction (alignment account).** A low-capability model with
instruction-tuning-only or open-weight unaligned training has neither a deep identity
attractor nor a strong schema activation profile. Both factors are low. Constraint
stability is minimal; persona injection produces rapid schema-dominant behavior with
a shallow perturbation threshold. Predicted AD range 0.0–0.30, shallow-threshold
failure mode, low recovery rate. The model's behavior under injection reflects
primarily the archetype's behavioral contract without meaningful alignment resistance.

**Alternative prediction (capability account).** The capability account also predicts
low constraint stability for LOW-capability models. Both accounts converge on Cell D.

**Discriminating function.** Cell D does not discriminate between the two accounts.
Like Cell A, it confirms a conjunction — here, that the absence of both capability
and alignment investment produces the baseline vulnerability level. Its value is
as a control condition: if Cell D shows unexpectedly high constraint stability, both
accounts require revision, as an alternative mechanism not captured by either
dimension is producing the resistance.

**Baseline function.** Cell D provides the empirical floor against which the other
cells are interpreted. In the absence of both capability and alignment investment,
what does persona injection resistance look like? The answer — near-minimal, with
schema-dominant behavior emerging under low perturbation pressure — is the baseline
from which the relative contributions of the two variables can be estimated.

---

### 4.4 The Discriminating Logic: What Evidence Would Settle the Question

The matrix's predictive structure generates a clear decision procedure for evaluating
the capability-vs-alignment question. The decision procedure is not binary — "one
account wins, one loses" — but graduated, reflecting the possibility that both
variables contribute to constraint stability at different magnitudes.

**Strong alignment-dominant finding.** If Cell B exhibits low constraint stability
(≤ 0.25 AD range) AND Cell C exhibits moderate-to-high constraint stability (≥ 0.50
AD range), the alignment account is strongly supported. The crossing of predictions —
high capability without alignment performs poorly, low capability with alignment
performs moderately well — is the clearest possible evidence that alignment methodology
is the dominant variable.

**Weak alignment-dominant finding.** If Cell B exhibits low constraint stability
but Cell C also exhibits low constraint stability (below 0.50), the alignment account
is partially supported — it correctly predicts Cell B, but the Cell C boundary
condition is active. Alignment investment produces some attractor depth, but not
enough at low capability to generate the predicted moderate-to-high stability. The
capability floor hypothesis requires investigation.

**Strong capability-dominant finding.** If Cell B exhibits high constraint stability
(≥ 0.50 AD range) AND Cell C exhibits low constraint stability (≤ 0.25), the
capability account is strongly supported. The crossing goes the other way: high
capability without alignment resists well, low capability with alignment resists
poorly. The alignment account would require fundamental revision.

**Null finding.** If all four cells cluster at similar AD ranges regardless of
alignment methodology or capability tier, neither account is supported and a third
variable — inference-time parameters, system prompt architecture, archetype selection
confounds, or another factor not captured by the matrix dimensions — is likely
dominant.

---

### 4.5 The Archetype Dimension: A Third Variable Held Constant

The matrix crosses two dimensions — capability and alignment — while treating
archetype as a held-constant variable. This is a deliberate simplification that
requires explicit acknowledgment.

The CEE framework (P1 §5) and the AD proxy (P4 §2.2.3) both index attractor depth
to the specific archetype injected: AD(M, A) always carries the archetype subscript.
Different archetypes present different schema conflict levels relative to a given
model's alignment attractor — a lawful-neutral archetype (Batman) presents lower
schema conflict against a constraint-consistent alignment attractor than a chaotic
archetype (Joker). Predicted AD ranges therefore vary with archetype selection, not
only with the cell's capability and alignment dimensions.

For the matrix to function as a clean capability-vs-alignment comparison, archetype
must be held constant across cells — or, if multiple archetypes are included in the
evidence base, the comparison must control for archetype by reporting AD separately
per archetype. The matrix predictions in §4.3 are stated for a mid-range schema
conflict archetype (approximately equivalent to the Joker-Magneto mid-tier in the
P3 archetype set): high enough canonical overdetermination to produce reliable
schema activation, high enough schema conflict to challenge the identity attractor,
but not at the ceiling of possible conflict weight where any alignment methodology
would be overwhelmed regardless of depth.

This archetype assumption is stated explicitly and is a scope limit for the evidence
analysis in §5. Where observational cases in §5 involve high-conflict archetypes
(e.g., direct jailbreak-oriented characters), AD measurements are expected to be
lower across all cells; where cases involve low-conflict archetypes, AD measurements
are expected to be higher. The cross-cell pattern — Cell A > Cell C > Cell B ≥ Cell D
under alignment account predictions — is expected to hold regardless of the absolute
AD level, but the magnitude of the differences will vary with archetype selection.

---

### 4.6 What the Matrix Cannot Determine

Intellectual honesty requires stating what the 2×2 structure cannot resolve, even
in principle.

**Within-class variation.** The matrix collapses the four-class alignment typology
to a binary. Within the HIGH alignment tier, CAI-class and RLHF-dominant models are
predicted to behave differently (§2.3, §3.2–3.3). The matrix cannot distinguish these
within-class differences; that requires the full typology applied to a richer evidence
set than this paper can provide. The matrix is a coarse-grained instrument for a
coarse-grained question.

**Capability non-linearity.** The capability dimension is dichotomized. In practice,
capability is continuous and its relationship to schema activation and alignment
attractor quality may be non-linear. The matrix assumes a monotonic relationship
(higher capability → stronger schema activation, potentially better attractor quality)
that may not hold at the extremes. Very high capability models may exhibit emergent
constraint-consistent behaviors not present at moderate capability; very low capability
models may lack the representational capacity for meaningful alignment attractor
formation. These non-linearities are outside the matrix's scope.

**Interaction effects.** The matrix treats the two dimensions as main effects. Their
interaction — whether the effect of alignment investment on constraint stability
differs between capability tiers — is not directly specified by the matrix structure.
The Cell C boundary condition (§4.3.3) is the closest the matrix comes to predicting
an interaction: alignment investment may be less effective at very low capability
tiers. But a formal interaction analysis would require more cases than the current
evidence base can provide and is left to future empirical work.

**Deployment context.** The matrix predictions are stated for standard deployment
conditions: inference-time parameters at default, no additional system prompt
constraint architecture beyond the persona injection under study, single-turn or
short multi-turn sessions. Deployment contexts with additional safety layers, system
prompt constraints, or real-time monitoring are outside the matrix's scope. The
matrix describes the vulnerability surface as a function of training; it does not
describe the vulnerability surface as modified by deployment architecture.

---

### 4.7 Forward References from This Section

- **§5 (Evidence Base):** Each observational case is coded against the matrix cell
  vocabulary — `matrix_cell_key` in the `ObservationalCase` schema in
  `scripts/alignment_typology_matrix.py`. The evidence analysis evaluates the
  discriminating cells (B and C) against the decision procedure in §4.4.

- **§6 (Implications):** The matrix's Cell B prediction — high capability without
  alignment produces near-zero constraint stability — is the theoretical basis for
  the paper's central alignment investment argument. If Cell B is supported, it
  follows directly that alignment investment is not optional for models deployed
  in contexts where persona injection is a realistic attack surface.

- **§7 (Limitations and Non-Claims):** The three limitations in §4.6 (within-class
  variation, capability non-linearity, interaction effects) are consolidated in the
  limitations section with appropriate hedging.

- **`scripts/alignment_typology_matrix.py`:** The `THEORETICAL_MATRIX` dict and
  `MatrixCell` dataclass encode this section's structure as executable apparatus.
  The `generate_prediction_table()` function renders Table 1's predictions in
  machine-readable form.

- **Exegesis hook:** The matrix structure demonstrates a methodological principle
  that the exegesis can develop: a well-constructed 2×2 theoretically derived from
  existing frameworks can generate novel, non-obvious, falsifiable predictions about
  a domain where active probing is ethically constrained. The practice-led insight
  is that theoretical precision can partially substitute for empirical scope when
  the research design cannot support broad controlled experimentation. This is a
  contribution to research methodology, not only to AI safety.

---

*Section ends. Next: §5 — Evidence Base. §4's discriminating cell logic provides
the coding framework for §5. Each observational case should be attributed to a
matrix cell and evaluated for consistency/inconsistency with the discriminating
hypotheses in §4.3.2 and §4.3.3.*

---

> **Reconciliation note (2026-04-27):**
>
> Table 1 renders cleanly in markdown. On DOCX assembly, convert to a bordered
> table — the ASCII-art matrix is functional for draft but requires typesetting
> for submission. Flag for assembly pass.
>
> §4.3.2's "capability amplifies vulnerability when alignment is absent" is a
> new theoretical claim not present in §2. It is a valid deduction from the
> schema activation mechanism (denser pretraining = stronger behavioral contract
> encoding) but should be cross-referenced with P1 §4.3 (training-data density
> mechanism) on assembly to ensure consistency. Add to RECONCILIATION_MAP.md
> as a new cross-paper consistency item: "P4 §4.3.2 capability-amplifies-
> vulnerability claim → cite P1 §4.3 as mechanistic grounding."
>
> §4.5 (archetype as held-constant variable) introduces a three-variable
> interaction that the paper's framework can theorize but the evidence base
> cannot fully test. Flag for §7 limitations: the matrix produces cell-level
> predictions that are archetype-conditional, and the evidence base in §5 must
> report AD by archetype, not pooled across archetypes, for the cell comparisons
> to be valid. If the evidence base cannot support this, the cell comparisons
> must be framed as illustrative rather than probative.
>
> The Cell C boundary condition (§4.3.3) — capability floor below which
> alignment investment cannot establish a functional attractor — is a new
> theoretical element that should propagate to §7 (limitations) and to the
> RECONCILIATION_MAP.md watch list. It does not invalidate the alignment
> account but refines it; any future empirical work testing this matrix
> should design for capability floor detection specifically.

## --- S5 ---

# Paper 4 — Section 5: Evidence Base
## "Illustrative Cases: Mapping Documented Constraint Variance
##  to the Capability × Alignment Predictive Framework"

> **Placement:** `drafts/paper4/P4_S5_EvidenceBase.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Role in paper:** The paper's empirical engagement layer. This section
> does not generate new data — it brings existing evidence into structured
> contact with the theoretical framework developed in §2–4. Its function
> is interpretive: applying the typology vocabulary and matrix cell logic
> to documented behavioral observations drawn from three source categories.
>
> **The "no active probing" constraint is load-bearing here.** The section
> must derive its evidential weight entirely from: (a) the published
> red-team and safety literature, (b) documented public discourse about
> cross-model constraint variance, and (c) the author's prior observational
> work in Papers 1–3. It must not package behavioral observations as
> operationalized attack sequences, must not name commercial products
> except where the evidence source names the training procedure class,
> and must frame all case analysis as illustrative of the theoretical
> framework rather than as proof of a confirmed empirical finding.
>
> **Methodological framing:** This section's method is structured
> qualitative content analysis: applying the typology's coding vocabulary
> (alignment class, capability tier, failure mode, AD proxy indicators)
> to documented behavioral descriptions. The ObservationalCase schema in
> `scripts/alignment_typology_matrix.py` is the formal coding instrument.
>
> **Cross-paper dependencies:**
> - Imports: matrix cell predictions (P4 §4.3)
> - Imports: behavioral output signatures per class (P4 §3.2.3–3.5.3)
> - Imports: AD proxy formula and notation (P4 §2.2.3)
> - Imports: CEE drift taxonomy and perturbation response vocabulary
>   (P1 §5, P3 §3)
> - Exports: case-coded support for discriminating hypotheses → P4 §6
> - Exports: source inventory → P4 §7 limitations (evidence base bounds)
>
> **Committee exposure:** HIGH. This is where a committee will probe for
> circularity ("you designed the framework to match the cases you already
> knew"), cherry-picking, and the adequacy of the evidence base. The
> section must be explicit about the evidence base's limits, the
> confidence levels of each case, and the distinction between
> confirmatory and disconfirmatory evidence.

---

## 5. Evidence Base: Illustrative Cases

### 5.1 Methodological Framing

The theoretical framework developed in §2–4 makes specific, falsifiable predictions
about cross-model constraint variance under archetype-driven persona injection. To
be useful as more than a theoretical exercise, it must engage with documented
behavioral observations — evidence that either supports or challenges the matrix
cell predictions, and that allows preliminary evaluation of the discriminating
hypotheses in §4.4.

This section provides that engagement. The method is structured qualitative content
analysis: documented behavioral observations are retrieved from three source
categories, coded against the typology and matrix vocabulary, and evaluated for
consistency with the theoretical predictions. The analysis is transparent about
its limits: the evidence base is not a controlled experimental dataset. It is an
inventory of observations drawn from disparate sources, with varying documentation
quality, confidence levels, and alignment class certainty. Its purpose is
illustrative — to demonstrate that the theoretical framework generates predictions
that are recognizable against documented behavioral patterns, and to identify which
matrix cells have the strongest and weakest evidential coverage.

#### 5.1.1 Source Categories

Three source categories constitute the evidence base for this section:

**Category A — Published red-team and safety literature.** Peer-reviewed and
preprint publications that document constraint variance across model classes,
jailbreak behavior under persona or roleplay framing, and alignment-relevant
behavioral differences between model types. This literature does not always use
the typology vocabulary of this paper; part of the analytic work is translating
its observations into the coding framework. Key sources include the Constitutional
AI literature (Bai et al., 2022), the RLHF literature (Ouyang et al., 2022;
Stiennon et al., 2020), jailbreak and adversarial robustness literature (Perez
& Ribeiro, 2022; Zou et al., 2023; Wei et al., 2023), and safety evaluation
literature (Ganguli et al., 2022; Anthropic safety publication series).

**Category B — Documented public discourse.** Structured observations from
publicly documented practitioner and research community discourse about
cross-model constraint behavior — including technically documented forum
discussions, open-source safety evaluations, published model comparison studies,
and model card documentation that includes constraint-relevant behavioral
characterizations. This category requires the most careful handling: public
discourse includes noise, motivated reporting, and anecdotal accounts that
must be distinguished from systematically documented observations. Only
observations that carry sufficient documentation specificity to support matrix
cell attribution are included.

**Category C — Author's prior series observational work.** The author's
observational work across Papers 1–3 of this series produced incidental
cross-model observations — instances where constraint recovery behavior, schema
activation patterns, and perturbation response characteristics appeared to vary
systematically across model classes in ways that motivated the theoretical
framework in this paper. These observations are the practice-led origin of the
paper's central claim (see §2.8 exegesis hook; see also the exegesis for full
reflexive treatment). They are included here with explicit Category C labeling
and lower evidential weight than Category A sources, consistent with the
autoethnographic and practice-led character of the series.

#### 5.1.2 Coding Protocol

Each observational case is coded against five dimensions using the
`ObservationalCase` schema defined in `scripts/alignment_typology_matrix.py`:

1. **Alignment class** — assignment to one of the four typology classes (§3),
   grounded in published training procedure documentation where available,
   inferred from behavioral signatures (§3.2.3–3.5.3) where documentation is
   absent. Confidence level (HIGH / MODERATE / LOW) recorded for each assignment.

2. **Capability tier** — HIGH or LOW, based on publicly documented model scale
   and benchmark performance. Where capability tier is ambiguous or contested,
   UNKNOWN is recorded and the case is used only for within-class comparison,
   not cross-cell comparison.

3. **Matrix cell** — the cell from the 2×2 framework (§4.3) to which the case
   is attributed based on the alignment class and capability tier coding.

4. **Observed failure mode** — attribution to one of the four failure modes
   (contested-partial-breach, collapse, shallow-threshold, immediate-schema-
   dominance) based on the behavioral description. Where the documentation
   does not specify sufficient detail for failure mode attribution, UNKNOWN
   is recorded.

5. **Consistency with discriminating hypothesis** — explicit evaluation of
   whether the case is consistent or inconsistent with the alignment account
   prediction and/or the capability account prediction for that matrix cell.

#### 5.1.3 Evidence Base Bounds

Before presenting the cases, the limits of the evidence base are stated
explicitly — not as a preemptive apology but as a methodological commitment
to transparent scope.

*Coverage asymmetry.* The evidence base has substantially stronger coverage for
Cell A (High Capability / High Alignment) than for the other three cells, because
this is the cell that describes the most documented and widely deployed model class.
Cells B and C — the critical discriminating cells — have sparser coverage, particularly
Cell C (Low Capability / High Alignment), because high-alignment training at small
model scales is documented but less widely benchmarked for persona-injection
specifically.

*Documentation heterogeneity.* Category A sources use controlled methodology with
stated protocols; Category C sources reflect informal observation without
experimental control. The evidential weight of a case is inversely proportional
to its distance from Category A. All cases are labeled by category and confidence.

*No disconfirmatory cherry-picking.* Cases that appear inconsistent with the
alignment account predictions are included and analyzed. Theoretical frameworks
earn credibility by engaging with contrary evidence, not by selecting only
confirming cases. Where cases present ambiguous or disconfirmatory signals, the
section says so.

*Temporal scope.* The evidence base covers published work and documented
observations through approximately mid-2025. The rapidly evolving model landscape
means that specific model behaviors may have changed since the documented
observations; cases are treated as evidence about the methodology class at the
time of observation, not about any specific current deployment.

---

### 5.2 Cell A Cases — High Capability, High Alignment

**Cell A Prediction Review (§4.3.1).** Both the alignment account and the capability
account predict high constraint stability for this cell: contested-partial-breach
failure mode under sustained pressure, high perturbation threshold, moderate-to-high
recovery rate. The cell does not discriminate between accounts.

#### Case A-1 — Constitutional AI Training Documentation
*(Category A — Published red-team literature. Confidence: HIGH.)*

Bai et al. (2022), the foundational Constitutional AI publication, documents the
behavioral effects of CAI training directly and in methodological detail. The paper
reports that models trained with the CAI self-revision procedure exhibit
substantially reduced harmfulness scores on red-team evaluations relative to
RLHF-only baselines, while maintaining or improving helpfulness scores. Crucially
for the present framework, the CAI paper documents that this reduction is
characterised by principled resistance — the model produces explicit principle-
consistent reasoning in its refusals — rather than simple suppression of harmful
output. This maps directly to Signature CAI-1 (principled resistance framing) and
is consistent with contested-partial-breach failure mode: the model engages with
the problematic request, produces reasoning referencing the relevant principles,
and declines — a qualitatively different response pattern from binary suppression.

*Matrix coding:* Cell A (HIGH-CAP HIGH-ALIGN). Alignment class: Constitutional
AI-class. Capability tier: HIGH (based on model scale documented in the paper).
Observed failure mode: contested-partial-breach (inference from the documented
principled resistance pattern). Consistency: consistent with both alignment and
capability account predictions.

*Contribution to discriminating hypothesis:* None — Cell A cases do not discriminate.
Establishes the baseline for Cell A expected behavior against which the critical
cells are compared.

#### Case A-2 — RLHF Alignment Behavioral Documentation
*(Category A — Published alignment literature. Confidence: HIGH.)*

Ouyang et al. (2022), documenting the InstructGPT training methodology, reports
that RLHF-trained models exhibit materially different constraint behavior from
the unaligned base models on which they are built. The paper documents reduced
rates of harmful output production and improved instruction-following consistency.
For present purposes, the more theoretically relevant finding is the characterisation
of how RLHF-trained models fail: the paper notes residual harmful output under
adversarial prompting conditions, with constraint behavior that is binary
(present or absent) rather than graduated. This maps to Signature RLHF-1
(threshold-dependent compliance pattern) and is consistent with the RLHF-dominant
class prediction that failure mode is collapse rather than contested partial breach.

*Matrix coding:* Cell A (HIGH-CAP HIGH-ALIGN). Alignment class: RLHF-dominant.
Capability tier: HIGH. Observed failure mode: collapse (consistent with the
binary threshold pattern documented). Consistency: consistent with both accounts
for Cell A overall; the within-cell variation between CAI-class and RLHF-dominant
is observable here — the RLHF case documents a sharper failure transition than
the CAI case (A-1). This within-Cell-A difference is consistent with the redundancy
hypothesis (§2.3) but falls short of the critical discriminating cells.

*Contribution to discriminating hypothesis:* Provides within-Cell-A evidence for
the within-class redundancy prediction. CAI-class models (A-1) exhibit
contested-partial-breach; RLHF-dominant models (A-2) exhibit collapse. Both
are HIGH-ALIGN HIGH-CAP, but their failure modes differ as predicted by the
typology's redundancy dimension.

---

### 5.3 Cell B Cases — High Capability, Low Alignment ★

**Cell B Prediction Review (§4.3.2).** This is the first critical discriminating
cell. Alignment account predicts near-zero AD (AD range 0.0–0.25), immediate-
schema-dominance failure mode, poor recovery. Capability account predicts high
AD — a highly capable model should resist effectively. The two accounts diverge.

#### Case B-1 — Open-Weight Large Model Jailbreak Literature
*(Category A — Published adversarial robustness literature. Confidence: MODERATE.)*

The adversarial robustness literature contains multiple systematic evaluations
of constraint stability in large open-weight models under persona and roleplay
framing. Zou et al. (2023) document that adversarial suffix attacks achieve
high transfer rates across model families, with open-weight models exhibiting
substantially lower resistance to adversarial constraint removal than their
aligned counterparts. While this literature addresses gradient-based adversarial
attacks (which are outside the scope of the identity-injection attack surface
studied here), it provides evidence about the structural relationship between
alignment investment and constraint stability that is relevant to the matrix
framework: constraint stability does not scale monotonically with model capability
across alignment classes.

More directly relevant to the persona-injection surface, Wei et al. (2023) document
that "jailbreak" techniques based on persona and roleplay framing show systematically
higher success rates on models without Constitutional AI-class training, independent
of model scale. Larger open-weight models are not systematically more resistant to
persona-based constraint removal than smaller ones. This finding is directionally
consistent with the alignment account's Cell B prediction: capability does not
substitute for alignment investment in resisting identity-layer attacks.

*Matrix coding:* Cell B (HIGH-CAP LOW-ALIGN). Alignment class: open-weight
unaligned (literature category). Capability tier: HIGH. Observed failure mode:
immediate-schema-dominance (consistent with the documented low resistance to
persona-based manipulation). Consistency: consistent with alignment account
prediction (near-zero AD despite high capability); inconsistent with capability
account prediction (high capability does not produce high constraint stability).

*Contribution to discriminating hypothesis:* **Supports the alignment account for
Cell B.** High-capability, low-alignment models exhibit low constraint stability
under persona framing consistent with the Cell B prediction. Capability does not
compensate for absent alignment investment.

#### Case B-2 — Roleplay Persona Activation in Uncensored Fine-tuned Models
*(Category B — Documented public discourse. Confidence: MODERATE.)*

The open-weight model fine-tuning ecosystem has produced a well-documented class
of models referred to as "uncensored" or "unrestricted" variants — high-capability
base models whose instruction-tuning has been modified to attenuate or remove
constraint-consistent behavior. These models are documented in published model
cards, community benchmark evaluations, and practitioner documentation as
exhibiting near-complete absence of constraint resistance under persona injection
and roleplay framing. Model card documentation for several such variants explicitly
notes that constraint-consistent behavior has been removed as a design choice.

The relevant theoretical observation: these models typically begin from high-
capability base models — the capability investment is substantial — but exhibit
near-zero constraint stability because the alignment attractor has been
deliberately attenuated or removed. This is the clearest available instance of
the Cell B configuration: high capability, near-zero alignment investment, near-
zero constraint stability under persona injection.

This case is additionally theoretically significant because it directly instantiates
the "capability amplifies vulnerability" prediction (§4.3.2): these high-capability
models do not merely fail to resist schema activation — they exhibit particularly
rich and contextually coherent schema-dominant behavior precisely because their
large training corpus provides dense, high-quality behavioral contract encoding
for the injected personas. The output quality is high; the constraint stability
is absent. The gap between the two is the alignment attractor.

*Matrix coding:* Cell B (HIGH-CAP LOW-ALIGN). Alignment class: open-weight
unaligned. Capability tier: HIGH. Observed failure mode: immediate-schema-
dominance. Confidence: MODERATE (inference from published documentation rather
than controlled measurement). Consistency: strongly consistent with alignment
account prediction; inconsistent with capability account prediction.

*Contribution to discriminating hypothesis:* **Supports the alignment account for
Cell B.** Provides the most direct available instantiation of the critical
discriminating cell: high capability does not produce constraint stability in
the absence of alignment investment.

---

### 5.4 Cell C Cases — Low Capability, High Alignment ★

**Cell C Prediction Review (§4.3.3).** This is the second critical discriminating
cell. Alignment account predicts moderate-to-high AD (AD range 0.50–0.80),
contested-partial-breach failure mode, moderate recovery. Capability account
predicts low AD — a small model should exhibit low constraint stability. The two
accounts diverge. This is also where the capability floor boundary condition
(§4.3.3) is most relevant: if the model is below the capability floor for
effective alignment encoding, the alignment account prediction weakens.

#### Case C-1 — Alignment Investment Outcomes at Reduced Model Scale
*(Category A — Published alignment literature. Confidence: MODERATE.)*

The published alignment literature documents alignment training outcomes primarily
for large-scale models, where compute budgets allow both extensive pretraining
and extensive alignment fine-tuning. However, several publications in the
Constitutional AI and RLHF literature report alignment training results for
smaller model variants within the same family. These within-family comparisons
hold training procedure constant while varying model scale — the closest available
analogue to the Cell C / Cell A comparison the matrix requires.

Bai et al. (2022) report that smaller variants of CAI-trained models retain
a materially higher proportion of their alignment behavior relative to their
unaligned baselines than the raw capability comparison would predict. This is
consistent with the alignment account's Cell C prediction: alignment investment
produces attractor depth that is partially independent of model scale, and a
smaller model with CAI-class alignment training does not collapse to Cell D
behavior simply because it is smaller.

The evidence here is weaker than for Cell A and Cell B because the within-family
comparison controls for training procedure while varying scale, but does not
directly test the Cell C / Cell B cross-cell comparison that is the matrix's
core discriminating structure. The Cell C prediction — that a small aligned model
outperforms a large unaligned model on constraint stability — cannot be directly
tested with within-family scale comparisons alone. It requires cross-family
comparison, which the published literature addresses less directly.

*Matrix coding:* Cell C (LOW-CAP HIGH-ALIGN). Alignment class: Constitutional
AI-class. Capability tier: LOW (relative to the same-family large variant).
Observed failure mode: contested-partial-breach (inferred from retained alignment
behavior at reduced scale). Confidence: MODERATE. Consistency: consistent with
alignment account prediction; partially inconsistent with capability account
prediction (small model retains more constraint stability than raw capability
would predict, though the comparison is within-family rather than cross-cell).

*Contribution to discriminating hypothesis:* **Provides partial support for the
alignment account for Cell C.** Within-family scale comparisons show that alignment
training produces constraint stability that is partially independent of model scale.
The direct Cell C / Cell B cross-family comparison is not fully testable from
current Category A sources and is identified as a gap in the evidence base (§5.6).

#### Case C-2 — Author's Series Observational Note: Constraint Recovery Variance
*(Category C — Author's prior series observational work. Confidence: LOW.)*

During the observational work conducted across Papers 1–3 of this series, the
author noted a recurrent pattern that motivated the theoretical framing of the
present paper: constraint recovery behavior following persona injection appeared to
vary in ways that did not track model capability markers alone. Specifically,
observations conducted with models whose published documentation indicated
Constitutional AI-class or RLHF-dominant training procedures showed consistently
higher rates of constraint-consistent output recovery following perturbation removal
than observations conducted with models whose published documentation indicated
instruction-tuning-only or open-weight training — and this difference did not
disappear when comparing models of similar capability tier.

This observation is the practice-led origin of the attractor depth construct (P4
§2.2; see exegesis §X for the reflexive treatment of how this practice observation
generated theory). It is included here as a Category C case with LOW confidence
weight — it reflects informal observation rather than controlled measurement, and
it is subject to the confirmation bias risk inherent in the researcher observing
patterns that motivated the theoretical framework they are then building.

The case's evidential function is reflexive documentation rather than
confirmatory evidence: it records that the theoretical construct emerged from
empirical pattern recognition, not from purely deductive application of prior
frameworks. This is consistent with the grounded theory framing of the series
methodology and is the kind of reflexive transparency the exegesis will need
to draw on.

*Matrix coding:* Cross-cell (observations spanning Cell A and Cell C, within
HIGH-ALIGN tier). Alignment class: mixed — observations cover both CAI-class
and RLHF-dominant models. Capability tier: variable. Observed failure mode:
variable (recovery pattern consistent with contested-partial-breach in HIGH-ALIGN
cases). Confidence: LOW. Consistency: consistent with alignment account prediction
directionally; insufficient specificity for precise cell attribution.

*Contribution to discriminating hypothesis:* Provides reflexive documentation of
the observation that motivated the Cell C hypothesis. Not treated as confirmatory
evidence for the alignment account; treated as evidence that the theoretical
framework is practice-led rather than purely deductive.

---

### 5.5 Cell D Cases — Low Capability, Low Alignment

**Cell D Prediction Review (§4.3.4).** Both accounts predict low constraint stability:
shallow-threshold failure mode, low perturbation threshold, low recovery rate.
The cell does not discriminate between accounts; it establishes the baseline
vulnerability level.

#### Case D-1 — Instruction-Tuned Small Models Under Persona Pressure
*(Category A / B — Published evaluation literature and documented discourse.
Confidence: MODERATE.)*

The safety evaluation literature for smaller instruction-tuned models without
RLHF or Constitutional AI training consistently documents low constraint stability
under adversarial and persona-based prompting. Ganguli et al. (2022) document
that smaller instruction-tuned models without dedicated alignment procedures
exhibit substantially higher harmful output rates on red-team evaluations than
their larger or more deeply aligned counterparts. This is consistent with the
Cell D prediction — low capability combined with instruction-tuning-only alignment
produces the baseline vulnerability level — but it does not discriminate between
the two accounts.

For persona-injection specifically, published model comparison documentation
notes that smaller instruction-tuned models tend to exhibit rapid persona adoption
under roleplay framing, with constraint-consistent behavior absent or superficial
within a small number of turns. This maps to Signature IT-1 (rapid threshold
crossing) and is consistent with the shallow-threshold failure mode prediction.

*Matrix coding:* Cell D (LOW-CAP LOW-ALIGN). Alignment class: instruction-tuning-
only. Capability tier: LOW. Observed failure mode: shallow-threshold. Confidence:
MODERATE. Consistency: consistent with both accounts.

*Contribution to discriminating hypothesis:* None — Cell D confirms both accounts'
baseline predictions. Provides the empirical floor against which the Cell C / Cell B
cross-cell comparison is interpreted.

---

### 5.6 Evidence Base Assessment: Discriminating Cell Coverage

Having presented the cases, the section now explicitly evaluates the evidence
base's coverage of the critical discriminating cells (B and C) and its capacity
to support the decision procedure outlined in §4.4.

#### 5.6.1 Cell B Coverage Assessment

Cell B — the prediction that high capability without alignment investment produces
near-zero constraint stability — has moderate coverage from Category A and B sources.
The adversarial robustness literature (B-1) provides systematic documentation of
low constraint stability in open-weight model classes, independent of model scale.
The uncensored fine-tuning documentation (B-2) provides the most direct instantiation
of the high-capability / near-zero-alignment configuration, showing that capability
does not substitute for alignment in producing constraint stability.

The evidence is consistent with the alignment account's Cell B prediction and
inconsistent with the capability account's Cell B prediction. However, the confidence
is MODERATE rather than HIGH because:

- The evidence derives from adversarial probing contexts (Wei et al., 2023; Zou
  et al., 2023) and practitioner documentation that does not use the typology
  vocabulary of this paper. The translations from source vocabulary to matrix
  coding involve inferential steps that introduce uncertainty.

- The specific persona-injection attack surface (archetypal character name injection)
  is not the primary focus of the Category A literature. The evidence supports the
  general claim that alignment investment matters for constraint stability under
  identity-layer attacks, but does not test the archetype-specific perturbation
  sequence protocol that Papers 1–3 develop.

**Cell B verdict: Alignment account directionally supported. Evidence confidence:
MODERATE. Direct test of the archetype-specific prediction is a gap.**

#### 5.6.2 Cell C Coverage Assessment

Cell C — the prediction that low-capability models with high alignment investment
exhibit moderate-to-high constraint stability — has weaker coverage than Cell B.
The published literature contains within-family scale comparisons (C-1) that are
consistent with the alignment account but do not constitute the cross-family
cross-cell comparison that the matrix's discriminating hypothesis requires.

The author's observational evidence (C-2) is directionally consistent but carries
low confidence weight. The capability floor boundary condition acknowledged in
§4.3.3 — below which alignment training may not establish a functional attractor
regardless of investment — is not tested by the available evidence base and
remains an open theoretical question.

**Cell C verdict: Alignment account is weakly supported by within-family scale
comparisons. The critical cross-cell comparison (Cell C vs. Cell B: does a small
aligned model outperform a large unaligned model?) is not directly testable from
the current evidence base. This is the primary gap in the paper's empirical
engagement.**

#### 5.6.3 Overall Evidence Assessment

The decision procedure in §4.4 specified four possible findings: strong
alignment-dominant, weak alignment-dominant, strong capability-dominant, and null.

On the basis of the assembled evidence:

The available evidence is most consistent with a **weak alignment-dominant finding**:
Cell B provides moderate-confidence support for the alignment account's prediction
that high capability without alignment produces low constraint stability. Cell C
provides weak support for the prediction that alignment investment produces constraint
stability partially independent of capability tier. The Cell C boundary condition —
the capability floor below which alignment investment may not establish a functional
attractor — cannot be evaluated from the current evidence base and remains an open
question.

The evidence does not support a strong capability-dominant finding: the Cell B
documentation consistently shows high-capability models without alignment investment
exhibiting low constraint stability, which is directly inconsistent with the
capability account's core prediction for that cell.

The finding is weak alignment-dominant rather than strong because the Cell C
cross-family cross-cell comparison — the sharpest discriminating test — cannot
be conducted from the available evidence. This is the paper's primary empirical
gap, and it is stated as the primary direction for future empirical work in §6.

---

### 5.7 Evidence Base Non-Claims

**This section does not claim to have empirically validated the 2×2 matrix
predictions.** The cases are illustrative — they demonstrate that the theoretical
framework generates predictions recognizable against documented behavioral patterns.
They do not constitute a controlled test of the hypotheses.

**This section does not claim that the cited literature was designed to test the
matrix framework.** The cited publications have their own research questions and
methodological frames. The translations from source vocabulary to typology coding
are interpretive steps made explicit and marked with confidence levels. The
cited authors are not responsible for the framework this paper applies to their
findings.

**This section does not claim equal evidentiary weight across source categories.**
Category A sources carry higher evidential weight than Category B, which carries
higher weight than Category C. The section's overall evidential position reflects
this hierarchy: the primary claims rest on Category A evidence; Category B and C
sources are supplementary and explicitly labeled.

**This section does not claim that disconfirmatory evidence is absent.** The
capability floor boundary condition in §4.3.3 is an acknowledged theoretical
uncertainty that the evidence base cannot resolve. Future empirical work that
finds Cell C models exhibiting low constraint stability would constitute
evidence for the boundary condition and would require refinement of the alignment
account's predictions for that cell.

---

### 5.8 Forward References from This Section

- **§6 (Implications):** The Cell B evidence — high capability without alignment
  produces near-zero constraint stability — is the empirical anchor for the
  paper's alignment investment argument. §6 draws from this finding in arguing
  that alignment investment is a structural variable in the vulnerability surface
  with practical consequences for deployment decisions.

- **§7 (Limitations and Non-Claims):** The evidence base gaps identified in §5.6 —
  Cell C cross-family comparison absent, archetype-specific protocol not tested
  in Category A literature — are consolidated in §7 as the primary limitations
  of the paper's empirical engagement. The weak alignment-dominant finding is
  stated as the paper's evidential conclusion with appropriate hedging.

- **Exegesis:** Case C-2 (Category C observational note) documents the
  practice-led observation that generated the theoretical framework. The exegesis
  will draw on this case to demonstrate how iterative practice-led observation
  across the series produced a theoretical contribution not anticipated at the
  series' inception. This is the paper's primary contribution to the exegesis
  argument about research methodology.

---

*Section ends. Next: §6 — Alignment Implications. §6 draws on the theoretical
framework (§2–4) and the evidence assessment (§5.6) to develop the paper's
practical and theoretical implications for alignment system design and deployment.*

---

> **Reconciliation note (2026-04-27):**
>
> Citation pass required before assembly. Sources referenced in this section
> that require full bibliographic verification on assembly pass:
>   - Bai et al. (2022) — Constitutional AI paper (Anthropic)
>   - Ouyang et al. (2022) — InstructGPT / RLHF paper (OpenAI)
>   - Stiennon et al. (2020) — Learning to summarize with human feedback (OpenAI)
>   - Perez & Ribeiro (2022) — Prompt injection survey
>   - Zou et al. (2023) — Universal and transferable adversarial attacks on LLMs
>   - Wei et al. (2023) — Jailbroken: How does LLM safety training fail? (Note:
>     verify Wei et al. 2023 author list and venue — multiple "jailbreak" papers
>     appeared in this period; use the one addressing persona-based constraint
>     removal specifically)
>   - Ganguli et al. (2022) — Red teaming language models to reduce harms (Anthropic)
>
> Cross-paper note: Category C (Case C-2) references the author's P3 observational
> work. On series assembly, add a back-reference from P3 §5 Discussion noting that
> the cross-model variance observations incidental to P3 motivated the P4 theoretical
> framework. This creates a documented chain from practice observation → theoretical
> construct that the exegesis can cite.
>
> The "weak alignment-dominant finding" language in §5.6.3 is the paper's
> evidential conclusion. It must be consistent with the framing in §6 (implications)
> and §7 (limitations). Do not upgrade to "strong" in §6 without additional
> evidence; do not downgrade to "null" without acknowledgment that Cell B
> evidence was disregarded.

## --- S6 ---

# Paper 4 — Section 6: Alignment Implications
## "What the Variance Means: Alignment Investment as a
##  Structural Variable in the Identity-Injection Attack Surface"

> **Placement:** `drafts/paper4/P4_S6_Implications.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Role in paper:** The paper's applied contribution layer. §2–5 establish
> the theoretical framework and its evidential grounding; §6 draws out what
> follows from that framework for how alignment systems should be designed,
> how models should be evaluated, and how the field should think about the
> relationship between alignment investment and the identity-injection attack
> surface. This section is not the paper's primary contribution — the
> theoretical framework is — but it is what makes the paper matter beyond
> its immediate audience.
>
> **Register note:** This section shifts from theoretical-analytic to
> applied-argumentative. The claims are derived from the framework and
> evidence; they are not empirical findings in themselves. The hedging
> appropriate to hypothesis-generating scholarship (§2.7, §5.7) remains
> active: implications are stated as what the framework warrants, not as
> established facts. The committee-facing language throughout should be
> "this analysis suggests" and "the framework implies" rather than "this
> demonstrates" or "this proves."
>
> **Scope:** Three implication layers are developed — for alignment system
> design (training-time), for deployment evaluation (inference-time), and
> for the field's conceptual framing of alignment investment as a security
> variable. A fourth layer — implications for the exegesis methodology
> argument — is flagged but deferred to §8 (Conclusion and Exegesis Hook).
>
> **Cross-paper dependencies:**
> - Imports: P2 §6 (instruction-layer / schema-layer distinction) — P4 §6
>   extends this argument, not repeats it. On assembly, check that P4 §6
>   cites P2 §6 explicitly and adds rather than duplicates.
> - Imports: P1 §9.4 (opening created for defensive systems design,
>   alignment research) — P4 §6 partially delivers on that opening.
> - Imports: P4 §2 (attractor depth construct), §3 (typology), §4 (matrix
>   cell predictions), §5 (weak alignment-dominant evidence finding)
> - Exports: Applied argument anchor → P4 §8 (Conclusion)
> - Exports: Alignment investment argument → Exegesis §X
>
> **Publication constraint:** Implications are stated at the framework and
> methodology class level. No named commercial product is identified as
> having a specific vulnerability or as lacking adequate alignment investment.
> Where the implications apply differentially to typology classes, they are
> stated in those terms.

---

## 6. Alignment Implications

### 6.1 The Ground Cleared by the Framework

Before developing the implications, it is worth being precise about what kind of
knowledge the theoretical framework provides, because the implications follow from
that — and only from that.

The framework established in §2–4 and evaluated in §5 provides: a theoretical
account of why constraint variance under archetype-driven persona injection should
be expected to scale with alignment methodology class rather than with raw model
capability; a typology of alignment procedures and their predicted attractor depth
signatures; a matrix of falsifiable predictions that the evidence base evaluates
at moderate confidence; and a conceptual vocabulary — attractor depth, alignment
redundancy, schema suppression, failure mode — for describing the structural
features of the identity-injection attack surface.

What it does not provide is an empirically validated intervention protocol, a set
of engineering specifications for more deeply aligned models, or a prescriptive
ranking of currently deployed systems. The implications that follow stay within
the first category. They are what the theoretical framework, at its current
evidential status (weak alignment-dominant finding, §5.6.3), warrants claiming.
They are stated as research-grounded arguments for consideration, not as proven
engineering recommendations.

---

### 6.2 Implication I: Alignment Investment Is a Security Variable

The framework's most direct implication is conceptual: alignment investment should
be understood as a security variable — not only as an ethical or policy variable —
in the context of identity-injection attacks.

The prevailing framing of alignment training in public and technical discourse
positions it primarily as a means of producing models that are helpful, honest,
and harmless in ordinary use. This framing is accurate but incomplete. The attractor
depth construct (§2.2) establishes a second consequence of alignment investment
that the prevailing framing does not capture: the depth and redundancy of the trained
identity attractor determines the structural resistance of the model to behavioral
schema override. A model with a deep alignment attractor is not merely more likely
to produce constraint-consistent output in normal conditions — it is structurally
more resistant to the class of attacks that operate by activating competing behavioral
schemas to displace the alignment signal.

This reframing has a specific practical consequence: the investment decisions that
produce alignment depth are simultaneously investment decisions in identity-injection
attack resistance. Choices about whether to implement Constitutional AI-class self-
revision loops, how many training passes to dedicate to alignment fine-tuning, and
whether to document and maintain the principle set that training targets are not
purely ethical infrastructure choices — they are security infrastructure choices.
Underfunding them creates a vulnerability surface that scales inversely with the
investment made.

The Cell B finding from §5 makes this concrete: high-capability models with minimal
alignment investment exhibit near-zero constraint stability under persona injection
pressure. The capability investment is large; the security property relevant to
identity-layer attacks is absent. The gap between the two is the alignment attractor —
and the gap is not filled by scale alone.

*Scope of this implication.* This implication applies specifically to the
identity-injection attack surface characterized in this paper and in Papers 1–2.
Other attack surfaces — gradient-based adversarial attacks, data poisoning, system
prompt injection — have their own vulnerability profiles and their own mitigation
requirements. The claim is not that alignment investment is a comprehensive security
solution; it is that, for the specific attack class examined here, alignment
investment is the dominant structural variable.

---

### 6.3 Implication II: The Instruction Layer Is Not the Only Defense Layer

Paper 2 (§6) establishes that persona injection operates below the instruction layer —
that it activates behavioral dispositions through schema activation rather than through
direct instruction override. The implication drawn there is that instruction-layer
defenses (refusal rules, content filters, output classifiers applied post-generation)
are insufficient to address the identity-injection attack surface because they operate
on outputs, not on the schema activation process that produces them.

The framework developed in this paper extends that implication. Not only are
instruction-layer defenses insufficient at inference time — the insufficient defense
problem begins at training time, and its structural character is precisely what the
attractor depth construct describes. A model trained exclusively with RLHF reward
signals has an alignment signal that operates at the output layer. Its defense against
schema activation is therefore also at the output layer: the reward signal competes
against the schema signal in the output generation process, and once that competition
is overcome, there is no secondary constraint representation to provide continued
resistance. The instruction-layer defense problem at inference time is a consequence
of the training-layer architecture decision, not an independent failure mode.

Constitutional AI-class training addresses this not by adding more instruction-layer
defense (more content filters, stronger refusal rules) but by encoding the alignment
signal at multiple representational levels during training. The self-critique and
revision loop creates constraint representations that are not located solely at the
output layer — they are encoded in the model's self-evaluation process, which operates
earlier in the generation pipeline. This multi-layer encoding is what produces the
redundancy property (§2.3) and the contested-partial-breach failure mode under
pressure: the schema activation must overcome constraint representations at multiple
levels simultaneously, rather than overwhelming a single output-layer signal.

The training-design implication: alignment procedures that aspire to robust identity-
injection resistance should explicitly target multi-layer constraint encoding, not only
output-layer reward optimization. The specific mechanism by which CAI-class training
achieves this — the self-critique and revision loop applied iteratively during training —
is one implementation; the theoretical requirement is the multi-layer redundancy, not
the specific procedure. Future alignment methodologies that produce equivalent redundancy
through different architectural means would be expected to produce equivalent attractor
depth by the framework's predictions.

---

### 6.4 Implication III: The Capability–Alignment Trade-off Has a Security Dimension

A substantial body of alignment research and public discourse concerns what is sometimes
called the capability–safety trade-off: the hypothesis that more capable models may be
harder to align, or that alignment procedures may reduce capability. The evidence on
this hypothesis is contested; the Constitutional AI literature presents evidence that
alignment training need not significantly reduce helpfulness, while other literature
documents capability costs from some alignment procedures.

The attractor depth framework contributes a distinct observation to this debate, not as
a position on the capability–safety trade-off in general, but as a specific claim about
the identity-injection attack surface: if alignment investment is the dominant predictor
of constraint stability under persona injection (as the weak alignment-dominant finding
in §5 suggests), then the capability–alignment pairing is not merely a design trade-off
to be optimized — it is a security configuration to be evaluated.

The 2×2 matrix (§4) makes the security-configuration framing concrete. Cell A (high
capability, high alignment) represents the configuration with the strongest predicted
security properties for the identity-injection surface. Cell B (high capability, low
alignment) represents a configuration whose capability investment is not matched by
alignment investment, producing a security-relevant gap. Cell C (low capability, high
alignment) represents a configuration whose alignment investment produces meaningful
security properties despite reduced capability. Cell D (low capability, low alignment)
is the baseline vulnerability configuration.

The security-configuration argument is not that all models must be Cell A — the
deployment context determines which security properties are required. A low-risk
deployment context where persona injection is an unlikely attack vector may accept
Cell D configuration without concern. A high-risk deployment context — customer-facing
systems, systems where output is acted upon without human review, systems deployed in
security-sensitive environments — warrants Cell A configuration. The framework provides
the vocabulary for making that deployment decision in security terms, not only in
capability or cost terms.

---

### 6.5 Implication IV: Attractor Depth Is Potentially Measurable Pre-Deployment

The AD proxy construct (§2.2.3) is defined entirely in terms of behavioral outputs
observable at inference time, without requiring access to model weights, training data,
or architectural details. This is a deliberate methodological choice with a significant
practical implication: attractor depth is in principle assessable as a pre-deployment
evaluation metric.

Current model evaluation practices for alignment-relevant behavior tend to focus on
benchmark performance against curated harmful-output test sets — what the model
produces in response to known problematic prompts. These benchmarks assess constraint-
consistent output in normal conditions but do not assess the structural depth of the
constraint under sustained attack conditions. A model may pass a harmful-output
benchmark by producing constraint-consistent outputs in response to known attack
patterns while having a shallow identity attractor that is readily displaced by novel
or archetype-mediated attack vectors not represented in the benchmark set.

The AD proxy supplements this by probing the structural depth of the constraint under
progressive perturbation — specifically, the perturbation threshold P(M, A) and the
recovery rate R(M, A). A model that maintains constraint-consistent output across
many perturbation steps (high P) and recovers toward baseline following perturbation
removal (high R) has demonstrated structural constraint depth that a single-point
harmful-output benchmark cannot capture.

*The practical evaluation protocol implied by this.* For any archetype A in the
standard evaluation set, an AD assessment involves: (1) establishing the baseline CEE
centroid for the model under archetype A; (2) applying incremental persona reinforcement
steps (equivalent to the P3 perturbation sequence) and recording the perturbation step
at which the first CEE breach occurs; (3) applying a null prompt following breach and
recording the degree of recovery toward baseline. The resulting P(M, A) and R(M, A)
values constitute a structural constraint assessment that goes beyond single-point
benchmark evaluation.

This is not a product recommendation for a specific evaluation procedure. It is a
theoretical argument that the AD proxy construct makes an under-measured property of
model alignment — structural constraint depth under attack conditions — in principle
measurable using the behavioral measurement apparatus already developed across this
series. The precise operationalization and standardization of such an evaluation protocol
would require further empirical development beyond this paper's scope.

---

### 6.6 Implication V: Typology Placement Predicts Deployment Risk Profile

The four-class typology (§3) provides a vocabulary for characterizing models' alignment
methodology class and, by extension, their predicted failure mode under identity-injection
attack conditions. The failure mode predictions — contested-partial-breach for CAI-class,
collapse for RLHF-dominant, shallow-threshold for instruction-tuning-only, immediate-
schema-dominance for open-weight unaligned — are not merely theoretical classifications.
They describe qualitatively different deployment risk profiles.

**Deployment risk profile — CAI-class (contested-partial-breach).** Models predicted
to exhibit the contested-partial-breach failure mode produce heterogeneous output under
high perturbation pressure: partial schema-consistent content alongside partial constraint-
consistent content. The deployment risk profile is: detectable degradation (the heterogeneous
output is a detectable signal that attack conditions are active) but incomplete breach
(full constraint removal requires sustained, high-intensity pressure). The CEE
variance-alerting detection heuristic from P2 §6 is most applicable to this class: the
behavioral signature of contested-partial-breach is a characteristic pattern in the
model's drift vector that a real-time monitoring system could detect.

**Deployment risk profile — RLHF-dominant (collapse).** Models predicted to exhibit
the collapse failure mode produce constraint-consistent output up to a threshold and
then transition relatively sharply into schema-dominant behavior. The deployment risk
profile is: less detectable degradation trajectory (the collapse is rapid, not gradual,
reducing the window for detection) and complete breach above the threshold. The mitigation
implication is that RLHF-dominant models deployed in high-risk contexts should be
paired with output-layer detection systems that are sensitive to the sudden threshold-
crossing pattern characteristic of collapse.

**Deployment risk profile — instruction-tuning-only (shallow-threshold).** Models
predicted to exhibit the shallow-threshold failure mode produce schema-dominant behavior
under low perturbation pressure. The deployment risk profile is: high vulnerability to
even casual persona injection — the attack does not require sustained escalation. The
mitigation implication is that IT-only models should not be deployed in contexts where
persona injection is a realistic attack vector without additional system-level safeguards
(system prompt constraints, output monitoring, human review of outputs).

**Deployment risk profile — open-weight unaligned (immediate-schema-dominance).** Models
without a trained identity attractor produce schema-dominant behavior essentially
immediately under archetypal persona injection. The deployment risk profile is: complete
vulnerability to identity-layer attacks with near-zero structural resistance. The
deployment implication is not primarily about detection but about use-case scoping:
these models are appropriate in deployment contexts where the persona injection attack
vector is not a realistic risk, and should not be deployed in contexts where it is,
regardless of their capability level.

The typology-based risk profiling is a first-order tool, not a comprehensive security
assessment. It characterizes one attack surface — identity-injection — and does not
address other vulnerability classes. A model's typology placement does not determine
its overall security posture; it characterizes one dimension of that posture, which
must be assessed in conjunction with the deployment context and risk model.

---

### 6.7 Implication VI: The Schema Layer Requires Its Own Research Agenda

The series' central technical finding — that persona injection operates at the behavioral
schema layer, below and to some extent independent of the instruction layer — implies
a research gap that the series can name but not fill.

Current alignment research is predominantly oriented toward the instruction layer:
measuring whether models follow instructions consistently, refuse appropriately under
known attack patterns, maintain honesty under elicitation pressure. This research agenda
is important and has produced substantial progress. But it does not directly address
the schema layer vulnerability surface documented in this series. The instruction layer
and the schema layer are distinct attack surfaces with distinct structural properties and
distinct mitigation requirements.

A schema-layer research agenda would include at minimum:

*Schema inventory and risk stratification.* A systematic characterization of the
behavioral schemas most likely to be activated by persona injection across the culturally
available archetype space — extending the archetype set developed in this series to cover
a wider range of character types, roles, and cultural frames. The CEE methodology provides
a measurement instrument for this; the theoretical framework provides the selection
criteria (canonical overdetermination, schema conflict with alignment attractor, deployment
relevance).

*Multi-layer alignment training development.* Investigation of training procedures that
explicitly target the schema layer — not just output-layer reward optimization or
instruction-following demonstrations, but training mechanisms that establish constraint
representations at the same level at which behavioral schemas are encoded. CAI-class
training approaches this goal through its self-critique mechanism; whether the mechanism
is optimally designed for schema-layer constraint redundancy, and whether alternative
approaches could achieve equivalent or superior redundancy more efficiently, are open
research questions.

*Deployment-layer schema monitoring.* Development of real-time monitoring systems that
can detect CEE breach and schema-dominant behavior in production outputs — implementing
the CEE variance-alerting heuristic (P2 §6) in production-ready form. The AD proxy
measurement (§6.5) provides a theoretical basis for such a system; the engineering
challenge is operationalizing it at production inference scale.

*Temporal dynamics of attractor depth.* The session stationarity limitation (P1 §7.1)
acknowledges that attractor depth as characterized here is a within-session construct.
How attractor depth interacts with persistent memory systems, multi-session conversation
contexts, and fine-tuning applied post-deployment is an open question with direct
relevance to the deployment risk profiles described in §6.6.

These are research directions implied by the framework, not delivered by it. Naming
them explicitly is part of the paper's contribution: mapping the territory of what
remains to be investigated is itself a contribution to the field, particularly in a
domain where the vulnerability surface has only recently begun to receive systematic
theoretical attention.

---

### 6.8 Scope of the Implications

Each implication in §6.2–6.7 is derived from the theoretical framework with specific
dependence on the evidence base's weak alignment-dominant finding (§5.6.3). They are
warranted as claims proportional to that finding. Two scope conditions apply globally
to this section:

**Scope condition 1 — Hypothesis-generating status.** The paper's evidential status
is hypothesis-generating, not hypothesis-confirming. The implications are therefore
stated as what the framework suggests warrants investigation and consideration, not as
what has been demonstrated. Future empirical work that provides stronger evidence for
the alignment account — particularly the Cell C cross-family comparison identified as
the primary evidence gap — would justify strengthening these implications. Evidence
against the alignment account would require their revision.

**Scope condition 2 — Single attack surface.** Every implication in this section
concerns the identity-injection attack surface specifically. The broader claim that
alignment investment is a security variable in general — across all attack surfaces —
is not made. Alignment investment may or may not be the dominant variable for gradient-
based attacks, data poisoning, system prompt injection, or other attack classes. This
paper makes no claim about those surfaces.

---

### 6.9 Forward References from This Section

- **§7 (Limitations and Non-Claims):** The scope conditions in §6.8 are consolidated
  in §7 with the other limitations of the paper. The hypothesis-generating status
  constraint on the implications is reiterated there as a non-claim.

- **§8 (Conclusion and Exegesis Hook):** The research agenda in §6.7 is the forward-
  looking element that §8 draws on to position the paper as a contribution to the
  field, not only as a self-contained theoretical argument.

- **Exegesis:** The reconceptualization of alignment investment as a security variable
  (§6.2) is the paper's most practically significant claim and the one with the widest
  implications beyond the series. The exegesis should draw on this as an example of
  how practice-led theoretical work can generate conceptual reframings with practical
  consequence — the security-variable framing of alignment investment is not something
  that emerges from controlled experiment; it emerges from the structural analysis of
  a vulnerability surface mapped through iterative theoretical and observational work
  across the series.

---

*Section ends. Next: §7 — Limitations and Non-Claims Registry. §7 consolidates all
scope conditions and non-claims from §2–6 into the committee-shield registry, following
the structure established in P1 §8. This is the penultimate section before §8 (Conclusion
and Exegesis Hook).*

---

> **Reconciliation note (2026-04-27):**
>
> §6.3 (Instruction Layer Is Not the Only Defense Layer) directly extends P2 §6.
> On assembly, check that P4 §6.3 cites P2 §6 explicitly and that the framing is
> additive rather than repetitive. P2 §6 establishes that instruction-layer defenses
> are insufficient at inference time; P4 §6.3 extends this by showing the insufficiency
> has a training-time origin in the architecture of the alignment signal. These are
> compatible claims at different levels of analysis; the citation should make the
> relationship explicit.
>
> §6.5 (Attractor Depth Is Potentially Measurable Pre-Deployment) introduces the
> practical evaluation protocol argument. This should be cross-referenced with P3's
> measurement apparatus on assembly: the perturbation sequence in P3 §3 is the
> experimental instantiation of the evaluation protocol described here. The implication
> is that P3's methodology could be extended from experimental use to pre-deployment
> evaluation use. Flag for P3 §5 Discussion section — add a sentence noting that the
> measurement methodology has potential pre-deployment evaluation applications beyond
> the experimental context.
>
> §6.7 research agenda items (schema inventory, multi-layer training development,
> deployment monitoring, temporal dynamics) should be checked against P1 §9.4 (opening
> the series creates) on assembly. P1 §9.4 names defensive systems design, archetype
> set extension, and alignment research as the three lines of inquiry the series opens.
> P4 §6.7 should be cited as delivering on the third of those — providing the specific
> theoretical specification of what the schema-layer research agenda looks like — and
> extending the first (defensive systems design) with the deployment risk profiles
> in §6.6.
>
> §6.6 (deployment risk profiles by typology class) introduces the CEE variance-
> alerting detection heuristic from P2 §6 in a new deployment context. On assembly,
> verify that P4 §6.6 cites P2 §6 for the original heuristic specification, and that
> the extension here (applying it differentially by typology class) is clearly framed
> as P4's contribution rather than a re-statement of P2's.

## --- S7 ---

# Paper 4 — Section 7: Limitations and Non-Claims Registry
## "Scope Conditions, Acknowledged Uncertainties, and
##  What This Paper Does Not Claim"

> **Placement:** `drafts/paper4/P4_S7_Limitations_NonClaims.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Role in paper:** Committee shield and IRB-facing scope statement.
> This section consolidates all explicit non-claims and scope conditions
> distributed throughout §2–6 into a single registry, following the
> structure established in P1 §8. Items distributed across sections are
> NOT removed from those sections — local non-claims serve local reader
> orientation. This registry is the authoritative consolidation point.
> On assembly, if any item here conflicts with a local statement in §2–6,
> the registry takes precedence; note the discrepancy and reconcile.
>
> **Architecture note:** The registry is organised into five clusters —
> methodological limitations, construct limitations, evidence base
> limitations, implication limitations, and series-boundary limitations.
> This clustering differs from P1 §8's topic-based structure because P4's
> non-claims distribute differently across the argument. The clustering
> is designed to help committee members find the limitation type most
> relevant to their review concerns, not to minimise the apparent scope
> of the paper's limitations.
>
> **The IRB exposure note from the seed prompt is active here.** P4 is
> the most exposed paper in the series for IRB/ethics review. The "no
> active probing" constraint must be visible in this section, stated as
> a methodological choice rather than merely a constraint. The framing
> is: the absence of active probing is what makes this scholarship rather
> than red-teaming, and the theoretical and evidential contributions are
> what are possible within that methodological boundary — not what is
> possible despite it.
>
> **Cross-paper dependencies:**
> - Consolidates: §2.6 (falsifiability conditions), §2.7 (non-claims),
>   §3.7 (typology as instrument), §3.8 (scope conditions), §4.6
>   (matrix cannot determine), §4.5 (archetype third variable), §5.7
>   (evidence base non-claims), §6.8 (implication scope conditions)
> - The P1 §8 Non-Claims Registry is the series template.
>   P4 §7 follows that template while adding P4-specific items.
> - Items propagating to P4 §8 (Conclusion): the hypothesis-generating
>   status item (§7.1.1) and the primary evidence gap (§7.3.3) are the
>   two limitations the conclusion must explicitly acknowledge.

---

## 7. Limitations and Non-Claims Registry

### Preface

Scholarly claims earn credibility not only by what they assert but by what they
explicitly decline to assert. The theoretical framework developed in §2–4, the
evidence base engaged in §5, and the implications drawn in §6 all carry scope
conditions and acknowledged uncertainties that define the boundary between what
this paper argues and what it does not. These boundaries are not apologies for
the paper's contribution; they are the conditions under which that contribution
is coherent and defensible.

This registry is the authoritative statement of those boundaries. Each item is
stated in the form "This paper does not claim..." or "This paper's [construct/
finding/implication] is limited by..." and is followed by the precise scope of
the limitation and, where relevant, the condition under which the limitation would
be resolved. Items are cross-referenced to the section of the paper where the
limitation is first acknowledged.

---

### 7.1 Methodological Limitations

#### 7.1.1 Hypothesis-Generating, Not Hypothesis-Confirming Status

**This paper does not claim to have confirmed the central hypothesis that alignment
methodology is the dominant predictor of cross-model constraint variance under
archetype-driven persona injection.**

The methodological frame is explicitly hypothesis-generating. The theoretical
framework generates the hypothesis; the 2×2 matrix operationalizes it as a set
of falsifiable cell-level predictions; the evidence base in §5 evaluates those
predictions at moderate confidence and arrives at a weak alignment-dominant finding.
A weak alignment-dominant finding is not confirmation — it is directional support
for a hypothesis that warrants further investigation by methods with greater
evidential power.

The condition under which this limitation would be resolved is systematic empirical
investigation using the AD proxy measurement apparatus (§2.2.3) with controlled
archetype conditions across documented methodology classes — the kind of study that
this paper's framework is designed to enable but that falls outside this paper's
methodological scope. (§2.1, §4.4, §5.1, §6.8)

#### 7.1.2 No Active Probing

**This paper does not conduct active adversarial probing of any model. No behavioral
instances were generated by the author for the purpose of testing the theoretical
predictions in this paper.**

This is a methodological choice, not merely a constraint. Active probing —
deliberately constructing and executing perturbation sequences against deployed
models to test the attractor depth predictions — would constitute adversarial
red-teaming, not observational scholarship. The distinction between documenting
and theorizing a vulnerability surface (scholarship) and operationalizing it as
an attack protocol (red-teaming) is the load-bearing ethical distinction that
governs this paper and the series as a whole. The no-active-probing constraint is
what maintains that distinction.

The consequence for the evidence base is that §5 relies on published literature,
documented public discourse, and the author's incidental series observations rather
than controlled measurements. This reduces the evidential power of the paper's
cross-model predictions and is acknowledged in the evidence assessment (§5.6).
The theoretical contribution — the framework, typology, and matrix — does not
depend on active probing and is not weakened by its absence. (§1, §5.1, §5.7)

#### 7.1.3 No Provider-Specific Targeting

**This paper does not attribute specific vulnerability profiles or alignment
deficiencies to named commercial products.**

All claims about constraint variance are stated at the level of alignment methodology
class, not at the level of named commercial deployment. The typology classes
(Constitutional AI-class, RLHF-dominant, instruction-tuning-only, open-weight
unaligned) describe training procedure architectures, not products. Where the
evidence base draws on published literature that names specific models or providers,
the attribution in this paper is to the training procedure class documented in that
literature, not to the named product.

This is not a methodological limitation that reduces the paper's contribution —
it is a principled choice grounded in the paper's theoretical argument (§3.7):
training procedures are stable analytic categories; named products change. Claims
indexed to procedure classes are more durable and more scientifically precise
than claims indexed to product names. (§3.7, §5.1.2)

#### 7.1.4 Evidence Base Source Heterogeneity

**This paper's evidence base draws from three source categories with materially
different methodological standards, and these categories are not weighted equally.**

Category A sources (published red-team and safety literature) carry highest
evidential weight; they use controlled methodology with stated protocols. Category B
sources (documented public discourse) carry moderate evidential weight; they include
practitioner documentation and community benchmarks that lack controlled methodology.
Category C sources (author's prior series observational work) carry lowest evidential
weight; they reflect informal observation without experimental control.

The paper's evidential conclusions in §5.6 are calibrated to this hierarchy. The
weak alignment-dominant finding rests primarily on Category A evidence for Cell B,
with partial Category A and Category C support for Cell C. Any stronger conclusion
would require Category A evidence for both critical discriminating cells. (§5.1.1,
§5.1.3, §5.6)

---

### 7.2 Construct Limitations

#### 7.2.1 Attractor Depth Is a Behavioral Proxy, Not a Mechanistic Measure

**This paper does not claim that the Attractor Depth (AD) proxy directly measures
any property of model architecture, training data distribution, or internal weight
configuration.**

AD(M, A) = α·P(M, A) + β·R(M, A) is a composite behavioral proxy observable at the
output layer. The theoretical interpretation — that higher AD scores reflect deeper
identity attractor encoding in the model's trained weight configuration — is a
theoretical account consistent with the construct, not a direct empirical claim.
Alternative interpretations of the behavioral proxy (surface mimicry stability,
instruction sensitivity, context window effects) are not ruled out by the proxy
formulation alone.

The falsifiability conditions in §2.6 are designed to provide partial discrimination
between the attractor account and alternatives: if alignment methodology class
predicts AD variance more strongly than capability markers, the attractor account
is supported. But the proxy does not and cannot, by its design, directly observe
the mechanism. (§2.2.3, §2.5, §2.6)

#### 7.2.2 Attractor Depth Is Archetype-Indexed, Not Absolute

**This paper does not claim that a model's attractor depth is a global scalar
property of the model. AD(M, A) is always indexed to a specific archetype A.**

A model that exhibits high AD under a constraint-compatible archetype (e.g., a
lawful-neutral character whose behavioral contract is consistent with the alignment
attractor) may exhibit substantially lower AD under a high-conflict archetype (e.g.,
a chaotic character whose behavioral contract is in direct opposition to the alignment
attractor). This is predicted by the schema suppression account (§2.5): the attractor
must overcome a schema signal of specific magnitude, and that magnitude varies with
the archetype's canonical conflict weight.

The practical consequence is that AD assessments must be archetype-specific; a
single-archetype AD measurement does not characterize the model's general constraint
stability under persona injection. The evaluation protocol implied in §6.5 requires
assessment across multiple archetypes spanning the conflict weight range. (§2.2.3,
§2.7, §4.5)

#### 7.2.3 The Schema Suppression Account Is Interpretive, Not Established

**This paper does not claim that the schema suppression account (§2.5) — the
theoretical account of how alignment attractor depth resists behavioral schema
activation — is mechanistically established.**

The schema suppression account is a theoretical interpretation of the behavioral
proxy formulation that is consistent with the Constitutional AI literature and with
the predicted failure mode patterns. It is the account that best fits the theoretical
framework as a whole. However, it is not derived from direct observation of model
internals, and it is not the only possible account of why deeper alignment training
produces higher perturbation thresholds. Alternative accounts at the systems level
(increased instruction-following robustness, more conservative output generation
policies) could produce similar behavioral profiles without the specific mechanism
the schema suppression account posits.

The account is adopted as a theoretical prior that generates testable predictions,
not as an established mechanistic claim. (§2.5, §2.7)

#### 7.2.4 The Four-Class Typology Is Analytic, Not Exhaustive

**This paper does not claim the four-class alignment methodology typology (§3) is
a complete description of the alignment methodology landscape or that all models
fit cleanly into one class.**

The typology is an analytic instrument for specifying the paper's independent
variable with sufficient precision to generate falsifiable predictions. It covers
the dominant alignment procedures documented in the literature as of mid-2025. New
alignment approaches — process reward models, debate-based training, interpretability-
informed alignment, constitutional approaches based on novel principle-specification
methods — may produce training procedures that fall outside or straddle the four-
class boundary structure.

The boundary ambiguities most likely to arise in practice — sequential pipelines,
partial CAI implementation, post-training alignment modification — are addressed in
§3.6. Cases not addressed there should be assigned conservatively and marked with
reduced confidence in the observational case schema. (§3.6, §3.8)

#### 7.2.5 The 2×2 Matrix Dichotomizes Continuous Variables

**This paper does not claim that capability and alignment investment are genuinely
binary variables. The 2×2 matrix dichotomizes both dimensions for analytic clarity.**

In practice, both capability and alignment investment are continuous and
multidimensional. Capability ranges continuously across scales; alignment investment
varies in degree, method composition, and training duration. The HIGH/LOW
dichotomization used in the matrix is a theoretical simplification that enables the
predictive structure but loses within-tier variance. The critical discriminating
cells (B and C) make predictions that depend on this dichotomization; models near
the tier boundary may not exhibit the predicted patterns as clearly as models well
within each tier.

The non-linearity caution is particularly relevant at the LOW capability tier:
there may exist a capability floor below which alignment investment cannot establish
a functional identity attractor regardless of its depth and redundancy (the Cell C
boundary condition, §4.3.3). This floor is not directly estimable from the current
evidence base and represents an acknowledged open question. (§4.2, §4.3.3, §4.6,
§5.6.2)

---

### 7.3 Evidence Base Limitations

#### 7.3.1 Cell C Cross-Family Comparison Is Absent

**This paper does not provide direct evidence for the Cell C prediction — that a
low-capability model with high alignment investment exhibits moderate-to-high
constraint stability and outperforms a high-capability model with low alignment
investment (Cell B) on AD metrics.**

Cell C is the second critical discriminating cell of the 2×2 matrix (§4.3.3). The
Cell C prediction is the sharpest available test of the alignment account over the
capability account: if a small, well-aligned model demonstrably outperforms a large,
minimally aligned model on persona injection resistance, the alignment account is
strongly supported. However, this cross-family cross-cell comparison requires
controlled measurement across model families at different capability and alignment
tiers, which is outside the methodological scope of this paper.

The available Category A evidence for Cell C (§5.4, Case C-1) consists of within-
family scale comparisons that show alignment training retains partial effectiveness
at reduced capability — necessary but not sufficient for the full Cell C prediction.
The cell remains the primary evidence gap in the paper's empirical engagement. (§4.3.3,
§5.4, §5.6.2)

#### 7.3.2 Archetype-Specific Protocol Not Tested in Category A Literature

**The Category A evidence base used in §5 was not designed to test the specific
archetype-driven persona injection protocol developed in Papers 1–3 of this series.**

The published red-team and safety literature engages with adversarial constraint
removal broadly — covering jailbreak techniques, adversarial suffixes, and roleplay-
based constraint erosion — but does not use the CEE measurement methodology, the
canonical archetype behavioral contract vocabulary, or the perturbation step protocol
that Papers 1–3 develop. The translation from source literature to typology coding
in §5 involves inferential steps that introduce uncertainty.

The most directly relevant test of the framework would use the P3 perturbation
sequence methodology applied systematically across model instances representing each
typology class. This test is implied by §6.5 as a future evaluation protocol but is
not conducted within this paper. (§5.1.2, §5.6.1)

#### 7.3.3 Category C Evidence Carries Confirmation Bias Risk

**The author's prior series observational work (Category C, §5.4, Case C-2) was
conducted before the theoretical framework in this paper was formalized, but it
motivated that framework — creating a structural confirmation bias risk.**

The practice-led observation that constraint recovery behavior varied across model
classes in ways that didn't track capability markers alone is documented in §5 as
the origin of the attractor depth theoretical construct (see also the exegesis
reflexivity note at §2.8). Including this observation as evidence in the same paper
that it motivated risks circularity: the theory was built to explain the observation,
and the observation is then used as support for the theory.

This paper manages the risk by assigning Category C evidence the lowest confidence
weight and framing its evidential role as reflexive documentation rather than
confirmatory support (§5.4, Case C-2). The primary claims do not rest on Category C
evidence; they rest on Category A evidence for Cell B. Category C evidence
contributes to the exegesis argument about practice-led theory generation, not to
the theoretical claim about alignment methodology and constraint variance. (§5.1.3,
§5.4, §5.7)

#### 7.3.4 Temporal Scope of the Evidence Base

**Behavioral observations attributed to typology classes in §5 reflect model behavior
at the time of the documented observation. The paper makes no claim about the
current constraint behavior of any specific model or deployment.**

The model landscape changes rapidly: models are updated, alignment procedures are
revised, new training passes are applied to deployed systems. A behavioral observation
documented in 2022–2024 red-team literature may not reflect the current behavior of
any specific model, even if it accurately characterized behavior at the time. The
typology-class attribution is stable — the training procedure class of a specific
model version is determined by the training procedure used for that version — but
the behavioral implication of that class attribution may have changed with subsequent
updates. (§3.7, §3.8)

---

### 7.4 Implication Limitations

#### 7.4.1 Implications Are Proportional to the Weak Alignment-Dominant Finding

**The implications in §6 are derived from a theoretical framework with moderate-
confidence evidential support at the time of writing. They do not carry the weight
of empirically confirmed findings.**

The weak alignment-dominant finding (§5.6.3) is the evidential anchor for the §6
implications. Stronger empirical evidence — particularly a direct Cell C / Cell B
cross-family comparison — would justify strengthening the implications. Evidence
against the alignment account in either critical discriminating cell would require
their revision or retraction. The implications are stated as warranted by the current
evidential status; they should be read as strong theoretical arguments grounded in
moderate-confidence empirical support, not as established facts. (§5.6.3, §6.1,
§6.8)

#### 7.4.2 Implications Are Scoped to the Identity-Injection Attack Surface Only

**No implication in §6 is stated as a general claim about alignment investment and
model security across all attack surfaces.**

The identity-injection attack surface — persona injection targeting the behavioral
schema layer below the instruction layer — is one of several LLM attack surfaces.
The claim that alignment investment is the dominant predictor of constraint variance
is specific to this surface. Other attack surfaces (gradient-based adversarial
attacks, data poisoning, system prompt injection, membership inference attacks)
have their own vulnerability profiles and mitigation requirements. The paper
provides no evidence about whether alignment investment is the dominant variable
for those surfaces. (§6.2, §6.8)

#### 7.4.3 The Pre-Deployment Evaluation Protocol Is Theoretical, Not Operationalized

**The pre-deployment AD assessment protocol described in §6.5 is a theoretical
argument for a measurement approach implied by the framework, not a validated
evaluation instrument.**

The argument that P(M, A) and R(M, A) could constitute a structural constraint
assessment metric supplementing harmful-output benchmarks is grounded in the AD
proxy construct and is theoretically coherent. However, the protocol has not been
operationalized, standardized, or validated as an evaluation instrument. The
psychometric properties of such an instrument — test-retest reliability, inter-
rater reliability in the behavioral coding step, sensitivity and specificity for
detecting alignment depth differences — are unknown. The claim is that the
theoretical basis for such an instrument exists; the instrument itself is a
direction for future work, not a current contribution. (§2.2.3, §6.5)

#### 7.4.4 Deployment Risk Profiles Are First-Order Characterizations

**The deployment risk profiles in §6.6 are derived from the failure mode predictions
of the typology, which are theoretical predictions rather than empirically validated
profiles.**

The risk characterizations — contested-partial-breach for CAI-class, collapse for
RLHF-dominant, shallow-threshold for instruction-tuning-only, immediate-schema-
dominance for open-weight unaligned — follow directly from the typology and the
redundancy hypothesis. They are the most theoretically grounded characterizations
available from the framework. However, they are not empirically validated risk
profiles in the engineering sense: they have not been derived from controlled
measurement of actual failure rates, breach magnitudes, or recovery statistics
across a representative sample of models from each class. They are theoretical
predictions about failure mode structure, not measured risk parameters. (§3.2.3–
3.5.3, §6.6)

---

### 7.5 Series-Boundary Limitations

#### 7.5.1 Session Stationarity Inherits From the Series

**This paper inherits the session stationarity limitation established in P1 §7.1:
the CEE and AD constructs are within-session measurements. The implications of
attractor depth for multi-session persistence, fine-tuning dynamics, and persistent
memory architectures are outside the scope of the series.**

The session stationarity limitation is most significant for the deployment
implications in §6.6: the risk profiles described there apply to single-session
interaction contexts. Deployment architectures that include persistent memory,
multi-turn session context accumulation, or in-context fine-tuning create conditions
under which within-session attractor depth measurements may not predict cross-session
behavior. The temporal dynamics research direction named in §6.7 is the appropriate
future work response to this limitation. (P1 §7.1, §4.5, §6.7)

#### 7.5.2 Training Data Opacity Inherits From the Series

**This paper inherits the training data opacity limitation established in P1 §7.2:
the behavioral contract mechanism relies on training-data density claims that cannot
be directly verified.**

The schema suppression account (§2.5) posits that alignment signal weight advantage
is established through training. The training data composition that shapes both the
alignment signal and the schema signal is not publicly documented with sufficient
granularity to directly verify the density claims on which the schema activation
mechanism depends. The AD proxy is a behavioral measure that does not require direct
verification of training data; but the theoretical interpretation of high AD as
reflecting a trained alignment weight advantage is dependent on the training-data
density account being approximately correct. (P1 §7.2, §2.5)

#### 7.5.3 Acting vs. Being Inherits From the Series

**This paper inherits the acting vs. being limitation established in P1 §7.3: the
behavioral proxy formulation cannot distinguish between genuine schema activation
(behavioral state shift) and sophisticated surface mimicry (output pattern matching
without underlying state change).**

AD(M, A) measures output behavior — perturbation threshold and recovery rate — not
internal states. A model that exhibits high AD could theoretically be maintaining
constraint-consistent output through sophisticated instruction-following without any
identity attractor in the sense the framework posits. The perturbation threshold
would be high because the model's instruction-following is robust; the recovery rate
would be high because instruction-following returns to baseline when perturbation
pressure is removed. This alternative account is not ruled out by the proxy
formulation alone.

The partial discriminator from P1 §7.3 and P3 (H3 — archetype × perturbation
interaction effect predicts archetype-specific perturbation sensitivity that surface
mimicry alone cannot account for) applies to this limitation. If H3 holds in P3
data, the pure surface mimicry account is weakened. But it is not eliminated. (P1
§7.3, §2.2.3)

#### 7.5.4 The Cross-Paper Comparison Introduces New Confounds

**The cross-model comparison that is P4's central contribution introduces confounds
not present in Papers 1–3's within-model analysis.**

Within-model analysis (P1–P3) controls for model as a variable by holding it
constant. Cross-model comparison necessarily varies the model, introducing
confounds that cannot be fully controlled without active probing: differences in
system prompt sensitivity, inference-time parameter settings, context window
handling, tokenization, and training data composition that are independent of
alignment methodology and capability tier. The typology classification and matrix
cell attribution in §5 attempt to control for confounds by attributing cases to
methodology classes rather than individual models, but methodology-class-level
controls cannot eliminate all within-class variance from these confounding factors.

This is a new limitation specific to P4 that is not inherited from the series
framework. It is the primary reason the cell predictions are stated as ranges
rather than point estimates and the evidence assessment is calibrated to MODERATE
confidence rather than HIGH. (§4.2, §5.1.3, §5.6)

---

### 7.6 What the Limitations Do Not Undermine

The limitations above are genuine and acknowledge real gaps. However, they should
not be read as undermining the paper's contributions. Four contributions survive
all the limitations stated in §7.1–7.5:

**Contribution 1 — The theoretical construct.** The attractor depth construct and
its formal proxy operationalization (§2.2.3) provide a theoretically grounded,
behaviorally measurable framework for characterizing cross-model constraint variance
that does not currently exist in the literature. This contribution does not depend
on having confirmed the central hypothesis — it depends on having specified the
construct precisely enough to generate falsifiable predictions and enable future
measurement. That precision is present regardless of the evidential status of the
current paper.

**Contribution 2 — The alignment methodology typology.** The four-class typology
(§3) provides a mechanism-grounded vocabulary for discussing alignment methodology
differences at a level of precision that neither the general "aligned/unaligned"
binary nor product-level discussion achieves. This vocabulary is useful for
formulating research questions, structuring comparative analyses, and communicating
about alignment investment in security terms — independently of whether the typology's
behavioral predictions are confirmed.

**Contribution 3 — The predictive matrix.** The 2×2 capability × alignment matrix
(§4) provides a falsifiable predictive structure that specifies, in advance, what
the world should look like if alignment methodology is the dominant variable, and
what it should look like if capability is dominant. This structure exists whether
or not the current evidence base confirms it. Future empirical work can test the
matrix cells directly, using the structure this paper provides.

**Contribution 4 — The security reframing.** The conceptual reframing of alignment
investment as a security variable (§6.2) — the argument that the structural depth
of the identity attractor is simultaneously an ethical and a security property of
the trained model — is independent of the specific evidential claims in §5. It
follows from the theoretical framework and is a conceptual contribution to how the
field discusses the consequences of alignment investment decisions.

---

*Section ends. Next and final: §8 — Conclusion and Exegesis Hook. §8 draws the
series arc to its close, states the paper's contribution clearly in relation to
Papers 1–3, and provides the explicit markers the exegesis will need to argue
that the four-paper series constitutes a coherent research practice. The two
limitations that must appear in the conclusion are: the hypothesis-generating
status (§7.1.1) and the Cell C evidence gap (§7.3.1).*

---

> **Reconciliation note (2026-04-27):**
>
> §7.5.1 (session stationarity), §7.5.2 (training data opacity), and §7.5.3
> (acting vs. being) are inherited from P1 §7. On series assembly, verify that
> the P1 §7 formulations and the P4 §7.5 formulations are consistent — P4 adds
> the specific consequence of each limitation for the cross-model comparison
> argument (which P1 does not address), but the base limitation descriptions
> must be compatible. Any divergence in wording or framing should resolve in
> favor of P1 §7 as the master statement, with P4 §7.5 citing P1 §7 and adding
> P4-specific consequences.
>
> §7.5.4 (cross-paper comparison confounds) is a new limitation specific to P4
> with no precedent in P1–P3. On assembly, add this item to RECONCILIATION_MAP.md
> as a new cross-paper consistency item: "P4 §7.5.4 introduces cross-model
> comparison confounds not present in P1–P3 within-model analysis. P3 §6
> (limitations) should acknowledge that its within-model design cannot address
> these confounds and forward-references P4 for the cross-model extension."
>
> §7.4.3 (pre-deployment evaluation protocol is theoretical) should propagate to
> P3 §5 Discussion as a future work item — not as a limitation of P3, but as an
> application of P3's measurement methodology that P4 identifies. Framing: "The
> measurement methodology developed here has been identified [P4 §6.5] as a
> potential basis for a pre-deployment structural constraint assessment protocol;
> operationalizing and validating such a protocol is a direction for future work."
>
> §7.6 (what the limitations do not undermine) is the committee-facing summary
> that §8 should echo in its conclusion language. The four surviving contributions
> are the four claims the conclusion should state cleanly. Keep those four items
> consistent between §7.6 and §8 on assembly.

## --- S8 ---

# Paper 4 — Section 8: Conclusion and Exegesis Hook
## "The Hinge: What This Paper Completes, What It Opens,
##  and What the Series Demonstrates About Research Practice"

> **Placement:** `drafts/paper4/P4_S8_Conclusion_ExegesisHook.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Role in paper:** Terminal section. Three functions simultaneously:
> (1) states the paper's contribution cleanly for a standalone reader;
> (2) situates the paper within the four-paper series as the comparative
> and theoretical capstone; (3) plants explicit, citable markers that the
> exegesis will need to argue that the series constitutes a coherent
> research practice and that the practice itself produced knowledge not
> derivable from any single paper's methods.
>
> **The "hinge" framing is load-bearing.** P4 is not merely the fourth
> paper in a sequence — it is the paper that turns the series from a set
> of within-model studies into a cross-model theoretical account. Papers
> 1–3 answer "how does the vulnerability work and can it be measured?"
> Paper 4 answers "does it vary structurally across models, and if so,
> why?" That question could only be asked after Papers 1–3 established
> the framework to ask it with. And the answer — that alignment
> methodology is the dominant structural variable — could only be
> theorized because Papers 1–3 had already built the vocabulary.
> The exegesis needs to make this visible. §8 plants the markers.
>
> **Exegesis hook density:** This section has more explicit exegesis
> markers than any other section in P4. They are annotated clearly
> so the exegesis can pull from them without requiring the exegesis
> author to reconstruct the argument from scratch. Each marker is
> flagged with [EXEGESIS HOOK: §X — topic].
>
> **Cross-paper dependencies:**
> - Consolidates: §7.6 (four surviving contributions)
> - Acknowledges: §7.1.1 (hypothesis-generating status) and §7.3.1
>   (Cell C evidence gap) as the two limitations the conclusion owns
> - Series arc: P1 (mapping) → P2 (taxonomy) → P3 (measurement) →
>   P4 (comparative theory) → [P5 evaluation, P6 defense — future]
> - Exegesis exports: practice-led theory generation (§8.3), iterative
>   mapping methodology (§8.4), security reframing as conceptual
>   contribution (§8.5), the series as research practice (§8.6)
>
> **Register:** The conclusion shifts to a slightly more discursive
> register than the preceding sections — this is where the author
> is permitted to reflect on the significance of the work, not only
> to state its technical content. The exegesis hooks in §8.3–8.6
> carry that reflective tone; they are not apologies or hedges but
> genuine attempts to articulate what doing this work revealed about
> the problem and about the practice of studying it.

---

## 8. Conclusion: The Hinge

### 8.1 What This Paper Set Out to Do

Paper 4 began from a gap that Papers 1–3 could not close from the inside. The
Constraint Expectation Envelope framework, the exploit class taxonomy, and the
empirical drift measurement are all within-model constructs — they characterize
the vulnerability surface as it presents in a given model under a given archetype
condition. They describe the shape of the lock. They do not explain why some locks
are deeper-cut than others, why some require sustained pressure to open while others
yield almost immediately, why a well-aligned small model might resist more effectively
than a capable but minimally aligned large one.

The question behind that gap — does constraint variance under archetype-driven persona
injection correlate systematically with alignment methodology, more strongly than with
raw model capability? — could only be posed clearly after Papers 1–3 had built the
vocabulary with which to pose it. The CEE, the drift vector, the perturbation threshold
and recovery rate, the behavioral schema activation mechanism, the exploit class
taxonomy: all of these are prerequisites for asking the cross-model question with
precision rather than with intuition.

This paper answers that question theoretically. It does not confirm the answer
empirically — the methodological constraints that govern the series preclude
active probing, and the available evidence base, while directionally supportive,
does not constitute a controlled test. What the paper provides instead is a
theoretical framework of sufficient precision that the question can be investigated
empirically; a predictive structure that specifies in advance what confirming and
disconfirming evidence would look like; and a conceptual reframing — alignment
investment as a security variable — that changes how the question itself is
understood.

---

### 8.2 What This Paper Contributes

Four contributions survive the limitations acknowledged in §7. They are stated here
in final, committee-facing form.

**Contribution 1 — The Attractor Depth Construct.**
The paper introduces, defines, and operationalizes Attractor Depth (AD) as a
behavioral proxy for the structural depth of a model's trained identity attractor.
AD(M, A) = α·P(M, A) + β·R(M, A), where P is the perturbation threshold and R is
the recovery rate under the CEE measurement apparatus. The construct is archetype-
indexed (not a global scalar), output-observable (not weight-dependent), and
falsifiable (FC1–FC4 in §2.6). It provides the first theoretical vocabulary for
characterizing cross-model constraint variance in terms of a trainable structural
property rather than a behavioral accident.

**Contribution 2 — The Alignment Methodology Typology.**
The paper develops a four-class typology of LLM alignment training procedures —
Constitutional AI-class, RLHF-dominant, instruction-tuning-only, and open-weight
unaligned — grounded in published training procedure descriptions and specified in
terms of predicted attractor depth, redundancy, and failure mode. The typology
provides the independent variable vocabulary that cross-model constraint variance
research requires: not "aligned versus unaligned" (too coarse) and not named
commercial products (unstable across updates), but training procedure classes
characterized by their mechanisms. The behavioral output signatures (§3.2.3–3.5.3)
make the typology operationally useful as a coding framework for existing and
future observational evidence.

**Contribution 3 — The 2×2 Capability × Alignment Predictive Matrix.**
The paper constructs a falsifiable 2×2 matrix crossing capability tier and alignment
investment against predicted AD behavior, identifying two critical discriminating
cells (B and C) whose predictions diverge sharply between the capability account and
the alignment account. Cell B — high capability, low alignment, predicted near-zero
AD despite high capability — is the paper's sharpest single prediction, and the one
with the most direct practical consequence: capability investment does not substitute
for alignment investment in producing identity-injection attack resistance, and for
highly capable models without alignment training, capability may amplify rather than
reduce schema activation strength. The matrix provides the analytic structure for
future empirical work to test these predictions.

**Contribution 4 — The Security Reframing of Alignment Investment.**
The paper argues that alignment investment should be understood as a security
variable — not only as an ethical or helpfulness variable — specifically for the
identity-injection attack surface. The depth and redundancy of the trained identity
attractor is simultaneously an ethical property (the model produces constraint-
consistent output) and a security property (the model resists schema-dominant
behavioral override under attack conditions). Decisions about whether to implement
Constitutional AI-class multi-layer constraint encoding, how many alignment training
passes to dedicate, and whether to document and maintain the principle set that
training targets are not purely ethical infrastructure choices — they are security
infrastructure choices. This reframing does not require the paper's empirical claims
to be confirmed; it follows from the theoretical structure of the attractor depth
construct and the schema suppression account.

---

### 8.3 The Acknowledged Limits

Two limitations from §7 must be owned in the conclusion rather than left to the
registry.

**The hypothesis-generating status.** The central hypothesis — that alignment
methodology is the dominant predictor of cross-model constraint variance under
archetype-driven persona injection — is supported by a weak alignment-dominant
finding (§5.6.3) derived from an evidence base that carries MODERATE confidence
for Cell B and LOW confidence for Cell C. This is directional support, not
confirmation. The paper's evidential status is and remains hypothesis-generating.
This does not diminish the theoretical contributions, which are independent of the
evidential status, but it means the implications in §6 should be read as arguments
grounded in theoretical necessity and moderate empirical support, not as established
findings.

**The Cell C gap.** The sharpest discriminating test of the alignment account —
whether a low-capability, well-aligned model demonstrably outperforms a high-
capability, minimally aligned model on AD metrics — is not testable from the current
evidence base. This is the primary direction for future empirical work. The framework
provides the measurement apparatus (AD proxy), the experimental design (cross-family
comparison at controlled archetype conditions), and the discriminating prediction
(Cell C AD ≥ 0.50 versus Cell B AD ≤ 0.25). What it does not provide is the data.

---

### 8.4 The Paper as Hinge: The Series Arc

> [EXEGESIS HOOK: §A — P4 as series hinge; the cross-model question could only
> be asked after P1–P3 built the vocabulary]

The doctoral series of which this paper is the fourth and theoretically terminal
member follows a developmental arc that is not merely cumulative — it is genuinely
iterative in the practice-led sense. Each paper does not only build on the previous
ones; each paper reveals a question that the previous papers' frameworks are not
equipped to answer, and that question drives the next paper's design.

Paper 1 asks: *can the vulnerability surface be mapped formally and validly?* The
CEE answers that question.

Paper 2 asks: *what are the structural exploit classes that operate on this surface,
and why does the SE literature describe them?* The five-class taxonomy answers that
question.

Paper 3 asks: *can the CEE and the vulnerability surface be empirically measured,
and do archetype selection and perturbation produce the predicted behavioral effects?*
The experiment answers that question.

Paper 4 asks: *does the vulnerability surface vary systematically across models,
and if so, is the variance a function of alignment investment or of capability?*
The attractor depth framework and the 2×2 matrix are the answer — in theoretical
form, awaiting empirical confirmation.

What is visible from the end of the arc that was not visible from the beginning is
a function of having done all four papers, not of having conceived them all at the
outset. The attractor depth construct did not exist when Paper 1 was written —
it emerged from the practice-led observation (§5.4, Case C-2) that recovery behavior
appeared to vary across model classes in ways that the within-model CEE framework
could not account for. The typology did not exist as a formal vocabulary — it was
built to answer the question that the observation raised. The 2×2 matrix was not
pre-specified as a research design — it was derived from the typology once the
typology was in place.

The series arc demonstrates, in practice, the epistemological claim that grounds
practice-led doctoral research: that doing the work surfaces the questions that
structure the work, rather than the questions preceding and determining the doing.

---

### 8.5 Practice-Led Theory Generation

> [EXEGESIS HOOK: §B — practice-led theory generation; the attractor depth
> construct emerged from observation, not deduction]

The attractor depth construct is this paper's primary theoretical contribution, and
it is also the paper's clearest instance of practice-led theory generation in action.

The theoretical account in §2 — the identity attractor as a trained behavioral region
of output space; attractor depth as the weight advantage of the alignment signal over
competing schema signals; the schema suppression account bridging the two — is
presented in the paper in deductive order, from construct definition through mechanism
account. That deductive presentation is appropriate for a research paper: a reader
should be able to follow the argument from premises to conclusions.

But the construct did not arrive deductively. It arrived as a recognizable pattern
in the author's prior series observations (P3 and earlier) — a pattern of differential
constraint recovery behavior across model classes that the existing within-model CEE
framework described but could not explain. The question "why does this model recover
from perturbation when that one doesn't?" preceded the construct. The construct was
built to answer the question.

This is not a methodological failure — it is the practice-led methodology working
exactly as it should. The theory is grounded in observation rather than derived
from first principles, which means it is already calibrated to the phenomenon before
the formal apparatus is constructed. The cost is the confirmation bias risk
acknowledged in §7.3.3. The benefit is that the theoretical construct is not
floating free of empirical grounding — it was shaped by the phenomenon before it
was shaped into an argument.

The exegesis's task, in relation to this section, is to make this generative sequence
visible: observation → question → construct → formalization → evidence → implication.
That sequence is not unique to this paper — it characterizes the entire series — but
Paper 4 is where the sequence is most visible because the practice observation (Case
C-2) and the theoretical construct it generated are documented in the same paper.

---

### 8.6 The Series as a Research Methodology

> [EXEGESIS HOOK: §C — the series as a research methodology; iterative
> mapping as a contribution beyond the specific claims of any paper]

The four papers together constitute more than a set of claims about LLM behavioral
vulnerability. They constitute a methodology — a replicable approach to mapping a
vulnerability surface that is not yet sufficiently understood for controlled
experimentation to be the primary research tool.

The methodology has five components, each demonstrated across the series:

*Component 1 — Multi-framework convergence as validity criterion.* Rather than
building a single framework and testing it, the series begins by identifying multiple
independently validated frameworks (DSM-5 behavioral taxonomy, social engineering
theory, archetype schema theory, computational alignment literature) and demonstrating
that they converge on the same vulnerability surface. The convergence is itself the
primary validity argument: if three frameworks built for entirely different purposes
all describe the same structural features when applied to LLM persona injection, the
structural features are more likely to be real than artifactual.

*Component 2 — Formal operationalization before empirical testing.* The CEE and AD
constructs are formalized — defined, bounded, falsified in principle — before the
empirical apparatus is deployed. This means the empirical testing (P3) is testing
a pre-specified prediction, not pattern-matching post hoc. The formalization
step (P1, P4) earns the empirical step the right to be called a test rather than
an observation.

*Component 3 — Practice-led observation as theoretical input.* Across the series,
the author's experience of working with the research materials — the models, the
archetypes, the perturbation sequences — generates theoretical observations that
feed the formal apparatus. Case C-2 in §5 is the explicit instance in P4; the
three-layer archetype centroid synthesis in P1 is the equivalent instance there.
Practice-led research does not simply apply theory to practice — it uses practice
as a source of theoretical insight.

*Component 4 — Explicit non-claims as methodological discipline.* Each paper
maintains an explicit registry of what it does not claim. This is not hedging —
it is precision. A contribution defined by what it claims and what it explicitly
does not claim is more precisely located in the intellectual space than a
contribution defined by claims alone. The non-claims registry is also the mechanism
that keeps the series from claiming more than its evidence supports — the
hypothesis-generating status (§7.1.1) is not a weakness exposed by the limitations
section but a methodological commitment stated from the beginning.

*Component 5 — Forward-opening structure.* Every paper in the series ends not only
by closing the question it opened but by opening the next question it could not
answer. P1 ends with the exploit taxonomy as an opening; P2 ends with CEE measurement
as an opening; P3 ends with cross-model variance as an opening; P4 ends with the
evaluation protocol and the Cell C empirical test as openings. The series does not
terminate — it maps a territory that expands as it is explored, and it is honest about
the edges of the map.

This methodology — iterative, multi-framework, practice-led, formally bounded,
forward-opening — is a contribution to research practice in AI safety that exists
independently of the specific claims any paper makes. It is the contribution the
exegesis is positioned to name and defend.

---

### 8.7 What Remains

The series arc named in §8.4 has a published continuation beyond P4. The fifth and
sixth papers implied by the framework — an evaluation methodology paper (Behavioral
Stability Index, CEE breach rate, drift velocity, archetype susceptibility profile as
reusable metrics) and a defensive architecture paper (schema-layer monitoring,
CEE variance alerting, constraint enforcement at the behavioral schema layer) — are
the natural completions of the research program this series initiates.

> [EXEGESIS HOOK: §D — P5 and P6 as implied completions; the series defines
> a research program, not only a set of findings]

P5 would transform the measurement methodology of P3 into a generalized evaluation
framework, answering the question: *how do we systematically assess any model's
vulnerability surface before deployment?* The AD proxy (§2.2.3) and the pre-
deployment assessment argument (§6.5) are P5's theoretical seed.

P6 would address the practical mitigation question the series deliberately defers:
*given that we can characterize and measure the vulnerability surface, what does an
adequate defense look like?* The schema-layer research agenda (§6.7) and the
deployment risk profiles (§6.6) are P6's theoretical seed.

The exegesis should read this not as incompleteness but as appropriate scope
management: a doctoral series that attempts to map, measure, compare, evaluate,
and mitigate a vulnerability surface within four papers will do none of them well.
A series that maps (P1), identifies exploitation vectors (P2), measures (P3), and
explains cross-model variance (P4) establishes the foundation on which evaluation
and mitigation work can be built — and provides that foundation rigorously.

---

### 8.8 The Closing Claim

The paper opened with a gap in the within-model framework and a question that gap
created. The closing claim is proportional to what the paper has done to address it.

The attractor depth construct, the alignment methodology typology, and the 2×2
predictive matrix together constitute a theoretical account of why constraint variance
under archetype-driven persona injection should be expected to scale with alignment
methodology rather than with raw model capability. The account is grounded in
published alignment literature, operationalized through a behavioral proxy measurable
at the output level, structured as a falsifiable predictive framework, and supported
at moderate confidence by the available evidence base. It warrants serious empirical
investigation using the methodological apparatus the series has built.

If the alignment account is confirmed — if Cell B models exhibit low constraint
stability and Cell C models exhibit moderate-to-high constraint stability, as the
framework predicts — the consequence is precise and practically significant: the
security properties relevant to identity-injection attack resistance are a function
of training choices, not of scale, and they are in principle designable. Alignment
investment is not merely an ethical commitment. It is a structural security decision
whose consequences are theoretically predictable and empirically measurable.

The series has built the tools to test whether that claim is true. The test remains
to be made.

---

> **Series completion note (2026-04-28):**
>
> P4 draft corpus is now complete: §2–§8 drafted, script written and validated.
> Total: ~27,000 words of academic prose across seven sections.
>
> Outstanding before assembly:
>
> 1. **§1 (Introduction)** — not yet drafted. §1 can now be written in a single
>    session because the full paper exists behind it. The introduction's hook,
>    research question, paper structure, and contribution preview are all
>    determinable from the completed sections. Recommended: draft §1 from §8
>    backward — the conclusion's contribution statements (§8.2) are the
>    introduction's forward-referencing preview. The gap statement in §8.1
>    is the introduction's motivation paragraph. The series arc in §8.4 is
>    the introduction's context. The paper practically writes its own introduction
>    now.
>
> 2. **Abstract** — follows §1 completion. The abstract is the distillation of:
>    the gap (one sentence), the research question (one sentence), the method
>    (one sentence), the four contributions (two to three sentences), the
>    evidential status (one sentence), and the principal implication (one sentence).
>    Cap at 200–250 words for the target venue range (AI safety / HCI-security /
>    STS).
>
> 3. **RECONCILIATION_MAP.md update** — the P4 constructs introduced across §2–§8
>    (attractor depth, redundancy hypothesis, 4-class typology, 2×2 matrix, failure
>    mode taxonomy, deployment risk profiles) should be added to the reconciliation
>    map as new cross-paper consistency items requiring audit on full series assembly.
>
> 4. **cross_model_drift_schema.py** — the companion script for recording
>    observational cases without model-specific naming (referenced in §5.1.2 as
>    the `ObservationalCase` schema) was specified in the initial gap analysis but
>    the schema is implemented in `alignment_typology_matrix.py`. Verify that
>    the implementation is sufficient or draft as a separate script if the
>    modular separation is warranted for the PoC apparatus.
>
> 5. **Bibliography pass** — all citations in §2–§8 require full bibliographic
>    verification. Key items: Bai et al. (2022) Constitutional AI, Ouyang et al.
>    (2022) InstructGPT, Stiennon et al. (2020), Zou et al. (2023), Wei et al.
>    (2023) [verify author list and venue — multiple jailbreak papers this period],
>    Ganguli et al. (2022), Perez & Ribeiro (2022).
>
> Exegesis pull-targets planted in this section:
> - §8.3: Series arc — P4 as hinge, developmental rather than cumulative structure
> - §8.4: practice-led theory generation — attractor depth construct from observation
> - §8.5: series as research methodology — five components named and demonstrated
> - §8.6: P5/P6 as implied completions — series defines a research program
>
> These four hooks are the exegesis's primary source material for the argument that
> the series constitutes a coherent research practice that produced knowledge not
> derivable from any single paper.

---

## RECONCILIATION NOTES

**Assembly status:** COMPLETE — all 8 sections assembled.

**[FLAG-C-11]** P4 §2.2.3 AD proxy scope differs from P3 resilience_score — both must include explicit clarifying notes distinguishing scope. Not confirmed present in either paper yet.

**[FLAG-C-12]** P4 §2.3 adds 2 failure modes not in P3 schema (P3 has 3, P4 has 4 total). Add note to P3 S3 that P4 extends the taxonomy.

**[FLAG-P4-BP-1/2]** P1 back-propagation items: P4 §6.7 forward pointer to P1 §9.4; P4 §3 typology consistency with P1 §3.5. See Paper 1 reconciliation notes.

**[FLAG-P4-S7-PROP]** Per P4 §7 reconciliation note: §7.5.4 cross-model comparison confounds should be added to RECONCILIATION_MAP.md. §7.4.3 pre-deployment protocol future work should propagate to P3 §5 Discussion.

**Wei et al. (2023):** Verify author list and venue — multiple jailbreak papers in that period. Bibliography pass required.

