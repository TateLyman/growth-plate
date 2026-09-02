# Round 29 — where to push: the budget is paid in cells, the output is measured in micrometres

## The trap, stated exactly

Everything this project has established converges on one structure, and once it is written down the
search space collapses.

**Fusion is proliferative exhaustion** (`weise2001`): the plate fuses when proliferation reaches zero.
So the budget is denominated in **progenitors**. But height is denominated in **micrometres**. What
converts one into the other is the yield, and the yield factorises *exactly*:

> **µm per progenitor = (terminal cells produced per progenitor) × (height of each terminal cell)**
>
> call these **amplification** and **h_term**

Now put every lever the atlas has examined into that equation:

| lever | acts on | why it fails |
|---|---|---|
| more proliferation / GH | amplification | drains the pool faster, hastens fusion (`nilsson2014`) |
| bigger pool | pool | never achieved with intact flux — three mouse perturbations, all diverted or blocked flux |
| slower senescence | rate | works **only** by inhibiting growth; 4 weeks of inhibition buys 2 (`forcinito2011`) |
| more IGF / BMP | amplification | long-bone chondrocytes are **already at ceiling** for both (`lui2018`) |
| delay fusion (aromatase) | duration | `herrmann2002` stopped growing at 24 with plates still **open** |

**Every one of them acts on amplification or on rate, and both are paid for in progenitors.** That is
why the GH dose-response saturates: KIGS, 0.30 vs 0.21 mg/kg/week — a 43 % higher dose — buys +0.75 vs
+0.69 SDS in year one and *nothing* at near-adult height. Velocity is spent capacity.

**h_term is the only term in the equation that is not paid for in progenitors.**

## Four facts about h_term, all already in the atlas, never assembled

**1. It is not what nature varies.** I decomposed the yield from `lui2018`'s raw per-animal values:

| | femur vs metacarpal, 2–3 wk |
|---|---|
| yield ratio | **10.40 ×** |
| h_term ratio | **1.38 ×** (27.9 vs 20.2 µm) |
| residual — amplification | **7.54 ×** |
| share of the log gap: terminal cell size | **14 %** |
| share: clonal amplification | **86 %** |

At 2 weeks, *before* the metacarpal collapses, the ratio is only **1.10×** — a bone about to fuse has
terminal cells **91 % the size** of one that never will, and gets **one tenth** the length per
progenitor. The gap is not cell size.

**2. In humans it is flat.** 29–38 µm from birth to 13 years, no age dependence (`kember1976`); rib
lacunar diameter likewise (`byers2000`) — across an interval where velocity varies several-fold and
then spikes at puberty. **Humans do not use this parameter to set growth rate.**

**3. It is not at a ceiling.** Terminal volume spans ≥4.6-fold across mammalian plates: ~5,000 fl in
the slow mouse proximal radius, ~14,000 in mouse tibia, **~23,000 in the jerboa metatarsal**.

**4. And the largest component is *swelling*, not biosynthesis.** Phase 2 takes the cell from ~2,000 to
~8,000 fl while dry mass density falls to ~0.07 pg/fl — **a 60 % dilution** (`cooper2013`). **A cell
that gets bigger by taking on water spends no divisions.**

## The claim

h_term enters height **linearly, elasticity 1**; varies several-fold between mammals; is held flat
across human childhood; and is produced largely osmotically. It is the one term that is **large,
movable, and free** — it buys micrometres without spending the pool that fusion is waiting on.

## The objection, which is the right one

An invariant parameter may be invariant because **nothing varies it** — an unused degree of freedom
with no homeostat to fight — or because something **defends it**. This node asserts the first and
**cannot yet exclude the second.** Two things weigh against the optimistic reading and are recorded on
the node:

- The 14 % share is *equally consistent* with terminal cell size being **constrained**. The same number
  supports both readings; it does not discriminate.
- The human premise sits on **one side of an unresolved contradiction (C-L1-09)**. In rat this
  parameter *falls* with age and `roach2003` identifies its loss as what drives cessation; in rabbit it
  falls too. The human flatness rests on **12 subjects, 1–2 per age**. If that is a power failure rather
  than a fact, the central premise fails.

Also unhandled: hypertrophy is **time-boxed** (~12 h to triple, ~12 h at terminal size). If bigger cells
take proportionally longer to make or to clear at the chondro-osseous junction, velocity does not rise
with volume and the elasticity of 1 is wrong.

## The discriminating test — and it is already in published human data

A **velocity** drug buys first-year velocity and saturates on final height, because velocity is spent
capacity. A **yield** drug should give height **without proportionate skeletal maturation**, because it
extracts more µm per progenitor.

> **The discriminator is Δheight ÷ Δbone-age under a CNP analogue, against untreated controls.**
> If bone age advances in step with height, CNP is a velocity drug and this route is closed.
> If height outruns bone age, it is the first yield drug and the parameter is movable in humans.

CNP reaches exactly this compartment: it acts on the growth plate **largely by expanding the
hypertrophic zone**, with far more CNP-regulated genes there than in resting and proliferative cartilage
combined (`agoston2007`). And a CNP analogue is **approved**.

**The confound that must be handled:** in achondroplasia, CNP is correcting an FGFR3 gain-of-function
lesion, so a gain there may be repair rather than headroom above normal. **The clean read is a CNP
analogue in a non-FGFR3 indication** — idiopathic short stature, SHOX deficiency, Turner — where any
gain is against an intact pathway.

**If the human data are ambiguous, the animal test is one cohort:** give a CNP analogue to normal mice
and measure terminal cell height, bone length **and resting zone cell count per 500 µm** *together*.
That last measurement is the one nobody makes, and it is the entire question — **whether the micrometres
were free.**

## Committed

- New node `terminal_cell_volume_is_the_undefended_term` (L1, `hypothesis`, **C**, decomposition row
  flagged `value_unverified`), with the objection recorded as prominently as the argument.
- New gap `g_l1_raise_terminal_cell_volume`, tractability 4, carrying the Δheight/Δbone-age test.
- Three edges from `hypertrophic_volume_increase`, `cnp_protein` and to
  `the_exchange_rate_between_growth_and_pool_depletion`, all `speculative`.
- `atlas/tools/yield_lui2018.py` extended reasoning; decomposition reproducible from the vendored S1 Data.

Validator: 642 nodes, 1242 edges, 319 gaps, 1142 refs — 0 errors, 0 warnings.
