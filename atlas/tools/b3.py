from w import *

write(dict(id='ghr_gene', name='GHR', type='gene', layer='L8',
 aliases=['growth hormone receptor gene','Laron gene'],
 summary="""GHR is the human experiment that separates growth hormone secretion from growth hormone action.
Godowski 1989 determined the nine-exon coding structure of the receptor gene on chromosome 5 and
showed that two of nine Laron-type dwarfism patients carried a deletion removing a large,
non-consecutive part of the extracellular hormone-binding domain. Amselem 1989 independently
demonstrated linkage of the disease trait to intragenic GHR markers in two consanguineous
Mediterranean families and identified a thymidine-to-cytosine substitution replacing phenylalanine
96 with serine in the extracellular domain, absent from seven unrelated Laron patients of other
population groups - so the disorder is genetically heterogeneous but locus-specific. The
phenotypic consequence of biallelic GHR loss is the largest monogenic stature effect in this
atlas: Laron syndrome patients in the 69-patient Israeli cohort span -4 to -10 height SDS, with
high circulating GH and low IGF-1, retarded bone age and delayed sexual development. Only
homozygotes express the disease. The mechanistic value of GHR is that it fixes the causal
direction of the somatomedin hypothesis in humans: abolishing the receptor while leaving the
ligand elevated produces near-complete growth failure, which no amount of GH can rescue and which
IGF-1 replacement partially does.""",
 quantitative=[
   q('adult height deficit, homozygous GHR loss of function (Laron syndrome)','-4 to -10','SDS','69-patient cohort followed >50 years; Jews of oriental origin, Muslims and Christians of Middle Eastern/Mediterranean origin','human','laron2015','range as reported across the cohort'),
   q('Laron patients with a large GHR extracellular-domain deletion','2','of 9 patients','gene-structure and Southern analysis of the GHR locus','human','godowski1989','not applicable (count)'),
   q('GHR coding sequence span on chromosome 5','87','kb','nine coding exons plus additional 5-prime untranslated exons','human','godowski1989','at least; lower bound as reported'),
 ],
 localization=['human: germline; receptor expressed in liver and in growth plate chondrocytes'],
 human_evidence='direct',
 human_evidence_note='Biallelic loss-of-function humans with measured height SDS across a 69-patient cohort followed for over 50 years, plus two independent 1989 gene-level identifications.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human genotype-to-stature data; the Ghr-knockout mouse is not used to support any claim here.',
 confidence='A',
 key_refs=[
   R('godowski1989','The human GHR gene has nine coding exons over at least 87 kb of chromosome 5; two of nine Laron patients carry a deletion of the extracellular hormone-binding domain.'),
   R('amselem1989','Laron dwarfism segregates with intragenic GHR markers and a p.Phe96Ser substitution in the extracellular domain in consanguineous Mediterranean families.'),
   R('laron2015','69-patient Laron syndrome cohort followed for over 50 years spans -4 to -10 height SDS with high GH and low IGF-1; only homozygotes express the disease.'),
 ],
))

write(dict(id='igf1_gene', name='IGF1', type='gene', layer='L8',
 aliases=['insulin-like growth factor 1 gene'],
 summary="""IGF1 supplies the human null experiment that the GH receptor cannot: Woods 1996 described a patient
with a homozygous partial deletion of the IGF1 gene presenting with intrauterine growth
retardation followed by continued postnatal growth failure, together with sensorineural deafness
and mental retardation. The combination is what makes the locus informative. Growth hormone
deficiency and GH receptor deficiency both spare prenatal growth, because fetal growth is largely
GH-independent, whereas IGF1 deletion impairs growth from before birth - so the IGF1 gene sits
downstream of the point at which the somatotropic axis becomes GH-dependent, and IGF-1 itself is
required in both epochs. The extra-skeletal features (deafness, cognitive impairment) establish
that IGF-1 action is not confined to the growth plate, which is a constraint on any therapeutic
strategy that raises systemic IGF-1 to gain stature. On the common-variation side of the same
locus, Mendelian randomisation now shows the relationship is continuous rather than confined to
null alleles: instrumenting serum IGF-1 with UK Biobank variants and testing against GIANT height
gives 0.09 SD taller adult height per 1 SD higher IGF-1, an effect that persists after adjustment
for childhood BMI and is reproduced by an IGF-1 genetic risk score against measured heights at ages
7-17 in ALSPAC. The gap between a catastrophic null phenotype and a 0.09 SD per SD population slope
is the quantitative statement of how strongly buffered this axis is.""",
 quantitative=[
   q('adult height change per 1 SD genetically predicted serum IGF-1','0.09','SD','two-sample Mendelian randomization, inverse-variance weighted; GIANT height excluding UK Biobank (non-Hispanic White n=1,176,465 plus four other ancestry groups)','human','de2026','persists after adjustment for childhood BMI'),
 ],
 localization=['human: germline; IGF-1 produced systemically by liver and locally within the growth plate'],
 human_evidence='direct',
 human_evidence_note='One homozygous human deletion patient plus a large-scale Mendelian randomization estimate of the continuous IGF-1 to height slope.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Both the null phenotype and the population slope are measured in humans.',
 confidence='B',
 claim_grades=[
   dict(claim='Homozygous IGF1 deletion causes combined pre- and postnatal growth failure with deafness and cognitive impairment.', grade='D', basis='Single patient (woods1996); later IGF1 point-mutation patients exist but were not independently verified in this sweep.'),
   dict(claim='Higher circulating IGF-1 causally increases adult height by about 0.09 SD per SD.', grade='A', basis='Two-sample MR in >1.1M individuals with an independent longitudinal replication in ALSPAC (de2026).'),
 ],
 key_refs=[
   R('woods1996','Homozygous partial deletion of IGF1 causes intrauterine growth retardation with postnatal growth failure, deafness and mental retardation.'),
   R('de2026','Mendelian randomization gives 0.09 SD taller adult height per 1 SD higher serum IGF-1, replicated against measured heights at ages 7-17 in ALSPAC.'),
 ],
))

write(dict(id='igf1r_gene', name='IGF1R', type='gene', layer='L8',
 aliases=['type 1 IGF receptor gene'],
 summary="""IGF1R is the receptor-side counterpart to IGF1 and is the locus that explains a specific clinical
puzzle: children born small for gestational age who fail to catch up and whose serum IGF-1 is
normal or high rather than low. Abuzzahab 2003 screened 42 patients with unexplained intrauterine
growth retardation and persistent short stature plus a second cohort of 50 short children with
elevated circulating IGF-1, and found a girl who was a compound heterozygote for two exon-2 point
mutations (Arg108Gln and Lys115Asn) whose fibroblasts showed decreased IGF-I binding, establishing
partial IGF1R loss of function as a cause of combined prenatal and postnatal growth failure. The
receptor is haploinsufficiency-sensitive: heterozygous nonsense and deletion alleles are now
recurrently reported in severe short stature with poor growth hormone response, because the defect
is downstream of the ligand that GH raises. The signature - low birth size, no catch-up, normal or
raised IGF-1, blunted rhGH response - is the mirror image of the GHR/Laron signature (normal birth
size, high GH, low IGF-1). Together IGF1, IGF1R and GHR partition the somatotropic axis into
prenatal-competent and prenatal-independent segments using nothing but human alleles. The
quantitative weakness is that no adequately powered genotype-defined IGF1R cohort with mean adult
height SDS was reached in this sweep.""",
 quantitative=[
   q('patients screened with unexplained IUGR plus short stature','42','patients','single-strand conformation polymorphism screening of IGF1R followed by sequencing','human','abuzzahab2003','not applicable (count)'),
   q('additional patients screened with short stature and elevated IGF-1','50','patients','complete IGF1R sequencing in 9 of these','human','abuzzahab2003','not applicable (count)'),
 ],
 localization=['human: germline; receptor expressed in growth plate chondrocytes and near-ubiquitously'],
 human_evidence='direct',
 human_evidence_note='Human compound-heterozygote patient with fibroblast binding assay; the phenotype has been recurrently reported since.',
 species_basis=['human','in_vitro_human_cell'],
 translation_risk='not_applicable',
 translation_risk_reason='Human alleles with patient-derived fibroblast assays.',
 confidence='B',
 key_refs=[
   R('abuzzahab2003','IGF1R compound-heterozygous exon-2 mutations reduce IGF-I binding in patient fibroblasts and cause intrauterine plus postnatal growth retardation.'),
   R('de2026','Mendelian randomization of the IGF-1 axis gives 0.09 SD taller adult height per 1 SD higher serum IGF-1.'),
 ],
 open_questions=['g_l8gen_007'],
))

write(dict(id='igfals_gene', name='IGFALS', type='gene', layer='L8',
 aliases=['acid-labile subunit gene','ALS gene'],
 summary="""IGFALS encodes the acid-labile subunit that, with IGFBP-3 or IGFBP-5, forms the 150 kDa ternary
complex holding IGF-1 and IGF-2 in circulation. Domene 2004 identified the first inactivating
IGFALS mutation and showed that it collapses the whole circulating IGF system. The subsequent
14-mutation, 17-patient review (Domene 2009) gives the number that matters for this atlas: despite
extraordinarily low serum IGF-1 and IGFBP-3 that fail to rise on GH stimulation, prepubertal height
SDS was typically only between -2 and -3, about 1.4 SD below midparental height SDS. That is a
remarkably mild stature phenotype for a near-total loss of circulating IGF-1 carriage, and it is
the strongest human argument in the atlas that the growth plate is driven principally by locally
produced or locally bioavailable IGF-1 rather than by the size of the circulating reservoir.
Pubertal delay occurred in half of patients and insulin insensitivity was common, so the complex is
not functionally inert. IGFALS therefore functions as a dosage control that dissociates circulating
IGF-1 concentration from linear growth - the same dissociation PAPPA2 makes from the opposite
direction, by trapping IGF-1 in an intact complex.""",
 quantitative=[
   q('prepubertal height SDS, IGFALS deficiency','-2 to -3','SDS','17 patients carrying 14 distinct IGFALS mutations','human','domen2009','typical range as reported'),
   q('height deficit relative to midparental height SDS','-1.4','SDS','same patient series','human','domen2009','approximate as reported'),
   q('patients with pubertal delay','50','%','same series','human','domen2009','not applicable (proportion)'),
 ],
 localization=['human: germline; ALS protein is hepatically produced and circulates'],
 human_evidence='direct',
 human_evidence_note='17 human patients with 14 distinct mutations, measured heights and full IGF-axis biochemistry.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human loss-of-function series only.',
 confidence='A',
 claim_grades=[
   dict(claim='IGFALS inactivation collapses the circulating IGF ternary complex.', grade='A', basis='Original inactivating mutation with biochemistry (domen2004) and 17 patients with concordant IGF-1/IGFBP-3/ALS profiles (domen2009).'),
   dict(claim='The stature cost of that collapse is only about -1.4 SDS relative to midparental height.', grade='B', basis='One aggregated patient series (domen2009); the estimate has not been reproduced in an independent cohort.'),
 ],
 key_refs=[
   R('domen2004','Inactivation of the IGFALS gene produces a deficiency of the entire circulating insulin-like growth factor system.'),
   R('domen2009','17 ALS-deficient patients with 14 mutations: prepubertal height SDS -2 to -3, about 1.4 SD below midparental height, with pubertal delay in 50%.'),
 ],
))

write(dict(id='pappa2_gene', name='PAPPA2', type='gene', layer='L8',
 aliases=['pregnancy-associated plasma protein A2 gene','PAPP-A2 gene'],
 summary="""PAPPA2 encodes the metalloproteinase that liberates IGF-1 from IGFBP-3 and IGFBP-5, and its human
loss-of-function phenotype is the cleanest available demonstration that free rather than total
IGF-1 drives growth. Dauber 2016 found two different homozygous PAPPA2 mutations, p.D643fs25* and
p.Ala1033Val, in multiple members of two unrelated families with progressive growth failure,
moderate microcephaly, thin long bones and mildly decreased bone density. The biochemical signature
is inverted relative to every other short-stature endocrinopathy: circulating total IGF-1, IGFBP-3,
IGFBP-5, acid-labile subunit and IGF-II were all elevated, not reduced. In vitro both mutations
abolished PAPP-A2 proteolytic activity entirely, size-exclusion chromatography showed a significant
increase in IGF-1 held within the ternary complex, and free IGF-1 concentrations were decreased.
The gene therefore separates two quantities that are normally measured as one: total IGF-1 goes up
while the growth-relevant fraction goes down, and the child gets shorter. Any clinical inference
that reads total serum IGF-1 as a proxy for IGF-1 action is falsified by this locus. Its
therapeutic corollary - that recombinant IGF-1 bypasses the block - has been tested in these
patients, and PAPPA2 deficiency now sits in the growth-plate basket of the vosoritide RASopathy
trial programme alongside ACAN and NPR2.""",
 quantitative=[
   q('distinct homozygous PAPPA2 mutations identified','2','mutations','p.D643fs25* and p.Ala1033Val in two unrelated families','human','dauber2016','not applicable (count)'),
   q('PAPP-A2 proteolytic activity, both mutant alleles','0','% of wild type','in vitro IGFBP-3 and IGFBP-5 cleavage assay','in_vitro_human_cell','dauber2016','complete absence of activity as reported'),
   q('direction of change in total circulating IGF-1','elevated','qualitative','patients versus reference; IGFBP-3, IGFBP-5, ALS and IGF-II also elevated','human','dauber2016','no numeric fold-change given in abstract'),
   q('direction of change in free IGF-1','decreased','qualitative','same patients; size-exclusion chromatography showed increased ternary-complex-bound IGF-1','human','dauber2016','no numeric value given in abstract'),
 ],
 localization=['human: germline; protease acts in the circulation and in the pericellular space'],
 human_evidence='direct',
 human_evidence_note='Two unrelated consanguineous families with homozygous mutations, full IGF-axis biochemistry and matched in vitro proteolysis assays.',
 species_basis=['human','in_vitro_human_cell'],
 translation_risk='not_applicable',
 translation_risk_reason='Human loss-of-function families with human-protein enzymology.',
 confidence='B',
 claim_grades=[
   dict(claim='Loss of PAPP-A2 proteolytic activity causes short stature despite elevated total IGF-1.', grade='A', basis='Two unrelated families with independent mutations and concordant inverted biochemistry (dauber2016).'),
   dict(claim='The proximate cause of the growth failure is reduced free IGF-1 rather than another PAPP-A2 substrate.', grade='C', basis='Supported by the chromatography and free-IGF-1 measurements in dauber2016 but not tested against an alternative-substrate hypothesis; single study.'),
 ],
 key_refs=[
   R('dauber2016','Two homozygous PAPPA2 mutations abolish IGFBP proteolysis, raising total but lowering free IGF-1 and causing progressive growth failure in two unrelated families.'),
   R('dauber2026','Vosoritide basket trial enrolling children with ACAN and NPR2 deficiency and RASopathies, the therapeutic context in which these growth-plate genotypes are now grouped.'),
 ],
))

write(dict(id='stat5b_gene', name='STAT5B', type='gene', layer='L8',
 aliases=['signal transducer and activator of transcription 5B gene'],
 summary="""STAT5B is the transcription factor through which the growth hormone receptor drives IGF1
transcription, and human STAT5B deficiency is the experiment that places the defect below the
receptor while keeping the receptor intact. Kofoed 2003 reported the first patient: severe growth
hormone insensitivity with normal-to-elevated GH and GH-binding protein but very low IGF-1, caused
by a homozygous STAT5B mutation, and accompanied by immune dysfunction - because STAT5B also
transduces interleukin-2 receptor signalling, so the same allele produces growth failure and
lymphoid disease together. Hwa 2005 characterised a second patient from a consanguineous pedigree
with a novel homozygous insertion causing total absence of STAT5B protein; she measured 114 cm at
16.4 years, a height SDS of -7.8, with IGF-1 at 7.2 ng/ml against a normal range of 242-600,
IGFBP-3 at 543 against 2500-4800, and acid-labile subunit at 1.22 microg/ml against 5.6-16, none of
which rose during an IGF-1 generation test. The severity is the point: STAT5B nullizygosity gives a
larger stature deficit than IGFALS deficiency by roughly 5 SDS despite both collapsing circulating
IGF-1, because STAT5B loss also removes locally transcribed IGF-1 and the immune phenotype adds
morbidity. The combination of near-absent IGF-1 and a failed generation test with a structurally
normal GH receptor is the diagnostic fingerprint that distinguishes it from Laron syndrome.""",
 quantitative=[
   q('height SDS, homozygous STAT5B null','-7.8','SDS','female, 114 cm at 16.4 years, consanguineous pedigree','human','hwa2005','n=1'),
   q('serum IGF-1, homozygous STAT5B null','7.2','ng/ml','same patient; laboratory normal range 242-600 ng/ml','human','hwa2005','failed to rise during an IGF-1 generation test'),
   q('serum IGFBP-3, homozygous STAT5B null','543','ng/ml','same patient; normal range 2500-4800 ng/ml','human','hwa2005','n=1'),
   q('serum acid-labile subunit, homozygous STAT5B null','1.22','microg/ml','same patient; normal range 5.6-16 microg/ml','human','hwa2005','n=1'),
 ],
 localization=['human: germline; STAT5B transduces GH receptor signalling in liver and growth plate and IL-2 receptor signalling in lymphocytes'],
 human_evidence='direct',
 human_evidence_note='Two independent homozygous human patients with full GH-IGF axis biochemistry and an IGF-1 generation test.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human loss-of-function patients only.',
 confidence='B',
 claim_grades=[
   dict(claim='Homozygous STAT5B loss causes severe growth hormone insensitivity with normal GH receptor.', grade='A', basis='Two independent patients from unrelated pedigrees with concordant biochemistry (kofoed2003, hwa2005).'),
   dict(claim='The stature deficit of STAT5B nullizygosity is about -7.8 SDS.', grade='D', basis='Single measured patient (hwa2005); no genotype-defined cohort mean exists.'),
 ],
 key_refs=[
   R('kofoed2003','A homozygous STAT5B mutation causes growth hormone insensitivity with normal GH and GH-binding protein but low IGF-1, plus immune dysfunction.'),
   R('hwa2005','Total absence of STAT5B protein gives height -7.8 SDS with IGF-1 7.2 ng/ml (normal 242-600) and no response to an IGF-1 generation test.'),
 ],
))
