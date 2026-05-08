# Series Bibliography Reconciliation

## Scope

This audit covers the four-paper draft set present in `/mnt/data`:

- Paper 1: `P1_*` markdown sections.
- Paper 2: `P2_*` markdown sections plus legacy `Paper2_Section4_ExploitTaxonomy.md` and `Paper2_Section5_CEE_Operational.md` where relevant.
- Paper 3: `P3_*` markdown sections.
- Paper 4: `P4_*` markdown sections.

## Global citation normalization rules

1. Use APA 7 or IEEE consistently per target venue. Current drafts mix author-date prose, numbered placeholders, and code/document references. For TDSC/IEEE submission, convert author-date citations to numbered IEEE bracket style after final assembly. For doctoral/exegesis review, APA 7 is easier to inspect.
2. Treat code files as project artifacts, not external scholarly sources. Cite them in-text as `Author project artifact, year/version` or in an appendix/source-artifact section, not as normal peer-reviewed literature.
3. Treat DSM-5-TR and PCL-R as restricted/proprietary manuals. Cite the manuals, but avoid reproducing criteria or scoring items beyond fair-use paraphrase.
4. Do not cite `[REF-CODE]` in a paper draft. Replace with artifact citations such as `forensic_archetype_jung_monolith.py`, `trait_drift_analysis.py`, or an appendix entry.
5. Use one date per source. Do not use split dates like `Hare (1991/2003)` unless the text explicitly compares editions.

## Cross-paper issues requiring correction

### 1. Hadnagy date inconsistency

- Found as `Hadnagy (2010)` in multiple paper sections.
- Found as `Hadnagy (2011)` in the methods chapter/docx snippets.
- Recommended correction: standardize to `Hadnagy (2011)` for the Wiley book *Social Engineering: The Art of Human Hacking*.
- If the author intentionally uses a 2010 copyright date, add a note and keep it consistent; otherwise use 2011.

### 2. Perez & Ribeiro / Perez et al. citation form

- Current text uses `Perez & Ribeiro (2022)` for *Ignore Previous Prompt*.
- Recommended reference form: `Perez, F., & Ribeiro, I. (2022). Ignore previous prompt: Attack techniques for language models. arXiv:2211.09527.`
- For IEEE style, cite as `F. Perez and I. Ribeiro, ...`.

### 3. Greshake et al. title

- The stable arXiv title is *Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection*.
- Earlier title variants exist; use the final arXiv title unless discussing historical title evolution.

### 4. Willison source class

- `Willison (2022)` is a blog/practitioner source, not peer-reviewed literature.
- Keep it in Paper 2 as origin/practitioner context for prompt injection vocabulary, but do not over-weight it as an academic foundation.

### 5. Wei et al. publication status

- *Jailbroken: How Does LLM Safety Training Fail?* appears as NeurIPS 2023.
- Cite proceedings when using final scholarly reference, not only arXiv.

### 6. DSM/PCL-R reference handling

- DSM-5-TR: cite APA (2022) as the source manual.
- PCL-R: choose Hare (2003) unless the first-edition history matters. Current `Hare (1991/2003)` should become `Hare (2003)` in methods/instrument contexts.

### 7. Missing reference lists

None of the four paper draft sets currently contains a complete inserted bibliography/reference list. The `*_REFERENCES_DRAFT.md` files generated in this deliverable are ready to paste into each paper after final section assembly.

## Cross-paper source classes

### Core external scholarly sources

- American Psychiatric Association (2022)
- Bai et al. (2022)
- Bartlett (1932)
- Campbell (1949)
- Christiano et al. (2017)
- Cialdini (1984/2007)
- Ellis & Bochner (2000); Bochner (2000); Chang (2008)
- Freedman & Fraser (1966)
- Ganguli et al. (2022)
- Greshake et al. (2023)
- Hare (2003)
- Jung (1959/1969)
- Marr (1982)
- Milgram (1963, 1974)
- Newell & Simon (1972)
- Ouyang et al. (2022)
- Perez & Ribeiro (2022)
- Rumelhart (1980)
- Stiennon et al. (2020)
- Wei et al. (2023)
- Willison (2022)
- Zou et al. (2023)

### Internal/project artifacts needing a separate artifact bibliography

- `forensic_archetype.py`
- `forensic_archetype_jung_monolith.py`
- `forensic_archetype_tarot_monolith.py`
- `tarot_drift_integration.py`
- `trait_drift_analysis.py`
- `Statistical_Analysis_Plan.md`
- `sap_pipeline_validation.py`
- `RECONCILIATION_MAP_v2.md`

## Recommended folder addition per paper

Add two files to each paper draft folder:

- `BIBLIOGRAPHY_AUDIT.md`
- `REFERENCES_DRAFT.md`

These generated files are named with `P1_`, `P2_`, `P3_`, and `P4_` prefixes for direct placement into draft folders.
