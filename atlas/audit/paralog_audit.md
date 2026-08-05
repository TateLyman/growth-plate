# Paralog-attribution audit

**Shard:** `paralog` · **date run:** 2026-08-05 · **bibliography:** `atlas/sources/shards/paralog.yaml`

## Why this pass exists

Three findings in this build share one mechanical structure: an effect attributed to
entity **A** when a paralog, isoform or cross-reactive relative **B** was co-present,
more abundant in the relevant zone, or was the literal agent used in the key experiment.

| Prior finding | Shape |
|---|---|
| ANKH / ENPP1 (CORR-001) | PPi transport attributed to ANKH; ENPP1 was in the cells |
| PKG-II / cGKI (CORR-003) | plate phenotype attributed to PKG-II; cGKI co-expressed at **higher** zonal enrichment (5.9× vs 4.4×); double knockout never made |
| IGF1R / insulin (phase3_close) | the one cartilage mTORC1 experiment used **insulin**, not IGF-1 |

Rather than wait for a fourth instance, every node attributing a mechanism to a specific
molecule was put through five questions: (a) does a paralog exist; (b) is it expressed in
the relevant zone and at what relative abundance; (c) was the key perturbation selective
for A over B and at what fold; (d) was the ligand/agonist selective or cross-reactive;
(e) has the double perturbation been done.

## The decision rule applied

Applied uniformly, so the CLEAN/AT_RISK ratio means something:

- A **selective genetic loss of function that produces a phenotype** attributes necessity
  to that gene correctly. Paralogs merely *existing* does not undermine it. → CLEAN.
- Paralog risk arises when (i) the perturbation is **pharmacological or otherwise
  non-selective**, (ii) the evidence is **expression-level or correlative** but the claim
  is causal, or (iii) the claim is of **exclusivity or sufficiency** ("A is *the*
  effector") while B is co-present and never removed.
- A node that **explicitly withholds** attribution and names the unexcluded relative is
  CLEAN — that is the behaviour this audit is trying to produce, not a failure of it.

## Result

**91 nodes audited · 80 CLEAN · 9 AT_RISK · 0 SUPERSEDED**, plus **2** (`pkg2_kinase`,
`cgmp_second_messenger`) re-read from the prior pass where the SUPERSEDED verdict of
CORR-003 already stands.

No `CORR-00N` opened: nothing found here kills a mechanism outright. One direct
**contradiction between two independent primary lines** was found (`mmp13_protease`,
below) and is logged in `contradictions.md` §1 rather than as a correction, because
neither paper supersedes the other.

Nine gaps opened: `g_para_001` … `g_para_009`. Nodes that passed carry
`paralog_audit: passed` with the date; nodes that did not carry `paralog_risk` with a
one-line statement of which relative is unexcluded. **No confidence grade was changed** —
per the standing rule, being at risk is not the same as the primary evidence failing, and
in no case here did the primary evidence fail.

### Worst family record

**Thyroid (THRA / THRB / DIO2 / DIO3): 2 of 4 AT_RISK**, and the two failures are the
load-bearing ones. The isoform question is *unresolved in the atlas's own contradiction
log* and the resolving experiment — `gthe1999`'s TRα1⁻/⁻β⁻/⁻ double null — shows that
**single receptor deletions reveal only a small proportion of the hypothyroid phenotype**,
which invalidates the inference from either single null to isoform assignment. The
deiodinase half is worse: `dio2_deiodinase` carried *no primary DIO2 growth plate
reference at all* before this pass (its only `key_ref` was `robson2000`, a **receptor**
localisation paper), and DIO1 — the other activating deiodinase — is not mentioned in the
node.

### Best family record

**Redundant-pair transcription factors and matrix enzymes.** SOX5/SOX6, RUNX2/RUNX3,
SMAD1/SMAD5, LRP5/LRP6, ADAMTS4/ADAMTS5, TNAP/PHOSPHO1 and Noggin/Chordin **all have the
double perturbation published**, and in every case the atlas node already states the
gene-dose framing rather than a single-gene one. Seven families, seven doubles, zero
risk. This is the control group that shows the audit is not simply flagging everything.

---

# Entries

Ordered by family. `→` marks the action taken.

---

## FGF receptor family — FGFR1 / FGFR2 / FGFR3 / FGFR4

## fgfr1_receptor
- **mechanism attributed to:** FGFR1 acting at the chondro-osseous junction and perichondrium; delayed hypertrophic maturation on deletion.
- **paralogs/isoforms in family:** FGFR2, FGFR3, FGFR4; also IIIb/IIIc splice isoforms of FGFR1 itself.
- **co-expressed in the relevant zone? relative abundance:** Yes but **spatially separated**, which is the discriminator. `delezoide1998` human fetal ISH: FGFR1 and FGFR2 are perichondrial/periosteal, FGFR3 is the only receptor in growth plate chondrocytes. In the cranial vault all three co-express, which is why the craniosynostosis phenotypes are FGFR1/2 and the chondrodysplasia phenotypes are FGFR3.
- **key experiment's perturbation and its SELECTIVITY:** `jacob2006`, conditional *Fgfr1* deletion in the osteo-chondrogenic lineage — **gene-selective by construction**, fold-selectivity not applicable.
- **ligand/agonist selectivity:** Not load-bearing; the claim rests on genetics and ISH, not on applied ligand.
- **double perturbation done?** Yes for the eminence phenotype — *Fgfr1;Fgfr2* combined loss in Scleraxis-lineage cells, cited in node. Not needed for the zonal claim, which is settled by non-overlapping expression.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. The FGFR family is the *positive control* for this whole audit: the atlas resolved the paralog question at authoring by using the human expression map rather than the mouse functional data.

## fgfr2_receptor
- **mechanism attributed to:** FGFR2 marks prechondrogenic condensations, then perichondrium/periosteum/periarticular cartilage; contributes to condensation, not to zonal control.
- **paralogs/isoforms in family:** FGFR1/3/4.
- **co-expressed in the relevant zone? relative abundance:** Explicitly **not** in columnar or hypertrophic chondrocytes (`delezoide1998`, human).
- **key experiment's perturbation and its SELECTIVITY:** ISH localisation, gene-specific probes. No functional perturbation claimed by the node — correctly.
- **ligand/agonist selectivity:** n/a.
- **double perturbation done?** Not required; the node claims no growth plate function to be excluded.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`.

## fgfr3_receptor
- **mechanism attributed to:** FGFR3 as the growth plate brake; G380R as combined ligand-independent activation plus failed down-regulation.
- **paralogs/isoforms in family:** FGFR1/2/4.
- **co-expressed in the relevant zone? relative abundance:** FGFR3 is the **only** FGFR in human fetal growth plate chondrocytes (`delezoide1998`). Relative abundance of FGFR1/2 there: not detected.
- **key experiment's perturbation and its SELECTIVITY:** `colvin1996`/`deng1996` *Fgfr3*-null — gene-selective. `toydemir2006` human *FGFR3* R621H CATSHL — allele-selective. Both arms selective.
- **ligand/agonist selectivity:** **Cross-reactive, and the node says so.** FGF2 and FGF1 activate several FGFRs; `sarabipour2016`'s FRET used FGF1/FGF2, and `sahni1999`'s proliferation arrest used FGF2. The node states in terms that "effects attributed to FGF2 in cartilage cannot be assigned to FGFR3 without genetic confirmation". The genetic confirmation exists, so the chain closes.
- **double perturbation done?** Not applicable — the *absence* of FGFR1/2 from the compartment does the work a double knockout would.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. Note recorded that a further paralog asymmetry is already captured: FRS2α binds FGFR1 far more strongly than FGFR3, which the node correctly uses to weaken the c-Cbl recruitment step rather than to strengthen it.

## fgf2_ligand
- **mechanism attributed to:** FGF2 as the *experimental* agonist, explicitly not as a physiological ligand.
- **paralogs/isoforms in family:** FGF1, FGF9, FGF18 and the rest of the FGF family; FGF2 activates FGFR1c/2c/3c.
- **co-expressed in the relevant zone? relative abundance:** The physiological ligands in vivo are FGF18 (chondrocyte control) and FGF9 (vascularisation) per `hung2016`.
- **key experiment's perturbation and its SELECTIVITY:** n/a — the node makes no attribution to defend.
- **ligand/agonist selectivity:** **None, and the node states it.**
- **double perturbation done?** n/a.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. This is an attribution correctly *withheld*; it is the pattern that would have prevented CORR-003.

## fgf18_ligand / fgf9_ligand
- **mechanism attributed to:** FGF18 as the principal FGFR3 ligand in the plate; FGF9 as the vascularisation-dominant ligand.
- **paralogs/isoforms in family:** each other, plus FGF8/17 (same subfamily as FGF18).
- **co-expressed in the relevant zone? relative abundance:** Both perichondrial. The `hung2016` **allelic series combines both genes** and separates their contributions directly.
- **key experiment's perturbation and its SELECTIVITY:** Gene-selective nulls plus the combined allelic series — this *is* the double perturbation.
- **ligand/agonist selectivity:** `ozasa2005` used FGF18 protein on ATDC5, which is subfamily-cross-reactive; but the in vivo genetics carry the claim.
- **double perturbation done?** **Yes — `hung2016`.**
- **VERDICT: CLEAN** (both nodes)
- **action:** → `paralog_audit: passed` on both.

---

## Natriuretic peptide family — CNP / ANP / BNP · NPR1 / NPR2 / NPR3

## npr2_receptor
- **mechanism attributed to:** NPR2 as the receptor guanylyl cyclase generating the cGMP that drives growth plate output; hypertrophic-zone-weighted partition of that effect.
- **paralogs/isoforms in family:** **NPR1 (GC-A)**, the second receptor guanylyl cyclase, ligand ANP/BNP; NPR3, the clearance receptor.
- **co-expressed in the relevant zone? relative abundance:** **Not measured.** No study locates NPR1 protein or transcript by zone in growth plate of any species (`g_para_002` search log). The atlas records NPR2 transcript as flat across compartments (`agoston2007`) and has no NPR1 datum at all.
- **key experiment's perturbation and its SELECTIVITY:** `nakao2015` cartilage-specific *Npr2* deletion — **gene-selective**, and the phenotype (hypertrophic layer 23.0% of control, femur 45.3%) is a genuine necessity result for NPR2. That much is untouched.
- **ligand/agonist selectivity:** CNP is strongly NPR2-preferring, so the ligand arm is not the problem. **The problem is the reciprocal**: ANP has its own receptor in the same cell.
- **double perturbation done? NEVER.** No *Npr1;Npr2* or *Nppa;Nppc* compound mutant exists in cartilage.
- **VERDICT: AT_RISK**
- **The finding:** `zhou2024` (Commun Biol, PMID 39443661) shows *Corin*- and *Nppa*(ANP)-null mice have **impaired chondrocyte differentiation and shortened limb long bones**, with ANP acting **in chondrocytes** through **cGMP-dependent protein kinase G** to suppress MAPK phosphorylation and raise pGSK-3β/β-catenin. That is the same second messenger, the same kinase family and two of the same substrates (GSK-3β) that the atlas attributes wholly to the CNP→NPR2 arm. `nakao2015`'s authors already raised ANP/BNP cross-activation of GC-B as a live alternative; this is stronger than cross-activation — it is a **genetic requirement for a parallel ligand–receptor pair feeding the same pool**.
- **What is *not* at risk:** NPR2's necessity, the human *NPR2* dose series (AMDM, heterozygous ISS, gain-of-function tall stature), and vosoritide's mechanism. Human *NPR2* genetics is gene-selective and settles requirement in humans.
- **action:** → `paralog_risk` added: *"The chondrocyte cGMP–PKG pool is attributed entirely to NPR2; NPR1/ANP is a genetically required parallel source in the same cell (`zhou2024`) and has never been removed in the same animal."* → gap `g_para_001` opened (double perturbation + zonal NPR1 map). Confidence held at **B** — the primary NPR2 evidence did not fail.

## cnp_protein
- **mechanism attributed to:** locally made CNP as the physiological driver of the natriuretic-peptide growth arm.
- **paralogs/isoforms in family:** **ANP (NPPA), BNP (NPPB).**
- **co-expressed in the relevant zone? relative abundance:** *Nppc* transcript flat across compartments (`agoston2007`); *Nppa*/*Nppb* in growth plate **never measured**.
- **key experiment's perturbation and its SELECTIVITY:** `nakao2015` cartilage-specific *Nppc* deletion — gene-selective, but **milder than the *Npr2* cKO**, which the authors attribute to residual CNP from non-cartilage tissue. An equally consistent reading after `zhou2024` is that part of the receptor-side phenotype is ANP-driven.
- **ligand/agonist selectivity:** CNP is NPR2-preferring; not the failure point.
- **double perturbation done? NEVER** — no *Nppa;Nppc* compound cartilage mutant.
- **VERDICT: AT_RISK**
- **action:** → `paralog_risk`: *"ANP is genetically required for chondrocyte differentiation via chondrocyte cGMP–PKG (`zhou2024`); the *Nppc*-cKO-versus-*Npr2*-cKO severity gap is currently explained by extra-cartilage CNP alone, with the ANP arm unexcluded."* → covered by `g_para_001`. Confidence held at **B**.

## npr3_clearance_receptor
- **mechanism attributed to:** NPR3 as the clearance receptor setting local CNP concentration; CNP-inducible negative feedback.
- **paralogs/isoforms in family:** NPR1, NPR2 — but NPR3 is the only family member **without** a guanylyl cyclase domain, so its function is structurally distinct.
- **co-expressed in the relevant zone? relative abundance:** *Npr3* induced **16-fold by CNP in the hypertrophic zone and nowhere else** (`agoston2007`) — a zone-resolved number, which is more than most nodes in this atlas have.
- **key experiment's perturbation and its SELECTIVITY:** Human biallelic *NPR3* loss of function (`moffatt2025`, `lauffer2022`) — **gene-selective, human, and the phenotype (tall stature, skeletal overgrowth) is the predicted direction**.
- **ligand/agonist selectivity:** NPR3 binds all three natriuretic peptides — and the node **says so explicitly** rather than claiming CNP specificity.
- **double perturbation done?** Not required; human genetics is gene-selective.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. Note that the ANP finding in `g_para_001` *increases* this node's importance rather than threatening it: a promiscuous clearance receptor is exactly the shared node two ligand arms would compete at.

## pkg2_kinase / cgmp_second_messenger
- **Already adjudicated — CORR-003.** PKG-II attribution SUPERSEDED for the zonal claim; cGKI named as the unexcluded relative at 5.9× vs 4.4×; `g_l2d_001` open on the *Prkg1;Prkg2* double. Re-read in this pass: no further paralog exposure, and `cgmp_second_messenger` remains the node that had it right.
- **VERDICT: SUPERSEDED (prior pass), no new action.**
- **action:** → note appended to `cgmp_second_messenger` that the cGMP pool now has an unresolved *source* question (NPR1/ANP, `g_para_001`) in addition to its unresolved *effector* question (cGKI vs cGKII, `g_l2d_001`). Two independent unexcluded relatives on one second messenger.

---

## Phosphodiesterase isoforms

## pde3b
- **mechanism attributed to:** PDE3B as the phosphodiesterase degrading NPR2-derived cGMP in the growth plate; the node calls it "the phosphodiesterase with the strongest functional evidence".
- **paralogs/isoforms in family:** **PDE3A** — and PDE3A has its own node in this atlas, carrying a **human gain-of-function skeletal phenotype** (autosomal dominant hypertension with brachydactyly type E, short metacarpals, short stature; `maass2015`).
- **co-expressed in the relevant zone? relative abundance:** PDE3B chosen "based on gene expression data" (`kawabe2025`, verified in the abstract). PDE3A is recorded in the atlas at "moderate to negligible" levels in whole-bone/osteocyte transcriptomes. **Neither isoform has been localised by growth plate zone in any species.** So the relative abundance that the isoform assignment rests on is a bulk-transcriptome comparison, not a zonal measurement.
- **key experiment's perturbation and its SELECTIVITY:** **This is the failure.** The functional experiment is **cilostazol and milrinone** — verified from the `kawabe2025` abstract: *"The representative PDE3 inhibitors cilostazol and milrinone elevated cGMP levels…"*, and *"cilostazol stimulated the elongation of cultured bones and enlarged the body size of juvenile mice."* Both are **PDE3-family** inhibitors. Fold-selectivity for PDE3B over PDE3A: **effectively none, and this is a documented structural fact, not an oversight** — `rowley2024` (J Med Chem 2024) records that PDE3A and PDE3B share **48% overall identity and >95% active-site homology**, calls that homology *"a massive obstacle for obtaining selectivity at the active site"*, and states that **every FDA-approved PDE3 inhibitor is family-selective only**. Obtaining a PDE3B-selective compound required a DNA-encoded library screen and novel boronic-acid chemistry.
- **ligand/agonist selectivity:** As above — the agent used cannot discriminate the two isoforms *in principle*, not merely in practice.
- **double perturbation done? NEVER.** No *Pde3a;Pde3b* compound mutant in cartilage. No cartilage-specific *Pde3a* knockout at all (`g_para_002` search log: 3 hits, none skeletal-genetic).
- **VERDICT: AT_RISK** — and this is the highest-value finding of the pass.
- **What survives:** the **IMPC *Pde3b*-null increased tibial length**. That is a gene-selective genetic perturbation and it is the reason this is AT_RISK rather than SUPERSEDED. The genetic arm supports PDE3B; the pharmacological arm — which is the arm carrying the cGMP mechanism, the K⁺ channel/hyperpolarisation/TRPM7 chain, the bone elongation and the whole therapeutic-repositioning argument — supports **PDE3, not PDE3B**.
- **Why this is the same shape as CORR-001/003:** the mechanism was assigned in a system where the alternative was present, and the alternative here is not a bystander — PDE3A is the isoform with the *human* skeletal genetics, and the direction fits: PDE3A gain of function shortens metacarpals, so PDE3A inhibition lengthening bone is exactly what a PDE3-family inhibitor would be expected to do.
- **action:** → `paralog_risk`: *"The cGMP, K⁺-channel and bone-elongation results are cilostazol/milrinone (PDE3-family) effects; PDE3A shares >95% active-site homology, is not excluded by any compound used, and is the isoform carrying the human brachydactyly/short-stature genetics."* → gap `g_para_002` opened. Confidence held at **C** — the IMPC genetic result did not fail.

## pde3a
- **mechanism attributed to:** PDE3A as a cross-inhibition point between PTH1R/cAMP and NPR2/cGMP arms; human skeletal relevance via gain-of-function brachydactyly.
- **paralogs/isoforms in family:** PDE3B (above); more broadly PDE4/PDE7/PDE8 for cAMP.
- **co-expressed in the relevant zone? relative abundance:** Not localised by zone in any species — **and the node says exactly that.**
- **key experiment's perturbation and its SELECTIVITY:** `maass2015` human **gain-of-function mutations** — allele- and gene-selective, human. The chondrocyte assignment is explicitly labelled by the node as "a review-level synthesis, not a measurement" (`ursachi2026`).
- **ligand/agonist selectivity:** No pharmacology is used to support the claim, which is why this node escapes the problem that `pde3b` has.
- **double perturbation done?** Not required for the human genetic claim.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`, plus a cross-reference note: this node is the **named alternative** in `g_para_002`.

## pde5a
- **mechanism attributed to:** PDE5A as the dominant cGMP-hydrolysing activity of rat epiphyseal chondrocytes; and a **negative** functional result — raising bulk cGMP does not lengthen bone.
- **paralogs/isoforms in family:** PDE1, PDE2, PDE3, PDE6, PDE9, PDE10, PDE11 all hydrolyse cGMP; PDE11 is tadalafil's nearest off-target.
- **co-expressed in the relevant zone? relative abundance:** PDE5A transcript reported in human/mouse/chicken bulk chondrocyte profiling; no zonal map.
- **key experiment's perturbation and its SELECTIVITY:** tadalafil, which is >1000-fold selective over PDE1–PDE4 and PDE7–PDE10; its weakest margin is against PDE11. **Target engagement was independently verified** — tissue cGMP rose 52%, peak CNP-stimulated cGMP rose 37% — so the compound demonstrably hit a cGMP PDE in the tissue.
- **ligand/agonist selectivity:** n/a.
- **double perturbation done?** Not needed. The claim being defended is a **null result on longitudinal growth with confirmed target engagement**, which is the one situation where paralog cross-reactivity cannot manufacture a false positive — a *broader* inhibitor would only have made the negative result stronger.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. Recorded explicitly: this negative stands **against** the `pde3b`/`kawabe2025` positive, and the two are not reconciled. That tension is now sharper, not weaker, because the positive result's isoform assignment is the one in doubt.

## pde1c
- **mechanism attributed to:** **Nothing.** The node is an explicit negative: PDE1C is not reported in growth plate in any species.
- **paralogs/isoforms in family:** PDE1A, **PDE1B**.
- **co-expressed in the relevant zone? relative abundance:** The node **names PDE1B as the isoform actually reported** in human, mouse and chicken growth plate chondrocyte transcriptomes, and PDE1C as the one that is not.
- **key experiment's perturbation and its SELECTIVITY:** none claimed.
- **ligand/agonist selectivity:** n/a.
- **double perturbation done?** n/a.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. **This node is the template.** It is a coastline node that names the correct paralog against itself. Grade E is right and the naming is what makes it useful.

## pde9a
- **mechanism attributed to:** Nothing — retained as an explicit negative, with PDE6/9/11 reported absent from bone and cartilage.
- **paralogs/isoforms in family:** whole PDE superfamily.
- **VERDICT: CLEAN** — attribution withheld.
- **action:** → `paralog_audit: passed`.

---

## IGF1R / insulin receptor / hybrid receptors

## igf1_receptor
- **mechanism attributed to:** IGF1R as the chondrocyte receptor through which circulating and local IGF-1 act.
- **paralogs/isoforms in family:** **INSR** (INSR-A and INSR-B isoforms), and **INSR/IGF1R hybrid receptors**, plus IGF2R (clearance).
- **co-expressed in the relevant zone? relative abundance:** INSR is ubiquitous; **hybrid receptor abundance at the chondrocyte surface has never been quantified in any species**, which the node states. This is a genuine unmeasured quantity, not a rhetorical hedge.
- **key experiment's perturbation and its SELECTIVITY:** The node previously rested on `alarid1992` (insulin's cartilage effect in vivo is IGF-I-dependent) and `dauber2016` (human PAPP-A2). **This audit supplies the missing selective perturbation:** `wang2011` (JBMR, PMID 21312270) made **cartilage-specific *Igf1r* knockouts**, both embryonic (Col2-driven; disorganised columns, delayed ossification and vascular invasion, reduced proliferation, increased apoptosis, increased *Pthrp* transcription) and **tamoxifen-inducible postnatal** (growth retardation, disorganised plate, reduced proliferation, reduced Col2 and *Ihh*, increased PTHrP). That is gene-selective for IGF1R and does not touch INSR. The atlas had no cartilage IGF1R genetics before this.
- **ligand/agonist selectivity:** IGF1R binds IGF-1 with ~**100-fold** higher affinity than insulin (`alarid1992` framing, already in node) — a real fold-selectivity number, correctly recorded.
- **double perturbation done? NEVER** for cartilage — no chondrocyte *Insr;Igf1r* compound mutant, so the hybrid contribution remains unmeasured.
- **VERDICT: CLEAN**, with one clause carved out.
- **The carved-out clause:** the **IGF1R → mTORC1** link. The one cartilage experiment coupling this family to mTORC1 used **insulin**, not IGF-1 (`phornphutkul2008`). Checked in the graph: edge `igf1_receptor --hypothesized_link--> mtorc1_chondrocyte` is already **`speculative`**, which is the correct grade and means this was handled at authoring. No downgrade needed; no new risk.
- **action:** → `paralog_audit: passed`. → `wang2011` added to `key_refs` as the cartilage-selective IGF1R perturbation. → `g_para_003` opened on the hybrid-receptor fraction, which remains a genuine quantitative hole rather than an attribution error.

## insulin_receptor
- **mechanism attributed to:** INSR requirement for human growth, separable from IGF1R, via Donohue syndrome.
- **paralogs/isoforms in family:** IGF1R; INSR-A/INSR-B splice isoforms; hybrids.
- **co-expressed in the relevant zone? relative abundance:** unquantified by zone — **stated in the node**.
- **key experiment's perturbation and its SELECTIVITY:** biallelic human *INSR* loss of function — **gene-selective, human**, and the phenotype is not rescuable by hyperinsulinaemia, which is what makes it a receptor claim rather than a ligand claim.
- **ligand/agonist selectivity:** The node states outright that **"at the chondrocyte surface insulin and IGF signalling are not cleanly separable pharmacologically"** because of hybrids. Attribution correctly bounded.
- **double perturbation done?** No, and the node does not need it.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. Exemplary handling: the node names the hybrid problem *before* being asked.

---

## Collagen isoforms — II / IX / X / XI

## collagen_type_ii
- **mechanism attributed to:** collagen II as the fibril-forming backbone; MMP-13 cleavage in the lower hypertrophic zone.
- **paralogs/isoforms in family:** **IIA and IIB splice forms** (node distinguishes them, and assigns IIA to prechondrocytes/perichondrium, IIB to differentiated chondrocytes); collagens IX, XI in the same heterotypic fibril.
- **co-expressed in the relevant zone? relative abundance:** **Quantified**: ≤80% II, ≥10% IX, ≥10% XI by mass in young growth cartilage; ≥90% II, ~1% IX, ~3% XI in mature articular (`eyre2002`).
- **key experiment's perturbation and its SELECTIVITY:** human *COL2A1* allelic series (achondrogenesis II → hypochondrogenesis → SEDC → Stickler/Kniest) — gene-selective, human, graded.
- **ligand/agonist selectivity:** n/a.
- **double perturbation done?** n/a — but see the striking cross-gene fact the node already carries: **the α3(XI) chain *is* the COL2A1 gene product α1(II)B**, so "collagen II" and "collagen XI" are not genetically independent. The node states this rather than treating them as separate paralogs.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`.

## collagen_type_ix
- **mechanism attributed to:** fibril-surface organiser, not load-bearing element; required for matrilin-3 integration, not for fibril formation.
- **paralogs/isoforms in family:** COL9A1/A2/A3 chains (all three in one molecule); other FACIT collagens XII, XIV.
- **co-expressed in the relevant zone? relative abundance:** ≥10% of fibrillar collagen in young growth cartilage, ~1% in mature (`eyre2002`) — measured.
- **key experiment's perturbation and its SELECTIVITY:** *Col9a1*-null (`fssler1994`) — gene-selective; human COL9A1/2/3 MED — gene-selective, all three chains independently.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`.

## collagen_type_xi
- **mechanism attributed to:** collagen XI nucleates the fibril and sets its diameter.
- **paralogs/isoforms in family:** **collagen V** — and this is the interesting one. α1(V) and α1(XI) are close paralogs and interchangeable in the fibril.
- **co-expressed in the relevant zone? relative abundance: quantified, and the node leads with it.** In the *cho/cho* (*Col11a1*-null) mouse, **α1(V) substitutes for the missing α1(XI)** (`fernandes2007`) — the paralog does not merely co-exist, it physically takes the empty slot. And in mature human articular cartilage the isolated "collagen XI" fraction is **~1:1 α1(V):α1(XI)** (`eyre2002`), so what is called collagen XI in adult tissue is a **V/XI hybrid**.
- **key experiment's perturbation and its SELECTIVITY:** *Col11a1*-null, gene-selective; plus `blaschke2000` **reconstitution from purified components**, which is the strongest possible selectivity — the paralog is physically absent from the tube. Fold: fibril diameter control holds only while the II:XI molar ratio stays below **8:1**.
- **double perturbation done?** Not needed; reconstitution substitutes for it.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. **Second template node.** A paralog that literally substitutes into the mutant, quantified at ~1:1 in adult tissue, and stated in the summary. This is what a paralog-aware node looks like.

## collagen_type_x
- **Already adjudicated — CORR-002** (proliferative not hypertrophic zone compression). Re-read for paralog exposure: collagen X's nearest relative is collagen VIII (same short-chain family), which is not reported in growth plate. No paralog risk found.
- **VERDICT: CLEAN** (for the paralog question specifically; the zonal question was corrected separately).
- **action:** → `paralog_audit: passed`.

---

## SoxD/SoxE transcription factors — SOX5 / SOX6 / SOX9

## sox5_tf · sox6_tf
- **mechanism attributed to:** SOX5 and SOX6 jointly raise the efficiency of SOX9-driven matrix gene activation; **neither is individually essential**.
- **paralogs/isoforms in family:** each other (near-identical SoxD proteins); SOX13 is the third SoxD.
- **co-expressed in the relevant zone? relative abundance:** co-expressed with each other and SOX9 in all mouse cartilage zones (`smits2001`).
- **key experiment's perturbation and its SELECTIVITY:** single nulls (mild) versus **double null** — gene-selective at both levels.
- **double perturbation done? YES — `smits2001`**, and it is the *only* reason the requirement is visible: double-null fetuses die with generalised chondrodysplasia expressing essentially no cartilage matrix genes.
- **VERDICT: CLEAN** (both)
- **action:** → `paralog_audit: passed` on both. Both nodes already frame this as **gene dose, not gene identity** — the correct framing, and one the atlas applies consistently across SOX5/6, RUNX2/3, SMAD1/5 and LRP5/6.

## sox9_tf
- **mechanism attributed to:** master chondrogenic factor; condensation, differentiation, *Sox5*/*Sox6* expression, columnar proliferation, *Col10a1* activation with MEF2C, restraint of RUNX2 and β-catenin.
- **paralogs/isoforms in family:** **SOX8, SOX10** (SoxE group).
- **co-expressed in the relevant zone? relative abundance:** SOX8/SOX10 are not established growth plate chondrocyte factors; SOX9 protein is mapped to RZ/PZ/PHZ and upper HZ (`dy2012`).
- **key experiment's perturbation and its SELECTIVITY:** **human heterozygous *SOX9* haploinsufficiency alone is sufficient** (campomelic dysplasia, `foster1994`/`wagner1994`) — gene-selective, human, and dose-sensitive at 50%. Mouse: *Sox9*-null cells excluded from condensations in **chimaeras** (`bi1999`) — cell-autonomous, which no paralog in a neighbouring cell can rescue.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. The chimaera design is worth noting: it is the one experimental format that excludes paralog rescue *and* non-cell-autonomous compensation simultaneously.

---

## ADAMTS and TIMP families

## adamts4 · adamts5
- **mechanism attributed to:** ADAMTS5 as the dominant murine aggrecanase; ADAMTS4 dispensable in mouse; **both** contributing in human explants.
- **paralogs/isoforms in family:** each other; wider ADAMTS family.
- **co-expressed in the relevant zone? relative abundance:** zonal growth plate distribution not established for either — **stated in both nodes**.
- **key experiment's perturbation and its SELECTIVITY:** `glasson2005` catalytically-inactive *Adamts5* — gene- **and domain**-selective.
- **double perturbation done? YES — `majumdar2007`**, and the double result is the growth-plate-relevant one: *Adamts4/Adamts5* double nulls are **physiologically normal**, so neither aggrecanase is required for skeletal growth. The node then draws the right conclusion — that the mechanism of aggrecan removal from the hypertrophic zone **is not established by any obvious candidate** and is a real hole.
- **Species caveat handled:** both nodes state that human explants show both enzymes contributing, so the murine hierarchy does not transfer.
- **VERDICT: CLEAN** (both)
- **action:** → `paralog_audit: passed` on both. This pair is the cleanest in the audit: single knockouts, a double knockout, a catalytic-dead allele, and an explicit refusal to extend the mouse hierarchy to humans.

## timp_family
- **mechanism attributed to:** TIMP-3 as the **only** aggrecanase inhibitor; TIMP-1/2/4 weak or inactive.
- **paralogs/isoforms in family:** the four TIMPs — the node treats the family as the unit of analysis, correctly.
- **key experiment's perturbation and its SELECTIVITY:** `kashiwagi2001` — **sub-nanomolar Ki for the TIMP-3 N-terminal domain against ADAMTS4 and ADAMTS5**, with TIMP-1/-2/-4 weak or inactive (`hashimoto2001`). That is a **measured differential-inhibition constant across all four paralogs** — precisely the data type this audit asks for and rarely finds.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. The node also correctly notes that because aggrecanase activity is dispensable in mouse, TIMP-3's physiological growth plate role is unresolved — a conclusion, not a hedge.

---

## MMP family — MMP-9 / MMP-13 / MMP-14

## mmp13_protease
- **mechanism attributed to:** MMP-13 as **"the enzyme that cleaves the triple helix of collagen II in the lower growth plate"**, with the discriminating claim that **"unlike the Mmp9-null, these growth plate abnormalities persist into adult life"**.
- **paralogs/isoforms in family:** MMP-1, MMP-8 (other collagenases), **MMP-9** (gelatinase acting on the same substrates downstream), MMP-14.
- **co-expressed in the relevant zone? relative abundance:** **All of them, in the same zone, in human tissue.** `haeusler2005` finds MMP-1, -9, -10, -11 **and** -13 all immunopositive in human hypertrophic chondrocytes, with **MMP-14 the most prominent MMP in the human growth plate and present in all zones**. So in the human plate MMP-13 is one of at least five co-localised proteases and is *not* the most abundant.
- **key experiment's perturbation and its SELECTIVITY:** `inada2004` *Mmp13*-null — gene-selective.
- **double perturbation done? YES — and the atlas did not have it.** `stickens2004` (Development, PMID 15539485) made ***Mmp9*/*Mmp13* double nulls**: severely impaired endochondral bone, diminished ECM remodelling, prolonged chondrocyte survival, delayed vascular recruitment, defective trabecular bone and **drastically shortened bones**. The authors' conclusion is explicit: **"degradation of cartilage collagen and aggrecan is a coordinated process in which MMP13 works synergistically with MMP9."** The same paper confirms **collagen II and aggrecan as in vivo MMP-13 substrates**, so the substrate half of the node's claim is *strengthened*; it is the **exclusivity** ("*the* enzyme") that does not survive a synergy result.
- **A direct contradiction found, and it is not a paralog issue:** `stickens2004` reports that the *Mmp13*-null growth plate phenotype **"increased until about 5 weeks and completely resolved by 12 weeks of age."** The node states, from `inada2004`, that the abnormalities **persist into adult life** — and uses that persistence as the discriminator against the transient *Mmp9*-null. Two independently generated *Mmp13*-null lines, both 2004, opposite claims about persistence. Neither supersedes the other on the evidence available.
- **VERDICT: AT_RISK**
- **action:** → `paralog_risk`: *"Collagen II cleavage in the lower plate is attributed exclusively to MMP-13; MMP-9 acts synergistically on the same substrates (`stickens2004` double null), and in human tissue MMP-1/-9/-10/-11/-14 are co-localised in the same zone with MMP-14 the most prominent."* → `stickens2004` added to `key_refs`. → gap `g_para_004` opened (contradiction type) on the persistence conflict + the human isoform question. → contradiction logged in `contradictions.md` §1. Confidence held at **B**: the necessity result and the substrate identification both stand, and the second line *confirms* the phenotype, differing only on its duration.

## mmp9_protease
- **mechanism attributed to:** MMP-9 supplied by marrow-derived chondroclasts, acting at the last hypertrophic septum to release angiogenic activity; ~8-fold plate lengthening, transient.
- **paralogs/isoforms in family:** MMP-2 (the other gelatinase), MMP-13.
- **co-expressed in the relevant zone? relative abundance:** MMP-9 immunopositive in human hypertrophic chondrocytes, osteoblasts and osteoclasts (`haeusler2005`), alongside the other MMPs above.
- **key experiment's perturbation and its SELECTIVITY:** `vu1998` *Mmp9*-null — gene-selective, **plus rescue by wild-type bone marrow transplantation**, which independently establishes the cellular source. A cell-source rescue is a much stronger control than a paralog exclusion and is not available to most nodes here.
- **double perturbation done? YES — `stickens2004`**, same double as above. The synergy result is consistent with, and does not undermine, the MMP-9 single-null attribution.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. → note added that the *Mmp9;Mmp13* double is far more severe than either single, so the two proteases are not independent contributors to the same process.

## mmp14_mt1mmp
- **mechanism attributed to:** membrane-tethered pericellular proteolysis as the non-redundant activity; *Mmp14*-null dwarfism.
- **paralogs/isoforms in family:** **MMP-15 (MT2-MMP), MMP-16 (MT3-MMP), MMP-24** — the other membrane-type MMPs.
- **co-expressed in the relevant zone? relative abundance:** MMP-14 is the **most prominent** MMP in human growth plate and present in **all zones** (`haeusler2005`) — a rare instance where the atlas has a human relative-abundance statement for the protein it is attributing to.
- **key experiment's perturbation and its SELECTIVITY:** `holmbeck1999` global *Mmp14*-null, gene-selective; and critically `xia2023` shows the **chondrocyte-specific** deletion does **not** reproduce the global phenotype, which the node uses to bound the claim rather than to inflate it.
- **double perturbation done?** No MT-MMP compound mutant in cartilage. **Not required**: the claim defended is a necessity result from a selective single-gene deletion, and the node explicitly declines to attribute the whole phenotype to chondrocytes.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`.

---

## PTH receptor family

## pth1r_receptor
- **mechanism attributed to:** PTH1R in late proliferative/prehypertrophic chondrocytes maintaining proliferation and delaying hypertrophy.
- **paralogs/isoforms in family:** **PTH2R**, and PTH3R in non-mammals.
- **co-expressed in the relevant zone? relative abundance:** PTH2R's ligand is **TIP39**, not PTHrP or PTH; PTH2R is not an established growth plate receptor. The ligand specificity does the discriminating work.
- **key experiment's perturbation and its SELECTIVITY:** unusually strong and multi-directional. `schipani1997` **targeted constitutively active H223R receptor rescues the *Pthrp*-null plate** — an epistasis result that places the receptor downstream of the ligand and cannot be produced by a paralog. `chung1998` **wild-type/*Pth1r*-null chimaeras** — cell-autonomous, paralog-proof in the same sense as `bi1999`. Human both directions: activating H223R (Jansen) and functional loss (Blomstrand).
- **ligand/agonist selectivity:** PTHrP and PTH both act at PTH1R; the node does not attempt to separate them at the receptor, and `lanske1999` records that *Pth1r* and *Pthlh* ablation give **different** phenotypes, i.e. PTHrP-independent receptor functions — an explicit refusal to collapse ligand and receptor.
- **double perturbation done?** Not required.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. Also verified: the node's `n=1` caveat on Blomstrand (heterozygous splice mutation with an unexpressed paternal allele — functionally but not genotypically biallelic) is a genuine and correctly recorded limitation.

---

## BMP ligands and antagonists

## bmp2_ligand
- **mechanism attributed to:** BMP2 as the non-redundant BMP within cartilage.
- **paralogs/isoforms in family:** **BMP4** (closest), BMP5/6/7/8.
- **co-expressed in the relevant zone? relative abundance:** BMP2 in perichondrium and PHZ/HZ; BMP4 co-expressed; BMP6 also in HZ per the `bmp6_ligand` node. Relative abundance not quantified.
- **key experiment's perturbation and its SELECTIVITY:** **`shu2011` deleted *Bmp2* and *Bmp4* separately in the same cartilage-specific system** and found the *Bmp2* deletion much more severe. That is a **direct paralog comparison in matched conditions**, which is the second-best available design after a double.
- **double perturbation done?** Yes **in limb mesenchyme** (`bandyopadhyay2006`: *Bmp2;Bmp4* double blocks skeletogenesis; *Bmp7* dispensable), **not** in cartilage. The node states that redundancy is compartment-specific — the right conclusion from having both datasets.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. Note recorded that the cartilage-specific *Bmp2;Bmp4* double has not been made, but the matched single comparison already discriminates.

## bmp6_ligand · bmp7_ligand
- **mechanism attributed to:** BMP6 — impaired hypertrophic zone function in the germline null, framed as *inventory* not as a control point. BMP7 — **dispensable** for limb skeletogenesis; role is articular, not physeal.
- **paralogs/isoforms in family:** BMP2/4/5/7 (BMP6's closest is BMP5/7).
- **key experiment's perturbation and its SELECTIVITY:** germline nulls, gene-selective. `bandyopadhyay2006` tested *Bmp7* removal **on top of** *Bmp2/Bmp4* loss and found no additional limb phenotype — a genuine triple-perturbation negative.
- **double perturbation done?** For BMP7, yes (above). For BMP6, no.
- **VERDICT: CLEAN** (both) — attribution deliberately withheld in both nodes. `bmp6_ligand` additionally flags an **iron-status confounder** (BMP6 is the hepcidin ligand) that the skeletal literature has not controlled, which is the right kind of caveat even though it is not a paralog one.
- **action:** → `paralog_audit: passed` on both.

## noggin_antagonist · chordin_antagonist
- **mechanism attributed to:** Noggin as the dominant BMP antagonist; joint fusion phenotypes from BMP dose.
- **paralogs/isoforms in family:** each other, plus gremlin, follistatin, twisted gastrulation.
- **key experiment's perturbation and its SELECTIVITY:** `brunet1998` *Nog*-null and `gong1999` human *NOG* haploinsufficiency — gene-selective, both species.
- **double perturbation done? YES — `stottmann2001`**: single nulls have distinct territories, the **double loses structures neither single loses**.
- **ligand/agonist selectivity — the one real exposure, and the node names it:** *"Noggin is widely used experimentally as the BMP-off reagent in growth plate explants, so a large fraction of 'BMP is required for X' claims in this subsystem are Noggin-inference rather than receptor genetics."* Noggin binds BMP2/4/7 and GDF5 without discriminating them, so every downstream explant claim inherits that non-selectivity.
- **VERDICT: CLEAN** (both)
- **action:** → `paralog_audit: passed` on both. The Noggin-as-reagent caveat is flagged as a **standing methodological risk** for any future node that cites a Noggin explant experiment, and is recorded in `g_para_009`.

---

## SMAD family

## smad1_5_8
- **mechanism attributed to:** combined SMAD1/5 dose, not any single paralogue, carries BMP output; pSMAD1/5/8 activity peaks in PZ/PHZ.
- **paralogs/isoforms in family:** SMAD1, SMAD5, SMAD9(SMAD8) — the node is *named* for the group, which is itself the correct framing.
- **co-expressed in the relevant zone? relative abundance: measured as activity, not abundance** — pSMAD1/5/8 immunostaining highest in PZ/PHZ and **lower in HZ despite *Bmp2*/*Bmp6* mRNA being highest there** (`garrison2017`). That mRNA/activity inversion is exactly the kind of discrepancy that produced CORR-003, and here the node records the inversion and attributes it to hypertrophic-zone SMAD7 rather than smoothing it.
- **key experiment's perturbation and its SELECTIVITY:** `retting2009` — single *Smad1*, single *Smad5* and *Smad8*-null all near-normal; **chondrocyte-restricted *Smad1*;*Smad5* double** gives severe chondrodysplasia.
- **double perturbation done? YES.**
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`.

## smad2_3
- **mechanism attributed to:** SMAD3 output as a **brake** on the hypertrophy transition — opposite in sign to the BMP-SMAD arm.
- **paralogs/isoforms in family:** SMAD2 (co-paralog), SMAD4 (co-SMAD), SMAD7 (inhibitory).
- **key experiment's perturbation and its SELECTIVITY:** `yang2001` *Smad3*-null, gene-selective; corroborated by `serra1997` dominant-negative TGFBR2 — a **different level of the pathway**, same direction. Independent-level corroboration is a strong substitute for a paralog double.
- **double perturbation done?** No *Smad2;Smad3* cartilage double. Not needed for a single-gene necessity claim.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. The node's framing — that the BMP/TGF-β sign split means *"'TGF-β superfamily signalling' is not a usable unit of analysis in this atlas"* — is the correct generalisation of the paralog problem to a whole superfamily.

---

## GLI family

## gli1_tf · gli2_tf · gli3_repressor
- **mechanism attributed to:** GLI3R as the dominant Ihh transducer; GLI1 as a pathway *reporter* rather than an effector; GLI2 activator role largely dispensable.
- **paralogs/isoforms in family:** each other — and this family is the hardest case in principle, because all three read the same DNA motif.
- **co-expressed in the relevant zone? relative abundance:** GLI3R concentration across zones has **never been measured in any species** — `gli3_repressor` states this outright as the node's central limitation.
- **key experiment's perturbation and its SELECTIVITY:** **genetic epistasis, which is the correct tool here.** `hilton2005`/`koziel2005`: deleting *Gli3* in an *Ihh*-null background **rescues most of the cartilage phenotype**. That result discriminates *between the paralogs directly* — it shows the pathway output is derepression (GLI3R relief) rather than activator gain (GLI1/GLI2), and no amount of GLI1/GLI2 co-expression can explain it away. `hilton2005` further records that osteoblast and vascular defects **persist**, so additional Ihh effectors are required — a bounded claim.
- **double perturbation done?** Yes in effect: *Ihh;Gli3* compound is the discriminating double, and it was the one that mattered.
- **VERDICT: CLEAN** (all three)
- **action:** → `paralog_audit: passed` on all three. `gli2_tf`'s note that human *GLI2* loss confounds a growth plate readout with GH deficiency (pituitary/midline defects) is a correct refusal to use the human phenotype as a chondrocyte test.

---

## Hedgehog transducers

## smoothened · patched1 · sufu_protein
- **mechanism attributed to:** SMO as transducer (cell-autonomous proliferation requirement); PTCH1 as receptor and pathway readout; SUFU as brake.
- **paralogs/isoforms in family:** PTCH2 for PTCH1; no close SMO or SUFU paralog.
- **key experiment's perturbation and its SELECTIVITY:** `long2001` chondrocyte-specific *Smo* deletion (cell-autonomous), `xiu2022` chondrocyte *Sufu* deletion — both gene-selective conditionals.
- **VERDICT: CLEAN** (all three)
- **action:** → `paralog_audit: passed` on all three. Recorded: `smoothened` carries an **unrelated** open contradiction (`wang2022`, Hedgehog-driven cartilage-to-bone transition proceeding **independently of** Smoothened, unreconciled with the conditional-knockout literature, `c_l3core_smo`). That is a pathway-topology conflict, not a paralog conflict, and is out of scope here.

---

## Thyroid hormone receptors and deiodinases

## thra_receptor
- **mechanism attributed to:** TRα as the isoform whose **human** loss produces the skeletal phenotype (RTHα: growth retardation, delayed bone age, disharmonious short stature).
- **paralogs/isoforms in family:** **THRB (TRβ1, TRβ2)**; plus THRA's own two isoforms TRα1 (T3-binding) and **TRα2 (non-T3-binding, dominant-negative-like)**.
- **co-expressed in the relevant zone? relative abundance:** **Both receptors are in the same cells.** `robson2000` places TRα1, TRα2 **and TRβ1** protein all in reserve and proliferating rat chondrocytes and all absent from hypertrophic cells. There is **no relative abundance measurement** distinguishing them, and no human growth plate localisation of either.
- **key experiment's perturbation and its SELECTIVITY:** human heterozygous dominant-negative *THRA* variants (`jorge2025`) — gene-selective. But a **dominant-negative** allele acts on shared response elements and shared RXR heterodimer partners, so it is not cleanly isoform-restricted at the level of pathway output.
- **ligand/agonist selectivity:** T3 binds TRα1 and TRβ1 with **comparable affinity** — the ligand cannot discriminate them at all. This is the (d) failure in its purest form: **the hormone is the same molecule for both receptors.**
- **double perturbation done? YES, but not in cartilage, and it undercuts the isoform assignment.** `gthe1999` (Genes Dev, PMID 10346821): TRα1⁻/⁻β⁻/⁻ mice show **retarded growth and bone maturation not found in either single receptor-deficient mouse**, and the authors state that **"deletion of TRα1 or TRβ individually reveals only a small proportion of the phenotypes that arise in hypothyroidism"**, concluding that **TRα1 and TRβ cooperate with or substitute for each other on common pathways**. A cartilage-restricted double has never been made.
- **VERDICT: AT_RISK**
- **action:** → `paralog_risk`: *"T3 binds TRα and TRβ with comparable affinity and both are protein-detected in the same RZ/PZ chondrocytes (`robson2000`); the double null shows single deletions capture only a small fraction of the T3 phenotype (`gthe1999`), so neither single-gene phenotype assigns the chondrocyte T3 response to an isoform."* → `gthe1999` added to `key_refs`. → gap `g_para_005` opened. Confidence held at **A** — the human RTHα phenotype is real, replicated and directly observed; what is at risk is the *cellular isoform assignment*, not the human requirement.

## thrb_receptor
- **mechanism attributed to:** TRβ as the isoform required for **all** T3 responses in chondrocytes, from `rabier2006`.
- **paralogs/isoforms in family:** THRA (TRα1/TRα2).
- **co-expressed in the relevant zone? relative abundance:** as above — both present, neither quantified against the other.
- **key experiment's perturbation and its SELECTIVITY:** `rabier2006`, **primary neonatal rib chondrocytes from germline TRα- and TRβ-deficient mice**. Gene-selective at the level of the allele, but two independent confounds: (i) **germline** nulls permit developmental compensation by the remaining paralogue, which `gthe1999` demonstrates is exactly what happens in this family; (ii) **rib** chondrocytes, not long-bone growth plate.
- **ligand/agonist selectivity:** T3 — non-discriminating between the paralogs.
- **double perturbation done? Yes (`gthe1999`), and it argues against the single-null inference.** The node's own logged contradiction — mouse rib chondrocytes say TRβ, human genetics says THRA — is **partly explained** by the double: if the isoforms substitute for each other, then which one a *germline* single null implicates depends on compensation, species and tissue, not on which one normally carries the signal.
- **VERDICT: AT_RISK**
- **action:** → `paralog_risk`: *"'All T3 responses require TRβ' rests on a germline TRβ-null rib chondrocyte culture in which TRα is present and can have compensated; `gthe1999` shows the two isoforms substitute for each other, so a germline single null does not assign the response."* → `gthe1999` added to `key_refs`. → `g_para_005` covers both nodes. → the existing `contradictions.md` entry updated with `gthe1999` as partial mechanistic explanation. Confidence held at **D** (already the lowest working grade; the contradiction was already logged).

## dio2_deiodinase
- **mechanism attributed to:** DIO2 as the enzyme generating local intracellular T3 in the growth plate, letting a chondrocyte set its own T3 exposure independently of serum T4.
- **paralogs/isoforms in family:** **DIO1** — the *other* activating (outer-ring) deiodinase, entirely unmentioned in the node — and DIO3, the inactivating one.
- **co-expressed in the relevant zone? relative abundance: neither enzyme measured by zone in any species.** DIO1 in growth plate: **no primary study exists** (`g_para_006` search log — tight query, 6 hits, all screened, none reporting DIO1).
- **key experiment's perturbation and its SELECTIVITY: ABSENT — and worse than absent.** Before this audit the node's **only** `key_ref` was `robson2000`, which is a **thyroid hormone receptor** localisation paper, not a deiodinase paper. The node was carrying a DIO2 attribution with **zero primary DIO2 evidence attached**, while itself stating that the quantitative claim "is widely repeated but has not been measured with zonal resolution in any species". The self-flag was correct; the evidence base was thinner than the self-flag implied.
- **ligand/agonist selectivity:** n/a (no pharmacology used).
- **double perturbation done? NEVER** — no *Dio1;Dio2* compound mutant with a growth plate readout.
- **VERDICT: AT_RISK**
- **What this audit supplies:** `dentice2005` (PMID 15965468) — the Hedgehog-inducible ubiquitin ligase subunit **WSB-1 targets DIO2 for degradation in the developing growth plate**, modulating local thyroid hormone activation and PTHrP secretion. That is genuine primary evidence that **DIO2 specifically** is locally regulated in this tissue, and it ties the deiodinase to the Ihh/PTHrP loop. `shen2004` (PMID 15025570) adds differential DIO2 expression in chicken growth plates. Both are now attached. The node is materially better evidenced than it was — but DIO1 is still not excluded, and neither reference measures the **fraction** of growth plate T3 that is locally generated, which is the specific claim flagged as unmeasured.
- **action:** → `paralog_risk`: *"Local T3 generation is attributed to DIO2 with DIO1 — the other activating deiodinase — never measured or excluded in growth plate in any species."* → `dentice2005` and `shen2004` added to `key_refs`. → gap `g_para_006` opened. Confidence held at **D**.

## dio3_deiodinase
- **mechanism attributed to:** DIO3 as the inactivating deiodinase gating early T3 exposure — a developmental timing claim.
- **paralogs/isoforms in family:** DIO1, DIO2.
- **co-expressed in the relevant zone? relative abundance:** zonal expression in postnatal human growth plate **not reported — stated in the node**.
- **key experiment's perturbation and its SELECTIVITY:** the node's claim rests on DIO3's distinctive **inner-ring** specificity (T4→rT3, T3→3,3'-T2), which no other deiodinase performs — an enzymological rather than genetic discriminator, and a valid one.
- **VERDICT: CLEAN** — attribution correctly withheld for the growth plate specifics.
- **action:** → `paralog_audit: passed`.

---

## Estrogen receptors — ERα / ERβ / GPER1

## estrogen_receptor_alpha
- **mechanism attributed to:** ERα as the receptor carrying estrogen's growth-terminating action; AF-1 opposing closure while non-AF-1 functions drive it.
- **paralogs/isoforms in family:** **ERβ (ESR2)** and **GPER1** — plus ERα's own AF-1/AF-2 domains, which the node already dissociates.
- **co-expressed in the relevant zone? relative abundance:** ERβ **is** expressed in growth plate cartilage and **can heterodimerise with ERα**, generally damping ERα-driven transcription — so the paralog is not just co-present, it is a physical binding partner of the attributed receptor. Relative abundance by zone in human: unquantified.
- **key experiment's perturbation and its SELECTIVITY:** `brjesson2012` ERα-null and ERαAF-1-null — **gene- and domain-selective**. Human homozygous *ESR1* disruption (`smith1994`, 204 cm, incomplete epiphyseal closure, elevated estradiol, normal testosterone) — gene-selective, human, and with the ligand demonstrably present, which excludes a ligand-availability explanation.
- **ligand/agonist selectivity:** 17β-estradiol is **non-selective** across ERα, ERβ and GPER1 — so any estradiol-based experiment would be uninterpretable here. **The claim does not rest on one.** Both load-bearing experiments are receptor-genetic.
- **double perturbation done? YES — and this audit found it.** `vidal2000` (PNAS, PMID 10805804) compared **ERα-KO (ERKO), ERβ-KO (BERKO) and the double ERα/β-KO (DERKO)** head to head in male mice: **ERKO and DERKO, but not BERKO, showed decreased longitudinal and radial skeletal growth** with decreased serum IGF-1. The double adds **nothing** over ERα alone, and ERβ removal alone does **nothing**. This is the cleanest possible outcome for a paralog audit: the alternative was removed, singly and in combination, and it is not carrying the effect.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. → `vidal2000` added to `key_refs` as the double-perturbation confirmation. Scope noted honestly: `vidal2000` is **male mice and skeletal growth**, `brjesson2012` is **female mice and closure** — the double perturbation confirms the ERα assignment for the *growth* arm; the *closure* arm has ERα and human genetics but no published DERKO closure comparison.

## estrogen_receptor_beta
- **mechanism attributed to:** ERβ as **secondary**; the node's operative claim is a **negative** — that estrogen's growth-terminating action should be attributed to ERα and that saying "estrogen receptors" generically overstates ERβ.
- **paralogs/isoforms in family:** ERα, GPER1.
- **co-expressed in the relevant zone? relative abundance:** expressed in growth plate cartilage; heterodimerises with ERα; not quantified against it.
- **key experiment's perturbation and its SELECTIVITY:** *Esr2*-null, gene-selective — **essentially normal longitudinal bone growth**, now directly corroborated by `vidal2000`'s BERKO arm.
- **ligand/agonist selectivity:** the node correctly notes that the rat costochondral work showing E2 responses requiring **both** receptors used 17β-estradiol, a non-selective ligand — and treats that as evidence for membrane-initiated signalling rather than for a nuclear closure role.
- **double perturbation done? YES — `vidal2000` DERKO**, which shows removing ERβ **on top of** ERα adds nothing.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. → `vidal2000` added. The node's negative claim is now backed by the single **and** the double knockout, which is a real evidence improvement on a grade-D node. **Confidence not raised** — the node remains human-evidence-absent, and this audit does not upgrade grades.

## gper1_receptor
- **mechanism attributed to:** GPER1 on the **ascending, growth-promoting** limb — positive regulation of chondrocyte proliferation in pubertal female mice, relayed through PTHrP/Ihh.
- **paralogs/isoforms in family:** ERα, ERβ (unrelated by sequence — GPER1 is a 7TM GPCR — but they share the ligand, which is what matters).
- **co-expressed in the relevant zone? relative abundance:** GPER-1 **highly expressed in growth plates at 4 and 8 weeks with a gradual decline through 12–16 weeks** (`chou2021`) — an age-resolved expression profile, which most nodes lack.
- **key experiment's perturbation and its SELECTIVITY: verified from the primary and it is genetic.** `chou2021` generated **chondrocyte-specific GPER-1 knockout mice** (80% expression reduction in growth plate chondrocytes), giving decreased crown–rump length, decreased tibial and femoral length, reduced proliferative-zone cell number and thickness, and reduced PCNA/Ki67 indices. Confirmed independently with a **GPER-1 antagonist in cultured epiphyseal cartilage**. So the attribution is **not** an estradiol-ligand inference — it is a conditional knockout plus a selective antagonist.
- **ligand/agonist selectivity:** not load-bearing, because the perturbation is on the receptor.
- **double perturbation done? NEVER** — and the node **says so precisely**: the two-receptor explanation of estrogen's biphasic dose effect *"has not been tested by manipulating GPER1 and ERalpha in the same animal across a dose range"*. That is the correct discriminating experiment, correctly named, before this audit asked for it.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. → `chou2021` upgraded in `key_refs` with the knockout design and the 80% figure recorded.

## androgen_receptor
- **mechanism attributed to:** **explicitly withheld.** AR is present in growth plate but not demonstrated to be required; androgen's growth effect runs predominantly through **aromatisation to estradiol**.
- **paralogs/isoforms in family:** AR is the relevant receptor; the cross-reactivity is at the **ligand** level — testosterone is a substrate for aromatase and therefore an indirect estrogen agonist.
- **key experiment's perturbation and its SELECTIVITY:** `chagin2009` — **neither AR agonists nor antagonists changed growth** in fetal rat metatarsal culture, a system that reads longitudinal growth directly. A pharmacological null with selective agents at the receptor.
- **ligand/agonist selectivity — this is the exemplary part:** human **complete androgen insensitivity syndrome** (non-functional AR, 46,XY) resolves the ligand cross-reactivity in humans: affected individuals are taller than average females with growth and fusion tracking **aromatised estrogen exposure**, not absent androgen signalling. An experiment of nature that separates a hormone from its metabolite.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. **Third template node** — the effect is actively *moved off* the molecule the node is about, on human evidence.

## aromatase_cyp19a1
- **mechanism attributed to:** aromatase as the committed, rate-limiting step making estrogen locally producible.
- **paralogs/isoforms in family:** single gene, tissue-specific promoters rather than paralogs.
- **key experiment's perturbation and its SELECTIVITY:** human *CYP19A1* deficiency (continued growth, unfused epiphyses) — gene-selective, human; plus aromatase inhibitors used clinically, which are highly enzyme-selective.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`.

---

## IGF bioavailability layer — IGFBP1-6, PAPP-A/PAPP-A2, STC2

## igfbp3
- **mechanism attributed to:** IGFBP-3 as the principal ternary-complex partner and main PAPP-A2 substrate.
- **paralogs/isoforms in family:** IGFBP-1 through -6.
- **co-expressed in the relevant zone? relative abundance:** carries **75–90% of circulating IGF-1** — a real relative-abundance figure against its own paralogs. Growth plate zonal localisation not reported (stated).
- **key experiment's perturbation and its SELECTIVITY:** human *PAPPA2* deficiency (`dauber2016`) with **size-exclusion chromatography confirming IGF-1 retention in ternary complex**, and IGFBP-3 measured at 4403–5912 µg/L against a Tanner I reference of 2206–4200. A quantitative, paralog-resolved biochemical readout — IGFBP-3 **and** IGFBP-5 were measured separately in the same patients.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`.

## igfbp5
- **mechanism attributed to:** matrix-immobilised IGF reservoir; PAPP-A2 substrate.
- **paralogs/isoforms in family:** IGFBP-1..6; IGFBP-3 is the co-ternary-complex former.
- **co-expressed in the relevant zone? relative abundance:** most abundant IGFBP **in bone matrix**; measured at 645–997 µg/L vs 211–707 reference in *PAPPA2* deficiency — again distinguished from IGFBP-3 in the same assay.
- **key experiment's perturbation and its SELECTIVITY:** as above, human, paralog-resolved.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`.

## igfbp4
- **mechanism attributed to:** pure inhibitor; the **strictly IGF-dependent** substrate of PAPP-A.
- **paralogs/isoforms in family:** IGFBP-1..6.
- **key experiment's perturbation and its SELECTIVITY:** `kobber2022` **cryo-EM of the 2:2 PAPP-A·STC2 complex** — structural, showing STC2 excludes **IGFBP-4 specifically** from binding while the catalytic site stays accessible. Substrate specificity established at atomic resolution is about as paralog-selective as evidence gets.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`.

## igfbp1 · igfbp2 · igfbp6
- **mechanism attributed to:** in every case **explicitly withheld for the growth plate**. IGFBP-1: "no study has measured IGFBP-1 in growth plate interstitium or shown a chondrocyte-level effect in any species." IGFBP-2: "specific contribution to growth plate IGF availability has not been isolated experimentally in any species." IGFBP-6: "no growth plate localisation, no human mutation phenotype and no chondrocyte functional data exist."
- **paralog handling:** each node distinguishes itself from its five paralogs by a **measured biochemical property** — IGFBP-1 by insulin-suppressed hepatic transcription and non-participation in the ternary complex; IGFBP-2 by heparin-binding/RGD and slow PAPP-A cleavage; IGFBP-6 by a **20–100-fold preference for IGF-2 over IGF-1**, with the node then drawing the correct species inference (IGF-2 is quantitatively dominant in adult human serum but not mouse, so rodent work will underestimate IGFBP-6's human relevance).
- **VERDICT: CLEAN** (all three)
- **action:** → `paralog_audit: passed` on all three.

## pappa_protease · pappa2_protease
- **mechanism attributed to:** PAPP-A as a local paracrine amplifier via IGFBP-4; PAPP-A2 as the IGFBP-3/-5 protease setting human stature.
- **paralogs/isoforms in family:** each other (the two pappalysins).
- **co-expressed in the relevant zone? relative abundance:** neither localised in human physeal tissue — stated in both nodes.
- **key experiment's perturbation and its SELECTIVITY:** **substrate specificity separates them cleanly and it is measured**: PAPP-A cleaves IGFBP-4 strictly IGF-dependently (and -2/-5 slowly); PAPP-A2 cleaves IGFBP-3 and -5. `dauber2016` human homozygous *PAPPA2* mutations — gene-selective, human. `nimptsch2024` provides the discriminating population datum: **PAPP-A2 and STC2, but not PAPP-A, associate with circulating total IGF-1** — the paralogs behave differently in the same human cohort.
- **VERDICT: CLEAN** (both)
- **action:** → `paralog_audit: passed` on both. The asymmetry the `pappa_protease` node flags — no human *PAPPA* loss-of-function short-stature syndrome despite a clear *PAPPA2* one — is honestly recorded rather than glossed.

## stanniocalcin2
- **mechanism attributed to:** STC2 as endogenous inhibitor of **both** pappalysins.
- **paralogs/isoforms in family:** **STC1**, which the node names as also inhibiting PAPP-A rather than claiming STC2 exclusivity.
- **key experiment's perturbation and its SELECTIVITY:** cryo-EM structure plus human height-association genetics plus a human biomarker association — three independent evidence types pointing the same way.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`.

---

## RUNX, LRP, PIEZO, cilium and remaining families

## runx2_tf · runx3_tf
- **mechanism attributed to:** licensing of chondrocyte hypertrophy by **combined RUNX dose**.
- **co-expressed in the relevant zone? relative abundance:** both in PHZ/HZ; RUNX3 protein IHC-detected in embryos (`soung2007`).
- **key experiment's perturbation and its SELECTIVITY:** `yoshida2004` — *Runx2*-null still completes maturation; **the *Runx2;Runx3* double completely lacks it**, and **limb length falls in proportion to combined gene dose**. A dose–response across two paralogs is the strongest form of this evidence.
- **double perturbation done? YES.**
- **VERDICT: CLEAN** (both)
- **action:** → `paralog_audit: passed` on both. Human *RUNX2* haploinsufficiency (cleidocranial dysplasia) supplies the gene-selective human arm for `runx2_tf`; `runx3_tf` correctly states that its human contribution is **unknown**.

## lrp5_coreceptor · lrp6_coreceptor
- **mechanism attributed to:** summed LRP5+LRP6 dose, with LRP6 dominant in the mouse embryo.
- **key experiment's perturbation and its SELECTIVITY:** `joeng2011` — *Lrp6* loss more severe than *Lrp5*; **reducing *Lrp5* dose on an *Lrp6* mutant background worsens it further**. Compound allelic series, i.e. the double.
- **double perturbation done? YES.**
- **VERDICT: CLEAN** (both)
- **action:** → `paralog_audit: passed` on both. `lrp5_coreceptor` additionally carries the right **negative**: both human LRP5 phenotypes are bone-mass-dominated, not stature-dominated, so the human readout is osteoblastic and not clearly physeal — an explicit refusal to import a bone claim into the growth plate.

## piezo1_channel · piezo2_channel
- **mechanism attributed to:** PIEZO1 as the mechanosensitive channel with in-plate loss-of-function evidence; PIEZO2 as **not** a demonstrated growth plate mechanotransducer.
- **paralogs/isoforms in family:** each other; TRPV4 as a functional (not sequence) alternative.
- **key experiment's perturbation and its SELECTIVITY:** `brylka2024` deleted ***Piezo1* and *Piezo2* in the same study, in the same Col2a1-Cre system** — *Piezo1* deletion abolished trabecular bone under the plate and caused peri-physeal rib fractures; *Piezo2* deletion produced **no** endochondral phenotype. A matched head-to-head paralog comparison.
- **double perturbation done?** Not needed — the paralog single null is phenotypically silent in this readout.
- **VERDICT: CLEAN** (both)
- **action:** → `paralog_audit: passed` on both. `piezo2_channel` is an unusually good negative node: it states that PIEZO2 "is repeatedly listed as a growth plate mechanotransducer but the supporting experiments were done elsewhere", and relocates the best-characterised PIEZO2 mechanism to **DRG neurons** — the correct disposition for a molecule attributed to the wrong cell type.

## trpv4_channel
- **mechanism attributed to:** TRPV4 activity level setting growth plate output; human dysplasia series.
- **paralogs/isoforms in family:** TRPV1–TRPV6; PIEZO1 as functional alternative.
- **key experiment's perturbation and its SELECTIVITY:** human *TRPV4* gain- **and** loss-of-function alleles (non-monotonic dose-response) — gene-selective, human, both directions; plus `nevarez2026` small-molecule TRPV4 inhibition **rescuing** the mutant mouse, which is a selectivity-dependent result but one operating on a demonstrably TRPV4-driven phenotype.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. The node's own limitation — that the direct mechanotransduction experiments are **prenatal or articular**, and no defined mechanical stimulus has been applied to a postnatal growth plate with a TRPV4-dependent growth-rate readout — is a scope limit, not a paralog one.

## ift80_protein · ift88_protein · kif3a_protein
- **mechanism attributed to:** cilium-dependent control of Hedgehog *placement* (KIF3A), Hedgehog/WNT balance (IFT80), and Ihh-dependent proximodistal growth (IFT88).
- **paralogs/isoforms in family:** functionally overlapping IFT-B subunits and kinesin-II subunits.
- **key experiment's perturbation and its SELECTIVITY:** all three are **conditional, tissue-restricted deletions** (`yuan2015` inducible Col2a1-CreER; `haycraft2007` mesenchyme **versus ectoderm**, which localises the requirement to a lineage; `koyama2007` cartilage-restricted). `haycraft2007`'s mesenchyme-versus-ectoderm contrast is a genuine specificity control.
- **Non-redundancy demonstrated rather than assumed:** both `haycraft2007` and `koyama2007` report phenotypes that **Ihh deletion does not reproduce** (ectopic perichondrium-derived chondrocyte-like domains; spatially spread perichondrial Hedgehog readouts with excessive intramembranous ossification). Cilium loss is shown *not* to be equivalent to Hedgehog loss — an explicit test of the obvious alternative explanation.
- **VERDICT: CLEAN** (all three)
- **action:** → `paralog_audit: passed` on all three. `ift80_protein` carries human *IFT80* Jeune genetics, making it the best-anchored of the three.

## tnap_alpl · phospho1_enzyme
- **mechanism attributed to:** TNAP destroys **extravesicular** PPi; PHOSPHO1 supplies **intravesicular** Pi. Two enzymes, two compartments, one process.
- **paralogs/isoforms in family:** TNAP's paralogs are the intestinal/placental/germ-cell alkaline phosphatases (not bone-expressed); PHOSPHO1's is PHOSPHO2.
- **key experiment's perturbation and its SELECTIVITY:** `anderson2004` high-resolution TEM in *Alpl*⁻/⁻ places the defect **precisely**: crystals initiate normally **inside** matrix vesicles and fail to propagate **beyond** the membrane. That is compartment-level resolution of an enzyme's role. `staines2021` supplies a real selectivity number the other direction: proton pump inhibitors inhibit **PHOSPHO1 with IC50 0.73–19.27 µM without inhibiting TNAP** — a measured cross-enzyme selectivity margin.
- **double perturbation done? YES — `yadav2011`**: *Phospho1/Alpl* double nulls show **complete absence of skeletal mineralization with perinatal lethality**, far beyond either single. Plus an epistasis test: **TNAP overexpression normalises *Phospho1*⁻/⁻ plasma PPi but does NOT correct the bone phenotype** — proving the two enzymes are not interchangeable even when one is in excess.
- **VERDICT: CLEAN** (both)
- **action:** → `paralog_audit: passed` on both. **Best-evidenced pair in the audit**: double null, epistatic rescue failure, compartment-resolved ultrastructure, a measured inhibitor selectivity margin, and human interventional proof (asfotase alfa, 1-year survival 42%→95%).

## enpp1_enzyme · ankh_transporter
- **Already adjudicated — CORR-001.** ANKH exports ATP; ENPP1 hydrolyses it to PPi. Re-read for residual paralog exposure: **ABCC6** is the third transporter and is quantified against ANKH in the node (ABCC6 60–70% vs ANKH ~25% of plasma PPi), so the relative-abundance question is answered numerically.
- **VERDICT: CLEAN** (post-correction)
- **action:** → `paralog_audit: passed`.

## stat5b_tf · jak2_kinase
- **mechanism attributed to:** STAT5B as the growth-relevant arm of GH signalling; JAK2 as proximal transducer.
- **paralogs/isoforms in family:** **STAT5A**, which is ~90%+ identical to STAT5B and co-expressed in the same cells; STAT1/STAT3 also downstream of GHR; JAK1/JAK3/TYK2 for JAK2.
- **co-expressed in the relevant zone? relative abundance:** STAT5B phosphorylation status by growth plate zone **not reported** — stated.
- **key experiment's perturbation and its SELECTIVITY:** **human homozygous *STAT5B* mutations** (`kofoed2003`, `hwa2005`, including one with complete absence of STAT5B protein) — gene-selective, human, and the phenotype is GH insensitivity **biochemically indistinguishable from GHR deficiency**. STAT5A is present and intact in these patients and does not compensate. That is the paralog double-check performed by nature: the alternative was present, and it did not rescue.
- **VERDICT: CLEAN** (both)
- **action:** → `paralog_audit: passed` on both. `jak2_kinase` correctly grades its own evidence as **indirect**, inferred from the receptor above and the transcription factor below, rather than claiming direct growth evidence.

## gh_receptor · socs2_protein · ghsr_receptor · leptin_receptor
- **mechanism attributed to:** GHR as GH receptor (rotation mechanism, `brooks2014`); SOCS2 as the GH-signalling brake; GHSR1a in the ghrelin arm; LEPR ObRb in the energy arm.
- **paralog handling:** `socs2_protein` — SOCS1/SOCS3/CIS are the paralogs; the *Socs2*-null **gigantism with normal circulating GH and IGF-1** is gene-selective and the paralogs demonstrably do not compensate. `leptin_receptor` explicitly separates the **ObRb isoform** from the short isoforms and separates the endocrine role from the LepR⁺ marrow stromal marker role — a conflation this atlas correctly refuses. `gh_receptor` carries zonal rat data (RZ/PZ highest, `gevers2002`).
- **VERDICT: CLEAN** (all four)
- **action:** → `paralog_audit: passed` on all four.

## klotho_beta_cofactor
- **mechanism attributed to:** FGF21 acting on growth plate chondrocytes through **an FGFR1–ERK arm**, gated by β-Klotho, to produce undernutrition-induced local GH insensitivity.
- **paralogs/isoforms in family:** **FGFR3**, and to a lesser extent FGFR2/FGFR4; α-Klotho for KLB.
- **co-expressed in the relevant zone? relative abundance: the paralog is in the same cells, on the same paper's own data.** `wu2012` detected ***Fgfr1* AND *Fgfr3*** transcripts (with *Klb* and *Fgf21*) in the same mouse growth plate chondrocytes. And this atlas's own `fgfr3_receptor` node states, from human ISH, that **the growth plate is an FGFR3-dominant tissue** — FGFR1 is not even detected in human growth plate chondrocytes (`delezoide1998`). So the receptor the mechanism is assigned to is the one the human expression map says is **absent** from this cell type.
- **key experiment's perturbation and its SELECTIVITY:** siRNA against **FGFR1** (and ERK1) prevented every FGF21 effect. siRNA is gene-selective, so FGFR1 **necessity** is supported in mouse chondrocytes. But **no *Fgfr3* knockdown control is reported**, so FGFR3 was never removed and its contribution is unmeasured — and knockdown efficiency/off-target fold-selectivity are not stated.
- **ligand/agonist selectivity:** **the dose is the second problem, and the node already flags it.** The inhibitory effects required recombinant human FGF21 at **5–10 µg/ml**, which the node correctly calls "far above physiological circulating FGF21". At those concentrations FGF21 can engage FGFRs with reduced Klotho dependence, so ligand-to-receptor assignment is weakest exactly where the effect was measured.
- **double perturbation done? NEVER** — no *Fgfr1;Fgfr3* double knockdown or double conditional in chondrocytes.
- **VERDICT: AT_RISK**
- **action:** → `paralog_risk`: *"The FGF21 effect is assigned to an FGFR1–ERK arm on FGFR1 siRNA alone; FGFR3 is co-detected in the same chondrocytes by the same paper (`wu2012`), was never knocked down, and is the receptor the human growth plate actually expresses (`delezoide1998`)."* → gap `g_para_007` opened. Confidence held at **D** — the *Fgf21*-null in vivo necessity result (`wu2013`) is gene-selective at the ligand and does not depend on which receptor carries it.

## gsk3b_kinase
- **mechanism attributed to:** GSK3B as the destruction-complex kinase whose inhibition raises β-catenin and drives terminal differentiation in chondrocytes.
- **paralogs/isoforms in family:** **GSK3A** — ~98% identical in the kinase domain, co-expressed in essentially every cell, and functionally redundant with GSK3B for β-catenin destruction.
- **co-expressed in the relevant zone? relative abundance:** zonal maps absent for both — but the functional relationship is measured and it is worse than co-expression. **In cartilage-specific *Gsk3b* knockout mice, GSK3A protein is elevated** (`bali2021`): the paralog does not merely sit there, it **upregulates to compensate**.
- **key experiment's perturbation and its SELECTIVITY: this is a clear (d) failure.** The functional evidence is `guidotti2015`, **lithium chloride** in human OA chondrocytes. LiCl inhibits **GSK3A and GSK3B indistinguishably** — it is a metal ion competing at the Mg²⁺ site, with no isoform preference whatsoever — and it additionally inhibits inositol monophosphatase and other targets at the concentrations used. Fold-selectivity for GSK3B over GSK3A: **none; and no ATP-competitive GSK3 inhibitor with meaningful GSK3A/B selectivity exists.**
- **double perturbation done? YES — and the node states the opposite.** This is a factual error in the node, corrected here. `bali2021` (J Mol Med 2021) generated a **tamoxifen-inducible cartilage-specific *Gsk3a*/*Gsk3b* double knockout**: precocious growth plate remodelling, progressive loss of cellular and proteoglycan components, decreased SOX9, increased osteoclast recruitment and apoptosis, **shorter long bones and growth retardation**. `itoh2012` adds the allelic series: ***Gsk3a*⁻/⁻ alone and *Gsk3b*⁺/⁻ alone do not significantly affect skeletal development, but the compound *Gsk3a*⁻/⁻;*Gsk3b*⁺/⁻ causes dwarfism** with impaired chondrocyte differentiation, and demonstrates the two isoforms are **functionally redundant in a cell-autonomous fashion, independently of Wnt/β-catenin**, acting via RelA Thr-254.
- **VERDICT: AT_RISK** — and the double perturbation, now that it has been found, makes the verdict *firmer* rather than resolving it.
- **Why the double confirms the risk instead of clearing it:** the discriminating experiment came out on the side of redundancy. The **cartilage-specific *Gsk3b* single knockout is phenotypically normal** — the only thing that changes is that GSK3A protein goes up. So the GSK3-dependent chondrocyte phenotype cannot be assigned to GSK3B by any available evidence: the selective genetic removal of GSK3B does nothing, and the non-selective chemical removal of both does something. `itoh2012` further shows the redundant function runs **independently of Wnt/β-catenin**, which weakens the node's framing of GSK3B as primarily a destruction-complex kinase in this tissue.
- **What still stands:** GSK3B's biochemical role in the β-catenin destruction complex is not in question, and the node's anchoring of the claim to the β-catenin *substrate* level (`akiyama2004`) rather than to GSK3B itself is what keeps this from being a supersession. The node also already calls LiCl "a blunt instrument" and lists the confounding non-WNT functions. Grade **D** was already correct.
- **action:** → `paralog_risk`: *"GSK3A and GSK3B are functionally redundant in chondrocytes (`itoh2012`); the cartilage-specific *Gsk3b* single knockout is normal with compensatory GSK3A upregulation (`bali2021`), and the only positive chondrocyte evidence is LiCl, which does not distinguish the two."* → **node text corrected**: the claim that no chondrocyte-restricted *Gsk3b* conditional knockout has been reported is wrong; one exists and is phenotypically silent. → `bali2021` and `itoh2012` added to `key_refs`. → gap `g_para_008` opened, reframed from "has the double been done" to "which GSK3-dependent chondrocyte phenotypes survive isoform-selective removal". Confidence held at **D**.

## hif1a_chondrocyte · vhl_protein
- **mechanism attributed to:** HIF1A enforcing survival and growth arrest in the hypoxic plate interior; pVHL as the oxygen-off switch upstream.
- **paralogs/isoforms in family:** **HIF2A (EPAS1)** and HIF3A — HIF2A is the classic confound in any HIF1A attribution, since it shares the HRE and the VHL degradation route.
- **key experiment's perturbation and its SELECTIVITY:** chondrocyte-restricted *Hif1a* deletion (gene-selective) with a **spatially resolved** readout — death specifically of **interior** cells, loss of p57, raised BrdU.
- **double perturbation done? YES, and it is the discriminating one.** `pfander2004`: *Vhlh* deletion (stabilising HIF α subunits generally) causes dwarfism, and the ***Vhlh;Hif1a* double null resembles the *Hif1a* single null**. If HIF2A were carrying a substantial share of the VHL-loss phenotype, removing only HIF1A from the *Vhlh*-null could not return it to the *Hif1a*-null appearance. The epistasis therefore bounds HIF2A's contribution without ever deleting it.
- **A second alternative also tested:** `schipani2001` shows VEGF induction around dying cells is **HIF1A-independent**, so the node does not over-attribute VEGF to HIF1A.
- **VERDICT: CLEAN** (both)
- **action:** → `paralog_audit: passed` on both.

## hsd11b1_enzyme · hsd11b2_enzyme
- **mechanism attributed to:** **nothing, in the growth plate.** Both nodes are grade **E** explicit negatives: HSD11B1 — "a targeted search returns no study measuring HSD11B1 expression or activity in growth plate chondrocytes by zone, in any species"; HSD11B2 — "whether chondrocytes express HSD11B2 has not been established".
- **paralog handling:** the two enzymes are each other's counter-directional partners (reductase vs dehydrogenase) and each node names the other.
- **VERDICT: CLEAN** (both) — attribution withheld; the pre-receptor amplification model is labelled "widely assumed but the primary evidence is essentially absent".
- **action:** → `paralog_audit: passed` on both.

## mct8_transporter
- **mechanism attributed to:** MCT8 as the T3/T4 transporter determining cellular thyroid hormone access.
- **paralogs/isoforms in family:** **OATP1C1, MCT10, LAT1, LAT2** — all thyroid hormone transporters.
- **key experiment's perturbation and its SELECTIVITY:** hemizygous human *SLC16A2* loss of function — gene-selective, human; plus the **Triac** intervention (`van2022`), which works precisely *because* it enters cells **independently of MCT8** — a mechanism-confirming pharmacological design rather than a confounded one.
- **double perturbation done?** n/a for the human claim.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. The node states outright that **"whether growth plate chondrocytes depend on MCT8 or on alternative transporters (OATP1C1, MCT10, LAT1/2) has not been established in any species"** — the paralog list is written into the node before being asked for.

## vitamin_d_receptor
- **mechanism attributed to:** VDR-null rickets is **mostly mineral-mediated**, with a residual chondrocyte-autonomous role.
- **key experiment's perturbation and its SELECTIVITY:** `sabbagh2005` — a **calcium/phosphate/lactose rescue diet prevents the rachitic changes** in VDR-null mice. That is a mechanism-discriminating intervention that separates a direct cartilage receptor requirement from a systemic mineral effect, and it moves most of the attribution *off* the receptor.
- **VERDICT: CLEAN**
- **action:** → `paralog_audit: passed`. Same shape as `androgen_receptor`: the node reassigns its own effect on the strength of a discriminating experiment.

---

# Summary table

| Family | Nodes | CLEAN | AT_RISK | Double perturbation exists? |
|---|---:|---:|---:|---|
| FGFR + FGF ligands | 6 | 6 | 0 | Yes (`hung2016` Fgf9/Fgf18; Fgfr1/Fgfr2) |
| Natriuretic peptide (CNP/NPR) | 3 | 1 | 2 | **NEVER** (Npr1;Npr2 / Nppa;Nppc) |
| PKG (prior pass) | 2 | — | — | **NEVER** (`g_l2d_001`) |
| PDE isoforms | 5 | 4 | 1 | **NEVER** (Pde3a;Pde3b) |
| IGF1R / INSR | 2 | 2 | 0 | Never, but hybrids acknowledged |
| Collagen isoforms | 4 | 4 | 0 | n/a — reconstitution + substitution data |
| SOX5/6/9 | 3 | 3 | 0 | **Yes** (`smits2001`) |
| ADAMTS + TIMP | 3 | 3 | 0 | **Yes** (`majumdar2007`) |
| MMP | 3 | 2 | 1 | **Yes** (`stickens2004`) — newly attached |
| PTH1R | 1 | 1 | 0 | n/a — epistasis + chimaera |
| BMP + antagonists | 5 | 5 | 0 | **Yes** (`bandyopadhyay2006`, `stottmann2001`) |
| SMAD | 2 | 2 | 0 | **Yes** (`retting2009`) |
| GLI + Hh transducers | 6 | 6 | 0 | **Yes** (`hilton2005` Ihh;Gli3) |
| Thyroid (THRA/THRB/DIO2/DIO3) | 4 | 1 | 3 | **Yes but not in cartilage** (`gthe1999`) |
| Estrogen (ERα/ERβ/GPER/AR/aromatase) | 5 | 5 | 0 | **Yes** (`vidal2000` DERKO) |
| IGFBP + pappalysins + STC2 | 9 | 9 | 0 | n/a — substrate specificity measured |
| RUNX / LRP / PIEZO / TRPV4 | 7 | 7 | 0 | **Yes** (`yoshida2004`, `joeng2011`, `brylka2024`) |
| Cilium (IFT80/88/KIF3A) | 3 | 3 | 0 | n/a — lineage-restricted controls |
| Mineralization (TNAP/PHOSPHO1/ENPP1/ANKH) | 4 | 4 | 0 | **Yes** (`yadav2011`) |
| GH axis (GHR/JAK2/STAT5B/SOCS2/GHSR/LEPR) | 6 | 6 | 0 | n/a — human genetics |
| Remaining (KLB, GSK3B, HIF1A/VHL, HSD11B1/2, MCT8, VDR) | 8 | 6 | 2 | **Yes** (`pfander2004` Vhlh;Hif1a; `bali2021` Gsk3a/Gsk3b cDKO) |
| PKG (prior pass, CORR-003) | 2 | — | — | **NEVER** (`g_l2d_001`) |
| **Total** | **91** | **80** | **9** | 12 of 21 families have a published double |

## What the ratio means

**80 CLEAN to 9 AT_RISK.** The atlas is in better shape on this failure mode than the three
prior findings suggested, and the reason is structural rather than lucky: **seven families
already have their double perturbation published**, and the nodes were written around the
double rather than around a single knockout. Where the atlas fails, it fails in a
consistent and predictable place — **wherever the load-bearing experiment is
pharmacological rather than genetic**. Four of the nine AT_RISK findings (`pde3b`,
`gsk3b_kinase`, `thrb_receptor` in part, `klotho_beta_cofactor` in part) trace to a
compound or a ligand that cannot distinguish the paralogs: cilostazol/milrinone across
PDE3A/PDE3B, LiCl across GSK3A/GSK3B, T3 across TRα/TRβ, high-dose FGF21 across FGFR1/FGFR3.

The generalisable rule this pass produces: **in this domain, an attribution supported only
by a small molecule should be assumed paralog-ambiguous until the selectivity margin is
looked up and written down.** Not one of the four nodes above recorded a selectivity fold
before this audit; in every case the number (or its documented impossibility) was
retrievable in a single search.

Two further observations worth carrying:

1. **Nodes that name their own alternative are the ones that pass.** `pde1c` names PDE1B
   against itself, `collagen_type_xi` records α1(V) substituting into the null,
   `androgen_receptor` moves its own effect onto aromatised estrogen, `mct8_transporter`
   lists its four competitors, `insulin_receptor` volunteers the hybrid problem,
   `gper1_receptor` names the un-run ERα/GPER1 dose experiment. This behaviour, not
   confidence grade, is what predicts surviving an audit — `pde1c` is grade **E** and
   passes cleanly, while several grade-A and grade-B nodes needed work.
2. **The two nodes with no paralog risk *and* no attribution are still doing work.**
   `pde9a` and `hsd11b1_enzyme` are explicit negatives, and their value is that they mark
   where the coastline is rather than leaving a silent hole.

## Reference disposition

Standing policy applied — **no measurement was retired anywhere in this pass.**

| Ref | Classification | Reasoning |
|---|---|---|
| `kawabe2025` (PDE3 inhibitors elongate bone) | **interpretation_superseded** (partial) | The cGMP rise, K⁺ channel activation, bone elongation and body-size increase are real and are retained in full. What does not follow is the isoform assignment: cilostazol and milrinone are PDE3-family agents and cannot discriminate PDE3B from PDE3A. The measurement stands; "PDE3B" as its molecular subject does not, pending `g_para_002`. |
| `rowley2024` (PDE3A/PDE3B homology) | **observation_stands** | The correcting evidence for the selectivity question. |
| `inada2004` (*Mmp13*-null persists into adulthood) | **observation_stands, contested** | An independent *Mmp13*-null line (`stickens2004`) reports resolution by 12 weeks. Both are primary; neither supersedes the other on available evidence. Logged as a contradiction, **not** retired. |
| `stickens2004` (Mmp9/Mmp13 double) | **observation_stands** | Confirms MMP-13's substrates in vivo and supplies the double perturbation. |
| `rabier2006` (all T3 responses require TRβ) | **interpretation_superseded** | The measurement — abolished T3 responses in TRβ-deficient rib chondrocytes — stands. The inference that TRβ is therefore the isoform carrying the chondrocyte T3 response does not survive `gthe1999`, which shows the isoforms substitute for each other so that germline single nulls under-report. Not retired. |
| `gthe1999` (TRα1⁻/⁻β⁻/⁻ double) | **observation_stands** | The correcting evidence for the thyroid isoform question. |
| `vidal2000` (ERKO/BERKO/DERKO) | **observation_stands** | Confirming evidence; it makes `estrogen_receptor_alpha` and `estrogen_receptor_beta` materially more trustworthy rather than less. |
| `zhou2024` (corin/ANP in chondrocytes) | **observation_stands** | New alternative-source evidence for the chondrocyte cGMP pool. |
| `wang2011` (cartilage-specific *Igf1r*) | **observation_stands** | Supplies the IGF1R-selective cartilage perturbation the atlas lacked. |
| `chou2021` (chondrocyte GPER-1 cKO) | **observation_stands** | Establishes that the GPER1 attribution is genetic, not an estradiol-ligand inference. |
| `dentice2005`, `shen2004` (DIO2 in growth plate) | **observation_stands** | First primary DIO2 growth plate evidence attached to `dio2_deiodinase`. |
| `guidotti2015` (LiCl in chondrocytes) | **interpretation_superseded** (partial) | The observed link between GSK3 inactivation, oxidative DNA damage and terminal differentiation stands as a measurement. Its assignment to GSK3B specifically does not, since LiCl does not discriminate GSK3A. Not retired. |
| `wu2012` (FGF21/FGFR1 in chondrocytes) | **observation_stands, scope-limited** | The siRNA necessity result for FGFR1 stands as measured. It does not exclude FGFR3, which the same paper detected in the same cells and never knocked down. |
