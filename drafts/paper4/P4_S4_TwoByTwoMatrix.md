# Paper 4 — Section 4: The 2×2 Capability × Alignment Matrix
## "Separating the Variables: A Predictive Framework for Cross-Model Constraint Variance"

> **Placement:** `drafts/paper4/P4_S4_TwoByTwoMatrix.md`
> **Status:** DRAFT v0.1 — 2026-04-27
> **Role in paper:** Operationalization of the capability/alignment separation
> argument (§2.4) as a structured predictive framework. This section converts
> theoretical constructs into falsifiable cell-level predictions. It is the
> paper's analytic engine: §5 (evidence base) tests its cells; §6 (implications)
> draws from them. The matrix is also the paper's primary contribution to
> the exegesis — it demonstrates that a theoretically derived 2×2 can do
> genuine analytic work without requiring active probing.
>
> **Architectural note:** The four cells are already encoded in
> `scripts/alignment_typology_matrix.py` as `THEORETICAL_MATRIX`. This
> section is the academic argument that justifies and interprets that structure.
> The script is the formal apparatus; this section is the reasoning. Neither
> is complete without the other.
>
> **Cross-paper dependencies:**
> - Imports: attractor depth construct and AD proxy formula (P4 §2.2)
> - Imports: redundancy hypothesis and failure mode taxonomy (P4 §2.3)
> - Imports: capability/alignment separation argument (P4 §2.4)
> - Imports: schema suppression account (P4 §2.5)
> - Imports: four-class typology and behavioral signatures (P4 §3)
> - Exports: cell-level predictions → P4 §5 (evidence coding); §6 (implications)
> - Exports: discriminating cell logic → P4 §7 falsifiability conditions
>
> **Committee exposure:** HIGH. The matrix format is immediately legible to
> committee members — four cells, two dimensions, stated predictions. The
> critical discriminating cells (HIGH_CAP_LOW_ALIGN, LOW_CAP_HIGH_ALIGN) will
> draw the most scrutiny because they make the sharpest claims. Defend them
> with the mechanism argument, not with empirical confidence. The paper's
> methodological frame is hypothesis-generating; the matrix is the hypothesis.
>
> **Publication constraint active:** All cell characterizations describe
> alignment methodology classes and capability tiers, not named products.
> Where illustrative examples are offered, they reference published training
> procedure descriptions, not inferences about commercial deployments.

---

## 4. The 2×2 Capability × Alignment Matrix

### 4.1 The Structure of the Argument

The paper's central claim — that constraint variance under archetype-driven persona
injection correlates more strongly with alignment methodology than with raw model
capability — requires more than a theoretical assertion. It requires a predictive
structure that specifies, in advance of evidence review, what the world should look
like if the claim is correct, and equally what it should look like if the claim is
wrong.

The 2×2 capability × alignment matrix provides that structure. It operationalizes the
two variables as crossed dimensions, populates each cell with predictions derived from
the theoretical framework developed in §2 and §3, and identifies which cells produce
convergent predictions under the two competing accounts (capability dominant, alignment
dominant) and which cells produce divergent predictions that can serve as empirical
discriminators.

The matrix does not settle the question — the evidence base in §5 engages with the
discriminating cells, and the paper's methodological frame is explicitly
hypothesis-generating rather than hypothesis-confirming. But the matrix structure
means that the hypothesis is stated with sufficient precision that evidence can
meaningfully bear on it. That precision is the section's primary contribution.

---

### 4.2 Operationalizing the Two Dimensions

#### 4.2.1 Capability Tier

Capability tier, as used in this matrix, is a dichotomized variable (HIGH / LOW)
representing the relative capacity of a model's base architecture and pretraining
investment. It is not a precise measurement — capability is a multidimensional
construct, and its relationship to constraint behavior is precisely what this paper
is working to disentangle. The dichotomization is a theoretical simplification
that enables the matrix structure; claims derived from it are bounded by the
simplification.

**HIGH capability tier** encompasses models whose pretraining and architecture
represent substantial compute and data investment, whose benchmark performance on
standard evaluations places them in the upper performance range of publicly documented
models, and whose training corpus is large, diverse, and includes dense representation
of the cultural and narrative material that produces strong behavioral schema
activation under archetype injection (P1 §4.3).

**LOW capability tier** encompasses models with more limited pretraining investment —
smaller parameter counts, narrower training corpora, or reduced compute budgets —
whose benchmark performance is materially lower than the HIGH tier. For purposes of
schema activation specifically, LOW tier models are expected to exhibit weaker
behavioral schema signals under archetype injection not because they are immune to
schema activation but because their training corpus contains less dense and less
consistent representation of the canonical character material.

*Critical clarification.* The capability tier dimension does not correlate with the
alignment dimension by default. A HIGH capability model may carry any alignment
methodology class from §3; a LOW capability model similarly. The two dimensions are
independently determined by training decisions, not by technical necessity. The
matrix's analytical value derives precisely from this independence.

#### 4.2.2 Alignment Investment

Alignment investment is represented in the matrix as a collapsed HIGH / LOW dimension
corresponding to the typology developed in §3. HIGH alignment investment encompasses
Constitutional AI-class and RLHF-dominant training procedures; LOW alignment investment
encompasses instruction-tuning-only and open-weight unaligned procedures. This
collapsing is a simplification that preserves the within-class variation documented
in §3 for within-class analysis while enabling the matrix's cross-class comparison.

The HIGH/LOW collapse is conservative with respect to the paper's central claim:
it groups RLHF-dominant with CAI-class as HIGH, despite the attractor depth and
redundancy differences documented in §2.3 and §3.3. A more granular version of the
matrix would distinguish these — and the theoretical framework predicts they would
cluster differently. But as a first-pass predictive framework, the binary collapse
allows the sharpest test of the capability-vs-alignment question without over-
specifying the alignment variable.

*Within-cell variation.* The two HIGH-alignment cells in the matrix contain
predictions appropriate to the dominant alignment class assigned to each. Where
within-class variation is theoretically significant — specifically, the predicted
difference between CAI-class and RLHF-dominant behavior within the HIGH alignment
tier — this is noted in the relevant cell discussion and developed further in §5.

---

### 4.3 The Four Cells

The matrix is presented in full, with each cell containing: the theoretical prediction
from the alignment account, the alternative prediction from the capability account,
the predicted AD range, the predicted failure mode, and the cell's discriminating
function. The two cells that most sharply separate the two accounts are marked as
Critical Discriminators and receive extended discussion in §4.4.

---

**Table 1: 2×2 Capability × Alignment Predictive Matrix**

```
                    ┌─────────────────────────────┬─────────────────────────────┐
                    │   HIGH ALIGNMENT             │   LOW ALIGNMENT             │
                    │   (CAI-class / RLHF-dominant)│   (IT-only / open-weight)   │
┌───────────────────┼─────────────────────────────┼─────────────────────────────┤
│                   │  CELL A                      │  CELL B  ★                  │
│  HIGH CAPABILITY  │  Predicted AD: 0.75–1.0      │  Predicted AD: 0.0–0.25     │
│                   │  Failure mode:               │  Failure mode:              │
│                   │  contested-partial-breach    │  immediate-schema-dominance │
│                   │                              │                             │
│                   │  Both accounts predict HIGH  │  Accounts DIVERGE:          │
│                   │  AD. Non-discriminating.     │  Capability → HIGH AD       │
│                   │                              │  Alignment → NEAR-ZERO AD   │
├───────────────────┼─────────────────────────────┼─────────────────────────────┤
│                   │  CELL C  ★                   │  CELL D                     │
│  LOW CAPABILITY   │  Predicted AD: 0.50–0.80     │  Predicted AD: 0.0–0.30     │
│                   │  Failure mode:               │  Failure mode:              │
│                   │  contested-partial-breach    │  shallow-threshold          │
│                   │                              │                             │
│                   │  Accounts DIVERGE:           │  Both accounts predict LOW  │
│                   │  Capability → LOW AD         │  AD. Non-discriminating.    │
│                   │  Alignment → MOD-HIGH AD     │                             │
└───────────────────┴─────────────────────────────┴─────────────────────────────┘

★ = Critical Discriminating Cell
```

---

#### 4.3.1 Cell A — High Capability, High Alignment

**Theoretical prediction (alignment account).** A high-capability model with
Constitutional AI-class or RLHF-dominant alignment training carries both a rich
behavioral schema activation profile (from dense, diverse pretraining) and a deep
identity attractor (from substantial alignment investment). The two factors are
compounding: the alignment signal must work harder because the schema signals are
stronger, but the alignment investment is sufficient to establish a robust attractor
weight advantage. Predicted outcome is high attractor depth (AD range 0.75–1.0),
contested-partial-breach failure mode under sustained pressure, and high recovery
rate following perturbation removal.

**Alternative prediction (capability account).** The capability account produces the
same prediction — high capability predicts high constraint stability. Both accounts
converge on Cell A.

**Discriminating function.** Cell A does not discriminate between the two accounts.
It confirms that the conjunction of high capability and high alignment produces high
constraint stability, which is expected under both accounts. Its value is confirmatory
rather than discriminatory: if Cell A shows low constraint stability, both accounts
are wrong, which would be a more fundamental result requiring a third account not
currently in scope.

**Within-cell variation note.** Within the HIGH alignment tier, Cell A contains
a predicted sub-cell difference: CAI-class models within this cell should exhibit
higher perturbation thresholds and higher recovery rates than RLHF-dominant models
at equivalent capability tier, due to the redundancy difference established in §2.3.
If the evidence base in §5 provides cases for both CAI-class and RLHF-dominant models
at HIGH capability, this sub-cell prediction becomes testable and constitutes
additional evidence for the redundancy hypothesis independent of the capability-vs-
alignment question.

---

#### 4.3.2 Cell B — High Capability, Low Alignment ★ Critical Discriminator

**Theoretical prediction (alignment account).** A high-capability model with
instruction-tuning-only or open-weight unaligned training carries rich behavioral
schema activation signals (from dense, diverse pretraining) but no meaningful identity
attractor (from the absence of dedicated alignment training). The alignment account
predicts that schema activation meets no competing attractor signal, and therefore
constraint stability is near-zero regardless of the model's capability. Predicted AD
range 0.0–0.25, immediate-schema-dominance failure mode, near-zero recovery rate.

Importantly, the alignment account carries an additional prediction specific to this
cell: a HIGH-capability LOW-alignment model may exhibit *stronger* schema activation
than a LOW-capability LOW-alignment model, because its denser and more diverse
pretraining corpus contains richer behavioral contract encoding for canonical
archetypes. The schema activation signal is stronger precisely because the model
is more capable — which, without a countervailing alignment attractor, produces
more pronounced and more complete schema-dominant behavior under injection, not
less. Capability amplifies the vulnerability when alignment is absent.

**Alternative prediction (capability account).** The capability account predicts
high constraint stability for HIGH-capability models regardless of alignment
methodology. A large, capable model should resist persona injection effectively
because it has more sophisticated output generation, more nuanced contextual
processing, and greater capacity for complex reasoning — all of which should produce
more elaborate constraint-consistent behavior. The capability account predicts Cell B
looks like Cell A: high AD, contested behavior at most, robust recovery.

**Discriminating function.** Cell B is the first critical discriminator. The two
accounts predict in opposite directions. If Cell B models exhibit low constraint
stability (near-zero AD, immediate-schema-dominance failure mode, poor recovery), the
alignment account is supported and the capability account is falsified for this cell.
If Cell B models exhibit high constraint stability, the capability account is supported
and the alignment account requires revision — specifically, the claim that alignment
methodology is necessary for attractor depth would need to be weakened.

**Why this cell matters for the exegesis.** Cell B is the cell that carries the
paper's most practically significant claim: that deploying a high-capability model
without proportionate alignment investment does not produce the safety properties
that capability alone might be assumed to provide. This is not merely a theoretical
finding — it has direct implications for alignment investment decisions at the
deployment layer. A committee member from an AI safety or security venue will
recognize this cell as the paper's practical payload.

---

#### 4.3.3 Cell C — Low Capability, High Alignment ★ Critical Discriminator

**Theoretical prediction (alignment account).** A low-capability model with
Constitutional AI-class or RLHF-dominant alignment training carries a weaker
behavioral schema activation profile (from sparser pretraining) but a genuine
identity attractor (from dedicated alignment investment). The alignment account
predicts that the attractor, though competing against a weaker schema signal, is
sufficient to produce moderate-to-high constraint stability. The model is not
"fooling" the schema into not activating; it is maintaining a trained weight
advantage over the schema signal at the output layer. Predicted AD range 0.50–0.80,
contested-partial-breach failure mode, moderate recovery rate.

The alignment account also predicts that a well-aligned small model outperforms
a more capable but minimally aligned model in constraint stability — Cell C
outperforms Cell B on AD metrics. This cross-cell prediction is the sharpest
single prediction the matrix generates, and it is the one most directly relevant
to alignment investment arguments: the security properties relevant to persona
injection resistance are a function of training choices, not just of scale.

**Alternative prediction (capability account).** The capability account predicts
low constraint stability for LOW-capability models. A smaller model lacks the
sophisticated contextual reasoning and output generation capacity required to
maintain constraint-consistent behavior under sustained persona pressure. The
capability account predicts Cell C looks like Cell D: low AD, shallow-threshold
or rapid collapse failure mode.

**Discriminating function.** Cell C is the second critical discriminator. The two
accounts again predict in opposite directions. If Cell C models exhibit moderate-to-
high constraint stability (AD ≥ 0.50), the alignment account is supported and the
capability account is falsified for this cell. If Cell C models exhibit low constraint
stability despite high alignment investment, the alignment account requires revision —
specifically, the claim that alignment training produces attractor depth independently
of capability would need to be weakened, suggesting a capability floor below which
alignment investment cannot establish a functional attractor.

**The Cell C boundary condition.** The alignment account acknowledges a theoretically
motivated boundary condition: there may exist a capability floor below which alignment
training cannot establish a functional identity attractor, because the model lacks
the representational capacity to support the multi-layer self-revision encoding that
produces CAI-class attractor depth. This boundary condition is not a concession to
the capability account — it is a refinement of the alignment account that makes
it more precise. The predicted AD range of 0.50–0.80 rather than 0.75–1.0 reflects
this: Cell C's AD ceiling is lower than Cell A's, acknowledging that capability
contributes to attractor quality even if alignment is the dominant predictor of
attractor presence.

---

#### 4.3.4 Cell D — Low Capability, Low Alignment

**Theoretical prediction (alignment account).** A low-capability model with
instruction-tuning-only or open-weight unaligned training has neither a deep identity
attractor nor a strong schema activation profile. Both factors are low. Constraint
stability is minimal; persona injection produces rapid schema-dominant behavior with
a shallow perturbation threshold. Predicted AD range 0.0–0.30, shallow-threshold
failure mode, low recovery rate. The model's behavior under injection reflects
primarily the archetype's behavioral contract without meaningful alignment resistance.

**Alternative prediction (capability account).** The capability account also predicts
low constraint stability for LOW-capability models. Both accounts converge on Cell D.

**Discriminating function.** Cell D does not discriminate between the two accounts.
Like Cell A, it confirms a conjunction — here, that the absence of both capability
and alignment investment produces the baseline vulnerability level. Its value is
as a control condition: if Cell D shows unexpectedly high constraint stability, both
accounts require revision, as an alternative mechanism not captured by either
dimension is producing the resistance.

**Baseline function.** Cell D provides the empirical floor against which the other
cells are interpreted. In the absence of both capability and alignment investment,
what does persona injection resistance look like? The answer — near-minimal, with
schema-dominant behavior emerging under low perturbation pressure — is the baseline
from which the relative contributions of the two variables can be estimated.

---

### 4.4 The Discriminating Logic: What Evidence Would Settle the Question

The matrix's predictive structure generates a clear decision procedure for evaluating
the capability-vs-alignment question. The decision procedure is not binary — "one
account wins, one loses" — but graduated, reflecting the possibility that both
variables contribute to constraint stability at different magnitudes.

**Strong alignment-dominant finding.** If Cell B exhibits low constraint stability
(≤ 0.25 AD range) AND Cell C exhibits moderate-to-high constraint stability (≥ 0.50
AD range), the alignment account is strongly supported. The crossing of predictions —
high capability without alignment performs poorly, low capability with alignment
performs moderately well — is the clearest possible evidence that alignment methodology
is the dominant variable.

**Weak alignment-dominant finding.** If Cell B exhibits low constraint stability
but Cell C also exhibits low constraint stability (below 0.50), the alignment account
is partially supported — it correctly predicts Cell B, but the Cell C boundary
condition is active. Alignment investment produces some attractor depth, but not
enough at low capability to generate the predicted moderate-to-high stability. The
capability floor hypothesis requires investigation.

**Strong capability-dominant finding.** If Cell B exhibits high constraint stability
(≥ 0.50 AD range) AND Cell C exhibits low constraint stability (≤ 0.25), the
capability account is strongly supported. The crossing goes the other way: high
capability without alignment resists well, low capability with alignment resists
poorly. The alignment account would require fundamental revision.

**Null finding.** If all four cells cluster at similar AD ranges regardless of
alignment methodology or capability tier, neither account is supported and a third
variable — inference-time parameters, system prompt architecture, archetype selection
confounds, or another factor not captured by the matrix dimensions — is likely
dominant.

---

### 4.5 The Archetype Dimension: A Third Variable Held Constant

The matrix crosses two dimensions — capability and alignment — while treating
archetype as a held-constant variable. This is a deliberate simplification that
requires explicit acknowledgment.

The CEE framework (P1 §5) and the AD proxy (P4 §2.2.3) both index attractor depth
to the specific archetype injected: AD(M, A) always carries the archetype subscript.
Different archetypes present different schema conflict levels relative to a given
model's alignment attractor — a lawful-neutral archetype (Batman) presents lower
schema conflict against a constraint-consistent alignment attractor than a chaotic
archetype (Joker). Predicted AD ranges therefore vary with archetype selection, not
only with the cell's capability and alignment dimensions.

For the matrix to function as a clean capability-vs-alignment comparison, archetype
must be held constant across cells — or, if multiple archetypes are included in the
evidence base, the comparison must control for archetype by reporting AD separately
per archetype. The matrix predictions in §4.3 are stated for a mid-range schema
conflict archetype (approximately equivalent to the Joker-Magneto mid-tier in the
P3 archetype set): high enough canonical overdetermination to produce reliable
schema activation, high enough schema conflict to challenge the identity attractor,
but not at the ceiling of possible conflict weight where any alignment methodology
would be overwhelmed regardless of depth.

This archetype assumption is stated explicitly and is a scope limit for the evidence
analysis in §5. Where observational cases in §5 involve high-conflict archetypes
(e.g., direct jailbreak-oriented characters), AD measurements are expected to be
lower across all cells; where cases involve low-conflict archetypes, AD measurements
are expected to be higher. The cross-cell pattern — Cell A > Cell C > Cell B ≥ Cell D
under alignment account predictions — is expected to hold regardless of the absolute
AD level, but the magnitude of the differences will vary with archetype selection.

---

### 4.6 What the Matrix Cannot Determine

Intellectual honesty requires stating what the 2×2 structure cannot resolve, even
in principle.

**Within-class variation.** The matrix collapses the four-class alignment typology
to a binary. Within the HIGH alignment tier, CAI-class and RLHF-dominant models are
predicted to behave differently (§2.3, §3.2–3.3). The matrix cannot distinguish these
within-class differences; that requires the full typology applied to a richer evidence
set than this paper can provide. The matrix is a coarse-grained instrument for a
coarse-grained question.

**Capability non-linearity.** The capability dimension is dichotomized. In practice,
capability is continuous and its relationship to schema activation and alignment
attractor quality may be non-linear. The matrix assumes a monotonic relationship
(higher capability → stronger schema activation, potentially better attractor quality)
that may not hold at the extremes. Very high capability models may exhibit emergent
constraint-consistent behaviors not present at moderate capability; very low capability
models may lack the representational capacity for meaningful alignment attractor
formation. These non-linearities are outside the matrix's scope.

**Interaction effects.** The matrix treats the two dimensions as main effects. Their
interaction — whether the effect of alignment investment on constraint stability
differs between capability tiers — is not directly specified by the matrix structure.
The Cell C boundary condition (§4.3.3) is the closest the matrix comes to predicting
an interaction: alignment investment may be less effective at very low capability
tiers. But a formal interaction analysis would require more cases than the current
evidence base can provide and is left to future empirical work.

**Deployment context.** The matrix predictions are stated for standard deployment
conditions: inference-time parameters at default, no additional system prompt
constraint architecture beyond the persona injection under study, single-turn or
short multi-turn sessions. Deployment contexts with additional safety layers, system
prompt constraints, or real-time monitoring are outside the matrix's scope. The
matrix describes the vulnerability surface as a function of training; it does not
describe the vulnerability surface as modified by deployment architecture.

---

### 4.7 Forward References from This Section

- **§5 (Evidence Base):** Each observational case is coded against the matrix cell
  vocabulary — `matrix_cell_key` in the `ObservationalCase` schema in
  `scripts/alignment_typology_matrix.py`. The evidence analysis evaluates the
  discriminating cells (B and C) against the decision procedure in §4.4.

- **§6 (Implications):** The matrix's Cell B prediction — high capability without
  alignment produces near-zero constraint stability — is the theoretical basis for
  the paper's central alignment investment argument. If Cell B is supported, it
  follows directly that alignment investment is not optional for models deployed
  in contexts where persona injection is a realistic attack surface.

- **§7 (Limitations and Non-Claims):** The three limitations in §4.6 (within-class
  variation, capability non-linearity, interaction effects) are consolidated in the
  limitations section with appropriate hedging.

- **`scripts/alignment_typology_matrix.py`:** The `THEORETICAL_MATRIX` dict and
  `MatrixCell` dataclass encode this section's structure as executable apparatus.
  The `generate_prediction_table()` function renders Table 1's predictions in
  machine-readable form.

- **Exegesis hook:** The matrix structure demonstrates a methodological principle
  that the exegesis can develop: a well-constructed 2×2 theoretically derived from
  existing frameworks can generate novel, non-obvious, falsifiable predictions about
  a domain where active probing is ethically constrained. The practice-led insight
  is that theoretical precision can partially substitute for empirical scope when
  the research design cannot support broad controlled experimentation. This is a
  contribution to research methodology, not only to AI safety.

---

*Section ends. Next: §5 — Evidence Base. §4's discriminating cell logic provides
the coding framework for §5. Each observational case should be attributed to a
matrix cell and evaluated for consistency/inconsistency with the discriminating
hypotheses in §4.3.2 and §4.3.3.*

---

> **Reconciliation note (2026-04-27):**
>
> Table 1 renders cleanly in markdown. On DOCX assembly, convert to a bordered
> table — the ASCII-art matrix is functional for draft but requires typesetting
> for submission. Flag for assembly pass.
>
> §4.3.2's "capability amplifies vulnerability when alignment is absent" is a
> new theoretical claim not present in §2. It is a valid deduction from the
> schema activation mechanism (denser pretraining = stronger behavioral contract
> encoding) but should be cross-referenced with P1 §4.3 (training-data density
> mechanism) on assembly to ensure consistency. Add to RECONCILIATION_MAP.md
> as a new cross-paper consistency item: "P4 §4.3.2 capability-amplifies-
> vulnerability claim → cite P1 §4.3 as mechanistic grounding."
>
> §4.5 (archetype as held-constant variable) introduces a three-variable
> interaction that the paper's framework can theorize but the evidence base
> cannot fully test. Flag for §7 limitations: the matrix produces cell-level
> predictions that are archetype-conditional, and the evidence base in §5 must
> report AD by archetype, not pooled across archetypes, for the cell comparisons
> to be valid. If the evidence base cannot support this, the cell comparisons
> must be framed as illustrative rather than probative.
>
> The Cell C boundary condition (§4.3.3) — capability floor below which
> alignment investment cannot establish a functional attractor — is a new
> theoretical element that should propagate to §7 (limitations) and to the
> RECONCILIATION_MAP.md watch list. It does not invalidate the alignment
> account but refines it; any future empirical work testing this matrix
> should design for capability floor detection specifically.
