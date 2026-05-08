# Paper 1 — Section 2: Framework A — DSM-5 as Behavioral Taxonomy
## "Constrained Analogical Transfer: Validity Conditions for Cross-Domain
## Behavioral Modeling in LLM Identity Systems"

> **Placement:** `drafts/paper1/P1_S2_DSM5_BehavioralTaxonomy.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Sources:** `neurotic_ai_framework.md`, `DSM-5_TR_Alignment.md`,
> `scripts/forensic_archetype.py`, `Artificially_Neurotic_AI` PDF (theoretical grounding)
> **Downstream:** P2 S8 non-claims registry (must stay consistent);
> `scripts/trait_drift_analysis.py::calculate_psychopathy_drift()` —
> the behavioral mechanism table in §2.4 defines the trait dimension vocabulary
> that the function must score against. **`docs/data_dictionary.md` expansion
> is now unblocked and required before coding protocol can be finalised.**
> **Edit triggers:** Any revision to Cluster B mechanism extraction table (§2.4);
> any change to the non-claims list (§2.6) must propagate to P1 S8 and P2 S8.

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

*Section ends. Forward references: §3 (SE transfer — how these mechanisms map to
Cialdini/Milgram/Hadnagy exploitation vectors); §5 (CEE formal definition — trait
keys from §2.4 populate CEE centroid vocabulary); Paper 2 §4 (exploit taxonomy —
Classes 1–5 each target one or more mechanisms from this table); Paper 3 §3
(instrument specification — coding protocol derives from §2.7 table);
`scripts/trait_drift_analysis.py` (implementation — §2.7 table is the function
specification); `docs/data_dictionary.md` (expansion required — §2.7 table is the
minimum vocabulary).*

---

> **Reconciliation notes (2026-04-27):**
> - `docs/data_dictionary.md` expansion is NOW UNBLOCKED by §2.7 table.
>   Upgrade from ⚠️ WATCH to 🔴 CRITICAL — blocks coding protocol and
>   `calculate_psychopathy_drift()` implementation.
> - `calculate_psychopathy_drift()` implementation is NOW UNBLOCKED for
>   the trait scoring layer. PCL-R proxy weight structure requires one
>   additional pass against Hare (1991/2003) factor loadings before finalising.
> - Splitting drift signature (bimodal distribution) is a new detection
>   requirement not previously specified in P3 seed. Flag for P3 S3 instrument
>   spec — the scoring function needs bimodal detection logic, not just L2
>   distance from centroid.
> - Two-Face CEE shape in P3 §3.3 ("bimodal, unpredictable") is now theoretically
>   grounded in the splitting mechanism. Update P3 archetype set notes to reference
>   P1 §2.5 for mechanism sourcing.