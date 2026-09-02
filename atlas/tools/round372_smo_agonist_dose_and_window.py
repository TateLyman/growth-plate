#!/usr/bin/env python3
"""
ROUND 372. DOES A DOSABLE SMO AGONIST EXIST, AND WHAT IS THE DOSE.

R371 removed chemistry as the discriminator between SMO agonists: at 400-560 Da the growth
plate partition curve is already near unity (farnum2006: 332 Da ~100% of vascular
concentration), so cartilage transport does not choose between them. What is left is
(a) the SMO-over-GR window for the four APPROVED agonists, and (b) the dose.

THIS SCRIPT COMPUTES THREE THINGS.

1. THE THERAPEUTIC WINDOW: Gli-luciferase EC50 (wang2010smo, full text) against
   glucocorticoid-receptor potency (ChEMBL, human GR CHEMBL2034). A ratio above 1 means SMO is
   engaged at a LOWER concentration than GR, i.e. there is a window in which the hedgehog arm
   runs and the growth-suppressing arm does not.
   ⚠ THIS COMPARES A FUNCTIONAL REPORTER EC50 WITH A BINDING Ki/IC50 AND THAT IS NOT
   APPLES-TO-APPLES. Reporter amplification flatters functional potency. Treat the ratio as a
   RANKING, not as an occupancy calculation.

2. THE SYSTEMIC DOSE for SAG, by FDA body-surface-area allometry from the only in vivo
   growth-plate experiment that exists (trompet2024: 25 ug/g/day i.p., mouse, P31-P37).

3. THE LOCAL DEPOT, which is the route that produced the length gain. Two numbers matter and
   neither is potency:
     - the local CONCENTRATION the rat bead actually delivered, versus the EC50
     - the DIFFUSION LENGTH over the bead's measured 3-week lifetime, against the size of a
       human distal femoral epiphysis
   The second is the one that decides whether a point-source depot can cover a human plate.
"""
import math

# ---------------------------------------------------------------- 1. the window
# Gli-luciferase EC50, nM - wang2010smo full text (PMC2889058), one lab, one assay
GLI_EC50 = {
    "clobetasol propionate": 0.2,
    "fluticasone propionate": 0.3,
    "fluocinonide": 0.3,
    "halcinonide": 1.8,
}
# human glucocorticoid receptor potency, nM - ChEMBL CHEMBL2034, best and median of nM records
GR = {   # (best, median, n)
    "clobetasol propionate": (0.662, 1.456, 2),
    "fluticasone propionate": (0.040, 0.500, 7),
    "fluocinonide": (2.392, 5.263, 2),
    "halcinonide": (0.732, 1.611, 2),
}

print("=" * 78)
print("1. THE SMO-OVER-GR WINDOW FOR THE FOUR APPROVED AGONISTS")
print("=" * 78)
print(f"{'compound':26s} {'Gli EC50':>9s} {'GR best':>9s} {'GR med':>9s} {'ratio(med)':>11s} {'ratio(best)':>12s}")
rows = []
for c, gli in GLI_EC50.items():
    best, med, n = GR[c]
    rows.append((med / gli, c, gli, best, med, n))
    print(f"{c:26s} {gli:9.2f} {best:9.3f} {med:9.3f} {med/gli:11.1f}x {best/gli:12.2f}x")
rows.sort(reverse=True)
print(f"\nBEST WINDOW: {rows[0][1]} - SMO engaged {rows[0][0]:.0f}-fold below GR on median GR potency")
print("WORST: halcinonide and fluticasone - GR is engaged AT OR BELOW the SMO concentration,")
print("       so there is no concentration at which the hedgehog arm runs alone.")

# ---------------------------------------------------------------- 2. systemic SAG
print("\n" + "=" * 78)
print("2. SYSTEMIC SAG DOSE BY FDA BODY-SURFACE-AREA ALLOMETRY")
print("=" * 78)
MOUSE_DOSE = 25.0        # mg/kg/day, trompet2024, i.p., P31-P37
KM_MOUSE, KM_HUMAN = 3.0, 37.0
hed = MOUSE_DOSE * KM_MOUSE / KM_HUMAN
print(f"trompet2024 mouse dose      : {MOUSE_DOSE:.0f} mg/kg/day i.p. (25 ug/g), 7 consecutive days")
print(f"human equivalent dose (HED) : {hed:.2f} mg/kg/day  (mouse Km {KM_MOUSE} / human Km {KM_HUMAN})")
for bw in (50, 60, 70):
    print(f"   at {bw} kg -> {hed*bw:7.1f} mg/day   ({hed*bw*7:7.0f} mg per 7-day pulse)")
print("⚠ SAG IS A RESEARCH CHEMICAL. No GMP material, no human PK, no toxicology package,")
print("  and no Smoothened agonist has ever been administered to a human (0 registry trials).")

# ---------------------------------------------------------------- 3. local depot
print("\n" + "=" * 78)
print("3. THE LOCAL SOC DEPOT - CONCENTRATION AND DIFFUSION REACH")
print("=" * 78)
SAG_MW = 490.1
bead_ug = 7.0                      # trompet2024: 7 ug SAG in 1.5 uL DMSO, agarose bead
nmol = bead_ug * 1e-6 / SAG_MW * 1e9
rat_epiphysis_uL = 19.0            # ~4 x 3 x 3 mm spheroid, P30 rat distal femur (estimate)
conc_uM = nmol / rat_epiphysis_uL  # nmol/uL = uM
sag_ec50_nM = 3.0                  # canonical SAG Gli EC50, order of magnitude
print(f"bead payload                : {bead_ug:.0f} ug = {nmol:.1f} nmol SAG")
print(f"if distributed through a ~{rat_epiphysis_uL:.0f} uL rat epiphysis: {conc_uM:.0f} uM")
print(f"that is ~{conc_uM*1000/sag_ec50_nM:,.0f}x the SAG Gli EC50 (~{sag_ec50_nM:.0f} nM)")
print("→ THE DEPOT IS NOT POTENCY-LIMITED. It is a large reservoir maintaining a gradient,")
print("  so the human dose does NOT scale with potency - it scales with geometry.")

print("\nDIFFUSION REACH over the bead's MEASURED lifetime (Gli1-LacZ signal present at 1 week,")
print("GONE BY 3 WEEKS), for a ~500 Da solute in cartilage:")
t = 21 * 24 * 3600
for D in (1e-6, 2e-6, 3e-6):       # cm^2/s; water ~5e-6, cartilage reduces it 2-3x
    L = math.sqrt(2 * D * t)
    print(f"   D = {D:.0e} cm2/s  ->  sqrt(2Dt) = {L:5.2f} cm = {L*10:5.1f} mm")
print("\nSCALE TO BEAT: a human adolescent distal femoral epiphysis is roughly 70-80 mm wide,")
print("so the half-distance from a central placement is ~35-40 mm.")
print("→ A SINGLE CENTRAL DEPOT REACHES MOST OF IT AND 2-3 DEPOTS COVER IT. The rat plate is")
print("  ~4 mm across, so the geometry is FAVOURABLE at human scale rather than prohibitive -")
print("  diffusion length grows as sqrt(t) and the residence time is set by the depot, not the")
print("  animal.")
print("\n⚠ EVERY NUMBER IN SECTION 3 IS AN ORDER-OF-MAGNITUDE ESTIMATE. The rat epiphysis volume")
print("  is estimated, not measured; D for SAG in cartilage has never been measured; and a")
print("  sqrt(2Dt) length ignores binding, clearance by the epiphyseal vasculature and the fact")
print("  that the resting zone sits at a surface rather than filling the volume.")

# ---------------------------------------------------- 4. how much drug for a human depot
print("\n" + "=" * 78)
print("4. HOW MUCH DRUG A HUMAN EPIPHYSEAL DEPOT ACTUALLY NEEDS")
print("=" * 78)
print("The requirement is a CONCENTRATION over a VOLUME, so compute the mass needed to hold a")
print("human distal femoral epiphysis at the EC50 - this is the number that decides feasibility.")
for r_cm, label in ((1.75, "half-epiphysis, 35 mm diameter"), (3.5, "whole epiphysis, 70 mm diameter")):
    vol_L = (4.0 / 3.0) * math.pi * r_cm ** 3 / 1000.0
    for mult, mlabel in ((1, "1x EC50"), (10, "10x EC50"), (100, "100x EC50")):
        mass_ug = sag_ec50_nM * 1e-9 * mult * SAG_MW * vol_L * 1e6
        print(f"   {label:32s} {vol_L*1000:6.0f} mL  at {mlabel:9s} = {mass_ug:8.2f} ug SAG")
print(f"\nthe trompet2024 rat bead held {bead_ug:.0f} ug.")
print("→ A SINGLE RAT-SIZED PAYLOAD ALREADY EXCEEDS WHAT IS NEEDED TO FILL A WHOLE HUMAN")
print("  EPIPHYSIS AT EC50. The human depot is a MICROGRAM-to-LOW-MILLIGRAM problem, not a")
print("  gram problem, because the requirement scales with volume x nanomolar, not with body mass.")
print("\n⛔ THE HONEST CORRECTION TO THAT: a depot must BALANCE CLEARANCE, not fill a volume once.")
print("  Drug is continuously washed out by the epiphyseal vasculature, so the real requirement")
print("  is a RELEASE RATE sustained over weeks. The fill calculation sets a LOWER BOUND on the")
print("  payload and shows the scale is not prohibitive; it does not set the dose.")
print("  Clearance from the epiphysis has never been measured for any SMO agonist.")
