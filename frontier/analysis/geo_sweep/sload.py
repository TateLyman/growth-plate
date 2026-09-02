import numpy as np,re,os,gzip,io
SEPS=['\t',',',';',' ']
def sniff(path,maxb=4_000_000):
    with open(path,'rb') as f: head=f.read(maxb)
    if head[:2]==b'\x1f\x8b':
        try: head=gzip.GzipFile(fileobj=io.BytesIO(head)).read()
        except Exception: pass
    t=head.decode('utf8','replace')
    lines=[l for l in t.split('\n') if l.strip()][:60]
    if not lines: return None
    best=max(SEPS,key=lambda s: min(l.count(s) for l in lines[:12]) if len(lines)>=12 else lines[0].count(s))
    return best
GENECOL=re.compile(r'^(gene|genes|gene_?name|gene_?symbol|symbol|geneid|gene_?id|id|name|ensembl|feature|tracking_id|X|)$',re.I)
def load_tbl(path,maxrows=200000):
    sep=sniff(path)
    if not sep: return None
    op=gzip.open if open(path,'rb').read(2)==b'\x1f\x8b' else open
    with op(path,'rt',encoding='utf8',errors='replace') as f:
        hdr=None
        for l in f:
            if l.strip(): hdr=l.rstrip('\n').split(sep); break
        if hdr is None: return None
        rows=[];n=0
        for l in f:
            if not l.strip(): continue
            p=l.rstrip('\n').split(sep)
            rows.append(p); n+=1
            if n>=maxrows: break
    if not rows: return None
    w=max(len(hdr),max(len(r) for r in rows))
    if len(hdr)==w-1: hdr=['GENE']+hdr   # rownames header omitted
    hdr=[h.strip().strip('"') for h in hdr]
    # find numeric columns
    ref=rows[min(5,len(rows)-1)]
    numcols=[]
    for i in range(1,w):
        good=0
        for r in rows[:40]:
            if i<len(r):
                try: float(r[i].strip('"')); good+=1
                except Exception: pass
        if good>=30: numcols.append(i)
    if len(numcols)<2: return None
    # gene id column: prefer a text column whose header looks gene-like, else col0
    txt=[i for i in range(w) if i not in numcols]
    gi=txt[0] if txt else 0
    for i in txt:
        if i<len(hdr) and re.search(r'(symbol|gene_?name|^gene$|^name$)',hdr[i],re.I): gi=i;break
    g=np.array([ (r[gi].strip('"') if gi<len(r) else '') for r in rows])
    X=np.full((len(rows),len(numcols)),np.nan)
    for a,r in enumerate(rows):
        for b,i in enumerate(numcols):
            if i<len(r):
                try: X[a,b]=float(r[i].strip('"'))
                except Exception: pass
    cols=[hdr[i] if i<len(hdr) else 'c%d'%i for i in numcols]
    return dict(g=g,X=X,cols=cols,path=path)
