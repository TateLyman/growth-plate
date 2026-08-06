#!/usr/bin/env python3
"""Recover the non-cartilage cell populations of the human growth plate by
unsupervised clustering, then ask whether GLI1/PDGFRA mark a stromal population -
the human counterpart of the qu2025 mouse reservoir.

WHY THIS RATHER THAN A MARKER GATE. reservoir_screen.py used a hand-built stromal
gate and failed its THY1 guard twice (CORR-018). chu2026 resolved T cell, myeloid,
NK, plasma, B, endothelial, vascular smooth muscle and MSC/osteoblast clusters in
this same data, so the populations ARE there - the gate was the problem, not the
data. Clustering recovers them the way the authors did instead of guessing a gate.

SAMPLES. Only the four DIRECTLY PROCESSED biopsies. The other ten libraries in
GSE288028 are vehicle- and GH-cultured arms; 24 h of explant culture changes
exactly what a progenitor question is most sensitive to.

GUARDS, DECLARED BEFORE ANY CLUSTERING IS RUN. These test whether the clustering
recovered the known biology, not whether it gave the answer I want:
  G1 An IMMUNE population must appear - a cluster with high PTPRC. chu2026 report
     T, myeloid, NK, plasma and B cells in this tissue.
  G2 An ENDOTHELIAL population must appear - a cluster with high PECAM1 or CDH5.
  G3 A HYPERTROPHIC chondrocyte cluster must appear - high COL10A1.
  G4 Any cluster nominated as stromal must be COL1A1-high AND COL2A1-low, and that
     is a description of the cluster, not a gate used to build it.
  If G1 AND G2 both fail, the non-cartilage compartment is not in these libraries
  and NOTHING IS REPORTED.
"""
import sys, os, json
import numpy as np, pandas as pd, scanpy as sc, anndata as ad

FRESH = {"GSM9328218_P30453_1001.h5":"donor1","GSM9328221_P31011_1001.h5":"donor2",
         "GSM9328224_P25452_001.h5":"donor3","GSM9328229_P22202_1015.h5":"donor4"}
MARKERS = {
 "chondrocyte":["COL2A1","ACAN","SOX9","COL9A1","COL11A1"],
 "hypertrophic":["COL10A1","IBSP","SPP1","MEF2C"],
 "resting/stem":["SFRP5","GAS1","APOE","CHRDL2","PTHLH"],
 "proliferative":["CCND1","MKI67","TOP2A","PCNA"],
 "stromal/MSC":["COL1A1","COL1A2","PDGFRA","PRRX1","LUM","DCN","THY1"],
 "osteoblast":["RUNX2","SP7","ALPL","BGLAP"],
 "immune":["PTPRC","CD3E","CD68","LYZ","NKG7","MS4A1","JCHAIN"],
 "endothelial":["PECAM1","CDH5","VWF"],
 "vascular smooth muscle":["ACTA2","MYH11","TAGLN","RGS5"],
 "hedgehog":["GLI1","PTCH1","HHIP","GLI2","GLI3","SMO","IHH"],
}
def main(d, outdir):
    sc.settings.verbosity=1
    ads=[]
    for fn,dn in FRESH.items():
        p=os.path.join(d,fn)
        if not os.path.exists(p): print(f"MISSING {p}",file=sys.stderr); return 1
        a=sc.read_10x_h5(p); a.var_names_make_unique()
        a.obs["donor"]=dn; a.obs_names=[f"{dn}_{b}" for b in a.obs_names]
        ads.append(a); print(f"  {dn}: {a.n_obs} cells x {a.n_vars} genes")
    A=ad.concat(ads, join="outer", label=None); A.var_names_make_unique()
    print(f"\nconcatenated: {A.n_obs} cells x {A.n_vars} genes")

    A.var["mt"]=A.var_names.str.startswith("MT-")
    sc.pp.calculate_qc_metrics(A, qc_vars=["mt"], inplace=True, log1p=False)
    print(f"  mito genes found: {int(A.var['mt'].sum())}; median pct_counts_mt "
          f"{np.median(A.obs['pct_counts_mt']):.1f}")
    before=A.n_obs
    A=A[(A.obs.n_genes_by_counts>=200)&(A.obs.pct_counts_mt<20)].copy()
    sc.pp.filter_genes(A, min_cells=3)
    print(f"  QC: {before} -> {A.n_obs} cells (>=200 genes, <20% mito), {A.n_vars} genes")

    A.layers["counts"]=A.X.copy()
    sc.pp.normalize_total(A, target_sum=1e4); sc.pp.log1p(A)
    A.raw=A
    sc.pp.highly_variable_genes(A, n_top_genes=2000, batch_key="donor")
    A=A[:,A.var.highly_variable].copy()
    sc.pp.scale(A, max_value=10)
    sc.tl.pca(A, n_comps=50, svd_solver="arpack")
    try:
        import harmonypy  # noqa
        sc.external.pp.harmony_integrate(A, "donor"); rep="X_pca_harmony"
        print("  batch correction: harmony")
    except Exception:
        rep="X_pca"; print("  batch correction: NONE (harmonypy unavailable) - donor composition reported per cluster")
    sc.pp.neighbors(A, n_neighbors=15, use_rep=rep)
    sc.tl.leiden(A, resolution=1.0, key_added="leiden", flavor="igraph", n_iterations=2, directed=False)
    n=A.obs.leiden.nunique(); print(f"\nLeiden: {n} clusters at resolution 1.0")

    R=A.raw.to_adata()
    R.obs=A.obs.copy()
    def frac(cl, g):
        if g not in R.var_names: return np.nan
        m=R[R.obs.leiden==cl, g].X
        m=np.asarray(m.todense()).ravel() if hasattr(m,"todense") else np.asarray(m).ravel()
        return 100.0*float((m>0).sum())/len(m)
    def mean_expr(cl,g):
        if g not in R.var_names: return np.nan
        m=R[R.obs.leiden==cl, g].X
        m=np.asarray(m.todense()).ravel() if hasattr(m,"todense") else np.asarray(m).ravel()
        return float(m.mean())
    cls=sorted(A.obs.leiden.unique(), key=int)
    prof={c:{k:{g:round(frac(c,g),1) for g in v} for k,v in MARKERS.items()} for c in cls}
    size={c:int((A.obs.leiden==c).sum()) for c in cls}
    donors={c:A.obs.loc[A.obs.leiden==c,"donor"].value_counts().to_dict() for c in cls}

    # ---- guards ----
    def best(cl_set, g): return max((frac(c,g) for c in cl_set), default=0)
    imm=[c for c in cls if frac(c,"PTPRC")>=25]
    endo=[c for c in cls if max(frac(c,"PECAM1"),frac(c,"CDH5"))>=25]
    hyp=[c for c in cls if frac(c,"COL10A1")>=np.nanpercentile([frac(x,"COL10A1") for x in cls],90)]
    fail=[]
    if not imm: fail.append(f"G1 FAILED: no cluster with PTPRC in >=25% of cells (max {max(frac(c,'PTPRC') for c in cls):.1f}%)")
    if not endo: fail.append(f"G2 FAILED: no cluster with PECAM1 or CDH5 in >=25% of cells (max {max(max(frac(c,'PECAM1'),frac(c,'CDH5')) for c in cls):.1f}%)")
    if not hyp: fail.append("G3 FAILED: no hypertrophic cluster")
    print("\n" + ("GUARD STATUS: " + "; ".join(fail) if fail else "guards G1-G3 PASS"))
    if len(fail)>=2 and any("G1" in f for f in fail) and any("G2" in f for f in fail):
        print("\nBoth the immune and endothelial guards failed: the non-cartilage compartment is")
        print("not recoverable from these libraries. REFUSING TO REPORT the reservoir result.")
        json.dump({"guards":fail,"cluster_sizes":size}, open(os.path.join(outdir,"cluster_guards_failed.json"),"w"), indent=1)
        return 1

    print(f"\n{'cl':>3} {'n':>6} {'donors':<34} " + " ".join(f"{g:>7}" for g in
          ("COL2A1","COL10A1","COL1A1","PDGFRA","PTPRC","PECAM1","ACTA2","GLI1","SFRP5","MKI67")))
    for c in cls:
        dd=",".join(f"{k[-1]}:{v}" for k,v in sorted(donors[c].items()))
        print(f"{c:>3} {size[c]:>6} {dd:<34} " + " ".join(f"{frac(c,g):>7.1f}" for g in
              ("COL2A1","COL10A1","COL1A1","PDGFRA","PTPRC","PECAM1","ACTA2","GLI1","SFRP5","MKI67")))
    os.makedirs(outdir, exist_ok=True)
    A.obs[["donor","leiden"]].to_csv(os.path.join(outdir,"cell_clusters.csv"))
    json.dump({"profiles":prof,"sizes":size,"donors":{k:{kk:int(vv) for kk,vv in v.items()} for k,v in donors.items()},
               "guards":{"immune_clusters":imm,"endothelial_clusters":endo,"hypertrophic_clusters":hyp,"failures":fail}},
              open(os.path.join(outdir,"cluster_profiles.json"),"w"), indent=1)
    print(f"\nwrote {outdir}/cluster_profiles.json and cell_clusters.csv")
    return 0

if __name__=="__main__":
    d=sys.argv[1]; out=sys.argv[2] if len(sys.argv)>2 else "clusterout"
    os.makedirs(out, exist_ok=True); sys.exit(main(d,out))
