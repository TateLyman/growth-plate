"""R477 - turn anonymous ADAM12 height GWAS signals into a SIGNED gene direction.

Method: for every GTEx v8 cis variant tested against ADAM12, align the height beta to
the ADAM12-RAISING allele using the eQTL NES (NES is the effect of ALT relative to REF),
then read standing / sitting / leg from the three absolute-trait sumstats of one cohort.

Inputs (streamed separately, see atlas/tools/tbifetch.py):
  ADAM12.std.tsv / .sit.tsv / .leg.tsv  - GCST90728584 / 86 / 87 harmonised, ADAM12 +/-150 kb
  adam12_metasoft.json  - curl 'https://gtexportal.org/api/v2/association/metasoft?
                          gencodeId=ENSG00000148848.14&itemsPerPage=600'

CRITICAL: the crude pooled aggregate over all variant-tissue pairs is an ARTEFACT.
The region carries two independent regulatory signals 208 kb apart and only one of them
is an ADAM12 eQTL. Always run the per-variant gene-specificity check:
  curl 'https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=<vid>'
"""
import json, sys

def load(path):
    d = {}
    for line in open(path):
        t = line.rstrip('\n').split('\t')
        try:
            d.setdefault(int(t[1]), []).append(
                dict(ea=t[2], oa=t[3], beta=float(t[4]), se=float(t[5]),
                     eaf=float(t[6]), p=float(t[7]), rsid=t[9]))
        except (ValueError, IndexError):
            continue
    return d

def beta_per_alt(d, pos, ref, alt):
    for c in d.get(pos, []):
        if {c['ea'], c['oa']} == {ref, alt}:
            return (c['beta'] if c['ea'] == alt else -c['beta']), c['se'], c['p'], c['rsid'], c['eaf']
    return None

def main(std, sit, leg, metasoft, tissue='Cells_Cultured_fibroblasts', eqtl_p=1e-8):
    S, T, L = load(std), load(sit), load(leg)
    g = json.load(open(metasoft))['data']
    out = []
    for rec in g:
        v = rec['tissues'].get(tissue)
        if not v or v.get('pValue') is None or v['pValue'] >= eqtl_p:
            continue
        p = rec['variantId'].split('_')
        pos, ref, alt = int(p[1]), p[2], p[3]
        h = beta_per_alt(S, pos, ref, alt)
        if not h:
            continue
        s = beta_per_alt(T, pos, ref, alt)
        l = beta_per_alt(L, pos, ref, alt)
        sgn = 1 if v['nes'] > 0 else -1          # height beta PER ADAM12-RAISING allele
        out.append(dict(variant_id=rec['variantId'], rsid=h[3], pos=pos,
                        raising_allele=(alt if v['nes'] > 0 else ref),
                        eqtl_nes=v['nes'], eqtl_p=v['pValue'], metaP=rec['metaP'],
                        eaf_raising=(h[4] if v['nes'] > 0 else 1 - h[4]),
                        standing_beta=h[0]*sgn, standing_p=h[2],
                        sitting_beta=(s[0]*sgn if s else None), sitting_p=(s[2] if s else None),
                        leg_beta=(l[0]*sgn if l else None), leg_p=(l[2] if l else None)))
    return sorted(out, key=lambda r: r['eqtl_p'])

if __name__ == '__main__':
    rows = main(*sys.argv[1:5]) if len(sys.argv) > 4 else main(
        'ADAM12.std.tsv', 'ADAM12.sit.tsv', 'ADAM12.leg.tsv', 'adam12_metasoft.json')
    tall = sum(1 for r in rows if r['standing_beta'] > 0)
    print(f"n={len(rows)}  ADAM12-raising allele TALLER {tall}  SHORTER {len(rows)-tall}")
    print(json.dumps(rows, indent=1))
