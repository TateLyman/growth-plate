# F-R043 — The stack, derived from the identity rather than borrowed

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** The stack, built independently. Along the way the governing equation **integrates to a closed
form**, and that closed form reorganises the whole problem: it says which terms are free, which one
decides whether the total is finite, and that λ — the thing every intervention in the literature moves —
**does not appear in the total at all.** One new agent class falls out of it that this branch had never
seen, and it is the one the theory said could not exist.

---

## 1. The identity integrates, and the answer is one line

Per column, from F-R032/R033:

```
dL/dt  =  λ · n · A · h_term
dn/dt  =  λ · n · (a − b)  +  influx
```

**Influx is zero for length, and that is now settled rather than assumed.** The lateral supply into the
plate is the Axin2⁺ population of the groove of Ranvier, and the primary literature is explicit that those
cells are *"responsible for the **appositional (transverse) growth** of the growth plate"* — they build
width. F-R033's parallel-column geometry says width contributes nothing to length. So the two independent
lines meet: **influx ≈ 0 in `dL/dt`, and the stem pool is a closed account.**

Set `influx = 0` and integrate with `(a − b)` constant:

```
n(t) = n₀ · e^{λ(a−b)t}

L(t) = [ A · h_term · n₀ / (a − b) ] · ( e^{λ(a−b)t} − 1 )
```

Three regimes, and they are the three questions:

| regime | behaviour | which of the three goals |
|---|---|---|
| **a − b < 0** | L converges to a finite asymptote | the normal human. Finite height |
| **a − b = 0** | L grows **linearly, forever**, at `λ n₀ A h` | unlimited, constant velocity |
| **a − b > 0** | L grows **exponentially** | unlimited *and* accelerating |

And in the finite case the asymptote is:

> # L∞ = A · h_term · n₀ / (b − a)

**Four symbols. Forty-three rounds price them, and the equation says exactly what each one is worth.**

- **`A` and `h_term` are free multipliers.** They scale the total linearly and appear **nowhere** in
  `dn/dt`. Doubling either doubles final height at no cost to the pool. This is the arithmetic reason
  h_term-first is correct, and I reached it from the identity rather than from anyone's ranking.
- **`n₀` is the starting pool** — linear, and not modifiable after the secondary ossification centre forms.
- **`(b − a)` is the only term in the denominator.** It alone decides whether the total is finite. As it
  goes to zero the total diverges. **This is what "unlimited" means, formally.**
- **`λ` does not appear in `L∞` at all.**

> ### λ sets the rate and not the total. Spending faster does not let you spend more.

That is the conjugacy identity in its strongest form, and it retires an assumption I have been carrying
since F-R024. **"Fast" and "unlimited" are not in tension.** They looked antagonistic because every lever
the field has ever tested moves `λ` — GH, oestrogen, Hedgehog, ERβ — and `λ` is precisely the term that
trades. **`A` and `h_term` raise the rate *and* the total simultaneously.** There is no trade on those two.
The whole difficulty was that the field had been pulling the one lever that cannot win.

**Which reduces the programme to three instructions:**

1. **Fast** → raise `A` and `h_term`. Raise `λ` only if the pool is protected.
2. **Unlimited** → drive `(b − a)` toward zero. Nothing else does it.
3. **Never close** → the same as (2), plus block whatever pushes `b` up at puberty.

Goals 2 and 3 are the same goal. There were never three problems. There are two.

---

## 2. `(b − a)` — the term that decides everything, and the agent I did not know existed

F-R040's FLAW 8 said the theory needed a **cartilage-restricted ERα antagonist**, that no such agent
exists, and that building one meant solving targeted delivery (octaarginine, cystine-dense peptides,
WYRGRL collagen-II peptide — all real, none done for this target).

**That framing was wrong, and the reason is that closure has a named local effector downstream of the
receptor.**

### CXXC5 — *"CXXC5 mediates growth plate senescence and is a target for enhancement of longitudinal bone growth"*, Life Science Alliance 2019;2(2):e201800254 (PMC6458850)

The axis, in the authors' terms:

> *"With pubertal progression, **estrogen induces CXXC5 expression** and subsequently **inhibits the
> Wnt/β-catenin pathway**, resulting in **growth plate senescence**."*

CXXC5 is a negative regulator of Wnt/β-catenin that acts in the cytosol by binding **DVL**. E2 (100 nM)
induces CXXC5 in human C28/I2 chondrocytes, maximal at 24 h. `Cxxc5` mRNA rises through pubertal
progression in the plate.

**And it is genetically load-bearing:** `Cxxc5⁻/⁻` mice show **significantly delayed growth plate
senescence** and **significantly greater tibial length at 12 weeks** (ANOVA P = 2.37 × 10⁻²; post-hoc
P < 0.005), with increased cells per column at 9 and 12 weeks (P < 0.005).

**Two agents exist:**

| agent | target | dose used | model |
|---|---|---|---|
| **KY19382** | dual **CXXC5–DVL (IC₅₀ 19 nM)** and **GSK3β (IC₅₀ 10 nM)**; orally active | **0.1 mg/kg/day i.p.** | **wild-type mice**, 3 → 13 weeks (10 weeks dosing) |
| PTD-DBMP | peptide, blocks CXXC5–DVL only | 1 mg/kg/day i.p., 2 weeks | 7-week-old mice |

**KY19382 in wild-type mice:** tibiae significantly longer (n = 7–15, ***P < 0.0005); **increased cell
number per column in the resting, proliferative *and* hypertrophic zones**; no histological abnormality in
articular cartilage or liver; no weight difference over 10 weeks. PTD-DBMP reproduces the per-column
increase.

**Why this changes the architecture, and not just the shopping list:**

1. **It is the closure arm without the receptor.** Every "never close" result this branch has relied on
   blocks ERα, and F-R039–R042 established that blocking ERα *systemically* costs the GH/IGF-1 spurt
   (whole-body ERα⁻/⁻: IGF-1 −20%, MUP −24%; MPP: femur, plate height, PZ, PCNA all down; Vidal: IGF-1
   −23%). CXXC5 sits **downstream of the receptor, inside the chondrocyte.** Blocking it removes
   oestrogen's local senescence arm while leaving oestrogen signalling everywhere else — liver, bone,
   uterus, the GH axis — completely intact. **Cartilage restriction stops being a delivery problem
   because it stops being necessary.** FLAW 8 is not solved; it is dissolved.
2. **It is a `(b − a)` lever, not a `λ` lever** — at least by its stated phenotype. Delayed *senescence*
   is by definition a change in the exhaustion term, not the rate term. That is the denominator.
3. **It has a wild-type gain arm.** F-R038 and F-R040 recorded, repeatedly, that every candidate in this
   programme had only a loss-of-function or rescue arm — CREB (666-15 does nothing in wild-type mice),
   acetyl-CoA (GEO confirms only loss-of-function was ever run), Sox9, mTORC1. KY19382 was given to
   normal mice and made them longer.

**And the honest problem with it is §5.**

---

## 3. `A` and `λ` — FGFR3, and the first human tall-stature loss-of-function

### The human gain arm exists, and I had never looked for it

**CATSHL syndrome** (camptodactyly, tall stature, hearing loss; OMIM 610474) is **heterozygous partial
loss of function of FGFR3** — p.R621H in the kinase domain. The phenotype:

> **Adult height >97th centile in 5/5 men, mean 77 inches (195.6 cm). >75th centile in 9/9 women,
> >97th in 8/9, mean 70 inches (177.8 cm).** Skeletal features include **tall vertebral bodies**.

Two things matter here and both are firsts for this branch:

- **This is a human, at a receptor, with a partial block, reaching roughly +2 SD.** Not a mouse, not a
  knockout, not a rescue. It is the human existence proof for the `A` arm that F-R040's FLAW 4 said
  did not exist for any arm of the theory.
- **Tall vertebral bodies.** **FLAW 1 — "this is a limb theory, not a height theory" — is repaired here
  and not by the receptor I was chasing.** ERα is appendicular-selective (Vidal: crown–rump 98% of
  control) and ERβ's axial gain is transient and untestable in mice (F-R042 §4). FGFR3 reaches the spine
  in a human. So does CNP (§4). **The two arms I am actually building on are axial-competent; the
  oestrogen arms never were.**

### And the wild-type animal gain arm exists too

**TYRA-300 (dabogratinib)**, FGFR3-selective inhibitor, *JCI Insight* 2025 (PMC12128972). The relevant
experiment is the one the paper treats as an aside — **wild-type female C57BL/6J**, oral gavage, 4 weeks
(age 4 → 8 weeks):

| endpoint | 12 mg/kg | 14 mg/kg |
|---|---|---|
| **femur length** | **+5.0%** | **+8.2%** |
| **tibia length** | **+3.9%** | **+6.4%** |
| nasoanal length | — | **+7.3%** |
| tail length | ✱ | ✱ |

All P < 0.05. The authors: *"inhibition of **wild-type** FGFR3 signaling can effectively enhance growth
velocity in a **dose-dependent** manner."* **Meclozine** — an over-the-counter antihistamine — reproduces
the direction in wild-type mice at 1–2 mg/kg/day, with a bell-shaped dose response (20 mg/kg does nothing).

### The clinical agents, and a dose finding that matters

| agent | route | human dose | result |
|---|---|---|---|
| **infigratinib** | **oral, daily** | **0.25 mg/kg/day** | PROPEL 3, n = 114, 52 wk: AHV **+1.74 cm/yr vs placebo** (95% CI 1.31–2.17, P < 0.001); **first significant improvement in body proportionality**. NEJM, 28 Jun 2026 |
| **dabogratinib (TYRA-300)** | oral, daily | 0.125 / 0.25 / 0.375 / 0.50 mg/kg | BEACH301 phase 2 dose escalation, first child dosed Aug 2025 |

> **The dose gap is the finding.** The mouse experiment that moved a **normal** plate used **12–14 mg/kg/day**.
> The paediatric achondroplasia programmes dose **0.125–0.5 mg/kg/day** — 25–100× lower — because they are
> titrating against a **hyperactive** receptor in a child who cannot tolerate FGFR toxicity. **Those doses
> are calibrated for a mutant receptor and there is no reason to expect them to be the right doses for a
> wild-type one.** Infigratinib's own oncology dose is 125 mg/day (~1.8 mg/kg), 7× the achondroplasia dose
> and tolerated in adults. This is the single most concrete translational statement in the round, and it
> is a statement about the *ceiling*, not the agent.

### The identity's warning on this arm, stated plainly

FGFR3 inhibition raises **proliferation** — that is `λ`, the taxed term. By §1, `λ` does not enter `L∞`.
So on the arithmetic alone, FGFR3 inhibition should front-load and converge, like GH, like ERβ, like SAG.

**The one reason to think it does not:** FGFR3 signalling *"induces a **reversible** senescence phenotype
in chondrocytes similar to oncogene-induced premature senescence"* — strong sustained ERK, growth arrest,
matrix loss, senescence markers. If FGFR3 also sets `b`, then blocking it lowers the denominator as well as
raising the numerator, and CATSHL's +2 SD adult height is the observable consequence. **CATSHL adults are
tall at adult height, which is a durability endpoint — the endpoint F-R042's FLAW 13 said nothing in this
programme ever reports.** That is suggestive and it is not proof; nobody has counted stem cells in a
CATSHL plate or an FGFR3-inhibited wild-type one.

---

## 4. `h_term` — the only term provably outside `dn/dt`, and the one with a licence

### Why it goes first

`h_term` multiplies `dL/dt` and appears nowhere in `dn/dt`. By §1 it scales `L∞` linearly at zero pool
cost. It is the only term for which that is *provable* rather than hoped.

### The human gain arm, again at both ends

- **NPR2 gain of function** (p.V883M, constitutively cGMP-generating): **tall stature**, macrodactyly,
  scoliosis, coxa valga — *epiphyseal chondrodysplasia, Miura type*, across three- and four-generation
  families. A submembrane activating deletion in NPR-B also causes tall stature (JCEM 2020).
- **CNP overproduction** by chromosomal translocation: **tall stature** in humans.
- **CNP-transgenic mice: 19% longer than littermates at 10 weeks**, with overgrowth of *"long bones of
  limbs, **vertebrae and skulls**"* and increased thickness of **every** growth-cartilage layer.
  **Axial reach again.** CNP22 on wild-type tibiae: **+31–42%** longitudinal growth ex vivo, with
  *"an increase in the **number and size** of hypertrophic chondrocytes."*

### The agent

**Navepegritide (TransCon CNP, YUVIWEL)** — **FDA accelerated approval February 2026**, once-weekly
subcutaneous. ApproaCH pivotal trial met its AGV primary endpoint at week 52 and held it through
**104 weeks**, with improved lower-limb alignment, proportionality and height z-scores, and — the
endpoint that matters most for this stack — **"no evidence of accelerated bone age."**

> **That is the empirical signature of a term outside `dn/dt`: output up, clock not advanced.** No other
> arm in this programme has it.

Vosoritide (daily) is the alternative: ~+1.6 cm/yr AGV vs placebo.

### And GH, priced correctly

**COACH phase 2** (Eur J Endocrinol 2026): navepegritide **+ lonapegsomatropin**, treatment-naive children,
week 52 — **AGV 8.69 cm/yr vs 5.95 cm/yr** on navepegritide monotherapy, **Δ +2.74 cm/yr**. Arm span
+9.4 cm.

The identity's reading of that number is not the press release's. **GH is a `λ` lever, and `λ` is absent
from `L∞`.** `chu2025` measured the cost directly — GH depletes the stem pool — and the human atlas
(Sci Transl Med 2026) now shows GH **directly** stimulating human growth-plate stem-cell proliferation via
JAK/STAT, TGFβ and ERK. **+2.74 cm/yr is real velocity that the model does not credit to the total.** It
belongs in the stack only when `(b − a)` is being held, and never as the load-bearing arm.

---

## 5. The one conflict I cannot resolve — and it is the decisive experiment

KY19382 works by **raising Wnt/β-catenin**. Two other lines say Wnt is exactly what depletes the stem pool.

| source | manipulation | result |
|---|---|---|
| **KY19382 / Cxxc5⁻/⁻** (LSA 2019) | Wnt **up** (CXXC5–DVL block + GSK3β inhibition) | resting-zone cell number **up**, senescence **delayed**, tibia **longer** |
| **eLife 2021;10:e64513** | Wnt **up** in PTHrP⁺ cells (*Apc* haploinsufficiency) | PTHrP⁺ cells **474.8 vs 718.7 at P9, 558.4 vs 910.3 at P12, 443.4 vs ~ at P21** — a **~35–40% deficit**; short columns 45.9 vs 67.4 (P = 0.03); long columns 7.3 vs 26.5 at P96 (P = 0.03) |
| **human atlas** (Sci Transl Med 2026) | descriptive | human **root stem cells** reside in a niche *"low in **WNT** and TGF-β"* |

**Two of three say Wnt-high is where stem cells go to die. The one that says otherwise is the one holding
my best agent.**

**The resolution I favour, flagged as inference and not fact:** CXXC5 is an **oestrogen-induced, pubertal
brake**. Blocking it should *restore the juvenile Wnt set-point*, not exceed it. *Apc* haploinsufficiency is
constitutive, supraphysiological, cell-autonomous Wnt inside the stem compartment itself, from birth.
Different magnitude, different compartment, different window. The dose-shape of KY19382 (0.1 mg/kg — three
orders of magnitude below the meclozine-style doses, and indirubin analogues show bell-shaped responses)
is consistent with a restoration rather than an elevation.

**But I have said "restoration, not elevation" before and been wrong about which one an agent delivers.**
That is the CREB trap (F-R038 §2: 666-15 restores an achondroplastic plate and does *nothing* to a normal
one) run in reverse.

> **The experiment that decides the stack, stated as a protocol because that is all that is missing:**
>
> KY19382, 0.1 mg/kg/day, wild-type mice, from 3 weeks. Measure at **1 month, 6 months and 18 months**:
> (i) tibia and femur length and **crown–rump**; (ii) stem-cell number by **two independent markers**
> (PTHrP-CreER lineage and CD73), with **EdU turnover** so accumulation can be told from healthy
> expansion — the `horike2026` assay design; (iii) growth velocity by calcein double-labelling; (iv)
> plate patency at 18 months.
>
> **If the pool holds at 18 months, `(b − a)` has been moved and the equation says the total is no longer
> finite. If the pool falls, KY19382 is the fourth front-loader and the identity has won again.**

Every positive result in this programme has been ≤ 12 weeks (PHTPP), ≤ 6 months (SAG), or one late
timepoint. **Chagin is the only study that followed to 18 months, and it is the only one where the
advantage vanished.** That is not a coincidence; it is a selection effect in the field's follow-up windows,
and it is why the timepoints above are the whole test.

---

## 6. The stack

**Rule, from §1: one agent per term. Stack across terms, never within one** — except where direct synergy
data exists at a *serial* node (§6c).

### 6a. Load-bearing arms

| # | term in `L∞` | agent | route / dose | status of the evidence |
|---|---|---|---|---|
| **1** | **`h_term`** — free multiplier | **navepegritide** | 100 µg/kg **weekly SC** | **Approved Feb 2026.** Human genetic gain arm (NPR2 GOF → tall stature). WT mouse gain arm (+19%, axial). **Bone age not advanced at 104 wk** |
| **2** | **`A`, and possibly `b`** | **infigratinib** (or dabogratinib) | oral daily; **0.25 mg/kg** is the achondroplasia dose and is **very likely sub-therapeutic for a wild-type receptor** (§3) | Phase 3 positive. Human genetic gain arm (**CATSHL, mean adult ♂ 195.6 cm, tall vertebrae**). **WT mouse gain arm (femur +8.2%)** |
| **3** | **`(b − a)`** — the denominator | **KY19382** | 0.1 mg/kg/day i.p. in mouse; **orally active**; HED ≈ **0.008 mg/kg ≈ 0.6 mg/day** for 70 kg by Kₘ scaling (3/37) | **Wild-type mouse gain arm; senescence delayed; `Cxxc5⁻/⁻` confirms the genetics.** **No human exposure of any kind.** §5 is unresolved |

### 6b. Human-validated fallback for term 3 — because arm 3 has never been in a person

Arm 3 is the arm the whole equation turns on and the only one with zero human data. The fallback is not a
different mechanism; it is the same term approached at the ligand, with adult-height RCTs behind it:

| combination | adult-height gain | evidence |
|---|---|---|
| **GnRHa + rhGH** | **5–10 cm** (GHD, ISS) | RCT, LoE 1 |
| **anastrozole + rhGH** | greater AH than rhGH alone | RCT (Rothenbuhler) |
| **oxandrolone + rhGH** | **+2.7 cm** | Cochrane meta, RCT |
| letrozole alone / GnRHa alone | **null at adult height** | RCT |

**The pattern is §1 restated in human data: delay alone moves nothing, because delay alone moves nothing in
`L∞`.** `λ` is absent from the total; slowing it and stopping there buys you the same height later. Only
delay *plus* drive shows up at adult height.

**Oxandrolone deserves its own line.** Non-aromatizable, so it drives without feeding the closure arm;
DHT promotes chondrocyte proliferation and proteoglycan synthesis directly in the plate. **Drive that does
not convert to oestrogen is the only kind of drive this equation likes.**

### 6c. The one within-term addition, and why it is not a violation

FGFR3 signalling inactivates NPR2 by driving its **dephosphorylation** through a PPP-family phosphatase.
So arms 1 and 2 are **serial nodes on one chain**, not parallel additions to one node — which is exactly
why they are not redundant, and why the two cGMP failures the design rule was built on (sacubitril not
additive with CNP; tadalafil raising cGMP 37–52% with no length gain) do not predict this case. **LB-100**
(PP2A inhibitor, human phase 1/2 in oncology) sits on the third node and is **synergistic with BMN-111 in
explants** (10 µM + 0.1 µM, 6 days). Recorded as the only defensible within-arm addition, and only on that
synergy data.

### 6d. Not in the stack, and why

| excluded | reason |
|---|---|
| **all SERMs** — tamoxifen, raloxifene | **Tamoxifen: apoptosis of growth-plate chondrocytes, permanent growth arrest, IGF-1 suppressed.** **Raloxifene acts as an ERβ *agonist* and *induces* growth-plate fusion.** Whole class points the wrong way |
| **systemic ERα blockade** | loses the spurt — MPP, whole-body ERα⁻/⁻, every human ESR1/aromatase case |
| **ERβ antagonism (PHTPP)** | F-R042: front-loads, converges by 18 months, tracks serum IGF-1. Keep **only** if oestrogen is elevated, where its brake actually scales |
| **mTORC1 activation** | **expands the pool and gives no length in vivo** (Tsc1 cKO: bones normal or short). A pure identity trade with the length side empty |
| **Wnt agonists as such** (indirubin-3′-oxime, lithium) | §5. The pool cost is measured and it is 35–40% |
| **groove-of-Ranvier / influx strategies** | Axin2⁺ cells do **transverse** growth. Zero length term |
| **CREB inhibition, acetyl-CoA / HDAC, hypoxia, local warming** | eliminated F-R034–R039, unchanged |
| **GH as a load-bearing arm** | `λ`-only; absent from `L∞`; pool cost measured (`chu2025`) and now shown directly on human cells |

---

## 7. What the stack is worth, stated without inflation

**What can be defended:**

- Arms 1 and 2 each have a **human genetic gain arm reaching roughly +2 SD** (NPR2 GOF; CATSHL 195.6 cm),
  a **wild-type animal gain arm** (+19% CNP-Tg; +8.2% femur TYRA-300), **axial reach** (vertebrae in both),
  and a **licensed or phase-3-positive agent**.
- Arm 1 has the **bone-age-sparing** signature that says it is not borrowing from the future.
- The combination benchmark that exists — navepegritide + GH — is **8.69 cm/yr**, and the delay+drive
  benchmark at adult height is **5–10 cm**.

**What cannot:**

- **`L∞` is finite unless arm 3 works, and arm 3 has never been given to a human.** Arms 1 and 2 multiply
  a finite total. They can plausibly multiply it a lot. They cannot make it unbounded.
- **No stem-cell measurement exists for any agent in the stack.** Not one. FLAW 5 and FLAW 6 stand exactly
  where F-R040 left them.
- **"Unlimited" is a statement about `(b − a) → 0`, and the only evidence that anything moves it is a
  single 2019 paper whose mechanism is contradicted by two others (§5).**
- The mechanical ceiling (FLAW 12, L² strength vs L³ load) is untouched by any of this and is a property of
  the phenotype, not a preference.

**The honest one-sentence version:** *the equation now says exactly what to build and in what order, two of
the three arms are licensed or nearly so and have human tall-stature genetics behind them, and the arm that
decides whether the answer is "a lot" or "unlimited" rests on one mouse paper and one unresolved conflict
about Wnt.*

---

## 8. Flaw register — what moved

| flaw | change |
|---|---|
| **1. limb-only, not height** | **repaired, and by different agents than I expected.** CATSHL has **tall vertebral bodies**; CNP-Tg mice overgrow *"vertebrae and skulls."* The oestrogen arms never reached the spine; the arms the stack actually rests on do |
| **4. no human instance** | **substantially repaired for arms 1 and 2.** NPR2 GOF and CATSHL are human, at the receptor, with adult heights. Still **wholly open for arm 3** |
| **5. no velocity lever that spares the pool** | **h_term is that lever, and it is now licensed.** Navepegritide: 104 weeks of growth, bone age not advanced |
| **8. delivery of a cartilage-restricted block** | **dissolved, not solved.** CXXC5 is the local effector *downstream of the receptor*; restriction becomes unnecessary. The targeting chemistry (octaarginine, CDPs, WYRGRL, CBD-CNP) remains available and is no longer on the critical path |
| **13. durability never measured** | **unchanged and now the explicit gate.** §5's protocol is written against it |
| **NEW 14 — the Wnt contradiction** | KY19382 vs *Apc*-haploinsufficiency vs the human WNT-low niche. **The single experiment that decides the stack** |
| **NEW 15 — the dose gap** | Paediatric FGFR3-inhibitor doses are titrated against a **hyperactive** receptor and are 25–100× below what moved a **wild-type** plate. The clinical ceiling for the `A` arm is unknown and probably not where the label says |
| 2, 3, 6, 7, 9, 10, 11, 12 | unchanged |

---

## 9. What I would want next

**No paper is blocking.** What is missing is §5's experiment, and one thing I could not retrieve:

1. **The Life Science Alliance figure source data** — Fig 5J tibia lengths in mm and the per-column counts.
   The paper is open access but the numbers live only in the figures; I have the statistics and not the
   effect sizes. **This is the effect size of the only `(b − a)` agent in existence.**
2. **Any human or primate exposure to a CXXC5–DVL inhibitor.** CK Regeon has KY19382 in formulation
   development for alopecia; I found **no registered human trial**. If one exists, it is the only safety
   and PK anchor arm 3 will ever have.
3. **The Sci Transl Med human growth-plate atlas full text** (adw3590; the bioRxiv preprint is
   2025.03.14.642964). I have it only through abstracts and search summaries. It is the **first human
   growth-plate single-cell atlas** and the only thing that will ever address FLAW 11.
