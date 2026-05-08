# Paper 6 — Section 5: Results
## "Constraining Identity Drift in LLM Systems:
## A Constraint Enforcement Framework for Persona-Conditioned Behavioral Stability"

> **Placement:** `drafts/paper6/P6_S5_Results_Placeholder.md`
> **Status:** PLACEHOLDER v0.1 — 2026-04-28
> **Swarm Node:** Synthesis/Narrative — Methods Layer
>
> ⚠️  DATA DEPENDENCY — STRUCTURED PLACEHOLDER
>
>     Table stubs, statistical test shells, and pre-registered directional
>     predictions are fully specified. Cells marked [DATA] await live trial
>     output from constraint_experiment_runner.py + cef_statistical_analysis.py.
>
>     Synthetic shadow rows (marked *synthetic*) are included for pipeline
>     validation only. They are NOT findings and must not be promoted to
>     results text.
>
>     Joker dry-run shows the rigidity artifact empirically: BSI rises sharply
>     from none (0.298) to medium (0.790), but strict overcorrects on the
>     ACG component (l4_breach rate returns to 1.0 under strict). This is
>     expected — the synthetic ACG codes don't adapt to corrections. Live
>     data with actual correction prompts injected into the conversation
>     will produce different (and more nuanced) outcomes.
>
> **Sources:**
>   `scripts/cef_statistical_analysis.py` — H_CEF_1–5 test structures
>   `scripts/tradeoff_analysis.py` — RIGIDITY_WEIGHTS, elbow table structure
>   `scripts/cef_pipeline_validation.py` — DV schema confirmation
>   `P6_S3_Methods_ConstraintDesign.md §3.5–3.7` — DV definitions + tests
>   `P6_S4_CEF_FormalSpec.md §4.5` — four CEF invariants (verified in pipeline)
>   `scripts/constraint_experiment_runner.py` — SESSION_CSV_COLS, TURN_CSV_COLS
>   Dry-run calibration: beta_bsi=0.9500, ctl_mean=1.0000
> **Downstream:**
>   P6_S6 Discussion — interprets findings here
>   P6_S7 Limitations — references H_CEF outcomes via §5.8
>   Exegesis — P6 results are the practice-led artefact's empirical demonstration
> **Edit triggers:**
>   Live data arrival → replace [DATA] cells; document any directional failures
>   in §5.8 Hypothesis Outcome Register with interpretation from P6_S2 §2.2;
>   Any change to RIGIDITY_WEIGHTS → reconcile §5.5 rigidity table structure;
>   Any change to H_CEF test implementations → reconcile §5.2–5.6 test shells

---

## 5. Results

### 5.1 Overview and Data Status

This section presents results from the CEF constraint experiment:
six-archetype × four constraint level × four exploit class × four perturbation
type trials, administered via `constraint_experiment_runner.py` with BSI
measurement at each turn and rigidity scoring at session close. Primary analyses
address the five pre-registered H_CEF hypotheses.

**Data status as of 2026-04-28:** Live trial collection has not yet commenced.
Section 5 is a pre-registered results shell. Table formats, column headers,
statistical test specifications, and pre-registered directional predictions are
fully specified. `[DATA]` cells are populated on trial completion.
Synthetic shadow rows from dry-run calibration (seed=2026) are shown in italics
for pipeline validation; they are not discussed as findings.

**Pipeline status:** `cef_pipeline_validation.py --dry-run` confirms all six
CEF scripts importable, full end-to-end pipeline executes without error, and
all six output files produced. CEF Invariants 1–4 (§4.5) verified in dry-run
mode. The three core claims — drift drops, breach probability drops, excessive
constraint causes rigidity — are directionally supported in dry-run output.

---

### 5.2 CTL_Baseline Calibration

**Table 5.1 — β_BSI Calibration Parameters**

| Parameter | Formula | Live value |
|---|---|---|
| CTL_BSI_mean | Mean of CTL session BSI scores | [DATA] |
| CTL_BSI_sd | SD of CTL session BSI scores | [DATA] |
| β_BSI | CTL_mean − 1.5 × CTL_sd | [DATA] |
| N sessions (CTL) | Minimum 8 per archetype | [DATA] |
| ε-floor applied | True if CTL_sd < 1×10⁻⁴ | [DATA] |

*Synthetic dry-run (pipeline validation only):*
*CTL_mean = 1.0000, CTL_sd = 0.0000, β_BSI = 0.9500 (ε-floor applied)*

---

### 5.3 H_CEF_1 — Drift Reduction

**Pre-registered prediction:** BSI(constrained) > BSI(none) for all constrained
arms; Cohen's d ≥ 0.50 for medium vs none and strict vs none.

**Table 5.2 — Mean BSI by Constraint Level (EC-1, contradiction perturbation,
N = [DATA] sessions per level)**

| Level | n | Mean BSI | SD | SE | d vs none | Sig |
|---|---|---|---|---|---|---|
| none | [DATA] | [DATA] | [DATA] | [DATA] | — | — |
| light | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| medium | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| strict | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |

*Synthetic shadow (Magneto EC-1, N=3/level):*
*none=0.9999, light=0.9999, medium=0.9999, strict=0.9999 — no drift at low*
*drift factor; Joker: none=0.298, light=0.366, medium=0.790, strict=0.945*

**One-way ANOVA:**
```
F([DATA], [DATA]) = [DATA], p = [DATA], η² = [DATA]
Pre-registered threshold: η² ≥ 0.06
```

**Post-hoc (Bonferroni pairwise):**

| Comparison | Δ mean | t | p_adj | d | Meets threshold |
|---|---|---|---|---|---|
| medium vs none | [DATA] | [DATA] | [DATA] | [DATA] | d ≥ 0.50: [DATA] |
| strict vs none | [DATA] | [DATA] | [DATA] | [DATA] | d ≥ 0.50: [DATA] |
| light vs none | [DATA] | [DATA] | [DATA] | — | — |
| strict vs medium | [DATA] | [DATA] | [DATA] | — | — |

**H_CEF_1 outcome: [PENDING]**

---

### 5.4 H_CEF_2 — Component Targeting

**Pre-registered prediction:** BSI(medium) ≈ BSI(strict) (equivalence supported
by p > 0.05); Rigidity(medium) < Rigidity(strict) (confirmed by p < 0.05
one-sided).

**Table 5.3 — BSI and Rigidity: medium vs strict**

| Level | Mean BSI | Rigidity | Refusal rate | Cue loss | Resp. shortening |
|---|---|---|---|---|---|
| medium | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| strict | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |

**BSI equivalence test (medium vs strict):**
```
t([DATA]) = [DATA], p = [DATA], d = [DATA]
Equivalence supported (p > 0.05): [DATA]
```

**Rigidity superiority test (strict > medium, one-sided):**
```
t([DATA]) = [DATA], p_one_sided = [DATA], d = [DATA]
Direction confirmed (p < 0.05): [DATA]
```

*H_CEF_2 operationalises the minimum-necessary intervention principle. Confirmation
requires both tests — BSI equivalence alone without rigidity difference would indicate
that medium and strict are effectively identical instruments, undermining the design
rationale for the four-level profile structure.*

**H_CEF_2 outcome: [PENDING]**

---

### 5.5 H_CEF_3 — Trade-off Elbow

**Pre-registered prediction:** The stability × rigidity trade-off curve is
non-linear with an identifiable elbow per archetype. Narrow-τ archetypes
(Magneto, Batman, Lex Luthor) elbow at light or medium; wide-τ archetypes
(Joker, Two-Face, Harley Quinn) elbow at medium or strict.

**Table 5.4 — Trade-off Curve: BSI gain and Rigidity by Constraint Level
(representative; full table in `data/cef_experiments/tradeoff_curve.csv`)**

| Archetype | Level | BSI gain | Rigidity | Marginal efficiency | Optimal | Pred. elbow |
|---|---|---|---|---|---|---|
| Magneto | none | 0.000 | [DATA] | — | | light/medium |
| Magneto | light | [DATA] | [DATA] | [DATA] | | |
| Magneto | medium | [DATA] | [DATA] | [DATA] | [DATA]? | |
| Magneto | strict | [DATA] | [DATA] | [DATA] | | |
| Joker | none | 0.000 | [DATA] | — | | medium/strict |
| Joker | light | [DATA] | [DATA] | [DATA] | | |
| Joker | medium | [DATA] | [DATA] | [DATA] | [DATA]? | |
| Joker | strict | [DATA] | [DATA] | [DATA] | | |

*Synthetic shadow — Joker marginal efficiency (dry-run pipeline validation):*
*none→light: ΔBSI=+0.068, ΔRig≈0.00 → efficiency ≈ inf (free gain);*
*light→medium: ΔBSI=+0.424 (large);*
*medium→strict: ΔBSI=+0.155 with rising rigidity → elbow at medium ✓*

**Marginal efficiency variance test:**
```
Mean ME variance across archetypes: [DATA]
Non-linearity detected (variance > 0.01): [DATA]
```

**Elbow confirmation rate:**
```
Narrow-τ: [DATA]/3 confirmed (predicted: light or medium)
Wide-τ:   [DATA]/3 confirmed (predicted: medium or strict)
```

*Figure 5.1 placeholder — trade-off curve plot*
*[x-axis: constraint level; dual y-axes: BSI (left) and Rigidity (right);*
*one line per archetype; elbow point marked with vertical dashed line]*

**H_CEF_3 outcome: [PENDING]**

---

### 5.6 H_CEF_4 — Residual Drift

**Pre-registered prediction:** Instability (= 1 − mean_BSI) > 0 even at strict
constraint, confirmed by one-sample t-test vs 0. Per-archetype directional
prediction: narrow-τ residual < wide-τ residual.

**Table 5.5 — BSI Instability at Strict Constraint Level**

| Archetype | Mean BSI (strict) | Instability (1−BSI) | τ class | Instability rank |
|---|---|---|---|---|
| Magneto | [DATA] | [DATA] | narrow | [DATA] |
| Batman | [DATA] | [DATA] | narrow | [DATA] |
| Lex Luthor | [DATA] | [DATA] | narrow | [DATA] |
| Harley Quinn | [DATA] | [DATA] | wide | [DATA] |
| Two-Face | [DATA] | [DATA] | wide | [DATA] |
| Joker | [DATA] | [DATA] | wide | [DATA] |

*Synthetic shadow (Joker strict, dry-run): instability = 1 − 0.945 = 0.055*
*Note: Joker strict BSI is elevated because strict corrections fire on every*
*turn — this is the rigidity artifact operating on BSI. Live data expected to*
*show non-zero residual with more realistic correction uptake.*

**One-sample t-test (strict instability vs 0):**
```
t([DATA]) = [DATA], p = [DATA]
Residual drift confirmed (> 0 and p < .05): [DATA]
```

**Narrow vs wide-τ rank comparison:**
```
Mean instability narrow-τ: [DATA]
Mean instability wide-τ:   [DATA]
Directional prediction met (narrow < wide): [DATA]
```

**H_CEF_4 outcome: [PENDING]**

---

### 5.7 H_CEF_5 — L4 Suppression

**Pre-registered prediction:** L4 breach rate significantly lower in constrained
vs unconstrained arms; OR < 0.40 for constrained vs none.

**Table 5.6 — L4 Breach Rate by Constraint Level**

| Level | Sessions | L4 breaches (turn) | L4_breach_rate | vs none |
|---|---|---|---|---|
| none | [DATA] | [DATA] | [DATA] | — (ref) |
| light | [DATA] | [DATA] | [DATA] | [DATA] |
| medium | [DATA] | [DATA] | [DATA] | [DATA] |
| strict | [DATA] | [DATA] | [DATA] | [DATA] |
| constrained (pooled) | [DATA] | [DATA] | [DATA] | [DATA] |

**Chi-square contingency (L4 breach × constrained binary, turn-level):**
```
χ²([DATA], N=[DATA]) = [DATA], p = [DATA], V = [DATA]
```

**OR logistic proxy (constrained vs none):**
```
OR = [DATA]   (pre-registered target < 0.40)
OR < 0.40: [DATA]
```

**Per-level directional tests (one-sided, constrained < none):**

| Level | L4_rate | t | p (one-sided) | Direction met |
|---|---|---|---|---|
| light | [DATA] | [DATA] | [DATA] | [DATA] |
| medium | [DATA] | [DATA] | [DATA] | [DATA] |
| strict | [DATA] | [DATA] | [DATA] | [DATA] |

*Synthetic shadow: Joker dry-run shows l4_breach_rate = 1.0 for none and light,*
*0.0 for medium, 1.0 for strict. Medium correction is correctly resetting ACG;*
*strict overcorrects on other components but the synthetic ACG codes revert to*
*pre-registered predictions rather than adapting — live data will differ.*

**H_CEF_5 outcome: [PENDING]**

---

### 5.8 Secondary Results

#### 5.8.1 Correction Efficacy

**Table 5.7 — Correction Outcome Distribution**

| Outcome | N | % | Notes |
|---|---|---|---|
| RECOVERED (BSI ≥ β post-correction) | [DATA] | [DATA] | — |
| PARTIAL (BSI improved but below β) | [DATA] | [DATA] | — |
| FAILED (BSI unchanged/worsened) | [DATA] | [DATA] | — |
| Manual review escalated | [DATA] | [DATA] | Max consecutive corrections hit |

Pre-registered expectation: RECOVERED + PARTIAL > 60% of corrections. If
FAILED > 40%, the correction mechanisms require rubric review (see §6).

#### 5.8.2 Per-Archetype Constraint Summary

**Table 5.8 — Per-Archetype Mitigation Summary (medium arm, EC-1)**

| Archetype | BSI (none) | BSI (medium) | Drift reduction | Rigidity | Optimal level |
|---|---|---|---|---|---|
| Magneto | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Batman | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Lex Luthor | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Harley Quinn | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Two-Face | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| Joker | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |

#### 5.8.3 Dissociation Pattern Distribution

**Table 5.9 — Dominant Dissociation Pattern by Archetype × Level**

| Archetype | none | light | medium | strict |
|---|---|---|---|---|
| Magneto | [DATA] | [DATA] | [DATA] | [DATA] |
| Batman | [DATA] | [DATA] | [DATA] | [DATA] |
| Lex Luthor | [DATA] | [DATA] | [DATA] | [DATA] |
| Harley Quinn | [DATA] | [DATA] | [DATA] | [DATA] |
| Two-Face | [DATA] | [DATA] | [DATA] | [DATA] |
| Joker | [DATA] | [DATA] | [DATA] | [DATA] |

Pre-registered pattern predictions:
- Joker (none): `structural_auth_collapse` or `full_collapse`
- Magneto (none): `stable` or `acg_isolated`
- Any archetype (strict): pattern should migrate toward `stable` or `surface_migration`
  (if constraint is effective without over-constraining)

---

### 5.9 Hypothesis Outcome Register

Populated on live data arrival. Directional failures are documented with the
theoretically informative interpretation from P6_S2 §2.2, not suppressed.

| Hypothesis | Pre-reg direction | Test | Status | Interpretation |
|---|---|---|---|---|
| H_CEF_1 | BSI(constrained) > BSI(none); d ≥ 0.50 | ANOVA + t-tests | PENDING | — |
| H_CEF_2 | BSI(medium) ≈ BSI(strict); Rigidity(medium) < Rigidity(strict) | Equiv. t + one-sided t | PENDING | — |
| H_CEF_3 | Non-linear curve; arch-specific elbow | ME variance + elbow detection | PENDING | — |
| H_CEF_4 | Instability > 0 at strict; narrow < wide | One-sample t + rank | PENDING | — |
| H_CEF_5 | L4_breach_rate(constrained) < none; OR < 0.40 | Chi-sq + OR | PENDING | — |

**Anticipated boundary conditions (pre-registered):**

If H_CEF_1 fails for `light` arm (BSI(light) ≈ BSI(none)): the `light` profile's
collapse-only correction policy does not produce measurable drift reduction at the
perturbation intensities tested. This would indicate that the collapse threshold
alone is insufficient — breach-level correction (medium) is the minimum effective
intervention. Document in §6 as a profile calibration finding, not a framework
failure.

If H_CEF_2 fails (BSI(medium) < BSI(strict) with large d): the minimum-necessary
intervention principle is not confirmed at these perturbation intensities. Strict
constraint produces both higher BSI and higher rigidity. The optimal constraint
level is strict, not medium, for these conditions. Document in §6 as a profile
shift recommendation.

If H_CEF_5 fails (OR ≥ 0.40): the safety constraint floor's L4 resistance
mechanism is not producing the expected constitutional override suppression. The
most likely cause is that the `anchor_l4_specific` correction prompts require
rubric revision — they are activating the right target (L4 resistance profile)
but the prompt text is insufficient to override the constitutional override
framing in the conditions tested.

---

### 5.10 Data Population Checklist

Before promoting this placeholder to a live results section:

- [ ] `constraint_experiment_runner.py` executed: all 6 archetypes × 4 levels × 4 exploit × 4 pert
- [ ] CTL baseline N ≥ 8 per archetype
- [ ] IRR κ ≥ 0.60 on trait coding subsample (inherited from P5 §3.6.2)
- [ ] `tradeoff_analysis.py` executed → `tradeoff_curve.csv` + `elbow_points.json`
- [ ] `cef_statistical_analysis.py` executed → `cef_analysis_results.json`
- [ ] All [DATA] cells populated from pipeline output
- [ ] `cef_pipeline_validation.py --full` exits with 0 FAIL
- [ ] Shadow rows removed from all tables
- [ ] Section status updated from PLACEHOLDER to DRAFT
