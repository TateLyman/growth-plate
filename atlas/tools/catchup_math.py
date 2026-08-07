# Figure-read digitisation. Values are MY readings off rendered figures, +/- roughly 10-15%.
# Forcinito 2011 Fig 1B: tibial growth rate (mm/wk) vs age (wk).  Trp- diet birth->4wk.
import numpy as np
age_f   = np.array([2,   4,   6,   8,  12,  16,  18])
ctrl_f  = np.array([5.0, 3.7, 2.7, 2.4, 0.5, 0.1, 0.0])
trp_f   = np.array([1.3, 1.5, 5.5, 3.7, 0.8, 0.2, 0.1])
Ic = np.trapezoid(ctrl_f, age_f); It = np.trapezoid(trp_f, age_f)
print("FORCINITO Fig 1B, integrated tibial growth 2->18 wk")
print(f"  control  {Ic:5.1f} mm      Trp-  {It:5.1f} mm      Trp- gains {It-Ic:+.1f} mm overall")
# restrict to post-treatment recovery only (4 wk onward)
m = age_f>=4
Ic4 = np.trapezoid(ctrl_f[m], age_f[m]); It4 = np.trapezoid(trp_f[m], age_f[m])
print(f"  from 4 wk (end of deficiency): control {Ic4:5.1f}  Trp- {It4:5.1f}  -> Trp- gains {It4-Ic4:+.1f} mm")
print(f"  measured deficit at 4 wk (paper text): 10.1 mm  (16.5 vs 26.6)")
print(f"  => projected residual deficit at 18 wk: {10.1-(It4-Ic4):+.1f} mm  ({100*(1-(10.1-(It4-Ic4))/10.1):.0f}% of deficit recovered)")
print(f"  both curves at 16-18 wk are ~0 mm/wk -> animals had PLATEAUED, so this is a final value\n")

# Marino 2008 Fig 2: tibia length (mm) vs age.  PTU day1 -> 8wk.
age_c = np.array([3,6,8,11,13,16,21]); ctrl_m = np.array([22,33,36,37.5,38.5,38.5,39.7])
age_p = np.array([8,11,13,16,21]);     ptu_m  = np.array([22,28,32,34,35.5])
print("MARINO Fig 2, tibia length (mm)")
print(f"  at  8 wk (end of PTU): control {ctrl_m[2]:.1f}  PTU {ptu_m[0]:.1f}  deficit {ctrl_m[2]-ptu_m[0]:.1f} mm")
print(f"  at 21 wk (last):       control {ctrl_m[-1]:.1f}  PTU {ptu_m[-1]:.1f}  deficit {ctrl_m[-1]-ptu_m[-1]:.1f} mm")
rec = 1-(ctrl_m[-1]-ptu_m[-1])/(ctrl_m[2]-ptu_m[0])
print(f"  recovered {100*rec:.0f}% of the deficit; PTU tibia is {100*ptu_m[-1]/ctrl_m[-1]:.1f}% of control")
rc = (ctrl_m[-1]-ctrl_m[-3])/(21-13); rp = (ptu_m[-1]-ptu_m[-3])/(21-13)
print(f"  growth rate 13->21 wk: control {rc:.2f} mm/wk, PTU {rp:.2f} mm/wk -> gap closing {rp-rc:.2f} mm/wk")
print(f"  NEITHER curve is flat at 21 wk, so this is NOT a final value\n")
print("MARINO other tissues at last measurement, PTU as % of control:")
for nm,c,p in [("body mass (16wk)",275,150),("tail length (16wk)",17.5,14.5),
               ("heart (21wk)",1.0,0.58),("liver (21wk)",10.2,5.8),("kidney (21wk)",0.97,0.53)]:
    print(f"  {nm:20s} {100*p/c:5.1f}%")
print(f"  {'tibia (21wk)':20s} {100*ptu_m[-1]/ctrl_m[-1]:5.1f}%   <- the plate recovers best of any measure")
