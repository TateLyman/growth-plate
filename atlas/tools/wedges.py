import yaml
E = []
def e(s, t, rel, sign, ctx, tier, refs, conf, mag=None, notes=None, gap=None):
    d = dict(edge_id='e%05d' % (len(E) + 1), source=s, target=t, relation=rel, sign=sign)
    if mag: d['magnitude'] = mag
    d.update(context=ctx, evidence_tier=tier, refs=refs, confidence=conf)
    if gap: d['gap_id'] = gap
    if notes: d['notes'] = notes
    E.append(d)

M = 'mouse growth plate, embryonic and postnatal, both sexes'

# ---------------- BMP / TGF-beta ----------------
e('bmp2_ligand','bmp_signaling_growth_plate','activates','+','mouse PHZ/HZ, Col2-Cre conditional deletion','T1',['shu2011','garrison2017'],'C',
  notes='Bmp2 mRNA peaks in HZ; cartilage-specific Bmp2 loss reduces proliferation and maturation, Bmp4 loss does not.')
e('bmp6_ligand','bmp_signaling_growth_plate','activates','+','mouse HZ, germline null','T1',['perry2008','garrison2017'],'D')
e('bmp7_ligand','bmp_signaling_growth_plate','activates','+','mouse perichondrium, limb mesenchyme','T1',['bandyopadhyay2006'],'C',
  notes='Individually dispensable for limb skeletogenesis.')
e('gdf5_protein','bmp_signaling_growth_plate','activates','+','mouse joint interzone and adjacent cartilage','T1',['storm1994','guo2009'],'C')
e('bmp_signaling_growth_plate','smad1_5_8','phosphorylates','+','mouse chondrocytes, BMPR1A/BMPR1B-dependent','T1',['yoon2005','retting2009'],'C')
e('smad1_5_8','chondrocyte_hypertrophy','required_for','+',M,'T1',['retting2009'],'C',
  notes='Smad1/Smad5 double conditional null gives severe chondrodysplasia with impaired hypertrophy.')
e('smad1_5_8','chondrocyte_proliferation_rate','activates','+','mouse PZ','T1',['retting2009','garrison2017'],'C')
e('noggin_antagonist','bmp_signaling_growth_plate','inhibits','-','mouse perichondrium and interzone; human NOG haploinsufficiency','T1',['brunet1998','gong1999'],'A')
e('noggin_antagonist','bmp2_ligand','binds','-','extracellular, mouse and human','T1',['brunet1998'],'C')
e('chordin_antagonist','bmp_signaling_growth_plate','inhibits','-','mouse craniofacial and axial mesenchyme; physeal role unconfirmed','T1',['stottmann2001'],'D')
e('noggin_antagonist','interzone_formation','required_for','+','mouse limb joints, E12.5-E14.5','T1',['brunet1998','gong1999'],'A',
  notes='Nog-null mice fail to form joints; human NOG haploinsufficiency causes symphalangism.')
e('gdf5_protein','interzone_formation','required_for','+','mouse limb interzone; human GDF5/CDMP1 mutation','T1',['storm1994','thomas1996'],'A')
e('gdf5_protein','gdf5_height_locus','correlates_with','+','human, population cohorts of European ancestry','T1',['sanna2008'],'B',
  mag='approximately 0.4 cm per allele (value_unverified)')
e('bmp_signaling_growth_plate','ihh_protein','activates','+','mouse limb explant, BMP2 bead implantation','T1',['minina2001'],'C')
e('ihh_protein','bmp2_ligand','activates','+','mouse perichondrium, limb explant','T1',['minina2001'],'C')
e('bmp_signaling_growth_plate','ihh_bmp_crosstalk','required_for','+','mouse limb explant','T1',['minina2001','minina2002'],'C')
e('ihh_protein','ihh_bmp_crosstalk','required_for','+','mouse limb explant','T1',['minina2001','stjacques1999'],'C')
e('bmp_signaling_growth_plate','chondrocyte_proliferation_rate','activates','+','mouse PZ, limb explant; Ihh-independent component demonstrated','T1',['minina2001'],'C')
e('fgfr3_receptor','bmp_signaling_growth_plate','inhibits','-','mouse limb explant, FGF versus BMP bead antagonism','T1',['minina2002'],'C')
e('smad1_5_8','collagen_type_x','transcribes','+','mouse chondrocytes, Col10a1-luciferase; Smad1 with Runx2 and MEF2','T1',['kozhemyakina2009'],'D')
e('tgfbr2_receptor','smad2_3','phosphorylates','+','mouse cartilage, via TGFBR1','T1',['serra1997','yang2001'],'C')
e('smad2_3','chondrocyte_hypertrophy','inhibits','-','mouse growth plate, Smad3 germline null','T1',['yang2001'],'C')
e('tgfb_signaling_chondrocyte','chondrocyte_hypertrophy','inhibits','-','mouse growth plate and articular cartilage','T1',['serra1997','yang2001'],'B')
e('latent_tgfb_matrix_store','tgfb_signaling_chondrocyte','required_for','+','human, inferred from LTBP3 and TGFB1 germline phenotypes','T1',['huckert2015','kinoshita2000'],'C',
  notes='Human bidirectional dose evidence; the matrix concentration itself is unmeasured (g_l3rest_004).')
e('tgfbr2_receptor','loeys_dietz_syndrome','correlates_with','+','human germline heterozygous missense variants','T1',['serra1997'],'E',
  notes='Association is clinical-genetic; the mouse receptor experiment is cited as the mechanistic anchor, not as human evidence.')

# ---------------- WNT canonical ----------------
e('wnt_canonical_chondrocyte','beta_catenin_ctnnb1','activates','+',M,'T1',['akiyama2004','dao2012'],'C')
e('gsk3b_kinase','beta_catenin_ctnnb1','degrades','-','human chondrocytes in vitro; LiCl inhibition raises beta-catenin','T1',['guidotti2015','akiyama2004'],'D')
e('lrp5_coreceptor','wnt_canonical_chondrocyte','required_for','+','mouse embryo, redundant with Lrp6; human LRP5 allelic series','T1',['joeng2011','gong2001','boyden2002'],'B')
e('lrp6_coreceptor','wnt_canonical_chondrocyte','required_for','+','mouse embryonic skeleton, dominant of the two paralogues','T1',['joeng2011'],'C')
e('sclerostin_sost','lrp5_coreceptor','inhibits','-','human osteocyte-derived; growth plate action unconfirmed','T1',['poole2005','balemans2001','boyden2002'],'B',gap=None,
  notes='Whether sclerostin reaches the growth plate chondrocyte is open (g_l3rest_007).')
e('dkk1_antagonist','lrp5_coreceptor','inhibits','-','human LRP5 G171V resists DKK1 binding','T1',['boyden2002','li2006'],'B')
e('dkk1_antagonist','lrp6_coreceptor','inhibits','-','mouse bone, transgenic overexpression and heterozygous null','T1',['li2006'],'C')
e('beta_catenin_ctnnb1','chondrocyte_hypertrophy','activates','biphasic','mouse growth plate; loss delays hypertrophy, gain accelerates it, excess blocks chondrogenesis','T1',
  ['akiyama2004','chen2008','dao2012','yuasa2009'],'C',
  notes='Dose-dependent with opposite phenotypes at the extremes; no human dose-response exists (g_l3rest_006).')
e('wnt_canonical_chondrocyte','pth1r_receptor','inhibits','-','mouse growth plate; Wnt lowers PTHrP signalling activity without changing PTHrP expression','T1',['guo2009'],'C')
e('sox9_tf','beta_catenin_ctnnb1','degrades','-','mouse chondrocytes and Xenopus assay; SOX9 binds Armadillo repeats and promotes degradation','T1',['akiyama2004','topol2009'],'C')
e('beta_catenin_ctnnb1','sox9_tf','inhibits','-','mouse chondrocytes; stabilised beta-catenin phenocopies Sox9 loss','T1',['akiyama2004'],'C')
e('beta_catenin_ctnnb1','mmp13_protease','transcribes','+','mouse HZ, Col10a1-Cre conditional deletion','T1',['golovchenko2013'],'D')
e('beta_catenin_ctnnb1','vegfa_growth_plate','transcribes','+','mouse chondrocytes; requires cooperation with BMP2 signalling','T1',['chen2008','golovchenko2013'],'C')
e('beta_catenin_ctnnb1','bmp2_ligand','transcribes','+','mouse cartilage, inducible gain of function','T1',['dao2012'],'C')
e('beta_catenin_ctnnb1','runx2_tf','activates','+','mouse growth plate chondrocytes','T1',['dao2012','dy2012'],'C')
e('beta_catenin_ctnnb1','epiphyseal_fusion','activates','+','mouse, transient activation in young adult cartilage causes premature plate closure','T1',['yuasa2009'],'D',
  notes='Mice do not normally fuse, so this is a forced phenotype and its human relevance is unestablished.')
e('beta_catenin_ctnnb1','chondrocyte_to_osteoblast_transdifferentiation','activates','+','mouse hypertrophic chondrocytes','T1',['dao2012','dy2012'],'D')
e('sclerostin_sost','wnt_canonical_chondrocyte','inhibits','-','rabbit, rat and mini-pig articular cartilage, exogenous sclerostin hydrogel','T1',['ruscitto2023'],'C',
  notes='Demonstrates chondrocyte responsiveness to sclerostin; not a growth plate experiment.')

# ---------------- WNT non-canonical ----------------
e('wnt5a_ligand','wnt_noncanonical_pcp','activates','+','mouse limb mesenchyme, graded ligand','T1',['gao2011','li2009'],'C')
e('wnt5a_ligand','vangl2_pcp','phosphorylates','+','mouse limb, ROR2-dependent, graded with WNT5A concentration','T1',['gao2011'],'C')
e('vangl2_pcp','wnt_noncanonical_pcp','required_for','+','mouse limb; Looptail allele is phosphorylation-deficient and dominant negative','T1',['gao2011'],'C')
e('wnt_noncanonical_pcp','chondrocyte_column_formation','required_for','+','mouse PZ, explant live imaging','T1',['li2009'],'C')
e('wnt_noncanonical_pcp','chondrocyte_rotation','required_for','+','mouse PZ, post-mitotic rotation','T1',['li2009'],'C')
e('wnt5a_ligand','chondrocyte_hypertrophy','inhibits','-','mouse; Wnt5a delays and Wnt5b promotes the transition','T1',['yang2003'],'D',
  notes='Paralogue-specific and opposite in sign, so "non-canonical WNT" is not a usable single variable here.')

# ---------------- Notch ----------------
e('notch_signaling_chondrocyte','rbpj_tf','activates','+','mouse chondrocyte lineage, NICD-dependent','T1',['mead2009','kohn2015'],'C')
e('rbpj_tf','hes1_tf','transcribes','+','mouse chondrocytes','T1',['hosaka2013','rutkowski2016'],'C')
e('hes1_tf','chondrocyte_hypertrophy','activates','+','mouse; HES1 and HES5 promote hypertrophy onset','T1',['rutkowski2016','hosaka2013'],'C')
e('hes1_tf','sox9_tf','inhibits','-','mouse chondrogenic cells; direct Sox9 regulation shown for HES5 rather than HES1','T1',['rutkowski2016'],'D')
e('notch_signaling_chondrocyte','sox9_tf','inhibits','-','mouse limb mesenchyme; prolonged Notch suppresses Sox9, acute Notch induces it','T1',['kohn2015','mead2009'],'C',
  notes='Sign is duration-dependent; Kohn 2015 shows acute induction and sustained suppression.')
e('notch_signaling_chondrocyte','chondrocyte_proliferation_rate','inhibits','-','mouse cartilage precursors; Rbpj deletion increases proliferation','T1',['mead2009'],'C')
e('rbpj_tf','endochondral_ossification','required_for','+','mouse, Sox9-Cre and Prx1-Cre conditional deletion','T1',['hosaka2013','kohn2015','gao2022'],'C')
e('notch_signaling_chondrocyte','chondrocyte_hypertrophy','inhibits','-','mouse, forced NICD expression in chondrocyte lineage','T1',['mead2009'],'C',
  notes='Opposite in sign to the HES1 terminal-maturation edge; the two act at different steps.')

# ---------------- mTORC1 / nutrient ----------------
e('raptor_protein','mtorc1_chondrocyte','required_for','+','mouse limb cartilage, Prx1-Cre conditional deletion','T1',['chen2014'],'C')
e('tsc1_tsc2','mtorc1_chondrocyte','inhibits','-','mouse resting and proliferating zone chondrocytes','T1',['hsieh2021'],'C')
e('mtorc1_chondrocyte','hypertrophic_volume_increase','activates','+','mouse limb cartilage; effect is on cell size and matrix, not proliferation','T1',['chen2014'],'C')
e('mtorc1_chondrocyte','autophagy_chondrocyte','inhibits','-','mouse growth plate maturing zone and chondrocytic cells','T1',['srinivas2009'],'D')
e('mtorc1_chondrocyte','prehypertrophic_chondrocyte','activates','+','mouse synchondrosis; Tsc1 deletion confers prehypertrophic features on resting cells','T1',['hsieh2021'],'C')
e('tsc1_tsc2','resting_zone','required_for','+','mouse cranial base synchondrosis; loss expands the resting zone','T1',['hsieh2021'],'C')
e('amino_acid_sensing_chondrocyte','mtorc1_chondrocyte','activates','+','chondrocyte, extrapolated from canonical amino-acid sensing; not tested in growth plate','T5',['chen2018','stegen2020'],'speculative',
  gap='g_l3rest_010', notes='Placed as a hypothesis: no experiment links glutamine availability to chondrocyte mTORC1 activity in vivo.')
e('sox9_tf','amino_acid_sensing_chondrocyte','activates','+','mouse chondrocytes; SOX9 raises glutamine consumption and GLS1','T1',['stegen2020'],'C')
e('amino_acid_sensing_chondrocyte','sox9_tf','required_for','+','mouse chondrocytes; GLS1-derived acetyl-CoA sustains chondrogenic histone acetylation','T1',['stegen2020'],'C',
  notes='Closes a transcription-metabolism feedforward loop with the preceding edge.')
e('autophagy_chondrocyte','hypertrophic_chondrocyte_survival','required_for','+','mouse Atg5/Atg7 conditional null; human growth plate tissue slices with autophagy inhibitors','T1',['vuppalapati2015','srinivas2009'],'B')
e('hif1a_chondrocyte','autophagy_chondrocyte','activates','+','mouse growth plate maturing zone','T1',['srinivas2009'],'D')
e('settembre_placeholder','x','activates','+','','T1',[],'C') if False else None

# ---------------- Hypoxia ----------------
e('hypoxic_gradient_signaling','hif1a_chondrocyte','activates','+','mouse growth plate interior; rat and rabbit direct oximetry','T1',['schipani2001','brighton1971'],'C')
e('oxygen_gradient_growth_plate','hypoxic_gradient_signaling','correlates_with','+','rat, rabbit, mouse; human gradient never measured','T1',['brighton1971','schipani2001'],'D',
  notes='The human oxygen gradient is assumed, not measured (g_l3rest_011).')
e('vhl_protein','hif1a_chondrocyte','degrades','-','mouse cartilage, Vhlh conditional deletion; Vhlh;Hif1a double null resembles Hif1a null','T1',['pfander2004'],'C')
e('hif1a_chondrocyte','chondrocyte_apoptosis_hz','inhibits','-','mouse growth plate interior','T1',['schipani2001','zelzer2004'],'C')
e('hif1a_chondrocyte','vegfa_growth_plate','transcribes','+','mouse epiphyseal chondrocytes; a HIF1A-independent component also exists near dying cells','T1',['schipani2001','zelzer2004'],'C')
e('hif1a_chondrocyte','chondrocyte_proliferation_rate','inhibits','-','mouse growth plate interior; loss raises BrdU incorporation and lowers p57','T1',['schipani2001'],'C')
e('vegfa_growth_plate','vascular_invasion_poc','required_for','+','mouse, soluble receptor sequestration and Col2-Cre conditional deletion','T1',['gerber1999','zelzer2004'],'C')
e('vegfa_growth_plate','chondrocyte_apoptosis_hz','inhibits','-','mouse epiphyseal and joint chondrocytes, distant from vessels','T1',['zelzer2004'],'C')
e('vegfa_growth_plate','hypertrophic_zone','inhibits','-','mouse; VEGF sequestration expands the hypertrophic zone reversibly','T1',['gerber1999'],'C',
  notes='Sign refers to zone height: blocking VEGF enlarges HZ because terminal cells are not removed.')
e('vegfa_growth_plate','type_h_vessel','activates','+','mouse metaphysis and perichondrium','T1',['duan2015','gerber1999'],'D')
e('hypoxic_gradient_signaling','nutrient_diffusion_growth_plate','correlates_with','+','avascular cartilage; diffusion distance sets both','T5',['schipani2015'],'E')

# ---------------- Transcriptional control ----------------
e('sox9_tf','sox5_tf','transcribes','+','mouse chondrocytes, staged conditional inactivation','T1',['akiyama2002'],'C')
e('sox9_tf','sox6_tf','transcribes','+','mouse chondrocytes, staged conditional inactivation','T1',['akiyama2002'],'C')
e('sox9_tf','sox_trio','required_for','+','mouse cartilage','T1',['akiyama2002','smits2001'],'B')
e('sox5_tf','sox_trio','required_for','+','mouse cartilage; redundant with SOX6','T1',['smits2001'],'C')
e('sox6_tf','sox_trio','required_for','+','mouse cartilage; redundant with SOX5','T1',['smits2001'],'C')
e('sox_trio','collagen_type_ii','transcribes','+','mouse cartilage; matrix genes near-absent in Sox5;Sox6 double null','T1',['smits2001','bi1999'],'B')
e('sox_trio','aggrecan_acan','transcribes','+','mouse cartilage','T1',['smits2001'],'C')
e('sox9_tf','chondrocyte_column_formation','required_for','+','mouse growth plate, doxycycline-inducible Sox9 deletion','T1',['dy2012'],'C')
e('sox9_tf','runx2_tf','inhibits','-','mouse growth plate chondrocytes','T1',['dy2012'],'C')
e('sox9_tf','chondrocyte_to_osteoblast_transdifferentiation','inhibits','-','mouse growth plate chondrocytes','T1',['dy2012'],'C')
e('sox9_tf','sox9_chondrogenic_commitment','required_for','+','mouse condensation; human campomelic dysplasia haploinsufficiency','T1',['bi1999','foster1994','wagner1994'],'A')
e('fgfr3_receptor','sox9_tf','activates','+','mouse and human achondroplasia models; activated FGFR3 prevents SOX9 downregulation','T1',['zhou2015'],'C',
  notes='Contradicts the requirement direction in Dy 2012; logged as g_l3rest_012.')
e('runx2_tf','chondrocyte_hypertrophy','activates','+','mouse; complete failure only in Runx2;Runx3 double null','T1',['yoshida2004','vega2004'],'B')
e('runx3_tf','chondrocyte_hypertrophy','activates','+','mouse; redundant with RUNX2, dose-dependent','T1',['yoshida2004','soung2007'],'C')
e('runx2_tf','ihh_protein','transcribes','+','mouse chondrocytes; RUNX2 binds the Ihh promoter directly','T1',['yoshida2004'],'C',
  notes='Closes a feedback loop from the hypertrophy licence back onto the IHH/PTHrP circuit.')
e('runx2_tf','collagen_type_x','transcribes','+','mouse chondrocytes, Col10a1 reporter','T1',['kozhemyakina2009','vega2004'],'C')
e('runx2_tf','mmp13_protease','transcribes','+','mouse hypertrophic chondrocytes','T1',['yoshida2004'],'D')
e('runx2_tf','cleidocranial_dysplasia','correlates_with','+','human heterozygous RUNX2 loss of function','T1',['mundlos1997'],'A')
e('hdac4_protein','runx2_tf','inhibits','-','mouse PHZ; HDAC4 binds and inhibits RUNX2','T1',['vega2004','nishimori2021'],'B')
e('hdac4_protein','mef2c_tf','inhibits','-','mouse chondrocytes; genetically titrated against MEF2C in vivo','T1',['arnold2007','kozhemyakina2009','nishimori2019'],'B')
e('hdac4_protein','chondrocyte_hypertrophy','inhibits','-','mouse PHZ; human HDAC4 haploinsufficiency causes brachydactyly type E','T1',['vega2004','le2019','takeyari2023'],'A')
e('mef2c_tf','chondrocyte_hypertrophy','activates','+','mouse; both loss and superactivation shorten bone by opposite routes','T1',['arnold2007'],'C')
e('mef2c_tf','runx2_tf','activates','+','mouse chondrocytes; MEF2 permits Runx2 mRNA expression','T1',['nishimori2019','nishimori2021'],'C')
e('mef2c_tf','collagen_type_x','transcribes','+','mouse upper hypertrophic chondrocytes, with residual SOX9 protein','T1',['dy2012','kozhemyakina2009'],'C')
e('salt_inducible_kinase3','hdac4_protein','phosphorylates','-','mouse PHZ/HZ; phosphorylation at 14-3-3 sites retains HDAC4 in cytoplasm','T1',['sasagawa2012','nishimori2021'],'C',
  notes='Sign refers to HDAC4 repressor activity, which falls when SIK3 phosphorylates it.')
e('salt_inducible_kinase3','chondrocyte_hypertrophy','activates','+','mouse; Sik3-null hypertrophy blocked to E18.5','T1',['sasagawa2012'],'C')
e('salt_inducible_kinase3','epiphyseal_fusion','activates','+','mouse; chondrocyte SIK3 overexpression closes growth plates in adults','T1',['sasagawa2012'],'D',
  notes='Mice do not normally fuse, so this is a gain-of-function phenotype without a human counterpart.')
e('pthrp_protein','salt_inducible_kinase3','inhibits','-','mouse growth plate; via cAMP/PKA phosphorylation of SIK3 PKA sites','T1',['nishimori2021'],'C')
e('pth1r_receptor','hdac4_protein','activates','+','mouse chondrocytes; PTHrP/PKA drives HDAC4 dephosphorylation and nuclear entry','T1',['kozhemyakina2009','nishimori2019'],'C',
  notes='Also PP2A-dependent; okadaic acid reverses forskolin-induced nuclear translocation.')
e('pthrp_ihh_feedback_loop','hdac4_protein','activates','+','mouse PHZ','T1',['nishimori2019','nishimori2021'],'C')
e('pthrp_protein','zfp521_protein','transcribes','+','mouse prehypertrophic chondrocytes','T1',['correa2010'],'C')
e('zfp521_protein','runx2_tf','inhibits','-','mouse chondrocytes; HDAC4-dependent antagonism','T1',['correa2010'],'C')
e('zfp521_protein','chondrocyte_hypertrophy','inhibits','-','mouse; Zfp521 deletion phenocopies PTHrP loss','T1',['correa2010'],'C')
e('foxa_family_chondrocyte','collagen_type_x','transcribes','+','mouse chondrocytes; conserved FoxA sites in the Col10a1 enhancer','T1',['ionescu2012'],'C')
e('foxa_family_chondrocyte','chondrocyte_hypertrophy','required_for','+','mouse; FoxA2;FoxA3 double mutants are postnatally dwarfed','T1',['ionescu2012'],'C')
e('foxa_family_chondrocyte','mmp13_protease','transcribes','+','mouse growth plate','T1',['ionescu2012'],'D')

# ---------------- Cilium ----------------
e('ift88_protein','primary_cilium_chondrocyte','required_for','+','mouse limb mesenchyme, conditional deletion','T1',['haycraft2007'],'C')
e('ift80_protein','primary_cilium_chondrocyte','required_for','+','mouse chondrocytes and stromal cells; human IFT80 ciliopathy','T1',['wang2013','beales2007','yuan2015'],'B')
e('kif3a_protein','primary_cilium_chondrocyte','required_for','+','mouse cartilage, conditional deletion','T1',['koyama2007'],'C')
e('primary_cilium_chondrocyte','smoothened','required_for','+','mouse chondrocytes; SMO must accumulate in the ciliary membrane','T1',['haycraft2007','dorn2012'],'B')
e('primary_cilium_chondrocyte','gli3_repressor','required_for','+','mouse; GLI3 processing depends on intraflagellar transport','T1',['haycraft2007','ruizperez2007'],'C',
  notes='Evc-null cilia process Gli3 normally, so EVC acts downstream of this step.')
e('primary_cilium_chondrocyte','ihh_protein','required_for','+','mouse growth plate; cilium loss abolishes Ihh target gene induction inside the plate','T1',['haycraft2007','koyama2007'],'C',
  notes='Directional caveat: Kif3a loss raises hedgehog signalling in the adjacent perichondrium while lowering it in cartilage.')
e('primary_cilium_chondrocyte','wnt_canonical_chondrocyte','inhibits','-','mouse chondrogenic cells; IFT80 silencing raises WNT activity','T1',['wang2013','yuan2015'],'D')
e('evc_evc2_complex','smoothened','binds','+','mouse and cultured cells; complex confined to the EvC zone at the ciliary base','T1',['dorn2012','ruizperez2007'],'B')
e('evc_evc2_complex','gli1_tf','activates','+','mouse growth plate; Evc-null plates have normal Ihh but markedly reduced Gli1','T1',['ruizperez2007','dorn2012'],'B')
e('evc_evc2_complex','patched1','transcribes','+','mouse growth plate; Ptch1 induction lost in Evc-null cartilage','T1',['ruizperez2007'],'B')
e('evc_evc2_complex','sufu_protein','inhibits','-','cultured cells; EVC2 acts between SMO and the PKA/SUFU step','T1',['dorn2012'],'C')
e('evc_evc2_complex','chondrocyte_hypertrophy','inhibits','-','mouse; Evc-null growth plates show advanced chondrocyte maturation','T1',['ruizperez2007'],'C')
e('kif3a_protein','growth_plate','required_for','+','mouse cranial base synchondrosis; zonal organisation lost by P7','T1',['koyama2007'],'C')
e('ift80_protein','chondrocyte_hypertrophy','required_for','+','mouse, inducible Col2a1-CreER deletion','T1',['yuan2015'],'C')
e('ift80_protein','articular_cartilage','inhibits','-','mouse; postnatal Ift80 deletion thickens articular cartilage while shortening the growth plate','T1',['yuan2015'],'D')
e('primary_cilium_chondrocyte','primary_cilium_mechanosensing','hypothesized_link','unknown','human growth plate; ciliary prevalence and length by zone unmeasured','T5',['koyama2007','wang2013'],'speculative',
  gap='g_l3rest_014', notes='Whether the Hedgehog-transducing cilium and the mechanosensing cilium are the same organelle population in human physis is untested.')

# ---------------- Convergence ----------------
e('sox9_tf','pathway_convergence_node','required_for','+','mouse; receives Notch, WNT, Hedgehog/cilium and metabolic inputs','T1',
  ['kohn2015','akiyama2004','wang2013','stegen2020'],'E', notes='Membership edge: SOX9 is one of the four documented convergence points.')
e('runx2_tf','pathway_convergence_node','required_for','+','mouse; restrained by HDAC4, ZFP521 and SOX9, promoted by beta-catenin and MEF2C','T1',
  ['vega2004','correa2010','dy2012','dao2012'],'E', notes='Membership edge.')
e('beta_catenin_ctnnb1','pathway_convergence_node','required_for','+','mouse; integrates WNT, SOX9 antagonism, PTHrP and ciliary Hedgehog tone','T1',
  ['akiyama2004','guo2009','wang2013'],'E', notes='Membership edge.')
e('hdac4_protein','pathway_convergence_node','required_for','+','mouse; subcellular localisation integrates PTHrP-PKA-SIK3, PP2A and MEF2C/RUNX2 availability','T1',
  ['nishimori2021','kozhemyakina2009','arnold2007'],'E', notes='Membership edge.')
e('pathway_convergence_node','chondrocyte_hypertrophy','hypothesized_link','unknown','human growth plate; joint integration never measured in one tissue','T5',
  ['kohn2015','dy2012','nishimori2021'],'speculative', gap='g_l3rest_015',
  notes='Convergence is assembled from pairwise mouse experiments; single-cell multiplexed measurement is required to test it.')

E = [x for x in E if x is not None]
with open('/home/user/growth-plate/atlas/edges/shards/l3rest.edges.yaml', 'w') as f:
    yaml.safe_dump({'edges': E}, f, sort_keys=False, default_flow_style=False, width=112, allow_unicode=True)
print(len(E), 'edges')
