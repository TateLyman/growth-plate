"""Zn coordination sites in the TET2 catalytic domain, and whether TET1 conserves them.

Rationale: Au(I) drugs are zinc ejectors (Nat/Chem lit; PARP-1 paper PMC12720219 shows
sodium aurothiomalate IC50 24.8 nM on PARP-1, which has Zn fingers, vs >uM on PARP-2,
which does not). If auranofin's ~206x functional TET1-over-TET2 selectivity has a
structural basis, it should show up as a difference in Cys-coordinated Zn sites.
"""
from Bio.PDB import MMCIFParser, NeighborSearch
from Bio.PDB.Polypeptide import protein_letters_3to1 as t31
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
import warnings, collections
warnings.filterwarnings('ignore')

st = MMCIFParser(QUIET=True).get_structure('x', '/home/user/gp_data/4nm6.cif')
model = st[0]
atoms = [a for a in model.get_atoms()]
ns = NeighborSearch(atoms)

metals = []
for res in model.get_residues():
    rn = res.get_resname().strip()
    if rn in ('ZN', 'FE2', 'FE'):
        metals.append(res)
print('metal ions found:', collections.Counter(r.get_resname().strip() for r in metals))
print()

# map: for each metal, coordinating protein residues within 3.0 A
seq_pos = {}
for m in metals:
    ion = list(m.get_atoms())[0]
    close = ns.search(ion.get_coord(), 3.0)
    partners = []
    for a in close:
        p = a.get_parent()
        if p is m:
            continue
        pn = p.get_resname().strip()
        if pn in ('HOH',):
            continue
        het, num, ic = p.get_id()
        if het.strip():          # ligand, not protein
            partners.append(('LIG', pn, num, a.get_id()))
        else:
            partners.append(('AA', pn, num, a.get_id()))
    aa = sorted(set((p[1], p[2]) for p in partners if p[0] == 'AA'), key=lambda x: x[1])
    lig = sorted(set((p[1], p[2]) for p in partners if p[0] == 'LIG'))
    print('%-4s %-6s chain %s  coordinated by: %s   %s' % (
        m.get_resname().strip(), m.get_id()[1], m.get_parent().id,
        ', '.join('%s%d' % (t31.get(n, n), i) for n, i in aa),
        ('+ligand ' + str(lig)) if lig else ''))
    seq_pos[(m.get_resname().strip(), m.get_id()[1])] = [i for n, i in aa if n == 'CYS']

print()
cys_all = sorted(set(i for v in seq_pos.values() for i in v))
print('TET2 residue numbers of ALL Zn/Fe-coordinating cysteines:', cys_all)
print('count of Cys in metal sites:', len(cys_all))

# ---- align TET1 vs TET2 full length, map those Cys ----
t1 = str(next(SeqIO.parse('/home/user/gp_data/tet1.fasta', 'fasta')).seq)
t2 = str(next(SeqIO.parse('/home/user/gp_data/tet2.fasta', 'fasta')).seq)
t3 = str(next(SeqIO.parse('/home/user/gp_data/tet3.fasta', 'fasta')).seq)
print('\nlengths TET1 %d TET2 %d TET3 %d' % (len(t1), len(t2), len(t3)))

al = PairwiseAligner()
al.substitution_matrix = substitution_matrices.load('BLOSUM62')
al.open_gap_score, al.extend_gap_score, al.mode = -11, -1, 'global'


def maprefs(ref, other, positions, label):
    a = al.align(ref, other)[0]
    # build index map ref->other
    m = {}
    ri = oi = 0
    A, B = a[0], a[1]
    for x, y in zip(A, B):
        if x != '-':
            ri += 1
        if y != '-':
            oi += 1
        if x != '-':
            m[ri] = (oi if y != '-' else None, y)
    print('\n%s: TET2 metal-Cys -> %s' % (label, label))
    cons = 0
    for p in positions:
        tgt = m.get(p)
        if tgt is None:
            print('   TET2 C%-5d -> (unaligned)' % p); continue
        oi_, ch = tgt
        ok = (ch == 'C')
        cons += ok
        print('   TET2 C%-5d -> %s %s%s' % (p, label, ch, ('' if oi_ is None else str(oi_))),
              'CONSERVED' if ok else '<-- DIVERGENT')
    print('   conserved %d/%d' % (cons, len(positions)))
    return cons


c1 = maprefs(t2, t1, cys_all, 'TET1')
c3 = maprefs(t2, t3, cys_all, 'TET3')

# ---- total cysteine content of the catalytic domains ----
# TET2 CD 1129-1936; TET1 CD 1418-2136; TET3 CD 697-1660 (UniProt/lit)
segs = {'TET1 CD 1418-2136': t1[1417:2136], 'TET2 CD 1129-1936': t2[1128:1936],
        'TET3 CD 697-1660': t3[696:1660],
        'TET1 CXXC 584-625': t1[583:625], 'TET3 CXXC 50-90': t3[49:90]}
print('\ncysteine content:')
for k, s in segs.items():
    print('   %-20s len %4d  Cys %3d  (%.2f%%)' % (k, len(s), s.count('C'), 100.0 * s.count('C') / len(s)))
