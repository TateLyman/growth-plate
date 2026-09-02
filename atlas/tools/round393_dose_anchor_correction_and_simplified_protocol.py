#!/usr/bin/env python3
"""
R393 - THE COMPLEXITY IS DOWNSTREAM OF ONE ANCHOR, AND THE ANCHOR WAS CHOSEN BADLY.

R388-R392 scaled every human number from li2021's 20 mg/kg. That is the HIGHEST dose
in the published effective range, and it was chosen because li2021 is the study with
a stature endpoint.

⛔ BUT CORR-203 ALREADY EXCLUDES li2021's EFFECT SIZE AS A PREDICTION - it is
   restoration in an Ihh-ablated dysplasia. So the atlas imported the DOSE from a
   study whose EFFECT it had already discounted, and then let the entire practical
   burden - gram-scale synthesis, a 30 mg/mL formulation that does not exist,
   multi-site injections - follow from that single choice.

This tool prices the three anchors that actually exist in the literature.
"""

MW_FREE, MW_SALT = 490.06, 562.98
SALT = MW_SALT / MW_FREE
KM_M, KM_H = 3.0, 37.0
N_DOSES = 10            # the R392 escalate/plateau/taper pulse
PULSES_PER_YEAR = 4

ANCHORS = [
    # label, mouse mg/kg, what was actually MEASURED at that dose, ref
    ("LOW",  0.5,  "2.8-fold Gli1 rise in COLON of adult mice; colitis and colitis-\n"
                   "               associated tumour burden both reduced. Aqueous (PBS) vehicle.",
                   "lee2016colitis"),
    ("MID",  5.0,  "INCREASED PTCH1, GLI1 AND SOX9 IN CHONDROCYTES IN VIVO, systemic,\n"
                   "               3 weeks. Authors state 5-20 mg/kg/day is the effective\n"
                   "               systemic range for activating SHH signalling in mice.",
                   "rundle2023"),
    ("HIGH", 20.0, "stature corrected in an Ihh-ablated dysplasia; L3 vertebra +32.1%.\n"
                   "               ⛔ CORR-203 excludes the effect size as a prediction.",
                   "li2021"),
]

print("="*80)
print("R393  THE THREE DOSE ANCHORS, PRICED")
print("="*80)
print(f"""
All three are published, all three are systemic, all three demonstrably engage the
pathway. They span FORTY-FOLD. R388-R392 used only the top one.
""")

BW = 60.0
CONC = 30.0
for label, mgkg, measured, ref in ANCHORS:
    hed_mgkg = mgkg * KM_M / KM_H
    dose_free = hed_mgkg * BW
    dose_salt = dose_free * SALT
    vol = dose_salt / CONC
    sites = max(1, -(-vol // 2.0))
    pulse_salt = dose_salt * N_DOSES
    year_g = pulse_salt * PULSES_PER_YEAR / 1000
    conc_for_1ml = dose_salt / 1.0
    print("-"*80)
    print(f"{label:<5} anchor = {mgkg:>4.1f} mg/kg mouse   [{ref}]")
    print(f"      measured: {measured}")
    print(f"      HED                  {hed_mgkg:.3f} mg/kg")
    print(f"      dose at {BW:.0f} kg        {dose_free:6.1f} mg free base  =  {dose_salt:6.1f} mg SALT")
    print(f"      volume @{CONC:.0f} mg/mL    {vol:5.2f} mL   ->  {int(sites)} injection site(s)")
    print(f"      conc for a 1 mL dose {conc_for_1ml:5.1f} mg/mL")
    print(f"      per 10-dose pulse    {pulse_salt:7.1f} mg")
    print(f"      four pulses / year   {year_g:6.3f} g")

print("-"*80)
print("""
⭐⭐ THE SIMPLIFICATION IS THE MID ANCHOR, AND IT IS BETTER JUSTIFIED THAN THE HIGH ONE.

  rundle2023 gave 5 mg/kg/day SYSTEMICALLY for three weeks and reported INCREASED
  PTCH1, GLI1 AND SOX9 IN CHONDROCYTES. That is target engagement, in vivo, in the
  RIGHT CELL TYPE, at a quarter of li2021's dose. li2021's claim to the anchor was
  its stature endpoint - and CORR-203 already disqualifies that endpoint from being
  used as a prediction. So the MID anchor rests on the more relevant measurement.

  WHAT IT CHANGES, AT 60 kg:
    · ONE injection of ~0.9 mL instead of two of 1.9 mL - and every body weight from
      50 to 80 kg stays at ONE site
    · 279 mg per pulse instead of 877 mg  (3.1x less)
    · 1.1 g per year instead of 3.5 g
    · the formulation requirement RELAXES from >=30 mg/mL to about 25 mg/mL for a
      single 1 mL injection - and even 10 mg/mL gives a perfectly ordinary 2.8 mL
    · the gram-scale custom synthesis argument weakens: at ~1 g/year this is a small
      batch, not a manufacturing programme

⭐ AND THE LOW ANCHOR IS WHERE EVERYTHING COLLAPSES ENTIRELY, IF IT WORKS.
    · 2.8 mg of salt per dose, 28 mg per pulse, 112 mg per YEAR
    · a 1 mL injection needs 2.8 mg/mL - a trivial solubility target, and
      lee2016colitis already dosed a Smoothened agonist systemically in PBS
    · 112 mg/year is an ordinary catalogue purchase, not a synthesis contract
    · one small subcutaneous injection, insulin-syringe volume
  ⛔ BUT: the only measurement at that dose is in COLON, not cartilage. It is a real
    option and it is a genuine gamble on potency.

⚠ THE ARGUMENT THAT THE PLATE MAY NEED LESS THAN THE COLON - grade E, but it is not
  nothing. lee2016colitis states its modest 2.8-fold Gli1 rise is because CONSTITUTIVE
  epithelial Hh ligand keeps basal stromal Gli1 HIGH in colon, i.e. the colon is a
  hard tissue to move proportionally. The growth plate at bone age 16 is a tissue
  whose hedgehog output is DECLINING - that is the entire premise of the
  intervention. A tissue with lower basal tone should be EASIER to move.

⛔ THE HONEST COUNTERWEIGHT, STATED PLAINLY: BOTH GROWTH-PLATE RESULTS ARE AT THE TOP
  OF THE RANGE. trompet2024's +61% pool was at 25 mg/kg and li2021's stature at
  20 mg/kg. Nobody has tested a lower dose at a growth plate in any species. Starting
  low is a bet that costs one six-month readout cycle if it is wrong, and saves the
  entire manufacturing and formulation burden if it is right.
""")

# ---------------------------------------------------------------------------
print("="*80)
print("THE SIMPLIFIED PULSE - MID ANCHOR, 60 kg")
print("="*80)
hed = 5.0 * KM_M / KM_H
target_free = hed * BW
ESC = [0.25, 0.50, 1.00, 1.00]
print(f"target dose {target_free:.1f} mg free base = {target_free*SALT:.1f} mg salt = "
      f"{target_free*SALT/CONC:.2f} mL at {CONC:.0f} mg/mL -> ONE SITE\n")
print(f"{'dose':>5}{'day':>6}{'interval':>11}{'%':>7}{'salt':>10}{'volume':>9}  phase")
day, cum = 1, 0.0
for i in range(1, N_DOSES+1):
    frac = ESC[i-1] if i <= len(ESC) else 1.0
    if i == 1:   iv, ph = "-",    "START - observe 2 h"
    elif i <= 3: iv, ph = "48 h", "escalation"
    elif i <= 8: iv, ph = "48 h", "plateau"
    elif i == 9: iv, ph = "72 h", "taper"
    else:        iv, ph = "96 h", "taper - final"
    salt = target_free * frac * SALT
    cum += salt
    print(f"{i:>5}{day:>6}{iv:>11}{frac:>6.0%}{salt:>8.1f} mg{salt/CONC:>7.2f} mL  {ph}")
    day += 2 if i < 8 else (3 if i == 8 else 4)
print(f"\n  TOTAL {cum:.0f} mg of dihydrochloride per pulse at {BW:.0f} kg  ({cum/1000:.2f} g)")
print(f"  Against the HIGH anchor's 877 mg: {100*(1-cum/877):.0f}% less drug, and every dose")
print(f"  is a SINGLE injection under 1 mL.")
print("""
  ⭐ THE ESCALATION IS SHORTER TOO. The HIGH anchor needed four escalation steps
     because the top dose is far above anything ever given systemically. From the MID
     anchor the target is inside the published effective range from the start, so
     three steps suffice - and the first dose is 7 mg, which is a trivial exposure to
     open a first-in-human sequence with.

  ⛔ WHAT DOES NOT CHANGE, AND MUST NOT BE READ AS SIMPLIFIED AWAY:
     · the blackout list - it is about receptor occupancy, not dose
     · the taper - the adaptation argument is dose-independent
     · contraception counselling - teratogenicity is not a high-dose-only property
     · the surveillance, especially upper-GI symptoms and any hip or knee pain
     · ONE PULSE, then the six-month readout, then decide
     · and the three real blockers: no GMP material, no aqueous formulation
       demonstrated at any concentration for SAG itself, and no Smoothened agonist
       has ever been given to a human by any route
""")
