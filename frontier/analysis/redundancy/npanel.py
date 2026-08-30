import numpy as np, gzip, json
RZ=["Gas1","Spon1","Wif1","Pthlh","Sfrp5","Prg4","Sfrp1","Dkk2","Notum","Fzd6"]
def ann(f):
    s={}
    with gzip.open(f,'rt',errors='replace') as fh:
        on=False
        for l in fh:
            if l.startswith('!platform_table_begin'): on=True; next(fh); continue
            if l.startswith('!platform_table_end'): break
            if on:
                p=l.split('\t')
                if len(p)>2 and p[2].strip(): s[p[0]]=p[2].strip()
    return s
# ---------- MOUSE (GPL1261): erda axis + CNP axis ----------
sm=ann("GPL1261.annot.gz")
ids=json.load(open("GSE4481_meta.json"))["ids"]
S=np.array([sm.get(i,"") for i in ids])
dC=np.load("dCNP.npy"); dF=np.load("dFG.npy"); expr=np.load("expr.npy")
print("=== VALIDATED RESTING-ZONE (N) SIGNATURE, per gene ===")
print(f"{'gene':8s}|{'ERDA dir (WT-GOF)':^30s}|{'CNP dir':^22s}")
print(f"{'':8s}|{'wk1':>7s}{'wk2':>7s}{'wk3':>7s}{'wk4':>7s}|{'R/P':>7s}{'H':>7s}{'M':>7s}")
print("-"*62)
vals={}
for g in RZ:
    idx=[i for i,s in enumerate(S) if s==g and expr[i]]
    if not idx: print(f"{g:8s}|  no probe / not expressed"); continue
    f4=[np.nanmean(dF[j][idx]) for j in range(4)]; c3=[np.nanmean(dC[j][idx]) for j in range(3)]
    vals[g]=(f4,c3)
    print(f"{g:8s}|"+"".join(f"{v:+7.2f}" for v in f4)+"|"+"".join(f"{v:+7.2f}" for v in c3))
if vals:
    print("-"*62)
    mf=[np.mean([vals[g][0][j] for g in vals]) for j in range(4)]
    mc=[np.mean([vals[g][1][j] for g in vals]) for j in range(3)]
    print(f"{'MEAN':8s}|"+"".join(f"{v:+7.2f}" for v in mf)+"|"+"".join(f"{v:+7.2f}" for v in mc))
    # z vs genome
    def z(vec,idxs):
        g=vec[expr&np.isfinite(vec)]; v=vec[idxs]
        return (np.nanmean(v)-g.mean())/(g.std()/np.sqrt(len(v)))
    allidx=[i for i,s in enumerate(S) if s in RZ and expr[i]]
    print(f"{'z-score':8s}|"+"".join(f"{z(dF[j],allidx):+7.2f}" for j in range(4))+"|"+"".join(f"{z(dC[j],allidx):+7.2f}" for j in range(3))+f"   (n={len(allidx)})")
