import yaml
E=[]
def e(src,tgt,rel,sign,ctx,tier,refs,conf,mag=None,notes=None,ts=None,gap=None):
    d=dict(edge_id='e%05d'%(len(E)+1), source=src, target=tgt, relation=rel, sign=sign)
    if mag: d['magnitude']=mag
    d['context']=ctx; d['evidence_tier']=tier; d['refs']=refs; d['confidence']=conf
    if gap: d['gap_id']=gap
    if ts: d['timescale']=ts
    if notes: d['notes']=notes
    E.append(d)

# ================= L8 -> L3 =================
e('npr2_gene','npr2_receptor','required_for','+',
  'human, heterozygous NPR2 loss-of-function carriers within a 39-member acromesomelic dysplasia family, both sexes; germline',
  'T1',['olney2006','bartels2004'],'A',
  mag='height z -1.8 +/- 1.1 in 16 carriers vs -0.4 +/- 0.8 in 23 non-carriers (P<0.0005)',
  ts='lifetime (birth to adult height)',
  notes='Gene dosage sets receptor function: three tested AMDM missense alleles have markedly deficient guanylyl cyclase activity, and obligate carriers are below matched-control height.')
e('npr2_gene','cgmp_second_messenger','activates','+',
  'human, heterozygous NPR2 missense alleles from idiopathic short stature probands expressed in transfected cells; also 1:1 co-transfection with wild type',
  'T1',['vasques2013'],'A',
  mag='no detectable cGMP after CNP stimulation for all three mutants; significant reduction when co-expressed 1:1 with wild type',
  notes='Establishes the dominant-negative component of heterozygous NPR2 alleles, not merely halved dose.')
e('npr2_gene','npr2_receptor','activates','+',
  'human, heterozygous gain-of-function NPR2 p.Val883Met (guanylyl cyclase domain) and p.Arg655Cys (kinase homology domain); germline',
  'T1',['miura2012','hannema2013'],'A',
  mag='ligand-independent cGMP generation and elevated blood cGMP; tall stature with macrodactyly (V883M) or extreme tall stature without deformity (R655C)',
  ts='lifetime',
  notes='Opposite-direction human dosage arm. Together with olney2006 this makes NPR2 a two-sided human dose experiment on the same receptor.')
e('nppc_gene','cnp_protein','transcribes','+',
  'human, three patients with balanced translocations breaking in 2q37.1 (partners chr7, chr8, chr13); de novo, both sexes',
  'T1',['bocciardi2007','moncla2007'],'A',
  mag='plasma CNP doubled versus five controls; NPPC substantially overexpressed in fibroblasts, with skeletal overgrowth',
  notes='Three independent chromosomal partners converge on NPPC overexpression, proposed to separate the gene from a negative regulatory element.')
e('nppc_gene','npr2_receptor','activates','+',
  'human, two families with heterozygous NPPC mutations in the conserved CNP ring; autosomal dominant short stature with small hands',
  'T1',['hisadooliva2018'],'B',
  mag='significant reduction in cGMP synthesis by the mutant ligands; screen of 668 patients plus 29 ISS families',
  notes='Ligand-side loss of function reduces receptor output; effect size in SDS not reported.')
e('fgfr3_gene','fgfr3_receptor','inhibits','-',
  'human, heterozygous germline FGFR3 activating alleles; achondroplasia G380R, hypochondroplasia N540K, thanatophoric dysplasia K650E/R248C, both sexes',
  'T1',['shiang1994','bellus1995','tavormina1995'],'A',
  mag='graded constitutive kinase activation across four disorders; adult height 132 cm (M) / 124 cm (F) in achondroplasia',
  ts='effect established within the first two postnatal years',
  notes='Sign is negative because FGFR3 is a negative regulator of bone growth: activating the receptor shortens the bone.')
e('fgfr3_gene','fgfr3_receptor','activates','+',
  'human, heterozygous FGFR3 p.R621H (and p.R621C in a second family), partial loss of kinase function; CATSHL syndrome, both sexes',
  'T1',['toydemir2006'],'B',
  mag='tall stature with camptodactyly, scoliosis and hearing loss, recapitulating the Fgfr3-knockout mouse phenotype',
  ts='lifetime',
  notes='The loss-of-function arm. Sign is positive on growth: reducing FGFR3 signalling lengthens bone. Graded B because the original report is one family, with one independent confirmatory family since.')
e('ihh_gene','ihh_protein','required_for','+',
  'human, 16 probands with heterozygous IHH variants including the first complete IHH deletion; plus homozygous IHH mutations causing acrocapitofemoral dysplasia',
  'T1',['sentchordimont2020','hellemans2003'],'A',
  mag='heterozygous carriers show mild-to-moderate short stature with fifth-finger middle phalanx shortening; biallelic loss gives cone-shaped epiphyses of hands and hips',
  ts='lifetime',
  notes='Penetrance is incomplete: 5 of 16 heterozygous carriers were of normal height. IHH is nonetheless the commonest gene found on growth-plate panels in idiopathic short stature (4/102).')
e('ihh_gene','ihh_protein','activates','unknown',
  'human, three large families with heterozygous missense mutations in the IHH amino-terminal signalling domain; brachydactyly type A-1',
  'T1',['gao2001'],'B',
  mag='three mutated residues predicted to be adjacent on the IHH surface; middle phalanges shortened or absent',
  notes='Sign recorded as unknown deliberately: BDA-1 missense alleles do not phenocopy IHH haploinsufficiency, so they are not simple loss of function and the direction of effect on Hedgehog output is not established.')
e('pth1r_gene','pth1r_receptor','activates','+',
  'human, heterozygous PTH1R His223Arg in the first intracellular loop; Jansen-type metaphyseal chondrodysplasia, germline',
  'T1',['schipani1995'],'A',
  mag='constitutive ligand-independent cAMP accumulation in COS-7 cells, absent in wild type; short-limbed dwarfism with hypercalcaemia and hypophosphataemia',
  ts='prenatal onset, lifelong',
  notes='Gain of function delays hypertrophic differentiation and shortens limbs, the direction predicted by the PTHrP-IHH loop.')
e('pth1r_gene','pth1r_receptor','required_for','+',
  'human, Blomstrand chondrodysplasia; maternal splice-altering PTH1R allele expressed, paternal allele silent, so chondrocytes carry functionally zero receptor',
  'T1',['jobert1998'],'D',
  mag='mutant receptor well expressed but binds neither PTH nor PTHrP and gives no cAMP or inositol phosphate response; lethal with advanced endochondral maturation',
  notes='Single patient, and the null state arose from allele-specific non-expression rather than biallelic mutation. Graded D on that basis despite the clarity of the biochemistry.')
e('hdac4_gene','hdac4_protein','required_for','+',
  'human, six overlapping 2q37.3 deletions narrowing the critical region to HDAC4, plus de novo intragenic HDAC4 deletion and frameshift in deletion-negative patients; both sexes',
  'T1',['williams2010','le2019'],'B',
  mag='brachydactyly type E in 48% and short stature among 103 individuals with 2q37 deletion; penetrance markedly incomplete',
  ts='childhood through adult stature',
  notes='Losing a repressor of chondrocyte hypertrophy shortens the digits, the direction expected if hypertrophic differentiation is advanced rather than extended.')

# ================= L8 -> L5 =================
e('acan_gene','aggrecan_acan','required_for','+',
  'human, 103 individuals from 20 families with heterozygous ACAN loss-of-function variants, both sexes, childhood through adult height',
  'T1',['gkourogianni2017','nilsson2014_2'],'A',
  mag='adult median height -2.8 SDS (range -5.9 to -0.9); childhood median -2.0 SDS (range -4.2 to -0.6)',
  ts='deficit widens from childhood to adult height, with premature growth cessation',
  notes='Perfect cosegregation of variant and phenotype across 20 families. Bone age is ADVANCED, not delayed, so the mechanism is a shortened growth window rather than a slowed plate.')
e('acan_gene','acan_dosage_effect','required_for','+',
  'human, same 20-family cohort; ACAN haploinsufficiency versus two functional copies',
  'T1',['gkourogianni2017'],'A',
  mag='one functional ACAN copy costs approximately 2.8 SDS of adult height',
  notes='No genotype-phenotype correlation was found between ACAN mutation class and joint involvement, so within this locus the dominant-negative/haploinsufficiency distinction does not stratify outcome.')
e('col10a1_gene','collagen_type_x','required_for','+',
  'human, 128 metaphyseal chondrodysplasia Schmid cases (4 new plus 124 published), heterozygous, both sexes, at first presentation',
  'T1',['meng2025','warman1993'],'A',
  mag='height Z -3.62 +/- 1.95 for missense (dominant-negative) versus -1.99 +/- 1.28 for truncating (haploinsufficient) variants, P=0.013',
  ts='onset median 12 months for NC1-domain variants versus 72 months for non-NC1 (P=0.0014)',
  notes='The only locus in this atlas where dominant-negative and haploinsufficient alleles of one gene have measured stature effects in the same cohort: interference costs ~1.6 SDS more than losing a copy.')
e('col10a1_gene','hypertrophic_chondrocyte','required_for','+',
  'human, COL10A1 p.W651fsX666 assayed in vitro for trimerisation against wild-type collagen X',
  'T1',['yang2025'],'C',
  mag='mutant chain disrupts trimerisation of normal collagen X, indicating dominant-negative interference rather than simple mRNA decay',
  notes='In vitro human-protein assay; the link to the hypertrophic chondrocyte is by restricted expression of collagen X rather than by direct tissue measurement.')
e('col2a1_gene','collagen_type_ii','required_for','+',
  'human, seven unrelated SEDC families carrying six triple-helical glycine substitutions plus one intronic variant; heterozygous, both sexes',
  'T1',['zhan2025'],'B',
  mag='disproportionate short stature with platyspondyly and delayed epiphyseal ossification in all seven families',
  notes='No published mean adult height SDS by COL2A1 mutation class exists, which is why no magnitude in SDS is given here. See gap g_l8gen_005.')
e('comp_gene','comp_protein','required_for','+',
  'human, 830 genetically diagnosed PSACH/EDM1 patients (471 probands, 224 COMP variants) aggregated from 106 publications, both sexes',
  'T1',['ni2026','briggs1995'],'B',
  mag='80.8% of variants missense, 87.7% of probands in the type-3 calcium-binding repeat; PSACH significantly shorter than EDM1 (P<0.001)',
  notes='Mechanism is misfolding and ER retention of the pentamer, not dosage: this is why COMP missense alleles are far more severe than null alleles.')

# ================= L8 -> L4 =================
e('ghr_gene','gh_receptor','required_for','+',
  'human, homozygous GHR loss-of-function (Laron syndrome), 69-patient cohort of Middle Eastern and Mediterranean origin followed over 50 years, both sexes',
  'T1',['laron2015','godowski1989','amselem1989'],'A',
  mag='-4 to -10 height SDS with high circulating GH and low IGF-1; only homozygotes express the disease',
  ts='postnatal; birth size is near-normal because fetal growth is largely GH-independent',
  notes='The largest monogenic stature effect in this atlas. Fixes the causal direction of the somatomedin hypothesis in humans: abolishing the receptor while the ligand is elevated produces near-complete growth failure.')
e('stat5b_gene','stat5b_tf','required_for','+',
  'human, two unrelated consanguineous pedigrees with homozygous STAT5B mutations; one with total absence of STAT5B protein',
  'T1',['hwa2005','kofoed2003'],'B',
  mag='height -7.8 SDS (114 cm at 16.4 years) with IGF-1 7.2 ng/ml against a normal range of 242-600, and no response to an IGF-1 generation test',
  ts='postnatal growth failure with growth hormone insensitivity',
  notes='Places the lesion below the GH receptor: GH and GH-binding protein are normal to elevated while IGF-1 generation fails. Immune dysfunction accompanies it because STAT5B also transduces IL-2 receptor signalling.')
e('igfals_gene','als_igfals','required_for','+',
  'human, 17 patients carrying 14 distinct IGFALS mutations, prepubertal and pubertal, both sexes',
  'T1',['domen2009','domen2004'],'A',
  mag='prepubertal height SDS between -2 and -3, about 1.4 SD below midparental height SDS; pubertal delay in 50%',
  ts='postnatal, prepubertal onset',
  notes='The key quantitative point is how MILD this is: near-total collapse of the circulating IGF ternary complex costs only ~1.4 SDS, which argues the plate is driven by local rather than circulating IGF-1.')
e('igfals_gene','igf_ternary_complex','required_for','+',
  'human, same 17-patient series; IGF-1, IGF-II, IGFBP-1, -2 and -3 all measured',
  'T1',['domen2004','domen2009'],'A',
  mag='extraordinarily low serum IGF-1 and IGFBP-3 that remain abnormally low after GH stimulation, greatest reduction in IGFBP-3',
  notes='ALS loss disrupts the entire circulating IGF system, not one component.')
e('pappa2_gene','pappa2_protease','required_for','+',
  'human, two unrelated families with homozygous PAPPA2 p.D643fs25* or p.Ala1033Val; progressive growth failure, both sexes',
  'T1',['dauber2016'],'B',
  mag='complete absence of PAPP-A2 proteolytic activity in vitro; total IGF-1, IGFBP-3, IGFBP-5, ALS and IGF-II all ELEVATED while free IGF-1 is decreased',
  notes='Inverts the usual biochemical signature of short stature and falsifies the use of total serum IGF-1 as a proxy for IGF-1 action.')
e('pappa2_gene','igf_ternary_complex','degrades','-',
  'human, same two families; size-exclusion chromatography of patient serum',
  'T1',['dauber2016'],'B',
  mag='significant increase in IGF-1 retained within the ternary complex when PAPP-A2 activity is absent',
  notes='Direct human demonstration that the protease liberates IGF-1 from the ternary complex.')
e('igf1r_gene','igf1_receptor','required_for','+',
  'human, compound heterozygote for IGF1R exon-2 Arg108Gln and Lys115Asn, screened from 42 patients with unexplained IUGR plus short stature',
  'T1',['abuzzahab2003'],'B',
  mag='decreased IGF-I binding in cultured patient fibroblasts; intrauterine and postnatal growth retardation with normal or elevated IGF-1',
  ts='prenatal and postnatal',
  notes='The mirror image of the GHR/Laron signature: low birth size, no catch-up, normal-to-high IGF-1, blunted rhGH response.')
e('igf1_gene','igf1_systemic','required_for','+',
  'human, homozygous partial IGF1 gene deletion; single patient with intrauterine growth retardation, postnatal growth failure, deafness and mental retardation',
  'T1',['woods1996'],'D',
  mag='growth failure from before birth, unlike GH deficiency or GH receptor deficiency which spare prenatal growth',
  ts='prenatal onset, persisting postnatally',
  notes='Single patient. Places IGF1 downstream of the point at which the somatotropic axis becomes GH-dependent.')
e('igf1_gene','adult_height_attainment','correlates_with','+',
  'human, two-sample Mendelian randomization; UK Biobank IGF-1 instruments against GIANT height excluding UK Biobank across five ancestry groups (n>1.8M), plus ALSPAC ages 7-17',
  'T1',['de2026'],'A',
  mag='0.09 SD taller adult height per 1 SD higher genetically predicted serum IGF-1',
  ts='childhood through adult height',
  notes='The population-scale counterpart to the Laron and IGFALS phenotypes. The gap between a catastrophic null and a 0.09 SD/SD slope quantifies how strongly buffered this axis is.')
e('esr1_gene','estrogen_receptor_alpha','required_for','+',
  'human, man homozygous for a disruptive ESR1 mutation, and a woman with an ESR1 variant and estrogen resistance',
  'T1',['smith1994','quaynor2013'],'B',
  mag='204 cm adult height with incomplete epiphyseal closure and continued linear growth into adulthood, despite elevated estradiol and normal testosterone; lumbar BMD 3.1 SD below the young adult mean',
  ts='growth continues past the normal age of fusion',
  notes='Establishes in humans that estrogen acting through ESR1, not androgen and not circulating estrogen concentration, closes the growth plate in both sexes.')
e('esr1_gene','epiphyseal_fusion','required_for','+',
  'human, ESR1-null male with radiographically incomplete epiphyseal closure in adulthood',
  'T1',['smith1994'],'B',
  mag='epiphyses unfused at age 28 despite otherwise normal pubertal development',
  ts='fusion fails to occur at the normal age',
  notes='Receptor-side arm of the estrogen-fusion pair; the ligand-side arm is cyp19a1_gene.')
e('cyp19a1_gene','aromatase_cyp19a1','required_for','+',
  'human, XX and XY siblings with a novel CYP19 mutation, plus four adult aromatase-deficient men',
  'T1',['morishima1995','rochira2010'],'A',
  mag='absent estrogen action with elevated testosterone, androstenedione and 17-hydroxyprogesterone and low estradiol; tall stature in both sexes',
  ts='tall stature accrues through failure of timely fusion',
  notes='Ligand-side arm of the estrogen-fusion pair. Rochira 2010 adds the constraint that these men are tall DESPITE a severely impaired GH response to GHRH-arginine and low IGF-1.')
e('cyp19a1_gene','estradiol_hormone','required_for','+',
  'human, aromatase-deficient man treated sequentially with testosterone and then estradiol',
  'T1',['carani1997','morishima1995'],'A',
  mag='only estradiol produced the skeletal response; testosterone did not',
  ts='months of hormone replacement',
  notes='The intervention arm that closes the loop: it is the estrogen product, not the androgen substrate, that acts on the skeleton.')

# ================= L8 -> L11 =================
e('shox_gene','shox_haploinsufficiency','required_for','+',
  'human, 41 patients from 23 families across the full SHOX dose series (nullizygous, haploinsufficient, mild), both sexes',
  'T1',['doan2026','rao1997','shears1998'],'A',
  mag='median height SDS -6.3 nullizygous (Langer), -2.4 haploinsufficient (Leri-Weill), -2.1 in SHOX-positive idiopathic short stature',
  ts='childhood through adult height',
  notes='A monotonic 0/1/2-copy human dose series. SHOX has no rodent orthologue, so this series has no animal counterpart to launder.')
e('shox_gene','turner_syndrome','required_for','+',
  'human, PAR1 deletions encompassing SHOX in individuals with Xp22 or Yp11.3 rearrangements and in Turner syndrome',
  'T1',['rao1997'],'B',
  mag='a 170 kb PAR1 interval deleted in 36 short-statured individuals and in none of their normal-height relatives or 30 normal-height rearrangement carriers',
  notes='SHOX haploinsufficiency is the mechanism by which loss of one sex chromosome shortens stature; it does not account for the whole Turner height deficit.')
e('acan_gene','acan_related_short_stature','required_for','+',
  'human, 103 individuals from 20 families, both sexes',
  'T1',['gkourogianni2017'],'A',
  mag='adult median height -2.8 SDS with advanced bone age; early-onset osteoarthritis in 12 of 20 families',
  ts='lifetime, with premature growth cessation')
e('col10a1_gene','schmid_metaphyseal_chondrodysplasia','required_for','+',
  'human, large Mormon kindred (lod 18.2 at theta=0) plus 128 aggregated cases',
  'T1',['warman1993','meng2025'],'A',
  mag='height Z -3.62 (missense) or -1.99 (truncating) at first presentation',
  ts='onset median 12 months (NC1-domain) or 72 months (non-NC1)')
e('comp_gene','pseudoachondroplasia','required_for','+',
  'human, 471 probands with COMP variants across 106 publications',
  'T1',['briggs1995','ni2026'],'A',
  mag='PSACH significantly shorter and earlier-onset than the allelic EDM1 phenotype (P<0.001)')
e('comp_gene','multiple_epiphyseal_dysplasia','required_for','+',
  'human, same 830-patient aggregation; EDM1 subset',
  'T1',['briggs1995','ni2026'],'A',
  mag='allelic with PSACH at the same COMP calcium-binding domain but milder stature phenotype')
e('col2a1_gene','spondyloepiphyseal_dysplasia','required_for','+',
  'human, seven unrelated Chinese SEDC families with six triple-helical glycine substitutions',
  'T1',['zhan2025','webb2026'],'A',
  mag='disproportionate short stature in all affected; GH gave +0.76 and +0.27 height SDS over 3.5 and 3 years in two children',
  ts='GH response measured over 3-3.5 years')
e('ghr_gene','laron_syndrome','required_for','+',
  'human, 69-patient cohort followed over 50 years; homozygous GHR deletions and missense alleles',
  'T1',['laron2015','godowski1989','amselem1989'],'A',
  mag='-4 to -10 height SDS with high GH and low IGF-1')
e('stat5b_gene','stat5b_deficiency','required_for','+',
  'human, two unrelated consanguineous pedigrees with homozygous STAT5B mutations',
  'T1',['kofoed2003','hwa2005'],'A',
  mag='height -7.8 SDS in the protein-null patient, with IGF-1 7.2 ng/ml (normal 242-600)')
e('pappa2_gene','pappa2_deficiency','required_for','+',
  'human, two unrelated families with homozygous PAPPA2 mutations',
  'T1',['dauber2016'],'A',
  mag='progressive growth failure with microcephaly and thin long bones despite elevated total IGF-1')
e('igf1r_gene','igf1r_mutation_human','required_for','+',
  'human, compound heterozygote identified from 42 IUGR plus short-stature patients',
  'T1',['abuzzahab2003'],'A',
  mag='intrauterine and postnatal growth retardation with reduced fibroblast IGF-I binding')
e('igf1_gene','igf1_deficiency_human','required_for','+',
  'human, homozygous partial IGF1 deletion, single patient',
  'T1',['woods1996'],'B',
  mag='intrauterine growth retardation with postnatal growth failure, deafness and mental retardation')
e('esr1_gene','estrogen_resistance_esr1','required_for','+',
  'human, homozygous ESR1 disruptive mutation (male) and an ESR1 variant with estrogen resistance (female)',
  'T1',['smith1994','quaynor2013'],'A',
  mag='204 cm adult height with unfused epiphyses in the index male')
e('cyp19a1_gene','aromatase_deficiency_human','required_for','+',
  'human, XX and XY siblings plus four adult men with CYP19A1 mutations',
  'T1',['morishima1995','carani1997','rochira2010'],'A',
  mag='tall stature with unfused epiphyses; severely impaired GH response to GHRH-arginine')
e('fgfr3_gene','achondroplasia','required_for','+',
  'human, heterozygous FGFR3 c.1138G>A/G>C (G380R), predominantly de novo and paternal in origin',
  'T1',['shiang1994','rousseau1994'],'A',
  mag='G380R on 16 of 16 achondroplasia chromosomes examined')
e('fgfr3_gene','hypochondroplasia','required_for','+',
  'human, heterozygous FGFR3 N540K in the tyrosine kinase domain',
  'T1',['bellus1995'],'A',
  mag='weaker constitutive activation than G380R, with a correspondingly milder stature deficit')
e('npr2_gene','npr2_heterozygous_short_stature','required_for','+',
  'human, heterozygous NPR2 loss-of-function carriers in family and idiopathic-short-stature cohorts',
  'T1',['olney2006','vasques2013','hisadooliva2015'],'A',
  mag='height z -1.8 +/- 1.1 in carriers; pathogenic NPR2 alleles in ~3% of SHOX-negative Leri-Weill referrals')
e('npr2_gene','npr2_gain_of_function_tall','required_for','+',
  'human, heterozygous NPR2 p.Val883Met and p.Arg655Cys, germline',
  'T1',['miura2012','hannema2013'],'A',
  mag='ligand-independent and hyper-stimulated cGMP production with tall stature')
e('nppc_gene','nppc_duplication_tall_stature','required_for','+',
  'human, three patients with 2q37.1 balanced translocations and NPPC overexpression',
  'T1',['bocciardi2007','moncla2007'],'A',
  mag='plasma CNP doubled versus five controls, with overgrowth and cartilage dysplasia')
e('pth1r_gene','jansen_metaphyseal_chondrodysplasia','required_for','+',
  'human, heterozygous PTH1R His223Arg, germline',
  'T1',['schipani1995'],'A',
  mag='constitutive ligand-independent cAMP accumulation with short-limbed dwarfism and hypercalcaemia')
e('pth1r_gene','blomstrand_chondrodysplasia','required_for','+',
  'human, splice-altering maternal PTH1R allele with the paternal allele unexpressed',
  'T1',['jobert1998'],'D',
  mag='receptor binds neither PTH nor PTHrP; lethal with advanced endochondral bone maturation',
  notes='Single patient; graded D.')
e('igfals_gene','igf1_deficiency_human','correlates_with','+',
  'human, 17 patients with 14 IGFALS mutations',
  'T1',['domen2009'],'B',
  mag='profoundly low circulating IGF-1 but only -1.4 SDS below midparental height',
  notes='The dissociation between circulating IGF-1 and stature is the informative part.')
e('hdac4_gene','idiopathic_short_stature','correlates_with','-',
  'human, 103 individuals with 2q37 deletion syndrome; incomplete penetrance',
  'T1',['le2019','williams2010'],'C',
  mag='brachydactyly type E in 48% and short stature among the cardinal features',
  notes='Graded C because no mean height SDS specific to HDAC4-mutation carriers, as distinct from whole-2q37-deletion carriers, has been published.')

# ================= architecture / method edges =================
e('height_gwas','height_polygenic_score','required_for','+',
  'human, 5.4M individuals of diverse ancestries; out-of-sample prediction',
  'T1',['yengo2022'],'A',
  mag='12,111 SNPs explain 40% of phenotypic variance in European-ancestry and 10-20% in other-ancestry populations')
e('assortative_mating_height','height_heritability','correlates_with','+',
  'human, 47,135 co-parents from the Norwegian Mother, Father and Child Cohort plus relative-similarity modelling',
  'T1',['sunde2024'],'B',
  mag='genetic assortative mating detected in 9 of 16 traits; distant relatives more affected than close ones',
  ts='cumulative across generations',
  notes='Direction is positive: assortment raises trait genetic variance and relative similarity, inflating heritability estimated from relatives. Magnitude specific to height is not published.')
e('rare_variant_height','missing_heritability_height','required_for','+',
  'human, 347,630 UK Biobank whole genomes across 34 traits, plus 333,100 WGS for rare non-coding height signals',
  'T1',['wainschtein2026','hawkes2024'],'A',
  mag='rare variants contribute 20% and common variants 68% of pedigree heritability; 79% of the rare component is non-coding',
  notes='Sign is positive on explained heritability: including rare variants closes most of the gap.')
e('height_gwas','common_vs_rare_pathway_divergence','correlates_with','unknown',
  'human, three published height pathway-enrichment analyses (n=30,147; 183,727; 253,288) compared against the 2023 skeletal disorder nosology',
  'T1',['wood2014','weedon2008','lango2010','unger2023'],'C',
  mag='0 of 3 height GWAS enrichment lists name the GH-IGF/somatotropic axis, which supplies the largest monogenic stature effects (-4 to -10 SDS)',
  notes='Records the divergence as an observation. The explanatory mechanism is untested and is held at grade E on the target node.')
e('de_novo_variant_growth','fgfr3_gene','activates','+',
  'human male germline; 10 FGFR3 missense substitutions assayed by digital PCR across a dissected postmortem testis, donors of varying age',
  'T1',['moura2024','neville2025'],'B',
  mag='9 of 10 substitutions raise ligand-independent FGFR3 signalling; germline positive selection gives a 2-3 fold enrichment of disease-causing mutations',
  ts='accumulates across the reproductive lifespan (1.67 mutations/year/haploid genome)',
  notes='Mechanistic basis of the paternal age effect in achondroplasia: the mutation is selected for in spermatogonia, not merely tolerated.')
e('igf2_h19_imprinting','russell_silver_syndrome','required_for','+',
  'human, 11p15.5 ICR1 loss of methylation on the paternal allele',
  'T1',['abi2019'],'B',
  mag='accounts for approximately 60% of Silver-Russell syndrome; severe intrauterine and postnatal growth retardation')
e('igf2_h19_imprinting','beckwith_wiedemann_syndrome','required_for','+',
  'human, 11p15.5 ICR1 hypermethylation on the maternal allele',
  'T1',['abi2019'],'B',
  mag='approximately 10% of Beckwith-Wiedemann syndrome; overgrowth phenotype',
  notes='Reciprocal to the Silver-Russell lesion at the same 11p15.5 element.')
e('uniparental_disomy_growth','igf2_h19_imprinting','inhibits','-',
  'human, 60 genetically confirmed Temple syndrome patients (31 UPD(14)mat, 22 epimutation, 5 deletion)',
  'T1',['abi2019','ogawa2025'],'D',
  mag='14q32.2 hypomethylation lowers IGF2 expression at 11p15.5, producing a transcriptional signature shared with Silver-Russell syndrome',
  notes='Single transcriptional-profiling study for the trans effect; graded D on that basis even though the Temple phenotype itself is A-grade.')
e('dna_methylation_growth_plate','height_gwas','correlates_with','+',
  'human, 72 developing chondrocyte samples 7-21 post-conception weeks, ~700,000 CpGs',
  'T1',['mcdonnell2024','richard2025'],'B',
  mag='>8,200 developmental differentially methylated regions; 24 loci where skeletal disease risk variants colocalise with methylation QTLs',
  ts='7-21 post-conception weeks',
  notes='Identifies a developmental-only regulatory class that would be invisible in adult-tissue eQTL catalogues - a specific route by which height-associated non-coding variants could act.')

yaml.dump({'edges':E}, open('/home/user/growth-plate/atlas/edges/shards/l8gen.edges.yaml','w'),
          sort_keys=False, default_flow_style=False, width=100, allow_unicode=True)
print('edges written:', len(E))
