#!/usr/bin/env python3
"""
POST HOC. Declared as such.

PREREGISTRATION.md section 4 locked a gene list and section 3.1 preregistered a
positive control for the *background rule*. It did not preregister a positive control
for the *zonal profile method* - a set of genes whose human growth-plate localisation
is not in dispute, which the analysis must recover if its zonal ratios mean anything.
That was an oversight in the plan, not a discovery made afterwards, and it is recorded
here rather than quietly folded into the preregistered run.

These genes test the method. They are not used to answer any gap, and nothing from
this file enters the graph as a finding.

  COL10A1  hypertrophic chondrocytes, definitionally
  COL2A1   cartilage-wide, the most abundant transcript in the tissue
  COL1A1   perichondrium/bone, should be depleted inside the cartilage zones
  IBSP     bone sialoprotein - mineralisation front / bone
  SPP1     osteopontin - hypertrophic/mineralising
  MKI67    proliferation
  MMP13    hypertrophic
  SP7      osterix - osteoblast lineage, perichondrium

Expected before running (stated here so the check is falsifiable):
COL10A1, MMP13, SPP1, IBSP peak in HZ; COL1A1 and SP7 peak in perichondrium;
COL2A1 detected in every cartilage compartment; MKI67 not necessarily PZ-peaked
because LCM captures the whole zone including non-cycling cells.

Usage:  python3 posthoc_method_controls.py
"""
import os, sys, json, csv, statistics

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analysis as A                                     # noqa: E402

CONTROLS = ["COL10A1", "COL2A1", "COL1A1", "IBSP", "SPP1", "MKI67", "MMP13", "SP7"]
EXPECT = {"COL10A1": "HZ", "MMP13": "HZ", "SPP1": "HZ", "IBSP": "HZ",
          "COL1A1": "PC", "SP7": "PC", "COL2A1": "any_cartilage", "MKI67": "none"}


def main():
    X, p2g = A.load()
    _, thr = A.background(X, p2g)
    idx = A.sym_index(p2g, CONTROLS)
    rows = []
    for g in CONTROLS:
        for p in idx.get(g) or []:
            if p not in X:
                continue
            rec = {"gene": g, "probe_set": p, "expected_peak": EXPECT[g]}
            for donor in (1, 2):
                vals, rel = A.profile(X, p, donor)
                for z in ["RZ", "PZ", "PHZ", "HZ", "PC"]:
                    i = [k for k, (_, d, zz) in enumerate(A.SAMPLES)
                         if d == donor and zz == z][0]
                    rec[f"d{donor}_{z}"] = round(vals[z], 1)
                    rec[f"d{donor}_{z}_det"] = int(vals[z] > thr[i])
                axis = {z: rel[z] for z in A.AXIS}
                rec[f"d{donor}_max_zone"] = max(axis, key=axis.get)
                rec[f"d{donor}_max_all"] = max(rel, key=rel.get)
                rec[f"d{donor}_fold_range"] = round(
                    max(axis.values()) / max(1e-9, min(axis.values())), 2)
            rows.append(rec)

    out = os.path.join(A.RES, "posthoc_method_controls.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    # verdict: for each gene, does its best-detected probe set peak where expected?
    print(f"{'gene':9s} {'expect':14s} {'d1 peak':8s} {'d2 peak':8s} {'fold d1/d2':14s} verdict")
    verdicts = {}
    for g in CONTROLS:
        rs = [r for r in rows if r["gene"] == g]
        if not rs:
            print(f"{g:9s} not on platform")
            continue
        best = max(rs, key=lambda r: max(r[f"d{d}_{z}"] for d in (1, 2)
                                         for z in ["RZ", "PZ", "PHZ", "HZ", "PC"]))
        e = EXPECT[g]
        p1, p2 = best["d1_max_all"], best["d2_max_all"]
        if e == "any_cartilage":
            ok = all(best[f"d{d}_{z}_det"] for d in (1, 2)
                     for z in ["RZ", "PZ", "PHZ", "HZ"])
        elif e == "none":
            ok = None
        else:
            ok = (p1 == e and p2 == e)
        verdicts[g] = ok
        print(f"{g:9s} {e:14s} {p1:8s} {p2:8s} "
              f"{best['d1_fold_range']:>6}/{best['d2_fold_range']:<7} "
              f"{'PASS' if ok else ('n/a' if ok is None else 'MISS')}")
    scored = {k: v for k, v in verdicts.items() if v is not None}
    print(f"\nmethod controls passing: {sum(scored.values())}/{len(scored)}")
    json.dump({"verdicts": {k: v for k, v in verdicts.items()},
               "passing": sum(scored.values()), "scored": len(scored)},
              open(os.path.join(A.RES, "posthoc_method_controls.json"), "w"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
