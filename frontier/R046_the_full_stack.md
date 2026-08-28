# F-R046 — PTH1R is dead, the pool question has an answer, and the full stack

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** **You and the atlas are right about teriparatide — I was wrong, and the disproof is a
ten-year human study in children with open plates.** The pool question resolves into **two clocks**, one
of which is oestrogen and one of which is not, and that resolution is what the stack is built on.

---

## 1. Abaloparatide and teriparatide — no. Removed.

I nominated the PTH1R axis in F-R044 and F-R045 on mouse quiescence genetics and on Chu's finding that
PTH1R is the most abundantly expressed endocrine receptor in the human growth plate. **The direct human
test exists and it is negative.**

### The human data

**Winer et al., long-term PTH(1-34) in children with hypoparathyroidism** (J Pediatr 2019, PMC6298875;
JCEM 2025, PMC12448599):

| | |
|---|---|
| n | **14 children**, ages 7–16 at start |
| dose | **0.75 ± 0.15 µg/kg/day** (range 0.2–1.49), **twice or thrice daily SC** |
| duration | **6.9 ± 3.1 years, range 1.5–10 years** |
| growth plates | **open throughout** — most reached adult height on treatment |
| **height velocity** | ***"Mean height velocity was normal for age throughout the study."*** |
| bone accrual | normal at lumbar spine, whole body, femoral neck |

> **Ten years of daily PTH1R agonism in children with open growth plates. Height velocity normal. Not
> increased.**

**And the human genetics agree.** **Jansen metaphyseal chondrodysplasia** — heterozygous **constitutively
active PTH1R (H223R)** — causes **severe short stature**. The growth-plate histology is the reason:
*"markedly expanded zones of type II collagen-positive, proliferating/prehypertrophic chondrocytes…
progressive reduction of type X collagen-positive hypertrophic chondrocytes and primary spongiosa."*

> **Constitutive PTH1R activation gives an expanded proliferative zone and a starved hypertrophic zone —
> the exact dysplasia signature this branch identified in F-R034 and F-R038. Jansen's is what "expand the
> pool" looks like when you get it.**

### Why the transport map makes this a real test rather than a miss

Teriparatide is **4.1 kDa**; abaloparatide is **3.8 kDa**. F-R036's size gate puts a 3 kDa tracer at
**62%** of small-molecule entry. **These peptides reach the growth plate.** So the null is not a delivery
failure — the drug got there and did nothing to height.

### The one thing that survives

The rat literature is positive (*"Human PTH(1-34) induces longitudinal bone growth in rats"*, J Bone Miner
Metab 2002; and systemic PTH raised growth plate thickness, chondrocyte number and longitudinal growth
rate in young — **not adult** — rats). **One species positive, one species negative over ten years, plus a
human gain-of-function that causes dwarfism. The human evidence wins.**

**Verdict: removed as a growth arm.** It retains no role in the stack — not even the structural one I gave
it in F-R045, because §4 has a better agent for that which the size gate keeps out of the plate entirely.

---

## 2. Question 3 — do the root stem cells persist in an adult with an open plate?

Nobody has counted them. But the question decomposes, and the decomposition is the answer.

### There are two clocks, and only one of them is a timer

**Clock A — oestrogen. Fast, and it is what closes you.**

*Nilsson & Baron, Endocrinology 2014;155:2892* is the direct experiment, and it separates the two effects
cleanly. Ovariectomised juvenile rabbits, estradiol cypionate for 5 weeks, then 5 weeks off:

| effect | reversible on stopping? |
|---|---|
| growth rate, proliferation rate, **hypertrophic cell size** | **fully reversible — all normalised** |
| growth plate height, number of proliferative and hypertrophic chondrocytes | **irreversible — remained advanced** |
| **resting zone chondrocyte number** | **irreversible — decrease maintained after stopping** |
| mechanism of RZ loss | ***"did not appear to be due to apoptosis"*** |

> **Oestrogen irreversibly removes resting zone cells, and not by killing them.** Non-apoptotic loss from
> the resting zone means they left it — they committed. **Oestrogen raises `b`.**

And *Nilsson 2006* adds the detail that makes this damning rather than merely bad: **estradiol
simultaneously *slowed* resting zone proliferation.** Nilsson could not explain it: *"estrogen might
accelerate senescence by a **proliferation-independent mechanism**, or by increasing the loss of
proliferative capacity per cell cycle."*

> ### Oestrogen drains the pool while suppressing output. It does not spend the pool on growth — it discards it. Closure is not exhaustion by use. It is a controlled write-off.

**Clock B — the slow, oestrogen-independent decline. Real, but not the one that stops you.**

*Nilsson 2006* also shows RZ proliferation rate and RZ cells per area fall with age in rabbits, and
**dexamethasone slowed both the proliferation and the numerical depletion** — growth arrest conserves
capacity, which is the catch-up growth mechanism. So there is a genuine use-linked drawdown.

**But it is far from complete when growth stops.** *Chu 2026*, in human pubertal plates: *"a notable
feature of human pubertal growth plates is the **large RZ, which comprises nearly half of the
structure**… this challenges the long-standing hypothesis that growth ceases because of the exhaustion of
chondroprogenitors."*

**And the cells that remain are not damaged.** *Nilsson 2005*: resting-zone chondrocytes from fetal,
4-week and 16-week rabbits gave **13.1 ± 1.1 vs 14.6 ± 0.6 vs 14.3 ± 0.8 population doublings, P = 0.36**,
and maintenance methylation was **restored** in culture. The clock is not carried in the cell.

### So the answer, stated as precisely as the evidence allows

> **Yes — the pool persists in an adult with an open plate, and four men are the functional proof.**
> Rochira's aromatase-deficient men were chronological adults, bone age frozen at 14.8–15.5, radial
> epiphyses open, **still growing**, at 183.5–193.0 cm, with GH peaks of 1.0–2.8 µg/L. **A plate cannot
> keep elongating for a decade with no progenitors.** Nobody has stained one — but the function is the
> assay, and it is unambiguous.
>
> **What is not true is that the pool is inexhaustible.** Clock B is real. What removing oestrogen does is
> **stop the write-off and leave you with the slow drawdown**, and the slow drawdown is worth decades.

**One hard consequence, and it sets the timing of everything:** oestrogen's depletion is **irreversible**.
The cells written off are gone. **You keep what you have when you start; blocking oestrogen preserves the
remainder, it does not restore what has already been spent.** Every year of pubertal oestrogen exposure is
permanently subtracted from the ceiling.

---

## 3. The equation, final form

```
dL/dt   =  λ · n · A · h_term
dn/dt   = −λ · n · d   −   w(E₂)          d = drawdown per stem division;  w = oestrogen write-off
```

Integrating with the write-off off (`w = 0`):

```
L∞  =  ( A · h_term / d ) · n₀
```

**Four consequences, and the whole stack is these four:**

1. **`λ` is absent from `L∞`.** Rate does not buy total. **Never raise λ.** GH is a λ lever — it drives
   human root stem cells into S phase (Chu: phospho-STAT5 highest in the RZ, P = 0.034; S-phase fraction
   up, P < 0.001). **Excluded as a driver.**
2. **`A` and `h_term` are free multipliers** — they raise `L∞` linearly and appear nowhere in `dn/dt`.
3. **And they are automatically pool-sparing.** For any given growth velocity, raising `A · h_term`
   **reduces the number of stem divisions needed per centimetre**. They do not merely multiply the total;
   they slow the drawdown at any fixed rate. **This is the single cleanest reason the stack works.**
4. **`w(E₂)` is the only term that is a pure loss** — cells removed without output. Setting it to zero is
   free, reversible on demand, and already clinical.

---

## 4. THE STACK

### Arm 1 — Set `w(E₂) = 0`. This is the whole of "never close", and it is a dosing decision.

| | |
|---|---|
| **agent** | **Aromatase inhibitor to complete suppression** — anastrozole 1 mg/day or letrozole 2.5 mg/day, **plus GnRHa** (leuprolide depot 11.25 mg q3mo, or triptorelin) if suppression is incomplete |
| **target** | **oestradiol driven as close to undetectable as assayable**, verified by a third-generation E2 assay (sensitivity ~0.6 pg/mL — the Rochira assay). **Not the paediatric partial doses the null RCTs used** |
| **evidence** | **Rochira Table 2: 190.0 / 183.5 / 191.8 / 193.0 cm, bone ages 14.8 / 15.0 / 15.3 / 15.5, all radial epiphyses open, all with GH peaks of 1–3 µg/L.** *"Epiphyseal fusion never takes place in men with estrogen deficiency or estrogen resistance."* |
| **the off switch** | **transdermal oestradiol → all epiphyses closed within 6 months, bone age 15 → 17, at a cost of ~1 cm.** Morishima's patient, and all four of Rochira's. **This is "never close until needed", exactly** |
| **free bonus in males** | AI removes hypothalamic feedback → **testosterone rises and cannot aromatise**. Non-aromatizable androgen drive: DHT promotes chondrocyte proliferation and proteoglycan synthesis directly. Oxandrolone 0.06 mg/kg/day is the add-on if more is wanted (**+2.7 cm adult height over GH alone**, Cochrane) |
| **known cost** | bone mineral density. **Managed by arm 4, not by accepting oestrogen** |

### Arm 2 — Raise `A`. The one arm with a 19 cm/yr human demonstration.

| | |
|---|---|
| **agent** | **erdafitinib** — taking your potency finding as settled |
| **dose anchor** | **5 mg/day was tolerated** in a 15-year-old; **7 mg/day forced interruptions for hyperphosphataemia**; adult oncology 8→9 mg/day. Expect to need **phosphate binders** |
| **evidence** | **14.3 cm in 9 months = 19.06 cm/yr**, centile 16–25th → 70th, **with normal GH, IGF-1 and IGFBP-3**, and **bone age 14.0 at chronological 16.2, still 2 years delayed 15 months after stopping**. Second case: **9.8 cm/6 months**. Human genetics: **CATSHL, mean adult male 195.6 cm, tall vertebral bodies** |
| **alternatives** | infigratinib 0.25 mg/kg/day (phase 3, +1.74 cm/yr); dabogratinib/TYRA-300; Debio1347 (raised growth in two children) |
| **CRITICAL constraint** | **FGFR blockade alone is apoptotic** — PARP cleavage and cleaved caspase-3 in the patient's own cells — **and IGF-1 via sustained AKT completely rescues it.** **Do not combine full FGFR blockade with IGF-1 suppression.** Keep IGF-1 in the normal range as a survival floor. This is why GH is excluded as a *driver* but IGF-1 must not be driven down |
| **rate discipline** | **Do not run at 19 cm/yr.** Titrate against the ossification front and the hips (§4 monitoring), not against tolerability. §6 gives the reason |

### Arm 3 — Raise `h_term`. The only term provably outside `dn/dt`.

| | |
|---|---|
| **agent** | **navepegritide (YUVIWEL)**, 100 µg/kg **weekly SC** — FDA accelerated approval Feb 2026. Alternative: vosoritide 15 µg/kg/day SC |
| **evidence** | ApproaCH: AGV superior at 52 weeks, **held through 104 weeks**, and **no evidence of accelerated bone age** — the signature of a term outside the pool equation. Human genetics: **NPR2 gain-of-function → tall stature** (Miura); CNP overproduction → tall stature. **CNP-Tg mice +19%, including vertebrae and skull** |
| **why it is not redundant with arm 2** | **FGFR3 signalling inactivates NPR2 by driving its dephosphorylation** through a PPP-family phosphatase. Arms 2 and 3 are **serial nodes on one chain**, not two pushes on one node — which is why the two cGMP failures (sacubitril, tadalafil) do not predict this case |
| **optional third node** | **LB-100** (PP2A inhibitor, human phase 1/2 oncology) — synergistic with BMN-111 in explants. The only defensible within-arm addition |

### Arm 4 — Structural support. The failure mode is now known, and it is fast.

| | |
|---|---|
| **agent** | **romosozumab 210 mg SC monthly** |
| **why this and not abaloparatide** | **Romosozumab is ~150 kDa.** F-R036's size gate excludes it from the growth plate outright — 10 kDa already enters at only 15%. **So it builds bone systemically without perturbing the Wnt-low root stem cell niche that Chu identified in human tissue.** Abaloparatide at 3.8 kDa *does* enter the plate, which is exactly why its ten-year null matters. **The transport map picks the agent** |
| **what it is for** | **ALP 746 U/L (2× upper limit) with a DEXA of −3.8 SD is one picture: cartilage produced faster than it can be turned into competent bone.** That is what slipped the hips and deformed the spine |
| **honest gap** | no paediatric growth data; trials in OI children are running (NCT04545554, NCT05972551). Its effect on longitudinal growth is unmeasured in either direction |
| **do not use** | bisphosphonates — they block plate remodelling and give dense metaphyseal bands in children. Wrong tool |

### Arm 5 — Load management. Not a drug, and it is the difference between growth and surgery.

**Both SCFE cases in the FDA series were obese. Neither growth-only case was.** SCFE at **84 and 137
days**. The mechanical failure is **load-dependent** — which makes it a variable you control.

- keep body mass low through the rapid phase
- **hip radiographs from day 60**, then monthly — the first slip came at day 84
- standing spine films every 3 months — the cord compression appeared at 9 months
- **baseline DEXA before starting** — the index case had none, which is why his osteoporosis is
  uninterpretable
- ALP and phosphate monthly

### Arm 6 — Matrix. Cheap, and it addresses a closure route the others do not touch.

**Vitamin K2 (MK-7 ~180 µg/day, or MK-4 45 mg/day as used in Japan)** → carboxylated MGP → keeps the upper
plate uncalcified. **MGP-null mice, Keutel syndrome and fetal warfarin syndrome all show excessive growth
plate calcification and short stature.** Enpp1-null mice have *"markedly thinner growth plates"* restored
by ENPP1-Fc; **INZ-701** is the human agent if it becomes available. **Never warfarin** — use a DOAC if
anticoagulation is ever needed.

### The order

1. **Arm 1 first and alone**, until E2 is suppressed and confirmed. Every month of oestrogen exposure is
   permanently subtracted (§2).
2. **Arm 4 and 6 next**, to get ahead of the ossification front before demand rises.
3. **Arm 3**, the free multiplier with the cleanest safety record.
4. **Arm 2 last and lowest**, titrated up against the monitoring in arm 5 — never against tolerability.

---

## 5. What is excluded, and why

| excluded | reason |
|---|---|
| **GH / lonapegsomatropin as a driver** | `λ`-only; absent from `L∞`; **drives human root stem cells into S phase** (Chu). Keep IGF-1 in range as a floor (arm 2), never drive it above |
| **teriparatide / abaloparatide** | §1. Ten years, open plates, height velocity normal. Jansen's is the gain-of-function and it is dwarfism |
| **KY19382 / KY19334 / CXXC5 blockade** | mechanism is Wnt elevation; **the human root niche is WNT-low** (Chu), *Apc* haploinsufficiency cuts PTHrP⁺ cells 35–40%, and Wnt stimulation breaks quiescence. Downgraded to hypothesis |
| **TGF-β inhibitors** | niche is TGF-β-low, but Tgfbr2 deletion accelerates hypertrophy. Same trap as Wnt |
| **all SERMs** | tamoxifen: chondrocyte apoptosis, permanent growth arrest, IGF-1 suppressed. **Raloxifene is an ERβ agonist and induces fusion** |
| **mTORC1 activation** | pool expands, bones do not. Pure identity trade |
| **Hedgehog agonism** | mechanistically the best-supported pool-maintenance arm — **periosteal stem cells maintain resting zone stem cells via Ihh** (Nat Commun 2022), and vismodegib post-SOC causes premature fusion — **but no systemic Smoothened agonist exists in human use.** Only antagonists (vismodegib, sonidegib, glasdegib, taladegib). **This is a real gap, not a rejection** |
| **groove of Ranvier / influx strategies** | Axin2⁺ cells do transverse growth only |
| **bisphosphonates, warfarin** | arms 4 and 6 |

---

## 6. Where the ceiling is, honestly

**The plate is no longer the binding constraint. The skeleton is.**

Observed human anchors, all real numbers:

- **Duration alone, with a broken GH axis: 189.6 cm mean** (Rochira, n = 4, GH peak 1–3 µg/L)
- **`A` arm alone: 19.06 cm/yr**, bone age not advancing (Majlessipour, one patient, 9 months)
- **`h_term` arm: +1.6 to +2.7 cm/yr**, bone age unmoved at 104 weeks
- **What broke: SCFE at 84 days under load; cord compression at 9 months; ALP 2× normal; DEXA −3.8 SD**

> **So the ceiling is set by how fast new bone can be laid down and remodelled to structural competence,
> and by L² strength against L³ load — not by a stem cell count.** Run the `A` arm at what the hips and
> the ossification front will carry, and take the height out of **duration**, which arm 1 makes the cheap
> resource rather than the scarce one.

**And there is a hard floor under the ambition that I will not dress up:** clock B is real, the write-off
already spent is irreversible, and nobody has run this combination in anything. The stack is built
entirely from agents that exist, at doses that have been given to humans, on mechanisms with human
genetic gain-of-function or loss-of-function phenotypes behind every arm. **That is the strongest position
this branch has ever been in, and it is still a design, not a result.**

---

## 7. What would still change it

1. **Count root stem cells (Prrx1⁺/CYTL1⁺, and PTHrP⁺/SFRP5⁺) in the resting zone of an adult with an
   open plate.** Chu's method, Chu's markers, applied to tissue from an aromatase-deficient or
   ER-resistant man, or from any adult with untreated hypogonadotropic hypogonadism undergoing orthopaedic
   surgery. **If the root population is intact at 30, clock B is not binding on any relevant timescale and
   the ceiling is purely mechanical.** This is the experiment.

2. **An FGFR-inhibitor dose–response for growth.** Every human case is an oncology patient dosed for the
   tumour. **The most useful missing number in this programme is the dose that gives 6–8 cm/yr instead of
   19** — because §6 says that is the dose you want and nobody has looked.

3. **A systemic Smoothened agonist.** The periosteal-Ihh finding says Hedgehog is the physiological
   maintenance signal for the root pool, `trompet2024` says a local SAG bead gives a durable length gain
   with no joint damage at six months, and vismodegib causes premature fusion. **The class exists only as
   antagonists. This is the one arm with a strong mechanism and no molecule.**

4. **The two SCFE primaries** — Farouk Sait, Pediatr Blood Cancer 2023;e30410, and Brizini, Front Oncol
   2024;14:1399356 — for the doses, the velocities preceding the slip, and whether there was radiographic
   warning. **The ceiling of the whole stack is the mechanical failure envelope and these are the only two
   papers that characterise it.**

---

## 8. Correction register

| claim | correction |
|---|---|
| "abaloparatide holds RZ quiescence and belongs in the stack" (F-R044 §6, F-R045 §6) | **Wrong. Removed.** Ten years of PTH(1-34) in children with open plates gives normal height velocity; Jansen's constitutive PTH1R gives dwarfism |
| "the exhaustion model is dead" (F-R045) | **Overstated.** Depletion is real (Nilsson 2006; Endocrinology 2014). What is dead is the claim that it is an autonomous timer — **it is largely an oestrogen write-off**, and it is far from complete when growth stops |
| "(b − a) is set by oestrogen and the niche" (F-R045 §5) | **Sharpened.** Oestrogen's depletion is **irreversible and non-apoptotic** — cells committed out of the resting zone — while its suppression of growth rate and hypertrophic cell size is **fully reversible.** Two mechanisms, one hormone |
