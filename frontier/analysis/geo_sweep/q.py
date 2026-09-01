import numpy as np,glob,os,re,json
BASE=os.path.dirname(os.path.abspath(__file__))
_c={}
def acc_list(): return sorted(os.path.basename(f)[:-4] for f in glob.glob(BASE+'/cache/*.npz'))
def D(acc):
    if acc in _c: return _c[acc]
    z=np.load(BASE+'/cache/%s.npz'%acc,allow_pickle=True)
    d=dict(g=z['g'],X=z['X'],labels=[str(x) for x in z['labels']],kind=str(z['kind']),
           stitle=str(z['stitle']),org=str(z['org']),summary=str(z['summary']),acc=acc)
    d['gi']={s:i for i,s in enumerate(d['g'])}
    _c[acc]=d; return d
def v(d,gene):
    i=d['gi'].get(gene.upper())
    return None if i is None else d['X'][i].astype(float)
def grp(d,rx):
    return [i for i,l in enumerate(d['labels']) if re.search(rx,l,re.I)]
def contrast(genes,ra,rb,minn=2,accs=None,org=None):
    res=[]
    for a in (accs or acc_list()):
        d=D(a)
        if org and org.lower() not in d['org'].lower(): continue
        A=grp(d,ra); B=grp(d,rb); A=[i for i in A if i not in B]
        if len(A)<minn or len(B)<minn: continue
        row=dict(acc=a,nA=len(A),nB=len(B),org=d['org'].split(';')[0],title=d['stitle'][:64])
        hit=False
        for gn in genes:
            x=v(d,gn)
            if x is None: row[gn]=None
            else:
                row[gn]=round(float(np.nanmean(x[A])-np.nanmean(x[B])),2); hit=True
        if hit: res.append(row)
    return res
def show(rows,genes):
    if not rows: print('  (none)'); return
    hdr='%-11s %-3s %-3s %-22s '%('acc','nA','nB','organism')+' '.join('%8s'%g[:8] for g in genes)
    print(hdr); print('-'*len(hdr))
    for r in rows:
        print('%-11s %-3d %-3d %-22s '%(r['acc'],r['nA'],r['nB'],r['org'][:22])+
              ' '.join(('%8.2f'%r[g] if r.get(g) is not None else '       .') for g in genes))
