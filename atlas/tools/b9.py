import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad')
from w import w

r_xie = dict(ref_id='xie2025', pmid='40781081', first_author='Xie C', year=2025, type='primary', one_line_finding='In human growth plate SPP1 and AHSG mark the mineralization-inhibiting epiphyseal boundary while ENPP1 and ALPL coexist with them at the promoting metaphyseal boundary')
r_kim = dict(ref_id='kim2010', pmid='20601283', first_author='Kim HJ', year=2010, type='primary', one_line_finding='Extracellular Pi stimulates and PPi inhibits growth plate chondrocyte terminal differentiation and apoptosis, with different Pi thresholds for differentiation and apoptosis, all Pit-1 dependent')
r_mil = dict(ref_id='milln2016', pmid='26590809', first_author='Millan JL', year=2016, type='review', one_line_finding='Plasma PPi 1-6 uM in humans; TNAP acts to establish a local Pi/PPi ratio conducive to controlled calcification')
r_rus = dict(ref_id='russell1971', pmid='4324072', first_author='Russell RG', year=1971, type='primary', one_line_finding='Plasma PPi 3.50 +/- 0.11 umol/L in 73 healthy adults, 99% range 1.19-5.65 umol/L')
r_alt = dict(ref_id='althoff1982', pmid='7107329', first_author='Althoff J', year=1982, type='primary', one_line_finding='Porcine growth plate Ca x P ion product is far above the 2 mM^2 needed for in vitro mineralization in every zone')
r_har = dict(ref_id='harmey2004', pmid='15039209', first_author='Harmey D', year=2004, type='primary', one_line_finding='Genetic manipulation of TNAP, NPP1 and ANK moves PPi and osteopontin in the same direction and rescues opposite mineralization phenotypes')
r_and = dict(ref_id='anderson2004', pmid='14982838', first_author='Anderson HC', year=2004, type='primary', one_line_finding='Alpl-/- growth plate mineral initiates in matrix vesicles but cannot propagate into a PPi-rich extravesicular matrix')

w(dict(
 id='pi_ppi_ratio', name='Extracellular Pi/PPi ratio as the mineralization control variable', aliases=['Pi:PPi ratio','phosphate to pyrophosphate ratio'], type='process',
 summary=("Mineralization in the growth plate is not controlled by mineral supply. Electron microprobe analysis of pig "
  "growth plate shows the extracellular Ca x P ion product is far above the ~2 mM^2 needed for mineralization in vitro "
  "in EVERY zone, including the resting and proliferative zones that never mineralize, so the tissue is chronically "
  "supersaturated and the operative variable is inhibition. The dominant inhibitor is PPi and the dominant permissive "
  "signal is Pi, so the ratio of the two is the control variable. Human circulating values bracket the scale: plasma "
  "PPi is 3.50 +/- 0.11 umol/L (99% range 1.19-5.65) against a serum phosphate of order 1-2 mmol/L, i.e. a "
  "circulating Pi:PPi ratio of roughly 300-600:1. The ratio is not merely physicochemical. In growth plate "
  "chondrocytes extracellular Pi stimulates and extracellular PPi inhibits terminal differentiation marker "
  "expression, mineralization and apoptosis, with different Pi thresholds for the two - lower Pi favours "
  "differentiation, higher Pi is required for apoptosis - all dependent on Pit-1/Pit-2 type III Na/Pi cotransporter "
  "expression and actual Pi uptake. Every genetic manipulation of the axis (TNAP loss, ENPP1 loss, ANK loss, PHOSPHO1 "
  "loss) moves the phenotype in the direction predicted by the ratio, and opposing mutations cancel. What is missing "
  "is the number: no measurement of Pi or PPi concentration, or of their ratio, in the extracellular fluid of any "
  "growth plate zone in situ was located in this sweep."),
 quantitative=[
  dict(parameter='Circulating Pi:PPi ratio in healthy humans', value='~300-600', unit='mol:mol (serum Pi 1-2 mmol/L over plasma PPi 3.5 umol/L)', conditions='derived from measured plasma PPi and conventional serum phosphate reference range', species='human', source_ref='russell1971', uncertainty='derived quantity; the serum phosphate term is a reference range, not measured in the same subjects', value_unverified=True),
  dict(parameter='Ca x P ion product needed for in vitro mineralization of connective tissue', value='2', unit='mM^2', conditions='threshold cited by microprobe study', species='not_applicable', source_ref='althoff1982', uncertainty='threshold value'),
  dict(parameter='Growth plate extracellular Ca x P ion product relative to that threshold', value='much greater than 1', unit='fold above threshold, in all zones', conditions='porcine growth plate electron microprobe', species='porcine', source_ref='althoff1982', uncertainty='stated qualitatively as much higher'),
  dict(parameter='Relative Pi requirement for terminal differentiation versus apoptosis of growth plate chondrocytes', value='apoptosis requires higher Pi than differentiation', unit='rank order of concentration thresholds', conditions='cultured growth plate chondrocytes, graded extracellular Pi, Pit-1 knockdown control', species='rat', source_ref='kim2010', uncertainty='absolute Pi concentrations not extracted from abstract'),
 ],
 localization=['porcine growth plate all zones: supersaturated Ca x P product (althoff1982)',
  'growth plate zone-resolved Pi and PPi concentrations: never measured in situ in any species'],
 human_evidence='indirect',
 human_evidence_note='Human evidence is the plasma PPi range plus the two opposing human loss-of-function syndromes (ALPL and ENPP1); the local ratio in the growth plate has never been measured in humans or animals.',
 species_basis=['human','porcine','rat','mouse'], translation_risk='moderate',
 translation_risk_reason='The systemic numbers are human but the tissue-level ratio, which is the actual control variable, is unmeasured in every species.',
 confidence='B',
 key_refs=[r_kim, r_alt, r_rus, r_mil, r_har, r_and],
 open_questions=['g_l5matrix_002'],
))

w(dict(
 id='fibronectin_cartilage', name='Fibronectin in cartilage and growth plate', aliases=['FN1','fibronectin'], type='protein',
 summary=("Fibronectin is the adhesive glycoprotein through which chondrocytes engage their own matrix, principally "
  "via alpha5beta1 integrin, and it is a node in the matrix-matrix network, binding COMP directly. Its relevance to "
  "this layer rests on one strong human observation and a set of weaker cell-biological ones. The human observation is "
  "that heterozygous FN1 mutations cause a subtype of spondylometaphyseal dysplasia with corner fractures - a "
  "metaphyseal, growth-plate-adjacent phenotype - so fibronectin dosage does affect the human physis. The cell "
  "biology is that alpha5beta1-fibronectin engagement modulates chondrocyte proliferation and matrix interaction, and "
  "that fibronectin fragments generated by matrix degradation are catabolic, inducing collagenase-3 and inflammatory "
  "mediators in chondrocytes, which makes fibronectin fragmentation an amplifier of matrix loss rather than a "
  "structural role. Zonal fibronectin distribution across the human growth plate was not established in this sweep, "
  "and this node is the thinnest in the layer for that reason."),
 quantitative=[],
 localization=['human metaphysis: FN1 haploinsufficiency produces corner fractures at the metaphyseal margin (lee2017)',
  'growth plate zonal fibronectin: not established'],
 human_evidence='direct',
 human_evidence_note='Heterozygous FN1 mutations cause a directly characterised human spondylometaphyseal dysplasia with metaphyseal corner fractures.',
 species_basis=['human','bovine','in_vitro_animal_cell'], translation_risk='moderate',
 translation_risk_reason='Human genetics establish that FN1 dosage matters for the metaphysis, but the mechanism in the growth plate is inferred from articular chondrocyte culture.',
 confidence='C',
 key_refs=[
   dict(ref_id='lee2017', pmid='29100092', first_author='Lee CS', year=2017, type='primary_abstract_only', one_line_finding='Heterozygous FN1 mutations cause spondylometaphyseal dysplasia with corner fractures'),
   dict(ref_id='di2002', pmid='12225811', first_author='Di Cesare PE', year=2002, type='primary_abstract_only', one_line_finding='COMP binds fibronectin directly in a matrix-matrix interaction'),
   dict(ref_id='enomotoiwamoto1997', pmid='9200013', first_author='Enomoto-Iwamoto M', year=1997, type='primary_abstract_only', one_line_finding='alpha5beta1 integrin mediates chondrocyte-fibronectin interaction and modulates proliferation')],
 open_questions=['g_l5matrix_009'],
))

w(dict(
 id='fetuin_a_ahsg', name='Fetuin-A (AHSG)', aliases=['AHSG','alpha2-Heremans-Schmid glycoprotein','fetuin-A'], type='protein',
 summary=("Fetuin-A is a liver-derived serum glycoprotein that reaches bone and cartilage from the circulation and "
  "acts as a systemic mineralization inhibitor with a mechanism unlike osteopontin's. Rather than adsorbing to a "
  "growing crystal face, it sequesters calcium and phosphate into soluble colloidal calciprotein particles, keeping "
  "supersaturated fluid metastable. Ahsg-null mice develop widespread ectopic calcification, particularly on a "
  "calcification-prone genetic background, establishing the function in vivo. Its relevance to the growth plate was "
  "established directly in human tissue: spatial proteomics of human growth plate identifies AHSG together with SPP1 "
  "as the proteins concentrated at the growth plate-epiphysis interface, which behaves as a mineralization inhibition "
  "zone, while the metaphyseal interface carries the same inhibitors PLUS ENPP1 and ALPL and behaves as a promotion "
  "zone. A size-exclusion mechanism may make this spatially precise: fetuin is excluded from the interior of the "
  "collagen fibril, so intrafibrillar mineral can form by inhibitor exclusion while extrafibrillar mineral is "
  "suppressed."),
 quantitative=[],
 localization=['human GP-epiphysis interface: AHSG enriched at the mineralization inhibition zone (xie2025)',
  'human GP-metaphysis interface: AHSG present but coexisting with ENPP1 and ALPL (xie2025)',
  'serum: liver-derived, reaches mineralizing tissue from the circulation (schafer2003)'],
 human_evidence='direct',
 human_evidence_note='AHSG protein has been localised directly in human paediatric growth plate tissue at a defined mineralization boundary.',
 species_basis=['human','mouse','in_vitro_animal_cell'], translation_risk='low',
 translation_risk_reason='Mouse loss-of-function and human tissue localisation agree, and the biophysical mechanism is defined on the purified human protein.',
 confidence='B',
 key_refs=[
   dict(ref_id='schafer2003', pmid='12897203', first_author='Schafer C', year=2003, type='primary', one_line_finding='Ahsg-null mice develop widespread ectopic calcification, establishing fetuin-A as a systemic calcification inhibitor'),
   dict(ref_id='heiss2003', pmid='12556469', first_author='Heiss A', year=2003, type='primary_abstract_only', one_line_finding='Fetuin-A forms soluble colloidal calciprotein particles with calcium phosphate rather than adsorbing to crystal faces'),
   dict(ref_id='price2009', pmid='19414589', first_author='Price PA', year=2009, type='primary_abstract_only', one_line_finding='Fetuin is excluded from the collagen fibril interior, so mineralization proceeds intrafibrillarly by inhibitor exclusion'),
   r_xie],
))
