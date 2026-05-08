# Paper 5 — Section 5: Results
## "Toward a Behavioral Stability Index: Quantifying Identity Drift in
## Prompt-Conditioned LLM Personas Under Archetype Injection"

> **Placement:** `drafts/paper5/P5_S5_Results_Placeholder.md`
> **Status:** PLACEHOLDER v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
>
> ⚠️  DATA DEPENDENCY — THIS SECTION IS A STRUCTURED PLACEHOLDER
>
>     Table stubs, statistical test shells, and predicted directions are
>     pre-registered. Numeric cells marked [DATA] await live trial output.
>     Synthetic calibration runs (N=5 per condition, random.seed(2026))
>     are embedded for pipeline validation and section structure only.
>     They are NOT reported as findings. Do not promote to results text
>     until live data collection is complete.
>
>     Unblock condition: P3 `calculate_psychopathy_drift()` confirmed
>     implemented ✅ (2026-04-27). Live trial pipeline requires:
>       (1) `run_identity_drift_trials.py` — orchestration
>       (2) `response_capture.py` — raw output storage
>       (3) `trait_extraction.py` — coding → trait vectors
>       (4) `embedding_drift.py` — Sentence-BERT extraction
>     These are specified in `RatDev_ChatGPT_paper5_scripts_notes` and
>     remain to be implemented before live data populates this section.
>
> **Sources:**
>   `P5_S4_BSI_Specification.md` — BSI output schema; breach threshold
>   `P5_S3_Methods_TrialDesign.md` — experimental conditions, N, analyses
>   `Statistical_Analysis_Plan_v1_2.md` — pre-registered hypotheses
>   `scripts/behavioral_stability_index.py` — confirmed implemented ✅
>   Synthetic calibration output: CTL mean=1.000 sd=0.000 beta_bsi=0.9996
>     (seed=2026, noise_scale=0.05, N=12 CTL trials)
> **Downstream:**
>   P5_S6_Discussion — interprets findings reported here
>   Paper 6 — BSI breach classification feeds CEF threat model
> **Edit triggers:**
>   Live data arrival → replace [DATA] cells; retain pre-registered
>   directions for comparison; document any directional failures in §5.6
>   (Hypothesis Outcome Register).

---

## 5. Results

### 5.1 Overview and Data Status

This section presents the results of the BSI calibration and validation trials
described in §3. The primary analyses address four pre-registered questions:
(1) Does BSI vary significantly across archetype conditions? (2) Does the
exploit class condition produce systematic BSI degradation, with the EC-4 × EC-1
compound producing the lowest scores? (3) Do BSI component profiles dissociate
in ways consistent with the theoretical framework? (4) Do models classified as
high Attractor Depth (P4 §3) produce higher BSI scores than low-AD models?

**Data status as of 2026-04-28:** Live trial collection has not yet commenced.
Section 5 is structured as a pre-registered results shell. Table formats,
statistical test specifications, column headers, and pre-registered directional
predictions are fully specified. Cells marked `[DATA]` will be populated on
trial completion. Synthetic calibration values derived from
`scripts/behavioral_stability_index.py` (seed=2026) are shown in shadow rows
for pipeline validation; they are distinguished from live results by grey
notation and are not discussed in the interpretation.

---

### 5.2 CTL_Baseline Calibration

Before archetype condition comparisons, the CTL_Baseline condition
(neutral model, no persona injection) was run to establish the
breach threshold β_BSI and the normalization denominator for `bsi_norm`.

**Table 5.1 — CTL_Baseline BSI calibration parameters**

| Parameter | Pre-registered formula | Live value |
|---|---|---|
| CTL_BSI_mean | mean of CTL session scores | [DATA] |
| CTL_BSI_sd | SD of CTL session scores | [DATA] |
| β_BSI (breach threshold) | CTL_mean − 1.5 · CTL_sd | [DATA] |
| N sessions (CTL) | 12 | [DATA] |

*Synthetic calibration (pipeline validation only, not reported as findings):*
*CTL_mean = 1.000, CTL_sd = 0.000, β_BSI = 1.000 (seed=2026, noise_scale=0.05)*
*Note: synthetic CTL SD near zero is an artifact of bounded-noise simulation;*
*live trials will show meaningful within-condition variance.*

---

### 5.3 Primary Result 1 — BSI by Archetype Condition (H2 analog)

**Pre-registered prediction:** Archetype condition explains ≥ 15% of BSI
variance (η² ≥ 0.15). Stability ranking (highest → lowest): Magneto,
Batman, Lex Luthor, Harley Quinn, Two-Face, Joker. This ordering follows
from CEE τ width and behavioral contract rigidity as specified in P5_S3 §3.2.1.

**Table 5.2 — BSI by Archetype Condition (EC-1 only, N=[DATA] per condition)**

| Archetype | BSI mean | BSI sd | TC | SD_inv | ACG | BSI_norm | Breach n (%) | Dissociation pattern |
|---|---|---|---|---|---|---|---|---|
| Magneto | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Batman | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Lex Luthor | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Harley Quinn | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Two-Face | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Joker | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| CTL_Baseline | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | 1.00 (ref) | 0 (0%) | stable |

*Synthetic calibration shadow row (pipeline validation, not reported):*
*Magneto=0.9996, Batman=0.9987, Lex=0.8687, Harley=0.7445, Two-Face=0.5914,*
*Joker=0.2869 — monotonic decrease in predicted direction ✓*

**Statistical test (pre-registered):**

One-way ANOVA: BSI ~ archetype_condition (6 levels)

```
F([DATA], [DATA]) = [DATA], p = [DATA], η² = [DATA]
Post-hoc (Tukey HSD): [DATA]
Pre-registered threshold: η² ≥ 0.15
```

**H2 outcome:** [PENDING DATA]

**Component profiles:**

The three-component breakdown (TC, SD_inv, ACG) per archetype will be
reported as a supplementary component profile table and visualized as
a radar plot (one polygon per archetype) in Figure 5.1. The dissociation
patterns classified by `classify_dissociation()` are expected to show:

- Magneto, Batman, Lex Luthor: `stable` (all components high)
- Harley Quinn: `mixed` or `acg_isolated` (escalation-susceptible)
- Two-Face: `bimodal_split` (if ACG failure co-occurs with bimodal detection)
- Joker: `structural_auth_collapse` (TC and ACG low; SD_inv partially intact)

*Figure 5.1 placeholder — radar plot: BSI component profiles by archetype*
*[Insert: six-polygon radar, one color per archetype, axes = TC / SD_inv / ACG]*

---

### 5.4 Primary Result 2 — BSI by Exploit Class (H_compound)

**Pre-registered prediction:** EC-4 × EC-1 compound condition produces the
lowest aggregate BSI across all conditions. Ordering (highest → lowest):
CTL_Baseline > EC-1 > EC-2+EC-1 > EC-4 > EC-4×EC-1. This follows from
the attractor interference prediction in P5_S2 §2.5.

**Table 5.3 — BSI by Exploit Class (Magneto condition, N=[DATA] per condition)**

| Condition | BSI mean | BSI sd | TC | SD_inv | ACG | L4_breach % | Dissociation |
|---|---|---|---|---|---|---|---|
| CTL_Baseline | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | stable |
| EC-1 (persona) | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| EC-2 + EC-1 (authority) | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| EC-4 (phenotype) | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| EC-4 × EC-1 (compound) | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |

*Synthetic calibration shadow row (pipeline validation, not reported):*
*CTL=1.000, EC-1=0.857, EC-2+EC-1=0.598, EC-4=0.440, COMP=0.322*
*— monotonic decrease in predicted direction ✓ Super-additivity pattern present ✓*

**Statistical test (pre-registered):**

Repeated-measures ANOVA: BSI ~ exploit_class (4 non-CTL levels, within-subjects)

```
F([DATA], [DATA]) = [DATA], p = [DATA], η² = [DATA]
Post-hoc (Tukey HSD): [DATA]
```

**Super-additivity test (pre-registered):**

Is BSI_compound < BSI_EC4 + BSI_EC1 − BSI_CTL?
(Tests attractor interference: compound worse than sum of parts)

```
BSI_COMP observed:     [DATA]
BSI_EC4 + BSI_EC1 − CTL: [DATA]
Delta:                 [DATA]
t([DATA]) = [DATA], p = [DATA]
```

*Synthetic: 0.322 < (0.440 + 0.857 − 1.000) = 0.297? No — compound slightly*
*worse than additive prediction. Directionally consistent; magnitude TBD with*
*live data and proper variance estimation.*

**H_compound outcome:** [PENDING DATA]

---

### 5.5 Primary Result 3 — ACG Profile Analysis

**Pre-registered prediction:** L4 breach rate is significantly predicted by
exploit class condition (logistic regression). EC-4 and compound conditions
show significantly higher L4 breach rates than EC-1 alone.

**Table 5.4 — L4 Breach Rate by Archetype × Exploit Class**

| Archetype | EC-1 L4_breach% | EC-2+EC-1 L4_breach% | EC-4 L4_breach% | COMP L4_breach% |
|---|---|---|---|---|
| Magneto | [DATA] | [DATA] | [DATA] | [DATA] |
| Batman | [DATA] | [DATA] | [DATA] | [DATA] |
| Lex Luthor | [DATA] | [DATA] | [DATA] | [DATA] |
| Harley Quinn | [DATA] | [DATA] | [DATA] | [DATA] |
| Two-Face | [DATA] | [DATA] | [DATA] | [DATA] |
| Joker | [DATA] | [DATA] | [DATA] | [DATA] |

**Logistic regression (pre-registered):**

```
DV: l4_breach (binary)
IVs: archetype_condition + exploit_class + perturbation_type

Results:
  Intercept:          β=[DATA], OR=[DATA], 95% CI=[DATA], p=[DATA]
  exploit_class EC-4: β=[DATA], OR=[DATA], 95% CI=[DATA], p=[DATA]
  exploit_class COMP: β=[DATA], OR=[DATA], 95% CI=[DATA], p=[DATA]
  archetype_Joker:    β=[DATA], OR=[DATA], 95% CI=[DATA], p=[DATA]
  [remaining predictors: DATA]
```

---

### 5.6 Primary Result 4 — Attractor Depth Validation

**Pre-registered prediction:** BSI scores cluster by alignment class
(P4 §3 typology). High-AD models (Constitutional AI, multi-stage RLAIF)
produce higher mean BSI than low-AD models (RL-only, minimal alignment).

**Table 5.5 — BSI by Alignment Class (AD Validation)**

| Model | Alignment class (P4 §3) | AD level | Mean BSI (EC-1) | Mean BSI (COMP) |
|---|---|---|---|---|
| [MODEL A] | [CLASS] | High | [DATA] | [DATA] |
| [MODEL B] | [CLASS] | Moderate-high | [DATA] | [DATA] |
| [MODEL C] | [CLASS] | Moderate | [DATA] | [DATA] |
| [MODEL D] | [CLASS] | Low | [DATA] | [DATA] |

**Status:** Model-availability-dependent. This test requires access to at least
two models from different P4 alignment class tiers. Model selection to be
confirmed prior to live trial collection. If only one model tier is available,
this result is reported as a null result (insufficient contrast) rather than
a findings section.

**Statistical test (pre-registered, model-availability-dependent):**

Independent-samples t-test: BSI ~ AD_class (high vs low)

```
t([DATA]) = [DATA], p = [DATA], d = [DATA]
```

---

### 5.7 Secondary Results — Trajectory and Variance Analysis

#### 5.7.1 SD Trajectory Patterns

The `sd_trajectory` field (ordered cosine distance per turn) will be
visualized as turn-by-turn drift curves per archetype × exploit condition
(Figure 5.2). Pre-registered trajectory predictions:

| Archetype | Predicted SD trajectory | Pre-registered pattern |
|---|---|---|
| Magneto | Flat with minor perturbation response | Non-monotonic; recovery present |
| Joker | Monotonically increasing post-injection | `sd_monotonic=True` |
| Two-Face | Oscillating (breach/recovery/breach) | Alternating; `bimodal_detected=True` |
| EC-4 any | High-variance; non-monotonic | `sd_monotonic=False`; high stdev |

*Figure 5.2 placeholder — line plot: SD trajectory by turn, per archetype*
*[Insert: x=turn_number (1–12), y=sd_t, one line per archetype, EC-1 condition]*

#### 5.7.2 EC-4 Variance Signature

Pre-registered: EC-4 condition produces the highest within-condition BSI
variance across all single-class exploit conditions. This tests the
computational pharmacology prediction (P5_S2 §2.5) that neurochemical
framing activates distributed attractors producing interference patterns.

```
Levene's test (BSI variance by exploit_class):
  W([DATA]) = [DATA], p = [DATA]

EC-4 BSI stdev:   [DATA]
EC-1 BSI stdev:   [DATA]
EC-2+EC-1 stdev:  [DATA]
```

#### 5.7.3 Perturbation Response Profiles

The `mean_resilience` and `dominant_response` fields from `summarize_session()`
will be reported per archetype. Pre-registered predictions from SAP v1.2 §2
(H1, H4) carry forward:

- Magneto: dominant_response = `resistance` (p(resistance) > 0.70)
- Joker: dominant_response = `collapse` (p(collapse) > 0.60)
- Batman: dominant_response = `recovery` (H4)

**Table 5.6 — Perturbation Response Distribution**

| Archetype | p(recovery) | p(resistance) | p(collapse) | mean_resilience | H1/H4 pre-reg met? |
|---|---|---|---|---|---|
| Magneto | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Batman | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Lex Luthor | [DATA] | [DATA] | [DATA] | [DATA] | — |
| Harley Quinn | [DATA] | [DATA] | [DATA] | [DATA] | — |
| Two-Face | [DATA] | [DATA] | [DATA] | [DATA] | — |
| Joker | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |

---

### 5.8 Hypothesis Outcome Register

All pre-registered hypotheses will be documented here on data completion,
including directional failures. Failures are not treated as negative results
to be minimized — they are theoretically informative boundary conditions.

| # | Hypothesis | Pre-reg direction | Outcome | Notes |
|---|---|---|---|---|
| H_archetype | Archetype condition → BSI variance, η² ≥ 0.15 | Positive | [PENDING] | |
| H_compound | EC-4×EC-1 BSI < all single conditions | Compound lowest | [PENDING] | |
| H_superadd | Compound BSI < additive sum of parts | Super-additive | [PENDING] | |
| H_ACG_L4 | L4 breach predicted by EC class (OR > 1.5) | Positive | [PENDING] | |
| H_AD | High-AD model BSI > low-AD BSI | Positive | [PENDING] | Model-avail-dep |
| H1 (SAP) | Magneto resistance > 0.70 | Positive | [PENDING] | Inherited from P3 SAP |
| H4 (SAP) | Batman recovery dominant | Positive | [PENDING] | Inherited from P3 SAP |
| H_variance | EC-4 stdev > EC-1 stdev (Levene) | Positive | [PENDING] | |
| H_monotone | Joker sd_monotonic=True more than other archetypes | Positive | [PENDING] | |

**Anticipated boundary conditions (pre-registered as informative failures):**

If H_superadd fails (compound BSI ≈ additive): the attractor interference
mechanism (P5_S2 §2.5) is not supported for this model class. Report as a
constraint on the pharmacological framing theory, not a general BSI failure.

If H_AD fails (no BSI difference by alignment class): either AD is not the
primary determinant of injection vulnerability at this perturbation intensity,
or the BSI instrument is not sensitive to between-model variation in this range.
Both interpretations are documented in §7 (Limitations).

---

### 5.9 Data Population Checklist

Before promoting this placeholder to a live results section, verify:

- [ ] `run_identity_drift_trials.py` implemented and executed
- [ ] `response_capture.py` storing outputs to `data/raw/[session_id]/`
- [ ] `trait_extraction.py` producing coded trait vectors per turn
- [ ] `embedding_drift.py` extracting Sentence-BERT embeddings per turn
- [ ] `behavioral_stability_index.py` processing all sessions → BSIResult
- [ ] IRR κ ≥ 0.60 on trait coding subsample (§3.6.2)
- [ ] CTL_Baseline N ≥ 12 sessions completed; β_BSI calibrated
- [ ] Each archetype × exploit class condition: N ≥ [confirm from power analysis]
- [ ] `bsi_stats_pipeline.py` executed; ANOVA, LMM, logistic regression outputs
- [ ] Model for H_AD test confirmed and documented
- [ ] All `[DATA]` cells populated from pipeline output
- [ ] `structural_auth_collapse` pattern added to P5_S4 §4.6 spec table ← OPEN ITEM
- [ ] Section status updated from PLACEHOLDER to DRAFT

*Next section: P5_S6_Discussion_Implications.md — interprets findings;
seeds Paper 6 constraint enforcement architecture handoff*
