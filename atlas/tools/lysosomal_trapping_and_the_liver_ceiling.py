#!/usr/bin/env python3
"""
DOES ERDAFITINIB'S LYSOSOMAL TRAPPING BREAK ROUND 213's ARITHMETIC? AND CAN THE
LIVER CEILING ON TYRA-300 BE ROUTED AROUND?

WHY THIS TOOL EXISTS
--------------------
The user raised an objection to round 213 that the atlas had not considered:
erdafitinib is a lipophilic base with documented lysosomal accumulation, so its
effective tissue exposure may far exceed what free plasma predicts, and matching
free plasma concentration may not match target engagement. The objection is
legitimate and the underlying observation is confirmed by the discovery paper's
own abstract. THE CONCLUSION IT LEADS TO IS NOT THE ONE EITHER OF US EXPECTED.

TWO PREMISES OF THE OBJECTION NEED SEPARATING, BECAUSE ONE IS WRONG AND THE
OTHER IS RIGHT FOR A DIFFERENT REASON THAN GIVEN.
  - LIPOPHILICITY. The objection put erdafitinib well above dabogratinib. On the
    same calculators they are close, and PubChem currently puts dabogratinib
    HIGHER. This axis does not separate them.
  - BASICITY. This one separates them completely, and it is the axis that
    actually drives lysosomotropism. Erdafitinib carries a secondary aliphatic
    amine. Dabogratinib's only sp3 nitrogens sit in a diazaspiro ring with one
    nitrogen SULFONYLATED, which is not basic at all.
"""

import math

# ------------------------------------------------------------ physicochemistry
# PubChem computed (CID 67462786, 170647464); ChEMBL ALogP where available
CHEM = {
    "erdafitinib": {
        "MW": 446.5, "formula": "C25H30N6O2", "xlogp_pubchem": 3.2,
        "alogp_chembl": 4.18, "tpsa": 77.3, "hbd": 1, "rotb": 9,
        "basic_centre": "SECONDARY ALIPHATIC AMINE - the N-isopropyl of an "
                        "isopropylamino-ethyl arm, CC(C)NCCN<. Secondary "
                        "alkylamines sit near pKa 10; beta-nitrogen "
                        "substitution pulls it down toward 9",
        "charge_at_pH74": "MONOCATIONIC, essentially completely",
    },
    "dabogratinib (TYRA-300)": {
        "MW": 559.5, "formula": "C25H24Cl2N6O3S", "xlogp_pubchem": 3.6,
        "alogp_chembl": None, "tpsa": 113, "hbd": 1, "rotb": 6,
        "basic_centre": "NONE ABOVE pKa 5. The 2,6-diazaspiro[3.3]heptane has "
                        "one nitrogen carrying a METHANESULFONYL group, which "
                        "is not basic, and the other tied to a pyridine. The "
                        "remaining nitrogens are aromatic and the two chlorines "
                        "on the pyridine suppress even that basicity. The single "
                        "H-bond donor is the indazole NH, which is weakly ACIDIC",
        "charge_at_pH74": "NEUTRAL",
    },
    "PD173074 (reference lysosomotrope)": {
        "MW": 476.2, "formula": None, "xlogp_pubchem": 4.5,
        "alogp_chembl": 4.83, "tpsa": 50.4, "hbd": 2, "rotb": None,
        "basic_centre": "tertiary amine; ChEMBL pKa 10.12, logP at pH 7.4 = 5.16",
        "charge_at_pH74": "MONOCATIONIC",
    },
}

# ------------------------------------------------------------- the primary data
PERERA = ("perera2017, the erdafitinib DISCOVERY paper, states it directly in its "
          "own abstract: JNJ-42756493 shows RAPID UPTAKE INTO THE LYSOSOMAL "
          "COMPARTMENT of cells in culture, WHICH IS ASSOCIATED WITH PROLONGED "
          "INHIBITION OF FGFR SIGNALING, possibly due to sustained release of the "
          "inhibitor. The hedge - possibly - is theirs. THE USER IS RIGHT THAT THIS "
          "IS NOT AN EXTRAPOLATION FROM pKa AND logP; the developers observed it.")

ENGLINGER = [
    ("selective lysosomal accumulation", "confirmed by confocal against LysoTracker "
     "in two lung cancer lines using the compound's intrinsic fluorescence"),
    ("in silico prediction", "10.1-fold and 9.6-fold lysosome-over-cytoplasm from two "
     "parameter sets - so the modelled accumulation is about tenfold, not hundredfold"),
    ("persistence after washout", "after a 1-hour exposure and recovery in drug-free "
     "medium, PD173074 was STILL compartmentalised to lysosomes at 120 HOURS, "
     "dose-dependently"),
    ("AND THE DECISIVE ONE", "chloroquine co-incubation for 1 hour gave 14.29-fold "
     "against 2.78-fold suppression of phospho-ERK at 1 uM PD173074 - a 5.1-fold "
     "BETTER target hit - and rescued AKT inhibition entirely, 2.94-fold against "
     "0.76-fold at 1 uM and 3.45 against 1.03 at 10 uM. RAISING LYSOSOMAL pH MADE "
     "THE FGFR INHIBITOR SUBSTANTIALLY MORE POTENT AT ITS TARGET"),
]

# ------------------------------------------------------- ion-trapping arithmetic
PH_LYSO, PH_CYT = 4.7, 7.2


def trap_ratio(pka, ph_lo=PH_LYSO, ph_hi=PH_CYT):
    """Free-base equilibration -> total-concentration ratio between compartments."""
    return (1 + 10 ** (pka - ph_lo)) / (1 + 10 ** (pka - ph_hi))


def frac_in_lysosome(ratio, f_lyso):
    return ratio * f_lyso / (ratio * f_lyso + (1 - f_lyso))


# ------------------------------------------------------- cartilage Donnan uptake
def donnan_cation(fcd_M, salt_M=0.15):
    """Monovalent cation partition into a matrix of fixed charge density fcd_M."""
    c_in = (fcd_M + math.sqrt(fcd_M ** 2 + 4 * salt_M ** 2)) / 2
    return c_in / salt_M


# ----------------------------------------------------------------- liver options
LIVER = [
    ("1. FIND OUT IF IT IS EXPOSURE-DEPENDENT. COSTS NOTHING.",
     "SURF301 has individual steady-state AUC in 34 patients and ALT in all 41. "
     "Plot one against the other. An exposure-response makes the transaminitis a "
     "concentration effect and it sets the ceiling; a flat scatter makes it "
     "idiosyncratic and it becomes a monitoring problem, not a dose problem. "
     "EVERYTHING BELOW DEPENDS ON THIS ANSWER AND NOBODY HAS PUBLISHED IT.",
     "the data exists today"),
    ("2. THE BID ARMS ARE THE MOST VALUABLE UNREPORTED DATASET IN THE PROGRAMME.",
     "SURF301 ran 40, 50 and 60 mg TWICE DAILY and the ENA presentation reports only "
     "the QD arms. If the transaminitis is Cmax-driven, BID at matched AUC lowers "
     "Cmax and may clear it. AND BID IS WHAT A GROWTH PLATE WANTS ANYWAY - the QD "
     "profile at 90 mg spends part of each day nearer the FGFR3 IC90 line, while a "
     "physis is integrating continuously. BID could buy trough coverage AND liver "
     "headroom at once.",
     "the data exists today"),
    ("3. TEST WHETHER IT IS THE TFEB MECHANISM, BECAUSE THERE IS A NAMED ANTIDOTE.",
     "qiu2026 dissected osimertinib hepatotoxicity - the drug DEPHOSPHORYLATES TFEB, "
     "which translocates to the nucleus, drives autophagy and lysosome biogenesis, and "
     "kills hepatocytes through vacuolation. They then identify S-ADENOSYL-L-METHIONINE "
     "as a clinical hepatoprotective agent that mitigates it BY INHIBITING TFEB "
     "ACTIVATION. SAMe is licensed for liver indications in several countries and is "
     "otherwise a supplement. THE PREDICTION CUTS AGAINST ITSELF, WHICH IS WHY IT IS "
     "WORTH TESTING - TYRA-300 is NOT lysosomotropic, so if its transaminitis is still "
     "TFEB-driven then TFEB activation is not a lysosomotropism phenomenon and the "
     "antidote generalises. Nuclear TFEB and vacuolation in primary human hepatocytes "
     "is a two-week experiment.",
     "new bench work, small"),
    ("4. CARTILAGE-TARGETED DELIVERY IS THE ONLY OPTION THAT REMOVES THE CEILING "
     "RATHER THAN RAISING IT.",
     "ye2026, already held here, delivered a hedgehog agonist SYSTEMICALLY to growth "
     "plate cartilage using chondrocyte-membrane-coated collagen-II-targeting "
     "nanoparticles and raised body length. Any liver ceiling is a ratio problem - it "
     "binds only because cartilage and hepatocyte see the same plasma. A carrier that "
     "raises the cartilage-to-liver ratio raises the attainable FGFR3 coverage without "
     "touching the liver dose. THE OBJECTION IS THAT ye2026 REPORTS DELIVERY ONLY AS "
     "NORMALISED FLUORESCENCE - no absolute concentration, no AUC, no half-life - so "
     "the ratio it achieves is unknown and might be 1.5-fold.",
     "published platform, unquantified"),
    ("5. THE LYSOSOME-ALKALINISER TRICK, AND WHY IT PROBABLY DOES NOT WORK HERE.",
     "englinger2018's chloroquine result is the most striking number in this file - "
     "5.1-fold better target suppression at the same drug concentration. Applied to "
     "erdafitinib it would mean the same FGFR3 inhibition at a LOWER dose, hence less "
     "FGFR2 epithelial toxicity, hence a higher ceiling. THREE THINGS AGAINST IT. It is "
     "a 1-hour co-incubation, which is not steady state, and the steady-state argument "
     "below says the effect should shrink. It would raise cytosolic erdafitinib in the "
     "nail bed and oral mucosa too, which is where the dose is actually lost. And it "
     "does nothing for TYRA-300, which is not lysosomotropic in the first place.",
     "cheap to test, weak prior"),
    ("6. THE BIOLOGICS ROUTE HAS NO LIVER PROBLEM AND A WORSE PROBLEM.",
     "yang2024 built a tetravalent bispecific antibody that selectively inhibits diverse "
     "FGFR3 oncogenic variants. An antibody has no hepatic metabolism and perfect isoform "
     "selectivity. IT ALSO CANNOT ENTER CARTILAGE - the matrix excludes large solutes and "
     "growth plate cartilage is avascular. A LIGAND TRAP IS DIFFERENT AND THIS DISTINCTION "
     "MATTERS: a soluble FGFR3 decoy works by removing FGF from the extracellular space "
     "and never has to reach the chondrocyte surface at depth. That is the one biologic "
     "geometry that is not obviously excluded.",
     "route open for decoys, closed for receptor antibodies"),
    ("7. AND THERE IS A FOURTH MOLECULE WITH THE ONLY JUVENILE THERAPEUTIC INDEX ANYONE "
     "HAS MEASURED.",
     "ozaki2020 evaluated ASP5878 specifically FOR ACHONDROPLASIA and reported it in AUC "
     "terms, which nobody else does - bone elongation in achondroplasia model MALE mice at "
     "300 microgram/kg, an AUC of 275 ng.h/mL in juvenile mice; minimal adverse effect, "
     "VERY SLIGHT CORNEAL EPITHELIAL ATROPHY, at an AUC of 459 ng.h/mL in juvenile rats. "
     "THAT IS A 1.67-FOLD WINDOW AND IT IS THE ONLY ONE ON RECORD IN A GROWING ANIMAL. "
     "It was also LESS effective at bone elongation than a CNP analogue, and the sex "
     "constraint applies - male mice only.",
     "published, and the window is narrow"),
]


def rule(c="="):
    print(c * 92)


def main():
    rule()
    print("LYSOSOMAL TRAPPING, CARTILAGE ACCESS, AND THE LIVER CEILING")
    rule()

    print("\n[1] THE PHYSICOCHEMISTRY, AND WHICH AXIS ACTUALLY SEPARATES THEM")
    for name, d in CHEM.items():
        print(f"\n    {name}")
        print(f"        MW {d['MW']}   TPSA {d['tpsa']}   HBD {d['hbd']}   "
              f"XLogP(PubChem) {d['xlogp_pubchem']}   ALogP(ChEMBL) {d['alogp_chembl']}")
        print(f"        charge at pH 7.4: {d['charge_at_pH74']}")
        for i in range(0, len(d['basic_centre']), 80):
            print(f"          {d['basic_centre'][i:i+80]}")
    print("\n    LIPOPHILICITY DOES NOT SEPARATE THEM. PubChem currently gives erdafitinib")
    print("    XLogP 3.2 and dabogratinib 3.6 - dabogratinib is the HIGHER of the two on")
    print("    that calculator. ChEMBL's ALogP puts erdafitinib at 4.18, close to the 4.3")
    print("    the objection quoted, but dabogratinib is not in ChEMBL so the pair cannot")
    print("    be compared on one algorithm. THE OBJECTION'S logP PREMISE DOES NOT HOLD.")
    print("\n    BASICITY SEPARATES THEM COMPLETELY, AND THAT IS THE AXIS THAT MATTERS.")
    print("    Lysosomotropism requires a base that is neutral enough at pH 7.4 to cross a")
    print("    membrane and protonated at pH 4.7 to be stranded. Erdafitinib has exactly")
    print("    that group. Dabogratinib's corresponding nitrogen is CAPPED WITH A")
    print("    METHANESULFONYL, which removes its basicity entirely. THE CONCLUSION THE")
    print("    OBJECTION REACHED IS CORRECT AND THE REASON GIVEN FOR IT IS NOT.")
    print("\n    TPSA IS THE SECOND REAL DIFFERENCE AND IT POINTS THE SAME WAY - 77.3 for")
    print("    erdafitinib against 113 for dabogratinib. Above roughly 90 square angstroms,")
    print("    passive membrane permeability falls off. For an AVASCULAR tissue reached only")
    print("    by diffusion, that is directionally against dabogratinib.")

    print("\n[2] THE OBSERVATION IS PRIMARY, NOT INFERRED")
    rule("-")
    for i in range(0, len(PERERA), 88):
        print(f"    {PERERA[i:i+88]}")

    print("\n[3] AND AN INDEPENDENT GROUP DISSECTED THE SAME PHENOMENON IN ANOTHER FGFR")
    print("    INHIBITOR AND CONCLUDED THE OPPOSITE ABOUT WHAT IT MEANS")
    rule("-")
    for k, v in ENGLINGER:
        print(f"\n    {k}")
        for i in range(0, len(v), 84):
            print(f"        {v[i:i+84]}")
    print("\n    SO THE LITERATURE CONTAINS BOTH READINGS OF THE SAME PHYSICS. perera2017")
    print("    calls it a DEPOT that prolongs inhibition. englinger2018 calls it a SINK")
    print("    that blunts inhibition and shows a 5.1-fold gain from emptying it.")

    print("\n[4] THE ARITHMETIC THAT RECONCILES THEM, AND IT DECIDES THE ROUND")
    rule("-")
    print(f"    Ion trapping between lysosome (pH {PH_LYSO}) and cytosol (pH {PH_CYT}):\n")
    print(f"        {'pKa':>5}{'lyso:cyt ratio':>18}{'% of soluble cell drug in lysosomes':>40}")
    print(f"        {'':>5}{'':>18}{'f=1%':>13}{'f=3%':>13}{'f=5%':>13}")
    for pka in (7.0, 8.0, 9.0, 9.5, 10.0, 11.0):
        r = trap_ratio(pka)
        cells = "".join(f"{frac_in_lysosome(r, f)*100:>12.0f}%" for f in (0.01, 0.03, 0.05))
        print(f"        {pka:>5.1f}{r:>18.0f}{cells}")
    print(f"\n    The ratio saturates at 10^(pH_cyt - pH_lyso) = {10**(PH_CYT-PH_LYSO):.0f}-fold once the")
    print("    pKa clears the lysosomal pH, so anything above about pKa 8 behaves the same.")
    print("    A DABOGRATINIB WITH NO BASIC CENTRE HAS A RATIO OF 1. IT DOES NOT PARTICIPATE.")

    print("\n    NOW THE PART THAT MATTERS AND THAT NEITHER PAPER STATES. AT STEADY STATE")
    print("    THE LYSOSOME IS A CAPACITOR, NOT A RESISTOR. The neutral species crosses")
    print("    membranes freely, so at equilibrium the neutral concentration is the SAME in")
    print("    plasma water, cytosol and lysosomal lumen. Cytosolic TOTAL concentration is")
    print("    therefore fixed by the extracellular free concentration and the cytosolic pH")
    print("    ALONE - it does not depend on how much drug the lysosomes hold. The lysosome")
    print("    fills from the same neutral pool; it does not drain the cytosol.")
    print("\n    CONSEQUENCE ONE, AND IT DEFENDS ROUND 213. On continuous once-daily dosing")
    print("    with a 59-hour half-life, erdafitinib is at steady state permanently. There")
    print("    is never a washout, so the depot never releases into a falling gradient and")
    print("    the sink is already full. THE FREE-PLASMA COMPARISON IN ROUND 213 SURVIVES:")
    print("    4.01x for the child who grew 19 cm/year, 4.33x for TYRA-300 at 90 mg.")
    print("\n    CONSEQUENCE TWO, AND IT BREAKS SOMETHING I WROTE YESTERDAY. Round 213 opened")
    print("    a gap asking for the GROWTH PLATE CONCENTRATION of each drug, to be measured")
    print("    by LC-MS on microdissected cartilage. THAT MEASUREMENT WOULD BE MISLEADING.")
    print("    A lysosomotropic drug shows a large TOTAL tissue concentration that is mostly")
    print("    locked in an organelle on the wrong side of a membrane from the kinase. The")
    print(f"    table above says {frac_in_lysosome(trap_ratio(9.5), 0.03)*100:.0f} per cent of soluble intracellular erdafitinib "
          "sits in")
    print("    lysosomes at a 3 per cent lysosomal volume fraction. Erdafitinib would read")
    print("    an order of magnitude higher than dabogratinib in cartilage with NO difference")
    print("    in target engagement. THE GAP HAS TO SPECIFY A FREE OR CYTOSOLIC MEASUREMENT,")
    print("    or pair the concentration with a pERK readout by zone. CORR-208.")

    print("\n[5] WHERE THE OBJECTION IS RIGHT, AND ROUND 213 WAS WRONG TO ASSUME PARITY")
    rule("-")
    print("    THE CARTILAGE MATRIX IS NOT A NEUTRAL COMPARTMENT. Growth plate cartilage")
    print("    carries a high fixed negative charge from glycosaminoglycan sulfates and")
    print("    carboxylates. A cation partitions INTO it by Donnan equilibrium. Erdafitinib")
    print("    is monocationic at pH 7.4; dabogratinib is neutral and gets nothing.\n")
    print(f"        {'fixed charge density':>24}{'monovalent cation partition':>30}")
    for fcd in (0.05, 0.10, 0.15, 0.20, 0.25):
        print(f"        {fcd:>21.2f} M{donnan_cation(fcd):>29.2f}x")
    print("\n    So the Donnan term buys erdafitinib roughly 1.4 to 2.1-fold in the matrix")
    print("    water. REAL, MODEST, AND ENTIRELY ABSENT FOR DABOGRATINIB. Add the TPSA")
    print("    difference and the direction is consistent. THIS IS THE OBJECTION'S STRONGEST")
    print("    FORM AND ROUND 213 SIMPLY ASSUMED IT AWAY.")
    print("\n    AND THERE IS A SECOND, LARGER ASYMMETRY NOBODY HAS RAISED. CARTILAGE IS")
    print("    AVASCULAR. Drug arrives by diffusion over hours from the perichondrial and")
    print("    metaphyseal margins - which is precisely the NON-steady-state regime where")
    print("    englinger2018's sink argument bites. Chondrocytes near the margin would load")
    print("    their lysosomes first and buffer drug out of the interstitial fluid before it")
    print("    reaches the cells at depth. THE TWO EFFECTS HAVE OPPOSITE SIGNS IN CARTILAGE")
    print("    SPECIFICALLY - charge pulls erdafitinib in, chondrocyte lysosomes near the")
    print("    edge hold it up - and the net is unmeasured in any species.")

    print("\n[6] THE ONE PLACE THE DEPOT IS UNAMBIGUOUSLY AN ADVANTAGE, AND IT IS THE")
    print("    REGIMEN THE CHILD ACTUALLY RECEIVED")
    rule("-")
    print("    The index child ran 7 mg WITH FREQUENT INTERRUPTIONS FOR HYPERPHOSPHATAEMIA.")
    print("    Interruption is exactly the falling-gradient condition in which a lysosomal")
    print("    depot releases and a 59-hour half-life is extended further. englinger2018")
    print("    found lysosomal compartmentalisation still present 120 HOURS after a 1-hour")
    print("    exposure. SO ERDAFITINIB'S REAL GROWTH-PLATE COVERAGE DURING AN INTERRUPTED")
    print("    SCHEDULE WAS BETTER THAN THE STEADY-STATE CALCULATION IMPLIES, AND")
    print("    DABOGRATINIB WOULD NOT HAVE THAT PROPERTY. Round 213 did not see this and it")
    print("    is a genuine point for erdafitinib - on an intermittent schedule, not a")
    print("    continuous one.")

    print("\n[7] THE LIVER, RANKED BY WHAT IT COSTS TO FIND OUT")
    rule("-")
    for title, body, cost in LIVER:
        print(f"\n    {title}")
        for i in range(0, len(body), 84):
            print(f"        {body[i:i+84]}")
        print(f"        [{cost}]")

    print("\n[8] THE VERDICT ON BOTH QUESTIONS")
    rule("-")
    print("    ON LYSOSOMES. The observation is real and primary, the logP premise is wrong,")
    print("    the basicity premise is right, and the steady-state arithmetic says it does")
    print("    NOT overturn round 213's free-plasma comparison under continuous dosing. What")
    print("    it does overturn is the measurement round 213 proposed to validate that")
    print("    comparison, and it exposes a cartilage-access asymmetry - Donnan uptake and")
    print("    lower polar surface area - that round 213 assumed away and that favours")
    print("    erdafitinib by an unmeasured amount. IT ALSO GIVES ERDAFITINIB A REAL")
    print("    ADVANTAGE ON AN INTERRUPTED SCHEDULE, WHICH IS THE SCHEDULE IT WAS GIVEN ON.")
    print("\n    ON THE LIVER. Route around it rather than through it, and in this order -")
    print("    read the exposure-response that already exists, then report the BID arms that")
    print("    already exist, then test TFEB because there is a named antidote, then invest")
    print("    in cartilage targeting because that is the only move that removes the ceiling")
    print("    instead of raising it. DO NOT PICK A HEPATOPROTECTANT BEFORE KNOWING WHETHER")
    print("    THE INJURY IS EXPOSURE-DEPENDENT, because if it is, the answer is a dose or a")
    print("    schedule and no supplement changes that.")
    rule()


if __name__ == "__main__":
    main()
