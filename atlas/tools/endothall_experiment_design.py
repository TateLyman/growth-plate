#!/usr/bin/env python3
"""
Round 135. Full in-silico specification of the decisive experiment for the
NPR2 receptor-phosphorylation branch:

    continuous delivery of a PPP-family phosphatase inhibitor to juvenile
    wild-type mice, dosed to skeletal maturity, with long-bone length as the
    endpoint.

Everything here is arithmetic on values already in the atlas. Every input is
tagged MEASURED (with its source) or ASSUMED (with its basis), and the script
prints the tag with the number so no derived value can be mistaken for data.

Run:  python3 atlas/tools/endothall_experiment_design.py
"""
import math
import os
import statistics as st
import warnings

warnings.filterwarnings("ignore")

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------
MW_ENDOTHALL = 186.16   # MEASURED: C8H10O5, formula mass
MW_LB100 = 268.3        # MEASURED: feng2023 MS parent ion m/z 269.2 -> M = 268.3
IC50_PP2A_nM = 95.0     # MEASURED: rollema2025, isolated PP2A


def ng_per_mL_to_nM(ng, mw=MW_ENDOTHALL):
    return ng / mw * 1000.0


def nM_to_ng_per_mL(nm, mw=MW_ENDOTHALL):
    return nm * mw / 1000.0


# --------------------------------------------------------------------------
# 1. POWER. Raw per-animal data from shuhaibar2017 eLife 31343 Figure 1
#    source data. This is the only dataset anywhere that gives the variance of
#    the exact endpoints this experiment would measure, in the exact strain,
#    at the exact ages.
# --------------------------------------------------------------------------
ELIFE = os.environ.get(
    "ELIFE_FIG1",
    "/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b"
    "/scratchpad/elife31343/elife_poa_e31343_Figure_1_source_data_1.xlsx",
)

# Fallback: the summary statistics computed from that file at round 135, kept
# here so the script runs without the workbook. MEASURED, recomputed from raw.
WT_STATS = {
    # endpoint: {age_weeks: (n, mean, sd)}
    "femur_mm":        {4: (15, 11.930, 1.402), 8: (12, 14.553, 0.445), 16: (13, 16.028, 0.610)},
    "tibia_mm":        {4: (15, 14.912, 1.459), 8: (12, 17.148, 0.518), 16: (13, 17.785, 0.660)},
    "body_length_mm":  {4: (18, 75.967, 7.706), 8: (12, 91.500, 3.205), 16: (13, 96.154, 3.716)},
    "cranial_width_mm": {4: (10, 9.773, 0.608), 8: (12, 10.602, 0.339), 16: (13, 10.478, 0.303)},
}
SEVEN_E_EFFECT = {  # MEASURED: same source, per cent difference 7E/7E vs wild type
    "femur_mm":        {4: 7.06, 8: 13.91, 16: 8.44},
    "tibia_mm":        {4: 5.63, 8: 10.15, 16: 8.80},
    "body_length_mm":  {4: 5.89, 8: 10.00, 16: 7.97},
    "cranial_width_mm": {4: 2.16, 8: -2.36, 16: 2.54},
}


def n_per_group(effect_frac, cv, power=0.80, alpha=0.05):
    """Two-sample two-sided t-test, normal approximation with a small-sample
    correction. effect_frac and cv are fractions of the control mean."""
    z_a = 1.959963985
    z_b = 0.8416212336 if abs(power - 0.80) < 1e-9 else 1.2815515655
    d = effect_frac / cv
    n = 2.0 * (z_a + z_b) ** 2 / d ** 2
    return math.ceil(n + 1)  # +1 for the t vs z correction


def power_table():
    print("=" * 78)
    print("1. POWER  -  from shuhaibar2017 eLife 31343 Fig 1 raw per-animal data")
    print("=" * 78)
    print("   wild-type coefficient of variation, and the 7E genetic effect for scale\n")
    for ep, ages in WT_STATS.items():
        print(f"  {ep}")
        for age, (n, mean, sd) in sorted(ages.items()):
            cv = sd / mean
            print(f"    wk{age:>2}: n={n:2d} mean={mean:8.3f} sd={sd:6.3f} "
                  f"CV={100*cv:5.2f}%   7E effect {SEVEN_E_EFFECT[ep][age]:+6.2f}%")
        print()
    print("  n PER GROUP for 80% power, alpha 0.05, two-sided, by target effect size")
    print("  (the 7E genotype is the ceiling; a drug is assumed to reach a fraction of it)\n")
    hdr = "    endpoint/age      " + "".join(f"{p:>8}" for p in
                                             ["+1%", "+2%", "+3%", "+4%", "+6%", "+8%"])
    print(hdr)
    for ep in ("femur_mm", "tibia_mm", "body_length_mm"):
        for age in (8, 16):
            n, mean, sd = WT_STATS[ep][age]
            cv = sd / mean
            row = f"    {ep[:14]:<14} wk{age:<3}"
            for eff in (0.01, 0.02, 0.03, 0.04, 0.06, 0.08):
                row += f"{n_per_group(eff, cv):>8}"
            print(row)
    print()
    print("  READ-OFF: at 8 weeks femur CV is 3.05% and the 7E effect is +13.9%;")
    print("  at 16 weeks CV is 3.81% and the effect has fallen to +8.4%. Eight weeks")
    print("  is both the tighter measurement and the larger signal, so it is the")
    print("  powered endpoint - with 16 weeks kept as the durability question.\n")


# --------------------------------------------------------------------------
# 2. THE VELOCITY-VERSUS-FINAL-SIZE READING OF THE SAME DATA
# --------------------------------------------------------------------------
def velocity_vs_final():
    print("=" * 78)
    print("2. DOES THE 7E ADVANTAGE PERSIST?  (the question this whole project asks)")
    print("=" * 78)
    for ep in ("femur_mm", "tibia_mm", "body_length_mm"):
        e8, e16 = SEVEN_E_EFFECT[ep][8], SEVEN_E_EFFECT[ep][16]
        print(f"  {ep:<16} wk8 {e8:+6.2f}%   wk16 {e16:+6.2f}%   "
              f"retained {100*e16/e8:5.1f}% of the peak advantage")
    print()
    print("  Between 8 and 16 weeks the 7E advantage SHRINKS on every appendicular")
    print("  endpoint - femur keeps 61%, tibia 87%, body length 80%. Cross-sectional")
    print("  cohorts, not longitudinal, so this is suggestive not decisive. But it is")
    print("  the velocity-versus-adult-height dissociation showing up inside the best")
    print("  genetic model this branch has, and no drug can be expected to do better.\n")


# --------------------------------------------------------------------------
# 3. DONNAN PARTITION OF A DIANION INTO GROWTH-PLATE CARTILAGE
# --------------------------------------------------------------------------
def donnan(cF, c0=0.15, z=-2):
    """Ideal Donnan partition of an ion of valence z into a tissue with fixed
    charge density cF (mol/L of tissue water, magnitude) bathed in a 1:1 salt
    at c0. Returns c_in/c_out."""
    c_minus = (-cF + math.sqrt(cF ** 2 + 4 * c0 ** 2)) / 2.0
    lam = c_minus / c0           # Donnan ratio for a monovalent anion
    return lam ** abs(z)


def donnan_table():
    print("=" * 78)
    print("3. HOW MUCH ENDOTHALL ACTUALLY GETS INTO THE MATRIX")
    print("=" * 78)
    print("  Endothall is a DICARBOXYLIC ACID - EPA calls it that explicitly - so at")
    print("  pH 7.4 it is a dianion, and growth-plate matrix is a fixed anionic gel.")
    print("  Fixed charge density, MEASURED (lesperance1992, sodium NMR):")
    print("    calf EPIPHYSEAL cartilage  -0.19 to -0.35 M")
    print("    calf articular cartilage   -0.28 +/- 0.03 M\n")
    print("    |FCD| M   Donnan ratio   partition of a -1 ion   partition of a -2 ion")
    for cF in (0.19, 0.28, 0.35):
        c_minus = (-cF + math.sqrt(cF ** 2 + 4 * 0.15 ** 2)) / 2.0
        lam = c_minus / 0.15
        print(f"    {cF:5.2f}     {lam:6.3f}          {lam:6.3f}                {lam**2:6.3f}")
    print()
    print("  So electrostatic exclusion alone puts interstitial endothall at roughly")
    print("  14 to 30 per cent of the free plasma concentration - a 3 to 7-fold")
    print("  penalty ON TOP OF the plasma-to-medium gap, in the wrong direction.")
    print("  STERIC partitioning is not the problem: at 186 Da the farnum2006 and")
    print("  williams2007 curve sits near 100 per cent (332 Da is ~100%).")
    print("  ASSUMED: ideal Donnan, no activity coefficients, no binding, cartilage")
    print("  water at bath ionic strength. Bovine/calf FCD used for mouse.\n")


# --------------------------------------------------------------------------
# 4. WHAT INFUSION RATE HOLDS A TARGET CONCENTRATION
# --------------------------------------------------------------------------
def infusion_table():
    print("=" * 78)
    print("4. THE INFUSION RATE NEEDED - AND THE TWO PARAMETERS THAT DECIDE IT")
    print("=" * 78)
    print("  Steady state under constant infusion:  C_ss = R_in / CL")
    print("  ASSUMED Vd: a small hydrophilic dianion is largely confined to")
    print("  extracellular water. Mouse ECF ~0.20-0.26 L/kg.")
    print("  MEASURED-ADJACENT t1/2: endothall plasma terminal half-life 5.20 and")
    print("  5.94 h in rat (Lixte patent US20160333024A1, after dosing two ESTER")
    print("  prodrugs, NOT LB-100 - so it is endothall's own elimination only if")
    print("  formation is faster than elimination, which it is here: the parents")
    print("  had half-lives of 0.39-0.92 h).\n")
    print("    Vd(L/kg)  t1/2(h)   CL(mL/h/kg)   mg/kg/day for C_ss = 1uM / 5uM / 10uM")
    for vd in (0.20, 0.26, 0.60):
        for t12 in (3.0, 5.5, 8.0):
            cl = 0.693 * vd / t12 * 1000.0          # mL/h/kg
            out = []
            for target_uM in (1, 5, 10):
                c = nM_to_ng_per_mL(target_uM * 1000)   # ng/mL
                rate = c * cl * 24 / 1e6                # mg/kg/day
                out.append(f"{rate:6.2f}")
            print(f"    {vd:5.2f}    {t12:5.1f}    {cl:9.1f}     " + " / ".join(out))
    print()
    print("  FOR SCALE, the doses this atlas already knows:")
    print("    1.5 mg/kg/day continuous LB-100, 14 d, adult mouse - TOLERATED (martiniova2011)")
    print("    0.5 mg/kg/day average as q2d bolus, juvenile mouse - 42% MORTALITY (fenton2023)")
    print("    2.0 mg/kg/day oral endothall, rat chronic LOAEL, gastric lesions (EPA RED)")
    print("    9.41 mg/kg/day oral endothall, offspring NOAEL (EPA RED)")
    print()
    print("  READ-OFF: across the plausible parameter box, holding 1 uM needs roughly")
    print("  0.1-0.6 mg/kg/day and holding 5-10 uM needs roughly 0.6-6 mg/kg/day. The")
    print("  low end sits UNDER every tolerated dose above; the high end sits over the")
    print("  rat chronic oral LOAEL. The experiment is therefore not obviously")
    print("  impossible and not obviously safe, which is exactly why it has to be run.\n")


# --------------------------------------------------------------------------
# 5. RECONCILING THE HUMAN DATA - WHERE THE MISSING PARAMETER HIDES
# --------------------------------------------------------------------------
def human_reconciliation():
    print("=" * 78)
    print("5. WHY THE HUMAN NUMBERS ARE LOWER THAN THE MODEL PREDICTS")
    print("=" * 78)
    dose_mg_m2 = 2.33                       # MEASURED chung2017 MTD
    dose_mg_kg = dose_mg_m2 / 37.0          # ASSUMED: human km factor 37
    endothall_equiv = dose_mg_kg * MW_ENDOTHALL / MW_LB100
    print(f"  LB-100 {dose_mg_m2} mg/m2 = {dose_mg_kg:.4f} mg/kg = "
          f"{endothall_equiv:.4f} mg/kg as endothall equivalents, if fully converted")
    cl_rat = 0.693 * 0.23 / 5.5 * 1000      # mL/h/kg
    cl_human = cl_rat * (70 / 0.25) ** -0.25
    print(f"  ASSUMED human CL by allometry from the mouse-scale estimate: "
          f"{cl_human:.2f} mL/h/kg")
    c_pred = endothall_equiv * 1e6 / 24 / cl_human    # ng/mL if infused evenly
    print(f"  Predicted average endothall if fully converted and evenly spread: "
          f"{c_pred:.0f} ng/mL = {ng_per_mL_to_nM(c_pred):.0f} nM")
    print(f"  MEASURED peaks (chung2017 Table 3): 11.5, 14.8, 34.3 ng/mL = "
          f"{ng_per_mL_to_nM(11.5):.0f}, {ng_per_mL_to_nM(14.8):.0f}, "
          f"{ng_per_mL_to_nM(34.3):.0f} nM")
    print(f"  Discrepancy: about {c_pred/34.3:.0f}-fold to {c_pred/11.5:.0f}-fold high.\n")
    print("  THE DISCREPANCY IS THE MISSING PARAMETER. It is absorbed by some product")
    print("  of (a) the fraction of LB-100 that ever becomes endothall in vivo and")
    print("  (b) endothall's true clearance. feng2023 shows circulating endothall")
    print("  about tenfold below circulating LB-100 on a molar basis, which points at")
    print("  (a) - but a peak ratio is not a conversion fraction. NOBODY HAS EVER")
    print("  DOSED ENDOTHALL AS ENDOTHALL AND MEASURED ITS PK IN ANY SPECIES, so the")
    print("  two are confounded in every dataset that exists.\n")


# --------------------------------------------------------------------------
# 6. WHAT THE EX VIVO EXPERIMENT ACTUALLY EXPOSED THE TISSUE TO
# --------------------------------------------------------------------------
def ex_vivo_conversion():
    print("=" * 78)
    print("6. BACK-CALCULATING THE EX VIVO DOSE-RESPONSE IN ENDOTHALL TERMS")
    print("=" * 78)
    print("  MEASURED (rollema2025): LB-100 hydrolysis t1/2 = 4.9 h at pH 7.4, 37 C")
    print("  MEASURED (shuhaibar2021): 2-hour preincubation, then FGF, then imaging.")
    print("    1 uM LB-100 -> NO effect;  5 uM -> effect;  10 uM -> effect")
    print("    6-day femur culture at 10 uM -> 1.30-fold elongation\n")
    t12 = 4.9
    for hours, label in ((2.0, "2 h preincubation (Fig 1F)"),
                         (24.0, "24 h"), (144.0, "6 d culture (Fig 3C)")):
        frac = 1 - 0.5 ** (hours / t12)
        print(f"    {label:<28} fraction hydrolysed {frac*100:6.2f}%")
        for load in (1, 5, 10):
            print(f"        {load:2d} uM LB-100 -> up to {load*frac:6.3f} uM endothall"
                  f" ({nM_to_ng_per_mL(load*frac*1000):8.1f} ng/mL)")
    print()
    print("  READ-OFF, AND IT IS THE SHARPEST THING IN THIS FILE: at 2 hours, 1 uM")
    print("  LB-100 has generated about 0.25 uM = 250 nM endothall - already ~2.6x")
    print("  the isolated-PP2A IC50 of 95 nM - AND IT DID NOTHING to the FGF block.")
    print("  5 uM generates about 1.25 uM and worked. So the concentration the INTACT")
    print("  TISSUE needs is somewhere between 0.25 and 1.25 uM, i.e. 3 to 13-fold")
    print("  above the isolated-enzyme IC50. Penetration, the wrong-phosphatase")
    print("  possibility, and Donnan exclusion are all candidates for that shortfall,")
    print("  and this atlas cannot yet separate them.")
    print("  CAVEAT: assumes no endothall in the stock and none lost; rollema2025 says")
    print("  a room-temperature DMSO stock already carries ~0.2% endothall.\n")


# --------------------------------------------------------------------------
# 7. PUMP FEASIBILITY
# --------------------------------------------------------------------------
def pump_feasibility():
    print("=" * 78)
    print("7. CAN A MINIPUMP ACTUALLY DELIVER IT TO A GROWING MOUSE")
    print("=" * 78)
    print("  MEASURED (martiniova2011): Alzet 1002 delivers 0.25 uL/h from a 100 uL")
    print("  reservoir for 14 days, implanted intraperitoneally, and 0.03 mg/day of")
    print("  LB-100 in that pump was tolerated in an adult mouse.")
    print("  ASSUMED, TO BE VERIFIED FROM THE MANUFACTURER: model 2004 = 0.25 uL/h for")
    print("  28 days, model 2006 = 0.15 uL/h for 42 days, both 200 uL.\n")
    print("  THE DESIGN PROBLEM NOBODY CAN AVOID: a pump delivers a FIXED mass per")
    print("  hour while the animal roughly triples in mass over the dosing window, so")
    print("  the mg/kg/day dose FALLS as the mouse grows.\n")
    # ASSUMED body weights, C57BL/6J, to be replaced with a sourced growth curve
    weights = {21: 8.5, 28: 12.5, 35: 17.0, 42: 20.0, 49: 22.0, 56: 24.0}
    print("    ASSUMED body weight (g) and the resulting dose from a pump set to")
    print("    deliver 1.0 mg/kg/day at implantation on PND21:\n")
    target = 1.0
    fixed_ug_per_day = target * weights[21] / 1000 * 1000   # ug/day
    print(f"    fixed output {fixed_ug_per_day:.1f} ug/day")
    for pnd, w in sorted(weights.items()):
        print(f"      PND{pnd:>2}  weight {w:5.1f} g   ->  {fixed_ug_per_day/w:5.2f} mg/kg/day")
    print()
    for rate_uL_h, model in ((0.25, "1002 / 2004"), (0.15, "2006")):
        vol_per_day = rate_uL_h * 24
        conc = fixed_ug_per_day / vol_per_day        # ug/uL = mg/mL
        print(f"    model {model}: {vol_per_day:.1f} uL/day -> reservoir must be "
              f"{conc:.2f} mg/mL")
    print()
    print("  Both are low concentrations for a compound formulated as a water-soluble")
    print("  salt, so solubility is unlikely to bind - BUT the endothall solubility")
    print("  and the stability of endothall in a 37 C pump for 28-42 days are both")
    print("  UNMEASURED and are on the get-list.\n")



# --------------------------------------------------------------------------
# 8. THE FIGURE 1F CONCENTRATION-RESPONSE, FITTED  (round 136)
#    Bar heights read off the supplied panel by eye - APPROXIMATE.
# --------------------------------------------------------------------------
def fig1f_fit():
    print("=" * 78)
    print("8. shuhaibar2021 FIGURE 1F, RE-EXPRESSED IN ENDOTHALL AND FITTED")
    print("=" * 78)
    ctrl, fgf, canth = 0.86, 0.38, 0.76
    resp = {1: 0.35, 5: 0.84, 10: 1.19}
    t12, hours = 4.9, 2.0
    frac = 1 - 0.5 ** (hours / t12)
    print(f"  APPROXIMATE bar heights read off the panel: control {ctrl}, FGF {fgf},")
    print(f"  FGF+1/5/10 uM LB-100 = {resp[1]}/{resp[5]}/{resp[10]}, FGF+10 uM cantharidin {canth}")
    print(f"  Fraction of LB-100 hydrolysed in the 2 h preincubation: {frac:.3f}\n")
    pts = []
    for lb in sorted(resp):
        endo = lb * frac
        rescue = (resp[lb] - fgf) / (ctrl - fgf)
        pts.append((endo, rescue))
        print(f"    {lb:>2} uM LB-100 -> {endo:.3f} uM endothall, fractional rescue {rescue:+.3f}")
    (c1, e1), (c2, e2) = pts[1], pts[2]
    lg = lambda e: math.log(min(max(e, 1e-3), 0.999) / (1 - min(max(e, 1e-3), 0.999)))
    h = (lg(e2) - lg(e1)) / (math.log(c2) - math.log(c1))
    ec50 = c1 / math.exp(lg(e1) / h)
    print(f"\n  HILL FIT from the two active points: EC50 = {ec50:.2f} uM endothall, slope = {h:.1f}")
    pred = 1 / (1 + (ec50 / pts[0][0]) ** h)
    print(f"  Predicted rescue at the INACTIVE point ({pts[0][0]:.2f} uM): {pred:.3f}"
          f"  (observed {pts[0][1]:+.3f}) - the fit reproduces the third point it was not fitted to.")
    print(f"  10 uM cantharidin gives {(canth - fgf) / (ctrl - fgf):+.2f} rescue;"
          f" 10 uM LB-100 OVERSHOOTS control by {100*(resp[10]-ctrl)/ctrl:+.0f}%,")
    print("  which is the tonic-restraint result showing up again.\n")
    print("  THE TARGET CONCENTRATION FOR THE EXPERIMENT IS THEREFORE ABOUT 0.7 uM")
    print("  ENDOTHALL SUSTAINED, and 1.5-2 uM for a near-maximal effect. The slope of")
    print("  about 5 means the useful dose range is NARROW - a threefold miss on either")
    print("  side gives almost nothing or no more than everything.\n")


# --------------------------------------------------------------------------
# 9. THE WINDOW, WITH BOTH SIDES NOW MEASURED  (round 136)
# --------------------------------------------------------------------------
def window():
    print("=" * 78)
    print("9. REQUIRED EXPOSURE AGAINST TOLERATED EXPOSURE - THEY OVERLAP")
    print("=" * 78)
    print("  MEASURED (sera_endothall_2009, from EPA MRID 42169502): endothall plasma")
    print("  half-life after IV in male rat is 1.8 h at 0.9 mg/kg and 13.9 h at 4.5 mg/kg")
    print("  - SATURABLE elimination, a 7.7-fold half-life change for a 5-fold dose.\n")
    print("    infusion rate needed, mg/kg/day, using the two measured half-lives:")
    for dose, t12h in ((0.9, 1.8), (4.5, 13.9)):
        for vd in (0.20, 0.26):
            cl = 0.693 * vd / t12h * 1000
            row = f"      t1/2 {t12h:4.1f} h, Vd {vd:.2f}: "
            for tgt in (0.7, 2.0):
                row += f" {tgt} uM -> {tgt*MW_ENDOTHALL/1000*cl*24/1000:6.3f}   "
            print(row)
    print("\n    TOLERATED, all MEASURED:")
    print("      2-year rat oral NOAEL 8 mg/kg/day; oral absorption 1.2-7 per cent")
    print("      -> ABSORBED systemic NOAEL 0.10 to 0.56 mg/kg/day")
    print("      2-year rat oral LOAEL 16 -> absorbed 0.19 to 1.12 mg/kg/day")
    print("      mouse IP LD50 14 mg/kg single dose; 1.5 mg/kg/day LB-100 continuous")
    print("      for 14 days tolerated in adult mice")
    print("\n  READ-OFF: holding 0.7 uM needs 0.03 to 0.31 mg/kg/day and the absorbed")
    print("  chronic no-effect band is 0.10 to 0.56. THEY OVERLAP. This is the first")
    print("  time in this thread that a required exposure and a tolerable one have.")
    print("  Holding 2 uM needs 0.09 to 0.89 and sits at or above the band.\n")
    print("  AND THE PRODRUG IS THE WRONG MOLECULE ON POTENCY OF HARM:")
    lb_umol = 1000 * 3.0 / MW_LB100
    en_umol = 1000 * 14 / MW_ENDOTHALL
    print(f"    LB-100 3 mg/kg IP, lethal to ALL juvenile mice = {lb_umol:.1f} umol/kg")
    print(f"    endothall IP LD50 in mice = {en_umol:.1f} umol/kg")
    print(f"    -> LB-100 is {en_umol/lb_umol:.1f}-fold more lethal PER MOLE than the species")
    print("       it is supposed to be delivering, so its toxicity is largely its own.\n")




# --------------------------------------------------------------------------
# 10. ROUND 137 - THE HALF-LIVES ARE ORAL, SO CLEARANCE IS ONLY BOUNDED
# --------------------------------------------------------------------------
def bounded_window():
    print("=" * 78)
    print("10. THE CORRECTED WINDOW - AN UPPER BOUND ON HALF-LIFE, NOT A VALUE")
    print("=" * 78)
    print("  CORR-133. The EPA toxicology chapter (epa_endothall_tox_chapter_2004),")
    print("  which is the PRIMARY review of MRID 42169502, says the 1.8 / 2.5 / 13.9 hour")
    print("  blood half-lives are from ORAL dosing. Only ONE intravenous dose was given,")
    print("  0.9 mg/kg, and the only IV result reported is 69 per cent urinary excretion.")
    print("  A secondary source called them intravenous; they are not.\n")
    print("  CONSEQUENCE: with 5-7 per cent oral absorption the oral curve is probably")
    print("  ABSORPTION-limited, so 1.8 h is an UPPER BOUND on the true elimination")
    print("  half-life at low dose - which makes clearance a LOWER bound and the required")
    print("  infusion rate a LOWER bound too. The dose-dependence (1.8 -> 13.9 h) is then")
    print("  most simply prolonged absorption, NOT saturable elimination.\n")
    for vd in (0.20, 0.26):
        cl = 0.693 * vd / 1.8 * 1000
        row = f"    Vd {vd:.2f} L/kg, t1/2 <= 1.8 h -> CL >= {cl:5.1f} mL/h/kg:"
        for tgt in (0.7, 2.0):
            row += f"   {tgt} uM needs >= {tgt*MW_ENDOTHALL/1000*cl*24/1000:5.3f} mg/kg/day"
        print(row)
    print()
    print("    Against the MEASURED oral absorption of 5-7 per cent:")
    for f in (0.05, 0.07):
        print(f"      absorption {100*f:.0f}%: 2-year rat NOAEL 8 mg/kg/d -> absorbed "
              f"{8*f:.2f}; LOAEL 16 -> {16*f:.2f} mg/kg/day")
    print()
    print("  READ-OFF, AND IT IS TIGHTER THAN ROUND 136 RATHER THAN LOOSER:")
    print("    0.7 uM (the fitted EC50)  needs 0.24-0.31 mg/kg/day")
    print("    chronic absorbed NO-EFFECT dose is 0.40-0.56 mg/kg/day")
    print("    -> a margin of about 1.3 to 2.3-fold. Thin, but the right side of one.")
    print("    2 uM (near-maximal)        needs 0.69-0.89 mg/kg/day")
    print("    chronic absorbed LOAEL is  0.80-1.12 mg/kg/day")
    print("    -> no margin at all. The near-maximal effect is not reachable safely.\n")


# --------------------------------------------------------------------------
# 11. THE PUMP DOES NOT FIT THE ANIMAL  (round 137)
# --------------------------------------------------------------------------
def pump_mass():
    print("=" * 78)
    print("11. THE PUMP MASS CONSTRAINT - RESOLVED, AND IT BITES")
    print("=" * 78)
    print("  MEASURED (alzet_pump_specs): models 2004 and 2006 are both 200-series,")
    print("  3.0 x 0.7 cm, COMPLETE PUMP WEIGHT 1.1 g, 200 uL reservoir. Filled with a")
    print("  dilute aqueous solution the manufacturer equates 200 uL to about 200 mg, so")
    print("  a filled pump is about 1.3 g.\n")
    for w, label in ((8.5, "PND21 weanling"), (12.5, "PND28"), (17.0, "PND35"), (25.0, "adult")):
        print(f"    {label:<16} {w:5.1f} g -> filled 2004/2006 is "
              f"{100*1.3/w:5.1f}% of body weight"
              f"{'   FAILS the 10% convention' if 1.3/w > 0.10 else '   passes'}")
    print()
    print(f"  The 10 per cent limit is met at {1.3/0.10:.0f} g, which is about PND28-30.")
    print("  SO THE 28- AND 42-DAY PUMPS CANNOT BE IMPLANTED AT WEANING. Three options:")
    print("    (a) start at PND28 with a model 2004 and accept losing the first week;")
    print("    (b) serial 100-series pumps from PND21 - martiniova2011 used a model 1002")
    print("        in mice - which needs one extra surgery but covers the whole window;")
    print("    (c) abandon pumps. Drinking water is out: oral absorption is 5-7 per cent")
    print("        and the oral route carries the gastric lesion that sets the ceiling.")
    print("  OPTION (b) IS THE DESIGN. The 100-series filled mass is still unmeasured")
    print("  here and is the one remaining logistical number.\n")




# --------------------------------------------------------------------------
# 12. ROUND 138 - Vd AND CLEARANCE DERIVED FROM PRIMARY DATA, AND A MARGIN
#     THAT DOES NOT DEPEND ON THE ABSORBED FRACTION
# --------------------------------------------------------------------------
SOO_1H = {  # cpm per 100 mg DRY tissue at 1 h, Soo 1967 Table III-2 via the
            # 1992 EPA Drinking Water Criteria Document
    "Liver": 242, "Kidney": 1070, "Heart": 135, "Lung": 210, "Spleen": 71,
    "Brain": 43, "Blood": 309, "Muscle": 50, "Fat": 0,
}
SOO_SA = 407.0          # cpm per microgram endothall
SOO_DOSE = 5.0          # mg/kg oral


def soo_distribution():
    print("=" * 78)
    print("12. WHERE ENDOTHALL ACTUALLY GOES  (Soo 1967 Table III-2, 1 hour)")
    print("=" * 78)
    b = SOO_1H["Blood"]
    for k, v in SOO_1H.items():
        print(f"    {k:<8} {v:>6} cpm/100 mg dry   tissue:blood {v/b:5.2f}")
    print()
    print("  ONLY THE KIDNEY EXCEEDS BLOOD, at 3.5-fold - the active organic-anion")
    print("  secretion SERA predicted. Everything else is at or below blood, BRAIN at")
    print("  0.14, MUSCLE at 0.16 and FAT at zero. This is a compound that stays in")
    print("  plasma and interstitium and does not enter cells or lipid.")
    print("  THE MUSCLE NUMBER IS THE BEST PROXY THE ATLAS WILL EVER GET FOR CARTILAGE:")
    print("  a high-water, uncharged, moderately perfused tissue sees about a sixth of")
    print("  the blood concentration. Cartilage, avascular and anionic, should see less.\n")


def soo_pk():
    print("=" * 78)
    print("13. VOLUME OF DISTRIBUTION AND CLEARANCE, DERIVED TWO WAYS")
    print("=" * 78)
    ug_per_100mg_dry = SOO_1H["Blood"] / SOO_SA
    print(f"  Blood at 1 h: {SOO_1H['Blood']} cpm/100 mg dry = "
          f"{ug_per_100mg_dry:.3f} ug endothall per 100 mg dry blood")
    concs = []
    for dryfrac in (0.18, 0.20, 0.22):
        mL = 100 / dryfrac / 1000 / 1.06
        c = ug_per_100mg_dry / mL
        concs.append(c)
        print(f"    dry fraction {dryfrac:.2f} -> {c:.2f} ug/mL = {c/MW_ENDOTHALL*1000:.1f} uM")
    print("\n  (A) FROM CONCENTRATION AND ABSORBED DOSE:  Vd = absorbed / C(1 h)")
    for F in (0.07, 0.10):
        lo, hi = SOO_DOSE * F / max(concs), SOO_DOSE * F / min(concs)
        print(f"      F = {F:.2f}: Vd = {lo:.2f} to {hi:.2f} L/kg")
    print("      -> EXTRACELLULAR-FLUID-LIKE, which is what a dianion should be, and")
    print("         it confirms the 0.20-0.26 L/kg the earlier rounds ASSUMED.\n")
    pts = [(1, 309), (2, 96), (4, 92), (6, 56), (8, 39)]
    auc = sum((c0 + c1) / 2 * (t1 - t0) for (t0, c0), (t1, c1) in zip(pts, pts[1:]))
    auc += 309  # crude 0-1 h
    print(f"  (B) FROM AREA UNDER THE BLOOD CURVE: AUC(0-8 h) about {auc:.0f} cpm.h/100 mg dry")
    print("      CL = F x Dose / AUC")
    for F in (0.07, 0.10):
        for total in (900, 1400):
            mL = 100 / 0.20 / 1000 / 1.06
            auc_mgh_L = total / SOO_SA / mL
            cl = SOO_DOSE * F / auc_mgh_L * 1000
            print(f"      F = {F:.2f}, AUC {total}: CL = {cl:.0f} mL/h/kg")
    print("      -> CL about 50 to 110 mL/h/kg, consistent with (A) and with the")
    print("         upper-bound estimate from the 1.8 h half-life.\n")
    print("  REQUIRED INFUSION RATE, mg/kg/day:")
    for cl in (60, 100, 130):
        row = f"      CL {cl:>4} mL/h/kg:"
        for tgt in (0.7, 1.0, 2.0):
            row += f"   {tgt} uM -> {tgt*MW_ENDOTHALL/1000*cl*24/1000:5.3f}"
        print(row)
    print()
    print("  AND THE MARGIN IS INDEPENDENT OF THE ABSORBED FRACTION. Both sides carry")
    print("  F: the tolerated absorbed dose is F x 8 mg/kg/day, and the required rate is")
    print("  C_target x F x Dose / AUC. F cancels exactly, leaving")
    print("      margin = NOAEL_oral x AUC / (C_target x Dose_PK x 24)")
    for total in (900, 1400):
        mL = 100 / 0.20 / 1000 / 1.06
        auc_mgh_L = total / SOO_SA / mL
        for tgt, lbl in ((0.7, "EC50 0.7 uM"), (2.0, "near-max 2 uM")):
            c = tgt * MW_ENDOTHALL / 1000
            m = 8.0 * auc_mgh_L / (c * SOO_DOSE * 24)
            print(f"      AUC {total}, {lbl}: margin = {m:.1f}x")
    print()
    print("  READ-OFF: about 2.4 to 3.7-fold margin at the fitted EC50, and under 1.3")
    print("  at a near-maximal concentration. THE HALF-MAXIMAL TARGET IS REACHABLE")
    print("  BELOW THE CHRONIC NO-EFFECT DOSE; THE MAXIMAL ONE IS NOT.\n")


# --------------------------------------------------------------------------
# 14. THE PUMP PROBLEM IS SOLVED  (round 138)
# --------------------------------------------------------------------------
def pump_solved():
    print("=" * 78)
    print("14. ONE PUMP COVERS THE WHOLE WINDOW")
    print("=" * 78)
    print("  MEASURED (alzet_pump_specs, 100-series): models 1003D, 1007D, 1002, 1004")
    print("  and 1006 are all 1.5 x 0.6 cm, COMPLETE PUMP WEIGHT 0.4 g, 100 uL reservoir.")
    print("  Filled with a dilute aqueous solution that is about 0.5 g.\n")
    for w, label in ((8.5, "PND21 weanling"), (12.5, "PND28"), (24.0, "PND56")):
        print(f"    {label:<16} {w:5.1f} g -> 100-series filled is {100*0.5/w:4.1f}% of "
              f"body weight   {'passes' if 0.5/w <= 0.10 else 'FAILS'}"
              f"   |  200-series {100*1.3/w:5.1f}%   "
              f"{'passes' if 1.3/w <= 0.10 else 'FAILS'}")
    print()
    print("  MODEL 1006 IS THE ANSWER: 0.08 uL/hour for 6 WEEKS from a 100 uL reservoir")
    print("  at 0.4 g. Implanted at weaning it covers PND21 to PND63 in ONE surgery at")
    print("  6 per cent of body weight.")
    for rate_uL_h, model, days in ((0.08, "1006", 42), (0.11, "1004", 28)):
        vol = rate_uL_h * 24
        for target in (0.2, 0.3, 0.4):
            ug_day = target * 8.5 / 1000 * 1000
            print(f"    model {model}: {vol:.2f} uL/day; to start at {target} mg/kg/day in an "
                  f"8.5 g mouse needs {ug_day/vol:5.2f} mg/mL")
        break
    print("  Against a water solubility of 100 g/L that is four orders of magnitude of")
    print("  headroom. THE FIXED OUTPUT STILL MEANS THE DOSE FALLS AS THE MOUSE GROWS -")
    print("  2.8-fold from PND21 to PND56 - which front-loads exposure into the fastest-")
    print("  growing window and is arguably the right shape anyway.\n")



def main():
    power_table()
    velocity_vs_final()
    donnan_table()
    infusion_table()
    human_reconciliation()
    ex_vivo_conversion()
    pump_feasibility()
    fig1f_fit()
    window()
    bounded_window()
    pump_mass()
    soo_distribution()
    soo_pk()
    pump_solved()
    print("=" * 78)
    print("END. Every ASSUMED value above is an item on the get-list in")
    print("nodes/L12_pharmacology_as_mechanistic_probe/"
          "the_experiment_specified_and_what_is_missing.yaml")
    print("=" * 78)


if __name__ == "__main__":
    main()
