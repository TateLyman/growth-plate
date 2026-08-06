"""Triage the GEO sweep.  The atlas holds ONE human age (early pubertal, 4 donors).
Rank by: is it human? is it growth plate / physis / epiphysis? does the title or
summary name an AGE we do not hold?  Print, do not filter silently."""
import json, re
d = json.load(open("geo_sweep.raw.json"))
S = d["summaries"]

GP   = re.compile(r"growth plate|physe?al|physis|epiphys|chondrocyte|cartilage|chondrogen", re.I)
AGE  = re.compile(r"\bfetal|foetal|embryo|neonat|infant|newborn|juvenile|prepubert|pubert|"
                  r"adolescen|child|paediatric|pediatric|postnatal|week[s]? (post|of) |"
                  r"\bP\d{1,3}\b|age[ds]? \d|year[- ]old|gestation", re.I)
CLOSE= re.compile(r"fusion|closure|senescen|exhaust|clonal|lineage|stem cell|resting zone|quiescen", re.I)

rows = []
for uid, r in S.items():
    if not isinstance(r, dict): continue
    acc = r.get("accession", "")
    tax = r.get("taxon", "") or ""
    title = r.get("title", "") or ""
    summ  = r.get("summary", "") or ""
    txt = title + " || " + summ
    if not GP.search(txt): continue
    human = "Homo sapiens" in tax
    ages  = sorted(set(m.group(0).lower() for m in AGE.finditer(txt)))
    close = sorted(set(m.group(0).lower() for m in CLOSE.finditer(txt)))
    tight = bool(re.search(r"growth plate|physe?al|physis|epiphys", txt, re.I))
    score = (4 if human and tight else 0) + (2 if tight else 0) + (1 if human else 0) \
            + min(len(ages), 3) + min(len(close), 3)
    rows.append(dict(acc=acc, uid=uid, human=human, tight=tight, taxon=tax[:40],
                     n=r.get("n_samples", 0), gdstype=r.get("gdstype", ""),
                     pdat=r.get("pdat", ""), title=title[:170],
                     ages=ages[:6], close=close[:5], score=score))
rows.sort(key=lambda x: (-x["score"], x["acc"]))
json.dump(rows, open("geo_triage.json", "w"), indent=1)
print(f"{len(rows)} growth-plate-relevant series of {len(S)} swept\n")
hum = [r for r in rows if r["human"] and r["tight"]]
print(f"=== HUMAN + growth plate/physis/epiphysis: {len(hum)} ===")
for r in hum:
    print(f"{r['acc']:<12} n={r['n']:<4} {r['pdat']}  {r['title']}")
    if r["ages"]:  print(f"             AGE: {', '.join(r['ages'])}")
