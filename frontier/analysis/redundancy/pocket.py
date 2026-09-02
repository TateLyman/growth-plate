"""How similar is NRK's ATP pocket to kinases that DO have inhibitors?

NRK is Tdark: 0 ligands, 0 drugs, not a ChEMBL target. That means nobody has
LOOKED, not that nothing binds. The practical question is whether an existing
GCK/STE20 inhibitor would hit it off-target. That is decided by the ATP pocket.

Approach: pairwise-align NRK's kinase domain (UniProt 25-313) against the kinase
domains of GCK-family members that have chemical matter, then compare (a) whole
kinase-domain identity and (b) the specific pocket-lining positions -- the
glycine-rich loop, the VAIK lysine, the gatekeeper, and the hinge.
"""
from Bio import SeqIO, Align
from Bio.Align import substitution_matrices

seqs = {}
for rec in SeqIO.parse('gck.fasta', 'fasta'):
    sym = rec.description.split('|')[2].split('_')[0]
    seqs[sym] = str(rec.seq)

# UniProt kinase-domain boundaries
KD = {
    'NRK':   (25, 313),   'M4K4':  (25, 289),  'TNIK': (25, 289),
    'MINK1': (25, 289),   'M4K1':  (17, 293),  'M4K5': (12, 285),
    'M4K2':  (16, 273),   'M4K3':  (13, 276),  'OXSR1': (9, 299),
    'STK39': (77, 356),
}
CHEM = {  # what chemical matter exists, for context
    'M4K4':  'Tchem - PF-06260933, GNE-495, DMX-5804',
    'TNIK':  'Tchem - NCB-0846, KY-05009  (Wnt/TCF4 kinase)',
    'MINK1': 'Tchem - hit by MAP4K4 inhibitors',
    'M4K1':  'Tchem - HPK1, heavy immuno-oncology programme',
    'M4K5':  'Tbio', 'M4K2': 'Tbio', 'M4K3': 'Tbio',
    'OXSR1': 'Tbio', 'STK39': 'Tchem - SPAK, WNK pathway',
}

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -11
aligner.extend_gap_score = -1
aligner.mode = 'global'

def dom(sym):
    a, b = KD[sym]
    return seqs[sym][a-1:b]

nrk = dom('NRK')
print("NRK kinase domain: UniProt 25-313, %d aa" % len(nrk))
print("NRK full protein : %d aa   (kinase domain N-terminal, CNH domain 1209-1552)" % len(seqs['NRK']))
print()
print("%-7s %-9s %8s %8s   %s" % ("kinase", "KD len", "identity", "similar", "chemical matter"))
print("-" * 84)
rows = []
for sym in ['M4K4', 'TNIK', 'MINK1', 'M4K1', 'M4K5', 'M4K2', 'M4K3', 'OXSR1', 'STK39']:
    d = dom(sym)
    aln = aligner.align(nrk, d)[0]
    A = str(aln[0]); B = str(aln[1])
    ident = sum(1 for x, y in zip(A, B) if x == y and x != '-')
    sim = sum(1 for x, y in zip(A, B)
              if x != '-' and y != '-' and
              substitution_matrices.load("BLOSUM62")[x, y] > 0)
    n = min(len(nrk), len(d))
    rows.append((100.0*ident/n, sym, len(d), 100.0*sim/n))
    print("%-7s %-9d %7.1f%% %7.1f%%   %s" % (sym, len(d), 100.0*ident/n, 100.0*sim/n, CHEM[sym]))

rows.sort(reverse=True)
print()
print("CLOSEST BY KINASE-DOMAIN IDENTITY: %s (%.1f%%)  -- %s" % (rows[0][1], rows[0][0], CHEM[rows[0][1]]))
print()

# ---- pocket motifs -------------------------------------------------------
import re
print("=" * 84)
print("ATP-POCKET MOTIFS  (the residues an ATP-competitive inhibitor contacts)")
print("=" * 84)
for sym in ['NRK', 'M4K4', 'TNIK', 'MINK1', 'M4K1']:
    s = dom(sym)
    gly = re.search(r'G.G..G.V', s)          # glycine-rich / P-loop
    vaik = re.search(r'[AV][AV]IK', s)       # beta3 lysine
    hrd = re.search(r'HRD[LIVM]K', s)        # catalytic loop
    dfg = re.search(r'DFG', s)               # activation loop start
    print("%-6s  P-loop %-12s  VAIK %-8s  HRD %-8s  DFG@%s" % (
        sym,
        gly.group(0) if gly else '-',
        vaik.group(0) if vaik else '-',
        hrd.group(0) if hrd else '-',
        dfg.start() if dfg else '-'))

# gatekeeper: last residue of beta5, immediately N-terminal to the hinge.
# locate by aligning to MAP4K4 whose gatekeeper (Met104 in full-length) is known.
print()
print("GATEKEEPER by alignment to MAP4K4 (gatekeeper Met, full-length M104):")
m4k4 = dom('M4K4')
gk_full = 104
gk_idx = gk_full - KD['M4K4'][0]        # index within the M4K4 kinase domain
aln = aligner.align(nrk, m4k4)[0]
A, B = str(aln[0]), str(aln[1])
bi = -1
for i, (x, y) in enumerate(zip(A, B)):
    if y != '-':
        bi += 1
        if bi == gk_idx:
            ai = sum(1 for z in A[:i] if z != '-')
            print("  MAP4K4 gatekeeper %s  <->  NRK %s  (NRK kinase-domain pos %d, full-length %d)"
                  % (y, x, ai + 1, ai + KD['NRK'][0]))
            print("  MAP4K4 context: %s" % B[max(0, i-6):i+7].replace('-', ''))
            print("  NRK    context: %s" % A[max(0, i-6):i+7].replace('-', ''))
            break
