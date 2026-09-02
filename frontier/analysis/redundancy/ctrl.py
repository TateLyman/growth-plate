import numpy as np, json
dC=np.load("dCNP.npy"); dF=np.load("dFG.npy"); expr=np.load("expr.npy")
zn=["R/P","H","M"]; wk=[1,2,3,4]
def r(x,y):
    m=np.isfinite(x)&np.isfinite(y); return np.corrcoef(x[m],y[m])[0,1]
print("=== POSITIVE CONTROL 1: FGFR3-blockade axis, age vs age (same axis, diff timepoints) ===")
for i in range(4):
    print("  wk%d"%wk[i], "".join(f"  {r(dF[i][expr],dF[j][expr]):+.3f}" for j in range(4)))
print("\n=== POSITIVE CONTROL 2: CNP axis, zone vs zone (same axis, diff zones) ===")
for i in range(3):
    print(f"  {zn[i]:4s}", "".join(f"  {r(dC[i][expr],dC[j][expr]):+.3f}" for j in range(3)))
print("\n=== CROSS: CNP zone x FGFR3 week ===")
print("      " + "".join(f"   wk{w}   " for w in wk))
for i in range(3):
    print(f"  {zn[i]:4s}", "".join(f"  {r(dC[i][expr],dF[j][expr]):+.3f} " for j in range(4)))
mx=max(abs(r(dC[i][expr],dF[j][expr])) for i in range(3) for j in range(4))
selfF=np.mean([abs(r(dF[i][expr],dF[j][expr])) for i in range(4) for j in range(4) if i!=j])
selfC=np.mean([abs(r(dC[i][expr],dC[j][expr])) for i in range(3) for j in range(3) if i!=j])
print(f"\nmean |r| WITHIN FGFR3 axis = {selfF:.3f}   WITHIN CNP axis = {selfC:.3f}   MAX |r| BETWEEN = {mx:.3f}")
print(f"shared variance between arms <= {mx**2*100:.1f}%")
