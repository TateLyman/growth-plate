# DOMAIN 18 — CELL-INTRINSIC CAPACITY LIMITS
## Translation, RNA processing, genome maintenance, organelles and secretory throughput

R436 full-concept-space enumeration. **Every row was obtained by EXTERNAL search** (Europe PMC REST API,
NCBI eutils). Nothing was taken from the atlas. Species is stated for every experimental claim. Reviews are
used as an INDEX and flagged as such. Where I could not verify a specific number or PMID I have written
`UNVERIFIED` rather than guess.

**Reading key.**
- `HEIGHT DIRECTION` — `loss→SHORT` is the overwhelming default across this whole domain and is *not*
  interesting on its own. The valuable rows are `loss→TALL/OVERGROWTH`, and any row where the capacity has
  actually been **RAISED** with a growth or skeletal endpoint.
- `OBSCURE? yes` = essentially absent from the mainstream growth-plate / short-stature literature.
- ⭐ marks rows that carry an actual intervention or an inverted direction.

**Rows: 122 (A17 · B18 · C20 · D19 · E33 · F5 · G10). Marked OBSCURE: 86.**

---

## TABLE

### A. RIBOSOME BIOGENESIS AND THE RIBOSOMOPATHIES

| # | CAPACITY / GENE / DISEASE | WHAT IT LIMITS | HEIGHT DIRECTION | CAN IT BE RAISED? AGENT? | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|
| A1 | **RMRP / cartilage-hair hypoplasia** — RNase MRP RNA | pre-rRNA processing at ITS1; also cell-cycle transcript turnover | **loss→SHORT**, disproportionate short-limbed metaphyseal chondrodysplasia. The canonical "ribosome disease of cartilage" | No agent. HSCT corrects immunodeficiency/anaemia, **not stature** | 42170584 (review, INDEX); 39886981 (human, cell-cycle checkpoint arm); 41517791 (human case) | no |
| A2 | **POP1 / anauxetic dysplasia 2; NEPRO(C3orf17) / anauxetic dysplasia 3** — RNase MRP protein subunits | same complex as RMRP, protein side | **loss→EXTREME SHORT** ("anauxetic" = no growth; among the most severe human dwarfisms) | none | 41888142 (2026, human RNase MRP structure; identifies NEPRO/C18orf21 as bona fide subunits) | **yes** |
| A3 | **RPL13 / spondyloepimetaphyseal dysplasia** | 60S large-subunit assembly | **missense/splice→SEVERE SHORT** with SEMD and **no anaemia** — a ribosomal protein whose human phenotype is purely skeletal | none | 31630789 (human, 4 unrelated probands, AJHG) | **yes** |
| A4 | **ERI1** — 3′→5′ exoribonuclease, 5.8S rRNA 3′-end trimming | rRNA maturation + histone-mRNA turnover | ⭐ **missense→SEVERE SHORT (SEMD); biallelic NULL→NOT skeletal** (mild ID + digital anomalies). A phenotypic dichotomy in which loss-of-function is *milder* than missense — so this is **not** a simple dosage/capacity effect | none | 37352860 (human, 8 individuals / 7 families, AJHG) | **yes** |
| A5 | **RPS/RPL genes — Diamond-Blackfan anaemia (RPS19, RPL5, RPL11, RPS26…)** | 40S/60S assembly; nucleolar stress→p53 | **loss→SHORT** (short stature is a recognised DBA feature, partly steroid- and transfusion-confounded) | Corticosteroids treat the anaemia and **cost** height. ⚠ **L-leucine as a translation-raising therapy in DBA is often cited but I could NOT verify a trial with a growth endpoint** — see gaps | 33076379 (review, INDEX); 32932838 ("Ribosomopathies: new therapeutic perspectives", INDEX); 38697731 (2024 DBA international consensus statement, INDEX) | no |
| A6 | **SBDS / EFL1 / DNAJC21 / SRP54 — Shwachman-Diamond and SDS-like** | 60S maturation: eIF6 release from the 60S joining face | **loss→SHORT + metaphyseal chondrodysplasia**; growth failure is a defining feature and persists after marrow transplant | none for stature | 20301722 (GeneReviews, INDEX); 37226705, 36542827 (reviews, INDEX); 29914977 (SRP54, human) | no |
| A7 | **TCOF1 / treacle — Treacher Collins** | rDNA transcription and pre-rRNA methylation, specifically in neural crest | **loss→craniofacial hypoplasia; stature near-normal.** A *regional*, not systemic, capacity defect — important negative | p53 inhibition rescues in mouse; no human agent | 41010008 (2025); 35881792 (mouse, rRNA transcription requirement in development) | no |
| A8 | **POLR1A / acrofacial dysostosis Cincinnati type; POLR1C, POLR1D / TCS 2-3** | RNA Pol I → 47S pre-rRNA | **loss→craniofacial AND limb anomalies**; p53-dependent cell death in zebrafish | none | 25913037 (human + zebrafish, AJHG); 35422389 (Pol I/III review, INDEX) | no |
| A9 | **POLR3A / POLR3B — 4H leukodystrophy** | RNA Pol III → 5S rRNA **and all tRNAs**, i.e. the tRNA supply ceiling | **loss→SHORT STATURE**, with hypodontia and hypogonadotropic hypogonadism (growth failure is part of the syndrome) | none | 35422389 (review, INDEX) | **yes** |
| A10 | **DKC1 / NOP10 / NHP2 / dyskerin** | H/ACA RNP: rRNA pseudouridylation **and** telomerase RNA stability — a dual ribosome/telomere gene | **loss→SHORT** (dyskeratosis congenita, Hoyeraal-Hreidarsson: severe IUGR and growth failure) | none for stature | 42256974 (human DKC1 case); 41868676 (dyskerin review, INDEX) | no |
| A11 | **RPSA — isolated congenital asplenia** | 40S ribosomal protein | ⭐ **loss→asplenia with NO growth phenotype.** Not every RP haploinsufficiency costs height — the tissue-specificity is the whole puzzle | n/a | 31630789 (cited as contrast in the RPL13 paper) | **yes** |
| A12 | **Nucleolar stress → p53 (RPL5-RPL11-5S RNP → MDM2)** | the *sensor* converting a ribosome-assembly shortfall into growth arrest/apoptosis | ⭐ Removing p53 rescues several ribosomopathy models — so the growth loss is a **checkpoint decision, not a raw protein-synthesis shortfall.** This reframes the whole class | p53 inhibition (pifithrin; mouse only); MDM2 modulation | 41777667 (nucleolus/MYC/p53 review, INDEX); 32527837 (RNA exosome → ribosome biogenesis → p53) | no |
| A13 | **rDNA copy number and nucleolar size as a scaling variable** | how much rRNA a cell *can* make | Untested for stature in any species | n/a | 40366093 (nucleolus in development/stem cells, review, INDEX) | **yes** |
| A14 | **SNORA33 / snoRNA-guided rRNA pseudouridylation in chondrocytes** | ribosome *heterogeneity*, not amount | Direction unknown; shown to change in **human chondrocytes** exposed to OA synovial fluid | none | 37628759 (human chondrocytes) | **yes** |
| A15 | **Ribosome heterogeneity / "specialised ribosomes" in musculoskeletal tissue** | which mRNAs get translated rather than how many | no stature direction yet | none | 41743109 (review, INDEX) | **yes** |
| A16 | ⭐ **SOX9 sets translational capacity in chondroprogenitors** | SOX9 regulates ribosome biogenesis factors and ribosomal-protein genes in an immediate-early phase; knockdown lowers polysomes and total translation, **and SOX9 OVEREXPRESSION RAISES THEM** | The master chondrocyte TF is also the *ribosome* TF. Authors propose this prepares the cell for the proliferative burst and matrix output of the growth plate | ⭐ The only demonstration in cartilage that translational capacity can be pushed **up** — in vitro (ATDC5 cells), no length endpoint | 34235151 (mouse ATDC5 cells) | **yes** |
| A17 | **HDAC4 overexpression upregulates the ribosome pathway in chondrocytes** | transcriptional route into ribosome content | improves chondrocyte survival/biofunction (in vitro) | HDAC inhibitors run the *other* way | 37414410 (chondrocytes, RNA-seq) | **yes** |

### B. TRANSLATION INITIATION, ELONGATION, AND THE STRESS RESPONSES

| # | CAPACITY / GENE / DISEASE | WHAT IT LIMITS | HEIGHT DIRECTION | CAN IT BE RAISED? AGENT? | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|
| B1 | ⭐⭐ **mTORC1 → 4E-BP1/2 → SOX9 translation** | cap-dependent translation of *Sox9* mRNA (5′TOP-like motif) in limb mesenchyme | Raptor loss → **marked loss of cartilage and bone**. **Knocking down 4E-BP1/2 — i.e. RAISING translational output — RESCUED the condensation defect**, and a Sox9 transgene rescued skeletal growth | ⭐ The clearest "raise translation → rescue skeletal growth" result in cartilage. Agent: none clinical; genetic in mouse | 30008325 (mouse, Stem Cell Reports) | no |
| B2 | **mTORC1 → S6K1 → Gli2 → PTHrP** | couples cell growth to differentiation timing | ⚠ **mTORC1 HYPERACTIVATION (Tsc1 deletion in chondrocytes) → CHONDRODYSPLASIA**, uncoupled proliferation/differentiation; rapamycin rescued. **More capacity is NOT more bone** — a band, not an arrow | rapamycin (rescues the excess, not a growth agent) | 27039827 (mouse, Nat Commun) | no |
| B3 | **Mechanical activation of mTOR in cartilage** | load→translation coupling | required for cartilage development (mouse) | n/a | 25002119 (mouse) | **yes** |
| B4 | **EIF2AK3 / PERK — Wolcott-Rallison syndrome** | eIF2α kinase, ER-stress arm of the integrated stress response | **loss→SHORT + SPONDYLOEPIPHYSEAL DYSPLASIA + osteopenia/fractures + neonatal diabetes.** A human proof that ISR machinery is skeletally load-bearing | none | 22672868, 24032041 (human cases explicitly listing SED + growth retardation); 34864759 (growth in monogenic neonatal diabetes, INDEX) | no |
| B5 | **EIF2AK4 / GCN2** — amino-acid-sensing ISR kinase | translational response to amino-acid scarcity | Human biallelic disease is **pulmonary veno-occlusive disease, not stature** — a negative worth recording | GCN2 inhibitors and activators exist (oncology) | UNVERIFIED for any stature endpoint | **yes** |
| B6 | **EIF2AK1 / HRI, EIF2AK2 / PKR** | haem- and dsRNA-sensing ISR arms | PKR participates in IL-1α responses in **cartilage** — the only chondrocyte ISR datum found | none | 17850766 (cartilage, PKR requirement) | **yes** |
| B7 | **ATF4 / CHOP / GADD34 — ISR effectors** | amino-acid transport, collagen synthesis, and the terminal arrest/death decision | Atf4-null mice are small with delayed ossification (widely stated; **the systemic primary was not retrieved here**). ✓ What I did verify: **chondrocytic Atf4 regulates skeletal development via Ihh** — so the ISR effector sits directly on the growth-plate morphogen the atlas already works | none | 22190639 (mouse, chondrocyte-specific Atf4→Ihh); systemic Atf4-null primary UNVERIFIED | no |
| B8 | ⭐ **ISRIB / eIF2B activators** | restores translation initiation when eIF2α is phosphorylated — a **capacity-restoring drug that exists** | **NO bone-length endpoint in any species.** The whole ISRIB literature is neuro, immuno and oncology | ISRIB, 2BAct — obtainable research compounds | negative search result: Europe PMC "ISRIB bone growth" returns no skeletal length paper | **yes** |
| B9 | ⭐ **DHPS / DOHH — eIF5A hypusination** | translation *elongation* through polyproline tracts — **and collagen is the most proline-rich protein in the body** | **loss→developmental disorder** (DHPS deficiency syndrome; DOHH-related encephalopathy with hypoparathyroidism, cardiomyopathy). Stature direction not cleanly separated from the syndrome | Spermidine is the hypusine substrate — an obtainable capacity donor. Gene-therapy strategy in preprint | 37333770 (human + mouse); 40883692 (DOHH review + case); 42327909 (DOHH case); 41410504 (polyaminopathies review, INDEX); PPR1234268 (gene therapy, PREPRINT) | **yes** |
| B10 | ⭐ **Cytoplasmic aminoacyl-tRNA synthetases: AARS1, IARS1, LARS1, KARS1, VARS1, SARS1, QARS1, MARS1, RARS1, YARS1, WARS1** | charged-tRNA supply = the raw substrate of elongation | Multiple biallelic ARS1 deficiencies include **growth failure / short stature** in the syndrome definition (LARS1 = infantile liver failure syndrome 1, with growth failure) | ⭐⭐ **AMINO-ACID SUPPLEMENTATION IS AN ACTUAL CLINICAL INTERVENTION IN THIS CLASS** — a genuine capacity-raising therapy | 36330207 (aaRS in health/disease, INDEX); 37274208 (in vivo models, INDEX); 38844943, 38807157 (LARS1 human/zebrafish); 41404429 (tyrosine supplementation in YARS2 disease, human case reports) | **yes** |
| B11 | **Mitochondrial aminoacyl-tRNA synthetases: AARS2, IARS2, EARS2, RARS2, YARS2** | mitochondrial translation | **loss→SHORT** in several (IARS2 phenotypes include growth failure and skeletal dysplasia) | tyrosine supplementation reported for YARS2 | 39062673 (IARS review, INDEX); 39169373, 36704128 (human IARS2 cases); 41404429 | **yes** |
| B12 | ⭐⭐ **METTL1 / WDR4 — tRNA N7-methylguanosine (m7G) modification; primordial dwarfism** | tRNA stability and decoding capacity | **loss→PRIMORDIAL DWARFISM in humans.** In mouse, conditional Mettl1 deletion or a Wdr4 missense knock-in **severely impaired endochondral bone formation and bone-mass accrual** | ⭐⭐ **α-KETOGLUTARATE SUPPLEMENTATION AMELIORATED THE SKELETAL DEFECT of Mettl1-deficient mice.** Mechanism: m7G loss → less Rho-GTPase translation → BCAT1 up → intracellular αKG restricted. Targeting ISR or mTORC1 made it *worse* | 39255038 (mouse + human, J Clin Invest 2024); 39471230 (PNAS 2024, mechanism + intervention) | **yes** |
| B13 | **Other tRNA modification enzymes: NSUN2, ELP1/ELP3, CTU1/CTU2, TRMT10A, ADAT3, TRIT1, PUS3, PUS7, ALKBH8** | wobble/anticodon modification → elongation speed and fidelity | several syndromes include short stature or growth failure (TRMT10A: microcephaly, short stature, diabetes) | none | 38943267 (tRNA methylation disorders, review, INDEX); 41965784 (INDEX) | **yes** |
| B14 | **EEF1A2, EEF2, EEF2K** | elongation rate | **EEF2K is the BRAKE on elongation, so inhibiting it RAISES elongation** — the rare "raise capacity by inhibiting something" configuration | eEF2K inhibitors exist (research) | no skeletal primary found | **yes** |
| B15 | ⭐ **SECISBP2 — selenoprotein synthesis defect** | UGA→selenocysteine recoding; makes all 25 selenoproteins including the deiodinases | **loss→SHORT STATURE** + abnormal thyroid metabolism (high fT4, low T3). A *translation* defect that presents as an endocrine one | Selenium supplementation tried; corrects some selenoproteins | 41311234, 40918659 (human cases); 38963712 (2024 European Thyroid Association guideline, INDEX) | **yes** |
| B16 | **SEPSECS, EEFSEC, PSTK — selenocysteine machinery** | same pathway, other steps | SEPSECS→pontocerebellar hypoplasia 2D; **EEFSEC deficiency = early-onset neurodegeneration** | none | 39753114 (human, EEFSEC); 41719757 (selenoprotein genetics review, INDEX) | **yes** |
| B17 | ⭐ **GPX4 — Sedaghatian spondylometaphyseal dysplasia** | a *selenoprotein* whose loss is a **lethal SPONDYLOMETAPHYSEAL DYSPLASIA** — the most direct link from selenoprotein translation to a growth-plate disease | **loss→severe skeletal dysplasia, perinatally lethal** | Selenium; a **selenium-independent GPX4 variant compensated in mouse** | 34688299 (GPX4 therapy roadmap, INDEX); 34794077 (mouse, Se-independent GPX4 rescue) | **yes** |
| B18 | ⭐ **Codon usage / Gly-tRNA supply as a ceiling on collagen output** | COL2A1 is (Gly-X-Y)n — glycine at every third residue, plus a huge Pro/Hyp load. Gly- and Pro-tRNA demand in a hypertrophic chondrocyte is arguably the most extreme in the body | **Conceptually the sharpest capacity argument in this domain and NOBODY HAS TESTED IT** | tRNA therapeutics are now a real modality (engineered/supplemented tRNAs) | no primary found linking codon usage to collagen output; modality: 38801719, 37703991 (tRNA medicines, reviews, INDEX) | **yes** |

### C. RNA PROCESSING, SPLICING, DECAY AND SURVEILLANCE

| # | CAPACITY / GENE / DISEASE | WHAT IT LIMITS | HEIGHT DIRECTION | CAN IT BE RAISED? AGENT? | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|
| C1 | **RNU4ATAC — MOPD1 / Roifman / Lowry-Wood** | the **minor (U12) spliceosome** — a non-coding snRNA serving ~700–800 minor-intron genes | **loss→MICROCEPHALIC OSTEODYSPLASTIC PRIMORDIAL DWARFISM**, one of the most severe growth-failure phenotypes known | none | 42322193 (large cohort, human); 41808109 (phenotypic spectrum); 39761998 (genotype-phenotype, INDEX) | no |
| C2 | **RNU6ATAC** | minor spliceosome, U6atac snRNA | **NEW 2026: biallelic variants → minor spliceopathy with transcriptome-wide minor-intron retention, multisystem** | none | 41808409 (human) | **yes** |
| C3 | ⭐ **Minor-intron retention as a graded, measurable capacity read-out** | a transcriptome-wide outlier signature identifies minor-spliceopathy patients | Establishes that spliceosome capacity is a *continuous, measurable* variable, not a binary | n/a | 40975062 (human) | **yes** |
| C4 | **SF3B4 — Nager acrofacial dysostosis** | U2 snRNP branch-point recognition | **loss→craniofacial + LIMB (radial ray) anomalies**; neural-crest survival requirement; **downstream mitochondrial dysfunction** in zebrafish | none | 40047147 (human iPSC/NCC model); 40126363, 38508476 (zebrafish); 41667381 (2026 integrated models) | no |
| C5 | **EFTUD2 — mandibulofacial dysostosis with microcephaly** | U5 snRNP GTPase (tri-snRNP recycling) | **loss→craniofacial + microcephaly + growth restriction** | none | 40983222, 41147426 (human) | no |
| C6 | **SNRPB — cerebrocostomandibular syndrome** | Sm core protein; autoregulated by a poison exon | loss→rib gaps, micrognathia; neural-crest-restricted requirement in mouse | none | 35593225 (mouse); 41727730 (human case) | **yes** |
| C7 | **TXNL4A — Burn-McKeown syndrome** | U5 snRNP (Dib1) | loss→craniofacial. **The promoter-deletion allele makes this a pure DOSAGE/capacity disease** | none | 34713892, 32187816 (human); 32735620 (iPSC model) | **yes** |
| C8 | **Tissue specificity of core-spliceosome disease** | why a *ubiquitous* machine gives a *regional* phenotype — the same question the growth plate poses for every housekeeping gene | n/a | n/a | 40264708 (U5 spliceosomopathies review, INDEX); 35893124 (EFTUD2/SNRPB/TXNL4A all essential for neural crest); 41081049 (modelling craniofacial spliceosomopathies, INDEX) | **yes** |
| C9 | **RNU4-2 / ReNU syndrome** | major spliceosome U4 snRNA; one of the commonest monogenic NDDs, described 2024 | growth direction **UNVERIFIED here** | none | UNVERIFIED | **yes** |
| C10 | **RNA exosome: EXOSC1/2/3/5/8/9, DIS3** | nuclear 3′→5′ RNA surveillance; also feeds rRNA processing | **EXOSC5 biallelic → SHORT STATURE, cerebellar hypoplasia, developmental delay.** Exosome mutations alter ribosome biogenesis and **raise p53** | none | 32504085 (human, EXOSC5 + short stature); 32527837 (mechanism); 42275096 (2026 review, INDEX) | **yes** |
| C11 | ⭐⭐ **DIS3L2 — Perlman syndrome** | cytoplasmic 3′→5′ exoribonuclease; degrades uridylated RNA including **pre-let-7** | ⭐⭐ **loss→OVERGROWTH.** Perlman = fetal macrosomia, nephromegaly, Wilms tumour. **An RNA-DEGRADATION capacity defect that makes you BIGGER** — the single clearest inversion in this domain | Therapeutic direction would be to INHIBIT DIS3L2; no agent, and it is a tumour-predisposition gene | 42040973 (human case, 2026); 30068702 (overgrowth/IGF2 review, INDEX); 40500755 (Dis3l2→Akt, neural crest); PPR98410 (Drosophila, PI3K-dependent) | **yes** |
| C12 | ⭐ **NMD: UPF3B, UPF2, SMG9, SMG8, PAN2** | clearance of premature-termination-codon transcripts — this sets the penetrance of *every* nonsense allele in the genome | SMG9→heart-and-brain malformation with growth restriction; PAN2 biallelic→syndromic NDD with multiple congenital anomalies | NMD *inhibitors* exist (readthrough field) — direction would need care | 35304602 (PAN2, human) | **yes** |
| C13 | ⭐⭐ **NMD as the SWITCH between TALL and SHORT in one gene — NFIX** | **NFIX deletions/nonsense alleles that TRIGGER NMD → Sotos-like OVERGROWTH with ADVANCED bone age (Malan syndrome). Alleles that ESCAPE NMD → Marshall-Smith syndrome.** Same gene, opposite growth phenotype, decided by decay capacity | ⭐⭐ **A capacity pathway that determines the SIGN of a growth phenotype** | n/a — but it means NMD modulation is directionally consequential | 20673863 (human, AJHG); 42038232, 29897170 (Malan syndrome, human); 29184170 (reciprocal 19p13 duplication → **short** stature) | **yes** |
| C14 | **Poison exons / alternative-splicing-triggered decay as a self-capping circuit** | spliceosome components autoregulate by including a poison exon, so the machine caps itself | Conceptual; explains why heterozygous dosage matters at all | Splice-switching ASOs can raise the productive isoform | 37161864, 41678398 | **yes** |
| C15 | **PABPN1 (OPMD) and polyadenylation capacity** | poly(A) length, mRNA stability | Adult muscle disease; **no stature link found** — a negative | none | negative result | **yes** |
| C16 | **RNA export: GLE1, NXF1, NUP-opathies** | mRNA egress from the nucleus | GLE1→lethal congenital contracture syndrome (skeletal, but via motor neuron) | none | UNVERIFIED for a chondrocyte mechanism | **yes** |
| C17 | ⭐ **Stress granules / P-bodies (G3BP1, TIA1, DDX3X)** | reversible translational shutdown — **and stress-granule assembly ARRESTS SECRETION via the TRAPP complex** | Directly relevant: a matrix-secreting cell that granulates stops exporting. Never studied in a growth plate | none | 31429971 (human cells; TRAPP-mediated secretion arrest) | **yes** |
| C18 | **RNA-binding proteins in cartilage: SERBP1, IGF2BP1/2/3, ELAVL1/HuR, MSI2, LIN28A/B** | stability and translation of growth-plate transcripts | LIN28B is a *bona fide* human height and pubertal-timing locus | LIN28/let-7 chemistry is all inhibitors; no HuR agonist | 38229171 (trans-ancestral pubertal height growth GWAS); 35183440 (genetics of pubertal timing, INDEX); 32745689 (miRNA/cartilage, INDEX) | no |
| C19 | **m6A and other mRNA modifications: METTL3, METTL14, METTL5, FTO, ALKBH5, YTHDF1/2/3** | mRNA stability and translation efficiency; METTL5 modifies 18S rRNA and modulates ribosome assembly | FTO is a major BMI/height-adjacent locus; direction in cartilage unmapped | STM2457 (METTL3i) — inhibitory only | 41487998 (METTL5 review, INDEX) | **yes** |
| C20 | **miR-140 and cartilage microRNAs** | post-transcriptional damping of chondrocyte programmes | A **human gain-of-function miR-140 mutation causes skeletal dysplasia** — a non-coding RNA capacity node | none | 32745689 (review, INDEX) | no |

### D. GENOME MAINTENANCE, REPLICATION AND SEGREGATION CAPACITY

| # | CAPACITY / GENE / DISEASE | WHAT IT LIMITS | HEIGHT DIRECTION | CAN IT BE RAISED? AGENT? | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|
| D1 | ⭐⭐ **Origin licensing: ORC1, ORC4, ORC6, CDT1, CDC6, GMNN, CDC45, MCM5, MCM3, MCM7 — Meier-Gorlin syndrome** | how many replication origins a cell can license per S phase | ⭐ **loss→SHORT.** An entire gene family whose *defining* feature is primordial short stature with normal proportions, microtia and absent patellae. **The purest statement in human genetics that replication capacity sets body size** | The reverse has never been tried. **GMNN/geminin is the licensing INHIBITOR — inhibiting geminin would RAISE licensing.** No agent, and geminin loss is itself a Meier-Gorlin allele (so almost certainly a band) | 37059840 (expanded landscape, human); 41448435 (2026, molecular impact of MGS mutations on human origin licensing); 33477564 (congenital diseases of DNA replication, INDEX); 33654309 (MCM3/MCM7); 35023948 (CDC6); 36012502 (ORC6) | no |
| D2 | **Meier-Gorlin + GH** | — | GH therapy reported in a single MGS1 case with 6-year follow-up; **not an established therapy** | rhGH — anecdotal | 35282325 (human case report); 36635911 (SGA consensus guideline, INDEX) | **yes** |
| D3 | **DONSON, WDHD1, TRAIP, GINS1, MCM4, PRIM1, POLA1, POLE1, POLE2** — replisome | replication-fork assembly and throughput | **loss→MICROCEPHALIC PRIMORDIAL DWARFISM.** POLE1 = FILS syndrome (facial dysmorphism, immunodeficiency, livedo, **short stature**) | none | 37458194 (DONSON, vertebrate); 41962535 (2026, WDHD1 biallelic → MPD, human); 33477564 (INDEX) | **yes** |
| D4 | **ATR, ATRIP, RBBP8/CtIP — Seckel syndrome** | the replication-stress checkpoint | **loss→SEVERE PROPORTIONATE DWARFISM** | ATR inhibitors exist (oncology) — wrong direction | 40029331 (ATRIP deficiency → MPD + immunodeficiency, human); 32994318 (mouse Atrip-Seckel: progenitor death) | no |
| D5 | ⭐ **PCNT — MOPD type II** | pericentriolar matrix; spindle organisation and ATR signalling | **loss→the most extreme non-lethal human dwarfism** (adult height often <100 cm) — and **notably GH-UNRESPONSIVE.** A hard negative for "just add GH" when the defect is cell-intrinsic capacity | none | 33042696 (human case); 39597091 (MOPD II diagnostic case study); 34217350 (targeted exome in syndromic short stature) | no |
| D6 | **Primary microcephaly / centriole set: ASPM, WDR62, MCPH1, CENPJ, CEP152, CEP63, PLK4, RTTN, KIF11, NIN** | centriole duplication → mitotic fidelity → total cell number | **loss→SHORT** (many are microcephalic dwarfisms) | none | 37443841 (review, INDEX: "when centrosome dysfunction dictates brain and body size") | no |
| D7 | **BUB1B, CEP57, TRIP13, MAD2L1BP — mosaic variegated aneuploidy** | spindle assembly checkpoint | **loss→growth retardation, microcephaly, short stature** + cancer. CEP57 case: short stature, microcephaly, brachydactyly, small teeth | none | 35804254 (BUB1B, human); 35434947 (CEP57, human); 37796616 (MAD2L1BP, human) | **yes** |
| D8 | **SMC5 / near-tetraploidy-MVA** | replication-associated recombination | recessive SMC5 → MVA-like phenotype | none | 41374403 (human, 2025) | **yes** |
| D9 | **Cohesinopathies: NIPBL, SMC1A, SMC3, RAD21, HDAC8, BRD4, MAU2, STAG1** | sister-chromatid cohesion **and** enhancer-promoter looping — so partly transcriptional, not purely capacity | **loss→SHORT** (Cornelia de Lange: profound pre- and postnatal growth restriction) | none | 41230206 (17 patients, human); 37962004 (MAU2); 41300558 (BRD4, INDEX); 40677927 (WGS in "mutation-negative" CdLS) | no |
| D10 | **RecQ helicases: BLM (Bloom), RECQL4 (Rothmund-Thomson), RECQL1 (RECON), WRN** | replication-fork restart | **loss→SHORT.** Bloom syndrome is *proportionate severe short stature with no endocrine deficit* — a clean statement that genome-maintenance capacity caps body size independent of hormones | none | 40728512 (RecQ overview, INDEX); 36805074 (RECON syndrome); PPR418073 (BLM vs RMI1, PREPRINT) | no |
| D11 | **Fanconi anaemia pathway (FANCA–FANCW, BRCA2/FANCD1)** | interstrand crosslink repair | **loss→SHORT** (short stature in a majority), radial ray defects. **Small pituitary volume is documented in FA**, so part of it is endocrine — a confound worth naming | ⭐ FA also shows **metabolic inflexibility** (compromised glucose oxidation, enhanced ketogenesis) — a metabolic capacity arm | 39224124 (small pituitary in FA, human); 41313766 (2025, FA metabolic reprogramming) | no |
| D12 | **Transcription-coupled repair: ERCC6/CSB, ERCC8/CSA (Cockayne); ERCC2/ERCC3/GTF2H5 (trichothiodystrophy); XP-CS** | how long RNA Pol II can keep transcribing a damaged template | **loss→CACHECTIC DWARFISM.** Cockayne syndrome is arguably the most severe *postnatal* growth failure of any human disease | none | 28848724, 32173062, 37106549 (human); 31662099 (NER in embryonic development, INDEX); 40332372 (TCR/R-loop, INDEX) | no |
| D13 | **NHEJ: LIG4 syndrome, XRCC4, NHEJ1/Cernunnos, NBN (Nijmegen breakage)** | double-strand-break rejoining | **loss→MICROCEPHALIC PRIMORDIAL DWARFISM** | none | 40114033 (XRCC4-related MPD, clinical series of 7, human) | **yes** |
| D14 | **RNF168 / RIDDLE syndrome** | ubiquitin signalling at double-strand breaks | loss→short stature, immunodeficiency | none | UNVERIFIED (primary not retrieved) | **yes** |
| D15 | ⭐ **Telomere biology disorders: TERT, TERC, RTEL1, TINF2, PARN, NAF1, ACD, CTC1** | replicative lifespan of a progenitor pool — including, in principle, the resting-zone chondrocyte pool | **loss→SHORT** (dyskeratosis congenita; Hoyeraal-Hreidarsson has severe IUGR and growth failure) | ⭐ **DANAZOL RAISES TELOMERE LENGTH IN HUMANS** (androgen→TERT), now with long-term phase 1/2 data. **NO height endpoint has ever been reported.** AAV-TERT extends mouse lifespan; body length UNVERIFIED | 41115243 (2026, danazol long-term phase 1/2 in telomere biology disorders); 41953763 (danazol efficacy/safety); 41035407 (adult TBD management, INDEX); 29696773 (RTEL1 human) | no |
| D16 | **Ribonucleotide reductase and dNTP pools: RRM2B, SAMHD1, TK2, DGUOK, ITPA** | nucleotide supply for nuclear and mtDNA replication | RRM2B→mtDNA depletion with failure to thrive; SAMHD1→Aicardi-Goutières | ⭐ **Nucleoside supplementation (deoxynucleosides) is used in TK2 deficiency** — a capacity-raising substrate therapy in a related pathway | 38421058 (nucleotide metabolism/leukodystrophy, INDEX) | **yes** |
| D17 | **G-quadruplex-driven replication stress as a shared mechanism** | fork stalling at structured DNA; links Bloom, telomere and ICF disorders into one capacity axis | — | G4 stabilisers exist — wrong direction | 41975004 (2026 review, INDEX) | **yes** |
| D18 | **cGAS-STING as the sensor converting genome instability into growth arrest** | the *decision*, not the damage — structurally the same shape as nucleolar stress→p53 | Suggests some genome-instability short stature is a signalling output that could in principle be uncoupled | STING inhibitors (research) | 41980769 (2026 review, INDEX) | **yes** |
| D19 | ⭐ **Replicative senescence of the resting-zone chondrocyte pool** | how many divisions the growth plate has left | The atlas-external framing: growth-plate senescence is division-counted, so *any* genome-maintenance defect that forces extra cycles or arrests them changes final height | — | 41795828 (2026 systematic review of quiescence in the resting zone, INDEX) | no |

### E. ORGANELLES, SECRETORY THROUGHPUT AND METABOLIC CAPACITY

| # | CAPACITY / GENE / DISEASE | WHAT IT LIMITS | HEIGHT DIRECTION | CAN IT BE RAISED? AGENT? | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|
| E1 | ⭐⭐ **MIA3/TANGO1 — procollagen ER exit** | procollagen is ~300 nm and **does not fit a standard 60–80 nm COPII vesicle**; TANGO1 builds the megacarrier. This is the most literal secretory-capacity ceiling in the body | **loss→odontochondrodysplasia (human); TANGO1 loss → ABSENCE of bone mineralisation (mouse); short isoform loss → skeletal patterning defects (zebrafish)** | none | 40119123 (human MIA3 phenotypic spectrum); 33778321 (mouse/zebrafish); 41307135 (2025 zebrafish); 34350936 (general role); 38650832, 38314136 (reviews, INDEX) | **yes** |
| E2 | **COPII cargo selection: SEC24D (Cole-Carpenter/OI-like), SEC23A (cranio-lenticulo-sutural dysplasia), SEC31, SAR1B** | **collagen has a specific SEC24 paralogue preference** — a hard-wired throughput constraint | **loss→skeletal dysplasia with bone fragility.** SEC24D depletion inactivates an ATF6/TGF-β/RUNX2 loop | none | 34761479 (collagen SEC24 preference); 34580982 (SEC23A, human); 40374976 (SEC24D mechanism); 31970693 (COPII in vertebrates, INDEX) | **yes** |
| E3 | ⭐ **TRAPPC2 — X-linked spondyloepiphyseal dysplasia tarda** | TRAPP tethering complex; procollagen trafficking | ⭐ **loss→SHORT with a specifically AXIAL/SHORT-TRUNK phenotype.** A trafficking gene whose human phenotype is the *spine* rather than the limbs | none | 41732158 (2026), 41059451 (human); 39769094 ("TRAPPopathies", INDEX) | **yes** |
| E4 | ⭐ **NBAS — SOPH syndrome / infantile liver failure 2** | Golgi→ER **retrograde** transport (syntaxin-18 complex) | **loss→SHORT STATURE** (the "S" in SOPH), optic atrophy, Pelger-Huët anomaly; also skeletal dysplasia and OI-like presentations | ⭐ **Spermidine recovered the autophagy defects underlying cell-trafficking disorders** (in vitro) — an obtainable compound aimed at this class | 42305553 (2026, human spectrum); 33542026 (NBAS + OI, human); 34149817 (odontochondrodysplasia-like); 38279772 (INDEX); 39838718 (spermidine rescue, cell models) | **yes** |
| E5 | ⭐ **Vesicular trafficking as a whole CLASS of skeletal dysplasia** | >370 genes now linked to cell-transport defects; the review argues trafficking is a major, under-recognised skeletal-dysplasia mechanism | — | — | 41257398 (2025 review, INDEX) | **yes** |
| E6 | **Collagen-specific ER chaperones: SERPINH1/HSP47 (OI type X), FKBP10 (Bruck), CRTAP, P3H1/LEPRE1, PPIB, SIL1** | folding throughput for the most abundant secreted protein in the body | **loss→SHORT + bone fragility.** HSP47 is *collagen-dedicated*, so it is the cleanest chaperone-capacity gene in the skeleton | ⭐ **ARIMOCLOMOL** — an approved (2024, Niemann-Pick C) heat-shock **amplifier**, i.e. a capacity-RAISING drug — has **zero skeletal literature** | 30522930, 36455410, 37516663 (arimoclomol, non-skeletal); 35225118 (collagen misfolding UPR, INDEX) | **yes** |
| E7 | ⭐⭐ **ER stress in chondrocytes as a growth-plate-limiting mechanism (MCDS/COL10A1, PSACH/COMP, MED/MATN3, MGP-SED)** | when a mutant matrix protein jams the ER, output collapses | **loss of throughput→SHORT.** Even **MGP heterozygous missense causes SED via ER stress** rather than via mineralisation | ⭐ **Carbamazepine** (proteostasis/autophagy route) has been given to control and OI mice with bone endpoints; ⭐ **Curcumin reduced ER stress by INCREASING proteolysis of mutant matrilin-3** — both are capacity-raising strategies with skeletal readouts | 32399188 (chondrocyte ER stress, INDEX); 41155349 (2025 PSACH/MED review, INDEX); 36675026 (curcumin/matrilin-3); 35701367 (carbamazepine in control + OI mice); 37923733 (MGP→ER stress→SED, human); 38510140 (Col10a1 medaka) | no |
| E8 | ⭐ **UPR as a THROUGHPUT expander: XBP1s, ATF6, IRE1** | expands ER volume and folding capacity to match secretory load | **XBP1s overexpression is used industrially to raise recombinant-protein output** — proof the ceiling is real and movable *in vitro* | ⭐ **ATF6 activators (AA147, AA263) exist. No bone endpoint in any species** | 41301756 (XBP1 in development/regeneration, INDEX); 41509511 (CHO bioprocessing) | **yes** |
| E9 | ⭐⭐⭐ **Autophagy sets procollagen-II secretion in the growth plate** | Atg7 loss in chondrocytes → **ER storage of procollagen II** and a defective Col2 fibrillar network. Postnatal chondrocyte autophagy is induced by **FGF18 via FGFR4 → JNK → VPS34-beclin-1** | **loss→less matrix, less growth** | ⭐⭐⭐ **THE AGENT IS `TAT-BECLIN1`, a cell-permeable peptide that enhances endogenous Beclin1 activity. It RESCUED autophagy in the growth plates of Fgf18+/− mice and restored the ECM defect in Fgf18+/− and Fgfr4−/− mice IN VIVO.** One of only two genuine capacity-raising *pharmacological* interventions in this whole domain with a growth-plate endpoint. ⚠ Dose/route not stated in the sources I could reach | 26595272 (mouse, Nature 2015); ⭐ **26939858** (the authors' own Cell Cycle commentary "Autophagy gets to the bone", which is where the agent is named) | no |
| E10 | **Lysosome / TFEB / ER-phagy (FAM134B)** | recycling capacity; MiT/TFE factors transcriptionally control ER-phagy | Ties E8 and E9 together — the ER's *disposal* arm | TFEB activators (trehalose) untested on bone length | 32716134 (MiT/TFE→FAM134B) | **yes** |
| E11 | **Lysosomal storage: GNPTAB (mucolipidosis II / I-cell), MPS I–VII** | degradative throughput and GAG turnover | **loss→SEVERE SHORT STATURE** (I-cell, Morquio A, Hurler) | ⭐ **ERT and HSCT partially improve growth in MPS** — a real, measured capacity-restoring therapy with height as an outcome. Effects on **final** height remain limited | 42279040 (2026, longitudinal growth in MPS IVA/IIIA); 40083105 (2025 systematic review, HSCT and growth outcomes in MPS); 41168830 (elosulfase alfa long-term) | no |
| E12 | ⭐ **Peroxisomes: PEX7, GNPAT, AGPS — rhizomelic chondrodysplasia punctata; PEX1 etc. — Zellweger** | plasmalogen synthesis and peroxisomal β-oxidation | ⭐ **loss→RHIZOMELIC (proximal-limb) SHORTENING with epiphyseal stippling** — a metabolic organelle defect with a *specific growth-plate geometry* | Plasmalogen replacement has been developed and trialled | 35070570 (AGPS, human case); 40165314 (2025 RCDP outcome measure, INDEX); 41130295 (plasmalogens as therapeutic targets, INDEX) | **yes** |
| E13 | **Mitochondrial disease as a stature phenotype (mtDNA depletion, MELAS, Kearns-Sayre, Pearson, Barth)** | ATP supply and mitochondrially-derived signals | **loss→SHORT.** Short stature is among the commonest endocrine/growth findings in primary mitochondrial disease | none for stature | 39891580 (endocrine dysfunction in primary mitochondrial disease, INDEX); 41501912 (2026 paediatric cohort) | no |
| E14 | **Mitochondrial ribosome: MRPS2, MRPS22, MRPL genes** | mitochondrial translation of the 13 OXPHOS subunits | **loss→multisystem disease with growth failure** | none | 29576219 (MRPS2, human); 33426504 (mitochondrial translation defects, INDEX) | **yes** |
| E15 | **Mitochondrial dysfunction → mTORC1 → skeletal ageing** | links OXPHOS state to the growth-signalling hub in bone | mouse | rapamycin (wrong direction) | 40249823 (mouse, 2025) | **yes** |
| E16 | **Glycolysis vs OXPHOS by growth-plate zone; HIF-1α in the avascular plate** | which capacity is limiting *where*: the resting/proliferative zone is hypoxic and glycolytic | HIF-1α controls chondrocyte proliferation/differentiation (cranial base synchondrosis, mouse) | HIF-PHIs raise HIF — no length endpoint | 40854917 (mouse cranial base); 39044709 (cartilage oxygen homeostasis, INDEX) | no |
| E17 | ⭐ **Pentose phosphate pathway: TKT (transketolase deficiency), TALDO1, G6PD** | NADPH and **ribose-5-phosphate — the substrate for every nucleotide and all rRNA** | ⭐ **TKT deficiency → SHORT STATURE + developmental delay + congenital heart defects, in all five reported individuals**, with confirmed enzyme deficiency and pentose-phosphate metabolites in plasma and urine | none | 27259054 (human, AJHG 2016); 32828637 (metabolomic diagnosis of PPP defects) | **yes** |
| E18 | **One-carbon / folate / cobalamin: MTHFD1, MTR, MTRR, SHMT2, MMACHC (cblC)** | methyl-group and purine supply | **loss→SHORT** (cblC: growth failure) | Folate/B12 are the archetypal substrate-supply raise — but only correct deficiency | 39676000 (B12 and craniofacial development, INDEX) | no |
| E19 | ⭐⭐ **CBS — classical homocystinuria** | transsulfuration capacity | ⭐⭐ **loss→TALL AND MARFANOID** — arachnodactyly, long limbs, scoliosis, ectopia lentis. One of very few inborn errors of metabolism whose stature direction is **UP** | Betaine and pyridoxine treat it — i.e. **treatment REDUCES the tall phenotype.** The mechanism is thought to be homocysteine disrupting fibrillin/collagen cross-linking | 42255525 (2026, delay in diagnosis); 32245022, 35154919, 29279830 (human); 30394212 (tall stature review, INDEX) | no |
| E20 | ⭐⭐ **NAD+ de novo synthesis: NADSYN1, HAAO, KYNU — Congenital NAD Deficiency Disorder** | NAD+ availability during organogenesis | ⭐ **loss→VERTEBRAL SEGMENTATION DEFECTS, limb anomalies, cardiac/renal malformation (VACTERL-like)** | ⭐⭐ **Niacin/NAD-precursor supplementation prevents the malformations in mouse models** — one of very few published capacity-RAISING interventions with a skeletal endpoint | 33942433 (human genotype/phenotype expansion); 35484986 (NAD+ deficiency in human malformation/miscarriage); 40047807 (2025, yolk-sac NAD metabolism, mouse); 34200361 (KYNU, human) | **yes** |
| E21 | ⭐⭐⭐ **NAD+ SALVAGE in the growth plate: NAMPT** | NAD+ supply in limb mesenchyme | ⭐⭐ **Nampt deletion in all limb mesenchymal cells (Prx1-Cre) → DRAMATIC LIMB SHORTENING at birth from DEATH OF GROWTH-PLATE CHONDROCYTES.** Post-natal NAD depletion also kills chondrocytes and halts endochondral ossification and joint development. **Osteoblast formation was spared** — a chondrocyte-specific NAD dependence | ⭐⭐⭐ **NICOTINAMIDE RIBOSIDE GIVEN DURING PREGNANCY PREVENTED THE MAJORITY OF THE IN-UTERO DEFECTS (mouse).** NR is an over-the-counter compound. This is the strongest "raise a metabolic capacity → protect longitudinal growth" result found in this entire domain | 37330524 (mouse, Nat Commun 2023) | **yes** |
| E22 | **Sirtuins: SIRT1, SIRT6, SIRT7** | NAD+-dependent deacetylases; **SIRT7 is nucleolar and governs Pol I / rDNA transcription** — a direct NAD+→ribosome-capacity link | Sirt6-null mice are severely growth-retarded and progeroid (widely reported; primary not retrieved here) | NAD+ precursors (NR, NMN) raise the cofactor; **no bone-length endpoint found** | 41892337 (SIRT7 review, INDEX) | **yes** |
| E23 | **Hexosamine pathway and O-GlcNAc: OGT, OGA, GFPT1** | nutrient-sensing PTM on thousands of proteins — **and UDP-GlcNAc is the donor for GAG chain synthesis**, so this pathway is simultaneously signalling and matrix substrate | **OGT-CDG: X-linked intellectual disability with short stature** | OGA inhibitors (thiamet-G) raise O-GlcNAc — no bone endpoint | 37334838, 38566589, 39535175 (OGT-CDG models); 38653092 (CDG nosology, INDEX); 37107691 (HBP review, INDEX); 39975416 (endocrine implications of CDG, INDEX) | **yes** |
| E24 | ⭐ **Sulfate/PAPS donor capacity: PAPSS2 (brachyolmia), SLC13A1 (hyposulfataemia + mild SEMD), SLC26A2 (diastrophic dysplasia)** | PAPS is the universal sulfate donor for all proteoglycan sulfation — the plate's largest single biosynthetic sink | **loss→SHORT with specific skeletal dysplasias** | ⭐ Oral sulfate donors are the obvious substrate-supply route; **no sulfate donor has a bone-length endpoint in any species** | 36175384 (SLC13A1 human, hyposulfataemia + SEMD); 35261200 (PAPSS2 human); 25594860 (PAPSS2 mechanism); 27322429 (sulfonation review, INDEX) | **yes** |
| E25 | ⭐ **Nucleotide-sugar handling: CANT1 (Desbuquois dysplasia 1), TGDS (Catel-Manzke), SLC35D1 (Schneckenbecken), B4GALT7/B3GAT3/XYLT1** | UDP-sugar supply and product inhibition of Golgi glycosyltransferases | **loss→SHORT with multiple dislocations and advanced carpal ossification** | none | 30439444 (Cant1 KI/KO mice, cartilage GAG biosynthesis + endochondral ossification); 22539336 (human); 41928906 (2026 Cant1/β-catenin/CHSY1 axis); 34220933, 34539746 (reviews, INDEX) | **yes** |
| E26 | **Proteasome capacity: PSMB8/PSMB4/PSMA3/POMP/PSMG2 (PRAAS/CANDLE); PSMB1/PSMC1/PSMC3/PSMD12/PSMD11 (primary proteasomopathies)** | degradative throughput; and, when it fails, a type-I interferon response | **loss→SHORT STATURE + lipodystrophy** in PRAAS; NDD phenotypes in the primary proteasomopathies | NFE2L1/NRF1 drives proteasome "bounce-back"; no agent | 42167218 (2026, monoallelic PSMB8 PRAAS-ID); 38866022 (PSMD11); 35563729 (proteostasis/autoinflammation review, INDEX) | **yes** |
| E27 | **HSF1 / HSP70 / HSP90 — global chaperone capacity** | folding throughput under load | HSF1-null mice show growth retardation (widely stated; **primary not retrieved**) | ⭐ **Arimoclomol (approved) amplifies the heat-shock response; HSP90 inhibitors run the other way** | 37516663, 36455410 (arimoclomol, non-skeletal) | **yes** |
| E28 | **CCT/TRiC chaperonin (CCT5)** | folding of actin/tubulin — cytoskeletal capacity for a cell that must swell 10–20× during hypertrophy | CCT5 → hereditary sensory neuropathy; **no stature link found** — a negative | none | negative result | **yes** |
| E29 | **Lipid synthesis / SREBP: SCAP, SREBF1/2, FASN, MBTPS1/2 (S1P/S2P)** | membrane supply for a cell doubling its volume; also cholesterol for hedgehog signalling | **MBTPS2 (S2P) → X-linked osteogenesis imperfecta** — a site-2 protease that activates both SREBP and ATF6, i.e. lipid *and* UPR capacity in one gene | statins run the other way (and paediatric human data show no height effect) | 34093655 (MBTPS2-OI omics, human fibroblasts) | **yes** |
| E30 | **Mitophagy: PINK1, PRKN, BNIP3; ATR licenses PINK1-mediated mitophagy** | mitochondrial quality control in a hypoxic tissue; also a *link between the genome-maintenance and organelle arms* | no stature direction | none | 40105243 (ATR→PINK1 mitophagy) | **yes** |
| E31 | ⭐ **Polyamine supply: ODC1, SMS, AMD1, SRM — and spermidine as the eIF5A hypusine donor** | polyamines are required for eIF5A hypusination (B9) **and** are themselves growth-limiting | **SMS loss (Snyder-Robinson) → SHORT; ODC1 gain (Bachmann-Bupp) → also abnormal growth.** A band | ⭐ Spermidine is obtainable and rescues autophagy defects in trafficking disorders (E4); DFMO lowers polyamines (approved) — the wrong direction here | 41410504 (polyaminopathies review, INDEX); 39838718 (spermidine rescue); 40993392 (dietary polyamine depletion, oncology — direction of *caution*) | **yes** |
| E32 | **Iron/ferroptosis capacity in chondrocytes (GPX4 again, DMT1, SLC7A11)** | redox capacity of a cell making enormous amounts of collagen under hypoxia | GPX4 loss is a lethal SMD (B17); ferroptosis drives cartilage degeneration | ferroptosis inhibitors (research) | 41836552 (DMT1/ferroptosis in cartilage); 34688299 (INDEX) | **yes** |
| E33 | **Metabolic inflexibility as a systemic capacity limit (Fanconi anaemia as the worked example)** | whole-organism substrate handling rather than a single organelle | compromised glucose oxidation, enhanced ketogenesis, failure to thrive | none | 41313766 (2025, human FA) | **yes** |

### F. CROSS-CUTTING / CONCEPTUAL ROWS

| # | CAPACITY / CONCEPT | WHAT IT LIMITS | HEIGHT DIRECTION | CAN IT BE RAISED? | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|
| F1 | ⭐ **"Translational capacity" (ribosome number) vs "translational efficiency" (signalling) as separable variables** | the muscle-hypertrophy field has formalised exactly this distinction and concluded that **acute mTORC1 signalling is merely permissive while sustained growth requires physical expansion of the ribosome pool via RNA Pol I** | Directly transferable framing for the growth plate, where nobody has made the distinction | The review discusses "practical modulators" of ribosome biogenesis in humans | 42274633 (2026 review, INDEX); 41897342 (2026, ribosome biogenesis in muscle atrophy/hypertrophy, INDEX) | **yes** |
| F2 | **Nucleolar/ribosome decline as a programmed developmental event** | a *programmed* decline in ribosome levels governs human early neurodevelopment | Raises the possibility that ribosome content is a *scheduled* variable in other tissues too — including a growth plate that is winding down | — | 40760247 (2025, human) | **yes** |
| F3 | **Which capacity is limiting is ZONE-dependent** | resting zone (quiescent, hypoxic) vs proliferative (replication capacity) vs hypertrophic (secretory + volume capacity) | Predicts that no single capacity is limiting for the whole plate | — | 41795828 (resting zone quiescence, INDEX); 37485234 (hypertrophic chondrocytes, INDEX) | no |
| F4 | **Capacity defects vs signalling defects respond differently to GH** | PCNT/MOPD2 is explicitly GH-unresponsive; Meier-Gorlin GH data are anecdotal; MPS growth responds partially to ERT/HSCT | A practical triage rule: cell-intrinsic capacity defects tend not to respond to hormone | — | 33042696, 35282325, 40083105 | no |
| F5 | **Every ribosomopathy/spliceosomopathy is tissue-selective — and nobody knows why** | the shared unexplained observation across A, C | If the growth plate is a high-demand tissue, it should be preferentially vulnerable — which is exactly what CHH, RPL13-SEMD, ERI1-SEMD, MOPD1 and Wolcott-Rallison show | — | 40264708, 35893124, 24252615 (ribosome biogenesis in skeletal development, INDEX) | no |

### G. LATE ADDITIONS — SEARCHED AND MOSTLY NEGATIVE (recorded so they are not re-derived)

| # | CAPACITY / GENE / DISEASE | WHAT IT LIMITS | HEIGHT DIRECTION | CAN IT BE RAISED? AGENT? | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|
| G1 | **Ribosome-associated quality control: NEMF, LTN1, ZNF598, GCN1, RQT complex** | disposal of stalled ribosomes and incomplete nascent chains — a *throughput protection* system, not a throughput system | **No stature phenotype found** for any RQC gene. NEMF disease is neurological. Recorded as a searched negative | none | 38949989 (RQC in human disease, INDEX); 35452614, 41535548 (INDEX) | **yes** |
| G2 | **tRNA splicing: TSEN2/15/34/54, CLP1, RTCB, FAM98B** | maturation of intron-containing pre-tRNAs, i.e. usable tRNA supply | **loss→pontocerebellar hypoplasia** with growth failure; Drosophila mutants phenocopy | none | 35132432 (Drosophila); 37544645, 42014620 (INDEX) | **yes** |
| G3 | **Integrator complex (INTS1, INTS8, INTS11…) and transcription pause-release** | how fast RNA Pol II can be released into productive elongation — a *transcriptional* throughput ceiling upstream of everything in this domain | INTS-related NDDs include growth restriction; and **RNU4ATAC mutations disrupt Integrator homeostasis**, tying C1 to this row | none | 36537210 (RNU4ATAC → Integrator, human); 35615272 (pause/escape in NDD, INDEX) | **yes** |
| G4 | **Topoisomerases and condensin (TOP3A, TOP2B, NCAPD2/D3/H)** | decatenation capacity during replication and mitosis | Europe PMC returned **zero hits** for the combined query; direction not established | none | negative search result | **yes** |
| G5 | **SEC61 translocon and co-translational targeting (SRP54, SRP72, SEC61A1)** | the very first step of secretion — getting procollagen into the ER at all | **SRP54 → severe congenital neutropenia and a Shwachman-Diamond-LIKE syndrome**, i.e. with growth failure | none | 29914977 (human, SRP54); 30237254 (INDEX) | **yes** |
| G6 | **FGF→lysosome biogenesis in chondrocytes (mannose-6-phosphate receptor pathway)** | a second, newer arm of the FGF→catabolic-capacity axis in cartilage, distinct from E9 | mouse | none | 40747612 (2025) | **yes** |
| G7 | **MMP13 frameshift → short stature via enhanced MMP13-HSPA5/BiP interaction and ER stress** | a matrix protease whose *mutant protein jams the chaperone*, so the stature effect runs through ER capacity rather than through proteolysis | **loss/misfolding→SHORT** | none | 41877217 (2026, human) | **yes** |
| G8 | ⭐ **"Osteopotentia" and demand-driven rER EXPANSION in a collagen-secreting bone cell** | the paper states the premise of this whole domain explicitly: bone-forming cells **respond to high metabolic demand by ACTIVELY EXPANDING their rough ER and raising type-I collagen synthesis**, and a gene is required for it | loss→impaired osteoblast maturation, bone formation and skeletal integrity (mouse) | ⭐ The clearest published statement that secretory capacity in a skeletal cell is a *regulated, expandable* variable rather than a fixed ceiling. Never asked in a chondrocyte | 20440000 (mouse) | **yes** |
| G9 | **KIF5B / kinesin-mediated intracellular transport** | motor-driven cargo movement — the step between ER exit and the cell surface | **dominant-negative KIF5B → osteogenesis imperfecta, via downregulated mTOR signalling** (human) | none | 37934770 (human, 2023) | **yes** |
| G10 | **eIF6 / SBDS axis and nonsense-suppression therapy in inherited bone-marrow failure** | eIF6 release is the specific 60S step SDS blocks; readthrough agents are proposed for this class | growth failure is core to SDS | ⭐ **Nonsense-suppression / readthrough therapy has been proposed for IBMFS** — a capacity-restoring modality with no skeletal endpoint | 32630050 (hypothesis paper, INDEX); 38697731 (DBA international consensus, INDEX) | **yes** |

---

## PROSE

### 1. ANY CAPACITY THAT HAS EVER BEEN RAISED ABOVE NORMAL WITH A GROWTH ENDPOINT IN ANY SPECIES

This is the question the domain exists to answer, and the honest answer is: **the list is very short, almost
all of it is rescue-of-a-deficit rather than elevation-above-normal, and only two items involve a compound a
person could actually obtain.** Ranked by how close each comes to a true elevation with a length endpoint:

1. ⭐⭐⭐ **NAD+ — NICOTINAMIDE RIBOSIDE, growth plate, mouse, length endpoint (PMID 37330524).** Deleting
   *Nampt* in all limb mesenchymal cells produced dramatic limb shortening from death of growth-plate
   chondrocytes; **nicotinamide riboside given during pregnancy prevented the majority of the defects.**
   NR is over-the-counter. The paper also shows the dependence is **chondrocyte-specific** — osteoblast
   formation was preserved — which is unusually clean. ⚠ But it is *restoration in a knockout*, not
   elevation in a normal animal, and the authors do not report giving NR to wild-type mice.
2. ⭐⭐⭐ **Autophagy — TAT-BECLIN1, growth plate, mouse (PMIDs 26595272 Nature + 26939858, where the agent is
   named).** Chondrocyte autophagy is induced postnatally by FGF18→FGFR4→JNK→VPS34-beclin-1 and controls
   procollagen-II secretion; Atg7 loss traps procollagen II in the ER. The *Fgf18*+/− and *Fgfr4*−/−
   growth-plate ECM defects were **rescued in vivo with TAT-Beclin1, a cell-permeable peptide that enhances
   endogenous Beclin1.** This is the closest thing in the literature to "raise a secretory-throughput
   capacity with a drug and get more growth-plate output," and **the agent is a defined, obtainable research
   peptide** rather than a genetic manipulation. ⚠ Still a rescue of a deficit, not elevation above normal;
   dose and route not in the sources I could reach.
3. ⭐⭐ **tRNA m7G capacity — α-ketoglutarate, endochondral bone, mouse (PMID 39255038, JCI).** *Mettl1*
   deletion or a *Wdr4* missense knock-in impaired endochondral bone formation; **αKG supplementation
   ameliorated the skeletal defect.** Notably, targeting the ISR or mTORC1 made the bone defect **worse** —
   a direct warning that "boost the stress response" is not automatically the right direction here.
4. ⭐⭐ **Translational output via 4E-BP1/2 knockdown, limb mesenchyme, mouse (PMID 30008325).** mTORC1
   controls *Sox9* translation; **knocking down the translational repressors 4E-BP1/2 — which raises
   cap-dependent translation — rescued the mesenchymal condensation defect**, and a Sox9 transgene rescued
   skeletal growth. Genetic, not pharmacological.
5. ⭐ **SOX9 overexpression raises ribosome biogenesis and total translational capacity in chondroprogenitors
   (PMID 34235151).** In vitro (ATDC5), with polysome profiling and SUnSET — the only demonstration that
   translational capacity in a cartilage cell can be pushed *up*. **No length endpoint.**
6. ⭐ **Amino-acid supplementation in aminoacyl-tRNA synthetase deficiency, human.** Supplying the cognate
   amino acid to raise charging capacity is an actual clinical practice in this class; tyrosine
   supplementation in YARS2 disease is documented (PMID 41404429). Growth is among the reported outcomes but
   I did not find a dedicated height analysis.
7. ⭐ **Degradative capacity raised pharmacologically in a skeletal dysplasia model — curcumin increased
   proteolysis of mutant matrilin-3 and reduced ER stress (PMID 36675026);** carbamazepine has been given to
   control and OI mice with bone structure/strength endpoints (PMID 35701367).
8. ⭐ **Lysosomal capacity restored by ERT/HSCT in mucopolysaccharidosis, human, with height as an outcome**
   (PMIDs 40083105, 42279040, 41168830). The clearest human evidence that restoring a degradative capacity
   improves growth — and also that it does **not** normalise final height.
9. ⭐ **Telomere capacity raised in humans — danazol elongates telomeres (PMIDs 41115243, 41953763).** The
   only capacity in this entire domain that has been *measurably raised in living humans by a drug*, and
   **height has never been measured.** That is a striking omission given that dyskeratosis congenita is a
   short-stature disease.
10. **Chaperone capacity — arimoclomol**, an approved heat-shock-response amplifier (PMIDs 37516663,
    36455410, 30522930). Zero skeletal literature of any kind.
11. **Secretory capacity — XBP1s/ATF6 activation** raises folding and secretory output in industrial cell
    lines (PMID 41509511) and ATF6 activators exist; **no bone endpoint in any species.**
12. **eIF2B activation — ISRIB.** Restores translation initiation under ISR. Searched directly: **no
    bone-length endpoint in any species.**

**Everything else in this domain has only ever been switched OFF.** That is the structural finding: this is
a domain of loss-of-function human genetics and conditional knockouts, and the elevation direction is
almost entirely unexplored. The reason is not biological — it is that these capacities were studied by
disease geneticists and cancer biologists, for whom the interesting direction is always *less*.

### 2. WHICH OF THESE IS ACTUALLY RATE-LIMITING IN A CHONDROCYTE, AND HOW WOULD YOU KNOW

**The candidates, ordered by how much the demand exceeds an ordinary cell's:**

- **Procollagen ER exit (E1/E2).** A growth-plate chondrocyte secretes collagen II as its principal output,
  and procollagen physically will not fit a standard COPII vesicle. TANGO1 loss abolishes bone
  mineralisation in mouse and causes odontochondrodysplasia in humans; collagen has a *specific* SEC24
  paralogue preference. This is the only capacity in the list where the cargo's geometry forces a dedicated
  machine. **Strongest prior for a genuine ceiling.**
- **Autophagy/ER disposal (E9).** Directly demonstrated: Atg7 loss causes procollagen-II to accumulate *in
  the ER*, and raising autophagy rescues the phenotype. The disposal arm of the secretory pathway is
  demonstrably rate-relevant.
- **PAPS/sulfate donor supply (E24) and UDP-sugar supply (E25).** Aggrecan carries ~100 sulfated GAG chains;
  the donor pools are finite and every human defect in them is a skeletal dysplasia.
- **Translational capacity (A16/B1/F1).** SOX9 controls ribosome biogenesis in chondroprogenitors, and
  raising cap-dependent translation rescues skeletal growth. The muscle field has already concluded that
  ribosome *number*, not mTORC1 signalling, is the sustained-growth bottleneck.
- **Replication capacity (D1).** The Meier-Gorlin class is the single strongest human genetic statement that
  replication throughput sets body size — but it is proportionate and systemic, which argues it acts on
  total cell number rather than on the plate specifically.
- **NAD+ (E21).** The one metabolic capacity with a demonstrated chondrocyte-selective requirement.

**How you would know — the discriminating experiments, none of which has been done:**

1. **Measure it, zone by zone.** Polysome profiling, SUnSET/puromycin incorporation, nucleolar area, and
   rDNA transcription rate in resting vs proliferative vs hypertrophic chondrocytes. If translational
   capacity is limiting, it should rise steeply into the zone that makes the matrix. `34235151` shows the
   assays work in a chondrocyte model.
2. **Raise it in a normal animal and put a caliper on the femur.** Every result in section 1 is a rescue.
   The decisive experiment for every one of them is the same: give it to a wild-type growing animal.
3. **The "cargo overload" test.** If ER exit is limiting, then *lowering* collagen II output should paradoxically
   improve some downstream parameter, and raising TANGO1/SEC24D should raise matrix output. Neither has been tried.
4. **The tissue-specificity control (F5).** A capacity is only "limiting in a chondrocyte" if its
   perturbation hurts cartilage more than other tissues at equal dose. RPSA (asplenia, no growth phenotype)
   vs RPL13 (pure SEMD) shows this discriminates in practice.
5. **Dose-response, not knockout.** Minor-intron retention (C3) shows that a capacity can be measured as a
   graded, transcriptome-wide read-out. That is the template: build a graded knockdown series in chondrocytes
   and find where the matrix output curve bends. A knockout tells you a gene is required; only a series tells
   you it is *limiting*.

**The strongest argument that translation is NOT simply rate-limiting** is A12: many ribosomopathy phenotypes
are p53-dependent, i.e. the growth loss is a *checkpoint decision* triggered by unassembled ribosome
components, not a shortfall of protein. If that generalises, then raising ribosome biogenesis in a normal
cell may do nothing, because nothing was arrested.

### 3. DISEASES WHERE THE CAPACITY DEFECT PRODUCES TALL RATHER THAN SHORT

This is the rarest category in the domain and I searched for it specifically. Confirmed:

- ⭐⭐ **DIS3L2 / Perlman syndrome (C11).** Loss of a cytoplasmic 3′→5′ exoribonuclease produces **fetal
  overgrowth** — macrosomia, nephromegaly, Wilms tumour. Mechanistically it degrades uridylated RNA
  including pre-let-7, and Drosophila and vertebrate work put it upstream of PI3K/Akt. **This is the one
  unambiguous case in this domain of an RNA-machinery capacity defect that makes an organism bigger.**
  Direction of therapeutic interest would be inhibition; there is no agent, and it is an oncogenic direction.
- ⭐⭐ **CBS / classical homocystinuria (E19).** A transsulfuration enzyme deficiency producing **tall,
  marfanoid habitus with disproportionately long limbs and arachnodactyly.** The classic entry in every
  "tall stature" differential that is an inborn error of metabolism. The proposed mechanism is homocysteine
  interfering with fibrillin/collagen cross-linking — i.e. the height is a *connective-tissue* consequence
  of a metabolic capacity defect, not increased growth-plate output. Treatment lowers the phenotype.
- ⭐⭐ **NFIX (C13) — the same gene going both ways, decided by NMD.** Alleles subject to nonsense-mediated
  decay give **Sotos-like OVERGROWTH with ADVANCED bone age (Malan syndrome)**; alleles that escape NMD give
  Marshall-Smith syndrome; and the **reciprocal 19p13 microduplication encompassing NFIX gives SHORT
  stature and small head circumference** (PMID 29184170). This is the most instructive row in the whole
  domain: an RNA-surveillance capacity determines the *sign* of a growth phenotype.
- ⭐ **PSMD11 (E26) — obesity rather than tall stature**, but a proteasome capacity defect whose body-size
  direction is *up* rather than down (PMID 38866022). Recorded because it breaks the class pattern.

**Near-misses and negatives, recorded so they are not re-derived:**
- The classical overgrowth syndromes (NSD1/Sotos, EZH2/Weaver, DNMT3A/Tatton-Brown-Rahman, SETD2, CHD8) are
  **chromatin** rather than cellular-capacity genes and belong to another domain; PMIDs 37450557 and
  33194904 are useful indexes. Several of them pay the trade — advanced bone age.
- Marfan (FBN1) and the microfibril module are ECM, not capacity.
- **Fragile X / FMR1** is a translational repressor whose loss de-represses translation, and the phenotype
  includes macrocephaly and (childhood) tall stature — but I could **not** verify a growth-specific primary
  in this session; recorded as UNVERIFIED rather than asserted.
- **Meier-Gorlin (D1) is the tempting inversion and it does not work.** Loss of origin licensing shortens;
  but the licensing *inhibitor* geminin (GMNN) is itself a Meier-Gorlin gene, so removing the brake also
  shortens. The axis is a band with both ends down, which is the commonest shape in this domain.
- No ribosomopathy, no spliceosomopathy, no genome-maintenance disorder and no organelle disorder found in
  this enumeration produces tall stature. **The direction of this whole domain is overwhelmingly downward,
  and that asymmetry is itself the finding**: capacity is normally in excess, and the phenotypes appear only
  when it falls below demand — which is exactly why raising it above normal has almost never been tried.

---

## WHAT I COULD NOT VERIFY

Recorded honestly. Nothing below should be cited as fact.

1. ✅ **RESOLVED DURING THE ROUND — the autophagy-activating agent in PMID 26595272 is `TAT-Beclin1`**, named
   in the authors' own commentary (PMID 26939858, *Cell Cycle* 2016, "Autophagy gets to the bone").
   What remains unverified is the **dose, route and schedule**, which are in the Nature Methods section and
   were not reachable from any open source I could access.
2. **ATF4-null mouse skeletal phenotype (B7)** — widely stated but I did not retrieve the primary.
3. **HSF1-null and SIRT6-null mouse growth phenotypes (E22, E27)** — same; asserted in reviews, primary not
   retrieved.
4. **RNF168/RIDDLE syndrome stature (D14)**, **UTP4/CIRH1A (A10)**, **BMS1 (A11)**, **NOL11 (A12 in the
   brief's list)** — no primary retrieved; direction not established here.
5. **RNU4-2/ReNU syndrome growth direction (C9)** — the gene is real and recent; I did not verify a stature
   phenotype.
6. **FMR1/fragile X tall stature** — could not verify a growth-endpoint primary.
7. **EIF2AK4/GCN2 stature (B5)** — I found no stature phenotype and record that as an unconfirmed negative
   rather than a demonstrated one.
8. **Codon usage/Gly-tRNA supply and collagen output (B18)** — I searched directly and found **no primary at
   all.** This appears to be a genuinely unasked question rather than a retrieval failure, but I cannot
   exclude that it exists under vocabulary I did not use.
9. **Telomerase overexpression (AAV-TERT) and body length** — mouse lifespan-extension work exists; I could
   not verify any body-length or bone-length endpoint.
10. **AJHG/Nature/JCI full texts** were only accessible as abstracts via eutils in several cases (RPL13,
    ERI1, Perlman, TKT). Effect sizes beyond what the abstracts state are not reported here.
11. **Europe PMC returned intermittent 502/503 errors** during two query batches; those queries were retried
    and succeeded, but I cannot rule out that a small number of results were missed.
12. **L-leucine in Diamond-Blackfan anaemia (A5).** The idea — supply an mTORC1-activating amino acid to
    raise translation in a ribosome-deficient cell — is widely discussed, but a targeted search returned no
    trial with a **growth or height** endpoint. Recorded as unverified rather than asserted.
13. **TAT-Beclin1 dose, route and schedule (E9).** Named but not quantified in the sources I could reach.
14. I did **not** search clinicaltrials.gov, Drugs@FDA or the EMA in this session — those sources would be the
    right place to look for juvenile-toxicity length endpoints under arimoclomol, ISRIB-class compounds,
    ATF6 activators and danazol, and for any paediatric height data in the MPS ERT programmes.
