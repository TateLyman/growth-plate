"""Index the 506 downloaded trials that measured a stature endpoint AND posted results.
The losartan finding came from exactly this shape of record.  Rank by: is the
intervention plausibly ACTING ON THE GROWTH PLATE, and is the population GROWING?"""
import json, glob, re, collections, csv

GROWTH = re.compile(r"\b(height|stature|body length|growth velocity|height velocity|adult height|"
  r"final height|near[- ]adult height|standing height|bone age|height sds|height z|"
  r"height-for-age|segment ratio|arm span|sitting height|limb length|leg length|"
  r"femur length|tibia length|growth rate|length velocity)\b", re.I)
NOISE = re.compile(r"growth factor|tumou?r growth|hair growth|weight[- ]for[- ]height", re.I)
# interventions whose growth effect is ALREADY the point - not news
KNOWN = re.compile(r"somatropin|growth hormone|\bgh\b|norditropin|genotropin|humatrope|"
  r"omnitrope|saizen|nutropin|somatrogon|lonapegsomatropin|skytrofa|ngenla|vosoritide|"
  r"voxzogo|igf-1|mecasermin|increlex|oxandrolone|testosterone|estrogen|estradiol|"
  r"anastrozole|letrozole|leuprolide|triptorelin|gnrh", re.I)

rows=[]
for p in glob.glob("ctg/*.json"):
    d=json.load(open(p)); ps=d.get("protocolSection",{})
    nct=ps.get("identificationModule",{}).get("nctId")
    om=ps.get("outcomesModule",{}) or {}
    outs=[(t,x.get("measure","")) for t,k in (("P","primaryOutcomes"),("S","secondaryOutcomes"),("O","otherOutcomes"))
          for x in (om.get(k) or [])]
    g=[(t,m) for t,m in outs if GROWTH.search(m) and not NOISE.search(m)]
    if not g: continue
    iv=", ".join(i.get("name","") for i in (ps.get("armsInterventionsModule") or {}).get("interventions",[]))
    cond=", ".join((ps.get("conditionsModule") or {}).get("conditions",[]))
    el=ps.get("eligibilityModule") or {}
    minage=el.get("minimumAge",""); maxage=el.get("maximumAge","")
    child = bool(re.search(r"CHILD",str(el.get("stdAges",""))))
    # is a growth endpoint actually REPORTED in the results section?
    rs=d.get("resultsSection",{}) or {}
    oms=(rs.get("outcomeMeasuresModule") or {}).get("outcomeMeasures") or []
    reported=[o.get("title","") for o in oms if GROWTH.search(o.get("title","") or "") and not NOISE.search(o.get("title","") or "")]
    rows.append(dict(nct=nct, n=((ps.get("designModule") or {}).get("enrollmentInfo") or {}).get("count"),
        title=ps.get("identificationModule",{}).get("briefTitle","")[:110],
        cond=cond[:70], iv=iv[:80], child=child, minage=minage, maxage=maxage,
        n_growth_planned=len(g), n_growth_reported=len(reported),
        reported=reported[:4], known=bool(KNOWN.search(iv+" "+cond)),
        status=(ps.get("statusModule") or {}).get("overallStatus","")))
rows.sort(key=lambda r:(-r["n_growth_reported"], -(r["n"] or 0)))
json.dump(rows, open("ctg_index.json","w"), indent=1)
tot=[r for r in rows if r["n_growth_reported"]]
novel=[r for r in tot if not r["known"] and r["child"]]
print(f"{len(rows)} trials with a planned stature endpoint and posted results")
print(f"{len(tot)} actually REPORT a stature outcome in the results section")
print(f"{len(novel)} of those are in CHILDREN with an intervention NOT already a growth drug\n")
print("=== the unexamined set: growing children, non-growth drug, height reported ===")
for r in novel[:45]:
    print(f"{r['nct']}  n={str(r['n']):<6} {r['iv'][:44]:<44} | {r['cond'][:34]:<34} | {r['reported'][0][:50]}")
with open("ctg_index.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["nct","n","child","known_growth_drug","n_growth_reported","intervention","condition","first_reported_growth_outcome","title"])
    for r in rows: w.writerow([r["nct"],r["n"],r["child"],r["known"],r["n_growth_reported"],r["iv"],r["cond"],(r["reported"] or [""])[0],r["title"]])
