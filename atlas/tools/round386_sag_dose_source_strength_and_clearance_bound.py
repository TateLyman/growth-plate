#!/usr/bin/env python3
"""
ROUND 386. THE TWO UNSETTLED ISSUES, AND THE DOSE RECOMPUTED AFTER VOSORITIDE WAS DROPPED.

R385 left three things open: epiphyseal clearance, whether a setting fibrin gel distributes
or plugs, and GMP. This script settles the dose question on a physically correct scaling,
audits a units bug in R372 that understated the reference exposure 1000-fold, and bounds
the clearance problem from both sides so the size of the remaining uncertainty is explicit.

⛔ THE BUG: R372 computed nmol/uL and printed the result labelled 'uM'. nmol/uL is mM.
   The rat epiphyseal concentration was reported as ~251x EC50; it is ~250,000x.
"""
import math
MW_FREEBASE, MW_SALT = 490.1, 562.98
EC50 = 3e-9

def radius_mm(vol_mm3): return (3.0 * vol_mm3 / (4.0 * math.pi)) ** (1.0/3.0)

print("=" * 78); print("1. THE R372 UNITS AUDIT"); print("=" * 78)
mol = 7.0e-6 / MW_FREEBASE
C_bead_mM = mol / (1.5e-6) * 1e3
C_ratepi = mol / (19.0e-6)
print(f"trompet2024 bead: 7 ug = {mol*1e9:.2f} nmol in 1.5 uL")
print(f"  concentration IN THE BEAD          {C_bead_mM:.2f} mM")
print(f"  averaged over a 19 uL rat epiphysis {C_ratepi*1e6:.0f} uM = {C_ratepi/EC50:,.0f}x EC50")
print("  ⛔ R372 said ~251x. Correct value is ~250,000x. Every 'x EC50' in R372 section 3 is 1000x low.")

print("\n" + "=" * 78); print("2. THE RIGHT SCALING IS SOURCE STRENGTH, NOT FILL VOLUME"); print("=" * 78)
print("""For a depot acting as a constant-concentration sphere of radius a, the steady-state
concentration at distance r is C(r) = C_source * a / r. What must be matched between
species is therefore the SOURCE STRENGTH C*a, not the total payload and not the average
tissue concentration. This supersedes R372's fill calculation, which was only ever a
lower bound.""")
a_rat = radius_mm(1.5); Sr = C_bead_mM * a_rat
a_hum = radius_mm(2000.0)
print(f"\nrat bead   : C {C_bead_mM:.2f} mM, a {a_rat:.2f} mm -> C*a = {Sr:.2f} mM.mm")
print(f"human depot: 2 mL -> a {a_hum:.2f} mm")
print(f"\n{'gel':>8s} {'C*a':>9s} {'vs rat':>9s}   concentration at the plate, 10-20 mm from depot centre")
for cuM in (100, 300, 1000):
    S = (cuM/1000.0) * a_hum
    c10 = (cuM/1000.0)*a_hum/10.0; c20 = (cuM/1000.0)*a_hum/20.0
    print(f"{cuM:6d} uM {S:7.2f}   {Sr/S:6.2f}x low   {c10*1e3:7.0f} uM ({c10*1e-3/EC50:,.0f}x EC50)"
          f" ... {c20*1e3:6.0f} uM ({c20*1e-3/EC50:,.0f}x EC50)")
print("""
→ 1000 uM IN 2 mL MATCHES THE RAT BEAD'S SOURCE STRENGTH ALMOST EXACTLY (0.87x).
→ AND THE DEPOT IS NOT POTENCY-LIMITED AT ANY OF THESE DOSES: even the lowest delivers
  >13,000x EC50 out to 20 mm. THE DOSE CHOICE IS ABOUT DURATION AND ABOUT SAFETY MARGIN
  ON THE Ihh BAND, NOT ABOUT REACHING THRESHOLD.""")

print("\n" + "=" * 78); print("3. BOUNDING THE CLEARANCE PROBLEM FROM BOTH SIDES"); print("=" * 78)
fill_ug = EC50*100 * 0.1 * MW_FREEBASE * 1e6      # 100x EC50 across 100 mL, free base
print(f"LOWER BOUND - fill a ~100 mL epiphysis once at 100x EC50: {fill_ug:.1f} ug free base")
vol_scaled = C_ratepi * 0.1 * MW_FREEBASE * 1e3   # match rat AVERAGE tissue conc in 100 mL, mg
print(f"UPPER BOUND - match the rat's AVERAGE tissue concentration in 100 mL: {vol_scaled:.0f} mg per epiphysis")
print(f"\n→ THE TWO BOUNDS SPAN {vol_scaled*1000/fill_ug:,.0f}-FOLD, AND THE ENTIRE GAP IS THE UNMEASURED")
print("  CLEARANCE RATE. NO AMOUNT OF REASONING CLOSES IT.")
print("""
⭐ BUT IT DOES NOT HAVE TO BE CLOSED, BECAUSE THE EFFECT IS MEASURABLE WHEN THE PARAMETER
  IS NOT. haraguchi2025's Hhip cKO growth plate is 41-52% LARGER IN AREA, and physeal
  thickness is directly readable on MRI. → DOSE-ESCALATE AGAINST AN IMAGING PD READOUT:
  place the first pulse, measure physeal thickness at 6 weeks, escalate at the next pulse
  if it has not moved. That converts an unmeasurable pharmacokinetic parameter into a
  measured pharmacodynamic one.
⚠ AND THE CONTROL THAT MUST RIDE WITH IT: R365 and failure mode #1 - a widened plate with
  NO height gain is charge-without-discharge. Physeal width is TARGET ENGAGEMENT, not
  efficacy. Both must move.""")

print("\n" + "=" * 78); print("4. THE DOSE AFTER VOSORITIDE WAS DROPPED"); print("=" * 78)
print("""WHAT CHANGED. R384 set the LOW column because TWO arms lowered ERK and therefore raised
chondrocyte Ihh (zhou2015a): erdafitinib at the receptor and vosoritide at RAF-1 inside the
ERK arm. With vosoritide gone only erdafitinib remains on that node - but erdafitinib is the
DOMINANT contributor, sitting upstream of ERK AND CREB (R263/R265), while vosoritide acted
only inside the ERK arm. SO THE BASELINE Ihh ELEVATION FALLS, BUT BY LESS THAN HALF.

ALSO CHANGED:
  · SCFE risk drops from quadruple- to triple-stacked - vosoritide contributed 3 of the
    cases in dauber2026.
  · ⛔ THE h_term MULTIPLIER IS GONE. SAG x vosoritide was the clean multiplicative pair in
    H = N x A x h_term. Without it a bigger pool has a smaller per-cell output to multiply.
  · ⭐ AND SAG BECOMES MORE IMPORTANT, NOT LESS: the remaining stack is GH (throughput,
    priced at ~0 attained height), erdafitinib (lambda and h_term via CREB) and anastrozole
    (the period). NOTHING TOUCHES N. SAG is now the only pool arm in the entire stack.""")
for label, cuM in (("R384 low (two ERK arms)", 100), ("R386 OPERATIVE (one ERK arm)", 300), ("rat-matched ceiling", 1000)):
    per = cuM*1e-6*(2.0/1000.0)*MW_SALT*1e6
    print(f"  {label:30s} {cuM:5d} uM  {per:7.1f} ug/depot  {per*8/1000:5.2f} mg per bilateral pulse")
print("""
→ OPERATIVE DOSE: 300 uM IN 2 mL = 337.8 ug OF SAG DIHYDROCHLORIDE PER DEPOT,
  2.70 mg FOR THE WHOLE BILATERAL PULSE.
  Justified three ways: one fewer Ihh-raising arm than R384 assumed; still 2.88x BELOW the
  rat-matched source strength, which is the deliberate margin for erdafitinib's residual
  Ihh elevation; and inside he2024sag's published in vivo range.
⚠ AND THE REVERSE RULE: IF A CNP ANALOGUE IS EVER RESTARTED, DROP BACK TO 100 uM - that
  restores the second ERK-lowering arm and moves him back up the Ihh band.""")
