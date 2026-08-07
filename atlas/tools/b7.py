from w import *

write(dict(id='dominant_negative_vs_haploinsufficiency', name='Dominant-negative versus haploinsufficiency dose effects',
 type='process', layer='L8',
 aliases=['mutation class and effect size','poison-subunit versus reduced-dosage'],
 summary="""Two heterozygous alleles of the same gene can produce very different phenotypes depending on whether
the mutant product is absent or present-but-defective, and the growth plate provides the cleanest
human measurement of that difference anywhere in medicine. In COL10A1 metaphyseal chondrodysplasia
Schmid, Meng 2025 pooled 4 new and 124 published cases and found height Z of -3.62 +/- 1.95 for
missense variants versus -1.99 +/- 1.28 for truncating variants (P = 0.013), with more metaphyseal
irregularity in the missense group (P = 0.019). Truncating COL10A1 transcripts are degraded by
nonsense-mediated decay, leaving one functional allele; missense alleles make a stable chain that
disrupts trimerisation of the wild-type product, as Yang 2025 demonstrated directly for the
p.W651fsX666 allele. Dominant-negative interference therefore costs about 1.6 SDS more stature than
losing one copy outright, at the same locus, in the same disease. The same logic explains why
COL2A1 glycine substitutions give lethal-to-severe type II collagenopathies while whole-gene
deletions give the mild Stickler spectrum, and why COMP missense variants concentrated in the
type-3 calcium-binding repeat (87.7% of 471 probands) are cytotoxic through ER retention rather
than dosage-limiting. The generalisation has a documented exception within this layer: in ACAN,
Gkourogianni 2017 found no genotype-phenotype correlation between mutation class and joint
involvement across 20 families, so the dominant-negative premium is locus-specific and must be
demonstrated rather than assumed.""",
 quantitative=[
   q('height Z, COL10A1 missense (dominant-negative)','-3.62','SDS','128 metaphyseal chondrodysplasia Schmid cases','human','meng2025','SD 1.95; P=0.013 versus truncating'),
   q('height Z, COL10A1 truncating (haploinsufficiency)','-1.99','SDS','same cohort','human','meng2025','SD 1.28'),
   q('stature premium of dominant-negative over haploinsufficient COL10A1 alleles','1.63','SDS','difference of the two group means','human','meng2025','derived from the reported means; no CI on the difference is published'),
   q('COMP probands with a variant in the type-3 calcium-binding repeat','87.7','%','413 of 471 probands across 106 publications','human','ni2026','80.8% of all COMP variants are missense'),
 ],
 localization=['human: applies at any locus whose product is a multimer or matrix assembly'],
 human_evidence='direct',
 human_evidence_note='Direct human height comparison between mutation classes at a single locus, with an in vitro trimerisation assay establishing the mechanism.',
 species_basis=['human','in_vitro_human_cell'],
 translation_risk='not_applicable',
 translation_risk_reason='Human genotype-phenotype comparison with human-protein biochemistry.',
 confidence='B',
 claim_grades=[
   dict(claim='At COL10A1, dominant-negative missense alleles reduce stature more than haploinsufficient truncating alleles.',grade='B',basis='One pooled 128-case cohort with P=0.013 (meng2025), mechanistically corroborated by an independent trimerisation assay (yang2025); the height comparison itself has not been repeated in a second cohort.'),
   dict(claim='The dominant-negative premium generalises across matrix-protein loci.',grade='C',basis='Consistent with the COL2A1 and COMP genotype-phenotype patterns but explicitly absent in ACAN (gkourogianni2017), so the generalisation has a documented counterexample.'),
 ],
 key_refs=[
   R('meng2025','COL10A1 missense variants give height Z -3.62 +/- 1.95 versus -1.99 +/- 1.28 for truncating variants (P=0.013) in 128 cases.'),
   R('yang2025','COL10A1 p.W651fsX666 impairs trimerisation of normal collagen X, demonstrating a dominant-negative effect on the wild-type allele.'),
   R('ni2026','80.8% of COMP variants are missense and 87.7% of probands carry one in the type-3 repeat domain, the domain whose misfolding drives ER retention.'),
   R('gkourogianni2017','No genotype-phenotype correlation between ACAN mutation class and joint involvement across 20 families - the documented counterexample.'),
 ],
))

write(dict(id='genomic_imprinting_growth', name='Genomic imprinting and growth', type='process', layer='L8',
 aliases=['parent-of-origin effects on stature'],
 summary="""A small number of human loci are expressed from only one parental allele, and they are
disproportionately growth-regulating - which is what the parental-conflict hypothesis predicts, and
which gives human genetics a set of natural single-dose experiments no other mechanism supplies.
The two best-characterised clusters both cause reciprocal growth phenotypes. At 11p15.5, loss of
paternal ICR1 methylation reduces IGF2 and causes Silver-Russell syndrome with severe intrauterine
and postnatal growth retardation, while gain of maternal ICR1 methylation causes Beckwith-Wiedemann
overgrowth; disruption of the same region therefore moves growth in opposite directions depending
on which parental allele is affected. At 14q32.2, hypomethylation of the paternal MEG3/DLK1 region
gives Temple syndrome with pre- and postnatal growth failure, while the reciprocal defect gives
Kagami-Ogata syndrome with prenatal overgrowth. Abi Habib 2019 supplied the finding that links the
two clusters mechanistically: 14q32.2 hypomethylation alters expression not only at that locus but
across other imprinted genes, and specifically lowers IGF2 at 11p15.5, producing a shared
transcriptional signature that explains the long-noted clinical overlap between Temple and
Silver-Russell syndromes. Imprinted growth regulation is therefore not a set of independent loci
but a network with IGF2 as a convergence point - a claim made from patient-derived expression
profiling rather than from mouse.""",
 quantitative=[
   q('Silver-Russell patients with paternal ICR1 loss of methylation','60','%','11p15.5 imprinting disorder cohorts','human','abi2019','approximate; the commonest single molecular cause'),
   q('postnatal short stature in genetically confirmed Temple syndrome','87.0','%','60 Japanese patients with UPD(14)mat, epimutation or deletion','human','ogawa2025','not applicable (proportion)'),
   q('central precocious puberty in Temple syndrome','86.0','%','same cohort','human','ogawa2025','not applicable (proportion)'),
 ],
 localization=['human: 11p15.5 (IGF2/H19, CDKN1C/KCNQ1OT1) and 14q32.2 (DLK1/MEG3) imprinted clusters'],
 human_evidence='direct',
 human_evidence_note='Human patient cohorts with molecularly defined methylation defects and patient-derived expression profiling.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human imprinting disorders; mouse distal chromosome 7 models are not used to support these claims because parental-transmission phenotypes are known to differ between the species.',
 confidence='B',
 claim_grades=[
   dict(claim='Reciprocal methylation defects at imprinted growth loci produce reciprocal growth phenotypes.',grade='A',basis='Two independent clusters (11p15.5 SRS/BWS, 14q32.2 Temple/Kagami-Ogata) each with reciprocal patient groups and molecular confirmation.'),
   dict(claim='14q32.2 hypomethylation acts partly by lowering IGF2 at 11p15.5, explaining Temple/Silver-Russell overlap.',grade='D',basis='Single transcriptional profiling study (abi2019); not independently replicated.'),
 ],
 key_refs=[
   R('abi2019','14q32.2 hypomethylation deregulates other imprinted genes and lowers IGF2 at 11p15.5, giving Temple and Silver-Russell syndromes a shared transcriptional signature.'),
   R('ogawa2025','60 genetically confirmed Temple syndrome patients: postnatal short stature in 87.0% and central precocious puberty in 86.0%.'),
 ],
))

write(dict(id='igf2_h19_imprinting', name='IGF2/H19 imprinted locus', type='gene', layer='L8',
 aliases=['11p15.5 ICR1','IGF2/H19 imprinting control region'],
 summary="""The IGF2/H19 domain at 11p15.5 is controlled by imprinting control region 1, which is methylated on
the paternal allele and unmethylated on the maternal one, and its disruption produces the two
reciprocal human growth syndromes that bracket normal stature. Paternal ICR1 loss of methylation
silences IGF2 and accounts for roughly 60% of Silver-Russell syndrome, characterised by severe
intrauterine and postnatal growth retardation. Maternal ICR1 hypermethylation activates IGF2 on
both alleles and causes about 10% of Beckwith-Wiedemann syndrome, characterised by overgrowth. The
lesions are structurally reciprocal at the same 1.5 kb element, so the locus behaves as a
continuous human IGF2 dose rheostat rather than a binary disease gene. Two mechanistic details are
established in patient material rather than inferred. First, microdeletions of the CTCF-binding
repeats within ICR1 and point mutations in an OCT-binding motif can each cause the hypermethylated
BWS state in a maternally inherited, familial pattern, which localises the control to specific
transcription-factor footprints. Second, Abi Habib 2019 showed that IGF2 at this locus is
downregulated by hypomethylation at an entirely different imprinted domain on chromosome 14,
placing IGF2 downstream of a wider imprinting network. Because IGF2 acts principally on prenatal
growth, the postnatal stature deficit in Silver-Russell is not fully explained by IGF2 dose alone.""",
 quantitative=[
   q('Silver-Russell syndrome cases with paternal ICR1 loss of methylation','60','%','11p15.5 molecular diagnostic series','human','abi2019','approximate as reported'),
   q('Beckwith-Wiedemann syndrome cases with maternal ICR1 hypermethylation','10','%','11p15.5 molecular diagnostic series','human','abi2019','approximate as reported'),
 ],
 localization=['human: 11p15.5; IGF2 expressed from the paternal allele, H19 from the maternal allele'],
 human_evidence='direct',
 human_evidence_note='Human imprinting disorder cohorts with allele-specific methylation analysis and patient-derived expression profiling.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human imprinting; the mouse distal-7 orthologue shows contradictory parental-transmission phenotypes for some models and is deliberately not invoked.',
 confidence='B',
 claim_grades=[
   dict(claim='Reciprocal ICR1 methylation defects cause reciprocal growth phenotypes through IGF2 dosage.',grade='A',basis='Two large reciprocal patient groups (SRS and BWS) with allele-specific methylation and IGF2 expression data; established across many independent diagnostic series.'),
   dict(claim='IGF2 dosage at this locus is regulated in trans by imprinting status at 14q32.2.',grade='D',basis='Single expression-profiling study (abi2019).'),
 ],
 key_refs=[
   R('abi2019','14q32.2 hypomethylation lowers IGF2 expression at the 11p15.5 domain, and paternal ICR1 loss of methylation accounts for ~60% of Silver-Russell syndrome.'),
   R('ogawa2025','Temple syndrome (the 14q32.2 counterpart) causes postnatal short stature in 87.0% of 60 genetically confirmed patients.'),
 ],
))

write(dict(id='uniparental_disomy_growth', name='Uniparental disomy and growth', type='phenotype', layer='L8',
 aliases=['UPD and stature','maternal UPD14'],
 summary="""Uniparental disomy - inheriting both copies of a chromosome or chromosome segment from one parent -
is the cleanest available human test of parent-of-origin dosage, because the total gene dose is
normal and only the parental provenance changes. Maternal UPD of chromosome 14 causes Temple
syndrome. Ogawa 2025 reported 60 genetically confirmed Japanese patients, of whom 31 had UPD(14)mat,
22 an epimutation, 5 a deletion and 2 either UPD(14)mat or an epimutation: small for gestational
age in 88.3%, postnatal short stature by around age 2 in 87.0%, and central precocious puberty in
86.0%. The growth phenotype is therefore double: a prenatal and early postnatal deficit followed by
a shortened growth window from precocious puberty, which is why untreated adult stature is worse
than the childhood deficit alone predicts. Growth hormone in 32 patients raised median height SDS
from -3.4 to -2.4 and GnRH analogue therapy in 32 ameliorated the precocious puberty. The
comparison group is instructive: the reciprocal paternal defect at the same locus gives
Kagami-Ogata syndrome with prenatal overgrowth. Uniparental isodisomy carries a second consequence
that is not about imprinting at all - it makes any recessive founder variant on the duplicated
chromosome homozygous, producing blended phenotypes that can be misread as atypical presentations
of the imprinting disorder.""",
 quantitative=[
   q('small for gestational age in Temple syndrome','88.3','%','60 genetically confirmed patients (31 UPD(14)mat, 22 epimutation, 5 deletion, 2 undetermined)','human','ogawa2025','not applicable (proportion)'),
   q('postnatal short stature (by about 2 years)','87.0','%','same cohort','human','ogawa2025','not applicable (proportion)'),
   q('central precocious puberty','86.0','%','same cohort','human','ogawa2025','not applicable (proportion)'),
   q('median height SDS before growth hormone','-3.4','SDS','32 of 60 patients treated','human','ogawa2025','median; no control arm'),
   q('median height SDS after growth hormone','-2.4','SDS','same 32 patients','human','ogawa2025','median; no control arm'),
 ],
 localization=['human: chromosome 14q32.2 (Temple/Kagami-Ogata) and 11p15.5 (Silver-Russell/Beckwith-Wiedemann)'],
 human_evidence='direct',
 human_evidence_note='60 molecularly confirmed human patients with measured stature, pubertal timing and treatment response.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human parent-of-origin phenotypes.',
 confidence='B',
 claim_grades=[
   dict(claim='Maternal UPD14 causes pre- and postnatal growth failure plus central precocious puberty in the great majority of patients.',grade='A',basis='60 genetically confirmed patients with three distinct molecular mechanisms giving concordant phenotypes (ogawa2025).'),
   dict(claim='Growth hormone improves height SDS in Temple syndrome by about 1.0 SDS.',grade='D',basis='Single uncontrolled treated subgroup of 32 patients (ogawa2025); no randomised comparison exists.'),
 ],
 key_refs=[
   R('ogawa2025','60 Temple syndrome patients: SGA 88.3%, postnatal short stature 87.0%, central precocious puberty 86.0%; GH raised median height SDS from -3.4 to -2.4.'),
   R('abi2019','14q32.2 hypomethylation lowers IGF2 at 11p15.5, giving Temple and Silver-Russell syndromes a shared transcriptional signature.'),
 ],
))

write(dict(id='de_novo_variant_growth', name='De novo variation and growth', type='process', layer='L8',
 aliases=['paternal age effect','selfish spermatogonial selection'],
 summary="""Several of the largest-effect growth-plate mutations in humans are not inherited but arise de novo
in the paternal germline, and they are enriched far above the background mutation rate by positive
selection acting on spermatogonial stem cells. Neville 2025 sequenced 81 bulk sperm samples from
men aged 24-75 with duplex NanoSeq and measured a linear accumulation of 1.67 mutations per year
per haploid genome (95% CI 1.41-1.92), identified more than 35,000 germline coding mutations, and
found 40 genes under significant positive selection in the male germline, most of them associated
with developmental or cancer-predisposition disorders; selection drives a 2-3 fold increased risk
of known disease-causing mutations, so 3-5% of sperm from middle-aged and older men carry a
pathogenic exome mutation. FGFR3, the achondroplasia gene, is the archetype. Moura 2024 assayed 10
FGFR3 missense substitutions by digital PCR across a dissected postmortem human testis and showed
that 9 raise ligand-independent receptor signalling, with two distinct expansion behaviours: some
variants form larger subclonal expansions whose frequency correlates positively with donor age,
while others show elevated frequency independent of age, consistent with accumulation before sexual
maturity. That is the mechanistic explanation for why achondroplasia is overwhelmingly de novo,
paternal in origin, and associated with advanced paternal age - the mutation is not merely
tolerated in the germline, it is selected for.""",
 quantitative=[
   q('germline mutation accumulation rate in sperm','1.67','mutations per year per haploid genome','81 bulk sperm samples, men aged 24-75, duplex NanoSeq','human','neville2025','95% CI 1.41-1.92'),
   q('genes under significant positive selection in the male germline','40','genes','31 newly identified; deep targeted and exome NanoSeq','human','neville2025','not applicable (count)'),
   q('increase in risk of known disease-causing mutations from germline positive selection','2-3','fold','same analysis','human','neville2025','range as reported'),
   q('sperm carrying a pathogenic exome mutation, middle-aged to older men','3-5','%','same analysis','human','neville2025','range as reported'),
   q('FGFR3 missense substitutions raising ligand-independent signalling','9','of 10 tested','digital PCR plus biophysical assay on a dissected postmortem testis','human','moura2024','not applicable (count)'),
 ],
 localization=['human: male germline, spermatogonial stem cell compartment'],
 human_evidence='direct',
 human_evidence_note='Direct sequencing and locus-specific quantification in human sperm and dissected human testis.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human germline measurements throughout.',
 confidence='B',
 claim_grades=[
   dict(claim='Positive selection in the male germline enriches pathogenic de novo mutations above the neutral rate.',grade='A',basis='Genome-wide duplex sequencing of 81 sperm samples identifying 40 positively selected genes (neville2025) plus locus-resolved subclonal expansion mapping in testis for FGFR3 (moura2024).'),
   dict(claim='This mechanism explains the paternal-age association of achondroplasia specifically.',grade='B',basis='Age-correlated FGFR3 subclonal expansions measured directly in human testis (moura2024); the epidemiological link to achondroplasia incidence is inferred rather than jointly measured in the same study.'),
 ],
 key_refs=[
   R('neville2025','Duplex sperm sequencing of 81 men: 1.67 mutations/year/haploid genome and 40 positively selected genes, driving 2-3 fold enrichment of disease-causing mutations.'),
   R('moura2024','Nine of ten FGFR3 missense substitutions raise ligand-independent signalling; several form age-correlated subclonal expansions in human testis.'),
   R('shiang1994','Achondroplasia arises from recurrent FGFR3 Gly380 substitutions, predominantly de novo.'),
 ],
))

write(dict(id='dna_methylation_growth_plate', name='DNA methylation in the growth plate', type='process', layer='L8',
 aliases=['chondrocyte methylome','growth plate epigenome'],
 summary="""DNA methylation in developing human cartilage has now been mapped directly, which converts a
previously animal-only claim into a human one. McDonnell 2024 quantified methylation at
approximately 700,000 CpGs in developing human chondrocytes from 72 samples spanning 7 to 21
post-conception weeks, found significant change at 3% of all CpGs, and defined more than 8,200
developmental differentially methylated regions. Integrating with genetic data identified 24 loci
where osteoarthritis risk variants colocalise with methylation quantitative trait loci, and
comparison with mature chondrocyte datasets separated effects exerted only during development from
those operating throughout the life course. The developmental-only class is the important one for
this atlas: it means a regulatory variant can act on cartilage before birth and leave a permanent
skeletal consequence with no detectable effect in adult tissue, which is a specific mechanism by
which height-associated non-coding variants could be invisible to any adult-tissue eQTL catalogue.
The complementary claim from animal work - Nilsson 2005 showed growth plate senescence in rabbit is
accompanied by loss of DNA methylation - remains species-restricted and is not asserted here as
human fact. The gap between the two is that no human dataset yet spans postnatal growth plate
through fusion, so the human methylome is characterised in fetal cartilage and in adult articular
cartilage but not across the growing physis itself.""",
 quantitative=[
   q('CpGs assayed in developing human chondrocytes','700000','CpG sites','72 samples, 7-21 post-conception weeks','human','mcdonnell2024','approximate as reported'),
   q('CpGs showing significant developmental change','3','%','same dataset','human','mcdonnell2024','not applicable (proportion)'),
   q('developmental differentially methylated regions','8200','DMRs','same dataset','human','mcdonnell2024','more than; lower bound as reported'),
   q('loci where osteoarthritis risk variants colocalise with methylation QTLs','24','loci','same dataset','human','mcdonnell2024','not applicable (count)'),
 ],
 localization=['human: developing chondrocytes 7-21 post-conception weeks; postnatal growth plate not covered'],
 human_evidence='direct',
 human_evidence_note='Epigenome-wide methylation measured in 72 human developing cartilage samples with colocalisation against human genetic association data.',
 species_basis=['human'],
 translation_risk='low',
 translation_risk_reason='The methylome claim is measured in human tissue. The senescence-associated demethylation claim is rabbit-only and is explicitly not extended to humans here.',
 confidence='B',
 claim_grades=[
   dict(claim='DNA methylation changes substantially across human cartilage development and colocalises with skeletal disease risk variants.',grade='A',basis='72-sample human developmental methylome with 8,200 DMRs and 24 mQTL-GWAS colocalisations (mcdonnell2024).'),
   dict(claim='Growth plate senescence is accompanied by loss of DNA methylation in humans.',grade='C',basis='Demonstrated in rabbit (nilsson2005); no human postnatal growth plate methylome exists. Recorded as a species gap, not as human fact. See gap g_l8gen_013.'),
 ],
 key_refs=[
   R('mcdonnell2024','700,000-CpG methylome of 72 human developing chondrocyte samples (7-21 PCW): 3% of CpGs change, >8,200 developmental DMRs, 24 OA loci colocalise with mQTLs.'),
   R('nilsson2005','Growth plate senescence in rabbit is associated with loss of DNA methylation - animal evidence only.'),
   R('richard2025','Human skeletal developmental functional genomics intersecting chondrocyte regulatory maps with height heritability.'),
 ],
 open_questions=['g_l8gen_013'],
))

write(dict(id='epigenetic_clock_growth', name='Epigenetic clocks and growth', type='method', layer='L8',
 aliases=['DNA methylation age in children','PedBE clock'],
 summary="""Epigenetic clocks estimate biological age from DNA methylation and are accurate enough in children
to be a candidate maturational readout, but they have not been validated against skeletal
maturation, which is what this atlas would need them for. McEwen 2020 built the Pediatric-Buccal-
Epigenetic clock from 1,721 genome-wide methylation profiles across 11 cohorts of typically
developing individuals aged 0-20, selecting 94 CpG sites by elastic-net regression in a
1,032-sample training set and achieving a median absolute error of 0.35 years in a separate
689-sample test set. That is finer resolution than bone age scoring, non-invasive, and continuous.
What is missing is any published correspondence between epigenetic age acceleration and bone age,
peak height velocity, or the timing of epiphyseal fusion. The clock literature in children has
instead been applied to prenatal adversity, prematurity and neurodevelopment: placental epigenetic
gestational-age acceleration, for instance, associates with slower postnatal weight and fat-mass
gain but explicitly shows no association with height or lean-mass gain. Until an epigenetic-age-
versus-bone-age study exists, an epigenetic clock is a validated chronological-age estimator in
children and nothing more for growth-plate purposes - which is exactly how it is graded here.""",
 quantitative=[
   q('CpG sites in the PedBE clock','94','CpG sites','elastic-net selection from 1,032 buccal training samples','human','mcewen2020','not applicable (count)'),
   q('median absolute error of PedBE age prediction','0.35','years','689-sample independent test set, ages 0-20','human','mcewen2020','median absolute error'),
   q('total methylation profiles assembled','1721','profiles','11 cohorts of typically developing individuals aged 0-20','human','mcewen2020','not applicable (count)'),
 ],
 localization=['human: buccal epithelium and blood; no cartilage or growth plate clock exists'],
 human_evidence='direct',
 human_evidence_note='Human paediatric cohorts with measured chronological age; no skeletal maturation endpoint has been tested.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human method development.',
 confidence='B',
 claim_grades=[
   dict(claim='DNA methylation predicts chronological age in children to within about 0.4 years.',grade='A',basis='Training and independent test sets totalling 1,721 profiles across 11 cohorts (mcewen2020).'),
   dict(claim='Epigenetic age acceleration indexes skeletal maturation or predicts growth cessation.',grade='X',basis='Widely assumed in reviews but no primary study relating an epigenetic clock to bone age, peak height velocity or epiphyseal fusion was located. See gap g_l8gen_014.'),
 ],
 key_refs=[
   R('mcewen2020','The PedBE clock predicts chronological age from 94 buccal CpGs with median absolute error 0.35 years in children aged 0-20.'),
   R('mcdonnell2024','Human developmental cartilage methylome, the substrate a cartilage-specific clock would have to be built on.'),
 ],
 open_questions=['g_l8gen_014'],
))
