import sys;sys.path.insert(0,'.')
import q,numpy as np,re,json,itertools,random,statistics
IGN=set('IGF2 H19 DLK1 MEG3 RIAN MIRG RTL1 MEST PEG3 ZIM1 PLAGL1 CDKN1C KCNQ1OT1 AIRN IGF2R MAGEL2 NDN SNRPN GPC3 GRB10 PEG10 NNAT SGCE GNAS SLC38A4 PHLDA2 IMPACT MKRN3 BLCAP INPP5F NAP1L5 FAM50B DLGAP2 PPP1R9A OSBPL5 ASCL2 UBE3A MEG8 DIRAS3 L3MBTL1 ZNF597 MCTS2 PEG13'.split())
DRUG=re.compile(r'(unc06|unc0642|g9a|ehmt|bix|a-366|tsa|trichostatin|butyrate|valproic|vpa|romidepsin|vorinostat|saha|entinostat|ms-275|tacedinaline|ci-994|panobinostat|hdac|i-bet|jq1|bet |bromodomain|gsk-?j4|kdm6|dznep|ezh2|gsk126|epz|tazemetostat|5-?aza|azacitidine|decitabine|dnmt|zebularine|nicotinamide|topotecan|irinotecan|camptothecin|etoposide|indotecan|drug|treat|inhibitor|compound|dose|uM|nM|\dh\b|24h|48h|72h)',re.I)
CTRL=re.compile(r'(dmso|vehicle|control|untreated|ctrl|mock|parental|wt|wild)',re.I)
def groups(d):
    L=[str(l) for l in d['labels']];toks={}
    for i,l in enumerate(L):
        s=set(re.findall(r'[A-Za-z][A-Za-z0-9\-\+\.]{1,26}',l))|set(re.findall(r'[A-Za-z]+\s*[:=]\s*([^|]{1,26})',l))
        for t in s:
            t=t.strip().lower()
            if len(t)<2 or t in ('the','and','rep','sample','of','from','biological','replicate','tissue','type','cell','cells','line','strain','background','na','none','gender','male','female','mouse','human','rat','hours','hour','time'): continue
            toks.setdefault(t,set()).add(i)
    n=len(L);g={t:sorted(v) for t,v in toks.items() if 2<=len(v)<=n-2}
    seen=set();out={}
    for t,v in g.items():
        k=tuple(v)
        if k in seen: continue
        seen.add(k);out[t]=v
    return out
random.seed(21)
res=[]
for a in q.acc_list():
    try: d=q.D(a)
    except Exception: continue
    if len(d['labels'])<4: continue
    X=d['X'];ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,50)
    idx={str(g):i for i,g in enumerate(d['g'])}
    sel=[idx[g] for g in IGN if g in idx and ok[idx[g]]]
    if len(sel)<12: continue
    g=groups(d)
    if len(g)>45: g=dict(sorted(g.items(),key=lambda kv:-len(kv[1]))[:45])
    pool=np.array([i for i in range(len(ex)) if ok[i]])
    order={k:pool[np.argsort(np.abs(ex[pool]-ex[k]))[:120]] for k in sel}
    for (t1,A),(t2,B) in itertools.combinations(g.items(),2):
        if set(A)&set(B) or len(A)<2 or len(B)<2: continue
        if not (DRUG.search(t1) and CTRL.search(t2)) and not (DRUG.search(t2) and CTRL.search(t1)): continue
        if DRUG.search(t2) and CTRL.search(t1): A,B,t1,t2=B,A,t2,t1
        v=np.nanmean(X[:,A],axis=1)-np.nanmean(X[:,B],axis=1)
        if not np.isfinite(v[sel]).all(): continue
        bg=float(np.nanmean(v[ok]))
        sims=[np.mean([v[random.choice(order[k])] for k in sel]) for _ in range(400)]
        mu,sd=statistics.mean(sims),statistics.pstdev(sims)
        ign=float(np.nanmean(v[sel]))
        res.append(dict(acc=a,name='%s vs %s'%(t1,t2),ign=round(float(ign-bg),3),z=round(float((ign-mu)/sd) if sd else 0.0,2),
                        n=len(sel),org=d['org'].split(';')[0][:12],title=d['stitle'][:56]))
res.sort(key=lambda r:-r['z'])
json.dump(res,open('ign_drug_screen.json','w'),default=float)
print('drug-vs-control contrasts scored:',len(res))
print('\n===== RAISES THE IMPRINTED NETWORK =====')
for r in res[:40]: print('%+6.2f z  IGN%+6.2f  %-11s %-12s %-30s | %s'%(r['z'],r['ign'],r['acc'],r['org'],r['name'][:30],r['title']))
print('\n===== LOWERS IT =====')
for r in res[-12:]: print('%+6.2f z  IGN%+6.2f  %-11s %-12s %-30s | %s'%(r['z'],r['ign'],r['acc'],r['org'],r['name'][:30],r['title']))
