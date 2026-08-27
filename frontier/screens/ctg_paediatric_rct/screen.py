#!/usr/bin/env python3
"""
PAEDIATRIC RCT HEIGHT SCREEN
============================
Instrument: the ClinicalTrials.gov results database. Every long-term paediatric drug trial
records height as a safety variable. Unlike FAERS (adverse-only) and unlike the juvenile
toxicity packages (adverse-only), a continuous height outcome is BIDIRECTIONAL: a drug that
makes children taller is as visible as one that makes them shorter.

Output: (a) a measured BASE RATE - the null distribution of drug-minus-control height
differences in paediatric RCTs, which no screen in this field has ever had; (b) the signed
ranked list against that base rate.

Nothing here is inferred. Every number is read from a posted results table.
"""
import json,re,math,statistics,csv,sys
S=json.load(open("ctg_raw/studies.json"))

HEIGHT=re.compile(r'\b(height|stature|statural|body length|crown[- ]heel|growth velocity|linear growth)\b',re.I)
NOTHEIGHT=re.compile(r'(peak height|wave height|fundal|papilla|amplitude|bone marrow|st[- ]segment|'
    r'jump|ridge height|crest height|gingival|alveolar|disc height|voice|weight[- ]for[- ]height|'
    r'percentage of (participants|subjects)|number of (participants|subjects)|below the third|'
    r'bmi|body mass index|weight for height|blood pressure|percentile for age)',re.I)
CTRL=re.compile(r'\b(placebo|control|vehicle|comparator|standard of care|no treatment|observation|'
    r'untreated|usual care|sham|non[- ]?treated)\b',re.I)
# a control arm that is itself an active growth-relevant drug is NOT a clean control
ACTIVECTRL=re.compile(r'(somatropin|growth hormone|estradiol|estrogen|testosterone|metformin)',re.I)
UNITS=[('cm/yr',re.compile(r'cm\s*/?\s*(year|yr)',re.I)),
       ('cm',re.compile(r'^\s*(cm|cm\.|centimeters?|centimeter \(cm\)|centimeters \(cm\)|centimetre)\s*$',re.I)),
       ('Z',re.compile(r'^\s*(z[- ]?scores?|sds|standard deviations?|standard deviation score \(sds\) units|z score)\s*$',re.I))]
CHANGE=re.compile(r'\b(change|velocity|rate of|gain)\b',re.I)
BASECAT=re.compile(r'\bbaseline\b',re.I)
DRUGTYPES={'DRUG','BIOLOGICAL','DIETARY_SUPPLEMENT','COMBINATION_PRODUCT'}
GROWTHDRUG=re.compile(r'(somatropin|somapacitan|lonapegsomatropin|growth hormone|\bGH\b|igf-?1|mecasermin|'
    r'vosoritide|BMN.?111|navepegritide|infigratinib|recifercept|oxandrolone|anastrozole|letrozole|'
    r'testosterone|estradiol|leuprolide|triptorelin|histrelin|GnRH)',re.I)
GROWTHDX=re.compile(r'(short stature|growth hormone deficien|turner|achondroplasia|hypochondroplasia|'
    r'small for gestational age|\bSGA\b|idiopathic short|growth failure|hypopituitar|noonan|'
    r'prader[- ]willi|russell[- ]silver|SHOX|growth retardation|dwarf|skeletal dysplasia|'
    r'growth disorder|panhypopit|constitutional delay|precocious puberty|tall stature)',re.I)
# indications where any effect is RESTORATION of a deficit, not ELEVATION of a normal plate
# (the atlas's CORR-203). Kept and labelled, not dropped.
RESTORE=re.compile(r'(hypophosphat|rickets|mucopolysacchar|hunter|hurler|morquio|gaucher|pompe|'
    r'chronic kidney|renal fail|dialysis|cystic fibrosis|malnutrition|malnourish|stunt|wasting|'
    r'undernutrition|failure to thrive|celiac|coeliac|crohn|inflammatory bowel|colitis|'
    r'arthritis|\bhiv\b|thalassemia|sickle|spinal muscular|retinopathy of prematurity|preterm|'
    r'very low birth|hypothyroid|adrenal hyperplasia|an(a)?emia|transplant|leuk(a)?emia|cancer|'
    r'deficiency|hypogonad|nephrotic|eosinophilic esophagitis|hepatitis|malaria|diarrh|'
    r'enteropathy|schistosom|tuberculosis|epilep|seizure|dravet|lennox|asthma|rhinitis|'
    r'atopic dermatitis|dermatitis|psoriasis|obes)',re.I)

def unit_of(u):
    for name,rx in UNITS:
        if rx.search(u) if name=='cm/yr' else rx.match(u): return name
    return None
def as_int(x):
    try: return int(x)
    except: return 0
def as_f(x):
    try: return float(x)
    except: return None

comparisons=[];trials=set();skipped={}
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
    is_growthdx=bool(GROWTHDX.search(ctx))
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
                gs=[g for g in gs if g[3]>=20]
                ctrls=[g for g in gs if CTRL.search(g[0]) and not ACTIVECTRL.search(g[0])]
                drugs=[g for g in gs if not CTRL.search(g[0])]
                if not ctrls or not drugs: continue
                ctrl=max(ctrls,key=lambda g:g[3])
                for d in drugs:
                    se=None
                    if d[2] and ctrl[2] and om.get('dispersionType')=='STANDARD_DEVIATION':
                        se=math.sqrt(d[2]**2/d[3]+ctrl[2]**2/ctrl[3])
                    comparisons.append(dict(nct=nct,cond=conds,title=title,ivnames=ivnames,
                        u=u,outcome=t,cat=catname,growthdx=is_growthdx,
                        growthdrug=bool(GROWTHDRUG.search(d[0]+' '+ivnames)),
                        restore=bool(RESTORE.search(ctx)),
                        drug=d[0],dv=d[1],dsd=d[2],dn=d[3],
                        ctl=ctrl[0],cv=ctrl[1],csd=ctrl[2],cn=ctrl[3],
                        diff=d[1]-ctrl[1],se=se,z=(d[1]-ctrl[1])/se if se else None))
                    trials.add(nct)

print(f"COMPARISONS: {len(comparisons)} arm-vs-control contrasts from {len(trials)} trials\n")
json.dump(comparisons,open("ctg_raw/comparisons.json","w"),indent=1,default=str)

# ---- POSITIVE CONTROL (the atlas's own: losartan trial NCT00429364, 0.822 vs 0.935 cm/yr)
pc=[c for c in comparisons if c['nct']=='NCT00429364']
print("POSITIVE CONTROL NCT00429364 (Marfan losartan vs atenolol, atlas value 0.822 vs 0.935 cm/yr):")
for c in pc: print(f"   {c['outcome'][:60]} | {c['drug'][:28]}={c['dv']} vs {c['ctl'][:28]}={c['cv']} {c['u']}")
if not pc: print("   [not recovered - control arm is an active comparator (atenolol), excluded by design]")

def summarise(rows,label):
    if not rows: return
    d=[x['diff'] for x in rows]
    pos=sum(1 for x in d if x>0)
    print(f"{label:52s} n={len(d):4d}  median {statistics.median(d):+7.3f}  "
          f"mean {statistics.mean(d):+7.3f}  pos {pos:3d}/{len(d):3d} ({100*pos/len(d):3.0f}%)  "
          f"[{min(d):+.2f},{max(d):+.2f}]")

print("\n"+"="*104)
print("BASE RATE — the null distribution nobody in this field has measured")
print("="*104)
for u in ('cm/yr','cm','Z'):
    sub=[c for c in comparisons if c['u']==u]
    print(f"\n--- unit: {u} ---")
    summarise(sub,"  ALL paediatric drug-vs-control contrasts")
    summarise([c for c in sub if not c['growthdrug'] and not c['growthdx']],"  EXCLUDING growth drugs and growth diagnoses")
    summarise([c for c in sub if not c['growthdrug'] and not c['growthdx'] and not c['restore']],
              "  ...and EXCLUDING deficit/restoration indications")
    summarise([c for c in sub if c['growthdrug'] or c['growthdx']],"  growth drugs / growth diagnoses only (control)")
