#!/usr/bin/env python3
"""
overgrowth_screen.py - run the search backwards, from the only experiments that ever worked.

WHY THIS EXISTS
---------------
Every screen this atlas has run so far starts inside the graph: pick a node, walk signed
edges into an elongation outcome, multiply signs, emit a compound. That search is bounded by
what the graph happens to contain, which is bounded by what has been studied in mice.

This one starts outside. Human overgrowth syndromes and tall-stature associations are a
catalogue of PERTURBATIONS THAT ARE ALREADY KNOWN TO MAKE A HUMAN TALLER - lifetime,
whole-organism, in the right species, integrating growth velocity AND growth duration by
construction, and already run at population scale. Nothing the graph can produce competes
with that as evidence. The field mines the short-stature side exhaustively, because
dwarfisms present in clinic; the tall side is comparatively unmined because being tall is
rarely a complaint.

So: harvest every human gene associated with tall stature or overgrowth, ask which of them
are expressed in a human growth plate, and ask which of them a drug already exists for.

WHAT THE OUTPUT IS AND IS NOT
-----------------------------
A ROW IS NOT A CANDIDATE. It is a gene that satisfies three necessary conditions and none of
the sufficient ones. Three things this tool deliberately does NOT do:

1. IT DOES NOT INFER DIRECTION. An Open Targets association says a gene is implicated in tall
   stature. It does not say whether LOSS or GAIN of function causes it, and therefore does not
   say whether you would want an agonist or an antagonist. FGFR3 carries both: gain of
   function gives achondroplasia, loss of function gives CATSHL tall stature. Every row leaves
   `direction` as UNRESOLVED, to be read from the primary. A screen that guessed here would
   produce confident recommendations with the sign backwards, which is the single most
   expensive mistake in this whole project (see target_screen.py's anastrozole bug).

2. IT DOES NOT DISTINGUISH THE MECHANISM OF TALLNESS. Marfan, Loeys-Dietz and the
   Marfanoid-connective-tissue group are tall through dolichostenomelia - a structural
   collagen/fibrillin defect producing disproportionate limb length - not through a growth
   plate that runs faster or longer. Sotos, Weaver, Tatton-Brown-Rahman and the PIK3CA
   spectrum are chromatin and growth-signalling overgrowth syndromes whose height comes with
   intellectual disability, tumour risk, or both. Neither class is a lead for anything. The
   `mechanism_class` column is left blank for hand classification, because a keyword rule
   would silently discard the interesting cases along with the uninteresting ones.

3. IT DOES NOT SCORE DRUGGABILITY AS DESIRABILITY. A known drug means a molecule exists, not
   that giving it to a growing child is defensible.

The honest use of this file is: it turns an unbounded literature question into a finite
reading list of maybe thirty genes, ranked by how much is already known about each.

Usage:
  python3 atlas/tools/overgrowth_screen.py
"""
from __future__ import annotations
import csv, json, os, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
GP_EXPR = os.path.join(ROOT, "query", "human_growth_plate_expression.csv")
NODES = os.path.join(ROOT, "atlas", "nodes")
OUT = os.path.join(ROOT, "query", "overgrowth_screen")
API = "https://api.platform.opentargets.org/api/v4/graphql"

# Search terms. Deliberately broad on the harvest side; the filtering is done by requiring the
# RETURNED DISEASE NAME to look like overgrowth, so a term that drifts cannot drag in noise.
TERMS = ["tall stature", "overgrowth syndrome", "gigantism", "macrosomia", "acromegaly",
         "Marfan syndrome", "Sotos syndrome", "Weaver syndrome", "Beckwith-Wiedemann",
         "excessive growth", "accelerated skeletal maturation", "advanced bone age"]
KEEP_NAME = re.compile(r"tall|overgrowth|gigantism|macrosom|acromegal|marfan|sotos|weaver|"
                       r"beckwith|malan|tatton|excessive growth|macrocephaly", re.I)
# Terms whose presence means the disease is about being SHORT, however the search matched.
DROP_NAME = re.compile(r"dwarf|short stature|achondroplas|hypochondroplas|microcephal|"
                       r"growth retardation|growth failure|osteogenesis imperfecta", re.I)

SEARCH_D = ('query($q:String!){search(queryString:$q,entityNames:["disease"],page:'
            '{index:0,size:25}){hits{id name}}}')
ASSOC_T = ('query($id:String!,$i:Int!){disease(efoId:$id){name associatedTargets('
           'page:{index:$i,size:50}){count rows{score target{id approvedSymbol}}}}}')
DRUGS = ('query($id:String!){target(ensemblId:$id){approvedSymbol '
         'knownDrugs(size:25){count rows{drugId prefName mechanismOfAction phase status '
         'drugType}}}}')


def gql(query, variables, tries=4):
    for k in range(tries):
        try:
            req = urllib.request.Request(
                API, data=json.dumps({"query": query, "variables": variables}).encode(),
                headers={"Content-Type": "application/json"})
            return json.load(urllib.request.urlopen(req, timeout=90))
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(2 * (k + 1))


def gp_expression():
    """{gene: n_donors_detected} from the four FRESH GSE288028 human growth plate samples.

    Carries the caveat of its source: the donors are children being operated on to PREVENT
    idiopathic tall stature, so this table says a gene is present in a human growth plate, not
    that it is present in a normal one.
    """
    if not os.path.exists(GP_EXPR):
        return {}
    return {r["gene"]: int(r["n_donors_detected"])
            for r in csv.DictReader(open(GP_EXPR))}


def atlas_genes():
    import glob, yaml
    out = {}
    for p in glob.glob(os.path.join(NODES, "**", "*.yaml"), recursive=True):
        try:
            d = yaml.safe_load(open(p))
        except Exception:
            continue
        if not isinstance(d, dict) or not d.get("id"):
            continue
        for name in [d["id"]] + list(d.get("aliases") or []):
            out.setdefault(str(name).upper().replace("_", ""), d["id"])
    return out


CACHE = os.path.join(OUT, "_cache")


def cache_load(name):
    p = os.path.join(CACHE, name)
    return json.load(open(p)) if os.path.exists(p) else None


def cache_save(name, obj):
    os.makedirs(CACHE, exist_ok=True)
    json.dump(obj, open(os.path.join(CACHE, name), "w"))


def main():
    # ---- 1. resolve the disease set -------------------------------------------------------
    # Everything below checkpoints to query/overgrowth_screen/_cache. The first version of
    # this script wrote only at the end and was killed by a timeout after ~50 minutes of live
    # API calls, losing all of it. A long screen that cannot be resumed is a screen that gets
    # run once and then never re-run when a source updates.
    cached = cache_load("harvest.json")
    diseases = {}
    for t in ([] if cached else TERMS):
        try:
            hits = gql(SEARCH_D, {"q": t})["data"]["search"]["hits"]
        except Exception as ex:
            print(f"  search '{t}': ERR {type(ex).__name__}")
            continue
        for h in hits:
            if KEEP_NAME.search(h["name"]) and not DROP_NAME.search(h["name"]):
                diseases[h["id"]] = h["name"]
        time.sleep(0.3)
    if cached:
        diseases, tgt = cached["diseases"], cached["targets"]
        # JSON has no tuples: the (disease, score) pairs come back as lists, which are
        # unhashable, and the dedup below is a set(). Restore them on the way in rather than
        # working around it at every use site.
        for _e in tgt.values():
            _e["diseases"] = [tuple(x) for x in _e["diseases"]]
        print(f"resumed from cache: {len(diseases)} disease terms, {len(tgt)} targets")
    print(f"{len(diseases)} overgrowth / tall-stature disease terms resolved")

    # ---- 2. harvest every associated target ------------------------------------------------
    tgt = tgt if cached else {}
    for n, (did, dname) in enumerate([] if cached else sorted(diseases.items()), 1):
        try:
            page, total = 0, None
            while True:
                d = gql(ASSOC_T, {"id": did, "i": page})["data"]["disease"]
                if d is None:
                    break
                at = d["associatedTargets"]
                total = at["count"]
                for r in at["rows"]:
                    s, sym, eid = r["score"], r["target"]["approvedSymbol"], r["target"]["id"]
                    e = tgt.setdefault(sym, {"ensembl": eid, "best": 0.0, "diseases": []})
                    e["diseases"].append((dname, round(s, 3)))
                    e["best"] = max(e["best"], s)
                page += 1
                if page * 50 >= min(total or 0, 150):   # 150 deep is well past the signal
                    break
            print(f"  {n:3d}/{len(diseases)} {dname[:52]:52s} {total} targets", flush=True)
        except Exception as ex:
            print(f"  {n:3d}/{len(diseases)} {dname[:52]:52s} ERR {type(ex).__name__}")
        time.sleep(0.15)
    if not cached:
        cache_save("harvest.json", {"diseases": diseases, "targets": tgt})
    print(f"\n{len(tgt)} distinct targets across all terms")

    # ---- 3. annotate: growth plate expression, existing drugs, atlas coverage ---------------
    expr, atlas = gp_expression(), atlas_genes()
    dcache = cache_load("drugs.json") or {}

    # The knownDrugs query costs ~20 s per target against this API, so asking it of all 1,596
    # harvested genes takes eight hours. It is also the wrong order of operations: a gene not
    # present in a human growth plate is not a lead whatever drugs exist for it. So the
    # expensive call is made ONLY for genes that clear the free local filters first. Genes that
    # do not clear them are still written out, with n_known_drugs left BLANK rather than zero -
    # blank means NOT ASKED, and conflating that with "no drug exists" would quietly turn an
    # unrun query into a negative result.
    # Thresholds taken from the harvest's own score distribution rather than picked. Over the
    # 1,596 targets the median association score is 0.058 and the 90th percentile is 0.118,
    # with a cliff to 0.396 at p95 - i.e. the bottom nine tenths is the tier where a gene was
    # mentioned near a disease name once. Cutting at p90 and requiring the gene in 3 of 4
    # human growth plate donors leaves 141 targets. A looser cut (0.02, 2 donors) left 1,131,
    # which at ~20 s per drug query is six hours of API time spent ranking noise.
    MIN_ASSOC, MIN_DONORS = 0.10, 3

    def worth_asking(sym, e):
        return expr.get(sym, 0) >= MIN_DONORS and e["best"] >= MIN_ASSOC

    ask = [s_ for s_, e_ in tgt.items() if worth_asking(s_, e_)]
    print(f"{len(ask)} of {len(tgt)} targets clear the free filters "
          f"(detected in >={MIN_DONORS}/4 human growth plate donors AND association "
          f"score >={MIN_ASSOC}, the harvest's own 90th percentile); "
          f"only these get the drug query", flush=True)

    rows = []
    for i, (sym, e) in enumerate(sorted(tgt.items(), key=lambda x: -x[1]["best"]), 1):
        asked = worth_asking(sym, e)
        if not asked:
            drugs = None
        elif sym in dcache:
            drugs = [tuple(d) for d in dcache[sym]]
        else:
            drugs = []
            try:
                kd = gql(DRUGS, {"id": e["ensembl"]})["data"]["target"]
                for r in (kd or {}).get("knownDrugs", {}).get("rows", []) or []:
                    drugs.append((r.get("prefName"), r.get("mechanismOfAction"), r.get("phase")))
            except Exception:
                pass
            dcache[sym] = drugs
            if i % 20 == 0:
                cache_save("drugs.json", dcache)
        seen, uniq = set(), []
        for d in (drugs or []):
            k = (d[0], d[1])
            if k not in seen:
                seen.add(k)
                uniq.append(d)
        top = sorted(uniq, key=lambda d: -(d[2] or 0))[:4]
        rows.append({
            "gene": sym,
            "best_assoc_score": round(e["best"], 4),
            "n_overgrowth_terms": len({d for d, _ in e["diseases"]}),
            "top_terms": "; ".join(f"{d}({s})" for d, s in
                                   sorted(set(e["diseases"]), key=lambda x: -x[1])[:3]),
            "gp_donors_detected": expr.get(sym, ""),
            "in_atlas": atlas.get(sym.upper(), ""),
            "n_known_drugs": len(uniq) if drugs is not None else "",
            "max_phase": (max([d[2] or 0 for d in uniq], default="")
                          if drugs is not None else ""),
            "example_drugs": "; ".join(f"{d[0]} [{d[1]}] ph{d[2]}" for d in top),
            "direction": "UNRESOLVED",
            "mechanism_class": "",
        })
        if asked and i % 10 == 0:
            print(f"  {i}/{len(tgt)} scanned", flush=True)
        if sym not in dcache or not dcache.get(sym):
            time.sleep(0.05)
    cache_save("drugs.json", dcache)

    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, "targets.csv")
    with open(p, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    triple = [r for r in rows if r["gp_donors_detected"] not in ("", 0)
              and isinstance(r["n_known_drugs"], int) and r["n_known_drugs"] > 0]
    json.dump({
        "n_disease_terms": len(diseases), "disease_terms": sorted(diseases.values()),
        "n_targets": len(rows),
        "n_expressed_in_human_gp": sum(1 for r in rows if r["gp_donors_detected"] not in ("", 0)),
        "n_asked_for_drugs": len(ask),
        "filter_thresholds": {"min_assoc_score": MIN_ASSOC, "min_gp_donors": MIN_DONORS,
                              "rationale": "min_assoc is the 90th percentile of the harvest's "
                                           "own score distribution (median 0.058, p90 0.118, "
                                           "p95 0.396) - not a chosen number"},
        "n_with_a_known_drug": sum(1 for r in rows if isinstance(r["n_known_drugs"], int)
                                   and r["n_known_drugs"] > 0),
        "BLANK_n_known_drugs_MEANS": "the drug query was NOT RUN for this gene because it did "
                                     "not clear the free filters. It does not mean no drug "
                                     "exists.",
        "n_meeting_all_three": len(triple),
        "WARNING_DIRECTION": "every row is direction UNRESOLVED. An association does not say "
                             "whether loss or gain of function causes the tall phenotype, so it "
                             "does not say whether an agonist or an antagonist is wanted. FGFR3 "
                             "carries both directions at once. This must be read from the "
                             "primary before any row is treated as a lead.",
        "WARNING_MECHANISM": "tall stature is not one phenotype. The Marfanoid connective-tissue "
                             "group is tall through a structural fibrillin/collagen defect, not "
                             "through growth plate kinetics; the chromatin overgrowth syndromes "
                             "carry intellectual disability and tumour risk. mechanism_class is "
                             "left blank for hand classification on purpose - a keyword rule "
                             "would discard the interesting cases with the uninteresting ones.",
        "WARNING_EXPRESSION": "the human growth plate expression table comes from children "
                              "operated on to PREVENT idiopathic tall stature, so it shows a "
                              "gene is present in A human growth plate, not a normal one.",
    }, open(os.path.join(OUT, "summary.json"), "w"), indent=1)

    print(f"\n{len(rows)} targets | {sum(1 for r in rows if r['gp_donors_detected'] not in ('',0))}"
          f" expressed in human growth plate | "
          f"{sum(1 for r in rows if isinstance(r['n_known_drugs'],int) and r['n_known_drugs']>0)}"
          f" with a known drug | {len(triple)} meeting all three")
    print(f"wrote {p}\n")
    print("targets meeting all three necessary conditions (NOT candidates - direction unread):")
    print(f"  {'gene':10s} {'assoc':>6s} {'GP':>3s} {'drugs':>5s} {'ph':>3s}  terms")
    for r in sorted(triple, key=lambda x: -x["best_assoc_score"])[:40]:
        print(f"  {r['gene']:10s} {r['best_assoc_score']:6.3f} {r['gp_donors_detected']:>3} "
              f"{r['n_known_drugs']:5d} {str(r['max_phase']):>3}  {r['top_terms'][:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
