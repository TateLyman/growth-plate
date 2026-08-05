#!/usr/bin/env python3
"""
Regenerate the coverage dashboard in README.md from the repository itself.
Counts are real; nothing here is hand-written. Run after every layer sweep.
"""
import os, sys, glob, re
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)
README = os.path.join(REPO, "README.md")


def load(p, d=None):
    if not os.path.exists(p):
        return d
    with open(p) as f:
        return yaml.safe_load(f) or d


def main():
    vocab = load(os.path.join(ROOT, "schema", "vocab.yaml"))
    layers = vocab["layers"]

    nodes = {}
    for p in glob.glob(os.path.join(ROOT, "nodes", "**", "*.yaml"), recursive=True):
        n = load(p)
        if isinstance(n, dict) and n.get("id"):
            nodes[n["id"]] = n

    edges = (load(os.path.join(ROOT, "edges", "edges.yaml"), {}) or {}).get("edges", [])
    gaps = (load(os.path.join(ROOT, "gaps", "gaps.yaml"), {}) or {}).get("gaps", [])
    slogs = (load(os.path.join(ROOT, "gaps", "search_log.yaml"), {}) or {}).get("searches", [])
    refs = (load(os.path.join(ROOT, "sources", "bibliography.yaml"), {}) or {}).get("refs", {})

    # per-layer tallies
    rows, tot = [], {"n": 0, "f": 0, "e": 0, "g": 0}
    edge_layer = {}
    for e in edges:
        src = nodes.get(e.get("source"), {})
        L = src.get("layer")
        edge_layer[L] = edge_layer.get(L, 0) + 1

    for L in sorted(layers, key=lambda x: int(x[1:])):
        ln = [n for n in nodes.values() if n.get("layer") == L]
        full = [n for n in ln if not n.get("stub")]
        lg = [g for g in gaps if g.get("layer") == L]
        hard = [g for g in lg if g.get("type") in ("search_established", "quantitative_gap")]
        le = edge_layer.get(L, 0)
        doc = os.path.join(ROOT, "docs", f"{L}_{layers[L]}.md")
        has_doc = "✅" if os.path.exists(doc) else "—"
        fig = glob.glob(os.path.join(ROOT, "figures", f"{L}_*.mmd"))
        quota = "✅" if (len(lg) >= 8 and len(hard) >= 3) else f"{len(lg)}/8·{len(hard)}/3"
        rows.append(f"| {L} | {layers[L]} | {len(ln)} | {len(full)} | {le} | "
                    f"{len(lg)} | {quota} | {has_doc} | {'✅' if fig else '—'} |")
        tot["n"] += len(ln); tot["f"] += len(full); tot["e"] += le; tot["g"] += len(lg)

    conf = {}
    for n in nodes.values():
        if not n.get("stub"):
            conf[n.get("confidence")] = conf.get(n.get("confidence"), 0) + 1
    conf_line = " · ".join(f"**{k}** {conf[k]}" for k in sorted(conf)) or "_none yet_"

    gt = {}
    for g in gaps:
        gt[g.get("type")] = gt.get(g.get("type"), 0) + 1
    gt_line = " · ".join(f"`{k}` {v}" for k, v in sorted(gt.items())) or "_none yet_"

    nq = sum(len(n.get("quantitative") or []) for n in nodes.values())
    csvp = os.path.join(ROOT, "quant", "parameters.csv")
    ncsv = 0
    if os.path.exists(csvp):
        with open(csvp) as f:
            ncsv = max(0, sum(1 for _ in f) - 1)

    # MR-001 item 6: evidence-quality metrics. A falling A-count with rising
    # propositional rigour is a SUCCESSFUL run, so these are tracked instead of
    # treating the A-count as a target.
    researched = [n for n in nodes.values() if not n.get("stub")]
    n_res = len(researched) or 1
    n_direct = sum(1 for n in researched if n.get("human_evidence") == "direct")
    def human_primaries(n):
        c = 0
        for k in (n.get("key_refs") or []):
            if not isinstance(k, dict):
                continue
            t = (k.get("type") or "")
            if t in ("primary", "meta_analysis", "systematic_review",
                     "trial_registry", "regulatory"):
                c += 1
        return c
    n_repl = sum(1 for n in researched
                 if n.get("human_evidence") == "direct" and human_primaries(n) >= 2)
    hef = 100.0 * n_direct / n_res
    rhf = 100.0 * n_repl / n_res
    per_layer_ev = {}
    for L in sorted(layers, key=lambda x: int(x[1:])):
        ln = [n for n in researched if n.get("layer") == L]
        if not ln:
            continue
        d = sum(1 for n in ln if n.get("human_evidence") == "direct")
        r = sum(1 for n in ln if n.get("human_evidence") == "direct"
                and human_primaries(n) >= 2)
        per_layer_ev[L] = (len(ln), d, r)
    ev_rows = "\n".join(
        f"| {L} | {t} | {d} ({100.0*d/t:.0f}%) | {r} ({100.0*r/t:.0f}%) |"
        for L, (t, d, r) in per_layer_ev.items())

    n_edges_per_node = len(edges) / (len(nodes) or 1)
    all_refs_cited = set()
    for n in researched:
        for k in (n.get("key_refs") or []):
            if isinstance(k, dict) and k.get("ref_id"):
                all_refs_cited.add(k["ref_id"])
    refs_per_res = sum(len(n.get("key_refs") or []) for n in researched) / n_res
    quant_cov = 100.0 * sum(1 for n in researched if n.get("quantitative")) / n_res

    vr = load(os.path.join(ROOT, "sources", "verification_report.yaml"), {}) or {}
    vc = vr.get("counts", {})
    vline = (f"{vc.get('ok',0)} verified · {vc.get('mismatch',0)} mismatched · "
             f"{vc.get('unresolved',0)} unresolved · {vc.get('no_identifier',0)} manual"
             if vc else "_not yet run_")

    targets = {"nodes": 1200, "edges": 2500, "gaps": 150}
    def bar(v, t):
        pct = min(100, int(100 * v / t))
        return f"{'█' * (pct // 5)}{'░' * (20 - pct // 5)} {v}/{t} ({pct}%)"

    md = f"""**Totals** — {tot['n']} nodes ({tot['f']} researched, {tot['n']-tot['f']} stubs) ·
{len(edges)} edges · {len(gaps)} gaps ({len(slogs)} search logs) · {len(refs)} references

```
nodes  {bar(tot['n'], targets['nodes'])}
edges  {bar(len(edges), targets['edges'])}
gaps   {bar(len(gaps), targets['gaps'])}
```

| Layer | Name | Nodes | Researched | Edges out | Gaps | Quota | Doc | Fig |
|---|---|---:|---:|---:|---:|:--:|:--:|:--:|
{chr(10).join(rows)}
| | **total** | **{tot['n']}** | **{tot['f']}** | **{len(edges)}** | **{tot['g']}** | | | |

**Confidence distribution** (researched nodes): {conf_line}

**Gap types**: {gt_line}

**Quantitative**: {nq} values on nodes · {ncsv} rows in `quant/parameters.csv`

**Reference verification** (`tools/verify_refs.py`): {vline}

### Evidence quality

These are tracked instead of treating the A-grade count as a target. Direct,
replicated human evidence in growth-plate biology is genuinely scarce; a falling
A-count alongside rising propositional rigour is a successful run, not a shortfall.

| metric | value | target |
|---|---:|---:|
| `human_evidence_fraction` — researched nodes with `human_evidence: direct` | **{hef:.1f}%** | — |
| `replicated_human_fraction` — direct human evidence **and** ≥2 human primaries | **{rhf:.1f}%** | — |
| `edges_per_node` | **{n_edges_per_node:.2f}** | ≥3.0 |
| `refs_per_researched` | **{refs_per_res:.2f}** | ≥3.0 |
| `quant_node_coverage` | **{quant_cov:.1f}%** | ≥60% |
| `stub_fraction` | **{100.0*(tot['n']-tot['f'])/(tot['n'] or 1):.1f}%** | 0% |

| Layer | researched | human_evidence: direct | replicated human |
|---|---:|---:|---:|
{ev_rows}

_Quota column: ≥8 gaps per layer, ≥3 of which are `search_established` or
`quantitative_gap`. Generated by `atlas/tools/dashboard.py`._"""

    with open(README) as f:
        txt = f.read()
    new = re.sub(r"<!-- DASHBOARD:BEGIN -->.*?<!-- DASHBOARD:END -->",
                 "<!-- DASHBOARD:BEGIN -->\n" + md + "\n<!-- DASHBOARD:END -->",
                 txt, flags=re.S)
    with open(README, "w") as f:
        f.write(new)
    print(md)


if __name__ == "__main__":
    sys.exit(main())
