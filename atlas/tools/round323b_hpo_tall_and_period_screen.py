#!/usr/bin/env python3
"""
ROUND 323b. THE HPO FILES, FINALLY QUERIED - the human phenotype ontology was supplied on
2026-08-13 and CLAUDE.md registered it with the words "replaces per-syndrome manual curation".
It was never opened. This is CORR-316 and CORR-328 again: run the local data before the
literature.

WHY IT IS WORTH RUNNING DESPITE CORR-295. CORR-295 says a DISEASE literature is the wrong
place to look for height-INCREASING levers, because being short brings a child to a clinic and
being tall does not. That correction is about SEARCH BIAS, and the right response to a known
bias is to measure it rather than to avoid the resource. This screen measures it in one line:
the ratio of genes annotated to short stature against genes annotated to tall stature.

TWO GENE SETS, BOTH OF WHICH THE ATLAS HAS WANTED FOR MANY ROUNDS.
  A. TALL - the union of HP:0000098 Tall stature, HP:0001519 Disproportionate tall stature and
     HP:0011407 Proportionate tall stature, with genes ALSO annotated to HP:0004322 Short
     stature REMOVED. A gene that can present either way carries no direction, which is the
     defect CORR-325 named in the microfibril module (FBN1 het +8.82 cm, biallelic missense =
     acromicric dysplasia, short).
  B. PERIOD - HP:0002750 Delayed skeletal maturation minus HP:0005616 Accelerated skeletal
     maturation. At bone age 16 the scarce resource is the PERIOD and the stack contains
     exactly one period agent. A human-genetic list of period-extending lesions has never
     existed in this atlas.

THE JOINS. Human growth plate expression (GSE288028, 14 postnatal samples, 79,934 cells) for
CORR-327; kosmicki2026 Supplementary Table 6 for a signed effect in centimetres where the gene
is one of the 207; Open Targets for tractability and drugs, with each drug's direction
classified and compared against the direction the phenotype implies.

WHAT IT CANNOT DO. An HPO annotation is a curated statement about a SYNDROME, usually
germline and usually biallelic or de novo, with no effect size and no allele. It nominates;
it cannot rank. And a syndrome that includes tall stature among twenty features is not
evidence that the gene is a height lever - it is evidence that the gene is somewhere upstream
of one.

Usage:  python3 atlas/tools/round323b_hpo_tall_and_period_screen.py
"""
import collections
import json
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HPO = os.path.join(HERE, "data", "supplied_2026_08_13", "hpo_phenotype_to_genes.txt")
OUTDIR = os.path.join(HERE, "data", "round323")
OT = "https://api.platform.opentargets.org/api/v4/graphql"

TALL = ["HP:0000098", "HP:0001519", "HP:0011407"]
SHORT = ["HP:0004322"]
DELAYED = ["HP:0002750"]
ADVANCED = ["HP:0005616"]

INHIBIT_WORDS = ("inhibitor", "antagonist", "blocker", "negative modulator", "degrader",
                 "inverse agonist", "disrupting agent", "suppressor")
ACTIVATE_WORDS = ("agonist", "activator", "positive modulator", "stimulant", "opener",
                  "potentiator", "substitute", "replacement")

Q = """query($ids:[String!]!){targets(ensemblIds:$ids){
  id approvedSymbol
  tractability{label modality value}
  drugAndClinicalCandidates{count rows{drug{id name drugType maximumClinicalStage
    mechanismsOfAction{rows{actionType mechanismOfAction}}}}}
}}"""


def gql(query, variables, tries=4):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(OT, data=body, headers={"Content-Type": "application/json"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # noqa: BLE001
            if i == tries - 1:
                print("  ! %s" % e, file=sys.stderr)
                return None
            time.sleep(2 ** i)
    return None


def classify(a):
    a = (a or "").lower()
    if any(w in a for w in INHIBIT_WORDS):
        return "down"
    if any(w in a for w in ACTIVATE_WORDS):
        return "up"
    return "?"


def load_hpo():
    by = collections.defaultdict(set)
    dis = collections.defaultdict(set)
    with open(HPO) as f:
        f.readline()
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) < 5:
                continue
            by[p[0]].add(p[3])
            dis[(p[0], p[3])].add(p[4])
    return by, dis


def ens_ids(symbols):
    out = {}
    for s in symbols:
        for _ in range(2):
            try:
                u = ("https://rest.ensembl.org/lookup/symbol/homo_sapiens/%s"
                     "?content-type=application/json" % s)
                out[s] = json.load(urllib.request.urlopen(u, timeout=25))["id"]
                break
            except Exception:  # noqa: BLE001
                time.sleep(1.0)
    return out


def ot_lookup(symbols):
    ids = ens_ids(symbols)
    rev = {v: k for k, v in ids.items()}
    tmap = {}
    idl = sorted(set(ids.values()))
    for i in range(0, len(idl), 25):
        d = gql(Q, {"ids": idl[i:i + 25]})
        if d and "data" in d:
            for t in d["data"]["targets"] or []:
                tmap[t["approvedSymbol"]] = t
        time.sleep(0.25)
    print("  Open Targets resolved %d/%d (%d ensembl ids)" % (len(tmap), len(symbols), len(idl)))
    return tmap, rev


def summarise(t, want):
    tract = sorted({x["label"] for x in (t["tractability"] or []) if x.get("value")})
    seen = {}
    for r in ((t.get("drugAndClinicalCandidates") or {}).get("rows") or []):
        d = r.get("drug") or {}
        nm = d.get("name")
        if not nm:
            continue
        cur = seen.setdefault(nm, dict(name=nm, drugtype=d.get("drugType"),
                                       approved=(d.get("maximumClinicalStage") == "APPROVAL"),
                                       maxphase=d.get("maximumClinicalStage"),
                                       actions=set(), moas=set()))
        for m in ((d.get("mechanismsOfAction") or {}).get("rows") or []):
            if m.get("actionType"):
                cur["actions"].add(m["actionType"])
            if m.get("mechanismOfAction"):
                cur["moas"].add(m["mechanismOfAction"])
    drugs = []
    for v in seen.values():
        v["actions"] = sorted(v["actions"])
        v["moas"] = sorted(v["moas"])
        v["direction"] = classify("; ".join(v["actions"]) + "; " + "; ".join(v["moas"]))
        v["matches_need"] = (v["direction"] == want)
        drugs.append(v)
    drugs.sort(key=lambda x: (not x["matches_need"], not x["approved"], x["name"]))
    return tract, drugs


def main():
    by, dis = load_hpo()
    gp = json.load(open(os.path.join(HERE, "data", "round308",
                                     "gse288028_pseudobulk_presence.json")))["genes"]
    s6 = json.load(open(os.path.join(HERE, "data", "round300", "s6_burden_effects.json")))
    human = {}
    for r in s6:
        if r.get("cat") != "pLoF":
            continue
        if r["gene"] not in human or r["p"] < human[r["gene"]][1]:
            human[r["gene"]] = (r["eff"], r["p"])

    tall = set().union(*[by[t] for t in TALL])
    short = set().union(*[by[t] for t in SHORT])
    delayed = set().union(*[by[t] for t in DELAYED])
    advanced = set().union(*[by[t] for t in ADVANCED])

    print("=" * 100)
    print("THE ASCERTAINMENT ASYMMETRY, MEASURED (CORR-295 as a number)")
    print("=" * 100)
    print("  genes annotated SHORT stature : %d" % len(short))
    print("  genes annotated TALL stature  : %d" % len(tall))
    print("  ratio short:tall              : %.1f : 1" % (len(short) / float(len(tall))))
    print("  annotated BOTH (no direction) : %d" % len(tall & short))
    print("  TALL-ONLY, directional        : %d" % len(tall - short))
    print()
    print("  delayed skeletal maturation   : %d" % len(delayed))
    print("  accelerated                   : %d" % len(advanced))
    print("  delayed ONLY (period-extending): %d" % len(delayed - advanced))

    sets = {"TALL_ONLY": sorted(tall - short),
            "DELAYED_ONLY": sorted(delayed - advanced)}
    # A gene that is BOTH tall-only and period-extending is the strongest shape available here.
    both = sorted(set(sets["TALL_ONLY"]) & set(sets["DELAYED_ONLY"]))
    sets["TALL_AND_PERIOD"] = both

    # expression filter first - the free query, CORR-327
    result = {}
    for name, syms in sets.items():
        rows = []
        for s in syms:
            e = gp.get(s)
            rows.append(dict(gene=s, cpm=(e or {}).get("medCPM"), det=(e or {}).get("det"),
                             maxpct=(e or {}).get("maxPct"),
                             hum_cm=human.get(s, (None, None))[0],
                             hum_p=human.get(s, (None, None))[1],
                             diseases=sorted(set().union(
                                 *[dis[(t, s)] for t in TALL + DELAYED if (t, s) in dis]
                             ))[:4] if any((t, s) in dis for t in TALL + DELAYED) else []))
        rows.sort(key=lambda r: -(r["cpm"] or 0))
        result[name] = rows

    expressed = [r["gene"] for r in result["TALL_ONLY"]
                 if (r["det"] or 0) >= 10 and (r["cpm"] or 0) >= 5]
    print()
    print("  TALL-ONLY genes expressed in the postnatal human growth plate "
          "(>=10/14, >=5 CPM): %d of %d" % (len(expressed), len(result["TALL_ONLY"])))

    print()
    print("=" * 100)
    print("A. TALL-STATURE-ONLY GENES, EXPRESSED IN THE HUMAN GROWTH PLATE")
    print("   want = the pharmacology that PHENOCOPIES the syndrome. Syndromes here are loss")
    print("   or disruption, so the wanted direction is INHIBITION unless noted.")
    print("=" * 100)
    tmap, _ = ot_lookup(expressed)
    tall_rows = []
    for r in result["TALL_ONLY"]:
        if r["gene"] not in expressed:
            continue
        t = tmap.get(r["gene"])
        tract, drugs = summarise(t, "down") if t else ([], [])
        r["tractability"] = tract
        r["drugs"] = drugs
        tall_rows.append(r)
        app = [d["name"] for d in drugs if d["matches_need"] and d["approved"]]
        cli = [d["name"] for d in drugs if d["matches_need"] and not d["approved"]]
        hum = ("%+.2f cm P=%.0e" % (r["hum_cm"], r["hum_p"])) if r["hum_cm"] is not None else "-"
        print("  %-9s %8.1f CPM %2d/14 %5.1f%%  human %-18s %s"
              % (r["gene"], r["cpm"], r["det"], r["maxpct"], hum,
                 ",".join(tract)[:60] or "-"))
        if app:
            print("        APPROVED INHIBITORS : %s" % ", ".join(sorted(app)[:12]))
        if cli:
            print("        clinical inhibitors : %s" % ", ".join(sorted(cli)[:12]))

    print()
    print("=" * 100)
    print("B. PERIOD LIST - DELAYED skeletal maturation and NOT accelerated,")
    print("   expressed in the human growth plate, ranked by abundance")
    print("=" * 100)
    per_expr = [r for r in result["DELAYED_ONLY"]
                if (r["det"] or 0) >= 10 and (r["cpm"] or 0) >= 20]
    print("  %d of %d expressed at >=20 CPM in >=10/14 samples" %
          (len(per_expr), len(result["DELAYED_ONLY"])))
    tmap2, _ = ot_lookup([r["gene"] for r in per_expr])
    for r in per_expr:
        t = tmap2.get(r["gene"])
        tract, drugs = summarise(t, "down") if t else ([], [])
        r["tractability"] = tract
        r["drugs"] = drugs
        app = [d["name"] for d in drugs if d["matches_need"] and d["approved"]]
        hum = ("%+.2f cm" % r["hum_cm"]) if r["hum_cm"] is not None else ""
        print("  %-9s %8.1f CPM %2d/14 %5.1f%% %-10s %s%s"
              % (r["gene"], r["cpm"], r["det"], r["maxpct"], hum,
                 ",".join(tract)[:52] or "-",
                 ("  | APPROVED INHIB: " + ", ".join(sorted(app)[:6])) if app else ""))

    print()
    print("=" * 100)
    print("C. BOTH - tall stature AND delayed maturation, no short-stature annotation")
    print("=" * 100)
    for gsym in both:
        e = gp.get(gsym)
        print("  %-9s %s" % (gsym, ("%.1f CPM %d/14" % (e["medCPM"], e["det"])) if e
                             else "not in GSE288028"))

    os.makedirs(OUTDIR, exist_ok=True)
    json.dump(result, open(os.path.join(OUTDIR, "hpo_tall_and_period.json"), "w"), indent=1,
              default=list)
    print("\nwrote %s" % os.path.join(OUTDIR, "hpo_tall_and_period.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
