import sys,os;sys.path.insert(0,'.')
import q,numpy as np
UP=[str(x) for x in np.load('lenup.npy')];DN=[str(x) for x in np.load('lendn.npy')]
# drop erythroid/muscle contamination from DOWN
BAD={'GATA1','KLF1','TRIM58','SLC25A37','GLRX5','UROD','ERMAP','EIF2AK1','ACTN2','TMOD1','TPM3','TRIM55','RPL3L','CORO6','POPDC3','RAG2','CD72','JOSD2','NUP210L','STOX1','TRAK2','ACSS1','CRAT','NDUFA2','ENDOU','RAB17','HIPK4','MACROD1','MED18'}
DN=[g for g in DN if g not in BAD]
print('UP %d  DN(cleaned) %d: %s'%(len(UP),len(DN),', '.join(DN)),file=sys.stderr)
def zs(D,gs):
    X=D['X']; out=[]
    for g in gs:
        x=q.v(D,g)
        if x is None: continue
        s=np.nanstd(x)
        if not np.isfinite(s) or s<1e-6: continue
        out.append((x-np.nanmean(x))/s)
    return (np.nanmean(np.array(out),axis=0),len(out)) if out else (None,0)
rows=[]
for a in q.acc_list():
    try: D=q.D(a)
    except Exception: continue
    if len(D['labels'])<4: continue
    u,nu=zs(D,UP); dn,nd=zs(D,DN)
    if nu<25 or nd<4: continue
    sc=u-dn
    o=np.argsort(-sc)
    rows.append((a,D['org'].split(';')[0][:12],D['stitle'][:58],
        [(D['labels'][i][:44],round(float(sc[i]),2)) for i in o[:2]],
        [(D['labels'][i][:44],round(float(sc[i]),2)) for i in o[-2:]],
        float(sc.max()-sc.min()),nu,nd))
rows.sort(key=lambda r:-r[5])
import json;json.dump([[r[0],r[1],r[2],r[3],r[4],r[5]] for r in rows],open('screen.json','w'))
print('datasets scored:',len(rows))
for r in rows[:60]:
    print('\n%s %s | %s  (spread %.2f)'%(r[0],r[1],r[2],r[5]))
    print('   HIGH: '+' || '.join('%s [%.2f]'%(t,v) for t,v in r[3]))
    print('   LOW : '+' || '.join('%s [%.2f]'%(t,v) for t,v in r[4]))
