# Stub disposition - L0 developmental_origin sweep (shard l0dev, 2026-08-05)

Admission rule applied: a node is kept only if it (a) sets an initial condition the
POSTNATAL growth plate inherits, (b) explains a site-, sex- or population-specific
difference in growth, or (c) supplies an organism-level number the mechanistic layers
must reproduce. Format: `node_id | DELETE | reason`.

dermomyotome | DELETE | Origin of muscle and dermis, not of any growth plate compartment; sets no initial condition the postnatal plate inherits.
dll3_gene | DELETE | Somite-clock Notch ligand; its human phenotype (spondylocostal dysostosis) is a segmentation defect belonging in L11, not a growth-plate initial condition.
engrailed1_gene | DELETE | Ventral ectoderm identity; no demonstrated consequence for any postnatal growth plate property.
fgf10_gene | DELETE | Limb-bud initiation ligand; folded into limb_bud_initiation to avoid a signalling review. Null phenotype is limb absence, not an altered plate.
fgf8_aer | DELETE | Duplicate of apical_ectodermal_ridge, which carries the FGF8/FGF10 content as the signalling centre that sets element identity.
gastrulation | DELETE | Textbook antecedent; no site-, sex- or population-specific growth consequence and no organism-level number.
gli3_gene | DELETE | Postnatal function is already held by L3 gli3_repressor; its embryonic role sets digit NUMBER, not growth rate or any inherited plate property.
hes7_oscillator | DELETE | Segmentation-clock component; axial segment number is not a growth-plate initial condition and no postnatal plate readout exists.
hoxa9_gene | DELETE | No postnatal growth-plate expression, function or phenotype reported for Hox9 paralogs; would be a patterning reference, not a node.
joint_cavitation | DELETE | Articular-surface process; the element-length-setting decision is joint POSITION, held by interzone_formation. Cavitation itself has no growth plate readout.
lateral_plate_mesoderm | DELETE | Lineage-origin reference. No evidence retrieved that appendicular (LPM) versus axial (somite) origin predicts any growth plate property; converted to gap g_l0dev_010.
lfng_gene | DELETE | Segmentation clock; see hes7_oscillator.
lmx1b_gene | DELETE | Dorsoventral limb identity; nail-patella syndrome is a human phenotype for L11 and has no reported growth plate parameter.
mesp2_gene | DELETE | Somite boundary formation; no growth plate inheritance.
ncam1_condensation | DELETE | Condensation adhesion molecule; no quantitative link from adhesion to condensation size or final element length was retrievable. Content folded into mesenchymal_condensation.
nkx3_2_gene | DELETE | Sclerotome chondrogenic competence; the human phenotype (spondylo-megaepiphyseal-metaphyseal dysplasia) is an L11 entity and no L0-to-plate initial condition is demonstrated.
osterix_sp7 | DELETE | Osteoblast commitment transcription factor; covered by L3 runx2_tf and by vascular_invasion_poc (Osx+ precursors arrive with vessels). Duplicate.
paraxial_mesoderm | DELETE | Lineage-origin reference; see lateral_plate_mesoderm.
pax1_gene | DELETE | Sclerotome marker; no demonstrated postnatal growth plate consequence.
pax9_gene | DELETE | Sclerotome marker; no demonstrated postnatal growth plate consequence.
presomitic_mesoderm | DELETE | Segmentation substrate; no growth plate inheritance.
primitive_streak | DELETE | Textbook antecedent; fails all three admission tests.
resegmentation | DELETE | Vertebral morphogenesis mechanism; no growth plate property is set by it that this sweep could evidence.
ripply2_gene | DELETE | Segmentation clock; see hes7_oscillator.
runx2_osteoblast_commitment | DELETE | Duplicate of L3 runx2_tf; cleidocranial dysplasia belongs to L11.
sclerotome | DELETE | Axial lineage-origin reference. The question it was meant to answer (does somitic origin make vertebral plates behave differently) is unanswered in the literature; converted to gap g_l0dev_010.
segmentation_clock | DELETE | Sets somite number, not any growth plate parameter; an embryology reference.
shh_zpa | DELETE | Duplicate of zone_of_polarizing_activity.
somite | DELETE | Lineage-origin reference; see sclerotome.
somitogenesis | DELETE | See segmentation_clock.
syndetome | DELETE | Tendon progenitor compartment; outside the growth plate inheritance chain.
tbx4_gene | DELETE | Hindlimb-bud initiation; folded into limb_bud_initiation and pitx1_gene, which carries the hindlimb-identity claim with a functional mouse phenotype.
tbx6_gene | DELETE | Presomitic mesoderm specification; no growth plate inheritance.
wnt7a_gene | DELETE | Dorsoventral ectoderm signal; the DV-axis claim that does bear on the plate (condensation-stage progenitors populate the dorsal resting/proliferative zone) is carried by mesenchymal_condensation with a direct lineage-tracing source.
wnt9a_gene | DELETE | Interzone marker; folded into interzone_formation.
wnt_fgf_ra_wavefront | DELETE | Segmentation wavefront; no growth plate inheritance.

Deleted 36 of 61 L0 stubs; 25 retained and researched.

---

# Stub disposition - L9 whole_organism_growth sweep (shard l9organism, 2026-08-05)

Same admission rule: kept only if the node (a) sets an initial condition the postnatal
plate inherits, (b) explains a site-, sex- or population-specific growth difference, or
(c) supplies an organism-level number the mechanistic layers must reproduce.

adipocyte_hyperplasia | DELETE | Cell-level fat-tissue parameter. Sets no initial condition for the physis, explains no site- or sex-specific difference in bone elongation, supplies no organism-level target. The only growth-relevant link (adiposity -> pubertal timing) is owned by L4 leptin_hormone and by L10.
adipose_tissue_growth | DELETE | Body-fat trajectory is a covariate of pubertal timing, not a constraint on plate kinetics; the mechanism runs through L4 leptin_hormone. Would have been an L9 node with no edge into L1-L7 and no target number.
articular_cartilage | KEEP (initially marked DELETE, reversed) | Deleted on the first pass as structural rather than organism-level, then restored: an existing canonical edge e00409 (L3 ift80_protein -> articular_cartilage) depends on it, and human MRI supplies a genuine organism-level dissociation - femoral articular cartilage is thicker while the distal femoral physis is open and thins with age, while patellar cartilage is invariant (sidharthan2021, n=240). Admission criterion (c) is met.
costal_cartilage | DELETE | No quantitative organism-level target located and no initial condition inherited by the long-bone physis. Trunk growth is captured quantitatively by sitting_height_ratio, which is retained.
craniosynostosis | DELETE | Pathology used as a natural experiment; L11 owns that role. The normative timing numbers a craniofacial growth model must reproduce are retained in suture_fusion_timing.
follistatin_protein | DELETE | Molecular modifier of the myostatin/activin axis with no human organism-level growth number. Its role is summarised inside myostatin_mstn and activin_receptor_2b, both retained because human loss-of-function and pharmacological-blockade data give organism-level muscle-mass numbers.
nasal_septal_cartilage | DELETE | The septum-as-midface-growth-centre claim rests on murine and surgical-series evidence and supplies no human organism-level number; midface growth is carried by craniofacial_growth and cranial_base_synchondrosis, both retained with human numbers.

Deleted 6 of 40 L9 stubs; 34 retained and researched.

---

# Stub disposition - Phase 3 seam pass (shard l0l9seam, 2026-08-05)

Covers the 34 stubs that survived phase 2C (33 in L8, 1 in L3) plus the one genuine
non-stub duplicate the detector surfaced. Admission rule for L8: a node is kept only if
it (a) changes what may be claimed about the human genetics of stature, (b) supplies a
number a mechanistic layer must reproduce, or (c) is the only home for an allelic series
or a method artefact that would otherwise be laundered into fact. Format:
`node_id | FATE | reason`.

Before doing anything, `graph.py --duplicates` was re-run and every one of its 33 flagged
collisions was read. All ten gene/protein pairs behaved exactly as DESIGN_DECISIONS D1
describes and were left alone: npr2_gene/npr2_receptor, fgfr3_gene/fgfr3_receptor,
ihh_gene/ihh_protein, acan_gene/aggrecan_acan, stat5b_gene/stat5b_tf, ghr_gene/gh_receptor,
col2a1_gene/collagen_type_ii, pth1r_gene/pth1r_receptor, igf1r_gene/igf1_receptor,
nppc_gene/cnp_protein. The D2 false positives (pappa/pappa2, PTH/teriparatide, the collagen
and IGFBP families, LRP5/LRP6, IFT80/IFT88, ADAMTS4/5, BMP2/6/7) were likewise confirmed
as matcher artefacts. D2's closing statement that "every flagged collision is a false
positive" is now FALSE and is corrected below: one genuine duplicate was present and had
been missed because the two copies carry different node_ids and sit in different layers.

## MERGE

acan_dosage_effect | MERGE -> acan_related_short_stature | THE significant one. Not a stub; both copies were fully researched, which is why eight parallel sweeps never noticed. L5 `acan_dosage_effect` (type phenotype) and L11 `acan_related_short_stature` (type phenotype) are the same entity: same cohort (gkourogianni2017, 103 individuals from 20 families), same three headline numbers (adult height -2.8 SDS, childhood height -2.0 SDS, bone age +1.3 y), same mouse mechanism reference (bendre2025), and two aliases held in common verbatim ("aggrecanopathy", "ACAN haploinsufficiency"). This is not a D1 gene/protein split - neither node is about genetic variation as such and both are the human clinical dosage phenotype - and it is not a layer split either, because L5 already holds the matrix biology in `aggrecan_acan`. L11 survives as the correct home for a pathology-as-natural-experiment node; L5's exome-family range (-2.3 to -4.2 SDS), deletion-severity claim and mouse-proliferation null were merged into it, one edge (e00542, -> aggrecan_acan) was redirected in both edges.yaml and the l5matrix shard, five rows of quant/parameters.csv were repointed from L5 to L11, and both old ids are kept as aliases so the query alias table still resolves them.
giant_consortium | MERGE -> height_gwas | GIANT is the meta-analysis structure that PRODUCED the height_gwas dataset, not an independent object: yengo2022 is a GIANT analysis and so was the first-generation weedon2008 scan. Keeping both would have counted one consortium's sample-size curve as two nodes. weedon2008 and the 20-loci/~3%-of-variance figure were merged into height_gwas.
polygenic_architecture_height | MERGE -> height_gwas | Describes the same object from the other side (polygenicity, effect-size distribution, prediction ceiling), all of which height_gwas already measures - 7,209 segments over 21% of the genome, 40% variance explained - with the remainder held by height_heritability and missing_heritability_height. A separate node would have restated three researched nodes without adding a datum.
pgs_ancestry_transferability | MERGE -> height_polygenic_score | A property of the score, not an entity. The transferability numbers (40% European vs 10-20% other ancestries) were already inside height_gwas; they now sit with the method node that owns them, together with martin2019 and the berg2019/sohail2019 stratification result.
uniparental_disomy_growth | MERGE -> genomic_imprinting_growth | UPD is the assay by which parent-of-origin effects on growth are demonstrated, not a separate mechanism; the syndromes it produces (Silver-Russell, Temple, Prader-Willi) are L11 entities that already exist. Merged with the UPD(14)mat and UPD7 cohort numbers attached.

## DELETE

de_novo_variant_growth | DELETE | Search-established. Europe PMC, 2026-08-05, `(("de novo mutation" OR "de novo variant") AND (height OR stature) AND (population OR cohort) AND (normal range OR general population)) AND (PUB_TYPE:"Journal Article" NOT PUB_TYPE:"Review")`, 1172 hits, top 25 screened: every one is a syndromic case report or case series in which a de novo variant causes a named disorder that happens to include short stature. Not one estimates the contribution of de novo mutation to normal-range stature or to a growth plate parameter. The syndromic instances belong to L11; the frequency-spectrum argument is held by rare_variant_height. Converted to gap g_l0l9_007.
epigenetic_clock_growth | DELETE | Epigenetic clocks index biological ageing in blood or buccal tissue; the two retrieved studies that touch growth (Simpkin 2017 ALSPAC; PMID 34372922) relate methylation age to pubertal timing and mid-life outcomes, not to any growth plate parameter. The growth-plate-relevant methylation claim is already carried by L7 epigenetic_drift_fusion (methylation-drift model of senescence) and by L8 dna_methylation_growth_plate, both researched; the maturity-clock role is held by L7 bone_age and L9 dental_development_clock. Node would have had no independent content.

## RESEARCH (28 of 34; no stub survives)

Filled to full schema in this pass (13): klotho_beta_cofactor (L3), assortative_mating_height,
dna_methylation_growth_plate, dominant_negative_vs_haploinsufficiency,
gene_environment_interaction_height, genomic_imprinting_growth, height_polygenic_score,
hmga2_gene, igf2_h19_imprinting, mendelian_randomization_height, omnigenic_model,
rare_variant_height, zbtb38_gene.

Filled by the concurrent L8 gene sweep (shard l8gen) and verified non-stub here (15):
acan_gene, col2a1_gene, fgfr3_gene, gdf5_height_locus, ghr_gene, igf1_gene, igf1r_gene,
ihh_gene, nppc_gene, npr2_gene, pappa2_gene, pth1r_gene, shox_gene, shox_haploinsufficiency,
stat5b_gene. Each is a D1-protected gene node; the correct link to its protein counterpart
is an edge, not a merge, and shox_gene/shox_haploinsufficiency were deliberately NOT merged
for the same reason (gene dose series versus penetrance-and-therapy phenotype).

Counts: 28 RESEARCH, 5 MERGE (4 stubs + 1 non-stub), 2 DELETE. 1 edge redirected.
