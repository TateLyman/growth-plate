print("=== WHY 'gain vs PAH' OVERSTATES, AND WHAT THE CLEAN NUMBERS ARE ===")
print("The atlas's own remaining_growth_prediction node: BP/TW 95% prediction interval")
print("  = +/- 4 to 8 cm, i.e. 'error large enough to swallow the effect size of most")
print("  growth-promoting interventions'. Gain-vs-PAH also regresses to the mean.")
print("  => USE RANDOMISED / INTERNALLY-CONTROLLED CONTRASTS ONLY.\n")
rows=[("GH vs PLACEBO (Leschek, randomised, double-blind, peripubertal ISS)",3.7,"randomised"),
      ("AI on top of GH (matched pairs, >=2 yr anastrozole, p=0.044)",3.3,"internally controlled"),
      ("GH+AI vs GH alone (advanced-BA males, 173.2 vs 170.9)",2.3,"internally controlled"),
      ("GH dose 0.37 vs 0.24 mg/kg/wk, adjusted final height",3.6,"internally controlled")]
for n,v,k in rows: print(f"  +{v:4.1f} cm  {n:62s} [{k}]")
print("\n  GH vs placebo + AI on top of GH  = +{:.1f} cm  <- defensible combined estimate".format(3.7+3.3))
print("  (matches the operator's quoted 7.2 cm at the higher dose)")
print("\n=== WHAT THIS DOES TO MY 2.19 cm 'HARD CEILING' ===")
print("  BP at SA16.0 = 98.8% of adult height -> 2.19 cm remaining.")
print("  BUT BP PREDICTS THE **UNTREATED** TRAJECTORY.")
print("  GH+AI raised HtSDS-BA by +2.76 SD = MORE HEIGHT AT THE SAME SKELETAL MATURITY.")
print("  => THE BP RELATION IS NOT A CEILING. IT IS THE CONTROL ARM.")
print("  => my '2.19 cm is what remains' was WRONG as a bound.\n")
print("=== THE COUNTER, MEASURED ===")
for n,ba,yr in [("GH alone",1.2,2.08),("GH + AI (advanced-BA study)",0.2,1.89),
                ("GH + AI (matched-pair study)",1.37,1.0),("GH alone (matched-pair)",1.81,1.0),
                ("ESR1-null human (herrmann/Smith)",2.5,3.5)]:
    print(f"   {n:34s} {ba/yr:5.2f} BA-yr per calendar yr")
print("\n   => GH+AI in the advanced-BA study ran the counter at 0.11 BA-yr/yr,")
print("      SLOWER THAN THE OESTROGEN-NULL HUMAN (0.71). Arm3's stated target, achieved.")
print("\n=== HONEST TRANSFER TO BA 16 ===")
print("  tested range: BA 13.0-15.0 at start (14.0 mean). Paper: 'did not test outcomes at BA 16 or older'")
print("  and 'an advanced stage of bone age limits the application window'.")
print("  Subject is BA 16 and 180.3 cm; trial boys were SHORT (PAH ~161-170).")
print("  => extrapolation is ONE bone-age year, but into a taller, later subject with less room.")
