# Paper 3 Bibliography Audit

## Paper

**Behavioral Drift in Prompt-Conditioned LLM Personas: Empirical Measurement of Constraint Expectation Envelopes Under Archetype Injection and Perturbation**

## Files audited

- `P3_S1_Introduction.md`
- `P3_S2_Methods.md`
- `P3_S3_InstrumentSpec.md`
- `Statistical_Analysis_Plan.md`
- `trait_drift_analysis.py`
- `sap_pipeline_validation.py`

## Completeness status

**Bibliography status:** incomplete and currently methods-heavy.

Paper 3 has fewer explicit external citations than Papers 1, 2, and 4 because it relies heavily on prior papers and internal instruments. That is defensible only if Paper 3 includes a clear internal-dependency citation pattern and a separate artifact/software reference list.

## In-text citation inventory

Detected external citations:

- Bochner (2000)
- Chang (2008)
- Ellis & Bochner (2000)
- Hare (1991/2003)

Detected internal dependencies/artifacts:

- Paper 1 §4.6, §5, §6.3
- Paper 2 §4
- `forensic_archetype.py`
- `trait_drift_analysis.py`
- `Statistical_Analysis_Plan.md`
- `sap_pipeline_validation.py`
- `SYNTHETIC_CONSENT.md` (referenced but not present in uploaded files)
- `docs/stimuli_registry.json` (referenced but not present in uploaded files)
- `analysis/sensitivity/` (referenced as folder path, not present in uploaded root)

## Verification findings

### Strong / ready citations

- Ellis & Bochner / Bochner / Chang are appropriate if Paper 3 frames practice-led, autoethnographic, or reflexive methodology.
- Hare is appropriate as an instrument vocabulary source only if the text continues to state clearly that PCL-R is used analogically and not diagnostically.

### Needs correction

1. `Hare (1991/2003)` should be normalized.
   - Recommended: use Hare (2003) for the PCL-R second edition manual.

2. Internal dependencies need formal citation handling.
   - Paper 3 repeatedly depends on Paper 1 and Paper 2. Add a “Series dependency note” or cite the prior papers as companion manuscripts.

3. Missing referenced project files.
   - `SYNTHETIC_CONSENT.md` and `docs/stimuli_registry.json` are referenced but not present in the uploaded root set. If they exist in the repo, include them in the artifact bibliography; if not, draft them before finalization.

4. Statistical source gap.
   - The SAP specifies ANOVA, repeated-measures ANOVA, Levene, Shapiro-Wilk, Tukey HSD, Games-Howell, logistic/Poisson models. Paper 3 should cite at least one methods/statistics source or justify using SAP as internal preregistration/specification.
   - Recommended additions: Field (statistics text), Maxwell & Delaney, or official SciPy/statsmodels docs if implementation-focused.

## Required fixes before submission

- Insert `P3_REFERENCES_DRAFT.md` into assembled Paper 3.
- Normalize Hare to 2003.
- Add references for statistical tests or move them entirely to SAP with a cited SAP appendix.
- Add project artifacts for missing protocol/registry files if they exist.
- Make the companion-paper citation style explicit.

## Risk register

| Risk | Severity | Fix |
|---|---:|---|
| Too few external methods/statistics citations | High | Add statistical methodology references |
| Missing project protocol files referenced in text | High | Create or remove references |
| Hare split-date citation | Medium | Normalize to Hare (2003) |
| Prior papers cited informally only | Medium | Add companion manuscript references |
| Instrument source treated as self-evident | Medium | Add software/artifact bibliography |
