"""Proper detection call for GSE9160 (MAS5-scaled Affy GPL570).
Background estimated from the whole-array probe distribution, not AFFX spike-ins
(which are high-intensity hybridisation controls and give absurd thresholds)."""
import gzip, statistics as st, bisect

def load(fn):
    rows = []; hdr = None; on = False; titles = None
    with gzip.open(fn, 'rt', errors='replace') as f:
        for l in f:
            l = l.rstrip('\n')
            if l.startswith('!Sample_title'):
                titles = [x.strip('"') for x in l.split('\t')[1:]]
            if l.startswith('!series_matrix_table_begin'): on = True; continue
            if l.startswith('!series_matrix_table_end'): break
            if on:
                p = l.split('\t')
                if hdr is None: hdr = p; continue
                rows.append(p)
    return titles, hdr, rows

def ann(f):
    m = {}
    with gzip.open(f, 'rt', errors='replace') as fh:
        on = False
        for l in fh:
            if l.startswith('!platform_table_begin'): on = True; continue
            if l.startswith('!platform_table_end'): break
            if on:
                p = l.rstrip('\n').split('\t')
                if p[0] == 'ID': continue
                if len(p) > 2: m[p[0].strip('"')] = p[2].strip('"')
    return m

T, H, R = load('GSE9160_series_matrix.txt.gz')
A = ann('GPL570.annot.gz')
n = len(T)
cols = [[] for _ in range(n)]
vals = []
for p in R:
    pid = p[0].strip('"')
    try:
        v = [float(x) if x not in ('', 'null', 'NA') else 0.0 for x in p[1:]]
    except Exception:
        continue
    for j in range(n): cols[j].append(v[j])
    g = A.get(pid)
    if g: vals.append((g, pid, v))
for c in cols: c.sort()

# On a GPL570 array roughly 40-55% of probes are "absent" in any one tissue.
# Use the 60th percentile of the whole array as a conservative present/absent line.
THR_PCT = 0.60
bg = [c[int(THR_PCT * len(c))] for c in cols]
print("arrays: %d   probes/array: %d" % (n, len(cols[0])))
print("zones:", [t.split(',')[0] for t in T])
print()
print("background = %dth percentile of all probes on each array:" % int(THR_PCT * 100))
print("  " + "  ".join("%6.0f" % b for b in bg))
print("  (atlas R292 quoted per-array thresholds of 451-827 -- these should be comparable)")
print()

def report(sym, show=True):
    hits = [(pid, v) for (g, pid, v) in vals if g == sym]
    if not hits:
        if show: print("%-9s no probe on array" % sym)
        return None
    best = None
    for pid, v in hits:
        det = sum(1 for j in range(n) if v[j] > bg[j])
        if best is None or det > best[0]: best = (det, pid, v)
    if show:
        for pid, v in hits:
            flags = ''.join('D' if v[j] > bg[j] else '.' for j in range(n))
            print("  %-9s %-13s %s  %s" % (sym, pid, " ".join("%6.0f" % x for x in v), flags))
    return best

print("=== POSITIVE CONTROLS ===")
for g in ["COL2A1", "ACAN", "COL10A1", "IHH"]: report(g)
print()
print("=== THE GENE IN QUESTION ===")
report("SPIN4")
print()
print("=== GENES USED IN R143 TERM B2 (the zonal Wnt-output panel) ===")
for g in ["AXIN2", "SP5", "LGR5", "NKD1"]: report(g)
print()
print("=== ALTERNATIVE CANDIDATES ===")
for g in ["NRK", "TET1", "TET2", "TET3", "CHD8", "SPIN1", "ZFAT", "LCORL", "FBN1"]: report(g)
