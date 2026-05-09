# SEED: Naive Claude — Lab Manual Blind Smoke Test
# Node: Naive Claude (Stress Test / Usability Audit)
# Prepared by: Rat Dev Claude (Assembler Node)
# Date: 2026-05-09
# RACI: König runs this session; results reported to Rat Dev Claude for manual revision
#
# ── ATTACHMENT STRATEGY ───────────────────────────────────────────────────────
# Naive Claude has attachment limits. Do NOT attach all four manuals at once.
# Delivery sequence:
#   Message 1 (this seed): persona + task framing + LAB_RUNBOOK_INDEX.md
#   Message 2: LAB_MANUAL_01_setup.md (when Naive Claude asks for it or begins)
#   Message 3: LAB_MANUAL_02_llm_trials.md (after 01 walkthrough complete)
#   Message 4: LAB_MANUAL_03_irr_coding.md (after 02 walkthrough complete)
#   Supplementary (if requested): OPERATOR_QUICKREF.md, IRR_PRACTICE_SET.md
# Do NOT provide the data dictionary, paper drafts, or scripts — Naive Claude
# should discover those gaps through the manual text, not pre-knowledge.
# ─────────────────────────────────────────────────────────────────────────────

---

## MESSAGE 1 — SEND FIRST (paste this entire block as the opening message)

---

You are a Computer Science undergraduate student. You have just been assigned
to collect data for a research project by your supervisor. You do not know
what the research is about. You have not read any of the papers. You have
never worked with this codebase before.

Your supervisor has given you access to a repository and a set of lab manuals
in the `labs/` directory. They told you to start with the runbook index and
follow it.

You have the following:
- A laptop running Ubuntu 24 with Python 3.13 already installed
- A terminal
- An Anthropic API key (you will not use it today — the first manual is dry-run only)
- The attached document: `LAB_RUNBOOK_INDEX.md`

**Your task:** Work through the manuals exactly as written. Do not skip steps.
Do not assume anything that isn't stated in the document you have been given.

**As you work, report:**
1. Every step you complete successfully, and what output you saw
2. Every point where you are uncertain what to do — quote the exact phrase
   that confused you and explain why
3. Every point where the instructions assume knowledge you don't have
4. Every place where you tried something and got an unexpected result
5. Any step where you are not sure if you passed or failed
6. Anything you would want to ask your supervisor before continuing

**Important rules:**
- Do not ask me for help interpreting the documents. Work with what the
  documents say. If you can't figure it out from the document, that IS
  the finding — report it.
- If a step says "expected output: X" and you get Y, report both X and Y
  verbatim. Do not guess which one is correct.
- If you would normally Google something, note "I would search for [X]"
  rather than doing it — this test is about what the manual covers, not
  what the internet covers.
- Do not modify any files unless the manual explicitly instructs you to.
- When you are unsure whether to continue or stop, stop. Report why.

Begin by reading `LAB_RUNBOOK_INDEX.md` (attached). Tell me:
- What you understand the repo to be for
- What you will do first
- Any questions that arise before you take a single action

[ATTACH: labs/LAB_RUNBOOK_INDEX.md]

---

## MESSAGE 2 — SEND AFTER Naive Claude reads the index and is ready to begin

---

Good. Here is the first manual.

Work through it step by step. Do not proceed past a step until you have
either completed it or flagged it as blocked.

If a step fails, do not skip it. Report the failure and stop.

[ATTACH: labs/LAB_MANUAL_01_setup.md]

---

## MESSAGE 3 — SEND AFTER Manual 01 walkthrough complete

---

Manual 01 is done. Here is Manual 02.

Same rules apply. One step at a time. Report every uncertainty and every
unexpected output.

Note: Manual 02 contains phases that require König approval before running.
When you reach a König-approval gate, stop and report: "I have reached
a König-approval gate. I cannot proceed without authorization."

Do not simulate running the live API phases — treat them as blocked until
authorized. The dry-run steps can proceed.

[ATTACH: labs/LAB_MANUAL_02_llm_trials.md]

---

## MESSAGE 4 — SEND AFTER Manual 02 walkthrough complete

---

Manual 02 done. Here is Manual 03.

Same rules. Note: Manual 03 requires data from Manual 02 to have been
collected. Since you ran only dry-run sessions, some steps in Manual 03
may not be executable. When you reach a step that requires live data,
report: "This step requires live session data from Manual 02. Cannot
execute in dry-run mode." Then continue reading the rest of the manual
and report any additional issues you find.

[ATTACH: labs/LAB_MANUAL_03_irr_coding.md]

---

## WHAT TO LOOK FOR — König Debrief Checklist

After the session, review Naive Claude's output for these failure categories.
These map to the ChatGPT audit's five failure classes.

**Failure Class 1 — Environment reproducibility:**
- Did Naive Claude encounter Python version issues?
- Did the pip install command work as written?
- Did any path assumption fail (e.g., `cd scripts/` from wrong directory)?

**Failure Class 2 — Orchestration / state tracking:**
- Did Naive Claude know which phase they were in without being told?
- Did they know when they had "passed" a phase?
- Did they know what to do between manuals?

**Failure Class 3 — Assumed knowledge gaps:**
- Did Naive Claude encounter terms (BSI, CEE, τ, κ) without definition?
- Did any command produce output they couldn't interpret?
- Did any "expected output" not match what they saw?

**Failure Class 4 — Decision ambiguity:**
- Were there decision points where the manual gave no guidance?
- Did Naive Claude freeze or guess?
- Did they reach König-approval gates and handle them correctly?

**Failure Class 5 — Missing artifacts:**
- Did they find a reference to a file that doesn't exist yet?
  (e.g., rater_coding_template.csv, pipeline_state.json)
- Did any command fail because a required file was absent?

**Severity tagging for findings:**
- 🔴 BLOCKS — operator cannot proceed without this being fixed
- 🟡 CONFUSES — operator proceeds incorrectly or guesses wrong
- 🟢 MINOR — operator recovers independently but wastes time

---

## REPORT FORMAT — Ask Naive Claude to produce this at the end

---

At the end of the session, ask Naive Claude:

"Please produce a structured report of every issue you found, organized by
manual and step number. For each issue, state:
1. Which manual and step (e.g., Manual 01 §4.2)
2. What the manual says
3. What happened or what was unclear
4. Whether this would block you, confuse you, or just slow you down
5. What you would have wanted the manual to say instead"

This report feeds directly into manual revision. Route it to Rat Dev Claude
(Assembler Node) for the next enhancement pass.

---

## SESSION PARAMETERS

| Parameter | Value |
|---|---|
| Naive Claude model | claude-sonnet-4-6 (current) |
| Project knowledge | DISABLED — this is a blind test |
| Attachments per message | 1 document maximum (respect attachment limits) |
| Memory | DISABLED — fresh session, no prior context |
| König role in session | Messenger only — deliver documents, do not interpret |
| Session goal | Find every place the manuals fail a real operator |

**König's only permitted responses during the session:**
- Delivering the next manual when Naive Claude is ready
- Saying "continue" if Naive Claude pauses unnecessarily
- Saying "that is the finding — report it" when Naive Claude asks for help

König should NOT:
- Explain what a term means
- Clarify ambiguous instructions
- Tell Naive Claude whether an output is correct
- Help Naive Claude recover from a failure

The point of the test is to find what breaks unaided. If you help, the
test result is contaminated.

---

*Seed version: 1.0 — 2026-05-09*
*Prepared by: Rat Dev Claude (Assembler Node)*
*Route findings to: Rat Dev Claude for manual revision pass*
*RACI: König runs the session; König is silent observer except document delivery*
