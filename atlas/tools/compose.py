import json, os, re, sys, collections
sys.path.insert(0, "/home/user/growth-plate/atlas/tools")
from context_filter import AXES, classify
sys.path.insert(0, "/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad")
from overrides import SEX_OVERRIDE, REVIEW_TYPES

SP = "/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad"
dos = json.load(open(SP + "/dossier3.json"))
n2l = json.load(open(SP + "/n2l.json"))
# zones asserted (with refs) in the nodes' own `localization` records
NODEZ = json.load(open(SP + "/node_zone.json"))

# ---------------------------------------------------------------- sex per ref
for rid, d in dos.items():
    sx = d["sex"]
    if d.get("type") in REVIEW_TYPES and not d["sex_basis"].startswith("title"):
        sx = None
    if rid in SEX_OVERRIDE:
        sx = SEX_OVERRIDE[rid]
    d["sex_final"] = sx

# ---------------------------------------------------------------- zone: definitional nodes
ZN = {}
for n in ["resting_zone", "resting_chondrocyte", "resting_zone_niche",
          "pthrp_positive_resting_chondrocyte", "human_resting_zone_chondrocyte",
          "apoe_resting_zone_marker", "foxa2_resting_chondrocyte",
          "rz_depletion_causes_fusion", "label_retaining_chondrocyte",
          "soc_formation_triggers_stemness", "chondroprogenitor_quiescence"]:
    ZN[n] = "resting"
for n in ["proliferative_zone", "proliferative_chondrocyte", "chondrocyte_proliferation_rate",
          "clonal_column", "column_density", "chondrocyte_column_formation",
          "monoclonal_column_formation", "cell_cycle_time_pz", "chondrocyte_rotation"]:
    ZN[n] = "proliferative"
for n in ["prehypertrophic_zone", "prehypertrophic_chondrocyte"]:
    ZN[n] = "prehypertrophic"
for n in ["hypertrophic_zone", "hypertrophic_chondrocyte", "chondrocyte_hypertrophy",
          "hypertrophic_volume_increase", "hypertrophic_phase_duration",
          "hypertrophic_chondrocyte_survival", "chondrocyte_apoptosis_hz",
          "chondrocyte_to_osteoblast_transdifferentiation", "zone_provisional_calcification",
          "chondro_osseous_junction", "cartilage_septum_resorption", "septoclast",
          "mineralization_front", "collagen_type_x"]:
    ZN[n] = "hypertrophic"
for n in ["groove_of_ranvier", "perichondrial_ring_lacroix", "periosteal_stem_cell",
          "appositional_growth"]:
    ZN[n] = "perichondrium"

ZTXT = {"resting": "resting zone", "proliferative": "proliferative zone",
        "prehypertrophic": "prehypertrophic zone", "hypertrophic": "hypertrophic zone",
        "perichondrium": "perichondrium"}
ZORD = ["resting", "proliferative", "prehypertrophic", "hypertrophic", "perichondrium"]

# layers whose readouts have no growth-plate zone at all
ORGANISM_LAYERS = {"L8_genetics_and_heritability", "L9_whole_organism_growth",
                   "L10_environment_and_population", "L13_methods_and_data"}

SPTXT = {"human": "human", "mouse": "mouse", "rat": "rat", "rabbit": "rabbit",
         "chick": "chick", "bovine": "bovine", "pig": "pig", "sheep": "sheep",
         "zebrafish": "zebrafish"}


def ref_species(d):
    sp = d.get("species") or {}
    if not sp:
        return []
    mx = max(sp.values())
    return [s for s in ["human", "mouse", "rat", "rabbit", "chick", "bovine", "pig", "sheep", "zebrafish"]
            if sp.get(s, 0) >= max(3, 0.3 * mx)]


def ref_stage(d):
    """(literal string, [vocab words]) from what the source states."""
    lits, vocab = [], []
    spec = ref_species(d)
    human = spec[:1] == ["human"]
    # In human papers "P1"/"P2" are patient identifiers and "E2" is oestradiol, never ages.
    E = [] if human else (d.get("E") or [])
    P = [] if human else (d.get("P") or [])
    if E:
        lits.append("E%g" % E[0] if len(E) == 1 else "E%g-E%g" % (E[0], E[-1]))
        vocab.append("fetal")
    if P:
        lits.append("P%d" % P[0] if len(P) == 1 else "P%d-P%d" % (P[0], P[-1]))
        if any(x <= 7 for x in P):
            vocab.append("neonatal")
        if any(8 <= x <= 28 for x in P):
            vocab.append("juvenile")
        if any(x > 28 for x in P):
            vocab.append("adult")
    dy = [n[0] for n in (d.get("nums") or []) if n[2] == "day"]
    wk = [n[0] for n in (d.get("nums") or []) if n[2] == "week"]
    mo = [n[0] for n in (d.get("nums") or []) if n[2] == "month"]
    yr = [n[0] for n in (d.get("nums") or []) if n[2] == "year"]
    raw = d.get("num_raw") or []
    if raw:
        lits.append("/".join(raw[:3]))
    if human:
        if yr:
            if min(yr) < 2:
                vocab.append("infant")
            if any(2 <= x < 10 for x in yr):
                vocab.append("childhood")
            if any(10 <= x < 18 for x in yr):
                vocab.append("pubertal")
            if any(x >= 18 for x in yr):
                vocab.append("adult")
        if mo:
            vocab.append("infant")
    else:
        if dy:
            if min(dy) <= 7:
                vocab.append("neonatal")
            if any(8 <= x <= 28 for x in dy):
                vocab.append("juvenile")
            if any(x > 28 for x in dy):
                vocab.append("adult")
        if wk:
            if min(wk) <= 3:
                vocab.append("juvenile")
            if any(4 <= x <= 7 for x in wk):
                vocab.append("peripubertal")
            if any(x >= 8 for x in wk):
                vocab.append("adult")
        if mo or yr:
            vocab.append("adult")
    for a, u in (d.get("age_mean") or []):
        lits.append("mean age %g %s" % (a, u))
        if u.startswith("year"):
            vocab.append("infant" if a < 2 else "childhood" if a < 10 else "pubertal" if a < 18 else "adult")
        else:
            vocab.append("infant")
    # Word evidence ("adult mice", "children") is only used when the source gives no
    # explicit age at all - otherwise a stray "immature" in the discussion would add a
    # stage the experiment never used.
    if not vocab:
        aw = d.get("age_words") or {}
        mxw = max(aw.values()) if aw else 0
        for k, n in aw.items():
            if n >= max(2, 0.25 * mxw):
                vocab.append({"fetal": "fetal", "neonatal": "neonatal", "child": "juvenile",
                              "pubertal": "pubertal", "adult": "adult"}[k])
    seen, vv = set(), []
    for v in vocab:
        if v not in seen:
            seen.add(v); vv.append(v)
    return ("; ".join(lits[:3]) if lits else None), vv


def ref_zones(d, thresh=3):
    z = d.get("zone") or {}
    if not z:
        return []
    mx = max(z.values())
    return [k for k in ZORD if z.get(k, 0) >= thresh and z.get(k, 0) >= 0.2 * mx]


STAGE_ORDER = ["fetal", "neonatal", "infant", "juvenile", "childhood", "prepubertal",
               "peripubertal", "pubertal", "adult"]


def build(edge):
    old = str(edge.get("context") or "").strip().rstrip(";,. ")
    have = {ax: classify(old, ax, None) == "MATCH" for ax in AXES}
    # Reviews/meta-analyses describe other people's experiments; their species, zone and
    # age words are not this edge's experimental context.
    caps = [dos[r] for r in (edge.get("refs") or []) if r in dos
            and dos[r].get("type") not in REVIEW_TYPES]
    caps_sex = [dos[r] for r in (edge.get("refs") or []) if r in dos]
    src_kinds = {c["src"] for c in caps}
    parts, prov = [], {}

    # ---- species
    if not have["species"] and "no species" not in old.lower():
        sp = []
        for c in caps:
            for s in ref_species(c):
                if s not in sp:
                    sp.append(s)
        if sp:
            parts.append(" and ".join(SPTXT[s] for s in sp[:3]))
            prov["species"] = "determined"
        else:
            parts.append("species unknown")
            prov["species"] = "unknown"

    # ---- zone
    if not have["zone"]:
        zdef = [ZN[n] for n in (edge["source"], edge["target"]) if n in ZN]
        if zdef:
            zs = [z for z in ZORD if z in zdef]
            parts.append(" and ".join(ZTXT[z] for z in zs) if len(zs) == 1
                         else " and ".join(ZTXT[z].replace(" zone", "") for z in zs) + " zones")
            prov["zone"] = "definitional"
        else:
            # Only carry a node's zonal localization onto the edge when BOTH endpoints
            # actually live in the growth plate; otherwise a systemic or epidemiological
            # edge would inherit a zone it was never measured in.
            GP_LAYERS = {"L1_growth_plate_architecture", "L2_stem_and_progenitor_biology",
                         "L3_signaling_networks", "L5_matrix_and_mineralization",
                         "L6_mechanobiology", "L7_fusion_and_cessation"}

            def resident(n):
                return n in NODEZ or n2l.get(n) in GP_LAYERS
            both_resident = resident(edge["source"]) and resident(edge["target"])
            zs_src = NODEZ.get(edge["source"], []) if both_resident else []
            zs_tgt = NODEZ.get(edge["target"], []) if both_resident else []
            inter = [z for z in ZORD if z in zs_src and z in zs_tgt]
            union = [z for z in ZORD if z in zs_src or z in zs_tgt]
            zn = inter or union
            zr = []
            for c in caps:
                for z in ref_zones(c):
                    if z not in zr:
                        zr.append(z)
            zr = [z for z in ZORD if z in zr]
            if zn:
                parts.append(("%s (zonal localization of the interacting nodes, per their "
                              "localization records)") % ", ".join(ZTXT[z] for z in zn))
                prov["zone"] = "node_localization"
            elif zr:
                parts.append("zones resolved in source: " + ", ".join(ZTXT[z] for z in zr))
                prov["zone"] = "from_source"
            else:
                lay = {n2l.get(edge["source"], "?"), n2l.get(edge["target"], "?")}
                if lay and lay <= ORGANISM_LAYERS:
                    parts.append("zone unknown (organism-level readout, no zonal resolution)")
                else:
                    parts.append("zone unknown (not reported)")
                prov["zone"] = "unknown"

    # ---- sex
    if not have["sex"]:
        sxs = {c["sex_final"] for c in caps_sex if c["sex_final"]}
        nrep = sum(1 for c in caps_sex if c["sex_final"])
        qual = "" if nrep == len(caps_sex) else " (sex reported in %d of %d sources)" % (nrep, len(caps_sex))
        if "both" in sxs or sxs == {"male", "female"}:
            parts.append("both sexes (male and female)" + qual)
            prov["sex"] = "determined"
        elif sxs == {"male"}:
            parts.append("male only" + qual)
            prov["sex"] = "determined"
        elif sxs == {"female"}:
            parts.append("female only" + qual)
            prov["sex"] = "determined"
        else:
            parts.append("sex unknown (not reported in source)")
            prov["sex"] = "unknown"

    # ---- stage
    if not have["stage"]:
        lits, vocab = [], []
        for c in caps:
            l, v = ref_stage(c)
            if l:
                lits.append(l)
            for x in v:
                if x not in vocab:
                    vocab.append(x)
        vocab = [v for v in STAGE_ORDER if v in vocab]
        if vocab:
            s = ", ".join(vocab)
            if lits:
                s += " (" + "; ".join(lits[:2])[:70] + ")"
            parts.append(s)
            prov["stage"] = "determined"
        else:
            parts.append("age/stage unknown (not reported)")
            prov["stage"] = "unknown"

    new = old + ("; " if parts else "") + ", ".join(parts)
    return new, prov, sorted(src_kinds)


if __name__ == "__main__":
    import yaml
    edges = yaml.safe_load(open("/home/user/growth-plate/atlas/edges/edges.yaml"))["edges"]
    stats = collections.defaultdict(collections.Counter)
    out = {}
    for e in edges:
        new, prov, sk = build(e)
        out[e["edge_id"]] = new
        for ax, v in prov.items():
            stats[ax][v] += 1
    json.dump(out, open(SP + "/newctx.json", "w"), indent=0)
    for ax in ("zone", "sex", "stage", "species"):
        print(ax, dict(stats[ax]))
    # projected coverage
    proj = collections.Counter()
    for e in edges:
        c = out[e["edge_id"]]
        for ax in AXES:
            if classify(c, ax, None) == "MATCH":
                proj[ax] += 1
    n = len(edges)
    print("\nPROJECTED COVERAGE")
    for ax in AXES:
        print("  %-8s %4d/%d = %.1f%%" % (ax, proj[ax], n, 100 * proj[ax] / n))
