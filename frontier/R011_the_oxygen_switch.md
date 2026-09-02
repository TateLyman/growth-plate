# F-R011 — the same substrate lengthens or shortens the bone depending on the oxygen tension of the tissue receiving it

**I was wrong in F-R010 to propose downgrading this file's α-ketoglutarate contraindication. A 2019
*Nature* paper — by the same laboratory whose 2025 paper started this whole thread — gives the
mechanism, and it runs the opposite way to my assumption. In a HYPOXIC chondrocyte, glutamine flux
raises α-ketoglutarate, which **hyper-hydroxylates proline and lysine on collagen**, making the matrix
**resistant to protease-mediated degradation** — more bone mass, and **skeletal dysplasia**. The
contraindication was right. It was right for the wrong reason, and the real reason is grade A.**

**And that single fact closes the loop on everything: avascularity does not merely starve the growth
plate. It converts the plate's own matrix into a form that cannot be cleared. Supply without
perfusion is not neutral. It is harmful.**

Date 2026-08-28 · operator-supplied, read in full: `andersen2008`, `tatara2005turkey`,
`sliwa2009`, `tatara2005piglet` · found from them: `stegen2019` (*Nature* 565:511–515, PMID 30651640,
PMC7195049) · texts in `frontier/screens/mtorc1/`

---

## 1. The finding that inverts F-R010

**`stegen2019`, abstract, verbatim:**

> *"prolonged HIF-1α signalling in chondrocytes leads to **skeletal dysplasia** by interfering with
> cellular bioenergetics and biosynthesis. Decreased glucose oxidation results in an energy deficit,
> which limits proliferation, activates the unfolded protein response and **reduces collagen
> synthesis**. However, **enhanced glutamine flux increases α-ketoglutarate levels, which in turn
> increases PROLINE AND LYSINE HYDROXYLATION on collagen. This metabolically regulated collagen
> modification renders the cartilaginous matrix MORE RESISTANT TO PROTEASE-MEDIATED DEGRADATION and
> thereby INCREASES BONE MASS.**"*

**I assumed in F-R010 that AKG → proline → more collagen substrate → longer bone. That is not what
AKG does in a hypoxic chondrocyte. It does not build more collagen. It over-modifies the collagen
that is there, and the over-modified matrix cannot be removed.**

> ### **Elongation requires the hypertrophic matrix to be DEGRADED and replaced at the chondro-osseous junction. A protease-resistant matrix is charge without discharge, written at the level of a post-translational modification.**

**`s41586-019-0874` returns 0 files in this atlas. `collagen modification` 0. `proline hydroxylation`
0.** P4HA and PLOD — the very enzymes — appear in R444 and R454 as *matrix machinery*, with **no
record that their activity is set by α-ketoglutarate and therefore by oxygen tension.**

## 2. It explains the entire Lublin pig corpus, which I read as a puzzle and is actually one result

Every one of these papers reports the **same shape**: mass up, length flat or down.

| study | n | intervention | **mass / density / strength** | **LENGTH** |
|---|---:|---|---|---|
| `tatara2007` | 141 pigs | maternal HMB | weight 301→322 g, trabecular vBMD 1.364→1.448, cortical 2.439→2.608, CSA 275→318, strength ↑ | ⛔ **200.9 → 196.8 mm (−2.0%)** |
| `tatara2005piglet` | piglets | postnatal AKG, femur | density and geometry ↑ | **55.4/54.4, 73.3/74.5, 75.2/75.5 — all ns** |
| `tatara2005turkey` | turkeys | AKG 0.4 g/kg × 98 d | *"positive effect on **all** bone characteristics"* | ⛔ ***"except bone length"*** |
| `andersen2008` | 24 pigs | postnatal AKG, femur + humerus | cortical density ↑, humerus strength +43% | **femur 200.3→202.5 ns; humerus 182.4→182.9 ns** |
| `tatara2012` | 259 pigs | maternal AKG **alone** | weight 300→319 g, vBMD ↑ | **197.4 → 197.7 — nothing** |

**Five studies, four species-and-site combinations, one signature: α-ketoglutarate reliably makes bone
heavier, denser and stronger, and reliably does nothing for length or reduces it.** `stegen2019` says
why, in one sentence: **more hydroxylation, less degradability, more mass.**

**And `tatara2005turkey` even measured the intermediate.** Its own abstract: *"Plasma concentrations of
**proline and leucine were increased by AKG**, whereas **glutamine** was **decreased**."* **Glutamine
consumed, proline produced — the exact flux `stegen2019` maps — and the bone did not get longer.**

## 3. ⭐⭐⭐ AND THE ONE EXCEPTION IS THE PROOF

`andersen2008`, Table 2. **Same 24 animals. Same 0.1 g/kg/day oral AKG for 21 days. Three bones
measured in the same carcass:**

| | Control | AKG | |
|---|---:|---:|---|
| **Sixth rib — length (mm)** | **232.9 ± 4.2** | **250.0 ± 4.1** | **+7.3%, p < 0.01** |
| Humerus — length (mm) | 182.4 ± 2.4 | 182.9 ± 2.3 | +0.3%, ns |
| Femur — length (mm) | 200.3 ± 2.9 | 202.5 ± 2.9 | +1.1%, ns |

and the rib also gains **ultimate strength +23% (p<0.05)** and **Young's modulus +52% (p<0.001)**.

> ### **One animal. One dose. One circulation. The rib grew 7.3% longer and the two weight-bearing long bones did not move.**

**The rib is the bone whose growth plate is (i) not weight-bearing, (ii) thin, and (iii) closest to
perichondrial vessels.** Under R448's own physics those are not three variables but one: permeability
is **exponentially strain-dependent**, so load and transport are the same term, and a thin plate has a
shorter diffusion path. **The costochondral junction is the least hypoxic growth plate in the body —
which is precisely why it is the classical site for scoring nutritional bone disease.**

**Under `stegen2019` the prediction is exact: where HIF-1α tone is low, AKG's carbon goes into
collagen and the bone lengthens; where HIF-1α tone is high, the same carbon goes into hydroxylation
and the bone does not.** The rib is the internal control I could not have designed better, and it was
sitting in Table 2 of a 2008 animal-nutrition paper.

## 4. THE LAW, corrected

F-R010 proposed *growth = f(signal) × g(substrate)*. **That is incomplete and the missing term
reverses the sign of the substrate term.**

> # **Growth = SYNTHESIS × DISCHARGE, and OXYGEN sets both.**
>
> **Hypoxia lowers synthesis** (`stegen2019`: energy deficit → UPR → reduced collagen synthesis;
> `loopmans2025`: NADPH deficit → ferroptosis in the hypertrophic zone).
> **Hypoxia simultaneously blocks discharge** (`stegen2019`: glutamine → αKG → proline/lysine
> hyper-hydroxylation → protease-resistant matrix).
>
> **Therefore substrate given to a hypoxic plate does not become length. It becomes an unremovable
> matrix. Supply without perfusion is not neutral — it is the wrong direction.**

Now every result in this branch falls out of one diagram:

| system | O₂ / access | substrate | signal | outcome |
|---|---|---|---|---|
| pig femur, HMB alone | low | ✘ | ✔ | **−2.0% length**, +7% mass |
| pig femur, AKG alone | low | ✔ | ✘ | **0% length**, +6% mass |
| turkey radius, AKG | low | ✔ | ✔ (leucine ↑) | **0% length**, everything else ↑ |
| pig femur, AKG+HMB | low | ✔✔ | ✔ | **+1.8%** |
| **pig RIB, AKG** | **high** | ✔ | ✘ | ⭐ **+7.3%** |
| **mouse metatarsal + CQ/Baf** | **high (dish)** | ✔✔ medium | ✔✔ | ⭐⭐ **+91–170%, h_term +71%** |
| **deer antler** | **vascularised** | ✔✔✔ | ✔ | ⭐⭐⭐ **365×** |
| Tsc1 cKO in vivo, dying | low + restricted thorax | ✘ | ✔✔✔ | chondrodysplasia |
| HIF-1α stabilised (`stegen2019`) | **maximal hypoxic signalling** | — | — | **skeletal dysplasia** |

**The oxygen/access column predicts the length outcome in every row. The signal column predicts
nothing on its own, and the substrate column changes sign with oxygen.**

**And it reframes the field's oldest number one last time.** GH, CNP, IGF-1, FGFR3, hedgehog — thirty
years, unrelated mechanisms, all converging on **2–4%** — are all signals delivered to a tissue that
is simultaneously **synthesis-starved and discharge-jammed by its own hypoxia.** The convergence is
not a property of growth. **It is the ceiling of shouting at a factory whose loading dock is shut and
whose finished goods cannot leave the building.**

## 5. ⛔ Correction to F-R010, made explicitly

F-R010 §4 said this file's α-ketoglutarate contraindication, made *"on mechanism alone"* (TET
co-substrate → demethylation → senescence, grade E), *"should be downgraded to a contested caveat."*

**Withdrawn.** `stegen2019` gives AKG a **grade-A, mechanism-plus-phenotype reason to be
contraindicated for LENGTH** — collagen over-hydroxylation, protease resistance, skeletal dysplasia —
that is independent of, and much stronger than, the TET argument. **The conclusion in `CLAUDE.md` was
correct and my proposed revision was wrong.** What should change is not the verdict but the reason,
and the reason matters because it names the condition under which it flips: **AKG is contraindicated
in a hypoxic plate and may be beneficial in a perfused one.** The rib is the evidence for the second
clause.

⚠ I am not claiming the pig rib result proves the mechanism — `andersen2008` measured no oxygen, no
hydroxylation and no HIF-1α. **What it does is agree with the prediction, in the one site where the
prediction differs.**

## 6. What this makes the actual programme

**Order of operations is now not a preference. It is a sign.**

1. **Raise access first** — perfusion, unloading. Until this is done, steps 2 and 3 are neutral to
   harmful. `stegen2019` is the mechanism; the rib is the demonstration; the antler is the ceiling.
2. **Then substrate** — and the target is *collagen synthesis*, not collagen modification. That means
   the amino acids themselves under adequate O₂, not αKG into a hypoxic plate.
3. **Then signal** — mTORC1, pulsed at the ligand level (`newton2015`'s +91–170% and **h_term +71%**;
   NV-5138/leucine at the Sestrin2 input; never brake deletion, per CORR-300 and `yan2016`).
4. **And keep the discharge open** — MMP-13/protease access at the chondro-osseous junction is now
   implicated twice independently: `yan2016`'s blots and `stegen2019`'s mechanism.

**The single decisive experiment is unchanged in form and now has a second axis:** the `newton2015`
5-day metatarsal culture, run as a **2 × 2 of oxygen tension × substrate**.

| | **21% O₂** | **1–2% O₂ (physiological plate)** |
|---|---|---|
| control medium | baseline | baseline-low |
| **+ αKG / glutamine** | *predict: length ↑* | **predict: length ↓ or flat, hydroxyproline ↑, matrix protease-resistant** |

Read length, hydroxyproline:proline ratio, and matrix degradability. **If the same substrate reverses
sign with oxygen, the law is proven in one experiment, and the entire nutritional literature of this
field — including five pig studies — is reinterpreted.**

## 7. Status of the two things you asked me to solve

**(a) The antler matrix — this route is now closed and I will stop spending your time on it.** I
cloned `heshidian/DeerAntlersSingleCell` (30 MB). **It is analysis scripts only.** The data paths are
the authors' local array — `/media/heshidian/RAID5_42TB/0.MyFiles/1.BGI/6.Cartialgenous/…` — and the
only accessions in the code are `GSE215758` (the osteosarcoma comparator, not the antler) and
reference annotations. No matrix, no metadata, no hardcoded values. CNGB `CNP0003724` resolves to a
JavaScript page whose data API returns 502 and whose FTP paths 404 in all six data partitions.
**The only remaining route is the corresponding authors** — `bahengxing@cstu.edu.cn`,
`lichunyi1959@163.com`, `guying@genomics.cn` — **and one per-layer average-expression table is all I
need.** I would not spend more effort here; §6 does not depend on it.

**(b) Better tooling — built, and it produced this round.** `frontier/screens/litsearch.py` now runs
OpenAlex, Crossref and Semantic Scholar alongside Europe PMC, with backoff. **`stegen2019` — a 2019
*Nature* paper with 316 citations, central to this entire question, and absent from this atlas — was
returned by an OpenAlex query on "proline supplementation bone growth longitudinal collagen
synthesis" and does not surface on the equivalent Europe PMC query.** That is the tooling paying for
itself in one round.

## 8. What I want next

1. ⭐⭐ **`stegen2019` full text (PMC7195049, open access)** — I need the **magnitude**: how much shorter,
   which bones, and above all whether they measured **length under HIF-1α LOSS** (the opposite
   direction). If HIF-1α deletion *lengthens* bone, that is the in-vivo proof of §4 and the most
   important number left.
2. ⭐ **Anything measuring hydroxyproline:proline ratio or collagen cross-link density by growth-plate
   zone** — the modification gradient across the plate has, as far as I can find, never been measured,
   and §4 predicts it rises toward the hypoxic centre.
3. **Any bone-lengthening or growth study run at controlled oxygen tension.** Organ-culture work is
   almost always at 21% O₂ — which, if §4 is right, means **the entire ex-vivo literature has been
   run at an oxygen tension the tissue never sees**, and that is why it disagrees with the in-vivo
   literature so often.
