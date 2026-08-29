import sys;sys.path.insert(0,'.')
import q,numpy as np
UP=list(np.load('lenup.npy'));DN=list(np.load('lendn.npy'))
def score(acc,A,B,name):
    D=q.D(acc)
    Xn=D['X']; bg=float(np.nanmean(np.nanmean(Xn[:,A],axis=1)-np.nanmean(Xn[:,B],axis=1)))
    def z(gs):
        vs=[]
        for g in gs:
            x=q.v(D,g)
            if x is None: continue
            a=np.nanmean(x[A]);b=np.nanmean(x[B])
            if np.isnan(a) or np.isnan(b): continue
            vs.append(a-b)
        return ((float(np.mean(vs))-bg) if vs else float('nan'), len(vs))
    u,nu=z(UP); dn,nd=z(DN)
    print('%-44s  UPsig %+6.3f(n=%3d)   DNsig %+6.3f(n=%3d)   delta %+6.3f'%(name,u,nu,dn,nd,u-dn))
