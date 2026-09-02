#!/usr/bin/env python3
"""Is there a GLI1+/PDGFRA+ population ADJACENT TO the human resting zone but
OUTSIDE the cartilage - the human counterpart of the qu2025 mouse reservoir?

The dissociated scRNA-seq attempt (reservoir_screen.py) failed its own guards:
a cartilage-dominated biopsy has ambient COL2A1 everywhere and adjacency is not
recoverable from dissociated cells anyway. THIS is the right instrument -
avijgan2026br's Visium HD, bin2cell-segmented, with each cell assigned to
HZ, PZ, RZ or SOC and carrying spatial coordinates.

The SOC - secondary ossification centre - is the non-cartilage tissue lying
directly against the resting zone. That is where a reservoir would be.

METHOD. Median depth is 82 counts per cell, far too sparse for per-cell calls on
a low expressor like GLI1. Everything here is PSEUDOBULK: counts summed within a
group, divided by that group's total counts, expressed per 10,000. Distance
analysis bins cells by distance to the nearest RZ cell and pseudobulks the bins.

GUARDS, declared before any result is seen:
  G1 COL10A1 must be highest in HZ.
  G2 COL2A1 must be lower in SOC than in every cartilage zone.
  G3 IBSP or SPP1 (bone matrix) must be highest in SOC.
  G4 HEDGEHOG COHERENCE: PTCH1 and GLI1 are both direct Hedgehog targets. Their
     rank order across the four areas must agree (Spearman rho > 0). If GLI1 is
     dropout noise this fails and nothing is reported.
"""
import sys, json
import numpy as np, h5py, scipy.sparse as sp

def main(path):
    f=h5py.File(path,"r")
    cats=[c.decode() if isinstance(c,bytes) else c for c in f["obs/area/categories"][:]]
    codes=f["obs/area/codes"][:]
    genes=np.array([g.decode() if isinstance(g,bytes) else g for g in f["var/_index"][:]])
    gi={g:i for i,g in enumerate(genes)}
    X=sp.csr_matrix((f["X/data"][:],f["X/indices"][:],f["X/indptr"][:]),
                    shape=(len(codes),len(genes))).tocsc()
    spat=f["obsm/spatial"][:]

    def cpm(cells, g):
        j=gi.get(g)
        if j is None or len(cells)==0: return float("nan")
        tot=X[cells,:].sum()
        return float(X[cells,j].sum())/tot*1e4 if tot>0 else float("nan")

    area={c:np.where(codes==i)[0] for i,c in enumerate(cats)}
    order=["RZ","PZ","HZ","SOC"]
    PROBE=["GLI1","PDGFRA","PTCH1","HHIP","GLI2","GLI3","IHH","COL2A1","ACAN","COL10A1",
           "COL1A1","IBSP","SPP1","SFRP5","CHRDL2","PRRX1","PDGFRB","THY1","MKI67","SGMS2"]
    tab={g:{a:cpm(area[a],g) for a in order} for g in PROBE}

    fail=[]
    if not (tab["COL10A1"]["HZ"]==max(tab["COL10A1"][a] for a in order)):
        fail.append(f"G1 FAILED: COL10A1 not highest in HZ -> {tab['COL10A1']}")
    if not all(tab["COL2A1"]["SOC"] < tab["COL2A1"][a] for a in ("RZ","PZ","HZ")):
        fail.append(f"G2 FAILED: COL2A1 not lowest in SOC -> {tab['COL2A1']}")
    bone=max(("IBSP","SPP1"), key=lambda g: tab[g]["SOC"])
    if not (tab[bone]["SOC"]==max(tab[bone][a] for a in order)):
        fail.append(f"G3 FAILED: neither IBSP nor SPP1 highest in SOC -> IBSP {tab['IBSP']} SPP1 {tab['SPP1']}")
    g1=np.array([tab["GLI1"][a] for a in order]); pt=np.array([tab["PTCH1"][a] for a in order])
    def rank(v): 
        o=np.argsort(np.argsort(v)); return o.astype(float)
    r1,r2=rank(g1),rank(pt)
    rho=float(np.corrcoef(r1,r2)[0,1])
    if not (rho>0): fail.append(f"G4 FAILED: GLI1 and PTCH1 rank orders disagree across areas (rho={rho:.2f})")
    if fail:
        print("\n".join(fail)); print("\nREFUSING TO REPORT."); return 1
    print(f"guards PASS - COL10A1 max in HZ; COL2A1 min in SOC; {bone} max in SOC; "
          f"GLI1/PTCH1 rank agreement rho={rho:.2f}\n")

    print(f"cells: " + ", ".join(f"{a} {len(area[a])}" for a in order) + f"  (total {len(codes)})")
    print(f"\nPSEUDOBULK, counts per 10,000 within area\n")
    print(f"{'gene':<9} " + "".join(f"{a:>9}" for a in order) + "   SOC/RZ")
    for g in PROBE:
        v=[tab[g][a] for a in order]
        ratio = tab[g]["SOC"]/tab[g]["RZ"] if tab[g]["RZ"]>0 else float("inf")
        print(f"{g:<9} " + "".join(f"{x:>9.2f}" for x in v) + f"   {ratio:>6.2f}")

    # ---- distance to the resting zone ----
    rz=spat[area["RZ"]]
    from scipy.spatial import cKDTree
    tree=cKDTree(rz)
    d,_=tree.query(spat, k=1)
    noncart=np.concatenate([area["SOC"]])
    print("\nDISTANCE FROM EACH SOC CELL TO THE NEAREST RZ CELL, pseudobulk by distance band")
    bands=[(0,100),(100,250),(250,500),(500,1000),(1000,1e9)]
    print(f"{'band(px)':<12} {'n':>5} " + "".join(f"{g:>9}" for g in ("GLI1","PDGFRA","PTCH1","COL1A1","IBSP","COL2A1")))
    dist_rows=[]
    for lo,hi in bands:
        sel=noncart[(d[noncart]>=lo)&(d[noncart]<hi)]
        if len(sel)<15: 
            print(f"{lo}-{hi if hi<1e9 else 'inf':<7} {len(sel):>5}   (too few cells to pseudobulk)"); continue
        vals={g:cpm(sel,g) for g in ("GLI1","PDGFRA","PTCH1","COL1A1","IBSP","COL2A1")}
        dist_rows.append(dict(lo=lo,hi=hi if hi<1e9 else None,n=int(len(sel)),**{k:round(v,2) for k,v in vals.items()}))
        print(f"{str(lo)+'-'+(str(hi) if hi<1e9 else 'inf'):<12} {len(sel):>5} " + "".join(f"{vals[g]:>9.2f}" for g in ("GLI1","PDGFRA","PTCH1","COL1A1","IBSP","COL2A1")))
    out="/home/user/growth-plate/query/spatial_reservoir.json"
    json.dump({"area_pseudobulk":tab,"n_cells":{a:int(len(area[a])) for a in order},
               "distance_bands":dist_rows,"gli1_ptch1_rank_rho":rho}, open(out,"w"), indent=1)
    print(f"\nwrote {out}")
    return 0

if __name__=="__main__":
    sys.exit(main(sys.argv[1]))
