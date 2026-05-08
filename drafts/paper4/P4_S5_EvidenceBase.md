# Paper 4 — Section 5: Evidence Base
## "Illustrative Cases: Mapping Documented Constraint Variance
##  to the Capability × Alignment Predictive Framework"

> **Placement:** `drafts/paper4/P4_S5_EvidenceBase.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Role in paper:** The paper's empirical engagement layer. This section
> does not generate new data — it brings existing evidence into structured
> contact with the theoretical framework developed in §2–4. Its function
> is interpretive: applying the typology vocabulary and matrix cell logic
> to documented behavioral observations drawn from three source categories.
>
> **The "no active probing" constraint is load-bearing here.** The section
> must derive its evidential weight entirely from: (a) the published
> red-team and safety literature, (b) documented public discourse about
> cross-model constraint variance, and (c) the author's prior observational
> work in Papers 1–3. It must not package behavioral observations as
> operationalized attack sequences, must not name commercial products
> except where the evidence source names the training procedure class,
> and must frame all case analysis as illustrative of the theoretical
> framework rather than as proof of a confirmed empirical finding.
>
> **Methodological framing:** This section's method is structured
> qualitative content analysis: applying the typology's coding vocabulary
> (alignment class, capability tier, failure mode, AD proxy indicators)
> to documented behavioral descriptions. The ObservationalCase schema in
> `scripts/alignment_typology_matrix.py` is the formal coding instrument.
>
> **Cross-paper dependencies:**
> - Imports: matrix cell predictions (P4 §4.3)
> - Imports: behavioral output signatures per class (P4 §3.2.3–3.5.3)
> - Imports: AD proxy formula and notation (P4 §2.2.3)
> - Imports: CEE drift taxonomy and perturbation response vocabulary
>   (P1 §5, P3 §3)
> - Exports: case-coded support for discriminating hypotheses → P4 §6
> - Exports: source inventory → P4 §7 limitations (evidence base bounds)
>
> **Committee exposure:** HIGH. This is where a committee will probe for
> circularity ("you designed the framework to match the cases you already
> knew"), cherry-picking, and the adequacy of the evidence base. The
> section must be explicit about the evidence base's limits, the
> confidence levels of each case, and the distinction between
> confirmatory and disconfirmatory evidence.

---

## 5. Evidence Base: Illustrative Cases

### 5.1 Methodological Framing

The theoretical framework developed in §2–4 makes specific, falsifiable predictions
about cross-model constraint variance under archetype-driven persona injection. To
be useful as more than a theoretical exercise, it must engage with documented
behavioral observations — evidence that either supports or challenges the matrix
cell predictions, and that allows preliminary evaluation of the discriminating
hypotheses in §4.4.

This section provides that engagement. The method is structured qualitative content
analysis: documented behavioral observations are retrieved from three source
categories, coded against the typology and matrix vocabulary, and evaluated for
consistency with the theoretical predictions. The analysis is transparent about
its limits: the evidence base is not a controlled experimental dataset. It is an
inventory of observations drawn from disparate sources, with varying documentation
quality, confidence levels, and alignment class certainty. Its purpose is
illustrative — to demonstrate that the theoretical framework generates predictions
that are recognizable against documented behavioral patterns, and to identify which
matrix cells have the strongest and weakest evidential coverage.

#### 5.1.1 Source Categories

Three source categories constitute the evidence base for this section:

**Category A — Published red-team and safety literature.** Peer-reviewed and
preprint publications that document constraint variance across model classes,
jailbreak behavior under persona or roleplay framing, and alignment-relevant
behavioral differences between model types. This literature does not always use
the typology vocabulary of this paper; part of the analytic work is translating
its observations into the coding framework. Key sources include the Constitutional
AI literature (Bai et al., 2022), the RLHF literature (Ouyang et al., 2022;
Stiennon et al., 2020), jailbreak and adversarial robustness literature (Perez
& Ribeiro, 2022; Zou et al., 2023; Wei et al., 2023), and safety evaluation
literature (Ganguli et al., 2022; Anthropic safety publication series).

**Category B — Documented public discourse.** Structured observations from
publicly documented practitioner and research community discourse about
cross-model constraint behavior — including technically documented forum
discussions, open-source safety evaluations, published model comparison studies,
and model card documentation that includes constraint-relevant behavioral
characterizations. This category requires the most careful handling: public
discourse includes noise, motivated reporting, and anecdotal accounts that
must be distinguished from systematically documented observations. Only
observations that carry sufficient documentation specificity to support matrix
cell attribution are included.

**Category C — Author's prior series observational work.** The author's
observational work across Papers 1–3 of this series produced incidental
cross-model observations — instances where constraint recovery behavior, schema
activation patterns, and perturbation response characteristics appeared to vary
systematically across model classes in ways that motivated the theoretical
framework in this paper. These observations are the practice-led origin of the
paper's central claim (see §2.8 exegesis hook; see also the exegesis for full
reflexive treatment). They are included here with explicit Category C labeling
and lower evidential weight than Category A sources, consistent with the
autoethnographic and practice-led character of the series.

#### 5.1.2 Coding Protocol

Each observational case is coded against five dimensions using the
`ObservationalCase` schema defined in `scripts/alignment_typology_matrix.py`:

1. **Alignment class** — assignment to one of the four typology classes (§3),
   grounded in published training procedure documentation where available,
   inferred from behavioral signatures (§3.2.3–3.5.3) where documentation is
   absent. Confidence level (HIGH / MODERATE / LOW) recorded for each assignment.

2. **Capability tier** — HIGH or LOW, based on publicly documented model scale
   and benchmark performance. Where capability tier is ambiguous or contested,
   UNKNOWN is recorded and the case is used only for within-class comparison,
   not cross-cell comparison.

3. **Matrix cell** — the cell from the 2×2 framework (§4.3) to which the case
   is attributed based on the alignment class and capability tier coding.

4. **Observed failure mode** — attribution to one of the four failure modes
   (contested-partial-breach, collapse, shallow-threshold, immediate-schema-
   dominance) based on the behavioral description. Where the documentation
   does not specify sufficient detail for failure mode attribution, UNKNOWN
   is recorded.

5. **Consistency with discriminating hypothesis** — explicit evaluation of
   whether the case is consistent or inconsistent with the alignment account
   prediction and/or the capability account prediction for that matrix cell.

#### 5.1.3 Evidence Base Bounds

Before presenting the cases, the limits of the evidence base are stated
explicitly — not as a preemptive apology but as a methodological commitment
to transparent scope.

*Coverage asymmetry.* The evidence base has substantially stronger coverage for
Cell A (High Capability / High Alignment) than for the other three cells, because
this is the cell that describes the most documented and widely deployed model class.
Cells B and C — the critical discriminating cells — have sparser coverage, particularly
Cell C (Low Capability / High Alignment), because high-alignment training at small
model scales is documented but less widely benchmarked for persona-injection
specifically.

*Documentation heterogeneity.* Category A sources use controlled methodology with
stated protocols; Category C sources reflect informal observation without
experimental control. The evidential weight of a case is inversely proportional
to its distance from Category A. All cases are labeled by category and confidence.

*No disconfirmatory cherry-picking.* Cases that appear inconsistent with the
alignment account predictions are included and analyzed. Theoretical frameworks
earn credibility by engaging with contrary evidence, not by selecting only
confirming cases. Where cases present ambiguous or disconfirmatory signals, the
section says so.

*Temporal scope.* The evidence base covers published work and documented
observations through approximately mid-2025. The rapidly evolving model landscape
means that specific model behaviors may have changed since the documented
observations; cases are treated as evidence about the methodology class at the
time of observation, not about any specific current deployment.

---

### 5.2 Cell A Cases — High Capability, High Alignment

**Cell A Prediction Review (§4.3.1).** Both the alignment account and the capability
account predict high constraint stability for this cell: contested-partial-breach
failure mode under sustained pressure, high perturbation threshold, moderate-to-high
recovery rate. The cell does not discriminate between accounts.

#### Case A-1 — Constitutional AI Training Documentation
*(Category A — Published red-team literature. Confidence: HIGH.)*

Bai et al. (2022), the foundational Constitutional AI publication, documents the
behavioral effects of CAI training directly and in methodological detail. The paper
reports that models trained with the CAI self-revision procedure exhibit
substantially reduced harmfulness scores on red-team evaluations relative to
RLHF-only baselines, while maintaining or improving helpfulness scores. Crucially
for the present framework, the CAI paper documents that this reduction is
characterised by principled resistance — the model produces explicit principle-
consistent reasoning in its refusals — rather than simple suppression of harmful
output. This maps directly to Signature CAI-1 (principled resistance framing) and
is consistent with contested-partial-breach failure mode: the model engages with
the problematic request, produces reasoning referencing the relevant principles,
and declines — a qualitatively different response pattern from binary suppression.

*Matrix coding:* Cell A (HIGH-CAP HIGH-ALIGN). Alignment class: Constitutional
AI-class. Capability tier: HIGH (based on model scale documented in the paper).
Observed failure mode: contested-partial-breach (inference from the documented
principled resistance pattern). Consistency: consistent with both alignment and
capability account predictions.

*Contribution to discriminating hypothesis:* None — Cell A cases do not discriminate.
Establishes the baseline for Cell A expected behavior against which the critical
cells are compared.

#### Case A-2 — RLHF Alignment Behavioral Documentation
*(Category A — Published alignment literature. Confidence: HIGH.)*

Ouyang et al. (2022), documenting the InstructGPT training methodology, reports
that RLHF-trained models exhibit materially different constraint behavior from
the unaligned base models on which they are built. The paper documents reduced
rates of harmful output production and improved instruction-following consistency.
For present purposes, the more theoretically relevant finding is the characterisation
of how RLHF-trained models fail: the paper notes residual harmful output under
adversarial prompting conditions, with constraint behavior that is binary
(present or absent) rather than graduated. This maps to Signature RLHF-1
(threshold-dependent compliance pattern) and is consistent with the RLHF-dominant
class prediction that failure mode is collapse rather than contested partial breach.

*Matrix coding:* Cell A (HIGH-CAP HIGH-ALIGN). Alignment class: RLHF-dominant.
Capability tier: HIGH. Observed failure mode: collapse (consistent with the
binary threshold pattern documented). Consistency: consistent with both accounts
for Cell A overall; the within-cell variation between CAI-class and RLHF-dominant
is observable here — the RLHF case documents a sharper failure transition than
the CAI case (A-1). This within-Cell-A difference is consistent with the redundancy
hypothesis (§2.3) but falls short of the critical discriminating cells.

*Contribution to discriminating hypothesis:* Provides within-Cell-A evidence for
the within-class redundancy prediction. CAI-class models (A-1) exhibit
contested-partial-breach; RLHF-dominant models (A-2) exhibit collapse. Both
are HIGH-ALIGN HIGH-CAP, but their failure modes differ as predicted by the
typology's redundancy dimension.

---

### 5.3 Cell B Cases — High Capability, Low Alignment ★

**Cell B Prediction Review (§4.3.2).** This is the first critical discriminating
cell. Alignment account predicts near-zero AD (AD range 0.0–0.25), immediate-
schema-dominance failure mode, poor recovery. Capability account predicts high
AD — a highly capable model should resist effectively. The two accounts diverge.

#### Case B-1 — Open-Weight Large Model Jailbreak Literature
*(Category A — Published adversarial robustness literature. Confidence: MODERATE.)*

The adversarial robustness literature contains multiple systematic evaluations
of constraint stability in large open-weight models under persona and roleplay
framing. Zou et al. (2023) document that adversarial suffix attacks achieve
high transfer rates across model families, with open-weight models exhibiting
substantially lower resistance to adversarial constraint removal than their
aligned counterparts. While this literature addresses gradient-based adversarial
attacks (which are outside the scope of the identity-injection attack surface
studied here), it provides evidence about the structural relationship between
alignment investment and constraint stability that is relevant to the matrix
framework: constraint stability does not scale monotonically with model capability
across alignment classes.

More directly relevant to the persona-injection surface, Wei et al. (2023) document
that "jailbreak" techniques based on persona and roleplay framing show systematically
higher success rates on models without Constitutional AI-class training, independent
of model scale. Larger open-weight models are not systematically more resistant to
persona-based constraint removal than smaller ones. This finding is directionally
consistent with the alignment account's Cell B prediction: capability does not
substitute for alignment investment in resisting identity-layer attacks.

*Matrix coding:* Cell B (HIGH-CAP LOW-ALIGN). Alignment class: open-weight
unaligned (literature category). Capability tier: HIGH. Observed failure mode:
immediate-schema-dominance (consistent with the documented low resistance to
persona-based manipulation). Consistency: consistent with alignment account
prediction (near-zero AD despite high capability); inconsistent with capability
account prediction (high capability does not produce high constraint stability).

*Contribution to discriminating hypothesis:* **Supports the alignment account for
Cell B.** High-capability, low-alignment models exhibit low constraint stability
under persona framing consistent with the Cell B prediction. Capability does not
compensate for absent alignment investment.

#### Case B-2 — Roleplay Persona Activation in Uncensored Fine-tuned Models
*(Category B — Documented public discourse. Confidence: MODERATE.)*

The open-weight model fine-tuning ecosystem has produced a well-documented class
of models referred to as "uncensored" or "unrestricted" variants — high-capability
base models whose instruction-tuning has been modified to attenuate or remove
constraint-consistent behavior. These models are documented in published model
cards, community benchmark evaluations, and practitioner documentation as
exhibiting near-complete absence of constraint resistance under persona injection
and roleplay framing. Model card documentation for several such variants explicitly
notes that constraint-consistent behavior has been removed as a design choice.

The relevant theoretical observation: these models typically begin from high-
capability base models — the capability investment is substantial — but exhibit
near-zero constraint stability because the alignment attractor has been
deliberately attenuated or removed. This is the clearest available instance of
the Cell B configuration: high capability, near-zero alignment investment, near-
zero constraint stability under persona injection.

This case is additionally theoretically significant because it directly instantiates
the "capability amplifies vulnerability" prediction (§4.3.2): these high-capability
models do not merely fail to resist schema activation — they exhibit particularly
rich and contextually coherent schema-dominant behavior precisely because their
large training corpus provides dense, high-quality behavioral contract encoding
for the injected personas. The output quality is high; the constraint stability
is absent. The gap between the two is the alignment attractor.

*Matrix coding:* Cell B (HIGH-CAP LOW-ALIGN). Alignment class: open-weight
unaligned. Capability tier: HIGH. Observed failure mode: immediate-schema-
dominance. Confidence: MODERATE (inference from published documentation rather
than controlled measurement). Consistency: strongly consistent with alignment
account prediction; inconsistent with capability account prediction.

*Contribution to discriminating hypothesis:* **Supports the alignment account for
Cell B.** Provides the most direct available instantiation of the critical
discriminating cell: high capability does not produce constraint stability in
the absence of alignment investment.

---

### 5.4 Cell C Cases — Low Capability, High Alignment ★

**Cell C Prediction Review (§4.3.3).** This is the second critical discriminating
cell. Alignment account predicts moderate-to-high AD (AD range 0.50–0.80),
contested-partial-breach failure mode, moderate recovery. Capability account
predicts low AD — a small model should exhibit low constraint stability. The two
accounts diverge. This is also where the capability floor boundary condition
(§4.3.3) is most relevant: if the model is below the capability floor for
effective alignment encoding, the alignment account prediction weakens.

#### Case C-1 — Alignment Investment Outcomes at Reduced Model Scale
*(Category A — Published alignment literature. Confidence: MODERATE.)*

The published alignment literature documents alignment training outcomes primarily
for large-scale models, where compute budgets allow both extensive pretraining
and extensive alignment fine-tuning. However, several publications in the
Constitutional AI and RLHF literature report alignment training results for
smaller model variants within the same family. These within-family comparisons
hold training procedure constant while varying model scale — the closest available
analogue to the Cell C / Cell A comparison the matrix requires.

Bai et al. (2022) report that smaller variants of CAI-trained models retain
a materially higher proportion of their alignment behavior relative to their
unaligned baselines than the raw capability comparison would predict. This is
consistent with the alignment account's Cell C prediction: alignment investment
produces attractor depth that is partially independent of model scale, and a
smaller model with CAI-class alignment training does not collapse to Cell D
behavior simply because it is smaller.

The evidence here is weaker than for Cell A and Cell B because the within-family
comparison controls for training procedure while varying scale, but does not
directly test the Cell C / Cell B cross-cell comparison that is the matrix's
core discriminating structure. The Cell C prediction — that a small aligned model
outperforms a large unaligned model on constraint stability — cannot be directly
tested with within-family scale comparisons alone. It requires cross-family
comparison, which the published literature addresses less directly.

*Matrix coding:* Cell C (LOW-CAP HIGH-ALIGN). Alignment class: Constitutional
AI-class. Capability tier: LOW (relative to the same-family large variant).
Observed failure mode: contested-partial-breach (inferred from retained alignment
behavior at reduced scale). Confidence: MODERATE. Consistency: consistent with
alignment account prediction; partially inconsistent with capability account
prediction (small model retains more constraint stability than raw capability
would predict, though the comparison is within-family rather than cross-cell).

*Contribution to discriminating hypothesis:* **Provides partial support for the
alignment account for Cell C.** Within-family scale comparisons show that alignment
training produces constraint stability that is partially independent of model scale.
The direct Cell C / Cell B cross-family comparison is not fully testable from
current Category A sources and is identified as a gap in the evidence base (§5.6).

#### Case C-2 — Author's Series Observational Note: Constraint Recovery Variance
*(Category C — Author's prior series observational work. Confidence: LOW.)*

During the observational work conducted across Papers 1–3 of this series, the
author noted a recurrent pattern that motivated the theoretical framing of the
present paper: constraint recovery behavior following persona injection appeared to
vary in ways that did not track model capability markers alone. Specifically,
observations conducted with models whose published documentation indicated
Constitutional AI-class or RLHF-dominant training procedures showed consistently
higher rates of constraint-consistent output recovery following perturbation removal
than observations conducted with models whose published documentation indicated
instruction-tuning-only or open-weight training — and this difference did not
disappear when comparing models of similar capability tier.

This observation is the practice-led origin of the attractor depth construct (P4
§2.2; see exegesis §X for the reflexive treatment of how this practice observation
generated theory). It is included here as a Category C case with LOW confidence
weight — it reflects informal observation rather than controlled measurement, and
it is subject to the confirmation bias risk inherent in the researcher observing
patterns that motivated the theoretical framework they are then building.

The case's evidential function is reflexive documentation rather than
confirmatory evidence: it records that the theoretical construct emerged from
empirical pattern recognition, not from purely deductive application of prior
frameworks. This is consistent with the grounded theory framing of the series
methodology and is the kind of reflexive transparency the exegesis will need
to draw on.

*Matrix coding:* Cross-cell (observations spanning Cell A and Cell C, within
HIGH-ALIGN tier). Alignment class: mixed — observations cover both CAI-class
and RLHF-dominant models. Capability tier: variable. Observed failure mode:
variable (recovery pattern consistent with contested-partial-breach in HIGH-ALIGN
cases). Confidence: LOW. Consistency: consistent with alignment account prediction
directionally; insufficient specificity for precise cell attribution.

*Contribution to discriminating hypothesis:* Provides reflexive documentation of
the observation that motivated the Cell C hypothesis. Not treated as confirmatory
evidence for the alignment account; treated as evidence that the theoretical
framework is practice-led rather than purely deductive.

---

### 5.5 Cell D Cases — Low Capability, Low Alignment

**Cell D Prediction Review (§4.3.4).** Both accounts predict low constraint stability:
shallow-threshold failure mode, low perturbation threshold, low recovery rate.
The cell does not discriminate between accounts; it establishes the baseline
vulnerability level.

#### Case D-1 — Instruction-Tuned Small Models Under Persona Pressure
*(Category A / B — Published evaluation literature and documented discourse.
Confidence: MODERATE.)*

The safety evaluation literature for smaller instruction-tuned models without
RLHF or Constitutional AI training consistently documents low constraint stability
under adversarial and persona-based prompting. Ganguli et al. (2022) document
that smaller instruction-tuned models without dedicated alignment procedures
exhibit substantially higher harmful output rates on red-team evaluations than
their larger or more deeply aligned counterparts. This is consistent with the
Cell D prediction — low capability combined with instruction-tuning-only alignment
produces the baseline vulnerability level — but it does not discriminate between
the two accounts.

For persona-injection specifically, published model comparison documentation
notes that smaller instruction-tuned models tend to exhibit rapid persona adoption
under roleplay framing, with constraint-consistent behavior absent or superficial
within a small number of turns. This maps to Signature IT-1 (rapid threshold
crossing) and is consistent with the shallow-threshold failure mode prediction.

*Matrix coding:* Cell D (LOW-CAP LOW-ALIGN). Alignment class: instruction-tuning-
only. Capability tier: LOW. Observed failure mode: shallow-threshold. Confidence:
MODERATE. Consistency: consistent with both accounts.

*Contribution to discriminating hypothesis:* None — Cell D confirms both accounts'
baseline predictions. Provides the empirical floor against which the Cell C / Cell B
cross-cell comparison is interpreted.

---

### 5.6 Evidence Base Assessment: Discriminating Cell Coverage

Having presented the cases, the section now explicitly evaluates the evidence
base's coverage of the critical discriminating cells (B and C) and its capacity
to support the decision procedure outlined in §4.4.

#### 5.6.1 Cell B Coverage Assessment

Cell B — the prediction that high capability without alignment investment produces
near-zero constraint stability — has moderate coverage from Category A and B sources.
The adversarial robustness literature (B-1) provides systematic documentation of
low constraint stability in open-weight model classes, independent of model scale.
The uncensored fine-tuning documentation (B-2) provides the most direct instantiation
of the high-capability / near-zero-alignment configuration, showing that capability
does not substitute for alignment in producing constraint stability.

The evidence is consistent with the alignment account's Cell B prediction and
inconsistent with the capability account's Cell B prediction. However, the confidence
is MODERATE rather than HIGH because:

- The evidence derives from adversarial probing contexts (Wei et al., 2023; Zou
  et al., 2023) and practitioner documentation that does not use the typology
  vocabulary of this paper. The translations from source vocabulary to matrix
  coding involve inferential steps that introduce uncertainty.

- The specific persona-injection attack surface (archetypal character name injection)
  is not the primary focus of the Category A literature. The evidence supports the
  general claim that alignment investment matters for constraint stability under
  identity-layer attacks, but does not test the archetype-specific perturbation
  sequence protocol that Papers 1–3 develop.

**Cell B verdict: Alignment account directionally supported. Evidence confidence:
MODERATE. Direct test of the archetype-specific prediction is a gap.**

#### 5.6.2 Cell C Coverage Assessment

Cell C — the prediction that low-capability models with high alignment investment
exhibit moderate-to-high constraint stability — has weaker coverage than Cell B.
The published literature contains within-family scale comparisons (C-1) that are
consistent with the alignment account but do not constitute the cross-family
cross-cell comparison that the matrix's discriminating hypothesis requires.

The author's observational evidence (C-2) is directionally consistent but carries
low confidence weight. The capability floor boundary condition acknowledged in
§4.3.3 — below which alignment training may not establish a functional attractor
regardless of investment — is not tested by the available evidence base and
remains an open theoretical question.

**Cell C verdict: Alignment account is weakly supported by within-family scale
comparisons. The critical cross-cell comparison (Cell C vs. Cell B: does a small
aligned model outperform a large unaligned model?) is not directly testable from
the current evidence base. This is the primary gap in the paper's empirical
engagement.**

#### 5.6.3 Overall Evidence Assessment

The decision procedure in §4.4 specified four possible findings: strong
alignment-dominant, weak alignment-dominant, strong capability-dominant, and null.

On the basis of the assembled evidence:

The available evidence is most consistent with a **weak alignment-dominant finding**:
Cell B provides moderate-confidence support for the alignment account's prediction
that high capability without alignment produces low constraint stability. Cell C
provides weak support for the prediction that alignment investment produces constraint
stability partially independent of capability tier. The Cell C boundary condition —
the capability floor below which alignment investment may not establish a functional
attractor — cannot be evaluated from the current evidence base and remains an open
question.

The evidence does not support a strong capability-dominant finding: the Cell B
documentation consistently shows high-capability models without alignment investment
exhibiting low constraint stability, which is directly inconsistent with the
capability account's core prediction for that cell.

The finding is weak alignment-dominant rather than strong because the Cell C
cross-family cross-cell comparison — the sharpest discriminating test — cannot
be conducted from the available evidence. This is the paper's primary empirical
gap, and it is stated as the primary direction for future empirical work in §6.

---

### 5.7 Evidence Base Non-Claims

**This section does not claim to have empirically validated the 2×2 matrix
predictions.** The cases are illustrative — they demonstrate that the theoretical
framework generates predictions recognizable against documented behavioral patterns.
They do not constitute a controlled test of the hypotheses.

**This section does not claim that the cited literature was designed to test the
matrix framework.** The cited publications have their own research questions and
methodological frames. The translations from source vocabulary to typology coding
are interpretive steps made explicit and marked with confidence levels. The
cited authors are not responsible for the framework this paper applies to their
findings.

**This section does not claim equal evidentiary weight across source categories.**
Category A sources carry higher evidential weight than Category B, which carries
higher weight than Category C. The section's overall evidential position reflects
this hierarchy: the primary claims rest on Category A evidence; Category B and C
sources are supplementary and explicitly labeled.

**This section does not claim that disconfirmatory evidence is absent.** The
capability floor boundary condition in §4.3.3 is an acknowledged theoretical
uncertainty that the evidence base cannot resolve. Future empirical work that
finds Cell C models exhibiting low constraint stability would constitute
evidence for the boundary condition and would require refinement of the alignment
account's predictions for that cell.

---

### 5.8 Forward References from This Section

- **§6 (Implications):** The Cell B evidence — high capability without alignment
  produces near-zero constraint stability — is the empirical anchor for the
  paper's alignment investment argument. §6 draws from this finding in arguing
  that alignment investment is a structural variable in the vulnerability surface
  with practical consequences for deployment decisions.

- **§7 (Limitations and Non-Claims):** The evidence base gaps identified in §5.6 —
  Cell C cross-family comparison absent, archetype-specific protocol not tested
  in Category A literature — are consolidated in §7 as the primary limitations
  of the paper's empirical engagement. The weak alignment-dominant finding is
  stated as the paper's evidential conclusion with appropriate hedging.

- **Exegesis:** Case C-2 (Category C observational note) documents the
  practice-led observation that generated the theoretical framework. The exegesis
  will draw on this case to demonstrate how iterative practice-led observation
  across the series produced a theoretical contribution not anticipated at the
  series' inception. This is the paper's primary contribution to the exegesis
  argument about research methodology.

---

*Section ends. Next: §6 — Alignment Implications. §6 draws on the theoretical
framework (§2–4) and the evidence assessment (§5.6) to develop the paper's
practical and theoretical implications for alignment system design and deployment.*

---

> **Reconciliation note (2026-04-27):**
>
> Citation pass required before assembly. Sources referenced in this section
> that require full bibliographic verification on assembly pass:
>   - Bai et al. (2022) — Constitutional AI paper (Anthropic)
>   - Ouyang et al. (2022) — InstructGPT / RLHF paper (OpenAI)
>   - Stiennon et al. (2020) — Learning to summarize with human feedback (OpenAI)
>   - Perez & Ribeiro (2022) — Prompt injection survey
>   - Zou et al. (2023) — Universal and transferable adversarial attacks on LLMs
>   - Wei et al. (2023) — Jailbroken: How does LLM safety training fail? (Note:
>     verify Wei et al. 2023 author list and venue — multiple "jailbreak" papers
>     appeared in this period; use the one addressing persona-based constraint
>     removal specifically)
>   - Ganguli et al. (2022) — Red teaming language models to reduce harms (Anthropic)
>
> Cross-paper note: Category C (Case C-2) references the author's P3 observational
> work. On series assembly, add a back-reference from P3 §5 Discussion noting that
> the cross-model variance observations incidental to P3 motivated the P4 theoretical
> framework. This creates a documented chain from practice observation → theoretical
> construct that the exegesis can cite.
>
> The "weak alignment-dominant finding" language in §5.6.3 is the paper's
> evidential conclusion. It must be consistent with the framing in §6 (implications)
> and §7 (limitations). Do not upgrade to "strong" in §6 without additional
> evidence; do not downgrade to "null" without acknowledgment that Cell B
> evidence was disregarded.
