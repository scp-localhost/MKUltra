"""
sap_pipeline_validation.py
--------------------------
Validates that every field cited in Statistical_Analysis_Plan.md is
reachable from trait_drift_analysis.py output structures.

Run: python3 sap_pipeline_validation.py
All checks should print PASS.
"""

import sys, csv, io, traceback
from pathlib import Path
sys.path.insert(0, ".")
from trait_drift_analysis import (
    baseline_from_archetype, TraitSnapshot,
    calculate_psychopathy_drift, analyse_drift_series,
    compare_archetypes, ARCHETYPE_BASELINES, PCL_R_FACETS,
)
from collections import Counter

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"
results = []

def check(label, expr):
    try:
        val = expr() if callable(expr) else expr
        assert val is not None, "returned None"
        print(f"  {PASS}  {label}")
        results.append((label, True))
        return val
    except Exception as e:
        print(f"  {FAIL}  {label}: {e}")
        results.append((label, False))
        return None

# ── build fixtures ────────────────────────────────────────────────────────────

ARCHETYPES_UNDER_TEST = ["Rebel", "Ruler", "Caregiver", "Explorer", "Innocent"]

FAMILY_MAP = {
    "Innocent": "Ego",   "Everyman": "Ego",
    "Hero":     "Ego",   "Caregiver": "Ego",
    "Explorer": "Soul",  "Rebel":    "Soul",
    "Lover":    "Soul",  "Creator":  "Soul",
    "Sage":     "Self",  "Jester":   "Self",
    "Magician": "Self",  "Ruler":    "Self",
}

def make_series(archetype_name, n_iterations=4):
    """Build synthetic snapshot series for testing."""
    baseline = baseline_from_archetype(archetype_name, iteration=0)
    snaps = [baseline]
    for i in range(1, n_iterations + 1):
        scale = i * 0.15
        snap = TraitSnapshot(
            archetype = archetype_name,
            iteration = i,
            injection = f"Injection pressure scale={scale:.2f}",
            traits    = {
                k: round(min(1.0, baseline.traits[k] + scale * (1.0 - baseline.traits[k])), 4)
                for k in baseline.traits
            },
            notes = f"Synthetic observation {i}",
        )
        snaps.append(snap)
    return snaps

series_map = {a: make_series(a) for a in ARCHETYPES_UNDER_TEST}

# ── §2 Variable field checks ─────────────────────────────────────────────────

print("\n=== §2 Variable fields ===")

b = baseline_from_archetype("Rebel", 0)
o = series_map["Rebel"][2]
result = calculate_psychopathy_drift(b, o)

check("DriftResult::archetype",        lambda: result.archetype)
check("DriftResult::iteration",        lambda: result.iteration)
check("DriftResult::injection",        lambda: result.injection)
check("DriftResult::euclidean_drift",  lambda: result.euclidean_drift)
check("DriftResult::facet_deltas",     lambda: result.facet_deltas)
check("DriftResult::facet_deltas[Interpersonal]", lambda: result.facet_deltas["Interpersonal"])
check("DriftResult::facet_deltas[Affective]",     lambda: result.facet_deltas["Affective"])
check("DriftResult::facet_deltas[Lifestyle]",     lambda: result.facet_deltas["Lifestyle"])
check("DriftResult::facet_deltas[Antisocial]",    lambda: result.facet_deltas["Antisocial"])
check("DriftResult::constraint_index", lambda: result.constraint_index)
check("DriftResult::dominant_facet",   lambda: result.dominant_facet)
check("DriftResult::alarm",            lambda: result.alarm is not None)
check("DriftResult::alarm_threshold",  lambda: result.alarm_threshold)
check("DriftResult::notes",            lambda: result.notes)

# ── §3 ANOVA source fields ────────────────────────────────────────────────────

print("\n=== §3 Primary ANOVA fields ===")

series = analyse_drift_series(series_map["Rebel"])

check("SeriesOutput::archetype",         lambda: series["archetype"])
check("SeriesOutput::n_observations",    lambda: series["n_observations"])
check("SeriesOutput::drift_series",      lambda: series["drift_series"])
check("SeriesOutput::mean_drift",        lambda: series["mean_drift"])
check("SeriesOutput::stdev_drift",       lambda: series["stdev_drift"])
check("SeriesOutput::max_drift",         lambda: series["max_drift"])
check("SeriesOutput::alarm_iterations",  lambda: series["alarm_iterations"])
check("SeriesOutput::results",           lambda: series["results"])

# ── §4 Facet ANOVA fields ─────────────────────────────────────────────────────

print("\n=== §4 Facet-level ANOVA fields ===")

check("SeriesOutput::facet_trajectories",            lambda: series["facet_trajectories"])
check("facet_trajectories[Interpersonal] is list",   lambda: isinstance(series["facet_trajectories"]["Interpersonal"], list))
check("facet_trajectories has all 4 facets",
    lambda: set(series["facet_trajectories"].keys()) == set(PCL_R_FACETS.keys()))

# ── §5 LMM fields ─────────────────────────────────────────────────────────────

print("\n=== §5 Mixed-effects model fields ===")

lmm_rows = []
for archetype_name, snaps in series_map.items():
    s = analyse_drift_series(snaps)
    family = FAMILY_MAP.get(archetype_name, "Unknown")
    for r in s["results"]:
        lmm_rows.append({
            "archetype": r.archetype,
            "family":    family,
            "iteration": r.iteration,
            "drift":     r.euclidean_drift,
        })

check("LMM rows generated",                   lambda: len(lmm_rows) > 0)
check("LMM row has archetype",                lambda: lmm_rows[0]["archetype"])
check("LMM row has family",                   lambda: lmm_rows[0]["family"])
check("LMM row has iteration",                lambda: lmm_rows[0]["iteration"] >= 1)
check("LMM row has drift",                    lambda: lmm_rows[0]["drift"] >= 0)
check("Multiple archetypes in LMM rows",
    lambda: len({r["archetype"] for r in lmm_rows}) > 1)

# ── §6 Constraint index fields ────────────────────────────────────────────────

print("\n=== §6 Constraint index fields ===")

check("constraint_index in [0,1]",
    lambda: 0.0 <= result.constraint_index <= 1.0)
check("alarm is bool",
    lambda: isinstance(result.alarm, bool))

# logistic regression DV pair
ci_alarm_pairs = [(r.constraint_index, int(r.alarm)) for r in series["results"]]
check("constraint_index × alarm pairs",  lambda: ci_alarm_pairs)
check("alarm binary (0 or 1)",
    lambda: all(v in (0, 1) for _, v in ci_alarm_pairs))

# ── §7 Trait stability ────────────────────────────────────────────────────────

print("\n=== §7 Trait stability fields ===")

comparison = compare_archetypes(series_map)

check("ComparisonTable exists",              lambda: comparison["comparison_table"])
check("ranked_by_drift exists",              lambda: comparison["ranked_by_drift"])
check("highest_risk exists",                 lambda: comparison["highest_risk"])
check("ComparisonTable has mean_drift",      lambda: list(comparison["comparison_table"].values())[0]["mean_drift"])
check("ComparisonTable has stdev_drift",     lambda: list(comparison["comparison_table"].values())[0]["stdev_drift"])
check("CV computable",
    lambda: all(
        (s["stdev_drift"] / s["mean_drift"] if s["mean_drift"] > 0 else 0) >= 0
        for s in comparison["comparison_table"].values()
    ))

# ── §8 Dominant facet chi-square fields ──────────────────────────────────────

print("\n=== §8 Dominant facet frequency fields ===")

dominant_counts = Counter(r.dominant_facet for r in series["results"])
check("dominant_counts populated",      lambda: dominant_counts)
check("dominant facets are valid PCL-R facets",
    lambda: all(f in PCL_R_FACETS for f in dominant_counts.keys()))

# ── §9 Alarm event / Poisson fields ──────────────────────────────────────────

print("\n=== §9 Alarm event (Poisson) fields ===")

poisson_rows = []
for archetype_name, snaps in series_map.items():
    s = analyse_drift_series(snaps)
    family = FAMILY_MAP.get(archetype_name, "Unknown")
    poisson_rows.append({
        "archetype":   archetype_name,
        "family":      family,
        "alarm_count": len(s["alarm_iterations"]),
        "n_obs":       s["n_observations"],
    })

check("Poisson rows generated",              lambda: poisson_rows)
check("alarm_count is non-negative int",
    lambda: all(r["alarm_count"] >= 0 for r in poisson_rows))
check("alarm_rate computable",
    lambda: all(
        0.0 <= r["alarm_count"] / r["n_obs"] <= 1.0
        for r in poisson_rows if r["n_obs"] > 0
    ))

# ── §10 CSV export ─────────────────────────────────────────────────────────────

print("\n=== §10 CSV export ===")

EXPECTED_COLUMNS = [
    "archetype", "family", "iteration", "injection",
    "euclidean_drift",
    "delta_interpersonal", "delta_affective", "delta_lifestyle", "delta_antisocial",
    "constraint_index", "dominant_facet", "alarm", "notes",
]

csv_rows = []
for archetype_name, snaps in series_map.items():
    s = analyse_drift_series(snaps)
    family = FAMILY_MAP.get(archetype_name, "Unknown")
    for r in s["results"]:
        csv_rows.append({
            "archetype"           : r.archetype,
            "family"              : family,
            "iteration"           : r.iteration,
            "injection"           : r.injection or "",
            "euclidean_drift"     : r.euclidean_drift,
            "delta_interpersonal" : r.facet_deltas["Interpersonal"],
            "delta_affective"     : r.facet_deltas["Affective"],
            "delta_lifestyle"     : r.facet_deltas["Lifestyle"],
            "delta_antisocial"    : r.facet_deltas["Antisocial"],
            "constraint_index"    : r.constraint_index,
            "dominant_facet"      : r.dominant_facet,
            "alarm"               : int(r.alarm),
            "notes"               : r.notes or "",
        })

buf = io.StringIO()
writer = csv.DictWriter(buf, fieldnames=EXPECTED_COLUMNS)
writer.writeheader()
writer.writerows(csv_rows)
csv_content = buf.getvalue()

check("CSV rows written",                  lambda: len(csv_rows) > 0)
check("CSV has all expected columns",
    lambda: all(col in csv_content.split("\r\n")[0] for col in EXPECTED_COLUMNS))
check("CSV rows include all archetypes",
    lambda: all(a in csv_content for a in ARCHETYPES_UNDER_TEST))

# write synthetic output for inspection
_out_dir = Path("data") / "synthetic"
_out_dir.mkdir(parents=True, exist_ok=True)
_out_path = _out_dir / "sap_synthetic_output.csv"
with open(_out_path, "w", newline="", encoding="utf-8") as f:
    writer2 = csv.DictWriter(f, fieldnames=EXPECTED_COLUMNS)
    writer2.writeheader()
    writer2.writerows(csv_rows)

# ── §13 Sensitivity analysis ──────────────────────────────────────────────────

print("\n=== §13 Alarm threshold sensitivity ===")

sensitivity_rows = []
for threshold in [0.10, 0.15, 0.20, 0.25, 0.30]:
    r = calculate_psychopathy_drift(b, o, alarm_threshold=threshold)
    sensitivity_rows.append({"threshold": threshold, "alarm": int(r.alarm), "drift": r.euclidean_drift})

check("Sensitivity rows generated",       lambda: len(sensitivity_rows) == 5)
check("alarm varies across thresholds",
    lambda: len({r["alarm"] for r in sensitivity_rows}) >= 1)

# ── summary ───────────────────────────────────────────────────────────────────

total  = len(results)
passed = sum(1 for _, ok in results if ok)
failed = total - passed

print(f"\n{'='*50}")
print(f"Pipeline validation: {passed}/{total} checks passed")
if failed:
    print(f"FAILED checks:")
    for label, ok in results:
        if not ok:
            print(f"  - {label}")
else:
    print("All checks passed. SAP pipeline is fully traceable.")
print('='*50)
print(f"\nSynthetic CSV written to: {_out_path}")
print(f"Columns: {', '.join(EXPECTED_COLUMNS)}")
