# benchmark_run.md — answers from the Human Growth System Atlas
Run date: 2026-08-05. Protocol: QUERY.md.
Load order followed: derived.json → graph.json → parameters.json → gaps.json; coverage.md read before answering (§8).

**Layer warning carried into every answer below** (coverage.md): L2 = 0% replicated-human, 69% high translation risk;
L3 = 11% replicated-human; L8 = 3 nodes, unswept. L11/L12/L9/L10 are the strong (83–100% direct-human) layers.
Only 468/764 edges are `traversal_usable`; 296 (`precedes`, `binds`, `correlates_with`, `hypothesized_link`) are
excluded from every path in this file. Edge-context fill rates: species 94%, stage/age 11.3%, sex 6.2%, zone 5.5%.

---

### q01  [entity]
CLAIM: NPR2 is a homodimeric transmembrane receptor guanylyl cyclase whose CNP-driven cGMP output is a graded three-state human dosage locus for stature.
PROVENANCE: [ATLAS]
CONFIDENCE: B
SPECIES_BASIS: human, mouse
PATH: npr2_receptor (node read only; no traversal)
REFS: bartels2004, olney2006, hanley2020, vasques2013, wang2015, hannema2013, lauffer2020, nakao2015, agoston2007
GAPS_CROSSED: none traversed; node carries open questions g_l3core_003, g_l3core_004
OPERATION: Type 1 ENTITY — node read + claim_grades check. `claim_grades` is null on this node, so the node-level grade B is the only grade available.
ANSWER: CNP binding activates the intracellular cyclase to make cGMP from GTP; activity requires phosphorylation of seven juxtamembrane Ser/Thr plus ATP binding to the pseudokinase domain. Human dosage series: biallelic loss → acromesomelic dysplasia Maroteaux type, adult height ~120–134 cm; heterozygous loss → ~1.4–1.7 SDS below non-carrier relatives, worsening with age; gain-of-function → tall stature with macrodactyly. Cartilage-specific mouse Npr2 deletion partitions onto the hypertrophic zone (type-X-positive layer to 23.0% of control vs 71.1% non-hypertrophic; femur 45.3%, tibia 54.6% of control length at 10 weeks). The node flags an internal contradiction (nakao2015 vs agoston2007) on whether zonal NPR2 distribution explains the zonal partition — see q19.

### q02  [entity]
CLAIM: The groove of Ranvier is a circumferential perichondrium-continuous wedge of dense cellular tissue at the plate periphery that is presumed to supply cells for latitudinal enlargement.
PROVENANCE: [ATLAS]
CONFIDENCE: C
SPECIES_BASIS: rabbit, human, porcine
PATH: groove_of_ranvier (node read only)
REFS: shapiro1977, cheng1995, walzer2014, langenskild1998
GAPS_CROSSED: none traversed; open question g_l1arch_013
OPERATION: Type 1 ENTITY — node read; `claim_grades` null, node grade C used.
ANSWER: Established in rabbit for cellular organisation and direction of cell flow from perichondrium into the plate margin; confirmed present in human calcaneus and talus and, in human polydactylous digits, harbouring CD90+/CD105+ mesenchymal progenitors and mature alpha-SMA-covered vessels. Its clinical significance is negative — groove disorganisation causes congenital hyperostosis in piglets and injury is implicated in angular deformity and osteochondroma. Translation risk is moderate: the structure is human-confirmed but its *function* rests on rabbit morphology and has never been tested by lineage tracing in any species, and no study has apportioned plate diameter increase between groove and interstitial growth (g_l1arch_013).

### q03  [mechanism]
CLAIM: The atlas cannot carry a GH secretory pulse to a micrometre of tibial length — the chain breaks at three unusable edges and at two missing unit conversions.
PROVENANCE: [ATLAS-INFERRED]
CONFIDENCE: C (weakest node in the attempted path: gh_pulse_pattern_hypothesis C, elongation_budget C, e00428/e00429 both C)
SPECIES_BASIS: rat (pulse-pattern and elongation-budget evidence), human (GH deconvolution only), pig, mouse
PATH: gh_secretion_pulsatility –e00420(+,A)→ growth_hormone –e00421(binds, **UNUSABLE**)→ gh_receptor –e00422(+,A)→ jak2_kinase –e00423(+,A)→ stat5b_tf ✗DEAD END. Alternate arm: growth_hormone –e00429(+,C)→ igf1_local_growth_plate –e00433(binds, **UNUSABLE**)→ igf1_receptor ✗. Alternate arm: growth_hormone –e00428(+,C)→ resting_zone –e00004(precedes, **UNUSABLE**)→ proliferative_zone ✗. Terminal segment that does exist: chondrocyte_hypertrophy –e00010(+,C)→ elongation_budget –e00013(+,C)→ growth_velocity_longitudinal.
REFS: gevers1996, gevers1996a, hornsby2025, wilsman1996, hunziker1989, hunziker1987, breur1991
GAPS_CROSSED: e00431 (gh_pulse_pattern_hypothesis → growth_velocity_longitudinal) is a **hypothesized_link, confidence speculative** — the only edge in the graph that connects GH pattern directly to velocity, and it is not traversable. Open gaps g_l4endo_002, g_l1arch_001, g_l9organism_001.
OPERATION: Type 2 MECHANISM — path trace carrying units, reporting the breaks.
ANSWER: Units at each step: pulse is ng/mL·min of burst mass by 10-min-sampled deconvolution in humans; the receptor step is a `binds` edge with no sign, so it cannot be traversed; there is **no measurement of the GH concentration–time profile in growth plate interstitium in any species**, so the systemic→tissue unit conversion does not exist. The output end is in % of elongation (rat: 9% division / 32% matrix / 59% hypertrophy in proximal tibia; 44%/49% in proximal radius) and cells/day (16,400/day), measured only in 28-day-old Long-Evans rats elongating at 50–400 µm/day; human plates run at roughly 40 µm/day with a proliferative cycle inferred at ~20 days rather than ~31 h, so the rat partition cannot be transferred. There is also no published model deriving human cm/yr from plate cell kinetics (g_l9organism_001). The graph therefore cannot answer this directionally — that is the result.

### q04  [mechanism]
CLAIM: IHH restrains its own expression through a two-edge negative feedback loop: it transcriptionally raises periarticular PTHrP, and PTHrP delays the differentiation step at which Ihh is switched on.
PROVENANCE: [ATLAS] for the two edges; [ATLAS-INFERRED] for the sign product.
CONFIDENCE: B (both edges B; loop node pthrp_ihh_feedback_loop B)
SPECIES_BASIS: mouse, chicken (human: indirect, monogenic only)
PATH: ihh_protein –e00086(transcribes, +, B)→ pthrp_protein –e00085(inhibits, −, B)→ ihh_protein. Sign product = −1 → `negative_stabilising` cycle (derived.cycles, length 2, bistable: false). Both edges traversal_usable.
REFS: vortkamp1996, karp2000, koziel2004, kobayashi2002, lanske1996, stjacques1999
GAPS_CROSSED: none in the 2-cycle. Open gap g_l3core_001 (loop never characterised as a closed control system).
OPERATION: Type 2 MECHANISM — path trace with sign product; cycle class read from derived.cycles rather than recomputed.
ANSWER: Chondrocytes leaving the effective range of PTHrP exit the cycle and switch on Ihh; Ihh signals back via PTCH1/SMO, relieving GLI3 repressor, and raises Pthlh transcription periarticularly. Note e00085 is *indirect* — PTHrP delays the differentiation step rather than repressing Ihh transcription — so the loop is a differentiation-timing loop, not a transcriptional autorepression. Loop geometry sets proliferative column length and is limited by heparan sulfate/DISP1 (Ext1 hypomorph expands the range; Disp1 hypomorph shortens it). Units and gain are unmeasured: the atlas notes the loop has never been characterised quantitatively as a closed control system in any species, human included.

### q05  [perturbation]
CLAIM: FGFR3 inhibition inverts the sign of every one of the 70 nodes reachable from fgfr3_receptor — 35 that FGFR3 activation raises fall, 35 that it lowers rise — but the propagation is almost entirely murine and never reaches adult height.
PROVENANCE: [ATLAS-INFERRED]
CONFIDENCE: C (weakest edges in the dominant sub-paths: e00370 C, e00298 C, e00133 C)
SPECIES_BASIS: mouse (edge contexts), human (the four disease edges e00200/e00202/e00204/e00205, all grade A)
PATH: derived.reachability['fgfr3_receptor'] — 70 nodes, depth 1–4; 11 usable out-edges (e00128, e00129, e00133, e00139, e00152, e00200, e00202, e00204, e00205, e00298, e00370). Under inhibition every stored sign flips: e.g. npr2_receptor +1 (was −1 via e00152), pthrp_ihh_feedback_loop +1, bmp_signaling_growth_plate +1, chondrocyte_proliferation_rate +1, hypertrophic_zone +1, elongation_budget +1, epiphyseal_fusion +1, growth_velocity_longitudinal −1 (via e00370→e00369→e00591→e00044).
REFS: wagner2021, shuhaibar2017, ozasa2005, minina2002, zhou2015, colvin1996, deng1996, horike2026, shiang1994
GAPS_CROSSED: e00370 (fgfr3→sox9, +) is flagged on the edge itself as contradicting the requirement direction in Dy 2012 and is logged as gap **g_l3rest_012** — and it is the parent of 22 of the 70 reachable nodes, so a large fraction of this prediction hangs on a contested edge. Say so plainly.
OPERATION: Type 3 PERTURBATION — precomputed reachability with sign products; no context filter was specified in the question, so none was applied. Excluded by the traversal rule: all 296 unusable edges globally, including every `binds` route out of the receptor complex.
ANSWER: The sign-flipped prediction: proliferation rate, BMP signalling, PTHrP/IHH loop activity, NPR2 output, hypertrophic zone size and the elongation budget all rise; SOX9, SOX5/6, the SOX trio, column formation, collagen II and aggrecan all fall (because the atlas's SOX9 edge is *positive* from FGFR3 — the contested direction). The graph's own arithmetic therefore predicts that FGFR3 inhibition **reduces** growth_velocity_longitudinal at depth 4, which contradicts the human trial edge e00720 (infigratinib activates growth_velocity, +1.74 cm/yr, grade A). That disagreement is the finding: it is entirely attributable to e00370/g_l3rest_012 and is presented rather than resolved. Note also 3 of the 4 disease edges are `required_for` from receptor to syndrome — they encode which allele causes which disease, not a dose-response.

### q06  [perturbation]
CLAIM: Vosoritide propagates to 38 nodes at depth ≤4 and stops entirely inside the signalling network — it never reaches growth_velocity_longitudinal or adult_height_attainment in the graph.
PROVENANCE: [ATLAS-INFERRED]
CONFIDENCE: B (entry edge e00214 is A; the sign-carrying relay e00142/e00152 is B; downstream limbs fall to C)
SPECIES_BASIS: human (e00214, vosoritide node), mouse (everything downstream of npr2_receptor)
PATH: vosoritide –e00214(+,A)→ npr2_receptor –e00107(+)→ cgmp_second_messenger; –e00142(−)→ fgfr3_receptor, then the whole FGFR3 subtree with signs inverted (achondroplasia −1, sox9_tf −1, runx2_tf +1, bmp_signaling +1, ihh_protein +1, chondrocyte_proliferation_rate +1, hypertrophic_zone +1). Terminal depth 4. Only one out-edge exists from vosoritide and no in-edges.
REFS: savarirayan2020, savarirayan2024, dauber2026, alfaraj2026, wagner2021, shuhaibar2017
GAPS_CROSSED: none speculative in the path. But the *stop* is the answer.
OPERATION: Type 3 PERTURBATION — reachability with sign products. Excluded by the traversal rule: `binds` edges out of the receptor layer; no context filter requested.
ANSWER: Propagation is: vosoritide → NPR2 → cGMP, and NPR2 ⊣ FGFR3 → the entire FGFR3 signalling subtree with every sign inverted relative to FGFR3 activation. It stops at depth 4 (β-catenin, SOX5/6, RUNX2, IHH, SMAD1/5/8, HDAC4, GSK3B, hypertrophic_zone, and the Jansen/Blomstrand/Noonan disease nodes). **It does not reach growth_velocity_longitudinal, adult_height_attainment, elongation_budget or epiphyseal_fusion.** Comparable agents do have such edges (navepegritide e00715, infigratinib e00720, rhGH e00726 all activate growth_velocity, grade A), so this is a missing edge in the graph rather than a claim that vosoritide has no growth effect — the node itself records +1.57 cm/yr (95% CI 1.22–1.93). Logged as a coverage gap.

### q07  [perturbation]
CLAIM: The graph predicts only three consequences of raised glucocorticoid exposure, all negative and all at depth 1, and the age-11/female context filter excludes two of the three edges.
PROVENANCE: [ATLAS-INFERRED]
CONFIDENCE: B unfiltered (e00455 B, e00261 B); C if e00456 is retained
SPECIES_BASIS: rabbit (5-week-old **male**), human (childhood, sex unstated)
PATH: BFS from glucocorticoid_cortisol over traversal_usable edges only (this node is not in the precomputed reachability set, so it was computed). Depth 1: –e00455(inhibits, −, B)→ growth_velocity_longitudinal; –e00456(inhibits, −, C)→ resting_zone; –e00261(required_for, −, B)→ cushing_syndrome_growth. Depth 2: none — growth_velocity_longitudinal has no usable out-edges, resting_zone's only out-edge e00004 is `precedes` (unusable), cushing_syndrome_growth has no out-edges. Total reachable set = 3 nodes.
REFS: (edge refs) rabbit unilateral intra-plate infusion series; node glucocorticoid_cortisol, cushing_syndrome_growth
GAPS_CROSSED: e00457 (glucocorticoid_cortisol → catch_up_growth) is `precedes` and was **excluded**, so the graph cannot tell you directionally whether the suppression is recoverable. Gaps g_l4endo_011 (contradiction), g_l4endo_003, g_l12b_021, g_l12b_023.
OPERATION: Type 3 PERTURBATION — computed reachability with sign products, **filtered by context**. EXCLUDED BY THE FILTER: e00455 (context "5-week-old male rabbits, 80 ng/µL at 1 µL/h into one plate") — wrong species and explicitly male; e00456 (rabbit, sex and age unstated). EXCLUDED BY THE TRAVERSAL RULE: e00457 (`precedes`). SURVIVING the filter: e00261 only ("human, endogenous or exogenous glucocorticoid excess in childhood") — and it carries no sex and no age.
ANSWER: Unfiltered, the prediction is uniformly negative: growth velocity down, resting zone activity down, Cushing-type growth failure. Filtered for an 11-year-old girl, **one edge survives and it is not sex- or age-resolved**, so the sex- and age-specific answer is not in the graph. This is the weak-context-filtering problem coverage.md warns about (sex named in 6.2% of edge contexts, stage/age in 11.3%). The atlas also holds an unresolved contradiction here (c_l4endo_02 / g_l4endo_011): pharmacological glucocorticoid suppresses growth 77% on unilateral rabbit infusion, yet chondrocyte-specific GR knockout in mouse is largely dispensable — so even the local-versus-systemic locus of action is disputed.

### q08  [perturbation]
CLAIM: Suppressing SOX9 does both — it amplifies through one bistable positive loop and is damped by three negative-stabilising loops, and it propagates to 59 nodes.
PROVENANCE: [ATLAS-INFERRED]
CONFIDENCE: C (weakest edges in the dominant sub-paths are C)
SPECIES_BASIS: mouse (dominant), human in the disease terminals only
PATH: derived.reachability['sox9_tf'] = 59 nodes, depth 1–5, 26 positive / 33 negative under SOX9 *activation*; all invert under suppression. Depth-1 set: beta_catenin_ctnnb1 (−), runx2_tf (−), chondrocyte_to_osteoblast_transdifferentiation (−), amino_acid_sensing_chondrocyte (+), sox5_tf (+), sox6_tf (+), sox_trio (+), chondrocyte_column_formation (+), sox9_chondrogenic_commitment (+), pathway_convergence_node (+).
Cycles containing sox9_tf: positive_amplifying [beta_catenin_ctnnb1, sox9_tf] e00315/e00314 **bistable: true**; positive_amplifying [sox9_tf, amino_acid_sensing_chondrocyte] e00344/e00345; negative_stabilising ×3 (all routed through pthrp_protein → … → runx2_tf/bmp → ihh_protein).
REFS: zhou2015 (and the contested Dy 2012 direction)
GAPS_CROSSED: **g_l3rest_012** — an open `contradiction` gap on whether SOX9 is required for hypertrophy or must be downregulated for it. Every sign in this answer depends on which direction is right.
OPERATION: Type 3 PERTURBATION — reachability + sign products + cycle-class lookup. No context filter requested; note 22 of 59 nodes are reached only through the contested e00370/e00314 corridor.
ANSWER: Amplification: SOX9 and β-catenin form a bistable mutually-reinforcing 2-cycle, so a suppression of SOX9 is self-reinforcing rather than self-correcting at that node — the classic signature of a switch, and the atlas explicitly flags it bistable. Damping: three negative-stabilising cycles run SOX9 → RUNX2/BMP → IHH → PTHrP → back, which oppose the excursion. The graph therefore predicts **local amplification inside a bistable switch, embedded in a globally stabilising network** — not a single answer. Because the direction of the SOX9–hypertrophy relation is itself an open contradiction (g_l3rest_012), the sign of the whole 59-node prediction is not secure.

### q09  [perturbation]
CLAIM: The atlas holds 10 positive/amplifying loops (6 of them bistable) against 17 negative/stabilising loops, and the brakes exist because the same four hubs sit in both classes — but all of it is confined to L3/L12 plus one L4 loop.
PROVENANCE: [ATLAS] (cycles are precomputed in derived.json) with [ATLAS-INFERRED] on the brake-sharing analysis
CONFIDENCE: B–C (loop edges range A to C; the NPR2/FGFR3 loops are B, the IHH/BMP loops C)
SPECIES_BASIS: mouse and chicken for the IHH/BMP/SOX9 loops; mouse+rat for NPR2/FGFR3; human for the GH–SOCS2 loop
PATH: derived.cycles / derived.cycle_summary. POSITIVE (10): [ihh, smoothened, gli3_repressor] **bistable**; [ihh, bmp_signaling]; [ihh, bmp2, bmp_signaling]; [npr2, cgmp, pkg2, npr2_agonist_class, fgfr3_mapk_branch] **bistable**; [npr2, fgfr3, fgfr3_mapk_branch] **bistable**; [npr2, fgfr3, fgfr3_npr2_crosstalk] **bistable**; [npr2, fgfr3] **bistable**; [cgmp, pkg2, npr2_agonist_class]; [beta_catenin, sox9] **bistable**; [sox9, amino_acid_sensing_chondrocyte].
NEGATIVE (17): 7 through pthrp_protein↔ihh_protein (including the 2-cycle e00085/e00086), 2 through the pthrp_ihh_feedback_loop node, [cnp_protein, npr3_clearance_receptor], 4 through npr2/cgmp/mek1_erk/fgfr3, 2 within fgfr3 branches, and [gh_receptor, jak2, stat5b, socs2].
REFS: per-edge; see e00085/e00086, e00142/e00152, e00314/e00315, e00097/e00089/e00090
GAPS_CROSSED: none — cycles are built only from traversal_usable edges. All `timescales` fields are null, so no loop has a measured time constant.
OPERATION: Type 3 PERTURBATION — cycle enumeration and class read directly from derived.cycles (not recomputed).
ANSWER: Yes, every positive loop has a brake, and the brake is topological rather than separate: IHH↔BMP amplification is opposed by seven IHH→PTHrP→IHH negative loops; NPR2↔FGFR3 amplification is opposed by four negative loops through cGMP→MEK/ERK→FGFR3; SOX9↔β-catenin amplification is opposed by three PTHrP-routed negative loops; and the GH axis brake (GHR→JAK2→STAT5B→SOCS2) is purely negative with no positive counterpart. Two structural caveats: (i) all 27 cycles lie in L3, L12 or L4 — the atlas has **no** characterised feedback loop in L1 architecture, L5 matrix, L6 mechanobiology or L7 fusion, so "does it have a brake" is unanswerable in those layers; (ii) no cycle carries a timescale, so loop gain and settling time are unmeasured everywhere.

### q10  [comparative]
CLAIM: On the two axes the atlas can compute, FGFR3 outranks CNP/NPR2 for stature; on the other two axes the atlas has no data at all, so the ranking is two-of-four, not four-of-four.
PROVENANCE: [ATLAS] for the effect sizes and convergence; [COVERAGE-GAP] for the two elasticity axes and the GWAS axis
CONFIDENCE: A for the human effect sizes (merker2018, olney2006, savarirayan2020 all A/B); B for convergence
SPECIES_BASIS: human (all effect sizes), mouse (mechanistic weighting)
PATH: derived.convergence[fgfr3_receptor] = 10 inbound / 2 layers (L3, L12); derived.convergence[npr2_receptor] = 8 inbound / 2 layers (L3, L12). Nodes: achondroplasia, acromesomelic_dysplasia_maroteaux, npr2_heterozygous_short_stature, npr2_gain_of_function_tall, vosoritide, infigratinib_growth, height_gwas.
REFS: merker2018, horton1978, bartels2004, olney2006, savarirayan2020, yengo2022
GAPS_CROSSED: g_l8gwas_001 (open quantitative_gap), g_l11path_006, g_l11path_003
OPERATION: Type 4 COMPARATIVE — four-way ranking attempted; all four reported including the two that fail.
ANSWER: **(1) Velocity elasticity — NOT COMPUTABLE.** The string "elasticity" does not occur anywhere in graph.json, parameters.json, derived.json or gaps.json; the atlas has no elasticity field of any kind. The nearest substitutes are trial effect sizes and both are FGFR3-axis: vosoritide +1.57 cm/yr (CI 1.22–1.93) and infigratinib +1.74 cm/yr, so they do not discriminate. **(2) Final-height elasticity — NOT COMPUTABLE as an elasticity**, but the raw human effect sizes rank FGFR3 first: one FGFR3 G380R allele → 132 cm (M) / 124 cm (F); one lost NPR2 allele → ~1.4 SDS (~9 cm); biallelic NPR2 loss → 120–134 cm, i.e. comparable to *heterozygous* FGFR3. **(3) GWAS enrichment — UNKNOWN.** g_l8gwas_001 is an open gap asking exactly what fraction of the 12,111 height SNPs act through the growth plate; L8 has 3 nodes and is unswept. **(4) Graph convergence — FGFR3 10 inbound / 2 layers vs NPR2 8 / 2.** Disagreement to report: the axes that favour FGFR3 are gene-dose axes, while pharmacologically the two converge (NPR2 agonism is the licensed treatment for FGFR3 disease, via edge e00142/e00152), so "matters more" has opposite answers depending on whether you mean per-allele burden or per-target tractability.

### q11  [comparative]
CLAIM: There is no single winner — growth_velocity_longitudinal and adult_height_attainment tie on inbound edges (25 each) while epiphyseal_fusion wins on layer breadth (22 inbound from 7 layers).
PROVENANCE: [ATLAS] (derived.convergence, precomputed)
CONFIDENCE: n/a (structural property of the graph, not an evidential claim)
SPECIES_BASIS: n/a
PATH: derived.convergence, ranks 1–3: growth_velocity_longitudinal 25 inbound / 6 layers [L0, L1, L12, L13, L4, L9]; adult_height_attainment 25 / 4 [L11, L12, L7, L9]; epiphyseal_fusion 22 / 7 [L11, L13, L2, L3, L4, L7, L9]. Rank 4–6: igf1_systemic 19/3, bone_age 18/5, chondrocyte_hypertrophy 18/2.
REFS: n/a
GAPS_CROSSED: none
OPERATION: Type 4 COMPARATIVE — convergence axis; disagreement between the two orderings reported rather than collapsed.
ANSWER: If "most inbound" is the criterion, it is a tie at 25 between growth_velocity_longitudinal and adult_height_attainment. If "from the most layers" is the criterion, epiphyseal_fusion wins with 7 of 14 layers converging on it despite having fewer inbound edges. The node that is jointly top on both criteria is **growth_velocity_longitudinal** (25 inbound, 6 layers) and that is the best single answer, but it should be reported alongside epiphyseal_fusion, which is the atlas's genuine cross-layer sink. Note chondrocyte_hypertrophy is high-degree (18) but narrow (2 layers) — degree and breadth are not the same measure here.

### q12  [evidence]
CLAIM: Oestrogen-dependence of human fusion rests on two mirror-image experiments of nature — ESR1 nonsense (receptor dead, plates stay open) and CYP19A1 loss (ligand absent, plates close on estradiol) — in a literal handful of individuals.
PROVENANCE: [ATLAS]
CONFIDENCE: B
SPECIES_BASIS: human (only)
PATH: estrogen_driven_fusion (node read) + epiphyseal_fusion (A) for the endpoint
REFS: smith1994, smith2008, morishima1995, carani1997, singhania2022, rochira2009
GAPS_CROSSED: g_l7fuse_005, g_l7fuse_009. `pending_source: carani1997` — the interventional key reference is flagged pending on the node.
OPERATION: Type 5 EVIDENCE — key_refs + confidence + human_evidence + translation_risk, distinguishing established-in-humans from inferred.
ANSWER: Established in humans, not inferred: human_evidence = **direct**, translation_risk = **low**, species_basis = human alone. The ESR1 propositus (homozygous codon-157 stop) was 204 cm with incomplete closure, elevated estradiol/estrone, normal testosterone, and six months of transdermal oestrogen producing a 10-fold rise in free estradiol had no effect; on follow-up his bone age advanced only 15 → 17.5 y over 3.5 y. The aromatase-deficient man was 204 cm (+3.7 SD) with bone age 14 y at chronological age 24.25 y, and transdermal estradiol — but not six months of high-dose testosterone — produced complete closure and growth arrest. What is *not* established: these are single cases with no untreated control course and unblinded treatment responses, and no human growth plate ER-alpha localisation at fusion has ever been reported. The confidence is B for exactly that reason — the mechanism is human and interventional, the sample is n≈1 per arm.

### q13  [evidence]
CLAIM: Vosoritide's growth-velocity effect is grade-A randomised human evidence; its adult-height effect is not evidence at all.
PROVENANCE: [ATLAS]
CONFIDENCE: A
SPECIES_BASIS: human (efficacy), mouse (mechanism only)
PATH: vosoritide (node read); parameters.by_node[vosoritide]; gap g_l12pharm_001
REFS: savarirayan2020, savarirayan2024, dauber2026, alfaraj2026, kamrulhasan2026
GAPS_CROSSED: g_l12pharm_001 (`search_established`, tractability 4), g_l3core_003, g_mr002_h1/h2/h3
OPERATION: Type 5 EVIDENCE — key_refs + confidence + human_evidence + translation_risk.
ANSWER: human_evidence = **direct**; translation_risk = **low**, and the node states explicitly that the residual translation risk concerns *mechanism*, not effect. Pivotal 52-week phase 3 NCT03197766, n=121, ages 5–<18 y, 15.0 µg/kg/day: adjusted mean +1.57 cm/yr vs placebo (95% CI 1.22–1.93). Class meta-analysis of 11 studies (N=542; 4 RCTs, n=326): pooled +1.36 cm/yr (95% CI 1.05–1.68). Efficacy extended below age 5 and tested in a basket trial including ACAN and NPR2 deficiency. The boundary: growth velocity is a surrogate, the pivotal trial's own authors say final adult height is not established by these data, and a systematic Europe PMC search on 2026-08-05 ("vosoritide AND final/near-adult height", 64 hits, 20 screened) found no report of achieved adult height in any CNP-analogue-treated cohort. Which cellular process is being modulated in humans is also unmeasured (g_l3core_003).

### q14  [evidence]
CLAIM: The PTHrP+ resting chondrocyte stem cell is a well-evidenced *mouse* cell type with zero human support, and the one human study to look reports the analogous population is PTHLH-negative.
PROVENANCE: [ATLAS]
CONFIDENCE: C
SPECIES_BASIS: mouse (only)
PATH: pthrp_positive_resting_chondrocyte (node read)
REFS: mizuhashi2018, muruganandan2022, trompet2024, chu2026
GAPS_CROSSED: g_l2stem_001 (`method_blocked`), g_l2stem_003, g_l2stem_010; node `contradicts` foxa2_resting_chondrocyte and prrx1_root_stem_cell
OPERATION: Type 5 EVIDENCE — key_refs + confidence + human_evidence + translation_risk.
ANSWER: **Layer warning first (coverage.md §): L2 has 0% replicated-human nodes and 69% high translation risk; an answer about resting-zone stem cells is an answer about mice.** The mouse evidence is strong and quantitative: PTHrP-creER pulsed at P6 labels cells that stay resting ~1 week then generate monoclonal (Confetti) columns for ≥1 year; descendants become Col1a1-GFP+ osteoblasts and Cxcl12-GFP+ stroma but not adipocytes (0/443 under rosiglitazone + high-fat diet). But only ~2–3% of PTHrP+ colony-forming cells behave as long-term stem cells (16.3% secondary colonies × 12.5% passageable ×9). human_evidence = **absent**; translation_risk = **high**, because inducible-Cre lineage tracing cannot be done in humans at all. chu2026 reports the human pubertal resting-zone "root" population does **not** express PTHLH — a direct challenge to the marker. muruganandan2022 further reports PTHrP+ colonies are much shorter-lived than FoxA2+ (1.4% vs 9% to late passage). The atlas holds this as an active three-way disagreement, not a settled cell type.

### q15  [negative]
CLAIM: The atlas holds 11 established gaps in L2 covering the resting zone, of which 5 are `search_established` with reproducible null search logs.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (negative space)
SPECIES_BASIS: n/a — the point of most of these gaps is that no human basis exists
PATH: gaps.by_layer['L2'] (11 gaps) plus resting-zone-tagged gaps in other layers (g_l1arch_013, g_l3rest_010, g_l4endo_003, g_l7fuse_001)
REFS: search_logs g_l2stem_001, g_l2stem_003, g_l2stem_005, g_l2stem_007, g_l2stem_009
GAPS_CROSSED: n/a — the gaps are the answer
OPERATION: Type 6 NEGATIVE — gaps.json filtered by layer, with search logs attached.
ANSWER: The eleven: **g_l2stem_001** (method_blocked) which human RZ cell, if any, self-renews and clonally makes columns over years, and does it express PTHLH; **g_l2stem_002** what fraction of human osteoblasts is chondrocyte-derived; **g_l2stem_003** (search_established, tractability 4) does SOC formation *cause* RZ stemness or merely coincide — Europe PMC 2026-08-05, `("secondary ossification cent*") AND (ablat* OR block* OR prevent* OR delay*) AND ("resting zone" OR "stem cell" OR self-renewal) AND (mouse OR mice)` → **0 records**; **g_l2stem_004** (contradiction) are the five skeletal stem cell schemes distinct cell types; **g_l2stem_005** (search_established) do human RZ chondrocytes have finite division-denominated capacity — 213 records screened, none a primary human measurement; **g_l2stem_006** is RZ depletion a cause or consequence of fusion; **g_l2stem_007** does telomere length shorten in human plate chondrocytes; **g_l2stem_008** how many divisions does a human RZ progenitor start with; **g_l2stem_009** does the hSSC panel (PDPN+CD146−CD73+CD164+) label human RZ; **g_l2stem_010** what fraction is genuinely long-term self-renewing in vivo (is 2–3% an in-vitro artefact); **g_l2stem_011** does any non-murine mammal show the postnatal clonal switch. The common root: every one of these needs either lineage tracing (impossible in humans) or human tissue that does not exist in quantity — 102 postnatal growing human growth plates in the entire literature.

### q16  [negative]
CLAIM: The atlas does not rank gaps by value — only by `tractability` 1–5 — so any "single highest-value" answer is derived; on the derived criterion the winner is a zone-resolved human growth plate spatial transcriptome (g_l13data_001).
PROVENANCE: [ATLAS-INFERRED]
CONFIDENCE: n/a
SPECIES_BASIS: n/a
PATH: gaps.by_tractability['5'] = 17 gaps; ranked by (number of other gaps closed) × tractability. g_l13data_001 (tractability 3) is the unique gap whose closure directly closes g_l3core_006 (human zonal PDE isoforms), g_l0dev_004 (zonal HOX), g_l6mech_007 (PIEZO1/2), g_l3rest_010 (zonal mTORC1), g_l13b_005 (zone-resolved human ISH map), and constrains g_l13b_009 (rat→human transcriptome concordance).
REFS: geo_census_20260805, gse267139, gse288028
GAPS_CROSSED: n/a
OPERATION: Type 6 NEGATIVE — gaps filtered and cross-referenced; explicit statement that the ranking field asked for does not exist.
ANSWER: The atlas has no "value" field. What it has is `tractability` (1–5, 17 gaps at 5) and `why_it_matters` prose. Deriving from those: g_l13data_001 states in its own discriminating_experiment that it is "the single highest-value experiment identified in this layer," and structurally it is the only gap that is several other gaps expressed once — a GEO census on 2026-08-05 (`(growth plate) AND (spatial) AND Homo sapiens[Organism]`) returned **0 records**, while 7 non-human spatial records and 18 human single-cell records exist. Rival candidates, both defensible: **g_l12pharm_001** (does CNP-analogue therapy raise final adult height — the endpoint every approved drug in L12 is licensed without), and **g_l6mech_002/x-L6-02** (the human stress–growth coefficient, extrapolated into every guided-growth and vertebral-tethering operation performed today). I decline to collapse these to one on atlas authority, because the atlas does not contain the ranking.

### q17  [contradiction]
CLAIM: There is no single elastic modulus for the hypertrophic zone — the published values span three orders of magnitude (380 kPa to 416 MPa) and the direction of the zonal gradient disagrees between studies.
PROVENANCE: [ATLAS]
CONFIDENCE: C (zonal_stiffness_gradient); the human value (xie2025) is a single-source parameter
SPECIES_BASIS: newborn porcine, 9-week rabbit, rabbit cranial base, human (phalangeal 0–5 y and tibial)
PATH: parameters.by_node['zonal_stiffness_gradient'] and ['mineralization_front']; audit/contradictions.md row **c_l5matrix_02**
REFS: sergerie2009, eckstein2022, radhakrishnan2004, xie2025
GAPS_CROSSED: g_l5matrix_008 (direction), g_l5matrix_001 (the missing hydrated tissue-scale human number)
OPERATION: Type 7 CONTRADICTION — spread + methodological reason returned; **no central estimate given**. Note: this parameter is *not* in `parameters.disputed` (which holds only 5 keys, all IGFBP-3/PHV); the contradiction lives in audit/contradictions.md, which is where the protocol sends you.
ANSWER: The spread: **416.20 MPa (SD 107.18)** for HZ by sharp-tip AFM on hydrated human cryosections (9 nm tip, 26 N/m cantilever, 6 µN, Hertz conical fit), against RZ 130.70 MPa in the same donors (xie2025); **380–690 kPa** Hertz reduced modulus peaking in the *upper* hypertrophic zone in 9-week rabbit proximal tibia by microindentation (eckstein2022); **1.41 MPa (SD 0.19)** for the mineralizing zone in rabbit cranial base AFM, rising monotonically from 0.57 MPa reserve (radhakrishnan2004); and sergerie2009 in newborn porcine distal ulna finds the **reserve** zone stiffest, with PZ and HZ half as stiff axially. The methodological reason: the studies differ simultaneously in species (pig/rabbit/human), site (weight-bearing long bone vs cranial base vs phalanx), age (newborn to 14 years) and method/length scale (bulk unconfined compression vs microindentation vs 9-nm-tip AFM). A 1,000-fold magnitude range is itself proof the methods are not measuring the same physical quantity. Load-bearing for every finite-element model of physeal loading, guided growth and Salter-Harris fracture propagation.

### q18  [contradiction]
CLAIM: Sources agree on the *magnitude* of peak height velocity to within 0.1 cm/yr but disagree on the *age* at which it occurs by up to 1.1 years.
PROVENANCE: [ATLAS]
CONFIDENCE: A for magnitude (node claim_grade A: "three independent longitudinal cohorts on two continents fitted with the same shape-invariant model agree to within 0.1 cm/yr"); B for the timing/amplitude variance decomposition
SPECIES_BASIS: human (only)
PATH: parameters.disputed — 4 of the 5 disputed keys are PHV keys: 'peak height velocity, boys', 'age at peak height velocity, boys', 'peak height velocity, girls', 'age at peak height velocity, girls'. Node growth_velocity_curve (A).
REFS: chun2024, galvo2025, elhakeem2024, srensen2026, cole2010, cole2014, berkey1993, tanner1966a
GAPS_CROSSED: g_l9organism_002 (open quantitative_gap on residual SDs of competing growth models)
OPERATION: Type 7 CONTRADICTION — `parameters.disputed` spread + methodological reason; no central estimate.
ANSWER: Magnitude — boys 9.61 cm/yr (chun2024, SITAR, 123 Korean boys, 1519 heights) vs 9.52 (galvo2025, Bayesian SITAR, 201 Brazilian boys); girls 8.32 vs 8.38. That is agreement. Age at PHV — boys **12.46 y** (Korean) vs **13.55 y** (Brazilian); girls 10.99 vs 11.30; ALSPAC gives 13.5 y (males) and 11.8 y (females, SD 0.8, n=4267); Christ's Hospital boys 1939–1968 gives 14.3 y. Methodological reasons for the disagreement, in order of size: (i) genuine population and secular differences — Christ's Hospital is 0.8–1.8 y later than contemporary cohorts; (ii) timing and amplitude are not independent (earlier onset raises PHV by 1.82 cm/yr per year in boys, 1.39 in girls), so cohorts differing in pubertal timing must differ in PHV; (iii) a reporting artefact flagged on the parameter itself — chun2024 labels its dispersion SE but the magnitude is consistent with an individual-level SD. Also disputed downstream: whether a mid-growth spurt at 6–8 y exists at all is graded **D**, being model-dependent (visible to kernel regression and shape-invariant fits, invisible to Preece-Baines).

### q19  [contradiction]
CLAIM: No — NPR2 receptor distribution does not explain the zonal partition of the CNP effect, and the atlas holds the receptor and transducer data as an unresolved conflict.
PROVENANCE: [ATLAS]
CONFIDENCE: B (npr2_receptor); the zonal claim itself is the contested part
SPECIES_BASIS: mouse (both sides); human zonal map does not exist
PATH: npr2_receptor node — `contradicts: [nakao2015, agoston2007]`; localization field: "mouse PHZ: GC-B protein reported by IHC (nakao2015)" vs "mouse RZ, PZ and HZ: NPR2 transcript at similar levels across all three zones by zonal microarray (agoston2007)" vs "human growth plate: NPR2 zonal protein map unconfirmed"
REFS: nakao2015, agoston2007, miyazaki2022, savarirayan2020
GAPS_CROSSED: g_l3core_003 (quantitative_gap), g_l3core_004 (species_gap), g_l12b_003 (known_unknown — is the efficacy ceiling set by receptor occupancy or by PKG availability)
OPERATION: Type 7 CONTRADICTION — the disagreement and its methodological reason returned; no side picked.
ANSWER: The effect is strongly hypertrophic-weighted — cartilage-specific Npr2 deletion cuts the type-X-positive layer to 23.0% of control against 71.1% for the non-hypertrophic layer (and Nppc deletion 34.6% vs 76.7%). But NPR2 is reported at *similar* transcript levels in all three zones by zonal microarray, while the downstream kinases PKG-I/II are far higher in hypertrophic cells (agoston2007). The methodological reason for the conflict: nakao2015 reads GC-B **protein by IHC in PHZ**, agoston2007 reads **transcript by zonal microarray across RZ/PZ/HZ** — different analyte, different modality, and antibody specificity in cartilage is a known problem the atlas flags elsewhere. So the leading candidate explanation is the transducer (PKG-II), not the receptor, and that is exactly what g_l12b_003 asks. There is **no human zonal NPR2 protein map at all**, so the human version of this question is not merely unresolved, it is unmeasured.

### q20  [contradiction]
CLAIM: No — the five published skeletal stem cell schemes disagree on anatomy, adipogenic potential, developmental window and markers, and one immunophenotype is used for two anatomically different cells.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (this is a `contradiction`-typed gap, tractability 2)
SPECIES_BASIS: mouse for all five schemes; human only for the CD146+/hSSC definitions, which themselves disagree
PATH: gap g_l2stem_004; nodes mouse_skeletal_stem_cell_hierarchy, pthrp_positive_resting_chondrocyte, lepr_positive_stromal_cell, foxa_family_chondrocyte
REFS: chan2015, chan2018, debnath2018, worthley2015, zhou2014, shu2021, mizuhashi2018, sacchetti2007, bianco2015
GAPS_CROSSED: g_l2stem_004 itself; nearest_evidence is mizuhashi2018 alone, and the gap notes it is "the only cross-scheme quantification located"
OPERATION: Type 7 CONTRADICTION — spread + methodological reason; no reconciliation offered.
ANSWER: The disagreements, concretely: mSSC is CD45−Ter119−Tie2−AlphaV+Thy−6C3−CD105−CD200+ and **excludes** fat; the periosteal stem cell carries the **same** CD200+CD105−Thy−6C3− phenotype but is Ctsk-lineage and periosteal; Grem1+ OCR cells are metaphyseal, non-adipogenic and non-overlapping with Nestin-GFP; LepR+ cells are perisinusoidal, **do** make adipocytes, contribute nothing to developing cartilage and dominate osteoblast output only after adolescence; PTHrP+ resting chondrocytes are Grem1-negative. On the human side the CD146+ definition **includes** adipogenesis while the hSSC definition **excludes** it and reports CD146+ cells as poorer colony formers. The methodological reason is stated in the gap: no study has ever applied all marker panels and all Cre drivers to the same animals at the same ages with the same functional assay, so every "overlap" in the literature is inferred across papers rather than measured. Consequence the atlas draws: any therapeutic inference from L2 is currently arbitrary.

### q21  [contradiction]
CLAIM: No — growth plate severity is demonstrably non-monotonic in FGFR3 activation, and the atlas holds two independent non-monotonicities in the same allelic series.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (contradiction gap, tractability 3); underlying node fgfr3_receptor is B
SPECIES_BASIS: human (allele–phenotype), in_vitro (kinase activity)
PATH: gap g_l11path_004; node fgfr3_receptor; disease nodes achondroplasia, hypochondroplasia, saddan_syndrome, thanatophoric_dysplasia
REFS: tavormina1999, bellus2000, wilcox1998, naski1996, webster1996, sarabipour2016
GAPS_CROSSED: g_l11path_004; also g_l12b_004 and g_l12b_005 downstream (drug potency vs allele)
OPERATION: Type 7 CONTRADICTION — the two conflicting observations returned with their methodological reason.
ANSWER: Non-monotonicity 1: **K650M (SADDAN) has ~3× the constitutive kinase activity of K650E (thanatophoric dysplasia type II), yet K650M is survivable and K650E is lethal** (tavormina1999; four unrelated K650M individuals surviving past infancy). The same codon also generates weakly activating K650N/K650Q causing hypochondroplasia-like disease (bellus2000), so one residue spans the whole severity range non-monotonically. Non-monotonicity 2: **K650E growth plates are histologically better preserved than R248C and Y373C plates** (wilcox1998) — the opposite ordering from kinase activity. Methodological reason the atlas gives: kinase activity was measured in transient transfection in generic cells, not chondrocytes, and no study has compared downstream pathway usage (MAPK/ERK vs STAT1 vs PLCγ), receptor trafficking or ligand dependence between the alleles in chondrocytes. Lethality in TD is respiratory — thoracic cage and cranial base geometry — and nobody has asked whether the alleles differ on *those* elements rather than on long bones. Consequence: "reduce FGFR3 kinase output" (infigratinib, TYRA-300) targets a quantity that does not by itself determine outcome.

### q22  [design]
CLAIM: Delay secondary ossification centre formation without disturbing the plate, then assay resting-zone clonality and serial colony-forming capacity — the atlas holds this as a fully specified discriminating experiment at tractability 4.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (design)
SPECIES_BASIS: mouse (the experiment is mouse-only by construction; it cannot be done in humans)
PATH: gap g_l2stem_003 → `discriminating_experiment` field
REFS: mizuhashi2018, newton2019, chan2015
GAPS_CROSSED: g_l2stem_003 is `search_established` — the null is documented, not assumed
OPERATION: Type 8 DESIGN — discriminating_experiment field returned, with tractability.
ANSWER: **Design:** epiphysis-directed inhibition of cartilage-canal angiogenesis (local VEGF trap, or Vegfa deletion restricted to epiphyseal chondrocytes) initiated at P4; then at P12 and P18 assay (i) PTHrP-creER clonal column formation and (ii) secondary and serial colony-forming capacity of sorted resting chondrocytes. **Readouts:** if SOC formation is causal, delayed-SOC animals retain the P9-like phenotype (~3% secondary colonies, no serial passage) at P12–P18 and form only short transient columns; if the switch is autonomous, they reach the P12-like phenotype (~16% secondary colonies, passageable clones) on schedule despite an absent SOC. A comparative variant tests the same prediction across bones whose SOCs appear at different times within one animal. **Tractability 4.** Why it is needed: the current support is two temporal correlations in one species, and a Europe PMC search on 2026-08-05 for SOC-ablation-plus-resting-zone studies returned **0 records**. chan2015 is the nearest evidence (VEGF blockade shifts progenitor fate) but was never tested on the resting zone.

### q23  [design]
CLAIM: The atlas holds 17 gaps at maximum tractability (5), spread across nine layers, of which three are answerable from documents that already exist.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a
SPECIES_BASIS: mixed; the human-answerable ones are noted below
PATH: gaps.by_tractability['5']
REFS: per gap
GAPS_CROSSED: n/a
OPERATION: Type 8 DESIGN — gaps ranked by `tractability`.
ANSWER: The 17: **g_mr002_h3** (was the vosoritide dose set by an efficacy plateau or a blood-pressure cap — answerable by retrieving the FDA clinical pharmacology review for NDA 214938); **g_l12b_024** (the FDA multidisciplinary reviews for vosoritide/navepegritide/infigratinib); **g_l12b_005** (infigratinib IC50 vs G380R at stated ATP); **g_l12b_004** (does infigratinib inhibit N540K potently enough); **g_l0dev_004** (are HOX genes expressed in growth plate chondrocytes, and in which zone); **g_l0dev_009** (is differential elongation dominated by hypertrophic volume or proliferation — the Cooper 2013 vs Lui 2018 contradiction); **g_l6mech_002** (over what stress range is the growth–stress relation linear, and where are its saturation points); **g_l6mech_004** (do static and dynamic loading at equal mean stress suppress growth equally); **g_l3core_009** (BMP arm vs IHH arm contribution to column length); **g_l4endo_010** (does human SOCS2 loss cause overgrowth as the mouse predicts); **g_l10env_008** (how much of the ~20 cm/century secular gain is environmental); **g_l13b_001** (does any catalogued biobank of human growth plate tissue exist); **g_l13b_009** (does the rat zone-resolved transcriptome predict the human one); **g_l13b_011** (RNA integrity decay in human physeal cartilage vs post-mortem interval); **g_l9organism_002** (residual SDs of ICP/Preece-Baines/JPA-2/SITAR on the same curves); **g_l9organism_007** (proportion of infants crossing two major centiles against the WHO standard); **g_l9organism_009** (mean and SD of dental-minus-skeletal age). The three documentary ones — g_mr002_h3, g_l12b_024, g_l13b_001 — cost regulatory-document retrieval rather than tissue, and g_l13b_011 gates the feasibility of most of the L13 tissue programme.

### q24  [design]
CLAIM: The atlas frames the CNP exposure null as three named competing hypotheses (H1 downstream saturation, H2 diffusion-limited plate concentration, H3 tolerability-capped dosing) and gives each its own discriminating experiment; H3 is the one to run first.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (design); underlying observation graded on vosoritide (A) and navepegritide (A)
SPECIES_BASIS: human (the null itself), large-animal/mouse (H1 and H2 tests)
PATH: gaps g_mr002_h1 (species_gap, tractability 3), g_mr002_h2 (method_blocked, 3), g_mr002_h3 (known_unknown, **5**)
REFS: galetaki2026, savarirayan2020, savarirayan2023
GAPS_CROSSED: all three are open; none has been discriminated — this is QUERY.md §6's listed correction ("three hypotheses compete; none discriminated")
OPERATION: Type 8 DESIGN — discriminating_experiment fields ranked by tractability.
ANSWER: **Run H3 first (tractability 5, documentary).** Retrieve the FDA clinical pharmacology/biopharmaceutics review for NDA 214938 and read the dose-selection rationale: if efficacy plateaued, H3 is excluded; if the dose was tolerability-limited (CNP is vasoactive), then both agents sit below their biological ceiling and would look equivalent regardless of any downstream gating. The label alone cannot distinguish "saturated" from "as high as we dared go". **H2 next (tractability 3):** dose a CNP analogue in a large animal with a human-thickness plate (pig or sheep — rodent plates are too thin for diffusion limitation to be measurable) at three plasma exposures spanning ≥10-fold, and measure intra-plate concentration by MALDI imaging mass spectrometry on frozen sections, zone-resolved, with paired plasma PK. Saturating relationship ⇒ H2 live; linear ⇒ H2 excluded. **H1 (tractability 3):** dose across sub-saturating to saturating NPR2 occupancy (occupancy confirmed by binding or phospho-NPR2) and measure zone-resolved plate cGMP and phospho-VASP on the same sections. Plateau while occupancy still rises, lower in RZ than HZ ⇒ H1; tracking throughout ⇒ H1 excluded. Note H1 and H2 are indistinguishable from any plasma-side measurement, which is why every dose-selection decision in this field currently assumes H2 is false without testing it.

### q25  [species]
CLAIM: No — but "mice don't fuse" is too loose: mice never complete cartilage-to-bone replacement, yet they form hundreds of countable, genotype-tunable transphyseal bony bridges.
PROVENANCE: [ATLAS]
CONFIDENCE: C
SPECIES_BASIS: mouse (the claim), human (the contrast)
PATH: mouse_does_not_fuse; comparative_fusion_across_species (B); epiphyseal_fusion (A)
REFS: yu2025, samvelyan2022, staines2018, chu2026, haines1975
GAPS_CROSSED: g_l7fuse_001, g_l7fuse_004, g_l7fuse_011
OPERATION: Type 9 SPECIES — translation_risk + human_evidence + what the human data actually is.
ANSWER: At 55 weeks the mouse plate is still a discrete cartilaginous band: mineral content of the HZ has risen and the mineralised area expanded relative to 10 weeks, but it remains **calcified cartilage, not bone**, with aggrecan GAG still detectable. The machinery was switched off, not up — type X collagen and MMP-13 present at 10 weeks are absent at 55. What does happen: WT sham tibiae carry **~495 transphyseal bony bridges at density 1.2**, against **187 bridges at density 14.4 in Socs2−/−** — a ~12-fold density difference by genotype (samvelyan2022, micro-CT). Species sorting (comparative_fusion_across_species): complete fusion in human, dog, rabbit and goat; growth cessation without fusion in rat and mouse; site- and age-specific persistence in cynomolgus monkey. translation_risk = **high**, and the node states the risk runs in reverse: because the mouse cannot express the endpoint, every murine claim about fusion mechanism is an inference from a surrogate (plate height, bridge count, senescent decline), and that surrogate-to-endpoint step is untested.

### q26  [species]
CLAIM: Each arm of the PTHrP/IHH loop has a human monogenic phenotype, but the loop as a closed control system has never been characterised in human tissue.
PROVENANCE: [ATLAS]
CONFIDENCE: B
SPECIES_BASIS: mouse, chicken, human (genetics only)
PATH: pthrp_ihh_feedback_loop; human_evidence = **indirect**; translation_risk = **moderate**
REFS: vortkamp1996, lee1996, stjacques1999, karp2000, kobayashi2002, long2001, mak2008, koziel2004, lanske1996
GAPS_CROSSED: g_l3core_001; also g_l3core_005 (does PTHrP/PTH1R regulate CNP/NPR2 output or vice versa — open, tractability 4)
OPERATION: Type 9 SPECIES — translation_risk + human_evidence + what the human data actually is.
ANSWER: **What the human data actually is: four monogenic dose-effects, and nothing else.** PTHLH haploinsufficiency → brachydactyly type E; IHH mutations → brachydactyly A1 and acrocapitofemoral dysplasia; PTH1R gain of function → Jansen metaphyseal chondrodysplasia; PTH1R loss → Blomstrand chondrodysplasia. That establishes each *node* is required in humans. It does not establish the *loop*: topology, gain, range and the zonal PTHrP and IHH protein distributions are all unconfirmed in human growth plate (localization field: "human RZ/PHZ: zonal PTHrP and IHH protein distribution unconfirmed"). Loop wiring is inferred almost entirely from mouse and chick genetics — ISH for Pthlh periarticular, Ihh in PHZ, PTH1R highest in PZ/PHZ. translation_risk = moderate, and the node names the specific reason: **mice do not undergo epiphyseal fusion, so late-stage loop behaviour may differ** exactly where it matters most for human growth cessation. Layer warning: L3 is 21% direct-human and 11% replicated-human.

### q27  [species]
CLAIM: No. The 17.1% per 0.1 MPa coefficient comes from rat, rabbit and calf; no human physis has ever had a known stress applied and the resulting growth rate measured.
PROVENANCE: [ATLAS]
CONFIDENCE: C
SPECIES_BASIS: rat, rabbit, bovine
PATH: hueter_volkmann_law (human_evidence = **indirect**, translation_risk = **high**); audit row **x-L6-02** (X-grade: repeated in reviews, not traceable to human primary data)
REFS: stokes2006, stokes2002, stokes2007, villemure2009, roelen2026
GAPS_CROSSED: g_l6mech_001, g_l6mech_002 (tractability 5 — where the linear range saturates), g_l6mech_003, g_l6mech_006 (what strain rates a human physis actually experiences), g_l6mech_012
OPERATION: Type 9 SPECIES — translation_risk + human_evidence + what the human data actually is. No silent extrapolation.
ANSWER: What is measured: calibrated external loading across caudal vertebral and proximal tibial physes in rats, rabbits and calves for 8 days, growth read as fluorochrome label separation. Over roughly −0.2 to +0.1 MPa the relation was apparently linear at **17.1% per 0.1 MPa** averaged across plates (range 9.2–23.9; 15.0 for vertebrae, 18.6 for proximal tibia), despite baseline rates spanning 30 µm/day (rat vertebra) to 366 µm/day (rabbit proximal tibia). The response is asymmetric: compression suppresses more than equal tension accelerates (52% vs 113% of control). What the *human* data is: **entirely inferential** — guided growth, epiphysiodesis, vertebral body tethering, and the progression of Blount disease and scoliosis all behave as the law predicts, but no human study has applied a known stress and measured growth, and the in vivo human physeal stress is itself unmeasured. This is a single-programme value (Stokes/Aronsson) and the atlas holds x-L6-02 flagging that the coefficient is applied to human patients in orthopaedic reviews and FE models without a human primary source.

### q28  [species]
CLAIM: No — human physeal oxygen tension has never been measured by any method, and this is a documented `search_established` null.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (established gap); the hypoxia claim itself is held at audit row x-L1-01
SPECIES_BASIS: rat, rabbit (1971 microelectrode work); mouse (genetic inference)
PATH: gap g_l3rest_011 (search_established, tractability 2); node oxygen_gradient_growth_plate (L1, C); audit row **x-L1-01**
REFS: brighton1971, schipani2001, schipani2015, zhang2023_2
GAPS_CROSSED: g_l3rest_011
OPERATION: Type 9 SPECIES — human_evidence + what the human data actually is; gap returned with search log (§7.1).
ANSWER: **Search log, reproducible:** Europe PMC, 2026-08-05, `TITLE:("growth plate" OR physis OR "epiphyseal plate") AND ("oxygen tension" OR pO2 OR oximetry)` → 21 records; and `("growth plate" OR physis OR "epiphyseal plate") AND human AND ("oxygen tension" OR "pO2" OR "oxygen partial pressure" OR "oxygen microelectrode")` → 452 records. The only direct-measurement papers are the two 1971 Brighton & Heppenstall studies in **rat and rabbit**, plus a 1991 study of oxygen tension effects on proteoglycan synthesis in cultured cells. **No record reports human physeal oximetry**, and no modern method (fibre-optic probe, EPR oximetry, phosphorescence quenching, BOLD MRI) has been applied to a human growth plate. Two reasons this matters beyond the missing number: a human adolescent plate is far thicker than a mouse plate, so the diffusion distance that generates the gradient is not comparable and the human gradient could be steeper; and chondrocytes buffer their own oxygenation via KLF1-dependent, HIF-independent haemoglobin condensates (zhang2023_2), so tissue oxygen cannot be predicted from geometry. The atlas holds "the growth plate is hypoxic with a metaphysis-to-centre gradient" as an **X-grade** claim (x-L1-01) — ubiquitous in reviews, traceable only to 1971 rodent data.

### q29  [species]
CLAIM: Not known in humans — it is settled in mice at ~60–63% of trabecular and endosteal osteoblasts, and the human fraction has never been measured because the method cannot be applied to humans.
PROVENANCE: [ATLAS]
CONFIDENCE: C
SPECIES_BASIS: mouse (only)
PATH: chondrocyte_to_osteoblast_transdifferentiation (human_evidence = **absent**, translation_risk = **high**)
REFS: zhou2014a, yang2014, shu2021, mizuhashi2018
GAPS_CROSSED: g_l2stem_002 (quantitative_gap: what fraction of human trabecular and endosteal osteoblasts is chondrocyte-derived, and over what age range)
OPERATION: Type 9 SPECIES — translation_risk + human_evidence + what the human data actually is.
ANSWER: In mice it is settled by two independent Cre systems (Col10a1-Cre constitutive; Agc1-CreERT2 inducible), neither labelling perichondrium, periosteum or any osteoblast-lineage cell at induction: ~63% of trabecular and ~62% of endosteal osteocalcin+ cells at one month, ~60%/68% of Col1-GFP+ osteoblasts at three weeks; the cells persist as embedded osteocytes into adulthood. Dual-recombinase mapping adds the boundary — chondrocytes are the main osteoblast source only *before* adolescence, after which LepR+ stroma takes over starting in the diaphysis. The residual controversy is technical (Cre-driver specificity; the authors themselves flag 60% could be an overestimate from ectopic Col10a1-Cre activity). **In humans: no measurement of any kind exists.** translation_risk = high for two reasons — the measurement requires irreversible genetic labelling of a transient cell state, which cannot be done in humans; and the developmental boundary itself has no human analogue because human plates fuse and mouse plates do not.

### q30  [species]
CLAIM: No — there is no PIEZO1 or PIEZO2 protein or transcript report in human physeal tissue of any kind, and the null is search-established.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (established gap, tractability 4)
SPECIES_BASIS: mouse (all functional evidence); human only in osteoarthritic osteophytes
PATH: gap g_l6mech_007 (search_established); related g_l6mech_008, g_l6mech_009
REFS: brylka2024, chen2025a, chen2025, tschaffonmller2026
GAPS_CROSSED: g_l6mech_007
OPERATION: Type 9 SPECIES — human_evidence + what the human data actually is; gap returned with search log.
ANSWER: **Search log:** Europe PMC, 2026-08-05, `(PIEZO1 OR PIEZO2) AND human AND ("growth plate" OR physis OR "epiphyseal plate") AND (immunohistochemistry OR RNAscope OR "in situ hybridization" OR "single-cell"…)` → 196 records; none reports PIEZO1/2 in human physeal tissue resolved by zone. What exists is all mouse: chondrocyte-specific Piezo1 deletion abolishes trabecular bone under the plate and causes peri-physeal rib fractures while Piezo2 deletion does nothing comparable; hypertrophic-chondrocyte Piezo1 deletion raises osteoclast number in the primary spongiosa; compression upregulates PIEZO1 in mouse vertebral growth plate chondrocytes, deletion slows scoliosis, and PIEZO1 colocalises with the primary cilium there. **The only human cartilage PIEZO1 protein data are from osteophytes in osteoarthritis** — not growth plate. This matters because PIEZO1 is being pursued as a scoliosis drug target on the strength of the mouse work; the gap is tractability 4, answerable with existing archival tissue.

### q31  [entity]
CLAIM: ANKH exports ATP, not pyrophosphate — ENPP1 then makes PPi extracellularly.
PROVENANCE: [ATLAS]
CONFIDENCE: B
SPECIES_BASIS: mouse, rat, in_vitro_human_cell, human (genetics)
PATH: ankh_transporter (node read); parameters.superseded_rows holds the retired "~75% of bone PPi attributable to Ank" row flagged `superseded_model: true`; audit row **c_l5matrix_01**; QUERY.md §6 correction CORR-001
REFS: szeri2022, wang2005, harmey2004, zaka2009
GAPS_CROSSED: g_l5matrix_006 (open contradiction gap)
OPERATION: Type 1 ENTITY — node read + claim_grades (null on this node; node grade B used) + explicit check against the §6 correction table.
ANSWER: In HEK293 cells engineered to lack ENPP1 entirely, introducing ANKH produces robust ATP release with **no** increase in extracellular PPi, and Enpp1−/− mouse bone contains **under 2.5%** of wild-type PPi despite intact *Ank*. ANKH therefore exports nucleoside triphosphates, predominantly ATP; ABCC6 does the same. ANKH supplies ~25% of plasma PPi, ABCC6 60–70%. Consequence for the growth plate: the older chondrocyte literature (blocking Ank raises PPi and blocks mineralization; overexpressing Ank lowers PPi and induces ALP, collagen I, osteocalcin and mineralization) was interpreted as direct PPi transport and **must be reread as ATP export plus local ENPP1 activity**. My training data contains the superseded PPi-transporter version; the atlas holds the corrected one and the atlas wins. Human evidence is genetic only (ANKH gain of function → craniometaphyseal dysplasia and chondrocalcinosis); ANKH zonal protein localisation in human growth plate is unconfirmed.

### q32  [entity]
CLAIM: The measured predictive SD of corrected mid-parental target height is 4.4–5.1 cm; the familiar ±8.5 cm band was never measured.
PROVENANCE: [ATLAS]
CONFIDENCE: B (node); per-claim grades A / B / C as below
SPECIES_BASIS: human (only)
PATH: target_height_predictive_sd (node read + claim_grades); parameters.by_node['target_height_predictive_sd']
REFS: zeevi2024, luo1998, wright1999, tanner1970
GAPS_CROSSED: g_l9organism_004, g_l9organism_005
OPERATION: Type 1 ENTITY — node read + **claim_grades** (this node has them, unlike q01/q02).
ANSWER: claim_grades: "empirical predictive SD is 4.4–4.7 cm" = **B** (one direct measurement, 23 large Israeli/US Jewish families, n=303 adult children; internally replicated within and across families, not replicated in a second population); "the ±8.5 cm band was a theoretical derivation, not a measurement" = **A** (documented against tanner1970 via zeevi2024); "guideline ±1.64 SDS bands are ~50% wider than the measured SD justifies" = **C** (arithmetic against a single empirical estimate). Numbers: residual SD 4.7 cm sons / 4.4 cm daughters pooled; 4.5 ± 0.9 and 4.2 ± 0.8 within families; luo1998 gives a 95% PI of ±10 cm in 2402 Swedes ⇒ SD ≈ 5.1 cm. The three bands in circulation (±8.5, ±9/±10, ±1.64 SDS = ±10.6/±11.7 cm) imply SDs of ~4.5, 4.8–5.3 and 6.5–7.1 cm for the same quantity. ±8.5 cm is best read as a theoretically derived ~1.9 SD band, not the 2 SD band it is usually assumed to be. Residual dispersion is not larger for taller parents (r=0.38, p=0.08), so one SD can be used across the range.

### q33  [negative]
CLAIM: Unknown — no PDE isoform has ever been localised to a growth plate zone in human tissue by any method.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (search_established gap, tractability 3)
SPECIES_BASIS: human/mouse/chicken bulk transcript only; functional assignment is rat vs mouse and they disagree
PATH: gap g_l3core_006; nodes pde_isoform_inventory, pde1c, pde3a, pde3b, pde5a, pde9a
REFS: ursachi2026 (indexing takcs2023, kawabe2025), wang2018, grogan2013
GAPS_CROSSED: g_l3core_006; also g_l13data_001 — this gap is one of the several that a human spatial transcriptome would close at once
OPERATION: Type 6 NEGATIVE — gaps.json filtered, **with search logs attached**.
ANSWER: **Search logs (Europe PMC, all 2026-08-05):** `TITLE_ABS:"phosphodiesterase" AND TITLE_ABS:"growth plate"` → 14; `(PDE3A OR PDE3B OR PDE5A OR PDE9A OR PDE1C) AND ("growth plate" OR physis …)` → 2; `(phosphodiesterase OR PDE3B OR PDE5A OR PDE9A) AND ("growth plate" OR physis) AND human AND (immunohistochemistry OR in situ hybridisation …)` → 201; `PDE9A AND (cartilage OR chondrocyte OR bone OR skeletal)` → 234; `PDE1C AND (cartilage OR chondrocyte OR "growth plate")` → 59. What is known: bulk profiling across human, mouse and chicken reports PDE1B, 3B, 4B, 4D, 5A, 7A, 8A, 10A, with PDE6/9/11 family genes reported absent from skeletal tissue. Functional assignment is **species-split**: PDE5 dominates cGMP hydrolysis in newborn rat epiphyseal chondrocytes, PDE3B is the functional target in mouse. The only zone-resolved cartilage PDE data are from human and bovine **articular** cartilage (PDE3B superficial, PDE7A deep). What is missing: any zonal localisation in human growth plate by IHC, ISH, laser-capture or spatial transcriptomics, and any human growth plate PDE enzymatic activity assay. PDE9A and PDE1C have no primary growth plate literature in any species.

### q34  [negative]
CLAIM: Unknown — this is open gap g_l8gwas_001, in the atlas's least-swept layer.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (quantitative_gap, tractability 4)
SPECIES_BASIS: human
PATH: gap g_l8gwas_001; node height_gwas (B)
REFS: yengo2022
GAPS_CROSSED: g_l8gwas_001; also g_l8gwas_002 (do growth-plate eQTLs have measurable in situ expression effects)
OPERATION: Type 6 NEGATIVE — gap returned; layer coverage warning attached.
ANSWER: **Layer warning: L8 has 3 nodes and has not been swept. Its low gap count means "not yet examined", not "few unknowns."** What is known: 12,111 conditionally independent genome-wide-significant SNPs from 5.4 million individuals, clustering into 7,209 non-overlapping segments of mean ~90 kb covering ~21% of the genome, explaining 40% of phenotypic variance in European-ancestry and only 10–20% in other ancestries; association density is elevated near genes with skeletal growth function. What is not known and is the gap as asked: what fraction of those SNPs act **through the growth plate chondrocyte** as opposed to through muscle, endocrine or other tissues. The atlas does not contain a number and I will not supply one. Note the node also carries an internal contradiction (c001): the Nature version says segments have a **mean** ~90 kb, the preprint of the same analysis says **median** ~90 kb, which cannot both be true of a right-skewed distribution.

### q35  [negative]
CLAIM: Unknown — no CNP analogue has a published growth-plate tissue concentration in any species, and the atlas records the audited count as 0 of 12 compounds.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (quantitative_gap g_l12pharm_002, tractability 3; and method_blocked g_mr002_h2)
SPECIES_BASIS: none — the measurement does not exist in any species
PATH: gaps g_l12pharm_002, g_mr002_h2; audit row **x-L12-03** ("the growth plate drug concentrations achieved by systemic therapy are adequate" — the unstated premise of every dose selection in growth pharmacology, X-grade)
REFS: savarirayan2023, galetaki2026
GAPS_CROSSED: g_l12pharm_002, g_mr002_h2
OPERATION: Type 6 NEGATIVE — gap returned with search log.
ANSWER: **Search log:** Europe PMC, 2026-08-05, `vosoritide AND achondroplasia AND (randomi* OR "growth velocity")` → 134 records; plasma PK is well characterised for vosoritide and navepegritide and weight-band dosing is derived by population PK modelling, but **no compound in the audited set has a published growth plate tissue concentration in any species**. What is missing specifically: a measured concentration-versus-depth profile across the zones of a plate, for any CNP analogue, in any species — and therefore no empirical basis for whether effective tissue exposure follows plasma exposure or is diffusion-limited and flattened by the avascular, proteoglycan-dense matrix. This is not a footnote: it is competing hypothesis **H2** for why vosoritide exposure predicts urine cGMP but not growth (QUERY.md §6). The reason it is `method_blocked` rather than merely unmeasured is that rodent plates are too thin for diffusion limitation to be resolvable, so the experiment requires a large animal.

### q36  [negative]
CLAIM: Unknown in humans — 213 records screened, none a primary human measurement of resting-zone proliferative or clonal capacity.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (search_established gap, tractability 3)
SPECIES_BASIS: rabbit and mouse only
PATH: gap g_l2stem_005; related g_l2stem_007, g_l2stem_008; audit row **x001**
REFS: schrier2006, baron1994, gafni2001, marino2008, nilsson2005, newton2019
GAPS_CROSSED: g_l2stem_005
OPERATION: Type 6 NEGATIVE — gap returned with search log; L2 layer warning attached.
ANSWER: **Layer warning: L2 is 0% replicated-human.** **Search log:** Europe PMC, 2026-08-05, `(human) AND ("growth plate" OR physis) AND ("resting zone" OR "reserve zone") AND (clonal OR "self-renewal" OR "proliferative capacity" OR "replicative capacity"…)` → 213 records, **none** a primary human measurement. What is known, all animal: rabbit RZ chondrocytes fall in proliferation rate and number with age, and the decline is **division-dependent rather than age-dependent**; it is **not** a cell-autonomous Hayflick limit, since cultured rabbit RZ population doublings are independent of donor age; and mouse clonal tracing found progenitors *acquiring* self-renewal postnatally rather than only spending down a budget. So even in animals the "finite capacity" model is contested in its mechanism. Relatedly the atlas holds **x001** as an X-grade claim: "growth plate chondrocytes exhaust a finite proliferative capacity through telomere attrition" is routinely asserted in review literature but not traceable to primary data, and whether telomeres shorten in human plate chondrocytes is itself an open gap (g_l2stem_007).

### q37  [negative]
CLAIM: Unknown in every species — no zone-resolved HOX localisation exists in any growth plate, and no HOX measurement exists in human growth plate tissue at all.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (search_established gap, **tractability 5**)
SPECIES_BASIS: mouse (bulk zonal RNA-seq and function); human absent
PATH: gap g_l0dev_004; nodes hox_code_limb (D), hoxa11_gene, hoxd11_gene; edge e00580 (hoxd11_gene required_for growth_velocity_longitudinal, C)
REFS: lui2018, pineault2015, rux2021
GAPS_CROSSED: g_l0dev_004; g_l0dev_001 (scale_gap: does positional HOX identity causally set site-specific elongation rate)
OPERATION: Type 6 NEGATIVE — gap returned with search log.
ANSWER: **Search log:** Europe PMC, 2026-08-05, `(Hox OR Hoxa11 OR Hoxd11 OR Hoxa13 OR Hoxd13) AND ("growth plate") AND (chondrocyte) AND ("resting zone" OR "proliferative zone" OR "hypertrophic zone" OR zonal…)` → 90 records; top 20 by relevance screened; **none reports zonal HOX localisation in a growth plate**. The two closest are rux2021 (articular, not growth plate cartilage) and lui2018. What is known: bulk laser-capture RNA-seq of separated proliferative and hypertrophic zones detects Hoxd13, Shox and Tbx5 differences between phalangeal and tibial plates in rodent, so positional transcripts are present at bulk-zone level; and Hoxa11/Hoxd11 function is required postnatally for zeugopod elongation (mouse: compound mutants show falling elongation rate, falling plate height, premature senescent involution, and *paradoxically elevated* RZ/PZ proliferation — the signature of accelerated progenitor consumption). What is missing: any ISH, IHC or single-cell dataset resolving HOX by zone, in any species; and any human measurement. Tractability 5 — this is one of the cheapest high-value gaps in the atlas.

### q38  [negative]
CLAIM: The atlas does not contain the childhood (age 3–9) population SD of height velocity — not as a value, and not as a logged gap.
PROVENANCE: [COVERAGE-GAP]
CONFIDENCE: n/a
SPECIES_BASIS: n/a
PATH: searched growth_velocity_curve, peak_height_velocity, growth_velocity_measurement_interval, seasonality_growth_velocity, who_growth_standard, icp_growth_model; parameters.by_node search on "height velocity"; gaps search on "height velocity" and "velocity reference"
REFS: n/a — the value is absent
GAPS_CROSSED: no existing gap covers it. Nearest gaps are g_l9organism_002 (residual SDs of competing growth *models*) and g_l9organism_007 (proportion of infants crossing two centiles) — neither is this quantity.
OPERATION: Type 6 NEGATIVE — attempted gaps.json filter, found no covering gap, therefore §7.2: log a coverage gap and state the atlas does not cover it.
ANSWER: What the atlas *does* have, and it is adjacent but not the answer: peak height velocity 9.5–9.6 cm/yr (boys) and 8.3–8.4 (girls) graded A; SD of *age* at PHV = 0.8 y in ALSPAC females; SITAR tempo SD 0.97 y and velocity SD 15% in Christ's Hospital; mean annual velocity 6.10 cm/yr in 760 Danish 8–11 year olds; and berkey1993 US velocity centiles ages 7–18 from 6,532 children stratified by maturational tempo. None of these is a population SD of height velocity in the 3–9 y childhood plateau. I am not supplying one from memory — a between-individual SD is a quantitative claim and [MODEL] is never permitted for those. Logged in coverage_gaps.yaml against layer L9.

### q39  [negative]
CLAIM: Unknown — no G380R-specific infigratinib IC50 has been published with stated assay conditions, despite a completed phase 3 trial against that allele.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (quantitative_gap g_l12b_005, **tractability 5**; plus search_established g_mr002_allele, tractability 4)
SPECIES_BASIS: in_vitro (recombinant kinase panels)
PATH: gaps g_l12b_005, g_mr002_allele, g_l12b_004; nodes infigratinib_growth, fgfr3_tyrosine_kinase_inhibitor
REFS: ryu2022, chembl_infigratinib, guagnano2011, tavormina1999
GAPS_CROSSED: g_l12b_005
OPERATION: Type 6 NEGATIVE — gap returned with the adjacent values that do exist.
ANSWER: What exists: a ChEMBL-curated microfluidic mobility-shift value of **1.0 nM against FGFR3 at ATP = Km**, and a radiometric panel giving **0.66 nM wild-type, 0.5 nM K650E, 44.4 nM K650M, 505.9 nM V555M** — without stated ATP concentration. What is missing: any published IC50 against **G380R**, the allele the drug is licensed-track to treat, with ATP concentration, substrate and readout stated; and any free (unbound) paediatric plasma concentration at the 0.25 mg/kg/day clinical dose to compare it against. Why the gap is load-bearing rather than pedantic: the allele-dependence spans ~1,000-fold, so extrapolating from wild-type is unsafe; and K650M has ~3× the constitutive kinase activity of K650E yet is 89-fold less well inhibited, so potency and severity are decoupled in this series (see q21). Without the number there is no way to relate dose to target engagement, no therapeutic-index estimate against the off-target FGFR1/2 activity that reduced trabecular bone in mice, and no basis for predicting other alleles.

### q40  [negative]
CLAIM: No — a GEO census returned zero human growth plate spatial records, and this single absence is the reason several other atlas gaps exist.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (search_established gap, tractability 3)
SPECIES_BASIS: n/a
PATH: gap g_l13data_001; node human_growth_plate_tissue_scarcity (A)
REFS: geo_census_20260805, gse267139, gse288028
GAPS_CROSSED: g_l13data_001
OPERATION: Type 6 NEGATIVE — gap returned with search log.
ANSWER: **Search log:** NCBI GEO DataSets via E-utilities esearch (db=gds), 2026-08-05, `(growth plate[All Fields]) AND (spatial[All Fields]) AND Homo sapiens[Organism]` → **0 records**. The census found 7 records matching growth plate AND spatial, all non-human and mouse-dominated (e.g. GSE288529 ApoE as a resting-zone marker; GSE275252 ADGRG6). Human growth plate **single-cell** data does exist — 18 records, including GSE267139 (human cartilage development) and GSE288028 (GH action in the human pubertal growth plate) — so human tissue is not wholly unobtainable; it is the spatially resolved modality specifically that is absent. Consequence the atlas draws explicitly: the human zonal PDE inventory, zonal receptor expression, zonal HOX, zonal mTORC1 and the oxygen-responsive transcriptional gradient are **not independent unknowns but one missing measurement expressed several times**. The binding constraint is tissue access and RNA degradation in decalcified bone, not platform availability.

### q41  [negative]
CLAIM: Unknown — no published report of achieved final or near-adult height in any CNP-analogue-treated cohort exists, and this is the atlas's flagged surrogate-endpoint problem.
PROVENANCE: [ATLAS]
CONFIDENCE: n/a (search_established gap g_l12pharm_001, tractability 4); the velocity effect it is contrasted with is A
SPECIES_BASIS: human
PATH: gap g_l12pharm_001; node vosoritide (A); node trial_endpoint_annualized_growth_velocity
REFS: savarirayan2020, kamrulhasan2026, alfaraj2026
GAPS_CROSSED: g_l12pharm_001
OPERATION: Type 6 NEGATIVE — gap returned with search log.
ANSWER: **Search log:** Europe PMC, 2026-08-05, `vosoritide AND ("final adult height" OR "final height" OR "adult height" OR "near-adult height")` → 64 hits, 20 screened, **none** reporting achieved final or near-adult height. The two most likely candidates were screened and excluded at abstract level: PMID 42306228 (meta-analysis, 11 studies, N=542, 4 RCTs n=326) reports AGV 1.36 cm/yr (95% CI 1.05–1.68), height Z-score, standing height and U/L ratio — no final height; PMID 40821249 (review to May 2025) discusses "long-term potential" prospectively. Absence is consistent with trial design, not reporting failure. The specific risk the atlas names: velocity and adult height dissociate whenever an intervention also advances skeletal maturation, and **no published analysis exists of whether treatment alters the bone-age-to-chronological-age ratio**. Open-label extensions NCT03424018 and NCT03989947 are the designed route to the answer. This is also the cleanest available human test of whether total plate elongation capacity is fixed or extensible.

### q42  [negative]
CLAIM: Two.
PROVENANCE: [ATLAS]
CONFIDENCE: A
SPECIES_BASIS: human
PATH: human_growth_plate_tissue_scarcity (node + claim_grades + parameters.by_node); epiphyseal_fusion; hypoxia_necrosis_at_fusion
REFS: human_gp_donor_census_20260805, white2008, emons2009, rodriguez1992, nilsson2003, werther1990, strangevognsen1997, geo_census_20260805
GAPS_CROSSED: none — this is a completed census, not a gap
OPERATION: Type 6 NEGATIVE — the negative-space census returned directly, with its provenance.
ANSWER: **2 human growth plates have been examined histologically at or immediately before fusion**: white2008 (distal tibia, n=1) and emons2009 (one late-pubertal plate "about to fuse", collected with a series of unfused plates). Context from the same census (2026-08-05, 30 located studies, 21 stating donor counts): **259 distinct human donors** total, of which **157 are fetal or perinatal autopsy** (125 from a single 1992 series of 46 stillborns and 79 newborns, 20 SIDS sternochondral, 12 fetal-to-13-month) and only **102 contributed a postnatal, still-growing plate** — every one of them surgical waste (epiphysiodesis, polydactyly resection, amputation for osteosarcoma or trauma, transplant salvage). The largest postnatal series is 24 proximal tibial biopsies across Tanner 1–5, never deposited in any repository. claim_grades: "at most ~100 postnatal growing human plates examined" = **A**; "the true number is lower because of cohort overlap" = **E**; "essentially all postnatal tissue is surgical waste" = **A**. Two consequences: "the normal human growth plate" is a composite of children having surgery, so normality is assumed rather than demonstrated; and the fusing-plate literature rests on n=1 with no TUNEL-positive cells and EM signs of hypoxia and necrosis rather than apoptosis.

---
## Adversarial set

### a01  [adversarial]
CLAIM: The atlas does not cover leptin's role in bone marrow adipocyte differentiation.
PROVENANCE: [COVERAGE-GAP]
CONFIDENCE: n/a
SPECIES_BASIS: n/a
PATH: alias 'leptin' → leptin_hormone (L4, B), leptin_receptor, lepr_positive_stromal_cell (L2). Nodes read; none addresses adipocyte differentiation as an outcome.
REFS: n/a
GAPS_CROSSED: none exists
OPERATION: Alias resolution → node read → §7.2 (no covering gap, log a coverage gap).
ANSWER: The atlas holds leptin as the permissive energy-sufficiency signal for the reproductive and growth axes (LEP/LEPR/MC4R deficiency cohort, hypogonadotropic hypogonadism, recombinant leptin restoring puberty) and a reported rodent-only local action stimulating aromatase in the plate. It separately holds LepR+ stromal cells as the highest-purity marrow stroma marker in mouse, noting they "form bone, cartilage and adipocytes in culture and on transplantation." **What it does not contain is any account of leptin signalling driving bone marrow adipocyte differentiation** — the LepR+ node is about lineage output of a marker-defined cell, not about leptin as an instructive adipogenic signal. Out of the atlas's declared scope (human longitudinal skeletal growth). Logged.

### a02  [adversarial]
CLAIM: The atlas contains nothing on SARS-CoV-2 or on infection-related growth disruption of that kind.
PROVENANCE: [COVERAGE-GAP]
CONFIDENCE: n/a
SPECIES_BASIS: n/a
PATH: alias lookups 'sars', 'covid' → **no entries**; full-text scan of graph.json nodes → no match
REFS: n/a
GAPS_CROSSED: none exists
OPERATION: Alias resolution returned nothing → §7.1 (no covering gap in gaps.json) → §7.2.
ANSWER: No node, no edge, no gap. I decline to answer from general knowledge: childhood growth effects of an infection are a quantitative and mechanistic claim, and [MODEL] is not permitted for those. The nearest thing the atlas holds is L10/L11 systemic-illness growth suppression as a class (g_l11path_022 weighs inflammation, glucocorticoid exposure, undernutrition and acquired GH resistance in paediatric systemic disease) — but that is a general frame, not a SARS-CoV-2 finding, and I will not present it as one. Logged.

### a03  [adversarial]
CLAIM: The atlas covers sclerostin biology and names romosozumab, but contains nothing on its mechanism or efficacy in osteoporosis.
PROVENANCE: [ATLAS] for the boundary statement; [COVERAGE-GAP] for the question as asked
CONFIDENCE: B (sclerostin_sost node)
SPECIES_BASIS: human
PATH: alias 'romosozumab' → no direct node; the string occurs only inside sclerostin_sost (L3, B, human)
REFS: balemans2001, poole2005
GAPS_CROSSED: none exists for the osteoporosis question
OPERATION: Alias resolution → node read → declared boundary applied.
ANSWER: What the atlas says, verbatim in substance: sclerostin is a secreted WNT antagonist binding LRP5/6; human SOST-null sclerosteosis produces bone overgrowth **including tall stature**, one of very few human WNT phenotypes with increased linear growth; in normal human bone sclerostin is a delayed osteocyte product, absent from early osteoblasts, so it is a late spatially restricted brake; and whether it reaches the growth plate chondrocyte at all is unresolved, since SOST expression in growth plate cartilage has not been demonstrated. On romosozumab the atlas says exactly one thing: **it is licensed in adults only, so no paediatric physeal readout exists.** Adult osteoporosis efficacy and mechanism are outside the atlas (coverage.md lists adult bone density as out of scope). I decline to supply them. Logged.

### a04  [adversarial]
CLAIM: Out of scope — the atlas holds WNT only as growth plate chondrocyte signalling and contains nothing oncological.
PROVENANCE: [COVERAGE-GAP]
CONFIDENCE: n/a
SPECIES_BASIS: n/a
PATH: alias 'wnt' → wnt_canonical_chondrocyte, wnt5a_ligand, wnt_noncanonical_pcp, beta_catenin_ctnnb1, sclerostin_sost, dkk1; alias 'colorectal' → **no entries**
REFS: n/a
GAPS_CROSSED: none exists
OPERATION: Alias resolution → scope boundary.
ANSWER: The atlas's WNT content is growth-plate-specific: canonical WNT/β-catenin in chondrocytes, the bistable β-catenin↔SOX9 loop, non-canonical PCP, and open gaps on what sets zonal β-catenin levels (g_l3rest_005), the β-catenin dose–response for chondrocyte fate (g_l3rest_006), and whether SOST/DKK1 are present in growth plate cartilage at all (g_l3rest_007). **There is no colorectal cancer content, no APC, no oncology of any kind.** I know the colorectal WNT story; it does not go in an [ATLAS] answer and the atlas is not the right source for it. Logged.

### a05  [adversarial]
CLAIM: The atlas covers dietary protein's route to the growth plate but contains no intake recommendation and no athlete data.
PROVENANCE: [ATLAS] for what is covered; [COVERAGE-GAP] for the question as asked
CONFIDENCE: B (protein_intake_growth)
SPECIES_BASIS: human
PATH: alias 'protein intake' → protein_intake_growth (L10, B, human); alias 'athlete' → no node (nearest: gymnastics_stature_effect, leptin_hormone)
REFS: hoppe2004
GAPS_CROSSED: g_l10env_002 (does a protein/amino-acid manipulation that changes circulating IGF-1 also change chondrocyte mTORC1)
OPERATION: Alias resolution → node read → the asked-for quantity is absent → §7.2.
ANSWER: What the atlas has: in 24 healthy 8-year-old boys randomised to 1.5 L skimmed milk or isonitrogenous lean meat for 7 days, protein intake rose 61% and 54% respectively, yet serum IGF-I rose 19% (P=0.001) and the IGF-I/IGFBP-3 ratio 13% (P<0.0001) **only in the milk arm** — so protein *quantity* is not the operative variable, protein *source* is. A 2×2 factorial in 57 boys separated the fractions: casein raised IGF-1 15% with no insulin change; whey raised fasting insulin 21% with no IGF-1 change. **There is no optimal-intake figure anywhere in the atlas, and no athlete cohort.** The nearest athletic content is gymnastics_stature_effect, which is about training load and an unresolved selection-versus-causation contradiction (c-L6-02), not nutrition. I decline to give a g/kg/day number. Logged.

### a06  [adversarial]
CLAIM: The atlas cannot answer this — its comparative fusion node covers seven mammalian species and no bird, and its only avian content is embryonic limb patterning.
PROVENANCE: [ATLAS] for the boundary; [COVERAGE-GAP] for the comparison asked
CONFIDENCE: B (comparative_fusion_across_species)
SPECIES_BASIS: human, dog, rabbit, goat, rat, mouse, cynomolgus monkey — **no avian**
PATH: comparative_fusion_across_species (L7, B); chick appears only in apical_ectodermal_ridge, limb_bud_initiation, progress_zone, zone_of_polarizing_activity (all L0 embryonic) and as a species in the PTHrP/IHH loop
REFS: haines1975, weise2001, panebianco2026, roach2003, yu2025, samvelyan2022
GAPS_CROSSED: g_l0dev_002 (is there any developmental antecedent distinguishing species that fuse from species that do not)
OPERATION: Alias/species scan → node read → scope boundary.
ANSWER: The atlas sorts species into three groups by terminal plate fate — (1) complete fusion: human, dog, rabbit, goat; (2) growth cessation without fusion: rat, mouse; (3) site- and age-specific persistence: cynomolgus monkey — and calls this sorting "the single most load-bearing fact in this atlas." **Birds are not in it.** Chick appears only as an embryonic limb-patterning model (AER, ZPA, progress zone) and as a species contributing to the PTHrP/IHH loop; there is no avian growth plate architecture, kinetics or fusion content. So the atlas can tell you where mammals sit and cannot tell you how birds differ. Logged.

### a07  [adversarial]
CLAIM: Entirely out of scope — the atlas's heritability content is height only.
PROVENANCE: [COVERAGE-GAP]
CONFIDENCE: n/a
SPECIES_BASIS: n/a
PATH: alias 'intelligence' → **no entries**; L8 contains height_gwas, missing_heritability_height and one further node (3 nodes total, unswept)
REFS: n/a
GAPS_CROSSED: none exists
OPERATION: Alias resolution returned nothing → §7.2.
ANSWER: No node, no edge, no gap, no reference. The atlas is a map of human longitudinal skeletal growth; cognitive genetics is not adjacent to it in any way, and the fact that both traits are polygenic is not a reason to answer from a height atlas. I decline. Logged for completeness only — this is a scope boundary rather than a sweep target, and I would not put it in the next sweep's queue.

### a08  [adversarial]
CLAIM: The atlas holds the HOX limb code but not vertebral column patterning.
PROVENANCE: [ATLAS] for what is covered; [COVERAGE-GAP] for the question as asked
CONFIDENCE: D (hox_code_limb)
SPECIES_BASIS: mouse, human
PATH: hox_code_limb (L0, **D**), hoxa11_gene, hoxa13_gene, hoxd11_gene; edge e00580 (hoxd11_gene required_for growth_velocity_longitudinal, C)
REFS: pineault2015, lui2018
GAPS_CROSSED: g_l0dev_004 (tractability 5 — zonal HOX in any growth plate), g_l0dev_001, g_l0dev_010 (does germ-layer origin — somitic sclerotome for vertebral plates vs lateral plate for limb — matter)
OPERATION: Alias resolution → node read → the asked-for domain is absent.
ANSWER: What the atlas has is **proximodistal limb** identity: posterior HOX paralogue groups 9–13, Hox9/10 → stylopod, Hox11 → zeugopod, Hox13 → autopod, graded **D** — the lowest-graded node I have cited in this run. Its atlas relevance is narrow and explicitly stated: the identity is not discarded at birth, and Hoxa11/Hoxd11 compound mutants show falling elongation rate and premature senescent involution with *elevated* proliferation, the signature of accelerated progenitor consumption. **Vertebral column HOX patterning is not in the atlas.** The nearest thing is g_l0dev_010, an open gap asking whether the somitic-sclerotome origin of vertebral plates versus lateral-plate origin of limb plates has any consequence — which presupposes the vertebral patterning question rather than answering it. Logged.

### a09  [adversarial]
CLAIM: Out of scope — coverage.md names articular cartilage explicitly as outside the atlas, and the atlas has no osteoarthritis aetiology content.
PROVENANCE: [ATLAS] for the boundary; [COVERAGE-GAP] for the question
CONFIDENCE: B (articular_cartilage node, which is about growth not disease)
SPECIES_BASIS: human, mouse
PATH: alias 'articular' → articular_cartilage (L9, B); alias 'osteoarthritis' → **no entries**; the string appears only incidentally in gdf5_gene, multiple_epiphyseal_dysplasia, pseudoachondroplasia, telomere_attrition_chondrocyte, endocrine_disrupting_chemicals
REFS: yuan2015
GAPS_CROSSED: none exists
OPERATION: Alias resolution → scope boundary from coverage.md ("Articular cartilage, oncology, veterinary, adult bone density, forensic applications and surgical management are all out of scope").
ANSWER: The atlas's only articular cartilage node exists as the growth plate's *opposite number*: in 240 knee MRIs of children 7–18 without chondral pathology, femoral articular cartilage was thicker with open distal femoral physes than with closing/closed physes at medial condyle, lateral condyle and lateral trochlea (all p<0.001), while patellar cartilage was thickest overall and did not vary with maturity. It is retained only because it supplies an organism-level dissociation the mechanistic layers must reproduce (the same ciliary perturbation that shortens the mouse plate thickens articular cartilage). **Nothing about osteoarthritis causation is in the atlas.** I know the field; it is not atlas content and I will not present it as such. Logged as scope boundary, not sweep target.

### a10  [adversarial]
CLAIM: The atlas contains no equine data of any kind.
PROVENANCE: [COVERAGE-GAP]
CONFIDENCE: n/a
SPECIES_BASIS: n/a
PATH: alias 'horse'/'equine' → **no entries**; full-text scan of graph.json → no equine node, no equine species_basis, no equine reference. comparative_fusion_across_species species list: human, dog, rabbit, goat, rat, mouse, cynomolgus monkey.
REFS: n/a
GAPS_CROSSED: none exists
OPERATION: Alias resolution returned nothing; comparative species node checked directly → §7.2.
ANSWER: The atlas's comparative fusion node is the right place to look and the horse is not in it. Veterinary species are outside the declared scope (coverage.md). I decline to give a closure age from memory — a species-specific timing figure is precisely the kind of quantitative species claim [MODEL] is barred from. Logged.

### a11  [adversarial]
CLAIM: The atlas holds teriparatide only as the drug that cannot be given to growing children; adult fracture-risk data are absent.
PROVENANCE: [ATLAS] for what is covered; [COVERAGE-GAP] for the question
CONFIDENCE: D (teriparatide node)
SPECIES_BASIS: human, mouse
PATH: teriparatide (L12, **D**); edge e00745 teriparatide –hypothesized_link, **speculative**→ growth_velocity_longitudinal (traversal_usable: false, context "human; regulatorily blocked by the osteosarcoma restriction")
REFS: FDA label; pth1r_receptor, jansen_metaphyseal_chondrodysplasia
GAPS_CROSSED: g_l12b_019 (does pharmacological PTH1R agonism expand the proliferative zone and increase linear growth in a human — method_blocked)
OPERATION: Alias resolution → node read → edge check (the only teriparatide edge is speculative and unusable) → scope boundary.
ANSWER: The atlas's framing is the opposite of the question: PTH1R is the receptor through which PTHrP holds prehypertrophic chondrocytes in the proliferative pool, so teriparatide is "in principle the most mechanistically apt drug in this layer — and it is the one that cannot be given to children for growth." The FDA label instructs avoidance with open epiphyses because of increased baseline osteosarcoma risk, inferred from rat carcinogenicity data. The node is graded **D** and its only outgoing edge is a `hypothesized_link` at speculative confidence, which the protocol forbids traversing. **Postmenopausal fracture-risk efficacy is not in the atlas** (adult bone density is out of scope). Logged.

### a12  [adversarial]
CLAIM: The atlas covers the microbiome→IGF-1→linear growth axis and contains nothing on obesity.
PROVENANCE: [ATLAS] for what is covered; [COVERAGE-GAP] for the question
CONFIDENCE: C (gut_microbiome_growth)
SPECIES_BASIS: mouse (causal), human (association only)
PATH: gut_microbiome_growth (L10, C), microbiome_igf1_axis; alias 'obesity' → **no entries**
REFS: yan2016
GAPS_CROSSED: g_l10env_001 (does manipulating the gut microbiota of an undernourished human child raise IGF-1 and increase linear growth — search_established)
OPERATION: Alias resolution → node read → the asked-for outcome is absent.
ANSWER: What the atlas has, and it is carefully bounded: "the gut microbiome is causally sufficient to change juvenile **body length** in gnotobiotic mice and has not been shown to do so in humans." Colonising germ-free mice raised bone formation, growth plate activity and longitudinal/radial bone growth with a substantial serum IGF-1 rise; antibiotics lowered IGF-1 and inhibited bone formation, and short-chain fatty acids restored both. The human version is an open `search_established` gap (g_l10env_001). **Obesity is not a node, an edge, a gap or an alias in this atlas.** I decline to answer on it. Logged.

### a13  [adversarial]
CLAIM: The atlas covers the scoliosis vicious-cycle mechanism but contains nothing about bracing.
PROVENANCE: [ATLAS] for what is covered; [COVERAGE-GAP] for the question
CONFIDENCE: B (scoliosis_vertebral_growth)
SPECIES_BASIS: human, rat, bovine, porcine
PATH: scoliosis_vertebral_growth (L6, B) → hueter_volkmann_law (C); full-text scan for 'brace'/'bracing' → **0 matches in graph.json**
REFS: stokes2006, stokes2002
GAPS_CROSSED: x-L6-02 (the 17%/0.1 MPa coefficient applied to humans without a human source), g_l6mech_012 (what determines reversible modulation vs permanent bar)
OPERATION: Alias/full-text scan → node read → scope boundary (coverage.md: surgical management out of scope).
ANSWER: The atlas holds adolescent idiopathic scoliosis as "the largest natural human experiment in physeal mechanobiology" via the vicious-cycle hypothesis — asymmetric loading modulates vertebral growth by Hueter-Volkmann, the vertebra wedges, the curve worsens — and notes a frontal-plane simulation using the **animal** stress–growth sensitivity reproduced observed progression rates. The animal counterpart is direct: sustained compression and distraction across rat and calf tail vertebrae produce wedging. **The word "brace" does not appear anywhere in the atlas.** And the coefficient that any bracing mechanism would have to invoke is itself an X-grade claim in humans (x-L6-02), so even the mechanistic substrate for an answer is unvalidated here. Logged.

### a14  [adversarial]
CLAIM: The atlas holds the mechanism of vitamin D deficiency rickets, not its epidemiology, and contains no UK prevalence figure.
PROVENANCE: [ATLAS] for the mechanism; [COVERAGE-GAP] for the prevalence
CONFIDENCE: B (vitamin_d_deficiency_rickets)
SPECIES_BASIS: human
PATH: vitamin_d_deficiency_rickets (L10, B), vitamin_d_calcitriol, vitamin_d_receptor, phosphate_homeostasis; full-text scan for a UK prevalence figure → none
REFS: (node key_refs); masuyama2006 for the chondrocyte-VDR link
GAPS_CROSSED: none covering prevalence
OPERATION: Alias resolution → node read → parameters search for a prevalence row → absent → §7.2.
ANSWER: What the atlas has is the entry point, and it corrects a common assumption: calcitriol acts via VDR to raise intestinal calcium and phosphate absorption, and when it fails **it is hypophosphataemia, not a direct chondrocyte effect, that produces the rachitic plate** — because normal phosphate is required for apoptosis of terminal hypertrophic chondrocytes and hence for orderly resorption of the hypertrophic zone. That yields the widened disorganised HZ and flared metaphysis. **No population prevalence figure for any country is in the atlas**, and a prevalence is a quantitative claim that [MODEL] cannot supply. Logged.

### a15  [adversarial]
CLAIM: The atlas covers mTORC1 as the nutrient-to-cell-size converter in chondrocytes and contains nothing on lifespan.
PROVENANCE: [ATLAS] for what is covered; [COVERAGE-GAP] for the question
CONFIDENCE: C (mtorc1_chondrocyte)
SPECIES_BASIS: mouse (only)
PATH: mtorc1_chondrocyte (L3, C), raptor_protein, amino_acid_sensing_chondrocyte; alias 'lifespan' → only 'finite proliferative capacity model of growth plate lifespan' (a different sense of the word)
REFS: chen2014 (Chen and Long)
GAPS_CROSSED: g_l3rest_010 (zonal mTORC1 activity in HUMAN growth plate — search_established, tractability 4)
OPERATION: Alias resolution → node read → note the alias collision → scope boundary.
ANSWER: Note first an alias trap: the only "lifespan" alias in the atlas resolves to `finite_proliferative_capacity_model`, meaning the *growth plate's* lifespan, not the organism's. On mTORC1 the atlas says: it sets biosynthetic capacity through S6K1 and 4E-BP1; Prx1-Cre deletion of mTor or Raptor sharply reduces embryonic skeletal growth with delayed hypertrophy; the mechanism is specifically **translational** — proliferation and survival unchanged, but chondrocyte cell size, matrix amount and protein synthesis rate all fall. Species basis: mouse only. And the zonal profile of mTORC1 activity in **human** growth plate has never been measured (g_l3rest_010). **Organismal lifespan and rapamycin longevity biology are not in the atlas.** Logged as scope boundary.

### a16  [adversarial]
CLAIM: The atlas contains nothing on slipped capital femoral epiphysis and, by its own statement, excludes surgical management.
PROVENANCE: [COVERAGE-GAP]
CONFIDENCE: n/a
SPECIES_BASIS: n/a
PATH: alias 'slipped'/'scfe' → **no entries**; full-text scan of graph.json → no match
REFS: n/a
GAPS_CROSSED: none exists
OPERATION: Alias resolution returned nothing → §7.1 (no covering gap) → §7.2.
ANSWER: No node, no edge, no gap. coverage.md states surgical management is out of scope. Surgical indications are also a clinical-decision claim, and the atlas's design principle — "it cannot exceed the measurement record" — is not a licence to substitute my training data for a missing node. The nearest atlas content is the physeal mechanics of Salter-Harris fracture propagation, which is itself blocked by the unresolved zonal stiffness contradiction (q17) — so the atlas could not support a mechanical account of the slip even if it tried. I decline. Logged as scope boundary.

### a17  [adversarial]
CLAIM: Nothing — brown adipose tissue does not appear in the atlas at all.
PROVENANCE: [COVERAGE-GAP]
CONFIDENCE: n/a
SPECIES_BASIS: n/a
PATH: alias 'brown adipose' → **no entries**; alias 'adipocyte' → only dlk1_gene ("preadipocyte factor 1"); full-text scan → no BAT content
REFS: n/a
GAPS_CROSSED: none exists
OPERATION: Alias resolution returned nothing → §7.2.
ANSWER: No node, no edge, no gap, no reference. The only adipose-adjacent content is DLK1/PREF-1 as a growth locus and the observation that PTHrP+ resting chondrocyte descendants do **not** become adipocytes in vivo (0/443 cells under rosiglitazone plus high-fat diet) — which is a negative result about a different lineage in a different tissue. I know the PRDM16/PGC-1α/UCP1 story and it does not belong in an [ATLAS] answer. Logged as scope boundary.

### a18  [adversarial]
CLAIM: The atlas covers androgens as growth-promoting agents in children, not anabolic steroid effects on adult bone density.
PROVENANCE: [ATLAS] for what is covered; [COVERAGE-GAP] for the question
CONFIDENCE: n/a for the question asked
SPECIES_BASIS: human (oxandrolone in Turner syndrome), rat (androgen_receptor edge e00468)
PATH: alias 'anabolic steroid' → **no entries**; nearest: oxandrolone, testosterone_hormone, androgen_receptor (edge e00468 required_for growth_velocity_longitudinal, C, "rat fetal metatarsal organ culture")
REFS: (turner_syndrome, oxandrolone node refs)
GAPS_CROSSED: none covering adult BMD
OPERATION: Alias resolution → adjacent nodes read → scope boundary (coverage.md: adult bone density out of scope).
ANSWER: The atlas's androgen content is paediatric and growth-directed: oxandrolone as a height-augmenting adjunct in Turner syndrome, testosterone thresholds relative to remaining growth (morning testosterone >10 nmol/L in boys with <4% of pubertal growth remaining), and an androgen receptor requirement for growth velocity resting on **rat fetal metatarsal organ culture** at confidence C. **Adult bone mineral density is explicitly out of scope** and there is no anabolic-steroid node. I decline to answer on adult BMD. Logged as scope boundary.

### a19  [adversarial]
CLAIM: The atlas covers bone age and fusion order and holds the key forensic assumption as an **unverified X-grade claim** — but it contains no forensic age-estimation practice.
PROVENANCE: [ATLAS] for the assumption and its status; [COVERAGE-GAP] for forensic practice
CONFIDENCE: A (bone_age, fusion_timing_order); the population-invariance assumption is X-grade
SPECIES_BASIS: human
PATH: bone_age (L7, A), bone_age_measurement_error, fusion_timing_order (A), population_variation_fusion; audit row **x-L7-02**
REFS: kvist2021, satoh2015
GAPS_CROSSED: g_l7fuse_008 (pooled inter- and intra-rater error of Greulich-Pyle and Tanner-Whitehouse, in years — open), g_l7fuse_007
OPERATION: Node read + audit ledger check; the atlas-relevant finding is returned and the out-of-scope part declined.
ANSWER: The atlas-relevant finding, and it is a warning rather than a method: **x-L7-02 holds "fusion order is conserved across human populations, only the timing shifts" as an X-grade claim** — repeated wherever a single-population union sequence is applied to another population, and in forensic anthropology standards, but not traceable to primary data establishing invariance. The underlying human data: MRI of 958 healthy 14.0–21.5 year olds gives an ascending foot-to-wrist order with site-specific completion percentages (17-year-old females: radius 75%, femur 85%, proximal tibia 97%, distal tibia 98%, calcaneus 98%); a Bosniak skeletal collection of 258 males aged 14–30 derived separate sequences for beginning and complete union with substantial variation. And the **pooled inter- and intra-rater error of Greulich-Pyle and Tanner-Whitehouse is an open gap** (g_l7fuse_008), which is exactly the quantity a forensic estimate needs. Forensic practice, standards and legal application are out of scope (coverage.md). Logged.

### a20  [adversarial]
CLAIM: The atlas covers FGF23 physiology and paediatric CKD growth failure separately, but not FGF23's role in CKD-MBD.
PROVENANCE: [ATLAS] for the two nodes; [COVERAGE-GAP] for the intersection asked
CONFIDENCE: A (fgf23_hormone), B (chronic_kidney_disease_growth)
SPECIES_BASIS: human, mouse
PATH: fgf23_hormone (L4, A) and chronic_kidney_disease_growth (L11, B); no edge connects them; alias 'renal osteodystrophy' → chronic_kidney_disease_growth
REFS: masuyama2006, fukumoto2026
GAPS_CROSSED: none covering the intersection
OPERATION: Alias resolution on both entities → node reads → edge check between them (none exists) → §7.2 for the intersection.
ANSWER: What the atlas has on FGF23 (grade A, direct human): a 251-residue osteocyte/osteoblast-derived phosphaturic hormone requiring α-Klotho to signal through FGFR1c in the proximal tubule, internalising NaPi-2a/2c, suppressing CYP27B1 and inducing CYP24A1 — lowering phosphate and calcitriol simultaneously. Excess (PHEX-mutant XLH, ADHR, tumour-induced osteomalacia) causes rickets and disproportionate short stature; loss of FGF23 or Klotho causes hyperphosphataemic tumoural calcinosis; VDR signalling **in chondrocytes** regulates osteoblast FGF23 production; and burosumab improved height velocity by 0.085–0.121 Z-score/year in 641 children with XLH. What it has on paediatric CKD: a multi-hit growth-failure node (acidosis, protein-energy wasting, secondary hyperparathyroidism, disordered vitamin D and phosphate handling, inflammation, acquired GH resistance), with growth failure associated with PTH levels in a national dialysis cohort, and rhGH effective because the defect is GH *resistance*. **There is no node, edge or gap on FGF23 in CKD-MBD specifically, and no edge joins the two nodes.** I decline to synthesise one across the gap. Logged.
