"""Extract the NUMBERS from the posted results of every trial that reported a stature
outcome in growing children.

POSITIVE CONTROL, checked before anything is written: NCT00429364 (Pediatric Heart
Network Marfan trial) must come back with an 'Annual Rate of Change in Height' measure
carrying group values 0.822 and 0.935 cm/yr - the values this atlas already read by
hand.  If the extractor cannot reproduce a number it has already verified, it is not
trusted with 505 it has not.
"""
import json, glob, re, csv, sys

GROWTH = re.compile(r"\b(height|stature|body length|growth velocity|height velocity|adult height|"
  r"final height|near[- ]adult height|standing height|bone age|height sds|height z|"
  r"height-for-age|segment ratio|arm span|sitting height|limb length|leg length|"
  r"femur length|tibia length|growth rate|length velocity)\b", re.I)
NOISE = re.compile(r"growth factor|tumou?r growth|hair growth|weight[- ]for[- ]height", re.I)

def measures(path):
    d = json.load(open(path))
    ps = d.get("protocolSection", {}) or {}
    rs = d.get("resultsSection", {}) or {}
    nct = ps.get("identificationModule", {}).get("nctId")
    out = []
    for om in ((rs.get("outcomeMeasuresModule") or {}).get("outcomeMeasures") or []):
        title = om.get("title", "") or ""
        if not GROWTH.search(title) or NOISE.search(title): continue
        groups = {g.get("id"): g.get("title", "") for g in (om.get("groups") or [])}
        rec = dict(nct=nct, title=title.strip(), unit=(om.get("unitOfMeasure") or "").strip(),
                   ptype=om.get("type",""), param=om.get("paramType",""),
                   disp=om.get("dispersionType",""), groups=[], stats=[])
        for cls in (om.get("classes") or []):
            cl = (cls.get("title") or "").strip()
            for cat in (cls.get("categories") or []):
                ct = (cat.get("title") or "").strip()
                for m in (cat.get("measurements") or []):
                    rec["groups"].append(dict(
                        group=groups.get(m.get("groupId"), m.get("groupId")),
                        cls=cl, cat=ct, value=m.get("value"),
                        spread=m.get("spread"), lo=m.get("lowerLimit"), hi=m.get("upperLimit")))
        for an in (om.get("analyses") or []):
            rec["stats"].append(dict(pvalue=an.get("pValue"), method=an.get("statisticalMethod"),
                param=an.get("paramType"), est=an.get("paramValue"),
                ci_lo=an.get("ciLowerLimit"), ci_hi=an.get("ciUpperLimit"),
                groups=[groups.get(g, g) for g in (an.get("groupIds") or [])]))
        out.append(rec)
    return out

# ---------------- positive control -------------------------------------------------
ctrl = [m for m in measures("ctg/NCT00429364.json")
        if "annual rate of change in height" in m["title"].lower()]
vals = {str(g["value"]) for m in ctrl for g in m["groups"]}
if not ({"0.822", "0.935"} <= vals):
    print("POSITIVE CONTROL FAILED for NCT00429364.")
    print("  measures found:", [m['title'] for m in ctrl][:5])
    print("  values found:", sorted(vals)[:20])
    print("REFUSING TO EXTRACT THE OTHER 505."); sys.exit(1)
print("positive control PASS: NCT00429364 reproduces 0.822 / 0.935 cm/yr\n")

# ---------------- extract everything ----------------------------------------------
allm, files = [], sorted(glob.glob("ctg/*.json"))
for p in files:
    try: allm.extend(measures(p))
    except Exception as e: print("  skip", p, e)
print(f"{len(allm)} stature outcome measures extracted from {len(files)} trials")
json.dump(allm, open("ctg_measures.json", "w"), indent=1)

with open("ctg_measures.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["nct","outcome_title","unit","param_type","dispersion","arm","class","category",
                "value","spread","ci_lo","ci_hi"])
    for m in allm:
        for g in m["groups"]:
            w.writerow([m["nct"], m["title"], m["unit"], m["param"], m["disp"],
                        g["group"], g["cls"], g["cat"], g["value"], g["spread"], g["lo"], g["hi"]])
n_rows = sum(len(m["groups"]) for m in allm)
n_stat = sum(len(m["stats"]) for m in allm)
print(f"{n_rows} arm-level numbers, {n_stat} prespecified statistical comparisons with p-values")
with_p = [s for m in allm for s in m["stats"] if s.get("pvalue")]
print(f"{len(with_p)} of those carry a posted p-value")
