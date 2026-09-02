#!/usr/bin/env python3
"""
ROUND 269 - the CORR-272 sweep, run rather than recommended.

CORR-272's finding was that xiu2022 sat in this graph for months as an L3
signalling edge (sufu_protein -> gli2_tf | inhibits) while the paper behind it
carried micro-CT femur lengths at two ages under two opposite perturbations.
Keyword search over node PROSE cannot find that, because the graph recorded the
signalling fact and dropped the length fact.

So: search the REFERENCES the graph cites, not the graph's own prose.

For every reference in the bibliography, fetch the abstract from PubMed and ask
two questions:
  (1) does the abstract report a LONGITUDINAL LENGTH endpoint - bone, limb or
      body length, or stature - as opposed to a zone height, plate width or
      area, which CORR-189 says are not growth rates?
  (2) does any node in this graph record a quantitative finding from that
      reference at all?

A reference that answers YES to (1) and NO to (2) is a length endpoint this
atlas is sitting on. That is the xiu2022 failure mode, enumerated.

Outputs a ranked TSV. Nothing here is a biological claim - it is a pointer list,
and every hit must be read in full before anything is graded. Search results are
claims about the query (CORR-267).
"""
import json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "sources", "bibliography.yaml")
NODES = os.path.join(ROOT, "nodes")
CACHE = os.path.join(ROOT, "data", "round269", "abstracts.json")

# (1) A LENGTH endpoint. Deliberately excludes zone height, plate thickness and
#     area - CORR-189 says those are not growth rates and not yields.
LENGTH = re.compile(
    r"\b(bone|femur|femoral|tibia|tibial|humerus|humeral|radius|ulna|metatarsal|"
    r"limb|leg|body|crown-rump|naso-anal|nose-to-tail|tail)\s*(-|\s)?\s*"
    r"(length|elongation|growth)\b"
    r"|\blongitudinal (bone )?growth\b"
    r"|\bbody length\b|\bfinal height\b|\badult height\b|\battained height\b"
    r"|\bstature\b|\bheight (SDS|SD score|standard deviation)\b"
    r"|\blinear growth\b|\bgrowth velocity\b",
    re.I,
)
# A direction word, so that "we measured bone length" ranks below "bone length increased".
DIRECTION = re.compile(
    r"\b(increas\w+|decreas\w+|reduc\w+|longer|shorter|greater|lesser|enhanc\w+|"
    r"impair\w+|promot\w+|inhibit\w+|rescu\w+|restor\w+|accelerat\w+|attenuat\w+|"
    r"gain\w*|loss|shorten\w+|lengthen\w+|unaffected|no (significant )?(change|difference))\b",
    re.I,
)
# Species, so a human hit can be ranked above a mouse one.
HUMAN = re.compile(r"\b(patient|child|children|human|boy|girl|adolescen\w+|cohort|trial)\b", re.I)


def load_bibliography():
    """Parse ref_id/pmid/title pairs without a yaml dependency on nested schema."""
    refs = {}
    cur = None
    with open(BIB, errors="ignore") as fh:
        for line in fh:
            m = re.match(r"^  ([A-Za-z0-9_.\-]+):\s*$", line)
            if m:
                cur = m.group(1)
                refs[cur] = {"ref_id": cur, "pmid": None, "title": None, "year": None}
                continue
            if cur is None:
                continue
            m = re.match(r"^    pmid:\s*'?([0-9]+)'?\s*$", line)
            if m:
                refs[cur]["pmid"] = m.group(1)
            m = re.match(r"^    title:\s*(.+?)\s*$", line)
            if m:
                refs[cur]["title"] = m.group(1).strip("'\"")
            m = re.match(r"^    year:\s*'?([0-9]{4})'?\s*$", line)
            if m:
                refs[cur]["year"] = m.group(1)
    return refs


def refs_with_recorded_quantities():
    """Every ref_id that appears as a source_ref in some node's quantitative block.

    This is the test for 'the graph already took a number from this paper'. A ref
    cited only in key_refs or in an edge is NOT counted - that is precisely the
    xiu2022 state, where the paper was cited for a mechanism and its measurements
    were never extracted.
    """
    seen = set()
    for dirpath, _, files in os.walk(NODES):
        for fn in files:
            if not fn.endswith(".yaml"):
                continue
            with open(os.path.join(dirpath, fn), errors="ignore") as fh:
                for line in fh:
                    m = re.match(r"\s*source_ref:\s*([A-Za-z0-9_.\-]+)\s*$", line)
                    if m:
                        seen.add(m.group(1))
    return seen


def fetch_abstracts(pmids):
    out = {}
    if os.path.exists(CACHE):
        out.update(json.load(open(CACHE)))
    todo = [p for p in pmids if p not in out]
    for i in range(0, len(todo), 150):
        batch = todo[i : i + 150]
        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
            + urllib.parse.urlencode(
                {"db": "pubmed", "id": ",".join(batch), "retmode": "xml"}
            )
        )
        for attempt in range(4):
            try:
                raw = urllib.request.urlopen(url, timeout=120).read()
                break
            except Exception:
                time.sleep(2 * (attempt + 1))
                raw = None
        if raw is None:
            sys.stderr.write("batch failed at %d\n" % i)
            continue
        try:
            root = ET.fromstring(raw)
        except ET.ParseError:
            sys.stderr.write("parse error at %d\n" % i)
            continue
        for art in root.iter("PubmedArticle"):
            pid = art.findtext(".//PMID")
            texts = [t.text or "" for t in art.iter("AbstractText")]
            title = art.findtext(".//ArticleTitle") or ""
            out[pid] = (title + " " + " ".join(texts)).strip()
        for pid in batch:
            out.setdefault(pid, "")
        sys.stderr.write("fetched %d/%d\n" % (min(i + 150, len(todo)), len(todo)))
        time.sleep(0.4)
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    json.dump(out, open(CACHE, "w"))
    return out


def main():
    refs = load_bibliography()
    recorded = refs_with_recorded_quantities()
    pmids = [r["pmid"] for r in refs.values() if r["pmid"]]
    abstracts = fetch_abstracts(pmids)

    rows = []
    for r in refs.values():
        if not r["pmid"]:
            continue
        ab = abstracts.get(r["pmid"], "")
        if not ab:
            continue
        lm = LENGTH.findall(ab)
        if not lm:
            continue
        score = 0
        score += 3 if DIRECTION.search(ab) else 0
        score += 2 if HUMAN.search(ab) else 0
        score += min(len(lm), 3)
        already = r["ref_id"] in recorded
        rows.append(
            {
                "ref_id": r["ref_id"],
                "pmid": r["pmid"],
                "year": r["year"] or "",
                "quantitative_recorded": "YES" if already else "NO",
                "score": score,
                "human": "Y" if HUMAN.search(ab) else "",
                "title": (r["title"] or "")[:120],
            }
        )

    rows.sort(key=lambda x: (x["quantitative_recorded"] == "YES", -x["score"], x["ref_id"]))
    unrecorded = [x for x in rows if x["quantitative_recorded"] == "NO"]

    print(
        "TOTAL refs %d | with pmid %d | abstracts retrieved %d"
        % (len(refs), len(pmids), sum(1 for p in pmids if abstracts.get(p)))
    )
    print(
        "refs whose ABSTRACT reports a longitudinal LENGTH endpoint: %d" % len(rows)
    )
    print(
        "  ... of which the graph has NEVER recorded a quantitative finding: %d"
        % len(unrecorded)
    )
    print()
    print("\t".join(["ref_id", "pmid", "year", "quant", "score", "human", "title"]))
    for x in rows:
        print(
            "\t".join(
                [
                    x["ref_id"],
                    x["pmid"],
                    x["year"],
                    x["quantitative_recorded"],
                    str(x["score"]),
                    x["human"],
                    x["title"],
                ]
            )
        )


if __name__ == "__main__":
    main()
