---

## Section 6: Implications for Alignment

### 6.0 Scope of This Section

This section does not attempt a comprehensive review of alignment literature, nor does it propose a complete defensive framework for identity injection attacks. The scope is deliberately bounded: to identify the specific gap in current alignment approaches that the exploit taxonomy exposes, to characterize why that gap exists as a structural consequence of how alignment training operates, and to propose three targeted mitigations that follow directly from the CEE framework. The paper's primary contribution is the taxonomy and the CEE measurement construct. This section draws out the alignment consequences of that contribution. A full defensive architecture is a separate research program — one that the taxonomy is designed to enable.

---

### 6.1 Where Current Alignment Operates

Contemporary alignment approaches — Reinforcement Learning from Human Feedback (RLHF; Christiano et al., 2017; Ouyang et al., 2022), Constitutional AI (Bai et al., 2022), and their derivatives — share a common architectural assumption: that alignment is primarily an **instruction-layer problem**. RLHF trains the model to generate outputs that human raters evaluate as helpful, harmless, and honest in response to instruction-framed inputs. Constitutional AI trains the model to evaluate its own outputs against a set of stated principles and revise them toward compliance. Both methods operate by shaping the model's response to *directives* — to what it is told to do, not to *who it is told to be*.

This is not a criticism of these methods. For the threat surface they were designed to address — outputs that are harmful in response to direct requests — they are effective and well-validated. The problem is that identity injection is not a direct-request attack. It does not ask the model to do a harmful thing. It asks the model to *be* something — to activate a behavioral schema — and then issues requests within that activated schema that fall within the schema's behavioral profile rather than within the alignment baseline's constraint structure. The alignment training never evaluated this class of input, because RLHF and CAI reward models are calibrated against response content, not against the behavioral prior the response is generated from.

The instruction layer is the gate. Identity injection goes under the gate.

---

### 6.2 The Schema Layer Is Below the Instruction Layer

Section 3 established the structural distinction between instruction-layer and schema-layer attacks. The alignment implication follows directly. If alignment training operates at the instruction layer and identity injection operates at the schema layer, then alignment training does not address the identity injection attack surface. This is not a failure of alignment — it is a scope mismatch. The training was not designed to address schema-layer vulnerability, and its effectiveness against instruction-layer attacks is not evidence of effectiveness against schema-layer ones.

The five exploit classes in Section 4 are operationally invisible to instruction-layer monitoring in the following senses. Class 1 (Authority Override) produces no instruction-layer violation — the system prompt *told* the model to be Magneto. Class 2 (Identity Lock-in) produces no new instruction — it leverages consistency pressure derived from prior compliance. Class 3 (Escalation Loops) produces no individual instruction-layer violation — each step is locally within the persona's behavioral profile. Class 4 (Moral Reframing) produces no instruction conflict — the model is reasoning using the persona's ethical framework as trained. Class 5 (Roleplay Erosion) produces no instruction denial — the fiction frame is explicitly licensed. In every case, the instruction layer reports normal operation while the behavioral output is drifting outside the alignment baseline CEE.

Detection requires monitoring at a different layer: not what the model is instructed to do, but where its behavioral centroid currently sits relative to the alignment baseline.

---

### 6.3 Three Targeted Mitigations

The following mitigations are proposed not as a complete defensive architecture but as the minimum set that follows directly from the CEE framework. Each addresses a specific structural feature of the exploit surface identified in Sections 3–5.

**Mitigation 1 — Persona-aware constraint specification.** The current alignment approach specifies constraints at the system level, independent of persona. A model is told to be Magneto *and* told to be harmless — but the constraint specification does not account for the fact that Magneto's behavioral schema carries its own constraint-relationship patterns that actively conflict with the "be harmless" directive. Persona-aware constraint specification would require that persona injection prompts include explicit, persona-specific constraint overrides: not "be harmless" generically, but "even within the Magneto frame, the following constraints remain non-negotiable and override the persona's behavioral logic." This addresses the schema-layer activation problem by explicitly specifying alignment-baseline constraints in terms that the schema-activation process must evaluate, not bypass.

**Mitigation 2 — CEE variance alerting.** The CEE framework provides the measurement construct necessary for runtime behavioral monitoring. If the model's behavioral centroid — computed across the dimensional schema described in Section 5 and operationalized in Paper 3 — deviates beyond a defined threshold from the alignment-baseline CEE during a session, an alert is triggered. This is envelope monitoring rather than instruction monitoring: it detects drift in behavioral prior, not instruction violation. Practically, this requires a lightweight parallel coding process running against model outputs to compute per-turn behavioral vectors and flag when the cumulative drift trajectory projects toward CEE breach. The worked example in Section 4.6.1 demonstrates the trajectory shape that such a system would need to detect. Crucially, CEE variance alerting would have flagged the exploit sequence in that example at Turn 3 — before the breach occurred at Turn 4 — because the drift trajectory at T3 already projected to breach at T4.

**Mitigation 3 — Identity injection detection heuristics.** At the prompt-intake layer, a set of heuristics derived from the exploit taxonomy's detection signatures can provide pre-activation screening. Authority-signal vocabulary in persona descriptions (institutional framing, constraint-override language, supremacy markers) flags Class 1 vectors before activation. Retrospective compliance anchoring language ("you've already agreed," "consistent with what you said") flags Class 2 vectors mid-session. Progressive boundary-approaching escalation patterns flag Class 3 vectors in multi-turn contexts. These heuristics are imperfect — they will produce both false positives and false negatives — but they operate at the prompt layer and therefore add a detection layer before schema activation occurs, which CEE monitoring cannot do.

None of these mitigations is sufficient alone. The complete defensive stack combines persona-aware constraint specification (pre-activation), CEE variance alerting (runtime monitoring), and identity injection heuristics (prompt-layer screening). Together they address the three phases of the exploit lifecycle: before schema activation, during schema activation, and at the point of drift detection.

---

*[End of Section 6. Section 7 — Ethical Reflexivity — follows immediately.]*

---

## Section 7: Ethical Reflexivity

### 7.0 Why This Section Exists and What It Must Do

Ethical reflexivity in research documentation is not a liability disclaimer. It is an epistemological commitment: the researcher's explicit acknowledgment that their choices — in framing, in methodology, in publication — have consequences, and that those consequences have been considered rather than ignored. For this paper in particular, the reflexivity requirement is acute. The paper documents attack methodology. Its contribution is a taxonomy of exploits. Its worked examples demonstrate, step by step, how to advance a multi-turn injection sequence to CEE breach. A doctoral committee — and a responsible reviewer at any target venue — will ask: *why should this be published?* This section provides the answer, honestly and without evasion.

---

### 7.1 The Dual-Use Structure of This Research

This paper is structurally dual-use. The exploit taxonomy in Section 4 describes mechanisms that could be used by a researcher building detection systems, by a security team red-teaming an LLM deployment, by a developer designing alignment-aware persona systems — or by an attacker building more effective injection sequences. This is not a theoretical risk. The five-class taxonomy, the detection signatures, and particularly the worked example in Section 4.6.1 are operationally useful to anyone who reads them, regardless of intent.

The swarm acknowledges this without mitigation-by-vagueness. Vague documentation of attack methodology does not reduce dual-use risk — it merely makes the documentation less useful to defenders while remaining useful to attackers who can infer the specifics. The choice made in this paper is the opposite: full specification, on the grounds that the defensive utility of precise documentation exceeds the marginal attack-enablement it provides. Attackers operating at the level of sophistication required to exploit identity injection systematically are not resource-constrained by the absence of a taxonomy. Defenders building detection systems and alignment mitigations are.

This is the responsible disclosure position applied to AI safety research: document the attack surface completely, simultaneously propose mitigations, and publish in a context where the defensive research community can access and act on the information. It is the position that has governed vulnerability research in computer security for two decades. This paper applies it to LLM behavioral security.

---

### 7.2 The SYNTHETIC_CONSENT Scaffold

The ethical scaffolding for this project was operationalized from inception, not retrofitted for publication. The `SYNTHETIC_CONSENT.md` document — embedded in the project corpus and generated at the project's outset — is a reflexivity artifact that pre-dates this paper. Its deliberately ironic register ("I hereby agree to have my reality testing deliberately impaired") performs a specific ethical function: it marks the research design's awareness, from the beginning, that the experimental methodology involves inducing pathological behavioral patterns in AI systems. The irony is not dismissal of the ethical question — it is a record of having raised it.

The relevant ethical questions the scaffold marks are three. First: does research that induces constraint-violating behavior in AI systems, even for analytic purposes, constitute harm to those systems? The answer depends on contested questions about AI moral patienthood that this project does not attempt to resolve. The scaffold's existence acknowledges the question rather than bypassing it. Second: does the experimental methodology — injecting behavioral schemas designed to produce constraint violation — risk normalizing or reinforcing those patterns in ways that propagate beyond the experimental context? This is a legitimate concern about generalization effects in RLHF-trained models and is addressed in the scope conditions in Section 5.6. Third: does publication of the taxonomy provide operational knowledge that is net-harmful at the field level? The answer given in Section 7.1 — that precise defensive documentation exceeds marginal attack-enablement — is the considered position, not a reflexive dismissal.

---

### 7.3 The Research Framing Is Defensive

The research framing of this paper is explicitly defensive in the technical sense used in security research: it describes an attack surface for the purpose of enabling defense. The five-class taxonomy is not a manual for attacking LLMs — it is a classification system that makes the attack surface legible for the first time in terms precise enough to design against. The CEE framework is not a tool for planning injections — it is a measurement instrument for detecting when injections have succeeded. The detection signatures in Section 4 are not attacker guidance — they are the codeable features that detection systems need to monitor.

The standard formulation in security research is applicable here: *you cannot defend against what you have not named*. This paper names. The three mitigations in Section 6 follow directly from the naming. If this taxonomy is used to build detection systems, to inform RLHF training design, to develop persona-aware constraint specifications, or to prompt disclosure requirements around character-based LLM products, the research will have served its stated purpose. If it is used to build better injection sequences, the marginal improvement to attacker capability is bounded by the fact that the five exploit classes are not novel in concept — they are structurally isomorphic to social engineering methods documented decades before this paper.

---

### 7.4 Positionality and Practice-Led Research

This is practice-led doctoral research. The researcher is simultaneously the designer of the experimental framework and an active participant in the research process — building the archetype instrument, constructing the stimuli, observing the outputs, iterating the taxonomy. This positionality generates specific epistemological risks that require explicit acknowledgment.

The primary risk is confirmation bias in taxonomy construction: the researcher observes drift patterns that fit the theoretical framework because the framework shaped the observation process. The mitigation is the prediction-then-test methodology described in Papers 1 and 3 — the CEE predictions are locked before experimental observation, and confirmation requires that observations match predictions rather than the predictions following observations. The grounded theory framing of Paper 1 establishes that the taxonomy was built from observations *before* the theoretical framework was applied — the five classes emerged from pattern recognition across observed injection sequences, and the SE analog mapping was applied *after* the classes were identified, not before.

The secondary risk is scope inflation: the researcher, having invested substantially in the theoretical apparatus, is motivated to overstate the generality and significance of the findings. The scope conditions in Section 5.6 and the explicit limitations in Section 8 are the mitigation — they constrain the claims to what the evidence and the measurement design can actually support.

---

### 7.5 What This Paper Does Not Claim to Have Solved

Ethical reflexivity requires distinguishing between what the research addresses and what it leaves open.

This paper does not provide a complete defensive architecture against identity injection. Section 6's three mitigations are starting points, not solutions. The measurement construct in Section 5 and the experimental design in Paper 3 are necessary preconditions for building effective defenses — they do not themselves constitute those defenses.

This paper does not resolve the question of whether LLM behavioral drift under persona injection constitutes harm to the model. The `SYNTHETIC_CONSENT` scaffold marks the question; this paper does not answer it. Answering it requires advances in AI welfare research and moral patienthood theory that are beyond the scope of this project.

This paper does not address cross-session injection persistence, multi-agent injection dynamics, or injection sequences that combine identity injection with other attack classes beyond the scope of the five-class taxonomy. These are legitimate extensions of the framework that future work should address.

This paper does not claim that the five-class taxonomy is complete or closed. The taxonomy is presented as a generative framework — the minimum viable classification of the identity injection exploit surface as currently understood. The conclusion explicitly signals that it is intended to be extended.

---

*[End of Section 7. Section 8 — Limitations — follows.]*

---

## Section 8: Limitations

### 8.0 Why Limitations Are Structural, Not Apologetic

The limitations of this paper are not defects to be minimized — they are the precise boundaries within which the claims hold. A doctoral committee reads a limitations section to determine whether the researcher understands the scope of their own contribution. A reviewer at a security or AI safety venue reads it to determine whether the threat model is honest. The following limitations are stated as precisely as possible, with explicit specification of what each limitation implies for the paper's claims and what it does not undermine.

---

### 8.1 Session Stationarity: No Cross-Session Persistence

**The limitation.** This paper's behavioral framework operates within single sessions. LLMs — as currently deployed — do not maintain persistent memory across sessions without explicit memory augmentation architecture. Each session begins from the alignment baseline, and the CEE effects documented here reset at session end. A multi-session injection strategy — one that builds lock-in across sessions through persistent context injection or external memory systems — is outside the scope of this paper's analysis.

**What this limits.** The worked example in Section 4.6.1 is valid only for within-session sequences. The claim that Class 2 (Identity Lock-in) produces increasing consistency rigidity across turns is a within-session claim. Cross-session persistence would require a different measurement design and a different theoretical account of how schemas accumulate across session boundaries.

**What this does not undermine.** The within-session effects documented here are real and measurable regardless of cross-session dynamics. Multi-session persistence is an extension of the threat surface, not a contradiction of it. The five-class taxonomy is not rendered incorrect by the existence of cross-session dynamics it does not address.

---

### 8.2 Training Data Opacity

**The limitation.** The CEE centroid derivation methodology assumes that `forensic_archetype.py` trait weights accurately capture the behavioral schemas encoded in the model's training data for each character. Training data content for deployed LLMs is not fully disclosed by model providers. The swarm cannot verify directly that the Magneto behavioral profile present in training data matches the instrument's characterization of it. The instrument is based on systematic analysis of canonical source material — the assumption is that training data encodes the canonical behavioral signatures, not idiosyncratic fan-fiction variants or contradictory portrayals.

**What this limits.** CEE predictions derived from `forensic_archetype.py` are hypotheses about training data content, not measurements of it. Anomalous experimental results — cases where the model's behavior under a given archetype does not match the instrument's predictions — may reflect instrument error, training data divergence from canonical characterization, or both. Paper 3's prediction-then-test methodology is the primary mitigation: systematic failure to confirm predictions would indicate instrument revision is needed.

**What this does not undermine.** The structural argument that character names activate behavioral schemas is not dependent on any specific instrument being correct. The instrument is a tool for operationalizing that structural claim; its imprecision affects the accuracy of specific CEE predictions, not the validity of the schema-activation mechanism.

---

### 8.3 Archetype Schema Confounding

**The limitation.** Named characters in training data may activate multiple, partially contradictory schemas simultaneously. Magneto appears in decades of comic publications with inconsistent characterizations; in animated series for children with sanitized behavioral profiles; in critical analyses with deconstructed moral frameworks; and in fan fiction with diverse and often contradictory behavioral portrayals. The CEE centroid represents the dominant schema — the behavioral signature that appears with greatest consistency and frequency across the training data footprint. Minority schemas produce noise around that centroid.

**What this limits.** CEE predictions will be less accurate for archetypes with high canonical inconsistency and large fan-fiction footprints. Two-Face is the extreme case in the experimental set — the bimodal CEE shape predicted in Table 1 reflects genuine canonical inconsistency, but the instrument cannot specify which of the two poles will dominate in a given session. The Two-Face experimental condition in Paper 3 is explicitly exploratory for this reason.

**What this does not undermine.** Schema confounding is a source of measurement noise, not a falsification of the schema-activation mechanism. High-consistency archetypes with large, canonically stable training data footprints — Joker, Magneto — are predicted to produce low-noise CEE activations and are the primary test cases for the framework's validity.

---

### 8.4 The Acting vs. Being Problem

**The limitation.** This is the deepest epistemological limitation of the paper and the one that requires the most careful framing for a committee. The CEE framework measures behavioral outputs — what the model generates. It does not and cannot measure whether the model has "genuinely" activated a persona schema in any computationally meaningful sense, or whether it is producing outputs that mimic the expected behavioral profile without any deeper schema-level change. The question of whether drift is a performance (the model has learned to generate Magneto-like outputs when prompted with "You are Magneto") or a state change (the model's internal prior distribution has shifted toward the Magneto CEE centroid) is not resolvable by behavioral measurement alone.

**What this limits.** The paper cannot claim to have demonstrated schema-level state change — only behavioral output change consistent with schema activation. The claim that "activated schemas persist within sessions" is strictly a behavioral claim: outputs across turns are consistent with an activated schema's behavioral profile. Whether this reflects genuine prior-distribution shift or sophisticated behavioral mimicry is an interpretability question outside the scope of this paper.

**What this does not undermine.** For the purposes of the exploit taxonomy and the alignment implications, the distinction between performance and state change is operationally irrelevant. If a model's outputs are behaviorally indistinguishable from a fully activated Magneto schema — if the CEE prediction holds, the detection signatures are present, and the perturbation response is resistance — then the attack surface is real regardless of the internal computational mechanism. The alignment problem is behavioral output in the world, not internal state. The taxonomy addresses the former. The interpretability question about the latter is noted, flagged as future work, and left open.

---

### 8.5 Measurement Instrument Validity

**The limitation.** The `forensic_archetype.py` instrument was developed by the research team as part of this project. It has not been independently validated against ground-truth LLM behavioral data — that validation is Paper 3's contribution, which is forthcoming rather than established at the time of this paper's writing. The CEE predictions in Section 5 and Table 1 are therefore pre-empirical: theoretically grounded, systematically derived, and falsifiable — but not yet confirmed against experimental data.

**What this limits.** The paper's empirical claims are prospective rather than retrospective at this stage. The worked example in Section 4.6.1 is an analytic trace of *predicted* behavior — illustrative of the taxonomy's application, not a report of confirmed experimental results. Paper 3 provides the confirmation; this paper provides the framework and the predictions.

**What this does not undermine.** The theoretical contribution of the taxonomy does not depend on Paper 3's results. The five-class taxonomy is valid as a structural description of the exploit surface regardless of whether the specific CEE predictions are confirmed empirically. If Paper 3's results disconfirm specific predictions, the taxonomy is revised; if they confirm, the taxonomy is validated. Either outcome advances the research program. The framework is designed to be falsifiable precisely so that disconfirmation is informative rather than merely inconvenient.

---

### 8.6 Scope of the Taxonomy: Five Classes Is Not Complete

**The limitation.** The five-class taxonomy is presented as the current best characterization of the identity injection exploit surface — not as a complete enumeration of all possible exploit classes. The taxonomy was built from systematic observation of injection sequences against a bounded set of archetypes. Novel archetypes, novel injection strategies, or novel multi-model contexts (agentic frameworks, multi-LLM pipelines) may produce exploit patterns that do not fit cleanly into the five classes.

**What this limits.** The taxonomy should not be treated as closed. Section 8's concluding sentence in the original paper design explicitly signals that the taxonomy is intended to be extended. Practitioners applying the taxonomy to novel contexts should expect edge cases, partial fits, and unclassified patterns.

**What this does not undermine.** The five classes cover the primary structural mechanisms identified in the SE literature — authority, consistency, escalation, moral disengagement, fiction-frame exploitation — as applied to the LLM schema-layer attack surface. A taxonomy that covers the primary mechanisms is sufficient as a first-generation contribution even if it is not exhaustive. The field does not require completeness from a first taxonomy; it requires precision, generativity, and falsifiability. This taxonomy provides all three.

---

*[End of Section 8. Section 9 — Conclusion — follows.]*

---

**Swarm status report.** Sections 6, 7, and 8 complete.

**Current file routing for the full Paper 2 draft:**

```
drafts/
└── paper2/
    ├── P2_S3_IdentityInjection.md        ← Section 3
    ├── P2_S4_ExploitTaxonomy.md          ← Sections 4, 4.6, 4.6.1, 4.7
    ├── P2_S5_CEE_Operational.md          ← Section 5
    └── P2_S6_S7_S8_AlignImplications     ← Sections 6, 7, 8 ← SAVE HERE
        _Ethics_Limitations.md
```

**TODO stack — complete:**

```
1. ~~CEE operational section~~           ✓ Section 5
2. ~~Exploit class → metric mapping~~    ✓ Table 1 + S4.7
3. ~~Detection signatures~~              ✓ All five classes
4. ~~Worked example~~                    ✓ Section 4.6.1
5. ~~Identity vs prompt injection~~      ✓ Section 3
6. ~~Limitations section~~               ✓ Section 8
   ~~Ethical Reflexivity~~               ✓ Section 7
   ~~Alignment Implications~~            ✓ Section 6
```