#!/usr/bin/env python3
"""
THE NPR-C MOLECULE-CLASS QUESTION, SETTLED - and round 209's proposed resolution
is REFUTED by a paper this atlas has been holding, unread, since 2026-08-08.

WHY THIS TOOL EXISTS
--------------------
Round 209 ranked NPR3 blockade by LIGAND OCCUPANCY as the strongest addition to
the stack and left exactly one blocker in the way. NPR-C is bifunctional: a
clearance sink in cartilage (which growth wants silenced) and a Gi-coupled
receptor through which CNP protects the aorta (which safety wants active). Round
209 proposed a way through - that an ANTAGONIST silences both arms but an
OCCUPYING NATURAL LIGAND might block clearance while ENGAGING Gi - and graded
that proposition E, the central untested claim of the round.

IT IS NO LONGER UNTESTED. smith2022 tested it directly, in a human-NPR-C
functional cAMP assay and in two vessel preparations, and used OSTEOCRIN ITSELF
as its antagonist tool compound.

THE PROCESS FAILURE IS WORTH RECORDING. smith2022 was added to this bibliography
on 2026-08-08 with cited_by 0 and was never opened. Round 209 was written on
2026-08-10 and spent its main contribution constructing a hypothesis that the
held paper had already refuted. The user's standing instruction - "remember to
record every study you had better cause you loose them sometimes" - was earned.
"""

# ------------------------------------------------------------------ the assay
# smith2022, human NPR-C in HeLa cells, forskolin 10 uM, IBMX 1 mM, 10 min
# preincubation. NPR-C carries a Gi binding domain; agonism LOWERS cAMP.
CAMP_ASSAY = [
    ("cANF(4-23)", "100 nM", "AGONIST",
     "clear decrease in forskolin-stimulated cAMP; reversed by M372049 and by osteocrin"),
    ("compound 1 (bis-aminotriazine)", "100 uM", "AGONIST",
     "cAMP inhibited 37.67 per cent; reversed by M372049 and by osteocrin"),
    ("compound 17", "100 uM", "AGONIST", "cAMP inhibited 31.43 per cent"),
    ("compound 26", "100 uM", "weak", "cAMP inhibited 20.65 per cent, trend not significant"),
    ("compound 41", "100 uM", "BINDER, NOT ACTIVATOR",
     "cAMP inhibited 9.16 per cent - binds NPR-C but does not activate it"),
    ("M372049", "10 uM", "ANTAGONIST",
     "does NOT affect basal forskolin-induced cAMP; blocks the agonists"),
    ("OSTEOCRIN", "100 nM", "ANTAGONIST",
     "does NOT affect basal forskolin-induced cAMP; blocks the agonists - SAME "
     "FUNCTIONAL CLASS AS M372049 ON THIS READOUT"),
]

# ---------------------------------------------------------------- organ baths
VESSELS = [
    ("rat aorta", "cANF(4-23) causes vasorelaxation; BLOCKED by M372049 AND BY OSTEOCRIN"),
    ("rat small mesenteric artery",
     "cANF(4-23) vasorelaxation BLOCKED by M372049 and by osteocrin; compound 1 "
     "partially blocked, and 6.4-fold less potent in NPR-C-knockout tissue"),
]

# --------------------------------------------------- what osteocrin DOES do
# three independent in vivo models, all routed through LIGAND ABUNDANCE, not Gi
OSTN_IN_VIVO = [
    ("szaroszyk2022", "mouse, pressure overload",
     "skeletal-muscle-specific Ostn knockout EXAGGERATES and Ostn overexpression "
     "ATTENUATES cardiac dysfunction and myocardial fibrosis; mechanism stated as "
     "musclin enhancing CNP ABUNDANCE, promoting cardiomyocyte contractility via PKA "
     "and inhibiting fibroblast activation via PKG. OSTN also reduced in skeletal "
     "muscle of human heart failure patients"),
    ("harris2023", "mouse, exercise then ex vivo ischaemia-reperfusion",
     "Ostn disruption ABOLISHES exercise-induced cardioprotection, with blunted cGMP, "
     "reduced nuclear PKGI and CREB and suppressed PGC1alpha"),
    ("saw2025", "mouse HFpEF (SAUNA model) plus human HFpEF muscle",
     "exogenous musclin POTENTIATED natriuretic peptide signalling in skeletal muscle - "
     "increased PKG1 activity and PGC-1alpha"),
    ("scott2024", "conscious normal sheep, incremental IV proOSTN",
     "plasma ANP, BNP and CNP all rose with cGMP; arterial and central venous pressure "
     "fell; PLASMA cAMP, RENIN AND ALDOSTERONE UNCHANGED"),
]

# ------------------------------------------------------- the cartilage inversion
# every NPR3-axis height observation on record has the Gi arm OFF
GI_OFF_HEIGHT_DATA = [
    ("weber2025", "mouse", "Npr3-null: max hypertrophic cell height in the axis of "
     "elongation ~20 per cent above wild-type littermates; disproportionate elongation "
     "of proximal and mid-tail vertebrae via an expanded hypertrophic zone AND larger "
     "hypertrophic cells", "receptor absent - NO clearance, NO Gi"),
    ("lauffer2022 / boudin2018", "human", "biallelic NPR3 loss of function, +3.03 to "
     "+4.76 SDS, proband 205.1 cm", "receptor absent - NO clearance, NO Gi"),
    ("kanai2017", "mouse", "raised circulating OSTN gives dose-dependent skeletal "
     "overgrowth; CNP x OSTN double transgenics gain bone length over elevated CNP alone",
     "receptor OCCUPIED BY A SILENT LIGAND - no clearance, no Gi (smith2022)"),
]

# the human natural experiment for LOWERED chondrocyte cAMP, already in this atlas
PDE3A = ("PDE3A gain-of-function (Bilginturan, hypertension with brachydactyly type E) "
         "lowers PTH1R-driven chondrocyte cAMP and produces SHORTENED METACARPALS AND "
         "SHORT STATURE, attributed to accelerated chondrocyte maturation "
         "(maass2015; atlas node pde3a, confidence D)")

# ------------------------------------------------------------ the human anchor
# schn2026, HARP/HARA cohorts, serum musclin by ELISA, LMS medians (ng/ml)
MUSCLIN_P50 = {0: 3.762, 4: 4.013, 8: 4.267, 12: 4.527, 16: 4.792, 18: 4.924,
               30: 5.589}


def rule(c="="):
    print(c * 92)


def main():
    rule()
    print("ROUND 211 - DOES OCCUPANCY PRESERVE THE Gi ARM? NO. AND THE ANSWER INVERTS")
    print("THE COMPOUND SPECIFICATION.")
    rule()

    print("\n[1] THE DIRECT TEST, WHICH THIS ATLAS ALREADY OWNED")
    print("    smith2022, human NPR-C in HeLa, forskolin-stimulated cAMP.")
    print("    NPR-C carries a Gi binding domain; ENGAGING IT LOWERS cAMP.\n")
    for mol, conc, cls, eff in CAMP_ASSAY:
        print(f"\n    {mol:<32}{conc:<10}{cls}")
        for i in range(0, len(eff), 82):
            print(f"        {eff[i:i+82]}")
    print("\n    OSTEOCRIN AT 100 nM IS SILENT ON cAMP AND BLOCKS THE AGONISTS. On the Gi")
    print("    readout it is in the SAME functional class as M372049 - the very antagonist")
    print("    round 209 said it would differ from.")

    print("\n[2] AND IT BLOCKS NPR-C VASORELAXATION IN TWO VESSEL PREPARATIONS")
    for v, res in VESSELS:
        print(f"    {v}")
        print(f"        {res}")

    print("\n[3] SO ROUND 209's CENTRAL PROPOSITION IS REFUTED")
    rule("-")
    print("    CLAIMED (grade E): 'an occupying NPR-C ligand preserves the Gi arm that an")
    print("    antagonist would block.'")
    print("    OBSERVED: osteocrin neither engages Gi nor preserves it. It occupies the")
    print("    receptor silently and prevents anything else from engaging it.")
    print("    THE MOLECULE-CLASS DISTINCTION ROUND 209 DREW IS REAL, BUT OSTEOCRIN IS ON")
    print("    THE WRONG SIDE OF IT. The classes are SILENT OCCUPIER (osteocrin, M372049,")
    print("    compound 23, compound 41) against OCCUPYING AGONIST (cANF(4-23), compound 1,")
    print("    compound 17) - and until now the atlas did not know the second class existed.")

    print("\n[4] BUT THE LIABILITY DOES NOT FOLLOW, BECAUSE OSTEOCRIN DOES NOT PHENOCOPY A NULL")
    rule("-")
    print("    The feared route was: block NPR-C, lose CNP's aortoprotection (aubdool2025).")
    print("    A GENETIC NULL loses the receptor. AN OCCUPIER RAISES THE LIGAND. Three")
    print("    independent in vivo models say the ligand-raising arm delivers cardiovascular")
    print("    benefit WITHOUT the Gi arm:")
    for ref, model, res in OSTN_IN_VIVO:
        print(f"\n    {ref}  [{model}]")
        print(f"        {res[:84]}")
        for i in range(84, len(res), 84):
            print(f"        {res[i:i+84]}")
    print("\n    WHAT IS STILL NOT MEASURED, AND IT IS THE EXACT ENDPOINT: aortic root or")
    print("    ascending aortic DIMENSION under osteocrin, in any species. Every osteocrin")
    print("    cardiovascular endpoint on record is myocardial, skeletal-muscle or")
    print("    haemodynamic. aubdool2025's lesion is STRUCTURAL and nobody has looked.")

    print("\n[5] THE INVERSION, WHICH IS THE REAL FINDING")
    rule("-")
    print("    Round 209 wanted a molecule that blocks the sink AND engages Gi. That")
    print("    molecule now demonstrably exists - cANF(4-23), and orally-relevant small")
    print("    molecules at the same site (smith2022 compound 1, EC50 ~1 uM, in vivo PK).")
    print("    THE ATLAS SHOULD PROBABLY NOT WANT IT.")
    print("\n    Gi engagement LOWERS cAMP. In chondrocytes cAMP is the PTHrP/PTH1R/Gs arm")
    print("    that HOLDS cells proliferative and DELAYS hypertrophy. The human natural")
    print("    experiment for lowering it is already in this atlas:")
    print(f"        {PDE3A[:86]}")
    for i in range(86, len(PDE3A), 86):
        print(f"        {PDE3A[i:i+86]}")
    print("\n    AND EVERY OBSERVATION OF NPR3-AXIS HEIGHT GAIN ON RECORD HAS THE Gi ARM OFF:")
    for ref, sp, res, state in GI_OFF_HEIGHT_DATA:
        print(f"\n        {ref} [{sp}] - {state}")
        print(f"            {res[:80]}")
        for i in range(80, len(res), 80):
            print(f"            {res[i:i+80]}")
    print("\n    THERE IS ZERO SKELETAL DATA WITH THE Gi ARM ON. Gi-OFF may be a REQUIREMENT")
    print("    of the height effect rather than a liability to be engineered away. If it is,")
    print("    the round-209 compound specification is backwards for the SECOND time, and")
    print("    osteocrin is the right molecule for the reason opposite to the one given.")

    print("\n[6] THE REAGENT THAT SEPARATES THE TWO ARMS ALREADY EXISTS")
    rule("-")
    print("    devotta2023 built HNPR3-deltaC - human NPR3 truncated by the 34 C-terminal")
    print("    residues carrying the Gi activator sequence. In Xenopus it RESCUES the")
    print("    clearance-dependent programme (neural crest) and FAILS to rescue the")
    print("    Gi-dependent one (cranial placode), which was independently confirmed by")
    print("    rescuing the latter with the adenylyl cyclase inhibitor SQ22536.")
    print("    A RECEPTOR THAT CLEARS BUT CANNOT SIGNAL. Knocked into a mouse it answers")
    print("    both halves at once - whether the aortic lesion is the Gi arm or the ligand,")
    print("    and whether the height effect survives with clearance intact.")

    print("\n[7] THE HUMAN CONCENTRATION ANCHOR, AND WHY DOSING IS ELEVATION NOT RESTORATION")
    rule("-")
    print("    schn2026, 399 children and 502 adults, serum musclin by ELISA, LMS medians:")
    for age, v in MUSCLIN_P50.items():
        print(f"        age {age:>2} y   P50 {v:.3f} ng/ml")
    lo, hi = MUSCLIN_P50[0], MUSCLIN_P50[18]
    print(f"\n    Birth to 18 years the median rises {hi/lo:.2f}-fold - MONOTONIC AND SHALLOW -")
    print("    while height velocity over the same span falls by roughly an order of")
    print("    magnitude. ENDOGENOUS MUSCLIN DOES NOT TRACK GROWTH RATE. There is no")
    print("    physiological surge to restore, so any osteocrin dosing is ELEVATION above a")
    print("    normal baseline, which CORR-203 makes the harder claim to support. It also")
    print("    means the therapeutic exposure must be supraphysiological by a wide margin -")
    print("    smith2022 used 100 nM to antagonise, against a paediatric median of ~4-5")
    print("    ng/ml. No sex association; oestrogen-containing oral contraceptives LOWER it.")

    print("\n[8] AND OSTEOCRIN IS NOT MONOGAMOUS")
    rule("-")
    print("    jin2023 - musclin binds TRANSFERRIN RECEPTOR 1 and ANTAGONISES Tfr1-mediated")
    print("    cAMP/PKA-dependent thermogenic induction in beige adipocytes, attenuating")
    print("    thermogenesis and exacerbating diet-induced obesity. A SECOND RECEPTOR the")
    print("    atlas did not have, and again a cAMP-LOWERING direction. Male mice only, so")
    print("    CORR-191 applies to the phenotype - though the endpoint is metabolic, not")
    print("    length.")

    print("\n[9] WHAT THIS DOES TO THE STACK")
    rule("-")
    print("    OSTEOCRIN STAYS THE TOP-RANKED ADDITION and the case for it is now BETTER")
    print("    SOURCED, not worse - its in vivo mechanism is confirmed to be ligand")
    print("    elevation, and three independent cardiovascular models find it protective")
    print("    rather than harmful. What changed is the REASON: the Gi arm is not preserved,")
    print("    it is silenced, and that may be exactly what cartilage needs.")
    print("    THE ANTAGONISTS - M372049 and nishizawa2017 compound 23 - MOVE UP, not down.")
    print("    They are in the same functional class as osteocrin on the Gi readout, so the")
    print("    round-209 reason for preferring the peptide over them has evaporated. Compound")
    print("    23 is 12,600-fold selective and serum-stable; osteocrin is a 50-residue")
    print("    peptide. On every other axis the small molecule is the easier agent.")
    print("    THE NPR-C AGONISTS ARE A NEW AND SEPARATE ARM - right for the aorta,")
    print("    predicted wrong for the plate, and untested on bone in any species.")
    rule()


if __name__ == "__main__":
    main()
