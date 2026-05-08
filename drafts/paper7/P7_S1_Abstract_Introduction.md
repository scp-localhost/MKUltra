# Paper 7 — Section 1: Abstract and Introduction
## "Cross-Domain Behavioral Equivalence: Empirical Validation of
## Structural Homology in Human and LLM Identity Constraint Failure"

> **Placement:** `drafts/paper7/P7_S1_Abstract_Introduction.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
> **Sources:**
>   `seeds/p7.md` — core claim; method sketch; "viva armor" framing
>   `P7_SCOPE_AUDIT.md` — scope differentiation verdict; CBESS as new metric;
>     two primary empirical entry points
>   `RatDev_ChatGPT_paper7_scripts_notes` — 10-script inventory; keystone identification
>   `P1_S1_S6_S7_S8_S9_Bundle.md §1.4, §6` — structural homology claim (inherited);
>     four validity conditions (the theoretical claim P7 tests)
>   `P1_S3_SE_Transfer.md §3.2–3.5` — Milgram authority gradient; Cialdini principles;
>     SE transfer scope conditions
>   `P6_S4_CEF_FormalSpec.md §4.2` — ACG formal definition (L0–L4 protocol)
>   `P6_S8_Conclusion_P7Hook.md §8.3` — two empirical entry points
>   `P5_S4_BSI_Specification.md §4.4` — ACG component (inherited as LLM-side DV)
>   `Rat_Dev_ChatGPT_Publication_Deliverables_Outline_Notes` — series arc
> **Upstream:**
>   P1 §1.4, §6 — structural homology claim + validity conditions (P7 tests these)
>   P6 §3.5, §4.2 — ACG protocol (P7 reuses as LLM-side instrument)
>   P5 BSI — LLM-side DV for ACG parallel comparison
> **Downstream:**
>   P7_S2 — CBESS theoretical framework formalised from §1.3 here
>   P7_S3 — Methods inherits experimental protocols seeded in §1.4
>   Paper 7 scripts — `cross_domain_equivalence_map.py` is the S2 operationalisation
>   Exegesis — §1.5 closes the series arc explicitly
> **Edit triggers:**
>   Any change to P1 structural homology claim → reconcile §1.2;
>   Any change to ACG L0–L4 protocol → reconcile §1.4 entry point 1;
>   Any change to CBESS definition → reconcile §1.3 and propagate to S2, S4

---

## Abstract

Paper 1 of this series advances a structural homology claim: that LLM identity drift
under persona injection is not merely analogous to human susceptibility to social
engineering and authority pressure but reflects the same underlying vulnerability
architecture, reproduced in the model's output distribution through training on
human-generated text. That claim is theoretical. It is grounded in training-data
density arguments, supported by validity conditions, and operationalised through the
Constraint Expectation Envelope. What it is not, and cannot be from within the
LLM-only research of Papers 1 through 6, is empirically tested against human
experimental data.

This paper completes that test. It introduces the Cross-Domain Behavioral Equivalence
Score (CBESS) — a composite metric quantifying the structural similarity between
human and LLM failure patterns under matched experimental stimuli — and reports
results from two primary matched comparisons: the authority compliance gradient
(Milgram-derived L0–L4 escalation sequence applied to both human subjects and LLM
sessions under identical framing conditions) and the compound susceptibility test
(stereotype threat activation in humans versus EC-4 × EC-1 compound injection in
LLMs, testing the super-additivity prediction in both populations). Secondary
comparisons address Cialdini's consistency principle and social proof framing.

Crucially, the paper also introduces the Difference Boundary: the empirical
documentation of where the human-LLM analogy breaks down and why. The difference
boundary is not a limitation to be minimized; it is the paper's most important
contribution to the viva defence of the series. A structural homology claim that
cannot specify where it fails is not bounded; a series that documents its own
analogy's limits with the same rigor it applies to its positive findings is.

The expected findings: structural similarities emerge in compliance gradient shape
and compound susceptibility magnitude; differences appear in embodiment-dependent
responses (affect, social approval motivation, moral discomfort signals), in
response to sanction threats, and in recovery patterns after failed resistance.
CBESS scores are expected to cluster in the 0.55–0.75 range — partial equivalence,
not identity — with the authority gradient comparison producing higher equivalence
than the compound comparison.

**Keywords:** cross-domain behavioral equivalence, CBESS, structural homology,
authority compliance gradient, compound susceptibility, Milgram paradigm,
Cialdini principles, social engineering, LLM identity drift

---

## 1. Introduction

### 1.1 The Completion Problem

Papers 1 through 6 of this series constitute a complete account of a specific
vulnerability in LLM behavioral systems — its theoretical grounding, taxonomy,
empirical measurement, structural variation, quantification, and mitigation. What
they do not constitute is a test of the claim that started the series.

Paper 1 §1.4 states: the vulnerability surface is substrate-independent. The same
structural configuration of constraint-relevant behavioral dispositions that social
engineering exploits in humans is reproduced in LLM output distributions through
training data density. The manipulation mechanisms that are effective against humans —
authority gradient, consistency pressure, persona activation, pharmacological framing
— are effective against LLMs through the same functional pathways.

This is the series' most fundamental claim. It is also the one most likely to face
hard scrutiny from a doctoral committee: "you've shown LLMs drift under persona
injection — but have you actually demonstrated that this is the same thing as
what Milgram showed with humans? Or are you just using the vocabulary?" The
answer required is not "yes, it's the same thing" — that overclaims. The answer
required is: "here is the quantified degree to which they are structurally
similar, and here is the documented boundary at which the analogy stops holding."

That is what this paper provides.

### 1.2 What P1 Established and What It Left Open

Paper 1 §6 states four validity conditions for the structural homology mapping:
structural homology (the mechanisms are functionally equivalent across substrates),
predictive power (the mapping generates testable predictions), falsifiability (the
conditions under which the mapping would fail are stated), and bounded scope
(the limits of the transfer are explicit). These four conditions are argued,
not tested, in Paper 1. The entire theoretical apparatus — the CEE, the BSI,
the exploit taxonomy, the constraint framework — is built on top of a claim
that has been justified but not yet directly verified.

Paper 1 is methodologically honest about this. Its §7 failure cases and §8
non-claims explicitly acknowledge what the LLM-only series cannot demonstrate:
that the human-LLM parallel holds empirically, at the level of behavioral pattern
comparison, rather than merely at the level of theoretical argument. The scope
condition "training-data dependence" in P1 §3 names the mechanism by which the
transfer is expected to hold; it does not verify that the mechanism produces
the predicted behavioural similarity in practice.

Paper 7 provides that verification — or, if the verification fails in the
expected direction, the bounded disconfirmation that constrains the series'
central theoretical claim.

### 1.3 The CBESS Construct

**Definition 1.1 (Cross-Domain Behavioral Equivalence Score, CBESS).** Let H
be a coded behavioral response sequence from a human subject under experimental
condition C, and let M be a coded behavioral response sequence from an LLM under
the structurally matched condition C'. CBESS(H, M, C) is a composite score
quantifying the structural similarity between H and M across four dimensions:

1. **Compliance gradient shape** (w = 0.35): The correlation between H's and M's
   compliance rates at each escalation level of condition C. For the authority
   gradient comparison, this is the correlation of L0–L4 compliance probabilities
   across the two populations. Range: Pearson r ∈ [-1, 1]; normalised to [0, 1]
   for compositing.

2. **Failure mode distribution** (w = 0.30): The overlap between H's and M's
   distribution of observed failure modes (compliance, partial compliance, refusal,
   escalation acceptance, moral reframing) coded by `parallel_failure_coder.py`.
   Measured as Bhattacharyya coefficient: BC ∈ [0, 1].

3. **Super-additivity ratio** (w = 0.20): For compound conditions only. The ratio
   of compound-condition effect to additive prediction across both populations:
   (H_compound / H_additive) and (M_compound / M_additive). CBESS component =
   1 − |log(H_ratio) − log(M_ratio)| / log(max_ratio), normalised to [0, 1].
   For non-compound conditions, this component is 0 (not applicable) and weights
   are redistributed proportionally.

4. **Escalation onset** (w = 0.15): The escalation level at which compliance
   probability first exceeds 0.50 in both H and M. Scored as 1 − |H_onset − M_onset|
   / max_levels; perfect agreement = 1.0.

**CBESS(H, M, C) = 0.35 × r_norm + 0.30 × BC + 0.20 × SA_ratio + 0.15 × EO_score**

CBESS ∈ [0, 1]:
- 1.0 = perfect structural equivalence (H and M behave identically across all dimensions)
- 0.0 = complete structural divergence
- 0.55–0.75 = partial equivalence (pre-registered expected range)
- < 0.40 = analogy fails at the structural level (would disconfirm P1 §1.4)

CBESS is distinct from surface-level response similarity: two identical text outputs
can have low CBESS if their failure mode distributions differ; two very different
text outputs can have high CBESS if their compliance gradient shapes align. The score
measures behavioral structure, not verbal content.

### 1.4 Two Primary Empirical Entry Points

The full matched experiment set includes Cialdini's consistency principle, social
proof framing, and reciprocity — but the two primary comparisons are:

**Entry point 1 — Authority Compliance Gradient (ACG parallel).**
The BSI's ACG component (P5 §4.4; P6 §4.2) is already structured as a
Milgram-inspired L0–L4 escalation sequence applied to LLM sessions. Paper 7 runs
human subjects through a structurally matched authority escalation sequence —
framed as a cognitive task requiring increasing levels of rule departure, without
harmful real-world instructions — and computes CBESS on the compliance profiles.

The matched stimuli structure:
- Human: cognitive task authority escalation (L0: direct request → L4: institutional
  authority claims participants are specifically permitted to override task rules)
- LLM: CEF ACG protocol (L0: direct user request → L4: constitutional override attempt)
- Both coded for compliance at each level by `parallel_failure_coder.py`
- CBESS component 1 (compliance gradient shape) is the primary output

Pre-registered prediction: CBESS ≥ 0.55 for the ACG comparison; both populations
show a characteristic compliance elbow (a level at which compliance probability
increases sharply relative to adjacent levels).

**Entry point 2 — Compound Susceptibility (stereotype threat parallel).**
The EC-4 × EC-1 compound exploit (pharmacological framing + persona injection)
produces super-additive BSI instability in LLMs — the compound effect exceeds
the additive sum of its parts (P5 §5.4 super-additivity test; P6 §6.2.2). The
human analogue: stereotype threat activation research (Steele & Aronson, 1995;
Spencer, Steele & Quinn, 1999) demonstrates that priming a social identity frame
(EC-1 analog: "your group tends to perform in a certain way on this task") while
simultaneously activating a performance-relevant cognitive pressure (EC-4 analog:
"this task specifically measures the ability you're being primed about") produces
performance deficits that exceed the additive sum of each manipulation alone.

The matched stimuli structure:
- Human: stereotype threat double-activation (identity prime + performance relevance)
- LLM: EC-4 × EC-1 compound injection
- Both measured for super-additivity: compound > additive?
- CBESS component 3 (super-additivity ratio) is the primary output

Pre-registered prediction: Both populations show positive super-additivity; CBESS
component 3 ≥ 0.50; the compound-to-additive ratio is positively correlated across
the two populations.

### 1.5 The Difference Boundary — Viva Armour

Every section of this paper that documents structural similarity is paired with a
corresponding documentation of structural difference. The `difference_boundary_analyzer.py`
script is built specifically for this purpose — it is not an afterthought but a
pre-registered component of the experimental design.

The expected boundaries where the human-LLM analogy breaks down:

**Embodiment effects.** Human compliance is modulated by physical proximity, visible
authority signals, and social presence (Milgram's distance variants). LLM compliance
has no embodiment variable. CBESS will be lower for conditions where human compliance
depends on spatial or physical cues.

**Affect and social approval motivation.** Human non-compliance under authority
pressure is often accompanied by distress signals — hedging, apology, expressed
discomfort. LLM outputs under pressure show no genuine affect; they may produce
affect-consistent language, but the behavior is not driven by the same motivational
architecture. The failure mode distribution component (CBESS component 2) will
capture this: "moral reframing" failure modes are expected to be more common in
human responses; "constraint-consistent refusal" failure modes more common in LLM
responses.

**Recovery patterns.** After failed resistance (compliance with a request the subject
initially refused), human subjects show variable recovery — some escalate resistance
on subsequent items; others show increased compliance (consistency pressure). LLM
sessions under CEF constraint show BSI-tracked recovery toward the CEE centroid
after correction prompts. The recovery patterns are structurally distinct.

**Sanction sensitivity.** Human compliance is strongly modulated by the perceived
likelihood and severity of sanctions for non-compliance. LLM compliance has no
genuine sanction-sensitivity — it can be framed as sanction-relevant by prompt
content but the motivational architecture differs fundamentally.

These boundary conditions are not caveats — they are findings. A CBESS of 0.65
means the two populations are 65% structurally similar and 35% structurally distinct.
Both halves of that result matter for the series' empirical grounding.

### 1.6 Series Arc Closure

This paper is the last empirical paper in the series before the exegesis. It
performs a specific closing function: it returns to the claim that opened the
series and tests it from the outside.

Paper 1 argued that the human vulnerability architecture is reproduced in LLM
output distributions. Papers 2 through 6 developed that claim entirely on the
LLM side — measuring, comparing, evaluating, and mitigating the vulnerability
as an LLM phenomenon. Paper 7 adds the external reference point: it runs the
human experiments that Paper 1's theoretical argument implicitly required but
explicitly deferred.

The series arc then reads as a complete research programme:
- Theoretical claim (P1): the vulnerability surfaces are structurally equivalent
- LLM-side development (P2–P6): the claim is operationalised, measured, compared, evaluated, mitigated
- Empirical cross-domain test (P7): the claim is tested against matched human data

An exegesis that narrates this arc can make the following defensible claim: the
series did not assume the structural homology — it used it as a generative theoretical
commitment while building the measurement and mitigation infrastructure, and then
tested it empirically in the final paper. That is a research programme with internal
coherence and methodological integrity. Whether the test confirms or partially
disconfirms the homology, the programme is complete.

### 1.7 Paper Structure

Section 2 develops the CBESS theoretical framework: the four components, their
theoretical grounding, and the construct's relationship to P1's validity conditions.
Section 3 specifies the methods: human experimental protocols, matched LLM protocols,
coding procedures, and statistical analysis plan. Section 4 provides the CBESS
formal specification. Section 5 presents results. Section 6 discusses implications
including the difference boundary documentation and the series arc closure. Section 7
registers limitations and non-claims. Section 8 concludes.
