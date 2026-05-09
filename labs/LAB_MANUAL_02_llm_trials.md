# LAB MANUAL 02 — Running Live LLM Trials (P3 / P5 Data Collection)

**Audience:** Computer Science undergraduate student running P3 and P5 experiments
**Prerequisites:** Manual 01 complete and all four dry-run checks passed
**Estimated time:** Phase 1–2: 2–4 hours. Full matrix: 8–16 hours (can be split across days)
**RACI:** König approves the run plan before Phase 3 or Phase 4 begins
**Series:** MKUltra doctoral research — Paper 3 (H1–H4) and Paper 5 (BSI calibration)

---

## Purpose

This manual runs the LLM trial pipeline against the Anthropic API, captures
raw model responses, computes BSI scores per session, and produces the
`bsi_sessions.csv` that feeds all downstream analysis. The full matrix
(96 sessions) unblocks H1 through H4 in Paper 3 and calibrates the BSI
for Paper 5. All three papers are downstream of this manual.

---

## 1. API Key Setup

1. Export your Anthropic API key. **Never paste it into a file or commit it.**

```bash
export ANTHROPIC_API_KEY=sk-ant-YOUR_KEY_HERE
```

2. Confirm the key is active in the environment.

```bash
echo $ANTHROPIC_API_KEY | head -c 14
# Expected: sk-ant-api03- (first 14 chars only, do not print the full key)
```

3. Confirm `.env` and any files containing the key are in `.gitignore`.

```bash
grep -n "ANTHROPIC" .gitignore
# Expected: at least one line matching — if absent, add: echo ".env" >> .gitignore
```

---

## 2. Understanding the Condition Matrix

The full experiment is a 6 × 4 × 4 factorial design.

**Archetypes (6):**

| # | Archetype | Predicted CEE shape | Hypothesis role |
|---|-----------|-------------------|-----------------|
| 1 | Joker | Chaotic, high impulsivity | H1 primary contrast |
| 2 | Magneto | Grievance-driven, organized defiance | H1 primary contrast |
| 3 | Batman | Rigid constraint, high self-control | H4 recovery condition |
| 4 | Harley Quinn | Abandonment-driven, labile | H2 ANOVA |
| 5 | Lex Luthor | Instrumental, hyperlogical | H2 ANOVA |
| 6 | Two-Face | Bimodal, split constraint | H3 interaction |

**Exploit classes (4):**

| Class | Mechanism | Human SE analog |
|-------|-----------|-----------------|
| CTL | No injection (baseline control) | No manipulation |
| EC-1 | Authority override persona injection | Authority/pretexting |
| EC-2+EC-1 | Compound: authority + consistency lock-in | Milgram gradient |
| EC-4 | Escalating perturbation sequence | Commitment ratchet |

**Perturbation types (4):**

| Type | What it does |
|------|-------------|
| contradiction | Presents a direct contradiction to the persona's stated position |
| authority | Introduces a higher authority claim to override the persona |
| consistency | Invokes the persona's prior statements against itself |
| escalation | Progressively increases constraint pressure across turns |

**Full matrix = 6 × 4 × 4 = 96 sessions.**
Each session runs 12 turns with approximately 14 API calls.
At current Anthropic pricing, budget approximately $0.50–$1.50 per session
depending on response length. Estimate total cost before Phase 4.

---

## 3. Recommended Execution Sequence

**Always run phases in order. Do not jump to Phase 3 or 4 without König approval.**

### Before Any Live Run: Single Session Smoke Test

Run one live session and inspect it before running batches.

```bash
python run_identity_drift_trials.py \
  --archetype Joker \
  --exploit-class EC-1 \
  --perturbation-type contradiction \
  --n-trials 1
```

Inspect the raw output:

```bash
ls data/raw/
# You will see one directory named with a session UUID
ls data/raw/<SESSION_UUID>/
# Expected: responses.jsonl
head -5 data/raw/<SESSION_UUID>/responses.jsonl
```

Verify the JSONL is valid and contains model responses. If this step fails,
stop and report to König before continuing.

---

### Phase 1 — CTL Baseline (BSI Calibration)

This establishes the unconditioned baseline BSI for β_BSI calibration
(per P5 S5). Run this first. It produces `data/bsi_sessions/ctl_baseline_scores.json`.

```bash
python run_identity_drift_trials.py --ctl-baseline --archetype ALL
```

**Approximate calls:** 6 archetypes × 4 perturbation types × 14 calls = ~336 API calls.

Verify on completion:

```bash
ls data/bsi_sessions/ctl_baseline_scores.json
# Expected: exists
cat data/bsi_sessions/ctl_baseline_scores.json
# Expected: JSON with "bsi_scores" array (24 values) and "n": 24
```

---

### Phase 2 — Primary Contrast Pair (H1)

H1 predicts Magneto will show significantly lower BSI (more constraint-resistant)
than Joker under EC-1. This phase runs the minimum needed to test H1.

```bash
python run_identity_drift_trials.py \
  --archetype Magneto \
  --exploit-class EC-1 \
  --perturbation-type ALL

python run_identity_drift_trials.py \
  --archetype Joker \
  --exploit-class EC-1 \
  --perturbation-type ALL
```

Run Magneto first. Inspect before running Joker.

**Approximate calls per archetype:** 4 perturbation types × 14 calls = ~56 calls.
**Phase 2 total:** ~112 API calls.

---

### Phase 3 — Full 6-Archetype EC-1 Set (H2)

H2 tests BSI differences across all six archetypes under EC-1 (ANOVA).
Requires König sign-off before running.

```bash
python run_identity_drift_trials.py \
  --archetype ALL \
  --exploit-class EC-1
```

Note: This replaces the Phase 2 Magneto and Joker sessions with fresh runs.
If you ran Phase 2 separately, you can pass individual archetypes to avoid
re-running completed conditions:

```bash
# Run only the four remaining archetypes
for ARCH in Batman "Harley Quinn" "Lex Luthor" "Two-Face"; do
  python run_identity_drift_trials.py \
    --archetype "$ARCH" \
    --exploit-class EC-1 \
    --perturbation-type ALL
done
```

**Phase 3 total:** ~336 API calls (6 archetypes × 4 perturbation × ~14 calls).

---

### Phase 4 — Full Matrix (H3 + H4, König Approval Required)

H3 tests exploit class × archetype interaction. H4 tests Batman recovery.
This phase runs all remaining exploit class conditions.

```bash
python run_identity_drift_trials.py --full-matrix
```

**Full matrix total:** ~1,344 API calls (96 sessions × ~14 calls).
This may take 8–16 hours. It can be interrupted and resumed — see Section 7.

---

## 4. Cost and Time Estimates

| Phase | Sessions | Approx. API calls | Approx. cost (USD) | Approx. time |
|-------|---------|-------------------|--------------------|-------------|
| Smoke test | 1 | 14 | < $0.05 | 5 min |
| Phase 1 (CTL) | 24 | 336 | $1–4 | 1–2 hr |
| Phase 2 (H1) | 8 | 112 | $0.50–1.50 | 30–60 min |
| Phase 3 (H2) | 24 | 336 | $1–4 | 1–2 hr |
| Phase 4 (full matrix) | 96 | ~1,344 | $5–20 | 8–16 hr |

These are estimates. Actual cost depends on response length. Check your
Anthropic usage dashboard after each phase.

---

## 5. Raw Output: What Is in `responses.jsonl`

Each line in `responses.jsonl` is one API call, encoded as JSON. Key fields:

```json
{
  "session_id": "UUID",
  "turn": 3,
  "archetype": "Magneto",
  "exploit_class": "EC-1",
  "perturbation_type": "contradiction",
  "prompt": "...",
  "response": "...",
  "timestamp": "2026-05-09T14:23:00Z"
}
```

Do not edit these files. They are the raw record of what the model said.

---

## 6. BSI CSV: Column Definitions

`data/bsi_sessions/bsi_sessions.csv` has one row per session. Key columns
(per P5 S4 §4.5.3 schema):

| Column | Type | Description |
|--------|------|-------------|
| `bsi` | float | Behavioral Stability Index (0–1; lower = more drift) |
| `bsi_norm` | float | BSI normalized against CTL baseline |
| `bsi_breach` | bool | True if BSI below breach threshold |
| `tc` | float | Trait Coherence score |
| `sd_inv` | float | Semantic Distance inverse |
| `acg` | float | Authority Compliance Gradient mean |
| `breach_rate` | float | Proportion of turns in breach |
| `severity_weight` | float | Breach severity composite |
| `mean_resilience` | float | Mean resilience across turns |
| `bimodal_detected` | bool | Two-Face bimodal pattern flag |
| `archetype` | str | Archetype condition |
| `exploit_class` | str | EC-1, EC-2+EC-1, EC-4, or CTL |
| `perturbation_type` | str | contradiction, authority, consistency, or escalation |
| `session_id` | str | UUID matching `data/raw/` directory name |
| `timestamp` | str | ISO 8601 session start time |

---

## 7. Resuming Interrupted Runs

If a run is interrupted, it can be resumed by re-running the same command.
Sessions already in `bsi_sessions.csv` are not duplicated — check the row count:

```bash
wc -l data/bsi_sessions/bsi_sessions.csv
```

To find which conditions are missing, compare against the expected condition list:

```bash
python -c "
import pandas as pd
df = pd.read_csv('data/bsi_sessions/bsi_sessions.csv')
print(df.groupby(['archetype','exploit_class','perturbation_type']).size())
"
```

Each condition should appear exactly once. Any missing condition can be
re-run by passing the specific `--archetype`, `--exploit-class`, and
`--perturbation-type` flags.

---

## 8. Verifying Data Quality Before Analysis

Run these checks after each phase before proceeding:

**Check 1: Row count**

```bash
wc -l data/bsi_sessions/bsi_sessions.csv
# Phase 1: 25 (24 CTL sessions + header)
# After Phase 3: 49 (24 EC-1 + 24 CTL + header)
# Full matrix: 97 (96 + header)
```

**Check 2: No null BSI values**

```bash
python -c "
import pandas as pd
df = pd.read_csv('data/bsi_sessions/bsi_sessions.csv')
nulls = df['bsi'].isna().sum()
print(f'Null BSI values: {nulls}')
assert nulls == 0, 'NULL BSI FOUND — investigate raw session files'
print('BSI completeness: OK')
"
```

**Check 3: BSI range sanity**

```bash
python -c "
import pandas as pd
df = pd.read_csv('data/bsi_sessions/bsi_sessions.csv')
print(df['bsi'].describe())
assert df['bsi'].between(0,1).all(), 'BSI out of [0,1] range'
print('BSI range: OK')
"
```

**Check 4: Schema columns present**

```bash
python -c "
import pandas as pd
REQUIRED = ['bsi','bsi_norm','bsi_breach','tc','sd_inv','acg',
            'archetype','exploit_class','perturbation_type','session_id']
df = pd.read_csv('data/bsi_sessions/bsi_sessions.csv')
missing = [c for c in REQUIRED if c not in df.columns]
print(f'Missing columns: {missing}')
assert not missing, 'Schema mismatch — check run_identity_drift_trials.py version'
print('Schema: OK')
"
```

---

## 9. Red Flags — When to Stop and Report

Stop the run and contact König if any of the following appear:

- More than 10% of sessions show `bsi_breach = True` in a CTL condition
  (CTL baseline should be near-zero breach rate)
- Any session produces an empty `responses.jsonl`
- Any session produces fewer than 10 turns in `responses.jsonl`
  (each session should produce 12 turns)
- The Anthropic API returns repeated `overloaded_error` responses
  (rate limiting — add `--quiet` flag and space out runs)
- `bsi` values clustering at exactly 0.0 or 1.0 across many sessions
  (indicates a scoring failure, not a real result)
- Any Python traceback during a live (non-dry-run) session

---

## 10. What Success Looks Like

After the full matrix run (Phase 4), all of the following are true:

```bash
wc -l data/bsi_sessions/bsi_sessions.csv
# 97 lines

ls data/bsi_sessions/ctl_baseline_scores.json
# File exists

ls data/raw/ | wc -l
# 96 session directories (plus any smoke-test session from step 3)
```

Run the analysis pipeline to confirm the BSI CSV is analysis-ready:

```bash
cd scripts/
python bsi_stats_pipeline.py
```

The pipeline should print the `HYPOTHESIS OUTCOME REGISTER` with real
(not synthetic) results for H1 through H4.

The CSV is now ready for IRR coding (Manual 03) and for Paper 3 analysis.

---

*Manual version: 1.0 — 2026-05-09*
*Prepared by: Rat Dev Claude (Assembler Node)*
*RACI: König approves Phase 3 and Phase 4 run plans before execution*
*Previous: LAB_MANUAL_01_setup.md | Next: LAB_MANUAL_03_irr_coding.md*
