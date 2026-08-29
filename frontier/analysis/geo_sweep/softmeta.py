import json,urllib.request,os,re,time
from concurrent.futures import ThreadPoolExecutor
accs=json.load(open('gp_accs.json'))
os.makedirs('soft',exist_ok=True)
def one(a):
    o='soft/%s.txt'%a
    if os.path.exists(o) and os.path.getsize(o)>200: return 'have'
    u='https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=%s&targ=gsm&form=text&view=brief'%a
    for _ in range(3):
        try:
            t=urllib.request.urlopen(u,timeout=180).read().decode('utf8','replace')
            if len(t)>200: open(o,'w').write(t); return 'ok'
        except Exception: time.sleep(3)
    return 'miss'
with ThreadPoolExecutor(6) as ex: res=list(ex.map(one,accs))
from collections import Counter; print(Counter(res),flush=True)
