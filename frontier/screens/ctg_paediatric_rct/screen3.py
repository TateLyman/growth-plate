#!/usr/bin/env python3
"""Final pass: correct SE handling (Standard Error vs Standard Deviation), z and two-sided p."""
import json,re,math,statistics,csv
src=open("screen.py").read()
exec(src.split("comparisons=[];trials=set()")[0].split('"""',2)[2])
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
def phi(z): return 0.5*(1+math.erf(z/math.sqrt(2)))
def pval(z): return 2*(1-phi(abs(z)))

recs=[]
for nct,s in S.items():
    p=s.get('protocolSection',{});r=s.get('resultsSection',{})
    if not r: continue
    dm=p.get('designModule',{})
    if dm.get('studyType')!='INTERVENTIONAL': continue
    if (dm.get('designInfo',{}) or {}).get('allocation')!='RANDOMIZED': continue
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
        disp=(om.get('dispersionType') or '')
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
                named=[g for g in gs if CTRL.search(g[0])]
                if not named: continue
                ref=max(named,key=lambda g:g[3])
                for d in gs:
                    if d is ref or CTRL.search(d[0]): continue
                    se=None
                    if d[2] is not None and ref[2] is not None:
                        if disp.lower().startswith('standard error'): se=math.sqrt(d[2]**2+ref[2]**2)
                        elif disp.lower().startswith('standard deviation'): se=math.sqrt(d[2]**2/d[3]+ref[2]**2/ref[3])
                    diff=d[1]-ref[1]
                    recs.append(dict(nct=nct,cond=conds[:60],title=title[:80],ivnames=ivnames[:80],u=u,
                        outcome=t[:95],cat=catname[:40],disp=disp,
                        growthdx=bool(GROWTHDX.search(ctx)),growthdrug=bool(GROWTHDRUG.search(d[0]+' '+ivnames)),
                        restore=bool(RESTORE.search(ctx)),
                        arm=d[0][:55],av=d[1],an=d[3],ref=ref[0][:35],rv=ref[1],rn=ref[3],
                        diff=round(diff,4),se=round(se,4) if se else None,
                        z=round(diff/se,3) if se else None,p=round(pval(diff/se),5) if se else None))
with open("results_randomised_placebo_controlled.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(recs[0].keys()));w.writeheader();w.writerows(recs)
json.dump(recs,open("ctg_raw/final.json","w"),indent=1)

clean=[c for c in recs if not c['growthdrug'] and not c['growthdx']]
print(f"RANDOMISED + placebo/control arm + paediatric + drug + height-change outcome")
print(f"  contrasts: {len(recs)} from {len({c['nct'] for c in recs})} trials")
print(f"  after removing growth drugs & growth diagnoses: {len(clean)} from {len({c['nct'] for c in clean})} trials\n")
for u in ('cm','cm/yr','Z'):
    for lbl,rows in (("ALL",[c for c in recs if c['u']==u]),
                     ("non-growth drug & non-growth dx",[c for c in clean if c['u']==u]),
                     ("  ...also non-deficit indication",[c for c in clean if c['u']==u and not c['restore']]),
                     ("growth drugs/dx (internal +ve control)",[c for c in recs if c['u']==u and (c['growthdrug'] or c['growthdx'])])):
        if not rows: continue
        d=[x['diff'] for x in rows];pos=sum(1 for x in d if x>0)
        print(f"{u:6s} {lbl:40s} n={len(d):3d} median {statistics.median(d):+7.3f} pos {pos:3d}/{len(d):3d} ({100*pos/len(d):3.0f}%)")
    print()
print("="*100)
print("SIGNIFICANT CONTRASTS (p<0.05), non-growth drug & non-growth diagnosis")
print("="*100)
sig=sorted([c for c in clean if c['p'] is not None and c['p']<0.05],key=lambda z:z['diff'])
for c in sig:
    print(f"{c['diff']:+7.3f} {c['u']:5s} z={c['z']:+6.2f} p={c['p']:.4f} | {c['nct']} n={c['an']}/{c['rn']} | {c['cond'][:40]}")
    print(f"        {c['arm'][:50]} ({c['av']}) vs {c['ref'][:28]} ({c['rv']})")
    print(f"        {c['outcome'][:92]} [{c['cat']}]")
print(f"\n(of {sum(1 for c in clean if c['p'] is not None)} contrasts with computable p)")
