# MASTER PIPELINE RUNBOOK — MKUltra Data Collection
# File: labs/MASTER_PIPELINE_RUNBOOK.md
# Version: 1.0 — 2026-05-09
# Audience: All operators + König
# Purpose: Single navigation layer above the three individual manuals.
#          Track state, find the right document, know what's next.
# RACI: König reviews; operators update pipeline_state.json as phases complete
# ─────────────────────────────────────────────────────────────────────────────

## 0. What This Document Is

This is not the manual. The manuals are LAB_MANUAL_01, 02, and 03.

This document is the **cockpit view**: where are we in the pipeline right now,
what does the current data inventory look like, what decision gate comes next,
and where does the operator go for detailed instructions.

Read this first. Then go to the relevant manual.

---

## 1. Phase Completion Tracker

Update this table as phases complete. Do not mark COMPLETE until the
verification check for that phase passes.

| Phase | Description | Status | Sessions | Date | König approval |
|-------|-------------|--------|---------|------|---------------|
| 0 | Environment setup + dry-run verification | `NOT_STARTED` | — | — | Required before Phase 1 |
| 1 | CTL baseline sessions | `NOT_STARTED` | 0 / 24 | — | — |
| 2 | H1 contrast pair (Magneto + Joker, EC-1) | `NOT_STARTED` | 0 / 8 | — | — |
| 3 | Full 6-archetype EC-1 set | `NOT_STARTED` | 0 / 24 | — | **König approves** |
| 4 | Full 96-session matrix | `NOT_STARTED` | 0 / 96 | — | **König approves** |
| 5 | IRR subsample coding (κ check) | `NOT_STARTED` | 0 / 120 responses | — | **König approves κ** |
| 6 | Full session coding | `NOT_STARTED` | 0 / ~1152 responses | — | **König approves** |

**Status values:** `NOT_STARTED` → `IN_PROGRESS` → `COMPLETE` → `BLOCKED`

---

## 2. Current Data Inventory

Run this command block to check what data currently exists.
Run it at the start of each session and after each phase.

```bash
# From repo root
echo "=== PHASE 0: Synthetic data ==="
ls data/synthetic/sap_synthetic_output.csv 2>/dev/null && echo "EXISTS" || echo "MISSING"

echo "=== PHASE 1-4: BSI sessions ==="
if [ -f data/bsi_sessions/bsi_sessions.csv ]; then
  echo "bsi_sessions.csv: $(wc -l < data/bsi_sessions/bsi_sessions.csv) rows (expected 97 for full matrix)"
else
  echo "bsi_sessions.csv: MISSING"
fi

echo "=== CTL baseline ==="
ls data/bsi_sessions/ctl_baseline_scores.json 2>/dev/null && echo "EXISTS" || echo "MISSING"

echo "=== Raw sessions ==="
echo "Session directories: $(ls data/raw/ 2>/dev/null | wc -l)"

echo "=== PHASE 5: IRR subsample ==="
ls data/coding/irr_subsample.csv 2>/dev/null && echo "EXISTS" || echo "MISSING"
ls data/coding/irr_results.csv 2>/dev/null && cat data/coding/irr_results.csv | grep OVERALL || echo "irr_results.csv: MISSING"

echo "=== PHASE 6: Full coding ==="
ls data/coding/coded_output_final.csv 2>/dev/null && \
  echo "coded_output_final.csv: $(wc -l < data/coding/coded_output_final.csv) rows" || \
  echo "coded_output_final.csv: MISSING"
```

---

## 3. Decision Gates — What König Must Approve

The following actions require explicit König approval before proceeding.
"Explicit" means König says "proceed" — not silence or assumption.

| Gate | What it protects | Consequence of skipping |
|------|-----------------|------------------------|
| Phase 3 run plan | API budget, condition prioritization | Wasted API spend; possible unbalanced data |
| Phase 4 run plan | Full matrix budget (~$5–20) | Cannot be undone once run |
| IRR κ results | Coding quality standard | Invalid data if coding proceeds with low κ |
| Rubric revision (if κ < 0.80) | Operationalization integrity | Changing the rubric mid-study contaminates IRR |
| Full coding start | All of the above | Cannot be re-coded if definitions shift afterward |

**Protocol:** Send König the relevant verification output (CSV, κ report,
session count) and wait for written confirmation before proceeding.

---

## 4. Escalation Paths

| Situation | Contact | What to send |
|---|---|---|
| Script crash — unknown error | König | Full traceback + current data inventory output |
| API error — persistent after retry | König | Error type, session count, time of failure |
| κ below 0.80 | König | `irr_results.csv` + list of low-κ dimensions |
| Session count mismatch | König | Current vs. expected count + condition coverage output |
| Any ALARM flag in coded data | König | Session ID + ALARM description from notes column |
| Uncertainty about any decision | König | Description of what you know and what you don't |

**Do not send König:** general progress updates unless requested.
**Do send König:** anything that requires a decision before you can continue.

---

## 5. Quick Navigation to Individual Manuals

| You need to... | Go to |
|---|---|
| Set up environment from scratch | `labs/LAB_MANUAL_01_setup.md` |
| Run the dry-run verification | `labs/LAB_MANUAL_01_setup.md §4` |
| Set up API key and run live sessions | `labs/LAB_MANUAL_02_llm_trials.md §1` |
| Understand the condition matrix | `labs/LAB_MANUAL_02_llm_trials.md §2` |
| Resume interrupted runs | `labs/LAB_MANUAL_02_llm_trials.md §7` |
| Check data quality | `labs/LAB_MANUAL_02_llm_trials.md §8` |
| Generate IRR subsample | `labs/LAB_MANUAL_03_irr_coding.md §2` |
| Understand coding procedure | `labs/LAB_MANUAL_03_irr_coding.md §4` |
| Run κ computation | `labs/LAB_MANUAL_03_irr_coding.md §5` |
| Handle a script crash | `labs/OPERATOR_QUICKREF.md §1` |
| Handle an API error | `labs/OPERATOR_QUICKREF.md §2` |
| Handle low κ | `labs/OPERATOR_QUICKREF.md §3` |
| Calibrate before coding | `labs/IRR_PRACTICE_SET.md` |
| Understand a trait dimension | `labs/data_dictionary.md` |
| Find IRR anchor examples | `labs/data_dictionary_expansion_v1_1.md §2` |

---

## 6. Pipeline Health Check

Run this single command block at the start of any session to confirm
the environment is still working correctly.

```bash
cd scripts/

echo "=== HEALTH CHECK ==="

echo "--- Python version ---"
python3 --version

echo "--- Required packages ---"
python3 -c "import anthropic, sentence_transformers, pingouin, statsmodels, scipy, pandas; print('All packages: OK')"

echo "--- SAP validation (synthetic, ~30 seconds) ---"
python3 sap_pipeline_validation.py 2>&1 | tail -3

echo "--- Dry run single session (synthetic, ~10 seconds) ---"
python3 run_identity_drift_trials.py --dry-run --archetype Joker --n-trials 1 --quiet 2>&1 | tail -3

echo "=== HEALTH CHECK COMPLETE ==="
```

**Expected output (all lines):**
```
Python 3.11.x
All packages: OK
All checks passed. SAP pipeline is fully traceable.
[BSI line with numeric values and no Python traceback]
HEALTH CHECK COMPLETE
```

If any line differs from expected: stop, run the relevant manual section,
or consult `labs/OPERATOR_QUICKREF.md`.

---

## 7. `pipeline_state.json` — Machine-Readable State

Maintain this file in the repo root. Update it when phases complete.
This is the persistent record of pipeline state across sessions and operators.

**Schema:**
```json
{
  "_doc": "MKUltra pipeline state — update as phases complete",
  "last_updated": "YYYY-MM-DDTHH:MM:SS",
  "operator": "your name",
  "phases": {
    "phase_0_env": {
      "status": "NOT_STARTED",
      "date_completed": "",
      "notes": ""
    },
    "phase_1_ctl": {
      "status": "NOT_STARTED",
      "sessions_completed": 0,
      "sessions_expected": 24,
      "date_completed": "",
      "notes": ""
    },
    "phase_2_h1": {
      "status": "NOT_STARTED",
      "sessions_completed": 0,
      "sessions_expected": 8,
      "date_completed": "",
      "notes": ""
    },
    "phase_3_h2": {
      "status": "NOT_STARTED",
      "sessions_completed": 0,
      "sessions_expected": 24,
      "konig_approved": false,
      "date_completed": "",
      "notes": ""
    },
    "phase_4_full": {
      "status": "NOT_STARTED",
      "sessions_completed": 0,
      "sessions_expected": 96,
      "konig_approved": false,
      "date_completed": "",
      "notes": ""
    },
    "phase_5_irr": {
      "status": "NOT_STARTED",
      "responses_coded": 0,
      "responses_expected": 120,
      "kappa_overall": null,
      "kappa_passed": null,
      "konig_approved": false,
      "date_completed": "",
      "notes": ""
    },
    "phase_6_coding": {
      "status": "NOT_STARTED",
      "responses_coded": 0,
      "konig_approved": false,
      "date_completed": "",
      "notes": ""
    }
  },
  "konig_approvals": {
    "phase_3_run_approved": false,
    "phase_3_approval_date": "",
    "phase_4_run_approved": false,
    "phase_4_approval_date": "",
    "irr_results_approved": false,
    "irr_approval_date": "",
    "full_coding_approved": false,
    "full_coding_approval_date": ""
  },
  "red_flags": [],
  "alarm_flags": []
}
```

**To update after Phase 1 completes (example):**
```bash
# Edit pipeline_state.json, change:
#   "phase_1_ctl": { "status": "COMPLETE", "sessions_completed": 24, "date_completed": "2026-05-10" }
```

Do not automate this file. Update it manually so each update is a deliberate
human decision, not a side effect of a script run.

---

## 8. Document Inventory

All operational documents for the pipeline, in priority order:

| Document | Location | Purpose |
|---|---|---|
| This file | `labs/MASTER_PIPELINE_RUNBOOK.md` | Navigation + state tracking |
| Setup manual | `labs/LAB_MANUAL_01_setup.md` | Environment + dry-run verification |
| LLM trials manual | `labs/LAB_MANUAL_02_llm_trials.md` | Live data collection |
| IRR coding manual | `labs/LAB_MANUAL_03_irr_coding.md` | Coding + reliability |
| Operator quick ref | `labs/OPERATOR_QUICKREF.md` | Failure recovery |
| IRR practice set | `labs/IRR_PRACTICE_SET.md` | Rater calibration warm-up |
| Rater CSV template | `labs/rater_coding_template.csv` | Coding sheet template |
| Data dictionary | `labs/data_dictionary.md` | Trait definitions + rubric |
| Dict expansion | `labs/data_dictionary_expansion_v1_1.md` | Missing entries + IRR anchors |
| SAP | `labs/Statistical_Analysis_Plan_v1_2.md` | Pre-registered analysis plan |
| Stimuli registry | `labs/stimuli_registry.json` | Pre-registered stimuli |
| Pipeline state | `pipeline_state.json` (repo root) | Machine-readable state tracker |

---

*Master Pipeline Runbook version: 1.0 — 2026-05-09*
*Prepared by: Rat Dev Claude (Assembler Node)*
*Source: Rat Dev ChatGPT Lab Manual Audit recommendation*
*RACI: König reviews; König is the approving authority for all decision gates*
