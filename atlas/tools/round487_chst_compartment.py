#!/usr/bin/env python3
"""
R487 - IS THERE A HUMAN COMMON-VARIANT HEIGHT SIGNAL AT CHST3 OR CHST11?

GWAS Catalog's gene-association endpoint returns ZERO for both genes, and neither is in
kosmicki2026's 207 (that instrument is a HETEROZYGOUS burden test and both human CHST
diseases are RECESSIVE, so their absence there is a design artefact - CORR-358).

This asks the sumstats directly, on the three ABSOLUTE traits in one cohort of 451,921
Europeans, using R323/R406's corrected method: take the region's STANDING-HEIGHT lead,
read the same variant out of sitting height and leg length, align to the height-INCREASING
allele.

  GCST90728584 standing height   GCST90728586 sitting height   GCST90728587 leg length

Coordinates are GRCh38 (base_pair_location); the position inside variant_id is GRCh37.
"""
import os, sys, json

SP = ('/tmp/claude-0/-home-user-growth-plate/'
      'ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad')
sys.path.insert(0, SP)
import tbifetch  # noqa: E402

BASE = ('https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/'
        'GCST90728001-GCST90729000/{acc}/harmonised/{acc}.h.tsv.gz')
FILES = {'std': 'GCST90728584', 'sit': 'GCST90728586', 'leg': 'GCST90728587'}

WIN = 150_000
GENES = {
    'CHST3':  ('10', 71963538, 72019147),
    'CHST11': ('12', 104455295, 104762014),
}


def pull(acc, chrom, beg, end):
    names, linear, _ = tbifetch.read_tbi(os.path.join(SP, acc + '.tbi'))
    url = BASE.format(acc=acc)
    ch = chrom if chrom in linear else ('chr' + chrom)
    rows = tbifetch.region(url, linear, ch, beg, end, span=6_000_000)
    # harmonised column order: chrom0 pos1 EA2 OA3 beta4 se5 eaf6 p7 variant_id8
    out = {}
    for line in rows:
        f = line.split('\t')
        try:
            pos = int(f[1]); beta = float(f[4]); se = float(f[5]); p = float(f[7])
        except (ValueError, IndexError):
            continue
        vid = f[8] if len(f) > 8 else '%s_%d' % (chrom, pos)
        out[vid] = (chrom, pos, f[2], f[3], beta, se, p)
    return out


def main():
    res = {}
    for gene, (chrom, gs, ge) in GENES.items():
        beg, end = gs - WIN, ge + WIN
        tab = {}
        for k, acc in FILES.items():
            tab[k] = pull(acc, chrom, beg, end)
            print('%-6s %-4s %s: %d variants' % (gene, k, acc, len(tab[k])), file=sys.stderr)
        if not tab['std']:
            print('%s: NO VARIANTS RETURNED' % gene)
            continue
        lead_id, lead = min(tab['std'].items(), key=lambda kv: kv[1][6])
        c, pos, ea, oa, b, se, p = lead
        flip = -1.0 if b < 0 else 1.0
        inc = oa if b < 0 else ea
        row = {'gene': gene, 'lead': lead_id, 'chrom': c, 'pos_grch38': pos,
               'increasing_allele': inc, 'n_variants': len(tab['std'])}
        for k in ('std', 'sit', 'leg'):
            r = tab[k].get(lead_id)
            if r is None:
                row[k] = None
                continue
            row[k] = {'beta': r[4] * flip, 'se': r[5], 'p': r[6]}
        if row.get('sit') and row.get('leg'):
            s, l = row['sit']['beta'], row['leg']['beta']
            row['pct_trunk'] = 100.0 * s / (s + l) if (s + l) != 0 else None
        # genome-wide significant count in window
        row['n_gws'] = sum(1 for v in tab['std'].values() if v[6] < 5e-8)
        row['min_p'] = min(v[6] for v in tab['std'].values())
        res[gene] = row

    print('=' * 92)
    print('R487  CHST3 / CHST11 COMMON-VARIANT HEIGHT SIGNAL, THREE ABSOLUTE TRAITS')
    print('      GWAS Catalog harmonised sumstats, 451,921 Europeans, +/-150 kb window')
    print('=' * 92)
    for gene, r in res.items():
        print()
        print('%s  window %s:%d-%d  n=%d variants  min P=%.3g  n(P<5e-8)=%d'
              % (gene, r['chrom'], GENES[gene][1] - WIN, GENES[gene][2] + WIN,
                 r['n_variants'], r['min_p'], r['n_gws']))
        print('  standing-height lead %s at chr%s:%d, height-increasing allele %s'
              % (r['lead'], r['chrom'], r['pos_grch38'], r['increasing_allele']))
        for k, lab in (('std', 'standing height'), ('sit', 'sitting height'),
                       ('leg', 'leg length')):
            v = r[k]
            if v is None:
                print('    %-16s NOT PRESENT in that file' % lab)
            else:
                print('    %-16s beta %+.6f  SE %.6f  P %.3g' % (lab, v['beta'], v['se'], v['p']))
        if r.get('pct_trunk') is not None:
            print('    %% TRUNK           %.1f%%' % r['pct_trunk'])

    out = '/home/user/growth-plate/atlas/data/round487'
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'chst_compartment.json'), 'w') as fh:
        json.dump(res, fh, indent=2)
    print('\nwrote', os.path.join(out, 'chst_compartment.json'))


if __name__ == '__main__':
    main()
