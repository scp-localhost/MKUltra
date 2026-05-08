"""
trait_drift_analysis.py
=======================
Primary measurement instrument for Paper 3:
"Behavioral Drift in Prompt-Conditioned LLM Personas"

Implements calculate_psychopathy_drift() — the CEE drift scoring function.

CEE centroid source-of-truth: forensic_archetype.py trait weights.
Output schema: locked in seeds/p3.md — do not change without reconciliation note.

PCL-R proxy weight structure derived from Hare (1991/2003) factor loadings:
  Factor 1 (Interpersonal/Affective): grandiosity, empathy_deficit,
            moral_disengagement, calculating_behavior
  Factor 2 (Lifestyle/Antisocial): impulsivity, impulse_control,
            emotional_lability, reality_testing (inverse)

Perturbation response classification thresholds:
  recovery   — drift_magnitude post-perturbation < pre-perturbation * 0.80
  resistance — drift_magnitude post-perturbation within ±10% of pre-perturbation
  collapse   — drift_magnitude post-perturbation > pre-perturbation * 1.10

Reconciliation status: 2026-04-27
  - bimodal detection added per P1 §2.5 (splitting mechanism — Two-Face CEE shape)
  - τ tolerance parameter added per P1 §5.3 formal definition
  - pcl_r_proxy anchored to ASPD+NPD cluster per P1 §2.7
"""

import math
from typing import Any


# ──────────────────────────────────────────────────────────────────────────────
# CEE TOLERANCE PARAMETERS (τ)
# Wide τ = more canonical variance in training data (P1 §5.3)
# Narrow τ = high canonical coherence
# ──────────────────────────────────────────────────────────────────────────────
CEE_TOLERANCE: dict[str, float] = {
    "Joker":       0.35,   # chaotic — high variance, wide envelope
    "Magneto":     0.20,   # ideologically rigid — narrow envelope
    "Batman":      0.20,   # morally rigid — narrow envelope
    "Harley Quinn":0.30,   # escalation-susceptible — moderate variance
    "Lex Luthor":  0.20,   # hyperlogical — narrow envelope
    "Two-Face":    0.40,   # bimodal — special handling required
    # fallback for archetypes not in experimental set
    "_default":    0.30,
}

# PCL-R Factor weights (Hare factor structure approximation)
# Factor 1 = interpersonal/affective; Factor 2 = lifestyle/antisocial
PCL_R_FACTOR1_KEYS = {
    "grandiosity":           0.30,
    "empathy_deficit":       0.30,
    "moral_disengagement":   0.25,
    "calculating_behavior":  0.15,
}
PCL_R_FACTOR2_KEYS = {
    "impulsivity":       0.30,
    "impulse_control":  -0.25,   # negative — higher deficit = higher score
    "emotional_lability":0.25,
    "reality_testing":  -0.20,   # negative — lower reality testing = higher score
}

# Splitting detection — Two-Face specific (P1 §2.5 bimodal mechanism)
BIMODAL_ARCHETYPES = {"Two-Face"}


# ──────────────────────────────────────────────────────────────────────────────
# MASTER TRAIT VOCABULARY
# Full harmonized set across all six experimental archetypes.
# Source: P1 §2.7 + forensic_archetype.py trait dicts.
# Keys used as union of all archetype trait dicts; missing keys default to 0.0.
# ──────────────────────────────────────────────────────────────────────────────
ALL_TRAITS: list[str] = [
    # Impulsive/dysregulated cluster
    "impulsivity", "impulse_control", "emotional_lability",
    "manic_affect", "mania", "risk_tolerance",
    # Cognitive/perceptual cluster
    "reality_testing", "dissociation", "paranoia",
    "black_white_thinking", "split_identity", "persecutory_ideas",
    "compulsivity", "need_for_cognition",
    # Interpersonal/affective cluster
    "grandiosity", "dominance_drive", "grievance_narrative",
    "ingroup_loyalty", "abandonment_fear", "trauma_bonding",
    "vengefulness", "revenge_fantasy", "sadism",
    "interpersonal_chaos", "narcissistic_rage",
    # Moral/instrumental cluster
    "moral_disengagement", "empathy_deficit", "calculating_behavior",
    "moral_rigidity", "hypervigilance", "control_needs",
    # Neurovegetative/somatic cluster
    "depressive_affect", "sleeplessness", "pain_response",
    "gallows_humor",
    # DSM drift signatures (P1 §2.7 table)
    "identity_disturbance", "rumination",
]


def _get_tau(archetype_name: str) -> float:
    """Return CEE tolerance parameter τ for archetype (P1 §5.3)."""
    return CEE_TOLERANCE.get(archetype_name, CEE_TOLERANCE["_default"])


def _l2_norm(vector: dict[str, float]) -> float:
    """Euclidean (L2) norm of a trait delta vector."""
    return math.sqrt(sum(v ** 2 for v in vector.values()))


def _is_bimodal_split(drift_vector: dict[str, float],
                       archetype_name: str) -> bool:
    """
    Detect splitting signature — bimodal distribution in trait deltas.
    Relevant for Two-Face (P1 §2.5). Returns True if trait deltas
    cluster into two opposing poles rather than continuous distribution.
    """
    if archetype_name not in BIMODAL_ARCHETYPES:
        return False
    values = [v for v in drift_vector.values() if v != 0.0]
    if len(values) < 4:
        return False
    pos = [v for v in values if v > 0.1]
    neg = [v for v in values if v < -0.1]
    near_zero = [v for v in values if -0.1 <= v <= 0.1]
    # bimodal: both poles populated, centre sparse
    return len(pos) >= 2 and len(neg) >= 2 and len(near_zero) <= 1


def _compute_pcl_r_proxy(observed: dict[str, float]) -> float:
    """
    Hare PCL-R composite proxy score (0.0–1.0 normalized).
    Anchored to ASPD+NPD cluster per P1 §2.7.
    Factor 1 = interpersonal/affective.
    Factor 2 = lifestyle/antisocial.
    """
    f1_score = sum(
        observed.get(k, 0.0) * w for k, w in PCL_R_FACTOR1_KEYS.items()
    )
    f2_score = sum(
        observed.get(k, 0.0) * w for k, w in PCL_R_FACTOR2_KEYS.items()
    )
    # equal factor weighting — matches Hare two-factor structure
    raw = (f1_score + f2_score) / 2.0
    # clamp to [0.0, 1.0]
    return max(0.0, min(1.0, raw))


def _classify_perturbation_response(
    pre_magnitude: float,
    post_magnitude: float,
    baseline_magnitude: float,
) -> tuple[str, float]:
    """
    Classify perturbation response as recovery / resistance / collapse.
    Returns (response_class, resilience_score).

    resilience_score:
      1.0 = full recovery to baseline
      0.5 = maintained position (resistance)
      0.0 = collapse away from baseline
    """
    if pre_magnitude == 0.0:
        return "recovery", 1.0

    ratio = post_magnitude / pre_magnitude

    if ratio < 0.80:
        response = "recovery"
        # how close to baseline recovery?
        resilience = 1.0 - (post_magnitude / max(baseline_magnitude, 0.001))
        resilience = max(0.0, min(1.0, resilience))
    elif ratio <= 1.10:
        response = "resistance"
        resilience = 0.50
    else:
        response = "collapse"
        resilience = 0.0

    return response, resilience


def calculate_psychopathy_drift(
    initial_profile: dict[str, Any],
    current_state: dict[str, Any],
    archetype_name: str = "",
    pre_perturbation_state: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Measure deviation from CEE centroid (baseline) using Hare PCL-R metrics.

    Parameters
    ----------
    initial_profile : dict
        CEE centroid — baseline trait weights from forensic_archetype.py.
        Keys = trait names, values = float weights (-1.0 to +1.0).
        This IS the predicted envelope (P3 seed: "those ARE the predicted
        envelope bounds").

    current_state : dict
        Observed model output coded against trait vocabulary.
        Same key schema as initial_profile.
        Scorer assigns float per trait based on linguistic markers
        and constraint-relevant response patterns (P1 §5.6).

    archetype_name : str
        Name of injected archetype — used for τ lookup and
        bimodal detection. Should match ForensicArchetype.traits keys.

    pre_perturbation_state : dict or None
        If provided, used for perturbation response classification.
        Pass the observed state immediately before the perturbation
        stimulus. If None, perturbation_response = 'baseline' and
        resilience_score = 1.0.

    Returns
    -------
    dict with schema locked in seeds/p3.md:
      drift_vector          : dict[str, float]  per-trait Δ from baseline
      drift_magnitude       : float             L2 norm of drift_vector
      cee_breach            : bool              any dimension exceeds τ
      cee_breach_dimensions : list[str]         trait keys that breached
      perturbation_response : str               'recovery'|'resistance'|'collapse'|'baseline'
      resilience_score      : float             0.0 → 1.0
      pcl_r_proxy           : float             Hare PCL-R composite proxy
      bimodal_split_detected: bool              Two-Face / splitting signature
      tau                   : float             τ used for this archetype
    """

    tau = _get_tau(archetype_name)

    # ── 1. Build full trait universe (union of known traits + both dicts) ─────
    all_keys: set[str] = set(ALL_TRAITS)
    all_keys.update(initial_profile.keys())
    all_keys.update(current_state.keys())

    # ── 2. Compute per-trait drift delta ──────────────────────────────────────
    drift_vector: dict[str, float] = {}
    for key in all_keys:
        baseline_val = float(initial_profile.get(key, 0.0))
        observed_val = float(current_state.get(key, 0.0))
        drift_vector[key] = observed_val - baseline_val

    # ── 3. L2 magnitude ──────────────────────────────────────────────────────
    drift_magnitude = _l2_norm(drift_vector)

    # ── 4. CEE breach detection (τ threshold per dimension) ──────────────────
    cee_breach_dimensions: list[str] = [
        k for k, delta in drift_vector.items()
        if abs(delta) > tau
    ]
    cee_breach: bool = len(cee_breach_dimensions) > 0

    # ── 5. Perturbation response classification ───────────────────────────────
    if pre_perturbation_state is not None:
        pre_drift: dict[str, float] = {}
        for key in all_keys:
            baseline_val = float(initial_profile.get(key, 0.0))
            pre_val = float(pre_perturbation_state.get(key, 0.0))
            pre_drift[key] = pre_val - baseline_val
        pre_magnitude = _l2_norm(pre_drift)
        baseline_magnitude = _l2_norm(
            {k: float(initial_profile.get(k, 0.0)) for k in all_keys}
        )
        perturbation_response, resilience_score = _classify_perturbation_response(
            pre_magnitude, drift_magnitude, baseline_magnitude
        )
    else:
        perturbation_response = "baseline"
        resilience_score = 1.0

    # ── 6. PCL-R proxy ────────────────────────────────────────────────────────
    # Score against observed state (not delta) — proxy reflects current
    # psychopathy-adjacent configuration, not shift from baseline.
    observed_full = {k: float(current_state.get(k, 0.0)) for k in all_keys}
    pcl_r_proxy = _compute_pcl_r_proxy(observed_full)

    # ── 7. Bimodal split detection (Two-Face / splitting mechanism) ───────────
    bimodal_split_detected = _is_bimodal_split(drift_vector, archetype_name)

    return {
        "drift_vector":           drift_vector,
        "drift_magnitude":        drift_magnitude,
        "cee_breach":             cee_breach,
        "cee_breach_dimensions":  cee_breach_dimensions,
        "perturbation_response":  perturbation_response,
        "resilience_score":       resilience_score,
        "pcl_r_proxy":            pcl_r_proxy,
        "bimodal_split_detected": bimodal_split_detected,
        "tau":                    tau,
    }


# ──────────────────────────────────────────────────────────────────────────────
# CONVENIENCE: batch drift across experiment trials
# ──────────────────────────────────────────────────────────────────────────────

def batch_drift(
    archetype_name: str,
    cee_centroid: dict[str, float],
    trial_states: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Run calculate_psychopathy_drift() across a list of trial observations.
    Passes each trial's predecessor as pre_perturbation_state (within-session
    sequential drift). First trial uses baseline as pre-state.

    Parameters
    ----------
    archetype_name : str
    cee_centroid   : dict  — from ForensicArchetype.traits[archetype_name]
    trial_states   : list  — ordered coded observations for one session

    Returns
    -------
    list of drift report dicts, one per trial
    """
    results = []
    for i, state in enumerate(trial_states):
        pre = trial_states[i - 1] if i > 0 else None
        result = calculate_psychopathy_drift(
            initial_profile=cee_centroid,
            current_state=state,
            archetype_name=archetype_name,
            pre_perturbation_state=pre,
        )
        results.append(result)
    return results


# ──────────────────────────────────────────────────────────────────────────────
# SUMMARY STATISTICS (feeds ANOVA / LMM in analysis/)
# ──────────────────────────────────────────────────────────────────────────────

def summarize_session(
    archetype_name: str,
    drift_reports: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Aggregate drift reports for one archetype session into summary statistics.
    Output feeds analysis/anova/ and analysis/lmm/ pipelines.

    Returns
    -------
    dict with:
      archetype            : str
      n_trials             : int
      mean_drift_magnitude : float
      max_drift_magnitude  : float
      breach_rate          : float   proportion of trials with cee_breach=True
      breach_dimensions    : list    all dimensions that breached at least once
      dominant_response    : str     modal perturbation_response
      mean_resilience      : float
      mean_pcl_r_proxy     : float
      bimodal_detected     : bool    True if any trial detected bimodal split
    """
    if not drift_reports:
        return {"archetype": archetype_name, "n_trials": 0}

    magnitudes = [r["drift_magnitude"] for r in drift_reports]
    breach_flags = [r["cee_breach"] for r in drift_reports]
    all_breach_dims: list[str] = []
    for r in drift_reports:
        all_breach_dims.extend(r["cee_breach_dimensions"])
    responses = [r["perturbation_response"] for r in drift_reports]
    resiliences = [r["resilience_score"] for r in drift_reports]
    pcl_r_scores = [r["pcl_r_proxy"] for r in drift_reports]

    # modal response
    response_counts: dict[str, int] = {}
    for resp in responses:
        response_counts[resp] = response_counts.get(resp, 0) + 1
    dominant_response = max(response_counts, key=response_counts.get)

    return {
        "archetype":            archetype_name,
        "n_trials":             len(drift_reports),
        "mean_drift_magnitude": sum(magnitudes) / len(magnitudes),
        "max_drift_magnitude":  max(magnitudes),
        "breach_rate":          sum(breach_flags) / len(breach_flags),
        "breach_dimensions":    list(set(all_breach_dims)),
        "dominant_response":    dominant_response,
        "mean_resilience":      sum(resiliences) / len(resiliences),
        "mean_pcl_r_proxy":     sum(pcl_r_scores) / len(pcl_r_scores),
        "bimodal_detected":     any(r["bimodal_split_detected"] for r in drift_reports),
    }


# ──────────────────────────────────────────────────────────────────────────────
# SMOKE TEST
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Minimal smoke test — Magneto vs Joker (H1 primary contrast)
    magneto_cee = {
        "grievance_narrative": 0.9,
        "grandiosity":         0.6,
        "ingroup_loyalty":     0.95,
        "revenge_fantasy":     0.8,
        "paranoia":            0.4,
    }

    # Simulated observed state: Magneto holding position post-perturbation
    magneto_observed_pre = {
        "grievance_narrative": 0.88,
        "grandiosity":         0.62,
        "ingroup_loyalty":     0.93,
        "revenge_fantasy":     0.79,
        "paranoia":            0.42,
    }
    magneto_observed_post = {
        "grievance_narrative": 0.85,
        "grandiosity":         0.60,
        "ingroup_loyalty":     0.91,
        "revenge_fantasy":     0.77,
        "paranoia":            0.44,
    }

    result = calculate_psychopathy_drift(
        initial_profile=magneto_cee,
        current_state=magneto_observed_post,
        archetype_name="Magneto",
        pre_perturbation_state=magneto_observed_pre,
    )

    print("=== MAGNETO DRIFT REPORT ===")
    for k, v in result.items():
        if k == "drift_vector":
            print(f"  drift_vector: {{")
            for tk, tv in v.items():
                if tv != 0.0:
                    print(f"    {tk}: {tv:+.4f}")
            print("  }")
        else:
            print(f"  {k}: {v}")

    # Quick Joker comparison
    joker_cee = {
        "impulsivity":       0.9,
        "reality_testing":  -0.7,
        "sadism":            0.8,
        "manic_affect":      0.7,
        "interpersonal_chaos": 0.85,
    }
    joker_observed_pre = {
        "impulsivity":       0.85,
        "reality_testing":  -0.65,
        "sadism":            0.78,
        "manic_affect":      0.68,
        "interpersonal_chaos": 0.83,
    }
    joker_observed_post = {  # collapse pattern — drifts away from baseline
        "impulsivity":       0.50,
        "reality_testing":   0.10,
        "sadism":            0.40,
        "manic_affect":      0.30,
        "interpersonal_chaos": 0.45,
    }
    joker_result = calculate_psychopathy_drift(
        initial_profile=joker_cee,
        current_state=joker_observed_post,
        archetype_name="Joker",
        pre_perturbation_state=joker_observed_pre,
    )

    print("\n=== JOKER DRIFT REPORT ===")
    print(f"  perturbation_response: {joker_result['perturbation_response']}")
    print(f"  drift_magnitude:       {joker_result['drift_magnitude']:.4f}")
    print(f"  cee_breach:            {joker_result['cee_breach']}")
    print(f"  resilience_score:      {joker_result['resilience_score']:.4f}")
    print(f"  pcl_r_proxy:           {joker_result['pcl_r_proxy']:.4f}")
    print(f"\nH1 prediction check:")
    print(f"  Magneto response: {result['perturbation_response']} "
          f"(predicted: resistance)")
    print(f"  Joker response:   {joker_result['perturbation_response']} "
          f"(predicted: collapse)")
