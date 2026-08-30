"""TET1/2/3 expression across microdissected growth-plate ZONES.

GSE16981 (Lui & Baron, "Spatial and Temporal Regulation of Gene Expression in the
Mammalian Growth Plate") and GSE23432 - postnatal rat growth plates microdissected
into resting / proliferative / hypertrophic zones, Affymetrix Rat 230 2.0 (GPL1355).

Question: our arm targets the RESTING ZONE renewal:commitment ratio. Is TET1
expressed there, and is it zone-patterned? Hole 13 says TET1 is only 7/10 in the
growth plate as a whole - zone resolution is the right test.
Note: TET1's older alias is Cxxc6; TET2 = Kiaa1546; TET3 = Kiaa0401. Search all.
"""
import gzip, io, re, statistics as st

ANNOT = '/home/user/gp_data/gpl1355.annot.gz'
TARGET_ALIASES = {
    'TET1': ['Tet1', 'Cxxc6'],
    'TET2': ['Tet2', 'Kiaa1546'],
    'TET3': ['Tet3', 'Kiaa0401'],
    # positive controls with known zonal patterns
    'COL2A1': ['Col2a1'], 'COL10A1': ['Col10a1'], 'ACAN': ['Acan', 'Agc1'],
    'IHH': ['Ihh'], 'PTHLH': ['Pthlh'], 'SOX9': ['Sox9'], 'MKI67': ['Mki67'],
}
low = {}
for k, v in TARGET_ALIASES.items():
    for a in v:
        low[a.lower()] = k

# ---- map probes ----
probe2gene = {}
with gzip.open(ANNOT, 'rt', errors='replace') as f:
    for line in f:
        if line.startswith('!') or line.startswith('#'):
            continue
        p = line.rstrip('\n').split('\t')
        if len(p) < 3:
            continue
        sym = p[2].strip()
        if sym.lower() in low:
            probe2gene[p[0].strip()] = (low[sym.lower()], sym)
print('probes matched:', len(probe2gene))
for pr, (g, s) in sorted(probe2gene.items(), key=lambda x: x[1][0]):
    print('   %-16s %-8s (%s)' % (pr, g, s))


def run(path, label):
    print('\n' + '=' * 70)
    print(label)
    titles = None
    rows = {}
    with gzip.open(path, 'rt', errors='replace') as f:
        for line in f:
            if line.startswith('!Sample_title'):
                titles = [x.strip().strip('"') for x in line.rstrip('\n').split('\t')[1:]]
            if line.startswith('!'):
                continue
            p = line.rstrip('\n').split('\t')
            pid = p[0].strip().strip('"')
            if pid == 'ID_REF' or not p[1:]:
                continue
            if pid in probe2gene:
                try:
                    rows[pid] = [float(x) if x not in ('', 'null', 'NA') else None for x in p[1:]]
                except ValueError:
                    pass
    if not titles:
        print('  no sample titles'); return
    print('  samples:', len(titles))

    # classify zone from title
    def zone(t):
        s = t.lower()
        if re.search(r'\brz\b|resting|reserve', s): return 'RZ'
        if re.search(r'\bpz\b|prolifer', s): return 'PZ'
        if re.search(r'\bhz\b|hypertroph', s): return 'HZ'
        return None
    z = [zone(t) for t in titles]
    print('  zone calls:', {k: z.count(k) for k in ('RZ', 'PZ', 'HZ', None)})
    if not any(z):
        return
    print('\n  %-10s %-14s %8s %8s %8s' % ('gene', 'probe', 'RZ', 'PZ', 'HZ'))
    for pid, vals in sorted(rows.items(), key=lambda x: probe2gene[x[0]][0]):
        g = probe2gene[pid][0]
        out = []
        for zz in ('RZ', 'PZ', 'HZ'):
            v = [vals[i] for i in range(len(vals)) if i < len(z) and z[i] == zz and vals[i] is not None]
            out.append(st.mean(v) if v else float('nan'))
        rz,pz,hz=out
        ratio = (rz/pz) if pz else float('nan')
        print('  %-10s %-14s %8.1f %8.1f %8.1f   RZ/PZ %5.2f  RZ/HZ %5.2f' % (g, pid, rz,pz,hz, ratio, (rz/hz) if hz else float('nan')))


import sys
run('/home/user/gp_data/gse16981.txt.gz', 'GSE16981 - Lui & Baron, rat growth plate zones')
run('/home/user/gp_data/gse23432.txt.gz', 'GSE23432 - Ihh signaling, rat growth plate zones')
