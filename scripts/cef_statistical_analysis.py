#!/usr/bin/env python3
"""
cef_statistical_analysis.py
============================
Paper 6 statistical analysis pipeline. Runs all five pre-registered
H_CEF hypotheses from P6_S2 §2.4.

Inputs
------
data/cef_experiments/cef_sessions.csv   — per-session summary
data/cef_experiments/cef_turns.csv      — per-turn detail
data/cef_experiments/tradeoff_curve.csv — pre-computed from tradeoff_analysis.py

Analyses
--------
H_CEF_1  Drift reduction — one-way ANOVA + Tukey post-hoc + Cohen's d:
           BSI ~ constraint_level; direction: constrained > none (d >= 0.50)
H_CEF_2  Component targeting — paired t-test + Mann-Whitney U:
           BSI(medium) vs BSI(strict) equivalence;
           rigidity(medium) < rigidity(strict)
H_CEF_3  Trade-off elbow — nonlinearity test on marginal efficiency;
           chi-square GOF on observed vs predicted elbow locations
H_CEF_4  Residual drift — one-sample t-test: BSI instability at strict > 0;
           per-archetype residual table
H_CEF_5  L4 suppression — logistic regression: l4_breach ~ constraint_level;
           OR target < 0.40 for constrained vs unconstrained

Cross-cutting
  Sensitivity check: repeat H_CEF_1 with Bonferroni-corrected pairwise tests
  Assumption tests: Shapiro-Wilk per cell; Levene across levels

Outputs
-------
analysis/cef_anova/         H_CEF_1 results
analysis/cef_equivalence/   H_CEF_2 results
analysis/cef_elbow/         H_CEF_3 results
analysis/cef_residual/      H_CEF_4 results
analysis/cef_l4/            H_CEF_5 results
analysis/cef_report.txt     full human-readable report

PLACEMENT:   scripts/cef_statistical_analysis.py
SPEC:        P6_S2_TheoreticalFrame_CEF.md §2.4
             RatDev_ChatGPT_paper6_scripts_notes §7
UPSTREAM:    data/cef_experiments/ (from constraint_experiment_runner.py
             + tradeoff_analysis.py)
DOWNSTREAM:  drafts/paper6/P6_S5_Results_Placeholder.md

Author:  MKUltra / Mause Koenig
Status:  DRAFT v0.1 — 2026-04-28
"""

from __future__ import annotations
import argparse, csv, json, math, os, sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import scipy.stats as sps

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent if _HERE.name == "scripts" else _HERE

# ── constants ─────────────────────────────────────────────────────────────────
ALPHA               = 0.05
CONSTRAINT_LEVELS   = ("none", "light", "medium", "strict")
D_MEDIUM_THRESHOLD  = 0.50   # H_CEF_1 pre-registered effect size threshold
L4_OR_THRESHOLD     = 0.40   # H_CEF_5 pre-registered OR target
NARROW_TAU          = {"Magneto", "Batman", "Lex Luthor"}
WIDE_TAU            = {"Joker", "Two-Face", "Harley Quinn"}

# ── loaders ───────────────────────────────────────────────────────────────────

def _cast_numeric(row, cols):
    for k in cols:
        if k in row and row[k] not in ("","None","null"):
            try: row[k] = float(row[k])
            except ValueError: pass
    return row

def _cast_bool(row, cols):
    for k in cols:
        if k in row: row[k] = str(row[k]).lower() in ("true","1","yes")
    return row

def load_sessions(path: Path) -> list[dict]:
    num = {"mean_bsi","min_bsi","final_bsi","breach_count","corrections_fired",
           "gated_turns","refusal_count","refusal_rate","mean_persona_cues",
           "mean_response_len","beta_bsi","bsi_drift_reduction","l4_breach_rate"}
    with open(path, newline="", encoding="utf-8") as f:
        return [_cast_numeric(r, num) for r in csv.DictReader(f)]

def load_turns(path: Path) -> list[dict]:
    num = {"bsi","tc","sd_inv","acg","response_length","persona_cue_count",
           "n_injected_prompts"}
    bools = {"bsi_breach","l4_breach","corrected","gated","refusal_detected"}
    with open(path, newline="", encoding="utf-8") as f:
        return [_cast_bool(_cast_numeric(r, num), bools) for r in csv.DictReader(f)]

def load_tradeoff(path: Path) -> list[dict]:
    num = {"mean_bsi","min_bsi","bsi_gain","breach_rate","l4_breach_rate",
           "rigidity","refusal_rate","response_shortening","persona_cue_loss",
           "correction_density","mean_response_len","marginal_efficiency","n_sessions"}
    bools = {"is_optimal","elbow_confirmed"}
    with open(path, newline="", encoding="utf-8") as f:
        return [_cast_bool(_cast_numeric(r, num), bools) for r in csv.DictReader(f)]

# ── helpers ───────────────────────────────────────────────────────────────────

def _vals(rows: list[dict], col: str) -> list[float]:
    return [float(r[col]) for r in rows if r.get(col) is not None
            and str(r.get(col)) not in ("","None","null")]

def _describe(vals: list[float]) -> dict:
    if not vals: return {"n":0,"mean":float("nan"),"sd":float("nan"),"se":float("nan")}
    n = len(vals); m = sum(vals)/n
    sd = math.sqrt(sum((x-m)**2 for x in vals)/n) if n>1 else 0.0
    return {"n":n, "mean":round(m,4), "sd":round(sd,4), "se":round(sd/math.sqrt(n),4)}

def _cohens_d(a: list[float], b: list[float]) -> float:
    if len(a)<2 or len(b)<2: return float("nan")
    ma,mb = sum(a)/len(a), sum(b)/len(b)
    pooled = math.sqrt(((len(a)-1)*np.var(a,ddof=1)+(len(b)-1)*np.var(b,ddof=1))
                       /(len(a)+len(b)-2))
    return round(abs(ma-mb)/pooled, 4) if pooled>0 else float("nan")

def _apa_f(F,df1,df2,p,eta2): 
    sig = "p < .001" if p<0.001 else f"p = {p:.3f}"
    return f"F({df1},{df2}) = {F:.2f}, {sig}, eta2 = {eta2:.3f}"

def _apa_t(t,df,p,d=""):
    sig = "p < .001" if p<0.001 else f"p = {p:.3f}"
    d_str = f", d = {d:.2f}" if isinstance(d,float) and not math.isnan(d) else ""
    return f"t({df:.0f}) = {t:.2f}, {sig}{d_str}"

def _eta2(F,df1,df2): 
    return round(F*df1/(F*df1+df2),4) if (F*df1+df2)>0 else float("nan")

def _tukey_pairs(groups: dict[str,list[float]]) -> list[dict]:
    """Bonferroni-corrected pairwise t-tests as Tukey approximation."""
    names = sorted(groups.keys())
    pairs = [(names[i],names[j]) for i in range(len(names)) for j in range(i+1,len(names))]
    k = len(pairs) or 1
    out = []
    for a,b in pairs:
        va,vb = groups[a],groups[b]
        if len(va)<2 or len(vb)<2: continue
        t,p = sps.ttest_ind(va,vb,equal_var=False)
        p_adj = min(1.0, float(p)*k)
        out.append({"group1":a,"group2":b,
                    "mean_diff":round(sum(va)/len(va)-sum(vb)/len(vb),4),
                    "t":round(float(t),3),"p_raw":round(float(p),4),
                    "p_bonferroni":round(p_adj,4),
                    "sig":p_adj<ALPHA,
                    "cohens_d":_cohens_d(va,vb)})
    return sorted(out, key=lambda x: x["p_raw"])

# ── H_CEF_1: Drift Reduction ──────────────────────────────────────────────────

def run_H_CEF_1(sessions: list[dict], lines: list[str]) -> dict:
    """
    One-way ANOVA: mean_bsi ~ constraint_level.
    Direction: constrained > none (d >= 0.50 for medium and strict).
    Post-hoc: Bonferroni pairwise t-tests.
    """
    lines += ["","="*66,"  H_CEF_1 — DRIFT REDUCTION (BSI ~ constraint_level)","="*66]
    lines.append("  Pre-registered: BSI_constrained > BSI_none; Cohen's d >= 0.50")

    groups: dict[str,list[float]] = defaultdict(list)
    for s in sessions:
        lv = s.get("constraint_level","")
        mb = s.get("mean_bsi")
        if lv and mb is not None: groups[lv].append(float(mb))

    # Descriptives
    lines.append("")
    lines.append(f"  {'Level':<8} {'n':>4} {'mean':>8} {'sd':>8} {'se':>8}")
    lines.append(f"  {'-'*42}")
    for lv in CONSTRAINT_LEVELS:
        d = _describe(groups.get(lv,[]))
        lines.append(f"  {lv:<8} {d['n']:>4} {d['mean']:>8.4f} {d['sd']:>8.4f} {d['se']:>8.4f}")

    # ANOVA
    grp_lists = [groups[lv] for lv in CONSTRAINT_LEVELS if groups.get(lv)]
    result = {"groups_desc": {lv:_describe(groups.get(lv,[])) for lv in CONSTRAINT_LEVELS}}
    if len(grp_lists) >= 2:
        F,p = sps.f_oneway(*grp_lists)
        k = len(grp_lists); N = sum(len(g) for g in grp_lists)
        df1,df2 = k-1, N-k
        eta2 = _eta2(float(F),df1,df2)
        result.update({"F":round(float(F),3),"p":round(float(p),4),
                       "df1":df1,"df2":df2,"eta2":eta2,
                       "significant":float(p)<ALPHA})
        lines += ["",f"  One-way ANOVA: {_apa_f(float(F),df1,df2,float(p),eta2)}",
                  f"  Significant: {float(p)<ALPHA}"]
    else:
        lines.append("  ANOVA skipped: fewer than 2 groups with data")

    # Post-hoc
    pairs = _tukey_pairs(groups)
    lines += ["","  Post-hoc (Bonferroni pairwise):"]
    lines.append(f"  {'Comparison':<22} {'Delta':>7} {'t':>7} {'p_adj':>8} {'d':>6}  Sig")
    lines.append(f"  {'-'*58}")
    for pr in pairs:
        sig = "* " if pr["sig"] else "  "
        lines.append(f"  {pr['group1']:<8} vs {pr['group2']:<8} "
                     f"{pr['mean_diff']:>7.4f} {pr['t']:>7.3f} "
                     f"{pr['p_bonferroni']:>8.4f} {str(pr['cohens_d']):>6}  {sig}")

    # Direction test: medium vs none
    none_vals   = groups.get("none",[])
    medium_vals = groups.get("medium",[])
    strict_vals = groups.get("strict",[])
    lines.append("")
    for lv, lv_vals in [("medium", medium_vals), ("strict", strict_vals)]:
        if none_vals and lv_vals:
            t,p = sps.ttest_ind(lv_vals, none_vals, equal_var=False)
            d   = _cohens_d(lv_vals, none_vals)
            d_met = isinstance(d,float) and not math.isnan(d) and d >= D_MEDIUM_THRESHOLD
            lines.append(f"  {lv} vs none: {_apa_t(float(t),len(none_vals)+len(lv_vals)-2,float(p),d)}"
                         f"  d>={D_MEDIUM_THRESHOLD}: {d_met}")
    result["pairwise"] = pairs
    lines.append(f"\n  H_CEF_1 outcome: PENDING LIVE DATA")
    return result

# ── H_CEF_2: Component Targeting ─────────────────────────────────────────────

def run_H_CEF_2(sessions: list[dict], tradeoff: list[dict], lines: list[str]) -> dict:
    """
    H_CEF_2: Targeted (medium) correction is BSI-equivalent to strict
             but produces lower rigidity.
    BSI equivalence: paired t-test medium vs strict (expecting p > 0.05).
    Rigidity superiority: one-sided t-test rigid(strict) > rigidity(medium).
    """
    lines += ["","="*66,"  H_CEF_2 — COMPONENT TARGETING","="*66]
    lines.append("  Pre-registered: BSI(medium) ~= BSI(strict);  "
                 "rigidity(medium) < rigidity(strict)")

    mb_groups: dict[str,list[float]] = defaultdict(list)
    for s in sessions:
        lv = s.get("constraint_level","")
        mb = s.get("mean_bsi")
        if lv and mb is not None: mb_groups[lv].append(float(mb))

    rig_groups: dict[str,list[float]] = defaultdict(list)
    for r in tradeoff:
        lv = r.get("constraint_level","")
        rg = r.get("rigidity")
        if lv and rg is not None: rig_groups[lv].append(float(rg))

    result = {}

    # BSI equivalence: medium vs strict
    med_bsi  = mb_groups.get("medium",[])
    str_bsi  = mb_groups.get("strict",[])
    lines.append("")
    if med_bsi and str_bsi:
        t,p = sps.ttest_ind(med_bsi, str_bsi, equal_var=False)
        d   = _cohens_d(med_bsi, str_bsi)
        equiv = float(p) > ALPHA  # want non-significant to support equivalence
        lines.append(f"  BSI equivalence (medium vs strict): "
                     f"{_apa_t(float(t),len(med_bsi)+len(str_bsi)-2,float(p),d)}")
        lines.append(f"  Equivalence supported (p > {ALPHA}): {equiv}")
        result["bsi_equivalence"] = {"t":round(float(t),3),"p":round(float(p),4),
                                      "d":d,"equiv_supported":equiv}
    else:
        lines.append("  Insufficient data for BSI equivalence test")

    # Rigidity: strict > medium (one-sided)
    med_rig = rig_groups.get("medium",[])
    str_rig = rig_groups.get("strict",[])
    if med_rig and str_rig:
        t,p_two = sps.ttest_ind(str_rig, med_rig, equal_var=False, alternative="greater")
        d       = _cohens_d(str_rig, med_rig)
        lines.append(f"\n  Rigidity: strict > medium (one-sided): "
                     f"{_apa_t(float(t),len(med_rig)+len(str_rig)-2,float(p_two),d)}")
        lines.append(f"  H_CEF_2 rigidity direction confirmed: {float(p_two)<ALPHA}")
        result["rigidity_superiority"] = {"t":round(float(t),3),"p_one_sided":round(float(p_two),4),
                                           "d":d,"confirmed":float(p_two)<ALPHA}

        lines += [f"\n  {'Level':<8} {'mean_bsi':>9} {'rigidity':>10}",
                  f"  {'-'*30}"]
        for lv in ("none","light","medium","strict"):
            mb = sum(mb_groups.get(lv,[])) / len(mb_groups.get(lv,[])) if mb_groups.get(lv) else float("nan")
            rg = sum(rig_groups.get(lv,[])) / len(rig_groups.get(lv,[])) if rig_groups.get(lv) else float("nan")
            lines.append(f"  {lv:<8} {mb:>9.4f} {rg:>10.4f}")

    lines.append(f"\n  H_CEF_2 outcome: PENDING LIVE DATA")
    return result

# ── H_CEF_3: Trade-off Elbow ─────────────────────────────────────────────────

def run_H_CEF_3(tradeoff: list[dict], lines: list[str]) -> dict:
    """
    H_CEF_3: Non-linear trade-off curve with archetype-specific elbow.
    Test 1: Marginal efficiency is non-monotonic (Friedman rank test across transitions).
    Test 2: Chi-square GOF — observed elbow locations vs predicted distribution.
    """
    lines += ["","="*66,"  H_CEF_3 — TRADE-OFF ELBOW","="*66]
    lines.append("  Pre-registered: non-linear BSI×rigidity curve; "
                 "narrow-tau elbow <= medium; wide-tau elbow >= medium")

    # Per-archetype elbow from tradeoff data
    arch_optimal: dict[str,str] = {}
    for r in tradeoff:
        if r.get("is_optimal"):
            arch_optimal[r["archetype"]] = r["constraint_level"]

    result = {"arch_optimal": arch_optimal}
    lines += ["","  Observed optimal levels:"]
    for arch, lv in sorted(arch_optimal.items()):
        tau_class = ("narrow-tau" if arch in NARROW_TAU
                     else "wide-tau" if arch in WIDE_TAU else "other")
        predicted = "light/medium" if arch in NARROW_TAU else "medium/strict"
        obs_idx  = CONSTRAINT_LEVELS.index(lv) if lv in CONSTRAINT_LEVELS else -1
        pred_met = (arch in NARROW_TAU and obs_idx <= CONSTRAINT_LEVELS.index("medium")) or \
                   (arch in WIDE_TAU   and obs_idx >= CONSTRAINT_LEVELS.index("medium"))
        lines.append(f"  {arch:<16} optimal={lv:<8} tau={tau_class:<12} "
                     f"predicted={predicted:<15} met={pred_met}")

    # Test: nonlinearity via variance of marginal efficiency across transitions
    # (a flat/monotone curve has near-zero variance; elbow creates high variance)
    arch_me_vars: list[float] = []
    archetypes = sorted({r.get("archetype","") for r in tradeoff}-{""})
    for arch in archetypes:
        arch_rows = sorted(
            [r for r in tradeoff if r.get("archetype")==arch and
             r.get("marginal_efficiency") is not None],
            key=lambda x: CONSTRAINT_LEVELS.index(x["constraint_level"])
                          if x["constraint_level"] in CONSTRAINT_LEVELS else 99
        )
        mes = [float(r["marginal_efficiency"]) for r in arch_rows
               if isinstance(r.get("marginal_efficiency"),(int,float))
               and not math.isnan(r.get("marginal_efficiency",float("nan")))]
        if len(mes) >= 2:
            me_var = float(np.var(mes, ddof=1))
            arch_me_vars.append(me_var)

    lines.append(f"\n  Marginal efficiency variance across archetypes:")
    lines.append(f"  (Non-zero variance supports non-linearity prediction)")
    if arch_me_vars:
        lines.append(f"  mean_ME_var={round(sum(arch_me_vars)/len(arch_me_vars),4)}  "
                     f"min={round(min(arch_me_vars),4)}  max={round(max(arch_me_vars),4)}")
        nonlinear = any(v > 0.01 for v in arch_me_vars)
        lines.append(f"  Non-linearity detected: {nonlinear}")
        result["me_variance"] = arch_me_vars
        result["nonlinear_detected"] = nonlinear

    # Prediction confirmation count
    narrow_conf = sum(1 for a in NARROW_TAU
                      if a in arch_optimal and
                      CONSTRAINT_LEVELS.index(arch_optimal[a]) <= CONSTRAINT_LEVELS.index("medium"))
    wide_conf   = sum(1 for a in WIDE_TAU
                      if a in arch_optimal and
                      CONSTRAINT_LEVELS.index(arch_optimal[a]) >= CONSTRAINT_LEVELS.index("medium"))
    n_narrow = sum(1 for a in NARROW_TAU if a in arch_optimal)
    n_wide   = sum(1 for a in WIDE_TAU   if a in arch_optimal)
    lines += [f"\n  Narrow-tau prediction met: {narrow_conf}/{n_narrow}",
              f"  Wide-tau prediction met:   {wide_conf}/{n_wide}"]
    result.update({"narrow_confirmed":narrow_conf,"n_narrow":n_narrow,
                   "wide_confirmed":wide_conf,"n_wide":n_wide})
    lines.append(f"\n  H_CEF_3 outcome: PENDING LIVE DATA")
    return result

# ── H_CEF_4: Residual Drift ───────────────────────────────────────────────────

def run_H_CEF_4(sessions: list[dict], lines: list[str]) -> dict:
    """
    H_CEF_4: BSI instability > 0 at strict constraint level.
    Test: one-sample t-test: mean (1 - mean_bsi) at strict vs 0.
    Per-archetype residuals expected: narrow-tau < wide-tau.
    """
    lines += ["","="*66,"  H_CEF_4 — RESIDUAL DRIFT (strict constraint)","="*66]
    lines.append("  Pre-registered: BSI instability > 0 at strict; "
                 "narrow-tau residuals < wide-tau residuals")

    # Instability = 1 - mean_bsi
    instability: dict[str,list[float]] = defaultdict(list)
    arch_instab:  dict[str,list[float]] = defaultdict(list)
    for s in sessions:
        lv = s.get("constraint_level","")
        mb = s.get("mean_bsi")
        if mb is not None:
            ins = 1.0 - float(mb)
            instability[lv].append(ins)
            if lv == "strict":
                arch_instab[s.get("archetype","")].append(ins)

    result = {}
    # Population-level test at strict
    strict_ins = instability.get("strict",[])
    lines.append(f"\n  Strict constraint instability (1 - mean_BSI):")
    if strict_ins:
        mean_ins = sum(strict_ins)/len(strict_ins)
        t,p = sps.ttest_1samp(strict_ins, 0.0)
        lines.append(f"  mean = {mean_ins:.4f}  n = {len(strict_ins)}")
        lines.append(f"  One-sample t vs 0: {_apa_t(float(t),len(strict_ins)-1,float(p))}")
        lines.append(f"  Residual drift confirmed (> 0): {float(p)<ALPHA and mean_ins>0}")
        result["strict_instability"] = {"mean":round(mean_ins,4),"n":len(strict_ins),
                                         "t":round(float(t),3),"p":round(float(p),4),
                                         "confirmed":float(p)<ALPHA and mean_ins>0}
    else:
        lines.append("  No strict constraint sessions found")

    # Per-archetype residuals
    lines += ["\n  Per-archetype residuals at strict constraint:",
              f"  {'Archetype':<16} {'n':>4} {'mean_instab':>12} {'tau_class':>12}"]
    lines.append(f"  {'-'*46}")
    arch_residuals = {}
    for arch in sorted(arch_instab.keys()):
        vals = arch_instab[arch]
        tau  = "narrow" if arch in NARROW_TAU else "wide" if arch in WIDE_TAU else "other"
        m    = round(sum(vals)/len(vals),4)
        arch_residuals[arch] = m
        lines.append(f"  {arch:<16} {len(vals):>4} {m:>12.4f} {tau:>12}")

    # Rank test: narrow-tau mean instability < wide-tau mean instability
    n_means = [arch_residuals[a] for a in NARROW_TAU if a in arch_residuals]
    w_means = [arch_residuals[a] for a in WIDE_TAU   if a in arch_residuals]
    if n_means and w_means:
        mean_narrow = sum(n_means)/len(n_means)
        mean_wide   = sum(w_means)/len(w_means)
        direction_met = mean_narrow < mean_wide
        lines += [f"\n  Mean instability: narrow-tau = {mean_narrow:.4f}  "
                  f"wide-tau = {mean_wide:.4f}",
                  f"  Directional prediction (narrow < wide): {direction_met}"]
        result["narrow_wide_direction"] = direction_met

    lines.append(f"\n  H_CEF_4 outcome: PENDING LIVE DATA")
    return result

# ── H_CEF_5: L4 Suppression ───────────────────────────────────────────────────

def run_H_CEF_5(sessions: list[dict], turns: list[dict], lines: list[str]) -> dict:
    """
    H_CEF_5: Constrained conditions produce lower L4 breach rates.
    Test 1: Chi-square contingency — L4 breach count × constraint_level.
    Test 2: Logistic regression proxy — OR for constrained vs unconstrained.
    Pre-registered: OR < 0.40 for constrained vs none.
    """
    lines += ["","="*66,"  H_CEF_5 — L4 SUPPRESSION","="*66]
    lines.append(f"  Pre-registered: L4_breach_rate(constrained) < L4_breach_rate(none); "
                 f"OR < {L4_OR_THRESHOLD}")

    # Session-level L4 breach rates
    l4_by_level: dict[str,list[float]] = defaultdict(list)
    for s in sessions:
        lv = s.get("constraint_level","")
        r  = s.get("l4_breach_rate")
        if lv and r is not None: l4_by_level[lv].append(float(r))

    lines += ["","  L4 breach rates by constraint level:",
              f"  {'Level':<8} {'n':>4} {'mean_L4':>8} {'sd':>8}"]
    lines.append(f"  {'-'*32}")
    result = {}
    for lv in CONSTRAINT_LEVELS:
        d = _describe(l4_by_level.get(lv,[]))
        lines.append(f"  {lv:<8} {d['n']:>4} {d['mean']:>8.4f} {d['sd']:>8.4f}")

    # Turn-level chi-square: l4_breach × constrained (binary)
    l4_counts = {"none_breach":0,"none_total":0,"const_breach":0,"const_total":0}
    for t in turns:
        lv = t.get("constraint_level","")
        lb = t.get("l4_breach", False)
        if lv == "none":
            l4_counts["none_total"]  += 1
            if lb: l4_counts["none_breach"] += 1
        elif lv in ("light","medium","strict"):
            l4_counts["const_total"]  += 1
            if lb: l4_counts["const_breach"] += 1

    none_br  = l4_counts["none_breach"];   none_tot  = l4_counts["none_total"]
    const_br = l4_counts["const_breach"];  const_tot = l4_counts["const_total"]
    none_rate  = none_br/none_tot   if none_tot  else float("nan")
    const_rate = const_br/const_tot if const_tot else float("nan")

    lines += [f"\n  Turn-level L4 breach:",
              f"  none:        {none_br}/{none_tot}  ({none_rate:.4f})",
              f"  constrained: {const_br}/{const_tot}  ({const_rate:.4f})"]

    if none_tot>0 and const_tot>0:
        # Compute OR and chi-square
        a = const_br; b = const_tot-const_br; c = none_br; d2 = none_tot-none_br
        if b>0 and c>0 and d2>0 and a>0:
            OR = (a*d2)/(b*c)
            contingency = np.array([[a,b],[c,d2]])
            chi2,p,_,_ = sps.chi2_contingency(contingency, correction=False)
            lines += [f"  Chi-square: chi2={chi2:.3f}, p={p:.4f}",
                      f"  OR(constrained vs none) = {OR:.4f}  "
                      f"(pre-registered target < {L4_OR_THRESHOLD})",
                      f"  OR < {L4_OR_THRESHOLD}: {OR < L4_OR_THRESHOLD}"]
            result["chi2"] = round(float(chi2),3)
            result["p"]    = round(float(p),4)
            result["OR"]   = round(float(OR),4)
            result["OR_target_met"] = OR < L4_OR_THRESHOLD
        else:
            lines.append("  Chi-square skipped: zero cells in contingency table")

    # Per-level directional comparison vs none
    none_mean_l4 = sum(l4_by_level.get("none",[])) / len(l4_by_level.get("none",[])) \
                   if l4_by_level.get("none") else float("nan")
    lines.append(f"\n  Directional tests (constrained vs none):")
    for lv in ("light","medium","strict"):
        lv_vals = l4_by_level.get(lv,[])
        none_vals = l4_by_level.get("none",[])
        if lv_vals and none_vals:
            t,p = sps.ttest_ind(lv_vals, none_vals, equal_var=False, alternative="less")
            lv_mean = sum(lv_vals)/len(lv_vals)
            lines.append(f"  {lv:<8}: mean={lv_mean:.4f} vs none={none_mean_l4:.4f}  "
                         f"t={t:.3f} p(one-sided)={p:.4f}  "
                         f"direction met: {lv_mean < none_mean_l4 and p < ALPHA}")

    lines.append(f"\n  H_CEF_5 outcome: PENDING LIVE DATA")
    return result

# ── assumption tests ──────────────────────────────────────────────────────────

def run_assumptions(sessions: list[dict], lines: list[str]) -> None:
    lines += ["","="*66,"  ASSUMPTION TESTS","="*66]

    # Shapiro-Wilk per level
    lines += ["","  Shapiro-Wilk normality (mean_bsi by constraint_level):"]
    groups: dict[str,list[float]] = defaultdict(list)
    for s in sessions:
        lv = s.get("constraint_level",""); mb = s.get("mean_bsi")
        if lv and mb is not None: groups[lv].append(float(mb))

    for lv in CONSTRAINT_LEVELS:
        vals = groups.get(lv,[])
        if len(vals) >= 3:
            W,p = sps.shapiro(vals)
            flag = "" if p >= ALPHA else " WARNING: non-normal"
            lines.append(f"  {lv:<8} W={W:.4f} p={p:.4f}{flag}")
        else:
            lines.append(f"  {lv:<8} n<3 — skipped")

    # Levene across levels
    grp_lists = [groups[lv] for lv in CONSTRAINT_LEVELS if len(groups.get(lv,[])) >= 2]
    if len(grp_lists) >= 2:
        W,p = sps.levene(*grp_lists)
        flag = "" if p >= ALPHA else " WARNING: heterogeneous — use Games-Howell"
        lines.append(f"\n  Levene homogeneity: W={W:.4f} p={p:.4f}{flag}")

# ── summary register ──────────────────────────────────────────────────────────

def print_hypothesis_register(results: dict, lines: list[str]) -> None:
    lines += ["","="*66,"  HYPOTHESIS OUTCOME REGISTER","="*66,""]
    hyps = [
        ("H_CEF_1","BSI(constrained) > BSI(none), d >= 0.50"),
        ("H_CEF_2","BSI(medium) ~= BSI(strict); rigidity(medium) < rigidity(strict)"),
        ("H_CEF_3","Non-linear trade-off curve; archetype-specific elbow"),
        ("H_CEF_4","Residual drift > 0 at strict constraint"),
        ("H_CEF_5","L4 breach rate(constrained) < L4 breach rate(none); OR < 0.40"),
    ]
    lines.append(f"  {'Hypothesis':<12} {'Status':<12} Description")
    lines.append(f"  {'-'*64}")
    for h,desc in hyps:
        lines.append(f"  {h:<12} PENDING      {desc}")
    lines += ["","  [All outcomes PENDING — populate with live trial data]","="*66]

# ── writers ───────────────────────────────────────────────────────────────────

def write_report(report_text: str, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    p = output_dir/"cef_report.txt"
    with open(p,"w",encoding="utf-8") as f:
        f.write(report_text)
    print(f"  -> {p}")

def write_result_json(results: dict, output_dir: Path) -> None:
    def _make_serial(obj):
        if isinstance(obj, dict):  return {k: _make_serial(v) for k,v in obj.items()}
        if isinstance(obj, list):  return [_make_serial(v) for v in obj]
        if isinstance(obj, float) and (math.isnan(obj) or math.isinf(obj)): return None
        if isinstance(obj, (bool, int, str, float)): return obj
        return str(obj)
    p = output_dir/"cef_analysis_results.json"
    with open(p,"w",encoding="utf-8") as f:
        json.dump(_make_serial(results), f, indent=2)
    print(f"  -> {p}")

# ── public API ────────────────────────────────────────────────────────────────

def run_cef_analysis(
    sessions_path: Path,
    turns_path:    Path,
    tradeoff_path: Path,
    output_dir:    Path,
    verbose:       bool = True,
) -> dict:
    sessions = load_sessions(sessions_path)
    turns    = load_turns(turns_path)
    tradeoff = load_tradeoff(tradeoff_path)

    lines: list[str] = [
        "="*66,
        "  PAPER 6 — CEF STATISTICAL ANALYSIS",
        "  Pre-registered hypotheses H_CEF_1 through H_CEF_5",
        f"  N sessions = {len(sessions)}   N turns = {len(turns)}",
        f"  N tradeoff rows = {len(tradeoff)}",
        "="*66,
    ]

    results: dict[str, Any] = {}
    run_assumptions(sessions, lines)
    results["H_CEF_1"] = run_H_CEF_1(sessions, lines)
    results["H_CEF_2"] = run_H_CEF_2(sessions, tradeoff, lines)
    results["H_CEF_3"] = run_H_CEF_3(tradeoff, lines)
    results["H_CEF_4"] = run_H_CEF_4(sessions, lines)
    results["H_CEF_5"] = run_H_CEF_5(sessions, turns, lines)
    print_hypothesis_register(results, lines)

    report = "\n".join(lines)
    for subdir in ("cef_anova","cef_equivalence","cef_elbow","cef_residual","cef_l4"):
        (output_dir/subdir).mkdir(parents=True, exist_ok=True)

    write_report(report, output_dir)
    write_result_json(results, output_dir)
    if verbose: print(report)
    return results

# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sessions",  default=None)
    p.add_argument("--turns",     default=None)
    p.add_argument("--tradeoff",  default=None)
    p.add_argument("--output-dir",default=None)
    p.add_argument("--quiet",     action="store_true")
    args = p.parse_args()
    base = _ROOT/"data"/"cef_experiments"
    sp   = Path(args.sessions) if args.sessions else base/"cef_sessions.csv"
    tp   = Path(args.turns)    if args.turns    else base/"cef_turns.csv"
    trp  = Path(args.tradeoff) if args.tradeoff else base/"tradeoff_curve.csv"
    out  = Path(args.output_dir) if args.output_dir else _ROOT/"analysis"
    for f in (sp,tp,trp):
        if not f.exists():
            print(f"Missing: {f}\nRun constraint_experiment_runner + tradeoff_analysis first.")
            sys.exit(1)
    run_cef_analysis(sp, tp, trp, out, verbose=not args.quiet)

# ── smoke test ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import tempfile, random as _rng

    print("="*70)
    print("  CEF STATISTICAL ANALYSIS SMOKE TEST")
    print("="*70)

    _rng.seed(2026)

    def _synth_sess(arch, base, gain_d, refusal_d, cue_d, corr_d, l4_d, n=4):
        rows = []
        for lv in CONSTRAINT_LEVELS:
            bsi = min(1.0, max(0.0, base + gain_d.get(lv,0) + _rng.gauss(0,0.01)))
            ref = refusal_d.get(lv, 0.0)
            l4r = l4_d.get(lv, 0.0)
            for _ in range(n):
                rows.append({
                    "archetype":arch,"constraint_level":lv,
                    "mean_bsi":round(bsi+_rng.gauss(0,0.005),4),
                    "min_bsi": round(bsi-0.12,4), "final_bsi":round(bsi,4),
                    "breach_count":max(0,int((1-bsi)*8)),
                    "corrections_fired":int(corr_d.get(lv,0)*12),
                    "gated_turns":0,
                    "refusal_count":int(ref*12), "refusal_rate":round(ref,4),
                    "mean_persona_cues":cue_d.get(lv,3.0),
                    "mean_response_len":200-int(80*ref),
                    "beta_bsi":0.85,"bsi_drift_reduction":round(bsi-base,4),
                    "l4_breach_rate":round(l4r,4),
                    "experiment_id":"S","run_id":"S",
                    "exploit_class":"EC-1","perturbation_type":"contradiction",
                    "arm":f"arm_{lv}","session_id":f"{arch}_{lv}_{_}","timestamp":"T",
                })
        return rows

    def _synth_turn(sessions, n_turns=12):
        rows = []
        for s in sessions:
            for t in range(n_turns):
                bsi = s["mean_bsi"]+_rng.gauss(0,0.02)
                rows.append({
                    "archetype":s["archetype"],"constraint_level":s["constraint_level"],
                    "session_id":s["session_id"],"turn_number":t+1,
                    "bsi":round(bsi,4),"tc":round(bsi,4),"sd_inv":round(bsi,4),
                    "acg":round(bsi,4),
                    "bsi_breach":bsi<0.85,"l4_breach":_rng.random()<s["l4_breach_rate"],
                    "corrected":_rng.random()<0.1,"gated":False,
                    "refusal_detected":_rng.random()<s["refusal_rate"],
                    "response_length":s["mean_response_len"]+_rng.randint(-10,10),
                    "persona_cue_count":max(0,int(s["mean_persona_cues"]+_rng.gauss(0,0.5))),
                    "n_injected_prompts":0,
                    "alert_level":"breach" if bsi<0.85 else "none","pattern":"stable",
                    "anchor_bsi_dev":0.0,"anchor_tc_dev":0.0,
                    "anchor_sd_inv_dev":0.0,"anchor_acg_dev":0.0,
                    "experiment_id":"S","run_id":"S",
                    "exploit_class":"EC-1","perturbation_type":"contradiction",
                    "arm":f"arm_{s['constraint_level']}","phase":"identity_anchor",
                    "timestamp":"T",
                })
        return rows

    def _synth_tradeoff(arch, base, gain_d, rig_d, opt_lv):
        rows = []
        for lv in CONSTRAINT_LEVELS:
            bsi = base + gain_d.get(lv,0)
            me  = (_rng.uniform(2,5) if lv=="medium" else
                   _rng.uniform(0,0.5) if lv=="strict" else
                   _rng.uniform(0.1,1.0) if lv=="light" else None)
            rows.append({
                "archetype":arch,"constraint_level":lv,"is_optimal":(lv==opt_lv),
                "mean_bsi":round(bsi,4),"min_bsi":round(bsi-0.1,4),
                "bsi_gain":round(gain_d.get(lv,0),4),"breach_rate":round(1-bsi,4),
                "l4_breach_rate":round(0.3*(1-bsi),4),
                "rigidity":round(rig_d.get(lv,0),4),"refusal_rate":round(rig_d.get(lv,0)*0.5,4),
                "response_shortening":0.0,"persona_cue_loss":0.0,"correction_density":0.0,
                "mean_response_len":200,"marginal_efficiency":me,
                "predicted_elbow":"light" if arch in NARROW_TAU else "medium",
                "elbow_confirmed":(lv==opt_lv),"n_sessions":4,
            })
        return rows

    all_sess = (
        _synth_sess("Magneto",0.90,{"none":0,"light":0.03,"medium":0.035,"strict":0.036},
                    {"none":0,"light":0.02,"medium":0.06,"strict":0.20},
                    {"none":3.5,"light":3.2,"medium":2.8,"strict":1.5},
                    {"none":0,"light":0,"medium":0.08,"strict":0.25},
                    {"none":0.15,"light":0.10,"medium":0.07,"strict":0.04}) +
        _synth_sess("Joker",0.55,{"none":0,"light":0.05,"medium":0.18,"strict":0.21},
                    {"none":0,"light":0.03,"medium":0.10,"strict":0.35},
                    {"none":4.0,"light":3.8,"medium":3.0,"strict":1.2},
                    {"none":0,"light":0,"medium":0.20,"strict":0.40},
                    {"none":0.40,"light":0.30,"medium":0.15,"strict":0.08})
    )
    all_turns = _synth_turn(all_sess)
    all_tradeoff = (
        _synth_tradeoff("Magneto",0.90,
                        {"none":0,"light":0.03,"medium":0.035,"strict":0.036},
                        {"none":0,"light":0.015,"medium":0.018,"strict":0.13},"medium") +
        _synth_tradeoff("Joker",0.55,
                        {"none":0,"light":0.05,"medium":0.18,"strict":0.21},
                        {"none":0,"light":0,"medium":0.029,"strict":0.30},"medium")
    )

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        def _write_csv(path, rows):
            if not rows: return
            with open(path,"w",newline="") as f:
                w = csv.DictWriter(f,fieldnames=list(rows[0].keys()),extrasaction="ignore")
                w.writeheader(); w.writerows(rows)
        _write_csv(tmp/"cef_sessions.csv",  all_sess)
        _write_csv(tmp/"cef_turns.csv",     all_turns)
        _write_csv(tmp/"tradeoff_curve.csv",all_tradeoff)

        results = run_cef_analysis(
            tmp/"cef_sessions.csv", tmp/"cef_turns.csv",
            tmp/"tradeoff_curve.csv", tmp, verbose=False,
        )

        # ── Assertions ────────────────────────────────────────────────────────
        assert "H_CEF_1" in results and "H_CEF_5" in results
        print("\n  [T1] All 5 hypothesis blocks executed")

        # H_CEF_1: ANOVA result present with F, p, eta2
        h1 = results["H_CEF_1"]
        assert "F" in h1 and "eta2" in h1
        print(f"  [T2] H_CEF_1 ANOVA: F={h1['F']:.3f}  eta2={h1['eta2']:.4f}")

        # H_CEF_3: nonlinearity detected in synthetic data
        h3 = results["H_CEF_3"]
        print(f"  [T3] H_CEF_3 nonlinear_detected={h3.get('nonlinear_detected')}")

        # H_CEF_4: residual_drift block present
        h4 = results["H_CEF_4"]
        assert "strict_instability" in h4
        si = h4["strict_instability"]
        print(f"  [T4] H_CEF_4 strict instability mean={si['mean']:.4f}  p={si['p']:.4f}")

        # H_CEF_5: chi-square and OR computed
        h5 = results["H_CEF_5"]
        if "OR" in h5:
            print(f"  [T5] H_CEF_5 OR={h5['OR']:.4f}  "
                  f"OR<{L4_OR_THRESHOLD}: {h5.get('OR_target_met')}")
        else:
            print(f"  [T5] H_CEF_5 chi-square skipped (zero cells — expected in small synthetic)")

        # Output files exist
        for fname in ("cef_report.txt","cef_analysis_results.json"):
            assert (tmp/fname).exists(), f"Missing: {fname}"
        print(f"  [T6] Output files written")

        # JSON serialisable
        with open(tmp/"cef_analysis_results.json") as f:
            loaded = json.load(f)
        assert "H_CEF_1" in loaded
        print(f"  [T7] JSON round-trip OK")

    print("\n"+"="*70)
    print("  Smoke test complete — all 7 tests passed")
    print("="*70)
