import yaml, glob

p = [x for x in glob.glob('/home/user/growth-plate/atlas/nodes/**/*.yaml', recursive=True)
     if x.endswith('/perichondrial_tgfb_restraint.yaml')][0]
d = yaml.safe_load(open(p))

d['quantitative'] = [
 {'parameter': 'HUMAN RANDOMISED TEST of lowering this axis on growth',
  'value': ('height velocity 0.822 vs 0.935 cm/yr; height-for-age Z velocity 0.046 vs 0.019 z/yr; '
            'upper:lower segment ratio -0.014 vs -0.015 /yr; arm span:height 0.001 vs 0.001 /yr'),
  'unit': 'least-squares mean per year, atenolol vs losartan',
  'conditions': ('Pediatric Heart Network trial NCT00429364, 608 children and young adults with Marfan '
    'syndrome randomised to atenolol or losartan for 3 years. HEIGHT, HEIGHT-FOR-AGE Z-SCORE, ARM SPAN '
    'TO HEIGHT RATIO AND UPPER TO LOWER SEGMENT RATIO WERE ALL PRESPECIFIED SECONDARY OUTCOME MEASURES '
    'and the results are POSTED PUBLICLY on ClinicalTrials.gov. Differences computed by this atlas from '
    'the posted least-squares means and standard errors'),
  'species': 'human', 'source_ref': 'robertson2023',
  'uncertainty': ('NO DETECTABLE EFFECT ON ANY GROWTH ENDPOINT. Height velocity +0.113 cm/yr for '
    'losartan (t=0.39, p~0.69); height-for-age Z velocity -0.027 z/yr, i.e. the point estimate runs '
    'the OTHER way (t=-1.47, p~0.14); body proportions identical on both measures. THE DECISIVE '
    'LIMITATION IS THE COMPARATOR: this is losartan against ATENOLOL, not against placebo. Both arms '
    'are on active drug, beta-blockade has its own effects, and there is no untreated control - so a '
    'null between two active agents does not show that lowering this axis does nothing to growth. My '
    'p-values approximate the SE of the difference as the quadrature sum of the two group SEs; the '
    'trial model may share variance, so they are indicative. The trial was also null on its own primary '
    'endpoint, aortic root Z-score.')},
 {'parameter': 'perichondrium removal, effect on the growth plate',
  'value': 'extended collagen X zone AND extended BrdU-incorporating zone',
  'unit': 'qualitative, organ culture',
  'conditions': ('chick embryonic tibiotarsi in organ culture; terminal differentiation monitored with '
    'a monoclonal antibody to chicken collagen type X and proliferation by BrdU labelling'),
  'species': 'chicken', 'source_ref': 'long1998',
  'uncertainty': ('THE INTERNAL CONTROL IS WHAT MAKES THIS DECISIVE: partial removal of perichondrium '
    'from ONE SIDE of the tibiotarsus expanded both the collagen X domain and the BrdU zone AT THE SITE '
    'OF REMOVAL and not where the perichondrium remained intact. A side-specific effect within a single '
    'bone eliminates every systemic explanation. It also establishes the DUAL action - the perichondrium '
    'negatively regulates hypertrophy AND proliferation - 24 years before the fibrillin mechanism was '
    'found.')},
 {'parameter': 'route by which perichondrial TGF-beta restrains hypertrophy',
  'value': 'PTHrP-dependent for hypertrophic differentiation, PTHrP-independent for proliferation',
  'unit': 'qualitative',
  'conditions': ('mouse; a dominant-negative TGF-beta type II receptor expressed in '
    'perichondrium/periosteum increased hypertrophic differentiation in growth plate chondrocytes in '
    'vivo, and TGF-beta1 stimulated PTHrP mRNA in the perichondrium in organ culture'),
  'species': 'mouse', 'source_ref': 'alvarez2001',
  'uncertainty': ('THIS CONNECTS THE FIBRILLIN AXIS TO THE CANONICAL CIRCUIT THIS ATLAS ALREADY HOLDS. '
    'The perichondrial TGF-beta signal reaches the plate through PTHrP, so the fibrillin-LTBP module '
    'is upstream of the Ihh/PTHrP feedback loop rather than parallel to it. TGF-beta1 inhibits '
    'proliferation and hypertrophic differentiation by TWO SEPARATE MECHANISMS, only one of which is '
    'PTHrP-dependent.')},
 {'parameter': 'active TGF-beta concentration that precisely restores normal cartilage growth',
  'value': '300',
  'unit': 'pg/ml active TGF-beta1',
  'conditions': ('avian tibiotarsal organ cultures stripped of perichondrium and periosteum; '
    'perichondrial cell cultures treated with 2 ng/ml or more exogenous TGF-beta1 produce 300 pg/ml of '
    'active TGF-beta, and that concentration added back to stripped cultures effected precise '
    'regulation of cartilage growth'),
  'species': 'chicken', 'source_ref': 'crochiere2008',
  'uncertainty': ('THE WORD THE AUTHORS USE IS "PRECISE" - the added factor compensates EXACTLY for '
    'removal of the endogenous perichondrium, which is a strong claim and the reason this is a dose '
    'rather than a direction. It also means the restraint is a graded set-point rather than an on/off '
    'signal, which is what a therapeutic target would need to be. Regulation is stated to run through '
    'at least three independent mechanisms, only one of which is the TGF-beta response.')},
] + d['quantitative']

d['human_evidence'] = 'direct'
d['human_evidence_note'] = (
 "UPGRADED TO DIRECT 2026-08-06 and the direct evidence is a NULL. The Pediatric Heart Network trial "
 "NCT00429364 randomised 608 children and young adults with Marfan syndrome to atenolol or losartan and "
 "PRESPECIFIED height, height-for-age Z-score, arm span to height ratio and upper to lower segment "
 "ratio as secondary outcomes. The results are posted publicly. Losartan produced no detectable "
 "difference on any of them - height velocity +0.113 cm/yr (p~0.69) and height-for-age Z velocity "
 "-0.027 z/yr (p~0.14), the latter running the opposite way. The comparator is atenolol rather than "
 "placebo, so this bounds the effect of choosing losartan over a beta-blocker, not the effect of the "
 "axis. Separately, erkula2002 gives human Marfan growth charts from 180 patients: mean final height "
 "191.3 +/- 9 cm in males and 175.4 +/- 8.2 cm in females, with the pubertal growth velocity peak "
 "arriving 2.4 years early in males and 2.2 years early in females.")
d['confidence_note'] = d['confidence_note'] + (
 " HELD AT B on re-examination the same day. The human randomised test now exists and is null, but it "
 "is null against an active comparator and cannot refute the mechanism; the mouse genetics remain as "
 "strong as they were. What the trial does remove is the assumption that the axis is straightforwardly "
 "druggable for height.")
for r in ({'ref_id': 'long1998', 'pmid': '9463353', 'first_author': 'Long F', 'year': 1998,
           'type': 'primary',
           'one_line_finding': ('Perichondrium removal extends both the collagen X and BrdU zones, and '
             'one-sided removal does so only on that side - the perichondrium negatively regulates '
             'hypertrophy and proliferation, locally.')},
          {'ref_id': 'alvarez2001', 'pmid': '11458391', 'first_author': 'Alvarez J', 'year': 2001,
           'type': 'primary',
           'one_line_finding': ('Perichondrial TGF-beta restrains hypertrophic differentiation through '
             'PTHrP and proliferation through a separate PTHrP-independent mechanism.')},
          {'ref_id': 'crochiere2008', 'pmid': '18033673', 'first_author': 'Crochiere ML', 'year': 2008,
           'type': 'primary',
           'one_line_finding': ('300 pg/ml active TGF-beta1 added to perichondrium-stripped avian organ '
             'cultures precisely restores normal cartilage growth.')},
          {'ref_id': 'erkula2002', 'pmid': '11977157', 'first_author': 'Erkula G', 'year': 2002,
           'type': 'primary',
           'one_line_finding': ('Marfan growth charts from 180 patients: mean final height 191.3 cm '
             'male and 175.4 cm female, with the pubertal velocity peak 2.2-2.4 years early.')}):
    if r['ref_id'] not in {k['ref_id'] for k in d.get('key_refs', [])}:
        d['key_refs'].append(r)
d['last_verified'] = '2026-08-06'
yaml.safe_dump(d, open(p, 'w'), sort_keys=False, width=112, allow_unicode=True,
               default_flow_style=False)
print('perichondrial_tgfb_restraint:', len(d['quantitative']), 'rows, human_evidence',
      d['human_evidence'])
