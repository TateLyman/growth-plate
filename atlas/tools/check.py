import yaml, glob, os, sys
R="/home/user/growth-plate/atlas"
def L(p,d=None):
    return (yaml.safe_load(open(p)) if os.path.exists(p) else d) or d
vocab=L(f"{R}/schema/vocab.yaml")
bib=L(f"{R}/sources/bibliography.yaml",{}).get("refs",{})
shard=L(f"{R}/sources/shards/l7fuse.yaml",{}).get("refs",{})
refs=set(bib)|set(shard)
nodes={}
for p in glob.glob(f"{R}/nodes/**/*.yaml",recursive=True):
    n=yaml.safe_load(open(p)); nodes[n["id"]]=n
gaps=L(f"{R}/gaps/shards/l7fuse.gaps.yaml",{}).get("gaps",[])
searches=L(f"{R}/gaps/shards/l7fuse.search.yaml",{}).get("searches",[])
edges=L(f"{R}/edges/shards/l7fuse.edges.yaml",{}).get("edges",[])
gapids={g["gap_id"] for g in gaps}
logged={s["gap_id"] for s in searches}
err=[]
REQ=["id","name","type","layer","human_evidence","last_verified"]
REQF=["summary","human_evidence_note","species_basis","translation_risk","translation_risk_reason","confidence","key_refs"]
for p in sorted(glob.glob(f"{R}/nodes/L7_fusion_and_cessation/*.yaml")):
    n=yaml.safe_load(open(p)); w=os.path.basename(p)
    if n["id"]!=os.path.splitext(w)[0]: err.append(f"{w}: id mismatch")
    for f in REQ+REQF:
        if not n.get(f): err.append(f"{w}: missing {f}")
    if n["type"] not in vocab["node_types"]: err.append(f"{w}: bad type {n['type']}")
    if n["human_evidence"] not in vocab["human_evidence"]: err.append(f"{w}: bad human_evidence")
    if n["translation_risk"] not in vocab["translation_risk"]: err.append(f"{w}: bad translation_risk")
    if n["confidence"] not in vocab["confidence"]: err.append(f"{w}: bad confidence")
    for kr in n.get("key_refs") or []:
        if kr.get("ref_id") not in refs: err.append(f"{w}: unknown ref {kr.get('ref_id')}")
        if kr.get("type") and kr["type"] not in vocab["ref_types"]: err.append(f"{w}: bad ref type {kr['type']}")
        if not kr.get("one_line_finding"): err.append(f"{w}: ref {kr.get('ref_id')} no finding")
    for q in n.get("quantitative") or []:
        for f in ["parameter","value","unit","species","source_ref"]:
            if q.get(f) in (None,""): err.append(f"{w}: quant '{q.get('parameter')}' missing {f}")
        if q.get("species") and q["species"] not in vocab["species"]: err.append(f"{w}: quant bad species {q.get('species')}")
        if q.get("source_ref") and q["source_ref"] not in refs: err.append(f"{w}: quant unknown ref {q.get('source_ref')}")
    for g in n.get("open_questions") or []:
        if g not in gapids: err.append(f"{w}: unknown gap {g}")
    if n.get("pending_source") and n["pending_source"] not in refs: err.append(f"{w}: bad pending_source")
GREQ=["gap_id","question","type","layer","why_it_matters","what_is_known","what_is_missing","discriminating_experiment"]
for g in gaps:
    for f in GREQ:
        if not g.get(f): err.append(f"gap {g.get('gap_id')}: missing {f}")
    if g["type"] not in vocab["gap_types"]: err.append(f"gap {g['gap_id']}: bad type")
    if g["layer"] not in vocab["layers"]: err.append(f"gap {g['gap_id']}: bad layer")
    for r in g.get("nearest_evidence") or []:
        if r not in refs: err.append(f"gap {g['gap_id']}: nearest_evidence unknown ref {r}")
    if g["type"]=="search_established" and g["gap_id"] not in logged:
        err.append(f"gap {g['gap_id']}: search_established without log")
for s in searches:
    for f in ["gap_id","database","exact_query_string","date_run","hit_count"]:
        if s.get(f) is None: err.append(f"search {s.get('gap_id')}: missing {f}")
EREQ=["edge_id","source","target","relation","context","evidence_tier","refs","confidence"]
seen=set()
for e in edges:
    eid=e.get("edge_id")
    if eid in seen: err.append(f"edge {eid}: dup")
    seen.add(eid)
    for f in EREQ:
        if e.get(f) in (None,"",[]): err.append(f"edge {eid}: missing {f}")
    if e["source"] not in nodes: err.append(f"edge {eid}: source {e['source']} missing")
    if e["target"] not in nodes: err.append(f"edge {eid}: target {e['target']} missing")
    if e["relation"] not in vocab["relations"]: err.append(f"edge {eid}: bad relation")
    if e.get("sign") is not None and str(e["sign"]) not in [str(x) for x in vocab["signs"]]: err.append(f"edge {eid}: bad sign {e.get('sign')}")
    if e["confidence"] not in vocab["confidence"]: err.append(f"edge {eid}: bad confidence")
    if e["evidence_tier"] not in vocab["evidence_tier"]: err.append(f"edge {eid}: bad tier")
    for r in e.get("refs") or []:
        if r not in refs: err.append(f"edge {eid}: unknown ref {r}")
    needs = e["relation"]=="hypothesized_link" or e["confidence"]=="speculative"
    if needs:
        if not e.get("gap_id"): err.append(f"edge {eid}: needs gap_id")
        elif e["gap_id"] not in gapids: err.append(f"edge {eid}: bad gap_id")
    if e["relation"]=="hypothesized_link" and e["confidence"]!="speculative":
        err.append(f"edge {eid}: hypothesized_link must be speculative")
hard=[g for g in gaps if g["type"] in ("search_established","quantitative_gap")]
print(f"L7 nodes={len(glob.glob(f'{R}/nodes/L7_fusion_and_cessation/*.yaml'))} edges={len(edges)} gaps={len(gaps)} hard={len(hard)} searches={len(searches)} refs_in_shard={len(shard)}")
print("ERRORS:", len(err))
for e in err: print("  x",e)
