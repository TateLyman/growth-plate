import yaml, os
D='atlas/nodes/L6_mechanobiology'
def w(n):
    n.setdefault('layer','L6'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    yaml.safe_dump(n,open(os.path.join(D,n['id']+'.yaml'),'w'),sort_keys=False,width=100,allow_unicode=True)
    print('wrote',n['id'])

w(dict(id='piezo1_channel', name='PIEZO1', type='protein', aliases=['Piezo1','FAM38A'],
summary=("PIEZO1 is the only mechanosensitive channel with loss-of-function evidence obtained inside the growth plate rather than in "
 "articular cartilage. Col2a1-Cre inactivation in mice produces near-absence of trabecular bone beneath the growth plate postnatally "
 "and multiple rib fractures adjacent to the physes by day 7, while linear skeletal growth is only mildly affected - so the channel is "
 "required for the bone that the plate produces more than for the plate's own output. Col10a1-Cre deletion restricted to hypertrophic "
 "chondrocytes gives an osteopenic phenotype with increased osteoclast number in the primary spongiosa, mediated by RANKL repression and "
 "OPG induction, without altering hypertrophic apoptosis or chondrocyte-to-osteoblast transdifferentiation. Under applied compression, "
 "PIEZO1 is upregulated in vertebral growth plate chondrocytes and drives GPX4 loss and ferroptosis; Col2a1-CreERT;Piezo1fl/fl deletion or "
 "local pharmacological blockade slowed scoliosis progression in mice. PIEZO1 colocalises with the primary cilium in mouse growth plate "
 "chondrocytes and its stress response requires IFT88. Human data are thin: increased PIEZO1 protein has been shown in cartilaginous zones "
 "of human osteophytes, but no study has localised PIEZO1 in human growth plate tissue."),
quantitative=[
 dict(parameter='rib fracture penetrance in chondrocyte-specific Piezo1 deletion', value='100', unit='% of animals at 7 days', conditions='Piezo1 Col2a1-Cre mice, fractures adjacent to growth plates', species='mouse', source_ref='brylka2024', uncertainty='n not extracted from abstract'),
 dict(parameter='compressive stress applied to induce PIEZO1 upregulation in vivo', value='10', unit='kPa', conditions='mouse caudal compression model, 8 weeks', species='mouse', source_ref='chen2025', uncertainty='device-applied nominal value'),
 dict(parameter='compressive stress applied to primary growth plate chondrocytes in vitro', value='100', unit='kPa', conditions='custom loading device, P5 mouse growth plate chondrocytes', species='mouse', source_ref='chen2025', uncertainty='nominal'),
 dict(parameter='cilia-positive chondrocytes after chloral hydrate disruption', value='97.2 -> 16.6', unit='%', conditions='mouse growth plate chondrocytes in vitro', species='mouse', source_ref='chen2025', uncertainty='p<0.001'),
],
localization=['mouse growth plate chondrocytes (all zones, Col2a1 domain): confirmed by conditional deletion phenotype (brylka2024)',
 'mouse hypertrophic zone: confirmed by Col10a1-Cre deletion phenotype (tschaffonmller2026)',
 'mouse growth plate chondrocyte primary cilium: colocalised with acetylated alpha-tubulin (chen2025)',
 'human osteophyte cartilage: PIEZO1 protein increased (brylka2024)',
 'human growth plate: unconfirmed - no localisation study located'],
human_evidence='absent',
human_evidence_note='The only human PIEZO1 protein data in cartilage come from osteophytes in osteoarthritis; PIEZO1 has not been localised or functionally tested in human physeal tissue.',
species_basis=['mouse'], translation_risk='high',
translation_risk_reason='Entirely conditional-knockout mouse biology; human physeal expression is unestablished and mice do not undergo epiphyseal fusion.',
confidence='C',
key_refs=[
 dict(ref_id='brylka2024', pmid='38395992', first_author='Brylka LJ', year=2024, type='primary', one_line_finding='Chondrocyte Piezo1 but not Piezo2 deletion abolished trabecular bone under the growth plate and caused peri-physeal rib fractures'),
 dict(ref_id='tschaffonmller2026', pmid='42157948', first_author='Tschaffon-Muller MEA', year=2026, type='primary', one_line_finding='Hypertrophic-chondrocyte Piezo1 deletion raised osteoclast number in the primary spongiosa via RANKL/OPG'),
 dict(ref_id='chen2025a', pmid='40714837', first_author='Chen F', year=2025, type='primary', one_line_finding='Compression-induced PIEZO1 drives GPX4 loss and ferroptosis in vertebral growth plate chondrocytes; deletion slowed scoliosis'),
 dict(ref_id='chen2025', pmid='41194970', first_author='Chen F', year=2025, type='primary', one_line_finding='PIEZO1 colocalises with the primary cilium in growth plate chondrocytes and requires IFT88 for its stress response'),
 dict(ref_id='chen2026', pmid='42082502', first_author='Chen F', year=2026, type='primary', one_line_finding='Simulated microgravity unloading reverses PIEZO1-overexpression-driven growth plate ossification'),
],
open_questions=['g_l6mech_007','g_l6mech_008']))

w(dict(id='piezo2_channel', name='PIEZO2', type='protein', aliases=['Piezo2','FAM38B'],
summary=("PIEZO2 is repeatedly listed as a growth plate mechanotransducer but the supporting experiments were done elsewhere. Chondrocyte-specific "
 "Piezo2 inactivation with Col2a1-Cre produced no growth plate or endochondral ossification phenotype and did not protect against surgically "
 "induced osteoarthritis, in the same study in which Piezo1 deletion did both. In inducible Aggrecan-Cre mice, Piezo2 deletion reduced pain "
 "behaviour and preserved activity after destabilisation of the medial meniscus but failed to protect cartilage, and separately reduced "
 "trabecular bone volume, thickness and density independent of injury - a bone rather than physis effect. The best-characterised PIEZO2 "
 "mechanism in skeletal tissue is neuronal: in dorsal root ganglion neurons, PIEZO2 activation by abnormal mechanical stress releases CGRP, "
 "which acts through RAMP1 on cartilage endplate cells to drive IL-6 and IL-1beta, degrading the endplate. No experiment has localised or "
 "deleted PIEZO2 in a growth plate with a growth-rate readout, and there is no human growth plate PIEZO2 data at all. Human PIEZO2 "
 "loss-of-function causes distal arthrogryposis and proprioceptive loss, with skeletal consequences that are plausibly secondary to absent "
 "fetal movement rather than to a chondrocyte-autonomous defect."),
quantitative=[
 dict(parameter='growth plate / endochondral phenotype in Piezo2 Col2a1-Cre mice', value='none detected', unit='qualitative', conditions='compared with the overt phenotype of Piezo1 Col2a1-Cre littermates', species='mouse', source_ref='brylka2024', uncertainty='negative result reported in abstract'),
 dict(parameter='trabecular bone volume, thickness and density in Acan-CreERT2 Piezo2 cKO', value='decreased', unit='qualitative (micro-CT)', conditions='independent of DMM injury, 28 weeks', species='mouse', source_ref='ely2025', uncertainty='effect sizes not reported in abstract'),
],
localization=['mouse articular chondrocytes: functional evidence (ely2025)','rat dorsal root ganglion innervating cartilage endplate: confirmed (xu2026)','mouse growth plate: no localisation study located','human growth plate: no data located'],
human_evidence='absent',
human_evidence_note='No human growth plate PIEZO2 expression or function data exist; human PIEZO2 phenotypes are neuromuscular and arthrogrypotic.',
species_basis=['mouse','rat'], translation_risk='high',
translation_risk_reason='The growth plate role is asserted by extension from articular cartilage and sensory neurons; the one direct test in the growth plate lineage was negative.',
confidence='D',
key_refs=[
 dict(ref_id='brylka2024', pmid='38395992', first_author='Brylka LJ', year=2024, type='primary', one_line_finding='Chondrocyte Piezo2 deletion produced no endochondral ossification phenotype, unlike Piezo1'),
 dict(ref_id='ely2025', pmid='40684207', first_author='Ely EV', year=2025, type='primary', one_line_finding='Piezo2 cKO reduced OA pain without protecting cartilage and reduced trabecular bone parameters'),
 dict(ref_id='xu2026', pmid='41990255', first_author='Xu H', year=2026, type='primary', one_line_finding='PIEZO2 in DRG neurons drives a CGRP-RAMP1-IL6 loop degrading the cartilage endplate'),
],
open_questions=['g_l6mech_007'], contradicts=['piezo1_channel']))

w(dict(id='trpv4_channel', name='TRPV4', type='protein', aliases=['Trpv4','vanilloid receptor-related osmotically activated channel'],
summary=("TRPV4 has the strongest human evidence of any candidate physeal mechanotransducer, but that evidence is genetic rather than mechanical. "
 "Gain-of-function TRPV4 variants cause a graded series of human skeletal dysplasias - metatropic dysplasia, spondylometaphyseal dysplasia "
 "Kozlowski type, brachyolmia - all of which are growth plate diseases with severe short stature and metaphyseal disorganisation, and "
 "loss-of-function variants also produce SMD Kozlowski, so the dose-response is non-monotonic. Small-molecule TRPV4 inhibition rescues the "
 "skeletal phenotype of Trpv4 mutant mice, establishing that the channel's activity level, not merely its presence, sets growth plate output. "
 "The direct mechanotransduction experiments, however, are prenatal or articular: in mechanically stimulated mouse embryonic hindlimb explants "
 "TRPV4 localises to regions of high biophysical stimulus and is required for loading-driven cartilage growth and joint morphogenesis via "
 "proliferation and matrix synthesis, while the classic osmotic and compressive TRPV4 work is in articular chondrocytes. No study has applied "
 "a defined mechanical stimulus to a postnatal growth plate and shown a TRPV4-dependent change in longitudinal growth rate, and TRPV4 has not "
 "been localised zonally in human physeal tissue."),
quantitative=[],
localization=['mouse embryonic hindlimb cartilage, regions of high biophysical stimulus: confirmed (khatib2023)',
 'mouse growth plate (postnatal), zonal: not established mechanically',
 'human growth plate: inferred from dysplasia phenotypes, no zonal localisation study located'],
human_evidence='indirect',
human_evidence_note='Human evidence is Mendelian: gain- and loss-of-function TRPV4 variants cause metatropic dysplasia and spondylometaphyseal dysplasia Kozlowski, both growth plate disorders, but no human mechanical experiment exists.',
species_basis=['mouse','human'], translation_risk='moderate',
translation_risk_reason='The human genetic link to growth plate disease is solid; the mechanotransduction step is demonstrated only in mouse embryonic explants and articular chondrocytes.',
confidence='B',
key_refs=[
 dict(ref_id='khatib2023', pmid='36696489', first_author='Khatib NS', year=2023, type='primary', one_line_finding='Loading-driven cartilage growth and joint morphogenesis in mouse embryonic hindlimb explants require TRPV4 activity'),
 dict(ref_id='nevarez2026', pmid='41574606', first_author='Nevarez L', year=2026, type='primary', one_line_finding='Small-molecule TRPV4 inhibition rescues the skeletal dysplasia phenotype of Trpv4 mutant mice'),
 dict(ref_id='roblesespinoza2025', pmid='41097048', first_author='Robles-Espinoza K', year=2025, type='review', one_line_finding='Documents the clinical spectrum of human TRPV4 metatropic dysplasia'),
 dict(ref_id='wang2025a', pmid='41225599', first_author='Wang H', year=2025, type='primary', one_line_finding='A loss-of-function TRPV4 variant also causes human spondylometaphyseal dysplasia Kozlowski type'),
],
open_questions=['g_l6mech_008']))
