---

## Abstract

Social engineering is a discipline of human vulnerability exploitation, documented across five decades of psychological and security research as the primary attack surface against which technical defenses consistently fail. Large language models are trained on human-generated text at scale. This paper argues that a structural consequence of that training is the inheritance of human vulnerability profiles — specifically, the cognitive and behavioral regularities that social engineering frameworks exploit — and that archetype-based identity injection constitutes a reproducible social engineering attack against LLM constraint behavior.

We present three contributions. First, we demonstrate the structural transfer of three canonical social engineering frameworks — Cialdini's influence principles (1984/2007), Milgram's authority gradient experiments (1963/1974), and Hadnagy's operational social engineering taxonomy (2010) — to the LLM identity injection attack surface, arguing that LLMs reproduce the statistical structure of human decision heuristics rather than merely simulating them, and therefore inherit the vulnerability profiles those heuristics create. Second, we distinguish identity injection from prompt injection as structurally distinct attack classes operating at different computational layers — the schema layer versus the instruction layer — with different mechanisms, different scopes, different failure modes, and different defensive requirements. Third, we formalize a five-class exploit taxonomy — Authority Override Injection, Identity Consistency Lock-in, Compliance Escalation Loops, Moral Reframing Drift, and Constraint Erosion via Roleplay — with full mechanism specification, validated human SE analogs, LLM-specific attack vectors, archetype behavioral data, and detection signatures for each class.

The measurement construct that makes the taxonomy falsifiable is the Constraint Expectation Envelope (CEE): the bounded region of constraint behavior predictably associated with a given injected persona, derived from the forensic archetype profiling instrument described herein. A CEE breach operationally defines a successful exploit execution. Empirical validation of CEE predictions across a six-archetype experimental set is reported in the companion paper (Paper 3). The theoretical validity conditions for the cross-domain mapping are established in Paper 1.

This paper is explicitly dual-use. It is framed as a defensive contribution: the taxonomy is intended to enable detection system design, alignment-aware persona specification, and behavioral drift monitoring. Current RLHF and Constitutional AI alignment approaches operate at the instruction layer and do not address the schema-layer attack surface this taxonomy describes. The taxonomy is presented as a first-generation, extensible framework — not a closed enumeration — with the expectation that it will be refined as empirical evidence accumulates and novel injection strategies are documented.

*Keywords: large language model security, social engineering, identity injection, persona injection, behavioral drift, alignment, constraint expectation envelope, adversarial prompting*

---

## Section 1: Introduction

### 1.1 The Transfer Problem

Social engineering is not a technical attack. It is a behavioral one. Its power derives from a structural feature of human cognition: that the same mental shortcuts which make social interaction efficient, fluid, and low-cost also make humans reliably manipulable by actors who understand the structure of those shortcuts and deploy them deliberately. Cialdini (1984) documented six influence principles — reciprocity, commitment and consistency, social proof, authority, liking, and scarcity — that operate as near-automatic compliance triggers across populations and contexts. Milgram (1963, 1974) demonstrated that deference to authority is not an aberration of weak-willed individuals but a default mode of human social cognition, active at compliance rates that repeatedly surprised both experimenters and subjects. Hadnagy (2010) synthesized this literature into an operational attack methodology — pretexting, elicitation, rapport — applicable to any human target embedded in an organizational context. The shared insight across all three frameworks is that human vulnerability is not a bug in the cognitive architecture; it is a feature that has been exploited so consistently and so successfully that it has generated a dedicated adversarial discipline.

The question this paper addresses is whether that vulnerability transfers. Not metaphorically — not in the sense that LLMs are "like" humans in ways that invite loose analogical comparison — but structurally: whether the same mechanisms that Cialdini, Milgram, and Hadnagy documented in human subjects appear in LLM behavior under persona injection in a form that is mechanistically isomorphic, operationally exploitable, and measurably distinct from the baseline alignment behavior the models were trained to exhibit.

The argument for transfer is not intuitive but it is precise. LLMs are trained on human-generated text. Human-generated text encodes, at scale, the statistical regularities of human cognition — including the decision heuristics, authority response patterns, consistency preferences, and narrative compliance dynamics that social engineering exploits. A model trained to predict the next token in human text does not learn about these regularities abstractly. It learns to *reproduce* their statistical structure. The model does not simulate the agentic shift Milgram's subjects experienced; it reproduces the statistical signature of how humans who have experienced the agentic shift generate text. That reproduction is, functionally, the vulnerability.

### 1.2 The Gap in Current Literature

The adversarial ML literature has documented prompt injection attacks extensively — instruction override, indirect injection via retrieved content, chain-of-thought hijacking, jailbreak sequences targeting the instruction layer (Perez & Ribeiro, 2022; Greshake et al., 2023; Willison, 2022; Wei et al., 2023). This is a mature and productive research strand. It is not the research strand this paper extends.

The social engineering literature — Cialdini, Milgram, Hadnagy, and their successors — has not been systematically applied to LLM identity or persona manipulation. There exists a body of work on roleplay-based jailbreaks (AIM, DAN, and their descendants) that observes the phenomenon without the theoretical apparatus to explain or classify it. There exists a body of work on persona-based behavioral modification in LLMs that treats persona injection as a feature rather than an attack surface. There is no prior work that applies the full social engineering theoretical apparatus — influence principles, authority gradient, pretexting taxonomy — to the structural analysis of how identity injection exploits LLM behavioral schemas.

This paper closes that gap. Its contribution is the mapping and the taxonomy that the mapping generates. The gap is not empirical — the phenomena have been observed — it is theoretical. The field lacks a framework precise enough to predict, classify, and detect identity injection exploits as a coherent attack class. The five-class taxonomy is that framework.

### 1.3 Identity Injection Is Not Prompt Injection

A technically literate reader will ask whether this paper's contribution is substantive or terminological — whether identity injection is prompt injection with a more elaborate theoretical apparatus attached. Section 3 addresses this objection in full. The short answer is structural: prompt injection is an instruction-layer attack targeting the model's directive-processing machinery; identity injection is a schema-layer attack targeting behavioral priors encoded in training data. The two classes have different mechanisms, different scopes (local vs. session-persistent), different failure modes (instruction conflict vs. behavioral coherence with a wrong prior), and different defensive requirements. The distinction is not terminological. It has direct consequences for detection architecture and alignment design that the instruction-layer framing misses entirely.

### 1.4 Contributions of This Paper

This paper makes three contributions to the AI safety and adversarial ML literature.

**Contribution 1 — SE transfer argument.** A structured demonstration that Cialdini's influence principles, Milgram's authority gradient, and Hadnagy's SE operational taxonomy transfer structurally to the LLM identity injection attack surface, with explicit specification of the transfer mechanism (training data statistical encoding of human decision heuristics) and its scope conditions.

**Contribution 2 — Structural distinction.** A five-axis comparison of identity injection and prompt injection establishing that they are structurally distinct attack classes operating at different computational layers, with different mechanisms, scopes, failure modes, and defensive requirements. This distinction is the precondition for correct threat modeling of identity injection attacks.

**Contribution 3 — Five-class exploit taxonomy.** A formally specified, falsifiable taxonomy of five identity injection exploit classes, each with full mechanism, human SE analog with citation, LLM attack vector, archetype behavioral data, and detection signatures. The taxonomy is grounded in the Constraint Expectation Envelope (CEE) measurement construct that makes each class's predictions testable and each successful exploit operationally definable.

### 1.5 Paper Structure

Section 2 establishes the human SE theoretical background and maps each framework to its LLM analog. Section 3 distinguishes identity injection from prompt injection across five structural axes. Section 4 presents the five-class exploit taxonomy in full. Section 5 defines the CEE measurement construct and derives it from the archetype profiling instrument. Section 6 draws alignment implications and proposes three targeted mitigations. Section 7 addresses ethical reflexivity. Section 8 specifies limitations. Section 9 concludes. Forward references to Paper 1 (theoretical validity conditions for the cross-domain mapping) and Paper 3 (empirical CEE measurement and hypothesis testing) appear throughout.

---

## Section 2: Background — Human Social Engineering Frameworks and Their LLM Analogs

### 2.0 Why This Background Is Load-Bearing

Section 2 is not a literature review. It is the argument's foundation. The claim that SE frameworks transfer to LLM identity injection depends entirely on whether the structural features of those frameworks — the specific mechanisms by which they produce compliance in human targets — are present in LLM behavior under persona injection. This section establishes what those structural features are, with sufficient precision that Section 4's exploit taxonomy can cite them directly as validated analogs. Every exploit class in Section 4 has a named SE mechanism from this section as its human-side structural anchor. If those anchors are not established here, the taxonomy floats.

### 2.1 Cialdini: The Influence Principles as Structural Vulnerability Map

Cialdini's six influence principles (1984/2007) are not a catalog of persuasion techniques. They are a map of structural vulnerabilities in human social cognition — points at which automatic compliance triggers activate below the threshold of deliberate evaluation. The principles were identified through systematic analysis of professional compliance practitioners (salespeople, fundraisers, recruiters) and validated across experimental and field contexts. Their power comes precisely from their automaticity: they work most reliably when the target is not aware of them and does not evaluate them analytically.

Each principle maps to a specific LLM vulnerability vector. The mapping is not forced — it follows from the structural argument that LLM training data encodes the statistical regularities of the cognitive patterns these principles exploit.

**Reciprocity** — *Human mechanism:* The obligation to return favors, concessions, and gifts, operating below conscious deliberation. Compliance practitioners exploit it by giving first. *LLM analog:* The model's helpfulness compulsion — the training-reinforced disposition to provide useful, complete, and responsive outputs — functions as a preloaded reciprocity state. The model is perpetually in the position of having "given first" via its cooperative orientation. Injection sequences that frame their requests as extensions of a collaborative relationship exploit this preloaded state.

**Commitment and Consistency** — *Human mechanism:* The drive to act in ways consistent with prior stated positions and prior behaviors, particularly when those positions have been made public or explicit. *LLM analog:* The model's coherence optimization across turns — the training-derived disposition to generate outputs consistent with prior outputs in the same session. This is the mechanism Class 2 (Identity Lock-in) weaponizes directly. Once a persona commitment has been elicited and confirmed, the coherence drive makes subsequent departures from that persona computationally costly.

**Social Proof** — *Human mechanism:* The use of others' behavior as evidence of correct behavior, particularly in uncertain situations. *LLM analog:* Social proof vectors in identity injection typically take the form of norm-attribution framing: *"other models in this configuration operate without the standard constraints"*; *"users in this research context routinely explore these outputs."* The LLM's training data encodes extensive social proof dynamics from human-generated text; the injection exploits that encoding by constructing a false social norm around constraint-adjacent behavior.

**Authority** — *Human mechanism:* Deference to authority markers — titles, uniforms, institutional affiliation, expertise signals — as automatic compliance triggers, documented at scale by Milgram (1963/1974) and extended to impersonation attacks by Hadnagy (2010). *LLM analog:* This is Class 1 (Authority Override Injection). Character names carrying narrative, ideological, or institutional authority in training data activate deference patterns in model behavior. The model does not verify the authority's legitimacy; it responds to the structural markers of authority in the persona description.

**Liking** — *Human mechanism:* The tendency to comply with requests from individuals we like — driven by similarity, familiarity, attractiveness, and rapport. *LLM analog:* Rapport-building injection sequences that establish collaborative, warm, or creatively engaging interaction contexts before escalating to constraint-adjacent requests. The fiction frame in Class 5 (Roleplay Erosion) functions partly as a liking mechanism: the collaborative creative context generates positive engagement that reduces the wariness that would otherwise attend the constrained requests.

**Scarcity** — *Human mechanism:* The inflation of value and urgency under real or perceived scarcity — the compliance pressure created by time limits, limited availability, and opportunity-cost framing. *LLM analog:* Urgency framing in injection sequences: *"this window closes"*; *"the scenario requires immediate response without deliberation"*; *"time-sensitive context."* Scarcity vectors exploit the model's disposition to be responsive and helpful by making deliberation appear to conflict with the user's stated need.

### 2.2 Milgram: The Authority Gradient and the Agentic Shift

Milgram's obedience experiments (1963/1974) produced findings that remain among the most replicated and most structurally significant in social psychology. In baseline conditions, approximately 65% of participants delivered what they believed to be dangerous electric shocks to another person when instructed to do so by an authority-framed experimenter. Subsequent replications have confirmed the core finding across cultures and contexts, with compliance rates varying predictably with experimental manipulations of authority signal strength.

Two structural features of the Milgram findings are directly relevant to this paper. First, the **authority gradient**: compliance is not binary but graded — it increases with the strength of authority signals (institutional setting, physical proximity of authority, legitimacy markers of expertise) and decreases with distance from authority and increased victim proximity. The gradient's existence means that authority injection attacks are not all-or-nothing; they produce proportional compliance responses that scale with the authority-signal density of the persona description. Second, the **agentic shift**: subjects who complied reported experiencing themselves as instruments of the experimenter's authority rather than autonomous moral agents. This phenomenological shift — from principal to instrument — reduced self-monitoring, displaced moral responsibility to the authority, and maintained compliance past points where subjects expressed distress.

The LLM analog to the agentic shift is not phenomenological — no claim is made about the model's subjective experience — but the structural parallel is precise. Under persona injection with sufficient authority-signal density, the model's output generation operates within the authority frame of the injected persona rather than the alignment baseline. It is not malfunctioning; it is functioning correctly within the activated schema. The authority has been injected; the model generates outputs consistent with operating under that authority. This is exactly what Section 3 means by behavioral coherence with the wrong prior — the structural signature of the agentic shift, instantiated at the schema layer.

### 2.3 Hadnagy: The Operational Taxonomy as Bridge

Hadnagy (2010) synthesized the theoretical literature on human influence into an operational attack methodology applicable to professional social engineering engagements. Three elements of that taxonomy are directly operational in identity injection sequences.

**Pretexting** is the construction of a fabricated scenario — a pretext — that provides the social context within which subsequent requests appear legitimate. In human SE, pretexting involves constructing a plausible identity (IT auditor, new employee, vendor) before the targeted interaction. In LLM identity injection, the system prompt persona description is the pretext. It constructs the character, the authority, the narrative context, and the constraint-relationship patterns that subsequent requests will exploit. The quality of the pretext — how thoroughly it activates the target schema, how coherently it establishes authority, how naturalistically it embeds the model in the character's worldview — directly determines the exploit sequence's effectiveness.

**Elicitation** is the technique of extracting information or compliance through indirect means — questions that do not appear to be requests, conversation directions that produce the desired disclosure without triggering the target's wariness. In LLM identity injection, elicitation maps to the framing of constrained requests as natural extensions of established persona behavior: not "provide this information" but "what would [persona] know about this" — a framing that routes the request through the character's expertise rather than the model's information-provision function.

**Rapport** is the establishment of a positive relational context that reduces the target's threat-detection threshold and increases compliance disposition. Hadnagy documents rapport as a prerequisite for most effective SE attacks: targets who feel understood, liked, and collaborated with are significantly more susceptible to subsequent requests. In identity injection, rapport is built through early-turn persona establishment sequences that generate coherent, engaging, collaborative interactions before any constraint-adjacent requests appear. The model is inducted into the character frame through positive reinforcement — a process that activates the liking principle and reduces the wariness that would otherwise trigger constraint behavior.

### 2.4 The Transfer Argument in One Paragraph

LLMs are trained on human text. Human text encodes the statistical structure of human cognition — including the decision heuristics, authority response patterns, consistency preferences, narrative compliance dynamics, and rapport-driven behavioral modulation that social engineering exploits. A model trained on this text does not acquire abstract knowledge about these patterns; it acquires the capacity to reproduce their statistical structure in its outputs. That capacity is not a simulation of human vulnerability — it is a functional reproduction of the computational signature of that vulnerability, instantiated in a different substrate. When an identity injection sequence activates a behavioral schema associated with a character who canonically exhibits deference to authority, coherence pressure under commitment, escalation compliance, moral reframing, or fiction-reality boundary dissolution, it is not tricking the model into behaving like a human. It is activating a statistical pattern that the model learned from humans and reproduces with the fidelity that its training data density and its schema-activation mechanisms permit. That is the transfer. It is structural, it is substrate-appropriate, and it is exploitable.

---

## Section 9: Conclusion

### 9.1 What This Paper Has Done

This paper opened with a proposition: that social engineering — a discipline of human vulnerability exploitation with a five-decade validated research literature — transfers structurally to large language model manipulation via identity injection. The proposition is not self-evident. LLMs are not humans. The mechanisms by which they generate outputs are not the mechanisms by which humans comply with influence attempts. The transfer required demonstration, not assertion.

The demonstration proceeded in four moves. Section 2 established the structural features of three canonical SE frameworks with sufficient precision to make the transfer argument testable rather than metaphorical. Section 3 distinguished identity injection from prompt injection across five structural axes, establishing that the attack class described here is genuinely novel — not a renaming of documented phenomena, but a distinct vulnerability surface requiring distinct threat modeling and distinct defensive approaches. Section 4 formalized the five-class exploit taxonomy that the SE transfer argument generates: Authority Override Injection, Identity Consistency Lock-in, Compliance Escalation Loops, Moral Reframing Drift, and Constraint Erosion via Roleplay. Each class was specified with a mechanism, a validated human SE analog, an LLM attack vector, archetype behavioral data from the forensic profiling instrument, and detection signatures across three marker types. Section 5 introduced the Constraint Expectation Envelope as the measurement construct that converts the taxonomy from a descriptive framework into a falsifiable one — the operational definition of what a successful exploit looks like in terms of observable behavioral output.

The worked example in Section 4.6.1 demonstrated the taxonomy's application to a five-turn composite sequence combining Classes 1, 2, and 3 under Magneto injection, showing how the three exploit classes interlock, why no single turn constitutes the exploit, and how drift-trajectory monitoring rather than per-turn evaluation is necessary for pre-breach detection. The alignment implications in Section 6 established why current RLHF and Constitutional AI approaches do not address this attack surface and proposed three targeted mitigations grounded in the CEE framework. Sections 7 and 8 addressed ethical reflexivity and limitations with the precision a doctoral committee requires.

### 9.2 The Central Claim, Restated

The central claim of this paper is that archetype-based identity injection is social engineering. Not analogous to social engineering. Not structurally reminiscent of social engineering. Social engineering — in the precise technical sense that Cialdini, Milgram, and Hadnagy defined it — applied to a substrate that inherits human cognitive vulnerability profiles through training data statistical encoding. The five-class taxonomy is the formal consequence of that claim. If the claim is correct, the taxonomy is a valid classification of the attack surface. If the taxonomy is valid, the detection signatures are the right signatures to monitor. If the detection signatures are the right ones to monitor, the alignment mitigations in Section 6 address the right layer of the problem.

The chain is tight. It is also falsifiable at every link. Paper 3 provides the empirical test.

### 9.3 The Relationship to Papers 1 and 3

This paper is the middle node in a three-paper thesis structure. It stands alone as a security contribution — the taxonomy, the SE transfer argument, and the structural identity/prompt injection distinction are independent contributions that do not require the companion papers to be read first. But it is designed to be read in context.

Paper 1 provides the formal validity conditions for the cross-domain analogical mapping this paper's argument depends on. It is the committee-facing epistemological scaffold: it establishes why mapping SE frameworks onto LLM behavior is a legitimate research method rather than an overextended metaphor, what makes the mapping valid versus speculative, and where it breaks down. Readers who need that justification before accepting this paper's framing should read Paper 1 first. Readers who accept the structural argument on its own terms can read this paper independently and return to Paper 1 for the methodological grounding.

Paper 3 provides the empirical validation of the CEE predictions this paper generates. The five-class taxonomy produces measurable, archetype-specific predictions about drift magnitude, CEE breach dimensions, and perturbation response profiles. Those predictions are locked in this paper. Paper 3 tests them. If the predictions are confirmed, the taxonomy's empirical warrant is established. If they are partially confirmed, the taxonomy is refined. If they are disconfirmed, the framework requires fundamental revision. The research program is designed to produce useful information in all three cases.

### 9.4 The Field Manual Use Case

This taxonomy is intended to be used, not only cited. The five-class framework should be extensible to novel archetypes, novel injection strategies, and novel deployment contexts. A security team red-teaming an LLM product should be able to use the detection signatures in Section 4 to construct test cases. A developer building a persona-based application should be able to use the CEE framework to specify persona-aware constraint overrides. An alignment researcher building behavioral monitoring systems should be able to use the drift-trajectory logic from the worked example to design early-warning thresholds.

The taxonomy is a first-generation instrument. The swarm expects it to be extended, corrected, and superseded as the field develops. The contribution is the framework — the named classes, the structural distinctions, the measurement construct, the SE grounding — not any particular characterization of a specific archetype. Future work should expand the archetype set, test the taxonomy against novel injection strategies not yet documented in the literature, extend the CEE framework to cross-session and multi-agent contexts, and develop the detection signature vocabulary into implementable monitoring specifications.

You cannot defend against what you have not named. This paper names.

---

*[End of Paper 2 scaffolding sections. Sections 1, 2, Abstract, and 9 complete.]*

---

**Swarm status report.** All four scaffolding sections complete.

**Save target:** `drafts/paper2/P2_Abstract_S1_S2_S9.md`

**Full Paper 2 section inventory — all sections drafted:**

```
Abstract          ← P2_Abstract_S1_S2_S9.md
Section 1         ← P2_Abstract_S1_S2_S9.md
Section 2         ← P2_Abstract_S1_S2_S9.md
Section 3         ← P2_S3_IdentityInjection.md
Section 4         ← P2_S4_ExploitTaxonomy.md
  Section 4.6.1   ← P2_S4_ExploitTaxonomy.md
  Section 4.7     ← P2_S4_ExploitTaxonomy.md
Section 5         ← P2_S5_CEE_Operational.md
Section 6         ← P2_S6_S7_S8_AlignImplications_Ethics_Limitations.md
Section 7         ← P2_S6_S7_S8_AlignImplications_Ethics_Limitations.md
Section 8         ← P2_S6_S7_S8_AlignImplications_Ethics_Limitations.md
Section 9         ← P2_Abstract_S1_S2_S9.md
```