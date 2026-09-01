# F-R002 — coverage red-team: forty-one out-of-the-box axes, greped against this repository

**Purpose.** I was asked for the things nobody has thought of. Before claiming any of them I ran the
rule this file enforces on itself: *grep the concept under at least two names, and grep `gaps.yaml`
as well as the nodes, before writing that nobody has asked* (CORR-313 / CORR-352 / CORR-353).

**Result. Thirty-four of forty-one were already worked, several of them further than I would have
taken them.** That is a coverage measurement, and it is a good one: this repository's enumeration
layer (`atlas/concepts/enumerations/`, 21 domains, R436) is doing its job. The seven that survive
are recorded below with the exact greps that establish them, so the claim is falsifiable.

Two of the seven are executed in `F-R001`. Five are open.

---

## A. Already worked — do not re-derive (34)

Grouped by the framing I attacked. Each row names where the atlas got there first.

### The trunk / non-physeal height stack — 7 axes, all worked, one of them better than my version

| my axis | where it already is |
|---|---|
| Standing height is not the sum of bone lengths; the discs are a separate compartment | **R319** — "sitting height is vertebral BONE plus intervertebral DISC" |
| The 19.3 mm diurnal swing is a lever, not measurement noise | **R319 states this in exactly those words**, and names `diurnal_stature_variation` as the node that filed it under measurement error |
| Hyper-buoyancy flotation / spaceflight axial unloading, with a stature endpoint | **R319** (`marcoslorenzo2026`, +1.6 cm in 4 h, −0.4 cm reversal) |
| Spinal sagittal curvature as a projection term on height | briefs 09 and 13; R319 |
| The axial growth centres close last, so the trunk is the live compartment | **R319** (`ekizoglu2026`, ring apophysis median ~22 y in males) |
| Hueter–Volkmann applied to the vertebral endplate physis | L6; **R319** (`halanski2026` porcine tethering, converges by 2–4 weeks) |
| Axial loading history — gymnasts vs swimmers | `gymnastics_stature_effect`, `theintz1993`, `daly2005` in `parameters.csv` |

I independently re-derived R319's synthesis, including its headline. It is correct and it is theirs.
The one thing I would add: R319's own limitation — *"the central unknown is whether the disc-height
SET POINT can be moved"* — is a question about an **osmotic equilibrium in an adult**, not about
growth, and therefore survives every fusion argument in this file. It is the only lever class here
that works identically at bone age 16 and at bone age 30.

### Time, schedule and the clock — 6 axes, all worked

Duty-cycling the progenitor pool (`g_l2_cycling_the_progenitor_pool`, R178, `oichi2023`) · dietary
restriction as a charge phase (CORR-353) · intermittent GH (**R367**: tested three times in humans,
twice randomised, short pauses lose, long pauses neutral, nothing beats continuous) · insect
duration levers (**R461**: PTTH-neuron ablation gives larger flies, and the architecture does not
transfer) · developmental tempo as a size dial (**R461**: `lazaro2023`, `seleit2024` — refuted) ·
diapause and dauer as pause-the-clock (**R461** — no larger post-diapause adult exists in any
species).

### The pool, the budget, and reversal — 6 axes, all worked

Partial reprogramming / OSK in cartilage (`THE_CLOCK.md` §3) · the methylation clock, both halves
(R276 writer / R283 eraser, TET1 +8.32 cm) · senolytics (**DEAD, R266** — growth-plate senescence is
not p16/SASP) · Gli1⁺/PDGFRA⁺ perichondrial reservoir (`THE_CLOCK.md` §2, `qu2025`) · the antler as
a renewable-budget existence proof with RXFP2 and PRRX1 (**R199**) · the imposed-not-intrinsic limit
(`nilsson2005`, `THE_CLOCK.md` §1).

### Fusion, duration and the ceiling — 4 axes, all worked

The oestrogen-null ceiling as a censored observation (`CEILING_CENSUS.md` — four parts, ~197 cm
observed endpoint without fusion) · aromatase inhibition (SETTLED, +1.3 cm over 3 y) · the residual
maturation route and its elimination of androgen (`CEILING_CENSUS` part 3) · bony-bridge formation
as the fusion mechanism (`bony_bridge_formation`, ~495 transphyseal bridges in WT mouse).

### Surgical and mechanical — 4 axes, worked

Distraction osteogenesis (SCALE section, R398, R418) · physeal distraction / chondrodiatasis
(enumerations 09, 14, 19) · physeal and vascularised epiphyseal transplantation (enumeration 19) ·
physical-modality sweep including vibration, run to a null length endpoint (**R456**).

### Instruments and screens — 5 axes, worked

FAERS disproportionality with a validated positive control (**R437**) · Drugs@FDA and EPAR juvenile
toxicity (**R350, R457**) · the human overgrowth / tall-stature gene space (**R17**, including its
own correction of the Marfan/fibrillin exclusion) · veterinary and livestock data including
prepubertal neutering (**R457**, `bitches +2.0 cm`) · the ChEMBL chemical-matter sweep that fixed
the Open Targets blindness (**CORR-347, R334**).

### Delivery, matrix and targets — 2 axes, worked

Cartilage-targeted nanoparticles into an avascular plate (`ye2026` CT-CM-NPs, WYRGRL) · the whole
regenerative/genetic modality space including base editing, prime editing, CRISPRa, TANGO ASOs,
SINEUPs, LYTACs and organoids (**enumeration 19**, 125 rows, each marked for whether it has ever
reached a physis).

---

## B. Executed in this branch (2)

| # | axis | grep that established it | status |
|---|---|---|---|
| 1 | **`ctg_measures.csv` — 5,445 arm-level human height numbers, acquired R18, never aggregated** | `grep -rl "ctg_measures" atlas/nodes atlas/gaps` → the only hits are unrelated substring matches; zero in CLAUDE.md | **done — F-R001** |
| 2 | **Per-person cumulative limb lengthening** | `repeat lengthening` 0 files · `serial lengthening` 0 files · `40101878` 0 files | **done — F-R001 §5** (14.5 cm over 3.7 procedures, n=90) |

---

## C. Open — the seven that survived the grep, ranked (5 remaining)

### C1 · The afferent limb of the size checkpoint

**Greps:** `dilp8` **0 files** · `critical weight` **0 files** · `size sensing` **0 files** ·
`gdf15` **0 files** · `gfral` **0 files** · `bone-brain` **0 files** · `lgr3` 1 file (incidental,
inside an unrelated PDF).

**The gap.** R461 assessed the insect **efferent** limb — ablating the PTTH neurons delays the
ecdysone pulse and produces larger flies (`mcbrayer2007`) — and correctly ruled that the
architecture does not transfer, because the insect grows by feeding with no plate and no pool being
spent. **The afferent limb was never assessed and is a different question.** In *Drosophila* a
growing or damaged imaginal disc secretes Dilp8, which acts on Lgr3 neurons to **delay maturation
until the tissue reports completion**. That is a tissue → brain signal reporting *remaining growth
capacity*, and it is the only place in biology where such a circuit is molecularly mapped.

**Why it is not idle.** Mammals demonstrably have the coupling — chronic illness, undernutrition and
growth failure all delay puberty — and this repository has the *hypothalamic* end of it in detail
(KISS1, MKRN3, LIN28B, leptin) while holding **nothing on the afferent signal**. Two consequences,
one therapeutic and one immediately practical:

- *Therapeutic:* a duration lever acting on the afferent limb would delay the trigger **without
  removing the pubertal spurt** (which is why GnRHa nulled in NCT00355030) and **without oestrogen
  blockade's bone cost** (the −1.33 → −1.94 lumbar BMD Z of R278). This file states repeatedly that
  it has no such lever.
- *Practical:* the same circuit, read backwards, is a **circulating marker of remaining physeal
  capacity**. This file has CXM (collagen-X degradation, 39 files) which reports current hypertrophic
  *activity*. A capacity signal is a different quantity and is the one the operator actually needs.

**Cheapest step.** A single query this repository can run for free: does human growth-plate
expression data (GSE9160 zone-resolved, `chu2026`, GSE288028) carry any **secreted** factor whose
receptor is hypothalamic and whose expression tracks zonal maturity? The dataset inventory exists
(`atlas/quant/dataset_inventory.csv`) and CORR-316 already mandates running it before any literature
search.

⚠ **Honest prior: low.** The relaxin/INSL superfamily is present in this file (RXFP 39 files, INSL3
10) without a growth-plate afferent role, and the vertebrate orthologue of Dilp8 is not established.
This is a well-posed question with a plausible negative answer, not a promising target.

### C2 · Allocation — is longitudinal growth locally budgeted or systemically rate-limited?

**Greps:** `amputee` **0 files** · `overgrowth of the residual` **0 files** · `shared resource` 1
file (incidental) · `size sensing` 0.

**The gap.** This file's model is a per-plate budget: each physis holds a division allowance, spends
it, and fuses. Under that model the ~200 physes are independent and nothing can be redirected.
But two of its own recent findings argue for a **shared systemic constraint** on top of the local
one: R454 — *a growth-plate chondrocyte secretes at the plasma-cell ceiling while matrix per cell
stays constant across a ninefold range of growth rate*; and R461 — *the Golgi module is limited by
**acceptor and donor supply**, not by enzymes*, with `dick2008papst` showing a Golgi step can be
raised by supplying substrate. Substrate pools (sulfate, PAPS, nucleotides) are **systemic**.

**Why it matters, arithmetically.** Most longitudinal growth is spent where it cannot be measured in
a stadiometer: humerus, radius, ulna, metacarpals, phalanges, ribs, clavicle, fibula. If any part of
the constraint is a shared pool, **that expenditure is a leak**, and the question "can it be
redirected" has never been posed in this file.

**The natural experiments already exist and are free.**
1. **Congenital limb deficiency and childhood amputation.** Do the remaining segments — critically
   the *contralateral* limb and the *spine* — overgrow? A shared pool predicts yes; independent
   budgets predict no.
2. **Epiphysiodesis.** Done routinely for limb-length discrepancy, and adult height after it is
   predicted accurately by simple subtraction — which is strong evidence **against** a shared pool
   and is the fastest way to kill this axis. `epiphysiodesis` returns 156 files here; the
   *compensation* question is not among them.

**This is a two-query axis and one of the two answers closes it permanently.** That is why it is
ranked second despite a prior that runs against it.

### C3 · The calvarial vault as a post-fusion height term

**Greps:** `vertex` 1 file (a GWAS filename) · `skull height` 4 files (all incidental) ·
`cranial vault` 18 files and `calvarial` 44 — **every one of them about craniosynostosis as a
cost**, chiefly HHIP's lambdoid fusion and the suture stem-cell node.

**The gap.** Standing height includes roughly 13–14 cm of head above the atlanto-occipital joint,
and the calvarial sutures are **the only growth interfaces in the entire height chain that never
fuse**. This file holds `cranial_suture` and `suture_mesenchyme_stem_cell` as **liabilities** — the
tissue HHIP loss damages — and has never asked whether vault height is a term that can move, in
either direction, after every physis has closed. Cranial vault distraction is routine surgery and
proves osteogenesis is available at a suture on demand; acromegaly changes adult skull dimensions.

⚠ **Honest prior: the magnitude is probably millimetres**, and the first honest step is a *ledger
entry*, not an intervention: what is the measured variance and age-trajectory of vertex-to-basion
height in adults? Recorded because a term nobody has costed is not the same as a term worth zero,
and because this is the only one in the non-physeal stack that is bone rather than water.

### C4 · The active-comparator half of the trial corpus

**339 of 529** arm contrasts in F-R001's harvest come from trials with no placebo arm and were
therefore excluded from the base rate. They include this atlas's own losartan positive control.
They are committed in `results_all_contrasts.csv` and are unanalysed. Head-to-head paediatric trials
are the only place a *relative* height effect between two active drugs is randomised.

### C5 · The absolute-height extraction

Trials that post height at baseline and at follow-up under an absolute-value outcome title were
dropped rather than differenced. Writing that extraction would roughly double the base-rate sample.
Cheapest open item in this branch.

---

## D. What this red-team says about the atlas

The enumeration layer is not the weak point; **the ledger is**. Every one of the 34 covered axes was
found in a node, a gap or an enumeration — and several were *not* in `CLAUDE.md`, which is the
failure mode CORR-352 names precisely: *anything not in CLAUDE.md is invisible, and its sign is
irrelevant.* R319 is the clearest case. It is one of the most consequential rounds in the file — it
opens a whole fusion-independent compartment — and I re-derived it from scratch before grepping,
because nothing in the operating file points at it.

**Concrete suggestion, in this file's own idiom:** the SETTLED/DEAD tables are indexed by
*conclusion*. There is no index by **compartment** — plate / disc / posture / soft tissue / surgical
— and the trunk work (R317–R319, R425, R455, R458, R472) is the compartment most likely to be
re-derived because it is the one least represented in the operating file.
