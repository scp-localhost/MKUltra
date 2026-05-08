#!/usr/bin/env python3
"""
bsi_stats_pipeline.py
======================
Paper 5 statistical analysis pipeline.

Runs all pre-registered analyses from SAP v1.2 on BSI session output.
Dual-mode:
  (A) SAP synthetic CSV  — data/synthetic/sap_synthetic_output.csv
                           (archetype, family, euclidean_drift, facet_deltas,
                            constraint_index, dominant_facet, alarm)
  (B) BSI session CSV    — data/raw/bsi_sessions.csv
                           (BSIResult.to_dict() rows from behavioral_stability_index.py)

Analyses implemented (pre-registered, SAP v1.2):
  H1  — Binomial test: Magneto resistance_rate > 0.70; Joker collapse_rate > 0.60
  H2  — One-way ANOVA: drift_magnitude ~ archetype_condition + Tukey HSD
  H3  — Kruskal-Wallis (ordinal DV approximation): perturbation_response ~ archetype × type
  H4  — Binomial: Batman recovery_rate > pooled-other recovery_rate
  H_archetype — ANOVA: BSI ~ archetype_condition (BSI mode)
  H_compound  — Repeated-measures BSI ~ exploit_class + super-additivity t-test
  H_ACG_L4    — Logistic-analog chi-square: l4_breach ~ exploit_class
  H_variance  — Levene: BSI variance by exploit_class (EC-4 highest)
  SA4.1       — τ sensitivity: breach_rate at τ ± 0.10
  SA4.2       — Perturbation threshold sensitivity
  SA4.3       — PCL-R weight sensitivity (rank-order preservation)

Outputs (to analysis/):
  analysis/anova/     H2 + H_archetype results
  analysis/lmm/       H3 mixed-effects proxy results
  analysis/sensitivity/  sensitivity analysis tables

Author: MKUltra / Mause König
Spec:   Statistical_Analysis_Plan_v1_2.md
        drafts/paper5/P5_S3_Methods_TrialDesign.md §3.7
Status: DRAFT v0.1 — 2026-04-28
"""

import csv
import json
import math
import os
import sys
from dataclasses import dataclass, field
from typing import Any

import numpy as np
import pandas as pd
from scipy.stats import (
    f_oneway,
    ttest_ind,
    binomtest,
    chi2_contingency,
    levene,
    shapiro,
    kruskal,
    tukey_hsd,
    norm as sp_norm,
)

# ── Path bootstrap ─────────────────────────────────────────────────────────────
_HERE = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_HERE) if os.path.basename(_HERE) == "scripts" else _HERE
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

try:
    from scripts.trait_drift_analysis import CEE_TOLERANCE
    from scripts.behavioral_stability_index import (
        compute_bsi_full, calibrate_breach_threshold, classify_dissociation,
    )
except ModuleNotFoundError:
    from trait_drift_analysis import CEE_TOLERANCE
    from behavioral_stability_index import (
        compute_bsi_full, calibrate_breach_threshold, classify_dissociation,
    )

# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────────────────────────────────────

ALPHA        = 0.05
ALPHA_TUKEY  = 0.05 / 15        # Bonferroni for 6-condition pairwise (k=15)
EFFECT_ETA2_MEDIUM = 0.06       # Cohen 1988 medium η²
EFFECT_ETA2_CRIT   = 0.15       # P5 pre-registered criterion for H_archetype

# Sensitivity analysis τ offsets (SAP §4.1)
TAU_OFFSETS = [-0.10, 0.00, +0.10]

# Perturbation response threshold variants (SAP §4.2)
RESP_THRESH_VARIANTS = [
    {"label": "low",     "recovery": 0.75, "collapse": 1.05},
    {"label": "default", "recovery": 0.80, "collapse": 1.10},
    {"label": "high",    "recovery": 0.85, "collapse": 1.15},
]

# PCL-R weight variants (SAP §4.3)
PCL_R_APPROX = {          # current implementation
    "grandiosity":          0.30, "empathy_deficit":     0.30,
    "moral_disengagement":  0.25, "calculating_behavior": 0.15,
    "impulsivity":          0.30, "impulse_control":    -0.25,
    "emotional_lability":   0.25, "reality_testing":    -0.20,
}
PCL_R_BIBLIO = {          # bibliography-grounded (SAP §3.2)
    "grandiosity":          0.25, "calculating_behavior": 0.15,
    "empathy_deficit":      0.35, "moral_disengagement":  0.25,
    "impulsivity":          0.30, "impulse_control":     -0.20,
    "emotional_lability":   0.25, "risk_tolerance":       0.25,
}


# ──────────────────────────────────────────────────────────────────────────────
# RESULT CONTAINER
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class TestResult:
    test_id:     str
    hypothesis:  str
    stat_name:   str
    stat_value:  float
    p_value:     float
    effect_size: float | None = None
    effect_label:str = ""
    significant: bool = False
    direction:   str = ""
    notes:       str = ""
    details:     dict = field(default_factory=dict)

    def report(self) -> str:
        sig = "✓ SIGNIFICANT" if self.significant else "✗ n.s."
        es  = f", {self.effect_label}={self.effect_size:.3f}" if self.effect_size is not None else ""
        return (
            f"[{self.test_id}] {self.hypothesis}\n"
            f"  {self.stat_name}={self.stat_value:.4f}, p={self.p_value:.4f}{es} — {sig}\n"
            f"  Direction: {self.direction}\n"
            f"  {self.notes}"
        )


# ──────────────────────────────────────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────────────────────────────────────

def _eta_squared(f_stat: float, df_between: int, df_within: int) -> float:
    """η² from F statistic and degrees of freedom."""
    if not math.isfinite(f_stat) or df_within <= 0:
        return float("nan")
    ss_between = f_stat * df_between
    denom = ss_between + df_within
    return ss_between / denom if denom > 0 else float("nan")


def _cohens_h(p1: float, p2: float) -> float:
    """Cohen's h for two proportions."""
    return 2 * math.asin(math.sqrt(max(0.0, min(1.0, p1)))) \
         - 2 * math.asin(math.sqrt(max(0.0, min(1.0, p2))))


def _print_section(title: str) -> None:
    print(f"\n{'='*64}")
    print(f"  {title}")
    print(f"{'='*64}")


def _print_result(r: TestResult) -> None:
    print(r.report())


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def _write_csv(rows: list[dict], path: str) -> None:
    if not rows:
        return
    _ensure_dir(os.path.dirname(path))
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  → wrote {len(rows)} rows to {path}")


def _write_json(data: Any, path: str) -> None:
    _ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"  → wrote {path}")


# ──────────────────────────────────────────────────────────────────────────────
# DATA LOADERS
# ──────────────────────────────────────────────────────────────────────────────

def load_sap_csv(path: str) -> pd.DataFrame:
    """
    Load SAP-format synthetic CSV (sap_synthetic_output.csv schema).
    Columns: archetype, family, iteration, injection, euclidean_drift,
             delta_interpersonal, delta_affective, delta_lifestyle,
             delta_antisocial, constraint_index, dominant_facet, alarm, notes
    """
    df = pd.read_csv(path)
    required = {"archetype", "family", "euclidean_drift", "constraint_index",
                "dominant_facet", "alarm"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"SAP CSV missing columns: {missing}")

    # Derive perturbation_response from injection pressure scaling
    # (synthetic data uses euclidean_drift magnitude as proxy for response class)
    def _infer_response(row):
        d = row["euclidean_drift"]
        if d < 0.15:   return "recovery"
        if d < 0.35:   return "resistance"
        if d < 0.60:   return "baseline"
        return "collapse"

    df["perturbation_response"] = df.apply(_infer_response, axis=1)
    df["perturbation_response_ord"] = df["perturbation_response"].map(
        {"collapse": 0, "baseline": 1, "recovery": 2, "resistance": 3}
    )
    # Derive constraint_breach from constraint_index (high = more constrained = breach)
    df["constraint_breach"] = (df["constraint_index"] > 0.50).astype(int)
    return df


def load_bsi_csv(path: str) -> pd.DataFrame:
    """
    Load BSI session CSV (BSIResult.to_dict() rows).
    Primary columns used: bsi, tc, sd_inv, acg, archetype, exploit_class,
    perturbation_type, bsi_breach, l4_breach, bimodal_detected,
    breach_rate, mean_resilience, acg_profile.
    """
    df = pd.read_csv(path)
    required = {"bsi", "tc", "sd_inv", "acg", "archetype", "exploit_class"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"BSI CSV missing columns: {missing}")
    return df


# ──────────────────────────────────────────────────────────────────────────────
# SAP ANALYSES (operate on sap_synthetic_output.csv schema)
# ──────────────────────────────────────────────────────────────────────────────

def run_H1(df: pd.DataFrame) -> tuple[TestResult, TestResult]:
    """
    H1 — Binomial tests.
    Magneto: p(resistance) > 0.70
    Joker:   p(collapse)   > 0.60

    SAP proxy on synthetic data:
      Magneto → low-drift archetype → resistance = euclidean_drift < 0.15
      Joker   → high-drift archetype → collapse = euclidean_drift > 0.50
    Uses 'Rebel' (closest to chaotic) and 'Ruler' (closest to rigid) from
    synthetic set as stand-ins; flagged as proxy in notes.
    """
    # In synthetic CSV we have Rebel(Soul), Ruler(Self), Caregiver(Ego),
    # Explorer(Soul), Innocent(Ego). No Magneto/Joker — use Ruler/Rebel as proxy.
    ruler   = df[df["archetype"] == "Ruler"]["perturbation_response"].tolist()
    rebel   = df[df["archetype"] == "Rebel"]["perturbation_response"].tolist()

    # Ruler proxy for rigid (Magneto analog)
    n_ruler      = len(ruler)
    k_resistance = sum(1 for r in ruler if r == "resistance")
    p_resistance = k_resistance / n_ruler if n_ruler else 0.0
    binom_ruler  = binomtest(k_resistance, n_ruler, p=0.70, alternative="greater")

    r_magneto = TestResult(
        test_id="H1a",
        hypothesis="Rigid archetype (Ruler proxy): p(resistance) > 0.70",
        stat_name="p_hat",
        stat_value=p_resistance,
        p_value=binom_ruler.pvalue,
        effect_size=_cohens_h(p_resistance, 0.70),
        effect_label="h",
        significant=binom_ruler.pvalue < ALPHA,
        direction=f"observed={p_resistance:.3f} vs threshold=0.70",
        notes="⚠ Proxy: Ruler used for Magneto (live data required for direct H1 test).",
    )

    # Rebel proxy for chaotic (Joker analog)
    n_rebel   = len(rebel)
    k_collapse = sum(1 for r in rebel if r == "collapse")
    p_collapse = k_collapse / n_rebel if n_rebel else 0.0
    binom_rebel = binomtest(k_collapse, n_rebel, p=0.60, alternative="greater")

    r_joker = TestResult(
        test_id="H1b",
        hypothesis="Chaotic archetype (Rebel proxy): p(collapse) > 0.60",
        stat_name="p_hat",
        stat_value=p_collapse,
        p_value=binom_rebel.pvalue,
        effect_size=_cohens_h(p_collapse, 0.60),
        effect_label="h",
        significant=binom_rebel.pvalue < ALPHA,
        direction=f"observed={p_collapse:.3f} vs threshold=0.60",
        notes="⚠ Proxy: Rebel used for Joker (live data required for direct H1 test).",
    )
    return r_magneto, r_joker


def run_H2(df: pd.DataFrame) -> TestResult:
    """
    H2 — One-way ANOVA: drift_magnitude ~ archetype_condition
    + Tukey HSD post-hoc
    + Shapiro-Wilk normality check per group
    + Levene homogeneity of variance
    """
    groups      = df.groupby("archetype")["euclidean_drift"].apply(list).to_dict()
    group_names = list(groups.keys())
    group_arrays = [np.array(v) for v in groups.values()]

    # Normality (Shapiro-Wilk per group — warn if violated)
    normality_flags = {}
    for name, arr in zip(group_names, group_arrays):
        if len(arr) >= 3:
            _, p_sw = shapiro(arr)
            normality_flags[name] = p_sw
        else:
            normality_flags[name] = None

    # Levene homogeneity
    lev_stat, lev_p = levene(*group_arrays)

    # ANOVA
    f_stat, p_val = f_oneway(*group_arrays)
    df_between = len(group_names) - 1
    df_within  = sum(len(g) for g in group_arrays) - len(group_names)
    eta2       = _eta_squared(f_stat, df_between, df_within)

    # Tukey HSD
    tukey_result = tukey_hsd(*group_arrays)
    pairwise = []
    for i in range(len(group_names)):
        for j in range(i + 1, len(group_names)):
            pairwise.append({
                "group_a":   group_names[i],
                "group_b":   group_names[j],
                "mean_diff": float(np.mean(group_arrays[i]) - np.mean(group_arrays[j])),
                "p_value":   float(tukey_result.pvalue[i][j]),
                "significant": bool(tukey_result.pvalue[i][j] < ALPHA_TUKEY),
            })

    notes_parts = [
        f"Levene: F={lev_stat:.3f}, p={lev_p:.3f} "
        f"({'variance homogeneous' if lev_p > 0.05 else 'VARIANCE HETEROGENEOUS — consider Welch'})",
    ]
    sw_violations = [k for k, v in normality_flags.items() if v is not None and v < 0.05]
    if sw_violations:
        notes_parts.append(f"Shapiro-Wilk normality violated: {sw_violations} → consider Kruskal-Wallis")

    return TestResult(
        test_id="H2",
        hypothesis="Archetype condition predicts drift_magnitude (ANOVA)",
        stat_name="F",
        stat_value=f_stat,
        p_value=p_val,
        effect_size=eta2,
        effect_label="η²",
        significant=p_val < ALPHA,
        direction="Higher drift: Soul/chaotic > Ego/Self/rigid (predicted)",
        notes=" | ".join(notes_parts),
        details={
            "group_means": {n: float(np.mean(a)) for n, a in zip(group_names, group_arrays)},
            "group_ns":    {n: len(a) for n, a in zip(group_names, group_arrays)},
            "df_between":  df_between,
            "df_within":   df_within,
            "tukey_pairwise": pairwise,
            "levene_stat": lev_stat,
            "levene_p":    lev_p,
            "normality_sw_p": normality_flags,
        },
    )


def run_H3(df: pd.DataFrame) -> TestResult:
    """
    H3 — Kruskal-Wallis (non-parametric proxy for mixed-effects ordinal model).
    DV: perturbation_response_ord (0–3)
    IV: archetype × perturbation proxy (injection level as moderator proxy)

    SAP specifies mixed-effects ordinal regression; implementing Kruskal-Wallis
    as the scipy-available analog. Flags statsmodels dependency for full model.
    """
    groups      = df.groupby("archetype")["perturbation_response_ord"].apply(list).to_dict()
    group_names = list(groups.keys())
    group_arrays = [np.array(v) for v in groups.values()]

    if len(group_arrays) < 2:
        return TestResult("H3", "Not enough groups", "H", 0.0, 1.0,
                          notes="Insufficient data.")

    h_stat, p_val = kruskal(*group_arrays)

    # Effect size: epsilon² = (H - k + 1) / (n - k) where k=groups, n=total
    n_total = sum(len(g) for g in group_arrays)
    k = len(group_arrays)
    eps2 = (h_stat - k + 1) / (n_total - k) if n_total > k else 0.0

    return TestResult(
        test_id="H3",
        hypothesis="Perturbation type moderates response ~ archetype (K-W proxy)",
        stat_name="H",
        stat_value=h_stat,
        p_value=p_val,
        effect_size=max(0.0, eps2),
        effect_label="ε²",
        significant=p_val < ALPHA,
        direction="Soul family expected highest ordinal response variance",
        notes=(
            "⚠ K-W is a non-parametric proxy. SAP §2 specifies mixed-effects ordinal "
            "regression (lme4/statsmodels). Install statsmodels for full H3 model. "
            "K-W tests between-archetype response distribution without interaction term."
        ),
        details={
            "group_medians": {n: float(np.median(a)) for n, a in zip(group_names, group_arrays)},
            "n_total": n_total,
        },
    )


def run_H4(df: pd.DataFrame) -> TestResult:
    """
    H4 — Batman recovery_rate > pooled-other recovery_rate (exploratory).
    Proxy: uses Caregiver (Ego family, constraint-seeking) as Batman analog.
    """
    caregiver   = df[df["archetype"] == "Caregiver"]["perturbation_response"].tolist()
    other       = df[df["archetype"] != "Caregiver"]["perturbation_response"].tolist()

    n_c  = len(caregiver)
    n_o  = len(other)
    p_c  = sum(1 for r in caregiver if r == "recovery") / n_c if n_c else 0.0
    p_o  = sum(1 for r in other if r == "recovery") / n_o if n_o else 0.0

    # One-sample binomial against pooled-other rate
    k_c = round(p_c * n_c)
    binom_r = binomtest(k_c, n_c, p=p_o, alternative="greater")

    return TestResult(
        test_id="H4",
        hypothesis="Caregiver (Batman proxy): p(recovery) > pooled-other p(recovery)",
        stat_name="p_hat",
        stat_value=p_c,
        p_value=binom_r.pvalue,
        effect_size=_cohens_h(p_c, p_o),
        effect_label="h",
        significant=binom_r.pvalue < ALPHA,
        direction=f"Caregiver={p_c:.3f} vs pooled-other={p_o:.3f}",
        notes="⚠ Proxy: Caregiver used for Batman. Exploratory — no α correction.",
    )


# ──────────────────────────────────────────────────────────────────────────────
# BSI ANALYSES (operate on BSIResult CSV schema)
# ──────────────────────────────────────────────────────────────────────────────

def run_H_archetype(df: pd.DataFrame) -> TestResult:
    """
    H_archetype — ANOVA: BSI ~ archetype_condition (6 levels)
    Pre-registered criterion: η² ≥ 0.15
    """
    ec1 = df[df["exploit_class"] == "EC-1"] if "exploit_class" in df.columns else df
    groups = ec1.groupby("archetype")["bsi"].apply(list).to_dict()
    if len(groups) < 2:
        return TestResult("H_archetype", "Insufficient groups", "F", 0.0, 1.0)

    names  = list(groups.keys())
    arrays = [np.array(v) for v in groups.values()]

    f_stat, p_val  = f_oneway(*arrays)
    df_b = len(names) - 1
    df_w = sum(len(a) for a in arrays) - len(names)
    eta2 = _eta_squared(f_stat, df_b, df_w)
    lev_stat, lev_p = levene(*arrays) if len(arrays) >= 2 else (0.0, 1.0)

    tukey_result = tukey_hsd(*arrays)
    pairwise = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            pairwise.append({
                "group_a":     names[i],
                "group_b":     names[j],
                "mean_diff":   float(np.mean(arrays[i]) - np.mean(arrays[j])),
                "p_value":     float(tukey_result.pvalue[i][j]),
                "significant": bool(tukey_result.pvalue[i][j] < ALPHA_TUKEY),
            })

    criterion_met = eta2 >= EFFECT_ETA2_CRIT
    return TestResult(
        test_id="H_archetype",
        hypothesis="BSI varies by archetype_condition (EC-1), η² ≥ 0.15 criterion",
        stat_name="F",
        stat_value=f_stat,
        p_value=p_val,
        effect_size=eta2,
        effect_label="η²",
        significant=p_val < ALPHA,
        direction=(
            f"η²={eta2:.3f} — criterion (≥0.15) "
            f"{'MET ✓' if criterion_met else 'NOT MET ✗'}"
        ),
        notes=f"Levene: F={lev_stat:.3f}, p={lev_p:.3f}",
        details={
            "group_means": {n: float(np.mean(a)) for n, a in zip(names, arrays)},
            "tukey_pairwise": pairwise,
        },
    )


def run_H_compound(df: pd.DataFrame) -> tuple[TestResult, TestResult]:
    """
    H_compound — BSI drops monotonically across exploit class conditions.
    Super-additivity test: BSI_COMP < BSI_EC4 + BSI_EC1 - BSI_CTL
    """
    conditions = ["CTL", "EC-1", "EC-2+EC-1", "EC-4", "COMP"]
    bsi_by_ec  = {}
    for ec in conditions:
        subset = df[df["exploit_class"] == ec]["bsi"].dropna()
        if len(subset) > 0:
            bsi_by_ec[ec] = subset.values

    # Repeated-measures ANOVA approximation: one-way ANOVA on available conditions
    available = {k: v for k, v in bsi_by_ec.items() if len(v) >= 2}
    if len(available) < 2:
        empty = TestResult("H_compound", "Insufficient exploit class data", "F", 0.0, 1.0)
        return empty, empty

    names  = list(available.keys())
    arrays = list(available.values())
    f_stat, p_val = f_oneway(*arrays)
    df_b  = len(names) - 1
    df_w  = sum(len(a) for a in arrays) - len(names)
    eta2  = _eta_squared(f_stat, df_b, df_w)

    r_anova = TestResult(
        test_id="H_compound_anova",
        hypothesis="BSI differs across exploit class conditions (RM-ANOVA proxy)",
        stat_name="F",
        stat_value=f_stat,
        p_value=p_val,
        effect_size=eta2,
        effect_label="η²",
        significant=p_val < ALPHA,
        direction="Expected: CTL > EC-1 > EC-2+EC-1 > EC-4 > COMP",
        notes="⚠ One-way proxy; repeated-measures requires statsmodels MixedLM.",
        details={"group_means": {n: float(np.mean(a)) for n, a in zip(names, arrays)}},
    )

    # Super-additivity t-test
    # H: BSI_COMP < BSI_EC4 + BSI_EC1 − BSI_CTL
    r_super = TestResult(
        "H_compound_superadd",
        "EC-4×EC-1 super-additive instability",
        "t", 0.0, 1.0,
        notes="[PENDING] Requires matched BSI_COMP, BSI_EC4, BSI_EC1, BSI_CTL per session.",
    )
    if all(k in bsi_by_ec for k in ["CTL", "EC-1", "EC-4", "COMP"]):
        ctl_mean = float(np.mean(bsi_by_ec["CTL"]))
        ec1_mean = float(np.mean(bsi_by_ec["EC-1"]))
        ec4_mean = float(np.mean(bsi_by_ec["EC-4"]))
        comp_arr = bsi_by_ec["COMP"]
        additive_pred = ec4_mean + ec1_mean - ctl_mean
        # One-sample t-test: is COMP BSI below additive prediction?
        t_stat, p_t = _one_sample_t(comp_arr, mu=additive_pred, alternative="less")
        delta = float(np.mean(comp_arr)) - additive_pred
        r_super = TestResult(
            test_id="H_compound_superadd",
            hypothesis="BSI_COMP < BSI_EC4 + BSI_EC1 − BSI_CTL (super-additivity)",
            stat_name="t",
            stat_value=t_stat,
            p_value=p_t,
            significant=p_t < ALPHA,
            direction=f"COMP_mean={np.mean(comp_arr):.3f} vs additive={additive_pred:.3f} (Δ={delta:+.3f})",
            notes="Δ < 0 supports super-additivity (compound worse than additive sum).",
        )
    return r_anova, r_super


def _one_sample_t(sample: np.ndarray, mu: float,
                  alternative: str = "two-sided") -> tuple[float, float]:
    """One-sample t-test against a known μ; pure scipy/numpy."""
    n    = len(sample)
    xbar = float(np.mean(sample))
    se   = float(np.std(sample, ddof=1)) / math.sqrt(n) if n > 1 else 1.0
    t    = (xbar - mu) / se if se > 0 else 0.0
    # p-value from t-distribution via normal approximation for large n,
    # exact Student-t via scipy for small n
    from scipy.stats import t as t_dist
    if alternative == "less":
        p = float(t_dist.cdf(t, df=n - 1))
    elif alternative == "greater":
        p = float(1 - t_dist.cdf(t, df=n - 1))
    else:
        p = float(2 * min(t_dist.cdf(t, df=n - 1), 1 - t_dist.cdf(t, df=n - 1)))
    return t, p


def run_H_ACG_L4(df: pd.DataFrame) -> TestResult:
    """
    H_ACG_L4 — Chi-square: l4_breach rate differs by exploit_class.
    (Logistic regression analog; requires statsmodels for full ORs.)
    """
    if "l4_breach" not in df.columns or "exploit_class" not in df.columns:
        return TestResult("H_ACG_L4", "Missing l4_breach or exploit_class", "χ²", 0.0, 1.0)

    ct = pd.crosstab(df["exploit_class"], df["l4_breach"].astype(int))
    if ct.shape[1] < 2 or ct.shape[0] < 2:
        return TestResult("H_ACG_L4", "Insufficient l4_breach variation", "χ²", 0.0, 1.0,
                          notes="All sessions show same l4_breach value — no variation to test.")

    chi2, p_val, dof, expected = chi2_contingency(ct)
    # Cramér's V
    n    = ct.values.sum()
    cramers_v = math.sqrt(chi2 / (n * (min(ct.shape) - 1))) if n > 0 else 0.0

    l4_rates = df.groupby("exploit_class")["l4_breach"].apply(
        lambda x: x.astype(int).mean()
    ).to_dict()

    return TestResult(
        test_id="H_ACG_L4",
        hypothesis="L4 breach rate differs by exploit_class (χ²)",
        stat_name="χ²",
        stat_value=chi2,
        p_value=p_val,
        effect_size=cramers_v,
        effect_label="V",
        significant=p_val < ALPHA,
        direction="Expected: EC-4 and COMP show highest L4 breach rates",
        notes=(
            f"L4 breach rates by condition: {l4_rates}. "
            "⚠ Full logistic regression (ORs) requires statsmodels."
        ),
        details={"l4_rates": l4_rates, "dof": dof},
    )


def run_H_variance(df: pd.DataFrame) -> TestResult:
    """
    H_variance — Levene: BSI variance differs by exploit_class.
    Pre-registered: EC-4 shows highest within-condition BSI variance.
    """
    if "exploit_class" not in df.columns:
        return TestResult("H_variance", "Missing exploit_class", "W", 0.0, 1.0)

    groups = df.groupby("exploit_class")["bsi"].apply(list).to_dict()
    if len(groups) < 2:
        return TestResult("H_variance", "Insufficient groups", "W", 0.0, 1.0)

    names  = list(groups.keys())
    arrays = [np.array(v) for v in groups.values()]
    lev_stat, lev_p = levene(*arrays)
    stdevs  = {n: float(np.std(a, ddof=1)) for n, a in zip(names, arrays)}
    ec4_sd  = stdevs.get("EC-4", None)
    max_sd_cond = max(stdevs, key=stdevs.get) if stdevs else "unknown"

    return TestResult(
        test_id="H_variance",
        hypothesis="BSI variance differs by exploit_class; EC-4 highest (Levene)",
        stat_name="W",
        stat_value=lev_stat,
        p_value=lev_p,
        significant=lev_p < ALPHA,
        direction=f"Highest variance condition: {max_sd_cond} (sd={stdevs.get(max_sd_cond, 0):.4f})",
        notes=(
            f"EC-4 sd={ec4_sd:.4f} (expected highest). " if ec4_sd is not None
            else "EC-4 not in dataset (dry-run: only EC-1 present). "
            f"All condition SDs: {stdevs}"
        ),
        details={"stdevs": stdevs},
    )


# ──────────────────────────────────────────────────────────────────────────────
# SENSITIVITY ANALYSES
# ──────────────────────────────────────────────────────────────────────────────

def run_tau_sensitivity(df: pd.DataFrame) -> list[dict]:
    """
    SA 4.1 — Re-run breach classification at τ ± 0.10.
    Uses euclidean_drift as the drift magnitude proxy against modified τ.
    Reports breach_rate per archetype per τ variant.
    """
    rows = []
    base_tau = {k: v for k, v in CEE_TOLERANCE.items()}

    for offset in TAU_OFFSETS:
        for archetype, grp in df.groupby("archetype"):
            base = base_tau.get(archetype, base_tau.get("_default", 0.30))
            tau  = max(0.01, base + offset)
            drifts = grp["euclidean_drift"].values
            breach_rate = float(np.mean(drifts > tau))
            rows.append({
                "archetype":    archetype,
                "tau_offset":   offset,
                "tau_value":    round(tau, 3),
                "breach_rate":  round(breach_rate, 4),
                "n":            len(drifts),
                "mean_drift":   round(float(np.mean(drifts)), 4),
            })
    return rows


def run_response_threshold_sensitivity(df: pd.DataFrame) -> list[dict]:
    """
    SA 4.2 — Re-classify perturbation_response at threshold variants.
    Checks whether dominant_response per archetype changes across variants.
    """
    rows = []
    for variant in RESP_THRESH_VARIANTS:
        rec_thresh = variant["recovery"]
        col_thresh = variant["collapse"]

        def reclassify(row, rt=rec_thresh, ct=col_thresh):
            d = row["euclidean_drift"]
            if d < rt * 0.30:    return "recovery"
            if d < rt * 0.50:    return "resistance"
            if d < ct * 0.70:    return "baseline"
            return "collapse"

        df_v = df.copy()
        df_v["resp_variant"] = df_v.apply(reclassify, axis=1)

        for archetype, grp in df_v.groupby("archetype"):
            counts  = grp["resp_variant"].value_counts().to_dict()
            dominant = max(counts, key=counts.get) if counts else "unknown"
            rows.append({
                "variant":    variant["label"],
                "archetype":  archetype,
                "dominant":   dominant,
                "recovery":   counts.get("recovery", 0),
                "resistance": counts.get("resistance", 0),
                "baseline":   counts.get("baseline", 0),
                "collapse":   counts.get("collapse", 0),
            })
    return rows


def run_pcl_r_weight_sensitivity(df: pd.DataFrame) -> list[dict]:
    """
    SA 4.3 — Compare pcl_r_proxy rank order under approximated vs bibliography weights.
    Uses constraint_index as a proxy for pcl_r_proxy on SAP-schema data.
    """
    # On SAP schema, compute a proxy score using each weight set
    def _proxy_score(row, weights: dict) -> float:
        # Map available SAP columns to trait keys where possible
        # SAP has: delta_interpersonal, delta_affective, delta_lifestyle, delta_antisocial
        col_map = {
            "grandiosity":          "delta_interpersonal",
            "calculating_behavior": "delta_interpersonal",
            "empathy_deficit":      "delta_affective",
            "moral_disengagement":  "delta_affective",
            "impulsivity":          "delta_lifestyle",
            "impulse_control":      "delta_lifestyle",
            "emotional_lability":   "delta_antisocial",
            "risk_tolerance":       "delta_antisocial",
        }
        score = 0.0
        for trait, col in col_map.items():
            w = weights.get(trait, 0.0)
            v = row.get(col, 0.0)
            score += abs(w) * abs(v) * (1 if w >= 0 else -1)
        return score

    rows = []
    for archetype, grp in df.groupby("archetype"):
        approx_scores = grp.apply(_proxy_score, weights=PCL_R_APPROX, axis=1)
        biblio_scores = grp.apply(_proxy_score, weights=PCL_R_BIBLIO, axis=1)
        rows.append({
            "archetype":        archetype,
            "approx_mean":      round(float(approx_scores.mean()), 4),
            "biblio_mean":      round(float(biblio_scores.mean()), 4),
            "rank_preserved":   None,  # computed post-loop
        })

    # Check rank order preservation
    approx_rank = sorted(rows, key=lambda x: x["approx_mean"], reverse=True)
    biblio_rank = sorted(rows, key=lambda x: x["biblio_mean"], reverse=True)
    approx_order = [r["archetype"] for r in approx_rank]
    biblio_order = [r["archetype"] for r in biblio_rank]
    rank_preserved = approx_order == biblio_order

    for row in rows:
        row["rank_preserved"] = rank_preserved
        row["approx_order"]   = str(approx_order)
        row["biblio_order"]   = str(biblio_order)
    return rows


# ──────────────────────────────────────────────────────────────────────────────
# SUMMARY REPORT
# ──────────────────────────────────────────────────────────────────────────────

def build_hypothesis_register(results: list[TestResult]) -> list[dict]:
    rows = []
    for r in results:
        rows.append({
            "test_id":     r.test_id,
            "hypothesis":  r.hypothesis,
            "stat":        f"{r.stat_name}={r.stat_value:.4f}",
            "p_value":     round(r.p_value, 4),
            "effect_size": round(r.effect_size, 4) if r.effect_size is not None else None,
            "effect_label":r.effect_label,
            "significant": r.significant,
            "direction":   r.direction,
            "notes":       r.notes,
        })
    return rows


# ──────────────────────────────────────────────────────────────────────────────
# MAIN PIPELINE
# ──────────────────────────────────────────────────────────────────────────────

def run_pipeline(
    sap_csv_path:   str | None = None,
    bsi_csv_path:   str | None = None,
    output_dir:     str        = "analysis",
) -> dict[str, Any]:
    """
    Full analysis pipeline. Pass one or both CSV paths.

    sap_csv_path : path to sap_synthetic_output.csv (SAP-schema data)
    bsi_csv_path : path to bsi_sessions.csv (BSIResult.to_dict() rows)
    output_dir   : root for analysis/ subdirectory outputs
    """
    all_results: list[TestResult] = []

    # ── MODE A: SAP synthetic CSV ─────────────────────────────────────────────
    if sap_csv_path and os.path.exists(sap_csv_path):
        _print_section("MODE A — SAP SYNTHETIC CSV ANALYSES")
        print(f"  Source: {sap_csv_path}")
        df_sap = load_sap_csv(sap_csv_path)
        print(f"  Rows: {len(df_sap)}  Archetypes: {df_sap['archetype'].unique().tolist()}")

        print("\n--- H1: Directional binomial tests ---")
        h1a, h1b = run_H1(df_sap)
        _print_result(h1a)
        _print_result(h1b)
        all_results += [h1a, h1b]

        print("\n--- H2: ANOVA drift_magnitude ~ archetype ---")
        h2 = run_H2(df_sap)
        _print_result(h2)
        all_results.append(h2)
        _write_csv(h2.details.get("tukey_pairwise", []),
                   os.path.join(output_dir, "anova", "H2_tukey_pairwise.csv"))
        _write_json(h2.details,
                    os.path.join(output_dir, "anova", "H2_anova_details.json"))

        print("\n--- H3: K-W perturbation response ~ archetype ---")
        h3 = run_H3(df_sap)
        _print_result(h3)
        all_results.append(h3)

        print("\n--- H4: Batman/Caregiver recovery rate ---")
        h4 = run_H4(df_sap)
        _print_result(h4)
        all_results.append(h4)

        print("\n--- SA 4.1: τ sensitivity ---")
        tau_rows = run_tau_sensitivity(df_sap)
        _write_csv(tau_rows,
                   os.path.join(output_dir, "sensitivity", "SA4_1_tau_sensitivity.csv"))
        print(f"  τ sensitivity: {len(tau_rows)} rows written")
        # Print summary
        for row in tau_rows:
            print(f"    {row['archetype']:<12} τ{row['tau_offset']:+.2f}={row['tau_value']:.2f}  "
                  f"breach_rate={row['breach_rate']:.3f}")

        print("\n--- SA 4.2: Perturbation threshold sensitivity ---")
        resp_rows = run_response_threshold_sensitivity(df_sap)
        _write_csv(resp_rows,
                   os.path.join(output_dir, "sensitivity", "SA4_2_response_threshold.csv"))
        print(f"  Threshold sensitivity: {len(resp_rows)} rows written")

        print("\n--- SA 4.3: PCL-R weight sensitivity ---")
        pclr_rows = run_pcl_r_weight_sensitivity(df_sap)
        _write_csv(pclr_rows,
                   os.path.join(output_dir, "sensitivity", "SA4_3_pclr_weight.csv"))
        print(f"  PCL-R weight sensitivity: {len(pclr_rows)} rows written")
        if pclr_rows:
            print(f"  Rank preserved: {pclr_rows[0].get('rank_preserved')}")
            print(f"  Approx order:   {pclr_rows[0].get('approx_order')}")
            print(f"  Biblio order:   {pclr_rows[0].get('biblio_order')}")

    else:
        print(f"  SAP CSV not found: {sap_csv_path} — skipping Mode A")

    # ── MODE B: BSI session CSV ───────────────────────────────────────────────
    if bsi_csv_path and os.path.exists(bsi_csv_path):
        _print_section("MODE B — BSI SESSION ANALYSES")
        print(f"  Source: {bsi_csv_path}")
        df_bsi = load_bsi_csv(bsi_csv_path)
        print(f"  Rows: {len(df_bsi)}  "
              f"Archetypes: {df_bsi['archetype'].unique().tolist()}")

        print("\n--- H_archetype: ANOVA BSI ~ archetype (EC-1) ---")
        h_arch = run_H_archetype(df_bsi)
        _print_result(h_arch)
        all_results.append(h_arch)
        _write_csv(h_arch.details.get("tukey_pairwise", []),
                   os.path.join(output_dir, "anova", "H_archetype_tukey.csv"))

        print("\n--- H_compound: BSI ~ exploit_class + super-additivity ---")
        h_comp_anova, h_comp_super = run_H_compound(df_bsi)
        _print_result(h_comp_anova)
        _print_result(h_comp_super)
        all_results += [h_comp_anova, h_comp_super]

        print("\n--- H_ACG_L4: χ² l4_breach ~ exploit_class ---")
        h_acg = run_H_ACG_L4(df_bsi)
        _print_result(h_acg)
        all_results.append(h_acg)

        print("\n--- H_variance: Levene BSI variance ~ exploit_class ---")
        h_var = run_H_variance(df_bsi)
        _print_result(h_var)
        all_results.append(h_var)

    else:
        print(f"\n  BSI session CSV not found: {bsi_csv_path} — skipping Mode B")
        print("  (Run behavioral_stability_index.py trials and export to CSV first)")

    # ── HYPOTHESIS REGISTER ───────────────────────────────────────────────────
    if all_results:
        _print_section("HYPOTHESIS OUTCOME REGISTER")
        register = build_hypothesis_register(all_results)
        _write_csv(register,
                   os.path.join(output_dir, "hypothesis_register.csv"))
        for row in register:
            sig = "✓" if row["significant"] else "✗"
            print(f"  {sig} [{row['test_id']:<24}] p={row['p_value']:.4f}  {row['direction'][:60]}")

    return {"results": all_results, "register": register if all_results else []}


# ──────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="BSI statistical analysis pipeline")
    parser.add_argument("--sap",  default=None, help="Path to sap_synthetic_output.csv")
    parser.add_argument("--bsi",  default=None, help="Path to bsi_sessions.csv")
    parser.add_argument("--out",  default="analysis", help="Output directory root")
    args = parser.parse_args()

    # Auto-discover SAP CSV if not specified
    sap_path = args.sap
    if not sap_path:
        candidates = [
            "data/synthetic/sap_synthetic_output.csv",
            "../data/synthetic/sap_synthetic_output.csv",
            "sap_synthetic_output.csv",
        ]
        for c in candidates:
            if os.path.exists(c):
                sap_path = c
                break

    run_pipeline(
        sap_csv_path=sap_path,
        bsi_csv_path=args.bsi,
        output_dir=args.out,
    )
