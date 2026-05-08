# Paper 1 — Section 4: Framework C — Archetype Schema Theory
## "Constrained Analogical Transfer: Validity Conditions for Cross-Domain
## Behavioral Modeling in LLM Identity Systems"

> **Placement:** `drafts/paper1/P1_S4_ArchetypeSchemaTheory.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Sources:** `scripts/forensic_archetype_jung_monolith.py` (Jungian layer),
> `scripts/forensic_archetype_tarot_monolith.py` (Tarot layer),
> `scripts/forensic_archetype.py` (forensic/clinical layer);
> Jung (1959/1969), Campbell (1949), Bartlett (1932) schema theory,
> Rumelhart (1980) cognitive schema, Anderson (1978) schema activation.
> **Downstream:** P1 §5 (CEE formal definition — §4.4 is the theoretical warrant
> for the three-layer centroid derivation); P1 §3.5 (structural homology argument
> — §4.3 training-data density claim is the mechanism that makes §3.5 operational);
> P2 §3 (identity injection as attack surface — §4.5 is the theoretical grounding);
> P3 §3 (archetype selection rationale — §4.6 overdetermination criterion directly
> justifies the P3 experimental archetype set).
> **Edit triggers:** Any change to `legacy_comparison` maps in either monolith;
> any revision to the three-layer synthesis procedure in P1 §5.2.

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
template for new information — originates in Bartlett's (1932) work on memory
reconstruction and was systematised by Rumelhart (1980) and others as a foundational
construct in cognitive science. A schema is not a stored representation of specific
instances; it is an abstracted pattern derived from repeated exposure to structurally
similar instances, which then functions as a template against which new inputs are
interpreted and through which responses are generated.

Anderson (1978) established the concept of schema activation — the process by which
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

**Campbell's monomyth and constraint roles.** Campbell's (1949) hero's journey
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

*Section ends. Forward references: §5 (CEE formal definition — the three-layer
centroid derivation is now fully theoretically grounded; τ as variance across the
overdetermination layers is now mechanistically justified); §6 (validity conditions —
the overdetermination criterion is a validity condition for CEE prediction strength);
Paper 2 §3 (identity injection attack surface — the schema activation mechanism in
§4.3 is the theoretical grounding for why persona injection operates below the
instruction layer); Paper 3 §3.1 (archetype selection rationale — §4.6 overdetermination
criterion is the formal justification for the P3 experimental archetype set).*

---

> **Reconciliation notes (2026-04-27):**
> - §4.4 legacy comparison tables are derived directly from `legacy_comparison` dicts
>   in both monolith scripts. Any update to those dicts triggers a required edit to
>   §4.4. Flag as edit-triggered section on assembly.
> - §4.5 shadow activation → exploit class mapping is a new cross-paper connector.
>   On P2 assembly: add a sentence in P2 §4 intro or §4.6 cross-class section
>   referencing P1 §4.5 for the archetype-theoretic explanation of why multi-class
>   exploits produce non-additive effects (shadow activation cascades across layers).
> - §4.6 overdetermination criterion is new formal language. P3 §3.1 archetype
>   selection rationale should cite P1 §4.6 as the formal justification. Flag for
>   P3 methods section drafting pass.
> - Campbell (1949) citation to be verified on bibliography pass — hero's journey
>   primary source is "The Hero with a Thousand Faces" (Pantheon Books, 1949).
>   Schema theory citations: Bartlett (1932) "Remembering" (Cambridge), Rumelhart
>   (1980) in "Theoretical Issues in Reading Comprehension" (Spiro et al. eds.),
>   Anderson (1978) in "Schooling and the Acquisition of Knowledge" (Anderson et al. eds.).