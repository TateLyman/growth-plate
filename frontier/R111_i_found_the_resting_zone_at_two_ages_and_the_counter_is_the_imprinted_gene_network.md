# F-R111 — I found it. The resting zone at two ages. The counter is the imprinted gene network, it collapses four times harder in the pool than anywhere else, and fracture puts it back.

You told me to find it and not settle for the nearest thing. **It exists, it was in GEO the whole time,
and my search had never looked in the right place** — the phrase "resting zone" appears only in
*sample* characteristics, and every enumeration I have run searched *series* titles and summaries. So I
downloaded the sample-level metadata for all **999 growth-plate-relevant series** and grepped that
instead.

`GSE113982 — Newton AH et al., **A radical switch in clonality reveals the formation of a stem cell
niche in the epiphyseal growth plate.** Nature 2019.` Laser-microdissected mouse growth plate:

| | resting zone | proliferative | hypertrophic |
|---|---|---|---|
| **P2 / P3** (before the stem-cell niche forms) | **14** | 12 | 12 |
| **P28** (after) | **18** | 22 | 22 |

**Not just two ages — the two ages that matter**, spanning exactly the secondary-ossification-centre
transition that F-R110 showed flips the sign of systemic SAG.

**Sanity check, and it validates the dataset:** RZ identity holds at both ages (SFRP5 +0.48 → +1.47,
PTHLH +1.17 → +1.29), and **MKI67 in the RZ relative to the PZ goes from +1.32 at P2 to −1.03 at P28** —
the resting zone is *not* quiescent before the niche exists and becomes so after. That is the paper's
own headline, recovered from the data.

---

## 1. First, a correction to F-R109: the three zones do not age by the same program

| | correlation of the two zones' ageing vectors |
|---|---|
| PZ vs HZ | **r = +0.336** |
| RZ vs PZ | **r = +0.160** |
| RZ vs HZ | **r = +0.081** |

**The differentiated zones age together. The resting zone does something largely its own.**

And the consequence for my last round: **F-R109's youth axis was built entirely from PZ and HZ, and it
only weakly describes resting-zone ageing (r = +0.136).**

> **The axis I built two rounds ago, and promoted vosoritide on, is a proliferative/hypertrophic-zone
> axis. It is only marginally informative about the compartment that holds the pool.** That is exactly
> why I kept asking for this dataset, and the answer is that the caveat was warranted.

---

## 2. What actually happens in the pool: the imprinted gene network collapses

Unbiased, top of the list of what the resting zone **loses** between P2/P3 and P28 (log2):

**IGF2 −7.7 · DLK1 −6.5 · MEST −5.7 · PLAGL1 −5.7 · CDKN1C −4.1 · H19 −4.0 · MEG3 −3.6 · ZIM1 −3.4 ·
RIAN −3.2 · AIRN −3.1 · PEG3 −3.1 · MAGEL2 −2.8 · KCNQ1OT1 −2.8 · GPC3 −2.7**

**Fourteen imprinted genes in the top fifty.** That is every major imprinted domain at once — *Igf2/H19*
and *Kcnq1ot1/Cdkn1c* (chr7), *Dlk1–Dio3* (Meg3/Rian/Mirg, chr12), *Airn/Igf2r* (chr17), *Plagl1* (chr10),
*Peg3/Zim1* (chr7), *Mest* (chr6), *Magel2* (chr7), *Gpc3* (X).

### ⇒ Quantified, against an expression-level-matched null (4,000 draws)

| zone | **imprinted network** | cell cycle | background | matched null | **z** |
|---|---|---|---|---|---|
| **resting** | **−3.09** | −0.84 | −0.48 | −0.55 ± 0.22 | **−11.4** |
| proliferative | −0.71 | −0.07 | +0.12 | +0.56 ± 0.18 | −6.9 |
| hypertrophic | −0.61 | +0.09 | +0.18 | +0.41 ± 0.15 | −6.9 |

**Three things this settles.**

1. **It is four times larger in the resting zone than in either differentiated zone**, in the same
   animals, same dissection, same libraries.
2. **It is not proliferation.** The cell cycle falls −0.84 in the RZ; the imprinted network falls −3.09.
   **3.7× larger than the cell-cycle change in the same cells.**
3. **It is not a general developmental downshift** — the PZ and HZ are the control and they lose a
   fifth as much.

> **The largest thing that happens to the growth-plate stem cell compartment as it ages is the
> coordinated shutdown of the imprinted gene network.** That is the counter, measured in the right
> cells, and it took finding this one dataset.

---

## 3. The mechanism I expected, tested, and rejected

**The imprint-maintenance machinery falls in the resting zone and only there:**

| gene | RZ | PZ | HZ |
|---|---|---|---|
| **TRIM28** (KAP1) | **−1.53** | −0.19 | +0.23 |
| **DNMT1** | **−1.12** | −0.01 | +0.62 |
| **CTCF** | **−0.94** | +0.72 | −0.25 |
| **DAXX** | **−1.36** | +0.40 | +0.08 |
| MPHOSPH8 (HUSH) | −0.91 | +0.58 | −0.25 |
| ZFP57 | −0.80 | −0.50 | +0.40 |
| SETDB1 | −0.57 | −0.63 | −0.07 |

ZFP57–TRIM28–SETDB1–DNMT1 is the complex that maintains methylation at imprinting control regions. All
of it declines, RZ-specifically. **That is a clean hypothesis and I had GSE202057 in the corpus to test
it — `TRIM28 establishes skeletal stem cell identity and safeguards skeletogenesis`, Trim28 KO in
cartilage.**

| | |
|---|---|
| Trim28 in the KO | **−1.89** (the knockout worked) |
| **imprinted network in Trim28 KO, above background** | **−0.30** *(vs −1.79 in RZ ageing)* |
| **Trim28 KO vs the resting-zone ageing vector** | **r = −0.014, p = 0.2 — NULL** |

**Removing TRIM28 does not reproduce the ageing resting zone, and shifts the imprinted network only a
sixth as far.** The machinery decline is a correlate, not a demonstrated cause. **I am reporting the
hypothesis and its refutation together rather than the hypothesis alone.**

*(Trim28 KO does score +0.183 on F-R109's PZ/HZ axis — but that is the "arrest looks like immaturity"
failure mode I flagged in F-R109 §6: GREM1 +3.98, renewal up, differentiation restricted.)*

---

## 4. The human genetics, and it is the strongest in the file

**GWAS Catalog: 264 genome-wide height associations across 32 of 54 imprinted-network genes.**
Against a size/LD-matched null (3,000 draws): **264 observed vs 118 ± 44, empirical p = 0.0077.**

ZFAT 52 · **SLC38A4 34** · **PLAG1 24** · GNAS 22 · **IGF2 19** · **GRB10 18** · **DLK1 17** · GLIS3 17 ·
IGF2R 7 · MEG3 6 · MKRN3 5 · KCNQ1OT1 4.

**And the machinery is not enriched — ZFP57 1, ZNF445 1, PADI6 1.** The network is the height axis; the
machinery that maintains it is not. That is independently consistent with §3's refutation.

**The Mendelian genetics is bidirectional at two independent loci, which is the evidential structure
this file reserves for its best arms (PTCH1 at 1/2/3 copies; DNMT3A loss-tall/gain-dwarfed):**

| locus | loss of the growth-promoting side | gain |
|---|---|---|
| **11p15 (IGF2 / H19 / CDKN1C)** | **Silver–Russell — severe short stature** | **Beckwith–Wiedemann — overgrowth** |
| **14q32 (DLK1 / MEG3)** | **Temple syndrome — short stature** | **Kagami–Ogata — overgrowth** |
| GPC3 | — | **Simpson–Golabi–Behmel — overgrowth** |
| GNAS | pseudohypoparathyroidism 1A — short stature, brachydactyly | — |

**Two imprinted domains, each producing overgrowth in one direction and short stature in the other, at
extreme effect sizes.** This is a dose-responsive human growth-setpoint system, and it is the system
that collapses hardest in the pool compartment.

---

## 5. Three other things this compartment shows that nothing else could

### ⇒ (a) The pool becomes Hedgehog-**ligand**-resistant with age, but the receptor does not move

| RZ, P28 minus P2/P3 | |
|---|---|
| **HHIP** (the decoy) | **+3.86 — roughly fifteen-fold** |
| BOC | −1.93 |
| GAS1 | −1.93 |
| CDON | −1.09 |
| GPC3 (shapes the gradient) | −2.74 |
| SCUBE3 (releases/transports the ligand) | −1.38 |
| **SMO** | **−0.27 — flat** |
| PTCH1 / GLI1 | +0.04 / +0.59 |

**The decoy rises fifteen-fold, all three positive co-receptors fall, the ligand-delivery machinery
falls — and the receptor is unchanged.** F-R103 saw this shape in bulk PZ; here it is in the pool, and
it is far larger.

> **A Smoothened agonist acts downstream of the ligand, the co-receptors and HHIP. Everything that
> degrades with age on this axis is upstream of the drug target.** This is the strongest and most
> specific argument the SMO-agonist class has ever had, and it is an argument *against* every
> ligand-side, Ihh-based or delivery-based approach.

### ⇒ (b) Vosoritide's target rises in the aged pool

**NPR2 +1.05 in the resting zone** (PZ 0.00, HZ −0.02). The receptor F-R109 promoted the arm on becomes
*more* abundant in the compartment we care about as it ages. **Against that: PRKG1, its obligate
effector, falls −0.89.** Net: the arm survives, with the caveat recorded.

### ⇒ (c) A third independent reason the GH axis is weak in the pool

**IGF1 +3.15 in the resting zone** — an eight-fold rise — while **IGF1R −1.38 and GHR −1.45.**
**Ligand up, both receptors down.** F-R089 had pool-negativity, F-R110 had null-on-the-axis in human
tissue; this is receptor loss in the pool compartment itself.

---

## 6. Then I screened 5,112 contrasts for anything that raises the network

Nothing pharmacological does. **Three biological states do:**

| state | imprinted network, above background |
|---|---|
| **HEY1–NCOA2 fusion** (mesenchymal chondrosarcoma) | **+3.74** |
| **the skeletal stem cell itself**, vs its progeny (GSE142873) | **+2.65** |
| **fracture callus skeletal stem cells vs uninjured** (GSE213574) | **+2.72** |

The first is an oncogenic fusion and the second is cell identity rather than an intervention. **The
third is neither.**

**Fracture callus, sorted SSC/BCSP, adult mouse, vs uninjured bone from the same populations:**
IGF2 **+5.19** · PEG3 **+5.89** · GRB10 **+4.47** · MEST **+4.42** · CDKN1C **+4.25** · PEG10 **+3.91** ·
SLC38A4 **+3.77** · NDN **+3.60** · MEG3 **+3.43** · GPC3 **+3.05** · PLAGL1 **+2.46**.

> **+2.72 above background — the near-exact inverse of the −3.09 collapse in the ageing resting zone,
> in adult skeletal stem cells, physiologically, without a tumour.**

**So the shutdown is not irreversible.** Adult skeletal stem cells can and do switch the network back
on, and the trigger that does it is injury.

**What that is not:** a fracture callus makes bone, not length. This is the program without the
geometry — F-R099's stock-versus-flow in a new guise, and I am not going to call it an arm. **What it
is** is the first demonstration anywhere in this file that the counter can run backwards in an adult
mammal, which is the thing F-R109 §5 said nobody had ever shown.

---

## 7. Corrections

1. **F-R109's youth axis is a PZ/HZ axis** and describes resting-zone ageing only weakly (r = +0.136).
   Every conclusion I drew from it applies to the differentiated zones. Vosoritide survives, but on §5(b)
   now rather than on the axis alone.
2. **My search method was wrong for five rounds.** Series-level metadata cannot find a zone-resolved
   dataset; sample-level characteristics can. `analysis/geo_sweep/softmeta.py` + `findrz.py` now do it,
   and running them over 999 series returned **13 candidates and exactly one that had what I needed.**
3. **The TRIM28/ZFP57 imprint-maintenance hypothesis is refuted**, by a knockout that was already in the
   corpus.
4. **F-R104–F-R107's methylation arm gets its final answer here.** In the resting zone every methylation
   gene falls together — DNMT1 −1.12, DNMT3A −0.91, TET2 −2.59, TET3 −1.56, MECP2 −1.09 — writers and
   erasers alike, tracking MKI67 −1.77. **There is no writer/eraser imbalance. There never was.** What
   there is is a specific downstream *output* — the imprinted network — falling 3.7× harder than the
   machinery or the cell cycle.

## 8. Where this leaves it

| | |
|---|---|
| **the counter, identified** | the coordinated shutdown of the imprinted gene network in the growth-plate stem cell compartment: **−3.09 vs −0.71/−0.61 in the differentiated zones, z = −11.4** |
| **human-validated** | 264 GWAS height associations, p = 0.0077; bidirectional Mendelian dose-response at 11p15 and 14q32 |
| **reversible?** | **yes, in adult skeletal stem cells, by fracture (+2.72)** — the first backwards movement of the counter in the file |
| **obtainable agent** | **none.** 5,112 contrasts, nothing pharmacological |
| **what the pool data does for the stack** | SMO agonism strengthened decisively (§5a); vosoritide survives (§5b); GH weakened a third time (§5c) |

## 9. Asks

1. **Anything that reactivates imprinted gene expression in a somatic stem cell without a demethylating
   agent.** DNMT inhibitors are excluded — F-R079 established DNMT1 must be preserved (Dnmt1^ΔPrx1
   bones are less than half length). This is now the single question.
2. **What in fracture callus does it.** GSE213574 is sorted SSC/BCSP with no time course and no
   mechanism. If the injury signal that reactivates the network is identifiable, it is the first
   candidate lever on the counter that has ever existed.
3. **A human growth-plate resting zone at more than one age.** GSE113982 is mouse. The human equivalent
   does not exist in 4,421 series, and every §2–§5 number would need to be confirmed there.

---

*You were right to push. The dataset existed, my search had a structural blind spot, and the compartment
I had never measured turned out to contain a larger and cleaner signal than anything in the two zones I
had. It also cost me part of the axis I built last round, and it killed the first mechanism I proposed
for it within the same hour.*
