"""Calibrate the contact-set analysis against TWO independent empirical datasets:
  (a) R146's ChEMBL within-clade carry-over  (TNIK/MAP4K4/MINK1/MAP4K1)
  (b) the Promega patent's live-cell tracer fold-changes (MAP4K1/2/3/5 and NRK,
      SAME assay, SAME cells, SAME chemotype family -- a controlled comparison
      that a cross-lab ChEMBL aggregate can never be)
and then place NRK.
"""
from Bio.PDB import MMCIFParser, NeighborSearch
from Bio.PDB.Polypeptide import protein_letters_3to1 as t31
from Bio import SeqIO, Align
from Bio.Align import substitution_matrices
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

LIG = {'5d7a': '58C', '6ra7': 'JWK', '8zml': 'A1D8H', '5ax9': '4KT'}
CUT = 4.5
seqs = {}
for rec in SeqIO.parse('gck.fasta', 'fasta'):
    seqs[rec.description.split('|')[2].split('_')[0]] = str(rec.seq)
blosum = substitution_matrices.load("BLOSUM62")
al = Align.PairwiseAligner(); al.substitution_matrix = blosum
al.open_gap_score = -11; al.extend_gap_score = -1; al.mode = 'global'
NAME = {'M4K4':'MAP4K4','M4K1':'MAP4K1','M4K2':'MAP4K2','M4K3':'MAP4K3','M4K5':'MAP4K5'}
def nm(s): return NAME.get(s, s)

def mapper(q):
    aln = al.align(seqs['TNIK'], seqs[q])[0]
    A, B = str(aln[0]), str(aln[1]); ri = qi = -1; m = {}
    for x, y in zip(A, B):
        if x != '-': ri += 1
        if y != '-': qi += 1
        if x != '-': m[ri] = (y if y != '-' else '-')
    return m

par = MMCIFParser(QUIET=True); cnt = Counter()
for pdb, lc in LIG.items():
    st = par.get_structure(pdb, pdb + '.cif')[0]
    atoms = [a for a in st.get_atoms() if a.element != 'H']
    ligat = [a for a in atoms if a.get_parent().get_resname() == lc]
    ns = NeighborSearch([a for a in atoms if a.get_parent().id[0] == ' '])
    seen = set()
    for a in ligat:
        for b in ns.search(a.coord, CUT):
            r = b.get_parent()
            if r.get_resname() in t31: seen.add(r.id[1])
    for k in seen: cnt[k] += 1
core = sorted(k for k, v in cnt.items() if v >= 2)
tn = seqs['TNIK']

def contact_id(q):
    M = mapper(q)
    ident = cons = nonc = 0; ch = []
    for k in core:
        t_ = tn[k-1]; x = M.get(k-1, '-')
        if x == t_: ident += 1
        elif x != '-' and blosum[t_, x] > 0: cons += 1; ch.append("%s%d%s" % (t_, k, x))
        else: nonc += 1; ch.append("%s%d%s*" % (t_, k, x))
    return ident, cons, nonc, ch

print("=" * 104)
print("LIGAND-CONTACT SET FROM 4 TNIK INHIBITOR CO-CRYSTALS: %d core positions" % len(core))
print("  " + " ".join("%s%d" % (tn[k-1], k) for k in core))
print("=" * 104)

# R146 measured ChEMBL carry-over, and Promega tracer fold-changes (FIG 1E/1F)
CARRY = {'M4K4': 89, 'MINK1': 87, 'M4K1': 94}          # carry-over WITH TNIK (R146)
TRACER = {'M4K1': (3.94, 2.07, 2.58), 'M4K2': (7.03, 10.89, 1.97),
          'M4K3': (6.84, 3.45, 1.58), 'M4K5': (2.82, 1.74, 1.18),
          'NRK':  (1.51, 2.85, 1.09)}

print()
print("%-9s %7s %6s %6s %9s %10s  %s" % ("kinase", "ident", "cons", "NON-C", "%identical",
                                          "R146 carry", "substitutions at contact positions"))
print("-" * 118)
order = ['M4K4', 'MINK1', 'M4K1', 'M4K2', 'M4K3', 'M4K5', 'NRK']
res = {}
for q in order:
    i, c, n, ch = contact_id(q); res[q] = (i, c, n)
    print("%-9s %7d %6d %6d %9.1f%% %10s  %s"
          % (nm(q), i, c, n, 100*i/len(core),
             ("%d%%" % CARRY[q]) if q in CARRY else "-",
             ", ".join(ch) if ch else "(none -- contact set is IDENTICAL to TNIK)"))
print()
print("  * = non-conservative (BLOSUM62 <= 0)")

print()
print("=" * 104)
print("CALIBRATION (a) -- R146's 68-94% CARRY-OVER WAS MEASURED ON KINASES WITH IDENTICAL POCKETS")
print("=" * 104)
for q in ['M4K4', 'MINK1', 'M4K1']:
    i, c, n = res[q]
    print("  TNIK vs %-7s : %d/%d contact positions identical (%.0f%%) -> measured carry-over %d%%"
          % (nm(q), i, len(core), 100*i/len(core), CARRY[q]))
i, c, n = res['NRK']
print("  TNIK vs %-7s : %d/%d contact positions identical (%.0f%%) -> ??? "
      % ('NRK', i, len(core), 100*i/len(core)))
print()
print("  -> the base rate was derived from a set where THERE WAS NOTHING TO DISCRIMINATE.")
print("     Every calibration kinase has a 100%-identical ligand contact surface.")
print("     NRK does not. The 68-94%% number CANNOT be extended to it.")

print()
print("=" * 104)
print("CALIBRATION (b) -- DOES CONTACT IDENTITY PREDICT ACTUAL BINDING? (Promega, one assay, one lab)")
print("=" * 104)
print("%-9s %9s %8s %8s %8s %9s" % ("kinase", "%ident", "CC-1804", "CC-1817", "CC-1294", "sum"))
print("-" * 60)
rows = []
for q in ['M4K1', 'M4K2', 'M4K3', 'M4K5', 'NRK']:
    i, c, n = res[q]; t = TRACER[q]
    rows.append((100*i/len(core), sum(t), q))
    print("%-9s %8.1f%% %8.2f %8.2f %8.2f %9.2f" % (nm(q), 100*i/len(core), t[0], t[1], t[2], sum(t)))
rows.sort(reverse=True)
print()
print("  ranked by tracer binding (sum of fold-change):")
for r in sorted(rows, key=lambda x: -x[1]):
    print("     %-8s sum %6.2f   contact identity %.1f%%" % (nm(r[2]), r[1], r[0]))
try:
    import statistics
    xs = [r[0] for r in rows]; ys = [r[1] for r in rows]
    mx, my = statistics.mean(xs), statistics.mean(ys)
    num = sum((a-mx)*(b-my) for a, b in zip(xs, ys))
    den = (sum((a-mx)**2 for a in xs) * sum((b-my)**2 for b in ys)) ** 0.5
    print("\n  Pearson r (contact identity vs tracer binding, n=%d) = %.2f" % (len(xs), num/den))
except Exception as e:
    print(e)
