# WHAT THIS ATLAS ACTUALLY NEEDS — audited 2026-08-13, not guessed

Computed from all 459 gaps rather than recalled. Re-run:
`python3 - <<'EOF'` … the classifier in the round-326 turn, or just read the counts below.

## The blocker distribution across 459 gaps

| what is missing | gaps |
|---|---|
| a measurement on **this subject** | 155 |
| a **delivery / formulation** solution | 81 |
| **a caliper on a growing animal** (a length endpoint) | 51 |
| a **dose / titration** answer | 39 |
| a **dataset** | 36 |
| **human tissue** we do not have | 27 |
| **a molecule that does not exist** | 17 |
| a **paywalled paper** | 9 |

Notebooks written: **7**. Datasets registered in `atlas/quant/dataset_inventory.csv`: **72**.

## The honest headline

**Every target that has survived scrutiny in rounds 312–326 has died on one of three things, and not one
of them is a dataset:**

1. **No length endpoint in a normal growing animal** — HHIP, CHAD, SCUBE3, NRK, TET1, LOXL2, tankyrase,
   sulfate donors, the TGF-β axis, PTP-MEG2 and trodusquemine. Every single one.
2. **No molecule, or the wrong modality** — HHIP (no agent in any species), CHAD (mimetics run backwards),
   NRK (Tdark, and its function is kinase-independent so the druggable domain is the wrong one),
   SCUBE3 (no recombinant product).
3. **Delivery into avascular cartilage** — R315, and it is only lifted for the perichondrial TGF-β axis
   because that axis acts outside the plate.

**So the binding constraint has moved from information to wet-lab capacity.** The atlas is now very good at
triage and has essentially exhausted what triage can decide. Fifty-one gaps say, in different words, *put
a caliper on a mouse.*

## TIER 0 — the cheapest high-value experiment in the file, and it is a mouse order

**`Nrk^tm1Mkom`** — MGI:5292104 / 5292105 / 5292106, B6.129S4 congenic, `denda2011`. Already phenotyped as
hemizygous male, homozygous female and heterozygous female — the three genotypes an X-linked gene needs.
Seven MP terms, **all placental/reproductive, not one skeletal.** IMPC has **zero** Nrk rows in 2,236,257.
NRK has the best human genetics in this atlas (35 monotone burden rows, best P = 6.4e-29).
→ **Order the line, breed to skeletal maturity, micro-CT and caliper the femur, tibia and vertebrae.**
No new model, no new chemistry, no dose-finding.

## TIER 1 — animal phenotyping capacity (the real answer)

A CRO or academic collaborator that runs: *wild-type C57BL/6, weaning to skeletal maturity, terminal femur
/ tibia / vertebral body length + growth-plate histomorphometry + zone heights.* That one capability closes
51 gaps. Ready-to-run studies, in ascending cost:

1. **Re-measure `chen2015`.** Losartan was already given to wild-type mice, the post-proliferative zone
   expanded, and the femur was never measured. Published protocol, published dose.
2. **Trodusquemine in growing wild-type mice**, dose inside its published human window; read phospho-IGF1R
   and phospho-AKT S473 in the plate alongside length.
3. **Tamoxifen-inducible `Hhip1` deletion in a juvenile.** The floxed allele exists (`haraguchi2025`).
   Read maturation timing, epiphyseal fusion status AND terminal length.
4. **A TGF-β-lowering agent in a normal growing animal** — vertebral length is not optional here, because
   `baffi2004` and `alkhatib2018` predict the cost lands on the axial skeleton.
5. **Graded sulfate donor in a growing rodent**, ³⁵S incorporation into cartilage proteoglycan + caliper.

## TIER 2 — data I cannot reach

- **Individual-level biobank access with exomes + standing AND sitting height** (UK Biobank approved
  researcher, or equivalent). Would answer: is NRK's +2.79 cm hemizygous-male or heterozygous-female;
  sex-stratified burden; and let the atlas run its own burden tests instead of reading someone's
  supplementary table.
- **A height GWAS that includes chrX.** `bartell2026` has **zero chrX rows in 11.2M variants**, so the
  entire R318/R323 compartment framework is blind to X — and the lead gene is X-linked.
- **`kosmicki2026`'s methods and X-chromosome handling**, plus a sex-stratified NRK row.
- **The AIMS trial's serial height data** (`mullen2019`) — 192 participants, ages 6–40, median 18,
  placebo-controlled, five years, annual BSA-adjusted Z scores so annual height must exist. Never analysed
  for growth. One email to the trials unit.
- **`PXD055563`'s supplementary phosphosite table** — the deposit holds only raw spectra plus an
  identification-mode mzTab with no quantification.

## TIER 3 — measurements on him that are NOT blood

- **BoneXpert on an existing left-hand film.** Zero extra radiation, zero visits. Returns Greulich-Pyle +
  Tanner-Whitehouse-3 + Bone Health Index. SETTLED since R282; method spread in `plluaas2026` was 0.5 y =
  2.2 cm of predicted adult height.
- **A spine film or MRI read for vertebral ring apophysis stage, endplate physis status and individual disc
  heights.** R317/R318/R319 are population priors until this exists — it is the axial equivalent of
  BoneXpert, and his residual is trunk-dominant.

## TIER 4 — chemistry that has to be made

- **A function-blocking anti-HHIP single-domain antibody.** Epitopes mapped (`griffiths2021`), protein
  already manufactured as an Fc fusion (`ye2025`), binders commercial but non-neutralising. ~15 kDa sits
  inside the size class already shown to cross full-thickness cartilage.
- **An antagonist of the CHAD–α2β1 interaction.** Motif known to eight residues (LRRWLEAK318).
- **Resynthesis of `zhang2012meg2`'s compound 7** — Ki 34 nM, selective, cell permeable, in vivo active,
  and no supplier anywhere.

## What has been checked and is NOT the answer

- More literature searching. R298 established that 202/298 atlas targets have no drug because the plate is
  transcription factors, secreted modulators, matrix and channels while the pharmacopoeia is kinases, GPCRs
  and nuclear receptors. R326 reproduced it on the best-anchored axis: 36 of 41 PI3K-AKT nodes have no
  agent in the wanted direction.
- More expression datasets. GSE9160, GSE288028, GSE114919, GSE252288/9, GSE225878 and chu2026 already
  answer "is it in the tissue" as a lookup.
- **`GSE18338` cannot carry the period question.** Checked 2026-08-13: it is **ONE female patient**, six
  arrays, three stages × two replicates, and the replicates are technical. n=1, wrong sex.
