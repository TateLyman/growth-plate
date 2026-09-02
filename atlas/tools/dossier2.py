import json, os, re, html, collections
SP = "/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad"
refs = json.load(open(SP + "/refs.json"))
meta = json.load(open(SP + "/epmc_meta.json"))
TAG = re.compile(r"<[^>]+>")


def strip(x):
    x = re.sub(r"<(ref-list|back)[ >].*?</\1>", " ", x, flags=re.S)
    x = TAG.sub(" ", x)
    return html.unescape(re.sub(r"\s+", " ", x))


def fulltext(pmcid):
    for d in ("ftcache", "ft"):
        f = os.path.join(SP, d, pmcid + ".xml")
        if os.path.exists(f) and os.path.getsize(f) > 1000:
            return strip(open(f, encoding="utf8", errors="replace").read())
    return None


SUBJ = (r"(?:C57[A-Za-z0-9/]*|BALB[^ ]*|129[A-Za-z0-9/]*|CD-?1|ICR|FVB|Sprague[- ]Dawley|"
        r"Wistar|New Zealand[- ]White|mice|mouse|rats?|rabbits?|animals|pups|littermates|"
        r"patients|subjects|participants|children|adolescents|volunteers|donors|women|men|"
        r"boys|girls|infants|neonates|chicks?|piglets?|lambs?|calves|sheep|cattle)")
P_BOTH = re.compile(r"\b(both sexes|either sex|male and female|females and males|males and females|"
                    r"female and male|male/female|male or female|men and women|women and men|"
                    r"boys and girls|girls and boys|of both genders|both genders|sex-independent|"
                    r"regardless of sex|in both males and females)\b", re.I)
P_MALE = re.compile(r"\bmale\s+(?:adult\s+|young\s+|juvenile\s+|wild-?type\s+)?" + SUBJ, re.I)
P_FEM = re.compile(r"\bfemale\s+(?:adult\s+|young\s+|juvenile\s+|wild-?type\s+)?" + SUBJ, re.I)
P_MALE2 = re.compile(r"\b" + SUBJ + r"\s+(?:were\s+|are\s+)?male\b", re.I)
P_FEM2 = re.compile(r"\b" + SUBJ + r"\s+(?:were\s+|are\s+)?female\b", re.I)
P_NM = re.compile(r"\b(\d+)\s*(?:\(\d+%\)\s*)?(?:males?|boys?|men)\b", re.I)
P_NF = re.compile(r"\b(\d+)\s*(?:\(\d+%\)\s*)?(?:females?|girls?|women)\b", re.I)

AGE_EXPL = re.compile(r"\b(?:E\d+(?:\.5)?|P\d{1,3})\b")
AGE_NUM = re.compile(r"\b(\d+(?:\.\d+)?)\s*(?:-|–|to)?\s*(?:\d+(?:\.\d+)?)?\s*[- ]?(day|week|month|year)s?[- ]old\b", re.I)
AGE_MEAN = re.compile(r"\b(?:mean|median|average)\s+age[^.]{0,40}?(\d+(?:\.\d+)?)\s*(year|month|week)", re.I)
AGE_WORD = {
    "fetal": re.compile(r"\b(fetal|foetal|embryonic day|prenatal|in utero)\b", re.I),
    "neonatal": re.compile(r"\b(neonat\w+|newborn|at birth)\b", re.I),
    "child": re.compile(r"\b(prepubert\w+|pre-pubert\w+|juvenile|childhood|children|weanling)\b", re.I),
    "pubertal": re.compile(r"\b(pubert\w+|adolescen\w+|Tanner stage)\b", re.I),
    "adult": re.compile(r"\b(adult|skeletally mature|post-?menopausal)\b", re.I),
}
ZONE = {
    "resting": re.compile(r"\b(resting zone|reserve zone|resting chondrocyte|resting-zone)\b", re.I),
    "proliferative": re.compile(r"\b(proliferat\w+ zone|proliferating chondrocyte|proliferative chondrocyte|columnar zone|columnar chondrocyte)\b", re.I),
    "prehypertrophic": re.compile(r"\b(pre-?hypertrophic)\b", re.I),
    "hypertrophic": re.compile(r"\b(hypertrophic zone|hypertrophic chondrocyte|chondrocyte hypertrophy)\b", re.I),
    "perichondrium": re.compile(r"\b(perichondri\w+|groove of Ranvier|ring of LaCroix|periosteum)\b", re.I),
}
SPEC = {
    "human": re.compile(r"\b(human|patients?|children|women|men|participants|subjects|donors)\b", re.I),
    "mouse": re.compile(r"\b(mice|mouse|murine|C57BL|BALB|FVB)\b", re.I),
    "rat": re.compile(r"\b(rats?|Sprague|Wistar)\b", re.I),
    "rabbit": re.compile(r"\b(rabbits?|New Zealand White)\b", re.I),
    "chick": re.compile(r"\b(chicks?|chicken|avian)\b", re.I),
    "bovine": re.compile(r"\b(bovine|calf|calves|cattle)\b", re.I),
    "pig": re.compile(r"\b(pigs?|porcine|piglets?)\b", re.I),
    "zebrafish": re.compile(r"\b(zebrafish|danio)\b", re.I),
    "sheep": re.compile(r"\b(sheep|ovine|lambs?)\b", re.I),
}

out = {}
for rid, r in refs.items():
    pmid = str(r.get("pmid") or "")
    md = meta.get(pmid, {})
    ab = md.get("abstract") or ""
    ft = fulltext(md["pmcid"]) if md.get("pmcid") else None
    src = "fulltext" if ft else ("abstract" if len(ab) > 100 else "none")
    ti = (md.get("title") or r.get("title") or "")
    text = (ti + ". " + (ft or ab))
    d = {"ref": rid, "src": src, "year": r.get("year"), "type": r.get("type"),
         "title": ti[:150], "one_line": (r.get("one_line_finding") or "")[:160]}
    nb, nm, nf = len(P_BOTH.findall(text)), len(P_MALE.findall(text)) + len(P_MALE2.findall(text)), len(P_FEM.findall(text)) + len(P_FEM2.findall(text))
    # numeric cohort counts (human studies)
    cm, cf = len(P_NM.findall(text)), len(P_NF.findall(text))
    d["sex_counts"] = [nb, nm, nf, cm, cf]
    if nb:
        sx = "both"
    elif nm and nf:
        sx = "both"
    elif nm:
        sx = "male"
    elif nf:
        sx = "female"
    elif cm and cf:
        sx = "both"
    else:
        sx = None
    d["sex"] = sx
    d["sex_snips"] = [s.strip() for s in re.findall(r"[^.;]{0,70}\b(?:male|female|both sexes|either sex|boys|girls)\b[^.;]{0,50}", text[:80000], re.I)[:4]]
    d["age_tokens"] = sorted(set(AGE_EXPL.findall(text)))[:12]
    d["age_nums"] = [" ".join(m) if isinstance(m, tuple) else m for m in AGE_NUM.findall(text)][:12]
    d["age_num_raw"] = sorted(set(re.findall(r"\b\d+(?:\.\d+)?\s*(?:-|–|to)?\s*(?:\d+(?:\.\d+)?)?\s*[- ]?(?:day|week|month|year)s?[- ]old\b", text, re.I)))[:10]
    d["age_mean"] = AGE_MEAN.findall(text)[:4]
    d["age_words"] = {k: len(p.findall(text)) for k, p in AGE_WORD.items() if p.findall(text)}
    d["zone"] = {k: len(p.findall(text)) for k, p in ZONE.items() if p.findall(text)}
    d["species"] = {k: len(p.findall(text)) for k, p in SPEC.items() if len(p.findall(text)) >= 2}
    out[rid] = d
json.dump(out, open(SP + "/dossier2.json", "w"), indent=0)
print("refs", len(out), collections.Counter(v["src"] for v in out.values()))
print("sex determined", sum(1 for v in out.values() if v["sex"]), collections.Counter(v["sex"] for v in out.values()))
print("zone any", sum(1 for v in out.values() if v["zone"]))
print("age any", sum(1 for v in out.values() if v["age_tokens"] or v["age_num_raw"] or v["age_words"] or v["age_mean"]))
