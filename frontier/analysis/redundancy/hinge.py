"""Rank the human kinome by identity to NRK over the GATEKEEPER+HINGE block only
(TNIK positions 105-112), the region that dominates ATP-competitive recognition.
Whole-pocket identity treats a P-loop tip and the hinge as equal; they are not."""
from Bio import SeqIO, Align
from Bio.Align import substitution_matrices
import warnings; warnings.filterwarnings('ignore')
CONTACT=[31,32,33,34,39,52,54,69,83,105,106,107,108,109,110,111,112,115,157,158,160,170,171]
HB=[CONTACT.index(k) for k in [105,106,107,108,109,110,111,112]]
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
P={}
for r in SeqIO.parse('kinome.fasta','fasta'):
    gn=[p[3:] for p in r.description.split() if p.startswith('GN=')]
    gn=gn[0] if gn else r.id
    p=pocket(str(r.seq))
    if p and p.count('-')<=4: P[gn]=p
def hb(p): return ''.join(p[i] for i in HB)
NH=hb(P['NRK']); TH=hb(P['TNIK'])
print("gatekeeper+hinge block, TNIK positions 105-112")
print("   NRK   %s"%NH)
print("   TNIK  %s   (differs at 107: F vs L)"%TH)
print()
rows=[]
for gn,p in P.items():
    h=hb(p)
    ok=[(a,b) for a,b in zip(NH,h) if a!='-' and b!='-']
    if len(ok)<6: continue
    i=100.0*sum(1 for a,b in ok if a==b)/len(ok)
    rows.append((i,gn,h,p))
rows.sort(reverse=True)
print("="*88)
print("RANKED BY GATEKEEPER+HINGE IDENTITY TO NRK")
print("="*88)
print("%-5s %-11s %-11s %8s  %s"%("rank","kinase","hinge block","%id","full contact set"))
print("-"*88)
for n,(i,gn,h,p) in enumerate(rows[:28],1):
    m=" <<< NRK" if gn=='NRK' else ""
    print("%-5d %-11s %-11s %7.1f%%  %s%s"%(n,gn,h,i,p,m))
print()
print("kinases sharing NRK's EXACT hinge block %s:"%NH)
print("   "+", ".join(sorted(gn for i,gn,h,p in rows if h==NH)))
