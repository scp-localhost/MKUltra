# LAB MANUAL 01 — Environment Setup and Pipeline Verification

**Audience:** Computer Science undergraduate student, Day 0
**Prerequisites:** Python 3.11+, git, pip, a terminal, and an Anthropic API key (for live runs only)
**Estimated time:** 45–90 minutes
**RACI:** König reviews and approves before operational use
**Series:** MKUltra doctoral research — LLM behavioral drift under persona injection

---

## Purpose

This manual gets the repository running and verifies the full data pipeline
on synthetic (zero-cost) data before any API key is used. When you finish,
every script will have executed successfully and you will know the output
locations. Nothing in this manual touches the Anthropic API.

---

## 1. Prerequisites Checklist

Before starting, confirm each item:

1. Python 3.11 or higher is installed.

```bash
python3 --version
# Expected: Python 3.11.x or higher
```

2. pip is installed and up to date.

```bash
pip --version
pip install --upgrade pip --break-system-packages
```

3. git is installed.

```bash
git --version
```

4. You have a terminal with write access to your home directory.

5. You have an Anthropic API key (format: `sk-ant-...`). **Do not use it yet.**
   You will need it for Manual 02 only. Keep it somewhere safe but do not
   paste it into any file in the repo.


---

## 2. Clone the Repository and Orient Yourself

1. Clone the repo. Run this from your home directory or wherever you keep
   project folders.

```bash
git clone https://github.com/scp-localhost/MKUltra.git MKUltra
cd MKUltra
```

Confirm you are now inside the repo root:

```bash
pwd
# Expected: something ending in /MKUltra
ls
# Confirm you can see: scripts/  docs/  labs/  README.md
```

> **Note for Claude.ai / network-restricted environments:** The egress proxy
> in Claude.ai blocks outbound connections to GitHub. If you are running this
> manual inside a Claude.ai session rather than on your own machine, you cannot
> `git clone`. In that case, König will provide the scripts directory as file
> uploads. On your own machine (Ubuntu, macOS, Windows WSL), the clone command
> above works normally.

2. Review the directory structure. After cloning you should see:

```
MKUltra/
├── analysis/         # Generated analysis outputs — do not commit
├── artifacts/        # Reference PDFs and images — read-only
├── cleanup.sh        # Repo maintenance script — do not run
├── data/             # Generated at runtime — do not commit
│   ├── raw/          # Per-session response JSONLs
│   ├── bsi_sessions/ # BSI aggregate CSV
│   ├── synthetic/    # Dry-run output
│   └── analysis/     # Statistical output
├── docs/             # Stimuli registry, data dictionary, SAP
├── drafts/           # Paper drafts — read-only for data collectors
├── init_repo.sh      # Git setup script — do not run
├── labs/             # Lab manuals and operator documentation ← you are here
├── LICENCE.md
├── README.md
├── scripts/          # All experiment scripts — the engine room
└── seeds/            # Assembly notes — read-only for data collectors
```

**The `data/` subdirectories do not exist yet** — they are created automatically
when scripts run. The tree above shows what you will see after completing §4,
not immediately after cloning.

**You will work in `scripts/` and read from `labs/` and `docs/`.
You write nothing to `drafts/`, `seeds/`, or `artifacts/`.**

---

## 3. Install Dependencies

Run this single command from the repo root. All packages are required.

```bash
pip install anthropic sentence-transformers pingouin statsmodels scipy pandas --break-system-packages
```

Expected: each package installs or reports "already satisfied." If any fail,
check your Python version and pip access, then retry.

---

## 4. Verification Sequence

Run all four checks in order. All must pass before you proceed to Manual 02.
A single failure here means your environment is not ready.

### 4.1 SAP Pipeline Validation

This script self-tests the entire statistical analysis pipeline
against a known synthetic dataset.

```bash
cd scripts/
python sap_pipeline_validation.py
```

**Expected output (last lines):**

```
All checks passed. SAP pipeline is fully traceable.
Output: data/synthetic/sap_synthetic_output.csv
```

If you see `All checks passed`, move to 4.2.
If you see any `FAIL` or `ERROR`, see Section 6 (Troubleshooting).

**What it produced:**
- `data/synthetic/sap_synthetic_output.csv` — synthetic BSI-format data
  used as the input for step 4.4.

---

### 4.2 Single Dry-Run Session

This runs one synthetic session for the Joker archetype with no API call.

```bash
python run_identity_drift_trials.py --dry-run --archetype Joker
```

**Expected output (abbreviated):**

```
============================================================
  TRIAL RUN — Paper 5 Identity Drift Experiments
============================================================
  Archetypes:    ['Joker']
  Exploit class: ['EC-1']
  Perturbation:  ['contradiction']
  Trials/cond:   1
  Total sessions:1
  Mode:          DRY RUN (synthetic)
  ...
  → BSI=0.XXXX  TC=0.XXXX  SD_inv=0.XXXX  ACG=X.XX  breach=True/False
```

The exact BSI number will vary; what matters is that you see a BSI value
printed with no Python traceback. The session output also appears in
`data/raw/` as a directory named with the session ID.

---

### 4.3 Full Matrix Dry Run

This runs all 96 sessions synthetically. Takes approximately 2–5 minutes.

```bash
python run_identity_drift_trials.py --dry-run --full-matrix
```

**Expected output (summary table at end):**

```
================================================================
  SUMMARY — 96 sessions complete
================================================================
  Archetype        Exploit      BSI_mean  Breaches
  ────────────────────────────────────────────────────
  Batman           CTL          0.XXXX    X/X
  Batman           EC-1         0.XXXX    X/X
  ...
  Two-Face         EC-4         0.XXXX    X/X

  Mode B unblock: bsi_stats_pipeline.py can now load
  data/bsi_sessions/bsi_sessions.csv
================================================================
```

Verify:
- Summary shows 96 sessions (6 archetypes × 4 exploit classes × 4 perturbation types)
- `data/bsi_sessions/bsi_sessions.csv` exists and is non-empty

```bash
wc -l data/bsi_sessions/bsi_sessions.csv
# Expected: 97 lines (1 header + 96 data rows)
```

---

### 4.4 Statistical Analysis Pipeline

This runs the hypothesis tests against the synthetic data produced in step 4.3.

```bash
python bsi_stats_pipeline.py --sap ../data/synthetic/sap_synthetic_output.csv
```

**Expected output (abbreviated):**

```
================================================================
  MODE A — SAP SYNTHETIC ANALYSES
================================================================
  ...
  H_drift: [result line]
  H_constraint: [result line]
  ...
================================================================
  HYPOTHESIS OUTCOME REGISTER
================================================================
  H_drift        | p=X.XXXX | η²=X.XXXX | SUPPORTED/NOT SUPPORTED
  H_constraint   | p=X.XXXX | η²=X.XXXX | SUPPORTED/NOT SUPPORTED
  ...
```

Verify that the pipeline reaches the `HYPOTHESIS OUTCOME REGISTER` section
without errors. The supported/not-supported verdict on synthetic data does not
matter — what matters is that the pipeline runs end-to-end.

The analysis CSVs are written to `data/analysis/`.

---

## 5. What Success Looks Like

When the environment is correctly set up, all four of these files exist:

```bash
ls data/synthetic/sap_synthetic_output.csv   # Step 4.1
ls data/raw/                                  # Step 4.2 — one session directory
ls data/bsi_sessions/bsi_sessions.csv        # Step 4.3 — 96 rows
ls data/analysis/                            # Step 4.4 — hypothesis CSVs
```

All four checks passed cleanly with no Python tracebacks. You are ready
for Manual 02.

---

## 6. Troubleshooting

**`ModuleNotFoundError: No module named 'anthropic'` (or any other module)**

Re-run the install command with `--break-system-packages`:

```bash
pip install anthropic sentence-transformers pingouin statsmodels scipy pandas --break-system-packages
```

If you are in a virtual environment, omit `--break-system-packages`.

---

**`stimuli_registry.json not found — using minimal stub prompts`**

This warning is expected. The dry-run uses built-in stubs and will still pass
all checks. If `docs/stimuli_registry.json` is present in the repo, the script
will find it automatically. The warning can be safely ignored during dry-run.

---

**`FileNotFoundError` for any data path**

The `data/` directory is created at runtime. Run the steps in order —
step 4.3 creates `bsi_sessions.csv`, which step 4.4 reads.

---

**`AssertionError` in `sap_pipeline_validation.py`**

A specific validation check failed. Read the error message — it will name
the failing test (T1 through T8). Report the full error output to König.

---

**`ANTHROPIC_API_KEY` errors during dry-run**

You should never need your API key for this manual. If the script asks for
one, confirm you are passing `--dry-run`. If the error persists, report to König.

---

## 7. Data Outputs Reference

| File | Created by | Contents |
|------|-----------|----------|
| `data/synthetic/sap_synthetic_output.csv` | `sap_pipeline_validation.py` | Synthetic SAP-format data; Mode A input |
| `data/raw/<session_id>/` | `run_identity_drift_trials.py` | Per-session response JSONLs |
| `data/bsi_sessions/bsi_sessions.csv` | `run_identity_drift_trials.py` | 96-row BSI aggregate; Mode B input |
| `data/analysis/*.csv` | `bsi_stats_pipeline.py` | Hypothesis test results |
| `data/analysis/anova/H_archetype_tukey.csv` | `bsi_stats_pipeline.py` | Tukey pairwise comparisons |

**Do not delete or modify any file in `data/`.** It is gitignored. Treat it as
append-only during data collection.

---

*Manual version: 1.1 — 2026-05-09*
*Prepared by: Rat Dev Claude (Assembler Node)*
*Patch: §2 — MKUltra naming unified, directory tree corrected, data/ creation note added, stimuli path fixed*
*RACI: König reviews and approves before operational use*
*Next: LAB_MANUAL_02_llm_trials.md*
