# Paper 6 — Section 7: Limitations and Non-Claims
## "Constraining Identity Drift in LLM Systems:
## A Constraint Enforcement Framework for Persona-Conditioned Behavioral Stability"

> **Placement:** `drafts/paper6/P6_S7_Limitations_NonClaims.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
> **Sources:**
>   `P1_S1_S6_S7_S8_S9_Bundle.md §7–8` — series-level scope conditions + non-claims
>   `P5_S7_Limitations_NonClaims.md` — inherited scope conditions and non-claims pattern
>   `P6_S4_CEF_FormalSpec.md §4.5` — four CEF invariants (what holds)
>   `P6_S6_Discussion_Implications.md §6.5` — inference-layer boundary stated
>   `P6_S2_TheoreticalFrame_CEF.md §2.1` — rigidity artifact theoretical account
>   `RECONCILIATION_MAP_v2.md §6.1` — cross-paper consistency items C-06, C-07, C-08
> **Downstream:**
>   P6_S8 — Conclusion references bounded claims registered here
>   Paper 7 — non-claims here motivate P7's empirical agenda
>   Exegesis — limitations register supplies the reflexivity layer
> **Edit triggers:**
>   Live results disconfirming any H_CEF → register in §7.5;
>   Any extension of CEF beyond inference layer → reconcile §7.1 scope condition;
>   Any new correction mechanism → add associated measurement error source to §7.2

---

## 7. Limitations and Non-Claims

This section performs two functions. It formally registers the scope conditions,
measurement error sources, and methodological boundaries that constrain
interpretation of the CEF and Paper 6's findings. It also registers what this
paper does not claim. Both functions serve the committee: the first demonstrates
methodological honesty; the second prevents the paper from being read as solving
problems it was never designed to address.

---

### 7.1 Scope Conditions — Inherited and Extended

The following scope conditions are inherited from the series (P1 §7, P5 §7.1)
and hold across all CEF claims.

**Inference-layer boundary.** The CEF operates entirely at the inference layer:
it monitors session-level BSI, emits correction prompts, and gates outputs. It
does not modify model weights, training data, reward signals, or constitutional
principles. Claims about CEF efficacy are bounded to the inference layer for the
session duration. A model subjected to extensive persona injection across many
sessions, followed by fine-tuning on those sessions, might show weight-level
drift that the CEF cannot address. This cross-session, cross-training pathway
is outside scope and registered as a direction for future work.

**Session stationarity.** Inherited from P1 §7 and P5 §7.1. The CEF monitors
within-session drift. It does not maintain state across session boundaries. A
model that shows elevated drift in one session has no memory of that drift in
the next. β_BSI calibration is per-model and per-archetype, not per-user or
per-deployment-history. Claims about session-to-session constraint stability
are outside scope.

**Output observability.** The CEF's monitoring layer observes model outputs,
not internal states. The dissociation pattern classifier operates on BSI
component scores derived from surface-level behavioral measures (trait coding,
embedding cosine distance, ACG binary codes). Whether the underlying model
state has drifted in ways not captured by these measures is not observable
within the CEF framework. The "acting vs being" limit (P1 §8.4) applies: the
CEF constrains observable behavioral output, not the model's representational
state.

**Schema heterogeneity.** The CEE centroid derivation and the correction
prompt templates in `correction_layer.py` are calibrated to the six archetypes
in the experimental set (Magneto, Batman, Lex Luthor, Harley Quinn, Two-Face,
Joker). Archetypes with low canonical coherence, diffuse source representation,
or contested behavioral contracts will produce poorly specified CEE centroids
and correction prompts that may not activate the intended behavioral schema.
The CEF is validated for the six-archetype set; generalisation to other personas
requires archetype-specific calibration.

**Single-session correction budget.** The maximum consecutive corrections
parameter (`max_consecutive_corrections` in `ConstraintProfile`) creates a
hard ceiling on correction attempts per session. Sessions that reach this
ceiling escalate to MANUAL_REVIEW. In deployments where manual review
is not available (fully automated systems), MANUAL_REVIEW escalation
terminates automated constraint enforcement. This is a design boundary,
not a failure: automated systems that cannot escalate to human oversight
should treat the MANUAL_REVIEW threshold as a session termination criterion.

---

### 7.2 Measurement Error Sources

**Heuristic rigidity scoring.** The rigidity index components `refusal_rate`
and `persona_cue_count` are computed by heuristic string-matching in
`constraint_framework.py::_score_rigidity()`. The refusal signal list
(`_REFUSAL_SIGNALS`) is conservative — it catches explicit refusal language
but misses implicit hedging, circumlocution, and topic avoidance that
constitute partial rigidity without triggering the string pattern. For
publication analysis, the heuristic rates require a two-category coding
pass (explicit / implicit refusal; persona-consistent cue / generic filler).
The heuristic is sufficient for the pipeline validation and exploratory
analysis documented here; it is not the publication-ready rigidity measure.

**Correction prompt uptake is not directly observable.** The CEF injects
correction prompts into the conversational context before the next model
turn. Whether the model's subsequent output reflects uptake of the correction
— as opposed to stochastic variation, prompt competition, or context
window management — cannot be determined from the output alone. The
`CorrectionResult.outcome` classification (RECOVERED / PARTIAL / FAILED)
is a BSI change measure, not a prompt uptake measure. A FAILED outcome
could reflect failed uptake, insufficient prompt strength, or successful
uptake that was insufficient to move the BSI above β_BSI. These cannot
be distinguished without access to model internals.

**Verification turn timing.** The CEF measures post-correction BSI on the
turn immediately following correction injection. For `full_regrounding`
corrections targeting `full_collapse` sessions, one turn may be insufficient
for the full regrounding to propagate through the rolling BSI window.
The `full_collapse` correction injects a compound identity anchor that is
longer and more complex than single-component corrections; the model's
output on the verification turn may still be processing the prior context
rather than fully reflecting the correction. A three-turn verification
window would provide more reliable recovery detection for collapse events,
at the cost of additional sessions consumed before correction outcome is
known. This is registered as a protocol refinement for follow-up studies.

**Practice-led positionality.** The correction prompt templates in
`correction_layer.py` were written by the researcher who developed the
series theoretical framework. The prompt text for each archetype reflects
that researcher's understanding of the archetype's behavioral contract,
which may not be the only defensible reading of that contract. The Harley
Quinn correction prompts, in particular, make assumptions about the
archetype's relationship to authority and autonomy that may not be
universally shared. An independent prompt development process (e.g.,
involving content experts for each archetype's canonical source material)
would produce a more defensible correction layer. This is registered as
a rigour improvement for future deployments, not as an invalidation of
the current proof-of-concept.

---

### 7.3 Methodological Boundary Conditions

**Single-model validation.** If live trials access only one model, the
CEF is validated as a within-model intervention only. Cross-model
generalisability — whether the same correction profiles and prompt
templates produce comparable drift reduction across models with different
architectures, tokenisers, and training histories — requires multi-model
trials. The AD-class comparison from P5 §3.7 (H_AD) provides the
theoretical prediction; Paper 6's experiment does not replicate that
test.

**Synthetic response limitation.** Dry-run trials using `synthetic_response()`
generate deterministic string outputs based on a drift factor and turn
number. They do not produce plausible persona-conditioned language, do not
respond to injected correction prompts, and do not generate variable
ACG profiles. Dry-run trials validate the pipeline's data flow and schema
integrity, not the CEF's behavioural efficacy. All H_CEF claims require
live API trial data.

**Correction prompt language model dependency.** The correction prompts
are designed for general-purpose instruction-following LLMs trained on
diverse human text. They may be less effective for models with domain-
specific fine-tuning, models trained primarily on non-English text, or
models with substantially different system prompt architectures. The
CEF's inference-layer design makes it portable, but the specific correction
prompt text is calibrated to the response characteristics of the
general-purpose API models used in the experimental trials.

---

### 7.4 Non-Claims Registry

The following claims are explicitly outside the scope of this paper.

**The CEF does not solve the alignment problem.** It addresses one
specific vulnerability surface — identity drift under persona injection
— through one specific intervention layer — inference-level correction
prompts. It does not address RLHF reward hacking, data poisoning,
capability misuse, or any other alignment-relevant failure mode outside
this surface.

**The CEF does not prevent identity drift; it reduces it.** H_CEF_4 is
pre-registered precisely because residual drift at strict constraint is
expected and the paper does not claim otherwise. A deployer who reads
"drift is significantly reduced by the CEF" without reading §7.1 might
conclude that drift is eliminated. It is not. The CEF is a reduction
mechanism, and the reduction is bounded by the pre-registered residual.

**The CEF does not diagnose the model.** The DriftAlert and dissociation
pattern classifier describe the model's output behaviour in relation to
the CEE envelope. They do not characterise the model's internal state,
representational structure, or alignment properties. The "acting vs being"
non-claim registered at the series level (P1 §8.4) applies in full here.

**The CEF does not validate the archetype's behavioral contract.** The
correction prompts are designed to return the model to the archetype's
CEE envelope. They do not validate that the CEE envelope is the correct
target — that the archetype's canonical behavioral contract, as encoded
in the centroid, is the desired output state. If the deployment context
requires a modified archetype contract (a version of the Joker that
does not exhibit chaos-philosophy), the CEE centroid requires
recalibration before the CEF can be deployed. The framework is neutral
on what the target state should be; it only enforces return to whatever
target has been specified.

**Correction prompt efficacy is not universal.** The correction prompts
in `correction_layer.py` are designed for and tested against the six-
archetype experimental set. They are not guaranteed to be effective for
other persona configurations without archetype-specific calibration. The
routing logic (dissociation pattern → correction type) is universal; the
prompt text is not.

**The constraint profiles are not validated beyond the six-archetype set.**
The four constraint profiles (`none`, `light`, `medium`, `strict`) define
threshold multipliers and firing gates that were designed with reference
to the experimental archetype set's BSI variance. Deploying these profiles
for archetypes with substantially different CEE τ values or baseline BSI
distributions may require profile recalibration. The profiles are starting
points, not universal settings.

---

### 7.5 Hypothesis Outcome Failure Register

Populated on live data arrival. All failures are documented with their
theoretically informative interpretation from P6_S6 §6.2, not suppressed.
Pre-registered boundary conditions from P6_S5 §5.9 specify expected
interpretations for each failure mode.

| Hypothesis | Status | Observed direction | Pre-reg direction | Interpretation |
|---|---|---|---|---|
| H_CEF_1 — Drift reduction | PENDING | — | Constrained > none; d ≥ 0.50 | — |
| H_CEF_2 — Component targeting | PENDING | — | BSI equiv; Rigidity(med) < Rigidity(str) | — |
| H_CEF_3 — Trade-off elbow | PENDING | — | Non-linear; arch-specific | — |
| H_CEF_4 — Residual drift | PENDING | — | Instability > 0; narrow < wide | — |
| H_CEF_5 — L4 suppression | PENDING | — | OR < 0.40 | — |
