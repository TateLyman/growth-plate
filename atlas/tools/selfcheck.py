import yaml, glob, os, sys
ROOT='atlas'
vocab=yaml.safe_load(open(ROOT+'/schema/vocab.yaml'))
bib=yaml.safe_load(open(ROOT+'/sources/bibliography.yaml'))['refs']
shard=yaml.safe_load(open(ROOT+'/sources/shards/l5matrix.yaml'))['refs']
known=set(bib)|set(shard)
gaps=yaml.safe_load(open(ROOT+'/gaps/shards/l5matrix.gaps.yaml'))['gaps']
searches=yaml.safe_load(open(ROOT+'/gaps/shards/l5matrix.search.yaml'))['searches']
edges=yaml.safe_load(open(ROOT+'/edges/shards/l5matrix.edges.yaml'))['edges']
gapids={g['gap_id'] for g in gaps}
logged={s['gap_id'] for s in searches}
allnodes={os.path.splitext(os.path.basename(p))[0] for p in glob.glob(ROOT+'/nodes/**/*.yaml',recursive=True)}
errs=[]
REQ_ALWAYS=["id","name","type","layer","human_evidence","last_verified"]
REQ_FULL=["summary","human_evidence_note","species_basis","translation_risk","translation_risk_reason","confidence","key_refs"]
nfiles=sorted(glob.glob(ROOT+'/nodes/L5_matrix_and_mineralization/*.yaml'))
for p in nfiles:
    n=yaml.safe_load(open(p)); rel=p
    stem=os.path.splitext(os.path.basename(p))[0]
    if n.get('id')!=stem: errs.append(f"{rel}: id mismatch")
    for f in REQ_ALWAYS+ (REQ_FULL if not n.get('stub') else []):
        if not n.get(f): errs.append(f"{rel}: missing {f}")
    if n.get('type') not in vocab['node_types']: errs.append(f"{rel}: bad type {n.get('type')}")
    if n.get('layer')!='L5': errs.append(f"{rel}: bad layer")
    if n.get('human_evidence') not in vocab['human_evidence']: errs.append(f"{rel}: bad human_evidence")
    if not n.get('stub'):
        if n.get('confidence') not in vocab['confidence']: errs.append(f"{rel}: bad confidence")
        if n.get('translation_risk') not in vocab['translation_risk']: errs.append(f"{rel}: bad translation_risk")
    for kr in n.get('key_refs') or []:
        if kr.get('ref_id') not in known: errs.append(f"{rel}: key_ref {kr.get('ref_id')} unknown")
        if kr.get('type') and kr['type'] not in vocab['ref_types']: errs.append(f"{rel}: bad ref type {kr.get('type')}")
        if not kr.get('one_line_finding'): errs.append(f"{rel}: key_ref {kr.get('ref_id')} no finding")
    for q in n.get('quantitative') or []:
        for f in ['parameter','value','unit','species','source_ref']:
            if q.get(f) in (None,''): errs.append(f"{rel}: quant '{q.get('parameter')}' missing {f}")
        if q.get('source_ref') not in known: errs.append(f"{rel}: quant cites unknown ref {q.get('source_ref')}")
        if q.get('species') not in vocab['species']: errs.append(f"{rel}: quant bad species {q.get('species')}")
    for g in n.get('open_questions') or []:
        if g not in gapids: errs.append(f"{rel}: unknown gap {g}")
GAP_REQ=["gap_id","question","type","layer","why_it_matters","what_is_known","what_is_missing","discriminating_experiment"]
for g in gaps:
    for f in GAP_REQ:
        if not g.get(f): errs.append(f"gap {g.get('gap_id')}: missing {f}")
    if g['type'] not in vocab['gap_types']: errs.append(f"gap {g['gap_id']}: bad type")
    if g['layer']!='L5': errs.append(f"gap {g['gap_id']}: bad layer")
    for r in g.get('nearest_evidence') or []:
        if r not in known: errs.append(f"gap {g['gap_id']}: nearest_evidence unknown ref {r}")
    if g['type']=='search_established' and g['gap_id'] not in logged:
        errs.append(f"gap {g['gap_id']}: search_established without search log")
for s in searches:
    for f in ["gap_id","database","exact_query_string","date_run","hit_count"]:
        if s.get(f) is None: errs.append(f"search {s.get('gap_id')}: missing {f}")
EDGE_REQ=["edge_id","source","target","relation","context","evidence_tier","refs","confidence"]
for e in edges:
    for f in EDGE_REQ:
        if e.get(f) in (None,'',[]): errs.append(f"edge {e.get('edge_id')}: missing {f}")
    if e['source'] not in allnodes: errs.append(f"edge {e['edge_id']}: source {e['source']} missing")
    if e['target'] not in allnodes: errs.append(f"edge {e['edge_id']}: target {e['target']} missing")
    if e['relation'] not in vocab['relations']: errs.append(f"edge {e['edge_id']}: bad relation")
    if e.get('sign') is not None and str(e['sign']) not in [str(x) for x in vocab['signs']]: errs.append(f"edge {e['edge_id']}: bad sign {e.get('sign')}")
    if e['confidence'] not in vocab['confidence']: errs.append(f"edge {e['edge_id']}: bad confidence")
    if e['evidence_tier'] not in vocab['evidence_tier']: errs.append(f"edge {e['edge_id']}: bad tier")
    for r in e['refs']:
        if r not in known: errs.append(f"edge {e['edge_id']}: unknown ref {r}")
    if e['relation']=='hypothesized_link' and e['confidence']!='speculative': errs.append(f"edge {e['edge_id']}: hypothesized_link needs speculative")
    if (e['relation']=='hypothesized_link' or e['confidence']=='speculative'):
        if e.get('gap_id') not in gapids: errs.append(f"edge {e['edge_id']}: missing/unknown gap_id")
hard=[g for g in gaps if g['type'] in ('search_established','quantitative_gap')]
print(f"nodes={len(nfiles)} gaps={len(gaps)} (hard={len(hard)}) searches={len(searches)} edges={len(edges)} shard_refs={len(shard)}")
print("ERRORS:", len(errs))
for e in errs: print("  X", e)
