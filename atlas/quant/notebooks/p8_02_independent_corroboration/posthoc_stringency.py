#!/usr/bin/env python3
"""
POST HOC. Declared as such. Does not replace any preregistered verdict.

THE PROBLEM THIS EXPOSES
PREREGISTRATION 4.1 reused P8-01's detection rule - intensity above the 95th percentile
of the array's olfactory-receptor null - on three new platforms. On GPL570 that rule had
a preregistered positive control: it reproduced the original submitters' own MAS5
present-calls (10,063/12,193 and 17,639/18,454) without seeing them.

NO SUCH CONTROL EXISTS FOR GPL6884, GPL9828 OR GPL9324. The rule was validated on one
platform and transferred to three others on the assumption that olfactory receptors are
silent everywhere, which is true, and that the arrays behave comparably, which was never
checked. The consequence is visible in the fraction of each array clearing its own
threshold:

    GSE9160  (GPL570, P8-01)   18 - 32 %
    GSE22855 (GPL6884)         38 - 39 %
    GSE32398 (GPL9828)         55 - 56 %
    GSE18338 (GPL9324)         58 - 61 %

A DETECTED call on an array where 56 % of probes clear the bar is weak evidence of
presence. Since two of the four claims are REFUTED by exactly such calls, the strength of
that refutation has to be measured rather than asserted.

WHAT THIS DOES
Re-runs the same verdicts at three stringencies and reports how each gene moves:

    p95  the preregistered rule
    p99  99th percentile of the OR null
    med  above the array's own median probe intensity

and prints each target's raw intensity as a PERCENTILE of its own array, which is
platform-independent in a way an absolute threshold is not.

Nothing here enters the graph on its own. It decides how confidently the preregistered
verdicts may be stated.

Usage:  python3 posthoc_stringency.py
"""
import os, sys, re, json, csv, statistics

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analysis as A                                          # noqa: E402

LEVELS = ["p95", "p99", "med"]


def main():
    targets = sorted({g for c in A.CLAIMS.values()
                      for g in c["negative"] + c["controls"]} |
                     set(A.GATE) | set(A.SECONDARY))
    rows, pct_rows = [], []

    for gse, meta in A.SERIES.items():
        pmap = json.load(open(os.path.join(A.DATA, meta["platform"] + ".json")))["map"]
        gsms, labels, X = A.load_series(gse)
        gp = [i for i, l in enumerate(labels) if re.search(meta["gp_match"], l, re.I)]
        orp = [p for p, s in pmap.items()
               if A.OR_RE.fullmatch(str(s or "")) and p in X]
        idx = A.sym_index(pmap, targets)

        thr = {lv: {} for lv in LEVELS}
        arr_sorted = {}
        for i in gp:
            nul = sorted(v for v in (X[p][i] for p in orp) if v is not None)
            col = sorted(v for v in (X[p][i] for p in X) if v is not None)
            arr_sorted[i] = col
            thr["p95"][i] = nul[int(0.95 * len(nul))]
            thr["p99"][i] = nul[min(len(nul) - 1, int(0.99 * len(nul)))]
            thr["med"][i] = col[len(col) // 2]

        for lv in LEVELS:
            frac = statistics.fmean(
                sum(1 for v in arr_sorted[i] if v > thr[lv][i]) / len(arr_sorted[i])
                for i in gp)
            rows.append({"dataset": gse, "level": lv,
                         "array_fraction_above_threshold": round(frac, 3)})

        for g in targets:
            probes = [p for p in idx.get(g, []) if p in X]
            if not probes:
                continue
            for i in gp:
                best = max((X[p][i] for p in probes if X[p][i] is not None),
                           default=None)
                if best is None:
                    continue
                col = arr_sorted[i]
                lo = sum(1 for v in col if v < best)
                pct_rows.append({
                    "dataset": gse, "platform": meta["family"], "gene": g,
                    "array": labels[i][:44], "value": round(best, 3),
                    "percentile_within_array": round(100.0 * lo / len(col), 1),
                    "p95": int(best > thr["p95"][i]),
                    "p99": int(best > thr["p99"][i]),
                    "med": int(best > thr["med"][i])})

    os.makedirs(A.RES, exist_ok=True)
    with open(os.path.join(A.RES, "posthoc_stringency.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(pct_rows[0]))
        w.writeheader(); w.writerows(pct_rows)

    print("ARRAY FRACTION CLEARING EACH THRESHOLD (mean over growth-plate arrays)")
    for r in rows:
        print(f"  {r['dataset']} {r['level']:4s} {100*r['array_fraction_above_threshold']:5.1f}%")

    print("\nPER-GENE, per dataset: median percentile within its own array, and the "
          "majority call at each stringency")
    print(f"  {'gene':10s} {'dataset':9s} {'pct':>6s}  p95 p99 med")
    for g in targets:
        for gse in A.SERIES:
            sub = [r for r in pct_rows if r["gene"] == g and r["dataset"] == gse]
            if not sub:
                continue
            med = statistics.median(r["percentile_within_array"] for r in sub)
            calls = {lv: sum(r[lv] for r in sub) > len(sub) / 2 for lv in LEVELS}
            flag = ""
            if calls["p95"] and not calls["med"]:
                flag = "  <- DETECTED only at the loosest threshold"
            print(f"  {g:10s} {gse:9s} {med:6.1f}  "
                  f"{'Y' if calls['p95'] else '.'}   "
                  f"{'Y' if calls['p99'] else '.'}   "
                  f"{'Y' if calls['med'] else '.'}{flag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
