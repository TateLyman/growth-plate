#!/usr/bin/env python3
"""
ROUND 186 - ogawa2002 READ IN FULL, AND IT IS A BETTER PAPER THAN ITS ABSTRACT.

Rounds 184 and 185 judged this study on its abstract, which reports "growth plate thickness,
chondrocyte number, and LGR were increased". Two of those three are the quantities CORR-189 says
cannot be trusted, and round 185 downgraded the candidate partly on that basis.

THE FULL TEXT REPORTS THE FLUX QUANTITIES. Tables 1 and 2 give, for young AND adult animals:

    LGR  longitudinal growth rate, micrometres/day, by DOUBLE TETRACYCLINE LABEL
    CPR  cell production rate, cells/day, computed by the authors as
             CPR = LGR / height of the degenerative (terminal hypertrophic) cell

That is the Kember-Sissons construction, and it means terminal cell height is RECOVERABLE by
inversion: h_term = LGR / CPR. So the h_term-versus-flux split can be computed exactly, in both age
cohorts, from published means. Nothing here is digitised or inferred.

WHAT IT STILL CANNOT DO. CPR = amplification x pool-consumption rate. Separating those needs a
resting-zone cycle time, which ogawa2002 does not measure. So this settles h_term and leaves the
amplification-versus-pool question exactly where round 184 left it.

AND THE SECOND FINDING, WHICH CORRECTS ROUND 185. The abstract says the effects "were observed only
in young rats; not in adult rats", and round 185 called that age gate the most serious limitation
because no dose escalation fixes it. Table 2 shows the adult point estimates moving the SAME WAY by
a SIMILAR RELATIVE AMOUNT and simply failing to reach significance at n = 6.
"""

import math
from scipy import stats

# ---------------------------------------------------------------------------
# ogawa2002 Tables 1 and 2. Means +/- SD, n = 6 per group.
# hPTH(1-34) 80 ug/kg/day, 5 days a week, 3 weeks. Sprague-Dawley males.
# ---------------------------------------------------------------------------
N = 6
COHORTS = {
    "YOUNG (6 wk)": {
        "control": {"grp": "G II",   "lgr": (207.0, 11.4), "cpr": (10.4, 1.1)},
        "pth":     {"grp": "G III",  "lgr": (235.0, 18.8), "cpr": (12.0, 1.0)},
        "sig": "P<0.05 for both LGR and CPR vs control",
    },
    "ADULT (15 wk)": {
        "control": {"grp": "G VII",  "lgr": (74.2, 4.5),   "cpr": (3.5, 0.3)},
        "pth":     {"grp": "G VIII", "lgr": (81.7, 8.4),   "cpr": (3.8, 0.4)},
        "sig": "NOT significant for either",
    },
}


def cohens_d(m1, s1, m2, s2):
    sp = math.sqrt((s1 ** 2 + s2 ** 2) / 2.0)
    return (m2 - m1) / sp, sp


def power_two_sample(d, n, alpha=0.05):
    df = 2 * n - 2
    nc = d * math.sqrt(n / 2.0)
    crit = stats.t.ppf(1 - alpha / 2, df)
    return (1 - stats.nct.cdf(crit, df, nc)) + stats.nct.cdf(-crit, df, nc)


def n_for_power(d, target=0.80, alpha=0.05):
    for n in range(3, 500):
        if power_two_sample(d, n, alpha) >= target:
            return n
    return None


def banner(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78)


banner("STEP 1 - RECOVER TERMINAL CELL HEIGHT BY INVERTING THE AUTHORS' OWN CONSTRUCTION")
print("  CPR = LGR / h_term   (ogawa2002 Methods, citing Thorngren & Hansson 1973)")
print("  therefore h_term = LGR / CPR\n")
print(f"  {'cohort':14s} {'arm':10s} {'LGR um/d':>9s} {'CPR /d':>8s} {'h_term um':>10s}")
res = {}
for cname, c in COHORTS.items():
    res[cname] = {}
    for arm in ("control", "pth"):
        lgr, cpr = c[arm]["lgr"][0], c[arm]["cpr"][0]
        h = lgr / cpr
        res[cname][arm] = {"lgr": lgr, "cpr": cpr, "h": h}
        print(f"  {cname:14s} {arm:10s} {lgr:9.1f} {cpr:8.2f} {h:10.2f}")
print("""
  SANITY: 19.6-21.5 um for a rat terminal hypertrophic cell. hunziker1994 measured 19.5-29.8 um
  directly in rat proximal tibia by stereology. Independent study, independent method, same range.""")

banner("STEP 2 - THE DECOMPOSITION. Where does the growth-rate gain actually come from?")
print("  LGR_ratio = CPR_ratio x h_term_ratio   (exact by construction, no residual)\n")
print(f"  {'cohort':14s} {'LGR':>7s} {'= CPR':>8s} {'x h_term':>10s}   {'share of log effect: CPR / h_term'}")
for cname in COHORTS:
    a, b = res[cname]["control"], res[cname]["pth"]
    rl, rc, rh = b["lgr"] / a["lgr"], b["cpr"] / a["cpr"], b["h"] / a["h"]
    lc, lh = math.log(rc), math.log(rh)
    tot = abs(lc) + abs(lh)
    sgn = "(neg)" if lh < 0 else "     "
    print(f"  {cname:14s} {rl:7.3f} {rc:8.3f} {rh:10.3f}   {100*abs(lc)/tot:5.1f}% / {100*abs(lh)/tot:5.1f}% {sgn}"
          f"   [resid {rl - rc*rh:+.5f}]")
print("""
  TERMINAL CELL HEIGHT IS FLAT IN BOTH COHORTS - 0.98x in the young, 1.01x in the adult. The entire
  growth-rate gain is CELL PRODUCTION. That is the opposite signature to growth hormone, which took
  1.36x of its effect out of terminal cell height (hunziker1994, round 183).

  IT DOES NOT FOLLOW THAT THIS IS AMPLIFICATION. CPR = amplification x pool-consumption rate, and
  ogawa2002 measures no resting-zone kinetics. GH also raised CPR - 3.87-fold - and 97 per cent of
  that was the pool being spent faster. PTH could be doing either. What has been eliminated is the
  h_term explanation, which is one of three, and that is real progress but it is not the answer.""")

banner("STEP 3 - THE AGE GATE. Round 185 called this the most serious limitation. Was it?")
print(f"  {'cohort':14s} {'measure':6s} {'control':>16s} {'PTH':>16s} {'ratio':>7s} {'Cohen d':>9s} "
      f"{'power at n=6':>13s} {'n for 80%':>10s}")
for cname, c in COHORTS.items():
    for measure in ("lgr", "cpr"):
        m1, s1 = c["control"][measure]
        m2, s2 = c["pth"][measure]
        d, sp = cohens_d(m1, s1, m2, s2)
        pw = power_two_sample(abs(d), N)
        need = n_for_power(abs(d))
        print(f"  {cname:14s} {measure.upper():6s} {m1:8.1f}+/-{s1:<6.1f} {m2:8.1f}+/-{s2:<6.1f} "
              f"{m2/m1:7.3f} {d:9.2f} {pw:12.0%} {need:10d}")
print("""
  THE ADULT ARM IS NOT A NULL, IT IS AN UNDERPOWERED POSITIVE. The adult LGR effect is +10.1 per cent
  against +13.5 per cent in the young - a similar RELATIVE effect with a large standardised effect
  size - and the study had roughly a one-in-three chance of detecting it with six animals per group.

  Round 185 wrote that the age gate was worse than the dose gap "because no dose escalation fixes an
  age gate". That was wrong on this evidence. What the adult cohort shows is a smaller and noisier
  version of the same effect, not its absence. The authors' sentence "observed only in young rats"
  is accurate about the UNLOADING-PREVENTION arm and about zone thickness and cell number - and the
  full text says so explicitly - but Tables 1 and 2 show LGR and CPR moving the same way at both ages.

  THIS MATTERS BECAUSE THE SUBJECT IS LATE. A 15-week rat plate growing at 74 um/day, 36 per cent of
  the young rate, is the closer analogue to a human plate at bone age 16 than a 6-week one is.""")

banner("STEP 4 - WHAT WOULD IT BE WORTH IF THE RELATIVE EFFECT TRANSFERRED?")
for cname in COHORTS:
    a, b = res[cname]["control"], res[cname]["pth"]
    print(f"  {cname:14s} LGR ratio {b['lgr']/a['lgr']:.3f}")
print("""
  Applied to a human plate at bone age 16 growing 3-4 cm/year, a 10-13 per cent rate increase is
  +0.3 to +0.5 cm/year. Over the 1.5-2 years of growth such a subject plausibly has left, that is
  ROUGHLY HALF A CENTIMETRE TO ONE CENTIMETRE.

  STATE THAT PLAINLY RATHER THAN BURYING IT. Even taking the rat result at face value and assuming
  it transfers, this is a small intervention - and it is a small intervention at a dose whose human
  equivalent is about ten times the approved abaloparatide dose, on a schedule the round-185
  benchmark says is twenty times too frequent. The case for it is mechanistic interest and the
  absence of anything better, not the size of the prize.""")

banner("STEP 5 - WHICH MOLECULE DID THIS EXPERIMENT ACTUALLY USE?")
print("""
  SYNTHETIC HUMAN PTH(1-34). The Acknowledgments thank Asahi Chemical Industries for providing it.
  hPTH(1-34) IS TERIPARATIDE. It is not abaloparatide, which is a PTHrP(1-34) ANALOGUE.

  Round 184 recommended abaloparatide over teriparatide on a mechanistic argument - abaloparatide is
  the PTHrP analogue, and PTHrP rather than PTH is the growth plate's endogenous ligand. THAT
  PREFERENCE RUNS AGAINST THE ONLY WILD-TYPE GROWTH DATA THAT EXISTS, which is teriparatide's. The
  mechanistic argument is not thereby wrong, but it was stated without noting that it pointed away
  from the sole supporting experiment, and that should have been said.""")
