"""How many human kinases carry a cysteine at the position equivalent to TNIK Cys108?
NRK conserves it (verified in the design-spec check). A pocket cysteine is a COVALENT
drug handle -- and covalent inhibitors do not obey the affinity rules that killed
rentosertib, because occupancy accumulates with time rather than tracking Kd."""
from Bio import SeqIO, Align
from Bio.Align import substitution_matrices
import warnings; warnings.filterwarnings('ignore')
CONTACT=[31,32,33,34,39,52,54,69,83,105,106,107,108,109,110,111,112,115,157,158,160,170,171]
I105, I107, I108 = CONTACT.index(105), CONTACT.index(107), CONTACT.index(108)
KD=(25,289)
seqs={}
for r in SeqIO.parse('gck.fasta','fasta'): seqs[r.description.split('|')[2].split('_')[0]]=str(r.seq)
ref=seqs['TNIK'][KD[0]-1:KD[1]]; refpos=[k-KD[0] for k in CONTACT]
bl=substitution_matrices.load("BLOSUM62")
loc=Align.PairwiseAligner(); loc.substitution_matrix=bl; loc.open_gap_score=-11; loc.extend_gap_score=-1; loc.mode='local'
def pocket(s):
    try: a=loc.align(ref,s)[0]
    except Exception: return None
    A,B=str(a[0]),str(a[1]); ri=a.aligned[0][0][0]-1; qi=a.aligned[1][0][0]-1; m={}
    for x,y in zip(A,B):
        if x!='-': ri+=1
        if y!='-': qi+=1
        if x!='-': m[ri]= y if y!='-' else '-'
    return ''.join(m.get(i,'-') for i in refpos)
cys=[]; tot=0
for rec in SeqIO.parse('kinome.fasta','fasta'):
    gn=[p[3:] for p in rec.description.split() if p.startswith('GN=')]
    gn=gn[0] if gn else rec.id
    p=pocket(str(rec.seq))
    if not p or p.count('-')>4: continue
    tot+=1
    if p[I108]=='C': cys.append((gn,p[I105],p[I107],p))
print("human kinases aligned: %d"%tot)
print("KINASES WITH CYSTEINE AT THE TNIK-Cys108 POSITION (gatekeeper+3, third hinge residue): %d"%len(cys))
print()
print("%-12s %-12s %-12s %s"%("kinase","gatekeeper","pos107","contact set"))
print("-"*74)
for gn,gk,f107,p in sorted(cys): print("%-12s %-12s %-12s %s"%(gn,gk,f107,p))
print()
print("  -> %.1f%% of the human kinome (%d of %d)"%(100.0*len(cys)/tot,len(cys),tot))
