# Paper 1 Bibliography Audit

## Paper

**Constrained Analogical Transfer: Validity Conditions for Cross-Domain Behavioral Modeling in LLM Identity Systems**

## Files audited

- `P1_S1_S6_S7_S8_S9_Bundle.md`
- `P1_S2_DSM5_BehavioralTaxonomy.md`
- `P1_S4_ArchetypeSchemaTheory.md`
- `P1_S5_CEE_FormalDefinition.md`
- `RECONCILIATION_MAP_v2.md`

## Completeness status

**Bibliography status:** incomplete but recoverable.

**Structural status:** Paper 1 is not fully assembled. `RECONCILIATION_MAP_v2.md` marks S3 - SE Transfer Framework as missing. Bibliographic finalization should wait until P1 S3 is drafted, because S3 will almost certainly add Cialdini, Milgram, Hadnagy, Freedman & Fraser, and possibly Bandura.

## In-text citation inventory

Detected external citations:

- American Psychiatric Association (2022)
- Anderson (1978)
- Bartlett (1932)
- Campbell (1949)
- Greshake et al. (2023)
- Hare (1991/2003)
- Jung (1959/1969)
- Marr (1982)
- Newell & Simon (1972)
- Perez & Ribeiro (2022)
- Rumelhart (1980)
- Zou et al. (2023)

Detected project artifact references:

- `DSM-5_TR_Alignment.md`
- `neurotic_ai_framework.md`
- `Artificially_Neurotic_AI` PDF
- `forensic_archetype.py`
- `forensic_archetype_jung_monolith.py`
- `forensic_archetype_tarot_monolith.py`
- `trait_drift_analysis.py`

## Verification findings

### Strong / ready citations

- DSM-5-TR citation is appropriate, but should be listed as American Psychiatric Association (2022), not only mentioned in prose.
- Bartlett (1932), Rumelhart (1980), Marr (1982), Newell & Simon (1972), Campbell (1949), and Jung (1959/1969) are appropriate foundations for the schema/analogical-transfer argument.
- Perez & Ribeiro (2022), Greshake et al. (2023), and Zou et al. (2023) are appropriate adversarial/prompt-injection sources for the domain problem.

### Needs correction

1. `Hare (1991/2003)` should be normalized.
   - Recommended: cite Hare (2003) for the PCL-R second edition manual.
   - Mention 1991 only if discussing first-edition history.

2. `Anderson (1978)` needs exact bibliographic confirmation.
   - Likely intended source: Anderson, R. C. (1978), schema-directed processes in language comprehension / cognitive psychology and instruction.
   - Action: confirm exact chapter title/editor before submission.

3. P1 S3 is missing.
   - This is the largest bibliography blocker because S3 is the natural home for Cialdini, Milgram, Hadnagy, and Freedman & Fraser.

4. Project artifacts need an internal artifact bibliography.
   - They should not be mixed into the same list as peer-reviewed or book sources unless the venue permits software references.

## Required fixes before submission

- Draft P1 S3 and run citation sweep again.
- Insert the reference list from `P1_REFERENCES_DRAFT.md` after final assembly.
- Normalize Hare to 2003 unless edition comparison is deliberate.
- Add a separate “Project Artifacts / Software” subsection.
- Convert to IEEE bracket citations if targeting IEEE/TDSC; otherwise keep APA 7 for doctoral review.

## Risk register

| Risk | Severity | Fix |
|---|---:|---|
| Missing S3 means bibliography is incomplete | High | Draft S3 before final bibliography lock |
| Hare split-date citation | Medium | Normalize to Hare (2003) |
| Anderson exact source uncertain | Medium | Verify exact chapter/article metadata |
| Internal scripts cited as literature | Medium | Move to artifact/software bibliography |
| Adversarial ML sources appear in intro but not reference list | High | Insert references draft |

