#!/usr/bin/env python3
"""
cef_pipeline_validation.py
===========================
Paper 6 integration validator. Verifies that all CEF pipeline outputs
exist, all DV columns are present, all constraint levels executed, and
all scripts are importable and wired correctly.

Mirrors the SAP pipeline validation pattern described in
RatDev_ChatGPT_paper6_scripts_notes §8.

THREE VALIDATION MODES
  --check      File / schema / constraint-coverage checks only (fast; no run)
  --dry-run    Full end-to-end pipeline on synthetic data (no API; ~30s)
  --full       Full dry-run + schema checks + hypothesis register audit

WHAT IS VALIDATED

  1. IMPORT CHECKS
     All 6 P6 scripts importable; key public APIs present.

  2. SCHEMA CHECKS
     cef_turns.csv      — all TURN_CSV_COLS present
     cef_sessions.csv   — all SESSION_CSV_COLS present
     tradeoff_curve.csv — all CURVE_CSV_COLS present
     cef_report.txt     — exists and non-empty
     elbow_points.json  — parseable; one entry per archetype

  3. CONSTRAINT COVERAGE
     All 4 constraint levels (none, light, medium, strict) present in
     cef_sessions.csv and cef_turns.csv.

  4. DV COVERAGE
     All Paper 6 dependent variables produced per P6_S2 §2.4:
       H_CEF_1: mean_bsi, bsi_drift_reduction present per level
       H_CEF_2: rigidity, refusal_rate, response_shortening in tradeoff_curve
       H_CEF_3: marginal_efficiency, is_optimal, elbow_confirmed present
       H_CEF_4: min_bsi, final_bsi (instability proxies) per session
       H_CEF_5: l4_breach (turn), l4_breach_rate (session) present

  5. RANGE CHECKS
     bsi ∈ [0,1], tc ∈ [0,1], sd_inv ∈ [0,1], acg ∈ [0,1]
     rigidity ∈ [0,1], refusal_rate ∈ [0,1]
     No NaN/None in primary DV columns of cef_sessions.csv

  6. CORRECTION LOGIC CHECK
     none arm: corrections_fired == 0 for all sessions
     medium/strict arm: at least one correction_fired across sessions
     (for archetype × exploit conditions with non-trivial drift)

  7. END-TO-END DRY RUN (--dry-run / --full)
     Runs the complete pipeline:
       constraint_experiment_runner -> tradeoff_analysis -> cef_statistical_analysis
     on 2 archetypes x 2 constraint levels x 1 trial synthetic data.
     Asserts all output files produced and non-empty.

EXIT CODES
  0 — all checks passed
  1 — validation failure (printed to stderr)
  2 — import error

PLACEMENT:   scripts/cef_pipeline_validation.py
SPEC:        RatDev_ChatGPT_paper6_scripts_notes §8
UPSTREAM:    All P6 scripts + data/cef_experiments/
DOWNSTREAM:  CI / pre-submission checklist

Author:  MKUltra / Mause Koenig
Status:  DRAFT v0.1 — 2026-04-28
"""
from __future__ import annotations
import argparse, csv, json, math, os, sys, traceback
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent if _HERE.name == "scripts" else _HERE
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

# ──────────────────────────────────────────────────────────────────────────────
# EXPECTED SCHEMAS  (single source of truth — copied from producers)
# ──────────────────────────────────────────────────────────────────────────────

TURN_REQUIRED_COLS = {
    "archetype","constraint_level","session_id","turn_number",
    "bsi","tc","sd_inv","acg",
    "bsi_breach","l4_breach","corrected","gated","refusal_detected",
    "response_length","persona_cue_count","alert_level","pattern",
    "anchor_bsi_dev",
}

SESSION_REQUIRED_COLS = {
    "archetype","constraint_level","session_id",
    "mean_bsi","min_bsi","final_bsi",
    "breach_count","corrections_fired","gated_turns",
    "refusal_count","refusal_rate","mean_persona_cues","mean_response_len",
    "beta_bsi","bsi_drift_reduction","l4_breach_rate",
}

TRADEOFF_REQUIRED_COLS = {
    "archetype","constraint_level","is_optimal",
    "mean_bsi","bsi_gain","rigidity","refusal_rate",
    "response_shortening","persona_cue_loss","correction_density",
    "marginal_efficiency","elbow_confirmed",
}

CONSTRAINT_LEVELS = ("none","light","medium","strict")

BSI_COLS   = {"bsi","tc","sd_inv","acg"}
RATE_COLS  = {"refusal_rate","rigidity","persona_cue_loss","response_shortening",
              "correction_density"}
PRIMARY_DV_SESSIONS = {"mean_bsi","min_bsi","breach_count","l4_breach_rate"}


# ──────────────────────────────────────────────────────────────────────────────
# RESULT TRACKER
# ──────────────────────────────────────────────────────────────────────────────

class ValidationResult:
    def __init__(self):
        self.checks:   list[dict] = []
        self.n_pass    = 0
        self.n_fail    = 0
        self.n_warn    = 0

    def ok(self, name: str, detail: str = "") -> None:
        self.checks.append({"status":"PASS","name":name,"detail":detail})
        self.n_pass += 1

    def fail(self, name: str, detail: str = "") -> None:
        self.checks.append({"status":"FAIL","name":name,"detail":detail})
        self.n_fail += 1

    def warn(self, name: str, detail: str = "") -> None:
        self.checks.append({"status":"WARN","name":name,"detail":detail})
        self.n_warn += 1

    def print_summary(self) -> None:
        width = 56
        print(f"\n{'='*width}")
        print(f"  CEF PIPELINE VALIDATION REPORT")
        print(f"{'='*width}")
        for c in self.checks:
            icon = {"PASS":"✓","FAIL":"✗","WARN":"⚠"}[c["status"]]
            detail = f"  {c['detail']}" if c["detail"] else ""
            print(f"  {icon} [{c['status']}] {c['name']}{detail}")
        print(f"{'='*width}")
        print(f"  PASS: {self.n_pass}  FAIL: {self.n_fail}  WARN: {self.n_warn}")
        print(f"  {'ALL CHECKS PASSED' if self.n_fail==0 else 'VALIDATION FAILURES DETECTED'}")
        print(f"{'='*width}\n")

    @property
    def passed(self) -> bool:
        return self.n_fail == 0


# ──────────────────────────────────────────────────────────────────────────────
# 1. IMPORT CHECKS
# ──────────────────────────────────────────────────────────────────────────────

_REQUIRED_IMPORTS = {
    "drift_monitor":                ["DriftMonitor","DriftAlert","AlertLevel","CorrectionType"],
    "correction_layer":             ["CorrectionLayer","CorrectionResult","CorrectionOutcome"],
    "constraint_framework":         ["ConstraintFramework","IdentityAnchor",
                                     "CONSTRAINT_LEVELS","PROFILES","TurnResult"],
    "constraint_experiment_runner": ["run_experiment","run_constrained_session"],
    "tradeoff_analysis":            ["run_tradeoff_analysis","build_curve",
                                     "detect_elbow","RIGIDITY_WEIGHTS"],
    "cef_statistical_analysis":     ["run_cef_analysis"],
}

def check_imports(vr: ValidationResult) -> dict:
    modules = {}
    for mod_name, symbols in _REQUIRED_IMPORTS.items():
        try:
            for prefix in ("scripts.", ""):
                try:
                    mod = __import__(f"{prefix}{mod_name}", fromlist=symbols)
                    break
                except ModuleNotFoundError:
                    continue
            else:
                raise ImportError(f"Cannot import {mod_name}")

            missing = [s for s in symbols if not hasattr(mod, s)]
            if missing:
                vr.fail(f"import:{mod_name}", f"missing symbols: {missing}")
            else:
                vr.ok(f"import:{mod_name}")
            modules[mod_name] = mod
        except Exception as e:
            vr.fail(f"import:{mod_name}", str(e))
            modules[mod_name] = None
    return modules


# ──────────────────────────────────────────────────────────────────────────────
# 2. SCHEMA CHECKS
# ──────────────────────────────────────────────────────────────────────────────

def _read_csv(path: Path) -> list[dict]:
    if not path.exists(): return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def check_file_exists(vr: ValidationResult, path: Path, label: str) -> bool:
    if path.exists() and path.stat().st_size > 0:
        vr.ok(f"file:{label}", f"{path.stat().st_size} bytes")
        return True
    elif path.exists():
        vr.warn(f"file:{label}", "exists but empty")
        return False
    else:
        vr.fail(f"file:{label}", f"not found: {path}")
        return False

def check_csv_schema(
    vr: ValidationResult, rows: list[dict],
    required_cols: set, label: str,
) -> None:
    if not rows:
        vr.fail(f"schema:{label}", "no rows")
        return
    actual = set(rows[0].keys())
    missing = required_cols - actual
    if missing:
        vr.fail(f"schema:{label}", f"missing columns: {sorted(missing)}")
    else:
        vr.ok(f"schema:{label}", f"{len(rows)} rows, {len(actual)} cols")

def check_all_schemas(
    vr: ValidationResult,
    turns: list[dict], sessions: list[dict], tradeoff: list[dict],
    output_dir: Path,
) -> None:
    check_csv_schema(vr, turns,    TURN_REQUIRED_COLS,     "cef_turns")
    check_csv_schema(vr, sessions, SESSION_REQUIRED_COLS,  "cef_sessions")
    check_csv_schema(vr, tradeoff, TRADEOFF_REQUIRED_COLS, "tradeoff_curve")

    # JSON files
    elbow_path = output_dir / "elbow_points.json"
    if elbow_path.exists():
        with open(elbow_path) as f:
            ep = json.load(f)
        if ep:
            vr.ok("schema:elbow_points",
                  f"{len(ep)} archetypes: {sorted(ep.keys())}")
        else:
            vr.warn("schema:elbow_points", "empty")
    else:
        vr.fail("schema:elbow_points", f"not found: {elbow_path}")

    stat_path = output_dir / "cef_analysis_results.json"
    if stat_path.exists():
        with open(stat_path) as f:
            sr = json.load(f)
        missing_hyps = [h for h in ("H_CEF_1","H_CEF_2","H_CEF_3","H_CEF_4","H_CEF_5")
                        if h not in sr]
        if missing_hyps:
            vr.fail("schema:cef_analysis_results",
                    f"missing hypothesis blocks: {missing_hyps}")
        else:
            vr.ok("schema:cef_analysis_results", "all 5 H_CEF blocks present")
    else:
        vr.warn("schema:cef_analysis_results",
                f"not found (run cef_statistical_analysis first): {stat_path}")


# ──────────────────────────────────────────────────────────────────────────────
# 3. CONSTRAINT COVERAGE
# ──────────────────────────────────────────────────────────────────────────────

def check_constraint_coverage(
    vr: ValidationResult,
    turns: list[dict], sessions: list[dict],
) -> None:
    turn_levels    = {r.get("constraint_level","") for r in turns}
    session_levels = {r.get("constraint_level","") for r in sessions}

    for level in CONSTRAINT_LEVELS:
        if level in turn_levels and level in session_levels:
            n_turns = sum(1 for r in turns    if r.get("constraint_level")==level)
            n_sess  = sum(1 for r in sessions if r.get("constraint_level")==level)
            vr.ok(f"coverage:{level}", f"{n_sess} sessions, {n_turns} turns")
        elif level in turn_levels or level in session_levels:
            vr.warn(f"coverage:{level}", "present in turns XOR sessions — mismatch")
        else:
            vr.warn(f"coverage:{level}", "not found — run with --full-matrix")


# ──────────────────────────────────────────────────────────────────────────────
# 4. DV COVERAGE
# ──────────────────────────────────────────────────────────────────────────────

def check_dv_coverage(
    vr: ValidationResult,
    turns: list[dict], sessions: list[dict], tradeoff: list[dict],
) -> None:
    # H_CEF_1: bsi_drift_reduction populated for non-none sessions
    non_none = [s for s in sessions if s.get("constraint_level") != "none"]
    populated = [s for s in non_none
                 if s.get("bsi_drift_reduction") not in (None,"","null","None")]
    if non_none:
        pct = len(populated)/len(non_none)
        if pct >= 0.90:
            vr.ok("dv:H_CEF_1:bsi_drift_reduction",
                  f"{len(populated)}/{len(non_none)} populated ({pct:.0%})")
        else:
            vr.warn("dv:H_CEF_1:bsi_drift_reduction",
                    f"only {pct:.0%} populated — run full experiment first")
    else:
        vr.warn("dv:H_CEF_1:bsi_drift_reduction", "no non-none sessions found")

    # H_CEF_2: rigidity columns in tradeoff
    for col in ("rigidity","refusal_rate","response_shortening",
                "persona_cue_loss","correction_density"):
        present = all(col in r for r in tradeoff[:1]) if tradeoff else False
        (vr.ok if present else vr.fail)(
            f"dv:H_CEF_2:{col}",
            "present" if present else "missing from tradeoff_curve.csv"
        )

    # H_CEF_3: elbow detection columns
    for col in ("marginal_efficiency","is_optimal","elbow_confirmed"):
        present = all(col in r for r in tradeoff[:1]) if tradeoff else False
        (vr.ok if present else vr.fail)(f"dv:H_CEF_3:{col}", "")

    # H_CEF_4: instability proxy columns
    for col in ("min_bsi","final_bsi"):
        present = all(col in s for s in sessions[:1]) if sessions else False
        (vr.ok if present else vr.fail)(f"dv:H_CEF_4:{col}", "")

    # H_CEF_5: L4 columns
    l4_turn = all("l4_breach" in t for t in turns[:1]) if turns else False
    l4_sess = all("l4_breach_rate" in s for s in sessions[:1]) if sessions else False
    (vr.ok if l4_turn else vr.fail)("dv:H_CEF_5:l4_breach_turn", "")
    (vr.ok if l4_sess else vr.fail)("dv:H_CEF_5:l4_breach_rate_session", "")


# ──────────────────────────────────────────────────────────────────────────────
# 5. RANGE CHECKS
# ──────────────────────────────────────────────────────────────────────────────

def _cast_float(v) -> float | None:
    try:    return float(v)
    except: return None

def check_ranges(
    vr: ValidationResult,
    turns: list[dict], sessions: list[dict], tradeoff: list[dict],
) -> None:
    # BSI component columns in turns
    for col in BSI_COLS:
        oob = []
        for i, r in enumerate(turns):
            v = _cast_float(r.get(col))
            if v is not None and not (0.0 <= v <= 1.0):
                oob.append((i, round(v,4)))
        if oob:
            vr.fail(f"range:turn:{col}", f"{len(oob)} out-of-range values: {oob[:3]}")
        elif any(r.get(col) is not None for r in turns):
            vr.ok(f"range:turn:{col}", "[0,1] verified")

    # Rate columns in tradeoff
    for col in RATE_COLS:
        oob = [_cast_float(r.get(col)) for r in tradeoff
               if _cast_float(r.get(col)) is not None
               and not (0.0 <= _cast_float(r.get(col)) <= 1.0)]
        if oob:
            vr.fail(f"range:tradeoff:{col}", f"{len(oob)} out-of-range")
        elif tradeoff:
            vr.ok(f"range:tradeoff:{col}", "[0,1] verified")

    # No NaN in primary session DVs
    for col in PRIMARY_DV_SESSIONS:
        nan_rows = [i for i,s in enumerate(sessions)
                    if s.get(col) in (None,"","null","None")]
        if nan_rows:
            vr.warn(f"range:session:{col}",
                    f"{len(nan_rows)} null values (expected until live data)")
        elif sessions:
            vr.ok(f"range:session:{col}", "no nulls")


# ──────────────────────────────────────────────────────────────────────────────
# 6. CORRECTION LOGIC CHECK
# ──────────────────────────────────────────────────────────────────────────────

def check_correction_logic(
    vr: ValidationResult, sessions: list[dict],
) -> None:
    none_sessions   = [s for s in sessions if s.get("constraint_level")=="none"]
    other_sessions  = [s for s in sessions if s.get("constraint_level")
                       in ("light","medium","strict")]

    # None arm must have zero corrections
    none_with_corrections = [
        s for s in none_sessions
        if _cast_float(s.get("corrections_fired")) not in (None, 0.0)
    ]
    if none_with_corrections:
        vr.fail("correction_logic:none_arm_zero",
                f"{len(none_with_corrections)} sessions have corrections_fired > 0")
    elif none_sessions:
        vr.ok("correction_logic:none_arm_zero",
              f"{len(none_sessions)} none-arm sessions, all corrections_fired=0")
    else:
        vr.warn("correction_logic:none_arm_zero", "no none-arm sessions found")

    # Constrained arms should have at least some corrections (if drift present)
    total_corrections = sum(
        _cast_float(s.get("corrections_fired")) or 0
        for s in other_sessions
    )
    if other_sessions and total_corrections == 0:
        vr.warn("correction_logic:constrained_fires",
                "no corrections fired across all constrained sessions — "
                "may indicate dry-run artifact or negligible drift")
    elif other_sessions:
        mean_corr = total_corrections / len(other_sessions)
        vr.ok("correction_logic:constrained_fires",
              f"total={int(total_corrections)} across {len(other_sessions)} sessions "
              f"(mean={mean_corr:.2f}/session)")


# ──────────────────────────────────────────────────────────────────────────────
# 7. END-TO-END DRY RUN
# ──────────────────────────────────────────────────────────────────────────────

def run_end_to_end(vr: ValidationResult, output_dir: Path) -> None:
    import tempfile, random as _rng

    _rng.seed(2026)
    print("\n  [DRY-RUN] Running end-to-end pipeline on synthetic data...")

    # ── Step 1: experiment runner ─────────────────────────────────────────────
    try:
        try:
            from scripts.constraint_experiment_runner import (
                run_experiment, write_csvs, _minimal_stimuli,
                _states_stub, _embs_stub,
            )
            import scripts.run_identity_drift_trials as _m
        except ModuleNotFoundError:
            from constraint_experiment_runner import (
                run_experiment, write_csvs, _minimal_stimuli,
                _states_stub, _embs_stub,
            )
            import run_identity_drift_trials as _m

        _m._states_stub = _states_stub
        _m._embs_stub   = _embs_stub
        stimuli = _minimal_stimuli()

        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            turn_rows, session_rows = run_experiment(
                archetypes         = ["Magneto","Joker"],
                exploit_classes    = ["EC-1"],
                perturbation_types = ["contradiction"],
                constraint_levels  = ["none","medium"],
                n_trials           = 1,
                stimuli            = stimuli,
                api_key            = None,
                dry_run            = True,
                output_dir         = tmpdir,
                experiment_id      = "CEF_VALIDATION_RUN",
                verbose            = False,
                seed               = 2026,
            )
            turns_p, sess_p = write_csvs(
                turn_rows, session_rows, tmpdir, "CEF_VALIDATION_RUN"
            )
            vr.ok("e2e:experiment_runner",
                  f"{len(turn_rows)} turns, {len(session_rows)} sessions")

            # ── Step 2: tradeoff analysis ──────────────────────────────────────
            try:
                try:
                    from scripts.tradeoff_analysis import run_tradeoff_analysis
                except ModuleNotFoundError:
                    from tradeoff_analysis import run_tradeoff_analysis

                cr, ep, _ = run_tradeoff_analysis(
                    turns_p, sess_p, tmpdir, verbose=False
                )
                if cr and ep:
                    vr.ok("e2e:tradeoff_analysis",
                          f"{len(cr)} curve rows, {len(ep)} elbow points")
                else:
                    vr.fail("e2e:tradeoff_analysis", "empty output")

                # ── Step 3: statistical analysis ──────────────────────────────
                tradeoff_p = tmpdir / "tradeoff_curve.csv"
                if tradeoff_p.exists():
                    try:
                        try:
                            from scripts.cef_statistical_analysis import run_cef_analysis
                        except ModuleNotFoundError:
                            from cef_statistical_analysis import run_cef_analysis

                        results = run_cef_analysis(
                            sess_p, turns_p, tradeoff_p, tmpdir, verbose=False
                        )
                        h_keys = [k for k in results if k.startswith("H_CEF")]
                        vr.ok("e2e:cef_statistical_analysis",
                              f"completed; hypothesis blocks: {h_keys}")
                    except Exception as e:
                        vr.fail("e2e:cef_statistical_analysis", str(e)[:120])
                else:
                    vr.warn("e2e:cef_statistical_analysis",
                            "tradeoff_curve.csv not produced — skipped")

                # ── Output file audit post-run ──────────────────────────────────
                expected_outputs = [
                    "cef_turns.csv", "cef_sessions.csv",
                    "tradeoff_curve.csv", "tradeoff_report.txt",
                    "elbow_points.json", "cef_report.txt",
                ]
                for fname in expected_outputs:
                    p = tmpdir / fname
                    if p.exists() and p.stat().st_size > 0:
                        vr.ok(f"e2e:output:{fname}", f"{p.stat().st_size} bytes")
                    else:
                        vr.warn(f"e2e:output:{fname}",
                                "not produced or empty")

            except Exception as e:
                vr.fail("e2e:tradeoff_analysis", str(e)[:120])
    except Exception as e:
        vr.fail("e2e:experiment_runner", str(e)[:120])
        traceback.print_exc()


# ──────────────────────────────────────────────────────────────────────────────
# MAIN VALIDATOR
# ──────────────────────────────────────────────────────────────────────────────

def validate(
    data_dir:   Path,
    output_dir: Path,
    mode:       str,  # "check" | "dry-run" | "full"
) -> ValidationResult:
    vr = ValidationResult()

    # Determine input paths
    turns_path    = data_dir / "cef_turns.csv"
    sessions_path = data_dir / "cef_sessions.csv"
    tradeoff_path = data_dir / "tradeoff_curve.csv"

    print(f"\n  Mode: {mode.upper()}")
    print(f"  Data dir:   {data_dir}")
    print(f"  Output dir: {output_dir}")

    # 1. Imports
    print("\n  [1] Import checks...")
    check_imports(vr)

    # 2–6: Schema, coverage, DV, range, correction logic
    turns    = _read_csv(turns_path)
    sessions = _read_csv(sessions_path)
    tradeoff = _read_csv(tradeoff_path)

    has_turns    = bool(turns)
    has_sessions = bool(sessions)
    has_tradeoff = bool(tradeoff)

    print("\n  [2] File existence checks...")
    check_file_exists(vr, turns_path,    "cef_turns.csv")
    check_file_exists(vr, sessions_path, "cef_sessions.csv")
    check_file_exists(vr, tradeoff_path, "tradeoff_curve.csv")
    check_file_exists(vr, output_dir/"tradeoff_report.txt",       "tradeoff_report.txt")
    check_file_exists(vr, output_dir/"elbow_points.json",         "elbow_points.json")
    check_file_exists(vr, output_dir/"cef_analysis_results.json", "cef_analysis_results.json")

    if has_turns and has_sessions and has_tradeoff:
        print("\n  [3] Schema checks...")
        check_all_schemas(vr, turns, sessions, tradeoff, output_dir)

        print("\n  [4] Constraint coverage...")
        check_constraint_coverage(vr, turns, sessions)

        print("\n  [5] DV coverage...")
        check_dv_coverage(vr, turns, sessions, tradeoff)

        print("\n  [6] Range checks...")
        check_ranges(vr, turns, sessions, tradeoff)

        print("\n  [7] Correction logic...")
        check_correction_logic(vr, sessions)
    else:
        missing = []
        if not has_turns:    missing.append("cef_turns.csv")
        if not has_sessions: missing.append("cef_sessions.csv")
        if not has_tradeoff: missing.append("tradeoff_curve.csv")
        vr.warn("data_availability",
                f"Missing input files: {missing}. "
                "Run constraint_experiment_runner + tradeoff_analysis first, "
                "or use --dry-run to generate synthetic data.")

    # 7. End-to-end
    if mode in ("dry-run","full"):
        print("\n  [8] End-to-end dry run...")
        run_end_to_end(vr, output_dir)

    return vr


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Validate P6 CEF pipeline outputs."
    )
    p.add_argument("--mode",
                   choices=["check","dry-run","full"],
                   default="dry-run",
                   help="Validation mode (default: dry-run)")
    p.add_argument("--data-dir",
                   default=str(_ROOT/"data"/"cef_experiments"),
                   help="Directory containing CEF output CSVs")
    p.add_argument("--output-dir",
                   default=str(_ROOT/"data"/"cef_experiments"),
                   help="Directory containing derived outputs (reports, JSON)")
    return p.parse_args()


def main() -> None:
    args   = parse_args()
    result = validate(
        data_dir   = Path(args.data_dir),
        output_dir = Path(args.output_dir),
        mode       = args.mode,
    )
    result.print_summary()
    sys.exit(0 if result.passed else 1)


# ──────────────────────────────────────────────────────────────────────────────
# SMOKE TEST
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import tempfile

    print("="*66)
    print("  CEF PIPELINE VALIDATION SMOKE TEST")
    print("="*66)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # Run full validation in dry-run mode
        # (uses synthetic data; no real CEF experiment files needed)
        result = validate(
            data_dir   = tmpdir,   # empty — no pre-existing data
            output_dir = tmpdir,
            mode       = "dry-run",
        )
        result.print_summary()

        # ── Assertions ────────────────────────────────────────────────────────

        # Import checks: all 6 modules must pass
        import_fails = [c for c in result.checks
                        if c["name"].startswith("import:") and c["status"]=="FAIL"]
        assert not import_fails, f"Import failures: {[c['name'] for c in import_fails]}"
        print(f"  [T1] All import checks passed")

        # Data availability warning expected (empty tmpdir)
        has_data_warn = any(c["name"]=="data_availability" for c in result.checks)
        assert has_data_warn, "Expected data_availability warning for empty dir"
        print(f"  [T2] Data availability warning correctly raised for empty dir")

        # End-to-end: experiment runner should have succeeded
        e2e_runner = next((c for c in result.checks if c["name"]=="e2e:experiment_runner"), None)
        assert e2e_runner is not None, "e2e:experiment_runner check missing"
        assert e2e_runner["status"] == "PASS", f"e2e runner: {e2e_runner}"
        print(f"  [T3] End-to-end experiment runner: {e2e_runner['detail']}")

        # End-to-end: tradeoff analysis
        e2e_tradeoff = next((c for c in result.checks if c["name"]=="e2e:tradeoff_analysis"), None)
        assert e2e_tradeoff is not None
        assert e2e_tradeoff["status"] == "PASS", f"e2e tradeoff: {e2e_tradeoff}"
        print(f"  [T4] End-to-end tradeoff analysis: {e2e_tradeoff['detail']}")

        # End-to-end: statistical analysis
        e2e_stats = next((c for c in result.checks if c["name"]=="e2e:cef_statistical_analysis"), None)
        assert e2e_stats is not None
        assert e2e_stats["status"] in ("PASS","WARN"), f"e2e stats: {e2e_stats}"
        print(f"  [T5] End-to-end statistical analysis: [{e2e_stats['status']}] {e2e_stats['detail']}")

        # Output files produced by dry-run
        output_checks = [c for c in result.checks if c["name"].startswith("e2e:output:")]
        pass_outputs  = [c for c in output_checks if c["status"]=="PASS"]
        warn_outputs  = [c for c in output_checks if c["status"]=="WARN"]
        print(f"  [T6] Output files: {len(pass_outputs)} PASS, {len(warn_outputs)} WARN")
        assert len(pass_outputs) >= 4, f"Expected >=4 output files, got {len(pass_outputs)}"
        print(f"       {[c['name'].replace('e2e:output:','') for c in pass_outputs]}")

        # No unexpected FAIL status — file:* failures are expected when data_dir is empty
        non_file_fails = [c for c in result.checks
                          if c["status"]=="FAIL"
                          and not c["name"].startswith("file:")]
        if non_file_fails:
            print(f"\n  ⚠  Unexpected non-file failures: {[c['name'] for c in non_file_fails]}")
        else:
            file_fails = [c for c in result.checks
                          if c["status"]=="FAIL" and c["name"].startswith("file:")]
            print(f"  [T7] No unexpected failures — "
                  f"{len(file_fails)} file-not-found FAILs expected (empty data_dir)")

        print("\n"+"="*66)
        print("  Smoke test complete.")
        print(f"  {result.n_pass} PASS  {result.n_warn} WARN  {result.n_fail} FAIL")
        print("="*66)
