from w import *

write(dict(id='common_vs_rare_pathway_divergence',
 name='Divergence between common-variant and rare-disease pathway rankings for height',
 type='hypothesis', layer='L8',
 aliases=['GWAS versus skeletal dysplasia gene rankings','architecture-dependent pathway ranking'],
 summary="""Ranking growth-plate pathways by common-variant height signal and by monogenic skeletal-dysplasia
burden produces two different orders, and the divergence is systematic rather than random. The
common-variant ranking, read from the three primary pathway-enrichment analyses, is dominated by
paracrine growth-plate signalling and matrix synthesis: Weedon 2008 reported Hedgehog (IHH, HHIP,
PTCH1), extracellular matrix (EFEMP1, ADAMTSL3, ACAN) and cell-cycle/chromatin genes (CDK6, HMGA2,
DLEU7); Lango Allen 2010 reported 180 loci enriched for genes connected in biological pathways and
for genes underlying skeletal growth defects; Wood 2014 reported FGF signalling, WNT/beta-catenin,
chondroitin-sulfate-related genes, mTOR, osteoglycin and hyaluronic acid binding. The rare-disease
ranking, read from the 2023 nosology's 771 entries across 552 genes and from ClinGen's curated
panel, is dominated by structural collagens and matrix assembly (COL1A1, COL1A2, COL2A1, COL10A1,
COMP, MATN3), sulfate transport (SLC26A2), mineralisation (ALPL), ion channels (TRPV4) and - the
largest single stature effects in medicine - the GH-IGF endocrine axis (GHR at -4 to -10 SDS,
STAT5B at -7.8 SDS, IGFALS, IGF1, IGF1R, PAPPA2). The GH-IGF axis appears in no published height
GWAS pathway-enrichment list retrieved in this sweep. Three pathway families are shared: Hedgehog
(IHH is both the commonest ISS panel finding and a top GWAS locus), CNP/NPR2, and
proteoglycan/glycosaminoglycan synthesis, which Marouli 2017 identifies specifically at the rare
coding tier. The reading offered here is that a gene contributes common-variant height variance
only if its dose is both continuously variable in the population and non-lethal at the margin;
endocrine-axis genes are buffered by feedback so that common variation produces little phenotype
while total loss is catastrophic, whereas paracrine and matrix genes act locally and dose-linearly
in the plate. That is a hypothesis, and it is graded as one.""",
 quantitative=[
   q('pathways named in the largest published height pathway-enrichment analysis','6','pathway families','FGF signalling, WNT/beta-catenin, chondroitin-sulfate genes, mTOR, osteoglycin, hyaluronic acid binding; n=253,288','human','wood2014','as reported in the abstract'),
   q('height GWAS pathway-enrichment lists naming the GH-IGF/somatotropic axis','0','of 3 analyses examined','weedon2008, lango2010 and wood2014 abstracts; see search log g_l8gen_001','human','wood2014','negative result; see search_established gap'),
   q('monogenic skeletal disorder entries in the 2023 nosology','771','entries','associated with 552 genes','human','unger2023','11th revision'),
   q('largest monogenic stature effect in the GH-IGF axis','-4 to -10','SDS','homozygous GHR loss of function, 69-patient Laron cohort','human','laron2015','range across the cohort'),
   q('per-allele effect of the largest-effect common height variants','0.4-0.44','cm','HMGA2 rs1042725 and the GDF5-UQCC region','human','weedon2007','independent estimates from two loci'),
 ],
 localization=['human: genome-wide comparison of two ranking procedures, not tissue-localized'],
 human_evidence='direct',
 human_evidence_note='Both rankings are compiled from human data - GWAS pathway enrichment on measured stature and curated human monogenic disorder catalogues.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='A comparison of two human evidence bases.',
 confidence='C',
 claim_grades=[
   dict(claim='Published height GWAS pathway-enrichment analyses list paracrine signalling and matrix genes, not the GH-IGF endocrine axis.',grade='A',basis='Direct reading of the enrichment results in weedon2008, lango2010 and wood2014, plus a reproducible null search (g_l8gen_001).'),
   dict(claim='Monogenic short stature is dominated by GH-IGF axis and structural collagen genes.',grade='A',basis='The 2023 nosology (unger2023) and ClinGen curation (webb2026), together with the measured stature effects in ghr_gene, stat5b_gene, igfals_gene, col2a1_gene, col10a1_gene and comp_gene.'),
   dict(claim='Hedgehog, CNP/NPR2 and proteoglycan synthesis are the pathway families where the two rankings converge.',grade='B',basis='IHH and ACAN appear in weedon2008 and in monogenic ISS panels (andrade2022); proteoglycan/GAG synthesis is named at the rare coding tier by marouli2017. Convergence is by inspection rather than by a formal overlap statistic.'),
   dict(claim='The divergence arises because feedback-buffered endocrine genes tolerate common variation while dose-linear local genes do not.',grade='E',basis='Explanatory hypothesis, not tested. The discriminating test is stated in gap g_l8gen_001.'),
 ],
 key_refs=[
   R('wood2014','697 height variants implicate FGF signalling, WNT/beta-catenin, chondroitin-sulfate genes, mTOR, osteoglycin and hyaluronic acid binding - no endocrine axis.'),
   R('weedon2008','The first 20 height loci implicate Hedgehog (IHH, HHIP, PTCH1), extracellular matrix (EFEMP1, ADAMTSL3, ACAN) and cell-cycle genes.'),
   R('lango2010','180 height loci are enriched for genes connected in biological pathways and for genes underlying monogenic skeletal growth defects.'),
   R('marouli2017','Rare coding height variants implicate proteoglycan and glycosaminoglycan synthesis and overlap monogenic growth-disorder genes.'),
   R('unger2023','771 genetic skeletal disorder entries across 552 genes define the rare-disease gene ranking.'),
   R('webb2026','ClinGen curation identifies COL1A1, COL1A2, COL2A1, FGFR3, SLC26A2, TRPV4, COMP, ALPL and SOX9 as the genes behind the commonest skeletal dysplasias.'),
   R('laron2015','Homozygous GHR loss gives -4 to -10 SDS, the largest monogenic stature effect, at a locus absent from height GWAS enrichment lists.'),
 ],
 open_questions=['g_l8gen_001'],
))
