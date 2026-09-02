from w import *

write(dict(id='hmga2_gene', name='HMGA2', type='gene', layer='L8',
 aliases=['high mobility group AT-hook 2'],
 summary="""HMGA2 was the first common variant reproducibly associated with a human quantitative trait, and it
remains the reference point for how small common-variant height effects actually are. Weedon 2007
found rs1042725 in a genome-wide scan of 4,921 individuals (P = 4e-8), confirmed it in 19,064
adults from four further studies (P = 3e-11, overall P = 4e-16), and reproduced it in 6,827
children and a 3,207-person tall/short case-control design. The per-allele effect is approximately
0.4 cm and the variant explains about 0.3% of population height variance. That number is the
quantitative anchor of the whole common-variant side of L8: a locus that is a strong biological
candidate - rare severe HMGA2 mutations alter body size in both mice and humans - contributes about
four millimetres per allele in the general population, roughly one two-hundredth of the effect of a
monogenic NPR2 or ACAN allele. Weedon 2008 subsequently placed HMGA2 among the first 20
genome-wide-significant height loci. The gene therefore illustrates the central asymmetry this
atlas has to hold: the same gene can be a large-effect Mendelian growth gene and a
0.3%-of-variance common locus, and neither fact predicts the other's magnitude.""",
 quantitative=[
   q('per-allele adult height effect, rs1042725 C allele','0.4','cm','general population, European ancestry','human','weedon2007','approximate as reported'),
   q('population height variance explained by rs1042725','0.3','%','same','human','weedon2007','estimate; CI not reported'),
   q('total replication sample','19064','adults','four independent studies following a 4,921-person discovery scan','human','weedon2007','overall P = 4e-16'),
   q('childhood replication sample','6827','children','same variant, P = 1e-6','human','weedon2007','not applicable (count)'),
 ],
 localization=['human: germline 12q14.3; expressed in proliferating mesenchyme'],
 human_evidence='direct',
 human_evidence_note='Discovery plus four independent replication cohorts and a case-control design, all with measured stature.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human association data; the murine pygmy mutant is mentioned only as a candidate-gene rationale, not as evidence for the human effect size.',
 confidence='A',
 key_refs=[
   R('weedon2007','HMGA2 rs1042725 C allele gives ~0.4 cm taller adult height and explains ~0.3% of population height variance, replicated in 19,064 adults and 6,827 children.'),
   R('weedon2008','HMGA2 confirmed among the first 20 genome-wide-significant height loci.'),
 ],
))

write(dict(id='zbtb38_gene', name='ZBTB38', type='gene', layer='L8',
 aliases=['zinc finger and BTB domain containing 38'],
 summary="""ZBTB38 was identified as a height locus in Weedon 2008, the first-generation GIANT scan that took
genome-wide association data on 13,665 individuals plus genotyping of 39 variants in 16,482 more
and reported 20 genome-wide-significant height loci. In that analysis the 20 variants jointly
explained approximately 3% of height variation, with roughly 5 cm separating the 6.2% of people
carrying 17 or fewer tall alleles from the 5.5% carrying 27 or more. ZBTB38 has stayed in every
subsequent height GWAS and is notable for what it is not: unlike IHH, HHIP, PTCH1, ACAN or EFEMP1
from the same paper, it has no established growth-plate function. It encodes a methyl-CpG-binding
zinc finger transcriptional regulator, and its most reproducible non-height association is with
epigenetic age - ZBTB38 expression was differentially associated with five separate epigenetic
clocks in adolescent blood. That places ZBTB38 in the category of height loci whose route to the
growth plate is unknown, which is exactly the category the omnigenic model predicts should
dominate. No per-allele centimetre effect for ZBTB38 specifically was verified in this sweep, only
the joint 20-locus figure, and that is recorded as a quantitative gap rather than filled with a
number carried over from memory.""",
 quantitative=[
   q('height variance explained by the 20 first-generation loci including ZBTB38','3','%','n=13,665 discovery plus 16,482 follow-up, European ancestry','human','weedon2008','approximate as reported'),
   q('height difference between extreme tall-allele-count groups','5','cm','6.2% of people with <=17 tall alleles versus 5.5% with >=27','human','weedon2008','approximate as reported'),
 ],
 localization=['human: germline 3q23; methyl-CpG-binding transcriptional regulator, tissue of action for the height effect unknown'],
 human_evidence='direct',
 human_evidence_note='Human GWAS association with measured stature; no human tissue-level mechanism established.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Association-only node; no cross-species mechanistic claim is made.',
 confidence='B',
 claim_grades=[
   dict(claim='Common variation at ZBTB38 is associated with adult height at genome-wide significance.', grade='A', basis='weedon2008 discovery plus follow-up genotyping, and the locus persists in every later height GWAS including yengo2022.'),
   dict(claim='ZBTB38 influences height through the growth plate.', grade='E', basis='Inference from the trait alone; no growth-plate expression or perturbation evidence was found. Flagged as inference.'),
 ],
 key_refs=[
   R('weedon2008','ZBTB38 among 20 height loci; the 20 SNPs jointly explain ~3% of height variance with ~5 cm between allele-count extremes.'),
   R('yengo2022','ZBTB38 remains within the saturated common-variant map of 12,111 independent height SNPs.'),
 ],
 open_questions=['g_l8gen_009'],
))

write(dict(id='gdf5_height_locus', name='GDF5 height locus', type='gene', layer='L8',
 aliases=['GDF5-UQCC region','rs143383'],
 summary="""The GDF5-UQCC region is the height locus that ties normal stature variation to osteoarthritis risk.
Sanna 2008 performed genome-wide association analyses in 6,669 individuals from Finland and
Sardinia with follow-up in 28,801 more and showed that common variants in this osteoarthritis-
associated locus contribute to height with an estimated additive effect of 0.44 cm per allele
(overall P < 1e-15). GDF5 (growth/differentiation factor 5, BMP-14) is a genuine skeletal
developmental gene - it specifies the joint interzone and is mutated in brachydactyly and in
Grebe/Hunter-Thompson chondrodysplasia - so unlike ZBTB38 this locus has a plausible and
independently established route to the growth plate and joint. The per-allele effect, 0.44 cm, is
statistically indistinguishable in magnitude from HMGA2's 0.4 cm, which is the useful comparison:
a locus with clear skeletal developmental function and a locus with none contribute the same
fraction of a centimetre. That equality is a direct observation against the intuition that
common-variant effect size tracks biological centrality, and it is one of the empirical footings of
the omnigenic argument. Sanna's authors explicitly proposed the link between height genetics and
osteoarthritis is mediated through bone growth and development.""",
 quantitative=[
   q('additive per-allele height effect, GDF5-UQCC region','0.44','cm','6,669 Finnish and Sardinian individuals plus 28,801 follow-up','human','sanna2008','overall P < 1e-15'),
 ],
 localization=['human: germline 20q11.22; GDF5 protein acts at the joint interzone and in growth plate cartilage'],
 human_evidence='direct',
 human_evidence_note='Human GWAS with replication and a measured per-allele centimetre effect.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human association data; murine Gdf5 (brachypodism) work sits in gdf5_protein and gdf5_gene (L0).',
 confidence='A',
 key_refs=[
   R('sanna2008','Common variants in the GDF5-UQCC region alter adult height by an estimated 0.44 cm per allele (P < 1e-15) in 35,470 individuals.'),
   R('weedon2008','Independent first-generation height GWAS establishing the scale of common-variant effects against which the GDF5 effect is compared.'),
 ],
))

write(dict(id='rare_variant_height', name='Rare variant contribution to height', type='process', layer='L8',
 aliases=['low-frequency coding variants and height','rare non-coding variants and height'],
 summary="""Rare variation contributes to height in a way that is quantitatively bounded and mechanistically
distinct from common variation. Marouli 2017 reported 83 height-associated coding variants with
minor allele frequencies of 0.1-4.8% and effects up to 2 cm per allele - more than ten times the
average common-variant effect - in genes including IHH, STC2, AR and CRISPLD2, and showed
functionally that rare height-increasing STC2 alleles compromise proteolytic inhibition of PAPP-A
and increase IGFBP-4 cleavage, raising IGF bioavailability. Those 83 variants overlap genes mutated
in monogenic growth disorders, so the rare-coding tier is partly the same gene set as the Mendelian
tier at lower allelic severity. Hawkes 2024 extended the search to non-coding regulatory regions
using whole-genome sequencing in 333,100 individuals across UK Biobank, TOPMed and All of Us, and
found 29 independent rare associations at P < 6e-10 after conditioning on known signals, with
effects from -7 cm to +4.7 cm, plus a replicated aggregate signal near HMGA1 worth about 5 cm.
Wainschtein 2026 then bounded the whole tier: across 34 traits in 347,630 UK Biobank whole genomes,
rare variants (MAF < 1%) account for about 20% of pedigree heritability and common variants about
68%, and of the rare-variant component 21% is coding and 79% non-coding. The rare tier is
therefore real, contains the largest individual effects outside Mendelian disease, and is mostly
regulatory rather than protein-altering.""",
 quantitative=[
   q('height-associated low-frequency coding variants','83','variants','minor allele frequency 0.1-4.8%, exome-array meta-analysis','human','marouli2017','not applicable (count)'),
   q('maximum per-allele effect, rare coding variants','2','cm','e.g. IHH, STC2, AR, CRISPLD2','human','marouli2017','>10x the average common-variant effect'),
   q('per-allele effect of rare STC2 height-increasing alleles','1-2','cm','functional follow-up shows compromised PAPP-A inhibition and increased IGFBP-4 cleavage','human','marouli2017','range as reported'),
   q('independent rare non-coding height associations','29','variants','WGS of 333,100 individuals (UK Biobank 200,003; TOPMed 87,652; All of Us 45,445), MAF < 0.1%, P < 6e-10 conditional','human','hawkes2024','not applicable (count)'),
   q('effect-size range, rare non-coding height variants','-7 to +4.7','cm','same analysis','human','hawkes2024','range across the 29 signals'),
   q('share of pedigree heritability from rare variants (MAF < 1%)','20','%','347,630 UK Biobank whole genomes, average across 34 complex traits','human','wainschtein2026','common variants contribute 68%; total WGS capture ~88%'),
   q('share of rare-variant heritability that is non-coding','79','%','same analysis','human','wainschtein2026','coding accounts for the remaining 21%'),
 ],
 localization=['human: germline, genome-wide'],
 human_evidence='direct',
 human_evidence_note='Three independent large human sequencing analyses with measured stature and explicit variance partitions.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human sequencing and heritability partitioning.',
 confidence='A',
 key_refs=[
   R('marouli2017','83 low-frequency coding variants alter height by up to 2 cm per allele; rare STC2 alleles act by compromising PAPP-A inhibition and raising IGF bioavailability.'),
   R('hawkes2024','29 independent rare non-coding height associations with effects from -7 cm to +4.7 cm in 333,100 whole genomes, plus a replicated ~5 cm aggregate signal near HMGA1.'),
   R('wainschtein2026','Rare variants account for ~20% and common variants ~68% of pedigree heritability across 34 traits; 79% of the rare-variant component is non-coding.'),
   R('depope2026','Joint WGS modelling identifies 59 rare variants and gene burden scores for height and achieves ~46% polygenic prediction accuracy.'),
 ],
))

write(dict(id='missing_heritability_height', name='Missing heritability of height', aliases=['heritability gap'],
 type='process', layer='L8',
 summary="""The height heritability gap has now been closed to within measurement error, and the answer was
neither epistatics nor gene-environment interaction. Twin and family designs place narrow-sense
heritability around 0.7-0.8; Sidorenko 2024 obtained an unbiased estimate of 0.76 +/- 0.05 using
recombination-rate-stratified identity-by-descent sharing between 119,000 sibling pairs, a design
that avoids the assortative-mating and shared-environment inflation that pedigree correlations
suffer. Yengo 2022 showed that 12,111 common SNPs capture 40% of phenotypic variance in Europeans.
Wainschtein 2026 supplied the bridge: whole-genome sequencing of 347,630 UK Biobank individuals
captures approximately 88% of pedigree-based narrow-sense heritability on average across 34 traits,
with 68% coming from common variants (MAF >= 1%) and 20% from rare variants, and 79% of that rare
component sitting in non-coding sequence. The gap that motivated a decade of theorising was
therefore mostly rare and mostly regulatory variation that the genotyping arrays never assayed, not
a failure of the additive model. Two residual items remain live: Sidorenko 2024 also shows sibling
linkage signals colocalise with GWAS loci and that substantial heritability remains unaccounted for
by GWAS-identified loci, and it is enriched near those same loci - implying the residue is allelic
heterogeneity at known loci rather than unknown biology. The remaining ~12% is not yet partitioned.""",
 quantitative=[
   q('height heritability, sibling IBD design','0.76','proportion of variance','119,000 sibling pairs, recombination-rate-stratified IBD sharing','human','sidorenko2024','SE 0.05'),
   q('fraction of pedigree heritability captured by WGS','88','%','347,630 UK Biobank European-ancestry whole genomes, mean across 34 traits','human','wainschtein2026','trait-level variation; 15 traits showed no significant WGS-pedigree difference'),
   q('heritability from common variants (MAF >= 1%)','68','%','same analysis','human','wainschtein2026','of pedigree heritability'),
   q('heritability from rare variants (MAF < 1%)','20','%','same analysis','human','wainschtein2026','of pedigree heritability'),
   q('phenotypic variance explained by 12,111 common height SNPs, European ancestry','40','%','out-of-sample prediction','human','yengo2022','45% using all HapMap 3 SNPs'),
 ],
 localization=['human: germline, genome-wide'],
 human_evidence='direct',
 human_evidence_note='Three independent human designs - sibling IBD, WGS variance partition, and common-SNP GWAS - measured on the same trait.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human quantitative genetics.',
 confidence='A',
 claim_grades=[
   dict(claim='Whole-genome sequencing accounts for approximately 88% of the pedigree heritability of complex traits, closing most of the height heritability gap.', grade='B', basis='One very large analysis (wainschtein2026); the 88% figure is a cross-trait average and has not been independently replicated at that precision.'),
   dict(claim='The narrow-sense heritability of adult height is about 0.76.', grade='A', basis='Sibling IBD estimate 0.76 +/- 0.05 (sidorenko2024) concordant with 40 twin cohorts spanning birth years 1886-1994 giving 0.69-0.84 in men (jelenkovic2016a).'),
 ],
 key_refs=[
   R('sidorenko2024','Recombination-stratified sibling IBD gives unbiased height heritability 0.76 +/- 0.05 and shows residual heritability is polygenic and enriched near GWAS loci.'),
   R('wainschtein2026','WGS in 347,630 individuals captures ~88% of pedigree heritability: 68% common, 20% rare, with 79% of the rare component non-coding.'),
   R('yengo2022','12,111 independent common SNPs explain 40% of height variance in European-ancestry populations.'),
   R('jelenkovic2016a','Height heritability 0.69-0.84 (men) and 0.53-0.78 (women) across 143,390 twin pairs born 1886-1994, with no secular trend.'),
 ],
))

write(dict(id='height_heritability', name='Heritability of adult height', aliases=['h2 of stature'],
 type='phenotype', layer='L8',
 summary="""Adult height heritability is high, stable across a century of birth cohorts, and age-dependent
within a lifetime. Jelenkovic 2016 pooled 45 twin cohorts from 20 countries with 180,520 paired
measurements at ages 1-19 and found that shared-environment variance is greatest in early
childhood and persists into early adulthood, while the relative genetic contribution rises with age
to a maximum in adolescence of 0.83 in boys and 0.76 in girls. The companion analysis of 40 twin
cohorts and 143,390 complete twin pairs born between 1886 and 1994 found adult heritability
estimates of 0.69-0.84 in men and 0.53-0.78 in women with no clear secular pattern: genetic
variance trended upward across birth years but heritability did not, and total height variance was
greatest in North America and Australia and lowest in East Asia while the heritability proportion
was similar across all three regions. That is a direct refutation, on 143,390 pairs, of the
frequently repeated claim that heritability of height is lower in populations with poorer living
standards and rises as conditions improve. Sidorenko 2024 provides the non-twin cross-check:
recombination-stratified IBD sharing between 119,000 sibling pairs gives 0.76 +/- 0.05, avoiding
the equal-environments assumption entirely and landing inside the twin range. Two independent
designs with different failure modes agreeing to within their standard errors is the strongest form
this estimate can take.""",
 quantitative=[
   q('peak heritability of height in adolescence, boys','0.83','proportion of variance','45 twin cohorts, 20 countries, 180,520 paired measurements ages 1-19','human','jelenkovic2016','upper bound of age-specific estimates'),
   q('peak heritability of height in adolescence, girls','0.76','proportion of variance','same','human','jelenkovic2016','upper bound of age-specific estimates'),
   q('adult height heritability, men','0.69-0.84','proportion of variance','40 twin cohorts, 143,390 complete twin pairs born 1886-1994','human','jelenkovic2016a','range across birth-year cohorts; no secular trend'),
   q('adult height heritability, women','0.53-0.78','proportion of variance','same','human','jelenkovic2016a','range across birth-year cohorts'),
   q('height heritability, sibling IBD design','0.76','proportion of variance','119,000 sibling pairs, recombination-rate-stratified IBD','human','sidorenko2024','SE 0.05'),
 ],
 localization=['human: population-level variance decomposition, not tissue-localized'],
 human_evidence='direct',
 human_evidence_note='Two very large twin pooling analyses plus an independent sibling IBD design, all on measured stature.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human population genetics.',
 confidence='A',
 claim_grades=[
   dict(claim='The narrow-sense heritability of adult height is approximately 0.7-0.8.', grade='A', basis='Twin pooling across 143,390 pairs (jelenkovic2016a) and an independent sibling IBD estimate of 0.76 +/- 0.05 (sidorenko2024) that does not rest on the equal-environments assumption.'),
   dict(claim='Height heritability does not rise with improving living standards.', grade='A', basis='143,390 twin pairs across birth years 1886-1994 and three geographic-cultural regions show no secular pattern (jelenkovic2016a).'),
 ],
 key_refs=[
   R('jelenkovic2016','Pooled 45 twin cohorts: shared-environment variance in height is greatest in early childhood and heritability peaks in adolescence at 0.83 (boys) and 0.76 (girls).'),
   R('jelenkovic2016a','143,390 twin pairs born 1886-1994: adult height heritability 0.69-0.84 (men) and 0.53-0.78 (women) with no secular trend across birth cohorts or regions.'),
   R('sidorenko2024','Sibling IBD design gives height heritability 0.76 +/- 0.05 without the equal-environments assumption.'),
 ],
))
