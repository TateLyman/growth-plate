#!/usr/bin/env python3
"""
THE CNP AXIS ACROSS ITS WHOLE DOSE RANGE IN HUMANS - and the term it moves.

WHY THIS TOOL EXISTS
--------------------
Round 202 left one question as the most decision-relevant unmeasured quantity in
the stack: does the CNP axis raise TERMINAL CELL HEIGHT, the free axis, or does
it buy length some other way? And round 202's other finding - that the
somatotropic axis SATURATES h_term while spending reserve linearly - raised the
obvious follow-up: does the CNP axis saturate too?

Both are answerable, and the answers point in opposite directions.

The census below is assembled ONLY from records already in this atlas plus one
paper the atlas held as a bare citation and had never read (jeong2026). Every
phenotype is as reported by its own authors.

A NOTE ON WHY THE DOSE RANGE IS THE ORGANISING AXIS. Human evidence on this
pathway comes from three places that are usually discussed separately and that
are really three points on one dose curve:
  POPULATION   common and rare missense variation, mild, lifelong
  PHARMACOLOGY vosoritide and navepegritide, moderate, months to years
  CONSTITUTIVE rare strongly activating germline variants, maximal, lifelong
Reading them together is what makes the shape visible.
"""

# ============================================================================
# POINT 1 - POPULATION. jeong2026, UK Biobank, 245 characterised NPR2 variants.
# ============================================================================
JEONG = {
    "variants_characterised": 245,
    "loss_of_function": 47,
    "partial_loss": 34,
    "gain_of_function": 14,
    "shape": "near-linear association between activity score and standing height",
    "r2": 0.438,
    "p": "5.8e-10",
    "additivity": "within each functional activity category, polygenic scores combine "
                  "ADDITIVELY with the effect of the NPR2 variant",
    "enrichment": "PTVs and LoF missense enriched in the SHORTEST individuals; "
                  "GoF variants enriched in the TALLEST",
    "phewas": "NPR2 activity significantly associated ONLY with height and "
              "height-associated traits",
    "authors_metaphor": "a dimmer switch",
}

# ============================================================================
# POINT 2 - PHARMACOLOGY. Pooled randomised evidence, achondroplasia.
# ============================================================================
PHARM = {
    "cnpmeta2026": {
        "design": "meta-analysis, 11 studies N=542, of which 4 RCTs n=326, low risk of bias",
        "agv": "+1.36 cm/year (95% CI 1.05 to 1.68), P<.00001",
        "height": "+1.24 cm (0.47 to 2.01), P=.002; height Z +0.28 (0.20 to 0.37)",
        "segment_ratio": "upper-to-lower UNCHANGED, MD -0.02 (95% CI -0.04 to +0.01), "
                         "P=0.17, I-squared 0",
        "age_gradient": "AGV gain LARGER at age 5+ (1.63 cm/yr, 1.34-1.92) than under 5 "
                        "(0.91 cm/yr, 0.41-1.41), subgroup P=.01",
        "adult_height": "EXPLICITLY NOT YET KNOWN",
    },
    "rua2025": {
        "design": "single-centre retrospective, 27 children, 15 completing 24 months",
        "segments": "sitting height SDS +0.79 against arm span SDS +0.32, both P<=.01",
        "ratios": "upper-to-lower segment ratio -0.10 (P<=.01, leg-favouring) BUT "
                  "sitting-height-to-height ratio UNCHANGED - two proportion measures "
                  "disagreeing inside one cohort",
    },
}

# ============================================================================
# POINT 3 - CONSTITUTIVE. Every human strong-activation report in the atlas.
# ============================================================================
# columns: ref, gene/lesion, n, height, then the non-height phenotypes as reported
CONSTITUTIVE = [
    ("miura2012",  "NPR2 p.Val883Met, constitutively active", 3,
     "tall stature, three-generation family, blood cGMP elevated",
     ["scoliosis", "macrodactyly of great toes"]),
    ("miura2014",  "NPR2 p.Ala488Pro, GoF", "4-generation family",
     "tall stature",
     ["scoliosis", "macrodactyly of great toes", "coxa valga",
      "slipped capital femoral epiphysis"]),
    ("lauffer2020", "NPR2 p.Met482_Leu483del, submembrane GoF", 3,
     "+2.77 SDS mother, +1.96 and +1.30 SDS daughters",
     ["macrodactyly of great toes", "pseudo-epiphyses of mid and proximal phalanges"]),
    ("moffatt2025", "NPR3 p.Pro128Ser, biallelic LoF (ER-retained)", 3,
     "height z +2.9 to +4.9",
     ["scoliosis in ALL THREE, one requiring SPINAL FUSION SURGERY",
      "markedly elongated proximal and middle phalanges",
      "additional epiphyses in phalangeal and metacarpal bones",
      "lumbar spine BMD low considering the tall stature"]),
    ("lauffer2022", "NPR3 biallelic LoF", 3,
     "+3.03, +3.9 and +3.93 SDS; proband 205.1 cm at 14.7 y",
     ["NORMAL sitting-height-to-height ratio and arm span",
      "normal blood pressure, normal aortic diameter in proband"]),
    ("boudin2018", "NPR3 biallelic LoF, three families", 4,
     "+2.7, +3.43, +3.9 and +4.76 SDS",
     ["aortic root dilatation in 2 of 4, PROGRESSIVE in both",
      "mitral valve prolapse in 1", "normal blood pressure in every patient"]),
]


def rule(c="="):
    print(c * 88)


def main():
    rule()
    print("THE CNP AXIS IN HUMANS, READ ACROSS ITS DOSE RANGE")
    rule()

    print("\n[1] POPULATION DOSE - jeong2026, UK Biobank")
    print(f"    {JEONG['variants_characterised']} NPR2 missense variants functionally "
          f"characterised:")
    print(f"        {JEONG['loss_of_function']} loss-of-function, "
          f"{JEONG['partial_loss']} partial loss, "
          f"{JEONG['gain_of_function']} GAIN-OF-FUNCTION")
    print(f"    shape      : {JEONG['shape']}")
    print(f"    fit        : R-squared {JEONG['r2']}, p = {JEONG['p']}")
    print(f"    additivity : {JEONG['additivity']}")
    print(f"    direction  : {JEONG['enrichment']}")
    print(f"    PheWAS     : {JEONG['phewas']}")
    print(f"    the authors' own word for the shape: \"{JEONG['authors_metaphor']}\"")

    print("\n    THIS IS THE ANSWER TO THE SATURATION QUESTION AND IT IS THE OPPOSITE")
    print("    OF THE SOMATOTROPIC ONE. Round 202 found h_term saturating against")
    print("    somatotropic drive - 40 per cent of the available gain in the first")
    print("    tripling of pool consumption, 9 per cent in the next 3.3-fold. The")
    print("    CNP axis in humans shows NO SUCH CEILING across the characterised")
    print("    range, and the gain-of-function end is populated and goes the right")
    print("    way. THE TWO AXES SHOULD THEREFORE BE DOSED BY OPPOSITE LOGIC.")

    print("\n[2] PHARMACOLOGICAL DOSE - pooled randomised evidence")
    m = PHARM["cnpmeta2026"]
    for k in ("design", "agv", "height", "segment_ratio", "age_gradient", "adult_height"):
        print(f"    {k:<14}: {m[k]}")
    r = PHARM["rua2025"]
    print(f"\n    rua2025 {r['design']}")
    print(f"        segments : {r['segments']}")
    print(f"        ratios   : {r['ratios']}")
    print("\n    THE POOLED RANDOMISED ANSWER IS PROPORTIONATE GROWTH, I-squared 0.")
    print("    Against the open-site register that is the FAVOURABLE answer - the")
    print("    agent does not pour growth into one segment and starve the others.")
    print("    AND THE AGE GRADIENT RUNS THE HELPFUL WAY: the gain is LARGER in the")
    print("    older subgroup, which is the opposite of the usual assumption and the")
    print("    only age-direction evidence the atlas has on this axis. It still stops")
    print("    far short of bone age 16 and adult height is explicitly unknown.")

    print("\n[3] CONSTITUTIVE DOSE - every human strong-activation report held here")
    counts = {}
    people = 0
    for ref, lesion, n, height, phenos in CONSTITUTIVE:
        print(f"\n    {ref}  [{lesion}]")
        print(f"        height : {height}")
        for p in phenos:
            print(f"        - {p}")
        if isinstance(n, int):
            people += n
        for p in phenos:
            # only POSITIVE findings are tallied - a reported normal is not a phenotype
            if p.lower().startswith("normal") or p.lower().startswith("no "):
                continue
            key = ("scoliosis" if "scoliosis" in p.lower() else
                   "digital overgrowth" if ("macrodactyly" in p.lower()
                                            or "phalang" in p.lower()) else
                   "extra/pseudo epiphyses" if "epiphys" in p.lower() and "slipped" not in p.lower() else
                   "aortic/valve" if ("aortic" in p.lower() or "mitral" in p.lower()) else
                   None)
            if key:
                counts.setdefault(key, set()).add(ref)

    print("\n" + "-" * 88)
    print("    PHENOTYPE TALLY ACROSS THE SIX REPORTS")
    print("-" * 88)
    for k in sorted(counts, key=lambda x: -len(counts[x])):
        print(f"    {k:<26} {len(counts[k])}/6 reports   {sorted(counts[k])}")

    print("\n    TWO PATTERNS, AND BOTH MATTER FOR THE OPEN-SITE REGISTER.")
    print("    (i) DIGITAL OVERGROWTH IS THE MOST CONSISTENT NON-HEIGHT FEATURE.")
    print("        Macrodactyly, elongated phalanges, extra and pseudo-epiphyses in")
    print("        the hands and feet. THE PHALANGES CONTRIBUTE NOTHING TO STATURE.")
    print("        At constitutive activation the axis puts a visible share of its")
    print("        output into sites with zero height value.")
    print("    (ii) SPINE DEFORMITY, NOT SPINE LENGTH. Scoliosis in three of six")
    print("        reports, in one of them in all three siblings with one requiring")
    print("        SPINAL FUSION SURGERY - which ENDS spinal growth outright - and")
    print("        with lumbar BMD low for the height achieved. A curve converts")
    print("        axial length into deviation, so this is a YIELD term and not only")
    print("        a safety term.")

    print("\n[4] WHAT THE THREE POINTS SAY TOGETHER")
    print("    The shape is DOSE-DEPENDENT and the atlas had been reading one point")
    print("    at a time:")
    print("      mild, lifelong        -> height only, linear, PheWAS-clean")
    print("      pharmacological       -> proportionate segment growth, I-squared 0")
    print("      maximal, constitutive -> height PLUS digital overgrowth PLUS spine")
    print("                               deformity")
    print("    THE POPULATION PheWAS CANNOT EXCLUDE THE CONSTITUTIVE PHENOTYPES and")
    print("    should not be quoted as if it did - it samples the mild end of the")
    print("    activity range, where by construction nothing extreme happens.")
    print("    Equally, the constitutive families are germline and lifelong, so they")
    print("    do not bound what a months-long exposure at a late bone age does.")
    print("    WHAT IS NOT AVAILABLE AT ANY DOSE: a terminal cell height measurement")
    print("    under any CNP-axis agent, in any species. weber2025's +20 per cent is")
    print("    NPR3 LOSS, which is the clearance arm and not NPR2 agonism, and NPR3")
    print("    is independently reported to be bifunctional.")
    rule()


if __name__ == "__main__":
    main()
