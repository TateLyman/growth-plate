import numpy as np, gzip, itertools
exec(open("key.py").read().split("# THE REJUVENATING CORE")[0])
z=(X==0)
print(f"=== DATA QUALITY ===\nprobes exactly 0 in >=1 sample: {(z.any(1)).mean()*100:.1f}%")
print(f"mean fraction of probes ==0 per sample: {z.mean()*100:.1f}%")
good=~z.any(1)
print(f"probes nonzero in ALL 14 samples: {good.sum()} of {X.shape[0]}")
expr=good&(np.nanmean(X,1)>np.nanmedian(np.nanmean(X[good],1)))
print(f"probes used after strict filter: {expr.sum()}")
def r(a,b,m=None):
    m=expr if m is None else m
    mm=m&np.isfinite(a)&np.isfinite(b); return np.corrcoef(a[mm],b[mm])[0,1]
A=np.nanmean(X[:,AMF],1); U=np.nanmean(X[:,AU],1); P=np.nanmean(X[:,P3],1)
obs_shared=r(A-U,P-U)
print(f"\n=== ON CLEAN PROBES ONLY (nonzero everywhere) ===")
print(f"shared-denominator r(ACT,YOUTH) = {obs_shared:+.3f}")
rng=np.random.default_rng(1); allc=AMF+AU+P3
nulls=[]
for _ in range(200):
    p=list(rng.permutation(allc)); a,u,pp=p[:3],p[3:8],p[8:11]
    nulls.append(r(np.nanmean(X[:,a],1)-np.nanmean(X[:,u],1), np.nanmean(X[:,pp],1)-np.nanmean(X[:,u],1)))
nulls=np.array(nulls)
print(f"permuted null (shared denom): mean={nulls.mean():+.3f} sd={nulls.std():.3f}  p(obs) = {(nulls>=obs_shared).mean():.3f}")
# disjoint observed + matched null
dis=[]
for c in itertools.combinations(range(len(AU)),2):
    u1=[AU[i] for i in c]; u2=[AU[i] for i in range(len(AU)) if i not in c]
    dis.append(r(A-np.nanmean(X[:,u1],1), P-np.nanmean(X[:,u2],1)))
obs_dis=np.mean(dis)
dn=[]
for _ in range(200):
    p=list(rng.permutation(allc)); a,u1,pp,u2=p[:3],p[3:5],p[5:8],p[8:11]
    dn.append(r(np.nanmean(X[:,a],1)-np.nanmean(X[:,u1],1), np.nanmean(X[:,pp],1)-np.nanmean(X[:,u2],1)))
dn=np.array(dn)
print(f"\ndisjoint-split observed r = {obs_dis:+.3f}")
print(f"disjoint permuted null: mean={dn.mean():+.3f} sd={dn.std():.3f}  p(obs) = {(dn>=obs_dis).mean():.3f}")
# does the STEM PANEL survive on clean probes?
sym2={}
with gzip.open("GPL1261.annot.gz",'rt',errors='replace') as f:
    on=False
    for l in f:
        if l.startswith('!platform_table_begin'): on=True; next(f); continue
        if l.startswith('!platform_table_end'): break
        if on:
            p=l.split('\t')
            if len(p)>2 and p[2].strip(): sym2[p[0]]=p[2].strip()
S2=np.array([sym2.get(i,"") for i in ids])
ACT2=A-U
RZ={"Pthlh","Sfrp5","Sfrp1","Gas1","Spon1","Wif1","Prg4","Foxa2","Grem1","Sox9","Acan","Col2a1"}
idx=[i for i,s in enumerate(S2) if s in RZ and expr[i]]
g=ACT2[expr&np.isfinite(ACT2)]
print(f"\nstem/chondro panel on CLEAN probes: z={(np.nanmean(ACT2[idx])-g.mean())/(g.std()/np.sqrt(len(idx))):+.2f} (n={len(idx)})")
for gg in ["Pthlh","Spon1","Prg4","Sox9","Acan","Col2a1"]:
    i2=[i for i,s in enumerate(S2) if s==gg and expr[i]]
    print(f"   {gg:8s} {'%+.2f'%np.nanmean(ACT2[i2]) if i2 else 'dropped (had zeros)'}")
