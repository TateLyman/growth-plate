"""RIGOROUS TEST: does auranofin in vivo produce a coordinated MYC-target repression,
as Chen 2023's TET1 -> 5hmC -> c-Myc chain predicts? And is the canonical TrxR/NRF2
arm engaged at all? Genome-wide background, permutation-tested."""
import gzip, statistics as st, math, random
random.seed(0)

hdr=None; rows=[]
with gzip.open('gse202935.txt.gz','rt',errors='replace') as f:
    for l in f:
        p=l.rstrip('\n').split('\t')
        if hdr is None: hdr=p; continue
        rows.append(p)
gi={h:i for i,h in enumerate(hdr)}; NAME=gi['gene_name']
TIS={}
for h in hdr:
    if h.startswith(('iWAT','eWAT','liv','BAT')) and '_' in h:
        t,g=h.rsplit('_',1); TIS.setdefault(t,{'V':[],'AF':[]})
        TIS[t]['AF' if g.startswith('AF') else 'V'].append(gi[h])

# canonical MYC target genes (well-established, curated by hand from the classic set)
MYC=set("""Npm1 Ncl Nop56 Nop58 Fbl Rrs1 Bysl Ddx21 Gnl3 Pes1 Wdr43 Utp20 Polr1b Rrp9
Eif4e Eif4a1 Eif2s1 Rps5 Rps6 Rpl3 Rpl5 Rpl22 Rplp0 Srm Odc1 Cad Tk1 Rrm2 Pcna Mcm2 Mcm4
Mcm5 Mcm7 Cdk4 Ccnd2 Ldha Slc7a5 Slc19a1 Hspd1 Hspe1 Nme1 Ppat Prps2 Gart Impdh2 Trap1
Tfam Cct3 Cct7 Ranbp1 Xpo1 Sord Pgk1 Eno1 Tpi1""".split())
# canonical NRF2 / oxidative-stress targets
NRF2=set("""Nqo1 Hmox1 Gclc Gclm Txnrd1 Srxn1 Gsta3 Gstm1 Gstp1 Slc7a11 Prdx1 Cat Sod1
Gpx2 Ephx1 Ugt1a6a Akr1b8 Cbr3 Ftl1 Fth1 Me1 G6pdx Blvrb""".split())

def vals(p,idx):
    o=[]
    for i in idx:
        try: o.append(float(p[i]))
        except: o.append(0.0)
    return o

print("%-6s %28s %8s %8s %9s %9s %9s"%("tissue","set","n","medLFC","bgMedLFC","shift","perm p"))
print("-"*84)
for t in ['iWAT','eWAT','liv','BAT']:
    V,A=TIS[t]['V'],TIS[t]['AF']
    lfc={}
    for p in rows:
        n=p[NAME] if len(p)>NAME else ''
        if not n: continue
        v=vals(p,V); a=vals(p,A)
        mv,ma=st.mean(v),st.mean(a)
        if mv<1 and ma<1: continue          # expressed filter
        lfc[n]=math.log2((ma+0.1)/(mv+0.1))
    allv=list(lfc.values()); bg=st.median(allv)
    for lab,S in [("MYC targets (Chen's node)",MYC),("NRF2/oxidative (TrxR arm)",NRF2)]:
        sel=[lfc[g] for g in S if g in lfc]
        if len(sel)<8: print("%-6s %28s %8d  (too few detected)"%(t,lab,len(sel))); continue
        m=st.median(sel); obs=m-bg
        # permutation: random gene sets of same size
        cnt=0; N=2000
        keys=list(lfc)
        for _ in range(N):
            samp=[lfc[k] for k in random.sample(keys,len(sel))]
            if abs(st.median(samp)-bg)>=abs(obs): cnt+=1
        print("%-6s %28s %8d %8.3f %9.3f %9.3f %9.4f"%(t,lab,len(sel),m,bg,obs,(cnt+1)/(N+1)))
    print()
