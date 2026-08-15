#!/usr/bin/env python3
"""
enumeration_completeness_check.py
=================================
THE CONTROL FOR THE COVERAGE MAP.

concept_coverage_map.py asks "what does the external enumeration contain that the atlas has
never touched?" and reports the ZEROs. That question is only meaningful if the enumeration is
at least as broad as the atlas. If it is NARROWER, the ZERO list is still true but the whole
exercise is measuring the enumeration's blind spots rather than the atlas's.

So this runs the contrast in the OTHER direction:

    ATLAS_VOCABULARY  minus  REGISTRY_VOCABULARY
      = every gene symbol the atlas works with that no external domain agent surfaced.

READ IT AS A CONTROL, NOT A FINDING
    * A small, boring residual (obscure one-off symbols, dataset accessions, typos) means the
      enumeration achieved coverage and the ZERO list can be trusted.
    * A large residual containing genes the atlas reasons about repeatedly means the
      enumeration is narrower than the atlas and the ZERO list understates the true gap - the
      right response is more enumeration, not more triage.

This is CORR-311's rule applied to a screen instead of a contrast: the negative control is
rows you already have. Without it a partition is a list; with it, it is a result.

WHY GENE SYMBOLS AND NOT CONCEPTS
    Concepts are prose and cannot be set-differenced. Gene symbols are the one vocabulary both
    sides share, and they are the unit almost every enumeration row carries. The cost is that
    purely non-genetic concepts (a loading regimen, an exposure, a measurement method) are
    invisible to this check - so a clean result here is necessary, not sufficient.

KNOWN COLLISIONS, LEFT IN DELIBERATELY
    A few real gene symbols collide with this project's own jargon: SDS (serine dehydratase
    vs standard deviation score), CPM (carboxypeptidase M vs counts per million), WAS
    (Wiskott-Aldrich vs the verb). They are genuinely in the gene vocabulary, so filtering
    them out by hand would be special-pleading against the authoritative list. Read the top
    of the residual with that in mind; it is three rows, not a systematic error.

USAGE
    python3 atlas/tools/enumeration_completeness_check.py
    python3 atlas/tools/enumeration_completeness_check.py --min-mentions 5 --json out.json
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("pyyaml required", file=sys.stderr)
    raise

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(HERE)
NODES = os.path.join(HERE, "nodes")
GAPS = os.path.join(HERE, "gaps", "gaps.yaml")
LEDGER = os.path.join(ROOT, "CLAUDE.md")
REGISTRY = os.path.join(HERE, "concepts", "concept_registry.yaml")

GENEISH = re.compile(r"^[A-Z][A-Z0-9]{1,9}[0-9A-Z]$")
GENE_NAMES = os.path.join(HERE, "data", "round344", "gse288028_gene_names.json")

# A stoplist cannot work here. CLAUDE.md is written in an emphatic all-caps style, so ROUND,
# GROWTH, LENGTH, PLATE and several hundred other ordinary English words pass any shape test.
# The authoritative filter is the real human gene vocabulary: the 36,601 symbols in the
# postnatal growth-plate expression matrix. A token counts as a gene only if it is one.
_REAL: set | None = None


def real_genes() -> set:
    global _REAL
    if _REAL is None:
        try:
            g = json.load(open(GENE_NAMES))
            if isinstance(g, dict):
                g = g.get("genes", g.get("gene_names")) or []
            _REAL = {str(x).upper() for x in g}
        except OSError:
            _REAL = set()
    return _REAL


def slurp(p: str) -> str:
    try:
        return open(p, encoding="utf-8", errors="ignore").read()
    except OSError:
        return ""


def atlas_blob() -> str:
    parts = []
    for root, _dirs, files in os.walk(NODES):
        for fn in files:
            if fn.endswith(".yaml"):
                parts.append(slurp(os.path.join(root, fn)))
    parts.append(slurp(GAPS))
    parts.append(slurp(LEDGER))
    return "\n".join(parts)


def symbols_in(text: str) -> collections.Counter:
    toks = re.findall(r"\b[A-Za-z][A-Za-z0-9]{2,10}\b", text)
    c = collections.Counter()
    for t in toks:
        if t != t.upper():          # require the token to be written in caps in the source
            continue
        u = t.upper()
        if not GENEISH.match(u) or u not in real_genes():
            continue
        c[u] += 1
    return c


def registry_symbols(path: str) -> set:
    doc = yaml.safe_load(slurp(path)) or {}
    out = set()
    for c in doc.get("concepts") or []:
        for a in [c.get("concept", "")] + list(c.get("aliases") or []):
            for tok in re.split(r"[^A-Za-z0-9]+", str(a)):
                u = tok.upper()
                if GENEISH.match(u) and u in real_genes():
                    out.add(u)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", default=REGISTRY)
    ap.add_argument("--min-mentions", type=int, default=3,
                    help="a symbol the atlas mentions this often is one it actually works with")
    ap.add_argument("--json")
    args = ap.parse_args()

    if not os.path.exists(args.registry):
        print("no registry - run build_concept_registry.py first", file=sys.stderr)
        sys.exit(1)

    atlas = symbols_in(atlas_blob())
    reg = registry_symbols(args.registry)

    worked = {s: n for s, n in atlas.items() if n >= args.min_mentions}
    missed = sorted(((n, s) for s, n in worked.items() if s not in reg), reverse=True)
    covered = len(worked) - len(missed)

    print("ENUMERATION COMPLETENESS CHECK  (the control, not the finding)")
    print("  atlas GENE symbols (>=%d mentions): %d" % (args.min_mentions, len(worked)))
    print("  present in the registry       : %d (%.1f%%)"
          % (covered, 100.0 * covered / max(1, len(worked))))
    print("  MISSED BY THE ENUMERATION     : %d\n" % len(missed))
    print("  top misses by how hard the atlas works them:")
    for n, s in missed[:60]:
        print("    %-12s %5d mentions" % (s, n))
    if len(missed) > 60:
        print("    ... %d more" % (len(missed) - 60))
    print("\n  READ: a large residual of genes the atlas works hard means the ENUMERATION is")
    print("  narrower than the atlas, and the ZERO list understates the true gap.")

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        json.dump({"n_worked": len(worked), "n_covered": covered,
                   "missed": [{"symbol": s, "atlas_mentions": n} for n, s in missed]},
                  open(args.json, "w"), indent=1)
        print("\n  written: %s" % os.path.relpath(args.json, ROOT))


if __name__ == "__main__":
    main()
