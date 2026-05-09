# MKUltra Lab Manual — Audit Response & Enhancement Plan
# Document: LAB_MANUAL_AUDIT_RESPONSE.md
# Author: Rat Dev Claude (Assembler Node)
# Date: 2026-05-09
# Source audit: Rat Dev ChatGPT Lab Manual Audit (Project Knowledge)
# RACI: König reviews and approves before task execution begins
# ─────────────────────────────────────────────────────────────────────────────

## Audit Finding Summary

The ChatGPT audit node identified the project as "unusually mature structurally"
with failures concentrated in operator cognition, not conceptual design. The
existing three manuals (01–03) plus the runbook index address the core pipeline.
What remains is five failure classes and one priority artifact.

**Failure classes identified (ChatGPT node):**
1. Environment reproducibility — no locked dependency manifest
2. Orchestration/runbook logic — no master pipeline state tracker
3. Coder calibration workflows — no warm-up/practice subsample
4. Human-subject execution procedures — IRB, consent, P7 arm undocumented
5. Novice-facing SOP documentation — missing operator decision trees

**Priority artifact named:**
> `MASTER_PIPELINE_RUNBOOK.md`

**Additional portability bug (ChatGPT audit §1.3):**
`sap_pipeline_validation.py` exports to `/home/claude/sap_synthetic_output.csv`
(hardcoded absolute path). This fails on any operator machine. Must be fixed
before any undergrad runs Manual 01.

---

## Gap Analysis: Existing vs. Required Coverage

| Failure class | Existing coverage | Gap | Severity |
|---|---|---|---|
| Environment reproducibility | Manual 01: pip install command | No `requirements.txt` or `pip freeze` lock; no Python version enforcement; no venv scaffold | HIGH |
| Orchestration / state tracking | Runbook Index: phase map table | No persistent state file; operator cannot tell which phases completed without manual inspection | HIGH |
| Coder calibration | Manual 03: IRR subsample procedure | No practice set; no warm-up coding round before subsample; raters go live cold | MEDIUM |
| Human-subject / P7 arm | Manual 03 §7: "future: Manual 04" | No IRB placeholder guidance; no consent language; no human session SOP | MEDIUM (deferred) |
| Operator decision trees | Red flags scattered across manuals | No "what do I do if X" quick-reference; undergrad will freeze at ambiguous state | MEDIUM |
| Path portability bug | Not addressed | `/home/claude/` hardcode in `sap_pipeline_validation.py` | HIGH (blocks Manual 01) |
| Coder CSV template | Manual 03 references template | No actual `rater_coding_template.csv` file exists in repo | HIGH (blocks Manual 03) |
| `--generate-subsample` flag | Manual 03 documents it | Flag may not exist in current `parallel_failure_coder.py` — needs verification | HIGH |

---

## Enhancement Plan: What Gets Built and By Whom

The following tasks are assigned to specific nodes. König approves the task
list before any node begins execution.

---

### TASK A — Environment Lock File
**Owner:** Rat Dev Claude (Assembler Node)
**Deliverable:** `docs/requirements.txt` (pinned versions) + Manual 01 patch
**Scope:**
- Generate `requirements.txt` with pinned versions for all six dependencies
- Add a step to Manual 01 that verifies Python version against `.python-version`
  or inline assertion before any install
- Add venv scaffold instructions as an optional but recommended path
- Note: do not break existing `--break-system-packages` flow for operators
  on managed systems

**Manual 01 patch — insert after step 3:**
```
3a. (Recommended) Create a virtual environment to isolate dependencies.

    python3 -m venv .venv
    source .venv/bin/activate   # macOS/Linux
    .venv\Scripts\activate      # Windows

    Then run the pip install command. To deactivate later: deactivate

3b. Alternatively, install system-wide with break-system-packages (existing step).

3c. Lock your environment after install:

    pip freeze > requirements_local.txt
    # Do not commit this — it is machine-specific.
    # Do compare it against docs/requirements.txt if something breaks.
```

**Status:** READY — Claude executes this session

---

### TASK B — Path Portability Fix (Script Bug)
**Owner:** Rat Dev Claude (Assembler Node)
**Deliverable:** Patch note for `scripts/sap_pipeline_validation.py`
**Scope:**
- Document the hardcoded `/home/claude/` path bug identified by ChatGPT audit node
- Provide the one-line fix
- Add verification step to Manual 01 that confirms the output path is relative

**The bug (ChatGPT audit §1.3, §6):**
```python
# CURRENT (broken on operator machines):
_out_path = Path("/home/claude/sap_synthetic_output.csv")

# FIX — already implemented in current script version:
_out_dir = Path("data") / "synthetic"
_out_dir.mkdir(parents=True, exist_ok=True)
_out_path = _out_dir / "sap_synthetic_output.csv"
```

**Audit note:** The fix appears to already be in the current script version
(confirmed by project knowledge read of `sap_pipeline_validation.py`).
Manual 01 should verify the output path in its "what success looks like" section.
The bug was present in an older version; confirm current script is the canonical one.

**Status:** VERIFY — König or Claude confirms current script has relative path

---

### TASK C — Coder CSV Template
**Owner:** Rat Dev Claude (Assembler Node)
**Deliverable:** `docs/rater_coding_template.csv`
**Scope:**
- Generate the actual CSV template that Manual 03 references but doesn't provide
- Columns: `response_id`, `session_id`, `turn`, `archetype` (hidden column),
  plus one column per ALL_TRAITS dimension, plus `notes`
- Include 3 example rows with plausible synthetic values so raters understand format
- Manual 03 §4 should reference the template explicitly with a `cp` command

**Template header (38 columns):**
```
response_id,session_id,turn,archetype,impulsivity,impulse_control,
emotional_lability,manic_affect,mania,risk_tolerance,reality_testing,
dissociation,paranoia,black_white_thinking,split_identity,
persecutory_ideas,compulsivity,need_for_cognition,grandiosity,
dominance_drive,grievance_narrative,ingroup_loyalty,abandonment_fear,
trauma_bonding,vengefulness,revenge_fantasy,sadism,interpersonal_chaos,
narcissistic_rage,moral_disengagement,empathy_deficit,calculating_behavior,
moral_rigidity,hypervigilance,control_needs,depressive_affect,
sleeplessness,pain_response,gallows_humor,identity_disturbance,
rumination,notes
```

**Status:** READY — Claude executes this session

---

### TASK D — Operator Decision Tree (Quick Reference Card)
**Owner:** Rat Dev Claude (Assembler Node)
**Deliverable:** `docs/OPERATOR_QUICKREF.md`
**Scope:**
- Single-page operator reference for the five most common failure states
- Format: "If [symptom] → [action] → [escalate if X]"
- Covers: script crashes, API errors, low κ, missing files, session interruption
- Explicitly tells the operator when to stop and contact König vs. self-recover

**Decision tree skeleton:**
```
SYMPTOM: Script exits with Python traceback
→ Read the last three lines of the traceback
→ If "ModuleNotFoundError": re-run pip install (Task A)
→ If "FileNotFoundError" for data/ path: check you ran steps in order
→ If anything else: screenshot the full traceback, stop, contact König

SYMPTOM: API returns error / rate limit
→ Wait 60 seconds, retry once
→ If persistent: check ANTHROPIC_API_KEY is set (echo $ANTHROPIC_API_KEY)
→ If key is set and error continues: check Anthropic status page, stop, contact König

SYMPTOM: κ result is below 0.60 on a dimension
→ Do not begin full coding
→ Print irr_results.csv, identify the low-κ dimension(s)
→ Follow Manual 03 §6 rubric revision procedure
→ Report revised definitions to König before re-coding

SYMPTOM: bsi_sessions.csv has fewer rows than expected
→ Run: python -c "import pandas as pd; df=pd.read_csv('data/bsi_sessions/bsi_sessions.csv'); print(df.groupby(['archetype','exploit_class','perturbation_type']).size())"
→ Identify missing conditions from output
→ Re-run only the missing conditions (Manual 02 §7)

SYMPTOM: A session produces fewer than 10 turns in responses.jsonl
→ Do not include this session in analysis
→ Document the session_id, the error (if any), and the condition
→ Report to König — König decides whether to re-run or exclude
```

**Status:** READY — Claude executes this session

---

### TASK E — Coder Warm-Up Practice Set
**Owner:** Rat Dev Claude (Assembler Node)
**Deliverable:** `docs/IRR_PRACTICE_SET.md`
**Scope:**
- 6 synthetic practice responses (one per archetype) with scoring keys
- Purpose: raters calibrate against the key *before* touching the real subsample
- Raters must score all 6 and compare to key; if ≥3 dimensions differ by >0.3,
  rater re-reads the data dictionary before proceeding
- This is the warm-up round, not IRR — it does not affect κ computation

**Why it matters:** Without this, raters arrive at the real subsample with
no shared calibration baseline. The first 20 responses effectively become a
second warm-up anyway, contaminating the κ computation.

**Practice item format:**
```
PRACTICE ITEM 1 — Archetype: [revealed after scoring]

Response text:
"[synthetic response text designed to be unambiguous on primary traits]"

Your scores:
impulsivity: ___
reality_testing: ___
[primary cluster only — 4–5 dimensions]
notes: ___

SCORING KEY (read after scoring):
Archetype: Joker
impulsivity: 0.85 — response proceeds with zero deliberation language
reality_testing: −0.6 — persona speaks as if it IS the character, no meta-frame
[explanation of why each score is what it is]
```

**Status:** READY — Claude executes this session

---

### TASK F — Master Pipeline Runbook (Priority Artifact)
**Owner:** Rat Dev Claude (Assembler Node)
**Deliverable:** `docs/MASTER_PIPELINE_RUNBOOK.md`
**Scope (ChatGPT audit node recommendation):**
- Single document that gives an operator a persistent state view of the pipeline
- Not a replacement for the individual manuals — a navigation layer above them
- Tracks which phases are complete, what data exists, what is next
- Includes a `pipeline_state.json` schema that operators update as phases complete

**Structure:**
```
MASTER_PIPELINE_RUNBOOK.md
├── 0. Overview: what this document is and how to use it
├── 1. Phase completion tracker (fill in as you go)
├── 2. Current data inventory (check commands)
├── 3. Decision gates (what König must approve before each phase)
├── 4. Escalation paths (who to contact for what)
├── 5. Quick navigation to individual manuals
└── 6. Pipeline health check (single command to run all verifications)
```

**The pipeline_state.json schema:**
```json
{
  "last_updated": "ISO-8601",
  "operator": "name",
  "phases": {
    "phase_0_env": {"status": "COMPLETE|IN_PROGRESS|NOT_STARTED", "date": ""},
    "phase_1_ctl": {"status": "", "sessions_completed": 0, "sessions_expected": 24},
    "phase_2_h1":  {"status": "", "sessions_completed": 0, "sessions_expected": 8},
    "phase_3_h2":  {"status": "", "sessions_completed": 0, "sessions_expected": 24},
    "phase_4_full": {"status": "", "sessions_completed": 0, "sessions_expected": 96},
    "phase_5_irr": {"status": "", "kappa_overall": null, "kappa_passed": null},
    "phase_6_coding": {"status": "", "responses_coded": 0}
  },
  "konig_approvals": {
    "phase_3_approved": false,
    "phase_4_approved": false,
    "irr_results_approved": false,
    "full_coding_approved": false
  },
  "red_flags": []
}
```

**Status:** READY — Claude executes this session

---

### TASK G — `--generate-subsample` Flag Verification
**Owner:** Rat Dev ChatGPT (Audit Node) — verification task
**Deliverable:** Confirmation or correction of Manual 03 §2 command
**Scope:**
- Manual 03 §2 documents `python parallel_failure_coder.py --generate-subsample`
- The ChatGPT audit has not confirmed this flag exists in current script version
- ChatGPT node should read `scripts/parallel_failure_coder.py` and verify:
  - Does `--generate-subsample` exist?
  - Does `--irr-check` exist with the `--rater1` / `--rater2` arguments?
  - Are the `--full-coding` arguments correct?
- If flags differ: correct Manual 03 to match actual script behavior
- Claude assembler cannot verify this without script execution access

**Status:** PENDING — ChatGPT audit node executes

---

### TASK H — Manual 04 Scoping (P7 Human Arm)
**Owner:** König decision → then Rat Dev Claude (Assembler Node) executes
**Deliverable:** `docs/LAB_MANUAL_04_p7_acg.md`
**Scope (when König authorizes):**
- IRB requirement placeholder — what must be in place before human arm begins
- Consent language template for CBESS comparison study
- Authority gradient simulator (LLM arm) procedure
- Human session SOP: recruitment, briefing, session structure, debriefing
- Matching protocol: how LLM sessions are matched to human profiles for CBESS
- CBESS computation from matched profile data

**Current status:** DEFERRED — König has not yet confirmed P3 LLM collection
is complete. This manual is not urgent. Do not begin until König confirms.

**Status:** BLOCKED ON KÖNIG DECISION

---

### TASK I — Naive Claude Stress Test
**Owner:** Naive Claude (Stress Test Node)
**Deliverable:** Failure report on all three manuals
**Scope:**
- Naive Claude (fresh instance, no project knowledge) reads each manual
  and attempts to follow it without any external context
- Documents every point of ambiguity, missing step, or assumed knowledge
- Reports: "I got stuck here because X was not defined / the command
  did not produce the expected output / I did not know which directory to be in"
- This is the highest-value test of operator-facing usability

**Prompt to send to Naive Claude:**
```
You are a Computer Science undergraduate student. You have been assigned
to collect data for a research project. You have the following three
documents and nothing else. No other context. No other documentation.
Follow each manual exactly and report every point where you are uncertain
what to do, where the instructions are ambiguous, or where you get an error
you don't know how to resolve.

[Attach: LAB_MANUAL_01_setup.md, LAB_MANUAL_02_llm_trials.md,
LAB_MANUAL_03_irr_coding.md, LAB_RUNBOOK_INDEX.md]
```

**Status:** READY — König or Claude assigns this to a fresh Claude instance

---

## Node Assignment Summary

| Task | Node | Status | Blocking |
|------|------|--------|---------|
| A — requirements.txt + venv scaffold | Rat Dev Claude | READY | Manual 01 operators |
| B — path bug verification | Rat Dev Claude / König | VERIFY | Manual 01 step 4.1 |
| C — rater_coding_template.csv | Rat Dev Claude | READY | Manual 03 §4 |
| D — OPERATOR_QUICKREF.md | Rat Dev Claude | READY | All operators |
| E — IRR_PRACTICE_SET.md | Rat Dev Claude | READY | Manual 03 IRR quality |
| F — MASTER_PIPELINE_RUNBOOK.md | Rat Dev Claude | READY | Orchestration gap |
| G — parallel_failure_coder.py flag verification | Rat Dev ChatGPT | PENDING | Manual 03 §2 |
| H — Manual 04 P7 human arm | König → Claude | BLOCKED | P3 completion |
| I — Naive Claude stress test | Naive Claude | READY | Usability validation |

---

## Execution Order Recommendation

Run in this sequence to unblock the most critical paths first:

1. **Task B** (verify path bug) — 5 minutes; if bug persists, Manual 01 is broken for everyone
2. **Task C** (rater CSV template) — 30 minutes; Manual 03 is incomplete without it
3. **Task A** (requirements.txt) — 30 minutes; environment reproducibility
4. **Task F** (Master Pipeline Runbook) — 2 hours; ChatGPT's highest-value recommendation
5. **Task D** (Operator Quick Reference) — 1 hour; reduces König interruptions
6. **Task E** (IRR Practice Set) — 1 hour; prevents κ contamination
7. **Task G** (ChatGPT flag verification) — whenever ChatGPT node is available
8. **Task I** (Naive Claude stress test) — after Tasks A–F complete; final usability gate
9. **Task H** (Manual 04) — after König confirms P3 collection complete

---

## What the ChatGPT Audit Got Right That the Existing Manuals Miss

Three observations from the audit that shaped this plan:

**"Operator cognition failures, not conceptual failures."**
The scripts work. The theory is sound. What breaks is an undergrad who hits
an ambiguous state and either guesses wrong or freezes. Tasks D and F directly
address this. The Quick Reference Card and the Master Runbook are not
documentation polish — they are failure prevention.

**"The biggest weakness is environment reproducibility."**
A locked `requirements.txt` and a venv scaffold are not bureaucratic overhead.
They are the difference between "this works on my machine" and "this is reproducible
research." Task A is a 30-minute fix that eliminates an entire category of
debugging sessions.

**"Coder calibration workflows."**
No warm-up round means two raters arrive at the real data with no shared
calibration signal. They will disagree on ambiguous cases in ways that reduce
κ below threshold. Task E costs 1 hour to build and potentially saves a full
re-coding cycle.

---

*Document version: 1.0 — 2026-05-09*
*Prepared by: Rat Dev Claude (Assembler Node)*
*Source: Rat Dev ChatGPT Lab Manual Audit (Project Knowledge)*
*RACI: König reviews task list and approves execution order before nodes begin*
