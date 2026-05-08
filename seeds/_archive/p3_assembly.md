You are assembling a near-complete academic manuscript from pre-written draft sections. This is a synthesis and normalization task, not a creative writing task.

## Objective

Construct a submission-ready draft of:

**"Behavioral Drift in Prompt-Conditioned LLM Personas: Empirical Measurement of Constraint Expectation Envelopes Under Archetype Injection and Perturbation"**

from the attached section files.

## Target Venues

Primary: IEEE Transactions on Dependable and Secure Computing (TDSC)
Secondary: IEEE S&P Workshop (LLM Security / SafeAI)

## Paper Role

This is the **empirical validation paper** in a multi-paper research program.

It must:

* Provide measurable evidence for the theoretical framework (Paper 1)
* Empirically evaluate the exploit and drift claims (Paper 2)
* Operationalize and validate the Constraint Expectation Envelope (CEE)

This paper MUST stand alone as an empirical contribution.

---

## Core Requirements

### 1. Preserve All Experimental Content

* Do NOT invent results, statistics, or findings
* Do NOT simulate data or fabricate significance
* Preserve:

  * experimental design
  * archetype conditions
  * measurement definitions
  * statistical analysis plan
* Maintain exact alignment with the instrument (`trait_drift_analysis.py`)

---

### 2. Assemble into Standard Empirical Paper Structure

Produce a clean manuscript with:

* Abstract
* 1. Introduction
* 2. Methods

  * Design overview
  * Archetype conditions
  * Injection protocol
  * Measurement variables
* 3. Instrument Specification

  * CEE centroid derivation
  * Drift calculation
  * τ (tolerance parameter)
* 4. Experimental Design and Procedure
* 5. Analysis Plan (SAP integration)
* 6. Results (ONLY if explicitly present in source material)
* 7. Discussion
* 8. Limitations
* 9. Conclusion

---

### 3. Protect Critical Scientific Positioning

Ensure the following are explicit:

* This paper tests **behavioral output patterns**, not internal model states
* No claim of psychological reality in LLMs
* The CEE is a **measurement construct**, not a cognitive claim
* Predictions are specified *before* observation (prospective design)
* The study is **theory-testing**, not exploratory pattern finding

---

### 4. Maintain Strict Methodological Integrity

* Clearly separate:

  * predicted outcomes vs observed outcomes
  * design vs interpretation
* Do NOT blur hypothesis and result
* Preserve causal language discipline:

  * use “predicts,” “is associated with,” not “proves” or “causes”

---

### 5. Normalize for IEEE Empirical Standards

* Formal, precise, non-narrative tone

* Explicit variable definitions (IVs, DVs)

* Clear mapping between:

  * theory (CEE)
  * instrument (drift function)
  * analysis (SAP)

* Ensure reproducibility:

  * procedures must be interpretable by an external researcher

---

### 6. Resolve Structural Issues

* Eliminate duplication across methods and instrument sections
* Ensure consistent terminology:

  * drift magnitude
  * CEE breach
  * perturbation response
  * resilience score
* Align section numbering and cross-references

---

### 7. Results Handling Rule (Critical)

If results are:

* Present → include and organize cleanly
* Partial → include only what exists, do not infer
* Absent → omit Results section or clearly mark as future work

Under no circumstances should results be invented or implied.

---

### 8. Output Requirements

* Single continuous manuscript
* Clean section hierarchy
* No commentary, notes, or meta-text
* No explanations of what was changed
* Ready for export to LaTeX or Word

---

## Conflict Resolution Rule

If sections conflict, prioritize:

1. Instrument specification (ground truth for measurement)
2. Statistical Analysis Plan
3. Methods section definitions
4. Conservative interpretation over expansion

---

## Important Constraint

You are not authoring new research.

You are performing controlled assembly of a doctoral-level empirical manuscript.

Begin once sections are provided.
