#!/usr/bin/env python3
"""
ERDAFITINIB AGAINST TYRA-300, SETTLED - and the answer is not the one the safety
literature implies.

WHY THIS TOOL EXISTS
--------------------
Round 208 noted in passing that "the atlas has been carrying the FGFR arm under
the wrong molecule" and left it there. The user asked for it settled. Almost
every piece was already in this bibliography and had never been put in one place.

THE QUESTION IS NOT WHICH DRUG IS SAFER. The user has explicitly deferred risk.
THE QUESTION IS WHICH MOLECULE DELIVERS MORE RETAINED ADULT HEIGHT - and on that
framing the deformity findings are YIELD terms, not safety terms, because a
kyphoscoliotic spine is shorter than a straight one and a forced discontinuation
truncates the treatment window.
"""

# ---------------------------------------------------------------- selectivity
# dabogratinib2026, Ba/F3 isoform-driven cell lines, author-stated fold values
SELECTIVITY = {
    "dabogratinib (TYRA-300)": {"FGFR3 over FGFR1": 63, "FGFR3 over FGFR2": 19,
                                "FGFR3 over FGFR4": 55},
}
PAN = ("erdafitinib, futibatinib, pemigatinib and infigratinib all retain LOW IC50 "
       "values in FGFR1-, FGFR2- and FGFR4-driven Ba/F3 lines - i.e. no meaningful "
       "FGFR3 selectivity at all (dabogratinib2026)")

# ------------------------------------------------------- what each receptor does
RECEPTORS = [
    ("FGFR3", "growth plate chondrocytes - mainly MATURE chondrocytes in human "
              "embryo-fetal long bone (delezoide1998)",
     "THE GROWTH TARGET. Gain-of-function shortens bone; inhibition lengthens it."),
    ("FGFR1", "PERICHONDRIUM and PERIOSTEUM in human fetal long bone "
              "(delezoide1998); kidney, where it regulates phosphate and calcium "
              "reabsorption (dabogratinib2026)",
     "INHIBITING IT WORKS AGAINST THE GOAL. Chondrocyte-specific Fgfr1 deletion gives "
     "REDUCED stature by P4 and REDUCED tibial length at P18 DESPITE an INCREASED "
     "hypertrophic zone (karolak2015) - the zone-up/length-down dissociation. Renal "
     "FGFR1 inhibition drives the hyperphosphataemia seen in >70 per cent of "
     "erdafitinib patients."),
    ("FGFR2", "perichondrium and periosteum (delezoide1998)", "structural, not the target"),
    ("FGFR4", "liver and elsewhere", "off-target; diarrhoea and other class effects"),
]

# ------------------------------------------------------------- the human data
HUMAN = [
    ("erdafitinib", "erdachild2024",
     "pre-pubescent boy, FGFR1-mutated glioma: 14.3 cm in 9 months = 19.06 cm/year "
     "annualised, with PRE-pubertal GH, IGF-I, IGFBP-3 and testosterone",
     "severe kyphoscoliosis, spinal cord compression and cervical myelopathy FORCED "
     "DISCONTINUATION; cranial vault (membranous bone) SPARED"),
    ("erdafitinib", "erdaseries2025",
     "retrospective series of paediatric CNS-tumour patients: unanticipated growth "
     "acceleration INDEPENDENT of sex steroids and of IGF1, with a DISTINCT WIDENING "
     "OF THE GROWTH PLATE and enhanced metaphyseal mineralisation",
     "children were heavily pretreated with SEVERE growth impairment before therapy - "
     "so an unknown share of this is CATCH-UP GROWTH"),
    ("erdafitinib", "nadeaunguyen2026",
     "FDA postmarketing review: FIVE paediatric cases of skeletal growth toxicity, "
     "median age 13, median time to onset 137 days",
     "ALL FIVE permanently discontinued; THREE required surgical correction. US label "
     "revised to add SCFE and ACCELERATED LINEAR GROWTH under Pediatric Use"),
    ("infigratinib", "savarirayan2026infig / propel3_2026",
     "phase 3 RCT, n=114, 2:1, oral 0.25 mg/kg/day: +1.74 cm/year annualised height "
     "velocity",
     "DOSED AT A FRACTION OF THE ONCOLOGY DOSE - the achondroplasia dose was chosen "
     "for tolerability, not for maximum growth"),
    ("TYRA-300", "tyra300_2025",
     "WILD-TYPE mice: naso-anal +7.3 per cent, femur +8.2, tibia +6.4 at 14 mg/kg, "
     "dose-dependent, WITH NO BODY-WEIGHT DIFFERENCE; lumbar vertebrae length up; "
     "skull and foramen magnum improved; hypertrophic chondrocytes LARGER and the "
     "plate MORE ORGANISED",
     "NO HUMAN GROWTH DATA OF ANY KIND. SURF301 is a phase I/II in ADULTS with "
     "urothelial carcinoma"),
]


def rule(c="="):
    print(c * 92)


def main():
    rule()
    print("ERDAFITINIB vs TYRA-300 - THE SELECTIVITY, AND WHY IT IS NOT A SAFETY POINT")
    rule()
    print("\n[1] THE NUMBERS")
    for drug, d in SELECTIVITY.items():
        print(f"    {drug}")
        for k, v in d.items():
            print(f"        {k:<22} {v}-fold")
    print(f"\n    {PAN}")
    print("\n    AND POTENCY ON TARGET IS NOT SACRIFICED - head to head in the UM-UC-14")
    print("    xenograft, dabogratinib 18 mg/kg once daily gave SLIGHTLY MORE tumour")
    print("    regression than erdafitinib 12.5 mg/kg twice daily.")

    print("\n[2] WHAT EACH RECEPTOR IS DOING IN A GROWING SKELETON")
    for name, where, why in RECEPTORS:
        print(f"\n    {name}")
        print(f"        located : {where}")
        print(f"        meaning : {why}")

    print("\n[3] THE MECHANISTIC ACCOUNT THIS ASSEMBLES, AND IT IS NEW TO THE ATLAS")
    print("    FGFR3 sits in the growth plate chondrocytes. FGFR1 and FGFR2 sit in the")
    print("    PERICHONDRIUM AND PERIOSTEUM - the fibrous ring that mechanically")
    print("    constrains the physis and carries the groove of Ranvier.")
    print("    A PAN-FGFR INHIBITOR THEREFORE DOES TWO THINGS AT ONCE: it accelerates")
    print("    the plate through FGFR3 AND it inhibits the ring that holds the plate")
    print("    together through FGFR1/2. That is precisely the recipe for a physis that")
    print("    grows fast and then fails mechanically - epiphysiolysis, slipped capital")
    print("    femoral epiphysis, kyphoscoliosis.")
    print("    AND karolak2015 SHOWS THE FGFR1 ARM ALSO WORKS AGAINST LENGTH DIRECTLY:")
    print("    chondrocyte Fgfr1 deletion gives a BIGGER hypertrophic zone and a SHORTER")
    print("    tibia. So in a pan-FGFR inhibitor the FGFR1 component is subtracting from")
    print("    the FGFR3 component while adding the structural failure.")

    print("\n[4] THE HUMAN EVIDENCE, WHICH IS WHERE THE SURPRISE IS")
    for drug, ref, effect, caveat in HUMAN:
        print(f"\n    {drug}  [{ref}]")
        print(f"        effect  : {effect}")
        print(f"        caveat  : {caveat}")

    print("\n[5] THE VERDICT")
    rule("-")
    print("    ERDAFITINIB IS THE LARGEST GROWTH EFFECT IN THIS ENTIRE ATLAS. 19.06")
    print("    cm/year annualised in a pre-pubertal child is roughly TEN TIMES the")
    print("    phase-3 infigratinib effect and TWELVE TIMES vosoritide's. Nothing else")
    print("    on record comes close, and it is HUMAN.")
    print("    IT IS ALSO SELF-LIMITING, AND ON YIELD GROUNDS RATHER THAN SAFETY ONES.")
    print("    Kyphoscoliosis shortens the spine. Spinal fusion ends spinal growth.")
    print("    Five of five discontinued permanently and three needed surgery. A drug")
    print("    that must be stopped at 137 days does not deliver adult height.")
    print("\n    THE SELECTIVITY ARGUMENT IS THEREFORE A YIELD ARGUMENT: 63-fold sparing")
    print("    of FGFR1 removes the receptor whose inhibition BOTH shortens bone AND")
    print("    weakens the perichondrial ring, while leaving the FGFR3 arm that produced")
    print("    the 19 cm/year intact.")
    print("\n    WHAT WOULD FALSIFY IT. If the growth acceleration itself is FGFR1- or")
    print("    perichondrium-mediated rather than FGFR3-mediated, an FGFR3-selective")
    print("    molecule would be safer AND weaker, and the trade would be a bad one.")
    print("    Two facts argue against that reading and neither is decisive: TYRA-300")
    print("    grows WILD-TYPE mice by 8.2 per cent at the femur with no body-weight")
    print("    change, and the erdafitinib child's CRANIAL VAULT - membranous bone with")
    print("    no growth plate - WAS SPARED, which localises the effect to endochondral")
    print("    tissue.")
    print("\n    THE DECISIVE UNKNOWN IS DOSE. Infigratinib gives +1.74 cm/year at 0.25")
    print("    mg/kg/day, a fraction of its oncology dose, chosen for tolerability.")
    print("    Erdafitinib gives 19 cm/year at full oncology dosing. NOBODY HAS DOSED AN")
    print("    FGFR3-SELECTIVE MOLECULE AT AN ONCOLOGY-SCALE EXPOSURE IN A GROWING")
    print("    SKELETON. That single experiment decides the whole arm.")
    rule()


if __name__ == "__main__":
    main()
