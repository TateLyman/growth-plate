#!/usr/bin/env python3
"""Test EXTERNALLY DERIVED, PRE-SPECIFIED gene modules against the human growth
plate clusters. Nothing here was chosen by looking at this data.

WHY. reservoir_v2 showed the human stromal population beside the plate is
Hedgehog-negative. That killed GLI1 as a handle but said nothing about what the
right handle is. The mouse literature names four other stem markers and one
niche module, each from a primary lineage-tracing paper, and none of them has
been looked at in human tissue:

  PTHLH   resting-zone stem cells      Mizuhashi 2018 Nature      PMID 30401834
  NT5E    resting-zone stem (post-SOC) Newton 2019 Nature         PMID 30814736
  AXIN2   groove of Ranvier, Wnt-resp. Usami 2019 JBMR            PMID 30602070
  FOXA2   upper RZ / SOC boundary      Muruganandan 2022 Nat Comm PMID 35523895
  APOE    resting zone pan-marker      Kodama 2025 Bone Research  PMID 40025030

  WNT-INHIBITORY NICHE MODULE of the mouse resting zone, Hallett 2021 eLife
  (PMID 34309509): SFRP1, SFRP5, DKK2, WIF1, NOTUM, FZD6.

  EVERY PMID ABOVE WAS VERIFIED AGAINST THE PRIMARY RECORD. Three of them were
  initially wrong - taken from a review's citation table through a summarisation
  step - and pointed at a MYCN paper, an electroconvulsive-therapy study and a
  mosquito-ecology paper. See CORR-023.

TWO PRE-DECLARED PREDICTIONS, written before the numbers were read:
  P1 If the human resting zone is the same niche as the mouse one, the clusters
     identified as resting zone BY MARKERS OUTSIDE THE MODULE will carry the
     Wnt-inhibitory module at higher levels than other chondrocyte clusters.
  P2 If the human stromal population beside the plate is the groove-of-Ranvier
     counterpart, it will be AXIN2-positive - Wnt-RESPONSIVE - even though it is
     Hedgehog-negative. AXIN2 is the specific handle this predicts.

NO CIRCULARITY. Resting-zone clusters are identified by PTHLH and CHRDL2 only.
SFRP5 is a member of the tested module AND the marker avijgan2026br used to call
the human resting zone, so it is EXCLUDED from the identification step and
reported separately.

GUARDS, declared before the result is read:
  G0 Per-donor ambient reference, as CORR-021. A donor is judged only if it has
     >= 30 immune cells; donor3 has 9 and is dropped.
  G1 A gene is REPORTED ONLY IF it clears 50 pooled counts across the compared
     groups. Below that the comparison is not made and the gene is listed as
     below floor. This is the CORR-019 rule.
  G2 The resting-zone call must succeed on its own markers: at least one
     chondrocyte cluster must carry PTHLH or CHRDL2 above 50 pooled counts. If
     not, P1 is untestable and is reported as untestable, not as negative.
"""
import sys, os, json
import numpy as np, pandas as pd, scanpy as sc, anndata as ad, scipy.sparse as sp

D=sys.argv[1]; CL=sys.argv[2]
OUT=sys.argv[3] if len(sys.argv)>3 else "/home/user/growth-plate/query/stem_module_human.json"
FRESH={"GSM9328218_P30453_1001.h5":"donor1","GSM9328221_P31011_1001.h5":"donor2",
       "GSM9328224_P25452_001.h5":"donor3","GSM9328229_P22202_1015.h5":"donor4"}
WNT_MODULE=["SFRP1","DKK2","WIF1","NOTUM","FZD6"]      # SFRP5 held out, see above
STEM=["PTHLH","NT5E","AXIN2","FOXA2","APOE"]
IDENT=["PTHLH","CHRDL2"]
EXTRA=["SFRP5","GLI1","PTCH1","COL2A1","COL1A1","PTPRC","ACAN","MKI67","LGR5","TCF7","NKD1","RSPO2","RSPO3","WNT5A","WNT5B"]

cl=pd.read_csv(CL,index_col=0); ads=[]
for fn,dn in FRESH.items():
    a=sc.read_10x_h5(os.path.join(D,fn)); a.var_names_make_unique()
    a.obs_names=[f"{dn}_{b}" for b in a.obs_names]; ads.append(a)
A=ad.concat(ads,join="outer"); A.var_names_make_unique()
A=A[cl.index].copy()
A.obs["leiden"]=cl["leiden"].astype(str).values; A.obs["donor"]=cl["donor"].values
LE=A.obs.leiden.values; DO=A.obs.donor.values
cls=sorted(set(LE),key=int)
PRESENT={g:(g in A.var_names) for g in WNT_MODULE+STEM+IDENT+EXTRA}
absent=[g for g,v in PRESENT.items() if not v]
print(f"GENES NOT IN THE MATRIX (their zeros mean nothing): {absent if absent else 'none'}\n")

def vec(mask,g):
    if g not in A.var_names: return None
    m=A[mask,g].X
    return np.asarray(m.todense()).ravel() if sp.issparse(m) else np.asarray(m).ravel()
def mn(mask,g):
    v=vec(mask,g); return float(v.mean()) if v is not None and len(v) else float("nan")
def ct(mask,g):
    v=vec(mask,g); return int(v.sum()) if v is not None and len(v) else 0

immune=[c for c in cls if (lambda v: v is not None and (v>0).mean()>=0.85 and v.mean()>=3)(vec(LE==c,"PTPRC"))]
imm_mask=np.isin(LE,immune)
keep=[d for d in sorted(set(DO)) if int((imm_mask&(DO==d)).sum())>=30]
print(f"G0 retained donors {keep}; dropped {[d for d in sorted(set(DO)) if d not in keep]} (ambient floor not measurable)")
K=np.isin(DO,keep)
amb=float(np.mean([mn(imm_mask&(DO==d),"COL2A1") for d in keep]))

CHTHR=100*amb   # CORR-022: ambient-referenced, NOT an absolute count. A >=500
                # absolute cutoff excluded the RESTING ZONE by construction -
                # avijgan2026br report the resting zone has the LOWEST mRNA
                # content of any zone, so an absolute COL2A1 bar deletes the
                # one compartment this analysis is about.
chond=[c for c in cls if mn((LE==c)&K,"COL2A1")>=CHTHR and int(((LE==c)&K).sum())>=20]
stromal=[c for c in cls if mn((LE==c)&K,"COL1A1")>=5 and (lambda v:(v>0).mean()>=.40)(vec((LE==c)&K,"PDGFRA"))
         and (lambda v:(v>0).mean()<.40)(vec((LE==c)&K,"PTPRC")) and mn((LE==c)&K,"COL2A1")<=5*amb]
print(f"chondrocyte clusters (COL2A1 >= {CHTHR:.0f} = 100x ambient) {chond}; stromal {stromal}\n")

# ---- G2 / P1: identify resting zone on PTHLH + CHRDL2 ONLY ----
print("RESTING-ZONE IDENTIFICATION (independent markers only: PTHLH, CHRDL2)")
print(f"{'cl':>4}{'n':>7}{'PTHLH mn':>10}{'PTHLH ct':>10}{'CHRDL2 mn':>11}{'CHRDL2 ct':>11}{'SFRP5 mn':>10}")
idcounts={}
for c in chond:
    m=(LE==c)&K
    idcounts[c]=ct(m,"PTHLH")+ct(m,"CHRDL2")
    print(f"{c:>4}{int(m.sum()):>7}{mn(m,'PTHLH'):>10.3f}{ct(m,'PTHLH'):>10}{mn(m,'CHRDL2'):>11.3f}{ct(m,'CHRDL2'):>11}{mn(m,'SFRP5'):>10.3f}")
if max(idcounts.values(), default=0) < 50:
    print("\nG2 FAILED: no chondrocyte cluster clears 50 pooled counts on PTHLH/CHRDL2.")
    print("P1 IS UNTESTABLE ON THIS DATA and is NOT reported as negative."); rz=[]; p1="untestable"
else:
    thr=max(idcounts.values())
    rz=[c for c in chond if idcounts[c]>=0.5*thr and idcounts[c]>=50]
    other=[c for c in chond if c not in rz]
    print(f"\nRESTING-ZONE clusters {rz}; other chondrocyte clusters {other}")
    print("\nP1 — WNT-INHIBITORY MODULE (Hallett 2021), resting zone vs other chondrocytes")
    print(f"{'gene':<8}{'RZ mean':>10}{'other mean':>12}{'ratio':>8}{'pooled cts':>12}   status")
    p1rows={}
    hits=0; tested=0
    for g in WNT_MODULE+["SFRP5"]:
        rzm=mn(np.isin(LE,rz)&K,g); om=mn(np.isin(LE,other)&K,g)
        tot=ct(np.isin(LE,rz)&K,g)+ct(np.isin(LE,other)&K,g)
        if not PRESENT[g]: st="NOT IN MATRIX"
        elif tot<50: st="below 50-count floor - not compared"
        else:
            r=rzm/om if om>0 else float("inf")
            st=f"ratio {r:.2f}"
            if g in WNT_MODULE:
                tested+=1
                if r>=1.5: hits+=1
        p1rows[g]=dict(rz_mean=rzm,other_mean=om,counts=tot,status=st)
        print(f"{g:<8}{rzm:>10.3f}{om:>12.3f}{(rzm/om if om>0 else float('nan')):>8.2f}{tot:>12}   {st}")
    p1=f"{hits}/{tested} testable Wnt-inhibitory genes enriched >=1.5x in the resting zone"
    print(f"\nP1 RESULT: {p1}")

# ---- P2: AXIN2 and the stem markers, stromal vs chondrocyte ----
print("\nP2 — STEM MARKERS AND WNT RESPONSIVENESS, stromal vs chondrocyte")
print(f"{'gene':<8}{'stromal mn':>12}{'chondro mn':>12}{'ratio':>8}{'pooled cts':>12}   status")
s_mask=np.isin(LE,stromal)&K; c_mask=np.isin(LE,chond)&K
p2rows={}
for g in STEM+["SFRP5","CHRDL2","LGR5","TCF7","NKD1","RSPO2","RSPO3"]:
    sm=mn(s_mask,g); cm=mn(c_mask,g); tot=ct(s_mask,g)+ct(c_mask,g)
    if not PRESENT.get(g,True): st="NOT IN MATRIX"
    elif tot<50: st="below 50-count floor - not compared"
    else:
        r=sm/cm if cm>0 else float("inf")
        st=("ENRICHED in stromal" if r>=2 else "DEPLETED in stromal" if r<=0.5 else "not differential")+f" ({r:.2f})"
    p2rows[g]=dict(stromal_mean=sm,chondro_mean=cm,counts=tot,status=st)
    print(f"{g:<8}{sm:>12.3f}{cm:>12.3f}{(sm/cm if cm>0 else float('nan')):>8.2f}{tot:>12}   {st}")

ax=p2rows.get("AXIN2",{})
print(f"\nP2 RESULT (AXIN2, the specific prediction): {ax.get('status','n/a')}")

# per-cluster table for the stem markers
print(f"\nPER-CLUSTER, retained donors, clusters >= 20 cells")
hdr=["PTHLH","CHRDL2","AXIN2","NT5E","FOXA2","APOE","SFRP5","GLI1","COL2A1","COL1A1"]
print(f"{'cl':>4}{'n':>7}"+"".join(f"{g:>9}" for g in hdr))
percl={}
for c in cls:
    m=(LE==c)&K
    if m.sum()<20: continue
    percl[c]={g:mn(m,g) for g in hdr}; percl[c]["n"]=int(m.sum())
    print(f"{c:>4}{int(m.sum()):>7}"+"".join(f"{mn(m,g):>9.3f}" for g in hdr))

json.dump({"retained_donors":keep,"genes_absent_from_matrix":absent,"chondrocyte_clusters":chond,
           "stromal_clusters":stromal,"resting_zone_clusters":rz,"P1":p1,
           "P1_rows":p1rows if rz else {},"P2_rows":p2rows,"per_cluster":percl},
          open(OUT,"w"),indent=1,default=float)
print(f"\nwrote {OUT}")
