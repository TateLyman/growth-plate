#!/usr/bin/env python3
"""
concept_coverage_map.py
=======================
THE INSTRUMENT THIS ATLAS HAS NEVER HAD.

Every round of this project has been LEAD-DRIVEN: follow a thread, work it, close it,
report a negative. That produces depth and it cannot produce coverage, because you can
only follow a thread you have already thought of. R411 built the blind-spot inventory for
GENES and R431 built ledger_coverage_sweep.py for NODES-vs-CLAUDE.md, but nobody has ever
asked the prior question:

    WHAT IS THE COMPLETE CONCEPT SPACE OF HUMAN GROWTH, AND WHICH PARTS OF IT HAS THIS
    ATLAS NEVER ONCE TOUCHED?

That question cannot be answered from inside the atlas - deriving the concept list from
the node graph is circular and returns exactly what is already there. The list has to come
from OUTSIDE: external enumeration of every system, axis, gene, event, exposure and
modality that touches human stature. This tool scores such an external list against the
atlas and reports the zeros.

INPUT
    A registry at atlas/concepts/concept_registry.yaml with the shape:

        concepts:
          - concept: Lysyl oxidase cross-linking
            domain: matrix
            aliases: [LOX, LOXL2, lysyl oxidase, BAPN]
            direction: loss lengthens          # optional
            source: PMID 12345678              # optional
            note: free text                    # optional

WHY ALIASES ARE MANDATORY AND NOT OPTIONAL
    CORR-353: a grep that misses on vocabulary is still a failed grep. This file called
    energy restriction DIETARY RESTRICTION and a search for "caloric restriction" returned
    nothing while a fully worked node had existed since R178. Every concept therefore
    carries the names the literature actually uses, and a hit on ANY alias counts.

WHY WORD BOUNDARIES
    CORR-353's second instance: `traction` matches inside `distraction`, `extraction`,
    `retraction` and `subtraction`, and `OSTN` matches inside `POSTNATAL`. Matching is
    word-boundary anchored by default. Set `substring: true` on a concept to opt out.

TIERS
    ZERO      nothing anywhere - not a node, not a gap, not a reference, not the ledger.
              This is the output that matters. It is a claim that the atlas has never
              once considered the concept.
    REF_ONLY  a reference mentions it but no node reasons about it.
    THIN      nodes exist but CLAUDE.md does not name it - the CORR-352 lossy-ledger state,
              worked and invisible.
    COVERED   nodes and ledger both.

Usage:
    python3 atlas/tools/concept_coverage_map.py
    python3 atlas/tools/concept_coverage_map.py --domain endocrine
    python3 atlas/tools/concept_coverage_map.py --tier ZERO
    python3 atlas/tools/concept_coverage_map.py --json atlas/data/round436/coverage.json
"""
from __future__ import annotations

import argparse
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
BIB = os.path.join(HERE, "sources", "bibliography.yaml")
LEDGER = os.path.join(ROOT, "CLAUDE.md")
REGISTRY = os.path.join(HERE, "concepts", "concept_registry.yaml")

TIERS = ["ZERO", "REF_ONLY", "THIN", "COVERED"]


def slurp(path: str) -> str:
    try:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            return fh.read()
    except OSError:
        return ""


def load_corpora():
    """Return (node_texts, gaps_text, bib_text, ledger_text)."""
    node_texts = {}
    for root, _dirs, files in os.walk(NODES):
        for fn in sorted(files):
            if fn.endswith(".yaml"):
                p = os.path.join(root, fn)
                node_texts[os.path.relpath(p, ROOT)] = slurp(p)
    return node_texts, slurp(GAPS), slurp(BIB), slurp(LEDGER)


# --- fast path -------------------------------------------------------------
# The naive scorer is O(concepts x aliases x nodes) regex searches - 2,193 concepts
# against 941 nodes did not finish in two minutes. Tokenising each corpus ONCE turns
# the single-word case (which is nearly all of it) into a set membership test, and the
# whole map then runs in about twenty seconds.
TOKEN = re.compile(r"[a-z0-9]+(?:[-\']?[a-z0-9]+)*")
WORDLIKE = re.compile(r"^[a-z0-9]+(?:[-\'][a-z0-9]+)*$")


def build_index(node_texts, gaps_t, bib_t, ledger_t):
    blob = {"nodes": "\n".join(node_texts.values()), "gaps": gaps_t,
            "bib": bib_t, "ledger": ledger_t}
    lower = {k: v.lower() for k, v in blob.items()}
    tokens = {k: set(TOKEN.findall(v)) for k, v in lower.items()}
    return lower, tokens


def alias_hits(alias, lower, tokens, key):
    a = alias.lower().strip()
    if len(a) < 3:
        return False
    if WORDLIKE.match(a):
        return a in tokens[key]
    return a in lower[key]      # multi-word aliases fall back to substring


def make_matcher(alias: str, substring: bool):
    """Word-boundary matcher unless the alias is punctuation-heavy or opted out."""
    esc = re.escape(alias)
    # \b does not fire next to non-word chars, so fall back to substring for
    # aliases that start or end with punctuation (e.g. "let-7", "miR-433-3p").
    lead = r"\b" if alias[:1].isalnum() else ""
    trail = r"\b" if alias[-1:].isalnum() else ""
    pat = esc if substring else lead + esc + trail
    return re.compile(pat, re.I)


def score_concept(c: dict, node_texts, gaps_t, bib_t, ledger_t) -> dict:
    aliases = [c["concept"]] + list(c.get("aliases") or [])
    substring = bool(c.get("substring"))
    matchers = [make_matcher(a, substring) for a in aliases if a]

    hit_nodes = []
    for path, text in node_texts.items():
        if any(m.search(text) for m in matchers):
            hit_nodes.append(path)
    n_gaps = sum(1 for m in matchers if m.search(gaps_t))
    n_bib = sum(len(m.findall(bib_t)) for m in matchers)
    n_ledger = sum(len(m.findall(ledger_t)) for m in matchers)

    if not hit_nodes and not n_gaps and not n_bib and not n_ledger:
        tier = "ZERO"
    elif not hit_nodes and not n_gaps:
        tier = "REF_ONLY"
    elif not n_ledger:
        tier = "THIN"
    else:
        tier = "COVERED"

    return dict(
        concept=c["concept"], domain=c.get("domain", "unassigned"),
        aliases=aliases[1:], direction=c.get("direction"), source=c.get("source"),
        note=c.get("note"), tier=tier,
        n_nodes=len(hit_nodes), n_gaps=n_gaps, n_bib=n_bib, n_ledger=n_ledger,
        example_nodes=hit_nodes[:3],
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", default=REGISTRY)
    ap.add_argument("--domain")
    ap.add_argument("--tier", choices=TIERS)
    ap.add_argument("--json")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(args.registry):
        print("no registry at %s\n"
              "Create it from the external enumeration - see the docstring."
              % os.path.relpath(args.registry, ROOT), file=sys.stderr)
        sys.exit(1)

    doc = yaml.safe_load(slurp(args.registry)) or {}
    concepts = doc.get("concepts") or []
    if not concepts:
        print("registry has no concepts", file=sys.stderr)
        sys.exit(1)

    node_texts, gaps_t, bib_t, ledger_t = load_corpora()
    lower, tokens = build_index(node_texts, gaps_t, bib_t, ledger_t)

    rows = []
    for c in concepts:
        aliases = [c["concept"]] + list(c.get("aliases") or [])
        h = {k: any(alias_hits(a, lower, tokens, k) for a in aliases)
             for k in ("nodes", "gaps", "bib", "ledger")}
        if not any(h.values()):
            tier = "ZERO"
        elif not h["nodes"] and not h["gaps"]:
            tier = "REF_ONLY"
        elif not h["ledger"]:
            tier = "THIN"
        else:
            tier = "COVERED"
        rows.append(dict(concept=c["concept"], domain=c.get("domain", "unassigned"),
                         aliases=aliases[1:], direction=c.get("direction"),
                         source=c.get("source"), note=c.get("note"), obscure=c.get("obscure"),
                         tier=tier, n_nodes=int(h["nodes"]), n_gaps=int(h["gaps"]),
                         n_bib=int(h["bib"]), n_ledger=int(h["ledger"]), example_nodes=[]))

    if args.domain:
        rows = [r for r in rows if r["domain"] == args.domain]
    if args.tier:
        rows = [r for r in rows if r["tier"] == args.tier]

    order = {t: i for i, t in enumerate(TIERS)}
    rows.sort(key=lambda r: (order[r["tier"]], r["domain"], -r["n_nodes"], r["concept"]))

    if not args.quiet:
        print("CONCEPT COVERAGE MAP")
        print("  registry : %s" % os.path.relpath(args.registry, ROOT))
        print("  concepts : %d" % len(rows))
        print("  corpus   : %d nodes, %d bibliography chars, %d ledger chars\n"
              % (len(node_texts), len(bib_t), len(ledger_t)))
        counts = {t: sum(1 for r in rows if r["tier"] == t) for t in TIERS}
        for t in TIERS:
            print("  %-9s %4d" % (t, counts[t]))
        print()
        by_domain = {}
        for r in rows:
            by_domain.setdefault(r["domain"], []).append(r)
        for dom in sorted(by_domain):
            rs = by_domain[dom]
            z = sum(1 for r in rs if r["tier"] == "ZERO")
            print("── %s  (%d concepts, %d ZERO)" % (dom, len(rs), z))
            for r in rs:
                flag = {"ZERO": "!!", "REF_ONLY": " ?", "THIN": " ~", "COVERED": "  "}[r["tier"]]
                print("   %s [%-8s] %-46s nodes=%-3d gaps=%-2d refs=%-3d ledger=%-3d %s"
                      % (flag, r["tier"], r["concept"][:46], r["n_nodes"], r["n_gaps"],
                         r["n_bib"], r["n_ledger"], r.get("direction") or ""))
            print()

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        with open(args.json, "w") as fh:
            json.dump({"n": len(rows), "rows": rows}, fh, indent=1)
        print("written: %s" % os.path.relpath(args.json, ROOT))


if __name__ == "__main__":
    main()
