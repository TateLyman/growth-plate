"""GSE288028 - HUMAN pubertal growth plate scRNA-seq, +/- growth hormone.

Two questions this file has never been able to ask:

 (1) Is TET1 expressed in human pubertal growth-plate chondrocytes, and is it
     enriched in the RESTING/stem compartment as the rat zone data (R166) says?
     Our subject IS a pubertal human growth plate.

 (2) *** Does GROWTH HORMONE change TET1? *** GH is already IN THE STACK at
     0.24-0.37 mg/kg/wk. If GH LOWERS TET1, GH and a TET1 inhibitor push the same
     way. If GH RAISES TET1, the two arms of our own stack OPPOSE each other -
     a within-stack conflict nobody has looked for.

Design: 4 fresh human growth plates (rep1-4); 3 paired cultured vehicle vs GH
(rep1,2,3; rep3 split across 2 files each); 2 mouse (ignored here).
"""
import h5py, numpy as np, scipy.sparse as sp, os, glob, math, statistics as st

SC = '/home/user/gp_data/sc'

NATIVE = {  # fresh, uncultured human
    'hs_rep1': ['GSM9328218_P30453_1001.h5'],
    'hs_rep2': ['GSM9328221_P31011_1001.h5'],
    'hs_rep3': ['GSM9328224_P25452_001.h5'],
    'hs_rep4': ['GSM9328229_P22202_1015.h5'],
}
PAIRS = {  # cultured vehicle vs GH, same donor
    'rep1': (['GSM9328219_P30453_1002.h5'], ['GSM9328220_P30453_1003.h5']),
    'rep2': (['GSM9328222_P31011_1002.h5'], ['GSM9328223_P31011_1003.h5']),
    'rep3': (['GSM9328225_P25452_004.h5', 'GSM9328226_P25452_005.h5'],
             ['GSM9328227_P25452_007.h5', 'GSM9328228_P25452_008.h5']),
}

# zone markers for human growth plate
MARK = {
    'RESTING':      ['PTHLH', 'FOXA2', 'SFRP5', 'APOE', 'CYTL1', 'GREM1'],
    'PROLIF':       ['MKI67', 'TOP2A', 'CCNB1', 'PCNA'],
    'HYPERTROPHIC': ['COL10A1', 'IBSP', 'SPP1', 'MEF2C', 'PANX3'],
    'CHONDRO':      ['COL2A1', 'ACAN', 'SOX9', 'COL9A1', 'COL11A1'],
}
GOI = ['TET1', 'TET2', 'TET3', 'DNMT1', 'DNMT3A', 'DNMT3B',
       'GHR', 'IGF1', 'IGF2', 'SOCS2', 'CISH', 'IGFBP3',
       'COL2A1', 'ACAN', 'SOX9', 'COL10A1', 'MKI67', 'PTHLH', 'IHH', 'FGFR3', 'NPR2']


def load(fn):
    with h5py.File(os.path.join(SC, fn), 'r') as f:
        g = f['matrix']
        names = np.array([x.decode() for x in g['features/name'][:]])
        shape = g['shape'][:]
        M = sp.csc_matrix((g['data'][:], g['indices'][:], g['indptr'][:]),
                          shape=(int(shape[0]), int(shape[1])))   # genes x cells
    return names, M.tocsr()


def cellsums(names, M, genes):
    idx = [i for i, n in enumerate(names) if n in genes]
    if not idx:
        return np.zeros(M.shape[1])
    return np.asarray(M[idx, :].sum(axis=0)).ravel()


def pseudobulk(files):
    """CPM-normalised pseudobulk over a sample (sum counts across cells)."""
    tot = None
    names0 = None
    ncell = 0
    for fn in files:
        names, M = load(fn)
        if names0 is None:
            names0 = names
        s = np.asarray(M.sum(axis=1)).ravel()
        tot = s if tot is None else tot + s
        ncell += M.shape[1]
    cpm = tot / tot.sum() * 1e6
    return names0, cpm, ncell


print('=' * 86)
print('PART 1 - TET expression in FRESH HUMAN pubertal growth plate (pseudobulk CPM)')
print('=' * 86)
print('%-10s %8s %s' % ('sample', 'ncells', ''.join('%9s' % g for g in
                                                    ['TET1', 'TET2', 'TET3', 'COL2A1', 'ACAN', 'COL10A1', 'PTHLH', 'GHR'])))
native_tet = {'TET1': [], 'TET2': [], 'TET3': []}
for lab, files in NATIVE.items():
    names, cpm, nc = pseudobulk(files)
    look = {g: (cpm[np.where(names == g)[0]].sum() if (names == g).any() else 0.0) for g in GOI}
    for k in native_tet:
        native_tet[k].append(look[k])
    print('%-10s %8d %s' % (lab, nc, ''.join('%9.1f' % look[g] for g in
                                             ['TET1', 'TET2', 'TET3', 'COL2A1', 'ACAN', 'COL10A1', 'PTHLH', 'GHR'])))
print()
for k, v in native_tet.items():
    print('  %s across 4 donors: mean %.1f CPM (range %.1f-%.1f)' % (k, st.mean(v), min(v), max(v)))

print()
print('=' * 86)
print('PART 2 - TET1 by CELL-LEVEL ZONE IDENTITY, fresh human growth plates')
print('=' * 86)
agg = {}
for lab, files in NATIVE.items():
    names, M = load(files[0])
    tot = np.asarray(M.sum(axis=0)).ravel()
    keep = tot >= 500                       # basic QC
    scores = {k: cellsums(names, M, set(v)) / np.maximum(tot, 1) for k, v in MARK.items()}
    # assign each cell to the zone with the highest normalised marker score
    zn = ['RESTING', 'PROLIF', 'HYPERTROPHIC']
    S = np.vstack([scores[z] for z in zn])
    call = np.array(zn)[S.argmax(axis=0)]
    call[(S.max(axis=0) == 0)] = 'NONE'
    t1 = cellsums(names, M, {'TET1'})
    for z in zn:
        m = keep & (call == z)
        if m.sum() < 20:
            continue
        cpm = (t1[m].sum() / tot[m].sum()) * 1e6
        agg.setdefault(z, []).append((cpm, int(m.sum())))
    print('  %-8s cells kept %5d   zone counts %s' % (lab, int(keep.sum()),
          {z: int((keep & (call == z)).sum()) for z in zn}))
print()
print('  %-14s %10s %10s' % ('zone', 'TET1 CPM', 'n donors'))
for z in ['RESTING', 'PROLIF', 'HYPERTROPHIC']:
    if z in agg:
        vals = [a for a, _ in agg[z]]
        print('  %-14s %10.1f %10d   (per-donor: %s)' % (z, st.mean(vals), len(vals),
              ', '.join('%.0f' % v for v in vals)))

print()
print('=' * 86)
print('PART 3 - *** DOES GROWTH HORMONE CHANGE TET1? *** paired vehicle vs GH, n=3 donors')
print('=' * 86)
res = {}
for rep, (veh, gh) in PAIRS.items():
    nv, cv, ncv = pseudobulk(veh)
    ng, cg, ncg = pseudobulk(gh)
    print('\n  %s   vehicle %d cells | GH %d cells' % (rep, ncv, ncg))
    print('    %-10s %10s %10s %9s' % ('gene', 'vehicle', 'GH', 'log2FC'))
    for g in ['TET1', 'TET2', 'TET3', 'SOCS2', 'CISH', 'IGF1', 'IGFBP3', 'GHR',
              'COL2A1', 'ACAN', 'COL10A1', 'MKI67', 'SOX9']:
        a = cv[np.where(nv == g)[0]].sum() if (nv == g).any() else 0.0
        b = cg[np.where(ng == g)[0]].sum() if (ng == g).any() else 0.0
        lfc = math.log2((b + 0.1) / (a + 0.1))
        res.setdefault(g, []).append(lfc)
        tag = '  <-- GH target' if g in ('SOCS2', 'CISH', 'IGF1') else ''
        print('    %-10s %10.2f %10.2f %+9.2f%s' % (g, a, b, lfc, tag))

print('\n  --- summary across the 3 paired donors (log2 GH/vehicle) ---')
print('  %-10s %s   %8s' % ('gene', ''.join('%9s' % r for r in PAIRS), 'mean'))
for g in ['TET1', 'TET2', 'TET3', 'SOCS2', 'CISH', 'IGF1', 'IGFBP3', 'COL2A1', 'ACAN', 'COL10A1', 'MKI67']:
    v = res[g]
    print('  %-10s %s   %+8.2f  %s' % (g, ''.join('%+9.2f' % x for x in v), st.mean(v),
                                       'CONSISTENT' if all(x > 0 for x in v) or all(x < 0 for x in v) else ''))
