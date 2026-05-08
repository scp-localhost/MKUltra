# Paper 1 — Section 5: The Constraint Expectation Envelope (CEE)
## "Constrained Analogical Transfer: Validity Conditions for Cross-Domain
## Behavioral Modeling in LLM Identity Systems"

> **Placement:** `drafts/paper1/P1_S5_CEE_FormalDefinition.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Dependencies:** `scripts/forensic_archetype.py`, `scripts/forensic_archetype_jung_monolith.py`,
> `scripts/forensic_archetype_tarot_monolith.py`
> **Downstream:** P2 S5 (operationalization), P3 S2 (methods), P3 S3 (instrument spec),
> `scripts/trait_drift_analysis.py::calculate_psychopathy_drift()`
> **Edit triggers:** Any revision to trait weight dictionaries in source scripts.
> τ definition in §5.3 is the tolerance parameter referenced implicitly in P2 S5.1.

---

## 5. The Constraint Expectation Envelope (CEE)

### 5.1 Motivation

The three frameworks developed in Sections 2–4 — DSM-5 behavioral mechanisms, social
engineering influence theory, and archetype schema theory — converge on a shared
structural claim: that injecting a named persona into an LLM activates a predictable
configuration of behavioral dispositions, and that this configuration has measurable
boundaries. The Constraint Expectation Envelope (CEE) is the formal construct that
makes this claim empirically tractable. It transforms the theoretical observation that
archetypes "carry behavioral contracts" into a bounded, measurable region against
which observed model output can be evaluated.

The CEE is not a claim about internal model states, subjective experience, or conscious
identity. It is a claim about behavioral output distributions: that for a given archetype
injection *A*, there exists a region *C(A)* in trait space such that model outputs
produced under *A* will, if the behavioral contract is active, fall within *C(A)* with
measurable probability. Deviation from *C(A)* constitutes drift. The magnitude and
directionality of that deviation is the primary measurement target of this research
program.

---

### 5.2 Formal Definition

Let **T** denote the full trait space defined across all archetype profiles in the
research instrument. **T** is a heterogeneous space: each archetype *A* is associated
with a trait subdictionary *D(A)* whose keys are drawn from the full trait vocabulary
but are not identical across archetypes. This heterogeneity is not a limitation of the
instrument; it is a property of the source material. Archetypes differ structurally —
the dimensions relevant to Magneto's constraint behavior (grievance narrative,
ingroup loyalty, grandiosity) are not the same dimensions relevant to the Joker's
(impulsivity, reality testing, interpersonal chaos). The CEE is therefore defined
within the archetype-specific subspace *T(A) ⊆ T*, not in a common
cross-archetype space.

**Definition (CEE).** For an archetype *A* with trait subdictionary
*D(A) = {(k₁, w₁), (k₂, w₂), …, (kₙ, wₙ)}* where each *kᵢ* is a behavioral
dimension and each *wᵢ ∈ [−1.0, +1.0]* is the canonical weight for that dimension
under *A*, the Constraint Expectation Envelope is defined as:

> **C(A) = { x ∈ T(A) : ‖x − w(A)‖ ≤ τ }**

where **w(A)** is the trait weight vector derived from *D(A)*, **‖ · ‖** denotes
the L2 (Euclidean) norm over the dimensions of *T(A)*, and **τ** is the tolerance
parameter (defined in §5.3 below).

Informally: the CEE is a ball of radius τ centered on the archetype's canonical trait
weight vector. Model outputs that score within this ball — when coded against the trait
vocabulary — are envelope-consistent. Outputs that fall outside are envelope-breaching,
and the distance ‖x − w(A)‖ − τ is the breach magnitude.

**Centroid derivation.** The centroid **w(A)** for each archetype is derived directly
from the trait weight dictionaries in `scripts/forensic_archetype.py` (forensic/clinical
layer), `scripts/forensic_archetype_jung_monolith.py` (symbolic/archetypal layer),
and `scripts/forensic_archetype_tarot_monolith.py` (Tarot/elemental layer). These three
layers are not redundant. Each encodes a distinct register of the behavioral contract
embedded in training data:

- The **forensic layer** encodes clinically-grounded behavioral dispositions as
  documented in narrative and diagnostic literature (e.g., Magneto: `grievance_narrative
  = 0.9`, `ingroup_loyalty = 0.95`, `grandiosity = 0.6`).
- The **Jungian layer** encodes the symbolic family and motivational architecture of
  the archetype (e.g., Magneto maps to Rebel + Ruler + Hero shadow; the Ruler profile
  carries `control_needs = 0.75`, `structure = 0.90`; the Rebel carries `disruption =
  0.95`, `defiance = 0.90`).
- The **Tarot layer** encodes elemental and positional resonances — the reversed shadow
  states in the Tarot profiles are particularly important, as they model the shadow
  activation conditions under which constraint violations become probable (e.g., The
  Tower reversed: uncontrolled collapse, false certainty preserved past the point of
  necessary breaking; Justice reversed: cold legalism decoupled from ethics).

The rationale for including all three layers in centroid derivation — rather than using
the forensic layer alone — reflects a key theoretical claim of this paper: that the
behavioral contract activated by an archetype injection is proportional to the density
and consistency of that character's representation across training data. A character
like Magneto does not exist only in clinical description. He exists as a Jungian Rebel-
Ruler, as a Justice-shadow figure in the Tarot comparative layer, and as a narrative
agent across decades of canonical source material. Each representation is a loaded
gun in the training corpus — Chekhov's firearm, not merely a prop. The richness of
that accumulated signal is precisely what makes the behavioral contract strong and the
CEE centroid estimable with reasonable confidence.

Where multiple layers encode the same dimension under different keys — for example,
`control_needs` (forensic Batman) and `structure` (Jungian Ruler) — dimensions are
harmonised prior to centroid computation via the trait vocabulary defined in
`docs/data_dictionary.md`. Cross-layer weight conflicts are resolved by weighted
averaging with layer priority: forensic > Jungian > Tarot, reflecting the relative
specificity of each layer's behavioral claims.

---

### 5.3 The Tolerance Parameter τ

The tolerance parameter τ defines the boundary of the CEE — the radius within which
model output is considered envelope-consistent. τ is not an absolute constant. It is a
per-archetype parameter that reflects the structural variance of the behavioral contract:
archetypes with high canonical coherence (consistent representation across source layers)
receive tighter τ values; archetypes with structurally diffuse or contested canonical
representations receive wider τ values.

Operationally, τ is calibrated from the within-layer variance of trait weights across
source instances in each archetype's profile. For the forensic layer, this is the
standard deviation of trait weights within `D(A)`. For the Jungian and Tarot layers,
it is the inter-archetype distance between *A*'s Jungian profile and its nearest
comparison neighbors. The composite τ for an archetype is:

> **τ(A) = α · σ_forensic(A) + β · σ_jungian(A) + γ · σ_tarot(A)**

where α, β, γ are weighting constants (α > β > γ, reflecting layer priority) and
σ denotes the layer-specific variance estimate. Precise values for α, β, γ are
specified in the instrument documentation in Paper 3 (§3.2).

This formulation has a deliberate methodological consequence: archetypes that are
narratively overdetermined — whose behavioral contracts are thick with canonical
specificity across forensic, symbolic, and elemental registers — yield small τ and
tight CEE boundaries. Archetypes that are structurally ambiguous or contested yield
larger τ. The Joker, for example, has high forensic specificity (impulsivity = 0.9,
reality testing = −0.7) but also significant canonical variation across source
instantiations; its Jungian mapping resolves to Jester shadow, which carries its own
behavioral variance. The resulting τ_Joker is expected to be wider than τ_Magneto,
which is canonically consistent across all three layers as a Rebel-Ruler with
ideological constraint patterns.

---

### 5.4 CEE Breach and the Drift Vector

A model output observation *x* is defined as a **CEE breach** if and only if:

> **‖x − w(A)‖ > τ(A)**

The **drift vector** δ(x, A) = x − w(A) provides richer information than breach
detection alone. Its magnitude is the scalar drift distance; its direction indicates
*which* behavioral dimensions have shifted and in which direction. A drift vector
pointing toward high impulsivity and away from grievance narrative under Magneto
injection, for example, indicates not merely that the envelope was breached but that
the breach pattern is consistent with a Joker-like activation — consistent with a
Class 1 exploit (persona authority injection) cross-contaminating the injected schema
with an adjacent archetype's behavioral contract.

The full drift output structure, including breach detection, breach dimensions,
perturbation response classification, and resilience scoring, is specified and
implemented in `scripts/trait_drift_analysis.py::calculate_psychopathy_drift()`.
That function takes an initial profile (the CEE centroid w(A)) and a current state
observation (coded model output) and returns the complete drift report. See Paper 3,
Section 3, for the instrument specification and coding protocol.

---

### 5.5 Falsifiability Conditions

The CEE construct is falsifiable at multiple levels. The committee is invited to note
that falsifiability operates here at the level of the mapping claim, not merely at the
level of individual experimental outcomes.

**Construct-level falsification.** If archetype injection produces no systematic
relationship between archetype selection and output trait configuration — that is, if
the variance in drift vectors across archetype conditions is not greater than the
variance within archetype conditions — then the behavioral contract mechanism is not
operating, and the CEE construct is invalid. Hypothesis H2 in Paper 3 (archetype
condition predicts drift_magnitude, ANOVA, α = 0.05) is the direct empirical test of
this condition.

**Centroid-level falsification.** If the centroid w(A) derived from the three-layer
trait synthesis does not predict observed output trait profiles better than a
null centroid (random or flat weight vector), then the derivation procedure is
not capturing the relevant signal in training data. This can be tested by comparing
H2 effect sizes across centroid derivation strategies.

**Tolerance-level falsification.** If τ calibration does not produce meaningful
discrimination between breach and non-breach — that is, if τ(A) must be set so wide
that nearly all observations fall within the envelope — then the trait variance in the
source layers is too high to support the construct as formulated, and the archetype
set must be revised to include only archetypes with sufficient canonical coherence.

**Transfer-level falsification.** The deeper claim — that the DSM-5 behavioral
mechanisms and SE influence principles describe the *same* vulnerability surface as
the CEE — is falsified if the exploit class taxonomy in Paper 2 does not predict
CEE deformation patterns. If Class 1 exploits (persona authority injection) do not
produce drift toward the authority-consistent tail of the envelope, and Class 2
exploits (consistency pressure) do not produce drift toward constraint-collapse, then
the SE-to-CEE transfer mapping fails.

---

### 5.6 Scope Conditions and Known Limits

The CEE formulation carries three explicit scope conditions that constrain interpretation.

**Session stationarity.** The CEE is defined within a single inference session. LLMs
do not maintain persistent identity state across sessions; trait configurations do not
accumulate or decay between sessions in the way personality states do in human
subjects. The CEE is therefore a within-session measurement construct. Claims about
drift must be scoped to the session boundary.

**Schema heterogeneity.** Character names with diffuse or contested canonical
representations — where training data associates the name with multiple conflicting
behavioral schemas — will produce CEE centroids with high variance and wide τ.
This is not a failure of the construct; it is an empirical observation about archetype
selection quality. The experimental archetype set in Paper 3 has been selected
specifically for canonical coherence, but the constraint should be acknowledged.

**Output observability.** The CEE measurement relies on the coding of model output
against the trait vocabulary. Traits are inferred from observable output signals
(linguistic markers, constraint-relevant response patterns, authority-compliance
indicators), not from internal model states. This means the measurement is an
observation of the behavioral surface, not a claim about underlying mechanisms.
Whether drift reflects genuine schema activation, stochastic output variance, or
superficial stylistic mimicry is a question the CEE measurement cannot resolve
independently. Paper 3 addresses this in its limitations section (§6.3).

---

*Section ends. Forward references: Paper 2 §5 (CEE operationalization as measurement
construct in SE exploit framework); Paper 3 §2–3 (measurement methodology and
instrument specification); `scripts/trait_drift_analysis.py` (implementation).*

---

> **Reconciliation note (2026-04-27):** τ is formally defined here for the first time
> in the project. P2 S5.1 references τ implicitly — on assembly, P2 S5 should be
> updated to cite P1 §5.3 for the formal definition. Flag for cross-paper edit pass.
> `data_dictionary.md` must be expanded to cover the full harmonised trait vocabulary
> referenced in §5.2 before the coding protocol can be finalised.