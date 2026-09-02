import yaml, glob

p = [x for x in glob.glob('/home/user/growth-plate/atlas/nodes/**/*.yaml', recursive=True)
     if x.endswith('/homocystinuria_tall.yaml')][0]
d = yaml.safe_load(open(p))

d.setdefault('quantitative', []).extend([
 {'parameter': 'height, stature or body-proportion data in the definitive natural history',
  'value': 'none reported',
  'unit': 'none',
  'conditions': ('international questionnaire survey of 629 patients with cystathionine beta-synthase '
    'deficiency, 31 pages, the largest series ever assembled and the reference natural history for this '
    'disorder'),
  'species': 'human', 'source_ref': 'mudd1985',
  'uncertainty': ('RECORDED AS AN ABSENCE, and it is the load-bearing one. Full text read 2026-08-06 '
    'and searched: the words height, stature, growth, scoliosis, arachnodactyly, arm span and body '
    'proportion do not appear anywhere in the paper. The disorder this atlas has been treating as the '
    'human natural experiment in tall stature has never had its stature measured in the series that '
    'defines it. This does not show patients are not tall - it shows the claim is not quantified where '
    'it would most be expected, and that no analysis of WHERE the extra length comes from is possible '
    'from this source.')},
 {'parameter': 'clinical features leading to investigation',
  'value': ('ectopia lentis 85.6; mental retardation 55.7; Marfanoid characteristics 36.9; bony '
    'abnormality 23.5; developmental retardation 22.5; early thromboembolic disorder 16.1'),
  'unit': '% of patients in whom the feature was a sole or contributory cause',
  'conditions': ('472 of the 629 patients, restricted to those ascertained on clinical grounds rather '
    'than by newborn or sibling screening'),
  'species': 'human', 'source_ref': 'mudd1985',
  'uncertainty': ('These are ASCERTAINMENT features - what led to the diagnosis - not prevalences, so '
    'they are biased toward whatever prompts investigation, and lens dislocation dominates for that '
    'reason. Note what stands in for stature: Marfanoid CHARACTERISTICS at 36.9% and bony ABNORMALITY '
    'at 23.5%, both unquantified descriptors. Neither separates a long-bone growth phenotype from a '
    'connective-tissue one.')},
 {'parameter': 'radiologic spinal osteoporosis by age 15, untreated',
  'value': '36 vs 64',
  'unit': '% (B6-responsive vs B6-non-responsive)',
  'conditions': ('time-to-event analysis restricted to patients reported either to have or not to have '
    'osteoporosis on a lateral radiograph of the spine, which is the papers definition of the finding'),
  'species': 'human', 'source_ref': 'mudd1985',
  'uncertainty': ('P<0.002 between the two groups. THE DOMINANT PROGRESSIVE SKELETAL FINDING IN THIS '
    'DISORDER IS BONE FRAGILITY, NOT ACCELERATED GROWTH - which is a bone-quality and connective-tissue '
    'picture rather than a growth-plate-velocity one, and points the interpretation of the skeletal '
    'phenotype away from the physis.')},
])

d['human_evidence_note'] = (
 "REVISED 2026-08-06 on reading mudd1985 in full. The tall stature of classical homocystinuria is a "
 "textbook descriptor that the definitive 629-patient natural history never quantifies: it reports no "
 "height, stature, growth or body-proportion data at all. What that series does quantify is Marfanoid "
 "characteristics as an ascertainment feature in 36.9%, bony abnormality in 23.5%, and progressive "
 "radiologic spinal osteoporosis reaching 36-64% by age 15. So the human evidence for this node is "
 "DIRECT as to the disorder and its skeletal involvement, but INDIRECT and unquantified as to stature "
 "itself, and silent on whether any of the extra length is growth-plate-mediated.")
d['human_evidence'] = 'indirect'
d['open_questions'] = sorted(set((d.get('open_questions') or []) + ['g_l1arch_018']))
d['last_verified'] = '2026-08-06'
krefs = {r['ref_id'] for r in d.get('key_refs', [])}
if 'mudd1985' not in krefs:
    d.setdefault('key_refs', []).append({
        'ref_id': 'mudd1985', 'pmid': '3872065', 'first_author': 'Mudd SH', 'year': 1985,
        'type': 'primary',
        'one_line_finding': ('629-patient natural history of CBS deficiency reporting no height or '
                             'stature data at all; Marfanoid characteristics 36.9% and bony abnormality '
                             '23.5% as ascertainment features, spinal osteoporosis 36-64% by age 15.')})
yaml.safe_dump(d, open(p, 'w'), sort_keys=False, width=112, allow_unicode=True,
               default_flow_style=False)
print('homocystinuria_tall updated:', len(d['quantitative']), 'rows, human_evidence ->', d['human_evidence'])
