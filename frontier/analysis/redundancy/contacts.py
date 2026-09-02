"""STRUCTURE-BASED ESTIMATE OF f = IC50(TNIK)/IC50(NRK), WITHOUT AN EXPERIMENT.

NRK has ZERO PDB structures (Tdark). TNIK has 12, four of them with an ATP-site
inhibitor bound -- including 5D7A = TNIK + NCB-0846, a compound already in the panel.

Logic: an ATP-competitive inhibitor only "sees" the residues it touches. R147 found
NRK differs from TNIK at 7 ATP-pocket positions. The question that decides f is not
"how many differences" but "are the differences WHERE THE LIGAND ACTUALLY IS".
So: take the real contact residues from the real co-crystals, map them into NRK
through an alignment, and count how many contact positions are substituted.
"""
from Bio.PDB import MMCIFParser, NeighborSearch, Selection
from Bio.PDB.Polypeptide import protein_letters_3to1 as t31
from Bio import SeqIO, Align
from Bio.Align import substitution_matrices
import warnings, re
warnings.filterwarnings('ignore')

LIG = {'5d7a': ('58C', 'NCB-0846 (clinical-stage TNIK inhibitor)'),
       '6ra7': ('JWK', 'compound 9 (1.2 A resolution)'),
       '8zml': ('A1D8H', 'undisclosed TNIK inhibitor (2024)'),
       '5ax9': ('4KT', 'TNIK inhibitor')}
CUT = 4.5

seqs = {}
for rec in SeqIO.parse('gck.fasta', 'fasta'):
    seqs[rec.description.split('|')[2].split('_')[0]] = str(rec.seq)

blosum = substitution_matrices.load("BLOSUM62")
al = Align.PairwiseAligner(); al.substitution_matrix = blosum
al.open_gap_score = -11; al.extend_gap_score = -1; al.mode = 'global'

def map_TNIK_to(q):
    """TNIK UniProt index (0-based) -> residue in query kinase."""
    aln = al.align(seqs['TNIK'], seqs[q])[0]
    A, B = str(aln[0]), str(aln[1])
    ri = qi = -1; m = {}
    for x, y in zip(A, B):
        if x != '-': ri += 1
        if y != '-': qi += 1
        if x != '-': m[ri] = (y if y != '-' else '-')
    return m

M = {q: map_TNIK_to(q) for q in ['NRK', 'M4K4', 'MINK1', 'M4K1']}

par = MMCIFParser(QUIET=True)
allcon = {}
print("=" * 100)
print("STEP 1 -- REAL LIGAND CONTACTS FROM TNIK CO-CRYSTALS (heavy atoms within %.1f A)" % CUT)
print("=" * 100)
for pdb, (lc, desc) in LIG.items():
    st = par.get_structure(pdb, pdb + '.cif')[0]
    atoms = [a for a in st.get_atoms() if a.element != 'H']
    ligat = [a for a in atoms if a.get_parent().get_resname() == lc]
    if not ligat:
        print("%s: ligand %s not found" % (pdb, lc)); continue
    ns = NeighborSearch([a for a in atoms if a.get_parent().id[0] == ' '])
    con = {}
    for a in ligat:
        for b in ns.search(a.coord, CUT):
            r = b.get_parent()
            nm = r.get_resname()
            if nm in t31:
                con[r.id[1]] = t31[nm]
    allcon[pdb] = con
    print("\n%s  (%s)  ligand %s -- %d contact residues" % (pdb.upper(), desc, lc, len(con)))
    print("   " + " ".join("%s%d" % (con[k], k) for k in sorted(con)))

# ---- consensus contact set -------------------------------------------------
from collections import Counter
cnt = Counter()
for c in allcon.values():
    for k in c: cnt[k] += 1
core = sorted(k for k, v in cnt.items() if v >= 2)          # seen in >=2 structures
anyc = sorted(cnt)
print()
print("=" * 100)
print("STEP 2 -- MAP THE CONTACT RESIDUES INTO NRK THROUGH THE ALIGNMENT")
print("=" * 100)
print("Contacts seen in >=2 of the %d inhibitor complexes: %d positions" % (len(allcon), len(core)))
print()

# author numbering in these TNIK structures should == UniProt numbering; verify
tn = seqs['TNIK']
match = mismatch = 0
for k in anyc:
    obs = [c[k] for c in allcon.values() if k in c][0]
    if 0 < k <= len(tn) and tn[k-1] == obs: match += 1
    else: mismatch += 1
print("Numbering check vs UniProt Q9UKE5: %d/%d contact residues match the sequence at that index"
      % (match, match + mismatch))
print()

print("%-10s %-8s %-8s %-8s %-8s  %s" % ("TNIK pos", "TNIK", "NRK", "MAP4K4", "MINK1", "verdict"))
print("-" * 88)
diffs = []
for k in core:
    tres = tn[k-1]
    n = M['NRK'].get(k-1, '?'); m4 = M['M4K4'].get(k-1, '?'); mk = M['MINK1'].get(k-1, '?')
    same = (n == tres)
    cons = (not same and n in blosum.alphabet and tres in blosum.alphabet and blosum[tres, n] > 0)
    v = "identical" if same else ("CONSERVATIVE (BLOSUM %+d)" % blosum[tres, n] if cons
                                  else "*** NON-CONSERVATIVE (BLOSUM %+d) ***" % blosum[tres, n])
    if not same: diffs.append((k, tres, n, cons, m4, mk))
    print("%-10d %-8s %-8s %-8s %-8s  %s" % (k, tres, n, m4, mk, v))

print()
print("=" * 100)
print("STEP 3 -- THE ANSWER")
print("=" * 100)
print("Core ligand-contact positions          : %d" % len(core))
print("Identical between TNIK and NRK         : %d  (%.1f%%)" % (len(core)-len(diffs), 100*(len(core)-len(diffs))/len(core)))
print("Substituted in NRK                     : %d" % len(diffs))
if diffs:
    nc = [d for d in diffs if not d[3]]
    print("  of which CONSERVATIVE                : %d" % (len(diffs)-len(nc)))
    print("  of which NON-CONSERVATIVE            : %d" % len(nc))
    for k, t_, n_, c_, m4, mk in diffs:
        print("     TNIK %s%d -> NRK %s   (MAP4K4 %s, MINK1 %s)  %s"
              % (t_, k, n_, m4, mk, "conservative" if c_ else "NON-CONSERVATIVE"))
