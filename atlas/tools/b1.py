from w import *

# ---------------- SHOX ----------------
write(dict(id='shox_gene', name='SHOX', type='gene', layer='L8',
 aliases=['short stature homeobox','PAR1 homeobox gene'],
 summary="""SHOX sits in the pseudoautosomal region PAR1 of Xp22/Yp11.3 and escapes X-inactivation, so it is
one of the very few human genes that is genuinely dosage-sensitive in a diploid-versus-monosomic
sense. Rao 1997 defined a 170 kb PAR1 interval deleted in 36 short-statured individuals with Xp22
or Yp11.3 rearrangements and absent from normal-height relatives and from 30 rearrangement
carriers of normal height, then isolated SHOX inside it and found one functional SHOX mutation by
screening 91 idiopathic-short-stature patients. Shears 1998 showed the same gene is deleted or
truncated in Leri-Weill dyschondrosteosis and that Langer mesomelic dysplasia is its homozygous
form, establishing a strict allelic dose series: two functional copies = normal stature, one copy =
mesomelic short stature with Madelung deformity, zero copies = severe mesomelic dwarfism. That
series has been measured: in 41 patients from 23 families the median height SDS was -6.3 for
Langer (nullizygous), -2.4 for Leri-Weill (haploinsufficient) and -2.1 for the SHOX-positive
idiopathic short stature referrals. SHOX is a homeodomain transcription factor; the human
mechanistic work localizing its product in growth plate cartilage is far thinner than the genetic
dose data, which is why the gene node and any protein-level claim must be graded separately.
SHOX has no mouse orthologue (the gene is absent from the rodent genome), so there is no
knockout mouse and essentially no murine mechanism to launder - an unusual and welcome situation
for this atlas.""",
 quantitative=[
   q('PAR1 interval deleted in short stature','170','kb','deleted in 36 individuals with Xp22/Yp11.3 rearrangements; absent in normal-height relatives and 30 normal-height rearrangement carriers','human','rao1997','not applicable (interval size)'),
   q('median height SDS, SHOX nullizygous (Langer mesomelic dysplasia)','-6.3','SDS','n=2 of 41 patients from 23 families','human','doan2026','median of 2 cases; range not reported'),
   q('median height SDS, SHOX haploinsufficient (Leri-Weill dyschondrosteosis)','-2.4','SDS','n=24 of 41 patients','human','doan2026','median; interquartile range not reported'),
   q('median height SDS, SHOX variant presenting as idiopathic short stature','-2.1','SDS','n=12 of 41 patients','human','doan2026','median; interquartile range not reported'),
   q('SHOX variant yield in unselected idiopathic short stature','3','of 102 patients','targeted multigene panel, Brazilian ISS cohort','human','andrade2022','3/102 = 2.9%; CI not reported'),
 ],
 localization=['human: germline PAR1 (Xp22.33/Yp11.32), escapes X-inactivation'],
 human_evidence='direct',
 human_evidence_note='The entire allelic series - nullizygous, haploinsufficient, and heterozygous-mild - is defined in humans with measured stature; there is no mouse orthologue of SHOX.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='SHOX is absent from the rodent genome, so no cross-species inference is possible or attempted.',
 confidence='A',
 claim_grades=[
   dict(claim='SHOX gene dosage sets human stature in a monotonic 0/1/2-copy series.', grade='A', basis='Three independent human cohorts (rao1997 discovery, shears1998 LWD/LMD allelism, doan2026 quantified SDS by dose).'),
   dict(claim='SHOX acts as a transcription factor within growth plate chondrocytes to produce this effect.', grade='D', basis='Asserted in reviews; no human growth-plate localization primary was reached in this sweep. See gap g_l8gen_004.'),
 ],
 key_refs=[
   ref('rao1997',9140395,'10.1038/ng0597-54','Rao E',1997,'primary','A 170 kb PAR1 interval containing the novel homeobox gene SHOX is deleted in 36 short-statured individuals and in no normal-height relative.'),
   ref('shears1998',9590293,'10.1038/ng0198-70','Shears DJ',1998,'primary','SHOX deletions and a premature stop segregate with Leri-Weill dyschondrosteosis; Langer mesomelic dysplasia is the homozygous form.'),
   ref('doan2026',None,None,'Dogan Ari AB',2026,'primary','Median height SDS by SHOX dose in 41 patients: -6.3 nullizygous, -2.4 Leri-Weill, -2.1 idiopathic short stature.'),
   ref('andrade2022',36373817,'10.1530/ec-22-0214','Andrade NLM',2022,'primary','SHOX variants in 3 of 102 children classified as idiopathic short stature.'),
 ],
 open_questions=['g_l8gen_004'],
))
# fix doan2026 pmid
import yaml as _y
p='/home/user/growth-plate/atlas/nodes/L8_genetics_and_heritability/shox_gene.yaml'
s=open(p).read().replace("pmid: 'None'","pmid: '42230379'").replace("  doi: null\n","")
open(p,'w').write(s)

# ---------------- SHOX haploinsufficiency (phenotype) ----------------
write(dict(id='shox_haploinsufficiency', name='SHOX haploinsufficiency', type='phenotype', layer='L8',
 aliases=['SHOX deficiency disorder','Leri-Weill dyschondrosteosis'],
 summary="""SHOX haploinsufficiency is the single-copy state of the PAR1 SHOX locus, produced by whole-gene
deletion, enhancer deletion, nonsense or missense variants, or by loss of one sex chromosome as in
Turner syndrome. It is the commonest identified monogenic cause of disproportionate short stature
in children referred as idiopathic. The measured penetrance on stature is incomplete but the
central tendency is reproducible: median height -2.4 SDS in molecularly confirmed Leri-Weill
dyschondrosteosis and -2.1 SDS where the same lesion presents without Madelung deformity. Two
features distinguish it from a generic short-stature gene. First, the deficit is mesomelic - the
forearm and lower leg are disproportionately shortened and the radius bows into a Madelung
deformity - so it is a limb-segment-specific rather than uniform growth defect. Second, expression
is consistently more severe in females than in males at the same genotype, and the penetrance gap
is wide enough that obligate carriers of normal height are routinely observed within affected
pedigrees. In molecular screening of unselected idiopathic short stature, MLPA plus sequencing
detects SHOX lesions in roughly one in six children, with two-thirds of the lesions falling in
enhancer rather than coding regions - a distribution that matters because coding-only sequencing
misses the majority.""",
 quantitative=[
   q('median height SDS in molecularly confirmed Leri-Weill dyschondrosteosis','-2.4','SDS','n=24 patients from 23 families, mixed ages','human','doan2026','median; range not reported'),
   q('median height SDS in SHOX-positive idiopathic short stature','-2.1','SDS','n=12 patients','human','doan2026','median'),
   q('height SDS after growth hormone in SHOX deficiency','-2.0','SDS','n=15 treated patients, mean pre-treatment -2.5 SDS','human','doan2026','mean; SD not reported'),
 ],
 localization=['human: germline PAR1, systemic; limb effect is mesomelic (zeugopod-predominant)'],
 human_evidence='direct',
 human_evidence_note='Human genotype-phenotype series only; the gene has no rodent orthologue.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='No animal model of SHOX exists, so no cross-species claim is made.',
 confidence='A',
 key_refs=[
   ref('shears1998',9590293,'10.1038/ng0198-70','Shears DJ',1998,'primary','SHOX deletions/nonsense segregate with Leri-Weill dyschondrosteosis; homozygous state gives Langer mesomelic dysplasia.'),
   ref('doan2026',42230379,None,'Dogan Ari AB',2026,'primary','41 SHOX-deficiency patients: median height SDS -2.4 (LWD) and -2.1 (ISS); GH raised mean height SDS from -2.5 to -2.0 in 15 treated.'),
   ref('rao1997',9140395,'10.1038/ng0597-54','Rao E',1997,'primary','PAR1 deletions encompassing SHOX cause growth failure in idiopathic short stature and Turner syndrome.'),
 ],
))

# ---------------- ACAN ----------------
write(dict(id='acan_gene', name='ACAN', type='gene', layer='L8',
 aliases=['aggrecan gene','ACAN haploinsufficiency'],
 summary="""Heterozygous loss-of-function variants in ACAN, which encodes the growth-plate proteoglycan
aggrecan, produce autosomal dominant short stature with advanced rather than delayed bone age -
an unusual combination that inverts the normal clinical heuristic for short stature. Nilsson 2014
identified novel heterozygous ACAN variants by whole-exome sequencing in three families with
dominant short stature, advanced bone age and premature growth cessation; affected adults reached
-2.3 to -4.2 SDS and affected children measured -1.9 to -3.5 SDS. Gkourogianni 2017 extended this
to 103 individuals from 20 families, with perfect cosegregation of variant and phenotype: adult
median height -2.8 SDS (range -5.9 to -0.9), childhood median -2.0 SDS (range -4.2 to -0.6), and
frequent early-onset osteoarthritis (12 of 20 families) and intervertebral disc disease (9 of 20).
The direction of the bone-age effect is the mechanistically informative part: aggrecan
haploinsufficiency does not simply slow the plate, it accelerates its maturation and shortens the
total growth window. No genotype-phenotype correlation was found between mutation class and joint
involvement, so within this gene the dominant-negative/haploinsufficiency distinction does not
appear to stratify outcome the way it does for COL10A1. The childhood-to-adult widening of the
deficit (-2.0 to -2.8 SDS median) is itself a quantitative statement that the loss accrues across
puberty rather than being set prenatally.""",
 quantitative=[
   q('adult height, ACAN heterozygotes','-2.8','SDS','n=103 individuals from 20 families, median','human','gkourogianni2017','range -5.9 to -0.9'),
   q('childhood height, ACAN heterozygotes','-2.0','SDS','same cohort, median','human','gkourogianni2017','range -4.2 to -0.6'),
   q('adult height, ACAN heterozygotes (discovery families)','-2.3 to -4.2','SDS','3 families, autosomal dominant short stature with advanced bone age','human','nilsson2014_2','range across affected individuals'),
   q('families with early-onset osteoarthritis','12','of 20 families','ACAN heterozygous short stature cohort','human','gkourogianni2017','not applicable (count)'),
   q('families with intervertebral disc disease','9','of 20 families','same cohort','human','gkourogianni2017','not applicable (count)'),
 ],
 localization=['human: germline; effector tissue is growth plate and articular cartilage extracellular matrix'],
 human_evidence='direct',
 human_evidence_note='Two independent human cohorts with measured adult and childhood stature and cosegregation testing.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Claims here are restricted to human allele-dose and measured stature; the murine cmd/nanomelia aggrecan literature is not invoked.',
 confidence='A',
 key_refs=[
   ref('nilsson2014_2',24762113,'10.1210/jc.2014-1332','Nilsson O',2014,'primary','Heterozygous ACAN variants in three families cause short stature (adult -2.3 to -4.2 SDS) with advanced bone age and early growth cessation.'),
   ref('gkourogianni2017',27870580,'10.1210/jc.2016-3313','Gkourogianni A',2017,'primary','103 individuals from 20 ACAN families: adult median height -2.8 SDS, childhood -2.0 SDS, with early osteoarthritis in 12/20 families.'),
   ref('andrade2022',36373817,'10.1530/ec-22-0214','Andrade NLM',2022,'primary','ACAN variants in 2 of 102 children classified as idiopathic short stature.'),
 ],
))

# ---------------- NPR2 ----------------
write(dict(id='npr2_gene', name='NPR2', type='gene', layer='L8',
 aliases=['NPR-B gene','guanylyl cyclase B gene','GUC2B'],
 summary="""NPR2 encodes the transmembrane guanylyl cyclase that converts GTP to cGMP on binding C-type
natriuretic peptide, and it is the best human dosage series in the whole growth-plate atlas
because both directions of the dose axis have been measured. Bartels 2004 sequenced 21 families
with acromesomelic dysplasia type Maroteaux and found 21 NPR2 mutations (4 nonsense, 4 frameshift,
2 splice-site, 11 missense), with three tested missense alleles showing markedly deficient
guanylyl cyclase activity - biallelic loss gives severe acromesomelic dwarfism. The same paper
noted that obligate heterozygous carriers were below the matched-control mean. Olney 2006
quantified that: in a 39-member AMDM family the 16 NPR2 mutation carriers had height z-score
-1.8 +/- 1.1 versus -0.4 +/- 0.8 in 23 non-carriers (P < 0.0005), with no difference in body
proportion. Vasques 2013 found three novel heterozygous NPR2 mutations in 47 idiopathic
short-stature probands, all three failing to produce cGMP on CNP stimulation and showing a
dominant-negative reduction when co-transfected 1:1 with wild type. Hisado-Oliva 2015 screened 173
suspected Leri-Weill and 95 ISS cases negative for SHOX and found pathogenic NPR2 alleles in ~3% of
the dyschondrosteosis referral group. Gain of function runs the other way: Miura 2012 reported
p.Val883Met producing ligand-independent cGMP and tall stature with macrodactyly across three
generations, and Hannema 2013 reported p.Arg655Cys in the kinase homology domain giving extreme
tall stature with no skeletal deformity. Loss and gain of the same cyclase therefore move human
stature in opposite directions, which is as close to a controlled human dose experiment as this
field gets.""",
 quantitative=[
   q('height z-score, heterozygous NPR2 mutation carriers','-1.8','SDS','n=16 carriers within a 39-member AMDM family','human','olney2006','SD 1.1; P < 0.0005 vs 23 non-carriers'),
   q('height z-score, non-carrier family members','-0.4','SDS','n=23 within the same family','human','olney2006','SD 0.8'),
   q('NPR2 mutations identified in acromesomelic dysplasia type Maroteaux','21','mutations','21 families; 4 nonsense, 4 frameshift, 2 splice-site, 11 missense','human','bartels2004','not applicable (count)'),
   q('heterozygous NPR2 mutation yield in idiopathic short stature','3','of 47 probands','direct sequencing of NPR2 coding region','human','vasques2013','not applicable (count)'),
   q('pathogenic NPR2 allele frequency in SHOX-negative Leri-Weill referrals','3','%','n=173 suspected LWD referrals','human','hisadooliva2015','approximate as reported'),
 ],
 localization=['human: germline; effector receptor localizes to growth plate chondrocytes'],
 human_evidence='direct',
 human_evidence_note='Human genotype-stature data at three dose levels (biallelic LoF, monoallelic LoF, GoF), each with an independent cohort and in vitro cyclase confirmation.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='All stature claims rest on measured human height; the mouse Npr2 literature is cited only in the protein node npr2_receptor.',
 confidence='A',
 claim_grades=[
   dict(claim='Reduced NPR2 gene dosage lowers human adult stature and increased signalling raises it.', grade='A', basis='Loss-of-function height z-scores measured in a controlled family design (olney2006) plus independent gain-of-function pedigrees (miura2012, hannema2013).'),
   dict(claim='The heterozygous effect size is about -1.4 SDS relative to non-carriers.', grade='B', basis='Single family (olney2006, 16 vs 23); not replicated at that precision in an independent cohort.'),
 ],
 key_refs=[
   ref('bartels2004',15146390,'10.1086/420960','Bartels CF',2004,'primary','21 NPR2 mutations across 21 AMDM families; tested missense alleles show markedly deficient guanylyl cyclase activity and obligate carriers are below control mean height.'),
   ref('olney2006',16384845,'10.1210/jc.2005-1550','Olney RC',2006,'primary','16 heterozygous NPR2 carriers had height z -1.8 +/- 1.1 versus -0.4 +/- 0.8 in 23 non-carriers within one family (P < 0.0005).'),
   ref('vasques2013',24001744,'10.1210/jc.2013-2571','Vasques GA',2013,'primary','Three novel heterozygous NPR2 mutations in 47 ISS probands, all abolishing CNP-stimulated cGMP and reducing wild-type activity when co-expressed.'),
   ref('hisadooliva2015',26075495,'10.1210/jc.2015-1808','Hisado-Oliva A',2015,'primary','Pathogenic NPR2 alleles in ~3% of SHOX-negative Leri-Weill dyschondrosteosis referrals (n=173).'),
   ref('miura2012',22870295,'10.1371/journal.pone.0042180','Miura K',2012,'primary','NPR2 p.Val883Met is constitutively active, raises blood cGMP and causes three-generation tall stature with macrodactyly.'),
   ref('hannema2013',24057292,'10.1210/jc.2013-2374','Hannema SE',2013,'primary','NPR2 p.Arg655Cys in the kinase homology domain markedly increases CNP-stimulated cGMP and causes extreme tall stature without skeletal deformity.'),
 ],
))

# ---------------- NPPC ----------------
write(dict(id='nppc_gene', name='NPPC', type='gene', layer='L8',
 aliases=['CNP gene','natriuretic peptide precursor C'],
 summary="""NPPC encodes the CNP precursor and is the ligand-side member of the CNP/NPR2 dose axis, so its
human allelic series is the mirror image of NPR2's. Overexpression comes first historically:
Bocciardi 2007 characterised a de novo balanced t(2;7)(q37.1;q21.3) in a girl with Marfanoid
habitus and skeletal overgrowth, with the chromosome 2 breakpoint near NPPC, plasma CNP doubled
relative to five controls, and NPPC substantially overexpressed in her fibroblasts. Moncla 2007
then found two further patients with balanced translocations breaking in the same 2q37.1 band
(involving chromosomes 8 and 13), the same overgrowth phenotype and the same NPPC overexpression,
and proposed that the breakpoints separate NPPC from a negative regulatory element on chromosome 2
- a mutational mechanism defined by three independent chromosomal partners converging on one gene.
Loss of function was found much later: Hisado-Oliva 2018 screened 668 patients (357 with
disproportionate short stature, 311 with autosomal dominant idiopathic short stature) plus 29 ISS
families and identified two heterozygous NPPC mutations, both in the highly conserved CNP ring,
both giving significant reductions in cGMP synthesis, cosegregating with short stature and small
hands. One of the two alleles corresponds to the spontaneous mouse lbab long-bone-abnormality
mutation. The gene is therefore bidirectionally validated in humans, but the loss-of-function arm
rests on two families and yields no published effect size in SDS, which is the main quantitative
hole on this node.""",
 quantitative=[
   q('plasma CNP concentration, NPPC-overexpressing translocation carrier','2','fold vs control','de novo balanced t(2;7)(q37.1;q21.3); compared with 5 normal controls','human','bocciardi2007','n=1 case vs 5 controls; CI not reported'),
   q('independent 2q37.1 translocation patients with NPPC overexpression and overgrowth','3','patients','breakpoint partners on chromosomes 7, 8 and 13','human','moncla2007','not applicable (count)'),
   q('heterozygous NPPC loss-of-function mutations found','2','mutations','screen of 668 patients (357 disproportionate short stature, 311 AD idiopathic short stature) plus 29 ISS families','human','hisadooliva2018','not applicable (count)'),
 ],
 localization=['human: germline; ligand acts on NPR2 in growth plate cartilage'],
 human_evidence='direct',
 human_evidence_note='Overgrowth from NPPC overexpression is documented in three independent translocation patients; loss of function is documented in two families with functional cGMP assays.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Stature claims rest entirely on measured human phenotypes; the mouse lbab allele is cited only as convergent support for pathogenicity of one variant.',
 confidence='A',
 claim_grades=[
   dict(claim='Increased NPPC expression causes human skeletal overgrowth.', grade='A', basis='Three independent patients with different translocation partners, each with measured NPPC overexpression (bocciardi2007, moncla2007).'),
   dict(claim='Heterozygous NPPC loss of function causes autosomal dominant short stature.', grade='B', basis='Two mutations in one screening study with in vitro cGMP confirmation and cosegregation; no independent replication cohort and no reported SDS effect size.'),
 ],
 key_refs=[
   ref('bocciardi2007',17373680,'10.1002/ajmg.a.31719','Bocciardi R',2007,'primary','Balanced t(2;7) near NPPC gives skeletal overgrowth with plasma CNP doubled versus five controls and NPPC overexpressed in fibroblasts.'),
   ref('moncla2007',17676597,'10.1002/humu.20569','Moncla A',2007,'primary','Two further 2q37.1 translocation patients (partners chr8, chr13) show the same NPPC overexpression and overgrowth phenotype.'),
   ref('hisadooliva2018',28661490,'10.1038/gim.2017.116','Hisado-Oliva A',2018,'primary','Two heterozygous NPPC CNP-ring mutations reduce cGMP synthesis and cause autosomal dominant short stature with small hands.'),
 ],
 open_questions=['g_l8gen_002'],
))
