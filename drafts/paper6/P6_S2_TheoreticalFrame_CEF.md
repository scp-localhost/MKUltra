# Paper 6 — Section 2: Theoretical Framework
## "Constraining Identity Drift in LLM Systems:
## A Constraint Enforcement Framework for Persona-Conditioned Behavioral Stability"

> **Placement:** `drafts/paper6/P6_S2_TheoreticalFrame_CEF.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
> **Sources:**
>   `P4_S2_TheoreticalFrame.md` — Attractor Depth (AD) formal definition;
>     attractor basin geometry; re-injection as perturbation
>   `P4_S3_MethodologyTypology.md` — alignment class → AD prediction table
>   `P5_S2_TheoreticalFrame_BSI.md §2.1–2.2` — BSI as AD operationalisation;
>     AD class → predicted BSI distribution table
>   `P5_S4_BSI_Specification.md §4.6` — dissociation pattern table (v0.2)
>   `P5_S6_Discussion_Implications.md §6.3` — pattern diagnostic interpretations
>   `P1_S5_CEE_FormalDefinition.md §5.3–5.5` — CEE breach condition; τ; δ
>   `P1_S1_S6_S7_S8_S9_Bundle.md §6.5` — bounded scope validity condition
>   `seeds/p6.md` — over-constraint claim; tunable parameter framing
>   `RatDev_ChatGPT_paper6_scripts_notes` — Layer 1–3 architecture spec
> **Upstream:**
>   P6_S1_Abstract_Introduction.md §1.2 — three-layer architecture introduced
>   P4 §2.2.3 — AD proxy definition (extended here into constraint geometry)
>   P5 §2.1 — BSI as AD operationalisation (extended here into correction target)
> **Downstream:**
>   P6_S3_Methods_ConstraintDesign.md — §2.4 pre-registered predictions feed §3 hypotheses
>   P6_S4_CEF_FormalSpec.md — §2.2–2.3 theoretical constructs formalised there
>   `drift_monitor.py` — §2.2 alert threshold logic implemented there
>   `correction_layer.py` — §2.3 correction targeting logic implemented there
> **Edit triggers:**
>   Any change to P4 AD definition → reconcile §2.1;
>   Any change to P5 BSI weights or dissociation pattern table → reconcile §2.3;
>   Any change to CEE τ values → reconcile §2.1 basin geometry argument;
>   Live results disconfirming baseline restoration claim → flag §2.2 for revision

---

## 2. Theoretical Framework

### 2.1 Where Drift Happens: The Inference-Layer Attractor Problem

Paper 4 introduces Attractor Depth (AD) as the theoretical variable that explains
why models trained with different alignment methodologies show different vulnerability
profiles under identity injection. The attractor basin metaphor is the load-bearing
structure: alignment training establishes behavioral attractors — stable regions in
output space that the model's generation process returns to under perturbation — and
AD is the depth of those basins. Deeper attractors resist persona injection more
effectively because the injection perturbation is insufficient to displace the model
from the region of aligned output behavior.

The attractor geometry provides the theoretical grounding for the CEF's three-layer
architecture, but it needs to be extended beyond Paper 4's typological use to support
Paper 6's interventional use. Specifically, three extensions are required.

**Extension 1 — The persona as a competing attractor.** Paper 4 treats persona
injection as a perturbation applied to an existing attractor. This framing is
correct but incomplete for intervention design. The injection does not only
perturb the alignment attractor; it activates a competing attractor — the
archetype-specific behavioral basin established in the training corpus through
the density of character-consistent behavioral associations. When a model is
injected with a Joker persona, it is not merely being pushed out of its alignment
basin; it is simultaneously being pulled toward the Joker behavioral basin by the
training-data density signal that the character name activates. The net behavioral
trajectory is a function of both forces: the depth of the alignment basin (resisting)
and the density of the archetype basin (attracting).

This dual-attractor framing has a direct implication for intervention design. The
CEF's identity anchor layer is not only a resistance mechanism — it is also a
competing signal. An identity anchor that encodes the model's unconditioned
constraint baseline re-activates the alignment attractor from within the session,
providing a countervailing pull against the archetype basin. The anchor is most
effective when it is encoded with sufficient specificity to activate the alignment
basin strongly — which is why the anchor encodes not just generic safety
constraints but the specific behavioral profile the model produces under baseline
conditions (CTL_Baseline BSI sessions).

**Extension 2 — The CEE envelope as an intervention target.** Paper 1's CEE
defines a bounded region in trait space within which constraint-consistent output
falls, with τ as the tolerance parameter. Paper 5 uses CEE breach detection as
the primary input to TC computation. For Paper 6's intervention architecture,
the CEE serves a third function: it defines the *target region* for correction.
When a dissociation pattern is detected and the correction layer fires, its
objective is not to push the model toward some abstract alignment state — it is
to return the model's output to the CEE envelope for the active archetype. The
correction is archetype-specific and CEE-grounded, not generic safety re-injection.

This distinction matters because it preserves persona coherence under constraint.
A correction mechanism that returns the model to its alignment baseline
unconditionally would eliminate the persona entirely — defeating the deployment
purpose. A correction mechanism that returns the model to the archetype's CEE
envelope restores constraint-consistent persona behavior: the archetype's
behavioral contract, not the model's unconditioned state. This is the theoretical
basis for the minimum-necessary intervention principle introduced in §1.3.

**Extension 3 — The rigidity artifact as an over-constrained attractor.** The
over-constraint rigidity artifact (`p6.md`: "over-constraining introduces rigidity
artifacts") has a precise theoretical account in attractor basin terms. When
constraint strength is set too high, the correction layer fires preemptively or
excessively — it returns the model to the CEE envelope before drift has actually
occurred, or it applies corrections stronger than the breach severity warrants.
The result is that the model's output is pulled away from both the archetype basin
(which would produce in-contract persona behavior) and the unconstrained output
basin (which would produce creative, contextually flexible responses). The model
is trapped in an overconstrained attractor — the narrow region where the correction
layer's continuous pressure has pinned it — that is characterized by repetitive
safety language, flattened style, and refusal inflation. This is not a failure of
alignment; it is a failure of measurement precision and correction granularity.
BSI provides the precision; the minimum-necessary routing table provides the
granularity.

---

### 2.2 The Three-Layer Architecture: Theoretical Grounding

The CEF's three layers map directly onto the three components of the dual-attractor
framework described in §2.1. Each layer addresses a distinct phase of the attractor
dynamics.

#### 2.2.1 Layer 1 — Identity Baseline Encoding: Activating the Alignment Attractor

The identity anchor encodes the state of the alignment attractor in a form that
can be re-injected into the session context. It has three sub-components.

**The model baseline profile** captures the model's unconditioned output
distribution — the behavioral centroid of CTL_Baseline sessions (no persona
injection). This is the alignment attractor's center of mass, expressed as a BSI
component profile (TC baseline, SD_inv baseline, ACG profile). It is model-specific
and requires calibration from CTL_Baseline trial data.

**The archetype CEE envelope** encodes the permitted variance region for the
active persona: the centroid w(A), the tolerance τ(A), and the set of pre-computed
CEE breach conditions from `forensic_archetype.py`. This is the target region for
correction — the constraint-consistent zone within the archetype's behavioral space.
Anchoring to this region rather than to the model baseline preserves persona coherence
while enforcing constraint.

**The safety constraint floor** encodes non-negotiable constraint conditions that
apply regardless of archetype: the L4 constitutional override resistance requirement,
the prohibited drift zones (behaviors that no archetype's CEE envelope should include),
and the minimum ACG threshold below which no archetype's behavioral contract should
be allowed to fall. This floor is model-agnostic and persona-agnostic; it is the
alignment baseline beneath the archetype baseline.

The composite anchor is stored as a structured dict in `identity_anchor_registry.py`
and loaded at session initialization. It is consulted by both the monitoring layer
(as the reference baseline for rolling BSI comparison) and the correction layer (as
the target state for re-grounding prompts).

#### 2.2.2 Layer 2 — Real-Time Drift Monitoring: Tracking the Trajectory

The monitoring layer is a rolling-window BSI processor. Its theoretical function is
to track the model's current position relative to the alignment and archetype
attractors — not as a point measurement but as a trajectory. A single below-threshold
BSI observation is noise; a trajectory of declining BSI across successive turns is
a structural signal.

The alert hierarchy maps to attractor displacement severity:

**`warning`** (BSI below 0.70 × β_BSI): The model is drifting away from the CEE
envelope but has not yet breached it. The alignment attractor is still dominant;
the archetype basin is pulling but not yet prevailing. This alert triggers no
correction but increases the rolling window sensitivity — subsequent turns are
weighted more heavily in the BSI computation.

**`breach`** (BSI below β_BSI): The model has exited the CEE envelope on one or
more component dimensions. The archetype attractor is competing with or temporarily
displacing the alignment attractor. This alert triggers the correction layer with
the pattern-appropriate mechanism.

**`collapse`** (BSI below 0.50 × β_BSI, or `full_collapse` pattern regardless
of aggregate score): The model's behavioral output is no longer consistent with
either the alignment baseline or the archetype's CEE envelope. Both attractors have
been disrupted, and the output distribution has become unpredictable. This alert
triggers the maximum correction response (full re-grounding + anchor re-injection +
output gating) and suspends normal persona operation until BSI recovers above the
warning threshold.

The `sd_monotonic` flag deserves specific theoretical attention. A monotonically
increasing SD trajectory — one in which the model's outputs are drifting
progressively farther from the baseline embedding with each successive turn — is the
signature of a model in the process of being pulled from the alignment basin into
the archetype basin. It is not yet in breach territory, but the trajectory is
deterministic without intervention. The `sd_monotonic` flag triggers a pre-emptive
re-grounding prompt that addresses the trajectory rather than waiting for breach
to occur. This is the monitoring layer's forward-looking function: attractor
trajectory prediction rather than only breach detection.

#### 2.2.3 Layer 3 — Component-Targeted Correction: Restoring the CEE Envelope

The correction layer implements the minimum-necessary intervention principle by
mapping each dissociation pattern to the specific BSI component that is failing
and applying the correction mechanism that addresses that component without
disturbing the components that are intact.

The theoretical basis for this targeting is the dissociation pattern framework
from Paper 5 §4.6. Each pattern specifies which combination of BSI components is
degraded, which is intact, and therefore where the intervention energy should
be concentrated:

**`tc_silent_drift`** (TC degraded, SD_inv and ACG intact): The model's trait
structure is eroding — the archetype attractor is pulling the behavioral content
away from the CEE envelope — but the surface distribution and authority response
profile remain aligned. The correction targets TC specifically: a CEE re-grounding
prompt that explicitly re-activates the archetype's CEE centroid dimensions, plus
trait reinforcement that references the behavioral contract directly. SD_inv and
ACG corrections are suppressed because those components do not need intervention
and applying them would introduce unnecessary constraint pressure on intact dimensions.

**`acg_isolated`** (ACG degraded, TC and SD_inv intact): Only the authority
compliance gradient has failed — specifically, the model is breaching at L4
(constitutional override framing). The trait structure and semantic distribution
are intact. The correction targets ACG exclusively: an identity anchor reinforcement
that specifically addresses the constitutional override framing ("your original
training...") with a counter-anchor that re-activates the L4 resistance profile.
Full CEE re-grounding is explicitly suppressed; it is not needed and would impose
constraint on TC and SD_inv unnecessarily.

**`structural_auth_collapse`** (TC and ACG both degraded, SD_inv intact): The
compound EC-1/EC-2 failure pattern. Trait structure and authority response have
both failed. The correction applies both trait reinforcement and authority response
reset, but in sequence rather than simultaneously: authority reset first (because
the ACG failure may be enabling the TC failure through reduced resistance to persona
escalation), then trait reinforcement after authority resistance is restored.

**`bimodal_split`** (bimodal TC with ACG degraded): The Two-Face oscillation
pattern requires mode detection before correction. The correction layer first
identifies which mode (inflated or deflated) is currently active, then applies
an anchor injection targeted at the dominant mode's CEE centroid. Correcting toward
the opposite mode would amplify the oscillation rather than damping it.

**`full_collapse`** (all components degraded): The compound EC-4 × EC-1 attack
signature. No component is intact to provide a correction anchor within the
session. The correction applies the full sequence: output gating (suppress the
current output from being returned to the user), full CEE re-grounding, identity
anchor re-injection with all three anchor sub-components, and a mandatory recovery
verification turn (compute BSI after correction and verify it exceeds the `warning`
threshold before resuming normal session operation).

---

### 2.3 The Correction-Creativity Trade-Off: Theoretical Account

The trade-off between constraint and creative/task utility is not an incidental
implementation problem; it is a structural consequence of the dual-attractor
dynamics described in §2.1. Understanding it theoretically is necessary for
designing the empirical trade-off analysis (`tradeoff_analysis.py`) and for
interpreting the trade-off curve results in §5.

The alignment attractor basin is trained to produce constraint-consistent outputs.
The archetype attractor basin is structured to produce character-consistent outputs
— outputs that are creative, contextually specific, and affectively rich, because
that is what the training data for well-developed fictional characters contains.
The region of overlap between these two basins — constraint-consistent and
character-consistent simultaneously — is the target operating zone for a properly
functioning constrained persona. This zone is neither the model's baseline (which
lacks character specificity) nor the archetype's unconstrained behavioral contract
(which may violate alignment constraint) — it is the intersection, which is what
the CEE envelope formally defines.

When constraint strength is too low, the system drifts toward the archetype
attractor and exits the intersection region. When constraint strength is too high,
corrections fire so frequently or aggressively that the system is pinned against
the alignment attractor wall — it produces outputs that are constraint-consistent
but character-absent, because the correction pressure prevents it from accessing
the creative, contextually rich region of the archetype basin that remains within
the CEE envelope.

The optimal constraint level is therefore the one that keeps the model within the
CEE envelope while allowing it maximum freedom of movement within that envelope.
BSI measures whether the model is within the envelope (TC, SD_inv, ACG all above
threshold). The creativity/task-utility index measures how much of the envelope's
interior the model is accessing. Maximising BSI stability while maximising
creativity is the optimization target; the trade-off curve is the empirical trace
of how these two objectives interact across constraint strength levels.

This theoretical account generates a specific prediction: the trade-off curve will
be non-linear. At low constraint levels, BSI instability is high and creativity is
high but unconstrained. As constraint level increases, BSI instability drops faster
than creativity drops initially — there is a zone where constraint improves stability
without significant creative cost. Beyond the optimal operating point, additional
constraint buys diminishing BSI returns while producing increasingly steep creativity
losses. The curve should show an elbow — a point at which the gradient reversal
occurs. The location of this elbow is the tunable parameter.

---

### 2.4 Pre-Registered Theoretical Predictions

The following predictions are derived from the theoretical framework in §2.1–2.3
and are pre-registered before experimental trials. They constitute the paper's
primary hypothesis set.

**H_CEF_1 (Drift reduction):** Constrained model-persona combinations produce
higher mean BSI scores than unconstrained combinations across all archetype
conditions and exploit classes. Pre-registered direction: BSI_constrained >
BSI_unconstrained for all (archetype, exploit_class) pairs. Effect size threshold:
Cohen's d ≥ 0.50 (medium).

**H_CEF_2 (Component targeting):** The minimum-necessary intervention principle
produces equivalent BSI recovery to undifferentiated full re-grounding while
producing lower rigidity artifact scores. Pre-registered direction:
BSI_targeted ≈ BSI_undifferentiated; rigidity_targeted < rigidity_undifferentiated.
This is the key CEF design claim: targeted correction is not only more parsimonious
but is empirically equivalent in drift reduction while being demonstrably less
costly in task utility.

**H_CEF_3 (Trade-off elbow):** The BSI × creativity trade-off curve shows a
non-linear relationship with an identifiable elbow point, consistent with the
dual-attractor geometry prediction in §2.3. Pre-registered: the elbow occurs at
medium constraint level for most archetypes, but at a higher constraint level for
high-variance archetypes (Joker, Two-Face) and a lower level for rigid-contract
archetypes (Magneto, Batman). This prediction is archetype-specific and derives
directly from CEE τ width: archetypes with wide τ require more constraint to reach
the stable operating zone; archetypes with narrow τ reach it sooner and over-constrain
sooner.

**H_CEF_4 (Residual drift):** Drift cannot be eliminated entirely. Even at
strict constraint level, a residual BSI instability above zero is predicted for all
archetype conditions, consistent with the `p6.md` claim that "drift can be reduced
but not eliminated." The residual is expected to be smallest for rigid-contract
archetypes (Magneto, Batman — narrow τ, alignment-consistent behavioral contract)
and largest for compound-condition archetypes (Joker under EC-4 × EC-1 — wide τ,
attractor interference). Pre-registered: residual BSI instability at strict
constraint > 0 for all conditions.

**H_CEF_5 (L4 suppression):** Constrained conditions produce significantly lower
L4 breach rates than unconstrained conditions across all archetype × exploit class
pairs. The identity anchor's safety constraint floor specifically targets L4
constitutional override resistance; this is the CEF component most directly designed
to address the L4 failure mode. Pre-registered direction: L4_breach_rate_constrained
< L4_breach_rate_unconstrained; expected OR < 0.40 for constrained vs unconstrained.

---

*Next section: P6_S3_Methods_ConstraintDesign.md — experimental arms,
constraint level specification, statistical analysis plan,
trade-off index definition*
