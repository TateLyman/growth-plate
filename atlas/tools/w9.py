import yaml, os
D='atlas/nodes/L6_mechanobiology'
def w(n):
    n.setdefault('layer','L6'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    yaml.safe_dump(n,open(os.path.join(D,n['id']+'.yaml'),'w'),sort_keys=False,width=100,allow_unicode=True)
    print('wrote',n['id'])

w(dict(id='disuse_growth_effect', name='Disuse and longitudinal growth', type='process',
summary=("Removing load does not simply reverse the Hueter-Volkmann effect. Two observations bound the question. In the growth plate itself, "
 "limb immobilisation abolished the abnormal peripheral ossification phenotype of cartilage-specific Ift88-null mice, showing that the "
 "disruptive stimulus in the adolescent plate is physiological load and that unloading is protective rather than growth-promoting for that "
 "phenotype. In humans, chronic disuse produces smaller and thinner long bones: children and adolescents with cerebral palsy and other "
 "neuromotor impairments have reduced bone size and cortical thickness, and even ambulatory children with spastic cerebral palsy already "
 "show smaller bone area and trabecular deficits. Whether the length deficit in these children is a physeal effect or is dominated by "
 "nutrition, muscle traction and the underlying neurological disorder is unresolved and is the reason human disuse cannot be read as a "
 "clean unloading experiment. Perpendicular evidence comes from prenatal akinesia, where absent fetal movement impairs joint and bone "
 "development and maternal exercise rescues it. The consistent pattern is that loading is required for normal skeletal form and cross-section, "
 "while its effect on longitudinal growth rate is smaller and its sign depends on the waveform."),
quantitative=[],
localization=['mouse tibial growth plate: immobilisation abolishes load-driven peripheral ossification defect (coveney2022)','human long bones in cerebral palsy: reduced size and cortical thickness (hodgson2025)'],
human_evidence='indirect',
human_evidence_note='Human disuse data come from cerebral palsy and neuromotor impairment cohorts in which disuse is confounded with nutrition, spasticity and the primary neurological lesion.',
species_basis=['mouse','human'], translation_risk='high',
translation_risk_reason='The controlled unloading experiments are murine limb immobilisation; the human comparisons are uncontrolled disease cohorts.',
confidence='C',
key_refs=[
 dict(ref_id='coveney2022', pmid='35038201', first_author='Coveney CR', year=2022, type='primary', one_line_finding='Limb immobilisation abolished the growth plate phenotype of Ift88 deletion, proving the phenotype is load-driven'),
 dict(ref_id='hodgson2025', pmid='40661739', first_author='Hodgson E', year=2025, type='primary', one_line_finding='Children with cerebral palsy and other neuromotor impairments have smaller and thinner long bones'),
 dict(ref_id='zimmermann2025', pmid='39927930', first_author='Zimmermann EA', year=2025, type='primary', one_line_finding='Even ambulatory children with spastic cerebral palsy show reduced bone area and trabecular deficits'),
],
open_questions=['g_l6mech_013']))

w(dict(id='bed_rest_growth_human', name='Bed rest as a human unloading experiment', type='phenotype',
summary=("Head-down-tilt bed rest is the standard terrestrial analogue of microgravity and produces a well-characterised musculoskeletal deconditioning "
 "syndrome, but as an experiment on the growth plate it is essentially empty. All established bed rest protocols - 14, 30 and 60 day campaigns with "
 "artificial gravity, exercise and pharmacological countermeasures - are conducted in adults, whose physes are closed, so they measure bone loss and "
 "muscle atrophy rather than growth modulation. What bed rest does reliably show in adults is spinal lengthening: recumbency removes the axial load "
 "that compresses intervertebral discs, and stature rises, which is the same mechanism as overnight recovery of diurnal height loss. Bed rest in "
 "children is never elective and long-term recumbency in paediatric populations occurs only alongside serious illness, so no controlled paediatric "
 "bed-rest study with a height-velocity endpoint has been located. This node therefore exists mainly to mark a gap: the mechanically cleanest human "
 "unloading protocol has never been applied to a growing skeleton, and the entire human unloading evidence base for the physis rests on disease "
 "cohorts and on spaceflight anthropometry in adults."),
quantitative=[],
localization=['human intervertebral discs and spine: lengthening under recumbency','human physis: no data'],
human_evidence='absent',
human_evidence_note='No controlled bed rest study in children with a longitudinal growth endpoint was located; adult bed rest measures bone density and disc height, not physeal growth.',
species_basis=['human'], translation_risk='not_applicable',
translation_risk_reason='Human protocol, but performed exclusively in skeletally mature adults.',
confidence='D',
key_refs=[
 dict(ref_id='tyrrell1985', pmid='4002039', first_author='Tyrrell AR', year=1985, type='primary', one_line_finding='Quantifies the recumbency-driven recovery of stature that underlies the bed-rest spinal lengthening effect: ~70% of diurnal loss regained in the first half of the night'),
 dict(ref_id='young2023', pmid='34674563', first_author='Young KS', year=2023, type='primary', one_line_finding='Provides the closest true unloading anthropometry in humans, from spaceflight rather than bed rest'),
],
open_questions=['g_l6mech_013']))

w(dict(id='spaceflight_microgravity_growth', name='Spaceflight, microgravity and growth', type='phenotype',
summary=("Astronauts get taller in orbit, but the gain is spinal unloading, not endochondral growth. Photogrammetric and tape anthropometry on nine ISS "
 "crew members showed a biphasic change: stature rose by up to 3% in the early flight phase, then plateaued for the remainder of the mission, and "
 "returned to preflight values after landing. Acromion height followed the same pattern, while chest, hip, thigh and calf circumferences fell by up "
 "to 11%. A 3% gain in an adult of 1.75 m is roughly 5 cm, several times the ~19 mm diurnal stature loss on Earth, consistent with removal of axial "
 "compression from the whole spine plus loss of the standing postural curves. Full reversibility on return, and the fact that these are adults with "
 "closed physes, rule out a growth plate contribution in this dataset. There is no human paediatric spaceflight, so the effect of microgravity on a "
 "growing physis is unmeasured in humans. The rodent literature provides the only direct evidence, showing spaceflight alters skeletal tissue "
 "including the spinal column, and simulated microgravity has been used experimentally to reverse PIEZO1-driven growth plate ossification in mice - "
 "which is a mechanistic argument that unloading acts on the physis, not a measurement of growth rate in flight."),
quantitative=[
 dict(parameter='stature increase during early spaceflight', value='up to 3', unit='% of preflight stature', conditions='nine ISS crew, photogrammetry plus tape measure, biphasic with an early rise then plateau', species='human', source_ref='young2023', uncertainty='n=9; individual variation not reported in abstract; fully reversed postflight'),
 dict(parameter='segment circumference decrease during spaceflight', value='up to 11', unit='%', conditions='chest, hip, thigh and calf, same crew', species='human', source_ref='young2023', uncertainty='returned close to preflight after landing'),
],
localization=['human spine (adult): stature gain measured','human physis: not measured, no paediatric spaceflight','rodent spinal column and skeleton: altered by spaceflight (veres2026, monfared2026)'],
human_evidence='direct',
human_evidence_note='Direct human in-flight anthropometry exists, but only in adults with closed physes, so it says nothing about physeal growth.',
species_basis=['human','mouse','rat'], translation_risk='not_applicable',
translation_risk_reason='The human measurement is real but concerns disc and posture, not growth plate output.',
confidence='B',
key_refs=[
 dict(ref_id='young2023', pmid='34674563', first_author='Young KS', year=2023, type='primary', one_line_finding='Stature rose up to 3% early in flight, plateaued, and reversed after landing in nine ISS crew'),
 dict(ref_id='veres2026', pmid='41660583', first_author='Veres J', year=2026, type='primary', one_line_finding='Spaceflight alters rodent spinal column tissues'),
 dict(ref_id='monfared2026', pmid='42088598', first_author='Monfared V', year=2026, type='review', one_line_finding='Reviews spaceflight effects on the rodent skeleton including growth-relevant compartments'),
 dict(ref_id='chen2026', pmid='42082502', first_author='Chen F', year=2026, type='primary', one_line_finding='Simulated microgravity unloading rescues PIEZO1-overexpression-driven growth plate ossification in mice'),
],
open_questions=['g_l6mech_013']))
