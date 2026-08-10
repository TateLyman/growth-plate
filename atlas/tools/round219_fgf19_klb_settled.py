#!/usr/bin/env python3
"""ROUND 219 - resolve the FGF19/beta-klotho compensatory loop, completely.

WHY THIS EXISTS
---------------
Rounds 217 and 218 both closed by naming "the FGF19/klotho-beta compensatory loop"
as THE ONE LEVER NOBODY HAS TRIED. The user asked for it to be resolved entirely.
It resolves against being a lever, on four independent grounds, and THREE OF THE
FOUR WERE ALREADY IN THIS ATLAS (CORR-041, CORR-042, and the cinque2015 extraction
sitting inside erdafitinib_versus_the_alternatives_decision). That is the third
instance of the CORR-205 failure mode and it is logged as CORR-215.

WHAT THE ROUND ADDS THAT WAS NOT ALREADY HERE
---------------------------------------------
1. The MAGNITUDE argument. Nobody had compared the FGF19 concentration that
   restrains cartilage with the FGF19 concentration a human carries.
2. The TRANS-KLB loophole. chen2025/fgf19cart2025 had to ADD soluble KLB to see
   any effect at all - which means the CORR-041 argument ("co-receptor absent from
   the tissue") does not by itself close the endocrine route, because the paper's
   own design supplies the co-receptor from outside. The SURF301 proteomic panel
   reports KLB RISING IN PLASMA. That is the one route that survives the tissue
   argument, and it is quantitatively hopeless for a different reason.
3. The RECEPTOR LEDGER PRICED. The atlas knew the direction of each FGFR. It had
   never computed what fraction of each erdafitinib actually removes at 8 mg.
4. The inversion: the FGFR4 arm that operates in HUMAN cartilage is the
   growth-PROMOTING one (FGF18/autophagy/Col2, cinque2015), not the
   growth-restraining one (FGF19/KLB/Wnt, fgf19cart2025). So the compensatory loop
   is not a lever to pull; the receptor it runs through is a cost erdafitinib is
   already paying.

NO NUMBER BELOW IS INVENTED. Sources are named inline.
"""
import math

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
head(1, "THE LIGAND CANNOT REACH THE RECEPTOR IN A HUMAN PLATE - MEASURED, NOT ARGUED")
print(wrap(
    "atlas measurement, GSE288028, four fresh human growth plate biopsies, per cent of "
    "CHONDROCYTE-GATED cells with detected transcript (CORR-041 / CORR-042):"))
print()
print("      gene         donor1   donor2   donor3   donor4     verdict")
print("      FGF19          0.00     0.01     0.00     0.00     LIGAND ABSENT (ungated)")
print("      KLB            1.00     2.50     0.20     0.00     CO-RECEPTOR ESSENTIALLY ABSENT")
print("      FGFR4         11.50    12.70    24.90    25.00     RECEPTOR PRESENT, 35-80x")
print("                                                          ENRICHED IN CHONDROCYTES")
print()
print(wrap(
    "kurosu2007 is the reason KLB is not optional: WITHOUT beta-klotho FGF19 does not bind "
    "FGFR1c or FGFR4 at all and binds POORLY to FGFR2c and FGFR3c. So the sponsor's own "
    "cartoon on surf301_pb060_2024 - 'FGF19 binds to FGFR3 and FGFR4 and to co-receptor KLB' "
    "- is drawing a complex that a human growth plate chondrocyte cannot assemble."))

# ----------------------------------------------------------------------------- 2
head(2, "AND THE CONCENTRATION IS OFF BY THREE ORDERS OF MAGNITUDE")
phys_lo, phys_hi = 0.115, 0.221      # ng/mL, median fasting serum FGF19, healthy
paper_dose = 200.0                    # ng/mL, fgf19cart2025 metatarsal culture
klb_dose = 200.0                      # ng/mL, exogenous KLB, same experiment
print(wrap(
    f"fgf19cart2025 shortened cultured mouse metatarsals with FGF19 at {paper_dose:.0f} ng/mL "
    f"PLUS exogenous beta-klotho at {klb_dose:.0f} ng/mL. Median fasting serum FGF19 in healthy "
    f"humans is roughly {phys_lo*1000:.0f}-{phys_hi*1000:.0f} pg/mL."))
print()
for label, p in (("against the lower median", phys_hi), ("against the lower end", phys_lo)):
    print(f"      fold gap {label:<26s} {paper_dose/p:9,.0f}x")
print()
olink_min = 1.5   # the dotted threshold on the pb060 volcano; the actual rise is not
                  # in the text layer and the figure was not archived - see the ASK list
for f in (1.5, 2.0, 3.0):
    print(f"      a {f:.1f}-fold rise takes {phys_hi*1000:.0f} pg/mL to "
          f"{phys_hi*f*1000:6.0f} pg/mL = {paper_dose/(phys_hi*f):9,.0f}x SHORT")
print()
print(wrap(
    "THE COMPENSATORY RISE IS NOT SMALL RELATIVE TO ITSELF. IT IS SMALL RELATIVE TO THE "
    "CONCENTRATION THAT DOES ANYTHING TO CARTILAGE. Even granting the trans-KLB loophole "
    "below, a 1.5- to 3-fold rise on a 0.2 ng/mL baseline is roughly a thousandfold short of "
    "the only concentration at which FGF19 has ever been shown to shorten a bone."))

# ----------------------------------------------------------------------------- 3
head(3, "THE TRANS-KLB LOOPHOLE, WHICH IS THE ONE THING CORR-041 DID NOT COVER")
print(wrap(
    "CORR-041 closed the endocrine route by showing the tissue lacks the co-receptor. "
    "fgf19cart2025's OWN DESIGN shows that argument is incomplete: FGF19 ALONE did nothing to "
    "the metatarsals. The effect appeared only when recombinant KLB was added to the medium. "
    "So a soluble co-receptor supplied from outside CAN reconstitute the complex in a tissue "
    "that does not make it - and surf301_pb060_2024 reports KLB RISING IN PLASMA alongside "
    "FGF19. That is a real route and the atlas did not have it."))
print()
print(wrap(
    "IT DIES ON ARITHMETIC RATHER THAN ON BIOLOGY, and on one unverified premise that must be "
    "stated rather than assumed: the Olink panel reports a plasma ANALYTE called KLB, and "
    "whether circulating beta-klotho exists as a functional shed ectodomain at ng/mL "
    "concentrations is NOT established - the well-characterised soluble klotho in human serum "
    "is ALPHA-klotho, at roughly 0.2-0.9 ng/mL. Recorded as a gap, not as a fact."))

# ----------------------------------------------------------------------------- 4
head(4, "THE RECEPTOR THAT MATTERS RUNS THE OTHER WAY, AND THE ATLAS ALREADY KNEW")
print(wrap(
    "SAME RECEPTOR, TWO LIGANDS, OPPOSITE SIGNS. fgf19cart2025 - FGF19 through FGFR4 WITH KLB "
    "restrains cartilage via SFRP1/WIF1/DKK2 and Wnt antagonism. cinque2015 - FGF18 through "
    "FGFR4 and JNK activates the VPS34-beclin-1 complex, and that autophagy is REQUIRED for "
    "type II collagen secretion and for bone growth; Fgf18+/- and Fgfr4-/- mice fail to induce "
    "postnatal autophagy and have decreased Col2 in the growth plate."))
print()
print(wrap(
    "WHICH LIGAND OPERATES IN A HUMAN PLATE IS A MEASUREMENT, NOT A JUDGEMENT CALL. FGF19 "
    "needs KLB and neither is there. FGF18 needs no klotho and IS detected. THEREFORE THE "
    "OPERATIVE FGFR4 SIGNAL IN HUMAN CARTILAGE IS THE GROWTH-PROMOTING ONE, and FGFR4 "
    "blockade is a COST rather than a benefit. The atlas reached this in CORR-046 and then "
    "rounds 217 and 218 nominated the FGF19 loop as a lever anyway."))

# ----------------------------------------------------------------------------- 5
head(5, "PRICING THE LEDGER - WHAT 8 mg ERDAFITINIB ACTUALLY REMOVES AT EACH RECEPTOR")
# perera2017 Ba/F3 CELLULAR IC50s, the developers' own primary characterisation (CORR-211)
IC50 = {"FGFR1": 22.1, "FGFR3": 13.2, "FGFR4": 25.0}
DIRECTION = {"FGFR1": "ANTI-growth (karolak2015)",
             "FGFR3": "PRO-growth  (the whole point)",
             "FGFR4": "ANTI-growth (cinque2015)"}
# round 217/218 fixed 8 mg at C/IC50(FGFR3) = 0.469 -> free concentration:
X3 = 0.469
C_FREE = X3 * IC50["FGFR3"]
print(wrap(
    f"Free plasma concentration at 8 mg is pinned by rounds 216-218 at C/IC50(FGFR3) = {X3:.3f}, "
    f"which against perera2017's cellular FGFR3 IC50 of {IC50['FGFR3']} nM is "
    f"{C_FREE:.2f} nM free. The same free concentration is then read against the SAME "
    f"paper's Ba/F3 IC50 for the other two receptors - one source, one assay, one scale."))
print()
print("      receptor   IC50(nM)   C/IC50    % removed n=1   % removed n=2.13   direction")
for r in ("FGFR3", "FGFR1", "FGFR4"):
    x = C_FREE / IC50[r]
    i1 = 100 * (1 - 1 / (1 + x))
    i2 = 100 * (1 - 1 / (1 + x ** 2.13))
    print(f"      {r:<9s}  {IC50[r]:6.1f}   {x:6.3f}   {i1:11.1f}     {i2:13.1f}      {DIRECTION[r]}")
print()
print(wrap(
    "READ THE FGFR4 ROW FOR THE ONLY THING IT IS ADMISSIBLE FOR. AT 8 mg ERDAFITINIB ALREADY "
    "REMOVES 5 TO 20 PER CENT OF FGFR4 - so even if the compensatory FGF19 rise were "
    "pharmacologically real, its receptor is partly blocked by the anchor drug, and an agent "
    "added to suppress the ligand would be buying a fraction of a fraction of a thousandth. "
    "THAT IS THE FGF19 QUESTION AND THE TABLE ANSWERS IT."))
# what dabogratinib's selectivity would look like at matched FGFR3 coverage
D = {"FGFR1": 278.0, "FGFR3": 11.0, "FGFR2": 157.0, "FGFR4": 405.0}
c_d = X3 * D["FGFR3"]     # matched fractional FGFR3 coverage
print()
print("      AT MATCHED FGFR3 COVERAGE (same C/IC50 = 0.469), the off-target burden would be:")
print("      receptor   erdafitinib % removed (n=1)   dabogratinib % removed (n=1)")
for r in ("FGFR1", "FGFR4"):
    xe = C_FREE / IC50[r]; xd = c_d / D[r]
    print(f"      {r:<9s}  {100*(1-1/(1+xe)):20.1f}   {100*(1-1/(1+xd)):26.1f}")

# ----------------------------------------------------------------------------- 5b
head("5b", "STOP. THIS IS THE RECEPTOR LEDGER AGAIN, AND IT IS A RETRACTED ARGUMENT")
print(wrap(
    "The paragraph that belongs here writes itself - erdafitinib removes roughly a third as "
    "much of each ANTI-growth receptor as of the PRO-growth one, dabogratinib removes almost "
    "none, selectivity cannot be bought with dose, therefore prefer the selective molecule. "
    "THAT PARAGRAPH IS FORBIDDEN, AND THE ATLAS SAYS SO IN TWO PLACES."))
print()
print(wrap(
    "CORR-046 RETRACTED THE RECEPTOR LEDGER for three reasons that all still apply here. (1) It "
    "is built from GERMLINE AND DEVELOPMENTAL DELETIONS - karolak2015 is Col2a1-Cre from "
    "embryonic cartilage, cinque2015's Fgfr4-/- is germline - and applied to PARTIAL POSTNATAL "
    "PHARMACOLOGY in an already-built adolescent plate. Those are different questions. (2) It "
    "weights three receptors equally while having a magnitude for only one: FGFR3 spans roughly "
    "65 cm of adult human stature between achondroplasia and CATSHL, and NEITHER FGFR1 NOR "
    "FGFR4 HAS ANY REPORTED HUMAN STATURE PHENOTYPE AT ALL. (3) The net effect of erdafitinib on "
    "a growing human was MEASURED and was large and positive, and a ledger assembled from mouse "
    "knockouts does not overrule a measurement."))
print()
print(wrap(
    "CORR-147 RECORDS THAT I REBUILT THE RETRACTED LEDGER TWICE AFTER ITS RETRACTION AND SERVED "
    "IT TO THE USER, WHO SAID 'YOU'RE LOOPING AGAIN'. This round is the fourth approach. It was "
    "caught before it entered a node only because the correction was read. Logged as CORR-217."))
print()
print(wrap(
    "WHAT THE TABLE IS ADMISSIBLE FOR, STATED NARROWLY. It is a per-receptor OCCUPANCY "
    "measurement that nobody had computed, on one assay and one scale, and it settles the FGF19 "
    "question above. It is NOT a net-mechanism verdict, because converting occupancy into height "
    "requires a per-receptor exchange rate and only FGFR3's is known. THE HONEST FORM OF THE "
    "COMPARISON IS: erdafitinib's off-target occupancy is roughly TEN TO FIFTEEN TIMES "
    "dabogratinib's at matched FGFR3 engagement, and the value of that difference in centimetres "
    "is UNKNOWN AND MAY BE ZERO."))
print()
print(wrap(
    "The CORR-211 caveat also applies in full - the two IC50 sets come from different "
    "laboratories in unmatched assays - though both rows use each molecule's OWN developers' "
    "numbers, which is the comparison CORR-211 requires."))

# ----------------------------------------------------------------------------- 6
head(6, "SO WHAT REPLACES THE LEVER - THE ARM ERDAFITINIB BREAKS HAS A REPAIR WITH BONE DATA")
print(wrap(
    "cinque2015 did not stop at the mechanism. INTRAPERITONEAL Tat-beclin-1 (Beclin-1 "
    "Activator II, retro-inverso, Millipore) at 2 mg/kg daily in newborn mice INCREASED Col2 "
    "LEVELS AND FEMUR SIZES IN P9 AND P15 Fgfr4-/- MICE, and restored Col2 and cleared "
    "intracellular procollagen-II deposits in Fgf18+/- mice."))
print()
print(wrap(
    "THAT IS A PHARMACOLOGICAL AGENT THAT LENGTHENED BONE IN VIVO, WHICH NOTHING IN ROUND 217's "
    "SERIES LIST HAD. And its logic is a better kind than series multiplication - it is a REPAIR "
    "of an arm rather than another block on the same cascade, so it does not depend on the "
    "independence assumption the FGF19 rise was supposed to threaten."))
print()
print("    IT IS UNRANKED, FOR TWO INDEPENDENT REASONS, AND BOTH ARE ANSWERABLE:")
print()
print(wrap(
    "ONE - RESTORATION OR ELEVATION (CORR-203). The Fgfr4-/- rescue is RESTORATION of a "
    "deficient animal. Whether Tat-beclin-1 lengthens a WILD-TYPE femur is the harder claim and "
    "the one this case needs. Extended Data Fig. 9g-i would say; those panels are not in the "
    "full text this atlas holds. ON THE ASK LIST.", 6))
print()
print(wrap(
    "TWO - AND THIS IS THE ONE CORR-046 FORCES. The candidate's whole rationale is that "
    "erdafitinib creates the deficit Tat-beclin-1 repairs. But cinque2015's Fgfr4-/- is a "
    "GERMLINE NULL - complete loss from conception - and erdafitinib at 8 mg removes 5 to 20 "
    "per cent of FGFR4 postnatally in a plate that is already built. NOBODY HAS SHOWN THAT "
    "PARTIAL POSTNATAL FGFR4 INHIBITION PRODUCES ANY Col2 OR AUTOPHAGY DEFICIT AT ALL. Until it "
    "does, this is a repair for a break that has not been demonstrated to occur.", 6))
print()
print(wrap(
    "AND ONE INFERENCE THAT DOES *NOT* SURVIVE, CAUGHT BY CHECKING. cinque2015 reports that "
    "RNAi of Fgfr3 OR Fgfr4 - but not Fgfr1 or Fgfr2 - blocks FGF18-induced autophagy in RCS "
    "chondrocytes. That invites a striking claim: that FGFR3 INHIBITION IS SELF-LIMITING, "
    "because it also removes the autophagy that collagen secretion needs. THE IN VIVO DATA IN "
    "THE SAME PAPER REFUSE IT - a significant fall in LC3-II was seen in the growth plates of "
    "Fgfr4-/- mice and NOT in Fgfr3-/- mice, and the authors conclude autophagy induction by "
    "FGF18 is MAINLY THROUGH FGFR4. The self-limiting claim is in-vitro-only and is graded E, "
    "not asserted."))

# ----------------------------------------------------------------------------- 7
head(7, "THE VERDICT, AND WHAT IS STILL OPEN")
for line in [
    "THE FGF19/KLB LOOP IS NOT A LEVER. It fails on ligand absence, on co-receptor absence,",
    "on a ~1000-fold concentration gap, and on the fact that its receptor is already partly",
    "blocked by the anchor drug. Rounds 217 and 218 were wrong to keep naming it, and the",
    "atlas already held three of the four disproofs (CORR-215).",
    "",
    "WHAT REPLACES IT IS THE INVERSE FINDING. The FGFR4 arm that actually operates in human",
    "cartilage is the growth-PROMOTING one (FGF18/autophagy/Col2), not the growth-restraining",
    "one (FGF19/KLB/Wnt). So there is no compensatory ligand to block, and the receptor is one",
    "erdafitinib partly occupies rather than one an added agent should target.",
    "",
    "AND THE ROUND'S OWN MAIN RISK WAS ITSELF. The occupancy table above wants to become the",
    "receptor ledger, which CORR-046 retracted and CORR-147 records me rebuilding twice after",
    "the retraction. It is admissible as occupancy and inadmissible as a verdict, because only",
    "FGFR3 has a human exchange rate and it is worth roughly 65 cm between its two directions",
    "while FGFR1 and FGFR4 have no human stature phenotype at all. Logged as CORR-217.",
    "",
    "AND THE REPLACEMENT CANDIDATE IS AN AUTOPHAGY ACTIVATOR, held UNRANKED pending one figure",
    "panel AND one experiment nobody has run - whether partial postnatal FGFR4 inhibition",
    "creates any deficit to repair.",
]:
    print("    " + line if line else "")
print()
print("    STILL OPEN, AND THE FIRST TWO ARE THINGS TO ASK FOR RATHER THAN TO CONCLUDE ABOUT:")
for i, q in enumerate([
    "cinque2015 EXTENDED DATA Fig. 9g-i - did Tat-beclin-1 lengthen a WILD-TYPE femur, or only",
    "  rescue Fgfr4-/-? Decides restoration vs elevation, which decides the candidate.",
    "weinstein1998 (Development 125:3615) FULL TEXT - the Fgfr3-/-;Fgfr4-/- double null is",
    "  described as PRONOUNCED DWARFISM. If that is skeletal rather than secondary to the lung",
    "  defect, it is a direct in vivo model of erdafitinib's receptor profile and the single",
    "  most decisive experiment in this thread. Paywalled.",
    "surf301_pb060_2024 FIGURE - the actual FGF19 and KLB fold changes, which are in a volcano",
    "  plot with a 1.5-fold threshold line and not in the text layer. The PDF was not archived.",
    "The sponsor's own FGFR4 PD analysis, stated on the poster as ONGOING.",
    "Does a circulating, functional soluble beta-klotho exist in humans at ng/mL? Not established.",
], 1):
    print(f"      {i if not q.startswith(' ') else ' '}. {q}" if not q.startswith("  ") else f"         {q.strip()}")
print()
rule()
