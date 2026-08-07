import yaml, glob

# ---- gap: the age window, which is what any translation attempt turns on -----------------
g = {
 'gap_id': 'g_l3_neprilysin_window',
 'question': ("Does a human equivalent of the mouse 3-to-4-week neprilysin-inhibition window exist, and "
   "when is it - and does raising endogenous CNP by blocking its degradation increase bone length in "
   "any human?"),
 'type': 'known_unknown', 'layer': 'L3',
 'why_it_matters': ("Sacubitril is an APPROVED drug, already given to children for heart failure, that "
   "produces dose-dependent skeletal overgrowth in wild-type mice through the same CNP/NPR-B pathway "
   "vosoritide targets - but by protecting the peptide the child already makes rather than infusing an "
   "analogue daily. That is a materially different pharmacological proposition from anything else in "
   "this atlas: oral, approved, paediatric-dosed, and acting on an endogenous ligand. Everything turns "
   "on the window, because the mouse effect appears ONLY at 3-4 weeks, when endogenous CNP and "
   "neprilysin expression are highest. Given outside its window the drug has no substrate to protect "
   "and will do nothing - and a null obtained that way would look like a refuted mechanism rather than "
   "a mistimed experiment."),
 'what_is_known': ("hakata2024: sacubitril given to wild-type C57BL/6 mice causes DOSE-DEPENDENT "
   "skeletal overgrowth with thickening of BOTH the proliferative and hypertrophic zones, mirroring CNP "
   "administration; the effect is ABOLISHED by cartilage-specific NPR-B knockout, which excludes "
   "neprilysin's many other substrates; it also works on fetal tibial explants in organ culture, so it "
   "needs no endocrine axis; and it appears only at 3-4 weeks of age, coinciding with peak endogenous "
   "CNP and NEP expression in lumbar vertebrae. The receiving pathway is the best-validated growth "
   "pathway in human skeletal medicine - NPR2 gain of function causes human tall stature, NPR2 loss "
   "causes acromesomelic dysplasia, NPPC duplication causes tall stature, and vosoritide is approved. "
   "The atlas already held the OTHER clearance arm, NPR3, from the start."),
 'what_is_missing': ("(1) THE MAGNITUDE. No effect size has been read - the abstract gives direction and "
   "dose-dependence but no lengths, and the full text has not been obtained. Nothing from this line "
   "should enter a model until it has. "
   "(2) THE HUMAN WINDOW. Mouse 3-4 weeks is peri-pubertal, but the mouse plate never closes and the "
   "human plate does, so the timelines are not superimposable. Whether the human equivalent is infancy, "
   "mid-childhood or the pubertal spurt is unknown, and it is answerable from existing human tissue: "
   "chu2026 provides a single-cell and spatial transcriptional atlas of the EARLY PUBERTAL HUMAN GROWTH "
   "PLATE, so MME and NPPC expression by zone and age could be read out of it directly. "
   "(3) ANY HUMAN MEASUREMENT AT ALL. Sacubitril/valsartan is approved for paediatric heart failure. No "
   "trial, registry or case series reporting height, growth velocity or bone age in treated children "
   "was located. Those children are on the drug for years during growth; the measurement is being taken "
   "at every clinic visit and never analysed - the same situation as the Pediatric Heart Network "
   "losartan trial, and in that case the data turned out to be posted publicly and simply unexamined. "
   "(4) WHETHER THE TWO CLEARANCE ARMS ARE ADDITIVE. NPR3 blockade and neprilysin inhibition remove "
   "different routes of CNP disposal. Nobody has combined them, and if the arms are independent the "
   "combination is the obvious experiment."),
 'nearest_evidence': ['hakata2024', 'chu2026'],
 'nearest_evidence_note': ("hakata2024 is the entire evidential basis and it is one paper, one "
   "laboratory, one species, read from its abstract. chu2026 is the human tissue resource that could "
   "answer the window question without a new experiment."),
 'discriminating_experiment': ("TWO STEPS, NEITHER REQUIRING A NEW ANIMAL. (1) READ MME AND NPPC "
   "EXPRESSION BY ZONE AND AGE OUT OF chu2026's HUMAN PUBERTAL GROWTH PLATE ATLAS. If neprilysin is not "
   "expressed in the human plate, or is expressed outside the growing years, the whole proposition "
   "fails immediately and cheaply. If it tracks CNP the way it does in mouse, the window is identified. "
   "(2) RETROSPECTIVELY ANALYSE HEIGHT IN CHILDREN ON SACUBITRIL/VALSARTAN. The drug is approved for "
   "paediatric heart failure and those children are measured at every visit over years. The comparator "
   "problem that defeated the losartan question is smaller here, because paediatric heart failure "
   "cohorts include children on other regimens. THEN, and only then, the animal experiment worth doing "
   "is a dose-response of sacubitril across the whole growing period in a normal animal with FEMUR "
   "LENGTH as the endpoint - the same measurement nobody has taken for losartan."),
 'tractability': 1,
}
for p in ('/home/user/growth-plate/atlas/gaps/shards/l1arch.gaps.yaml',
          '/home/user/growth-plate/atlas/gaps/gaps.yaml'):
    d = yaml.safe_load(open(p))
    if not any(x.get('gap_id') == g['gap_id'] for x in d['gaps']):
        d['gaps'].append(g)
    yaml.safe_dump(d, open(p, 'w'), sort_keys=False, width=110, allow_unicode=True,
                   default_flow_style=False)
print('gap g_l3_neprilysin_window added')

# ---- edges -------------------------------------------------------------------------------
p = '/home/user/growth-plate/atlas/edges/edges.yaml'
d = yaml.safe_load(open(p))
edges = d['edges'] if isinstance(d, dict) else d
have = {(e['source'], e['target'], e['relation']) for e in edges}
nxt = max(int(e['edge_id'][1:]) for e in edges) + 1
new = [
 dict(source='neprilysin_cnp_clearance', target='cnp_protein', relation='inhibits', sign='-',
      context=('neprilysin is the endopeptidase that catalyses degradation of C-type natriuretic '
               'peptide; mouse, growth plate and systemic, age/stage as reported in source'),
      evidence_tier='T1', refs=['hakata2024'], confidence='B',
      notes='Established enzymology; the growth-relevant consequence is shown by inhibitor rescue.',
      traversal_usable=True),
 dict(source='neprilysin_cnp_clearance', target='growth_velocity_longitudinal',
      relation='inhibits', sign='-',
      context=('wild-type C57BL/6 mice given the neprilysin inhibitor sacubitril show dose-dependent '
               'skeletal overgrowth, only at 3-4 weeks of age; abolished by cartilage-specific NPR-B '
               'knockout'),
      evidence_tier='T1', refs=['hakata2024'], confidence='C',
      notes=('Inhibiting the enzyme INCREASES growth, so the enzyme restrains it. Effect size unread - '
             'abstract only. Conditional on an age window whose human equivalent is unknown.'),
      traversal_usable=True),
 dict(source='neprilysin_cnp_clearance', target='npr2_receptor', relation='inhibits', sign='-',
      context=('by removing the ligand rather than the receptor; the sacubitril growth effect is '
               'abolished in cartilage-specific NPR-B knockout mice'),
      evidence_tier='T1', refs=['hakata2024'], confidence='C',
      notes='Ligand-side control of NPR2 signalling, parallel to NPR3-mediated clearance.',
      traversal_usable=True),
]
added = 0
for e in new:
    if (e['source'], e['target'], e['relation']) in have:
        continue
    edges.append({'edge_id': f'e{nxt:05d}', **e}); nxt += 1; added += 1
if isinstance(d, dict):
    d['edges'] = edges
yaml.safe_dump(d, open(p, 'w'), sort_keys=False, width=112, allow_unicode=True,
               default_flow_style=False)
print(f'added {added} edges, total {len(edges)}')
