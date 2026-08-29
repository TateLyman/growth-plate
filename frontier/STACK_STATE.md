# Live stack state — what is in it, what is missing, and why

**Branch:** `claude/height-enhancement-research-v34b4r`
**Last updated:** F-R076
**The goal, unchanged:** fast **and** unlimited **and** never-closing — all three simultaneously.
Only then the compounds.

This file exists so the state survives context loss. The round documents are the reasoning; this is the
ledger.

---

## 1. What is currently in the stack

| agent | dose | arm | what it actually does to the identity |
|---|---|---|---|
| **erdafitinib** | **8 mg** | **three jobs, not one (F-R060)** | (1) flux — PZ **+25%** in Fgfr3 cKO; (2) **terminal cell volume** — *"significant swelling of hypertrophic cells"* (infigratinib, JBMR 2024), HZ **+45%**; (3) **the closure step** — lowers **ERK1/2**, the same node phosphate→VEGFR2→caspase-9 uses to kill the terminal chondrocyte. **Works in wild-type: TYRA-300 femur +8.2%, tibia +6.4% in 4 wk; and the FDA tox package shows growth-plate thickening in NORMAL rats (≥1 mg/kg) and dogs (3 mg/kg).** **But see F-R061: at oncology doses it raises serum phosphate, which drives the very death signal it otherwise suppresses. The 8 mg label dose is titrated INTO phosphate 5.5–7.0 mg/dL.** |
| **somatropin (GH)** | **0.07 mg/kg/day** (= 0.49 mg/kg/wk) | **AKT support for erdafitinib** | **Not a rate agent.** FGFR3 blockade alone is **apoptotic**; IGF-1 via sustained AKT rescues it. That is the job. **REVISED in F-R066: the low-dose rationale is withdrawn.** GH -> IGF-1 -> AKT -> TSC2 -> **mTORC1**, and mTORC1 activation is what **expands** the stem pool (Newton: 2.5x). So GH does not merely spend the pool - it plausibly renews it. Chu's depletion was measured in an **oestrogen-replete** setting; oestrogen is the spending signal. **0.49 mg/kg/wk sits at the top of the range the human efficacy data used** (Mauras/ANSWER 0.24-0.53, +22.5 vs +13.0 expected); 2 IU/day is ~0.12 and no combination trial used it. **And a third candidate role as of F-R059:** GH **normalises terminal chondrocyte volume** in uremic rat via proposed Nkcc1 + Igf1 — the only half of the identity nothing else touches. One study, deficit-normalisation not supranormal gain; carried as a hypothesis. |
| **abaloparatide** | **80 µg** | structural — now with a mechanism | **Not a growth agent** (Winer, 10 years, open plates, no growth effect). For the **mechanical envelope** — and F-R060 gives the reason: *Fgfr3*-null mice show **increased femur length with decreased BMD**, and aromatase loss gives **increased osteoid and low phosphate**. **SCFE is the mechanical shadow of the effect we want, not an incidental toxicity.** |
| **serum phosphate** | **AGE-NORMAL** | **corrected again in F-R064 — this is now the third revision and the last one is right** | F-R060 predicted oestrogen ablation would *lower* it and cause rickets. **Backwards for humans:** oestrogen ablation **raises** phosphate (Uemura TmP/GFR +28.5% on GnRH-a; Zhang NHANES n=7,005, 3.83 vs 3.98 mg/dL, P<0.001; rat NaPi-IIa mechanism). **And erdafitinib raises it on-target (89% of patients).** Both stack arms push phosphate UP, and **phosphate is the executioner's ligand.** **F-R064: holding it LOW was wrong and pushes toward rickets.** Phosphate is *permissive* for the junction to advance; hypophosphatemia blocks terminal apoptosis and produces a thick plate on a short child. **Target age-normal** — not suppressed, not the oncology 5.5-7.0. The reason to control it is **ectopic/renal mineralisation**, not growth. Note **GH raises phosphate too** (IGF-1 upregulates proximal-tubule NaPi), so three arms raise it; **abaloparatide is phosphaturic** and pushes the other way. |
| **anastrozole** | **1 mg** | oestrogen arm — **revised in F-R063** | Head-to-head over 3 yr, 79 boys: anastrozole arm **+1.0 cm** PAH vs letrozole **+0.5 cm**; letrozole **slowed growth velocity** (P=.039) and **lowered IGF-1**, the Phase 3 driver of `v(c)`. Anastrozole keeps T in range (552 vs 982 ng/dL, 48% >1000 on letrozole). **Effect plateaus at 1 mg** — 0.5 mg approximately equals 1 mg in adolescent males, and >=1 mg reaches the assay floor, so doubling is inert. **RESOLVED in F-R065: anastrozole.** The letrozole argument was residual intracrine substrate (2.0% vs 6.5% residual E1S, with STS at 265-660x aromatase in the plate) — but that mattered only if residual oestrogen closed the plate, and link 11 shows it does not. **What binds is supply, and anastrozole preserves velocity, IGF-1 and normal T.** | Standing instruction, plus a second reason as of F-R057 (§4). |

---

## 2. The identity as it now stands — measured, not modelled (F-R058)

```
dL/dt  =  flux  ×  v(d)_terminal
          │         │
          │         └─ terminal chondrocytic domain volume = v(c) cell + v(m) matrix per cell
          └─ N_lost per day; gated by cell-cycle time and proliferative-zone height
```

Derived independently by **Wilsman 1996** from two separately-measured equations; confirmed empirically by
**Breur 1997** (`R² = 0.992`, exactly these two variables plus their interaction). **Verified on Wilsman's
own data: flux × domain = 8.42× against a measured growth ratio of 8.43×.**

**The human, anchored for the first time (F-R059).** `v(c)` measured stereologically in a human distal
tibial physis at closure — **5,900 µm³** (White 2008, RHT fixation, Wilsman's lab, same method as all animal
data; n=1 and chemotherapy-exposed, so plausibly depressed). Distal tibia peak rate 5 mm/yr = 13.7 µm/day.

| plate | rate µm/day | v(c) µm³ | flux cells/mm²/day |
|---|---|---|---|
| rat proximal tibia | 396 | 14,997 | 12,830 |
| rat proximal radius (slowest) | 47 | 4,135 | 4,340 |
| **HUMAN distal tibia, peak** | **13.7** | **5,900** | **≈1,300** |

> **The human runs at ~1/3 the cell flux of the slowest rat growth plate, at a comparable cell volume.
> Poor on both factors.** Humans are tall by *lasting*, not by growing fast — low flux **is** the mechanism
> of long duration, which is Gafni's banking result read forward.
>
> **Hence: raising flux is a withdrawal; raising `v(d)` is not.** Every extra division spends the account
> "never close" depends on; every extra µm³ of domain volume converts the *same* division into more length.
> **`v(d)` is the only lever that is fast and not a withdrawal.**

**Measured headroom in terminal cell volume, all wild-type mammals:** rat proximal tibia 14,997 (**2.5×**),
rabbit distal radius 18,000 (**3.1×**), jerboa metatarsal 23,000 (**3.9×**), **bat manus 40,300 µm³
(6.8×)** — the bat carrying 1,300 µm³ cells in its own foot, a **31× range in one animal under one
endocrine environment.** At constant flux the distal tibia alone would run **10 mm/yr at 2×, 34 mm/yr at
6.8×**, against 5 mm/yr now.

**The decomposition of the natural range, fastest rat plate against slowest:**

| factor | contribution | in the stack? |
|---|---|---|
| **flux** (N_lost/day) | **3.16×** | erdafitinib, via cell-cycle time |
| ↳ cell-cycle time | 2.47× (30.9 → 76.3 h) | erdafitinib |
| ↳ proliferative-zone height | 3.19× (43 → 137 µm) | **nothing** |
| ↳ growth fraction | **saturated, 0.89–0.99** | **closed — no headroom exists** |
| **terminal domain volume** | **2.67×** (human headroom **6.8×**) | **nothing — GH a candidate** |
| ↳ cell volume `v(c)` | 3.63× | **nothing** |
| ↳ **pericellular/territorial** matrix | +61% P→H; **the capillary invasion route** | **nothing** |
| ↳ interterritorial matrix | +26% P→H; calcifying structural template | **nothing** |
| conversion efficiency per unit volume | ~2× loss, rabbit 5 → 8 wk | **nothing** |

**Both factors are of comparable size and they multiply.** This kills both extreme positions the branch has
held: *"λ is worthless"* (F-R044 — wrong, flux is the larger factor) and *"h_term is the free multiplier"*
(F-R043 onward — overstated; it is one of two, and cannot act alone).

**Retracted:** F-R057's `dL/dt = N_h · h_term / τ`. Whole-plate transit time is **not** constant — 1.56 →
3.85 days in the rat, a 2.46× range varying inversely with growth rate. Cooper's "~24 h" is a narrower,
hypertrophic-zone-only claim inherited from bat/mouse forelimb work I still do not have. The form above
needs no τ assumption.

**The four arms and which term each moves:**

| arm | term | best evidence | verdict |
|---|---|---|---|
| pool | flux, `(b−a)` | FoxA2⁺ serial transplant; dexamethasone banking (Gafni, 88% → 14% fusion) | banks |
| oestrogen | `w(E₂)` | Weise, Nilsson, aromatase-deficiency cases | removes a write-off; does not stop the count |
| Hedgehog, ligand level only | flux/amplitude | Haraguchi *Hhip1* cKO, +43% plate area → +4.5% length at 53 wk | weak |
| vascular | transit | Gerber Flt-(1-3)-IgG; Voss 2015 human paediatric widening; resveratrol | banks, reversible |

---

## -1. THE CELLS ARE NOT EXHAUSTED, AND THE COST PER DIVISION IS VARIABLE (F-R071)

**Nilsson, Baron et al., *J Endocrinol* 2005;186:241 (PMID 16002553):**
> *"the number of population doublings of rabbit resting zone chondrocytes in culture **did not depend on
> the age of the animal** from which the cells were harvested... the mechanisms limiting replicative
> capacity **in vivo are distinct from those in vitro**."*

**Sharper than the abstract (F-R072):** RZ chondrocytes **DO** undergo Hayflick in culture — plateau at
**~14 population doublings**, with senescence-associated beta-galactosidase (vs 8-10 PD for adult rabbit
articular, **35-40 for young adult human articular**). **But maximum PD did not depend on donor age
(P=0.36).** **The cells have a finite intrinsic counter and living in an old animal does not spend it.**
**Two clocks, not one:** the in-vitro Hayflick counter is real and untouched by in-vivo ageing; the in-vivo
limit is separate and is what actually stops growth. The limit is imposed
in vivo and is epigenetic. Baron's own conclusion: **"loss of DNA methylation might be a fundamental
biological mechanism that limits longitudinal bone growth in mammals, thereby determining the overall adult
size of the organism."**

**Schrier, Baron et al., *J Endocrinol* 2006;189:27 (PMID 16614378)** — RZ proliferation rate and RZ cell
number both fall with age; **dexamethasone decreased RZ proliferation AND slowed numerical depletion**
(banking, measured at cell-count level). **And the result that breaks the conservation law:**
> *"Estrogen is known to accelerate growth plate senescence. **However, we found that estradiol cypionate
> treatment slowed resting zone chondrocyte proliferation**... estrogen might accelerate senescence by a
> proliferation-independent mechanism, or by **increasing the loss of proliferative capacity per cell
> cycle**."*

> ### F-R066's conservation law ("every centimetre advances the programme by a fixed amount") is CORRECTED. The advance per division is **not constant** — oestrogen raises it:
> ```
> clock advance = SUM over divisions of ( cost per division )    <- cost is MODULATED, not fixed
> ```
> **This is the first genuine escape from the conservation law.** And it upgrades the anti-oestrogen arm's
> rationale: it does not merely postpone the endpoint, **it makes every division cheaper in capacity.**
> Joins CXXC5 — a transcriptional brake applied every cycle is exactly what a per-cycle cost term looks like.

## -1a-00. **F-R083 — THE THREE MISSING EXPERIMENTS, ANSWERED WITHOUT RUNNING THEM**

**Computed from the repo's own growth-plate atlas + the chondrocyte methylome + GWAS Catalog.**
Code: `frontier/analysis/no_new_experiments/`.

### (a) HUMAN GROWTH PLATE, ZONE-RESOLVED (Chu atlas, 22,971 genes, 10 donors aged 11-14)
Paired within donor, prolif vs stem:

| gene | stem | prolif | preHT | HT | delta | p | pct |
|---|---|---|---|---|---|---|---|
| **DNMT1** | 14.1 | **33.0** | 26.8 | 23.4 | **+16.5** | **0.047** | 82 |
| **UHRF1** | 6.4 | **15.7** | **4.5** | **3.4** | **+11.0** | **0.051** | 60 |
| **DNMT3A** | 24.7 | 27.0 | 28.4 | 27.0 | −0.6 | 0.23 | **84** |
| DNMT3B | 1.2 | 2.1 | 1.2 | 0.9 | +1.3 | 0.085 | **35** |
| EZH2 / EED / SUZ12 | | **all peak in prolif** | | | | **0.016 / 0.009 / 0.037** | |
| **ESR1** | **44.5** | 30.6 | 28.3 | 29.2 | **−16.7** | **0.017** | 88 |
| ACAN / CCN2 | | | | | | | **97 / 98** |
| **RTL1 / CYP19A1** | | | | | | | **25 / 29 — ABSENT** |

> ### **Yanagihara's mouse IHC REPLICATES IN HUMAN TISSUE:** DNMT1 and UHRF1 both rise stem→proliferative
> and **collapse in preHT/HT** — maintenance machinery on in the proliferative compartment, off as cells
> leave it. **DNMT3A is at the 84th percentile in ALL zones incl. stem; DNMT3B is absent (35th) — DNMT3A has
> NO redundant partner in this tissue.** With TBRS's normal IGF-1/GH (F-R081), **cell autonomy is the
> parsimonious reading.**

**Three unlooked-for findings:** (i) **PRC2 is zonally organised** — EZH2/EED/SUZ12 all peak in prolif;
(ii) **ESR1 is a RESTING-ZONE gene**, falling on proliferation — a new argument that oestrogen acts on the
pool, fitting Schrier (F-R072); (iii) **RTL1 is at the 25th percentile — NOT expressed in human growth
plate.** F-R078 called RTL1 the second height gene at 14q32.2; **whatever it does, it does not do it in the
plate.** CYP19A1 at 29th weakens F-R049's intracrine-aromatase argument.

### (b) POLYCOMB TERRITORY — **I WAS WRONG, AND THIS IS THE CORRECTION**
Tested Dnmt1-dependent regions against Polycomb loci. **Hox clusters are ENRICHED, not depleted**
(HoxA 4.82x, HoxC 3.05x, HoxD 2.37x; all DMV loci 1.69x). But the gradient explains it:

| | fold | p(enrich) |
|---|---|---|
| **canyon cores** (CGI >=2 kb) | **1.18x** | **0.19 n.s.** |
| flanks (+/-5 kb) | 1.27x | **0.020** |
| distal (20-50 kb) | **1.65x** | **0.003** |

> ### **"DNMT1 and DNMT3A act on DIFFERENT COMPARTMENTS" (F-R080/81/82) is WITHDRAWN.** Territories overlap.
> What is true: **Dnmt1 methylation is un-enriched at canyon cores and rises monotonically with distance from
> them.** **"Lower DNMT3A, preserve DNMT1" can no longer rest on territory — it rests on enzyme function
> (de novo vs maintenance) and on the phenotypes (`Dnmt1^ΔPrx1` bone <50% vs `Dnmt3a` het longer). Those hold.**

### (c) THE LIABILITY IS REAL IN HUMANS — GWAS PLEIOTROPY
161 DNMT3A SNPs pulled from GWAS Catalog: **47 body-height associations, 4 heel-BMD. One SNP carries both.**

**rs13002567 — chr2:25,242,851, INTRON VARIANT OF DNMT3A (distance 0; next gene 33 kb):**

| trait | allele | beta | direction | p |
|---|---|---|---|---|
| **body height** | **C** | 0.0376 | **decrease** | **1e-300** |
| body height (repl.) | C | 0.0346 | decrease | 3e-38 |
| **heel bone mineral density** | **T** | 0.0197 | **decrease** | **3e-24** |
| bone tissue density | T | 0.0200 | decrease | 2e-23 |

> ### **The height-INCREASING allele (T) is the bone-density-DECREASING allele.** Bell-Hensley's mouse
> phenotype — longer bones, weaker bones — **reproduced in humans on COMMON variation, not dominant-negative
> missense.** **F-R082 hoped the cortical penalty was an allele-class artefact. It is not. The trade-off is
> intrinsic to the axis.**
>
> ### **Which makes F-R078's CCN2 pairing LOAD-BEARING, not optional:** CCN2 is at the **97.9th percentile**
> in human growth plate and is the one agent measured to raise **cortical thickness AND mineral content while
> lengthening bone.** **The liability is real and its counter is already in the stack and already expressed
> in the right tissue.**

*Caveat: POMC is 74 kb away; no formal colocalisation performed.*

### (d) **F-R084 — ALL THREE RESOLVED**

**1. POSTNATAL WINDOW — answered.** Mouse `Dnmt3a^R878H/+` is *"normal weight and size at birth"*, weights
**identical before 100 days**, longer femurs at 210 d; plate thicker at **P27**. **The entire phenotype is
acquired postnatally.** Human: both TBRS girls were **still growing at a raised setpoint at 10-13 y** and
needed treatment to stop. **Counterweight:** a documented **post-zygotic MOSAIC DNMT3A carrier** (identified
because **4 of his 14 offspring have TBRS**) is **NOT tall — 32nd percentile** (epigenetic age +23% vs ~40%
in full carriers). **⇒ The constraint is TARGET ENGAGEMENT FRACTION, not developmental timing.**

**2. HEIGHT/DENSITY SEPARABLE — YES.**
- **The bad news first:** IMPC **`Dnmt3a^tm1b` TRUE NULL het** — Bone Area F 8.754→8.399 **p=3.8e-05**;
  **BMC F 0.4274→0.4078 p=5.6e-04, M 0.4534→0.4429 p=0.039 (BOTH SEXES)**. Weaker `tm1a` allele: nothing
  (p=0.54, 0.91) — internal dose-response. **Three allele classes now agree (missense mice, human common
  variation, true null). The trade-off is INTRINSIC to DNMT3A.**
- **But it is NOT a law of skeletal biology.** Genome-wide **rg(height, bone area) = 0.064 (spine), 0.14
  (hip)** — near-independent. And direct: **ACAN 190 mapped SNPs, dense height signal, ZERO bone-density
  associations. CCN2 the same.** vs **DNMT3A: 47 height + 4 BMD, one SNP carrying both in OPPOSITE
  directions.**
> ### **Separability is demonstrated. The liability is DNMT3A-specific, and CCN2 is the counter on TWO independent grounds — a height locus with no BMD penalty in human genetics, AND the one agent measured to raise cortical thickness and mineral content while lengthening bone (F-R078).**

**3. SETPOINT + DEADLINE ADDITIVE — YES, 47,XXY ALREADY RUNS BOTH.**
**SHOX x3** (setpoint) + **hypogonadal delayed epiphyseal closure** (deadline) → **+5 to +7 cm**, on
*"normal circulating IGF-1 and IGFBP-3"*. **Separable in time:** height excess present **at ages 4-12, before
fusion matters** (SHOX arm alone); **increased LEG length** from delayed closure (deadline arm on top).
**This is the stack's exact architecture, occurring naturally and working.**

> ### **NEW CONSTRAINT:** a 47,XXY man also carrying heterozygous **ACAN** c.7141G>A reached **151.6 cm
> (−2.8 SDS)** with **bone age 17 y and plates FUSED at chronological 16 y 2 m**. **ACAN haploinsufficiency
> advanced bone age and closed the plates DESPITE Klinefelter hypogonadism.** **The deadline arm is NOT
> unconditional — a matrix defect forces fusion through it.** So **CCN2 protects the deadline arm as well as
> the cortex**, and anything degrading matrix sabotages both.

### ⚠️ THE FLAW I NEARLY MISSED
IMPC's true null shows the **bone deficit WITHOUT the length gain**, and **Tatton-Brown 2014 wrote *"a simple
haploinsufficiency model appears unlikely"***. **Had that stood, a DNMT3A INHIBITOR would be the wrong tool
entirely.** **Refuted by four human truncating alleles:** c.934_937dupTCTT **+3.2 SD**; p.Arg320* **+3.2
SDS**; p.G587fs **+3.77 SD**; p.Arg771* **+2.42 SD**. **Haploinsufficiency IS sufficient in humans; an
inhibitor is viable.** The mouse discrepancy is the n=8 power problem Tatton-Brown himself named.

### (d-old) WHAT COULD NOT BE SUBSTITUTED FOR AS OF F-R083 (now resolved above)
1. **Whether POSTNATAL DNMT3A reduction reproduces the phenotype.** All human+mouse data is germline. TBRS is
   overgrown by age 3; the mouse diverges only after 100 days. **Unresolvable from existing data, and the most
   important unknown in the arm** — a postnatal intervention is the only usable kind.
2. **Whether height and bone density are separable.** They travel together at rs13002567. CCN2 is the proposed
   counter; **the combination has never been tried in any organism.**
3. **Whether removing the deadline (F-R065 oestrogen) and raising the setpoint (DNMT3A) are additive.** Both
   established separately in humans; **the combination has never existed.**

## -1a-0. **THE CLOCK AND THE HEIGHT LEVER ARE THE SAME MOLECULE (F-R082)**

**Jackson lab, *Nat Genet* 2026;58:1632 — the causal experiment the pacing law never had.**

They built a clock from the **2,646 CpGs that DNMT3A gain-of-function hypermethylates** and tested it against
the **332 Horvath clock CpGs** in **5,085 people (Generation Scotland)**. The HESJAS sites track age
*"**performing just as well as the CpGs used to derive Horvath's**."*

> ### **The sites DNMT3A hypermethylates ARE the sites the epigenetic clock reads.** The clock is not a
> passive correlate of time — it is substantially **a record of DNMT3A activity at Polycomb domains**, and
> that activity **causally reduces stem-cell output**. *"Age-related gains in DNAme predominantly occur
> within Polycomb-marked domains"*; *"methylation at DMVs… accumulates in a time-dependent manner."*

**THE GROWTH PLATE READS IT IN BOTH DIRECTIONS, IN MICE:**

| | **DNMT3A LOSS** (Bell-Hensley, *Bone* 2024) | **DNMT3A GAIN** (Jackson 2026) |
|---|---|---|
| **growth plate** | **THICKER** (both R878H, P900L; not zone-specific; PCNA unchanged) | **THINNER** (10-12 mo) |
| **bone length** | **longer femur** (Smith, n=4, 210d); tibia small but significant | **postnatal growth failure** |
| trabecular | — | **osteoporosis at 6 mo** |
| lifespan | — | **12.8 mo vs 26-29 — HALVED** |

**Plate thicker + PCNA unchanged ⇒ the gain is in `v(d)` or duration, NOT flux.**

**Human mirror complete at the methylation level:** Smith 2021 WGBS, 11 DOS patients — **focal HYPOmethylation,
2,209 DMRs (R882) / 332 (non-R882), ALL hypomethylated**, worked example **the HOXB cluster**. Heyn found
**Hoxc13 HYPERmethylated** in GOF mice. **Same Polycomb class, opposite directions, opposite growth.**

### ⚠️ THE LIABILITY — LONGER BONES, WEAKER BONES

`Dnmt3a` mutant mice: **thinner cortical bone** (femur AND tibia), **significantly lower stiffness, yield
load, maximum load**; **normalised: reduced Young's modulus, yield stress, ultimate stress** — a **material**
deficit, not just geometry. Brittleness, tissue mineral density, osteoblast activity and osteoclast number
all **unchanged** — mechanism unresolved. Authors recommend **bone density and quality testing in patients**.

> ### **This is §3.6's mechanical ceiling INSIDE the DNMT3A lever — and it makes F-R078's CCN2 finding
> load-bearing:** CCN2 over-expression raised **cortical thickness (0.060 vs 0.049 mm) and mineral content
> (1.36 vs 1.10 mg/mm)** while lengthening bone. **The same variables, opposite signs. CCN2 is the measured
> counter to the measured liability.**

**Caveat that may dissolve it:** these are **missense** alleles (R878H is a **dominant negative**), and the
authors note prior work where *"partial loss of Dnmt3a may **increase** cortical thickness."* **True
haploinsufficiency may carry no cortical penalty, and nobody has compared nonsense vs missense skeletons.**

### THE TWO ENZYMES ARE NOT SYMMETRIC
**`Dnmt1^ΔPrx1` at 16 weeks: bone length LESS THAN HALF of control.** `Dnmt3a` het: *"small significant
increase."* **"Preserve DNMT1" is a hard constraint; "lower DNMT3A" is a titratable gain.** Any global
hypomethylating agent (azacitidine, decitabine) trades a catastrophic loss for a modest gain.

### WHAT IT DOES NOT DELIVER
**TBRS patients reach +3.0 SD and STOP.** DNMT3A loss **raises the setpoint and the rate; it does not remove
the endpoint.** **The endpoint is F-R065's arm — oestrogen ablation prevents fusion in humans (ESR1-null man
growing at 28.5; aromatase-null at 31).** **DNMT3A raises the ceiling; oestrogen ablation removes the
deadline. Neither alone is unbounded; together they are the closest to the three-term goal.**

### TENSION, NOT SMOOTHED OVER
Heyn 2019: hypermethylation skews progenitors *"towards differentiation away from self-renewal"* (pool
depletion, `a > b`). Jackson 2026, same lab, better powered: *"**HSC and early progenitor numbers remain
constant**… Polycomb-target genes are **not de-repressed**… could **impair transcriptional activation
dynamics** during differentiation."* **Number preserved, output reduced — that is flux, not `n0`. The two
papers disagree and the later one says output.**

## -1a. **DNMT3A — A HUMAN GENE WHOSE LOSS GIVES +3.0 SD OF HEIGHT (F-R080)**

**The strongest lead in the programme. Bidirectional, human, monogenic, and the loss direction is the tall
one — which means an INHIBITOR is the intervention.**

| direction | phenotype |
|---|---|
| **loss of function** (TBRS, OMIM 615879) | **tall stature, mean +3.0 SD** (first 13 patients); **height ≥+2 SD in 83% (44/53)** of the 55-patient cohort; one girl required **bilateral epiphysiodesis to STOP growth** |
| **PWWP gain of function** (Heyn, *Nat Genet* 2019) | **microcephalic dwarfism**, via **hypermethylation of Polycomb DNA-methylation valleys with depletion of H3K27me3 and H3K4me3 bivalent marks**; `Dnmt3a^W326R/+` dwarf mice |

**The epiphysiodesis case (*Front Endocrinol* 2021), c.958C>T p.Arg320\*:** +2.9 SDS at 3y3m; at 12y2m
**172.5 cm (+2.8 SDS) with BONE AGE 12y — NOT advanced**; PAH 187.1 cm; epiphysiodesis at 12y9m;
**final height 187.4 cm (+3.2 SDS)** at 19y6m. Post-surgery: legs +1.7 cm, sitting height +10.9, arm span +20.5.

> ### **The compartment is the one F-R070 already identified** — Polycomb/bivalent H3K27me3+H3K4me3, the class Lui measured H3K4me3 falling at. **DNMT3A's substrate is that compartment; DNMT1's is not (F-R079: 95.9% outside promoters/islands).**

### THE RESOLUTION — two enzymes, two compartments, OPPOSITE height signs

| | **DNMT1** | **DNMT3A** |
|---|---|---|
| role | maintenance | de novo |
| compartment | 95.9% gene body/intergenic | Polycomb valleys / bivalent promoters |
| **loss** | **SHORT** (`Dnmt1^ΔPrx1`; human *DNMT1*–Height in MSK-KP) | **TALL, +3.0 SD** |
| **gain** | untested | **dwarfism** |
| OSK | **never measured** | **decreased** |

> ### **TARGET: LOWER DNMT3A, PRESERVE DNMT1.** Azacitidine/decitabine are **exactly wrong** — nucleoside analogues trap all DNMTs including the one that must be kept. **Selective non-nucleoside DNMT3A inhibitors exist** (selectivity determinant: **Asn1192** in DNMT1 abolishes affinity). Chemical probes, not drugs — but the selectivity axis is solved.

### SOTOS vs TBRS — the contrast is the whole programme

| | **Sotos (NSD1)** | **TBRS (DNMT3A)** |
|---|---|---|
| bone age | **ADVANCED** | **not advanced** (n=1) |
| adult height | **"upper limit of normal"** — men 184.3, women 172.9 cm | **+3.2 SDS retained**, growth to 19y6m |

> **Sotos = grow fast, mature fast, end normal — the failure mode since F-R024. TBRS = grow fast and the
> skeletal clock does not run with it.** **DNMT3A loss appears to decouple rate from maturation; NSD1 loss
> does not.**

### **F-R081 — THE DECOUPLING NOW RESTS ON THREE PATIENTS, NOT ONE**

| patient | age | height | **bone age** | advance |
|---|---|---|---|---|
| **Japanese** (Miyoshi, 17-yr) | **10y7m** | **166.4 cm, +3.77 SD, Tanner 4** | **11.1 y** | **+0.5 y** |
| **Swedish** (Lennartsson) | 12y2m | 172.5 cm, +2.8 SDS | **12.0 y** | **−0.2 y** |
| Chilean (Martin) | 8y10m | +2.42 SD | 13 y | +4.2 y |

**+3.77 SD and Tanner 4 at ten-and-a-half with a bone age of 11.1** is the strongest single observation in
the branch. **The Chilean counterexample is disarmed by its own authors:** his **non-carrier sister** also had
advanced bone age (13y at 10y7m), *"raises the possibility that there are other familial factors"* — it
segregates independently of DNMT3A. And they state advanced BA *"has not been reported frequently in TBRS."*

**Fourth line, from the surgeons:** Greulich-Pyle *"**underestimated the amount of remaining growth**…
not validated for individuals with specific growth syndromes."* **These children have more growth left than
their skeletons say.**

### **AND THE OVERGROWTH IS NOT ENDOCRINE**
Japanese case at +3.77 SD: **IGF-1 325 ng/mL (+0.22 SD)**, *"Serum GH and IGF-1 levels were not elevated."*
Chilean: IGF-1 normal. **DNMT3A runs at +3 SD on a normal somatotropic axis — genuinely ORTHOGONAL to the GH
arm, and intrinsic to the tissue.**

### **BOTH TBRS GIRLS NEEDED TREATMENT TO STOP GROWING**
Japanese: **oral oestrogen 10.8→13.6 y to induce fusion** → 176 cm at 26. Swedish: **bilateral
epiphysiodesis at 12y9m** → 187.4 cm (+3.2 SDS). **Two countries, two deliberate forced-fusion
interventions, both still finished above +3 SD.**

### Heyn 2019 read in full — the mechanism IS the branch's pool axis
`Dnmt3a^W326R/+` mice: *"viable, healthy… **proportionately small with significantly reduced body and brain
weight**"*; in vivo hypermethylation at Hoxc13/Sox1. **The sentence:** *"hypermethylation of DMV/DMRs could
lead to a **skewing of stem/progenitor cells towards differentiation away from self-renewal**."* **That is
`a > b`, reached independently.** Also: *"**NSD1, DNMT3A and EZH2 are both height QTLs**"*; PHC1 mutation
gives microcephalic dwarfism. Conclusion: *"the interplay between DNA methylation and polycomb… as a
**determinant of organism size in mammals**."* **Limit: mouse phenotype is body WEIGHT; bone length not measured.**

**Tatton-Brown 2014 verified at the primary:** *"Height was increased in **all** individuals ranging from
**1.8 to 4.2 (mean 3.0)** SD… head circumference **1.2 to 5.1 (mean 2.5)**."*

### THE PACING LAW IS CONFIRMED IN HUMANS (Jeffries, PMC6633263, Horvath clock)

| syndrome | growth | epigenetic age acceleration |
|---|---|---|
| **TBRS** (*DNMT3A*) | overgrowth | **~+40%**, ANCOVA **P=0.004** |
| **Sotos** (*NSD1*) | overgrowth | **~+40%**, **P=6.4e-9** |
| **Kabuki** (*KMT2D*) | growth deficiency | **~−40%**, **P=0.023** |

> ### **Overgrowth → fast clock. Growth deficiency → slow clock.** **This REFINES F-R077:** the clock is not
> "chronologically paced" — it is paced by **growth accomplished**, not pubertal stage or bone age. CPP girls
> are **early, not overgrown**, so F-R077's null is exactly what the law predicts. *(Excluding the p.Arg882Cys
> ">800%" outlier — Arg882 is the clonal-haematopoiesis allele.)*

## -1b-FINAL. THE OSK DIRECTION PROBLEM IS **REFUTED** — REPROGRAMMING RAISES DNMT1 (F-R081)

**Su et al., *Eur Rev Med Pharmacol Sci* — senescent Integrin-a6^high CD71^high epidermal stem cells, transient
OSKM. The only direct measurement of DNMT1 after partial reprogramming that exists:**

> *"partial reprogramming **increased DNMT1 mRNA expression** in senescent ESCs, but had **no effect on TET1,
> TET2, and TET3**… we verified that partial reprogramming **significantly increased the DNMT1 PROTEIN
> expression**."* And *"young ESCs also had a **higher** mRNA expression of DNMT1 compared to senescent ESCs."*

**DNMT1 falls with senescence; reprogramming restores it. Effect persists 2 weeks after withdrawal.**
Their mechanism sentence is `Dnmt1^ΔPrx1` in another tissue: *"**DNMT1 is essential for the preservation of
the progenitor state**… lack of DNMT1 would result in severe defects in **proliferation and self-renewal**."*

> ### **F-R079's hazard predicted OSK would lower maintenance methylation and shorten bone. The measurement says DNMT1 goes UP. REFUTED, not downgraded.**
>
> ### **And the structural correction matters more:** methylation age fell **while DNMT1 rose, in the same
> cells**. **Rejuvenation is NOT global demethylation.** F-R069, F-R072 and F-R079 all implicitly equated
> them. **Partial reprogramming raises the maintenance writer AND lowers the de novo writer at Polycomb
> targets (F-R080) — both height-positive.**

**Limits:** epidermal stem cells not chondrocytes; **OSKM with c-Myc** vs the cartilage study's OSK without;
n=3; low-tier journal. **Direction clear, weight behind it thin.**

## -1b-OLD-3. THE OSK DIRECTION PROBLEM — DOWNGRADED, WRONG ENZYME (F-R080, superseded above)

**F-R080 read the OSK primary. The only methyltransferase antibody in it is DNMT3a (ab188470).**
*"post-OSK treatment, **DNMT3a** levels were noticeably declined."* **"DNMT1" occurs twice in the whole
paper, both citing the OA disease state — it was NEVER measured after OSK.** F-R069's "DNMTs down" should
have read **"DNMT3a down"** — and DNMT3A loss is the **height-POSITIVE** direction. **Hazard downgraded from
likely to unmeasured-and-probably-the-wrong-enzyme. Not withdrawn: DNMT1 after OSK is still the discriminator.**

**ALSO CORRECTED:** F-R069 reported OSK reducing cartilage methylation age. The authors: *"the limited sample
size in our study **precludes the attainment of statistical significance**."* **Not a measurement.**

## -1b-OLD-2. THE OSK DIRECTION PROBLEM AS STATED IN F-R079 (superseded above)

**F-R072 dissolved it on the grounds that Nilsson's assay was bulk. There is now a site-resolution map, a
conditional knockout, a mechanism and a human association. THE DISSOLUTION BELOW IS RETRACTED.**

**Yanagihara et al., *Nat Commun* 2025 (GSE270641, MBD-seq, mouse chondrocytes P3–5).** `Dnmt1^ΔPrx1`:
long bones **significantly shortened**, *"decreased chondrocyte proliferation and accelerated
differentiation"*; **Dnmt1/Uhrf1 localise to the PROLIFERATIVE zone**; at 1 wk proliferative area smaller,
BrdU⁺ lower, **hypertrophic and mineralised areas WIDER**; at 6 wk **loss of growth plates**, delayed SOC.

> *"DNA methylation **maintenance in proliferating chondrocytes** and **demethylation of DNA in hypertrophic
> chondrocytes** is essential for bone elongation."*

> ### **Demethylation IS the differentiation signal in the plate.** Less maintenance methylation → premature
> hypertrophy → shorter bone. **Human anchor: *"In the Musculoskeletal Knowledge Portal, Dnmt1 is
> significantly associated with Height."***

**F-R069 records OSK's cartilage mechanism as "DNMTs down, TET2 pivotal" — the height-negative direction.**

**My own analysis of the deposit (`frontier/analysis/GSE270641/`):** **95.9% of Dnmt1-dependent methylation
is OUTSIDE promoters/CpG islands** (promoters 2.7% obs vs 2.5% shuffled = **1.07×, no enrichment**; CpG
islands 1.7% vs 0.7%; gene bodies 53.8% vs 42.0%; intergenic 45.8%). **So the MARKS are in a different
compartment from OSK's CpG-island/bivalent target class (F-R070) — but the ENZYME is shared.** Compartment
separation does not protect against a global reduction of the writer.

> ### **NAMED HAZARD: AAV-OSK in a growing animal may phenocopy `Dnmt1^ΔPrx1`.** The published OSK cartilage
> work was **adult articular cartilage for OA — no growth plate.** **Nobody has run OSK with open physes.**
> **Discriminator: measure DNMT1 protein in proliferative-zone chondrocytes after OSK, alongside bone length.**

**And the untested direction is the interesting one:** the paper never tests Dnmt1 **over**-expression.
**Raising maintenance methylation should hold cells proliferative longer** — same shape as F-R072's
dexamethasone banking result, same cost.

**Data-quality note:** the deposited file is **missing chr7, chr8, chr9, chrX entirely** (76% genome
coverage). **RESOLVED IN F-R080 by pulling the raw runs.** No SRA toolkit, aligner or samtools in this
environment and 55 GB of FASTQ against 27 GB of disk, so I built a **repeat-masked 32-mer index** of the
target loci and **streamed reads from ENA without writing them to disk** (8M reads/run, SRR29528354-59).

**Validation:** the `Dnmt1` locus is the **only** one that FALLS in raw counts (0.58x) while everything else
rises — that is the **floxed-exon deletion itself**, detected in the correct three samples. The gene desert
rises **4.6x** in cKO (MBD pulldown specificity collapses as methylation is lost), so raw counts need the
desert as reference. **`Hhip` returns a clean null (4.31x vs 4.61x background), so the assay can say "no."**

**Result — the omitted genes ARE Dnmt1-dependent** (desert-normalised, Welch, n=3v3):
**Acan 0.43x p=0.015**; **Cyp19a1 0.53x p=0.012**; Igf2_H19 0.43x p=0.014; Cdkn1c 0.54x p=0.023;
Mkrn3 0.54x p=0.040; Gpc3 0.61x p=0.0003; Peg3 0.40x p=0.057. Known positives from the deposit rank at the
top (Dlk1 0.24x p=0.002, Meg3 0.26x p=0.007). **One positive control failed: Nnat 0.73x p=0.22.**

> **The matrix gene (`Acan`, F-R078) and the aromatase gene (`Cyp19a1`, the closure arm) both carry
> Dnmt1-dependent methylation in chondrocytes.** Not evidence that methylation controls their expression —
> evidence that **the methylation layer sits upstream of both the matrix term and the closure term.** **Dlk1–Dio3 domain enrichment is
2.38×, permutation p = 0.059 — NOT significant** (my first-pass Poisson p = 3.6e-19 used the wrong null).

## -1b-OLD. THE DIRECTION PROBLEM FOR OSK — dissolved (F-R072) — **RETRACTED BY F-R079 ABOVE**

| | direction |
|---|---|
| growth-plate senescence (Nilsson 2005, in vivo, global) | **methylation LOST** |
| OSK in chondrocytes (F-R069) | **DNMTs down, TET2 up = drives DEmethylation** |

**The methods section settles it.** Nilsson's assay is headed *"Assessment of **global** DNA methylation"* —
**MspI/HpaII isoschizomer digestion at CCGG sites, 32P end-labelling, TLC**, reported as one genome-averaged
percentage. **Zero site resolution.** It cannot distinguish global hypomethylation from focal PRC2-target
hypermethylation, **so it cannot conflict with the clock data or the PRC2 convergence.** Objection withdrawn.

**And the same assay contradicts itself across contexts:** growth plate in vivo **decreased**; **liver in
vivo INCREASED (P<0.001)**; **cultured RZ chondrocytes INCREASED +0.21%/population doubling (P=0.012)**.
A measure that moves in opposite directions by tissue and in vitro/in vivo is a context-dependent aggregate,
not a clock.

## -1c. DELIVERY — exhausted, gap confirmed and sharpened (F-R071)

**AAV reaches the growth plate only by the route that does not help.** **AAV8-CNP works** — increased
chondrocytes, both PZ and HZ heights up in ACH mice — **but CNP is SECRETED**: the vector transduces liver
or muscle and the protein circulates. **It never transduces a growth-plate chondrocyte.** **OSK is
cell-autonomous and must be inside the target cell.** The entire successful AAV-skeletal literature routes
around exactly our problem. **No serotype characterised for direct resting-zone transduction.**

## -1c-ii. THE CHEMICAL ROUTE: solves delivery, fails in vivo (F-R073)

**7c** = CHIR99021, DZNep, forskolin, TTNPB, valproic acid, Repsox, tranylcypromine. **2c** = Repsox +
tranylcypromine. **No vector — so no serotype problem.** And **four of seven map onto axes this branch
derived independently**: **CHIR99021** (GSK3beta -> Wnt = half of KY19382), **DZNep** (EZH2 = the PRC2
axis), **Repsox** (TGF-beta = F-R034's "low WNT and TGF-beta" niche), **tranylcypromine** (LSD1).
*Flag: TTNPB is an RAR agonist and retinoic acid suppresses chondrocyte identity — plausibly adverse.*

**But in vivo it fails** (PMC12835892, 7c by osmotic minipump x1 month): **lipid droplet accumulation in
liver and kidney, abnormal mitochondrial morphology, acute kidney injury** — and **2c was WORSE than 7c**.
The same paper: *"partial reprogramming with **OSK alone has been shown to avoid these toxicity
challenges**, whilst still... extend[ing] lifespan in wild-type mice."*

> **The trade is not in the chemical route's favour. Chemical solves delivery and creates systemic
> toxicity; AAV-OSK avoids toxicity and has a delivery problem. A screening problem beats a mechanism
> problem — AAV-OSK stays.**

## -1c-iv. DELIVERY: SOLVED (F-R074)

**The intra-epiphyseal route is published and works.** Zhang 2015, rabbit femoral head (an epiphysis with
an SOC): *"the greater trochanter of the femoral head was **drilled into the subchondral bone region using
a 1-mm Kirschner wire** without crossing the boundary surface of the femoral head cartilage under x-ray
perspective inspection. Then, the **rAAV virus variants (5.5 x 10^11 vp/mL) were injected into the
decompression region of the femoral head (25 uL per side)**."* **Expression confirmed at 12 weeks.**
Corroborated by AAV-anti-miR-214 work in femoral-head osteonecrosis and local rat bone.

> **The objection was mis-specified all along. It was never "AAV cannot reach that compartment" — it was
> "everyone injects into the joint because everyone is treating articular cartilage."** Change the needle
> position and the compartment is accessible. **The human analogue — core decompression — is a routine
> orthopaedic procedure.**

**What remains:** these targeted necrotic femoral-head bone, not the physis. **Whether vector in SOC marrow
diffuses into the adjacent resting zone is untested — but that is a millimetre-scale diffusion question on
an existing surgical model, not an inaccessible compartment.** *Caveat: drilling near an open physis risks
iatrogenic bone-bridge formation, the exact lesion we are avoiding.*

**SUPERSEDED — the original proposal, now shown to have precedent:** every cartilage tropism study is **intra-articular**
because the target was always articular cartilage. **But the resting zone's neighbour is the SOC —
vascularised bone with marrow.** **Intra-epiphyseal delivery into the SOC puts vector on the correct side
of the barrier that defeats intra-articular injection.** Needs no new vector, only a different needle
position and a tropism readout.

**PRECISION CORRECTION (F-R073):** **LSD1/KDM1A demethylates H3K4me1/me2, NOT me3; KDM5A-D does me2/me3.**
Lui measured **me3**, so **KDM5 inhibition remains the specific tool** — tranylcypromine acts one state
below. **But tranylcypromine earns a place independently: it raises bone mass in mice via LSD1 derepressing
BMP2 and WNT7B -> mTOR signalling** — **mTOR is Newton's pool-expansion axis** — **and it is an approved
human drug.**

## -1c-iii. THE CLOCK IN THE GROWTH PLATE: confirmed absent (F-R073)

| dataset | covers | why it fails |
|---|---|---|
| Nilsson 2005 | rabbit plate, fetal/4wk/16wk | **bulk CCGG, no site resolution** |
| human cartilage development methylome (PMC11639090) | ~700,000 CpGs, 72 samples | **FETAL ONLY, 7-21 post-conception weeks**; articular |
| adult chondrocyte clock | adult articular | no growth window |
| Petkovich (PMC5578459) / Stubbs (PMC5389178) | validated mouse clocks, open | **never applied to growth plate** |

**AND THE CLOCK ALREADY ENCODES GROWTH-PACING (F-R074).** Horvath's clock applies a **logarithmic
transformation below age 20 and linear above**: *"the tick rate was **exponential between 0 and 20 years
old**, after which it continued linearly"*; *"the rate of change of epigenetic ages is roughly the **inverse
of the chronological age**."* **The clock ticks fastest when growth is fastest, decelerates as growth
decelerates, and goes linear at about the age growth stops.** That is the growth-pacing shape — as a
**fitted empirical necessity**, because a linear model does not fit children. *(Shape correspondence, not
causal proof: growth co-occurs with everything else developmental, and these clocks are mostly blood-trained.)*

## -1c-v. THE PACING LAW NOW HAS HUMAN COHORT SUPPORT (F-R075)

**Simpkin et al., *Int J Epidemiol* 2017;46:549 — ALSPAC, n=1,018**, methylation at birth / 7 y / 15-17 y.
**Epigenetic age acceleration at age 7, per 1 year:**

| outcome | effect |
|---|---|
| **average height across childhood** | **+0.23 cm** (0.04-0.41, **p=0.018**) |
| **subsequent height growth velocity** | **-0.031 cm/yr** (-0.057 to -0.005, **p=0.021**) |

> ### Epigenetically **older** at seven = **taller already, then growing more slowly.** The budget model made visible. **The opposite-sign pattern is the discriminator:** nutrition/SES confounding makes children taller AND keep growing well — **same sign**. A drawn-down conserved quantity gives **opposite signs**, which is what is observed.

**Honest counterweights:** age at **peak height velocity is NULL** at all three timepoints (r=0.006/0.014/0.014)
— defensible, since PHV is a *timing* variable and pacing concerns a *cumulative* one, but that is my
argument not the authors'. **And fat mass shows the same opposite-sign pattern** (+1,321 g average, -112.5
g/yr trajectory), which **weakens skeletal specificity**. Effect sizes are small; blood, not plate.

**Three independent supports now:** Lui's tryptophan experiment (direct, rat, multi-organ), Horvath's
log-below-20 structure (fitted necessity), ALSPAC (human, correct signature). **Supported, not proven.**

## -1c-vii. TWO MORE HUMAN DATASETS — ONE REPLICATES, THE ONE EXPERIMENT SPLITS (F-R076)

**EPOCH, n=135, methylation at 10.4 y** (*Sci Rep* 2024) — **independent replication of the rate/timing
split I argued in F-R075:**

| | extrinsic EAA (Hannum) | intrinsic EAA (Horvath) |
|---|---|---|
| **peak height velocity** | **beta 0.018 (0.008-0.028), p=0.0008** | 0.011, **p=0.22** |
| **age at** peak height velocity | -0.0022, **p=0.067** | -0.0029, **p=0.12** |

**Rate associated, timing null — as predicted.** *Against it:* significant only on the **cell-composition-
sensitive** extrinsic measure; **intrinsic (Horvath) null.** SAT explains 8.4%. Authors call the effect small.

**The only INTERVENTIONAL dataset (n=10, GHD children, rhGH 0.025-0.035 mg/kg/day, 6 mo, 5-CpG forensic
predictor):**

| | baseline | 6 mo | p |
|---|---|---|---|
| height velocity | 3.9 cm/y | **8.7 cm/y** | **<0.0001** |
| IGF-1 | 120.5 ug/L | **341 ug/L** | 0.0076 |
| **epigenetic age acceleration** | +0.92 y | **-0.92 y** | **0.179 NS** |
| EAA adjusted for IGF-1 | | **-4.137 y** | 0.0295 |
| **IGF-1 -> age acceleration** | | **beta 0.011** | **0.0260** |

> **Velocity doubled and raw EAA FELL — against pacing, but non-significant at n=10. IGF-1, the mediator of
> the growth, was POSITIVELY associated with acceleration — for pacing.** The one experiment supplies one of
> each. **n=10, single arm, no control, and not a validated clock. It settles nothing and names the
> experiment.**

**Ledger: four for, two against.** *For:* Lui tryptophan; Horvath log-below-20; ALSPAC opposite-sign;
EPOCH rate/timing split. *Against:* EPOCH intrinsic-null; GH raw EAA direction.
**SUPERSEDED IN BLOOD BY F-R077 — see -1c-viii.**

## -1c-viii. I RAN THE CLOCK MYSELF. IN BLOOD IT IS CHRONOLOGICALLY PACED (F-R077)

**ArrayExpress E-MTAB-13950** (Palumbo 2024, public, EPIC, 45 samples) is a 2x2 separating chronological age
from developmental stage:

| group | n | chron age | Tanner | bone age |
|---|---|---|---|---|
| CT_PP pre-pubertal controls | 14 | 7.83 | 1 | - |
| **CPP** | **19** | **7.83** | **2 (2-3)** | **+1.69 +/- 1.00 y ADVANCED** |
| CT_P pubertal controls | 12 | 14.55 | 3 (2-4) | - |

**I computed Horvath 2013 (326/353 probes) and Horvath skin&blood 2018 (381/391) directly from the betas.**

| | CPP - CT_PP (same age, +1.69 y bone age) | 95% CI | p |
|---|---|---|---|
| Horvath 2013 | +0.417 y | -0.915 to +1.750 | **0.528** |
| **skin & blood** | **-0.016 y** | **-0.649 to +0.616** | **0.959** |

**Positive control both clocks p ~ 1e-4.** Calibration: CT_PP 7.70 vs chron 7.83; CT_P 13.54 vs 14.55.
**Not underpowered** - pooled SD 0.870 y gives 80% power at n=5/group for 1.69 y. Compression-corrected, a
true 1.69 y advance should read +0.84 y; **CI tops out at +0.62, so it is EXCLUDED, not merely unfound.**

**Reciprocal:** CPP vs CT_P (same Tanner, ~7 chron years apart) = **-3.353 y, p=7e-5.**

> ### Match chronological age -> clocks agree. Match developmental stage -> 3.4 years apart. **In blood the clock tracks TIME, not development.**

**Two clock-free confirmations from the same data:** (1) puberty axis built on controls only - CPP score
**+0.204** on a 0->1 scale, **p=0.357**, LOO-stable; (2) Lui's imprinted network (1,299 EPIC probes,
24 genes) - normal puberty moves **CDKN1C, MEIS1, PEG10, SGCE** at q<0.05; **CPP vs age-matched: NOTHING.**

**Also settles Bessa vs Palumbo:** of 8,967 probes moving >10% between control groups, **91% LOSE methylation
at puberty.** Palumbo's direction is right; Bessa's 450K/X-chromosome-dominated DMRs are not.
**And it explains EPOCH:** the only positive there was **extrinsic** (cell-composition-sensitive) EAA;
intrinsic was null, and my two intrinsic-type clocks are null. **The "EAA tracks pubertal development" signal
is most likely leukocyte composition.**

> ### **RETRACTED: F-R074 section 2's "cheapest decisive experiment" (a blood array on an ESR1-null man) and the Suzuki HH IDAT request in `data_request_suzuki_et_al.md`. DO NOT SEND THAT EMAIL.** A blood methylome that does not move for a 1.69-year bone-age advance in 19 children will not resolve delayed fusion in nine adults.
>
> **NOT retracted: Lui's tryptophan result.** That was rat growth plate and organ expression, not a blood
> clock. **The pacing law survives; every cheap blood proxy for it is dead.** The measurement must be made in
> physeal tissue - which makes F-R073 section 3 the only route left, not merely the best one.
**The observational associations replicate; the one manipulation of growth did not reproduce them.**

> **Consequence the branch had not confronted:** IGF-1 is the term that accelerated the clock, and the GH
> arm raises IGF-1 ~3x at **half** the stack's 0.07 mg/kg/day. **If IGF-1 is the pacer, "blast" is the
> accelerant, not neutral.** This does not overturn the blast argument — F-R065 showed the closure deadline
> it was racing is removable — **but it converts a free choice into a measured trade**, and the measurement
> is methylation age before/after GH with a real clock and a control arm.

## -1c-vi. THE HH ARRAY DATA EXISTS BUT WAS FILTERED (F-R075)

**Suzuki et al.** ran **Infinium EPIC on 9 hypogonadotropic hypogonadism patients + 12 controls** (blood) —
the delayed-fusion population. **But:** *"Probes known to show **aging-related** or sex-biased DNA methylation
changes were also **excluded**"* — **their ref 14 is Horvath 2013. They removed the clock CpGs.** No HH
epi-signature was found (clustering did not separate patients from controls).

**Data availability:** *"has not been deposited into a publicly available repository. **Data will be made
available on request**."* **The clock CpGs are present in the raw IDATs — the exclusion was analytical.**
Computing DNAm age on 21 existing samples is a laptop-scale reanalysis. **Corresponding authors: Maki Fukami
and Keiko Matsubara, National Research Institute for Child Health and Development, Tokyo.**
**Must also request chronological ages and androgen treatment status — the paper reports neither, and if the
patients are pre-pubertal the test is underpowered.**

> ### THE CHEAPEST DECISIVE TEST IN THE PROGRAMME: **if growth paces the clock, the log-to-linear inflection should track FUSION and MOVE when fusion moves.** ESR1-null and aromatase-deficient men keep epiphyses open into their thirties. **Their DNAm age should stay logarithmic past 20 and lag chronological age.** If the clock is time-paced it goes linear at 20 like everyone else. **A single methylation array on stored blood from an already-identified patient. No tissue, no animal.**

> **The animal version: resting-zone chondrocytes at a series of postnatal ages through the Petkovich or Stubbs
> clock, asking whether methylation age tracks GROWTH ACCOMPLISHED rather than chronological age.**
> **Falsifiable shape, not just direction:** F-R072 showed RZ labelling collapses 95.6% -> 9.2% between fetal
> and 5 weeks then plateaus. **If the clock is growth-paced, methylation age should advance steeply over
> that same window and then flatten — mirroring the labelling curve, not the calendar.**

**Cyclic vs constitutive, settled (F-R071):** continuous OSKM causes *"rapid sickness... mortality in as
little as 4 days"* **before** teratomas; **cyclic 2-on/5-off ran 35 weeks safely at single copy**, but
**8 cycles at two copies caused teratomas in liver, kidney, pancreas**. **Cyclic OSKM drives proliferation
of beta cells and satellite cells — it works in dividing compartments.** Design must be cyclic, single-copy,
dose-controlled.

---

## -1d. RETRACTED: the 11 pg/mL "threshold" (F-R072)

Since F-R047 the branch treated **11 +/- 2 pg/mL** as the oestradiol level at which RZ self-renewal is
suppressed. **Its actual source:** Schrier gave **estradiol cypionate 70 ug/kg i.m. weekly x2 weeks** and
measured *"serum estradiol... was **11 +/- 2 pg/mL**, compared to **<5 pg/mL** in animals treated with the
vehicle."* **That is one achieved concentration in one experiment. No dose-response. Nothing tested at 7,
15 or 30.** **Two points, not a threshold.**

**Consequence:** the anastrozole-vs-letrozole argument in F-R063/R065 partly rested on which agent "clears
the threshold." **That framing is unsupported.** What survives: less oestrogen is better, both agents get
well below the tested level, and **the decision rests on outcome data** (anastrozole +1.0 vs letrozole
+0.5 cm PAH; velocity and IGF-1 preserved) — where F-R063 landed anyway.

## -1e. THE POOL COLLAPSES BEFORE FIVE WEEKS (F-R072)

**Schrier, RZ BrdU labelling index, distal femur:** fetal **95.6 +/- 0.8%** -> 5 wk **9.2 +/- 1.2%** ->
9 wk 9.2% -> 17 wk 7.6%. **A ten-fold collapse before five weeks, then flat.** RZ cell number per mm also
fell (P<0.001, all regions).

**And the banking dissociation, measured:**

| | RZ labelling index | **RZ cell number** |
|---|---|---|
| **dexamethasone** 0.5 mg/kg/d | decreased (P<0.001) | **INCREASED (P=0.016)**, in the **reserve** RZ (P<0.001) |
| **estradiol cypionate** 70 ug/kg/wk | decreased (P=0.011) | **not affected** |

**Both slow division; only dexamethasone increases cell number.** That is banking vs braking, and it is the
direct evidence behind the per-cycle-cost escape (F-R071).

> **The constraint this creates:** if ~90% of the RZ proliferative collapse precedes five weeks in rabbit,
> pubertal interventions act on an already-mostly-spent compartment. **That raises the value of anything
> that RESTORES over anything that PRESERVES — an argument for the reprogramming arm over the banking arm.**

---

## 0. THE RESET — where "infinite" actually lives (F-R068)

**The counter can be un-counted. Demonstrated in *Drosophila*, and a candidate exists in mammalian
chondrocytes.**

**Fly (the mechanism):** *"Adult ISCs... **receive Delta from EMCs/EEPs to maintain stemness and reset the
division counter**."* Loss-of-function confirms it — Delta RNAi in the differentiated daughters
**significantly reduced stem cell numbers**. **Renewal capacity is conferred by the cell's own progeny, not
intrinsic to it.**

**Mammalian growth plate has the same topology** — Ihh is *"a reverse signal from terminally differentiated
chondrocytes... increasing PTHrP expression in the resting zone."* **But Hedgehog activation MOBILISES
rather than resets:** RZ-confined Ptch1 deletion gives "patched roses," wider columns and plate hyperplasia,
then *"drives resting zone chondrocytes into **transit-amplifying states**... and eventually **converts these
cells into osteoblasts**"* which **leave the plate**. **Pool spending dressed as expansion.** This explains
systemic SAG's failure (activation must be **RZ-confined**; Col2a1-creER did nothing), Haraguchi's slow
+4.5%, and the KY19382 niche-drain risk.

**The reset candidate, now MEASURED (F-R069): OSK partial reprogramming in chondrocytes** (*Exp Mol Med*,
PMC13049178). **AAV2, >1e11 gc intra-articular, OSK constitutive, c-Myc excluded.** They built a mouse
DNA-methylation clock (255 samples, 90 CpG sites, elastic net, calibrated) and ran WGBS on cartilage:
**methylation age reduced vs control, and YOUNGER THAN CHRONOLOGICAL AGE.** DNMTs down, **TET2** pivotal
(siRNA-confirmed), P21 down, **osteogenic conversion counteracted** — directly opposing the Hedgehog export
route above. Identity retained, no stemness gain. The window is independently established: **Lu et al.,
*Cell* 2025 (Altos/Salk)** — partial reprogramming reduces mesenchymal drift *"before dedifferentiation and
gain of pluripotency."*

> **THE LAYER MISMATCH IS CLOSED (F-R070).** *"Convergence of aging- and rejuvenation-related epigenetic
> alterations on **PRC2 targets**"* (*Mol Syst Biol* 2026; open preprint bioRxiv 2023.06.08.544045):
> **poised/bivalent promoters — defined by simultaneous H3K27me3 AND H3K4me3 — gain the greatest entropy
> with age, and "such epigenetic disorder can be reversed upon partial reprogramming treatment."** Their
> age-related DNA-methylation gain is **also** reversed, with *"specific reversal of methylation changes in
> PRC2-target genomic regions."*
>
> **And Lui's eleven growth-plate promoters — Igf2, H19, Plagl1, Mest, Peg3, Dlk1, Gtl2, Cdkn1c, Mdk,
> Meis1, Gpc3 — ARE the PRC2-target bivalent class.** The two layers are two readouts of one process, and
> partial reprogramming reverses both. **KDM5 inhibition drops back to being the alternative route, not the
> primary one.**

> **And two transfer gaps:** articular chondrocytes are non-renewing and load-bearing; growth-plate
> chondrocytes are **consumed** and fed by a niche — **rejuvenating a cell about to die at the junction
> accomplishes nothing (F-R064). The target is the resting-zone stem cells**, and intra-articular AAV2 is
> not obviously the route to them. Also **constitutive, not cyclic** — a different risk profile in a
> proliferating compartment.

**VERIFIED ABSENCE: partial reprogramming has never been applied to a growth plate, a physis, or
longitudinal bone growth.** AAV-OSK has rejuvenated kidney and muscle and extended lifespan in aged
wild-type mice. Cartilage now. Never the physis.

> ### THE DEFINING EXPERIMENT: deliver OSK to the resting zone of an open growth plate and measure longitudinal growth and time to fusion.

**The clock reagents are open and in hand (F-R070):** **Petkovich, *Cell Metab* 2017;25:954, PMC5578459** —
the 90-CpG mouse clock the OSK study trained against, **built explicitly to evaluate longevity
interventions**; plus **Stubbs, *Genome Biol* 2017;18:68, PMC5389178**. **Cheapest decisive test available:
run the clock on resting-zone chondrocytes across ages and ask whether methylation age tracks *growth
accomplished* rather than chronological age.** Lui's tryptophan result predicts it does.

**DELIVERY IS NOW THE REAL GAP (F-R070).** The entire AAV cartilage literature is **articular**: AAV2 best
in arthritic chondrocytes; AAV2/5/6/6.2 substantial in normal and OA; **AAV6 aggravates cartilage
degeneration**; **AAV7/8/9 hit liver strongly even after intra-articular injection**, AAV6 does not.
**But the resting zone sits beneath the secondary ossification centre, fed by epiphyseal vessels, not
exposed to the joint cavity — intra-articular delivery reaches articular cartilage, not obviously a resting
zone behind the SOC** (my inference from the anatomy; untested either way). And F-R068 showed compartment
specificity is **not optional** — Hedgehog worked only when confined to PTHrP+ cells; Col2a1-creER did
nothing.

> **No AAV serotype has been characterised for the growth-plate resting zone. That is the most specific
> unfilled hole in the programme — and unlike the mechanism questions it is a straightforward screen:
> seven serotypes, one reporter, one readout.**

**The architecture, if it holds:**
```
grow  -> clock advances (H3K4me3 erased; methylation age rises)
reset -> clock runs back (OSK, measured)
grow  -> ...
```
**If growth advances a clock and something winds it back, the total is no longer fixed.** "Infinite" stops
being a category error and becomes a question of cycle timing. **Three of six lines are solid, one is
measured on the wrong layer in the neighbouring tissue, and two have never been attempted.**

> **This is the first candidate for the one thing "infinite" requires: clearing accumulated epigenetic
> division memory in a mammalian chondrocyte.** **Not yet done in a growth plate, and no longitudinal-growth
> measurement exists.** That is now the defining experiment of the programme.

**Also settled in F-R068:** the fly counter's "precisely eight divisions" claim is **contested** by a
*Nature* referee (neutral competition confounds the clone analysis — *"a fatal flaw"*), so F-R067's
conservation law is **downgraded from measured to strongly indicated**. Lui's mammalian H3K4me3 decline
stands independently. **KY19382 caveat:** its own reviewer was *"not convinced"* the effect runs through
CXXC5-DVL rather than GSK3beta. **CKR-051 (CK Regeon) completed Phase 1** (NCT05833906, 52 healthy males) —
but **transdermal**, dermatological indication.

---

## 1. THE CLOCK IS A CHROMATIN DIVISION-COUNTER (F-R067) — and this is the governing constraint

***Nature*, "Intestinal stem cells count self-renewal divisions to switch multipotency":** ISCs count
**eight divisions** via *"antagonistic histone modifications: TrxG-dependent active marks (**H3K4me3** and
H3K36me3) progressively **decline**, whereas Polycomb repressive marks accumulate during successive
divisions."* **Same mark, same direction, as Lui's growth-plate programme, in an independent tissue.**

```
growth -> divisions -> H3K4me3 erasure at the growth-gene set -> senescence
```

> **Self-renewal ADVANCES the counter, it does not reset it.** Both daughters inherit the parent's advanced
> state. **So mTORC1 pool expansion buys cell NUMBER, not remaining CAPACITY.** F-R066's 2.5x is real and
> does not by itself buy "infinite."

**Demonstrated: the counter can be PAUSED** (tryptophan restriction delayed the programme; dexamethasone
banks, 88% -> 14% fusion). **Not demonstrated: any reset.** The fly counter resets at division nine, so
resets exist in nature; the mammalian growth-plate reset is unknown.

**Therefore the only target that attacks the counter rather than feeding it is the ERASER.** H3K4me3 is
removed by **KDM5/JARID1**. **CPI-455**: pan-KDM5, **IC50 10 nM**, **>200x selective**, *"elevated global
levels of H3K4 trimethylation."* **KDM5A inhibition is pro-osteogenic in vivo** (rescued bone loss in
osteoporotic mice). **Human direction check: Kabuki syndrome (KMT2D loss = less H3K4me3) -> "precocious
chondrocyte differentiation disrupts skeletal growth" -> short stature.**

> **KDM5 inhibition on skeletal growth is UNTESTED and is now the highest-value experiment in the programme.**

## 1a-0. THE BEST AGENT FOUND: KY19382 / CXXC5 (F-R067)

**Kim et al., *EMBO Mol Med* (PMC6458850).** **CXXC5 is the mediator of oestrogen-induced growth-plate
senescence** — a Wnt/beta-catenin negative regulator binding DVL's PDZ domain, **induced by oestrogen**,
rising in all three zones during senescence, suppressing FGF18/IHH/PTHrP. **Cxxc5-/- mice: oestrogen-derived
senescence abolished, longer tibiae.** **It sits downstream of the receptor — blockable without ablating
oestrogen.**

**KY19382** (CXXC5-DVL IC50 1.9e-8 M; GSK3beta IC50 1e-8 M), **0.1 mg/kg i.p. daily:**

| | 7-wk-old (LATE puberty, already senescing) | 3-wk-old |
|---|---|---|
| plate height | **significantly increased** | increased, every zone |
| **prolif + hypertrophic cells/column** | **BOTH increased, P<0.0005** | increased |
| **TRAP+ resorption foci** | **ELEVATED** | unchanged |
| **10 wk dosing (3->13 wk)** | **tibiae significantly longer, P<0.0005** | no weight/liver/cartilage abnormality |

**Passes the F-R064 test explicitly: TRAP+ resorption ROSE — the plate converts faster, it does not
accumulate.** Raises **both** factors of the identity in the same animals. **19 other pathways unchanged;
effects abolished by Ctnnb1 siRNA.** **No other agent in this branch does this.**

**Tension to watch:** F-R034's niche is WNT-antagonist-high and that state *preserves* the pool; KY19382
activates Wnt globally. Compartmental resolution (WNT-low in niche, high in columns), but **whether chronic
dosing eventually drains the niche is untested** — Newton's vismodegib result is the shape of that risk.

---

## 1a. THE POOL AGENT EXISTS (F-R066) — four rounds of "nothing renews n0" were wrong

**Newton, *Nature* 2019;567:234.** Chondrocyte-specific **Tsc1 ablation** = constitutive mTORC1 activation:

| readout | control | mTORC1-activated |
|---|---|---|
| **EdU+ epiphyseal stem cells/section** | **24.7 +/- 3.7** | **62.4 +/- 7.5, P = 0.014 (2.5x)** |
| PAR3 symmetric in clonal dyads | lower | **higher** — the direct symmetric-division marker |
| multi-columnar clones | — | **increased P3->P90**, *"accelerated expansion of colony-forming cells"* |
| Ki67, pH3 | unchanged | unchanged — **a fate switch, not a rate change** |

**Opposite direction confirms:** Raptor ablation (mTORC1 down) -> *"enhanced loss of clones"*; vismodegib
(Hh block) -> *"forced them to differentiate."* **pS6 is naturally LOW in resting-zone chondrocytes** —
the zone actively holds mTORC1 down to stay asymmetric. **That is the switch.**

> **`a > b` is a directional, measured, druggable axis in an intact mammal.** Oncogenic route: Tsc1/mTORC1.
> Non-oncogenic parallel (F-R034): hypoxia -> GREM1/FRZB/DKK1/SFRP5, converging with chu2026's human root
> niche and trompet2024's Hh-driven Wnt-inhibitory environment.

## 1a-ii. THE CLOCK IS PACED BY GROWTH AND WRITTEN IN HISTONE MARKS (F-R066)

**Lui, *FASEB J* 2010;24:3083.** Tryptophan restriction for 4 wk: *"the genetic program had been **delayed**,
implying that it is driven by **body growth itself rather than age**."*

> **A conservation law: every centimetre grown advances the programme by a fixed amount.** Growing faster
> reaches the same endpoint sooner. This is F-R018's "clock counts divisions," formalised — and the
> mechanism behind catch-up growth and Gafni's banking.

**The substrate is specific: H3K4me3 (activating) significantly DECREASED 1->4 wk in all 3 organs at all 3
promoters** (Mdk, Peg3, Plagl1), confirmed with a second antibody across 11 genes. **H3Ac: no consistent
change. H3K27me3: liver only.** **It is erasure of an activating mark, not deposition of a repressive one.**

> **H3K4me3 is erased by the KDM5/JARID1 demethylases, and KDM5 inhibitors exist.** Blocking that erasure is
> the first concrete named route to holding the programme open. **Untested on skeletal growth.**

**The unbeaten question:** does symmetric self-renewal **reset** the mark, or do daughters inherit it? If
inherited, mTORC1 expansion adds cells without resetting the clock — more cells, same budget each.

---

## 1b. LINK 11 IS SETTLED — and the answer is yes (F-R065)

**In humans, oestrogen ablation prevents fusion. It does not merely postpone it.**

| case | plate status | growth velocity |
|---|---|---|
| **ESR1-null man, age 28.5** (smith2008, read in F-R025) | **never fused**, bone age 15 at 28 | **0.3 cm/yr** |
| aromatase-deficient (maffei2004) | never fused | 1.3 cm/yr |
| aromatase-deficient, age 31 (Akcay) | **all epiphyses unfused** | ~0.83 cm/yr |
| **Wadlow** — GH excess from age 2, never pubertal | could not close | **~5 cm/yr for 9 years, no deceleration** |

**The rabbit misled me for six rounds.** Ovariectomy is not aromatase deficiency — it leaves adrenal
precursors, intracrine CYP19A1 and STS intact. **The human genetic experiments are better evidence.**

**But fusion and senescence are two different endpoints.** Open plate + no drive = 0.3 cm/yr. **Oestrogen
ablation blocks only one of them.** An open plate is necessary, not sufficient.

> **The three-term phenotype is human and its recipe is: block fusion at oestrogen, drive supply hard.**
> Wadlow is the demonstration.

## 1c. Senescence is a PROGRAMME, not damage (F-R065)

Not telomere attrition. A coordinated multi-organ transcriptional schedule — the **imprinted gene network**
(Lui & Baron): **Igf2, H19, Plagl1, Mest, Peg3, Dlk1, Gtl2/Meg3, Grb10, Ndn, Cdkn1c, Slc38a4** declining
together across organs on a time course matching the growth-rate decline. In the plate: **Mest, Dlk1, H19,
Gtl2 fall** while **Cdkn1c (p57KIP2) and Grb10 rise**.

**And the pool genuinely self-renews** — Newton, *Nature* 2019;567:234: at secondary-ossification-centre
formation chondroprogenitors **acquire self-renewal**, forming *"large, stable monoclonal columns."*

> **This converts `n0` from "impossible" to "unsolved," and names targets. Most tractable: DLK1.**

### 1c-i. DLK1 RETRACTED as a capacity lever — and the retraction is good news (F-R076)

**DLK1 has a human loss-of-function phenotype and it is the wrong kind.** Paternal deletion of *DLK1* alone
(14–69 kb, 14q32.2) causes **central precocious puberty and nothing skeletal beyond it** — *"did not
demonstrate additional features of the imprinted disorder Temple syndrome except for increased fat mass."*
Across **17 reported DLK1-defect individuals**, untreated adult heights run **137.8–160.5 cm**, but:

> *"Female patients... who received **regular GnRHa treatment all had reached normal-range adult heights**."*

**A human born with no functional DLK1 reaches normal adult height provided the plate is given time.**
DLK1's entire height effect runs through **pubertal timing**, and delaying puberty recovers **all** of it.

> **So the imprinted network does not gate plate capacity — but the same result is the branch's cleanest
> human demonstration that capacity and duration are separable and DURATION is what costs height.**

**Losing the whole domain (Temple syndrome, mat UPD14) is different and worse** — untreated adults at
**−3.67, −3.41, −2.73 SDS** — but that cohort is 86% SGA and **half the deficit is prenatal**, and the plate
still runs at **7.13 → 11.81 cm/yr** on GH 0.042 mg/kg/day (Brightman 2018, n=6). **A plate missing DLK1 and
GTL2/MEG3 outright is not rate-limited.**

**Mouse dosage, the up direction:** Dlk1 at **2× → embryonic overgrowth**; at **3× → late-gestation lethal**
with oedema and skeletal defects. Real effect, prenatal, window under one doubling wide. Not a lever.

### 1c-ii. CORRECTED AGAINST THE PRIMARIES, AND THE HEIGHT GENE IS PROBABLY MEG3 (F-R077)

**Two softenings.** (1) GnRHa-treated DLK1 girls reached **normal-range but NOT target** height — Dauber
Table 1 shortfalls **−9.5, +1.2, +0.8, −6.0 cm** vs midparental target, mean **−3.4 cm**. "Recovers all of
it" was too strong; it recovers most. (2) **Gomes argues a puberty-INDEPENDENT growth effect** — untreated
DLK1 women mean **−3.1 SD**, worse than historical untreated CPP, and *"a null mouse model… resulted in
decreased prenatal and postnatal growth… suggesting a potential direct effect of DLK1 on growth, independent
of early puberty."* (Caveat I add: the two worst heights are women aged 56 and 63 scored on modern
references — secular trend inflates that.)

**But the deletion-size series is better than what F-R076 claimed:**

| lesion (paternal) | genes | height | puberty |
|---|---|---|---|
| DLK1 exon 1 | DLK1 | −0.3 to −0.9 SD on GnRHa | **CPP, thelarche 4.6–5.9 y** |
| 109 kb | DLK1 + MEG3 | **−2.9, −2.2 SD** | menarche 10y3m |
| **411 kb** | + RTL1, MEG8, BEGAIN, WDR25 | **−4.4 SD** | **NORMAL menarche** |
| mat UPD14 (Temple) | whole domain | −2.7 to −3.7 SD | CPP 89% |

> ### **Stature scales with deletion size; puberty tracks DLK1.** So the height gene at 14q32.2 is **not DLK1 alone.**

### 1c-iii. THE LOCUS IS CLOSED. IT IS RTL1, NOT MEG3, AND BOTH DIRECTIONS ARE SHORTER (F-R078)

**Kagami 2008 (*Nat Genet* 40:237), the primary, supplied.** The **same 108,768-bp deletion gives opposite
syndromes by parental origin** — maternal → Kagami-Ogata, paternal → Temple. This is an imprinting-control
system, not gene dosage, and F-R077's gene-count reading was the wrong frame.

**MEG3 is REFUTED, twice.** (i) It is **maternally expressed**, so a *paternal* deletion removes an already-
silent allele and can contribute nothing to cases 9–11. (ii) *"**Gtl2^lacZ** mice… have a **normal
phenotype** with at least **60–80% reduction of all the MEGs**."* **DIO3 refuted too** (no thyroid
dysfunction in any case).

**RTL1 is confirmed, by the authors:** *"loss of active **DLK1 and RTL1** seems to constitute **additive**
underlying major factors… growth is more severely compromised in case 11, with **additional loss of active
RTL1**."* Mouse: paternal **Dlk1** KO **~80%** of normal size; paternal **Rtl1** deletion **~80%**; **both
~60%** (0.80 × 0.80 = 0.64).

**And F-R076 §1 is now FULLY retracted, not softened:** *"the paternally derived Dlk1 mutation… result[s] in
**pre- and postnatal growth deficiency**."* **DLK1 is both a timing gene and a growth gene.**

| gene | loss | excess |
|---|---|---|
| **DLK1** | ~80% size, precocious puberty | 2× overgrowth; **3× late-gestation lethal** |
| **RTL1** | ~80% size | 2.5–3× placental abnormality; human **bell-shaped thorax, coat-hanger ribs, growth retardation** |
| MEG3 / all MEGs | **60–80% down → normal mouse** | — |
| DIO3 | nothing | — |

> ### **Every gene at 14q32.2 with a height effect has an optimum and both directions away from it are shorter.** **The locus is not a gain-of-height lever. Thread opened F-R065, closed F-R078 on primary data.**


## 1d. The core combination has been randomised (F-R065)

**Mauras 2016, JCEM 101:4984** — 76 pubertal boys, AI vs GH vs AI/GH, 24-36 months, to near-final height:

| | to near-final height | near-final SDS |
|---|---|---|
| AI alone | +18.2 cm | -1.4 |
| GH alone | +20.6 cm | -1.4 |
| **AI + GH** | **+22.5 cm** | **-1.0** |
| *expected at -2.0 SDS* | *+13.0 cm* | |

**+9.5 cm over expectation (P=.01)**, bone health and adverse events similar across arms. **Sub-additive**
(+1.9 over GH alone). **Both arms are supply-side, so F-R064 leaves this untouched.**

**GH dose tension:** Mauras and ANSWER used **0.24-0.53 mg/kg/wk**; **2 IU/day is ~0.12 mg/kg/wk**. The
higher range produced the +22.5 cm and was safe over 24-36 months; Chu's depletion argument concerns
**indefinite** preservation, which those trials could not detect. **A time-horizon choice, not a right/wrong
number.**

---

## 2a. RETRACTED — "block the executioner" (F-R064)

**F-R060 named the terminal step and F-R062 built an arm around blocking it. That arm is removed.**

> *"Hypophosphatemia prevents apoptosis in the hypertrophic cells... the hypertrophic cells accumulate and
> form the rachitic bone."* *"The thickened growth plate paradoxically fails to produce normal linear
> growth."* **Children with hypophosphatemic rickets have SHORT STATURE.**

**Blocking the terminal step is the definition of rickets: a thick plate on a short child.**

**The reason was inside the identity all along.** `dL/dt = flux x v(d)` was derived from Wilsman's steady
state where **N_new = N_lost**. **If N_lost goes to zero, dL/dt goes to zero.**

> ### Longitudinal growth **is** the chondro-osseous junction advancing. Every micron of bone requires terminal chondrocytes to die and be replaced. **Growth and consumption of the plate are the same event, not opposing ones.**

**Reinterprets four filed puzzles:** Gerber's VEGF-trap mice (not "banking" — **induced rickets**); Voss's
+6 cm patient (**partial** blockade, supply intact); Karimian's doubled plate with +1.9% length (**cartilage
accumulated instead of converting**); the FDA dogs' thick plates with fractures (**the rachitic phenotype**).

**Removed from the stack:** direct VEGFR2 blockade, entirely. **And F-R061's "erdafitinib cancels itself via
phosphate" is withdrawn** — it rested on the false premise that blocking terminal apoptosis is desirable.

### And fusion gets a cleaner definition

**The plate does not close because consumption wins. It closes because supply runs out.** Kuhn's fused
proximal radius: `v(c)` = 2,590 um3. White's closing human physis: clusters with intervening acellularity.
Growth fraction saturated at 0.89-0.99. Byers: human ageing is **cell-number collapse with size preserved**.

> **"Never-closing" is a supply problem. Only arms that preserve or expand `n0` can deliver it — and the one
> that expands it does not exist.**

---

## 2b. The terminal step, named (F-R060)

```
serum phosphate → VEGFR2 (on the hypertrophic chondrocyte, not the endothelium)
                → Raf/MEK/ERK1/2 → caspase-9 → apoptosis → vascular invasion → junction advances
```

Sabbagh/Demay *PNAS* 2005 (low phosphate blocks the apoptosis; that expansion **is** rickets);
Yadav/Demay *iScience* 2023 (a screen for blockers of phosphate-induced ERK1/2 **identified VEGFR2**;
chondrocyte-specific VEGFR2 depletion → more hypertrophic cells, less apoptosis, impaired invasion).

**This unifies four arms previously treated as separate — oestrogen, vascular, mechanical envelope, and
transit time — and it retires "the vascular arm" as a description. Vascular invasion is downstream of a
cell-autonomous suicide signal, and the signal is phosphate.**

**And it supplies a renal route from oestrogen to closure** (Ikedo 2024): adipose aromatase → E2 → renal
NaPi2a/2c → serum phosphate → the axis above. **Nothing to do with ERα on a chondrocyte.**

**Design rule: block the death signal at VEGFR2, not by lowering phosphate.** Lowering phosphate achieves
the same plate effect and gives rickets; blocking the receptor spares the mineral.

**Human validation, and it contradicts F-R057.** Voss 2015 patient 5, pazopanib ×10 cycles: MRI-confirmed
**expansion of the hypertrophic chondrocyte layer**, fully reversible on stopping — and ***"no disruption in
longitudinal growth… gaining approximately 6 cm while on study."*** **The terminal step slowed while flux
and volume carried on.** F-R057's "VEGF blockade is a pure banking agent that costs rate" was drawn from
Gerber's ligand trap (which abolishes VEGF-A entirely); a receptor-level partial blockade behaves
differently.

---

## 2c. The counter-move inside erdafitinib (F-R061)

| via | terminal apoptosis | for us |
|---|---|---|
| FGFR3 → **ERK1/2 ↓** | suppressed | **delays closure — wanted** |
| FGF23 resistance → **phosphate ↑** → VEGFR2 → **ERK1/2 ↑** → caspase-9 | promoted | **accelerates closure — against us** |

**The same drug hits the same kinase with opposite signs.** Invisible until F-R060 named the executioner.

**They separate by ~10× in dose:**

| effect | normal rat | normal dog | ACH children |
|---|---|---|---|
| growth-plate thickening | **≥1 mg/kg** | 3 mg/kg | — |
| growth effect | — | — | **0.25 mg/kg → +3.38 cm/yr** |
| hyperphosphatemia | **10 mg/kg only** | — | **0 events at 0.25 mg/kg** |
| fracture + bone loss | — | **3 mg/kg** | — |

*"Hyperphosphatemia does not occur at the low doses of infigratinib that show activity in vivo."*
**Past the threshold you stop buying plate effect and start buying phosphate, which works against you.**
This is why F-R046's "threshold, not gradient" plateau at 0.25 mg/kg exists.

**Open decision (F-R061 §4.3):** all low-dose growth data is **infigratinib**; the stack specifies
**erdafitinib 8 mg**, an oncology dose with no growth-plate dose–response and a deliberate phosphate target
of 5.5–7.0 mg/dL. **No published mapping between the two exists and I will not guess one.** Either dose the
FGFR3 arm low with phosphate held at low-normal, or substitute infigratinib at the PROPEL 2 dose, which is
the only agent with a paediatric growth-plate dose–response behind it.

---

## 3. What is missing — ranked by how much it costs us

### 3.1 Terminal domain volume — **partly addressed after all** (corrected F-R060)

`v(d)` carries **2.67×** of the natural range and **6.8× measured human headroom**. F-R058 and F-R059 both
said nothing in the stack touches it and that **no agent raises terminal chondrocyte volume in a mammal**.
**Both were wrong, and the counter-example was the first drug in the stack:** FGFR3 inhibition produces
*"significant swelling of hypertrophic cells"* with HZ **+45%** against PZ +25%. **The volume lever is
occupied by erdafitinib.** What remains genuinely untouched:

**Cell volume `v(c)` — occupied, and now confirmed in wild-type (F-R061).** The published literature has
histology only in FGFR3 gain-of-function models (where TYRA-300's authors call the endpoint *"more similar
to a wild-type growth plate"* — normalisation). **The FDA infigratinib tox package supplies the wild-type
answer: dose-dependent growth-plate thickening in normal rats from 1 mg/kg and normal dogs at 3 mg/kg.**
Per-cell volume in wild-type is still inferred rather than measured (HZC-count-in-fixed-ROI is the ACH-model
proxy). NKCC1/NHE1/AE2 remain necessary-but-not-
sufficient; GH→Nkcc1 remains a one-study hypothesis.

**Matrix per cell `v(m)` — ADDRESSED IN F-R078 after being untouched for the whole programme.**
**32–49% of daily elongation**, larger than cellular enlargement in slow plates. Breur: matrix volume per
cell is essentially age-invariant and *"may be predetermined"*; regulators *"largely unknown"* as of 1997.

**The human loss-of-function gene is `ACAN`** — heterozygous aggrecan variants give autosomal dominant
short stature with **advanced bone age and premature epiphyseal fusion**, histologically *"reduced
hypertrophic cell expansion and decreased extracellular matrix volume."* **Halve the matrix, get a short
child whose plate closes early.**

**And a published gain-of-function lengthens bone: cartilage-specific CCN2 over-expression** — see §3.9.

### 3.2 And volume is what senescence and closure actually take

Across Breur's four plates from 21 to 35 days, elongation fell 12.5–39.5% and **cell volume fell 18.7–41.3%
while flux fell only 7.7–16.6% — and rose 7.4% in the proximal radius.** Kuhn gives the same dissociation
*inside one bone under identical systemic hormones*: at 12 weeks the rabbit **proximal radius is "almost
fused" at v(c) = 2,590 µm³** while the **distal radius is still growing at 290 µm/day at v(c) = 11,770 µm³**.
The two plates with no significant volume decline are exactly the two still open at 12 weeks.

> **Corrected in F-R059.** This holds *between* plates, not *within* one. In the human specimen caught
> mid-closure, cell volume was **statistically uniform across all nine regions** while bridging bone was
> **46% in one region and ~0 elsewhere**. **Closure initiates focally in a plate whose cells are all the
> same size — local volume collapse is not the local trigger.** Between-plate volume remains a valid
> correlate of remaining capacity.

**And the species split (F-R059).** In the *rat* 21→35 d, volume carried the decline and flux barely moved.
In the *human rib* birth→13.5 y, **cell size is preserved (lacunar diameter unchanged, ns) while cell number
collapses** — PZ height to 34%, HZ to 26%, matrix fraction rising 60→82.5% and 25→40%. **The human
age-related slowdown is flux-limited.** Which is exactly why volume is the compartment to push: the flux the
human is losing is the thing we must not spend.

**A second, independent senescence mechanism** (Kuhn): the **conversion efficiency per unit cell volume**
degrades with age — the 5-week rabbit slope is ~2× the 8- and 12-week slope (p < 0.01), and no
volume-to-rate relationship exists at all at 2–3 weeks. Restoring `v(c)` in an old plate buys about half
what it buys in a young one.

### 3.3 No pool arm

`L∞ ∝ n₀`. Erdafitinib, GH and abaloparatide neither expand nor protect the stem pool. Dexamethasone banks
it and costs rate. **Nothing found so far *expands* `n₀`.** The FoxA2⁺ tier proves `a > b` is achievable in
a mammalian plate through three serial transplants — but there is no agent that reproduces it.

### 3.4 No Hedgehog arm in the stack

HHIP1 deletion is the **only demonstrated `A` lever**. **No HHIP1 inhibitor molecule exists.** F-R056
established that the brake cannot be blocked at the ligand (HHIP and PTCH1 compete for the same two SHH
surfaces; HHIP Asp383 completes the SHH zinc sphere) — but the **HHIP-N CRD is a sterol-binding pocket** of
a superfamily defined by small-molecule binding. That is the drug-discovery target and it is unstarted.
F-R057 adds the constraint: **ligand-level brakes only.** Smo agonism and Sufu/Ptch1 removal both cause
premature closure (Xiu).

### 3.5 No vascular arm in the stack

Aflibercept/bevacizumab class. The **only intervention that demonstrably pauses the terminal step in a
mammal and is then released with the plate architecturally intact** (Gerber: full normalisation on
withdrawal). Human paediatric plate widening already documented (Voss 2015, 5/53). It is a τ-buyer, so it
belongs to "never close", not to speed.

### 3.6 The mechanical ceiling is real and the stack has one answer to it

Everything that widens the plate weakens it: SCFE on erdafitinib (F-R048), and Hall 2016 — juvenile rabbits,
antiangiogenic treatment, femoral-head plate dysplasia **and fracture**. This is a physical limit, nothing
to do with risk tolerance. **Abaloparatide is plausibly the counter** — that is why it stays in — but that
is an inference from Winer's safety data, **not a measurement**. Nobody has tested whether a bone anabolic
protects a pharmacologically widened plate.

> **F-R078 supplies the first measured counter-example, and it is not abaloparatide.** Cartilage-specific
> CCN2 over-expression lengthened the neonatal tibia **+5.6%** AND raised femoral **total mineral content
> (1.36 vs 1.10 mg/mm), trabecular mineral (0.49 vs 0.38) and cortical thickness (0.060 vs 0.049 mm), all
> P<0.05**, in the same animals. **Longer and stronger together — the only agent in the programme that does
> both.** See §3.9.

### 3.7 Link 11 is still open

**Ovariectomy does not prevent fusion in the rabbit** — Weise (E2 < 5 pg/mL, distal tibia fused at 2–6 wk)
and now Karimian independently (16/17 distal tibiae fused by 4 weeks). Two labs, same species, same
direction.

Two readings remain, and they are not distinguished:
- there is an **oestrogen-independent fusion driver** — supported by the fact that resveratrol delayed that
  residual fusion at all three plates with no anti-oestrogen mechanism; or
- the plate's **own intracrine oestrogen** does it (F-R049: CYP19A1 active in human plate; STS 265–660×
  aromatase by activity units). OVX removes the ovary, not intracrine aromatase, not STS, not adrenal DHEAS.

**Only the CYP19A1⁻/⁻ rabbit separates these. Those animals are alive and nobody has looked at their
growth plates** (F-R056 §1).

### 3.8 Two dose items to reconcile

- **GH — CORRECTED IN F-R078. This paragraph contradicted §1 and had been stale since F-R066.** It used
  to read that 0.35 mg/kg/wk *"lands in the depleting range"* on the strength of a mouse stem-cell paper
  (F-R032: *"GH augments both stem cell number and activity under physiological conditions but causes stem
  cell depletion under pharmacological exposure"*). **The only human outcome data at exactly that dose says
  otherwise.** Muthuvel/Dauber, **rhGH 50 µg/kg/day = 0.35 mg/kg/wk**, 10 ACAN-deficient children, 3 years:
  **height SDS +1.21 (P = 0.002), predicted adult height +6.8 cm (P = 0.002), IGF-1 SDS held at ~+2.3, and
  bone age/chronological age ratio change −0.10 (P = 0.205, NOT significant)** — in a population already
  prone to premature fusion. **Sustained gain, no maturation cost. §1's 0.07 mg/kg/day stands, and the
  low-dose rationale stays withdrawn.**
- **Erdafitinib 8 mg** sits inside the 5–9 mg window that has not produced SCFE. Consistent.

### 3.9 CCN2 — the branch had the sign backwards (F-R078)

**R341 killed CCN2 via pamrevlumab** (*"the published Ctgf-null phenotype is an EXPANDED hypertrophic zone…
a DISCHARGE FAILURE… PAMREVLUMAB points the wrong way"*), and the p21/Gli1 work found the opposite sign in
the stroma (*"p21⁺ chondrocytes generate a Ccn2-inhibiting area"*), amending the kill to **"not a *systemic*
lever."** **Both analyses are about LOWERING it. Nobody asked what raising it does — and the branch's own
reasoning implies the answer.**

**Cartilage-specific CCN2 over-expression (Col2a1 promoter, two independent founder lines, PLoS One
2013;8:e59226):**

| readout | result |
|---|---|
| **tibial diaphysis P1** | **6.225 ± 0.080 vs 5.897 ± 0.116 mm — +5.6%, P < 0.0001** |
| dose-dependence | correlated with transgene expression **in both founder lines** |
| **proteoglycan density** | enhanced (Safranin-O) — **this is `v(m)`** |
| Col2a1 / aggrecan mRNA | 100–1,000× / 15,000–20,000× |
| proliferation | PCNA up in PZ **and resting zone** — flux, possibly `n₀` |
| IGF | IGF-I/II mRNA up several-fold; **IGF-1R autophosphorylation enhanced** |
| **bone strength** | **mineral content, trabecular mineral, cortical thickness all up, P<0.05** |

**F-R079 — the same line followed to 24 months (*PLoS One* 2013;8:e71156):** viable and healthy to
**24 months**, CCN2 protein still accumulated in **growth-plate cartilage at 21 months**, **radiographic OA
in 50% of WT knees and NONE of the transgenics**, reduced ColX/ColI/MMP-13, enhanced proliferation at 21 mo.
**But neither paper ever measured adult bone length** — two papers, one line, 24 months, micro-CT and serial
radiography of four joints, and the number this programme needs was never taken. **The radiographs may
already contain it** (Hattori & Takigawa, Okayama).

**What it does NOT show:** the only length measurement is **P1 tibia, n=3**; *"12% larger at 8 weeks"* is
**body size/mass, not bone length**; **adult bone length was never measured**; zone heights are qualitative
(**HZ shorter** — a `v(c)` cost, since CCN2 *"promotes proliferation and differentiation but not
hypertrophy"*).

> **Complementarity:** CCN2 raises flux and `v(m)` and shrinks the HZ; **erdafitinib raises `v(c)`** (HZ +45%
> vs PZ +25%, *"significant swelling of hypertrophic cells"*). **Opposite halves of `v(d)`; each one's cost
> is the other's mechanism.** First genuinely complementary pairing in the stack.

> **The design that follows:** **Col2a1-promoter AAV-CCN2 by the intra-epiphyseal route of F-R074** (Zhang
> 2015 — 1 mm K-wire, 5.5×10¹¹ vp/mL, 25 µL, 12-week expression). **Promoter restriction solves the
> compartment problem the branch identified; the route solves the delivery problem. Both halves exist and
> nobody has combined them.**

**Unreconciled conflict, flagged not resolved:** CCN2's classical inducer is **TGF-β**, while F-R034 has the
resting-zone niche as *"low in WNT and TGF-β"* and F-R073's cocktail contains **Repsox (TGF-β/ALK5
inhibitor)** mapped onto that axis. **A CCN2 arm and a Repsox arm pull against each other.**

---

## 4. Why the oestrogen side is still not built

The standing instruction, and now a third reason. §3.2 says what closure looks like mechanically — a
**local collapse of terminal cell volume**. **Until something defends `v(c)`, there is nothing for an
anti-oestrogen arm to preserve.**

---

## 5. The single next thing

**Raise terminal chondrocytic domain volume.** It is half the identity, it carries **6.8× measured headroom
in the human** against a wild-type mammalian ceiling, and — uniquely among the levers — **it buys speed
without spending the division count that closure draws on.**

**The one experiment that would settle it, and that appears never to have been done:** has anything ever
raised terminal hypertrophic chondrocyte volume **above normal in a healthy mammalian growth plate**?
Searched (F-R059 §7): only deficit-normalisation (GH in uremia, via proposed Nkcc1/Igf1) and
loss-of-function (bumetanide −35%, EIPA/DIDS −60–70%, Igf1 cKO −34% height). Three independent lines —
GH→Nkcc1, CNP→hypertrophy, IGF-1→Phase 3 — converge on the lever from different directions and **none has
been pushed past normal.** Both candidate molecules (**GH, vosoritide**) are already in or adjacent to the
stack.

**The highest-value mechanistic question:** what sets the **bat manus at 40,300 µm³ and the bat pes at
1,300 µm³ in the same animal**? Whatever it is, it is local, endocrine-independent, and has a 31× dynamic
range.

Flux is not neglected — erdafitinib works there — but flux is capped (**growth fraction already saturated
at 0.89–0.99**) and, more importantly, **spending it is the thing that closes the plate.**
