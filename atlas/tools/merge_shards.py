#!/usr/bin/env python3
"""
Merge parallel-subagent shards into the canonical atlas files.

Subagents never write to bibliography.yaml / gaps.yaml / edges.yaml directly -
concurrent writes would silently lose entries. Each writes its own shard:

  sources/shards/<topic>.yaml        -> sources/bibliography.yaml   (refs)
  gaps/shards/<topic>.gaps.yaml      -> gaps/gaps.yaml              (gaps)
  gaps/shards/<topic>.search.yaml    -> gaps/search_log.yaml        (searches)
  edges/shards/<topic>.edges.yaml    -> edges/edges.yaml            (edges)

Merge rules:
  refs   - de-duped on pmid, then doi, then ref_id. Colliding ref_ids for
           DIFFERENT papers are renamed and a rewrite map is emitted, then
           applied across node/edge/gap files so no citation is left dangling.
  gaps   - de-duped on gap_id; collisions are renamed and rewritten likewise.
  edges  - edge_ids are reassigned sequentially (e00001...) since shards each
           number from 1; the rewrite is applied to gap/edge cross-references.
  all    - append-only semantics: nothing already canonical is removed.

Usage:
  python3 atlas/tools/merge_shards.py            # merge everything, report
  python3 atlas/tools/merge_shards.py --dry-run
  python3 atlas/tools/merge_shards.py --archive  # move merged shards aside
"""
import os, sys, glob, argparse, shutil, re
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(p, d=None):
    if not os.path.exists(p):
        return d
    with open(p) as f:
        return yaml.safe_load(f) or d


def dump(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        yaml.safe_dump(obj, f, sort_keys=False, default_flow_style=False,
                       width=120, allow_unicode=True)


def merge_refs(dry):
    canon_p = os.path.join(ROOT, "sources", "bibliography.yaml")
    canon = load(canon_p, {"refs": {}})
    canon.setdefault("refs", {})
    refs = canon["refs"]
    by_pmid = {str(v.get("pmid")): k for k, v in refs.items() if v.get("pmid")}
    by_doi = {v.get("doi"): k for k, v in refs.items() if v.get("doi")}
    rewrite, added, dup = {}, 0, 0

    for sp in sorted(glob.glob(os.path.join(ROOT, "sources", "shards", "*.yaml"))):
        shard = load(sp, {}) or {}
        for rid, rv in (shard.get("refs") or {}).items():
            if not isinstance(rv, dict):
                continue
            pm, doi = str(rv.get("pmid") or ""), rv.get("doi")
            hit = by_pmid.get(pm) if pm else None
            if not hit and doi:
                hit = by_doi.get(doi)
            if hit:
                if hit != rid:
                    rewrite[rid] = hit
                dup += 1
                # enrich canonical entry with any extra fields the shard learned
                for k, v in rv.items():
                    if k not in refs[hit] or refs[hit][k] in (None, "", []):
                        refs[hit][k] = v
                continue
            new_id = rid
            if new_id in refs:                       # same id, different paper
                n = 2
                while f"{rid}_{n}" in refs:
                    n += 1
                new_id = f"{rid}_{n}"
                rewrite[rid] = new_id
            rv["ref_id"] = new_id
            refs[new_id] = rv
            if pm:
                by_pmid[pm] = new_id
            if doi:
                by_doi[doi] = new_id
            added += 1

    if not dry:
        dump(canon_p, canon)
    return added, dup, rewrite, len(refs)


def merge_listfile(pattern, canon_rel, key, id_field, dry, renumber=False, prefix="e"):
    canon_p = os.path.join(ROOT, canon_rel)
    canon = load(canon_p, {key: []})
    canon.setdefault(key, [])
    items = canon[key]
    have = {i.get(id_field) for i in items if isinstance(i, dict)}
    rewrite, added = {}, 0

    for sp in sorted(glob.glob(os.path.join(ROOT, pattern))):
        shard = load(sp, {}) or {}
        for it in (shard.get(key) or []):
            if not isinstance(it, dict):
                continue
            iid = it.get(id_field)
            if renumber:
                new = f"{prefix}{len(items) + 1:05d}"
                if iid and iid != new:
                    rewrite[f"{os.path.basename(sp)}::{iid}"] = new
                it[id_field] = new
                items.append(it); added += 1; continue
            if iid in have:
                n = 2
                while f"{iid}_{n}" in have:
                    n += 1
                rewrite[iid] = f"{iid}_{n}"
                it[id_field] = f"{iid}_{n}"
                iid = it[id_field]
            have.add(iid)
            items.append(it); added += 1

    if not dry:
        dump(canon_p, canon)
    return added, rewrite, len(items)


def apply_rewrites(mapping, dry):
    """Rewrite ref_id / gap_id references across all node, edge and gap files."""
    if not mapping:
        return 0
    targets = (glob.glob(os.path.join(ROOT, "nodes", "**", "*.yaml"), recursive=True)
               + [os.path.join(ROOT, "edges", "edges.yaml"),
                  os.path.join(ROOT, "gaps", "gaps.yaml"),
                  os.path.join(ROOT, "gaps", "search_log.yaml")])
    changed = 0
    for p in targets:
        if not os.path.exists(p):
            continue
        txt = open(p).read()
        new = txt
        for old, nw in mapping.items():
            old = old.split("::")[-1]
            new = re.sub(rf"(?<![\w-]){re.escape(old)}(?![\w-])", nw, new)
        if new != txt:
            changed += 1
            if not dry:
                open(p, "w").write(new)
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--archive", action="store_true")
    a = ap.parse_args()
    dry = a.dry_run

    r_add, r_dup, r_rw, r_tot = merge_refs(dry)
    g_add, g_rw, g_tot = merge_listfile("gaps/shards/*.gaps.yaml",
                                        "gaps/gaps.yaml", "gaps", "gap_id", dry)
    s_add, _, s_tot = merge_listfile("gaps/shards/*.search.yaml",
                                     "gaps/search_log.yaml", "searches", "gap_id", dry)
    e_add, e_rw, e_tot = merge_listfile("edges/shards/*.edges.yaml",
                                        "edges/edges.yaml", "edges", "edge_id", dry,
                                        renumber=True)

    rw = {}
    rw.update(r_rw); rw.update(g_rw)
    touched = apply_rewrites(rw, dry)

    print(f"refs    +{r_add} new, {r_dup} already present  -> {r_tot} total")
    print(f"gaps    +{g_add}                               -> {g_tot} total")
    print(f"search  +{s_add}                               -> {s_tot} total")
    print(f"edges   +{e_add} (renumbered)                  -> {e_tot} total")
    if rw:
        print(f"id collisions rewritten: {len(rw)}; files touched: {touched}")
        for k, v in list(rw.items())[:10]:
            print(f"   {k} -> {v}")
    if dry:
        print("\n[dry run - nothing written]")
    elif a.archive:
        arch = os.path.join(ROOT, "sources", "shards", "_merged")
        for pat in ["sources/shards/*.yaml", "gaps/shards/*.yaml", "edges/shards/*.yaml"]:
            for sp in glob.glob(os.path.join(ROOT, pat)):
                if "_merged" in sp:
                    continue
                d = os.path.join(arch, os.path.basename(os.path.dirname(sp)))
                os.makedirs(d, exist_ok=True)
                shutil.move(sp, os.path.join(d, os.path.basename(sp)))
        print(f"shards archived to {arch}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
