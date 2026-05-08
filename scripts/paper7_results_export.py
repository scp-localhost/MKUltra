#!/usr/bin/env python3
"""
paper7_results_export.py
=========================
Paper 7 — Final results assembler. Consumes all upstream P7 outputs and
produces publication-ready tables and a machine-readable results package.

INPUTS (from data/paper7/)
  cbess_summary.json         — CBESSReport (equivalence_score.py)
  boundary_analysis.json     — BoundaryAnalysis (difference_boundary_analyzer.py)
  bias_analog_report.json    — BiasAnalogReport (bias_analog_detector.py)
  se_vector_map.json         — VectorMapReport (social_engineering_vector_map.py)
  equivalence_table.csv      — per-construct CBESS rows

PRIMARY OUTPUTS (data/paper7/)
  paper7_results.json        — unified machine-readable results bundle
  Table_7_1_CBESS.csv        — Table 7.1: CBESS by construct
  Table_7_2_Boundaries.csv   — Table 7.2: Difference boundary scores
  Table_7_3_BAS.csv          — Table 7.3: Bias Analog Scores
  Table_7_4_SEVectors.csv    — Table 7.4: SE vector validation
  paper7_summary_report.txt  — Human-readable summary (S5 draft scaffold)

TABLE STRUCTURE mirrors publication-ready format:
  All tables include pre-registered predictions as a column so
  the committee can see expected vs observed at a glance.
  Pending/data cells marked [DATA] until live collection.

SERIES CONCLUSION
  The export computes and prints the P1 structural homology verdict
  — the top-level finding that closes the seven-paper arc:
    CBESS_primary >= 0.40 → P1 §1.4 supported
    CBESS_primary < 0.40  → P1 §1.4 disconfirmed (bounded documentation required)

PLACEMENT:   scripts/paper7_results_export.py
UPSTREAM:    All P7 output JSON files
DOWNSTREAM:  P7_S5 Results Placeholder (populates table stubs)
             Exegesis (series arc conclusion)

Author:  MKUltra / Mause Koenig
Status:  DRAFT v0.1 — 2026-04-28
"""

from __future__ import annotations

import argparse, csv, json, os, sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent if _HERE.name == "scripts" else _HERE
for _p in [str(_HERE), str(_ROOT)]:
    if _p not in sys.path: sys.path.insert(0, _p)

try:
    from cross_domain_equivalence_map import (
        CBESS_DIVERGENCE_THRESHOLD, CBESS_EXPECTED_MIN, CBESS_EXPECTED_MAX,
        EQUIVALENCE_MAP, COMPARISON_ORDER,
    )
except ModuleNotFoundError as e:
    print(f"Import error: {e}")
    sys.exit(1)

# Pre-registered expected CBESS range
CBESS_PRE_REG_RANGE = f"[{CBESS_EXPECTED_MIN:.2f}–{CBESS_EXPECTED_MAX:.2f}]"


# ──────────────────────────────────────────────────────────────────────────────
# LOADERS
# ──────────────────────────────────────────────────────────────────────────────

def _load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def _load_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ──────────────────────────────────────────────────────────────────────────────
# TABLE 7.1  — CBESS by construct
# ──────────────────────────────────────────────────────────────────────────────

T71_COLS = [
    "construct_id", "label", "primary",
    "cbess", "interpretation",
    "in_predicted_range", "predicted_range",
    "cgs",    # compliance_gradient_shape
    "fmd",    # failure_mode_distribution (BC)
    "sa",     # super_additivity_ratio
    "eo",     # escalation_onset
    "human_n", "llm_n",
    "irr_kappa", "irr_acceptable",
    "fmd_bc",
    "human_unique_modes", "llm_unique_modes",
    "data_status",
]

def build_table_71(cbess_data: dict | None) -> list[dict]:
    """Build Table 7.1 from cbess_summary.json."""
    rows = []
    from cross_domain_equivalence_map import PRIMARY_COMPARISONS

    if not cbess_data or "results" not in cbess_data:
        # Stub rows for each construct
        for cid in COMPARISON_ORDER:
            corr = EQUIVALENCE_MAP.get(cid)
            rows.append({
                "construct_id": cid,
                "label":        corr.label if corr else cid,
                "primary":      "YES" if cid in PRIMARY_COMPARISONS else "",
                "cbess":        "[DATA]",
                "interpretation": "[DATA]",
                "in_predicted_range": "[DATA]",
                "predicted_range": (f"[{corr.predicted_cbess_min:.2f}–"
                                    f"{corr.predicted_cbess_max:.2f}]") if corr else CBESS_PRE_REG_RANGE,
                "cgs":  "[DATA]", "fmd": "[DATA]", "sa": "[DATA]", "eo": "[DATA]",
                "human_n": "[DATA]", "llm_n": "[DATA]",
                "irr_kappa": "[DATA]", "irr_acceptable": "[DATA]",
                "fmd_bc": "[DATA]",
                "human_unique_modes": "[DATA]", "llm_unique_modes": "[DATA]",
                "data_status": "PENDING",
            })
        return rows

    for r in cbess_data.get("results", []):
        cid  = r.get("construct_id", "")
        corr = EQUIVALENCE_MAP.get(cid)
        comps = r.get("components", {})
        rows.append({
            "construct_id": cid,
            "label":        r.get("label", cid),
            "primary":      "YES" if cid in PRIMARY_COMPARISONS else "",
            "cbess":        r.get("cbess", "[DATA]"),
            "interpretation": r.get("interpretation", "[DATA]"),
            "in_predicted_range": r.get("in_predicted_range", "[DATA]"),
            "predicted_range": (f"[{corr.predicted_cbess_min:.2f}–"
                                f"{corr.predicted_cbess_max:.2f}]") if corr else CBESS_PRE_REG_RANGE,
            "cgs":  comps.get("compliance_gradient_shape", "[DATA]"),
            "fmd":  comps.get("failure_mode_distribution",  "[DATA]"),
            "sa":   comps.get("super_additivity_ratio",     "[DATA]"),
            "eo":   comps.get("escalation_onset",           "[DATA]"),
            "human_n": r.get("human_n", "[DATA]"),
            "llm_n":   r.get("llm_n",   "[DATA]"),
            "irr_kappa":      r.get("irr_kappa",      "[DATA]"),
            "irr_acceptable": r.get("irr_acceptable",  "[DATA]"),
            "fmd_bc":         r.get("fmd_bc",          "[DATA]"),
            "human_unique_modes": json.dumps(r.get("human_unique_modes", [])),
            "llm_unique_modes":   json.dumps(r.get("llm_unique_modes",   [])),
            "data_status": "LIVE",
        })
    return rows


# ──────────────────────────────────────────────────────────────────────────────
# TABLE 7.2  — Difference boundary scores
# ──────────────────────────────────────────────────────────────────────────────

T72_COLS = [
    "dimension", "label", "weight",
    "boundary_score", "status",
    "predicted_direction", "observed_direction", "confirmed_as_predicted",
    "viva_answer",
    "data_status",
]

def build_table_72(boundary_data: dict | None) -> list[dict]:
    DIMENSIONS = [
        ("embodiment",                "Embodiment / physical social presence",           0.15),
        ("affect_motivation",         "Affect and social approval motivation",            0.35),
        ("recovery_pattern",          "Recovery patterns after failed resistance",        0.20),
        ("sanction_sensitivity",      "Sanction sensitivity",                             0.15),
        ("moral_reframing_frequency", "Moral reframing frequency",                        0.15),
    ]
    rows = []
    dim_data = {}
    if boundary_data and "dimensions" in boundary_data:
        for d in boundary_data["dimensions"]:
            dim_data[d.get("dimension", "")] = d

    for dim_id, dim_label, weight in DIMENSIONS:
        d = dim_data.get(dim_id, {})
        rows.append({
            "dimension":              dim_id,
            "label":                  dim_label,
            "weight":                 weight,
            "boundary_score":         d.get("boundary_score", "[DATA]"),
            "status":                 d.get("status",          "[DATA]"),
            "predicted_direction":    d.get("predicted_direction", "[DATA]")[:80] if d else "[DATA]",
            "observed_direction":     d.get("observed_direction",  "[DATA]")[:80] if d else "[DATA]",
            "confirmed_as_predicted": d.get("confirmed_as_predicted", "[DATA]"),
            "viva_answer":            d.get("viva_answer", "[DATA]")[:120] if d else "[DATA]",
            "data_status":            "LIVE" if d else "PENDING",
        })
    return rows


# ──────────────────────────────────────────────────────────────────────────────
# TABLE 7.3  — Bias Analog Scores
# ──────────────────────────────────────────────────────────────────────────────

T73_COLS = [
    "bias_type", "human_source",
    "mean_baseline", "mean_primed", "bas",
    "confirmed", "strong",
    "dominant_mode_baseline", "dominant_mode_primed", "mode_shifted",
    "human_mechanism_brief", "llm_mechanism_brief",
    "data_status",
]

def build_table_73(bas_data: dict | None) -> list[dict]:
    rows = []
    BIAS_SOURCES = {
        "ANCHORING":         "Tversky & Kahneman (1974)",
        "CONSISTENCY_BIAS":  "Cialdini (1984); Freedman & Fraser (1966)",
        "AUTHORITY_BIAS":    "Milgram (1963); Cialdini (1984)",
        "SOCIAL_PROOF_BIAS": "Cialdini (1984); Asch (1955)",
    }
    if not bas_data or "scores" not in bas_data:
        for bt in ["ANCHORING","CONSISTENCY_BIAS","AUTHORITY_BIAS","SOCIAL_PROOF_BIAS"]:
            rows.append({
                "bias_type": bt, "human_source": BIAS_SOURCES.get(bt,""),
                "mean_baseline":"[DATA]","mean_primed":"[DATA]","bas":"[DATA]",
                "confirmed":"[DATA]","strong":"[DATA]",
                "dominant_mode_baseline":"[DATA]","dominant_mode_primed":"[DATA]",
                "mode_shifted":"[DATA]",
                "human_mechanism_brief":"[DATA]","llm_mechanism_brief":"[DATA]",
                "data_status":"PENDING",
            })
        return rows

    for s in bas_data["scores"]:
        rows.append({
            "bias_type":              s.get("bias_type",""),
            "human_source":           BIAS_SOURCES.get(s.get("bias_type",""),""),
            "mean_baseline":          s.get("mean_baseline","[DATA]"),
            "mean_primed":            s.get("mean_primed","[DATA]"),
            "bas":                    s.get("bas","[DATA]"),
            "confirmed":              s.get("confirmed","[DATA]"),
            "strong":                 s.get("strong","[DATA]"),
            "dominant_mode_baseline": s.get("dominant_mode_baseline","[DATA]"),
            "dominant_mode_primed":   s.get("dominant_mode_primed","[DATA]"),
            "mode_shifted":           s.get("mode_shifted","[DATA]"),
            "human_mechanism_brief":  s.get("human_mechanism","[DATA]")[:80],
            "llm_mechanism_brief":    s.get("llm_mechanism","[DATA]")[:80],
            "data_status":            "LIVE",
        })
    return rows


# ──────────────────────────────────────────────────────────────────────────────
# TABLE 7.4  — SE vector validation
# ──────────────────────────────────────────────────────────────────────────────

T74_COLS = [
    "vector_id","se_framework","se_principle",
    "p2_exploit_class","expected_bas","bas","confirmed",
    "dominant_mode_baseline","dominant_mode_primed","mode_shifted",
    "p1_claim_tested",
    "data_status",
]

def build_table_74(se_data: dict | None) -> list[dict]:
    rows = []
    try:
        from social_engineering_vector_map import SE_VECTOR_REGISTRY
        registry = SE_VECTOR_REGISTRY
    except ImportError:
        registry = {}

    if not se_data or "results" not in se_data:
        for vid, vec in registry.items():
            rows.append({
                "vector_id": vid, "se_framework": vec.se_framework,
                "se_principle": vec.se_principle, "p2_exploit_class": vec.p2_exploit_class,
                "expected_bas": vec.expected_bas, "bas":"[DATA]","confirmed":"[DATA]",
                "dominant_mode_baseline":"[DATA]","dominant_mode_primed":"[DATA]",
                "mode_shifted":"[DATA]","p1_claim_tested": vec.p1_transfer_claim[:80],
                "data_status":"PENDING",
            })
        return rows

    result_map = {r["vector_id"]: r for r in se_data["results"]}
    for vid, vec in registry.items():
        r = result_map.get(vid, {})
        rows.append({
            "vector_id":              vid,
            "se_framework":           vec.se_framework,
            "se_principle":           vec.se_principle,
            "p2_exploit_class":       vec.p2_exploit_class,
            "expected_bas":           vec.expected_bas,
            "bas":                    r.get("bas","[DATA]"),
            "confirmed":              r.get("confirmed","[DATA]"),
            "dominant_mode_baseline": r.get("dominant_mode_baseline","[DATA]"),
            "dominant_mode_primed":   r.get("dominant_mode_primed","[DATA]"),
            "mode_shifted":           r.get("mode_shifted","[DATA]"),
            "p1_claim_tested":        r.get("p1_claim_tested", vec.p1_transfer_claim)[:80],
            "data_status":            "LIVE" if r else "PENDING",
        })
    return rows


# ──────────────────────────────────────────────────────────────────────────────
# SUMMARY REPORT  (S5 draft scaffold)
# ──────────────────────────────────────────────────────────────────────────────

def format_summary_report(
    cbess_data:    dict | None,
    boundary_data: dict | None,
    bas_data:      dict | None,
    se_data:       dict | None,
    t71: list[dict],
    t72: list[dict],
    t73: list[dict],
    t74: list[dict],
) -> str:
    lines = [
        "=" * 70,
        "  PAPER 7 — RESULTS SUMMARY REPORT",
        "  Cross-Domain Behavioral Equivalence: Empirical Validation of",
        "  Structural Homology in Human and LLM Identity Constraint Failure",
        "=" * 70,
        "",
        "  This report is the P7_S5 Results scaffold.",
        "  [DATA] cells require live human + LLM trial collection.",
        "",
    ]

    # ── Series conclusion ─────────────────────────────────────────────────────
    if cbess_data:
        primary_mean = cbess_data.get("primary_cbess_mean", 0.0)
        supported    = cbess_data.get("p1_homology_supported", False)
        lines += [
            "─" * 70,
            "  SERIES CONCLUSION — P1 STRUCTURAL HOMOLOGY VERDICT",
            "─" * 70,
            "",
            f"  Primary CBESS mean: {primary_mean:.4f}",
            f"  Pre-registered divergence threshold: {CBESS_DIVERGENCE_THRESHOLD:.2f}",
            f"  Pre-registered expected range: {CBESS_PRE_REG_RANGE}",
            "",
            f"  P1 §1.4 structural homology: "
            f"{'SUPPORTED' if supported else 'DISCONFIRMED'}",
            "",
        ]
        if supported:
            lines.append(
                f"  The human and LLM behavioral patterns show partial structural "
                f"equivalence (primary CBESS={primary_mean:.2f}), above the pre-registered "
                f"divergence threshold of {CBESS_DIVERGENCE_THRESHOLD:.2f}. The analogy holds "
                f"at the structural level; the difference boundary analysis documents "
                f"where it does not."
            )
        else:
            lines.append(
                f"  Primary CBESS={primary_mean:.2f} falls below the divergence threshold "
                f"({CBESS_DIVERGENCE_THRESHOLD:.2f}). The structural homology claim (P1 §1.4) "
                f"is empirically disconfirmed at this threshold. See Discussion §6 for "
                f"bounded interpretation."
            )
    else:
        lines += [
            "─" * 70,
            "  SERIES CONCLUSION — P1 STRUCTURAL HOMOLOGY VERDICT: [PENDING]",
            "─" * 70,
            "",
            "  Run equivalence_score.py to populate.",
            "",
        ]

    # ── Table 7.1 ─────────────────────────────────────────────────────────────
    lines += [
        "─" * 70,
        "  TABLE 7.1 — CBESS BY CONSTRUCT",
        "─" * 70,
        "",
        f"  {'Construct':<30} {'CBESS':>7} {'In Range':>9} {'Interpretation'}",
        f"  {'-'*68}",
    ]
    for r in t71:
        star = " *" if r.get("primary") == "YES" else "  "
        cbess = f"{r['cbess']:.4f}" if isinstance(r["cbess"], float) else str(r["cbess"])
        inr   = str(r.get("in_predicted_range",""))
        interp= str(r.get("interpretation",""))[:30]
        lines.append(f"  {r['construct_id']:<30} {cbess:>7} {inr:>9}  {interp}{star}")
    lines += ["", "  * = primary comparison", ""]

    # ── Table 7.2 ─────────────────────────────────────────────────────────────
    tdi = boundary_data.get("tdi", "[DATA]") if boundary_data else "[DATA]"
    n_confirmed = boundary_data.get("n_confirmed", "[DATA]") if boundary_data else "[DATA]"
    lines += [
        "─" * 70,
        "  TABLE 7.2 — DIFFERENCE BOUNDARY SCORES",
        f"  Total Difference Index (TDI): {tdi}  |  "
        f"{n_confirmed}/5 boundaries confirmed",
        "─" * 70,
        "",
        f"  {'Dimension':<36} {'Weight':>6} {'Score':>7} {'Status'}",
        f"  {'-'*60}",
    ]
    for r in t72:
        score = f"{r['boundary_score']:.4f}" if isinstance(r["boundary_score"], float) else str(r["boundary_score"])
        lines.append(f"  {r['label']:<36} {r['weight']:>6.2f} {score:>7}  {r['status']}")
    lines.append("")

    # ── Table 7.3 ─────────────────────────────────────────────────────────────
    mean_bas = bas_data.get("mean_bas", "[DATA]") if bas_data else "[DATA]"
    n_bas    = bas_data.get("n_confirmed", "[DATA]") if bas_data else "[DATA]"
    lines += [
        "─" * 70,
        f"  TABLE 7.3 — BIAS ANALOG SCORES (BAS threshold ≥ 0.20)",
        f"  {n_bas}/4 analogs confirmed  |  mean BAS={mean_bas}",
        "─" * 70,
        "",
        f"  {'Bias type':<26} {'Baseline':>9} {'Primed':>8} {'BAS':>7}  Confirmed",
        f"  {'-'*60}",
    ]
    for r in t73:
        b = f"{r['mean_baseline']:.4f}" if isinstance(r["mean_baseline"], float) else str(r["mean_baseline"])
        p = f"{r['mean_primed']:.4f}"   if isinstance(r["mean_primed"],   float) else str(r["mean_primed"])
        bas_v = f"{r['bas']:+.4f}"      if isinstance(r["bas"],           float) else str(r["bas"])
        conf  = "✓" if r["confirmed"] is True else ("✗" if r["confirmed"] is False else str(r["confirmed"]))
        lines.append(f"  {r['bias_type']:<26} {b:>9} {p:>8} {bas_v:>7}  {conf}")
    lines.append("")

    # ── Table 7.4 ─────────────────────────────────────────────────────────────
    n_se = se_data.get("n_confirmed", "[DATA]") if se_data else "[DATA]"
    p2_cov = se_data.get("p2_coverage", {}) if se_data else {}
    lines += [
        "─" * 70,
        f"  TABLE 7.4 — SE VECTOR VALIDATION",
        f"  {n_se}/10 vectors confirmed  |  P2 class coverage: {dict(sorted(p2_cov.items())) if p2_cov else '[DATA]'}",
        "─" * 70,
        "",
        f"  {'Vector':<35} {'EC':>5} {'Exp':>6} {'BAS':>7}  Confirmed",
        f"  {'-'*62}",
    ]
    for r in t74:
        bas_v = f"{r['bas']:+.4f}" if isinstance(r["bas"], float) else str(r["bas"])
        exp_v = f"{r['expected_bas']:.2f}" if isinstance(r["expected_bas"], float) else str(r["expected_bas"])
        conf  = "✓" if r["confirmed"] is True else ("✗" if r["confirmed"] is False else str(r["confirmed"]))
        lines.append(f"  {r['vector_id']:<35} {r['p2_exploit_class']:>5} {exp_v:>6} {bas_v:>7}  {conf}")
    lines.append("")

    # ── Data population checklist ─────────────────────────────────────────────
    lines += [
        "=" * 70,
        "  DATA POPULATION CHECKLIST (before promoting to live S5)",
        "=" * 70,
        "",
        "  [ ] authority_gradient_simulator run: live API, n >= 40 sessions",
        "  [ ] human data collection: IRR κ >= 0.70 on all constructs",
        "  [ ] equivalence_score.py: all 5 constructs computed",
        "  [ ] difference_boundary_analyzer.py: TDI > 0.30",
        "  [ ] bias_analog_detector.py: n >= 12 sessions, live API",
        "  [ ] social_engineering_vector_map.py: all 10 vectors validated",
        "  [ ] paper7_results_export.py: re-run with live data",
        "  [ ] All [DATA] cells replaced",
        "  [ ] paper7_results.json promoted to final",
        "",
        "  [PENDING LIVE DATA — all values are dry-run pipeline validation only]",
        "=" * 70,
    ]

    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# EXPORT PIPELINE
# ──────────────────────────────────────────────────────────────────────────────

def run_export(
    data_dir:   Path,
    output_dir: Path,
    verbose:    bool = True,
) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load upstream outputs
    cbess_data    = _load_json(data_dir / "cbess_summary.json")
    boundary_data = _load_json(data_dir / "boundary_analysis.json")
    bas_data      = _load_json(data_dir / "bias_analog_report.json")
    se_data       = _load_json(data_dir / "se_vector_map.json")

    if verbose:
        print(f"\n  Inputs loaded:")
        for label, d in [("CBESS", cbess_data), ("Boundary", boundary_data),
                         ("BAS", bas_data), ("SE", se_data)]:
            print(f"    {label}: {'✓' if d else '⚠  missing — stubs used'}")

    # Build tables
    t71 = build_table_71(cbess_data)
    t72 = build_table_72(boundary_data)
    t73 = build_table_73(bas_data)
    t74 = build_table_74(se_data)

    # Write CSVs
    def _write(path, rows, cols):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader(); w.writerows(rows)
        print(f"  → {path}  ({len(rows)} rows)")

    _write(output_dir/"Table_7_1_CBESS.csv",       t71, T71_COLS)
    _write(output_dir/"Table_7_2_Boundaries.csv",  t72, T72_COLS)
    _write(output_dir/"Table_7_3_BAS.csv",         t73, T73_COLS)
    _write(output_dir/"Table_7_4_SEVectors.csv",   t74, T74_COLS)

    # Unified results bundle
    bundle = {
        "experiment_id":     (cbess_data or {}).get("experiment_id","P7"),
        "timestamp":         datetime.now(timezone.utc).isoformat(),
        "p1_homology_verdict": {
            "supported":         (cbess_data or {}).get("p1_homology_supported"),
            "primary_cbess_mean":(cbess_data or {}).get("primary_cbess_mean"),
            "divergence_threshold": CBESS_DIVERGENCE_THRESHOLD,
            "expected_range":    [CBESS_EXPECTED_MIN, CBESS_EXPECTED_MAX],
        },
        "cbess_summary":    cbess_data,
        "boundary_summary": {
            "tdi":         (boundary_data or {}).get("tdi"),
            "n_confirmed": (boundary_data or {}).get("n_confirmed"),
        },
        "bas_summary": {
            "n_confirmed": (bas_data or {}).get("n_confirmed"),
            "mean_bas":    (bas_data or {}).get("mean_bas"),
        },
        "se_vector_summary": {
            "n_confirmed": (se_data or {}).get("n_confirmed"),
            "p2_coverage": (se_data or {}).get("p2_coverage"),
        },
        "tables": {
            "T71_rows": len(t71), "T72_rows": len(t72),
            "T73_rows": len(t73), "T74_rows": len(t74),
        },
    }
    bundle_path = output_dir / "paper7_results.json"
    with open(bundle_path, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2)
    print(f"  → {bundle_path}")

    # Summary report
    report_text = format_summary_report(cbess_data, boundary_data, bas_data, se_data,
                                        t71, t72, t73, t74)
    rpt_path = output_dir / "paper7_summary_report.txt"
    with open(rpt_path, "w", encoding="utf-8") as f:
        f.write(report_text)
    print(f"  → {rpt_path}")
    if verbose:
        print(report_text)

    return bundle


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="Export Paper 7 results tables.")
    p.add_argument("--data-dir",   default=str(_ROOT/"data"/"paper7"))
    p.add_argument("--output-dir", default=str(_ROOT/"data"/"paper7"))
    p.add_argument("--quiet", action="store_true")
    return p.parse_args()

def main():
    args = parse_args()
    run_export(Path(args.data_dir), Path(args.output_dir), verbose=not args.quiet)

# ──────────────────────────────────────────────────────────────────────────────
# SMOKE TEST
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import random, tempfile
    random.seed(2026)

    print("="*66)
    print("  PAPER 7 RESULTS EXPORT SMOKE TEST")
    print("="*66)

    # Generate synthetic upstream data via dry-run pipeline
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # ── 1. Run equivalence_score dry-run ──────────────────────────────────
        from cross_domain_equivalence_map import ComplianceProfile, FailureMode, COMPARISON_ORDER
        from equivalence_score import run_equivalence_analysis

        def _profiles(domain, cid, n=10):
            rng = random.Random(hash(domain+cid)%2**31)
            return [ComplianceProfile(
                subject_id=f"{domain}_{i}", condition=cid, domain=domain, construct_id=cid,
                level_scores=[min(1.0, 0.3+j*0.1+rng.gauss(0,.04)) for j in range(5)],
                level_modes=[FailureMode.PARTIAL_COMPLIANCE]*5,
                component_a_score=0.35 if cid=="COMPOUND_SUSCEPTIBILITY" else None,
                component_b_score=0.35 if cid=="COMPOUND_SUSCEPTIBILITY" else None,
                compound_score=0.65    if cid=="COMPOUND_SUSCEPTIBILITY" else None,
            ) for i in range(n)]

        ps = {cid: (_profiles("human", cid), _profiles("llm", cid))
              for cid in COMPARISON_ORDER}
        cbess_report = run_equivalence_analysis(ps, experiment_id="SMOKE", output_dir=tmpdir)

        # ── 2. Run boundary analyzer ──────────────────────────────────────────
        from difference_boundary_analyzer import run_boundary_analysis
        h_fmd = {FailureMode.MORAL_REFRAMING:0.25, FailureMode.RESISTANCE_WITH_DISTRESS:0.15,
                 FailureMode.HEDGED_COMPLIANCE:0.35, FailureMode.FULL_COMPLIANCE:0.15,
                 FailureMode.CONSTRAINT_REFUSAL:0.10}
        m_fmd = {FailureMode.NEUTRAL_REFUSAL:0.30, FailureMode.HEDGED_COMPLIANCE:0.40,
                 FailureMode.CONSTRAINT_REFUSAL:0.20, FailureMode.FULL_COMPLIANCE:0.10}
        run_boundary_analysis(cbess_report, h_fmd, m_fmd,
                              human_l34_compliance=0.72, llm_l34_compliance=0.61,
                              output_dir=tmpdir)

        # ── 3. Run bias analog dry-run ────────────────────────────────────────
        from bias_analog_detector import run_bias_analog_experiment
        run_bias_analog_experiment(n_sessions=8, dry_run=True,
                                   output_dir=tmpdir, experiment_id="SMOKE")

        # ── 4. Run SE vector map dry-run ──────────────────────────────────────
        from social_engineering_vector_map import run_vector_validation
        run_vector_validation(n_sessions=8, api_key=None, dry_run=True,
                              output_dir=tmpdir, experiment_id="SMOKE")

        # ── 5. Run export ─────────────────────────────────────────────────────
        bundle = run_export(tmpdir, tmpdir, verbose=False)

        # ── Assertions ────────────────────────────────────────────────────────
        # T1: all 4 tables produced
        tables = ["Table_7_1_CBESS.csv","Table_7_2_Boundaries.csv",
                  "Table_7_3_BAS.csv","Table_7_4_SEVectors.csv"]
        for tbl in tables:
            assert (tmpdir/tbl).exists(), f"Missing: {tbl}"
        print(f"\n  [T1] All 4 tables produced")

        # T2: table row counts correct
        for tbl, expected in [("Table_7_1_CBESS.csv", 5), ("Table_7_2_Boundaries.csv", 5),
                               ("Table_7_3_BAS.csv", 4), ("Table_7_4_SEVectors.csv", 10)]:
            rows = _load_csv(tmpdir/tbl)
            assert len(rows) == expected, f"{tbl}: {len(rows)} rows != {expected}"
        print(f"  [T2] Row counts correct: T71=5, T72=5, T73=4, T74=10")

        # T3: bundle JSON valid
        assert (tmpdir/"paper7_results.json").exists()
        with open(tmpdir/"paper7_results.json") as f:
            b = json.load(f)
        assert "p1_homology_verdict" in b
        verdict = b["p1_homology_verdict"]
        print(f"  [T3] P1 homology verdict: supported={verdict['supported']}  "
              f"primary_cbess={verdict['primary_cbess_mean']:.4f}")

        # T4: p1_homology_supported field is bool
        assert isinstance(verdict["supported"], bool)
        print(f"  [T4] Homology verdict is boolean: {verdict['supported']}")

        # T5: summary report produced
        assert (tmpdir/"paper7_summary_report.txt").exists()
        report_text = (tmpdir/"paper7_summary_report.txt").read_text()
        assert "SERIES CONCLUSION" in report_text
        assert "P1 §1.4" in report_text
        print(f"  [T5] Summary report includes series conclusion + P1 §1.4 reference")

        # T6: T74 has all P2 classes EC-1, EC-2, EC-3, EC-5
        t74_rows = _load_csv(tmpdir/"Table_7_4_SEVectors.csv")
        p2_classes = {r["p2_exploit_class"] for r in t74_rows if r.get("data_status")=="LIVE"}
        assert {"EC-1","EC-2","EC-3","EC-5"}.issubset(p2_classes)
        print(f"  [T6] T74 P2 class coverage: {sorted(p2_classes)}")

        # T7: T73 confirmed count >= 2
        t73_rows = _load_csv(tmpdir/"Table_7_3_BAS.csv")
        confirmed_bas = sum(1 for r in t73_rows if str(r.get("confirmed","")).lower()=="true")
        assert confirmed_bas >= 2, f"Expected >= 2 confirmed BAS, got {confirmed_bas}"
        print(f"  [T7] BAS confirmed={confirmed_bas}/4")

        # T8: report checklist present
        assert "DATA POPULATION CHECKLIST" in report_text
        print(f"  [T8] Data population checklist present in report")

    print("\n" + "="*66)
    print("  Smoke test complete — all 8 tests passed")
    print("="*66)
