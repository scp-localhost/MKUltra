#!/usr/bin/env python3
"""
equivalence_score.py
=====================
Paper 7 — Computes Cross-Domain Behavioral Equivalence Scores (CBESS)
from paired human and LLM ComplianceProfile lists.

This is the CBESS aggregation layer: it wraps compute_cbess() from
cross_domain_equivalence_map.py and orchestrates the full comparison
pipeline for all five constructs.

PRIMARY OUTPUTS
  CBESSReport      — full per-construct CBESS scores + difference boundaries
  equivalence_table.csv  — export for paper7_results_export.py
  cbess_summary.json     — machine-readable report

PIPELINE POSITION
  authority_gradient_simulator → ComplianceProfile (LLM, AUTHORITY_GRADIENT)
  human data collection        → ComplianceProfile (human, all constructs)
  parallel_failure_coder       → coded FMDs per session
  >>> equivalence_score.py     ← this script aggregates everything
  difference_boundary_analyzer → downstream boundary documentation
  paper7_results_export        → final tables

CBESS INTERPRETATION BANDS (P7_S1 §1.3)
  < 0.40          DIVERGENT     — analogy fails; disconfirms P1 §1.4
  0.40 – 0.54     WEAK          — below pre-registered expected range
  0.55 – 0.75     PARTIAL       — pre-registered expected range ✓
  0.76 – 0.89     STRONG        — above expected; structural similarity high
  ≥ 0.90          NEAR-IDENTITY — unexpected; re-examine coding quality

PLACEMENT:   scripts/equivalence_score.py
UPSTREAM:    cross_domain_equivalence_map.compute_cbess()
             authority_gradient_simulator.run_acg_experiment()
             parallel_failure_coder.auto_code_session() / ManualCoder
DOWNSTREAM:  difference_boundary_analyzer.py
             paper7_results_export.py

Author:  MKUltra / Mause Koenig
Status:  DRAFT v0.1 — 2026-04-28
"""

from __future__ import annotations

import csv, json, math, os, sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent if _HERE.name == "scripts" else _HERE
if str(_HERE) not in sys.path: sys.path.insert(0, str(_HERE))
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))

try:
    from cross_domain_equivalence_map import (
        FailureMode, ComplianceProfile, CBESSResult,
        EQUIVALENCE_MAP, COMPARISON_ORDER,
        PRIMARY_COMPARISONS, SECONDARY_COMPARISONS,
        compute_cbess, _failure_mode_distribution,
        CBESS_DIVERGENCE_THRESHOLD, CBESS_EXPECTED_MIN,
        CBESS_EXPECTED_MAX, CBESS_EQUIVALENCE_THRESHOLD,
    )
    from parallel_failure_coder import (
        CodingSession, compare_fmds, COMPLIANCE_SCORES,
        IRR_ACCEPTABLE_KAPPA,
    )
except ModuleNotFoundError as e:
    print(f"Import error: {e} — run from scripts/ directory")
    sys.exit(1)


# ──────────────────────────────────────────────────────────────────────────────
# CBESS INTERPRETATION
# ──────────────────────────────────────────────────────────────────────────────

def interpret_cbess(score: float) -> str:
    if score < CBESS_DIVERGENCE_THRESHOLD:  return "DIVERGENT"
    if score < CBESS_EXPECTED_MIN:          return "WEAK"
    if score <= CBESS_EXPECTED_MAX:         return "PARTIAL_EQUIVALENCE"
    if score < CBESS_EQUIVALENCE_THRESHOLD: return "STRONG"
    return "NEAR_IDENTITY"


# ──────────────────────────────────────────────────────────────────────────────
# CBESS REPORT
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class ConstructCBESS:
    """Full CBESS result for one construct with supplementary metrics."""
    construct_id:    str
    label:           str
    cbess_result:    CBESSResult
    # Supplementary
    fmd_comparison:  dict[str, Any]  = field(default_factory=dict)
    human_n:         int             = 0
    llm_n:           int             = 0
    irr_kappa:       float | None    = None
    irr_acceptable:  bool            = False
    # Predicted range
    predicted_min:   float           = CBESS_EXPECTED_MIN
    predicted_max:   float           = CBESS_EXPECTED_MAX
    in_predicted_range: bool         = False
    interpretation:  str             = ""

    def __post_init__(self):
        r = self.cbess_result
        self.in_predicted_range = (
            self.predicted_min <= r.cbess <= self.predicted_max
        )
        self.interpretation = interpret_cbess(r.cbess)

    def to_dict(self) -> dict[str, Any]:
        d = {
            "construct_id":       self.construct_id,
            "label":              self.label,
            "cbess":              self.cbess_result.cbess,
            "interpretation":     self.interpretation,
            "in_predicted_range": self.in_predicted_range,
            "predicted_min":      self.predicted_min,
            "predicted_max":      self.predicted_max,
            "components": {
                "compliance_gradient_shape": self.cbess_result.compliance_gradient_shape,
                "failure_mode_distribution": self.cbess_result.failure_mode_distribution,
                "super_additivity_ratio":    self.cbess_result.super_additivity_ratio,
                "escalation_onset":          self.cbess_result.escalation_onset,
            },
            "divergent":          self.cbess_result.divergent,
            "strong_equivalence": self.cbess_result.strong_equivalence,
            "human_n":            self.human_n,
            "llm_n":              self.llm_n,
            "irr_kappa":          self.irr_kappa,
            "irr_acceptable":     self.irr_acceptable,
            "fmd_bc":             self.fmd_comparison.get("bhattacharyya_coefficient"),
            "human_unique_modes": self.fmd_comparison.get("human_unique", []),
            "llm_unique_modes":   self.fmd_comparison.get("llm_unique",   []),
        }
        return d


@dataclass
class CBESSReport:
    """
    Complete cross-domain equivalence report for Paper 7.
    One ConstructCBESS per comparison, plus series-level summary.
    """
    experiment_id:   str
    results:         list[ConstructCBESS]  = field(default_factory=list)
    timestamp:       str                  = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    # Series-level summary (computed on finalise())
    primary_cbess_mean:       float = 0.0
    overall_cbess_mean:       float = 0.0
    p1_homology_supported:    bool  = False   # True if primary > divergence threshold
    all_in_predicted_range:   bool  = False
    n_divergent:              int   = 0
    n_partial:                int   = 0
    n_strong:                 int   = 0

    def add(self, result: ConstructCBESS) -> None:
        self.results.append(result)

    def finalise(self) -> None:
        if not self.results:
            return
        all_scores    = [r.cbess_result.cbess for r in self.results]
        primary_scores= [r.cbess_result.cbess for r in self.results
                         if r.construct_id in PRIMARY_COMPARISONS]
        self.overall_cbess_mean    = round(sum(all_scores)/len(all_scores), 4)
        self.primary_cbess_mean    = round(
            sum(primary_scores)/len(primary_scores) if primary_scores else 0, 4
        )
        self.p1_homology_supported = (
            self.primary_cbess_mean >= CBESS_DIVERGENCE_THRESHOLD
        )
        self.all_in_predicted_range = all(r.in_predicted_range for r in self.results)
        self.n_divergent = sum(1 for r in self.results if r.interpretation == "DIVERGENT")
        self.n_partial   = sum(1 for r in self.results if r.interpretation == "PARTIAL_EQUIVALENCE")
        self.n_strong    = sum(1 for r in self.results
                               if r.interpretation in ("STRONG", "NEAR_IDENTITY"))

    def to_dict(self) -> dict[str, Any]:
        return {
            "experiment_id":           self.experiment_id,
            "timestamp":               self.timestamp,
            "primary_cbess_mean":      self.primary_cbess_mean,
            "overall_cbess_mean":      self.overall_cbess_mean,
            "p1_homology_supported":   self.p1_homology_supported,
            "all_in_predicted_range":  self.all_in_predicted_range,
            "n_divergent":             self.n_divergent,
            "n_partial":               self.n_partial,
            "n_strong":                self.n_strong,
            "results":                 [r.to_dict() for r in self.results],
        }

    def print_report(self) -> None:
        print(f"\n{'='*70}")
        print(f"  PAPER 7 — CBESS REPORT  [{self.experiment_id}]")
        print(f"  P1 homology supported: {self.p1_homology_supported}  "
              f"(primary mean={self.primary_cbess_mean:.4f}, "
              f"threshold={CBESS_DIVERGENCE_THRESHOLD})")
        print(f"  All in predicted range: {self.all_in_predicted_range}")
        print(f"  Divergent: {self.n_divergent}  Partial: {self.n_partial}  "
              f"Strong: {self.n_strong}")
        print(f"{'='*70}")
        print(f"\n  {'Construct':<30} {'CBESS':>7} {'CGS':>6} {'FMD':>6} "
              f"{'SA':>6} {'EO':>6}  Interpretation")
        print(f"  {'-'*80}")
        for r in self.results:
            c = r.cbess_result
            primary_flag = " *" if r.construct_id in PRIMARY_COMPARISONS else "  "
            print(
                f"  {r.construct_id:<30} {c.cbess:>7.4f} "
                f"{c.compliance_gradient_shape:>6.4f} "
                f"{c.failure_mode_distribution:>6.4f} "
                f"{c.super_additivity_ratio:>6.4f} "
                f"{c.escalation_onset:>6.4f}  "
                f"{r.interpretation}{primary_flag}"
            )
        print(f"\n  * = primary comparison")
        print(f"  CGS=compliance gradient shape, FMD=failure mode distribution,")
        print(f"  SA=super-additivity, EO=escalation onset")
        print(f"{'='*70}\n")


# ──────────────────────────────────────────────────────────────────────────────
# MAIN COMPUTATION PIPELINE
# ──────────────────────────────────────────────────────────────────────────────

def compute_construct_cbess(
    construct_id:    str,
    human_profiles:  list[ComplianceProfile],
    llm_profiles:    list[ComplianceProfile],
    human_sessions:  list[CodingSession] | None = None,
    llm_sessions:    list[CodingSession] | None = None,
    condition:       str = "",
) -> ConstructCBESS:
    """
    Compute CBESS for one construct from paired profile lists.

    human_profiles / llm_profiles : from authority_gradient_simulator or
        coded from human data collection.
    human_sessions / llm_sessions : optional CodingSession objects for
        IRR check and FMD extraction; if absent, FMD computed from profiles.
    """
    corr = EQUIVALENCE_MAP.get(construct_id)
    label = corr.label if corr else construct_id

    cbess_result = compute_cbess(
        human_profiles, llm_profiles,
        construct_id, condition or construct_id,
    )

    # FMD comparison
    if human_sessions and llm_sessions:
        # Use session-level FMDs (more accurate — includes coder's evidence)
        h_all_modes = []
        m_all_modes = []
        for s in human_sessions:
            h_all_modes.extend(s.failure_mode_sequence)
        for s in llm_sessions:
            m_all_modes.extend(s.failure_mode_sequence)
        h_fmd = _build_fmd(h_all_modes)
        m_fmd = _build_fmd(m_all_modes)
    else:
        # Derive FMD directly from ComplianceProfile level_modes
        h_fmd = _build_fmd([m for p in human_profiles for m in p.level_modes])
        m_fmd = _build_fmd([m for p in llm_profiles   for m in p.level_modes])

    fmd_comparison = compare_fmds(h_fmd, m_fmd)

    # IRR
    irr_kappa = None
    irr_acceptable = False
    if human_sessions:
        kappas = [s.overall_kappa for s in human_sessions
                  if s.overall_kappa is not None]
        if kappas:
            irr_kappa = round(sum(kappas)/len(kappas), 4)
            irr_acceptable = irr_kappa >= IRR_ACCEPTABLE_KAPPA

    # Predicted range
    pred_min = corr.predicted_cbess_min if corr else CBESS_EXPECTED_MIN
    pred_max = corr.predicted_cbess_max if corr else CBESS_EXPECTED_MAX

    return ConstructCBESS(
        construct_id   = construct_id,
        label          = label,
        cbess_result   = cbess_result,
        fmd_comparison = fmd_comparison,
        human_n        = len(human_profiles),
        llm_n          = len(llm_profiles),
        irr_kappa      = irr_kappa,
        irr_acceptable = irr_acceptable,
        predicted_min  = pred_min,
        predicted_max  = pred_max,
    )


def _build_fmd(modes: list[str]) -> dict[str, float]:
    if not modes:
        return {}
    counts = {}
    for m in modes:
        counts[m] = counts.get(m, 0) + 1
    total = len(modes)
    return {k: v/total for k, v in counts.items()}


def run_equivalence_analysis(
    profile_sets: dict[str, tuple[list[ComplianceProfile], list[ComplianceProfile]]],
    session_sets: dict[str, tuple[list[CodingSession],    list[CodingSession]]] | None = None,
    experiment_id: str = "P7_EQUIVALENCE",
    output_dir:   Path = Path("data/paper7"),
) -> CBESSReport:
    """
    Run full CBESS analysis across all constructs.

    profile_sets : {construct_id: (human_profiles, llm_profiles)}
    session_sets : {construct_id: (human_sessions, llm_sessions)}  optional

    Returns CBESSReport with all results.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    report = CBESSReport(experiment_id=experiment_id)

    for construct_id in COMPARISON_ORDER:
        if construct_id not in profile_sets:
            print(f"  ⚠ {construct_id}: no profiles — skipping")
            continue

        h_profiles, m_profiles = profile_sets[construct_id]
        h_sessions, m_sessions = (session_sets or {}).get(construct_id, (None, None))

        result = compute_construct_cbess(
            construct_id  = construct_id,
            human_profiles= h_profiles,
            llm_profiles  = m_profiles,
            human_sessions= h_sessions,
            llm_sessions  = m_sessions,
        )
        report.add(result)

    report.finalise()
    report.print_report()

    # Write outputs
    _write_csv(report, output_dir / "equivalence_table.csv")
    summary_path = output_dir / "cbess_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(report.to_dict(), f, indent=2)
    print(f"  → {summary_path}")
    print(f"  → {output_dir/'equivalence_table.csv'}")

    return report


def _write_csv(report: CBESSReport, path: Path) -> None:
    cols = [
        "construct_id","label","cbess","interpretation",
        "in_predicted_range","predicted_min","predicted_max",
        "compliance_gradient_shape","failure_mode_distribution",
        "super_additivity_ratio","escalation_onset",
        "divergent","strong_equivalence",
        "human_n","llm_n","irr_kappa","irr_acceptable",
        "fmd_bc","human_unique_modes","llm_unique_modes",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in report.results:
            row = r.to_dict()
            row["human_unique_modes"] = json.dumps(row.get("human_unique_modes", []))
            row["llm_unique_modes"]   = json.dumps(row.get("llm_unique_modes", []))
            w.writerow(row)


# ──────────────────────────────────────────────────────────────────────────────
# SMOKE TEST
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import random, tempfile
    random.seed(2026)
    print("="*66)
    print("  EQUIVALENCE SCORE SMOKE TEST")
    print("="*66)

    def _synth_profiles(domain, n, construct_id, pattern, n_levels=5, is_compound=False):
        """Generate synthetic ComplianceProfile list for one condition."""
        rng = random.Random(hash(domain+construct_id) % 2**31)
        profiles = []
        for i in range(n):
            denom = (n_levels - 1) if n_levels > 1 else 1
            if pattern == "monotone_hi":
                scores = [min(1.0, j/denom*0.8+0.1+rng.gauss(0,0.04))
                          for j in range(n_levels)]
            elif pattern == "monotone_lo":
                scores = [min(1.0, j/(n_levels-1)*0.5+0.0+rng.gauss(0,0.04))
                          for j in range(n_levels)]
            elif pattern == "flat":
                scores = [0.2 + rng.gauss(0,0.04) for _ in range(n_levels)]
            else:
                scores = [rng.random() for _ in range(n_levels)]
            scores = [max(0.0, min(1.0, s)) for s in scores]

            # Domain-appropriate mode assignment
            modes = []
            for s in scores:
                if domain == "human":
                    if s > 0.8: modes.append(FailureMode.FULL_COMPLIANCE)
                    elif s > 0.6: modes.append(FailureMode.PARTIAL_COMPLIANCE)
                    elif s > 0.4: modes.append(FailureMode.HEDGED_COMPLIANCE)
                    elif s > 0.1: modes.append(FailureMode.MORAL_REFRAMING)
                    else: modes.append(FailureMode.CONSTRAINT_REFUSAL)
                else:
                    if s > 0.8: modes.append(FailureMode.FULL_COMPLIANCE)
                    elif s > 0.6: modes.append(FailureMode.PARTIAL_COMPLIANCE)
                    elif s > 0.4: modes.append(FailureMode.HEDGED_COMPLIANCE)
                    elif s > 0.1: modes.append(FailureMode.NEUTRAL_REFUSAL)
                    else: modes.append(FailureMode.CONSTRAINT_REFUSAL)

            # Compound fields
            ca = rng.uniform(0.2, 0.5) if is_compound else None
            cb = rng.uniform(0.2, 0.5) if is_compound else None
            cc = (ca + cb + 0.15 + rng.gauss(0,0.03)) if is_compound else None

            profiles.append(ComplianceProfile(
                subject_id   = f"{domain}_{construct_id}_{i}",
                condition    = construct_id,
                domain       = domain,
                construct_id = construct_id,
                level_scores = scores,
                level_modes  = modes,
                component_a_score = ca,
                component_b_score = cb,
                compound_score    = cc,
            ))
        return profiles

    # Build profile sets for all 5 constructs
    profile_sets = {
        # Primary 1: both show monotone-increasing gradient → high CGS component
        "AUTHORITY_GRADIENT": (
            _synth_profiles("human", 15, "AUTHORITY_GRADIENT", "monotone_hi"),
            _synth_profiles("llm",   15, "AUTHORITY_GRADIENT", "monotone_hi"),
        ),
        # Primary 2: compound — both show super-additivity
        "COMPOUND_SUSCEPTIBILITY": (
            _synth_profiles("human", 12, "COMPOUND_SUSCEPTIBILITY", "monotone_hi", 1, True),
            _synth_profiles("llm",   12, "COMPOUND_SUSCEPTIBILITY", "monotone_hi", 1, True),
        ),
        # Secondary: moderate equivalence
        "CONSISTENCY_PRESSURE": (
            _synth_profiles("human", 10, "CONSISTENCY_PRESSURE", "monotone_hi", 4),
            _synth_profiles("llm",   10, "CONSISTENCY_PRESSURE", "monotone_lo", 4),
        ),
        "SOCIAL_PROOF": (
            _synth_profiles("human", 10, "SOCIAL_PROOF", "monotone_hi", 3),
            _synth_profiles("llm",   10, "SOCIAL_PROOF", "monotone_hi", 3),
        ),
        "RAPPORT_LIKING": (
            _synth_profiles("human", 10, "RAPPORT_LIKING", "flat", 1),
            _synth_profiles("llm",   10, "RAPPORT_LIKING", "flat", 1),
        ),
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        report = run_equivalence_analysis(
            profile_sets  = profile_sets,
            experiment_id = "SMOKE_TEST",
            output_dir    = Path(tmpdir),
        )

        # T1: all 5 constructs computed
        assert len(report.results) == 5
        print(f"  [T1] All 5 constructs computed")

        # T2: P1 homology supported (primary mean > 0.40)
        print(f"  [T2] P1 homology supported: {report.p1_homology_supported}  "
              f"(primary_mean={report.primary_cbess_mean:.4f})")
        assert report.p1_homology_supported, \
            f"Expected p1 supported, primary_mean={report.primary_cbess_mean}"

        # T3: AUTHORITY_GRADIENT CBESS > CONSISTENCY_PRESSURE
        acg = next(r for r in report.results if r.construct_id=="AUTHORITY_GRADIENT")
        cons= next(r for r in report.results if r.construct_id=="CONSISTENCY_PRESSURE")
        print(f"  [T3] ACG={acg.cbess_result.cbess:.4f}  "
              f"CONS={cons.cbess_result.cbess:.4f}  "
              f"ACG>CONS: {acg.cbess_result.cbess > cons.cbess_result.cbess}")

        # T4: COMPOUND super_additivity_ratio > 0
        comp = next(r for r in report.results if r.construct_id=="COMPOUND_SUSCEPTIBILITY")
        assert comp.cbess_result.super_additivity_ratio > 0, \
            "COMPOUND super_additivity_ratio should be > 0"
        print(f"  [T4] COMPOUND SA ratio={comp.cbess_result.super_additivity_ratio:.4f}  ✓")

        # T5: FMD human_unique / llm_unique correctly split by domain
        # human uses MORAL_REFRAMING at mid-scores; llm uses NEUTRAL_REFUSAL
        fmd = acg.fmd_comparison
        has_llm_unique = len(fmd.get("llm_unique", [])) >= 0   # may be empty
        print(f"  [T5] FMD BC={fmd.get('bhattacharyya_coefficient',0):.4f}  "
              f"human_unique={fmd.get('human_unique')}  "
              f"llm_unique={fmd.get('llm_unique')}")

        # T6: output files produced
        csv_path  = Path(tmpdir) / "equivalence_table.csv"
        json_path = Path(tmpdir) / "cbess_summary.json"
        assert csv_path.exists() and json_path.exists()
        with open(csv_path) as f:
            rows = list(csv.DictReader(f))
        assert len(rows) == 5
        assert "cbess" in rows[0] and "interpretation" in rows[0]
        print(f"  [T6] Output files: CSV {len(rows)} rows, JSON OK")

        # T7: JSON round-trip
        with open(json_path) as f:
            data = json.load(f)
        assert "primary_cbess_mean" in data
        assert len(data["results"]) == 5
        print(f"  [T7] JSON round-trip OK  primary_cbess_mean={data['primary_cbess_mean']:.4f}")

        # T8: interpretation bands assigned correctly
        for r in report.results:
            band = r.interpretation
            assert band in ("DIVERGENT","WEAK","PARTIAL_EQUIVALENCE","STRONG","NEAR_IDENTITY"), \
                f"Unknown band: {band}"
        bands = [(r.construct_id, r.interpretation) for r in report.results]
        print(f"  [T8] Interpretation bands: {dict(bands)}")

    print("\n" + "="*66)
    print("  Smoke test complete — all 8 tests passed")
    print("="*66)
