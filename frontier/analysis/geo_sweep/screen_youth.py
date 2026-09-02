import sys,os;sys.path.insert(0,'.')
import q,youth,numpy as np,re,json,itertools
# auto-generate contrasts from sample labels
def groups(d):
    L=[l for l in d['labels']]
    toks={}
    for i,l in enumerate(L):
        s=set(re.findall(r'[A-Za-z][A-Za-z0-9\-\+\.]{1,26}',l))
        s|=set(re.findall(r'[A-Za-z]+\s*[:=]\s*([^|]{1,26})',l))
        for t in s:
            t=t.strip().lower()
            if len(t)<2 or t in ('the','and','rep','sample','of','from','biological','replicate','tissue','type','cell','cells','strain','background','age','na','none','gender','male','female','mouse','human','rat','mus','musculus'): continue
            toks.setdefault(t,set()).add(i)
    n=len(L)
    g={t:sorted(v) for t,v in toks.items() if 2<=len(v)<=n-2}
    # dedupe identical index sets
    seen={};out={}
    for t,v in g.items():
        k=tuple(v)
        if k in seen: continue
        seen[k]=t; out[t]=v
    return out
res=[]
accs=q.acc_list()
for a in accs:
    try: d=q.D(a)
    except Exception: continue
    if len(d['labels'])<4: continue
    g=groups(d)
    if len(g)>60: g=dict(list(sorted(g.items(),key=lambda kv:-len(kv[1])))[:60])
    for (t1,A),(t2,B) in itertools.combinations(g.items(),2):
        if set(A)&set(B): continue
        if len(A)<2 or len(B)<2: continue
        try: s=youth.score(a,A,B,'%s vs %s'%(t1,t2))
        except Exception: s=None
        if s: s['org']=d['org'].split(';')[0][:14]; s['title']=d['stitle'][:60]; res.append(s)
res.sort(key=lambda r:-r['r'])
json.dump(res,open('youth_screen.json','w'))
print('contrasts scored:',len(res))
print('\n===== MOST YOUTHFUL / LENGTHENING (top r) =====')
for r in res[:40]:
    print('%+.3f  %-11s %-13s %-34s | %s'%(r['r'],r['acc'],r['org'],r['name'][:34],r['title']))
print('\n===== MOST AGEING / SHORTENING (bottom r) =====')
for r in res[-25:]:
    print('%+.3f  %-11s %-13s %-34s | %s'%(r['r'],r['acc'],r['org'],r['name'][:34],r['title']))
