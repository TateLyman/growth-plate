import json, os, re, glob, html
SP = "/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad"
refs = json.load(open(SP + "/refs.json"))
meta = json.load(open(SP + "/epmc_meta.json"))

TAG = re.compile(r"<[^>]+>")


def strip(x):
    x = re.sub(r"<(ref-list|back|table-wrap)[ >].*?</\1>", " ", x, flags=re.S)
    x = TAG.sub(" ", x)
    return html.unescape(re.sub(r"\s+", " ", x))


def fulltext(pmcid):
    for d in ("ftcache", "ft"):
        f = os.path.join(SP, d, pmcid + ".xml")
        if os.path.exists(f) and os.path.getsize(f) > 1000:
            return strip(open(f, encoding="utf8", errors="replace").read())
    return None


SEX = {
    "male_only": r"\bmale\b(?!\s*(and|or|/|,)\s*female)",
    "female_only": r"\bfemale\b(?!\s*(and|or|/|,)\s*male)",
    "both": r"(both sexes|male and female|female and male|males and females|either sex|male/female|both male|of both genders|men and women|boys and girls)",
}
ZONE = {
    "resting": r"\b(resting zone|reserve zone|resting chondrocyte|RZ)\b",
    "proliferative": r"\b(proliferative zone|proliferating chondrocyte|proliferative chondrocyte|columnar zone|PZ)\b",
    "prehypertrophic": r"\b(prehypertrophic|pre-hypertrophic)\b",
    "hypertrophic": r"\b(hypertrophic zone|hypertrophic chondrocyte|hypertrophy)\b",
    "perichondrium": r"\b(perichondri\w+|groove of Ranvier|ring of LaCroix)\b",
}
SPEC = {
    "human": r"\bhuman|patients?\b|\bchildren\b|\bwomen\b|\bmen\b",
    "mouse": r"\b(mice|mouse|murine|C57BL|129S)\b",
    "rat": r"\brats?\b|Sprague|Wistar",
    "rabbit": r"\brabbits?\b|New Zealand White",
    "chick": r"\b(chick|chicken|embryonic day .*chick)\b",
    "bovine": r"\b(bovine|calf|cattle)\b",
    "zebrafish": r"\b(zebrafish|danio)\b",
}
AGEPAT = [
    (r"\bE\d+(\.\d+)?\b", "E"),
    (r"\bP\d+\b", "P"),
    (r"\b(\d+(?:\.\d+)?)[- ](?:to[- ]\d+[- ])?(day|week|month|year)s?[- ]old\b", "ago"),
    (r"\b(fetal|foetal|embryonic|prenatal)\b", "fetal"),
    (r"\b(neonatal|newborn|postnatal day)\b", "neonatal"),
    (r"\b(prepubertal|pre-pubertal|juvenile|childhood|children)\b", "child"),
    (r"\b(pubertal|puberty|adolescen\w+)\b", "pubertal"),
    (r"\b(adult|skeletally mature|mature mice|mature rats)\b", "adult"),
]

out = {}
for rid, r in refs.items():
    pmid = str(r.get("pmid") or "")
    md = meta.get(pmid, {})
    ab = md.get("abstract") or ""
    ft = fulltext(md["pmcid"]) if md.get("pmcid") else None
    src = "fulltext" if ft else ("abstract" if len(ab) > 100 else "none")
    text = ft or ab
    ti = (md.get("title") or r.get("title") or "")
    blob = ti + " " + text
    # methods window: prefer the region around animal/subject descriptions
    d = {"ref": rid, "src": src, "year": r.get("year"), "type": r.get("type"),
         "title": ti, "len": len(text)}
    low = blob
    d["sex"] = {k: len(re.findall(p, low, re.I)) for k, p in SEX.items()}
    d["zone"] = {k: len(re.findall(p, low, re.I)) for k, p in ZONE.items()}
    d["species"] = {k: len(re.findall(p, low, re.I)) for k, p in SPEC.items()}
    ages = {}
    for p, lab in AGEPAT:
        f = re.findall(p, low, re.I)
        if f:
            ages[lab] = len(f)
    d["age"] = ages
    # capture literal age snippets
    snips = re.findall(r"[^.]{0,60}\b(?:\d+(?:\.\d+)?[- ](?:day|week|month|year)s?[- ]old|E\d+\.?\d?|P\d+)\b[^.]{0,40}", low[:60000], re.I)
    d["age_snips"] = snips[:6]
    sexsnips = re.findall(r"[^.]{0,80}\b(?:male|female|both sexes|either sex)\b[^.]{0,60}", low[:60000], re.I)
    d["sex_snips"] = sexsnips[:6]
    out[rid] = d
json.dump(out, open(SP + "/dossier.json", "w"))
import collections
print("refs", len(out), collections.Counter(v["src"] for v in out.values()))
