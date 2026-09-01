"""Will a GCK-IV inhibitor bind NRK?  -- corrected, alignment-based.

predict.py was WRONG: it located motifs by regex independently in each sequence
and then compared by string index. NRK's motifs are canonical but variant
(P-loop GLGTYGRI not GNGTYGQV; beta3 TAVK not AAIK), so the regexes missed them
and the comparison lined NRK's HRD block up against everyone else's P-loop.

Correct method: define the ATP pocket ONCE in a reference kinase with inhibitor
co-crystals (MAP4K4), then map those positions into every other kinase THROUGH A
PAIRWISE ALIGNMENT. Calibrate pocket identity against the five pairs whose
cross-reactivity was measured empirically in R146, then place NRK on that curve.
"""
from Bio import SeqIO, Align
from Bio.Align import substitution_matrices
import re

seqs = {}
for rec in SeqIO.parse('gck.fasta', 'fasta'):
    seqs[rec.description.split('|')[2].split('_')[0]] = str(rec.seq)
KD = {'NRK': (25, 313), 'M4K4': (25, 289), 'TNIK': (25, 289), 'MINK1': (25, 289),
      'M4K1': (17, 293), 'M4K5': (12, 285), 'M4K2': (16, 273), 'M4K3': (13, 276),
      'OXSR1': (9, 299), 'STK39': (77, 356)}
NAME = {'M4K4': 'MAP4K4', 'M4K1': 'MAP4K1', 'M4K5': 'MAP4K5', 'M4K2': 'MAP4K2', 'M4K3': 'MAP4K3'}
def nm(s): return NAME.get(s, s)
def dom(s): a, b = KD[s]; return seqs[s][a-1:b]

blosum = substitution_matrices.load("BLOSUM62")
al = Align.PairwiseAligner(); al.substitution_matrix = blosum
al.open_gap_score = -11; al.extend_gap_score = -1; al.mode = 'global'

REF = 'M4K4'
ref = dom(REF)

# ---- define the pocket ONCE, in the reference ----------------------------
p_ploop = re.search(r'G.G..G..', ref).start()          # GNGTYGQV
p_b3K   = re.search(r'[ACILV][ACILV]IK', ref).start()+3
p_HRD   = re.search(r'HRD[LIVMF]K', ref).start()
p_DFG   = p_HRD + re.search(r'D[FLI]G', ref[p_HRD:]).start()
p_gk    = 104 - KD[REF][0]                              # MAP4K4 gatekeeper Met104

POCKET = (list(range(p_ploop, p_ploop + 8))             # glycine-rich loop
          + [p_ploop + 10, p_ploop + 12]                # beta2 floor
          + [p_b3K - 3, p_b3K]                          # beta3 Ala, Lys
          + [p_b3K + 17, p_b3K + 21]                    # alphaC region
          + list(range(p_gk - 2, p_gk + 6))             # gatekeeper -2 .. hinge +5
          + [p_HRD, p_HRD + 1, p_HRD + 2, p_HRD + 3, p_HRD + 5]   # catalytic loop
          + [p_DFG - 1, p_DFG, p_DFG + 1, p_DFG + 2])   # DFG
POCKET = sorted(set(i for i in POCKET if 0 <= i < len(ref)))
print("Reference = MAP4K4 kinase domain (UniProt 25-289).  Pocket = %d positions." % len(POCKET))
print("  P-loop@%d  beta3K@%d  gatekeeper@%d (Met%d)  HRD@%d  DFG@%d"
      % (p_ploop, p_b3K, p_gk, p_gk + KD[REF][0], p_HRD, p_DFG))
print("  reference pocket residues: %s" % ''.join(ref[i] for i in POCKET))
print()

def map_pocket(q):
    """Return the query residues aligned to the reference pocket positions."""
    if q == REF: return ''.join(ref[i] for i in POCKET)
    aln = al.align(ref, dom(q))[0]
    A, B = str(aln[0]), str(aln[1])
    ri = qi = -1; m = {}
    for x, y in zip(A, B):
        if x != '-': ri += 1
        if y != '-': qi += 1
        if x != '-': m[ri] = (y if y != '-' else '-')
    return ''.join(m.get(i, '-') for i in POCKET)

pk = {s: map_pocket(s) for s in KD}
print("=" * 92)
print("STEP 1 -- ATP-POCKET RESIDUES, all mapped onto the SAME reference positions")
print("=" * 92)
for s in ['M4K4', 'TNIK', 'MINK1', 'NRK', 'M4K1', 'M4K2', 'M4K3', 'M4K5', 'OXSR1', 'STK39']:
    print("%-8s %s" % (nm(s), pk[s]))

def pid(a, b):
    A, B = pk[a], pk[b]
    ok = [(x, y) for x, y in zip(A, B) if x != '-' and y != '-']
    if not ok: return 0.0, 0.0
    i = sum(1 for x, y in ok if x == y)
    sm = sum(1 for x, y in ok if blosum[x, y] > 0)
    return 100.0*i/len(ok), 100.0*sm/len(ok)

print()
print("=" * 92)
print("STEP 2 -- CALIBRATION: pocket identity vs the cross-reactivity MEASURED in R146")
print("=" * 92)
MEAS = {('M4K4','MINK1'): 68, ('M4K4','TNIK'): 89, ('TNIK','MINK1'): 87,
        ('M4K4','M4K1'): 92, ('TNIK','M4K1'): 94}
print("%-24s %14s %14s %20s" % ("pair", "pocket ident", "pocket simil", "MEASURED carry-over"))
print("-" * 78)
cal = []
for (a, b), v in sorted(MEAS.items(), key=lambda kv: kv[1]):
    i, s = pid(a, b); cal.append((i, v))
    print("%-24s %13.1f%% %13.1f%% %19d%%" % ("%s / %s" % (nm(a), nm(b)), i, s, v))
lo = min(c[0] for c in cal)
print()
print("  ALL five measured pairs cross-react 68-94%% of the time.")
print("  The LOWEST pocket identity in that calibration set is %.1f%% -- and it still" % lo)
print("  carries over %d%% of the time." % dict((round(c[0],1), c[1]) for c in cal)[round(lo,1)])

print()
print("=" * 92)
print("STEP 3 -- WHERE DOES NRK SIT?")
print("=" * 92)
print("%-24s %14s %14s   %s" % ("NRK vs", "pocket ident", "pocket simil", "vs calibration floor (%.1f%%)" % lo))
print("-" * 92)
rows = sorted(((pid('NRK', s)[0], pid('NRK', s)[1], s) for s in KD if s != 'NRK'), reverse=True)
for i, sm, s in rows:
    tag = "ABOVE floor -- inside the range where everything cross-reacts" if i >= lo else "below floor"
    print("%-24s %13.1f%% %13.1f%%   %s" % (nm(s), i, sm, tag))

print()
print("=" * 92)
print("STEP 4 -- RESIDUE-BY-RESIDUE vs the three drugged members")
print("=" * 92)
for s in ['TNIK', 'M4K4', 'MINK1']:
    A, B = pk['NRK'], pk[s]
    diffs = [(k, A[k], B[k]) for k in range(len(A)) if A[k] != B[k] and A[k] != '-' and B[k] != '-']
    ok = sum(1 for x, y in zip(A, B) if x != '-' and y != '-')
    print("\nNRK vs %s -- %d of %d pocket positions differ" % (nm(s), len(diffs), ok))
    print("   %-6s %s" % (nm(s)[:6], B))
    print("   NRK    %s" % A)
    print("   diff   %s" % ''.join(' ' if A[k] == B[k] else '^' for k in range(len(A))))
    if diffs:
        cons = [d for d in diffs if blosum[d[1], d[2]] > 0]
        print("   changes: " + ", ".join("%s->%s@%d" % (b, a, k+1) for k, a, b in diffs))
        print("   CONSERVATIVE (BLOSUM>0): %d/%d" % (len(cons), len(diffs)))
        gkcol = POCKET.index(p_gk)
        print("   GATEKEEPER column: %s (%s) vs %s (NRK)  -> %s"
              % (B[gkcol], nm(s), A[gkcol], "SAME" if A[gkcol] == B[gkcol] else "DIFFERENT"))
