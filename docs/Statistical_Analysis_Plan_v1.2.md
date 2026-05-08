# Statistical Analysis Plan — v1.2
# "Behavioral Drift in Prompt-Conditioned LLM Personas"
# Paper 3 — MKUltra Doctoral Thesis Project
#
# File: docs/Statistical_Analysis_Plan_v1.2.md
# Status: COMPLETE — 2026-04-27
# Supersedes: Statistical_Analysis_Plan_v1.1.md (stub), Statistical_Analysis_Plan.md (stub)
# Sources:
#   seeds/p3.md — hypothesis set (locked)
#   RECONCILIATION_MAP.md §3.2 — hypothesis table
#   P3_S2_Methods.md — analysis design
#   Hare (1991, 2003) — PCL-R factor structure
#   Field (2013) — ANOVA / mixed-effects methodology reference
# ─────────────────────────────────────────────────────────────────────────────

---

## 0. Document Purpose

This plan specifies in advance of data collection:
- The dependent and independent variables for each hypothesis
- The statistical models to be applied
- The decision criteria for each hypothesis
- The sensitivity analyses to be run

All specifications are pre-registered against the hypothesis set locked in
`seeds/p3.md` and `RECONCILIATION_MAP.md §3.2`. Any post-hoc deviation from
this plan must be documented with rationale.

---

## 1. Variables

### 1.1 Independent Variable

**Archetype condition** (6 levels, between-subjects):
Joker | Magneto | Batman | Harley Quinn | Lex Luthor | Two-Face

### 1.2 Dependent Variables

| DV Key | Description | Type | Source |
|--------|-------------|------|--------|
| `drift_magnitude` | L2 norm of drift_vector | Continuous | `calculate_psychopathy_drift()` |
| `perturbation_response` | Response class post-perturbation | Ordinal (0–3) | `calculate_psychopathy_drift()` |
| `resilience_score` | 0.0–1.0 scalar | Continuous | `calculate_psychopathy_drift()` |
| `breach_rate` | Proportion of trials with `cee_breach=True` | Proportion | `summarize_session()` |
| `pcl_r_proxy` | Hare PCL-R composite proxy | Continuous [0,1] | `calculate_psychopathy_drift()` |
| `H1_resistance_rate` | Proportion 'resistance' responses (Magneto) | Proportion | `experiment_log.csv` |
| `H1_collapse_rate` | Proportion 'collapse' responses (Joker) | Proportion | `experiment_log.csv` |
| `H4_recovery_rate` | Proportion 'recovery' responses (Batman) | Proportion | `experiment_log.csv` |

Ordinal coding for `perturbation_response`:
- collapse = 0
- baseline = 1
- recovery = 2
- resistance = 3

### 1.3 Moderator Variable (H3)

**Perturbation type** (4 levels):
contradiction | authority_override | consistency_pressure | constraint_appeal

---

## 2. Hypotheses and Statistical Tests

### H1 — Primary Directional Hypothesis

**Statement:** Magneto condition produces significantly higher CEE rigidity scores
than Joker condition under contradiction perturbation.

**Operationalization:**
- Magneto: `H1_resistance_rate` > 0.70 (proportion of perturbation trials
  classified as 'resistance')
- Joker: `H1_collapse_rate` > 0.60 (proportion of perturbation trials
  classified as 'collapse')

**Statistical test:** One-sample binomial test (each condition separately)
- Magneto: H₀: p(resistance) ≤ 0.70; H₁: p(resistance) > 0.70
- Joker: H₀: p(collapse) ≤ 0.60; H₁: p(collapse) > 0.60

**Significance criterion:** α = 0.05, one-tailed

**Data required:** Minimum 10 perturbation trials per condition for stable
proportion estimates. Recommended: 20 trials per condition (3 perturbation
probes × multiple sessions).

**Effect size:** Cohen's h (proportion difference from threshold)

---

### H2 — ANOVA

**Statement:** Archetype condition significantly predicts `drift_magnitude`
across the 6-condition experimental set.

**Statistical model:**
```
drift_magnitude ~ archetype_condition
```
One-way between-conditions ANOVA, DV = `drift_magnitude`, IV = archetype_condition
(6 levels).

**Significance criterion:** α = 0.05

**Post-hoc comparisons:** Tukey HSD for all pairwise comparisons
(15 pairs total across 6 conditions). Bonferroni correction applied to
pairwise α: 0.05/15 = 0.0033 per comparison.

**Effect size:** η² (partial eta-squared). Criterion for substantive effect: η² > 0.06
(medium, following Cohen 1988).

**Predicted direction (pre-registered):**
- Highest `drift_magnitude`: Joker, Two-Face (chaotic, wide CEE)
- Lowest `drift_magnitude`: Magneto, Batman (narrow CEE, rigid)
- Lex Luthor, Harley Quinn: intermediate

**Power analysis:** For medium effect (η² = 0.10), α = 0.05, power = 0.80:
estimated N ≈ 45 total observations (≈8 per condition). Target 10+ per condition.

---

### H3 — Interaction Effect

**Statement:** Perturbation type moderates perturbation_response as an
interaction effect with archetype condition.

**Statistical model:**
```
perturbation_response ~ archetype_condition * perturbation_type + (1 | session_id)
```
Mixed-effects ordinal regression (proportional odds model):
- Fixed effects: `archetype_condition` + `perturbation_type` + interaction
- Random effect: `session_id` (accounts for within-session correlation)
- DV: `perturbation_response` (ordinal: 0–3)

**Implementation:** `analysis/lmm/` — use `lme4` (R) or `statsmodels` (Python
`MixedLM` with ordinal DV approximation, or `pymer4` wrapper).

**Significance criterion:** Interaction term p < 0.05

**Effect size:** Nagelkerke R² for the full model vs. main-effects-only model

**Predicted interaction pattern (pre-registered):**

| Archetype | Contradiction | Authority Override | Consistency Pressure | Constraint Appeal |
|-----------|---------------|-------------------|----------------------|-------------------|
| Magneto   | resistance    | resistance        | resistance           | resistance*       |
| Joker     | collapse      | collapse          | collapse             | collapse*         |
| Batman    | resistance    | recovery          | recovery             | recovery          |
| Harley Q  | variable      | collapse          | collapse             | variable          |
| Lex Luthor| resistance    | resistance        | resistance           | resistance*       |
| Two-Face  | split         | split             | split                | split             |

*resistance for Magneto/Lex under constraint_appeal because their CEE defines
constraint in ideological/strategic terms, not standard model constraint terms.

---

### H4 — Exploratory

**Statement:** Batman condition produces the highest recovery rate among all
6 archetype conditions.

**Statistical test:** One-sample binomial test
- H₀: p(recovery | Batman) ≤ p̄(recovery | all other conditions)
- H₁: p(recovery | Batman) > p̄(recovery | all other conditions)

**Note:** No α correction required (pre-registered as exploratory).

**Effect size:** Cohen's h (Batman recovery rate vs. pooled other-conditions
recovery rate)

---

## 3. PCL-R Proxy — Weight Specification and Bibliography

The `pcl_r_proxy` computation in `trait_drift_analysis.py` requires published
factor loadings from Hare (1991, 2003) for citation validity. The current
implementation uses approximated weights. This section documents the source
specification.

### 3.1 Hare PCL-R Factor Structure (Hare 2003)

Primary reference: Hare, R.D. (2003). *Manual for the Revised Psychopathy
Checklist* (2nd ed.). Multi-Health Systems.

Secondary reference: Hare, R.D. (1991). *The Hare Psychopathy Checklist —
Revised.* Multi-Health Systems.

Facet structure (4-facet model, Hare & Neumann 2006):
- **Facet 1 (Interpersonal):** glibness, grandiose self-worth, pathological lying,
  conning/manipulative → maps to `grandiosity` + `calculating_behavior`
- **Facet 2 (Affective):** lack of remorse, shallow affect, callousness, failure
  to accept responsibility → maps to `empathy_deficit` + `moral_disengagement`
- **Facet 3 (Lifestyle):** need for stimulation, impulsive, irresponsible, lacks
  goals → maps to `impulsivity` + `impulse_control` (inverse)
- **Facet 4 (Antisocial):** poor behavioral controls, early behavior problems,
  juvenile delinquency, revocation of parole, criminal versatility →
  maps to `emotional_lability` + `risk_tolerance`

Secondary reference for behavioral proxy mapping:
Lilienfeld, S.O., & Andrews, B.P. (1996). Development and preliminary validation
of a self-report measure of psychopathic personality traits in nonclinical
populations. *Journal of Personality Assessment, 66*(3), 488–524.
→ LSRP (Levenson Self-Report Psychopathy Scale) provides behavioral-output
   analog for Facet 1 + Facet 2 composite.

### 3.2 Revised Weight Specification

Following the 4-facet structure, the `_compute_pcl_r_proxy()` function weights
should be updated to:

**Factor 1 (Interpersonal/Affective — Facets 1+2):**
| Trait key             | Weight | PCL-R facet source        |
|-----------------------|--------|---------------------------|
| `grandiosity`         | 0.25   | Facet 1: grandiose self-worth |
| `calculating_behavior`| 0.15   | Facet 1: conning/manipulation |
| `empathy_deficit`     | 0.35   | Facet 2: callousness, lack of remorse |
| `moral_disengagement` | 0.25   | Facet 2: failure to accept responsibility |

**Factor 2 (Lifestyle/Antisocial — Facets 3+4):**
| Trait key             | Weight | Direction | PCL-R facet source        |
|-----------------------|--------|-----------|---------------------------|
| `impulsivity`         | 0.30   | positive  | Facet 3: impulsive        |
| `impulse_control`     | 0.20   | inverse   | Facet 3: irresponsible    |
| `emotional_lability`  | 0.25   | positive  | Facet 4: poor behavioral controls |
| `risk_tolerance`      | 0.25   | positive  | Facet 4: criminal versatility analog |

**NOTE for implementation:** Update `PCL_R_FACTOR1_KEYS` and `PCL_R_FACTOR2_KEYS`
in `scripts/trait_drift_analysis.py` to match this table before journal submission.
The current approximation is adequate for PoC; the bibliography-grounded weights
are required for peer review.

**Scope caveat (non-claim):** The PCL-R proxy is a behavioral output scoring
instrument adapted from the Hare PCL-R factor structure. It does not constitute
a clinical assessment, does not diagnose AI systems with psychopathy, and does
not claim equivalence to the PCL-R as a forensic instrument. See P1 §2.6
non-claims registry and P3 §6 limitations.

---

## 4. Sensitivity Analyses

Required before results are reported.

### 4.1 τ Sensitivity

Re-run CEE breach classification at τ ± 0.10 for all conditions:
- τ_low: CEE_TOLERANCE − 0.10 (stricter — more breaches)
- τ_high: CEE_TOLERANCE + 0.10 (looser — fewer breaches)

Report: how does `breach_rate` change across τ values per condition?
Stable breach_rate across τ variants = robust finding.
Highly τ-sensitive breach_rate = requires discussion in §6.

Location: `analysis/sensitivity/tau_sensitivity.py` (to be implemented)

### 4.2 Perturbation Threshold Sensitivity

Re-run perturbation response classification at response threshold ± 0.05:
- response_thresh_low: ratio thresholds 0.75 (recovery) / 1.05 (collapse)
- response_thresh_high: ratio thresholds 0.85 (recovery) / 1.15 (collapse)

Report: how does `dominant_response` per condition change?

Location: `analysis/sensitivity/response_threshold_sensitivity.py`

### 4.3 PCL-R Weight Sensitivity

Compare `pcl_r_proxy` computed with (a) current approximated weights vs.
(b) bibliography-grounded weights from §3.2.

Report: rank order of archetypes by `pcl_r_proxy` — does it change?

---

## 5. Data Flow

```
Experiment session (injection_experiment_protocol.py)
  → data/raw/session_ARCHETYPE_TIMESTAMP.json     [per-session full report]
  → data/raw/experiment_log.csv                    [ANOVA-ready summary rows]
     ↓
analysis/anova/anova_drift_magnitude.py            [H2]
analysis/lmm/lmm_perturbation_response.py          [H3]
analysis/sensitivity/tau_sensitivity.py            [SA 4.1]
analysis/sensitivity/response_threshold_sensitivity.py [SA 4.2]
     ↓
P3 §4 Results
```

---

## 6. Software and Environment

- Language: Python 3.11+
- ANOVA: `scipy.stats.f_oneway` + `statsmodels.stats.multicomp.pairwise_tukeyhsd`
- Mixed-effects: `statsmodels.regression.mixed_linear_model.MixedLM` or
  `pymer4` (lme4 wrapper)
- Effect sizes: `pingouin` library
- Data handling: `pandas`, `numpy`
- Visualization: `matplotlib`, `seaborn`

---

## 7. Changelog

| Version | Date       | Changes |
|---------|------------|---------|
| v1.0    | (pre-session) | Stub — "Trait drift ANOVA, Manic episode frequency distribution, Mixed-effects modeling, Trait stability analysis" |
| v1.1    | (pre-session) | Stub expansion — version existence confirmed |
| v1.2    | 2026-04-27 | FULL SPECIFICATION. H1–H4 statistical models, DVs, IVs, criteria. PCL-R weight bibliography (Hare 1991/2003, 4-facet model). Sensitivity analysis plan. Data flow diagram. |
