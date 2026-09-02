#!/usr/bin/env python3
"""
R483 -- THE BAT WITHIN-ANIMAL DECOMPOSITION OF dL/dt = flux x v(d).

Every number below is read from farnum2007 "3" (Cells Tissues Organs
2008;187:35-47), Tables 1, 3 and 5, for ONE 13-day-old Eptesicus fuscus.
Twenty-nine growth plates from a single animal, so systemic hormone,
age, nutrition, sex and genotype are held constant BY DESIGN.  That is
what makes this the cleanest within-organism contrast in the atlas.

TWO THINGS THIS SCRIPT ESTABLISHES

  (1) THE FIELD'S OWN "CELLS PER DAY" SETS v(m) = 0.
      Farnum computes cells turned over per day as
          elongation / terminal hypertrophic CELL HEIGHT
      (verified on the tibia: 132 / 11.3 = 11.68, printed 11.7).
      But the terminal chondrocytic DOMAIN v(d) is the cell-to-cell
      centre distance, which is cell height PLUS the transverse septum.
      Vanky 2000 measures both in mouse: v_d 22.1 um vs v_c 17.7 um,
      so v_m is 20% of the domain in a normal animal.
      => every terminal-chondrocyte life span computed this way is
         ~20% too SHORT and every flux ~25% too HIGH.
      This is a systematic arithmetic feature of the primary
      literature, not an error in one paper.

  (2) WITHIN ONE ANIMAL, THE TERMINAL DOMAIN CARRIES MOST OF THE
      ELONGATION DIFFERENCE BETWEEN BONES -- the opposite of every
      variance decomposition in the atlas (R423, R449, R455, R470).
      The log-share split is computed below.

NOTE ON THE ATLAS'S OWN UNVERIFIED CLAIM.  CLAUDE.md R480 correction #4
records "the bat 40,300 / 1,300 figures are NOT verifiable".  They are
in Table 1, once each, verified in this session by reading the file:
  40,300 um^3 = terminal hypertrophic cell volume, metacarpal, digit 4, MANUS
   1,300 um^3 = terminal hypertrophic cell volume, phalanx 1, digit 5, PES
They are a BETWEEN-BONE comparison of terminal cell volumes, NOT a
within-plate proliferative-to-hypertrophic fold change.  The correction
was right that they are not a fold change; their identity is now settled.
The paper's largest within-plate fold change is 71.3x (digit 3 manus P2)
and its abstract says "volume changes approaching x70".
"""

from math import log

# --- Table 5, proximal tibia of the SAME animal (the internal control) ---
TIBIA = dict(name="proximal tibia", rate=132.0, h_height=11.3, h_vol=2240.0,
             p_vol=830.0, cells_day_printed=11.7)

# --- Tables 1 + 3, digit 3, same animal ---
MC3 = dict(name="metacarpal digit 3 (MANUS)", rate=1040.0, h_height=54.5,
           h_vol=33900.0, p_vol=900.0, cells_day_printed=None)
MT3 = dict(name="metatarsal digit 3 (PES)", rate=65.0, h_height=10.1,
           h_vol=1580.0, p_vol=590.0, cells_day_printed=None)
MC4 = dict(name="metacarpal digit 4 (MANUS)", rate=1020.0, h_height=52.5,
           h_vol=40300.0, p_vol=780.0, cells_day_printed=None)

PLATES = [MC3, MC4, TIBIA, MT3]


def line(c="-"):
    print(c * 78)


print(__doc__)
line("=")
print("STEP 0  --  VERIFY FARNUM'S FLUX CONSTRUCTION ON HIS OWN PRINTED VALUE")
line()
calc = TIBIA["rate"] / TIBIA["h_height"]
print(f"  tibia elongation / terminal cell HEIGHT = {TIBIA['rate']:.0f} / "
      f"{TIBIA['h_height']:.1f} = {calc:.2f}")
print(f"  printed 'Cells/day' in Table 5           = {TIBIA['cells_day_printed']}")
print(f"  => CONFIRMED: flux := rate / v_c, i.e. the construction sets v_m = 0.")
print()
print("  Vanky 2000 (mouse, bm/+ control) measures the domain directly:")
print("      v_d (final cell-centre distance) = 22.10 um")
print("      v_c (terminal cell height)       = 17.68 um")
print("      v_m                              =  4.42 um  = 20.0% of v_d")
print(f"  Applying that 20% to the bat tibia:")
vd_corr = TIBIA["h_height"] / 0.800
print(f"      implied v_d = {TIBIA['h_height']:.1f} / 0.800 = {vd_corr:.2f} um")
print(f"      corrected flux = {TIBIA['rate']:.0f} / {vd_corr:.2f} = "
      f"{TIBIA['rate']/vd_corr:.2f} cells/day, not {TIBIA['cells_day_printed']}")
print("      => published flux overstated by "
      f"{100*(TIBIA['cells_day_printed']/(TIBIA['rate']/vd_corr)-1):.0f}% "
      "if the mouse matrix share transfers.")
print()

line("=")
print("STEP 1  --  THE PLATES, AS PRINTED")
line()
print(f"{'plate':<32}{'um/day':>9}{'v_c um':>9}{'V_h um3':>11}{'V_p um3':>9}")
for p in PLATES:
    print(f"{p['name']:<32}{p['rate']:>9.0f}{p['h_height']:>9.1f}"
          f"{p['h_vol']:>11.0f}{p['p_vol']:>9.0f}")
print()
print("  Proliferative-zone cell volume spans only 590-900 um3 across these")
print("  four plates while terminal volume spans 1,580-40,300 um3.")
print("  Farnum paper 4, Fig 7 legend: proliferative cell volume is")
print("  essentially constant in all growth plates.")
print()

line("=")
print("STEP 2  --  DECOMPOSE EACH CONTRAST AS flux x v_c  (v_m assumed equal)")
line()
print("  dL/dt = flux x v_d.  With v_m unmeasured in the bat, this uses")
print("  v_c as a lower bound on v_d.  If v_m scales with v_c the split is")
print("  unchanged; if v_m is constant the terminal share is UNDERSTATED.")
print()


def decompose(fast, slow):
    r_rate = fast["rate"] / slow["rate"]
    r_vc = fast["h_height"] / slow["h_height"]
    flux_f = fast["rate"] / fast["h_height"]
    flux_s = slow["rate"] / slow["h_height"]
    r_flux = flux_f / flux_s
    share_vc = log(r_vc) / log(r_rate)
    print(f"  {fast['name']}  vs  {slow['name']}")
    print(f"    elongation ratio        {r_rate:8.2f}x")
    print(f"    terminal cell height    {r_vc:8.2f}x")
    print(f"    flux (cells/day)        {r_flux:8.2f}x   "
          f"({flux_f:.1f} vs {flux_s:.1f} cells/day)")
    print(f"    check  flux x v_c =     {r_flux*r_vc:8.2f}x  (vs {r_rate:.2f})")
    print(f"    LOG SHARE: terminal domain {100*share_vc:5.1f}%   "
          f"flux {100*(1-share_vc):5.1f}%")
    print()
    return share_vc


shares = []
shares.append(decompose(MC3, TIBIA))
shares.append(decompose(MC4, TIBIA))
shares.append(decompose(MC3, MT3))
shares.append(decompose(TIBIA, MT3))

line("=")
print("STEP 3  --  THE RESULT AGAINST THE ATLAS'S OWN VARIANCE DECOMPOSITIONS")
line()
print("  R423  mouse femur vs metacarpal        88% AMPLIFICATION, 12% cell size")
print("  R449  Longshanks selection             moved resting + proliferative")
print("                                         zones only; NO hypertrophic")
print("                                         parameter moved at all")
print("  R455  axial vs appendicular            80-95% CELL PRODUCTION")
print("  R470  Vanky bm/bm dwarf                58% flux, 22% v_d")
print("  thorngren1981 rabbit/rat/man           terminal cell size near-invariant")
print()
print(f"  THIS ROUND, one bat, four of its own bones:")
for nm, s in zip(["MC3 vs tibia", "MC4 vs tibia", "MC3 vs MT3", "tibia vs MT3"],
                 shares):
    print(f"    {nm:<16} terminal domain carries {100*s:5.1f}%")
print()
print("  The bat metacarpal is a wing element under selection for length.")
print("  The variance decompositions measure what varies WITHIN normal")
print("  mammalian design; a canalised term has little standing variance,")
print("  so every such decomposition scores it low.  That is a statement")
print("  about standing variation, NOT about what a perturbation outside")
print("  the normal range can do.  R469's gain-only-lever logic, applied")
print("  to a TERM instead of a gene.")
print()

line("=")
print("STEP 4  --  AND THE BAT DOES IT BY SHAPE, NOT BY VOLUME ALONE")
line()
print("  Verbatim from farnum2007 '4' (Cells Tissues Organs 2008;187:48-58):")
print("    terminal hypertrophic axial ratio (height/width)")
print("      bat metacarpal digit 3        ~ 2.0")
print("      bat pes digit 3               ~ 0.55")
print("      mouse, ALL FOUR plates        < 1.0")
print("    authors' phrase: 'extreme shape modulation in the direction of")
print("    growth of chondrocytes in the bat MC'")
print()
print("  Ladder assembled across the atlas:")
print("      mouse manus + pes             < 1.0        farnum2007 '4'")
print("      rat, 4 plates x 2 ages          0.80-1.20  breur1997 (R470)")
print("      bat pes                         0.55       farnum2007 '4'")
print("      bat metacarpal                  2.0        farnum2007 '4'")
print()
print("  A cylinder check on the bat MC digit 3: h=54.5 um, V=33,900 um3")
w = (33900.0 / (54.5 * 3.14159265)) ** 0.5 * 2
print(f"      implied width = {w:.1f} um  ->  axial ratio {54.5/w:.2f}")
print("      consistent with the stated ~2.0 (cylinder is an approximation).")
print()
print("  R454's arithmetic required only 2.47:1 LINEAR anisotropy to")
print("  produce the observed x4 height / x10 volume hypertrophy.")
print("  The bat metacarpal reaches an ABSOLUTE terminal axial ratio of 2.0")
print("  where every rodent plate ever measured sits at or below ~1.2.")
line("=")
