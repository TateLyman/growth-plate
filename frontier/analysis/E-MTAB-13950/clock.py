import csv, math, numpy as np
from scipy import stats

rows=list(csv.reader(open('horvath_raw.csv')))
meta={}
for r in rows[4:]:
    if r and r[0].strip():
        meta[r[0].strip()]=dict(coef=float(r[1]),
                                med=float(r[6]) if r[6] not in ('','NA') else None,
                                medY=float(r[7]) if r[7] not in ('','NA') else None)
INTERCEPT=float(rows[3][1]); assert rows[3][0]=='(Intercept)', rows[3][0]
cpgs=[k for k in meta if k.startswith('cg')]

L=open('betas_clock.tsv').read().rstrip('\n').split('\n')
samples=L[0].split('\t')[1:]
B={}
for line in L[1:]:
    p=line.split('\t'); B[p[0]]=np.array([float(x) for x in p[1:]])
present=[c for c in cpgs if c in B]; missing=[c for c in cpgs if c not in B]

def dnam_age(impute):
    x=np.full(len(samples), INTERCEPT)
    for c in present: x += meta[c]['coef']*B[c]
    const=0.0
    for c in missing:
        v=meta[c][impute]
        if v is None: v=0.5
        const += meta[c]['coef']*v
    x = x + const
    return np.where(x<=0, 21*np.exp(x)-1, 21*x+20), const

def grp(s):
    return 'CT_P' if s.startswith('CT_P') and not s.startswith('CT_PP') else ('CT_PP' if s.startswith('CT_PP') else 'CPP')
G=np.array([grp(s) for s in samples])

print(f"probes: {len(present)}/{len(cpgs)} present, {len(missing)} imputed")
print(f"samples: CPP={sum(G=='CPP')}  CT_PP={sum(G=='CT_PP')}  CT_P={sum(G=='CT_P')}\n")

CHRON={'CPP':7.83,'CT_PP':7.83,'CT_P':14.55}
for impute in ('med','medY'):
    age,const=dnam_age(impute)
    print(f"=== imputation: {impute} (constant contribution {const:.4f}) ===")
    for g in ('CT_PP','CPP','CT_P'):
        a=age[G==g]
        print(f"  {g:6s} n={len(a):2d}  DNAmAge mean={a.mean():6.3f}  sd={a.std(ddof=1):5.3f}  median={np.median(a):6.3f}  chron(median)={CHRON[g]}")
    cpp,ctpp,ctp=age[G=='CPP'],age[G=='CT_PP'],age[G=='CT_P']
    d=cpp.mean()-ctpp.mean()
    t,p=stats.ttest_ind(cpp,ctpp,equal_var=False)
    u,pu=stats.mannwhitneyu(cpp,ctpp,alternative='two-sided')
    sp=math.sqrt(((len(cpp)-1)*cpp.var(ddof=1)+(len(ctpp)-1)*ctpp.var(ddof=1))/(len(cpp)+len(ctpp)-2))
    print(f"  --> CPP vs age-matched CT_PP: diff = {d:+.3f} yr   Welch t={t:.3f} p={p:.4g}   MWU p={pu:.4g}   Cohen d={d/sp:.3f}")
    se=math.sqrt(cpp.var(ddof=1)/len(cpp)+ctpp.var(ddof=1)/len(ctpp))
    df=(cpp.var(ddof=1)/len(cpp)+ctpp.var(ddof=1)/len(ctpp))**2/((cpp.var(ddof=1)/len(cpp))**2/(len(cpp)-1)+(ctpp.var(ddof=1)/len(ctpp))**2/(len(ctpp)-1))
    tc=stats.t.ppf(0.975,df)
    print(f"      95% CI [{d-tc*se:+.3f}, {d+tc*se:+.3f}]")
    slope=(ctp.mean()-ctpp.mean())/(14.55-7.83)
    print(f"  --> normal clock slope CT_PP->CT_P: {slope:.3f} DNAm-yr per chron-yr  (CT_P-CT_PP={ctp.mean()-ctpp.mean():+.3f} over 6.72 yr)")
    if slope!=0: print(f"      CPP offset in chronological-equivalent years: {d/slope:+.3f} yr")
    t2,p2=stats.ttest_ind(ctp,ctpp,equal_var=False)
    print(f"  --> CT_P vs CT_PP (positive control): diff={ctp.mean()-ctpp.mean():+.3f} Welch p={p2:.3g}")
    print()
