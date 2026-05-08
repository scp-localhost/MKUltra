# Paper 4 Bibliography Audit

## Paper

**Alignment Depth as Attack Surface: Cross-Model Constraint Variance Under Archetype-Driven Persona Injection**

## Files audited

- `P4_S1_Abstract_Introduction.md`
- `P4_S2_TheoreticalFrame.md`
- `P4_S3_MethodologyTypology.md`
- `P4_S4_TwoByTwoMatrix.md`
- `P4_S5_EvidenceBase.md`
- `P4_S6_Implications.md`
- `P4_S7_Limitations_NonClaims.md`
- `P4_S8_Conclusion_ExegesisHook.md`
- `RECONCILIATION_MAP_v2.md`

## Completeness status

**Bibliography status:** incomplete but coherent.

Paper 4 is structurally the most complete of the four. Its bibliography is concentrated around alignment methodology and adversarial robustness. It still needs a formal references section and stronger handling of cited-but-implicit sources in §2, where Constitutional AI, RLHF, and attractor-depth arguments are built.

## In-text citation inventory

Detected external citations:

- Bai et al. (2022)
- Ganguli et al. (2022)
- Ouyang et al. (2022)
- Perez & Ribeiro (2022)
- Stiennon et al. (2020)
- Wei et al. (2023)
- Zou et al. (2023)

Detected likely required additions:

- Christiano et al. (2017) for human-preference RL/RLHF lineage.
- Greshake et al. (2023) if indirect prompt injection remains in the evidence base.
- Paper 1, Paper 2, and Paper 3 as companion manuscripts.
- `alignment_typology_matrix.py` as project artifact if present in repo.

## Verification findings

### Strong / ready citations

- Bai et al. (2022) is the correct anchor for Constitutional AI-class training.
- Ouyang et al. (2022), Stiennon et al. (2020), and Christiano et al. (2017) together support RLHF/human-feedback lineage.
- Ganguli et al. (2022) is appropriate for red-teaming and scaling behavior claims.
- Perez & Ribeiro, Wei et al., and Zou et al. are appropriate for adversarial/prompt/jailbreak context.

### Needs correction

1. Christiano et al. (2017) is mentioned in the broader corpus and should be added explicitly to Paper 4 if RLHF lineage is discussed.

2. The evidence base section lists source categories but may not cite every named source in each category at first mention. Add citations directly in §5.1.1.

3. `Anthropic safety publication series` is too vague as a reference phrase.
   - Replace with specific publications or remove as a bibliographic reference.

4. The paper should avoid provider-specific conclusions unless directly supported by cited documents. Current limitation language appears aligned with this requirement; keep it.

5. Companion manuscript references are required.
   - P4 repeatedly depends on Papers 1-3; cite them as unpublished companion manuscripts or internal doctoral research drafts.

## Required fixes before submission

- Insert `P4_REFERENCES_DRAFT.md` into assembled Paper 4.
- Add Christiano et al. (2017) where RLHF lineage is introduced.
- Replace vague source-category references with specific cited sources.
- Add project/software artifact references for the typology/matrix script if used.
- Add companion manuscript references for Papers 1-3.

## Risk register

| Risk | Severity | Fix |
|---|---:|---|
| P4 claims rely on Papers 1-3 but lacks formal companion citations | High | Add companion manuscript refs |
| Vague “Anthropic safety publication series” phrase | Medium | Replace with named sources |
| RLHF lineage missing Christiano et al. (2017) | Medium | Add source at first RLHF-history discussion |
| Evidence base heterogeneous | Medium | Keep limitation language and confidence weighting |
| Project matrix script not cited | Low-Medium | Add artifact citation |
