#!/usr/bin/env python3
"""
R488 - IS THE chr6 HEIGHT SIGNAL ATTRIBUTABLE TO SCUBE3, AND WHICH WAY DOES RAISING IT RUN?

R406 gave SCUBE3 29.5% TRUNK from the region's standing-height lead at chr6:35,313,194, and
flagged in its own caveat that the lead sits ~90 kb out in gene-dense chr6p21.  R477/R479 then
showed on ADAM12 that a region lead can belong entirely to a neighbouring gene while the gene of
interest carries an independent and far weaker eQTL - so a region coordinate is not a gene
coordinate until the attribution is checked.

Method is R477's, unchanged: take EVERY GTEx v8 significant single-tissue cis-eQTL for the gene,
align each variant to its GENE-RAISING allele using the NES sign (NES is per ALT relative to REF),
then read the height beta out of the three ABSOLUTE traits in one cohort of 451,921 Europeans.

  GCST90728584 standing height   GCST90728586 sitting height   GCST90728587 leg length

Coordinates: GTEx v8 is GRCh38; the sumstats base_pair_location is GRCh38 and the position inside
variant_id is GRCh37.  Matching is on GRCh38 position plus the allele pair, orientation-agnostic.
"""
import os, sys, json, collections

SP = ('/tmp/claude-0/-home-user-growth-plate/'
      'ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad')
sys.path.insert(0, SP)
import tbifetch  # noqa: E402

BASE = ('https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/'
        'GCST90728001-GCST90729000/{acc}/harmonised/{acc}.h.tsv.gz')
FILES = {'std': 'GCST90728584', 'sit': 'GCST90728586', 'leg': 'GCST90728587'}

CHROM, BEG, END = '6', 34_900_000, 35_500_000   # GRCh38, gene 35,214,419-35,253,079


def pull(acc):
    _, linear, _ = tbifetch.read_tbi(os.path.join(SP, acc + '.tbi'))
    ch = CHROM if CHROM in linear else ('chr' + CHROM)
    rows = tbifetch.region(BASE.format(acc=acc), linear, ch, BEG, END, span=6_000_000)
    out = {}
    for line in rows:
        f = line.split('\t')
        try:
            pos = int(f[1]); beta = float(f[4]); se = float(f[5]); p = float(f[7])
        except (ValueError, IndexError):
            continue
        out[(pos, f[2].upper(), f[3].upper())] = (beta, se, p)
    return out


def look(tab, pos, ref, alt):
    """Return (beta_per_ALT, se, p) or None. Sumstats col2=EA, col3=OA."""
    r = tab.get((pos, alt, ref))
    if r is not None:
        return r
    r = tab.get((pos, ref, alt))
    if r is not None:
        return (-r[0], r[1], r[2])
    return None


def main():
    eq = json.load(open('/tmp/e1.json'))['data']
    # best (smallest p) eQTL record per variant, and which tissue it came from
    best = {}
    for e in eq:
        vid = e['variantId']
        if vid not in best or e['pValue'] < best[vid]['pValue']:
            best[vid] = e
    print('SCUBE3 GTEx v8 significant cis-eQTL variants: %d (from %d variant-tissue pairs)'
          % (len(best), len(eq)), file=sys.stderr)

    tab = {k: pull(a) for k, a in FILES.items()}
    for k in tab:
        print('%s: %d sumstat rows in window' % (k, len(tab[k])), file=sys.stderr)

    rows = []
    for vid, e in best.items():
        p = vid.split('_')
        if len(p) < 5:
            continue
        pos, ref, alt = int(p[1]), p[2].upper(), p[3].upper()
        nes = e['nes']
        raising = alt if nes > 0 else ref
        flip = 1.0 if nes > 0 else -1.0     # beta per ALT -> beta per raising allele
        rec = {'variant': vid, 'rsid': e.get('snpId'), 'pos': pos,
               'eqtl_p': e['pValue'], 'nes': nes, 'tissue': e['tissueSiteDetailId'],
               'raising_allele': raising}
        ok = True
        for k in ('std', 'sit', 'leg'):
            r = look(tab[k], pos, ref, alt)
            if r is None:
                ok = False
                break
            rec[k] = {'beta': r[0] * flip, 'se': r[1], 'p': r[2]}
        if ok:
            rows.append(rec)

    print('\nmatched into all three traits: %d of %d' % (len(rows), len(best)))

    def summarise(sel, label):
        if not sel:
            print('  %-34s n=0' % label)
            return
        tall = sum(1 for r in sel if r['std']['beta'] > 0)
        print('  %-34s n=%-4d  raising-allele TALLER %d / SHORTER %d'
              % (label, len(sel), tall, len(sel) - tall))

    print('\nDIRECTION, aligned to the SCUBE3-RAISING allele')
    summarise(rows, 'all matched eQTL variants')
    for thr in (1e-4, 1e-6, 1e-8, 1e-10):
        summarise([r for r in rows if r['eqtl_p'] < thr], 'eQTL p < %g' % thr)
    gws = [r for r in rows if r['std']['p'] < 5e-8]
    summarise(gws, 'and genome-wide sig for height')

    strong = sorted([r for r in rows if r['eqtl_p'] < 1e-8],
                    key=lambda r: r['std']['p'])[:12]
    print('\nSTRONGEST eQTL VARIANTS (eQTL p<1e-8), ranked by standing-height P')
    print('%-26s %-12s %-10s %6s  %-28s %10s %9s %10s %9s %10s %9s %7s'
          % ('variant', 'rsid', 'eQTL p', 'NES', 'tissue', 'std beta', 'std P',
             'sit beta', 'sit P', 'leg beta', 'leg P', '%trunk'))
    for r in strong:
        s, l = r['sit']['beta'], r['leg']['beta']
        pt = (100.0 * s / (s + l)) if (s + l) != 0 else float('nan')
        print('%-26s %-12s %-10.2e %+6.3f  %-28s %+10.6f %9.2e %+9.6f %9.2e %+9.6f %9.2e %7.1f'
              % (r['variant'], r['rsid'] or '-', r['eqtl_p'], r['nes'],
                 r['tissue'][:28], r['std']['beta'], r['std']['p'],
                 s, r['sit']['p'], l, r['leg']['p'], pt))

    # tissue census for the strongest tier
    tis = collections.Counter(r['tissue'] for r in rows if r['eqtl_p'] < 1e-8)
    print('\ntissues carrying the strongest eQTLs:', dict(tis.most_common(8)))

    out = '/home/user/growth-plate/atlas/data/round488'
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'scube3_eqtl_direction.json'), 'w') as fh:
        json.dump(rows, fh, indent=1)
    print('\nwrote', os.path.join(out, 'scube3_eqtl_direction.json'))


if __name__ == '__main__':
    main()
