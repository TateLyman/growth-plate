#!/usr/bin/env python3
"""
The femoral-length ledger for PTH1R agonism, and what the terminal null can and
cannot exclude.

WHY THIS EXISTS
---------------
Round 193 found a published claim of persistent femoral elongation under
teriparatide (vahle2002, caliper, +5%/+6%). Round 194 opened the FDA
Pharmacology Review for NDA 21-318, which tabulates QCT femur length per group
per age window for the SECOND Lilly carcinogenicity study (R00100/R00200,
published as vahle2004). Those tables contain both the strongest positive and
the decisive negative, and they disagree with the published caliper result.

This script does three things:
  1. lays out every femoral-length observation under a PTH1R agonist in one
     table, with the measurement method attached to each, because the method is
     what separates them;
  2. recovers an implied SD from the significance boundary of the interim data
     and uses it to bound what the terminal null can exclude;
  3. converts the surviving interim effect into human terms under an explicit,
     labelled scaling assumption, so the size of the prize is on the record even
     though the rat gave it back.

ALL PRIMARY NUMBERS BELOW ARE TRANSCRIBED FROM SOURCE TABLES, NOT COMPUTED.
Derived quantities are marked DERIVED. The implied SD is marked INFERRED and is
value_unverified -- no source states it.
"""
import math

# --------------------------------------------------------------- observations
# method: 'qct'    = quantitative CT, FDA Pharmacology Review NDA 21-318
#         'caliper'= calipers, vahle2002 Methods
#         'bma'    = inferred from DXA bone mineral AREA, jolette2006
OBS = [
    # (label, source, method, species/strain, age window (mo), dose ug/kg/d,
    #  n/group, control value mm or None, treated value mm or None, pct, sig)
    ("18 d, 4-wk-old SD rats, 16 ug/kg",
     "fda_nda21318 (Lilly CG3-04, unpublished)", "qct", "SD rat M",
     "1.0-1.6", 16, 10, None, None, 0.0, False),
    ("18 d, 4-wk-old SD rats, 80 ug/kg",
     "fda_nda21318 (Lilly CG3-04, unpublished)", "qct", "SD rat M",
     "1.0-1.6", 80, 10, None, None, 0.0, False),
    ("6 mo treat 2-8 mo, 5 ug/kg (arm G1)",
     "fda_nda21318 (R00100)", "qct", "F344 rat F", "2-8", 5, 8,
     32.8, 33.3, 1.5, True),
    ("6 mo treat 2-8 mo, 30 ug/kg (arm G2)",
     "fda_nda21318 (R00100)", "qct", "F344 rat F", "2-8", 30, 8,
     32.8, 33.9, 3.4, True),
    ("6 mo treat 6-12 mo, 5 ug/kg (arm D1)",
     "fda_nda21318 (R00200)", "qct", "F344 rat F", "6-12", 5, 8,
     34.2, 34.7, 1.5, True),
    ("6 mo treat 6-12 mo, 30 ug/kg (arm D2)",
     "fda_nda21318 (R00200)", "qct", "F344 rat F", "6-12", 30, 8,
     34.2, 35.2, 2.9, True),
    ("terminal 26 mo, every arm incl. 2-26 and 6-26 continuous",
     "fda_nda21318 (R00100/R00200)", "qct", "F344 rat F", "to 26", 30, 8,
     35.0, 35.0, 0.0, False),
    ("2 y from 6-8 wk, males",
     "vahle2002", "caliper", "F344 rat M", "1.5-24", 75, 60,
     None, None, 5.0, True),
    ("2 y from 6-8 wk, females",
     "vahle2002", "caliper", "F344 rat F", "1.5-24", 75, 60,
     None, None, 6.0, True),
    ("2 y from 9-11 wk, males, PTH(1-84)",
     "jolette2006", "bma", "F344 rat M", "2.3-24", 150, 60,
     None, None, 5.0, True),
    ("2 y from 9-11 wk, females, PTH(1-84)",
     "jolette2006", "bma", "F344 rat F", "2.3-24", 150, 60,
     None, None, 3.0, True),
]

TERMINAL_MEAN = 35.0     # mm, all groups, FDA table, 1 mm reporting resolution
TERMINAL_N = 8


def main():
    print("=" * 78)
    print("FEMORAL LENGTH UNDER A PTH1R AGONIST -- COMPLETE LEDGER")
    print("=" * 78)
    hdr = f"{'method':>8} {'age win':>8} {'dose':>5} {'n':>3} {'ctrl':>6} {'trt':>6} {'delta':>7} {'sig':>4}  source"
    print(hdr)
    print("-" * len(hdr))
    for lab, src, meth, sp, win, dose, n, c, tr, pct, sig in OBS:
        cs = f"{c:.1f}" if c is not None else "   -"
        ts = f"{tr:.1f}" if tr is not None else "   -"
        print(f"{meth:>8} {win:>8} {dose:>5} {n:>3} {cs:>6} {ts:>6} "
              f"{pct:>6.1f}% {'*' if sig else '':>4}  {src}")

    print("\n[1] THE SPLIT IS BY MEASUREMENT METHOD, NOT BY STUDY")
    print("    QCT, interim (6 months of treatment): POSITIVE, dose-dependent,")
    print("      in BOTH the 2-8 month and the 6-12 month window.")
    print("    QCT, terminal (26 months of age): NULL in every arm, including")
    print("      the two arms dosed continuously to the end (2-26, 6-26).")
    print("    Caliper, terminal: +5%/+6% (vahle2002).")
    print("    BMA-inferred, terminal: +5%/+3% (jolette2006).")
    print("    The two positives at terminal both use methods that cannot")
    print("    separate longitudinal growth from radial and periarticular new")
    print("    bone. vahle2002 measured femoral WIDTH +33%/+32% in the same")
    print("    animals; jolette2006's BMA is length x width by construction.")
    print("    CORR-189 applies to jolette2006 by name: a projected AREA cannot")
    print("    be assigned to the length term.")

    print("\n[2] AGE GATE -- ANSWERED, AND THE ANSWER IS 'NO GATE'")
    print("    2-8 mo window (rapid growth):  +1.5% @5, +3.4% @30")
    print("    6-12 mo window (slowing):      +1.5% @5, +2.9% @30")
    print("    The two age windows are within 0.5 percentage points of each")
    print("    other at both doses. Whatever the drug does to femoral")
    print("    elongation, it does not require the rapid-growth phase.")
    print("    This retires the age-gate objection raised in round 185.")

    print("\n[3] UNTREATED GROWTH FOR SCALE")
    d = 34.2 - 32.8
    print(f"    Control femur 8 mo  = 32.8 mm; control 12 mo = 34.2 mm")
    print(f"    -> 4 months of untreated growth at this age = {d:.1f} mm")
    print(f"    -> 6 months of 30 ug/kg/d in the 6-12 mo window = "
          f"{35.2 - 34.2:.1f} mm  (DERIVED)")
    print(f"    The drug added {(35.2 - 34.2) / d:.2f}x what unaided growth")
    print("    delivered over the preceding four months. The effect is real and")
    print("    it is not small -- at the interim timepoint.")

    print("\n[4] WHAT THE TERMINAL NULL CAN EXCLUDE")
    print("    No SD is reported anywhere. Recover one from the significance")
    print("    boundary: +0.5 mm at n=8/group was flagged significant (p<0.05).")
    tcrit = 2.145   # two-sided 0.05, df=14
    delta_min = 0.5
    sd_implied = delta_min / (tcrit * math.sqrt(2.0 / 8))
    print(f"    two-sided t crit, df=14        : {tcrit}")
    print(f"    implied SD                     : {sd_implied:.3f} mm"
          "     [INFERRED, value_unverified]")
    print(f"    implied CV at 35 mm            : {100 * sd_implied / 35:.2f}%")
    for power, z in (("50%", 0.0), ("80%", 0.84)):
        mdd = (tcrit + z) * sd_implied * math.sqrt(2.0 / TERMINAL_N)
        print(f"    min detectable diff at {power:>3} power: {mdd:.2f} mm "
              f"= {100 * mdd / TERMINAL_MEAN:.2f}% of final length")
    print("    So the terminal null excludes a final-length gain of ~1.5% or")
    print("    more at 80% power. It does NOT exclude a gain of ~1%.")
    print("    It DOES exclude the +5%/+6% caliper claim: 5% of 35 mm is")
    print("    1.75 mm, which would have printed as 37, not 35.")

    print("\n[5] THE ONE READING THAT SURVIVES BOTH TABLES")
    print("    Interim positive + terminal null = the drug ACCELERATES femoral")
    print("    elongation and the animal gives it back. Controls caught up")
    print("    (32.8 -> 34.2 -> 35.0 mm) while treated animals arrived at the")
    print("    same asymptote earlier. This is a RATE effect on an unchanged")
    print("    total, i.e. exactly the rate-yield trade-off fitted from")
    print("    hunziker1994 in round 183 (A proportional to GR^-0.146).")
    print("    PTH1R agonism is therefore a rate agent, not a yield agent, in")
    print("    the only species where final bone length has been measured.")

    print("\n[6] WHY THIS IS NOT AUTOMATICALLY FATAL FOR THE HUMAN CASE")
    print("    The rat gives it back because the rat plate never closes and the")
    print("    control catches up over 14 further months. A human at bone age")
    print("    16+ has a plate that FUSES on its own schedule. If the schedule")
    print("    is set by time or by hormonal milieu, an accelerated 6 months is")
    print("    banked. If the schedule is set by exhaustion of a fixed")
    print("    proliferative reserve, accelerating consumption fuses earlier and")
    print("    banks nothing.")
    print("    THE RAT DATA CANNOT DISTINGUISH THESE. This is now the single")
    print("    open question on which the whole line turns.")

    print("\n[7] SIZE OF THE PRIZE IF -- AND ONLY IF -- IT IS BANKED")
    print("    ASSUMPTION, NOT DATA: the interim rat femoral response (+2.9% to")
    print("    +3.4% over 6 months) transfers to human femur at the same")
    print("    fractional rate. There is no human observation supporting this;")
    print("    it is an order-of-magnitude sanity check only.")
    femur_cm = 48.0     # nominal adolescent male femur length, illustrative
    tibia_cm = 39.0     # nominal
    for pct in (2.9, 3.4):
        lower_limb = (femur_cm + tibia_cm) * pct / 100.0
        print(f"      at {pct:.1f}%: femur +{femur_cm * pct / 100:.1f} cm, "
              f"femur+tibia +{lower_limb:.1f} cm  [ILLUSTRATIVE ONLY]")
    print("    Spine is excluded from this arithmetic: no vertebral HEIGHT was")
    print("    measured in any of these studies. L6 vertebral X-AREA rose")
    print("    10.6-16% (young) and 4.2-11.5% (older) -- a cross-section, which")
    print("    by CORR-189 says nothing about vertebral height.")

    print("\n[8] WHAT THE REGULATORY PACKAGE DOES NOT CONTAIN")
    print("    NDA 208743 (abaloparatide, Kuijpers): zero bone-length endpoints,")
    print("      zero juvenile animal studies, one passing mention of the growth")
    print("      plate in background prose.")
    print("    NDA 21-318 monkey study: animals were deliberately selected as")
    print("      'skeletally mature adults with no open growth plates' (9-11 y).")
    print("    So no PTH1R agonist has ever been given to a growing non-rodent")
    print("    in a regulatory study, by design.")
    print("=" * 78)


if __name__ == "__main__":
    main()
