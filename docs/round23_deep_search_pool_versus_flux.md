# Round 23 — deep literature search, and the finding that redirects the programme

**Date:** 2026-08-07 · **Branch:** `claude/growth-system-atlas-yl5esl`

Round 22 answered step 1 of the clock programme with a negative: the human stromal population beside
the growth plate is Hedgehog-negative, so GLI1 is the wrong handle. This round searched the
literature for the *right* handle, tested what it found against the human data, and came back with
something better than a handle — a reason the whole "enlarge the pool" framing is wrong.

---

## 1. The finding: growth tracks FLUX through the resting zone, not the SIZE of it

New node: `atlas/nodes/L2_stem_and_progenitor_biology/stem_pool_size_versus_flux.yaml` (grade **B**).

Three independent perturbations, three laboratories, three unrelated mechanisms. **In three of the
four cells, pool size and bone growth move in opposite directions.**

| perturbation | resting-zone pool | bone growth | source |
|---|---|---|---|
| Growth hormone | **depleted** | faster, then declining | `chu2025` PNAS, PMID 41289405 |
| Hedgehog ON in PTHrP+ cells (*Ptch1* cKO) | **hyperplasia**, columns 1–2 → 5–6 cells | **no significant length change**; transient; → osteoblasts | `orikasa2024` JCI Insight, PMID 38051593 |
| FGFR3 achondroplasia knock-in | **expanded** | **shorter** femur, tibia, ulna | `horike2026` Nat Commun, PMID 41748604 |
| …+ CREB inhibitor 666-15 | **shrinks** | **restored** | `horike2026` |

The mechanism is visible in the third row: in the achondroplastic plate, clonal progeny "moved in
random directions and remained within the resting zone" — **they cannot leave**. A pool that cannot
discharge is a bigger pool and a shorter bone. And the rescue runs the other way: restoring exit
*shrinks* the resting zone while the proliferative and hypertrophic zones grow and the bone lengthens.

**Why this matters for the programme.** Every depletion argument in this atlas invites one
instinct — make the pool bigger. That instinct is now refuted as a standalone strategy. Raising final
height requires raising the **integral of flux** — capacity × duration — not the standing size of the
compartment at any moment.

**And the informative experiment has never been run.** In `orikasa2024` the enlarged pool discharged
into *bone*; in `horike2026` it could not discharge at all. **Nobody has produced a larger pool with
intact flux.** New gap `g_l2_larger_pool_with_intact_flux` states it, including the cheap partial
version: re-analyse both papers' own animals for an *equivalence bound* on bone length, which converts
two weak nulls into a quantitative statement.

**Honesty about the weakest cell.** `orikasa2024`'s bone-length result is a reported
non-significance in a mouse cohort, not an equivalence test, and this atlas does not treat an
underpowered null as a demonstration of no effect. What carries weight is the *contrast* — the
morphology moved enormously and the length did not, in the same animals — and the fact that the
descendants converted to osteoblasts, so flux was **diverted**, not increased.

---

## 2. The second handle failed the same way the first did

The mouse literature names one alternative to Hedgehog: **AXIN2**, marking Wnt-responsive
chondroprogenitors at the groove of Ranvier (`usami2019`, PMID 30602070). That is a specific,
falsifiable prediction about the human population found in Round 22, and it was declared before the
numbers were read: *if this is the groove-of-Ranvier counterpart, it should be AXIN2-positive even
though it is Hedgehog-negative.*

**It failed.** AXIN2 **0.52** — not enriched. Two independent Wnt readouts agree: NKD1 **0.05**,
TCF7 **0.57**. And across five mouse stem markers, each taken from the primary that established it:

| marker | primary | stromal / chondrocyte |
|---|---|---|
| PTHLH | `mizuhashi2018` | **0.10** |
| FOXA2 | `muruganandan2022` | **0.01** |
| CHRDL2 | `avijgan2026br` | **0.01** |
| SFRP5 | `hallett2021` | **0.00** |
| NT5E (CD73) | `newton2019` | 0.65 |
| AXIN2 | `usami2019` | 0.52 |
| APOE | `kodama2025` | 5.08 — **not read as stemness** |

Every one is depleted in the stroma and enriched inside the cartilage. APOE is the single enrichment
and it is explicitly not counted: APOE is a high-expressing stromal and myeloid gene in any tissue,
it sits at 11.15 in a neighbouring non-stromal cluster here, and `kodama2025` established it as a
marker *within* cartilage, where its meaning does not carry outside.

**Two prospectively declared predictions, from unrelated pathways, failing in the same direction.**
What is left is a population that looks like ordinary perichondrial fibroblast-lineage stroma —
COL1A1, PRRX1, PDGFRA — carrying no known progenitor programme. That is a much stronger negative
than Round 22's, and it still is not proof: absence of a known programme is not absence of a progenitor.

---

## 3. Two corrections, and one of them is the most important thing here

### CORR-022 — an absolute threshold deleted the resting zone, and gave a clean positive on the wrong cells

Both scripts called cartilage at `COL2A1 mean >= 500`. That **excluded clusters 6 and 7 — the resting
zone** — at 358 and 270. Not bad luck: `avijgan2026br` established that the human resting zone carries
**the lowest mRNA content of any zone**, in all 17 sections. An absolute expression bar deletes the
resting zone *by construction*. The threshold encoded the opposite of a known fact about the tissue.

Fixed by calling cartilage at **100× the per-donor ambient floor** instead. It **strengthened** the
Hedgehog verdict (GLI1 0.30 → 0.28) — and it **destroyed a result I would have reported**. With the
resting zone excluded, the Wnt-module test returned **2 of 2**, a clean confirmation that the mouse
niche module transfers to human. With the real resting zone in place it returns **1 of 4**: WIF1 2.80×,
FZD6 1.45×, SFRP1 1.25×, and **DKK2 going the wrong way at 0.56× on 972 counts.** The module is
*partly* conserved. The clean positive was an artefact of testing the wrong cells.

Third time in two days that a test passed for a reason I had not checked. The pattern has a name now:
**a threshold chosen because it looks obviously right encodes an assumption about the tissue, and that
assumption needs a citation like any other.**

### CORR-023 — three fabricated PMIDs, in my own tool

`stem_module_human.py`'s docstring credited each marker to its primary. Three identifiers were wrong:

| I wrote | what it actually is | correct |
|---|---|---|
| Newton 2019 = 30894746 | a MYCN/BRCA1 paper | **30814736** |
| Muruganandan 2022 = 35523776 | electroconvulsive therapy | **35523895** |
| Hallett 2021 = 34881694 | larval ecology of *Aedes mariae* | **34309509** |

They came from a review's citation table through a summarisation step, transcribed without checking.
The papers are real and the attributions are correct — **only the identifiers were invented**, which is
the most dangerous form, because everything around them is true and nothing looks wrong. Caught by
running all ten PMIDs of this round through Europe PMC: three failed.

**Standing rule.** An identifier arriving through a secondary source or any summarisation step is
unverified data, not a citation, until resolved against the primary record with a matching title —
in tooling and comments exactly as in the bibliography.

---

## 4. What this does to the programme

The clock question was: *can we slow or reverse it?* The answer this round supplies is that the clock
is **the integral of flux out of the resting zone**, and that the two obvious ways to move it are
already spoken for:

- **GH raises flux and spends the pool faster.** It moves growth earlier without adding capacity —
  which is exactly the KIGS shape the atlas already holds (first year = 35–41% of lifetime gain; a 43%
  higher dose buys more in year 1 and **nothing** at near-adult height). Recorded as consistency, not
  as evidence: the atlas also holds the selection confound that forbids the inference.
- **Enlarging the pool does not lengthen the bone** in either experiment that has enlarged one.

That leaves duration, and the untested cell. Both are now stated as gaps rather than as hopes.

---

## 5. Atlas state

633 nodes · 1,226 edges · 312 gaps · 1,122 refs · **0 validator errors**

New node `stem_pool_size_versus_flux` (B). New gap `g_l2_larger_pool_with_intact_flux`.
New refs `orikasa2024`, `usami2019`. Updated `progenitor_reservoir_outside_the_plate` with the
five-marker, two-pathway negative. Corrections **CORR-022**, **CORR-023**.
Tools: `stem_module_human.py`; `reservoir_v2.py` and `cluster_gse288028.py` amended.

**Sources fetched this round:**
[Chu 2025 PNAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC12685065/) ·
[Orikasa 2024 JCI Insight](https://pmc.ncbi.nlm.nih.gov/articles/PMC10906233/) ·
[Horike 2026 Nat Commun](https://pmc.ncbi.nlm.nih.gov/articles/PMC12946275/) ·
[Hallett 2021 eLife](https://elifesciences.org/articles/64513) ·
[Cheng, Orikasa & Ono 2025 review, used as an index only](https://pmc.ncbi.nlm.nih.gov/articles/PMC12525321/)
