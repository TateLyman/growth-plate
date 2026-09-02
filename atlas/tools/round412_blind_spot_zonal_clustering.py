#!/usr/bin/env python3
"""
R412 - CLUSTER THE BLIND SPOTS BY ZONAL SHAPE. A gene closes; a PROGRAMME does not.

R411 produced 1,492 genes that are cartilage-enriched and abundant in the human growth
plate and have never been mentioned anywhere in this atlas. A flat list of 1,492 is not
usable, and R411's own negative control shows a large fraction of it is mitochondrial and
ribosomal housekeeping. The way to separate a programme from a housekeeping artefact is
that a programme has a SHAPE: it turns on, or off, at a particular point along the column.

So this takes the R411 blind-spot list and asks GSE9160 - the only zone-resolved human
growth plate - what shape each gene has, and keeps only shapes that REPLICATE IN BOTH
DONORS. Housekeeping is flat and drops out by construction.

DESIGN CHOICES, EACH MADE FOR A RECORDED REASON
  · PERICHONDRIUM IS EXCLUDED from the shape. It is a different tissue and CORR-339 is
    the standing instruction not to mix tissue composition into a cell-state contrast.
  · A DETECTION FLOOR of 300 on the MAS5 linear scale, which is well above this array's
    own floor calibrator (NPPC runs 4-20 across all ten samples).
  · ONE PROBE SET PER GENE, chosen as the highest-signal one, and the probe id is
    reported so the choice is auditable.
  · BOTH DONORS MUST AGREE IN DIRECTION at >= 1.5-fold. This is the only replication
    available and it is weak: n = 2, and CORR-317 says a female and a male are never a
    replicate pair. It is weaker for ABSOLUTE level than for SHAPE, because each donor is
    its own baseline, but it is not nothing and the claim grade reflects it.

READ THE OUTPUT AS: three programmes, defined by where they switch.
  HZ_RISING   - on in the hypertrophic zone. This is where h_term is made.
  RZ_FALLING  - on in the reserve zone and off downstream. This is the pool compartment.
  MID_PEAK    - on in the proliferative/prehypertrophic zones and off at both ends.
"""
import json, os, pickle
import numpy as np

INV = 'atlas/data/round411/blind_spot_inventory.json'
NB = 'atlas/quant/notebooks/p8_01_gse9160_human_zonal/_data'
OUT = 'atlas/data/round412/blind_spot_zonal_programmes.json'

# GSE9160 column order is HZ, PHZ, PZ, RZ, PC for donor 1 then donor 2.
# Reordered to RZ, PZ, PHZ, HZ; perichondrium dropped.
ZI = [3, 2, 1, 0]
ZONES = ['RZ', 'PZ', 'PHZ', 'HZ']
FLOOR = 300.0
FOLD = 0.585  # log2(1.5)


def load_array():
    p2g = json.load(open(f'{NB}/probe2gene.json'))
    g2p = {}
    for p, g in p2g.items():
        if g:
            g2p.setdefault(str(g).upper(), []).append(p)
    rows, seen_header = {}, False
    on = False
    for line in open(f'{NB}/GSE9160_series_matrix.txt'):
        if line.startswith('!series_matrix_table_begin'):
            on = True
            continue
        if line.startswith('!series_matrix_table_end'):
            break
        if not on:
            continue
        f = line.rstrip('\n').split('\t')
        if not seen_header:
            seen_header = True
            continue
        try:
            rows[f[0].strip('"')] = np.array([float(x) for x in f[1:]])
        except ValueError:
            pass
    return g2p, rows


def classify(d1, d2):
    r1 = np.log2((d1[3] + 50) / (d1[0] + 50))
    r2 = np.log2((d2[3] + 50) / (d2[0] + 50))
    if r1 > FOLD and r2 > FOLD:
        return 'HZ_RISING', float((r1 + r2) / 2)
    if r1 < -FOLD and r2 < -FOLD:
        return 'RZ_FALLING', float((r1 + r2) / 2)
    m1, m2 = int(np.argmax(d1)), int(np.argmax(d2))
    if m1 == m2 and m1 in (1, 2) \
       and min(d1[m1] / max(d1[0], 1), d2[m2] / max(d2[0], 1)) > 1.5 \
       and min(d1[m1] / max(d1[3], 1), d2[m2] / max(d2[3], 1)) > 1.5:
        return 'MID_PEAK', 0.0
    return None, 0.0


def main():
    inv = json.load(open(INV))
    meta = {d['symbol']: d for d in inv['genes']}
    blind = [d['symbol'] for d in inv['genes'] if d['atlas_mentions'] == 0]
    g2p, rows = load_array()

    groups = {'HZ_RISING': [], 'RZ_FALLING': [], 'MID_PEAK': []}
    n_prof = 0
    for g in blind:
        best = None
        for p in g2p.get(g, []):
            v = rows.get(p)
            if v is None:
                continue
            d1, d2 = v[0:5][ZI], v[5:10][ZI]
            if max(d1.max(), d2.max()) < FLOOR:
                continue
            sig = d1.mean() + d2.mean()
            if best is None or sig > best[0]:
                best = (sig, p, d1, d2)
        if best is None:
            continue
        n_prof += 1
        _, probe, d1, d2 = best
        c, sc = classify(d1, d2)
        if c:
            groups[c].append({'symbol': g, 'log2_HZ_over_RZ': round(sc, 2),
                              'pure_cpm': meta[g]['pure_cpm'],
                              'enrichment_ratio': meta[g]['enrichment_ratio'],
                              'probe': probe,
                              'donor1': {ZONES[i]: round(float(d1[i])) for i in range(4)},
                              'donor2': {ZONES[i]: round(float(d2[i])) for i in range(4)}})

    for k in groups:
        groups[k].sort(key=(lambda d: -abs(d['log2_HZ_over_RZ'])) if k != 'MID_PEAK'
                       else (lambda d: -d['pure_cpm']))

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump({'method': __doc__.strip(),
               'n_blind_spot_genes': len(blind),
               'n_with_usable_profile': n_prof,
               'counts': {k: len(v) for k, v in groups.items()},
               'programmes': groups}, open(OUT, 'w'), indent=1)

    print(f"blind-spot genes {len(blind)}, usable GSE9160 profile {n_prof}")
    print("replicated in BOTH donors:", {k: len(v) for k, v in groups.items()})
    for k in ('HZ_RISING', 'RZ_FALLING', 'MID_PEAK'):
        print(f"\n===== {k} =====")
        for d in groups[k][:30]:
            z = ' '.join(f"{n}{d['donor1'][n]:>6}" for n in ZONES)
            print(f"  {d['symbol']:<12}log2 {d['log2_HZ_over_RZ']:+5.2f} "
                  f"{d['pure_cpm']:>7.0f}CPM {d['enrichment_ratio']:>6.1f}x  D1 {z}")
    print(f"\nwrote {OUT}")


if __name__ == '__main__':
    main()
