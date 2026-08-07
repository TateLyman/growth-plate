import json, os, re, html, collections
SP = "/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad"
refs = json.load(open(SP + "/refs.json"))
meta = json.load(open(SP + "/epmc_meta.json"))
TAG = re.compile(r"<[^>]+>")


def strip(x):
    x = re.sub(r"<(ref-list|back)[ >].*?</\1>", " ", x, flags=re.S)
    return html.unescape(re.sub(r"\s+", " ", TAG.sub(" ", x)))


def fulltext(pmcid):
    for d in ("ftcache", "ft"):
        f = os.path.join(SP, d, pmcid + ".xml")
        if os.path.exists(f) and os.path.getsize(f) > 1000:
            return strip(open(f, encoding="utf8", errors="replace").read())
    return None


SUBJ = (r"(?:C57[A-Za-z0-9/]*|BALB[^ ]*|129[A-Za-z0-9/]*|CD-?1|ICR|FVB|Sprague[- ]?Dawley|"
        r"Wistar|New Zealand[- ]White|mice|mouse|rats?|rabbits?|animals|pups|littermates|"
        r"patients|subjects|participants|children|adolescents|volunteers|donors|"
        r"boys|girls|infants|neonates|chicks?|piglets?|lambs?|calves|sheep|siblings|"
        r"individuals|probands?|cases|controls|twins|cohort|mutants?|wild-?type)")
PRE = r"(?:adult\s+|young\s+|juvenile\s+|immature\s+|growing\s+|wild-?type\s+|transgenic\s+|mutant\s+|\d+\s+|weanling\s+)*"
PRE_L = r"(?:[A-Za-z0-9/+\-.()]{1,18}\s+){0,3}"
P_BOTHATT = re.compile(r"\b(?:male and female|female and male|males and females|females and males|"
                       r"both male and female|male/female|male and female)\s+" + PRE_L + SUBJ, re.I)
P_BOTHATT2 = re.compile(r"\b" + SUBJ + r"\s+of\s+(?:both sexes|either sex)\b", re.I)
P_BOTHATT3 = re.compile(r"\b(?:both sexes|either sex)\b[^.]{0,40}\b" + SUBJ, re.I)
P_MALE = re.compile(r"\bmales?\s+" + PRE + SUBJ, re.I)
P_FEM = re.compile(r"\bfemales?\s+" + PRE + SUBJ, re.I)
P_MALE2 = re.compile(r"\b" + SUBJ + r"\s+(?:were|are|was|is)\s+(?:all\s+)?males?\b", re.I)
P_FEM2 = re.compile(r"\b" + SUBJ + r"\s+(?:were|are|was|is)\s+(?:all\s+)?females?\b", re.I)
P_OVX = re.compile(r"\b(ovariectom\w+|ovx|female rabbits|female rats|female mice)\b", re.I)
P_ORX = re.compile(r"\b(orchidectom\w+|orchiectom\w+|castrated males?)\b", re.I)
P_NM = re.compile(r"\b(\d+)\s*(?:\(\d+(?:\.\d+)?%\)\s*)?(?:males?|boys?|men)\b", re.I)
P_NF = re.compile(r"\b(\d+)\s*(?:\(\d+(?:\.\d+)?%\)\s*)?(?:females?|girls?|women)\b", re.I)
P_GENERIC_BOTH = re.compile(r"\b(both sexes|either sex|sex-independent|men and women|women and men|boys and girls)\b", re.I)

AGE_E = re.compile(r"\bE(\d{1,2}(?:\.5)?)\b")  # filtered downstream
AGE_P = re.compile(r"\b(?:postnatal day\s*|P)(\d{1,2})\b")
AGE_NUM = re.compile(r"\b(\d+(?:\.\d+)?)\s*(?:(?:-|–|to)\s*(\d+(?:\.\d+)?)\s*)?[- ]?(day|week|month|year)s?[- ]old\b", re.I)
AGE_MEAN = re.compile(r"\b(?:mean|median|average)\s+age\D{0,30}?(\d+(?:\.\d+)?)\s*(year|month|week|day)", re.I)
AGE_WORD = {
    "fetal": re.compile(r"\b(fetal|foetal|embryonic day|prenatal|in utero|embryos?)\b", re.I),
    "neonatal": re.compile(r"\b(neonat\w+|newborn|at birth|perinatal)\b", re.I),
    "child": re.compile(r"\b(prepubert\w+|pre-pubert\w+|juvenile|childhood|children|weanling|immature)\b", re.I),
    "pubertal": re.compile(r"\b(pubert\w+|adolescen\w+|Tanner stage|peripubert\w+)\b", re.I),
    "adult": re.compile(r"\b(adults?|skeletally mature|post-?menopausal|mature mice|mature rats)\b", re.I),
}
ZONE = {
    "resting": re.compile(r"\b(resting zone|reserve zone|resting[- ]zone|resting chondrocyte|reserve chondrocyte)\w*", re.I),
    "proliferative": re.compile(r"\b(proliferat\w+ zone|proliferating chondrocyte|proliferative chondrocyte|columnar zone|columnar chondrocyte)\w*", re.I),
    "prehypertrophic": re.compile(r"\bpre-?hypertrophic\b", re.I),
    "hypertrophic": re.compile(r"\b(hypertrophic zone|hypertrophic chondrocyte|chondrocyte hypertrophy|terminal hypertrophic)\w*", re.I),
    "perichondrium": re.compile(r"\b(perichondri\w+|groove of Ranvier|ring of LaCroix)\b", re.I),
}
SPEC = {
    "human": re.compile(r"\b(human|patients?|children|women|men|participants|subjects|donors|probands?)\b", re.I),
    "mouse": re.compile(r"\b(mice|mouse|murine|C57BL|BALB|FVB)\b", re.I),
    "rat": re.compile(r"\b(rats?|Sprague|Wistar)\b", re.I),
    "rabbit": re.compile(r"\b(rabbits?|New Zealand White)\b", re.I),
    "chick": re.compile(r"\b(chicks?|chicken|avian)\b", re.I),
    "bovine": re.compile(r"\b(bovine|calf|calves|cattle)\b", re.I),
    "pig": re.compile(r"\b(pigs?|porcine|piglets?)\b", re.I),
    "sheep": re.compile(r"\b(sheep|ovine|lambs?)\b", re.I),
    "zebrafish": re.compile(r"\b(zebrafish|danio)\b", re.I),
}

out = {}
for rid, r in refs.items():
    pmid = str(r.get("pmid") or "")
    md = meta.get(pmid, {})
    ab = md.get("abstract") or ""
    ft = fulltext(md["pmcid"]) if md.get("pmcid") else None
    src = "fulltext" if ft else ("abstract" if len(ab) > 100 else "none")
    ti = (md.get("title") or r.get("title") or "")
    text = ti + ". " + (ft or ab)
    # Drop breeding/husbandry sentences: "pregnant female mice", "mated with males",
    # "timed-pregnant dams" describe the parents, not the experimental subjects.
    BREED = re.compile(r"pregnant|timed[- ]?preg|\bdams?\b|\bmated\b|mating|zygote|vaginal plug|"
                       r"\bplugs?\b|crossed with|\bsires?\b|breeding|bred with|harem|estrous|"
                       r"\bmatings\b|superovulat", re.I)
    sents = re.split(r"(?<=[.;])\s+", text)
    text_sub = " ".join(s for s in sents if not BREED.search(s))
    text = text_sub if len(text_sub) > 0.3 * len(text) else text
    ba = len(P_BOTHATT.findall(text)) + len(P_BOTHATT2.findall(text)) + len(P_BOTHATT3.findall(text))
    ma = len(P_MALE.findall(text)) + len(P_MALE2.findall(text))
    fa = len(P_FEM.findall(text)) + len(P_FEM2.findall(text))
    cm, cf = len(P_NM.findall(text)), len(P_NF.findall(text))
    gb = len(P_GENERIC_BOTH.findall(text))
    ovx, orx = len(P_OVX.findall(text)), len(P_ORX.findall(text))
    # title-level sex attachment wins (papers usually name the sex studied in the title)
    tm = len(re.findall(r"\bmales?\b|\bboys?\b|\bmen\b", ti, re.I))
    tf = len(re.findall(r"\bfemales?\b|\bgirls?\b|\bwomen\b", ti, re.I))
    tb = len(P_GENERIC_BOTH.findall(ti))
    if tb or (tm and tf):
        sx, basis = "both", "title-both"
    elif tm:
        sx, basis = "male", "title-male"
    elif tf:
        sx, basis = "female", "title-female"
    elif ba:
        sx, basis = "both", "attached-both"
    elif cm and cf:
        sx, basis = "both", "cohort-counts"
    elif ma and fa:
        if ma >= 3 * fa:
            sx, basis = "male", "attached-male-dominant"
        elif fa >= 3 * ma:
            sx, basis = "female", "attached-female-dominant"
        else:
            sx, basis = "both", "attached-male+female"
    elif ma:
        sx, basis = "male", "attached-male"
    elif fa:
        sx, basis = "female", "attached-female"
    elif cm and cf:
        sx, basis = "both", "cohort-counts"
    elif ovx and not orx:
        sx, basis = "female", "ovx"
    elif orx and not ovx:
        sx, basis = "male", "orx"
    else:
        sx, basis = None, ("generic-both-only" if gb else "none")
    d = {"ref": rid, "src": src, "year": r.get("year"), "type": r.get("type"),
         "title": ti[:160], "one_line": (r.get("one_line_finding") or "")[:170],
         "sex": sx, "sex_basis": basis, "sex_counts": [ba, ma, fa, cm, cf, gb, ovx, orx]}
    d["sex_snips"] = [s.strip()[:110] for s in re.findall(
        r"[^.;]{0,60}\b(?:males?|females?|both sexes|either sex|boys|girls|ovariectom\w+)\b[^.;]{0,50}",
        text[:120000], re.I)[:3]]
    # E-days only count if the paper actually talks about embryos, and only in a
    # biologically possible window; otherwise "E2" is just part of "PDE2".
    embryo_ctx = re.search(r"\b(embryo\w*|embryonic day|fetal|foetal|gestation\w*|E\d{1,2}\.5)\b", text, re.I)
    Es = sorted({float(x) for x in AGE_E.findall(text)}) if embryo_ctx else []
    Es = [x for x in Es if 8 <= x <= 21]
    # P-days only count with an explicit postnatal-day context; case-sensitive so that
    # p16/p21/p53 (protein names) are not read as ages.
    postnatal_ctx = re.search(r"postnatal day|\bpostnatal\b|\bpups?\b", text, re.I)
    Ps = sorted({int(x) for x in AGE_P.findall(text)}) if postnatal_ctx else []
    Ps = [x for x in Ps if x <= 90]
    nums = []
    for m in AGE_NUM.finditer(text):
        a = float(m.group(1)); b = float(m.group(2)) if m.group(2) else None
        nums.append((a, b, m.group(3).lower(), m.group(0)))
    d["E"] = Es[:10]; d["P"] = Ps[:14]
    d["nums"] = [[n[0], n[1], n[2]] for n in nums[:14]]
    d["num_raw"] = sorted({n[3] for n in nums})[:8]
    d["age_mean"] = [[float(a), b.lower()] for a, b in AGE_MEAN.findall(text)][:4]
    d["age_words"] = {k: len(p.findall(text)) for k, p in AGE_WORD.items() if p.findall(text)}
    d["zone"] = {k: len(p.findall(text)) for k, p in ZONE.items() if p.findall(text)}
    sp = {k: len(p.findall(text)) for k, p in SPEC.items()}
    d["species"] = {k: v for k, v in sp.items() if v >= 2}
    out[rid] = d
json.dump(out, open(SP + "/dossier3.json", "w"))
print("refs", len(out), collections.Counter(v["src"] for v in out.values()))
print("sex", collections.Counter(v["sex"] for v in out.values()))
print("basis", collections.Counter(v["sex_basis"] for v in out.values()))
print("zone>=1", sum(1 for v in out.values() if v["zone"]))
