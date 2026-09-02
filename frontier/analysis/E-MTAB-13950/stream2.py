import subprocess,numpy as np,sys
url="https://www.ebi.ac.uk/biostudies/files/E-MTAB-13950/Normalized_betavalues.txt"
p=subprocess.Popen(["curl","-sSL","--max-time","2400",url],stdout=subprocess.PIPE,bufsize=1<<22)
hdr=p.stdout.readline().decode().rstrip("\n").split("\t")
samples=hdr
def grp(s): return 'CT_P' if (s.startswith('CT_P') and not s.startswith('CT_PP')) else ('CT_PP' if s.startswith('CT_PP') else 'CPP')
G=np.array([grp(s) for s in samples])
iPP=np.where(G=='CT_PP')[0]; iP=np.where(G=='CT_P')[0]; iC=np.where(G=='CPP')[0]
tot=np.zeros(len(samples)); n=0
out=open("puberty_axis.tsv","w"); out.write("probe\t"+"\t".join(samples)+"\n"); kept=0
for line in p.stdout:
    parts=line.rstrip(b"\n").split(b"\t")
    if len(parts)!=len(samples)+1: continue
    v=np.array(parts[1:],dtype=float)
    tot+=v; n+=1
    d=v[iP].mean()-v[iPP].mean()
    if abs(d)>0.10:
        out.write(line.decode()); kept+=1
out.close()
gm=tot/n
print("probes:",n,"puberty-axis probes kept (|d|>0.10):",kept)
print("\n=== GLOBAL MEAN METHYLATION (all %d probes) ==="%n)
for g in ('CT_PP','CPP','CT_P'):
    a=gm[G==g]; print(f"  {g:6s} n={len(a):2d} mean beta={a.mean():.6f} sd={a.std(ddof=1):.6f}")
np.save("globalmean.npy",gm); np.save("groups.npy",G)
open("samples.txt","w").write("\n".join(samples))
