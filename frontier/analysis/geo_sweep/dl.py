import json,os,urllib.request,gzip,time,re,sys
keep=json.load(open('keep.json'))
def fetch(url,out):
    if os.path.exists(out) and os.path.getsize(out)>1000: return True
    try:
        d=urllib.request.urlopen(url,timeout=180).read()
        if d[:2]==b'\x1f\x8b': d=gzip.decompress(d)
        if len(d)<1000: return False
        open(out,'wb').write(d); return True
    except Exception: return False
ok=0
for r in keep:
    a=r['acc']; n=re.sub(r'\d{1,3}$','nnn',a)
    u=f"https://ftp.ncbi.nlm.nih.gov/geo/series/{n}/{a}/matrix/{a}_series_matrix.txt.gz"
    if fetch(u,f'mat/{a}.txt'): ok+=1
    else: print('miss',a,flush=True)
print('downloaded',ok,'of',len(keep))
