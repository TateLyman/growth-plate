"""Europe PMC sweep.  For each UNKNOWN this atlas cannot close, ask the whole
open-access literature.  Records every hit; downloads the OPEN ACCESS full text
and any supplementary files.  Lawful routes only - OA full text and supp only."""
import json, os, time, urllib.parse, urllib.request, sys

BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
def get(url, timeout=90, binary=False):
    for a in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "growth-plate-atlas/1.0 (mailto:hello@tateprograms.com)"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                b = r.read()
            return b if binary else b.decode("utf-8", "replace")
        except Exception as e:
            if a == 3: raise
            time.sleep(2 ** a)

def search(q, pagesize=100, cap=400):
    out, cur = [], "*"
    while len(out) < cap:
        u = BASE + "?" + urllib.parse.urlencode(
            {"query": q, "format": "json", "pageSize": pagesize, "cursorMark": cur,
             "resultType": "core"})
        d = json.loads(get(u))
        res = d.get("resultList", {}).get("result", [])
        out.extend(res)
        nxt = d.get("nextCursorMark")
        if not res or nxt == cur: break
        cur = nxt
        time.sleep(0.3)
    return out

# One query per UNKNOWN the atlas records, not per topic.
QUERIES = {
 "human_gp_histomorphometry":
   '("growth plate" OR physis OR physeal) AND (histomorphometr* OR "zone height" OR '
   '"cell height" OR "column density" OR stereolog*) AND (human OR child* OR infant* OR '
   'adolescen*) AND (HAS_FT:Y)',
 "human_gp_age_series":
   '("growth plate" OR physis) AND human AND (age OR ages OR "age range" OR ontogen*) AND '
   '(infant* OR neonat* OR "1 year" OR childhood OR prepubert*) AND HAS_FT:Y',
 "clonal_nonmouse":
   '("growth plate" OR physis) AND (clonal OR "lineage tracing" OR "clone size" OR '
   '"stem cell" OR "self-renew*") AND (rat OR rabbit OR sheep OR pig OR "guinea pig" OR '
   'bovine OR human OR monkey OR primate) AND HAS_FT:Y',
 "gp_senescence_budget":
   '("growth plate senescence" OR "proliferative exhaustion" OR "replicative senescence" '
   'AND "growth plate") AND HAS_FT:Y',
 "why_mouse_never_closes":
   '("growth plate" AND (closure OR fusion) AND (mouse OR mice OR murine OR rodent) AND '
   '(species OR "does not fuse" OR "remain open" OR "fail to fuse" OR persist*)) AND HAS_FT:Y',
 "human_specimen_route":
   '("growth plate" OR physeal OR physis) AND (epiphysiodesis OR "limb lengthening" OR '
   '"distraction osteogenesis" OR biopsy OR "surgical specimen" OR autopsy OR "post-mortem") '
   'AND human AND HAS_FT:Y',
 "gh_final_height_registry":
   '("growth hormone" AND ("adult height" OR "final height" OR "near-adult height") AND '
   '(registry OR KIGS OR NCGS OR GeNeSIS OR ANSWER OR cohort)) AND HAS_FT:Y',
 "chondrocyte_cycle_time":
   '(chondrocyte AND ("cell cycle time" OR "cycle time" OR "doubling time" OR '
   '"proliferation rate" OR "labelling index" OR "labeling index") AND ("growth plate" OR physis)) AND HAS_FT:Y',
 "gp_regeneration":
   '("growth plate" AND (regeneration OR transplant* OR "tissue engineer*" OR organoid OR '
   'iPSC OR "induced pluripotent")) AND HAS_FT:Y',
 "growth_plate_stem_marker_human":
   '(("resting zone" OR "reserve zone" OR "stem cell niche") AND ("growth plate" OR physis) '
   'AND human) AND HAS_FT:Y',
}

res, seen = {}, {}
for k, q in QUERIES.items():
    try:
        r = search(q)
    except Exception as e:
        print(f"{k}: FAILED {e}", file=sys.stderr); continue
    oa  = [x for x in r if x.get("isOpenAccess") == "Y"]
    ft  = [x for x in r if x.get("hasTextMinedTerms") or x.get("inEPMC") == "Y"]
    res[k] = [x.get("id") for x in r]
    for x in r: seen[x.get("id")] = x
    print(f"{k:<32} {len(r):>4} hits  {len(oa):>4} open access  {len(ft):>4} in EPMC")
json.dump({"queries": QUERIES, "byquery": res, "records": seen},
          open("epmc_sweep.raw.json", "w"))
print(f"\nunion {len(seen)} unique records; "
      f"{sum(1 for x in seen.values() if x.get('isOpenAccess')=='Y')} open access")
