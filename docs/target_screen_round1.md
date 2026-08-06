# Compound hypotheses from the graph — round 1

**Status: HYPOTHESES. Nothing here is evidence that any compound increases human height.**
Every row is "if the sign propagates, and if the drug reaches cartilage, and if the
weakest edge on the path holds" — three conditionals, each of which can be false.

Method: `atlas/tools/target_screen.py`. Reproduce with `--extract --resolve --report`.
Expression filter: `atlas/tools/gp_expression.py` over GSE288028.

---

## 1. How the screen works, and the bug that nearly invalidated it

For every node with a signed, traversable path into an elongation variable, the screen
multiplies `drug action × path net sign × variable elasticity` and reports a predicted
direction on height. Elasticities come from the flow model:

    elongation = (N_p / T_c) × h_term / f_cell × mechanical      →  N_p +1, T_c −1, h_term +1

**A drug may only be attached to a molecular-entity node.** This was not true in the
first run and it inverted a conclusion. `aromatase_deficiency_human` is a *phenotype*
node whose name contains "CYP19A1", so every aromatase inhibitor was attached to it —
but that node's path already encodes loss of enzyme activity, so the inhibitor's own
negative sign double-counted and **anastrozole came out predicted to decrease height.**
Both the right and wrong routes were emitted and the wrong one sorted first. Fixed by
restricting compound attachment to `gene / protein / hormone / metabolite` nodes, with a
short declared curated map for pathway nodes (mTORC1, MEK/ERK, Notch, TGF-β, HIF, Pi/PPi)
whose names carry no bare gene symbol.

## 2. Controls — all four pass

| control | expected | result |
|---|---|---|
| mTOR inhibitors (26 compounds) | negative — sirolimus suppresses growth in children | **all 26 predicted −** on h_term |
| glucocorticoid receptor agonists | negative | **predicted −** on proliferation |
| aromatase inhibitors | positive via delayed fusion | **predicted +**, grade A |
| FGFR3 inhibitors | positive | **predicted +** |

## 3. Filter cascade

| stage | compounds |
|---|---:|
| ≥1 predicted-positive route | 122 |
| target detected in ≥2/4 human growth-plate donors (GSE288028) | 106 |
| path grade A–C | — |
| not already an L12 node | **105** |

## 4. The hypotheses worth arguing about

Ranked by weakest grade on the path, then by absence of a predicted harm.

| target | example compound | phase | helps | predicted harm | grade | refs on the path |
|---|---|---|---|---|---|---|
| **TGFBR1** | galunisertib | 2 | h_term | none | **B** | serra1997, yang2001 |
| **EGLN1 (PHD)** | vadadustat, roxadustat, daprodustat | **4** | proliferation | none *(but see below)* | C | schipani2001, brighton1971 |
| **ADAMTS5** | aldumastat | 2 | h_term | none | C | glasson2005, majumdar2007, song2007, bendre2025 |
| **NOTCH1/2** | brontictuzumab, γ-secretase inhibitors | 2 | N_p, prolif, h_term, fusion | none | C | mead2009, dy2012, kohn2015 |
| **LEPR** | metreleptin | **4** | h_term, N_p | none | C | kishida2005 |
| **TRPV4** | (tool agonists) | — | h_term | proliferation | C | khatib2023, stokes2002 |
| **THRB** | thyroid β-agonists | — | h_term, prolif | none *(screen missed fusion)* | C | — |

### Why EGLN1 is the most interesting row and also the most dangerous

HIF-prolyl-hydroxylase inhibitors are **approved, oral, and already taken chronically**
by renal patients. The growth plate is the most hypoxic tissue in the body and HIF1α is
*required* there — cartilage-specific `Hif1a` deletion kills the interior of the plate
(schipani2001). Stabilising HIF is predicted to support the proliferative compartment.

**And the screen cannot see the obvious risk.** HIF stabilisation drives VEGF, and
vascular invasion at the chondro-osseous junction is what *terminates* the plate. A drug
that raises HIF could plausibly accelerate the very process that ends growth. The atlas
has no edge for it, so the "harms" column is empty — which is an absence of an edge, not
an absence of a risk. This is the clearest example in the whole screen of why an empty
harm column means nothing.

### Why ADAMTS5 is the only row without an exposure problem

Every other candidate has to reach an avascular, alymphatic tissue whose drug
concentration has never been measured in any species (`g_l12b_002`). **ADAMTS5 inhibitors
are the one class on this list designed from the start to act in cartilage**, because
they were developed for osteoarthritis. Whatever else is true of them, the exposure
argument that kills most candidates does not apply.

## 5. What this screen structurally cannot do

1. **Exposure.** Nothing here models whether a compound reaches the plate.
2. **The time axis.** `growth_velocity_longitudinal` is a sink in this graph — 45 edges
   in, 0 out — so a predicted *velocity* gain is not a predicted *adult height* gain, and
   the screen cannot tell them apart. Every velocity-raising agent in clinical use loses
   part of its gain to accelerated maturation.
3. **Absent edges.** A compound with an empty harm column has no *recorded* harm. See
   EGLN1 above.
4. **Grade is a ceiling, not a score.** A grade-C path means the weakest link is one
   animal study. Six of the seven rows above are grade C.

## 6. Next

Per-zone scoring rather than whole-plate: the expression filter currently asks "is this
transcribed anywhere in the plate", when the question is "is it transcribed in the zone
the path runs through". That needs the zonal cluster assignments from Chu 2026
(PMID 41984930), which is the top open row in `atlas/sources/access_queue.md`.

---

# ROUND 1 AMENDMENT — the Chu preprint arrived and demoted the top hit (2026-08-06)

Source: **Chu TL *et al.*, bioRxiv 2025.03.14.642964** (`chu2025pre`, tier T6). This is
the **preprint** of `chu2026` (PMID 41984930), not the published paper — same study,
different title, not peer-reviewed, numbers may have moved. Every value below is
preprint-derived and flagged as such.

## 1. TGFBR1 — the grade-B, "no predicted harm" row now has a harm, and it is human

The screen ranked TGFBR1 inhibitors first: `tgfb_signaling_chondrocyte —inhibits[−]→
chondrocyte_hypertrophy`, grade **B**, refs `serra1997` + `yang2001` — both **mouse
genetics**. Disinhibit hypertrophy, get bigger terminal cells.

The preprint reports, in **human growth-plate explants**:

- the quiescent stem population **GP1** sits in a **TGFβ-low** niche and actively
  suppresses the pathway, upregulating the soluble inhibitors **THBS1, THBS2, THBS4,
  DCN** — the most highly expressed TGFβ-related genes in that cluster;
- **GH stimulates explant growth and resting-zone proliferation by *activating* TGFβ**,
  autocrine, alongside JAK/STAT and ERK;
- EdU labelling in 7 vehicle vs 6 GH-treated patients: **P = 0.013 in one zone,
  P = 0.79 in the other**.

So in human tissue, TGFβ activation is part of how the principal growth hormone works,
and TGFβ-low is the signature of *quiescence*. **A TGFBR1 inhibitor is therefore
predicted to hold stem cells quiescent** — a harm to N_p and proliferation that the
graph had no edge for, so the screen's harm column was empty. Human tissue outranks
mouse genetics here.

**The row is not deleted, because the two claims concern different variables** —
TGFβ may restrain *hypertrophy* (mouse) while sustaining *stem-cell proliferation*
(human). But "grade B, no predicted harm" was wrong, and the corrected reading is a
velocity-versus-duration trade:

> TGFβ inhibition → fewer, larger terminal cells and a better-preserved stem pool.
> Whether that nets positive depends entirely on the time axis the flow model does not
> have, since a preserved resting zone delays exhaustion and therefore fusion
> (`rz_depletion_causes_fusion`, `stem_cell_exhaustion_fusion`).

That is a genuinely testable prediction and it was not visible before this paper.

## 2. GH acts on the resting zone, not the proliferative zone

One of the two EdU zones is significant and the other is flatly not (P = 0.79). Read
with the abstract's "promoted stem cell proliferation", GH's direct action is on the
**stem compartment**. Mapped onto the flow model, GH raises **N_p** — cells fed into the
column — rather than shortening **T_c**. That is consistent with `hunziker1989`
(acceleration without increased proliferation rate) and it means the 80 %-of-uncertainty
parameter may not be the one GH moves at all.

*Caveat: which zone carries which p-value is read from the figure panel text in the
extracted PDF and has not been confirmed against the published figure.*

## 3. The donors are children being operated on for being too tall

The biopsies come from **epiphysiodesis to prevent idiopathic tall stature** in
Scandinavian adolescents. Every expression value in
`query/human_growth_plate_expression.csv` — and therefore every "target is expressed in
human growth plate" filter decision in this document — comes from plates selected for
growing too much. There is no normal-stature paediatric growth-plate scRNA-seq to
compare against. This caveat is now in the tool's own header.

## 4. Per-zone expression now exists

`query/human_growth_plate_expression.byzone.csv`, built with the preprint's published
markers — GP1/2 stem (SFRP5, APOE, GAS1), GP3 proliferative (CCND1), GP4
pre-hypertrophic (IHH, MEF2C), GP5 hypertrophic (COL10A1). It is a **marker-score
approximation, not their clustering**: their labels are not in the GEO deposit, GP1 and
GP2 cannot be separated by markers alone, and they regressed cell-cycle signal out of
their embedding while this does not.

Zone assignment is also wildly donor-dependent — GP5 runs 448 / 2,388 / **4,021** / 51
cells across the four — so per-zone rates must be compared within a donor and agreed
across donors, never pooled.

## 5. What this changes about what to get next

Chu is no longer the top ask. The screen's remaining weakness is that **six of seven
surviving rows are grade C — one animal study at the weakest link.** The next request is
the primary papers behind those links, and `schipani2001` (EGLN1/HIF) first, because it
is the one whose compound class is already approved and orally dosed.

---

# ROUND 2 — the connectivity route is blocked; human genetics is the arbiter

## A. What I tried, and it failed

GSE288028 contains the only human growth-plate **drug-response** experiment in existence:
GH vs vehicle explants, 24 h, **3 paired patients**. If a GH signature could be derived
from the tissue GH demonstrably grows, it would be a template — find compounds whose
transcriptional signature resembles it (LINCS/CMap logic). SigCom-LINCS, Enrichr and
L1000CDS2 are all reachable.

**It does not work on this deposit.** Canonical GH/STAT5 targets, log2FC per patient:

| gene | pt1 | pt2 | pt3 |
|---|---:|---:|---:|
| SOCS2 | 0.10 | −0.15 | 0.12 |
| CISH | −0.17 | 0.01 | **2.00** |
| IGF1 | 0.24 | −0.88 | **2.31** |

**One patient of three responds.** Restricting to the stem zone — where the preprint says
GH acts — does not rescue it; SOCS2 goes *down* there (mean −1.09). And cell composition
swings ~5-fold between paired libraries of the same patient (stem zone pt3: 524 vehicle
vs 2,885 GH), so a pseudobulk contrast is confounded by capture, not biology.

**This does not refute the preprint.** Their positive result is EdU incorporation
(P = 0.013), a protein-level readout, with their own integration and batch correction on
data I don't have. My method is cruder and it failed. Recorded because a blocked route
that looks promising will otherwise be attempted again.

## B. The structural problem the screen was solving the wrong version of

| compartment | incoming signed, traversable edges |
|---|---:|
| `chondrocyte_hypertrophy` | 31 |
| stem / resting-zone nodes (8 nodes combined) | **13, and ZERO from L3 signalling** |

Only 8 of 39 L12 compounds reach the stem compartment at all, and all 8 are the already-
known axes (GH, AIs, oestrogen, octreotide, pegvisomant).

So round 1 generated 105 candidates against **hypertrophy and proliferation — the
well-connected parts of the graph — while two independent results say the movable lever
is the stem compartment**: Chu's EdU (GH acts on the resting zone, P = 0.013 vs P = 0.79)
and `hunziker1989` (acceleration without increased proliferation rate). The screen looked
where the light was.

## C. The arbiter: human height genetics

**Human genetics is a lifetime, whole-organism, population-scale dose-response experiment
on every gene, already run.** It is the only readout that integrates velocity *and*
duration — precisely what the flow model cannot do, since `growth_velocity_longitudinal`
is a sink. A gene whose loss-of-function makes people taller has already answered the
question the atlas is structurally unable to ask.

First result, and it reverses a reversal:

| target | Open Targets height association | reading |
|---|---|---|
| **TGFBR1** | **Proportionate tall stature (0.27)**, Disproportionate tall stature (0.12) | LoF → **taller** |
| **TRPV4** | Mild short stature (0.12) | LoF → shorter, so agonism → taller |

TGFBR1 tall-stature association is consistent with **Loeys-Dietz syndrome** (TGFBR1/TGFBR2
loss-of-function, marfanoid tall habitus) — *needs the primary to confirm direction and
effect size, and is recorded as unconfirmed until then.*

**TGFBR1 has now moved three times in one session:**

1. ranked **#1** — mouse genetics, TGFβ restrains hypertrophy (`serra1997`, `yang2001`)
2. **demoted** — human explant, TGFβ activation is part of how GH works (`chu2025pre`)
3. **back up** — human genetics, LoF associated with tall stature

Three lines, two of them human, pointing 2:1 toward *inhibition raises height*. The
explant objection stands and is not dissolved — it predicts a cost in stem-cell
proliferation — but a whole-organism human genetic readout outranks a 24 h explant
transcriptome, and it already integrates whatever that cost is.

TRPV4 is internally consistent with the screen: the screen predicted TRPV4 **agonists**
help h_term, and human LoF causes short stature.

## D. The pipeline from here

| stage | status |
|---|---|
| 1. graph mechanism screen | done — 105 candidates |
| 2. human growth-plate expression, per zone | done |
| 3. **human height genetics as arbiter** | running across all screen targets |
| 4. cartilage exposure filter — cartilage is polyanionic (aggrecan GAG fixed charge), so cations partition *in* by Donnan equilibrium; computable from ChEMBL properties | not built |
| 5. hand-audit of primaries for survivors | needs the papers |

Stage 4 is worth stating plainly because nobody applies it: the exposure problem that
kills most growth-plate candidates is not uniform across compounds. **Net charge at
pH 7.4 predicts cartilage partitioning**, and it is a free filter on all 105.

---

# ROUND 2 RESULT — the arbiter ran, validated, and killed two of my own rows

`atlas/tools/height_genetics.py`, 20 of 25 screen targets resolved against Open Targets.

## Validation: every gene with known human stature genetics returns correctly

| gene | tall | short | known human biology |
|---|---|---|---|
| GHR | — | 7 | Laron syndrome, GHR LoF → short ✓ |
| IGF1 | — | 4 | IGF1 deficiency → severe short ✓ |
| IGF1R | 2 | 1 | deletion → short, duplication → tall ✓ |
| FGFR3 | 2 | 7 | **both, correctly** — GoF achondroplasia (0.82) short, LoF CATSHL tall ✓ |
| PTHLH | — | 11 | PTHrP LoF → brachydactyly/short ✓ |

The arbiter works. That makes its negative verdicts credible.

## It kills two rows the screen produced

**TRPV4 — dead.** Screen predicted TRPV4 **agonists** raise h_term. Human genetics:
autosomal dominant brachyolmia **(0.71)**, parastremmatic dwarfism **(0.65)**, brachyolmia
(0.51) — and the TRPV4 skeletal dysplasias are **gain-of-function**. So TRPV4 activation
causes *short* stature in humans. My earlier note that "LoF → shorter, so agonism →
taller" was wrong about which direction the mutations run. **Row withdrawn.**

**MAPK1/ERK — contradicted.** Screen predicted MEK/ERK inhibition helps N_p. Human
genetics: `MAPK1 → Short stature (0.48)`. Disrupting ERK2 shortens humans. **Row
downgraded.**

## TGFBR1 — still the top row, and the primary is now *more* necessary, not less

| | |
|---|---|
| TALL | Marfan syndrome (0.44), **Marfan syndrome type 2 (0.38)**, **Proportionate tall stature (0.27)**, Disproportionate tall stature (0.12) |
| SHORT | **none** |

Four tall associations, zero short. But "Marfan syndrome type 2" is the ontology's name
for **Loeys-Dietz**, and that carries a trap I have to state against my own candidate:

> **The Loeys-Dietz paradox.** LDS is caused by TGFBR1/TGFBR2 mutations that are
> kinase-impairing at the receptor, yet the affected tissues show *increased* TGF-β
> signalling. The mutations are missense with dominant-negative behaviour, not clean
> null alleles. **A pharmacological TGFBR1 inhibitor therefore may not phenocopy the tall
> stature at all** — it may do the opposite of what the syndrome's downstream biology
> does.

So the genetic signal is real and one-directional, and it still does not establish that
inhibiting TGFBR1 makes anyone taller. Combined with `chu2025pre` (TGFβ activation is
part of how GH works in human explants), the honest status of my top candidate is
**unresolved, with three lines of evidence pointing in three different directions.**

## And the arbiter is silent exactly where I most needed it

**EGLN1, ADAMTS5, NOTCH1, NOTCH2: no stature association at all.** Not refuted —
absence here is dominated by what has been studied — but it means the approved-drug row
(EGLN1) and the only-class-that-reaches-cartilage row (ADAMTS5) have **nothing but
grade-C animal evidence supporting them**, and no human genetic check is available.

That raises rather than lowers the value of `schipani2001` and `glasson2005`: they are
now the *entire* evidential basis for the two most practically interesting candidates.

## Net effect on the request list

| paper | why it moved |
|---|---|
| **PMID 15731757 / 16928994** (Loeys-Dietz) | unchanged as #1, but now needs the **allele class** as well as the stature numbers — missense vs null decides whether an inhibitor is a phenocopy or an anti-phenocopy |
| **PMID 11731479** (schipani2001) | **promoted** — sole support for the approved-drug row |
| **PMID 15800624** (glasson2005) | **promoted** — sole support for the cartilage-penetrant row |
| TRPV4 primaries | **no longer needed** — row withdrawn |
