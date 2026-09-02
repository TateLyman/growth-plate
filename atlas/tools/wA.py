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

NODES = []

NODES.append(dict(
 id='bmp_signaling_growth_plate', name='BMP signalling in the growth plate', type='pathway',
 aliases=['bone morphogenetic protein signalling, chondrocyte'],
 summary=(
  "BMP ligands act on chondrocytes through the type I receptors BMPR1A and BMPR1B, which phosphorylate "
  "SMAD1/5/8; Bmpr1a;Bmpr1b double-null mouse limbs form only condensations and generate essentially no "
  "cartilage, while either single null is comparatively mild, establishing receptor redundancy (Yoon 2005, "
  "mouse). Downstream, chondrocyte-restricted loss of Smad1 plus Smad5 in mouse reproduces a severe "
  "chondrodysplasia with a disorganised, thinned proliferative zone, whereas Smad8 is dispensable "
  "(Retting 2009). In mouse limb explant culture BMP2 raises the proliferation rate of columnar "
  "chondrocytes and delays the onset of hypertrophy, and it does so in part by raising Ihh expression - "
  "yet BMP still increases proliferation in explants where Ihh signalling is blocked, so the BMP and "
  "Ihh/PTHrP arms are parallel rather than strictly serial (Minina 2001, mouse). BMP signalling and FGFR3 "
  "signalling are antagonistic on both proliferation and the hypertrophy decision in the same explant "
  "system (Minina 2002, mouse). The pathway is dose-limited in vivo by the secreted antagonists Noggin and "
  "Chordin and by intracellular SMAD7. Human evidence is genetic and indirect: NOG, GDF5, BMPR1B and "
  "LTBP3 variants cause recognisable skeletal phenotypes, but no human growth plate has been assayed for "
  "zonal pSMAD1/5/8 activity."),
 localization=[
  "mouse PZ: confirmed - Bmp2/Bmp6 expression and pSmad1/5/8 activity reported in proliferating and prehypertrophic chondrocytes (minina2001, retting2009)",
  "mouse PERI: confirmed - Bmp2/Bmp4/Bmp7 expressed in perichondrium (bandyopadhyay2006)",
  "human growth plate: unconfirmed - no zonal pSMAD1/5/8 immunostaining series published"],
 human_evidence='indirect',
 human_evidence_note=("Human evidence is entirely genetic (NOG symphalangism, GDF5/CDMP1 chondrodysplasia, "
  "LTBP3 brachyolmia); no direct measurement of BMP pathway activity in human growth plate tissue."),
 species_basis=['mouse','human'], translation_risk='moderate',
 translation_risk_reason=("Receptor and SMAD genetics are mouse-only; the human read-out is dysmorphology from "
  "germline variants, which cannot separate growth-plate-autonomous from patterning effects."),
 confidence='B',
 key_refs=[
  dict(ref_id='yoon2005', pmid='15781876', first_author='Yoon BS', year=2005, type='primary',
       one_line_finding='Bmpr1a/Bmpr1b double conditional-null mouse limbs fail to form cartilage; single nulls are mild.'),
  dict(ref_id='retting2009', pmid='19224984', first_author='Retting KN', year=2009, type='primary',
       one_line_finding='Chondrocyte Smad1/Smad5 double deletion causes severe chondrodysplasia; Smad8 loss adds nothing.'),
  dict(ref_id='minina2001', pmid='11714677', first_author='Minina E', year=2001, type='primary',
       one_line_finding='BMP2 in mouse limb explants increases chondrocyte proliferation and delays hypertrophy, partly Ihh-independent.'),
  dict(ref_id='minina2002', pmid='12361605', first_author='Minina E', year=2002, type='primary',
       one_line_finding='BMP and FGF signalling act antagonistically on proliferation and on the hypertrophy decision in the same explants.'),
 ],
 open_questions=['g_l3rest_001'],
))

NODES.append(dict(
 id='bmp2_ligand', name='BMP2', type='protein', aliases=['bone morphogenetic protein 2'],
 summary=(
  "BMP2 is expressed in mouse perichondrium and in prehypertrophic/hypertrophic chondrocytes. Chondrocyte-"
  "restricted Bmp2 deletion (Col2-Cre) in mouse shortens long bones, reduces chondrocyte proliferation and "
  "delays hypertrophic maturation, whereas the equivalent Bmp4 deletion produces a much weaker phenotype, "
  "so within cartilage BMP2 is the non-redundant member of the pair (Shu 2011). Germline analysis of the "
  "limb bud shows Bmp2 and Bmp7 are individually dispensable for skeletal element formation but Bmp2;Bmp4 "
  "double loss in limb mesenchyme blocks skeletogenesis, i.e. redundancy is compartment-specific "
  "(Bandyopadhyay 2006, mouse). BMP2 is also the ligand through which chondrocyte beta-catenin appears to "
  "act on maturation: Col2CreERT2-driven beta-catenin stabilisation raises Bmp2 in cartilage (Dao 2012, "
  "mouse), and VEGF induction in chondrocytes requires BMP2 and beta-catenin signalling together (Chen "
  "2008, mouse). No human BMP2 loss-of-function short-stature syndrome is established from growth plate "
  "material."),
 localization=[
  "mouse PERI: confirmed by in situ hybridisation (bandyopadhyay2006)",
  "mouse PHZ/HZ: confirmed by in situ hybridisation (shu2011)",
  "human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human growth plate localisation or interventional data for BMP2 in longitudinal growth.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='All causal data are mouse conditional knockouts; recombinant BMP2 human use is in fusion/nonunion, not physis.',
 confidence='C',
 key_refs=[
  dict(ref_id='shu2011', pmid='21984813', first_author='Shu B', year=2011, type='primary',
       one_line_finding='Cartilage-specific Bmp2 but not Bmp4 deletion impairs chondrocyte proliferation and maturation in mouse.'),
  dict(ref_id='bandyopadhyay2006', pmid='17194222', first_author='Bandyopadhyay A', year=2006, type='primary',
       one_line_finding='Bmp2 and Bmp4 are redundantly required in limb mesenchyme for skeletogenesis; Bmp7 is dispensable.'),
  dict(ref_id='dao2012', pmid='22508079', first_author='Dao DY', year=2012, type='primary',
       one_line_finding='Cartilage beta-catenin gain-of-function raises Bmp2 and accelerates chondrocyte maturation in mouse.'),
 ],
 open_questions=['g_l3rest_001'],
))

NODES.append(dict(
 id='bmp6_ligand', name='BMP6', type='protein', aliases=['bone morphogenetic protein 6'],
 summary=(
  "BMP6 is expressed by hypertrophic chondrocytes in the mouse growth plate. Germline Bmp6-null mice are "
  "viable and modestly affected: Perry 2008 reports delayed ossification and altered growth plate "
  "architecture with reduced hypertrophic zone function rather than gross dwarfism, consistent with heavy "
  "redundancy inside the BMP family. BMP6 is the ligand most cleanly linked to systemic iron handling "
  "(hepcidin), so any growth phenotype in Bmp6 mutants must be interpreted against a possible iron-status "
  "confounder, which the skeletal literature has not controlled. There is no human BMP6 skeletal "
  "dysplasia. This node is retained as a component of the BMP ligand inventory rather than as an "
  "established control point of human longitudinal growth."),
 localization=["mouse HZ: reported (perry2008)", "human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human BMP6 growth-plate data and no BMP6-linked human short stature syndrome.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Single mouse germline knockout with a mild phenotype; no human correlate.',
 confidence='D',
 key_refs=[
  dict(ref_id='perry2008', pmid='17980691', first_author='Perry MJ', year=2008, type='primary_abstract_only',
       one_line_finding='Bmp6-null mice show impaired growth plate function with delayed hypertrophic differentiation.'),
 ],
 open_questions=['g_l3rest_001'],
))

NODES.append(dict(
 id='bmp7_ligand', name='BMP7', type='protein', aliases=['bone morphogenetic protein 7','OP-1'],
 summary=(
  "BMP7 is expressed in mouse perichondrium and, unlike BMP2/BMP4, is individually dispensable for limb "
  "skeletal element formation: Bmp7-null limb buds pattern and ossify essentially normally, and removing "
  "Bmp7 on top of Bmp2/Bmp4 loss does not add a distinguishable limb phenotype (Bandyopadhyay 2006, "
  "mouse). Its non-redundant role appears postnatally and in articular rather than growth plate cartilage: "
  "conditional elimination of Bmp7 from limb mesenchyme leaves the growth plate grossly intact but leads to "
  "articular cartilage degeneration with age (Abula 2015, mouse). BMP7 is therefore a weak candidate as a "
  "growth-plate rate-setting ligand and is included here to close the ligand inventory and to mark the "
  "articular-versus-physeal divergence explicitly."),
 localization=["mouse PERI: confirmed by in situ hybridisation (bandyopadhyay2006)","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human growth plate data; recombinant BMP7 clinical use was in spinal fusion, not physiological growth.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse-only genetics; the phenotype is articular, and articular and physeal chondrocytes are not interchangeable.',
 confidence='C',
 key_refs=[
  dict(ref_id='bandyopadhyay2006', pmid='17194222', first_author='Bandyopadhyay A', year=2006, type='primary',
       one_line_finding='Bmp7 is dispensable for limb skeletogenesis in mouse, unlike Bmp2/Bmp4.'),
  dict(ref_id='abula2015', pmid='25889639', first_author='Abula K', year=2015, type='primary_abstract_only',
       one_line_finding='Removing Bmp7 from limb mesenchyme causes articular cartilage degeneration in mouse.'),
 ],
))

NODES.append(dict(
 id='gdf5_protein', name='GDF5', type='protein', aliases=['growth differentiation factor 5','CDMP1','BMP14'],
 summary=(
  "GDF5 is a BMP-family ligand expressed at prospective joint interzones. Loss of function in mouse "
  "(brachypodism, bp) shortens and fuses limb segments and reduces digit number, and the bp locus was "
  "identified as Gdf5 by positional cloning (Storm 1994). The human orthologue produces the mirror "
  "phenotype: GDF5/CDMP1 mutations cause Grebe- and Hunter-Thompson-type acromesomelic chondrodysplasia "
  "with severe limb shortening (Thomas 1996), so this is one of the few BMP-arm nodes with direct human "
  "loss-of-function evidence. GDF5 is also a common-variant height locus: the GDF5-UQCC region carries "
  "SNPs associated with adult stature in general-population GWAS (Sanna 2008), which places the ligand on "
  "the normal-variation axis and not only in dysplasia. Guo 2009 proposes Gdf5/BMP signalling as a "
  "downstream, non-cell-autonomous effector of Wnt/beta-catenin control of hypertrophy in mouse, linking "
  "this node to the WNT subsystem."),
 quantitative=[
  dict(parameter='Effect of GDF5-UQCC region height allele (rs143384/rs6060369 region) on adult stature',
       value='~0.4', unit='cm per allele', conditions='meta-analysis of population cohorts of European ancestry, both sexes',
       species='human', source_ref='sanna2008', uncertainty='value read from abstract only; CI not confirmed at source',
       value_unverified=True),
 ],
 localization=["mouse joint interzone: confirmed (storm1994)","human: inferred from skeletal phenotype of CDMP1 mutations (thomas1996)"],
 human_evidence='direct',
 human_evidence_note='Biallelic GDF5/CDMP1 mutations cause human acromesomelic chondrodysplasia, and common GDF5-region variants associate with adult height.',
 species_basis=['mouse','human'], translation_risk='low',
 translation_risk_reason='Concordant loss-of-function phenotypes in mouse and human plus a human common-variant height association.',
 confidence='A',
 key_refs=[
  dict(ref_id='storm1994', pmid='8145850', first_author='Storm EE', year=1994, type='primary',
       one_line_finding='Mouse brachypodism is caused by mutations in Gdf5, a new TGF-beta superfamily member.'),
  dict(ref_id='thomas1996', pmid='8589725', first_author='Thomas JT', year=1996, type='primary',
       one_line_finding='A human chondrodysplasia (Hunter-Thompson type) is caused by a CDMP1/GDF5 mutation.'),
  dict(ref_id='sanna2008', pmid='18193045', first_author='Sanna S', year=2008, type='primary',
       one_line_finding='Common variants at the GDF5-UQCC locus associate with adult human height.'),
  dict(ref_id='guo2009', pmid='19557172', first_author='Guo X', year=2009, type='primary',
       one_line_finding='Wnt/beta-catenin controls hypertrophy onset non-cell-autonomously, possibly via Gdf5/BMP.'),
 ],
 open_questions=['g_l3rest_002'],
))

NODES.append(dict(
 id='noggin_antagonist', name='Noggin (NOG)', type='protein', aliases=['NOG'],
 summary=(
  "Noggin is a secreted BMP-binding antagonist. Mouse Nog-null embryos show grossly enlarged, fused "
  "cartilage elements with failure of joint formation, i.e. unopposed BMP signalling expands the "
  "chondrogenic field (Brunet 1998). Human heterozygous NOG loss-of-function causes proximal symphalangism "
  "and multiple synostoses syndrome - joint fusion rather than dwarfism - which is the clearest human "
  "demonstration that BMP dose, not BMP presence, is what the skeleton reads (Gong 1999). Noggin and "
  "Chordin are partially redundant: single nulls have distinct territories but the double mutant loses "
  "structures neither single mutant loses (Stottmann 2001, mouse). Noggin is widely used experimentally as "
  "the BMP-off reagent in growth plate explants, so a large fraction of 'BMP is required for X' claims in "
  "this subsystem are Noggin-inference rather than receptor genetics."),
 localization=["mouse joint interzone and perichondrium: confirmed (brunet1998)",
               "human: inferred from NOG haploinsufficiency phenotype (gong1999)"],
 human_evidence='direct',
 human_evidence_note='Heterozygous NOG mutations cause human proximal symphalangism/multiple synostoses, a joint-fusion phenotype.',
 species_basis=['mouse','human'], translation_risk='low',
 translation_risk_reason='Human germline loss-of-function phenotype is concordant in direction with the mouse null.',
 confidence='A',
 key_refs=[
  dict(ref_id='brunet1998', pmid='9603738', first_author='Brunet LJ', year=1998, type='primary',
       one_line_finding='Noggin-null mice have enlarged cartilage elements and fail to form joints.'),
  dict(ref_id='gong1999', pmid='10080184', first_author='Gong Y', year=1999, type='primary',
       one_line_finding='Heterozygous NOG mutations cause human proximal symphalangism and multiple synostoses syndrome.'),
  dict(ref_id='stottmann2001', pmid='11784076', first_author='Stottmann RW', year=2001, type='primary',
       one_line_finding='Chordin and Noggin have essential but partly redundant roles in mouse skeletal morphogenesis.'),
 ],
))

NODES.append(dict(
 id='chordin_antagonist', name='Chordin (CHRD)', type='protein', aliases=['CHRD'],
 summary=(
  "Chordin is a secreted BMP antagonist that shares substrate ligands with Noggin. In mouse, Chrd-null "
  "animals have craniofacial and pharyngeal defects; the appendicular skeleton is comparatively spared "
  "until Noggin is also removed, at which point mandibular and skeletal morphogenesis fails, demonstrating "
  "redundancy between the two antagonists (Stottmann 2001). There is no established human CHRD skeletal "
  "dysplasia and no report of zonal CHRD protein or transcript distribution in human growth plate. "
  "Chordin is therefore included as an inventory node with an explicit negative: within the growth plate "
  "proper, Noggin dominates the published antagonist evidence and Chordin's physeal role is assumed rather "
  "than demonstrated."),
 localization=["mouse craniofacial mesenchyme: confirmed (stottmann2001)","mouse growth plate: unconfirmed","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human CHRD skeletal phenotype and no human growth plate expression data.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse-only, and even in mouse the demonstrated territory is craniofacial rather than physeal.',
 confidence='D',
 key_refs=[
  dict(ref_id='stottmann2001', pmid='11784076', first_author='Stottmann RW', year=2001, type='primary',
       one_line_finding='Chordin and Noggin act redundantly in mouse mandibular and skeletal morphogenesis.'),
 ],
 open_questions=['g_l3rest_003'],
))

NODES.append(dict(
 id='smad1_5_8', name='SMAD1/5/8 (BMP-responsive R-SMADs)', type='protein',
 aliases=['SMAD1','SMAD5','SMAD9','SMAD8','BMP R-SMADs'],
 summary=(
  "SMAD1, SMAD5 and SMAD9(SMAD8) are the receptor-regulated SMADs phosphorylated by BMPR1A/BMPR1B; "
  "phospho-SMAD1/5/8 partners SMAD4 and enters the nucleus. Chondrocyte-restricted removal of Smad1 and "
  "Smad5 together in mouse produces severe chondrodysplasia with disorganised proliferative columns and "
  "impaired hypertrophy, while Smad1 or Smad5 single mutants and Smad8-null mice are near-normal - the "
  "requirement is for combined dose, not for a particular paralogue (Retting 2009). SMAD1/5/8 is also the "
  "convergence point for the antagonist layer: Noggin, Chordin and SMAD7 all act by lowering pSMAD1/5/8 "
  "output. SMAD7 inhibits chondrocyte differentiation at several steps in mouse, including by interfering "
  "with BMP-SMAD signalling (Iwai 2008). No zonal pSMAD1/5/8 immunostaining series has been published on "
  "human growth plate tissue, so the human activity gradient across RZ-PZ-PHZ-HZ is unmeasured."),
 localization=["mouse PZ/PHZ: pSmad1/5/8 activity inferred from conditional genetics (retting2009)",
               "human growth plate: unconfirmed - no published zonal pSMAD1/5/8 staining"],
 human_evidence='absent',
 human_evidence_note='No human growth plate pSMAD1/5/8 measurement; human evidence for the BMP arm is confined to ligand/antagonist genetics.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Entirely mouse conditional genetics; the human zonal activity profile has never been measured.',
 confidence='C',
 key_refs=[
  dict(ref_id='retting2009', pmid='19224984', first_author='Retting KN', year=2009, type='primary',
       one_line_finding='Combined chondrocyte Smad1/Smad5 loss, but not either alone, causes severe chondrodysplasia in mouse.'),
  dict(ref_id='iwai2008', pmid='18644788', first_author='Iwai T', year=2008, type='primary',
       one_line_finding='Smad7 inhibits chondrocyte differentiation at multiple steps of endochondral bone formation.'),
 ],
 open_questions=['g_l3rest_001'],
))

NODES.append(dict(
 id='smad2_3', name='SMAD2/SMAD3 (TGF-beta-responsive R-SMADs)', type='protein',
 aliases=['SMAD2','SMAD3'],
 summary=(
  "SMAD2 and SMAD3 are phosphorylated by TGFBR1 downstream of TGFBR2 and mediate the canonical TGF-beta "
  "response. Smad3-null mice develop normal-length skeletons at birth but show progressive expansion of "
  "the hypertrophic zone and accelerated terminal differentiation, with degeneration of articular "
  "cartilage - i.e. SMAD3 output is a brake on the hypertrophy transition, opposite in sign to the "
  "BMP-SMAD1/5/8 arm (Yang 2001, mouse). The same directionality is seen with dominant-negative TGFBR2 "
  "expression in mouse skeletal tissue, which produces terminal chondrocyte differentiation and "
  "osteoarthritis (Serra 1997). This BMP-versus-TGF-beta sign split inside one ligand superfamily is the "
  "reason 'TGF-beta superfamily signalling' is not a usable unit of analysis in this atlas. Human "
  "SMAD2/SMAD3 variants cause aneurysm-osteoarthritis/Loeys-Dietz-spectrum disease with skeletal features, "
  "but no human growth plate SMAD2/3 activity measurement exists."),
 localization=["mouse PHZ/HZ: inferred from Smad3-null zonal expansion (yang2001)","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='Human SMAD3 variants cause connective tissue disease with skeletal manifestations, but no growth plate SMAD2/3 activity data exist.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Growth plate causal data are mouse germline/dominant-negative only.',
 confidence='C',
 key_refs=[
  dict(ref_id='yang2001', pmid='11285272', first_author='Yang X', year=2001, type='primary',
       one_line_finding='Smad3-null mice show expanded hypertrophic zones and accelerated terminal chondrocyte differentiation.'),
  dict(ref_id='serra1997', pmid='9334355', first_author='Serra R', year=1997, type='primary',
       one_line_finding='Dominant-negative TGF-beta type II receptor in mouse skeleton promotes terminal chondrocyte differentiation.'),
 ],
))

NODES.append(dict(
 id='tgfb_signaling_chondrocyte', name='TGF-beta signalling in chondrocytes', type='pathway',
 summary=(
  "TGF-beta1/2/3 signal through TGFBR2-TGFBR1 to SMAD2/3 and, non-canonically, to TAK1-p38. In the growth "
  "plate the canonical arm restrains terminal differentiation: blocking it either at the receptor "
  "(dominant-negative TGFBR2, Serra 1997) or at the effector (Smad3-null, Yang 2001) accelerates "
  "hypertrophy and causes premature cartilage degeneration in mouse. This is the opposite sign to the "
  "BMP-SMAD1/5/8 arm, which promotes proliferation and, through beta-catenin/BMP2, maturation. Human "
  "evidence is indirect but unusually informative because it is dose-signed in both directions: "
  "gain-of-function TGFB1 mutations that release the latent complex cause Camurati-Engelmann disease with "
  "diaphyseal hyperostosis and limb pain (Kinoshita 2000), while LTBP3 loss of function - which impairs "
  "storage and presentation of latent TGF-beta - causes brachyolmia with short stature (Huckert 2015). "
  "The physiological ligand concentration seen by a human growth plate chondrocyte has never been "
  "measured."),
 localization=["mouse PHZ/HZ: inferred (yang2001, serra1997)","human growth plate: unconfirmed"],
 human_evidence='indirect',
 human_evidence_note=("Human TGFB1 gain-of-function (Camurati-Engelmann) and LTBP3 loss-of-function (brachyolmia) "
  "phenotypes bracket the pathway in both directions, but neither is a growth-plate measurement."),
 species_basis=['mouse','human'], translation_risk='moderate',
 translation_risk_reason='Mechanism is mouse; human data are germline variants with systemic effects and no physeal read-out.',
 confidence='B',
 key_refs=[
  dict(ref_id='serra1997', pmid='9334355', first_author='Serra R', year=1997, type='primary',
       one_line_finding='Truncated kinase-dead TGFBR2 in mouse skeleton promotes terminal chondrocyte differentiation and osteoarthritis.'),
  dict(ref_id='yang2001', pmid='11285272', first_author='Yang X', year=2001, type='primary',
       one_line_finding='TGF-beta/Smad3 signalling represses chondrocyte hypertrophic differentiation in mouse.'),
  dict(ref_id='kinoshita2000', pmid='10973241', first_author='Kinoshita A', year=2000, type='primary',
       one_line_finding='Domain-specific TGFB1 mutations that destabilise the latency complex cause human Camurati-Engelmann disease.'),
  dict(ref_id='huckert2015', pmid='25669657', first_author='Huckert M', year=2015, type='primary',
       one_line_finding='LTBP3 loss-of-function mutations cause human brachyolmia with short stature and amelogenesis imperfecta.'),
 ],
 open_questions=['g_l3rest_004'],
))

NODES.append(dict(
 id='tgfbr2_receptor', name='TGFBR2', type='protein', aliases=['TGF-beta type II receptor'],
 summary=(
  "TGFBR2 is the ligand-binding serine/threonine kinase receptor that recruits and transphosphorylates "
  "TGFBR1, which then phosphorylates SMAD2/3. Expression of a truncated kinase-defective TGFBR2 in mouse "
  "skeletal tissue under the Col2a1 promoter produces progressive terminal chondrocyte differentiation, "
  "loss of the articular surface and osteoarthritis-like change, establishing TGFBR2 output as a brake on "
  "chondrocyte maturation (Serra 1997). In human, heterozygous TGFBR2 missense mutations cause "
  "Loeys-Dietz syndrome, whose skeletal features (arachnodactyly, scoliosis, joint laxity, "
  "craniosynostosis) are consistent with altered cartilage and connective tissue TGF-beta signalling, but "
  "the human phenotype is dominated by aortic disease and no growth plate specimen has been assayed. "
  "TGFBR2 activity in the physis is thus mouse-established and human-inferred."),
 localization=["mouse growth plate cartilage: transgene-based inference (serra1997)","human growth plate: unconfirmed"],
 human_evidence='indirect',
 human_evidence_note='Human TGFBR2 variants cause Loeys-Dietz syndrome with skeletal features; no human growth plate receptor data.',
 species_basis=['mouse','human'], translation_risk='moderate',
 translation_risk_reason='Human phenotype is systemic connective tissue disease; the physeal contribution is not separable.',
 confidence='C',
 key_refs=[
  dict(ref_id='serra1997', pmid='9334355', first_author='Serra R', year=1997, type='primary',
       one_line_finding='Dominant-negative TGFBR2 in mouse cartilage causes terminal chondrocyte differentiation and osteoarthritis.'),
  dict(ref_id='yang2001', pmid='11285272', first_author='Yang X', year=2001, type='primary',
       one_line_finding='The Smad3-null phenotype phenocopies receptor blockade, placing SMAD3 downstream of TGFBR2 in cartilage.'),
 ],
))

NODES.append(dict(
 id='latent_tgfb_matrix_store', name='Latent TGF-beta matrix store (LAP/LTBP complex)', type='process',
 aliases=['large latent complex','LTBP-bound TGF-beta'],
 summary=(
  "TGF-beta is secreted as a small latent complex (mature dimer non-covalently held by its latency-"
  "associated peptide) covalently linked to a latent TGF-beta binding protein (LTBP1/3/4), which anchors "
  "it to fibrillin-containing microfibrils in the extracellular matrix. Cartilage matrix therefore holds a "
  "reservoir of pre-made ligand whose bioavailability is set by proteolytic, integrin-mediated and "
  "mechanical release rather than by transcription. Two human genetic experiments bracket the store: "
  "TGFB1 mutations in the LAP domain destabilise latency and cause Camurati-Engelmann disease with excess "
  "signalling (Kinoshita 2000), while biallelic LTBP3 loss of function causes brachyolmia with short "
  "stature and reduced growth (Huckert 2015). This makes the latent store one of the few L3 nodes with "
  "human bidirectional dose evidence. What has never been measured in any species is the absolute "
  "concentration of latent TGF-beta per unit volume of growth plate matrix, or how much of it is released "
  "per loading cycle."),
 localization=["human bone/cartilage matrix: inferred from LTBP3 and TGFB1 human phenotypes",
               "growth plate zonal distribution of latent complex: unmeasured in any species"],
 human_evidence='indirect',
 human_evidence_note='Human LTBP3 and TGFB1 variant phenotypes imply a functional matrix latent store, but no direct measurement in human physeal matrix exists.',
 species_basis=['human','mouse'], translation_risk='moderate',
 translation_risk_reason='Inference from germline human variants; the biochemistry itself is largely from non-skeletal tissue.',
 confidence='C',
 key_refs=[
  dict(ref_id='kinoshita2000', pmid='10973241', first_author='Kinoshita A', year=2000, type='primary',
       one_line_finding='TGFB1 LAP-domain mutations cause Camurati-Engelmann disease, implying release of latent TGF-beta drives the phenotype.'),
  dict(ref_id='huckert2015', pmid='25669657', first_author='Huckert M', year=2015, type='primary',
       one_line_finding='Biallelic LTBP3 mutations cause human brachyolmia with short stature.'),
 ],
 open_questions=['g_l3rest_004'],
))

NODES.append(dict(
 id='ihh_bmp_crosstalk', name='IHH-BMP crosstalk', type='process',
 summary=(
  "BMP and Indian hedgehog signalling in the growth plate are interdependent but not serial. In mouse limb "
  "explants, BMP2 beads raise Ihh expression, and Ihh signalling raises Bmp2/Bmp4 expression in the "
  "perichondrium, so each arm can amplify the other. The decisive experiment is that BMP2 still increases "
  "chondrocyte proliferation when Ihh signalling is blocked (and Ihh still acts when BMP signalling is "
  "blocked with Noggin), which places them as parallel proliferative inputs converging on the same "
  "columnar chondrocytes rather than as one linear cascade (Minina 2001, mouse). The two arms differ in "
  "what they control: Ihh/PTHrP sets the position of the hypertrophy boundary through the negative "
  "feedback loop, whereas BMP raises proliferation rate and delays hypertrophy largely independently of "
  "PTHrP. Minina 2002 adds the third input, showing FGF opposes BMP on both readouts in the same system. "
  "All of this is mouse explant work; there is no human tissue equivalent."),
 localization=["mouse PZ/PHZ and perichondrium: confirmed in limb explant culture (minina2001, minina2002)",
               "human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='Crosstalk has never been tested in human tissue; no human explant or organoid experiment addresses it.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Bead-implant explant pharmacology in embryonic mouse limbs; dose and diffusion are non-physiological.',
 confidence='C',
 key_refs=[
  dict(ref_id='minina2001', pmid='11714677', first_author='Minina E', year=2001, type='primary',
       one_line_finding='BMP and Ihh/PTHrP act as parallel, mutually reinforcing inputs on chondrocyte proliferation and hypertrophy timing.'),
  dict(ref_id='minina2002', pmid='12361605', first_author='Minina E', year=2002, type='primary',
       one_line_finding='FGF signalling antagonises BMP on proliferation and hypertrophy in mouse limb explants.'),
  dict(ref_id='stjacques1999', pmid='10465785', first_author='St-Jacques B', year=1999, type='primary',
       one_line_finding='Ihh-null mice show reduced chondrocyte proliferation and failure of osteoblast development, defining the Ihh arm.'),
 ],
 open_questions=['g_l3rest_001'],
))

for n in NODES: w(n)
print(len(NODES), 'nodes')
