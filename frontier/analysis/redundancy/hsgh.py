"""GH vs vehicle in human growth plate, CELL-TYPE-MATCHED.

The pseudobulk comparison failed: the GH-response positive controls (SOCS2, CISH,
IGF1) do not move consistently and the chondrocyte genes swing by +/-6 log2
between replicates - i.e. the cultures differ in CELL COMPOSITION, which swamps
any GH effect. The fix is to compare like with like: restrict to cells of the
same assigned zone in both arms, then compare TET1.
"""
import h5py, numpy as np, scipy.sparse as sp, os, math, statistics as st

SC = '/home/user/gp_data/sc'
PAIRS = {
    'rep1': (['GSM9328219_P30453_1002.h5'], ['GSM9328220_P30453_1003.h5']),
    'rep2': (['GSM9328222_P31011_1002.h5'], ['GSM9328223_P31011_1003.h5']),
    'rep3': (['GSM9328225_P25452_004.h5', 'GSM9328226_P25452_005.h5'],
             ['GSM9328227_P25452_007.h5', 'GSM9328228_P25452_008.h5']),
}
MARK = {
    'RESTING':      ['PTHLH', 'FOXA2', 'SFRP5', 'APOE', 'CYTL1', 'GREM1'],
    'PROLIF':       ['MKI67', 'TOP2A', 'CCNB1', 'PCNA'],
    'HYPERTROPHIC': ['COL10A1', 'IBSP', 'SPP1', 'MEF2C', 'PANX3'],
}
REPORT = ['TET1', 'TET2', 'TET3', 'SOCS2', 'CISH', 'IGF1', 'IGFBP3', 'COL2A1', 'ACAN', 'MKI67']


def load(fn):
    with h5py.File(os.path.join(SC, fn), 'r') as f:
        g = f['matrix']
        names = np.array([x.decode() for x in g['features/name'][:]])
        shape = g['shape'][:]
        M = sp.csc_matrix((g['data'][:], g['indices'][:], g['indptr'][:]),
                          shape=(int(shape[0]), int(shape[1])))
    return names, M.tocsr()


def concat(files):
    ns, Ms = None, []
    for fn in files:
        n, M = load(fn)
        ns = n if ns is None else ns
        Ms.append(M)
    return ns, sp.hstack(Ms).tocsr() if len(Ms) > 1 else Ms[0]


def zonecall(names, M):
    tot = np.asarray(M.sum(axis=0)).ravel()
    sc = {}
    for k, v in MARK.items():
        idx = [i for i, n in enumerate(names) if n in set(v)]
        sc[k] = (np.asarray(M[idx, :].sum(axis=0)).ravel() / np.maximum(tot, 1)) if idx else np.zeros(M.shape[1])
    zn = list(MARK)
    S = np.vstack([sc[z] for z in zn])
    call = np.array(zn, dtype=object)[S.argmax(axis=0)]
    call[S.max(axis=0) == 0] = 'NONE'
    return call, tot


def cpm_in(names, M, tot, mask, gene):
    i = np.where(names == gene)[0]
    if len(i) == 0 or mask.sum() == 0:
        return float('nan')
    num = np.asarray(M[i, :][:, mask].sum()).ravel()[0]
    den = tot[mask].sum()
    return (num / den) * 1e6 if den else float('nan')


print('=' * 90)
print('GH vs VEHICLE, CELL-TYPE-MATCHED (human growth plate, 3 paired donors)')
print('=' * 90)
store = {}
comp = {}
for rep, (veh, gh) in PAIRS.items():
    nv, Mv = concat(veh)
    ng, Mg = concat(gh)
    cv, tv = zonecall(nv, Mv)
    cg, tg = zonecall(ng, Mg)
    kv, kg = tv >= 500, tg >= 500
    fv = {z: float((kv & (cv == z)).sum()) for z in MARK}
    fg = {z: float((kg & (cg == z)).sum()) for z in MARK}
    sv, sg = sum(fv.values()), sum(fg.values())
    comp[rep] = ({z: fv[z] / sv for z in fv}, {z: fg[z] / sg for z in fg})
    print('\n  %s  composition  vehicle %s   GH %s'
          % (rep, {z: '%.0f%%' % (100 * fv[z] / sv) for z in fv}, {z: '%.0f%%' % (100 * fg[z] / sg) for z in fg}))
    for z in ['RESTING', 'PROLIF', 'HYPERTROPHIC']:
        mv, mg = kv & (cv == z), kg & (cg == z)
        if mv.sum() < 30 or mg.sum() < 30:
            print('    %-13s (too few cells: %d / %d)' % (z, mv.sum(), mg.sum())); continue
        print('    %-13s n=%d/%d' % (z, mv.sum(), mg.sum()))
        for g in REPORT:
            a = cpm_in(nv, Mv, tv, mv, g)
            b = cpm_in(ng, Mg, tg, mg, g)
            if a != a or b != b:
                continue
            lfc = math.log2((b + 0.1) / (a + 0.1))
            store.setdefault((z, g), []).append(lfc)
            if g in ('TET1', 'SOCS2', 'CISH', 'IGF1'):
                print('        %-8s veh %8.1f  GH %8.1f  log2FC %+6.2f' % (g, a, b, lfc))

print('\n' + '=' * 90)
print('SUMMARY - log2(GH/vehicle) WITHIN matched zone, across donors')
print('=' * 90)
for z in ['RESTING', 'PROLIF', 'HYPERTROPHIC']:
    rows = [(g, store[(z, g)]) for g in REPORT if (z, g) in store]
    if not rows:
        continue
    print('\n  %s' % z)
    print('    %-9s %s   %8s  %s' % ('gene', ''.join('%9s' % r for r in PAIRS), 'mean', 'consistent?'))
    for g, v in rows:
        cons = 'YES' if (all(x > 0 for x in v) or all(x < 0 for x in v)) and len(v) >= 2 else ''
        print('    %-9s %s   %+8.2f  %s' % (g, ''.join('%+9.2f' % x for x in v) + ' ' * (9 * (len(PAIRS) - len(v))),
                                            st.mean(v), cons))
print("""
READ THE POSITIVE CONTROLS FIRST: SOCS2/CISH/IGF1 are canonical GH-induced genes.
If they do not move consistently UP, the GH stimulation is not detectable in this
data and NO conclusion about TET1 can be drawn from it.""")
