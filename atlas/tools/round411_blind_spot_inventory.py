#!/usr/bin/env python3
"""
R411 - THE INVERSE SEARCH. Not "which gene is good" but "what is this tissue spending
itself on that the atlas has never said one word about".

WHY THIS EXISTS. Every search this file has ever run starts from a GENE (a burden effect,
an IMPC row), a DRUG (Open Targets, ChEMBL, a vendor catalogue) or a PAPER (Europe PMC).
None of those can find a missing MODULE, because a module is only missing relative to the
atlas's own coverage, and coverage was never computed. R408 found the cell-volume module
by accident - it had never been localised in ~400 rounds. This asks the question that
would have found it on purpose.

METHOD
  1. purity-corrected enrichment on GSE288028, but SEX-CORRECTED (see below)
  2. keep genes at or above the ACAN benchmark on that split, >=20 CPM, detected 12/12
  3. count word-boundary mentions of each symbol across every node yaml, gaps.yaml and
     CLAUDE.md
  4. the zero-mention rows are the inventory

THE SEX CORRECTION, WHICH IS THE MOST IMPORTANT THING HERE. Running this genome-wide
immediately returned RPS4Y1 at 3442x, UTY at 213x, USP9Y at 199x and PRKY at 29x - all
Y-linked. XIST shows the 12 samples are 9 male and 3 female, and ALL THREE FEMALES SIT IN
THE CONTAMINATED HALF. So the purity ratio used since R344 is confounded with sex, and
any sex-linked gene reads as spuriously enriched. The fix is to compute the split within
the 9 males only.

That reduces the contamination contrast, so the ratios compress and the THRESHOLD MUST BE
RECALIBRATED rather than carried over: on the male-only split COL2A1 is 7.65 and ACAN is
1.96, so 1.96 - not 2.0 as an absolute - is the cartilage benchmark.

READ THE OUTPUT AS: a high-abundance, cartilage-enriched gene with zero atlas mentions is
a COVERAGE gap, not a lever. A large fraction of the list is mitochondrial oxidative
phosphorylation and ribosomal protein - NDUFA4, NDUFB3, COX8A, UQCRQ, MRPL17, RPL10A and
so on - which is a composition artefact of contrasting cartilage against blood, and is the
negative control this screen needs. What is worth reading is the CLUSTERS that are neither
housekeeping nor already known.
"""
import json, os, re, collections
import numpy as np

CPM = 'atlas/data/round344/gse288028_human12_cpm.npy'
GEN = 'atlas/data/round344/gse288028_gene_names.json'
PUR = 'atlas/data/round344/gse288028_purity_corrected.json'
OUT = 'atlas/data/round411/blind_spot_inventory.json'


def load():
    cpm = np.load(CPM)
    genes = json.load(open(GEN))
    meta = json.load(open(PUR))
    if isinstance(genes, dict):
        genes = genes.get('genes', genes.get('gene_names'))
    genes = [str(g).upper() for g in genes]
    col = meta['col2a1_by_sample']
    vals = np.array([col[k] for k in col] if isinstance(col, dict) else list(col), float)
    return cpm, genes, {g: i for i, g in enumerate(genes)}, vals


def male_only_split(cpm, idx, vals):
    """All three female samples fall in the contaminated half, so split within males."""
    xist = cpm[:, idx['XIST']]
    male = [i for i in range(cpm.shape[0]) if xist[i] < 10]
    ordered = sorted(male, key=lambda i: -vals[i])
    return ordered[:4], ordered[-4:], male


def atlas_mention_counts(symbols):
    """One pass over the whole graph, then a dict lookup per symbol."""
    parts = []
    for root, _, files in os.walk('atlas/nodes'):
        for f in files:
            if f.endswith('.yaml'):
                parts.append(open(os.path.join(root, f), errors='ignore').read())
    for extra in ('atlas/gaps.yaml', 'CLAUDE.md'):
        if os.path.exists(extra):
            parts.append(open(extra, errors='ignore').read())
    blob = '\n'.join(parts).upper()
    tok = collections.Counter(re.findall(r'[A-Z0-9]+(?:-[A-Z0-9]+)*', blob))
    return {s: tok.get(s, 0) for s in symbols}


def main():
    cpm, genes, idx, vals = load()
    pure, cont, male = male_only_split(cpm, idx, vals)
    P = np.median(cpm[pure, :], axis=0)
    C = np.median(cpm[cont, :], axis=0)
    R = (P + 0.01) / (C + 0.01)
    DET = (cpm > 0).sum(axis=0)

    bench = float(R[idx['ACAN']])
    print(f"males {len(male)} / females {cpm.shape[0]-len(male)}")
    print(f"CALIBRATORS on the sex-corrected split: COL2A1 {R[idx['COL2A1']]:.2f}  "
          f"ACAN {bench:.2f}  PTPRC {R[idx['PTPRC']]:.2f}")

    best = {}
    for i, g in enumerate(genes):
        if len(g) < 3 or P[i] < 20 or R[i] < bench or DET[i] != cpm.shape[0]:
            continue
        if g not in best or R[i] > best[g][1]:
            best[g] = (float(P[i]), float(R[i]))

    counts = atlas_mention_counts(list(best))
    recs = [{'symbol': g, 'pure_cpm': round(v[0], 1),
             'enrichment_ratio': round(v[1], 2), 'atlas_mentions': counts[g]}
            for g, v in best.items()]
    recs.sort(key=lambda d: (d['atlas_mentions'], -d['enrichment_ratio']))
    zero = [d for d in recs if d['atlas_mentions'] == 0]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump({'method': __doc__.strip(),
               'calibrators_on_this_split': {'COL2A1': round(float(R[idx['COL2A1']]), 2),
                                             'ACAN': round(bench, 2),
                                             'PTPRC': round(float(R[idx['PTPRC']]), 2)},
               'n_candidates': len(recs), 'n_zero_mention': len(zero),
               'genes': recs}, open(OUT, 'w'), indent=1)
    print(f"candidates {len(recs)}   ZERO atlas mentions {len(zero)}")
    print("\nTOP ZERO-MENTION ROWS BY ENRICHMENT")
    for d in sorted(zero, key=lambda d: -d['enrichment_ratio'])[:40]:
        print(f"  {d['symbol']:<12}{d['pure_cpm']:>9.0f} CPM {d['enrichment_ratio']:>7.1f}x")
    print(f"\nwrote {OUT}")


if __name__ == '__main__':
    main()
