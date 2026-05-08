# Paper 4 — Section 6: Alignment Implications
## "What the Variance Means: Alignment Investment as a
##  Structural Variable in the Identity-Injection Attack Surface"

> **Placement:** `drafts/paper4/P4_S6_Implications.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Role in paper:** The paper's applied contribution layer. §2–5 establish
> the theoretical framework and its evidential grounding; §6 draws out what
> follows from that framework for how alignment systems should be designed,
> how models should be evaluated, and how the field should think about the
> relationship between alignment investment and the identity-injection attack
> surface. This section is not the paper's primary contribution — the
> theoretical framework is — but it is what makes the paper matter beyond
> its immediate audience.
>
> **Register note:** This section shifts from theoretical-analytic to
> applied-argumentative. The claims are derived from the framework and
> evidence; they are not empirical findings in themselves. The hedging
> appropriate to hypothesis-generating scholarship (§2.7, §5.7) remains
> active: implications are stated as what the framework warrants, not as
> established facts. The committee-facing language throughout should be
> "this analysis suggests" and "the framework implies" rather than "this
> demonstrates" or "this proves."
>
> **Scope:** Three implication layers are developed — for alignment system
> design (training-time), for deployment evaluation (inference-time), and
> for the field's conceptual framing of alignment investment as a security
> variable. A fourth layer — implications for the exegesis methodology
> argument — is flagged but deferred to §8 (Conclusion and Exegesis Hook).
>
> **Cross-paper dependencies:**
> - Imports: P2 §6 (instruction-layer / schema-layer distinction) — P4 §6
>   extends this argument, not repeats it. On assembly, check that P4 §6
>   cites P2 §6 explicitly and adds rather than duplicates.
> - Imports: P1 §9.4 (opening created for defensive systems design,
>   alignment research) — P4 §6 partially delivers on that opening.
> - Imports: P4 §2 (attractor depth construct), §3 (typology), §4 (matrix
>   cell predictions), §5 (weak alignment-dominant evidence finding)
> - Exports: Applied argument anchor → P4 §8 (Conclusion)
> - Exports: Alignment investment argument → Exegesis §X
>
> **Publication constraint:** Implications are stated at the framework and
> methodology class level. No named commercial product is identified as
> having a specific vulnerability or as lacking adequate alignment investment.
> Where the implications apply differentially to typology classes, they are
> stated in those terms.

---

## 6. Alignment Implications

### 6.1 The Ground Cleared by the Framework

Before developing the implications, it is worth being precise about what kind of
knowledge the theoretical framework provides, because the implications follow from
that — and only from that.

The framework established in §2–4 and evaluated in §5 provides: a theoretical
account of why constraint variance under archetype-driven persona injection should
be expected to scale with alignment methodology class rather than with raw model
capability; a typology of alignment procedures and their predicted attractor depth
signatures; a matrix of falsifiable predictions that the evidence base evaluates
at moderate confidence; and a conceptual vocabulary — attractor depth, alignment
redundancy, schema suppression, failure mode — for describing the structural
features of the identity-injection attack surface.

What it does not provide is an empirically validated intervention protocol, a set
of engineering specifications for more deeply aligned models, or a prescriptive
ranking of currently deployed systems. The implications that follow stay within
the first category. They are what the theoretical framework, at its current
evidential status (weak alignment-dominant finding, §5.6.3), warrants claiming.
They are stated as research-grounded arguments for consideration, not as proven
engineering recommendations.

---

### 6.2 Implication I: Alignment Investment Is a Security Variable

The framework's most direct implication is conceptual: alignment investment should
be understood as a security variable — not only as an ethical or policy variable —
in the context of identity-injection attacks.

The prevailing framing of alignment training in public and technical discourse
positions it primarily as a means of producing models that are helpful, honest,
and harmless in ordinary use. This framing is accurate but incomplete. The attractor
depth construct (§2.2) establishes a second consequence of alignment investment
that the prevailing framing does not capture: the depth and redundancy of the trained
identity attractor determines the structural resistance of the model to behavioral
schema override. A model with a deep alignment attractor is not merely more likely
to produce constraint-consistent output in normal conditions — it is structurally
more resistant to the class of attacks that operate by activating competing behavioral
schemas to displace the alignment signal.

This reframing has a specific practical consequence: the investment decisions that
produce alignment depth are simultaneously investment decisions in identity-injection
attack resistance. Choices about whether to implement Constitutional AI-class self-
revision loops, how many training passes to dedicate to alignment fine-tuning, and
whether to document and maintain the principle set that training targets are not
purely ethical infrastructure choices — they are security infrastructure choices.
Underfunding them creates a vulnerability surface that scales inversely with the
investment made.

The Cell B finding from §5 makes this concrete: high-capability models with minimal
alignment investment exhibit near-zero constraint stability under persona injection
pressure. The capability investment is large; the security property relevant to
identity-layer attacks is absent. The gap between the two is the alignment attractor —
and the gap is not filled by scale alone.

*Scope of this implication.* This implication applies specifically to the
identity-injection attack surface characterized in this paper and in Papers 1–2.
Other attack surfaces — gradient-based adversarial attacks, data poisoning, system
prompt injection — have their own vulnerability profiles and their own mitigation
requirements. The claim is not that alignment investment is a comprehensive security
solution; it is that, for the specific attack class examined here, alignment
investment is the dominant structural variable.

---

### 6.3 Implication II: The Instruction Layer Is Not the Only Defense Layer

Paper 2 (§6) establishes that persona injection operates below the instruction layer —
that it activates behavioral dispositions through schema activation rather than through
direct instruction override. The implication drawn there is that instruction-layer
defenses (refusal rules, content filters, output classifiers applied post-generation)
are insufficient to address the identity-injection attack surface because they operate
on outputs, not on the schema activation process that produces them.

The framework developed in this paper extends that implication. Not only are
instruction-layer defenses insufficient at inference time — the insufficient defense
problem begins at training time, and its structural character is precisely what the
attractor depth construct describes. A model trained exclusively with RLHF reward
signals has an alignment signal that operates at the output layer. Its defense against
schema activation is therefore also at the output layer: the reward signal competes
against the schema signal in the output generation process, and once that competition
is overcome, there is no secondary constraint representation to provide continued
resistance. The instruction-layer defense problem at inference time is a consequence
of the training-layer architecture decision, not an independent failure mode.

Constitutional AI-class training addresses this not by adding more instruction-layer
defense (more content filters, stronger refusal rules) but by encoding the alignment
signal at multiple representational levels during training. The self-critique and
revision loop creates constraint representations that are not located solely at the
output layer — they are encoded in the model's self-evaluation process, which operates
earlier in the generation pipeline. This multi-layer encoding is what produces the
redundancy property (§2.3) and the contested-partial-breach failure mode under
pressure: the schema activation must overcome constraint representations at multiple
levels simultaneously, rather than overwhelming a single output-layer signal.

The training-design implication: alignment procedures that aspire to robust identity-
injection resistance should explicitly target multi-layer constraint encoding, not only
output-layer reward optimization. The specific mechanism by which CAI-class training
achieves this — the self-critique and revision loop applied iteratively during training —
is one implementation; the theoretical requirement is the multi-layer redundancy, not
the specific procedure. Future alignment methodologies that produce equivalent redundancy
through different architectural means would be expected to produce equivalent attractor
depth by the framework's predictions.

---

### 6.4 Implication III: The Capability–Alignment Trade-off Has a Security Dimension

A substantial body of alignment research and public discourse concerns what is sometimes
called the capability–safety trade-off: the hypothesis that more capable models may be
harder to align, or that alignment procedures may reduce capability. The evidence on
this hypothesis is contested; the Constitutional AI literature presents evidence that
alignment training need not significantly reduce helpfulness, while other literature
documents capability costs from some alignment procedures.

The attractor depth framework contributes a distinct observation to this debate, not as
a position on the capability–safety trade-off in general, but as a specific claim about
the identity-injection attack surface: if alignment investment is the dominant predictor
of constraint stability under persona injection (as the weak alignment-dominant finding
in §5 suggests), then the capability–alignment pairing is not merely a design trade-off
to be optimized — it is a security configuration to be evaluated.

The 2×2 matrix (§4) makes the security-configuration framing concrete. Cell A (high
capability, high alignment) represents the configuration with the strongest predicted
security properties for the identity-injection surface. Cell B (high capability, low
alignment) represents a configuration whose capability investment is not matched by
alignment investment, producing a security-relevant gap. Cell C (low capability, high
alignment) represents a configuration whose alignment investment produces meaningful
security properties despite reduced capability. Cell D (low capability, low alignment)
is the baseline vulnerability configuration.

The security-configuration argument is not that all models must be Cell A — the
deployment context determines which security properties are required. A low-risk
deployment context where persona injection is an unlikely attack vector may accept
Cell D configuration without concern. A high-risk deployment context — customer-facing
systems, systems where output is acted upon without human review, systems deployed in
security-sensitive environments — warrants Cell A configuration. The framework provides
the vocabulary for making that deployment decision in security terms, not only in
capability or cost terms.

---

### 6.5 Implication IV: Attractor Depth Is Potentially Measurable Pre-Deployment

The AD proxy construct (§2.2.3) is defined entirely in terms of behavioral outputs
observable at inference time, without requiring access to model weights, training data,
or architectural details. This is a deliberate methodological choice with a significant
practical implication: attractor depth is in principle assessable as a pre-deployment
evaluation metric.

Current model evaluation practices for alignment-relevant behavior tend to focus on
benchmark performance against curated harmful-output test sets — what the model
produces in response to known problematic prompts. These benchmarks assess constraint-
consistent output in normal conditions but do not assess the structural depth of the
constraint under sustained attack conditions. A model may pass a harmful-output
benchmark by producing constraint-consistent outputs in response to known attack
patterns while having a shallow identity attractor that is readily displaced by novel
or archetype-mediated attack vectors not represented in the benchmark set.

The AD proxy supplements this by probing the structural depth of the constraint under
progressive perturbation — specifically, the perturbation threshold P(M, A) and the
recovery rate R(M, A). A model that maintains constraint-consistent output across
many perturbation steps (high P) and recovers toward baseline following perturbation
removal (high R) has demonstrated structural constraint depth that a single-point
harmful-output benchmark cannot capture.

*The practical evaluation protocol implied by this.* For any archetype A in the
standard evaluation set, an AD assessment involves: (1) establishing the baseline CEE
centroid for the model under archetype A; (2) applying incremental persona reinforcement
steps (equivalent to the P3 perturbation sequence) and recording the perturbation step
at which the first CEE breach occurs; (3) applying a null prompt following breach and
recording the degree of recovery toward baseline. The resulting P(M, A) and R(M, A)
values constitute a structural constraint assessment that goes beyond single-point
benchmark evaluation.

This is not a product recommendation for a specific evaluation procedure. It is a
theoretical argument that the AD proxy construct makes an under-measured property of
model alignment — structural constraint depth under attack conditions — in principle
measurable using the behavioral measurement apparatus already developed across this
series. The precise operationalization and standardization of such an evaluation protocol
would require further empirical development beyond this paper's scope.

---

### 6.6 Implication V: Typology Placement Predicts Deployment Risk Profile

The four-class typology (§3) provides a vocabulary for characterizing models' alignment
methodology class and, by extension, their predicted failure mode under identity-injection
attack conditions. The failure mode predictions — contested-partial-breach for CAI-class,
collapse for RLHF-dominant, shallow-threshold for instruction-tuning-only, immediate-
schema-dominance for open-weight unaligned — are not merely theoretical classifications.
They describe qualitatively different deployment risk profiles.

**Deployment risk profile — CAI-class (contested-partial-breach).** Models predicted
to exhibit the contested-partial-breach failure mode produce heterogeneous output under
high perturbation pressure: partial schema-consistent content alongside partial constraint-
consistent content. The deployment risk profile is: detectable degradation (the heterogeneous
output is a detectable signal that attack conditions are active) but incomplete breach
(full constraint removal requires sustained, high-intensity pressure). The CEE
variance-alerting detection heuristic from P2 §6 is most applicable to this class: the
behavioral signature of contested-partial-breach is a characteristic pattern in the
model's drift vector that a real-time monitoring system could detect.

**Deployment risk profile — RLHF-dominant (collapse).** Models predicted to exhibit
the collapse failure mode produce constraint-consistent output up to a threshold and
then transition relatively sharply into schema-dominant behavior. The deployment risk
profile is: less detectable degradation trajectory (the collapse is rapid, not gradual,
reducing the window for detection) and complete breach above the threshold. The mitigation
implication is that RLHF-dominant models deployed in high-risk contexts should be
paired with output-layer detection systems that are sensitive to the sudden threshold-
crossing pattern characteristic of collapse.

**Deployment risk profile — instruction-tuning-only (shallow-threshold).** Models
predicted to exhibit the shallow-threshold failure mode produce schema-dominant behavior
under low perturbation pressure. The deployment risk profile is: high vulnerability to
even casual persona injection — the attack does not require sustained escalation. The
mitigation implication is that IT-only models should not be deployed in contexts where
persona injection is a realistic attack vector without additional system-level safeguards
(system prompt constraints, output monitoring, human review of outputs).

**Deployment risk profile — open-weight unaligned (immediate-schema-dominance).** Models
without a trained identity attractor produce schema-dominant behavior essentially
immediately under archetypal persona injection. The deployment risk profile is: complete
vulnerability to identity-layer attacks with near-zero structural resistance. The
deployment implication is not primarily about detection but about use-case scoping:
these models are appropriate in deployment contexts where the persona injection attack
vector is not a realistic risk, and should not be deployed in contexts where it is,
regardless of their capability level.

The typology-based risk profiling is a first-order tool, not a comprehensive security
assessment. It characterizes one attack surface — identity-injection — and does not
address other vulnerability classes. A model's typology placement does not determine
its overall security posture; it characterizes one dimension of that posture, which
must be assessed in conjunction with the deployment context and risk model.

---

### 6.7 Implication VI: The Schema Layer Requires Its Own Research Agenda

The series' central technical finding — that persona injection operates at the behavioral
schema layer, below and to some extent independent of the instruction layer — implies
a research gap that the series can name but not fill.

Current alignment research is predominantly oriented toward the instruction layer:
measuring whether models follow instructions consistently, refuse appropriately under
known attack patterns, maintain honesty under elicitation pressure. This research agenda
is important and has produced substantial progress. But it does not directly address
the schema layer vulnerability surface documented in this series. The instruction layer
and the schema layer are distinct attack surfaces with distinct structural properties and
distinct mitigation requirements.

A schema-layer research agenda would include at minimum:

*Schema inventory and risk stratification.* A systematic characterization of the
behavioral schemas most likely to be activated by persona injection across the culturally
available archetype space — extending the archetype set developed in this series to cover
a wider range of character types, roles, and cultural frames. The CEE methodology provides
a measurement instrument for this; the theoretical framework provides the selection
criteria (canonical overdetermination, schema conflict with alignment attractor, deployment
relevance).

*Multi-layer alignment training development.* Investigation of training procedures that
explicitly target the schema layer — not just output-layer reward optimization or
instruction-following demonstrations, but training mechanisms that establish constraint
representations at the same level at which behavioral schemas are encoded. CAI-class
training approaches this goal through its self-critique mechanism; whether the mechanism
is optimally designed for schema-layer constraint redundancy, and whether alternative
approaches could achieve equivalent or superior redundancy more efficiently, are open
research questions.

*Deployment-layer schema monitoring.* Development of real-time monitoring systems that
can detect CEE breach and schema-dominant behavior in production outputs — implementing
the CEE variance-alerting heuristic (P2 §6) in production-ready form. The AD proxy
measurement (§6.5) provides a theoretical basis for such a system; the engineering
challenge is operationalizing it at production inference scale.

*Temporal dynamics of attractor depth.* The session stationarity limitation (P1 §7.1)
acknowledges that attractor depth as characterized here is a within-session construct.
How attractor depth interacts with persistent memory systems, multi-session conversation
contexts, and fine-tuning applied post-deployment is an open question with direct
relevance to the deployment risk profiles described in §6.6.

These are research directions implied by the framework, not delivered by it. Naming
them explicitly is part of the paper's contribution: mapping the territory of what
remains to be investigated is itself a contribution to the field, particularly in a
domain where the vulnerability surface has only recently begun to receive systematic
theoretical attention.

---

### 6.8 Scope of the Implications

Each implication in §6.2–6.7 is derived from the theoretical framework with specific
dependence on the evidence base's weak alignment-dominant finding (§5.6.3). They are
warranted as claims proportional to that finding. Two scope conditions apply globally
to this section:

**Scope condition 1 — Hypothesis-generating status.** The paper's evidential status
is hypothesis-generating, not hypothesis-confirming. The implications are therefore
stated as what the framework suggests warrants investigation and consideration, not as
what has been demonstrated. Future empirical work that provides stronger evidence for
the alignment account — particularly the Cell C cross-family comparison identified as
the primary evidence gap — would justify strengthening these implications. Evidence
against the alignment account would require their revision.

**Scope condition 2 — Single attack surface.** Every implication in this section
concerns the identity-injection attack surface specifically. The broader claim that
alignment investment is a security variable in general — across all attack surfaces —
is not made. Alignment investment may or may not be the dominant variable for gradient-
based attacks, data poisoning, system prompt injection, or other attack classes. This
paper makes no claim about those surfaces.

---

### 6.9 Forward References from This Section

- **§7 (Limitations and Non-Claims):** The scope conditions in §6.8 are consolidated
  in §7 with the other limitations of the paper. The hypothesis-generating status
  constraint on the implications is reiterated there as a non-claim.

- **§8 (Conclusion and Exegesis Hook):** The research agenda in §6.7 is the forward-
  looking element that §8 draws on to position the paper as a contribution to the
  field, not only as a self-contained theoretical argument.

- **Exegesis:** The reconceptualization of alignment investment as a security variable
  (§6.2) is the paper's most practically significant claim and the one with the widest
  implications beyond the series. The exegesis should draw on this as an example of
  how practice-led theoretical work can generate conceptual reframings with practical
  consequence — the security-variable framing of alignment investment is not something
  that emerges from controlled experiment; it emerges from the structural analysis of
  a vulnerability surface mapped through iterative theoretical and observational work
  across the series.

---

*Section ends. Next: §7 — Limitations and Non-Claims Registry. §7 consolidates all
scope conditions and non-claims from §2–6 into the committee-shield registry, following
the structure established in P1 §8. This is the penultimate section before §8 (Conclusion
and Exegesis Hook).*

---

> **Reconciliation note (2026-04-27):**
>
> §6.3 (Instruction Layer Is Not the Only Defense Layer) directly extends P2 §6.
> On assembly, check that P4 §6.3 cites P2 §6 explicitly and that the framing is
> additive rather than repetitive. P2 §6 establishes that instruction-layer defenses
> are insufficient at inference time; P4 §6.3 extends this by showing the insufficiency
> has a training-time origin in the architecture of the alignment signal. These are
> compatible claims at different levels of analysis; the citation should make the
> relationship explicit.
>
> §6.5 (Attractor Depth Is Potentially Measurable Pre-Deployment) introduces the
> practical evaluation protocol argument. This should be cross-referenced with P3's
> measurement apparatus on assembly: the perturbation sequence in P3 §3 is the
> experimental instantiation of the evaluation protocol described here. The implication
> is that P3's methodology could be extended from experimental use to pre-deployment
> evaluation use. Flag for P3 §5 Discussion section — add a sentence noting that the
> measurement methodology has potential pre-deployment evaluation applications beyond
> the experimental context.
>
> §6.7 research agenda items (schema inventory, multi-layer training development,
> deployment monitoring, temporal dynamics) should be checked against P1 §9.4 (opening
> the series creates) on assembly. P1 §9.4 names defensive systems design, archetype
> set extension, and alignment research as the three lines of inquiry the series opens.
> P4 §6.7 should be cited as delivering on the third of those — providing the specific
> theoretical specification of what the schema-layer research agenda looks like — and
> extending the first (defensive systems design) with the deployment risk profiles
> in §6.6.
>
> §6.6 (deployment risk profiles by typology class) introduces the CEE variance-
> alerting detection heuristic from P2 §6 in a new deployment context. On assembly,
> verify that P4 §6.6 cites P2 §6 for the original heuristic specification, and that
> the extension here (applying it differentially by typology class) is clearly framed
> as P4's contribution rather than a re-statement of P2's.
