import sys;sys.path.insert(0,'.')
import q,numpy as np,re,json,itertools
IGN=['IGF2','H19','DLK1','MEG3','RIAN','MIRG','RTL1','MEST','PEG3','ZIM1','PLAGL1','CDKN1C','KCNQ1OT1','AIRN','IGF2R','MAGEL2','NDN','GPC3','GRB10','PEG10','NNAT','SGCE','GNAS','SLC38A4','PHLDA2','PLAG1','IMPACT','MKRN3','BLCAP','INPP5F','NAP1L5','FAM50B','ZFAT','GLIS3','DLGAP2','PPP1R9A','OSBPL5','ASCL2']
def groups(d):
    L=[str(l) for l in d['labels']];toks={}
    for i,l in enumerate(L):
        s=set(re.findall(r'[A-Za-z][A-Za-z0-9\-\+\.]{1,26}',l))|set(re.findall(r'[A-Za-z]+\s*[:=]\s*([^|]{1,26})',l))
        for t in s:
            t=t.strip().lower()
            if len(t)<2 or t in ('the','and','rep','sample','of','from','biological','replicate','tissue','type','cell','cells','strain','background','na','none','gender','male','female','mouse','human','rat','mus','musculus','norvegicus','sapiens'): continue
            toks.setdefault(t,set()).add(i)
    n=len(L); g={t:sorted(v) for t,v in toks.items() if 2<=len(v)<=n-2}
    seen=set();out={}
    for t,v in g.items():
        k=tuple(v)
        if k in seen: continue
        seen.add(k); out[t]=v
    return out
res=[]
for a in q.acc_list():
    try: d=q.D(a)
    except Exception: continue
    if len(d['labels'])<4: continue
    X=d['X']; ex=np.nanmax(X,axis=1); ok=ex>np.nanpercentile(ex,55)
    idx={str(g):i for i,g in enumerate(d['g'])}
    sel=[idx[g] for g in IGN if g in idx and ok[idx[g]]]
    if len(sel)<10: continue
    g=groups(d)
    if len(g)>40: g=dict(sorted(g.items(),key=lambda kv:-len(kv[1]))[:40])
    for (t1,A),(t2,B) in itertools.combinations(g.items(),2):
        if set(A)&set(B) or len(A)<2 or len(B)<2: continue
        v=np.nanmean(X[:,A],axis=1)-np.nanmean(X[:,B],axis=1)
        bg=float(np.nanmean(v[ok]))
        ign=float(np.nanmean(v[sel]))-bg
        if not np.isfinite(ign): continue
        res.append(dict(acc=a,name='%s vs %s'%(t1,t2),ign=round(ign,3),n=len(sel),
                        org=d['org'].split(';')[0][:13],title=d['stitle'][:52]))
res.sort(key=lambda r:-r['ign'])
json.dump(res,open('ign_screen.json','w'))
print('contrasts:',len(res))
print('\n===== RAISES THE IMPRINTED GENE NETWORK (above dataset background) =====')
for r in res[:45]: print('%+6.2f n=%-3d %-11s %-13s %-30s | %s'%(r['ign'],r['n'],r['acc'],r['org'],r['name'][:30],r['title']))
