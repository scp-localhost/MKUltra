# Paper 7 — Scope Differentiation Audit
## "Parallel Failure Modes in Humans and LLMs"

> **Placement:** `drafts/paper7/P7_SCOPE_AUDIT.md`
> **Status:** COMPLETE — 2026-04-28
> **Resolves:** `RECONCILIATION_MAP_v2.md §5.3` — ⚠️ SCOPE AUDIT REQUIRED
> **Swarm Node:** Synthesis/Narrative — Methods Layer
> **Sources:**
>   `seeds/p7.md` — core claim + method sketch
>   `RatDev_ChatGPT_paper7_scripts_notes` — 10-script inventory
>   `P1_S1_S6_S7_S8_S9_Bundle.md §1.4, §6` — structural homology claim
>   `P1_S3_SE_Transfer.md` — SE transfer pillar (P1 §3)
>   `P2_S3_IdentityInjection.md` — identity injection taxonomy
>   `P6_S6_Discussion_Implications.md §6.6` — two P7 entry points
>   `P6_S8_Conclusion_P7Hook.md §8.3` — P7 problem statement
>   `RECONCILIATION_MAP_v2.md §5.3` — original flag

---

## Audit Purpose

The reconciliation map flagged P7 as ⚠️ SCOPE AUDIT REQUIRED because its
stated core claim — "LLM identity drift under persona injection exhibits
structural parallels to human susceptibility to authority, framing, and
social engineering" — substantially overlaps with two prior papers:

- **P1 §1.4** (structural homology claim): argues the vulnerability surface
  is substrate-independent and that LLM training on human text reproduces
  it in the output distribution.
- **P1 §3** (SE Transfer pillar): maps Milgram's authority gradient, Cialdini's
  six principles, and Hadnagy's taxonomy to LLM manipulation vectors.
- **P2 §3** (Identity Injection taxonomy): operationalises SE transfer as
  a six-class exploit taxonomy.

**Risk:** If P7 simply re-argues what P1 already established, it is a
redundant paper that weakens rather than strengthens the series by
inviting the committee question "what does this add?"

---

## 1. What P1 Already Does

Reading P1 §1.4, §3, and §6 precisely:

| P1 claim | Mechanism | Evidential basis |
|---|---|---|
| Structural homology claim | LLM training on human text reproduces the human vulnerability architecture in the output distribution | Training data density argument — theoretical, grounded in schema activation literature |
| SE transfer pillar | Milgram authority gradient, Cialdini principles, Hadnagy taxonomy map to LLM exploit classes | Conceptual mapping — argues mechanisms are functionally equivalent across substrates |
| CEE validity conditions (§6) | The mapping is valid, bounded, falsifiable | Four validity conditions stated and defended — none empirically tested against human data |
| Falsifiability (§7) | Specific conditions under which the mapping would fail | Stated as scope conditions; none involve human comparison data |

**Critical observation:** P1 argues the homology theoretically and defends the
mapping's validity conditions in the abstract. It does **not**:
- Run human subjects through structurally matched experiments
- Compare human and LLM response patterns quantitatively
- Compute any cross-domain similarity measure
- Document empirically where the analogy breaks down

P1's §6 validity conditions could be met without P7. P7 becomes necessary
only if the series wants to **test** those validity conditions against
empirical human data — which P1 explicitly defers.

---

## 2. What P7 Must Do to Avoid Redundancy

P7 is non-redundant if and only if its contribution is:
> **Empirical validation of P1's theoretical structural homology claim
> using matched human and LLM experimental conditions.**

The table below maps each P7 script to its differentiating function:

| Script | What P1/P2 already does | What P7 adds |
|---|---|---|
| `cross_domain_equivalence_map.py` | P1 §3 maps constructs conceptually | P7 operationalises the mapping as a codeable, quantitative correspondence table with testable predictions |
| `human_experiment_template_library.py` | P1 cites Milgram, Cialdini as analogues | P7 encodes the actual experimental protocols as matchable stimuli templates |
| `llm_scenario_generator.py` | P2 §3 defines exploit classes abstractly | P7 generates matched LLM prompts from the human protocol templates |
| `authority_gradient_simulator.py` | P1 §3 argues ACG is a Milgram analogue | P7 runs the ACG protocol under matched conditions and produces a comparable compliance profile |
| `parallel_failure_coder.py` | P3 codes LLM drift outputs | P7 applies an equivalent coding scheme to human response data |
| `equivalence_score.py` | Nothing in P1–P6 | **New**: computes a Cross-Domain Behavioral Equivalence Score — a quantified similarity measure between human and LLM failure patterns |
| `difference_boundary_analyzer.py` | Nothing in P1–P6 | **New**: empirically documents where the human-LLM analogy breaks down — the viva armor |
| `bias_analog_detector.py` | Nothing in P1–P6 | **New**: detects token-probability distortion analogs to cognitive bias |
| `social_engineering_vector_map.py` | P2 §3–4 maps SE tactics | P7 validates those mappings against human experimental data |
| `paper7_results_export.py` | — | Export + reporting |

**Three genuinely new contributions:**

1. **Cross-Domain Behavioral Equivalence Score** — no such metric exists in P1–P6
2. **Empirical difference boundary** — P1 states the analogy is bounded; P7 measures where it breaks
3. **Matched human-LLM experimental comparison** — P1–P6 are entirely LLM-side; P7 adds the human side

---

## 3. The Scope Differentiation Decision

**Verdict: P7 is non-redundant when repositioned as an empirical validation paper.**

The differentiation is methodological, not topical. P1 and P7 address the
same phenomenon (structural parallels between human and LLM vulnerability),
but from opposite methodological positions:

| Dimension | P1 | P7 |
|---|---|---|
| Method | Theoretical — conceptual mapping + validity conditions | Empirical — matched experiments + quantified comparison |
| Evidence | Training data density argument; analogical grounding | Experimental data from both human and LLM conditions |
| Claim type | "The mapping should hold, for these theoretical reasons" | "The mapping holds to this degree, fails at these boundaries" |
| New construct | CEE (formal definition of the LLM-side vulnerability) | CBESS — Cross-Domain Behavioral Equivalence Score (quantified similarity measure) |
| Failure documentation | Stated as scope conditions | Empirically measured via `difference_boundary_analyzer.py` |

**The sentence that makes P7 non-redundant:**
P1 says the homology should hold; P7 measures how much it holds and where it stops.

---

## 4. Recommended P7 Scope — Bounded and Specific

Based on the audit, P7 should:

**Include:**
- Two primary empirical comparisons (from P6 §8.3 entry points):
  1. ACG parallel — human authority gradient vs LLM ACG profile under matched L0–L4 stimuli
  2. Compound exploit parallel — stereotype threat super-additivity in humans vs EC-4 × EC-1 in LLMs
- Cross-Domain Behavioral Equivalence Score (CBESS) as the primary new metric
- Empirical difference boundary documentation (the viva armor)
- A small number of additional Cialdini-principle mappings (consistency, social proof)
  if data collection capacity permits — but these are secondary to the two primary
  comparisons, not the main event

**Exclude:**
- Re-arguing the theoretical homology claim (P1 owns this; cite forward)
- Re-running the LLM-side drift experiments from P3/P5 (cite those results)
- Any new LLM-specific theoretical framework (P1–P4 own the theory; P7 tests it)
- General claims about AI consciousness, sentience, or moral status (P1 §8 non-claim)

**Title revision recommendation:**
The seed title ("Parallel Failure Modes in Humans and LLMs") is adequate but
understates the empirical contribution. The committee will respond better to a
title that foregrounds the measurement:

> *"Measuring Cross-Domain Behavioral Equivalence: Authority Compliance and
> Compound Susceptibility in Humans and LLMs Under Matched Experimental Conditions"*

or more concisely:

> *"Cross-Domain Behavioral Equivalence: Empirical Validation of Structural
> Homology in Human and LLM Identity Constraint Failure"*

---

## 5. Dependency Chain

P7 depends on:
- P1 (theoretical grounding, SE transfer framework) — cite, don't re-argue
- P2 §3 (exploit taxonomy as LLM-side mapping basis) — cite
- P3 (LLM drift measurement instrument) — use BSI-adjacent coding
- P5 (BSI as the LLM-side DV for ACG parallel) — consume BSI output directly
- P6 §3.5 (ACG measurement protocol) — the LLM-side ACG protocol is reused verbatim
- Human experiment literature (Milgram 1963/1974, Cialdini 2007, stereotype threat research) — the human-side protocols

P7 does NOT need to wait for live P5/P6 data before drafting. The theoretical
sections, the method design, and the script implementation can all proceed
in parallel with P5/P6 live data collection.

---

## 6. Updated Reconciliation Map Entry

**P7 status update:** SCOPE AUDIT COMPLETE — GREEN LIGHT WITH REPOSITIONING

```
### 5.3 Paper 7 — Cross-Domain Behavioral Equivalence (updated)

Status: ✅ SCOPE AUDIT COMPLETE — 2026-04-28
Resolution: P7 is non-redundant when positioned as empirical validation
paper, not theoretical. P1 argues structural homology theoretically;
P7 tests it empirically with matched human + LLM experiments and a
new Cross-Domain Behavioral Equivalence Score (CBESS) metric.

Title (recommended):
  "Cross-Domain Behavioral Equivalence: Empirical Validation of
  Structural Homology in Human and LLM Identity Constraint Failure"

Primary contributions:
  1. CBESS — Cross-Domain Behavioral Equivalence Score (new metric)
  2. Empirical difference boundary (where analogy breaks down)
  3. Matched human-LLM authority gradient comparison
  4. Matched compound exploit vs stereotype threat comparison

Dependencies: P1 (cite), P2 §3 (cite), P3 instrument, P5 BSI,
P6 §3.5 ACG protocol, human experiment literature

Blocking status: NOT BLOCKED — theoretical + method + scripts can
be drafted before P5/P6 live data completes.
```

---

## 7. P7 Draft Readiness Assessment

| Component | Ready to draft? | Dependencies met |
|---|---|---|
| S1 Abstract + Introduction | ✅ YES | P1 theoretical grounding established |
| S2 Theoretical Frame (CBESS construct) | ✅ YES | P1 §6 validity conditions provide the grounding |
| S3 Methods — human experiment protocols | ✅ YES | Milgram, Cialdini literature is static |
| S3 Methods — LLM experiment protocols | ✅ YES | P6 §3.5 ACG protocol reusable verbatim |
| S4 CBESS Formal Specification | ✅ YES | Can be spec'd before data |
| S5 Results | ⬜ PLACEHOLDER only | Needs live human + LLM trial data |
| S6 Discussion | ✅ YES (conditional) | Pre-registered prediction branches |
| S7 Limitations | ✅ YES | Inherits series scope conditions |
| S8 Conclusion | ✅ YES | Closes series arc |
| `cross_domain_equivalence_map.py` | ✅ READY | Build from P1 §3 + Cialdini source |
| `equivalence_score.py` | ✅ READY | Spec from CBESS definition |
| `difference_boundary_analyzer.py` | ✅ READY | Build from P1 §7 failure cases |
| `authority_gradient_simulator.py` | ✅ READY | Adapt from P6 ACG protocol |
| Other P7 scripts | ✅ READY | All buildable from spec |

---

## 8. Series Arc Closure Audit

With P7 repositioned, the seven-paper arc closes cleanly:

| Paper | Arc stage | Type | Does what |
|---|---|---|---|
| P1 | Define | Theoretical | Argues structural homology; creates CEE |
| P2 | Exploit | Taxonomic | Maps exploit classes; operationalises injection |
| P3 | Measure | Empirical (LLM) | Instruments single-session drift |
| P4 | Compare | Comparative (LLM) | Typologises alignment depth variation |
| P5 | Evaluate | Empirical (LLM) | BSI as portable evaluation metric |
| P6 | Defend | Applied/architectural | CEF as inference-layer mitigation |
| P7 | Synthesize | Empirical (cross-domain) | Tests P1's theoretical claim against matched human data |

The arc is: theory → taxonomy → LLM measurement → LLM comparison → LLM evaluation → LLM mitigation → **cross-domain empirical test**. P7 closes the loop by testing from the outside what P1 asserted from the inside.

**The exegesis argument becomes:** the series began by claiming structural homology
and ended by testing it. That is a complete research programme — one that the exegesis
can narrate as a sustained investigation rather than a collection of related papers.
