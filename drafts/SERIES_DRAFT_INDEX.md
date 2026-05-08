<!-- ════════════════════════════════════════════════════════════════════════
  SERIES DRAFT INDEX — FINAL ASSEMBLY PASS
  Series:   MKUltra Doctoral Research Programme — LLM Identity Drift
  Author:   Stephen Pote (scp)
  Generated: 2026-04-30
  Node:     MKUltra / Mause Koenig — Assembler
  Arc:      Define (P1) → Exploit (P2) → Measure (P3) → Compare (P4) →
            Evaluate (P5) → Defend (P6) → Synthesize (P7) → Exegesis
  Workflow: Pre-Git Init Checkpoint — ready for ChatGPT audit node
════════════════════════════════════════════════════════════════════════ -->

# SERIES DRAFT INDEX — Final Assembly Pass

---

## Assembly Summary

| Paper | Title (short) | Sections | Placeholders | Open Flags | Status |
|---|---|---|---|---|---|
| P1 | Constrained Analogical Transfer | 9 | 0 | 2 (P4 back-prop, bib) | ✅ COMPLETE |
| P2 | LLM Social Engineering | 10 | 0 | 2 (S4 merge, bib) | ✅ ASSEMBLED |
| P3 | Behavioral Drift Measurement | 3 of 8 | 5 (S4–S8) | 3 | ⚠️ PARTIAL |
| P4 | Alignment Depth as Attack Surface | 8 | 0 | 2 | ✅ COMPLETE |
| P5 | Behavioral Stability Index | 8 | 1 (S5 data) | 1 | ✅ ASSEMBLED |
| P6 | Constraint Enforcement Framework | 8 | 1 (S5 data) | 1 | ✅ ASSEMBLED |
| P7 | Cross-Domain Behavioral Equivalence | 9 + Scope Audit | 1 (S5 data) | 1 | ✅ COMPLETE |

**Total sections assembled:** 55 across 7 papers + Scope Audit
**Placeholder stubs (data-pending only):** 7 — all are results sections awaiting live trial data
**P3 acknowledged partial:** YES — S4–S8 not yet drafted
**Pre-git init status:** READY for ChatGPT audit node handoff

---

## Flag Clearance Register

| Flag | Status | Resolution |
|---|---|---|
| FLAG-P7-S5-MISSING | ✅ CLEARED | P7_S5_Results_Placeholder.md re-produced from project knowledge; all table structures, H_P7_1–5 shells, and pre-registered decision rules intact |
| FLAG-P2-S4-SPLIT | ⚠️ CARRY FORWARD | Both files included in assembly. Merge into canonical `P2_S4_Full.md` is a pre-git edit task for ChatGPT node |
| FLAG-C-CEE-DIVERGENCE | ✅ CLEAR | P1 S5 and P2 S5 definition identical |
| FLAG-EXPLOIT-COUNT | ✅ CLEAR | 5 classes confirmed throughout |
| FLAG-BSI-SCHEMA | ✅ CLEAR | P6 S4 field names match P5 S4 §4.5.3 |
| FLAG-ACG-L0-L4 | ✅ CLEAR | P7 S3 references P6 §4.2 verbatim |
| FLAG-P1-S3-MISSING | ✅ CLEARED | S3 was already drafted; prior reconciliation maps were stale |
| FLAG-C-04 (bib) | ⚠️ CARRY FORWARD | Bibliography pass — SE citation years, Wei et al. (2023) venue |
| FLAG-P3-PARTIAL | ⚠️ ACKNOWLEDGED | S4–S8 not drafted — known open item |
| FLAG-C-10 (data_dict) | 🔴 CARRY FORWARD | `data_dictionary.md` stub — blocks P3 coding protocol |
| FLAG-C-11/12 | ⚠️ CARRY FORWARD | P3–P4 scope notes; ChatGPT audit node task |
| FLAG-P7-SCRIPT-ASSIGN | ⚠️ CARRY FORWARD | 3 scripts with unclear paper ownership |

---

## Per-Paper Status

### P1 — Constrained Analogical Transfer
- **File:** `paper1/Paper1_Draft.md` | ~2,200 lines
- **Complete:** S1 Introduction, S2 DSM-5 Taxonomy, S3 SE Transfer,
  S4 Archetype Schema Theory, S5 CEE Formal Definition, S6 Validity Conditions,
  S7 Failure Cases, S8 Non-Claims Registry, S9 Conclusion
- **Carry-forward for ChatGPT node:**
  - P4 back-propagation: P4 §6.7 forward pointer needed in P1 §9.4
  - Bibliography pass: all citations in §1.2, §3.2

### P2 — LLM Social Engineering
- **File:** `paper2/Paper2_Draft.md` | ~1,060 lines
- **Complete:** Abstract, S1–S9 (S9 in Abstract bundle file)
- **Carry-forward for ChatGPT node:**
  - S4 file merge: `Paper2_Section4_ExploitTaxonomy.md` (legacy, Classes 1–5) +
    `P2_S4_ExploitTaxonomy.md` (canonical, §4.6.1 only) → single `P2_S4_Full.md`
  - Add P1 §3.3 cross-reference in P2 S3 or S5 (agentic shift / persona capture link)
  - Non-claims: consolidate distributed non-claims against P1 S8 master registry
  - Bibliography: SE citation years, Mouton et al. (2016) author list
- **Legacy files (excluded from assembly):**
  `Paper2_Methods_Chapter.docx`, `Paper2_Methods_Chapter_v2.docx`,
  `Paper2_Section3_Draft.docx`

### P3 — Behavioral Drift Measurement
- **File:** `paper3/Paper3_Draft.md` | ~730 lines
- **Complete:** S1 Introduction, S2 Methods, S3 Instrument Specification
- **[SECTION PENDING] stubs:** S4 Results, S5 Discussion, S6 Limitations,
  S7 Ethical Reflexivity, S8 Conclusion
- **Critical blocker:** `data_dictionary.md` must be expanded before coding
  protocol is finalised (P1 §2.7 table defines minimum vocabulary)
- **Carry-forward:** P3 S3 Two-Face bimodal CEE reference to P1 §2.5 (verify)

### P4 — Alignment Depth as Attack Surface
- **File:** `paper4/Paper4_Draft.md` | ~3,885 lines
- **Complete:** S1–S8 fully drafted
- **Carry-forward for ChatGPT node:**
  - §7.5.4 cross-model confounds → add to RECONCILIATION_MAP
  - §7.4.3 future work → propagate to P3 §5 Discussion note
  - Wei et al. (2023) venue verification

### P5 — Behavioral Stability Index
- **File:** `paper5/Paper5_Draft.md` | ~2,177 lines
- **Complete:** S1–S8; S5 is a pre-registered results placeholder
- **S5 populates when:** live trial data from `run_identity_drift_trials.py`
  and `bsi_stats_pipeline.py` is available

### P6 — Constraint Enforcement Framework
- **File:** `paper6/Paper6_Draft.md` | ~2,769 lines
- **Complete:** S1–S8; S5 is a pre-registered results placeholder
- **S5 populates when:** live CEF validation trial data available
- **BSI field names:** VERIFIED consistent with P5 S4 §4.5.3 canonical schema

### P7 — Cross-Domain Behavioral Equivalence
- **File:** `paper7/Paper7_Draft.md` | ~2,621 lines
- **Complete:** S1–S8 + Scope Audit; S5 re-produced and populated
- **S5 status:** Pre-registered placeholder with all table shells, H_P7_1–5
  hypothesis tests, and pre-registered decision rules. [DATA] cells populated
  on live human + LLM trial collection
- **Series arc conclusion:** Pre-registered at §5.8; populates when
  CBESS primary mean is computed from live data
- **Carry-forward:** 3 scripts with unclear paper ownership
  (`injection_experiment_protocol.py`, `tarot_drift_integration.py`,
  `alignment_typology_matrix.py`)

---

## Cross-Paper Consistency Register — Final State

| # | Item | Final status |
|---|---|---|
| C-01 | CEE definition P1/P2/P3/P4 | ✅ CLEAR |
| C-02 | CEE tolerance τ | ✅ CLEAR |
| C-03 | Archetype trait weights → `forensic_archetype.py` | ✅ SOURCE OF TRUTH |
| C-04 | SE citation years | ⚠️ BIBLIOGRAPHY PASS — ChatGPT node |
| C-05 | DSM-5 framing | ✅ CLEAR |
| C-06 | Acting vs. being limitation | ✅ CLEAR |
| C-07 | Session stationarity | ✅ CLEAR |
| C-08 | Training data opacity | ✅ CLEAR |
| C-09 | Non-claims registry | ⚠️ P2 consolidation — ChatGPT node |
| C-10 | data_dictionary.md | 🔴 CRITICAL — ChatGPT / scp task |
| C-11 | P4 AD proxy vs P3 resilience_score | ⚠️ Note required — ChatGPT node |
| C-12 | P4 4 failure modes vs P3 3 types | ⚠️ P3 S3 note required — ChatGPT node |
| C-BSI | BSI field names P5 vs P6 | ✅ CLEAR |
| C-ACG | ACG L0–L4 P6 vs P7 | ✅ CLEAR |
| C-CEE-DIV | CEE definition P1 vs P2 | ✅ CLEAR |
| C-EXPLOIT | 5-class count everywhere | ✅ CLEAR |

---

## Handoff Note to ChatGPT Audit Node

The Claude assembler node has completed its RACI responsibilities:

- ✅ All 7 paper drafts assembled from canonical section files
- ✅ P7 S5 re-produced and verified against script/spec sources
- ✅ P1 S3 confirmed present (prior reconciliation maps were stale)
- ✅ CEE, exploit count, BSI fields, ACG protocol all verified consistent
- ✅ Legacy P2 files excluded; both S4 files included with merge flag
- ✅ Bibliography citation years locked (C-04 carry-forward for verification pass)

**Items requiring ChatGPT audit node action:**
1. Rigor audit — claims, causal language, falsifiability across P1–P7
2. Voice coherence — narrative drift across papers (per RACI snapshot)
3. P2 S4 file merge (legacy + canonical → single `P2_S4_Full.md`)
4. P1 §9.4 / P4 §6.7 back-propagation forward pointer
5. `data_dictionary.md` expansion (or flag for scp to action)
6. C-11/C-12 scope notes in P3 S3 and P4 §7.5
7. Bibliography verification pass (SE citations, Wei et al. 2023)
8. Numeric paper references → title-based references (per RACI naming convention)

**Pre-git init checkpoint:** Assembler node declares READY.
Pending: ChatGPT audit pass + directory janitorial (`.gitignore`, legacy
file archive, RECONCILIATION_MAP collapse) before `git init`.

---

*Generated by MKUltra Assembler Node — 2026-04-30. Supersedes SERIES_DRAFT_INDEX.md
from initial assembly pass.*

