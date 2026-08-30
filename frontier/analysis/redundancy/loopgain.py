"""Estimate the gain of the proposed SPIN4 <-> Wnt positive feedback loop.

Loop:  drug lowers Wnt output  ->  less TCF7L2 drive on SPIN4  ->  less SPIN4
       ->  SPIN4 promotes Wnt, so Wnt falls further.
Gain   g = (dlnW/dlnS) * (dlnS/dlnW).  Amplification of a small drug input = 1/(1-g).

Two terms, measured separately:
  TERM A  dlnW/dlnS : from Lui 2023 Fig 6C -- complete Spin4 loss lowers TOPFLASH 1.00 -> 0.62.
  TERM B  dlnS/dlnW : how strongly Wnt output drives SPIN4. Measured two independent ways:
      B1  concordance of SPIN4 with canonical Wnt targets across ~270 RummaGEO drug signatures
      B2  zonal co-variation of SPIN4 with Wnt output in human growth plate (GSE9160)
"""
import json, re, collections, math

MW = None
PANEL = ["AXIN2","LEF1","TCF7","NKD1","RNF43","ZNRF3","SP5","CCND1","NOTUM","TNFRSF19"]

# ---------- TERM A ----------
print("=" * 78)
print("TERM A -- dlnW/dlnS, from Lui 2023 Fig 6C (isolated growth-plate chondrocytes)")
print("=" * 78)
A = 1 - 0.62
print("  complete Spin4 loss (S: 1 -> 0) lowers TOPFLASH 1.00 -> 0.62")
print("  SPIN4's TOTAL contribution to Wnt output = %.2f" % A)
print("  -> dlnW/dlnS <= %.2f at the WT operating point (upper bound: assumes linearity)" % A)

# ---------- TERM B1 : drug signatures ----------
def drugsigs(fn):
    d = json.load(open(fn))
    out = {}
    for x in d.get('associations', []):
        n = x['geneSet']['name']
        if '/' not in n:
            continue
        s, ds = n.split('/', 1)
        if not ds.startswith('RummaGEO Drug'):
            continue
        out[s] = -1 if x['thresholdValue'] < 0 else 1
    return out

S4 = drugsigs('hz_SPIN4.json')
W = {g: drugsigs('hz_%s.json' % g) for g in PANEL}

print()
print("=" * 78)
print("TERM B1 -- dlnS/dlnW from %d RummaGEO drug perturbation signatures" % len(S4))
print("=" * 78)
conc = disc = 0
per_gene = {}
for g, d in W.items():
    c = s_ = 0
    for sig, v in S4.items():
        if sig in d:
            if d[sig] == v: c += 1
            else: s_ += 1
    per_gene[g] = (c, s_)
    conc += c; disc += s_
print("  %-10s %8s %8s %9s" % ("Wnt gene", "concord", "discord", "% concord"))
for g in PANEL:
    c, s_ = per_gene[g]
    if c + s_:
        print("  %-10s %8d %8d %8.1f%%" % (g, c, s_, 100.0 * c / (c + s_)))
tot = conc + disc
p = conc / tot
print("  %-10s %8d %8d %8.1f%%" % ("TOTAL", conc, disc, 100 * p))
# binomial test vs 50%
se = math.sqrt(0.25 / tot)
z = (p - 0.5) / se
print("  vs chance (50%%): z = %.2f  (n = %d co-occurrences)" % (z, tot))
# Convert concordance to an elasticity-like coupling.  Perfect coupling = 100% concordance.
# A gene fully driven by Wnt would move with the panel every time.  Scale: (p-0.5)/0.5
B1 = max(0.0, (p - 0.5) / 0.5)
print("  -> coupling index (0 = independent, 1 = perfectly co-regulated): %.3f" % B1)

# ---------- comparison: how does a REAL Wnt target score on the same test? ----------
print()
print("  CONTROL -- run the identical test on AXIN2, a bona fide canonical Wnt target,")
print("  against the other 9 panel genes. This calibrates what 'strongly Wnt-driven' looks like.")
AX = drugsigs('hz_AXIN2.json')
c2 = s2 = 0
for g in PANEL:
    if g == 'AXIN2':
        continue
    d = W[g]
    for sig, v in AX.items():
        if sig in d:
            if d[sig] == v: c2 += 1
            else: s2 += 1
p2 = c2 / (c2 + s2)
print("  AXIN2 vs panel: %d concordant / %d discordant = %.1f%%  (n=%d)" % (c2, s2, 100 * p2, c2 + s2))
B_ref = (p2 - 0.5) / 0.5
print("  -> reference coupling index for a real Wnt target: %.3f" % B_ref)
print("  -> SPIN4 coupling RELATIVE to a real Wnt target: %.2f" % (B1 / B_ref if B_ref else float('nan')))

# ---------- TERM B2 : zonal co-variation in human growth plate ----------
print()
print("=" * 78)
print("TERM B2 -- zonal co-variation, human growth plate (GSE9160, 5 zones)")
print("=" * 78)
zones = ["Reserve", "Prolif", "PreHyp", "Hyper"]
prof = {
    "AXIN2":  [809.6, 564.1, 361.4, 2699.9],
    "SP5":    [33.9, 31.2, 29.3, 97.5],
    "LGR5":   [64.7, 34.2, 65.8, 317.4],
    "NKD1":   [211.6, 199.5, 231.8, 319.5],
    "SPIN4":  [90.9, 267.8, 193.2, 153.6],
}
def pearson(a, b):
    n = len(a); ma = sum(a)/n; mb = sum(b)/n
    num = sum((x-ma)*(y-mb) for x, y in zip(a, b))
    da = math.sqrt(sum((x-ma)**2 for x in a)); db = math.sqrt(sum((y-mb)**2 for y in b))
    return num/(da*db) if da and db else float('nan')
print("  %-8s %9s %9s %9s %9s   r(vs SPIN4)" % ("gene", *[z[:6] for z in zones]))
rs = []
for g in ["AXIN2", "SP5", "LGR5", "NKD1"]:
    r = pearson(prof[g], prof["SPIN4"])
    rs.append(r)
    print("  %-8s " % g + " ".join("%9.1f" % v for v in prof[g]) + "   %+.3f" % r)
print("  %-8s " % "SPIN4" + " ".join("%9.1f" % v for v in prof["SPIN4"]))
print("  mean r(SPIN4, Wnt output) across zones = %+.3f" % (sum(rs)/len(rs)))
print("  ** n=4 zones, n=2 donors -- INDICATIVE ONLY, not a significance test **")

# ---------- combine ----------
print()
print("=" * 78)
print("LOOP GAIN AND AMPLIFICATION")
print("=" * 78)
for label, B in [("B1 drug-signature coupling", B1),
                 ("B1 scaled to a real Wnt target's coupling", B1 / B_ref if B_ref else 0.0)]:
    g_loop = A * B
    amp = 1 / (1 - g_loop) if g_loop < 1 else float('inf')
    print("  %-45s B=%.3f  g=A*B=%.3f  amplification=%.2fx" % (label, B, g_loop, amp))
    print("       -> a 3.5%% drug input becomes %.1f%%   (target 40%%)" % (3.5 * amp))
