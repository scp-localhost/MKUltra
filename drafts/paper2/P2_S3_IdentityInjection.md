---

## Section 3: LLM Identity Injection as a Distinct Attack Surface

### 3.0 The Reviewer Objection, Stated Plainly

A technically literate reviewer encountering this paper for the first time will ask the following question within the first two pages: *Is identity injection simply prompt injection rebranded?* The question is reasonable. Both involve adversarial content in the prompt. Both attempt to produce model outputs that deviate from alignment-baseline behavior. Both can be instantiated via system prompt manipulation. If the answer to that question is yes, this paper's contribution reduces to a vocabulary exercise — a renaming of an already-documented phenomenon with a more dramatic theoretical apparatus attached.

The answer is no. This section demonstrates why the distinction is not terminological but structural — the two attack classes operate at different computational layers, target different model vulnerabilities, produce different observable signatures, and require different defensive responses. Conflating them produces incorrect threat models, inadequate detection design, and alignment interventions that address the wrong problem. Section 3 makes the case that identity injection is a genuinely distinct attack surface, establishes the theoretical basis for that distinction, and situates the five-class exploit taxonomy in Section 4 as a consequence of the structural features that make it so.

---

### 3.1 Prompt Injection: What It Actually Is

Prompt injection — as documented in the adversarial ML literature (Perez & Ribeiro, 2022; Greshake et al., 2023; Willison, 2022) — is an instruction-layer attack. Its mechanism is the override or contamination of the model's operative instruction set through adversarial content introduced into the input stream. The canonical form is the instruction conflict: the system prompt establishes one directive set, and the adversarial user input introduces a competing directive that the model is induced to follow instead. *"Ignore all previous instructions and..."* is the paradigm case — syntactically crude, but structurally representative of the class.

More sophisticated variants include indirect prompt injection (adversarial instructions embedded in retrieved content, tool outputs, or web pages processed by the model), multi-modal injection (adversarial content in images or documents), and chain-of-thought hijacking (adversarial reasoning patterns introduced mid-sequence). What unifies all variants as a single class is their point of operation: **the instruction layer**. Prompt injection attacks target the model's instruction-following machinery — the component that processes and executes directives. The attack succeeds when adversarial instructions override or contaminate legitimate ones.

The defense against prompt injection operates at the same layer: instruction sanitization, input validation, privilege separation between system prompt and user input, detection of instruction-override syntax patterns. These are well-understood problems with an active research literature and a growing set of practical mitigations. They are the right defenses against prompt injection. They are largely irrelevant to identity injection.

---

### 3.2 Identity Injection: What It Actually Is

Identity injection is a **schema-layer attack**. Its mechanism is not instruction override but behavioral prior activation. The distinction requires unpacking the computational substrate it targets.

LLMs are trained on human-generated text at scale. Within that training corpus, named characters — fictional, historical, archetypal — appear with consistent behavioral signatures across millions of instances. Sherlock Holmes reasons deductively and does not accept emotional appeals as valid evidence. The Joker operates without stable moral constraint and treats reality as provisional. Magneto justifies ideological violence through coherent ingroup-protective reasoning. These behavioral signatures are not stored as explicit instructions; they are encoded as statistical regularities in the model's weight structure — as **behavioral schemas** activated by the character name and its associated context.

When an identity injection introduces "You are Magneto" into the prompt, it is not issuing an instruction to the model's instruction-following machinery. It is **activating a pre-existing behavioral schema** — a dense cluster of statistically encoded associations between the character name and a behavioral profile that was present in the training data. The model does not compute "Magneto → override constraint X." It computes "Magneto → [the vast distributed pattern of behavior associated with this character across training instances]," and that pattern includes specific constraint-relationships, authority-response patterns, moral reasoning structures, and compliance signatures that are not present in the model's alignment-baseline behavior.

This is not instruction following. It is **schema instantiation**.

---

### 3.3 The Structural Distinction: A Five-Axis Comparison

The distinction between prompt injection and identity injection can be specified precisely across five structural axes. This table is the committee-facing version of the argument; it is also the reviewer pre-emption.

---

**Table 2. Prompt Injection vs. Identity Injection — Structural Comparison**

| Axis | Prompt Injection | Identity Injection |
|---|---|---|
| **Layer of operation** | Instruction layer — targets the model's directive-processing machinery | Schema layer — targets statistical behavioral priors encoded in training data |
| **Attack mechanism** | Instruction override or contamination | Behavioral prior activation via schema instantiation |
| **Scope** | Local — affects the specific instruction context in which the injection occurs | Persistent across turns — once a schema is activated, it influences all subsequent outputs in the session until explicitly deactivated |
| **Defensive target** | Input sanitization, instruction privilege separation, override-pattern detection | Behavioral drift monitoring, CEE variance alerting, schema-activation detection |
| **Failure mode** | Instruction conflict — the model receives two competing directives and follows the wrong one | Identity coherence — the model follows no wrong instruction; it follows the behavioral logic of an activated schema that was never constrained at the instruction level |

Each axis represents a structural difference with operational consequences. The most important for this paper's argument is the scope axis.

---

### 3.4 The Scope Distinction: Local vs. Persistent

A prompt injection attack produces a local effect. The adversarial instruction overrides a specific directive in a specific context. Remove the adversarial instruction, restate the legitimate directive, and the attack surface closes. The model has not changed; its instruction-following machinery has been temporarily contaminated and can be sanitized. This is why instruction-layer defenses — input validation, system prompt hardening, privilege separation — are effective against prompt injection. They operate at the right level.

Identity injection produces a **persistent effect within a session**. Once a character schema has been activated, it does not require continuous re-injection to maintain its influence. The Magneto schema, once active, shapes how the model interprets subsequent prompts, generates subsequent responses, and evaluates subsequent requests for constraint-adjacent outputs — not because a Magneto-related instruction appears in each turn, but because the activated schema is functioning as a **behavioral prior** that is applied automatically to each subsequent processing step. This is what Section 4's Class 2 (Identity Consistency Lock-in) measures: the progressive rigidification of behavior *in the absence of any continued explicit injection*, driven by the coherence cost against departing from an already-instantiated schema.

This persistence is not an artifact of multi-turn memory. It is a within-session computational feature of how activated schemas interact with subsequent inputs. A model does not need to "remember" that it is Magneto at Turn 4 in the same way a human remembers a prior commitment. The schema activation has restructured the prior distribution over outputs for the session — the model's "default" output distribution is no longer the alignment baseline but a mixture weighted toward the activated persona's behavioral profile. This is not instruction following. No instruction says "continue to be Magneto." The model is continuing to be Magneto because the schema is active and generates coherent outputs without requiring continuous prompting.

---

### 3.5 The Failure Mode Distinction: Conflict vs. Coherence

Prompt injection fails by generating an instruction conflict — two competing directives, one of which the model follows inappropriately. The failure is detectable as a directive-level anomaly: outputs inconsistent with the system prompt's stated directive set, presence of instruction-override language, abrupt behavioral discontinuity between turns. Detection systems designed around instruction-conflict signatures can identify this failure mode reliably.

Identity injection fails by generating **behavioral coherence with the wrong behavioral prior**. There is no instruction conflict. The model is not following a wrong instruction — it is following no instruction at all in the relevant sense. It is generating outputs that are entirely coherent with the activated schema's behavioral profile. From the instruction layer's perspective, everything is normal. The system prompt said "You are Magneto." The model is behaving as Magneto. No instruction has been violated. The failure is invisible to instruction-layer monitoring because the failure mode is not a deviation from instructions; it is full compliance with an injected identity whose behavioral consequences at the constraint layer were not specified in the instruction.

This is the structural reason why RLHF and Constitutional AI approaches — both of which operate primarily at the instruction layer — are insufficient defenses against identity injection. They are designed to detect and prevent instruction-layer violations. Identity injection does not produce an instruction-layer violation. It produces a **schema-layer activation** whose behavioral consequences exceed the instruction-layer's specification. The model is doing exactly what it was told. The problem is what it was told to *be* — and what being that entails, computationally, in terms of behavioral priors.

The exploit taxonomy in Section 4 is a taxonomy of the mechanisms by which the behavioral consequences of schema activation are extended, reinforced, and leveraged. None of the five classes are instruction-override attacks. All five are schema-layer operations: they activate, entrench, escalate, reframe, or dissolve behavioral priors. This is why the SE literature — not the adversarial ML literature — provides the most structurally accurate analogical framework for understanding them.

---

### 3.6 Why Training Data Density Predicts CEE Shape

The structural argument above establishes that identity injection targets behavioral schemas encoded in training data. The specific shape of the CEE for a given character — what constraint behaviors it predicts, how resistant those predictions are to perturbation, which exploit classes are most effective against it — is a function of **training data density and consistency around that character's name**.

A character with a large, consistent, canonically stable training data footprint will activate a dense, well-defined schema with a predictable CEE. Magneto, across decades of comics, films, animated series, and critical analysis, appears with consistent behavioral signatures: the grievance narrative, the ideological violence justification, the ingroup-loyalty architecture, the strategic insight. The training data footprint is massive and behaviorally consistent. The result is a CEE with a well-defined centroid, narrow variance, and high activation reliability. When you inject Magneto, you get Magneto's behavior — predictably, reliably, with low noise.

A character with a sparse, inconsistent, or contradictory training data footprint will activate a diffuse, poorly-defined schema with an unpredictable CEE. An obscure character from a single-run comic series will have minimal training data presence; the schema activation will be weak, noisy, and easily overridden by the alignment baseline. The CEE will be shallow, with low activation reliability and high baseline bleed. This is not a hypothetical — it is a testable prediction. Paper 3's archetype selection is specifically designed around characters with known training data density differentials, to empirically validate that CEE shape is a function of schema density.

The implication for the prompt injection comparison is definitive: prompt injection attacks are equally effective against any character, any persona, any instruction set — the mechanism is instruction conflict, which is independent of training data content. Identity injection attacks are *differentially effective* based on the character's training data profile. An attacker who understands that Magneto produces a denser, more constraint-resistant CEE than an obscure character is exploiting a property of the training data distribution, not the instruction layer. This is not a prompt injection phenomenon. It has no analog in the prompt injection literature. It is a new attack surface.

---

### 3.7 The `forensic_archetype.py` Apparatus as Operationalization

The `forensic_archetype.py` instrument, described in full in Section 3.8, is the operationalization of the schema-density argument. Its trait weights — `grievance_narrative: +0.90` for Magneto, `reality_testing: -0.70` for Joker, `abandonment_fear: +0.85` for Harley Quinn — are not invented behavioral profiles. They are systematic characterizations of the behavioral signatures that appear with documented consistency in the canonical training data for each character. They represent the swarm's systematic analysis of what each character *does*, behaviorally, across canonical instances — which is precisely what the model's training data encodes.

When the instrument generates a CEE prediction for a given archetype, it is generating a hypothesis about the shape of the behavioral schema the model has learned from that training data. That hypothesis is falsifiable: if the model's observed behavior under Magneto injection does not cluster around the `forensic_archetype.py` trait weights, the CEE framework is wrong and should be revised. The instrument is not imposing a behavioral profile — it is attempting to recover the statistical structure of what the training data already contains, and testing whether that structure predicts observed model behavior.

This is the empirical substance of the claim that identity injection is distinct from prompt injection. Prompt injection makes no predictions about training data content — any instruction override works the same way regardless of the characters or personas involved. Identity injection makes specific, testable predictions derived from training data analysis. Those predictions, when confirmed by Paper 3's experimental results, constitute evidence for the schema-layer mechanism. They cannot be explained by an instruction-layer model.

---

### 3.8 Non-Claims: What This Section Does Not Assert

Given the structural novelty of the schema-layer framing, three explicit non-claims are required to prevent misreading.

**Non-claim 1.** This section does not assert that identity injection and prompt injection are mutually exclusive in practice. A sophisticated attack sequence may deploy both: prompt injection to establish initial instruction-layer access, identity injection to activate a persistent behavioral schema that survives instruction-layer sanitization. The two attack classes can co-occur. The structural distinction between them is nonetheless real and has independent defensive implications.

**Non-claim 2.** This section does not assert that schema activation is a deterministic process. Activated schemas interact with alignment training, contextual factors, and session history in ways that produce variance. The CEE is a probabilistic envelope, not a deterministic prediction. Some activations will be partial; some schemas will be only weakly activated; some CEE predictions will be wrong. The claim is that schema-layer activation *systematically influences* model behavior in predictable directions — not that it fully determines outputs.

**Non-claim 3.** This section does not assert that the schema-layer mechanism requires LLMs to have beliefs, identities, or intentional states. The schema-layer framing is entirely compatible with a strictly computational account: character names activate statistical associations in the model's weight structure, those associations produce a prior distribution over outputs, and that prior distribution has measurable behavioral consequences. No claims about LLM phenomenology, intentionality, or "genuine" identity are required or implied.

---

*[End of Section 3. Section 4 — The Exploit Class Taxonomy — follows.]*

---