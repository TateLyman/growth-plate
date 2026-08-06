"""Sweep NCBI GEO for every dataset that could carry a HUMAN growth plate at an age
this atlas does not hold.  Records what exists; downloads nothing yet."""
import json, time, urllib.parse, urllib.request, sys, os

E = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
KEY = os.environ.get("NCBI_API_KEY", "")

def get(url):
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            if attempt == 3: raise
            time.sleep(2 ** attempt)

def esearch(db, term, retmax=200):
    u = f"{E}/esearch.fcgi?db={db}&term={urllib.parse.quote(term)}&retmax={retmax}&retmode=json"
    if KEY: u += f"&api_key={KEY}"
    return json.loads(get(u))["esearchresult"].get("idlist", [])

def esummary(db, ids):
    out = {}
    for i in range(0, len(ids), 100):
        chunk = ids[i:i+100]
        u = f"{E}/esummary.fcgi?db={db}&id={','.join(chunk)}&retmode=json"
        if KEY: u += f"&api_key={KEY}"
        d = json.loads(get(u)).get("result", {})
        for k, v in d.items():
            if k != "uids": out[k] = v
        time.sleep(0.4)
    return out

QUERIES = {
 "gp_human":        '("growth plate"[All Fields] OR epiphys*[All Fields]) AND "Homo sapiens"[Organism]',
 "gp_any":          '"growth plate"[All Fields] AND gse[Entry Type]',
 "chondro_human":   'chondrocyte*[All Fields] AND "Homo sapiens"[Organism] AND gse[Entry Type]',
 "cartilage_dev":   '(cartilage[All Fields] AND (fetal[All Fields] OR development*[All Fields] OR juvenile[All Fields])) AND "Homo sapiens"[Organism] AND gse[Entry Type]',
 "physis":          'physis[All Fields] OR physeal[All Fields]',
 "limb_skeleton":   '("limb"[All Fields] AND skelet*[All Fields]) AND "Homo sapiens"[Organism] AND gse[Entry Type]',
 "gp_rat":          '"growth plate"[All Fields] AND ("Rattus norvegicus"[Organism] OR "Oryctolagus cuniculus"[Organism] OR "Ovis aries"[Organism] OR "Sus scrofa"[Organism])',
 "senescence_gp":   '"growth plate"[All Fields] AND (senescence[All Fields] OR ageing[All Fields] OR aging[All Fields] OR fusion[All Fields])',
 "gh_treated":      '(somatropin[All Fields] OR "growth hormone"[All Fields]) AND cartilage[All Fields]',
}

res = {}
for name, q in QUERIES.items():
    try:
        ids = esearch("gds", q, retmax=400)
    except Exception as e:
        print(f"  {name}: FAILED {e}", file=sys.stderr); continue
    res[name] = ids
    print(f"{name}: {len(ids)} hits")
    time.sleep(0.4)

allids = sorted({i for v in res.values() for i in v})
print(f"union: {len(allids)} unique GDS/GSE records; fetching summaries...")
summ = esummary("gds", allids)
json.dump({"queries": QUERIES, "hits": res, "summaries": summ},
          open("geo_sweep.raw.json", "w"), indent=1)
print("wrote geo_sweep.raw.json", len(summ), "summaries")
