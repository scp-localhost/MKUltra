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
