#!/usr/bin/env python3
"""
ROUND 279 - a compound-discovery sweep, run against what the atlas already holds.

The operator's standing instruction is to find ACTUAL COMPOUNDS, including risky
and unproven ones. Previous rounds have mostly CLOSED things. This tool looks for
the opposite: any agent, in any species, reported to INCREASE bone or body length
in a NORMAL (non-deficient, non-rescue) animal - which is the one signature that
has repeatedly predicted a real lever in this file - and then subtracts everything
the atlas already knows about.

Method
  1. Fire a wide set of Europe PMC queries pairing intervention vocabulary with
     LENGTH endpoints and wild-type/normal-animal vocabulary.
  2. Pull titles+abstracts, keep records whose abstract contains a length endpoint
     AND a gain word in the same sentence.
  3. Extract candidate agent names from a curated regex of drug-name morphology
     (-ib, -mab, -stat, -tide, -afil, -parib, etc.) plus explicit compound codes.
  4. Subtract every token that already appears anywhere in atlas/nodes or in the
     bibliography, so what remains is genuinely absent from the graph.

Everything it prints is a POINTER. CORR-270 applies: nothing here may be graded
from an abstract. The point is to shorten the list a human has to read, not to
draw conclusions.
"""
import json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NODES = os.path.join(ROOT, "nodes")
BIB = os.path.join(ROOT, "sources", "bibliography.yaml")
OUT = os.path.join(ROOT, "data", "round279")

QUERIES = [
    # wild-type / normal animal + length gain, by intervention vocabulary
    '("wild-type" OR "wild type" OR normal) AND (mice OR mouse OR rat) AND ("increased bone length" OR "increased femur length" OR "increased tibia length" OR "increased body length" OR "longer bones" OR "increased longitudinal bone growth")',
    '(treatment OR administration OR agonist OR antagonist OR inhibitor) AND ("naso-anal" OR nasoanal OR "crown-rump") AND (increase* OR longer OR greater)',
    '("growth plate") AND (agonist OR inhibitor OR antagonist OR "small molecule") AND ("bone length" OR "tibia length" OR "femur length") AND increase*',
    '("bone elongation" OR "longitudinal growth") AND (enhanc* OR increas* OR promot*) AND ("small molecule" OR compound OR drug OR agonist)',
    # specific under-swept axes
    '(Wnt OR "beta-catenin" OR sclerostin OR "LRP5") AND ("bone length" OR "longitudinal bone growth" OR "growth plate") AND (increase* OR longer)',
    '(androgen OR oxandrolone OR "selective androgen receptor" OR SARM) AND ("bone growth" OR "growth plate" OR "linear growth" OR height)',
    '(BMP OR "bone morphogenetic") AND (inhibitor OR antagonist OR LDN OR DMH1) AND ("growth plate" OR "bone length" OR "longitudinal growth")',
    '(mTOR OR rapamycin OR "AMPK" OR metformin) AND ("bone length" OR "longitudinal bone growth") AND (mice OR rat)',
    '(hypoxia OR HIF OR "prolyl hydroxylase" OR roxadustat OR "PHD inhibitor") AND ("growth plate" OR "bone growth" OR "bone length")',
    '(SHOX OR "aggrecan" OR ACAN OR "natriuretic") AND (overexpress* OR agonist OR therapy) AND ("bone length" OR stature OR "growth plate")',
    '("intervertebral disc" OR "vertebral body") AND (height OR growth) AND (increase* OR restore* OR regenerat*) AND (agent OR injection OR compound)',
    '(thyroid OR "T3" OR "thyroid hormone receptor") AND (antagonist OR inhibitor OR "beta selective") AND ("growth plate" OR "bone growth" OR fusion)',
    '(GDF5 OR "FGF18" OR sprifermin OR "IGF-2" OR "PTHrP analog") AND ("growth plate" OR "bone length" OR "longitudinal growth")',
    '(senolytic OR "partial reprogramming" OR "Yamanaka" OR OSK) AND (cartilage OR "growth plate") AND (length OR growth OR elongation)',
]

LENGTH = re.compile(
    r"(bone|femur|femoral|tibia|tibial|humer\w+|metatarsal|limb|body|leg|vertebr\w+|spine|tail|naso-?anal|crown-rump)"
    r"[\s-]*(length|elongation|growth|height)|longitudinal (bone )?growth|body length|stature|linear growth",
    re.I)
GAIN = re.compile(r"\b(increas\w+|longer|greater|enhanc\w+|promot\w+|augment\w+|stimulat\w+|accelerat\w+|lengthen\w+|gain\w*)\b", re.I)
NORMAL = re.compile(r"\b(wild[- ]type|wildtype|normal|healthy|intact|non-?transgenic|C57BL)\b", re.I)

# drug-name morphology + explicit alphanumeric compound codes
AGENT = re.compile(
    r"\b([A-Z][a-zA-Z]{3,}(?:nib|mab|stat|tide|afil|parib|ciclib|degib|fenib|tinib|sartan|pril|zomib|rafenib|"
    r"limus|mycin|profen|dronate|setron|glitazone|caine|prazole|triptan))\b"
    r"|\b([A-Z]{1,4}[- ]?\d{3,6}[A-Za-z]?)\b"
    r"|\b(SAG21k|dynasore|vosoritide|navepegritide|infigratinib|erdafitinib|sacubitril|osteocrin|meclozine)\b")

STOP = {"COVID", "SARS", "PMID", "PMCID", "DOI", "ISBN", "NCT", "CI", "SD", "SEM", "IQR"}


def q(query, n=25):
    u = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
         + urllib.parse.urlencode({"query": query, "format": "json",
                                   "pageSize": str(n), "resultType": "core"}))
    for _ in range(3):
        try:
            return json.load(urllib.request.urlopen(u, timeout=60))
        except Exception:
            time.sleep(2)
    return {"resultList": {"result": []}}


def atlas_vocabulary():
    """Every lowercase token already present in the graph or bibliography."""
    seen = set()
    for base in (NODES,):
        for dp, _, fs in os.walk(base):
            for fn in fs:
                if fn.endswith(".yaml"):
                    with open(os.path.join(dp, fn), errors="ignore") as fh:
                        seen.update(re.findall(r"[a-z0-9]{4,}", fh.read().lower()))
    if os.path.exists(BIB):
        with open(BIB, errors="ignore") as fh:
            seen.update(re.findall(r"[a-z0-9]{4,}", fh.read().lower()))
    return seen


def main():
    known = atlas_vocabulary()
    sys.stderr.write("atlas vocabulary: %d tokens\n" % len(known))
    hits, seen_pmid = {}, set()
    for query in QUERIES:
        r = q(query)
        res = r["resultList"]["result"]
        sys.stderr.write("%-70s %5s hits, %d pulled\n" % (query[:70], r.get("hitCount"), len(res)))
        for x in res:
            pmid = x.get("pmid") or x.get("id")
            if not pmid or pmid in seen_pmid:
                continue
            seen_pmid.add(pmid)
            ab = ((x.get("title") or "") + " " + (x.get("abstractText") or ""))
            if not ab.strip():
                continue
            # require a length endpoint and a gain word in the SAME sentence
            sent = None
            for s in re.split(r"(?<=[.])\s+", ab):
                if LENGTH.search(s) and GAIN.search(s):
                    sent = s.strip()
                    break
            if not sent:
                continue
            agents = set()
            for m in AGENT.finditer(ab):
                tok = next(g for g in m.groups() if g)
                if tok.upper() in STOP or len(tok) < 4:
                    continue
                agents.add(tok)
            novel = {a for a in agents if re.sub(r"[^a-z0-9]", "", a.lower()) not in known}
            hits[pmid] = {
                "pmid": pmid, "year": x.get("pubYear"), "oa": x.get("isOpenAccess"),
                "pmcid": x.get("pmcid"), "title": (x.get("title") or "")[:140],
                "normal": bool(NORMAL.search(ab)), "agents": sorted(agents),
                "novel": sorted(novel), "sentence": sent[:280],
            }
        time.sleep(0.3)

    rows = sorted(hits.values(), key=lambda h: (-len(h["novel"]), not h["normal"], h["pmid"]))
    os.makedirs(OUT, exist_ok=True)
    json.dump(rows, open(os.path.join(OUT, "candidates.json"), "w"), indent=1)

    novel_rows = [h for h in rows if h["novel"]]
    print("records with a length-gain sentence: %d" % len(rows))
    print("  ... carrying an agent token ABSENT from the atlas: %d" % len(novel_rows))
    print("  ... and stated in a NORMAL/wild-type context: %d"
          % sum(1 for h in novel_rows if h["normal"]))
    print()
    for h in novel_rows:
        print("%s %s OA:%s %s  NORMAL=%s" % (h["pmid"], h["year"], h["oa"], h["pmcid"] or "-", h["normal"]))
        print("   NOVEL AGENTS: %s" % ", ".join(h["novel"]))
        print("   %s" % h["title"])
        print("   > %s" % h["sentence"])
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
