from w import *

write(dict(id='esr1_gene', name='ESR1', type='gene', layer='L8',
 aliases=['estrogen receptor alpha gene','ESR1 estrogen resistance'],
 summary="""ESR1 supplies the single most decisive human experiment in the fusion literature. Smith 1994
described a 28-year-old man homozygous for a disruptive ESR1 mutation who was 204 cm tall with
incomplete epiphyseal closure and a history of continued linear growth into adulthood despite
otherwise normal pubertal development; serum estradiol and estrone were elevated, testosterone was
normal, FSH and LH were increased, and lumbar spine bone mineral density was 0.745 g/cm2, 3.1 SD
below the young adult mean. He was normally masculinised, so androgen action was intact. The
inference is unavoidable and does not require a mouse: in humans it is estrogen acting through
ESR1, not androgen and not estrogen concentration per se, that closes the growth plate and
mineralises bone, in both sexes. Quaynor 2013 supplied the female counterpart, a woman with an ESR1
variant, delayed puberty and estrogen resistance. Because oestrogen was high and the receptor was
absent, the experiment separates ligand from receptor in a way no pharmacological study can. The
node is graded on a single index male plus one female case, which is thin by cohort standards but
epistemically strong because the phenotype is a natural knockout with an unambiguous readout.""",
 quantitative=[
   q('adult height, homozygous ESR1 disruptive mutation (male)','204','cm','28-year-old man, normal masculinisation, continued linear growth into adulthood','human','smith1994','n=1'),
   q('lumbar spine bone mineral density, same patient','0.745','g/cm2','dual-energy absorptiometry','human','smith1994','3.1 SD below the young adult mean'),
   q('epiphyseal closure status','incomplete','qualitative','radiographic assessment in adulthood','human','smith1994','n=1'),
 ],
 localization=['human: germline; receptor acts in growth plate chondrocytes, bone and the hypothalamic-pituitary axis'],
 human_evidence='direct',
 human_evidence_note='Two human loss-of-function patients (one male, one female) with measured stature, bone density and gonadotropins.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human receptor-null phenotype; the mouse ERKO literature is not needed and is not invoked.',
 confidence='B',
 claim_grades=[
   dict(claim='Estrogen acting through ESR1 is required for epiphyseal fusion in humans of both sexes.', grade='A', basis='Male ESR1-null with unfused plates and continued growth despite high estradiol (smith1994) plus independent female estrogen-resistance case (quaynor2013), and the concordant aromatase-deficiency series which removes ligand rather than receptor.'),
   dict(claim='The adult-height effect of ESR1 loss is about +204 cm / continued growth.', grade='D', basis='Single male patient; no cohort exists because the genotype is exceptionally rare.'),
 ],
 key_refs=[
   R('smith1994','A man homozygous for a disruptive ESR1 mutation reached 204 cm with unfused epiphyses, elevated estradiol, normal testosterone and lumbar BMD 3.1 SD below the young adult mean.'),
   R('quaynor2013','A woman with an ESR1 alpha variant showed delayed puberty and estrogen resistance.'),
 ],
))

write(dict(id='cyp19a1_gene', name='CYP19A1', type='gene', layer='L8',
 aliases=['aromatase gene','CYP19'],
 summary="""CYP19A1 encodes aromatase, the single enzyme converting androgens to estrogens, and its human
loss-of-function phenotype is the ligand-side control for the ESR1 receptor-side experiment.
Morishima 1995 reported a novel CYP19 mutation in an XX proband and her brother: the 28-year-old
sister had non-adrenal female pseudohermaphroditism at birth, progressive virilisation at the age
of puberty, pubertal failure with no signs of estrogen action, hypergonadotropic hypogonadism,
polycystic ovaries and tall stature, with elevated plasma testosterone, androstenedione and
17-hydroxyprogesterone and low estradiol. Carani 1997 then performed the intervention that closes
the loop, treating an aromatase-deficient man with testosterone and then estradiol and showing that
only estradiol produced the skeletal response. Rochira 2010 characterised four aromatase-deficient
men and found a paradox that constrains any simple model: their GH response to GHRH plus arginine
was severely impaired compared with 12 normal subjects and basal IGF-1 was low, yet they were tall.
Tall stature in aromatase deficiency therefore occurs despite, not because of, growth hormone -
the plate stays open long enough that a subnormal growth rate accumulates more total height than a
normal rate applied for a normal number of years. Aromatase deficiency and ESR1 disruption together
form the ligand/receptor pair that makes the estrogen-fusion claim in this atlas an A-grade human
result rather than an extrapolation.""",
 quantitative=[
   q('GH response to GHRH plus arginine, aromatase-deficient men','severely impaired','qualitative','n=4 aromatase-deficient men versus 12 normal subjects','human','rochira2010','P < 0.001; peak values not restated in abstract'),
   q('stature phenotype of untreated aromatase deficiency','tall','qualitative','XX proband followed from infancy plus XY sibling; four further adult men','human','morishima1995','no cohort mean height reported'),
 ],
 localization=['human: germline; aromatase expressed in ovary, testis, placenta, brain and adipose tissue under alternative tissue-specific promoters'],
 human_evidence='direct',
 human_evidence_note='Human enzyme-deficient patients of both sexes, with an intervention arm (testosterone versus estradiol) in an affected man.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human enzyme deficiency with human hormone-replacement intervention.',
 confidence='A',
 claim_grades=[
   dict(claim='Loss of aromatase activity prevents epiphyseal fusion and produces tall stature in humans of both sexes.', grade='A', basis='Sibling pair with the enzyme defect (morishima1995), an intervention showing estradiol but not testosterone restores the skeletal response (carani1997), and four further adult men (rochira2010).'),
   dict(claim='Tall stature in aromatase deficiency occurs despite an impaired GH-IGF-1 axis.', grade='B', basis='Case-control GH stimulation testing in 4 patients versus 12 controls (rochira2010); single study, small n.'),
 ],
 key_refs=[
   R('morishima1995','A novel CYP19 mutation in XX and XY siblings gives absent estrogen action, hypergonadotropic hypogonadism and tall stature.'),
   R('carani1997','In an aromatase-deficient man, estradiol but not testosterone produced the skeletal response.'),
   R('rochira2010','Four aromatase-deficient men had severely impaired GH response to GHRH-arginine and low IGF-1 yet were tall.'),
 ],
))

write(dict(id='hdac4_gene', name='HDAC4', type='gene', layer='L8',
 aliases=['histone deacetylase 4 gene','2q37 deletion syndrome gene'],
 summary="""HDAC4 encodes the class IIa histone deacetylase that restrains RUNX2-driven and MEF2C-driven
chondrocyte hypertrophy, and human haploinsufficiency of it defines the skeletal component of 2q37
deletion syndrome. Williams 2010 analysed six individuals with overlapping 2q37.3 deletions to
reduce the critical region from more than 20 candidate genes to HDAC4 alone, then found HDAC4
point lesions - an intragenic deletion disrupting splicing and an intragenic insertion causing a
frameshift and premature stop - in individuals with the same clinical picture but no 2q37 deletion.
That two-step argument (interval narrowing followed by intragenic mutation in deletion-negative
cases) is what establishes HDAC4 as the causal gene rather than a positional bystander. The
skeletal phenotype is brachydactyly type E - shortened metacarpals and metatarsals - together with
short stature, alongside developmental delay, behavioural abnormalities and craniofacial
dysmorphism. Penetrance is markedly incomplete: in 103 individuals with 2q37 deletion the
supposedly cardinal features were present in only a fraction, with brachydactyly type E in 48% and
overweight/obesity in 34%. The mechanistic significance for the growth plate is the direction of
effect: losing a repressor of hypertrophy shortens the digits, which is the phenotype expected if
premature or excessive hypertrophic differentiation exhausts the plate rather than extends it.""",
 quantitative=[
   q('individuals used to narrow the 2q37.3 critical region to HDAC4','6','individuals','overlapping deletions; candidate genes reduced from >20 to 1','human','williams2010','not applicable (count)'),
   q('brachydactyly type E penetrance in 2q37 deletion syndrome','48','%','103 individuals (101 published plus 2 new) with 2q37 deletion','human','jean2019','not applicable (proportion)'),
   q('overweight or obesity penetrance in 2q37 deletion syndrome','34','%','same series','human','jean2019','not applicable (proportion)'),
   q('dysmorphic craniofacial feature penetrance','86','%','same series','human','jean2019','not applicable (proportion)'),
 ],
 localization=['human: germline 2q37.3; the deacetylase acts in prehypertrophic chondrocytes'],
 human_evidence='direct',
 human_evidence_note='Human deletion mapping plus intragenic mutations in deletion-negative patients, with penetrance quantified in 103 individuals.',
 species_basis=['human'],
 translation_risk='not_applicable',
 translation_risk_reason='Human genotype-phenotype only; the Hdac4-null mouse (premature ossification) is cited in hdac4_protein, not here.',
 confidence='B',
 claim_grades=[
   dict(claim='HDAC4 haploinsufficiency causes brachydactyly mental retardation syndrome including brachydactyly type E and short stature.', grade='A', basis='Critical-region narrowing plus de novo intragenic mutations in deletion-negative cases (williams2010), with a 103-individual genotype-phenotype series (jean2019).'),
   dict(claim='HDAC4 dosage sets adult stature quantitatively.', grade='D', basis='No published mean height SDS for HDAC4-mutation carriers as distinct from whole-2q37-deletion carriers. See gap g_l8gen_008.'),
 ],
 key_refs=[
   R('williams2010','Six overlapping 2q37.3 deletions narrow the critical region to HDAC4 alone; de novo intragenic HDAC4 mutations are found in deletion-negative patients with the same phenotype.'),
 ],
 open_questions=['g_l8gen_008'],
))
