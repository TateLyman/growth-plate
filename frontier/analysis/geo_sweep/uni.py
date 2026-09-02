import numpy as np,json,os,re,glob,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import lib,sload
BASE=os.path.dirname(os.path.abspath(__file__))
RECS={r['acc']:r for r in json.load(open(BASE+'/recs.json'))}
SUPT=json.load(open(BASE+'/suptbl.json'))
ARR=set(json.load(open(BASE+'/withdata.json')))
_cache={}
def get(acc):
    if acc in _cache: return _cache[acc]
    D=None
    if acc in ARR:
        try: D=lib.load(acc)
        except Exception: D=None
        if D is not None and (D['g']!='').sum()<500: D=None
        if D is not None:
            D['labels']=[('%s %s'%(t,c)).strip() for t,c in zip(D['titles'],D['chars'])]
            D['kind']='array'
    if D is None and acc in SUPT:
        try: T=sload.load_tbl(SUPT[acc][0])
        except Exception: T=None
        if T is not None:
            T['labels']=T['cols']; T['acc']=acc; T['kind']='seq'
            T['logged']=bool(np.nanmax(T['X'])<30)
            D=T
    if D is not None:
        r=RECS.get(acc,{})
        D['stitle']=r.get('title',''); D['org']=r.get('org',''); D['summary']=r.get('summary','')
    _cache[acc]=D
    return D
def ALL():
    return sorted(set(list(ARR)+list(SUPT.keys())))
def val(D,gene):
    """case-insensitive gene lookup; returns log2 vector or None"""
    g=D['g']
    if not hasattr(D,'_gu'): pass
    key='_gu'
    if key not in D:
        D[key]=np.array([str(x).upper().split('.')[0] for x in g])
    m=np.where(D[key]==gene.upper())[0]
    if not len(m): return None
    k=m[np.argmax([np.nanmean(D['X'][q]) for q in m])]
    v=D['X'][k].astype(float)
    if D.get('logged'): return v
    return np.log2(np.clip(v,0,None)+1)
def groups(D,ra,rb):
    A=[i for i,l in enumerate(D['labels']) if re.search(ra,l,re.I)]
    B=[i for i,l in enumerate(D['labels']) if re.search(rb,l,re.I)]
    A=[i for i in A if i not in B]
    return A,B
def contrast(genes,ra,rb,minn=2,accs=None,quiet=True):
    out=[]
    for a in (accs or ALL()):
        D=get(a)
        if D is None: continue
        A,B=groups(D,ra,rb)
        if len(A)<minn or len(B)<minn: continue
        row={'acc':a,'nA':len(A),'nB':len(B),'org':D.get('org',''),'title':D.get('stitle','')[:70]}
        any_=False
        for gn in genes:
            v=val(D,gn)
            if v is None: row[gn]=None; continue
            d=float(np.nanmean(v[A])-np.nanmean(v[B]))
            row[gn]=round(d,2); any_=True
        if any_: out.append(row)
    return out
