# Phase 2d — canonical-mechanism audit

Every target below was selected by `atlas/tools/mechanism_audit.py` for being
load-bearing (3–21 edges) **and** almost entirely supported by reviews or refs typed
`primary_abstract_only` — i.e. the primary evidence had never been read. This pass
retrieved the primary source and put four questions to it:

1. Does the primary data actually show the mechanism the field attributes to it?
2. Is the mechanism direct, or is there an unnamed intermediate?
3. Was it established in a system where the relevant **alternative** was present?
4. Has a later paper revised it without the revision propagating into reviews?

**Confirmations are recorded with the same weight as corrections.** A null result here
is evidence the node is solid, and it is the only thing that distinguishes a node that
has been checked from a node that merely has not been contradicted yet.

Shard: `l2daudit` · date run: 2026-08-05 · 12 targets.

**Verdicts: 4 CONFIRMED · 6 SCOPED · 2 SUPERSEDED · 0 UNVERIFIABLE.**
Corrections opened: **CORR-002** (collagen X), **CORR-003** (PKG-II).
Refs upgraded `primary_abstract_only` → `primary`: **21**.

---

## cnp_protein

- **canonical claim as the field states it:** CNP made by non-hypertrophic growth plate
  chondrocytes acts locally through NPR2 to drive endochondral bone growth, and the
  effect is partitioned almost entirely onto the hypertrophic zone; proliferation is
  essentially untouched.
- **primary source(s) actually read:** `nakao2015` (PMC5395013, **FULL TEXT** incl.
  figure legends and methods); `agoston2007` (PMC1847438, **FULL TEXT**);
  `miyazaki2022` (PMC8923661, **FULL TEXT**). `chusho2001` (PMC31171) is a scanned
  deposit — abstract only. `wu2003`, `hisadooliva2018`, `bocciardi2007`, `moncla2007`,
  `savarirayan2020` remain abstract only (not open access).
- **Q1 does the data show it: PARTIALLY.** The local-action claim is fully supported:
  cartilage-specific `Nppc` deletion reproduces the systemic-knockout dwarfism, and the
  n for the histology is **5 per group** (Fig. 2 legend — the node previously recorded
  "n not stated in text", which was wrong). The **zonal exclusivity is not supported as
  stated**. In the *Nppc* cKO the BrdU index only *tended* to be lower, but in the
  matched *Npr2* cKO the BrdU index was **significantly** lower, and the authors' own
  summary is "the height of the proliferative chondrocyte layer, along with the
  proliferation of chondrocytes in that region, was **moderately reduced** in both".
  The correct statement is a *graded* partition — potent on hypertrophy, mild but real
  on proliferation — not a hypertrophy-only effect.
- **Q2 direct or intermediate:** Intermediate, and it matters. The route from CNP to
  hypertrophy is asserted through PKG-II; see CORR-003 for why that link does not
  survive the primary data. `miyazaki2022` adds a second effector arm
  (PKG → BK channel → membrane hyperpolarisation → TRPM7 Ca²⁺ entry → CaMKII) in which
  chondrocyte-specific *Trpm7* ablation **abolishes** CNP-driven bone growth in explant.
- **Q3 alternative present in the system:** Yes, and the authors say so. The
  Col2a1-Cre;*Nppc*^fl/fl mouse still has CNP from every non-cartilage tissue, which is
  their stated explanation for why the *Nppc* cKO is milder than the *Npr2* cKO. They
  also raise ANP/BNP cross-activation of GC-B as a live alternative. So "the local pool
  is the physiological driver" is demonstrated for the *receptor*, and only bounded for
  the *ligand*.
- **Q4 later revision not in reviews:** `miyazaki2022` (2022) is a necessity result on a
  branch that reviews of CNP signalling still omit. It was present in the bibliography
  but was not linked from this node.
- **VERDICT: SCOPED.**
- **action taken:** Node summary rewritten to state the graded (not exclusive) zonal
  partition and to name the BrdU asymmetry between the two knockouts; `n=5` added to
  the three `nakao2015` quantitative rows; `miyazaki2022` added to `key_refs`; refs
  `nakao2015`, `agoston2007`, `miyazaki2022` upgraded to `primary`.

---

## fgfr3_receptor

- **canonical claim as the field states it:** The achondroplasia allele G380R activates
  FGFR3 in a ligand-independent manner *and* escapes down-regulation; quantitative FRET
  settled the argument in favour of increased unliganded dimerisation, and the
  down-regulation defect is disrupted c-Cbl-mediated ubiquitination.
- **primary source(s) actually read:** `sarabipour2016` (PMC4870120, **FULL TEXT**);
  `monsonegoornan2000` (PMC85119, **FULL TEXT**); `cho2004` (PMC327195, **FULL TEXT**).
  `shiang1994`, `naski1996`, `webster1996` (PMC449970 is a scanned page-image deposit),
  `colvin1996`, `deng1996`, `delezoide1998` remain abstract only.
- **Q1 does the data show it: PARTIALLY.** `monsonegoornan2000` and `cho2004` are
  faithfully represented. `sarabipour2016` is **over-read by the node**. The paper itself
  writes that "the finding that the Intrinsic FRET is similar for the wild-type and the
  G380R mutant … does not necessarily imply that their high resolution dimer structures
  are identical", and it reports that chemical cross-linking + Western blot *disagrees*
  with the FRET result ("we did not observe a significant increase in cross-linking due
  to the G380R mutation"), and that the same measurement in chemically produced vesicles
  gave ≈0.5 kcal/mol against −1.8 kcal/mol here. The node's "resolved the two claims" is
  stronger than the primary.
- **Q2 direct or intermediate: Intermediate, unnamed in the node.** c-Cbl does **not**
  bind FGFR3 directly. `cho2004` cites the FRS2α → Grb2 → c-Cbl ternary-complex model and
  notes that FRS2α binds FGFR1 far more strongly than FGFR3, so the recruitment step for
  FGFR3 is weakly established. The node states "c-Cbl-mediated ubiquitination" as a
  direct action.
- **Q3 alternative present in the system: THIS IS THE DECISIVE FINDING.** The
  `sarabipour2016` construct is **FGFR3 extracellular + transmembrane domain only, with
  the entire intracellular kinase domain replaced by a fluorescent protein**, in
  CHO-derived plasma-membrane vesicles. The alternative mechanism it is used to
  adjudicate against — failed receptor termination via kinase-dependent c-Cbl
  ubiquitination and internalisation — is **structurally absent from the assay**. This is
  the same shape as the ANKH/ENPP1 error: the experiment could not have seen the
  competing mechanism, so its silence is not evidence against it.
- **Q4 later revision not in reviews: Yes — an unrecorded direct contradiction.**
  `cho2004` reports **decreased** ubiquitination of mutant FGFR3; Monsonego-Ornan *et al.*
  (2004) report **increased** ubiquitination. `cho2004` names the disparity, lists four
  methodological differences (Cos-7 vs HEK293, steady-state FGF2 vs 30 min–6 h FGF9,
  retroviral vs transient expression) and concludes "we cannot exclude the alternate
  possibility." Reviews state the decreased-ubiquitination model without the caveat, and
  the atlas node inherited that.
- **VERDICT: SCOPED.**
- **action taken:** Node summary rewritten — `sarabipour2016` restated as adjudicating
  dimerisation only, with the construct truncation named explicitly; the −1.8 kcal/mol
  figure and the cross-linking disagreement added; FRS2α/Grb2 named as the intermediate;
  the ubiquitination-sign contradiction recorded. Gap `g_l2d_003` opened. Refs upgraded.

---

## ihh_protein

- **canonical claim as the field states it:** IHH from prehypertrophic chondrocytes drives
  chondrocyte proliferation directly through SMO, raises periarticular PTHrP, and its
  signal is transduced mainly by relief of GLI3 repressor.
- **primary source(s) actually read:** `stjacques1999` (PMC316949, **FULL TEXT**);
  `kobayashi2005` (PMC1143590, **FULL TEXT**); `mak2008` (PMC7188307, **FULL TEXT**);
  `tsiairis2008` (PMC2430380, **FULL TEXT**). `vortkamp1996`, `hilton2005`, `koziel2004`,
  `gao2001`, `hellemans2003` remain abstract only.
- **Q1 does the data show it: YES.** `stjacques1999` Fig. 4C: BrdU-positive fraction in
  the *Ihh*^−/− humerus is approximately half of the wild-type littermate from as early as
  12.5 dpc (P < 0.01 to < 0.005), together with a shortened proliferative zone. The
  three-output decomposition in the node (PTHrP arm / direct proliferative arm /
  PTHrP-independent hypertrophy arm) is exactly what `kobayashi2005` and `mak2008` show,
  including the key control that PTHrP heterozygosity has only a minimal effect on
  Ihh-driven column elongation.
- **Q2 direct or intermediate:** Direct for proliferation, as the node states — the
  chondrocyte-autonomous *Smo* result is the right adjudicating experiment.
- **Q3 alternative present in the system:** Two real caveats, neither fatal.
  (a) `mak2008` raises Hh signalling largely with **Shh protein** and *Ptch1* inactivation
  rather than with Ihh itself, so the "Ihh-specific" reading rests on pathway identity,
  not ligand identity. (b) `tsiairis2008` bypasses *Disp1*^C829F early lethality by
  supplying **exogenous non-cholesterol-modified Shh** — the system therefore contains a
  second Hh ligand at the time the shortened-range loop is scored.
- **Q4 later revision not in reviews:** None found. Searches for post-2015 primaries
  revising Ihh→proliferation or the Gli3-repressor model returned nothing that overturns
  it (see `g_l2d_005` search log).
- **VERDICT: CONFIRMED** (with the two Q3 caveats recorded in the node).
- **action taken:** Node summary annotated that the entire *Ihh*-null characterisation is
  embryonic (12.5–18.5 dpc, lethal at birth) so it says nothing about the postnatal growth
  plate; the Shh-substitution and N-Shh-rescue caveats added; refs upgraded to `primary`.

---

## pth1r_receptor

- **canonical claim as the field states it:** PTH1R activation by PTHrP maintains
  proliferation and delays hypertrophy; the human gain- and loss-of-function alleles
  (Jansen, Blomstrand) are mirror-image natural experiments.
- **primary source(s) actually read:** `schipani1997` (PMC28367, **FULL TEXT**);
  `chung1998` (PMC23697, **FULL TEXT**); `jobert1998` (PMC509062 — scanned deposit,
  **ABSTRACT ONLY**); `schipani1995`, `lanske1999` (PMC408525 blocked at fetch time)
  abstract only.
- **Q1 does the data show it: YES**, and the primaries are stronger than the node claimed.
  `schipani1997` does not merely produce chondrodysplasia: the constitutively active
  receptor **corrects the growth plate of PTHrP-null mice at birth and rescues their
  survival**, which is the epistasis result that puts the receptor downstream of the
  ligand. `chung1998` chimeras show PTH1R acts cell-autonomously on **proliferating**
  chondrocytes, and that matrix mineralization around ectopic hypertrophic cells is
  **non-cell-autonomous**, requiring a critical mass of adjacent hypertrophic cells.
- **Q2 direct or intermediate:** Direct — the chimera design is precisely the test that
  excludes an intermediate cell type.
- **Q3 alternative present in the system:** One genotype caveat. The Blomstrand patient in
  `jobert1998` is **heterozygous** for the splice-creating point mutation; the paternal
  allele was simply **not expressed**, by an unexplained mechanism. Functionally biallelic,
  genotypically not, n = 1. The node's "biallelic loss of functional receptor" is defensible
  but was carrying more genetic weight than the primary supports.
- **Q4 later revision not in reviews:** None found.
- **VERDICT: CONFIRMED.**
- **action taken:** Node summary extended with the PTHrP-null rescue, the associated
  **premature epiphyseal closure** in rescued animals (a rare mouse observation directly
  relevant to L7, since mice do not normally fuse), and the `jobert1998` genotype
  precision (n = 1, unexplained paternal silencing). `maass2015` was cited in the node
  prose but missing from `key_refs` — added. Refs upgraded.

---

## growth_plate_senescence

- **canonical claim as the field states it:** Growth plate senescence is intrinsic, local
  and **division-dependent rather than time-dependent**, demonstrated by conservation of
  growth potential across growth-inhibited periods.
- **primary source(s) actually read:** `marino2008` (PMC2276705, **FULL TEXT**);
  `ambrosi2021` (PMC8721524, **FULL TEXT**). `schrier2006`, `nilsson2005` remain abstract
  only (not open access); `emons2011` is a review.
- **Q1 does the data show it: PARTIALLY.** `marino2008` shows the delay in functional,
  structural and molecular senescence markers convincingly. But it also reports, in its own
  results, that **catch-up growth was incomplete** at the final measurement (P < 0.001 for
  the residual deficit in body mass, tail length and tibia length). The authors offer two
  explanations, and *both* imply that growth potential is only **partially** conserved:
  either hypothyroidism slows proliferative-zone division more than resting-zone division,
  or "the number of stem-cell divisions tends to be similar in various hormonal and
  nutritional states **but is not completely invariant**." "Conservation of growth
  potential" as an unqualified statement is stronger than the primary.
- **Q2 direct or intermediate:** The counted quantity is *resting-zone stem-like cell
  divisions*, which is inferred, not measured; the measured quantities are growth rate and
  histomorphometry. The intermediate is unmeasured in every species.
- **Q3 alternative present in the system: Yes, and acknowledged.** Gonadal suppression by
  leuprolide was **incomplete** — uterine mass ≈0.16 g against ≈0.1 g for ovariectomised and
  ≈0.5 g for intact mature rats. Oestrogen, the single most important alternative driver of
  growth plate senescence, was therefore present and unequal between arms, and the authors
  say so. This is exactly the Q3 failure mode.
- **Q4 later revision not in reviews:** Partially. The atlas already holds `mizuhashi2018`
  and `newton2019` (resting-zone chondrocytes acquire self-renewing stem cell behaviour
  after secondary ossification centre formation), which bear directly on whether the resting
  zone has a fixed finite division budget — but neither is cited from this node.
- **VERDICT: SCOPED.**
- **action taken:** Node summary changed from "conservation of growth potential" to
  "**partial** conservation", with the incomplete-catch-up result and the leuprolide
  confound stated; `ambrosi2021` explicitly scoped as marrow/periosteal skeletal stem
  cells at 24 months, not growth plate chondrocytes; cross-reference to `mizuhashi2018` /
  `newton2019` added; gap `g_l2d_006` opened. Refs upgraded.

---

## npr2_receptor

- **canonical claim as the field states it:** NPR2 is the CNP receptor guanylyl cyclase;
  its zonal protein distribution does *not* explain the zonal partition of the CNP effect,
  because NPR2 is uniform across zones while PKG-I/II are hypertrophic-enriched.
- **primary source(s) actually read:** `nakao2015` (PMC5395013, **FULL TEXT**);
  `agoston2007` (PMC1847438, **FULL TEXT**); `lauffer2020` (PMC7450217, **FULL TEXT**);
  `chikuda2004` (PMC522991, **FULL TEXT**). Eight human-genetics refs remain abstract only.
- **Q1 does the data show it: PARTIALLY — two source-attribution errors.**
  (a) The node's `localization` credits **prehypertrophic GC-B protein by IHC to
  `nakao2015`**. It is not in that paper's data. `nakao2015` uses GC-B IHC only to confirm
  knock-down, and states the zonal claim as a **citation to the group's own earlier work**.
  The recorded `contradicts: [nakao2015, agoston2007]` is therefore a contradiction between
  `agoston2007` and an *uncited older paper*.
  (b) The node says NPR2 transcript is "similar across all three zones (RZ, PZ, HZ)".
  `agoston2007` micro-dissected **resting/proliferative (combined), hypertrophic, and
  mineralized** zones. Its "three zones" are not RZ/PZ/HZ, and it contains **no RZ-vs-PZ
  comparison at all**.
- **Q2 direct or intermediate:** The claimed downstream intermediate (PKG-II) is the subject
  of CORR-003.
- **Q3 alternative present in the system:** `nakao2015` raises ANP/BNP cross-activation of
  GC-B, and osteocrin/NPR3 clearance modulation, as untested alternatives in the *Nppc*
  cKO. Also note `agoston2007`'s new-to-this-node result: CNP induces **Npr3 16-fold in the
  hypertrophic zone only** (real-time PCR confirmed), a negative feedback loop that is
  itself zone-specific and is a competing explanation for zonal dose-response.
- **Q4 later revision not in reviews:** `miyazaki2022` (see cnp_protein).
- **VERDICT: SCOPED.**
- **action taken:** `localization` corrected — the prehypertrophic GC-B IHC claim is no
  longer attributed to `nakao2015` and is flagged as needing its true primary; the
  `agoston2007` zone definition corrected to resting/proliferative-combined vs hypertrophic
  vs mineralized; the Npr3 feedback result added; `nakao2015` BrdU significance (significant
  in *Npr2* cKO) added. Gap `g_l2d_002` opened for the true source of the prehypertrophic
  GC-B map. Refs upgraded.

---

## collagen_type_x

- **canonical claim as the field states it:** Collagen X is the canonical hypertrophic-zone
  marker and is largely dispensable for hypertrophy; the mouse null is essentially normal,
  with at most a compressed growth plate showing **reduced hypertrophic zone height**, and
  human COL10A1 knockout iPSC chondrocytes hypertrophy and ossify normally.
- **primary source(s) actually read:** `gress2000` (PMC2174562, **FULL TEXT**);
  `kamakura2023` (PMC10184020, **FULL TEXT**); `meng2025` (PMC12743679, **FULL TEXT**).
  `rosati1994`, `warman1993`, `yang2025`, `reginato1995` remain abstract only.
- **Q1 does the data show it: NO — the zone is reversed, and the null is not silent.**
  `gress2000` histomorphometry: "the **proliferative zone** in all KO mice was more
  compressed than the hypertrophic, **which was opposite that seen in the Tg mice**", with
  an ≈14% overall decrease in growth plate width at day 21. The mouse null also carries
  ≈10.8% perinatal lethality at week 3, a further cohort dying by 12 weeks (≈14% total),
  marrow aplasia and lymphatic organs at ≈80% of control. `kamakura2023` is likewise not a
  null result: the bone-area fraction in transplanted `COL10A1`^−/− tissue was
  **significantly larger** in the 414C2 background, and the hypertrophic-phase transcriptome
  shifted **away from proliferating-phase and toward calcification-phase genes** — the
  authors' own reading is "acceleration of differentiation".
- **Q2 direct or intermediate:** A collagen expressed **exclusively** in hypertrophic
  chondrocytes produces its clearest histological effect in the **proliferative** zone. That
  is a non-cell-autonomous action through an unnamed intermediate, and it is the most
  interesting thing in this node.
- **Q3 alternative present in the system:** Yes. `gress2000` explicitly separates the null
  (loss of function, proliferative-zone compression) from the collagen-X transgenic
  (dominant interference, hypertrophic-zone compression) and attributes the zonal difference
  to the two different mechanisms. Conflating them is what produces the error in the node.
- **Q4 later revision not in reviews:** `gress2000` *is* the revision of `rosati1994`, and
  it has propagated into reviews only as "a subtle phenotype", losing both the zone and the
  lethality.
- **VERDICT: SUPERSEDED** (of the specific zonal statement) → **CORR-002**.
- **action taken:** See CORR-002. Node summary corrected, two quantitative rows re-stated,
  one flagged `superseded_model: true`, edge `e00568` note added, refs upgraded.

---

## pthrp_ihh_feedback_loop

- **canonical claim as the field states it:** PTHrP from the periarticular region and IHH
  from prehypertrophic cells form a closed negative feedback loop whose geometry sets the
  length of the proliferative column.
- **primary source(s) actually read:** `stjacques1999`, `kobayashi2005`, `mak2008`,
  `tsiairis2008` (all **FULL TEXT**, as above). `vortkamp1996`, `lee1996`, `karp2000`,
  `kobayashi2002`, `long2001`, `koziel2004` remain abstract only.
- **Q1 does the data show it: YES**, for every arm taken separately, and the node is unusually
  careful in already stating that the loop has never been characterised as a control system —
  no diffusion coefficient, no decay length, no transfer function, no loop gain. That
  statement survived the audit intact.
- **Q2 direct or intermediate:** The Ihh → periarticular *Pthlh* arm is the one with a
  candidate unnamed intermediate — `stjacques1999` itself notes the perichondrial relay
  hypothesis, and `koziel2004` argues for direct long-range action. The node presents the
  direct reading; the relay alternative is not formally excluded in anything I could read.
- **Q3 alternative present in the system:** The `tsiairis2008` N-Shh rescue (a second Hh
  ligand present during the experiment) and the `mak2008` use of Shh protein as the
  activating ligand, as under `ihh_protein`.
- **Q4 later revision not in reviews:** None found.
- **VERDICT: CONFIRMED.**
- **action taken:** Node annotated with the perichondrial-relay alternative for the
  Ihh→*Pthlh* arm and with the two ligand-substitution caveats; no claim retracted. Refs
  upgraded.

---

## fgfr3_npr2_crosstalk

- **canonical claim as the field states it:** FGFR3 inactivates NPR2 post-translationally by
  driving dephosphorylation of its seven juxtamembrane sites; preventing that
  dephosphorylation genetically rescues achondroplasia.
- **primary source(s) actually read:** `robinson2017` (PMC5651182, **FULL TEXT**);
  `shuhaibar2017` (PMC5745078, **FULL TEXT**); `wagner2021` (PMC8262296, **FULL TEXT**).
  `ozasa2005`, `yasoda2004`, `savarirayan2020` remain abstract only.
- **Q1 does the data show it: PARTIALLY — the rescue is narrower than stated.** `wagner2021`
  is a **homozygous × homozygous** cross: `GC-B`^7E/7E into `FGFR3`^G380R/G380R. Human
  achondroplasia is heterozygous. The rescue is also anatomically partitioned — femur and
  tibia are restored, but **midface hypoplasia and macrocephaly are not rescued at all**, and
  the cranial-length comparison was underpowered (post-hoc power 36%; ~50 mice/group needed).
  And the effect is strongly **sex-specific at 2 weeks**: G380R shortened bones and reduced
  hypertrophic zone area in **males only**; GC-B-7E lengthened bones in **females only**; the
  hypertrophic-zone rescue was demonstrated in males because females had no deficit to rescue.
  The node stated a flat "restored to wild-type values".
- **Q2 direct or intermediate: an explicitly unnamed intermediate.** `shuhaibar2017`
  identifies only "a PPP-family phosphatase", inferred from 100 µM cantharidin, which
  inhibits PPP1, PPP2/PP2A, PPP4 and PPP5 together. No individual phosphatase has been
  identified in growth plate.
- **Q3 alternative present in the system: yes, in the mechanistic papers.** `robinson2017`
  uses **FGF2** on rat chondrosarcoma cells that express **FGFR2 as well as FGFR3**, with no
  receptor-specific knockdown; `shuhaibar2017` likewise applies FGF, not an FGFR3-selective
  perturbation, to intact tibia. Receptor specificity comes only from `wagner2021`'s genetics
  — and `wagner2021` **never measured NPR2 phosphorylation state in a G380R growth plate**,
  concluding only that it "cannot rule out that other FGFR3-activated signaling pathways also
  participate". The chain FGFR3-G380R → phosphatase → NPR2-dephospho has never been observed
  end-to-end in one system.
- **Q4 later revision not in reviews:** No revision; but `wagner2021` itself notes the
  phosphatase inhibitor LB-100 synergises with vosoritide, which is the therapeutic corollary
  and is not in the node.
- **VERDICT: SCOPED.**
- **action taken:** Node summary rewritten to state homozygosity, sex-specificity and the
  cranial non-rescue, to record that NPR2 phosphorylation has never been measured in a G380R
  growth plate, and to note the FGFR2 co-expression in RCS cells; effect sizes (12.6% / 7.9%
  vs 4.3% / 5.0% femur gain; +70.2% hypertrophic zone area, P = 0.003) added as quantitative
  rows. Gap `g_l2d_004` opened for phosphatase identity. Refs upgraded.

---

## catch_up_growth

- **canonical claim as the field states it:** Catch-up growth is generated locally within the
  growth plate by conserved proliferative capacity, demonstrated by producing catch-up in a
  single locally treated rabbit growth plate.
- **primary source(s) actually read:** `marino2008` (PMC2276705, **FULL TEXT**) — the rat
  replication. `baron1994` and `gafni2001`, the two rabbit primaries that carry the local and
  the histological-senescence claims respectively, are **not open access and were not
  reachable**; both remain `primary_abstract_only`. `wit2002` and `lui2011` are reviews.
- **Q1 does the data show it: PARTIALLY.** For the claim that catch-up reflects delayed
  senescence, `marino2008` is a clean full-text confirmation in rat. For the *completeness*
  of conserved growth potential it is a partial disconfirmation — catch-up was incomplete
  (see growth_plate_senescence). The node already says "may be complete or incomplete",
  which is correct and survives.
- **Q2 direct or intermediate:** The postulated intermediate — the resting-zone stem cell
  division count — is never measured; growth rate and marker expression stand in for it.
- **Q3 alternative present in the system:** Incomplete gonadal suppression in `marino2008`
  (leuprolide, uterine mass ≈0.16 g), leaving oestrogen as an uncontrolled co-driver. The
  systemic alternative is also not fully excluded by this study: `marino2008` observed
  catch-up in **heart, liver and kidney mass** too, and explicitly allows that "the observed
  catch-up growth in nonskeletal organs could be explained by a systemic mechanism". The
  node's claim that catch-up is evidence **against** a central size sensor rests on
  `baron1994`, which I could not read.
- **Q4 later revision not in reviews:** None found.
- **VERDICT: SCOPED.**
- **action taken:** Node annotated that the anti-central-sensor argument rests on a single
  unread rabbit primary, and that `marino2008` itself observed multi-organ catch-up
  compatible with a systemic contribution. `baron1994` and `gafni2001` escalated to
  `atlas/sources/access_queue.md` (P1 and P2) with the specific figures required. Node marked
  `pending_source: baron1994`; confidence held at B because the phenotype itself is
  human-measured and the mechanism claim was already hedged. `marino2008` upgraded to
  `primary`.

---

## fgfr3_mapk_branch

- **canonical claim as the field states it:** The RAS-RAF-MEK-ERK branch downstream of FGFR3
  is the arm that suppresses hypertrophy, leaving proliferation to STAT1.
- **primary source(s) actually read:** `murakami2004` (PMC338282, **FULL TEXT**);
  `shuhaibar2017` (PMC5745078, **FULL TEXT**); `agoston2007` (PMC1847438, **FULL TEXT**).
  `yasoda2004` and `ozasa2005` remain abstract only.
- **Q1 does the data show it: YES, precisely.** Constitutively active MEK1 in chondrocytes
  gives incomplete hypertrophy, reduced collagen X, persistent Sox9 and delayed endochondral
  ossification with **no change in BrdU incorporation** (Fig. 1P–Q), and BrdU-pulse-chase at
  P13 shows labelled cells stalling in the prehypertrophic region. The Stat1 dissociation is
  in the same paper: loss of Stat1 restores proliferation in Fgfr3-ACH mice but rescues
  neither the hypertrophic zone nor the phenotype.
- **Q2 direct or intermediate:** Logically, activating a downstream node (MEK1) and finding it
  suppresses the *Fgfr3*-null overgrowth shows **sufficiency**, not necessity — the authors
  write "mediated **at least in part** by the MAPK pathway", which the node paraphrased as
  "placing MAPK downstream". Fair but worth stating.
- **Q3 alternative present in the system:** The transgene is a constitutively active MEK1
  under a Col2a1 driver with mosaic expression (X-gal, Fig. 1T), i.e. supraphysiological and
  non-uniform; endogenous ERK amplitude under FGFR3-G380R is not what was tested. Separately,
  `agoston2007` shows CNP requires **p38** (not ERK) to achieve the expanded hypertrophic
  zone, while inhibiting ERK — so "the MAPK branch" is at least two antagonistic MAPK arms,
  and only the ERK arm is in this node.
- **Q4 later revision not in reviews:** None found.
- **VERDICT: CONFIRMED.**
- **action taken:** Node annotated with the sufficiency-vs-necessity distinction, the mosaic
  supraphysiological transgene caveat, and the p38 arm from `agoston2007`. Refs upgraded.

---

## pkg2_kinase

- **canonical claim as the field states it:** PKG-II is *the* kinase that carries the CNP
  signal in chondrocytes, acting as the switch from proliferation to hypertrophy by blocking
  SOX9 nuclear entry, and its hypertrophic-zone enrichment is the best explanation for why
  the CNP/NPR2 effect lands on the hypertrophic zone.
- **primary source(s) actually read:** `chikuda2004` (PMC522991, **FULL TEXT**);
  `agoston2007` (PMC1847438, **FULL TEXT**); `nakao2015` (PMC5395013, **FULL TEXT**);
  `miyazaki2022` (PMC8923661, **FULL TEXT**). `pfeifer1996`, `kawasaki2008`, `dazgonzlez2022`
  remain abstract only.
- **Q1 does the data show it: NO, for the zonal-explanation claim.** `chikuda2004` Fig. 3A:
  "cGKII was expressed predominantly in the **late proliferative and prehypertrophic**
  chondrocytes, preceding the start of hypertrophic differentiation" — that is the only
  **protein-level** zonal map of PKG-II in the growth plate, and it places the kinase upstream
  of, not inside, the hypertrophic zone. The node's opposite claim comes from `agoston2007`,
  which is **mRNA** from micro-dissected mouse tibia whose zones are
  resting/proliferative-combined, hypertrophic and mineralized. mRNA and protein disagree,
  across species, and the node reported only the mRNA.
- **Q2 direct or intermediate:** `miyazaki2022` supplies a *different* PKG substrate — the BK
  channel — driving hyperpolarisation, TRPM7-mediated Ca²⁺ entry and CaMKII, with
  chondrocyte-specific *Trpm7* ablation **abolishing** CNP-driven growth. SOX9 and GSK-3β are
  candidate substrates, not established sole intermediates.
- **Q3 alternative present in the system:** `chikuda2004` explicitly could not exclude cGKI:
  "the possibility of the involvement of cGKI cannot be ruled out … It would be helpful to
  investigate whether mice doubly deficient for cGKI and cGKII mimic the phenotype of
  CNP^−/− mice." `agoston2007` independently reaches the same conclusion (Prkg1 is 5.9-fold
  zone-enriched, more than Prkg2's 4.4-fold) and also calls for the double knockout. That
  experiment has still not been done. The relevant alternative was present, was named by both
  primaries, and was dropped by the node.
- **Q4 later revision not in reviews: the phenotype directions are opposite and both source
  papers say so.** `chikuda2004`: the KMI (Prkg2-mutant) growth plate is **2.6× EXPANDED** —
  665 ± 47 µm vs 255 ± 34 µm, n = 8 — by an intermediate layer of postmitotic **non**-hypertrophic
  cells. `nakao2015`: the cartilage-specific *Npr2* knockout hypertrophic layer is **23.0% of
  control** and the whole plate is thinner. A linear CNP → GC-B → cGMP → PKG-II chain predicts
  these phenocopy; they are opposite in sign. `chikuda2004` names it ("the growth plate of the
  former is reduced in height … whereas that of the latter is increased in height. This may
  indicate the involvement of other signaling pathway(s)"), `nakao2015` names it ("there still
  remains elusive problem"), `agoston2007` names it — and reviews propagate the linear chain
  anyway.
- **VERDICT: SUPERSEDED** (the zonal-explanation claim) → **CORR-003**.
- **action taken:** See CORR-003. Node summary rewritten, `contradicts` added, confidence
  regraded B → C, gap `g_l2d_001` opened for the cGKI/cGKII double knockout, edges `e00108`,
  `e00109`, `e00120` annotated. Refs upgraded.

---

## Refs upgraded from `primary_abstract_only` to `primary`

Read in full during this pass and recorded in `atlas/sources/shards/l2daudit.yaml`
(21 upgrades): `agoston2007`, `chikuda2004`, `nakao2015`, `sarabipour2016`,
`monsonegoornan2000`, `cho2004`, `stjacques1999`, `kobayashi2005`, `mak2008`,
`tsiairis2008`, `schipani1997`, `chung1998`, `gress2000`, `kamakura2023`, `wagner2021`,
`shuhaibar2017`, `robinson2017`, `murakami2004`, `marino2008`, `ambrosi2021`,
`miyazaki2022`.

Attempted and **not** upgraded — these are honest failures, not oversights:
`jobert1998` and `webster1996` are scanned page-image deposits in PMC with no machine
-readable body; `chusho2001` likewise; `baron1994`, `gafni2001`, `ozasa2005`, `yasoda2004`,
`schrier2006`, `nilsson2005`, `rosati1994`, `savarirayan2020` and the NPR2 human-genetics
series are not open access. Rows for the ones that block a mechanism are in
`atlas/sources/access_queue.md`.
