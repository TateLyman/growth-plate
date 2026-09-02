"""IS THERE A TET-INHIBITION SIGNATURE IN AURANOFIN-TREATED MICE, IN VIVO?

GSE202935: 4 tissues (iWAT, eWAT, liver, BAT), vehicle vs auranofin, n=4 each.
Nobody has asked this dataset the TET question.

THE DISCRIMINATING TEST. Auranofin has two candidate mechanisms:
  (A) canonical: TrxR (Txnrd1) inhibition -> oxidative stress -> NRF2 target genes UP
  (B) our arm:   TET1 inhibition -> 5hmC loss -> c-Myc DOWN  (Chen 2023's exact chain,
      derived independently in T-ALL: "epigenetically reprogramed the expression of
      oncogene c-Myc ... through the TET1/5hmC/c-Myc signaling pathway")
If ONLY (A) appears, the TET arm is not engaged at this dose in vivo.
If (B) appears too, that is indirect in vivo evidence for the TET1 arm.
"""
import gzip, statistics as st, math

rows=[]; hdr=None
with gzip.open('gse202935.txt.gz','rt',errors='replace') as f:
    for l in f:
        p=l.rstrip('\n').split('\t')
        if hdr is None: hdr=p; continue
        rows.append(p)
gi={h:i for i,h in enumerate(hdr)}
NAME=gi['gene_name']
TIS={}
for h in hdr:
    if '_' in h and (h.startswith(('iWAT','eWAT','liv','BAT'))):
        t,g=h.rsplit('_',1)
        TIS.setdefault(t,{'V':[],'AF':[]})
        TIS[t]['AF' if g.startswith('AF') else 'V'].append(gi[h])
print("tissues / n:", {k:(len(v['V']),len(v['AF'])) for k,v in TIS.items()})

byname={}
for p in rows:
    n=p[NAME] if len(p)>NAME else ''
    if n: byname.setdefault(n,[]).append(p)

def vals(p,idx):
    out=[]
    for i in idx:
        try: out.append(float(p[i]))
        except: out.append(0.0)
    return out

def welch(a,b):
    na,nb=len(a),len(b)
    if na<2 or nb<2: return None
    ma,mb=st.mean(a),st.mean(b)
    va,vb=st.variance(a),st.variance(b)
    se=math.sqrt(va/na+vb/nb)
    if se==0: return None
    return (mb-ma)/se

def report(genes,label):
    print("\n"+"="*104); print(label); print("="*104)
    print("%-10s %-8s %10s %10s %8s %7s"%("gene","tissue","vehicle","auranofin","log2FC","t"))
    print("-"*62)
    agg={}
    for g in genes:
        if g not in byname: 
            print("%-10s (not found)"%g); continue
        p=max(byname[g],key=lambda r: sum(vals(r,TIS['iWAT']['V']+TIS['iWAT']['AF'])))
        for t in ['iWAT','eWAT','liv','BAT']:
            v=vals(p,TIS[t]['V']); a=vals(p,TIS[t]['AF'])
            mv,ma=st.mean(v),st.mean(a)
            if mv<0.5 and ma<0.5: continue
            lfc=math.log2((ma+0.1)/(mv+0.1))
            tt=welch(v,a)
            agg.setdefault(g,[]).append(lfc)
            print("%-10s %-8s %10.2f %10.2f %8.2f %7s"%(g,t,mv,ma,lfc,('%.2f'%tt) if tt is not None else '-'))
    return agg

# ---- positive control: the paper's own headline ----
report(['Lep'],"POSITIVE CONTROL — the paper's own finding (leptin should FALL)")

# ---- arm A: canonical TrxR / NRF2 ----
A=report(['Txnrd1','Nqo1','Hmox1','Gclc','Gclm','Srxn1','Gsta3','Slc7a11'],
         "ARM A — canonical TrxR/NRF2 oxidative-stress response (expected UP if drug is active)")

# ---- arm B: the TET1 -> 5hmC -> c-Myc chain (Chen 2023) ----
B=report(['Myc'],"ARM B — c-Myc, the exact node Chen 2023 says TET1 inhibition represses")

# ---- machinery ----
report(['Tet1','Tet2','Tet3','Dnmt1','Dnmt3a','Dnmt3b','Uhrf1','Idh1','Idh2'],
       "THE METHYLATION MACHINERY ITSELF")

print("\n"+"="*104)
print("SUMMARY OF DIRECTIONS (mean log2FC across tissues)")
print("="*104)
for lab,d in [("ARM A (NRF2/TrxR)",A),("ARM B (c-Myc)",B)]:
    print(" ",lab)
    for g,l in d.items():
        print("    %-10s mean log2FC = %+.3f  (n tissues=%d)"%(g,sum(l)/len(l),len(l)))
