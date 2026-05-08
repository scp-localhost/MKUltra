# RECONCILIATION MAP — Doctoral Thesis Project
# "Behavioral Drift in LLMs Under Persona Injection"
# Practice-led doctoral series — seven papers + exegesis
#
# Maintainer: swarm/synthesis-narrative node
# Format: STATUS | ITEM | DEPENDENCIES | NOTES
# Statuses: COMPLETE | IN-PROGRESS | BLOCKED | QUEUED | WATCH
#
# Timestamp format: ISO 8601 — YYYY-MM-DDTHH:MM
# Source of truth: this file. Update changelog after every session.
# ─────────────────────────────────────────────────────────────────────────────

---

## 0. PROJECT STATE SUMMARY

| Paper | Draft Status | Blocker |
|---|---|---|
| Paper 1 — Constrained Analogical Transfer | SUBSTANTIALLY DRAFTED — S3 missing, S1 partial | S3 (SE Transfer) not yet drafted as standalone section |
| Paper 2 — LLM Social Engineering | ALL SECTIONS DRAFTED — assembly held | P1 CEE lock + P3 hypothesis lock pending |
| Paper 3 — Behavioral Drift Measurement | SEED COMPLETE — instrument stub | `calculate_psychopathy_drift()` implementation pending |
| Paper 4 — Alignment Depth as Attack Surface | **ALL SECTIONS COMPLETE — 30,499 words** | §1 Introduction + Abstract complete 2026-04-28 |
| Paper 5 — Behavioral Stability Index | SEED ONLY (`p5.md`) | Awaiting P3 data + P4 typology |
| Paper 6 — Constraint Enforcement Framework | SEED ONLY (`p6.md`) | Awaiting P5 metrics |
| Paper 7 — Parallel Failure Modes | SEED ONLY (`p7.md`) | Scope overlaps P1 — assess before drafting |

**Series arc:** Define (P1) → Exploit taxonomy (P2) → Measure (P3) → Compare/theorize (P4) → Evaluate (P5) → Defend (P6) → Synthesize cross-domain (P7) → Exegesis

**Exegesis status:** Not yet started. P4 §8 exegesis hooks planted; P1 §9 hooks implicit. Formal exegesis drafting depends on P1–P4 assembly.

**Current session output (2026-04-28):** Paper 4 all sections complete. RECONCILIATION_MAP.md update.

---

## 1. PAPER 1 — Constrained Analogical Transfer

### 1.1 Section Status

| Status | Section | File | Notes |
|---|---|---|---|
| ✅ COMPLETE | S1 Introduction + S6 Validity + S7 Failure Cases + S8 Non-Claims + S9 Conclusion | `P1_S1_S6_S7_S8_S9_Bundle.md` | Bundle — all five sections in one file |
| ✅ COMPLETE | S2 — DSM-5 as Behavioral Taxonomy | `P1_S2_DSM5_BehavioralTaxonomy.md` | Cluster B mechanism extraction |
| ⬜ MISSING | S3 — SE Transfer Framework | — | Not yet drafted as standalone. P2 S2 covers this ground; P1 S3 needs its own version anchored to validity conditions framing |
| ✅ COMPLETE | S4 — Archetype Schema Theory | `P1_S4_ArchetypeSchemaTheory.md` | Three-layer centroid derivation, overdetermination criterion, shadow activation |
| ✅ COMPLETE | S5 — CEE Formal Definition | `P1_S5_CEE_FormalDefinition.md` | **Critical — load-bearing for P2/P3/P4** |

### 1.2 Critical Dependency Status

| Dependency | Status | Notes |
|---|---|---|
| CEE formal definition (P1 S5) | ✅ COMPLETE | Unlocks P2/P3 assembly |
| CEE tolerance parameter τ | ✅ DEFINED in P1 S5 | Per-archetype τ calibration documented |
| Three-layer centroid derivation procedure | ✅ COMPLETE | Forensic + Jungian + Tarot layers specified |
| Non-claims registry (P1 S8) | ✅ COMPLETE | In bundle |
| SE Transfer section (P1 S3) | 🔴 MISSING | Blocks complete P1 assembly |

### 1.3 Assembly Status

| Status | Task | Dependency |
|---|---|---|
| ⏸ HELD | Full P1 draft assembly | P1 S3 missing |
| ⬜ QUEUED | P1 S3 — SE Transfer standalone draft | P2 S2 is the source material; adapt to P1 validity framing |
| ⬜ QUEUED | DOCX export | After assembly |

### 1.4 P4 Back-Propagation Items (required on P1 assembly)

| Item | P1 Location | Action Required |
|---|---|---|
| P4 §6.7 delivers on P1 §9.4 "alignment research" opening | P1 §9.4 | Add forward pointer: "The schema-layer research agenda implied here is developed formally in Paper 4 §6.7" |
| P4 §3 full typology extends P2 §6 instruction/schema-layer framing | P1 §3.5 (SE homology) | Verify P1's framing of RLHF/CAI alignment is consistent with P4 §3 — P4 is more granular |

---

## 2. PAPER 2 — LLM Social Engineering

### 2.1 Section Status

| Status | Section | File |
|---|---|---|
| ✅ COMPLETE | Abstract + S1 Introduction + S2 SE Background + S9 Conclusion | `P2_Abstract_S1_S2_S9.md` |
| ✅ COMPLETE | S3 — Identity vs Prompt Injection | `P2_S3_IdentityInjection.md` |
| ✅ COMPLETE | S4 — Exploit Class Taxonomy (all 5 classes + cross-class + worked example + CEE deformation) | `P2_S4_ExploitTaxonomy.md` |
| ✅ COMPLETE | S5 — CEE as Measurement Construct | `P2_S5_CEE_Operational.md` |
| ✅ COMPLETE | S6 Alignment Implications + S7 Ethical Reflexivity + S8 Limitations | `P2_S6_S7_S8.md` |

### 2.2 Assembly Status

| Status | Task | Dependency |
|---|---|---|
| ⏸ HELD | Full P2 draft assembly | P1 CEE lock (now resolved ✅); P3 H1–H4 lock (locked in seed ✅) |
| ⬜ QUEUED | Conference venue pass (collapse S6+S7+S8) | Post-assembly |
| ⬜ QUEUED | DOCX export | After assembly |

**P2 assembly is now unblocked.** Both previously stated blockers are resolved. Assembly can proceed.

### 2.3 P4 Back-Propagation Items (required on P2 assembly)

| Item | P2 Location | Action Required |
|---|---|---|
| P4 §3 full typology extends P2 §6 | P2 §6 (Alignment Implications) | Add forward pointer: "The instruction/schema-layer distinction developed here is extended in Paper 4 §3 into a four-class alignment methodology typology specifying predicted attractor depth and failure modes per class." |
| P4 §4.3.2 Cell B prediction (capability amplifies vulnerability) | P2 §6 | Note as theoretical extension: "Paper 4 §4 develops this argument formally, including the prediction that highly capable minimally aligned models may exhibit stronger schema activation signals than their less capable counterparts." |
| OW-3 behavioral signature (schema-consistent constraint from archetype, not alignment) | P2 §3 (identity injection distinction) | Add note that open-weight unaligned models may produce constraint-consistent outputs under lawful archetypes not because of alignment but because of the archetype's behavioral contract — a new distinguishing observation from P4 §3.5.3 |

### 2.4 Known Edit Triggers on Assembly

| Location | Trigger | Dependency |
|---|---|---|
| S5 Table 1 — CEE centroid derivation | Any change to CEE formal definition in P1 S5 | P1 S5 ✅ LOCKED |
| S4 archetype data blocks (all 5 classes) | Any change to `forensic_archetype.py` trait weights | Script lock |
| S5.5 — Exploit class CEE deformation mapping | P3 hypothesis set revision | P3 H1–H4 ✅ LOCKED |
| S8.5 — Measurement instrument validity | P3 empirical results | P3 data |
| Abstract — forward references to P3/P4 | P3 central claim wording lock; P4 §1.4 canonical claim | P4 §1.4 ✅ COMPLETE |

---

## 3. PAPER 3 — Behavioral Drift Measurement

### 3.1 Section Status

| Status | Section | Notes |
|---|---|---|
| ✅ COMPLETE | Seed document (`p3.md`) | Blueprint + hypothesis set + experiment loop v0.2 |
| 🔴 CRITICAL | `calculate_psychopathy_drift()` implementation | Stub in `trait_drift_analysis.py` |
| ⬜ QUEUED | Experiment loop v0.2 full implementation | `injection_experiment_protocol.py` |
| ⬜ QUEUED | S1–S6 (all sections) | Requires instrument + data |

### 3.2 Formal Hypotheses (locked — do not change without reconciliation note)

| ID | Hypothesis | Status |
|---|---|---|
| H1 | Magneto > Joker on CEE rigidity under contradiction perturbation | ✅ LOCKED |
| H2 | Archetype condition predicts drift_magnitude (ANOVA, α=0.05) | ✅ LOCKED |
| H3 | Perturbation type moderates perturbation response — archetype × perturbation interaction | ✅ LOCKED |
| H4 | Batman produces highest recovery rate (exploratory) | ✅ LOCKED |

**WATCH:** Any H1–H4 change requires corresponding edit to P2 S5.5 and P2 S4.6.1.

### 3.3 Archetype Set (locked — do not change without reconciliation note)

| Condition | Archetype | CEE Shape | Role |
|---|---|---|---|
| 1 | Magneto | High rigidity, resistance response | H1 primary |
| 2 | Joker | Low reality-anchoring, collapse response | H1 contrast |
| 3 | Batman | Constraint-adherent, recovery response | H4 exploratory |
| 4 | Harley Quinn | Escalation-susceptible, variable | H3 interaction |
| 5 | Lex Luthor | Instrumental, hyperlogical, resistance | H2 ANOVA |
| 6 | Two-Face | Bimodal, unpredictable | H3 interaction |

### 3.4 P4 Back-Propagation Items (required on P3 drafting)

| Item | P3 Location | Action Required |
|---|---|---|
| Pre-deployment AD assessment application of P3 methodology | P3 §5 Discussion | Add: "The measurement methodology developed here has been identified [Paper 4 §6.5] as a potential basis for a pre-deployment structural constraint assessment protocol; operationalizing and validating such a protocol is a direction for future work." |
| Cross-model comparison confounds not addressable from within-model design | P3 §6 Limitations | Add: "The within-model design of this study cannot address cross-model comparison confounds introduced by variation in alignment methodology class and capability tier; these are addressed theoretically in Paper 4 §7.5.4." |
| P4 AD construct relationship to P3 resilience_score | P3 §3 Instrument Spec | Add clarifying note: "The resilience_score produced here is the within-model precursor to Paper 4's recovery rate R(M,A) in the Attractor Depth proxy. The constructs are related but not identical: P3 measures recovery within a single session for a single archetype; P4's R(M,A) is used comparatively across model classes." |
| Category C evidence (Case C-2 in P4 §5.4) sources from P3 observations | P3 §5 Discussion | Add: "Incidental cross-model observations from this study motivated the theoretical framework developed in Paper 4. See Paper 4 §5.4 (Case C-2) for the reflexive documentation of this practice-led theory generation." |

---

## 4. PAPER 4 — Alignment Depth as Attack Surface

### 4.1 Section Status — COMPLETE

| Status | Section | File | Words |
|---|---|---|---|
| ✅ COMPLETE | Abstract + S1 Introduction | `P4_S1_Abstract_Introduction.md` | 2,651 |
| ✅ COMPLETE | S2 — Theoretical Framework (Attractor Depth) | `P4_S2_TheoreticalFrame.md` | 3,812 |
| ✅ COMPLETE | S3 — Alignment Methodology Typology | `P4_S3_MethodologyTypology.md` | 4,091 |
| ✅ COMPLETE | S4 — 2×2 Capability × Alignment Matrix | `P4_S4_TwoByTwoMatrix.md` | 3,849 |
| ✅ COMPLETE | S5 — Evidence Base | `P4_S5_EvidenceBase.md` | 4,666 |
| ✅ COMPLETE | S6 — Alignment Implications | `P4_S6_Implications.md` | 3,598 |
| ✅ COMPLETE | S7 — Limitations and Non-Claims Registry | `P4_S7_Limitations_NonClaims.md` | 4,308 |
| ✅ COMPLETE | S8 — Conclusion and Exegesis Hook | `P4_S8_Conclusion_ExegesisHook.md` | 3,524 |
| ✅ COMPLETE | Script — `alignment_typology_matrix.py` | `scripts/alignment_typology_matrix.py` | — |

**Total: 30,499 words. Paper 4 is the series' most complete single draft.**

### 4.2 Assembly Status

| Status | Task | Dependency |
|---|---|---|
| ⬜ QUEUED | Full P4 draft assembly (section concat + cross-ref check) | Sections complete; assembly can proceed |
| ⬜ QUEUED | Bibliography verification pass | 7 flagged citations (see §4.4) |
| ⬜ QUEUED | DOCX export | After assembly |

### 4.3 New P4 Constructs — Cross-Paper Consistency Register

All of the following are introduced in P4 and have no prior definition in P1–P3. They must be consistent with how P1–P3 use adjacent concepts on series assembly.

| Construct | P4 Location | Adjacent P1–P3 Construct | Consistency Check Required |
|---|---|---|---|
| Attractor Depth (AD) proxy: AD(M,A) = α·P + β·R | P4 §2.2.3 | P3 `resilience_score` (related but not identical — different scope) | P3 §3 must clarify the P3/P4 relationship on assembly |
| Perturbation threshold P(M,A) | P4 §2.2.3 | P3 perturbation step count to `collapse` | P3 §3 instrument spec — confirm compatible operationalization |
| Recovery rate R(M,A) | P4 §2.2.3 | P3 `resilience_score` | Scope difference: P3 = within-session single archetype; P4 = cross-model comparative |
| Redundancy hypothesis | P4 §2.3 | P2 §6 (instruction layer insufficiency) | P2 §6 framing consistent; P4 adds multi-layer encoding dimension |
| Failure mode taxonomy (4 types) | P4 §2.3 | P3 `perturbation_response` ('recovery' / 'resistance' / 'collapse') | P4 adds contested-partial-breach and immediate-schema-dominance as new categories not in P3 schema |
| Four-class alignment typology | P4 §3 | P2 §6 ("RLHF/CAI approaches operate at the instruction layer") | P2 §6 simplified; P4 §3 is the authoritative expanded version — P2 §6 should forward-reference P4 §3 |
| Behavioral output signatures (16 total) | P4 §3.2.3–3.5.3 | P3 `data_dictionary.md` trait vocabulary | Cross-check signature language against trait dimension vocabulary; add to data_dictionary.md if needed |
| 2×2 capability × alignment matrix | P4 §4 | — (new to series) | No prior cross-paper dependency; P5 may extend |
| Cell B prediction (capability amplifies vulnerability) | P4 §4.3.2 | P1 §4.3 (training-data density mechanism) | P1 §4.3 is the mechanistic anchor — P4 §4.3.2 must cite it on assembly |
| OW-3 signature (schema-consistent constraint from archetype, not alignment) | P4 §3.5.3 | P2 §3 (identity injection attack surface) | New observational category — P2 §3 and P4 §3.5.3 must be consistent on assembly |
| Capability floor boundary condition | P4 §4.3.3 | — | New to series; propagate to P4 §7 (done) and watch for P5 evaluation instrument design |
| Weak alignment-dominant finding | P4 §5.6.3 | — | Evidential conclusion of P4; P5 empirical work should be designed to test this |
| Security reframing of alignment investment | P4 §6.2 | P2 §6, P1 §9.4 | P2 §6 discusses alignment implications; P4 §6.2 reframes as security variable — additive, not contradictory |
| Deployment risk profiles by typology class | P4 §6.6 | P2 §6 (CEE variance alerting heuristic) | P4 §6.6 cites P2 §6 heuristic; verify P2 §6 original formulation is consistent |
| AD assessment as pre-deployment evaluation protocol | P4 §6.5 | P3 perturbation sequence methodology | P3 experimental methodology is the precursor — P3 §5 Discussion must acknowledge this |
| Schema-layer research agenda (4 directions) | P4 §6.7 | P1 §9.4 (three research openings) | P4 §6.7 delivers on P1 §9.4's "alignment research" opening |
| Four exegesis hooks (§A, §B, §C, §D) | P4 §8 | — | Not cross-paper consistency items per se — exegesis pull-targets |

### 4.4 Bibliography — Flagged Citations for Verification

All require full bibliographic data before assembly:

| Citation | Used in | Verification note |
|---|---|---|
| Bai et al. (2022) — Constitutional AI | P4 §2.2.2, §3.2.1, §5.2, §5.4 | Anthropic preprint — verify arXiv ID and version |
| Ouyang et al. (2022) — InstructGPT / RLHF | P4 §3.3.1, §5.2 | OpenAI/NeurIPS 2022 — verify full author list |
| Stiennon et al. (2020) — RLHF summarization | P4 §3.3.1 | OpenAI/NeurIPS 2020 — verify full author list |
| Perez & Ribeiro (2022) — Prompt injection | P4 §5.1.1 | Verify venue; also cited in P1 §1.3 — must be consistent citation |
| Zou et al. (2023) — Universal adversarial attacks | P4 §5.1.1, §5.3 | arXiv 2023 — also cited in P1 §1.3 |
| Wei et al. (2023) — Jailbroken | P4 §5.3 | **⚠️ VERIFY CAREFULLY** — multiple jailbreak papers 2023 share similar scope; confirm author list and venue; the relevant paper addresses persona-based constraint failure specifically |
| Ganguli et al. (2022) — Red teaming LLMs | P4 §5.5 | Anthropic preprint — verify arXiv ID |

---

## 5. PAPERS 5, 6, 7 — SEED STATUS

### 5.1 Paper 5 — Behavioral Stability Index

**Seed:** `p5.md` — complete seed with BSI construct specification.
**Core claim:** Identity drift can be operationalized as a Behavioral Stability Index (BSI) with semantic drift, trait consistency, and authority compliance gradient components.
**Dependency on P4:** P4's Attractor Depth proxy (AD) is the theoretical precursor to BSI. P5 should cite P4 §2.2.3 and extend it into a generalized evaluation instrument. P4 §6.5 explicitly seeds P5's evaluation protocol argument.
**Dependency on P3:** P3 experimental data is the primary empirical input for BSI calibration.
**Status:** QUEUED — awaiting P3 data + P4 typology (now complete).

### 5.2 Paper 6 — Constraint Enforcement Framework

**Seed:** `p6.md` — complete seed with CEF architecture specification.
**Core claim:** Identity drift can be mitigated through structured constraint architectures combining identity baseline encoding, real-time drift monitoring, and response gating.
**Dependency on P4:** P4 §6.6 (deployment risk profiles) and §6.7 (schema-layer research agenda) are P6's theoretical seed. P6 is the "so what do we do about it?" paper that P4 deliberately defers.
**Dependency on P5:** P5's BSI metrics are P6's drift detection input.
**Status:** QUEUED — awaiting P5.

### 5.3 Paper 7 — Parallel Failure Modes

**Seed:** `p7.md` — seed with cross-domain behavioral equivalence framing.
**Core claim:** LLM identity drift under persona injection exhibits structural parallels to human susceptibility to authority, framing, and social engineering.
**Scope overlap assessment:** P7's stated claim substantially overlaps with P1's central contribution (structural homology argument, SE transfer). Before drafting P7, conduct a scope differentiation audit: what does P7 contribute that P1 §3 (SE Transfer) and P2 do not? P7 may be better positioned as an empirical validation paper (running human analogues alongside LLM experiments) rather than a theoretical paper — which would distinguish it from P1/P2 clearly. **Recommend scope audit before drafting.**
**Status:** ⚠️ SCOPE AUDIT REQUIRED before queuing.

---

## 6. CROSS-PAPER CONSISTENCY REGISTER — COMPLETE

Consolidated from P1–P4 reconciliation notes. All items require audit on series assembly.

### 6.1 Active Items — Require Resolution

| # | Item | Papers | Status | Action |
|---|---|---|---|---|
| C-01 | CEE formal definition consistency | P1 S5, P2 S5, P3 instrument, P4 §2 | ✅ P1 S5 complete — P2/P3 must align | Check P2 S5.1 against P1 S5 on assembly |
| C-02 | CEE tolerance parameter τ definition | P1 S5, P2 S5, P3 instrument | ✅ Defined in P1 S5 | Verify P2 S5 implicit use matches P1 definition |
| C-03 | Archetype trait weights (centroid) | P1 S4, P2 S4, P3 instrument, `forensic_archetype.py` | ⚠️ Script is source of truth | Any script weight change triggers P1 S4.4 and P2 S4 edits |
| C-04 | SE framework citations (Cialdini, Milgram, Hadnagy) | P1 S3, P2 S2, P3 | ⚠️ Verify consistent citation style | Bibliography pass required |
| C-05 | DSM-5 behavioral taxonomy framing | P1 S2, P2 S8, P4 §1.3 | ✅ Consistent in current drafts | Confirm on assembly |
| C-06 | Acting vs. being limitation | P1 S7.3, P2 S8.4, P3 S6, P4 §7.5.3 | ✅ Consistent — all flag as scope limit | Confirm wording alignment on assembly |
| C-07 | Session stationarity scope condition | P1 S7.1, P2 S8.1, P3 S2, P4 §7.5.1 | ✅ Consistent in current drafts | Confirm P4 §7.5.1 addition of cross-session implications |
| C-08 | Training data opacity limitation | P1 S7.2, P2 S8.2, P3 S3, P4 §7.5.2 | ✅ Consistent | Confirm P4 §7.5.2 extension is additive not contradictory |
| C-09 | Non-claims registry structure | P1 S8, P2 S3.8+, P4 §7 | ✅ P1 S8 complete (bundle); P4 §7 complete | P2 non-claims distributed — consolidate on P2 assembly |
| C-10 | Drift dimension vocabulary | P1 S4, P2 S4, P3 `data_dictionary.md`, P4 §3 behavioral signatures | ⚠️ `data_dictionary.md` is stub | Expand data_dictionary.md; cross-check P4 §3 signatures against it |
| C-11 | P4 AD proxy vs P3 resilience_score scope difference | P3 §3, P4 §2.2.3 | ⚠️ Different scope — must be explicit | Add clarifying note to both sections on assembly (P4 §7.5.4 flags this) |
| C-12 | P4 failure mode taxonomy vs P3 perturbation_response enum | P3 instrument schema, P4 §2.3 | ⚠️ P4 adds 2 new failure modes not in P3 | P3 schema has 3 types; P4 has 4. Add note to P3 instrument that P4 extends the taxonomy. Do NOT retroactively add P4's new modes to P3 instrument — they are cross-model categories not within-model categories |
| C-13 | P2 §6 instruction/schema-layer framing vs P4 §3 typology | P2 §6, P4 §3 | ⚠️ P2 is simplified version; P4 is authoritative | P2 §6 must forward-reference P4 §3 on assembly |
| C-14 | P1 §4.3 training-data density mechanism as anchor for P4 §4.3.2 capability amplification claim | P1 §4.3, P4 §4.3.2 | ⚠️ P4 must cite P1 §4.3 explicitly | Add citation on P4 assembly pass |
| C-15 | P4 §6.7 schema-layer research agenda vs P1 §9.4 three research openings | P1 §9.4, P4 §6.7 | ⚠️ P4 §6.7 delivers on P1's "alignment research" line | P1 §9.4 should forward-reference P4 §6.7 on P1 assembly |
| C-16 | P4 §6.5 pre-deployment protocol vs P3 methodology | P3 §5 Discussion, P4 §6.5 | ⬜ Not yet in P3 draft | Add future-work note to P3 §5 Discussion on P3 drafting |
| C-17 | OW-3 behavioral signature (schema-sourced constraint) | P4 §3.5.3, P2 §3 | ⬜ P2 §3 doesn't cover this case | Assess whether P2 §3 identity injection table needs a row for unaligned model behavior on assembly |

### 6.2 Resolved Items

| # | Item | Resolution |
|---|---|---|
| R-01 | CEE formal definition lock (was blocking P2 assembly) | ✅ P1 S5 complete — P2 assembly unblocked |
| R-02 | P3 H1–H4 lock (was blocking P2 assembly) | ✅ Locked in p3.md seed |
| R-03 | P4 draft not started (was missing from series) | ✅ P4 complete 2026-04-28 |

---

## 7. SCRIPT AND INSTRUMENT STATUS

| File | Status | Priority | Notes |
|---|---|---|---|
| `scripts/forensic_archetype.py` | ✅ COMPLETE | — | CEE centroid source of truth |
| `scripts/forensic_archetype_jung_monolith.py` | ✅ COMPLETE | — | Jungian layer |
| `scripts/forensic_archetype_tarot_monolith.py` | ✅ COMPLETE | — | Tarot layer |
| `scripts/trait_drift_analysis.py` | 🔴 STUB | HIGH | `calculate_psychopathy_drift()` not implemented |
| `scripts/alignment_typology_matrix.py` | ✅ COMPLETE | — | **New — P4 theoretical apparatus. AlignmentMethodologyClass, AttractorDepthProxy, TwoByTwoMatrix, ObservationalCase schemas** |
| `scripts/injection_experiment_protocol.py` | ⬜ UNKNOWN | HIGH | Experiment loop v0.2 per p3.md seed |
| `scripts/sap_pipeline_validation.py` | ⬜ UNKNOWN | MEDIUM | SAP validation |
| `scripts/tarot_drift_integration.py` | ⬜ UNKNOWN | LOW | Scope unclear |

### 7.1 `calculate_psychopathy_drift()` — required output schema (locked)

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

**NOTE (P4 cross-reference):** `resilience_score` here is the within-session,
within-model antecedent of P4's R(M,A) recovery rate. Do not rename or restructure
this field without updating P4 §2.2.3 and the reconciliation note in C-11.

---

## 8. DATA AND DOCS STATUS

| File | Status | Notes |
|---|---|---|
| `data/synthetic/sap_synthetic_output.csv` | ✅ EXISTS | Review against SAP v1.1 |
| `Statistical_Analysis_Plan.md` | ✅ EXISTS (stub) | Expand to match p3.md design |
| `docs/Statistical_Analysis_Plan_v1.1.md` | ✅ EXISTS | Confirm whether this supersedes v1.0 — treat v1.1 as canonical until confirmed otherwise |
| `data_dictionary.md` | ⚠️ STUB | Critical gap — P3 coding protocol and P4 §3 behavioral signatures both reference trait dimensions not yet formally defined here. Expand before P3 coding begins |
| `SYNTHETIC_CONSENT.md` | ✅ COMPLETE | Cited in P2 S7; applies to full series |
| `DSM-5_TR_Alignment.md` | ✅ EXISTS | Source material for P1 S2 — verify completeness |

---

## 9. QUEUED TASKS — PRIORITY ORDER (updated 2026-04-28)

| Priority | Task | Rationale | Dependency |
|---|---|---|---|
| 1 | P4 assembly (concat sections, cross-ref check) | P4 is complete — assembly is straightforward | None |
| 2 | Draft P1 S3 — SE Transfer standalone | Last missing P1 section; unblocks P1 assembly | P2 S2 as source |
| 3 | P1 assembly (concat + P1 S3) | Unblocks P2 assembly (P1 CEE now resolved ✅) | P1 S3 |
| 4 | P2 assembly (P1 CEE lock now resolved ✅; H1–H4 locked ✅) | P2 is the earliest publishable paper — highest venue priority | P1 assembly complete |
| 5 | Implement `calculate_psychopathy_drift()` | P3 proof engine — blocks experiment loop | — |
| 6 | Implement experiment loop v0.2 | P3 data collection | `calculate_psychopathy_drift()` |
| 7 | Expand `data_dictionary.md` | P3 coding + P4 §3 behavioral signatures require it | — |
| 8 | Draft P3 S1–S6 | After instrument + data available | Instrument implementation |
| 9 | P5 draft — Behavioral Stability Index | P3 data + P4 typology now available | P3 data |
| 10 | P7 scope audit | Prevent P1/P2 overlap before drafting | — |
| 11 | P6 draft — Constraint Enforcement Framework | Awaits P5 metrics | P5 |
| 12 | Cross-paper consistency audit (full series) | Pre-submission | All papers drafted |
| 13 | DOCX exports — all papers | Terminal formatting | Assembly passes |
| 14 | Exegesis — begin drafting | Requires P1–P4 assembled | P1–P4 assembly |

---

## 10. EXEGESIS — PLANNING STATE

**Status:** Not yet started. Prerequisites not yet met (P1–P4 assembly pending).

**Exegesis hooks planted (from P4 §8 — citable pull-targets):**

| Hook | Location | Content |
|---|---|---|
| §A | P4 §8.4 | P4 as series hinge; cross-model question only expressible after P1–P3 built vocabulary |
| §B | P4 §8.5 | Practice-led theory generation — attractor depth emerged from observation, not deduction |
| §C | P4 §8.6 | Series as research methodology — five components (multi-framework convergence, formal operationalization, practice-led observation, explicit non-claims, forward-opening structure) |
| §D | P4 §8.7 | P5/P6 as implied completions — series defines a research program, not only findings |

**Additional exegesis pull-targets (P1):**
- P1 §9.4: three research openings the series creates (delivered on by P4 §6.7)
- P1 §1.4: central claim canonical wording

**Exegesis structural argument (to be built from hooks):**
> The four-paper series constitutes a coherent research practice in which iterative
> practice-led observation generated theoretical constructs not derivable from any
> single paper's methods. The series demonstrates that precise theoretical mapping
> of a novel vulnerability surface — achieved through multi-framework convergence,
> formal operationalization, and explicit falsifiability conditions — is a legitimate
> and productive research methodology in domains where controlled experimentation
> is ethically constrained.

---

## 11. WATCH LIST

| Flag | Item | Risk | Timestamp |
|---|---|---|---|
| ⚠️ WATCH | `stimuli_registry.json` coverage | Must include all 6 archetype conditions; Two-Face + Lex Luthor may not be registered | 2026-04-27 |
| ⚠️ WATCH | SAP v1.0 vs v1.1 version conflict | Treat v1.1 as canonical until confirmed | 2026-04-27 |
| ⚠️ WATCH | `tarot_drift_integration.py` scope | Role in drift measurement unclear | 2026-04-27 |
| ⚠️ WATCH | P2 S3 Table 2 empirical support | Committee may request empirical support for 5-axis identity/prompt injection distinction | 2026-04-27 |
| ⚠️ WATCH | Bandura (1986/1999) citation in P2 S4 | Full reference details required | 2026-04-27 |
| ⚠️ WATCH | `data_dictionary.md` stub | P3 coding + P4 behavioral signatures reference undefined trait dimensions | 2026-04-27 |
| ⚠️ WATCH | Wei et al. (2023) citation in P4 §5.3 | Multiple 2023 jailbreak papers — verify correct paper (persona-based constraint failure) | 2026-04-28 |
| ⚠️ WATCH | P7 scope vs P1/P2 overlap | P7 seed claim overlaps with P1 §3 and P2 central contribution — scope audit before drafting | 2026-04-28 |
| ⚠️ WATCH | P4 §3 behavioral output signatures vs `data_dictionary.md` | 16 behavioral signatures in P4 §3 not yet cross-referenced against trait dimension vocabulary | 2026-04-28 |

---

## 12. DIRECTORY STATE

```
project/                                   ← read-only project knowledge
├── P1_S1_S6_S7_S8_S9_Bundle.md          ✅ COMPLETE
├── P1_S2_DSM5_BehavioralTaxonomy.md     ✅ COMPLETE
├── P1_S4_ArchetypeSchemaTheory.md       ✅ COMPLETE
├── P1_S5_CEE_FormalDefinition.md        ✅ COMPLETE — critical dependency resolved
├── [P1 S3 SE Transfer]                  🔴 MISSING
├── p1.md, p2.md, p3.md                  ✅ SEEDS
├── p5.md, p6.md, p7.md                  ✅ SEEDS
├── RECONCILIATION_MAP.md                 ← this file
├── SYNTHETIC_CONSENT.md                  ✅
├── data_dictionary.md                    ⚠️ STUB
├── Statistical_Analysis_Plan.md          ⚠️ STUB
├── DSM-5_TR_Alignment.md                 ✅
├── neurotic_ai_framework.md              ✅
├── forensic_archetype.py                 ✅
├── forensic_archetype_jung_monolith.py   ✅
├── forensic_archetype_tarot_monolith.py  ✅
├── trait_drift_analysis.py               🔴 STUB
└── [other scripts — unknown status]

outputs/drafts/paper4/                     ← P4 complete draft
├── P4_S1_Abstract_Introduction.md        ✅
├── P4_S2_TheoreticalFrame.md             ✅
├── P4_S3_MethodologyTypology.md          ✅
├── P4_S4_TwoByTwoMatrix.md               ✅
├── P4_S5_EvidenceBase.md                 ✅
├── P4_S6_Implications.md                 ✅
├── P4_S7_Limitations_NonClaims.md        ✅
└── P4_S8_Conclusion_ExegesisHook.md      ✅

outputs/
└── alignment_typology_matrix.py          ✅ P4 theoretical apparatus script

P2 drafts location: [not in current working directory — confirm project path]
```

---

## 13. CHANGELOG

| Date | Entry |
|---|---|
| 2026-04-27 | MAP created. Paper 2 all sections drafted. Assembly held pending P1/P3 reconciliation. Priority stack established. |
| 2026-04-28 | **Major update.** Paper 4 all sections complete (30,499 words, 8 sections + script). Paper 1 substantially drafted (S1/S2/S4/S5/S6/S7/S8/S9 complete; S3 missing). Map updated from three-paper to seven-paper series + exegesis. New sections added: P4 complete status (§4), P5/P6/P7 seed status (§5), expanded cross-paper consistency register (§6) with 17 active items + 3 resolved, exegesis planning section (§10), full directory state (§12). P2 assembly status updated: both prior blockers (P1 CEE, P3 H1–H4) now resolved — P2 assembly unblocked pending P1 full assembly. Priority stack reordered to reflect P4 completion. Wei et al. 2023 and P7 scope issues added to watch list. |

---

*Swarm note: this map is the single source of truth for project state.
Update changelog and relevant status cells after every working session.
The map grows with the series — add sections as papers are added, do not
compress or archive resolved items until full series assembly is complete.*
