# F-R078 — The 14q32.2 locus closes as a lever, the growth plate has its own clock, and the branch had CCN2 pointing backwards

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** Both supplied papers read in full. Kagami answers the request in F-R077 §9 and **corrects
F-R077's own §7c**. Nilsson, re-read after F-R077, turns out to contain the one result that **partially
rescues the pacing law from my own null**. And a systematic audit of the ledger's open terms found a
**sign error in the branch's treatment of CCN2** and an **internal contradiction about the GH dose**.

---

## 1. Kagami is the primary I asked for, and MEG3 is refuted

**Kagami M, Sekita Y, Nishimura G, … Ferguson-Smith AC, Ishino F, Ogata T. "Deletions and epimutations
affecting the human 14q32.2 imprinted region in individuals with paternal and maternal upd(14)-like
phenotypes." *Nature Genetics* 2008;40:237.**

**The four deletions, with parental origin — which is the thing that makes the series informative:**

| cases | deletion | genes | parental origin | phenotype |
|---|---|---|---|---|
| (1), 2 | **108,768 bp** | DLK1, MEG3 | **maternal** | typical upd(14)**pat** (Kagami-Ogata) |
| **9, 10** | **108,768 bp** | DLK1, MEG3 | **paternal** | upd(14)**mat** (Temple), **mild to moderate short stature** |
| 3 | 411,354 bp | WDR25, BEGAIN, DLK1, MEG3, RTL1, RTL1as, MEG8 | maternal | mild upd(14)pat-like |
| **11** | **411,354 bp** | same | **paternal** | upd(14)mat, **marked short stature** |
| 4 | 474,550 bp | MEG3, RTL1, RTL1as, MEG8 (**no DLK1**) | maternal | mild upd(14)pat-like |
| 5 | ~6.5 Mb | whole region | maternal | mild upd(14)pat-like |
| 6–8 | none — **epimutation** | — | maternal | typical upd(14)pat |

> ### **The identical 108.8-kb deletion produces opposite syndromes depending on which parent it came from.** That is the cleanest possible demonstration that this locus is an imprinting-control system, not a gene-dosage system — and it is why F-R077 §7c's "gene count" reading of the series was the wrong frame.

### The height gene is RTL1, and MEG3 is excluded

**F-R077 §7c named "GTL2/MEG3 or RTL1" as candidates. The paper excludes MEG3 and confirms RTL1.**

**Why MEG3 cannot be it, in two independent ways.** First, logically: **MEG3 is maternally expressed**, so a
**paternal** deletion of it removes an allele that was already silent. Cases 9, 10 and 11 all lost paternal
MEG3 and it can have contributed nothing. Second, experimentally, in the authors' own words:

> *"**Gtl2^lacZ** mice with dysregulated imprinting status caused by a transgene insertion have a **normal
> phenotype** with at least **60–80% reduction of all the MEGs**."*

**DIO3 is excluded too** — *"thyroid dysfunction was absent from cases 1–11."*

**And the authors state the answer directly:**

> *"loss of active **DLK1 and RTL1** seems to constitute **additive** underlying major factors for the
> development of the upd(14)mat-like phenotype, because a upd(14)mat-like phenotype is common to cases 9–11,
> who lack active DLK1, and **growth is more severely compromised in case 11, with additional loss of active
> RTL1**."*

**With a quantitative mouse dose–response:**

| genotype | body size |
|---|---|
| paternal **Dlk1** knockout | **~80% of normal** |
| paternal **Rtl1** deletion | **~80% of normal** |
| **MatDi(12)** — both lost | **~60%** |

**0.80 × 0.80 = 0.64 ≈ 0.60. Additive on a log scale, exactly as the authors describe.**

### And this finishes off F-R076 §1

> *"the paternally derived **Dlk1** mutation has been previously shown to result in several upd(14)mat-like
> features, such as **pre- and postnatal growth deficiency** and obesity and facial abnormalities in mice."*

**F-R076 asserted DLK1's whole height effect runs through pubertal timing. F-R077 §7b softened that on
Gomes' argument. Kagami settles it: a paternal Dlk1 mutation costs ~20% of body size in mouse.** DLK1 is
**both** a timing gene and a growth gene. **The original F-R076 claim is now fully retracted, not merely
softened.**

### The locus closes as a lever, and this is the useful conclusion

| gene | loss | excess |
|---|---|---|
| **DLK1** | growth deficiency (~80% size), precocious puberty | 2× → embryonic overgrowth; **3× → late-gestation lethal** |
| **RTL1** | growth deficiency (~80% size) | 2.5–3.0× → placental abnormality; in humans (Kagami-Ogata) **bell-shaped thorax, coat-hanger ribs, growth retardation** |
| MEG3 / all MEGs | **60–80% reduction → normal mouse** | — |
| DIO3 | no thyroid phenotype | — |

> ### **Every gene at 14q32.2 that has a height effect at all has an optimum, and both directions away from it are shorter.** DLK1 up is lethal above one doubling; RTL1 up gives a deformed thorax. **The locus is not a gain-of-height lever and the thread that began in F-R065 is closed.** That is a real answer, not a failure — the branch spent four rounds on this locus and it is now excluded on primary data rather than left open.

*I still do not have Kagami's Supplementary Table 2. The height SD scores −2.9 and −2.2 (cases 9, 10) and
−4.4 (case 11) reach me through Dauber 2017's summary of it; the main text says only "mild to moderate"
and "marked."*

---

## 2. Nilsson re-read — the result that partially rescues the pacing law from my own null

I read this in F-R072 and dismissed the methylation half of it as *"a bulk assay with no site resolution."*
**That was right about the assay and wrong about the finding, because the informative part is not the
number — it is the pattern across tissues in the same animals.**

| tissue / condition, same rabbits, same ages | global CCGG methylation |
|---|---|
| growth plate **resting zone**, rib, fetal → 4 → 16 wk | **DECREASED, P = 0.004** |
| **all three zones**, distal ulna, fetal → 4 wk | **DECREASED, P < 0.001** |
| **between zones within an age** | **no significant difference** |
| **liver**, fetal → 4 → 16 wk | **INCREASED, P < 0.001** |
| cultured RZ chondrocytes, per population doubling | **INCREASED**, +0.21%/PD, P = 0.012 |

> ### In the **same animals at the same ages**, the growth plate loses methylation while the liver gains it. And **within the plate there is no difference between the resting, proliferative and hypertrophic zones** — so the change is not produced by the rapid transit-amplifying divisions, and it does not happen in culture either, where the same cells gain methylation as they divide.

> ### **F-R077 established that the epigenetic clock in blood is chronologically paced. Nilsson establishes that the growth plate is not doing what other tissues in the same animal are doing.** Both are true and they are not in conflict: **the plate has a programme the rest of the body does not share, which is precisely why a systemic readout cannot see it.** F-R077 said the measurement has to be made in physeal tissue. **This is the positive evidence that there is something there to measure.**

**Reconfirmed:** maximum population doublings **13.1 ± 1.1 (fetal) vs 14.6 ± 0.6 (4 wk) vs 14.3 ± 0.8
(16 wk), P = 0.36** — donor age does not spend the intrinsic counter. **Correction to my own F-R072
record:** I wrote that in-culture methylation was independent of donor age; the paper reports **P = 0.068**,
which is a trend, not a clean null.

**And Nilsson's own framing is the branch's thesis, written in 2005:**

> *"loss of DNA methylation might be a fundamental biological mechanism that **limits longitudinal bone
> growth in mammals, thereby determining the overall adult size of the organism**."*

**Nobody has followed it up with a site-resolution assay in twenty-one years.** Third independent search
this programme; still absent.

---

## 3. The audit found the largest untouched term in the identity, and it has a human gene

STACK_STATE §3.1 says of **matrix volume per cell**:

> *"**32–49% of daily elongation** — larger than cellular enlargement in slow plates — and **this branch has
> never once addressed it.**"*

`dL/dt = flux × v(d)`, `v(d) = v(c) + v(m)`. **Between a third and a half of the output term has never been
worked.** So I worked it.

### 3a. ACAN is the human loss-of-function for `v(m)`

**Heterozygous *ACAN* (aggrecan) variants cause autosomal dominant short stature with advanced bone age and
premature epiphyseal fusion** — *"altered growth plate morphogenesis, contributing to premature hypertrophic
chondrocyte maturation and impaired long bone"* growth, with **"reduced hypertrophic cell expansion and
decreased extracellular matrix volume."**

> ### **Halve the matrix and you get a short child whose plate closes early.** That is `v(m)` behaving exactly as the identity says it should — and it comes with the same advanced-bone-age signature as DLK1 loss.

### 3b. And the GH trial in those patients answers a question F-R076 raised about our own stack

**Muthuvel, Dauber et al., 3-year response, n = 10 ACAN-deficient children, rhGH 50 µg/kg/day** (reduced to
32 µg/kg/day by year 3):

| | baseline | 3 years |
|---|---|---|
| height SDS | −2.52 | **change +1.21** (0.82 to 1.94, **P = 0.002**) |
| height velocity | 5.2 cm/y | 8.3 (yr 1) → 6.8 (yr 3) |
| **predicted adult height gain** | | **+6.8 cm** (3.8–9.1, **P = 0.002**) |
| IGF-1 SDS | +0.3 | **+2.3 / +2.5 / +2.1** |
| **bone age / chronological age ratio** | 1.2 | **change −0.10, P = 0.205 — not significant** |

> ### **Three years of IGF-1 held at roughly +2.3 SDS, and skeletal maturation did not advance.** F-R076 §5 raised the worry that if IGF-1 paces the clock, the stack's growth-hormone arm is the accelerant. **This is a direct human test of that worry in the only maturation clock that can be measured in a child, and it is negative** — in a population whose plates are *already* prone to premature fusion, which is the hardest case. **The blast argument survives a real test rather than merely surviving my failure to test it.**

---

## 4. The branch has had CCN2 pointing backwards, and the experiment that matters is published

**This is a sign error in my own ledger and I want it recorded as one.**

The branch reached CCN2 twice, **both times as something to block**:

- **R341** killed it: *"the published Ctgf-null phenotype is an EXPANDED hypertrophic zone with impaired
  angiogenesis — i.e. a DISCHARGE FAILURE… **PAMREVLUMAB therefore points the wrong way**."*
- Later, the p21/Gli1 work found the opposite sign in the neighbouring compartment — *"p21⁺ chondrocytes
  generate a Ccn2-inhibiting area"*, CCN2 restrains Gli1⁺ progenitor recruitment from Pdgfra⁺ stroma — and
  the README amended the kill to **"CCN2 is not a *systemic* lever."**

**Both analyses are about lowering CCN2. In four rounds nobody asked what raising it does — even though the
branch's own reasoning implies the answer:** if blocking CCN2 inside the cartilage causes discharge failure
and is height-negative, then **raising it inside the cartilage should be height-positive.** It is.

**Cartilage-specific CCN2 over-expression — Col2a1 promoter + intron 1, two independent founder lines
(*PLoS One* 2013;8:e59226):**

| readout | result |
|---|---|
| **tibial diaphysis, P1** | **6.225 ± 0.080 mm vs 5.897 ± 0.116 mm wild-type — +5.6%, P < 0.0001** |
| **dose-dependence** | *"the extent of bone elongation… correlated with the extent of CCN2 over-expression… in **both founder lines**"* |
| proteoglycan | *"enhanced density of proteoglycans in the transgenic cartilage"* (Safranin-O) — **this is `v(m)`** |
| Col2a1 / aggrecan mRNA | 100–1,000× / 15,000–20,000× in long-term culture |
| proliferation | PCNA up **in the proliferative zone and also the resting zone** — **flux, and possibly `n₀`** |
| IGF | *"several-fold increase"* in IGF-I and IGF-II mRNA; **CCN2 enhances IGF-1R autophosphorylation**, abolished by PPP |
| **bone strength, pQCT femur, 8 wk** | **total mineral 1.36 ± 0.08 vs 1.10 ± 0.12 mg/mm; trabecular 0.49 vs 0.38; cortical thickness 0.060 vs 0.049 mm — all P < 0.05** |
| adverse | *"no major abnormalities in cartilage or bone development"* at E15.5 |

> ### **This is the only agent the programme has found that lengthens bone and STRENGTHENS it at the same time.** STACK_STATE §3.6 states the mechanical ceiling as a hard physical limit — everything that widens the plate weakens it (SCFE on erdafitinib; Hall 2016 femoral-head dysplasia **and fracture**) — and says abaloparatide is *"an inference from Winer's safety data, not a measurement."* **CCN2 over-expression is the measurement**, in the right direction, on the same animal that got longer.

**What I will not claim, because the paper does not support it:**

- **The only bone-length measurement is the P1 tibial diaphysis, n = 3 per group.**
- **"About 12% larger at 8 weeks" is body size/mass, not bone length** — the authors attribute it to
  *"better eating with tough skeleton."* **I nearly carried that forward as a length figure and it is not one.**
- **Adult bone length was never measured.** Same failure mode as every other lever in this programme.
- Growth-plate zone heights are **qualitative only** — *"the hypertrophic zone was shorter in the transgenic
  embryos"* with no numbers. **A shorter HZ is a `v(c)` cost**, and CCN2 *"promotes the proliferation and
  differentiation, but **not the hypertrophy**, of chondrocytes."*

### Which makes the composition argument sharp rather than vague

**CCN2 raises flux and `v(m)` and shrinks the hypertrophic zone. Erdafitinib raises `v(c)` — HZ +45% against
PZ +25%, with *"significant swelling of hypertrophic cells."* They occupy opposite halves of `v(d)` and the
one's cost is the other's mechanism.** That is the first genuinely complementary pairing in the stack rather
than two agents pushing the same term.

### The compartment problem has a solution the branch already built

CCN2 is height-positive inside the cartilage and height-negative outside it (restraining Gli1⁺ influx).
**A systemic agent hits both, which is exactly why R341's kill was correct.** But the published transgenic
is **promoter-restricted** — Col2a1 — not systemically delivered.

> ### **Col2a1-promoter AAV-CCN2, delivered by the intra-epiphyseal route F-R074 established** (Zhang 2015: 1-mm K-wire into subchondral bone, 5.5 × 10¹¹ vp/mL, 25 µL, 12-week expression). **Promoter restriction solves the compartment problem the branch itself identified; the route solves the delivery problem F-R069–R073 was stuck on. Both halves already exist and nobody has combined them.**

**And one tension I am flagging rather than resolving:** the classical inducer of CCN2 is **TGF-β**, while
F-R034 characterises the resting-zone niche as *"low in WNT and TGF-β"* and F-R073's reprogramming cocktail
contains **Repsox, a TGF-β/ALK5 inhibitor**, mapped onto that niche axis. **A CCN2 arm and a Repsox arm pull
against each other, and I have not worked out whether that matters or whether promoter-driven CCN2 bypasses
it entirely.** It is a real unreconciled conflict in the stack.

---

## 5. An internal contradiction in the ledger, and a human measurement that settles it

**STACK_STATE §1 says** the GH low-dose rationale is *"REVISED in F-R066: withdrawn"* and carries
**0.07 mg/kg/day = 0.49 mg/kg/wk**. **STACK_STATE §3.8 still says** *"0.35 mg/kg/wk is ~5× higher and lands
in the depleting range. The low dose is not a compromise."* **Those cannot both stand, and §3.8 has been
stale since F-R066.**

**§3b settles it with a human measurement rather than an inference.** The ACAN trial ran **50 µg/kg/day =
0.35 mg/kg/wk** — the exact disputed figure — for three years in children, and produced **+1.21 height SDS,
+6.8 cm predicted adult height, and no acceleration of skeletal maturation.** The "depleting range" claim
came from a mouse stem-cell paper; **the only human outcome data at that dose shows sustained gain.**
**§3.8 is corrected to agree with §1.**

---

## 6. Where the programme stands

| line | status |
|---|---|
| never close | solved in humans (F-R065) |
| fast | solved |
| limit is epigenetic, not cell-intrinsic | proven (F-R072) |
| delivery to the epiphysis | solved (F-R074) |
| blood clock as a readout of plate senescence | **dead (F-R077)** |
| **the plate has a programme other tissues do not share** | **positive evidence (§2) — plate down, liver up, same animals** |
| **14q32.2 imprinted locus as a lever** | **CLOSED (§1) — every gene there has an optimum and both directions are shorter** |
| **`v(m)`, 32–49% of elongation, "never once addressed"** | **ADDRESSED — human LoF gene (ACAN), and a published gain-of-function that lengthens bone (§3, §4)** |
| **mechanical ceiling (§3.6)** | **first measured counter-example — CCN2 lengthens and strengthens together** |
| **IGF-1 as the maturation-clock accelerant** | **tested in humans and negative (§3b)** |
| stem-pool expansion arm | **still no agent** — but CCN2 raised proliferation in the **resting zone**, which is the first hint of one that is not mTORC1 |
| site-resolution methylome in growth plate | **still absent — third independent search** |
| reversal extends longitudinal growth | never attempted |

---

## 7. What I need

**I checked `frontier/SUPPLIED_INDEX.md` first.** Three, in order.

1. **Kagami 2008 Supplementary Tables 1–3** (*Nat Genet* 40:237). §1 rests on the main text plus Dauber's
   summary of the supplement. I want the actual height SD scores, birth measurements and pubertal data for
   cases 9, 10 and 11, and the phenotypic scoring in Supplementary Table 3 that the discussion keeps citing.
2. **Any measurement of adult or skeletally mature bone length in a CCN2 over-expressing mouse** — the
   *PLoS One* line, or any other. §4 is built on a **P1 tibia with n = 3**, and the entire question is
   whether the neonatal gain survives to maturity or is spent early, which is the failure mode of every
   other lever in this programme. **A negative would be as valuable as a positive.**
3. **Any DNA methylation data with site resolution from growth-plate tissue at two or more postnatal ages,
   any species.** Unchanged from F-R077 and now confirmed absent by a third independent search. §2 is the
   argument for why it is worth generating: Nilsson showed in 2005 that the plate moves opposite to liver in
   the same animals, and called it *"a fundamental biological mechanism that limits longitudinal bone
   growth… determining the overall adult size of the organism."* **Twenty-one years, no follow-up.**

---

## 8. Sources

- Kagami et al., *Nat Genet* 2008;40:237 — **supplied**
- Nilsson et al., *J Endocrinol* 2005;186:241 — **supplied** (re-read)
- Dauber et al., *JCEM* 2017;102:1557; Gomes et al., *JCEM* 2019;104:2112 — supplied F-R077
- Cartilage-specific CCN2 over-expression — [PLoS One 2013;8:e59226](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0059226) / [PMC3610707](https://pmc.ncbi.nlm.nih.gov/articles/PMC3610707/)
- Muthuvel, Dauber et al., rhGH in ACAN deficiency, 3-year — [PMC11535719](https://pmc.ncbi.nlm.nih.gov/articles/PMC11535719/); 1-year — [JCEM 107:e2103](https://academic.oup.com/jcem/article/107/5/e2103/6469588)
- Nishida et al., recombinant CCN2 in rat articular cartilage defects, *JBMR* 2004 — [DOI](https://onlinelibrary.wiley.com/doi/full/10.1359/JBMR.040322)
- CCN2 in gelatin hydrogel for bone regeneration — [PubMed 19230129](https://pubmed.ncbi.nlm.nih.gov/19230129/)
