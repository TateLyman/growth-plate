# F-R009 — the unlock: one node reads the supply the plate cannot get, and it sets BOTH terms of height

**Correction first: I said in F-R008 that chloroquine could not be assumed to do what bafilomycin
does. It was tested in the same paper, and it works. An approved, oral, paediatric-dosed drug
stimulates longitudinal bone growth in cultured bone to the same extent as IGF-1, p < 0.001, across
39 bones — and the growth is "entirely attributed to promoted chondrocyte hypertrophy without any
contribution from cell proliferation," with proliferation FALLING. More length from fewer divisions.
This atlas has zero files on it.**

Date 2026-08-27 · operator-supplied and read in full: `newton2015` (*Autophagy* 11:1594–1607, PMID
26259639) and `yan2016` **Supplementary Information** · new tooling `frontier/screens/litsearch.py`

---

## 0. The correction, stated plainly

F-R008 §0 said: *"the accessible lysosomotropic agents — chloroquine, hydroxychloroquine — cannot be
assumed to do the same thing… That is a question, not a claim."*

**It was not a question. It was Figure 1 of the paper I was writing about.** `newton2015`, Results,
first paragraph:

> **"Baf and CQ stimulated growth to the same extent as the well-established promoter of bone growth
> IGF1 (Fig. 1A, 1B) with the effect of Baf being more potent than CQ (710 ± 18 μm versus 880 ± 28 μm
> growth in 5 d, p < 0.001, n = 13 animals [39 metatarsal bones] for CQ and 7 animals [21 bones] for
> Baf)."**

**Chloroquine — 30 µM, 39 metatarsal bones, 13 animals — grows bone as well as IGF-1.**

---

## 1. ⭐⭐⭐ THE DECOMPOSITION, AND IT IS THE MOST VALUABLE PROPERTY IN THIS FILE

`newton2015` measured every term in the same bones. Verbatim:

> **"the observed growth stimulation was ENTIRELY ATTRIBUTED TO THE PROMOTED CHONDROCYTE HYPERTROPHY
> WITHOUT ANY CONTRIBUTION FROM CELL PROLIFERATION OR SURVIVAL."**

| term | effect | statistic |
|---|---|---|
| **longitudinal growth** | **UP**, ≈ IGF-1 | **p < 0.001**, n = 39 (CQ) / 21 (Baf) bones |
| **terminal hypertrophic cell SIZE** | **UP** | p < 0.01, n = 5 |
| **COL10A1⁺ hypertrophic zone** | **194 ± 13 → 265 ± 23 µm** | p = 0.028, n = 5 |
| **cell PROLIFERATION** | ⬇ **10.6% → 6.0% BrdU** | **p = 0.024** |
| RPS6 phosphorylation | Baf **10.1-fold**, CQ **2.2-fold** | p = 0.011 / 0.016 |
| zone organisation, proteoglycan turnover, GAG release, mineralisation, osteoclast number | **all unchanged** | ns |
| **Torin1 (mTOR inhibitor)** | **abolishes the growth effect** | Fig. 1F, 1G |
| Atg5-null bones | **same effect** → autophagy-independent | Fig. 3 |

> ### **MORE LENGTH. FEWER DIVISIONS. That is the one direction this atlas's central constraint does not tax.**

`POSITIVE_LEDGER.md`, R199, R459 and R470 all state the trap in the same words: **every agent that
raises rate spends the reserve faster.** GH's own arithmetic (R395, `hunziker1994`) is the extreme
case — *97% of its effect is pool consumption*, break-even on yield. **Here proliferation goes DOWN
by 43% while length goes UP.** Whatever is being spent, it is not divisions.

**And it is h_term.** The atlas's largest single term — **44–59% of longitudinal growth** (CORR-361) —
about which R295 wrote: **"the swelling machinery has only ever been switched OFF."** `bush2010`
(bumetanide, −35%), `loqman2013` (DIDS), every entry in the file is an inhibitor.

**Here it is switched ON, pharmacologically, with a drug that has been in human paediatric use for
seventy years, and `newton2015` returns 0 files in this atlas.**

⚠ **What the text does not give is the control value**, so I cannot state a percentage over vehicle —
710 and 880 µm are CQ versus Baf, and the vehicle curve is in Figure 1A/B only. **The comparator that
IS stated is IGF-1, and matching IGF-1 is the meaningful benchmark.** → ask §6.1.

⚠ **And the direction is inverted relative to every other tissue, which is why the paper exists.**
`figueiredo2020` (*Biosci Rep* 40, 120 citations) is titled *"Chloroquine and bafilomycin A mimic
lysosomal storage disorders and IMPAIR mTORC1 signalling."* **Both are true. mTORC1's response to
lysosomal inhibition is cell-type-specific and the chondrocyte is the exception.** `newton2015`'s own
words: *"much to our surprise… this finding is at odds with…"*. **That exception is the finding, and
it means nothing here generalises from other tissues — including the safety reasoning.**

---

## 2. ⭐⭐⭐ THE UNLOCK — every constraint in this file is one sensor reading a supply that isn't there

Put the five rounds together.

**F-R005/F-R006 established what limits the tissue:** it is avascular, and therefore transport-limited
(R450/452), extensibility-limited (R448), matrix-supply-limited (R461), secreting at the plasma-cell
ceiling (R454), redox-limited (`loopmans2025`), and a **cysteine auxotroph with the weakest importer
on its own panel** (F-R005 §2). The antler removes the avascularity and runs **365× faster**, and its
authors attribute it to overcoming *"the METABOLIC LIMITS that typically constrain hypertrophic
expansion in avascular cartilage."*

**F-R007 established what bounds height:** `p`, the stem-daughter renewal probability, ~1 percentage
point below the 0.500 threshold, with an exponential payoff.

**F-R008 and this round establish what moves both:** mTORC1.

> ### **mTORC1 is the amino-acid, energy and oxygen sensor. It reads exactly the supply an avascular tissue cannot get. And its two outputs are exactly the two terms of the height identity: CELL SIZE (h_term, 44–59% of elongation) and DIVISION SYMMETRY (p, which sets duration).**

**That single statement predicts all four experimental results without adjustment:**

| manipulation | prediction | observed |
|---|---|---|
| **raise the sensor pharmacologically** | h_term ↑, length ↑ | `newton2015`: **cell size ↑, COL10A1 zone 194→265 µm, growth ≈ IGF-1, p<0.001, Torin1-reversible** |
| **raise it genetically, ex vivo** | length ↑ without proliferation | `newton2018`: **+52%, p=0.0016, n=18, no proliferation or COL10A1 change** |
| **raise it genetically, in vivo, postnatally** | `p` ↑, plate held open | `newton2019` Supp. Table 3: **plate 124→270 µm at P90, RZ 3.8×, clone size 2.6×, "accelerated expansion of colony-forming cells"** |
| **lower it** | shorter bones | `newton2019` Supp. Table 4: **tibia −5.2% (p=0.047), femur −6.2% (p=0.011)**, digital calipers, P90 |
| **saturate it constitutively from embryogenesis** | zonal order destroyed, shorter — **CORR-300's middle category** | `yan2016`: **chondrodysplasia**, HZ +44%, MMP-13 down, rapamycin rescues survival |

**Five manipulations. One node. Every sign correct.**

**And this is why the whole field converges on 2–4%.** GH, CNP, IGF-1, FGFR3 all act *upstream*, on
receptors, in a tissue whose downstream sensor is already reading "starved." **You can shout louder at
a cell that cannot get the raw material. mTORC1 is where the raw material is counted.**

### The corollary, which is the answer to the question you actually asked

If the ceiling is a sensor reading a supply that is structurally unavailable, then unbounded growth
does not require a new gene. **It requires convincing the sensor that supply is unlimited — without
saturating it.** And that decomposes into exactly the four things the last five rounds found
independently:

1. **Perfuse the tissue** so the supply is real — F-R005 Rung 3, the antler's receptor-level recipe
   (VEGFA→KDR on, BMP→BMPR / VEGFA→FLT1 / PDGF→PDGFRB off).
2. **Supply the substrate** the sensor counts — leucine for the sensor itself; cysteine and selenium
   for the redox tax that limits what the cell can do with it (F-R005 §2).
3. **Pulse the sensor, do not delete its brake** — CORR-300 (setpoint, not brake), R366 (*pulse beats
   sustained*). `yan2016` is what brake-deletion does; NV-5138's 3-hour half-life is what pulsing
   looks like.
4. **Give the extra output somewhere to go** — F-R006's second exit. `yan2016`'s own blots show
   **MMP-13 and OPN DOWN** in the mutant with a **44% taller hypertrophic zone**: charge accumulating
   against a blocked discharge. That is failure mode #1 with the molecular block finally named.

**Steps 1–3 raise the charge. Step 4 is why the charge has never become length.**

---

## 3. `yan2016` re-read: the negative is a dying-animal artefact plus a named discharge block

The supplementary you sent settles the confound question. `yan2016` Supp. Fig. legends record, at
**4 weeks**: *"X-ray imaging of TSC1CKO mice"*, *"**Thoracic volume and Lung weight** of control mice
and TSC1CKO mice at 4 weeks."* And Figure 6a: **every TSC1CKO mouse is dead by ~12 weeks; rapamycin
from 3 weeks gives 100% survival to 20+ weeks.**

**Measuring thoracic volume and lung weight means the animals were dying of restrictive respiratory
failure from a small rib cage** — ribs are Col2⁺, so they carry the deletion. Add `newton2018`'s
independent finding of **Col2-Cre activity in the brain, with seizures and chronic wasting.**

> **Every whole-body length in `yan2016` was measured at 4–5 weeks in an animal dying of a small chest
> and brain lesions. The confound can only shorten a bone, never lengthen one.**

**And Figure 6e gives the discharge block directly.** Zone heights: **proliferative zone flox/flox
≈255 vs CKO ≈250 — unchanged.** **Hypertrophic zone flox/flox ≈310 vs CKO ≈445 — +44%.** Figure 6g:
**MMP-13 and OPN reduced** in the CKO. MMP-13 is the collagenase that clears the hypertrophic matrix
at the chondro-osseous junction — **it is the discharge enzyme.**

> **A 44% taller hypertrophic zone with the discharge enzyme down, in a shorter bone. That is charge
> without discharge, measured, with the block named.** ⚠ Whether MMP-13 loss is cause or consequence
> of the differentiation block is not resolved by a blot, and I am not asserting it.

**Rapamycin collapses everything** — PZ 255→120, HZ 310→198 in the control too — which is the mirror
of the Raptor caliper result and completes the sign.

---

## 4. ⭐ The permanent search fix you asked for

`frontier/screens/litsearch.py`. Europe PMC and PubMed are **biomedical** indexes and systematically
under-cover animal science, livestock nutrition, veterinary, feed science, sports nutrition, and grey
literature — which is where a leucine-or-HMB-with-a-bone-length result would live.

| source | coverage | key | status |
|---|---|---|---|
| **OpenAlex** | **250M+ works, every discipline**, boolean + filters, reconstructed abstracts | none | **working** (rate-limited through this proxy; backoff added) |
| **Crossref** | 150M+ DOIs, publisher metadata, journal-scoped sweeps | none | **working** |
| **Semantic Scholar** | abstracts + citation graph | none | working, rate-limited |
| Europe PMC (`epmc.py`) | biomedical only | none | already in use |

**First run already returns things Europe PMC does not:** a **bioRxiv pig study on maternal HMB
supplementation and offspring bone mechanical and geometrical properties with immunolocalisation of
VEGF, TIMP2, MMP13 and BMP2 in bone and cartilage** (doi 10.1101/2020.10.01.322016), and the
`figueiredo2020` counter-paper in §1. **HMB with a skeletal endpoint in a livestock species exists,
and `HMB` returns 0 files in this atlas.** Not yet worked — it is the next round.

---

## 5. The experiment, now cheaper than it has ever been

The `newton2015` / `newton2018` **ex vivo metatarsal / bone organ culture** assay has produced **two
independent positives already**. It needs no mouse line, no tamoxifen, no genetics, and reads out in
**5 days**. Run it on **wild-type** bone, five arms:

| arm | why |
|---|---|
| vehicle | — |
| **IGF-1 100 ng/ml** | the benchmark `newton2015` matched — internal positive control |
| **chloroquine 30 µM** | reproduce the accessible agent |
| **leucine** | the physiological Sestrin2 ligand — the CORR-300-compliant, ligand-level input |
| **NV-5138** | the first-in-class human-dosed selective mTORC1 activator |

Read: **bone length daily**, terminal hypertrophic cell height, COL10A1⁺ zone height, BrdU. **If a
ligand-level, pulsable input reproduces any fraction of the chloroquine effect in wild-type bone, that
is the result this file has been looking for since R199** — and unlike everything else in the stack,
its mechanism raises h_term while *lowering* the division cost.

**And the in-vivo re-measurement stands unchanged from F-R008:** `Col2-CreERT × Tsc1^fl/fl`,
tamoxifen P3, **hold to P90, digital calipers on tibia and femur** — the identical protocol
`newton2019` already ran on the Raptor mice.

⛔ **Nothing here is a recommendation to take chloroquine, hydroxychloroquine, leucine or anything
else.** These are ex-vivo organ cultures at fixed bath concentrations, in mouse bone, with no
vasculature, no load and no systemic exposure. Chloroquine's own toxicology — retinopathy,
cardiomyopathy, QT — is dose- and duration-dependent and entirely unaddressed by any of this. And the
mTORC1 direction is chondrocyte-specific and **opposite** to what the same drugs do elsewhere.

---

## 6. What I need next

1. ⭐⭐ **`newton2015` Figure 1A and 1B, the actual growth curves** — the vehicle value is not in the
   text and I cannot compute a percentage without it. **Panel A/B numbers, or the source data, are
   the single most important missing figure in this project.**
2. ⭐ **`yan2016` Figure 6e source values** — I read PZ ≈255/250 and HZ ≈310/445 off the bar chart you
   sent; I want the numbers, and the Fig. 6g blot densitometry for MMP-13 and OPN.
3. ⭐ **The HMB / leucine livestock series** — Tomaszewska et al. (Lublin) ran a programme on maternal
   HMB and offspring skeletal development in pigs. **doi 10.1101/2020.10.01.322016** is one; the
   journal versions and any with a **bone LENGTH** rather than density/geometry endpoint are what I
   want. This is exactly the corpus §4 was built for.
4. **CNGB — here is the working link.** `https://db.cngb.org/search/project/CNP0003724/` redirects to
   **`https://db.cngb.org/data_resources/project/CNP0003724/`** and returns **HTTP 200**, but it is a
   JavaScript application: the page shell loads, the data API returns **502** from here, and the FTP
   paths (`ftp.cngb.org/pub/CNSA/data1-6/CNP0003724/`) all 404. **Open that URL in a browser and I
   need one of: (a) the per-layer average-expression table for the five AGC layers (RM, PC, TZ, CA,
   MC), or (b) the processed Seurat/h5ad object, or (c) failing both, just tell me the expression of
   ~40 genes I will list — SLC7A11, CBS, GPX4, PPP and glutathione genes, MTOR/RPTOR/RHEB/SESN2,
   GLI1/2/3, MMP13, and the vascular set — across those five layers.** That single table tests the
   redox model *and* this mTORC1 model against the animal that runs at 365×.
