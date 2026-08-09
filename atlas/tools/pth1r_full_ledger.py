#!/usr/bin/env python3
"""
ROUND 188 - THE FULL PTH1R LEDGER. Every question found that moves the verdict, in both directions.

The single most important finding of this round is the IMMUNOGENICITY DATA, which is
abaloparatide-specific, was missed in rounds 184-187, and reverses the molecule choice.
"""

import math

# FDA body-surface-area Km values (Guidance for Industry, 2005). HED = dose x (Km_animal / Km_human).
KM = {"mouse": 3.0, "rat": 6.0, "human": 37.0}
SUBJECT_KG = 60.0


def hed(dose_ug_kg, species):
    return dose_ug_kg * KM[species] / KM["human"]


def banner(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78)


banner("THE ANIMAL DOSE ANCHORS - AND THEY DISAGREE BY 32-FOLD")
anchors = [
    ("ogawa2002  rat, PTH(1-34), 80 ug/kg/d, growth rate UP", 80.0, "rat"),
    ("Nf2 paper  mouse, ABALOPARATIDE, 5 ug/kg/d, skeletal effects", 5.0, "mouse"),
]
print(f"  {'study':56s} {'HED ug/kg/d':>12s} {'ug/day at 60 kg':>16s}")
for label, d, sp in anchors:
    h = hed(d, sp)
    print(f"  {label:56s} {h:12.2f} {h*SUBJECT_KG:16.0f}")
print(f"""
  APPROVED HUMAN DOSES SIT BETWEEN THEM, NEARER THE MOUSE ANCHOR.
    teriparatide   20 ug/day  =  {20/SUBJECT_KG:.2f} ug/kg/day
    abaloparatide  80 ug/day  =  {80/SUBJECT_KG:.2f} ug/kg/day

  THIS SUBSTANTIALLY WEAKENS THE ROUND-184 AND ROUND-187 "TEN-FOLD SHORT" WORRY. That figure came
  entirely from ogawa2002's unusually high rat dose. Measured against abaloparatide's OWN animal
  dosing - 5 ug/kg/day in growing mice, which produced measurable skeletal change - the approved
  human dose of 80 ug/day is {80/SUBJECT_KG/hed(5.0,'mouse'):.1f}x ABOVE the mouse-equivalent, not below it.
  Nobody has run a dose-response for a growth endpoint in either species, so which anchor is
  relevant is unknown.""")

banner("WHAT MAKES IT MORE POSITIVE")
pos = [
 ("Human linear-growth data EXISTS and was missed",
  "winer2025 (JCEM): children with hypoparathyroidism on PTH(1-34), mean baseline age 13.7 +/- 5.5 y. "
  "HAZ INCREASED in the CaSR-variant group (age-by-group interaction P < 0.0001) while the APS-1 group "
  "stayed below 0. First human dataset with LINEAR GROWTH as an endpoint under a PTH1R agonist. "
  "CAVEAT: replacement dosing in hypoparathyroidism, so correcting calcium homeostasis is a confound, "
  "and APS-1 carries independent growth suppression. Not a clean anabolic test - but it is human, "
  "adolescent, and positive in the cleaner arm."),
 ("Abaloparatide-specific chondrocyte data now exists",
  "yang2019: abaloparatide stimulates chondrogenesis and suppresses hypertrophic differentiation in "
  "mouse limb-bud mesenchyme, via inhibition of intracellular ROS. Partly closes the round-186 gap that "
  "the only wild-type growth data used teriparatide."),
 ("PTH1R loss in OSTEOBLASTS causes PREMATURE FUSION",
  "qiu2015: conditional PTH1R deletion in osteoblasts gives postnatal growth retardation, fewer "
  "hypertrophic chondrocytes, impaired endochondral angiogenesis, PREMATURE GROWTH PLATE FUSION and "
  "shortened long bones. Loss of function closes the plate early, so agonism plausibly does the "
  "opposite - a DURATION bonus on top of any yield effect. Inference, not demonstration."),
 ("The osteosarcoma barrier is weaker than the label implies",
  "abdulelah2023 systematic review: clinical trials and post-marketing surveillance out to FIFTEEN YEARS "
  "show no increased osteosarcoma risk with teriparatide, with identified cases solitary and mostly "
  "attributable to other factors. The label warning derives from rat carcinogenicity."),
 ("Both labels confirm the dose is a genuine PULSE in humans",
  "Teriparatide: serum calcium rises from ~2 h, peaks 4-6 h (median +0.4 mg/dL), RETURNS TO BASELINE BY "
  "16-24 h. Abaloparatide: pre-dose calcium similar to baseline. Half-life ~1 h for both. Daily dosing "
  "is pulsatile in humans by direct measurement, which is what round 185 doubted."),
]
for i, (h, b) in enumerate(pos, 1):
    print(f"\n  P{i}. {h}\n      {b}")

banner("WHAT MAKES IT MORE NEGATIVE")
neg = [
 ("IMMUNOGENICITY - THE BIGGEST FINDING OF THIS ROUND, AND IT IS ABALOPARATIDE-SPECIFIC",
  "TYMLOS label 12.6: of patients on abaloparatide for 18 months, 41 per cent (318/773) developed "
  "anti-drug antibodies and 26 PER CENT (204/773) developed NEUTRALISING antibodies. Of those tested for "
  "cross-reactivity, 2.4 per cent (7/297) developed antibodies cross-reacting with PTHrP, AND 3 OF THOSE "
  "7 HAD NEUTRALISING ANTIBODIES TO ENDOGENOUS PTHrP. Antibodies persisted after stopping - 127 patients "
  "still positive at 1 year, 55 at 2 years, 6 at 3 years. FORTEO label 6.2 by contrast: 3 per cent "
  "(15/541), first detected after 12 months, diminished after withdrawal, no effect on calcium or BMD, "
  "and no neutralising fraction reported."),
 ("...and the second half of that is the mechanism by which this drug could SHORTEN him",
  "Endogenous PTHrP is the ligand the growth plate runs on. Neutralising it reproduces the PTHLH "
  "loss-of-function direction, and in humans PTHLH nonsense variants cause brachydactyly type E WITH "
  "SHORT STATURE (huang2026). The property that made abaloparatide mechanistically attractive - being a "
  "PTHrP analogue rather than a PTH one - is exactly what lets anti-drug antibodies cross-react with the "
  "plate's own signal. Roughly 1 per cent of those tested, not quickly reversible."),
 ("Sustained PTH1R signalling in chondrocytes shortens limbs - a third independent model",
  "liao2026 (PNAS): Nf2 loss in Col2a1+ chondrocytes decouples PTH1R from beta-arrestin2 internalisation, "
  "amplifying cAMP-CREB-pSOX9(S181)-VEGF-A signalling. Result is SHORT-LIMBED DWARFISM with reduced "
  "growth plate, proliferative zone, hypertrophic zone AND resting zone lengths and reduced EdU "
  "incorporation. The authors state the phenotype mimics PTH1R gain-of-function and Jansen. Genetic and "
  "sustained rather than pulsatile - but it is now Jansen, the humanized H223R mouse, and Nf2, three "
  "models agreeing that MORE PTH1R signalling in chondrocytes means shorter limbs."),
 ("PTH1R is enriched in the HYPERTROPHIC zone, not the proliferative one",
  "liao2026 states PTH1R has 'spatial enrichment in the hypertrophic zone', with Nf2-PTH1R colocalisation "
  "in PREhypertrophic and HYPERTROPHIC chondrocytes. Round 184 argued the receptor sits at the commitment "
  "boundary on late-proliferative cells, which was the localisation argument for it being an AMPLIFICATION "
  "lever. If the receptor is mostly post-commitment, the drug acts on cells that have already left the "
  "proliferative compartment and the amplification rationale weakens."),
 ("The growing-mouse abaloparatide experiment exists and did not measure length",
  "liao2026 gave abaloparatide 5 ug/kg/day for 30 days to ONE-MONTH-OLD mice - growing animals, wild-type "
  "controls included - and reported only trabecular and cortical microarchitecture. Femur length was not "
  "reported. That is the experiment this programme needs, already run, with the key endpoint missing."),
 ("The central question is still unanswered",
  "Whether the cell-production gain is amplification or faster pool consumption remains unmeasured. Round "
  "183: growth hormone raised cell production 3.87-fold and 97 per cent of it was faster pool spending, "
  "with amplification falling to 0.77. If abaloparatide does the same it stacks in COST with the GH "
  "already in the stack."),
]
for i, (h, b) in enumerate(neg, 1):
    print(f"\n  N{i}. {h}\n      {b}")

banner("THE IMMUNOGENICITY ARITHMETIC")
ada, neut, xr_tested, xr_pthrp, xr_neut = 41.0, 26.0, 297, 7, 3
print(f"""
  abaloparatide, 18 months:   anti-drug antibodies {ada:.0f}%   NEUTRALISING {neut:.0f}%
  teriparatide, same duration: antibodies 3%, non-neutralising, no BMD or calcium effect

  cross-reactivity to endogenous PTHrP: {xr_pthrp}/{xr_tested} tested = {100*xr_pthrp/xr_tested:.1f}%
  of which NEUTRALISING to PTHrP:       {xr_neut}/{xr_tested} tested = {100*xr_neut/xr_tested:.1f}%

  WHY THIS MATTERS MORE HERE THAN IN OSTEOPOROSIS. The label reports no clinically significant impact on
  BMD or fracture endpoints. But this use differs in three ways that all cut the same direction:
    1. THE WINDOW IS NON-REPEATABLE. Plates close. A 26 per cent chance of losing drug activity partway
       through the only opportunity is not the same risk as losing BMD gain you can chase later.
    2. THE ENDPOINT IS MORE SENSITIVE. Growth velocity responds faster and to smaller signals than BMD.
    3. THE TAIL IS INVERTED, NOT MERELY NULL. Neutralising endogenous PTHrP does not fail to help - it
       reproduces a human short-stature genotype, during the growth window, and persists for years.""")

banner("VERDICT ON THE MOLECULE")
print("""
  THE IMMUNOGENICITY DATA REVERSES THE ROUND-184 MOLECULE CHOICE. Teriparatide, not abaloparatide.

    - teriparatide is the molecule in the ONLY wild-type growth experiment (ogawa2002)
    - 3 per cent antibodies, non-neutralising, diminishing after withdrawal, against 26 per cent
      neutralising that persist for years
    - no route to neutralising endogenous PTHrP, because it is not a PTHrP analogue
    - the exposure disadvantage - 20 ug against 80 ug - is real but far less decisive than it looked,
      because the approved doses already sit ABOVE the mouse anchor and the 'ten-fold short' figure came
      from one arbitrary rat dose with no dose-response behind it

  ABALOPARATIDE'S REMAINING ADVANTAGES ARE NOW ONLY: four-fold higher labelled exposure, a gentler
  calcium profile, shorter signalling duration, and closer homology to the plate's own ligand. The last
  of those is the one that generates the anti-PTHrP antibodies.
""")
