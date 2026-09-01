import json,os,re,urllib.request,gzip
from concurrent.futures import ThreadPoolExecutor
S=json.load(open('suppl.json'))
GOOD=re.compile(r'(count|tpm|fpkm|rpkm|matrix|expression|_norm|normali|rsem|deseq|gene)',re.I)
BAD=re.compile(r'(\.tar$|barcode|\.mtx|features\.tsv|\.bw$|\.bigwig|peak|\.h5$|\.bam|\.bed|\.narrowPeak|\.pdf|\.png|\.xlsx?$|filtered_feature)',re.I)
CAP=400_000_000
jobs=[]
for a,fs in S.items():
    pick=[f for f in fs if GOOD.search(f) and not BAD.search(f)]
    for f in pick[:4]: jobs.append((a,f))
print('jobs',len(jobs))
def one(j):
    a,f=j
    o='sup/%s__%s'%(a,f.replace('/','_'))
    o=re.sub(r'\.gz$','',o)
    if os.path.exists(o): return 'have'
    n=re.sub(r'\d{1,3}$','nnn',a)
    u="https://ftp.ncbi.nlm.nih.gov/geo/series/%s/%s/suppl/%s"%(n,a,f)
    try:
        r=urllib.request.urlopen(u,timeout=300)
        b=r.read(CAP)
        if f.endswith('.gz'):
            try: b=gzip.decompress(b)
            except Exception:
                try: b=gzip.GzipFile(fileobj=__import__('io').BytesIO(b)).read()
                except Exception: pass
        open(o,'wb').write(b); return 'ok'
    except Exception as e: return 'fail'
with ThreadPoolExecutor(10) as ex: res=list(ex.map(one,jobs))
from collections import Counter; print(Counter(res))
