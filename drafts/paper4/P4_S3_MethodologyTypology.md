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
