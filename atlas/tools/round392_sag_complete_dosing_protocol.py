#!/usr/bin/env python3
"""
R392 - THE COMPLETE SAG DOSING PROTOCOL, EVERY PARAMETER COMPUTED.

Supersedes the dosing paragraphs of R388 (flat 11 doses) and R389 (tapered 10 doses)
by adding the element both were missing: a FIRST-PULSE DOSE ESCALATION, which is
mandatory because no Smoothened agonist has ever been given to a human by any route.

Every number below is either (a) taken from a named primary, or (b) arithmetic on
one, and marked as such. Nothing is invented.
"""

MW_FREE, MW_SALT = 490.06, 562.98      # PubChem CID 5284330 / 154884292
SALT_FACTOR = MW_SALT / MW_FREE         # 1.149

KM_MOUSE, KM_HUMAN = 3.0, 37.0          # FDA BSA allometry
MOUSE_MGKG = 20.0                       # li2021, s.c., every other day
TARGET_MGKG = MOUSE_MGKG * KM_MOUSE / KM_HUMAN   # 1.622 mg/kg

CONC = 30.0                             # mg/mL, the formulation requirement (R388)
MAX_PER_SITE = 2.0                      # mL, conventional s.c. limit

ESCALATION = [0.10, 0.25, 0.50, 1.00]   # fractions of target, doses 1-4
N_TOTAL = 10                            # 8 at q2d + 1 at 72h + 1 at 96h (R389 taper)

print("="*80)
print("R392  SAG DIHYDROCHLORIDE - COMPLETE DOSING PROTOCOL")
print("="*80)
print(f"""
ANCHOR      li2021: SAG 20 mg/kg SUBCUTANEOUS EVERY OTHER DAY, mouse
SCALING     FDA body-surface-area allometry, Km mouse {KM_MOUSE:.0f} / human {KM_HUMAN:.0f}
TARGET      {TARGET_MGKG:.3f} mg/kg per administration (free-base equivalent basis)
SALT        dihydrochloride, MW {MW_SALT} vs free base {MW_FREE} -> x{SALT_FACTOR:.3f}
CROSS-CHECK trompet2024 (25 mg/kg i.p. daily x7, NORMAL mice, pool +61%) scales to
            0.85 g/pulse at 60 kg against li2021's 1.07 g - ratio 1.26. Independent
            labs, routes, durations and endpoints converge. The target is robust.
""")

# ---------------------------------------------------------------------------
# 1. THE DOSE TABLE
# ---------------------------------------------------------------------------
print("="*80)
print("1. DOSE BY BODY WEIGHT  (target dose, once escalation is complete)")
print("="*80)
print(f"{'weight':>8}{'target dose':>14}{'as 2HCl salt':>15}{'volume @30 mg/mL':>19}{'sites':>7}")
for bw in (50, 55, 60, 65, 70, 75, 80):
    d = TARGET_MGKG * bw
    salt = d * SALT_FACTOR
    vol = salt / CONC
    sites = max(1, -(-vol // MAX_PER_SITE))
    print(f"{bw:>6} kg{d:>11.1f} mg{salt:>12.1f} mg{vol:>16.2f} mL{int(sites):>7}")
print("""
  ⚠ 'target dose' is expressed as FREE-BASE EQUIVALENT because that is what li2021
    dosed. The mass you weigh out is the SALT column - multiply by 1.149. Getting
    this backwards under-doses by 13%.
  ⭐ NOTE THE SITE COUNT. At 30 mg/mL anyone above ~65 kg needs THREE injection sites
    per administration, which is a real adherence cost over 10 doses. Specifying the
    formulation at 50 mg/mL instead brings every weight here to TWO sites or fewer
    and is the single cheapest improvement available - ask the formulator for 50,
    accept 30.""")

# ---------------------------------------------------------------------------
# 2. THE SCHEDULE - escalation, plateau, taper
# ---------------------------------------------------------------------------
BW = 60.0
target = TARGET_MGKG * BW
print("\n"+"="*80)
print(f"2. THE PULSE - 10 DOSES OVER 22 DAYS  (worked at {BW:.0f} kg)")
print("="*80)
print(f"{'dose':>5}{'day':>6}{'interval':>11}{'fraction':>10}{'free-base':>12}{'SALT mass':>12}{'volume':>10}  phase")
day = 1
cum = 0.0
rows = []
for i in range(1, N_TOTAL+1):
    frac = ESCALATION[i-1] if i <= len(ESCALATION) else 1.00
    if i == 1:      interval, phase = "-",     "ESCALATION - observe 2 h"
    elif i <= 4:    interval, phase = "48 h",  "ESCALATION"
    elif i <= 8:    interval, phase = "48 h",  "plateau"
    elif i == 9:    interval, phase = "72 h",  "TAPER"
    else:           interval, phase = "96 h",  "TAPER - final dose"
    d = target * frac
    salt = d * SALT_FACTOR
    cum += salt
    print(f"{i:>5}{day:>6}{interval:>11}{frac:>9.0%}{d:>10.1f} mg{salt:>9.1f} mg{salt/CONC:>7.2f} mL  {phase}")
    rows.append((i, day, salt))
    day += 2 if i < 8 else (3 if i == 8 else 4)
print(f"\n  TOTAL PER PULSE at {BW:.0f} kg: {cum:.0f} mg of dihydrochloride ({cum/1000:.2f} g)")
flat = target * SALT_FACTOR * 11
print(f"  Against R388's flat 11 doses at target: {flat:.0f} mg -> the escalating,")
print(f"  tapered pulse uses {100*(1-cum/flat):.0f}% LESS drug and is safer at both ends.")
print("""
  WHY ESCALATE - this is not caution, it is the only defensible design.
    · NO Smoothened agonist has ever been given to a human by any route (R390,
      re-confirmed on clinicaltrials.gov three ways). There is no tolerated human
      dose, no human PK, no human adverse-event profile.
    · The published effective systemic range in mice spans FORTY-FOLD (0.5 to 20+
      mg/kg), and where in it a growth plate responds is unmeasured (g_l12_390a).
      Escalation walks up that range instead of guessing a point inside it.
    · It costs nothing - it uses LESS total drug than the flat schedule (above).
  WHY TAPER - R389. The pathway adapts BELOW Smoothened (cohen2015: PTCH1 up, Gli
    down, Gli isoform stability), HHIP is a Gli target that the agonist INDUCES
    (chuang1999) while Smo activation DEGRADES HHIP protein (kwong2014). Stopping
    abruptly removes the degradation arm instantly and leaves the induced brake -
    a predicted rebound trough BELOW baseline. That matters here and almost nowhere
    else, because six doses of a Smoothened ANTAGONIST fused a normal growth plate
    (newton2019). The dangerous moment is the STOP, not the dosing.""")

# ---------------------------------------------------------------------------
# 3. RECONSTITUTION AND FORMULATION
# ---------------------------------------------------------------------------
print("\n"+"="*80)
print("3. MATERIAL, RECONSTITUTION AND FORMULATION")
print("="*80)
per_pulse_g = cum/1000
print(f"""
  MATERIAL   SAG dihydrochloride. CAS 364590-63-6 refers to the FREE BASE - specify
             the DIHYDROCHLORIDE explicitly when ordering. >=98% HPLC with a
             certificate of analysis. Quantity: {per_pulse_g:.2f} g per pulse at {BW:.0f} kg;
             {per_pulse_g*4:.1f} g covers four pulses (one year at a 3-month interval).
  ⛔ AT THIS SCALE DO NOT BUY CATALOGUE. Order {per_pulse_g*4:.0f}-{per_pulse_g*4+2:.0f} g as a custom synthesis -
     490 Da, published route, ordinary contract job - and specify an impurity
     profile, residual-solvent and endotoxin package in the same order. The
     incremental cost of pharmaceutical grade on a batch already being made is far
     smaller than qualifying material on top of nothing.

  FORMULATION TARGET  aqueous, >={CONC:.0f} mg/mL, isotonic, pH 4-6, sterile-filtered
                      0.22 um, in a sealed multi-dose vial with a preservative-free
                      single-use-per-dose discipline.
  ⛔ DO NOT SCALE li2021's DMSO VEHICLE. Their 5 mM DMSO stock is 2.45 mg/mL; a {BW:.0f} kg
     dose in it is {target*SALT_FACTOR/2.45:.0f} mL of DMSO subcutaneously. That is not a dosing option.
  ⚠ THE FORMULATION IS NOT YET DEMONSTRATED (g_l12_388b). Aqueous solubility of the
    dihydrochloride is not published as a number. The preformulation work is
    ordinary - equilibrium solubility across pH 3-7.4 at 5 and 25 C, then tonicity,
    buffer, stability and a rodent local-tolerance study at the intended
    concentration and volume - but it must be DONE, not assumed.
  ⭐ FALLBACK TRIGGER: if SAG dihydrochloride cannot reach {CONC:.0f} mg/mL, switch to
    SAG21k, which is several-fold more potent AND has a demonstrated aqueous in vivo
    vehicle (PBS, lee2016colitis). That trade costs the direct link to trompet2024
    and li2021, which is why it is the fallback and not the lead.

  STORAGE     lyophilised powder: sealed, desiccated, -20 C. EQUILIBRATE THE SEALED
              VIAL TO ROOM TEMPERATURE (~20 min) BEFORE OPENING - the powder is
              hygroscopic and opening it cold condenses water onto it.
              Reconstituted solution: 2-8 C, and treat as single-day unless a
              stability study says otherwise.""")

# ---------------------------------------------------------------------------
# 4. ADMINISTRATION
# ---------------------------------------------------------------------------
print("="*80)
print("4. ADMINISTRATION")
print("="*80)
print(f"""
  ROUTE       subcutaneous. Same route he already uses for growth hormone.
  NEEDLE      27-30 G, 8-13 mm, standard insulin/GH-style syringe or pen-fill.
  SITES       abdomen (avoiding 5 cm around the umbilicus) and anterior/lateral
              thigh. Split any volume above {MAX_PER_SITE:.0f} mL across two sites.
  ⭐ ROTATE AGAINST THE GH SITES, NOT JUST WITHIN THIS DRUG. He is already injecting
    growth hormone subcutaneously. Two agents into the same lipid depot risks local
    lipohypertrophy, which changes absorption of BOTH. Keep a written rotation map
    and put SAG on the contralateral quadrant from that day's GH.
  TECHNIQUE   pinch a fold, 45-90 degrees, inject slowly over 10-20 s, hold 5 s
              before withdrawing. Do not massage the site.
  FIRST DOSE  give it where medical observation is available and OBSERVE FOR 2 HOURS.
              There is no human exposure to this class, so the first administration
              is a first-in-human event regardless of how it is framed.
  TIMING      same time of day each dose. No food-effect data exist for the
              subcutaneous route, so consistency substitutes for knowledge.
  MISSED DOSE if <24 h late, give it and resume the original day grid. If >24 h late,
              SKIP it and resume - do not double. During the TAPER (doses 9-10) a
              missed dose should be given late rather than skipped, because the whole
              point of those two doses is to avoid an abrupt stop.""")

# ---------------------------------------------------------------------------
# 5. WHAT MUST NOT BE TAKEN DURING THE PULSE
# ---------------------------------------------------------------------------
print("="*80)
print("5. THE BLACKOUT LIST - direct pharmacological opponents DURING the pulse")
print("="*80)
print("""
  These are not background contraindications. During a pulse they are agents acting
  on the same receptor in the opposite direction, and taking one wastes the pulse.

  ⛔ ABSOLUTE - SMO ANTAGONISTS
       vismodegib, sonidegib, glasdegib. Direct antagonists at the target.
  ⛔ ABSOLUTE - AZOLES THAT ANTAGONISE SMO AT ORDINARY ANTIFUNGAL EXPOSURE
       ITRACONAZOLE, POSACONAZOLE (kim2010itra, chen2016posa). If an oral antifungal
       is needed use TERBINAFINE or FLUCONAZOLE - both return zero hedgehog records.
  ⛔ GLUCOCORTICOIDS BY ANY ROUTE - oral, inhaled, topical, intranasal,
       intra-articular. Cortisol competes with cholesterol at the SMO cysteine-rich
       domain and inhibits Shh/SMO, verified by a CRISPR SMO L116A knock-in
       (lu2025cortisol); dexamethasone and budesonide inhibit hedgehog. If an
       inhaled steroid is unavoidable use FLUTICASONE (axelsson2019).
  ⛔ MEGADOSE VITAMIN D3 - binds SMO, cyclopamine-sensitive, phenocopies the SMO null
       (bijlsma2006). Adequacy is non-negotiable; target mid-normal 25-OH-D and do
       not megadose.
  ⛔ THE DHCR7-INHIBITING SHELF - raises 7-DHC, whose B-ring oxysterol inhibits SMO
       (sever2016): HYDROXYZINE, fluoxetine, aripiprazole, trazodone, buspirone,
       lurasidone, ziprasidone, vilazodone, cariprazine, nebivolol, rotigotine,
       amiodarone. Hydroxyzine is a common antihistamine - ask specifically.
  ⛔ HEPARIN, LMWH, PENTOSAN POLYSULFATE, SULODEXIDE - soluble sulfated GAGs impair
       Shh release AND potentiate HHIP (jakobs2019heparin, griffiths2021).
  ⛔ DNMT INHIBITORS (azacitidine, decitabine) - re-express HHIP (zhang2020hhipmeth).
  ✓ STATINS ARE FINE. Cholesterol is SMO's endogenous CRD agonist so lowering it
       looked like a cost; 300 children on the UK Paediatric FH Register gave
       age-adjusted annual height 4.45 cm on statin vs 4.60 off, P=0.73
       (humphries2018). And SAG binds the 7TM site, not the CRD.
  ⚠ THE STACK ITSELF IS UNRESOLVED. SAG's metabolic route is not published in any
       species - no CYP identification, no transporter data, no protein binding.
       Erdafitinib is ~39% CYP2C9 and ~20% CYP3A4 and a P-gp substrate. THE
       INTERACTION IS SIMPLY UNKNOWN, and that is a genuine hole, not a reassurance.""")

# ---------------------------------------------------------------------------
# 6. MONITORING
# ---------------------------------------------------------------------------
print("="*80)
print("6. MONITORING")
print("="*80)
print("""
  BEFORE THE FIRST PULSE (baseline, and most of this is overdue anyway)
    · ⭐ ΔBA/ΔCA by BoneXpert on serial hand films - STILL THE PRIMARY, STILL NOT DONE.
         It decides whether a pool agent is worth giving him at all.
    · standing AND sitting height, at a FIXED TIME OF DAY (the diurnal swing exceeds
      a year of expected gain)
    · knee and spine imaging; lateral thoracolumbar film + DXA
    · FBC, LFT, U&E, glucose, HbA1c
    · ultrasensitive oestradiol by LC-MS/MS, IGF-1, TSH/fT4/fT3, HOMA-IR, 25-OH-D
    · a documented GI history - baseline bowel habit, any reflux or dysphagia
    · photograph of scalp/hair density (see PD below)

  DURING THE PULSE
    · daily: injection-site reaction, any new GI symptom
    · ⭐ UPPER GI AND OBSTRUCTIVE SYMPTOMS SPECIFICALLY - abdominal pain, distension,
      vomiting, early satiety, change in bowel habit. The predicted lesion is
      MUSCULARIS, not mucosa, and the segment at risk is the STOMACH and
      gastroesophageal junction, NOT the colorectum (li2026stromalhh). Colonoscopy is
      aimed at the compartment the biology says is protected.
    · weekly weight

  PHARMACODYNAMICS - the honest position
    · THERE IS NO ACCESSIBLE PD READOUT AT THE GROWTH PLATE. Nothing measurable in
      blood reports on it.
    · ⭐ WHAT IS FREE: hair and taste. The antagonist class produces ALOPECIA and
      AGEUSIA in humans at high incidence (zheng2025faers) - those are the human
      tissues that visibly report hedgehog tone. Their mirror observation under an
      agonist costs nothing and is worth recording.
    · A GLI1 qPCR readout on a skin punch biopsy is the obvious biochemical analogue
      but no validated protocol for the AGONIST direction was found this round -
      recorded as a gap, not a recommendation.

  AT 6 MONTHS - THE READOUT THAT DECIDES EVERYTHING
    · ΔBA/ΔCA · standing AND sitting height at fixed time · knee and spine imaging
      for plate width AND bar formation · DXA
    · ⭐ SITTING HEIGHT IS THE ENDPOINT THAT MATTERS, because the trunk is the
      compartment this route was chosen to reach and the depot could not.

  CONTRACEPTION
    · ⭐ SAG is a demonstrated teratogen - a SINGLE 25 mg/kg dose in pregnant mice
      gave cleft lip and palate, cranial bone abnormalities and haematomas, critical
      window E9.5-E10.5 (mao2026sag). Vismodegib and sonidegib carry MALE-PATIENT
      contraception requirements for embryo-fetal toxicity and potential seminal
      transfer. Counselling must cover the pulse AND a washout after it.""")

# ---------------------------------------------------------------------------
# 7. STOP RULES AND INTERVAL
# ---------------------------------------------------------------------------
print("="*80)
print("7. STOP RULES, INTERVAL, AND COURSE")
print("="*80)
print("""
  STOP THE PULSE IMMEDIATELY FOR
    · any obstructive GI symptom - pain, distension, vomiting, absolute constipation
    · any new skin lesion
    · any hip, groin, thigh or knee pain, or a limp -> IMMEDIATE imaging. Slipped
      capital femoral epiphysis is quadruple-stacked on this stack (erdafitinib
      postmarketing: 3 of 5 paediatric cases, median onset 137 days; GH; a widened
      physis is the mechanical substrate)
    · severe injection-site reaction or any systemic hypersensitivity

  DO NOT PROCEED TO A SECOND PULSE IF
    · the growth plate widens WITHOUT height gain - that is charge without
      discharge, this file's failure mode #1, eight prior instances. Plate width is
      TARGET ENGAGEMENT, NOT EFFICACY. Both must move.
    · ΔBA/ΔCA accelerates - the pool was spent rather than enlarged
    · any new cartilaginous lesion (enchondroma, osteochondroma). This stack is
      already Ihh-elevating through erdafitinib and lesions form a BAND (zhou2015a,
      li2021 at the two ends)

  INTERVAL   >=3 months, preferably 6. DERIVED, NEVER MEASURED IN ANY SPECIES.
             Two bounds and nothing between them: trompet2024's 3-week input was
             STILL WIDENING at 6 months, so re-dosing sooner buys nothing;
             orikasa2024's PERMANENT activation expanded the pool then CONVERTED it
             to trabecular bone with no final length gain, so continuous occupancy
             is actively harmful. ⛔ NO CONTINUOUS DOSING, EVER.
  COURSE     ONE PULSE. Then the 6-month readout. Then decide.
             Do not schedule pulse 2 before the pulse 1 readout exists.
             At bone age 16 the window is ~1-3 years, so at most 2-6 pulses total -
             but that is a ceiling, not a plan.

  ⛔ WHAT THIS PROTOCOL STILL CANNOT TELL YOU
    · whether systemic SAG lengthens bone in a normal animal (g_l12_388a) - the
      experiment exists unpublished inside rundle2023, which measured the
      contralateral femur and used its length only as a normaliser
    · where in the 40-fold range the plate responds (g_l12_390a)
    · whether the aqueous formulation is achievable (g_l12_388b)
    · whether an adult gut thickens at the high dose (g_l12_389a)
    · whether the rebound trough is real and whether the taper prevents it (g_l12_389b)
    · what SAG does in a human, at all""")
