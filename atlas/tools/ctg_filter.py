import json, re, urllib.request, urllib.parse, time
rows = json.load(open("ctg_sweep.raw.json"))
GROWTH = re.compile(r"\b(height|stature|body length|growth velocity|height velocity|adult height|"
  r"final height|near[- ]adult height|standing height|bone age|height sds|height z|"
  r"height-for-age|segment ratio|arm span|sitting height|limb length|leg length|"
  r"femur length|tibia length|growth rate|length velocity)\b", re.I)
NOISE = re.compile(r"growth factor|tumou?r growth|hair growth|bacterial growth|weight[- ]for[- ]height|"
  r"height of |growth hormone (level|concentration)|body mass index for height", re.I)

def outcomes(p):
    om = p.get("outcomesModule") or {}
    o = []
    for k, tag in (("primaryOutcomes","P"),("secondaryOutcomes","S"),("otherOutcomes","O")):
        for x in om.get(k) or []:
            o.append((tag, x.get("measure","")))
    return o

keep = []
for r in rows:
    p = r["rec"].get("protocolSection", {})
    o = outcomes(p)
    hits = [(t,m) for t,m in o if GROWTH.search(m) and not NOISE.search(m)]
    if not hits: continue
    im, sm, cm = p.get("identificationModule",{}), p.get("statusModule",{}), p.get("conditionsModule",{})
    keep.append(dict(nct=r["nct"], found_by=r["found_by"],
        title=im.get("briefTitle",""), status=sm.get("overallStatus",""),
        start=(sm.get("startDateStruct") or {}).get("date",""),
        n=((p.get("designModule") or {}).get("enrollmentInfo") or {}).get("count"),
        cond=", ".join(cm.get("conditions",[]))[:90],
        interv=", ".join(i.get("name","") for i in (p.get("armsInterventionsModule") or {}).get("interventions",[]))[:110],
        sponsor=((p.get("sponsorCollaboratorsModule") or {}).get("leadSponsor") or {}).get("name","")[:50],
        growth_outcomes=hits[:6], n_growth=len(hits)))
print(f"{len(keep)} of {len(rows)} trials carry a real stature/length endpoint")

# which have results POSTED?  ask in batches
API="https://clinicaltrials.gov/api/v2/studies"
def has_results(ncts):
    out={}
    for i in range(0,len(ncts),100):
        ch=ncts[i:i+100]
        u=API+"?"+urllib.parse.urlencode({"filter.ids":",".join(ch),"pageSize":100,
                                          "fields":"NCTId|HasResults"})
        for a in range(4):
            try:
                with urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"gpa/1.0"}),timeout=90) as r:
                    d=json.loads(r.read()); break
            except Exception:
                if a==3: raise
                time.sleep(2**a)
        for s in d.get("studies",[]):
            out[s.get("protocolSection",{}).get("identificationModule",{}).get("nctId")]=s.get("hasResults")
        time.sleep(0.25)
    return out
hr = has_results([k["nct"] for k in keep])
for k in keep: k["has_results"] = hr.get(k["nct"])
withres = [k for k in keep if k["has_results"]]
print(f"{len(withres)} of those have RESULTS POSTED")
json.dump(keep, open("ctg_growth_trials.json","w"), indent=1)
