#!/usr/bin/env python3
"""ROUND 222 - three supplied documents; the patent answers ask #1 and the answer is NO ARM.

WHAT THIS ROUND CLOSES
----------------------
ASK #1 (rounds 219 and 221): does Tat-Beclin 1 lengthen a WILD-TYPE bone, or only
restore a deficient one? The Nature paper's Extended Data was out of reach. The
inventors' own patent - WO 2017/055370 A1, Fondazione Telethon, Settembre and
Cinque among the inventors - contains the same panel, and it settles it: THE
WILD-TYPE TREATMENT ARM WAS NEVER RUN.

ASK #4 (round 221): the Breinholt mouse bolus-versus-infusion magnitudes, which
round 221 could only state as "significantly more". The published JPET version
carries Table 5.

HOW FIGURE 17 WAS READ
----------------------
The patent PDF is image-only. It was OCRed for text and Figure 17 was read from a
300-dpi render of the quadrant containing it. Bar heights below are read against
the printed axis and are good to about +/- 2 percentage points. THE ARM COUNT IS
NOT AN ESTIMATE - the legend lists three keys and the panels show three bars.
"""
W = 92
def rule(c="="): print(c * W)
def head(n, t):
    print(); rule(); print(f"[{n}] {t}"); rule("-")
def wrap(s, ind=4):
    out, line = [], ""
    for w in s.split():
        if len(line) + len(w) + 1 > W - ind:
            out.append(" " * ind + line); line = w
        else:
            line = (line + " " + w).strip()
    if line: out.append(" " * ind + line)
    return "\n".join(out)

# ----------------------------------------------------------------------------- 1
head(1, "ASK #1, ANSWERED - THERE IS NO WILD-TYPE TAT-BECLIN 1 ARM, IN THE PAPER OR THE PATENT")
print(wrap(
    "WO 2017/055370 A1, Figure 17 f-h. The legend lists exactly THREE keys and the panels show "
    "exactly THREE bars:"))
print()
print("        [ ]  Fgfr4 +/+  vehicle")
print("        [#]  Fgfr4 -/-  vehicle")
print("        [/]  Fgfr4 -/-  Tat-Beclin 1")
print()
print("      panel                       +/+ vehicle   -/- vehicle   -/- Tat-Beclin1   sig")
for a, b, c, d, e in [("f  collagen amount (%)", "~100", "~65", "~90", "** (-/- vs -/-)"),
                      ("g  femur length P9 (%)", "~100", "~89", "~97", "*  (-/- vs -/-)"),
                      ("h  femur length P15 (%)", "~100", "~93", "~98", "** both")]:
    print(f"      {a:<27s} {b:>11s}   {c:>11s}   {d:>15s}   {e}")
print()
print(wrap(
    "THE TREATED NULL LANDS JUST BELOW THE WILD-TYPE BAR AND NEVER ABOVE IT, AND THE WILD-TYPE "
    "ANIMAL WAS NEVER TREATED. This is RESTORATION, definitively, and CORR-203 makes ELEVATION "
    "above a normal baseline the claim this case needs. The elevation experiment has not been run "
    "by the laboratory that discovered the mechanism, in the paper, or in the patent they filed on "
    "it - which is where a company puts every result it has."))
print()
print(wrap(
    "AND THE PATENT'S OWN NUMBERS SUGGEST WHY THERE MAY BE NO HEADROOM. The Fgfr4-null deficit is "
    "35 per cent on COLLAGEN and only 7 to 11 per cent on LENGTH, and Tat-Beclin 1 recovers "
    "collagen to about 90 per cent while recovering length to 97-98. The length response to "
    "collagen is strongly saturating near the wild-type point, so an agent that adds collagen to "
    "an animal already at 100 per cent may buy nothing. THAT IS A PREDICTION, NOT A RESULT, and it "
    "is the reason the wild-type arm is worth running rather than assuming."))

# ----------------------------------------------------------------------------- 2
head(2, "AND THE SAME PATENT KILLS ITS OWN SECOND COMPOUND CLASS, IN ITS OWN BACKGROUND")
print(wrap(
    "The patent claims three activator classes: A BECLIN 1 PEPTIDE, AN mTORC1 INHIBITOR, or A BH3 "
    "MIMETIC. The mTORC1 list is explicit - rapamycin, KU0063794, WYE354, deforolimus, Torin 1, "
    "Torin 2, temsirolimus, everolimus, sirolimus, NVP-BEZ235, PI103."))
print()
print(wrap(
    "ITS OWN BACKGROUND SECTION THEN CITES THREE SOURCES SHOWING mTORC1 INHIBITORS REDUCE "
    "LONGITUDINAL GROWTH. This atlas retrieved two of them independently:"))
print()
gr_rapa, gr_ctrl = 94.0, 182.0
print(f"      alvarezgarcia2007 - 4-week-old male rats, rapamycin 2 mg/kg/day IP for 14 days:")
print(f"        bone longitudinal growth rate {gr_rapa:.0f} +/- 3 against {gr_ctrl:.0f} +/- 3 um/day"
      f"  =  {100*(1-gr_rapa/gr_ctrl):.0f} PER CENT REDUCTION")
print(f"        with disturbed maturation and hypertrophy and decreased cartilage resorption,")
print(f"        and body weight gain 60.2 against 113.6 g")
print(f"      hymes2011 - paediatric renal transplant recipients on sirolimus: significantly lower")
print(f"        growth velocity in cm/year and smaller change in height SDS at 6, 12 and 24 months")
print()
print(wrap(
    "SO THE mTORC1 BRANCH IS DEAD FOR THIS PURPOSE AND IT IS DEAD ON HUMAN AND RAT GROWTH DATA, "
    "NOT ON THEORY. Rapamycin at the SAME 2 mg/kg/day intraperitoneal dose cinque2015 used for "
    "Tat-Beclin 1 HALVES growth plate elongation in a growing rat. An autophagy activator is not a "
    "class - the route matters more than the endpoint, and mTORC1 inhibition buys autophagy by "
    "shutting down the anabolic programme that a growing chondrocyte needs."))
print()
print(wrap(
    "NOTE ON PROVENANCE. The patent's third citation is Gonzalez et al., Pediatr Nephrol 2010, "
    "which this atlas has NOT retrieved; hymes2011 is an independent report of the same direction "
    "and is what is cited here. addref.py refused the entry when it was first filed under the "
    "wrong first author, which is the tool working as intended."))
print()
print(wrap(
    "THE THIRD CLASS - BH3 MIMETICS (ABT-737, ABT-263/navitoclax, obatoclax, gossypol, AT-101, "
    "apogossypol, ApoG2, sabutoclax) - IS CLAIMED WITH NO BONE DATA ANYWHERE IN THE PATENT. It is "
    "a mechanistic extrapolation from Beclin 1 being sequestered by Bcl-2, and it is recorded as "
    "an open question rather than a candidate."))

# ----------------------------------------------------------------------------- 3
head(3, "EXAMPLE 2 - ACTIVATING FGFR3 MUTATIONS BLOCK AUTOPHAGIC FLUX, WHICH RUNS AGAINST MY OWN WORRY")
print(wrap(
    "Round 219 floated at grade E that FGFR3 INHIBITION MIGHT BE SELF-LIMITING, because Fgfr3 RNAi "
    "blocks FGF18-induced autophagy and that autophagy is what type II collagen secretion needs. "
    "The patent's Example 2 tests the other end of the same axis."))
print()
print(wrap(
    "RCS chondrocytes stably expressing FGFR3 wild-type, G380R (achondroplasia) or R248C "
    "(thanatophoric), made by retroviral transduction. Treated with the lysosomal inhibitors "
    "leupeptin (50 uM, 2 h) and bafilomycin (200 nM, 4 h) to clamp autophagosome degradation - the "
    "standard flux assay. LEUPEPTIN AND BAFILOMYCIN FAILED TO RAISE LC3-II IN THE MUTANT LINES "
    "against the FGFR3 wild-type cells, and FACS showed lower endogenous LC3. AUTOPHAGIC FLUX IS "
    "BLOCKED BY ACTIVATING FGFR3."))
print()
print("    THAT MAKES FOUR OBSERVATIONS ON THIS QUESTION AND THEY DO NOT ALL POINT ONE WAY:")
for s in [
    "AGAINST the self-limiting worry - activating FGFR3 BLOCKS flux (this patent, Example 2), so",
    "  overactivity suppresses the arm and inhibition plausibly relieves it.",
    "AGAINST - wang2015_ach_autophagy reports defective autophagy in an achondroplasia mouse plate.",
    "AGAINST - COL9A1 RISES dose-dependently to about 2.07-fold under TYRA-300 in humans (round 221).",
    "FOR - cinque2016_editorial states the authors' own view that FGF18 acts mainly through FGFR4",
    "  AND TO A LESSER EXTENT THROUGH FGFR3, so the FGFR3 contribution is not an in vitro artefact.",
]:
    print("      " + s)
print()
print(wrap(
    "AND THE RESOLUTION IS PROBABLY THAT BOTH ARE TRUE AT DIFFERENT POINTS OF ONE CURVE. Acute "
    "FGF18-driven FGFR3 signalling CONTRIBUTES to autophagy induction; chronic constitutive FGFR3 "
    "overactivation BLOCKS flux. Tonic and phasic signalling through one receptor need not share a "
    "sign. THE UNCOMFORTABLE COROLLARY FOR THIS CASE IS THAT WE ARE AT THE WILD-TYPE POINT - our "
    "patient has normal FGFR3, so inhibition removes a small positive contribution WITHOUT a "
    "pathological block to relieve, and the achondroplasia data do not transfer. The human COL9A1 "
    "rise is the only observation taken at the relevant point of the curve, and it is reassuring "
    "but indirect. Stays at E."))

# ----------------------------------------------------------------------------- 4
head(4, "ASK #4 - THE BREINHOLT MOUSE MAGNITUDES, AND THEY ARE A WILD-TYPE ELEVATION")
print(wrap(
    "Round 221 could only say continuous infusion produced 'significantly more' growth. The "
    "published JPET version carries Table 5. FVB mice, five weeks, CNP-38 at 203 ug/kg/day, SAME "
    "DOSE both arms, bone length by X-ray:"))
print()
print("      bone            bolus        continuous     ratio    different from bolus?")
for name, b, c in [("femur (right)", 5.5, 7.1), ("tibia (right)", 4.0, 12.2), ("SPINE (lateral)", 11.3, 25.0)]:
    diff = "NO" if name.startswith("femur") else "YES  (P<0.05)"
    print(f"      {name:<15s} +{b:5.1f}%      +{c:5.1f}%      {c/b:4.2f}x    {diff}")
print()
print(wrap(
    "TIBIA TRIPLES AND SPINE MORE THAN DOUBLES ON THE IDENTICAL DAILY DOSE, and both are formally "
    "different from the bolus arm by one-factor ANOVA on log-transformed data. Femur moves in the "
    "same direction and does not separate."))
print()
print(wrap(
    "AND THE AUTHORS STATE THE THING THIS ATLAS HAS BEEN LOOKING FOR SINCE CORR-203, IN THEIR "
    "DISCUSSION - that bone growth EVEN IN A HEALTHY ANIMAL WITH NORMAL ENDOGENOUS CNP LEVELS "
    "could be greatly accelerated by sustained exposure. THESE ARE WILD-TYPE FVB MICE AND THE "
    "SPINE GREW 25 PER CENT. That is an ELEVATION result with a magnitude, on the axial skeleton, "
    "which is the site profile this case needs - and the CNP axis has been carried in this atlas "
    "largely as an achondroplasia drug."))
print()
print(wrap(
    "hirota2018 already gave this atlas a wild-type CNP elevation by osmotic minipump, so the "
    "DIRECTION is confirmatory rather than new. What is new is the MAGNITUDE on the spine and the "
    "fact that it comes from a same-dose schedule contrast rather than a dose contrast."))

# ----------------------------------------------------------------------------- 5
head(5, "AND A DISSOCIATION IN THE SAME PAPER THAT SHOULD CHANGE HOW A MARKER IS READ")
print("      26-week cynomolgus, bone formation markers, per cent increase (Table 6):")
print()
print("      arm                                  BAP     PINP    growth delivered")
print("      TransCon CNP 100 ug CNP/kg/week      +14%    +53%    tail +9%, tibia +6%")
print("      daily CNP-39 20 ug CNP/kg/day        +51%   +144%    tail +3%, tibia +3%")
print()
print(wrap(
    "THE ARM WITH ROUGHLY THREE TIMES THE BONE-FORMATION MARKER RESPONSE DELIVERED ONE THIRD TO "
    "ONE HALF THE LENGTH. A bone turnover marker is not a growth readout, and here they run "
    "OPPOSITE. Any future monitoring plan that uses BAP or PINP to titrate a CNP-axis agent would "
    "have titrated toward the worse molecule. Recorded because this atlas has repeatedly reached "
    "for surrogate markers when a length endpoint was unavailable."))

# ----------------------------------------------------------------------------- 6
head(6, "WHAT IS NOW OPEN THAT WAS NOT OPEN BEFORE")
for i, q in enumerate([
    "Would Tat-Beclin 1 lengthen a WILD-TYPE bone? Nobody has run it, including the inventors, and",
    "  the patent's own saturation pattern predicts it might not. THE EXPERIMENT IS TRIVIAL.",
    "Do BH3 mimetics do anything to bone? Claimed in the patent, zero bone data anywhere in it.",
    "Does partial pharmacological FGFR3 inhibition raise or lower autophagic flux in a NORMAL",
    "  chondrocyte? Both ends of the axis are now characterised and the middle is empty.",
    "Is the CNP spine effect in wild-type mice reproducible outside the sponsor, and does it hold at",
    "  a late bone age? +25 per cent on a normal spine is the largest axial number in this atlas.",
    "Does a sustained-exposure CNP agent beat a daily one on the SPINE in a primate? breinholt2019",
    "  measured tail in the monkey and spine only in the mouse.",
], 1):
    print("      " + (f"{i}. {q}" if not q.startswith("  ") else f"   {q.strip()}"))
print()
rule()
