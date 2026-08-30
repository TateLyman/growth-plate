import numpy as np, json, re
A=np.load("GSE4481_X.npy");  ma=json.load(open("GSE4481_meta.json"))
B=np.load("GSE145821_X.npy");mb=json.load(open("GSE145821_meta.json"))
assert ma["ids"]==mb["ids"], "probe order differs"
ids=ma["ids"]
A=np.log2(np.clip(A,1,None))                      # GSE4481 is linear
ta,tb=ma["titles"],mb["titles"]

# ---- CNP contrasts, per zone (GSE4481) ----
def idx(pred,titles): return [i for i,t in enumerate(titles) if pred(t)]
zones={"R/P":"R/P","H":" H","M":" M"}
dCNP={}
for z,pat in zones.items():
    cnp=idx(lambda t: "CNP" in t and t.endswith(pat.strip()) , ta)
    bsa=idx(lambda t: "BSA" in t and t.endswith(pat.strip()) , ta)
    dCNP[z]=np.nanmean(A[:,cnp],1)-np.nanmean(A[:,bsa],1)
    print(f"CNP {z:4s}: n_cnp={len(cnp)} n_bsa={len(bsa)}")

# ---- FGFR3 BLOCKADE axis = WT - Mutant (reverses the GOF) ----
dFG={}
for wk in [1,2,3,4]:
    mut=idx(lambda t,w=wk: t.startswith("Mutant") and f"{w}wk" in t, tb)
    wt =idx(lambda t,w=wk: t.startswith("Control") and f"{w}wk" in t, tb)
    if not wt: wt=idx(lambda t,w=wk: ("Control" in t) and f"{w}wk" in t, tb)
    dFG[wk]=np.nanmean(B[:,wt],1)-np.nanmean(B[:,mut],1)
    print(f"FGFR3block wk{wk}: n_wt={len(wt)} n_mut={len(mut)}")
print("WT titles sample:", [t for t in tb if not t.startswith("Mutant")][:3])

# expressed filter: top half by mean abundance in both
expr=(np.nanmean(A,1)>np.nanmedian(np.nanmean(A,1)))&(np.nanmean(B,1)>np.nanmedian(np.nanmean(B,1)))
print("probes used:", expr.sum())
np.save("dCNP.npy", np.vstack([dCNP[z] for z in ["R/P","H","M"]]))
np.save("dFG.npy", np.vstack([dFG[w] for w in [1,2,3,4]]))
np.save("expr.npy", expr)

print("\n===== REDUNDANCY: CNP arm vs FGFR3-blockade arm (Pearson r across probes) =====")
print(f"{'':8s}" + "".join(f"  wk{w:<6d}" for w in [1,2,3,4]))
for z in ["R/P","H","M"]:
    row=f"{z:8s}"
    for w in [1,2,3,4]:
        x,y=dCNP[z][expr],dFG[w][expr]
        m=np.isfinite(x)&np.isfinite(y)
        row+=f"  {np.corrcoef(x[m],y[m])[0,1]:+.3f}   "
    print(row)
