#!/usr/bin/env python3
"""R356 - the POOL screen. Which genes are RESTING-ZONE-preferential in HUMAN tissue?

WHY THIS EXISTS
---------------
R355 concluded that the PERIOD question is substantially answered (anastrozole +
vepdegestrant cover the hormonal accelerator) and that the residual is N - the
resting-zone pool. Every candidate the atlas holds for N (HHIP, CHAD, SCUBE3,
STC2, CLEC3A, ECRG4, SPIN4) was found by some other route and each lacks a
molecule.

The obvious screen has never been run. GSE9160 is the ONLY zone-resolved
transcriptome of a human growth plate and it separates RESERVE from
proliferative, prehypertrophic and hypertrophic. R302 used it for PRESENCE on
251 hand-picked symbols. Nobody has asked it, genome-wide, "which genes does the
RESTING ZONE run that the rest of the column does not?"

That is the pool-compartment analogue of R347's purity-corrected screen, and it
is free.

DESIGN
------
* Each donor SEPARATELY. n=2 with one female and one male is never a replicate
  pair (CORR-317), and this array's two donors differ 1.75x in present calls.
  A gene counts only if it is RZ-preferential in BOTH.
* Enrichment is RZ vs the CARTILAGE COLUMN ONLY - max(PZ, PHZ, HZ).
  PERICHONDRIUM IS EXCLUDED FROM THE DENOMINATOR. It is a different tissue with
  its own programme (R292: FBN1's only clean-donor detection is there, HHIP is
  0/8 there), and mixing it in makes the contrast about tissue composition
  rather than about position in the column - the CORR-339 failure.
* RZ must clear that array's OWN or_null_p95 background. Thresholds differ
  2.4x between donors, so a single global cutoff would be a donor effect.
* Every probe set is kept separate to the last step (the module docstring of
  gse9160_panel.py: summarising by the maximum hides cross-hybridisation).

PREREGISTERED CONTROLS - written before any result was printed
--------------------------------------------------------------
The negative control is rows you already have (CORR-311). Three panels:

  MUST COME OUT RZ-PREFERENTIAL. If these do not, the contrast is not measuring
  position in the column and the screen is void:
      SFRP5, NT5E (CD73)   lui2023's Spin4 resting-zone progenitor markers
      PTHLH                the resting/periarticular source of the Ihh-PTHrP loop
      GREM1                a resting-zone/skeletal-stem marker
      HHIP                 haraguchi2025 places Hhip1 mRNA in RESTING-ZONE
                           chondrocytes in mouse; R292 found it PZ-detected in
                           human, so this one is a genuine test, not a gimme

  MUST COME OUT HYPERTROPHIC, i.e. must NOT be called RZ-preferential:
      COL10A1, IBSP, MMP13, SPP1, ALPL, MEF2C

  MUST COME OUT NEITHER (flat housekeeping):
      ACTB, GAPDH, RPL13A, PPIA, TUBB
  B2M IS DELIBERATELY OMITTED as a housekeeper. CORR-339 caught it coming out
  98th percentile on a contrast where it was supposed to be flat.

  CONTAMINANT PANEL - the specific thing that could wreck THIS screen.
  The reserve zone abuts the SECONDARY OSSIFICATION CENTRE, so an RZ dissection
  can carry epiphyseal bone and marrow that no other zone carries. If these come
  out RZ-preferential, "RZ-enriched" partly means "closer to the SOC" and every
  hit needs re-reading:
      HBB, HBA1, PTPRC, CD74, LYZ        blood / marrow
      BGLAP, SP7, IBSP, COL1A1, RUNX2    bone / osteoblast
      PECAM1, CDH5, VWF                  vessel
  ACAN and COL2A1 are printed as the cartilage-fraction reference: if they fall
  in RZ, the RZ samples are DILUTED and enrichment values are compressed.

Outputs atlas/data/round356/.
"""
import csv
import gzip
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'quant', 'notebooks', 'p8_01_gse9160_human_zonal', '_data')
OUT = os.path.join(ROOT, 'data', 'round356')

# ---------------------------------------------------------------- preregistered
CTRL_MUST_BE_RZ = ['SFRP5', 'NT5E', 'PTHLH', 'GREM1', 'HHIP']
CTRL_MUST_BE_HZ = ['COL10A1', 'IBSP', 'MMP13', 'SPP1', 'ALPL', 'MEF2C']
CTRL_MUST_BE_FLAT = ['ACTB', 'GAPDH', 'RPL13A', 'PPIA', 'TUBB']
CTRL_CONTAMINANT = ['HBB', 'HBA1', 'PTPRC', 'CD74', 'LYZ',
                    'BGLAP', 'SP7', 'COL1A1', 'RUNX2',
                    'PECAM1', 'CDH5', 'VWF']
CTRL_CARTILAGE = ['ACAN', 'COL2A1', 'COL9A1', 'SOX9']

ENRICH_MIN = 2.0     # RZ / max(PZ,PHZ,HZ)


def load_matrix():
    """Return probe -> {compartment_donor: value} plus per-array thresholds."""
    path = os.path.join(DATA, 'GSE9160_series_matrix.txt')
    order, vals = None, {}
    with open(path) as fh:
        in_table = False
        for line in fh:
            if line.startswith('!series_matrix_table_begin'):
                in_table = True
                continue
            if line.startswith('!series_matrix_table_end'):
                break
            if not in_table:
                continue
            parts = line.rstrip('\n').split('\t')
            if order is None:
                order = [p.strip('"') for p in parts[1:]]
                continue
            probe = parts[0].strip('"')
            try:
                vals[probe] = [float(x) for x in parts[1:]]
            except ValueError:
                continue
    return order, vals


def main():
    os.makedirs(OUT, exist_ok=True)
    gsm_order, vals = load_matrix()
    p2g = json.load(open(os.path.join(DATA, 'probe2gene.json')))

    bg = {}
    with open(os.path.join(ROOT, 'quant', 'notebooks',
                           'p8_01_gse9160_human_zonal', 'results',
                           'array_background.csv')) as fh:
        for row in csv.DictReader(fh):
            bg[row['gsm']] = (row['donor'], row['compartment'],
                              float(row['or_null_p95']))

    idx = {}
    for i, gsm in enumerate(gsm_order):
        donor, comp, thr = bg[gsm]
        idx[(donor, comp)] = (i, thr)

    print('GSE9160 columns resolved:')
    for k in sorted(idx):
        print('   donor %s %-4s  col %d  bg %.1f' % (k[0], k[1], idx[k][0], idx[k][1]))
    print()

    # ------------------------------------------------------ per-probe statistic
    rows = []
    for probe, v in vals.items():
        sym = p2g.get(probe)
        if not sym or '///' in sym:
            continue                      # ambiguous probe sets are not evidence
        rec = {'probe': probe, 'gene': sym}
        ok = True
        for donor in ('1', '2'):
            i_rz, thr_rz = idx[(donor, 'RZ')]
            rz = v[i_rz]
            col = [v[idx[(donor, c)][0]] for c in ('PZ', 'PHZ', 'HZ')]
            other = max(col)
            rec['rz_d%s' % donor] = rz
            rec['maxcol_d%s' % donor] = other
            rec['thr_d%s' % donor] = thr_rz
            rec['enr_d%s' % donor] = rz / max(other, 1.0)
            rec['det_d%s' % donor] = rz > thr_rz
            if not rec['det_d%s' % donor]:
                ok = False
        rec['detected_both'] = ok
        rec['enr_min'] = min(rec['enr_d1'], rec['enr_d2'])
        rows.append(rec)

    print('probe sets with an unambiguous gene symbol: %d' % len(rows))

    # ------------------------------------------------------------- CONTROL PANEL
    bysym = {}
    for r in rows:
        bysym.setdefault(r['gene'], []).append(r)

    def report(panel, label):
        print('\n--- %s ---' % label)
        out = []
        for g in panel:
            rs = bysym.get(g)
            if not rs:
                print('  %-8s NOT ON PLATFORM' % g)
                out.append({'gene': g, 'status': 'not_on_platform'})
                continue
            best = max(rs, key=lambda r: r['enr_min'])
            n_pass = sum(1 for r in rs
                         if r['detected_both'] and r['enr_min'] >= ENRICH_MIN)
            verdict = 'RZ-PREF' if n_pass else (
                'detected, not RZ' if best['detected_both'] else 'below background')
            print('  %-8s %d probes | best enr d1 %6.2f d2 %6.2f | '
                  'RZ d1 %8.0f d2 %8.0f | %s'
                  % (g, len(rs), best['enr_d1'], best['enr_d2'],
                     best['rz_d1'], best['rz_d2'], verdict))
            out.append({'gene': g, 'n_probes': len(rs), 'n_probes_rz_pref': n_pass,
                        'best_enr_d1': round(best['enr_d1'], 3),
                        'best_enr_d2': round(best['enr_d2'], 3),
                        'rz_d1': best['rz_d1'], 'rz_d2': best['rz_d2'],
                        'verdict': verdict})
        return out

    controls = {
        'must_be_rz': report(CTRL_MUST_BE_RZ, 'PREREG: MUST BE RZ-PREFERENTIAL'),
        'must_be_hz': report(CTRL_MUST_BE_HZ, 'PREREG: MUST NOT BE RZ (hypertrophic)'),
        'must_be_flat': report(CTRL_MUST_BE_FLAT, 'PREREG: MUST BE FLAT (housekeeping)'),
        'contaminant': report(CTRL_CONTAMINANT, 'PREREG: CONTAMINANT PANEL (SOC bone/marrow/vessel)'),
        'cartilage': report(CTRL_CARTILAGE, 'PREREG: CARTILAGE FRACTION REFERENCE'),
    }

    # ------------------------------------------------------------------- the hits
    hits = [r for r in rows if r['detected_both'] and r['enr_min'] >= ENRICH_MIN]
    hits.sort(key=lambda r: -r['enr_min'])
    genes = {}
    for r in hits:
        g = r['gene']
        if g not in genes or r['enr_min'] > genes[g]['enr_min']:
            genes[g] = r

    print('\n=== RZ-PREFERENTIAL IN BOTH DONORS (enr >= %.1f, RZ above background '
          'in both) ===' % ENRICH_MIN)
    print('probe sets: %d   distinct genes: %d' % (len(hits), len(genes)))

    # base rate: how many genes clear detection at all, so the hit fraction is
    # placeable (CORR-329 - a count means nothing without its denominator)
    detected = {}
    for r in rows:
        if r['detected_both']:
            g = r['gene']
            if g not in detected or r['enr_min'] > detected[g]['enr_min']:
                detected[g] = r
    print('BASE RATE: %d genes detected in RZ above background in BOTH donors; '
          '%d of them (%.1f%%) are RZ-preferential.'
          % (len(detected), len(genes), 100.0 * len(genes) / max(len(detected), 1)))

    json.dump({'controls': controls,
               'n_probes_scored': len(rows),
               'n_genes_detected_both': len(detected),
               'n_genes_rz_preferential': len(genes),
               'enrich_min': ENRICH_MIN},
              open(os.path.join(OUT, 'controls_and_base_rate.json'), 'w'), indent=1)

    with open(os.path.join(OUT, 'rz_preferential_genes.tsv'), 'w') as fh:
        w = csv.writer(fh, delimiter='\t')
        w.writerow(['gene', 'probe', 'enr_d1', 'enr_d2', 'enr_min',
                    'rz_d1', 'maxcol_d1', 'rz_d2', 'maxcol_d2'])
        for g, r in sorted(genes.items(), key=lambda kv: -kv[1]['enr_min']):
            w.writerow([g, r['probe'], round(r['enr_d1'], 3), round(r['enr_d2'], 3),
                        round(r['enr_min'], 3), r['rz_d1'], r['maxcol_d1'],
                        r['rz_d2'], r['maxcol_d2']])

    print('\ntop 40 by minimum-across-donors enrichment:')
    for g, r in list(sorted(genes.items(), key=lambda kv: -kv[1]['enr_min']))[:40]:
        print('  %-12s enr d1 %6.2f  d2 %6.2f   RZ %8.0f / %8.0f'
              % (g, r['enr_d1'], r['enr_d2'], r['rz_d1'], r['rz_d2']))

    print('\nwrote %s' % OUT)


if __name__ == '__main__':
    main()
