#!/usr/bin/env python3
"""
THE EXPLANT REACTIVATION LEDGER - two human growth-plate organ-culture papers,
read against each other and against their own axes.

WHY THIS TOOL EXISTS
--------------------
Round 200 ended at an unrun experiment: at the TISSUE level the human plate is
still present when growth stops (herrmann2002, open epiphyses at 27), but
whether the CELLS in it retain divisional capacity had never been tested.

Two papers already held in this atlas test exactly that, in human tissue, and
neither was read for it:

  avijgan2026  intact human growth plate biopsies, 17 days of ex vivo culture,
               three sequential thymidine analogues, Tanner 2-4 donors
  chu2026      1-mm human growth plate slices, 2 months of ex vivo culture,
               vehicle versus growth hormone, EdU endpoint

BOTH CARRY A NUMBER THE TEXT DOES NOT EMPHASISE, AND IN BOTH CASES THE NUMBER
CHANGES THE CONCLUSION. This tool does the arithmetic that separates what the
figures can support from what they cannot.

EVERY INPUT IS EITHER AUTHOR-STATED OR READ FROM A CALIBRATED HIGH-DPI RENDER
OF THE PUBLISHED FIGURE, AND WHICH IS WHICH IS MARKED ON EVERY LINE.
"""
import math

# ============================================================================
# PART 1 - avijgan2026 / avijgan2025 preprint: the ex vivo labelling timeline
# ============================================================================
# AUTHOR-STATED, preprint methods "Triple labelling of human growth plate
# biopsies with thymidine analogues". Human slices, 24-well, 2 ml DMEM/F12 +
# 50 ug/ml ascorbate + 0.2% BSA + 50 ug/ml gentamicin. SERUM-FREE.
PROTOCOL = [
    ("EdU",  "day 1, overnight",                 1,  2,  0.7),
    ("IdU",  "days 3 and 6",                     3,  8,  5.0),
    ("CldU", "days 9, 11, 13 and 15",            9, 17,  8.0),
]
# columns: analogue, dosing days, first day present, day removed/fixed,
#          EFFECTIVE CONTINUOUS EXPOSURE IN DAYS (derived: medium was rinsed
#          on days 2 and 8, explants fixed day 17)

# AUTHOR-STATED, Fig 2G legend of the preprint:
#   pair-wise matching sample ANOVA + Tukey post-hoc
#   n = 646 cells RZ, 1227 PZ, 505 HZ, FROM 3 PATIENTS
AVIJGAN_N_CELLS = {"RZ": 646, "PZ": 1227, "HZ": 505}
AVIJGAN_N_PATIENTS = 3
AVIJGAN_P = {"EdU": "< 0.05", "IdU": "0.0989", "CldU": "< 0.001"}

# READ FROM FIGURE. Published Fig. 2f rendered at 900 dpi and calibrated
# against the printed axis ticks. Three dots per violin = three donors.
# THESE ARE value_unverified: the paper prints no numeric medians for 2f.
FIG2F = {
    "EdU":  {"RZ": [14.9, 6.6, 0.8],  "PZ": [75.4, 48.4, 24.2], "HZ": [29.8, 22.2, 1.4]},
    "IdU":  {"RZ": [77.0, 50.0, 0.0], "PZ": [41.5, 2.3, 1.0],   "HZ": [19.0, 0.0, 0.0]},
    "CldU": {"RZ": [68.9, 51.8, 45.2], "PZ": [36.9, 19.4, 9.7], "HZ": [24.8, 7.8, 0.0]},
}

# AUTHOR-STATED, preprint Fig 2H/2I legend, published Fig 2g.
# poly(A) signal intensity per nucleus, as a percentage of maximum. MEDIANS.
# Mann-Whitney. Cultured n = 1194 RZ, 1454 PZ, 1053 HZ cells from 3 patients.
POLYA = {
    "RZ": (26.2469, 46.5278),
    "PZ": (62.7071, 69.2647),
    "HZ": (81.2138, 69.5188),
}

# ============================================================================
# PART 2 - chu2026: GH on the human explant, 2 months
# ============================================================================
# AUTHOR-STATED: EdU+/DAPI+ %, seven vehicle and six GH donors, each the
# average of two to four explants. ONE-WAY ANOVA WITH TUKEY ACROSS ALL FOUR
# GROUPS. Reported P = 0.79 (resting zone) and P = 0.013 (proliferative zone).
CHU_P_REPORTED = {"RZ": 0.79, "PZ": 0.013}
# READ FROM FIGURE. Fig 5L rendered at 1400 dpi, calibrated on the 0/2/4/6/8
# ticks. Per-donor dots. value_unverified.
CHU = {
    "RZ": {"veh": [2.70, 0.25, 0.14, 0.06, 0.02, 0.00, 0.00],
           "gh":  [3.23, 2.67, 0.78, 0.51, 0.43, 0.00]},
    "PZ": {"veh": [3.23, 2.32, 1.65, 0.90, 0.54, 0.00, 0.00],
           "gh":  [6.57, 5.42, 4.30, 2.97, 2.58, 1.43]},
}


def mean(v):
    return sum(v) / len(v)


def sd(v):
    m = mean(v)
    return math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1))


def welch(a, b):
    ma, mb = mean(a), mean(b)
    va, vb = sd(a) ** 2, sd(b) ** 2
    se = math.sqrt(va / len(a) + vb / len(b))
    t = (mb - ma) / se
    df = (va / len(a) + vb / len(b)) ** 2 / (
        (va / len(a)) ** 2 / (len(a) - 1) + (vb / len(b)) ** 2 / (len(b) - 1))
    return t, df, se


def t_to_p(t, df):
    """Two-sided p from Student t. scipy if present, else a normal fallback."""
    try:
        from scipy import stats
        return 2 * (1 - stats.t.cdf(abs(t), df)), "exact"
    except Exception:
        return 2 * (1 - 0.5 * (1 + math.erf(abs(t) / math.sqrt(2)))), "normal approx"


def rule(c="="):
    print(c * 86)


def main():
    rule()
    print("PART 1  avijgan2026 - WHAT Fig 2f CAN AND CANNOT SUPPORT")
    rule()
    print("\nThe published text says only that IdU and CldU 'were present in RZ cells'.")
    print("The figure says something much stronger and something much weaker, and it")
    print("matters which is which.\n")

    print("[1a] THE EXPOSURE WINDOWS ARE NOT EQUAL, AND NOBODY NORMALISES FOR IT")
    print(f"    {'analogue':<6} {'dosing':<24} {'present':<12} {'exposure':>9}")
    for name, dosing, d0, d1, expo in PROTOCOL:
        print(f"    {name:<6} {dosing:<24} {'day '+str(d0)+'-'+str(d1):<12} {expo:>6.1f} d")
    print("    A cumulative label given for 8 days will mark more cells than the same")
    print("    label given for 16 hours EVEN IF NOTHING CHANGED. The panel is drawn as")
    print("    though the three are comparable. THEY ARE NOT.")

    print("\n[1b] PER-DONOR VALUES READ FROM THE 900 dpi RENDER, AND THE RATE THEY IMPLY")
    print(f"    {'zone':<5} {'analogue':<6} {'donors':<22} {'mean %':>7} {'per day':>9}")
    rates = {}
    for name, _, _, _, expo in PROTOCOL:
        for z in ("RZ", "PZ", "HZ"):
            v = FIG2F[name][z]
            m = mean(v)
            rates[(z, name)] = m / expo
            print(f"    {z:<5} {name:<6} {str([round(x,1) for x in v]):<22}"
                  f" {m:>7.1f} {m/expo:>8.1f}%")

    print("\n[1c] THE RESULT THAT KILLS THE SIMPLE READING")
    for z in ("RZ", "PZ", "HZ"):
        r0, r1 = rates[(z, "EdU")], rates[(z, "CldU")]
        print(f"    {z}: {r0:6.1f} %/day at day 0-1  ->  {r1:5.1f} %/day at day 9-17"
              f"   ({r1/r0 if r0 else float('nan'):.2f}x)")
    print("    THE RESTING ZONE'S LABELLING RATE PER DAY DOES NOT RISE. What happens")
    print("    is that THE PROLIFERATIVE ZONE COLLAPSES. The apparent 'RZ overtakes PZ'")
    print("    in the CldU panel is produced by PZ shutdown plus an 11x longer exposure")
    print("    window, not by resting-zone recruitment.")

    print("\n[1d] AND THE AXIS ITSELF FORBIDS ABSOLUTE ARITHMETIC")
    print("    The printed y-axes run to 150% and down to -100%. A raw fraction of")
    print("    labelled cells cannot exceed 100 or fall below 0. The quantity plotted")
    print("    is therefore NORMALISED OR BACKGROUND-CORRECTED, not a labelling index.")
    print("    Everything in [1b] and [1c] is therefore a RATIO ARGUMENT ONLY - it is")
    print("    valid for comparing zones and timepoints on one axis, and INVALID as a")
    print("    statement about what fraction of resting-zone cells divided.")
    print("    THE HONEST BOUND: Fig 2f establishes a paired SIGN FLIP - RZ below PZ")
    print(f"    at day 0-1 (P {AVIJGAN_P['EdU']}) and RZ above PZ at day 9-17"
          f" (P {AVIJGAN_P['CldU']}),")
    print(f"    with the intermediate window not significant (P = {AVIJGAN_P['IdU']}).")
    print(f"    n = {AVIJGAN_N_CELLS} cells from {AVIJGAN_N_PATIENTS} patients.")
    print("    IT DOES NOT ESTABLISH A RE-ENTRY FRACTION.")

    print("\n[1e] Fig 2g IS ON AN INTERPRETABLE SCALE AND IT SURVIVES THE OBJECTION")
    print("    poly(A) per nucleus, MEDIANS, author-stated, as a percentage of maximum:")
    print(f"    {'zone':<5} {'uncultured':>11} {'cultured':>10} {'delta':>8} {'relative':>10}")
    for z, (u, c) in POLYA.items():
        print(f"    {z:<5} {u:>11.2f} {c:>10.2f} {c-u:>+8.2f} {100*(c-u)/u:>+9.1f}%")
    print("    THE GAIN IS SPECIFIC TO THE RESTING ZONE. The PZ moves +10%, the HZ")
    print("    FALLS 14% - so this is not a global culture artefact lifting every")
    print("    nucleus, and it cannot be produced by proliferative-zone exhaustion.")
    print("    A compartment defined by LOW transcriptional output nearly doubles it")
    print("    once the tissue is removed from the body. THAT is the reactivation")
    print("    result, and it rests on Fig 2g rather than on Fig 2f.")

    print("\n[1f] THE PROLONGED-G1 ALTERNATIVE THE AUTHORS COULD NOT EXCLUDE")
    print("    They write that they cannot exclude a prolonged G1 rather than true G0.")
    print("    FOR THIS ATLAS THE DISTINCTION DOES NOT CHANGE THE ANSWER. Under either")
    print("    reading the same thing is true: the compartment's output is set by its")
    print("    position in the body and rises when that position is removed. Arrest")
    print("    versus very slow cycling is a question about the mechanism of the")
    print("    ceiling, not about whether the ceiling is imposed. IT IS IMPOSED.")

    rule()
    print("PART 2  chu2026 - THE GH NULL IN THE RESTING ZONE IS NOT A NULL")
    rule()
    print("\n2 months of culture, EdU+/DAPI+ per cent, 7 vehicle and 6 GH donors,")
    print("each donor the average of 2-4 explants. Author-stated test: ONE-WAY ANOVA")
    print("WITH TUKEY ACROSS ALL FOUR GROUPS.\n")
    print(f"    {'zone':<5} {'veh mean':>9} {'GH mean':>8} {'fold':>6} "
          f"{'Tukey P':>8} {'unadj p':>9} {'MDD':>7} {'MD fold':>8}")
    for z in ("RZ", "PZ"):
        veh, gh = CHU[z]["veh"], CHU[z]["gh"]
        mv, mg = mean(veh), mean(gh)
        t, df, se = welch(veh, gh)
        p, mode = t_to_p(t, df)
        # minimum detectable difference, 80% power, alpha 0.05 two-sided
        sp = math.sqrt(((len(veh)-1)*sd(veh)**2 + (len(gh)-1)*sd(gh)**2)
                       / (len(veh)+len(gh)-2))
        mdd = 2.80 * sp * math.sqrt(1/len(veh) + 1/len(gh))
        print(f"    {z:<5} {mv:>9.3f} {mg:>8.3f} {mg/mv:>5.2f}x "
              f"{CHU_P_REPORTED[z]:>8.3f} {p:>9.3f} {mdd:>7.2f} {1+mdd/mv:>7.2f}x")
    print(f"    (unadjusted p by Welch t on the reconstructed per-donor values, {mode})")

    print("\n[2a] WHAT THAT TABLE SAYS")
    veh, gh = CHU["RZ"]["veh"], CHU["RZ"]["gh"]
    mv, mg = mean(veh), mean(gh)
    sp = math.sqrt(((len(veh)-1)*sd(veh)**2 + (len(gh)-1)*sd(gh)**2)
                   / (len(veh)+len(gh)-2))
    mdd = 2.80 * sp * math.sqrt(1/len(veh) + 1/len(gh))
    print(f"    The resting-zone point estimate is {mg/mv:.1f}x, IN THE SAME DIRECTION")
    print(f"    as the proliferative zone. The study could only have detected a")
    print(f"    {1+mdd/mv:.1f}x rise at 80% power. IT COULD NOT HAVE DETECTED THE EFFECT")
    print("    IT OBSERVED.")
    print("    P = 0.79 is a Tukey-corrected figure across four groups; the unadjusted")
    print("    two-sample comparison on the same points is around p = 0.2.")
    print("    THIS IS AN UNINFORMATIVE NULL, NOT EVIDENCE OF ABSENCE.")

    print("\n[2b] AND THE SIGNALLING DATA POINT THE OTHER WAY")
    print("    chu2026 measured where GH signal actually lands: phospho-STAT5 rose")
    print("    PREDOMINANTLY IN THE RESTING ZONE, P = 0.034, on short-term treatment.")
    print("    So the receptor arm is engaged in the RZ and the proliferative readout")
    print("    in the RZ is underpowered. Any claim that GH bypasses the human resting")
    print("    zone is unsupported by this paper.")

    print("\n[2c] WHAT chu2026 DOES ESTABLISH, WHICH IS STILL USEFUL")
    print("    (i) the human plate survives 2 months ex vivo with intact histology and")
    print("        Safranin O proteoglycan, BECAUSE it is avascular and diffusion-fed;")
    print("    (ii) BONE DOES NOT EXPAND ex vivo - the authors' own reading is that")
    print("        vascularisation is dispensable for chondrogenesis and essential for")
    print("        ossification;")
    print("    (iii) GH raised PZ proliferation 3.2x, P = 0.013, and produced a")
    print("        measurable expansion of the cartilage - BUT NOT IN EVERY DONOR.")

    rule()
    print("PART 3  THE COST OF REACTIVATION, WHICH ONLY APPEARS WHEN THE TWO PAPERS")
    print("        ARE READ TOGETHER")
    rule()
    print("\n    avijgan2026 : culture RAISES resting-zone transcriptional output 77%")
    print("    chu2026     : culture DESTROYS the root population's identity -")
    print("                  cluster GP1 is effectively lost, CYTL1 falling from 175")
    print("                  to 4 reads per positive cell, IGF1 absent, and CYTL1 and")
    print("                  RAMP3 begin appearing in the same cells and in the")
    print("                  hypertrophic layer where they do not belong.")
    print("\n    THESE ARE THE SAME EVENT DESCRIBED FROM TWO SIDES. The niche signal is")
    print("    withdrawn; the cells wake up; the identity that made them a reserve goes")
    print("    with it. Explant reactivation is not a clean pool expansion.")
    print("\n    AND THE MOUSE ALREADY SHOWED THIS PHENOTYPE UNDER A DEFINED LESION.")
    print("    newton2019, Tsc1 ablation (constitutive mTORC1) in the resting zone:")
    print("    CD73 zone height up (P = 0.0025), clone size up (P = 0.0342), EdU+")
    print("    epiphyseal stem cells 24.7 -> 62.4 (P = 0.014), PAR3 shifted toward")
    print("    symmetric division - and 'neither proliferation of chondroprogenitors")
    print("    nor their recruitment into the proliferative layer changed detectably',")
    print("    with a DISORDERED resting zone expressing NO ColX and NO Ihh.")
    print("\n    THE EXPLANT PHENOTYPE AND THE Tsc1 PHENOTYPE ARE THE SAME PHENOTYPE:")
    print("    the pool wakes, and it does not make columns.")

    rule()
    print("PART 4  THE RELEASE SIGNAL - WHAT EXPLANTING ACTUALLY REMOVES")
    rule()
    removed = [
        ("mechanical load", "removed", "cannot be excluded; no loaded-explant arm exists"),
        ("systemic hormones incl. oestrogen", "removed (serum-free medium)",
         "oestrogen withdrawal predicts SLOWER senescence, not faster re-entry, so it "
         "does not fit the 17-day timescale"),
        ("the vascular/SOC border signal", "removed or cut",
         "newton2019 shows the SOC BUILDS the niche, so removing it should SHRINK the "
         "pool, not wake it - argues against"),
        ("the intact paracrine field", "removed",
         "avijgan2026's own chondron-level heterogeneity in CHRDL2/SFRP5 is consistent "
         "with local antagonist control; UNTESTED"),
        ("diffusion limitation", "relieved (1-mm slice, 2 ml medium, both faces)",
         "the only removed input with a named downstream node: nutrient sufficiency is "
         "the canonical mTORC1 input"),
    ]
    print(f"\n    {'input':<36} {'status':<34}")
    for a, b, c in removed:
        print(f"    {a:<36} {b:<34}")
        print(f"        -> {c}")
    print("\n    rodgers2014 (mouse, Nature): mTORC1 is NECESSARY AND SUFFICIENT for")
    print("    quiescent stem cells to leave G0 for G(Alert), a primed state that is")
    print("    NOT yet division - cells enter the cycle faster once a second signal")
    print("    arrives. cMet is also required.")
    print("\n    G(Alert) IS THE MISSING TERM, AND IT RETROSPECTIVELY EXPLAINS TWO")
    print("    STANDING PUZZLES IN THIS ATLAS:")
    print("      newton2019  : mTORC1 on -> bigger pool, NO change in recruitment.")
    print("                    That is alerting without the second signal.")
    print("      trompet2024 : intra-articular SAG raised Pthrp-tdTomato+ cells from")
    print("                    65.5 to 139.8 per mm2 (n = 5, P = 0.017) ENTIRELY WITHIN")
    print("                    THE RESTING ZONE, with NO change in proliferation.")
    print("                    Same shape: pool without flux.")
    print("\n    THE PROGRAMME CONSEQUENCE, STATED PLAINLY: every pool-expanding")
    print("    intervention this atlas has found produces G(Alert) and stops there.")
    print("    THE ATLAS HAS NEVER IDENTIFIED THE SECOND SIGNAL. That, not pool size,")
    print("    is now the binding constraint on the reserve route.")
    rule()


if __name__ == "__main__":
    main()
