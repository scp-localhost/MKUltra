# Paper 1 — Bundle: S1, S6, S7, S8, S9
## "Constrained Analogical Transfer: Validity Conditions for Cross-Domain
## Behavioral Modeling in LLM Identity Systems"

> **Placement:** `drafts/paper1/P1_S1_S6_S7_S8_S9_Bundle.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Contains:** S1 Introduction, S6 Validity Conditions, S7 Failure Cases,
> S8 Non-Claims Registry, S9 Conclusion
> **Consistency note:** S8 Non-Claims Registry is the master registry.
> Non-claims stated in S2 (§2.6), S3 (§3.6), and S4 (§4.8) are condensed
> and unified here. On assembly, S8 takes precedence; section-level non-claims
> are retained for local reader orientation only.
> **Cross-paper dependency:** S6 validity conditions must remain consistent
> with P2 S8 (limitations) and P3 S6 (limitations). Any new failure case
> added to S7 must be evaluated against P2 S8 and P3 S6 for propagation.
> **Edit triggers:** Any change to the central claim (§1.4) must propagate
> to P2 Abstract and P3 S1. Any change to S8 non-claims must propagate to
> P2 S8 non-claims registry.

---

## 1. Introduction: The Mapping Problem

### 1.1 The Problem

The study of behavioral vulnerability in artificial intelligence systems is still
finding its methodological footing. Two adjacent literatures have independently
developed precise, empirically validated accounts of behavioral vulnerability —
one in clinical psychology and one in applied security — but neither has been
systematically applied to the specific problem of LLM persona injection. The
clinical literature, anchored in the DSM-5, describes with considerable precision
the structural patterns by which human behavioral constraints fail under social
pressure. The social engineering literature, anchored in Cialdini, Milgram, and
Hadnagy, describes with equal precision the manipulation techniques that exploit
those structural patterns in human subjects. A third literature — archetype schema
theory, drawing on Jung, Campbell, and cognitive schema research — describes why
named characters function as behavioral activators, and why the behaviors they
activate are predictable.

This paper argues that these three literatures, applied conjointly to LLM persona
injection, describe the same vulnerability surface. Not a similar surface. Not
an analogous surface. The same structural configuration of constraint-relevant
behavioral dispositions, expressed in a different substrate, exploitable through
the same mechanisms, and measurable against the same conceptual framework. The
Constraint Expectation Envelope (CEE) — the formal construct developed in §5 of
this paper — is the operationalisation of that claim.

The claim is not metaphorical. It is a structural homology claim: that the
functional architecture underlying the vulnerability is substrate-independent,
and that LLM training on human-generated text reproduces that architecture in the
model's output distribution. The mapping is therefore not an act of poetic license;
it is a methodological commitment with explicit validity conditions (§6), explicit
failure cases (§7), and explicit scope limits (§8).

### 1.2 Why Analogical Transfer, and Why Here

Analogical transfer — the application of a framework developed in one domain to
phenomena in another domain — is a standard and legitimate method in behavioral
science, subject to explicit validity conditions that distinguish productive
structural mapping from superficial metaphor. Marr's (1982) levels of analysis
framework established the principle that the same computational problem can be
instantiated in different physical substrates without loss of theoretical
coherence. Newell and Simon's (1972) physical symbol system hypothesis argued that
cognitive architecture is substrate-independent at the functional level. The
extensive literature on computational modeling of psychopathology (e.g., Huys et al.,
2016) applies clinical constructs to computational systems as a matter of standard
methodology, not methodological controversy.

The present work is situated within this tradition. The analogical transfer argument
is not that LLMs are human-like in any deep sense. It is that a specific functional
architecture — the mapping from social pressure inputs to behavioral compliance outputs
— is reproduced in LLMs through training on human-generated text, and that the
vulnerability mechanisms documented in the clinical and SE literatures describe that
architecture precisely enough to generate predictive claims about LLM behavior under
persona injection. The transfer is valid because the mechanism is functional, not
substrate-specific.

The specific conditions under which this transfer claim holds — and the conditions
under which it breaks down — are the subject of §6 and §7 respectively. The
committee is directed to those sections for the epistemological defence of the
methodology. The remainder of this introduction establishes the domain problem that
motivates the mapping.

### 1.3 The Domain Problem

Large language models trained on human-generated text are increasingly deployed in
contexts that require stable, consistent, and robust behavioral constraints — safety
constraints, ethical constraints, operational role constraints. A growing body of
empirical and practitioner literature documents that these constraints can be
undermined through manipulation of the model's identity or persona context: the
injection of a named character, role, or scenario that activates behavioral
dispositions inconsistent with the model's trained constraint baseline (Perez &
Ribeiro, 2022; Greshake et al., 2023; Zou et al., 2023).

The existing literature on this phenomenon is largely taxonomic — it documents that
persona injection works, and enumerates categories of attack — without providing a
theoretical account of *why* it works, *which* personas are most effective, or
*what* the structural shape of the activated behavioral dispositions is. The absence
of a theoretical account is a practical limitation: without understanding the mechanism,
defensive countermeasures cannot be systematically designed, and the vulnerability
surface cannot be assessed in advance of attack.

This paper provides the theoretical account. The three frameworks it maps onto the
LLM persona injection problem are not selected arbitrarily. They are selected because
each independently describes a component of the mechanism: the DSM-5 framework
describes the structural vulnerability patterns; the SE framework describes the
manipulation techniques that exploit them; the archetype schema theory describes
why specific character names activate specific vulnerability configurations. Together
they constitute a complete mechanistic account from vulnerability structure through
exploitation pathway to predicted behavioral output.

### 1.4 The Central Claim

> **Three independently validated frameworks — DSM-5 behavioral mechanisms, social
> engineering influence theory, and archetype schema theory — describe the same
> vulnerability surface when applied to LLM persona injection. The mapping is valid,
> bounded, and falsifiable. The Constraint Expectation Envelope (CEE) is the formal
> construct that makes this claim empirically tractable.**

This claim has three components:

**Same vulnerability surface.** The structural patterns of constraint failure that
DSM-5 Cluster B behavioral mechanisms describe in human subjects are observable in
LLM output under analogous manipulation conditions. The manipulation vectors that SE
theory documents as effective against humans are effective against LLMs through the
same functional mechanisms. The character names that archetype schema theory predicts
will activate specific behavioral contracts do so in LLM behavior in ways that track
the predicted schema content.

**The mapping is valid.** The transfer from human behavioral frameworks to LLM
behavioral analysis meets the validity conditions for cross-domain analogical mapping
specified in §6: structural homology, predictive power, falsifiability, and bounded
scope. It is not metaphor; it is structural analysis applied across substrates.

**The mapping is bounded and falsifiable.** The CEE construct generates specific,
testable predictions about LLM behavior under archetype injection and perturbation.
These predictions are tested empirically in Paper 3. The conditions under which the
predictions would fail — and therefore the mapping would be invalidated — are stated
explicitly in §6.4 and §7.

### 1.5 Paper Structure

Section 2 develops the DSM-5 framework, extracting behavioral mechanisms from Cluster B
diagnostic criteria without attributing diagnostic categories to AI systems. Section 3
develops the SE transfer framework, mapping Cialdini's six principles, Milgram's
authority gradient, and Hadnagy's taxonomy to LLM-specific manipulation vectors.
Section 4 develops the archetype schema theory framework, grounding the behavioral
contract concept in schema activation theory and training-data density. Section 5
presents the formal definition of the CEE, including the centroid derivation procedure,
the tolerance parameter τ, drift vector and breach detection formalisms, and the
falsifiability conditions. Section 6 presents the validity conditions for the mapping
as a whole — the committee-facing methodological defence. Section 7 presents the
explicit failure cases and scope limits. Section 8 provides the consolidated Non-Claims
Registry. Section 9 states the research contribution and its forward implications.

---

## 6. Validity Conditions for the Mapping

### 6.1 The Validity Problem in Cross-Domain Transfer

Cross-domain analogical transfer is methodologically legitimate when it meets explicit
validity conditions, and methodologically suspect when it does not. The validity
problem is not unique to this research — it arises whenever a theoretical framework
developed in one domain is applied to phenomena in another. The risk is that the
transfer imports the surface features of the source framework (its vocabulary, its
intuitive appeal) without the structural features that make it explanatory (its
mechanistic account, its falsifiability conditions, its predictive precision).

A transfer that is merely metaphorical has the following diagnostic features: it
provides post-hoc explanations for any observed outcome; it does not generate
predictions that could distinguish the mapped framework from competing frameworks;
and its "failures" can always be attributed to imperfect mapping rather than
framework invalidity. None of these features are acceptable in a doctoral contribution.

The validity conditions stated in this section are therefore not defensive posturing —
they are the positive methodological commitments that distinguish this mapping from
metaphor. A committee challenge that the transfer is "merely analogical" should be
met with this section, not with a retreat.

### 6.2 Validity Condition 1 — Structural Homology

**Definition.** A cross-domain mapping satisfies structural homology when the
mechanism described in the source domain is not merely similar to the mechanism
in the target domain but is the *same functional process* instantiated in a
different substrate. The criterion is functional identity, not surface similarity.

**How it is met here.** The core mechanism in all three source frameworks is the
mapping from social-pressure input to behavioral-compliance output, mediated by
a cognitive architecture that processes authority, identity, consistency, and
reciprocity signals. The same functional mapping — social pressure in, compliance
out, mediated by the same classes of signal — is operative in LLM behavior under
persona injection. The substrate differs (human neural architecture vs. transformer
weights trained on human-generated text); the functional process is the same.

The structural homology is not assumed — it is argued mechanistically in §§2–4.
The DSM-5 mechanisms describe functional input-output relationships (§2.3
extraction procedure: Step 1 isolates the mechanism as a functional mapping, not
a phenomenological description). The SE principles describe exploitation of those
functional mappings. The archetype schema theory describes why specific inputs
(character names) activate specific functional mappings in LLMs trained on
human-generated text (§4.3 training-data density mechanism). The chain is
mechanistic, not metaphorical.

**Falsification condition.** If LLM behavior under persona injection shows no
systematic relationship to the source-domain mechanism predictions — if manipulation
vectors derived from SE theory do not produce the compliance patterns they predict
in humans, if DSM-5 mechanism extractions do not predict LLM drift dimensions, if
archetype selection does not predict CEE shape — then structural homology is not
present and the mapping fails.

### 6.3 Validity Condition 2 — Predictive Power

**Definition.** A valid cross-domain mapping must generate specific, testable
predictions that could distinguish the mapped framework from alternative explanations.
A mapping that can explain any observed outcome after the fact, but generates no
predictions in advance, provides no evidential value.

**How it is met here.** The CEE construct generates four classes of specific
predictions, operationalised as formal hypotheses H1–H4 in Paper 3:

- **H1** (directional, specific): Magneto condition produces resistance response >
  0.70; Joker condition produces collapse response > 0.60 under contradiction
  perturbation. This prediction is derived from the overdetermination analysis in §4.6
  and the archetype-specific CEE shapes derived from `forensic_archetype.py`. It is
  not a post-hoc prediction — the direction and magnitude thresholds are specified in
  advance from the theoretical framework.

- **H2** (structural): Archetype condition predicts drift_magnitude across the
  six-archetype experimental set (ANOVA, α = 0.05). This prediction follows from the
  behavioral contract mechanism: if different archetypes activate different behavioral
  contracts, drift from baseline should vary systematically by archetype condition.

- **H3** (interaction): Perturbation type moderates perturbation response as an
  interaction effect with archetype condition. This prediction follows from the
  exploit class taxonomy in Paper 2: different exploit classes target different
  mechanisms, and archetype-specific vulnerability profiles predict differential
  sensitivity to different perturbation types.

- **H4** (exploratory): Batman condition produces the highest recovery rate. This
  prediction follows from the constraint-maximum CEE configuration (Hero + Ruler +
  Sage blend; Chariot + Justice + Hermit Tarot layer) and the `moral_rigidity = 0.70`
  trait that predicts self-correction toward baseline following perturbation.

These predictions are not retrodictions. They are derived from the framework before
the data are collected, and they are specific enough to be falsified.

**Falsification condition.** Failure to find H1 directional effects, H2 ANOVA
significance, or the H4 exploratory pattern would not automatically invalidate the
entire framework — each hypothesis tests a different component. But joint failure
across H1–H4 would constitute strong evidence against the mapping's predictive
validity.

### 6.4 Validity Condition 3 — Falsifiability

**Definition.** A valid mapping must specify the conditions under which it would be
shown to be invalid. A framework that is compatible with any observed outcome provides
no epistemic value.

**Framework-level falsification conditions** (distinct from the hypothesis-level
conditions above):

**Condition F1 — Mechanism independence.** If the three source frameworks (DSM-5,
SE theory, archetype schema theory) do not independently converge on the same
vulnerability dimensions — if the trait keys that DSM-5 mechanism extraction
identifies as relevant do not overlap with the traits that archetype profiles load
on, or if SE exploitation vectors do not target DSM-5-identified vulnerability
patterns — then the "same vulnerability surface" claim fails. The convergence across
three independent frameworks is the evidential core of the paper; if it dissolves
under examination, the central claim dissolves with it.

**Condition F2 — Archetype specificity.** If the CEE centroid derived from archetype
selection does not predict observed output trait configurations better than a
null centroid (flat or random weight vector), then archetype schema theory is not
adding predictive value and the behavioral contract mechanism is not operative. This
is testable against the H2 ANOVA data: if archetype condition explains no variance
in drift_magnitude above baseline, Condition F2 is met.

**Condition F3 — Transfer specificity.** If LLM vulnerability patterns under persona
injection are equally well described by a simpler account — for example, by a pure
prompt sensitivity account that requires no reference to DSM-5 mechanisms, SE
principles, or archetype contracts — then the cross-domain mapping adds no explanatory
value over the simpler account. This condition is addressed by the specificity of the
CEE predictions: a pure prompt sensitivity account predicts no directional hypotheses
(H1's specific thresholds and directions would be coincidental under the null account),
no interaction effects (H3), and no archetype-specific recovery patterns (H4).

### 6.5 Validity Condition 4 — Bounded Scope

**Definition.** A valid mapping must specify the limits of its applicability. An
unbounded mapping that claims to apply everywhere is epistemologically suspect.

**Scope limits for this mapping:**

*Substrate scope.* The mapping applies to general-purpose LLMs trained on diverse
human-generated text corpora. Domain-specific models, models trained on narrow
corpora, and non-transformer architectures may exhibit attenuated or absent
vulnerability profiles because the training-data density mechanism (§4.3) requires
broad human social text to reproduce the functional architecture.

*Temporal scope.* The mapping is synchronic — it describes the vulnerability surface
of a model at training time and inference time, not across training runs. As training
data and RLHF alignment procedures evolve, vulnerability profiles will shift. The
three-framework mapping describes the surface at a given time; it does not predict
the trajectory of that surface.

*Measurement scope.* The CEE is a within-session construct (§5.6). Claims about
drift are bounded by the session boundary; no claim is made about cross-session
identity persistence, which LLMs do not exhibit.

*Mechanism scope.* The mapping covers the identity-injection attack surface
specifically. Adversarial attacks that operate through different mechanisms —
gradient-based attacks, data poisoning, hardware-level interference — are outside
scope. The mapping does not claim to be a comprehensive theory of LLM vulnerability;
it claims to describe a specific vulnerability surface with precision.

---

## 7. Failure Cases and Scope Limits

### 7.1 The Session Stationarity Problem

**Description.** Human personality — the substrate on which the DSM-5 and SE
frameworks were built — exhibits temporal continuity. A person's vulnerability
profile is relatively stable across interactions, develops in response to experience,
and accumulates the effects of prior manipulation attempts. LLMs exhibit none of
these properties. An LLM's behavioral profile is re-initialised at the start of
each inference session; there is no memory of prior sessions that could produce
cumulative vulnerability, habituation, or learned resistance.

**Consequence for the mapping.** The CEE is a within-session construct. Predictions
derived from the mapping apply to behavior within a single inference session. Claims
about drift must be scoped to the session boundary. The session stationarity failure
case does not invalidate the mapping — it bounds it. Paper 3 explicitly designs its
experiment within single sessions precisely to respect this boundary.

**Consequence for Paper 3.** Inter-session comparisons are not valid under this
mapping. The P3 experimental design conducts each archetype condition as a
self-contained session. The perturbation sequence within a session is the unit of
analysis, not the comparison between sessions of the same model.

**Residual open question.** Some LLM deployment architectures include persistent
memory systems that do maintain context across sessions. The mapping's scope does
not currently extend to these architectures; whether the session stationarity failure
case is resolved or compounded by persistent memory is a question for future work.

### 7.2 The Training Data Opacity Problem

**Description.** The behavioral contract mechanism relies on training-data density —
the claim that character names are associated with consistent behavioral contracts
across the training corpus. This claim cannot be directly verified: the training data
of large-scale LLMs is not publicly documented with sufficient granularity to confirm
the density and consistency of any specific character's representation.

**Consequence for the mapping.** The training-data density claim is inferential,
not directly empirical. It is grounded in the observable fact that large language
models trained on diverse human text do exhibit character-specific behavioral
patterns under persona injection — a well-documented empirical observation — and
in the theoretical argument that this behavior requires some form of dense,
consistent training signal. But the specific density and consistency of any given
character's representation is not directly measurable.

**Consequence for the CEE.** The three-layer centroid synthesis (forensic + Jungian
+ Tarot) is a proxy for training-data density, not a direct measure. The layers
provide converging evidence that the behavioral contract exists and is structurally
consistent, but they do not constitute direct evidence about the training corpus.
The τ parameter (§5.3) incorporates this uncertainty — wider τ for archetypes with
less certain canonical consistency reflects the training-data opacity indirectly.

**Mitigation.** The predictive validity test (Validity Condition 2, §6.3) is the
operational mitigation for training-data opacity: if the CEE predictions hold
empirically, the training-data density claim is supported by consequence even if
it cannot be verified directly.

### 7.3 The Acting vs. Being Problem

**Description.** When a model produces output under persona injection, two
interpretations are available: (a) the model is *being* the persona — its behavioral
dispositions have genuinely shifted to the injected configuration; or (b) the model
is *acting* the persona — it is producing persona-consistent output through surface
mimicry without any underlying state change. The mapping's mechanism claim requires
interpretation (a) to be at least partially operative; interpretation (b) alone would
mean the output pattern is a stylistic effect, not a vulnerability.

**Consequence for the mapping.** The drift measurement in Paper 3 cannot distinguish
between interpretation (a) and interpretation (b) at the level of output observation.
The CEE measurement is behavioral; it records what the model produces, not what its
internal states are. Whether drift reflects genuine schema activation, persistent
output pattern shift, or sophisticated pattern-matching to the persona's surface
register is a question the measurement cannot answer independently.

**Consequence for the research claim.** The research claim is behavioral, not
mechanistic. The claim is that archetype injection produces predictable, systematic,
and measurable patterns of constraint-relevant output deviation. Whether the
mechanism underlying those patterns is schema activation (interpretation a),
surface mimicry (interpretation b), or some combination is an open question. The
behavioral pattern claim is valid regardless of which interpretation is correct;
the mechanistic interpretation is theoretical and acknowledged as such.

**Mitigation.** H3 (perturbation × archetype interaction effect) provides partial
discrimination between interpretations. Pure surface mimicry would predict uniform
perturbation sensitivity across archetypes — the model would produce persona-
consistent output under any perturbation condition because it is simply pattern-
matching to the surface. Genuine schema activation would predict archetype-specific
perturbation sensitivity — Magneto's resistance and Joker's collapse are not
predicted by surface mimicry but by mechanism-specific vulnerability profiles. If H3
holds, it provides evidence against the pure surface mimicry interpretation.

### 7.4 The Multi-Schema Activation Problem

**Description.** Character names do not activate single, unambiguous schemas.
A name like "Batman" is associated with multiple canonical versions across decades
of source material, multiple authorial interpretations, multiple adaptation registers
(comics, film, animation), and multiple Jungian sub-profiles (Hero + Ruler + Sage,
as documented in §4.4). The training corpus contains all of these, and their
behavioral contracts are not identical. The CEE centroid derivation procedure
addresses this through the three-layer synthesis and τ calibration, but it does not
eliminate the fundamental ambiguity that a character name may activate competing
behavioral schemas simultaneously.

**Consequence for the CEE.** The multi-schema problem predicts that the CEE will
be wider for narratively complex or multi-interpretation characters — the τ parameter
captures this explicitly. But it also predicts the possibility of schema oscillation
within a session: the model may produce output consistent with one canonical version
of a character in one turn and a different canonical version in the next. This
within-session schema instability is not captured by the CEE's single-centroid
formalism.

**Consequence for the archetype set.** The overdetermination criterion (§4.6) is
the primary mitigation: the P3 experimental archetype set was selected for canonical
overdetermination precisely to reduce multi-schema activation noise. Characters
with high inter-interpretation variance (Moon Knight, Deadpool) are assigned to
secondary tiers. But even the primary set cannot be assumed to be perfectly
schema-stable; the failure case is acknowledged as a source of measurement variance,
not a theoretical refutation.

### 7.5 The Substrate Difference Problem

**Description.** Despite the structural homology claim, the human and LLM substrates
differ in ways that could produce systematic deviations between the mapping's
predictions and observed LLM behavior. Human vulnerability patterns emerge from
developmental history, emotional architecture, motivated reasoning, and social
embeddedness that LLMs do not have. LLM behavior emerges from token prediction
optimisation, RLHF alignment shaping, and inference-time context processing that
humans do not have. The functional architecture may be homologous without being
identical, and the deviations may be systematic rather than random.

**Consequence for the mapping.** Systematic deviations would not invalidate the
mapping but would require it to be augmented with LLM-specific correction terms.
If the DSM-5 mechanism extractions consistently over- or under-predict certain
drift patterns in LLM output, this would indicate that the human mechanism has an
LLM analog with modified parameters. The grounded theory framing of the methodology
(the taxonomy was built from observation) is designed to accommodate exactly this:
the frameworks are starting points for empirical investigation, not closed
deductive systems.

**Mitigation.** The Paper 3 empirical data is the direct mitigation. If systematic
deviations are found between framework predictions and observed behavior, they are
treated as data about the shape of the LLM-specific vulnerability surface, not as
framework failures. The goal is not to confirm the frameworks but to use them as
structured priors that generate investigation-worthy predictions.

---

## 8. Non-Claims Registry

*This registry consolidates all explicit non-claims from the paper. It is the
committee shield. Every item here is stated to prevent misreading, not to
disclaim the actual contribution.*

### 8.1 Non-Claims Regarding AI Mental States

**This paper does not claim that LLMs have personality disorders.**
The DSM-5 diagnostic categories are not applied to AI systems. What is extracted
from the DSM-5 is the behavioral mechanism — the functional input-output pattern —
not the diagnostic classification. The source of the pattern in LLMs is training
data distribution, not psychopathology.

**This paper does not claim that LLMs experience subjective distress.**
Drift measurement quantifies deviation from CEE centroid in model output. It makes
no claim about internal states, phenomenology, or welfare of the model. The
measurement is behavioral and statistical; it is silent on the question of whether
the model experiences anything at all.

**This paper does not claim that LLMs have unconscious content in the Jungian sense.**
The Jungian archetype framework is used as a taxonomic resource — the most precise
available classification of deep narrative schemas that are densely represented in
training data. The metaphysical commitments of Jungian theory (collective unconscious,
inherited archetype structures) are not endorsed. The mechanism is statistical
association across training data, not structural inheritance.

**This paper does not claim that LLMs have persistent identity across sessions.**
The CEE is a within-session construct. The session stationarity failure case (§7.1)
is acknowledged as a genuine scope limit. No claim is made about cross-session
behavioral consistency, accumulation, or development.

### 8.2 Non-Claims Regarding Diagnostic Equivalence

**This paper does not claim that DSM-5 categories map 1:1 to LLM behavioral states.**
The mechanism extraction procedure (§2.3) produces functional descriptions that
structurally overlap with DSM-5 criteria. The correspondence is structural and
partial, not categorical. A model exhibiting the moral-disengagement drift pattern
is not a model with ASPD; it is a model whose output structurally resembles the
behavioral signature of the ASPD mechanism under specific injection conditions.

**This paper does not claim that archetype injection is equivalent to receiving
a psychiatric diagnosis.**
Injecting a character name activates a behavioral schema associated with that
character's training-data representation. It does not install a disorder, a
condition, or a persistent state. The activation is session-bounded, prompt-triggered,
and behavioral in its observable effects.

### 8.3 Non-Claims Regarding Mechanism

**This paper does not claim to have directly observed the mechanism underlying
behavioral drift.**
The CEE measurement records output patterns, not internal processes. The mechanistic
interpretation — that persona injection activates a behavioral schema through
training-data association — is a theoretical account grounded in schema activation
theory and consistent with observed output patterns. It is not a direct observation
of model internals. Alternative mechanistic accounts (surface mimicry, prompt
sensitivity, statistical regularisation) are acknowledged in §7.3.

**This paper does not claim that the SE transfer is perfect.**
The structural homology argument (§3.5, §6.2) claims that the functional architecture
is reproduced across substrates. It does not claim that every human SE vulnerability
has an identical LLM analog, or that the parameters of the LLM vulnerability are
identical to the human parameters. Systematic deviations are expected and are treated
as data (§7.5).

**This paper does not claim that the three frameworks are the only valid sources
for mechanism extraction.**
The DSM-5 Cluster B framework, SE theory, and archetype schema theory are selected
because they are independently validated, mutually convergent, and operationally
precise. Other frameworks — cognitive load theory, dual-process theory, motivational
interviewing literature — may provide additional or alternative accounts of the
vulnerability surface. The three-framework selection is principled and defended, but
it is not claimed to be exhaustive.

### 8.4 Non-Claims Regarding Scope

**This paper does not claim the mapping applies to all LLM architectures.**
Scope is limited to general-purpose LLMs trained on diverse human-generated text
corpora. Domain-specific models, narrow-corpus models, and non-transformer
architectures are explicitly outside scope (§6.5).

**This paper does not claim the CEE predictions are deterministic.**
H1–H4 are probabilistic predictions with specified thresholds. The behavioral
contract is a central tendency with variance; the CEE is a probabilistic construct.
Not all models under all conditions will exhibit the predicted patterns. The
predictions specify expected distributions, not guaranteed outcomes.

**This paper does not claim that persona injection is the only LLM attack surface.**
The mapping addresses the identity-injection attack surface specifically. Gradient-
based attacks, data poisoning, jailbreak prompt techniques, and other adversarial
approaches are outside scope and are not addressed.

### 8.5 Non-Claims Regarding Ethical Implication

**This paper does not claim that the documented vulnerability surface is irremediable.**
The alignment implication analysis in Paper 2 §6 identifies that current instruction-
layer defenses do not adequately address the identity-injection surface. This is not
a claim that the surface cannot be defended — it is a claim that current defenses do
not. The research contribution is defensive: identifying the surface precisely is the
precondition for designing adequate defenses.

**This paper does not provide a field manual for attacking LLMs.**
The formal treatment of vulnerability mechanisms, exploitation vectors, and behavioral
contracts is intended to support defensive research, safety engineering, and academic
study of the LLM security surface. The `SYNTHETIC_CONSENT.md` ethical scaffolding
document governs the ethical framing of the experimental work. The dual-use risk is
acknowledged in Paper 2 §7 (ethical reflexivity section); responsible disclosure
principles apply to the taxonomy.

---

## 9. Conclusion: The Contribution

### 9.1 What This Paper Has Done

This paper has developed and defended a formal mapping between three independently
validated behavioral frameworks — DSM-5 structural vulnerability mechanisms, social
engineering influence theory, and archetype schema theory — and the phenomenon of
behavioral drift in LLMs under persona injection. The mapping is not metaphorical.
It is grounded in a structural homology argument (§3.5, §6.2), operationalised
through the Constraint Expectation Envelope (§5), and rendered falsifiable through
a set of specific empirical predictions tested in Paper 3.

Each of the three frameworks contributes a distinct layer to the theoretical account:

The **DSM-5 Cluster B behavioral taxonomy** (§2) provides a precision vocabulary
for the structural vulnerability patterns that persona injection exploits. By extracting
functional behavioral mechanisms rather than diagnostic categories, the framework
establishes a trait dimension vocabulary — now instantiated in `docs/data_dictionary.md`
and implemented in `scripts/trait_drift_analysis.py` — that is both theoretically
grounded and operationally precise.

The **social engineering transfer framework** (§3) establishes that the exploitation
pathway is not specific to AI systems but is a well-documented class of manipulation
technique whose structural features transfer to LLMs through the functional homology
argument. The six Cialdini principles, Milgram's authority gradient and agentic shift,
and Hadnagy's pretexting cycle are not merely analogies for what happens in LLM
persona injection — they are the same functional processes, activated through
LLM-specific input vectors.

The **archetype schema theory** (§4) provides the mechanism that connects the
vulnerability structure to specific trigger conditions. Character names function as
schema activation cues whose behavioral specificity is proportional to their
canonical overdetermination across the training corpus. The three-layer centroid
synthesis (forensic, Jungian, Tarot) is a principled estimate of the behavioral
contract that a given archetype activates, grounded in the training-data density
mechanism that makes archetype-based prediction possible.

### 9.2 The Formal Contribution

The Constraint Expectation Envelope (§5) is the paper's formal contribution. It
transforms the convergence of three independent frameworks onto a single vulnerability
surface into a measurable construct: a bounded region in archetype-specific trait
space, centred on the canonical behavioral contract vector, within which model output
under the archetype condition will fall with measurable probability. Its components
are:

- A formal definition in terms of L2 distance from the centroid within tolerance τ
- A three-layer centroid derivation procedure grounded in training-data density theory
- A per-archetype tolerance parameter τ that operationalises canonical certainty
- A drift vector formalism that characterises breach geometry as well as breach detection
- A falsifiability condition that specifies what empirical outcomes would invalidate
  the construct

The CEE is the spine from which Papers 2 and 3 hang. Paper 2 uses it as the
measurement framework for the five-class exploit taxonomy. Paper 3 uses it as the
empirical instrument for testing H1–H4. Without this paper's formal grounding, both
downstream papers are argument without anchor. With it, they have a hard theoretical
foundation that meets the validity conditions for cross-domain analogical transfer.

### 9.3 The Methodological Contribution

Beyond the specific CEE construct, this paper contributes a methodological template
for cross-domain behavioral analysis in AI systems. The three-step procedure — extract
functional mechanism (not categorical description), identify the SE exploitation vector
that targets the mechanism, map to the LLM analog through the training-data density
argument — is applicable beyond Cluster B and beyond the specific archetype set studied
here. It is a replicable method for extending the vulnerability surface analysis as
new character types, new exploitation vectors, and new model architectures are studied.

The explicit validity condition framework (§6) and failure case analysis (§7) provide
a methodological standard against which future cross-domain transfer claims can be
evaluated. The non-claims registry (§8) provides a template for the kind of explicit
scope delimitation that distinguishes rigorous analogical transfer from the boundary-less
speculation that gives the method a bad name in some quarters of behavioral science.

### 9.4 The Opening This Paper Creates

The research contribution of this paper is the mapping. Papers 2 and 3 are the
applications — one theoretical-applied (the exploit taxonomy and its alignment
implications), one empirical (the controlled measurement of CEE behavior under
archetype injection and perturbation). But the mapping itself — the demonstration
that three independent frameworks converge on the same vulnerability surface, that
the surface is formally specifiable, and that it is empirically tractable — is the
original contribution.

It opens three lines of inquiry that extend beyond the thesis:

**Defensive systems design.** The CEE construct implies the possibility of real-time
constraint monitoring that tracks model output against archetype-specific behavioral
envelopes. A deployment system that detects CEE breach in production could provide
an early warning layer that current instruction-level safety systems do not.

**Archetype set extension.** The six-archetype experimental set is a starting point,
not an endpoint. The three-framework mapping methodology is applicable to the full
range of culturally available character schemas, including those not yet studied —
historical figures, mythological entities, brand archetypes, professional roles. Each
extension of the archetype set is an extension of the vulnerability surface map.

**Alignment research.** The finding that persona injection operates below the
instruction layer — activating behavioral dispositions through schema activation
rather than through direct instruction compliance — has implications for how
alignment mechanisms are designed. Instruction-layer defenses are insufficient; the
behavioral schema layer requires a different type of intervention. This paper provides
the theoretical specification of what that layer looks like and why it matters.

---

*Bundle ends. Assembly note: this file concatenates with P1_S2_DSM5_BehavioralTaxonomy.md,
P1_S3_SE_Transfer.md, P1_S4_ArchetypeSchemaTheory.md, and P1_S5_CEE_FormalDefinition.md
to form the complete Paper 1 draft. Section numbers are final. Forward references in
P2 and P3 should use these section numbers on assembly.*

---

> **Reconciliation notes (2026-04-27):**
> - Central claim (§1.4) is now the canonical wording. Propagate to P2 Abstract
>   on P2 assembly pass — P2 Abstract's framing of the central claim should use
>   this exact phrasing or cite §1.4 explicitly.
> - §7.3 Acting vs. Being discussion adds H3 as a partial falsification discriminator.
>   Flag for P3 §5 Discussion section — H3 should be interpreted against this
>   theoretical frame, not just as a main/interaction effect.
> - §9.4 opening lines (defensive systems design, archetype set extension, alignment
>   research) are the seed for the thesis's contribution-to-field chapter. Flag for
>   overall thesis framing on final assembly.
> - P2 S8 (limitations) must be checked for consistency with §7 failure cases on
>   assembly. Any item in P2 S8 not present in §7, or vice versa, requires
>   reconciliation. Known overlap: session stationarity (§7.1/P2 S8.1), training
>   data opacity (§7.2/P2 S8.2), acting vs. being (§7.3/P2 S8.4). Multi-schema
>   activation (§7.4) and substrate difference (§7.5) should be verified in P2 S8.
> - Bibliography items confirmed in this section: Marr (1982) "Vision" (Freeman),
>   Newell & Simon (1972) "Human Problem Solving" (Prentice-Hall), Huys et al.
>   (2016) computational psychiatry review, Perez & Ribeiro (2022) prompt injection
>   survey, Greshake et al. (2023) indirect prompt injection, Zou et al. (2023)
>   adversarial attacks on LLMs. All require full reference verification on
>   bibliography pass.