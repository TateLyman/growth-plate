"""THE REFINEMENT THAT DECIDES IT.

contacts2.py showed NRK scores 17/23 contact identity -- IDENTICAL to MAP4K1, which
R146 measured carrying over from TNIK 94% of the time. So a bare count of contact
differences cannot condemn NRK. Two questions remain:

  Q1. WHICH substitutions are NRK-SPECIFIC (i.e. not shared with MAP4K1/2/3/5,
      which are empirically tolerated)?
  Q2. At those positions, does the ligand touch the SIDE CHAIN or only the BACKBONE?
      A hinge contact made through main-chain N/O is INDIFFERENT to the side chain,
      so the substitution is free. Only side-chain contacts can cost potency.

And for Gly->Ala, model the virtual CB and measure the actual clearance.
"""
from Bio.PDB import MMCIFParser, NeighborSearch
from Bio.PDB.Polypeptide import protein_letters_3to1 as t31
from Bio import SeqIO, Align
from Bio.Align import substitution_matrices
from collections import Counter, defaultdict
import numpy as np, warnings
warnings.filterwarnings('ignore')

LIG = {'5d7a': ('58C', 'NCB-0846'), '6ra7': ('JWK', 'compound 9'),
       '8zml': ('A1D8H', 'undisclosed 2024'), '5ax9': ('4KT', 'TNIK inhibitor')}
CUT = 4.5
MC = {'N', 'CA', 'C', 'O', 'OXT'}

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
M = {q: mapper(q) for q in ['NRK','M4K4','MINK1','M4K1','M4K2','M4K3','M4K5']}
tn = seqs['TNIK']

def virtual_CB(res):
    """standard CB placement from N, CA, C"""
    try:
        N, CA, C = res['N'].coord, res['CA'].coord, res['C'].coord
    except KeyError:
        return None
    b = CA - N; c = C - CA; a = np.cross(b, c)
    return -0.58273431*a + 0.56802827*b - 0.54067466*c + CA

par = MMCIFParser(QUIET=True)
mc_only = defaultdict(list)     # pos -> list of (pdb, min_mc_dist, min_sc_dist)
cnt = Counter()
gly_clear = defaultdict(list)

for pdb, (lc, label) in LIG.items():
    st = par.get_structure(pdb, pdb + '.cif')[0]
    heavy = [a for a in st.get_atoms() if a.element != 'H']
    ligat = [a for a in heavy if a.get_parent().get_resname() == lc]
    prot = [a for a in heavy if a.get_parent().id[0] == ' ']
    ns = NeighborSearch(prot)
    touched = set()
    for a in ligat:
        for b in ns.search(a.coord, CUT):
            r = b.get_parent()
            if r.get_resname() in t31: touched.add(r.id[1])
    L = np.array([a.coord for a in ligat])
    for pos in touched:
        cnt[pos] += 1
        res = [r for r in st.get_residues() if r.id[1] == pos and r.get_resname() in t31]
        if not res: continue
        res = res[0]
        dmc = dsc = 9e9
        for at in res:
            if at.element == 'H': continue
            d = float(np.min(np.linalg.norm(L - at.coord, axis=1)))
            if at.get_id() in MC: dmc = min(dmc, d)
            else: dsc = min(dsc, d)
        mc_only[pos].append((pdb, dmc, dsc))
        if res.get_resname() == 'GLY':
            cb = virtual_CB(res)
            if cb is not None:
                gly_clear[pos].append((pdb, float(np.min(np.linalg.norm(L - cb, axis=1)))))

core = sorted(k for k, v in cnt.items() if v >= 2)

print("=" * 104)
print("Q1 -- WHICH CONTACT SUBSTITUTIONS ARE ACTUALLY NRK-SPECIFIC?")
print("=" * 104)
group = ['M4K1', 'M4K2', 'M4K3', 'M4K5']
print("%-8s %-6s %-6s %-34s %s" % ("TNIKpos", "TNIK", "NRK", "MAP4K1/2/3/5 at same position", "class"))
print("-" * 104)
nrk_specific = []
for k in core:
    t_ = tn[k-1]; n_ = M['NRK'].get(k-1, '-')
    if n_ == t_: continue
    others = [M[g].get(k-1, '-') for g in group]
    shared = any(o != t_ for o in others)
    cons = blosum[t_, n_] > 0
    if shared:
        cl = "shared with the tolerated MAP4Ks -> NOT evidence against NRK"
    else:
        cl = "*** NRK-SPECIFIC ***"
        nrk_specific.append(k)
    print("%-8d %-6s %-6s %-34s %s" % (k, t_, n_,
          " ".join("%s:%s" % (nm(g)[-1], o) for g, o in zip(group, others)),
          cl + ("" if cons else "  [non-conservative]")))

print()
print("  -> NRK-SPECIFIC contact substitutions: %s"
      % (", ".join("%s%d%s" % (tn[k-1], k, M['NRK'][k-1]) for k in nrk_specific) or "NONE"))
print("  -> everything else NRK does at the contact surface is ALSO done by MAP4K1,")
print("     which R146 measured carrying over from TNIK 94%% of the time.")

print()
print("=" * 104)
print("Q2 -- AT THOSE POSITIONS, DOES THE LIGAND TOUCH THE SIDE CHAIN OR ONLY THE BACKBONE?")
print("=" * 104)
print("%-8s %-6s %-14s %-14s %s" % ("pos", "TNIK", "min MC dist", "min SC dist", "interpretation"))
print("-" * 104)
for k in core:
    if k not in nrk_specific and not (tn[k-1] != M['NRK'].get(k-1)): continue
    rows = mc_only[k]
    if not rows: continue
    dmc = min(r[1] for r in rows); dsc = min(r[2] for r in rows)
    if dsc > 90:  interp = "GLYCINE -- no side chain at all"
    elif dsc > CUT: interp = "BACKBONE-ONLY contact -> side chain is INVISIBLE to the ligand"
    elif dsc < dmc: interp = "*** SIDE-CHAIN contact, and it is the CLOSER one ***"
    else: interp = "side chain within range but backbone closer"
    star = " <<<" if k in nrk_specific else ""
    print("%-8d %-6s %-14s %-14s %s%s" % (k, tn[k-1],
          "%.2f A" % dmc, ("%.2f A" % dsc) if dsc < 90 else "n/a",
          interp, star))

if gly_clear:
    print()
    print("=" * 104)
    print("Q3 -- GLY->ALA: MODEL THE VIRTUAL CB AND MEASURE REAL CLEARANCE TO THE LIGAND")
    print("=" * 104)
    for k in sorted(gly_clear):
        if tn[k-1] != 'G': continue
        vals = gly_clear[k]
        mind = min(v[1] for v in vals)
        nrkres = M['NRK'].get(k-1, '-')
        tag = ("  <-- NRK has %s here" % nrkres) if nrkres != 'G' else ""
        if mind < 3.2:   verdict = "*** CLASH -- Gly->Ala would cost potency ***"
        elif mind < 3.7: verdict = "tight, mild penalty plausible"
        else:            verdict = "CLEARANCE FINE -- a methyl fits without clashing"
        print("  G%-5d virtual CB min distance to ligand = %.2f A   %s%s"
              % (k, mind, verdict, tag))
        print("        per structure: " + ", ".join("%s %.2f" % (p, d) for p, d in vals))
