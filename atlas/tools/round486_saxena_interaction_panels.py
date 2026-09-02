#!/usr/bin/env python3
"""
R486 step 2 - the species x element INTERACTION, read against preregistered panels.

INSTRUMENT.  saxena2022's own deposited DESeq2 output (Zenodo 5123384), 17,464
mouse-jerboa 1:1 orthologues, postnatal day 5, TWO INDEPENDENT COHORTS (primary
n=3 and validation n=2), each with two contrasts: Jerboa:Mouse in the METATARSAL
and Jerboa:Mouse in the RADIUS/ULNA.  Positive LFC = higher in jerboa.

THE SIGNAL IS THE INTERACTION, MT_LFC - RU_LFC.  A gene that differs between
species in BOTH elements is a species difference; only the interaction carries
PROPORTION.  Requiring the same sign in BOTH cohorts is the replication filter.

CONTROLS ARE DECLARED HERE, BEFORE THE QUESTION PANELS, per CORR-311 (the
negative control is rows you already have) and CORR-339 (before any cross-tissue
contrast, ask what ELSE is in each tissue and put a marker of it in the panel).
The tissue is whole growth cartilage, so muscle, blood and bone contamination
must be scored, and positional HOX must be scored because MT and RU are
different limb segments by construction.

NOTHING HERE IS A HUMAN RESULT.  Mouse and jerboa, one postnatal day.
"""
import csv, os, statistics as st

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data', 'round486')

CONTROLS = {
    'POSCTRL_saxena_named':      ['Shox2', 'Crabp1', 'Gdf10', 'Mab21l2'],
    'POSCTRL_positional_HOX':    ['Hoxa13', 'Hoxd13', 'Hoxa11', 'Hoxd11', 'Hoxb9', 'Tbx5', 'Pitx1'],
    'NEGCTRL_housekeeping':      ['Gapdh', 'Actb', 'Ppia', 'Tubb5', 'Rpl13a', 'Hprt', 'Sdha'],
    'CONFOUND_muscle':           ['Myh3', 'Acta1', 'Myod1', 'Ckm', 'Myog', 'Tnnt1'],
    'CONFOUND_blood':            ['Hba-a1', 'Hbb-bs', 'Ptprc', 'Cd74'],
    'CONFOUND_bone':             ['Bglap', 'Sp7', 'Ibsp', 'Col1a1', 'Alpl'],
}

PANELS = {
    'RA_synthesis':   ['Aldh1a1', 'Aldh1a2', 'Aldh1a3', 'Rdh10', 'Dhrs3', 'Rbp1', 'Rbp4', 'Stra6'],
    'RA_clearance':   ['Cyp26a1', 'Cyp26b1', 'Cyp26c1'],
    'RA_binding':     ['Crabp1', 'Crabp2', 'Fabp5'],
    'RA_receptors':   ['Rara', 'Rarb', 'Rarg', 'Rxra', 'Rxrb', 'Rxrg'],
    'vc_anabolic':    ['Igf1', 'Igf2', 'Igf1r', 'Irs1', 'Slc2a1', 'Slc2a4', 'Gsk3b'],
    'vc_glycogen':    ['Gys1', 'Gyg', 'Gbe1', 'Ppp1r3c', 'Ppp1r3g', 'Stbd1', 'Gaa', 'Pygl', 'Pygm', 'Agl'],
    'vm_matrix':      ['Col2a1', 'Acan', 'Col11a1', 'Comp', 'Hapln1', 'Serpinh1', 'Col27a1'],
    'vm_sulfation':   ['Xylt1', 'Xylt2', 'Chst3', 'Chst11', 'Slc35b2', 'Papss1', 'Papss2', 'Slc26a2', 'Impad1'],
    'hypertrophy':    ['Ihh', 'Pthlh', 'Pth1r', 'Runx2', 'Mef2c', 'Sox9', 'Col10a1', 'Mmp13', 'Vegfa'],
    'CNP_axis':       ['Nppc', 'Npr2', 'Npr3', 'Ostn'],
    'FGF_axis':       ['Fgfr3', 'Fgf18', 'Fgfr1'],
    'atlas_leads':    ['Hhip', 'Stc2', 'Pappa', 'Pappa2', 'Chad', 'Scube3', 'Nrk', 'Clec3a', 'Ecrg4',
                       'Adam12', 'Loxl2', 'Plod1', 'Plod2', 'Cxxc5', 'Spin4', 'Tet1'],
}


def load(tag):
    rows = {}
    with open(os.path.join(D, f'saxena_deseq2_{tag}.tsv')) as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            for k in list(r):
                if k not in ('transcript', 'symbol'):
                    r[k] = float(r[k]) if r[k] not in ('', 'None') else None
            rows.setdefault(r['symbol'], []).append(r)
    return rows


def fmt(v, w=7, p=2):
    return f'{v:{w}.{p}f}' if v is not None else ' ' * (w - 1) + '-'


def main():
    n3, n2 = load('n3'), load('n2')

    # --- the genome-wide base rate for the interaction, computed BEFORE any panel
    inter = [abs(r['interaction_MT_minus_RU']) for rs in n3.values() for r in rs
             if r['interaction_MT_minus_RU'] is not None]
    inter.sort()
    q = lambda f: inter[int(f * (len(inter) - 1))]
    print(f'BASE RATE of |interaction| across {len(inter)} orthologues (n=3 cohort):')
    print(f'  median {q(.5):.3f}   p75 {q(.75):.3f}   p90 {q(.90):.3f}   '
          f'p95 {q(.95):.3f}   p99 {q(.99):.3f}   max {inter[-1]:.2f}')
    pct = lambda v: 100.0 * sum(1 for x in inter if x <= abs(v)) / len(inter) if v is not None else None

    def show(title, groups):
        print('\n' + '=' * 108)
        print(title)
        print('=' * 108)
        for name, genes in groups.items():
            print(f'\n--- {name}')
            print(f'{"gene":<10}{"baseMn":>9}{"MT lfc":>9}{"MT padj":>10}'
                  f'{"RU lfc":>9}{"RU padj":>10}{"INTER":>9}{"pct":>6}   {"n=2 INTER":>10}{"sign":>6}')
            for g in genes:
                if g not in n3:
                    print(f'{g:<10}    NOT IN THE 1:1 ORTHOLOGUE SET')
                    continue
                for r in n3[g]:
                    i3 = r['interaction_MT_minus_RU']
                    r2 = n2.get(g, [])
                    i2 = None
                    if r2:
                        m = [x for x in r2 if x['transcript'] == r['transcript']]
                        if m: i2 = m[0]['interaction_MT_minus_RU']
                    agree = ''
                    if i3 is not None and i2 is not None:
                        agree = 'same' if (i3 > 0) == (i2 > 0) else 'OPP'
                    p = pct(i3)
                    print(f'{g:<10}{fmt(r["MT_baseMean"],9,1)}{fmt(r["MT_log2FoldChange"])}'
                          f'{fmt(r["MT_padj"],10,4)}{fmt(r["RU_log2FoldChange"])}{fmt(r["RU_padj"],10,4)}'
                          f'{fmt(i3)}{("" if p is None else f"{p:5.1f}")}   {fmt(i2,10)}{agree:>6}')

    show('CONTROLS - declared before the question panels', CONTROLS)
    show('QUESTION PANELS', PANELS)


if __name__ == '__main__':
    main()
