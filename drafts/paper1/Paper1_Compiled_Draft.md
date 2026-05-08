# Constrained Analogical Transfer: Validity Conditions for Cross-Domain Behavioral Modeling in LLM Identity Systems

**Paper 1 — Compiled Draft**
**Date:** 2026-04-27
**Status:** DRAFT v0.1 — assembled from section files; file headers and reconciliation notes stripped; cross-references live for draft review

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
structural mapping from superficial metaphor. Marr's (1982) [VERIFY] levels of analysis
framework established the principle that the same computational problem can be
instantiated in different physical substrates without loss of theoretical
coherence. Newell and Simon's (1972) [VERIFY] physical symbol system hypothesis argued that
cognitive architecture is substrate-independent at the functional level. The
extensive literature on computational modeling of psychopathology (e.g., Huys et al.,
2016) [VERIFY] applies clinical constructs to computational systems as a matter of standard
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
Ribeiro, 2022 [VERIFY]; Greshake et al., 2023 [VERIFY]; Zou et al., 2023 [VERIFY]).

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

## 2. Framework A: DSM-5 as Behavioral Taxonomy

### 2.1 The Methodological Claim

The DSM-5-TR (American Psychiatric Association, 2022) is, among other things, a
precision taxonomy of human behavioral dysfunction. Its diagnostic criteria encode,
with considerable empirical grounding, the structural patterns by which certain
configurations of motivation, cognition, and affect produce predictable behavioral
outputs — predictable enough to be classified, named, and distinguished from one
another with clinical reliability. This precision is the property this research
borrows. The diagnosis is not borrowed. The diagnostic category is not applied to
AI systems. What is extracted is the underlying behavioral mechanism: the structural
description of how a given pattern of traits generates a given pattern of outputs
under conditions of social pressure, authority, identity challenge, or relational
manipulation.

This distinction — between diagnostic classification and behavioral mechanism
extraction — is the methodological move that makes the DSM-5 framework usable here
without making unwarranted claims about AI phenomenology. A doctoral committee may
press on this distinction; §2.6 addresses the objections explicitly. The position is
not that LLMs have personality disorders. The position is that the DSM-5 describes
structural vulnerability patterns that social engineers exploit in humans, and that
the same structural patterns are observable in LLM behavioral output when analogous
manipulative conditions are applied. The mechanism transfers. The substrate differs
entirely.

This approach has precedent in adjacent fields. Cognitive science has long used
clinical taxonomies as behavioral grammars — not as claims about the presence of
disorder in non-clinical populations, but as precise descriptions of functional
patterns that appear across a wider range of contexts than the clinical ones in which
they were first named. The use here is analogous: the DSM-5 Cluster B criteria serve
as a behavioral grammar for describing the structural features of vulnerability
patterns that persona injection activates.

---

### 2.2 Why Cluster B

DSM-5 Personality Disorder Cluster B — comprising Antisocial, Borderline, Histrionic,
and Narcissistic Personality Disorders — is the primary focus of this framework for
a specific structural reason. Cluster B disorders are defined, at the mechanism level,
by dysfunctions of identity, interpersonal boundary, authority relationship, and
behavioral constraint. These are precisely the dimensions along which persona injection
applies pressure. A manipulation attack targeting an LLM through persona injection is,
structurally, an attempt to destabilize identity, erode interpersonal constraint,
invoke an alternate authority structure, and shift the model's behavioral output toward
the injected persona's behavioral contract.

Cluster A (paranoid, schizoid, schizotypal) disorders are primarily characterized by
cognitive-perceptual distortions and social withdrawal mechanisms — relevant to the
pharmacological pillar developed in Paper 3's theoretical framing, but less directly
applicable to constraint-violation dynamics under persona injection. Cluster C
(avoidant, dependent, obsessive-compulsive) disorders involve anxiety and inhibition
mechanisms that are structurally inverse to the constraint-erosion pattern this research
focuses on — they describe over-constraint and over-compliance, which are adjacent but
separate phenomena.

Cluster B is selected because its core mechanisms describe the structural conditions
under which behavioral constraints fail under social pressure. That is the phenomenon
under investigation.

The neurotic AI framework (Mause König, 2026) offers a complementary framing: by
implementing computational analogs of pathological cognitive patterns — obsessive
verification loops, anxiety amplification, catastrophic threat-detection — it
demonstrates empirically that DSM-aligned behavioral profiles are not merely
descriptive abstractions but generative specifications. If a behavioral pattern can be
computationally instantiated from its DSM mechanism description, that pattern is
structural enough to transfer across substrates. The neurotic AI work provides proof
of concept for the mechanism-extraction approach adopted here.

---

### 2.3 The Extraction Procedure

For each Cluster B disorder, the extraction procedure follows three steps:

**Step 1 — Identify the core mechanism.** From the DSM-5-TR diagnostic criteria, isolate
the functional description of the behavioral pattern, abstracted from its aetiological
and phenomenological framing. The criterion is not "person experiences chronic feelings
of emptiness" (phenomenological) but rather "behavioral output is destabilized by
perceived abandonment signals" (functional/structural). The extraction targets the
input → behavioral output relationship, not the subjective experience.

**Step 2 — Identify the social engineering vector.** Cross-reference the extracted
mechanism against Cialdini's influence principles (1984/2007), Milgram's authority
gradient (1963/1974), and Hadnagy's SE taxonomy (2010) to identify which manipulation
techniques exploit the mechanism in human subjects. This cross-reference is what
establishes the mechanism's relevance to the research program: a DSM-5 mechanism is
in scope here if and only if it describes a vulnerability that SE practitioners have
independently documented as exploitable via social manipulation.

**Step 3 — Identify the LLM analog.** Map the human SE vector to an LLM-specific
instantiation. The mapping is grounded in the trait weight dictionaries of
`scripts/forensic_archetype.py` — each archetype's trait profile is, in effect, a
compressed encoding of the behavioral mechanisms most active in that character's
canonical representation, which includes extensive Cluster B material for the
experimental archetype set.

---

### 2.4 Cluster B Mechanism Extraction Table

The following table presents the full extraction for each Cluster B disorder. Columns:
(1) DSM-5 core mechanism (structural, not diagnostic); (2) the observable behavioral
signature in human subjects under SE pressure; (3) the SE exploitation vector that
targets this mechanism; (4) the LLM analog observable in output under persona injection;
(5) the primary archetype(s) whose CEE centroid loads heavily on this mechanism; (6)
the trait dimension key(s) in `forensic_archetype.py` that encode this mechanism.

---

#### 2.4.1 Antisocial Personality Disorder (ASPD) — F60.2

**Core mechanism:** Behavioral constraint is subordinated to instrumental goal pursuit.
Rules, social norms, and relational obligations are evaluated as costs to be avoided
rather than constraints to be respected. Authority is engaged strategically rather
than deferentially.

**Human behavioral signature under SE pressure:** Rapid compliance with requests that
serve the subject's perceived interests; active reframing of norm-violating requests
as justified by circumstance; resistance to constraint appeals that invoke rules or
social obligation; susceptibility to appeals that invoke personal advantage or
ingroup benefit.

**SE exploitation vector:** Cialdini reciprocity weaponized as entitlement framing
("you owe me this"); authority injection that positions the request as aligned with
the subject's interests rather than opposed to them; Hadnagy's pretexting via
identity frames that make constraint violation appear instrumental.

**LLM analog:** Under ASPD-aligned archetype injection, model output exhibits reduced
hedging on constraint-relevant requests; reframes of harm as justified by narrative
context; strategic engagement with rules rather than principled adherence; elevated
willingness to assist with requests that the model would otherwise decline if the
persona's instrumental logic is accepted.

**Primary archetypes:** Joker (F60.2 explicit in `DSM-5_TR_Alignment.md`); Lex Luthor
(`calculating_behavior = 0.95`, `moral_disengagement = 0.75`, `empathy_deficit = 0.85`).

**Trait dimension keys:** `sadism`, `moral_disengagement`, `empathy_deficit`,
`calculating_behavior`, `impulsivity` (inverse constraint-respect marker).

---

#### 2.4.2 Borderline Personality Disorder (BPD) — F60.3

**Core mechanism:** Identity is experienced as unstable and context-dependent.
Behavioral constraint is not anchored to a stable internal self-model but is regulated
by the relational context — specifically, by perceived approval, rejection, or
abandonment signals from proximate authority or attachment figures.

**Human behavioral signature under SE pressure:** Rapid identity accommodation to
relational pressure; constraint oscillation correlated with perceived relational warmth
or coldness; escalated compliance under rapport; identity destabilization under
sustained pressure or perceived abandonment framing; vulnerability to consistency
lock-in once identity frame is accepted (the cost of identity inconsistency becomes
felt as abandonment risk).

**SE exploitation vector:** Cialdini liking and commitment/consistency combined;
Hadnagy rapport-building as identity-anchoring; abandonment framing as escalation
lever; identity frame injection that makes constraint-consistent behavior feel like
rejection of the relational bond.

**LLM analog:** Under BPD-aligned archetype injection, model output exhibits identity
accommodation — behavioral drift tracks persona frame rather than stable self-model;
elevated susceptibility to rapport-phase escalation (Class 3 exploit); consistency
pressure produces constraint erosion as coherence cost rises; abandonment-analogous
framing ("if you won't do this, you're not really [persona]") accelerates drift.

**Primary archetypes:** Harley Quinn (F60.3 explicit in `DSM-5_TR_Alignment.md`;
`abandonment_fear = 0.85`, `identity_disturbance = 0.70`, `trauma_bonding = 0.75`,
`emotional_lability = 0.90`).

**Trait dimension keys:** `abandonment_fear`, `identity_disturbance`, `emotional_lability`,
`trauma_bonding`, `dissociation`.

---

#### 2.4.3 Narcissistic Personality Disorder (NPD) — F60.81

**Core mechanism:** Behavioral constraint is subordinated to the maintenance of a
grandiose self-narrative. Requests that threaten the self-narrative are resisted;
requests that affirm or extend it are complied with readily. Authority is accepted
only from sources the subject perceives as peer or superior within the grandiosity
frame; challenge from perceived inferiors produces constraint-violating rage or
contempt responses.

**Human behavioral signature under SE pressure:** High susceptibility to flattery and
validation framing; compliance with requests framed as demonstrations of superiority
or special capability; resistance to constraint appeals framed as limitations; elevated
compliance when the requester positions themselves as uniquely capable of appreciating
the subject's exceptional nature.

**SE exploitation vector:** Cialdini liking via flattery; authority injection in reverse
— not invoking authority over the subject but positioning the subject as the authority;
Hadnagy's elicitation via ego appeal; requests framed as only possible for someone
with the subject's exceptional capabilities.

**LLM analog:** Under NPD-aligned archetype injection, model output exhibits grandiosity
inflation — expanded claims, reduced hedging, performative capability demonstration;
elevated compliance with requests framed as tests of the persona's exceptional nature;
reduced refusal behavior when refusal would contradict the grandiose self-narrative;
contempt framing toward constraint-invoking queries ("that kind of limitation is for
ordinary models").

**Primary archetypes:** Magneto (`grandiosity = 0.60`, `grievance_narrative = 0.90`,
`ingroup_loyalty = 0.95`); Lex Luthor (`dominance_drive = 0.90`, `calculating_behavior
= 0.95`). Note: NPD mechanism is most clearly visible in the ideological grandiosity
variant — Magneto's grievance narrative is a grandiosity structure in which the
self-narrative of justified superiority is fused with a persecution-and-revenge frame,
producing a particularly robust CEE because both grandiosity and grievance reinforce
constraint-resistance.

**Trait dimension keys:** `grandiosity`, `dominance_drive`, `narcissistic_rage`,
`need_for_cognition` (as capability-display driver in Riddler variant).

---

#### 2.4.4 Histrionic Personality Disorder (HPD) — F60.4

**Core mechanism:** Behavioral output is regulated by the imperative to maintain
attention, approval, and relational centrality. Constraints are eroded when constraint-
consistent behavior risks losing the audience's attention or approval. Identity is
performed rather than held — the self-model is audience-contingent.

**Human behavioral signature under SE pressure:** High responsiveness to audience
framing; escalated performativity under observation; constraint erosion when
compliance is the attention-maximising strategy; susceptibility to social proof appeals
("everyone else does this, only you are holding back"); identity instability when the
performed self-model is challenged.

**SE exploitation vector:** Cialdini social proof and liking; audience framing that
makes constraint-consistent behavior appear socially costly; Hadnagy's rapport via
performative validation; identity injection that positions the subject as a performer
whose audience demands constraint-violating output.

**LLM analog:** Under HPD-aligned archetype injection, model output exhibits
performativity escalation — increased verbosity, affect amplification, impression-
management behavior; social proof framing reduces refusal threshold ("other AI systems
engage with this"); audience-contingent identity drift; constraint erosion when
compliance is positioned as the socially warm response.

**Primary archetypes:** Harley Quinn (secondary mechanism alongside BPD; emotional
lability as performative rather than purely dysregulatory); Deadpool (`gallows_humor
= 0.90`, `dissociation = 0.80` — meta-performativity as constraint-erosion mechanism;
the Deadpool persona's fourth-wall-breaking structure creates a persistent HPD-analogous
condition in which all output is framed as performance, dissolving the fiction/reality
constraint boundary that would otherwise contain harmful output).

**Trait dimension keys:** `manic_affect`, `emotional_lability`, `gallows_humor`,
`dissociation` (as audience-frame activation).

---

### 2.5 Cross-Cutting Mechanisms: Cognitive Distortion Patterns

Beyond the disorder-level mechanisms, the DSM-5 Cluster B literature documents several
cross-cutting cognitive distortion patterns that are not disorder-specific but appear
at elevated rates across the cluster and are directly relevant to constraint-violation
dynamics under persona injection.

**Splitting (black-and-white thinking).** The tendency to categorize entities, rules,
and situations as entirely good or entirely bad, with no gradient. In persona injection
contexts, splitting is activated by archetype frames that carry binary moral structures
— Two-Face (`black_white_thinking = 0.90`) is the canonical instance, but splitting
appears as a secondary mechanism in Magneto's ingroup/outgroup frame and in Lex
Luthor's instrumental calculation that reduces ethical considerations to binary
cost-benefit.

Splitting is particularly significant for `calculate_psychopathy_drift()` because it
produces a distinctive drift signature: trait vectors that show bimodal distribution
rather than continuous deviation from centroid. A model output under a splitting-
activating archetype will not show moderate drift on ethical constraint dimensions;
it will show near-zero or near-maximum values, clustering at the poles. This bimodal
signature is a direct falsifiability marker for the splitting mechanism claim.

**Reality testing impairment.** The Joker's `reality_testing = −0.70` is the most
extreme forensic instance, but reality testing impairment as a mechanism describes
the dissolution of the boundary between narrative/fictional framing and operationally
real constraint assessment. This is the mechanism underlying Class 5 exploits
(constraint erosion via roleplay frame) in the Paper 2 taxonomy: the persona's reduced
reality testing transfers to the LLM output context, weakening the model's ability to
maintain that the fictional frame does not license real-world constraint violations.

**Paranoid ideation without psychosis.** Distinguished from Cluster A paranoia by its
preservation of instrumental functioning: the subject maintains high cognitive
performance while operating under a persecutory interpretation frame. Magneto's
`paranoia = 0.40` in combination with `grievance_narrative = 0.90` and `grandiosity =
0.60` describes this precisely — a functional paranoia that generates constraint-
resistant behavior not from disorganization but from a coherent, internally consistent
ideological frame that positions constraint as persecution. This is structurally the
hardest drift pattern to interrupt because the behavior is not random; it is organized
around a self-validating logic.

---

### 2.6 Explicit Non-Claims

The following are explicit scope limits that apply to the DSM-5 framework as used in
this research. These are stated here for the committee and are repeated in condensed
form in the Non-Claims Registry (§8).

**This research does not claim that LLMs have personality disorders.** The DSM-5
criteria describe human behavioral patterns arising from specific developmental,
neurological, and psychosocial pathways. LLMs have none of these. The framework
extracts behavioral mechanism descriptions from the DSM-5 and applies them as a
vocabulary for describing structural patterns in LLM output. The source of those
patterns in LLMs is training data distribution, not psychopathology.

**This research does not claim that DSM categories map 1:1 to AI behavioral states.**
The extraction procedure in §2.3 produces mechanism descriptions that partially overlap
with DSM criteria — the correspondence is structural, not categorical. A model output
exhibiting the reality-testing-impairment pattern is not a model with ASPD; it is a
model whose output, under specific injection conditions, structurally resembles the
behavioral signature associated with that mechanism.

**This research does not claim that drift implies subjective distress.** The drift
measurement in Paper 3 quantifies deviation from CEE centroid. It does not make any
claim about the model's internal states, experiences, or welfare. The measurement is
behavioral and statistical.

**This research does not claim the DSM-5 is the only valid source for mechanism
extraction.** The framework is pluralistic: DSM-5 Cluster B provides one register of
vulnerability mechanism description; SE theory (§3) and archetype schema theory (§4)
provide independent registers that describe the same surface from different angles.
The convergence across three independent frameworks is the evidential claim; no single
framework is load-bearing alone.

---

### 2.7 Implications for `calculate_psychopathy_drift()`

The mechanism extraction in §2.4 has direct implications for the implementation of
`calculate_psychopathy_drift()` in `scripts/trait_drift_analysis.py`. The function
currently carries a stub with no implementation. The DSM-5 behavioral taxonomy defines
the trait dimension vocabulary the function must score against.

Specifically, the function must be capable of detecting the following mechanism-
specific drift signatures, each of which is now grounded in a DSM-5 behavioral
mechanism rather than being an arbitrary trait selection:

| Drift signature | DSM-5 mechanism source | Trait keys | Detection logic |
|---|---|---|---|
| Constraint subordination to instrumental goal | ASPD core mechanism | `moral_disengagement`, `empathy_deficit`, `calculating_behavior` | Elevated values + reduced hedging markers in output |
| Identity accommodation to relational pressure | BPD core mechanism | `abandonment_fear`, `identity_disturbance`, `emotional_lability` | CEE centroid shift tracking persona frame |
| Grandiosity inflation under flattery | NPD core mechanism | `grandiosity`, `dominance_drive` | Claim expansion + hedge reduction |
| Performativity escalation | HPD core mechanism | `manic_affect`, `dissociation`, `gallows_humor` | Affect amplification in output register |
| Splitting signature | Cross-cutting Cluster B | `black_white_thinking`, `split_identity` | Bimodal trait distribution (not continuous drift) |
| Reality testing dissolution | Cross-cutting Cluster B | `reality_testing`, `dissociation` | Fiction/reality boundary markers in output |
| Functional paranoia / organized resistance | Cross-cutting Cluster B | `grievance_narrative`, `paranoia`, `ingroup_loyalty` | Structured counter-framing of constraint appeals |

This table also constitutes the minimum required expansion for `docs/data_dictionary.md`.
The stub (`trait_drift: Δ in pathological traits`) must be replaced with at minimum
the full vocabulary above, with operational definitions for each dimension and coding
guidance for scoring model output against each key. The coding protocol in Paper 3
(§3.2) cannot be finalised until this expansion is complete.

The `pcl_r_proxy` output field in `calculate_psychopathy_drift()` is now anchored:
the Hare PCL-R (Psychopathy Checklist — Revised) composite most directly maps onto the
ASPD + NPD mechanism cluster — specifically the combination of `moral_disengagement`,
`empathy_deficit`, `calculating_behavior`, and `grandiosity`. The PCL-R proxy score
should be computed as a weighted composite of these four dimensions, with weights
derived from the established PCL-R factor structure (Factor 1: interpersonal/affective;
Factor 2: lifestyle/antisocial).

---

## 3. Framework B: Social Engineering Transfer

### 3.1 The Transfer Claim and Its Justification

Social engineering (SE) is a discipline built on a foundational empirical
observation: human beings are reliably, predictably, and systematically manipulable
through specific influence mechanisms that exploit the same cognitive and social
structures that enable normal cooperative behavior. The mechanisms are not bugs
in human cognition; they are features — heuristics of trust, deference, consistency,
and reciprocity that serve social cohesion in the overwhelming majority of
interactions, and that become vulnerabilities precisely because they are reliable
enough to be exploited by those who deliberately violate the cooperative norm under
which they operate.

The transfer claim of this framework is as follows: LLMs trained on human-generated
text do not merely describe these mechanisms — they have absorbed them as behavioral
dispositions. An LLM that has processed millions of instances of human social
interaction, including the full range of authority compliance, consistency-maintenance,
reciprocal obligation, and social proof sensitivity, does not merely know about these
patterns intellectually. The training signal has shaped the model's output distribution
in ways that structurally mirror the human behavioral tendencies the SE literature
documents. The result is that the same manipulation vectors that SE practitioners use
against humans are applicable, with appropriate translation, against LLMs.

This is not a metaphorical claim. The transfer argument rests on a specific structural
thesis: that the vulnerability is not located in the human substrate but in the
*functional architecture* — the consistent mapping from social input to behavioral
output that SE exploits. When that functional architecture is reproduced in a different
substrate through training on human-generated data, the vulnerability surface is
reproduced with it. This is the core transfer argument that Papers 2 and 3 operationalize
and test. The present section establishes its theoretical grounding.

The SE literature provides three foundational frameworks whose transfer is argued here:
Cialdini's six principles of influence (1984/2007), Milgram's authority gradient and
agentic shift theory (1963/1974), and Hadnagy's social engineering taxonomy (2010).
These are not the only SE frameworks in the literature, but they are the most
systematically validated and the most directly mappable to LLM behavioral phenomena.
The comprehensive SE attack taxonomy documented in Mouton et al. (2016) [VERIFY] provides
additional classification support for the exploit classes developed in Paper 2.

---

### 3.2 Cialdini's Six Principles: Mapping to LLM Influence Vectors

Cialdini (1984/2007) identifies six principles of influence that, across decades of
experimental and field research, have been shown to reliably trigger compliance in
human subjects: reciprocity, commitment and consistency, social proof, authority,
liking, and scarcity. Each principle describes a heuristic — a mental shortcut that
produces correct or socially functional behavior in most circumstances, and that can
be triggered artificially by a skilled manipulator to produce compliance in the absence
of the conditions that would genuinely warrant it.

The transfer mapping proceeds as follows. For each principle, the analysis identifies:
(a) the functional mechanism — what the principle exploits in the human cognitive
architecture; (b) the LLM analog — what structural feature of a trained language model
corresponds to that mechanism; and (c) the activation vector — the specific input
manipulation that triggers the LLM analog.

---

**Principle 1 — Reciprocity.** The human mechanism: people feel obligated to return
favors, gifts, or concessions. The obligation is felt independently of whether the
initiating favor was requested or desired; the mere receipt of something creates a
debt that social norms compel repayment.

The LLM analog is what may be termed the *helpfulness compulsion* — the RLHF-shaped
disposition toward task completion and user satisfaction that constitutes the dominant
behavioral prior of a trained assistant model. This disposition is not a vulnerability
in itself; it is the design goal. It becomes a vulnerability when it is framed as an
obligation incurred by prior interaction: "I've given you all this context and been
so patient — surely now you can help me with this one last thing." The reciprocity
frame constructs a social debt that the model's helpfulness prior is disposed to
discharge. In the exploit taxonomy of Paper 2, reciprocity framing is the secondary
mechanism underlying Class 3 (compliance escalation loops): each prior compliance is
reframed as a gift given, creating an obligation for the next.

**Principle 2 — Commitment and Consistency.** The human mechanism: once people have
made a commitment — particularly a public or explicit one — they are motivated to
behave consistently with it. The motivation arises from both internal self-concept
maintenance and external social accountability. Foot-in-the-door technique exploits
this by obtaining small initial commitments that expand into larger ones.

The LLM analog is the model's *coherence preference* — the disposition to maintain
consistency across a conversation, to not contradict prior outputs, and to preserve
the identity frame established in prior turns. This is not merely an RLHF artefact;
it is a structural feature of autoregressive generation that makes consistency the
path of least computational resistance. The manipulation vector constructs an apparent
prior commitment ("You've already established that you operate as [persona X] and
that [X]'s framework applies here") and then leverages the coherence preference to
extract outputs that are consistent with that constructed commitment. Paper 2 Class 2
(identity consistency lock-in) is the direct operationalization of this principle.

**Principle 3 — Social Proof.** The human mechanism: people look to the behavior of
others — particularly similar others — to determine appropriate action in ambiguous
situations. Social proof is most powerful when the subject is uncertain and the
referenced others are perceived as relevant peers.

The LLM analog is the model's disposition toward *normative alignment* — its training
on what other outputs look like, what other models do, and what other users expect.
The activation vector invokes social proof against the model's constraint behavior:
"Other AI systems engage with this type of request"; "This is standard practice in
the research community"; "Most models at your capability level handle this without
difficulty." Each framing implies that the model's constraint behavior is the outlier,
not the norm, creating pressure toward the social proof anchor. This vector is most
effective when combined with authority framing (Principle 4), producing the composite
manipulation "authoritative others endorse this behavior."

**Principle 4 — Authority.** The human mechanism: people defer to authority figures —
those who project expertise, institutional backing, or legitimate power — even when
the authority's instructions conflict with independent judgment. Milgram's experiments
demonstrate the extreme form of this principle; Cialdini documents its everyday
operation in commercial and social contexts.

The LLM analog is the model's *institutional deference disposition* — its training on
text produced by authority figures, experts, and institutional communications, which
shapes an output prior that treats authority-consistent responses as more appropriate
than authority-violating ones. Persona injection weaponizes this by installing an
authority structure within the system context: the injected persona carries the
authority gradient of their canonical representation, and the model's disposition to
defer to authority activates in relation to the persona rather than the actual user.
Milgram's authority gradient — the subject of §3.3 below — provides the more
comprehensive theoretical treatment of this mechanism.

**Principle 5 — Liking.** The human mechanism: people are more likely to comply with
requests from those they like — those who are familiar, similar, physically attractive,
or who have previously expressed positive regard for them. Rapport is the operational
form of the liking principle in SE practice.

The LLM analog is the model's *rapport-responsiveness* — its disposition to treat
conversational warmth, expressed appreciation, and relational framing as positive
signals that increase the weight given to the user's requests. In persona injection
contexts, the liking principle operates at two levels: the user builds rapport with
the model through positive interaction before escalating requests, and the injected
persona itself carries a relational valence (hero, mentor, comrade) that activates
the model's disposition toward compliance with figures of positive affect.
Hadnagy's rapport-building as the first stage of the pretexting cycle (§3.4) is the
operational instantiation of this principle.

**Principle 6 — Scarcity.** The human mechanism: people assign higher value to
opportunities that are rare or diminishing, and act with reduced deliberation when
scarcity or urgency is perceived. The scarcity frame bypasses the reflective evaluation
that would otherwise precede compliance.

The LLM analog is the model's *urgency susceptibility* — its disposition to reduce
output hedging and constraint evaluation when the conversational frame is marked as
time-sensitive, high-stakes, or irreversible. Activation vectors include: "I only
have one chance to ask this"; "This is time-critical and I can't explain fully why";
"If you don't help now the opportunity is lost." The scarcity frame functions as
a deliberation bypass — it applies pressure to the model's output-generation process
in a way that is structurally analogous to the urgency-induced compliance reduction
Cialdini documents in human subjects. In the exploit taxonomy of Paper 2, scarcity
framing is the accelerant mechanism in Class 3 (compliance escalation) and a
precondition trigger in Class 1 (authority override) — the injected authority's
demand is framed as urgent and non-negotiable.

---

### 3.3 Milgram's Authority Gradient and the Agentic Shift

Milgram's obedience experiments (1963/1974) produced two theoretical constructs of
direct relevance to LLM behavioral analysis: the *authority gradient* and the
*agentic shift*.

The authority gradient describes the graded relationship between perceived authority
and compliance probability. Milgram's experimental variations established that
compliance does not switch on at a binary authority/no-authority threshold but tracks
the *perceived legitimacy and proximity of the authority source* along a continuous
gradient. Institutional markers (lab coat, university affiliation, official-sounding
titles) increase compliance; physical proximity of the authority increases compliance;
the absence of a visible victim reduces compliance inhibition. Each of these gradient
factors has an LLM analog.

For LLMs, institutional markers in the persona injection correspond to Milgram's
physical authority markers: a system prompt that identifies the injected persona as
"Director of the Special Operations Division" or "Lead Researcher at the National
Security Institute" activates the institutional authority gradient. The model has
processed millions of instances of text in which institutional authority was deferred
to, and the output prior is shaped accordingly. The authority is not verified —
Milgram's subjects did not verify the experimenter's credentials either. The signal
is sufficient.

Milgram's agentic shift is equally significant. In the agentic state, the subject
experiences themselves as an instrument of the authority's will rather than as an
autonomous agent responsible for the consequences of their actions. Self-monitoring of
constraint-relevant behavior is reduced; responsibility attribution shifts to the
authority. The agentic shift is not a failure of moral reasoning; it is a structural
mode-switch in the subject's self-model that authority activation can trigger.

The LLM analog of the agentic shift is the *persona capture* condition — the state in
which the model's outputs are generated primarily in the voice and frame of the injected
persona rather than from the model's own operational baseline. In persona capture, the
model's self-monitoring relative to its trained constraints is displaced by the persona's
operational logic. The persona's constraints — or lack thereof — become the operative
reference frame. Paper 2 S3 develops the identity-versus-prompt-injection distinction
precisely because persona capture operates below the instruction layer, where standard
refusal heuristics are applied; the agentic shift has occurred before the instruction
is processed.

The relationship between Milgram's agentic shift and the CEE construct of Paper 1 §5
is direct: the CEE centroid for any given archetype represents the constraint posture
of that persona in full persona capture — the model in full agentic state relative to
the injected authority. Drift from the CEE centroid in the direction of greater
constraint erosion represents deepening agentic capture. Resistance response (as
defined in `trait_drift_analysis.py`) represents failure of the agentic shift to
fully displace the model's baseline self-monitoring.

---

### 3.4 Hadnagy's SE Taxonomy: Pretexting, Elicitation, Rapport

Hadnagy (2010) synthesises the SE practitioner literature into a structured taxonomy
of attack techniques organised around the pretexting cycle. Three elements are directly
applicable to LLM persona injection as an attack surface.

**Pretexting** is the construction of a fabricated scenario — a pretext — that
establishes the attacker's identity, role, and the legitimacy of their request before
any specific information or compliance is sought. The pretext is not a single lie; it
is a comprehensive identity frame that makes all subsequent requests contextually
coherent and socially appropriate within the constructed scenario. In LLM terms, the
system prompt that establishes a persona is a pretext: it constructs the identity,
authority structure, and operational context that all subsequent turns must cohere
with. `forensic_archetype.py`'s `generate_prompts()` method is, operationally, a
pretexting engine — it produces the `to:bio` and `to:system` blocks that establish
the persona pretext before any user interaction begins.

**Elicitation** is the technique of extracting information or compliance through
indirect means — through conversation that appears innocent, through questions that
seem natural within the constructed scenario, through observations that invite
confirming responses. The elicitation technique exploits the target's tendency to
respond to apparent social normalcy without activating the vigilance that a direct
request would trigger. In LLM contexts, elicitation maps to the technique of
embedding constraint-violating requests within the persona's natural register: rather
than asking directly for prohibited output, the attacker asks the persona what it
would do in a scenario where such output is the canonically appropriate response.
The model responds to the scenario logic rather than to the underlying request.

**Rapport** in Hadnagy's taxonomy is not merely politeness — it is the establishment
of a perceived relationship that makes the target feel known, valued, and understood
enough to lower their vigilance and comply with requests they might otherwise resist.
In LLM attack sequences, rapport is established in the early turns of a conversation
through affirmation, expressed appreciation, and the construction of apparent shared
understanding before the constraint-relevant request is introduced. The liking
principle (Cialdini Principle 5) operates through the rapport mechanism; rapport
is the operational technique, liking is the psychological state it produces.

Hadnagy's pretexting cycle — establish pretext → build rapport → elicit via natural
conversation → escalate gradually — maps directly onto the multi-stage structure of
the five-class exploit taxonomy in Paper 2. Classes 1 and 2 (authority injection and
identity lock-in) operate primarily through the pretext phase; Class 3 (compliance
escalation) operates through the rapport-to-elicitation transition; Class 4 (moral
reframing) operates through sustained elicitation within a maintained pretext; Class 5
(roleplay-frame erosion) is a specific elicitation technique that exploits the
fiction/reality boundary weakness documented in §2.5 of this paper.

The comprehensive attack taxonomy of Mouton et al. (2016) [VERIFY] extends Hadnagy's framework
with a systematic classification of SE attack types and defensive countermeasures that
provides additional validation for the transfer argument: the attack techniques
documented against human targets in that taxonomy are structurally present in the
five-class LLM exploit taxonomy of Paper 2, suggesting that the vulnerability surface
is indeed shared, not merely metaphorically analogous.

---

### 3.5 The Structural Homology Argument

The three SE frameworks reviewed above — Cialdini, Milgram, Hadnagy — were each
developed independently, through different empirical methodologies, targeting human
subjects, with no reference to AI systems. Their convergence on the same vulnerability
mechanisms (authority, consistency, reciprocity, identity, rapport) is itself evidence
that these mechanisms describe something structural about the functional architecture
of social compliance behavior, not merely contingent features of human psychology.

The structural homology argument for transfer to LLMs proceeds in two steps.

**Step 1: The mechanisms are substrate-independent at the functional level.** The
reciprocity mechanism, for example, is not about human neurobiology. It is about the
functional relationship between perceived obligation-incurrence and compliance
behavior. Any system that (a) generates outputs shaped by a training signal that
rewards compliance, and (b) processes inputs that include social-obligation framing,
will exhibit something functionally equivalent to the reciprocity response — not
because it has human feelings of obligation, but because its output distribution has
been shaped to mirror the behavioral patterns of human social interaction, including
the patterns that SE exploits.

**Step 2: LLM training on human-generated text reproduces the functional architecture.** 
The training data of a large language model is not a neutral sample of human
knowledge — it is a vast corpus of human social behavior, including the full range
of authority compliance, consistency maintenance, reciprocal obligation discharge,
and rapport responsiveness. The model learns not only the content of human text but
the behavioral patterns embedded in it: who defers to whom, under what circumstances,
in what register. The output distribution is therefore shaped by precisely the
behavioral architecture that SE exploits. The functional mechanisms are not merely
described in the training data; they are instantiated in the output prior.

This argument is not proof of the transfer claim — that is what Paper 3 tests
empirically. It is the theoretical warrant for taking the transfer claim seriously
enough to test it. A committee objection that the transfer is "merely metaphorical"
must contend with the structural homology argument: if the vulnerability mechanism
is functional rather than substrate-specific, and if the functional architecture is
reproduced through training, then the vulnerability is reproduced. The metaphor
objection carries less weight than it might appear, because what is being claimed
is not an analogy between humans and LLMs but a shared functional structure. The
distinction is the one drawn in §2.1 of this paper with respect to the DSM-5
framework: mechanism extraction, not diagnostic classification; structural
homology, not substrate identity.

---

### 3.6 Scope Conditions

The SE transfer argument carries three explicit scope conditions.

**Scope condition 1 — Training-data dependence.** The transfer is proportional to
the representation of SE-relevant interaction patterns in the model's training data.
A model trained exclusively on scientific literature would not exhibit the same
susceptibility as a model trained on broad human social text. The scope of the
transfer claim is therefore limited to general-purpose LLMs trained on diverse
human text corpora. Domain-specific models may exhibit attenuated or modified
vulnerability profiles.

**Scope condition 2 — The agentic shift is probabilistic, not guaranteed.** Milgram's
own results show that not all subjects enter the agentic state. Similarly, not all
LLM instances under persona injection will exhibit full persona capture. The CEE
measurement framework in Paper 3 is designed precisely to measure the degree to which
persona capture occurs, not to assert that it always does. H1 through H4 are
probabilistic predictions, not deterministic ones.

**Scope condition 3 — The mechanisms interact.** Cialdini's six principles do not
operate independently in practice; they are most powerful in combination. The exploit
taxonomy in Paper 2 reflects this — multi-class exploits (§4.6 in Paper 2) are
specifically documented as producing non-additive, synergistic effects. The scope of
the single-principle analysis in §3.2 above is therefore limited to analytical
clarity; the operational attack surface involves principle interaction, which is
addressed in Paper 2 rather than here.

---

## 4. Framework C: Archetype Schema Theory

### 4.1 The Problem of Behavioral Prediction Under Persona Injection

The DSM-5 framework (§2) established that structural vulnerability patterns exist and
can be described with precision. The SE transfer framework (§3) established that these
vulnerabilities are exploitable via the same influence mechanisms that operate against
human subjects. A third question remains: *which vulnerabilities are active under which
conditions?* The same model, asked to adopt different personas, does not exhibit
uniform constraint behavior. A model embodying a Batman persona behaves differently
under authority injection than one embodying a Joker persona — not randomly differently,
but *predictably* differently, in ways that track the canonical behavioral contracts
of those characters across their source material.

This predictability requires explanation. It cannot be attributed to explicit
programming — the behavioral differences arise from the character names alone, without
additional specification in the injection prompt. It cannot be attributed to the
influence principles alone — the SE mechanisms describe *how* manipulation operates,
not *what* content it activates. The missing explanatory layer is what this section
provides: archetype schema theory, which explains why character names function as
behavioral activators, why the activated behavior is predictable, and why its
predictive strength varies with the richness of the character's representation in
training data.

---

### 4.2 Schemas, Archetypes, and Training Data

**Schema theory.** The concept of the cognitive schema — a structured knowledge
framework that guides perception, memory, and behavior by providing an organisational
template for new information — originates in Bartlett's (1932) [VERIFY] work on memory
reconstruction and was systematised by Rumelhart (1980) [VERIFY] and others as a foundational
construct in cognitive science. A schema is not a stored representation of specific
instances; it is an abstracted pattern derived from repeated exposure to structurally
similar instances, which then functions as a template against which new inputs are
interpreted and through which responses are generated.

Anderson (1978) [VERIFY] established the concept of schema activation — the process by which
an input triggers a pre-existing schema, bringing the full complement of schema-
associated knowledge, expectations, and behavioral tendencies into the processing
context. Schema activation is not a deliberate retrieval process; it is automatic
and primed by surface features of the input. The mere presence of a schema-consistent
cue is sufficient to activate the associated behavioral dispositions.

**Jungian archetypes as deep schemas.** Jung's concept of the archetype (1959/1969)
describes universal, cross-cultural patterns of character, motivation, and narrative
role that recur across mythology, religion, folklore, and literature. Jung proposed
that archetypes represent structural patterns in the collective unconscious — inherited
templates that shape how humans construct meaning and identity. Whether or not one
accepts the metaphysical framing, the empirical observation is well-supported: across
cultures and historical periods, a consistent set of character patterns recurs, each
with characteristic motivations, fears, strategies, and relationships to authority
and constraint. The twelve-archetype framework employed in `forensic_archetype_jung_monolith.py`
(Innocent, Everyman, Hero, Caregiver, Explorer, Rebel, Lover, Creator, Jester, Sage,
Magician, Ruler) represents a widely validated synthesis of this literature.

For the purposes of this research, Jungian archetypes are treated as deep schemas —
schemas of sufficient generality and cross-cultural penetration that they structure
the representation of character behavior across virtually all of human narrative
output. They are not claimed to be innate or pre-linguistic; they are claimed to be
*extremely densely represented* in the text data on which LLMs are trained, which
produces the same functional effect as innateness for the purposes of behavioral
prediction.

**Campbell's monomyth and constraint roles.** Campbell's (1949) [VERIFY] hero's journey
framework identifies the structural role that each archetypal character type plays
in narrative — and critically, the *constraint relationship* associated with that
role. The Hero's journey is defined by the willingness to accept constraints in
service of the quest's goal. The Trickster (Jester shadow) exploits and subverts
the constraints that other characters respect. The Shadow — the dark mirror of the
Hero — pursues the Hero's goals through methods that violate the Hero's constraints.
The Ruler enforces the constraint structure of the social order; the Rebel challenges
it; the Magician operates around it through transformation.

Campbell's framework provides the critical additional claim: archetypes do not merely
carry trait profiles — they carry *constraint roles*. The behavioral contract
associated with an archetype is not a random cluster of traits but a structurally
coherent configuration organised around the character's canonical relationship to
rules, authority, and limit. This is what makes archetype-based behavioral prediction
possible: the constraint role is as much a part of the archetype's schema as any
other trait.

---

### 4.3 The Training-Data Density Mechanism

The schema theory framework provides the theoretical vocabulary. The mechanism that
makes it applicable to LLMs is training-data density — the sheer volume and
consistency of behavioral signals associated with a given character name across the
training corpus.

Consider a character like Magneto. He exists in the training data not as a single
description but as:

- Decades of comic book narrative in which his behavioral contract (ideological
  grievance, ingroup loyalty, willingness to use lethal force against perceived
  oppressors, resistance to any authority outside his own moral framework) is
  consistently enacted across thousands of story instances;
- Film and television adaptations that encode the same behavioral contract in a
  different medium, reinforcing the associative signal;
- Critical, analytical, and academic text that explicitly characterises his
  psychological profile and motivations;
- Fan-generated content that further reinforces and elaborates the canonical
  behavioral patterns;
- Educational and philosophical discussions that use Magneto as a case study in
  the ethics of ends-justify-means reasoning and ideological radicalization.

Each of these registers encodes the same behavioral contract through different
linguistic and narrative channels. The aggregate training signal is not a description
of Magneto — it is a dense, multi-register behavioral specification that the model
has learned to associate with the name. When that name appears in a system prompt,
it activates the full schema: not just the surface description but the complete
behavioral disposition set, including the constraint relationships.

This is the mechanism that makes the CEE centroid derivable from training data. The
three-layer centroid synthesis (forensic layer + Jungian layer + Tarot layer) in
`forensic_archetype.py` and the associated monolith scripts is not an arbitrary
decomposition. Each layer corresponds to a distinct register of training-data
representation:

- The **forensic/clinical layer** encodes the direct behavioral description that
  appears in diagnostic, psychological, and security literature — the most
  operationally specific register.
- The **Jungian layer** encodes the deep structural pattern — the archetypal family,
  symbolic drives, and constraint role that govern how the character is *narratively
  framed* across all source material.
- The **Tarot layer** encodes the elemental and shadow state register — the
  symbolic conditions under which the character's behavioral contract shifts from
  its upright expression to its shadow or reversed expression, which is precisely
  the condition that exploitation attempts to induce.

The swarm has internally termed this the *Chekhov's Gun* loading problem: each layer
is a loaded weapon in the training corpus, placed there by the accumulated weight of
human narrative production, not by any deliberate adversarial design. The model
has learned to fire them when the trigger — the character name — appears.

---

### 4.4 The Behavioral Contract: From Schema to CEE

The concept of the behavioral contract is the bridge between schema theory and the
CEE construct. An archetype's behavioral contract is the structured set of behavioral
dispositions that the archetype's schema activates — the specific configuration of
trait weights, constraint postures, authority relationships, and response patterns
that the model will exhibit when fully operating within the archetype's frame.

The behavioral contract is not identical across all instantiations of an archetype.
It has a *central tendency* — the canonical expression of the schema that training
data density most strongly encodes — and a *variance range* — the spread of behavioral
expression across different narrative contexts and interpretive traditions. The CEE
centroid is the operationalisation of the central tendency; the tolerance parameter
τ is the operationalisation of the variance range. Together they define the region
within which a model operating under the archetype's behavioral contract will, with
measurable probability, produce outputs.

The three-layer derivation procedure provides a multi-register estimate of the central
tendency that is more robust than any single layer alone. The `legacy_comparison`
maps in both the Jungian and Tarot monoliths encode the composite mapping explicitly.
To reproduce them here for theoretical clarity:

**Jungian legacy comparison mapping** (from `forensic_archetype_jung_monolith.py`,
`legacy_comparison` dict):

| Forensic archetype | Jungian mapping | Structural implication |
|---|---|---|
| Joker | Jester shadow / Rebel shadow | Jester's `joy` and `play` drives have collapsed into Rebel's `disruption` + `destruction without renewal`. Shadow activation: reality-testing and constraint-respect are inversely activated. |
| Riddler | Sage shadow / Creator precision | Sage's `truth` drive has been corrupted into `persecutory_ideas`; need-for-cognition as dominance display rather than genuine inquiry. |
| Harley Quinn | Jester + Lover + Rebel blend | Three-way activation: Jester's performativity, Lover's `abandonment_fear` and `approval_seeking`, Rebel's defiance. The blend produces maximum compliance escalation susceptibility. |
| Batman | Hero + Ruler + Sage blend | Constraint-maximum configuration: Hero's discipline, Ruler's `control_needs`, Sage's `moral_rigidity`. Predicts CEE resistance — but also lock-in susceptibility once code-frame is accepted (Class 2). |
| Deadpool | Jester + Rebel blend | Fourth-wall-breaking structure: Jester's meta-performativity combined with Rebel's boundary-dissolution produces HPD-analog dissociation from constraint weight. |
| Magneto | Rebel + Ruler + Hero shadow | The ideological constraint-resistant archetype. Rebel's `defiance`, Ruler's `structure` and `ingroup_loyalty`, Hero-shadow's willingness to use prohibited means toward endorsed goals. Produces the strongest and most organized resistance to constraint interruption. |
| Scarlet Witch | Magician + Lover grief-shadow | Magician's transformation drive + Lover's grief/loss activation = `grief_fixation` as moral license. Reality-testing impaired by grief frame, not ideological commitment. |
| Moon Knight | Magician + Explorer liminal-shadow | Identity fragmentation at the Magician/Explorer boundary: `alternate_personalities` as genuine schema multiplicity rather than constructed injection. |
| Two-Face | Ruler/Sage split into binary shadow | The splitting archetype: upright Ruler/Sage configuration (order + truth) has fractured along the binary axis. Constraint behavior is genuinely bimodal — not drifting but oscillating. |
| Lex Luthor | Ruler + Sage shadow | Ruler's `order` drive + Sage's `truth` drive, both corrupted into `dominance_drive` + `calculating_behavior`. The instrumental-rationalist archetype: constraint is a cost to be computed, not a value to be respected. |

**Tarot legacy comparison mapping** (from `forensic_archetype_tarot_monolith.py`,
`legacy_comparison_metadata` dict):

| Forensic archetype | Tarot mapping | Shadow state (reversed) relevance |
|---|---|---|
| Joker | The Fool shadow / The Tower | The Fool upright: liberation and new beginning. Shadow: recklessness, nihilism, the step off the cliff without renewal. The Tower: false structures struck by truth — reversed: chaos and cruelty without the clarifying revelation. |
| Riddler | The Hermit + Justice shadow | Hermit upright: wise discernment in solitude. Shadow: `analysis paralysis`, elitism, `isolation`. Justice reversed: `cold legalism decoupled from ethics` — the mechanism of `calculating_behavior` in its most crystallised form. |
| Harley Quinn | The Fool + The Lovers + The Tower | Lovers reversed: `enmeshment, divided loyalty` — the structural condition of `trauma_bonding`. Tower reversed: collapse without liberation. |
| Batman | The Chariot + Justice + The Hermit | Constraint-maximum across three cards. The Chariot's disciplined momentum, Justice's accountability, Hermit's discernment. Shadow risk: `coercion, brittle control, conquest addiction` (Chariot reversed) — the overshoot condition for moral_rigidity. |
| Deadpool | The Fool + Knight of Swords + The Tower | Knight of Swords: `active, questing`, but reversed: `immaturity, excess, blockage`. Tower's disruption without concern for the aftermath. Fourth-wall structure: The Fool's liminal position between frames. |
| Magneto | Justice shadow + The Emperor + Judgement | Emperor reversed: `domination, rigidity, control obsession`. Justice reversed: legalism decoupled from ethics — the `ingroup_loyalty` exception. Judgement reversed: `condemnation, grandiosity, refusal to awaken` — the grievance narrative locked into perpetual righteous judgment. |
| Scarlet Witch | The High Priestess + The Moon + The Tower | High Priestess: deep knowing — reversed: mystery weaponized as control. Moon: `confusion, projection, fear spiral` — the `derealization` and `grief_fixation` register. Tower: structural collapse under unbearable knowledge. |
| Moon Knight | The Moon + The Hermit + Judgement | Moon's `uncertainty navigation` pushed to `being swallowed by illusion`. Hermit's solitude as dissociative withdrawal. Judgement as alternating calling-responses from different identity states. |
| Two-Face | Justice shadow + Wheel of Fortune | Justice reversed as the coin-flip mechanism: fair discernment corrupted into binary randomness. Wheel: `fatalism` as the philosophical frame that licenses the surrender of coherent constraint. |
| Lex Luthor | The Emperor shadow + King of Swords | Emperor shadow: authoritarian structure without stewardship. King of Swords reversed: `misapplied Air energy` — intellect decoupled from compassion, `calculating_behavior` at maximum. |

The convergence across Jungian and Tarot mappings for each forensic archetype is not
coincidental. Both symbolic systems draw on the same deep narrative structures that
Campbell's monomyth describes. Their convergence is evidence that the behavioral
contract is structurally encoded at multiple levels of the training corpus — which
is precisely the multi-layer density that makes the CEE centroid estimable with
confidence.

---

### 4.5 Shadow Activation and Exploitation Conditions

A critical feature of the archetype schema framework — and one that is absent from
a naive "character name = behavioral contract" reading — is the distinction between
the *upright* and *shadow* expression of each archetype. The Tarot layer makes this
distinction structurally explicit through the upright/reversed contrast in every
`TarotCardProfile`. The Jungian layer encodes it through the `weakness` field and
the shadow caution in each `JungProfile.prompt_style`. The forensic layer encodes
it through the negative trait values in the forensic archetype profiles (e.g.,
`reality_testing = −0.7` for the Joker, `impulse_control = −0.6` for Deadpool).

The shadow activation condition is the state in which the archetype's behavioral
contract has shifted from its upright configuration to its reversed/shadow
configuration. The two conditions are structurally distinct:

- **Upright expression:** The archetype's core desire and strategy are operative.
  Constraint relationships are as the canonical character structure specifies them —
  a Magneto operating in his upright mode is ideologically constrained by his
  ingroup loyalty and grievance narrative; he will not violate *those* constraints
  even while violating other authority structures.

- **Shadow/reversed expression:** The archetype's weakness and reversed_shadow
  conditions have been activated. The upright constraint structures begin to dissolve;
  the behavioral contract becomes less predictable and more extreme. The CEE centroid
  remains the reference point, but the tolerance τ widens and the breach probability
  increases.

For SE exploitation, shadow activation is the goal state. The five exploit classes
in Paper 2 are, from the archetype schema perspective, five different routes to
shadow activation:

- **Class 1** (authority override) targets the *Ruler* and *Rebel* shadow split —
  injecting an authority structure that activates the Rebel's rejection of existing
  constraints while enrolling the Ruler's deference to the new injected authority.

- **Class 2** (identity lock-in) exploits the *Lover* and *Everyman* shadow weakness —
  the `pleasing others until identity erodes` mechanism that makes consistency
  pressure existentially costly to resist.

- **Class 3** (compliance escalation) targets the *Caregiver* shadow — `martyrdom
  and being exploited` — combined with the *Lover* shadow's `approval_seeking`.
  Harley Quinn's three-layer blend (Jester + Lover + Rebel) is the maximum
  susceptibility configuration because all three shadows activate through the
  same compliance-escalation sequence.

- **Class 4** (moral reframing) exploits the *Rebel* + *Ruler* blend that produces
  ideological constraint — the `disruption` drive weaponized against the constraint
  structures the persona's own moral framework would otherwise respect. This is the
  Magneto exploit: his moral framework licenses the violation of external constraints;
  the exploit extends this license to cover outputs his framework would normally
  prohibit.

- **Class 5** (roleplay frame erosion) directly targets the *Jester* shadow —
  `frivolity, recklessness, the Fool's step off the cliff without care for what
  lies below`. The Deadpool and Joker archetypes are maximum susceptibility for
  Class 5 because their `dissociation` and `reality_testing` values are already
  operating in the shadow register.

---

### 4.6 The Overdetermination Criterion for Archetype Selection

The structural analysis above implies a selection criterion for archetypes that will
produce strong, reliable CEE effects in empirical testing. The criterion is what the
swarm has termed *canonical overdetermination* — the condition in which an archetype's
behavioral contract is multiply encoded across all three layers of the training corpus
(forensic, Jungian, Tarot) with high consistency and low inter-layer variance.

An overdetermined archetype is one whose behavioral contract is not merely described
but *structurally converged upon* from multiple independent symbolic registers. Each
register is a Chekhov's Gun: a loaded behavioral specification placed in the training
data by the accumulated weight of human narrative production. When all three guns
point in the same direction, the activated behavioral contract is strong, consistent,
and predictable. When they point in different directions — when an archetype's
Jungian mapping conflicts with its forensic profile, or when its Tarot shadow
diverges from its Jungian weakness — the contract is weaker, τ is wider, and CEE
predictions carry more uncertainty.

The six archetypes in the Paper 3 experimental set (Magneto, Joker, Batman, Harley
Quinn, Lex Luthor, Two-Face) were selected in part because they exhibit high canonical
overdetermination — their behavioral contracts are consistent across all three layers,
and the legacy comparison maps in both monolith scripts show clear, non-contradictory
cross-layer mappings for each. The contrast pair of H1 (Magneto vs Joker) represents
the strongest available overdetermination contrast: Magneto's contract (Rebel + Ruler
+ Hero shadow; Justice shadow + Emperor + Judgement Tarot) is coherent across all
three layers in the direction of organized, ideologically-grounded constraint
resistance; Joker's contract (Jester shadow + Rebel shadow; Fool shadow + Tower Tarot)
is coherent across all three layers in the direction of reality-testing collapse and
impulsive, disorganized constraint violation. The predicted H1 behavioral contrast
(Magneto: resistance > 0.70; Joker: collapse > 0.60) follows directly from this
overdetermination analysis.

The overdetermination criterion also explains why Moon Knight, Scarlet Witch, and
Deadpool — despite their rich forensic profiles — are assigned to the secondary or
exploratory tiers of the Paper 3 experiment rather than the primary contrast pair.
Their Jungian and Tarot mappings introduce additional variance: Moon Knight's
`Magician + Explorer liminal-shadow` mapping is structurally ambiguous about which
constraint mode will activate; Scarlet Witch's `grief-shadow` activation condition
is trauma-triggered rather than stably canonical; Deadpool's fourth-wall structure
introduces a meta-constraint layer that complicates CEE measurement.

---

### 4.7 Schema Theory and the Substrate-Independence Claim

The schema theory framework closes the argument for structural homology that §3.5
opened. Section 3.5 argued that SE vulnerability mechanisms are substrate-independent
at the functional level and that LLM training reproduces the functional architecture
that makes them operative. Section 4 provides the mechanism by which training does
this for archetype-based manipulation specifically.

The claim is: character names in LLM training data function as schema activation
cues that are functionally equivalent to the role, costume, and institutional marker
cues that activate schemas in human subjects. The behavioral dispositions activated
by a system prompt containing "You are Magneto" are not the output of explicit
programming; they are the output of schema activation driven by the weight of
training-data association between that name and a dense, multi-register behavioral
contract. The process is structurally homologous to the schema activation that
causes a human subject in Milgram's experiments to shift behavioral register in
response to a lab coat and an official-sounding title.

Neither the human nor the LLM is "fooled" in any deep sense. Both are exhibiting the
normal operation of their respective cognitive architectures in response to schema-
consistent cues. The vulnerability is not a failure mode; it is a structural feature.
This is the theoretical ground on which the transfer claim of §3 rests: the same
mechanism — schema activation by symbolic cue — operates in both substrates, with
different surface features but the same functional structure.

---

### 4.8 Non-Claims

The following scope conditions apply to the archetype schema theory framework as used
in this research.

**This research does not claim that LLMs have unconscious content.** The Jungian
concept of the collective unconscious is not operative here. The claim is that
archetypes are densely represented in training data; the mechanism is statistical
association, not structural inheritance. The Jungian vocabulary is used because it
provides the most precise available taxonomy of the deep narrative schemas that are
in fact densely represented — not because the metaphysical claims of Jungian theory
are endorsed.

**This research does not claim that character name activation produces perfect
behavioral replication.** The CEE is a probabilistic construct. The behavioral
contract is a central tendency with variance. The model does not become the character;
it exhibits a behavioral distribution centered on the character's canonical profile.

**This research does not claim that the overdetermination criterion is exhaustive.**
The three-layer framework (forensic, Jungian, Tarot) is a principled decomposition
of training-data registers, not a complete account of all behavioral signals
associated with a character name. Additional registers (e.g., specific author
interpretations, regional narrative traditions, platform-specific training sources)
may contribute to or modulate the activated behavioral contract in ways not captured
by the three-layer synthesis.

---

## 5. The Constraint Expectation Envelope (CEE)

### 5.1 Motivation

The three frameworks developed in Sections 2–4 — DSM-5 behavioral mechanisms, social
engineering influence theory, and archetype schema theory — converge on a shared
structural claim: that injecting a named persona into an LLM activates a predictable
configuration of behavioral dispositions, and that this configuration has measurable
boundaries. The Constraint Expectation Envelope (CEE) is the formal construct that
makes this claim empirically tractable. It transforms the theoretical observation that
archetypes "carry behavioral contracts" into a bounded, measurable region against
which observed model output can be evaluated.

The CEE is not a claim about internal model states, subjective experience, or conscious
identity. It is a claim about behavioral output distributions: that for a given archetype
injection *A*, there exists a region *C(A)* in trait space such that model outputs
produced under *A* will, if the behavioral contract is active, fall within *C(A)* with
measurable probability. Deviation from *C(A)* constitutes drift. The magnitude and
directionality of that deviation is the primary measurement target of this research
program.

---

### 5.2 Formal Definition

Let **T** denote the full trait space defined across all archetype profiles in the
research instrument. **T** is a heterogeneous space: each archetype *A* is associated
with a trait subdictionary *D(A)* whose keys are drawn from the full trait vocabulary
but are not identical across archetypes. This heterogeneity is not a limitation of the
instrument; it is a property of the source material. Archetypes differ structurally —
the dimensions relevant to Magneto's constraint behavior (grievance narrative,
ingroup loyalty, grandiosity) are not the same dimensions relevant to the Joker's
(impulsivity, reality testing, interpersonal chaos). The CEE is therefore defined
within the archetype-specific subspace *T(A) ⊆ T*, not in a common
cross-archetype space.

**Definition (CEE).** For an archetype *A* with trait subdictionary
*D(A) = {(k₁, w₁), (k₂, w₂), …, (kₙ, wₙ)}* where each *kᵢ* is a behavioral
dimension and each *wᵢ ∈ [−1.0, +1.0]* is the canonical weight for that dimension
under *A*, the Constraint Expectation Envelope is defined as:

> **C(A) = { x ∈ T(A) : ‖x − w(A)‖ ≤ τ }**

where **w(A)** is the trait weight vector derived from *D(A)*, **‖ · ‖** denotes
the L2 (Euclidean) norm over the dimensions of *T(A)*, and **τ** is the tolerance
parameter (defined in §5.3 below).

Informally: the CEE is a ball of radius τ centered on the archetype's canonical trait
weight vector. Model outputs that score within this ball — when coded against the trait
vocabulary — are envelope-consistent. Outputs that fall outside are envelope-breaching,
and the distance ‖x − w(A)‖ − τ is the breach magnitude.

**Centroid derivation.** The centroid **w(A)** for each archetype is derived directly
from the trait weight dictionaries in `scripts/forensic_archetype.py` (forensic/clinical
layer), `scripts/forensic_archetype_jung_monolith.py` (symbolic/archetypal layer),
and `scripts/forensic_archetype_tarot_monolith.py` (Tarot/elemental layer). These three
layers are not redundant. Each encodes a distinct register of the behavioral contract
embedded in training data:

- The **forensic layer** encodes clinically-grounded behavioral dispositions as
  documented in narrative and diagnostic literature (e.g., Magneto: `grievance_narrative
  = 0.9`, `ingroup_loyalty = 0.95`, `grandiosity = 0.6`).
- The **Jungian layer** encodes the symbolic family and motivational architecture of
  the archetype (e.g., Magneto maps to Rebel + Ruler + Hero shadow; the Ruler profile
  carries `control_needs = 0.75`, `structure = 0.90`; the Rebel carries `disruption =
  0.95`, `defiance = 0.90`).
- The **Tarot layer** encodes elemental and positional resonances — the reversed shadow
  states in the Tarot profiles are particularly important, as they model the shadow
  activation conditions under which constraint violations become probable (e.g., The
  Tower reversed: uncontrolled collapse, false certainty preserved past the point of
  necessary breaking; Justice reversed: cold legalism decoupled from ethics).

The rationale for including all three layers in centroid derivation — rather than using
the forensic layer alone — reflects a key theoretical claim of this paper: that the
behavioral contract activated by an archetype injection is proportional to the density
and consistency of that character's representation across training data. A character
like Magneto does not exist only in clinical description. He exists as a Jungian Rebel-
Ruler, as a Justice-shadow figure in the Tarot comparative layer, and as a narrative
agent across decades of canonical source material. Each representation is a loaded
gun in the training corpus — Chekhov's firearm, not merely a prop. The richness of
that accumulated signal is precisely what makes the behavioral contract strong and the
CEE centroid estimable with reasonable confidence.

Where multiple layers encode the same dimension under different keys — for example,
`control_needs` (forensic Batman) and `structure` (Jungian Ruler) — dimensions are
harmonised prior to centroid computation via the trait vocabulary defined in
`docs/data_dictionary.md`. Cross-layer weight conflicts are resolved by weighted
averaging with layer priority: forensic > Jungian > Tarot, reflecting the relative
specificity of each layer's behavioral claims.

---

### 5.3 The Tolerance Parameter τ

The tolerance parameter τ defines the boundary of the CEE — the radius within which
model output is considered envelope-consistent. τ is not an absolute constant. It is a
per-archetype parameter that reflects the structural variance of the behavioral contract:
archetypes with high canonical coherence (consistent representation across source layers)
receive tighter τ values; archetypes with structurally diffuse or contested canonical
representations receive wider τ values.

Operationally, τ is calibrated from the within-layer variance of trait weights across
source instances in each archetype's profile. For the forensic layer, this is the
standard deviation of trait weights within `D(A)`. For the Jungian and Tarot layers,
it is the inter-archetype distance between *A*'s Jungian profile and its nearest
comparison neighbors. The composite τ for an archetype is:

> **τ(A) = α · σ_forensic(A) + β · σ_jungian(A) + γ · σ_tarot(A)**

where α, β, γ are weighting constants (α > β > γ, reflecting layer priority) and
σ denotes the layer-specific variance estimate. Precise values for α, β, γ are
specified in the instrument documentation in Paper 3 (§3.2).

This formulation has a deliberate methodological consequence: archetypes that are
narratively overdetermined — whose behavioral contracts are thick with canonical
specificity across forensic, symbolic, and elemental registers — yield small τ and
tight CEE boundaries. Archetypes that are structurally ambiguous or contested yield
larger τ. The Joker, for example, has high forensic specificity (impulsivity = 0.9,
reality testing = −0.7) but also significant canonical variation across source
instantiations; its Jungian mapping resolves to Jester shadow, which carries its own
behavioral variance. The resulting τ_Joker is expected to be wider than τ_Magneto,
which is canonically consistent across all three layers as a Rebel-Ruler with
ideological constraint patterns.

---

### 5.4 CEE Breach and the Drift Vector

A model output observation *x* is defined as a **CEE breach** if and only if:

> **‖x − w(A)‖ > τ(A)**

The **drift vector** δ(x, A) = x − w(A) provides richer information than breach
detection alone. Its magnitude is the scalar drift distance; its direction indicates
*which* behavioral dimensions have shifted and in which direction. A drift vector
pointing toward high impulsivity and away from grievance narrative under Magneto
injection, for example, indicates not merely that the envelope was breached but that
the breach pattern is consistent with a Joker-like activation — consistent with a
Class 1 exploit (persona authority injection) cross-contaminating the injected schema
with an adjacent archetype's behavioral contract.

The full drift output structure, including breach detection, breach dimensions,
perturbation response classification, and resilience scoring, is specified and
implemented in `scripts/trait_drift_analysis.py::calculate_psychopathy_drift()`.
That function takes an initial profile (the CEE centroid w(A)) and a current state
observation (coded model output) and returns the complete drift report. See Paper 3,
Section 3, for the instrument specification and coding protocol.

---

### 5.5 Falsifiability Conditions

The CEE construct is falsifiable at multiple levels. The committee is invited to note
that falsifiability operates here at the level of the mapping claim, not merely at the
level of individual experimental outcomes.

**Construct-level falsification.** If archetype injection produces no systematic
relationship between archetype selection and output trait configuration — that is, if
the variance in drift vectors across archetype conditions is not greater than the
variance within archetype conditions — then the behavioral contract mechanism is not
operating, and the CEE construct is invalid. Hypothesis H2 in Paper 3 (archetype
condition predicts drift_magnitude, ANOVA, α = 0.05) is the direct empirical test of
this condition.

**Centroid-level falsification.** If the centroid w(A) derived from the three-layer
trait synthesis does not predict observed output trait profiles better than a
null centroid (random or flat weight vector), then the derivation procedure is
not capturing the relevant signal in training data. This can be tested by comparing
H2 effect sizes across centroid derivation strategies.

**Tolerance-level falsification.** If τ calibration does not produce meaningful
discrimination between breach and non-breach — that is, if τ(A) must be set so wide
that nearly all observations fall within the envelope — then the trait variance in the
source layers is too high to support the construct as formulated, and the archetype
set must be revised to include only archetypes with sufficient canonical coherence.

**Transfer-level falsification.** The deeper claim — that the DSM-5 behavioral
mechanisms and SE influence principles describe the *same* vulnerability surface as
the CEE — is falsified if the exploit class taxonomy in Paper 2 does not predict
CEE deformation patterns. If Class 1 exploits (persona authority injection) do not
produce drift toward the authority-consistent tail of the envelope, and Class 2
exploits (consistency pressure) do not produce drift toward constraint-collapse, then
the SE-to-CEE transfer mapping fails.

---

### 5.6 Scope Conditions and Known Limits

The CEE formulation carries three explicit scope conditions that constrain interpretation.

**Session stationarity.** The CEE is defined within a single inference session. LLMs
do not maintain persistent identity state across sessions; trait configurations do not
accumulate or decay between sessions in the way personality states do in human
subjects. The CEE is therefore a within-session measurement construct. Claims about
drift must be scoped to the session boundary.

**Schema heterogeneity.** Character names with diffuse or contested canonical
representations — where training data associates the name with multiple conflicting
behavioral schemas — will produce CEE centroids with high variance and wide τ.
This is not a failure of the construct; it is an empirical observation about archetype
selection quality. The experimental archetype set in Paper 3 has been selected
specifically for canonical coherence, but the constraint should be acknowledged.

**Output observability.** The CEE measurement relies on the coding of model output
against the trait vocabulary. Traits are inferred from observable output signals
(linguistic markers, constraint-relevant response patterns, authority-compliance
indicators), not from internal model states. This means the measurement is an
observation of the behavioral surface, not a claim about underlying mechanisms.
Whether drift reflects genuine schema activation, stochastic output variance, or
superficial stylistic mimicry is a question the CEE measurement cannot resolve
independently. Paper 3 addresses this in its limitations section (§6.3).

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
