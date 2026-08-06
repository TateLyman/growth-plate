"""ClinicalTrials.gov v2 sweep.  The losartan result came from a trial that PRESPECIFIED
height as a secondary outcome and POSTED the results, which nobody had read.  Ask the
whole registry the same question: which trials measure a GROWTH endpoint, and of those,
which have RESULTS POSTED?  Downloads the full record for every hit with results."""
import json, time, urllib.parse, urllib.request, os, re

API = "https://clinicaltrials.gov/api/v2/studies"
def q(params):
    for a in range(4):
        try:
            u = API + "?" + urllib.parse.urlencode(params)
            req = urllib.request.Request(u, headers={"User-Agent":"growth-plate-atlas/1.0"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read())
        except Exception as e:
            if a == 3: raise
            time.sleep(2**a)

# outcome-measure text that means a LENGTH endpoint, not a weight/BMI/growth-factor one
GROWTH = re.compile(r"\b(height|stature|body length|growth velocity|height velocity|"
                    r"adult height|final height|near[- ]adult height|standing height|"
                    r"length velocity|bone age|height sds|height z|height-for-age|"
                    r"segment ratio|arm span|sitting height|limb length|leg length|"
                    r"femur length|tibia length|growth rate)\b", re.I)
NOISE  = re.compile(r"growth factor|tumou?r growth|hair growth|bacterial growth|"
                    r"growth hormone level|weight-for-height|height of the|"
                    r"growth of the tumor", re.I)

FIELDS = ("NCTId|BriefTitle|OverallStatus|HasResults|Phase|Condition|InterventionName|"
          "PrimaryOutcomeMeasure|SecondaryOutcomeMeasure|EnrollmentCount|StartDate|"
          "CompletionDate|MinimumAge|MaximumAge|LeadSponsorName")

def sweep(expr, label, page_size=1000, cap=20000):
    out, tok, n = [], None, 0
    while True:
        p = {"query.term": expr, "pageSize": page_size, "fields": FIELDS,
             "countTotal": "true"}
        if tok: p["pageToken"] = tok
        d = q(p)
        studies = d.get("studies", [])
        out.extend(studies); n += len(studies)
        tok = d.get("nextPageToken")
        if not tok or n >= cap: break
        time.sleep(0.3)
    print(f"{label}: {n} studies")
    return out

# Cast wide: any study whose text mentions a stature endpoint OR a growth condition.
EXPRS = {
 "height_outcome": 'AREA[OutcomeMeasureTitle](height OR stature OR "growth velocity" OR "bone age" OR "arm span")',
 "short_stature":  '"short stature" OR "idiopathic short stature" OR achondroplasia OR hypochondroplasia OR "Turner syndrome" OR "SHOX deficiency"',
 "tall_stature":   '"tall stature" OR "constitutional tall" OR "excessive height" OR epiphysiodesis',
 "gp_drugs":       'vosoritide OR "CNP analog" OR infigratinib OR "aromatase inhibitor" AND height',
 "sacubitril_ped": 'sacubitril AND (children OR pediatric OR paediatric OR adolescent)',
}
raw = {}
for k, e in EXPRS.items():
    try: raw[k] = sweep(e, k)
    except Exception as ex: print(f"{k}: FAILED {ex}"); raw[k] = []

seen, rows = set(), []
for k, studies in raw.items():
    for s in studies:
        p = s.get("protocolSection", s)
        nct = (p.get("identificationModule") or {}).get("nctId") or s.get("NCTId")
        if isinstance(nct, list): nct = nct[0]
        if not nct or nct in seen: continue
        seen.add(nct)
        rows.append({"nct": nct, "found_by": k, "rec": s})
print(f"\nunion: {len(rows)} unique trials")
json.dump(rows, open("ctg_sweep.raw.json","w"))
