#!/usr/bin/env python3
"""
process_evidence_rerank.py
==========================
RANK AN AGENT BY THE PROCESS IT MOVES, NOT BY WHETHER SOMEBODY PUT A CALIPER ON A BONE.

THE PROBLEM
    R302 is an operator ruling: a missing bone-length endpoint is a GAP, not a
    disqualification, and the only three real disqualifiers are (1) the target is absent
    from the tissue, (2) the direction is wrong, (3) it is redundant with an arm already in
    the stack. R437 then measured what the file actually does - 102 nodes carry the phrase
    "no length endpoint", and six of the eight instances of "no length endpoint in any
    species" in CLAUDE.md sit beside a kill word.

    So this tool asks, per node: WAS THE MISSING CALIPER THE ONLY THING WRONG WITH IT? If a
    node disposes of an agent and also names one of R302's three real disqualifiers, the
    disposal stands. If it disposes and names NONE of them, the agent was binned on the one
    ground R302 says is not a ground, and it should be sitting in the gap list instead.

WHAT IT SCORES
    For every node that mentions a missing length endpoint:
      * DISPOSED         - kill vocabulary present (dead, closed, killed, withdrawn,
                           contraindicated, do not propose, not a lever, fails)
      * REAL DISQUALIFIER - absent-from-tissue / wrong-direction / redundant-with-stack
                           language present, i.e. R302's actual grounds
      * PROCESS EVIDENCE  - does the node carry a measured effect on a TERM of the height
                           identity (N, amplification, h_term, matrix, discharge) even
                           though no bone was measured? Zone heights, cell counts, cell
                           size, proliferation index, column output, plate width.
      * TERM              - which term of H = N x A x h_term it moves, if any.

    RECOVERABLE = disposed, no real disqualifier named, and process evidence present.
    Those are the rows R302's ruling says were mis-binned.

HOW TO READ IT - THE HONEST LIMITS
    This is a TEXT audit of the atlas, not a re-reading of the primary literature. It cannot
    tell a disposal that is correct-but-tersely-worded from one that is wrong, and a node
    may name its real disqualifier in a sentence this regex does not match. So a RECOVERABLE
    row is a candidate for re-reading, never a candidate for the stack. The output is a
    queue, and the point of the queue is that this file has never had one pointing this way:
    every prior sweep asked "what has a length endpoint", and this asks "what was thrown out
    for not having one".

USAGE
    python3 atlas/tools/process_evidence_rerank.py
    python3 atlas/tools/process_evidence_rerank.py --only RECOVERABLE --json out.json
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

MISSING_CALIPER = re.compile(
    r"no\s+(?:[a-z0-9 ,/\-]{0,60}?)(?:bone[\s-]*)?length endpoint"
    r"|never (?:been )?(?:given|measured|dosed)[^.]{0,60}length"
    r"|nobody has (?:ever )?(?:put a caliper|measured a bone)"
    r"|no (?:bone|body|femur|tibia|vertebral) length (?:was )?(?:reported|measured|recorded)",
    re.I)

DISPOSAL = re.compile(
    r"\b(?:dead|do not (?:re-?)?(?:propose|promote|add)|closed|killed|kills it|withdrawn"
    r"|contraindicat\w+|disqualif\w+|not a lever|not promotable|not a candidate"
    r"|rules? it out|ruled out|deprioritis\w+|demoted)\b", re.I)

# R302's three ACTUAL grounds for disposal (see NO_MATTER/BAND below for two more).
ABSENT = re.compile(
    r"\b(?:absent from the (?:tissue|plate|growth plate)|not in the (?:tissue|plate)"
    r"|0/1[0-9] |contaminant[\s-]*leaning|fails? (?:the )?(?:CORR-327|receiver test)"
    r"|not expressed in|undetect\w+ in the (?:plate|tissue))\b", re.I)
WRONG_DIR = re.compile(
    r"\b(?:wrong direction|runs? (?:the )?(?:other way|backwards|against)|direction is wrong"
    r"|points? the wrong way|opposite (?:sign|direction)|inverse of what|shortens?\b[^.]{0,40}\bloss)\b",
    re.I)
REDUNDANT = re.compile(
    r"\b(?:step 0|substitution|redundant|already occupied|same (?:node|arm|step) as"
    r"|non-?additive|saturat\w+ the same)\b", re.I)

# TWO GROUNDS R302 DID NOT ENUMERATE BUT THIS FILE LEGITIMATELY USES, added after the first
# run over-called. R302 lists absent / wrong-direction / redundant as the real disqualifiers,
# and that list is about BIOLOGY. It is silent on two practical grounds that are nonetheless
# decisive and are not the same complaint as a missing caliper:
#   * NO CHEMICAL MATTER AT ALL - there is nothing to give. CORR-347 makes this a real,
#     checkable finding (ChEMBL n_molecules, not an Open Targets drug count) rather than an
#     assertion, and a target with zero molecules cannot be actioned however good the genetics.
#   * AN INTERIOR OPTIMUM WITH NO TITRATABLE AGENT - CORR-325's band. Half dose is taller and
#     zero dose is worse than wild type, and no agent delivers a partial, titrated reduction.
# AEBP1 is the case that exposed this: 35 monotone burden rows at P=8.4e-15, correct
# compartment, correct depth on a mapped axis - and it fails on both of these, not on the
# caliper. Counting it as mis-binned would have been my error, not the file's.
NO_MATTER = re.compile(
    r"\b(?:no chemical matter|zero chemical matter|no human ChEMBL target"
    r"|no (?:such )?(?:agent|molecule|compound|inhibitor|antibody) exists"
    r"|nothing to give|no (?:agent|molecule) in any species)\b", re.I)
BAND = re.compile(
    r"\b(?:interior optimum|it is a band|is a band\b|both (?:ends|directions) shorten"
    r"|no agent is titrated|band with no|non-?monotone)\b", re.I)

# Process-level evidence: a measured effect on a term of the identity, with no bone measured.
TERMS = [
    ("N (pool)", re.compile(
        r"\b(?:resting[\s-]*zone|reserve zone|progenitor (?:pool|number)|stem[\s-]*cell"
        r"|clone size|colony[\s-]*forming|CD73|Pthrp\+|self[\s-]*renew\w+)\b", re.I)),
    ("A (amplification)", re.compile(
        r"\b(?:cells? per column|column(?:ar)? (?:output|density)|proliferat\w+ (?:zone|rate|index)"
        r"|BrdU|EdU|Ki67|cell cycle|transit[\s-]*amplif\w+|residence time)\b", re.I)),
    ("h_term (volume/shape)", re.compile(
        r"\b(?:hypertrophic (?:zone|cell|chondrocyte)|terminal cell (?:size|height|volume)"
        r"|cell (?:swelling|enlargement|volume)|zone height|plate (?:height|width|thickness))\b", re.I)),
    ("matrix", re.compile(
        r"\b(?:aggrecan|proteoglycan|collagen (?:II|X|synthesis)|matrix (?:synthesis|deposition)"
        r"|sulfation|GAG\b|fixed charge)\b", re.I)),
    ("discharge", re.compile(
        r"\b(?:vascular invasion|chondro-?osseous junction|resorption|MMP-?13|septoclast"
        r"|mineralis\w+|ossification front)\b", re.I)),
]

MEASURED = re.compile(
    r"\b(?:P\s*[=<]|p\s*[=<]\s*0|significant\w*|increased?|decreased?|reduced?|raised?"
    r"|\d+(?:\.\d+)?\s*(?:%|per cent|fold|x)|\bn\s*=\s*\d+)\b", re.I)


def node_text(path: str) -> tuple[str, dict]:
    raw = open(path, encoding="utf-8", errors="ignore").read()
    try:
        doc = yaml.safe_load(raw) or {}
    except Exception:
        doc = {}
    return raw, doc if isinstance(doc, dict) else {}


def sentences_near(text: str, pat: re.Pattern, window: int = 700) -> str:
    """The disposal grounds sit near the complaint, not anywhere in a 40 KB node."""
    out = []
    for m in pat.finditer(text):
        out.append(text[max(0, m.start() - window): m.end() + window])
    return "\n".join(out)


def score(path: str) -> dict | None:
    raw, doc = node_text(path)
    if not MISSING_CALIPER.search(raw):
        return None
    ctx = sentences_near(raw, MISSING_CALIPER)

    disposed = bool(DISPOSAL.search(ctx))
    grounds = []
    if ABSENT.search(ctx):
        grounds.append("absent_from_tissue")
    if WRONG_DIR.search(ctx):
        grounds.append("wrong_direction")
    if REDUNDANT.search(ctx):
        grounds.append("redundant_step0")
    if NO_MATTER.search(ctx):
        grounds.append("no_chemical_matter")
    if BAND.search(ctx):
        grounds.append("interior_optimum")

    terms = []
    for name, pat in TERMS:
        hits = len(pat.findall(raw))
        if hits:
            terms.append((name, hits))
    terms.sort(key=lambda t: -t[1])
    has_measure = bool(MEASURED.search(ctx))

    if disposed and not grounds and terms and has_measure:
        verdict = "RECOVERABLE"
    elif disposed and grounds:
        verdict = "DISPOSED_ON_REAL_GROUNDS"
    elif disposed:
        verdict = "DISPOSED_THIN"
    else:
        verdict = "GAP_ALREADY"

    return dict(
        node=os.path.relpath(path, HERE),
        name=doc.get("name") or doc.get("id") or os.path.basename(path),
        confidence=doc.get("confidence"),
        verdict=verdict,
        disposed=disposed,
        real_grounds=grounds,
        terms=[{"term": t, "hits": h} for t, h in terms[:3]],
        top_term=terms[0][0] if terms else None,
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", action="append")
    ap.add_argument("--json")
    args = ap.parse_args()

    rows = []
    for root, _d, files in os.walk(NODES):
        for fn in sorted(files):
            if fn.endswith(".yaml"):
                r = score(os.path.join(root, fn))
                if r:
                    rows.append(r)

    counts: dict[str, int] = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1

    print("PROCESS-EVIDENCE RE-RANK  (a queue for re-reading, not a promotion list)")
    print("  nodes citing a missing length endpoint: %d" % len(rows))
    for k in ("RECOVERABLE", "DISPOSED_ON_REAL_GROUNDS", "DISPOSED_THIN", "GAP_ALREADY"):
        print("    %-26s %d" % (k, counts.get(k, 0)))
    print()

    keep = set(args.only) if args.only else {"RECOVERABLE"}
    sel = [r for r in rows if r["verdict"] in keep]
    sel.sort(key=lambda r: (r["top_term"] or "zz", r["name"]))
    print("  showing: %s\n" % ", ".join(sorted(keep)))
    print("  %-22s %-4s %s" % ("TERM MOVED", "CONF", "NODE"))
    for r in sel:
        print("  %-22s %-4s %s" % ((r["top_term"] or "-")[:22], r["confidence"] or "-",
                                   r["name"][:88]))

    print("\n  RECOVERABLE = disposal language present, NONE of R302's three real")
    print("  disqualifiers named nearby, and a measured effect on a term of the height")
    print("  identity. Those were binned on the one ground R302 says is not a ground.")

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        json.dump({"counts": counts, "rows": rows}, open(args.json, "w"), indent=1)
        print("\n  written: %s" % os.path.relpath(args.json, ROOT))


if __name__ == "__main__":
    main()
