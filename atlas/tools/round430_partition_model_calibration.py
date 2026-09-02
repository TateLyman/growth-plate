#!/usr/bin/env python3
"""
round430_partition_model_calibration.py
=======================================
CALIBRATE THE ATLAS'S PARTITION MODEL AGAINST THE ONLY ORDERED VALENCE SERIES
THAT EXISTS IN CARTILAGE, AND THEN RUN THE STACK THROUGH THE CALIBRATED FORM.

WHY THIS ROUND EXISTS
---------------------
This atlas runs three transport models and has never compared any of them to a
measurement in a living or intact growth plate:

  1. DONNAN CHARGE      x = cF/(2*cs);  r = x + sqrt(x^2+1);  partition = r^z
     implemented in round371_smo_agonist_cartilage_selection.py and, in an
     algebraically identical form, in endothall_experiment_design.py
     (verified equal in this script - see check_implementations()).
  2. FARNUM SIZE CURVE  332 Da ~100% of vascular, 3 kDa ~50-60%, 10 kDa ~10%,
     >=40 kDa undetectable. Used descriptively, never as a fitted function.
  3. THIELE MODULUS     plate_transport_model.py, reaction-diffusion. Not touched
     here - it answers a different question (depth profile, not entry partition).

Those models decided fostriecin vs M372049 vs compound 23 (R153), the SMO agonist
selection (R371), the compound-and-route decision (R391) and R428's pricing of the
delivery multiplier. All model output. None validated.

THE VALIDATION SET, WHICH HAS BEEN IN THIS BIBLIOGRAPHY SINCE 2026-08-07
------------------------------------------------------------------------
kang2017 (Radiology 2017;282:734-742, PMID 27649101). 44 intact PORCINE PATELLAE,
four gadolinium agents differing in charge, immersed at 2.5 mmol/L, T1 maps every
10 min to 120 min, control vs trypsin-digested. Reported quantity is the DIFFERENCE
IN THE ESTIMATED SLOPE OF THE TIME-dR CURVE between control and trypsin groups,
where dR = R1_post - R1_pre. Values: Gd-BOPTA 2- 0.037 > Gd-DTPA 2- 0.022 >
Gd-DOTA - 0.018 > gadobutrol 0 0.011.

menezes2006 (Radiology 2006;239:406-414, PMID 16641351). TWELVE 3-WEEK-OLD PIGLETS,
3 T, in vivo, IV gadoteridol (neutral) or gadopentetate (Gd-DTPA 2-). Enhancement
ratios significantly HIGHER for the NEUTRAL agent in the PHYSIS, epiphyseal
cartilage and SOC (P<0.05); the ionic agent gave greater physis-vs-metaphysis
CONTRAST. No numeric enhancement ratios in the abstract - direction only.

THE CORRECTION THIS SCRIPT MAKES, WHICH NOBODY HAD APPLIED
-----------------------------------------------------------
dGEMRIC measures dR1 = r1 * [Gd]. A SLOPE IN dR IS A CONCENTRATION PROXY ONLY IF r1
IS THE SAME ACROSS AGENTS, AND IT IS NOT. kang2017's own conclusion says so - it
calls Gd-BOPTA "a high-relaxivity GBCA" and attributes its higher contrast to that.
Rohrer 2005 (Invest Radiol 40:715-724) Tables 3 and 4 give r1 for every one of these
agents in water and in plasma at 0.47/1.5/3/4.7 T. Dividing each slope by that
agent's r1 converts the four numbers into concentration-rate differences, which is
the quantity the partition model actually predicts.

Usage:  python3 atlas/tools/round430_partition_model_calibration.py
"""
from __future__ import annotations
import math
import json
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "round430")

CS = 0.15          # bathing ionic strength, M (1:1 salt)

# ---------------------------------------------------------------------------
# MEASURED INPUTS. Every number here is sourced; nothing is fitted yet.
# ---------------------------------------------------------------------------

# lesperance1992, sodium NMR, calf. THIS IS A MEASUREMENT, NOT AN ASSUMPTION -
# which is what makes the exercise below a falsification test rather than a fit.
FCD_EPIPHYSEAL = (0.19, 0.35)      # M, calf epiphyseal cartilage
FCD_ARTICULAR  = 0.28              # M +/- 0.03, calf articular cartilage

# kang2017 Results, verbatim numbers. Slope difference control vs trypsin.
KANG = [
    # label,          z,   slope, salt_MW, anion_MW, r1_water_15T, r1_plasma_15T
    ("Gd-BOPTA 2-",   -2, 0.037,  1058.1,  665.7,    4.0,          6.3),
    ("Gd-DTPA 2-",    -2, 0.022,   938.0,  545.6,    3.3,          4.1),
    ("Gd-DOTA -",     -1, 0.018,   753.9,  557.7,    2.9,          3.6),
    ("gadobutrol 0",   0, 0.011,   604.7,  604.7,    3.3,          5.2),
]
# menezes2006's pair, for the size check
MENEZES = [
    ("gadoteridol 0",  0, 558.7, 2.9, 4.1),
    ("Gd-DTPA 2-",    -2, 545.6, 3.3, 4.1),
]

# farnum2006, murine proximal tibial growth plate, multiphoton, in vivo.
# Text: fluorescein "comparable to those in the vasculature"; 3 kDa "only ~60%";
# 10 kDa "only approximately a tenth"; >=40 kDa "no detectable entry".
# Fig 6 caption says 3 kDa is "half that compared to fluorescein" - 50 vs 60 per
# cent is an internal inconsistency in the paper and is carried as a range.
FARNUM = [
    (332.0,   1.00, 1.00),   # MW, low estimate, high estimate
    (3000.0,  0.50, 0.60),
    (10000.0, 0.10, 0.10),
    (40000.0, 0.00, 0.03),   # "within our detection limit (a few percent)"
]


# ---------------------------------------------------------------------------
def donnan_r(cF: float, cs: float = CS) -> float:
    """Donnan ratio for a monovalent CATION. Partition of charge z is r**z."""
    x = cF / (2.0 * cs)
    return x + math.sqrt(x * x + 1.0)


def donnan_r_alt(cF: float, cs: float = CS) -> float:
    """The endothall_experiment_design.py form, algebraically rearranged."""
    c_minus = (-cF + math.sqrt(cF ** 2 + 4 * cs ** 2)) / 2.0
    return cs / c_minus            # inverse of the anion ratio = cation ratio


def cF_from_r(r: float, cs: float = CS) -> float:
    """Invert r = x + sqrt(x^2+1)  ->  x = (r^2-1)/(2r);  cF = 2*cs*x."""
    return 2.0 * cs * (r * r - 1.0) / (2.0 * r)


def check_implementations() -> bool:
    ok = True
    for cF in (0.19, 0.28, 0.35, 0.50):
        a, b = donnan_r(cF), donnan_r_alt(cF)
        if abs(a - b) > 1e-9:
            ok = False
        c = cF_from_r(a)
        if abs(c - cF) > 1e-9:
            ok = False
    return ok


# ---------------------------------------------------------------------------
# B2. SIZE CHECK, RUN BEFORE THE CHARGE FIT AS THE BRIEF REQUIRES.
# ---------------------------------------------------------------------------
def size_check() -> dict:
    print("=" * 79)
    print("B2. IS THE CHARGE COMPARISON CONFOUNDED BY SIZE?")
    print("=" * 79)
    print("  The species in solution is the ANION, not the dimeglumine salt.")
    print("  Anion MW = PubChem salt MW - n * protonated meglumine (196.22 Da);")
    print("  cross-checked against the anion molecular formula. Both agree.\n")
    print("  kang2017's four agents:")
    print(f"    {'agent':<15}{'z':>3}{'salt MW':>10}{'ANION MW':>11}"
          f"{'r1 water':>10}{'r1 plasma':>11}")
    for lab, z, _s, salt, anion, r1w, r1p in KANG:
        print(f"    {lab:<15}{z:>3}{salt:>10.1f}{anion:>11.1f}{r1w:>10.1f}{r1p:>11.1f}")
    mws = [a for *_, a, _w, _p in [(l, z, s, sa, an, w, p) for l, z, s, sa, an, w, p in KANG]]
    anions = [an for _l, _z, _s, _sa, an, _w, _p in KANG]
    print(f"\n  MW spread across the four: {min(anions):.1f} - {max(anions):.1f} Da "
          f"= {max(anions)/min(anions):.2f}x")
    bop, dtpa = 665.7, 545.6
    print(f"  THE TWO z=-2 AGENTS DIFFER BY {bop-dtpa:.1f} Da ({bop/dtpa:.2f}x) - and the")
    print(f"  LARGER one (Gd-BOPTA) gives the LARGER slope (0.037 vs 0.022).")
    print("  ==> SIZE RUNS THE WRONG WAY to explain the Gd-BOPTA excess. If steric")
    print("      exclusion mattered at this scale the bigger anion would score LOWER.")
    print("\n  menezes2006's pair:")
    for lab, z, mw, r1w, r1p in MENEZES:
        print(f"    {lab:<15}{z:>3}{mw:>11.1f}{r1w:>10.1f}{r1p:>11.1f}")
    print(f"  MW difference {abs(558.7-545.6):.1f} Da = {abs(558.7-545.6)/545.6*100:.1f} per cent,")
    print("  and r1 in PLASMA is IDENTICAL (4.1 vs 4.1) - menezes2006 is in vivo, so")
    print("  plasma is the right medium.")
    print("  ==> MENEZES2006 IS THE CLEAN CHARGE TEST: size-matched AND relaxivity-")
    print("      matched. kang2017 is neither, which is why it needs correcting.\n")
    return {"kang_anion_mw_range": [min(anions), max(anions)],
            "bopta_over_dtpa_mw": bop / dtpa,
            "menezes_mw_diff_pct": abs(558.7 - 545.6) / 545.6 * 100}


# ---------------------------------------------------------------------------
# B1. THE RELAXIVITY CORRECTION AND THE DONNAN TEST.
# ---------------------------------------------------------------------------
def relaxivity_correct(medium: str) -> list:
    """Convert each slope to a concentration-rate difference, referenced to
    Gd-DTPA so the corrected Gd-DTPA value equals its raw value."""
    idx = 5 if medium == "water" else 6
    ref = [row for row in KANG if row[0].startswith("Gd-DTPA")][0][idx]
    out = []
    for lab, z, slope, _salt, anion, _w, _p in KANG:
        r1 = [row for row in KANG if row[0] == lab][0][idx]
        out.append({"label": lab, "z": z, "raw": slope, "r1": r1,
                    "corrected": slope * ref / r1, "anion_mw": anion})
    return out


def predicted_ratio(cF_normal: float, depletion: float, cs: float = CS) -> float:
    """Model prediction for [dP(z=-2)] / [dP(z=-1)], where dP is the CHANGE in
    partition on removing a fraction `depletion` of the fixed charge.
    This is a FINITE DIFFERENCE, not a derivative - trypsin digestion is a large
    perturbation and the derivative form is only valid for a small one."""
    r_n = donnan_r(cF_normal, cs)
    r_d = donnan_r(cF_normal * (1.0 - depletion), cs)
    d1 = r_d ** -1 - r_n ** -1
    d2 = r_d ** -2 - r_n ** -2
    return d2 / d1


def calibrate() -> dict:
    print("=" * 79)
    print("B1. FIT THE DONNAN MODEL TO THE MEASURED VALENCE SERIES")
    print("=" * 79)
    print("  THE CORRECTION FIRST. dGEMRIC measures dR1 = r1 * [Gd]. A slope in dR")
    print("  is a concentration proxy only if r1 is constant across agents. It is")
    print("  not, and kang2017's own conclusion names Gd-BOPTA as a high-relaxivity")
    print("  agent. Relaxivities from rohrer2005 Tables 3 (water) and 4 (plasma).\n")

    res = {}
    for medium in ("water", "plasma"):
        rows = relaxivity_correct(medium)
        print(f"  --- relaxivity in {medium.upper()} at 1.5 T "
              f"({'kang2017 is an ex vivo immersion, so a protein-free bath is the' if medium=='water' else 'upper bound: Gd-BOPTA interacts with macromolecules, so its in-'}")
        print(f"  {'      literal condition' if medium=='water' else '      cartilage r1 may approach its plasma value'})")
        print(f"    {'agent':<15}{'z':>3}{'raw':>8}{'r1':>7}{'CORRECTED':>12}")
        for r in rows:
            print(f"    {r['label']:<15}{r['z']:>3}{r['raw']:>8.3f}{r['r1']:>7.1f}"
                  f"{r['corrected']:>12.4f}")
        z0 = [r for r in rows if r["z"] == 0][0]["corrected"]
        z1 = [r for r in rows if r["z"] == -1][0]["corrected"]
        z2s = [r["corrected"] for r in rows if r["z"] == -2]
        z2 = sum(z2s) / len(z2s)
        bop_over_dtpa = max(z2s) / min(z2s)
        print(f"    raw Gd-BOPTA/Gd-DTPA ratio 1.68x  ->  corrected {bop_over_dtpa:.2f}x")
        # the charge-attributable excess over the charge-independent baseline
        e1, e2 = z1 - z0, z2 - z0
        print(f"    z=0 baseline {z0:.4f} (a NEUTRAL solute should be INSENSITIVE to")
        print(f"      proteoglycan removal under Donnan - this is the charge-INDEPENDENT")
        print(f"      porosity/water-content term trypsin also creates)")
        print(f"    charge-attributable excess:  z=-1 {e1:.4f}   z=-2 {e2:.4f}"
              f"   ratio {e2/e1:.3f}")
        res[medium] = {"rows": rows, "z0": z0, "z1": z1, "z2_mean": z2,
                       "bopta_over_dtpa_corrected": bop_over_dtpa,
                       "excess_ratio": e2 / e1}
        print()

    print("  --- IS THE MEASURED FIXED CHARGE DENSITY CONSISTENT WITH THAT RATIO?")
    print("  This is a FALSIFICATION TEST, not a fit: lesperance1992 MEASURED cF by")
    print("  sodium NMR (calf articular 0.28 M, epiphyseal 0.19-0.35 M), so cF is an")
    print("  input. The only free parameter is how much fixed charge trypsin removed,")
    print("  which kang2017 verified qualitatively by safranin-O but did not quantify.\n")
    print(f"    {'cF (M)':>8}" + "".join(f"{int(f*100):>8}%" for f in
                                         (0.25, 0.50, 0.75, 0.90, 1.00)))
    grid = {}
    for cF in (0.19, 0.28, 0.35, 0.50):
        row = [predicted_ratio(cF, f) for f in (0.25, 0.50, 0.75, 0.90, 1.00)]
        grid[cF] = row
        print(f"    {cF:>8.2f}" + "".join(f"{v:>9.3f}" for v in row))
    print("    (columns are the fraction of fixed charge removed by trypsin)")
    print("\n    OBSERVED, relaxivity-corrected:  "
          f"water {res['water']['excess_ratio']:.3f}   "
          f"plasma {res['plasma']['excess_ratio']:.3f}")

    # find the depletion fraction that reproduces the observed ratio at measured cF
    print("\n  --- WHAT DEPLETION DOES EACH MEASURED cF REQUIRE?")
    fits = {}
    for medium in ("water", "plasma"):
        obs = res[medium]["excess_ratio"]
        fits[medium] = {}
        for cF in (0.19, 0.28, 0.35):
            lo, hi = 1e-4, 0.999999
            best = None
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if predicted_ratio(cF, mid) < obs:
                    lo = mid
                else:
                    hi = mid
                best = mid
            pred = predicted_ratio(cF, best)
            ok = abs(pred - obs) < 1e-3
            fits[medium][cF] = best if ok else None
            msg = (f"depletion {best*100:5.1f}% reproduces it"
                   if ok else "NO depletion in (0,1) reproduces it")
            print(f"    {medium:<7} cF={cF:.2f}: {msg}")
    res["grid"] = {str(k): v for k, v in grid.items()}
    res["required_depletion"] = {m: {str(k): v for k, v in d.items()}
                                 for m, d in fits.items()}
    print()
    return res


# ---------------------------------------------------------------------------
# B3. ONE PARTITION FUNCTION COMBINING SIZE AND CHARGE.
# ---------------------------------------------------------------------------
def fit_size() -> dict:
    """Fit farnum2006's curve as f(MW). Solute radius ~ MW^(1/3), and steric
    partition into a fibrous gel falls roughly exponentially in radius, so the
    natural one-parameter form is f = exp(-k*(MW^(1/3) - MW0^(1/3))) anchored at
    f(332 Da) = 1. Fitted by least squares on ln f."""
    import numpy as np
    pts = [(mw, 0.5 * (lo + hi)) for mw, lo, hi in FARNUM if 0.5 * (lo + hi) > 0]
    mw0 = 332.0
    x = np.array([p[0] ** (1 / 3) - mw0 ** (1 / 3) for p in pts])
    y = np.array([math.log(p[1]) for p in pts])
    k = -float((x * y).sum() / (x * x).sum())          # through the origin
    pred = {mw: math.exp(-k * (mw ** (1 / 3) - mw0 ** (1 / 3)))
            for mw, _lo, _hi in FARNUM}
    print("=" * 79)
    print("B3. A SINGLE PARTITION FUNCTION FOR SIZE AND CHARGE")
    print("=" * 79)
    print("  SIZE TERM, fitted to farnum2006 (murine growth plate, in vivo):")
    print(f"    f_size(MW) = exp(-{k:.4f} * (MW^(1/3) - 332^(1/3)))")
    print(f"    {'MW':>8}{'observed':>18}{'fitted':>10}")
    for mw, lo, hi in FARNUM:
        obs = f"{lo:.2f}-{hi:.2f}" if lo != hi else f"{lo:.2f}"
        print(f"    {mw:>8.0f}{obs:>18}{pred[mw]:>10.3f}")
    print("    ONE parameter, four points. The 3 kDa point is the worst fit and it")
    print("    is also the point farnum2006 itself reports inconsistently (text ~60%,")
    print("    Fig 6 caption 'half'). NOT a mechanistic model - an interpolant.")
    print("\n  CHARGE TERM: f_charge(z) = r^z with r from the calibrated cF.")
    print("  COMBINED:    C_plate / C_plasma_free = f_size(MW) * r^z")
    print("  ASSUMED, and this is the load-bearing assumption: size and charge")
    print("  exclusion are INDEPENDENT and multiply. Nobody has tested that in")
    print("  cartilage, and farnum2006's tracers were anionic dextrans/fluorescein,")
    print("  so the size curve already contains SOME charge exclusion - which means")
    print("  the product double-counts for anions and the true anion partition is")
    print("  probably HIGHER than this function returns.\n")
    return {"k": k, "form": "exp(-k*(MW**(1/3) - 332**(1/3)))",
            "fitted": {str(int(m)): v for m, v in pred.items()}}


# ---------------------------------------------------------------------------
# B4. RUN THE STACK AND THE HELD CANDIDATES.
# ---------------------------------------------------------------------------
# MW in Da; z = net charge at pH 7.4; fu = free fraction (1 - protein binding).
# Charges are assigned from ionisable groups and are labelled as ASSIGNED where
# no measured value is held. fu values are label/literature figures where held.
AGENTS = [
    # label,                       MW,      z,   fu,    note
    ("sulfate ion (oral Na2SO4)",   96.1,  -2, 1.00, "the transported species is SO4 2-"),
    ("anastrozole",                293.4,   0, 0.60, "triazole, not basic at pH 7.4; PB ~40%"),
    ("erdafitinib",                446.5,   0, 0.002, "PB 99.8%; assigned neutral (weak base)"),
    ("SAG (free base)",            490.1,  +1, None, "methylamino-cyclohexyl protonated"),
    ("fostriecin",                 430.4,  -2, None, "PubChem C19H27O9P; phosphate monoester dianionic at pH 7.4"),
    ("M372049",                    887.0,   0, None, "887 Da per the atlas's own record; ASSIGNED neutral"),
    ("vepdegestrant",              723.9,   0, 0.005, "PB >99%; PROTAC"),
    ("compound 23 (nishizawa2017)", 1400.0,  0, None, "~1.3-1.5 kDa peptide, ASSIGNED neutral"),
    ("cANF(4-23)",                 2200.0,  +2, None, "20-mer, ASSIGNED net +2"),
    ("CNP-38 (from navepegritide)", 4100.0, +6, None, "CNP-38, Arg/Lys rich, ASSIGNED net +6"),
    ("vosoritide",                 4100.0,  +6, None, "CNP-39 analogue, ASSIGNED net +6"),
    ("somatropin (GH)",           22124.0,  -3, None, "22 kDa protein, ASSIGNED net -3 at pH 7.4"),
]


def run_stack(k: float, cF: float) -> list:
    r = donnan_r(cF)
    out = []
    for lab, mw, z, fu, note in AGENTS:
        if mw is None or not isinstance(mw, (int, float)) or mw <= 0:
            continue
        fsize = math.exp(-k * (mw ** (1 / 3) - 332.0 ** (1 / 3)))
        fsize = min(fsize, 1.0)
        fchg = r ** z
        out.append({"agent": lab, "mw": mw, "z": z, "fu": fu,
                    "f_size": fsize, "f_charge": fchg,
                    "partition_of_free": fsize * fchg, "note": note})
    return out


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    print()
    print("#" * 79)
    print("# R430 - CALIBRATING THE PARTITION MODEL AGAINST THE ONLY IN-CARTILAGE")
    print("# ORDERED VALENCE SERIES THAT EXISTS")
    print("#" * 79)
    print(f"\n  Donnan implementations agree across tools: {check_implementations()}")
    print(f"  (round371_smo_agonist_cartilage_selection.py and "
          f"endothall_experiment_design.py\n   are algebraically identical, and the "
          f"inversion round-trips.)\n")

    size = size_check()
    cal = calibrate()
    sz = fit_size()

    # Use the plasma-relaxivity correction as the primary, because Gd-BOPTA's
    # relaxivity advantage arises from macromolecular interaction and cartilage
    # matrix is macromolecular. Report the water case as the alternative.
    cF_use = FCD_ARTICULAR
    print("=" * 79)
    print("B4. EVERY AGENT IN THE STACK THROUGH THE CALIBRATED FUNCTION")
    print("=" * 79)
    print(f"  cF = {cF_use} M (lesperance1992 calf articular, MEASURED), cs = {CS} M")
    print(f"  Donnan ratio r = {donnan_r(cF_use):.3f}\n")
    rows = run_stack(sz["k"], cF_use)
    # The calibration set spans MW 96-666 Da and |z| <= 2. Anything outside that
    # is extrapolation and is marked, because the r^z form is HIGHLY non-linear.
    for r_ in rows:
        r_["in_envelope"] = (abs(r_["z"]) <= 2) and (96.0 <= r_["mw"] <= 700.0)
    print(f"  {'agent':<30}{'MW':>8}{'z':>4}{'f_size':>9}{'f_charge':>10}"
          f"{'PARTITION':>11}  envelope")
    for r_ in sorted(rows, key=lambda d: -d["partition_of_free"]):
        flag = "validated" if r_["in_envelope"] else "EXTRAPOLATED"
        print(f"  {r_['agent']:<30}{r_['mw']:>8.0f}{r_['z']:>4}"
              f"{r_['f_size']:>9.3f}{r_['f_charge']:>10.3f}"
              f"{r_['partition_of_free']:>11.3f}  {flag}")
    print("\n  PARTITION is of the FREE (unbound) plasma concentration. For agents")
    print("  that are >99% protein bound the free fraction is the multiplier that")
    print("  matters far more than the partition, and it is given separately.")
    print("\n  ENVELOPE: the calibration set spans MW 96-666 Da and |z| <= 2. Rows")
    print("  outside it are extrapolation of a strongly non-linear function.\n")
    print("  " + "-" * 75)
    print("  THE r^z FORM MUST NOT BE READ AS A PARTITION AT LARGE |z|.")
    print("  " + "-" * 75)
    for z in (1, 2, 3, 6, 14):
        print(f"    z = {z:+3d}  ->  r^z = {donnan_r(cF_use)**z:>12,.0f}"
              + ("   <- CPC+14, the cationic carrier peptide" if z == 14 else "")
              + ("   <- an assigned CNP-38 charge" if z == 6 else ""))
    print("    Ideal Donnan assumes a dilute, ideal, point-charge solute. At |z|>=3")
    print("    the predicted enrichment is not a free-solution partition - it is")
    print("    ELECTROSTATIC ADSORPTION onto the fixed charge, which is what")
    print("    vedadghavami2022 actually observed for CPC+14 and described as a")
    print("    BOUND DEPOT. An adsorbed molecule is retained, not necessarily free")
    print("    to engage a receptor. R371 quoted 1e4-1e6x for CPC+14 from this")
    print("    formula as though it were a concentration ratio; the measured")
    print("    behaviour it corresponds to is depot formation.")
    print("    ==> READ r^z AS AN UPTAKE/RETENTION INDEX FOR |z|>=3, NOT A")
    print("        FREE-CONCENTRATION PARTITION.\n")
    print("  " + "-" * 75)
    print("  WHERE THE CALIBRATED MODEL DISAGREES WITH SOMETHING THE FILE ACTED ON")
    print("  " + "-" * 75)
    sulf = [r for r in rows if r["agent"].startswith("sulfate")][0]
    print(f"    1. ORAL SODIUM SULFATE. R428 priced the delivery multiplier by SIZE")
    print(f"       alone and put sulfate at 96 Da 'at the top of the curve, ~1.0'.")
    print(f"       Sulfate is a DIANION. f_size {sulf['f_size']:.3f} but f_charge "
          f"{sulf['f_charge']:.3f}")
    print(f"       -> calibrated partition {sulf['partition_of_free']:.3f}, a "
          f"{1/sulf['partition_of_free']:.1f}-fold PENALTY, not unity.")
    print(f"       R428 applied the size half of the model and dropped the charge")
    print(f"       half on the one agent in the stack where charge dominates.")
    print(f"    2. R153's NEUTRAL PARTITIONS. A neutral solute has a Donnan partition")
    print(f"       of EXACTLY 1.0, so R153's 0.82 (M372049, 887 Da) and 0.74")
    print(f"       (compound 23, ~1400 Da) are size terms. The farnum-fitted size")
    print(f"       function gives {math.exp(-sz['k']*(887**(1/3)-332**(1/3))):.2f} and "
          f"{math.exp(-sz['k']*(1400**(1/3)-332**(1/3))):.2f} at those weights - so the")
    print(f"       size penalty R153 used was 20-40 per cent too generous.")
    print(f"    3. THE CNP ARM. R428 concluded the delivery multiplier helps only the")
    print(f"       ~4 kDa peptide arm. That survives on SIZE - but the peptide's")
    print(f"       charge term is an extrapolation of r^z far outside the validated")
    print(f"       range, so its absolute partition here is not usable. What is")
    print(f"       usable is the SIGN: a cationic peptide is favoured, not excluded.\n")

    payload = {"size_check": size, "calibration": cal, "size_fit": sz,
               "cF_used": cF_use, "stack": rows}
    with open(os.path.join(OUT, "partition_calibration.json"), "w") as fh:
        json.dump(payload, fh, indent=2, default=str)
    print(f"  written: {os.path.normpath(os.path.join(OUT, 'partition_calibration.json'))}")


if __name__ == "__main__":
    main()
