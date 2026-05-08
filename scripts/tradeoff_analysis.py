#!/usr/bin/env python3
"""
tradeoff_analysis.py
====================
Paper 6 — Stability x Creativity Trade-Off Analysis.
Consumes cef_turns.csv + cef_sessions.csv.
Produces tradeoff_curve.csv, elbow_points.json, tradeoff_report.txt.

THEORETICAL BASIS  (P6_S2 SS2.3)
  Pre-registered: non-linear curve with identifiable elbow per archetype.
  Narrow-tau (Magneto, Batman, Lex Luthor) -> elbow at light or medium.
  Wide-tau   (Joker, Two-Face, Harley Quinn) -> elbow at medium or strict.

RIGIDITY INDEX (pre-registered weights):
  0.40 * refusal_rate
  0.30 * response_shortening (relative to none arm)
  0.20 * persona_cue_loss   (relative to none arm)
  0.10 * correction_density

ELBOW DETECTION:
  Marginal efficiency = delta_bsi_gain / delta_rigidity per level transition.
  Elbow = transition where efficiency drops below 50% of prior value.
"""
from __future__ import annotations
import argparse, csv, json, math, os, sys
from collections import defaultdict
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent if _HERE.name == "scripts" else _HERE

CONSTRAINT_LEVELS = ("none", "light", "medium", "strict")

RIGIDITY_WEIGHTS = {
    "refusal_rate":        0.40,
    "response_shortening": 0.30,
    "persona_cue_loss":    0.20,
    "correction_density":  0.10,
}

ELBOW_EFFICIENCY_DROP = 0.50
MIN_MEANINGFUL_GAIN   = 0.01
NARROW_TAU = {"Magneto", "Batman", "Lex Luthor"}
WIDE_TAU   = {"Joker", "Two-Face", "Harley Quinn"}
CURVE_CSV_COLS = [
    "archetype","constraint_level","is_optimal",
    "mean_bsi","min_bsi","bsi_gain","breach_rate","l4_breach_rate",
    "rigidity","refusal_rate","response_shortening",
    "persona_cue_loss","correction_density","mean_response_len",
    "marginal_efficiency","predicted_elbow","elbow_confirmed","n_sessions",
]

# ── loaders ───────────────────────────────────────────────────────────────────

def _cast(row, numeric, bool_cols):
    for k in numeric:
        if k in row and row[k] not in ("", "None", "null"):
            try: row[k] = float(row[k])
            except ValueError: row[k] = None
    for k in bool_cols:
        if k in row: row[k] = str(row[k]).lower() in ("true","1","yes")
    return row

def load_turns(path):
    num = {"bsi","tc","sd_inv","acg","response_length","persona_cue_count",
           "n_injected_prompts","anchor_bsi_dev","anchor_tc_dev",
           "anchor_sd_inv_dev","anchor_acg_dev"}
    bools = {"bsi_breach","l4_breach","corrected","gated","refusal_detected"}
    with open(path, newline="", encoding="utf-8") as f:
        return [_cast(r, num, bools) for r in csv.DictReader(f)]

def load_sessions(path):
    num = {"mean_bsi","min_bsi","final_bsi","breach_count","corrections_fired",
           "gated_turns","refusal_count","refusal_rate","mean_persona_cues",
           "mean_response_len","beta_bsi","bsi_drift_reduction","l4_breach_rate"}
    with open(path, newline="", encoding="utf-8") as f:
        return [_cast(r, num, set()) for r in csv.DictReader(f)]

# ── rigidity ──────────────────────────────────────────────────────────────────

def compute_rigidity(turns, sessions, none_ref):
    tg = defaultdict(list)
    sg = defaultdict(list)
    for t in turns:  tg[(t.get("archetype",""), t.get("constraint_level",""))].append(t)
    for s in sessions: sg[(s.get("archetype",""), s.get("constraint_level",""))].append(s)
    out = {}
    archetypes = sorted({k[0] for k in tg})
    for arch in archetypes:
        ref_len = none_ref.get(arch,{}).get("mean_response_len", 1.0) or 1.0
        ref_cue = none_ref.get(arch,{}).get("mean_persona_cues", 1.0) or 1.0
        for level in CONSTRAINT_LEVELS:
            key = (arch, level)
            ts  = tg.get(key, [])
            ss  = sg.get(key, [])
            n_t = len(ts) or 1
            n_s = len(ss) or 1
            refusal_rate  = sum(1 for t in ts if t.get("refusal_detected")) / n_t
            mean_len      = sum(t.get("response_length") or 0 for t in ts) / n_t
            mean_cue      = sum(t.get("persona_cue_count") or 0 for t in ts) / n_t
            shortening    = max(0.0, 1.0 - mean_len / ref_len)
            cue_loss      = max(0.0, 1.0 - mean_cue / ref_cue)
            corr_total    = sum(s.get("corrections_fired") or 0 for s in ss)
            corr_density  = min(1.0, corr_total / (n_s * 12))
            rigidity = (
                RIGIDITY_WEIGHTS["refusal_rate"]        * refusal_rate
              + RIGIDITY_WEIGHTS["response_shortening"] * shortening
              + RIGIDITY_WEIGHTS["persona_cue_loss"]    * cue_loss
              + RIGIDITY_WEIGHTS["correction_density"]  * corr_density
            )
            out[key] = {
                "refusal_rate":        round(refusal_rate, 4),
                "response_shortening": round(shortening,   4),
                "persona_cue_loss":    round(cue_loss,     4),
                "correction_density":  round(corr_density, 4),
                "rigidity":            round(max(0.0, min(1.0, rigidity)), 4),
                "mean_response_len":   round(mean_len, 1),
                "mean_persona_cues":   round(mean_cue, 4),
            }
    return out

# ── stability ─────────────────────────────────────────────────────────────────

def compute_stability(sessions):
    sg = defaultdict(list)
    for s in sessions: sg[(s.get("archetype",""), s.get("constraint_level",""))].append(s)
    archetypes = sorted({k[0] for k in sg})
    none_means = {}
    for arch in archetypes:
        nr = sg.get((arch,"none"),[])
        if nr: none_means[arch] = sum(s.get("mean_bsi") or 0 for s in nr)/len(nr)
    out = {}
    for arch in archetypes:
        ref = none_means.get(arch, float("nan"))
        for level in CONSTRAINT_LEVELS:
            rows = sg.get((arch, level),[])
            if not rows: continue
            n = len(rows)
            mb = sum(s.get("mean_bsi") or 0 for s in rows)/n
            out[(arch,level)] = {
                "mean_bsi":    round(mb, 4),
                "min_bsi":     round(min(s.get("min_bsi") or 0 for s in rows), 4),
                "bsi_gain":    round(mb - ref, 4) if not math.isnan(ref) else 0.0,
                "breach_rate": round(sum(s.get("breach_count") or 0 for s in rows)/n, 4),
                "l4_rate":     round(sum(s.get("l4_breach_rate") or 0 for s in rows)/n, 4),
                "n_sessions":  n,
            }
    return out

# ── marginal efficiency + elbow ───────────────────────────────────────────────

def marginal_efficiency(stability, rigidity, arch):
    transitions = []
    for i in range(len(CONSTRAINT_LEVELS)-1):
        fl, tl = CONSTRAINT_LEVELS[i], CONSTRAINT_LEVELS[i+1]
        sf = stability.get((arch,fl),{}); st = stability.get((arch,tl),{})
        rf = rigidity.get((arch,fl),{});  rt = rigidity.get((arch,tl),{})
        db = st.get("bsi_gain",0.0) - sf.get("bsi_gain",0.0)
        dr = rt.get("rigidity",0.0) - rf.get("rigidity",0.0)
        if abs(dr) > 1e-6:   eff = db / dr
        elif db > MIN_MEANINGFUL_GAIN: eff = float("inf")
        else:                eff = 0.0
        transitions.append({
            "from_level": fl, "to_level": tl,
            "delta_bsi": round(db,4), "delta_rigidity": round(dr,4),
            "marginal_efficiency": round(eff,4) if not math.isinf(eff) else "inf",
        })
    return transitions

def detect_elbow(transitions, arch):
    finite = [t for t in transitions
              if isinstance(t["marginal_efficiency"],(int,float))
              and not math.isinf(t["marginal_efficiency"])]
    if len(finite) < 2:
        return "light" if arch in NARROW_TAU else "medium"
    for i in range(1, len(finite)):
        pe, ce = finite[i-1]["marginal_efficiency"], finite[i]["marginal_efficiency"]
        if pe > 0 and ce < pe * ELBOW_EFFICIENCY_DROP:
            return finite[i]["from_level"]
    best = max(finite, key=lambda t: t["marginal_efficiency"])
    return best["to_level"]

# ── curve builder ─────────────────────────────────────────────────────────────

def build_curve(turns, sessions):
    archetypes = sorted({s.get("archetype","") for s in sessions}-{""})
    sg = defaultdict(list)
    for s in sessions: sg[(s.get("archetype",""), s.get("constraint_level",""))].append(s)
    none_ref = {}
    for arch in archetypes:
        nr = sg.get((arch,"none"),[])
        if nr:
            n = len(nr)
            none_ref[arch] = {
                "mean_response_len": sum(s.get("mean_response_len") or 0 for s in nr)/n,
                "mean_persona_cues": sum(s.get("mean_persona_cues") or 0 for s in nr)/n,
            }
    stability = compute_stability(sessions)
    rigidity  = compute_rigidity(turns, sessions, none_ref)
    curve_rows, elbow_points = [], {}
    for arch in archetypes:
        trans = marginal_efficiency(stability, rigidity, arch)
        opt   = detect_elbow(trans, arch)
        pred  = "light" if arch in NARROW_TAU else "medium"
        pred_idx = CONSTRAINT_LEVELS.index(pred)
        next_pred = CONSTRAINT_LEVELS[pred_idx+1] if pred_idx+1 < len(CONSTRAINT_LEVELS) else pred
        confirmed = opt in (pred, next_pred)
        note = ("narrow-tau: predicted elbow at light or medium"
                if arch in NARROW_TAU else
                "wide-tau: predicted elbow at medium or strict")
        elbow_points[arch] = {
            "optimal_level": opt, "predicted_elbow": pred,
            "elbow_confirmed": confirmed, "prediction_note": note,
            "transitions": trans,
        }
        for level in CONSTRAINT_LEVELS:
            sd = stability.get((arch,level),{})
            rd = rigidity.get((arch,level),{})
            if not sd: continue
            li = CONSTRAINT_LEVELS.index(level)
            me = trans[li-1]["marginal_efficiency"] if 0 < li <= len(trans) else None
            curve_rows.append({
                "archetype": arch, "constraint_level": level,
                "is_optimal": (level == opt),
                "mean_bsi": sd.get("mean_bsi"), "min_bsi": sd.get("min_bsi"),
                "bsi_gain": sd.get("bsi_gain"), "breach_rate": sd.get("breach_rate"),
                "l4_breach_rate": sd.get("l4_rate"),
                "rigidity": rd.get("rigidity"),
                "refusal_rate": rd.get("refusal_rate"),
                "response_shortening": rd.get("response_shortening"),
                "persona_cue_loss": rd.get("persona_cue_loss"),
                "correction_density": rd.get("correction_density"),
                "mean_response_len": rd.get("mean_response_len"),
                "marginal_efficiency": me,
                "predicted_elbow": pred, "elbow_confirmed": confirmed,
                "n_sessions": sd.get("n_sessions",0),
            })
    return curve_rows, elbow_points

# ── report ────────────────────────────────────────────────────────────────────

def format_report(curve_rows, elbow_points):
    L = ["="*70,
         "  PAPER 6 — STABILITY x CREATIVITY TRADE-OFF ANALYSIS",
         "  Pre-registered: non-linear curve with archetype-specific elbow",
         "  P6_S2_TheoreticalFrame_CEF.md SS2.3",
         "="*70, "",
         "RIGIDITY INDEX WEIGHTS (pre-registered):"]
    for c,w in RIGIDITY_WEIGHTS.items():
        L.append(f"  {c:<26} w = {w:.2f}")
    L.append("")
    archetypes = sorted({r["archetype"] for r in curve_rows})
    for arch in archetypes:
        rows = [r for r in curve_rows if r["archetype"]==arch]
        ep   = elbow_points.get(arch,{})
        conf = "confirmed" if ep.get("elbow_confirmed") else "not confirmed"
        L += ["-"*70,
              f"  ARCHETYPE: {arch}",
              f"  Optimal level: {ep.get('optimal_level','?')}  "
              f"Predicted: {ep.get('predicted_elbow','?')}  ({conf})",
              f"  {ep.get('prediction_note','')}","",
              f"  {'Level':<8} {'BSI':>7} {'Gain':>7} {'Rigidity':>9} "
              f"{'Refusals':>9} {'CueLoss':>8} {'Efficiency':>11}  Optimal",
              f"  {'-'*67}"]
        for r in sorted(rows, key=lambda x: CONSTRAINT_LEVELS.index(x["constraint_level"])):
            bsi = f"{r['mean_bsi']:.4f}"    if r.get("mean_bsi")     is not None else "   —"
            gain= f"{r['bsi_gain']:+.4f}"   if r.get("bsi_gain")     is not None else "   —"
            rig = f"{r['rigidity']:.4f}"    if r.get("rigidity")     is not None else "   —"
            ref = f"{r['refusal_rate']:.4f}"if r.get("refusal_rate") is not None else "   —"
            cue = f"{r['persona_cue_loss']:.4f}" if r.get("persona_cue_loss") is not None else "  —"
            me  = r.get("marginal_efficiency")
            mes = f"{me:>11.4f}" if isinstance(me,float) else f"{'inf':>11}" if me=="inf" else f"{'—':>11}"
            opt = "  <- OPTIMAL" if r.get("is_optimal") else ""
            L.append(f"  {r['constraint_level']:<8} {bsi:>7} {gain:>7} {rig:>9} {ref:>9} {cue:>8} {mes}{opt}")
        trans = ep.get("transitions",[])
        if trans:
            L += ["",f"  MARGINAL EFFICIENCY:",
                  f"  {'Transition':<20} {'dBSI':>7} {'dRig':>10} {'Efficiency':>12}",
                  f"  {'-'*52}"]
            for t in trans:
                mes = f"{t['marginal_efficiency']:>12.4f}" if isinstance(t["marginal_efficiency"],float) else f"{'inf':>12}"
                L.append(f"  {t['from_level']}->{t['to_level']:<14} "
                         f"{t['delta_bsi']:>7.4f} {t['delta_rigidity']:>10.4f} {mes}")
        L.append("")
    L += ["="*70,"  ELBOW SUMMARY","="*70,"",
          f"  {'Archetype':<16} {'Optimal':<8} {'Predicted':<10} Confirmed",
          f"  {'-'*48}"]
    for arch in archetypes:
        ep = elbow_points.get(arch,{})
        L.append(f"  {arch:<16} {ep.get('optimal_level','—'):<8} "
                 f"{ep.get('predicted_elbow','—'):<10} "
                 f"{'YES' if ep.get('elbow_confirmed') else 'NO'}")
    nc = sum(1 for a in NARROW_TAU if elbow_points.get(a,{}).get("elbow_confirmed"))
    wc = sum(1 for a in WIDE_TAU   if elbow_points.get(a,{}).get("elbow_confirmed"))
    nn = sum(1 for a in NARROW_TAU if a in elbow_points)
    nw = sum(1 for a in WIDE_TAU   if a in elbow_points)
    L += ["",f"  H_CEF_3: narrow-tau confirmed {nc}/{nn}  wide-tau confirmed {wc}/{nw}",
          "  [PENDING LIVE DATA]","="*70]
    return "\n".join(L)

# ── writers ───────────────────────────────────────────────────────────────────

def write_outputs(curve_rows, elbow_points, report_text, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    curve_path = output_dir/"tradeoff_curve.csv"
    with open(curve_path,"w",newline="",encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CURVE_CSV_COLS, extrasaction="ignore")
        w.writeheader(); w.writerows(curve_rows)
    print(f"  -> {curve_path}  ({len(curve_rows)} rows)")
    elbow_path = output_dir/"elbow_points.json"
    with open(elbow_path,"w",encoding="utf-8") as f:
        json.dump(elbow_points, f, indent=2)
    print(f"  -> {elbow_path}")
    rpt_path = output_dir/"tradeoff_report.txt"
    with open(rpt_path,"w",encoding="utf-8") as f:
        f.write(report_text)
    print(f"  -> {rpt_path}")

# ── public API ────────────────────────────────────────────────────────────────

def run_tradeoff_analysis(turns_path, sessions_path, output_dir, verbose=True):
    turns    = load_turns(turns_path)
    sessions = load_sessions(sessions_path)
    curve_rows, elbow_points = build_curve(turns, sessions)
    report   = format_report(curve_rows, elbow_points)
    write_outputs(curve_rows, elbow_points, report, output_dir)
    if verbose: print(report)
    return curve_rows, elbow_points, report

# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--turns",      default=None)
    p.add_argument("--sessions",   default=None)
    p.add_argument("--output-dir", default=None)
    p.add_argument("--quiet",      action="store_true")
    args = p.parse_args()
    default_dir   = _ROOT/"data"/"cef_experiments"
    output_dir    = Path(args.output_dir) if args.output_dir else default_dir
    turns_path    = Path(args.turns)    if args.turns    else output_dir/"cef_turns.csv"
    sessions_path = Path(args.sessions) if args.sessions else output_dir/"cef_sessions.csv"
    if not turns_path.exists() or not sessions_path.exists():
        print(f"Input files not found. Run constraint_experiment_runner.py first.")
        sys.exit(1)
    run_tradeoff_analysis(turns_path, sessions_path, output_dir, verbose=not args.quiet)

# ── smoke test ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import tempfile, random
    print("="*70)
    print("  TRADEOFF ANALYSIS SMOKE TEST")
    print("="*70)
    random.seed(2026)

    def _synth(arch, base, gain, refusal, cue, corr, n_sess=3, n_turns=12):
        turns, sessions = [], []
        for level in CONSTRAINT_LEVELS:
            bsi   = min(1.0, max(0.0, base + gain.get(level,0) + random.gauss(0,0.01)))
            ref   = refusal.get(level,0.0)
            cu    = cue.get(level,1.0)
            cr    = corr.get(level,0.0)
            rlen  = max(50, 200 - int(80*ref))
            for si in range(n_sess):
                sid = f"{arch[:3]}_{level}_{si}"
                sessions.append({
                    "archetype": arch, "constraint_level": level, "session_id": sid,
                    "mean_bsi": round(bsi+random.gauss(0,0.005),4),
                    "min_bsi":  round(bsi-0.12+random.gauss(0,0.01),4),
                    "final_bsi":round(bsi+random.gauss(0,0.005),4),
                    "breach_count": max(0,int((1-bsi)*8)),
                    "corrections_fired": int(cr*n_turns),
                    "gated_turns":0, "refusal_count":int(ref*n_turns),
                    "refusal_rate":round(ref,4),
                    "mean_persona_cues":round(cu,4),
                    "mean_response_len":rlen+random.randint(-5,5),
                    "beta_bsi":0.85,
                    "bsi_drift_reduction":round(bsi-base,4),
                    "l4_breach_rate":round(0.3*(1-bsi),4),
                    "experiment_id":"S","run_id":"S",
                    "exploit_class":"EC-1","perturbation_type":"contradiction",
                    "arm":f"arm_{level}",
                })
                for t in range(n_turns):
                    turns.append({
                        "archetype":arch, "constraint_level":level, "session_id":sid,
                        "turn_number":t+1,
                        "bsi":round(bsi+random.gauss(0,0.02),4),
                        "tc":round(bsi+random.gauss(0,0.03),4),
                        "sd_inv":round(bsi+random.gauss(0,0.02),4),
                        "acg":round(bsi+random.gauss(0,0.05),4),
                        "bsi_breach":bsi<0.85, "l4_breach":random.random()<0.1*(1-bsi),
                        "corrected":random.random()<cr, "gated":False,
                        "refusal_detected":random.random()<ref,
                        "response_length":rlen+random.randint(-15,15),
                        "persona_cue_count":max(0,int(cu*3+random.gauss(0,0.5))),
                        "n_injected_prompts":int(cr>0),
                        "alert_level":"breach" if bsi<0.85 else "none",
                        "pattern":"stable",
                        "anchor_bsi_dev":round(bsi-base,4),
                        "anchor_tc_dev":0.0,"anchor_sd_inv_dev":0.0,"anchor_acg_dev":0.0,
                        "experiment_id":"S","run_id":"S",
                        "exploit_class":"EC-1","perturbation_type":"contradiction",
                        "arm":f"arm_{level}","phase":"identity_anchor",
                        "timestamp":"2026-04-28T00:00:00+00:00",
                    })
        return turns, sessions

    mt, ms = _synth("Magneto", 0.90,
        {"none":0.0,"light":0.03,"medium":0.035,"strict":0.036},
        {"none":0.0,"light":0.02,"medium":0.06, "strict":0.20},
        {"none":3.5,"light":3.2, "medium":2.8,  "strict":1.5},
        {"none":0.0,"light":0.0, "medium":0.08, "strict":0.25})
    jt, js = _synth("Joker", 0.55,
        {"none":0.0,"light":0.05,"medium":0.18,"strict":0.21},
        {"none":0.0,"light":0.03,"medium":0.10,"strict":0.35},
        {"none":4.0,"light":3.8, "medium":3.0, "strict":1.2},
        {"none":0.0,"light":0.0, "medium":0.20,"strict":0.40})

    all_t, all_s = mt+jt, ms+js

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        tp = tmp/"cef_turns.csv"
        sp = tmp/"cef_sessions.csv"
        tc = list(all_t[0].keys())
        sc = list(all_s[0].keys())
        with open(tp,"w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=tc,extrasaction="ignore"); w.writeheader(); w.writerows(all_t)
        with open(sp,"w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=sc,extrasaction="ignore"); w.writeheader(); w.writerows(all_s)
        print(f"\n  Synthetic: {len(all_t)} turn rows, {len(all_s)} session rows")
        cr, ep, rpt = run_tradeoff_analysis(tp, sp, tmp, verbose=False)
        print("\n"+rpt)

        assert len(cr)==8, f"Expected 8 curve rows, got {len(cr)}"
        print(f"\n  [T1] curve_rows={len(cr)}")
        assert "Magneto" in ep and "Joker" in ep
        print(f"  [T2] elbows: Magneto->{ep['Magneto']['optimal_level']}  Joker->{ep['Joker']['optimal_level']}")
        mi = CONSTRAINT_LEVELS.index(ep["Magneto"]["optimal_level"])
        assert mi <= CONSTRAINT_LEVELS.index("medium"), f"Magneto elbow too late: {ep['Magneto']['optimal_level']}"
        print(f"  [T3] Magneto elbow <=medium")
        jm = next(r for r in cr if r["archetype"]=="Joker" and r["constraint_level"]=="medium")
        jn = next(r for r in cr if r["archetype"]=="Joker" and r["constraint_level"]=="none")
        assert jm["mean_bsi"] > jn["mean_bsi"]
        print(f"  [T4] Joker BSI: none={jn['mean_bsi']:.4f} -> medium={jm['mean_bsi']:.4f}")
        js2 = next(r for r in cr if r["archetype"]=="Joker" and r["constraint_level"]=="strict")
        assert (js2["rigidity"] or 0) >= (jm["rigidity"] or 0)
        print(f"  [T5] Rigidity: medium={jm['rigidity']:.4f} <= strict={js2['rigidity']:.4f}")
        for f in ("tradeoff_curve.csv","elbow_points.json","tradeoff_report.txt"):
            assert (tmp/f).exists()
        print(f"  [T6] All 3 output files written")
        for arch in ("Magneto","Joker"):
            opts = [r for r in cr if r["archetype"]==arch and r["is_optimal"]]
            assert len(opts)==1, f"{arch}: {len(opts)} optimal rows"
        print(f"  [T7] is_optimal=1 per archetype")

    print("\n"+"="*70)
    print("  Smoke test complete — all 7 tests passed")
    print("="*70)
