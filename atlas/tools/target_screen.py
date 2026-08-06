#!/usr/bin/env python3
"""
target_screen.py - HYPOTHESIS GENERATION, and it must not be mistaken for anything else.

WHAT THIS IS
------------
The atlas graph knows which mechanism nodes have signed, traversable edges into the
variables that set elongation. This script walks those paths, resolves each upstream
node to a gene symbol, asks ChEMBL which compounds act on that gene and in which
direction, and multiplies the signs through to a PREDICTED DIRECTION ON HEIGHT.

WHAT THIS IS NOT
----------------
It is not evidence that any compound listed increases height. It is not a shortlist of
things to take. Every row is a HYPOTHESIS whose strength is capped by the weakest edge
on its path and by the species that edge was measured in. A row that reads
"predicted +, grade D, mouse" means: one mouse experiment, never replicated, would
predict this if the sign propagates and if the drug reaches cartilage - four
conditionals, any of which can be false.

The output carries, for every row, the things that would let a reader dismiss it:
  - the full signed path, edge by edge
  - the WEAKEST confidence grade anywhere on that path (this caps the claim)
  - the species the path evidence comes from
  - whether the target is expressed in human growth plate at all, where the atlas knows
  - whether the compound is already in the atlas's L12 layer (i.e. already considered)

SIGN ARITHMETIC
---------------
    elongation = (N_p / T_c) * h_term / f_cell * mechanical
so the elasticity of elongation to each is:
    N_p +1,  T_c -1,  h_term +1,  f_cell -1
A compound raises height through a variable if
    drug_action_sign * path_net_sign * variable_elasticity  =  +1
where drug_action_sign is +1 for agonist/activator/opener and -1 for
inhibitor/antagonist/blocker. Any compound whose ChEMBL action_type does not map to a
direction is dropped, not guessed.

THE TWO FAILURE MODES THIS SCRIPT CANNOT PROTECT AGAINST
--------------------------------------------------------
1. EXPOSURE. The growth plate is avascular and alymphatic and no drug concentration has
   ever been measured in it, in any species (gap g_l12b_002). A perfect target with no
   cartilage exposure does nothing. Nothing here models exposure.
2. THE SET POINT. growth_velocity_longitudinal is a sink in this graph - 45 edges in,
   0 out - so the atlas cannot represent a velocity gain being reabsorbed by accelerated
   maturation, which is what happens to most of them clinically. A predicted velocity
   gain is NOT a predicted adult-height gain, and this script cannot tell them apart.

Usage:
  python3 atlas/tools/target_screen.py --extract     # graph paths only, no network
  python3 atlas/tools/target_screen.py --resolve     # + ChEMBL (cached)
  python3 atlas/tools/target_screen.py --report
"""
from __future__ import annotations
import argparse, collections, json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
GRAPH = os.path.join(ROOT, "query", "graph.json")
OUT = os.path.join(ROOT, "query", "target_screen")
CACHE = os.path.join(OUT, "chembl_cache.json")

# ---------------------------------------------------------------- outcomes
# variable -> (node ids, elasticity of elongation wrt that variable)
OUTCOMES = {
    "N_p":    (["clonal_column", "chondrocyte_column_formation"], +1),
    "T_c":    (["cell_cycle_time_pz"], -1),
    "prolif": (["chondrocyte_proliferation_rate"], +1),
    "h_term": (["hypertrophic_chondrocyte", "chondrocyte_hypertrophy",
                "hypertrophic_volume_increase"], +1),
    # Delaying fusion lengthens the integral of velocity over time. The flow model has
    # no time axis at all, so this is scored SEPARATELY and never summed with the rest.
    "fusion": (["epiphyseal_fusion", "growth_plate_senescence"], -1),
}
SIGNV = {"+": 1, "-": -1}
GRADE_ORDER = ["A", "B", "C", "D", "E", "speculative", "X"]
ACTION = {
    "AGONIST": +1, "PARTIAL AGONIST": +1, "ACTIVATOR": +1, "OPENER": +1,
    "POSITIVE ALLOSTERIC MODULATOR": +1, "POSITIVE MODULATOR": +1,
    "INHIBITOR": -1, "ANTAGONIST": -1, "BLOCKER": -1, "NEGATIVE ALLOSTERIC MODULATOR": -1,
    "INVERSE AGONIST": -1, "NEGATIVE MODULATOR": -1, "DISRUPTING AGENT": -1,
    "DEGRADER": -1, "SEQUESTERING AGENT": -1,
}


def _phase(v):
    """ChEMBL max_phase is sometimes a string, sometimes a float, sometimes null."""
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def weakest(grades):
    idx = [GRADE_ORDER.index(g) if g in GRADE_ORDER else len(GRADE_ORDER) for g in grades]
    return GRADE_ORDER[max(idx)] if idx else "X"


# ---------------------------------------------------------------- graph walk
def load_graph():
    g = json.load(open(GRAPH))
    adj = collections.defaultdict(list)
    for e in g["edges"]:
        adj[e["source"]].append(e)
    return g["nodes"], g["edges"], adj


def signed_paths(adj, nodes, maxdepth=3):
    """For every node, the best signed path into each outcome.

    'Best' = shortest, tie-broken by strongest weakest-grade. Only traversal_usable
    edges with an explicit + or - sign are walked; sign-exempt relations
    (precedes/binds/correlates_with/hypothesized_link) are NOT traversed, because
    signing them would be fabrication.
    """
    targets = {n: k for k, (ids, _) in OUTCOMES.items() for n in ids}
    best = collections.defaultdict(dict)          # src -> outcome -> record
    for src in nodes:
        if src in targets:
            continue
        q = collections.deque([(src, [], 1)])
        seen = {src}
        while q:
            u, path, sg = q.popleft()
            if len(path) >= maxdepth:
                continue
            for e in adj.get(u, []):
                if not e.get("traversal_usable"):
                    continue
                s = SIGNV.get(e.get("sign"))
                if s is None:
                    continue
                v, np_, ns = e["target"], path + [e], sg * s
                if v in targets:
                    oc = targets[v]
                    grades = [x.get("confidence") or "X" for x in np_]
                    rec = {"outcome": oc, "net_sign": ns, "len": len(np_),
                           "weakest_grade": weakest(grades),
                           "edges": [x["edge_id"] for x in np_],
                           "route": " -> ".join([src] + [x["target"] for x in np_]),
                           "refs": sorted({r for x in np_ for r in (x.get("refs") or [])}),
                           "endpoint": v}
                    cur = best[src].get(oc)
                    if cur is None or (rec["len"], GRADE_ORDER.index(rec["weakest_grade"])) \
                            < (cur["len"], GRADE_ORDER.index(cur["weakest_grade"])):
                        best[src][oc] = rec
                elif v not in seen:
                    seen.add(v)
                    q.append((v, np_, ns))
    return best


GENE_RE = re.compile(r"^[A-Z][A-Z0-9]{1,9}(-[A-Z0-9]{1,4})?$")

# A drug acts on a MOLECULE. Attaching one to any other kind of node inverts signs.
#
# This nearly shipped wrong. `aromatase_deficiency_human` is a PHENOTYPE node whose name
# contains "CYP19A1", so the symbol was extracted from it and every aromatase inhibitor
# was attached to it. But that node's path to fusion already encodes LOSS of enzyme
# activity (net -1), so applying an inhibitor's -1 on top double-negates: anastrozole
# came out predicted to DECREASE height. The correct route from the protein node
# `aromatase_cyp19a1` (net +1) gives the right answer. Both rows were emitted and the
# wrong one sorted first.
#
# So: only molecular-entity node types may carry a compound.
DRUGGABLE_TYPES = {"gene", "protein", "hormone", "metabolite"}

# Pathway and complex nodes have no single gene symbol in their name, so the automated
# resolver silently skips them - which is how the mTOR positive control produced zero
# rows and looked like "no mTOR drugs exist" rather than "the resolver missed it".
# These mappings are CURATED, declared here, and deliberately few: each names the
# subunit a drug actually binds, not the whole complex.
#
# EACH CURATED GENE CARRIES A POLARITY, and omitting it inverted a conclusion.
#
# +1 means agonising the gene agonises the node. -1 means the gene is a NEGATIVE
# regulator, so a drug ChEMBL calls an INHIBITOR of it ACTIVATES the node.
#
# This was found by reading schipani2001, the sole primary under the screen's only
# approved-drug candidate. EGLN1/PHD2 hydroxylates HIF-1a for degradation, so a PHD
# inhibitor RAISES hypoxic signalling. The screen had EGLN1 at implicit +1, applied
# ChEMBL's "INHIBITOR" as -1 to the node `hypoxic_gradient_signaling`, and returned
# roxadustat/vadadustat/daprodustat as predicted to INCREASE proliferation. The atlas
# edge is correct and negative (e00353, hif1a --inhibits--> proliferation, refs
# schipani2001, which reports INCREASED BrdU in HIF-1a-null growth plates). With the
# polarity restored the same drugs are predicted to DECREASE it.
#
# This is the third instance of one bug: a compound attached to a node that is not its
# target. Phenotype nodes encoded loss of function; pathway nodes had no symbol; and now
# a negative-regulator subunit inverts the sign. The general rule the screen enforces:
# a drug may only be attached to a node whose relationship to the drug's actual target
# is IDENTITY, or to a curated node with an explicit declared polarity.
CURATED_GENES = {
    "mtorc1_chondrocyte": [("MTOR", +1), ("RPTOR", +1)],
    "mek1_erk_chondrocyte": [("MAP2K1", +1), ("MAPK1", +1), ("MAPK3", +1)],
    "notch_signaling_chondrocyte": [("NOTCH1", +1), ("NOTCH2", +1), ("PSEN1", +1)],
    "tgfb_signaling_chondrocyte": [("TGFBR1", +1), ("TGFBR2", +1)],
    "hypoxic_gradient_signaling": [("HIF1A", +1), ("EGLN1", -1)],   # PHD degrades HIF
    "pi_ppi_ratio": [("ENPP1", -1),      # generates PPi, lowers the Pi/PPi ratio
                     ("ALPL", +1),       # hydrolyses PPi, raises it
                     ("SLC20A1", +1)],   # imports Pi
}


def gene_polarity(node_id, gene):
    """+1 if agonising `gene` agonises the node; -1 if it inverts. See CURATED_GENES."""
    for g, p in CURATED_GENES.get(node_id, []):
        if g == gene:
            return p
    return 1


def gene_candidates(node):
    """Pull plausible HGNC symbols out of a node's id, name and aliases.

    Deliberately conservative: an unresolvable node is dropped, never guessed at, and a
    node that is not a molecular entity is refused outright regardless of what its name
    happens to contain.
    """
    nid_ = node.get("id", "")
    if nid_ in CURATED_GENES:
        return [g for g, _ in CURATED_GENES[nid_]]
    if node.get("type") not in DRUGGABLE_TYPES:
        return []
    out = []
    for s in [node.get("name", "")] + (node.get("aliases") or []):
        for tok in re.split(r"[^A-Za-z0-9\-]+", s):
            if GENE_RE.match(tok) and not tok.isdigit():
                out.append(tok)
    nid = node.get("id", "")
    m = re.match(r"^([a-z0-9]+)_(gene|protein|receptor|kinase|enzyme|tf|channel)", nid)
    if m:
        out.append(m.group(1).upper())
    seen, res = set(), []
    for g in out:
        if g not in seen and len(g) >= 3:
            seen.add(g)
            res.append(g)
    return res[:4]


# ---------------------------------------------------------------- ChEMBL
def _get(url, tries=3):
    for i in range(tries):
        try:
            r = urllib.request.Request(url, headers={"User-Agent": "growth-plate-atlas"})
            return json.load(urllib.request.urlopen(r, timeout=60))
        except Exception:
            if i == tries - 1:
                return None
            time.sleep(2 * (i + 1))


def chembl_for_gene(gene, cache):
    if gene in cache:
        return cache[gene]
    res = {"target_chembl_id": None, "pref_name": None, "mechanisms": []}
    d = _get("https://www.ebi.ac.uk/chembl/api/data/target/search.json?q="
             + urllib.parse.quote(gene) + "&limit=25")
    tid = None
    if d:
        for t in d.get("targets", []):
            if t.get("organism") != "Homo sapiens" or t.get("target_type") != "SINGLE PROTEIN":
                continue
            syns = {s.get("component_synonym", "").upper()
                    for c in t.get("target_components", [])
                    for s in c.get("target_component_synonyms", [])}
            if gene.upper() in syns:
                tid, res["pref_name"] = t["target_chembl_id"], t.get("pref_name")
                break
    if tid:
        res["target_chembl_id"] = tid
        m = _get(f"https://www.ebi.ac.uk/chembl/api/data/mechanism.json?"
                 f"target_chembl_id={tid}&limit=1000")
        for x in (m or {}).get("mechanisms", []):
            res["mechanisms"].append({
                "molecule_chembl_id": x.get("molecule_chembl_id"),
                "action_type": x.get("action_type"),
                "mechanism_of_action": x.get("mechanism_of_action"),
                "max_phase": x.get("max_phase")})
    cache[gene] = res
    return res


def molecule_names(ids, cache):
    todo = [i for i in ids if i and ("mol:" + i) not in cache]
    for i in range(0, len(todo), 40):
        chunk = todo[i:i + 40]
        d = _get("https://www.ebi.ac.uk/chembl/api/data/molecule.json?molecule_chembl_id__in="
                 + ",".join(chunk) + "&limit=100")
        for m in (d or {}).get("molecules", []):
            cache["mol:" + m["molecule_chembl_id"]] = {
                "name": m.get("pref_name"),
                "max_phase": m.get("max_phase"),
                "type": m.get("molecule_type"),
                "oral": (m.get("molecule_properties") or {}).get("num_ro5_violations")}
        for c in chunk:
            cache.setdefault("mol:" + c, {"name": None, "max_phase": None,
                                          "type": None, "oral": None})
    return cache


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--extract", action="store_true")
    ap.add_argument("--resolve", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--maxdepth", type=int, default=3)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    nodes, edges, adj = load_graph()

    paths_file = os.path.join(OUT, "paths.json")
    if a.extract or not os.path.exists(paths_file):
        best = signed_paths(adj, nodes, a.maxdepth)
        rows = []
        for src, ocs in best.items():
            n = nodes[src]
            rows.append({"node": src, "name": n.get("name"), "layer": n.get("layer"),
                         "type": n.get("type"),
                         "node_confidence": n.get("confidence"),
                         "human_evidence": n.get("human_evidence"),
                         "species_basis": n.get("species_basis"),
                         "genes": gene_candidates(n),
                         "outcomes": ocs})
        json.dump(rows, open(paths_file, "w"), indent=1)
        with_gene = [r for r in rows if r["genes"]]
        print(f"nodes with a signed path to an outcome : {len(rows)}")
        print(f"  of which a gene symbol was extracted : {len(with_gene)}")
        oc = collections.Counter(o for r in rows for o in r["outcomes"])
        for k, v in oc.most_common():
            print(f"    {k:8s} {v:4d} upstream nodes")
        if not a.resolve:
            return 0

    rows = json.load(open(paths_file))
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    if a.resolve:
        genes = sorted({g for r in rows for g in r["genes"]})
        print(f"resolving {len(genes)} gene symbols against ChEMBL (cached)")
        for i, g in enumerate(genes):
            chembl_for_gene(g, cache)
            if i % 25 == 0:
                json.dump(cache, open(CACHE, "w"))
                print(f"  {i}/{len(genes)}", flush=True)
        mols = {m["molecule_chembl_id"] for g in genes
                for m in cache.get(g, {}).get("mechanisms", [])}
        molecule_names(sorted(mols), cache)
        json.dump(cache, open(CACHE, "w"))
        print(f"  done; {sum(1 for g in genes if cache.get(g,{}).get('target_chembl_id'))}"
              f" genes resolved to a human single-protein ChEMBL target")

    # ---------------- assemble candidates
    l12 = {n for n, d in nodes.items() if d.get("layer") == "L12"}
    l12_names = {(nodes[n].get("name") or "").lower() for n in l12}
    cands = []
    for r in rows:
        for oc, rec in r["outcomes"].items():
            elas = OUTCOMES[oc][1]
            for g in r["genes"]:
                c = cache.get(g) or {}
                for m in c.get("mechanisms", []):
                    act = ACTION.get((m.get("action_type") or "").upper())
                    if act is None:
                        continue
                    mol = cache.get("mol:" + m["molecule_chembl_id"], {})
                    pol = gene_polarity(r["node"], g)
                    pred = act * pol * rec["net_sign"] * elas
                    cands.append({
                        "predicted_height_direction": "+" if pred > 0 else "-",
                        "outcome": oc, "target_gene": g,
                        "target_pref_name": c.get("pref_name"),
                        "compound": mol.get("name") or m["molecule_chembl_id"],
                        "chembl_id": m["molecule_chembl_id"],
                        "max_phase": mol.get("max_phase"),
                        "action_type": m.get("action_type"),
                        "gene_polarity_to_node": pol,
                        "path_net_sign": rec["net_sign"],
                        "elasticity": elas,
                        "weakest_grade_on_path": rec["weakest_grade"],
                        "path_len": rec["len"],
                        "route": rec["route"],
                        "edges": rec["edges"],
                        "path_refs": rec["refs"],
                        "upstream_node": r["node"],
                        "upstream_human_evidence": r["human_evidence"],
                        "upstream_species": r["species_basis"],
                        "already_in_L12": bool(mol.get("name")
                                               and mol["name"].lower() in l12_names)})
    json.dump(cands, open(os.path.join(OUT, "candidates.json"), "w"), indent=1)
    print(f"\ncandidate (compound x outcome) rows: {len(cands)}")
    pos = [c for c in cands if c["predicted_height_direction"] == "+"]
    print(f"  predicted to INCREASE a growth variable: {len(pos)}")
    print(f"  distinct compounds among those        : "
          f"{len({c['compound'] for c in pos})}")
    print(f"  of those, already an L12 node         : "
          f"{len({c['compound'] for c in pos if c['already_in_L12']})}")
    g = collections.Counter((c["weakest_grade_on_path"], c["outcome"]) for c in pos)
    print("\n  predicted-positive rows by weakest grade on the path and outcome:")
    for (gr, oc), v in sorted(g.items()):
        print(f"    grade {gr:11s} {oc:8s} {v:5d}")

    # ---------------- human growth-plate expression filter
    expr = {}
    ep = os.path.join(ROOT, "query", "human_growth_plate_expression.csv")
    if os.path.exists(ep):
        import csv as _csv
        for row in _csv.DictReader(open(ep)):
            expr[row["gene"]] = int(row["n_donors_detected"])
    else:
        print("\n  NO human expression table found - filter SKIPPED, not silently passed")

    # ---------------- aggregate per compound
    # A compound is one object even when it reaches several variables by several routes.
    # Scoring it per-row would let a promiscuous kinase inhibitor outrank a specific
    # agent purely by appearing more often.
    agg = {}
    for c in cands:
        k = c["compound"]
        a_ = agg.setdefault(k, {
            "compound": k, "chembl_id": c["chembl_id"], "max_phase": c["max_phase"],
            "helps": {}, "harms": {}, "targets": set(), "already_in_L12": False,
            "best_grade": "X", "min_len": 99, "routes": []})
        a_["already_in_L12"] |= c["already_in_L12"]
        a_["targets"].add(c["target_gene"])
        side = "helps" if c["predicted_height_direction"] == "+" else "harms"
        prev = a_[side].get(c["outcome"])
        cur = (GRADE_ORDER.index(c["weakest_grade_on_path"]), c["path_len"])
        if prev is None or cur < prev[0]:
            a_[side][c["outcome"]] = (cur, c["route"], c["weakest_grade_on_path"],
                                      c["target_gene"], c["path_refs"])
        if side == "helps":
            if GRADE_ORDER.index(c["weakest_grade_on_path"]) < GRADE_ORDER.index(a_["best_grade"]):
                a_["best_grade"] = c["weakest_grade_on_path"]
            a_["min_len"] = min(a_["min_len"], c["path_len"])
            a_["routes"].append(c["route"])
    for a_ in agg.values():
        a_["targets"] = sorted(a_["targets"])
        a_["n_donors_detected"] = max((expr.get(t, -1) for t in a_["targets"]),
                                      default=-1) if expr else None
        a_["expressed_in_human_gp"] = (a_["n_donors_detected"] is not None
                                       and a_["n_donors_detected"] >= 2)
        a_["target_expression"] = {t: expr.get(t, -1) for t in a_["targets"]} if expr else {}
        for side in ("helps", "harms"):
            a_[side] = {k2: {"route": v[1], "grade": v[2], "via": v[3], "refs": v[4]}
                        for k2, v in a_[side].items()}
    out_rows = sorted(agg.values(), key=lambda r: (
        GRADE_ORDER.index(r["best_grade"]), -len(r["helps"]), r["min_len"],
        -_phase(r["max_phase"])))
    json.dump(out_rows, open(os.path.join(OUT, "compounds.json"), "w"), indent=1)

    live = [r for r in out_rows if r["helps"] and r["expressed_in_human_gp"]]
    print(f"\n  distinct compounds with >=1 predicted-positive route : {len([r for r in out_rows if r['helps']])}")
    print(f"    of those whose target is detected in >=2/4 human donors: {len(live)}")
    print(f"    of those NOT already an L12 node                       : "
          f"{len([r for r in live if not r['already_in_L12']])}")
    print(f"\n  wrote {os.path.join(OUT,'compounds.json')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
