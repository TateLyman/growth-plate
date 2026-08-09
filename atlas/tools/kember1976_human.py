#!/usr/bin/env python3
"""
THE HUMAN ANCHOR FOR THE YIELD PROGRAMME - kember1976, distal femur.

The atlas has recorded that no human yield, amplification or transit time exists.
kember1976 does not give a yield either - it has no resting-zone CELL COUNT, only an
"inert zone" WIDTH - but it gives the two things the rodent decomposition most needs
checking against in man: the size of the amplifying compartment across age, and the
terminal hypertrophic cell height across age, in the same columns.

Table I, distal femur, mean values per column. Growth rates from serial radiographs
in the Harpenden Growth Study. Transcribed from the published table.
"""
import numpy as np
# age, sex, maturing+proliferating cells, hypertrophic cells, THC height um,
# inert zone mm, columnar zone mm
T = [
 (0.0,  'M', 62, 12, 35, None, 0.9),
 (0.9,  'M', 43,  8, 38, 0.8,  0.7),
 (1.3,  'F', 46,  8, 34, 0.6,  0.8),
 (2.0,  'M', 49,  6, 30, 0.9,  0.7),
 (2.0,  'M', 48,  8, 35, 0.8,  0.7),
 (3.5,  'M', 54,  7, 38, 1.1,  0.8),
 (5.0,  'M', 36,  6, 33, 1.0,  0.6),
 (7.0,  'M', 36,  7, 37, 1.2,  0.6),
 (8.0,  'M', 34,  8, 29, 0.5,  0.5),
 (13.0, 'M', 27,  5, 30, 0.8,  0.5),
 (14.0, 'M', 28,  6, 39, 0.7,  0.5),
 (14.0, 'F', 21,  2, 25, 0.1,  0.4),
]
print("="*78)
print("HUMAN DISTAL FEMUR ACROSS GROWTH - kember1976 Table I")
print("="*78)
print(f"{'age':>5} {'sex':>3} {'mat+prolif':>11} {'hypertroph':>11} {'THC um':>8} {'inert mm':>9} {'colum mm':>9}")
for a,s,mp,h,thc,iz,cz in T:
    print(f"{a:>5.1f} {s:>3} {mp:>11} {h:>11} {thc:>8} {str(iz):>9} {cz:>9}")

mp = np.array([r[2] for r in T], float); thc = np.array([r[4] for r in T], float)
age = np.array([r[0] for r in T], float)
print("\n" + "="*78)
print("THE HUMAN VERSION OF THE ROUND-174 DECOMPOSITION")
print("="*78)
early = age <= 2.0; late = age >= 13.0
print(f"  amplifying compartment (mat+prolif cells/column)")
print(f"    birth-2y  mean {mp[early].mean():6.1f}   13-14y mean {mp[late].mean():6.1f}"
      f"   ratio {mp[early].mean()/mp[late].mean():5.2f}x")
print(f"  terminal hypertrophic cell height (um)")
print(f"    birth-2y  mean {thc[early].mean():6.1f}   13-14y mean {thc[late].mean():6.1f}"
      f"   ratio {thc[early].mean()/thc[late].mean():5.2f}x")
import math
r_amp = mp[early].mean()/mp[late].mean(); r_thc = thc[early].mean()/thc[late].mean()
tot = r_amp*r_thc
print(f"\n  combined fall in (compartment x cell height) = {tot:.2f}x")
print(f"    share of the log fall from COMPARTMENT SIZE: {100*math.log(r_amp)/math.log(tot):4.0f}%")
print(f"    share from TERMINAL CELL HEIGHT:             {100*math.log(r_thc)/math.log(tot):4.0f}%")
print(f"\n  the single most closed plate in the series (14y female, inert zone 0.1 mm):")
print(f"    compartment 21 cells against a birth-to-2y mean of {mp[early].mean():.0f}"
      f"  = {mp[early].mean()/21:.2f}x fall")
print(f"    THC height 25 um against {thc[early].mean():.0f} um  = {thc[early].mean()/25:.2f}x fall")

print("\n" + "="*78)
print("TERMINAL CELL HEIGHT IS CONSERVED ACROSS SPECIES, NOT JUST ACROSS BONES")
print("="*78)
print(f"  human  distal femur, birth to 14y   {thc.min():.0f}-{thc.max():.0f} um   (kember1976)")
print( "  mouse  femur/tibia, 1-12wk          18-33 um     (lui2018 Fig1C)")
print( "  rat    femur/tibia, 1-16wk          18-38 um     (lui2018 FigS2)")
print("""  These three span a TEN-FOLD difference in proliferative cell cycle time
  (human about 20 days, rodent about 2 days - kember1976's own comparison) and the
  terminal cell height ranges overlap almost completely. A fourth independent line
  for the round-174 decomposition: the cell-size term is the conserved one.""")

print("="*78)
print("THE KINETIC NUMBER, AND KEMBER'S OWN WARNING")
print("="*78)
print("""  At 5-8 years the distal femur grows 1.4 cm/year = 38 um/day. With a terminal
  hypertrophic cell height of about 33 um that is 1.2 NEW CELLS PER COLUMN PER DAY.
  With about 24 proliferating cells per column, the mean cell cycle time is 20 DAYS.

  For comparison, this atlas computed 10.8 and 8.33 new cells per column per day for
  the MOUSE femur at 1 and 3 weeks (round 174) - roughly ten times the human rate,
  matching kember1976's independent statement that the rodent cycle time is 2 days
  against 20 in man.

  KEMBER'S OWN CONCLUSION, AND IT APPLIES DIRECTLY TO THIS PROGRAMME: "Since the
  corresponding cycle time is two days for rodent growth plates, which also have a
  different structure, IT IS UNWISE TO EXTRAPOLATE THE FINDINGS IN THIS TISSUE FROM
  MOUSE TO MAN."

  A STRUCTURAL DIFFERENCE HE ALSO NAMES. In man an INERT ZONE 0.5-1.2 mm thick lies
  between the proliferating cells and the epiphysial vessels; in rat and rabbit the
  proliferative zone is nourished directly by those vessels. The human amplifying
  compartment sits behind a diffusion barrier the rodent one does not have.

  CAVEAT ON THE COMPARTMENT COUNTS. Kember could not distinguish proliferating from
  maturing cells morphologically and estimated the proliferative fraction as two
  thirds, BY ANALOGY WITH RABBIT. The mat+prolif totals above are measured; the split
  into 24 proliferating cells is an assumption imported from another species.
""")
