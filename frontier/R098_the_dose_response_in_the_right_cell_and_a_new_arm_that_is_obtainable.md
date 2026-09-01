# F-R098 — The dose-response measured in the right cell, and a new arm that is upstream of Hedgehog, human-validated, tissue-selective and obtainable

`GSM7831319` was the experiment I asked for in F-R096 and F-R097. And `1697.pdf` opened an arm this
branch flagged once, in a table, at F-R022, and then never touched again.

---

## 1. The dose-response, in PTHrP⁺ stem cells, at the human genotype

`GSE244884` (Orikasa et al.) contains exactly two samples, both **femur growth plate, PTHrP-creER
lineage-marked at P6, tdTomato⁺ FACS-sorted, analysed at P36**:

| | genotype | what it models |
|---|---|---|
| **GSM7831319** | `PTHrP-creER; Ptch1(fl/+); R26R-tdTomato` | **Ptch1 heterozygous — the human *PTCH1*⁺/⁻ genotype** |
| GSM7831318 | `Col1-GFP; PTHrP-creER; Ptch1(fl/fl); R26R-tdTomato` | Ptch1 homozygous null — full brake removal |

I downloaded both raw matrices and classified the PTHrP lineage by marker-set score.
Script and output: `frontier/analysis/GSE244884/`.

**Where the PTHrP lineage ended up by P36:**

| fate | **Ptch1 fl/+ (het)** | **Ptch1 fl/fl (KO)** |
|---|---|---|
| **resting-zone / stem** | **70.0%** | **44.9%** |
| proliferative | 7.7% | 14.3% |
| pre-hypertrophic / hypertrophic | 18.8% | 33.4% |
| **osteoblast** | **2.2%** | **4.9%** |
| stromal | 1.3% | 2.4% |

χ² p = 1.6e-29. **Robust to both QC threshold and marker choice:**

| parameterisation | stem, het | stem, KO | osteoblast, het | osteoblast, KO |
|---|---|---|---|---|
| primary markers, nGene ≥1000 | 70.0% | 44.9% | 2.2% | 4.9% |
| reduced marker set | 57.2% | 25.7% | 16.7% | 30.7% |
| primary markers, nGene ≥2000 | 72.4% | 48.3% | 2.0% | 4.4% |

**Halving Ptch1 keeps the lineage in the stem compartment. Removing both copies empties it — into
proliferation, hypertrophy, and osteoblasts.** Osteoblast conversion roughly doubles, which is Orikasa's
published headline.

**This locates F-R088's error exactly.** F-R088 read *"Hedgehog activation promotes osteogenic fates of
resting zone chondrocytes"* and filed Hedgehog under "spends the pool." **That is the homozygous
phenotype.** At the heterozygous dose — **the dose every tall human in F-R096 and F-R097 actually
carries** — the lineage stays put. F-R096 predicted this dose-response from human genetics; here it is,
in the right cell, at the right age.

### The caveats, and one of them is serious

1. **There is no wild-type arm in this pair.** I can say het retains far more stem fraction than KO. I
   **cannot** say het is above wild-type. Gain-above-normal is still unmeasured.
2. **Two samples, two sequencing runs** (NovaA-237 and NovaA-186), 633 versus 4870 cells. Composition
   differences between separate 10x runs can be technical. **I cannot fully separate genotype from
   batch with n=1 per arm.**
3. **The Hedgehog readout inside the surviving stem cells does not confirm stronger signalling in the
   KO:** Gli1 0.100 → 0.131 (p=0.075, ns), Ptch1 unchanged (p=0.78), and **Hhip is *lower* in the KO**
   (0.784 → 0.648, p=1.7e-4) — the wrong direction for a Hedgehog target. The most likely reading is
   **survivorship**: the cells that responded most strongly to Ptch1 loss have already left the stem
   compartment, so what remains in the KO is the non-recombined or non-responding remnant. That is
   consistent with the fate table, but it is an inference, not a demonstration.
4. Cyclin D1 is **higher** in het stem cells than KO stem cells (0.493 vs 0.280, p=6e-13) — the het
   stem pool looks cycling-competent, the KO remnant looks quiescent-by-exhaustion. Suggestive, same
   caveats.

**Verdict: the direction predicted from human genetics is present in the right cell at the right dose,
and the wild-type arm is what would make it conclusive.**

---

## 2. `kosaki2011` — one more case, and the cleanest parental control yet

9q22.3 deletion, 2.4 Mb spanning *PTCH1*:

| | |
|---|---|
| father / mother | **175 cm / 166 cm — both normal stature** |
| birth weight | 3,833 g (**+2.0 SD**) |
| birth crown-heel length | 53.5 cm (**+2.1 SD**) |
| later | weight +3.5 SD, **height 95.5 cm (+3.8 SD)** |

**+3.8 SD with two normal-height parents.** The human range for *PTCH1* haploinsufficiency now reads:
**+0.8 SD (Ewing, over mid-parental target), +2.3 SD (Yamada daughter at 9), +2.9 SD (Yamada mother at
17), +3.4 SD (Italian frameshift at 9), +3.8 SD (Kosaki)** — against the one counterexample at −3 SD
that carries a second diagnosis (F-R097 §1).

---

## 3. The new arm: sulfation sets the *range* of Indian hedgehog

`Cortes M, Baria AT, Schwartz NB. Sulfation of chondroitin sulfate proteoglycans is necessary for proper
Indian hedgehog signaling in the developing growth plate. Development 2009;136:1697–1706.`

The **brachymorphic (bm) mouse** carries a *Papss2* mutation → less PAPS → **undersulfated chondroitin
sulfate**. Its growth plate shows:

1. *"abnormal Ihh distribution in the ECM… **reduced Ihh diffusion** and abnormal aggregation"*
2. **reduced *Ptch1* mRNA** — a direct Hedgehog target
3. **reduced Gli1-activator : Gli3-repressor ratio**
4. decreased range of Ptch-LacZ⁺ cells
5. **decreased chondrocyte proliferation**

And the biochemistry: **Ihh binds chondroitin sulfate, specifically chondroitin-4-sulfate**, and binds
**aggrecan through its CS chains**.

**Then the sentence that makes this an arm rather than a curiosity:**

> *"the phenotype associated with reduced chondroitin sulfation in the bm mouse is **the opposite of** the
> phenotype seen in HS synthesis mutants, particularly the **Ext1 gene trap mutant, in which reduction of
> HS results in an INCREASED RANGE of Hh signaling marked by increases in Ptch1 and Pthrp mRNA, as well
> as increased chondrocyte proliferation and EXPANSION OF THE PROLIFERATIVE ZONE**."*

**The extracellular matrix sets how far Ihh travels, and it is bidirectional and titratable.**

### Why this matters more than another agonist

F-R092 established, from your own GSE288028 data, the geometry of the problem: **IHH is manufactured in
the prehypertrophic zone; the stem cells sit far away at the top of the plate, receptor-rich
(PTCH1 ~51%, SMO ~17%, BOC, EVC2) and ligand-starved, with HHIP deployed around them as a decoy.**

**Sulfation is the variable that determines whether Ihh reaches them.**

And it solves the problem that has blocked every Hedgehog agent in this file: **tissue selectivity.**
A systemic SMO agonist activates Hedgehog everywhere — which is why Li/Yang's dose-limiting toxicity was
gut (intestinal hyperplasia 6.1%). **Raising the diffusion range of Ihh does nothing where there is no
Ihh. The ligand source is in the growth plate.** This is a route to growth-plate-restricted Hedgehog
elevation without systemic SMO agonism.

### The human genetics, which I ran

Same GWAS Catalog scan as F-R095, restricted to the sulfation machinery:

| gene | function | height associations | min p |
|---|---|---|---|
| **CSGALNACT1** | CS chain initiation | **16** | **4e-78** |
| **UST** | CS uronyl-2-O-sulfotransferase | **13** | 1e-54 |
| **EXTL3** | HS chain elongation | **12** | 7e-54 |
| **CHST11** | **chondroitin-4-sulfotransferase** | **10** | 7e-47 |
| SDC2 | syndecan-2 | 5 | 5e-23 |
| EXT1 / EXT2 | HS polymerase | 4 / 2 | 5e-18 / 8e-35 |
| HS6ST1 | HS 6-O-sulfotransferase | 4 | 1e-50 |
| CHST3 | chondroitin-6-sulfotransferase | 3 | 5e-16 |
| HSPG2 (perlecan) | HS/CS hybrid PG | 3 | 9e-60 |
| **PAPSS2** | PAPS synthase | 1 | **3e-35** |
| **SLC13A1** | renal sulfate reabsorption | 1 | **3e-24** |

**CHST11 is chondroitin-4-sulfotransferase — and chondroitin-4-sulfate is the exact species Cortes
showed Ihh binds.** The whole machinery, both CS and HS arms, carries human height signal.

### And the human loss-of-function syndrome exists

**SLC13A1** is the renal sulfate transporter and the master regulator of serum sulfate.
- `Slc13a1`-null mice: hyposulfatemia and **impaired growth**
- dogs and sheep with natural homozygous LoF: hyposulfatemia and **osteochondrodysplasia with growth
  restriction**
- **humans with biallelic LoF: hyposulfatemia with short stature, scoliosis and skeletal dysplasia**

**Serum sulfate → CS sulfation → Ihh range → growth. The chain is complete, from a small inorganic anion
to human stature, with a human deficiency syndrome at one end.**

### The one place the rescue law may not apply — and I am applying it to myself first

**Everything above is loss-of-function.** By F-R094's rescue law I should expect that raising sulfate in
a sulfate-replete person does nothing, exactly like SAG in a wild-type mouse.

**But the transport kinetics say this case may be different.** The chondrocyte sulfate transporter Km is
**~16 mM**, against a serum sulfate concentration of **~0.3 mM** — *"about 50-times the serum sulfate
concentration… under normal physiological conditions, sulfate transporters are **not saturated**."*

**The system runs at roughly 2% of Km.** In that regime uptake is near-linear in extracellular sulfate,
and there is no saturation plateau defending a set-point. **That is structurally unlike every other
lever in this file**, all of which sit at or near a defended maximum.

**Counterweights, stated plainly:**
- Cells have an **intracellular backup**: they can oxidise cysteine to replenish the sulfate pool, which
  may buffer plasma changes and blunt any benefit.
- **Nobody has shown supra-normal sulfate produces supra-normal growth.** This remains an inference from
  kinetics, not a result.
- Sulfation modifies Ihh **range**, which is a signalling-strength lever — whether that translates to
  pool (`n₀`) or only rate (`v`) is unmeasured.
- The depletion direction is real and clinically relevant: **paracetamol depletes serum sulfate** through
  sulfate conjugation and inhibits cartilage GAG synthesis in rat cartilage. Chronic paracetamol is a
  *negative* for this arm.

**Obtainable inputs, in the order I would rank them:** dietary/inorganic sulfate, **MSM
(methylsulfonylmethane)**, **N-acetylcysteine**, and simply not depleting the pool. All are cheap,
oral, and unremarkable — which is the first time in this programme that the leading candidate for an arm
is not a research chemical.

---

## 4. Where the whole argument stands

| term | agent | status |
|---|---|---|
| **pool `n₀`** | Ptch1 haploinsufficiency-equivalent Hedgehog elevation | human dose-response established (F-R096/97); mouse dose-response in the right cell (§1); **no drug that reproduces the 50% chronic regime** |
| **pool, upstream and tissue-selective** | **sulfation → Ihh range** | **NEW.** Human LoF syndrome, GWAS across the machinery, 50× kinetic headroom. **Untested in the gain direction.** |
| rate `v` | erdafitinib, mecasermin | unchanged |
| **duration / never-closing** | RARγ antagonism, anastrozole | **still the weakest term** — F-R094 showed CD2665 alone does nothing to length |
| do no harm | somatropin down + intermittent | F-R089 |

**The honest structure: we now have two independent routes to the pool and still no route to duration.**
Every *PTCH1* patient stops growing on schedule (F-R097 §5).

## 5. Asks

1. **A wild-type arm for GSE244884** — `PTHrP-creER; Ptch1(+/+); R26R-tdTomato` at P36, or any
   Ptch1⁺/⁻ growth-plate histology with resting-zone counts. **This converts §1 from a two-genotype
   comparison into gain-above-normal.** Still the top item, unchanged from F-R096.
2. **Any experiment raising sulfate, MSM or NAC with a bone-length or growth-plate endpoint**, in any
   species. If sulfation is a real gain lever, someone has overfed sulfate to a growing animal.
3. **Koziel et al. 2004** (*Ext1* gene trap — increased Hh range, expanded proliferative zone). I have
   it only through Cortes's citation. **Whether that mouse is longer is the whole question**, and it is
   the closest existing thing to a gain-of-range experiment.
4. **Serum sulfate versus height, or versus growth velocity, in any human cohort.** Sulfate is measurable
   and children are measured; the correlation may already exist in a dataset.
5. Still open: Xiu 2022 supplementary; bone age in any *PTCH1* overgrowth patient; chronic low-dose SMO
   agonism in a growing animal.

---

*The sulfation arm was in F-R022's table as one word — "sulfate" — under a column of untried knobs, and
it never reached the ledger. It took a 2009 paper to show it is the variable that decides whether Ihh
reaches the cells that F-R092 showed are waiting for it.*
