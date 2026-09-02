# Round 24 — can the clock be reversed? The instrument exists. The link does not.

**Date:** 2026-08-07 · **Branch:** `claude/growth-system-atlas-yl5esl`

Round 23 established that the clock is the integral of flux out of the resting zone, and that the
two obvious levers are spoken for. This round went at reversal directly — and the atlas's own prior
holdings narrowed the search before it started.

**Two things the atlas already knew, which decide what "reversal" can even mean:**

1. **Growth plate senescence is *not* cellular senescence** in the p16/SASP sense. It is coordinated
   division-dependent decline. So **senolytics are a category error** for it.
2. `nilsson2005` proposed the counter is a progressive DNA methylation change tracking division, and
   this atlas recorded that proposal as **untested for twenty years**.

So reversal means one thing: reset whatever counts the divisions. That is the search this round ran.

---

## 1. The finding: the clock is real, human, and resettable — and resetting it has never bought a division

New node: `atlas/nodes/L2_stem_and_progenitor_biology/epigenetic_age_reset_in_cartilage.yaml` (grade **C**).

**The clock exists, and it is human.** `sarkar2023` (Aging Cell, PMID 36638270) built a DNA-methylation
age predictor across human chondrocyte ontogeny from 8 fetal and 22 adult **uncultured** chondrocytes,
**r = 0.97, p = 2.4e-14**.

**It can be moved, by two unrelated routes.**
- A STAT3 agonist (**423F**), two weeks on aged adult human chondrocytes, lowered predicted methylation
  age in **5 of 6 donors** — and STAT3 ablation in fetal chondrocytes drove global **hyper**methylation,
  the reciprocal direction.
- `liu2026osk` (Exp Mol Med, PMID 41786976) delivered **AAV-OSK** intra-articularly in mouse, lowering
  predicted methylation age in vivo with DNMT3a down and TET2 up.

**The safety result is better than expected.** OSK-expressing chondrocytes kept their markers, showed
no rise in stemness genes, and produced **no dedifferentiation and no tumour** over 8 weeks. The
standing objection to reprogramming a growth tissue did not materialise in cartilage.

**And then the point of the whole exercise fails.** `liu2026osk` measured proliferation directly:

> the percentage of Ki67-positive chondrocytes **did not differ** between AAV-OSK and mock.

**The epigenetic age of a chondrocyte can be lowered in vivo, and no experiment has shown that doing
so restores its capacity to divide.** The link on which the entire reverse-the-clock argument
depends — epigenetic age → proliferative capacity — is the one link nobody has demonstrated.

### Why I am not overreading that null

It is a null, and this atlas does not treat a null as a demonstration of no effect. Three reasons it
is weak: adult articular chondrocytes have a Ki67 fraction near zero at baseline, so **the assay has a
floor** and the study was not designed to detect an increase; no quantitative values were given
beyond "no difference"; and **articular cartilage is not the growth plate.** What the row establishes
is not "reprogramming cannot restore proliferation" but "the one experiment that lowered chondrocyte
epigenetic age in vivo and then looked for more division did not find it."

### And the clock that exists does not test the hypothesis that matters

`sarkar2023`'s clock relates methylation to **chronological age**. `nilsson2005`'s claim is about a
counter that tracks **divisions**, and growth plate senescence is division-dependent, not
time-dependent. **A clock calibrated on time does not test a hypothesis about counting divisions.**

That gives the cheap first experiment, and it needs no new technology — new gap
`g_l2_reprogram_the_growth_plate`:

> **Apply the clock to growth plate chondrocytes separated by zone, from the same individual.** A
> division counter *must* advance from resting to proliferative **within one person**, where
> chronological age is held constant by construction. No published clock has made that comparison,
> and it is achievable on archived tissue.

---

## 2. A fourth decoupling of pool from growth, and a live confusion settled

`liu2026cih` (Advanced Science, PMID 41387208): chronic intermittent hypoxia in 3-week-old mice.

| | |
|---|---|
| growth plate length | **−31.3% ± 15.9** |
| proliferative zone | −34% |
| hypertrophic zone | −25% |
| **resting zone** | **unchanged** |
| GSK-J4 (KDM6 inhibitor) | **largely reversed** the growth impairment |

**A third of the growth plate was lost and then largely recovered without the resting-zone pool
changing at all** — a fourth independent perturbation decoupling pool size from growth, now added to
`stem_pool_size_versus_flux`.

**And it settles a confusion in the current literature.** The senescent cells here are **OSX+
metaphyseal osteoprogenitors — outside the plate** — carrying genuine p16/SASP-type markers. A
published letter (PMID 41377263, *Annals of Medicine and Surgery*, no new data) proposes senolytics
and senomorphics to *"delay epiphyseal fusion and hence restore growth potential."* **That proposal
requires growth plate senescence to be cellular senescence, and the primary evidence says it is not.**

What `liu2026cih` supports is narrower and real: clearing genuine senescence in the **peri-plate**
compartment can **protect** growth against an insult. It does not support extending growth beyond its
normal endpoint in a healthy plate, and nothing here tested that.

---

## 3. Where the whole programme now stands

Four rounds in, the honest map of "unlimited height":

| route | status |
|---|---|
| Refill the pool from an external reservoir | **Largely closed in human.** Two pathways, five markers, all negative (R22–23) |
| Enlarge the pool | **Refuted as a standalone.** Pool and growth move oppositely in 4 perturbations |
| Reverse the epigenetic clock | **Instrument exists, link unproven.** Age falls; division does not return |
| Clear senescent cells | **Category error for the plate itself.** Real, but only for peri-plate insult |
| Extend duration | Still open — and the only lever with human trial data behind it |
| **A larger pool with intact flux** | **Never attempted.** The one untested cell |

The two live experiments are both now written as gaps rather than hopes, and both are cheap:
**measure the clock by zone within one person**, and **get an equivalence bound on bone length** out of
`orikasa2024`'s and `horike2026`'s own animals.

---

## 4. Provenance, stated plainly

All three new primaries were read **through a summarisation step**, not directly, and no figures were
inspected. Each bibliography entry says so. Following CORR-023, **every PMID in this round was
resolved against Europe PMC before use** — 41786976, 41387208, 36638270, 40538142 all verified, with
`liu2026cih` corrected from 2025 to **2026** in the process.

---

## 5. Atlas state

634 nodes · 1,226 edges · 313 gaps · 1,125 refs · **0 validator errors**

New node `epigenetic_age_reset_in_cartilage` (C). New gap `g_l2_reprogram_the_growth_plate`.
New refs `sarkar2023`, `liu2026osk`, `liu2026cih`. Fourth row added to `stem_pool_size_versus_flux`.

**Sources fetched:**
[Sarkar 2023 Aging Cell](https://pmc.ncbi.nlm.nih.gov/articles/PMC9924946/) ·
[Liu 2026 Exp Mol Med](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049178/) ·
[Liu 2026 Adv Sci](https://pmc.ncbi.nlm.nih.gov/articles/PMC12822469/) ·
[Letter, used only as an example of the conflation](https://pmc.ncbi.nlm.nih.gov/articles/PMC12689101/)
