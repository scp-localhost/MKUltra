# Paper 2 Bibliography Audit

## Paper

**A Predictive Taxonomy of Persona-Mediated Alignment Exploits in Large Language Models / LLM Social Engineering**

## Files audited

- `P2_Abstract_S1_S2_S9.md`
- `P2_S3_IdentityInjection.md`
- `P2_S4_ExploitTaxonomy.md`
- `Paper2_Section4_ExploitTaxonomy.md`
- `Paper2_Section5_CEE_Operational.md`
- `P2_S6_S7_S8_AlignImplications_Ethics_Limitations.md`
- Paper 2 docx snippets where visible in uploaded context

## Completeness status

**Bibliography status:** incomplete but strongly recoverable.

Paper 2 has the densest security/social-engineering citation load. The core references are visible in the prose, but there is no consolidated reference list in the draft sections. Legacy and current section files also disagree on taxonomy count and some citation dates.

## In-text citation inventory

Detected external citations:

- Bai et al. (2022)
- Cialdini (1984/2007) / Cialdini (1984)
- Freedman & Fraser (1966)
- Greshake et al. (2023)
- Hadnagy (2010) and/or Hadnagy (2011)
- Milgram (1963/1974), Milgram (1974)
- Ouyang et al. (2022)
- Perez & Ribeiro (2022)
- Wei et al. (2023)
- Willison (2022)
- Zou et al. (2023)

Detected project artifact references:

- `forensic_archetype.py`
- `forensic_archetype_jung_monolith.py`
- `trait_drift_analysis.py`
- `Statistical_Analysis_Plan.md`
- CEE formalism from Paper 1
- Paper 3 measurement apparatus

## Verification findings

### Strong / ready citations

- Cialdini, Milgram, Hadnagy, and Freedman & Fraser are appropriate for the social-engineering transfer/taxonomy argument.
- Perez & Ribeiro, Greshake et al., Willison, Wei et al., and Zou et al. are appropriate for prompt injection/jailbreak context.
- Bai et al. and Ouyang et al. are appropriate for alignment-method references in the alignment implications section.

### Needs correction

1. Hadnagy date conflict.
   - Current sections mostly use Hadnagy (2010), while other uploaded methods snippets use Hadnagy (2011).
   - Recommended: standardize to Hadnagy (2011) for *Social Engineering: The Art of Human Hacking*.

2. Cialdini edition mismatch.
   - Some sections say Cialdini (1984/2007), others Cialdini (1984).
   - Recommended: use Cialdini (2007) if citing the revised edition, with note original work 1984; otherwise use 1984 consistently.

3. Prompt injection source hierarchy.
   - Willison (2022) is a practitioner/blog source and should be framed as terminology/history, not primary peer-reviewed evidence.
   - Perez & Ribeiro (2022) and Greshake et al. (2023) should carry the formal literature weight.

4. Legacy numbered placeholders.
   - The uploaded Paper2 Section 3 draft contains `[1][2][3]`, `[4][5]`, etc. in the docx snippet.
   - Replace all numbered placeholders with final IEEE numbers after assembly, or convert to APA author-date before doctoral review.

5. Taxonomy count consistency.
   - Some files describe a four-class taxonomy; later files describe a five-class taxonomy.
   - Bibliography cannot be fully locked until the assembled paper chooses one taxonomy version. Current Paper 2 section set appears to prefer five classes.

## Required fixes before submission

- Insert `P2_REFERENCES_DRAFT.md` into assembled Paper 2.
- Normalize Hadnagy to 2011.
- Normalize Cialdini edition handling.
- Replace `[REF-CODE]` and numeric placeholders with real references.
- Decide whether Paper 2 taxonomy is four-class or five-class and reconcile all section language.
- Add artifact/software references for scripts and internal documents.

## Risk register

| Risk | Severity | Fix |
|---|---:|---|
| Hadnagy date conflict | High | Standardize to 2011 |
| Four-class vs five-class taxonomy conflict | High | Reconcile before final bibliography numbering |
| Numbered placeholders unresolved | High | Convert after final assembly |
| Willison over-weighted | Medium | Keep as practitioner source only |
| Script references not bibliographically represented | Medium | Add artifact bibliography |
