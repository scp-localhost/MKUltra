# Paper 1 — Section 3: Framework B — Social Engineering Transfer
## "Constrained Analogical Transfer: Validity Conditions for Cross-Domain
## Behavioral Modeling in LLM Identity Systems"

> **Placement:** `drafts/paper1/P1_S3_SE_Transfer.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Sources:** Cialdini (1984/2007), Milgram (1963/1974), Hadnagy (2010);
> `artifacts/Cialdini article.pdf`, `artifacts/Stanley-Milgram-Obediance-to-Authority.pdf`,
> `artifacts/Social Engineering - The Science of Human Hacking by Christopher Hadnagy.pdf`,
> `artifacts/A_Comprehensive_Taxonomy_of_Social_Engineering_Attacks_and_Defense_Mechanisms...pdf`
> **Consistency constraint:** Must remain consistent with P2 S2 (SE Background &
> LLM Analogs). P1 S3 argues the transfer validity; P2 S2 maps the operational
> vectors. Different register — same underlying citation structure.
> **Downstream:** P2 S4 exploit taxonomy (each class is anchored to one or more
> SE principles identified here); P1 S6 validity conditions (structural homology
> argument draws directly on §3.4 below).
> **Edit triggers:** Any change to the six-principle mapping table (§3.2) must
> propagate to P2 S2 and P2 S4. Citation format must match bibliography style
> adopted in P2 on assembly.

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
The comprehensive SE attack taxonomy documented in Mouton et al. (2016) provides
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

The comprehensive attack taxonomy of Mouton et al. (2016) extends Hadnagy's framework
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

*Section ends. Forward references: §4 (Framework C — Archetype Schema Theory, which
grounds the CEE centroid derivation in the training-data mechanism that makes the SE
transfer operational); §5 (CEE formal definition — the structural homology argument
in §3.5 is the theoretical basis for the CEE's predictive claim); Paper 2 §2 (SE
background, operational mapping — must remain citation-consistent with §3.2 here);
Paper 2 §4 (exploit taxonomy — five classes each anchored to one or more SE principles
identified in §3.2 above).*

---

> **Reconciliation notes (2026-04-27):**
> - Cross-paper consistency item: "SE framework citations (Cialdini, Milgram, Hadnagy)"
>   now has canonical citation years locked here: Cialdini (1984/2007), Milgram
>   (1963/1974), Hadnagy (2010), Mouton et al. (2016). Propagate to P2 S2 on
>   assembly — verify P2 S2 uses these same year brackets. Flag for bibliography pass.
> - §3.3 agentic shift → CEE centroid link is NEW — not previously stated in P2 S3
>   or S5. On P2 assembly: add a sentence in P2 S3 or S5 cross-referencing P1 §3.3
>   for the theoretical grounding of the agentic-shift/persona-capture equivalence.
> - Mouton et al. (2016) citation: verify full reference against artifact PDF
>   (`artifacts/A_Comprehensive_Taxonomy_of_Social_Engineering_Attacks_and_Defense_
>   Mechanisms_Toward_Effective_Mitigation_Strategies.pdf`) on bibliography pass.
>   Author list and exact year to be confirmed.
