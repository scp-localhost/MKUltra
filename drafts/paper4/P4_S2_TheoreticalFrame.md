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
