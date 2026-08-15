# DOMAIN 11 — ALL DRUG AND EXPOSURE CLASSES VERSUS HEIGHT (complete inventory)

**R436 full-concept-space enumeration.** Compiled 2026-08-15 entirely from EXTERNAL sources
(Europe PMC REST API, openFDA API, Drugs@FDA review PDFs, web search). No atlas file was read except
the two briefs. Every PMID below was returned by a live query in this session; where a record had no
PMID (PMC-only or preprint) it is written as `PMC-only` or `UNVERIFIED`.

⭐ **Three FDA pharmacology/toxicology reviews were downloaded and text-extracted in this session**
(dabigatran, axitinib, regorafenib) — the brief predicted these hold limb-length and growth-plate
endpoints invisible to PubMed, and they do. See PROSE 3, which includes the retrieval recipe.

**Reading the DIRECTION column:**
- `↑` = reported to INCREASE longitudinal growth / bone length / adult height
- `↓` = reported to DECREASE it, or to advance bone age / close the plate early (a period cost)
- `↕` = biphasic, dose-dependent, or genuinely contested
- `0` = tested and null
- `?` = named in the domain brief but no direct growth/length endpoint found

**OBSCURE?** = rarely discussed in the mainstream growth literature. Those rows are the high-value ones.

---

## THE TABLE

| # | AGENT/CLASS | DIRECTION | EVIDENCE (species + PMID) | MECHANISM IF KNOWN | STATUS | OBSCURE? |
|---|---|---|---|---|---|---|
| **A. SOMATOTROPIC AXIS** |
| 1 | rhGH (somatropin), daily | ↑ | Human, meta-analysis ISS adult height 21398350; ISS RCT 25075207; ISS meta 33035189 | GHR→JAK2/STAT5→hepatic + local IGF-1 | approved | no |
| 2 | Long-acting GH: somapacitan, somatrogon, lonapegsomatropin | ↑ | Human NMA 39261416; somapacitan Turner phase 3 42538806 | as rhGH, weekly PK | approved | no |
| 3 | GH — SCFE / physeal avulsion as an on-target skeletal harm | ↓(local) | Human cohort SCFE 38225906; proximal tibial physeal avulsion case-control 38127811 | accelerated growth destabilises the physis mechanically | approved | **yes** |
| 4 | Ghrelin-receptor secretagogue: ibutamoren/MK-677 | ↑(GH axis) | Human hepatotoxicity 40675653; doping detection 40882886 | GHSR1a agonist, endogenous GH pulses | not approved; widely misused | **yes** |
| 5 | LUM-201 (oral GH secretagogue) | ↑ | Human phase 2 abstracts PMC11454631, PMC12545614 (conference; no full PMID) | GHSR agonist; restores pulsatile GH | clinical (phase 3 planned) | **yes** |
| 6 | Macimorelin | ? (diagnostic only) | Human 36694890; receptor pharmacology 40542284 | GHSR agonist, single dose | approved as diagnostic | **yes** |
| 7 | Anamorelin | ? | Human receptor work 40542284; cachexia indication | GHSR agonist | clinical/approved (Japan) | **yes** |
| 8 | Mecasermin (rhIGF-1) | ↑ | Human review 26822565 | direct IGF1R agonism, bypasses GHR | approved (severe IGF-1 deficiency) | no |
| 9 | Pegvisomant (GH-receptor antagonist) | ↓ | Human acromegaly; direct osteoblast effects 38159174 | blocks GHR dimerisation | approved (adults) | no |
| 10 | Octreotide / somatostatin analogue for TALL stature | ↓ (deliberate) | Human, boys, final height 16452538; 10 tall adolescents 2321479 | suppresses GH secretion | approved (off-label use) | **yes** |
| 11 | Lanreotide, pasireotide | ? | No growth-plate endpoint found (query returned 0) | SSTR2/5 agonism | approved | **yes** |
| 12 | Bromocriptine / cabergoline (prolactinoma) | ↑ (restoration) | Human case, catch-up growth 15160292; 1619034 | restores GH secretion by shrinking adenoma | approved | **yes** |
| **B. SEX STEROIDS AND THEIR MODULATORS** |
| 13 | Anastrozole | ↑ (period) | Human RCT anastrozole vs letrozole 3 yr 39262574; boys on GH 37988665; CAH 39492684 | aromatase inhibition → less oestrogen → slower plate senescence | approved (off-label) | no |
| 14 | Letrozole | ↑ (period) | Human + rhGH adult height boys 38018388; +GH/GnRHa girls 38723894; retrospective 36169241 | as above, deeper E2 suppression | approved (off-label) | no |
| 15 | Testolactone (1st-gen AI) | ↑ (period) | Human, familial male precocious puberty 2492636 (NEJM); 6-yr follow-up 9920079 | weak aromatase inhibition | withdrawn/historic | **yes** |
| 16 | Exemestane | ? | No paediatric height endpoint retrieved | steroidal aromatase inactivator | approved | **yes** |
| 17 | Tamoxifen (SERM) | ↓ | Rat metatarsal permanent growth arrest 17293177; young male rat 18348701; mouse cartilage 40517943 | apoptosis of resting-zone chondrocytes; PKC inhibition 11983487 | approved | no |
| 18 | Raloxifene | ↓ (oestrogen-agonist at plate) | Rabbit growth plate 12639932 | full ER agonist on rabbit physis → hastens fusion | approved | **yes** |
| 19 | Fulvestrant (SERD) | ↕ | Human, McCune-Albright girls 22999294 | ER degradation; bone-age advance slowed, height unchanged | approved | **yes** |
| 20 | Vepdegestrant / ER PROTAC degraders | ? | No skeletal or growth-plate endpoint found in any species | catalytic ERα protein removal | approved (adult oncology) | **yes** |
| 21 | Oestrogen (high-dose) for tall stature reduction | ↓ (deliberate) | Human, tall stature treatment complication 10518082; T+EE2 tall boys 11932294 | accelerates all seven plate-senescence parameters | historic practice | no |
| 22 | Ethinyl oestradiol, pubertal induction timing | ↕ | Human Turner 27916781; UK Turner trial 24751470 | dose/timing trade-off between spurt and fusion | approved | no |
| 23 | Aromatase deficiency (natural experiment) — E2 replacement | ↓ (closes plate) | Human adult male 40048086; 4 males 20164294 | proves oestrogen is the fusion signal in males | n/a | no |
| 24 | Testosterone, low-dose for CDGP | ↑ (no adult-height cost) | Human 12608930; 8961126; 1728537 | pubertal spurt without net height loss | approved | no |
| 25 | Oxandrolone | ↑ | Human Turner RCT 21493672 (BMJ); final analysis 31862699; meta 26322078; CF 20145725 | non-aromatisable androgen; systemic, NOT local | approved | no |
| 26 | Oxandrolone — trans-masculine youth | ↑ | Human, preliminary 33819432 | as above | approved (off-label) | **yes** |
| 27 | Oxandrolone acts systemically, NOT at the plate | 0 (local) | Rat fetal metatarsal, oxandrolone/testosterone/flutamide all null 19258714 | AR present but not rate-limiting ex vivo | preclinical | **yes** |
| 28 | Stanozolol | ↑ | Human GH+stanozolol Turner 25824243; GnRHa+stanozolol CPP 34177807; rat plate via ERα 21823523 | anabolic steroid; partial ERα route | approved (limited) | **yes** |
| 29 | Nandrolone decanoate | ? | No growth-plate endpoint retrieved (query returned 0) | AR agonist | approved (limited) | **yes** |
| 30 | SARMs — RAD140/testolone, ligandrol/LGD-4033, ostarine | ? (bone mass ↑) | Rat/mouse BMD: 40680216, 37407738, 37378829; no LENGTH endpoint anywhere | tissue-selective AR agonism | illicit; widely used by adolescents | **yes** |
| 31 | Finasteride | ? | No bone-length endpoint in any species; BMD/fracture cohort 29789004 | blocks 5α-reduction of T→DHT | approved | **yes** |
| 32 | Dutasteride (dual type 1+2) | ? | Human BMD 26225793, 25420363; no length endpoint | dual SRD5A inhibition | approved | **yes** |
| 33 | GnRH agonists (leuprolide, triptorelin, histrelin) | ↑ in CPP; ↓/neutral otherwise | Human 42130798, 39703867, 26528763; histrelin 23485026, 25803268; GnRHa+CPP 20356934 | halts premature puberty; removes spurt as well as fusion | approved | no |
| 34 | GnRH antagonists (degarelix, relugolix) | ? | No paediatric growth endpoint retrieved | direct GnRHR blockade | approved (adults) | **yes** |
| 35 | Cyproterone acetate | ↕ (no adult-height benefit) | Human 1478628; 8482275; +GH in non-GHD short stature null 9509068 | antiandrogen + progestin | approved (EU) | **yes** |
| 36 | Flutamide (± AI in CAH/FMPP) | ↑ (combination) | Human CAH 15985486; antiandrogen+AI+reduced HC adult height 39672600 | AR blockade lowers plate androgen/oestrogen load | approved (off-label) | **yes** |
| 37 | Bicalutamide + anastrozole (testotoxicosis) | ↑ | Human 16939760; 20333877; 20713483 | AR blockade + aromatase inhibition | off-label | **yes** |
| 38 | Ketoconazole (steroidogenesis inhibitor) | ↑ (adult height) | Human FMLPP adult height 15522928; 18088394; 2984563 | CYP17/CYP11 inhibition lowers androgen | off-label | **yes** |
| 39 | Spironolactone (+ testolactone) in FMPP | ↑ | Human 2492636; 8421081; 9920079 | AR antagonism + weak AI | approved (off-label) | **yes** |
| 40 | DHEA / "prohormone" supplements | ? | No bone-age endpoint retrieved (query returned 0) | androgen precursor → aromatisable | supplement | **yes** |
| **C. GLUCOCORTICOIDS AND MINERALOCORTICOIDS** |
| 41 | Systemic prednisolone/prednisone | ↓ | Human nephrotic 30240629; short-term linear growth 2202451; vs dexamethasone 12153596 | GR; IGF-1 axis, chondrocyte apoptosis | approved | no |
| 42 | Dexamethasone | ↓ (strongest) | Rat plate apoptosis 12630918; rat GR upregulation 18067838; maternal 32767431; porcine IGF axis 12176674 | GR→chondrocyte apoptosis, IGF-1 resistance | approved | no |
| 43 | Deflazacort vs prednisone (DMD) | ↓ (both) | Human CINRG 26311750; 8-yr 18279756; comparison 35723111 | GR; deflazacort marginally less growth-suppressing | approved | **yes** |
| 44 | **Vamorolone (dissociative steroid)** | ↓ **less than prednisone** | Human RCT 36036925; 48-wk RCT 38335499; bone/cartilage biomarkers 42547787 | GR modulator lacking the transactivation that suppresses growth | approved | **yes** |
| 45 | Inhaled budesonide | ↓ | Human 16452586; DPI growth RCT 19298635; vs fluticasone 16735113, 16119035 | systemic GR exposure; ~11% oral bioavailability | approved | no |
| 46 | Inhaled fluticasone (propionate/furoate) | ↓ (least of the ICS) | Human 1-yr growth RCT 37728224; 26644401; vs budesonide 16119035 | ~1% oral bioavailability | approved | no |
| 47 | Inhaled mometasone | ↓ (small) | Human placebo-controlled growth velocity 21854342 | GR | approved | **yes** |
| 48 | Inhaled ciclesonide | ↓ (minimal) | Human long-term safety 18070931; RCT review 34871154; case 27284755 | on-site-activated prodrug | approved | **yes** |
| 49 | Intranasal corticosteroids (budesonide, fluticasone furoate) | ↓ | Human budesonide nasal 16729787; **fluticasone furoate nasal growth velocity reduced 25017530** | systemic absorption from nasal mucosa | approved OTC in places | **yes** |
| 50 | Topical corticosteroids | ↓ (potency/BSA-dependent) | Human ultrasound skin marker 14513873; no dedicated height RCT found | percutaneous systemic GR exposure | approved OTC | **yes** |
| 51 | Hydrocortisone dose in CAH | ↓ (dose-dependent) | Human, reduced-HC + antiandrogen + AI adult height 39672600 | replacement above physiological need costs height | approved | no |
| 52 | Fludrocortisone (mineralocorticoid) | ~0 / permissive | Human salt supplementation and linear growth 29073619; aldosterone synthase deficiency catch-up 34415991 | MR; adequate salt/mineralocorticoid is permissive for growth | approved | **yes** |
| 53 | Eplerenone / spironolactone as MR antagonists | ? | No growth-plate endpoint found (query returned 0) | MR blockade | approved | **yes** |
| **D. THYROID** |
| 54 | Levothyroxine (replacement) | ↑ (restoration) | Human — no "final height" title hit; T3 mechanism 12788086 | T3 drives chondrocyte hypertrophy | approved | no |
| 55 | Thyroxine, supraphysiological | ↕ **biphasic** | **Rat tibial growth biphasic 2327214**; maternal excess 29219024; malnourished rat 3612316, 2292727 | low dose stimulates, high dose advances maturation | approved | **yes** |
| 56 | Methimazole / propylthiouracil (induced hypothyroidism) | ↓ | Swine 38658325; medaka 40706941 | removes T3 hypertrophy drive | approved | **yes** |
| **E. GLUCOSE AND METABOLIC** |
| 57 | **Metformin** | ↑ (modest, contested) | Human meta-analysis of RCTs 26414449; low-birth-weight girls RCT 16492692; precocious pubarche 20883985; **methodological critique 27110658/27110870** | delays menarche, prolongs pubertal growth; insulin-sensitising | approved | no |
| 58 | Insulin (adequate replacement in T1D) | ↑ (restoration) | Human growth trajectory 29455193; Mauriac syndrome reversal 41560719 | restores IGF-1 bioavailability | approved | no |
| 59 | TZDs (rosiglitazone, pioglitazone) | ? | No bone-growth endpoint retrieved (query returned 0) | PPARγ; adipogenic shift in marrow | approved | **yes** |
| 60 | GLP-1 RA (liraglutide, semaglutide, exenatide) | ? / ↓ (bone healing) | Adolescent obesity trials report BMI not height 41296499; exenatide impairs rat bone healing 41063270; PWS case 32252218 | GLP1R; weight loss during growth is itself a risk | approved incl. adolescents | **yes** |
| 61 | SGLT2i (dapagliflozin) + DPP4i (saxagliptin) | 0 | **Human T2NOW paediatric follow-up: no effect on growth/Tanner to 52 wk 39446459** | SGLT2/DPP4 | approved from age 10 | **yes** |
| 62 | Orlistat | ? | No adolescent growth endpoint retrieved | fat-soluble vitamin malabsorption is the theoretical route | approved | **yes** |
| **F. CARDIOVASCULAR AND RENAL** |
| 63 | **Statins** | 0 in humans; ↑ in FGFR3 dysplasia model | **Human UK Paediatric FH Register 1-yr growth data 29208363**; meta 32333266; **statin rescues FGFR3 skeletal dysplasia (mouse/iPSC) 25231866 (Nature)** | cholesterol synthesis; FGFR3 degradation in the dysplasia model | approved incl. children | no |
| 64 | Losartan / ARBs | ↑ bone mass, **accelerates hypertrophy** | Mouse developing skeleton 25779879 | AT1R blockade → less TGF-β signalling | approved | **yes** |
| 65 | ACE inhibitors (enalapril, captopril) | ? | No paediatric linear-growth endpoint retrieved | RAAS | approved | **yes** |
| 66 | Propranolol (infantile haemangioma — the natural experiment) | 0 | Human, growth and development during treatment 37335657 | non-selective β-blockade during the fastest growth phase of life | approved | **yes** |
| 67 | β2 agonists — salbutamol | ↓ GH secretion (acute) | Human asthmatic children 8514982, 7869909 | β2→cAMP; blunts GHRH responsiveness | approved | **yes** |
| 68 | **Clenbuterol** | ↓ **longitudinal growth** | **Rat, young males: inhibited longitudinal bone growth 11828236**; bone metabolism 12433936 | chronic β2 agonism | illicit; used for physique | **yes** |
| 69 | **Minoxidil (topical and oral)** | ↓ (predicted) | Mouse lung caution 33020194; lysyl hydroxylase inhibition 30481795; **weakens newly synthesised collagen 37605092**; clubfoot cells 32951485 | inhibits lysyl hydroxylase → defective collagen cross-linking; antiproliferative | approved/OTC; near-ubiquitous in teenage boys | **yes** |
| 70 | Nifedipine / calcium-channel blockers | ↓ (rabbit) | Rabbit epiphyseal growth plate + bone turnover 8443687 | L-type Ca²⁺ channel; chondrocyte maturation | approved | **yes** |
| 71 | Furosemide (loop diuretic) | ↓ (secondary) | Human infants, secondary hyperparathyroidism + bone disease 6637931 | hypercalciuria → 2° HPT | approved | **yes** |
| 72 | Thiazides / hydrochlorothiazide | ? (bone-sparing) | Human calcium handling 41293325, 41156295; no length endpoint | reduces calciuria | approved | **yes** |
| **G. ANTICOAGULANTS AND ANTIPLATELETS** |
| 73 | Warfarin | ↓ (embryopathy; postnatal unclear) | **Human chondrodysplasia punctata after warfarin 3601467; fetal warfarin syndrome 20922410, 16856447; rat model with skeletal disturbances 1412066; osteocalcin localisation under warfarin 2125389**. No paediatric POSTNATAL height study retrieved | vitamin-K-dependent carboxylation of matrix Gla protein and osteocalcin | approved | no |
| 74 | Heparin / LMWH | ↓ (bone mass) | Human paediatric use reviews 11954754, 15085464; osteoporosis is the labelled adult class effect | osteoblast/osteoclast effects; also a soluble sulfated GAG | approved | **yes** |
| 75 | **Dabigatran (DOAC)** | **0 on limb length (verified)** | ⭐ **FDA NDA 022512 s041 pharmacology review, READ THIS SESSION: GLP Han Wistar rat study from PND 7, 0/15/32.5/70 mg/kg/day, serial LEFT ULNA LENGTH at PND 14/28/42/56 + necropsy. No effect in males at any dose; one transient female reduction at PND 28 only (24.3±1.9 vs 25.2±0.55 mm), resolved.** Not in PubMed | direct thrombin inhibition | approved incl. paediatric VTE | **yes** |
| 76 | Pentosan polysulfate / sulodexide | ? | No skeletal endpoint retrieved | soluble sulfated GAG | approved | **yes** |
| **H. ANALGESICS AND ANTI-INFLAMMATORIES** |
| 77 | Indomethacin | ↕ / uncertain | Rabbit physeal injury: uncertain effect 3354322 | COX inhibition | approved | **yes** |
| 78 | Ibuprofen | ↕ | Rat: antagonises oestrogen and tamoxifen actions on bone 9610751 | COX-1/2 | OTC | **yes** |
| 79 | Celecoxib (COX-2 selective) | ↑ (protective in inflammation) | **Rat collagen-induced arthritis: prevents growth-plate destruction adjacent to inflamed joints 17437166** | removes inflammatory catabolism (CORR-203 shape: restoration) | approved | **yes** |
| 80 | **Paracetamol / acetaminophen** | ↓ (predicted, via sulfate depletion) | **Human: acetaminophen administration depletes body stores of sulphate 3732362; serum sulfate and acetaminophen metabolism 1746133; rat PAPS/sulfate homeostasis 1602369, 2858374.** Independent human anchor that low serum sulfate matters: SLC13A1 nonsense variants → decreased serum sulfate 27412988. No direct height endpoint | consumes the inorganic sulfate/PAPS pool that chondrocytes need for proteoglycan sulfation | OTC; near-universal in adolescents | **yes** |
| 81 | Opioids (morphine, buprenorphine) | ↓ | **Rat maternal morphine, skeletal system development 33985485** | central GH suppression; direct skeletal effects | approved | **yes** |
| 82 | Local anaesthetics (bupivacaine, ropivacaine, lidocaine) | ↓ (chondrotoxic) | Canine/porcine chondrocytes 36889691, 33580729; liposomal less toxic 28992420 | direct chondrocyte death; relevant to intra-articular use near a physis | approved | **yes** |
| **I. ANTIEPILEPTICS** |
| 83 | **Valproate / valproic acid** | ↓ | **Human/experimental: effects on longitudinal bone growth 15032379**; growth velocity + bone metabolism 27142370; rat microarchitecture 32193854 | HDAC inhibition (class I/IIa); also carnitine and vitamin D effects | approved | no |
| 84 | Carbamazepine | ↓ | Human vitamin D/PTH 20933174; bone metabolism 20199720, 16255847; rat 32193854 | CYP induction → 25-OH-D catabolism; also an ER-stress modulator | approved | no |
| 85 | Topiramate | ↓ (predicted) | Human bone metabolism 20199720; acid-base 19916989 | **carbonic anhydrase inhibition → metabolic acidosis**; weight loss | approved | **yes** |
| 86 | Zonisamide | ↓ (predicted) | No dedicated paediatric growth study retrieved | carbonic anhydrase inhibition | approved | **yes** |
| 87 | Phenytoin / phenobarbital | ↓ | Human vitamin D + thyroid 23888467 | CYP induction → vitamin D catabolism; gingival fibroblast effects 23907422 | approved | no |
| 88 | Levetiracetam | 0 / minimal | Human BMD meta-analysis 38959743; monotherapy 35623138; rat 32193854 | SV2A; the "bone-neutral" AED | approved | **yes** |
| 89 | Oxcarbazepine | ↓ (milder) | Human growth velocity + bone 27142370 | weaker CYP induction | approved | **yes** |
| 90 | **Acetazolamide** | ↓ | **Human: growth suppression in children on AEDs 8972532; linear growth in pseudotumor cerebri 38983548; BMD/growth/kidney 42350680** | carbonic anhydrase inhibition → chronic metabolic acidosis | approved | **yes** |
| **J. PSYCHOTROPICS** |
| 91 | **Methylphenidate** | ↓ | Human meta-analysis 42199906; systematic review/meta 33080250; 24-month 35196830; **in vitro premature growth plate closure 36835608**; rat femur 37903444 | appetite suppression + a direct chondrocyte effect | approved; extremely common in adolescents | no |
| 92 | Amphetamine / lisdexamfetamine | ↓ | Human 2-yr open label growth and puberty 29790103; 20215923; rat postnatal 20153755 | as above | approved | no |
| 93 | Atomoxetine | ↓ | Human 34217783 (with MPH); Korean chart review 29940719; prospective 35204932 | NET inhibition; appetite | approved | **yes** |
| 94 | Guanfacine | ↕ / ~0 | Human longitudinal database vs stimulants 30942617; GH response 14642016 | α2A agonist; may raise GH acutely | approved | **yes** |
| 95 | **SSRIs — fluoxetine, sertraline** | ↓ | **Human: fluoxetine and sertraline inhibit height growth and GH signalling during puberty 39392873**; **SSRIs reduce longitudinal growth in risperidone-treated boys 29958671**; juvenile rhesus 26067181, 29473029; embryonic bone 26347317 | 5-HT transporter on chondrocytes; GH-signalling interference | approved; very common in adolescents | **yes** |
| 96 | Atypical antipsychotics (risperidone, quetiapine) | ↕ | Macaque growth parameters 21186967; hyperprolactinaemia meta 36074098; skeletal health 25863660 | hyperprolactinaemia → hypogonadism; weight gain | approved | **yes** |
| 97 | Lithium | ↑ in a rescue model | **Rat metatarsals: lithium rescues dexamethasone-induced growth failure 38684886**; rat subchondral bone 16846729 | GSK3 inhibition → raises canonical Wnt | approved; prescribed to adolescents | **yes** |
| 98 | Buspirone, hydroxyzine, trazodone, aripiprazole (DHCR7-inhibiting shelf) | ? | No skeletal endpoint for any of them in any species | raise 7-dehydrocholesterol → B-ring oxysterols inhibit Smoothened (mechanistic only) | approved | **yes** |
| **K. ANTIBIOTICS, ANTIFUNGALS, ANTIVIRALS** |
| 99 | **Fluoroquinolones (ciprofloxacin)** | ↓ (cartilage) | **Immature dog articular cartilage 15014927; juvenile rat secondary ossification centres 15631371**; Mg+vit E protects 17210779; human CF MRI 1945573 | Mg²⁺ chelation in cartilage integrin binding | approved (restricted in children) | no |
| 100 | Gepotidacin (novel topoisomerase inhibitor) | 0 | **Juvenile rat: absence of fluoroquinolone-like arthropathy 36255258** | different target class — the negative control | approved | **yes** |
| 101 | Tetracyclines / doxycycline | ↓ (high/protracted dose) | Rat protracted treatment: bone growth and maturation 6414750; microplastic co-exposure young mice 41172752 | chelates Ca²⁺; MMP inhibition | approved (>8 yr) | **yes** |
| 102 | Azithromycin (mass administration) | ↑ (in undernourished populations) | **Human cluster-RCTs: Niger 34967883; infant growth 42268611; Kenya 41285436; Tanzania ELICIT 38127924** | removes enteric infection/inflammation burden | approved | **yes** |
| 103 | Neonatal antibiotic exposure (broad) | ↓ | Human 33500411 (Nat Commun); preterm trajectory 38286129 | microbiome perturbation → IGF-1 axis | n/a | **yes** |
| 104 | **Itraconazole / posaconazole** | ↓ (predicted) | Human/mouse oncology: SMO antagonism at ordinary antifungal exposure 42122264, 42085720, 39917616 | Smoothened antagonist, distinct from cyclopamine; blocks ciliary SMO | approved; used for adolescent onychomycosis | **yes** |
| 105 | Terbinafine, fluconazole | ? (no Hh activity) | Squalene epoxidase literature 42096519 etc.; **no hedgehog activity reported** | different enzyme (SQLE) | approved | **yes** |
| 106 | Tenofovir disoproxil fumarate | ↓ (bone; growth contested) | Human in-utero exposure and linear growth 27898591; long-term growth/bone 32044401; bone markers 27494909 | proximal tubulopathy → phosphate wasting | approved | no |
| 107 | Efavirenz | ↕ (higher bone mass in children) | Human South African children 27427876; low BMD in adults 26633015; vitamin D 27559961 | CYP24A1 induction → vitamin D catabolism | approved | **yes** |
| 108 | Dolutegravir (INSTI) | ↕ | Human HEU infants 42256685, 40674650; hormonal alterations 40787011 | weight gain in mother/infant; growth signal inconsistent | approved | **yes** |
| 109 | Rifampicin + isoniazid | ↓ (via vitamin D) | Human 3838603, 7116768; mouse 26476181 | CYP induction → 25-OH-D catabolism → osteomalacia | approved | **yes** |
| **L. IMMUNOSUPPRESSANTS AND BIOLOGICS** |
| 110 | Ciclosporin / tacrolimus | ↕ (steroid-sparing benefit) | Human paediatric transplant literature 15041337; steroid-avoidance regimens 19254246 | calcineurin inhibition; main growth benefit is enabling steroid withdrawal | approved | no |
| 111 | **Sirolimus / everolimus (rapalogs)** | ↓ | **Rat: rapamycin retards growth and markedly alters the growth plate 17370095; growth retardation by disrupting growth-plate angiogenesis 20555322; bone growth during therapy 19144108; rabbit 19382193; GH partially rescues 22493717.** Human TSC null on physical development 35083513; zebrafish 37659200 | mTORC1 inhibition — chondrocyte proliferation, plate angiogenesis, and the resting-zone pool | approved | no |
| 112 | Methotrexate | ↓ | Human JIA growth-plate cohort 41393467; methotrexate osteopathy 33128074; juvenile rat 34986414 | antifolate; direct chondrocyte toxicity | approved | no |
| 113 | Azathioprine / 6-mercaptopurine | ↕ (steroid-sparing) | Human paediatric IBD 12656694; JRA 10870318 | purine antimetabolite | approved | **yes** |
| 114 | Infliximab (anti-TNF) | ↑ (restoration) | **Human paediatric Crohn: early infliximab superior long-term linear growth 29298460; catch-up growth 24865777; biosimilar 37439588** | removes TNF-driven GH resistance | approved | no |
| 115 | Adalimumab | ↑ (restoration) | Human Crohn 28301428; PAILOT post-hoc 32324651; 22405171 | as above | approved | no |
| 116 | Etanercept | ↑ (restoration) | **Human: improves longitudinal growth in prepubertal JIA 18050366**; long-term 20669280; BSPAR 25638806 | soluble TNFR2-Fc | approved | no |
| 117 | Tocilizumab (anti-IL-6R) | ↑ (restoration) | Human phase III 2-yr growth data 29961686; PMC4184285; +MTX 37303692 | IL-6 blockade restores IGF-1 | approved | no |
| 118 | Canakinumab / anakinra (anti-IL-1) | ↑ (restoration) | Human FMF growth parameters 37658934; Turkish autoinflammatory cohort 32727940 | IL-1β blockade | approved | **yes** |
| 119 | **Tofacitinib (JAK1/3)** | ↕ | **Human JIA growth impact 42067428**; **juvenile rat: no direct bone effect, femur length tracked body weight 35944741** | JAK-STAT; growth signal is largely body-weight-driven | approved | **yes** |
| 120 | **Baricitinib (JAK1/2)** | ↓ | **Juvenile rat: JAK2 inhibition stunts growth and postnatal development 41861528** | JAK2 is the GHR transducer — direct hit on the somatotropic axis | approved incl. paediatric | **yes** |
| 121 | Ruxolitinib (JAK1/2) | ↓ (predicted by class) | Human paediatric case reports only 40786056 | as baricitinib | approved | **yes** |
| 122 | Anti-IL-17/IL-23 (secukinumab, ustekinumab) | ? | Paediatric psoriasis/IBD safety only 40874954, 38665375 — no growth endpoint | IL-17A / IL-12-23p40 | approved | **yes** |
| **M. ONCOLOGY** |
| 123 | Cranial / total-body irradiation | ↓ | Human, final height by dose 8320626; ALL survivors without CRT 23351599; HSCT+GH 21725370 | GH deficiency + direct physeal damage | n/a | no |
| 124 | Alkylators + busulfan conditioning | ↓ | Human post-BMT growth 8888742, 7606014, 10828870 | direct plate damage + gonadal failure | approved | no |
| 125 | Cisplatin | ↓ | Rat epiphyseal growth plate 21567026; chondrocyte oxidative stress 37497868, 40011998 | chondrocyte apoptosis via SIRT1/Nrf2 | approved | **yes** |
| 126 | Doxorubicin / anthracyclines | ↓ | **Rat: reduced vertebral length, growth plate and IVD effects; dexrazoxane did NOT rescue 15570399**; juvenile mouse 42122233 | topoisomerase II; chondrocyte death | approved | **yes** |
| 127 | Etoposide + cyclophosphamide | ↓ | Rat growth plate and metaphyseal bone 17218784 | cytotoxic | approved | **yes** |
| 128 | **Venetoclax (BCL-2 inhibitor)** | ↓ | **ATDC5 + rat metatarsal + HUMAN growth-plate biopsies + mouse: impairs longitudinal bone growth 37198212** | BCL-2 inhibition kills growth-plate chondrocytes | approved; in paediatric trials | **yes** |
| 129 | Imatinib | ↓ | **Human German CML-PAED cohort longitudinal growth 38497150; meta-analysis 37027248** | PDGFR/c-KIT/ABL off-target on the plate | approved | no |
| 130 | Dasatinib / nilotinib | ↓ | Human, body height in children 31948524; phase II 29498925 | as imatinib, broader kinase profile | approved | **yes** |
| 131 | **Anti-angiogenics / VEGFR TKIs (axitinib, regorafenib, sunitinib, pazopanib, sorafenib, bevacizumab, ramucirumab)** | ↓ **thickened / persistent growth plate** | ⭐ **FDA reviews READ THIS SESSION: axitinib NDA 202324 — thickened growth plates in immature mice AND dogs at ≥15 mg/kg/dose, dose-responsive incidence (femur 0/0/3/0/9 M); regorafenib NDA 203085 — persistent + thickened femoral epiphyseal growth plate in dogs, chondrodystrophy of sternal symphyses, and the reviewer's own class statement that this is "known to occur in growing dogs treated with VEGF inhibitors".** Published: sunitinib monkey physeal dysplasia 18981453 | blocks vascular invasion at the chondro-osseous junction → cartilage is not cleared, so the plate thickens without lengthening the bone | approved | **yes** |
| 132 | **Hedgehog inhibitors (vismodegib, sonidegib, glasdegib)** | ↓ **premature fusion** | **Ex vivo cultured bones: vismodegib causes growth retardation, shock waves prevent it 32770014**; human paediatric physeal fusion is a labelled warning | SMO antagonism removes the hedgehog signal that maintains the resting zone | approved | no |
| 133 | MEK inhibitors (selumetinib, trametinib, cobimetinib) | ? | Paediatric NF1 trials report tumour response not stature 42260435, 39762421 | MEK1/2 → reduces chondrocyte hypertrophy | approved | **yes** |
| 134 | Immune checkpoint inhibitors | ? | Paediatric endocrine AE review 31384097 only | hypophysitis is the plausible indirect route | approved | **yes** |
| 135 | CAR-T / radioligand therapy | ? | No paediatric height endpoint retrieved | n/a | approved | **yes** |
| 136 | **Nirogacestat (γ-secretase inhibitor)** | ↓ (predicted) | Approval note 38409573; Notch–bone literature 37575153 | Notch blockade shrinks the resting-zone stem pool | approved; given to young adults | **yes** |
| 137 | Amifostine (radioprotectant) | ↑ (protective) | **Rat: dose-response protection of growth plate function from irradiation 10814957**; 12902907 | free-radical scavenging at the plate | approved | **yes** |
| 138 | Melatonin (radioprotectant at the physis) | ↑ (protective) | Rat: protects epiphysis from fractionated irradiation 14521636; vs amifostine 18979313 | antioxidant | supplement | **yes** |
| **N. EPIGENETIC DRUGS** |
| 139 | HDAC inhibitors — givinostat, vorinostat, panobinostat, romidepsin | ↓ (predicted) | **No growth-plate endpoint for any of them (queries returned 0)**; valproate (a weak HDACi) is the proxy 15032379 | HDAC4 represses MEF2C; MEF2C drives hypertrophy | **givinostat approved 2024 for DMD — taken chronically by growing boys** | **yes** |
| 140 | DNMT inhibitors — azacitidine, decitabine | ↓ (predicted) | No chondrocyte endpoint (query returned 0) | loss of maintenance methylation accelerates differentiation | approved | **yes** |
| 141 | EZH2 inhibitor — tazemetostat | ? | No bone endpoint (query returned 0) | PRC2/H3K27me3 | approved incl. paediatric | **yes** |
| 142 | Menin–MLL inhibitors — revumenib, ziftomenib | ? | No skeletal endpoint retrieved | blocks KMT2A-dependent H3K4 methylation | approved 2024+ | **yes** |
| 143 | BET inhibitors, LSD1 inhibitors, IDH inhibitors | ? | No skeletal endpoint retrieved | chromatin | clinical/approved | **yes** |
| **O. BONE-DIRECTED DRUGS** |
| 144 | Bisphosphonates (pamidronate, zoledronate, alendronate) | ↕ / 0 on length | **Rat metatarsals: alendronate and pamidronate FAILED to prevent dexamethasone growth retardation 18276203**; zoledronate growth plates 24579680; oncopediatric dosing 21713986 | inhibit osteoclastic resorption; "zebra lines" 17606790 | approved | no |
| 145 | Denosumab (anti-RANKL) | ↓ (jams the plate) | **Cynomolgus infants exposed in utero: osteoclast-poor osteopetrotic-like skeleton 24727159** | resorption is REQUIRED at the chondro-osseous junction | approved | **yes** |
| 146 | Teriparatide / abaloparatide | 0 on length | Mouse infusion 31640962; no human paediatric length endpoint | PTH1R→cAMP; boxed warning historically restricted use with open epiphyses | approved (adults) | **yes** |
| 147 | Romosozumab / setrusumab (anti-sclerostin) | ? on length | Rat fusion model 38567415; setrusumab OI 39012717 | raises canonical Wnt; sclerostin is an osteocyte product | approved / clinical | **yes** |
| 148 | Calcitonin | ↑ maturation of plate cartilage | **Rat/chick: calcitonin stimulates maturation of growth plate cartilage 3987614**; rat tibial plate 8443688 | CTR on chondrocytes | approved | **yes** |
| 149 | Strontium ranelate | ? | No growth-plate endpoint (query returned 0) | dual-action bone agent | withdrawn (EU) | **yes** |
| 150 | **Fluoride (therapeutic and environmental)** | ↓ | **Rat metatarsal: fluoride inhibits longitudinal bone growth acting directly at the plate 31838736**; review 35895945; juvenile rat + Al 39454355; duck 33864983 | FGFR3/Ihh-PTHrP disruption 31731208 | water/dental/environmental | **yes** |
| 151 | Burosumab (anti-FGF23) | ↑ (restoration in XLH) | Human toddlers: prevents further height deficit 41026619; meta 39211452; alignment 40511857 | restores phosphate for mineralisation | approved | no |
| 152 | Asfotase alfa | ↑ (restoration in HPP) | Human 27699270; systematic review 39089608 | replaces TNSALP, clears PPi | approved | **yes** |
| **P. RETINOIDS AND VITAMINS** |
| 153 | **Isotretinoin** | ↓ **premature epiphyseal closure** | **Human: growth plate arrest after high-risk neuroblastoma therapy 32386124; genu varum case 32425129; review 34626532**; bone effects 11606950 | RAR agonism drives premature physeal fusion | approved; heavily prescribed to adolescents for acne | no |
| 154 | Etretinate | ↓ | **Human children: premature epiphyseal closure 3805366** | RAR agonism | withdrawn | **yes** |
| 155 | Acitretin | ↓ (class) | Human bone toxicity in children 2523875 | RAR agonism | approved | **yes** |
| 156 | **Palovarotene (RARγ agonist)** | ↓ **premature physeal closure** | **Juvenile FOP mice: pronounced skeletal toxicity 30226468**; maintains limb mobility 26896819; history 39677926 | RARγ agonism; the labelled harm is premature growth-plate closure | approved (Sohonos) | **yes** |
| 157 | Tretinoin / bexarotene | ? | No physeal endpoint retrieved | RAR/RXR | approved | **yes** |
| 158 | **RARγ ANTAGONISTS (e.g. CD2665, compound "7C")** | 0 on length | No normal-animal length gain found in the external literature this session | ligand-less repressor logic | preclinical | **yes** |
| 159 | Hypervitaminosis A | ↓ | **Calves: vitamin A+D induced premature physeal closure ("hyena disease") 9179748**; condylar model PMC-only | retinoid excess closes physes | n/a | **yes** |
| 160 | Vitamin D supplementation (replete children) | 0 on linear growth | **Cochrane: oral vitamin D under 5 yr 33305842**; D-pro RCT 34581765; Finnish cohort 21430256; CXM biomarker 35838180 | adequacy matters; excess does not add height | OTC | no |
| 161 | Calcitriol / active vitamin D in CKD | ↑ (restoration) | Rat uraemic plate 12506147, 9853253; intermittent vs daily + GH 15728789 | suppresses 2° HPT | approved | **yes** |
| 162 | Vitamin K2 / menaquinone-7 | ↑ (observational) | **Human: longitudinal height growth patterns on MK-7 supplementation 42356365**; K2 deficiency and short stature cross-sectional 39740283 | γ-carboxylation of osteocalcin/MGP | supplement | **yes** |
| **Q. RESPIRATORY, GI, ALLERGY** |
| 163 | Montelukast | 0 on growth | **Human placebo-controlled short-term growth vs budesonide 17659605** | CysLT1 antagonism; the non-steroid comparator | approved | **yes** |
| 164 | Theophylline | ↓ GH secretion | Human asthmatic children 8919920; vs beclomethasone 8516087 | adenosine antagonism / PDE inhibition | approved | **yes** |
| 165 | PPIs and H2 blockers | ? | No paediatric linear-growth endpoint retrieved; B12 in CF 11593135 | hypochlorhydria → mineral/B12 malabsorption | approved OTC | **yes** |
| 166 | Antihistamines (cetirizine, loratadine, hydroxyzine) | 0 | **Human ETAC: long-term cetirizine safety in very young children 10452767** | H1 antagonism | OTC | **yes** |
| 167 | Allergen immunotherapy | ? | No growth endpoint retrieved | immune modulation; steroid-sparing is the plausible route | approved | **yes** |
| 168 | Laxatives (senna, PEG) | ? | Paediatric dosing 41951122; rat lipid absorption null 23013930 | malabsorption is the theoretical route | OTC | **yes** |
| 169 | Cholestyramine / bile-acid sequestrants | ↓ (predicted) | Human paediatric FH 8757561; absorption 1168607 | fat-soluble vitamin (A, D, K) malabsorption | approved | **yes** |
| **R. FGFR3 / CNP AXIS — THE DELIBERATE LENGTHENING SHELF** |
| 170 | **Vosoritide (CNP analogue)** | ↑ | Human systematic reviews 42026358, 41934413; real-world 42518139, 42238253; RASopathy/ACAN/NPR2 basket 41967490 | NPR-B→cGMP→PKG inhibits MAPK below FGFR3 | approved | no |
| 171 | **Navepegritide (TransCon CNP)** | ↑ | **Human APPROACH RCT 41247754; ACcomplisH phase 2 37823031; first approval 42234372**; +lonapegsomatropin COACH 42144862 | weekly CNP prodrug | approved 2026 | no |
| 172 | **Infigratinib (oral FGFR1-3 TKI)** | ↑ | **Human PROPEL 3 phase 3, NEJM 42370681; phase 2 NEJM 39555818; hypochondroplasia 40581757; mouse 38590263** | FGFR3 kinase inhibition | phase 3 complete; filing | no |
| 173 | **Dabogratinib / TYRA-300 (FGFR3-selective)** | ↑ | **Mouse: promotes bone growth in two FGFR3-driven chondrodysplasia models 40178985**; discovery 39258897; clinical 41084837 | isoform-selective FGFR3 inhibition | phase 2 | **yes** |
| 174 | Erdafitinib (pan-FGFR TKI) | ↑ (off-label reports) | Human paediatric dermatologic AE 41936429; no controlled growth trial | pan-FGFR1-4 | approved (oncology) | **yes** |
| 175 | **Meclozine / meclizine (repurposed antihistamine)** | ↑ | **Mouse ACH: promotes longitudinal bone growth 28785080, 25456072; human phase 2 41326861; phase 1b 37428729; +GH 39514089; XLH 36569439** | suppresses FGFR3→MAPK | OTC antihistamine, repurposed | **yes** |
| 176 | Recifercept (soluble FGFR3 decoy) | ↑ (preclinical) | Mouse 33370388; synchondroses 35229060; **juvenile cynomolgus toxicity study 36367445** | ligand trap | development discontinued | **yes** |
| 177 | RBM-007 (anti-FGF2 RNA aptamer) | ↑ | **Mouse: restores defective bone growth in FGFR3-related dysplasia 33952673**; 34203430 | sequesters FGF2 upstream of FGFR3 | preclinical/clinical | **yes** |
| 178 | Statin (as an FGFR3-dysplasia agent) | ↑ (model only) | **Mouse + patient iPSC 25231866 (Nature)** | promotes degradation of mutant FGFR3 | approved (other indication) | **yes** |
| 179 | CNP analogue + bisphosphonate combination | ↑ | **Growing OI mice: enhanced bone growth 41378917** | additive on two different terms | preclinical | **yes** |
| **S. SUPPLEMENTS AND NUTRACEUTICALS SOLD FOR HEIGHT** |
| 180 | L-arginine | ↕ | **Human RCT prepubertal low-normal height (PMC-only, 2026)**; meta-analysis in ISS 41908342; Copenhagen school-child cohort 23046689; acute GH blunted by exercise 24225560 | NO / GH secretagogue at high dose | supplement | **yes** |
| 181 | L-ornithine | ↑ GH (rodent) | **Mouse: oral L-ornithine raises GH via ghrelin receptors 35896372, 28513740** | ghrelin-system-dependent GH release | supplement | **yes** |
| 182 | Lysine | ↑ in deficient diets only | Human infant wheat-diet supplementation 6795322 | limiting amino acid | supplement | **yes** |
| 183 | Glutamine | 0 / restoration | Human alanyl-glutamine RCT 32826717; shantytown children 24714829; CF + GH 12373009 | gut barrier; not a plate lever | supplement | **yes** |
| 184 | **GABA** | ↑ GH (rodent) | **Mouse: long-term GABA raises ghrelin and GH, regulates growth 40431374**; USP safety review 34444905 | ghrelin/GH axis | supplement | **yes** |
| 185 | Zinc | ↑ in deficiency | **Human: zinc-deficient short children, growth velocity 8320627**; meta 21501440; +vit A on IGF-1/bone age 25439136; 24829711 | cofactor; IGF-1 dependent | supplement | no |
| 186 | Calcium | 0 on height (replete) | Human maternal supplementation follow-up 38839195, 28583879; +zinc in GHD 23224626 | mineralisation, not elongation | supplement | no |
| 187 | **Collagen peptides / collagen tripeptide** | ↑ (rodent) | **Rat: hydrolysed collagen tripeptide promotes longitudinal bone growth via IGF-1/BMP 37862561**; **porcine gelatin hydrolysate 23631489** | raises IGF-1 and BMPs | supplement | **yes** |
| 188 | **Taurine** | ↑ (rodent, malnutrition) | **Mouse protein malnutrition: taurine enhances linear bone growth 25963419** | restoration, not elevation | supplement | **yes** |
| 189 | **Soy isoflavones** | ↑ (rodent) | **Growing female rats: improves longitudinal bone growth and bone quality 28359365** | phyto-oestrogen; note the fusion trade-off | supplement | **yes** |
| 190 | **Astragalus extract mixture HT042** | ↑ | **Human RCT, mild short stature 29130588**; **rat: increases longitudinal bone growth rate via circulating IGF-1 28713437**; dexamethasone rescue 39064775 | raises circulating IGF-1 | licensed functional food (Korea) | **yes** |
| 191 | **Eucommia ulmoides extract** | ↑ (rodent) | **Adolescent female rats: longitudinal bone growth rate, plate height, BMP-2 and IGF-1 25087723** | BMP-2/IGF-1 | herbal | **yes** |
| 192 | **Icariin (Epimedium)** | ↑ (avian model) | Chicken tibial dyschondroplasia recovery 29988477, 29527166; glucocorticoid-induced bone loss 26221270 | BMP-2 / WNT4 / VEGF upregulation | herbal | **yes** |
| 193 | **Probiotics** | ↑ (rodent + human trials) | **Growing mice: promotes bone development 42244361**; duck 42258054; severely malnourished infants RCT 36725893 | microbiome→IGF-1 axis | supplement | **yes** |
| 194 | Bovine colostrum | ↑ (in undernourished) | **Human 3-arm RCT, linear growth, India 42409313**; reviews 39770926, 34444709 | IGF-1 and growth factors in colostrum | supplement | **yes** |
| 195 | Deer antler velvet | ? (contains IGF-1) | **Human IGF-1 detected in commercial supplements 23996390**; 41459385 | exogenous IGF-1 of unknown oral bioavailability | supplement; a doping issue | **yes** |
| 196 | MSM (methylsulfonylmethane) | ? (chondrogenic in vitro) | MSC chondrogenesis 34090529; IL-1β protection 30316071; animal OA 23011466 | sulfur donor for GAG sulfation (unproven route) | supplement | **yes** |
| 197 | Creatine | ? | Paediatric/adolescent athlete review 37008451 | no plate mechanism proposed | supplement | **yes** |
| 198 | Ashwagandha (Withania somnifera) | ? | **No height endpoint in any species (queries returned only agronomy/sport)** | claimed GH/DHEA effects | supplement | **yes** |
| 199 | "HGH-boosters", height-formula blends | ? | Human preliminary herbal + BMD/height study 16220578; Chinese medicine acupoint study RETRACTED 37808125 | heterogeneous | supplement | **yes** |
| 200 | Alpha-ketoglutarate | ? | **No growth-plate endpoint (query returned 0)**; postnatal AKG improved plate morphology in dexamethasone-exposed pigs 23211309 | 2-oxoglutarate dioxygenase co-substrate (TET, KDM) | supplement | **yes** |
| **T. LIFESTYLE AND ENVIRONMENTAL EXPOSURES** |
| 201 | **Nicotine (smoking, vaping, NRT)** | ↓ | **Rat: acts on growth-plate chondrocytes via α7 nAChR to delay skeletal growth 19079602**; IGF-1 pathway 23454400; Snail/HDAC1/2 34245815 | direct α7 nicotinic receptor on chondrocytes | legal/illicit | **yes** |
| 202 | **Caffeine (energy drinks)** | ↓ | **Rat: impairs longitudinal bone growth via direct chondrocyte differentiation effect 27484046; dose- and time-dependent 26495862; puberty 41503445; review 32325753** | direct chondrocyte effect; adenosine receptors | ubiquitous in adolescents | **yes** |
| 203 | Alcohol | ↓ | Rat adolescent exposure, bone morphometry 42057340 | multiple; GH/IGF-1 suppression | legal | **yes** |
| 204 | Cannabis / THC / CBD | ? | **No adolescent height endpoint retrieved**; CBD bone scoping review 41595744; OVX rat null 41589111 | CB1/CB2 on bone cells | legal/illicit | **yes** |
| 205 | Lead | ↓ | Human, height indices in school children 33508259; windows of sensitivity 22284921 | competes with Ca²⁺; also delays puberty | environmental | no |
| 206 | Cadmium (± lead co-exposure) | ↓ | **Rat: altered growth plate and articular cartilage after chronic adolescent co-exposure 27423034**; zinc metabolism 32059372 | displaces zinc in bone | environmental | **yes** |
| 207 | Arsenic | ↓ | Human: plasma IGF-1 in children 24303053; NHANES mixture 40015175; +fluoride 17450237 | lowers IGF-1 | environmental | **yes** |
| 208 | Bisphenol A | ↕ | **Chicken in ovo: tibial growth plate histology 33991407**; neonatal low-dose rat physis 36779543 | xeno-oestrogen at the plate | environmental | **yes** |
| 209 | Phthalates, PFAS | ? | **No height-titled study retrieved for either** | endocrine disruption | environmental | **yes** |
| 210 | Microplastics (± tetracycline) | ↓ | **Young mice: impaired skeletal development via microbiota-gut-bone axis 41172752** | microbiome | environmental | **yes** |
| **U. MISCELLANEOUS AND OBSCURE** |
| 211 | **Deferoxamine** | ↓ **direct dysplasia** | **Human thalassaemia: bone dysplasia 1899759; platyspondyly in hypertransfused patients 8577502; MRI 8309753, 23563594** | chelates zinc/copper needed by plate enzymes; dose-dependent | approved | **yes** |
| 212 | Deferasirox / deferiprone | ↕ | Human paediatric endocrine complications 32131650; ENTRUST 5-yr safety 28296163 | iron chelation without the DFO physeal signature | approved | **yes** |
| 213 | **D-penicillamine** | ↓ (lathyrism) | **Rat foetal skeletal development 1143363; mouse limb-bud cell proliferation 867273; amphibian metamorphosis with BAPN 1085616**; elastin cross-link inhibition 2934220; neonatal mortality in mice 1564250 | aldehyde scavenger — blocks collagen/elastin cross-linking; antiproliferative in limb bud | approved | **yes** |
| 214 | Thalidomide | ↓ (embryopathy) | Human, updated pathogenesis 40198353; limb embryopathy 37226469 | cereblon neosubstrate degradation in the limb bud | approved (restricted) | no |
| 215 | Hydroxyurea (sickle cell) | ↑ / 0 | **Human African children, growth and puberty 41954645; Ugandan sibling-control 41053883; 25157002** | disease modification, not a direct plate effect | approved | **yes** |
| 216 | **Leptin / metreleptin** | ↕ | **Mouse: leptin stimulates aromatase IN THE GROWTH PLATE, limiting catch-up growth efficiency 29615477**; human paediatric lipodystrophy 28324110 | local aromatase induction — a plate-intrinsic oestrogen source | approved (lipodystrophy) | **yes** |
| 217 | Prostaglandin E1 (alprostadil) infusion | ↑ periosteal bone | **Human neonates: PGE1 periostitis/hyperostosis 9025848, 1776031**; dog 3592385 | EP4→periosteal bone formation | approved | **yes** |
| 218 | Misoprostol | ↑ (fracture healing) | Rat 17681893; OVX rat BMD 10410382 | EP receptor agonism | approved | **yes** |
| 219 | **Dynasore (dynamin inhibitor)** | ↕ **hormetic** | **Mouse metatarsal ex vivo: modulates longitudinal bone growth in a hormetic manner 42464284** | dynamin — endocytosis, mitochondrial fission | preclinical tool | **yes** |
| 220 | Resveratrol | ↑ **delays plate fusion** | **Female rabbits: delays growth plate fusion and improves bone growth 23840780**; COMPopathy 33778324; MTX bone loss 28282956 | VEGF/laminin suppression at the vascular invasion front | supplement | **yes** |
| 221 | Botulinum toxin | ↓ (local) | Rat mandibular bone growth 29588910; zebrafish bone regeneration 24806738 | mechanical unloading of the attached bone | approved | **yes** |
| 222 | Desmopressin / vasopressin analogues | ? | No linear-growth endpoint retrieved | V2 receptor | approved | **yes** |
| 223 | Tolvaptan | ? | ADPKD literature only; no paediatric height endpoint | V2 antagonism | approved | **yes** |
| 224 | Baclofen, dantrolene, muscle relaxants | ? | Baclofen raises GH acutely 21181128; no length endpoint | GABA-B; RyR | approved | **yes** |
| 225 | Melatonin (as a supplement, not radioprotection) | ↕ | Rat vertebral plate chondrocytes 23983601; AIS chondrocytes 25257530; Slc26a2 chondrodysplasia rescue 39759111 | MT receptors on chondrocytes | OTC supplement | **yes** |
| 226 | Sildenafil / PDE5 inhibitors | ? | **No growth-plate endpoint (query returned 0)** | cGMP — same second messenger as CNP but a different pool | approved | **yes** |
| 227 | **Cilostazol / PDE3 inhibitors** | ↑ | **"Phosphodiesterase 3 inhibitors boost bone outgrowth" 40456620 (2025; preprint PPR876462)**; cilostazol promotes vessel formation and bone regeneration in murine non-union 37864892; accelerates fracture healing in aged mice 38255829; class review 41732176 | PDE3 inhibition raises cGMP/cAMP in chondrocytes | approved | **yes** |
| 228 | Pentoxifylline (dual PDE3/4) | ? | 145 hits, none skeletal-longitudinal; class review 41732176 | non-selective PDE inhibition | approved | **yes** |
| 229 | Nitrates / sGC stimulators (riociguat, vericiguat) | ? | No growth-plate endpoint retrieved | soluble guanylyl cyclase — likely absent from the plate | approved | **yes** |
| 230 | Anaesthetics (sevoflurane, ketamine, propofol) | ? | No bone-growth endpoint retrieved for any | n/a | approved | **yes** |
| 231 | Hydroxychloroquine / chloroquine | ? | **No growth-plate endpoint (query returned 0)** | lysosomal | approved | **yes** |
| 232 | Eltrombopag | ? | 111 hits, none on longitudinal growth | TPO-R agonist | approved incl. paediatric | **yes** |
| 233 | Oligosaccharides / prebiotics | ↑ (rodent) | **Mouse: promotes leptin/POMC axis, accelerates short-stature growth, increased femur length 41421172** | leptin/POMC and IGF-1 | supplement | **yes** |
| 234 | **β-hydroxy-β-methylbutyrate (HMB)** | ↕ | Piglet: maternal HMB affects bone and hyaline cartilage via leptin/OPG 30659706; spiny mouse 33802646 | leptin/OPG system | supplement | **yes** |

**Row count: 234. Marked OBSCURE: 182. Not obscure: 52.** (Numbering verified contiguous 1–234, no
duplicates, no gaps.)

---

## PROSE 1 — EVERY AGENT WITH A REPORTED INCREASE IN LONGITUDINAL GROWTH IN ANY SPECIES

Grouped by how much the claim is worth. Species is stated for every entry.

### 1a. Approved human agents with a randomised or controlled adult-height/velocity gain
- **rhGH and long-acting GH analogues** (human) — the reference case; ISS adult-height meta-analyses 21398350, 33035189; somapacitan in Turner 42538806.
- **Aromatase inhibitors, anastrozole and letrozole** (human) — 39262574 (3-yr randomised head-to-head), 38018388, 38723894, 39492684. These buy *period*, not rate.
- **Oxandrolone** (human) — Turner RCT 21493672 with final analysis 31862699; meta-analysis 26322078; trans-masculine youth 33819432. Notably it is **systemic**: the same molecule is null on cultured rat metatarsals (19258714), so it does not act at the plate.
- **Testosterone, low dose, in constitutional delay** (human) — 12608930, 8961126: brings the spurt forward without an adult-height penalty.
- **GnRH analogues in true central precocious puberty** (human) — 42130798, 39703867, 26528763, 23485026.
- **Vosoritide** (human) — 42026358, 41934413, 41967490 (now extending beyond achondroplasia into RASopathies, ACAN and NPR2 deficiency).
- **Navepegritide / TransCon CNP** (human) — APPROACH RCT 41247754; ACcomplisH 37823031; first approval 42234372; combined with lonapegsomatropin 42144862.
- **Infigratinib** (human) — phase 3 NEJM 42370681, phase 2 NEJM 39555818; also effective in hypochondroplasia at low dose 40581757.
- **Meclozine** (human phase 2 41326861, phase 1b 37428729; mouse 28785080, 25456072) — an OTC antihistamine repurposed onto FGFR3.
- **Burosumab** in XLH (human 41026619) and **asfotase alfa** in hypophosphatasia (human 27699270) — restoration of a specific mineralisation defect.
- **Anti-cytokine biologics as restoration**: infliximab 29298460/24865777, adalimumab 28301428, etanercept 18050366, tocilizumab 29961686, canakinumab 37658934. Every one of these is catch-up in an inflamed child, not elevation in a healthy one.
- **Metformin** (human) — 26414449 meta-analysis, 16492692 RCT; but see the direct methodological challenge 27110658/27110870, which argues the control groups were mis-specified.
- **Azithromycin, mass administration** (human) — 34967883, 42268611, 41285436: a linear-growth gain in undernourished populations, i.e. infection-burden removal.

### 1b. Preclinical agents that lengthen bone, including in NORMAL animals
- **Dabogratinib / TYRA-300** (mouse) — 40178985: promotes bone growth in two FGFR3-driven chondrodysplasia models. The isoform-selective FGFR3 inhibitor.
- **RBM-007 anti-FGF2 aptamer** (mouse) — 33952673.
- **Recifercept, soluble FGFR3 decoy** (mouse) — 33370388, 35229060; juvenile cynomolgus toxicology 36367445.
- **Statin** (mouse + patient iPSC) — 25231866 (Nature): rescues FGFR3 skeletal dysplasia phenotypes.
- **CNP analogue + bisphosphonate** (growing OI mice) — 41378917.
- **Resveratrol** (female rabbit) — 23840780: **delays growth plate fusion** and improves bone growth. One of very few agents reported to move the *period* in a non-dysplastic animal.
- **Calcitonin** (rat/chick) — 3987614: stimulates maturation of growth plate cartilage.
- **Amifostine** (rat) — 10814957: dose-responsive **protection** of growth plate function from irradiation. Melatonin does the same (14521636, 18979313).
- **Celecoxib** (rat) — 17437166: prevents growth-plate destruction adjacent to inflamed joints.
- **Lithium** (rat metatarsal) — 38684886: rescues dexamethasone-induced growth failure.
- **Losartan** (mouse) — 25779879: increases bone mass and **accelerates chondrocyte hypertrophy** in the developing skeleton. Direction on final length is not established.
- **Dynasore** (mouse metatarsal ex vivo) — 42464284: **hormetic** — increases growth at one concentration band and not others. The most explicit dose-shape result in the set.
- **Prostaglandin E1** (human neonate, dog) — 9025848, 1776031, 3592385: periosteal new bone, not longitudinal.
- **PDE3 inhibitors, cilostazol class** (mouse) — **40456620, titled "Phosphodiesterase 3 inhibitors boost bone outgrowth"**; supported by cilostazol accelerating fracture healing and vessel formation 38255829, 37864892, and a 2026 review of PDE inhibitors as skeletal therapeutics 41732176. An approved oral generic with an explicit bone-outgrowth result.

### 1c. Supplements and nutraceuticals with a positive longitudinal-growth result
Everything here is either rodent, or a human trial in a deficient/short population.
- **Collagen tripeptide** (rat) 37862561 and **porcine gelatin hydrolysate** (rat) 23631489 — both titled "promotes longitudinal bone growth", both via IGF-1/BMP.
- **Astragalus extract mixture HT042** — human RCT in mild short stature 29130588; rat mechanism (circulating IGF-1) 28713437; rescues dexamethasone growth retardation in rat metatarsals 39064775. The best-evidenced height-marketed botanical.
- **Eucommia ulmoides** (rat) 25087723 — longitudinal bone growth rate, plate height, BMP-2, IGF-1.
- **Soy isoflavones** (growing female rat) 28359365 — but a phyto-oestrogen carries the fusion trade-off by construction.
- **Taurine** (mouse, protein malnutrition) 25963419.
- **Probiotics** (growing mice) 42244361; **oligosaccharides** via leptin/POMC with an explicit **increased femur length** in wild-type mice 41421172; human infant RCT 36725893.
- **Bovine colostrum** (human RCT, India) 42409313.
- **L-ornithine** (mouse) 35896372, 28513740 and **GABA** (mouse) 40431374 — both raise GH through the ghrelin system.
- **Zinc** (human, deficient children) 8320627, 25439136, 21501440.
- **Vitamin K2 / MK-7** (human, observational) 42356365.
- **L-arginine** (human, prepubertal low-normal height) — 2026 RCT is PMC-only in the index; meta-analysis in ISS 41908342.
- **Icariin** (chicken tibial dyschondroplasia) 29988477, 29527166.

### 1d. The one agent that lengthens by a mechanical rather than pharmacological route
- **Elbow/joint loading** (mouse) 21748461 — "promotes longitudinal bone growth of the ulna and the humerus." Included because it appeared in the same query set and is a genuine positive with a contralateral internal control.

---

## PROSE 2 — EVERY AGENT COMMONLY TAKEN BY ADOLESCENTS THAT SHORTENS

Ordered by how many adolescents are exposed.

1. **Glucocorticoids, every route.** Oral prednisolone/prednisone (30240629, 2202451), dexamethasone (12630918, 18067838), inhaled budesonide (16452586, 19298635), inhaled fluticasone (37728224 — least suppressive of the class), mometasone (21854342), ciclesonide (18070931), **intranasal** fluticasone furoate (25017530) and budesonide (16729787), and **topical** steroids (14513873). The single largest exposure in this domain. **Vamorolone** (36036925, 38335499, 42547787) is the one member of the class specifically engineered to spare growth, and the biomarker paper 42547787 shows prednisone but not vamorolone suppresses bone/cartilage biomarkers of growth failure.
2. **Methylphenidate and amphetamines.** Meta-analyses 42199906, 33080250; 24-month 35196830. Two mechanistic papers make this more than an appetite effect: **premature growth-plate closure in vitro 36835608** and reduced femoral bone growth in male rats 37903444. Lisdexamfetamine 29790103, 20215923.
3. **SSRIs.** **39392873** reports fluoxetine and sertraline inhibiting height growth and GH signalling during puberty in humans; **29958671** shows SSRIs reduce longitudinal growth in risperidone-treated boys. Juvenile rhesus 26067181, 29473029.
4. **Atomoxetine** 34217783, 29940719.
5. **Isotretinoin.** Heavily prescribed for adolescent acne. Premature epiphyseal closure documented in humans 32386124, 32425129, review 34626532. Etretinate did the same 3805366.
6. **Valproate, carbamazepine, phenytoin, topiramate, zonisamide, acetazolamide.** Valproate on longitudinal bone growth 15032379 and growth velocity 27142370; carbamazepine 20933174; acetazolamide **growth suppression in children** 8972532, 38983548, 42350680. Levetiracetam is the bone-neutral comparator 38959743.
7. **Caffeine and energy drinks.** Rat data are direct and dose-dependent: 27484046, 26495862, 41503445, 32325753.
8. **Nicotine — cigarettes, vapes, pouches.** Direct α7 nicotinic receptor action on growth-plate chondrocytes 19079602; IGF-1 pathway 23454400.
9. **Minoxidil, topical and oral.** OTC, near-ubiquitous in teenage boys for hair. Lysyl hydroxylase inhibition 30481795, weakens newly synthesised collagen 37605092, and a published caution that it cannot be used cleanly as an LH inhibitor in developing tissue 33020194.
10. **Anabolic steroids and SARMs bought online.** RAD140/ligandrol/ostarine have BMD data (40680216, 37407738, 37378829) and **no bone-length endpoint in any species** — and any aromatisable androgen advances bone age by construction.
11. **Fluoroquinolones.** Restricted in children for exactly this reason: immature dog cartilage 15014927, juvenile rat secondary ossification centres 15631371.
12. **Alcohol** 42057340; **opioids** 33985485.
13. **Paracetamol.** Ubiquitous; the sulfate-depletion route is mechanistically plausible (40910464, 40040359) but the specific human serum-sulfate result is a claim I could not attach to a PMID this session.
14. **Itraconazole and posaconazole** — prescribed for adolescent onychomycosis and tinea; both are Smoothened antagonists at ordinary antifungal exposure (42122264, 42085720, 39917616), which puts them in the same pharmacological class as vismodegib. Terbinafine and fluconazole return no hedgehog activity and are the substitutions.
15. **Givinostat** — approved 2024 for Duchenne, taken chronically by growing boys, and an HDAC inhibitor. **No growth-plate endpoint exists for it or for any HDAC inhibitor.** This is the most conspicuous unfilled gap in the table.
16. **Salbutamol** (acute GH suppression 8514982, 7869909) and **theophylline** (8919920).

---

## PROSE 3 — DRUGS WHOSE JUVENILE TOXICITY OR PAEDIATRIC LABEL RECORDS A LIMB-LENGTH OR SKELETAL ENDPOINT

This is the section the brief flags as invisible to PubMed, and it is largely correct: a
Europe PMC query for `TITLE:"juvenile toxicity" AND ABSTRACT:"femur length"` returns **one** record
(41603569, an antimalarial candidate in Wistar rats), and `ABSTRACT:"juvenile toxicity study" AND
ABSTRACT:"growth plate"` returns **zero**. The endpoints exist; they sit in regulatory documents.

**Confirmed via the published literature:**
- **Tofacitinib** — 35944741 is a *published* juvenile rat study explicitly titled around "the association between offspring growth and **femur length**", concluding no direct bone effect and that femur length tracked body weight. This is the clearest worked example of the design.
- **Baricitinib** — 41861528, juvenile rats: **JAK2 inhibition stunts growth and postnatal development.** JAK2 is the GH-receptor transducer, so this is a direct on-target hit, and baricitinib has paediatric indications.
- **Recifercept** — 36367445, a formally reported juvenile toxicity study in **2–3-month-old cynomolgus monkeys**.
- **Sunitinib** — 18981453, the nonclinical safety evaluation, reports **physeal dysplasia in cynomolgus monkeys with open growth plates**. This is the archetype for the VEGFR-TKI class.
- **Gepotidacin** — 36255258, juvenile rats, run specifically to demonstrate the **absence** of fluoroquinolone-like arthropathy. A negative control by design.
- **Denosumab** — 24727159, infant cynomolgus monkeys exposed in utero, osteoclast-poor osteopetrotic-like skeleton.
- **Zoledronic acid** — 21713986, preclinical study at an oncopediatric dosing regimen with an explicit bone-growth endpoint.
- **Palovarotene** — 30226468, juvenile FOP mice, "pronounced skeletal toxicity"; premature physeal closure is on the human label.
- **Venetoclax** — 37198212, which uniquely combines ATDC5 cells, rat metatarsals, **human growth-plate biopsies** and mice.

### ⭐ FDA PRIMARY DOCUMENTS RETRIEVED AND READ IN THIS SESSION

Three pharmacology/toxicology reviews were downloaded from `accessdata.fda.gov` and text-extracted.
None of these findings is indexed in PubMed. **Retrieval method, because it is the reusable part:**
query `https://api.fda.gov/drug/drugsfda.json?search=application_number:"NDA<n>"` to get the review
year from the submission record, then fetch
`https://www.accessdata.fda.gov/drugsatfda_docs/nda/<year>/<n>Orig1s000PharmR.pdf` with a browser
User-Agent and a `Referer: https://www.accessdata.fda.gov/scripts/cder/daf/` header. Default clients
get an Akamai interstitial that looks like a 404.

**1. DABIGATRAN ETEXILATE — NDA 022512 supplement 41 (paediatric), reviewer Victor Long.**
This is the archetype of the design the domain brief predicted, and it is NULL.
- GLP neonatal/juvenile toxicity study in **Han Wistar rats**, oral gavage, dosed from **PND 7**,
  **0 / 15 / 32.5 / 70 mg/kg/day**, once daily, 12/sex/group main phase + 20/sex/group recovery.
- **"Limb measurements. Methods: For main phase animals, the length of the left ulna was recorded on
  PND 14, 28, 42, 56, and at necropsy"** — and PND 70 and 84 additionally in the recovery phase.
- **Result: no effect on ulna length or growth in MALES at any dose, throughout treatment or
  recovery.** In females at 70 mg/kg/day there was one statistically significant reduction
  (**24.3 ± 1.9 mm vs 25.2 ± 0.55 mm control**) at **PND 28 only**; absent at every other timepoint,
  absent in the PND 14→56 change, and resolved by the end of treatment and recovery.
- Context that bounds it: mortality occurred in **all** dosage groups from on-target bleeding, so
  **a NOAEL could not be established**, and the reviewer's own key finding 4 reads "no clear effect
  on growth or development".

**2. AXITINIB — NDA 202324, reviewer Anwar Goheer.** The VEGFR class finding, with numbers.
- **"Toxicities in bone and teeth were observed in immature mice and in dogs… Effects in bone
  consisted of thickened growth plates in mice and dogs at ≥15 mg/kg/dose"** — approximately 6× (mice)
  and 15× (dogs) the human systemic exposure at the recommended starting dose.
- Incidence tables show a clean dose-response, e.g. **femur thickened growth plate 0/0/3/0/9 (males)
  and 0/0/1/2/9 (females)** across ascending dose groups; tibia 0/0/0/1/4 and 0/0/0/0/4. Rib growth
  plate thickening is tabulated separately.
- The reviewer states these toxicities **"are consistent with the activity of axitinib for inhibiting
  VEGFR, and should be considered when axitinib is administered to pediatric patients."**

**3. REGORAFENIB — NDA 203085.** Confirms the class generalisation in a second molecule and species.
- In dogs at the high dose: **"increased findings of persistent femoral epiphyseal growth plate
  compared to control… In some animals the growth plate was also thickened."**
- Also **"chondrodystrophy of the sternal symphyses"** and **"thickening of the epiphyseal growth
  plate with hypocellularity of the adjacent bone marrow."**
- ⭐ The load-bearing sentence is the reviewer's own class generalisation: **"These alterations are
  known to occur in growing dogs treated with VEGF inhibitors."** That converts the finding from a
  molecule fact into a class fact, in a regulator's words.
- Dentin/tooth alterations accompany it, exactly as in axitinib — the same "growing hard tissue"
  signature.

**Classes whose labels/reviews carry physeal findings but whose review PDFs I did NOT open**
(recorded as UNVERIFIED at document level; the class attribution is now supported by the regorafenib
reviewer's generalisation above):
- **Other VEGFR-directed agents** — pazopanib, sorafenib, sunitinib, bevacizumab, ramucirumab. Sunitinib's physeal dysplasia in cynomolgus monkeys with open plates IS published (18981453).
- **BMN 111 / vosoritide** — a clinicaltrials.gov protocol document surfaced in search states nonclinical findings were limited to the known CNP mechanism at the growth plate and vasculature, with promotion of longitudinal bone growth at hemodynamically tolerated doses.
- **Fluoroquinolones** — juvenile-animal arthropathy is the basis of the paediatric restriction across the class.
- **Hedgehog pathway inhibitors** — premature fusion of growth plates is a labelled warning for vismodegib and sonidegib.
- **Isotretinoin** — premature epiphyseal closure is in the labelled adverse-reaction set.

**The general regulatory rule** (from the FDA guidance *Nonclinical Safety Evaluation of Pediatric Drug
Products*, and ICH S11): a juvenile animal study is triggered by a safety signal in adults or by prior
class knowledge of potential to impair growth or developmental milestones. Where such a study is run,
serial limb length, body weight, sexual maturation and skeletal histopathology across the whole growth
period are routine endpoints. Two review articles indexed the landscape: 40237616 (juvenile animal
studies in US FDA prescribing information) and 21594977 (retrospective on their use in regulatory
decisions and labelling).

**A confound that governs the whole section:** several sources note that in juvenile rodent studies a
shorter femur commonly tracks lower body weight rather than a direct skeletal effect — 35944741 makes
exactly this argument for tofacitinib. **A length endpoint from a juvenile-toxicity review must be read
against body weight before it is read as a bone effect.**

---

## STRUCTURAL OBSERVATIONS FROM THE ENUMERATION

1. **The direction is asymmetric.** Of 234 rows, roughly 45 report an increase and roughly 90 a
   decrease; the rest are null, contested or unmeasured. Drugs are overwhelmingly built to suppress
   something, and growth is collateral.
2. **Almost every human "increase" is a restoration.** Anti-TNF, anti-IL-6, anti-IL-1, burosumab,
   asfotase alfa, calcitriol in CKD, insulin in T1D, azithromycin in undernourished populations, zinc
   in zinc deficiency, hydroxyurea in sickle cell, bromocriptine in prolactinoma — all catch-up in a
   deficit. The set of agents shown to raise growth **above normal in a normal animal** is very small:
   the FGFR3/CNP shelf, resveratrol in the rabbit, a handful of rodent nutraceuticals, and dynasore.
3. **Whole classes have no growth-plate endpoint at all.** HDAC inhibitors (including approved
   givinostat), DNMT inhibitors, EZH2 inhibitors, menin-MLL inhibitors, BET/LSD1/IDH inhibitors,
   checkpoint inhibitors, CAR-T, PDE5 inhibitors, PPIs, anaesthetics, muscle relaxants,
   hydroxychloroquine, SARMs, phthalates and PFAS. These are OBSCURE rows precisely because nobody
   looked.
4. **Three "same-class, opposite-direction" pairs are worth naming.** Fluticasone vs budesonide (both
   ICS, different systemic exposure). Vamorolone vs prednisone (same receptor, dissociated
   transactivation). Gepotidacin vs ciprofloxacin (same indication, one arthropathic and one not).
   Each is a natural experiment in which the confounder is held fixed.
5. **The retinoid and hedgehog axes are the two places where an approved drug reliably closes a human
   physis early** — isotretinoin/etretinate/palovarotene on one, vismodegib/sonidegib (and, at ordinary
   dose, itraconazole and posaconazole) on the other.

---

## WHAT I COULD NOT VERIFY

Recorded honestly, per the common brief.

- **FDA primary documents: THREE retrieved and read** (dabigatran NDA 022512 s041, axitinib NDA
  202324, regorafenib NDA 203085 — see PROSE 3). Everything quoted from those three is verified at
  document level. **Everything else attributed to a regulatory source is not.** Specifically NOT
  opened: pazopanib, sorafenib, sunitinib, bevacizumab and ramucirumab reviews; any EMA EPAR; any
  Health Canada or PMDA document. The sunitinib monkey finding is cited from the published paper
  (18981453), not from its review.
- **EMA EPARs were not searched at all.** The brief names them explicitly and this is a real gap:
  EU paediatric investigation plans often carry juvenile toxicity data that the US filing does not.
- **The paracetamol serum-sulfate figure.** The mechanism is coherent and the paracetamol-sulfation
  pharmacokinetics literature is real (40910464, 40040359), but I could not attach a PMID to the
  specific human result that an ordinary 1.5 g dose lowers serum inorganic sulfate by ~24%. Row 80's
  direction is therefore **predicted, not evidenced**.
- **RESOLVED ON RE-QUERY (three items I had first written as unverified — recorded because the
  first-pass failure is itself informative about indexing):**
  - *Cilostazol / PDE3.* `TITLE:"cilostazol" AND ABSTRACT:"bone growth"` returns **zero**, but
    `ABSTRACT:"cilostazol" AND ABSTRACT:"bone"` returns **40456620, "Phosphodiesterase 3 inhibitors
    boost bone outgrowth" (2025)**, plus preprint PPR876462 and a 2026 class review 41732176. The
    result was indexed under "bone outgrowth", not "bone growth". **A query that misses on vocabulary
    is still a failed query.**
  - *Rapamycin.* `ABSTRACT:"longitudinal bone growth"` returns zero but `TITLE:"rapamycin" AND
    ABSTRACT:"growth plate"` returns six papers including **17370095** ("retards growth and causes
    marked alterations in the growth plate of young rats") and **20555322** (growth retardation by
    disrupting growth-plate angiogenesis). Row 111 is now evidenced.
  - *Paracetamol and sulfate.* The human result exists and is old: **3732362 (1986)**, acetaminophen
    administration and body stores of sulphate; **1746133 (1991)**; rat PAPS depletion 2858374, 1602369.
    The specific "−24% at 1.5 g" figure is still not attached to a PMID by me, so row 80 states the
    depletion, not the percentage.
- **D-penicillamine human paediatric osteolathyrism.** Row 213 now carries rat foetal (1143363) and
  mouse limb-bud (867273) evidence. The *human paediatric* osteolathyrism-with-scoliosis case remains
  unattached to a PMID.
- **Conference abstracts.** LUM-201 (rows 5) rests on `J Endocr Soc` meeting abstracts (PMC11454631,
  PMC12545614, PMC11455403) with no journal PMID. Treated as index-level, not source-level.
- **Two 2026 records had no PMID in the index**: the L-arginine RCT in prepubertal children with
  low-normal height, and one Astragalus/arginine record. Both are marked PMC-only.
- **Reviews used as an index only, and flagged as such**: 34626532 (isotretinoin physeal closure),
  35895945 (fluoride and growth plate), 39677926 (palovarotene history), 40237616 and 21594977
  (juvenile animal studies in labelling), 41595744 (CBD and bone), 37008451 (creatine in adolescents).
- **Searched and genuinely empty** (queries returned 0 hits — these are informative negatives, not
  omissions): rosiglitazone/pioglitazone × bone growth; nandrolone × growth plate; doxycycline ×
  growth plate; gentamicin × growth plate; strontium ranelate × growth plate; sildenafil × growth
  plate; tazemetostat × bone; decitabine/azacitidine × chondrocyte; vorinostat/panobinostat × growth
  plate; trametinib × growth plate; pazopanib × growth plate; vandetanib × growth plate;
  chloroquine/hydroxychloroquine × growth plate; mineralocorticoid × growth plate; phthalate × height;
  perfluoroalkyl × height; DHEA × bone age; collagen peptide × growth plate; myo-inositol × bone
  growth; alpha-ketoglutarate × growth plate; cannabis × adolescent height; intranasal corticosteroid
  × growth (title-level); topical corticosteroid × growth suppression (title-level); levothyroxine ×
  final height (title-level); warfarin × growth in children (title-level); dabigatran × juvenile;
  CAR-T × children × height; orlistat × adolescent growth; isoniazid × pyridoxine × growth.
- **Not searched for lack of time**: individual EMA EPAR annexes; Health Canada and PMDA reviews;
  clinicaltrials.gov results-database skeletal adverse-event tables; veterinary growth-promoter
  literature beyond clenbuterol and ractopamine; the full traditional-medicine height-formula
  literature in non-English indices.
- **Copyright**: all entries are paraphrase. No article text is reproduced beyond short titles and,
  in PROSE 3, three short quoted phrases from US Government regulatory documents (not copyrightable).
- **PMID spot-check performed.** Fifteen of the most load-bearing PMIDs were independently
  re-resolved through NCBI eutils esummary and all fifteen returned the expected title and year:
  37198212, 41861528, 39392873, 36835608, 25231866, 40456620, 32386124, 30226468, 28785080,
  40178985, 23840780, 29130588, 19079602, 27484046, 21398350. The remaining ~450 identifiers were
  taken directly from live Europe PMC result objects in this session and were not individually
  re-resolved.
