# Round 36 — the FGFRs are not one target, and the discriminator I designed does not discriminate

## The contradiction you asked me to look for exists, and it favours erdafitinib

I called erdafitinib's ~11-fold greater FGFR4 potency **"a pure liability with no growth-plate benefit."**
That was wrong, twice stated. `fgf19cart2025`:

> FGF19 signalling through **FGFR4** with β-klotho **impairs chondrocyte maturation** neonatally and
> **decreases growth plate thickness** in adolescent plates — by upregulating the β-catenin antagonists
> **SFRP1, WIF1, DKK2** and suppressing Wnt/β-catenin.

**FGFR4 restrains cartilage growth. Inhibiting it should be pro-growth.**

| | FGFR3 (pro-growth to inhibit) | FGFR4 (pro-growth to inhibit) |
|---|---|---|
| erdafitinib | 3.00 nM | **5.70 nM** |
| infigratinib | 10.00 nM | 61.00 nM |

**Erdafitinib has two pro-growth targets, not one**, and is the only clinically available FGFR inhibitor
reaching FGFR4 at achievable concentrations. TYRA-300's FGFR3-selectivity — which I recommended last
round — would *forgo* this.

### And the convergence is sharper than the correction

The antagonists FGF19/FGFR4 induces — **SFRP1, WIF1, DKK2** — are the same Wnt-antagonist axis `lui2018`
found separating **fast-senescing from slow-senescing bones** (phalanx-high Wif1 +2.08/+3.12, Dkk3
+2.51/+1.66). **FGFR4 inhibition would push a plate along the exact axis that distinguishes an
early-fusing bone from a late-fusing one.** The atlas held both facts and never connected them.

### The honest counter — the dosing order is wrong

Erdafitinib: FGFR1 **1.20** < FGFR3 **3.00** < FGFR4 **5.70** nM. As dose falls, **FGFR4 engagement is
lost first and FGFR1 last.** There is no dose giving FGFR3 + FGFR4 without maximal FGFR1. The selectivity
ordering is precisely backwards for dosing down.

## But FGFR1 engagement is dose-separable in practice — and erdafitinib has the biomarker

PROPEL3, oral infigratinib 0.25 mg/kg/day, n=74 vs 39:

- AHV **4.28 → 5.75 cm/yr** vs placebo 4.57 → 3.95; **LS mean difference +1.74 cm/yr (1.31–2.17), p<0.0001**
- **No accelerated progression of bone age**, no negative BMD change
- **"No evidence of FGFR1 or FGFR2 inhibition (no corneal or retinal adverse events)"**

**So the selectivity that matters is achieved by *dose*, not by molecule.** And that is the opening the
biochemistry seemed to close: **erdafitinib's hyperphosphatemia is a direct, same-day, on-target readout
of FGFR1 engagement.** It is the only FGFR inhibitor whose FGFR1 boundary can be titrated against a
real-time biomarker. **Dosing to just below the phosphate threshold is the specific untested proposal.**

Caveat that keeps it honest: given the ordering, a phosphate-guided dose may leave little FGFR3
occupancy. And absence of adverse events is standing in for absence of target engagement.

## The test I designed does not discriminate

Round 29 proposed Δheight ÷ Δbone-age as the separator between a yield lever and a velocity lever, and
named PROPEL3 as decisive. It arrived. **Infigratinib: no accelerated bone age. Vosoritide: bone-age
ratio unmoved. Both pass.**

**It is a necessary condition both candidates satisfy, not a test that separates them.** I presented it
as decisive for four rounds; that overstated it. Logged as CORR-040.

## The postmarketing series

`nadeaunguyen2026` (FDA, FAERS + literature to Dec 2024): **five** paediatric cases of erdafitinib
skeletal growth toxicity, all single-agent for CNS malignancy. Median age **13** (10–15), 4/5 male,
**median time to onset 137 days** (84–274). Lower-limb pain (3), difficulty walking (2). Confounders:
obesity (2), concomitant GH (1). **Permanently discontinued in all five; three required surgery.** The US
label now carries bone growth abnormalities including SCFE and accelerated growth under Pediatric Use.

The 137-day median onset is the useful number: **the effect appears within ~4–5 months**, which bounds
how long any trial or titration needs to run to see it.

## Updated verdict

| | erdafitinib | infigratinib / TYRA-300 |
|---|---|---|
| FGFR3 | 3.00 nM | 10.00 nM / selective |
| **FGFR4 (also pro-growth)** | **5.70 nM** | 61.00 nM / spared |
| FGFR1 liability | worst (1.20 nM) | dose-separable at 0.25 mg/kg |
| FGFR1 biomarker | **phosphate, same-day** | none needed |
| human growth data | 19.06 cm/yr (n=1); 5 tox cases | **+1.74 cm/yr, RCT n=74** |
| bone age | delayed (no baseline) | **not accelerated** |

**Erdafitinib is the more complete pharmacology — two pro-growth targets and a titratable liability.
Infigratinib is the more established result — a randomised trial with bone age.** They are not the same
kind of evidence, and the honest position is that the FGFR4 argument makes erdafitinib worth testing
rather than worth assuming.

## What I still need

1. **Any FGFR4 loss-of-function skeletal phenotype** — `Fgfr4`-null mouse bone length. The FGF19 paper is
   overexpression and organ culture; a knockout would confirm the direction. I could not find one.
2. **Erdafitinib growth-plate/cartilage concentrations** — the plate is avascular. Nobody has measured
   whether any of these drugs reach it.
3. **A pharmacological recruiter of the Gli1+/Pdgfra+ reservoir** — still the highest-value missing
   compound, still nothing found.
4. **β-klotho (KLB) expression in growth plate cartilage** — FGFR4 signalling required it in this paper.
   If KLB is absent from the plate, the FGFR4 argument weakens sharply. **This is the cheapest check that
   could kill the whole FGFR4 case, and I have not been able to settle it.**

Validator: 643 nodes, 1247 edges, 320 gaps, 1149 refs — 0 errors, 0 warnings.
