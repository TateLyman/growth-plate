"""WHICH HUMAN KINASES HAVE AN NRK-LIKE ATP POCKET?

R151's lesson: clade membership does NOT predict potency (rentosertib lost 8.9x on a
paralog with a 100% identical contact surface). So stop asking "what is near NRK on
the kinome tree" and ask "what has NRK's actual ligand-contact residues" -- across all
480 human protein kinases, not just the GCK-IV clade.

Reference frame = the 23 ligand-contact positions derived in R150 from four TNIK
inhibitor co-crystals (5D7A/NCB-0846, 6RA7, 8ZML, 5AX9). Map them into every human
kinase by local alignment, then rank by similarity TO NRK.

Why this is the right question: if a WELL-DRUGGED kinase carries NRK's contact
signature, then compounds built against it are the ones most likely to fit NRK.
"""
from Bio import SeqIO, Align
from Bio.Align import substitution_matrices
import warnings; warnings.filterwarnings('ignore')

CONTACT = [31,32,33,34,39,52,54,69,83,105,106,107,108,109,110,111,112,115,157,158,160,170,171]
KD = (25, 289)

seqs = {}
for rec in SeqIO.parse('gck.fasta', 'fasta'):
    seqs[rec.description.split('|')[2].split('_')[0]] = str(rec.seq)
TNIK = seqs['TNIK']
ref = TNIK[KD[0]-1:KD[1]]
refpos = [k - KD[0] for k in CONTACT]          # index within ref

blosum = substitution_matrices.load("BLOSUM62")
loc = Align.PairwiseAligner(); loc.substitution_matrix = blosum
loc.open_gap_score = -11; loc.extend_gap_score = -1; loc.mode = 'local'

def pocket_of(seq):
    try:
        aln = loc.align(ref, seq)[0]
    except Exception:
        return None
    A, B = str(aln[0]), str(aln[1])
    # local alignment: find where ref starts in the alignment
    ri = aln.aligned[0][0][0] - 1
    qi = aln.aligned[1][0][0] - 1
    m = {}
    for x, y in zip(A, B):
        if x != '-': ri += 1
        if y != '-': qi += 1
        if x != '-': m[ri] = (y if y != '-' else '-')
    return ''.join(m.get(i, '-') for i in refpos)

# reference pockets
P_TNIK = ''.join(ref[i] for i in refpos)
P_NRK = pocket_of(seqs['NRK'])
print("contact frame (23 positions, TNIK numbering):")
print("  " + " ".join("%s%d" % (TNIK[k-1], k) for k in CONTACT))
print("  TNIK  %s" % P_TNIK)
print("  NRK   %s" % P_NRK)
print("  diff  %s" % ''.join(' ' if a == b else '^' for a, b in zip(P_TNIK, P_NRK)))
print()

rows = []
for rec in SeqIO.parse('kinome.fasta', 'fasta'):
    gn = None
    for part in rec.description.split():
        if part.startswith('GN='): gn = part[3:]
    if not gn: gn = rec.id.split('|')[1]
    p = pocket_of(str(rec.seq))
    if not p or p.count('-') > 4: continue
    ok = [(a, b) for a, b in zip(P_NRK, p) if a != '-' and b != '-']
    if not ok: continue
    idn = 100.0 * sum(1 for a, b in ok if a == b) / len(ok)
    smn = 100.0 * sum(1 for a, b in ok if blosum[a, b] > 0) / len(ok)
    okt = [(a, b) for a, b in zip(P_TNIK, p) if a != '-' and b != '-']
    idt = 100.0 * sum(1 for a, b in okt if a == b) / len(okt)
    rows.append((idn, smn, idt, gn, p))

rows.sort(reverse=True)
print("=" * 104)
print("HUMAN KINASES RANKED BY ATP-CONTACT-SET IDENTITY TO **NRK**  (n=%d aligned)" % len(rows))
print("=" * 104)
print("%-5s %-11s %8s %8s %10s  %s" % ("rank", "kinase", "%id NRK", "%sim NRK", "%id TNIK", "contact residues"))
print("-" * 104)
for i, (idn, smn, idt, gn, p) in enumerate(rows[:40], 1):
    mark = " <<< NRK" if gn == 'NRK' else ""
    print("%-5d %-11s %7.1f%% %7.1f%% %9.1f%%  %s%s" % (i, gn, idn, smn, idt, p, mark))

print()
print("where NRK's own clade sits:")
for want in ['NRK','TNIK','MINK1','MAP4K4','MAP4K1','MAP4K2','MAP4K3','MAP4K5','MAP4K6','STK24','STK25','STK26','SLK','STK10','OXSR1','STK39','PAK4','PAK1']:
    for i, (idn, smn, idt, gn, p) in enumerate(rows, 1):
        if gn == want:
            print("   #%-4d %-9s %.1f%% identical to NRK   (%.1f%% to TNIK)" % (i, gn, idn, idt)); break
