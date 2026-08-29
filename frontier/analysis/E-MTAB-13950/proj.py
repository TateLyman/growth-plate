import numpy as np
from scipy import stats
G=np.load("groups.npy",allow_pickle=True); gm=np.load("globalmean.npy")
def t(a,b,lab):
    tt,p=stats.ttest_ind(a,b,equal_var=False)
    print(f"   {lab}: diff={a.mean()-b.mean():+.6f}  Welch p={p:.4g}")
print("=== GLOBAL METHYLATION TESTS ===")
t(gm[G=='CPP'],gm[G=='CT_PP'],"CPP vs CT_PP (age-matched)")
t(gm[G=='CPP'],gm[G=='CT_P'],"CPP vs CT_P (stage-matched)")
t(gm[G=='CT_P'],gm[G=='CT_PP'],"CT_P vs CT_PP (normal puberty)")

L=open("puberty_axis.tsv").read().rstrip("\n").split("\n")
samples=L[0].split("\t")[1:]
M=np.array([[float(x) for x in l.split("\t")[1:]] for l in L[1:]])
print("\naxis matrix",M.shape)
iPP=np.where(G=='CT_PP')[0]; iP=np.where(G=='CT_P')[0]; iC=np.where(G=='CPP')[0]
mPP=M[:,iPP].mean(1); mP=M[:,iP].mean(1)
d=mP-mPP
print("axis probes: %d ; hypermethylated at puberty %d (%.0f%%), hypomethylated %d (%.0f%%)"%(
    len(d),(d>0).sum(),100*(d>0).mean(),(d<0).sum(),100*(d<0).mean()))
# projection: score = correlation-free scalar, position along CT_PP->CT_P axis, 0=prepubertal,1=pubertal
w=d/np.dot(d,d)
score=np.array([np.dot(M[:,j]-mPP,w) for j in range(M.shape[1])])
print("\n=== PUBERTY-AXIS SCORE (0 = prepubertal control mean, 1 = pubertal control mean) ===")
print("   axis defined on CONTROLS ONLY; CPP projected onto it")
for g in ('CT_PP','CPP','CT_P'):
    a=score[G==g]; print(f"   {g:6s} n={len(a):2d}  score={a.mean():+.4f} ± {a.std(ddof=1):.4f}   [{a.min():+.3f}, {a.max():+.3f}]")
tt,p=stats.ttest_ind(score[G=='CPP'],score[G=='CT_PP'],equal_var=False)
print(f"   CPP vs CT_PP: diff={score[G=='CPP'].mean()-score[G=='CT_PP'].mean():+.4f}  Welch p={p:.4g}")
u,pu=stats.mannwhitneyu(score[G=='CPP'],score[G=='CT_PP'])
print(f"   CPP vs CT_PP: MWU p={pu:.4g}")
# leave-one-out honesty: rebuild axis excluding each control, re-project
print("\n=== leave-one-control-out stability of CPP score ===")
sc=[]
for k in list(iPP)+list(iP):
    keep=[j for j in list(iPP)+list(iP) if j!=k]
    pp=[j for j in keep if G[j]=='CT_PP']; pu_=[j for j in keep if G[j]=='CT_P']
    m1=M[:,pp].mean(1); m2=M[:,pu_].mean(1); dd=m2-m1; ww=dd/np.dot(dd,dd)
    sc.append(np.mean([np.dot(M[:,j]-m1,ww) for j in iC]))
sc=np.array(sc); print(f"   CPP mean score across {len(sc)} LOO axes: {sc.mean():+.4f}  range [{sc.min():+.4f},{sc.max():+.4f}]")
