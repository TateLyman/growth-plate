import numpy as np, gzip, itertools
exec(open("key.py").read().split("# THE REJUVENATING CORE")[0])
print("=== per-sample distributions (batch check) ===")
for i,t in enumerate(T):
    col=X[:,i]; col=col[np.isfinite(col)]
    print(f"  {t:26s} median={np.median(col):6.2f}  q25={np.percentile(col,25):6.2f}  q75={np.percentile(col,75):6.2f}  n={len(col)}")
expr=np.nanmean(X,1)>np.nanmedian(np.nanmean(X,1))
def r(a,b):
    m=expr&np.isfinite(a)&np.isfinite(b); return np.corrcoef(a[m],b[m])[0,1]
A=np.nanmean(X[:,AMF],1); U=np.nanmean(X[:,AU],1); P=np.nanmean(X[:,P3],1)
print(f"\nSHARED denominator  r(ACT,YOUTH) = {r(A-U,P-U):+.3f}   <-- what R118 reported")
print("\n=== DISJOINT-SPLIT CONTROL: split adult-uninjured, no shared samples ===")
rs=[]
for c in itertools.combinations(range(len(AU)),2):
    u1=[AU[i] for i in c]; u2=[AU[i] for i in range(len(AU)) if i not in c]
    v=r(A-np.nanmean(X[:,u1],1), P-np.nanmean(X[:,u2],1)); rs.append(v)
    print(f"   AU split {c} vs rest -> r = {v:+.3f}")
print(f"\n   mean disjoint r = {np.mean(rs):+.3f}   (shared-denominator r = {r(A-U,P-U):+.3f})")
print("\n=== NEGATIVE CONTROL: split adult-uninjured against ITSELF ===")
ns=[]
for c in itertools.combinations(range(len(AU)),2):
    u1=[AU[i] for i in c]; u2=[AU[i] for i in range(len(AU)) if i not in c]
    # two independent 'contrasts' that share the SAME denominator structure but no real biology
    v=r(np.nanmean(X[:,u1],1)-np.nanmean(X[:,u2],1), np.nanmean(X[:,u1],1)-np.nanmean(X[:,u2],1))
    ns.append(v)
# proper null: shared-denominator with a random group as numerator
rng=np.random.default_rng(0); nulls=[]
allc=AMF+AU+P3
for _ in range(30):
    perm=list(rng.permutation(allc))
    a,u,p=perm[:3],perm[3:8],perm[8:11]
    nulls.append(r(np.nanmean(X[:,a],1)-np.nanmean(X[:,u],1), np.nanmean(X[:,p],1)-np.nanmean(X[:,u],1)))
print(f"   label-permuted, SHARED denominator: mean r = {np.mean(nulls):+.3f}  sd={np.std(nulls):.3f}  max={np.max(nulls):+.3f}")
print("\n   -> if permuted r is already high, the shared denominator ALONE manufactures correlation.")
