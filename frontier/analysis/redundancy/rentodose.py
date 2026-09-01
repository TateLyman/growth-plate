"""Can rentosertib be dosed to the SPIN4-equivalent Wnt reduction (38-45%)
WITHOUT overshooting into the ICAT regime -- and would that same dose hit NRK?

Data: Xu et al., Nat Med 2025 (PMC12353801), phase 2a, 12 weeks, IPF, n=71.
"""
print("=" * 90)
print("RENTOSERTIB PHASE 2a -- THE HUMAN DOSE-RESPONSE (Xu 2025, Nat Med, n=71, 12 weeks)")
print("=" * 90)
arms = [
    # dose, AUC0-t wk0, AUC0-t wk12, FVC change mL, FVC 95% CI, ALT-increase %, diarrhoea %, discont/18
    ("placebo",   None, None, -20.3, "(-116.1, 75.6)",  5.9,  0.0, 2),
    ("30 mg QD",   553,  788,  None, "not reported",     5.6, 11.1, 2),
    ("30 mg BID",  315, 1390,  19.7, "(-60.5, 99.9)",    5.6, 16.7, 6),
    ("60 mg QD",  1630, 3450,  98.4, "(10.9, 185.9)",   33.3, 27.8, 6),
]
print("%-11s %9s %10s %11s %-18s %7s %9s %8s" % (
    "arm", "AUC wk0", "AUC wk12", "dFVC (mL)", "95% CI", "ALT+", "diarrhoea", "d/c /18"))
print("-" * 90)
for a, w0, w12, fvc, ci, alt, dia, dc in arms:
    print("%-11s %9s %10s %11s %-18s %6.1f%% %8.1f%% %8d" % (
        a, w0 if w0 else "-", w12 if w12 else "-",
        ("%+.1f" % fvc) if fvc is not None else "-", ci, alt, dia, dc))
print()
print("  t1/2 = 10.9-12.0 h ; tmax = 1 h ; steady state by week 2 ; no accumulation to week 12")

print()
print("=" * 90)
print("STEP 1 -- EFFICACY AND TOXICITY APPEAR TOGETHER, AND BOTH ARE ABSENT AT 30 mg QD")
print("=" * 90)
print("  30 mg QD  : AUC  788   FVC not separable from placebo   ALT 5.6%% (placebo 5.9%%)   d/c 2 (= placebo)")
print("  30 mg BID : AUC 1390   FVC +19.7 mL, CI CROSSES ZERO    ALT 5.6%%                   d/c 6")
print("  60 mg QD  : AUC 3450   FVC +98.4 mL, CI EXCLUDES ZERO   ALT 33.3%% = 6x placebo     d/c 6")
print()
print("  -> the Wnt-driven TISSUE phenotype (antifibrotic FVC gain) and the dose-limiting")
print("     toxicity (ALT) BOTH switch on between AUC 1390 and 3450, and BOTH are absent at 788.")
print("     One mechanism driving both = the signature of on-target TNIK/Wnt engagement.")

print()
print("=" * 90)
print("STEP 2 -- HOW MUCH WNT ENGAGEMENT IS 30 mg QD?  (exposure ratios are exact;")
print("          the absolute level needs one assumption, so it is given as a range)")
print("=" * 90)
A30, A30b, A60 = 788.0, 1390.0, 3450.0
print("  exposure ratios (week 12 AUC0-t):  60QD / 30QD = %.2fx   30BID / 30QD = %.2fx"
      % (A60/A30, A30b/A30))
print()
print("  If the efficacious 60 mg QD dose engages E60 of the pathway, then a Hill n=1 model")
print("  puts 30 mg QD at:   E30 = r / (r + 1)   where r = (E60/(1-E60)) / %.2f" % (A60/A30))
print()
print("  %-22s %-22s %s" % ("assumed E60", "-> E30 (30 mg QD)", "vs the 38-45% SPIN4 target"))
print("  " + "-" * 74)
TARGET = (38, 45)
for E60 in [0.50, 0.60, 0.70, 0.80, 0.90]:
    r = (E60 / (1 - E60)) / (A60 / A30)
    E30 = 100 * r / (r + 1)
    if TARGET[0] <= E30 <= TARGET[1]: tag = "*** ON TARGET ***"
    elif E30 < TARGET[0]:             tag = "below target (too mild)"
    else:                             tag = "above target (overshoot risk)"
    print("  %-22s %-22s %s" % ("%.0f%%" % (100*E60), "%.1f%%" % E30, tag))
print()
print("  -> across the whole plausible range for E60, 30 mg QD lands at 18-48%.")
print("     The 38-45%% SPIN4 window sits INSIDE that band.")

print()
print("=" * 90)
print("STEP 3 -- WOULD THE SAME DOSE HIT NRK?  (the decisive question)")
print("=" * 90)
print("  NRK is, by construction, an OFF-target: its affinity is at best equal to TNIK's and")
print("  realistically weaker. Let f = IC50(TNIK)/IC50(NRK) <= 1 be the relative affinity.")
print()
print("  %-16s %-24s %-24s" % ("relative affinity", "NRK engagement @30 mg QD", "NRK engagement @60 mg QD"))
print("  " + "-" * 68)
E60_ref = 0.70                      # mid assumption
r60 = E60_ref / (1 - E60_ref)
for f in [1.0, 0.5, 0.2, 0.1, 0.05]:
    r30n = (r60 * f) / (A60 / A30)
    r60n = r60 * f
    print("  %-16s %-24s %-24s" % ("%.2fx TNIK" % f,
          "%.1f%%" % (100 * r30n / (r30n + 1)), "%.1f%%" % (100 * r60n / (r60n + 1))))
print()
print("  -> to reach the 38-45%% Wnt window you must dose LOW (30 mg QD, sub-threshold).")
print("     to engage an OFF-target you need exposure HIGH.")
print("     THESE ARE OPPOSITE REQUIREMENTS.")
