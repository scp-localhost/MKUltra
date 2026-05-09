# MKUltra Series — Master Runbook Index
# Empirical Pipeline Documentation for Data Collectors

**Series:** MKUltra — LLM Behavioral Drift Under Persona Injection
**Author/PI:** Stephen Pote (König)
**Node:** Rat Dev Claude (Assembler)
**Date:** 2026-05-09
**RACI:** König reviews and approves all manuals before operational use

---

## Who This Document Is For

A Computer Science undergraduate student who has been assigned to collect
data for the MKUltra doctoral research series. You do not need to have read
the seven papers. You need Python 3.11, git, and an Anthropic API key.

Start here. This document tells you which manual to read and in what order.

---

## The Three Manuals

| Manual | Filename | What You Do | Time |
|--------|----------|-------------|------|
| 01 | `LAB_MANUAL_01_setup.md` | Install dependencies, run dry-run verification | 45–90 min |
| 02 | `LAB_MANUAL_02_llm_trials.md` | Run live LLM experiment sessions against the API | 2–16 hrs |
| 03 | `LAB_MANUAL_03_irr_coding.md` | Score a subsample of responses for inter-rater reliability | 3–6 hrs |

**Read them in order. Do not start Manual 02 until Manual 01 passes all checks.
Do not start full coding in Manual 03 until König approves your IRR results.**

---

## Empirical Phase Map

This table shows what research output each phase produces and which papers it unblocks.

| Phase | Activity | Manual | Data produced | Unblocks |
|-------|----------|--------|--------------|----------|
| 0 | Environment setup + dry-run verification | 01 | Synthetic CSVs only | Phase 1 |
| 1 | CTL baseline sessions | 02 §Phase 1 | `ctl_baseline_scores.json` | BSI calibration (P5) |
| 2 | H1 primary contrast (Magneto vs Joker, EC-1) | 02 §Phase 2 | BSI rows for 8 sessions | H1 test (P3) |
| 3 | Full 6-archetype EC-1 set | 02 §Phase 3 | BSI rows for 24 sessions | H2 ANOVA (P3) |
| 4 | Full 96-session matrix | 02 §Phase 4 | Complete `bsi_sessions.csv` | H3 + H4 (P3), P5 S5 |
| 5 | IRR subsample coding (κ check) | 03 §1–6 | `irr_results.csv` | All coded output |
| 6 | Full session coding | 03 §7 | `coded_output_final.csv` | P3 Results §3.2 |

---

## Key File Locations

All paths are relative to the repo root.

| File | Created when | Used by |
|------|-------------|---------|
| `data/synthetic/sap_synthetic_output.csv` | Manual 01 step 4.1 | Pipeline validation |
| `data/raw/<session_id>/responses.jsonl` | Manual 02 each session | IRR coding |
| `data/bsi_sessions/bsi_sessions.csv` | Manual 02 each session | `bsi_stats_pipeline.py`, P3 analysis |
| `data/bsi_sessions/ctl_baseline_scores.json` | Manual 02 Phase 1 | BSI calibration (P5) |
| `data/coding/irr_subsample.csv` | Manual 03 step 2 | Both raters |
| `data/coding/rater1_subsample.csv` | Manual 03 §4 | IRR computation |
| `data/coding/rater2_subsample.csv` | Manual 03 §4 | IRR computation |
| `data/coding/irr_results.csv` | Manual 03 step 5 | König review |
| `data/coding/coded_output_final.csv` | Manual 03 §7 | P3 drift analysis |
| `data/analysis/*.csv` | `bsi_stats_pipeline.py` | H1–H4 results |

---

## Scripts Reference

All scripts live in `scripts/`. Run from inside that directory.

| Script | What it does | When to run |
|--------|-------------|-------------|
| `sap_pipeline_validation.py` | Self-tests the full analysis pipeline | Manual 01 step 4.1 |
| `run_identity_drift_trials.py` | Runs LLM sessions (dry or live) | Manual 01 steps 4.2–4.3; Manual 02 all phases |
| `bsi_stats_pipeline.py` | Computes H1–H4 statistical tests | After each Manual 02 phase; final analysis |
| `parallel_failure_coder.py` | Generates IRR subsample; computes κ | Manual 03 |
| `trait_drift_analysis.py` | Drift computation (called by other scripts) | Not called directly |
| `behavioral_stability_index.py` | BSI computation (called by other scripts) | Not called directly |
| `injection_experiment_protocol.py` | P3 protocol runner (alternative to `run_identity_drift_trials.py`) | Per König instruction |
| `forensic_archetype.py` | Archetype persona generation (called by session scripts) | Not called directly |

---

## RACI Summary

| Decision | Who decides |
|----------|------------|
| Approve Manual 01 verification results | König |
| Approve Phase 3 and Phase 4 run plans | König |
| Approve IRR rubric revisions | König |
| Approve IRR κ results before full coding | König |
| Approve coded output for analysis | König |

When in doubt: stop, document what you observed, and ask König.

---

## What "Do Not Modify" Means

You are a data collector, not an author. The following are read-only:

- `drafts/` — paper manuscripts in progress
- `seeds/` — assembly notes
- `docs/Statistical_Analysis_Plan_v1_2.md` — the pre-registered analysis plan
- `docs/stimuli_registry.json` — the pre-registered stimulus set
- Any script in `scripts/` — report bugs, do not fix them yourself

The only files you write to are:
- `data/` (produced by scripts automatically)
- `data/coding/rater1_subsample.csv` or `rater2_subsample.csv` (your coding)

---

*Runbook version: 1.0 — 2026-05-09*
*Prepared by: Rat Dev Claude (Assembler Node)*
*Series authority: Stephen Pote (Mause König)*
