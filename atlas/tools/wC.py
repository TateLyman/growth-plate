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

# ---------------- C. NOTCH ----------------
N.append(dict(
 id='notch_signaling_chondrocyte', name='Notch signalling in chondrocytes', type='pathway',
 summary=(
  "Ligand binding releases the Notch intracellular domain (NICD) by gamma-secretase cleavage; NICD enters "
  "the nucleus and converts RBPJ from repressor to activator. In cartilage the pathway is required at two "
  "separable steps and its sign depends on which step is examined. Forced NICD expression in the mouse "
  "chondrocyte lineage reduces cartilage precursor proliferation and blocks hypertrophic differentiation, "
  "while chondrocyte-lineage Rbpj deletion increases proliferation and increases hypertrophic chondrocyte "
  "number (Mead 2009) - so Notch restrains both proliferation and, in the gain-of-function direction, "
  "hypertrophy. Kohn 2015 resolves the mechanism genetically: Notch controls the ONSET of maturation "
  "through SOX9 (the Rbpj-mutant phenotype is rescued by removing one Sox9 allele), whereas Notch control "
  "of TERMINAL maturation is SOX9-independent. Hosaka 2013 shows the terminal arm operates through HES1 "
  "and demonstrates NICD1/2 nuclear translocation in human osteoarthritic articular chondrocytes, the only "
  "human chondrocyte data in this subsystem. Notch activity has never been mapped by zone in a human "
  "growth plate."),
 localization=[
  "mouse PHZ/HZ: RBPJ-dependent activity required for onset and terminal maturation (mead2009, kohn2015)",
  "human articular chondrocyte (OA): NICD1/NICD2 nuclear translocation confirmed (hosaka2013)",
  "human growth plate: unconfirmed"],
 human_evidence='indirect',
 human_evidence_note=("NICD nuclear translocation has been shown in human OA articular chondrocytes, and NOTCH2 "
  "gain-of-function causes human Hajdu-Cheney syndrome; neither is a growth plate measurement."),
 species_basis=['mouse','human'], translation_risk='moderate',
 translation_risk_reason='Mechanistic genetics are mouse; the human observations are in diseased articular, not physeal, cartilage.',
 confidence='B',
 key_refs=[
  dict(ref_id='mead2009', pmid='19590010', first_author='Mead TJ', year=2009, type='primary',
       one_line_finding='Chondrocyte NICD gain of function blocks hypertrophy; Rbpj deletion increases proliferation and hypertrophic chondrocyte number.'),
  dict(ref_id='kohn2015', pmid='26558140', first_author='Kohn A', year=2015, type='primary',
       one_line_finding='Notch controls onset of chondrocyte maturation SOX9-dependently and terminal maturation SOX9-independently.'),
  dict(ref_id='hosaka2013', pmid='23319657', first_author='Hosaka Y', year=2013, type='primary',
       one_line_finding='RBPJ-dependent Notch drives terminal endochondral ossification via HES1; NICD1/2 translocate in human OA chondrocytes.'),
  dict(ref_id='simpson2011', pmid='21378985', first_author='Simpson MA', year=2011, type='primary',
       one_line_finding='Truncating NOTCH2 mutations that stabilise NICD cause human Hajdu-Cheney syndrome with acro-osteolysis and bone loss.'),
 ],
 open_questions=['g_l3rest_009'],
))

N.append(dict(
 id='rbpj_tf', name='RBPJ', type='protein', aliases=['RBP-Jkappa','CSL','RBPSUH'],
 summary=(
  "RBPJ is the DNA-binding transcription factor through which all four Notch receptors signal; without "
  "NICD it recruits corepressors, with NICD it recruits MAML and activates transcription. Because it is a "
  "single obligatory node, Rbpj deletion is the cleanest available Notch-off experiment. Prx1-Cre and "
  "Sox9-Cre driven Rbpj deletion in mouse limb mesenchyme/chondroprogenitors impairs the terminal stage of "
  "endochondral ossification and raises SOX9 (Kohn 2015, Hosaka 2013), while Col2a1-CreERT-driven deletion "
  "in adult articular cartilage confers resistance to surgically induced osteoarthritis (Hosaka 2013). "
  "Deleting Rbpj in mesenchymal cells produces a rickets-like phenotype in mouse, indicating the "
  "requirement extends into mineralisation as well as differentiation (Gao 2022). RBPJ-independent Notch "
  "outputs exist in cartilage, so an Rbpj-null phenotype is a lower bound on Notch function, not a "
  "complete one. No human RBPJ growth plate data exist; human RBPJ haploinsufficiency causes Adams-Oliver "
  "syndrome, which is not primarily a physeal disorder."),
 localization=["mouse chondroprogenitor and growth plate: functionally required (kohn2015, hosaka2013)",
               "human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='Human RBPJ variants cause Adams-Oliver syndrome; no human growth plate RBPJ data.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Conditional mouse genetics only; the human RBPJ phenotype is vascular/limb-terminal rather than physeal.',
 confidence='C',
 key_refs=[
  dict(ref_id='kohn2015', pmid='26558140', first_author='Kohn A', year=2015, type='primary',
       one_line_finding='Prx1Cre;Rbpj-null limb phenotype is rescued by Sox9 heterozygosity, placing SOX9 downstream of RBPJ for maturation onset.'),
  dict(ref_id='hosaka2013', pmid='23319657', first_author='Hosaka Y', year=2013, type='primary',
       one_line_finding='Sox9-Cre Rbpj deletion impairs terminal endochondral ossification; adult deletion protects against osteoarthritis.'),
  dict(ref_id='gao2022', pmid='35694720', first_author='Gao Y', year=2022, type='primary_abstract_only',
       one_line_finding='Deleting RBP-Jkappa in mesenchymal cells causes rickets-like changes in mouse.'),
 ],
))

N.append(dict(
 id='hes1_tf', name='HES1', type='protein', aliases=['hairy and enhancer of split 1'],
 summary=(
  "HES1 is a basic helix-loop-helix repressor and canonical RBPJ target. In chondrocytes it is the "
  "effector through which Notch drives the terminal stage of endochondral ossification: NICD with RBPJ "
  "induces Hes1, and Hes1 induction is required for the ossification phenotype (Hosaka 2013, mouse). "
  "Genetic dissection of the Notch target repertoire shows HES1 and HES5 suppress chondrogenesis and "
  "promote the onset of hypertrophy, with partial overlap between them, whereas HEY1 and HEYL have no "
  "discernible role in either process - so the Notch output in cartilage is carried by the HES and not the "
  "HEY branch (Rutkowski 2016, mouse). Only HES5, not HES1, directly regulates Sox9 transcription in that "
  "analysis, which separates the two paralogues mechanistically. HES1 is heavily used in other tissues as "
  "a Notch activity reporter; in the growth plate it is a functional node in its own right. No human "
  "growth plate HES1 data exist."),
 localization=["mouse PHZ/HZ: induced downstream of NICD-RBPJ (hosaka2013)","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human growth plate HES1 measurement or human HES1 skeletal phenotype.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse genetics and mouse chondrogenic cell lines only.',
 confidence='C',
 key_refs=[
  dict(ref_id='hosaka2013', pmid='23319657', first_author='Hosaka Y', year=2013, type='primary',
       one_line_finding='NICD/RBPJ stimulates endochondral ossification through induction of Hes1 in chondrocytes.'),
  dict(ref_id='rutkowski2016', pmid='27160681', first_author='Rutkowski TP', year=2016, type='primary',
       one_line_finding='HES1 and HES5 suppress chondrogenesis and promote hypertrophy onset; HEY1/HEYL do not, and only HES5 directly regulates Sox9.'),
 ],
))

# ---------------- D. NUTRIENT SENSING ----------------
N.append(dict(
 id='mtorc1_chondrocyte', name='mTORC1 signalling in chondrocytes', type='pathway',
 aliases=['mechanistic target of rapamycin complex 1, growth plate'],
 summary=(
  "mTORC1 (mTOR-RAPTOR-mLST8) integrates amino acid, growth factor and energy availability and sets "
  "biosynthetic capacity through S6K1 and 4E-BP1. In mouse limb cartilage mTORC1 signalling is active "
  "during development, and Prx1-Cre deletion of either mTor or Raptor sharply reduces embryonic skeletal "
  "growth with delayed hypertrophy and bone formation. The mechanism is specifically translational: "
  "proliferation and survival are NOT changed, but chondrocyte cell size and cartilage matrix amount fall, "
  "and metabolic labelling shows a reduced protein synthesis rate in Raptor-deficient chondrocytes (Chen "
  "and Long 2014). This makes mTORC1 the node that converts nutrient supply into the cell-size component "
  "of longitudinal growth, distinct from the proliferation component set by IHH/PTHrP and FGFR3. mTORC1 "
  "also promotes limb bud cell growth and chondrogenesis at an earlier stage (Jiang 2017, mouse), and "
  "rapamycin blunts chondrocyte differentiation in vitro (Phornphutkul 2008). No study has measured "
  "phospho-S6 or phospho-4E-BP1 zonally in human growth plate tissue, so the assumption that human "
  "hypertrophic chondrocytes are the high-mTORC1 compartment is untested."),
 localization=[
  "mouse limb cartilage: mTORC1 activity confirmed during development (chen2014)",
  "human growth plate, zonal phospho-S6/phospho-4E-BP1: unmeasured"],
 human_evidence='absent',
 human_evidence_note=("No human growth plate mTORC1 activity measurement; the closest human data are systemic - "
  "growth retardation in children on mTOR inhibitors - which is not zone-resolved."),
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse conditional genetics plus rodent cell lines; no human tissue read-out at any zone.',
 confidence='C',
 key_refs=[
  dict(ref_id='chen2014', pmid='24948603', first_author='Chen J', year=2014, type='primary',
       one_line_finding='mTOR or Raptor deletion in mouse limb cartilage reduces chondrocyte size and matrix via lower protein synthesis, not lower proliferation.'),
  dict(ref_id='jiang2017', pmid='27606668', first_author='Jiang M', year=2017, type='primary',
       one_line_finding='mTORC1 signalling promotes limb bud cell growth and chondrogenesis in mouse.'),
  dict(ref_id='phornphutkul2008', pmid='18265001', first_author='Phornphutkul C', year=2008, type='primary',
       one_line_finding='mTOR signalling contributes to chondrocyte differentiation in vitro.'),
  dict(ref_id='chen2018', pmid='29423330', first_author='Chen J', year=2018, type='review',
       one_line_finding='Synthesis of mTOR signalling in skeletal development, used here as an index to primaries.'),
 ],
 open_questions=['g_l3rest_010'],
))

N.append(dict(
 id='raptor_protein', name='RAPTOR (RPTOR)', type='protein', aliases=['regulatory-associated protein of mTOR','RPTOR'],
 summary=(
  "RAPTOR is the defining scaffold subunit of mTORC1; it presents TOS-motif substrates such as S6K1 and "
  "4E-BP1 to the mTOR kinase and is what distinguishes mTORC1 from RICTOR-containing mTORC2. Deleting "
  "Raptor in mouse limb mesenchyme phenocopies mTor deletion in cartilage - severe reduction of embryonic "
  "skeletal growth, delayed chondrocyte hypertrophy, smaller chondrocytes and less matrix - and metabolic "
  "labelling in Raptor-deficient chondrocytes shows the deficit is in the rate of protein synthesis "
  "(Chen and Long 2014). Because the mTor-null and Raptor-null cartilage phenotypes match, the skeletal "
  "growth requirement is attributable to mTORC1 rather than mTORC2. Upstream, RHEB1 is required for the "
  "same axis: Rheb1 loss impairs limb growth through chondrogenesis in mouse (Zhang 2024). No human "
  "growth plate RAPTOR data exist."),
 localization=["mouse limb cartilage: functionally required (chen2014)","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human growth plate RAPTOR measurement or human RPTOR skeletal phenotype.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse conditional knockout only.',
 confidence='C',
 key_refs=[
  dict(ref_id='chen2014', pmid='24948603', first_author='Chen J', year=2014, type='primary',
       one_line_finding='Raptor deletion in mouse limb cartilage reduces protein synthesis rate, chondrocyte size and skeletal growth.'),
  dict(ref_id='zhang2024', pmid='38253890', first_author='Zhang Y', year=2024, type='primary',
       one_line_finding='Rheb1, the mTORC1 activator, is required for mouse limb growth through chondrogenesis in the growth plate.'),
 ],
))

N.append(dict(
 id='tsc1_tsc2', name='TSC1-TSC2 complex', type='protein', aliases=['tuberous sclerosis complex','hamartin-tuberin'],
 summary=(
  "TSC1-TSC2 is the GTPase-activating complex that keeps RHEB in its GDP-bound state and therefore holds "
  "mTORC1 off; growth-factor signalling through AKT and ERK inactivates it. In the growth plate the "
  "requirement for its downstream target is established from the opposite direction: RHEB1 loss impairs "
  "chondrogenesis and limb growth in mouse (Zhang 2024), and Raptor/mTor loss reduces chondrocyte size and "
  "matrix output (Chen and Long 2014). The corresponding chondrocyte-restricted Tsc1 or Tsc2 deletion - "
  "the experiment that would show what constitutive mTORC1 activation does to a growth plate - is not "
  "represented by a clean published growth-plate phenotype; the Tsc1 skeletal literature is dominated by "
  "osteoblast-lineage drivers (Dmp1-Cre, Osx-Cre), which report increased bone mass rather than a physeal "
  "read-out. In human, TSC1/TSC2 loss of function causes tuberous sclerosis complex, which has sclerotic "
  "bone lesions but no characteristic stature phenotype, and children treated with mTOR inhibitors for TSC "
  "provide the only human pharmacological probe. This node is therefore inferentially placed rather than "
  "directly evidenced."),
 localization=["growth plate zonal distribution: unmeasured in mouse and human"],
 human_evidence='indirect',
 human_evidence_note='Human TSC1/TSC2 loss causes tuberous sclerosis complex without an established growth plate phenotype; no physeal measurement exists.',
 species_basis=['mouse','human'], translation_risk='high',
 translation_risk_reason='The chondrocyte-specific genetic experiment has not been done; the node rests on downstream (RHEB/RAPTOR) inference.',
 confidence='E',
 key_refs=[
  dict(ref_id='zhang2024', pmid='38253890', first_author='Zhang Y', year=2024, type='primary',
       one_line_finding='Rheb1, the direct target of TSC1-TSC2 GAP activity, is required for limb growth via growth plate chondrogenesis.'),
  dict(ref_id='chen2014', pmid='24948603', first_author='Chen J', year=2014, type='primary',
       one_line_finding='Defines what loss of mTORC1 output does in cartilage, the phenotype TSC1-TSC2 loss should invert.'),
 ],
 open_questions=['g_l3rest_010'],
))

N.append(dict(
 id='amino_acid_sensing_chondrocyte', name='Amino acid sensing in chondrocytes', type='process',
 aliases=['glutamine metabolism, chondrocyte'],
 summary=(
  "Growth plate chondrocytes are avascular, highly anabolic and therefore acutely dependent on amino acid "
  "supply. Stegen 2020 shows the sensing is not merely permissive but identity-forming and runs as a "
  "feedforward loop: SOX9 raises glutamine consumption and glutaminase 1 (GLS1) levels, and GLS1 activity "
  "is then required for chondrocyte function through three separable routes - glutamate-dehydrogenase-"
  "derived acetyl-CoA for histone acetylation at chondrogenic genes, transaminase-derived aspartate for "
  "proliferation and matrix synthesis, and glutamine-derived glutathione for survival in the avascular "
  "core (mouse and cell-based). This is a direct metabolic-to-transcriptional convergence: the master "
  "chondrogenic transcription factor sets its own nutrient flux, and the flux is required to keep the "
  "chromatin state that supports the transcription factor. mTORC1 is the canonical amino-acid-responsive "
  "kinase in the same cell and controls translational output (Chen and Long 2014), but the two axes have "
  "not been tested against each other in the growth plate. No human growth plate metabolite measurement "
  "exists."),
 localization=["mouse growth plate: GLS1 dependence demonstrated (stegen2020)","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human growth plate amino acid or glutamine flux measurement.',
 species_basis=['mouse','in_vitro_animal_cell'], translation_risk='high',
 translation_risk_reason='Mouse genetics plus tracer metabolomics in cultured cells; human physeal metabolism is unmeasured.',
 confidence='C',
 key_refs=[
  dict(ref_id='stegen2020', pmid='32470321', first_author='Stegen S', year=2020, type='primary',
       one_line_finding='SOX9 drives glutamine uptake and GLS1, and GLS1 flux is required for chondrocyte epigenetic state, proliferation and survival.'),
  dict(ref_id='chen2014', pmid='24948603', first_author='Chen J', year=2014, type='primary',
       one_line_finding='mTORC1 converts nutrient status into chondrocyte protein synthesis rate and cell size.'),
 ],
 open_questions=['g_l3rest_010'],
))

N.append(dict(
 id='autophagy_chondrocyte', name='Autophagy in growth plate chondrocytes', type='process',
 summary=(
  "Autophagy is the lysosomal recycling pathway that maintains cells under nutrient and oxygen "
  "restriction - exactly the condition of the avascular mid-plate. Cartilage-specific deletion of Atg5 or "
  "Atg7 in mouse (Col2a1-Cre) causes growth retardation with increased chondrocyte death and reduced "
  "proliferation, and the effect is mild rather than catastrophic, i.e. autophagy is a survival buffer "
  "rather than an essential differentiation step (Vuppalapati 2015). The same study provides one of the "
  "few pieces of direct human evidence in this layer: pharmacological autophagy inhibition with "
  "bafilomycin A1 or 3-methyladenine promoted cell death in cultured slices of HUMAN growth plate tissue, "
  "and impaired growth of mouse metatarsal explants with caspase-3 and caspase-9 processing and "
  "cytochrome c release. Upstream, autophagic flux in chondrocytes is set by matrix sulfation state and "
  "FGF signalling: proteoglycan desulfation in the diastrophic dysplasia sulfate transporter mutant "
  "changes autophagy efficiency and FGF signalling extent during endochondral ossification (Settembre "
  "2008, mouse). mTORC1 is the canonical autophagy suppressor but the mTORC1-autophagy link has not been "
  "tested genetically in growth plate chondrocytes."),
 localization=[
  "human growth plate (cultured tissue slices): autophagy inhibition causes chondrocyte death (vuppalapati2015)",
  "mouse growth plate: Atg5/Atg7 required for chondrocyte survival (vuppalapati2015)"],
 human_evidence='direct',
 human_evidence_note='Autophagy inhibitors killed chondrocytes in cultured human growth plate tissue slices - an ex vivo human interventional result.',
 species_basis=['mouse','human','in_vitro_animal_cell'], translation_risk='moderate',
 translation_risk_reason='Human data are ex vivo pharmacology on explanted tissue with non-specific inhibitors; the genetics are mouse.',
 confidence='B',
 key_refs=[
  dict(ref_id='vuppalapati2015', pmid='26077727', first_author='Vuppalapati KK', year=2015, type='primary',
       one_line_finding='Chondrocyte Atg5/Atg7 deletion causes mild mouse growth retardation with caspase-dependent death; autophagy inhibitors kill chondrocytes in human growth plate slices.'),
  dict(ref_id='settembre2008', pmid='18832069', first_author='Settembre C', year=2008, type='primary',
       one_line_finding='Proteoglycan desulfation sets the efficiency of chondrocyte autophagy and the extent of FGF signalling in mouse.'),
 ],
 open_questions=['g_l3rest_010'],
))

# ---------------- E. HYPOXIA ----------------
N.append(dict(
 id='hif1a_chondrocyte', name='HIF1A in chondrocytes', type='protein', aliases=['hypoxia-inducible factor 1 alpha'],
 summary=(
  "HIF1A is the oxygen-labile subunit of HIF-1, hydroxylated by PHDs and destroyed by the VHL ubiquitin "
  "ligase when oxygen is available. Schipani 2001 provided the first evidence that the mammalian growth "
  "plate is developmentally hypoxic and, critically, that the hypoxia is in its INTERIOR rather than at "
  "its periphery; chondrocyte-restricted Hif1a deletion in mouse kills cells in that interior, lowers the "
  "CDK inhibitor p57 and raises BrdU incorporation, i.e. HIF1A enforces both survival and growth arrest. "
  "VEGF expression in the plate is only partly HIF1A-dependent: around dying cells VEGF rises "
  "HIF1A-independently and drives ectopic angiogenesis (Schipani 2001, mouse). Deleting the negative "
  "regulator Vhlh has the reciprocal effect - stabilised HIF1A, dwarfism, reduced proliferation, increased "
  "matrix - and the Vhlh;Hif1a double null resembles the Hif1a single null, placing HIF1A downstream "
  "(Pfander 2004, mouse). Human evidence is absent: there is no HIF1A staining series or oxygen "
  "measurement from human growth plate reported."),
 localization=[
  "mouse growth plate interior: hypoxic and HIF1A-dependent for survival (schipani2001)",
  "human growth plate: unconfirmed - no published HIF1A zonal staining series"],
 human_evidence='absent',
 human_evidence_note='No human growth plate HIF1A measurement; the human hypoxic-gradient claim is an extrapolation from mouse.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason=("Human growth plates are far thicker than mouse and vascularised differently at the "
  "epiphyseal cartilage canal level, so the diffusion geometry that produces the mouse gradient may not scale."),
 confidence='C',
 key_refs=[
  dict(ref_id='schipani2001', pmid='11691837', first_author='Schipani E', year=2001, type='primary',
       one_line_finding='The developing mouse growth plate is hypoxic in its interior; Hif1a-null interior chondrocytes die and lose p57-dependent growth arrest.'),
  dict(ref_id='pfander2004', pmid='15128677', first_author='Pfander D', year=2004, type='primary',
       one_line_finding='Vhlh deletion stabilises HIF1A and causes dwarfism; the Vhlh;Hif1a double null resembles the Hif1a null.'),
  dict(ref_id='yao2020', pmid='32768687', first_author='Yao Q', year=2020, type='primary_abstract_only',
       one_line_finding='HIF1A-dependent suppression of mitochondrial oxygen consumption lowers intracellular hypoxia and is required for hypoxic chondrocyte survival.'),
 ],
 open_questions=['g_l3rest_011'],
))

N.append(dict(
 id='vhl_protein', name='VHL', type='protein', aliases=['von Hippel-Lindau tumour suppressor','pVHL'],
 summary=(
  "pVHL is the substrate-recognition component of the E3 ubiquitin ligase that destroys hydroxylated HIF "
  "alpha subunits; it is the oxygen-off switch of the pathway. Cartilage-wide conditional inactivation of "
  "Vhlh in mouse produces viable but severely dwarfed animals with a reduced chondrocyte proliferation "
  "rate, increased extracellular matrix and atypical enlarged cells in the resting zone, and HIF1A target "
  "genes are elevated as expected (Pfander 2004). The epistasis is explicit: newborns lacking both Vhlh "
  "and Hif1a in chondrocytes look essentially like Hif1a single nulls, so most of the Vhlh phenotype is "
  "accumulated HIF1A activity. This is the loss-of-brake counterpart to the Hif1a knockout and together "
  "they bracket the pathway in mouse. In human, germline VHL mutations cause von Hippel-Lindau disease "
  "(and the Chuvash R200W allele causes congenital polycythaemia) with no reported growth plate phenotype, "
  "so no human physeal evidence anchors this node."),
 localization=["mouse growth plate, all zones (Col2-driven deletion): confirmed functionally (pfander2004)",
               "human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='Human VHL disease has no described growth plate phenotype; no human physeal VHL measurement exists.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse conditional genetics only; the human VHL phenotype is tumour-predisposition and erythropoietic.',
 confidence='C',
 key_refs=[
  dict(ref_id='pfander2004', pmid='15128677', first_author='Pfander D', year=2004, type='primary',
       one_line_finding='Cartilage Vhlh deletion causes mouse dwarfism with reduced proliferation and increased matrix, epistatically upstream of HIF1A.'),
  dict(ref_id='schipani2001', pmid='11691837', first_author='Schipani E', year=2001, type='primary',
       one_line_finding='Defines the HIF1A-dependent survival/arrest programme that VHL loss constitutively activates.'),
 ],
))

N.append(dict(
 id='vegfa_growth_plate', name='VEGFA in the growth plate', type='protein',
 aliases=['vascular endothelial growth factor A'],
 summary=(
  "VEGFA couples the hypertrophic chondrocyte to the vasculature that will replace it. Sequestering VEGF "
  "with a soluble receptor chimera in growing mice suppresses blood vessel invasion of the hypertrophic "
  "cartilage, expands the hypertrophic zone, impairs trabecular bone formation and is reversible on "
  "withdrawal - a pharmacological, dose-reversible demonstration that vascular invasion is VEGF-gated "
  "(Gerber 1999, mouse). Genetically, Col2a1-Cre deletion of Vegfa delays vessel invasion of the primary "
  "ossification centre and delays removal of terminal hypertrophic chondrocytes, but it also causes "
  "massive death of epiphyseal and joint chondrocytes far from any vessel, indicating a direct "
  "chondrocyte-survival role and not only an angiogenic one (Zelzer 2004, mouse). The cell-death pattern "
  "closely resembles the Hif1a-null pattern and HIF1A-null epiphyseal chondrocytes make less VEGFA, "
  "placing HIF1A-VEGFA on one survival axis - though Schipani 2001 also documents HIF1A-independent VEGF "
  "induction around dying cells. Perichondrial Vegfa additionally controls perichondrial vascularity and "
  "osteoblast differentiation (Duan 2015, mouse). No human growth plate VEGFA measurement is available."),
 localization=["mouse HZ: confirmed - VEGFA from hypertrophic chondrocytes drives vessel invasion (gerber1999)",
               "mouse epiphyseal/joint chondrocytes: VEGFA required for survival (zelzer2004)",
               "human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human growth plate VEGFA data; anti-VEGF therapeutics are not used in growing children in a way that yields physeal read-outs.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse pharmacology and conditional genetics; human physeal vascular biology is undescribed at this level.',
 confidence='C',
 key_refs=[
  dict(ref_id='gerber1999', pmid='10371499', first_author='Gerber HP', year=1999, type='primary',
       one_line_finding='VEGF sequestration in growing mice blocks hypertrophic cartilage vascular invasion and expands the hypertrophic zone, reversibly.'),
  dict(ref_id='zelzer2004', pmid='15073147', first_author='Zelzer E', year=2004, type='primary',
       one_line_finding='Chondrocyte Vegfa deletion delays vascular invasion and causes massive epiphyseal chondrocyte death, phenocopying Hif1a loss.'),
  dict(ref_id='duan2015', pmid='25977369', first_author='Duan X', year=2015, type='primary_abstract_only',
       one_line_finding='Vegfa regulates perichondrial vascularity and osteoblast differentiation in mouse bone development.'),
 ],
))

N.append(dict(
 id='hypoxic_gradient_signaling', name='Hypoxic gradient across the growth plate', type='process',
 aliases=['oxygen gradient, physis'],
 summary=(
  "The standard model holds that oxygen falls from the vascularised epiphyseal and metaphyseal margins "
  "toward the avascular centre of the plate, and that this gradient patterns HIF1A activity, glycolytic "
  "metabolism and survival. The direct evidence for the gradient itself is thin and old: Brighton and "
  "Heppenstall 1971 measured oxygen tension with microelectrodes across zones of the epiphyseal plate, "
  "metaphysis and diaphysis in rats and rabbits, in vitro and in vivo. Every subsequent statement about a "
  "human growth plate oxygen gradient is inferred from HIF1A-dependent phenotypes, pimonidazole adduct "
  "staining or from that rodent measurement. Schipani 2001 established by HIF1A genetics that the mouse "
  "plate is hypoxic in its interior rather than its periphery, which is the correct topology but is a "
  "genetic inference, not an oxygen measurement. Chondrocytes also actively defend their own oxygenation: "
  "they synthesise haemoglobin into membraneless cytoplasmic condensates ('Hedy') under hypoxic control "
  "via KLF1 and independently of HIF1/2A, and deleting chondrocyte haemoglobin causes severe hypoxia, "
  "glycolytic shift and death in the cartilage centre (Zhang 2023, mouse) - so the tissue oxygen field is "
  "partly cell-autonomously buffered and cannot be predicted from diffusion geometry alone."),
 localization=["rat and rabbit epiphyseal plate: oxygen tension measured by microelectrode (brighton1971)",
               "mouse growth plate interior: hypoxic by HIF1A-dependent genetics (schipani2001)",
               "human growth plate: never measured directly"],
 human_evidence='absent',
 human_evidence_note='No direct measurement of oxygen tension in a human growth plate has been published; the human gradient is assumed.',
 species_basis=['rat','rabbit','mouse'], translation_risk='high',
 translation_risk_reason=("The only direct measurements are from rodent/lagomorph plates a fraction of the thickness of a "
  "human adolescent plate, so the diffusion distance - the key determinant - is not comparable."),
 confidence='D',
 pending_source='brighton1971',
 key_refs=[
  dict(ref_id='brighton1971', pmid='5580029', first_author='Brighton CT', year=1971, type='primary_abstract_only',
       one_line_finding='Oxygen tension was measured by microelectrode across epiphyseal plate zones, metaphysis and diaphysis in rats and rabbits.'),
  dict(ref_id='schipani2001', pmid='11691837', first_author='Schipani E', year=2001, type='primary',
       one_line_finding='The mouse growth plate is hypoxic in its interior, shown genetically rather than by oximetry.'),
  dict(ref_id='zhang2023', pmid='37794190', first_author='Zhang F', year=2023, type='primary',
       one_line_finding='Chondrocytes form haemoglobin condensates under KLF1 control, HIF-independently, and buffer their own oxygen supply.'),
 ],
 open_questions=['g_l3rest_011'],
))

for n in N: w(n)
print(len(N), 'nodes')
