#!/usr/bin/env python3
"""
Round 243. Round 241 claimed, from the HUMAN figures, that the root cell holds
itself in the root state with a self-secreted double antagonist screen: soluble
WNT inhibitors plus soluble TGF-beta inhibitors (THBS1/2/4, DCN).

chu2026's supplement contains a table the main text never shows: the full
GP1-versus-GP2 differential expression list FOR THE MOUSE, 15,985 genes with
log2 fold change and adjusted P. That is an independent species inside the same
paper, and it makes the claim testable rather than merely asserted.

This script does three things and refuses to do a fourth:
  1. Fixes the sign convention from known markers rather than assuming it.
  2. Asks whether the mouse root cluster carries the same antagonists.
  3. Reports the genes that FAIL as loudly as the ones that pass.
It does not compute a summary statistic over a hand-picked gene set, because a
gene set chosen after seeing the human result would make any enrichment circular.
"""
import csv, sys, math

PATH = 'atlas/data/round243_supplied/chu2026_supp/adw3590_data_file_s1.csv'

def num(s):
    if s is None: return None
    s = s.strip().replace(',', '.')
    if not s: return None
    try: return float(s)
    except ValueError: return None

rows = {}
with open(PATH, encoding='utf-8-sig') as f:
    lines = f.read().split('\n')
hdr = None
for l in lines:
    p = l.split(';')
    if p[0] == 'Gene':
        hdr = p; continue
    if hdr is None or len(p) < 7: continue
    g = p[0].strip().upper()
    if not g: continue
    rows[g] = dict(baseMean=num(p[1]), lfc=num(p[2]), pval=num(p[5]), padj=num(p[6]))

print(f"parsed {len(rows)} genes from the mouse GP1-vs-GP2 table")
tested = {g: v for g, v in rows.items() if v['lfc'] is not None and v['padj'] is not None}
print(f"{len(tested)} have a fold change and an adjusted P (the rest are zero-count rows)\n")

# ---------------------------------------------------------------- sign convention
# Do NOT assume which direction is GP1. Fix it from markers the paper itself
# assigns: CYTL1/GAS1/SFRP5/APOE mark the root cluster, PTHLH marks GP2.
print("=" * 74)
print("STEP 1 - FIX THE SIGN CONVENTION FROM MARKERS, DO NOT ASSUME IT")
print("=" * 74)
# The paper's OWN assignment: CYTL1 marks GP1, RAMP3 marks GP2, and SFRP5 and APOE
# are shared RESTING ZONE markers enriched in BOTH GP1 and GP2 - so SFRP5 and APOE
# CANNOT fix the direction and it was an error to try. CYTL1 is the discriminator.
probe = ['CYTL1', 'GAS1', 'RAMP3', 'PTHLH', 'SFRP5', 'APOE', 'PRG4', 'IBSP']
for g in probe:
    v = rows.get(g)
    if v is None or v['lfc'] is None or v['padj'] is None:
        bm = (v or {}).get('baseMean')
        bm = f"{bm:.2f}" if bm is not None else "-"
        print(f"  {g:<8} not testable (baseMean {bm}) - no fold change reported"); continue
    print(f"  {g:<8} log2FC {v['lfc']:+8.3f}   padj {v['padj']:.2e}   baseMean {v['baseMean']:8.2f}")

print()
print("  READING: SFRP5 and APOE are enriched in BOTH human GP1 and GP2 as shared resting")
print("  zone markers, so they carry no directional information and are excluded. PTHLH in")
print("  mouse has baseMean 0.42 and is not significant - too lowly expressed to use.")
print("  CYTL1 is the paper's own GP1 discriminator and it is unambiguous.")

cy = rows.get('CYTL1', {}).get('lfc')
gs = rows.get('GAS1', {}).get('lfc')
if cy is None:
    print("\nCYTL1 absent - the convention cannot be fixed. STOPPING."); sys.exit(1)
sign = 1 if cy > 0 else -1
agree = (gs is not None) and ((gs > 0) == (cy > 0))
print(f"\n  CONVENTION FIXED ON CYTL1 (log2FC {cy:+.3f}, padj {rows['CYTL1']['padj']:.1e}):")
print(f"  {'POSITIVE' if sign>0 else 'NEGATIVE'} log2FC = enriched in GP1, the root cluster")
print(f"  GAS1, the quiescent-stem-cell marker, {'AGREES' if agree else 'DISAGREES'} "
      f"(log2FC {gs:+.3f})" if gs is not None else "  GAS1 not testable")
if not agree:
    print("  GAS1 DISAGREES WITH CYTL1 - the direction is NOT safe and every result below")
    print("  must be read as conditional on the CYTL1 assignment alone.")

print()
print("  CAUTION CARRIED FORWARD: PRG4 and IBSP are the two largest effects in the whole")
print("  table and both fall on the GP1 side. PRG4 is an articular-surface marker and IBSP")
print("  is bone sialoprotein. THE MOUSE GP1 CLUSTER MAY CONTAIN ARTICULAR OR PERICHONDRIAL")
print("  CELLS THAT THE HUMAN GP1 CLUSTER DOES NOT. That is a real limit on this comparison")
print("  and it is not resolvable from a DEG table alone.")
print()

def root_lfc(g):
    v = rows.get(g)
    if v is None or v['lfc'] is None or v['padj'] is None: return None
    return sign * v['lfc'], v['padj'], v['baseMean']

# ---------------------------------------------------------------- the test
print("=" * 74)
print("STEP 2 - DOES THE MOUSE ROOT CLUSTER CARRY THE SAME BRAKE?")
print("=" * 74)

PANELS = [
    ("SOLUBLE TGF-BETA INHIBITORS - the four named in the human root cell",
     ['THBS1', 'THBS2', 'THBS4', 'DCN']),
    ("SOLUBLE WNT INHIBITORS - the families the human figure counts nine of",
     ['SFRP1', 'SFRP2', 'SFRP4', 'SFRP5', 'DKK1', 'DKK2', 'DKK3', 'WIF1',
      'SOST', 'SOSTDC1', 'NOTUM', 'FRZB', 'APCDD1', 'KREMEN1', 'KREMEN2']),
    ("WNT LIGANDS - the four the human root cell does express",
     ['WNT4', 'WNT5A', 'WNT5B', 'WNT9A', 'WNT11', 'WNT16', 'WNT2B', 'WNT10B']),
    ("WNT RECEPTORS AND CO-RECEPTORS - is the cell deaf, or is it shouting no?",
     ['LRP5', 'LRP6', 'FZD1', 'FZD2', 'FZD4', 'FZD6', 'FZD8', 'CTNNB1']),
    ("QUIESCENCE AND ROOT IDENTITY",
     ['GAS1', 'CYTL1', 'SFRP5', 'APOE', 'PRRX1', 'FOXA2', 'MKI67', 'CCND1']),
    ("THE GH / IGF AXIS - does the mouse show the same receptor split?",
     ['GHR', 'IGF1', 'IGF1R', 'IGFBP3', 'STAT5A', 'STAT5B', 'PTH1R', 'PTHLH']),
    ("TGF-BETA / BMP MACHINERY",
     ['TGFB1', 'TGFB2', 'TGFB3', 'TGFBR1', 'TGFBR2', 'TGFBR3', 'LTBP1',
      'INHBA', 'SMAD2', 'SMAD3', 'BMP2', 'BMP4', 'SOX4', 'SOX9']),
]

SIG = 0.05
summary = {}
for title, genes in PANELS:
    print(f"\n--- {title}")
    print(f"    {'gene':<9}{'log2FC(root)':>13}{'padj':>12}{'baseMean':>11}   verdict")
    hits = miss = absent = 0
    for g in genes:
        r = root_lfc(g)
        if r is None:
            print(f"    {g:<9}{'-':>13}{'-':>12}{'-':>11}   not tested (zero counts)")
            absent += 1; continue
        lfc, padj, bm = r
        if padj < SIG and lfc > 0:
            v = "ROOT-ENRICHED"; hits += 1
        elif padj < SIG and lfc < 0:
            v = "opposite - GP2-enriched"; miss += 1
        else:
            v = "not significant"
        print(f"    {g:<9}{lfc:>+13.3f}{padj:>12.2e}{bm:>11.2f}   {v}")
    summary[title] = (hits, miss, absent, len(genes))

print("\n" + "=" * 74)
print("STEP 3 - THE TALLY, INCLUDING WHAT FAILED")
print("=" * 74)
for title, (h, m, a, n) in summary.items():
    print(f"  {h:>2} root-enriched / {m:>2} opposite / {a:>2} untested   of {n:>2}   {title[:52]}")

# ---------------------------------------------------------------- unbiased view
print("\n" + "=" * 74)
print("STEP 4 - THE UNBIASED VIEW: top root-enriched genes, chosen by the data")
print("=" * 74)
print("A gene set picked after reading the human result proves nothing. This ranks")
print("every adequately expressed gene and simply reports what the top of the list is.\n")
cand = [(g, sign * v['lfc'], v['padj'], v['baseMean'])
        for g, v in tested.items()
        if v['padj'] < 0.01 and v['baseMean'] >= 1.0]
cand.sort(key=lambda x: -x[1])
print(f"  {len(cand)} genes at padj<0.01 and baseMean>=1\n")
print("  TOP 40 ROOT-ENRICHED:")
for g, l, p, b in cand[:40]:
    print(f"    {g:<12}{l:+8.3f}  padj {p:.1e}  baseMean {b:8.2f}")
print("\n  TOP 20 GP2-ENRICHED (the other direction, for contrast):")
for g, l, p, b in sorted(cand, key=lambda x: x[1])[:20]:
    print(f"    {g:<12}{l:+8.3f}  padj {p:.1e}  baseMean {b:8.2f}")

# where do the brake genes rank among all root-enriched genes?
print("\n" + "=" * 74)
print("STEP 5 - WHERE THE BRAKE GENES ACTUALLY RANK")
print("=" * 74)
order = [g for g, _, _, _ in cand]
n = len(order)
for g in ['THBS1', 'THBS2', 'THBS4', 'DCN', 'SFRP5', 'GAS1', 'CYTL1', 'APOE']:
    if g in order:
        i = order.index(g)
        print(f"  {g:<8} rank {i+1:>5} of {n} root-enriched  (top {100*(i+1)/n:.1f}%)")
    else:
        v = rows.get(g)
        why = "not significant at padj<0.01 or baseMean<1" if v and v['lfc'] is not None else "not tested"
        print(f"  {g:<8} NOT in the root-enriched set - {why}")
