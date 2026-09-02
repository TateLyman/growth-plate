#!/usr/bin/env python3
"""
plate_transport_model.py - DOES EVADING NPR-C HELP THE PLATE MORE THAN THE VASCULATURE?

THE QUESTION THIS CLOSES, AND WHY A MODEL IS THE RIGHT INSTRUMENT
-----------------------------------------------------------------
g_l12_does_evading_npr3_help_the_plate_more_than_the_vasculature. Three candidate
compounds have died on the same trap: raising systemic exposure is what the
cardiovascular margin forbids, and a higher dose, an NPR2 allosteric modulator and
systemic clearance blockade all do exactly that. The dual-resistant CNP analogue
(the_compound_this_thread_needs) escapes ONLY IF removing a local sink raises
concentration MORE in the growth plate than in the vasculature.

That is not a biological question. It is a TRANSPORT question with a known answer form,
and it reduces to one dimensionless group.

  vasculature  = WELL MIXED. Concentration is set by plasma. Removing a local sink
                 changes essentially nothing.
  growth plate = AVASCULAR SLAB fed by diffusion from the epiphyseal and metaphyseal
                 faces, consuming ligand internally via NPR-C internalisation and
                 neprilysin proteolysis.

For a slab of half-thickness L, effective diffusivity D and first-order consumption k,
the steady-state profile is the classic reaction-diffusion result

    C(x)/C_surface = cosh(phi * x/L) / cosh(phi),      phi = L * sqrt(k/D)

phi is the THIELE MODULUS and it is the whole answer:

    phi << 1  reaction-limited. The plate equilibrates with plasma before consuming
              much. It behaves like the vasculature. REMOVING THE SINK BUYS NOTHING
              and the dual-resistant analogue is a dose increase in disguise.
    phi >> 1  diffusion-limited. Ligand is consumed before it penetrates. Interior
              concentration is exponentially depressed, and reducing k raises it
              steeply. THE ASYMMETRY IS REAL.

WHAT THIS SCRIPT IS AND IS NOT
------------------------------
IT IS NOT A MEASUREMENT AND IT CANNOT BECOME ONE. It is a sensitivity analysis over
parameters this atlas does not hold, run to find out WHICH parameter the answer hinges
on so that one measurement can settle it. Every number below is an assumption with a
stated basis, and the output is a map, not a value.

PARAMETER PROVENANCE, STATED BEFORE USE
---------------------------------------
L  half-thickness of the cartilage disc. The plate is fed from BOTH faces (the atlas
   holds that tracers enter from epiphyseal bone vasculature, metaphyseal bone
   vasculature and a perichondrial plexus), so the diffusion distance is the half
   thickness. NOT SOURCED TO A NUMBER IN THIS ATLAS - swept over 100 to 1000 um, which
   brackets published human physeal thicknesses of order a millimetre thinning with age.
D  effective diffusivity of a ~4 kDa peptide in physeal matrix. NOT SOURCED IN THIS
   ATLAS - g_l5 gaps explicitly record that no charged-solute diffusivity in PHYSEAL as
   opposed to articular matrix has been measured. Swept over 1e-7 to 1e-6 cm2/s, the
   range spanned by mid-size solutes in dense cartilage.
k  first-order local consumption. NOT MEASURED ANYWHERE. Upper-bounded by the whole-body
   elimination rate of vosoritide (plasma t1/2 about 28 min, ema_voxzogo_epar_2021),
   which must exceed local tissue consumption since it also contains renal and hepatic
   routes. Swept over t1/2_local of 10 min to 10 h.

THE ONE THING THE MODEL CANNOT DECIDE, AND IT MATTERS
-----------------------------------------------------
farnum2006's partition curve (3 kDa about 60 per cent of vascular, 10 kDa about 10 per
cent) is consistent with EITHER mechanism and the atlas cannot currently tell them apart:
  - STERIC EXCLUSION at entry gives a FLAT reduced concentration through the depth.
  - CONSUMPTION gives a U-SHAPED profile, depleted at the centre.
Those predict the same average and completely different answers to this question. The
discriminating observation is the DEPTH PROFILE, not the mean - which is what the
experiment proposed at the end of this docstring measures.

Usage:
  python3 atlas/tools/plate_transport_model.py
"""
from __future__ import annotations
import math

# ---- parameter grids (cm, s) --------------------------------------------------
L_um   = [100, 250, 500, 1000]                  # half-thickness, micrometres
D_cm2s = [1e-7, 3e-7, 1e-6]                     # effective diffusivity
T_half_min = [10, 30, 120, 600]                 # local consumption half-life, minutes

VOSORITIDE_PLASMA_T_HALF_MIN = 27.9             # ema_voxzogo_epar_2021, human 5-18y


def phi(L_cm: float, D: float, k: float) -> float:
    return L_cm * math.sqrt(k / D)


def centre_fraction(p: float) -> float:
    """C(centre)/C(surface) for a slab fed from both faces."""
    return 1.0 / math.cosh(p)


def mean_fraction(p: float) -> float:
    """Depth-averaged C/C_surface = tanh(phi)/phi."""
    return math.tanh(p) / p if p > 0 else 1.0


def main() -> int:
    print(__doc__.split("Usage:")[0])
    print("=" * 100)
    print("THIELE MODULUS AND STEADY-STATE DEPLETION ACROSS THE PLAUSIBLE PARAMETER SPACE")
    print("=" * 100)
    print(f"{'L(um)':>7}{'D(cm2/s)':>12}{'t1/2_loc':>10}{'phi':>8}{'C_cen/C_s':>11}{'C_mean/C_s':>12}   regime")
    rows = []
    for L in L_um:
        Lc = L * 1e-4
        for D in D_cm2s:
            for th in T_half_min:
                k = math.log(2) / (th * 60.0)
                p = phi(Lc, D, k)
                cc, cm = centre_fraction(p), mean_fraction(p)
                reg = ("well-mixed  -> NO asymmetry" if p < 0.5 else
                       "transitional" if p < 2.0 else
                       "diffusion-limited -> asymmetry REAL")
                rows.append((L, D, th, p, cc, cm))
                print(f"{L:>7}{D:>12.0e}{th:>10}{p:>8.2f}{cc:>11.3f}{cm:>12.3f}   {reg}")

    n = len(rows)
    wm = sum(1 for r in rows if r[3] < 0.5)
    tr = sum(1 for r in rows if 0.5 <= r[3] < 2.0)
    dl = sum(1 for r in rows if r[3] >= 2.0)
    print("\n" + "=" * 100)
    print(f"REGIME CENSUS over {n} parameter combinations:")
    print(f"  well-mixed (phi<0.5), asymmetry absent        : {wm:3d}  ({100*wm/n:.0f}%)")
    print(f"  transitional (0.5<=phi<2)                     : {tr:3d}  ({100*tr/n:.0f}%)")
    print(f"  diffusion-limited (phi>=2), asymmetry present : {dl:3d}  ({100*dl/n:.0f}%)")

    # ---- what does halving the sink buy, as a function of phi -----------------
    print("\n" + "=" * 100)
    print("THE ACTUAL QUESTION: what does REMOVING NPR-C-mediated consumption buy AT THE PLATE?")
    print("Modelled as reducing k by a factor f. The vasculature, being well mixed, gains")
    print("nothing locally - its concentration is set by plasma - so any gain here is the")
    print("therapeutic-index improvement a dose increase cannot buy.\n")
    print(f"{'phi_before':>11}{'f=2':>10}{'f=5':>10}{'f=10':>10}   (fold rise in CENTRE concentration)")
    for p0 in [0.25, 0.5, 1.0, 2.0, 3.0, 5.0]:
        out = f"{p0:>11.2f}"
        for f in (2.0, 5.0, 10.0):
            p1 = p0 / math.sqrt(f)
            out += f"{centre_fraction(p1)/centre_fraction(p0):>10.2f}"
        print(out)

    # ---- transient check: does the plate even reach steady state? -------------
    print("\n" + "=" * 100)
    print("SEPARATE AND POSSIBLY LARGER EFFECT - DOES THE PLATE EVER REACH STEADY STATE?")
    print("Diffusive equilibration time of a slab is about L^2/(2D). Compare it with the")
    print("plasma half-life of the agent: if equilibration is slower than the plasma pulse,")
    print("the plate never sees the peak concentration at all, and HALF-LIFE beats affinity.\n")
    print(f"{'L(um)':>7}{'D(cm2/s)':>12}{'tau_eq(min)':>14}   vs vosoritide plasma t1/2 = "
          f"{VOSORITIDE_PLASMA_T_HALF_MIN} min")
    for L in L_um:
        Lc = L * 1e-4
        for D in D_cm2s:
            tau = (Lc ** 2) / (2 * D) / 60.0
            flag = "PLATE NEVER EQUILIBRATES" if tau > VOSORITIDE_PLASMA_T_HALF_MIN else "equilibrates in time"
            print(f"{L:>7}{D:>12.0e}{tau:>14.1f}   {flag}")

    print("\n" + "=" * 100)
    print("WHAT WOULD SETTLE IT - one measurement, and it is a PROFILE not a mean.")
    print("""
  Infuse a labelled CNP analogue to steady plasma concentration, then image or section
  the plate and report concentration AS A FUNCTION OF DEPTH from the vascular face,
  normalised to simultaneous plasma.

    FLAT profile at reduced level   => steric exclusion. phi is small, the plate is
                                       well mixed, NPR-C evasion buys nothing locally,
                                       and the ligand branch of thread 3 should close.
    U-SHAPED profile, depleted at
    the centre                      => consumption-limited. Fit cosh(phi x/L)/cosh(phi)
                                       to recover phi directly, then read the expected
                                       gain straight off the table above.

  serrat2014 already images tracers in a live plate by multiphoton at a controlled depth
  50 um below the perichondrium, so the method exists and is in this atlas; what has
  never been done is to vary that depth systematically and report the profile.""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
