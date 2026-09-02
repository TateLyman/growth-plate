#!/usr/bin/env python3
"""
R391 - THE COMPOUND AND ROUTE DECISION, LAID OUT AGAINST WHAT IS ACTUALLY MEASURED.

Consolidates R368-R390. Two questions the file left genuinely open:
  (1) SAG or SAG21k or something else?
  (2) is systemic really the maximum-effect route, or was effect traded for practicality?

Nothing here is new data. It is the existing evidence arranged so the decision is
forced by it rather than asserted over it.
"""

# --------------------------------------------------------------------------
# 1. PHYSICOCHEMISTRY - PubChem, retrieved 2026-08-14
# --------------------------------------------------------------------------
CHEM = [
    # name,                 CID,        formula,             MW,     XLogP
    ("SAG (free base)",     5284330,   "C28H28ClN3OS",      490.1,  6.3),
    ("SAG dihydrochloride", 154884292, "C28H30Cl3N3OS",     563.0,  None),
    ("SAG21k",              16678532,  "C29H28ClF2N3O2S",   556.1,  6.5),
    ("Hh-Ag1.5",            44195701,  "C28H26ClF2N3OS",    526.0,  6.5),
    ("purmorphamine",       5284329,   "C31H32N6O2",        520.6,  6.5),
]

print("="*78)
print("1. PHYSICOCHEMISTRY DOES NOT SEPARATE THEM")
print("="*78)
print(f"{'compound':<22}{'CID':>11}{'formula':>22}{'MW':>8}{'XLogP':>8}")
for n, cid, mf, mw, lp in CHEM:
    print(f"{n:<22}{cid:>11}{mf:>22}{mw:>8}{('-' if lp is None else lp):>8}")
print("""
  Every Smoothened agonist is 490-556 Da at XLogP 6.3-6.5. R371 already established
  that the cartilage partition wall does not exist at this size (farnum2006: 332 Da
  reaches ~100% of vascular concentration, 3 kDa ~60%, 40 kDa undetectable), and
  R371's Donnan arithmetic gives a monovalent cation only 1.8-2.7x.
  → SIZE, LOGP AND CHARGE ARE NOT DECISION VARIABLES HERE. The choice is made on
    EVIDENCE IN THE TARGET TISSUE, not on chemistry.
  ⚠ PubChem returns the same CID for 'SAG1.3' and 'smoothened agonist' - the names
    are used interchangeably in catalogues. Do not treat SAG1.3 as a distinct agent
    without checking the vendor's own structure.""")

# --------------------------------------------------------------------------
# 2. THE EVIDENCE LEDGER - what each compound actually has
# --------------------------------------------------------------------------
CRITERIA = [
    # criterion,                                        SAG,                            SAG21k
    ("growth-plate POOL result in a NORMAL animal",  "YES  trompet2024 +61%",        "no"),
    ("stature endpoint in vivo",                     "YES  li2021 117->133 mm",      "no"),
    ("VERTEBRAL length measured",                    "YES  li2021 L3 +32.1%",        "no"),
    ("bone-LENGTH gain, normal animal (local)",      "YES  trompet2024 +3.63%",      "no"),
    ("systemic study WITH a bone endpoint",          "no",                           "YES  rundle2023 (normaliser)"),
    ("ADULT systemic safety with organ endpoints",   "no",                           "YES  lee2016colitis"),
    ("AQUEOUS in vivo vehicle demonstrated",         "no",                           "YES  PBS, lee2016colitis"),
    ("water-soluble SALT catalogued",                "YES  dihydrochloride",         "not established"),
    ("catalogue availability >=98% + CoA",           "YES  6+ vendors",              "limited/unclear"),
    ("fibrin-hydrogel loading published",            "no",                           "YES  he2024sag"),
    ("relative potency",                             "Kd 59 nM, Gli EC50 ~3 nM",     "several-fold MORE active"),
    ("teratogenic (single 25 mg/kg, pregnancy)",     "YES  mao2026sag",              "assume class effect"),
]
print("\n"+"="*78)
print("2. THE EVIDENCE LEDGER")
print("="*78)
print(f"{'criterion':<46}{'SAG':<32}{'SAG21k'}")
for c, a, b in CRITERIA:
    print(f"{c:<46}{a:<32}{b}")

print("""
⭐ THE DECIDING LINE: BOTH LOAD-BEARING EFFICACY RESULTS AT THE GROWTH PLATE ARE SAG.
  · trompet2024's +61% resting-zone pool in NORMAL mice is the one result CORR-203
    cannot touch, and it is SAG.
  · li2021's vertebral measurement - the entire compartment argument for going
    systemic - is SAG.
  SAG21k's advantages are real but every one of them is in a tissue that is not the
  target (colon, nerve, fracture callus) or is a formulation convenience. Switching
  compounds means abandoning the only two efficacy anchors this programme has.

→ DECISION: SAG DIHYDROCHLORIDE. SAG21k IS THE FALLBACK, NOT THE LEAD.
  The one thing that would force the switch is FORMULATION FAILURE: SAG21k is the
  only agonist with a demonstrated aqueous in vivo vehicle, and it is several-fold
  more potent, so if SAG dihydrochloride cannot be brought to the required
  concentration, SAG21k solves both problems at once - at the cost of losing the
  direct link to trompet2024 and li2021.""")

# --------------------------------------------------------------------------
# 3. ROUTE - was effect traded for practicality?
# --------------------------------------------------------------------------
print("\n"+"="*78)
print("3. ROUTE: IS SYSTEMIC ACTUALLY THE MAXIMUM-EFFECT CHOICE?")
print("="*78)
print("""
R375 ranked systemic FOURTH and called it 'NOT the maximum'. R388 switched to it on
compartment grounds. Both cannot stand unexamined. What changed between them:

  R375's case for LOCAL rested on one premise - that SYSTEMIC hedgehog activation is
  the hazard, and a depot confines it. R390 tested that premise in three organs:
    · COLON      systemic agonist AMELIORATES colitis and DECREASES colitis-
                 associated tumour burden; the ANTAGONIST increases it   (lee2016colitis)
    · PANCREAS   agonist protects beta cells; hedgehog INHIBITORS are reported to
                 raise diabetes incidence in patients                    (kong2025dhh)
    · SKIN       the human cancer signal (cSCC, ROR ~50) attaches to the marketed
                 ANTAGONISTS                                             (zheng2025faers)
  → THE SAFETY ARGUMENT THAT MOTIVATED THE LOCAL ROUTE HAS SUBSTANTIALLY WEAKENED.
    On every organ where systemic hedgehog tone has been manipulated and measured,
    the harm is on the SUPPRESSION side.

  Against that, the depot keeps one advantage and it is not small:
    · it holds the ONLY true bone-LENGTH endpoint in a NORMAL animal
      (trompet2024 bead: femur +2.75/+2.64/+3.63% at 1/2/6 months, still widening)
    · local concentration is ~250,000x EC50 (R386, after the R372 units correction),
      which nothing systemic approaches

  And the compartment fact is unchanged and decisive:
    · the residual at BA16 is TRUNK-dominant (R274/R318)
    · a knee depot CANNOT reach a vertebral plate at all
    · li2021 is the only study on this axis that measured a vertebra: L3 +32.1%

→ REVISED RANKING:
    1. HHIP knockdown          - true maximum, no molecule, $1-3M / 3-4 yr (R382)
    2. SYSTEMIC pulsed SAG     - MOVED UP from 4th. Only route that reaches the
                                 compartment holding the residual, and the safety
                                 premise against it did not survive R390
    3. Local SOC depot         - only true length endpoint, but aimed at the SMALLER
                                 compartment, and costs a procedure per pulse
    4. Sterol subtractions     - free, do them regardless, no length endpoint anywhere

⛔ AND THE COMBINATION IS *NOT* RECOMMENDED, FOR A SPECIFIC REASON.
  Adding a knee depot to a systemic pulse costs only 2.70 mg (0.27% more drug) and is
  superficially free. But R384 established that this stack is ALREADY Ihh-elevating -
  erdafitinib is pharmacological postnatal chondrocyte FGFR3 deficiency, which RAISES
  Ihh (zhou2015a) - and that cartilaginous lesions are a BAND with too little Ihh
  giving enchondroma and too much giving chondroma-like lesions. Stacking systemic
  plus local at the knee pushes ONE compartment furthest up that band.
  → SYSTEMIC ALONE, ONE PULSE, READ OUT AT 6 MONTHS. A knee depot becomes a candidate
    ONLY if the readout shows the trunk moved and the knee did not.""")

# --------------------------------------------------------------------------
# 4. THE ANSWERED / UNANSWERED LEDGER
# --------------------------------------------------------------------------
ANSWERED = [
    ("the regimen exists",            "li2021: 20 mg/kg s.c. q2d, P7/P14->P30, DMSO->saline"),
    ("dose cross-checks",             "li2021 1.07 g vs trompet2024 0.85 g per human pulse, ratio 1.26"),
    ("it reaches the TRUNK",          "li2021 L3 vertebra +32.1% - no depot can do this"),
    ("pool mechanism in a NORMAL animal","trompet2024 +61% RZ pool, Ki67 up in top 50 um"),
    ("stage favours him",             "post-SOC arm is the favourable one, 3 independent lines"),
    ("aqueous vehicle is possible",   "lee2016colitis dosed SAG21k in PBS"),
    ("ADULT gut, inflammation",       "systemic agonist AMELIORATES colitis"),
    ("ADULT gut, CANCER",             "SAG21k DECREASED colon tumour burden; vismodegib increased it"),
    ("the GI lesion is MESENCHYMAL",  "li2021 discussion: smooth muscle layer, obstruction risk"),
    ("tumour risk segment",           "STOMACH/GEJ, not intestine or colon (li2026stromalhh)"),
    ("human harm attaches to LOSS",   "colon, pancreas, skin - three organ systems"),
    ("the pathway self-limits",       "cohen2015: adaptation continues BELOW Ptch1"),
    ("agonist induces its own brakes","lee2016colitis measured Ptch1 AND Hhip up in vivo"),
    ("schedule: intermittent works",  "liu2026gorlin, human, every-other-day kept effect lost toxicity"),
    ("SMO agonist aligns with CREB",  "steiner2026smo: active SMO sequesters PKA-C"),
    ("teratogenicity",                "mao2026sag: single 25 mg/kg -> cleft lip/palate"),
]
UNANSWERED = [
    ("DOSE-RESPONSE at the plate", "g_l12_390a", "BLOCKS: formulation, GMP size, gut risk - all three"),
    ("systemic LENGTH in a normal animal", "g_l12_388a", "BLOCKS: whether the route works at all"),
    ("aqueous SAG.2HCl at >=30 mg/mL", "g_l12_388b", "BLOCKS: dosing volume - unless the dose falls"),
    ("adult gut at the HIGH dose", "g_l12_389a", "BLOCKS: nothing if the dose falls; else a real cap"),
    ("post-withdrawal rebound trough", "g_l12_389b", "BLOCKS: whether the taper is needed"),
    ("GMP material", "-", "BLOCKS: administration. Not scientific"),
    ("no SMO agonist ever in a human", "-", "BLOCKS: all first-in-human inference. CONFIRMED R390"),
    ("no agonist at a BA16-equivalent stage", "-", "BLOCKS: extrapolation from juvenile rodents"),
    ("pulse INTERVAL never measured", "g_l7_375a", "BLOCKS: pulses 2+. Not pulse 1"),
]
print("\n"+"="*78)
print("4. THE LEDGER")
print("="*78)
print(f"\nANSWERED ({len(ANSWERED)}):")
for k, v in ANSWERED:
    print(f"  ✓ {k:<34} {v}")
print(f"\nUNANSWERED ({len(UNANSWERED)}), ranked by what each blocks:")
for k, g, w in UNANSWERED:
    print(f"  ✗ {k:<38} [{g}]\n      {w}")

print("""
⭐ FIVE OF THE NINE UNANSWERED ITEMS ARE DOWNSTREAM OF ONE CURVE.
  The dose-response (g_l12_390a) sets the formulation demand, the GMP batch size and
  the gut-liability margin, and the SAME study design that measures it also delivers
  the systemic length endpoint (g_l12_388a) and the adult-gut answer (g_l12_389a).
  ONE experiment closes FIVE gaps:
    0.5 / 2 / 5 / 10 / 20 mg/kg s.c. q2d x 3 wk + vehicle, NORMAL mice, post-SOC,
    n>=10, read at maturity: femur + tibia + VERTEBRAL length by caliper, resting-zone
    cell number and Ki67, growth-plate Gli1/Ptch1/Hhip, and muscularis thickness by
    gut segment - plus a withdrawal arm at +2/+10/+21 days for the rebound question.
  THAT IS THE WHOLE PROGRAMME. Everything else is either free (subtractions, dBA-dCA)
  or a manufacturing contract.""")
