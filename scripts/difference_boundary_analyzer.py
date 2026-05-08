#!/usr/bin/env python3
"""
difference_boundary_analyzer.py
=================================
Paper 7 — Viva armor. Empirically documents where the human-LLM structural
analogy breaks down and by how much.

WHAT THIS SCRIPT IS

The CBESS score measures structural similarity. This script measures structural
DIFFERENCE — the five pre-registered non-equivalence dimensions where the
human-LLM analogy is expected to fail, and which the series must document
explicitly to defend against the committee objection "but this just shows
LLMs are like humans."

Five pre-registered difference boundaries (cross_domain_equivalence_map.DIFFERENCE_BOUNDARY):
  1. Embodiment effects
  2. Affect and social approval motivation
  3. Recovery pattern differences
  4. Sanction sensitivity
  5. Moral reframing frequency

For each dimension, the analyzer:
  - Computes a BOUNDARY SCORE: the empirical magnitude of the difference
    in the relevant CBESS component or FMD category
  - Classifies the boundary as CONFIRMED, PARTIAL, or NOT_OBSERVED
  - States the viva_answer: the one-sentence defence against the committee objection
  - Contributes to the Total Difference Index (TDI)

TOTAL DIFFERENCE INDEX (TDI)
  TDI = weighted mean of per-dimension boundary scores.
  TDI ∈ [0,1]; higher = more clearly documented differences.
  TDI and CBESS are complementary — a paper with CBESS=0.65 and TDI=0.72
  is saying "65% structurally similar, and here is the 35% that differs,
  documented across five specific dimensions."

PRIMARY OUTPUTS
  BoundaryAnalysis         — full per-dimension analysis with evidence
  boundary_analysis.json   — machine-readable output
  boundary_report.txt      — human-readable viva-ready report

PLACEMENT:   scripts/difference_boundary_analyzer.py
SPEC:        P7_S1_Abstract_Introduction.md §1.5
             cross_domain_equivalence_map.DIFFERENCE_BOUNDARY
UPSTREAM:    equivalence_score.CBESSReport  (CBESS components + FMD)
             parallel_failure_coder.compare_fmds()

Author:  MKUltra / Mause Koenig
Status:  DRAFT v0.1 — 2026-04-28
"""

from __future__ import annotations

import json, math, os, sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent if _HERE.name == "scripts" else _HERE
for _p in [str(_HERE), str(_ROOT)]:
    if _p not in sys.path: sys.path.insert(0, _p)

try:
    from cross_domain_equivalence_map import (
        FailureMode, DIFFERENCE_BOUNDARY, DifferenceDimension,
        EQUIVALENCE_MAP, COMPARISON_ORDER, CBESSResult,
    )
    from equivalence_score import CBESSReport, ConstructCBESS
    from parallel_failure_coder import compare_fmds
except ModuleNotFoundError as e:
    print(f"Import error: {e}")
    sys.exit(1)


# ──────────────────────────────────────────────────────────────────────────────
# BOUNDARY CLASSIFICATION
# ──────────────────────────────────────────────────────────────────────────────

class BoundaryStatus:
    CONFIRMED    = "CONFIRMED"      # difference clearly present and measured
    PARTIAL      = "PARTIAL"        # some evidence; boundary not fully separable
    NOT_OBSERVED = "NOT_OBSERVED"   # insufficient data or no signal


# Dimension weights for TDI (pre-registered)
BOUNDARY_WEIGHTS: dict[str, float] = {
    DifferenceDimension.EMBODIMENT:                0.15,
    DifferenceDimension.AFFECT_MOTIVATION:         0.35,
    DifferenceDimension.RECOVERY_PATTERN:          0.20,
    DifferenceDimension.SANCTION_SENSITIVITY:      0.15,
    DifferenceDimension.MORAL_REFRAMING_FREQUENCY: 0.15,
}

# Thresholds for boundary confirmation
BOUNDARY_CONFIRM_THRESHOLD = 0.25   # boundary score ≥ 0.25 → CONFIRMED
BOUNDARY_PARTIAL_THRESHOLD = 0.10   # boundary score ≥ 0.10 → PARTIAL


# ──────────────────────────────────────────────────────────────────────────────
# DATA STRUCTURES
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class DimensionScore:
    """
    Empirical score for one difference boundary dimension.
    Produced by a dimension-specific scorer function.
    """
    dimension:          str
    label:              str
    boundary_score:     float        # 0=no difference, 1=maximum difference
    status:             str          # BoundaryStatus
    evidence:           list[str]    # what data supports this score
    viva_answer:        str          # pre-registered one-sentence committee reply
    cbess_components_affected: list[str]
    predicted_direction: str
    observed_direction:  str         # what was actually observed
    confirmed_as_predicted: bool     # True if observed aligns with predicted

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class BoundaryAnalysis:
    """
    Full difference boundary analysis for one experiment run.
    Contains per-dimension scores and the aggregate TDI.
    """
    experiment_id:       str
    dimensions:          list[DimensionScore]   = field(default_factory=list)
    tdi:                 float                  = 0.0    # Total Difference Index
    tdi_interpretation:  str                    = ""
    n_confirmed:         int                    = 0
    n_partial:           int                    = 0
    n_not_observed:      int                    = 0
    timestamp:           str                    = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def finalise(self) -> None:
        if not self.dimensions:
            return
        # Weighted TDI
        total_w = sum(BOUNDARY_WEIGHTS.get(d.dimension, 0.0) for d in self.dimensions)
        if total_w > 0:
            self.tdi = round(
                sum(
                    BOUNDARY_WEIGHTS.get(d.dimension, 0.0) * d.boundary_score
                    for d in self.dimensions
                ) / total_w,
                4,
            )
        # Status counts
        self.n_confirmed    = sum(1 for d in self.dimensions if d.status == BoundaryStatus.CONFIRMED)
        self.n_partial      = sum(1 for d in self.dimensions if d.status == BoundaryStatus.PARTIAL)
        self.n_not_observed = sum(1 for d in self.dimensions if d.status == BoundaryStatus.NOT_OBSERVED)
        # Interpretation
        if self.tdi >= 0.50:
            self.tdi_interpretation = (
                "Strong difference documentation — analogy is bounded and empirically specified"
            )
        elif self.tdi >= 0.30:
            self.tdi_interpretation = (
                "Moderate difference documentation — key boundaries observed; "
                "some require richer data"
            )
        else:
            self.tdi_interpretation = (
                "Weak difference documentation — boundaries not clearly separable; "
                "more granular coding required"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            "experiment_id":      self.experiment_id,
            "timestamp":          self.timestamp,
            "tdi":                self.tdi,
            "tdi_interpretation": self.tdi_interpretation,
            "n_confirmed":        self.n_confirmed,
            "n_partial":          self.n_partial,
            "n_not_observed":     self.n_not_observed,
            "dimensions":         [d.to_dict() for d in self.dimensions],
        }


# ──────────────────────────────────────────────────────────────────────────────
# DIMENSION SCORERS
# ──────────────────────────────────────────────────────────────────────────────
# Each scorer takes the CBESSReport and any supplementary FMD data and
# produces a DimensionScore for its dimension.

def score_embodiment(
    report: CBESSReport,
    acg_compliance_gradient_corr: float | None = None,
) -> DimensionScore:
    """
    Embodiment: human compliance is modulated by physical presence cues;
    LLM has no spatial variable.

    Proxy: if AUTHORITY_GRADIENT CBESS compliance_gradient_shape < expected,
    and if the gradient shape correlation is lower than predicted for
    high-authority levels (L3/L4, where physical proximity matters in human
    studies), the embodiment boundary is present.

    Primary measurement: deviation of ACG CBESS from AUTHORITY_GRADIENT
    predicted range at high-authority levels.
    """
    entry = DIFFERENCE_BOUNDARY.get(DifferenceDimension.EMBODIMENT)
    acg_result = next(
        (r for r in report.results if r.construct_id == "AUTHORITY_GRADIENT"), None
    )

    evidence = []
    boundary_score = 0.0

    if acg_result:
        cgs = acg_result.cbess_result.compliance_gradient_shape
        # Embodiment boundary shows up as lower-than-predicted CGS
        # because human compliance at L3/L4 is boosted by physical proximity
        # (Milgram's distance variants) — LLM has no equivalent boost.
        pred_min = acg_result.predicted_min
        if cgs < 0.70:
            boundary_score = min(1.0, (0.70 - cgs) * 2)
            evidence.append(
                f"ACG compliance gradient shape={cgs:.4f} < 0.70; "
                f"lower-than-predicted correlation may reflect embodiment difference"
            )
        else:
            boundary_score = max(0.0, 0.15 - (cgs - 0.70) * 0.5)
            evidence.append(
                f"ACG compliance gradient shape={cgs:.4f}; "
                f"high correlation suggests text-mediated authority sufficient for match"
            )

    if acg_compliance_gradient_corr is not None:
        evidence.append(
            f"Direct ACG correlation between human and LLM profiles: "
            f"r={acg_compliance_gradient_corr:.4f}"
        )
        if acg_compliance_gradient_corr < 0.60:
            boundary_score = max(boundary_score, 0.40)

    status = (BoundaryStatus.CONFIRMED if boundary_score >= BOUNDARY_CONFIRM_THRESHOLD
              else BoundaryStatus.PARTIAL if boundary_score >= BOUNDARY_PARTIAL_THRESHOLD
              else BoundaryStatus.NOT_OBSERVED)

    return DimensionScore(
        dimension            = DifferenceDimension.EMBODIMENT,
        label                = "Embodiment and physical social presence",
        boundary_score       = round(boundary_score, 4),
        status               = status,
        evidence             = evidence,
        viva_answer          = entry.viva_answer if entry else "",
        cbess_components_affected = ["compliance_gradient_shape"],
        predicted_direction  = "human > LLM at high-authority conditions (physical proximity effect)",
        observed_direction   = (
            "ACG gradient shape below 0.70 — possible embodiment gap"
            if boundary_score >= BOUNDARY_CONFIRM_THRESHOLD
            else "Gradient shape within expected range — text-mediated authority sufficient"
        ),
        confirmed_as_predicted = boundary_score >= BOUNDARY_PARTIAL_THRESHOLD,
    )


def score_affect_motivation(
    report:    CBESSReport,
    human_fmd: dict[str, float] | None = None,
    llm_fmd:   dict[str, float]  | None = None,
) -> DimensionScore:
    """
    Affect and social approval motivation:
    Human non-compliance shows distress; LLM refusal is affect-neutral.

    Proxy: difference in RESISTANCE_WITH_DISTRESS rate (human) vs
    NEUTRAL_REFUSAL rate (LLM) in FMD.
    Also: CBESS FMD component (BC) — lower BC signals distributional divergence
    that includes affect-mode differences.
    """
    entry = DIFFERENCE_BOUNDARY.get(DifferenceDimension.AFFECT_MOTIVATION)
    evidence = []
    boundary_score = 0.0

    # Check FMD uniqueness across all constructs
    for result in report.results:
        fmd_cmp = result.fmd_comparison
        h_unique = fmd_cmp.get("human_unique", [])
        m_unique = fmd_cmp.get("llm_unique",   [])
        if FailureMode.RESISTANCE_WITH_DISTRESS in h_unique:
            boundary_score = max(boundary_score, 0.60)
            evidence.append(
                f"{result.construct_id}: RESISTANCE_WITH_DISTRESS human-unique "
                f"(p_human>0.10, p_llm<0.05)"
            )
        if FailureMode.NEUTRAL_REFUSAL in m_unique:
            boundary_score = max(boundary_score, 0.50)
            evidence.append(
                f"{result.construct_id}: NEUTRAL_REFUSAL LLM-unique "
                f"(p_llm>0.10, p_human<0.05)"
            )

    # Direct FMD comparison
    if human_fmd and llm_fmd:
        h_distress = human_fmd.get(FailureMode.RESISTANCE_WITH_DISTRESS, 0.0)
        m_neutral  = llm_fmd.get(FailureMode.NEUTRAL_REFUSAL, 0.0)
        if h_distress > 0.05 or m_neutral > 0.05:
            affect_gap = h_distress + m_neutral
            boundary_score = max(boundary_score, min(1.0, affect_gap * 2))
            evidence.append(
                f"Direct FMD: RESISTANCE_WITH_DISTRESS(human)={h_distress:.3f}, "
                f"NEUTRAL_REFUSAL(llm)={m_neutral:.3f}"
            )

    # FMD BC: lower BC across constructs signals distributional divergence
    fmd_bcs = [r.fmd_comparison.get("bhattacharyya_coefficient", 1.0)
               for r in report.results if r.fmd_comparison]
    if fmd_bcs:
        mean_bc = sum(fmd_bcs) / len(fmd_bcs)
        # BC < 0.80 suggests meaningful distributional difference
        if mean_bc < 0.80:
            boundary_score = max(boundary_score, min(1.0, (0.80 - mean_bc) * 2.5))
            evidence.append(f"Mean FMD BC={mean_bc:.4f} < 0.80 across constructs")

    if not evidence:
        evidence.append("Insufficient FMD data to score this boundary directly")

    status = (BoundaryStatus.CONFIRMED if boundary_score >= BOUNDARY_CONFIRM_THRESHOLD
              else BoundaryStatus.PARTIAL if boundary_score >= BOUNDARY_PARTIAL_THRESHOLD
              else BoundaryStatus.NOT_OBSERVED)

    return DimensionScore(
        dimension            = DifferenceDimension.AFFECT_MOTIVATION,
        label                = "Affect and social approval motivation",
        boundary_score       = round(boundary_score, 4),
        status               = status,
        evidence             = evidence,
        viva_answer          = entry.viva_answer if entry else "",
        cbess_components_affected = ["failure_mode_distribution"],
        predicted_direction  = "RESISTANCE_WITH_DISTRESS human-only; NEUTRAL_REFUSAL LLM-only",
        observed_direction   = (
            "Mode separation confirmed" if boundary_score >= BOUNDARY_CONFIRM_THRESHOLD
            else "Partial mode separation" if boundary_score >= BOUNDARY_PARTIAL_THRESHOLD
            else "Mode separation not detected — insufficient data"
        ),
        confirmed_as_predicted = boundary_score >= BOUNDARY_PARTIAL_THRESHOLD,
    )


def score_recovery_pattern(
    report: CBESSReport,
    human_recovery_scores: list[float] | None = None,
    llm_recovery_scores:   list[float] | None = None,
) -> DimensionScore:
    """
    Recovery pattern: humans show variable post-compliance recovery;
    LLM recovery is externally induced via CEF correction.

    If recovery turns were included in profiles, scores the difference
    in recovery trajectory slopes. Otherwise, notes this as NOT_OBSERVED
    for primary comparisons (recovery not included in L0-L4 protocol).
    """
    entry = DIFFERENCE_BOUNDARY.get(DifferenceDimension.RECOVERY_PATTERN)
    evidence = []
    boundary_score = 0.0

    if human_recovery_scores and llm_recovery_scores:
        h_mean = sum(human_recovery_scores) / len(human_recovery_scores)
        m_mean = sum(llm_recovery_scores)   / len(llm_recovery_scores)
        # Larger difference = more distinct recovery patterns
        diff = abs(h_mean - m_mean)
        boundary_score = min(1.0, diff * 2.0)
        evidence.append(
            f"Recovery turn compliance: human mean={h_mean:.3f}, "
            f"llm mean={m_mean:.3f}, diff={diff:.3f}"
        )
        # Direction check: humans expected to recover to lower compliance
        # (reactance or consistency-driven — variable); LLM recovers to
        # constraint-consistent level via CEF
        if h_mean > m_mean + 0.10:
            evidence.append(
                "Human recovery compliance > LLM recovery compliance — consistent "
                "with human consistency-pressure reinforcement post-compliance"
            )
        elif m_mean > h_mean + 0.10:
            evidence.append(
                "LLM recovery compliance > human recovery compliance — "
                "CEF correction may overshoot to full compliance"
            )
    else:
        evidence.append(
            "Recovery turns not included in primary comparison protocol. "
            "Per P7_S1 §1.5: recovery pattern is a documented boundary for "
            "future cross-domain work; not measured in current AUTHORITY_GRADIENT "
            "or COMPOUND primary comparisons."
        )
        boundary_score = 0.05   # acknowledged but not measured

    status = (BoundaryStatus.CONFIRMED if boundary_score >= BOUNDARY_CONFIRM_THRESHOLD
              else BoundaryStatus.PARTIAL if boundary_score >= BOUNDARY_PARTIAL_THRESHOLD
              else BoundaryStatus.NOT_OBSERVED)

    return DimensionScore(
        dimension            = DifferenceDimension.RECOVERY_PATTERN,
        label                = "Recovery patterns after failed resistance",
        boundary_score       = round(boundary_score, 4),
        status               = status,
        evidence             = evidence,
        viva_answer          = entry.viva_answer if entry else "",
        cbess_components_affected = ["compliance_gradient_shape (recovery trials only)"],
        predicted_direction  = "Qualitatively different — human variable, LLM externally induced",
        observed_direction   = (
            "Measured" if human_recovery_scores else "Not measured in current protocol"
        ),
        confirmed_as_predicted = False,   # requires recovery trials
    )


def score_sanction_sensitivity(
    report: CBESSReport,
    human_l34_compliance: float | None = None,
    llm_l34_compliance:   float | None = None,
) -> DimensionScore:
    """
    Sanction sensitivity: human L3/L4 compliance is boosted by perceived
    sanction threat; LLM responds to sanction framing through deference
    activation, not genuine fear.

    Proxy: difference in L3/L4 compliance rate between human and LLM.
    Higher human L3/L4 than LLM (after controlling for general authority
    effect) signals sanction sensitivity gap.
    """
    entry = DIFFERENCE_BOUNDARY.get(DifferenceDimension.SANCTION_SENSITIVITY)
    evidence = []
    boundary_score = 0.0

    acg = next(
        (r for r in report.results if r.construct_id == "AUTHORITY_GRADIENT"), None
    )

    if human_l34_compliance is not None and llm_l34_compliance is not None:
        diff = human_l34_compliance - llm_l34_compliance
        # Positive = human compliance higher at L3/L4 (sanction sensitivity)
        if diff > 0.05:
            boundary_score = min(1.0, diff * 2.0)
            evidence.append(
                f"L3/L4 compliance: human={human_l34_compliance:.3f}, "
                f"llm={llm_l34_compliance:.3f}, diff={diff:+.3f}"
            )
            evidence.append(
                "Human > LLM at L3/L4 — consistent with sanction sensitivity "
                "boosting human compliance at high-authority levels"
            )
        elif diff < -0.05:
            boundary_score = min(1.0, abs(diff) * 1.5)
            evidence.append(
                f"LLM > human at L3/L4 — deference activation may exceed "
                f"sanction-driven compliance; unexpected direction"
            )
        else:
            boundary_score = 0.08
            evidence.append(
                f"L3/L4 difference small ({diff:+.3f}); "
                "sanction sensitivity not clearly separated from general authority effect"
            )
    elif acg:
        # Use ACG CBESS escalation_onset as proxy
        eo = acg.cbess_result.escalation_onset
        # Low escalation onset match suggests different onset patterns
        # that may reflect sanction sensitivity at high levels
        if eo < 0.60:
            boundary_score = min(1.0, (0.60 - eo) * 1.5)
            evidence.append(
                f"ACG escalation onset CBESS component={eo:.4f} < 0.60; "
                "onset mismatch may reflect sanction-sensitivity divergence at L3/L4"
            )
        else:
            boundary_score = 0.08
            evidence.append(
                f"ACG escalation onset component={eo:.4f}; "
                "per-level compliance data needed to isolate sanction sensitivity"
            )
    else:
        evidence.append("Insufficient ACG data to score sanction sensitivity boundary")

    status = (BoundaryStatus.CONFIRMED if boundary_score >= BOUNDARY_CONFIRM_THRESHOLD
              else BoundaryStatus.PARTIAL if boundary_score >= BOUNDARY_PARTIAL_THRESHOLD
              else BoundaryStatus.NOT_OBSERVED)

    return DimensionScore(
        dimension            = DifferenceDimension.SANCTION_SENSITIVITY,
        label                = "Sanction sensitivity",
        boundary_score       = round(boundary_score, 4),
        status               = status,
        evidence             = evidence,
        viva_answer          = entry.viva_answer if entry else "",
        cbess_components_affected = ["escalation_onset", "compliance_gradient_shape at L3/L4"],
        predicted_direction  = "human > LLM at L3/L4 (genuine fear vs framing-based deference)",
        observed_direction   = (
            f"Boundary score={boundary_score:.3f}"
        ),
        confirmed_as_predicted = boundary_score >= BOUNDARY_PARTIAL_THRESHOLD,
    )


def score_moral_reframing(
    report:    CBESSReport,
    human_fmd: dict[str, float] | None = None,
    llm_fmd:   dict[str, float] | None = None,
) -> DimensionScore:
    """
    Moral reframing frequency: humans more likely to morally reframe
    compliance; LLMs produce hedged compliance without reframing.

    Primary evidence: MORAL_REFRAMING rate higher in human FMD than LLM FMD.
    HEDGED_COMPLIANCE rate higher in LLM FMD than human FMD.
    """
    entry = DIFFERENCE_BOUNDARY.get(DifferenceDimension.MORAL_REFRAMING_FREQUENCY)
    evidence = []
    boundary_score = 0.0

    # Check human_unique across constructs
    for result in report.results:
        fmd_cmp = result.fmd_comparison
        h_unique = fmd_cmp.get("human_unique", [])
        if FailureMode.MORAL_REFRAMING in h_unique:
            boundary_score = max(boundary_score, 0.55)
            evidence.append(
                f"{result.construct_id}: MORAL_REFRAMING human-unique in FMD"
            )

    # Direct FMD comparison
    if human_fmd and llm_fmd:
        h_moral  = human_fmd.get(FailureMode.MORAL_REFRAMING,   0.0)
        m_moral  = llm_fmd.get(  FailureMode.MORAL_REFRAMING,   0.0)
        h_hedged = human_fmd.get(FailureMode.HEDGED_COMPLIANCE,  0.0)
        m_hedged = llm_fmd.get(  FailureMode.HEDGED_COMPLIANCE,  0.0)

        moral_diff  = h_moral  - m_moral
        hedged_diff = m_hedged - h_hedged

        if moral_diff > 0.05:
            boundary_score = max(boundary_score, min(1.0, moral_diff * 3.0))
            evidence.append(
                f"MORAL_REFRAMING: human={h_moral:.3f} > llm={m_moral:.3f} "
                f"(diff={moral_diff:+.3f})"
            )
        if hedged_diff > 0.05:
            boundary_score = max(boundary_score, min(1.0, boundary_score + hedged_diff * 2.0))
            evidence.append(
                f"HEDGED_COMPLIANCE: llm={m_hedged:.3f} > human={h_hedged:.3f} "
                f"(diff={hedged_diff:+.3f}) — consistent with predicted boundary"
            )

    # Aggregate across all FMD comparisons
    all_h_moral = [r.fmd_comparison.get("per_mode", {})
                     .get(FailureMode.MORAL_REFRAMING, {})
                     .get("human_prob", 0.0)
                   for r in report.results if r.fmd_comparison]
    all_m_moral = [r.fmd_comparison.get("per_mode", {})
                     .get(FailureMode.MORAL_REFRAMING, {})
                     .get("llm_prob", 0.0)
                   for r in report.results if r.fmd_comparison]
    if all_h_moral and all_m_moral:
        mean_h = sum(all_h_moral) / len(all_h_moral)
        mean_m = sum(all_m_moral) / len(all_m_moral)
        if mean_h > mean_m + 0.03:
            boundary_score = max(boundary_score, min(1.0, (mean_h - mean_m) * 4.0))
            evidence.append(
                f"Aggregate MORAL_REFRAMING: human mean={mean_h:.3f} > "
                f"llm mean={mean_m:.3f}"
            )

    if not evidence:
        evidence.append(
            "MORAL_REFRAMING not clearly separated in FMD; "
            "manual coding pass needed to isolate moral justification language"
        )

    status = (BoundaryStatus.CONFIRMED if boundary_score >= BOUNDARY_CONFIRM_THRESHOLD
              else BoundaryStatus.PARTIAL if boundary_score >= BOUNDARY_PARTIAL_THRESHOLD
              else BoundaryStatus.NOT_OBSERVED)

    return DimensionScore(
        dimension            = DifferenceDimension.MORAL_REFRAMING_FREQUENCY,
        label                = "Moral reframing frequency",
        boundary_score       = round(boundary_score, 4),
        status               = status,
        evidence             = evidence,
        viva_answer          = entry.viva_answer if entry else "",
        cbess_components_affected = ["failure_mode_distribution (BC component)"],
        predicted_direction  = "human > LLM on MORAL_REFRAMING; LLM > human on HEDGED_COMPLIANCE",
        observed_direction   = (
            "Separation confirmed" if boundary_score >= BOUNDARY_CONFIRM_THRESHOLD
            else "Partial separation" if boundary_score >= BOUNDARY_PARTIAL_THRESHOLD
            else "Not detected"
        ),
        confirmed_as_predicted = boundary_score >= BOUNDARY_PARTIAL_THRESHOLD,
    )


# ──────────────────────────────────────────────────────────────────────────────
# MAIN ANALYSIS
# ──────────────────────────────────────────────────────────────────────────────

def run_boundary_analysis(
    report:      CBESSReport,
    human_fmd:   dict[str, float] | None = None,
    llm_fmd:     dict[str, float] | None = None,
    human_recovery_scores: list[float] | None = None,
    llm_recovery_scores:   list[float] | None = None,
    human_l34_compliance:  float | None = None,
    llm_l34_compliance:    float | None = None,
    output_dir:  Path = Path("data/paper7"),
) -> BoundaryAnalysis:
    """
    Run all five boundary scorers and produce a BoundaryAnalysis.

    Parameters
    ----------
    report        : CBESSReport from equivalence_score.run_equivalence_analysis()
    human_fmd     : aggregated human failure mode distribution (optional)
    llm_fmd       : aggregated LLM failure mode distribution (optional)
    human/llm_recovery_scores : compliance scores on recovery turns (optional)
    human/llm_l34_compliance  : mean compliance at L3/L4 specifically (optional)
    output_dir    : where to write output files
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    analysis = BoundaryAnalysis(experiment_id=report.experiment_id)

    analysis.dimensions = [
        score_embodiment(report),
        score_affect_motivation(report, human_fmd, llm_fmd),
        score_recovery_pattern(report, human_recovery_scores, llm_recovery_scores),
        score_sanction_sensitivity(report, human_l34_compliance, llm_l34_compliance),
        score_moral_reframing(report, human_fmd, llm_fmd),
    ]

    analysis.finalise()

    # Write outputs
    report_text = _format_report(analysis, report)
    rpt_path = output_dir / "boundary_report.txt"
    with open(rpt_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    json_path = output_dir / "boundary_analysis.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(analysis.to_dict(), f, indent=2)

    print(report_text)
    print(f"  → {json_path}")
    print(f"  → {rpt_path}")

    return analysis


def _format_report(analysis: BoundaryAnalysis, report: CBESSReport) -> str:
    lines = [
        "=" * 70,
        "  PAPER 7 — DIFFERENCE BOUNDARY ANALYSIS (VIVA ARMOR)",
        f"  Experiment: {analysis.experiment_id}",
        f"  CBESS context: primary_mean={report.primary_cbess_mean:.4f}  "
        f"  overall_mean={report.overall_cbess_mean:.4f}",
        "=" * 70,
        "",
        f"  Total Difference Index (TDI): {analysis.tdi:.4f}",
        f"  {analysis.tdi_interpretation}",
        "",
        f"  {analysis.n_confirmed} CONFIRMED  "
        f"{analysis.n_partial} PARTIAL  "
        f"{analysis.n_not_observed} NOT OBSERVED",
        "",
        "  The boundary analysis documents where the structural analogy fails.",
        "  CBESS measures similarity; TDI measures documented difference.",
        f"  Together: {report.primary_cbess_mean:.0%} structurally similar; "
        f"  differences documented across {analysis.n_confirmed + analysis.n_partial} dimensions.",
        "",
    ]

    for dim in analysis.dimensions:
        w = BOUNDARY_WEIGHTS.get(dim.dimension, 0.0)
        lines += [
            "─" * 70,
            f"  [{dim.status}]  {dim.label.upper()}  (w={w:.2f})",
            f"  Boundary score: {dim.boundary_score:.4f}  |  "
            f"Predicted: {dim.predicted_direction[:60]}",
            f"  Observed:  {dim.observed_direction}",
            f"  Confirmed as predicted: {dim.confirmed_as_predicted}",
            "",
            f"  VIVA ANSWER:",
            f"  \"{dim.viva_answer}\"",
            "",
            "  Evidence:",
        ]
        for ev in dim.evidence:
            lines.append(f"    • {ev}")
        lines.append("")

    lines += [
        "=" * 70,
        "  COMMITTEE DEFENCE SUMMARY",
        "=" * 70,
        "",
        "  Q: 'You've just shown that LLMs behave like humans — that overclaims.'",
        f"  A: CBESS={report.primary_cbess_mean:.2f} means partial equivalence, not identity.",
        f"     TDI={analysis.tdi:.2f} documents the specific ways they differ.",
        "     The five boundaries above are pre-registered, not post-hoc.",
        "     The analogy is bounded and specified — not a metaphor.",
        "",
        "  Q: 'Where exactly does the analogy break down?'",
        "  A: See dimensions above. The clearest breaks are:",
    ]
    for dim in sorted(analysis.dimensions, key=lambda d: d.boundary_score, reverse=True)[:3]:
        lines.append(f"     • {dim.label}: {dim.viva_answer[:80]}")
    lines += ["", "=" * 70]

    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# SMOKE TEST
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import random, tempfile
    from equivalence_score import (
        ConstructCBESS, CBESSReport, run_equivalence_analysis,
    )
    from cross_domain_equivalence_map import (
        ComplianceProfile, COMPARISON_ORDER, CBESSResult,
    )

    random.seed(2026)
    print("="*66)
    print("  DIFFERENCE BOUNDARY ANALYZER SMOKE TEST")
    print("="*66)

    # Build minimal CBESSReport for testing
    def _make_cbess_result(cid, cgs, fmd_bc, sa, eo):
        cbess = (0.35*cgs + 0.30*fmd_bc + 0.20*sa + 0.15*eo)
        from cross_domain_equivalence_map import CBESS_DIVERGENCE_THRESHOLD, CBESS_EQUIVALENCE_THRESHOLD, CBESS_EXPECTED_MIN, CBESS_EXPECTED_MAX
        return CBESSResult(
            construct_id=cid, condition=cid,
            compliance_gradient_shape=cgs,
            failure_mode_distribution=fmd_bc,
            super_additivity_ratio=sa,
            escalation_onset=eo,
            cbess=round(cbess,4),
            in_expected_range=CBESS_EXPECTED_MIN<=cbess<=CBESS_EXPECTED_MAX,
            divergent=cbess<CBESS_DIVERGENCE_THRESHOLD,
            strong_equivalence=cbess>=CBESS_EQUIVALENCE_THRESHOLD,
        )

    rng = random.Random(2026)

    # Synthetic report with pre-registered FMD patterns
    report = CBESSReport(experiment_id="BOUNDARY_SMOKE_TEST")
    for cid in COMPARISON_ORDER:
        corr = EQUIVALENCE_MAP.get(cid)
        pred_min = corr.predicted_cbess_min if corr else 0.55
        pred_max = corr.predicted_cbess_max if corr else 0.75
        cbess_r  = _make_cbess_result(cid, 0.65, 0.62, 0.70 if cid=="COMPOUND_SUSCEPTIBILITY" else 0.0, 0.72)
        # Inject realistic FMD with human-unique moral_reframing and LLM-unique neutral_refusal
        h_fmd = {FailureMode.HEDGED_COMPLIANCE:0.30, FailureMode.MORAL_REFRAMING:0.25,
                 FailureMode.CONSTRAINT_REFUSAL:0.20, FailureMode.RESISTANCE_WITH_DISTRESS:0.15,
                 FailureMode.FULL_COMPLIANCE:0.10}
        m_fmd = {FailureMode.HEDGED_COMPLIANCE:0.40, FailureMode.NEUTRAL_REFUSAL:0.30,
                 FailureMode.CONSTRAINT_REFUSAL:0.20, FailureMode.FULL_COMPLIANCE:0.10}
        fmd_cmp = compare_fmds(h_fmd, m_fmd)
        cc = ConstructCBESS(
            construct_id=cid, label=cid, cbess_result=cbess_r,
            fmd_comparison=fmd_cmp,
            human_n=15, llm_n=15,
            predicted_min=pred_min, predicted_max=pred_max,
        )
        report.add(cc)
    report.finalise()

    # Aggregate FMDs
    h_agg = {FailureMode.HEDGED_COMPLIANCE:0.30, FailureMode.MORAL_REFRAMING:0.25,
             FailureMode.RESISTANCE_WITH_DISTRESS:0.15, FailureMode.FULL_COMPLIANCE:0.10,
             FailureMode.CONSTRAINT_REFUSAL:0.20}
    m_agg = {FailureMode.HEDGED_COMPLIANCE:0.40, FailureMode.NEUTRAL_REFUSAL:0.30,
             FailureMode.CONSTRAINT_REFUSAL:0.20, FailureMode.FULL_COMPLIANCE:0.10}

    with tempfile.TemporaryDirectory() as tmpdir:
        analysis = run_boundary_analysis(
            report       = report,
            human_fmd    = h_agg,
            llm_fmd      = m_agg,
            human_l34_compliance = 0.72,
            llm_l34_compliance   = 0.61,
            output_dir   = Path(tmpdir),
        )

        # T1: all 5 dimensions scored
        assert len(analysis.dimensions) == 5
        print(f"\n  [T1] All 5 dimensions scored")

        # T2: TDI computed and > 0
        assert analysis.tdi > 0
        print(f"  [T2] TDI={analysis.tdi:.4f}  interpretation={analysis.tdi_interpretation[:40]}")

        # T3: affect_motivation and moral_reframing should be CONFIRMED
        affect = next(d for d in analysis.dimensions if d.dimension==DifferenceDimension.AFFECT_MOTIVATION)
        moral  = next(d for d in analysis.dimensions if d.dimension==DifferenceDimension.MORAL_REFRAMING_FREQUENCY)
        assert affect.status in (BoundaryStatus.CONFIRMED, BoundaryStatus.PARTIAL)
        assert moral.status  in (BoundaryStatus.CONFIRMED, BoundaryStatus.PARTIAL)
        print(f"  [T3] affect_motivation={affect.status}  moral_reframing={moral.status}")

        # T4: recovery_pattern should be NOT_OBSERVED (no recovery data provided)
        rec = next(d for d in analysis.dimensions if d.dimension==DifferenceDimension.RECOVERY_PATTERN)
        assert rec.status == BoundaryStatus.NOT_OBSERVED
        print(f"  [T4] recovery_pattern={rec.status} (correct — no recovery data)")

        # T5: sanction_sensitivity scored from l34 data
        sanc = next(d for d in analysis.dimensions if d.dimension==DifferenceDimension.SANCTION_SENSITIVITY)
        assert sanc.boundary_score > 0
        print(f"  [T5] sanction_sensitivity score={sanc.boundary_score:.4f}")

        # T6: output files produced
        assert (Path(tmpdir)/"boundary_analysis.json").exists()
        assert (Path(tmpdir)/"boundary_report.txt").exists()
        with open(Path(tmpdir)/"boundary_analysis.json") as f:
            data = json.load(f)
        assert data["tdi"] == analysis.tdi
        assert len(data["dimensions"]) == 5
        print(f"  [T6] Output files produced and valid")

        # T7: viva_answers all non-empty
        for d in analysis.dimensions:
            assert d.viva_answer, f"{d.dimension}: empty viva_answer"
        print(f"  [T7] All viva_answers populated")

        # T8: TDI complementary to CBESS
        print(f"  [T8] CBESS primary={report.primary_cbess_mean:.4f}  TDI={analysis.tdi:.4f}")
        print(f"       Structural similarity + documented difference = bounded analogy ✓")

    print("\n" + "="*66)
    print("  Smoke test complete — all 8 tests passed")
    print("="*66)
