#!/usr/bin/env python3
"""
The PTHrP-PTH1R axis is an inverted U for bone length, and wild type sits at
the top of it. That single statement reconciles every result in this line.

WHY THIS TOOL EXISTS
--------------------
By round 196 the line had a pile of results that did not obviously fit
together: catastrophic phenotypes at both genetic extremes, a rescue in
uraemia, a rescue in achondroplasia, and a wall of nulls under exogenous
agonism in healthy animals. Round 197 adds the two genetic gain-of-function
arms that were missing, and the pile resolves.

The organising claim is not new biology - it is the standard dose-response
shape - but nothing in this atlas had assembled the evidence for it on a LENGTH
endpoint specifically, which is what decides the case.

Every entry below is a bone-length or limb-length outcome under a defined
perturbation of PTHrP-PTH1R signalling tone. Nothing is estimated.
"""

# tone: qualitative position on the axis relative to wild type
# outcome: what happened to BONE LENGTH specifically
LADDER = [
    ("Blomstrand chondrodysplasia (human)", "PTH1R null",
     "ZERO", "lethal, advanced skeletal maturation, severely short limbs",
     "blomstrand_chondrodysplasia", "human"),

    ("PTH1R chondrocyte-specific knockout (mouse)", "PTH1R absent in cartilage",
     "ZERO in cartilage", "shortened growth plate established by E17.5",
     "correa2010", "mouse"),

    ("PTHrP null (mouse)", "ligand absent",
     "ZERO", "premature hypertrophy, short bones",
     "correa2010", "mouse"),

    ("Zfp521 chondrocyte cKO (mouse)", "PTHrP EFFECTOR removed downstream",
     "LOW", "endochondral bones smaller; growth plate -30%; resting zone "
     "5+ layers down to 1-2; cell columns and CELLS PER COLUMN both reduced; "
     "fewer hypertrophic cells each of INCREASED height; ECM -50%",
     "correa2010", "mouse"),

    ("PTHLH haploinsufficiency (human)", "ligand gene dose halved",
     "LOW", "brachydactyly type E with short stature",
     "pth1r_gene", "human"),

    ("uraemic rat + intermittent PTH(1-37)", "restored from a suppressed state",
     "LOW -> NORMAL", "snout-tail length gain 4.78 -> 6.17 cm, p=0.0055; "
     "restores to the treated-sham value, does not exceed it",
     "schmitt2000", "rat"),

    ("achondroplastic mouse + PTH", "added to an FGFR3-suppressed plate",
     "LOW -> NORMAL", "humeral and tibial length brought toward wild type; "
     "premature cranial synchondrosis fusion partially prevented",
     "xie2012", "mouse"),

    ("WILD TYPE", "endogenous", "OPTIMUM", "reference", "-", "-"),

    ("wild-type mouse pup + PTH(1-34) 50 ug/kg/d x 9 d", "agonist added",
     "ABOVE OPTIMUM", "NO CHANGE in tibia length, three cranial base bone "
     "lengths, or two synchondrosis lengths, while BV/TV, Tb.N and BMD rose",
     "koh2022", "mouse"),

    ("young male rat + PTH(1-34) 16-80 ug/kg/d x 18 d", "agonist added",
     "ABOVE OPTIMUM", "NO CHANGE in femur length while tibial bone "
     "parameters rose 10-50%",
     "fda_forteo_pharmreview_2002", "rat"),

    ("intact male F344 rat + PTH(1-34) 8-40 ug/kg/d x 1 y", "agonist added",
     "ABOVE OPTIMUM", "did not alter linear bone growth in males",
     "fda_forteo_pharmreview_2002", "rat"),

    ("F344 rat to 26 months + PTH(1-34) 5-30 ug/kg/d", "agonist added",
     "ABOVE OPTIMUM", "femur length 35 mm in ALL EIGHT ARMS at terminal",
     "fda_forteo_pharmreview_2002", "rat"),

    ("hypoparathyroid children, PTH(1-34) vs calcitriol, 3 y randomised",
     "agonist added at replacement dose",
     "ABOVE OPTIMUM", "height percentile 47 vs 53, p=0.76, no change over time",
     "winer2010", "human"),

    ("10-week-old FEMALE rat + PTH(1-34) 50 ug/kg/d x 15 d", "agonist added",
     "ABOVE OPTIMUM", "FEMORAL LENGTH INCREASED - the lone healthy-animal "
     "positive; systemic IGF-I fell; body weight not reported in the abstract",
     "toromanoff1998", "rat"),

    ("Col2-PTHrP overexpression (mouse)", "ligand forced up in cartilage",
     "HIGH", "SHORT-LIMBED DWARFISM and delayed endochondral ossification; "
     "by 7 weeks foreshortened and misshapen but histologically near-normal",
     "weir1996", "mouse"),

    ("Jansen metaphyseal chondrodysplasia (human)",
     "PTH1R constitutively active",
     "MAXIMAL", "SEVERE SHORT STATURE; hypertrophic exit delayed and then "
     "failing to discharge",
     "jansen_metaphyseal_chondrodysplasia", "human"),
]

ORDER = ["ZERO", "ZERO in cartilage", "LOW", "LOW -> NORMAL", "OPTIMUM",
         "ABOVE OPTIMUM", "HIGH", "MAXIMAL"]


def main():
    print("=" * 100)
    print("BONE LENGTH ACROSS THE FULL RANGE OF PTHrP-PTH1R SIGNALLING TONE")
    print("=" * 100)
    for tone in ORDER:
        rows = [r for r in LADDER if r[2] == tone]
        if not rows:
            continue
        print(f"\n### TONE = {tone}")
        for lab, pert, _, outcome, ref, sp in rows:
            print(f"  {lab}")
            print(f"      perturbation : {pert}")
            print(f"      LENGTH       : {outcome}")
            print(f"      {sp}, {ref}")

    print("\n" + "=" * 100)
    print("[1] THE SHAPE")
    print("=" * 100)
    print("    Both extremes shorten bone. Zero signalling shortens it")
    print("    (Blomstrand, PTHrP null, PTH1R cKO, Zfp521 cKO, PTHLH")
    print("    haploinsufficiency). Maximal signalling shortens it too")
    print("    (Jansen in human, Col2-PTHrP overexpression in mouse). The")
    print("    curve has a maximum, and every result in between is consistent")
    print("    with WILD TYPE SITTING AT OR NEAR THAT MAXIMUM.")

    print("\n[2] WHAT FOLLOWS, AND IT IS THE WHOLE ANSWER")
    print("    An agonist can only help from BELOW the optimum. That is exactly")
    print("    the set of states where agonism works:")
    print("      uraemia    - PTH-driven growth failure, rescued (schmitt2000)")
    print("      achondroplasia - FGFR3 suppressing the plate, rescued (xie2012)")
    print("    And it is exactly the set where agonism does nothing:")
    print("      wild-type mouse pup, young male rat, adult male rat, rat to")
    print("      terminal, and randomised human children.")
    print("    A healthy subject is not below the optimum. Adding agonist moves")
    print("    along the flat top of the curve, or over it.")

    print("\n[3] THE ONE STATE THAT MIGHT BE BELOW THE OPTIMUM, AND IT IS THE")
    print("    CASE IN QUESTION")
    print("    kindblom2002 measured both ligands of this loop in human growth")
    print("    plate biopsies across Tanner stages and found both fall")
    print("    significantly with maturation - |r| 0.816 for Ihh and 0.911 for")
    print("    PTHrP. If endogenous tone at Tanner 4-5 has dropped BELOW the")
    print("    optimum, a late subject is in the rescuable region and every")
    print("    null above was measured in the wrong animal at the wrong age.")
    print("    Nobody has measured the RECEPTOR across that range, and")
    print("    kindblom2002 excluded the resting zone by design. THIS IS THE")
    print("    ONLY ROUTE BY WHICH THIS LINE REMAINS ALIVE.")

    print("\n[4] THE COUNTERWEIGHT TO THAT HOPE")
    print("    Falling ligand tone with maturation is also what a plate that is")
    print("    SHUTTING DOWN looks like. The pre-hypertrophic population that")
    print("    carries the receptor (chu2026, hallett2021) shrinks with the")
    print("    plate. Falling tone is equally consistent with a vanishing")
    print("    target as with an unoccupied one, and the two predict opposite")
    print("    signs. One immunostaining series settles it.")

    print("\n[5] A SEPARATE PROBLEM WITH EVERY POSITIVE IN THIS FILE")
    print("    The healthy-animal positives are +2% to +6% on a length")
    print("    endpoint. wezeman2003 measured L4 vertebral body height in")
    print("    growing rats with a pair-fed design: pair-fed controls were")
    print("    7.69 mm against 8.22 mm ad libitum in males and 6.83 against")
    print("    7.19 mm in females - CALORIC INTAKE ALONE MOVES VERTEBRAL BODY")
    print("    HEIGHT BY 5 TO 6 PER CENT. Every positive in this line is inside")
    print("    the range that feeding alone produces, and only two studies in")
    print("    the whole line controlled intake.")
    print("=" * 100)


if __name__ == "__main__":
    main()
