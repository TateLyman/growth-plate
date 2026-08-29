import numpy as np,json,os,sys,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import uni
def build(acc):
    o='cache/%s.npz'%acc
    if os.path.exists(o): return 'have'
    D=uni.get(acc)
    if D is None: return 'none'
    g=np.array([str(x).upper().split('.')[0].split('///')[0].strip() for x in D['g']])
    keep=np.array([bool(x) and x not in ('---','NA','NAN','') for x in g])
    if keep.sum()<500: return 'nosym'
    g=g[keep]; X=D['X'][keep]
    if not D.get('logged'): X=np.log2(np.clip(X,0,None)+1)
    # collapse duplicates by max mean
    order=np.argsort(-np.nan_to_num(np.nanmean(X,axis=1),nan=-1e9))
    g2=g[order]; X2=X[order]
    _,first=np.unique(g2,return_index=True)
    g3=g2[np.sort(first)]; X3=X2[np.sort(first)]
    np.savez_compressed(o,g=g3,X=X3.astype(np.float32),
        labels=np.array(D['labels'],dtype=object),kind=D['kind'],
        stitle=D.get('stitle',''),org=D.get('org',''),summary=D.get('summary','')[:1500])
    return 'ok'
if __name__=='__main__':
    accs=uni.ALL()
    me=int(sys.argv[1]); tot=int(sys.argv[2])
    from collections import Counter
    c=Counter()
    for i,a in enumerate(accs):
        if i%tot!=me: continue
        try: r=build(a)
        except Exception as e: r='err:'+type(e).__name__
        c[r.split(':')[0]]+=1
        if r.startswith('err'): print(a,r,flush=True)
    print(me,dict(c),flush=True)
