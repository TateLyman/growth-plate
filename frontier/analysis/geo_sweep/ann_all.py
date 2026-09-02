import json,os,urllib.request,gzip,re
from concurrent.futures import ThreadPoolExecutor
plats=json.load(open('platlist.json'))
os.makedirs('ann',exist_ok=True)
def one(p):
    o='ann/%s.annot'%p
    if os.path.exists(o) and os.path.getsize(o)>5000: return ('have',p)
    num=p[3:]; pre='GPL'+num[:-3]+'nnn' if len(num)>3 else 'GPLnnn'
    for d in [pre,'GPL'+num+'']:
        u="https://ftp.ncbi.nlm.nih.gov/geo/platforms/%s/%s/annot/%s.annot.gz"%(d,p,p)
        try:
            b=urllib.request.urlopen(u,timeout=180).read()
            if b[:2]==b'\x1f\x8b': b=gzip.decompress(b)
            open(o,'wb').write(b); return ('ok',p)
        except Exception: pass
    # fallback: full platform table via GEO accession viewer
    try:
        u="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=%s&targ=self&form=text&view=full"%p
        b=urllib.request.urlopen(u,timeout=300).read().decode('utf8','replace')
        L=[l for l in b.split('\n')]
        hi=[n for n,l in enumerate(L) if l.startswith('ID\t')]
        if not hi: return ('nohdr',p)
        hdr=L[hi[0]].split('\t')
        gi=None
        for cand in ['Gene symbol','Gene Symbol','GENE_SYMBOL','gene_assignment','Symbol','GeneSymbol','ORF','GB_ACC']:
            if cand in hdr: gi=hdr.index(cand); break
        if gi is None: return ('nogene:'+'|'.join(hdr[:8]),p)
        with open(o,'w') as fh:
            fh.write('ID\tx\tGene symbol\n')
            for l in L[hi[0]+1:]:
                pp=l.split('\t')
                if len(pp)>gi: fh.write('%s\tx\t%s\n'%(pp[0],pp[gi].split('//')[1].strip() if '//' in pp[gi] else pp[gi]))
        return ('viewer',p)
    except Exception as e: return ('fail:'+type(e).__name__,p)
with ThreadPoolExecutor(8) as ex: res=list(ex.map(one,plats))
from collections import Counter
print(Counter(x[0].split(':')[0] for x in res))
for s,p in res:
    if not s.startswith(('ok','have','viewer')): print(p,s)
