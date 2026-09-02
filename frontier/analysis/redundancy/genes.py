import numpy as np, json, gzip
dC=np.load("dCNP.npy"); dF=np.load("dFG.npy"); expr=np.load("expr.npy")
ids=json.load(open("GSE4481_meta.json"))["ids"]
sym={}
with gzip.open("GPL1261.annot.gz",'rt',errors='replace') as f:
    on=False
    for l in f:
        if l.startswith('!platform_table_begin'): on=True; next(f); continue
        if l.startswith('!platform_table_end'): break
        if on:
            p=l.split('\t')
            if len(p)>2 and p[2].strip(): sym[p[0]]=p[2].strip()
S=np.array([sym.get(i,"") for i in ids])
want=["Pthlh","Pth1r","Ihh","Gli1","Ptch1","Col10a1","Mmp13","Mmp9","Vegfa","Sox9","Acan","Col2a1",
      "Mki67","Npr2","Npr3","Nppc","Fgfr3","Sp7","Runx2","Alpl","Esr1","Cyp19a1","Dlk1","Igf2","H19","Mest","Grem1","Sfrp5","Nt5e","Foxa2"]
print(f"{'gene':9s} | {'FGFR3-blockade (WT-GOF)':^30s} | {'CNP (CNP-BSA)':^22s}")
print(f"{'':9s} | {'wk1':>7s}{'wk2':>7s}{'wk3':>7s}{'wk4':>7s} | {'R/P':>7s}{'H':>7s}{'M':>7s}")
print("-"*68)
for g in want:
    idx=[i for i,s in enumerate(S) if s==g and expr[i]]
    if not idx: print(f"{g:9s} |  (not expressed / no probe)"); continue
    f4=[np.nanmean(dF[j][idx]) for j in range(4)]
    c3=[np.nanmean(dC[j][idx]) for j in range(3)]
    print(f"{g:9s} |"+"".join(f"{v:+7.2f}" for v in f4)+" |"+"".join(f"{v:+7.2f}" for v in c3))
