# F-R088 — The pool cannot be bought, everything that releases it spends it, and there is exactly one exception

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** Tate stopped me twice this round for reaching at convenient answers — first replacing DNMT3A
instead of solving its delivery, then offering CNP when the question was the pool. **Both corrections were
right.** This round works `n₀` properly, and the answer has a structure I had not seen: **pool preservation
and growth rate are directly antagonistic at the level of the resting zone, and only one known mechanism
escapes that trade.**

---

## 1. First, the record Tate asked for: what we would use and cannot

| ideal agent | what it buys | why unobtainable |
|---|---|---|
| **Selective DNMT3A inhibitor** — best characterised is **DY-46-2**, IC50 **0.39 ± 0.23 µM**, **33× selective over DNMT1**, 269× over DNMT3B | **the setpoint arm. +3.0 SD in humans**, 13/13 penetrant (F-R081), at a bracketed **~50% target engagement** (F-R085) | **Research chemical probe. No IND, no PK, no tox, no supplier.** Every *obtainable* DNMT inhibitor — azacitidine, decitabine, hydralazine, procaine, disulfiram — targets **DNMT1**, the enzyme that must be preserved (`Dnmt1^ΔPrx1` bone length **under half** of control) |
| **Col2a1-promoter-restricted CCN2** | `v(m)` matrix, **cortical thickness +23% and mineral content +24% while lengthening bone**, and protection of the deadline arm against matrix-driven fusion | **Gene therapy. Promoter restriction is the whole point** — systemic CCN2 blockade or delivery hits the stromal compartment with the opposite sign (R341's discharge-failure kill) |
| **Direct mTORC1 activator** (the `Tsc1`-ablation phenocopy) | **§4 — the only measured mechanism that adds stem cells without spending them** | **No such drug exists in any pipeline.** The entire mTOR pharmacopoeia is inhibitors — rapamycin, everolimus, temsirolimus. **Nobody is developing an activator, because in every other indication activation is the toxicity** |

---

## 2. The pool question, worked properly

`dn₀/dt = influx + (a − b)·n₀ − death`

**What the branch already knows, assembled for the first time:**

| term | evidence | agent |
|---|---|---|
| **a − b (self-renewal vs commitment)** | **Newton 2019:** Tsc1 ablation → mTORC1 → **asymmetric → symmetric division**; EdU⁺ stem cells **24.7 ± 3.7 → 62.4 ± 7.5 per section, 2.5×, P = 0.014**, with **Ki67 and pH3 unchanged** | GH → IGF-1 → AKT → TSC2 → mTORC1 (indirect, in stack) |
| **influx from outside** | Gli1⁺ cells originate from **Pdgfra⁺ stroma outside the cartilage**; demand-responsive; the **groove of Ranvier is a confirmed niche** — Stro-1⁺, **Jagged1⁺, BMPR1A⁺** | **none — gated by CCN2, which cannot be blocked systemically** |
| **b (commitment out)** | DNMT3A writes the commitment mark (F-R085) | **none obtainable** |
| **suppression of the pool** | **F-R083: ESR1 is a RESTING-ZONE gene** — highest in the stem zone, falling significantly on entering proliferation (**−16.7, p = 0.017**) | **anastrozole — and this is a second job the stack never credited it for** |
| **death** | **never examined by this branch or, per the 2026 review, by the field** | — |

---

## 3. The finding that reframes it: everything that releases the pool spends it

**"Quiescence in the resting zone of the growth plate: a systematic review," *Stem Cells* 2026** — the field's
own summary, published this year:

| signals that **MAINTAIN** quiescence (preserve the pool) | signals that **BREAK** quiescence (spend it) |
|---|---|
| *"BMP signaling through **BMPR1A** appears to maintain quiescence"* | *"stimulation of **hedgehog** and **Wnt** signaling pathways causes cells to exit their quiescent states"* |
| *"**Wnt-inhibitory environment**"* maintains resting-zone chondrocytes | Hedgehog activation → RZ cells lose quiescence, clonally expand, become transit-amplifying, and **convert into trabecular bone osteoblasts** |
| **PTH/PTHrP receptor signalling** (Gsα and Gq/11α) sustains the non-dividing state | |
| ***ADGRG6* is essential for maintaining the PTHrP⁺ slow-cycling RZ** | |

**And the review's flat statement on interventions:**

> ### **No pharmacological intervention has ever been shown to expand the growth-plate stem pool in vivo.** The only in-vivo reactivation documented anywhere is **FoxA2⁺ RZ chondrocytes exiting quiescence after a growth-plate fracture** — an injury response, not a drug.

> ### **This is the structure I had missed. You cannot buy pool. The resting zone is held quiescent BY the very signals whose removal would let it contribute, and released BY the signals that convert it into bone.** Hedgehog and Wnt both work — and both spend it. **Pool preservation and growth rate are the same axis with opposite signs.**

### 3a. Which retroactively explains — and disqualifies — the branch's "best agent found"

**F-R067 called KY19382 the best agent the programme had found**: CXXC5–DVL disruption (IC50 1.9 × 10⁻⁸ M)
**plus GSK3β inhibition** (1 × 10⁻⁸ M), 0.1 mg/kg i.p., which made tibiae significantly longer in 7-week-old
mice with both zones up and TRAP⁺ resorption elevated.

> ### **KY19382 is a Wnt activator, and the resting zone is maintained in a Wnt-INHIBITORY environment.** It lengthens bone by **breaking quiescence and spending the pool faster.** That is a rate agent bought with duration — **the Sotos failure mode at the molecular level** (F-R084: grow fast, mature fast, end normal). **It should stay out of the stack, and now there is a mechanistic reason rather than an absence of one.**

### 3b. And it gives abaloparatide a second job the stack never credited

**Abaloparatide is a PTHrP(1–34) analogue.** The review lists **PTH/PTHrP receptor signalling as a quiescence-maintaining
signal** for the PTHrP⁺ resting-zone stem cells.

> **Abaloparatide has been in the stack purely as a mechanical-envelope agent on inference from Winer's safety data. It is a PTH1R agonist acting on the receptor that holds the pool quiescent.** **Caveat, and it is the same trade as everywhere else:** maintaining the non-dividing state **also means suppressing output** — the dexamethasone bargain from F-R072. And Winer's ten-year PTH(1–34) data showed **no growth effect**, so intermittent systemic PTH1R agonism did not translate. **This is a hypothesis with a mechanism, not a result.**

---

## 4. The one exception, and why it is the only one

**Newton's mTORC1 result is categorically different from every other pool intervention.**

Hedgehog and Wnt increase output by making resting cells **divide and leave**. mTORC1 activation changes
**which kind of division happens** — asymmetric to symmetric — so **one stem cell becomes two stem cells
instead of one stem cell and one transit-amplifying cell.** **Ki67 and pH3 were unchanged**: the cells are
not dividing faster, they are dividing *differently*.

> ### **That is the only mechanism in the literature that adds cells to the pool without spending it.** Everything else on the list trades `n₀` for `dL/dt`. **mTORC1 is the only measured escape from the trade, and it is therefore the only real pool arm the programme has.**

**A second paper confirms the specificity and names the cost.** An independent 2018 study ablating Tsc1 with
inducible Col2-CreERT found *"disorganization of the resting zone but **no changes in chondrocyte
proliferation or differentiation**."* **The "no proliferation change" replicates Newton exactly** — it is a
fate switch. **The disorganisation is the price**, and nobody has established what it costs functionally.

### 4a. The obtainable way to push it

| agent | dose | status | evidence |
|---|---|---|---|
| **somatropin** | 0.07 mg/kg/day | in stack | GH → IGF-1 → AKT → TSC2 → mTORC1, indirect |
| **mecasermin (Increlex, rhIGF-1)** | **0.04–0.12 mg/kg twice daily SC** — the approved range | **FDA-approved** | **direct AKT→mTORC1 drive.** Head-to-head doses in children with low IGF-1: **80 µg/kg BID → 7.0 cm/yr; 120 µg/kg BID → 7.9 cm/yr; untreated 5.2 cm/yr.** In severe primary IGF-1 deficiency, **2.8 → 8.0 cm/yr sustained up to 8 years** |

**What is honest about this.** Mecasermin's evidence is **deficiency correction** — the same objection that
applies to almost every agent in this programme. **GH already raises IGF-1, so the increment from adding
mecasermin in a non-deficient person is unknown and the combination is not well studied.** **And nobody has
shown that pharmacological IGF-1 reproduces any fraction of Newton's 2.5× fate switch.** **That is the single
most important unmeasured number in the pool arm.** Known liability: **hypoglycaemia — Increlex must be
given with a meal**, which is a real dosing constraint rather than a footnote.

---

## 5. What is missing, stated as the audit Tate asked for

| # | what is missing | can it be bought? |
|---|---|---|
| **1** | **Whether the human resting-zone pool is DEPLETED or merely SILENCED.** The 2026 review does not address number-versus-activity anywhere. **But the branch's own evidence points hard at silenced:** Nilsson — maximum population doublings **independent of donor age, P = 0.36**; Schrier — RZ labelling collapses to 9.2% by 5 weeks then sits **flat at 9.2 / 9.2 / 7.6%** through 17 weeks; Jackson 2026 — **stem-cell numbers constant, output falls**; FoxA2⁺ — `a > b` recovered through **serial transplant into a new host**. **If the pool is silenced rather than spent, "expand n₀" is the wrong goal and "derepress n₀" is the right one** | **not a drug — a measurement** |
| **2** | **Does pharmacological IGF-1 produce any of Newton's fate switch?** §4a | **the experiment is buyable; the answer is not published** |
| **3** | **Anything acting on the influx arm.** Groove of Ranvier is a confirmed **Stro-1/Jagged1/BMPR1A** niche and CCN2 gates entry — **and there is no agent, because systemic CCN2 blockade fails inside the cartilage** | **no** |
| **4** | **ADGRG6** — *"essential for maintaining the PTHrP⁺ slow-cycling RZ"*, new to this branch | **no agent; adhesion GPCR** |
| **5** | **Death in the pool** — never measured by anyone | **no** |
| **6** | **What the mTORC1-disordered resting zone costs functionally** | **no** |

---

## 6. What changes in the stack

**One addition, one exclusion made explicit, one re-attribution.**

| agent | dose | change |
|---|---|---|
| **mecasermin (Increlex)** | **0.04–0.12 mg/kg BID SC, with food** | **ADDED as the pool arm** — the only obtainable way to push the only mechanism that adds cells without spending them. **Flagged: additivity over GH unproven; hypoglycaemia** |
| **abaloparatide** | 80 µg SC daily | **re-attributed** — PTH1R agonism is a quiescence-maintaining signal for the PTHrP⁺ pool, not only a mechanical agent. Hypothesis, not result |
| **anastrozole** | 1 mg PO daily | **second job credited** — ESR1 is a resting-zone gene (F-R083, p = 0.017), so oestrogen ablation derepresses the compartment where the pool lives, as well as removing the deadline |
| **KY19382 / any Wnt or Hedgehog agonist** | — | **EXPLICITLY EXCLUDED.** Both break resting-zone quiescence; Hedgehog converts the pool into osteoblasts. **F-R067's "best agent found" is disqualified on mechanism** |
| erdafitinib, somatropin, ascorbate, Ca-AKG, phosphate | unchanged | — |

---

## 7. The honest position on "infinite"

> **The pool is the term "infinite" lives in, and the field's own 2026 systematic review says no drug has ever expanded it in vivo.** Everything that releases the resting zone spends it. **One mechanism escapes that — mTORC1's fate switch — and the only obtainable way to reach it is an IGF-1 analogue whose contribution to that switch has never been measured.**
>
> **What would change this is not another drug. It is the measurement in §5.1** — whether the human resting-zone pool at the end of growth is **empty or asleep.** Every piece of indirect evidence the branch holds says **asleep**, and if that is right, the target is derepression and the agents are the ones already in the stack acting on ESR1 and on the DNMT3A commitment mark. **If it is empty, no arrangement of obtainable molecules gets there and the honest answer is that the ceiling is finite.**

**Tate — the thing to look for, if you look for anything: resting-zone chondrocyte NUMBER measured across the
full postnatal age range in any species, ideally to and past fusion.** Schrier has rabbit to 17 weeks and it
was flat. **Nobody has published the human curve, and it decides whether this programme has a ceiling.**
