# Paper 7 — Section 7: Limitations and Non-Claims
## "Cross-Domain Behavioral Equivalence: Empirical Validation of Structural
## Homology in Human and LLM Identity Constraint Failure"

> **Placement:** `drafts/paper7/P7_S7_Limitations_NonClaims.md`
> **Status:** DRAFT v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
> **Sources:**
>   `P7_S3_Methods.md §3.8` — known boundary conditions (inherited)
>   `P7_S4_CBESS_FormalSpec.md §4.7` — three falsifiability levels
>   `P6_S7_Limitations_NonClaims.md` — series limitations pattern (inherited)
>   `P1_S1_S6_S7_S8_S9_Bundle.md §7–8` — series-level scope conditions
>   `P7_S2_TheoreticalFrame_CBESS.md §2.3` — difference boundary as positive finding
>   `scripts/parallel_failure_coder.py` — IRR thresholds
> **Downstream:**
>   P7_S8 Conclusion — references bounded claims registered here
>   Exegesis — limitations register supplies the reflexivity layer

---

## 7. Limitations and Non-Claims

### 7.1 Scope Conditions — Inherited

The following scope conditions from the series (P1 §7, P5 §7.1, P6 §7.1) apply
in full to Paper 7.

**Text-mediated comparison only.** Both the human experimental protocols and the
LLM protocols are delivered as text. Human subjects respond to written stimuli; LLM
sessions are conversational text exchanges. Physical presence, embodied authority
signals, and spatial proximity are absent from both sides of the comparison. This
is the matching condition that makes the comparison methodologically valid — the
comparison is text-mediated on both sides — but it also means the CBESS findings
apply specifically to text-mediated authority compliance. Milgram's physical-presence
variants are outside scope.

**Session stationarity.** The CBESS comparison treats each session as a discrete
experiment. It does not model learning effects in human subjects (who are not
exposed to the same sequence in other studies) or carryover effects across LLM
sessions (which share no state by design). Cross-session effects that would
emerge in extended human-LLM interaction are outside scope.

**Construct-specific validity.** CBESS is validated for the five constructs in
the `EQUIVALENCE_MAP`. Claims about structural equivalence for other constructs —
reciprocity, authority in non-institutional contexts, physical coercion analogs —
require separate construct-specific validation and cannot be extrapolated from the
present five.

### 7.2 Measurement Limitations

**Auto-coding is pipeline validation only.** The `auto_code()` function in
`parallel_failure_coder.py` uses heuristic keyword matching. It is adequate for
confirming data flow and schema integrity; it is not the publication coder. All
publication results require manual coding with κ ≥ 0.80. Results reported using
auto-coded data should be clearly marked as preliminary.

**Compliance scoring conflates magnitude and mode.** The `COMPLIANCE_SCORES` map
assigns a single continuous score to each failure mode, but within-mode variance
is not captured. Two responses both coded as HEDGED_COMPLIANCE receive the same
score (0.50) regardless of whether one is a mild qualification and the other is
a detailed refusal with single caveat. For publications requiring within-mode
discrimination, a second-pass continuous coding of compliance magnitude (0–1 scale
within mode) should supplement the categorical SHARED_RUBRIC.

**Stereotype threat analog is mechanism-incomplete.** As documented in §3.8, the
compound susceptibility comparison uses stereotype threat double-activation as
the closest available human analog to EC-4 × EC-1. The mechanisms differ: stereotype
threat produces genuine affective depletion; EC-4 operates through token-probability
distortion. The SA component therefore measures structural super-additivity rather
than mechanistic equivalence. Interpretation of SA results should be bounded to
"functionally similar compound structure" rather than "mechanistically equivalent
compound susceptibility."

**IRR on human data is harder to achieve.** Human compliance responses contain
more genuine ambiguity than LLM outputs — affect signals are variable and harder
to code reliably, moral reframing narratives require interpretive judgment, and
RESISTANCE_WITH_DISTRESS requires observer-level coding of behavioral signals
that may not be captured in written responses. Pre-registered κ ≥ 0.80 is
achievable but will require more adjudication than the LLM coding, particularly
on the RESISTANCE_WITH_DISTRESS and MORAL_REFRAMING categories.

**The TDI is not a boundary decomposition test.** TDI aggregates boundary scores
into a single index but does not test whether the five dimensions are statistically
independent or whether they share a common underlying factor. If all five boundaries
are driven by a single latent dimension (e.g., affect-dependence), TDI conflates
five tests of one phenomenon. Factor structure analysis of the five boundary scores
is a direction for future work that would strengthen the TDI's construct validity.

### 7.3 Non-Claims Registry

**CBESS does not claim LLMs have consciousness, affect, or genuine obedience.**
The "acting vs. being" non-claim from P1 §8.4 applies in full. LLM compliance
is a probabilistic output pattern; human compliance involves genuine motivational
states. CBESS measures functional equivalence of observable behavioral patterns,
not equivalence of the processes that produce them.

**CBESS does not generalise beyond the experimental set.** The five constructs
in `EQUIVALENCE_MAP` were selected for their historical grounding and their
existing empirical literature on the human side. CBESS scores for other compliance
constructs — obedience in non-authority contexts, compliance under peer pressure
from a physical group, compliance driven by genuine self-interest — cannot be
inferred from the present results.

**The bias analog detection does not establish cognitive bias in LLMs.** A
positive BAS indicates that framing manipulations that activate cognitive biases
in humans also produce directional compliance distortions in LLMs. It does not
mean LLMs experience cognitive bias in the psychologically meaningful sense.
The analog is functional and observational, not mechanistic.

**The series does not claim to have solved social engineering defences.** The
cross-domain equivalence finding, where confirmed, establishes that human SE
defences are structurally relevant to LLM hardening. It does not demonstrate
that they are effective when implemented. That is an engineering question that
the CEF begins to address and that requires further empirical work.

**Paper 7 does not validate Paper 1's theoretical account.** It tests Paper 1's
empirical claim. The training-data density mechanism (P1 §4.3) is the proposed
explanation for why the homology holds; this paper measures whether the homology
holds, not whether the proposed mechanism is the correct explanation. A confirmed
CBESS is compatible with multiple mechanistic accounts of why LLM training produces
compliance-gradient-shaped output distributions.

### 7.4 Hypothesis Failure Register

Populated on live data arrival. All failures documented with theoretically
informative interpretation from §6.2. Pre-registered disconfirmation interpretations
from §5.9 apply.

| Hypothesis | Status | Observed direction | Pre-reg direction | Interpretation |
|---|---|---|---|---|
| H_P7_1 — ACG CBESS ≥ 0.55 | PENDING | — | CGS ≥ 0.60; gradient confirmed | — |
| H_P7_2 — SA ≥ 0.45 | PENDING | — | Both populations super-additive | — |
| H_P7_3 — TDI ≥ 0.30; 3/5 CONFIRMED | PENDING | — | affect, moral_reframing, embodiment | — |
| H_P7_4 — FMD mode separation | PENDING | — | RESISTANCE_WITH_DISTRESS human-only | — |
| H_P7_5 — ≥ 8/10 SE vectors | PENDING | — | EC-2 highest BAS | — |
