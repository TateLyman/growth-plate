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
articular_cartilage | DELETE | Structural rather than organism-level; epiphyseal/articular cartilage and its relation to the SOC are held by L1 (cartilage_canal, epiphyseal_vasculature) and L2 (skeletal_stem_cell). No organism-level number.
costal_cartilage | DELETE | No quantitative organism-level target located and no initial condition inherited by the long-bone physis. Trunk growth is captured quantitatively by sitting_height_ratio, which is retained.
craniosynostosis | DELETE | Pathology used as a natural experiment; L11 owns that role. The normative timing numbers a craniofacial growth model must reproduce are retained in suture_fusion_timing.
follistatin_protein | DELETE | Molecular modifier of the myostatin/activin axis with no human organism-level growth number. Its role is summarised inside myostatin_mstn and activin_receptor_2b, both retained because human loss-of-function and pharmacological-blockade data give organism-level muscle-mass numbers.
nasal_septal_cartilage | DELETE | The septum-as-midface-growth-centre claim rests on murine and surgical-series evidence and supplies no human organism-level number; midface growth is carried by craniofacial_growth and cranial_base_synchondrosis, both retained with human numbers.

Deleted 7 of 40 L9 stubs; 33 retained and researched.
