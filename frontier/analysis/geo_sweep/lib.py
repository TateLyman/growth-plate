import numpy as np,glob,os,re
def load(acc):
    f='mat/%s.txt'%acc
    L=open(f,encoding='utf-8',errors='replace').read().split('\n')
    meta={}
    for l in L:
        if l.startswith('!Sample_'):
            k=l.split('\t')[0][1:]
            v=[x.strip().strip('"') for x in l.split('\t')[1:]]
            meta.setdefault(k,[]).append(v)
        if l.startswith('!Series_platform_id'): plat=l.split('\t')[1].strip().strip('"')
    try:
        i=[n for n,l in enumerate(L) if l.startswith('!series_matrix_table_begin')][0]
        j=[n for n,l in enumerate(L) if l.startswith('!series_matrix_table_end')][0]
    except IndexError: return None
    rows=[l.split('\t') for l in L[i+2:j] if l.strip()]
    if not rows: return None
    ids=np.array([x[0].strip('"') for x in rows])
    X=np.array([[float(v) if v not in ('','null','NA','NaN') else np.nan for v in x[1:]] for x in rows])
    ann='ann/%s.annot'%plat
    sym=None
    if os.path.exists(ann):
        sym={}
        for l in open(ann,encoding='utf-8',errors='replace'):
            p=l.rstrip('\n').split('\t')
            if len(p)>2 and not p[0].startswith(('#','!','^')): sym[p[0]]=p[2]
    g=np.array([sym.get(x,'') if sym else '' for x in ids])
    titles=meta.get('Sample_title',[[]])[0]
    chars=[' | '.join(c[k] for c in meta.get('Sample_characteristics_ch1',[]) ) for k in range(len(titles))] \
          if meta.get('Sample_characteristics_ch1') else ['']*len(titles)
    return dict(acc=acc,plat=plat,X=X,ids=ids,g=g,titles=titles,chars=chars,
                logged=bool(np.nanmax(X)<30))
def val(D,gene):
    m=np.where(D['g']==gene)[0]
    if not len(m): return None
    k=m[np.argmax([np.nanmean(D['X'][q]) for q in m])]
    v=D['X'][k].astype(float)
    return np.log2(v+1) if not D['logged'] else v
