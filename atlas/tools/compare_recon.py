import numpy as np
print("="*66); print("MARINO 2008 Fig 2 tibia - two independent reconstructions")
ages=[3,6,8,11,13,16,21]
mine_c=[22,33,36,37.5,38.5,38.5,39.7]; cal_c=[21.60,32.85,35.89,38.11,39.03,38.57,39.77]
mine_p=[None,None,22,28,32,34,35.5];   cal_p=[None,None,20.30,28.15,32.02,34.23,35.80]
print(f"{'age':>4} {'ctrl mine':>10} {'ctrl cal':>9} {'d':>6} | {'PTU mine':>9} {'PTU cal':>8} {'d':>6}")
for i,a in enumerate(ages):
    pm = f"{mine_p[i]:9.1f}" if mine_p[i] else " "*9
    pc = f"{cal_p[i]:8.2f}" if cal_p[i] else " "*8
    pd = f"{mine_p[i]-cal_p[i]:+6.2f}" if mine_p[i] else " "*6
    print(f"{a:>4} {mine_c[i]:10.1f} {cal_c[i]:9.2f} {mine_c[i]-cal_c[i]:+6.2f} | {pm} {pc} {pd}")
d8_m,d8_c = 36-22, 35.89-20.30; d21_m,d21_c = 39.7-35.5, 39.77-35.80
print(f"\n  deficit at 8wk : mine {d8_m:.2f}   calibrated {d8_c:.2f}   <- our largest disagreement")
print(f"  deficit at 21wk: mine {d21_m:.2f}   calibrated {d21_c:.2f}")
print(f"  recovered      : mine {100*(1-d21_m/d8_m):.1f}%  calibrated {100*(1-d21_c/d8_c):.1f}%")

print("\n"+"="*66); print("FORCINITO/LUI - my Fig1B integration vs their Lui absolute curve")
lui_age=[1,2,4,5,6,8,12,16,20]
lui_c=[12.5,17.4,26.75,30.72,34.23,38.67,43.81,45.91,45.44]
lui_t=[12.5,14.1,16.47,20.21,25.82,33.06,40.07,42.41,43.57]
i4=lui_age.index(4)
gc = lui_c[-1]-lui_c[i4]; gt = lui_t[-1]-lui_t[i4]
print(f"  Lui curve, growth 4->20 wk : control {gc:5.2f} mm   Trp- {gt:5.2f} mm   Trp- gains {gt-gc:+.2f}")
print(f"  my Fig 1B integration 4->18: control 18.60 mm   Trp- 27.50 mm   Trp- gains +8.90")
print(f"  deficit at 4 wk: Lui recon {lui_c[i4]-lui_t[i4]:.2f}   Forcinito PRINTED 10.1 (26.6 vs 16.5)")
print(f"  residual at end: Lui recon {lui_c[-1]-lui_t[-1]:.2f} mm   my integration {10.1-8.9:.2f} mm")
print(f"  Gafni MEASURED (rabbit femur, different inhibitor): 1.6 +/- 1.6 mm, NS")

print("\n"+"="*66); print("WHAT THE RESIDUAL IS AS A FRACTION OF FINAL BONE LENGTH")
for nm,res,final in [("Gafni rabbit femur", 1.6, 17.4/0.91),   # final approx from deficit/recovery
                     ("Lui/Forcinito rat tibia", 1.87, 45.44),
                     ("Marino rat tibia (NOT plateaued)", 3.97, 39.77)]:
    print(f"  {nm:34s} {res:4.2f} mm  =  {100*res/final:4.1f}% of final length")
print("\n  recovery fraction vs how late/short/mild the insult was:")
for nm,rec,ins in [("Marino  8wk PTU from day 1", 74.5,"harshest, earliest"),
                   ("Lui/Forc 4wk Trp- from birth", 81.8,"middle"),
                   ("Gafni   5wk dex from 5wk of age", 90.8,"latest, mildest")]:
    print(f"    {nm:32s} {rec:5.1f}%   {ins}")
