#!/usr/bin/env python3
"""
R488 - GENERALISED eQTL-SIGNED DIRECTION AND COMPARTMENT, R477/R479's INSTRUMENT.

For any gene: take every GTEx v8 significant single-tissue cis-eQTL, align each variant to its
GENE-RAISING allele using the NES sign (NES is per ALT relative to REF), and read the beta out of
the three ABSOLUTE height traits measured in one cohort of 451,921 Europeans.

  GCST90728584 standing height   GCST90728586 sitting height   GCST90728587 leg length

Then run the gene-specificity check R479 showed is obligatory: at the variants where the gene leads,
how far does it lead, and at the region's strongest HEIGHT variants, is the gene the top eQTL gene
at all?  A region coordinate is not a gene coordinate until that is answered.

Usage:  round488_eqtl_signed_compartment.py <SYMBOL> <GENCODE_ID> <CHR> <START> <END>
"""
import os, sys, json, collections, subprocess

SP = ('/tmp/claude-0/-home-user-growth-plate/'
      'ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad')
sys.path.insert(0, SP)
import tbifetch  # noqa: E402

BASE = ('https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/'
        'GCST90728001-GCST90729000/{acc}/harmonised/{acc}.h.tsv.gz')
FILES = {'std': 'GCST90728584', 'sit': 'GCST90728586', 'leg': 'GCST90728587'}
CA = '/root/.ccr/ca-bundle.crt'
GTEX = 'https://gtexportal.org/api/v2/association/singleTissueEqtl'


def api(url):
    return json.loads(subprocess.check_output(
        ['curl', '-sS', '--cacert', CA, url]).decode())


def pull(acc, chrom, beg, end):
    _, linear, _ = tbifetch.read_tbi(os.path.join(SP, acc + '.tbi'))
    ch = chrom if chrom in linear else ('chr' + chrom)
    out = {}
    for line in tbifetch.region(BASE.format(acc=acc), linear, ch, beg, end, span=6_000_000):
        f = line.split('\t')
        try:
            pos = int(f[1]); beta = float(f[4]); se = float(f[5]); p = float(f[7])
        except (ValueError, IndexError):
            continue
        out[(pos, f[2].upper(), f[3].upper())] = (beta, se, p)
    return out


def look(tab, pos, ref, alt):
    r = tab.get((pos, alt, ref))
    if r is not None:
        return r
    r = tab.get((pos, ref, alt))
    return (-r[0], r[1], r[2]) if r is not None else None


def main():
    sym, gid, chrom, gs, ge = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
    beg, end = gs - 300_000, ge + 300_000

    eq = api('%s?gencodeId=%s&datasetId=gtex_v8&itemsPerPage=5000&format=json' % (GTEX, gid))['data']
    best = {}
    for e in eq:
        v = e['variantId']
        if v not in best or e['pValue'] < best[v]['pValue']:
            best[v] = e
    tab = {k: pull(a, chrom, beg, end) for k, a in FILES.items()}

    rows = []
    for vid, e in best.items():
        p = vid.split('_')
        if len(p) < 5:
            continue
        pos, ref, alt = int(p[1]), p[2].upper(), p[3].upper()
        flip = 1.0 if e['nes'] > 0 else -1.0
        rec = {'variant': vid, 'rsid': e.get('snpId'), 'pos': pos, 'eqtl_p': e['pValue'],
               'nes': e['nes'], 'tissue': e['tissueSiteDetailId'],
               'raising_allele': alt if e['nes'] > 0 else ref}
        ok = True
        for k in ('std', 'sit', 'leg'):
            r = look(tab[k], pos, ref, alt)
            if r is None:
                ok = False; break
            rec[k] = {'beta': r[0] * flip, 'se': r[1], 'p': r[2]}
        if ok:
            rows.append(rec)

    print('=' * 96)
    print('%s (%s)  chr%s:%d-%d  %d eQTL variants, %d matched into all three traits'
          % (sym, gid, chrom, gs, ge, len(best), len(rows)))
    print('=' * 96)
    if not rows:
        return

    tall = sum(1 for r in rows if r['std']['beta'] > 0)
    print('DIRECTION, aligned to the %s-RAISING allele: TALLER %d / SHORTER %d  (%.1f%%)'
          % (sym, tall, len(rows) - tall, 100.0 * tall / len(rows)))
    for thr in (1e-4, 1e-8):
        s = [r for r in rows if r['eqtl_p'] < thr]
        if s:
            t = sum(1 for r in s if r['std']['beta'] > 0)
            print('  eQTL p<%-6g n=%-4d TALLER %d / SHORTER %d' % (thr, len(s), t, len(s) - t))
    print('  NOTE: LD-correlated, NOT independent tests.')

    # (a) variants where the gene is most specifically implicated
    tops = sorted(rows, key=lambda r: r['eqtl_p'])[:4]
    # (b) variants with the strongest height signal
    hgt = sorted(rows, key=lambda r: r['std']['p'])[:3]
    seen = set()
    print('\nGENE-SPECIFICITY (R479) - top eQTL gene at each variant, and where %s ranks' % sym)
    for tag, sel in (('STRONGEST eQTL', tops), ('STRONGEST HEIGHT', hgt)):
        for r in sel:
            if r['variant'] in seen:
                continue
            seen.add(r['variant'])
            d = api('%s?variantId=%s&datasetId=gtex_v8&itemsPerPage=2000&format=json'
                    % (GTEX, r['variant']))['data']
            gb = {}
            for e in d:
                g = e['geneSymbol']
                if g not in gb or e['pValue'] < gb[g]['pValue']:
                    gb[g] = e
            order = sorted(gb.items(), key=lambda kv: kv[1]['pValue'])
            rank = [i for i, (g, _) in enumerate(order, 1) if g == sym]
            s, l = r['sit']['beta'], r['leg']['beta']
            pt = 100.0 * s / (s + l) if (s + l) else float('nan')
            print('\n  [%s] %s %s  eQTL p=%.2e NES %+0.3f  %s'
                  % (tag, r['variant'], r['rsid'] or '-', r['eqtl_p'], r['nes'], r['tissue'][:30]))
            print('      std %+0.6f P=%.2e | sit %+0.6f P=%.2e | leg %+0.6f P=%.2e | %%trunk %.1f'
                  % (r['std']['beta'], r['std']['p'], s, r['sit']['p'], l, r['leg']['p'], pt))
            print('      %s ranks %s of %d genes:' % (sym, rank[0] if rank else '?', len(order)),
                  ', '.join('%s %.1e' % (g, e['pValue']) for g, e in order[:5]))

    tis = collections.Counter(r['tissue'] for r in rows if r['eqtl_p'] < 1e-6)
    print('\ntissues at eQTL p<1e-6:', dict(tis.most_common(6)))

    out = '/home/user/growth-plate/atlas/data/round488'
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, '%s_eqtl_direction.json' % sym.lower()), 'w') as fh:
        json.dump(rows, fh, indent=1)
    print('\nwrote %s/%s_eqtl_direction.json' % (out, sym.lower()))


if __name__ == '__main__':
    main()
