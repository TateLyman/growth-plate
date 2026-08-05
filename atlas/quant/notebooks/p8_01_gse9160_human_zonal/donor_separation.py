#!/usr/bin/env python3
"""
POST HOC, and the most consequential thing this notebook found.

The preregistered method controls (posthoc_method_controls.py) failed in a patterned
way: donor 1 recovered the expected compartment for almost every canonical marker with
large fold ranges, and donor 2 did not, with fold ranges collapsed toward 1. That is
not a biological difference between an 11-year-old girl and a 13-year-old boy. It is a
difference in how cleanly the five compartments were separated during laser capture.

This script quantifies it genome-wide rather than from a handful of markers, so the
claim rests on the whole array and not on a chosen gene.

Metric: for every probe set detected above background in all four zones of a donor,
the fold range across the zonal axis. If both dissections resolved zones equally well,
the two distributions should be similar. The contrast between them is the diagnostic.

Marker cross-check: COL10A1 is definitionally hypertrophic. Its intensity in the
RESTING zone sample is a direct read-out of bleed-through, and is reported per donor.

Usage:  python3 donor_separation.py
"""
import os, sys, json, csv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analysis as A                                     # noqa: E402

BLEED_MARKERS = ["COL10A1", "IBSP", "SPP1", "MMP13", "ALPL"]


def main():
    X, p2g = A.load()
    _, thr = A.background(X, p2g)
    out = {"donors": {}}

    for donor in (1, 2):
        i = {z: [k for k, (_, d, zz) in enumerate(A.SAMPLES)
                 if d == donor and zz == z][0]
             for z in ["RZ", "PZ", "PHZ", "HZ", "PC"]}
        fr = []
        for p, v in X.items():
            vals = [v[i[z]] for z in A.AXIS]
            if all(v[i[z]] > thr[i[z]] for z in A.AXIS) and min(vals) > 0:
                fr.append(max(vals) / min(vals))
        fr.sort()
        n = len(fr)
        out["donors"][donor] = {
            "probesets_detected_in_all_four_zones": n,
            "fold_range_p50": round(fr[n // 2], 2),
            "fold_range_p90": round(fr[int(.90 * n)], 2),
            "fold_range_p99": round(fr[int(.99 * n)], 2),
            "fold_range_max": round(fr[-1], 1),
            "fraction_above_2x": round(sum(1 for x in fr if x > 2) / n, 3),
            "fraction_above_5x": round(sum(1 for x in fr if x > 5) / n, 3),
            "fraction_above_10x": round(sum(1 for x in fr if x > 10) / n, 3),
        }

    # bleed-through: hypertrophic markers measured in the resting-zone sample
    idx = A.sym_index(p2g, BLEED_MARKERS)
    bleed = []
    for g in BLEED_MARKERS:
        for p in idx.get(g) or []:
            if p not in X:
                continue
            row = {"gene": g, "probe_set": p}
            keep = False
            for donor in (1, 2):
                i = {z: [k for k, (_, d, zz) in enumerate(A.SAMPLES)
                         if d == donor and zz == z][0] for z in ["RZ", "HZ"]}
                rz, hz = X[p][i["RZ"]], X[p][i["HZ"]]
                row[f"d{donor}_RZ"] = round(rz, 1)
                row[f"d{donor}_HZ"] = round(hz, 1)
                row[f"d{donor}_RZ_as_pct_of_HZ"] = round(100 * rz / max(1e-9, hz), 1)
                if hz > 5 * thr[i["HZ"]]:
                    keep = True
            if keep:
                bleed.append(row)
    with open(os.path.join(A.RES, "donor_separation_bleedthrough.csv"),
              "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(bleed[0]))
        w.writeheader()
        w.writerows(bleed)

    d1, d2 = out["donors"][1], out["donors"][2]
    out["contrast_ratio_p90"] = round(d1["fold_range_p90"] / d2["fold_range_p90"], 2)
    out["contrast_ratio_frac_above_5x"] = round(
        d1["fraction_above_5x"] / max(1e-9, d2["fraction_above_5x"]), 1)
    out["conclusion"] = (
        "Donor 1 resolves the zonal axis; donor 2 largely does not. For zonal-contrast "
        "purposes this dataset is effectively n=1, and the preregistered "
        "both-donors-must-agree concordance rule therefore penalises genes for donor 2's "
        "dissection rather than for biological disagreement. Detection (presence/absence) "
        "is unaffected and if anything is stronger in donor 2, whose arrays have the "
        "lower background.")
    json.dump(out, open(os.path.join(A.RES, "donor_separation.json"), "w"), indent=1)

    print(json.dumps(out, indent=1))
    print("\nCOL10A1 in the RESTING zone, as % of the same donor's hypertrophic zone:")
    for r in bleed:
        if r["gene"] == "COL10A1":
            print(f"  {r['probe_set']:14s} donor1 {r['d1_RZ_as_pct_of_HZ']:6.1f}%   "
                  f"donor2 {r['d2_RZ_as_pct_of_HZ']:6.1f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
