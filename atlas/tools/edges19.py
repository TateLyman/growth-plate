import yaml

p = '/home/user/growth-plate/atlas/edges/edges.yaml'
d = yaml.safe_load(open(p))
edges = d['edges'] if isinstance(d, dict) else d
existing = {(e['source'], e['target'], e['relation']) for e in edges}
nxt = max(int(e['edge_id'][1:]) for e in edges) + 1

new = [
 # The perichondrium restrains elongation. Fibrillin-1 loss removes the restraint, so the SIGN on
 # the restraint->elongation edge is negative: more restraint, less length.
 dict(source='perichondrial_tgfb_restraint', target='growth_velocity_longitudinal',
      relation='inhibits', sign='-',
      context=('mouse Marfan model, Fbn1 conditional inactivation with metatarsal organ culture; '
               'embryonic/perinatal metatarsal, sex unknown (not reported in source)'),
      evidence_tier='T1', refs=['sedes2022'], confidence='C',
      notes=('Fbn1-deficient metatarsals grew LONGER and released LESS TGF-beta, and recombinant '
             'TGF-beta1 add-back normalised their linear growth. The add-back is what fixes the sign: '
             'the axis restrains elongation, so removing it lengthens the bone.'),
      traversal_usable=True),
 dict(source='marfan_syndrome', target='perichondrial_tgfb_restraint',
      relation='inhibits', sign='-',
      context=('outer perichondrium of Fbn1-deficient mice; fibrillin-1 loss reduces LTBP-3 and LTBP-4 '
               'accumulation and phospho-Smad2, age/stage as reported in source'),
      evidence_tier='T1', refs=['sedes2022'], confidence='C',
      notes=('Fibrillin-1 is required for the restraint, so the Marfan lesion LOWERS TGF-beta '
             'signalling here - the opposite direction to the aortic Marfan literature, which must '
             'not be imported into bone. There is no fibrillin-1 node in this atlas yet; the edge is '
             'anchored on the disorder instead and that is a coverage gap, not a modelling choice.'),
      traversal_usable=True),
 dict(source='perichondrial_tgfb_restraint', target='chondrocyte_hypertrophy',
      relation='inhibits', sign='-',
      context=('mouse growth plate; Smad3 exon 8 null shows enhanced terminal differentiation and '
               'increased collagen X expressing cells, and losartan given to wild-type mice elongates '
               'the hypertrophic zone with raised Col10a1'),
      evidence_tier='T1', refs=['yang2001', 'chen2015'], confidence='C',
      notes=('TGF-beta/Smad3 represses terminal hypertrophic differentiation, so lowering the axis '
             'releases the brake. NOTE chen2015 measured zone height and bone mass, NOT bone length.'),
      traversal_usable=True),
 dict(source='homocystinuria_tall', target='perichondrial_tgfb_restraint',
      relation='inhibits', sign='-',
      context=('human disorder and in vitro human fibroblasts; homocysteinylation of fibrillin-1 '
               'disrupts multimerisation and reduces microfibril network deposition'),
      evidence_tier='T1', refs=['hubmacher2010', 'purcell2017'], confidence='C',
      notes=('Homocystinuria reaches the same axis chemically rather than genetically, which is why '
             'it shares long bone overgrowth, scoliosis and ectopia lentis with Marfan despite an '
             'unrelated primary defect.'),
      traversal_usable=True),
]

added = 0
for e in new:
    k = (e['source'], e['target'], e['relation'])
    if k in existing:
        print('skip existing', k)
        continue
    e = {'edge_id': f'e{nxt:05d}', **e}
    edges.append(e)
    nxt += 1
    added += 1

if isinstance(d, dict):
    d['edges'] = edges
else:
    d = edges
yaml.safe_dump(d, open(p, 'w'), sort_keys=False, width=112, allow_unicode=True,
               default_flow_style=False)
print(f'added {added} edges, total {len(edges)}')
