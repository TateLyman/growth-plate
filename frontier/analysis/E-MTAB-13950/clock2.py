import csv,json,math,numpy as np
from scipy import stats
rows=[r for r in csv.reader(open('sb2d/aging-10-101508-s005.csv'))]
hdr=rows[0]; body=rows[1:]
INT=float([r for r in body if r[0]=='(Intercept)'][0][1])
coef={r[0]:float(r[1]) for r in body if r[0].startswith('cg')}
ann={r[0]:(r[3],r[4],r[6]) for r in body if r[0].startswith('cg')}
L=open('betas2.tsv').read().rstrip('\n').split('\n')
samples=L[0].split('\t')[1:]
B={}
for l in L[1:]:
    p=l.split('\t'); B[p[0]]=np.array([float(x) for x in p[1:]])
def grp(s): return 'CT_P' if (s.startswith('CT_P') and not s.startswith('CT_PP')) else ('CT_PP' if s.startswith('CT_PP') else 'CPP')
G=np.array([grp(s) for s in samples])
pres=[c for c in coef if c in B]; miss=[c for c in coef if c not in B]
print(f"SKIN & BLOOD CLOCK: {len(pres)}/{len(coef)} probes present, {len(miss)} missing (contribute a constant, so group differences are unaffected)")
x=np.full(len(samples),INT)
for c in pres: x+=coef[c]*B[c]
# impute missing at cohort-independent value: use 0.5 (constant across samples)
for c in miss: x+=coef[c]*0.5
age=np.where(x<=0,21*np.exp(x)-1,21*x+20)
CH={'CT_PP':7.83,'CPP':7.83,'CT_P':14.55}
for g in ('CT_PP','CPP','CT_P'):
    a=age[G==g]; print(f"  {g:6s} n={len(a):2d}  DNAmAge={a.mean():6.3f} ± {a.std(ddof=1):5.3f}   chron={CH[g]}")
cpp,ctpp,ctp=age[G=='CPP'],age[G=='CT_PP'],age[G=='CT_P']
def cmp(a,b,lab):
    t,p=stats.ttest_ind(a,b,equal_var=False)
    se=math.sqrt(a.var(ddof=1)/len(a)+b.var(ddof=1)/len(b))
    df=(a.var(ddof=1)/len(a)+b.var(ddof=1)/len(b))**2/((a.var(ddof=1)/len(a))**2/(len(a)-1)+(b.var(ddof=1)/len(b))**2/(len(b)-1))
    tc=stats.t.ppf(0.975,df); d=a.mean()-b.mean()
    print(f"  {lab}: {d:+.3f} yr  95%CI[{d-tc*se:+.3f},{d+tc*se:+.3f}]  Welch p={p:.4g}")
    return d
cmp(cpp,ctpp,"CPP vs CT_PP (age-matched, stage differs)")
cmp(ctp,ctpp,"CT_P vs CT_PP (positive control)")
cmp(cpp,ctp,"CPP vs CT_P (stage-matched, age differs)")

# power
sp=math.sqrt(((len(cpp)-1)*cpp.var(ddof=1)+(len(ctpp)-1)*ctpp.var(ddof=1))/(len(cpp)+len(ctpp)-2))
print(f"\n  pooled SD = {sp:.3f} yr")
for eff in (1.69,1.0,0.42):
    n=math.ceil(2*((1.96+0.84)*sp/eff)**2)
    print(f"   n per group for 80% power to detect {eff:.2f} yr: {n}")
