#!/usr/bin/env python3
"""Adds: (a) ALL-PAIRS mode so active-comparator trials are visible (recovers the atlas's
own losartan positive control), (b) n>=10, (c) the signed per-drug table."""
import json,re,math,statistics,itertools,csv
exec(open("screen.py").read().split("comparisons=[];trials=set()")[0].split('"""',2)[2])
S=json.load(open("ctg_raw/studies.json"))

def as_int(x):
    try: return int(x)
    except: return 0
def as_f(x):
    try: return float(x)
    except: return None
def unit_of(u):
    for name,rx in UNITS:
        if (rx.search(u) if name=='cm/yr' else rx.match(u)): return name
    return None

recs=[]
for nct,s in S.items():
    p=s.get('protocolSection',{});r=s.get('resultsSection',{})
    if not r: continue
    dm=p.get('designModule',{})
    if dm.get('studyType')!='INTERVENTIONAL': continue
    elig=p.get('eligibilityModule',{})
    if not ({'CHILD','ADOLESCENT'} & set(elig.get('stdAges',[]) or [])): continue
    ivs=p.get('armsInterventionsModule',{}).get('interventions',[]) or []
    if not ({i.get('type') for i in ivs} & DRUGTYPES): continue
    ivnames=' ; '.join(i.get('name','') for i in ivs)
    title=p.get('identificationModule',{}).get('briefTitle','')
    conds=' ; '.join(p.get('conditionsModule',{}).get('conditions',[]) or [])
    ctx=conds+' '+title
    for om in r.get('outcomeMeasuresModule',{}).get('outcomeMeasures',[]) or []:
        t=om.get('title','') or ''
        if not HEIGHT.search(t) or NOTHEIGHT.search(t) or not CHANGE.search(t): continue
        u=unit_of((om.get('unitOfMeasure') or '').strip())
        if not u: continue
        groups={g['id']:g.get('title','') for g in om.get('groups',[]) or []}
        den={}
        for d in om.get('denoms',[]) or []:
            for c in d.get('counts',[]) or []: den[c['groupId']]=as_int(c.get('value'))
        for cl in om.get('classes',[]) or []:
            for cat in cl.get('categories',[]) or []:
                catname=((cat.get('title') or '')+'|'+(cl.get('title') or '')).strip('|')
                if BASECAT.search(catname): continue
                gs=[]
                for m in cat.get('measurements',[]) or []:
                    v=as_f(m.get('value'))
                    if v is None: continue
                    gid=m['groupId']
                    gs.append((groups.get(gid,gid),v,as_f(m.get('spread')),den.get(gid,0)))
                gs=[g for g in gs if g[3]>=10]
                if len(gs)<2: continue
                named=[g for g in gs if CTRL.search(g[0])]
                mode='placebo' if named else 'active-comparator'
                ref=max(named,key=lambda g:g[3]) if named else min(gs,key=lambda g:g[1])
                for d in gs:
                    if d is ref: continue
                    se=math.sqrt(d[2]**2/d[3]+ref[2]**2/ref[3]) if (d[2] and ref[2] and om.get('dispersionType')=='STANDARD_DEVIATION') else None
                    recs.append(dict(nct=nct,cond=conds,title=title,ivnames=ivnames,mode=mode,u=u,
                        outcome=t,cat=catname,
                        growthdx=bool(GROWTHDX.search(ctx)),
                        growthdrug=bool(GROWTHDRUG.search(d[0]+' '+ivnames)),
                        restore=bool(RESTORE.search(ctx)),
                        arm=d[0],av=d[1],asd=d[2],an=d[3],ref=ref[0],rv=ref[1],rn=ref[3],
                        diff=round(d[1]-ref[1],4),se=round(se,4) if se else None,
                        z=round((d[1]-ref[1])/se,2) if se else None))
json.dump(recs,open("ctg_raw/allpairs.json","w"),indent=1)
print(f"ALL CONTRASTS: {len(recs)} from {len({r['nct'] for r in recs})} trials  "
      f"(placebo-controlled {sum(1 for r in recs if r['mode']=='placebo')}, "
      f"active-comparator {sum(1 for r in recs if r['mode']!='placebo')})\n")

pc=[c for c in recs if c['nct']=='NCT00429364']
print("POSITIVE CONTROL — NCT00429364, Marfan, losartan vs atenolol. Atlas hand-read: 0.822 vs 0.935 cm/yr")
for c in pc[:4]:
    print(f"   RECOVERED: {c['arm'][:26]}={c['av']} vs {c['ref'][:26]}={c['rv']} {c['u']} | {c['outcome'][:55]}")
print()

with open("results_all_contrasts.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(recs[0].keys()));w.writeheader();w.writerows(recs)

print("="*106)
print("THE SIGNED LIST — non-growth drug, non-growth diagnosis, placebo-controlled, ranked by height difference")
print("="*106)
clean=[c for c in recs if not c['growthdrug'] and not c['growthdx'] and c['mode']=='placebo']
for u in ('cm/yr','cm','Z'):
    sub=sorted([c for c in clean if c['u']==u],key=lambda z:-z['diff'])
    if not sub: continue
    print(f"\n### {u}  (n={len(sub)})")
    for c in sub:
        tag='deficit' if c['restore'] else 'NORMAL '
        zs=f"z={c['z']:+.2f}" if c['z'] is not None else "z=  n/a"
        print(f"  {c['diff']:+8.3f} {zs} [{tag}] {c['nct']} n={c['an']}/{c['rn']}  {c['cond'][:38]}")
        print(f"           {c['arm'][:46]} ({c['av']}) vs {c['ref'][:26]} ({c['rv']})  <- {c['outcome'][:62]}")
