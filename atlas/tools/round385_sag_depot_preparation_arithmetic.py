#!/usr/bin/env python3
"""
ROUND 385. THE PREPARATION ARITHMETIC FOR A SAG-FIBRIN EPIPHYSEAL DEPOT.

Everything the protocol needs numerically: which salt, what mass, what stock, what volume,
and what the whole-pulse total is. R384 concluded the dose must be at the LOW end because
erdafitinib and vosoritide already raise chondrocyte Ihh through the MEK/ERK node
(zhou2015a), so the low column is the operative one.

⛔ ONE CORRECTION TO EVERY PRIOR ROUND'S ARITHMETIC IS BUILT IN HERE. R372, R373, R374 and
   R375 all used MW 490.1, which is the SAG FREE BASE (Tocris 4366). The formulation calls
   for the water-soluble DIHYDROCHLORIDE (Tocris 6390), MW 562.98, because the free base is
   cLogP 6.79. Mass doses must be scaled by 562.98/490.1 = 1.149x to deliver the same
   number of molecules. Every mass figure below is for the SALT.
"""
MW_FREEBASE = 490.1
MW_SALT     = 562.98
EC50_nM     = 3.0

print("=" * 78)
print("1. THE SALT CORRECTION")
print("=" * 78)
print(f"SAG free base (Tocris 4366)          MW {MW_FREEBASE}")
print(f"SAG dihydrochloride (Tocris 6390)    MW {MW_SALT}   <- the formulation form, water-soluble")
print(f"mass scaling factor                  {MW_SALT/MW_FREEBASE:.3f}x")
print("⛔ R372-R375 all computed masses on the FREE BASE. Multiply them by 1.149 for the salt.")

print("\n" + "=" * 78)
print("2. PER-DEPOT LOADING")
print("=" * 78)
print(f"{'gel conc':>10s} {'depot vol':>10s} {'SAG.2HCl per depot':>20s} {'x EC50 in gel':>14s}")
rows = []
for conc_uM in (30, 100, 300, 1000):
    for vol_mL in (1.0, 2.0):
        mass_ug = conc_uM * 1e-6 * (vol_mL / 1000.0) * MW_SALT * 1e6
        rows.append((conc_uM, vol_mL, mass_ug))
        print(f"{conc_uM:8d} uM {vol_mL:8.1f} mL {mass_ug:17.1f} ug {conc_uM*1000/EC50_nM:12,.0f}x")
print("\n  he2024sag dosed 30, 100 and 1000 uM gels IN VIVO, so all four rows are inside")
print("  the only published in vivo range for a SAG-fibrin gel.")

print("\n" + "=" * 78)
print("3. THE OPERATIVE LOW DOSE (R384) AND THE WHOLE-PULSE TOTAL")
print("=" * 78)
DEPOTS_PER_EPIPHYSIS, EPIPHYSES = 2, 4     # distal femur + proximal tibia, bilaterally
for label, conc_uM, vol_mL in (("LOW  (operative, R384)", 100, 2.0),
                               ("MID", 300, 2.0),
                               ("HIGH (R374 original)", 1000, 2.0)):
    per_depot = conc_uM * 1e-6 * (vol_mL / 1000.0) * MW_SALT * 1e6
    per_pulse = per_depot * DEPOTS_PER_EPIPHYSIS * EPIPHYSES
    print(f"{label:24s} {per_depot:7.1f} ug/depot  x {DEPOTS_PER_EPIPHYSIS} depots x {EPIPHYSES} epiphyses "
          f"= {per_pulse/1000:5.2f} mg per pulse")
print("\n  → THE ENTIRE PULSE IS UNDER ONE MILLIGRAM OF DRUG AT THE OPERATIVE DOSE.")
print("    For scale, trompet2024's single rat bead held 7 ug and produced the length gain.")

print("\n" + "=" * 78)
print("4. STOCK AND SPIKING")
print("=" * 78)
STOCK_mM = 10.0
stock_mg_per_mL = STOCK_mM * 1e-3 * MW_SALT
print(f"stock: {STOCK_mM:.0f} mM SAG.2HCl in sterile water = {stock_mg_per_mL:.2f} mg/mL")
print(f"       a 1 mg vial (the standard Tocris pack) makes {1.0/stock_mg_per_mL*1000:.0f} uL of {STOCK_mM:.0f} mM stock")
for conc_uM in (100, 300, 1000):
    for vol_mL in (2.0,):
        spike_uL = conc_uM / (STOCK_mM * 1000.0) * vol_mL * 1000.0
        print(f"  to make {vol_mL:.0f} mL of gel at {conc_uM:4d} uM: spike {spike_uL:6.1f} uL of stock "
              f"({spike_uL/(vol_mL*1000)*100:.1f}% v/v)")
print("\n  spike into the SEALER PROTEIN (fibrinogen) component, NOT the thrombin component -")
print("  thrombin is the trigger, and the drug should be distributed through the clot.")
print(f"\n  ONE 1 mg VIAL COVERS {1000.0/ (100*1e-6*(2.0/1000)*MW_SALT*1e6) :.1f} DEPOTS AT THE LOW DOSE,")
print("  i.e. a single catalogue vial is more than one whole bilateral pulse.")

print("\n" + "=" * 78)
print("5. WHAT THE ARITHMETIC DOES NOT SETTLE")
print("=" * 78)
print("""  · EPIPHYSEAL CLEARANCE HAS NEVER BEEN MEASURED for any SMO agonist, so the depot is
    sized as a reservoir against an unknown washout rate, not against a measured one.
  · The fill calculation (26 ug free base holds a whole human epiphysis at 100x EC50,
    R372) is a LOWER BOUND on payload, not a dose.
  · Whether a setting fibrin gel distributes through epiphyseal cancellous bone at all,
    rather than forming a single plug at the cannula tip, is unknown in any species.
  · And SAG dihydrochloride at catalogue grade is >=98% HPLC with no endotoxin spec, no
    sterility assurance and no impurity qualification. Sterile filtration through 0.22 um
    removes bioburden; it does NOT make the material qualified for implantation.""")
