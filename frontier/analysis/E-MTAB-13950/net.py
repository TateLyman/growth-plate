import json,numpy as np,collections
from scipy import stats
net=json.load(open('network_probes.json'))
L=open('betas2.tsv').read().rstrip('\n').split('\n')
samples=L[0].split('\t')[1:]
B={}
for l in L[1:]:
    p=l.split('\t'); B[p[0]]=np.array([float(x) for x in p[1:]])
def grp(s): return 'CT_P' if (s.startswith('CT_P') and not s.startswith('CT_PP')) else ('CT_PP' if s.startswith('CT_PP') else 'CPP')
G=np.array([grp(s) for s in samples])
iPP=G=='CT_PP'; iP=G=='CT_P'; iC=G=='CPP'
bygene=collections.defaultdict(list)
for pr,v in net.items():
    if pr in B:
        for g in v['gene']: bygene[g].append(pr)
print(f"{'gene':10s} {'n':>4s} {'preP':>7s} {'CPP':>7s} {'Pub':>7s} | {'Pub-preP':>9s} {'p':>9s} | {'CPP-preP':>9s} {'p':>9s}")
print("-"*80)
allp=[]
for g in sorted(bygene):
    prs=bygene[g]
    M=np.array([B[p] for p in prs])
    a=M[:,iPP].mean(0); b=M[:,iC].mean(0); c=M[:,iP].mean(0)
    t1,p1=stats.ttest_ind(c,a,equal_var=False)
    t2,p2=stats.ttest_ind(b,a,equal_var=False)
    allp.append((g,p1,p2))
    star1='*' if p1<0.05 else ' '; star2='*' if p2<0.05 else ' '
    print(f"{g:10s} {len(prs):4d} {a.mean():7.4f} {b.mean():7.4f} {c.mean():7.4f} | {c.mean()-a.mean():+9.4f} {p1:9.3g}{star1}| {b.mean()-a.mean():+9.4f} {p2:9.3g}{star2}")
# Benjamini-Hochberg
def bh(ps):
    m=len(ps); o=np.argsort(ps); q=np.empty(m); prev=1
    for r in range(m-1,-1,-1):
        prev=min(prev, ps[o[r]]*m/(r+1)); q[o[r]]=prev
    return q
q1=bh([x[1] for x in allp]); q2=bh([x[2] for x in allp])
print("\nBH-FDR q<0.05:")
print("  normal puberty (CT_P vs CT_PP):", [allp[i][0] for i in range(len(allp)) if q1[i]<0.05] or "NONE")
print("  CPP vs age-matched (CPP vs CT_PP):", [allp[i][0] for i in range(len(allp)) if q2[i]<0.05] or "NONE")
