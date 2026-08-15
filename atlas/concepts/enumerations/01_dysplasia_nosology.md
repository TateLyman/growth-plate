# DOMAIN 01 — GENETIC SKELETAL DISORDER NOSOLOGY (R436 full-space enumeration)

**Agent:** domain-01 enumeration. **Date:** 2026-08-15.
**Sources:** all external. Primary = **Nosology of Genetic Skeletal Disorders, 2023 revision (11th)**,
Unger S, Ferreira CR, Mortier GR, … Superti-Furga A. *Am J Med Genet A* 2023;191(5):1164–1209.
**PMID 36779427**, PMCID PMC10081954, DOI 10.1002/ajmg.a.63132. Full text retrieved via NCBI
eutils (`efetch db=pmc id=10081954`) and parsed directly; **771 entries, 552 genes, 41 groups.**
Secondary = Europe PMC REST search, NCBI eutils, and the **Human Phenotype Ontology public API**
(`ontology.jax.org/api/network/annotation/<HP:id>`) for gene/disease sets under
HP:0000098 Tall stature, HP:0001548 Overgrowth, HP:0002750 Delayed skeletal maturation,
HP:0001519 Disproportionate tall stature, HP:0011407 Proportionate tall stature,
HP:0003782 Eunuchoid habitus, HP:0003799 Marked delay in bone age,
HP:0002663 Delayed epiphyseal ossification, HP:0005616 Accelerated skeletal maturation (control),
HP:0000053 Macroorchidism, HP:0004570 Increased vertebral height, HP:0008421 Tall lumbar vertebral bodies.
**No file in the growth-plate repository other than the two briefs was read.**

Species is **HUMAN** for every row unless explicitly marked otherwise.

**SIZE OF THIS ENUMERATION: 187 table rows — 41 group rows (Table A) + 146 disorder/mechanism rows
(Table B). 119 rows are marked OBSCURE = YES.** All 75 spot-checked PMIDs were re-resolved against
NCBI esummary on 2026-08-15; none is fabricated.

---

## KEY STRUCTURAL FACTS ABOUT THE 2023 NOSOLOGY (verified from full text)

- 11th revision; **771 entries / 552 genes / 41 groups**.
- The headline change is the **DYADIC NAMING SYSTEM** — every entity is now named
  `<phenotype>, <GENE>-related` (e.g. "Achondrogenesis, COL2A1-related"), replacing eponyms and
  list-numbering. Entries carry a stable `NOS xx–yyyy` identifier.
- Groups renamed in 2023 (verified in the text): "Osteopetrosis and related **osteoclast** disorders";
  "Osteogenesis Imperfecta and **bone fragility** group"; **"Overgrowth (tall stature) syndromes and
  segmental overgrowth"** (was "…with skeletal involvement" — deliberately broadened);
  "Syndromes **featuring** craniosynostosis"; "Isolated brachydactylies" / "Brachydactylies as part of
  syndromes"; "Skeletal disorders caused by **abnormalities of cilia or ciliary signaling**";
  "Disorders of **bone mineralization**"; "**Split hand/foot** with and without other manifestations".
- ⚠ **The Nosology does NOT annotate height direction per entry.** It is organised by radiographic
  pattern and by gene, not by stature. Every HEIGHT DIRECTION call below is therefore *my* synthesis
  from the group's constituent disorders plus external sources, not a quotation of the Nosology.
- ⚠ **The Nosology carries essentially no bone-age field.** Grepping the entire full text for
  "bone age" returns exactly **two** entries — both **ADVANCED**, not delayed (see rows G05/G07 notes).
  There is **no delayed-bone-age or delayed-fusion axis anywhere in the Nosology.** That absence is
  itself a finding: the nosology's organising axis is *radiographic morphology*, and skeletal
  *tempo* is invisible to it.
- Prior revisions for provenance: 2019 (PMID 31633310), 2015 (PMID 26394607), 2010 (PMID 21438135),
  2006 (PMID 17120245). A 2026 ClinGen re-curation of skeletal-disorder gene validity also exists
  (PMID 41313243) — not yet read in full.

---

## TABLE A — THE 41 GROUPS (the ACTUAL group list, verbatim group names)

`N=` is the number of `NOS` entries I counted in that group's table in the full text.

| # | GROUP/CONCEPT | MECHANISM | GENES (representative; from the Nosology's own entries) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| G01 | **FGFR3 chondrodysplasias** (N=5) | FGFR3 tyrosine-kinase signalling; gain-of-function → constitutive ERK/STAT braking of proliferation | FGFR3 (thanatophoric 1/2, achondroplasia, hypochondroplasia, SADDAN, CATSHL) | **MIXED — GoF = SHORT; LoF = TALL.** Contains **CATSHL** (camptodactyly, tall stature, hearing loss), cross-listed to group 31 | 36779427; CATSHL 27139183, 37990933 | no (group) / **YES** (the LoF arm) |
| G02 | **Type 2 collagen disorders** (N=10) | COL2A1 triple-helix; also COL11A1/2, COL9A1-3, FN1 overlap | COL2A1, COL11A1, COL11A2, COL9A1/2/3, FN1 | SHORT (achondrogenesis→SEDC→Kniest); **BUT Stickler type I is annotated tall/marfanoid habitus in HPO** | 36779427 | no |
| G03 | **Type 11 collagen disorders** (N=7) | COL11A1/COL11A2 fibril nucleation, fibril diameter control | COL11A1, COL11A2 | SHORT to normal; Stickler II, OSMED, Marshall | 36779427 | no |
| G04 | **Sulfation disorders** (N=12) | Sulfate supply, PAPS synthesis, Golgi PAPS transport and GAG sulfotransfer | SLC26A2, PAPSS2, IMPAD1, CHST3, CHST11, CHST14, SLC35B2, DSE, CANT1, TGDS, HS2ST1, CHSY1 | SHORT (achondrogenesis 1B, diastrophic, brachyolmia, Desbuquois) | 36779427 | no |
| G05 | **Dysplasias with multiple joint dislocations** (N=10) | Proteoglycan linkage-region synthesis; exocyst; kinesin | XYLT1, B3GALT6, B4GALT7, B3GAT3, CANT1, KIF22, EXOC6B, CSGALNACT1, SLC10A7, CHSY1, PISD, SLC39A13 | SHORT. ⚠ contains **SDJLABA, CSGALNACT1-related — "skeletal dysplasia with joint laxity and ADVANCED BONE AGE"**, one of only two bone-age entries in the whole Nosology | 36779427 | **YES** (advanced-BA entity) |
| G06 | **Filamins and related disorders** (N=15) | Actin cross-linking / mechanotransduction scaffold; TAK1–TAB2 | FLNA, FLNB, MAP3K7, TAB2, RFLNA, MYH3, SH3PXD2B, CHST3 | SHORT to normal (FMD, OPD, Larsen, atelosteogenesis) | 36779427 | no |
| G07 | **Proteoglycan core proteins disorders** (N=6) | Core protein of the aggregating/basement-membrane proteoglycans | HSPG2 (perlecan), **ACAN**, BGN | SHORT. ⚠ contains **"Short stature with ADVANCED bone age, ACAN-related"** (the 2nd of two BA entries). ACAN is the largest single negative-height effect in human burden data | 36779427 | no |
| G08 | **TRPV4 disorders** (N=5) | Mechanosensitive/osmosensitive Ca²⁺ channel; GoF | TRPV4 | SHORT (metatropic, brachyolmia, SMD Kozlowski, parastremmatic) — **NON-MONOTONIC: both GoF and LoF alleles shorten** | 36779427 | no |
| G09 | **Pseudoachondroplasia and the multiple epiphyseal dysplasias** (N=11) | Misfolded ECM protein retention in chondrocyte ER (COMP/MATN3) → ER stress | COMP, MATN3, COL9A1/2/3, CANT1, SLC26A2, RNU4ATAC, COL2A1 | SHORT | 36779427 | no |
| G10 | **Skeletal disorders caused by abnormalities of cilia or ciliary signaling** (N=61 — the LARGEST group) | Intraflagellar transport, dynein-2 retrograde motor, ciliary base/tip; the cilium is where all Hh transduction occurs | DYNC2H1, IFT80/81/122/140/172/43, WDR19/34/35/60, NEK1, TTC21B, CILK1, INTU, TRAF3IP1, DYNC2LI1, TCTEX1D2 | SHORT (SRPS, ATD/Jeune, cranioectodermal). ⭐ **BUT ciliary genes (incl. IFT140) recur in NON-SYNDROMIC FAMILIAL TALL STATURE** — see B-list | 36779427; 34194391; 38152138 | **YES** (the tall arm) |
| G11 | **Metaphyseal dysplasias** (N=12) | Hypertrophic-zone/metaphyseal transition; RNase MRP; ribosome biogenesis | COL10A1, RMRP, POP1, SBDS, EFL1, DNAJC21, SRP54, MMP13, MMP9, RUNX2, LBR, NEPRO | SHORT | 36779427 | no |
| G12 | **Spondylometaphyseal dysplasias (SMD)** (N=6) | Mixed: TRAP/interferon, Golgi tether, phospholipid synthesis, ferroptosis | ACP5, TRIP11, FN1, COL2A1, PCYT1A, PLCB3, HHAT, TRPV4, GPX4, CFAP410, NEK1 | SHORT | 36779427 | no |
| G13 | **Spondyloepi(meta)physeal dysplasias (SE(M)D)** (N=32) | ER/Golgi secretory stress, UFMylation, glycosylation, NGD | TRAPPC2, EIF2AK3 (PERK), DYM, RAB33B, MATN3, DDRGK1, UFSP2, DDR2, SMARCAL1, EXTL3, PGM3, NANS, RPL13, MBTPS1, NBAS, RINT1, TMEM165, AIFM1, RSPRY1, BNIP1, PISD | SHORT | 36779427 | no |
| G14 | **Severe spondylodysplastic dysplasias** (N=7) | Golgi/nucleotide-sugar transport; mitochondrial import | TRIP11, SLC35D1, GPX4, SBDS, INPPL1, PAM16, ALG9 | SHORT, usually lethal | 36779427 | no |
| G15 | **Mesomelic and rhizo-mesomelic dysplasias** (N=17) | Limb-segment patterning; SHOX dosage; non-canonical WNT/PCP | **SHOX**, GPC6, FZD2, WNT5A, DVL1, DVL3, ROR2, NXN, SULF1, SLCO5A1, ID4, AFF3, MAB21L2, HOXD cluster, ZRS | SHORT. ⭐ **SHOX is dosage-dependent and its OVER-dosage (PAR1/Xp22.33 duplication, extra sex chromosomes) is a leading cause of TALL stature** — see B-list | 36779427; 41751622 | **YES** (the overdosage arm) |
| G16 | **Acromesomelic dysplasias** (N=7) | CNP→NPR2→cGMP→PKG2 axis; BMP receptor | **NPR2**, **PRKG2**, GDF5, BMPR1B | SHORT (biallelic NPR2 LoF = AMDM). ⭐ **Monoallelic NPR2 GAIN-of-function = TALL (Miura type, group 31)** — same gene, opposite alleles | 36779427; 24259409; 32282051 | no (short arm) / **YES** (GoF arm) |
| G17 | **Acromelic dysplasias** (N=17) | Microfibril / TGF-β sequestration; also PDE4D–PKA–GNAS | IHH, ADAMTSL2, **FBN1** (TB5 domain), LTBP3, ADAMTS10, ADAMTS17, LTBP2, SMAD4, PDE4D, PRKAR1A, GNAS, GDF6, SDC2, MIR140, RMRP | SHORT (geleophysic, acromicric, Weill-Marchesani). ⭐ **The same gene FBN1 gives TALL in group 31** — the clearest allele-direction split in the Nosology | 36779427 | no |
| G18 | **Brachydactylies (isolated)** (N=11) | Digit-ray/phalangeal patterning: IHH–PTHrP, BMP, GDF5 | IHH, BMPR1B, BMP2, GDF5, ROR2, NOG, HOXD13, KCNJ2, SOX9, PAX3, PTHLH | Digits short; stature normal or mildly short | 36779427 | no |
| G19 | **Brachydactylies as part of syndromes** (N=22) | Chromatin (TRPS1, HDAC4, CREBBP/EP300), GPI anchor, GNAS/cAMP | TRPS1, EXT1, TGDS, TBC1D24, HDAC4, PIGV, PDE3A, PRMT7, GNAS, MYCN, HOXA13, CREBBP, EP300, CHSY1, ERF, GPC4, ARID1A/ARID1B | SHORT | 36779427 | no |
| G20 | **Bent bones dysplasia group** (N=6) | SOX9 dosage; IL6ST/LIFR gp130; kinesin | SOX9, LIFR, IL6ST, KIF5B, FGFR2, LAMA5, ALPL | SHORT | 36779427 | no |
| G21 | **Primordial dwarfism and slender bones group** (N=35) | Centrosome/replication/DNA-damage-response and the CUL7–OBSL1–CCDC8 "3-M" complex; minor spliceosome | CUL7, OBSL1, CCDC8, PCNT, ATR, RBBP8, CEP152, DNA2, TRAIP, NSMCE2, CENPE, CRIPT, XRCC4, DONSON, PCNA, CDKN1C, RNU4ATAC, TBCE, FAM111A | SHORT (extreme, prenatal onset). ⚠ Mechanistically the *mirror* of the overgrowth group — CDKN1C sits in both | 36779427 | no |
| G22 | **Lysosomal Storage Diseases with Skeletal Involvement** (N=26) | Glycosaminoglycan / oligosaccharide catabolic block → dysostosis multiplex | IDUA, IDS, SGSH, NAGLU, HGSNAT, GNS, GALNS, GLB1, ARSB, GUSB, ARSK, VPS33A, FUCA1, **MAN2B1**, MANBA, AGA, NEU1, CTSA, SLC17A5, SUMF1, GNPTAB | SHORT. ⚠ **MAN2B1 (α-mannosidosis) is annotated TALL stature + increased vertebral height in HPO** — a genuine oddity inside a short-stature group | 36779427; HPO OMIM/ORPHA:309282 | **YES** |
| G23 | **Chondrodysplasia punctata (CDP) group** (N=11) | Cholesterol/plasmalogen biosynthesis; peroxisome; vitamin-K-dependent γ-carboxylation; lamin B receptor | ARSL(ARSE), EBP, NSDHL, MGP, LBR, PEX7, GNPAT, AGPS, FAR1, PEX5, GNPTAB, FAM20C, DDR2 | SHORT. ⚠ **NSDHL (CK syndrome / CHILD) is HPO-annotated TALL** | 36779427 | **YES** (NSDHL arm) |
| G24 | **Osteopetrosis and related osteoclast disorders** (N=20) | Osteoclast number/function: proton pump, chloride channel, RANK/RANKL, carbonic anhydrase | TCIRG1, CLCN7, SNX10, OSTM1, TNFRSF11A, TNFSF11, PLEKHM1, CA2, IKBKG, SLC4A2, FERMT3, RASGRP2, LRRK1, CTSK, SLC29A3, CSF1R | SHORT to normal. **Resorption is REQUIRED to discharge the plate — the class demonstrates the "jam"** | 36779427 | no |
| G25 | **Osteosclerotic disorders** (N=42) | High-bone-mass: WNT brake removal (SOST/LRP5/LRP4/SFRP4), FGF23/mineral, gap junction, TGFB1 | **SOST**, LRP5, LRP4, SFRP4, AMER1, LEMD3, ANKH, GJA1, **TGFB1**, GALNT3, FGF23, FAM20C, MAP2K1, SLCO2A1, **HPGD**, TBXAS1, POLR3B, DHCR24 | **MIXED and this is the key one: SCLEROSTEOSIS (SOST biallelic LoF) is TALL/OVERGROWTH**, and Camurati-Engelmann (TGFB1) and primary hypertrophic osteoarthropathy (HPGD/SLCO2A1) are marfanoid/tall | 36779427; 24019634; HPO OMIM:269500 | **YES** |
| G26 | **Osteogenesis Imperfecta and bone fragility group** (N=55) | Type I collagen synthesis/folding/cross-linking/mineralisation; WNT1; osteoblast | COL1A1, COL1A2, CRTAP, P3H1, PPIB, IFITM5, SERPINF1, SERPINH1, FKBP10, TMEM38B, BMP1, WNT1, CREB3L1, SPARC, TENT5A, PLOD2, PLS3, SP7, MBTPS2 | SHORT (severity-dependent) | 36779427 | no |
| G27 | **Disorders of bone mineralisation** (N=24) | Phosphate/pyrophosphate/vitamin-D homeostasis | ALPL, PHEX, FGF23, DMP1, ENPP1, CLCN5, SLC34A3, CYP27B1, CYP2R1, VDR, CYP3A4, CASR, GCM2, CDC73, TRPV6, ANKH, TNFRSF11B, SGK3, HNRNPC | SHORT (rickets/osteomalacia phenotypes) | 36779427 | no |
| G28 | **Skeletal disorders of parathyroid hormone signaling cascade** (N=6) | PTH1R–Gsα–cAMP–PKA–SIK–HDAC4 cascade | PTH1R, **SIK3**, PTH, PTHLH, PDE4D, PRKAR1A, GNAS | SHORT at BOTH ends: Jansen (constitutive PTH1R, max cAMP) and Blomstrand (LoF) and acrodysostosis all shorten | 36779427 | no |
| G29 | **Osteolysis group** (N=12) | Osteoclast/matrix turnover; nuclear lamina; NOTCH2 stabilisation | TNFRSF11A, LMNA, ZMPSTE24, MTX2, MMP2, MMP14, **NOTCH2**, MAFB, **PDGFRB**, BANF1, ASAH1 | SHORT. ⚠ **Hajdu-Cheney (NOTCH2) is the ONLY disorder carrying HP:0008421 "Tall lumbar vertebral bodies"**; PDGFRB links Penttinen ↔ Kosaki OVERGROWTH | 36779427 | **YES** |
| G30 | **Disorganized development of skeletal components group** (N=22) | Local/mosaic dysregulation: EXT-heparan sulfate, GNAS mosaicism, RAS/MAPK, IDH1/2, hedgehog | EXT1, EXT2, GNAS, SH3BP2, PTPN11, FGFR1, ACVR1, NF1, ELMO2, TREM2/TYROBP, IDH1, IDH2, MET, KRAS, PTEN, AKT1, COL2A1, ACP5, SOX6 | **SEGMENTAL OVERGROWTH with usually SHORT overall stature** (MO/enchondromatosis). ⭐ Contains **dysplasia epiphysealis hemimelica (Trevor)** — literal epiphyseal overgrowth — and the note that PTEN is excluded because its overgrowth "is restricted to macrocephaly" | 36779427 | no |
| G31 | **Overgrowth (tall stature) syndromes and segmental overgrowth** (N=31) | Four sub-mechanisms: (i) microfibril/TGF-β release, (ii) chromatin writers/readers, (iii) imprinting & growth factors, (iv) mosaic PI3K/AKT | FBN1, FBN2, TGFBR1/2, TGFB2/3, SMAD2/3, EZH2, EED, SUZ12, NSD1, APC2, NFIX, SETD2, DNMT3A, 11p15.5, GPC3, AKT1, AKT2, PIK3CA, SMS, **NPPC**, **NPR2**, **NPR3**, **FGFR3**, PDGFRB, ACTB | **TALL — the whole group** | 36779427 | no (group) / individual entries flagged in B-list |
| G32 | **Genetic inflammatory or rheumatoid-like osteoarthropathies** (N=6) | Autoinflammation (NLRP3, IL1RN), lipin, hyaluronidase | WISP3(CCN6), NLRP3, IL1RN, LPIN2, HYAL1, ANTXR2, ASAH1 | SHORT | 36779427 | no |
| G33 | **Cleidocranial dysplasia and related disorders** (N=8) | RUNX2 dosage and its cofactor CBFB; membranous ossification | RUNX2, CBFB, RNU12, FIG4, VAC14, MSX2, ALX4, CTSK, ATP6V0A2, LMNA, NOTCH2 | Mildly SHORT | 36779427 | no |
| G34 | **Syndromes featuring craniosynostosis** (N=35) | FGFR1/2/3 GoF, TWIST1/TCF12 dosage, ERF/SMAD6 brakes, POR sterol | FGFR1, FGFR2, FGFR3, TWIST1, TCF12, **SKI**, MSX2, ERF, SMAD6, BMP2, RUNX2, RECQL4, RAB23, MEGF8, SIX1, **POR** | Variable, mostly normal/short. ⭐ Nosology explicitly cross-references **Shprintzen-Goldberg (SKI), a MARFANOID entity**, into the overgrowth group; **RAB23 (Carpenter) and MEGF8 are HPO tall-annotated** | 36779427 | **YES** (SKI/RAB23/MEGF8 arm) |
| G35 | **Craniofacial Dysostoses** (N=35) | Ribosome biogenesis (POLR1/TCOF1), spliceosome (EFTUD2/SF3B4/TXNL4A), ephrin | TCOF1, POLR1A/B/C/D, EFTUD2, SF3B4, TXNL4A, EDNRA, DHODH, PRRX1, ALX1/3/4, SIX2, TWIST1, EFNB1, ZSWIM6, EIF4A3, GNAI3, PLCB4 | Normal to short | 36779427 | no |
| G36 | **Vertebral and costal dysostoses** (N=26) | Somitogenesis clock (NOTCH/DLL3/LFNG/HES7/MESP2/RIPPLY2), TBX6 dosage | MNX1, DLL3, TBX6, MESP2, LFNG, HES7, RIPPLY2, VANGL1, CDK10, GDF6, GDF3, MEOX1, MYO18B, SNRPB, BMPER, HAAO | SHORT TRUNK. ⚠ **This is the only group whose primary lesion is axial segment number — directly relevant to trunk height, and rarely discussed in growth endocrinology** | 36779427 | **YES** |
| G37 | **Patellar dysostoses** (N=3) | TBX4/LMX1B/KAT6B limb-identity and patellar specification | TBX4, LMX1B, KAT6B, SOX9, PITX1, RECQL4 | Normal | 36779427 | **YES** (tiny, almost never discussed) |
| G38 | **Limb hypoplasia – reduction defects group** (N=42) | T-box dosage, cohesin, ZRS enhancer, RBM8A/TAR | TBX3, TBX5, TBX4, TBX15, NIPBL, SMC1A, SMC3, RAD21, HDAC8, RBM8A, THPO, SALL4, ESCO2, SHH/ZRS/LMBR1, PITX1, EN1 | Normal stature; limb segments absent | 36779427 | no |
| G39 | **Split hand/foot with and without other manifestations** (N=15) | AER maintenance; TP63; DLX5/DLX6 | TP63, CDH3, DLX5, DLX6, DYNC1I1, LBX1, BTRC, POLL, DPCD, FBXW4, WNT10B, MAP3K20(ZAK) | Normal | 36779427 | no |
| G40 | **Polydactyly-Syndactyly-Triphalangism group** (N=32) | Hedgehog gradient and GLI processing; ZRS; ciliary Hh | SHH/ZRS, **GLI1, GLI2, GLI3, SMO, SUFU, KIF7**, FBLN1, HOXD13, SALL1, FGFR2, FGFR3, FGF10, WNT6, LRP4, GREM1, FMN1, KIAA0825 | Normal stature mostly. ⭐ **GLI3, SUFU and KIF7 are HPO tall-annotated** (acrocallosal syndrome) — a hedgehog-dosage tall arm inside a "digit" group | 36779427 | **YES** |
| G41 | **Defects in joint formation and synostoses** (N=9) | BMP antagonist dosage (NOG/GDF5/GDF6), joint interzone | NOG, GDF5, GDF6, FGF9, PITX1, MACROH2A1, GSC, HOXA11, MECOM, FLNB, RFLNA, MAP3K7 | Normal to mildly short | 36779427 | **YES** |

---

## TABLE B — THE TALL / OVERGROWTH / DELAYED-BONE-AGE / DELAYED-FUSION ENUMERATION

This is the part the brief asks for exhaustively. Rows are disorder- or mechanism-level.
`BA` = bone age. Direction codes: **TALL**, **OVERGROWTH** (may be segmental), **DELAYED BA**,
**DELAYED FUSION**, **ADV BA** (recorded as a negative/control).

### B1 — Nosology Group 31 in full (all 31 entries, verbatim from the 2023 full text)

| # | ENTITY (dyadic name) | MECHANISM | GENE(S) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B01 | Marfan syndrome, FBN1-related (NOS 31–0010) | Microfibril loss → released latent TGF-β; long-bone overgrowth | FBN1 | TALL, disproportionate (dolichostenomelia) | 36779427 | no |
| B02 | Congenital contractural arachnodactyly / Beals-Hecht, FBN2-related (31–0020) | Fibrillin-2 microfibril | FBN2 | TALL, disproportionate + contractures | 36779427 | no |
| B03–B08 | **Loeys-Dietz syndrome 1–6** (31–0030…0080) | TGF-β receptor/ligand/SMAD signalling — paradoxically INCREASED tissue TGF-β signalling | TGFBR1, TGFBR2, TGFB2, TGFB3, SMAD2, SMAD3 | TALL/marfanoid; osteopenia noted for all variants | 36779427 | no |
| B09 | Weaver syndrome, EZH2-related (31–0090) | PRC2 H3K27 methyltransferase LoF | EZH2 (also NSD1, EED, SUZ12 cases) | TALL + **ADVANCED BA** | 36779427 | no |
| B10 | Cohen-Gibson (Weaver-like), EED-related (31–0100) | PRC2 core subunit | EED | TALL + ADV BA | 36779427 | **YES** |
| B11 | Imagawa-Matsumoto (Weaver-like), SUZ12-related (31–0110) | PRC2 core subunit | SUZ12 | TALL + ADV BA | 36779427; 42523552 | **YES** |
| B12 | Sotos syndrome, NSD1-related (31–0120) | H3K36 methyltransferase haploinsufficiency | NSD1 | TALL + ADV BA (childhood); adult height often normalises | 36779427 | no |
| B13 | **Sotos syndrome, APC2-related (31–0130)** | AR Sotos phenocopy; APC2 (WNT pathway) | APC2 | TALL | 36779427 | **YES** — a *recessive* Sotos, almost never cited |
| B14 | Malan (Sotos-like), NFIX-related (31–0140) | NFIX haploinsufficiency (NMD-competent alleles) | NFIX | TALL | 36779427; 20673863 | no |
| B15 | Luscan-Lumish, SETD2-related (31–0150) | H3K36me3 writer | SETD2 | TALL/overgrowth | 36779427 | **YES** |
| B16 | Tatton-Brown-Rahman, DNMT3A-related (31–0160) | de-novo DNA methyltransferase LoF | DNMT3A | TALL (**proportionate**, HP:0011407) | 36779427 | no |
| B17 | **Marshall-Smith, NFIX-related (31–0170)** | *Same gene as Malan*, NMD-escaping alleles | NFIX | **ACCELERATED skeletal maturation with FAILURE TO THRIVE** — advanced BA *dissociated* from linear growth | 36779427; 20673863 | **YES** — the cleanest human dissociation of BA from height |
| B18 | Beckwith-Wiedemann syndrome (31–0180) | 11p15.5 imprinting: IGF2 gain / CDKN1C loss / KCNQ1OT1 | 11p15.5 (IGF2, CDKN1C, KCNQ1OT1, H19) | OVERGROWTH + ADV BA | 36779427; 29377879 | no |
| B19 | Simpson-Golabi-Behmel, GPC3-related (31–0190) | Glypican-3 loss → unrestrained IGF/hedgehog/BMP at the cell surface | GPC3 (also GPC4) | OVERGROWTH, prenatal onset | 36779427; 8589713 | no |
| B20 | Proteus syndrome, AKT1-related (31–0200) | Mosaic AKT1 p.E17K | AKT1 (mosaic) | SEGMENTAL OVERGROWTH, progressive | 36779427 | no |
| B21 | **Hypoinsulinemic hypoglycemia with hemihypertrophy, AKT2-related (31–0210)** | AKT2 activating variant | AKT2 | SEGMENTAL OVERGROWTH | 36779427 | **YES** |
| B22 | CLOVES / PROS, PIK3CA-related (31–0220) | Mosaic PI3K activation | PIK3CA (mosaic) | SEGMENTAL OVERGROWTH | 36779427 | no |
| B23 | Fibroadipose hyperplasia, PIK3CA-related (31–0230) | as above | PIK3CA (mosaic) | SEGMENTAL OVERGROWTH | 36779427 | no |
| B24 | Snyder-Robinson, SMS-related (31–0240) | Spermine synthase LoF → spermidine/spermine ratio ↑ | SMS | ⚠ **The Nosology labels this "tall stature"** (with ID, osteoporosis, fractures) and HPO annotates HP:0001519 disproportionate tall stature. Much of the clinical literature emphasises asthenic build and *short* stature — **DIRECTION CONTESTED, recorded as such** | 36779427; HPO OMIM:309583 | **YES** |
| B25 | **Overgrowth syndrome with 2q37 translocations (31–0250)** | Position effect → **overexpression of NPPC (CNP)** | NPPC | TALL — the *ligand-gain* arm of the CNP axis | 36779427 | **YES** |
| B26 | **Tall stature with long halluces, NPR2-related (31–0260)** = epiphyseal chondrodysplasia, Miura type | **Monoallelic GAIN-of-function NPR2** → ↑cGMP | NPR2 | TALL | 36779427; 24259409; 32282051 | **YES** |
| B27 | **Tall stature with long halluces, NPR3-related (31–0270)** = Boudin-Mortier syndrome | **Biallelic LoF of the CNP CLEARANCE receptor** | NPR3 | TALL | 36779427; 35233476; 40171685 | **YES** |
| B28 | **Moreno-Nishimura-Schmidt syndrome (31–0280)** | Unknown; sporadic | *no gene assigned* | Overgrowth/tall | 36779427 | **YES** |
| B29 | **CATSHL — camptodactyly, tall stature, hearing loss, FGFR3-related (31–0290)** | **FGFR3 LOSS of function** (dominant-negative in the original family; a 2nd family biallelic) | FGFR3 | **TALL** — the human germline validation that lowering FGFR3 lengthens bone | 36779427; 27139183; 37990933 | **YES** |
| B30 | Kosaki overgrowth syndrome, PDGFRB-related (31–0300) | PDGFRB activating variants (allelic to Penttinen) | PDGFRB | OVERGROWTH, progressive | 36779427; 41223009 | **YES** |
| B31 | Segmental odontomaxillary dysplasia, ACTB-related (31–0310) | Mosaic ACTB | ACTB (mosaic) | SEGMENTAL OVERGROWTH | 36779427 | **YES** |

### B2 — TALL / OVERGROWTH / DELAYED-BONE-AGE ENTITIES **OUTSIDE** NOSOLOGY GROUP 31

Gene assignments in this section were verified individually against the **HPO public API**
(`ontology.jax.org/api/network/annotation/<OMIM|ORPHA id>`), which returns the curated gene(s) for
each disease record. Where the API returned no gene, I say so rather than guessing.

#### B2a — CHROMATIN / EPIGENETIC OVERGROWTH (the "epigenetic overgrowth" class)

| # | ENTITY | MECHANISM | GENE(S) (HPO-verified) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B32 | **Rahman syndrome** (H1-4 / HIST1H1E) | **LINKER histone H1.4** C-terminal frameshift — not a core histone, not a writer | H1-4 (HIST1H1E) | OVERGROWTH in childhood; ⚠ growth pattern paper reports height **normalises/decelerates** with age, and cases with SHORT stature + hypopituitarism exist | 29383847; 40444808; 37362168 | **YES** |
| B33 | **Bryant-Li-Bhoj neurodevelopmental syndrome 2** | H3.3 variant histone (H3-3B/H3F3B) | H3-3B | TALL / OVERGROWTH | HPO OMIM:619721; 40241305 | **YES** |
| B34 | **Stolerman neurodevelopmental syndrome** | **KDM6B** — H3K27 DEMETHYLASE (the eraser opposite EZH2) | KDM6B | **PROPORTIONATE TALL (HP:0011407)** | 37196654; HPO OMIM:618505 | **YES** — the eraser arm of PRC2 |
| B35 | **KDM2B-related NDD with cardiac/renal/ocular anomalies** | H3K36/H3K4 demethylase, PRC1.1 component | KDM2B | OVERGROWTH | HPO OMIM:621474 | **YES** |
| B36 | **Rabin-Pappas syndrome** & IDD70 | SETD2 (H3K36me3 writer) — *different* alleles from Luscan-Lumish | SETD2 | OVERGROWTH (Rabin-Pappas is the severe end) | HPO OMIM:620155/620157 | **YES** |
| B37 | **Bainbridge-Ropers syndrome** | ASXL3 — PR-DUB/BAP1 deubiquitinase complex | ASXL3 | **Disproportionate TALL** (HP:0001519) | HPO OMIM:615485 | **YES** — usually filed as failure-to-thrive, the tall annotation is unexpected |
| B38 | **Kleefstra syndrome 1** | EHMT1 (G9a-like, H3K9me2 writer) | EHMT1 | TALL / OVERGROWTH annotated | HPO OMIM:610253 | **YES** |
| B39 | **Tenorio syndrome** | RNF125 — RING E3 ubiquitin ligase; overgrowth + macrocephaly + ID + immune | RNF135? ⚠ **The disease-causing gene is RNF125** (PMID 25196541); HPO returns **RNF135** for the *Overgrowth-macrocephaly-facial dysmorphism* record ORPHA:137634 — these are **two different genes and two different syndromes**, easily conflated | OVERGROWTH | 25196541; 34196401; 37986019 | **YES** |
| B40 | **RNF135-related overgrowth-macrocephaly-facial dysmorphism** | RNF135 sits inside the NF1 microdeletion interval on 17q11.2 | RNF135 | OVERGROWTH | HPO ORPHA:137634 / OMIM:613675 | **YES** |
| B41 | **CHD8-related macrocephaly/autism** | ATP-dependent chromatin remodeller; also a WNT/β-catenin brake | CHD8 | TALL/overgrowth; CHD8 pLoF is one of the largest human height-increasing burden effects | 40577202 (as candidate in tall-stature cohort) | no |
| B42 | **KDM4A** (candidate) | H3K9me3/H3K36me3 demethylase | KDM4A | TALL — **candidate**, same rare missense in 2 unrelated syndromic-tall patients | 40577202 | **YES** |
| B43 | **Lui-Jee-Baron syndrome (SPIN4)** | **SPIN4 — an epigenetic READER (Tudor domain), X-linked**, lowers baseline canonical WNT | SPIN4 | **OVERGROWTH / TALL** | 36927955; 41780720; 41158422 | **YES** — new (2023), 3 families |
| B44 | **CIC-related IDD45** | Capicua, HMG-box transcriptional repressor downstream of RTK/ERK | CIC | TALL | HPO OMIM:617600 | **YES** |
| B45 | **SRRM2 / TAF4 / RNU2-2 / KLHL20 / LRRC7 / MSL2 NDDs** | Spliceosome (SRRM2), general TF (TAF4), snRNA (RNU2-2), CUL3 adaptor (KLHL20), synaptic (LRRC7), MSL histone-acetylation complex (MSL2 = Basilicata-Akhtar) | SRRM2, TAF4, RNU2-2, KLHL20, LRRC7, MSL2 | TALL annotated (TAF4 also delayed skeletal maturation) | HPO OMIM:620439/620450/621304/621390/621415/620985 | **YES** — none appears in the growth literature |

#### B2b — IMPRINTING AND GROWTH-FACTOR DOSAGE

| # | ENTITY | MECHANISM | GENE(S) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B46 | Beckwith-Wiedemann spectrum | 11p15.5: IGF2 gain-of-dosage / CDKN1C loss / KCNQ1OT1 IC2 LOM / patUPD | IGF2, CDKN1C, KCNQ1OT1, H19 | OVERGROWTH + **ADVANCED BA** | 29377879 | no |
| B47 | **Kagami-Ogata syndrome** (14q32.2 patUPD / matDeletion / epimutation) | The **DLK1-DIO3 imprinted locus**: RTL1 overexpression, MEG3/MEG8 loss | RTL1, MEG3 (region-level) | OVERGROWTH (fetal), coat-hanger ribs; the **mirror** of Temple syndrome (short) | 32592473; 34055463; 38741340 | **YES** in a growth context |
| B48 | Simpson-Golabi-Behmel type 1 | GPC3 loss → glypican no longer sequesters IGF2/Hh/BMP at the cell surface | GPC3 (also GPC4) | OVERGROWTH, prenatal | 8589713; 25238977 | no |
| B49 | **Perlman syndrome** | DIS3L2 — 3'→5' exoribonuclease acting on **let-7-uridylated** RNAs (LIN28/let-7 axis) | DIS3L2 | Fetal OVERGROWTH, nephroblastomatosis, high lethality | HPO ORPHA:2849; 42040973 | **YES** — the only human disease directly on the LIN28/let-7 RNA-turnover arm |
| B50 | **15q26 duplication / "15q overgrowth syndrome"** | **IGF1R DUPLICATION** (dosage gain of the receptor) | IGF1R (region) | TALL/OVERGROWTH; the reciprocal 15q26 deletion gives IUGR + short | 42130906; 28899882 | **YES** |
| B51 | 17p13.3 duplication syndrome | YWHAE/PAFAH1B1 dosage | YWHAE, PAFAH1B1 (region) | TALL annotated | HPO OMIM:613215 / ORPHA:217385 | **YES** |
| B52 | **DLK1 / MKRN3 loss → central precocious puberty** | Imprinted hypothalamic brakes on GnRH; loss = early puberty | DLK1, MKRN3 | TALL as a CHILD, **ADVANCED BA, reduced adult height** — the classic "trade" | 38715103 (DLK1 deletion/Temple) | no |

#### B2c — PI3K / AKT / mTOR / RAS — MOSAIC AND GERMLINE

| # | ENTITY | MECHANISM | GENE(S) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B53 | PTEN hamartoma tumour syndrome / BRRS / macrocephaly-autism | PTEN loss → PI3K/AKT | PTEN | Macrocephaly + tall in childhood; **the Nosology deliberately EXCLUDES PTEN from group 30 "because the overgrowth is restricted to macrocephaly"** — a stated editorial judgement worth knowing | 36779427; HPO OMIM:605309; 40577202 | no (but the exclusion note is) |
| B54 | **MPPH syndrome** (megalencephaly-polymicrogyria-polydactyly-hydrocephalus) | PIK3R2 (p85β) activating; also AKT3, CCND2 | PIK3R2 | OVERGROWTH (brain-predominant) | HPO OMIM:603387 | **YES** |
| B55 | MCAP (megalencephaly-capillary malformation) | mosaic PIK3CA | PIK3CA | SEGMENTAL OVERGROWTH | HPO OMIM:602501 | no |
| B56 | Costello syndrome | HRAS germline activating | HRAS | ⚠ HPO annotates **TALL + OVERGROWTH + delayed skeletal maturation** (fetal overgrowth), yet postnatal stature is short — a **direction-flip across life stages**, worth recording as such | HPO OMIM:218040 | **YES** (the flip) |
| B57 | **STRADA (PMSE / polyhydramnios-megalencephaly-symptomatic epilepsy)** | STRADA-LKB1-AMPK → mTORC1 de-repression | STRADA | OVERGROWTH/TALL | HPO OMIM:611087 | **YES** |
| B58 | **DEPDC5** (candidate in syndromic tall stature) | GATOR1 — the amino-acid brake on mTORC1; loss raises mTORC1 | DEPDC5 | TALL (in a syndromic-tall exome cohort) | 40577202 | **YES** |

#### B2d — SEX STEROID / SEX CHROMOSOME — **THE DELAYED-FUSION CLASS** ⭐

This is the highest-value block for a "keep the plate open" question, and almost none of it is in the
Nosology (it is endocrine, not dysplastic).

| # | ENTITY | MECHANISM | GENE(S) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B59 | **Aromatase deficiency (CYP19A1)** | No oestrogen synthesis → epiphyses never receive the fusion signal | CYP19A1 | **TALL + DELAYED BA + UNFUSED EPIPHYSES INTO ADULTHOOD, growth continues** | 36504506; 41908849; 24485503 | no (but under-used) |
| B60 | **Oestrogen resistance / insensitivity (ESR1)** | Receptor-level; the only gene carrying **HP:0003799 "MARKED delay in bone age"** | ESR1 | TALL + **MARKED DELAYED BA + delayed fusion** | 32242619; 35134944; 32152632 | no |
| B61 | ⭐ **17α-hydroxylase/17,20-lyase deficiency (CYP17A1, "CYP17D")** | Combined block of adrenal *and* gonadal sex-steroid synthesis | CYP17A1 | **BA delayed ≥2 y in 92.5% of 88 patients; EXTENDED GROWTH PHASE; 39% of final heights ≥90th centile; eunuchoid proportions** — the LARGEST human cohort of pharmacological-grade sex-steroid absence with a bone-age endpoint | **40350803** | **YES — highest-value single row in this file** |
| B62 | **Congenital hypogonadotropic hypogonadism / Kallmann** (HP:0003782 eunuchoid habitus) | No gonadal steroid → prolonged growth, eunuchoid proportions | ANOS1, FGFR1, FGF8, FGF17, GNRH1, GNRHR, KISS1, KISS1R, TAC3, TACR3, PROK2, PROKR2, CHD7, HS6ST1, NSMF, SPRY4, WDR11, DUSP6, NHLH2 (all HPO-verified under HP:0003782) | TALL/eunuchoid, DELAYED BA, DELAYED FUSION | HPO HP:0003782 | no individually / **YES** as a systematic growth lever |
| B63 | **Complete androgen insensitivity (AR)** | 46,XY with no androgen action but intact aromatisation | AR | Adult height intermediate between male and female norms; **delayed-ish fusion** | HPO ORPHA:99429; 41163677 | no |
| B64 | **46,XY / 46,XX sex reversal (SRY)** | SRY — in HPO the *only* gene under both tall stature AND delayed skeletal maturation in the sex-determination arm | SRY | TALL + DELAYED BA | HPO OMIM:400044/400045 | **YES** |
| B65 | **Sex-chromosome aneuploidy: 47,XXY (Klinefelter), 47,XYY, 47,XXX, 48,XXYY, 48,XXXY, 48,XYYY** | Extra **SHOX** copies in PAR1 + hypogonadism (in XXY) | SHOX dosage (region); HPO returns no single gene | TALL. **Klinefelter is the single commonest primary cause of childhood tall stature in a population cohort (1/2146 boys)** | 40233073; 40388606 | no |
| B66 | **Xp22.33 / PAR1 duplication encompassing SHOX** | SHOX **over**dosage without aneuploidy | SHOX | TALL | 41751622; 41683999 | **YES** |
| B67 | **Familial male-limited precocious puberty (LHCGR activating)** | Constitutive LH receptor → early androgen/oestrogen | LHCGR | TALL as child, **ADVANCED BA**, short adult | HPO ORPHA:3000 | no |
| B68 | **Congenital adrenal hyperplasia, 21-OH deficiency (CYP21A2)** | Androgen excess | CYP21A2 | TALL child, ADVANCED BA, short adult | HPO ORPHA:90794; 40269793 | no |
| B69 | ⭐ **Familial glucocorticoid deficiency (MC2R, MRAP, NNT, TXNRD2, STAR)** | Cortisol absence + high ACTH | MC2R, MRAP, NNT, TXNRD2, STAR (HPO tall list) | **TALL** — the human loss-of-function arm of the glucocorticoid axis | HPO ORPHA:361 | **YES** |
| B70 | **Severe untreated primary hypothyroidism (Van Wyk-Grumbach)** | TSH cross-activating FSHR; pituitary hyperplasia; macroorchidism | TSHR, TSHB, TG, TPO, DUOX2, SLC5A5, IYD (all under HP:0002663 delayed epiphyseal ossification) | **EXTREME DELAYED BA with SHORT stature** — the standard demonstration that delayed BA alone does not buy height | 41948356 | no |
| B71 | ⚠ **Transgender girls on GnRH analogue + oestradiol** | Iatrogenic manipulation of the fusion signal in otherwise normal plates | — (iatrogenic) | **Adult height UNAFFECTED** — a directly relevant human negative for "delay the fusion signal → gain height" | 35666195 | **YES** |

#### B2e — GH / IGF-1 AXIS GIGANTISM (rate, not period)

| # | ENTITY | MECHANISM | GENE(S) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B72 | **X-linked acrogigantism (X-LAG)** | **Xq26.3 microduplication → GPR101 gain** — infantile-onset GH excess | GPR101 (HPO-verified on OMIM:300942) | **TALL — produces the tallest recorded humans**; onset in INFANCY | HPO OMIM:300942; 37891382 | no |
| B73 | Familial isolated pituitary adenoma / pituitary gigantism | AIP loss (also MEN1) | AIP, MEN1 | TALL | HPO ORPHA:99725 | no |
| B74 | MEN1 / MEN4 | MEN1; **CDKN1B (p27) and CDKN2B** | MEN1, CDKN1B, CDKN2B | Proportionate TALL annotated | HPO ORPHA:652 | **YES** (the CDKN link) |
| B75 | Carney complex | PRKAR1A (also PDE11A) — PKA de-repression | PRKAR1A, PDE11A | TALL/acromegalic; macroorchidism | HPO ORPHA:1359 | no |
| B76 | McCune-Albright | mosaic GNAS activating | GNAS | ADVANCED BA + macroorchidism; GH excess in a subset | HPO (HP:0005616, HP:0000053) | no |
| B77 | ⭐ **"Growth without GH"** | Normal or TALL adult height reached despite severe GHD and persistently low IGF-1; obesity/hyperinsulinaemia present in all | — (acquired/congenital GHD) | **TALL despite absent GH**; one case with lifelong hypogonadism showed **slow prolonged growth with DELAYED EPIPHYSEAL FUSION** | **41464859** | **YES** |
| B78 | ⭐ **Insulin-mediated pseudoacromegaly / severe insulin resistance** | Selective post-receptor insulin resistance — mitogenic arm spared | ABCC8 (reported); FGF21-pathway digenic variants | Acral/soft-tissue OVERGROWTH without GH excess | 33210059; 34792134; 38549284 | **YES** |

#### B2f — CONNECTIVE TISSUE / MARFANOID (outside group 31)

| # | ENTITY | MECHANISM | GENE(S) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B79 | **Homocystinuria (CBS)** and remethylation defects | Homocysteine disrupts fibrillin/collagen cross-linking | CBS | **TALL, marfanoid, disproportionate** — and treatment prevents it | HPO OMIM:236200 | no |
| B80 | MASS phenotype; familial ectopia lentis; MVP1 | FBN1 alleles milder than Marfan | FBN1 | TALL/marfanoid | HPO OMIM:604308/129600 | no |
| B81 | Familial thoracic aortic aneurysm 9/10/12 | MFAP5, LOX, THSD4 (HPO tall list) | MFAP5, LOX, THSD4 | Disproportionate TALL | HPO OMIM:616166/617168/619825 | **YES** |
| B82 | **Kyphoscoliotic EDS type 1 (PLOD1) = Nevo syndrome** | **Lysyl hydroxylase 1** — Nevo syndrome (overgrowth + kyphoscoliosis) is ALLELIC to kEDS | PLOD1 | Disproportionate TALL / OVERGROWTH | 15666309; HPO OMIM:225400 | **YES** |
| B83 | kEDS type 2 (FKBP14 / FKBP22) | Collagen chaperone/PPIase | FKBP14 | Disproportionate TALL | HPO ORPHA:300179 | **YES** |
| B84 | Musculocontractural EDS; cardiac-valvular EDS; periodontal EDS | CHST14/DSE (dermatan sulfate epimerase-transferase); COL1A2; C1R | CHST14, DSE, COL1A2, C1R | TALL/marfanoid annotated | HPO ORPHA:2953/230851/OMIM:130080 | **YES** |
| B85 | Brittle cornea syndrome | ZNF469 (also PRDM5) | ZNF469 | Disproportionate TALL | HPO OMIM:229200 | **YES** |
| B86 | Cutis laxa AR types IA/IB/ID/IIC/IID | FBLN5, EFEMP2 (FBLN4), LTBP4, ATP6V1A, ATP6V1E1 — elastic-fibre assembly | FBLN5, EFEMP2, ATP6V1A, ATP6V1E1 | TALL/OVERGROWTH annotated | HPO OMIM:219100/614437/617402/617403 | **YES** |
| B87 | **Camurati-Engelmann disease (TGFB1)** | Constitutively activating TGFB1 — releases active TGF-β from LAP | TGFB1 | TALL/marfanoid habitus with diaphyseal hyperostosis | HPO OMIM:131300 | **YES** — a *gain* of TGF-β that is tall, the opposite of the usual reading |
| B88 | Shprintzen-Goldberg syndrome (SKI) | SKI = SMAD co-repressor; cross-listed by the Nosology into group 31 | SKI | Marfanoid | 36779427 | no |
| B89 | Stickler syndrome type I (COL2A1) | Type II collagen | COL2A1 | ⚠ TALL/marfanoid habitus annotated in HPO **inside a short-stature collagen group** | HPO OMIM:108300 | **YES** |
| B90 | Marfan lipodystrophy syndrome / neonatal progeroid FBN1 | 3'-end FBN1 alleles disrupting the **asprosin**-encoding exons | FBN1 | TALL + lipodystrophy | HPO OMIM:616914 | **YES** |

#### B2g — HEDGEHOG / CILIARY (tall arm)

| # | ENTITY | MECHANISM | GENE(S) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B91 | **Acrocallosal syndrome** | GLI3 / KIF7 — hedgehog transduction and GLI processing | GLI3, KIF7 | **TALL annotated** | HPO ORPHA:36 | **YES** |
| B92 | **Joubert syndrome 32 (SUFU)** | SUFU = the intracellular GLI brake | SUFU | TALL annotated | HPO OMIM:617757 | **YES** |
| B93 | **PTCH1 whole-gene deletion in syndromic tall stature** | Loss of the hedgehog receptor-brake | PTCH1 | TALL — found by exome/CMA in a syndromic-tall cohort. ⚠ **Direction contested**: PTCH1 also carries HP:0005616 accelerated skeletal maturation, and population burden data for PTCH1 pLoF are in the *shortening* direction | 40577202 | **YES** |
| B94 | ⭐ **Non-syndromic familial tall stature with an OLIGOGENIC ciliary-gene burden** | Multiple ciliary genes co-segregating; **IFT140** and **NAV2** both expressed in the growth plate and both falling from proliferative → hypertrophic zone (mouse) | IFT140, NAV2, SCAF11 (candidates) | TALL | **34194391; 38152138** | **YES** |

#### B2h — HIGH BONE MASS / WNT (tall arm)

| # | ENTITY | MECHANISM | GENE(S) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B95 | ⭐ **Sclerosteosis 1 (SOST biallelic LoF)** | Loss of the secreted WNT antagonist sclerostin | SOST (HPO-verified OMIM:269500); allelic sclerosteosis 2 = LRP4 | **TALL + OVERGROWTH** (classic gigantism with syndactyly) | HPO OMIM:269500; 24019634; 35052419 | **YES** — the human tall arm of the SOST/romosozumab axis |
| B96 | Van Buchem disease | SOST **enhancer** deletion (regulatory, milder) | SOST (regulatory) | Bone overgrowth; stature usually normal — **the dose-response counterpart of B95** | 32328030 (review, index only) | **YES** |
| B97 | ⭐ **Primary hypertrophic osteoarthropathy / pachydermoperiostosis** | **HPGD (15-PGDH) or SLCO2A1** loss → PROSTAGLANDIN E2 accumulation | HPGD (HPO-verified OMIM:259100), SLCO2A1 | **TALL annotated**, acral overgrowth, periostosis, delayed suture closure | HPO OMIM:259100; 39659384; 39878145 | **YES** — the only human PGE2-degradation lesion with a stature annotation |

#### B2i — METABOLIC, LYSOSOMAL, MITOCHONDRIAL, OTHER

| # | ENTITY | MECHANISM | GENE(S) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B98 | **α-mannosidosis, infantile form (MAN2B1)** | Lysosomal α-mannosidase | MAN2B1 | ⚠ **TALL + increased vertebral height** annotated inside a dysostosis-multiplex disorder — I could not reconcile this with the usual clinical description and record it as an HPO annotation, not as a verified phenotype | HPO ORPHA:309282 | **YES** |
| B99 | Congenital generalized lipodystrophy 1/2 (AGPAT2, BSCL2) | Absent adipose → hyperinsulinaemia | AGPAT2, BSCL2 | **TALL child + ACCELERATED BA** | HPO OMIM:608594/269700 | **YES** |
| B100 | MC4R deficiency (and LEP/LEPR) | Melanocortin-4 receptor; hyperinsulinaemia | MC4R (HPO tall + accelerated maturation) | TALL child, accelerated growth and BA | HPO OMIM:618406; 40246357 | no |
| B101 | GABA-transaminase deficiency (ABAT) | GABA catabolic block | ABAT | TALL annotated in HPO. ⚠ "Accelerated linear growth" is widely repeated for this disorder but **I could not verify it in a primary source this round — treat as UNVERIFIED** | HPO OMIM:613163; phenotype reviews 28411234, 27376954 (not read in full) | **YES** |
| B102 | Mitochondrial: MNGIE (TYMP), POLG, DNA2, LARS2/Perrault, TIMM50, NNT, TXNRD2 | Various mitochondrial | TYMP, POLG, DNA2, LARS2, TIMM50 | TALL annotated (usually thin/asthenic habitus) | HPO HP:0000098 set | **YES** |
| B103 | CK syndrome / CHILD (NSDHL) | Post-squalene cholesterol biosynthesis; sterols are SMO ligands | NSDHL | TALL annotated | HPO OMIM:300831 | **YES** |
| B104 | CHIME syndrome (PIGL); MCAHS2 / PIGA; PIGG-related | **GPI-anchor biosynthesis** — 4 independent GPI genes carry tall/overgrowth annotations | PIGL, PIGA, PIGG, PIGV | TALL/OVERGROWTH; PIGG also delayed skeletal maturation | HPO ORPHA:3474; OMIM:300868 | **YES** — a whole pathway invisible to the growth literature |
| B105 | **DICER1 — "GLOW" syndrome** (global developmental delay, lung cysts, overgrowth, Wilms tumour) | miRNA processing | DICER1 | OVERGROWTH | HPO OMIM:618272 | **YES** — miRNA-processing overgrowth |
| B106 | **PTBP1 — STAD syndrome** | Polypyrimidine tract binding protein 1; splicing | PTBP1 | TALL + accelerated skeletal maturation | HPO OMIM:621495 | **YES** |
| B107 | **HECTD4-related NDD** | HECT E3 ligase | HECTD4 | TALL/OVERGROWTH | HPO OMIM:620250 | **YES** |
| B108 | **NONO-related X-linked ID / LVNC** | Paraspeckle protein | NONO | TALL | HPO OMIM:300967; ORPHA:466791 | **YES** |
| B109 | **FIBP — Thauvin-Robinet-Faivre syndrome** | FGF1 intracellular binding protein; AR; overgrowth + Wilms predisposition | FIBP | **TALL/OVERGROWTH (proportionate)** | 26660953; 27183861; 40536757 | **YES** |
| B110 | **HERC1 — MDFPMR / megalencephaly-kyphoscoliosis-overgrowth** | Giant HECT E3 ligase; mTOR/RAS interactions | HERC1 | **Disproportionate TALL + OVERGROWTH** | HPO OMIM:617011; 39891458 | **YES** |
| B111 | Nemaline/centronuclear/other congenital myopathies (ACTA1, NEB, TPM2, TPM3, TNNT1, KBTBD13, KLHL41, MYPN, MTM1, PYROXD1, TRIM32) | Muscle — asthenic elongated habitus | as listed (HPO tall set) | TALL annotated. ⚠ Most plausibly **reduced mechanical loading / reduced muscle mass**, not a plate lever — but as a class it is a systematic "low muscle → tall" signal | HPO HP:0000098 set | **YES** |
| B112 | **Muscular hypotonia as a general tall-stature route** | see B111 | — | Hypothesis, **UNVERIFIED** as a mechanism | — | **YES** |

#### B2j — CHROMOSOMAL / CNV OVERGROWTH (the group the Nosology largely omits)

| # | ENTITY | MECHANISM | GENE(S) | HEIGHT DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B113 | ⭐ **7q22.2-q22.3 microdeletion with overgrowth AND DELAYED BONE AGE** | 3.2 Mb de novo deletion; candidate cell-cycle genes SRPK2, KMT2E(MLL5), RINT1, LHFPL3 | region (SRPK2, KMT2E, RINT1, LHFPL3 proposed) | **OVERGROWTH + DELAYED BA** — one of very few entities with BOTH | **20219702** | **YES — the exact combination the atlas wants** |
| B114 | Distal duplication 15q / triplication 15q | includes IGF1R | region | TALL/OVERGROWTH | HPO ORPHA:1707/314588 | **YES** |
| B115 | 2p15p16.1 microdeletion; 5q12 deletion; 19p13.13 deletion; 9q21.3 microdeletion; 16p11.2 220-kb deletion; Xq25 duplication; monosomy 18q; monosomy 9q22.3 (PTCH1); mosaic trisomy 8; Wolf-Hirschhorn (NSD2); Phelan-McDermid (SHANK3) | Contiguous-gene dosage | region | TALL annotated | HPO HP:0000098 set | **YES** |
| B116 | **"Cytogenetic anomalies are the predominant genetic alteration in non-familial tall stature"** | Population-level finding, not a syndrome | — | TALL | **40524006** | **YES** — reframes the diagnostic order of operations |

#### B2k — ENTITIES DEFINED BY DELAYED BONE AGE / DELAYED EPIPHYSEAL OSSIFICATION

| # | ENTITY | MECHANISM | GENE(S) (HPO HP:0002663 / HP:0003799) | DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B117 | **HP:0003799 "Marked delay in bone age" — the ENTIRE annotated gene set is TWO genes** | — | **ESR1, LHX4** (diseases: estrogen resistance; CPHD4; epiphyseal dysplasia Baumann type; HH-microcephaly-deafness; primary hypergonadotropic hypogonadism-partial alopecia) | DELAYED BA | HPO HP:0003799 | **YES** — the ontology's near-emptiness here is itself the finding |
| B118 | **"Epiphyseal dysplasia, Baumann type"** | Unknown; annotated with marked delay in bone age | HPO returns **no gene** | DELAYED BA | HPO HP:0003799 record; **could not find a primary paper — UNVERIFIED** | **YES** |
| B119 | HP:0002663 "Delayed epiphyseal ossification" gene set (42 genes) | Mixed: thyroid dyshormonogenesis (TG, TPO, TSHR, TSHB, SLC5A5, DUOX2, DUOXA2, IYD), pituitary (POU1F1, PROP1, LHX3, LHX4, HESX1), vitamin D (VDR, CYP2R1, CYP27B1, SLC34A3, CLCN5), sex steroid (**CYP19A1, ESR1**), cartilage (COL2A1, COL9A3, COMP, MATN3, MIR140, SOX9, TRPV4, KIF22, PTH1R, B3GALT6, INPPL1, PISD, GPX4, RNU4ATAC, DDRGK1, IARS2, LONP1, PAM16, TONSL, KCNH1, FGFR2, KIF7) | DELAYED epiphyseal ossification | HPO HP:0002663 | no (individually) / **YES** as a set |
| B120 | ⭐ **The structural point: of 370 genes under HP:0002750 (delayed skeletal maturation) and 227 under tall/overgrowth, only 27 genes appear in BOTH** | — | **CDKN1C, COL2A1, CPLX1, CTBP1, CYP19A1, DNA2, ELN, ESR1, FARSB, FBN1, FBXO11, HRAS, HSPG2, IGF2, KRAS, LETM1, NELFA, NPR2, NRAS, NSD1, NSD2, PDGFRB, PIGG, PTEN, SMAD4, SRY, TAF4** | **TALL *AND* DELAYED BA** | computed from HPO API, 2026-08-15 | **YES — this intersection is, as far as I can tell, unpublished** |

#### B2l — NEGATIVE CONTROLS (recorded because negatives are part of the map)

| # | ENTITY | MECHANISM | GENE(S) | DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B121 | Short stature with **ADVANCED** bone age, ACAN-related (NOS 07–0050) | Aggrecan haploinsufficiency | ACAN | SHORT + ADV BA | 36779427 | no |
| B122 | **Skeletal dysplasia with joint laxity and ADVANCED bone age (SDJLABA), CSGALNACT1-related** (NOS 05–0090) | Chondroitin sulfate chain initiation | CSGALNACT1 | SHORT + ADV BA | 36779427 | **YES** |
| B123 | **Marshall-Smith syndrome (NFIX)** | see B17 | NFIX | **ACCELERATED BA + FAILURE TO THRIVE** | 20673863 | **YES** |
| B124 | **HP:0005616 "Accelerated skeletal maturation" — 69 genes** | The mirror set; every overgrowth-with-advanced-BA syndrome sits here | ABCC9, ACAN, AIP, ALMS1, AMOTL1, APC2, ARCN1, ASXL2, B3GAT3, B4GALT7, BSCL2, CANT1, CAVIN1, CDKN1C, CHST3, CSGALNACT1, CYP11B1, CYP19A1, DDOST, DDX6, EED, EFEMP1, EZH2, GLI3, GNAS, GPC3, GPC4, GPR101, GPX4, GUSB, H1-4, HSD11B1, IGF2, INPPL1, INSR, KCNJ8, KCNQ1, KCNQ1OT1, KMT2A, LEP, LEPR, LHCGR, MC2R, MC4R, MEN1, MKRN3, NFIX, NSD1, PDE4D, PRKAR1A, PRKG2, PSMD12, PTBP1, PTCH1, PTH1R, RMRP, RNF135, SLC10A7, SLC26A2, SLC35D1, SMARCA2, SUZ12, TCF20, TET3, TRPS1, TSHR, UBE3C, XYLT1 | ADVANCED BA | HPO HP:0005616 | **YES** as a set |
| B125 | ⭐ **AMOTL1 — orofacial clefting, cardiac anomalies and TALL STATURE** | **Angiomotin-like 1 — a HIPPO/YAP pathway component**; recurrent hotspot | AMOTL1 | **TALL + accelerated skeletal maturation** | **36751037; 42012498** | **YES — a human TALL-stature gene in the Hippo pathway** |
| B126 | **Cantu syndrome (ABCC9 / KCNJ8)** | K-ATP channel gain-of-function | ABCC9, KCNJ8 | Macrosomia at birth + **accelerated skeletal maturation**; adult stature not clearly tall | HPO HP:0005616 | **YES** |
| B127 | ⚠ **Dyssegmental dysplasia Silverman-Handmaker (HSPG2)** appears under TALL in HPO | Perlecan LoF | HSPG2 | This is a **lethal short-limb dysplasia**; the tall annotation almost certainly derives from a vertebral/segmental descriptor. **Recorded as a likely HPO annotation artefact** | HPO OMIM:224410 | **YES** (as a caution) |
| B128 | **Elejalde syndrome (acrocephalopolydactylous dysplasia)** | Unknown; lethal fetal overgrowth. ⚠ **Name collision**: a *different* "Elejalde syndrome" is the neuroectodermal melanolysosomal disease (MYO5A/Griscelli-related) | none assigned | OVERGROWTH (lethal) | 890100; 21164339; 22413886 | **YES** |
| B129 | **Hydrocephalus, tall stature, joint laxity and kyphoscoliosis (OMIM 236660)** | Unknown | HPO returns **no gene** | TALL | HPO OMIM:236660 / ORPHA:2181 | **YES** |
| B130 | **MOMO syndrome** (macrosomia, obesity, macrocephaly, ocular abnormalities) | Unknown; one case resolved to a 3q13.2q21.2 microdeletion | none assigned | OVERGROWTH | 8322820; 22821547; 39634243 | **YES** |
| B131 | **Fryns-Smeets-Thiry; Giacheti; Moreno-Nishimura-Schmidt; Sillence syndrome; Thoracolaryngopelvic dysplasia; Microcephaly-glomerulonephritis-marfanoid habitus; Marfanoid habitus with situs inversus** | Unknown; all HPO tall-annotated with **no gene assigned** | none | TALL | HPO HP:0000098 set | **YES — the unsolved tail of the tall-stature space** |
| B132 | **Progressive non-infectious anterior vertebral fusion (Copenhagen syndrome)** | Idiopathic anterior fusion of vertebral bodies in children — an acquired/idiopathic **AXIAL FUSION** phenotype with no gene | none | Trunk growth arrest | 11858144; 16328382; 37408023 | **YES** |

#### B2m — CANDIDATE / EMERGING GENES FOR TALL STATURE (not yet disease genes)

| # | CANDIDATE | MECHANISM | GENE | DIRECTION | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|---|
| B133 | ⭐ **SST (somatostatin) whole-gene deletion** | Loss of the endogenous GH-release brake | SST | TALL — found by CMA in a syndromic-tall patient | **40577202** | **YES** — an obvious mechanism nobody had a human allele for |
| B134 | ⭐ **GRB10 (imprinted growth suppressor)** | Adaptor that dampens IGF1R/INSR signalling; imprinted; regulates fetal growth **independently of IGF1R/INSR** in mouse | GRB10 | TALL — candidate | **40577202**; mouse mechanism 38816743; bone-growth variant 38871555 | **YES** |
| B135 | **CDH8** | Cadherin-8 | CDH8 | TALL — P/LP variant in syndromic-tall cohort | 40577202 | **YES** |
| B136 | **NAV2** | Neuron navigator 2; growth-plate expressed, falls proliferative→hypertrophic (mouse) | NAV2 | TALL — familial isolated tall stature, 211 cm proband | **38152138** | **YES** |
| B137 | **IFT140, SCAF11** | Ciliary IFT-A; SR-related splicing factor. Both height-associated in GWAS and growth-plate expressed | IFT140, SCAF11 | TALL — candidates | 38152138; 34194391 | **YES** |
| B138 | **KDM4A** | H3K9me3/H3K36me3 demethylase | KDM4A | TALL — same rare missense in 2 unrelated probands | 40577202 | **YES** |
| B139 | **L1CAM-like gene duplication (CHL1?)** | Reported in a patient with cognitive impairment, tall stature and obesity | ⚠ gene identity **UNVERIFIED** — title says "cell adhesion molecule L1-like gene"; I did not open the paper | TALL | 37114233 | **YES** |

#### B2n — DOSE-RESPONSE MIRRORS (the same locus in both directions)

These are the most informative rows in the whole enumeration, because they fix a *direction* rather
than an association.

| # | LOCUS | LOW DOSE / LOSS | HIGH DOSE / GAIN | KEY PMID | OBSCURE? |
|---|---|---|---|---|---|
| B140 | **NSD1 / 5q35** | Sotos syndrome — **TALL, advanced BA** | ⭐ **5q35.2q35.3 MICRODUPLICATION — "reversed Sotos": microcephaly, SHORT stature, DELAYED bone age, GH deficiency** | **40995982; 41804817; 21567906** | **YES** |
| B141 | **SHOX / PAR1** | Leri-Weill dyschondrosteosis, Langer, ISS — **SHORT** | Duplication / extra sex chromosomes — **TALL**; and the effect is modulated by gonadal status | **11134233**; 41751622; 41683999 | **YES** (the overdosage half) |
| B142 | **FGFR3** | **CATSHL — TALL** (LoF) | Achondroplasia / thanatophoric — **SHORT** (GoF) | 27139183; 37990933 | no (but rarely stated as one axis) |
| B143 | **NPR2** | Acromesomelic dysplasia Maroteaux — **SHORT** (biallelic LoF) | Miura epiphyseal chondrodysplasia — **TALL** (monoallelic GoF) | 24259409; 32282051 | **YES** |
| B144 | **NPR3** (CNP clearance receptor) | Biallelic LoF — **TALL** (Boudin-Mortier) | (no human gain allele described) | 35233476; 40171685 | **YES** |
| B145 | **NPPC / CNP ligand** | LoF — short | 2q37 translocation → **overexpression → TALL** | 36779427; 35528827 | **YES** |
| B146 | **IGF1R / 15q26** | 15q26 deletion — IUGR, **SHORT** | 15q26 duplication — **TALL** | 42130906; 28899882 | **YES** |
| B147 | **11p15.5 (IGF2/CDKN1C/H19)** | Silver-Russell — **SHORT** | Beckwith-Wiedemann — **OVERGROWTH** | 29377879 | no |
| B148 | **14q32 DLK1-DIO3** | Temple syndrome — **SHORT** | Kagami-Ogata — **OVERGROWTH** | 32592473 | **YES** |
| B149 | **NFIX** (allele-class, not dosage) | Malan — TALL, NMD-competent alleles | Marshall-Smith — **ACCELERATED BA + failure to thrive**, NMD-escaping alleles | **20673863** | **YES** |
| B150 | **PDGFRB** | (LoF: primary familial brain calcification) | Kosaki **OVERGROWTH** / Penttinen (premature-ageing) — two *activating* phenotypes | 41223009 | **YES** |
| B151 | **SOST** | Sclerosteosis (biallelic null) — **TALL/overgrowth**; Van Buchem (enhancer deletion) — milder | (romosozumab = pharmacological partial loss in adults) | 24019634; 32328030 | **YES** |

---

# PROSE — "THE TALL / DELAYED-FUSION LIST"

## 1. The shape of the space

The 2023 Nosology contains **771 disorders** and devotes **exactly one group of 31 entries (4.0%)** to
tall stature and overgrowth. Every other group is short, normal or segmental. That ratio is not an
accident of curation: **being short brings a child to a clinic and being tall usually does not**, so
the ascertainment that built the Nosology is systematically biased against the direction this project
cares about. A Finnish population cohort of 1.14 million births found that disorders associated with
tall stature affect **0.14%** of children and are *frequently underdiagnosed* (PMID 40233073) — and
the commonest single primary cause it found was **Klinefelter syndrome at 1/2146 boys**, i.e. a
karyotype, not a skeletal dysplasia. A companion finding is that in **non-familial** tall stature,
**cytogenetic anomalies are the predominant genetic alteration** (PMID 40524006). The practical order
of operations for "why is this person tall" is therefore karyotype/CMA **first**, gene panel second —
which is the opposite of how the short-stature workup is taught.

## 2. Where the tall stature actually is — nine mechanism classes

Pooling Nosology group 31, the HPO tall/overgrowth gene sets and the recent exome cohorts, the
tall-stature space partitions into nine mechanisms. Only the first two are well covered by the
mainstream growth literature.

1. **Microfibril / TGF-β release** — FBN1, FBN2, TGFBR1/2, TGFB2/3, SMAD2/3, SKI, LTBP4, MFAP5, LOX,
   THSD4, EFEMP2, FBLN5, and (via a completely different route) CBS homocystinuria. The unifying
   lesion is a failure to *sequester* a morphogen or to cross-link a fibre.
2. **Chromatin writers, erasers, readers and linker histones** — NSD1, NSD2, EZH2, EED, SUZ12,
   SETD2, DNMT3A, EHMT1, ASXL3, KMT2C, **KDM6B**, **KDM2B**, **KDM4A**, **H1-4**, **H3-3B**, **SPIN4**.
   This is the class the field calls "epigenetic overgrowth", and it now includes both *writers*
   (which is well known) and **erasers and readers** (which is not).
3. **Imprinting and growth-factor dosage** — 11p15.5, 14q32 DLK1-DIO3, GPC3/GPC4, DIS3L2, **GRB10**,
   IGF1R duplication.
4. **PI3K/AKT/mTOR and RAS, germline and mosaic** — PIK3CA, AKT1, AKT2, PIK3R2, PTEN, STRADA,
   DEPDC5, HRAS/KRAS/NRAS.
5. **Sex-steroid absence** — CYP19A1, ESR1, **CYP17A1**, AR, and the entire congenital
   hypogonadotropic hypogonadism gene set. *This is the only class that acts on the PERIOD rather
   than the RATE.*
6. **GH/IGF-1 excess** — GPR101, AIP, MEN1, CDKN1B, PRKAR1A, GNAS; plus the paradoxical
   "growth without GH" and insulin-mediated pseudoacromegaly.
7. **Hedgehog and cilium** — GLI3, KIF7, SUFU, PTCH1, and the oligogenic ciliary burden in
   non-syndromic familial tall stature (IFT140).
8. **WNT brake removal at the osteocyte** — SOST (sclerosteosis), LRP4, LRP5.
9. **Everything else, and it is a long tail** — GPI-anchor genes (PIGA/PIGL/PIGG/PIGV), mitochondrial
   genes, congenital myopathies, DICER1, PTBP1, HECTD4, NONO, FIBP, HERC1, AMOTL1, HPGD.

## 3. The delayed-bone-age / delayed-fusion list, ranked

The brief asks specifically for delayed bone age and delayed epiphyseal fusion. This is a **much
smaller and much more interesting** set than the tall set, and the Nosology contains *none* of it.

**Tier 1 — human states with a documented EXTENDED GROWTH PHASE and unfused epiphyses:**
- ⭐ **17α-hydroxylase/17,20-lyase deficiency (CYP17A1)** — 88 patients, **bone age delayed ≥2 years
  in 92.5%**, median BA 11.0 y at median CA 15.8 y, extended growth phase, **39% of final heights at
  or above the 90th percentile**, high span-to-height ratio (PMID 40350803). This is by a wide margin
  the largest human cohort of near-total sex-steroid absence with a bone-age endpoint, and it is
  effectively absent from the growth-plate literature.
- **Aromatase deficiency (CYP19A1)** — men with open epiphyses and continuing growth into the third
  decade (PMIDs 36504506, 41908849).
- **Oestrogen resistance (ESR1)** — the **only** gene in the entire HPO carrying
  *HP:0003799 "Marked delay in bone age"* alongside LHX4.
- **Congenital hypogonadotropic hypogonadism** — 19 genes under HP:0003782 eunuchoid habitus.
- **"Growth without GH"** — one patient with lifelong hypogonadism showed slow, prolonged growth with
  **delayed epiphyseal fusion** (PMID 41464859).

**Tier 2 — overgrowth *with* delayed bone age (the rarest combination in human genetics):**
- ⭐ **7q22.2-q22.3 microdeletion — overgrowth AND delayed bone age** (PMID 20219702). Candidate genes
  proposed by the authors are cell-cycle: SRPK2, KMT2E(MLL5), RINT1, LHFPL3.
- ⭐ **The 27-gene HPO intersection** (tall/overgrowth ∩ delayed skeletal maturation):
  CDKN1C, COL2A1, CPLX1, CTBP1, **CYP19A1**, DNA2, ELN, **ESR1**, FARSB, **FBN1**, FBXO11, HRAS,
  HSPG2, IGF2, KRAS, LETM1, NELFA, **NPR2**, NRAS, **NSD1**, NSD2, **PDGFRB**, PIGG, PTEN, SMAD4,
  **SRY**, TAF4. I computed this from the HPO API on 2026-08-15 and have not seen it published.
  Note that **NPR2 appears here** — the tall-stature GoF allele is annotated with delayed rather than
  advanced skeletal maturation, which is the favourable configuration.

**Tier 3 — the CATSHL/NPR2/NPR3 axis, which is where an intervention would sit:**
- **CATSHL (FGFR3 LoF)** — TALL. The human germline demonstration that reducing FGFR3 lengthens bone.
- **NPR2 monoallelic GoF (Miura)** and **NPR3 biallelic LoF (Boudin-Mortier)** — TALL, and both are
  the *pharmacologically addressable* end of the CNP axis.
- **NPPC overexpression via 2q37 translocation** — TALL from a ligand gain.

**Tier 4 — the human NEGATIVES, which matter as much:**
- **Severe untreated hypothyroidism** produces the most extreme delayed bone age in medicine and the
  patients end up **short**. Delayed bone age on its own does not buy height.
- **Transgender girls treated with GnRH analogue plus oestradiol reach an adult height unaffected by
  treatment** (PMID 35666195) — a direct human test of "manipulate the fusion signal, gain height"
  that came out null.
- **Marshall-Smith syndrome (NFIX)** — accelerated skeletal maturation *with* failure to thrive. Bone
  age and linear growth dissociate completely.
- **Familial glucocorticoid deficiency / MC2R** — tall as a child; the adult-height literature runs
  the other way.

## 4. Groups and mechanisms RARELY DISCUSSED in the growth literature (the flag the brief asks for)

- **Group 36, vertebral and costal dysostoses.** The only group whose primary lesion is the *number
  and shape of axial segments* — i.e. trunk height — set by the somitogenesis clock (DLL3, LFNG,
  HES7, MESP2, RIPPLY2, TBX6). Growth endocrinology essentially never touches segment number.
- **Group 37, patellar dysostoses** (3 entries) and **Group 41, defects in joint formation and
  synostoses** (9 entries). The two smallest groups; almost never cited.
- **Group 25, osteosclerotic disorders**, as a source of **TALL** phenotypes (sclerosteosis,
  Camurati-Engelmann, pachydermoperiostosis). The high-bone-mass literature and the tall-stature
  literature do not talk to each other.
- **The GPI-anchor biosynthesis pathway** (PIGA, PIGL, PIGG, PIGV) — four independent genes with
  tall/overgrowth annotations and zero presence in growth physiology.
- **Congenital myopathies as a tall-stature class** (ACTA1, NEB, TPM2, TPM3, TNNT1, KBTBD13, KLHL41,
  MYPN, MTM1, PYROXD1, TRIM32). If real, this is a *mechanical unloading* route to tall stature and
  it is the mirror image of the mechanical-loading literature.
- **Mitochondrial disease as a tall-stature class** (TYMP/MNGIE, POLG, DNA2, LARS2, TIMM50, NNT).
- **The E3-ubiquitin-ligase overgrowth cluster** — RNF125 (Tenorio), RNF135, HERC1, HECTD4, KLHL20.
  Four or five independent ligases; no unifying account exists.
- **Prostaglandin degradation (HPGD/SLCO2A1)** as a skeletal-overgrowth mechanism.
- **"Reversed Sotos" (5q35 microduplication)** — the dose-response mirror that turns NSD1 from an
  association into a directional lever.
- **The Nosology's own editorial exclusions** are informative and never quoted: PTEN is excluded from
  the disorganized-development group "because the overgrowth is restricted to macrocephaly", and
  group 31 explicitly excludes "disorders that cause overgrowth secondary to vascular malformations".
- **Skeletal TEMPO is not an axis in the Nosology at all.** Two entries out of 771 mention bone age,
  both advanced. There is no delayed-bone-age or delayed-fusion group, so any search that starts from
  the Nosology will structurally miss the entire class that matters most here.

## 5. Three specific observations worth carrying forward

1. **The same gene gives both directions more often than the field acknowledges** — FGFR3, NPR2,
   FBN1, NSD1, SHOX, IGF1R, 11p15, 14q32, NFIX, PDGFRB, SOST (Table B2n). Eleven loci where the
   direction is fixed by dosage or allele class rather than by the gene.
2. **Every large tall-stature effect that is not a karyotype is either a chromatin gene, a microfibril
   gene, or a sex-steroid gene.** There is no fourth large class.
3. **The tall-stature space has a substantial unsolved tail.** At least seven HPO tall-annotated
   entities have **no gene assigned at all** (Moreno-Nishimura-Schmidt, MOMO, Elejalde/ACPD,
   Fryns-Smeets-Thiry, Giacheti, thoracolaryngopelvic dysplasia, hydrocephalus-tall stature-joint
   laxity-kyphoscoliosis, microcephaly-glomerulonephritis-marfanoid habitus). Those are the places a
   genuinely novel growth mechanism is most likely still hiding.

---

# WHAT I COULD NOT VERIFY

- **Full text of the Nosology's supplementary tables.** I parsed the PMC author manuscript
  (PMC10081954) successfully and extracted all 41 groups and their entries, but the record is
  `restricted-by pmc`; some inheritance/MIM fields were interleaved awkwardly by tag-stripping. Entry
  counts per group (`N=`) are my counts of `NOS xx–yyyy` tokens and could be off by one or two where
  a note line was formatted unusually. **The group names and the 771/552/41 headline figures are
  verbatim and are reliable.**
- **The Kamien 2018 generalized-overgrowth review (PMID 29593474 / PMC5836217)** returned front
  matter only from eutils; I could not read its gene table. Same for the two 2025–26 Polish
  systematic reviews (PMIDs 41693191, 42023627) — abstracts only. All three are cited as **index,
  not source**.
- **Snyder-Robinson (SMS) height direction is genuinely contested.** The 2023 Nosology labels it
  "tall stature" and HPO annotates disproportionate tall stature; much clinical writing emphasises
  asthenic build with short stature. I did not resolve it.
- **α-mannosidosis (MAN2B1) annotated as tall stature with increased vertebral height** — recorded
  as an HPO annotation I could not reconcile with the clinical literature.
- **Dyssegmental dysplasia Silverman-Handmaker (HSPG2) annotated as tall** — almost certainly an
  annotation artefact from a vertebral descriptor; flagged, not resolved.
- **"Epiphyseal dysplasia, Baumann type"**, annotated with *marked delay in bone age*: I could find
  **no primary publication** and HPO returns no gene. Genuinely unresolved.
- **ABAT / GABA-transaminase deficiency "accelerated linear growth"** — widely repeated, no primary
  source verified in this round.
- **PMID 37114233** ("cell adhesion molecule L1-like gene duplication with tall stature") — I did not
  open it, so the gene identity is UNVERIFIED.
- **X-LAG gene mapping via ORPHA:300373 returned no gene**; the GPR101 assignment comes from
  OMIM:300942 (Chromosome Xq26.3 duplication syndrome), which HPO does map to GPR101.
- **Effect sizes in centimetres** are absent throughout. The Nosology and HPO are both categorical;
  neither carries a magnitude. Anyone ranking these targets will need a separate quantitative source.
- **ClinGen's 2026 evidence-based re-curation of skeletal-disorder genes (PMID 41313243)** was found
  but not read; it is the obvious next document, because it would tell us which of the 552 Nosology
  genes actually survive formal gene-disease validity scoring.
- I did **not** use WebSearch/WebFetch or clinicaltrials.gov this round — everything came from
  Europe PMC REST, NCBI eutils and the HPO API. OMIM itself is not freely scriptable and was accessed
  only indirectly through HPO's OMIM-keyed disease records.
