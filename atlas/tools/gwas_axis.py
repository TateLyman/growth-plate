"""Common variation in the OESTROGEN/FUSION axis versus the CNP/GH VELOCITY axis:
which moves adult height more, in the same people, in the same units?

FIRST VERSION OF THIS SCRIPT WAS WRONG AND IS RECORDED AS SUCH. It selected each
gene's lead SNP by |BETA|, which selects rare variants with enormous standard errors:
CYP19A1 came back at 2.06 SD per allele with P=0.04, GDF5's true lead (rs143384,
P=3.4e-1152, beta 0.079) was missed, and a NEGATIVE CONTROL out-scored every positive
control. The guard on negative-vs-positive controls passed only because it compared
medians. Lead SNPs are now selected by MINIMUM P, and effect sizes are compared only
among COMMON variants.

WHAT THIS IS NOT: a gene-based association test. No LD reference is used, so this is a
WINDOWED LOOKUP and a window can capture a neighbour's signal. Graded accordingly.

GUARDS, declared before results are seen:
  G1  Build confirmed empirically - rs143384 at chr20:34,025,756 (GRCh37).
  G2  POSITIVE CONTROLS (GDF5, HMGA2, ZBTB38, LCORL) must each reach P < 1e-20.
  G3  Every NEGATIVE CONTROL's best P must be WEAKER than every positive control's.
      Not medians - the failure of the first version was hidden by a median.
  G4  The comparison is on EFFECT SIZE at common variants, not on whether a signal
      exists. Height is polygenic enough that significance alone means little.
"""
import gzip, json, collections, statistics, sys

WINDOW, GW, MAF_MIN = 100_000, 5e-8, 0.01
genes = json.load(open("gene_coords_b37.json"))
byc = collections.defaultdict(list)
for g, v in genes.items():
    byc[v["chr"]].append((max(0, v["start"] - WINDOW), v["end"] + WINDOW, g))

hits = {g: [] for g in genes}
n = skipped = 0
with gzip.open("gwas/GIANT_HEIGHT_YENGO_2022_GWAS_SUMMARY_STATS_EUR.gz", "rt") as f:
    hdr = f.readline().rstrip("\n").split("\t")
    iC,iP,iB,iS,iPv,iR,iF = (hdr.index(x) for x in ("CHR","POS","BETA","SE","P","RSID","EFFECT_ALLELE_FREQ"))
    for line in f:
        p = line.rstrip("\n").split("\t")
        c = p[iC]
        if c not in byc: continue
        pos = int(p[iP])
        tgt = [g for lo,hi,g in byc[c] if lo <= pos <= hi]
        if not tgt: continue
        try: b, pv, fr, se = float(p[iB]), float(p[iPv]), float(p[iF]), float(p[iS])
        except ValueError: skipped += 1; continue
        maf = min(fr, 1-fr)
        for g in tgt: hits[g].append((pv, b, se, maf, p[iR]))
        n += 1
print(f"{n:,} SNPs mapped into windows; {skipped} skipped for missing fields\n")

rows=[]
for g,v in genes.items():
    h = hits[g]
    common = [x for x in h if x[3] >= MAF_MIN]
    lead = min(h, key=lambda x:x[0]) if h else None
    leadc = min(common, key=lambda x:x[0]) if common else None
    gw_common = [x for x in common if x[0] < GW]
    rows.append(dict(gene=g, cls=v["cls"], n_snp=len(h), n_common=len(common),
        n_gw_common=len(gw_common),
        lead_p=lead[0] if lead else None, lead_beta=lead[1] if lead else None,
        lead_rs=lead[4] if lead else None,
        c_p=leadc[0] if leadc else None, c_beta=leadc[1] if leadc else None,
        c_maf=leadc[3] if leadc else None, c_rs=leadc[4] if leadc else None,
        max_abs_beta_gw=max((abs(x[1]) for x in gw_common), default=None)))

fail=[]
P = {r["gene"]:r for r in rows}
for g in ("GDF5","HMGA2","ZBTB38","LCORL"):
    # P underflows to 0.0 below about 1e-308, and 0.0 is FALSY in Python - an earlier
    # version of this guard read the strongest possible signals as missing data.
    if P[g]["lead_p"] is None or P[g]["lead_p"] >= 1e-20:
        fail.append(f"G2 FAILED: positive control {g} lead P = {P[g]['lead_p']}")
worst_pos = max(P[g]["lead_p"] for g in ("GDF5","HMGA2","ZBTB38","LCORL"))
for g in ("OR2L13","TAS2R38","MYOZ1","CFTR"):
    if P[g]["lead_p"] is not None and P[g]["lead_p"] <= worst_pos:
        fail.append(f"G3 FAILED: negative control {g} (P={P[g]['lead_p']:.2e}) is at least as strong "
                    f"as the weakest positive control (P={worst_pos:.2e})")
if fail:
    print("\n".join(fail)); print("\nREFUSING TO REPORT."); sys.exit(1)
print(f"guards PASS - weakest positive control P = {worst_pos:.2e}; "
      f"strongest negative control P = {min(P[g]['lead_p'] for g in ('OR2L13','TAS2R38','MYOZ1','CFTR')):.2e}\n")

print(f"{'gene':<10} {'class':<12} {'nCommon':>8} {'nGWsig':>7} {'lead P':>11} {'beta':>8} {'MAF':>6}  lead SNP")
for cls in ["duration","velocity","structure","control_pos","control_neg"]:
    for r in sorted([x for x in rows if x["cls"]==cls], key=lambda x: x["c_p"] if x["c_p"] is not None else 9):
        if r["c_p"] is None: print(f"{r['gene']:<10} {cls:<12} {'no data in this SNP set':>40}"); continue
        print(f"{r['gene']:<10} {cls:<12} {r['n_common']:>8} {r['n_gw_common']:>7} {r['c_p']:>11.2e} "
              f"{r['c_beta']:>8.4f} {r['c_maf']:>6.3f}  {r['c_rs']}")
    print()

print("=== CLASS SUMMARY - |beta| of the lead COMMON variant, in SD of height per allele ===")
print(f"{'class':<14} {'n':>3} {'median':>8} {'max':>8}   {'genes reaching p<5e-8':>22}")
for cls in ["duration","velocity","structure","control_pos","control_neg"]:
    v=[abs(r["c_beta"]) for r in rows if r["cls"]==cls and r["c_beta"] is not None]
    sig=[r["gene"] for r in rows if r["cls"]==cls and r["n_gw_common"]]
    print(f"{cls:<14} {len(v):>3} {statistics.median(v):>8.4f} {max(v):>8.4f}   {len(sig)}/{len(v)}: {', '.join(sig)[:70]}")
json.dump(rows, open("gwas_axis.json","w"), indent=1)
