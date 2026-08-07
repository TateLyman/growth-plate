from w import *

write(dict(id='fgfr3_gene', name='FGFR3', type='gene', layer='L8',
 aliases=['fibroblast growth factor receptor 3 gene'],
 summary="""FGFR3 is the clearest bidirectional dose experiment in human skeletal genetics because activating
and inactivating alleles of the same receptor move stature in opposite directions, and because the
activating series is graded rather than binary. Shiang 1994 and Rousseau 1994 independently showed
that achondroplasia is caused by heterozygous transmembrane-domain substitutions at Gly380, found
on essentially all achondroplasia chromosomes; Tavormina 1995 showed that thanatophoric dysplasia
types I and II arise from distinct, more strongly activating FGFR3 domains; Bellus 1995 showed
hypochondroplasia arises from the weaker tyrosine-kinase-domain N540K. FGFR3 is thus a negative
regulator of bone growth in which the degree of constitutive activation predicts the degree of
shortening across four clinically distinct disorders. The loss-of-function arm was found last:
Toydemir 2006 mapped CATSHL syndrome - camptodactyly, tall stature, scoliosis, hearing loss - to
FGFR3 p.R621H, a partial loss of kinase function that recapitulates the Fgfr3-knockout mouse
phenotype and therefore establishes in humans that reducing FGFR3 signalling lengthens bone. A
second, independent CATSHL family with p.R621C at the same residue has since been reported.
Separately, FGFR3 is a paternal-age-effect gene: Moura 2024 measured 10 FGFR3 missense
substitutions in postmortem human testis by digital PCR and found 9 raised ligand-independent
signalling, several forming age-correlated subclonal expansions - the germline selection mechanism
that makes achondroplasia predominantly a de novo, paternally derived mutation.""",
 quantitative=[
   q('achondroplasia chromosomes carrying a Gly380 transmembrane substitution','16','of 16','FGFR3 c.1138G>A or G>C','human','shiang1994','not applicable (count)'),
   q('FGFR3 missense substitutions raising ligand-independent signalling in human testis','9','of 10 tested','digital PCR plus biophysical signalling assay on dissected postmortem testis','human','moura2024','not applicable (count)'),
   q('FGFR3 variants found in idiopathic short stature panel screening','2','of 102 patients','targeted multigene panel','human','andrade2022','not applicable (count)'),
 ],
 localization=['human: germline; receptor acts in proliferative and prehypertrophic growth plate chondrocytes'],
 human_evidence='direct',
 human_evidence_note='Gain- and loss-of-function alleles both defined in humans with measured stature and independently replicated across four disorders.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='All allele-to-stature claims are human; the mouse Fgfr3 knockout is cited only as concordant background for the CATSHL direction.',
 confidence='A',
 key_refs=[
   R('shiang1994','Achondroplasia is caused by heterozygous FGFR3 transmembrane Gly380 substitutions present on all 16 achondroplasia chromosomes examined.'),
   R('rousseau1994','Independent identification of FGFR3 mutations as the cause of achondroplasia.'),
   R('tavormina1995','Thanatophoric dysplasia types I and II are caused by distinct FGFR3 mutations more strongly activating than the achondroplasia allele.'),
   R('bellus1995','Hypochondroplasia is caused by the weaker tyrosine-kinase-domain FGFR3 N540K substitution.'),
   R('toydemir2006','FGFR3 p.R621H causes partial loss of function and CATSHL syndrome with tall stature, establishing that reduced FGFR3 signalling lengthens human bone.'),
   R('moura2024','Nine of ten FGFR3 missense substitutions assayed in human testis raise ligand-independent signalling; several form age-correlated subclonal germline expansions.'),
 ],
))

write(dict(id='ihh_gene', name='IHH', type='gene', layer='L8',
 aliases=['Indian hedgehog gene'],
 summary="""IHH gives a three-level human dose series with an unusually informative middle. Gao 2001 showed
that heterozygous missense mutations in the amino-terminal signalling domain cause brachydactyly
type A-1, shortening or loss of the middle phalanges, with three mutations in three large families
all altering residues predicted to lie adjacent on the IHH surface - a gain-of-abnormal-function or
altered-ligand-range mechanism rather than simple dosage reduction. Hellemans 2003 showed that
homozygous IHH mutations cause acrocapitofemoral dysplasia, an autosomal recessive disorder with
cone-shaped epiphyses in hands and hips - biallelic loss gives a generalised, not digit-restricted,
epiphyseal disorder. Sentchordi-Montane 2020 then characterised 16 probands with heterozygous IHH
variants including the first complete IHH deletion and found that none showed classical
brachydactyly A-1; the commonest presentation was mild-to-moderate short stature with shortening of
the fifth-finger middle phalanx, and two short probands had no radiological hand anomaly at all
while five carriers of normal height did. Heterozygous IHH loss is therefore a
variably-penetrant short-stature allele rather than a brachydactyly allele, and the BDA-1 missense
class must be mechanistically distinct from haploinsufficiency. In unselected idiopathic short
stature IHH is the commonest single finding on growth-plate gene panels: 4 of 102 in Andrade 2022,
ahead of SHOX.""",
 quantitative=[
   q('heterozygous IHH probands characterised','16','probands','targeted NGS or Sanger in short stature and/or brachydactyly; 15 distinct variants including the first complete IHH deletion','human','sentchordimont2020','not applicable (count)'),
   q('IHH heterozygotes with classical brachydactyly type A-1','0','of 16 probands','same cohort','human','sentchordimont2020','not applicable (count)'),
   q('IHH heterozygotes of normal height but with brachydactyly','5','of 16 probands','same cohort','human','sentchordimont2020','not applicable (count)'),
   q('IHH variant yield in idiopathic short stature','4','of 102 patients','targeted multigene panel; commonest single gene in this cohort','human','andrade2022','not applicable (count)'),
 ],
 localization=['human: germline; ligand produced by prehypertrophic chondrocytes'],
 human_evidence='direct',
 human_evidence_note='Heterozygous, homozygous and null alleles all characterised in humans with measured stature and hand radiology.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human allelic series only; the extensive murine Ihh literature is held in ihh_protein.',
 confidence='A',
 claim_grades=[
   dict(claim='Heterozygous IHH loss of function causes mild-to-moderate short stature with incomplete penetrance.', grade='A', basis='16-proband cosegregating series (sentchordimont2020) plus independent panel yield in an unselected ISS cohort (andrade2022).'),
   dict(claim='BDA-1 missense alleles act by a mechanism other than reduced IHH dosage.', grade='B', basis='Inferred from the phenotypic non-overlap between gao2001 missense families and haploinsufficient carriers; not directly tested by an allele-matched functional comparison.'),
 ],
 key_refs=[
   R('gao2001','Three heterozygous missense mutations in the IHH N-terminal signalling domain cause brachydactyly type A-1 in three large families.'),
   R('hellemans2003','Homozygous IHH mutations cause acrocapitofemoral dysplasia with cone-shaped epiphyses of hands and hips.'),
   R('sentchordimont2020','16 heterozygous IHH probands show mild-moderate short stature and fifth-finger changes but no classical brachydactyly A-1; five carriers of normal height.'),
   R('andrade2022','IHH is the commonest gene found (4/102) on a growth-plate panel in children classified as idiopathic short stature.'),
 ],
))

write(dict(id='pth1r_gene', name='PTH1R', type='gene', layer='L8',
 aliases=['PTH/PTHrP receptor gene','PTHR1'],
 summary="""PTH1R is a bidirectional human dose experiment on the PTHrP-IHH feedback loop that sets the pace of
chondrocyte hypertrophy. Schipani 1995 identified a heterozygous His223Arg substitution in the
first intracellular loop in Jansen-type metaphyseal chondrodysplasia and showed it produces
constitutive, ligand-independent cAMP accumulation in COS-7 cells - a gain-of-function receptor
that delays hypertrophic differentiation and gives short-limbed dwarfism with ligand-independent
hypercalcaemia and hypophosphataemia. Jobert 1998 supplied the opposite pole: in Blomstrand
chondrodysplasia the patient was heterozygous for a maternally inherited point mutation creating a
novel splice site that deletes 11 amino acids of the fifth transmembrane domain; the mutant
receptor was well expressed but bound neither PTH nor PTHrP and produced no cAMP or inositol
phosphate response, and critically the paternal allele was not expressed, so the chondrocytes had
functionally zero receptor. Blomstrand chondrodysplasia is lethal with advanced endochondral bone
maturation. The two disorders therefore bracket the receptor: constitutive activation delays
hypertrophy and shortens limbs; total absence accelerates ossification and is lethal. Because the
Blomstrand case achieved nullizygosity through allele-specific silencing rather than biallelic
mutation, the human evidence for the null state is a single carefully dissected patient, and that
is the weak link on this node.""",
 quantitative=[
   q('constitutive ligand-independent cAMP accumulation, PTH1R H223R','present','qualitative','COS-7 cells transfected with mutant vs wild-type receptor; absent in wild type','in_vitro_human_cell','schipani1995','magnitude not reported in abstract'),
   q('PTH and PTHrP binding, Blomstrand PTH1R mutant','absent','qualitative','COS-7 expression of the exon-M5-deleted receptor; no cAMP or inositol phosphate response','in_vitro_human_cell','jobert1998','no quantitative binding constant reported'),
 ],
 localization=['human: germline; receptor acts on proliferative/prehypertrophic chondrocytes and on kidney and bone'],
 human_evidence='direct',
 human_evidence_note='Gain- and loss-of-function human patients with matched in vitro receptor assays.',
 species_basis=['human','in_vitro_human_cell'],
 translation_risk='not_applicable',
 translation_risk_reason='Human mutations with human-cell functional assays; no rodent inference.',
 confidence='B',
 claim_grades=[
   dict(claim='Constitutive PTH1R activation causes Jansen metaphyseal chondrodysplasia with short limbs and hypercalcaemia.', grade='A', basis='Human mutation plus matched in vitro constitutive-activity assay (schipani1995), phenotype replicated in later Jansen kindreds.'),
   dict(claim='Complete absence of functional PTH1R accelerates endochondral maturation and is lethal.', grade='D', basis='Single patient (jobert1998); the null state arose from allele-specific non-expression rather than biallelic mutation and has not been replicated by that route.'),
 ],
 key_refs=[
   R('schipani1995','A heterozygous PTH1R His223Arg substitution causes constitutive ligand-independent cAMP accumulation and Jansen-type metaphyseal chondrodysplasia.'),
   R('jobert1998','In Blomstrand chondrodysplasia a splice-altering PTH1R mutation gives a receptor that binds neither PTH nor PTHrP, with the paternal allele unexpressed.'),
 ],
 open_questions=['g_l8gen_003'],
))

write(dict(id='col2a1_gene', name='COL2A1', type='gene', layer='L8',
 aliases=['type II collagen alpha-1 gene'],
 summary="""COL2A1 encodes the alpha-1 chain of type II collagen, the principal fibrillar collagen of growth
plate and articular cartilage, and its human allelic series is the textbook case of
dominant-negative dosage rather than haploinsufficiency. The recurrent pathogenic class is glycine
substitution within the Gly-X-Y repeat of the triple-helical domain: Zhan 2025 found six such
substitutions (Gly1110Ser, Gly1107Glu, Gly873Arg, Gly456Ala, Gly1062Ser, Gly1182Arg) plus one
intronic variant across seven unrelated Chinese SEDC families, all presenting with disproportionate
short stature and skeletal abnormality. Because collagen II is a homotrimer, a single mutant chain
poisons the assembly of trimers containing any wild-type chains, which is why heterozygous missense
alleles give a phenotype far more severe than the expected 50% reduction and why true whole-gene
deletions instead give the mild Stickler spectrum. The severity gradient across type II
collagenopathies - achondrogenesis type II (lethal), SEDC, Kniest, Stickler - tracks the position
and steric bulk of the substituting residue rather than the amount of protein made. ClinGen's
skeletal disorders expert panel classifies COL2A1 as definitively associated with at least one
skeletal disorder among the 26 gene-disease relationships it curated. The quantitative weakness of
this node is that no published series gives a mean adult height SDS by mutation class for COL2A1
the way Meng 2025 does for COL10A1; the reported growth data are single-arm GH-treatment responses
(+0.76 and +0.27 height SDS over 3.5 and 3 years in two SEDC children).""",
 quantitative=[
   q('COL2A1 glycine-substitution missense variants in consecutive SEDC families','6','of 7 families','whole-exome/targeted sequencing, unrelated Chinese families; seventh was an intronic variant','human','zhan2025','not applicable (count)'),
   q('height SDS gain on growth hormone, SEDC','0.76','SDS','one patient, 3.5 years of GH','human','zhan2025','n=1; no control arm'),
   q('height SDS gain on growth hormone, SEDC','0.27','SDS','second patient, 3 years of GH','human','zhan2025','n=1; no control arm'),
   q('COL2A1 variant yield in idiopathic short stature','1','of 102 patients','targeted multigene panel','human','andrade2022','not applicable (count)'),
 ],
 localization=['human: germline; product is the dominant fibrillar collagen of growth plate and articular cartilage'],
 human_evidence='direct',
 human_evidence_note='Human genotype-phenotype series with cosegregation; no animal data are used for any claim on this node.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Purely human allelic data.',
 confidence='B',
 claim_grades=[
   dict(claim='Heterozygous glycine substitutions in the COL2A1 triple-helical domain cause spondyloepiphyseal dysplasia congenita.', grade='A', basis='Seven unrelated families (zhan2025) plus ClinGen definitive gene-disease classification (webb2026); a very large independent literature exists.'),
   dict(claim='The mechanism is dominant-negative incorporation into the collagen II homotrimer rather than haploinsufficiency.', grade='C', basis='Consistent with the severity gradient and with the mild phenotype of whole-gene deletions, but no allele-matched human trimer-assembly experiment was reached in this sweep. See gap g_l8gen_005.'),
 ],
 key_refs=[
   R('zhan2025','Six COL2A1 glycine substitutions plus one intronic variant across seven unrelated SEDC families; GH gave +0.76 and +0.27 height SDS in two patients.'),
   R('webb2026','ClinGen skeletal disorders expert panel classifies COL2A1 as definitively associated with skeletal disease across curated gene-disease relationships.'),
   R('andrade2022','COL2A1 variant found in 1 of 102 children classified as idiopathic short stature.'),
 ],
 open_questions=['g_l8gen_005'],
))

write(dict(id='col10a1_gene', name='COL10A1', type='gene', layer='L8',
 aliases=['type X collagen alpha-1 gene'],
 summary="""COL10A1 encodes the short-chain collagen made exclusively by hypertrophic chondrocytes, and it is
the one human locus in this atlas where dominant-negative and haploinsufficiency alleles of the
same gene have been compared quantitatively in the same cohort. Warman 1993 mapped autosomal
dominant Schmid metaphyseal chondrodysplasia to a 13 bp COL10A1 deletion segregating in a large
kindred (lod 18.2 at theta=0), producing a frameshift that shortens the alpha-1(X) chain by nine
residues in the conserved C-terminal NC1 domain. Meng 2025 assembled 4 new cases plus 124 published
ones and found the discriminating result: patients carrying missense variants had height Z
-3.62 +/- 1.95 versus -1.99 +/- 1.28 for truncating variants (P = 0.013), and had more metaphyseal
irregularity of the distal radius and ulna (P = 0.019). Because truncating COL10A1 alleles are
degraded by nonsense-mediated decay - leaving the wild-type allele to make half the normal amount
of collagen X - while missense alleles produce a stable chain that disrupts trimerisation of the
wild-type product, this is a direct human measurement that dominant-negative interference costs
about 1.6 SDS more stature than losing one copy outright. NC1-domain variants also present earlier
than non-NC1 variants (median 12 versus 72 months, P = 0.0014). The mechanistic reading is
corroborated in vitro: Xu 2025 showed a frameshift allele disrupts trimerisation of normal collagen
X, exerting a dominant-negative effect on the wild-type chain.""",
 quantitative=[
   q('height Z-score, COL10A1 missense (dominant-negative) variants','-3.62','SDS','metaphyseal chondrodysplasia Schmid, at first presentation; 4 new plus 124 published cases','human','meng2025','SD 1.95; P=0.013 vs truncating'),
   q('height Z-score, COL10A1 truncating (haploinsufficiency) variants','-1.99','SDS','same cohort','human','meng2025','SD 1.28'),
   q('age at onset, NC1-domain variants','12','months','median, same cohort','human','meng2025','P=0.0014 versus non-NC1'),
   q('age at onset, non-NC1-domain variants','72','months','median, same cohort','human','meng2025','P=0.0014'),
 ],
 localization=['human: germline; product restricted to hypertrophic zone chondrocytes'],
 human_evidence='direct',
 human_evidence_note='Height Z-scores measured in 128 human COL10A1 cases and stratified by mutation class.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='The Col10a1-null mouse has a mild or absent phenotype and is deliberately not used to support any claim here.',
 confidence='A',
 claim_grades=[
   dict(claim='COL10A1 mutations cause metaphyseal chondrodysplasia Schmid.', grade='A', basis='Original linkage kindred at lod 18.2 (warman1993) plus a 128-case genotype-phenotype series (meng2025).'),
   dict(claim='Missense (dominant-negative) COL10A1 alleles reduce stature more than truncating (haploinsufficient) alleles.', grade='B', basis='Single pooled cohort of 128 cases with P=0.013 (meng2025); the comparison is within one literature aggregation rather than two independent cohorts.'),
 ],
 key_refs=[
   R('warman1993','A 13 bp COL10A1 deletion segregates with autosomal dominant Schmid metaphyseal chondrodysplasia at lod 18.2, truncating the NC1 domain.'),
   R('meng2025','In 128 COL10A1 cases, missense variants gave height Z -3.62 +/- 1.95 versus -1.99 +/- 1.28 for truncating variants (P=0.013).'),
 ],
))

write(dict(id='comp_gene', name='COMP', type='gene', layer='L8',
 aliases=['cartilage oligomeric matrix protein gene','thrombospondin-5 gene'],
 summary="""COMP mutations cause pseudoachondroplasia and multiple epiphyseal dysplasia type 1, and the human
allelic data show that these are not two diseases but two ends of one continuum produced by
mutations in a single structural domain. Briggs 1995 localised both to chromosome 19p13.1 and found
COMP mutations in three patients within the region encoding a calcium-binding motif, establishing
allelism. Ni 2026 aggregated 830 genetically diagnosed PSACH/EDM1 patients (471 probands, 224
distinct COMP variants) from 106 publications: 80.8% of variants are missense, 87.7% of probands
carry a variant in the type-3 calcium-binding repeat domain, 38.9% in exon 13 alone, and
c.1417_1419del (p.Asp473del) is the single commonest allele. PSACH patients had significantly
earlier onset and significantly shorter stature than EDM1 patients (both P < 0.001). The mechanism
is not dosage: COMP is a pentamer, mutant subunits misfold, accumulate in the chondrocyte rough
endoplasmic reticulum and trigger a stress response, so heterozygous missense alleles are
cytotoxic-dominant while true null alleles are far milder. The consequence for this atlas is that
COMP is a counterexample to the assumption that a matrix gene's stature effect scales with how much
functional protein is left. What is missing is a published mean adult height in centimetres or SDS
for genotype-defined PSACH cohorts; the 830-case aggregation reports stature only as a
between-group comparison.""",
 quantitative=[
   q('genetically diagnosed PSACH/EDM1 patients aggregated','830','patients','471 probands, 224 distinct COMP variants, from 106 publications','human','ni2026','systematic literature aggregation'),
   q('COMP variants that are missense','80.8','%','same aggregation','human','ni2026','not applicable (proportion)'),
   q('probands with a variant in the type-3 repeat domain','87.7','%','413 of 471 probands','human','ni2026','not applicable (proportion)'),
   q('probands with a variant in exon 13','38.9','%','183 of 471 probands','human','ni2026','not applicable (proportion)'),
 ],
 localization=['human: germline; product is a pentameric extracellular matrix glycoprotein of growth plate and articular cartilage'],
 human_evidence='direct',
 human_evidence_note='830 genotyped human patients with clinical stature comparison between PSACH and EDM1.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human genotype-phenotype aggregation only.',
 confidence='B',
 claim_grades=[
   dict(claim='COMP mutations cause both pseudoachondroplasia and multiple epiphyseal dysplasia type 1 as one allelic continuum.', grade='A', basis='Original allelism demonstration (briggs1995) plus 830-case aggregation with domain mapping (ni2026); ClinGen definitive (webb2026).'),
   dict(claim='PSACH is significantly shorter than EDM1 at the same locus.', grade='B', basis='One systematic aggregation of published cases (ni2026, P<0.001); vulnerable to ascertainment because diagnosis labels are partly assigned on stature.'),
 ],
 key_refs=[
   R('briggs1995','PSACH and MED are allelic, both caused by COMP mutations in a calcium-binding motif on chromosome 19p13.1.'),
   R('ni2026','830 PSACH/EDM1 patients: 80.8% missense variants, 87.7% in the type-3 repeat domain; PSACH significantly shorter and earlier-onset than EDM1.'),
   R('webb2026','ClinGen curation places COMP among genes definitively associated with skeletal disorders.'),
 ],
 open_questions=['g_l8gen_006'],
))
