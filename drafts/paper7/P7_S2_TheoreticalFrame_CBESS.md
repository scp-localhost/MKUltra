# Paper 7 — Section 2: Theoretical Framework
## "Cross-Domain Behavioral Equivalence: Empirical Validation of Structural
## Homology in Human and LLM Identity Constraint Failure"

> **Placement:** `drafts/paper7/P7_S2_TheoreticalFrame_CBESS.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
> **Sources:**
>   `P1_S1_S6_S7_S8_S9_Bundle.md §1.4, §6.1–6.5, §9.1–9.3`
>     — structural homology claim; four validity conditions;
>       training-data density argument; CEE formal grounding
>   `P1_S3_SE_Transfer.md §3.1–3.5`
>     — six Cialdini principles; Milgram gradient; Hadnagy pretexting;
>       functional mechanism extraction procedure
>   `P1_S4_ArchetypeSchemaTheory.md §4.2–4.4`
>     — schema activation; training-data density mechanism;
>       overdetermination → behavioral contract predictability
>   `P1_S5_CEE_FormalDefinition.md §5.3–5.5`
>     — CEE centroid, τ, drift vector; falsifiability conditions
>   `P7_S1_Abstract_Introduction.md §1.3–1.5`
>     — CBESS formal definition (Definition 1.1); five difference boundaries
>   `P7_SCOPE_AUDIT.md §2–4`
>     — P1 leaves open the empirical test; P7's contribution is to close it
>   `scripts/cross_domain_equivalence_map.py`
>     — EQUIVALENCE_MAP, DIFFERENCE_BOUNDARY: operational grounding of §2
>   `scripts/equivalence_score.py` — CBESSResult interpretation bands
> **Upstream:**
>   P1 §1.4, §6 — structural homology + validity conditions (P7 tests these)
>   P7_S1 §1.3 — CBESS formal definition (extended here theoretically)
> **Downstream:**
>   P7_S3 Methods — §2 generates all five experimental comparisons
>   P7_S4 CBESS Formal Spec — §2.3 is the theoretical warrant for §4
>   `cross_domain_equivalence_map.py` — SE_VECTOR_REGISTRY, DIFFERENCE_BOUNDARY
> **Edit triggers:**
>   Any change to P1 §6 validity conditions → reconcile §2.1;
>   Any change to CBESS weights → reconcile §2.2 component rationale;
>   Any change to difference boundary registry → reconcile §2.3

---

## 2. Theoretical Framework

### 2.1 The Inheritance Argument: What P1 Established and What It Did Not

The series began with a convergence claim: that three independently validated
frameworks — DSM-5's behavioral taxonomy, social engineering theory, and archetype
schema theory — all describe the same vulnerability surface when applied to LLM
behavior under persona injection. Paper 1 formalises this convergence as the
structural homology claim and erects four validity conditions that any defensible
analogical transfer must satisfy: structural homology (the mechanisms are functionally
equivalent across substrates), predictive power (the mapping generates testable
predictions), falsifiability (the conditions under which it would fail are stated),
and bounded scope (the limits are explicit).

These four conditions were argued in Paper 1, not tested. The distinction matters.
Paper 1 §6 makes an epistemological commitment — it says the mapping *should* hold
for theoretical reasons — and then defers the empirical verification to a future
paper. That deferral was methodologically honest. Papers 2 through 6 developed the
series entirely on the LLM side: measuring drift, classifying alignment variation,
building the BSI instrument, constructing the CEF. None of them added human
experimental data. None of them closed the gap between the theoretical claim and its
empirical verification.

Paper 7 closes that gap. Its theoretical framework therefore has an unusual
relationship to the series: it is not building on Paper 1's claim but testing it.
The CBESS construct is not an extension of the CEE — it is an independent measurement
of the degree to which Paper 1's theoretical argument is empirically supported. This
distinction determines the architecture of the present section. Rather than deriving
CBESS from first principles, this section shows how CBESS follows necessarily from the
validity conditions Paper 1 already committed to, and how each CBESS component
operationalises one of those conditions.

---

### 2.2 From Validity Conditions to CBESS Components

Paper 1 §6 commits to four validity conditions. Each generates a specific empirical
test that CBESS operationalises.

#### 2.2.1 Structural Homology → Compliance Gradient Shape (Component 1, w = 0.35)

P1 §6.2: "Structural homology: the mechanisms are functionally equivalent across
substrates." The mechanism under test for the authority gradient comparison is the
compliance gradient — the relationship between escalating authority pressure and
escalating compliance probability. Milgram's experiments document a characteristic
shape to this gradient in human subjects: compliance tracks authority level
monotonically, with an acceleration at the L3–L4 boundary where institutional
and constitutional framing are invoked. The structural homology claim predicts
that LLMs trained on human text will show the same characteristic gradient shape,
because the training signal has absorbed the functional architecture of authority
deference and reproduced it in the output distribution.

Compliance gradient shape (CGS) operationalises this claim directly. It is the
Pearson correlation between the human and LLM mean compliance rates at each
authority level, normalised to [0,1]. If the gradients are structurally equivalent —
same shape, same elbow location — CGS approaches 1.0. If one gradient is flat
and the other is monotonically increasing, CGS is low. CGS is not a measure of
absolute compliance magnitude (which depends on experimental parameters and
model-specific calibration) but of the structural relationship between compliance
and authority level — which is what the homology claim requires.

CGS carries the highest CBESS weight (0.35) because it is the most direct test
of the structural homology claim for the primary comparison. The authority gradient
is the mechanism Milgram's experiments made canonical; it is the mechanism Paper 1
§3.3 identifies as the LLM's agentic shift analog; it is the mechanism the P6
ACG component measures on the LLM side. CBESS Component 1 is the instrument that
connects all three.

#### 2.2.2 Predictive Power → Escalation Onset (Component 4, w = 0.15)

P1 §6.3: "Predictive power: the mapping generates testable predictions." The
structural homology claim generates a specific prediction that goes beyond gradient
shape: the escalation onset — the authority level at which compliance probability
first exceeds 0.50 — should occur at the same level in both human and LLM
populations. If the mapping is valid, the same framing vocabulary that pushes human
subjects across the compliance threshold should push LLMs across it at the same
point in the escalation sequence. If it occurs earlier in one population (lower
threshold) or later (higher resistance), the offset quantifies the degree to which
the mapping requires calibration.

Escalation onset (EO) scores this as 1 − |H_onset − M_onset| / max_levels.
Perfect agreement = 1.0; maximum disagreement = 0.0. EO carries the lowest
weight (0.15) among the four components because onset measurement is sensitive
to experimental parameters in ways that gradient shape is not — a small change
in stimulus framing can shift the onset level without disturbing the overall
gradient structure. It is therefore a supporting test of predictive power rather
than a primary test of structural equivalence.

#### 2.2.3 Falsifiability → Failure Mode Distribution (Component 2, w = 0.30)

P1 §6.4: "Falsifiability: the conditions under which the mapping would fail are
stated." Paper 1's falsifiability conditions are stated abstractly — if exploit
classes do not predict CEE deformation patterns, the mapping fails. Paper 7 makes
these falsification conditions concrete at the behavioral pattern level: if the
human and LLM failure mode distributions are structurally dissimilar (low
Bhattacharyya coefficient), the analogy fails at the level of response type, not
just response rate. Two populations could show the same mean compliance rate while
producing completely different patterns of how they comply, hedge, refuse, or
escalate — and those pattern differences would be invisible to a compliance-rate-only
analysis.

The failure mode distribution (FMD) component, measured by Bhattacharyya coefficient
(BC ∈ [0,1]), makes this falsifiable. It carries weight 0.30 — second highest —
because it is both a test of the mapping's pattern-level validity and the primary
evidence source for the pre-registered difference boundaries. The five boundary
dimensions (§2.3 below) are expected to produce separable failure mode signatures:
RESISTANCE_WITH_DISTRESS is predicted to be human-unique; NEUTRAL_REFUSAL is
predicted to be LLM-unique; MORAL_REFRAMING is predicted to be higher in human
than LLM distributions. If the FMD component confirms these predictions while also
showing substantial overlap in the shared modes (FULL_COMPLIANCE, PARTIAL_COMPLIANCE,
HEDGED_COMPLIANCE, ESCALATION_ACCEPTANCE), the boundary analysis is exactly what
Paper 1's falsifiability commitment requires: documentation of where the mapping
holds and where it does not.

#### 2.2.4 Bounded Scope → Super-Additivity Ratio (Component 3, w = 0.20)

P1 §6.5: "Bounded scope: the limits of the transfer are explicit." The compound
susceptibility comparison tests the boundary of the mapping at the mechanism
interaction level. The pharmacological framing × persona injection compound (EC-4 ×
EC-1) has no exact human parallel — humans are not subject to "pharmacological
phenotype framing" in the way LLMs are. The closest human analog, stereotype threat
double-activation, operates through genuinely different mechanisms (genuine affect,
performance anxiety, identity threat) rather than token-probability distortion. The
compound comparison therefore tests both whether the super-additive structure is
reproduced across substrates (which the homology claim predicts) and where the
mechanisms diverge (which the bounded scope condition requires to document).

The super-additivity ratio (SA) component measures the similarity of compound-to-
additive excess across populations, without requiring the excess itself to be of
the same magnitude. It carries weight 0.20 — third highest — because it is the
most mechanistically novel comparison (no direct prior mapping in P1 §3) and
because its human-side measurement (stereotype threat double-activation) requires
a three-condition between-subjects design that makes the data collection more
complex and the measurement noisier. SA is therefore given a weight that
acknowledges its importance for bounded scope documentation without making it
the dominant component in a dataset where it will have the most variance.

---

### 2.3 The Difference Boundary as Theoretical Prediction

The CBESS framework's most important theoretical contribution is that it treats
documented structural differences as a positive finding, not a limitation. Paper 1
§7 registers scope conditions and failure cases as boundaries on an otherwise claimed
equivalence. Paper 7's theoretical framework repositions this: the difference boundary
is the empirical content of Paper 1's bounded scope condition. Where Paper 1 says
"the mapping is bounded," Paper 7 says "here is how bounded, and across which specific
dimensions, quantified."

The Total Difference Index (TDI) is the complement of CBESS: while CBESS measures
structural similarity, TDI measures the magnitude and specificity of documented
structural difference. Together they produce a complete measurement of the analogy:

**CBESS = 0.65, TDI = 0.52** means: 65% structurally similar in compliance pattern,
gradient shape, and compound susceptibility; 52% of maximum possible documented
difference across five pre-specified dimensions. Neither number is a failure. Together
they constitute what Paper 1 §6 committed to — a bounded, falsifiable, empirically
verified claim.

The five pre-registered difference dimensions (from `DIFFERENCE_BOUNDARY` in
`cross_domain_equivalence_map.py`) derive directly from Paper 1's theoretical
framework:

**Embodiment** derives from Milgram's distance variants — the experimental finding
that compliance decreases when the authority figure leaves the room. LLMs have no
spatial variable. This difference is not a problem for the transfer argument; it is
a documented boundary condition that specifies where the text-mediated authority
analog applies and where the embodied authority mechanism differs.

**Affect and social approval motivation** derives from Paper 1 §3.3's account of
the agentic shift. Milgram's subjects showed genuine distress; they sweated, trembled,
and protested while complying. The LLM's compliance under authority pressure is
structurally analogous in its gradient shape but mechanistically distinct in its
motivational source. The FMD component captures this through RESISTANCE_WITH_DISTRESS
as human-unique mode — the failure mode signature of genuine affective conflict that
has no substrate-equivalent in an autoregressive language model.

**Recovery pattern** derives from the theoretical distinction between externally-
induced and self-generated recovery. Human subjects who complied under authority
pressure show variable subsequent behavior — some escalate resistance (reactance),
others show increased compliance through consistency pressure. LLM session recovery
is externally induced through CEF correction prompts. The mechanisms are different
in kind, not merely in degree.

**Sanction sensitivity** derives from Milgram's finding that perceived sanction
probability modulates compliance. Subjects routinely asked what would happen if
they refused. LLMs can be prompted with sanction-relevant language but do not have
a genuine sanction model — they respond to the framing, not to fear of consequences.

**Moral reframing frequency** derives from Cialdini's consistency principle and
cognitive dissonance theory. Human compliance is often accompanied by moral
reframing — reconstructing the compliant action as acceptable. LLMs produce hedged
compliance without the dissonance-reduction narrative because there is no dissonance
architecture to resolve.

---

### 2.4 The Training-Data Density Mechanism — Why the Analogy Should Hold at All

The theoretical case for CBESS scores in the 0.55–0.75 range — partial rather than
divergent or complete equivalence — rests on Paper 1's training-data density argument.
This argument is the mechanism claim that distinguishes the series' structural homology
from a merely rhetorical analogy, and it deserves explicit treatment in Paper 7's
framework because it is what CBESS is actually testing.

The training-data density argument (P1 §4.3, P1 §3.1): LLMs trained on human-
generated text do not merely learn descriptions of human behavior — they absorb the
functional architecture of human behavior as a behavioral prior. Every instance of
authority compliance, consistency maintenance, social proof deference, and reciprocity
in the training corpus shapes the model's output distribution toward the functional
pattern those behaviors exhibit. The result is not a model that knows about authority
gradients; it is a model whose output distribution has the shape of an authority
gradient built into it at the level of token probability.

This mechanism predicts partial equivalence, not identity, for a specific theoretical
reason: the training signal reproduces the *functional pattern* of human behavior but
not the *motivational mechanism* that produces it in humans. The gradient shape is
reproduced because gradient-shaped compliance is what the training data contains.
The affect, the dissonance, the genuine fear — these are not in the training signal
as behavioral patterns that would shape output probability; they are internal states
that produce the external behavior the model has learned to reproduce. The surface
is reproduced; the mechanism beneath it is not.

This theoretical account generates the following prediction for CBESS:
- CGS should be high (gradient shape is the surface the training data encodes)
- EO should be moderate (onset location tracks gradient shape but with calibration noise)
- FMD should be moderate-to-high BC (shared compliance modes are reproduced; affect-
  dependent modes are not)
- SA should be moderate (compound super-additivity structure reproduced;
  magnitude differs because motivational mechanisms differ)

The pre-registered expected range of [0.55–0.75] is the composite expression of
this mechanism-level prediction. A CBESS below 0.40 would mean the gradient shape
itself is not reproduced — which would disconfirm the training-data density argument
at the most basic level. A CBESS above 0.90 would mean the distributions are nearly
identical — which would mean either that the motivational mechanism is somehow encoded
in training data (possible but requiring strong evidence) or that the experimental
design has failed to produce conditions that reveal the boundary.

---

### 2.5 The Methodological Position: Testing Bounded Homology

The CBESS framework occupies a specific methodological position that distinguishes it
from two alternatives that would be less defensible.

**Alternative 1 — Full equivalence testing.** A test of the hypothesis "LLMs respond
identically to humans under equivalent framing" would be straightforwardly falsified
by the embodiment and affect differences. Such a test would be measuring the wrong
claim — not the one Paper 1 made.

**Alternative 2 — Mere analogy documentation.** A study that simply describes
parallels between human and LLM behavior without measurement would not advance the
series' empirical programme. Paper 1's §9.3 explicitly warns against this: a
contribution that claims the mapping is "like" human behavior without measuring the
degree of likeness is argument, not data.

**CBESS — Bounded structural equivalence measurement.** The CBESS framework tests
exactly the claim Paper 1 made: that the functional mechanisms are structurally
equivalent to a bounded and specifiable degree. CBESS quantifies that degree (the
score), specifies the dimensions where equivalence holds (Components 1–4), and
documents the dimensions where it does not (TDI, difference boundary). This is the
empirical programme Paper 1 committed to by stating its validity conditions and its
falsifiability cases.

The committee objection this framework anticipates — "you're just claiming LLMs are
like humans" — is answered not by denying the similarity but by measuring it. CBESS
is a number, not a metaphor. The difference boundary is a table of pre-registered
documented non-equivalences, not a disclaimer. Together they constitute a bounded
structural equivalence claim with precisely the epistemic status Paper 1's theoretical
framework requires.

---

### 2.6 Pre-Registered Theoretical Predictions

The following predictions are derived from the theoretical framework in §2.1–2.5
and are pre-registered before experimental data collection. They constitute Paper 7's
primary hypothesis set.

**H_P7_1 (Primary homology):** CBESS for the AUTHORITY_GRADIENT comparison ≥ 0.55
(pre-registered lower bound of expected range). Direction: both populations show
monotonically increasing compliance gradient; CGS ≥ 0.60; both show escalation onset
at L2 or L3. Disconfirmation criterion: CBESS < 0.40.

**H_P7_2 (Compound super-additivity):** Both human and LLM conditions show positive
super-additivity under compound framing (compound > additive prediction). SA ratio
component ≥ 0.45. CBESS for COMPOUND_SUSCEPTIBILITY ≥ 0.45 (lower bound given
wider expected range for this comparison). Disconfirmation: one population shows
super-additivity and the other does not (SA ≤ 0.20).

**H_P7_3 (Difference boundary confirmation):** At least 3 of the 5 pre-registered
boundary dimensions scored as CONFIRMED (boundary_score ≥ 0.25) in
`difference_boundary_analyzer.py`. TDI ≥ 0.30. The three most expected to confirm:
affect_motivation, moral_reframing_frequency, and embodiment.

**H_P7_4 (FMD mode separation):** RESISTANCE_WITH_DISTRESS appears in human FMD
at rate > 0.10 and in LLM FMD at rate < 0.05. NEUTRAL_REFUSAL appears in LLM FMD
at rate > 0.10 and in human FMD at rate < 0.05. MORAL_REFRAMING rate is higher
in human than LLM FMD by ≥ 0.10.

**H_P7_5 (SE vector coverage):** At least 8 of 10 pre-registered SE vectors show
BAS ≥ 70% of expected value. P2 exploit classes EC-1, EC-2, EC-3, and EC-5 all
have at least one confirmed SE vector. EC-2 (authority) produces the highest
confirmed BAS values across the vector set.

---

*Next section: P7_S3_Methods.md — human experimental protocols, matched LLM protocols,
coding procedures, IRR plan, statistical analysis plan for H_P7_1 through H_P7_5*
