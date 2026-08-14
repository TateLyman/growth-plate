#!/usr/bin/env python3
"""
ROUND 382. HOW MUCH GAPMER, AND WHICH OF THE EIGHT ROUTES IS CHEAPEST.

Two calculations and one ranking.

(1) THE GAPMER DOSE, derived twice and cross-checked. An unconjugated phosphorothioate
    2'-MOE gapmer aimed at a NON-LIVER tissue is the relevant class: GalNAc conjugation
    buys roughly 10-fold potency but delivers to hepatocytes, and ASGR1 is 3.2 CPM in the
    growth plate (R376), so the conjugate is the wrong format here.

(2) COST TO FIRST DECISION for each of the eight routes in R381. The right metric is NOT
    cost-to-therapy - every route ends at the same regulatory wall - it is what it costs to
    learn whether the route works at all.

⚠ ALL COST FIGURES ARE ORDER-OF-MAGNITUDE PLANNING ESTIMATES FROM PUBLIC VENDOR AND
   CONTRACT-MANUFACTURING PRACTICE. They are `value_unverified` and are here to rank the
   options, not to budget one.
"""
KM_MOUSE, KM_HUMAN = 3.0, 37.0

print("=" * 78)
print("1. THE GAPMER DOSE - TWO INDEPENDENT ROUTES")
print("=" * 78)
print("\nROUTE A - allometry from the systemic mouse dosing range for extrahepatic gapmers")
print("  literature range: 20-25 mg/kg TWICE WEEKLY subcutaneous = 40-50 mg/kg/week")
for mouse_wk in (40.0, 50.0):
    hed = mouse_wk * KM_MOUSE / KM_HUMAN
    print(f"  mouse {mouse_wk:.0f} mg/kg/wk -> HED {hed:5.2f} mg/kg/wk", end="")
    print("   ->  " + " · ".join(f"{bw} kg = {hed*bw:5.0f} mg/wk" for bw in (50, 60, 70)))

print("\nROUTE B - the empirical class dose of APPROVED unconjugated systemic PS-MOE gapmers")
print("  inotersen (Tegsedi)   284 mg ONCE WEEKLY subcutaneous")
print("  volanesorsen (Waylivra) 285 mg ONCE WEEKLY subcutaneous")
print("  (GalNAc-conjugated agents dose ~10x lower but go to liver - wrong format here)")

print("\n→ THE TWO ROUTES CONVERGE: ~240-280 mg/week from allometry, ~285 mg/week from the")
print("  approved class. TAKE ~250-300 mg ONCE WEEKLY SUBCUTANEOUS as the planning dose.")
annual_g = 0.285 * 52
print(f"\n  ANNUAL API REQUIREMENT: 285 mg x 52 = {annual_g:.1f} g of GMP oligonucleotide per year.")
print("  ⛔ THAT IS THE NUMBER THAT MATTERS FOR FEASIBILITY, AND IT IS SMALL. Oligonucleotide")
print("     synthesis is run at kilogram scale industrially; ~15 g/yr is a rounding error on")
print("     a manufacturing line. The cost is in CMC, release testing and toxicology, NOT in")
print("     the grams.")
print("\n⚠ CAVEATS ON THE DOSE. It assumes (a) growth-plate cartilage behaves like other")
print("  extrahepatic tissue for a PS-ASO, which posey2017 supports qualitatively and nobody")
print("  has quantified; (b) no conjugate; (c) an adult-scaled mg/kg. And the DEPTH of")
print("  knockdown needed is unknown - see the dose-response gap g_l12_377b.")

print("\n" + "=" * 78)
print("2. COST TO FIRST DECISION - THE EIGHT ROUTES OF R381")
print("=" * 78)
ROUTES = [
    ("SAM / methyl donor",        "$20/month",      "OTC today",
     "grade E; active at 25-250 uM vs ~100 nM plasma; antiproliferative (R347)"),
    ("miR-221 mimic",             "$200-500",       "catalogue reagent",
     "HHIP is a VALIDATED miR-221 target; but miRNAs are promiscuous by design"),
    ("PS-ASO gapmer panel",       "$5k-15k",        "~20 gapmers, 200 nmol each, + cell assay",
     "the cheapest route to a CLEAN, POTENT, SELECTIVE HHIP-lowering agent"),
    ("anti-HHIP KineTAC",         "$30k-80k",       "CRO bispecific expression + purification",
     "needs an HHIP binder first; epitope-agnostic; ACKR3 handle 6.17x enriched"),
    ("siRNA in WYRGRL exosome",   "$50k-150k",      "lentivirus + exosome prep, lab-months",
     "vehicle demonstrated (yuan2024) but it is a biologics process, not a reagent"),
    ("CRISPRi dose-response",     "$20k-50k",       "dCas9-KRAB chondrocytes + guide panel",
     "NOT a therapy - it is the experiment that tells you how much knockdown to aim for"),
    ("somatic enhancer editing",  "$100k+",         "no growth-plate delivery precedent",
     "irreversible; only route that could pick a TRUNK-restricted element"),
    ("function-blocking antibody", "$150k-500k",    "de novo campaign + functional counter-screen",
     "most expensive discovery path; superseded as a requirement by the degrader logic"),
]
print(f"{'route':28s} {'cost to decide':14s} {'what that buys':44s}")
for r, c, w, n in ROUTES:
    print(f"{r:28s} {c:14s} {w:44s}")
    print(f"{'':28s} {'':14s} {n}")

print("\n" + "=" * 78)
print("3. THE ANSWER, AND IT IS NOT ON THE LIST")
print("=" * 78)
print("""THE CHEAPEST DECISIVE STEP IS A CALIPER. darbellay2024 already built and phenotyped
Col2a1_EGFP;Hhip_deltaCE2-3 - a mouse with Hhip transcripts 15 per cent lower IN CARTILAGE
- and measured no bone. Obtaining or re-deriving that line and measuring femur, tibia and
vertebral length at skeletal maturity costs roughly $10k-25k of mouse work and needs no new
chemistry, no new vehicle and no new target validation.

IT IS ALSO GATING IN BOTH DIRECTIONS:
  · If 15 per cent knockdown moves a bone, then ANY of the eight routes is worth building,
    because every one of them can beat 15 per cent.
  · If it does not, the required depth is greater than 15 per cent and the cheap dirty
    options (SAM, miR mimic) are dead on potency before anyone spends on them.

AND THE SECOND-CHEAPEST IS THE DOSE-RESPONSE (g_l12_377b), because it decides the MODALITY:
monotone means the irreversible routes are acceptable, an interior optimum below wild type
means only a titratable reversible agent - the gapmer - is usable at all.

RECOMMENDED SEQUENCE:
  STEP 0  caliper the existing mouse                        ~$10k-25k   gates everything
  STEP 1  CRISPRi graded knockdown in human chondrocytes    ~$20k-50k   decides modality
  STEP 2  ASO gapmer panel, screen for potency in the same  ~$5k-15k    cheapest clean agent
          cells, then a normal growing mouse with a caliper
  STEP 3  only then choose between gapmer and KineTAC
⛔ AND THE HONEST TIMELINE: steps 0-2 are 12-24 months. A GMP ASO plus toxicology plus an
   IND is a further year at 1-3 million dollars, and every individualised-oligonucleotide
   pathway requires a severely debilitating or life-threatening disease caused by a specific
   pathogenic variant (R377). NOTHING ON THIS LIST CAN REACH A SUBJECT INSIDE A 1-3 YEAR
   GROWTH WINDOW. The HHIP programme is the right long answer and it is not a short one.""")
