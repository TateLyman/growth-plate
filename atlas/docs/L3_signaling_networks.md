# L3 — Signalling networks

**88 nodes (0 stubs) · 683 edges touching the layer · 76 gaps · 66 refs**
Confidence: A 8 · B 18 · C 47 · D 12 · E 3. `human_evidence` direct 18 (21%) / indirect 28 /
**absent 42 (48%)**. `translation_risk` **high on 50 of 88**. Replicated human: **11%**.

This is the densest layer and the least human. It is also where a language model's fluency is
most dangerous, because the murine pathway literature is enormous, internally consistent and
reads as settled. Phase 2d put twelve canonical mechanisms to their primary sources; **two
were SUPERSEDED and six were SCOPED**. Both superseded mechanisms are in this layer.

---

## 1. The settled core

**The PTHrP/IHH negative feedback loop survived a full audit.** `stjacques1999` Fig. 4C:
BrdU⁺ fraction in the *Ihh*⁻/⁻ humerus is ~half wild-type from 12.5 dpc (P < 0.01 to
< 0.005) with a shortened proliferative zone. `kobayashi2005` and `mak2008` establish the
three-output decomposition — PTHrP arm, direct proliferative arm, PTHrP-independent
hypertrophy arm — including the control that PTHrP heterozygosity barely affects
Ihh-driven column elongation. **VERDICT: CONFIRMED**, with two recorded caveats: the entire
*Ihh*-null characterisation is embryonic (12.5–18.5 dpc, lethal at birth) and therefore says
nothing about the postnatal plate, and `mak2008` raises Hh signalling largely with **Shh
protein** and *Ptch1* inactivation rather than Ihh, so "Ihh-specific" rests on pathway
identity, not ligand identity.

**PTH1R is epistatically downstream of PTHrP and acts cell-autonomously on proliferating
chondrocytes. CONFIRMED.** `schipani1997`: the constitutively active receptor **corrects the
growth plate of PTHrP-null mice at birth and rescues survival**. `chung1998` chimeras show
cell-autonomy for proliferation and, separately, that matrix mineralization around ectopic
hypertrophic cells is **non**-cell-autonomous, requiring a critical mass of neighbours. One
correction from the audit: the Blomstrand patient in `jobert1998` is **heterozygous**, with
the paternal allele unexpressed by an unexplained mechanism — functionally biallelic,
genotypically not, n = 1.

**FGFR3 is a negative regulator of elongation, and the human allelic series is the strongest
evidence in the layer.** The MAPK branch is **CONFIRMED** precisely: constitutively active
MEK1 in chondrocytes gives incomplete hypertrophy, reduced collagen X, persistent Sox9 and
delayed ossification with **no change in BrdU incorporation** (`murakami2004`, Fig. 1P–Q).

**The NPR2 dose–stature relationship is human, graded and bidirectional.** Biallelic loss
(AMDM): adult height 130.5 and 134 cm (−6.57 and −4.58 SDS) in two siblings after 8.5 years
of high-dose GH (`arya2020`). Heterozygous carriers: −1.8 vs −0.4 SDS against non-carrier
relatives (n = 16 vs 23, SD 1.1/0.8, **P < 0.0005**, `olney2006`); −2.06 vs −1.37 in a second
family (`hanley2020`); −4.5 to −1.7 across three dominant-negative missense families
(`vasques2013`). Gain of function runs the other way: p.Met482_Leu483del gives +2.77, +1.96,
+1.30 SDS in a mother and two daughters (`lauffer2020`). Prevalence among idiopathic short
stature is contested — **6% (3/47)** in `vasques2013` against **0–3.8%** in `wang2015`
(192 patients, 192 controls). No other node in this layer has a human dose–response in both
directions.

**Cartilage-specific knockouts give the pathway's amplitude.** `nakao2015`, n = 5/group:
*Npr2* cKO hypertrophic zone **23.0%** of control, non-hypertrophic layer 71.1%, femur 45.3%;
*Nppc* cKO hypertrophic zone 34.6%, non-hypertrophic 76.7%, tibia 65.9%.

---

## 2. The live disagreements

**CORR-003 is the layer's central live failure, and it sits in the effector step of the
pathway vosoritide targets.** A linear CNP → GC-B → cGMP → PKG-II chain predicts that losing
PKG-II phenocopies losing GC-B. It does the opposite, by a wide margin and in the same
direction as nothing else. The *Prkg2*-mutant KMI rat growth plate is **2.6× EXPANDED —
665 ± 47 µm vs 255 ± 34 µm, n = 8** (`chikuda2004`), through an accumulated intermediate
layer of postmitotic **non**-hypertrophic chondrocytes; the cartilage-specific *Npr2*
knockout hypertrophic layer is **23.0% of control** with a thinner plate overall
(`nakao2015`). Same nominal pathway, opposite sign.

Three things make this more than a curiosity. (i) The zonal justification also fails: the
only **protein-level** map places PKG-II in **late proliferative and prehypertrophic**
chondrocytes "preceding the start of hypertrophic differentiation" (`chikuda2004` Fig. 3A,
rat IHC), while the hypertrophic enrichment the field cites is **mRNA** (`agoston2007`,
4.4-fold). (ii) The alternative was present, named and never removed: cGKI (*Prkg1*) is
co-expressed at **5.9-fold** zonal enrichment — *higher* than PKG-II's 4.4-fold — and the
cGKI/cGKII double knockout was proposed independently by `chikuda2004` in 2004 and
`agoston2007` in 2007 and **still has not been made** (Europe PMC, 19 hits, all screened,
2026-08-05; gap `g_l2d_001`). (iii) All three primaries flag the contradiction in their own
text — "This may indicate the involvement of other signaling pathway(s)"; "there still
remains elusive problem"; "not identical" — and reviews propagate the linear chain anyway.
`pkg2_kinase` was regraded B → C and the atlas had carried **no quantitative row at all** for
the *Prkg2* phenotype until this audit, which is exactly why no numeric check could see the
sign conflict.

**Does raising cGMP raise growth? Rat and mouse pharmacology give opposite answers**
(C-L3-02, `g_l3core_007`). `wang2018`: PDE5 is the major cGMP-hydrolysing activity in newborn
rat epiphyseal chondrocytes; tadalafil raised peak CNP-stimulated cGMP **37%** and
whole-tissue cGMP **52%** (both P < 0.01) and produced **0% change in long bone length** over
three weeks. `kawabe2025`/`miyazaki2022`: PDE3B is the functional isoform; cilostazol and
milrinone raise cGMP, activate PKG-dependent K⁺ channels, drive TRPM7-mediated Ca²⁺ entry,
elongate cultured bones and enlarge juvenile mice, and *Pde3b*-null mice have longer tibiae.
This cannot currently be attributed between species, isoform or compartment (bulk vs
microdomain cGMP). The clinical stake is unattended: children on chronic PDE5 inhibitors for
pulmonary arterial hypertension have never had growth plate follow-up reported.

**Which FGFR3 branch carries human disease?** C-L3-01, `g_l3core_008`. The
proliferation-arrest account is rat/mouse (`sahni1999`, `su1997`). Primary **human** fetal
thanatophoric dysplasia I chondrocytes showed a mitogenic response to FGF2 and FGF9
**indistinguishable from controls**; the lesion was ligand-independent STAT activation with
nuclear STAT1 in hypertrophic cells and increased apoptosis (BAX up, BCL-2 down)
(`legeaimallet1998`). And deleting *Stat1* in achondroplasia-mutant mice restores
proliferation but rescues **neither the hypertrophic zone nor the dwarfism**
(`murakami2004`). `fgfr3_stat1_branch` is held at **grade D** with three `contradicts` refs.
No study has measured proliferation index, phospho-ERK and phospho-STAT1 together, by zone,
in human dysplastic plate against matched controls.

**The FGFR3 audit found an assay that structurally could not see the alternative.**
`sarabipour2016` is quoted as settling ligand-independent dimerisation (ΔΔG = **−1.8
kcal/mol** for G380R), but the construct is FGFR3 **extracellular + transmembrane only, with
the entire kinase domain replaced by a fluorescent protein**, in CHO-derived vesicles. The
competing mechanism — failed kinase-dependent c-Cbl ubiquitination and internalisation — is
*structurally absent from the assay*. The same paper's chemical cross-linking **disagrees**
with its own FRET result, and chemically produced vesicles gave ≈0.5 kcal/mol for the same
mutation. Separately, `cho2004` reports **decreased** ubiquitination of mutant FGFR3 and
Monsonego-Ornan 2004 reports **increased** — sign-inverted, named in `cho2004`, dropped by
reviews and by this atlas until the audit (`g_l2d_003`).

**SOX9: required for hypertrophy, or must be switched off for it?** C-L3-04. `dy2012` shows
SOX9 is needed to generate hypertrophy and directly activates *Col10a1* with MEF2C.
`zhou2015` shows the achondroplasia lesion **is** failure to downregulate SOX9, and
`kohn2015` shows Notch-driven Sox9 suppression is required for maturation onset. `sox9_tf`
(grade A) and `beta_catenin_ctnnb1` carry reciprocal `CONTRADICTS`. No experiment titrates
SOX9 within one differentiating population and reads hypertrophy as a continuous function of
it (`g_l3rest_012`).

**Two zonal facts are grade X.** x-L3-01: the "120 cm untreated adult height in AMDM" figure
has no primary cohort with an n and a dispersion measure anywhere; it is carried
`value_unverified`. x-L3-02: "GC-B protein is restricted to prehypertrophic chondrocytes" is
stated in `nakao2015` as a **citation to earlier work**, not as data — that paper's GC-B IHC
serves only to confirm knockdown — and the search for the true primary returned 10 records,
none qualifying (`g_l2d_002`, tract 5).

---

## 3. The load-bearing assumption

**That a pathway's zonal site of action can be inferred from zonal mRNA abundance.**

Almost every "where in the plate does this act" claim in L3 traces to one source:
`agoston2007`, a microarray of micro-dissected mouse tibia. That study's compartments are
**resting/proliferative COMBINED, hypertrophic, and mineralized**. They are not RZ/PZ/HZ, and
the study contains **no resting-versus-proliferative comparison at all**. The atlas had
recorded its NPR2 result as "similar across all three zones (RZ, PZ, HZ)" — a claim the
source cannot make — and had built the PKG-II zonal explanation on its 4.4-fold enrichment.

The evidence against the assumption is direct and was found by asking one question of one
figure: where mRNA and protein have both been mapped in this layer, **they disagree**
(PKG-II: hypertrophic by mRNA, prehypertrophic by protein, across two species and two assay
types). The atlas's own structural statistic agrees — **zone context fill across the whole
edge set is 5.2%**, so almost no edge in the graph is zone-annotated at all, and any
zone-filtered perturbation query returns a weakly constrained answer by construction.

If mRNA zonal enrichment does not locate protein activity, then the receptor-versus-effector
argument of C-L3-03 is unresolvable as posed, CORR-003's zonal half was never a real claim in
either direction, x-L3-02 stays open, and every therapeutic inference of the form "the drug
target is expressed where we want the effect" — which is the design rationale for the entire
CNP-analogue class — is unsupported at the level it is asserted.

---

## 4. What would change everything

**The chondrocyte-specific *Prkg1;Prkg2* double knockout**, proposed in 2004 and 2007 and
still not made. If the double mutant phenocopies CNP/GC-B loss — thinned plate, hypertrophic
layer at ~23% of control — then cGKI and cGKII are redundant effectors, the linear chain is
restored with one added node, and the KMI expansion is explained as compensatory cGKI
signalling in an unopposed intermediate layer. If it reproduces the 2.6× **expansion**, then
PKG is not the CNP effector for hypertrophy at all, `miyazaki2022`'s BK-channel → TRPM7 →
CaMKII arm becomes the leading candidate (chondrocyte-specific *Trpm7* ablation **abolishes**
CNP-driven bone growth in explant), and the mechanistic account of vosoritide has to be
rewritten downstream of the receptor.

Running a close second: any zone-resolved **protein**-level map of this pathway. It would
adjudicate C-L3-03, x-L3-02, and the PKG-II zone question simultaneously, and it is the only
thing that would let L3 make a zonal statement that does not rest on a 2007 three-compartment
microarray.

---

## 5. Numbers

| Parameter | Value | Unit | Species | Spread / n | Source | Flag |
|---|---|---|---|---|---|---|
| *Prkg2*-mutant (KMI) plate height | **665 vs 255** | µm | rat, prox. tibia, 10 wk | SEM 47 / 34, n = 8 | `chikuda2004` | single source; **sign-inverted vs `nakao2015`** |
| *Npr2* cKO hypertrophic zone | 23.0 | % of control | mouse, 2 wk | n = 5/group | `nakao2015` | single source |
| *Nppc* cKO hypertrophic zone | 34.6 | % of control | mouse, 2 wk | n = 5/group | `nakao2015` | single source |
| *Npr2* cKO femur length | 45.3 | % of control | mouse, 10 wk | — | `nakao2015` | single source |
| *Prkg2* vs *Prkg1* zonal mRNA enrichment | 4.4 vs **5.9** | fold (HZ vs RZ+PZ) | mouse | 3 trials, microarray | `agoston2007` | mRNA only; protein disagrees |
| Npr3 induction by CNP, HZ only | 16 | fold | mouse | RT-PCR significant, n.s. by array | `agoston2007` | single source |
| cGMP rise with tadalafil (cell / tissue) | 37 / 52 | % above vehicle | rat | P < 0.01 both | `wang2018` | single source |
| Long bone length change, 3 wk tadalafil | **0** | % | rat | n.s.; bodyweight −9%, P < 0.01 | `wang2018` | negative; contradicted by `kawabe2025` |
| G380R unliganded dimerisation ΔΔG | −1.8 | kcal/mol | in vitro human cell | vesicles gave ≈0.5; cross-linking n.s. | `sarabipour2016` | **kinase domain absent from construct** |
| Femur gain, GC-B(7E) on G380R/G380R | 12.6 (M) / 7.9 (F) | % | mouse, 16 wk | vs 4.3/5.0 on WT; n = 4–23 | `wagner2021` | homozygous × homozygous |
| HZ area gain, GC-B(7E), males | +70.2 | % | mouse, 2 wk | P = 0.003; final HZ n.s. vs WT (P = 0.80) | `wagner2021` | sex-specific |
| Cranial rescue by GC-B(7E) | **0** | detectable | mouse | power 36%; ~50/group needed | `wagner2021` | **underpowered null** |
| Heterozygous NPR2 carrier height | −1.8 vs −0.4 | SDS | **human** | n = 16 vs 23, P < 0.0005 | `olney2006` | — |
| NPR2 gain-of-function height | +2.77 / +1.96 / +1.30 | SDS | **human** | n = 3, one family | `lauffer2020` | single family |
| Biallelic NPR2 adult height on GH | 130.5–134 | cm | **human** | n = 2; −6.57 / −4.58 SDS | `arya2020` | n = 2 |
| Untreated AMDM adult height | "120" | cm | human | **no cohort, no n, no SD** | `arya2020` (secondary) | **grade X (x-L3-01)** |
| NPR2 haploinsufficiency in ISS | 6 (3/47) vs 0–3.8 | % | **human** | no CI reported | `vasques2013` / `wang2015` | disputed |
| Vosoritide velocity gain | +1.57 | cm/yr | **human** | 95% CI 1.22–1.93; n = 121 | `savarirayan2020` | — |
| Plasma CNP, NPPC-translocation overgrowth | 2 | fold | **human** | n = 1 vs 5 controls | `bocciardi2007` | n = 1 |
| Zone context fill across edge set | 5.2 | % | — | — | `phase3_close` | structural |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l2d_001`** (contradiction, tract 3) — the cGKI/cGKII double knockout. Chondrocyte-specific
   *Prkg1;Prkg2* deletion, scored on plate height, hypertrophic layer fraction and long bone
   length. Thinned/reduced HZ → linear chain with redundancy; 2.6× expansion → PKG is not the
   hypertrophy effector.
2. **`g_l3core_007`** (contradiction, tract 4) — PDE5 vs PDE3B. Run tadalafil, cilostazol and
   *Pde3b* deletion in **one** species, one age, one plate, with a matched cGMP readout and
   direct elongation measurement. Compartment can be separated with a FRET cGMP sensor
   targeted to membrane vs cytosol.
3. **`g_l3core_008`** (contradiction, tract 3) — which FGFR3 branch in humans? Phospho-ERK,
   phospho-STAT1, Ki-67 and TUNEL, zone-annotated, on human achondroplasia/TD physeal tissue
   against matched controls. Rodent model predicts a proliferation deficit; `legeaimallet1998`
   predicts normal proliferation with hypertrophic-zone apoptosis.
4. **`g_l2d_002`** (search_established, tract 5) — the true primary for prehypertrophic GC-B
   protein. If no such primary exists, the receptor half of C-L3-03 collapses and the zonal
   partition question is entirely an effector question.
5. **`g_l3core_011`** (quantitative_gap, tract 4) — residual NPR2 guanylyl cyclase activity vs
   adult height. Every human variant in the series assayed in one standardised cGMP output
   assay, plotted against measured adult height SDS. This converts an allelic list into a
   dose–response curve and directly constrains achievable vosoritide effect size.
6. **`g_l3rest_001` / `g_l3rest_010` / `g_l3rest_011`** (search_established) — has **any**
   pathway activity readout (nuclear phospho-SMAD1/5/8, mTORC1, pO₂) ever been measured
   zone-by-zone in human growth plate? Three separate searches, three nulls. These are the
   empirical footings the load-bearing assumption above is missing.
7. **`g_l2d_004`** (known_unknown, tract 4) — which PPP-family phosphatase dephosphorylates
   NPR2? `shuhaibar2017` identified only "a PPP-family phosphatase" from 100 µM cantharidin,
   which inhibits PPP1, PP2A, PPP4 and PPP5 together. Individual siRNA knockdowns in primary
   chondrocytes with an NPR2 phospho-site readout.

---

## 7. Human-translation status

**48% of this layer's nodes have no human evidence at all; 57% carry high translation risk;
only 11% have replicated human evidence.** Of 88 nodes, 50 are mouse-only or
mouse-plus-in-vitro. The `species_basis` fields are blunt about it: `beta_catenin_ctnnb1`,
`gli1_tf`, `mef2c_tf`, `smad1_5_8`, `sox6_tf`, `vegfa_growth_plate`, `raptor_protein`,
`hif1a_chondrocyte`, `sufu_protein`, `vangl2_pcp` and thirty others are `sp=mouse`, full stop.

The human evidence that exists is of one kind and it is genetic. Eight grade-A nodes —
`sox9_tf`, `runx2_tf`, `lrp5_coreceptor`, `noggin_antagonist`, `hdac4_protein`,
`ift80_protein`, `evc_evc2_complex`, `gdf5_protein` — are graded A because a human Mendelian
disorder proves the gene is required for human skeletal growth. That is a real and strong
form of evidence, and it establishes **necessity, not zonal site, not amplitude, not
epistasis**. Every claim in this layer about *where* a pathway acts, *how much* it
contributes, or *what it acts through* is mouse, rat, chick, bovine or cultured cell.

Four separate searches asked whether any human zonal measurement exists — for BMP activity
(`g_l3rest_001`), mTORC1 (`g_l3rest_010`), oxygen (`g_l3rest_011`), Notch (`g_l3rest_009`),
PDE isoforms (`g_l3core_006`), PCP protein asymmetry (`g_l3rest_008`), cilium frequency
(`g_l3rest_014`) and HDAC4 nuclear/cytoplasmic ratio (`g_l3rest_013`). **All returned
nothing.** The correct reading of any L3 mechanistic answer is: the topology is probably
right, the location is asserted from mouse mRNA, and the two places where someone checked the
protein, it moved.
