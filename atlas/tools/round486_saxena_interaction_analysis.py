#!/usr/bin/env python3
"""
R486 step 3 - the quantitative read, with the composition confound priced first.

FOUR THINGS, IN THIS ORDER, BECAUSE THE ORDER IS THE ARGUMENT:
  (1) THE COMPOSITION CONFOUND, MEASURED.  CORR-339 says ask what ELSE is in
      each tissue.  The controls in step 2 show MUSCLE and BONE up and
      CARTILAGE down in the interaction.  Quantify it and state the correction
      it implies before reading any panel.
  (2) THE RA TARGET-GENE READOUT.  If retinoic acid SIGNALLING is genuinely
      lower in the elongating element, the DIRECT RA-INDUCIBLE GENES must be
      coordinately down.  This is the test that can refute the story, so it is
      run as a panel rather than gene by gene.
  (3) THE UNBIASED TOP OF THE INTERACTION, replicated across both cohorts.
  (4) THE TWO IGFBP-3/-5 PROTEASES, which is where the atlas's own live arm is.

Positive interaction = relatively higher in the JERBOA METATARSAL, the element
that is disproportionately elongated.
"""
import csv, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data', 'round486')


def load(tag):
    out = {}
    with open(os.path.join(D, f'saxena_deseq2_{tag}.tsv')) as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            for k in list(r):
                if k not in ('transcript', 'symbol'):
                    r[k] = float(r[k]) if r[k] not in ('', 'None') else None
            out[r['transcript']] = r
    return out


n3, n2 = load('n3'), load('n2')
sym3 = {}
for r in n3.values():
    sym3.setdefault(r['symbol'], r)


def inter(sym, cohort):
    src = n3 if cohort == 3 else n2
    for r in src.values():
        if r['symbol'] == sym:
            return r['interaction_MT_minus_RU']
    return None


def line(c='='): print(c * 100)


# ---------------------------------------------------------------- (1) confound
line(); print('(1) THE COMPOSITION CONFOUND, MEASURED BEFORE ANYTHING ELSE'); line()
groups = {
    'CARTILAGE  (Col2a1 Acan Col11a1 Comp Hapln1 Col9a1 Col9a2 Sox9)':
        ['Col2a1', 'Acan', 'Col11a1', 'Comp', 'Hapln1', 'Col9a1', 'Col9a2', 'Sox9'],
    'MUSCLE     (Myh3 Acta1 Myog Tnnt1 Des Myl4 Tnnc2 Mylpf)':
        ['Myh3', 'Acta1', 'Myog', 'Tnnt1', 'Des', 'Myl4', 'Tnnc2', 'Mylpf'],
    'BONE       (Col1a1 Alpl Ibsp Sp7 Sparc Postn)':
        ['Col1a1', 'Alpl', 'Ibsp', 'Sp7', 'Sparc', 'Postn'],
    'HOUSEKEEP  (Actb Ppia Sdha Hprt Tubb5 Gapdh)':
        ['Actb', 'Ppia', 'Sdha', 'Hprt', 'Tubb5', 'Gapdh'],
}
med = {}
for g, gl in groups.items():
    vals = [sym3[s]['interaction_MT_minus_RU'] for s in gl
            if s in sym3 and sym3[s]['interaction_MT_minus_RU'] is not None]
    vals.sort()
    m = vals[len(vals) // 2] if vals else None
    med[g.split()[0]] = m
    print(f'  {g:<58} n={len(vals)}  median interaction {m:+.2f}   '
          f'range {min(vals):+.2f} to {max(vals):+.2f}')
print()
print(f'  => THE JERBOA METATARSAL SAMPLE IS RELATIVELY CARTILAGE-POOR AND')
print(f'     MUSCLE- AND BONE-RICH.  Cartilage median {med["CARTILAGE"]:+.2f}, '
      f'muscle {med["MUSCLE"]:+.2f}, bone {med["BONE"]:+.2f}, housekeeping {med["HOUSEKEEP"]:+.2f}.')
print(f'  => TWO CONSEQUENCES.  A POSITIVE interaction for any gene expressed in')
print(f'     muscle or bone may be contamination.  A NEGATIVE interaction for a')
print(f'     cartilage gene may be dilution: the cartilage-normalised value is')
print(f'     roughly interaction minus ({med["CARTILAGE"]:+.2f}).')

# ------------------------------------------------------- (2) RA target readout
line(); print('(2) THE RA TARGET-GENE READOUT - the test that can refute the story'); line()
print('  Direct, canonical retinoic-acid-INDUCIBLE genes.  If RA SIGNALLING were')
print('  lower in the elongating element these must be COORDINATELY NEGATIVE.')
print()
ra_targets = ['Cyp26a1', 'Cyp26b1', 'Cyp26c1', 'Rarb', 'Dhrs3', 'Crabp2', 'Stra6',
              'Hoxa1', 'Hoxb1', 'Rbp1', 'Nr2f1', 'Nr2f2']
print(f'  {"gene":<10}{"MT lfc":>9}{"RU lfc":>9}{"INTER n3":>10}{"INTER n2":>10}  direction')
pos = neg = 0
for g in ra_targets:
    if g not in sym3:
        print(f'  {g:<10}   not in the 1:1 orthologue set'); continue
    r = sym3[g]; i3 = r['interaction_MT_minus_RU']; i2 = inter(g, 2)
    if i3 is None: continue
    d = 'DOWN in elongating' if i3 < 0 else 'UP in elongating'
    if i3 < 0: neg += 1
    else: pos += 1
    print(f'  {g:<10}{r["MT_log2FoldChange"]:>9.2f}{r["RU_log2FoldChange"]:>9.2f}'
          f'{i3:>10.2f}{(f"{i2:>10.2f}" if i2 is not None else "         -")}  {d}')
print()
print(f'  => {neg} DOWN, {pos} UP.  THE READOUT IS NOT COHERENT.  A simple "RA')
print(f'     signalling is lower in the elongating element" reading is NOT supported:')
print(f'     Cyp26a1 and Cyp26c1 go down while Rarb, Dhrs3, Crabp2 and Stra6 go up.')
print(f'     RECORDED AS MIXED.  What survives is the BINDING-PROTEIN shift, not a')
print(f'     demonstrated change in pathway output.')

# --------------------------------------------------- (3) unbiased top, replicated
line(); print('(3) THE UNBIASED TOP OF THE INTERACTION, REPLICATED IN BOTH COHORTS'); line()
cand = []
for t, r in n3.items():
    i3 = r['interaction_MT_minus_RU']
    r2 = n2.get(t)
    i2 = r2['interaction_MT_minus_RU'] if r2 else None
    if i3 is None or i2 is None: continue
    if r['MT_baseMean'] is None or r['MT_baseMean'] < 50: continue      # abundance floor
    if (i3 > 0) != (i2 > 0): continue                                   # must replicate in sign
    if r['MT_padj'] is None or r['MT_padj'] > 0.01: continue            # MT contrast significant
    cand.append((abs(i3), i3, i2, r))
cand.sort(reverse=True)
print(f'  {len(cand)} genes pass: baseMean>=50, MT padj<0.01, same interaction sign in BOTH cohorts.')
print(f'\n  TOP 25 UP in the elongating element:')
print(f'  {"gene":<12}{"baseMn":>10}{"MT lfc":>8}{"RU lfc":>8}{"n3":>8}{"n2":>8}')
ups = [c for c in cand if c[1] > 0][:25]
for _, i3, i2, r in ups:
    print(f'  {r["symbol"]:<12}{r["MT_baseMean"]:>10.0f}{r["MT_log2FoldChange"]:>8.2f}'
          f'{r["RU_log2FoldChange"]:>8.2f}{i3:>8.2f}{i2:>8.2f}')
print(f'\n  TOP 25 DOWN in the elongating element:')
print(f'  {"gene":<12}{"baseMn":>10}{"MT lfc":>8}{"RU lfc":>8}{"n3":>8}{"n2":>8}')
dns = [c for c in cand if c[1] < 0][:25]
for _, i3, i2, r in dns:
    print(f'  {r["symbol"]:<12}{r["MT_baseMean"]:>10.0f}{r["MT_log2FoldChange"]:>8.2f}'
          f'{r["RU_log2FoldChange"]:>8.2f}{i3:>8.2f}{i2:>8.2f}')

# ------------------------------------------------------- (4) the IGFBP proteases
line(); print('(4) THE TWO IGFBP-3/-5 PROTEASES - the atlas\'s own live arm'); line()
print('  loechel2000: ADAM12-S cleaves IGFBP-3 and IGFBP-5 and NOT IGFBP-1/2/4/6.')
print('  PAPPA2 cleaves IGFBP-3 and IGFBP-5.  PAPPA cleaves IGFBP-4.')
print('  So ADAM12 and PAPPA2 are SUBSTRATE-MATCHED and PAPPA is the internal control.')
print()
for g in ['Adam12', 'Pappa2', 'Pappa', 'Igfbp3', 'Igfbp5', 'Igfbp4', 'Stc2', 'Stc1']:
    if g not in sym3:
        print(f'  {g:<10} not in the 1:1 orthologue set'); continue
    r = sym3[g]; i3 = r['interaction_MT_minus_RU']; i2 = inter(g, 2)
    cn = (i3 - med['CARTILAGE']) if i3 is not None else None
    print(f'  {g:<10} baseMean {r["MT_baseMean"]:>9.0f}  MT {r["MT_log2FoldChange"]:+.2f} '
          f'(padj {r["MT_padj"] if r["MT_padj"] is not None else float("nan"):.4f})  '
          f'RU {r["RU_log2FoldChange"]:+.2f}  INTER n3 {i3:+.2f}  n2 '
          f'{(f"{i2:+.2f}" if i2 is not None else "  -  ")}  cartilage-normalised {cn:+.2f}')
line()
