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

---

# ROUND 3 — the three primaries arrived and killed both top candidates

`serra1997` (PMID 9334353), `loeys2005` (PMID 15731757), `schipani2001` (PMID 11731479),
supplied as full text. Each was requested because it was the sole or founding support for
a candidate. Each removed the candidate it was supporting.

## 1. TGFBR1 — dead. The mouse paper never measured the thing I inferred.

The screen's #1 row rested on `serra1997` via `tgfb_signaling_chondrocyte —inhibits[−]→
chondrocyte_hypertrophy`. **The atlas edge is correct.** DNIIR mice do show increased
type X collagen, a thicker hypertrophic zone, increased IHH and reduced proteoglycan.

What the paper does **not** contain is the step I inferred from it:

- The only statement about bone size is *"MT-DNIIR **newborn** mice do not have
  detectable defects in the size or shape of specific bones"* — qualitative, from skeletal
  preparations, **at birth**.
- The growth-plate phenotype appears at **4 and 8 weeks**. **No long-bone length is
  measured at those ages, or at any age.** Three mentions of femur/tibia in the whole
  paper, none of them a measurement.
- The transgene is expressed in **periosteum/perichondrium, synovium and articular
  cartilage**, with *"lower levels ... in growth plate cartilage"* — so even the growth
  plate changes may be secondary to perichondrial signalling.

**"More hypertrophy → longer bone" was my inference, and it has never been tested in this
model.** The flow model's h_term elasticity of +1 made it feel like arithmetic; it is not.

## 2. TGFBR1 — the human genetics is weaker than the association score implied

`loeys2005`, the founding LDS paper, on the two things I asked for:

**Allele class.** Heterozygous **missense mutations in the kinase domain**, loss of
function in transfection assay. And the paper explicitly forecloses the reading a drug
would need:

> *"acute responsiveness is preserved in cells heterozygous with respect to
> loss-of-function mutations ... and effectively **exclude the possibility that the
> phenotype ... results from either potent dominant-negative interference or gain of
> function**"*

while simultaneously reporting **increased nuclear phosphorylated Smad2** in the aortic
wall. Heterozygous receptor LoF, *raised* downstream signalling in tissue. **A
pharmacological TGFBR1 inhibitor is not a phenocopy of this genotype** — it is closer to
its opposite.

**Stature.** There is **no height measurement anywhere in the paper.** The skeletal table
reports dolichostenomelia **4/14 (29 %)** and arachnodactyly **8/14 (57 %)** — marfanoid
habitus features, in a minority, with no centimetres and no SDS. The Open Targets
"proportionate tall stature (0.27)" association is not backed by stature data in the
founding primary.

**All four lines under TGFBR1 have now failed:** mouse never measured length; human
genetics has no stature numbers and an allele class that inverts the pharmacology; the
human explant says TGFβ activation is part of how GH works. **Row withdrawn.**

## 3. EGLN1 — the sign was backwards, and the atlas was right while the screen was wrong

`schipani2001` reports that cartilage-specific `Hif1a` deletion causes interior cell
death, **decreased p57, and INCREASED BrdU incorporation** — HIF-1α *induces growth
arrest*. The atlas edge encodes this correctly: `e00353 hif1a_chondrocyte —inhibits[−]→
chondrocyte_proliferation_rate`.

**The screen inverted it.** EGLN1/PHD2 degrades HIF-1α, so a PHD inhibitor *raises*
hypoxic signalling — but the screen applied ChEMBL's `INHIBITOR` as −1 against the node
`hypoxic_gradient_signaling`, and returned vadadustat/roxadustat/daprodustat as predicted
to **increase** proliferation. With the polarity restored they are predicted to
**decrease** it, which is what schipani2001 implies.

I had also flagged, from mechanism alone, that HIF stabilisation drives VEGF and that
vascular invasion terminates the plate. `schipani2001` confirms ectopic angiogenesis
around the dying cells. Both the proliferation arm and the vascular arm point the same
way. **Row withdrawn.**

### The third instance of one bug

| variant | what went wrong |
|---|---|
| **phenotype nodes** | `aromatase_deficiency_human` encoded loss of function; inhibitor double-negated → anastrozole predicted to *decrease* height |
| **pathway nodes** | `mtorc1_chondrocyte` had no bare gene symbol → the mTOR control silently produced zero rows |
| **negative-regulator subunits** | `EGLN1` degrades its own pathway → PHD inhibitors predicted with the wrong sign |

All three are the same error: **a compound attached to a node that is not its target.**
Curated genes now carry an explicit **polarity**, and the rule is stated in the tool: a
drug may be attached only to a node whose relationship to its actual target is identity,
or to a curated node with a declared polarity.

## 4. What is left

| target | status |
|---|---|
| ~~TGFBR1~~ | withdrawn — round 3 |
| ~~EGLN1~~ | withdrawn — round 3, sign inverted |
| ~~TRPV4~~ | withdrawn — round 2, human genetics |
| ~~MAPK1/ERK~~ | downgraded — round 2 |
| **ADAMTS5** | **standing.** Grade C, no human stature association either way, and still the only class designed to reach cartilage. `glasson2005` not yet read. |
| **NOTCH1/2** | standing. Grade C, helps all four variables, no human stature association. |
| **LEPR** | standing. Grade C, approved drug (metreleptin). |

**Four of seven rows are gone, and every one was removed by a paper I asked for rather
than by re-reading what I already had.** That is the screen working as designed: it
generates hypotheses cheaply and they are meant to be cheap to kill.

## 5. The finding that outranks all of the above

`serra1997` increased hypertrophy and **never measured bone length**. `hunziker1989`
reports growth acceleration **without** increased proliferation. `chu2025pre` puts GH's
action in the resting zone, not the proliferative zone.

Three independent results converge on the same warning: **the flow model's clean ±1
elasticities describe an identity, not a causal chain.** Moving h_term or proliferation
in a mouse has repeatedly failed to move length, or has never been checked. Until a
compound is shown to change a growth-plate variable *and* the resulting bone length in
the same animal, every row this screen produces is an arithmetic prediction about a
system that has not been shown to behave arithmetically.

---

# ROUND 4 — `hunziker1989` reframes the objective, and `glasson2005` kills the last strong row

## 1. ADAMTS5 — withdrawn

`glasson2005`, on the knockout, in its own words:

> *"There were **no abnormalities in total body weight** ... or histological appearance of
> **any tissue examined**, indicating that **ADAMTS5 enzyme activity is not critical for
> normal development and growth**."*

Femur and sternum were among the tissues examined, and proximal tibial growth plates were
analysed specifically. An ADAMTS5 inhibitor is predicted to do nothing to height.
**Five of seven rows are now gone.** Standing: NOTCH1/2 and LEPR, both grade C, neither
with a human stature association.

## 2. `hunziker1989` — the screen was optimising the wrong objective

Rat proximal tibia, n = 6 per age, stereology + fluorochrome labelling + ³H-thymidine
autoradiography. **Table 4, recovered in full:**

| parameter | 21→35 d (**+20 % growth**) | 35→80 d (**−75 % growth**) |
|---|---:|---:|
| **final cell HEIGHT** | **+23 %** | −53 % |
| final lateral diameter | **−14 %** | +13 % |
| **final cell VOLUME** | **−13 %** | −56 % |
| matrix volume per cell | **0** | **0** |
| cell cycle time | −33 % | 0 |
| **cells produced per column per day** | **0** | −50 % |
| columnar growth fraction | −33 % | −50 % |
| duration of hypertrophic activity | **0** | **0** |

Height 31.2 → 38.5 µm (P < 0.02); diameter 29.9 → 25.6 µm (P < 0.03); volume −13 %
(P < 0.03).

### Three consequences, in ascending order of importance

**(a) Volume is not the causal variable — height is, and they move in opposite
directions.** Growth rate rises 20 % while terminal cell *volume falls 13 %*. The field's
central quantitative claim — final hypertrophic **volume** is the strongest correlate of
elongation rate (`breur1991` r = 0.98, `cooper2013`) — is a *between-plate* correlation.
*Within* a plate across ages, volume and height dissociate and **only height tracks
growth**. My rewrite of `g_l1arch_009` to prioritise obtaining a human *volume* was
therefore aimed at the wrong quantity; the human **height** contradiction (33 vs 20.5 µm,
C-L1-07) is the one that matters.

**(b) `N_p` and `T_c` are not independent — they cancel.** Cycle time falls 33 % (81 → 54 h)
and the columnar growth fraction falls 33 % (27 → 18 cells), so **cells produced per
column per day is unchanged**. The only data that exist on their joint behaviour say they
are anticorrelated with a conserved ratio. **`flow_model.py` samples them independently**,
which inflates the uncertainty of their product and is why `T_c` scores 80 %. That
ranking is an artefact of an independence assumption this paper contradicts.

**(c) The pharmacological objective is a SHAPE change, not a size change.** Physiological
acceleration makes the terminal chondrocyte **taller and narrower at constant-or-lower
volume**. Hunziker's term is *phenotype modulation*. The entire CNP/FGFR3 therapeutic
programme targets hypertrophic **enlargement**. **Nothing in the atlas's L12 layer targets
cell shape**, and the machinery that sets a chondrocyte's aspect ratio — cytoskeleton,
cell-volume regulation, the pericellular matrix that constrains lateral expansion — is
where the screen should have been pointed.

That is a different target class from anything round 1 produced, and it follows directly
from the one paper that measured which variable actually carries a physiological change
in growth rate.

## 3. Also entered

- **hypertrophic phase duration is an invariant**: 51 / 45 / 48 h across a four-fold
  range of growth rate (CE 4.1–8.7 %). About two days, regardless.
- **matrix per cell is unchanged in BOTH directions**, so matrix synthesis is a large
  *contributor* to elongation but not a *regulator* of it. The "matrix is an unmoved
  lever" idea from round 1 §5 is withdrawn — it is unmoved because physiology does not
  move it either.
- `byers2000` is **human RIB**, not long bone. Proliferative and hypertrophic zone heights
  fall with age, matrix volume fraction and septal thickness rise. Useful, but it is not
  the distal-femur dimension set the flow model wanted, and is recorded as rib.

## 4. Score after four rounds

| round | candidates standing |
|---|---|
| 1 (graph screen) | 7 |
| 2 (human genetics) | 5 — TRPV4, MAPK1 out |
| 3 (three primaries) | 3 — TGFBR1, EGLN1 out |
| 4 (`glasson2005`) | **2** — ADAMTS5 out |

**Every removal came from a paper requested and read, not from re-reading what was
already held.** Two rows survive on grade-C animal evidence alone, and the most useful
output of the exercise is not a candidate at all — it is that `hunziker1989` says the
objective function was wrong.

---

# ROUND 5 — the shape screen, and why it returns nothing

Following `hunziker1989`, the objective was re-pointed from hypertrophic *volume* to
terminal cell *aspect ratio*. Two attempts, one negative result each, and the second is
the useful one.

## A. Deriving the shape machinery from human tissue — the dataset cannot support it

`atlas/tools/shape_screen.py` contrasts the human hypertrophic zone against the
proliferative zone, per donor, in GSE288028. It was run three times and **the first two
results were contamination signatures**:

| version | top hits | what they actually were |
|---|---|---|
| 1 — GP5 markers `COL10A1, IBSP, SPP1` | BGLAP, DMP1, MEPE, SATB2, COL1A1/2 | **osteoblasts.** IBSP and SPP1 are bone matrix genes; I added them to the marker set myself. Chu's published GP5 marker is COL10A1 alone. |
| 2 — Chu markers, osteoblasts excluded | LAPTM5, FYB1, SAMHD1, CXCR4, CD44 | **marrow.** The chondro-osseous junction is continuous with marrow and a COL2A1-positive gate does not exclude leukocytes. |
| 3 — blood excluded, marker threshold enforced | — | **refuses to report** |

At defensible stringency only **one of four donors** yields both a GP3 and a GP5 pool.
The tool now halts rather than reporting, because relaxing the gate is precisely what
produced versions 1 and 2.

The reason is not depth alone — the four libraries are not comparable tissue:

| donor | cells | median UMI | COL10A1 > 200 cpm |
|---|---:|---:|---:|
| d1 | 5,295 | 5,008 | 118 (**2 %**) |
| d2 | 12,911 | 4,906 | 501 (**4 %**) |
| **d3** | 9,115 | **10,041** | 6,433 (**71 %**) |
| d4 | 383 | 3,339 | 15 (4 %) |

Donor 3 has twice the depth *and* a twenty-fold different zonal composition. Any
cross-donor contrast is donor 3 alone.

**This is the third independent failure of GSE288028 as a reuse substrate** — after the
GH signature (1 of 3 patients responding) and the 5-fold composition swings between
paired vehicle/GH libraries. It is the only human growth-plate scRNA-seq that exists, and
it will not carry this weight.

## B. Screening the graph for shape — zero hits, and that is the result

A node now exists for the variable: **`terminal_cell_shape_modulation`**, carrying
Hunziker's height (31.2 → 38.5 µm), diameter (29.9 → 25.6 µm), volume (−13 %), and a
derived aspect ratio **1.04 → 1.50**. It is wired to `growth_velocity_longitudinal`
(grade C) and records the volume dissociation explicitly as a **dissociation, not a
dependency**.

`target_screen.py` now carries `shape` as an outcome. Re-run:

> **0 of 209 upstream nodes have a signed, traversable path into it.**

Every shape-adjacent route in the atlas — `pericellular_matrix`,
`cartilage_osmotic_swelling`, `cytoskeletal_tension_chondrocyte` — terminates in
`hypertrophic_volume_increase`, and both of the relevant edges are speculative and
traversal-unusable. There was no node for cell height or aspect ratio anywhere in 621
nodes before today.

**So the screen cannot be run, and the reason is not a tooling limit: nobody has mapped
what controls the aspect ratio of a hypertrophic chondrocyte.** Opened as
`g_l1arch_016`.

## C. What that changes about the request

The bottleneck is no longer compound identification. It is that **the causal layer under
the one variable that demonstrably carries growth-rate change is empty**, and it is empty
in the literature, not just in this atlas.

The honest first move is also the cheapest: **`hunziker1989` has never been replicated,
in any species, and the entire reframing rests on it.** Six of the seven candidates from
round 1 were killed by primaries; this reframing deserves the same treatment before more
is built on it.

| want | why |
|---|---|
| **PMID 3543020** — Hunziker, Schenk & Cruz-Orive 1987, the companion stereology paper | baseline height, diameter and volume by zone, and the method behind the 1989 numbers. Held as `primary` with no full text read. |
| any **replication** of height-and-diameter-measured-separately at two growth rates | the reframing rests on one 1989 study with n=6 |
| **PMID 20550897** — Darling 2010, chondrocyte pericellular matrix mechanics | the only proposed mechanism for anisotropic constraint; held abstract-level |
| **PMID 10579729** — Costell 1999, perlecan null | currently `primary_abstract_only`; perlecan is the strongest PCM lead |
| PCM / collagen VI growth-plate micromechanics (e.g. Prein *et al.*, *Matrix Biol* 2016) | not in the atlas at all |

---

# ROUND 6 — the replication exists, and it is a different lab, a different perturbation and three species

## 1. What was NOT obtained

**`hunziker1987` (PMID 3543020) is still unread.** The supplied PDF is a *Literature
Abstracts* listing page from *J Pediatr Orthop* 1987 which cites the paper by title and
journal and carries **no abstract and no body text**. The bibliography records this
explicitly so the row is not later mistaken for a read source.

## 2. Item #2 found, and it survives

I asked for "any replication of height-and-diameter-measured-separately at two growth
rates" and could not name one. Two exist, from a different group, and the stronger is
**interventional** rather than observational.

**`stokes2007` (PMID 17532281)** — rat and cattle vertebrae, rat/cattle/rabbit proximal
tibia, sustained compression or distraction altering growth rate by up to 53 %:

| predictor of altered growth rate | correlation | regression coefficient |
|---|---:|---:|
| **final maximum chondrocytic height** | **0.56** | **1.39** |
| number of proliferative chondrocytes per unit width | 0.38 | 0.72 |

> *"chondrocytic enlargement made a greater contribution to altered growth rates"*

**This replicates hunziker1989's ranking — cell enlargement over proliferation — in a
different laboratory, under a mechanical rather than developmental perturbation, across
three species and two anatomical sites.** It does not replicate the *height/volume
dissociation*, because Stokes measured only height.

**`stokes2002a` (PMID 15456065)** agrees in direction (mean cell height r = 0.41) and
**cuts against a pure shape account**: the authors state the percentage changes in
chondrocyte dimensions were **smaller** than the percentage changes in growth velocity.
Under mechanical loading, cell height does *not* fully account for the growth change —
unlike Hunziker's physiological comparison, where +23 % height carried +20 % growth almost
exactly. Effects were also larger for compression than distraction.

**Verdict: the ranking replicates; the completeness does not.** Cell height is the largest
single contributor to a growth-rate change in every design tested, and it is sufficient in
one of them.

## 3. `hunziker1994` — and this one corrects me

Hypophysectomised rats infused with IGF-I or GH, same laboratory, same stereology:

| parameter | untreated | IGF-I | GH |
|---|---:|---:|---:|
| stem cell cycle time | 50 d | 15 d | **8 d** |
| proliferating cell cycle time | 11 d | 4.5 d | **3 d** |
| **duration of hypertrophic phase** | 6 d | 4 d | **2.8 d** |
| matrix volume per cell | \-\-\- unchanged in all groups \-\-\- | | |
| cell height and volume | reduced | **restored** | **restored** |

**In round 4 I recorded hypertrophic-phase duration as "an invariant of the system,
about two days regardless." That was wrong as a general claim.** It is invariant across
*physiological* states in normal rats (45–51 h, `hunziker1989`); GH **more than halves it**
in a hypophysectomised one. Likewise `hunziker1989` found cycle-time changes cancelling
against growth fraction — under hormone rescue they do not cancel at all.

> **Pharmacology moves parameters that physiological variation holds fixed.**

That is the most encouraging single finding of this whole exercise for the compound
question, and it cuts directly against the conclusion I was drifting toward — that the
system is homeostatically defended on every axis. It is not. It is defended against
*physiological* perturbation.

The honest limit: everything here is **rescue from deficiency**, not augmentation above a
normal baseline. Cell height was *restored*, never exceeded, and cell productivity did not
reach normal with either agent. Whether any of these parameters can be pushed above
normal is untested by this design.

## 4. The shape mechanism now has its first measured numbers

`prein2016`, AFM on mouse growth plate:

| | |
|---|---|
| pericellular / territorial matrix | **1.6 ± 0.01 kPa** |
| interterritorial matrix | **3.6 ± 0.1 kPa** |
| chondrocyte shape index | **1.57** |

**The cell sits in a soft shell inside a matrix 2.25× stiffer.** That is the mechanical
architecture an anisotropic-constraint account of shape modulation requires, measured for
the first time. The gap that remains is exactly specified: this is a *radial* measurement
in the proliferative zone, and **nobody has measured whether the constraint differs
axially versus laterally**, which is the only thing that would channel expansion into
height rather than width.

`costell1999` closes one route: the perlecan null is a **chondrodysplasia** — reduced and
shortened fibrillar collagen — so perlecan loss shortens bone and is not a height lever.
`darling2010` is **articular** cartilage, not growth plate, and is recorded as such.

## 5. Where this leaves the compound question

| claim | status after round 6 |
|---|---|
| cell height is the dominant contributor to growth-rate change | **replicated**, 3 species, 2 designs, 2 labs |
| height and volume dissociate | **unreplicated** — only Hunziker measured both |
| hypertrophic-phase duration is invariant | **false as stated** — GH halves it |
| the parameters are pharmacologically movable | **yes**, at least from deficiency |
| what sets the aspect ratio | **still unknown**; PCM/ITM stiffness ratio measured, axial vs lateral anisotropy never measured |

The screenable target is now specific enough to state: **an agent that increases the
axial-to-lateral stiffness ratio of the constraint around a terminal hypertrophic
chondrocyte, or that biases its volume increase along the growth axis.** No compound in
the atlas's L12 layer acts on either, and `g_l1arch_016` records the experiment that would
test it.
