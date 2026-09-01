# R129 — Zhou 2015 read in full. Its central mechanism FAILS replication in human zonal
# data, and the paper contradicts itself. One result survives. And then the tiered answer
# to the actual question: **190.0 cm (6'2.8") is defensible, 195.6 cm is not — and the
# single variable that dominates the whole thing is months on the aromatase inhibitor.**

---

## 1. WHAT THE PAPER IS

**Zhou S, Shen Y, Wang L, Li P.** *Int J Clin Exp Med* 2015;8(8):12076–85. Outbred ICR mice, **n=6 per
group**, weekly IP from 4 weeks for 4 weeks: **70 µg/kg estradiol cypionate, 15 mg/kg oxandrolone,
2.5 mg/kg SIS3** (Smad3 phosphorylation inhibitor). Zones sorted by FACS — **Bmp3⁺ = RZ, Col10a1⁺ = HZ,
double-negative = PZ**. Length of **spine, femur and tibia** by X-ray.

**Its claims:** RZ→PZ is an EMT, PZ→HZ is an MET; **oestrogen blocks the RZ→PZ transition** by repressing
TGF-β/Smad3; **androgen promotes the PZ→HZ transition**; SIS3 mimics oestrogen.

---

## 2. ⛔ THE CENTRAL CLAIM DOES NOT REPLICATE IN HUMAN

I tested its core prediction directly in **GSE9160** — laser-captured human growth plate, five compartments,
two normal children. Prediction: epithelial markers **low in PZ**, mesenchymal markers **high in PZ**.

| panel | genes matching | median PZ/(RZ,HZ) ratio |
|---|---|---|
| epithelial (predicted PZ-low) | 3/5 | 0.73 — *weakly consistent* |
| **mesenchymal (predicted PZ-high)** | **4/7** | **1.01 — exactly chance** |
| **TGF-β/SMAD axis (the proposed gate)** | **4/8** | **1.00 — exactly chance** |

And the two largest-effect genes run **backwards**:

| gene | Reserve | Prolif | direction |
|---|---|---|---|
| **ACTA2** (Zhou: mesenchymal, PZ-high) | **14,730.8** | **843.1** | **17-fold INVERTED** |
| **SMAD3** (the paper's mechanistic gene) | **1,251.3** | **748.0** | **INVERTED** |
| VIM | 12,082.4 | 5,449.9 | inverted |

> **SMAD3 — the single gene the entire proposed mechanism runs through — is higher in the human resting
> zone than the proliferative zone, the opposite of what the paper reports in mouse. The mesenchymal arm
> and the TGF-β arm both sit at exactly chance.**

**The EMT/MET gate framework is not supported in human tissue.**

### And the paper has independent problems
- **It contradicts itself.** Abstract: *"androgen promoted **MET** from PZ to HZ."* Discussion: *"Androgen is
  determined to promote **EMT** for differentiation"* and *"Androgen effectively promotes **EMT**."* Those are
  opposite claims in one paper.
- **No numerical results are given for the length assay** — only "estrogen inhibited while androgen
  enhanced," and the text calls it *"skeleton **radial** growth"* while measuring lengths.
- **Mice do not fuse**, and the authors concede it: *"there is no epiphyseal fusion at the time of sexual
  maturation in mice and we cannot figure out the reason of chondrocytes depletion."*
- *Int J Clin Exp Med* is not a MEDLINE-indexed journal.

## 3. WHAT SURVIVES — ONE RESULT, AND IT IS WORTH KEEPING

> **Oxandrolone increased the length of spine, femur and tibia in INTACT male AND female mice.**

That is **the only NAAS length endpoint in normal, gonadally intact animals I have found**, and it includes
the **spine** — the compartment R121/R122 identified as the one still open at bone age 16. If real, it is
mildly against R127's redundancy argument, because intact male mice already have endogenous androgen and
oxandrolone still added length.

**But it cannot carry weight:** no numbers, n=6, unfused species, self-contradicting paper, unindexed
journal, and 4–8-week-old mice have low baseline androgen — closer to the Turner situation than to a male
on an AI. **R127/R128's verdict stands: NAAS remain redundant on top of AI-doubled testosterone.** This
paper weakens the argument slightly; it does not overturn it.

---

## 4. ⭐ THE ANSWER TO THE ACTUAL QUESTION, BY EVIDENCE TIER

### TIER 1 — randomised or internally controlled, in humans
| | gain |
|---|---|
| GH vs **placebo** (Leschek, randomised, double-blind) | **+3.7 cm** |
| AI on top of GH (matched pairs, **≥2 years**) | **+3.3 cm**, p = 0.044 |
| **TOTAL** | **+7.0 cm → 187.3 cm** |

⚠ **Scope limit that must be applied:** measured in **short** boys at **BA 13–15**. The subject is 180.3 cm
at **BA 16** — taller, later, one bone-age year past the tested range. A discount is required and its size
is unknown.

### TIER 2 — mechanistically supported, no final-height measurement in this setting
- **erdafitinib** — h_term + matrix + NPR2 phospho-state; bone-age-neutral on operator films
- **CNP axis** (vosoritide ± sacubitril) — ≤2.4% redundant with erda, spine-competent (+0.89 cm/yr sitting
  height, **rescue-derived**)
- **disc / axial decompression** — **+1.2 cm**, fusion-independent, works at any age

### TIER 3 — no length endpoint anywhere; do not count toward the number
N-arm charge→discharge (PDGF-BB/MHY1485/local GH → vismodegib); AR antagonist as charge agent (MSC data
only); VinSpinIn/SPIN4; NAAS on top of AI.

### The arithmetic
| scenario | result |
|---|---|
| Tier 1 only | **187.3 cm = 6'1.7"** |
| Tier 1 + disc | 188.5 cm = 6'2.2" |
| **Tier 1 + disc + CNP sustained 3 yr @ 0.5 cm/yr** | **190.0 cm = 6'2.8"** |
| **TARGET** | **195.6 cm — shortfall 5.6 cm** |

> **6'2"–6'3" is defensible on current evidence. 6'5" is not — and the reason is not that the biology
> forbids it. R124 put the empirical ceiling of the oestrogen-removal lever at 204 cm, well above target.
> The target is above what the EVIDENCE supports FROM A BONE-AGE-16 START, which is a different and
> narrower objection than the one I was making ten rounds ago.**

---

## 5. ⭐⭐ THE VARIABLE THAT DOMINATES EVERYTHING, AND IT IS TIME

The matched-pair anastrozole data is **binary on duration**:

| exposure | result |
|---|---|
| **≥2 years** | 173.1 vs 169.8 cm — **+3.3 cm, p = 0.044** |
| **1 year** | 172.0 vs 171.6 cm — **+0.4 cm, p = 0.730 — nothing** |

> **Under two years the AI contributes zero. It is the largest single defensible term in the entire stack,
> and it does not exist below a two-year threshold. Every month of delay subtracts directly from the
> biggest number available.**

Nothing else in this file — no compound, no dataset, no mechanism — has that property. **Duration on the
AI is the highest-leverage variable and it is the one that is purely a function of starting sooner.**

---

## 6. WHAT WOULD ACTUALLY CLOSE THE REMAINING 5.6 cm

Ranked by expected value, honestly:

1. **Measure the compartments (R122).** Sitting height vs subischial leg length, plus ring-apophysis
   staging. **Hand bone age reports the compartment that is finished, not the one with budget.** A tape
   measure and one radiograph, and it decides where everything should be aimed. Still not done.
2. **NT-proCNP.** Decides whether the entire CNP arm does anything. One assay.
3. **The N arm is the only place the remaining 5.6 cm can come from**, and it has no length endpoint in any
   species. The decisive experiment is R119's: **charge then discharge, measure the bone** — now runnable
   with two approved agents (PDGF-BB → vismodegib).
4. **The Col2-ARKO resting-zone measurement (R128)** — decides whether AR antagonism is a real charge agent.

---
### Corrections and status carried by this round
- **Zhou 2015's EMT/MET framework is NOT SUPPORTED in human zonal data** — mesenchymal and TGF-β arms at
  chance, SMAD3 and ACTA2 inverted. The paper additionally contradicts itself between abstract and
  discussion.
- **One result kept**: oxandrolone raised spine/femur/tibia length in intact mice — the only NAAS length
  endpoint in normal animals, unquantified, and insufficient to overturn R127.
- **The target is re-scoped**: not forbidden by the biology (ceiling 204 cm), but **above what the evidence
  supports from a BA-16 start.** Defensible best is **190.0 cm (6'2.8")**.
- **New top-priority finding: the AI's benefit is BINARY at two years.** Time on drug now outranks every
  compound question in the file.
