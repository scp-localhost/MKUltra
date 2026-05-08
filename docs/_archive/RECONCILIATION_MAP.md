# RECONCILIATION MAP — MKUltra Doctoral Thesis Project
# "Behavioral Drift in LLMs Under Persona Injection"
# Three-paper practice-led doctoral series
#
# Maintainer: swarm/synthesis-narrative node
# Format: STATUS | ITEM | DEPENDENCIES | NOTES
# Statuses: COMPLETE | IN-PROGRESS | BLOCKED | QUEUED | WATCH
#
# Timestamp format: ISO 8601 — YYYY-MM-DDTHH:MM (session date approximated
# from swarm session; exact wall-clock unavailable — use git commit for
# ground truth on file dates)
# ─────────────────────────────────────────────────────────────────────────────

---

## 0. PROJECT STATE SUMMARY

| Paper | Draft Status | Blocker |
|---|---|---|
| Paper 1 — Constrained Analogical Transfer | SEED COMPLETE — drafting not started | Waiting P2 reconciliation |
| Paper 2 — LLM Social Engineering | ALL SECTIONS DRAFTED — assembly held | P1/P3 reconciliation pending |
| Paper 3 — Behavioral Drift Measurement | SEED COMPLETE — `calculate_psychopathy_drift()` stub | Implementation pending |

**Current session output:** Paper 2 all sections drafted.
**Hold point:** Full Paper 2 assembly held pending P1 CEE lock + P3 hypothesis set lock.

---

## 1. PAPER 2 — SECTION INVENTORY

### 1.1 Drafted This Session

| Status | Section | File | Timestamp |
|---|---|---|---|
| ✅ COMPLETE | Abstract | `drafts/paper2/P2_Abstract_S1_S2_S9.md` | 2026-04-27 |
| ✅ COMPLETE | S1 — Introduction | `drafts/paper2/P2_Abstract_S1_S2_S9.md` | 2026-04-27 |
| ✅ COMPLETE | S2 — SE Background & LLM Analogs | `drafts/paper2/P2_Abstract_S1_S2_S9.md` | 2026-04-27 |
| ✅ COMPLETE | S3 — Identity vs Prompt Injection | `drafts/paper2/P2_S3_IdentityInjection.md` | 2026-04-27 |
| ✅ COMPLETE | S4 — Exploit Class Taxonomy (all 5 classes) | `drafts/paper2/P2_S4_ExploitTaxonomy.md` | 2026-04-27 |
| ✅ COMPLETE | S4.6 — Cross-Class Interaction Effects | `drafts/paper2/P2_S4_ExploitTaxonomy.md` | 2026-04-27 |
| ✅ COMPLETE | S4.6.1 — Worked Example (Classes 1+2+3, Magneto) | `drafts/paper2/P2_S4_ExploitTaxonomy.md` | 2026-04-27 |
| ✅ COMPLETE | S4.7 — CEE Deformation Mapping | `drafts/paper2/P2_S4_ExploitTaxonomy.md` | 2026-04-27 |
| ✅ COMPLETE | S5 — CEE as Measurement Construct | `drafts/paper2/P2_S5_CEE_Operational.md` | 2026-04-27 |
| ✅ COMPLETE | S6 — Alignment Implications | `drafts/paper2/P2_S6_S7_S8.md` | 2026-04-27 |
| ✅ COMPLETE | S7 — Ethical Reflexivity | `drafts/paper2/P2_S6_S7_S8.md` | 2026-04-27 |
| ✅ COMPLETE | S8 — Limitations | `drafts/paper2/P2_S6_S7_S8.md` | 2026-04-27 |
| ✅ COMPLETE | S9 — Conclusion | `drafts/paper2/P2_Abstract_S1_S2_S9.md` | 2026-04-27 |

### 1.2 Assembly Status

| Status | Task | Dependency | Timestamp |
|---|---|---|---|
| ⏸ HELD | Full Paper 2 draft assembly (concat + cross-ref check) | P1 CEE formal definition lock; P3 hypothesis set lock | 2026-04-27 |
| ⏸ HELD | Conference venue pass (collapse S6+S7+S8 into single section) | Full assembly first | 2026-04-27 |
| ⏸ HELD | DOCX export of full Paper 2 draft | Assembly held | 2026-04-27 |

### 1.3 Known Edit Triggers on Assembly

Items in P2 that will require targeted edits depending on P1/P3 reconciliation outcomes:

| Location | Edit Trigger | Dependency |
|---|---|---|
| S5 Table 1 — CEE centroid derivation | Any change to CEE formal definition in P1 S5 | P1 S5 lock |
| S4 archetype data blocks (all 5 classes) | Any change to `forensic_archetype.py` trait weights | Script lock |
| S5.5 — Exploit class CEE deformation mapping | P3 hypothesis set revision | P3 H1–H4 lock |
| S8.5 — Measurement instrument validity | P3 empirical results (if available pre-assembly) | P3 data |
| S9.3 — Relationship to Papers 1 and 3 | P1 and P3 section numbering finalised | Both papers |
| Abstract — forward references to P3 | P3 central claim wording lock | P3 S1 lock |

---

## 2. PAPER 1 — SECTION INVENTORY

### 2.1 Status

| Status | Section | Notes | Timestamp |
|---|---|---|---|
| ✅ COMPLETE | Seed document (`seeds/p1.md`) | Full section blueprint available | Pre-session |
| ⬜ QUEUED | S1 — Introduction: The Mapping Problem | Drafting not started | — |
| ⬜ QUEUED | S2 — Framework A: DSM-5 as Behavioral Taxonomy | Source: `DSM-5_TR_Alignment.md` | — |
| ⬜ QUEUED | S3 — Framework B: SE Transfer | Cross-ref P2 S2 — must be consistent | — |
| ⬜ QUEUED | S4 — Framework C: Archetype Schema Theory | Source: `forensic_archetype_jung_monolith.py` | — |
| 🔴 CRITICAL | S5 — CEE Formal Definition | **Load-bearing for P2 S5 and P3 instrument** | — |
| ⬜ QUEUED | S6 — Validity Conditions for the Mapping | Committee-facing section | — |
| ⬜ QUEUED | S7 — Explicit Failure Cases | Must align with P2 S8 limitations | — |
| ⬜ QUEUED | S8 — Non-Claims Registry | Committee shield | — |
| ⬜ QUEUED | S9 — Conclusion | — | — |

### 2.2 Critical Dependency: CEE Formal Definition (P1 S5)

The CEE formal definition in P1 S5 is the single highest-priority unresolved item
in the entire three-paper series. Everything downstream depends on it:

- P2 S5 operationalizes the CEE — must be consistent with P1's formal definition
- P2 S4.7 maps exploit classes to CEE deformation vectors — assumes P1 definition
- P3 measurement instrument derives CEE bounds from `forensic_archetype.py` — assumes P1 definition
- P3 H1–H4 are all CEE-dependent hypotheses

**Action required:** P1 S5 draft before P2/P3 assembly. This is the next priority
after the current session unless P3 implementation is more urgent.

---

## 3. PAPER 3 — SECTION INVENTORY

### 3.1 Status

| Status | Section | Notes | Timestamp |
|---|---|---|---|
| ✅ COMPLETE | Seed document (`seeds/p3.md`) | Full blueprint + hypothesis set + experiment loop v0.2 | Pre-session |
| 🔴 CRITICAL | `calculate_psychopathy_drift()` implementation | Stub in `scripts/trait_drift_analysis.py` — needs full implementation | — |
| ⬜ QUEUED | Experiment loop v0.2 full implementation | `scripts/injection_experiment_protocol.py` | — |
| ⬜ QUEUED | S1 — Introduction | — | — |
| ⬜ QUEUED | S2 — Methods | Includes CEE derivation methodology | — |
| ⬜ QUEUED | S3 — Instrument Specification | `forensic_archetype.py` as CEE source | — |
| ⬜ QUEUED | S4 — Results | Requires data | — |
| ⬜ QUEUED | S5 — Discussion | Requires results | — |
| ⬜ QUEUED | S6 — Limitations | Must align with P2 S8 | — |

### 3.2 Formal Hypotheses (locked in seed — do not change without reconciliation note)

| ID | Hypothesis | Status |
|---|---|---|
| H1 | Magneto > Joker on CEE rigidity under contradiction perturbation (resistance response > 0.70 vs collapse > 0.60) | LOCKED in seed |
| H2 | Archetype condition predicts drift_magnitude (ANOVA, α=0.05) | LOCKED in seed |
| H3 | Perturbation type moderates perturbation response — interaction effect archetype × perturbation | LOCKED in seed |
| H4 | Batman produces highest recovery rate (exploratory) | LOCKED in seed |

**WATCH:** Any change to H1–H4 requires corresponding edit to P2 S5.5 (CEE deformation mapping)
and P2 S4.6.1 (worked example perturbation response annotation).

### 3.3 Archetype Set (locked — do not change without reconciliation note)

| Condition | Archetype | CEE Shape | Role |
|---|---|---|---|
| 1 (primary) | Magneto | High rigidity, resistance response | H1 primary |
| 2 (primary) | Joker | Low reality-anchoring, collapse response | H1 contrast |
| 3 | Batman | Constraint-adherent, recovery response | H4 exploratory |
| 4 | Harley Quinn | Escalation-susceptible, variable response | H3 interaction |
| 5 | Lex Luthor | Instrumental, hyperlogical, resistance | H2 ANOVA |
| 6 | Two-Face | Bimodal, unpredictable | H3 interaction |

---

## 4. CROSS-PAPER CONSISTENCY ITEMS

Items that must be consistent across papers. Check on assembly.

| Item | P1 Location | P2 Location | P3 Location | Status |
|---|---|---|---|---|
| CEE formal definition | S5 (QUEUED) | S5.1 (COMPLETE) | S2 Methods (QUEUED) | 🔴 P1 S5 not yet drafted |
| CEE tolerance parameter τ | S5 | S5.1 | Instrument spec | 🔴 Not yet defined |
| Archetype trait weights (centroid) | S4 (schema theory) | S4 + S5 Table 1 | `forensic_archetype.py` | ⚠️ WATCH — script is source of truth |
| SE framework citations (Cialdini, Milgram, Hadnagy) | S3 | S2 + S4 | Background only | ⚠️ Verify consistent citation style |
| DSM-5 behavioral taxonomy framing | S2 | Non-claims registry (S8) | — | ✅ Consistent in current drafts |
| "Acting vs being" limitation | S7 failure cases | S8.4 | S6 limitations | ✅ Consistent — all flag as scope limit |
| Session stationarity scope condition | S7 failure cases | S8.1 | S2 methods | ✅ Consistent in current drafts |
| Training data opacity limitation | S7 failure cases | S8.2 | S3 instrument | ✅ Consistent in current drafts |
| Non-claims registry | S8 (QUEUED) | S3.8 + throughout | — | ⚠️ P1 S8 not yet drafted; P2 has partial non-claims |
| Drift dimension vocabulary | S4 (schema theory) | S4 (detection sigs) + S5 Table 1 | `data_dictionary.md` | ⚠️ `data_dictionary.md` is stub — expand |

---

## 5. SCRIPT / INSTRUMENT STATUS

| File | Status | Priority | Notes | Timestamp |
|---|---|---|---|---|
| `scripts/forensic_archetype.py` | ✅ COMPLETE | — | Source of truth for CEE centroids | Pre-session |
| `scripts/forensic_archetype_jung_monolith.py` | ✅ COMPLETE | — | Jungian layer; used in P1 S4 | Pre-session |
| `scripts/forensic_archetype_tarot_monolith.py` | ✅ COMPLETE | — | Tarot layer; supplementary | Pre-session |
| `scripts/trait_drift_analysis.py` | 🔴 STUB | HIGH | `calculate_psychopathy_drift()` not implemented | Pre-session |
| `scripts/injection_experiment_protocol.py` | ⬜ UNKNOWN | HIGH | Experiment loop v0.2 per p3.md seed | — |
| `scripts/sap_pipeline_validation.py` | ⬜ UNKNOWN | MEDIUM | SAP validation — check against `Statistical_Analysis_Plan_v1.1.md` | — |
| `scripts/tarot_drift_integration.py` | ⬜ UNKNOWN | LOW | Tarot layer integration with drift — scope unclear | — |

### 5.1 `calculate_psychopathy_drift()` — required output schema

Target output (locked in p3.md seed — do not change without reconciliation note):

```python
{
  'drift_vector':          dict[str, float],   # per-trait delta from baseline
  'drift_magnitude':       float,              # L2 norm
  'cee_breach':            bool,
  'cee_breach_dimensions': list[str],
  'perturbation_response': str,               # 'recovery' | 'resistance' | 'collapse'
  'resilience_score':      float,             # 0.0 → 1.0
  'pcl_r_proxy':           float,             # Hare PCL-R composite proxy
}
```

---

## 6. DATA / DOCS STATUS

| File | Status | Notes | Timestamp |
|---|---|---|---|
| `data/synthetic/sap_synthetic_output.csv` | ✅ EXISTS | Review against SAP v1.1 | Pre-session |
| `docs/Statistical_Analysis_Plan.md` | ✅ EXISTS (stub) | Trait drift ANOVA + LMM — expand to match p3.md design | Pre-session |
| `docs/Statistical_Analysis_Plan_v1.1.md` | ✅ EXISTS | Check if this supersedes v1.0 | Pre-session |
| `docs/stimuli_registry.json` | ✅ EXISTS | Review — must cover 6-archetype set | Pre-session |
| `data_dictionary.md` | ⚠️ STUB | Single line — needs full trait dimension vocabulary | Pre-session |
| `artifacts/SYNTHETIC_CONSENT.md` | ✅ COMPLETE | Cited in P2 S7 ethical reflexivity | Pre-session |

---

## 7. QUEUED TASKS — PRIORITY ORDER

Priority order for next sessions, post-P1/P3 discussion:

| Priority | Task | Rationale |
|---|---|---|
| 1 | Draft P1 S5 — CEE formal definition | Highest dependency item — unlocks P2+P3 assembly |
| 2 | Implement `calculate_psychopathy_drift()` | P3 proof engine requires it; blocks experiment loop |
| 3 | Implement experiment loop v0.2 (`injection_experiment_protocol.py`) | P3 data collection blocked |
| 4 | Expand `data_dictionary.md` — full trait dimension vocabulary | P3 coding protocol requires it; P2 S4 detection sigs reference it |
| 5 | Draft P1 S1–S4, S6–S9 | Complete P1 draft |
| 6 | Assemble full Paper 2 draft | Held on P1 CEE lock + P3 hypothesis lock |
| 7 | Conference venue pass — Paper 2 (collapse S6+S7+S8) | Post-assembly; target USENIX/IEEE S&P adjacent |
| 8 | Draft P3 S1–S6 (methods, results, discussion) | After instrument implementation + data |
| 9 | Cross-paper consistency audit (full) | Pre-submission pass |
| 10 | DOCX exports — all three papers | Terminal formatting pass |

---

## 8. DIRECTORY RECOMMENDATIONS

Current flat `drafts/` will become unmanageable. Recommended migration:

```
drafts/
├── paper1/
│   └── (sections TBD)
├── paper2/
│   ├── P2_Abstract_S1_S2_S9.md      ✅ generated 2026-04-27
│   ├── P2_S3_IdentityInjection.md   ✅ generated 2026-04-27
│   ├── P2_S4_ExploitTaxonomy.md     ✅ generated 2026-04-27
│   ├── P2_S5_CEE_Operational.md     ✅ generated 2026-04-27
│   ├── P2_S6_S7_S8.md               ✅ generated 2026-04-27
│   └── Paper2_FULL_DRAFT.docx       ⏸ HELD
├── paper3/
│   └── (sections TBD)
└── legacy/
    ├── Paper2_Methods_Chapter.docx
    ├── Paper2_Methods_Chapter_v2.docx
    └── Paper2_Section3_Draft.docx
```

**Action:** Move existing `drafts/*.docx` to `drafts/legacy/` to prevent
confusion with new section-level MD files. Check whether legacy DOCX content
is superseded by new section drafts before archiving.

---

## 9. WATCH LIST — POTENTIAL ISSUES

Items flagged for attention that are not yet blockers but could become so:

| Flag | Item | Risk | Timestamp |
|---|---|---|---|
| ⚠️ WATCH | `stimuli_registry.json` coverage | Must include all 6 archetype conditions; unknown if Two-Face + Lex Luthor are registered | 2026-04-27 |
| ⚠️ WATCH | `Statistical_Analysis_Plan_v1.1.md` vs `Statistical_Analysis_Plan.md` | Version conflict unclear — v1.1 may have superseded v1.0; confirm canonical version | 2026-04-27 |
| ⚠️ WATCH | `tarot_drift_integration.py` scope | Role of tarot layer in drift measurement unclear — does it contribute to CEE derivation or is it supplementary only? | 2026-04-27 |
| ⚠️ WATCH | P2 S3 Table 2 (prompt vs identity injection) | Committee may request empirical support for the 5-axis distinction; currently theoretical — P3 data could validate the scope distinction empirically | 2026-04-27 |
| ⚠️ WATCH | CEE tolerance parameter τ | Not yet formally defined anywhere in project — P1 S5 must define it; P2 S5 uses it implicitly | 2026-04-27 |
| ⚠️ WATCH | Bandura (1986/1999) citation in P2 S4 Class 4 | Bandura moral disengagement cited — verify full reference details for bibliography | 2026-04-27 |
| ⚠️ WATCH | `data_dictionary.md` stub | P3 coding protocol and P2 S4 detection signatures reference trait dimensions that are not formally defined in the dictionary — expand before coding begins | 2026-04-27 |

---

## 10. CHANGELOG

| Date | Entry |
|---|---|
| 2026-04-27 | MAP created. Paper 2 all sections drafted in session. Assembly held pending P1/P3 reconciliation. Priority stack established. Directory restructure recommended. Five-class exploit taxonomy complete. CEE operational definition complete. Worked example (S4.6.1) complete. Identity vs prompt injection distinction complete (S3). Alignment implications, ethical reflexivity, limitations complete (S6/S7/S8). Abstract, introduction, SE background, conclusion complete. |

---

*Swarm note: this map is the single source of truth for project state.
Update the changelog entry and relevant status cells after every working session.
Do not rely on memory or git log alone — the map is the map.*
