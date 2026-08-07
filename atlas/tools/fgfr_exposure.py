# FGFR arm: target coverage at the doses that are actually proven, vs the stack's proposed dose.
MW_INFI = 560.4   # g/mol
print("="*70); print("INFIGRATINIB - oncology PK anchor (user-supplied, FDA)")
cmax_ng = 282.5; fu = 0.032
tot_nM = cmax_ng/MW_INFI*1000
free_nM = tot_nM*fu
print(f"  125 mg/day: total Cmax {cmax_ng} ng/mL = {tot_nM:.0f} nM; fu {fu*100:.1f}% -> free Cmax {free_nM:.1f} nM")
for ic,lab in [(2.0,"FGFR3 biochemical"),(1.99,"FGFR3-G380R (ACH mutant)"),(3.01,"HCH variants, mean")]:
    print(f"    vs {lab:28s} IC50 {ic:4.2f} nM -> {free_nM/ic:5.1f}x coverage")
print("\n  PROVEN GROWTH DOSE 0.25 mg/kg/day:")
for wt in (25,60):
    mg = 0.25*wt; ratio = mg/125; f = free_nM*ratio
    print(f"    {wt} kg -> {mg:5.2f} mg/day = {ratio:.3f}x the oncology dose -> free Cmax ~{f:.2f} nM = {f/2.0:.2f}x FGFR3 IC50")
print("    (assumes dose-proportional PK; infigratinib binding is reported concentration-dependent)")
print("\n" + "="*70); print("ERDAFITINIB at the stack's proposed 8 mg (FDA review, measured)")
print(f"  free Cmax 6.3 nM vs FGFR3 IC50 3.0 nM -> {6.3/3.0:.1f}x coverage")
print("\n  SO AT PROVEN-EFFECTIVE DOSES:")
print(f"    infigratinib 0.25 mg/kg (60 kg) ~ {free_nM*(0.25*60/125)/2.0:.2f}x IC50   <- delivers +1.74 cm/yr in phase 3")
print(f"    erdafitinib  8 mg               ~ {6.3/3.0:.2f}x IC50")
print("\n" + "="*70); print("DOSE-RESPONSE SHAPE - the decisive fact")
print("  PROPEL 2 cohorts: 0.016, 0.032, 0.064, 0.128, 0.25 mg/kg (n=8,19,16,16,13)")
print("  Effect appeared ONLY in cohort 5 (0.25 mg/kg): +2.50 cm/yr at 18 mo (95% CI 1.22-3.79, P=0.001)")
print("  -> the highest dose tested is the FIRST one that works. Curve is still CLIMBING, not plateaued.")
print("  -> oncology used up to 200 mg/day; growth doses are 10-100x lower. Large characterised headroom.")
print("\n" + "="*70); print("HEAD TO HEAD, PLACEBO-ADJUSTED, SAME DISEASE (achondroplasia)")
print("  infigratinib PROPEL 3 (n=114): LS mean difference +1.74 cm/yr (95% CI 1.31-2.1)")
print("                                 raw mean difference +2.10 cm/yr (SE 0.36)")
print("  vosoritide pivotal   (n=121): +1.57 cm/yr vs placebo")
print("  -> EQUIVALENT. The narrative review's '6.0 cm/yr infigratinib' was not placebo-adjusted and is refuted.")
print("\n  OUTSIDE achondroplasia: vosoritide +3.56 cm/yr (dauber2026, within-subject, n=28).")
print("  No infigratinib equivalent exists outside achondroplasia.")
