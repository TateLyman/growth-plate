"""Download the OPEN ACCESS full text XML for every OA record in the sweep.
Lawful route only: Europe PMC's fullTextXML endpoint, which serves only what the
publisher has licensed for open access.  Non-OA records are recorded, not fetched."""
import json, os, time, urllib.request, sys
d = json.load(open("epmc_sweep.raw.json"))
recs = d["records"]
oa = [r for r in recs.values() if r.get("isOpenAccess") == "Y" and r.get("pmcid")]
os.makedirs("fulltext", exist_ok=True)
FT = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
ok = fail = skip = 0
for i, r in enumerate(oa):
    p = f"fulltext/{r['pmcid']}.xml"
    if os.path.exists(p) and os.path.getsize(p) > 2000: skip += 1; continue
    try:
        req = urllib.request.Request(FT.format(pmcid=r["pmcid"]),
                                     headers={"User-Agent": "growth-plate-atlas/1.0 (mailto:hello@tateprograms.com)"})
        with urllib.request.urlopen(req, timeout=60) as h:
            b = h.read()
        if len(b) > 2000: open(p, "wb").write(b); ok += 1
        else: fail += 1
    except Exception:
        fail += 1
    time.sleep(0.12)
    if (i+1) % 200 == 0: print(f"  {i+1}/{len(oa)}  ok={ok} fail={fail} skip={skip}", flush=True)
print(f"full text: {ok} downloaded, {skip} already held, {fail} unavailable, of {len(oa)} OA records")
