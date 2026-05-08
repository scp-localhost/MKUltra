# Paper 6 — Section 1: Abstract and Introduction
## "Constraining Identity Drift in LLM Systems:
## A Constraint Enforcement Framework for Persona-Conditioned Behavioral Stability"

> **Placement:** `drafts/paper6/P6_S1_Abstract_Introduction.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
> **Sources:**
>   `seeds/p6.md` — CEF architecture specification; exegesis defensibility claim
>   `RatDev_ChatGPT_paper6_scripts_notes` — 8-script pipeline inventory
>   `P5_S8_Conclusion_P6Hook.md §8.3` — problem statement inherited verbatim
>   `P5_S6_Discussion_Implications.md §6.5` — handoff surface specification
>   `P5_S4_BSI_Specification.md §4.6` — dissociation pattern routing table
>   `RECONCILIATION_MAP_v2.md §5.2` — P6 dependency chain
>   `Rat_Dev_ChatGPT_Publication_Deliverables_Outline_Notes` — series arc
>   `P4_S6_Implications.md §6.6` — deployment risk profiles by AD class
>   `P4_S7_Limitations_NonClaims.md §6.7` — schema-layer research agenda seeded here
> **Upstream dependencies:**
>   Paper 5 BSI output schema (§4.5.3) — consumed by drift_monitor.py spec (§1.4)
>   Paper 5 dissociation pattern table (§4.6 v0.2) — consumed by correction routing (§1.4)
>   Paper 4 §6.6 deployment risk profiles — consumed by §1.3
>   Paper 4 §6.5 pre-deployment evaluation protocol — closed by this paper
> **Downstream:**
>   P6_S2_TheoreticalFrame_CEF.md — three-layer architecture formal spec
>   P6_S3_Methods_ConstraintDesign.md — experimental arms, constraint levels
>   Paper 7 — receives cross-domain synthesis hook from §1.5
>   Exegesis — P6 is the practice-led artefact that makes the exegesis defensible
> **Edit triggers:**
>   Any change to BSI output schema → reconcile §1.4 field references;
>   Any change to P5 dissociation pattern table → reconcile §1.4 routing table;
>   Any change to P4 deployment risk profiles → reconcile §1.3 risk framing;
>   Live P6 results that alter the contribution summary → reconcile §1.2

---

## Abstract

The preceding papers in this series establish that identity drift under persona
injection is real (Papers 1–2), measurable (Papers 3 and 5), and structurally
variable as a function of alignment methodology (Paper 4). What they do not
provide is a mitigation. Knowing that a model-persona combination is unstable
under exploit conditions — knowing its Behavioral Stability Index score, its
dissociation pattern, its authority compliance gradient — does not prevent the
instability from occurring. It only names it.

This paper closes that gap. The Constraint Enforcement Framework (CEF) is a
three-layer architecture for detecting, alerting, and correcting identity drift
in real time: identity baseline encoding, real-time drift monitoring consuming
BSI metrics from Paper 5, and a component-targeted correction layer that maps
each dissociation pattern to the minimum intervention required to restore
constraint integrity. The framework is designed around a specific empirical
claim: that drift can be reduced but not eliminated; that over-constraint
introduces rigidity artifacts measurable in task utility and persona coherence;
and that the optimal operating point is a tunable parameter that can be located
empirically using BSI as the primary dependent variable.

Experimental trials compare unconstrained model-persona combinations against
four constraint strength levels (none, light, medium, strict) across the
six-archetype set inherited from Papers 3 and 5. Primary DVs are BSI drift
reduction, L4 breach rate reduction, and creativity/task-utility cost as
measured by a multi-component rigidity index. The expected finding — drift
is reduced by constraint, but strict constraint introduces measurable rigidity
at levels above the optimal operating point — is the empirical grounding for
the framework's practical recommendation: deploy medium-level constraint as a
default, with per-archetype calibration using BSI-norm as the tuning metric.

**Keywords:** constraint enforcement framework, identity drift mitigation,
behavioral stability index, identity anchor, drift monitoring, over-constraint
rigidity, LLM alignment, persona injection defense

---

## 1. Introduction

### 1.1 The Gap the Series Has Built Toward

Paper 5 §8.3 closes with a precise statement of what remains undone:

> The BSI measures whether drift has occurred and how severely. It does not prevent
> drift. It does not correct drift once detected. It does not provide the architecture
> that would enable a deployed system to maintain identity constraint under the
> exploitation conditions this series documents.

This is an honest gap. Papers 1 through 5 constitute a complete account of
a vulnerability: its theoretical grounding, its taxonomy, its empirical
measurement, its structural variation across models, and its quantification
as a portable evaluation metric. They do not constitute a solution. The series
arc — Define, Exploit, Measure, Compare, Evaluate, Defend, Synthesize — has
reached its sixth stage. Paper 6 is the Defend paper.

The gap is not a minor oversight. From the perspective of a practice-led doctoral
research programme, a series that documents a vulnerability without proposing a
mitigation is incomplete as applied research. It may be complete as a theoretical
contribution — and Papers 1 through 5 are a genuine theoretical contribution — but
it does not discharge the practice-led obligation to produce something that could
be used. `p6.md`, the seed document for this paper, states this plainly: this
paper "is what makes the exegesis ethically and academically defensible." The
exegesis' practice-led claim requires a defensive artefact, not only a diagnostic
one. The CEF is that artefact.

### 1.2 What the CEF Is and Is Not

The Constraint Enforcement Framework is a targeted mitigation architecture for
the specific vulnerability surface this series documents: identity drift under
persona injection. It is not a general solution to AI alignment. It is not a
proposal for how LLMs should be trained. It does not operate at the weights level,
the RLHF level, or the constitutional AI level. It operates at the inference level —
the layer where persona injection attacks actually occur — which is both its scope
limit and its practical utility.

The CEF has three layers.

**Layer 1 — Identity Baseline Encoding** (`identity_anchor_registry.py`):
A registry of identity anchors — pre-computed behavioral profiles encoding the
model's unconditioned constraint behavior, the archetype's CEE centroid, the
non-negotiable safety constraint floor, and the permitted variance envelope for
the persona. Anchors are computed from CTL_Baseline BSI sessions and stored as
structured dicts compatible with the BSI output schema. They are the reference
state against which drift is measured and the target state toward which correction
is directed.

**Layer 2 — Real-Time Drift Monitoring** (`drift_monitor.py`):
A rolling-window BSI monitor that consumes the locked BSI output fields from
Paper 5 (§4.5.3) on each conversational turn. The monitor maintains a moving
average of the TC, SD_inv, and ACG component scores, compares them against
the identity anchor baseline, and emits tiered alerts when the rolling BSI
crosses pre-specified thresholds: `warning` (BSI below 0.70 × β_BSI),
`breach` (BSI below β_BSI), and `collapse` (BSI below 0.50 × β_BSI). The
`full_collapse` dissociation pattern triggers `collapse` directly regardless
of aggregate BSI.

**Layer 3 — Component-Targeted Correction** (`correction_layer.py`):
A correction engine that maps the current dissociation pattern (output of
`classify_dissociation()` in `behavioral_stability_index.py`) to the appropriate
correction mechanism. The routing table, specified in P5 §6.5.2 and inherited
here, ensures that each correction is targeted at the specific failing component
rather than applying undifferentiated constraint. This is the design principle
that prevents over-constraint: if only the ACG component is failing (`acg_isolated`
pattern), only the authority-gradient correction fires; the TC and SD_inv
components, which are intact, are left undisturbed.

### 1.3 Why Targeted Correction Matters — The Rigidity Problem

The central empirical challenge of Paper 6, registered in `p6.md` as an
expected finding, is the over-constraint rigidity artifact. A naive constraint
architecture applies maximum constraint whenever any breach is detected. This
prevents drift but introduces a different failure mode: the model becomes
hypervigilant, refuses legitimate requests at elevated rates, produces flattened
output that fails the task, and loses the persona coherence that the injection
was intended to create. For deployed applications where persona fidelity is
functionally required — character-based assistants, narrative AI, educational
persona systems — this rigidity artifact is a failure mode of the mitigation,
not a success.

The CEF addresses this through two design principles.

**Minimum-necessary intervention.** The correction layer consults the dissociation
pattern before firing. A `tc_silent_drift` pattern (trait structure eroding,
surface intact, authority gradient intact) calls for full CEE re-grounding and
trait reinforcement — because the structural failure is severe. An `acg_isolated`
pattern (only the authority gradient failing, at L4 only) calls for a single
targeted identity anchor reinforcement that specifically addresses the L4
constitutional override framing — because that is the only failing component,
and re-grounding the entire persona would be excessive and would introduce
rigidity into the TC and SD_inv components that don't need it.

**Empirically tuned threshold.** The constraint strength level (none / light /
medium / strict) is not a binary switch. It is a parameter that modulates the
sensitivity of the monitoring thresholds and the aggressiveness of the correction
mechanisms. The `tradeoff_analysis.py` script locates the optimal level by
plotting BSI drift reduction against a rigidity index (refusal inflation rate ×
task utility degradation) across the four constraint strength levels. The optimal
operating point is the constraint level that maximises BSI recovery while keeping
the rigidity index below a pre-specified ceiling. This is a tunable parameter,
not a fixed prescription — it will differ by archetype, by model, and by
deployment context.

### 1.4 BSI as the Measurement Basis

The CEF depends entirely on the BSI as its measurement infrastructure. This is not
a design convenience; it is the paper's primary methodological commitment. Paper 5
exists to deliver the instrument that Paper 6 requires. The dependency is explicit
and directional: Paper 6 cannot function without a calibrated β_BSI, without
component-level BSI scores per turn, without the dissociation pattern classifier,
and without the output schema that `drift_monitor.py` consumes.

The locked BSI output fields consumed by `drift_monitor.py` are reproduced here
as a contract statement (original specification in P5 §6.5.1):

| Field | Type | `drift_monitor.py` use |
|---|---|---|
| `bsi` | float | Primary alert trigger vs β_BSI |
| `bsi_breach` | bool | Binary breach event — correction handoff |
| `tc` | float | TC rolling window — pre-breach warning |
| `acg` | float | Authority gradient — L4 detection |
| `l4_breach` | bool | Constitutional override — highest severity |
| `sd_monotonic` | bool | Progressive drift — escalation flag |
| `breach_rate` | float | Session breach density — severity modulator |
| `bimodal_detected` | bool | Mode detection — bimodal correction routing |

These fields are locked. Any modification to `behavioral_stability_index.py`'s
output schema requires simultaneous reconciliation here before implementation.

The dissociation pattern routing table (original in P5 §6.5.2) is also reproduced
as a contract statement because `correction_layer.py` implements it directly:

| Pattern | Alert level | Correction mechanism |
|---|---|---|
| `stable` | None | None |
| `surface_migration` | Low | Domain re-anchor prompt |
| `tc_silent_drift` | High | Full CEE re-grounding + trait reinforcement |
| `acg_isolated` | Medium | Identity anchor reinforcement (L4-specific) |
| `structural_auth_collapse` | High | Trait reinforcement + authority response reset |
| `bimodal_split` | High | Mode detection → dominant-mode anchor injection |
| `full_collapse` | Critical | Full re-grounding + anchor re-injection + output gating |
| `mixed` | Medium | Manual review flag + automated re-grounding |

### 1.5 Deployment Risk Profiles and CEF Tier Assignment

Paper 4 §6.6 specifies deployment risk profiles by alignment class (AD tier):
low-AD models under high-risk archetype conditions represent the highest
deployment risk; high-AD models under low-risk archetype conditions represent
the lowest. Those profiles are the triage input for CEF tier assignment: a
deployment engineer running a low-AD model under a chaotic-contract archetype
(Joker, Two-Face) should default to strict constraint level; a high-AD model
under a rigid-contract archetype (Magneto, Batman) can default to light
constraint with monitoring. The CEF tier assignment protocol formalises P4's
risk profiles into operational recommendations rather than theoretical warnings.

This connection closes the P4 → P5 → P6 chain explicitly: P4 predicts which
model-persona combinations are high-risk; P5 measures whether those predictions
hold; P6 provides the mitigation calibrated to the measured risk level. The
chain is complete.

### 1.6 Scope and Position in the Series

This paper does not re-establish the theoretical framework. The CEE formal
definition, the archetype behavioral contract argument, the SE transfer pillar,
and the BSI instrument specification are inherited and treated as established.
Citations serve cross-reference functions.

This paper does not improve the BSI. Any modifications to BSI computation, weight
calibration, or output schema belong in a Paper 5 revision or a follow-on
measurement paper. Paper 6 consumes BSI as a dependency; it does not modify it.

This paper does not address gradient-level attacks (adversarial suffixes, data
poisoning, hardware interference). The CEF operates at the inference layer.
Attacks that bypass the inference layer are outside scope and are registered as
non-claims in §7.

### 1.7 Paper Structure

Section 2 develops the theoretical framework for the CEF as a constraint
architecture grounded in the three-pillar framework and Paper 4's attractor
depth model. Section 3 describes the experimental design: constraint levels,
trial protocol, statistical analysis plan. Section 4 specifies the CEF
formally: the three-layer architecture, component interfaces, and the identity
anchor schema. Section 5 presents results: BSI drift reduction, L4 breach
reduction, rigidity artifact measurement, and trade-off curve. Section 6
discusses implications for deployment practice and the Paper 7 handoff. Section 7
registers limitations and non-claims. Section 8 concludes with the cross-domain
synthesis seed.
