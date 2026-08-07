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
 id='primary_cilium_chondrocyte', name='Primary cilium of the growth plate chondrocyte', type='tissue_structure',
 aliases=['chondrocyte primary cilium'],
 summary=(
  "Growth plate chondrocytes carry a single non-motile primary cilium that acts as the compartment in "
  "which Hedgehog signal transduction occurs: PTCH1 leaves and SMO enters the ciliary membrane on ligand "
  "binding, and GLI processing depends on intraflagellar transport along the axoneme. Removing the cilium "
  "genetically therefore removes IHH responsiveness without removing IHH. Ift88 deletion in limb "
  "mesenchyme shortens the proximodistal axis and disrupts endochondral bone formation through loss of Ihh "
  "signalling, in addition to polydactyly from disturbed SHH patterning (Haycraft 2007, mouse). Cartilage "
  "Kif3a deletion abolishes the normal zonal organisation by postnatal day 7 - proliferative and "
  "hypertrophic zones are replaced by cells with strong Col2a1 but almost no Ihh, Col10a1, Vegfa, Mmp13 or "
  "Sp7 - while hedgehog signalling paradoxically INCREASES and spreads in the adjacent perichondrium, "
  "producing ectopic cartilage and excessive intramembranous ossification (Koyama 2007, mouse). The "
  "cilium's importance is thus topological: it does not merely amplify Hedgehog, it confines it. Human "
  "evidence is the ciliopathy skeletal dysplasias (Jeune, Ellis-van Creveld, short-rib polydactyly), which "
  "are among the strongest human anchors in this layer."),
 localization=["mouse growth plate, all zones: cilia present and required (haycraft2007, koyama2007)",
               "human growth plate: inferred from ciliopathy dysplasias; direct ultrastructural zonal survey not identified"],
 human_evidence='indirect',
 human_evidence_note='Human ciliopathy genes (IFT80, EVC, EVC2) cause defined chondrodysplasias, but no human growth plate cilium morphometry was located.',
 species_basis=['mouse','human'], translation_risk='moderate',
 translation_risk_reason='Mechanism is mouse; human evidence is germline ciliopathy phenotypes without physeal tissue analysis.',
 confidence='B',
 key_refs=[
  dict(ref_id='haycraft2007', pmid='17166921', first_author='Haycraft CJ', year=2007, type='primary',
       one_line_finding='Mesenchymal Ift88 deletion shortens the proximodistal limb axis by disrupting Ihh signalling during endochondral bone formation.'),
  dict(ref_id='koyama2007', pmid='17507416', first_author='Koyama E', year=2007, type='primary',
       one_line_finding='Cartilage Kif3a deletion destroys zonal organisation and lowers hedgehog signalling inside the plate while raising it in the perichondrium.'),
  dict(ref_id='beales2007', pmid='17468754', first_author='Beales PL', year=2007, type='primary',
       one_line_finding='IFT80 mutations cause human Jeune asphyxiating thoracic dystrophy, the first IFT protein linked to human disease.'),
 ],
 open_questions=['g_l3rest_014'],
))

N.append(dict(
 id='ift88_protein', name='IFT88', type='protein', aliases=['polaris','Tg737','intraflagellar transport 88'],
 summary=(
  "IFT88 is a core IFT-B complex subunit required to build and maintain the ciliary axoneme; null alleles "
  "cause mid-gestation lethality, so limb function was established with a conditional allele. Disrupting "
  "cilia in limb MESENCHYME with conditional Ift88 deletion causes extensive polydactyly with loss of "
  "anteroposterior digit patterning (aberrant SHH pathway activity) and shortening of the proximodistal "
  "axis attributable to disrupted IHH signalling during endochondral bone formation; deleting cilia in "
  "limb ECTODERM has no overt patterning effect, localising the requirement to the mesenchymal lineage "
  "(Haycraft 2007, mouse). Ift88-mutant limbs also develop ectopic perichondrium-derived chondrocyte-like "
  "domains that are not seen in Ihh mutants, so cilium loss is not simply equivalent to Hedgehog loss. "
  "Human IFT88 variants have been reported in ciliopathy cohorts but IFT88 is not an established human "
  "chondrodysplasia gene, and no human growth plate IFT88 measurement exists."),
 localization=["mouse limb mesenchyme/growth plate: functionally required (haycraft2007)","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='IFT88 is not an established human skeletal dysplasia gene; no human growth plate data.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse conditional genetics only; the human ciliopathy anchor is IFT80/EVC, not IFT88.',
 confidence='C',
 key_refs=[
  dict(ref_id='haycraft2007', pmid='17166921', first_author='Haycraft CJ', year=2007, type='primary',
       one_line_finding='Conditional Ift88 deletion in limb mesenchyme, but not ectoderm, causes polydactyly and proximodistal shortening via Shh and Ihh disruption.'),
 ],
))

N.append(dict(
 id='ift80_protein', name='IFT80', type='protein', aliases=['intraflagellar transport 80','WDR56'],
 summary=(
  "IFT80 is an IFT-B subunit and the first intraflagellar transport protein linked to human disease: "
  "hypomorphic IFT80 mutations cause a subset of Jeune asphyxiating thoracic dystrophy, an autosomal "
  "recessive chondrodysplasia with a constricted thoracic cage, short ribs, and often polydactyly, retinal "
  "degeneration and cystic kidney disease; ift80 knockdown gives cystic kidneys in zebrafish and short or "
  "absent cilia in Tetrahymena (Beales 2007). IFT80 is predominantly expressed in growth plate "
  "chondrocytes, and silencing it in mouse stromal cells impairs cilium formation and chondrogenic "
  "differentiation with lower collagen II and aggrecan; the deficit is caused by simultaneously "
  "DOWN-regulated Hedgehog and UP-regulated WNT signalling, and is rescued by GLI2 overexpression (Wang "
  "2013, mouse cells). Inducible Col2a1-CreER deletion of Ift80 shortens limbs when induced embryonically "
  "and, when induced postnatally, produces stunted growth with a shortened growth plate but THICKENED "
  "articular cartilage - opposite directions in the two cartilages of the same bone (Yuan 2015, mouse). "
  "IFT80 is therefore the best-anchored cilium node in this layer, with both human loss-of-function and "
  "mouse conditional genetics."),
 localization=["mouse growth plate chondrocytes: predominant expression site (wang2013)",
               "human: inferred from Jeune asphyxiating thoracic dystrophy (beales2007)"],
 human_evidence='direct',
 human_evidence_note='Biallelic hypomorphic IFT80 mutations cause human Jeune asphyxiating thoracic dystrophy with short ribs and short limbs.',
 species_basis=['human','mouse'], translation_risk='low',
 translation_risk_reason='Human recessive chondrodysplasia and mouse conditional deletion agree on the direction of the growth defect.',
 confidence='A',
 key_refs=[
  dict(ref_id='beales2007', pmid='17468754', first_author='Beales PL', year=2007, type='primary',
       one_line_finding='IFT80 mutations underlie a subset of human Jeune asphyxiating thoracic dystrophy.'),
  dict(ref_id='wang2013', pmid='23333501', first_author='Wang C', year=2013, type='primary',
       one_line_finding='IFT80 silencing impairs ciliogenesis and chondrogenesis by lowering Hedgehog and raising Wnt activity; GLI2 overexpression rescues it.'),
  dict(ref_id='yuan2015', pmid='26098911', first_author='Yuan X', year=2015, type='primary',
       one_line_finding='Inducible chondrocyte Ift80 deletion shortens the growth plate but thickens articular cartilage in postnatal mice.'),
 ],
 open_questions=['g_l3rest_014'],
))

N.append(dict(
 id='kif3a_protein', name='KIF3A', type='protein', aliases=['kinesin family member 3A','kinesin-II subunit'],
 summary=(
  "KIF3A is a subunit of heterotrimeric kinesin-II, the anterograde IFT motor; without it, cilia are not "
  "built. Cartilage-restricted Kif3a deletion in mouse produces cranial base growth retardation and "
  "progressive synchondrosis failure: by postnatal day 7 the mutant growth plate has lost identifiable "
  "proliferative and hypertrophic zones and is instead composed of cells with strong Col2a1 but barely "
  "detectable Ihh, Col10a1, Vegfa, Mmp13 and Sp7 (Koyama 2007). The informative part is the topology of "
  "the signalling defect: hedgehog readouts (Ptch1, Gli1, syndecan-3) are LOW inside the mutant plate but "
  "HIGHER and spatially spread throughout the adjacent perichondrium, and this is accompanied by excessive "
  "intramembranous ossification along the perichondrial border and ectopic cartilage masses - a "
  "combination that cartilage Ihh deletion does not reproduce. The cilium therefore restricts where "
  "Hedgehog acts, not only whether it acts. There is no human KIF3A skeletal dysplasia."),
 localization=["mouse growth plate and synchondrosis: functionally required (koyama2007)","human growth plate: unconfirmed"],
 human_evidence='absent',
 human_evidence_note='No human KIF3A skeletal phenotype; human KIF3A associations are with atopic disease.',
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason='Mouse conditional genetics only, and the reported site is the cranial base synchondrosis rather than a long-bone physis.',
 confidence='C',
 key_refs=[
  dict(ref_id='koyama2007', pmid='17507416', first_author='Koyama E', year=2007, type='primary',
       one_line_finding='Cartilage Kif3a deletion abolishes growth plate zonation and inverts the spatial distribution of hedgehog signalling between cartilage and perichondrium.'),
  dict(ref_id='haycraft2007', pmid='17166921', first_author='Haycraft CJ', year=2007, type='primary',
       one_line_finding='Independent IFT mutant confirming that cilium loss disrupts Ihh-dependent endochondral growth.'),
 ],
))

N.append(dict(
 id='evc_evc2_complex', name='EVC-EVC2 complex', type='protein', aliases=['EVC','EVC2','LIMBIN','EvC zone complex'],
 summary=(
  "EVC and EVC2 form an obligate complex localised to a discrete compartment at the base of the primary "
  "cilium, the 'EvC zone'. Evc-null mice reproduce an Ellis-van Creveld-like syndrome with short ribs, "
  "short limbs and dental abnormalities; their growth plates show delayed bone collar formation and "
  "ADVANCED chondrocyte maturation, Ihh expression is normal but the Ihh target genes Ptch1 and Gli1 are "
  "markedly reduced, cilia are present and Gli3 processing is normal - so the lesion is downstream of SMO "
  "and independent of ciliogenesis itself (Ruiz-Perez 2007, mouse). Dorn 2012 supplies the biochemistry: "
  "Hedgehog agonists promote a SMO-EVC2 association restricted to the EvC zone, and EVC2 mutants that "
  "still enter cilia but are displaced from that zone act as dominant inhibitors, blocking signalling "
  "between SMO and PKA/SUFU before GLI activation. In human, EVC mutations cause recessive Ellis-van "
  "Creveld syndrome (short limbs, short ribs, postaxial polydactyly, dysplastic nails and teeth, "
  "congenital heart defect in about 60%) and heterozygous missense alleles cause dominant Weyers "
  "acrodental dysostosis, an allelic milder condition (Ruiz-Perez 2000). This node is the direct "
  "mechanical link between the cilium subsystem and the IHH subsystem."),
 quantitative=[
  dict(parameter='Congenital cardiac defect frequency in Ellis-van Creveld syndrome',
       value='60', unit='% of affected individuals', conditions='clinical series across Amish and non-Amish pedigrees',
       species='human', source_ref='ruizperez2000', uncertainty='literature figure quoted in the source; no CI given'),
 ],
 localization=["mouse chondrocyte cilium base: confirmed by antibody staining (ruizperez2007)",
               "EvC zone at ciliary base: confirmed biochemically (dorn2012)",
               "human growth plate: inferred from Ellis-van Creveld phenotype"],
 human_evidence='direct',
 human_evidence_note='EVC and EVC2 mutations cause human Ellis-van Creveld syndrome (recessive) and Weyers acrodental dysostosis (dominant).',
 species_basis=['human','mouse'], translation_risk='low',
 translation_risk_reason='Human recessive and dominant allelic series, plus a concordant mouse null and cell-biological mechanism.',
 confidence='A',
 key_refs=[
  dict(ref_id='ruizperez2000', pmid='10700184', first_author='Ruiz-Perez VL', year=2000, type='primary',
       one_line_finding='EVC mutations cause Ellis-van Creveld syndrome; heterozygous missense alleles cause allelic Weyers acrodental dysostosis.'),
  dict(ref_id='ruizperez2007', pmid='17660199', first_author='Ruiz-Perez VL', year=2007, type='primary',
       one_line_finding='Evc localises to the base of the chondrocyte cilium and is required for Ihh-dependent Ptch1/Gli1 induction downstream of Smo.'),
  dict(ref_id='dorn2012', pmid='22981989', first_author='Dorn KV', year=2012, type='primary',
       one_line_finding='Hedgehog agonists drive a SMO-EVC2 complex confined to the EvC zone; EVC2 displaced from that zone is a dominant inhibitor.'),
 ],
 open_questions=['g_l3rest_014'],
))

# ---------------- H. CONVERGENCE ----------------
N.append(dict(
 id='pathway_convergence_node', name='Pathway convergence in the growth plate signalling network', type='process',
 aliases=['signalling convergence points, L3'],
 summary=(
  "Most L3 pathways are drawn as parallel cascades, but the genetics show they collapse onto a small "
  "number of shared targets, and it is the ratio at those targets - not the activity of any one pathway - "
  "that determines chondrocyte behaviour. Four convergence points are supported by primary data, each "
  "receiving three or more distinct upstream inputs. (1) SOX9 receives inputs from Notch (RBPJ-dependent "
  "suppression, genetically demonstrated by rescue of the Rbpj-mutant phenotype with Sox9 heterozygosity; "
  "Kohn 2015), from WNT (mutual antagonism with beta-catenin; Akiyama 2004, Topol 2009), from the cilium "
  "via Hedgehog (IFT80 loss lowers Hh and raises Wnt and thereby blocks chondrogenesis; Wang 2013), and "
  "from metabolism (SOX9 drives GLS1 and the resulting acetyl-CoA sustains its own regulon; Stegen 2020). "
  "(2) RUNX2 is the hypertrophy licence and is restrained by HDAC4 (Vega 2004), by ZFP521 downstream of "
  "PTHrP (Correa 2010) and by SOX9 (Dy 2012), while it is promoted by beta-catenin-dependent maturation "
  "(Dao 2012) and by MEF2C (Nishimori 2019); RUNX2 in turn transcribes Ihh directly (Yoshida 2004), "
  "feeding back into the loop that regulates it. (3) beta-catenin integrates canonical WNT, SOX9 "
  "antagonism, PTHrP (which it inhibits to initiate hypertrophy; Guo 2009) and cilium-dependent Hedgehog "
  "tone (Wang 2013). (4) HDAC4 nuclear localisation is the physical convergence of PTHrP-PKA-SIK3 "
  "phosphorylation control (Nishimori 2021), PP2A-dependent dephosphorylation (Kozhemyakina 2009) and "
  "MEF2C/RUNX2 availability (Arnold 2007) - one protein's address in the cell encodes the output of an "
  "entire endocrine loop. The practical consequence is that single-pathway therapeutic reasoning in the "
  "growth plate is unreliable: CNP/FGFR3 modulation, Hedgehog agonism and WNT modulation all terminate on "
  "these same four nodes."),
 localization=["mouse PZ/PHZ/HZ: all four convergence points demonstrated in mouse growth plate or chondrocytes",
               "human growth plate: unconfirmed - no human tissue study has measured two or more of these nodes simultaneously"],
 human_evidence='absent',
 human_evidence_note=("No human growth plate study has measured multiple convergence-point activities in the same tissue; "
  "the convergence structure is assembled from separate mouse experiments."),
 species_basis=['mouse'], translation_risk='high',
 translation_risk_reason=("This node is a synthesis across mouse experiments performed in different genetic backgrounds, "
  "ages and skeletal sites; convergence demonstrated pairwise is not the same as convergence demonstrated jointly."),
 confidence='E',
 key_refs=[
  dict(ref_id='kohn2015', pmid='26558140', first_author='Kohn A', year=2015, type='primary',
       one_line_finding='Genetic epistasis places SOX9 downstream of RBPJ-dependent Notch for the onset of chondrocyte maturation.'),
  dict(ref_id='akiyama2004', pmid='15132997', first_author='Akiyama H', year=2004, type='primary',
       one_line_finding='SOX9 and beta-catenin are reciprocal antagonists whose ratio determines the chondrocyte phenotype.'),
  dict(ref_id='wang2013', pmid='23333501', first_author='Wang C', year=2013, type='primary',
       one_line_finding='Loss of the ciliary protein IFT80 simultaneously lowers Hedgehog and raises Wnt output in chondrogenic cells.'),
  dict(ref_id='dy2012', pmid='22421045', first_author='Dy P', year=2012, type='primary',
       one_line_finding='SOX9 restrains both Runx2 expression and beta-catenin signalling in growth plate chondrocytes.'),
  dict(ref_id='nishimori2021', pmid='33148508', first_author='Nishimori S', year=2021, type='primary',
       one_line_finding='PTHrP-PKA-SIK3-HDAC4 phosphorylation converts an endocrine signal into the nuclear/cytoplasmic address of a single corepressor.'),
  dict(ref_id='yoshida2004', pmid='15107406', first_author='Yoshida CA', year=2004, type='primary',
       one_line_finding='RUNX2 binds the Ihh promoter directly, closing a feedback loop from the hypertrophy licence back onto the IHH/PTHrP circuit.'),
  dict(ref_id='stegen2020', pmid='32470321', first_author='Stegen S', year=2020, type='primary',
       one_line_finding='SOX9 sets its own nutrient flux through GLS1, making metabolism part of the convergence rather than a downstream consequence.'),
 ],
 open_questions=['g_l3rest_012','g_l3rest_015'],
))

for n in N: w(n)
print(len(N), 'nodes')
