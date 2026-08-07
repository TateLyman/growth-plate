from w import *

write(dict(id='omnigenic_model', name='Omnigenic model', type='hypothesis', layer='L8',
 aliases=['polygenic to omnigenic'],
 summary="""Boyle 2017 proposed that for complex traits, association signal is spread across most of the genome
- including near many genes with no obvious connection to the trait - because gene regulatory
networks are sufficiently interconnected that any gene expressed in a trait-relevant cell can
affect the function of core trait genes, and that most heritability is explained by effects on
genes outside core pathways. Height is the trait the argument was built on and the trait where it
is most testable. The supporting observations from this atlas are quantitative and independent of
the model's authors: Yengo 2022 found 12,111 independent height SNPs clustered in 7,209 segments
covering about 21% of the genome; the per-allele effect of GDF5-UQCC, a bona fide skeletal
developmental locus, is 0.44 cm, statistically indistinguishable from the 0.4 cm of HMGA2 and no
larger than that of loci with no known skeletal function; and Wood 2014 needed 697 variants to
reach one fifth of heritability while all common variants together captured 60%. Against a strict
core-gene reading, Marouli 2017's 83 rare coding variants of up to 2 cm are concentrated in genes
that are also mutated in monogenic growth disorders, so the effect-size tail does respect a core
gene set even while the common-variant bulk does not. The model is a hypothesis node in this atlas
and is graded as one: the observation that signal is diffuse is A-grade, the mechanistic claim that
diffuseness arises through regulatory-network propagation to core genes has not been directly
tested in any growth-plate system.""",
 quantitative=[
   q('fraction of genome covered by height-associated segments','21','%','union of 7,209 segments containing the 12,111 independent SNPs','human','yengo2022','not reported with CI'),
   q('height heritability captured by 697 genome-wide-significant variants','20','%','n=253,288, European ancestry','human','wood2014','approximately one fifth as reported'),
   q('height heritability captured by all common variants','60','%','same analysis','human','wood2014','as reported'),
   q('variance explained by the ~9,500 most strongly associated SNPs','29','%','phenotypic variance, tested in independent studies','human','wood2014','~21% for top ~2,000 and ~24% for top ~3,700 SNPs'),
 ],
 localization=['human: genome-wide; no tissue localization is claimed'],
 human_evidence='indirect',
 human_evidence_note='The model is an interpretation of human GWAS architecture; the diffuseness observation is direct human data, the network-propagation mechanism is not directly measured.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='A statement about human genetic architecture; no animal inference.',
 confidence='C',
 claim_grades=[
   dict(claim='Height association signal is spread across a large fraction of the genome rather than confined to skeletal pathways.',grade='A',basis='12,111 independent SNPs across 21% of the genome in 5.4M people (yengo2022) and the 697-variant/60% split (wood2014).'),
   dict(claim='Peripheral genes affect height by propagating through regulatory networks onto core growth-plate genes.',grade='E',basis='The mechanistic core of the model; not tested in chondrocytes or any growth-plate system. Flagged as inference.'),
   dict(claim='Large-effect variants are concentrated in a core gene set even though common-variant signal is not.',grade='B',basis='83 rare coding variants of up to 2 cm overlap monogenic growth-disorder genes (marouli2017); a single analysis, but internally consistent with the monogenic literature in this layer.'),
 ],
 key_refs=[
   R('boyle2017','Proposes that interconnected regulatory networks let all genes expressed in trait-relevant cells affect core genes, so most heritability lies outside core pathways.'),
   R('yengo2022','12,111 independent height SNPs cluster in 7,209 segments covering ~21% of the genome.'),
   R('wood2014','697 variants explain one fifth of height heritability while all common variants capture 60%.'),
   R('marouli2017','Rare coding variants of up to 2 cm per allele overlap genes mutated in monogenic growth disorders.'),
 ],
 open_questions=['g_l8gen_010'],
))

write(dict(id='height_polygenic_score', name='Height polygenic score', type='method', layer='L8',
 aliases=['height PGS','height polygenic risk score'],
 summary="""A height polygenic score sums allele dosages weighted by GWAS effect sizes and is the best-performing
polygenic predictor of any human quantitative trait, which makes it the ceiling case for what
polygenic prediction can do. Yengo 2022 reported that the 12,111 genome-wide-significant SNPs
account for 40% of phenotypic variance in European-ancestry out-of-sample prediction, rising to 45%
using all HapMap 3 SNPs, and falling to about 10-20% (14-24% with all HapMap 3 SNPs) in populations
of other ancestries. Depope 2026 reached a comparable ceiling by a different route, jointly
modelling tens of millions of UK Biobank whole-genome-sequence variants with approximate message
passing and obtaining about 46% prediction accuracy for height. Against a narrow-sense heritability
of about 0.76, a 40-46% predictor captures roughly 55-60% of the genetic variance and essentially
all of the common-variant component - the residual is the rare and non-coding tier that
Wainschtein 2026 quantifies at 20% of pedigree heritability. Two limits are structural rather than
technical. First, prediction accuracy is not transferable across ancestries because it depends on
linkage disequilibrium and allele frequency in the training population, not because the biology
differs. Second, a score trained in a population with assortative mating carries inflated effect
estimates, since assortment raises the genetic variance of the trait and induces correlations
between causal alleles.""",
 quantitative=[
   q('phenotypic variance explained, European ancestry','40','%','12,111 genome-wide-significant SNPs, out-of-sample prediction','human','yengo2022','45% using all HapMap 3 SNPs'),
   q('phenotypic variance explained, non-European ancestries','10-20','%','same score, out-of-sample','human','yengo2022','14-24% using all HapMap 3 SNPs'),
   q('prediction accuracy from joint WGS modelling','46','%','gVAMP applied to tens of millions of UK Biobank WGS variants','human','depope2026','approximate as reported'),
   q('narrow-sense heritability benchmark','0.76','proportion of variance','119,000 sibling pairs, IBD design','human','sidorenko2024','SE 0.05'),
 ],
 localization=['human: germline genome-wide; a statistical construct, not tissue-localized'],
 human_evidence='direct',
 human_evidence_note='Out-of-sample prediction accuracy measured against observed stature in independent human cohorts.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human prediction method.',
 confidence='A',
 key_refs=[
   R('yengo2022','Height PGS explains 40% of variance in European-ancestry and 10-20% in other-ancestry populations out of sample.'),
   R('depope2026','Joint WGS modelling by approximate message passing reaches ~46% prediction accuracy for height.'),
   R('sidorenko2024','Height heritability 0.76 +/- 0.05 provides the benchmark against which PGS accuracy is judged.'),
   R('sunde2024','Assortative mating raises trait genetic variance and similarity between relatives, biasing PGS-derived estimates trained in assorting populations.'),
 ],
))

write(dict(id='pgs_ancestry_transferability', name='PGS ancestry transferability', type='process', layer='L8',
 aliases=['portability of polygenic scores','cross-ancestry prediction'],
 summary="""Height polygenic scores lose most of their accuracy outside the ancestry group they were trained in,
and the height literature is unusually well placed to say why, because the same paper that measures
the loss also tests the two candidate explanations. Yengo 2022 found that the 12,111 SNPs explain
40% of variance in European-ancestry populations but only about 10-20% in others, while per-allele
effect sizes, associated regions and prioritised genes were similar across ancestries. That
similarity is the discriminating observation: it excludes the interpretation that height has a
different genetic basis in different populations and localises the failure to linkage disequilibrium
and allele frequency differences within associated regions - a property of the study design and the
marker panel rather than of the biology. Graff 2021 supports the same conclusion from the other
direction: in an African-ancestry meta-analysis of 52,764 individuals, 643 of 802 known European
height signals were directionally consistent and 205 were nominally significant, and only 2 of 20
newly identified secondary signals had minor allele frequency below 5%. The practical consequence
for this atlas is that any claim of the form 'this locus explains X% of height' is a claim about a
population and a marker panel, not about a mechanism, and none of the growth-plate mechanism nodes
inherit an ancestry qualifier from it.""",
 quantitative=[
   q('height variance explained by PGS, European ancestry','40','%','12,111 SNPs, out-of-sample','human','yengo2022','45% with all HapMap 3 SNPs'),
   q('height variance explained by PGS, non-European ancestries','10-20','%','same score, out-of-sample','human','yengo2022','14-24% with all HapMap 3 SNPs'),
   q('European height signals directionally consistent in African ancestry','643','of 802 signals','African Ancestry Anthropometry Genetics Consortium, n=52,764','human','graff2021','205 of the 643 were nominally significant at P<0.05'),
   q('new African-ancestry secondary signals with MAF < 5%','2','of 20 signals','same analysis','human','graff2021','not applicable (count)'),
 ],
 localization=['human: population-level property of marker panels, not tissue-localized'],
 human_evidence='direct',
 human_evidence_note='Two independent human analyses measuring cross-ancestry prediction accuracy and signal concordance.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Between-population, not between-species, transfer.',
 confidence='A',
 claim_grades=[
   dict(claim='Height PGS accuracy falls by roughly half to three quarters outside the training ancestry.',grade='A',basis='Measured out of sample in yengo2022 and corroborated by partial signal transfer in graff2021.'),
   dict(claim='The loss is caused by linkage disequilibrium and allele frequency differences rather than different underlying biology.',grade='B',basis='Supported by similar per-allele effect sizes and gene prioritisation across ancestries within yengo2022 and by 643/802 directional concordance in graff2021, but not established by a purpose-designed decomposition.'),
 ],
 key_refs=[
   R('yengo2022','PGS variance explained falls from 40% (European) to 10-20% (other ancestries) despite similar effect sizes and prioritised genes across ancestries.'),
   R('graff2021','643 of 802 European height signals are directionally consistent in 52,764 African-ancestry individuals; 205 nominally significant.'),
 ],
))

write(dict(id='mendelian_randomization_height', name='Mendelian randomization using height', type='method', layer='L8',
 aliases=['MR of height','height as an instrument'],
 summary="""Height is the workhorse exposure and outcome for Mendelian randomization because it has thousands of
strong instruments, is measured without error, and cannot be reverse-caused by most outcomes of
interest. Two uses matter for this atlas. Used as an outcome, MR converts endocrine correlations
into causal slopes: De La Barrera 2026 instrumented serum IGF-1 with UK Biobank variants and tested
against GIANT height excluding UK Biobank (non-Hispanic White n=1,176,465, plus African descent
168,191, South Asian 49,032, East Asian 361,369 and Hispanic 58,709), obtaining 0.09 SD taller
adult height per 1 SD higher IGF-1 by inverse-variance weighting, persisting after adjustment for
childhood BMI and replicated longitudinally against measured heights at ages 7-17 in ALSPAC. That
number puts a hard ceiling on how much of normal stature variation the IGF-1 axis explains, and it
sits alongside the Laron and IGFALS phenotypes as the population-scale version of the same axis.
Used as an exposure, height MR consistently estimates effects on cardiovascular and other outcomes,
but those analyses are outside this atlas's scope. The methodological caveat that matters here is
that assortative mating for height induces correlations between causal alleles and inflates genetic
variance, which biases MR estimates that use height instruments unless family-based designs are
used - a caveat that applies specifically and strongly to this trait.""",
 quantitative=[
   q('adult height change per 1 SD genetically predicted serum IGF-1','0.09','SD','two-sample MR, inverse-variance weighted, GIANT excluding UK Biobank across five ancestry groups','human','de2026','persisted after adjustment for childhood BMI; replicated in ALSPAC ages 7-17'),
   q('GIANT non-Hispanic White outcome sample','1176465','individuals','plus 168,191 African descent, 49,032 South Asian, 361,369 East Asian, 58,709 Hispanic','human','de2026','not applicable (count)'),
 ],
 localization=['human: population-level instrumental-variable analysis'],
 human_evidence='direct',
 human_evidence_note='Human genetic instruments against measured human stature, with a longitudinal cohort replication.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human epidemiological method.',
 confidence='B',
 claim_grades=[
   dict(claim='Higher circulating IGF-1 causally increases adult height by about 0.09 SD per SD.',grade='A',basis='Two-sample MR in >1.8M individuals with an independent ALSPAC longitudinal replication using both measured IGF-1 and an IGF-1 genetic risk score (de2026).'),
   dict(claim='Height MR estimates are unbiased in populations with assortative mating.',grade='D',basis='Not supported. Assortative mating induces gametic-phase correlations between causal alleles (sunde2024), which biases population-based MR using height instruments; family-based designs are required.'),
 ],
 key_refs=[
   R('de2026','MR gives 0.09 SD taller adult height per 1 SD higher serum IGF-1, replicated against repeated height measurements at ages 7-17 in ALSPAC.'),
   R('sunde2024','Assortative mating increases trait-specific genetic variance and genetic similarity between relatives, a source of bias for height-instrument designs.'),
   R('yengo2022','Supplies the instrument set: 12,111 conditionally independent height SNPs from 5.4M individuals.'),
 ],
))

write(dict(id='assortative_mating_height', name='Assortative mating for height', type='process', layer='L8',
 aliases=['homogamy for stature'],
 summary="""Height is one of the traits for which assortative mating is genetically detectable, and it matters
for this atlas because it inflates every quantitative-genetic parameter derived from relatives.
Sunde 2024 showed theoretically and empirically that assortative mating raises trait-specific
genetic variance and genetic similarity between relatives, and that distant relatives are more
affected than close ones - a signature that lets the history of assortment be read from
present-day data. Correlating polygenic indices in 47,135 co-parents from the Norwegian Mother,
Father and Child Cohort Study gave genetic evidence of assortative mating in nine of sixteen traits
examined, and the same traits showed elevated similarity between relatives, especially distant
ones. For six of the nine traits the offspring generation showed greater genetic variance than
stable long-run assortment would produce, implying assortment is recent or intensifying rather than
at equilibrium. Three consequences follow for L8. Twin heritability estimates are biased upward
because assortment increases dizygotic but not monozygotic genetic correlation. Polygenic score
weights trained in an assorting population absorb the induced gametic-phase disequilibrium between
causal alleles. And Mendelian randomization using height instruments inherits the same bias unless
family-based designs are used. The magnitude of the height-specific inflation is not quantified in
the sources reached here, which is the main quantitative gap on this node.""",
 quantitative=[
   q('co-parent pairs with polygenic indices analysed','47135','co-parents','Norwegian Mother, Father and Child Cohort Study (MoBa)','human','sunde2024','not applicable (count)'),
   q('traits with genetic evidence of assortative mating','9','of 16 traits','polygenic index correlation between co-parents','human','sunde2024','not applicable (count)'),
   q('traits showing offspring genetic variance inconsistent with equilibrium assortment','6','of 9 traits','same analysis','human','sunde2024','interpreted as recent or intensifying assortment'),
 ],
 localization=['human: population mating structure, not tissue-localized'],
 human_evidence='direct',
 human_evidence_note='Polygenic indices measured in 47,135 human co-parents plus relative-similarity patterns across a national cohort.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human population structure.',
 confidence='B',
 claim_grades=[
   dict(claim='Assortative mating is genetically detectable and raises genetic variance and relative similarity for assorted traits.',grade='A',basis='Path-analytic prediction plus empirical confirmation in 47,135 co-parents with the predicted distant-versus-close relative gradient (sunde2024).'),
   dict(claim='Assortative mating for height specifically inflates height heritability estimates by a quantified amount.',grade='D',basis='No height-specific inflation magnitude was located; the effect is established in principle and for the trait class but not measured for stature. See gap g_l8gen_011.'),
 ],
 key_refs=[
   R('sunde2024','Genetic evidence of assortative mating in 9 of 16 traits among 47,135 MoBa co-parents, with elevated similarity between distant relatives and offspring genetic variance inconsistent with equilibrium assortment.'),
   R('sidorenko2024','Sibling IBD heritability design chosen partly because it is less exposed to assortative-mating inflation than pedigree correlations.'),
 ],
 open_questions=['g_l8gen_011'],
))

write(dict(id='gene_environment_interaction_height', name='Gene-environment interaction in height', type='process', layer='L8',
 aliases=['GxE for stature'],
 summary="""The default expectation - that height heritability should be low in deprived populations because
environmental variance dominates, and should rise as living standards improve - has been tested at
large scale and is not supported. Jelenkovic 2016 pooled 40 twin cohorts with 143,390 complete twin
pairs born between 1886 and 1994 and found adult heritability of 0.69-0.84 in men and 0.53-0.78 in
women with no clear secular pattern across birth-year cohorts; genetic variance did trend upward,
but so did total variance, leaving the ratio flat. Comparing Europe, North America and Australia,
and East Asia, total height variance was greatest in North America and Australia and lowest in East
Asia, yet the heritability proportion was similar across all three. The companion developmental
analysis of 45 twin cohorts (180,520 paired measurements, ages 1-19) locates the environmental
signal where it actually is: shared-environment variance is greatest in early childhood and
persists until early adulthood, while the relative genetic contribution rises with age. A
purpose-built test of the socioeconomic hypothesis reached the same negative conclusion: pooling 29
cohorts and 65,978 twin pairs with parental education data, parental education was positively
associated with offspring height from mid-childhood onward but the genetic and environmental
variance components showed no consistent relation to it, with only a weak meta-regression trend
toward greater shared-environmental variance in low-education families. So the environment shifts
the mean of height strongly and reproducibly, while leaving the variance decomposition close to
unchanged - which is a different statement from 'no gene-environment interaction' but is the one
the data support.""",
 quantitative=[
   q('adult height heritability across birth years 1886-1994, men','0.69-0.84','h2','40 twin cohorts, 143,390 complete twin pairs; no clear secular pattern','human','jelenkovic2016a','range across birth-year cohorts'),
   q('adult height heritability across birth years 1886-1994, women','0.53-0.78','h2','same','human','jelenkovic2016a','range across birth-year cohorts'),
   q('twin pairs tested for parental-education moderation of height variance','65978','complete twin pairs','29 cohorts, ages 1-69, three geographic-cultural regions','human','jelenkovic2020','no consistent relation of variance components to parental education'),
   q('peak adolescent heritability, boys','0.83','h2','45 twin cohorts, 180,520 paired measurements ages 1-19','human','jelenkovic2016','age-specific maximum'),
 ],
 localization=['human: population-level variance decomposition'],
 human_evidence='direct',
 human_evidence_note='Three pooled twin analyses covering over 200,000 twin pairs across 20+ countries and a century of birth years.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human population genetics.',
 confidence='A',
 claim_grades=[
   dict(claim='Height heritability does not increase with improving living standards or higher parental education.',grade='A',basis='143,390 twin pairs across birth years 1886-1994 and three regions (jelenkovic2016a) plus a purpose-designed 65,978-pair parental-education test (jelenkovic2020), by overlapping but independently analysed designs.'),
   dict(claim='Shared environment contributes most to height variance in early childhood and declines thereafter.',grade='A',basis='45-cohort developmental decomposition with 180,520 paired measurements (jelenkovic2016).'),
 ],
 key_refs=[
   R('jelenkovic2016a','143,390 twin pairs born 1886-1994: no secular change in height heritability despite rising genetic variance; heritability proportion similar across three world regions.'),
   R('jelenkovic2016','Shared-environment variance in height is greatest in early childhood; heritability rises with age to 0.83 (boys) and 0.76 (girls) in adolescence.'),
 ],
 open_questions=['g_l8gen_012'],
))
