"""Cysteine divergence between TET1-CD and TET2-CD.

R150/R151 logic applied to our own lead arm: if the Cys surfaces that a soft
Au(I) electrophile could attack are identical between paralogs, there is nothing
for the drug to discriminate on, and carry-over is the DEFAULT expectation.
"""
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import MMCIFParser, ShrakeRupley
import warnings
warnings.filterwarnings('ignore')

t1 = str(next(SeqIO.parse('/home/user/gp_data/tet1.fasta', 'fasta')).seq)
t2 = str(next(SeqIO.parse('/home/user/gp_data/tet2.fasta', 'fasta')).seq)
t3 = str(next(SeqIO.parse('/home/user/gp_data/tet3.fasta', 'fasta')).seq)

al = PairwiseAligner()
al.substitution_matrix = substitution_matrices.load('BLOSUM62')
al.open_gap_score, al.extend_gap_score, al.mode = -11, -1, 'global'

a = al.align(t1, t2)[0]
A, B = a[0], a[1]
i1 = i2 = 0
pairs = []
for x, y in zip(A, B):
    if x != '-':
        i1 += 1
    if y != '-':
        i2 += 1
    pairs.append((i1 if x != '-' else None, x, i2 if y != '-' else None, y))

# TET1 CD 1418-2136, TET2 CD 1129-1936
cd1 = [p for p in pairs if p[0] and 1418 <= p[0] <= 2136]
tot = len(cd1)
ident = sum(1 for p in cd1 if p[1] == p[3])
print('TET1-CD vs TET2-CD over %d aligned columns: %.1f%% identity' % (tot, 100.0 * ident / tot))
print()

c_both, c_only1, c_only2 = [], [], []
for p in cd1:
    if p[1] == 'C' and p[3] == 'C':
        c_both.append(p)
    elif p[1] == 'C':
        c_only1.append(p)
    elif p[3] == 'C':
        c_only2.append(p)

print('Cys in TET1-CD conserved as Cys in TET2 : %d' % len(c_both))
print('Cys UNIQUE to TET1-CD (TET2 has other)  : %d' % len(c_only1))
for p in c_only1:
    print('     TET1 C%-5d  <->  TET2 %s%s' % (p[0], p[3], p[2] if p[2] else '-'))
print('Cys UNIQUE to TET2-CD (TET1 has other)  : %d' % len(c_only2))
for p in c_only2:
    print('     TET2 C%-5d  <->  TET1 %s%s' % (p[2], p[1], p[0] if p[0] else '-'))

# same for TET3
a3 = al.align(t1, t3)[0]
i1 = i3 = 0
p3 = []
for x, y in zip(a3[0], a3[1]):
    if x != '-':
        i1 += 1
    if y != '-':
        i3 += 1
    p3.append((i1 if x != '-' else None, x, i3 if y != '-' else None, y))
cd3 = [p for p in p3 if p[0] and 1418 <= p[0] <= 2136]
u1 = [p for p in cd3 if p[1] == 'C' and p[3] != 'C']
print('\nCys UNIQUE to TET1-CD vs TET3-CD        : %d' % len(u1))
for p in u1:
    print('     TET1 C%-5d  <->  TET3 %s%s' % (p[0], p[3], p[2] if p[2] else '-'))

# solvent accessibility of the 9 metal cysteines + all Cys in the TET2 structure
print('\n--- solvent accessibility of Cys in the TET2-CD crystal (4NM6, chain A) ---')
st = MMCIFParser(QUIET=True).get_structure('x', '/home/user/gp_data/4nm6.cif')
ch = st[0]['A']
sr = ShrakeRupley()
prot = [r for r in ch if r.get_id()[0] == ' ']


class _S:
    def __init__(self, rs): self.rs = rs
    def get_residues(self): return iter(self.rs)


sr.compute(st[0]['A'], level='R')
metal_cys = {1133, 1135, 1193, 1221, 1271, 1273, 1289, 1298, 1358}
buried = exposed = 0
for r in prot:
    if r.get_resname().strip() == 'CYS':
        sasa = getattr(r, 'sasa', None)
        if sasa is None:
            continue
        tag = 'METAL-SITE' if r.get_id()[1] in metal_cys else ''
        st8 = 'exposed' if sasa > 10 else 'buried'
        if st8 == 'buried':
            buried += 1
        else:
            exposed += 1
        print('   Cys%-5d SASA %6.1f A^2  %-8s %s' % (r.get_id()[1], sasa, st8, tag))
print('   buried %d / exposed %d' % (buried, exposed))
