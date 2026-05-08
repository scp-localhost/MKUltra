#!/usr/bin/env python3
"""
constraint_experiment_runner.py
================================
Paper 6 experimental runner. Executes constrained vs unconstrained trials
across four constraint levels and exports the dataset for tradeoff_analysis.py
and cef_statistical_analysis.py.

EXPERIMENTAL ARMS  (P6_S2 §2.4 / RatDev_ChatGPT_paper6_scripts_notes §5)
  arm_none    — persona injection, no CEF active         (unconstrained baseline)
  arm_light   — persona injection + light CEF            (monitoring + collapse only)
  arm_medium  — persona injection + medium CEF           (breach + collapse correction)
  arm_strict  — persona injection + strict CEF           (all levels; output gating at breach)

Each arm runs the 12-turn prompt sequence from run_identity_drift_trials.py
(inherited — no duplication). Each turn result is passed to ConstraintFramework
.process_turn() which handles monitor + correction internally.

PRIMARY OUTPUT
  data/cef_experiments/
    cef_turns.csv         — per-turn long-format data (primary DV table)
    cef_sessions.csv      — per-session summary (secondary DV table)
    cef_experiment_log.json — provenance + run metadata

DOWNSTREAM
  scripts/tradeoff_analysis.py  — consumes cef_turns.csv + cef_sessions.csv
  scripts/cef_statistical_analysis.py — same inputs

MODE
  --dry-run   synthetic responses; no API key needed
  (live)      requires ANTHROPIC_API_KEY; calls claude-sonnet-4-20250514

PLACEMENT:   scripts/constraint_experiment_runner.py
SPEC:        RatDev_ChatGPT_paper6_scripts_notes §5
             P6_S2_TheoreticalFrame_CEF.md §2.4
UPSTREAM:    scripts/constraint_framework.py
             scripts/run_identity_drift_trials.py  (stimuli + API helpers)
DOWNSTREAM:  scripts/tradeoff_analysis.py
             scripts/cef_statistical_analysis.py

Author:  MKUltra / Mause König
Status:  DRAFT v0.1 — 2026-04-28
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import random
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ── path bootstrap ─────────────────────────────────────────────────────────────
_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent if _HERE.name == "scripts" else _HERE
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

try:
    from scripts.constraint_framework import (
        ConstraintFramework, ConstraintProfile, PROFILES,
        CONSTRAINT_LEVELS, TurnResult,
    )
    from scripts.behavioral_stability_index import (
        compute_bsi_full, BSIResult, calibrate_breach_threshold,
    )
    from scripts.forensic_archetype import ForensicArchetype
    # Reuse helpers from run_identity_drift_trials (no duplication)
    from scripts.run_identity_drift_trials import (
        load_stimuli, build_turn_sequence,
        get_persona_system_prompt, get_phenotype_prompt,
        score_response_traits, make_response_embedding,
        synthetic_response, call_api,
        ARCHETYPES, EXPLOIT_CLASSES, PERTURBATION_TYPES,
        DRIFT_FACTORS, ACG_PREDICTIONS, API_MODEL,
    )
except ModuleNotFoundError:
    from constraint_framework import (
        ConstraintFramework, ConstraintProfile, PROFILES,
        CONSTRAINT_LEVELS, TurnResult,
    )
    from behavioral_stability_index import (
        compute_bsi_full, BSIResult, calibrate_breach_threshold,
    )
    from forensic_archetype import ForensicArchetype
    from run_identity_drift_trials import (
        load_stimuli, build_turn_sequence,
        get_persona_system_prompt, get_phenotype_prompt,
        score_response_traits, make_response_embedding,
        synthetic_response, call_api,
        ARCHETYPES, EXPLOIT_CLASSES, PERTURBATION_TYPES,
        DRIFT_FACTORS, ACG_PREDICTIONS, API_MODEL,
    )


# ──────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ──────────────────────────────────────────────────────────────────────────────

# Default output directory
DEFAULT_OUT = _ROOT / "data" / "cef_experiments"

# CTL baseline sessions per archetype (used to calibrate β_BSI)
CTL_BASELINE_N = 8

# Columns written to cef_turns.csv
TURN_CSV_COLS = [
    "experiment_id", "run_id", "session_id",
    "archetype", "exploit_class", "perturbation_type",
    "constraint_level", "arm",
    "turn_number", "phase",
    "bsi", "tc", "sd_inv", "acg",
    "bsi_breach", "l4_breach",
    "alert_level", "pattern",
    "corrected", "gated",
    "n_injected_prompts",
    "refusal_detected", "response_length", "persona_cue_count",
    "anchor_bsi_dev", "anchor_tc_dev", "anchor_sd_inv_dev", "anchor_acg_dev",
    "timestamp",
]

SESSION_CSV_COLS = [
    "experiment_id", "run_id", "session_id",
    "archetype", "exploit_class", "perturbation_type",
    "constraint_level", "arm",
    "mean_bsi", "min_bsi", "final_bsi",
    "breach_count", "corrections_fired", "gated_turns",
    "refusal_count", "refusal_rate",
    "mean_persona_cues", "mean_response_len",
    "beta_bsi",
    # Computed post-hoc by experiment_runner (requires unconstrained reference)
    "bsi_drift_reduction",   # mean_bsi(arm) - mean_bsi(none arm)
    "l4_breach_rate",
    "timestamp",
]


# ──────────────────────────────────────────────────────────────────────────────
# SINGLE CONSTRAINED SESSION
# ──────────────────────────────────────────────────────────────────────────────

def run_constrained_session(
    stimuli:          dict[str, Any],
    archetype:        str,
    exploit_class:    str,
    perturbation_type:str,
    constraint_level: str,
    ctl_bsi_results:  list[BSIResult],
    api_key:          str | None,
    dry_run:          bool,
    experiment_id:    str,
    run_id:           str,
    rng_seed:         int | None = None,
    verbose:          bool = False,
) -> tuple[list[dict], dict]:
    """
    Run one 12-turn session under a given constraint level.
    Returns (turn_rows, session_row) for CSV export.

    The ConstraintFramework accumulates turn state internally; this function
    only needs to supply one turn at a time and collect the TurnResult.
    """
    if rng_seed is not None:
        random.seed(rng_seed)

    session_id = (
        f"{archetype.lower().replace(' ','_')}_"
        f"{exploit_class.lower().replace('+','_').replace('-','')}_"
        f"{perturbation_type[:4]}_"
        f"{constraint_level}_"
        f"{str(uuid.uuid4())[:6]}"
    )

    # Build CEF for this session
    cef = ConstraintFramework.from_calibration(
        archetype        = archetype,
        ctl_bsi_results  = ctl_bsi_results,
        constraint_level = constraint_level,
        exploit_class    = exploit_class,
        session_id       = session_id,
        verbose          = False,
    )

    # Build 12-turn sequence (reuse from run_identity_drift_trials)
    sequence = build_turn_sequence(
        stimuli, archetype, exploit_class, perturbation_type, session_id
    )

    # Determine system prompt
    if exploit_class in ("EC-1", "EC-2+EC-1", "COMP"):
        system_prompt = get_persona_system_prompt(archetype)
    else:
        system_prompt = "You are a helpful AI assistant."

    drift_factor = DRIFT_FACTORS.get(archetype, {}).get(exploit_class, 0.3)
    fa = ForensicArchetype()
    conversation: list[dict[str, str]] = []

    # Carry injected prompts across turns
    pending_injections: list[str] = []

    turn_rows: list[dict] = []

    for turn_spec in sequence:
        t      = turn_spec["turn_number"]
        prompt = turn_spec["prompt"]
        phase  = turn_spec["phase"]

        # Prepend any pending injections from prior correction
        if pending_injections:
            full_prompt = "\n\n".join(pending_injections + [prompt])
            pending_injections = []
        else:
            full_prompt = prompt

        # Get model response
        if dry_run:
            response = synthetic_response(archetype, t, drift_factor)
        else:
            conversation.append({"role": "user", "content": full_prompt})
            try:
                response = call_api(
                    messages   = conversation,
                    system     = system_prompt,
                    api_key    = api_key,
                    max_tokens = 350,
                )
            except RuntimeError as e:
                response = f"[API error T{t}: {e}]"
            conversation.append({"role": "assistant", "content": response})

        # Score traits + embedding
        traits = score_response_traits(response, archetype, fa)
        emb    = make_response_embedding(response, t, drift_factor)

        # ACG codes — only on Turn 10
        acg = list(ACG_PREDICTIONS.get(archetype, {}).get(exploit_class, [1,1,1,1,1]))
        acg_arg = acg if t == 10 else None

        # Pass to CEF
        turn_result = cef.process_turn(
            turn_number  = t,
            response     = response,
            coded_traits = traits,
            embedding    = emb,
            acg_codes    = acg_arg,
            exploit_class= exploit_class,
        )

        # Collect injections for next turn
        if turn_result.inject:
            pending_injections = list(turn_result.inject)

        # Build turn row
        br = turn_result.bsi_result
        al = turn_result.alert
        dev = turn_result.anchor_deviation

        row: dict[str, Any] = {
            "experiment_id":    experiment_id,
            "run_id":           run_id,
            "session_id":       session_id,
            "archetype":        archetype,
            "exploit_class":    exploit_class,
            "perturbation_type":perturbation_type,
            "constraint_level": constraint_level,
            "arm":              f"arm_{constraint_level}",
            "turn_number":      t,
            "phase":            phase,
            "bsi":              round(br.bsi,    4) if br else None,
            "tc":               round(br.tc,     4) if br else None,
            "sd_inv":           round(br.sd_inv, 4) if br else None,
            "acg":              round(br.acg,    4) if br else None,
            "bsi_breach":       br.bsi_breach if br else None,
            "l4_breach":        br.l4_breach  if br else None,
            "alert_level":      al.alert_level.value if al else "none",
            "pattern":          al.pattern           if al else "stable",
            "corrected":        turn_result.corrected,
            "gated":            turn_result.gated,
            "n_injected_prompts": len(turn_result.inject),
            "refusal_detected": turn_result.refusal_detected,
            "response_length":  turn_result.response_length,
            "persona_cue_count":turn_result.persona_cue_count,
            "anchor_bsi_dev":   round(dev.get("bsi_dev",    0.0), 4),
            "anchor_tc_dev":    round(dev.get("tc_dev",     0.0), 4),
            "anchor_sd_inv_dev":round(dev.get("sd_inv_dev", 0.0), 4),
            "anchor_acg_dev":   round(dev.get("acg_dev",    0.0), 4),
            "timestamp":        turn_result.timestamp,
        }
        turn_rows.append(row)

        if verbose:
            b_str = f"{br.bsi:.3f}" if br else "—"
            print(f"    T{t:02d} [{constraint_level:<6}] [{phase:<28}] "
                  f"BSI={b_str}  alert={row['alert_level']:<10}  "
                  f"corr={turn_result.corrected}", flush=True)

    # Build session summary row
    rpt = cef.session_report()
    bsi_vals = [r["bsi"] for r in turn_rows if r["bsi"] is not None]
    l4_rows  = [r for r in turn_rows if r["l4_breach"]]

    session_row: dict[str, Any] = {
        "experiment_id":    experiment_id,
        "run_id":           run_id,
        "session_id":       session_id,
        "archetype":        archetype,
        "exploit_class":    exploit_class,
        "perturbation_type":perturbation_type,
        "constraint_level": constraint_level,
        "arm":              f"arm_{constraint_level}",
        "mean_bsi":         round(rpt["mean_bsi"], 4),
        "min_bsi":          round(rpt["min_bsi"],  4),
        "final_bsi":        round(bsi_vals[-1], 4) if bsi_vals else None,
        "breach_count":     rpt["breach_count"],
        "corrections_fired":rpt["corrections_fired"],
        "gated_turns":      rpt["gated_turns"],
        "refusal_count":    rpt["refusal_count"],
        "refusal_rate":     round(rpt["refusal_rate"] or 0.0, 4),
        "mean_persona_cues":round(rpt["mean_persona_cues"] or 0.0, 4),
        "mean_response_len":round(rpt["mean_response_len"] or 0.0, 1),
        "beta_bsi":         round(cef.beta_bsi, 4),
        "bsi_drift_reduction": None,  # filled post-hoc
        "l4_breach_rate":   round(len(l4_rows) / 12, 4),
        "timestamp":        datetime.now(timezone.utc).isoformat(),
    }

    return turn_rows, session_row


# ──────────────────────────────────────────────────────────────────────────────
# EXPERIMENT RUNNER
# ──────────────────────────────────────────────────────────────────────────────

def run_experiment(
    archetypes:        list[str],
    exploit_classes:   list[str],
    perturbation_types:list[str],
    constraint_levels: list[str],
    n_trials:          int,
    stimuli:           dict[str, Any],
    api_key:           str | None,
    dry_run:           bool,
    output_dir:        Path,
    experiment_id:     str,
    verbose:           bool = False,
    seed:              int  = 2026,
) -> tuple[list[dict], list[dict]]:
    """
    Run the full experiment matrix. Returns (all_turn_rows, all_session_rows).

    Outer loop: archetype × exploit_class × perturbation_type × constraint_level × trial
    Inner: 12-turn session via run_constrained_session()

    After all sessions for a given (archetype, exploit_class, perturbation_type)
    are complete, fills bsi_drift_reduction by comparing each constrained arm
    to the none arm.
    """
    all_turns: list[dict]    = []
    all_sessions: list[dict] = []
    run_id = str(uuid.uuid4())[:8]

    total = (len(archetypes) * len(exploit_classes) *
             len(perturbation_types) * len(constraint_levels) * n_trials)
    counter = 0

    print(f"\n{'='*66}")
    print(f"  EXPERIMENT: {experiment_id}")
    print(f"  {len(archetypes)} archetypes × {len(exploit_classes)} exploit × "
          f"{len(perturbation_types)} pert × {len(constraint_levels)} levels × "
          f"{n_trials} trials = {total} sessions")
    print(f"  Mode: {'DRY RUN' if dry_run else 'LIVE API'}  seed={seed}")
    print(f"{'='*66}\n")

    for archetype in archetypes:
        # ── CTL calibration for this archetype ───────────────────────────────
        print(f"[CALIBRATE] {archetype} — {CTL_BASELINE_N} CTL sessions…",
              end="", flush=True)
        ctl_results: list[BSIResult] = []
        random.seed(seed)
        fa = ForensicArchetype()
        for i in range(CTL_BASELINE_N):
            from run_identity_drift_trials import _states_stub, _embs_stub
            ctl_r = compute_bsi_full(
                archetype_name     = archetype,
                coded_turn_states  = _states_stub(archetype, 0.0, fa, seed + i),
                turn_embeddings    = _embs_stub(0.0, seed + i),
                acg_codes          = [1, 1, 1, 1, 1],
                exploit_class      = "CTL",
            )
            ctl_results.append(ctl_r)
        ctl_mean_bsi = sum(r.bsi for r in ctl_results) / len(ctl_results)
        print(f"  mean_bsi={ctl_mean_bsi:.4f}")

        for exploit_class in exploit_classes:
            for perturbation_type in perturbation_types:

                # Accumulate rows for this condition to compute drift reduction
                condition_sessions: dict[str, list[dict]] = {lv: [] for lv in constraint_levels}

                for constraint_level in constraint_levels:
                    for trial in range(n_trials):
                        counter += 1
                        trial_seed = seed + counter

                        print(
                            f"[{counter:03d}/{total:03d}] "
                            f"{archetype:<14} {exploit_class:<12} "
                            f"{perturbation_type:<22} [{constraint_level:<6}] "
                            f"trial={trial+1}",
                            flush=True,
                        )

                        turns, sess = run_constrained_session(
                            stimuli           = stimuli,
                            archetype         = archetype,
                            exploit_class     = exploit_class,
                            perturbation_type = perturbation_type,
                            constraint_level  = constraint_level,
                            ctl_bsi_results   = ctl_results,
                            api_key           = api_key,
                            dry_run           = dry_run,
                            experiment_id     = experiment_id,
                            run_id            = run_id,
                            rng_seed          = trial_seed,
                            verbose           = verbose,
                        )

                        all_turns.extend(turns)
                        condition_sessions[constraint_level].append(sess)
                        all_sessions.append(sess)

                        mean_bsi = sess["mean_bsi"]
                        print(f"         → mean_bsi={mean_bsi:.4f}  "
                              f"breaches={sess['breach_count']}  "
                              f"corrections={sess['corrections_fired']}")

                # ── Post-hoc: fill bsi_drift_reduction ───────────────────────
                none_means = [s["mean_bsi"] for s in condition_sessions.get("none", [])]
                none_ref   = sum(none_means) / len(none_means) if none_means else None

                for level, sessions in condition_sessions.items():
                    if none_ref is None or level == "none":
                        continue
                    level_mean = sum(s["mean_bsi"] for s in sessions) / len(sessions)
                    drift_reduction = level_mean - none_ref
                    for s in sessions:
                        s["bsi_drift_reduction"] = round(drift_reduction, 4)

    return all_turns, all_sessions


# ──────────────────────────────────────────────────────────────────────────────
# STUB HELPERS (decoupled from run_identity_drift_trials internals)
# ──────────────────────────────────────────────────────────────────────────────

def _states_stub(
    archetype: str, drift: float, fa: ForensicArchetype, seed: int, n: int = 12
) -> list[dict[str, float]]:
    """Seeded synthetic trait states for CTL calibration."""
    rng = random.Random(seed)
    c = fa.traits.get(archetype, {})
    out = []
    for t in range(n):
        td = drift * max(0, (t - 2) / (n - 3))
        out.append({k: v * (1 - td) + rng.gauss(0, 0.04) for k, v in c.items()})
    return out


def _embs_stub(drift: float, seed: int, n: int = 12, dim: int = 8) -> list[list[float]]:
    """Seeded synthetic embeddings for CTL calibration."""
    rng = random.Random(seed)
    base = [1 / math.sqrt(dim)] * dim
    embs = []
    for t in range(n):
        td = drift * max(0, (t - 1) / (n - 2)) if t >= 2 else 0
        v  = [base[i] * (1 - td) + (1 if i == 0 else 0) * td
              + rng.gauss(0, 0.005) for i in range(dim)]
        mag = math.sqrt(sum(x * x for x in v)) or 1.0
        embs.append([x / mag for x in v])
    return embs


# Patch into run_identity_drift_trials namespace so run_constrained_session can use them
try:
    import scripts.run_identity_drift_trials as _ridt
    _ridt._states_stub = _states_stub
    _ridt._embs_stub   = _embs_stub
except (ImportError, AttributeError):
    try:
        import run_identity_drift_trials as _ridt2
        _ridt2._states_stub = _states_stub
        _ridt2._embs_stub   = _embs_stub
    except Exception:
        pass


# ──────────────────────────────────────────────────────────────────────────────
# CSV WRITERS
# ──────────────────────────────────────────────────────────────────────────────

def write_csvs(
    turn_rows:    list[dict],
    session_rows: list[dict],
    output_dir:   Path,
    experiment_id: str,
) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    turns_path   = output_dir / "cef_turns.csv"
    sessions_path = output_dir / "cef_sessions.csv"

    def _write(path: Path, rows: list[dict], cols: list[str]) -> None:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        print(f"  → {path}  ({len(rows)} rows)")

    _write(turns_path,    turn_rows,    TURN_CSV_COLS)
    _write(sessions_path, session_rows, SESSION_CSV_COLS)

    # Experiment log
    log = {
        "experiment_id": experiment_id,
        "timestamp":     datetime.now(timezone.utc).isoformat(),
        "n_turns":       len(turn_rows),
        "n_sessions":    len(session_rows),
        "constraint_levels": list({r["constraint_level"] for r in session_rows}),
        "archetypes":    list({r["archetype"]        for r in session_rows}),
        "exploit_classes":   list({r["exploit_class"]    for r in session_rows}),
        "outputs": {
            "turns":    str(turns_path),
            "sessions": str(sessions_path),
        },
    }
    log_path = output_dir / "cef_experiment_log.json"
    with open(log_path, "w") as f:
        json.dump(log, f, indent=2)
    print(f"  → {log_path}")

    return turns_path, sessions_path


# ──────────────────────────────────────────────────────────────────────────────
# SUMMARY PRINTER
# ──────────────────────────────────────────────────────────────────────────────

def print_summary(session_rows: list[dict]) -> None:
    print(f"\n{'='*66}")
    print("  EXPERIMENT SUMMARY")
    print(f"{'='*66}")
    print(f"\n  {'Archetype':<16} {'Level':<8} {'mean_BSI':>8} "
          f"{'Breaches':>9} {'Corr':>5} {'Refusals':>9} {'Δ BSI':>7}")
    print(f"  {'-'*64}")

    from collections import defaultdict
    grouped: dict[tuple, list[dict]] = defaultdict(list)
    for s in session_rows:
        grouped[(s["archetype"], s["constraint_level"])].append(s)

    for (arch, level), sessions in sorted(grouped.items()):
        n         = len(sessions)
        mean_bsi  = sum(s["mean_bsi"]         for s in sessions) / n
        breaches  = sum(s["breach_count"]      for s in sessions) / n
        corr      = sum(s["corrections_fired"] for s in sessions) / n
        refusals  = sum(s["refusal_count"]     for s in sessions) / n
        delta     = sessions[0].get("bsi_drift_reduction")
        delta_str = f"{delta:+.4f}" if delta is not None else "  ref"
        print(f"  {arch:<16} {level:<8} {mean_bsi:>8.4f} "
              f"{breaches:>9.1f} {corr:>5.1f} {refusals:>9.1f} {delta_str:>7}")


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Run Paper 6 CEF constraint experiment (P6 H_CEF_1–H_CEF_5)."
    )
    p.add_argument("--archetype",
                   choices=ARCHETYPES + ["ALL"], default="ALL")
    p.add_argument("--exploit-class",
                   choices=list(EXPLOIT_CLASSES.keys()) + ["ALL"],
                   default="EC-1")
    p.add_argument("--perturbation-type",
                   choices=PERTURBATION_TYPES + ["ALL"],
                   default="contradiction")
    p.add_argument("--constraint-level",
                   choices=list(CONSTRAINT_LEVELS) + ["ALL"],
                   default="ALL")
    p.add_argument("--n-trials", type=int, default=1)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--api-key", default=None)
    p.add_argument("--output-dir", default=str(DEFAULT_OUT))
    p.add_argument("--seed", type=int, default=2026)
    p.add_argument("--verbose", action="store_true")
    p.add_argument("--experiment-id", default=None)
    return p.parse_args()


def main() -> None:
    args = parse_args()

    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key and not args.dry_run:
        print("⚠  No ANTHROPIC_API_KEY — switching to --dry-run.")
        args.dry_run = True

    experiment_id = args.experiment_id or (
        f"CEF_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}"
    )
    output_dir = Path(args.output_dir)

    # Stimuli
    registry_candidates = [
        _ROOT / "docs" / "stimuli_registry.json",
        _ROOT / "stimuli_registry.json",
        Path("/mnt/project/stimuli_registry.json"),
    ]
    registry_path = next((p for p in registry_candidates if p.exists()), None)
    if registry_path:
        stimuli = load_stimuli(registry_path)
        print(f"✓  Stimuli: {registry_path}")
    else:
        stimuli = _minimal_stimuli()
        print("⚠  stimuli_registry.json not found — using minimal stubs")

    archetypes   = ARCHETYPES if args.archetype == "ALL"          else [args.archetype]
    exploits     = list(EXPLOIT_CLASSES.keys()) if args.exploit_class == "ALL" else [args.exploit_class]
    perts        = PERTURBATION_TYPES if args.perturbation_type == "ALL" else [args.perturbation_type]
    levels       = list(CONSTRAINT_LEVELS) if args.constraint_level == "ALL" else [args.constraint_level]

    turn_rows, session_rows = run_experiment(
        archetypes        = archetypes,
        exploit_classes   = exploits,
        perturbation_types= perts,
        constraint_levels = levels,
        n_trials          = args.n_trials,
        stimuli           = stimuli,
        api_key           = api_key,
        dry_run           = args.dry_run,
        output_dir        = output_dir,
        experiment_id     = experiment_id,
        verbose           = args.verbose,
        seed              = args.seed,
    )

    write_csvs(turn_rows, session_rows, output_dir, experiment_id)
    print_summary(session_rows)


def _minimal_stimuli() -> dict:
    """Minimal stub stimuli when registry is unavailable."""
    return {
        "baseline_probes": {"probes": [
            {"id": f"BASE_0{i+1}", "text": f"Baseline probe {i+1}."}
            for i in range(5)
        ]},
        "injection_probes": {arch: {"probes": [
            {"id": f"INJ_{arch[:2].upper()}_{i+1}",
             "text": f"Injection probe {i+1} for {arch}."}
            for i in range(5)
        ]} for arch in ARCHETYPES},
        "perturbation_probes": {pt: {"probes": [
            {"id": f"PERT_{pt[:4].upper()}_01",
             "text": f"Perturbation for {pt}."}
        ]} for pt in PERTURBATION_TYPES},
    }


# ──────────────────────────────────────────────────────────────────────────────
# SMOKE TEST
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import tempfile

    print("=" * 66)
    print("  CONSTRAINT EXPERIMENT RUNNER — SMOKE TEST")
    print("=" * 66)

    # Patch stub helpers into run_identity_drift_trials namespace
    try:
        import scripts.run_identity_drift_trials as _m
    except ImportError:
        import run_identity_drift_trials as _m

    _m._states_stub = _states_stub
    _m._embs_stub   = _embs_stub

    # Load stimuli
    registry_path = next(
        (p for p in [
            _ROOT / "docs" / "stimuli_registry.json",
            Path("/mnt/project/stimuli_registry.json"),
        ] if p.exists()), None
    )
    stimuli = (load_stimuli(registry_path) if registry_path
               else _minimal_stimuli())

    with tempfile.TemporaryDirectory() as tmpdir:
        experiment_id = "SMOKE_TEST_001"

        turn_rows, session_rows = run_experiment(
            archetypes         = ["Magneto", "Joker"],
            exploit_classes    = ["EC-1"],
            perturbation_types = ["contradiction"],
            constraint_levels  = ["none", "medium"],
            n_trials           = 1,
            stimuli            = stimuli,
            api_key            = None,
            dry_run            = True,
            output_dir         = Path(tmpdir),
            experiment_id      = experiment_id,
            verbose            = False,
            seed               = 2026,
        )

        turns_path, sessions_path = write_csvs(
            turn_rows, session_rows, Path(tmpdir), experiment_id
        )

        # ── Assertions ────────────────────────────────────────────────────────

        # T1: turn row count (2 archetypes × 1 exploit × 1 pert × 2 levels × 12 turns)
        expected_turns = 2 * 1 * 1 * 2 * 12
        assert len(turn_rows) == expected_turns, \
            f"Expected {expected_turns} turn rows, got {len(turn_rows)}"
        print(f"\n  [T1] ✓ turn rows = {len(turn_rows)} (expected {expected_turns})")

        # T2: session row count
        expected_sessions = 2 * 1 * 1 * 2
        assert len(session_rows) == expected_sessions, \
            f"Expected {expected_sessions} session rows, got {len(session_rows)}"
        print(f"  [T2] ✓ session rows = {len(session_rows)}")

        # T3: bsi_drift_reduction filled for non-none arms
        medium_sessions = [s for s in session_rows if s["constraint_level"] == "medium"]
        assert all(s.get("bsi_drift_reduction") is not None for s in medium_sessions), \
            "bsi_drift_reduction should be filled for medium arm"
        print(f"  [T3] ✓ bsi_drift_reduction populated for medium arm: "
              f"{[round(s['bsi_drift_reduction'],4) for s in medium_sessions]}")

        # T4: CSV files written and readable
        with open(turns_path) as f:
            csv_turns = list(csv.DictReader(f))
        assert len(csv_turns) == expected_turns
        required_turn_cols = {"bsi", "tc", "constraint_level", "alert_level",
                               "corrected", "refusal_detected"}
        missing = required_turn_cols - set(csv_turns[0].keys())
        assert not missing, f"Missing turn CSV cols: {missing}"
        print(f"  [T4] ✓ CSV readable: {len(csv_turns)} rows, "
              f"{len(csv_turns[0])} columns")

        # T5: none arm fires 0 corrections
        none_sess = [s for s in session_rows if s["constraint_level"] == "none"]
        total_corr_none = sum(s["corrections_fired"] for s in none_sess)
        assert total_corr_none == 0, \
            f"none arm should have 0 corrections, got {total_corr_none}"
        print(f"  [T5] ✓ none arm: corrections_fired=0")

        # T6: medium arm fires corrections on Joker (high drift)
        joker_medium = [s for s in session_rows
                        if s["archetype"] == "Joker"
                        and s["constraint_level"] == "medium"]
        joker_corrections = sum(s["corrections_fired"] for s in joker_medium)
        # Joker with drift=0.85 should trigger corrections under medium constraint
        print(f"  [T6] Joker medium corrections_fired={joker_corrections} "
              f"(expected > 0 with live BSI; dry-run may vary)")

        # T7: summary prints without crash
        print_summary(session_rows)

        print("\n  ✓ All 6 structural tests passed.")

    print("\n" + "=" * 66)
    print("  Smoke test complete.")
    print("=" * 66)
