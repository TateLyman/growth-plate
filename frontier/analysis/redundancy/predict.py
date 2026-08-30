"""Quantitative prediction: will a GCK-IV inhibitor bind NRK?

Method: an ATP-pocket is what an ATP-competitive inhibitor actually touches, so
whole-domain identity is the wrong ruler. Build the pocket residue set from
motif anchors (P-loop, beta3-K, alphaC-E, gatekeeper+hinge, catalytic loop, DFG),
compute pairwise POCKET identity, then CALIBRATE against the five pairs whose
cross-reactivity I measured empirically in R146. Finally place NRK on that curve.
"""
from Bio import SeqIO, Align
from Bio.Align import substitution_matrices
import re, itertools

seqs = {}
for rec in SeqIO.parse('gck.fasta', 'fasta'):
    seqs[rec.description.split('|')[2].split('_')[0]] = str(rec.seq)

KD = {'NRK': (25, 313), 'M4K4': (25, 289), 'TNIK': (25, 289), 'MINK1': (25, 289),
      'M4K1': (17, 293), 'M4K5': (12, 285), 'M4K2': (16, 273), 'M4K3': (13, 276),
      'OXSR1': (9, 299), 'STK39': (77, 356)}
NAME = {'M4K4': 'MAP4K4', 'M4K1': 'MAP4K1', 'M4K5': 'MAP4K5', 'M4K2': 'MAP4K2', 'M4K3': 'MAP4K3'}
def nm(s): return NAME.get(s, s)

def dom(s):
    a, b = KD[s]; return seqs[s][a-1:b]

blosum = substitution_matrices.load("BLOSUM62")
al = Align.PairwiseAligner(); al.substitution_matrix = blosum
al.open_gap_score = -11; al.extend_gap_score = -1; al.mode = 'global'

REF = 'M4K4'   # anchor: MAP4K4 has multiple inhibitor co-crystals

def anchors(s):
    """Locate the canonical catalytic motifs in a kinase domain sequence."""
    a = {}
    m = re.search(r'G.G..G.V', s);            a['ploop'] = m.start() if m else None
    m = re.search(r'[AVIC][AVIC]IK', s);      a['b3K']   = (m.start()+3) if m else None
    m = re.search(r'HRD[LIVMF]K', s);         a['HRD']   = m.start() if m else None
    m = re.search(r'D[FLI]G', s[a['HRD']:] if a['HRD'] else s)
    a['DFG'] = (a['HRD'] + m.start()) if (m and a['HRD']) else None
    return a

def pocket_idx(s):
    """~26 ATP-pocket positions, defined off the motif anchors.
    P-loop +flank, beta3 K, alphaC E, gatekeeper+hinge, catalytic loop, DFG-1/DFG."""
    a = anchors(s)
    idx = []
    if a['ploop'] is not None:
        idx += list(range(a['ploop'], a['ploop'] + 8))        # GxGxxGxV
        idx += [a['ploop'] + 10, a['ploop'] + 12]             # beta2 floor
    if a['b3K'] is not None:
        idx += [a['b3K'] - 3, a['b3K'], a['b3K'] + 17, a['b3K'] + 21]  # beta3 A, K, alphaC region
    if a['HRD'] is not None:
        # gatekeeper/hinge sit ~ HRD-40 .. HRD-33 in this family; take the block
        idx += list(range(a['HRD'] - 41, a['HRD'] - 32))
        idx += [a['HRD'], a['HRD'] + 1, a['HRD'] + 2, a['HRD'] + 3, a['HRD'] + 5]
    if a['DFG'] is not None:
        idx += [a['DFG'] - 1, a['DFG'], a['DFG'] + 1, a['DFG'] + 2]
    return [i for i in idx if 0 <= i < len(s)]

def pocket_seq(s):
    d = dom(s); return ''.join(d[i] for i in pocket_idx(d)), pocket_idx(d)

print("=" * 88)
print("STEP 1 -- ATP-POCKET RESIDUES, derived from catalytic motif anchors")
print("=" * 88)
pk = {}
for s in ['NRK', 'M4K4', 'TNIK', 'MINK1', 'M4K1', 'M4K2', 'M4K3', 'M4K5', 'OXSR1', 'STK39']:
    p, idx = pocket_seq(s)
    pk[s] = p
    print("%-8s %2d residues   %s" % (nm(s), len(p), p))

def pocket_id(a, b):
    A, B = pk[a], pk[b]
    n = min(len(A), len(B))
    if n == 0: return 0.0, 0.0
    ident = sum(1 for x, y in zip(A[:n], B[:n]) if x == y)
    sim = sum(1 for x, y in zip(A[:n], B[:n]) if blosum[x, y] > 0)
    return 100.0*ident/n, 100.0*sim/n

print()
print("=" * 88)
print("STEP 2 -- CALIBRATION: pocket identity vs MEASURED cross-reactivity (R146)")
print("=" * 88)
MEAS = {('M4K4','MINK1'): 68, ('M4K4','TNIK'): 89, ('TNIK','MINK1'): 87,
        ('M4K4','M4K1'): 92, ('TNIK','M4K1'): 94}
print("%-22s %14s %14s %16s" % ("pair", "pocket ident", "pocket simil", "MEASURED carry-over"))
print("-" * 74)
cal = []
for (a, b), v in sorted(MEAS.items(), key=lambda kv: -kv[1]):
    i, s = pocket_id(a, b)
    cal.append((i, v))
    print("%-22s %13.1f%% %13.1f%% %15d%%" % ("%s / %s" % (nm(a), nm(b)), i, s, v))

lo = min(c[0] for c in cal); hi = max(c[0] for c in cal)
print()
print("  Measured carry-over spans %d-%d%% across pocket identity %.1f-%.1f%%." % (
      min(v for _, v in cal), max(v for _, v in cal), lo, hi))
print("  -> in this family, EVERY pair in the calibration range cross-reacts most of the time.")

print()
print("=" * 88)
print("STEP 3 -- WHERE DOES NRK SIT?")
print("=" * 88)
print("%-24s %14s %14s   %s" % ("NRK vs", "pocket ident", "pocket simil", "position vs calibration"))
print("-" * 88)
rows = []
for s in ['TNIK', 'M4K4', 'MINK1', 'M4K1', 'M4K3', 'M4K2', 'M4K5', 'OXSR1', 'STK39']:
    i, sim = pocket_id('NRK', s)
    rows.append((i, s, sim))
rows.sort(reverse=True)
for i, s, sim in rows:
    if i >= hi:      pos = "ABOVE the whole calibration range"
    elif i >= lo:    pos = "INSIDE the calibration range"
    else:            pos = "below calibration range"
    print("%-24s %13.1f%% %13.1f%%   %s" % (nm(s), i, sim, pos))

print()
print("=" * 88)
print("STEP 4 -- RESIDUE-BY-RESIDUE: where would selectivity have to live?")
print("=" * 88)
for s in ['TNIK', 'M4K4', 'MINK1']:
    A, B = pk['NRK'], pk[s]
    n = min(len(A), len(B))
    diffs = [(k, A[k], B[k]) for k in range(n) if A[k] != B[k]]
    print("\nNRK vs %s -- %d/%d pocket positions differ:" % (nm(s), len(diffs), n))
    print("   NRK : %s" % A[:n])
    print("   %-4s: %s" % (nm(s)[:4], B[:n]))
    print("   diff: %s" % ''.join(' ' if A[k] == B[k] else '^' for k in range(n)))
    if diffs:
        print("   changes: " + ", ".join("%s%d%s" % (b, k+1, a) for k, a, b in diffs))
        cons = [d for d in diffs if blosum[d[1], d[2]] > 0]
        print("   of which CONSERVATIVE (BLOSUM>0): %d/%d" % (len(cons), len(diffs)))
