#!/usr/bin/env python3
"""
THE WRITE-OFF SITE AUDIT - was any compound killed on an endpoint that could not
have seen the sites we now know are open?

WHY THIS TOOL EXISTS
--------------------
CORR-195 established the open-site register: at a hand-wrist bone age of 16 the
knee, the proximal femur, the spine and sacrum, and the spheno-occipital
synchondrosis can all still be contributing, and the KNEE IS STILL THE LARGEST
SINGLE CONTRIBUTOR. The register imposed a rule - no agent may be scored against
one site.

That rule applies BACKWARDS as well as forwards. If a compound was retired
because a study found no effect, and that study measured only one site, the
retirement rests on a partial endpoint. This tool re-examines every negative and
null length result in the bibliography and asks ONE question of each: WHAT DID
THE ENDPOINT ACTUALLY MEASURE?

THE CLASSIFICATION
------------------
  WHOLE-BODY   adult height, stature, naso-anal, crown-rump, body length -
               a SUM over sites, so a null is a real null
  AXIAL        vertebra, spine, tail, sitting height - covers the late-running
               contributors
  APPENDICULAR long bone, tibia, femur, humerus, ulna, metatarsal - covers the
               knee, which is the biggest single term, but NOT the spine
  CELL/TISSUE  a histological or molecular endpoint with no length at all
  UNCLEAR      cannot be classified from the recorded finding

A null on an APPENDICULAR-only endpoint does not exclude an axial effect, and a
null on an AXIAL-only endpoint does not exclude a knee effect. Neither is fatal
on its own - what matters is whether the atlas WROTE THE COMPOUND OFF on it.
"""
import os, re, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "sources", "bibliography.yaml")

NEGATIVE = re.compile(
    r"\b(did not (increase|change|alter|affect|raise|lengthen)|no (gain|increase|change|effect|"
    r"difference|significant)|not additive|failed to|without (any )?(gain|increase|change)|"
    r"unchanged|null|abolished|no longer)\b", re.I)

LENGTHY = re.compile(
    r"\b(length|elongation|height|stature|growth rate|overgrowth|longitudinal growth)\b", re.I)

SITE_PATTERNS = [
    ("WHOLE-BODY",   r"\b(adult height|final height|stature|standing height|naso-?anal|"
                     r"crown-?rump|body length|whole[- ]body)\b"),
    ("AXIAL",        r"\b(vertebra\w*|spine|spinal|axial skeleton|tail length|sitting height|"
                     r"trunk|T1-S1)\b"),
    ("APPENDICULAR", r"\b(long bone|tibia\w*|femur|femoral|humerus|humeral|ulna\w*|radius|"
                     r"metatarsal|metacarpal|limb|appendicular|leg length|knee)\b"),
    ("CELL/TISSUE",  r"\b(zone (height|thickness)|cell (height|volume|size)|chondrocyte|"
                     r"histomorphometr\w+|proliferation index|apoptosis|cGMP|expression)\b"),
]


def classify(text):
    hits = []
    for label, pat in SITE_PATTERNS:
        if re.search(pat, text, re.I):
            hits.append(label)
    return hits or ["UNCLEAR"]


def main():
    with open(BIB) as f:
        data = yaml.safe_load(f)
    refs = data.get("refs", data)

    rows = []
    for rid, v in refs.items():
        if not isinstance(v, dict):
            continue
        olf = str(v.get("one_line_finding") or "")
        if not olf:
            continue
        # a negative statement ABOUT a length endpoint
        for sent in re.split(r"(?<=[.;])\s+", olf):
            if NEGATIVE.search(sent) and LENGTHY.search(sent):
                rows.append((rid, sent.strip(), classify(sent)))
                break

    print("=" * 96)
    print("NEGATIVE OR NULL LENGTH RESULTS IN THE BIBLIOGRAPHY, BY ENDPOINT SITE")
    print("=" * 96)
    print(f"    scanned {len(refs)} references; {len(rows)} carry a negative length statement\n")

    buckets = {}
    for rid, sent, cls in rows:
        key = "+".join(sorted(cls))
        buckets.setdefault(key, []).append((rid, sent))

    # the ones that matter: a length null seen ONLY through one skeletal region
    RISK = [k for k in buckets
            if ("APPENDICULAR" in k or "AXIAL" in k)
            and "WHOLE-BODY" not in k]

    print("-" * 96)
    print("AT RISK - a length null measured through ONE skeletal region, with no")
    print("whole-body endpoint in the recorded finding. These are the ones to check.")
    print("-" * 96)
    n_risk = 0
    for k in sorted(RISK):
        for rid, sent in buckets[k]:
            n_risk += 1
            print(f"\n  [{k}]  {rid}")
            print(f"      {sent[:300]}")
    if not n_risk:
        print("    none")

    print("\n" + "-" * 96)
    print("NOT AT RISK - the null was measured on a whole-body endpoint, which is a")
    print("SUM over every open site and therefore cannot hide a site-specific gain.")
    print("-" * 96)
    for k in sorted(buckets):
        if k in RISK:
            continue
        for rid, sent in buckets[k]:
            print(f"  [{k}]  {rid}: {sent[:170]}")

    print("\n" + "=" * 96)
    print("SUMMARY BY BUCKET")
    print("=" * 96)
    for k in sorted(buckets, key=lambda x: -len(buckets[x])):
        flag = "  <-- CHECK" if k in RISK else ""
        print(f"    {k:<40} {len(buckets[k]):>3}{flag}")
    print("\n    A BUCKET LABEL IS NOT A VERDICT. It says what the recorded finding")
    print("    mentions, not what the paper measured. Every entry flagged AT RISK is")
    print("    resolved by hand in the round-204 node - most turn out to be fine,")
    print("    and the ones that are not are named there.")
    print("=" * 96)


if __name__ == "__main__":
    main()
