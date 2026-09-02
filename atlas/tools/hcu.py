import yaml, glob

p = [x for x in glob.glob('/home/user/growth-plate/atlas/nodes/**/*.yaml', recursive=True)
     if x.endswith('/homocystinuria_tall.yaml')][0]
d = yaml.safe_load(open(p))

d['quantitative'].extend([
 {'parameter': 'adult height of an HCU cohort against the general population',
  'value': 'about +1',
  'unit': 'standard deviation score',
  'conditions': ('48 Irish pyridoxine-NONresponsive HCU patients, weight and height at nine set time '
    'points to 18 years, SDS against British 1990 and UK-WHO reference data. Birth weight was normal '
    '(male 3.71 and 3.37 vs 3.55 kg; female 3.33 and 3.36 vs 3.40 kg)'),
  'species': 'human', 'source_ref': 'purcell2017',
  'uncertainty': ('THE QUANTIFICATION mudd1985 DOES NOT CONTAIN, and it settles the physeal-versus-'
    'structural question this atlas asked: birth weight is normal and the excess appears afterwards, '
    'so the extra length is accrued POSTNATALLY and therefore at the growth plate. Weight rose by the '
    'same amount with no BMI difference, i.e. a balanced increase. HEAVY CAVEAT THE ABSTRACT DOES NOT '
    'CARRY: 77% of late-diagnosed and 75% of screened patients grew WITHIN their expected midparental '
    'height range, so most of the cohort is inside its own genetic target and the disease effect is '
    'smaller than a bare +1 SD against the population implies. Single centre, single country, no '
    'untreated arm.')},
 {'parameter': 'adult height by duration of untreated homocysteine exposure',
  'value': '+7.97',
  'unit': 'cm at 18 years, late-diagnosed minus newborn-screened',
  'conditions': ('same cohort; late-diagnosed n=12, mean age at diagnosis 5.09 years (range 1.33-11.79) '
    'against newborn-screened n=36. Weight +4.97 kg, P=0.0058. No difference in growth RATE between the '
    'groups after 10 years of age, so the divergence is accrued before then'),
  'species': 'human', 'source_ref': 'purcell2017',
  'uncertainty': ('P=0.0204. THIS IS THE INTERNAL DOSE-RESPONSE AND IT IS THE STRONGEST EVIDENCE IN THE '
    'NODE: within one disease, roughly five years of additional untreated hyperhomocysteinaemia is worth '
    'about 8 cm of adult height. The late-diagnosed group is also the OLDER cohort (mean current age '
    '34.6 vs 23.7 years), so the secular trend in population height runs AGAINST the finding and '
    'strengthens it. Against that: n=12, retrospective, single centre, and diagnosis age is confounded '
    'with everything else that changed in care between the two eras.')},
 {'parameter': 'effect of dietary homocysteine on long bone length in a growing animal',
  'value': 'tibial length significantly increased; tibial weight +12% and not significant',
  'unit': 'mm, chick tibia at 8 weeks',
  'conditions': ('chicks fed 0.6% dl-homocysteine for the first 8 weeks of life, n=8, against n=10 '
    'controls; body weight rose faster and was significantly greater at the end (P<0.01)'),
  'species': 'chicken', 'source_ref': 'mass2003',
  'uncertainty': ('P<0.01 for length. THE ANIMAL COUNTERPART OF THE HUMAN FINDING, and it localises the '
    'effect: radiographs showed generalised osteopenia and ACCELERATED EPIPHYSEAL OSSIFICATION with '
    'metaphyseal and suprametaphyseal lucencies that the authors call similar to human homocystinurics, '
    'and they describe the model as reproducing "accelerated skeletal growth, epiphyseal growth plate '
    'lesions". Tibiae were stronger, but strength was proportional to the increased length and cortical '
    'thickness, so there is no intrinsic material change - the bone is bigger, not better. High-dose '
    'dietary exposure producing a disease, in a fast-growing bird; not a model of therapeutic intent.')},
 {'parameter': 'molecular target of homocysteine in the connective tissue phenotype',
  'value': 'fibrillin-1, not collagen cross-linking',
  'unit': 'qualitative',
  'conditions': ('recombinant fragments spanning the entire fibrillin-1 molecule plus tropoelastin; '
    'homocysteinylation but NOT cysteinylation caused abnormal self-interaction traced to reduced '
    'multimerisation of the fibrillin-1 C terminus, and greatly reduced fibrillin-1 network deposition '
    'by human dermal fibroblasts'),
  'species': 'in_vitro_human_cell', 'source_ref': 'hubmacher2010',
  'uncertainty': ('THIS IS WHY THE HOMOCYSTINURIA STEP DOES NOT BELONG TO g_l1arch_018. That gap '
    'proposes collagen cross-link density as the mechanical converter; homocysteine acts on FIBRILLIN, '
    'the Marfan protein, and orth1994 showed it leaves cross-links in non-lesional cartilage unchanged. '
    'The authors note that Marfan and homocystinuria share long bone overgrowth, scoliosis and ectopia '
    'lentis from fundamentally different origins, which is the clue that the shared axis is the '
    'fibrillin microfibril and its control of TGF-beta rather than anything about collagen. IN VITRO '
    'ONLY: recombinant protein and dermal fibroblasts, no growth plate, no animal.')},
])

d['summary'] = d['summary'].rstrip() + (
 " RESOLVED 2026-08-06 AND MOVED OFF THE CROSS-LINK HYPOTHESIS. The tall stature is real, postnatal and "
 "quantified: an Irish cohort of 48 pyridoxine-nonresponsive patients runs about +1 SD taller and "
 "heavier than the population with no BMI difference and NORMAL BIRTH WEIGHT, and within the disease "
 "the late-diagnosed are 7.97 cm taller at 18 years than the newborn-screened, with the divergence "
 "complete before age 10 (purcell2017). Normal birth weight with postnatal excess means the length is "
 "accrued at the growth plate, which answers the physeal-versus-structural question this atlas raised. "
 "The animal counterpart agrees and localises it: chicks fed homocysteine grow faster with "
 "significantly longer tibiae and accelerated epiphyseal ossification (mass2003). But the mechanism is "
 "NOT collagen cross-linking - homocysteine modifies FIBRILLIN-1 and blocks microfibril network "
 "deposition (hubmacher2010) while leaving cross-links in non-lesional cartilage unchanged (orth1994). "
 "So this node belongs with the fibrillin/TGF-beta overgrowth axis shared with Marfan syndrome, not "
 "with g_l1arch_018. Caveat that limits all of it: about three quarters of the cohort still grew within "
 "their own midparental target range.")
d['human_evidence'] = 'direct'
d['human_evidence_note'] = (
 "REVISED TWICE ON 2026-08-06. mudd1985, the 629-patient reference natural history, reports no height "
 "or stature data at all - the words do not appear in 31 pages. purcell2017 supplies what it lacks: "
 "measured height SDS at nine time points to 18 years in 48 patients, about +1 SD above the population, "
 "normal birth weight, and a 7.97 cm within-disease difference by duration of untreated exposure. So "
 "the human evidence is DIRECT and quantified for the stature itself and for its postnatal (therefore "
 "physeal) timing, and IN VITRO ONLY for the mechanism.")
d['confidence'] = 'C'
d['confidence_note'] = (
 "Held at C on 2026-08-06 despite the new quantification. What improved is the phenotype: measured, "
 "postnatal, dose-responsive within the disease, with an animal counterpart showing longer tibiae. What "
 "did not improve is the mechanism, which rests on in vitro homocysteinylation of recombinant "
 "fibrillin-1 and dermal fibroblast cultures with nothing in a growth plate. B would require the "
 "fibrillin/TGF-beta step shown in physeal tissue.")
for r in ({'ref_id': 'purcell2017', 'pmid': '29270317', 'first_author': 'Purcell O', 'year': 2017,
           'type': 'primary',
           'one_line_finding': ('48 Irish pyridoxine-nonresponsive HCU patients run ~1 SD taller and '
             'heavier than the population with normal birth weight, and late-diagnosed patients are '
             '7.97 cm taller at 18 than newborn-screened.')},
          {'ref_id': 'mass2003', 'pmid': '12597778', 'first_author': 'Masse PG', 'year': 2003,
           'type': 'primary',
           'one_line_finding': ('Chicks fed 0.6% homocysteine for 8 weeks grew faster with '
             'significantly longer tibiae, generalised osteopenia and accelerated epiphyseal '
             'ossification.')},
          {'ref_id': 'hubmacher2010', 'pmid': '19889633', 'first_author': 'Hubmacher D', 'year': 2010,
           'type': 'primary',
           'one_line_finding': ('Homocysteinylation, but not cysteinylation, disrupts fibrillin-1 '
             'multimerisation and greatly reduces fibrillin-1 network deposition by human fibroblasts '
             '- the Marfan protein, not collagen.')}):
    if r['ref_id'] not in {k['ref_id'] for k in d.get('key_refs', [])}:
        d.setdefault('key_refs', []).append(r)
d['last_verified'] = '2026-08-06'
yaml.safe_dump(d, open(p, 'w'), sort_keys=False, width=112, allow_unicode=True,
               default_flow_style=False)
print('homocystinuria_tall:', len(d['quantitative']), 'rows, confidence', d['confidence'],
      ', human_evidence', d['human_evidence'])
