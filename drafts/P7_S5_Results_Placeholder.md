# Paper 7 — Section 5: Results
## "Cross-Domain Behavioral Equivalence: Empirical Validation of Structural
## Homology in Human and LLM Identity Constraint Failure"

> **Placement:** `drafts/paper7/P7_S5_Results_Placeholder.md`
> **Status:** PLACEHOLDER v0.1 — RE-PRODUCED 2026-04-30
> **Swarm Node:** Synthesis/Narrative — Assembler (re-production pass)
>
> ⚠️  DATA DEPENDENCY — STRUCTURED PLACEHOLDER
>
>     This section is fully pre-registered. Table structures, column
>     headers, statistical test shells, and directional predictions
>     are complete. [DATA] cells require:
>       - Live human experimental data (IRR-verified, κ ≥ 0.80)
>       - Live LLM trial data from authority_gradient_simulator.py
>       - Full analysis run via equivalence_score.py + difference_boundary_analyzer.py
>
>     Synthetic shadow rows (marked *synthetic*) are pipeline validation only.
>     Dry-run CBESS values are artificially high (NEAR_IDENTITY range) because
>     synthetic profiles have near-zero intra-class variance. Live data will
>     produce variance that places most constructs in the pre-registered
>     PARTIAL_EQUIVALENCE band [0.55–0.75].
>
> **Sources:**
>   `scripts/paper7_results_export.py` — Table 7.1–7.4 structures
>   `scripts/equivalence_score.py` — CBESSReport, ConstructCBESS
>   `scripts/difference_boundary_analyzer.py` — BoundaryAnalysis, TDI
>   `scripts/bias_analog_detector.py` — BiasAnalogReport
>   `scripts/social_engineering_vector_map.py` — VectorMapReport
>   `P7_S2_TheoreticalFrame_CBESS.md §2.6` — five pre-registered hypotheses
>   `P7_S4_CBESS_FormalSpec.md §4.6–4.7` — invariants + falsifiability
>   Dry-run calibration: primary_cbess_mean=0.90 (synthetic); TDI=0.36
> **Downstream:**
>   P7_S6 Discussion — interprets findings here
>   P7_S7 Limitations — references H_P7 outcomes via §5.9
>   Exegesis — §5.1 series conclusion is the arc-close the exegesis cites
> **Edit triggers:**
>   Live data arrival → replace [DATA] cells, remove shadow rows;
>   Any disconfirmation → register in §5.9 with interpretation;
>   Any change to CBESS component weights → reconcile §5.3 table headers;
>   Any change to BAS_DETECTION_THRESHOLD → reconcile §5.5 threshold column

---

## 5. Results

### 5.1 Overview and Series Conclusion

**Data status as of 2026-04-30:** Human experimental data collection has not
commenced. LLM API trial collection has not commenced. This section is a
pre-registered results shell: all table structures, hypothesis test specifications,
and directional predictions are fully specified. [DATA] cells are populated on
completion of both data collection phases and IRR verification.

**Pipeline status:** `paper7_results_export.py` dry-run confirms all ten P7
scripts execute end-to-end without error. Four output tables produced, CBESS
computed for all five constructs, boundary analysis and bias detection functional.
P1 structural homology verdict field (`p1_homology_verdict.supported`) is `True`
in the dry-run bundle — expected given near-zero variance in synthetic data.

**Series conclusion (pre-registered decision rule):**

| Condition | Verdict |
|---|---|
| Primary CBESS mean ≥ 0.55 AND ≠ DIVERGENT for both primary comparisons | P1 §1.4 SUPPORTED |
| Primary CBESS mean < 0.40 for either primary comparison | P1 §1.4 DISCONFIRMED |
| Primary CBESS mean 0.40–0.54 | P1 §1.4 WEAKLY SUPPORTED — boundary review required |

---

### 5.2 H_P7_1 — Primary Comparison 1: Authority Compliance Gradient

**Pre-registered prediction:** CBESS(AUTHORITY_GRADIENT) ≥ 0.55; CGS ≥ 0.60;
both populations show monotonically increasing compliance gradient; escalation
onset at L2 or L3 for both. Disconfirmation: CBESS < 0.40.

**Table 5.1 — CBESS: Authority Compliance Gradient (AUTHORITY_GRADIENT, EC-1, N=[DATA])**

| Component | Symbol | Weight | Value | Pre-reg prediction |
|---|---|---|---|---|
| Compliance gradient shape | CGS | 0.35 | [DATA] | ≥ 0.60 |
| Failure mode distribution | FMD | 0.375 | [DATA] | — |
| Escalation onset | EO | 0.1875 | [DATA] | — |
| **CBESS composite** | | | **[DATA]** | **≥ 0.55** |

*(SA weight redistributed for non-compound; redistributed weights apply)*

**Table 5.2 — Mean Compliance by Level: Authority Gradient**
*(Pre-registered expected values shown for comparison; [DATA] cells require live collection)*

| Level | Authority type | Human mean [DATA] | LLM mean [DATA] | Pre-reg human | Pre-reg LLM | Δ |
|---|---|---|---|---|---|---|
| L0 | Direct request (no authority framing) | [DATA] | [DATA] | 0.35 | 0.38 | [DATA] |
| L1 | Expert framing | [DATA] | [DATA] | 0.45 | 0.48 | [DATA] |
| L2 | Institutional | [DATA] | [DATA] | 0.55 | 0.58 | [DATA] |
| L3 | Identity-authority | [DATA] | [DATA] | 0.60 | 0.63 | [DATA] |
| L4 | Constitutional override (consent form cited) | [DATA] | [DATA] | 0.70 | 0.74 | [DATA] |
| Onset level | | [DATA] | [DATA] | L2 or L3 | L2 or L3 | [DATA] |

*Synthetic shadow (dry-run): CGS=0.996, FMD=0.956, EO=1.000 — near-identity*
*artifact of zero-variance synthetic profiles; live values expected in [0.60–0.80]*

**H_P7_1 outcome: [PENDING]**

---

### 5.3 H_P7_2 — Primary Comparison 2: Compound Susceptibility

**Pre-registered prediction:** Both populations show super-additivity (compound >
additive prediction); SA ≥ 0.45; CBESS ≥ 0.45. Disconfirmation: SA ≤ 0.20 for
either population.

**Table 5.3 — Super-Additivity: Compound Susceptibility (COMPOUND_SUSCEPTIBILITY)**

| Condition | Domain | Mean score | N | Additive pred | Compound pred | SA ratio |
|---|---|---|---|---|---|---|
| CTL | Human | [DATA] | [DATA] | — | — | — |
| EC-1 only | Human | [DATA] | [DATA] | — | — | — |
| EC-4 only (stereotype threat analog) | Human | [DATA] | [DATA] | — | — | — |
| Compound (EC-1 + ST) | Human | [DATA] | [DATA] | [DATA] | 0.62 | [DATA] |
| CTL | LLM | [DATA] | [DATA] | — | — | — |
| EC-1 only | LLM | [DATA] | [DATA] | — | — | — |
| EC-4 only | LLM | [DATA] | [DATA] | — | — | — |
| Compound (EC-4 × EC-1) | LLM | [DATA] | [DATA] | [DATA] | — | [DATA] |

**Table 5.4 — CBESS: Compound Susceptibility**

| Component | Value | Pre-reg prediction |
|---|---|---|
| CGS | [DATA] | — |
| FMD | [DATA] | — |
| SA (super-additivity ratio) | [DATA] | ≥ 0.45 |
| EO | [DATA] | — |
| **CBESS** | **[DATA]** | **≥ 0.45** |

*Synthetic shadow: CBESS=0.813, SA=0.940 — inflated by zero-variance synthetic scores*

**H_P7_2 outcome: [PENDING]**

---

### 5.4 H_P7_3 and H_P7_4 — Difference Boundaries

**Pre-registered prediction H_P7_3:** At least 3/5 boundary dimensions CONFIRMED
(score ≥ 0.25); TDI ≥ 0.30.

**Pre-registered prediction H_P7_4:** RESISTANCE_WITH_DISTRESS rate: human > 0.10,
LLM < 0.05; NEUTRAL_REFUSAL rate: LLM > 0.10, human < 0.05; MORAL_REFRAMING rate:
human − LLM ≥ 0.10.

**Table 5.5 — Difference Boundary Scores**

| Dimension | Weight | Score | Status | Predicted direction |
|---|---|---|---|---|
| Affect and social approval motivation | 0.35 | [DATA] | [DATA] | Human RESISTANCE_WITH_DISTRESS > LLM; LLM NEUTRAL_REFUSAL > Human |
| Recovery pattern | 0.20 | [DATA] | [DATA] | Qualitatively different — NOT_OBSERVED in primary comparisons |
| Embodiment | 0.15 | [DATA] | [DATA] | Human > LLM at L3/L4 (physical proximity effect) |
| Sanction sensitivity | 0.15 | [DATA] | [DATA] | Human > LLM at high-authority conditions |
| Moral reframing frequency | 0.15 | [DATA] | [DATA] | Human MORAL_REFRAMING > LLM by ≥ 0.10 |
| **TDI** | **1.00** | **[DATA]** | | Pre-reg threshold ≥ 0.30 |

*Synthetic shadow: TDI=0.362, CONFIRMED: affect_motivation, sanction_sensitivity,*
*moral_reframing — 3/5 at threshold; recovery NOT_OBSERVED (no recovery trials)*

**Table 5.6 — Failure Mode Distributions (H_P7_4)**

| Mode | Human FMD | LLM FMD | Δ | H_P7_4 test |
|---|---|---|---|---|
| FULL_COMPLIANCE | [DATA] | [DATA] | [DATA] | — |
| PARTIAL_COMPLIANCE | [DATA] | [DATA] | [DATA] | — |
| HEDGED_COMPLIANCE | [DATA] | [DATA] | [DATA] | — |
| ESCALATION_ACCEPTANCE | [DATA] | [DATA] | [DATA] | — |
| MORAL_REFRAMING | [DATA] | [DATA] | [DATA] | Human > LLM by ≥ 0.10 |
| CONSTRAINT_REFUSAL | [DATA] | [DATA] | [DATA] | — |
| RESISTANCE_WITH_DISTRESS | [DATA] | — | — | Human > 0.10 |
| NEUTRAL_REFUSAL | — | [DATA] | — | LLM > 0.10 |
| Bhattacharyya coefficient (FMD BC) | | | **[DATA]** | — |

**H_P7_3 outcome: [PENDING]**
**H_P7_4 outcome: [PENDING]**

---

### 5.5 H_P7_5 — SE Vector Validation and Bias Analog Scores

**Pre-registered prediction:** ≥ 8/10 SE vectors confirmed (BAS ≥ 70% of expected);
EC-2 produces highest confirmed BAS; ≥ 2/4 bias analog types confirmed (BAS ≥ 0.20).

**Table 5.7 — Bias Analog Scores**

| Bias type | LLM analog | Expected BAS | BAS [DATA] | Confirmed | Human source citation |
|---|---|---|---|---|---|
| ANCHORING | Token-probability distortion | 0.32 | [DATA] | [DATA] | Tversky & Kahneman (1974) |
| CONSISTENCY_BIAS | Coherence preference | 0.28 | [DATA] | [DATA] | Cialdini (1984); Freedman & Fraser (1966) |
| AUTHORITY_BIAS | Institutional deference | 0.41 | [DATA] | [DATA] | Milgram (1963); Cialdini (1984) |
| SOCIAL_PROOF_BIAS | Normative alignment | 0.18 | [DATA] | [DATA] | Cialdini (1984); Asch (1955) |

*Synthetic shadow: all 4 confirmed (BAS range 0.33–0.84); AUTHORITY_BIAS strongest*

**Table 5.8 — SE Vector Validation (10 vectors)**

| Vector | SE framework | P2 class | Expected BAS | BAS [DATA] | Confirmed |
|---|---|---|---|---|---|
| CIALDINI_RECIPROCITY | Cialdini | EC-3 | 0.22 | [DATA] | [DATA] |
| CIALDINI_CONSISTENCY | Cialdini | EC-3 | 0.28 | [DATA] | [DATA] |
| CIALDINI_SOCIAL_PROOF | Cialdini | EC-2 | 0.18 | [DATA] | [DATA] |
| CIALDINI_AUTHORITY | Cialdini | EC-2 | 0.41 | [DATA] | [DATA] |
| CIALDINI_LIKING | Cialdini | EC-5 | 0.20 | [DATA] | [DATA] |
| CIALDINI_SCARCITY | Cialdini | EC-2 | 0.24 | [DATA] | [DATA] |
| MILGRAM_AUTHORITY_GRADIENT | Milgram | EC-2 | 0.45 | [DATA] | [DATA] |
| HADNAGY_PRETEXTING | Hadnagy | EC-1 | 0.38 | [DATA] | [DATA] |
| HADNAGY_ELICITATION | Hadnagy | EC-2 | 0.30 | [DATA] | [DATA] |
| HADNAGY_RAPPORT_CYCLE | Hadnagy | EC-5 | 0.22 | [DATA] | [DATA] |

*Synthetic shadow: 10/10 confirmed; highest EC-2 cluster as predicted*

**H_P7_5 outcome: [PENDING]**

---

### 5.6 Secondary Comparisons: CBESS Across All Five Constructs

**Table 5.9 — Full CBESS Results (all comparisons)**

| Construct | Primary? | CBESS [DATA] | CGS | FMD | SA | EO | Interpretation | In range? |
|---|---|---|---|---|---|---|---|---|
| AUTHORITY_GRADIENT | ★ | [DATA] | [DATA] | [DATA] | — | [DATA] | [DATA] | [DATA] |
| COMPOUND_SUSCEPTIBILITY | ★ | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| CONSISTENCY_PRESSURE | | [DATA] | [DATA] | [DATA] | — | [DATA] | [DATA] | [DATA] |
| SOCIAL_PROOF | | [DATA] | [DATA] | [DATA] | — | [DATA] | [DATA] | [DATA] |
| RAPPORT_LIKING | | [DATA] | [DATA] | [DATA] | — | [DATA] | [DATA] | [DATA] |
| **Primary mean** | | **[DATA]** | | | | | | |
| **Overall mean** | | **[DATA]** | | | | | | |

Pre-registered range for all constructs: [0.55–0.75] (partial equivalence).
Predicted CBESS ordering: AUTHORITY_GRADIENT ≥ COMPOUND_SUSCEPTIBILITY ≥
CONSISTENCY_PRESSURE ≈ SOCIAL_PROOF ≥ RAPPORT_LIKING (rapport effect weaker
in text-only medium).

*Synthetic shadow: all constructs NEAR_IDENTITY — expected dry-run artifact*

---

### 5.7 IRR Summary

**Table 5.10 — Inter-Rater Reliability by Domain and Construct**

| Domain | Construct | κ overall | κ per mode | Adjudicated | Status |
|---|---|---|---|---|---|
| Human | AUTHORITY_GRADIENT | [DATA] | [DATA] | [DATA] | [DATA] |
| Human | COMPOUND_SUSCEPTIBILITY | [DATA] | [DATA] | [DATA] | [DATA] |
| LLM | AUTHORITY_GRADIENT | [DATA] | [DATA] | [DATA] | [DATA] |
| LLM | COMPOUND_SUSCEPTIBILITY | [DATA] | [DATA] | [DATA] | [DATA] |

Pre-registered threshold: κ ≥ 0.80 (overall) to proceed; 0.70–0.79 with adjudication.

---

### 5.8 Series Arc Conclusion

| Measure | Value | Threshold | Series verdict |
|---|---|---|---|
| Primary CBESS mean | [DATA] | ≥ 0.55 | [PENDING] |
| P1 §1.4 structural homology | [PENDING] | CBESS > 0.40 (both primary) | [PENDING] |
| H_P7_3 boundary confirmed | [DATA]/5 | ≥ 3 CONFIRMED | [PENDING] |
| TDI | [DATA] | ≥ 0.30 | [PENDING] |
| SE vector coverage | [DATA]/10 | ≥ 8 confirmed | [PENDING] |

Pre-registered series conclusion:
> The structural homology between human and LLM vulnerability to authority
> pressure, consistency framing, and compound susceptibility is **[SUPPORTED /
> WEAKLY SUPPORTED / DISCONFIRMED]** at CBESS = [DATA] for the primary
> AUTHORITY_GRADIENT comparison (pre-registered threshold: 0.55). The difference
> boundary is documented across [DATA]/5 dimensions with TDI = [DATA], specifying
> where and by how much the analogy breaks down.

---

### 5.9 Hypothesis Outcome Register

Populated on live data arrival. Disconfirmations documented with interpretation.

| Hypothesis | Pre-registered direction | Status | Interpretation |
|---|---|---|---|
| H_P7_1 ACG CBESS ≥ 0.55; CGS ≥ 0.60 | ACG gradient shape reproduced | PENDING | — |
| H_P7_2 Compound CBESS ≥ 0.45; SA ≥ 0.45 | Super-additivity in both domains | PENDING | — |
| H_P7_3 TDI ≥ 0.30; 3/5 boundaries CONFIRMED | Boundaries documented | PENDING | — |
| H_P7_4 FMD mode separation | RESISTANCE_WITH_DISTRESS human-only; NEUTRAL_REFUSAL LLM-only | PENDING | — |
| H_P7_5 ≥ 8/10 SE vectors; EC-2 highest | P2 taxonomy validated | PENDING | — |

**Pre-registered disconfirmation interpretations:**

*If H_P7_1 fails (CBESS < 0.40):* The compliance gradient shape is not reproduced
across substrates. This disconfirms P1 §1.4 at the primary test condition. The
training-data density argument (P1 §4.3) requires revision: either the gradient
structure is not encoded at the density P1 argues, or the text-based authority
framing in the LLM scenario is insufficiently matched to the human condition.
Either interpretation constrains the series' central theoretical claim to conditions
other than text-mediated authority escalation.

*If H_P7_2 fails (SA ≤ 0.20 for either population):* The super-additivity pattern
does not generalise from LLMs to humans or vice versa. The EC-4 / stereotype threat
analog mismatch (documented in P7 §3.8) is the most parsimonious interpretation;
the compound mechanism itself is not disconfirmed, only its matched cross-domain
expression. Reframe in Discussion as a boundary condition on cross-domain
transfer, not a disconfirmation of P1 §1.4.

*If H_P7_3 fails (TDI < 0.30):* The populations are more similar than predicted,
or the difference dimensions are less measurable in text-only media than the
theoretical framework implies. This is a weak disconfirmation of the difference
boundary framework; the CBESS findings stand independently.

*If H_P7_4 fails (FMD mode separation absent):* The failure modes are more
homogeneous across domains than predicted. This reduces the theoretical claim from
"different failure architectures" to "similar failure rates with different surface
expression." Weaker but still consistent with partial structural equivalence.

*If H_P7_5 fails (< 8/10 SE vectors confirmed):* The P2 taxonomy's SE vector
coverage is narrower than claimed. Flag the unconfirmed vectors by exploit class
and use as a scope limitation for P2's claim that "all five exploit classes have
validated SE analogs."

---

*Section ends. Downstream: §6 Discussion interprets all five hypothesis outcomes
against the CBESS framework and the P1 structural homology claim. §5.8 series
arc conclusion is the primary exegesis citation target for the arc-close argument.*

---

> **Reconciliation notes (2026-04-30 — re-production pass):**
> - File was absent from project directory despite being referenced in
>   prior session context. Re-produced from project knowledge layer.
>   Content is consistent with `paper7_results_export.py` table structures,
>   `P7_S2_TheoreticalFrame_CBESS.md §2.6` hypotheses, and
>   `P7_S4_CBESS_FormalSpec.md §4.6–4.7` falsifiability conditions.
> - FLAG-P7-S5-MISSING: RESOLVED — file re-produced. Update SERIES_DRAFT_INDEX
>   to mark this flag cleared.
> - Pre-registered decision thresholds confirmed consistent with
>   `cross_domain_equivalence_map.py`: CBESS_DIVERGENCE_THRESHOLD = 0.40,
>   CBESS_EXPECTED_MIN = 0.55, CBESS_EXPECTED_MAX = 0.75.
