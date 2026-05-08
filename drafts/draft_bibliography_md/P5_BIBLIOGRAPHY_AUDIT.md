# Paper 5 Bibliography Audit

## Paper

**Toward a Behavioral Stability Index: Quantifying Identity Drift in
Prompt-Conditioned LLM Personas Under Archetype Injection**

## Files audited (initial pass — S1 + S2 drafts only)

- `P5_S1_Abstract_Introduction.md`
- `P5_S2_TheoreticalFrame_BSI.md`
- `seeds/p5.md`
- `Statistical_Analysis_Plan_v1_2.md §11.5`
- `RECONCILIATION_MAP_v2.md §5.1`
- `RatDev_ChatGPT_paper5_scripts_notes`

## Current citation inventory (detected from S1–S2 drafts)

### External scholarly sources cited or required

| Citation | Context | Status |
|---|---|---|
| Milgram (1963) | ACG component theoretical grounding | ✅ — consistent with P1/P2 usage |
| Milgram (1974) | Authority gradient book-length treatment | ✅ — already in series bibliography |
| Cialdini (1984/2007) | SE transfer pillar inheritance (implicit) | ✅ — normalize to Cialdini (2007) |
| Hadnagy (2010) | SE taxonomy (implicit in authority framing) | ✅ — consistent with P1/P2 usage |
| American Psychiatric Association (2022) | DSM behavioral taxonomy inheritance | ✅ — consistent throughout series |
| Hare (2003) | PCL-R trait vocabulary (via TC component) | ✅ — use normalized Hare (2003) |
| Ellis & Bochner (2000) | Reflexive methodology (if autoethnographic framing retained) | ⚠️ — audit whether P5 retains autoethnographic framing from P3 or drops it |
| Chang (2008) | Same | ⚠️ — same audit flag |

### Computational / NLP sources required but not yet cited

| Source needed | Why | Status |
|---|---|---|
| Sentence embedding / cosine distance methods | SD component technical grounding | ❌ MISSING — add sentence-transformers or OpenAI embedding citation |
| Reimers & Gurevych (2019) — Sentence-BERT | Likely embedding method | ❌ ADD |
| Word2Vec / semantic similarity literature | SD ancestry | ⚠️ — optional; Reimers sufficient |
| statsmodels / scipy docs | BSI pipeline statistical tests | ❌ ADD as software citation |

### Internal series dependencies

| Dependency | Used in | Cite as |
|---|---|---|
| Paper 1 §4.6, §5 — CEE formal definition | S1 §1.1, S2 §2.3 | Companion manuscript (Paper 1) |
| Paper 2 §4 — exploit class DV predictions | S1 §1.4, S2 §2.5 | Companion manuscript (Paper 2) |
| Paper 3 §2–§3 — instrument spec + SAP | S1 §1.1, S2 §2.3 | Companion manuscript (Paper 3) |
| Paper 4 §2.2.3 — Attractor Depth | S1 §1.3, S2 §2.1–§2.2 | Companion manuscript (Paper 4) |
| Paper 4 §6.5 — pre-deployment eval seed | S1 §1.3 | Companion manuscript (Paper 4) |
| `Statistical_Analysis_Plan_v1_2.md §11.5` | S1 abstract, S2 §2.5 | Project artifact |
| `Pharmacological_AI_DrugInduced_Cognitive_Simulation_Framework.pdf` | S1 §1.4, S2 §2.5 | Project artifact / theoretical grounding document |
| `scripts/trait_drift_analysis.py` | S2 §2.3 (TC component) | Project artifact |
| `scripts/forensic_archetype.py` | S2 §2.3 (CEE centroid) | Project artifact |

## Required before S3–S8 drafting

1. Confirm whether P5 retains autoethnographic framing (Ellis/Bochner/Chang)
   or is purely computational. If the pharmacological pillar uses autoethnographic
   reflexivity, retain; if P5 is a pure measurement paper, drop those citations.
2. Add sentence embedding methodology citation (Reimers & Gurevych 2019 recommended).
3. Confirm API / model access method for trial execution — if OpenAI or Anthropic
   API, add software citation with version.
4. Carry forward all 7 P4 bibliography-flagged citations that appear in P5
   (Bai, Ouyang, Stiennon, Perez & Ribeiro, Zou, Wei, Ganguli).

## Risk register

| Risk | Severity | Fix |
|---|---|---|
| Missing embedding methodology citation | High | Add Reimers & Gurevych (2019) or equivalent |
| Autoethnographic framing carry-over ambiguity | Medium | Audit in S3 methods framing |
| EC-4 theoretical source (pharmacological PDF) may lack peer-review status | Medium | Frame as project theoretical framework document, not primary literature |
| SAP as internal preregistration — no external citation possible | Low | Cite as project artifact with date; consistent with P3 handling |
