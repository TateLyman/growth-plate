import yaml, os
D = '/home/user/growth-plate/atlas/nodes/L3_signaling_networks'

def w(n):
    n.setdefault('layer', 'L3'); n.setdefault('stub', False)
    n.setdefault('last_verified', '2026-08-05')
    order = ['id','name','aliases','type','layer','stub','summary','quantitative','localization',
             'human_evidence','human_evidence_note','species_basis','translation_risk',
             'translation_risk_reason','confidence','key_refs','open_questions','contradicts',
             'pending_source','last_verified']
    out = {k: n[k] for k in order if k in n}
    for k in n:
        if k not in out: out[k] = n[k]
    with open(os.path.join(D, n['id'] + '.yaml'), 'w') as f:
        yaml.safe_dump(out, f, sort_keys=False, default_flow_style=False, width=112, allow_unicode=True)
    print('wrote', n['id'])

N = []

N.append(dict(
 id='sox9_tf', name='SOX9', type='protein', aliases=['SRY-box transcription factor 9'],
 summary=(
  "SOX9 is the master chondrogenic transcription factor and the only node in this layer with an "
  "unambiguous human loss-of-function phenotype. Heterozygous SOX9 mutations and translocations cause "
  "campomelic dysplasia with bowed long bones, hypoplastic scapulae and autosomal XY sex reversal (Foster "
  "1994; Wagner 1994), so human haploinsufficiency alone is sufficient to derail skeletogenesis. In mouse, "
  "Sox9-null cells are excluded from cartilage condensations (Bi 1999), and staged inactivation shows "
  "successive requirements: for condensation, for overt chondrocyte differentiation, and for expression of "
  "Sox5 and Sox6 (Akiyama 2002). Later in the growth plate, SOX9 maintains columnar proliferation and is "
  "required to generate hypertrophy while simultaneously restraining Runx2 and beta-catenin, thereby "
  "blocking acquisition of an osteoblast phenotype; SOX9 protein outlives its mRNA into upper hypertrophic "
  "cells, where it acts with MEF2C to activate Col10a1 directly (Dy 2012, mouse). SOX9 is antagonised by "
  "and antagonises beta-catenin reciprocally (Akiyama 2004; Topol 2009), is suppressed by sustained Notch "
  "signalling (Kohn 2015), and drives its own nutrient supply via GLS1 (Stegen 2020) - making it the "
  "single most convergent node in L3."),
 localization=["mouse RZ/PZ/PHZ and upper HZ (protein): confirmed (dy2012)",
               "human: inferred from campomelic dysplasia haploinsufficiency (foster1994, wagner1994)"],
 human_evidence='direct',
 human_evidence_note='Heterozygous human SOX9 loss of function causes campomelic dysplasia, a defined skeletal phenotype.',
 species_basis=['human','mouse'], translation_risk='low',
 translation_risk_reason='Human haploinsufficiency phenotype and mouse conditional genetics agree in direction and in tissue.',
 confidence='A',
 key_refs=[
  dict(ref_id='foster1994', pmid='7990924', first_author='Foster JW', year=1994, type='primary',
       one_line_finding='Campomelic dysplasia with autosomal sex reversal is caused by mutations in the SRY-related gene SOX9.'),
  dict(ref_id='wagner1994', pmid='8001137', first_author='Wagner T', year=1994, type='primary',
       one_line_finding='Independent confirmation that mutations in and around SOX9 cause campomelic dysplasia and sex reversal.'),
  dict(ref_id='akiyama2002', pmid='12414734', first_author='Akiyama H', year=2002, type='primary',
       one_line_finding='Sox9 is required at successive steps of chondrocyte differentiation and for Sox5/Sox6 expression in mouse.'),
  dict(ref_id='dy2012', pmid='22421045', first_author='Dy P', year=2012, type='primary',
       one_line_finding='Sox9 maintains columnar proliferation, generates hypertrophy, restrains Runx2 and beta-catenin, and activates Col10a1 with Mef2c.'),
  dict(ref_id='bi1999', pmid='10319868', first_author='Bi W', year=1999, type='primary',
       one_line_finding='Sox9-null cells are excluded from cartilage condensations in mouse chimaeras.'),
 ],
 open_questions=['g_l3rest_012'],
 contradicts=['beta_catenin_ctnnb1'],
))

N.append(dict(
 id='sox5_tf', name='SOX5 (L-SOX5)', type='protein', aliases=['L-Sox5','SOX5'],
 summary=(
  "SOX5 is a SoxD-family factor with no transactivation domain of its own; it binds DNA as a dimer and "
  "raises the efficiency with which SOX9 activates cartilage matrix genes. Sox5 single-null mice have only "
  "mild skeletal abnormalities, and the requirement is revealed only in combination with Sox6: Sox5;Sox6 "
  "double-null fetuses die with generalised chondrodysplasia in which chondroblasts express essentially no "
  "cartilage matrix genes, begin proliferating only after a long delay, and epiphyseal chondroblasts "
  "ectopically switch on hypertrophic markers (Smits 2001, mouse). SOX5 expression is itself SOX9-dependent "
  "(Akiyama 2002, mouse). In human, heterozygous SOX5 loss of function causes Lamb-Shaffer syndrome, whose "
  "core features are neurodevelopmental with variable skeletal findings, so the human phenotype does not "
  "recapitulate the murine cartilage-specific requirement - a species discordance that should be stated "
  "explicitly rather than smoothed over."),
 localization=["mouse cartilage, all zones: co-expressed with Sox6 and Sox9 (smits2001)","human growth plate: unconfirmed"],
 human_evidence='indirect',
 human_evidence_note='Human SOX5 haploinsufficiency (Lamb-Shaffer syndrome) is primarily neurodevelopmental; no human growth plate data.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='The mouse requirement is only visible in the Sox5;Sox6 double null; the human heterozygous phenotype is a different organ system.',
 confidence='C',
 key_refs=[
  dict(ref_id='smits2001', pmid='11702786', first_author='Smits P', year=2001, type='primary',
       one_line_finding='Sox5 and Sox6 are individually near-dispensable but jointly essential for cartilage matrix gene expression and growth plate formation.'),
  dict(ref_id='akiyama2002', pmid='12414734', first_author='Akiyama H', year=2002, type='primary',
       one_line_finding='Sox9 is required for expression of Sox5 and Sox6.'),
 ],
))

N.append(dict(
 id='sox6_tf', name='SOX6', type='protein',
 summary=(
  "SOX6 is the near-identical paralogue of SOX5 and is functionally interchangeable with it in cartilage. "
  "Sox6 single nulls are born with mild skeletal abnormalities; Sox5;Sox6 double nulls have a severe "
  "generalised chondrodysplasia with matrix-deficient, rudimentary cartilages and disrupted growth plate "
  "formation, and epiphyseal chondroblasts inappropriately activate hypertrophic markers (Smits 2001, "
  "mouse). The redundancy means gene dose, not gene identity, is the variable, exactly as for BMP-SMAD1/5 "
  "and RUNX2/RUNX3 elsewhere in this layer. SOX6 expression requires SOX9 (Akiyama 2002, mouse). Human "
  "SOX6 variants have been reported with skeletal and haematological features, but no human growth plate "
  "SOX6 measurement or established SOX6 chondrodysplasia is available."),
 localization=["mouse cartilage, all zones: co-expressed with Sox5 and Sox9 (smits2001)","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No established human SOX6 chondrodysplasia and no human growth plate SOX6 data.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse double-knockout genetics only.',
 confidence='C',
 key_refs=[
  dict(ref_id='smits2001', pmid='11702786', first_author='Smits P', year=2001, type='primary',
       one_line_finding='Sox6 is redundant with Sox5; the double null has severe generalised chondrodysplasia.'),
  dict(ref_id='akiyama2002', pmid='12414734', first_author='Akiyama H', year=2002, type='primary',
       one_line_finding='Sox9 is required for Sox6 expression, placing SOX6 downstream of SOX9.'),
 ],
))

N.append(dict(
 id='sox_trio', name='SOX trio (SOX9-SOX5-SOX6)', type='process',
 aliases=['Sox trio','chondrogenic Sox trio'],
 summary=(
  "The 'SOX trio' is the functional unit of SOX9 plus the two SoxD proteins SOX5 and SOX6. SOX9 provides "
  "the transactivation domain and is required for SOX5 and SOX6 expression (Akiyama 2002, mouse); SOX5 and "
  "SOX6 lack transactivation domains and act as potent, mutually redundant enhancers of SOX9-driven matrix "
  "gene transcription (Smits 2001, mouse). The trio's collective output is what defines the chondrocyte: "
  "loss of SOX9 removes the lineage, whereas loss of both SoxD factors leaves cells that are still nominal "
  "chondroblasts but produce almost no matrix and initiate proliferation only after a long delay. The "
  "asymmetry matters for the atlas: SOX9 is the identity switch, SOX5/SOX6 are the gain. The trio also "
  "sets metabolic state - SOX9 drives glutamine uptake and GLS1, and the resulting acetyl-CoA is needed "
  "for the histone acetylation that keeps chondrogenic genes on (Stegen 2020) - so this is a "
  "transcription-metabolism feedforward loop, not a linear regulon. Human data exist for SOX9 only."),
 localization=["mouse cartilage: co-expression and hierarchy established (akiyama2002, smits2001)",
               "human growth plate: SOX9 inferred from campomelic dysplasia; SOX5/SOX6 unconfirmed"],
 human_evidence='indirect',
 human_evidence_note='Only the SOX9 member has direct human evidence (campomelic dysplasia); the trio as a unit has never been assayed in human tissue.',
 species_basis=['mouse','human'], translation_risk='moderate',
 translation_risk_reason='Hierarchy is mouse-derived; human evidence covers one of the three members.',
 confidence='B',
 key_refs=[
  dict(ref_id='akiyama2002', pmid='12414734', first_author='Akiyama H', year=2002, type='primary',
       one_line_finding='Sox9 acts at successive differentiation steps and is required for Sox5 and Sox6 expression.'),
  dict(ref_id='smits2001', pmid='11702786', first_author='Smits P', year=2001, type='primary',
       one_line_finding='Sox5 and Sox6 are redundant potent enhancers of chondroblast function.'),
  dict(ref_id='stegen2020', pmid='32470321', first_author='Stegen S', year=2020, type='primary',
       one_line_finding='SOX9 raises glutamine consumption and GLS1, and the resulting acetyl-CoA maintains chondrogenic histone acetylation.'),
 ],
))

N.append(dict(
 id='runx2_tf', name='RUNX2', type='protein', aliases=['CBFA1','AML3','RUNX2'],
 summary=(
  "RUNX2 is the transcription factor that licenses chondrocyte hypertrophy and osteoblast differentiation. "
  "Human heterozygous RUNX2/CBFA1 loss of function causes cleidocranial dysplasia with clavicular "
  "hypoplasia, delayed fontanelle closure, supernumerary teeth and short stature (Mundlos 1997), giving "
  "this node direct human dose evidence. In mouse, chondrocyte maturation is delayed in Runx2-null animals "
  "but still occurs; only Runx2;Runx3 double nulls show a complete absence of maturation, and limb length "
  "falls in proportion to the combined Runx2 and Runx3 gene dose (Yoshida 2004). The same study shows "
  "RUNX2 binds the Ihh promoter directly and induces Ihh, so RUNX2 sits upstream of the IHH/PTHrP loop as "
  "well as downstream of it - a feedback the linear textbook cascade omits. RUNX2 activity is restrained "
  "post-translationally rather than only transcriptionally: HDAC4 binds and inhibits RUNX2 (Vega 2004), "
  "ZFP521 antagonises RUNX2 through an HDAC4-dependent mechanism downstream of PTHrP (Correa 2010), and "
  "SOX9 keeps Runx2 expression in check (Dy 2012)."),
 quantitative=[
  dict(parameter='Limb length reduction with Runx2/Runx3 gene dose',
       value='dose-dependent', unit='qualitative ordering across Runx2/Runx3 allele combinations',
       conditions='E18.5 mouse limbs, Runx2 and Runx3 allelic series', species='mouse',
       source_ref='yoshida2004', uncertainty='no numeric values reported in the abstract; figure values not read',
       value_unverified=True),
 ],
 localization=["mouse PHZ/HZ: confirmed (vega2004, yoshida2004)",
               "human: inferred from cleidocranial dysplasia haploinsufficiency (mundlos1997)"],
 human_evidence='direct',
 human_evidence_note='Human RUNX2 haploinsufficiency causes cleidocranial dysplasia including short stature.',
 species_basis=['human','mouse'], translation_risk='low',
 translation_risk_reason='Concordant human haploinsufficiency and mouse null phenotypes; both affect endochondral and intramembranous bone.',
 confidence='A',
 key_refs=[
  dict(ref_id='mundlos1997', pmid='9182765', first_author='Mundlos S', year=1997, type='primary',
       one_line_finding='CBFA1/RUNX2 mutations cause human cleidocranial dysplasia.'),
  dict(ref_id='yoshida2004', pmid='15107406', first_author='Yoshida CA', year=2004, type='primary',
       one_line_finding='Runx2 and Runx3 are jointly essential for chondrocyte maturation and RUNX2 directly induces Ihh by binding its promoter.'),
  dict(ref_id='vega2004', pmid='15537544', first_author='Vega RB', year=2004, type='primary',
       one_line_finding='HDAC4 binds and inhibits RUNX2 in prehypertrophic chondrocytes.'),
  dict(ref_id='dy2012', pmid='22421045', first_author='Dy P', year=2012, type='primary',
       one_line_finding='SOX9 keeps Runx2 expression in check to prevent premature prehypertrophy and osteoblastic conversion.'),
 ],
 open_questions=['g_l3rest_012'],
))

N.append(dict(
 id='runx3_tf', name='RUNX3', type='protein', aliases=['AML2','CBFA3'],
 summary=(
  "RUNX3 is the RUNX paralogue that shares the hypertrophy-licensing function with RUNX2. Its importance "
  "is invisible in single mutants and appears only in combination: Runx2-null mice still complete "
  "chondrocyte maturation, whereas Runx2;Runx3 double nulls show a complete absence of maturation and "
  "shortened limbs, with the severity tracking total RUNX gene dose (Yoshida 2004, mouse). Runx3 "
  "transcripts rise at the onset of cartilage mineralisation, after Sox9 and concomitant with alkaline "
  "phosphatase, and gain/loss of function in limb-bud-derived chondrogenic cells shows RUNX3 regulates "
  "both early and late maturation markers while transcriptionally inhibiting Runx1 (Soung 2007, mouse "
  "cells). No human RUNX3 skeletal dysplasia is established, and RUNX3 is not a recognised human short "
  "stature gene, so the human contribution of this paralogue is unknown."),
 localization=["mouse PHZ/HZ: RUNX3 protein detected by immunohistochemistry in embryos (soung2007)",
               "human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human RUNX3 skeletal phenotype or growth plate measurement.',
 species_basis=['mouse','in_vitro_animal_cell'], translation_risk='high',
 translation_risk_reason='Mouse compound genetics and mouse cell lines; no human anchor at all.',
 confidence='C',
 key_refs=[
  dict(ref_id='yoshida2004', pmid='15107406', first_author='Yoshida CA', year=2004, type='primary',
       one_line_finding='Runx2;Runx3 double-null mice completely lack chondrocyte maturation; the defect is RUNX gene-dose-dependent.'),
  dict(ref_id='soung2007', pmid='17488194', first_author='Soung do Y', year=2007, type='primary',
       one_line_finding='Runx3 regulates early and late chondrocyte maturation markers and transcriptionally inhibits Runx1.'),
 ],
))

N.append(dict(
 id='mef2c_tf', name='MEF2C', type='protein', aliases=['myocyte enhancer factor 2C'],
 summary=(
  "MEF2C is the MADS-box transcription factor that activates the hypertrophy gene programme. Deleting "
  "Mef2c in endochondral cartilage, or expressing a dominant-negative MEF2C, impairs hypertrophy, "
  "cartilage angiogenesis, ossification and longitudinal bone growth in mouse; a superactivating MEF2C "
  "causes precocious hypertrophy, ossification of the growth plates and dwarfism (Arnold 2007). Both "
  "directions therefore shorten the bone, by opposite mechanisms - failure to hypertrophy and premature "
  "exhaustion of the plate - which is why MEF2C output must be described as a set point rather than as a "
  "'growth-promoting' factor. The set point is enforced by HDAC4: the Mef2c-mutant bone deficiency is "
  "rescued by an Hdac4 mutation, and the ectopic ossification of Hdac4-null mice is reduced by Mef2c "
  "heterozygosity, i.e. the two are titrated against each other in vivo (Arnold 2007, mouse). MEF2C also "
  "acts with residual SOX9 protein to activate Col10a1 directly in upper hypertrophic chondrocytes "
  "(Dy 2012, mouse). Human MEF2C haploinsufficiency (5q14.3 deletion) is a neurodevelopmental syndrome "
  "without a defined physeal phenotype."),
 localization=["mouse PHZ/HZ: functionally required for hypertrophy (arnold2007)","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='Human MEF2C haploinsufficiency presents as a neurodevelopmental disorder; no growth plate read-out is reported.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse conditional and transgenic alleles; the human haploinsufficiency phenotype does not include a described physeal defect.',
 confidence='C',
 key_refs=[
  dict(ref_id='arnold2007', pmid='17336904', first_author='Arnold MA', year=2007, type='primary',
       one_line_finding='MEF2C is required for chondrocyte hypertrophy; superactive MEF2C causes precocious ossification and dwarfism, and MEF2C is titrated against HDAC4 in vivo.'),
  dict(ref_id='dy2012', pmid='22421045', first_author='Dy P', year=2012, type='primary',
       one_line_finding='MEF2C acts with residual SOX9 protein to directly activate Col10a1 in upper hypertrophic chondrocytes.'),
 ],
 open_questions=['g_l3rest_013'],
))

N.append(dict(
 id='hdac4_protein', name='HDAC4', type='protein', aliases=['histone deacetylase 4','class IIa HDAC'],
 summary=(
  "HDAC4 is a class IIa histone deacetylase with negligible intrinsic deacetylase activity that works as a "
  "signal-responsive corepressor. It is expressed in prehypertrophic chondrocytes and restrains hypertrophy "
  "by two routes: binding and inhibiting RUNX2 (Vega 2004) and binding and repressing MEF2 (Arnold 2007; "
  "Nishimori 2019). Hdac4-null mice show ectopic and premature chondrocyte hypertrophy with premature "
  "ossification, phenocopying constitutive RUNX2 expression, while HDAC4 overexpression in proliferating "
  "chondrocytes blocks hypertrophy and phenocopies RUNX2 loss (Vega 2004, mouse). Its activity is set by "
  "SUBCELLULAR LOCALISATION, not by abundance: phosphorylation at 14-3-3-binding sites holds it in the "
  "cytoplasm (inactive), and dephosphorylation lets it enter the nucleus (active as a repressor). PTHrP "
  "drives that dephosphorylation via PP2A (Kozhemyakina 2009) and via inhibition of SIK3 "
  "(Nishimori 2019, 2021). Human HDAC4 haploinsufficiency in 2q37 deletion syndrome causes brachydactyly "
  "type E, present in 48% of 103 reported individuals, plus developmental delay - direct human evidence "
  "that HDAC4 dose sets metacarpal/metatarsal growth plate output (Le 2019); a missense HDAC4 variant "
  "produces the same syndrome in a family (Takeyari 2023)."),
 quantitative=[
  dict(parameter='Brachydactyly type E frequency in 2q37 deletion (HDAC4 haploinsufficiency)',
       value='48', unit='% of individuals', conditions='literature review of 101 published plus 2 new cases (n=103), mixed ages and sexes',
       species='human', source_ref='le2019', uncertainty='no CI reported; ascertainment biased toward clinically diagnosed cases'),
  dict(parameter='Dysmorphic craniofacial features in 2q37 deletion',
       value='86', unit='% of individuals', conditions='same n=103 cohort', species='human',
       source_ref='le2019', uncertainty='no CI reported'),
 ],
 localization=["mouse PHZ: confirmed - HDAC4 expressed in prehypertrophic chondrocytes (vega2004)",
               "human: inferred from 2q37 deletion phenotype (le2019)",
               "human growth plate protein localisation: unconfirmed"],
 human_evidence='direct',
 human_evidence_note='HDAC4 haploinsufficiency in humans (2q37 deletion, and a point mutation in one family) causes brachydactyly type E.',
 species_basis=['mouse','human'], translation_risk='low',
 translation_risk_reason='Human haploinsufficiency produces a growth-plate-attributable digit phenotype concordant with the mouse premature-hypertrophy null.',
 confidence='A',
 key_refs=[
  dict(ref_id='vega2004', pmid='15537544', first_author='Vega RB', year=2004, type='primary',
       one_line_finding='HDAC4 is expressed in prehypertrophic chondrocytes and inhibits RUNX2; Hdac4-null mice show ectopic premature hypertrophy.'),
  dict(ref_id='arnold2007', pmid='17336904', first_author='Arnold MA', year=2007, type='primary',
       one_line_finding='HDAC4 and MEF2C are titrated against each other genetically in endochondral bone formation.'),
  dict(ref_id='kozhemyakina2009', pmid='19704004', first_author='Kozhemyakina E', year=2009, type='primary',
       one_line_finding='PTHrP/forskolin activates a PP2A-dependent HDAC4 phospho-S246 phosphatase, driving HDAC4 into the nucleus to repress MEF2.'),
  dict(ref_id='le2019', pmid='30848064', first_author='Le TN', year=2019, type='primary',
       one_line_finding='In 103 individuals with 2q37 deletion, brachydactyly type E occurs in 48% and HDAC4 is the primary genetic contributor.'),
  dict(ref_id='takeyari2023', pmid='37020696', first_author='Takeyari S', year=2023, type='primary_abstract_only',
       one_line_finding='A missense HDAC4 variant causes brachydactyly-mental retardation syndrome in a family, without a deletion.'),
 ],
 open_questions=['g_l3rest_013'],
))

N.append(dict(
 id='salt_inducible_kinase3', name='SIK3', type='protein', aliases=['salt-inducible kinase 3','SIK3 kinase'],
 summary=(
  "SIK3 is an AMPK-family kinase that sits directly above HDAC4 and controls where HDAC4 is. SIK3 "
  "phosphorylates HDAC4 at its 14-3-3-binding sites, anchoring HDAC4 in the cytoplasm and thereby "
  "releasing MEF2C to drive hypertrophy. Sik3-null mice are normal-sized as embryos and become dwarfed "
  "with age; hypertrophy is markedly delayed from E14.5 and blocked until E18.5, growth plates and "
  "articular cartilage are expanded, chondrocytes accumulate in sternum, ribs and spine, and HDAC4 remains "
  "NUCLEAR in Sik3-null chondrocytes where it is cytoplasmic in wild-type hypertrophic cells "
  "(Sasagawa 2012). The converse is also shown: chondrocyte-specific SIK3 overexpression closes growth "
  "plates in adult mice. PTHrP acts through this kinase: PTHrP-cAMP-PKA phosphorylates the PKA sites on "
  "SIK3, inhibiting SIK3 kinase activity, so HDAC4 loses its cytoplasmic anchor, enters the nucleus and "
  "blocks MEF2 and RUNX2 (Nishimori 2021, mouse). SIK1 and SIK2 substitute when SIK3 activity is low, and "
  "HDAC5 substitutes when HDAC4 is low, so the cascade is doubly redundant. No human SIK3 skeletal "
  "phenotype is established; human SIK3 variants are known for the short-sleep trait."),
 localization=["mouse PHZ/HZ: SIK3 protein detected in cytoplasm of prehypertrophic and hypertrophic chondrocytes (sasagawa2012)",
               "human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human SIK3 skeletal phenotype; human SIK3 variants are associated with sleep duration, not stature.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse germline knockout and transgenic overexpression; the human orthologue has no described physeal role.',
 confidence='C',
 key_refs=[
  dict(ref_id='sasagawa2012', pmid='22318228', first_author='Sasagawa S', year=2012, type='primary',
       one_line_finding='SIK3 anchors HDAC4 in the cytoplasm; Sik3-null mice have blocked hypertrophy and nuclear HDAC4, and SIK3 overexpression closes growth plates.'),
  dict(ref_id='nishimori2021', pmid='33148508', first_author='Nishimori S', year=2021, type='primary',
       one_line_finding='PTHrP/cAMP/PKA phosphorylates and inhibits SIK3, lowering HDAC4 phosphorylation and allowing nuclear HDAC4 to block MEF2 and RUNX2.'),
  dict(ref_id='nishimori2019', pmid='30843886', first_author='Nishimori S', year=2019, type='primary',
       one_line_finding='HDAC4 is required for PTHrP effects on chondrocyte differentiation in vivo, with HDAC5 as a partially redundant mediator.'),
 ],
 open_questions=['g_l3rest_013'],
))

N.append(dict(
 id='foxa_family_chondrocyte', name='FOXA family in chondrocytes (FOXA2/FOXA3)', type='protein',
 aliases=['FoxA2','FoxA3','forkhead box A'],
 summary=(
  "FOXA factors are pioneer transcription factors induced during chondrogenesis that bind conserved sites "
  "in the collagen X enhancer and can drive a Col10a1 reporter in both chondrocytes and fibroblasts, i.e. "
  "they carry hypertrophy competence into a non-cartilage cell (Ionescu 2012). Mice lacking both FoxA2 and "
  "FoxA3 in chondrocytes have defective hypertrophy, reduced alkaline phosphatase and impaired sternebral "
  "mineralisation, and become postnatally dwarfed with significantly reduced collagen X and MMP13 in the "
  "growth plate; single mutants are unremarkable, so this is another redundant pair (Ionescu 2012, mouse). "
  "FOXA2 is separately of interest because a FoxA2-marked resting-zone population has been proposed in L2, "
  "which raises the unresolved question of whether the same factor acts at both ends of the differentiation "
  "trajectory. There is no human FOXA2/FOXA3 skeletal phenotype and no human growth plate FOXA measurement."),
 localization=["mouse PHZ/HZ: functionally required for the hypertrophic programme (ionescu2012)",
               "human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human FOXA2/FOXA3 skeletal phenotype or growth plate data.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse compound conditional knockouts and reporter assays only.',
 confidence='C',
 key_refs=[
  dict(ref_id='ionescu2012', pmid='22595668', first_author='Ionescu A', year=2012, type='primary',
       one_line_finding='FoxA2/FoxA3 double-mutant chondrocytes fail to hypertrophy and the mice are postnatally dwarfed with reduced Col10a1 and Mmp13.'),
 ],
))

N.append(dict(
 id='zfp521_protein', name='ZFP521 (ZNF521)', type='protein', aliases=['Zfp521','ZNF521','EHZF'],
 summary=(
  "ZFP521 is a zinc-finger transcriptional coregulator that PTHrP induces in prehypertrophic chondrocytes "
  "and that executes part of the PTHrP anti-hypertrophy programme. Chondrocyte-targeted Zfp521 deletion in "
  "mouse phenocopies PTHrP-null and chondrocyte PTH1R-null animals: reduced proliferation, early "
  "hypertrophic transition and a thinner growth plate. Mechanistically ZFP521 associates with RUNX2 and "
  "antagonises it by an HDAC4-dependent mechanism; without ZFP521, Runx2 and its target genes rise while "
  "cyclin D1 and BCL2 fall and caspase-3 activation and apoptosis increase, and PTHrP can no longer "
  "upregulate cyclin D1 or suppress Runx2, Ihh and Col10a1 (Correa 2010, mouse). ZFP521 therefore sits in "
  "the same RUNX2-restraining module as HDAC4 and provides an independent route by which PTHrP holds the "
  "hypertrophy switch off. No human ZNF521 skeletal phenotype has been established and there is no human "
  "growth plate measurement."),
 localization=["mouse PHZ: induced by PTHrP in prehypertrophic chondrocytes (correa2010)","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human ZNF521 skeletal phenotype or growth plate data.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Single-laboratory mouse conditional knockout with no human correlate.',
 confidence='C',
 key_refs=[
  dict(ref_id='correa2010', pmid='20951345', first_author='Correa D', year=2010, type='primary',
       one_line_finding='Zfp521 is a PTHrP target that antagonises RUNX2 via an HDAC4-dependent mechanism; its deletion phenocopies PTHrP loss in mouse.'),
 ],
))

for n in N: w(n)
print(len(N), 'nodes')
