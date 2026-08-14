#!/usr/bin/env python3
"""
ROUND 388. THE SYSTEMIC SAG REGIMEN, DERIVED FROM THE ONLY PUBLISHED SYSTEMIC SAG STUDY
THAT HAS A STATURE ENDPOINT, A TOXICITY SCREEN AND A FORMULATION.

li2021 (Mol Ther Methods Clin Dev): Acan-creERT Ihh-ablation dysplasia model.
  DOSE      20 ug/g  = 20 mg/kg
  ROUTE     SUBCUTANEOUS
  SCHEDULE  EVERY OTHER DAY
  DURATION  from P7 or P14 to P30 (16-23 days)
  VEHICLE   SAG dissolved in DMSO to 5 mM, then diluted with normal saline
  RESULT    body length 117.2 +/- 6.9 -> 133.2 +/- 6.1 mm; femur +67.4%; tibia +33.1%;
            L3 VERTEBRA +32.1%; skull +18.5%
  TOX       all viscera inspected, no abnormality or tumorigenesis; INTESTINAL
            HYPERPLASIA IN 6.1% OF TREATED MICE

⚠⚠ CORR-203 GOVERNS THE EFFECT SIZE AND NOTHING ELSE. This is RESTORATION in an
   Ihh-ablated dysplasia. +67% femur is a rescued deficit, NOT elevation above normal.
   WHAT TRANSFERS IS THE DOSE, THE ROUTE, THE SCHEDULE, THE FORMULATION, THE TOXICITY
   SCREEN, AND THE FACT THAT IT REACHED THE VERTEBRAE.
"""
MW_FREE, MW_SALT = 490.06, 562.98
KM_MOUSE, KM_HUMAN = 3.0, 37.0
MOUSE_MGKG = 20.0
DAYS, EVERY_N = 21, 2

hed = MOUSE_MGKG * KM_MOUSE / KM_HUMAN
doses = DAYS // EVERY_N + 1
print("=" * 78); print("1. THE HUMAN-EQUIVALENT REGIMEN"); print("=" * 78)
print(f"mouse: {MOUSE_MGKG:.0f} mg/kg subcutaneous EVERY OTHER DAY")
print(f"HED  : {hed:.2f} mg/kg per dose  (Km {KM_MOUSE}/{KM_HUMAN})")
print(f"\n{'body wt':>8s} {'per dose':>10s} {'doses/pulse':>12s} {'g per 3-wk pulse':>18s}")
for bw in (50, 60, 70):
    per = hed * bw
    print(f"{bw:6d} kg {per:8.0f} mg {doses:11d} {per*doses/1000:16.2f} g")
print(f"\n  pulse = {DAYS} days, every other day = {doses} doses - matching li2021's 16-23 day duration")
print("  and the 3-week depot life that sets the local protocol's pulse length.")

print("\n" + "=" * 78); print("2. WHY trompet2024's SYSTEMIC ARM IS NOT THE REGIMEN TO COPY"); print("=" * 78)
print("""  trompet2024 : 25 mg/kg INTRAPERITONEAL, ONCE DAILY, 7 days  -> pool +61%, LENGTH
                UNINFORMATIVE (95% CI -2.03 to +6.23 mm on a 12.7 mm bone, R368)
  mao2026sag  : 25 mg/kg SINGLE INTRAPERITONEAL -> reduced proliferation, delayed G0/G1
  li2021      : 20 mg/kg SUBCUTANEOUS, EVERY OTHER DAY, 16-23 days -> stature corrected,
                viscera clean
  → THE TOLERATED, EFFECTIVE REGIMEN IS THE LOWER-INTENSITY ONE: 20 mg/kg every other day
    is HALF the cumulative daily exposure of the 25 mg/kg arm that mao2026sag flags as
    anti-proliferative, and it is the arm with the stature result and the clean viscera.""")

print("\n" + "=" * 78); print("3. THE FORMULATION PROBLEM, WHICH IS THE REAL SYSTEMIC BLOCKER"); print("=" * 78)
print("li2021's vehicle is 5 mM SAG in DMSO diluted into saline. Scale it and it breaks:")
conc_5mM_mg_mL = 5e-3 * MW_FREE
print(f"  5 mM SAG free base = {conc_5mM_mg_mL:.2f} mg/mL")
for bw in (60,):
    per = hed * bw
    print(f"  a {bw} kg human dose is {per:.0f} mg -> {per/conc_5mM_mg_mL:.1f} mL OF 5 mM STOCK")
    print(f"     mouse comparison: a 25 g mouse dose is {MOUSE_MGKG*0.025:.2f} mg -> "
          f"{MOUSE_MGKG*0.025/conc_5mM_mg_mL*1000:.0f} uL. Trivial in a mouse, impossible in a human.")
print("\n  SUBCUTANEOUS VOLUME IS LIMITED TO ROUGHLY 1-2 mL PER SITE. So the formulation must")
print("  be concentrated, and that is what the DIHYDROCHLORIDE SALT EXISTS FOR:")
for mg_mL in (5.63, 10, 20, 30, 50):
    mM = mg_mL / MW_SALT * 1000
    per = hed * 60
    vol = per / mg_mL
    sites = max(1, int(vol / 2.0 + 0.999))
    flag = "  <- feasible" if vol <= 6 else ""
    print(f"   {mg_mL:5.1f} mg/mL ({mM:5.1f} mM salt): a 60 kg dose = {vol:5.1f} mL -> {sites} s.c. site(s){flag}")
print("""
→ THE REQUIREMENT IS AN AQUEOUS FORMULATION OF SAG DIHYDROCHLORIDE AT >=30 mg/mL.
  That is a FORMULATION DEVELOPMENT TASK - solubility, tonicity, pH, stability - NOT a
  scientific unknown, and the salt was made precisely because the free base is cLogP 6.79.
⛔ DO NOT SCALE THE DMSO VEHICLE. 40 mL of DMSO subcutaneously is not a dosing option.""")

print("\n" + "=" * 78); print("4. MATERIAL, AND WHY THE SYSTEMIC ROUTE MAKES GMP EASIER TO JUSTIFY"); print("=" * 78)
for bw in (60,):
    g = hed*bw*doses/1000
    print(f"  one 3-week pulse at {bw} kg = {g:.2f} g of drug substance")
    print(f"  four pulses per year        = {g*4:.2f} g/yr")
print("""  At catalogue prices (order 300-500 USD per 10 mg) a single pulse is tens of thousands
  of dollars and is simply the wrong way to buy it.
⭐ AT GRAM SCALE YOU COMMISSION SYNTHESIS RATHER THAN BUYING CATALOGUE - SAG is 490 Da with
  a published route, and a multi-gram batch is an ordinary contract job. AND THAT IS THE
  POINT THAT REFRAMES THE WHOLE BLOCKER: once a custom batch is being made anyway, the
  INCREMENTAL cost of running it to GMP with an impurity and endotoxin package is far
  smaller than GMP on top of nothing. THE SYSTEMIC ROUTE'S LARGER DOSE MAKES THE
  QUALIFICATION PROBLEM EASIER TO JUSTIFY, NOT HARDER.""")

print("\n" + "=" * 78); print("5. SYSTEMIC VERSUS THE DEPOT - THE HONEST LEDGER"); print("=" * 78)
print("""  SYSTEMIC WINS ON
   · NO PROCEDURE AT ALL - no cannula, no sedation, no fluoroscopy, no instrument near a
     physis, and the SCFE risk from instrumentation disappears entirely
   · ⭐ IT REACHES THE TRUNK. li2021: L3 VERTEBRAL LENGTH +32.1%. The residual at bone age
     16 is trunk-dominant and a knee depot cannot reach a vertebral plate at all. THIS IS
     THE SINGLE BIGGEST ARGUMENT AND IT IS DECISIVE ON COMPARTMENT GROUNDS.
   · every growth plate simultaneously, including ones nobody would instrument
   · SUBCUTANEOUS - the same route he already uses for GH
   · dose is adjustable and reversible day to day; a depot cannot be taken back
   · formulation, schedule and a toxicity screen are all published

  SYSTEMIC LOSES ON
   · ~1 g per pulse against 2.70 mg for the depot - about 400-fold more drug
   · systemic hedgehog activation is the hazard the local route was designed to avoid;
     the counterweight is heine2011 (one week in neonatal animals, tolerated, no tumour
     promotion) and li2021 (2-3 weeks, viscera clean)
   · INTESTINAL HYPERPLASIA IN 6.1% of li2021's treated mice - the classic Hh-agonist gut
     effect, and the one finding that is NOT clean
   · the depot has the only true LENGTH endpoint in a NORMAL animal (trompet2024's bead);
     every systemic length result is a rescue in a deficient model""")

# ---------------------------------------------------------------------------
# 6. THE CROSS-CHECK THAT MATTERS: TWO INDEPENDENT MOUSE REGIMENS, ONE HUMAN DOSE
# ---------------------------------------------------------------------------
# li2021      : 20 mg/kg s.c. EVERY OTHER DAY over ~21 days  (stature + tox + vertebrae)
# trompet2024 : 25 mg/kg i.p. ONCE DAILY over 7 days, in NORMAL mice (pool +61%)
# Scale both by the same FDA BSA factor and compare TOTAL DRUG per pulse.
BW = 60.0
li_total = MOUSE_MGKG * KM_MOUSE / KM_HUMAN * BW * (DAYS // EVERY_N + 1)
tro_total = 25.0 * KM_MOUSE / KM_HUMAN * BW * 7

print(f"""
==============================================================================
6. THE CROSS-CHECK - TWO INDEPENDENT MOUSE REGIMENS LAND ON THE SAME HUMAN DOSE
==============================================================================
  li2021      20 mg/kg s.c. every other day x 21 d  -> {li_total/1000:.2f} g per pulse at {BW:.0f} kg
  trompet2024 25 mg/kg i.p. once daily      x  7 d  -> {tro_total/1000:.2f} g per pulse at {BW:.0f} kg
  ratio = {li_total/tro_total:.2f}x

⭐ TWO REGIMENS FROM DIFFERENT LABS, DIFFERENT ROUTES, DIFFERENT DURATIONS, DIFFERENT
  MODELS AND DIFFERENT ENDPOINTS CONVERGE ON ROUGHLY ONE GRAM PER THREE-WEEK PULSE IN A
  60 kg HUMAN. That is not a coincidence of arithmetic - both were dosed to the top of
  what a mouse tolerates, and BSA scaling is the standard bridge. THE NUMBER IS ROBUST.

⭐ AND THEY ARE COMPLEMENTARY, WHICH IS THE ARGUMENT FOR THE SYSTEMIC ROUTE:
   · trompet2024 is the NORMAL-ANIMAL arm - systemic SAG in wild-type mice raised the
     resting-zone stem-cell pool +61% with the divisions actually happening (singlets
     falling, doublets and triplets rising). CORR-203 does not touch it.
   · li2021 is the DOSE/ROUTE/FORMULATION/TOX/COMPARTMENT arm - and it is the only one
     that measured a VERTEBRA.
  Neither alone justifies the route. Together they supply the pool mechanism in a normal
  animal and the practical regimen with the trunk reach.
⛔ WHAT NEITHER SUPPLIES IS A LENGTH ENDPOINT FROM SYSTEMIC SAG IN A NORMAL ANIMAL.
  trompet2024's own systemic length arm is UNINFORMATIVE, not null (7 days of drug read
  2 days later, n=7 vs 5, 95% CI -2.03 to +6.23 mm on a 12.7 mm bone). THAT REMAINS THE
  SINGLE LARGEST GAP ON THIS ROUTE AND IT IS AN UNRUN EXPERIMENT, NOT A NEGATIVE.
""")
