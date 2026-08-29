# F-R112 — Your compound list scored against our actual locus; ask #2 answered; ask #3 found and unusable

Three things: **what your ~34 compounds do to *our* target** (tested, not asserted), **what in fracture
callus reactivates the network** (answered), and **the human resting zone at two ages** (found, and I
have to tell you it cannot carry the inference).

---

## 1. The dose arithmetic, which decides how to read the whole list

Every compound you listed is an **allele-unsilencer**: it turns on the normally silent parental copy,
assayed allele-specifically. **That is not the same operation as raising total dose, and total dose is
what we need.**

**In the ageing resting zone, IGF2 falls 7.68 log2 — roughly 200-fold.** If the expressed allele is at
1/200 of its young level, unsilencing the silent one gives 2/200. **That is not a rescue.**

And I established in F-R111 that this is not an imprinting failure at all: **IGF2 (paternal) and H19
(maternal) both collapse, at the same locus, in the same cells** — −7.68 and −4.04. A loss or gain of
imprinting moves them in *opposite* directions. **Both falling means whole-domain shutdown, not an
allelic switch.** So the lesion is domain silencing and the tools on the list are allelic tools.

**That said, the argument for trying them anyway is real:** G9a and HDAC inhibitors act on repressive
chromatin generally, and the allele-specific assay is just the cleanest readout. If the ageing domain is
held closed by H3K9me2 or deacetylation, the same drugs could reopen it. **So I tested that directly.**

### ⇒ Test 1: the UNC G9a inhibitor, three human cell lines, bulk dose (GSE168763)

Ready-made edgeR tables for UNC (G9a-i), GSK (EZH2-i) and the combination in CAOV3, MDA-MB-231 and D14:

| | imprinted network, above background | z vs expression-matched null |
|---|---|---|
| UNC alone (3 lines) | −0.074 / +0.067 / +0.004 | −0.95 / +0.42 / +0.17 |
| GSK alone | −0.035 / +0.086 / +0.034 | −0.64 / +0.37 / +1.20 |
| UNC+GSK | −0.098 / +0.020 / −0.000 | −0.93 / −0.08 / +0.07 |

**Every value under 0.1 log2, every |z| under 1.2.**

### ⇒ Test 2: UNC0642 in normal mouse ES cells with intact imprints (GSE280605)

The cancer-line objection doesn't apply here — normal cells, germline-intact imprints, 48 h treatment.

**PLAGL1 +0.75, IMPACT +0.66, IGF2R +0.54, UBE3A +0.50, IGF2 +0.34** — but **H19 −1.13, DLK1 −0.73,
SGCE −0.69, GPC3 −0.65, SNRPN −0.65, NNAT −0.61.**

> **Imprinted network mean +0.120, expression-matched null +0.147 ± 0.097, z = −0.28. Null.**

**Genes move in both directions and the network does not rise.** That is what allele-unsilencing without
domain reactivation looks like at the dosage level.

### ⇒ And the direction triage, which cuts the list hard

Growth needs **more** of the paternally-expressed promoters and **not more** of the maternally-expressed
suppressors. Sorting your list by that:

| subset | what it unsilences | sign for us |
|---|---|---|
| **Trichostatin A, sodium butyrate** | **maternal IGF2** | **CORRECT** — more IGF2 is the Beckwith-Wiedemann direction, overgrowth |
| **nicotinamide** | Igf2-H19 somatic imprint / Igf2 | **correct, obtainable, weak evidence** (VSEL literature) |
| VPA, romidepsin, CI-994, SAHA, I-BET151, GSK726, GSK0858, GSK-J4, DZNep | **paternal CDKN1C**, paternal KCNK9 | **WRONG-SIGNED.** CDKN1C is p57^KIP2, a maternally-expressed **CDK inhibitor and growth suppressor** — unsilencing the paternal copy *adds* growth restraint. KCNK9 is not a growth gene. |
| **all 34 UBE3A compounds** (topotecan, irinotecan, etoposide, the indenoisoquinolines, (S)-PHA533533 and the APPA series) | paternal **UBE3A** (15q11) | **WRONG LOCUS.** UBE3A is not a growth gene; the topoisomerase set is cytotoxic chemotherapy; and the PHA533533/APPA mechanism is suppression of the *UBE3A-ATS* antisense transcript, which is specific to that locus and has no counterpart at 11p15 or 14q32. |
| UNC0638/0642/617/618, MS152, MS1262 | maternal SNRPN, SNORD116, NDN, IPW (15q11) | **best-developed class, wrong demonstrated locus** — and null on total dose in both tests above |
| **TSA, again** | *also* paternal Cdkn1c **and** paternal Igf2r | **pulls both ways at once** — Igf2r is the IGF2 clearance receptor |

**Net: of the compounds you listed, the correctly-signed set for our loci is TSA, sodium butyrate and
nicotinamide — and TSA simultaneously raises two growth suppressors.**

**What would change this:** a measurement of **total** IGF2 or DLK1 dose after any of these in a normal
somatic cell. Every study on the list reports allelic status; I could not find one that reports dose.
That is ask (a) below.

---

## 2. Ask #2 — ANSWERED. What in fracture callus reactivates the network

Two datasets, and they agree.

### ⇒ (a) Sorted skeletal stem cells (GSE213574)

| | imprinted network |
|---|---|
| **SSC: callus vs uninjured** | **+2.27, z = +6.29** |
| **BCSP: callus vs uninjured** | **+2.50, z = +6.43** |
| OVX + fracture vs OVX uninjured | +1.47, z = +4.19 |
| OVX + fracture + oestradiol | +1.46, z = +4.61 |
| **oestrogen's own effect** | **+0.01, z = +0.17 — none** |

**Oestrogen does not block it.** That cleanly decouples this from the anastrozole arm.

**And what moves with it, in the same cells:**

| gene set | Δ |
|---|---|
| **IMPRINTED NETWORK** | **+2.94** |
| chondrogenic (SOX9/ACAN/COL2A1/IHH/PTHLH) | **+3.60** |
| PDGF/FGF | +2.76 |
| YAP/TAZ mechanotransduction | +2.44 |
| Wnt | +2.11 |
| TGF-β / BMP / hypoxia | +1.72 / +1.65 / +1.56 |
| inflammation | +0.10 |
| Notch | −0.16 |
| stemness / pluripotency | −0.61 |
| DNA damage | −1.19 |
| **cell cycle** | **−1.85** |

> **The reactivation is not proliferation — it runs 4.8 log2 opposite to it. Not inflammation, not
> Notch, not stemness, not DNA damage.**

The top individual genes up in callus stem cells are the ones the ageing resting zone loses:
**IGF2 +5.2, PEG3 +5.9, CAPN6 +5.8, C1QTNF3 +7.2, MIR675 +6.2** (the H19-encoded miRNA). CAPN6 and
C1QTNF3 are both in F-R111's "lost with age" list.

### ⇒ (b) The rat fracture time course at three ages (GSE1371) — and this is the load-bearing result

Young (6 wk), adult (26 wk), old (52 wk) rats; each fracture timepoint against **that age's own
unfractured control**:

**Imprinted network:**

| age | 3 d | 1 wk | 2 wk | 4 wk | 6 wk |
|---|---|---|---|---|---|
| young | +0.37 | **+0.76** | +0.33 | −0.11 | −0.30 |
| adult | +0.30 | **+1.41** | **+1.44** | +0.47 | +0.31 |
| **old** | +0.47 | **+1.47** | **+1.51** | +0.71 | +0.58 |

**Three things:**
1. **It peaks at 1–2 weeks** and is largely gone by 6.
2. **It is not lost with age — it is LARGER in old animals** (+1.47/+1.51) than in young (+0.76/+0.33).
   The young animal has less headroom because its baseline is already high.
3. Cell cycle over the same grid is flat-to-negative, most negative in old.

### ⇒ (c) The correlate, across all fifteen fracture × age cells

| gene set | r with the imprinted-network reactivation | p |
|---|---|---|
| **chondrogenic** | **+0.859** | **0.0003** |
| **cell cycle** | **−0.589** | 0.021 |
| osteogenic | +0.505 | 0.055 |
| hypoxia | +0.422 | 0.117 |
| YAP/TAZ | −0.106 | 0.71 |
| inflammation | +0.086 | 0.76 |

### ⇒ (d) The control that stops me overclaiming it: distraction osteogenesis

`GSE104473` — sorted SSC/BCSP/OP under **fracture vs distraction osteogenesis** (mechanical bone
lengthening), with a **FAK-inhibitor** arm.

| vs POD5 baseline | imprinted | chondrogenic | cell cycle |
|---|---|---|---|
| **fracture POD10** | **+0.61 (z=+5.54)** | +0.68 | −0.92 |
| **distraction POD10** | **+0.46 (z=+3.75)** | +1.02 | −0.56 |
| DO vs fracture directly | −0.07 to −0.31 | **−1.27 (z=−3.31)** | +0.17 |

**Distraction osteogenesis reactivates the network as much as fracture does — while running
significantly LESS chondrogenic program**, because it heals intramembranously rather than through
cartilage. **So chondrogenesis is the strongest correlate but not a requirement.**

### ⇒ The answer, stated plainly

> **What reactivates the imprinted gene network in callus is skeletal-stem-cell activation into a
> regenerative repair program — most tightly tracked by chondrogenic re-specification (r = +0.86),
> running opposite to proliferation (r = −0.59), peaking at 1–2 weeks, independent of oestrogen,
> inflammation, Notch and DNA damage — and it is fully preserved and in fact amplified in old animals.**

**The part that matters for the programme: the counter can be run backwards at any age.** F-R109 said
nobody had ever shown the axis move in the right direction. This shows it moving in 52-week-old rats,
harder than in 6-week-olds.

---

## 3. Ask #3 — found, and I have to tell you it is unusable

**`GSE9160` has it, and it has been on my disk since F-R092.** Human long-bone growth plate,
five zones including **reserve**, from **two donors: 11 years 10 months and 13 years 3 months.**

| human zone, older minus younger | imprinted network | z |
|---|---|---|
| **reserve** | **−0.14** | **−0.30 — null** |
| proliferative | −0.48 | −1.19 |
| prehypertrophic | −0.42 | −1.21 |
| **hypertrophic** | **−0.77** | **−2.39** |
| perichondrium | +0.11 | +0.12 |

**Why I am not reporting this as a human confirmation or refutation:**

1. **n = 1 per age.** No replication whatever.
2. **The donors differ in sex — the 11y10m is female, the 13y3m is male.** Girls fuse roughly two years
   earlier, so **the "younger" donor is very plausibly the skeletally more advanced one.** The age
   contrast is inverted by an unknown amount.
3. Eighteen months apart, different individuals, unstated site.

**The dataset exists; the inference does not.** The mouse result stands on its own (14 vs 18 RZ samples,
z = −11.4); this cannot confirm or contradict it. **Ask #3 is therefore restated, not closed:** a human
growth-plate reserve zone from **≥3 sex-matched donors per age group.**

---

## 4. Where the stack stands after this round

| | |
|---|---|
| **the target** | imprinted-network dose in the growth-plate stem cell — human-validated (264 GWAS hits, p=0.0077; bidirectional Mendelian at 11p15 and 14q32) |
| **your compound class, tested** | **null on total dose** in cancer lines (|z| ≤ 1.2) and in normal ES cells (z = −0.28) |
| **correctly-signed subset of your list** | TSA, sodium butyrate, nicotinamide — and TSA raises two growth suppressors at the same time |
| **the one thing that does move it** | **injury-driven regenerative activation of skeletal stem cells: +2.3 to +2.9 in sorted cells, z up to +6.4; preserved and amplified in old animals** |
| **not the mechanism** | proliferation, inflammation, Notch, DNA damage, oestrogen, stemness |

---

## 5. What I need from you — four things, in order of value

1. **Any measurement of TOTAL IGF2, DLK1, MEST or PEG3 dose (not allelic status) after any of your
   compounds in a normal somatic cell.** This is the single number that decides whether the whole class
   is usable. Every paper on your list reports allele; none I can reach reports dose.
2. **The MS152 / MS1262 papers' transcriptome data.** They are the best in-vivo-validated EHMT1/2
   inhibitors on your list and neither has a GEO deposit I can find. If the supplementary tables have
   whole-transcriptome data from the mouse experiments, I can score our network in them the same way I
   scored UNC.
3. **The 2026 APPA supplementary CSV** you mentioned — not because UBE3A is our locus, but because if
   any of those compounds were counter-screened against other imprinted domains, that counter-screen is
   exactly the dataset I need.
4. **Anything on what a fracture does to a growth plate that is still open** — the callus experiments
   are all diaphyseal in adults. Whether an injury signal can reach and reactivate an intact growth
   plate's resting zone is the question that turns §2 from a mechanism into an arm, and I could not find
   it in 5,591 enumerated series.

---

*The list was the right kind of thing to bring and I could test it rather than argue about it. It came
out null on dose in the two systems where dose is measurable, and the direction triage removes most of
the rest. What replaced it is better evidenced and worse for us pharmacologically: the only thing that
demonstrably runs the counter backwards is injury, it works better in old animals than young, and
nobody has ever pointed it at a growth plate.*
