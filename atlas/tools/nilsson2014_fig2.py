#!/usr/bin/env python3
"""
nilsson2014 Figure 2, DIGITISED BY EYE from the published panel (user-supplied image).

The gap g_l2_raise_the_yield_per_progenitor records that this figure holds the terms
of a yield under a PERTURBATION but that they exist only as raster plots. These are
read-off values with axis calibration by eye. THEY ARE NOT MEASUREMENTS. Read error is
estimated at roughly half a minor gridline and is stated per panel.

Design: ovariectomised juvenile rabbits. TREATMENT 11->16 wk (estradiol vs vehicle),
then WASHOUT 16->21 wk with no treatment in either arm.
"""
import itertools

# panel: {bone: {age: (vehicle, estradiol)}}   read error in the last column
D = {
 "GP height (um)":            {"tibia":  {11:(523,520), 16:(432,372), 21:(300,277)},
                               "radius": {11:(490,490), 16:(401,337), 21:(279,215)}, "err":"+-5 um"},
 "PZ (cells/column)":         {"tibia":  {11:(41.0,41.0), 16:(32.5,25.0), 21:(19.0,13.0)},
                               "radius": {11:(46.0,46.0), 16:(36.5,26.3), 21:(23.0,14.0)}, "err":"+-0.5 cell"},
 "HZ (cells/column)":         {"tibia":  {11:(14.6,14.6), 16:(9.0,8.2),  21:(5.6,4.85)},
                               "radius": {11:(12.8,12.8), 16:(11.1,7.6), 21:(6.2,4.8)},  "err":"+-0.2 cell"},
 "RZ (cells/mm GP width)":    {"tibia":  {11:(35.3,35.3), 16:(26.3,21.2), 21:(17.7,14.3)},
                               "radius": {11:(36.8,36.8), 16:(29.0,21.5), 21:(23.5,15.2)}, "err":"+-0.5 cell/mm"},
}
print("="*78); print("nilsson2014 Fig 2 - digitised. Rabbit. TREATMENT 11-16wk, WASHOUT 16-21wk.")
print("="*78)
for panel, blk in D.items():
    print(f"\n{panel}   (read error {blk['err']})")
    print(f"  {'bone':<8}{'age':>5}{'vehicle':>10}{'estradiol':>11}{'E2 deficit':>12}")
    for bone in ("tibia","radius"):
        for age,(v,e) in sorted(blk[bone].items()):
            print(f"  {bone:<8}{age:>5}{v:>10.1f}{e:>11.1f}{v-e:>12.1f}")

print("\n" + "="*78)
print("STRUCTURAL AMPLIFICATION INDEX = PZ cells per column / RZ cells per mm width")
print("cells held in the amplifying compartment per unit progenitor stock")
print("="*78)
print(f"{'bone':<8}{'age':>5}{'vehicle':>10}{'estradiol':>11}{'E2/veh':>9}")
for bone in ("tibia","radius"):
    for age in (11,16,21):
        pz = D["PZ (cells/column)"][bone][age]; rz = D["RZ (cells/mm GP width)"][bone][age]
        av, ae = pz[0]/rz[0], pz[1]/rz[1]
        print(f"{bone:<8}{age:>5}{av:>10.3f}{ae:>11.3f}{ae/av:>9.3f}")

print("""
WHAT THIS IS AND IS NOT
-----------------------
NOT the yield. A yield is a FLUX over a FLUX - proliferative output per progenitor
CONSUMED over an interval. Both terms here are STANDING STOCKS at an instant. The
flux numerator lives in the paper's Figure 3 (BrdU proliferation rate), which is not
in the panel supplied.

WHAT IT DOES SHOW. The amplifying compartment per unit progenitor stock DECLINES WITH
AGE in both bones and both arms - tibia 1.16 at 11wk to about 1.0 at 21wk - and is
LOWER UNDER OESTROGEN at every age after baseline. That is the direction nilsson2014
asserts and never quantified. The effect is modest, roughly 5-15 per cent, and it is
NOT independent of the yield claim because both use the same resting-zone denominator.

THE DESIGN POINT THAT MATTERS MOST. 16-21wk is a WASHOUT - no drug in either arm. The
oestrogen-treated plates continue to run at a lower amplification index through a
period when no oestrogen is present. Whatever oestrogen did to the exchange rate, it
was not reversed by removing it.
""")
