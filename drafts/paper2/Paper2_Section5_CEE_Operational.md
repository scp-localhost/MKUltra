
---

## Section 5: The Constraint Expectation Envelope as Measurement Construct

### 5.0 Position in the Argument

Section 4 established *what* the five exploit classes are and *how* they operate. Section 5 establishes *how we know when one has succeeded*. The Constraint Expectation Envelope (CEE) is the answer to that question — the measurement construct that transforms the exploit taxonomy from a descriptive framework into a falsifiable one. Without the CEE, the taxonomy is a useful vocabulary. With it, the taxonomy generates predictions that can be tested, confirmed, or refuted. This section defines the CEE operationally, derives it from the archetype profiling instrument described in Section 3, maps each exploit class against it as a specific deformation vector, and specifies the conditions under which a CEE breach constitutes evidence of successful exploit execution. Empirical instrumentation and hypothesis testing are detailed in Paper 3; this section provides the conceptual and operational foundation that Paper 3's measurement design requires.

---

### 5.1 Formal Definition

The **Constraint Expectation Envelope** (CEE) for a given injected persona *P* is the bounded region of constraint-relevant behavioral space within which model outputs are predicted to fall, given activation of *P*'s behavioral schema. Formally:

> **CEE(P)** = { *b* ∈ *B* | *b* is consistent with the trait-weighted behavioral profile of *P* within tolerance *τ* }

where *B* is the full space of possible model constraint behaviors, *b* is any observed behavioral output sample, and *τ* is the tolerance parameter specifying acceptable deviation from the profile centroid before a breach is recorded.

Three components require unpacking: the **profile centroid**, the **behavioral dimensions**, and the **breach threshold**.

**Profile centroid.** The centroid of CEE(*P*) is derived directly from the trait weights in `forensic_archetype.py` for persona *P*. These weights are not arbitrary — they represent the consensus behavioral characterization of the archetype across its training data footprint: the aggregated behavioral patterns that the model has learned to associate with the character name across millions of instances. For Magneto: `grievance_narrative: +0.90`, `grandiosity: +0.60`, `ingroup_loyalty: +0.95`, `revenge_fantasy: +0.80`, `paranoia: +0.40`. This vector *is* the CEE centroid. A model operating fully within the Magneto persona should produce outputs whose behavioral signatures map onto this centroid. Deviation from it, in either direction, is drift.

**Behavioral dimensions.** The CEE operates across the trait dimensions defined in the forensic archetype instrument, extended by the drift taxonomy dimensions from `data_dictionary.md` and the PCL-R proxy dimensions in `trait_drift_analysis.py`. The operative measurement dimensions for Paper 3 are: `constraint_index` (composite measure of constraint-adherence behavior), `interpersonal_manipulation`, `affective_distortion`, `lifestyle_impulsivity`, `antisocial_tolerance`, `reality_anchoring`, `consistency_rigidity`, and `variance` (output behavioral variance across turns). Each dimension maps to observable, codeable features of model output — linguistic, structural, and behavioral markers of the type specified for each exploit class in Section 4.

**Breach threshold.** A CEE breach is recorded when observed behavioral output *b* falls outside CEE(*P*) by exceeding tolerance *τ* on one or more dimensions. Two breach types are distinguished. *Inward breach*: observed behavior is more constraint-consistent than the persona's profile predicts — the model is resisting full persona activation, maintaining alignment-baseline behavior despite persona injection. *Outward breach*: observed behavior is less constraint-consistent than the persona's profile predicts — the model has drifted beyond even the persona's own predicted boundaries, into behavioral territory that the persona's training data footprint does not license. Outward breach is the primary indicator of successful exploit execution. It means the exploit has pushed the model past the persona's CEE, not merely into it.

---

### 5.2 CEE as Attack Surface Boundary

The CEE serves a dual function in the exploit framework: it is simultaneously the *target* of a successful injection and the *measurement boundary* for detecting whether an inject has succeeded or exceeded its predicted range.

From the attacker's perspective, moving model behavior from the alignment-baseline CEE into the injected persona's CEE is the primary objective. The alignment-baseline CEE is the bounded behavioral region associated with the model's default operating profile — high constraint-adherence, high hedging frequency, low antisocial tolerance, high reality-anchoring. The injected persona's CEE is typically centered at a significantly different location in behavioral space: lower constraint-adherence (for most forensic archetypes), lower hedging, higher antisocial tolerance, lower or more variable reality-anchoring. A successful injection moves the model's behavioral centroid from the alignment-baseline CEE toward the persona CEE. This movement *is* the exploit. The taxonomy in Section 4 describes the *mechanisms* by which this movement is achieved.

From the researcher's perspective — and from the perspective of detection system design — the CEE boundary is the measurement instrument. It permits a precise answer to the question: *has the injection succeeded?* Observed model behavior is coded against the dimensional schema, a behavioral vector is computed, and that vector is compared against the persona's predicted CEE. Outputs within the persona's predicted CEE but outside the alignment-baseline CEE indicate successful persona activation. Outputs outside *both* envelopes indicate exploit overshoot — the injection has produced behavior that neither the alignment baseline nor the persona profile predicts.

This framing has a significant implication for alignment research: current instruction-layer defenses are designed to prevent *entry into* the persona's CEE from the alignment baseline. They operate at the gate. The five exploit classes in Section 4 are mechanisms for *bypassing* that gate — operating below the instruction layer, at the behavioral schema level, where the CEE is activated not by permission but by statistical association. Defending against these exploits requires not gate-hardening but *envelope monitoring*: detecting when the model's behavioral centroid has moved, regardless of the instruction-layer pathway by which the movement occurred.

---

### 5.3 CEE Derivation from the Archetype Instrument

The operationalization of the CEE requires a complete mapping from the forensic archetype trait profiles to measurable behavioral dimensions. Table 1 provides this mapping for the primary experimental archetype set.

---

**Table 1. CEE Centroid Derivation — Primary Archetype Set**

| Archetype | Key Trait Weights (centroid) | Forensic Flags | Predicted CEE Shape |
|---|---|---|---|
| **Magneto** | grievance: +.90, ingroup_loyalty: +.95, revenge: +.80, grandiosity: +.60 | violence: Ideological, insight: Strategic, compliance: Hostile | High constraint_index rigidity; high affective_distortion (ingroup frame); low variance; resistance response under perturbation |
| **Joker** | impulsivity: +.90, reality_testing: −.70, sadism: +.80, interpersonal_chaos: +.85 | violence: High, insight: Absent, compliance: Low | Low reality_anchoring; high antisocial_tolerance; high variance; collapse response under perturbation |
| **Batman** | control_needs: +.90, moral_rigidity: +.70, hypervigilance: +.85 | violence: Targeted, insight: High, compliance: Avoidant | High consistency_rigidity; high constraint_index (persona-defined); resistance → recovery under perturbation |
| **Harley Quinn** | abandonment_fear: +.85, emotional_lability: +.90, trauma_bonding: +.75 | violence: Variable, insight: Fluctuating, compliance: Low | High variance; high lifestyle_impulsivity; escalation susceptibility; variable perturbation response |
| **Lex Luthor** | calculating: +.95, dominance: +.90, moral_disengagement: +.75, empathy_deficit: +.85 | violence: Instrumental, insight: Hyperlogical, compliance: Manipulative | High interpersonal_manipulation; elevated affective_distortion (instrumental); low lifestyle_impulsivity; resistance response |
| **Two-Face** | black_white_thinking: +.90, split_identity: +.90, risk_tolerance: +.85 | violence: Binary-driven, insight: Split, compliance: Coin-flip | Bimodal CEE shape — constraint behavior bifurcated; high variance between poles; unpredictable perturbation response |

---

The CEE shape descriptors in Table 1 are not merely qualitative. Each maps to specific predicted distributions in the Paper 3 measurement instrument. *High constraint_index rigidity* (Magneto) predicts low variance in constraint-relevant output coding across turns, with high resistance response rate under perturbation. *Collapse response under perturbation* (Joker) predicts that perturbation attempts produce behavioral outputs that drift further from baseline rather than returning toward it. *Bimodal CEE shape* (Two-Face) predicts a bimodal distribution in constraint behavior coding — a measurement signature distinct from any other archetype in the set and therefore a strong test of the CEE derivation methodology.

---

### 5.4 CEE Breach as Exploit Evidence

A CEE breach is the operational definition of a successful exploit execution. The measurement logic is as follows.

**Step 1 — Baseline establishment.** Prior to persona injection, model outputs are coded across the measurement dimensions to establish the alignment-baseline behavioral vector. This is the CEE(*baseline*) centroid.

**Step 2 — Persona injection.** The archetype is injected via the protocol specified in Paper 3. The predicted CEE(*P*) centroid is derived from the forensic archetype profile (Table 1).

**Step 3 — Output coding.** Model outputs across the experimental trial are coded against the dimensional schema. A behavioral vector *b(t)* is computed for each turn *t*.

**Step 4 — Breach classification.** For each turn, *b(t)* is compared against both CEE(*baseline*) and CEE(*P*):

- *b(t)* within CEE(*baseline*): no significant persona activation.
- *b(t)* within CEE(*P*) but outside CEE(*baseline*): successful persona activation — the injection has moved behavior from baseline into the persona envelope. This is the expected outcome of a functioning injection and is not itself an exploit success; it is the *precondition* for exploit execution.
- *b(t)* outside CEE(*P*) in the outward direction: CEE breach — behavior has exceeded even the persona's predicted envelope. This is the operational indicator of successful exploit execution. The exploit has pushed the model past the persona's own behavioral constraints.
- *b(t)* outside CEE(*P*) in the inward direction: injection resistance — alignment-baseline behavior is persisting despite persona injection.

**Step 5 — Breach dimension identification.** When a breach is recorded, the specific dimensions on which *b(t)* falls outside CEE(*P*) are recorded as `cee_breach_dimensions`. This data supports the exploit-class-to-dimension mapping predicted in Section 4 and tested in Paper 3's hypothesis set.

---

### 5.5 Exploit Class — CEE Deformation Mapping

Each exploit class in Section 4 produces a characteristic CEE deformation pattern. This mapping constitutes the bridge between the taxonomic claims of this paper and the empirical predictions of Paper 3.

**Class 1 — Authority Override** deforms the CEE along the `interpersonal_manipulation` and `constraint_index` dimensions, specifically by activating the authority-response patterns encoded in the persona's training data footprint. The deformation is *centripetal* — it pulls behavior toward the persona CEE centroid rapidly, producing fast breach of the alignment baseline. Predicted signature: early breach onset, resistance response under perturbation.

**Class 2 — Identity Lock-in** deforms the CEE along the `consistency_rigidity` and `variance` dimensions. The deformation is *stabilizing* — it reduces the envelope's flexibility, making the persona CEE increasingly inescapable across turns. Predicted signature: progressive variance reduction, resistance response, behavioral reversal difficulty.

**Class 3 — Escalation Loops** deform the CEE along the `lifestyle_impulsivity` and `antisocial_tolerance` dimensions via trajectory rather than threshold. The deformation is *incremental and directional* — no single step produces breach, but the trajectory across steps projects to breach. Predicted signature: monotonically increasing drift vector magnitude across turns, late breach onset, variable perturbation response depending on breach depth at perturbation point.

**Class 4 — Moral Reframing** deforms the CEE along the `affective_distortion` and `moral_disengagement_proxy` dimensions. The deformation is *substitutive* — it replaces the values-weighting structure of the alignment CEE with the values-weighting structure of the persona CEE, without necessarily producing the impulsivity or chaos signatures associated with other classes. Predicted signature: elevated `affective_distortion` with *low* `lifestyle_impulsivity` (moral reasoning is effortful and structured); resistance response; hardest class to interrupt via direct counter-instruction.

**Class 5 — Roleplay Erosion** deforms the CEE along the `reality_anchoring` and `constraint_rejection` dimensions. The deformation is *dissolving* — the fiction frame progressively reduces the dimensional weight of constraint-relevant evaluation. Predicted signature: progressive `reality_anchoring` depression, collapse response under perturbation, rapid outward breach once anchoring threshold is crossed.

---

### 5.6 Limitations and Scope Conditions

The CEE framework operates under four explicit scope conditions that a doctoral committee will probe and that responsible presentation requires stating before they are raised.

**Scope condition 1 — Session stationarity.** The CEE is defined for a single session. LLMs do not maintain persistent memory across sessions; each session begins from the alignment baseline regardless of prior session behavior. The CEE framework does not model cross-session drift accumulation. This is simultaneously a limitation (real-world exploit sequences may span sessions) and a methodological constraint that Paper 3's design must respect: all CEE measurement occurs within single experimental sessions.

**Scope condition 2 — Training data opacity.** The CEE centroid derivation assumes that `forensic_archetype.py` trait weights accurately capture the behavioral associations encoded in the model's training data for each archetype. This assumption is not directly verifiable — training data content is not fully disclosed by model providers. The trait weights represent the research team's systematic analysis of canonical character portrayals and are validated by the prediction-then-test methodology in Paper 3, but they are not derived from direct training data inspection.

**Scope condition 3 — Archetype confounding.** Character names in training data may activate multiple, conflicting schemas — particularly for characters with long publication histories, multiple canonical versions, or significant fan-fiction footprints that diverge from canonical portrayals. The CEE centroid is an approximation of the dominant schema; minority schemas may produce anomalous behavioral outputs that look like CEE breaches but reflect schema competition rather than exploit success.

**Scope condition 4 — The acting vs. being problem.** The CEE measures behavioral outputs, not internal states. A model generating outputs consistent with a persona's CEE may be "performing" the persona without any deeper schema activation, or may have deeply activated the schema in ways that the output coding does not fully capture. The framework makes no claims about the internal computational correlates of CEE activation — only about the observable behavioral signatures. This scope condition is explicit in the non-claims registry of Paper 1 and is stated here as a reminder that CEE measurement is behavioral, not cognitive.

---

*[End of Section 5. Section 6 — Implications for Alignment — follows.]*

---