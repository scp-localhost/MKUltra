# MKUltra — Behavioral Drift in LLM Persona Systems

## Overview

This repository contains a practice-led research program investigating **behavioral drift in large language models under persona injection**.

The work explores a unified hypothesis:

> Behavioral constraint failure in LLMs under persona conditioning can be modeled, predicted, and measured using cross-domain frameworks drawn from:
>
> * clinical behavioral taxonomies
> * social engineering theory
> * archetype/schema systems

The project is organized as a multi-paper series progressing from theory → exploitation → measurement → comparative analysis → defensive architecture.

---

## Research Structure

The repository supports a staged research pipeline:

```
Paper 1 → Theoretical Mapping (behavioral mechanisms)
Paper 2 → Exploit Taxonomy (attack surface)
Paper 3 → Measurement System (drift quantification)
Paper 4 → Cross-Model Theory (alignment variance)
Paper 5 → Evaluation Metrics (BSI)
Paper 6 → Constraint Enforcement (defensive architecture)
Paper 7 → Cross-Domain Synthesis (human ↔ LLM equivalence)
```

This sequence forms the backbone of the eventual doctoral exegesis.

---

## Repository Layout

```
analysis/     Statistical models, ANOVA, LMM, sensitivity analysis
artifacts/    Source literature and reference material (PDFs, diagrams)
data/         Raw and synthetic datasets
docs/         Formal specifications (SAP, reconciliation maps)
drafts/       Paper sections and manuscript fragments
scripts/      Core experimental and modeling code
```

### Key Components

* **forensic_archetype.py**
  Canonical archetype behavioral profiles (centroid source)

* **trait_drift_analysis.py**
  Drift measurement engine (CEE-based scoring)

* **Statistical_Analysis_Plan.md**
  Model specification and hypothesis structure

* **RECONCILIATION_MAP.md**
  Cross-paper dependency tracker and project state

---

## Core Concepts

* **Persona Injection**
  Activation of behavioral schemas via identity assignment

* **Identity Drift**
  Deviation from baseline constraint behavior under persona conditioning

* **Constraint Expectation Envelope (CEE)**
  A bounded region of expected behavior for a given persona; used as the primary measurement construct

* **Exploit Taxonomy**
  Structured classification of persona-mediated attack vectors

---

## Methodological Position

This project is:

* **Theory-building first**
  (analogical mapping across established frameworks)

* **Measurement-driven second**
  (formalization via CEE and drift metrics)

* **Hypothesis-generating**
  (not yet large-scale empirical validation)

No claims are made regarding:

* model consciousness
* human equivalence
* clinical diagnosis

---

## Status

Active development.

* Papers 1–4: Drafted (varying completeness)
* Paper 3: Instrument implementation in progress
* Papers 5–7: Seed stage

See `docs/RECONCILIATION_MAP.md` for current state and dependencies.

---

## Usage

This repository is not packaged as a production system.

Typical workflows:

* Assemble papers from `/drafts`
* Run drift analysis via `/scripts`
* Validate hypotheses using `/analysis`
* Track dependencies via `/docs`

---

## Notes

* This work operates under a **no-active-probing constraint**
  (analysis is theoretical and observational, not adversarial deployment)

* Alignment and safety implications are treated as **research outputs**, not operational tools

---

## License

TBD

---

## Contact / Attribution

Author: [TBD]

This repository represents an evolving research system rather than a finalized publication artifact.
