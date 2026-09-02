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
 id='wnt_canonical_chondrocyte', name='Canonical WNT/beta-catenin signalling in chondrocytes', type='pathway',
 aliases=['Wnt/beta-catenin pathway, growth plate'],
 summary=(
  "Canonical WNT signalling stabilises beta-catenin, which enters the nucleus and converts TCF/LEF from "
  "repressors into activators. In cartilage the pathway is dose-dependent with opposite phenotypes at the "
  "two extremes, and this is established by paired gain- and loss-of-function alleles in the same mouse "
  "genetic background. Too little: Col2a1-Cre inactivation of Ctnnb1 gives dwarfism with reduced "
  "chondrocyte proliferation and delayed hypertrophic differentiation (Akiyama 2004), and Col2a1-ICAT "
  "transgenic mice - normal size at birth, then progressively runted - have narrower proliferative and "
  "hypertrophic zones, more apoptosis and delayed secondary ossification centre formation (Chen 2008). "
  "Too much: chondrocyte-restricted beta-catenin stabilisation causes severe chondrodysplasia "
  "phenocopying Sox9 inactivation (Akiyama 2004), tamoxifen-induced stabilisation accelerates maturation "
  "and drives ectopic ossification centres (Dao 2012), and transient activation in young adult mice causes "
  "growth retardation with premature growth plate closure and articular cartilage thickening (Yuasa 2009). "
  "At the progenitor stage the sign flips again: beta-catenin is required for osteoblast fate, and "
  "osteoblast precursors lacking it become chondrocytes instead (Hill 2005, Day 2005). No dose-response "
  "curve has been measured in human chondrocytes."),
 localization=[
  "mouse PHZ/HZ: highest canonical activity inferred from reporter and genetic studies (dao2012, guo2009)",
  "mouse PZ: lower activity; loss-of-function reduces proliferation (akiyama2004, chen2008)",
  "human growth plate: unconfirmed - no zonal nuclear beta-catenin or TCF-reporter data"],
 human_evidence='indirect',
 human_evidence_note=("Human evidence is confined to WNT co-receptor genetics (LRP5 OPPG and high-bone-mass alleles) "
  "and SOST; no human growth plate has been assayed for canonical WNT activity."),
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason=("Every dose statement comes from mouse conditional alleles; the human physiological range of "
  "chondrocyte beta-catenin activity is unknown, and mice do not undergo epiphyseal fusion."),
 confidence='C',
 key_refs=[
  dict(ref_id='akiyama2004', pmid='15132997', first_author='Akiyama H', year=2004, type='primary',
       one_line_finding='beta-catenin inactivation and Sox9 overexpression give the same dwarfism; beta-catenin stabilisation and Sox9 loss give the same chondrodysplasia.'),
  dict(ref_id='chen2008', pmid='18397998', first_author='Chen M', year=2008, type='primary',
       one_line_finding='Col2a1-ICAT mice (reduced chondrocyte beta-catenin) are progressively runted with narrowed PZ and HZ and delayed SOC.'),
  dict(ref_id='dao2012', pmid='22508079', first_author='Dao DY', year=2012, type='primary',
       one_line_finding='Inducible cartilage-specific beta-catenin gain of function promotes maturation and primary/secondary ossification centre formation.'),
  dict(ref_id='yuasa2009', pmid='19815716', first_author='Yuasa T', year=2009, type='primary',
       one_line_finding='Transient Wnt/beta-catenin activation in young adult mouse cartilage causes growth retardation and abnormal growth plate closure.'),
  dict(ref_id='guo2009', pmid='19557172', first_author='Guo X', year=2009, type='primary',
       one_line_finding='Wnt/beta-catenin initiates hypertrophy by inhibiting PTHrP signalling activity, and controls final maturation PTHrP-independently.'),
  dict(ref_id='hill2005', pmid='15866163', first_author='Hill TP', year=2005, type='primary',
       one_line_finding='Osteoblast precursors lacking beta-catenin become chondrocytes, so high canonical WNT blocks chondrogenesis at the progenitor stage.'),
 ],
 open_questions=['g_l3rest_005','g_l3rest_006'],
))

N.append(dict(
 id='beta_catenin_ctnnb1', name='beta-catenin (CTNNB1)', type='protein', aliases=['CTNNB1'],
 summary=(
  "beta-catenin is the transducer whose cytoplasmic pool is destroyed by the APC/AXIN/GSK3B destruction "
  "complex unless WNT-receptor engagement inhibits it. In chondrocytes its level is read as a dose, not a "
  "switch. Deleting it in committed growth plate chondrocytes lowers proliferation and delays hypertrophy; "
  "stabilising it accelerates hypertrophy and, if raised further or earlier, blocks chondrogenesis "
  "altogether (Akiyama 2004; Dao 2012, mouse). Deleting it only from Col10a1-expressing hypertrophic "
  "chondrocytes leaves hypertrophic zone height normal but reduces Mmp13 and Vegfa and produces less "
  "trabecular bone, showing a distinct late requirement in the terminal cell (Golovchenko 2013, mouse). "
  "beta-catenin and SOX9 are mutually antagonistic: SOX9 binds beta-catenin through its C-terminal "
  "transactivation domain, blocks TCF/LEF-dependent transcription and promotes beta-catenin degradation "
  "(Akiyama 2004), and SOX9 promotes nuclear phosphorylation of beta-catenin to speed its turnover "
  "(Topol 2009). This reciprocal inhibition is the single most important convergence in the layer: the "
  "same molecular ratio sets both chondrocyte identity and the hypertrophy decision."),
 localization=[
  "mouse HZ: functionally required for Mmp13/Vegfa expression in Col10a1+ cells (golovchenko2013)",
  "mouse PZ/PHZ: functionally required for normal proliferation and hypertrophy timing (akiyama2004, chen2008)",
  "human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human growth plate beta-catenin localisation or perturbation data; human CTNNB1 variants cause neurodevelopmental disease, not a defined physeal phenotype.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='All causal data are mouse conditional alleles; the human dose-response is unmeasured.',
 confidence='C',
 key_refs=[
  dict(ref_id='akiyama2004', pmid='15132997', first_author='Akiyama H', year=2004, type='primary',
       one_line_finding='SOX9 binds beta-catenin via its C-terminal transactivation domain, inhibits TCF/LEF transcription and promotes beta-catenin degradation.'),
  dict(ref_id='topol2009', pmid='19047045', first_author='Topol L', year=2009, type='primary',
       one_line_finding='SOX9 inhibits WNT signalling by promoting phosphorylation of beta-catenin in the nucleus.'),
  dict(ref_id='golovchenko2013', pmid='23567158', first_author='Golovchenko S', year=2013, type='primary_abstract_only',
       one_line_finding='Deleting beta-catenin only in Col10a1+ hypertrophic chondrocytes lowers Mmp13/Vegfa and reduces trabecular bone without changing HZ size.'),
  dict(ref_id='dao2012', pmid='22508079', first_author='Dao DY', year=2012, type='primary',
       one_line_finding='Cartilage-specific beta-catenin gain of function accelerates maturation and ossification centre formation.'),
 ],
 open_questions=['g_l3rest_005'],
 contradicts=['sox9_tf'],
))

N.append(dict(
 id='gsk3b_kinase', name='GSK3B', type='protein', aliases=['glycogen synthase kinase 3 beta','GSK-3beta'],
 summary=(
  "GSK3B is the destruction-complex kinase that phosphorylates beta-catenin on the N-terminal degron and "
  "targets it for beta-TrCP-mediated degradation; WNT-receptor engagement inhibits this activity and lets "
  "beta-catenin accumulate. In chondrocytes, pharmacological GSK3 inhibition with lithium chloride "
  "raises beta-catenin and drives terminal differentiation markers together with oxidative DNA damage and "
  "matrix remodelling in human OA chondrocytes in vitro (Guidotti 2015), which is a chemical-genetics "
  "mirror of the beta-catenin gain-of-function mouse phenotype. GSK3B is not chondrocyte-specific and sits "
  "downstream of many inputs, so any perturbation of it is a blunt instrument: it also regulates "
  "glycogen metabolism, mTOR-adjacent signalling and microtubule dynamics in the same cell. No "
  "chondrocyte-restricted Gsk3b conditional knockout growth plate phenotype has been reported that "
  "separates its WNT role from these other functions, and no human growth plate GSK3B measurement exists."),
 localization=["in_vitro_human_cell (OA chondrocytes): activity manipulated pharmacologically (guidotti2015)",
               "human growth plate: unconfirmed","mouse growth plate zonal distribution: unconfirmed"],
 human_evidence='indirect',
 human_evidence_note='Human evidence is in vitro pharmacology on cultured human articular chondrocytes, not growth plate tissue.',
 species_basis=['in_vitro_human_cell'], translation_risk='high',
 translation_risk_reason='Lithium is a promiscuous inhibitor, the cells were articular and diseased, and no in vivo physeal genetics exist.',
 confidence='D',
 key_refs=[
  dict(ref_id='guidotti2015', pmid='26618897', first_author='Guidotti S', year=2015, type='primary',
       one_line_finding='LiCl-dependent GSK3 inactivation in human chondrocytes links oxidative DNA damage to matrix remodelling and terminal differentiation.'),
  dict(ref_id='akiyama2004', pmid='15132997', first_author='Akiyama H', year=2004, type='primary',
       one_line_finding='Establishes that the level of beta-catenin - the GSK3B substrate - is what chondrocytes read.'),
 ],
 open_questions=['g_l3rest_005'],
))

N.append(dict(
 id='lrp5_coreceptor', name='LRP5', type='protein', aliases=['low-density lipoprotein receptor-related protein 5'],
 summary=(
  "LRP5 is a single-pass WNT co-receptor that, with Frizzled, is required for canonical signal "
  "transduction. Human genetics supplies a rare two-sided dose experiment on one gene: biallelic "
  "loss-of-function causes osteoporosis-pseudoglioma syndrome with very low bone mass and fractures "
  "(Gong 2001), while the heterozygous G171V missense allele, which impairs binding of the antagonist "
  "DKK1, causes autosomal dominant high bone mass (Boyden 2002). Both phenotypes are dominated by bone "
  "mass rather than by stature, which is the important negative for this atlas: the human LRP5 read-out "
  "is osteoblastic, not clearly physeal. In mouse, Lrp5 and Lrp6 act redundantly in the embryo, and only "
  "the compound mutants reveal the full skeletal requirement (Joeng 2011). Whether LRP5 signalling in the "
  "growth plate chondrocyte itself contributes to human height has not been tested."),
 localization=["human bone: inferred from OPPG and HBM phenotypes (gong2001, boyden2002)",
               "human growth plate chondrocyte: unconfirmed"],
 human_evidence='direct',
 human_evidence_note='Two independent human germline allele classes (null and DKK1-resistant missense) give opposite bone-mass phenotypes.',
 species_basis=['human','mouse'], translation_risk='low',
 translation_risk_reason='Human loss- and gain-of-function alleles are both characterised; the caveat is that the read-out is bone mass, not longitudinal growth.',
 confidence='A',
 key_refs=[
  dict(ref_id='gong2001', pmid='11719191', first_author='Gong Y', year=2001, type='primary',
       one_line_finding='LRP5 loss of function causes human osteoporosis-pseudoglioma syndrome.'),
  dict(ref_id='boyden2002', pmid='12015390', first_author='Boyden LM', year=2002, type='primary',
       one_line_finding='The LRP5 G171V allele causes autosomal dominant human high bone mass.'),
  dict(ref_id='joeng2011', pmid='21924256', first_author='Joeng KS', year=2011, type='primary',
       one_line_finding='Lrp5 and Lrp6 act redundantly to control mouse embryonic skeletal development.'),
 ],
))

N.append(dict(
 id='lrp6_coreceptor', name='LRP6', type='protein', aliases=['low-density lipoprotein receptor-related protein 6'],
 summary=(
  "LRP6 is the paralogue of LRP5 and the dominant WNT co-receptor during mouse embryogenesis. Joeng 2011 "
  "shows that Lrp5 and Lrp6 are redundant in the embryonic skeleton: Lrp6 loss produces a markedly more "
  "severe skeletal phenotype than Lrp5 loss, and reducing Lrp5 dose on an Lrp6 mutant background worsens "
  "it further, so the two receptors provide a summed rather than a divided input. This gene-dose "
  "structure is the reason single-receptor knockouts underestimate the requirement for canonical WNT in "
  "cartilage and bone. Human LRP6 variants have been associated with low bone mass and with coronary "
  "disease, but there is no LRP6 skeletal dysplasia with a defined growth plate phenotype and no human "
  "physeal measurement."),
 localization=["mouse embryonic skeleton: functionally required (joeng2011)","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human LRP6 growth plate phenotype; associations are with bone mass and cardiovascular traits.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse embryonic genetics only; human LRP6 skeletal data are association-level.',
 confidence='C',
 key_refs=[
  dict(ref_id='joeng2011', pmid='21924256', first_author='Joeng KS', year=2011, type='primary',
       one_line_finding='Lrp5 and Lrp6 redundantly control mouse embryonic skeletal development, with Lrp6 the more important of the two.'),
 ],
))

N.append(dict(
 id='sclerostin_sost', name='Sclerostin (SOST)', type='protein', aliases=['SOST'],
 summary=(
  "Sclerostin is a secreted WNT antagonist that binds LRP5/LRP6 and blocks canonical signalling. Human "
  "loss of function is definitive and bidirectional in effect: SOST-null sclerosteosis produces massive "
  "bone overgrowth with gigantism-adjacent features including tall stature and cranial nerve compression "
  "(Balemans 2001), which is one of the very few human WNT-pathway phenotypes that includes increased "
  "linear growth rather than only increased bone mass. In normal human bone, sclerostin protein is a "
  "delayed product of embedded osteocytes and is not detectable in early osteoblasts, so it acts as a "
  "late, spatially restricted brake (Poole 2005). The critical unresolved point for this atlas is whether "
  "sclerostin reaches the growth plate chondrocyte at all: SOST expression in growth plate cartilage has "
  "not been demonstrated, and the tall stature of sclerosteosis could be an indirect consequence of "
  "cortical and endosteal overgrowth. The therapeutic antibody romosozumab is licensed in adults only, so "
  "no paediatric physeal read-out exists."),
 localization=["human osteocyte: confirmed by immunohistochemistry (poole2005)",
               "human growth plate chondrocyte: unconfirmed - not demonstrated","mouse growth plate: unconfirmed"],
 human_evidence='direct',
 human_evidence_note='SOST null (sclerosteosis) is a human loss-of-function phenotype including increased stature; osteocyte localisation is shown in human bone.',
 species_basis=['human'], translation_risk='low',
 translation_risk_reason='Primary evidence is human germline and human histology; the risk is mechanistic (site of action), not species.',
 confidence='B',
 key_refs=[
  dict(ref_id='balemans2001', pmid='11181578', first_author='Balemans W', year=2001, type='primary',
       one_line_finding='Sclerosteosis is caused by deficiency of the secreted protein SOST.'),
  dict(ref_id='poole2005', pmid='16123173', first_author='Poole KE', year=2005, type='primary',
       one_line_finding='Sclerostin is a delayed secreted product of embedded osteocytes that inhibits bone formation.'),
 ],
 open_questions=['g_l3rest_007'],
))

N.append(dict(
 id='dkk1_antagonist', name='DKK1', type='protein', aliases=['Dickkopf-1'],
 summary=(
  "DKK1 is a secreted antagonist that binds LRP5/LRP6 (with Kremen) and removes them from the receptor "
  "complex, shutting down canonical WNT. Transgenic overexpression of Dkk1 in mouse bone causes osteopenia "
  "with reduced osteoblast number, and Dkk1 heterozygous-null mice have increased bone mass, giving a "
  "clean in vivo dose relation for the bone compartment (Li 2006). The human LRP5 G171V high-bone-mass "
  "allele acts by resisting DKK1 binding, which is independent human evidence that DKK1 tone is "
  "physiologically load-bearing (Boyden 2002). What is missing is the physeal half: no report establishes "
  "DKK1 protein in the human or mouse growth plate by zone, and no chondrocyte-restricted Dkk1 deletion "
  "growth plate phenotype has been published. DKK1 is thus a well-evidenced bone node and an assumed "
  "cartilage node."),
 localization=["mouse bone: confirmed by transgenic and heterozygous-null phenotypes (li2006)",
               "growth plate zonal distribution: unconfirmed in mouse and human"],
 human_evidence='indirect',
 human_evidence_note='Human evidence is the DKK1-resistant LRP5 allele; there is no direct human DKK1 growth plate measurement.',
 species_basis=['mouse','human'], translation_risk='moderate',
 translation_risk_reason='Mouse transgenics for the mechanism; the human inference is via a receptor allele, not via DKK1 itself.',
 confidence='C',
 key_refs=[
  dict(ref_id='li2006', pmid='16730481', first_author='Li J', year=2006, type='primary',
       one_line_finding='Dkk1 overexpression causes mouse osteopenia and Dkk1 heterozygosity increases bone mass.'),
  dict(ref_id='boyden2002', pmid='12015390', first_author='Boyden LM', year=2002, type='primary',
       one_line_finding='The human high-bone-mass LRP5 allele resists DKK1 inhibition.'),
 ],
 open_questions=['g_l3rest_007'],
))

N.append(dict(
 id='wnt_noncanonical_pcp', name='Non-canonical WNT / planar cell polarity in the growth plate', type='pathway',
 aliases=['WNT-PCP','planar cell polarity, chondrocyte'],
 summary=(
  "Column formation requires that daughter chondrocytes rotate and intercalate into a single file aligned "
  "with the long axis; this is a planar-cell-polarity process, not a proliferation process. In mouse, "
  "non-canonical Frizzled signalling controls chondrocyte polarity: manipulating Fzd/Wnt5a signalling "
  "disrupts the stereotyped rotation that follows division and produces disorganised, non-columnar clones "
  "without necessarily changing proliferation rate (Li and Dudley 2009). WNT5A acts as a graded cue: it "
  "induces ROR2-dependent phosphorylation of VANGL2, and the level of VANGL2 phosphorylation encodes the "
  "position of a cell within a WNT5A gradient, converting a diffusible signal into a vector (Gao 2011, "
  "mouse). Wnt5a and Wnt5b have distinct, non-interchangeable effects on the proliferation-to-hypertrophy "
  "transition (Yang 2003, mouse). This subsystem explains the columnar architecture that L1 describes, and "
  "it is the arm of WNT signalling least studied in human tissue - no human growth plate has been assayed "
  "for PCP protein asymmetry."),
 localization=["mouse PZ: confirmed - polarity and rotation defects on Fzd/Wnt5a perturbation (li2009)",
               "human PZ: unconfirmed - no PCP protein asymmetry data in human growth plate"],
 human_evidence='indirect',
 human_evidence_note='Human WNT5A and ROR2 mutations cause Robinow syndrome with limb shortening, but no human growth plate PCP measurement exists.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse genetics and explant imaging; the human columnar organisation is described morphologically but never mechanistically.',
 confidence='C',
 key_refs=[
  dict(ref_id='li2009', pmid='19224985', first_author='Li Y', year=2009, type='primary',
       one_line_finding='Non-canonical Frizzled signalling controls the post-mitotic rotation that builds chondrocyte columns in mouse.'),
  dict(ref_id='gao2011', pmid='21316585', first_author='Gao B', year=2011, type='primary',
       one_line_finding='A WNT5A gradient induces graded ROR2-dependent VANGL2 phosphorylation, converting concentration into polarity.'),
  dict(ref_id='yang2003', pmid='12538525', first_author='Yang Y', year=2003, type='primary',
       one_line_finding='Wnt5a and Wnt5b have distinct activities in coordinating chondrocyte proliferation and differentiation.'),
 ],
 open_questions=['g_l3rest_008'],
))

N.append(dict(
 id='wnt5a_ligand', name='WNT5A', type='protein',
 summary=(
  "WNT5A is the principal non-canonical WNT ligand of the growth plate. In mouse it is expressed in a "
  "graded fashion across developing limb elements and acts through ROR2 to phosphorylate VANGL2, with the "
  "degree of phosphorylation reporting position in the gradient (Gao 2011). Functionally, Wnt5a and its "
  "paralogue Wnt5b have opposite effects on where the proliferative-to-hypertrophic transition occurs: "
  "Wnt5a delays and Wnt5b promotes the transition in mouse, so they are not interchangeable despite high "
  "sequence similarity (Yang 2003). In human, dominant and recessive WNT5A mutations cause Robinow "
  "syndrome, whose cardinal skeletal feature is mesomelic limb shortening with normal-length axial "
  "skeleton - a segment-selective growth failure consistent with a positional rather than a "
  "rate-limiting role. No human growth plate WNT5A protein gradient has been measured."),
 localization=["mouse limb mesenchyme, graded: confirmed (gao2011)","mouse growth plate: reported (yang2003)",
               "human growth plate: unconfirmed"],
 human_evidence='indirect',
 human_evidence_note='WNT5A mutations cause human Robinow syndrome with mesomelic shortening; no human growth plate expression or gradient data.',
 species_basis=['mouse','human'], translation_risk='moderate',
 translation_risk_reason='Mechanism is mouse; the human phenotype is developmental patterning and cannot be assigned to a growth plate zone.',
 confidence='C',
 key_refs=[
  dict(ref_id='gao2011', pmid='21316585', first_author='Gao B', year=2011, type='primary',
       one_line_finding='WNT5A gradients establish planar cell polarity by inducing ROR2-dependent VANGL2 phosphorylation.'),
  dict(ref_id='yang2003', pmid='12538525', first_author='Yang Y', year=2003, type='primary',
       one_line_finding='Wnt5a and Wnt5b exert distinct and partly opposing effects on the chondrocyte hypertrophy transition.'),
 ],
 open_questions=['g_l3rest_008'],
))

N.append(dict(
 id='vangl2_pcp', name='VANGL2', type='protein', aliases=['Van Gogh-like 2','Loop-tail'],
 summary=(
  "VANGL2 is a four-pass transmembrane core PCP protein that becomes asymmetrically localised across a "
  "polarised cell. In the limb, WNT5A signalling through ROR2 phosphorylates VANGL2 at conserved "
  "N-terminal serine/threonine residues, and the amount of phosphorylation is proportional to WNT5A "
  "concentration; the Looptail (Vangl2 Lp) allele is phosphorylation-deficient and acts as a dominant "
  "negative (Gao 2011, mouse). This makes VANGL2 the molecular ruler that converts a diffusible WNT5A "
  "gradient into a directional instruction for chondrocyte stacking. Direct growth-plate-restricted "
  "conditional Vangl2 genetics with a columnar-organisation read-out are sparse, and no human VANGL2 "
  "skeletal dysplasia is established (human VANGL2 variants are associated with neural tube defects). "
  "This node is therefore mechanistically strong in mouse limb and empty in human physis."),
 localization=["mouse limb mesenchyme: confirmed, phosphorylation graded along the WNT5A axis (gao2011)",
               "human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='Human VANGL2 variants are linked to neural tube defects, not to a growth plate phenotype.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse limb genetics only; no human skeletal phenotype anchors the node.',
 confidence='C',
 key_refs=[
  dict(ref_id='gao2011', pmid='21316585', first_author='Gao B', year=2011, type='primary',
       one_line_finding='Graded ROR2-dependent VANGL2 phosphorylation encodes position within a WNT5A gradient in the mouse limb.'),
  dict(ref_id='li2009', pmid='19224985', first_author='Li Y', year=2009, type='primary',
       one_line_finding='Non-canonical Frizzled signalling, the pathway VANGL2 serves, controls chondrocyte column formation.'),
 ],
 open_questions=['g_l3rest_008'],
))

for n in N: w(n)
print(len(N), 'nodes')
