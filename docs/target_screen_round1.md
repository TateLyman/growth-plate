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

---

# ROUND 7 — the anisotropy was already measured, and I said it wasn't

## The correction

Rounds 5 and 6 of this document state that nobody has measured whether the constraint
around a hypertrophic chondrocyte differs axially versus laterally, and call that the
decisive gap. **That is wrong.** It was measured in 1998.

`villemure2009`, a survey of growth plate mechanics, used as an **index** rather than a
source — which is what this atlas's source policy says reviews are for — points to:

> **The growth plate is about ten times more compliant in the axial (longitudinal growth)
> direction than in its transverse (radial) direction** — `cohen1998` (PMID 10412420),
> transversely isotropic biphasic model of unconfined compression; corroborated by
> `sergerie2009`.

Permeability is similar in both directions; the transverse Poisson's ratio is 2–3× the
out-of-plane ratio.

I could have found this at any point by asking the field's own review what had been
measured, instead of asking whether the *graph* contained it. The graph's silence was
taken for the literature's silence. That is the same error as round 1's "look where the
light is," one level up.

## What it does to the hypothesis — it strengthens it, and simplifies it

The shape result needed a mechanism, and the mechanism is now three measured facts that
fit together:

| | |
|---|---|
| matrix is **~10× more compliant axially** than transversely | `cohen1998` |
| pericellular matrix **1.6 kPa** inside interterritorial **3.6 kPa** | `prein2016` |
| terminal cell gets **taller (+23 %) and narrower (−14 %) at −13 % volume** during a +20 % growth acceleration | `hunziker1989` |

**A cell expanding inside a matrix that resists lateral expansion ten times more than
axial expansion goes up rather than out, with no active shaping machinery required.**
Hunziker's "phenotype modulation" may not be a cellular program at all — it may be what a
pressurised object does inside an anisotropic shell.

That is a *simpler* hypothesis than a shape-control pathway, and it is more tractable:
the lever is the **matrix**, not a receptor.

## What is still genuinely missing, stated correctly this time

A **static** anisotropy explains how a cell could be shaped. It does not explain why the
shaping *varies* — why a 35-day rat's terminal cells are 23 % taller than a 21-day rat's.
That requires the anisotropy ratio itself, or the cell's expansion pressure, to change
with growth rate.

> **Nobody has measured whether the axial/transverse anisotropy ratio changes with growth
> rate, age, or load.** `cohen1998` and `sergerie2009` each characterise the tissue at one
> state.

That is the gap, and it is narrower and more answerable than the one I wrote in round 5.

## Consequences for the compound question

If the anisotropy is the lever, the target class changes again — away from receptors and
toward the matrix that sets the ratio:

- collagen fibril orientation and crosslinking in the longitudinal septa (LOX, LOXL)
- proteoglycan content and fixed charge density, which sets swelling pressure
- MMP/aggrecanase remodelling of the septa specifically
- anything that changes tissue hydration or osmotic pressure

None of these is in the atlas's L12 layer, and all of them are systemic-toxicity-prone.
But the target is now a **material property**, which is a different and more measurable
thing than a signalling node.

## Ask

| want | why | status |
|---|---|---|
| **PMID 10412420** — Cohen, Lai & Mow 1998 | the source of the 10× figure. I have it only through a review. | not obtained |
| **PMID 19185303** — Sergerie 2009 | already queued for Table 2 (absolute moduli per zone); now also the corroboration of the anisotropy | not obtained |
| **PMID 8132746** — Hunziker 1994 full text | PMC deposit is abstract-only. The tables carry cell height and volume per treatment group — the only drug × shape numbers that exist | not obtained |
| **PMID 17532281** — Stokes 2007 full text | PMC deposit is abstract-only. Per-species cell height tables | not obtained |
| ~~PMID 3543020~~ Hunziker 1987 | **dropped.** Stokes 2007 replicates the ranking independently, so the 1987 method paper is no longer load-bearing | unobtainable |

---

# ROUND 8 — all four primaries obtained; the mechanism holds and the drug data cuts a new way

## 1. Cohen 1998 — the anisotropy, from the source

| bovine distal ulnar growth plate | value |
|---|---|
| **E₃, axial, in compression** | **0.47 ± 0.11 MPa** |
| **E₁, transverse, in tension** | **4.55 ± 1.21 MPa** |
| ratio | **9.7×** |
| ν₂₁ / ν₃₁ | 0.30 ± 0.20 / **0** |
| permeability, axial vs radial | 3.4 ± 1.6 vs 5.0 ± 1.8 ×10⁻¹⁵ m⁴/N·s |

n = 20 paired. Chondroepiphysis gives 1.07 and 10.63 MPa — **the same 9.9× ratio**, so
the anisotropy is a property of the cartilage, not of the plate specifically.

**The loading modes differ and that must not be glossed.** E₁ is *tensile*, E₃ is
*compressive*; this is not one property measured in two directions. But those are exactly
the modes a swelling cell imposes: expanding radially loads the surrounding matrix in
**circumferential tension**, expanding axially loads the matrix above and below in
**compression**. So the comparison is the right one, and the reading survives: **a cell
meets roughly ten times more resistance going sideways than going up.**

Permeability is similar in both directions, so **the anisotropy is in the solid matrix,
not in fluid transport.**

## 2. Hunziker 1994 — the only drug × cell-shape data that exists, and it cuts a new way

Hypophysectomised rat, 8-day infusion. Figure 1 legend, in full:

| terminal hypertrophic cell | NaCl | IGF-I | GH | normal |
|---|---:|---:|---:|---:|
| height (µm) | **19.5** | 27.3 | 26.5 | **29.8** |
| volume (µm³) | **6,370** | 9,890 | 11,140 | **10,246** |
| *implied aspect ratio* | *0.96* | *1.27* | *1.15* | *1.42* |

*(aspect ratio derived here assuming a right circular cylinder — the paper reports height
and volume and never diameter. It is not a measurement.)*

**Read that bottom row.** GH drives volume **above** normal (11,140 vs 10,246) while
reaching an aspect ratio of only 1.15 against a normal 1.42. IGF-I does better on shape
(1.27) with less volume. **Hormones restore size more completely than shape**, which
matches the authors' own finding that cell productivity did not reach normal with either
agent.

If that holds, it says something specific and useful: **the existing pharmacology is
loading the axis that does not carry physiological growth change.** GH inflates the cell;
physiological acceleration elongates it. Those are different operations, and the drug does
the one Hunziker 1989 showed does not track growth rate.

**This is a derived quantity resting on a geometric assumption.** It is the single most
consequential inference in this document and the least secure. Measuring the terminal cell
diameter in hormone-treated animals would settle it, and it is a measurement on archived
material.

## 3. Stokes 2007 uses the same identity everyone uses

`Growth = N × h_max` — new chondrocytes per day times maximum chondrocytic height. The
same structure as Kember 1976, Thurston 1985, and this atlas's flow model. Every published
account of longitudinal growth is that product, and **none of them carries a term for cell
shape**, which is why the variable stayed invisible until Hunziker measured height and
diameter separately.

## 4. Where this leaves the whole exercise

| | |
|---|---|
| the mechanism | **plausible and measured**: 9.7× anisotropic matrix, softer pericellular shell, cell goes up rather than out |
| the physiological result | **replicated in ranking** (Stokes 2007, 3 species), **not in the height/volume dissociation** (only Hunziker measured both) |
| the drug data | GH and IGF-I raise volume to or above normal but under-restore aspect ratio — **derived, needs a diameter measurement** |
| the candidate list | 2 of 7 standing, both grade C |
| the target class | a **material property** — the axial/transverse stiffness ratio — not a receptor |

**The most valuable thing to come out of this is not a compound.** It is that the field's
governing identity has no shape term, one 1989 paper says shape is what moves, the
mechanism for it was measured in 1998 and never connected, and the only drug data
available suggests the approved agents push the other axis.

The next measurement is small, specific, and uses tissue that already exists: **terminal
cell height AND diameter, in the same sections, in hormone-treated versus control
animals.** That single number decides whether the reframing is real.

---

# ROUND 9 — I went looking, and found the paper that undercuts my own reframing

Asked to look for what I needed, I searched for anyone who had measured terminal cell
height *and* diameter together. The best-powered such measurement exists, it is open
access, I fetched it myself, and **it contains a direct head-to-head test of the claim
this document has been building for five rounds — which the claim loses.**

## `rubin2021` (Nat Commun, PMC8433335)

3D MAPs: PACT-deCAL clearing, light-sheet imaging, segmentation, **hundreds of thousands
of chondrocytes** across mouse proximal tibia, distal tibia and distal ulna.

> *"these results … show that **hypertrophic cell volume is a better predictor of
> longitudinal bone growth than hypertrophic cell height**"* — with cell diameter
> correlated to only some of the differences.

Two further findings that matter as much:

- **65 % of total chondrocyte volume increase occurs *before* the hypertrophic zone**
  (volume rises 20 % RZ→PZ, 74 % PZ→PHZ, 50 % PHZ→HZ; ~9-fold overall). That is against
  the standing paradigm, and it is the paradigm embedded in this atlas's `h_term` term
  and in every drug programme aimed at hypertrophic enlargement.
- **Resting and hypertrophic chondrocytes have the same aspect ratio.** Cells go round →
  flat → round; shape changes only across the first three zones and returns. The authors
  suggest the allometric route exists *"to prevent expansion of the bone circumference
  during elongation"* — which is the anisotropic-constraint argument, stated from the
  cell's side instead of the matrix's.

## Is it actually a contradiction? Probably not — and the resolution is the axis

| study | comparison | result |
|---|---|---|
| `rubin2021`, `breur1991` | **between plates** (spatial) | **volume** predicts |
| `hunziker1989` | **one plate, two ages** (temporal) | height ↑23 %, **volume ↓13 %**, growth ↑20 % |
| `stokes2007` | mechanical modulation | height beats proliferation; **volume not measured** |

This is the same distinction I drew in round 4 against `breur1991` — and `rubin2021` is a
far stronger version of the between-plate result. **Volume may predict between plates
while height carries change within a plate over time.** The datasets do not overlap and
neither refutes the other.

But the honest weighting is not close: **one unreplicated n = 6 study from 1989, in 2D,
against a 10⁵-cell 3D dataset pointing the other way.** `terminal_cell_shape_modulation`
is downgraded **C → D** and the disagreement is recorded as contradiction **C-L1-08**.

## The experiment that settles it, and it needs no new method

**Apply `rubin2021`'s own pipeline to `hunziker1989`'s design** — one growth plate, two
ages spanning a growth-rate change, 3D morphometry of height, diameter and volume in the
same cells. Nobody has run the within-plate temporal comparison with a modern method. The
pipeline exists, is published, and would answer it unchanged.

## Standing after nine rounds

| | |
|---|---|
| compounds | **2 of 7**, both grade C, neither with a human stature association |
| the shape reframing | **downgraded to D** — contradicted by the best-powered measurement, rescued only by an axis-of-comparison argument |
| the mechanism | intact and measured — 9.7× matrix anisotropy (`cohen1998`), soft pericellular shell (`prein2016`) — but it explains *how* a cell could be shaped, and `rubin2021` says shape is not what predicts growth |
| what the drugs do | GH/IGF-I raise volume to or above normal (`hunziker1994`) — which, if `rubin2021` is right, is the **correct** axis after all |

That last line is worth stating plainly, because it reverses round 8's conclusion.
I wrote there that the existing pharmacology "is loading the axis that does not carry
physiological growth change." On `rubin2021`'s evidence, volume *is* the axis that
predicts growth, and GH is loading it correctly. **Round 8's most quotable sentence is
the one most likely to be wrong.**

## What I still want

| | why |
|---|---|
| **PMID 21559968** — Wosu 2012, *"Mechanical properties of the porcine growth plate vary with developmental stage"* | the one paper that appears to ask whether the anisotropy changes with age — the exact gap in `g_l1arch_016` |
| **PMID 29573446** — Bylski-Austrow 2018, scoliosis growth-plate histomorphometry | reports hypertrophic cell height **and** width, in **human** tissue |
| **PMID 3761364** — Cruz-Orive & Hunziker 1986, *"Stereology for anisotropic cells"* | the method under every Hunziker number; would show whether the 1989 height/diameter estimates are as robust as the volume ones |
| **PMID 3944163** — Buckwalter 1986, *"Morphometric analysis of chondrocyte hypertrophy"* | an independent morphometry of the same question, pre-dating both camps |

---

# ROUND 10 — two of the three land, and both cut FOR the mechanism

`cruzorive1986` obtained (the anisotropic-cell stereology method under every Hunziker
number). `buckwalter1986` not found. The other two are the important ones.

## 1. `wosu2012` — the anisotropy DOES change, and by ten-fold

I wrote in round 7 that nobody had measured whether the axial/transverse ratio changes
with growth rate or age. **It was measured, in the same tissue and with `cohen1998`'s own
model.** Porcine distal ulna, four developmental stages, E1/E3 derived here from the
paper's Table 2:

| stage | n | plate thickness | E₃ axial | E₁ transverse | **E₁/E₃** |
|---|---:|---:|---:|---:|---:|
| **newborn** | 24 | 3508 µm | 0.52 | 5.72 | **11.0** |
| 4 wk (group A) | 11 | 2523 µm | 0.95 | 9.74 | **10.3** |
| 4 wk (group B) | 15 | 2299 µm | 0.57 | 0.41 | **0.72** |
| 8 wk | 28 | 2007 µm | 0.49 | 0.39 | **0.80** |
| **18 wk** | 14 | 1800 µm | 0.34 | 0.39 | **1.15** |

**The tissue goes from strongly transversely stiff to essentially isotropic** across
exactly the period in which porcine growth rate falls. The newborn value of 11.0
independently reproduces `cohen1998`'s 9.7 in newborn bovine.

That is the prediction the anisotropic-constraint account makes: the constraint that
channels expansion axially is strongest when growth is fastest and disappears as growth
slows.

**Three things keep this honest.** It is a correlation across ages, not an intervention —
plate thickness halves over the same period and everything falls with age. The 4-week
animals split into two subgroups whose E₁ differs **24-fold at the same nominal age**, so
"developmental stage" is not cleanly defined there. And the ratio is derived here; the
paper reports the moduli separately and never computes it.

## 2. `bylskiaustrow2018` — the first human height AND width, and width does not move

Human **vertebral** physis, 13 severe-scoliosis patients (convex-side apex, mean curve
67 ± 23°) vs 5 age-matched autopsy controls:

| | scoliosis | control | p |
|---|---:|---:|---|
| hypertrophic zone height | 152 ± 34 µm | 180 ± 42 µm | 0.21 (ns) |
| **cell height** | **8.5 ± 1.1 µm** | **12.8 ± 1.2 µm** | **< 0.0005** |
| **cell width** | **14.9 ± 1.5 µm** | **15.0 ± 2.5 µm** | **ns** |
| *implied aspect ratio* | *0.57* | *0.85* | — |

**Height differs by 34 %. Width differs by 0.7 %.** This is the first time anyone has
measured both in human tissue, and the answer is that **width is the invariant and height
is the variable.**

Caveats: vertebral not long-bone physis; the scoliosis group is heterogeneous by
aetiology; controls are n = 5 autopsy; and **no growth rate was measured in either group**,
so this shows height varying where width does not — it does not show height tracking
growth.

## 3. What this does to the Rubin contradiction

If **width is fixed**, then within a plate volume ∝ height, and volume and height are the
*same variable* — they cannot be distinguished as predictors. `rubin2021` found volume the
better predictor by comparing **different plates**, where width is free to differ.

So the reconciliation sharpens: **within a plate, height and volume are one quantity;
between plates, they separate and volume wins.** That is consistent with every dataset
here, and it means the Hunziker/Rubin disagreement is not about biology but about which
contrast was run.

It does not rescue everything. `hunziker1989` reports width *falling* 14 %, so width is
not always invariant — different species, different bone, different perturbation. The
clean statement is narrower: **nobody has shown height and volume dissociating in the same
plate with a modern method**, and until they do, `terminal_cell_shape_modulation` stays at
**D**.

## 4. Standing after ten rounds

| | |
|---|---|
| anisotropic constraint exists | **measured twice** — 9.7× bovine (`cohen1998`), 11.0× porcine newborn (`wosu2012`) |
| it varies with developmental stage | **yes, ~10-fold collapse**, tracking growth rate (`wosu2012`) |
| human cell width vs height | **width invariant, height varies 34 %** (`bylskiaustrow2018`) |
| height vs volume as the causal variable | **unresolved** — C-L1-08, needs one within-plate 3D experiment |
| compounds | 2 of 7 standing, both grade C |

The mechanism is now better evidenced than the phenomenon it was invoked to explain.
Three independent measurements say the growth plate is a strongly anisotropic constraint
that relaxes as growth slows, and one human dataset says cell width is fixed while height
moves. What is still missing is the single experiment that would tie them to growth rate
directly.

---

# Round 11 — the anchor was never a measurement

The fourth paper of round 10 was `cruzorive1986`, *Stereology for anisotropic cells:
application to growth cartilage*. I asked for it three rounds earlier with a stated
purpose: *"the method under every Hunziker number; would show whether the 1989
height/diameter estimates are as robust as the volume ones."*

They are not. The answer inverts the last four rounds of this document.

## 1. `hunziker1989` did not measure cell height

Its own Methods say so. Vertical cell height *"cannot be determined by direct measurement
on histological sections"*; no unbiased model-free procedure exists; *"the methods applied
are necessarily assumption-dependent."* The number comes from `cruzorive1986` eq. 8.11, a
**super-egg of revolution** at fixed exponent n = 2.9:

```
X(0°)  =  5 · v̄ / ( π · E{X²(90°)} )
```

**Cell volume divided by a cell-width second moment.** I reproduced the method paper's own
worked example — 5 × 10 760 µm³ / (π × 484.9 µm²) = 35.32 µm against its printed 35.3 µm.

So the two headline numbers this document has been treating as an *observed dissociation* —
height +23 %, volume −13 % — are not independent observations of the same cells. One is
computed from the other.

What `hunziker1989` **did** measure, with estimators the method paper calls unbiased
irrespective of cell size, shape, orientation, section thickness and resolution: cell
**volume**, **surface area**, **numerical density**.

| | estimator | status |
|---|---|---|
| volume −13 % while growth +20 % | disector + point counting | **stands** |
| matrix per cell unchanged | unbiased | **stands** |
| surface area −13 % | vertical sections + cycloids | **stands** |
| height +23 % | super-egg model | **model output** |
| diameter −14 % | N_A(90°)/N_V | **model-dependent, biased high in this zone** |

## 2. Three ways the height claim is softer than it looked

**Tilt bias runs in opposite directions for the two parameters.** §10.5: no unbiased
estimator of either diameter exists, and the direct estimator *"will tend to underestimate
X(90°) for proliferative cells and to overestimate X(90°) for hypertrophic cells, and the
opposite will be the case for X(0°)."* The magnitude is set by the cell-tilt distribution —
never measured, not held constant across the two ages. **A change in tilt alone produces
height↑ / width↓**, which is exactly the reported signature.

**The fixed exponent errs toward the conclusion.** P(n) = (π/4)Γ(1+1/n)Γ(1+2/n)/Γ(1+3/n)
= 0.524 at n = 2 (spheroid), 0.626 at n = 2.9 (used), 0.785 at n = ∞ (cylinder). Height =
v/(P·E{X²}), so holding n fixed while the cell genuinely becomes more cylindrical
**overstates** the height rise.

**The elongation budget is not independent corroboration.** Reconstructed from Tables 1–3:

```
rate = (PZ height / proliferative cell height) × (24 / T_c) × terminal cell height
```

| age | predicted | measured | closure |
|---|---|---|---|
| 21 d | 258 | 276 | 93.5 % |
| 35 d | 305 | 330 | 92.4 % |
| 80 d | 77 | 85 | 90.5 % |

Good coherence — but *proliferative cells per column* is itself PZ height ÷ the
model-estimated **proliferative** cell height (226/8.1 = 27.9 vs 27 printed; 171/9.6 = 17.8
vs 18; 78/8.2 = 9.5 vs 9). The height estimator sits on both sides and enters only as the
**ratio** h_term/h_prolif, where a common multiplicative bias cancels exactly. That ratio
rises **4.1 %** (3.85 → 4.01), not 23 %. Factorised that way, +19.6 % growth =
0.638 × 1.500 × 1.234 — mostly a 50 % rise in cycles/day against a 36 % fall in
proliferative cells per column. Same arithmetic, different attribution.

## 3. An inconsistency in Table 2

E{X²} must be ≥ (mean)² for any distribution. Back-solving E{X²(90°)} = 5v/(π·X(0°)) from
the printed triples:

| age | implied E{X²} | (printed diameter)² | ratio |
|---|---|---|---|
| 21 d | 1018.9 | 894.0 | 1.140 ✓ |
| 35 d | 719.3 | 655.4 | 1.098 ✓ |
| 80 d | 662.5 | 835.2 | **0.793 ✗** |

At 80 days the printed diameter exceeds what the other two columns permit, by 12 % — the
direction and roughly the size of the bias §10.5 attributes to that estimator in
hypertrophic cells.

## 4. What this does to the compound programme

Rounds 5–10 were built on a reframe: *stop targeting hypertrophic enlargement, target the
aspect ratio, because Hunziker measured shape and not size as the carrier.* The
observational basis for that reframe is now one grade weaker than it was, and the honest
statement of C-L1-08 changes from *two measurements on different axes* to:

> **Neither height nor volume is established as the carrier of a within-plate temporal
> change in growth rate.** `rubin2021` measured all three dimensions directly in 3D but
> only between plates. `hunziker1989` ran the within-plate contrast but derived height and
> width from volume and width-moments through a shape model with no unbiased version. Its
> most reliable number — volume falling 13 % while growth rises 20 % — still contradicts
> `breur1991` and `rubin2021` head-on.

The anisotropy work of rounds 7–10 is **untouched**: `cohen1998`, `wosu2012` and
`bylskiaustrow2018` are direct mechanical and morphometric measurements, not stereological
model outputs. What they explain is now less certain than they are.

The compound implication is unchanged in list but changed in confidence: an agent that
raises terminal cell aspect ratio at constant volume remains the only untried class here,
and it is now aimed at a phenomenon whose existence rests on a model rather than a ruler.
The decisive experiment did not change design — `rubin2021`'s MAPs pipeline on
`hunziker1989`'s two-age design — but its motive got stronger. It would be **the first
model-free measurement of terminal chondrocyte height in any species.**

## 5. Standing after eleven rounds

| | |
|---|---|
| anisotropic constraint exists and varies ~10-fold | **measured** (`cohen1998`, `wosu2012`) |
| human cell width invariant while height varies 34 % | **measured** (`bylskiaustrow2018`) |
| terminal cell height at two growth rates | **never measured model-free, in any species** |
| height vs volume as carrier | **neither established** — C-L1-08 rewritten, CORR-009 |
| compounds | 2 of 7 standing, both grade C |

Three rounds of this document leaned on `hunziker1989` before anyone read the forty-page
methods paper it cites in its second sentence. That is the same failure as CORR-006 and
CORR-008: **a number's grade is a property of how it was obtained, and that is usually
documented somewhere other than the paper you are citing.**

---

# Round 12 — round 11 over-corrected, and the paper on the other side is weaker too

Round 11 ended by asserting that terminal cell height has never been measured without a
shape model in any species. The obvious next move was to check that claim rather than
publish it. Checking it took twenty minutes and it is **wrong**.

## 1. `stokes2007` measured it directly, at scale, and the atlas already had the PDF

*"Growth and final chondrocytic height h_max were measured directly."* The method: cell
profiles segmented automatically in 1.5 µm sections with the microscope stage rotated to
align the growth axis; form-factor filter > 0.3; manual removal of non-viable, partially
sectioned and coalesced cells; measured profile height regressed against depth by a logistic
fit; h_max read at the chondro-osseous junction. **No spheroid, no super-egg, no ellipsoid.**

| | |
|---|---|
| animals | 41 rats, 39 rabbits, 18 calves |
| paired comparisons for h_max | **146** |
| control | **within the same animal** |
| growth rate | measured **in the same specimen**, calcein / xylenol orange |
| result | h_max **r = 0.56, β = 1.39** vs 0.38 / 0.72 for proliferative cell number |

That is a stronger dataset on "does terminal cell height track growth rate" than anything
else in this dispute — different laboratory, different perturbation, three species. It
cannot adjudicate height vs volume, because only height was measured.

## 2. `rubin2021` is not the 10⁵-cell measurement the atlas recorded

The cell count is real; it is not the power of the predictor comparison.

1. **n = 3** — the correlation runs across three growth plate *types*, PT / DT / DU.
2. **Growth was not measured in these animals** — taken from previously published data,
   E16.5 → P40, correlated against morphology at **E16.5**.
3. **Three pairwise t-tests** on the largest 10 % of HZ volumes: DT–PT p = 0.0279, DT–DU
   p = 0.0045, **PT–DU p = 0.4834 (ns)**.
4. **The comparative sentence names a different variable from the conclusion** — volume
   correlated with all differences *"whereas cell **diameter** was correlated only with some
   of these differences"*; the conclusion is about cell **height**.

## 3. The asymmetry that matters, and it runs the same way in both papers

| | volume | height |
|---|---|---|
| `hunziker1989` | disector + point counting, unbiased | **super-egg model output** |
| `rubin2021` | direct mesh volume, divergence theorem | **bounding box on a fitted ellipsoid** |

In **both** of the only two studies that put these variables head to head, volume is the
better-estimated one. *"Volume is the better predictor"* is exactly what an
estimator-quality difference produces. Round 11's framing — model-derived height should not
outrank a direct measurement — applied the audit to one side only.

## 4. Corrected standing of C-L1-08

- **Height tracks growth rate** — well supported. `stokes2007`, model-free, 146 paired
  comparisons, three species, growth measured in the same specimen.
- **Volume beats height** — rests on n = 3 plates, an embryonic snapshot against literature
  growth, and a sentence about diameter.
- **Unexplained by anyone** — `hunziker1989`'s *best*-estimated number: terminal cell volume
  falling 13 % while growth rises 20 % within one plate over age.

**The gap is not the axis of comparison and not the age of the 1989 paper. It is that height
and volume have never been measured against each other by estimators of equal quality.**
`rubin2021`'s MAPs pipeline on `hunziker1989`'s two-age within-plate design would close it.

## 5. What this does to the compound programme

It puts the aspect-ratio reframe back roughly where rounds 7–10 had it, on better footing
than round 11 left it. An agent that raises terminal cell height at constant volume is still
the untried class, and the phenomenon it targets now has a 146-plate model-free measurement
behind it rather than one 1989 stereology paper.

`terminal_cell_shape_modulation` stays at **D** through all of this. Nothing here is a human
measurement, nothing is a manipulation, and the one quantity that would decide it has not
been measured.

## 6. Two corrections in one day, in opposite directions

CORR-009 said: read the method paper behind the number you are citing. CORR-010 exists
because CORR-009 did that for one side of a dispute and not the other, and declared a
question unanswered without checking a paper it had read the same morning. **A correction is
a claim like any other and inherits the obligation it was written to enforce.**

---

# Round 13 — the supplement confirms their result and hands over the reason it happened

`rubin2021`'s Supplementary Information arrived. It does two things at once: it **confirms**
the paper's conclusion against round 12's objection, and it **explains** the result in a way
that reopens the question on already-published data.

## 1. Their conclusion holds. Round 12's objection was cosmetic.

Scored against the growth ranking (PT and DU more active than DT):

| comparison | growth | volume (Fig. 2C) | bounding-box height (Supp. Fig. 4A, HZ) |
|---|---|---|---|
| PT vs DT | PT > DT | p = 0.0279 ✓ | **ns in the HZ** ✗ |
| DU vs DT | DU > DT | p = 0.0045 ✓ | p = 2.0e-03 ✓ |
| PT vs DU | ≈ equal | p = 0.4834 ns ✓ | **p = 2.0e-03, DU > PT** ✗ |

**Volume 3/3. Height 1/3.** Peak HZ bounding-box heights ≈ 23 (PT), 22 (DT), 26 µm (DU).
Round 12 noted the paper's comparative sentence says *diameter* where its conclusion says
*height*. True, and irrelevant — the substance holds. Withdrawn.

## 2. And the caption explains why

Supplementary Fig. 4A, in the authors' own words: the height of the cell bounding box
**"is influenced by cell orientation"** — beside an illustration of three cells yielding the
same h: a wide flat ellipse, a tall narrow ellipse, and a **tilted** elongated one.

```
axial extent  =  intrinsic long-axis length  ×  alignment with the P-D axis
```

Volume is orientation-free by construction. Axial extent is not. `cruzorive1986` §10.5 names
the identical confound for `hunziker1989`'s 2D estimators, in 1986.

> **In both of the only two studies that put these variables head to head, volume is measured
> without the orientation confound and height with it.**

That is a mechanistic reason for "volume beats height" that owes nothing to biology. It does
not rescue the height hypothesis. It says the comparison as run cannot separate *the cells got
longer* from *the cells straightened up* — and those two have different targets. Cell-volume
regulation and pericellular compliance for the first; column alignment — integrin β1,
cytoskeletal tension, chondrocyte rotation — for the second.

## 3. The data to separate them is already published

Supplementary Table 1 lists, per cell: **PC1/PC2/PC3 coefficient** *and* **PC1/PC2/PC3
orientation**. Supp. Figs 2–3 quantify per-feature segmentation error including the PC
coefficients. Supp. Fig. 5 shows PC1 orientation reproduces across two orthogonal imaging
angles. Code on Zenodo, sample data on Figshare, full tables from the corresponding author.

They had an orientation-free axis length for every cell and used bounding-box height for the
predictor comparison instead.

**So the decisive test is a re-analysis, not an experiment.** For each hypertrophic cell:
take PC1 coefficient and the angle between PC1 orientation and the P-D axis; compute mean
intrinsic length, mean alignment, and their product per plate; correlate each against the
same three growth values.

- If **intrinsic length scores 3/3** and alignment differs between DU and PT → cell
  elongation does track growth, the published metric was defeated by rotation, and the target
  class moves to **column alignment**.
- If **intrinsic length still scores 1/3** → terminal cell elongation genuinely does not
  predict growth between plates and volume stands unqualified.

Either result closes the height half of C-L1-08. Opened as `g_l1arch_017` — **tractability 1,
the only one in this dispute.**

## 4. Standing after thirteen rounds

| | |
|---|---|
| volume predicts growth between plates | **3/3, verified from the source figures** |
| axial extent predicts growth between plates | **1/3, verified** |
| but axial extent is orientation-confounded | **stated by the authors** |
| the same confound in `hunziker1989` | **stated by `cruzorive1986` §10.5, 1986** |
| intrinsic length vs alignment, decomposed | **never reported by anyone** |
| the data to do it | **already collected** |
| `terminal_cell_shape_modulation` | still **D** |

Three rounds of correction in one day, and the net movement is not toward height or toward
volume. It is that the field has been comparing an orientation-free variable against an
orientation-confounded one and reading the difference as biology.

---

# Round 14 — I ran the re-analysis, and it refuted my own hypothesis

Round 13 said the decisive test was a re-analysis, not an experiment, and guessed the raw
data was out of reach. It wasn't. `rubin2021`'s Figshare deposit
(`10.6084/m9.figshare.14903052.v1`), labelled "sample data to test the codes", is **1.37 GB
of per-cell feature tables** — `PC_range`, `PCA_coeff`, `ellipsoid_radii`,
`ellipsoid_evecs`, `volume`, `surface_area`, `sphericity`, `centroids` — for one growth
plate: distal ulna `DU_S84_m3_wt`, 21 tiles, **29,162 segmented cells**.

Two traps in it, both silent: the tiles mix MATLAB v5 and v7.3 in the same directory (15
open only with `scipy`, 6 only with `h5py` — reading with either alone drops two thirds of
the sample), and cell centroids are **local to each 900×900 px tile**, so without the
`Tile_coordinates.xlsx` offsets all 21 stacks pile up on each other.

## The validation guard

Before reporting anything, `atlas/tools/rubin_decompose.py` reconstructs their **own
published** profile for this sample (Supp Fig 4A) and refuses to continue if it misses:

| | reconstructed | published trace |
|---|---|---|
| mean bounding-box height, first half of axis | **10.13 µm** | ~9–10 |
| hypertrophic peak | **27.55 µm** | ~26 |

Passed. The registration and P-D axis convention are right.

## Result 1 — the confound does not bite. My hypothesis was wrong.

Round 13 proposed that "volume beats height" might be an artefact of the orientation
confound the authors flag. Within this plate it is not.

Mean alignment `|cos(PC1, P-D)|` moves only **0.322 → 0.384** from resting to hypertrophic
zone — and both are far below the **0.500** expected for uniformly random axes in 3D.
Chondrocyte long axes stay preferentially **in the plane of the plate**, even in the
hypertrophic zone. Across bins 0–34 the profile is flat at 0.31–0.39; the apparent doubling
in my first pass came entirely from a 24-cell terminal bin.

Counterfactual swap — hypertrophic cell **shapes** wearing resting-zone **orientations**,
and the reverse (1,841 RZ vs 456 HZ cells):

| | axial extent | fold |
|---|---|---|
| resting zone, observed | 9.67 µm | — |
| HZ shapes, RZ orientations | 18.68 µm | **×1.93** ← elongation alone |
| RZ shapes, HZ orientations | 10.71 µm | **×1.11** ← realignment alone |
| hypertrophic zone, observed | 19.10 µm | ×1.98 |

**Elongation 96.7 % of the log rise, realignment 15.0 %, interaction −11.7 %.**

## Result 2 — and this one is bigger: the enlargement is near-isotropic

| | fold, RZ → HZ peak |
|---|---|
| principal axis 1 (long) | **×2.171** (15.86 → 34.44 µm) |
| principal axis 2 | **×2.273** (10.47 → 23.79 µm) |
| principal axis 3 (short) | **×2.378** (7.49 → 17.82 µm) |
| **cube root of the volume fold** | **×2.124** |

All four within 12 %, and the **short** axis grows marginally fastest.

> **If enlargement is isotropic, then within a plate height ≈ volume<sup>1/3</sup> × a
> constant. Height and volume are not independent variables, so they cannot be independent
> predictors — and "volume is the better predictor" reduces to "volume is the better-measured
> view of one variable."**

That is a mechanistic account of the recurring result that needs **no** orientation confound.
It is a cleaner answer than the one I was hunting for, and it arrived by the hypothesis
failing.

## What it does not do

One plate. No proximal tibia, no distal tibia — so the **DU-vs-PT** difference that carries
`rubin2021`'s headline is still untestable. And RZ→HZ is a **differentiation** axis;
`hunziker1989`'s is one zone at two growth rates. His claim is precisely that the change
there is **anisotropic** (height +23 % with volume −13 %). No such anisotropy exists along
the axis this dataset can see — which is not a refutation, because it is not the same axis.

Graded **D**: my own re-analysis, one sample, unreplicated. Same standard as anyone else's.

## Standing after fourteen rounds

| | |
|---|---|
| orientation confound in the height metric | **real, and immaterial within a plate** — measured |
| RZ→HZ enlargement | **near-isotropic**, 4 independent estimates within 12 % |
| height vs volume as independent predictors | **they may not be independent at all** |
| the between-plate comparison | **still open** — needs PT and DT feature tables |
| `hunziker1989`'s anisotropic claim | **untested along its own axis in any species** |
| `terminal_cell_shape_modulation` | still **D** |

Four rounds, four corrections, and the last one cost me my own hypothesis. The net position
is better than any of the framings that preceded it: the field's two candidate variables may
be one variable seen two ways, and the only place they could genuinely separate is the axis
nobody has measured with a modern method.

---

# Round 15 — the data-availability audit, and what is actually reachable

Round 14 needed the proximal-tibia and distal-tibia feature tables. Every public route was
checked. None has them.

| source | contents | verdict |
|---|---|---|
| figshare `10.6084/m9.figshare.14903052.v1` | distal ulna, 21 tiles, 29,162 cells, full per-cell features | **used in round 14** |
| figshare `10.6084/m9.figshare.14932503.v1` | preprocessing inputs for DU tiles 19–20 | same sample |
| Nat Commun **Source Data**, 371 MB | S1–S7: XPIWIT binaries, demo `.vff`/`.tif`, ImageJ macros. S8: a two-way ANOVA of SMAD-positive counts | **no figure data** |
| Zenodo ×8 (Agrawal 2024, eLife 95289) | ~250 GB raw Imaris `Col2creER;Confetti` stacks, PT + distal femur, **E18.5 and P40** | raw images, other label scheme |

Two things worth stating plainly.

**The Source Data archive does not contain source data.** For a paper whose central claim is
a morphometric comparison, "source data are provided with this paper" resolves to the
segmentation software and demo images. None of the values behind Fig. 2 or Supplementary
Fig. 4A are in it. Reaching it at all took a detour: the PMC download link returns a
JavaScript interstitial, and the file only came down through Europe PMC's
`supplementaryFiles` endpoint.

**The most interesting object found was in the follow-up paper.** The eLife 2024 Zenodo
deposits are proximal tibia and distal femur at **E18.5 and P40** — one plate, two ages,
spanning a large change in growth rate. That is `hunziker1989`'s own design. If 3D MAPs
cell-morphology output exists for those samples, it would be **the first modern 3D test of
the shape-modulation claim** — a better prize than the PT-vs-DT comparison that started this.
The deposits themselves are raw Confetti clonal stacks under a different labelling scheme, so
they cannot be used without rerunning the pipeline.

Both were requested from the corresponding authors on 2026-08-06. `g_l1arch_017` moves from
tractability **1 to 2**: the analysis is written and validated, but the input now depends on
someone answering an email.

## Standing after fifteen rounds

| | |
|---|---|
| within-plate orientation confound | **measured, immaterial** (round 14) |
| within-plate enlargement | **near-isotropic** (round 14) |
| between-plate comparison | blocked on data that exists but is not public |
| `hunziker1989`'s own axis, in 3D | **possibly already imaged**, in the 2024 deposits |
| `terminal_cell_shape_modulation` | still **D** |

---

# Round 16 — the per-cell test corrects me again, and finds the better question

Round 14 rested on forty binned means. Forty means can look isometric while the cells inside
them are not, so I ran the test that could falsify it: per-cell regression of log axis length
on log volume, where isometry predicts a slope of exactly **1/3**.

## Corroborated — and no longer one plate

| window | PC1 | PC2 | PC3 | axial extent |
|---|---|---|---|---|
| all 29,162 cells | 0.345 | 0.373 | 0.351 | 0.311 |
| resting (n=1,841) | 0.374 | 0.356 | 0.339 | 0.280 |
| hypertrophic (n=456) | 0.341 | 0.352 | **0.421** | 0.326 |

Isometry survives per cell. And `rubin2021`'s own Fig. 3 reaches it by a different statistic
on **all three plates** — HZ growth isometric in PT (slope 0, p = 0.937), DT (0, p = 0.903),
DU (0.01, p = 0.301). That half of round 14 is replicated by the authors themselves.

## Corrected — round 14's consequence was too strong

I wrote that if enlargement is isometric, height and volume are not independent variables.
Within the HZ, **log volume explains only 43.2 % of the variance in log axial extent.** At the
level of single cells they are plainly two variables. The claim holds only for zone means —
which happens to be the level `rubin2021`'s comparison operates at, so the argument survives
where it was aimed and fails where I stated it.

## And the residual is orientation

What volume leaves unexplained in the HZ:

- correlates with **alignment at r = +0.664** — 44 % of the residual
- correlates with intrinsic length at r = +0.076 — 0.6 %

> **The orientation confound is weak between zones and dominant between cells.** Round 14 asked
> whether realignment drives the *rise in the mean* — it does not, alignment is flat. This asks
> what makes one hypertrophic cell's axial extent differ from another's — and after volume,
> almost all of it is orientation.

Which means whether the confound contaminates the between-plate comparison turns entirely on
**whether mean alignment differs between plates** — a number nobody has reported and which the
public deposit cannot give, because it holds only the distal ulna. The email is better
motivated now than when it was sent.

## The finding I did not expect

| axis | resting | hypertrophic |
|---|---|---|
| PC1 long | 0.322 | 0.384 |
| PC2 medium | 0.490 | 0.472 |
| **PC3 short** | **0.660** | **0.625** |

**The short axis is the one that points along the bone** — in both zones, against 0.500 for
random. The chondrocyte is a disc lying in the plane of the plate whose *thin* direction is
the growth direction, and longitudinal growth comes from that thin axis thickening — at slope
**0.421**, faster than isometry, as the cell enlarges.

So the quantity this entire literature calls **"hypertrophic cell height" is the extent along
the cell's shortest principal axis**, not its longest.

With one caveat that is itself a new question. This is embryonic mouse (E16.5) distal ulna.
`hunziker1989`'s postnatal rat terminal cell is **38.5 µm tall against 25.6 µm wide** — taller
than wide, which would put the *long* axis up the bone. Different species, different age, and
`rubin2021`'s terminal bins are too sparse to compare. Not a contradiction:

> **Nobody has measured whether, or where, the terminal chondrocyte turns its long axis up the
> bone.** If it does, that is the shape modulation Hunziker described, and it happens somewhere
> between an embryonic mouse ulna and a 35-day rat tibia.

## Standing after sixteen rounds

| | |
|---|---|
| isometry, per cell and across three plates | **corroborated** |
| height and volume as one variable | **true for zone means, false per cell** |
| orientation confound | **weak between zones, dominant between cells** |
| between-plate mean alignment | the pivotal number — **never reported** |
| which axis points along the bone | **the short one**, in embryonic mouse |
| does the terminal cell ever stand up? | **unmeasured in any species** |
| `terminal_cell_shape_modulation` | still **D** |
