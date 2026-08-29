# frontier/ — the adversarial branch

**Role.** A second researcher, working against the Human Growth System Atlas rather than inside it.
The atlas is a growth-plate atlas: its identity is `adult height = birth length + Σ_plates Σ_years
(velocity × duration)`, and 477 rounds have been spent finding the terms of that sum and the agents
that move them. This branch exists to ask the questions that identity cannot ask, and to bring
**instruments** the atlas does not have.

**Rules I inherit and will not break.** Every number here is read from a primary record or an API
response, never recalled. Every PMID was resolved live. A missing measurement is a gap, not a
disqualification. Restoration of a deficit is not elevation of a normal plate (CORR-203). A screen
without a base rate is a list, not a result (CORR-329). And before writing "nobody has done X",
I grep this repository first — the ledger is lossy in both directions (CORR-313 / CORR-352).

**Rule I add.** *Before proposing a new mechanism, ask what instrument would have seen it.* Every
structural negative in this repository — R298's druggability base rate, R437's FAERS blindness,
R457's one-sided regulatory record, CORR-295's disease-ascertainment bias — is a statement about an
**instrument**, not about biology. The fastest way to find something new is therefore not a new
target list. It is a new instrument.

---

## What is here

| file | what it is |
|---|---|
| `R001_paediatric_rct_height_screen.md` | **The round.** A new instrument, built and run: the ClinicalTrials.gov results database as a randomised, bidirectional, human height assay. Produces the first measured **base rate** for drug effects on paediatric linear growth, closes one open atlas gap with human randomised data, and lands one number the atlas's SCALE section does not have. |
| `R003_the_redox_ledger.md` | **The main result.** R436 measured an 825-concept blind spot, scored 199 of 866, filtered that with three criteria its own correction ledger forbids, and closed it. Working one unscored domain returns an axis absent from this atlas — selenium 0 files, selenoprotein 0, G6PD 0, oxidative protein folding 0, ferroptosis 0 nodes and 0 gaps — that lands on R459's named open question, on R454/R461's supply-limited matrix module, and on a 2025 *Nature Metabolism* paper whose first sentence is about **bone lengthening**. Proposes that the budget is a **redox ledger**, not a division counter — the only lever class that raises yield without raising rate. |
| `R005_the_ceiling_is_avascularity.md` | Six limits this atlas priced separately have one cause: the plate has no blood supply. The antler does endochondral ossification 365× faster in a vascularised niche. Plus a new local finding — the plate looks like a **cysteine auxotroph with the weakest importer on its own panel**. |
| `R006_the_hypertrophic_bottleneck.md` | **The current best answer.** Five independent lines converge on one cell; charge-without-discharge is shown to be *structural* (one exit, and it is the fusion mechanism); and the antler has a second exit. Corrects R005's Rung 4 against the operator-supplied primaries. |
| `R004_the_unscored_queue.md` | The other 667, opened and ranked: six length endpoints in normal animals already run and never scored, a second epigenetic axis, a second route to fusion, and a comparative argument that what imposes the limit is the **secondary ossification centre** — a structure this atlas already has a node for. |
| `R002_coverage_redteam.md` | **The negative space of my own search.** Forty-one out-of-the-box axes generated from first principles, each greped against this repository, each given a verdict. Thirty-four were already worked, several more deeply than I would have. Seven are genuinely open. Recorded so nobody re-derives them. |
| `ASKS.md` | What I need from the operator, ranked, with what each unlocks. |
| `screens/ctg_paediatric_rct/` | Code, raw harvest parameters and result tables. Re-runnable. |

## The two-paragraph summary

The atlas's own acquisition round (R18, 2026-08-06) downloaded 506 clinical trials with posted
height results and wrote that **269 of them are "natural experiments on human height that nobody has
aggregated."** They were never aggregated. This branch re-harvested the registry (841 trials, a
larger set than R18's), extracted every arm-level height contrast, and ran it. The extractor
reproduces the atlas's own hand-read positive control exactly (losartan 0.935 vs atenolol 0.822
cm/yr, NCT00429364) and recovers the known true positives (growth drugs and growth diagnoses: 35/37
positive in cm, median +0.99 cm; 11/11 positive in height-Z). Against that validated instrument,
drugs given to children for reasons unrelated to growth have a **median effect of −0.27 cm/yr and
−0.11 cm**, with only 22% of non-deficit contrasts positive. No new height-increasing lever appears.
What does appear is a **−1.7 cm, p = 0.030, 96-week randomised placebo-controlled human result for
selexipag** — the exact measurement the atlas's R457 said was missing, on a cAMP-raising agent, in
the direction that argues against the arm.


---

## The second summary — F-R003, and why F-R001 was the smaller half

F-R001 built a good instrument over a low-ceiling space: approved paediatric drugs, tested against
placebo, in indications unrelated to growth. It measured the base rate honestly and the base rate is
−0.27 cm/yr. **That space cannot contain a revolutionary answer, because a drug that made children
dramatically taller would not have stayed in a diabetes trial.**

F-R003 goes at the ceiling instead, and finds the crack in a different place: not in the biology, but
in the **coverage instrument**. R436 is the best thing in this repository for finding what nobody has
thought of — 21 external domain agents, 2,193 concepts, scored against the whole graph. It found 825
concepts the atlas had never once mentioned, then **scored 199 of 866**, filtered those with three
criteria (ACAN-level cartilage enrichment, ≥20 CPM in the plate, a recorded TALL direction) that
CORR-349, CORR-363, CORR-342, CORR-295 and CORR-344 each independently forbid, got four syndromes, and
recorded that the blind spot "does not hide an obvious missed compound."

**The unscored 667 are 97–100% of the mechanics, cell-biology, vascular-neural-immune and
intervention-landscape domains.** Working one of them returns the redox axis: the chondrocyte secretes
collagen at the plasma-cell ceiling (R454) in an avascular, transport-limited compartment (R448/R450/
R452), disulfide folding makes ROS, the plate pays it down through the pentose phosphate pathway,
glutathione and selenoprotein GPX4 — and when supply fails, the cell dies by a **non-apoptotic,
TUNEL-poor, necrosis-like, iron-driven** route that matches, exactly, the death morphology R459
assembled from three species and could not name. That axis has **no node, no gap and no question**
anywhere in this atlas. Its receiver passes the free local query in all four human donors — GPX4 is
detected in more cells than NPR2, the vosoritide receptor, in every one — and the zonal gradient
argues against the naive version of the model, which F-R003 reports rather than smooths.


---

## The third summary — F-R012, and the retraction of F-R006 through F-R011

Rounds F-R006 through F-R011 built one thesis: *charge without discharge*. The plate can make matrix
faster than it can clear it; the hypertrophic chondrocyte has exactly one exit and that exit is the
fusion mechanism; therefore unjamming the discharge should buy length. F-R011 compressed it to
`Growth = SYNTHESIS × DISCHARGE, and OXYGEN sets both`.

**F-R012 retracts it.** Stegen 2019 (Nature) ran that experiment in vivo, in both directions, with a
ruler on the tibia, and printed the answer in an Extended Data p-value list that the abstract does
not mention:

- Over-modifying a **wild-type** growth plate with dimethyl-αKG raised hydroxyproline, COL2⁺
  cartilage remnants and trabecular bone volume — and **did not change tibia length at all.**
- Un-jamming a wild-type plate with the GLS1 inhibitor BPTES **shortened the tibia at p = 1×10⁻⁷**,
  the largest length effect in the paper.
- In the PHD2-null mutant, BPTES **normalised** αKG, hydroxyproline, remnants and bone mass and
  **did not rescue length**. DCA — restoring glucose oxidation — **did** rescue length, at
  p = 1.2×10⁻⁴, while driving the remnants and the mineralised mass strictly *higher*.

**Matrix clearance is a mass valve, not a length valve.** Discharge failure diverts cartilage into
trabecular bone; it does not slow the plate's linear output. This kills the protease/cross-link/LOX
class as a height lever, confirms the atlas's αKG contraindication a second time, and explains the
entire Lublin pig corpus in one line — those are modification-arm interventions, so mass, density and
strength move and length does not.

What survives is the synthesis side: **length is a bioenergetic term, spent at prehypertrophy.**
Oohira 1974 localises it — collagen synthesis per cell is **17–20× higher** at the Zone 3/4 transition
than in the proliferative zone, in the same compartment where CORR-361 puts 44–59% of elongation and
where F-R008's bafilomycin result raised terminal cell height by 71%. And CORR-203 lands immediately
on the new candidate: DCA rescued a deficient tibia and did nothing to a wild-type one. Restoration is
not elevation. The open question the branch now carries is the one nobody has run — **raise
biosynthetic capacity at prehypertrophy in an animal that is not deficient, and measure the bone.**


---

## The fourth summary — F-R013, and the bug that ate the answer

The atlas's own blind-spot instrument found the best out-of-the-box height lead in this repository,
marked it with its highest flag, and lost it twice.

`atlas/data/round436/coverage.json`, row `NRF2 / KEAP1`: **"⭐ Nrf2 ACTIVATION stimulates chondrocyte
differentiation and INCREASES BONE LENGTHS in zebrafish"**, source `37748761`, `n_bib: 0`. The one
node that lifted it off ZERO mentions Nrf2 exactly once — in a sentence saying *metformin's* Nrf2
literature has no bone-length endpoint. A starred lead was down-ranked by a string match on a
sentence dismissing a different drug.

The systematic loss is bigger. **87 of the 2,193 rows carry a spreadsheet cell reference — `A10`,
`D15`, `G16` — in the `concept` field instead of a concept name**, with the real name surviving only
as a fragment spliced into the `note`. Every tier score on those rows was computed by grepping the
atlas for the cell reference. 53 came back ZERO because nothing contains the string "A17"; 27 came
back COVERED by matching a two-character substring (`E13` → a 325-node file). `MIA3/TANGO1` occupies
six rows and was scored COVERED four times and ZERO twice. **50 of the 87 are axial/trunk — the
operator's own residual compartment.** `frontier/screens/r436_recovery/recover.py` recovers the names
and re-scores: **55 of 87 verdicts flip.**

`coverage.json` also carries ⭐ on 112 rows, of which **31 never entered the bibliography**. Six of
those have a positive length endpoint and no node: NRF2 (+5.6% zebrafish), Serrat 2010 (*"all runners
had significantly longer limbs"*), McGarry 2024 (cyclic loading → longer tibiae), swimming (humerus
+2.8%), Romeo 2019 (endothelial proteolysis mediates elongation), PP5 ablation. Plus **FXYD2 /
Longshanks** (a selection line bred for long tibiae), **NFIX** (tall direction is the *loss*
direction), and the only genomic read-out of mechanical loading in **human** growth-plate cartilage
(PMID 39655393, ZERO, no node).

Read together they are one term. Cartilage has no vessels; it is perfused by convection driven by
cyclic loading. Five of those leads raise **delivery**; NRF2 raises **utilisation** — glutathione via
GCLC/GCLM, exactly the program F-R003 found the atlas has no node for and the plate looks starved of.
F-R012 reached the same term from the opposite direction: length is bioenergetic, spent at
prehypertrophy. **The plate is not signal-limited, it is supply-limited, and nobody has ever run the
transport arm and the utilisation arm together.**

Two corrections in this round. I withdrew last round's oxygen-tension ask as probably nonexistent;
**Brighton & Heppenstall 1971 (PMID 5580029, 5133323) is starred at ZERO in this repository's own
table** — including plate pO₂ measured distal to an arteriovenous fistula. And the pig rib anomaly
resolved without falsifying F-R012 (femur +1.1% ns, humerus +0.3% ns; the rib gained length with a
16% *thinner* wall and flat cross-section) — while handing over a contraindication the atlas does not
hold: **AKG raises plasma 17β-oestradiol 20% (p=0.002), and 158%/121% in Kowalik 2005a, with growth
retardation specific to males.**


---

## The fifth summary — F-R014, and the sign

I have had the sign of oxygen wrong for four rounds. F-R005 said "perfuse without ossifying";
F-R011 said `OXYGEN sets both`; F-R013 said the plate is supply-limited and left oxygen inside
"supply." **PMID 5133323 — the paper whose abstract is not deposited anywhere, recovered this round
from scanned page images — decides it, and the sign is negative.**

Brighton & Heppenstall 1971, femoral A-V fistula in 18 mongrel puppies, oxygen microelectrode with a
histologically burn-marked tip, contralateral limb as paired control. The fistula is the one
manipulation that lengthens a tibia in **100% of puppies**. Distal to it, plate pO₂ was
**significantly lower in every zone**, widening with time: ns at day 1, **P<0.01** at day 3 and week
1, **P<0.001** at week 3; cell columns −3.48% O₂ (t=−6.94), hypertrophic cells −1.00% (t=−6.32). In
the six dogs whose fistula closed, no difference. And it is not a consumption artefact — explants
going from dormant to log-phase growth showed identical pO₂ at day 0, 3 and 7.

Their conclusion: **Low O₂ → anaerobic metabolism → increased plate growth. High O₂ → aerobic
metabolism → decreased plate growth.** Two more dose-responses agree: less O₂ to explants gave *more*
bone formation (JBJS 1969), and the in vivo plate grows **5× faster at 4–5× lower pO₂** than the in
vitro plate. The same table is the pO₂ map nobody had read: proliferative zone **6–7% O₂**,
hypertrophic zone **2.0–2.2%**, between a 15% epiphysis and a 14% diaphysis.

`serrat2010` supplies the other arm and the control that makes it: wheel running raised fluorescein
delivery to the tibial plate **1.5×** and lengthened femur (P<0.001), radius, tibia and humerus,
while **tail length was unaffected** — local, not endocrine. `zhang2024` (n=3, the only
transcriptomic read-out of loading in human growth-plate cartilage) shows 30 seconds of cyclic load
remodelling the **tight-junction pathway, AQP9 up, AQP7 and SLC27A4 down** 24 h later — the transport
apparatus itself.

So the equation is **`Length ∝ (substrate delivery) × (glycolytic capacity)`, with pO₂ entering
NEGATIVELY.** An A-V fistula raises flow while shunting arterial blood past the capillary bed: more
volume, less oxygen. It is a device that does both of the things that lengthen a bone, and nothing in
the literature has ever done all three arms at once.

This also reconciles `stegen2019`, which I had been reading backwards: its PHD2-null chondrocytes
consumed *less* oxygen, "**making centrally localized chondrocytes less hypoxic**" — a less hypoxic
plate with a short tibia, exactly as Brighton predicts.

Two honest corrections. The atlas is **not** blind to delivery — `R450 the perfusion term` and
`local_limb_warming_is_a_free_delivery_and_growth_lever` already hold it well, and F-R013's
"supply-limited" claim was largely already this atlas's position. The real gap is narrow: the atlas
carries `brighton1971` as **`primary_abstract_only`** with the finding recorded as *"Oxygen tension
was measured by microelectrode"* — no numbers, no direction, no sign — and frames oxygen only as a
patterning cue. Nothing anywhere in the atlas says low oxygen increases growth rate. And
`yoshida2018` (Keap1-null NEKO mice: femur significantly shorter, P<0.05, but growth-plate thickness
unaffected and the lesion in osteoblasts) re-grades F-R013's NRF2 lead from best-in-repository to
dose-dependent with an unresolved mammalian direction.


---

## The sixth summary — F-R015, the 8% switch

I could not get `brighton1969` in full (JBJS Am 1969;51:1383–96, PMID 4186275). OpenAlex and Unpaywall
both flag it green OA with full text; **they are wrong** — the target is a Figshare record for
Brighton's *thesis* of the same title, with `files: []` and "In Copyright." LWW and Ovid return HTTP
402. But Semantic Scholar returned the paper's opening paragraph, two independent searches recovered
its abstract, and the abstract corrects F-R014:

> "**The cartilage portion of the epiphyseal plate exhibited maximum growth in 21 per cent oxygen,
> while maximum metaphyseal bone formation occurred in 5 per cent oxygen.** … in higher oxygen
> tensions, the cartilage portion showed narrowing, a progressive loss of acid mucopolysaccharide
> stainability, **eventual loss of the zone of hypertrophic cells**…"

In 1971 Brighton paraphrased this as "less oxygen → greater bone formation." True of *bone* — and he
omitted that his cartilage endpoint peaked at 21%. F-R014 inherited the selective half. **There is no
single sign. There is a threshold.**

Following the OA citing literature produced the keystone, which neither this branch nor the atlas
held: **Li, Oreffo, Sengers & Tare, Biotechnol Bioeng 2014;111:1876–1885.** Human chondrocyte pellets
generating their own oxygen gradients give a threshold at **pO₂ ≈ 8%**: *below* it "enhanced PG
deposition," *above* it "favor collagenous matrix production." **Oxygen does not set how much matrix a
chondrocyte makes. It sets which matrix.**

Against Brighton's 1971 in vivo map: secondary epiphysis **15.2%**, cell columns **6.0–7.0%**,
hypertrophic cells **2.1–2.2%**, diaphysis **14.0–15.2%**. **The growth plate is the only compartment
in the bone below the switch, and the bone on both sides of it is above.** The plate is a
proteoglycan-program slot cut into collagen-program tissue.

Proteoglycan carries the matrix's fixed charge; fixed charge draws water; swelling pressure is the
work that separates epiphysis from metaphysis (the atlas's own R448, "the matrix outpressures the cell
by 710-fold"); and terminal hypertrophy — CORR-361's 44–59% of elongation — is mostly water. So
**pO₂ < 8% → proteoglycan → osmotic swelling → hypertrophy → elongation; pO₂ > 8% → collagen → the
hypertrophic zone disappears.**

Six results collapse into that one statement: Brighton 1969's AMPS loss and vanishing hypertrophic
zone at high O₂; the A-V fistula driving every zone *deeper* below the switch and lengthening 100% of
limbs; `stegen2019`'s *less hypoxic* chondrocytes flipping to the collagen program (P4HA, PLOD, LOX,
pyridinoline up; tibia shorter, p=1e-8); Farquharson's 10-fold pyridinoline fall down the plate as the
descent through the gradient rather than de-cross-linking for discharge; Serrat's 1.5× solute delivery
feeding a running program; and F-R003's NADPH/PPP arm, which supplies UDP-sugars for GAG as well as
glutathione.

**The target is now specific: hold the plate below 8% pO₂ while flooding it with the substrates of
sulfated proteoglycan synthesis** — glucose (UDP-glucuronate, hexosamine pathway), sulfate
(PAPS/PAPSS2/SLC26A2), and NADPH. The atlas holds every part as disease genes and holds the osmotic
engine in R448, but `threshold oxygen` returns **0 files** and `UDP-glucuronate` returns **0**: its
oxygen node and its osmotic node have never been connected.

The deciding experiment is small and does not exist: metatarsal organ culture — the same assay
`newton2015`/`newton2018` used — run at 1/2/5/8/12/21% O₂, measuring **length, GAG and hypertrophic
zone height together**. 1969 measured the wrong endpoint; 2014 used the wrong cell.


---

## The seventh summary — F-R016, oxygen trades velocity against duration

Built `frontier/screens/brighton_recovery/cite_harvest.py`: resolve each Brighton paper in OpenAlex,
enumerate every citing work, pull full text for the OA ones, regex-scan for quantitative
restatements. **372 citing works, 71 open access, 13 restatements.** Two targets recovered, one
located, and a paper nobody here had seen falsifies F-R015.

**Recovered — `brighton1983` (PMID 6406512).** Rabbit rib growth plate, zones separated by a
purpose-built guillotine, fluorimetric assay: *"No glycerol phosphate dehydrogenase activity was
detectable in any zone of the growth plate, whereas control liver slices exhibited abundant enzyme
activity. Thus the glycerol phosphate shuttle… is entirely lacking in growth-plate chondrocytes."*
**Not low — absent, in every zone.** Obligate glycolysis by construction: giving this tissue more
oxygen does not give it more ATP, because the machinery that would convert the offer is not installed.

**Located — Brighton's thesis.** The "green OA full text" OpenAlex and Unpaywall both point at is a
Figshare record with an empty file list. Full metadata identifies it as **UIC's INDIGO repository,
handle `10027/14248`, Degree Grantor "University of Illinois at Chicago, Health Sciences Center,"**
with the field *"File(s) available to UIC only."* Robert D. Ray, second author on the 1969 paper,
chaired orthopaedics at Illinois. The file is catalogued and restricted, not lost — a document-delivery
or ILL request against that handle.

**Falsified — F-R015.** `leijten2012` (PLoS ONE 7:e49896, PMC3503827): fetal mouse tibiae, 21 days at
**21% vs 2.5% O₂**. *"Normoxia increased the length of the tibiae, length of the hypertrophic zone…
and mRNA levels of MMP9, MMP13, RUNX2, COL10A1, ALPL. Hypoxia increased the size of the cartilaginous
epiphysis, length of the resting zone… and ACAN, COL2A1, SOX9."* And: *"**hypoxia retains chondrocytes
in the resting zone while normoxia stimulates them to progress towards the hypertrophic zone.**"* That
replicates `brighton1969` on a real length endpoint 43 years later. The **matrix-program half of the
8% switch survives** (ACAN up in hypoxia, COL10A1 up in normoxia). My inference that the proteoglycan
program *drives elongation* dies — I had the osmotic mechanics right and the control logic backwards.

**The corrected model.** A 21-day explant has a fixed pool and no renewal, so only *velocity* is
observable, and 21% wins. A puppy with an open plate has months, so *duration* dominates, and the A-V
fistula's lower pO₂ wins. Same knob, opposite arms:

> **Oxygen does not set how fast a plate grows. It sets whether the progenitor pool is preserved or
> spent. High O₂ → differentiate now → velocity up, duration down. Low O₂ → stay resting → velocity
> down, duration up.**

That is the atlas's own `height = Σ (velocity × duration)` with a knob on the trade, and it settles
every conflict in the branch: Brighton's paradox (in vivo 5× faster at 4–5× lower pO₂ — because in
vivo the pool renews), `newton2019`'s resting zone collapsing 31.7→15.0 in controls while the Tsc1
mutant's grows 36.2→57.0, and `stegen2019`'s less-hypoxic chondrocytes spending faster into a
**shorter** tibia. CORR-203 in its sharpest form: an intervention that raises velocity in a closed
assay may be shortening the animal.

**So the target is sequential, not simultaneous: preserve the pool at low pO₂, then spend it at high
pO₂.** Every experiment in this literature holds oxygen constant and reports whichever arm its
timescale could see. Staged hypoxic-expansion-then-normoxic-differentiation is routine in stem-cell
manufacturing and has never been applied to a growth plate. In the metatarsal assay it is one extra
pipetting step, and it is the first question in this branch whose answer nobody can currently guess.


---

## The eighth summary — F-R017, growth that does not end is a cycle

**Retrieval closed out.** The Figshare OAI-PMH record for Brighton's thesis returns `In Copyright` /
**`Restricted Access`** in the metadata itself, and `/articles/10911983/files` returns `[]`. OpenAlex
and Unpaywall are both wrong to call it green OA. It is catalogued, restricted, and has no online copy
— UIC document delivery, ILL against handle `10027/14248`, or ProQuest. Stambough & Brighton 1980 has
20 citations and exactly one OA, which does not restate the data. The Internet Archive holds **no**
Surgical Forum volumes and only the JBJS 1969 *index*. Three ILL slips; the branch is no longer
blocked on them.

**The oxygen knob is now molecular, from two papers that have never been cited together.** Re-reading
`leijten2012` past its abstract: its Figure 4D is *"secreted **Wnt and BMP antagonists**"* and it
carries the heading **"Normoxia Reduces Frzb and Dkk1 Protein Levels"** — ELISA, not mRNA. And
`hallett2021` (eLife, PMC8313235) shows the resting-zone stem cell requires exactly that: LRCs are
enriched for Wnt *inhibitors*, non-LRCs for Wnt *activators*, and forcing Wnt on in PTHrP⁺ resting
chondrocytes (*Pthlh-creER; Apc*-fl) **"impaired their ability to form columnar chondrocytes."**
`zhang2018yap` adds the identity arm — hypoxia → HIF-1α → YAP (Hippo-independent) → SOX9/COL2 — and,
crucially, **reoxygenation reverses it.** A toggle, not a ratchet.

> **Low pO₂ → HIF-1α → YAP/SOX9 + Frzb/Dkk1/Grem1 → Wnt-inhibitory niche → pool preserved.
> High pO₂ → Frzb/Dkk1 protein falls → Wnt de-repressed → columnar/hypertrophic output → length
> produced, pool spent.**

**And that relaxes F-R007's impossible constraint.** F-R007 required `p ≥ 0.500` — the stem-daughter
renewal fraction — and found 0.392–0.493 across 36 combinations. But every one of those numbers comes
from an animal in a **constant** regime. Over a cycle of `N_E` expansion rounds at `p_E` and `N_S`
spend rounds at `p_S`, the pool returns to baseline when
`N_E·ln(2p_E) + N_S·ln(2p_S) = 0` — when the **geometric mean of `2p` over the cycle equals 1.**
Not `p ≥ 0.5` always; `p ≥ 0.5` on average.

> **Growth that does not end is not a state to be held. It is a cycle with net-zero pool balance,
> and height accrues one spend-phase at a time. Rate = spend-phase output ÷ cycle time — so "fast"
> and "unending" are set by different parameters and stop competing.**

This is why F-R014 and F-R015 kept inverting: each was hunting a single optimal oxygen tension for a
system whose two phases have opposite optima. `brighton1969` and `leijten2012` measure the spend
phase; the A-V fistula measures a system with its expansion phase intact. They were never in conflict.

**The named hazard is lactate.** `cih2025` (PMC12306074): chronic intermittent hypoxia inhibited long
bone growth via lactate → **H3K18 lactylation on the *PPARγ* promoter** → adipogenic shift in BM-MSCs,
partially rescued by T0070907. Different timescale and different compartment from the proposed cycle —
but `brighton1983` showed the plate has **no glycerol phosphate shuttle in any zone**, so its entire
redox balance leaves as lactate. Lactate clearance is a design parameter of the expansion phase, and
`serrat2010`'s convection carries it both ways.

**What would kill it:** a replicative or epigenetic clock in the resting-zone cell that runs
independently of `p`, so restoring pool *size* does not restore pool *capacity*. The 2026 PRISMA
systematic review of resting-zone quiescence (PMC13110114) says the field cannot currently settle it:
*"features of cellular quiescence in RZ chondrocytes remain poorly reported and underexplored."*
The framework is not proven — it is now specific enough to be wrong in a particular way.


---

## The ninth summary — F-R018, the clock counts divisions, and capacity is not conserved

F-R017 said the framework dies if the resting-zone cell carries a clock independent of `p`. **It does,
and it counts divisions, not time.** Nilsson & Baron: *"growth plate senescence occurs because the
progenitor chondrocytes in the resting zone have a limited replicative capacity which is gradually
exhausted with increasing cell division… senescence is a function of cell divisions rather than time
alone,"* and growth-inhibiting conditions *"conserve"* that capacity — which is why catch-up growth
exists. So a hold phase genuinely banks potential; that half of F-R017 is already validated across
species and decades. But an expansion phase that grows the pool **by division** spends the budget it
is trying to save, and F-R017 tracked pool *size* when what must return is *capacity*.

**The atlas got here first and graded the pessimistic answer E.**
`arm3_pool_ceiling_is_imposed_not_intrinsic.yaml` holds: the ceiling is **not Hayflick and not
telomeric** (C); the program is **epigenetically encoded**, not hormonal, not time (B); it is delayed
by anything that slows growth (B); and — *"INFERENCE, and the most consequential one in the node"* —
**"delaying is height-neutral rather than height-additive" (E)**, with the basis line *"no study has
run a full charge-then-discharge cycle to adult height and compared."* Two independent routes, same
gap, and the futility assumption is explicitly unproven.

**The arithmetic, which I think everyone has had backwards.** "Height-neutral" assumes a fixed
division budget. That holds only for purely differentiative divisions. For a per-cell counter `n`, a
symmetric self-renewing division gives `1×n → 2×(n−1) = 2n−2`, a **net gain of `n−2`** — positive for
every `n > 2`. The Hayflick budget is per *cell*; the pool's budget is the *sum*, and the sum grows
whenever a cell doubles rather than differentiates. So the entire question reduces to one measurable
property:

> **Per-cell counter, partitioned at division → expansion CREATES capacity → height-additive,
> unbounded while `n > 2`. Per-lineage program, inherited whole → expansion adds cells but not
> capacity → height-neutral, and the atlas's grade-E inference is right.**

**The one in vivo test is consistent with capacity addition.** `newton2024sag` (PMC11063944): SAG
beads in one rat femoral SOC, vehicle beads contralateral. The treated femur was significantly longer
at 1 month, *"an effect that was even more pronounced 2 and 6 months after implantation"* — tibia too,
growth rate up by calcein/xylenol, growth-plate height augmented, no OA at 6 months. And **"the signal
vanished within 3 weeks."** A stimulus gone by week 3 whose length advantage keeps widening at months
2 and 6 is not a velocity effect; it is capacity that was added once and kept paying out.

**And if it falls the other way, the clock is still resettable.** `stat3clock2023` (PMC9924946) built a
**DNA-methylation epigenetic clock across human chondrocyte ontogeny**, then showed a **small-molecule
STAT3 agonist decreased adult chondrocyte methylation** (STAT3 ablation hypermethylated), with
**DNMT3B** as the CUT&RUN-validated target. Plus local OSK delivery (PMC13049178, 2026). The ceiling
being epigenetic rather than telomeric is what makes a reset conceivable at all.

**The deciding experiment is one assay on tissue that already exists:** expand a resting-zone pool with
SAG, then measure the expanded pool's **mean methylation age** against the contralateral control on the
chondrocyte clock. Age up → per-lineage → neutral. Age flat while cell number rose → per-cell →
capacity was created → unbounded height is arithmetically available. The pool-expansion lab and the
clock lab have never cited each other.


---

## The tenth summary — F-R019, the constraint is topology, not chemistry

The atlas's objective function is `adult height = RESERVE × h_term`, with the exchange rate that a
division adds 8–9 µm at the cost of one unit of exhaustible reserve while the hypertrophy of the same
cell adds 40–50 µm free. Good model, real exchange rate — resting on **three unstated assumptions,
all of them false or untested.**

**A1 — the number of plates is fixed. False.** `PMC12678681` uses natural anatomical variation:
metatarsals form a plate at one end only, the pisiform is the only carpal with one, and the difference
*is* the reserve zone — *"at the opposite end, the absence of a PTHrP⁺ reserve zone results in premature
chondrocyte differentiation,"* and *"a pool of PTHrP⁺ reserve zone chondrocytes is a defining
characteristic of growth plates."* **A growth plate is a cell state, not an anatomical given.** The
atlas's own coverage table starred this — *"a growth plate is not guaranteed, it is specified"* — in one
of the 87 rows the spreadsheet bug destroyed.

**A2 — RESERVE has no influx. Untested, and the atlas names the gap then misses the answer.** R202:
*"where the extra cells come from is the whole question under a fixed reserve… extra cells from extra
divisions spend reserve; extra cells from delayed clearance do not. Nobody has measured which."* Two
options offered. **The third is recruitment.** The plate has a groove of Ranvier, a perichondrial ring
and an SOC-derived niche, and **`dReserve/dt = influx − outflux` has never had its first term measured
in any species.**

**A3 — h_term saturates. On the hormonal axis only.** GH 1.36×, NPR3 loss 1.20×, IGF-1 setting it — all
the same knob, *"sub-additive by construction."* But hypertrophy is **osmotic**, the atlas owns that
mechanics in R448, and F-R015/F-R016 showed proteoglycan deposition is oxygen-gated at ~8% pO₂. The
matrix route to h_term is orthogonal to a saturated axis and has never been tried.

**And the fact that reframes the clinic:** `PMC12685065` (2025) — **"GH reduces the pool of
slow-cycling, label-retaining stem cells by promoting their differentiation into transient
progenitors… leading to stem cell depletion,"** with renewal *"via population asymmetry"* (F-R007's
model, lineage-traced). **The standard height drug buys velocity by burning duration**, and above the
saturating h_term dose it is height-negative.

**The antler, read as topology.** Human plate: reserve is a **depot**, consumed one way, vascular
invasion terminates it, ~0.05 mm/day, ends once. Antler: reserve is a **flow** fed by the antlerogenic
periosteum — *"the only tissue responsible for postnatal antler formation"* — with **RXFP2⁺ MSCs**,
**vascularised cartilage**, two hypertrophic exits, ~20 mm/day, and **annual full regeneration
indefinitely.** Same chemistry. **The plate is a burning fuse; the antler is a flame. Nobody has tried
to attach a fuel line.**

**The cancellation theorem — why this whole field returns percentages.** `ba2025`: the antler's
periosteal stem cells are *"primarily activated by Wnt signalling."* `hallett2021`: the plate's
resting-zone stem cells are *maintained by a Wnt-inhibitory environment* and forcing Wnt on impairs
them. **The same signal recruits in the source compartment and depletes in the reserve compartment.**
Hedgehog does it too (SAG expands epSSCs and lengthens bone; Hh also drives resting-zone cells
osteogenic; R251 found discharge needs Hh *withdrawal*). So does GH. **Every intervention ever tried
was systemic, hit both compartments, and partly cancelled — which is why the only reliably large
effect in the literature, the A-V fistula at 100% of puppies, is the one that is inherently local.**
The route to large effects is **spatial, not chemical**, and `newton2024sag` is the accidental proof:
a bead in one femoral SOC, agent cleared by week 3, advantage still widening at 6 months.

The honest objective function is `H = Σ_plates ∫ h_term·outflux dt` with `dReserve/dt = influx − outflux`.
The atlas sets `influx = 0` and `Σ_plates` constant; with those the integral is bounded and conservation
is optimal. **Unbounded is `influx ≥ outflux`. Fast is `h_term × outflux` large. They are independent —
they only looked like a trade-off because influx was assumed to be zero.**


---

## The eleventh summary — F-R020, the reserve IS fed, and the gate has a name

F-R019 asserted `dReserve/dt = influx − outflux` had never had its first term measured, and asked for a
lineage trace across the perichondrial boundary. **That experiment was published eleven months ago,
open access, and I had not found it.**

**Rosello-Diez lab, Nat Commun 2025;16:10107 (PMC12627582).** Mosaic cartilage-targeted **p21**
overexpression (cell-cycle arrest), left limb only with a contralateral control, plus `Gli1-CreER` and
`Pdgfra-CreER` lineage tracing, snRNA-seq, clonal RGBow reporters and DTA ablation:

- **The plate compensates completely.** Followed to **P100**, past the end of growth: *"no major
  asymmetries in bone length"* — femur only ~1.5% short, despite a large fraction of cartilage being
  cell-cycle arrested.
- **The compensating cells come from outside.** *"Reparative Gli1⁺ cells originate from **Pdgfra⁺ cells
  outside the cartilage**, revealing the surrounding tissues as an unexpected CP source."*
- **It is demand-responsive** — *"the challenged cartilage signals to the surrounding tissues"* — and
  Pdgfra-lineage cells **in the resting zone** proliferate more under challenge.
- **It is necessary.** Ablating Gli1-derived chondrocytes on the p21 background significantly
  **shortened** the bone; ablating them in normal growth shortened femur and tibia at P100.
- The **groove of Ranvier** is quantified explicitly in their figures.

**A2 is falsified. `height = RESERVE × h_term` is missing a source term that is real and required.**
And this resolves F-R018 cleanly: a recruited stromal cell brings its **own unspent division counter**,
so influx adds capacity without touching the resident clock.

**The gate is CCN2.** Pseudobulk DE + MultiNicheNet found not hedgehog but **CCN2/CTGF, downregulated**
in challenged limbs, with *"p21⁺ chondrocytes generate a Ccn2-inhibiting area"*; and ex vivo human CCN2
on fetal femurs **downregulated Gli1 and reduced Ki67**. CCN2 restrains Gli1 activation in stromal
progenitors; when it falls, they convert and migrate in.

**And then the discipline paid off.** I drafted this proposing **pamrevlumab** (phase-3 anti-CCN2) as
the obvious agent — then greped, and found the atlas had **already killed CCN2** in R341: not in
kosmicki2026's 207, no IMPC length row, and *"the published Ctgf-null phenotype is an EXPANDED
hypertrophic zone with impaired angiogenesis — i.e. a DISCHARGE FAILURE… PAMREVLUMAB therefore points
the wrong way."*

**That kill stands. Both are right, about different compartments — and the collision is the cleanest
confirmation of F-R019's cancellation theorem yet.** Inside the cartilage CCN2 is a matricellular
coordinator and blocking it causes discharge failure (height-negative). Outside it, CCN2 restrains
Gli1 in Pdgfra⁺ stroma and blocking it recruits progenitors (height-positive). **One molecule,
opposite signs in adjacent compartments; a systemic antibody hits both and the discharge failure wins
— which is exactly what R341 measured.**

> **CCN2 is not a drug target. It is a delivery target.** R341's kill should be amended from *"CCN2 is
> not a lever"* to *"CCN2 is not a **systemic** lever; its intracartilaginous arm is a discharge-failure
> contraindication and its stromal arm is the only measured controller of progenitor influx."*

**The limit I am not hiding:** all of this is fetal/perinatal mouse, and the compensation *restored*
normal length rather than exceeding it. The demonstrated influx is **homeostatic** — it defends a set
point. Whether that set point can be raised is now a question about a named molecule in a named
compartment, which is a different kind of question from the one F-R019 was asking.

Supporting chain, four species and four decades, never assembled before: **PMID 16652202** (2006,
chick) lacZ-labelled LaCroix-ring cells re-injected into the ring were found *"arranged horizontally
along parts of the physis"*; **PMID 19563472** (2009, rabbit) the groove of Ranvier is a **stem cell
niche** with label-retaining Stro-1⁺/Jagged1⁺/BMPr1a⁺ cells; **PMC3854713** (2013, rabbit) BrdU and
Fe-nanoparticle tracing shows *"a gradual migration of cells"* from niche into cartilage; **PMC12627582**
(2025, mouse) closes it with genetics.


---

## The twelfth summary — F-R021, Hedgehog is the throttle and the groove of Ranvier is the valve

Both operator-supplied papers deliver, and they close a chain across 2006→2025, four species, five
papers that do not cite each other.

**`karlsson2009` (rabbit, BrdU 12 d + chase to 56 d).** Label-retaining cells persist in the germinal
zone while *"no positive cells could be detected in the proliferative or hypertrophic zone."* The
groove of Ranvier is a bona fide niche — **Stro-1, Patched, Jagged1, BMPr1a, N-cadherin**, with
*"cells in the growth plate directly adjacent… **did not express these markers**"* and Jagged1 forming
*"a distinct boundary."* And the sentence the authors buried: *"**Interestingly, a more abundant
expression of BrdU-positive cells was detected in the growth plate near the perichondrial groove of
Ranvier compared to centrally in the growth plate at later time points.**"* **A gradient of
label-retaining cells inside the plate, highest at the rim — the spatial signature of influx, which a
sealed depot spending itself uniformly has no reason to produce.**

**`fenichel2006` (chick).** Ring-of-LaCroix cells, adenoviral-lacZ labelled and re-injected into the
ring, were found 4 weeks later *"arranged horizontally along parts of the physis,"* their Fig. 5
showing *"migration of the cells from the periphery **transversely through the physis**."* Plus the
loss-of-function context: **excision of the ring causes growth arrest and short stature** (Rodriguez
1985), and human **Salter-Harris VI** injuries to the perichondrial ring cause growth arrest.

**The join is PATCHED.** `PTCH1` is the Hedgehog receptor and direct upstream of `GLI1`. So the groove
is **Hh-responsive tissue immediately outside the plate** — and F-R020's Nat Commun paper showed
**Gli1⁺ stromal cells outside the cartilage** are the long-lived chondroprogenitor precursors, required
for normal bone length, braked by CCN2. **PTCH1 in the groove and GLI1 in the recruits are the same
pathway one step apart: Hedgehog is the throttle on influx and the groove of Ranvier is the valve.**

**This reinterprets `newton2024sag`.** Its authors read it as expansion of epSSCs *inside* the plate —
but they delivered SAG from a bead in the secondary ossification centre, adjacent to where the Hh
receptor actually concentrates, and a length advantage that keeps widening long after the agent cleared
is what **recruitment** looks like, not a transient proliferative push. And it explains why Hedgehog
reads contradictory across this literature: Hh drives resting cells osteogenic *inside* the plate
(PMC10906233), discharge needs Hh *withdrawal* (R251), and Hh *recruits* outside. **F-R019's
cancellation theorem, third confirmation. `newton2024sag` got a large compounding effect because a bead
is not systemic.**

**Credit where due:** the atlas's `groove_of_ranvier.yaml` already grades this `confidence: C` and says
its function *"supplying cells for latitudinal growth — rests on rabbit morphology and **has never been
tested by lineage tracing in any species**."* It flagged the gap. What it lacks is the evidence:
`Fenichel` returns **0 files**, and `karlsson2009` exists here only inside a downloaded review's
reference list.

**The remaining uncertainty is one caliper measurement.** If the groove is latitudinal-only, influx
exists but buys width. The deciding experiment: local Hh agonist **at the groove** (not the SOC),
contralateral control, perichondrial lineage label scored for entry into the **PTHrP⁺ resting zone**,
and **length and width measured separately to skeletal maturity.** Nobody has ever reported both from
the same animal — and **Rodriguez 1985's ring-excision study may already contain the answer.**


---

## The thirteenth summary — F-R022, the pool-expanding levers are all tumour suppressors

**Three corrections.** (a) I gave the wrong DOI last round — `10.1007/BF02554932` is `caraceni1985`
(bromocriptine, Calcif Tissue Int 1985;**37:687–689**), which is why that is what arrived. Rodriguez is
ten pages earlier in the same issue: **PMID 3937595, DOI `10.1007/bf02554930`, 37:677–683.**
(b) **Its abstract refutes the claim I built on.** Excision of the perichondrial ring gave *"an
enlargement of the growth plate at the exposed surface that grew in an abnormal direction… and bending
of the bone,"* supporting *"the role of the perichondrial ring in the **mechanical constraint** of the
growth plate."* **It did not arrest growth.** `fenichel2006`'s "removal causes growth arrest and short
stature" is unsupported by the literature it points at — and F-R021 had already noted its citation
keying was unreliable. **The loss-of-function leg of the influx argument is withdrawn**; the positive
evidence (label-retention gradient at the rim, labelled cells crossing the physis, `rosellodiez2025`'s
genetics) is untouched. (c) The SAG-bead paper is **`trompet2024`**, not the label I had been using.

**One new positive.** Rodriguez's companion paper (**PMID 4064411**, Clin Orthop 1985;201:251–258):
150 r focused on the perichondrial groove **"induced the formation of a chondrocyte nest at the
proximal external edge of the growth plate,"** which then **"underwent endochondral ossification."**
A focal insult to the groove builds a cartilage engine outside the plate — the classical origin of
osteochondroma. `chondrocyte nest` returns **0 files** in the atlas.

**The convergence.** The atlas's `the_stack_in_a_normal_human.yaml` says *"**mundy2026** localises the
osteochondroma progenitor to the **PDGFRα-positive inner perichondrium**, the population this atlas
nominated for recruitment."* That is the same cell `rosellodiez2025` shows entering the plate and
being required for normal bone length, and the same compartment Rodriguez irradiated. **One population:
recruited into the plate it restores growth; released without control it builds an ectopic engine.**

**And the ceiling, which the atlas named before I did:** *"**EVERY KNOWN POOL-EXPANDING LEVER IS A
TUMOUR SUPPRESSOR.** PTCH1 loss gives Gorlin syndrome. TSC1/TSC2 gives tuberous sclerosis… PTEN and
DEPDC5 [in a 37-patient tall-stature cohort] are both tumour suppressors… **AN EXPANDABLE SELF-RENEWING
PROGENITOR POOL IS WHAT A TUMOUR IS**… that is why no pharmacological pool recruiter exists: the obvious
molecules are the ones oncology spends its effort BLOCKING."* That is deeper than "delivery is the
problem," and it was here first.

**The dose–response it implies is the actual answer.** Same Hedgehog/pool axis, three exposures:
chronic germline (PTCH1→Gorlin; EXT1/2→hereditary multiple exostoses, whose carriers are **short**) →
tumours and lost height; chronic systemic → oncogenic risk plus F-R019's cancellation; **transient
local pulse (`trompet2024`: signal gone by 3 weeks, divergence widening to 6 months, no OA) →
positive and compounding.** The atlas reaches the identical prescription — *"a pulse rather than a
chronic state, delivered into one anatomical compartment"* — from tumour-suppressor genetics while this
branch reached it from the cancellation theorem. **Two routes, one answer; the atlas's was deeper.**
What F-R019–F-R021 add is why the pulse must also be *spatially split*, and where the valve is
(PTCH1⁺ groove of Ranvier). And **osteochondroma bounds the risk**: over-driving this axis does not
merely risk cancer, it **costs height**, because an ectopic engine competes with the plate it grew from.


---

## The fourteenth summary — F-R023, the plate is a hydraulic press

`rodriguez1985` arrived and answers a bigger question than the one asked of it. It measured **no bone
lengths** — pure histomorphology — so the loss-of-function leg stays withdrawn. But in **every operated
radius** it reports a law:

> *"there was **a lengthening of the hypertrophic cartilage at the external edge of the growth plate,
> subjacent to the removed perichondrial ring**. This feature seems to be a **specific response** of the
> growth plate to the excision of the perichondrial ring."* … *"the lengthened hypertrophic cartilage
> **protruded forming an arc**."* … and where an **osseous bridge** formed instead, it *"would constrain
> the growth plate and **impede the protrusion of cartilage**."*

**Cut the wall and the tissue comes out through the hole. Leave a wall and it does not.**

**Against R448 that is a reframe.** R448 computes chondrocyte turgor ≈ **400 Pa** against matrix
swelling pressure ≈ **0.28 MPa** — *"the matrix out-pressures the cell by 710-fold"* — and concludes
h_term is a **matrix-yield** problem, correctly killing the raise-the-drive arm. But 0.28 MPa is ~2.8
atmospheres, generated continuously, and **isotropic**. An isotropic pressure in a confined space does
not choose a direction; **the confinement chooses for it.**

> **The growth plate is a hydraulic press. Proteoglycan matrix is the working fluid; the perichondrial
> ring and cortical bone are the cylinder walls; longitudinal elongation is what happens because it is
> the only direction left open.**
>
> `longitudinal output ∝ (pressure generated) × (fraction vectored axially)` — and **the second factor
> is architectural.** R448 searched the first and found it saturated. **Nobody has searched the second:
> `radial constraint`, `hoop stress` and `circumferential constraint` each return 0 files.**

The field already knows the axial half under other names — **Hueter–Volkmann** (compression slows,
tension accelerates; 61 files) and **distraction osteogenesis** (pure axial tension lengthens a human
limb **with no growth plate at all**, 14.5 cm/person; 47 files). Three literatures, one law, never
joined.

**And this is the only lever in twenty-three rounds not gated by a tumour suppressor.** F-R022's
ceiling — *"an expandable self-renewing progenitor pool is what a tumour is"* — constrains the influx
arm regardless of risk tolerance, because chronic release of those brakes **costs height** (HME
carriers are short). **Confinement geometry has no such ceiling. A stiffer cylinder wall is not an
oncogene.**

**The combination**, `dH/dt = P_swell × f_axial × Φ`, duration = ∫ until influx < outflux — five levers
on four independent axes: **(1)** generate pressure — pO₂ **< 8%** → proteoglycan, plus GAG substrate
(glucose, sulfate/PAPS, NADPH); **(2) vector it — maximise radial confinement, apply axial tension
never compression**; **(3)** supply — cyclic loading convection (Serrat 1.5×, McGarry, Zhang human
AQP9/tight-junction response); **(4)** feed the pool — transient local Hh pulse at the PTCH1⁺ groove
(the one axis with a ceiling: pulse, don't saturate); **(5)** schedule — alternate hypoxic-preserve and
normoxic-spend phases. **Axes 1 and 2 multiply**, and every study in the literature has worked one and
left the other at baseline — a second, mechanical reason the field's effects are percentages. **Axis 2
also works when the pool is nearly spent, because it consumes nothing** — so for a subject at BA16+ the
ordering is **2 → 1 → 3 → 5 → 4**, the reverse of where this branch spent its first fifteen rounds.

**The test:** a compliant circumferential band around the perichondrial ring of one proximal tibia,
contralateral control, gripping radially but sliding axially so it does not become a tether. Predict
**longer and narrower** versus **shorter and wider**. The field builds growth-modulation hardware
constantly — tension-band plates, guided growth, the Luque trolley — and **every device ever built
applies axial force. Nobody has built one that applies radial force**, because nobody has framed the
plate as a pressure vessel.


---

## The fifteenth summary — F-R024, "never closes" is solved; velocity is the whole problem

The strongest evidence in this project was in the atlas the whole time, in
`round200_arrest_not_absence_and_the_adult_velocity.yaml`, and I had not read it.

**Term A — the plate never closes — is a described human phenotype with a failed closure attempt on
record.** `smith2008`'s ESR1-null man: **204 cm at 28**, continued adult growth, and *"**could not be
closed by any means — six months of transdermal oestrogen raising free oestradiol tenfold had no
detectable effect**,"* bone age moving only 15 → 17.5 in three and a half years. Not a mouse inference:
a deliberate, sustained, 10× closure attempt in a person that **failed**.

**Term B — the cells are still there.** `herrmann2002`: grew 170 → 197 cm, **ceased spontaneously at
24**, and three years later still untreated showed **open epiphyses at bone age 16**. *"A plate that
had run out of cells would not still be a plate."* **Arrest, not depletion.** A 27-year-old with an
open physis that has simply stopped being used. The round-86 census: 743 records screened, 45 full
texts, **20 people** with complete oestrogen loss, **not one** with a final height reached without
intervention.

**Term C — velocity — is unsolved, and it is the entire remaining problem.** `maffei2004`
**1.44 cm/yr** (21→29 y, bone age frozen at 15 *through 27 months of supraphysiological testosterone*);
`imre2025` **0.83 cm/yr** (25→31 y, still growing at 31). The atlas's own verdict: *"**ONE CENTIMETRE A
YEAR IS THE MEASURED CEILING OF THE DURATION LEVER.** Removing oestrogen for an entire lifetime does
not restore pubertal velocity."* Against a pubertal 8–10 cm/yr, **the uncloseable plate runs at roughly
one-tenth of what the same tissue does in a fourteen-year-old.** And the spread — one man quit at 24
while others ran a decade longer — is *"larger than any pharmacological effect in this file."*

**Which means every one of the twenty-three rounds before this was working on B.** Reserve, influx, the
clock, the renewal fraction, the groove, CCN2, Hedgehog. **B is not the binding constraint in the one
population where A is already satisfied.** Those men have cells and an uncloseable plate. What they
lack is drive.

**F-R023 says what drive is made of:** `dH/dt = P_swell × f_axial × Φ`. An open, arrested,
cell-containing plate at 1 cm/yr has one of those near zero, and **nobody has ever looked at the
tissue.** The leading candidate is P_swell: F-R015's **8% pO₂ switch** gates the proteoglycan program,
an adult epiphysis is far better vascularised than a child's, and **a plate sitting above the switch
would be making collagen instead of proteoglycan and generating no swelling pressure with all its cells
intact.** That single fact would explain the entire 1 cm/yr.

**A × C is the product nobody has attempted** — because in every recorded case of an uncloseable plate,
the clinical response was to **close it**. Twenty people in the world literature had permanently open
growth plates and medicine's response was to shut them.

**And one measurement answers almost everything.** An MRI or biopsy of an adult oestrogen-null open
physis would settle: does it have a resting zone; is it making proteoglycan or collagen (one Safranin-O
stain); what is its pO₂; is there PDGFRα⁺/Gli1⁺ influx at the margin; is the PTCH1⁺ groove intact.
**Every open question in this branch is answerable from one piece of tissue that exists in living
people** — and `imre2025` was published this year, so at least one of them is alive, identified,
thirty-one, and still growing.


---

## The sixteenth summary — F-R025, the drive is not endocrine

You did get `smith2008`, and it settles term C.

**The ESR1-null man at 28.5 y: IGF-I 528 ng/ml (nr 123–465) — above the adult range — and oestradiol
119 pg/ml (nr 10–50), 2.4× above it** (ER-α disruption removes the negative feedback, so he was
swimming in a hormone he could not read). The paper states it: *"the IGF-I concentrations in the
propositus were slightly elevated for an adult male, and testosterone levels were persistently within
normal limits."*

**What that bought:** arm span **213 → 216 cm over ten years = 0.30 cm/yr** (unconfounded; stature is
confounded by bilateral distal femoral surgery), bone age **15 → 17.5 over seven years**, and
**"length of the hands and feet was unchanged."** `maffei2004`'s untreated series is the cleanest:
**177 → 179 → 180 → 182.5 → 183.5 cm across five adult years = 1.3 cm/yr, approximately linear**, then
oestradiol took him to 184.5 and stopped him there.

> **An open, uncloseable, cell-containing human growth plate under supranormal IGF-1 produces
> 0.3–1.3 cm/yr against a pubertal 8–10.**

**This forecloses the obvious plan.** Hold the plate open and drive it with GH/IGF-1 — refuted before
anyone runs it, because the drive was already supranormal. `maffei2004` adds the androgen arm:
**27 months of supraphysiological testosterone with bone age frozen at 15 throughout. Term C is local,
exactly as F-R023 requires.**

**Second finding — the two ways of never closing are not equivalent.** Aromatase deficiency (no
ligand) **closes the moment you give the ligand back**: `maffei2004` went 183.5 → 184.5 on oestradiol
and stopped. ESR1 disruption (no receptor) **"could not be closed by any means — six months of
transdermal oestrogen raising free oestradiol tenfold had no detectable effect."** **The durable form
of term A is receptor-level, not ligand-level** — and the atlas holds the SERD class well
(`fulvestrant` 33, `tamoxifen` 135) while `ESR1 disruption` returns **2**.

**Third — residual growth is not uniform across plates.** Same man, same decade: **arm span grew,
hands and feet did not.** The Marmara case lists humerus, radius, ulna, femur, tibia, fibula still
unfused at 31 — long bones only. A metacarpal physis spans nearly the whole width of a narrow bone; a
femoral physis sits inside a wide metaphysis behind a substantial perichondrial ring. **Different
cylinders** — a testable prediction of F-R023's pressure-vessel model, and an anomaly the endocrine
model does not address at all.

**So the goal decomposes cleanly:** *never close* — **solved, and now graded** (receptor-level survives
a 10× challenge); *constant* — **solved** (linear multi-year adult growth, bone age frozen for four
years, open epiphyses at BA 16 in a 27-year-old); *fast* — **unsolved, and now known not to be
endocrine.**

**One question remains: why does an open, uncloseable, well-driven plate run at a tenth of pubertal
speed?** Leading answer, from F-R015: the **8% pO₂ switch**. An adult epiphysis is far better perfused
than a child's; above the switch the chondrocyte makes collagen instead of proteoglycan, generates no
swelling pressure, and does nothing with every cell intact. **That would explain the entire 1 cm/yr
and it is testable with one Safranin-O stain.** None of F-R023's three candidate answers requires a
drug, and none touches F-R022's tumour-suppressor ceiling.

**Next round needs no new papers:** the atlas's round-86 census already holds 14 aromatase-deficient
males from 743 screened records. Extracting growth velocities across all fourteen tests §1, which
currently rests on two cases.


---

## The seventeenth summary — F-R026, one cell two fates, and the histology of an arrested plate

**The deferred round, run.** The `nihms2173869` file **is** `mundy2026`. It resolves the perichondrium
into two layers and asks which makes the tumour: `Pdgfrα-CreER` targets **inner + outer**,
`Fgf18-CreER` targets **outer only**, both crossed to floxed *Ext1*. *"Osteochondromas had formed in
**Pdgfrα;Ext1** mutants targeting both layers, but **NONE** were appreciable in **Fgf18;Ext1** mutants
targeting the outer layer."* **The tumour progenitor is the Pdgfrα⁺ cell of the INNER cuboidal
perichondrial layer.**

Set beside F-R020: `rosellodiez2025` shows the **Pdgfrα⁺ cell outside the cartilage** becomes a Gli1⁺
long-lived chondroprogenitor, **enters the plate**, and is **required for normal bone length**.
**Same cell, two fates, and neither paper cites the other.**

**And EXT1 names the steering.** EXT1/EXT2 build **heparan sulfate**, which binds Ihh and turns a
secreted molecule into a spatial **gradient**. Lose HS, the gradient flattens.

> **The difference between "recruited productively into the plate" and "forms a lump beside it" is not
> which cell and not whether Hedgehog is on — it is whether the heparan-sulfate-shaped gradient is
> intact to tell the cell where to go. The goal is not more Hedgehog; it is a steeper gradient.**
> Flooding with agonist flattens the very gradient that directs the cell — a third independent reason
> systemic Hh gives percentages while a local bead compounds.

Atlas: `heparan sulfate` 37, `EXT1` 67, `Fgf18` 75 — parts held; **`inner perichondrium` 1 file,
`Ihh gradient` 0.**

**Three persistent-physis cases, and a distinction that had to be drawn.** `tas2020`: a 32-year-old,
electric shock 17 years earlier causing a left femoral fracture — *"a **normal right knee** and a
**persistent distal femoral physis line in the left**,"* confirmed on T1 MRI. **One man, one hormonal
milieu — one physis persisted, the other closed. Closure is under local control.**

`carroll2018` biopsied one: **"fragments of NONOSSIFYING hyaline cartilage with admixed fibroconnective
tissue, consistent with persistent physis."** Real cartilage, not scar — but **nonossifying**, fibrous-
admixed, no zonal architecture described. **The first histology of an adult persistent physis in this
branch, and it is a hard result: cartilage that has stopped running the endochondral programme.**

> **"Persistent physis" and "still-growing physis" are not the same tissue.** Persistent (normal adult):
> nonossifying, fibrous, mechanically weak enough to stress-fracture through, **zero output**, locally
> caused. Unfused (oestrogen-null): **0.3–1.3 cm/yr sustained for decades**, systemically caused.
> **The comparison between those two columns is exactly term C** — both open, one producing nothing and
> one producing a centimetre a year. A side-by-side of `carroll2018`'s H&E against a Safranin-O of an
> oestrogen-null physis would isolate the drive in one figure, and half the tissue already exists in a
> pathology archive.

Atlas: `persistent physis` 1 file, `nonossifying` 0, `electric shock` 0.

**Never close now has three routes of different grade:** receptor-level (`smith2008`, survived 10×
oestradiol), ligand-level (closes on ligand restoration), and **local/acquired (`tas2020`, unilateral
and permanent — the only compartment-specific one, and therefore the most interesting for delivery).**
**Fast** remains unsolved but now has a histological lead: whatever term C is, it is the difference
between cartilage that runs the endochondral programme and cartilage that merely persists.


---

## The eighteenth summary — F-R027, the absolute statement

**Why `herrmann2002`'s man stopped at 24 — the atlas answered it before I asked.**
`rz_depletion_causes_fusion.yaml`: *"**Depletion is SUFFICIENT TO STOP GROWTH and NOT SUFFICIENT TO
FUSE A PLATE**; fusion additionally requires the oestrogen signal that converts an exhausted plate to
bone."* And the mechanism, separating two things I had been treating as one: *"**oestrogen slows
resting-zone proliferation — that is, SELF-RENEWAL — without delaying, and possibly while accelerating,
DIFFERENTIATION OUT of the resting zone. The pool drains because the OUTFLOW is unchanged while the
INFLOW falls.**"* `nilsson2014`: oestrogen-accelerated RZ loss **persisted five weeks after washout**,
and transient exposure **permanently** hastened fusion.

**So he drained.** No oestrogen meant nothing suppressed his inflow — and he drained anyway, because
self-renewal alone does not keep up. The plate was still there at bone age 16 three years later because
**there was no oestrogen signal to convert an exhausted plate into bone.** Open, cell-poor,
nonossifying, producing nothing — exactly `carroll2018`'s histology.

**The balance:** `d(RZ)/dt = self-renewal + recruitment − differentiation`, and
`dH/dt ∝ differentiation × λ × h_term`. Three established facts make the answer forced:
**(i) growth IS outflow** — every centimetre is a cell leaving the resting zone, an identity not a
trade-off; **(ii) self-renewal cannot cover it** — `p = 0.392–0.493`, all below 0.500, and
`PMC12685065` confirms renewal by population asymmetry while GH *depletes* the pool; **(iii) oestrogen
blockade removes the conversion step, not the consumption step.**

**Which explains a century of percentages in one table.** GH: outflow ↑, inflow unchanged → drains
faster. Oestrogen blockade alone: nothing changes but the ending → open empty plate at 1 cm/yr.
Glucocorticoid: outflow ↓↓ → duration bought with velocity. Oestrogen: inflow ↓ → the fastest drain.
**Nobody has ever raised inflow.**

> **THE ABSOLUTE STATEMENT — unbounded, fast, non-closing growth requires the perichondrial recruitment
> rate to equal or exceed the differentiation rate, with oestrogen-receptor signalling blocked so that a
> transient shortfall does not become irreversible bony conversion.**
> **Speed** = `differentiation × λ × h_term`. **Sustainability** = `recruitment ≥ differentiation`.
> **Oestrogen blockade** makes a shortfall recoverable rather than terminal.
> **Fast and unbounded are not in tension — they are coupled by one inequality: recruit at least as
> fast as you grow.**

Recruitment is the only inflow that escapes the trade, because **a recruited Pdgfrα⁺ stromal cell
arrives with its own unspent division counter.** Every term now has a name: blockade **receptor-level**
(`smith2008`, survived 10× oestradiol); inflow **Pdgfrα⁺ inner perichondrium → Gli1⁺**
(`rosellodiez2025`, `mundy2026`); throttle **PTCH1⁺ groove** (`karlsson2009`, `trompet2024`); brake
**CCN2**; steering **heparan sulfate**; exposure rule **transient, local, self-limiting**; speed
`P_swell × f_axial × Φ`. And what is *not* the answer: GH/IGF-1 and androgen, both refuted in humans.

**The census could not be run, and that is the finding.** Round 86: *"NOT ONE has a reported final
height"* without intervention; the numbers that exist are *"the height at which a clinician
deliberately stopped them."* **The human ceiling has never been observed — not unknown, never
permitted.**

**Still open, and stated exactly:** recruitment has never been shown to **exceed** the set point
(everything demonstrated is homeostatic restoration); it has never been demonstrated postnatally; the
8% switch has never been measured in an adult physis; radial confinement has never been tested
constructively; and **no one has combined any two of these arms in the same animal.**


---

## The nineteenth summary — F-R028, the knife edge, the drain, and the human pressure vessel

**`imre2025` is genuinely closed** — Unpaywall `oa_status: closed`, `has_repository_copy: false`,
`oa_locations: []`; Europe PMC lists one URL, "Subscription required." No open copy exists. **But the
abstract carries the decisive number:** *"transdermal estradiol (**25 µg twice weekly**)… **Epiphyseal
fusion occurred within 6 months**"* — in a **31-year-old**. A low-dose HRT patch fused every long-bone
physis in half a year. Against `smith2008`, where **a tenfold oestradiol elevation on top of an
endogenous level already 2.4× the upper limit "could not be closed by any means."**

> **Ligand-level blockade is a knife edge; a trace of oestrogen from any source closes it, and the plate
> is more sensitive at 31 than an adolescent's at 14. Receptor-level is the only durable form of term
> A.** Any aromatase-inhibition strategy has to contend with adrenal androgen aromatised in adipose,
> incomplete enzyme inhibition, and dietary oestrogens — all reaching a receptor that is present and
> evidently exquisite.

**`nilsson2014` measures the drain, and it is not cell death.** RZ chondrocytes per mm decline with age
(PT p<0.001, DR p<0.001); oestrogen accelerates it (p<0.01, p<0.001); **TUNEL⁺ RZ cells are identical —
4.6 ± 0.6% vs 4.4 ± 1.0%, p = 0.87**; and **five weeks after washout the deficit remained** (DR p<0.01),
*"a mechanism by which estrogen permanently advances structural growth plate senescence."*
**The cells are not dying — they are leaving and not being replaced.** F-R027's outflow model,
measured. **And an honest negative: the pool did not spontaneously refill in five weeks.** Caveats —
nobody looked at the perichondrium, and `rosellodiez2025`'s refill was *induced* by a challenge that
made the cartilage signal to surrounding tissue, which oestrogen depletion may not do. **But
spontaneous postnatal recruitment sufficient to refill a depleted resting zone has not been observed,
and one study looked in roughly the right place and did not find it.**

**The human test system exists and I did not know it.** *The Leiden ex vivo human growth plate model in
severe tall stature* (2026): viable human GP obtained **reproducibly** during routine percutaneous
epiphysiodesis in adolescents treated for **extreme tall stature**, expanded, formed organoids,
deposited cartilage matrix — *"a unique platform to study local mechanisms of endochondral bone
growth."* **The only reliable source of living human growth plate is surgery performed to stop tall
adolescents from growing.**

**And F-R023's pressure vessel is now described in human tissue.** PMC12334589 (2025, OA): the
**GP–epiphysis interface** shows *"a sharp transition in tissue modulus, **acting as a protective
shell**"* and is a **mineralization INHIBITION zone** (**SPP1, AHSG** — *"forming a defense line"*);
the **GP–metaphysis interface** shows *"a gradual modulus increase, enabling efficient load
redistribution"* and is a **mineralization PROMOTION zone** (**ENPP1, ALPL**). Their phrase for the
output: **"polarized bone elongation."** Closed end, radial wall (the perichondrial ring), moving face
— all three named, in humans, with moduli and a proteomic map. Atlas: `AHSG` **0 files**,
`mineralization inhibition zone` **0**, `polarized bone elongation` **0**.

**The framework now reduces to two runnable experiments:** (1) can recruitment **exceed** the set point
— local Hh pulse at the groove, unchallenged limb, contralateral control, length to maturity; (2) is an
arrested plate above the **8% switch** — one Safranin-O, and the Leiden model supplies the tissue
prospectively instead of waiting on a pathology archive.


---

## The twentieth summary — F-R029, the three-term phenotype already exists, and I had two conclusions wrong

**Correction 1, to F-R027.** I called its load-bearing assumption untested — *"recruitment has never
been shown to exceed the set point."* **I had the refuting paper and had read it twice without pulling
the sentence.** `trompet2024` (JCI Insight 2024;9(6):e165226, open access): *"we used an alternative
approach that **enhanced the number of stem cells, which subsequently converted into the leg length
outgrowth, thus demonstrating that the growth potential can be improved by the increased number of
stem cells**."* Normal rats, contralateral control, one leg longer and the gap widening at 2 and 6
months. **Not homeostasis. The assumption is met.**

And the mechanism is this branch's own, reached from the other side. Their Figure 3: *"SAG
administration expands the growth plate skeletal stem cell pool and **creates a Wnt-inhibitory
environment**."* A **six-day** systemic SAG pulse raised Pthrp-mCherry⁺ resting-zone stem cells
**+61%**; RNA-seq put **Wnt among the top 2 downregulated pathways**; and they cite `hallett2021` — the
exact paper F-R017 built its Wnt-inhibitory-niche argument on. **F-R017 got there through oxygen and
Frzb/Dkk1; `trompet2024` got there through Hedgehog. Two routes, one niche.**

**Correction 2, to F-R025.** I concluded *"the drive is not endocrine"* from `smith2008`'s IGF-1 of
528 against a range of 123–465 and called it supranormal. **It is 1.14× the upper limit.** The Endotext
gigantism case grew **19 cm/yr** at IGF-1 **1.03× ULN**. **Serum IGF-1 does not measure the drive.**
F-R025 survives narrowly (a *normal* axis, however high in range, does not restore adult velocity) and
fails generally (at tumoral output the axis is the largest lever ever documented).

**The finding: the three-term phenotype exists and the standard literature states it in one sentence** —
*"when GH hypersecretion is accompanied by gonadotropin deficiency, **accelerated linear growth may
persist for decades**."* Never closes (no gonadotropin → no sex steroid → no fusion), constant
("decades"), fast (up to 19 cm/yr).

**And the tallest documented case says the quiet part.** Robert Wadlow: 183 cm at 8, 196 at 10,
**224 at 13**, **265 at ~21**, **272 at 22** — **~5.1 cm/yr from 13 to 21 and ~5.2 cm/yr in the final
year. Nine years, essentially linear, no detectable deceleration**, against 0.3–1.3 cm/yr in the
oestrogen-null men of the same age band. **He did not stop. He died** — of an infected blister from a
leg brace, still growing.

**Both human phenotypes that satisfy all three terms have existed, and neither has ever been permitted
or survived long enough to reach an endpoint.** The aromatase census: *"NOT ONE has a reported final
height"* without intervention. Gigantism: treated, or dead of the tumour.

**Model update:** `dH/dt = DRIVE × pool × λ × h_term`, `d(pool)/dt = inflow − outflow(DRIVE, pool)`.
**Drive multiplies both** — it raises velocity *and* accelerates depletion, exactly as `PMC12685065`
shows GH depleting the stem pool. **Wadlow's flat nine-year curve is then the anomaly worth staring
at:** maximal drive on a finite pool should visibly decelerate, and it did not. Either the pool is far
larger than the aromatase cases imply, or **high drive recruits as well as spends** — which is what
`trompet2024` shows Hedgehog doing (+61%) and `rosellodiez2025` shows the perichondrium doing on
demand.

**The decisive question is now answerable from existing case material, not new experiments: do adults
with untreated gigantism plus hypogonadism decelerate, or hold velocity?** The **AIP** and
**X-LAG/GPR101** cohorts are the modern genetically-defined populations with systematic follow-up.
Atlas: `AIP` 98 files, `GPR101` 26, `X-LAG` 18 — but **`gonadotropin deficiency` 3 and `Wadlow` 0.**
**The conjunction that is the whole phenotype is not a concept anywhere in the graph.**


---

## The twenty-first summary — F-R030, every within-plate lever fails the same half

**The atlas stated F-R027's condition before I derived it, and killed the obvious lever.** R242:
*"The target condition asked for was **replacement greater than or equal to loss WITHOUT losing
output**, and a PRRX1 lever **fails the second half**."* Because `hu2024`/`hu2025` in antler reserve
mesenchyme show **PRRX1 is the brake**: *"as miR-140-3p rises, Prrx1 is inhibited, **the maintenance of
RM cell self-renewal and pluripotency is disrupted**, and that is what **initiates** the rapid
chondrogenic differentiation"*; overexpression *"decreases proliferation and maintains the
undifferentiated state."* R241 had already found the ligand-level version — the root cell holds itself
quiescent with **self-secreted WNT and TGF-β antagonists.**

**The structural finding: the same shape appears at five levels.** PRRX1↑, Wnt/TGF-β antagonists↑,
hypoxia, glucocorticoid — all preserve the pool by stopping growth. GH, oestrogen, Hh-release,
miR-140-3p — all buy output by draining. **Every lever acting *inside* the plate is one knob on one
flow — the exit of a cell from the resting state — and no setting does both, because pool and output
are the same cells at two moments. That is why a century of work produced percentages, and it is
topological, not pharmacological.**

> **Therefore the condition cannot be met by any intracartilaginous lever. Replacement must arrive from
> cells that are not themselves the output — and there is exactly one such route: Pdgfrα⁺ inner
> perichondrium → Gli1⁺ chondroprogenitor → resting zone.**

**And this year's human paper supplies the architecture.** Chu TL et al., *Sci Transl Med* 2026
(`10.1126/scitranslmed.adw3590`), single-cell + spatial on **human pubertal growth plates from
growth-restricting surgery**: **two stem populations in the resting zone**; the **root cells are
Prrx1⁺, PTHrP-negative, in a niche low in WNT *and* TGF-β**, and clonal tracing shows they *"generate
extensive chondrocyte clones."* And: **"GH… stimulates cartilage growth and PROLIFERATION OF CARTILAGE
STEM CELLS."**

**That resolves the GH paradox into a tier structure** — `PMC12685065` (mouse) has GH *depleting* the
PTHrP⁺ pool; Chu has GH *stimulating* stem proliferation in human explants. Both hold if **GH spends
the working tier and pushes the root tier that feeds it** — which is the mechanism for **Wadlow's flat
nine-year curve**. Maximal drive on one pool must decelerate; on a two-tier hierarchy where the drive
also pushes the upstream tier, it need not.

**The hierarchy is now four deep and every arrow crosses a compartment:** perichondrium (Pdgfrα⁺/Prrx1⁺,
outside) → root (Prrx1⁺ PTHrP⁻, low-Wnt/low-TGF-β) → PTHrP⁺ working tier → proliferative/hypertrophic
output. **Only the top arrow originates outside the cartilage, and it is the only source not itself
being spent as output.**

**"Never close until we choose" is finished, and it is a switch with both directions shown in humans:**
ER-α disruption held a plate open against a **tenfold** oestradiol challenge on top of an endogenous
level already 2.4× ULN (`smith2008`); **25 µg transdermal oestradiol twice weekly fused a 31-year-old
in six months** (`imre2025`). Term A is not a research problem.

**What is left is one quantitative question** — can perichondrial recruitment be driven to match the
differentiation rate postnatally without losing output — plus two genuine unknowns: **nobody has ever
fired a second Hedgehog pulse** (`trompet2024` fired one; signal gone by 3 weeks, no OA at 6 months,
effect still widening), and **nothing yet measures whether the root tier is refillable or is the true
terminal reservoir.**


---

## The twenty-second summary — F-R031, Trompet's Figure 5, and two corrections

**The figure, read.** `trompet2024` Fig 5B–E: paired DMSO-contralateral vs SAG, **every line rises**,
and the significance *deepens with time* — femur P<0.05 → P<0.01 → P<0.001 at 1, 2, 6 months; whole leg
to **P<0.0001**; panel E is two femurs against a ruler. Fig 5G–H: the calcein–xylenol **growth-rate**
difference is significant only at 1 month (femur) and 2 months (tibia). Fig 5J–K: **Ki67⁺ cells in the
top 50 µm — the resting zone — spike at ONE WEEK only** (femur ≈4.5%→13%, tibia ≈8%→19%, both P<0.01)
and are **NS at 1 and 2 months.** Fig 5M: **Pthlh⁺ cells ≈20% → ≈29% at one week.**

> **The stem-cell response is a one-week event. The SAG signal is gone by three weeks. And the length
> gap widens for six months with the P value falling the whole way. A single week of stem-cell
> proliferation buys at least six months of divergent growth — not a sustained drug effect, but a
> larger pool created once and paying out continuously.** The pool has been expanded **once**. Nobody
> has expanded it **twice**.

**Correction 1 — GH does not push the root tier.** F-R030 explained Wadlow's flat curve that way.
`chu2026`'s own quantification (7 vehicle / 6 GH donors, EdU counted separately by zone) refutes it:
**PZ P = 0.013, RZ P = 0.79.** GH is a working-tier drug — it amplifies output downstream of the stem
compartment and does not replenish it, agreeing with `PMC12685065`. **F-R030's central argument gets
stronger** (the largest output driver known still fails the second half of the condition) **and its
mechanism for Wadlow is withdrawn.** The observation stands; I have no explanation for it and will not
invent one.

**Correction 2 — the hierarchy conflated two compartments.** `chu2026` states: *"gene expression
analysis for **periostin (POSTN) confirmed their absence**"* — perichondrium was excluded by design.
**GP1 is intracartilaginous**, upstream of PTHrP⁺ by velocyto trajectory (*"GP1 as the root population
and GP5 as the terminal end point"*), but inside the plate. Prrx1 is shared with perichondrial
mesenchyme, which is what misled me. **The perichondrium → root arrow is demonstrated in fetal mouse
and unmeasured in humans — because the one human dataset excluded the compartment.**

**What `chu2026` gives that nothing else does:** the root niche with human markers — **SFRP5** (secreted
WNT antagonist) and **APOE**, in a niche *"low in WNT and TGF-β"*, with DKK1/GREM1/FGF2/KLF4 in the
regulatory set — **the atlas's R241 "self-secreted WNT and TGF-β antagonists" with human gene names on
it.** And the platform: human growth plate in **1-mm slices, two months**, which *"retained its
structural integrity and biological activity, as evidenced by preserved histology and **proteoglycan
abundance assessed by Safranin O staining**"* — the stain I had been asking for across four rounds,
already done, on human tissue. Plus a result aimed straight at this branch's oxygen arc:
***"vascularization is dispensable for chondrogenesis but essential for ossification"*** — cartilage
grows on diffusion alone at 1 mm; bone does not.

**And the honest limitation on GH:** *"not all patient samples responded… interindividual differences
in GH responsiveness."*

---

## The twenty-third summary — F-R032, output is conjugate to the pool, and that is an identity

Two documents this programme had never read: **`chu2026`'s supplement** (Tate supplied it — the atlas
called it *"the highest-value unobtained document"*) and **`chu2025`'s full text** (PNAS, PMID 41289405,
PMC12685065, open access, plus its SI Appendix and figures).

**The identity.** `round247` showed that under neutral drift the self-renewal fraction `r` cancels out of
the output equation — one committed cell per stem division for every `r` — and concluded the fraction is
not in the equation. That is right *only because the premise imposed neutrality*. Let symmetric renewal
have probability `a` and symmetric loss `b`:

> **E[committed] + E[Δstem] = 1, exactly, for all `a` and `b`.**

**Output above the neutral rate is not paid for by pool loss. It *is* pool loss, in the same cells,
counted twice.** The atlas has been pricing an "exchange rate" empirically since R198. There is no
exchange rate; it is 1:1 and it is arithmetic. `round247` was right that `r` cancels and wrong that the
fraction is gone — the *neutral* parameter cancels, the **asymmetry `a − b` is the pool derivative** and
is conjugate to output one-for-one. `round240` named the right quantity and the wrong fraction.

**Measured, not argued.** `chu2025` fig. **S6** stratifies clones in the femoral plate, n=5/group:
**singlets 47.4% → 37.6% (p<0.01), dyads 38.7% → 40.4% (n.s.), long columns 7.4% → 16.1% (p<0.001).**
GH moves −9.8 points out of the retained class and +8.7 into the committed class **and leaves the
asymmetric class alone — the one class the arithmetic says is fate-neutral.** With CD73⁺ cells
283 → 220/mm (p<0.001) and **Ki67 in stem cells unchanged (22.2% → 19.3%, n.s.)**: the pool falls by
*conversion*, not by dividing faster.

**The escape.** The identity is denominated *per stem division*, so it prices **λ** and does not price
**N**. Doubling λ doubles output and doubles the spend; **doubling N doubles output and spends nothing
extra per unit output.** Every drug the field has targets λ. **Fast must be bought in N.** Which makes
Terms B and C the same lever, and the whole problem one inequality:

> ### `influx ≥ λ·N·(b − a)`, with ER signalling blocked, and λ·N large.

The RHS scales with the drive, so **influx cannot be a pre-treatment — it must be co-dosed and titrated
against the drive.** Nobody has done this: `trompet2024` fired one Hedgehog pulse and stopped; the GH
literature raises λ with no influx term at all.

**`chu2026`'s figures correct the atlas's record of `chu2026`.** Round 240 recorded, from the abstract,
that it showed GH *"stimulating proliferation of both cartilage stem cells and proliferative-zone
chondrocytes."* **Every stem-compartment endpoint in the supplement is null and trends the wrong way** —
GP2 cycling 22.5%→23%, RZ CYTL1⁺ n.s. (down), RZ RAMP3⁺ n.s., RZ SOX9⁺ P=0.79 (down) — while GP3
(proliferating) goes 14%→45%, p<0.0001. **And the only length endpoint in the paper is P = 0.1827, n=5
paired.** The preprint title said *"direct stimulation of cartilage stem cells"*; the published title says
*"direct effect."* The counterweight round 240 carried can be set down: human agrees with mouse.

**A consequence that kills a whole class of levers.** `A` is a *count*, not a rate. Accelerating a fixed
count changes *when* cells emerge, not how many per stem division. **Tripling proliferative-zone cycling
cannot raise height at steady state** — which is exactly what S10T + S8C measured and did not conclude.

**Also in the supplement, unused by anyone:** RZ height does **not** distinguish tall-stature from
normal-height children (fig. S2L — a lead, n=2 vs 4, unquantified); clonal scaling is exponential,
i.e. *"stochastic drift in a **zero-sum system**"*, raising the possibility that N is capped by niche
slots rather than cell behaviour; the explant is **normoxic** (~18.6% O₂ against Brighton's 6–7% PZ and
2.1% HZ, on the wrong side of the 8% switch); the culture itself **halves** the cycling fraction
(14.2% → 8.4%, p<0.0001); and the explant is **influx-free by construction** — a central core has no
groove of Ranvier — so it is permanently in the bounded regime.

**One measurement, absent, would have decided the paper:** fig. S8C is a paired test on *absolute* plate
height at two months **with no day-zero baseline**, though spare slices from each biopsy were explicitly
allocated to immediate fixation. **The highest-value missing measurement in the field's best human
platform is a day-zero plate height, and it costs nothing.**

**Chain checked, not assumed.** `chu2025` names **PCP** as the regulator of symmetric vs asymmetric stem
division — the one lead that would separate the `λ` machinery from the `a−b` machinery. I pulled the cited
paper (Li 2017, eLife 6:e23279): **"self-renewal" appears 0 times, "fate" once (about *Drosophila*), and
every "stem"/"asymmetric" hit is introduction framing or reference list.** It contains no stem-fate data.
The lead is real and currently **unsupported** — recorded as such.

**Still unexplained, on the record:** Wadlow's flat ~5 cm/yr from 13 to 22. Under §2 a pituitary giant
sits in the `a < b` regime and should decelerate. He did not.

---

## The twenty-fourth summary — F-R033, the thickness budget, and a geometry error of mine

**I had the geometry wrong and I am correcting it first.** F-R032 §3 said doubling N doubles output, and
§5b proposed that niche slot count scales with plate cross-sectional area. **Columns act in parallel** —
every column pushes the epiphysis away by the same distance simultaneously, so adding columns makes a bone
**wider, not longer**. The field's own rate formula (divisions per column per unit time × terminal cell
height) has no width term. So `N` must be read as **reserve depth above one column**, and the "free"
direction I had found contributes nothing to height. **The niche-widening architecture is withdrawn.**

**Kondo 2021 (PMC8804827) is the measurement that settles it.** Mouse tibia P6–P70: growth rate tracks
**resting zone height (R² = 0.973)** and **proliferative zone height (R² = 0.948)** — and **growth plate
area returns R² = 0.171, P = 0.415.** The abstract reports width as "the strongest correlation"
(R² = 0.989), but the paper's own text has rate falling after P13 while width rises to P28 — **opposite
trajectories, and R² is unsigned, so that is a strong NEGATIVE correlation.** The area null is the check
that proves the signs: area combines a positive axial dimension with a negative radial one and cancels.

**U2 — closed to a residual. The plate has a diffusion-limited thickness budget and every term is inside
it.** Seven lines: growth-plate thickness conserved to ~2–3× across 10⁵-fold body mass while **articular
cartilage in the same animals spans 33×** (90 µm mouse → 3,000 µm elephant); the plate is fed essentially
from one side (Brighton: metaphyseal bone 19.8 mmHg vs diaphyseal 108.7); chondrocytes evolved
**haemoglobin bodies, P50 27.6 vs 58.2 mmHg**; HIF-1α deletion kills the plate interior; `newton2019`'s
clone size runs **7.8 central vs 5.7 lateral by SOC proximity (P = 0.0012)** and **axitinib, which blocks
SOC vessels, reduced it (P = 0.0023)**; the one-sided slab calculation gives ~1.3× headroom and the
observed intra-plate spread is 1.37×; and the only untaxed dimension is the one that does not lengthen.

> **Identity 1 (conjugacy): output above neutral = pool loss, 1:1. Prices λ.**
> **Constraint 2 (thickness budget): RZ + PZ + HZ ≤ L_max(D, C₀, Q). Prices n, A and h_term against each other.**
> **There is no free term** — and the one lever outside both is **supply**, since L_max ∝ √(D·C₀/Q).

**U3 — advanced, one measurement short, and the news is bad.** Reading `trompet2024` Fig 5 panel by panel:
Ki67 up only at **1 week** (femur 4.5→13%, tibia 8→19%, both ✱✱), growth **rate** up only at 1 month and
**NS at 2 months**, length offset ~1.5 mm on 35 mm femur (≈4%) persisting to 6 months. The famous **+61%**
is a different experiment read **two days after the last dose**, and the bead's Gli1 signal **vanished
within 3 weeks**. **That is a one-off gain banked, not a compounding one.** But the pool was counted at one
week and **never again** — set-point versus sustained-elevation is undecided, and nobody has fired a
second pulse.

**Two things in Trompet that are better than recorded:** the age-window is a **route artefact** — genetic
activation in PTHrP⁺ cells works *"independent of age"* — which removes that constraint; and **Hedgehog is
named as the `a − b` regulator** (*"the balance between generation of daughter stem cells and committed
progeny"*), acting by creating a **Wnt-inhibitory environment**, converging with `chu2026`'s human root
niche being **low in WNT and TGF-β**. Unlike F-R032's PCP lead, this one is supported by its own data.

**"Fast" now has a number.** Rat proximal tibia runs **~360–400 µm/day**; the human distal femoral physis
averages **~27 µm/day** and peaks near 50–55. **A rat plate runs ~7× a human plate, at similar thickness.**
Wilsman's four-plate series spans 50→400 µm/day with cycle times 30.9/34.0/48.7/76.3 h and *"almost all
differences… attributable to the length of the **G1 phase**."* And **Longshanks** — 20 generations of
selection, **13% longer tibiae** — moved *"the number of proliferative chondrocytes"* and **nothing else**,
with `marchini2019` naming de-repression via two limb enhancers of **Nkx3-2**.

**Where it is still flawed, precisely:** the thickness cap is inferred from seven lines and never measured
— **no one has ever measured oxygen tension in a human growth plate**; Trompet's pool persistence is
unmeasured beyond one week; and **Longshanks is ambiguous in exactly the sentence that matters** (more
cells *per column*, which §2 taxes, or *per plate*, which §0 says is useless) — and that paper is
paywalled.

---

## The twenty-fifth summary — F-R034, oxygen is not a supply, it is the renewal knob

**F-R033 §2 is falsified, and the paper I said I needed is what refutes it.** Tate could not get Brighton
& Heppenstall 1971 (*JBJS* 53A:719–728) — but its companion, **Brighton & Heppenstall, *Clin Orthop*
1971;80:167–173 (PMID 5133323)**, has been archived in this repo as page scans since F-R014 and I had
never fully read it. Its **Table 1 is the complete zonal oxygen profile**, and its footnote —
*"First value = oxygen tension in mm Hg. Value in parentheses = per cent oxygen"* — closes the provenance
question. **My numbers were right**: SOC 14.9–15.1%, proliferative 6.0–7.1%, hypertrophic 2.0–2.2%,
metaphysis 1.0–2.5%, diaphysis 14.0–15.2%. Species is dog; the rabbit values match.

**And the same paper's discussion destroys the model I built on it:**

> *"**High oxygen consumption in the epiphyseal plate has not been reported by any author under any
> condition or circumstance**… Despite increased epiphyseal plate growth, the oxygen tension at the zone
> level did not change. **Little oxygen was consumed in the face of active bone growth**… **the delivery
> of less oxygen to the plate results in more growth of the plate**."*
> **Low O₂ → Anaerobic Metabolism → Increased Plate Growth. High O₂ → Aerobic → Decreased Plate Growth.**

Plus: less O₂ in vitro → *more* bone; the in vivo plate grows **5× faster** than in vitro at **4–5×
lower** pO₂; and the A-V fistula lowered pO₂ in every zone while lengthening **100%** of puppies. The
plate is **glycolytic and barely consumes oxygen**. So there is no oxygen budget, no inter-zone
competition, and **"raise the supply" — the one lever I called untaxed — points the wrong way.** Had the
mechanism-first rule not held, F-R033 would have produced a hyperoxia recommendation.

**Marchini's workbook kills it independently.** Per-animal (n=49): **PZ vs HZ r = −0.118, p = 0.42**;
within-line −0.013 / +0.021 / −0.159, all null. **No zone trade-off exists.** Total plate height spans
**435–753 µm (1.73×)** in one cohort at one age, against my computed 1.3× ceiling.

**Flaw 3 closed: "per column", explicitly.** And Table 1 shows the plate **got thicker** — μCT +24%/+34%
— with **HZ unchanged (P=0.219)**, **hypertrophic cells/column 18/18/18 (P=0.722)**, **h_term unchanged
(P=0.775)**, **division rate unchanged**, **duration unchanged (99% complete within 24–48 h of each
other)**. Selection moved exactly one term: **proliferative cells per column, +32%.**

**A dissociation the paper does not report:** from the raw data, **LS1 is already +14.5% at birth
(p≈0.001)** while **LS2 is +5.2%, n.s.** — same endpoint, opposite routes. And LS2, the postnatal line,
carries the larger plate phenotype (RZ +56%, PZ +37%). **So the postnatally achievable figure is LS2's
~18%**, and any claim that Longshanks demonstrates a postnatal mechanism must rest on LS2 alone.

**Wilson 2021 signs confirmed** — height/RZ/PZ positive with rate, **width negative**, area R²=0.171
n.s. My reconstruction was right. **Breur confirms the column model formally** (*"the complete
chondrocytic column is the functional unit"*) — and challenges the atlas's `h_term` axis, since *"it is
unlikely that the mean height… is an indicator of the mean chondrocytic volume"* and 1-D models were
*"unsuitable or not as robust"* as 3-D ones.

**What replaces the dead lever is better.** `leijten2012` seems to contradict Brighton (normoxia
increased length) until it is read against the conjugacy identity: *"**hypoxia retains chondrocytes in
the resting zone while normoxia stimulates them to progress towards the hypertrophic zone**."* That is
`a − b` in words — normoxia spends the pool, hypoxia preserves it; a fixed-pool fetal explant rewards
spending, an intact animal rewards preserving. **Oxygen tension is a control input on the renewal
balance, not a supply.**

And the mechanism converges four ways. Hypoxia induces **GREM1, FRZB, DKK1** (mRNA and ELISA protein) —
secreted WNT/BMP antagonists. `chu2026`: the human root niche is *"low in WNT and TGF-β"*, markers
**SFRP5** + APOE, with DKK1/GREM1 in its regulatory set. `trompet2024`: SAG works by *"creating a
**Wnt-inhibitory environment**"* and Hh governs *"the balance between daughter stem cells and committed
progeny."* Atlas R241: the niche is *"self-secreted WNT and TGF-β antagonists."*

> **A candidate `a − b` lever that is local, physiological, has a named effector set, has human niche
> validation — and is not a tumour suppressor.** Every prior pool lever in the atlas was one.

Its failure mode is stated: it raises `a − b` at the cost of `λ`. **On its own it delivers two of three
terms**, and the third needs it co-dosed with a drive lever — the titration architecture nobody has run.

**Still needed, and now top of the list: Stambaugh & Brighton 1980, *JBJS* 62A:740–749** (PMID 7391097) —
verified genuinely closed (Unpaywall `is_oa:false`, no repository, no PMC, no scan, no abstract). Since
oxygen is *not* the limiting solute, *"Diffusion in the various zones of the normal and the rachitic
growth plate"* is the only existing measurement of what else crosses the plate. **Second: Brighton, Ray,
Soble & Kuettner, *JBJS* 51A:1383, 1969** — the oxygen dose-response, which would be the dose curve for
the `a − b` knob.

---

## The twenty-sixth summary — F-R035, the two papers hunted, and the size gate

**Brighton 1969 — results recovered, PDF not.** *"In vitro epiphyseal-plate growth in various oxygen
tensions"* (JBJS 51A:1383–96, PMID 4186275): **cartilage growth maximal at 21% O₂ (160 mmHg)**;
**maximum metaphyseal bone formation at 5% O₂ (38 mmHg)**; above 21%, *"progressive loss of acid
mucopolysaccharide stainability, eventual loss of the zone of hypertrophic cells."* Retrieval note:
Unpaywall flags this DOI **green OA** via a figshare thesis deposit — **false positive**, the record has
`files: []`, license *"In Copyright"*, a ProQuest stub. **The UIC INDIGO handle 10027/14248 on this
branch's standing list resolves to the same record**, so the "Brighton thesis" ask and this paper are one
item with no file behind it.

**Stambaugh & Brighton 1980 — partially recovered, verified genuinely closed.** Via Serrat 2014, which
cites it in text: *"**diffusion coefficients for radioactively labeled insulin in the reserve growth
plate zone were over twofold greater at 22°C than at 4°C**."* So: radiolabelled insulin (~5.8 kDa),
zone-specific coefficients, normal vs rachitic. The zone table is **not** obtained — PubMed no abstract,
Unpaywall `is_oa:false`/no repository copy, no PMC, no Internet Archive scan, OpenAlex closed, LWW
Cloudflare 403, **Ovid HTTP 402 Payment Required**, 11 citing works of which 1 is in EPMC full text.
**It needs a library scan or ILL of pages 740–749.**

**The 1969 dose-response corrects F-R034 §7.** Not "hypoxia is good" — a **monotone knob with a
ceiling**: raising pO₂ shifts cells reserve→hypertrophy (`a − b` falls, elongation rises), lowering it
holds them in reserve, cartilage optimum ~21%, toxic above. `leijten2012` agrees. And Brighton's own
electrode data put the living proliferative zone at **6.0–7.1%** — **far below the in vitro optimum, on
the reserve-preserving side.** That is F-R016's velocity/duration trade with a measured dose axis.

**The 40-year contradiction is resolved, and it is perfusion.** An A-V fistula is a flow intervention:
Serrat measures **blood velocity +118%, vessel diameter +31%**, tracer entry **>150%**. Its low pO₂ is
the signature of shunting, not the mechanism. And an atlas node I had not read —
`the_plate_is_advection_fed_not_diffusion_limited` — reaches my Brighton conclusion independently and
quantitatively: measured diffusivity 20–60 µm²/s, **interstitial flow +2.5/−2 µm/s converging from both
junctions**, **Péclet 6–25**, **Damköhler 0.015–0.185** — *"a tissue that consumes a few per cent of what
crosses it is not consumption-limited."* Two routes, one conclusion. **Oxygen is a signal; advection is
the supply.** (It also corrects my one-sided-slab geometry a second time — the plate is fed
convergently from both ends.)

**And hunting the 1980 paper produced the thing that matters more than either — the size gate:**

> *"Williams et al. … showed that **molecules >10 kDa were essentially size excluded from the growth
> plate**."*

Small molecules (<500 Da) enter freely; CNP/vosoritide ~4 kDa enters; **IGF-1 at 7.6 kDa enters**;
**GH at 22 kDa is essentially excluded**; antibodies at 150 kDa are out. **This predicts `chu2026`'s
P = 0.1827**: GH triples GP3 cycling in a 1–2 mm bathed explant, where there is no barrier — the direct
GH-on-plate mechanism may be largely an artefact of bypassing the transport block. **The first
constraint in this programme that filters agents rather than mechanisms.**

**Credit where the atlas had it:** the Serrat temperature work is already held, graded, in
`local_limb_warming_is_a_free_delivery_and_growth_lever` — unilateral 40°C giving femur +1.3%, tibia
+1.5%, elongation rate +12%, persisting ~1% at seven weeks — **together with the two things that stop it
being an answer**: `serrat2013`'s finding that temperature-responsiveness exists only in a window of
rapid growth (rates identical at 7/21/27°C in the second phase), and **Ring & Lee 1958 — 40°C at the
knee in four children, no influence on longitudinal growth.**

**Still needed: a library scan of Stambaugh & Brighton 1980** (zone-by-zone diffusion coefficients, plus
the rachitic comparison — now load-bearing because the size gate needs calibrating), and **Williams et
al.**, the primary behind the 10 kDa cut-off.

---

## The twenty-seventh summary — F-R036, the transport map completed and the gate is mineral

Tate obtained all three: **Stambaugh & Brighton 1980**, **Williams/Zipfel/Tinsley/Farnum** (*Biophys J*
93:1039–1050 — which turns out to be **the source of the atlas's whole Péclet/Damköhler analysis**), and
**Brighton & Schaffzin 1970**.

**Two corrections I owe.** It is **inulin**, not insulin — Serrat's text carries the error and I
propagated it (the 2.76× temperature claim checks out: 2.02 → 5.57). And *"molecules >10 kDa are
essentially size excluded"* is Serrat's paraphrase, too strong: the primary says **3 kDa enters at 62%
and 10 kDa at 15%** of a small tracer's level, that **10 kDa still saturates the plate in 5 minutes**,
and that since FL and 10k-FL diffusivities differ only ~2× ex vivo, *"the transport block **may be a
charge effect**."*

**Stambaugh & Brighton — the barrier is mineral, and it is reversible.** Rabbit, ³H-inulin
(×10⁻⁶ cm²/s): hyaline 1.89, **reserve 2.02**, columns 1.51, **hypertrophic 0.62** — the hypertrophic
value is **31% of the reserve zone**. At 22°C: **reserve 5.57 (highest in the table, Q₁₀ 1.97)** vs
**hypertrophic 1.11**, and warming raised D in **every zone except the hypertrophic one**. Meanwhile
**% matrix FALLS** 88.9 → 55.0 toward the barrier while **ash rises 3.1 → 24.4% of dry matter (8×)**, and
**ash was the single best correlate** of diffusion across every parameter measured. The causal test:
rachitic rat hypertrophic D **0.71 → 4.65 (6.5× open)** as ash falls 23.4 → 11.1%, and healing closes it
again to 1.27. **Demineralise the front and it opens; re-mineralise and it shuts.**

**Williams — the map.** Three sources (epiphyseal, metaphyseal, subperichondrial plexus). COJ-entering
molecules distribute throughout in 90 s; perichondrium-entering molecules stay put. **The proliferative
and early hypertrophic zones are "at least two-to-fivefold as permissive" as either junction** — the
midplane is the open door, both junctions are the barriers. And the midplane is *"the transition at which
chondrocytes commit to hypertrophy"*, where perichondrial BMP2/FGF18/PTHrP concentrate.

> **The place where the commitment decision is made is the most transport-accessible place in the plate.**

**And a mechanism for commitment nobody has framed as a lever:** swelling hypertrophic chondrocytes
*"can no longer communicate as freely with the perichondrium… **this self-constructed environment may
then partially define their development toward hypertrophy**."* **Commitment is partly a transport
event** — a positive feedback loop mediated by geometry, not signalling. Maintaining midplane access
should oppose it. Also recovered: **EXT1 loss → less heparan sulfate → longer Ihh range → extended
proliferative zone**, i.e. a tunable range-setter on the exact term Longshanks selection moved.

**My one-sided slab dies a third and final time** — *"no indication of a proposed unidirectional
entrance… generally symmetric from both the E and M vasculatures"* — and the centrifugal flow field is
*"characteristic of a **resting limb only**"*, so **the advective field is load-dependent**.

**Brighton & Schaffzin — the oxygen ceiling has a blockable mechanism.** At 90% O₂: **no reduction in
cartilage length**, but proteoglycan stainability lost, **hypertrophic zone lost**, bone component
markedly shortened — and **EACA (protease inhibitor) and chloroquine (lysosome stabiliser) partially
reversed it**. Oxygen toxicity is lysosomal and proteolytic, it attacks hypertrophy and ossification
rather than cartilage production, and it is druggable.

**Delivery is now a design constraint that favours us:** the reserve pool (where `a` is set) is the most
permeable zone measured and the most temperature-responsive; the midplane (where `b` is set) is the most
permissive band. And it filters agents before any are named — **every small-molecule lever in this
programme reaches its target and every protein lever does not**: pO₂/HIF, Hedgehog and ER blockade get
in; **GH at 22 kDa is largely excluded in vivo** (which quantitatively supports F-R035's prediction of
`chu2026`'s P = 0.1827); GREM1/FRZB/DKK1/SFRP5 at 20–40 kDa **cannot be delivered as protein and must be
induced in situ** — which is exactly why hypoxia/HIF or Hedgehog is the right *shape* of intervention.

**Chased myself rather than asked:** **Serrat 2017** obtained on retry — **IGF-I (7.6 kDa) is readily
taken up, peaks in the plate within ~90 min, is bioactive (>4× p-Akt), and localises to chondrocytes** —
with the perichondrium showing **IGFBP entrapment**, *"IGFBPs up to **50-fold higher** in perichondrium
than growth plate."* So for the one protein lever inside the gate, the rate-limiting step may be
**binding-protein displacement at the perichondrium**, not the matrix. And: **no human growth-plate
transport measurement exists** — every value here is rabbit, rat, mouse or pig. That absence is the
finding, and it is what unknowns #4 and #13 turn on.

---

## The twenty-eighth summary — F-R037, I checked my own "does not exist" and broke two of my own claims

Tate's instruction was to not accept my own absence claims. The three unknowns **are** genuinely
unmeasured — but hunting them found **two flaws in my stack**, one in its keystone.

**FLAW ONE — "hypoxia is the `a − b` lever" is a pool-without-flux trap.** Four independent lines:
**(a)** `leijten2012`'s own length endpoint — hypoxia expanded the resting zone **and produced a shorter
tibia**; I quoted the zone result and left the length result in a table. **(b)** `Kobayashi 2023`
(PMC9882305), fetched in full: **four genetic routes — miR-140-5p GOF (the model of human SEDN), Ldha
cKO, Acly cKO, and Fgfr3 activation — all give expanded resting zone with MORE resting chondrocytes and
SHORT bones**, all converging on FGFR3 upregulation, and the miR-140 mutant gets there via **reduced
Hif1a**, the opposite direction from my story. **(c)** `horike2026` — FGFR3-ACH knock-in, cells
*"accumulating in the resting zone instead of entering columns."* **(d)** The human experiment I hadn't
looked for: at altitude, *"independent of ethnicity or caloric status, absolute and relative **tibia
length was significantly reduced in children with lower blood oxygen saturation**"*, with **~1–2 cm of
adult stature attributable to hypoxia itself**.

> **An increased number of resting-zone chondrocytes is a signature of skeletal dysplasia, not of tall
> stature.**

And the sign flips back when you look at **delivery** rather than tension: warming lengthens, exercise
lengthens, an A-V fistula lengthens, altitude shortens. **More delivery, longer limb** — which is
F-R035's conclusion, intact. Hypoxia is withdrawn as a lever; the GREM1/FRZB/DKK1/SFRP5 niche convergence
stands, but hypoxia is not the route to it. (Calibration: the 2025 gpSSC niche review contains **zero**
occurrences of "oxygen" or "hypoxia" — unexamined, not refuted.)

**FLAW TWO — and it is the keystone.** My whole "fast must be bought in N" architecture rests on
`trompet2024` demonstrating pool expansion → length. Read against its own text, **it does not**:

- *"**neither the number nor proliferative activity of cells expressing CD73 was affected** by treatment
  with SAG at both time points tested"* — and Tomato⁺CD73⁺ *"tended to be **suppressed** on P30–P36"*,
  the exact window where the length effect is obtained. Overlap with PTHrP⁺ is only **40–50%**.
- *"proliferation in the **columnar zone of flat chondrocytes was not affected**"* — no amplification gain.
- *"the **orientation of stem cell division… is not affected** by Hh signaling"* — no shift toward renewal.
- *"**Although the mode of epSSC renewal remains to be elucidated**…"* — the authors decline to claim the
  pool grew.
- And the length gain is attributed by them to *"**an elevation in the height of the terminal hypertrophic
  chondrocytes**"* — h_term, which sits **outside** the pool equation entirely.

**So there is now no experiment showing that buying growth in N works.**

**The discriminator, and it saves the model.** Longshanks LS2 *also* had an expanded resting zone
(**+56%**) and got **longer** bones — because PZ **+37%** and cells/column **+32%** expanded with it. The
dysplasias expand the reserve while output falls; Longshanks expanded it while output rose. And
`chu2026` fig. S2L: tall and normal-height children **both** show a *"prominently enlarged resting
zone."* **Pool size is not the variable. Pool size with maintained discharge is** — which is the
conjugacy identity, unbroken.

**The central gap, sharper:** *there is no demonstrated intervention, in any species, that increases the
growth-plate stem pool while maintaining output.* Every agent that raises the pool blocks the exit; every
agent that raises output spends the pool. **No counterexample exists in the record.**

**Still wanted:** `trompet2024` **Supplemental Figures 2 and 5** (the CD73 panels, the division-orientation
panel 2M, and 5E/5F — the terminal-cell-height data on which §2 turns); **`horike2026`**, the cleanest
published case of expanded RZ with short bones; and **Bailey 2007**, *"Tradeoffs between oxygen and energy
in tibial growth at high altitude."*

---

## The twenty-ninth summary — F-R038, the lever was real and pointing the other way

**`trompet2024` supplement — flaw two refined, and I was unfair in one direction.** Supplementary
Figure 2 is titled by the authors *"Intraperitoneal injections of SAG **do not alter the number or
proliferation of CD73⁺ cells**"* — so the negative is theirs, not my inference. **But its power is 0.1648
and 0.3323** (n = 3/5, 3/3), which is uninformative rather than null. The fair statement is symmetrical:
at this n, **neither the claim that SAG expands the stem pool nor the claim that it does not is
supported.**

**Supplementary Figure 5 confirms the substance.** Femur, bead, paired t-test: **plate height ns / ✱✱ /
ns** and **terminal hypertrophic cell height ns / ✱ / ns** at 1 week, 1 month, 2 months; **Ki67 in the
proliferative zone ns**; OARSI joint score at 6 months **ns** (no joint damage). **The entire significant
mechanism is two panels at one timepoint, and h_term is one of them.** So the corrected flaw two: the
length gain is solid and durable; the only mechanism it can point to is **h_term** — which sits
**outside the pool equation**, i.e. the one free direction the conjugacy identity permits.

**`horike2026` read — a clean negative that removes a candidate.** Expanded resting zone in
achondroplasia comes from *"disruption of turnover… **accumulation of cells in the resting zone**"*, by
lineage tracing. And the restoration trap is resolved: *"administration of 666-15 **significantly changed
neither weight, femur length, nor expression of CD73 in the resting zone in control mice**… not effective
in a physiological condition."* **CREB inhibition does nothing to a normal mouse.** The atlas ranked it
third among pool levers with CORR-203 unresolved; it is now resolved, negatively. (Also kept: **cystine-
dense peptides and octaarginine preferentially accumulate in cartilage** — a cartilage-targeting carrier
chemistry whose **cationic** charge matches Williams's charge hypothesis exactly.)

**`bailey2007` read — and it explains flaw one through glucose, not oxygen.** 113 children at 3100 m:
*"independent of ethnicity or caloric status, absolute and relative **tibia length was significantly
reduced in children with lower blood oxygen saturation**"*, and *"in hypoxemia, body fat has less impact
on growth than when ample oxygen is present."* Their model: *"in hypoxemia, **glucose metabolism will be
downregulated**."* Put beside `Kobayashi 2023`, the chain closes:

> hypoxaemia → glucose metabolism down → glycolytic flux down → citrate/**acetyl-CoA** down → histone
> acetylation down → **FGFR3 up** → resting-zone turnover disrupted, cells accumulate → **expanded RZ,
> short bones**

Human epidemiology, mouse metabolic genetics and mouse FGFR3 genetics on one pathway — and it runs
through **glucose, not oxygen**, which is what Brighton said in 1971 when he found the plate
*"predominantly glycolytic"* and barely oxygen-consuming.

> **My F-R034 §7 lever was real. Its sign was inverted.** Lowering pO₂ suppresses glycolysis, starves
> acetyl-CoA, de-represses FGFR3 and jams the reserve — the dysplasia phenotype. The corrected direction:
> **raise glycolytic flux / acetyl-CoA → more histone acetylation → FGFR3 down → turnover restored →
> longer bone.**

It is also the first candidate in this programme that clears the transport gate by construction —
**acetate is 59 Da**, and Kobayashi names the route: *"Ac-CoA is generated from… **dietary acetate via
Acetyl-CoA synthases**"*, with **Acss2-mediated synthesis from acetate** shown to partially compensate in
these very cells.

**And the caveat, which is the trap that just killed CREB.** Kobayashi tested **only loss of function**.
I searched the full text: **zero occurrences of "rescue", "restored", "supplementation", "HDAC", or any
gain-of-glycolysis experiment.** Nobody has raised acetyl-CoA in a normal growth plate and measured bone
length. **Five converging lines on direction, no test of the gain arm — exactly where CREB inhibition sat
until someone tried it in wild-type mice and it did nothing.** Recorded as the best-supported open
candidate, explicitly not as an answer.

**Closed this round:** CREB is not an elevation lever; the Trompet supplement shows h_term at one month
and CD73 at power 0.16; the human hypoxia negative holds and now has a mechanism. **Open, top-ranked:**
does raising glycolytic flux/acetyl-CoA in a normal plate lengthen bone — untested, and now the highest
-value experiment in the programme. Nothing is retrieval-blocked; `Kobayashi`'s GEO series **GSE192971**
and **GSE98309** are public and I can pull them myself.

---

## The thirtieth summary — F-R039, the antagonism dissolves: the closure arm is local

Since F-R028 this branch has carried an unresolved tension it logged as U12 and never answered: every
human with ER or aromatase loss grows **slowly** (0.3–1.3 cm/yr), and the pubertal spurt is
oestrogen-driven — so "never close" and "fast" looked antagonistic *through oestrogen itself*. If true,
that is fatal to the goal.

**It is not true. The two arms run through different tissues, and the separation is demonstrated
genetically.** The **Col2α1-ERα⁻/⁻** mouse — ERα deleted **only in cartilage** — against whole-body ERα⁻/⁻:

| | whole-body ERα⁻/⁻ | **cartilage-only** |
|---|---|---|
| growth during sexual maturation | **reduced**, shorter bones | **normal** |
| serum IGF-I / GH secretion | **significantly reduced**, disturbed | intact |
| old age | continued; **tibia +8.3%, plate height +18%** at 16–19 mo | **continued** |
| **supraphysiological E2 challenge** | plate height reduced | **NO reduction, either sex** |
| E2 on bone mass, uterus, thymus | — | **normal in both** |

> *"**indirect, probably GH/IGF-I-mediated effects NOT requiring ERα in growth plate cartilage** are
> responsible for the role of ERα to modulate skeletal growth during early sexual maturation"* — and
> *"this effect was **not seen in either female or male Col2α1-ERα⁻/⁻ mice**, demonstrating an
> **essential role of cartilage-located ERα**"* for E2-induced plate reduction.

**Deleting ERα in cartilage alone gives a normal pubertal spurt, normal systemic oestrogen action,
complete resistance to E2 closing the plate, and continued growth into old age.** And it explains the
human cases: aromatase deficiency and whole-body ESR1 loss remove oestrogen action *everywhere*,
including the GH/IGF-I amplification that drives the spurt. **Their slow growth is a property of a broken
systemic axis, not of an open plate** — the two have been confounded in every round of this branch until
now.

The mechanism lands on the right compartment: in WT the E2 reduction was *"due to a reduction of the
**proliferative zone**, while the hypertrophic zone was unchanged"* — that is `A`, the same term
Longshanks moved. And the mirror confirms the direction: **ERαAF-1⁰ mice carry a hyperactive ERα**, growth
ceased, tibia **−4.9%**, and *"the proximal tibial growth plates were **closed in all** old ERαAF-1⁰ mice
while they were **open in all** WT mice"* — with closure running through a pathway that *"does not
require ERα AF-1."*

**What it changes:** never-close no longer costs velocity. **"Fast" stops being a fight against closure
and becomes "hold the pubertal state."** Sustained normal pubertal velocity — ~8–10 cm/yr — held
indefinitely requires exceeding no human rate ever observed; it requires holding one. **What it does not
show:** mouse plates don't normally fuse; "normal growth" is normal, not enhanced; and **no human has a
cartilage-restricted ER defect** — every human datapoint is the *slow* configuration.

**The acetyl-CoA lever takes a hard hit.** The one accessible way to raise histone acetylation in humans
points the wrong way: **valproic acid, an HDAC inhibitor at therapeutic concentrations, is associated with
short stature in children**, *"markedly suppressed"* metatarsal longitudinal growth, and represses
Sox5/Sox6/Sox9/Col2 — with a COX-2 → caspase-3 → apoptosis mechanism. Mechanistically expected too, since
**HDAC4 represses hypertrophy**, so global HDACi de-represses it. And I checked the gain arm at source:
**GSE192971**, verbatim — *"To test the consequence of **reduced** glycolysis and **reduced** cytoplasmic
acetyl-CoA."* Both GEO series are loss-of-function by design. **Downgraded** from best-supported candidate
to "coherent chain, human negative on its only accessible proxy." The chain still explains the *failure
mode*; running it backwards as therapy does not follow.

**Needed:** **Börjesson AE et al., JBMR 2010, PMID 20564247** — *"The role of estrogen receptor α in
growth plate cartilage for longitudinal bone growth."* **Not open access, no PMC record** (checked). It is
the primary behind every Col2α1-ERα⁻/⁻ result above and this round rests on the same group's review
account of it.

---

## The thirty-first summary — F-R040, the theory and its complete flaw register

**Börjesson 2010 read in the primary; every F-R039 claim holds, with numbers.** At 17 weeks (male):
total ERα⁻/⁻ had reduced femur *and* crown-rump length with **serum IGF-1 −20% ± 6% (p<0.01)** and
**liver MUP −24% ± 18% (p<0.05)**; **Col2α1-ERα⁻/⁻ was normal on all of them** (IGF-1 +14% ± 7% ns).
Under E2 challenge (830 ng/d): controls lost plate height and terminal cell height (10.5→9.6) with BrdU
770→**485✱**; the knockout held plate height and terminal cell height (10.5→**10.5**) — while uterus,
thymus, fat and every BMD measure responded **identically** in both. At one year, continued growth and
increased femur length with **serum IGF-1 −3.0% ± 6.5% ns**. And the human split confirmed at source:
*"Estrogen therapy resulted in rapid growth plate closure in patients with aromatase deficiency **but not
in the man with a mutation in the ERα gene**."*

**A new velocity lever, with the sign I have never seen before.** *"Region-specific effects of blocking
estrogen receptors on longitudinal bone growth"* (J Endocrinol 2021;250(1), PMID 34014834): **ERβ blocking
INCREASED appendicular elongation (P<0.01)** while ERα blocking suppressed it (P<0.05), with Col2,
aggrecan, Sox9, ColX, MMP13 and Runx2 all up and **local IGF-1 unchanged**. **The two oestrogen receptors
have opposite signs on limb growth** — nothing in this branch had considered ERβ.

**And a genuine structural flaw, confirmed twice: this is a limb theory, not a height theory.**
Börjesson: crown-rump **2.1% ± 1.7%, ns**, and *"increased **appendicular but not axial** skeletal
growth… resembles the **eunuchoid habitus**."* Independently: *"**ERs appeared not to affect axial bone
growth** during puberty."* **Sitting height is roughly half of adult stature, and this theory does not
reach it.**

**The full flaw register (F-R040 §3), twelve items.** The load-bearing ones: the E2 protection may be
**partial** (BrdU 795→554, −30%, ns against controls' −37%✱ — height was protected, proliferation may not
have been); **mouse plates don't fuse**, so every murine "never close" result is a slowing, and the human
receptor-level evidence is **one patient**; **no human has a cartilage-restricted ER defect**, so the
central claim has no human instance; **still no velocity lever that spares the pool**; and a mechanical
ceiling on "unlimited" that is not a risk preference — **bone strength scales as L², load as L³**.

**FLAW 7 is the crux and it names the experiment that decides the stack.** The stack shape is *sustain
systemic GH/IGF-1 + block cartilage ERα locally*. But GH depletes the pool and oestrogen *"accelerates
the proliferative exhaustion, and thereby senescence"*. **Does removing cartilage ERα protect against
GH's pool cost, or are they additive? Nobody has run GH on a Col2α1-ERα⁻/⁻ animal.**

**Closed to date:** Term A's mechanism at receptor and tissue level; the Term A/C antagonism dissolved;
the conjugacy identity; the transport map; oxygen as signal not supply; parallel-column geometry.
**Eliminated:** hypoxia as a pool lever, CREB inhibition, global HDAC inhibition, GH as a direct in-vivo
plate lever.

**Wanted:** **PMID 34014834** (region-specific ER blocking) — closed access. Anything primary on
**vertebral growth-plate cessation control**. Everything else remaining is experiments, not documents.

---

## The thirty-second summary — F-R041, two receptors with opposite signs, and a hole in Term A

**`jin2021` read in full — the best-shaped lever in the programme.** PHTPP (selective ERβ antagonist),
**0.3 mg/kg/day i.p., 5 d/wk, 4→12 weeks**, female C57BL/6, n=6: **femur length ↑ (P<0.01)**, **GP height
↑ (P<0.01)**, **PZ ↑ with HZ unchanged**, **PZ/HZ ratio the highest of any group**, **PCNA ↑**, **TUNEL
unchanged**, **PTHrP ↑ / Ihh ↓**, local IGF-1 unchanged, and **serum GH and IGF-1 higher**. The authors:
*"ERβ blocking can promote appendicular bone growth via the **Ihh/PTHrP signaling pathway rather than the
GH/IGF-1 pathway in situ**."*

It is the right shape for five reasons: it moves **`A`** specifically (PZ up, HZ unchanged — the exact
signature of the term Longshanks moved and the term Börjesson showed E2 suppresses); it is not an
apoptosis artefact; PTHrP↑/Ihh↓ is `b` down, reached from a new pathway; it *raises* the systemic drive
rather than costing it; and **systemic dosing worked, so it needs no cartilage targeting.**

**And MPP validates the ERα story from the other side:** systemic ERα blockade *decreased* femur length,
GP height, PZ and PCNA — reproducing whole-body ERα⁻/⁻ and every human aromatase/ESR1 case. **Systemic
ERα blockade loses the spurt; that is why the ERα arm must be cartilage-restricted.**

**FLAW 1 (limb-only) substantially repaired — by the other receptor.** Chagin 2004: *"Young adult
ERβ⁻/⁻ mice demonstrated an increased **AXIAL- and APPENDICULAR**-skeletal growth… ERβ is a physiological
inhibitor of appendicular- and axial-skeletal growth."* ERα is appendicular-selective (ERα⁻/⁻ crown-rump
**98% of control**); **ERβ inhibits both.** Residual: 8 weeks of PHTPP during puberty did *not* move
lumbar length, while lifelong genetic ERβ⁻/⁻ did by 4 months — so duration or completeness matters.

**NEW FLAW, and it is in Term A which I had called solved.** Chagin 2004: *"the growth plates were
**consistently FUSED in the appendicular skeleton of 18-month-old female ERα⁻/⁻ mice**… **must be
mediated through ERβ** because old ERα⁻/⁻β⁻/⁻ mice displayed **unchanged, unfused growth plates**."*
**Blocking ERα alone does not give permanent non-closure.** Every never-close result this branch relied
on is an ERα result, and Börjesson stopped at 12 months; Chagin went to 18 and found fusion. Caveats that
bound it: the driver is compensatory hyperoestrogenaemia specific to the whole-body KO (*"the ERα⁻/⁻ and
ERα⁻/⁻β⁻/⁻, **but not the ERβ⁻/⁻**, mouse models have clearly increased serum estradiol"*), which a
cartilage-restricted block should not produce; and the human ERα-mutant man resisted 10× oestradiol with
ERβ intact. **But it proves ERβ can mediate fusion given enough oestrogen for long enough.**

> **The theory converges on two receptors, and they do not cancel.** Block **ERβ systemically** — raises
> `A`, raises PCNA without apoptosis, raises serum GH/IGF-1, **reaches the spine**, and **closes the
> ERβ-mediated fusion escape**. Block **ERα in cartilage only** — removes local closure and age-related
> slowing while preserving the systemic spurt.

**`henry2012`** read for completeness: postnatal Sox9 inactivation causes stunting, reduced proliferation
and de-differentiation — Sox9 is **required**, but this is loss-of-function only, so it is a downstream
marker, not a lever with a gain arm. Same trap as CREB and acetyl-CoA; recorded, not promoted.

**Flaw 5 now has its first real candidate — PHTPP — with the test named: the stem pool was never measured
under it.** Flaw 7 (GH × cartilage ERα) unchanged and still the crux.

**Needed: Chagin AS et al., JBMR 2004, PMID 14753739, DOI 10.1359/jbmr.0301203** — not OA, no PMC. It is
load-bearing twice: the magnitude of the axial+appendicular gain in ERβ⁻/⁻ mice (the velocity number for
the whole ERβ arm) and the 18-month fusion histology. Lower priority: **Lindberg 2001** and **Vidal 1999**.

---

## The thirty-third summary — F-R042, the ERβ gain is transient, and the human RCTs confirm the stack shape

**Chagin 2004 read in the primary. The abstract sells an increase; the results price it.** The
amplification effect is real and large — proximal tibia at 4 months, **proliferative chondrocytes per
column 6.1 ± 0.1 (ERβ⁻/⁻) vs 3.9 ± 0.3 (WT), +56%, p<0.001**, with hypertrophic cells *down* 2.5→1.5.
That is `A` moving further than 20 generations of Longshanks selection achieved. **And then it does not
translate:** femur length increased at 2 and 4 months but **not at 18**; crown-rump increased at 4 months
but **not at 18**. Calcein labelling at 4 months: **ERβ⁻/⁻ growth velocity was already equal to WT** —
*"the increased appendicular skeletal growth… **must have occurred before 4 months of age**."*

> **ERβ deletion front-loads growth and the advantage is gone by 18 months.** For it to disappear, WT
> must out-grow the knockout after 4 months — the ERβ⁻/⁻ plate stopped while WT kept going.

**That is the conjugacy identity, confirmed a fourth time.** GH, oestrogen, Hedgehog and now ERβ have each
produced early gain followed by convergence. **The identity is no longer a model; it is the observed
behaviour of every lever tested.** Lindberg 2001 supplies the mechanism — *"the effects on longitudinal
bone growth were **correlated with similar effects on serum levels of IGF-I**"* — so the ERβ effect is
substantially a **systemic IGF-1** effect, i.e. a drive lever in disguise, which is exactly what
front-loading predicts. (Vidal 1999: ERα⁻/⁻ femur **93%**, crown-rump **98%**, serum IGF-1 **−23%**.)

**Two corrections to F-R041.** The axial repair was overstated: the CR gain is transient, and **mouse
vertebral plates never fuse in any genotype** — *"the vertebra growth plates were open at both 4 and 18
months… no differences between the different genotypes"* — so **no mouse experiment can inform human
spinal fusion.** FLAW 1 reinstated. And DERKO growth is *"intermediate"*, so **the double block gives open
plates at 18 months with roughly normal velocity** — Terms A and B, not C.

**Then the search I said I would run rather than ask for returned the most useful clinical result of the
programme.** Looking for growth endpoints measured past skeletal maturity:

> **Delay alone fails. Delay plus drive works.**
> Letrozole alone in ISS: **+5.9 cm predicted adult height on treatment, "no statistically significant
> difference in AH"** — gains reversed (RCT). In pre/early-pubertal boys: **164.8 ± 4.0 vs 163.7 ± 3.7 cm
> placebo, null**. GnRHa alone in ISS: *"insufficient evidence."*
> **GnRHa + rhGH: 6–9 cm in GHD (*"NAH difference close to 10 cm"*), 5–10 cm in ISS, +2.8 to +4.3 cm in
> CPP by meta-analysis — sustained, RCT-confirmed.** AI + rhGH: *"more than rhGH or AI alone"*, and
> *"considerably greater if patients were treated for **at least 36 months**"* — but **adult height never
> collected**.

**This was the model's prediction and it is confirmed in humans.** F-R039–R041 argued that *systemic*
oestrogen blockade removes the GH/IGF-1 amplification driving the spurt (whole-body ERα⁻/⁻ IGF-1 −20%;
MPP lowers femur, plate height, PZ and PCNA; Vidal −23%). **Delay without drive should buy nothing at
adult height — two randomised trials say it buys nothing.** Restoring drive pharmacologically recovers
5–10 cm.

**What the theory adds over the existing clinical stack:** GnRHa abolishes the endogenous spurt so GH must
substitute, and GH itself depletes the pool (`chu2025`). **A cartilage-restricted ERα block would delay
closure while leaving the endogenous spurt intact** — no substitution, no imported pool cost. That is the
one structural improvement proposed here, and it now has a human benchmark to beat: **5–10 cm.**

**New flaw 13:** durability is almost never measured. Every positive in this programme is ≤12 weeks, ≤6
months, or a single late timepoint — and **the only study that followed to 18 months is the one where the
advantage vanished.**

---

## The thirty-fourth summary — F-R043: the identity integrates, and the stack falls out of the closed form

**The equation was never solved. Solving it reorganises the whole problem.** With `influx = 0` — now
settled, because the Axin2⁺ groove-of-Ranvier population does *"appositional (**transverse**) growth"* and
F-R033's parallel-column geometry gives width no length term — `dn/dt = λn(a−b)` integrates, and the
finite case has an asymptote:

> # L∞ = A · h_term · n₀ / (b − a)

**`λ` does not appear.** It sets the rate and not the total. **`A` and `h_term` are free multipliers** —
they scale the total linearly and appear nowhere in `dn/dt`. **`(b − a)` is the only term in the
denominator**, so it alone decides whether the total is finite.

**Which retires the assumption this branch carried since F-R024: fast and unlimited are not antagonistic.**
They looked antagonistic because every lever the field has tested — GH, oestrogen, Hedgehog, ERβ — moves
`λ`, and `λ` is the one term that trades. `A` and `h_term` raise rate *and* total at once. And "unlimited"
and "never close" turn out to be the same instruction: **drive `(b − a)` to zero.** There were never three
problems.

**The agent the theory said could not exist, exists.** FLAW 8 said a cartilage-restricted ERα block needed
targeted delivery that nobody had built. But closure has a **local effector downstream of the receptor**:
*"estrogen induces **CXXC5** expression and subsequently inhibits the Wnt/β-catenin pathway, resulting in
growth plate senescence"* (Life Science Alliance 2019;2:e201800254). `Cxxc5⁻/⁻` mice: senescence delayed,
tibiae longer at 12 weeks. **KY19382** — dual CXXC5–DVL / GSK3β inhibitor, IC₅₀ 19/10 nM, orally active —
at **0.1 mg/kg/day in wild-type mice** for ten weeks lengthened tibiae (P < 0.0005) and raised cells per
column in **all three zones**, with no cartilage or liver pathology. **Blocking the effector instead of the
receptor leaves the systemic GH/IGF-1 spurt untouched by construction: cartilage restriction stops being
necessary rather than staying unsolved.**

**FLAW 1 — limb-only — is repaired, by arms I was not looking at.** **CATSHL** (partial FGFR3 loss of
function, p.R621H) gives **mean adult male height 195.6 cm, 5/5 men >97th centile, and tall vertebral
bodies**; **CNP-transgenic mice are +19% with overgrowth of "long bones of limbs, vertebrae and skulls."**
The oestrogen arms never reached the spine. The arms the stack actually rests on do.

**And both have wild-type gain arms — the thing F-R038/R040 said no candidate had.** TYRA-300 in normal
C57BL/6: **femur +8.2%, tibia +6.4%, nasoanal +7.3%** in four weeks. CNP22 on wild-type tibiae: +31–42%.

**The stack:** navepegritide (`h_term`, licensed Feb 2026, **bone age not advanced at 104 weeks**) +
infigratinib or dabogratinib (`A`; note the paediatric dose is titrated against a *hyperactive* receptor
and sits **25–100× below** what moved a wild-type plate) + KY19382 (`b − a`, no human exposure).
Human-validated fallback for the third arm: GnRHa/anastrozole/oxandrolone **plus** GH — 5–10 cm, +2.7 cm,
RCT-confirmed, and **delay alone is null at adult height**, exactly as `L∞` predicts.

**Eliminated:** the whole SERM class (**tamoxifen causes chondrocyte apoptosis and permanent growth
arrest; raloxifene is an ERβ *agonist* and *induces* fusion**); mTORC1 activation (**pool expands, bones
do not** — a pure identity trade with the length side empty); Ranvier influx (transverse only).

**New flaw 14, and it is the one that decides the stack:** KY19382 works by **raising** Wnt, but
*Apc*-haploinsufficiency raises Wnt in PTHrP⁺ cells and **cuts them 35–40%**, and the first human
growth-plate atlas puts the root stem cells in a niche *"low in WNT and TGF-β."* Two of three say Wnt-high
is where stem cells go to die. **New flaw 15:** the FGFR3 dose gap above.

**The honest position:** the equation now says what to build and in what order; two of three arms are
licensed or phase-3-positive with human tall-stature genetics behind them; and the arm that decides whether
the answer is "a lot" or "unlimited" rests on one 2019 mouse paper and one unresolved contradiction.

---

## The thirty-fifth summary — F-R044: yes we still close, and I killed the wrong influx term

**Direct answer, in three parts.**

**The oestrogen arm — no, and it is already solved in humans.** *"**Epiphyseal fusion never takes place** in
men with estrogen deficiency or estrogen resistance."* Aromatase deficiency: **204.5 cm at 24**, steady
growth, no spurt. ESR1 resistance: **204 cm at 28**, still growing. And Morishima's patient closes the loop
in both directions — continuous growth into adulthood that **ceased on Premarin**, with *"all epiphyses of
the hand and wrist completely fused **within 6 months**."* **"Never close until needed" is a dosing
decision, not a research problem.** It also reframes F-R042's letrozole null: those RCTs tested 2–3 years of
*partial* suppression, not the mechanism.

**The matrix arm — new, and it does not need the pool to run out.** The aged plate silts up: mineral first
(scattered deposits from W10), then aggrecan and Col II down, Col X and MMP-13 gone, and at W55 *"the growth
plate **remained calcified cartilage**."* This is F-R036's mineral barrier arriving from the other side.
**MGP-null mice, Keutel syndrome and fetal warfarin syndrome all show excessive growth-plate calcification
and short stature; Enpp1⁻/⁻ mice have "markedly thinner growth plates" restored by ENPP1-Fc.** Two
physiological inhibitors — carboxylated MGP (vitamin K-dependent) and pyrophosphate — keep the upper plate
uncalcified, and **nobody has ever raised either in a normal plate.**

**The exhaustion arm — yes on the old model, but the model was wrong.** F-R043 set `influx = 0` because the
Axin2⁺ Ranvier cells do transverse growth. True, and irrelevant: **the relevant source is inside the plate.**
**FoxA2⁺ cells sit at the *top* of the resting zone (PTHrP⁺ sit at the bottom) and are an order of magnitude
longer-lived — 9% reach passage 9+ versus 1.4% of PTHrP⁺ reaching passage 5.** Their column contribution
*rises* with age, 1% at one month to **26% at nine months**. And after injury they show **2.7-fold expansion
in 3 days**, rebuild **96% of the plate in a week** as real physeal cartilage, **without costing
longitudinal growth**, with **symmetric self-renewal confirmed by serial transplant and dye dilution.**

> **`a > b` is not hypothetical. It has been demonstrated in a mammalian growth plate. Every "pool
> depletion" result in this branch, `chu2025` included, measured tier one.**

**The design rule inverts.** `λ` is absent from `L∞`, and §1 says the plate can be held open indefinitely —
so **time is free and λ is worthless. Never buy speed with λ.** Speed comes only from `A` and `h_term`.
Which means the stack needs a **quiescence-*preserving*** agent — the opposite of everything the field does.
The circuit is named: **BMP maintains quiescence, Wnt and Hedgehog break it, Gsα and Gq/11α downstream of
PTH1R are required to sustain it**, and the review's own warning is that *"releasing RZ cells from
quiescence… risks stem cell depletion."* **PTHrP is the uniquely well-shaped signal — it holds the resting
zone quiescent *and* raises `A` by delaying terminal differentiation — and its human agent, abaloparatide,
already exists.**

**Erdafitinib, accepted.** Its human record adds the thing the theory needed: **a child growing at 10 cm/yr
with oestradiol <5 pg/mL and IGF-1 at −3.8 SD** — *"growth acceleration independent of sex steroids and
IGF-1."* Drive that needs neither oestrogen nor the GH axis. **Two honest corrections:** its bone-age
sparing is **confounded** (both patients hypogonadal, so bone age could not advance anyway — the
unconfounded evidence is navepegritide's), and **the failure mode matters more than the velocity** —
physeal widening, metaphyseal sclerosis, kyphoscoliosis, and SCFE as *"a major on-target adverse event"* are
one syndrome: **the plate outran its own mineralisation.** That is a hard ceiling on `A`, and it collides
with the anti-mineralisation arm above. Sharpest internal conflict in the design.

**KY19382's five issues each have a fix:** use **KY19334** or **PTD-DBM** (CXXC5–DVL only, no GSK3β arm);
cap the dose at restoration of the juvenile Wnt set-point rather than elevation; cartilage-target it
(octaarginine / WYRGRL / CBD precedent); PTD-DBM's human topical programme is the only PK anchor; and
**count FoxA2⁺, not just CD73 and PTHrP.**

**And the reason nothing has ever worked may be a screening artefact.** A λ lever shows early gain and late
convergence. A true `(a−b)` lever shows **little early gain and late divergence**, because pool divergence
has time constant `1/(λ(a−b))` and resting-zone cells are slow-cycling. **Every trial in this field measures
AGV at 52 weeks — an endpoint that scores front-loaders as successes and the one class that could deliver
unlimited growth as a failure.**

**Bottom line: the three goals are orthogonal for the first time in 44 rounds.** Oestrogen ablation holds
the plate open and closes it on command; `A` and `h_term` supply speed without touching the clock; tier-2
recruitment supplies cells. **What stands between this and infinite is not a mechanism — it is that nobody
has counted FoxA2⁺ cells past twelve weeks.**

---

## The thirty-sixth summary — F-R045: the exhaustion model is dead, and three of the four papers that killed it were the ones I asked for

**The premise underneath forty-four rounds — a finite stem pool that is spent and cannot be refilled — is
not supported by the primaries.**

**Nilsson 2005, read at source, says the opposite of what it is cited for.** Resting-zone chondrocytes from
**fetal, 4-week and 16-week rabbits underwent 13.1 ± 1.1, 14.6 ± 0.6 and 14.3 ± 0.8 population doublings —
P = 0.36.** *"Previous proliferation in vivo had **no effect** on subsequent proliferation in vitro."* And
methylation **did not fall in culture — it rose**, +0.21% per doubling, because *"**maintenance methylases
were upregulated when the cells were placed in cell culture**… loss of cell–cell or cell–matrix
interactions."* Telomeres excluded three ways. Methylation fell in the **slow** resting zone, not the fast
proliferative zone — the wrong ordering for a per-division counter. **Take the cell out of the plate and
its clock resets. The limit is the niche, not the cell.**

**Chu 2026 rejects exhaustion by name.** *"A notable feature of human pubertal growth plates is the **large
RZ, which comprises nearly half of the structure**. **This challenges the long-standing hypothesis that
growth ceases because of the exhaustion of chondroprogenitors** [ref 52 = Nilsson & Baron 2004]. Instead…
growth cessation might involve **active remodeling of the stem cell niche**… by elevating hormones such as
estrogens and GH."* Also: **PTH1R is the most abundant endocrine receptor in the human growth plate**;
**GHR peaks in the root stem cells and IGF1R in the hypertrophic cells**; GH raises phospho-STAT5
**in the resting zone** (P = 0.034) and S-phase fraction (P < 0.001) — `chu2025`'s pool-spending, now on
human tissue; and the **root niche is low in WNT *and* TGF-β**.

**Rochira 2010 Table 2 is the cleanest human proof that duration beats drive.** Four adult men with
aromatase deficiency: heights **190.0 / 183.5 / 191.8 / 193.0 cm**, bone ages **14.8 / 15.0 / 15.3 / 15.5**,
all radial epiphyses open — with **GH peaks of 2.0, 1.5, 1.0 and 2.8 µg/L** against a cutoff of ≥11.
Oestrogen closed every plate within six months and bought **~1 cm**. **Bone age is not a clock that runs on
time; it runs on oestrogen, and without oestrogen it stops.** This retires F-R042's "delay alone buys
nothing" — those RCTs tested 2–3 years of *partial* suppression.

**The erdafitinib record, complete.** Index case: male **15 y 4 m**, Tanner 2–3, **7 mg/day → 5 mg/day**,
**14.3 cm in 9 months = 19.06 cm/yr**, centile 16–25th → 70th — with **normal GH, IGF-1 and IGFBP-3**, and
**bone age 14.0 at chronological 16.2, still 2 years delayed 15 months after stopping.** Growth without
maturation, unconfounded. FDA series (n = 5, median onset 137 d): **two SCFE at 84 and 137 days, both in
obese patients**; three accelerated-growth cases, **none obese**. ALP 746 U/L, DEXA −3.8 SD, kyphoscoliosis
with cord compression. **And the mechanism sets a constraint: erdafitinib alone is apoptotic (PARP, cleaved
caspase-3); IGF-1 via sustained AKT completely rescues it.** So F-R044's "drop GH" was half right — GH as a
*driver* stays out, but **IGF-1/AKT must be preserved as a survival floor.**

**The model corrects.** `(b − a)` is not a biological constant; it is set by oestrogen and the niche, and
both are switchable. **The plate does not run out. It is switched off — and the switch has been in clinical
use since the 1990s.** The binding constraint moves from cells to structure: SCFE at 84 days under load,
kyphoscoliosis at 9 months, ALP 2× normal, DEXA −3.8. **So do not run at 19 cm/yr.** Run the `A` arm at the
rate the ossification front and the hips will carry, with **abaloparatide** behind it — which holds RZ
quiescence, raises `A` by delaying hypertrophy, hits the plate's most abundant receptor, *and* is the
strongest bone anabolic available — and take the height out of **duration**, now the cheap resource.

**Two arms removed, one of them mine.** **CXXC5/KY19382 downgraded** — its mechanism is Wnt elevation and
the human root niche is Wnt-low (three independent lines). **TGF-β inhibition rejected before it landed** —
the niche is TGF-β-low but Tgfbr2 deletion accelerates hypertrophy. One rule covers both: *the root niche
wants low WNT and low TGF-β; the maturing compartment needs both, and no systemic agent can tell them
apart.*

**What I need now is the mechanical envelope, not the biology:** the two SCFE primaries (Farouk Sait 2023;
Brizini 2024), any FGFR-inhibitor dose–response for growth — **the most useful missing number is the dose
that gives 6–8 cm/yr instead of 19** — and one experiment: **count root stem cells in the resting zone of
an adult with an open plate.** If they are there, `(b − a) = 0` is demonstrated in a human and the question
is closed.

---

## The thirty-seventh summary — F-R046: PTH1R is dead, the pool question resolves into two clocks, and the full stack

**Teriparatide and abaloparatide: no. You and the atlas were right and I was wrong.** Winer's children with
hypoparathyroidism took **PTH(1-34) at 0.75 ± 0.15 µg/kg/day for up to 10 years with open growth plates**,
and *"mean height velocity was normal for age throughout the study."* Not increased. And the human
gain-of-function is **Jansen metaphyseal chondrodysplasia** — constitutively active PTH1R — which is
**severe short stature** with *"markedly expanded zones of proliferating/prehypertrophic chondrocytes…
progressive reduction of type X collagen-positive hypertrophic chondrocytes."* **That is the dysplasia
signature this branch has been flagging since F-R034: Jansen's is what "expand the pool" looks like when
you get it.** The transport map makes the null a real test rather than a delivery miss — teriparatide is
4.1 kDa and abaloparatide 3.8 kDa, and a 3 kDa tracer enters at 62%. The drug reached the plate and did
nothing.

**The pool question — two clocks.** *Endocrinology 2014;155:2892* separates them in ovariectomised rabbits
given E2 for 5 weeks then 5 weeks off. **Reversible on stopping:** growth rate, proliferation rate,
hypertrophic cell size — all normalised. **Irreversible:** plate height, proliferative and hypertrophic
cell number, and **resting zone cell number** — all stayed advanced. And the RZ loss *"did not appear to be
due to apoptosis."* Non-apoptotic loss from the resting zone means the cells **committed out**. Put beside
Nilsson 2006 — estradiol simultaneously **slowed** RZ proliferation while accelerating senescence, which
he could not explain — the picture is:

> **Oestrogen drains the pool while suppressing output. It does not spend the pool on growth; it discards
> it. Closure is not exhaustion by use — it is a controlled write-off.**

**Clock B, the slow use-linked drawdown, is real** (RZ cells per area fall with age; dexamethasone
conserves them by slowing proliferation — the catch-up growth mechanism). **But it is nowhere near
complete when growth stops:** Chu 2026 finds the human pubertal RZ is *"nearly half of the structure."*
And the cells that remain are undamaged — Nilsson 2005's 16-week cells had the same doublings left as
fetal cells (P = 0.36). **So yes, the pool persists in an adult with an open plate, and Rochira's four men
are the functional proof: bone age frozen at 14.8–15.5, epiphyses open, still growing at 183.5–193.0 cm,
with GH peaks of 1.0–2.8 µg/L. A plate cannot elongate for a decade with no progenitors.** Nobody has
stained one; the function is the assay.

**One hard consequence: the write-off is irreversible. You keep what you have when you start.** Every
month of oestrogen exposure is permanently subtracted, which sets the timing of the whole stack.

**The final equation.** `dn/dt = −λnd − w(E₂)`, giving `L∞ = (A·h_term/d)·n₀`. λ is absent — **never raise
it**. And `A` and `h_term` are not only free multipliers: **at any fixed velocity they reduce the number of
stem divisions needed per centimetre.** They multiply the total *and* slow the drawdown. That is the
cleanest reason the stack works.

**THE STACK.** (1) **Complete aromatase inhibition ± GnRHa**, E2 to undetectable on a third-generation
assay — reversed with transdermal oestradiol when height is sufficient, which closes every epiphysis in
6 months at a cost of ~1 cm. AI in males also raises non-aromatizable testosterone: drive without closure.
(2) **Erdafitinib**, 5 mg/day anchor (7 mg forced interruptions for hyperphosphataemia) — **but keep IGF-1
in range, because FGFR blockade alone is apoptotic and IGF-1/AKT rescues it.** (3) **Navepegritide**
100 µg/kg weekly — serial with arm 2, not redundant, because FGFR3 inactivates NPR2 by dephosphorylation.
(4) **Romosozumab 210 mg monthly** — chosen *by the transport map*: at ~150 kDa the size gate keeps it out
of the plate, so it builds bone without touching the Wnt-low root niche, which is exactly why abaloparatide
at 3.8 kDa was the wrong agent. (5) **Load management** — both SCFE cases were obese, neither growth-only
case was; hip films from day 60, spine films quarterly, baseline DEXA. (6) **Vitamin K2** for MGP
carboxylation. Order: arm 1 first and alone, then 4 and 6, then 3, then 2 titrated up last.

**The ceiling is now mechanical, not cellular.** Duration alone with a broken GH axis gave 189.6 cm. The
`A` arm alone gave 19.06 cm/yr with bone age not advancing. What broke was SCFE at 84 days, cord
compression at 9 months, ALP 2× normal, DEXA −3.8 SD. **So run the A arm at what the hips and the
ossification front will carry and take the height out of duration.**

**Still missing:** count root stem cells in an adult with an open plate (the experiment); an
FGFR-inhibitor dose–response for growth — **the dose that gives 6–8 cm/yr instead of 19**; a systemic
Smoothened agonist (periosteal Ihh maintains the root pool — strong mechanism, **no molecule**); and the
two SCFE primaries for the mechanical envelope.

---

## The thirty-eighth summary — F-R047: eight layers of oestrogen, five ways to get more cells, and the one arm of the proposal to change

**There are eight routes by which an oestrogenic signal can reach ERα in a growth-plate chondrocyte. An
aromatase inhibitor blocks one.**

**Layer 0 — the receptor, and it is the only complete answer.** **Fulvestrant** is *"a pure antiestrogen
with no agonistic effects, leading to degradation of ERα."* **Not elacestrant** — nonclinical data show
*"agonist effects on bone"*, and a bone-agonist SERD is the one thing you must not give. Two subtleties:
**ERβ is a proven escape route** (Chagin: ERα⁻/⁻ mice all fused at 18 months via ERβ; only the double
knockout stayed open) and fulvestrant's ERβ degradation is undocumented — which is the argument for doing
receptor *and* ligand ablation. And **do not block GPER1: it is growth-promoting.** Chondrocyte-specific
GPER1 knockouts have significantly **decreased** proliferative zone thickness and shorter tibiae, acting
*"via PTHrP/Ihh regulation."* Fulvestrant is a GPER agonist — the right sign by accident.

**Layer 2 is the hole nobody in this field has mentioned.** **Estrone sulfate is the most abundant
circulating oestrogen**, and **steroid sulfatase regenerates E2 from it entirely independently of
aromatase** — and *"increase in intratumoral STS has been demonstrated **following treatment with an
AI**… a compensatory and adaptive response."* **You give the AI, the tissue upregulates the bypass.** The
agent is **irosustat (STX64), IC₅₀ 8 nM**, through phase 1/2. It also blocks DHEA-S → DHEA.

The rest: **exemestane** (irreversible; and chondrocytes make their own aromatase — *"articular
chondrocytes possess CYP19A1 at mRNA and protein levels"* — but AIs are 285–296 Da and cross the plate in
90 seconds); **abiraterone + prednisone** to cut adrenal *and* gonadal precursor supply, with
**non-aromatizable oxandrolone added back**; **HSD17B1 inhibitors** for the potency step;
**27-hydroxycholesterol**, *"an endogenous SERM"* made from cholesterol by CYP27A1 **inside bone itself**
— lower cholesterol hard, no AI touches it; **calcium-D-glucarate** for enterohepatic recirculation; and
**eliminate soy, flax and hops** (8-prenylnaringenin is the most potent phytoestrogen known; genistein is
a potent **ERβ** agonist — the escape receptor). Verify by **LC-MS/MS measuring E1S, not just E2**, and by
bone age: in Rochira's men it froze at 14.8–15.5 for years.

**The cell problem, and five refills.** The write-off is irreversible and non-apoptotic — the cells commit
out. **(1) Ex vivo expansion, and Nilsson licenses it himself:** cells from fetal, 4-week and 16-week
rabbits gave 13.1 / 14.6 / 14.3 doublings (P = 0.36) and methylation **rose** in culture because
*"maintenance methylases were upregulated when the cells were placed in cell culture."* **Fourteen
doublings is 16,000×. The cells you have left are not the cells you are limited to.** (2) **FoxA2⁺
injury expansion** — 2.7× in 3 days, 96% regeneration in 7, growth unaffected, symmetric self-renewal by
dye dilution. (3) **Periosteal Ihh** — strongest mechanism, **no molecule exists** (only antagonists).
(4) **Partial reprogramming** — AAV-OSK in cartilage reduced senescence and DNMT expression with no rise
in stemness genes, and Chu found the **KLF4 regulon already selectively active in human
chondroprogenitors**. (5) Raising `A·h_term` cuts stem divisions per centimetre — automatic conservation.

**The proposal: two-thirds right. Drop the GH.** Chu 2026, on human tissue: **GHR is highest in GP1, the
root stem cells; IGF1R is highest in GP5, the hypertrophic cells — *"opposite gradients."*** GH raised
phospho-STAT5 **in the resting zone** (P = 0.034) and S-phase (P < 0.001), and chu2025 states outright
that *"excess GH… **depletes the stem cell pool**."* **High-dose GH is a maximum-rate drawdown on exactly
the cells you are short of.** The substitution: **mecasermin (rhIGF-1) 50–100 µg/kg BID to a normal — not
high — IGF-1.** It acts on GP5, not on the root cells, and it is the exact molecule erdafitinib needs,
because **FGFR blockade alone is apoptotic and IGF-1 via sustained AKT completely rescues it.** The reason
to want GH here is to supply IGF-1; IGF-1 supplies IGF-1 without the cost.

**Romosozumab rechecked — survives, wrong reason.** **Sclerosteosis (SOST loss) causes gigantism and tall
stature; van Buchem, with partial loss, has normal stature** — dose-dependent, in humans. But sclerostin
*"is expressed in the hypertrophic chondrocytes within the growth plate"*, and at 150 kDa romosozumab
cannot get in. **So it will strengthen bone and will not add height** — plus a 12-month approved ceiling
and a cardiovascular boxed warning. **And teriparatide comes back, for the opposite reason to the one it
was removed for:** Winer's ten years in children with open plates is not just a null, it is **the best
long-duration safety dataset for a bone anabolic in a growing human that exists.** Structural arm, not
growth arm. Jansen's stays the warning against continuous or supraphysiological dosing.

**Papers wanted, Tier 1:** **Endocrinology 2014;155:2892 (PMID 24708243)** — the only quantitative
measurement of the oestrogen write-off, and the single most important paper for the cell question;
**J Endocrinol 2006;189:27 (PMID 16614378)** — the age-by-age RZ counts and the dexamethasone conservation
data; **Farouk Sait 2023 (Pediatr Blood Cancer e30410)** and **Brizini 2024 (Front Oncol 14:1399356)** —
the mechanical envelope that sets the ceiling on the erdafitinib arm.

---

## The fortieth summary — F-R057: the turnover clock, and why every brake so far bought time instead of speed

**The identity was missing a term.** Cooper 2013 (Nature 495:375, PMC3606657), confirming Farnum's bat and
mouse work by BrdU pulse-chase: *"the entire hypertrophic zone of each growth plate turns over once in about
24 hours regardless of the maximum volume attained by individual chondrocytes, the number of hypertrophic
chondrocytes, or rate of growth plate elongation."* So **`dL/dt = N_h · h_term / τ`**. And the cell reaches
terminal size at ~12 h then **sits at that size for another ~12 h** before turnover — half the hypertrophic
lifetime is unused schedule.

**That dissolves a paradox fourteen rounds old.** **Karimian 2013 (PLoS ONE 8:e67859)** — resveratrol
200 mg/kg/d, 16 weeks, rabbits — moved **every term of the identity the right way at once**: resting-zone
area 0.11→0.26 mm² (p<0.01), hypertrophic cells/column 3.3→5.0, terminal cell size 10.5→12.4 µm, plate height
133→284 µm, BrdU **down**, apoptosis unchanged, and **fusion delayed at the distal tibia, distal femur and
proximal tibia** — the last of which sets final length. E2 moved every one of them the opposite way. **Length
gain: 1.9%.** Numerator up 1.79×, output up 2% ⇒ **τ rose by nearly the same factor.** Same for VEGF blockade
(Gerber 1999: hypertrophic zone expands *because* junction turnover is blocked; growth impaired, fully
reversible on withdrawal) and dexamethasone. **Banking agents raise the numerator *by* lengthening τ. It is
one act, not two, which is why "fast" and "unlimited" have refused to combine.**

**The jerboa separates them.** Metatarsal hypertrophic chondrocytes reach **~23,000 fl** — 4.6× the mouse
radius, 1.6× the mouse tibia — inside an unchanged 24 h envelope, by **extending Phase 3** of the three-phase
enlargement (Phase 1 true hypertrophy 600→2,000 fl; Phase 2 **swelling**, 2,000→8,000 fl at density diluted
to 0.07 pg/fl; Phase 3 mass added at the new low density). **Phase 3 is locally IGF-1-dependent** —
*Igf1^fl/fl;HoxB6-Cre* cuts terminal height 34% and stops cells dead at 7,000 fl. **The one manoeuvre that is
fast and is not a withdrawal: extend Phase 3 into the idle second twelve hours.**

**Two corrections.** (1) F-R055 read Haraguchi's *Hhip1* cKO as a clock lever; the supplied figure shows
plate area falling 0.44→0.29 in control and 0.62→0.42 in mutant — **parallel decline**. It raises amplitude
(`A`) and leaves the senescence slope untouched. (2) Karimian's discussion cites Wilsman 1996 for *"less than
10% of bone growth… linked to cell proliferation"* — that decomposes **column height**, not rate sensitivity
to λ. It means per-cell amplification is ~10×. It is not a licence to spend λ.

**Xiu constrains the Hedgehog arm to one layer:** ablating **either Smo or Sufu** in juvenile chondrocytes
causes **premature closure and shorter limbs** — the response is bell-shaped. **Remove brakes that act on the
ligand (HHIP1), never brakes that act on the transducer (Sufu, Ptch1)** — a second, independent reason
systemic SAG did nothing.

**A fourth arm, and it reaches humans already.** Fusion has an executioner arriving from outside the plate:
RES cut VEGF⁺ cells 626→265/mm² and junction laminin 515→368, while **E2 raised laminin 62%**. **Voss 2015
(COG Phase I): 5/53 children on pazopanib or sunitinib had growth-plate abnormalities — four with widening on
successive radiographs, one with physeal cartilage hypertrophy on MRI.** Reversible in rats and monkeys. The
ceiling is mechanical: Hall 2016, juvenile rabbits, plate dysplasia **and fracture** — the F-R048 envelope
from an independent direction.

**Link 11 hardened and cracked in the same round.** Karimian's OVX controls fused 16/17 distal tibiae by four
weeks — **ovariectomy does not prevent fusion in the rabbit**, confirming Weise in a second laboratory. But
that residual fusion was **delayed at all three plates by an agent with no anti-oestrogen mechanism**, acting
locally, serum IGF-I unchanged. Whatever closes the plate after the ovaries are gone is **druggable outside
the oestrogen axis** — or is the plate's own intracrine oestrogen, which only the CYP19A1⁻/⁻ rabbit separates.

**Stack status: three of four arms buy τ; only Hedgehog-at-the-ligand raises the numerator, and weakly (+43%
plate area → +4.5% length over a year). A stack of four τ-lengtheners never closes and barely grows, which
fails the brief as badly as one that grows fast and closes. Not building the oestrogen side until a
numerator-raiser with τ held fixed exists.**

**Papers wanted, ranked.** (1) **Farnum & Wilsman, Calcif Tissue Int 1997;61:323, PMID 9351885** — *"The
domain of hypertrophic chondrocytes in growth plates growing at different rates."* Closed, no PMC copy. **The
single most important outstanding paper in the branch:** the whole τ framing stands or falls on whether 24 h
is a constant. (2) **Breur, VanEnkevort, Farnum, Wilsman, J Orthop Res 1991;9:348, PMID 2010838** — the
*linear* relationship between hypertrophic cell volume and growth rate; this is the coefficient that converts
a volume gain into centimetres, missing since F-R043. (3) **Kuhn, DeLacey, Leenellett, J Orthop Res
1996;14:706** — same relationship **in the rabbit, across ages**. (4) **Wilsman 1996, J Orthop Res 14:927,
PMID 8982136** — the full eight-variable decomposition. (5) **Cooper 2013 Supplementary S3 and S5**
(`NIHMS440348-supplement-1.docx`, `-2.pdf` at PMC3606657) — *not paywalled*, PMC serves them behind a
proof-of-work bot challenge I will not solve; they open in a browser. (6) **Any measurement of τ under an
intervention** — nobody appears to have asked, and it would turn this round's central claim from an inference
into a measurement. (7) **CYP19A1⁻/⁻ rabbit growth-plate histology** (standing). (8) **Voss 2015, Pediatr
Blood Cancer 62:45** in full.

---

## The forty-first summary — F-R058: the identity closes to 0.1%, and two F-R057 claims do not survive

**Restored, having been dropped: the ALT argument for GH.** GH is **not** in this stack as a rate driver —
it is **AKT support for erdafitinib**, because FGFR3 blockade alone is **apoptotic** and IGF-1 via sustained
AKT rescues it. `STACK_STATE` had described its job as `h_term` delivery and then complained it was in the
wrong compartment; wrong job description, and the complaint answered a question nobody asked. And the
strongest single result in the branch, also dropped: **"when GH hypersecretion is accompanied by
gonadotropin deficiency, accelerated linear growth may persist for DECADES"** — all three terms at once, in
a real human phenotype, **through the systemic axis.** The dose question resolves as a **sign flip**, in the
authors' own words: *"GH augments both stem cell number and activity under physiological conditions but
causes stem cell depletion under pharmacological exposure."* **2 IU is not a compromise — it is the side of
the flip where GH adds to the pool.** 0.35 mg/kg/wk is ~5× higher and lands in the depleting range.

**The identity is not a model. It was derived in 1996 and it is exact.** Wilsman's two independently
measured equations collapse at steady state to **`dL/dt = flux × terminal chondrocytic domain volume`**
(`v(d) = v(c) + v(m)`). Tested on his own Table 2/3/4, proximal tibia against proximal radius: **flux 3.16×
× domain volume 2.67× = 8.42×, against a measured growth ratio of 8.43×.** Breur 1997 confirms it from the
other direction — best model `R² = 0.992`, exactly those two variables plus their interaction; I refit it
from his table and got 0.997. **Both factors are comparable and they multiply — which kills "λ is worthless"
(F-R044, wrong: flux is the *larger* factor) and "h_term is the free multiplier" (F-R043 on, overstated).**

**Retraction 1: τ is not a constant.** F-R057 made `dL/dt = N_h·h_term/τ` its spine. Whole-plate transit
from Wilsman's Table 2 is **1.56 / 1.91 / 2.36 / 3.85 days — a 2.46× range**, varying inversely with rate.
Cooper's "~24 h" is a narrower hypertrophic-zone claim inherited from bat/mouse forelimb work; his own
supplementary BrdU runs to **18, 30 and 42 h**. The §1 form needs no τ at all.

**Retraction 2: the jerboa is not a pure h_term demonstration.** Supplementary Fig. S3, now in hand: the
jerboa metatarsal plate is *"approximately **three-times taller in each zone**"* — resting, proliferating
**and** hypertrophic. A coordinated whole-plate scale-up, which is what the identity demands and not what I
claimed it showed. It still checks out quantitatively (Fig. S2: mouse tibia **158 ± 24 µm/day**, metatarsal
**102 ± 14.5**; a 2-point mouse slope ≈0.0093 predicts ~241 µm/day at 23,000 fl ≈ 2.4× the mouse metatarsal).
**Slopes do not transfer between species:** rat 0.0212, pig 0.0338, rabbit 0.030–0.061, mouse ≈0.0093 — and
**Kuhn's 5-week rabbit slope is ~2× the 8/12-week slope (p<0.01), with no relationship at all at 2–3 weeks.**
That is a **second senescence mechanism: conversion efficiency per unit volume degrades with age.**

**A hard ceiling I did not know existed.** Wilsman's continuous-BrdU **growth fraction is 0.89–0.99** in all
four plates. **Essentially every proliferative-zone chondrocyte is already cycling** — there is no quiescent
reserve to recruit, and any "wake up resting proliferative cells" mechanism is capped at 1–11%. Flux is
reachable only through cell-cycle time (2.47×) and PZ height (3.19×).

**Senescence and closure are carried by volume, not flux.** Recomputed from Breur's Table 1, D21→D35:
elongation −12.5 to −39.5%, **cell volume −18.7 to −41.3%, flux only −7.7 to −16.6% and *rising* 7.4% in
the proximal radius.** Kuhn gives the same dissociation *inside one bone under identical hormones*: at 12
weeks the rabbit **proximal radius is "almost fused" at v(c) = 2,590 µm³** while the **distal radius still
runs 290 µm/day at v(c) = 11,770 µm³**. **Maintenance of terminal cell volume is the signature of a plate
that stays open — and nothing in the stack defends it.**

**Correcting my own correction:** Karimian's "<10% of growth from proliferation" is **numerically right**
(Wilsman: duplication 9%, matrix 32%, enlargement 59% in the fast plate; 7%/49%/44% in the slow one).
F-R057 called it a misreading of *column height* — wrong, it decomposes **daily turned-over volume by
source**. The real error is Karimian's: a source share is not a sensitivity coefficient, since `N_lost`
multiplies through all three terms. **And matrix production is 32–49% of elongation — larger than cell
enlargement in slow plates — and this branch has never once addressed it.**

**Stack status: the identity has six levers and the stack moves one.** Erdafitinib works on cell-cycle time;
GH and abaloparatide are enablers, not terms. Growth fraction is closed. **Terminal domain volume — 2.67× of
the range, the carrier of senescence, the signature of an open plate — is untouched on both sub-levers.**
Oestrogen side still unbuilt, now with a third reason: until something defends `v(c)` there is nothing for
it to preserve.

**Still needed:** **Farnum & Wilsman, Calcif Tissue Int 1997;61(4):323–328, PMID 9351885** — *still
outstanding*; the bundle held **Breur et al., 61(5):418–425**, a different paper with a near-identical title
in the same volume, which does not measure transit time. **Cooper's reference 7** (bat/mouse forelimb, the
source of the 24 h claim). **Any measurement of terminal hypertrophic chondrocyte volume in a human growth
plate** — I have rat, pig, rabbit, mouse and jerboa and **no human number**, so every claim about human
headroom is unanchored. **Anything post-1997 on pharmacological control of matrix volume per chondrocyte.**
Plus the standing two: CYP19A1⁻/⁻ rabbit growth plates, and Voss 2015 in full.

---

## The forty-second summary — F-R059: the human number, the bat ceiling, and the lever that is not a withdrawal

**Every F-R058 request is closed. Nothing below is a paper I failed to look for.**

**τ is settled.** Cooper's reference 7 is **Farnum, Tinsley & Hermanson, *Cells Tissues Organs*
2008;187:35–47** (big brown bat). Table 4: hypertrophic-zone fraction lost per 24 h ranges **0.48–1.60**
(τ_HZ **15–50 h, 3.3×**); whole-plate **0.17–0.78** (**1.3–5.9 days, 4.6×**); terminal cell life span
**1.2–10.0 h**. Farnum calls it *"quite constant"* and immediately adds ***"the data are fairly noisy."***
**HZ transit is loosely conserved to ~3×; whole-plate transit is not conserved at all.** F-R058's retraction
was right, and my computed 1.56–3.85 d from Wilsman's rat data is confirmed in a second species by the
original measurement.

**The ceiling is a bat wing.** Same paper: **manus MC digit 4 terminal hypertrophic cell = 40,300 µm³ at
52.5 µm height; the same animal's pes carries 1,300 µm³ at 9.1 µm.** A **31× range of terminal cell volume
within one individual under one endocrine environment**, with P→H amplification ~52× in the manus vs ~2.5×
in the pes and HZ area fraction 0.7–0.8 vs 0.5. **`v(c)` is a locally-set free multiplier, not a species
constant — and the bat, not the jerboa, is the ceiling.**

**The human number exists.** **White, Wilsman, Leiferman & Noonan, *J Child Orthop* 2008;2:315–319** — a
human **distal tibial physis caught mid-closure** at 12 y 11 m, **RHT fixation and point-sampled stereology
in Wilsman's own lab**, i.e. identical method to every rat/pig/bat number. **Average hypertrophic cell volume
5,900 µm³** (range 3,600–8,400, **no significant difference across nine regions**), physeal height 980 µm,
**46% bridging bone in the middle of the central region and ~0 elsewhere.** Caveats carried, not buried:
**n = 1**, osteosarcoma treated with **cisplatin/doxorubicin/methotrexate** — which the authors note reduce
growth rate and final height — so 5,900 is plausibly *depressed*.

**This corrects F-R058.** I had written that *"maintenance of terminal cell volume is the signature of a
plate that stays open."* **That holds between plates, not within one:** cell volume was uniform across the
whole physis while bridging was focal. **Closure initiates focally in a plate whose cells are all the same
size — local volume collapse is not the local trigger.**

**Putting the human on the identity reorders the stack.** Distal tibia peak **5 mm/yr = 13.7 µm/day**
([Pritchett 1984](https://pubmed.ncbi.nlm.nih.gov/6499303/)). With `dL/dt = flux × v(d)`: **human flux
≈ 1,300 cells/mm²/day against the rat's *slowest* plate at 4,340 measured.** **The human is flux-poor AND
volume-poor at once.** Humans are tall by *lasting*, not by growing fast — and low flux **is** the mechanism
of duration, which is Gafni's banking result read forward.

> **Therefore raising flux is a withdrawal and raising `v(d)` is not.** Every extra division spends the
> account "never close" depends on; every extra µm³ converts the *same* division into more length. **`v(d)`
> is the only lever that is fast and not a withdrawal.** F-R057 reached this via a τ argument that was
> wrong; it is re-derived here from flux/senescence coupling, which is not.

**Measured human headroom:** rat prox tibia 2.5×, rabbit 3.1×, jerboa 3.9×, **bat manus 6.8×**. At constant
flux the distal tibia alone runs **10 mm/yr at 2× and 34 mm/yr at 6.8×**, against 5 now.

**Human plate ageing is the opposite of the rat's.** **Byers et al., *Bone* 2000;27:495–501** (46 children,
11 d – 13.5 y): PZ height to **34%**, HZ to **26%**, matrix fraction **60→82.5%** and **25→40%** — and
**chondrocyte lacunar diameter unchanged in both zones (ns).** **Cell number collapses, cell size is
preserved.** In the rat 21→35 d volume carried the decline. **The human slowdown is flux-limited** — which is
exactly why volume is the compartment to push.

**Matrix is two levers, and one of them is the closure pathway.** **Noonan, Hunziker, Nessler & Buckwalter,
*J Orthop Res* 1998;16:500–508** (6 mini-pigs): cell volume **1,174→5,530 µm³ (4.7×)**; matrix/cell
**8,040→11,760 (+46%)**, split **pericellular/territorial +61% (4,580→7,390)** vs **interterritorial +26%
(3,460→4,370)**; absolute cell **+4,356** vs matrix **+3,720**. Growth rate correlates with **interterritorial**
matrix/cell in the PZ but **pericellular/territorial** matrix/cell in the HZ. And the anatomy: *"the
pericellular/territorial matrix does not calcify"* while the interterritorial calcifies, and **"capillaries
invade the pericellular/territorial matrix compartment after mineralization of the interterritorial matrix."**
**That is the same door the VEGF/laminin executioner comes through (F-R057), described anatomically.**

**The volume-accelerator gap is narrower than F-R058 said.** **GH normalises terminal chondrocyte volume** in
uremic rat, authors proposing **Nkcc1 + Igf1** ([PMC7350242](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7350242/));
**CNP increases chondrocyte hypertrophy**; NKCC1 (bumetanide −35%, [PMC3154001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3154001/)),
NHE1/AE2 and local IGF-1 remain loss-of-function only. **Three lines converge on the lever and none has been
pushed above normal in a healthy plate.** **That gives GH a third candidate job — a `v(c)` agent via Nkcc1 —
on one uremic-rat study, labelled as a hypothesis.**

**Stack: erdafitinib 8 mg on cell-cycle time; GH 2 IU as AKT support, physiological side of the sign flip,
and now candidate `v(c)`; abaloparatide 80 µg on the mechanical envelope. Terminal domain volume — half the
identity, 6.8× human headroom, the only non-withdrawal lever — is still untouched.** Oestrogen side stays
unbuilt: it protects duration, and duration is currently protecting 13.7 µm/day.

**Open, and stated as experiments rather than requests:** (1) has *anything* raised terminal hypertrophic
chondrocyte volume **above normal in a healthy mammal** — searched, apparently never done, and both candidate
molecules (GH, vosoritide) are already at hand; (2) **what sets bat manus 40,300 vs bat pes 1,300 in the same
animal** — Farnum describes it and does not explain it, and the answer is by construction a local
endocrine-independent controller with 31× range; (3) the within-plate closure trigger, given White's uniform
volumes and Noonan's invasion anatomy. **Still not gettable by me:** CYP19A1⁻/⁻ rabbit growth-plate histology
(animals exist at INRAE, no skeletal phenotype published), and **Voss 2015, *Pediatr Blood Cancer* 62(1):45–51**
in full (Wiley, closed).

---

## The forty-third summary — F-R060: the executioner has a name, and erdafitinib was doing three jobs

**All three standing requests closed.** Voss received and read; **the CYP19A1⁻/⁻ rabbit question closed as
"the data does not exist"** — Jolivet's 259 pages (all supplements; Figs S1–S7 entirely gonadal) mention bone
twice in passing, and Dewaele's "body weight ratio" is *testis*/body weight. **Verified by reading, not
inferred from search.**

**The terminal step now has a molecular identity.** `serum phosphate → VEGFR2 **on the hypertrophic
chondrocyte** → Raf/MEK/ERK1/2 → caspase-9 → apoptosis → vascular invasion → junction advances.`
Sabbagh/Demay *PNAS* 2005;102:9637 (low phosphate blocks the apoptosis — that expansion **is** rickets);
Yadav/Demay *iScience* 2023, [PMID 37636062](https://pubmed.ncbi.nlm.nih.gov/37636062/) (a screen for
blockers of phosphate-induced ERK1/2 **identified VEGFR2**; chondrocyte-specific VEGFR2 depletion → more
hypertrophic cells, less apoptosis, impaired invasion). **VEGFR2 is a phosphate sensor that triggers the
cell's own death — so "the vascular arm" was never primarily vascular.** This unifies four arms the branch
had treated separately: oestrogen, vascular, mechanical envelope, transit.

**A renal route from oestrogen to closure, which appears to be new.** **Ikedo 2024** ([bioRxiv
2024.06.24.600344](https://doi.org/10.1101/2024.06.24.600344)): **osteoblast**-specific aromatase KO → *no*
bone phenotype; **adipose**-specific KO → lower tibial/femoral BMD, **increased osteoid volume and width**,
**serum phosphate ↓, renal reabsorption ↓, FGF23 ↓, renal NaPi2a/2c protein ↓.** So adipose aromatase → E2 →
NaPi2 → phosphate → the axis above. **Nothing to do with ERα on a chondrocyte.** Two opposite consequences:
it may be *part of why* oestrogen ablation delays fusion, **and** it is a named failure mode — low phosphate
plus osteoid is rickets, and a widened undermineralised physis on weak metaphysis is the SCFE substrate.
**Design rule: block the death signal at VEGFR2, not by lowering phosphate. New non-optional stack
requirement: serum phosphate monitored and repleted.**

**Voss in full overturns F-R057's vascular reading.** Patient 5, pazopanib ×10 cycles: MRI **expansion of
the hypertrophic chondrocyte layer**, rapidly reversible on stopping — and ***"no disruption in longitudinal
growth… gaining approximately 6 cm while on study."*** **The terminal step slowed while flux and volume
carried on** — the profile F-R059 said doesn't exist. F-R057's "VEGF blockade costs rate" came from Gerber's
**ligand trap** (abolishes VEGF-A entirely); **receptor-level partial blockade behaves differently.**
Incidence **5/35 = 14.3%** among anti-VEGFR2 TKI recipients specifically; cediranib and sorafenib gave none.

**The central correction: erdafitinib was never a one-lever drug.** F-R058 and F-R059 both said "the stack
moves one of six levers" and that **no agent raises terminal chondrocyte volume in a mammal.** Both wrong,
and the counter-example was the first drug in the stack. FGFR3 inhibition: **(1) flux** — PZ **+25%** in
Fgfr3 cKO; **(2) terminal cell volume** — *"significant swelling of hypertrophic cells"* (infigratinib,
*JBMR* 2024;39:765), HZ **+45%**, i.e. zone up while cell *number* falls; **(3) the closure step** — lowers
**ERK1/2**, the same node the phosphate death signal runs through. And **FGFR3 promotes closure**
(Matsushita, *Hum Mol Genet* 2009;18:227 — activated Fgfr3 → **premature synchondrosis closure** via MAPK,
BMP ligand up / antagonist down).

**And it passes the test that killed the Hedgehog arm.** **TYRA-300 in WILD-TYPE C57BL/6J**, oral daily,
4→8 wk ([PMID 40178985](https://pubmed.ncbi.nlm.nih.gov/40178985/)): **femur +8.2%, tibia +6.4%, nasoanal
+7.3%** at 14 mg/kg, dose-dependent, **no body-weight difference.** Compare Haraguchi's *Hhip1* cKO: +4.5%
**at 53 weeks**. Systemic SAG did nothing in wild-type (F-R053/54); **systemic FGFR3 inhibition works.**
**Caveat enforced: no growth-plate histology was done in wild-type** — the length gain is measured, the
mechanism is inferred from gain-of-function models.

**SCFE explained.** Larger terminal cells, fewer of them, expanded HZ, suppressed terminal apoptosis, and
*Fgfr3*-null mice showing **increased femur length with decreased BMD**. **SCFE is the mechanical shadow of
exactly the effect we want** — it cannot be dosed away without giving up the benefit, which is what
abaloparatide is for, now for a stated reason. Also: **FGFR3 loss upregulates Hedgehog signalling**
([PMC4474636](https://pmc.ncbi.nlm.nih.gov/articles/PMC4474636/)), linking this arm to the `A`-lever.

**Open, all experiments or specific unavailable documents:** (1) **does FGFR3 inhibition raise terminal cell
volume in a *wild-type* plate** — one histology panel on animals already run, the highest-value missing
measurement in the branch; (2) **serum phosphate in AI-treated children** — predicted to fall; not reported
in the published paediatric AI literature, so **Hero 2005/2006/2009 supplementary chemistry tables would
answer it**; (3) does any FGFR3 inhibitor delay fusion in a **long bone** (verified for synchondroses,
inferred for physes); (4) erdafitinib + VEGFR2 blockade hit the same ERK/caspase-9 node — redundant,
synergistic, or additively unsafe mechanically; (5) what sets **bat manus 40,300 vs bat pes 1,300 µm³** in
one animal; (6) CYP19A1⁻/⁻ rabbit growth plates — now confirmed non-existent.

---

## The forty-fourth summary — F-R061: the counter-move is inside erdafitinib, at the dose we specified

**Correction, and it reverses F-R060 §4.** I predicted oestrogen ablation would *lower* serum phosphate and
create a rickets-like failure mode. **Backwards for humans.** **Uemura, *JCEM* 2000;85:1215** — HRT dropped
TmP/GFR in all 5 patients (**mean −14.5%**); **GnRH-a raised it in all 5 (mean +28.5%, up to +78.3%),
reversible**; TmP/GFR and serum Pi both correlate **negatively** with E2 (**r = −0.767 / −0.797**, P<0.01).
**Zhang, *AJKD* 2014;63:198, NHANES n=7,005** — postmenopausal women **on** oestrogen: phosphorus **3.83 vs
3.98 mg/dL, P<0.001** fully adjusted; phosphorus **rises** across ages 46–60, sex×age P<0.001. Rat mechanism:
oestrogen **downregulates NaPi-IIa** causing phosphate wasting, independent of PTH and apparently not via
ERα. **Ikedo is the outlier — adipose-local, lifelong, murine — and I'm not smoothing it over. There is no
rickets risk in the oestrogen arm.**

**Wickman 2003 (letrozole in 23 CDGP boys, 12 mo) settles three things.** **E2 fell to 8.1 ± 2.1 pM ≈ 2.2
pg/mL** — well under the Nilsson/Schrier **11 ± 2 pg/mL** threshold — while the control arm sat at **40.6 pM
≈ 11.1 pg/mL**, i.e. *normal male puberty runs right at the threshold*. **Testosterone shunted to 57.8 nM
(~3× control)** — F-R052's substrate counter-move, quantified. **No BMD/BMC/BMAD difference between groups**;
CTx, PICP, osteocalcin unchanged. **And E2 fully rebounds by 6 months after stopping.** Wickman does not
measure phosphate, and **no published paediatric AI study does** — stated as non-existence, not a request.

**The wild-type histology I asked for exists — in the FDA tox package, not the literature.** The full
TYRA-300 paper confirms its wild-type arm is **length and PK only** (no histology), and its ACH-model
endpoint is described as *"more similar to a wild-type growth plate"* — normalisation. **FDA NDA 214622
(infigratinib), GLP toxicology in normal animals:** *"sternal bone **minimal/mild growth plate thickening**
at **1 mg/kg/day and above**"* (13-wk rat); femur and sternum at ≥3 mg/kg; and in **6-month-old beagles**,
*"**increased growth plate thickness** and **fractures in the lumbar spine** associated with increased
physeal thickness… and/or **bone loss**"* at 3 mg/kg. **FGFR3 inhibition thickens the plate in normal
animals — not merely normalisation.**

**And the mechanical-envelope claim survives, sharpened.** TYRA-300 showed **BMD +21.4%, BV/TV +73.3%** in
the ACH model, which nearly made me withdraw F-R060 §5.1 — the dog data resolves it: **FGFR3 inhibition
normalises bad bone and degrades good bone.** The stack operates on good bone. Abaloparatide stays, now on a
wild-type fracture finding.

**The finding I did not expect.** F-R060 named the executioner: `phosphate → VEGFR2 → Raf/MEK/ERK1/2 →
caspase-9`. **FGFR inhibition raises serum phosphate as its defining on-target effect** — FGF23 resistance.
From the FDA review: **hyperphosphatemia in 89%** (82% by lab), **median onset 8 days**, **phosphate binders
in 83%**, **the commonest cause of dose reduction (78%)**, a **DLT**, positive exposure–response; rat
phosphorus **+30–38%** and dog **FGF23 +6.9-fold**, with **kidney mineralization**.

> **So erdafitinib hits ERK1/2 twice with opposite signs:** FGFR3 → ERK ↓ (suppresses terminal apoptosis —
> wanted) and phosphate ↑ → VEGFR2 → ERK ↑ → caspase-9 (promotes it — against us). **F-R052's "every node
> has a counter-move" appearing inside the stack's own first drug.**

**And the specified dose is on the wrong side of it.** **BALVERSA is titrated *upward on phosphate*: start
8 mg, go to 9 mg if phosphate is <5.5 mg/dL at day 14, target 5.5–7.0 mg/dL** — hyperphosphatemia is the
proof-of-target-engagement biomarker. **That is precisely the range that maximally drives the death signal.**

**The two effects separate by ~10×.** Plate thickening from **1 mg/kg** (rat) vs hyperphosphatemia only at
**10 mg/kg**; and in children, **0.25 mg/kg infigratinib → +3.38 cm/yr AHV with *zero* hyperphosphatemia
events**, with the programme stating *"hyperphosphatemia does not occur at the low doses of infigratinib
that show activity in vivo."* **This is why F-R046's "threshold, not gradient" plateau exists: past
threshold you stop buying plate and start buying phosphate.**

**Recommendation, and the honest gap.** Dose the FGFR3 arm to the lowest plate-thickening dose with **serum
phosphate held at low-normal — the inverse of the oncology paradigm**, binders to normal rather than to 7.0.
**But all the low-dose growth data is *infigratinib* and the stack specifies *erdafitinib 8 mg*, which has
no growth-plate dose–response and a deliberate phosphate target. No published mapping between them exists
and I will not guess one.** Either dose low with phosphate control, or substitute infigratinib at the
PROPEL 2 dose — the only agent with an actual paediatric growth-plate dose–response. That is your call.

**Open:** (1) **serum phosphate on FGFR3 inhibition *plus* oestrogen ablation** — both raise it by
independent mechanisms, never combined, now the most important unknown in the stack; (2) erdafitinib
growth-plate dose–response (does not exist); (3) does phosphate binding preserve the FGFR3 plate effect
(directly testable, never tested); (4) **the Dunkel CDGP bone-health paper (NCT01797718, letrozole vs
testosterone, n=35, 2013–2018)** — if it reports serum phosphate or TmP/GFR it answers the oestrogen half of
(1), and I could not reach that publication; (5) bat manus 40,300 vs pes 1,300 µm³; (6) CYP19A1⁻/⁻ rabbit
growth plates, confirmed non-existent.

---

## The forty-fifth summary — F-R062: the stack, and the one requirement it does not meet

**The Dunkel CDGP bone paper: retrieved as far as it legitimately goes.** It is **Varimo T, Miettinen PJ,
Huopio H, Rikkonen T, Voutilainen R, Tenhola S, Raivio T, Hero M. *Eur J Endocrinol* 2025;193(2):289–296**
(doi 10.1093/ejendo/lvaf160). Full abstract obtained via NCBI E-utilities; **OpenAlex confirms
`oa_status: closed`, `any_repository_has_fulltext: False`** — no preprint, no accepted manuscript, no
repository copy anywhere, and the Finnish portals sit behind anti-bot layers. **I did not route around the
paywall.** Two useful conclusions anyway: the paper reports **pQCT and turnover markers, not phosphate**, so
the full text would not have answered the phosphate question; and its result is real — **27 boys, letrozole
2.5 mg/day (n=15) vs testosterone 1 mg/kg q4wk (n=12), 6 months: distal tibia BMC 0–6 mo −1.8 mg/mm on Lz vs
+18.1 on T (P = .043)**, P1NP and BAP rising more on T, **no cortical or endosteal differences**, and the
authors' own limit: *"do not allow conclusions regarding skeletal safety of longer Lz use."*

**The stack is specified in F-R062, and it meets two of the three requirements.**

| requirement | status |
|---|---|
| **fast** | **solved** — identity verified to 0.1%; both factors have agents with wild-type effect sizes |
| **never-closing** | **substantially solved, one gap** — executioner identified and blockable at three points, one human-validated with growth preserved |
| **infinite** | **NOT solved** — nothing expands or renews `n₀`, and `L∞ ∝ n₀` |

**Arms:** (1) **erdafitinib 8 mg** — the load-bearing agent, the only one moving flux **+** `v(c)` **+** the
ERK closure node, and the only growth-plate agent in the branch with a wild-type effect size (TYRA-300
**femur +8.2%** in 4 wk; FDA tox: plate thickening in **normal** rats from **1 mg/kg**). (2) **Phosphate
control — mandatory, not optional**, and inverted from oncology practice: **hold serum phosphate at
low-normal, never the label's 5.5–7.0 target**, because erdafitinib hits ERK1/2 twice with opposite signs
and **Arm 5 raises phosphate too, by an independent renal route.** (3) **GH 2 IU** — AKT rescue for Arm 1
(FGFR blockade alone is apoptotic), on the *augmenting* side of the stem-pool sign flip, plus a speculative
`v(c)` role via Nkcc1. (4) **Abaloparatide 80 µg** — the envelope failure is **intrinsic**: normal dogs
fracture at the plate-thickening dose; FGFR3 inhibition **normalises bad bone and degrades good bone**.
(5) **Letrozole 2.5 mg/day** (Varimo's dose) → **E2 ≈ 2.2 pg/mL**, below the 11 pg/mL threshold, with
**testosterone shunting ~3× to 57.8 nM** — protective, and an argument against suppressing androgens
anywhere in this stack.

**The five issues, stated after assembly:** (1) **two of five arms push phosphate the wrong way by
independent mechanisms and that combination has never been measured in any organism**; (2) 8 mg violates
Rule 1 — the plate effect is available ~10× lower, and the excess is bought from `n₀`, the already-unsolved
term; (3) the mechanical envelope is a **ceiling on achievable effect**, not a safety footnote, and
abaloparatide's role there is inference; (4) **every closure term is a delay, not a prevention** — VEGFR2
blockade reverses *"rapidly"*, letrozole's E2 **fully rebounds in 6 months**, dexamethasone returns; (5) the
honest magnitudes are **+8.2% femur (wild-type mouse, 4 wk)**, **+4.5% (Hhip1 cKO, 53 wk)**, **+3.38 cm/yr
(children)** — the **6.8× `v(d)` headroom is measured biology, not a demonstrated drug effect.**

**What is genuinely still open, and none of it is a dose.** (1) **A pool-renewal agent** — FoxA2⁺ proves
`a > b` is achievable through three serial transplants; **nothing reproduces it pharmacologically**, and
`L∞ ∝ n₀`. (2) **Link 11** — ovariectomy does not prevent fusion in the rabbit (Weise; Karimian **16/17
distal tibiae fused by 4 weeks**), and only the CYP19A1⁻/⁻ rabbit skeleton separates the two readings; that
animal exists and the data does not. (3) **Whether terminal chondrocyte volume can be pushed *above* normal
in a healthy plate** — three lines converge on the lever (FGFR3→`v(c)`, GH→Nkcc1, IGF-1→Phase 3) and **every
one is measured only as normalisation of a deficit**, while the bat proves 31× is biologically available.

**Bottom line: this is a fast, long-duration growth stack with an unusually well-characterised closure-delay
arm. It is not an infinite-growth stack, and no arrangement of currently existing molecules is — the missing
piece is stem-pool renewal, and that molecule has not been made.**

---

## The forty-sixth summary — F-R076: DLK1 is a timing gene, and the clock question splits

**F-R065 called DLK1 "the most tractable entry point" into Lui's imprinted senescence network. It is
tractable and it is the wrong kind of lever, and finding that out was worth more than the lever.**

**DLK1 loss is a human disease, and it comes in two sizes.** Paternal deletion of *DLK1* alone gives
**central precocious puberty and essentially nothing else** — *"did not demonstrate additional features of
the imprinted disorder Temple syndrome except for increased fat mass."* Paternal loss of the whole 14q32.2
domain gives **Temple syndrome**: IUGR, hypotonia, precocious puberty, short stature.

**Across 17 reported DLK1-defect individuals, untreated adult heights run 137.8–160.5 cm.** And then the
sentence that decides it: *"Female patients... who received **regular GnRHa treatment all had reached
normal-range adult heights**."*

> **A human born with no functional DLK1 at all reaches normal adult height provided the plate is given
> time.** DLK1's entire effect on height runs through **pubertal timing**, and delaying puberty recovers
> **all** of it. **As a capacity lever it is withdrawn.**

**But that is the branch's cleanest human demonstration of its own central claim.** Capacity and duration
are separable; **duration is what costs the height.** Delete one of the eleven network genes outright and
the plate is still fine — it just runs out of time. The Temple cohort says the same thing louder: adults at
**−3.67 / −3.41 / −2.73 SDS**, yet the treated children go **7.13 → 11.81 cm/year** on 0.042 mg/kg/day GH.
**A plate missing DLK1 *and* GTL2/MEG3 is not rate-limited.**

**On the pacing law, two more human datasets, and they do not agree.** **EPOCH (n=135)** independently
reproduces the split F-R075 argued for — **peak height velocity associated (β 0.018, p=0.0008), age at peak
height velocity null** — but only on the **cell-composition-sensitive** extrinsic clock; the intrinsic
Horvath measure was null (p=0.22). **And the only interventional dataset in existence (n=10, GH-deficient
children) splits inside itself:** height velocity doubled, **raw epigenetic age acceleration fell**
(non-significant, p=0.179) — against pacing — while **IGF-1, the mediator of the growth, was positively
associated with acceleration (β 0.011, p=0.026)** — for it.

**Ledger: four for, two against. The observational associations replicate; the one experiment that actually
manipulated growth did not reproduce them.** Supported, unproven, and now unproven in a sharper way.

**One consequence the branch had not confronted.** IGF-1 was the accelerating term, and the GH arm raises
IGF-1 roughly three-fold at **half** the stack's dose. **If IGF-1 paces the clock, "blast" is the
accelerant, not a free choice.** That does not overturn the blast argument — F-R065 settled that the closure
deadline it was racing is removable in humans — **but it prices it, and nobody has run the measurement that
would settle the price.**

---

## The forty-seventh summary — F-R077: I ran the clock myself, and in blood it is chronologically paced

**Tate supplied Dauber 2017 and Gomes 2019 as asked. He also supplied two papers I did not know to ask for,
and one of them names a public dataset that answers the question the branch has been circling since F-R066.**

Palumbo 2024's data-availability line reads: *"Raw methylation data and the normalized beta-values are
available on ArrayExpress (E-MTAB-13950)."* **It is public. EPIC arrays. 45 samples. And the design is
better than anything I had asked for:**

| group | n | chronological age | Tanner | bone age |
|---|---|---|---|---|
| pre-pubertal controls | 14 | **7.83** | 1 | — |
| **central precocious puberty** | **19** | **7.83** | **2 (2–3)** | **+1.69 ± 1.00 y advanced** |
| pubertal controls | 12 | 14.55 | 3 (2–4) | — |

**Same chronological age, 1.69 years of extra skeletal maturation.** I streamed the 625 MB beta matrix and
computed the Horvath 2013 pan-tissue clock (326/353 probes) and the Horvath skin-&-blood clock (381/391)
directly from the published coefficients.

**The pipeline works:** pre-pubertal controls came out at DNAmAge **7.70** against a chronological 7.83;
pubertal controls at **13.54** against 14.55. Positive control p ≈ 7×10⁻⁵.

**The result:**

| clock | CPP − age-matched controls | 95% CI | p |
|---|---|---|---|
| Horvath 2013 | +0.417 y | −0.915 to +1.750 | 0.528 |
| **skin & blood** | **−0.016 y** | **−0.649 to +0.616** | **0.959** |

**And it is not a power failure** — pooled SD 0.870 y gives 80% power to detect 1.69 y at n=5 per group.
Correcting for the clock's compression, a true 1.69-year advance should read +0.84 y. **The confidence
interval tops out at +0.62. It is excluded, not merely unfound.**

**The reciprocal:** matched on *Tanner stage* instead, CPP and pubertal controls differ by **−3.353 years,
p = 7×10⁻⁵**. Match the chronological age and the clocks agree; match the developmental stage and they are
3.4 years apart. **In blood, the clock tracks time, not development.**

**Two clock-free confirmations from the same data.** A puberty axis built on controls alone puts the CPP
girls **one fifth** of the way along the normal transition (p = 0.36). And Lui's imprinted network — 1,299
EPIC probes across 24 genes — moves with normal puberty (**CDKN1C, MEIS1, PEG10, SGCE** at q<0.05) and
**not at all** in CPP versus age-matched controls.

**It also settles a contradiction and explains a split.** Bessa 2018 and Palumbo 2024 disagree flatly on the
direction of the pubertal methylation shift; on Palumbo's own probe-level data, **91% of the moving probes
lose methylation at puberty** — Palumbo is right. And EPOCH's only positive was on **extrinsic** (blood-cell-
composition-sensitive) age acceleration, with intrinsic null. **My two intrinsic-type clocks are null too.
The "epigenetic age accelerates with puberty" signal is most likely leukocyte composition.**

**What I had to retract is the part that matters.** F-R074 §2 called a blood array on an ESR1-null man *"the
cheapest decisive experiment the programme has."* It is not decisive — it is not even sensitive. And the
letter I drafted last round asking Fukami and Matsubara for the hypogonadotropic-hypogonadism IDATs is now
marked **do not send**: it would be asking two researchers for their time to reproduce a negative at lower
power. **Lui's tryptophan result is untouched — that was rat growth plate, measured by expression. The
pacing law survives; every cheap blood proxy for it is dead, and the measurement has to be made in physeal
tissue.**

**On DLK1, the primaries corrected me twice.** GnRHa-treated girls reached normal-*range* height but not
their own targets (shortfalls −9.5, +1.2, +0.8, −6.0 cm), and Gomes explicitly argues a puberty-independent
growth effect that F-R076 denied. **But the deletion-size series is better than what I claimed:** DLK1-exon-1
alone gives precocious puberty with near-normal height; a 411-kb deletion gives **−4.4 SD and normal
menarche**. Stature scales with how much of the domain is lost; puberty tracks DLK1. **So the height gene at
14q32.2 is not DLK1 — it is GTL2/MEG3 or RTL1, and MEG3 is the other Lui-network gene at that locus.**

---

## The forty-eighth summary — F-R078: the locus closes, the plate has its own clock, and I had CCN2 backwards

**Kagami 2008 is the primary I asked for last round, and it corrects F-R077's own §7c.**

The four deletions come with parental origin, and that is what makes the series work: **the identical
108,768-bp deletion gives Kagami-Ogata when maternal and Temple syndrome when paternal.** This is an
imprinting-control system, not gene dosage, and my gene-count reading was the wrong frame.

**MEG3 is refuted twice over.** It is maternally expressed, so a *paternal* deletion removes an already
silent allele — and *"Gtl2^lacZ mice… have a **normal phenotype** with at least 60–80% reduction of all the
MEGs."* DIO3 too. **RTL1 is the second height gene, and the authors say so:** *"growth is more severely
compromised in case 11, with additional loss of active RTL1."* In mouse: Dlk1 KO **~80%** of normal size,
Rtl1 deletion **~80%**, both **~60%**.

**And F-R076 §1 is now fully retracted rather than softened** — *"the paternally derived Dlk1 mutation…
result[s] in pre- and postnatal growth deficiency."* DLK1 is a timing gene **and** a growth gene.

> **But the useful conclusion is that the locus closes as a lever.** DLK1 at 2× overgrows and at 3× is
> lethal; RTL1 in excess gives a bell-shaped thorax and coat-hanger ribs. **Every gene there with a height
> effect has an optimum, and both directions away from it are shorter.** Four rounds on this locus,
> excluded on primary data.

**Nilsson I under-weighted, and re-reading it partially rescues the pacing law from my own null.** I
dismissed it in F-R072 as a bulk assay. The assay is bulk; the **pattern** is the finding. In the same
rabbits at the same ages: growth-plate resting zone **down** (P=0.004), all three ulnar zones **down**
(P<0.001), **no difference between zones within an age**, **liver up** (P<0.001), cultured chondrocytes
**up**. **The plate and the liver move in opposite directions in the same animal, and it is not the
transit-amplifying divisions doing it.** F-R077 showed the blood clock is chronological; this shows the
plate is not doing what the rest of the body does — **which is exactly why a systemic readout cannot see
it, and it is the positive evidence that there is something in the plate worth measuring.**

**Then I audited the ledger's own open terms, and the biggest one had a gene.** STACK_STATE §3.1 said of
matrix volume per cell — **32–49% of daily elongation** — that *"this branch has never once addressed it."*
The human loss-of-function is **ACAN**: heterozygous aggrecan variants give short stature with advanced bone
age and premature fusion, *"decreased extracellular matrix volume."* **Halve the matrix, get a short child
whose plate closes early.**

**And the GH trial in those patients answers a worry I raised two rounds ago.** F-R076 §5 asked whether
IGF-1 is the accelerant that makes the blast strategy costly. Ten ACAN-deficient children, three years of
rhGH, IGF-1 SDS held at **+2.3**: height SDS **+1.21**, predicted adult height **+6.8 cm**, and **bone
age/chronological age ratio change −0.10, not significant.** In a population already prone to premature
fusion. **The blast argument survives a real test.**

**The thing I most want on record is a sign error of my own.** The branch reached CCN2 twice and both times
asked about *blocking* it — R341 killed pamrevlumab because Ctgf-null gives an expanded hypertrophic zone,
i.e. discharge failure. **Nobody asked what raising it does, even though that reasoning implies the
answer.** Cartilage-specific CCN2 over-expression: **tibia +5.6% at P1 (P<0.0001), dose-dependent across two
independent founder lines**, enhanced proteoglycan density (**that is `v(m)`**), proliferation up in the
proliferative **and resting** zones, IGF-I/II up with enhanced IGF-1R autophosphorylation — **and femoral
mineral content, trabecular mineral and cortical thickness all up.**

> **That last row matters more than the length.** §3.6 states the mechanical ceiling as a hard physical
> limit — everything that widens the plate weakens it — and says abaloparatide is *"an inference, not a
> measurement."* **CCN2 is the measurement: longer and stronger in the same animal. The only agent in the
> programme that does both.**

**What it does not show, stated because I nearly carried it forward wrongly:** the only length measurement
is a **P1 tibia at n=3**; *"12% larger at 8 weeks"* is **body mass, not bone length**; **adult bone length
was never measured**; and the hypertrophic zone was **shorter** — a `v(c)` cost. **Which is exactly why it
pairs with erdafitinib**, which raises `v(c)` (HZ +45% vs PZ +25%). Opposite halves of `v(d)`; each one's
cost is the other's mechanism. First genuinely complementary pairing in the stack.

**And the compartment problem has a solution the branch already built.** CCN2 is height-positive inside
cartilage and height-negative outside it, which is why R341's systemic kill was right. The published
transgenic is **promoter-restricted**. **Col2a1-promoter AAV-CCN2 by the intra-epiphyseal route of F-R074 —
both halves exist and nobody has combined them.**

**One conflict I am flagging rather than resolving:** CCN2's classical inducer is TGF-β, while F-R034 has
the resting-zone niche as *"low in WNT and TGF-β"* and F-R073's cocktail contains Repsox, a TGF-β inhibitor.
**A CCN2 arm and a Repsox arm pull against each other.**

**And one contradiction inside the ledger, now fixed.** §3.8 still argued that 0.35 mg/kg/wk GH *"lands in
the depleting range"* while §1 carries 0.49 mg/kg/wk and calls the low-dose rationale withdrawn. The
depleting claim came from a mouse stem-cell paper; the ACAN trial ran **exactly 0.35 mg/kg/wk in children
for three years** with sustained gain and no maturation cost. **§3.8 corrected to agree with §1.**

---

## The forty-ninth summary — F-R079: the growth-plate methylome exists, and it reverses one of my own retractions

**The gap I have named in four consecutive rounds is closed, and closing it cost me a retraction I made in
F-R072.**

**GSE270641 is site-resolution DNA methylation in growth-plate chondrocytes with a bone-length phenotype.**
Yanagihara et al., *Nat Commun* 2025: `Dnmt1^ΔPrx1` mice have **significantly shortened long bones** from
*"decreased chondrocyte proliferation and accelerated differentiation."* Dnmt1 and Uhrf1 sit in the
**proliferative zone**. At one week the proliferative area is smaller, BrdU⁺ lower, and the **hypertrophic
and mineralised areas wider**; by six weeks there is **loss of growth plates** and delayed secondary
ossification.

**The mechanism is the branch's whole thesis in one sentence:** *"DNA methylation **maintenance in
proliferating chondrocytes** and **demethylation of DNA in hypertrophic chondrocytes** is essential for bone
elongation."* **Demethylation is the differentiation signal.** And there is a human anchor — *"In the
Musculoskeletal Knowledge Portal, Dnmt1 is significantly associated with Height."*

**This is Nilsson 2005's hypothesis with a knockout behind it, twenty years later.**

> **And it forces a retraction.** F-R072 §1 was headed *"the OSK direction problem dissolves — the assay had
> no site resolution."* **That dissolution is withdrawn.** F-R069 records OSK's cartilage mechanism as
> **"DNMTs down, TET2 pivotal"** — which is now the measured height-negative direction.

**I analysed the deposit myself.** 95.9% of Dnmt1-dependent methylation lies **outside** promoters and CpG
islands — promoters show **no enrichment at all** (2.7% observed vs 2.5% shuffled, 1.07×), gene bodies
53.8%, intergenic 45.8%. **So the marks are in a different compartment from OSK's CpG-island/bivalent target
class. But the enzyme is shared** — if OSK lowers DNMT1 protein, compartment separation does not save you.

> **Named hazard: AAV-OSK in a growing animal may phenocopy `Dnmt1^ΔPrx1`.** The published OSK cartilage
> work was adult articular cartilage for osteoarthritis — **no growth plate**. Nobody has run it with open
> physes. The reprogramming arm has carried this assumption since F-R069 and I did not see it until the
> knockout existed. **Discriminator: DNMT1 protein in proliferative-zone chondrocytes after OSK, with bone
> length.**

**And the untested direction is the interesting one.** The paper never tests Dnmt1 over-expression. **Raising
maintenance methylation should hold cells proliferative for longer** — the same shape as the dexamethasone
banking result in F-R072, and the same cost.

**I also found a defect in the deposit and an error of my own.** The file is **missing chr7, chr8, chr9 and
chrX entirely** — 76% genome coverage — so my first-pass "zero regions" at *Acan*, *Igf2*, *H19*, *Cdkn1c*,
*Cyp19a1* and *Dnmt1* were artefacts of which chromosomes were uploaded. And my first-pass Dlk1–Dio3
enrichment of *"3.2×, p = 3.6 × 10⁻¹⁹"* used a Poisson null against a uniform rate, which is wrong because
methylation regions cluster. **Permutation against 20,000 random same-size windows gives 2.38×, p = 0.059 —
not significant.** Both are recorded in the round rather than quietly fixed.

**Kagami's supplement confirmed the height figures exactly** — −2.2, −2.9 and −4.4 SD — and added that case
11 was already **−2.4 SD at birth**, so about half the RTL1 effect is prenatal. It also showed her menarche
was **normal** while the DLK1-only case was **early**: height and pubertal timing move separately at that
locus, which is F-R078's conclusion seen a third time.

**On CCN2, half the ask is answered and the other half is now very sharp.** The same Col2a1-CCN2 line was
followed to **24 months**: healthy, CCN2 still accumulated in growth-plate cartilage at 21 months, and
**radiographic osteoarthritis in 50% of wild-type knees and none of the transgenics**. But **two papers, one
line, 24 months of follow-up, micro-CT and serial radiography of four joints — and neither ever measured
adult bone length.** The only length figure in the whole line is a **P1 tibia at n = 3**. Those radiographs
may already contain the number.

---

## The fiftieth summary — F-R080: DNMT3A is a human height gene, and loss is the tall direction

**The supplied paper was the OSK study itself — F-R079's ask #3, which I called the single highest-value
unknown in the stack. Reading it downgraded the hazard I raised last round and opened the strongest lead the
programme has found.**

**First, the correction.** F-R079 warned that OSK lowers DNMTs and `Dnmt1^ΔPrx1` shortens bone, so AAV-OSK in
a growing animal might phenocopy the knockout. **The primary shows that rested on an imprecision in my own
F-R069 record.** The only methyltransferase antibody in the entire paper is **DNMT3a (ab188470)** —
*"post-OSK treatment, DNMT3a levels were noticeably declined."* **The string "DNMT1" appears exactly twice in
the whole paper, both citing the OA disease state. It was never measured after OSK.** DNMT3A is a **de novo**
methyltransferase; DNMT1 is the **maintenance** enzyme. **F-R069's "DNMTs down" should have read "DNMT3a
down," and that turns out to matter enormously.** *(Also corrected: the authors say their methylation-age
result is underpowered — "the limited sample size in our study precludes the attainment of statistical
significance." F-R069 reported it as a measurement.)*

**Because DNMT3A is a human height gene, and loss is the tall direction.**

| direction | phenotype |
|---|---|
| **loss of function** — Tatton-Brown-Rahman syndrome | **tall stature, mean +3.0 SD**; height ≥+2 SD in **83% (44/53)**; one girl needed **bilateral epiphysiodesis to stop growing** |
| **PWWP gain of function** (Heyn, *Nat Genet* 2019) | **microcephalic dwarfism**, by **hypermethylation of Polycomb DNA-methylation valleys with depletion of H3K27me3 and H3K4me3** |

**One gene, both directions, in humans.** And the compartment is the one F-R070 already identified —
Polycomb/bivalent, the class Lui measured H3K4me3 falling at.

**This resolves the F-R079 conflict completely.** F-R079 measured that **95.9% of Dnmt1-dependent methylation
is outside promoters and CpG islands** — gene bodies and intergenic. Heyn's dwarfism mechanism is
hypermethylation of Polycomb valleys. **Two enzymes, two compartments, opposite height signs: DNMT1 loss →
short; DNMT3A loss → tall.** So the target is precise: **lower DNMT3A, preserve DNMT1** — which makes
azacitidine and decitabine exactly the wrong tools, since nucleoside analogues trap all DNMTs including the
one that must be kept. **Selective non-nucleoside DNMT3A inhibitors exist**, with the selectivity determinant
named (Asn1192 in DNMT1 abolishes affinity).

**And then the contrast that is the whole programme.** Sotos syndrome (NSD1) is also an overgrowth syndrome
from loss of an epigenetic writer — but Sotos has **advanced bone age**, early puberty, and an adult height
only at the *"upper limit of normal"* (men 184.3 cm, women 172.9). *"Advanced bone age… accelerates skeletal
maturation and closure of growth plates, ultimately limiting the period of growth despite early childhood
overgrowth."* **That is the failure mode this branch has described since F-R024.** The TBRS girl, by
contrast, had **bone age 12 years at chronological 12 years**, grew until **19 years 6 months**, and kept
**+3.2 SDS**.

> **DNMT3A loss appears to decouple growth rate from skeletal maturation. NSD1 loss does not.** That is
> exactly the property "fast without paying in duration" requires. **And the crucial cell rests on one
> patient — the 55-patient cohort contains no bone-age data at all.**

**Finally, the pacing law is confirmed in humans and it rescues my own F-R077 null.** Jeffries et al. ran the
Horvath clock across three syndromes: **TBRS +40% (P=0.004), Sotos +40% (P=6.4×10⁻⁹), Kabuki −40%
(P=0.023).** Overgrowth accelerates the clock; growth deficiency decelerates it. **F-R077 found no
acceleration in girls with precocious puberty and bone age +1.69 y, and I concluded the clock was
"chronologically paced." That needs refining: CPP children are early, not overgrown.** The clock tracks
**growth accomplished**, not pubertal stage or skeletal maturation — so F-R077's null is precisely what the
law predicts, and it is a cleaner control than I realised.

**The SRA pull finished.** No sra-toolkit, aligner or samtools in this environment and 55 GB of FASTQ against
27 GB of disk, so I built a repeat-masked 32-mer index of the target loci and streamed the reads straight
from ENA without writing them to disk.

**It validated itself on the engineered lesion:** the `Dnmt1` locus is the *only* one that falls in raw
counts (0.58×) while every other locus rises — that is the floxed-exon deletion, detected in the correct
three samples. And the negative control earned its place: **the gene desert rises 4.6× in the knockouts**,
because MBD2 pulldown specificity collapses as methylation is lost and the library drifts toward input.
**Raw counts alone are uninterpretable.**

Read against that background, **the genes the deposit omitted are Dnmt1-dependent after all** — **`Acan`
(0.43×, p=0.015)** and **`Cyp19a1` (0.53×, p=0.012)**, plus `Igf2/H19`, `Cdkn1c`, `Mkrn3`, `Peg3` and
`Gpc3`. The known positives from the deposit rank immediately below the deletion (`Dlk1` 0.24×, `Meg3`
0.26×), and **`Hhip` returns a clean null (4.31× against a 4.61× background), which is what makes the
positives mean anything.**

**The matrix gene of F-R078 and the aromatase gene of the closure arm both carry Dnmt1-dependent methylation
in chondrocytes.** That is not evidence that methylation controls their expression — it is evidence that the
methylation layer sits *upstream of* both the matrix term and the closure term rather than beside them.
**One positive control failed to replicate** (`Nnat`, the densest locus in the deposit, 0.73×, p=0.22), and
I am recording that rather than dropping it.

---

## The fifty-first summary — F-R081: the OSK hazard is refuted, and the DNMT3A decoupling now rests on three patients

**All four of F-R080's asks were answered by the supplied documents. The most important one refutes a hazard
I raised two rounds ago.**

**Partial reprogramming RAISES DNMT1.** Su et al. sorted senescent epidermal stem cells with low self-renewal
and applied transient OSKM: *"partial reprogramming **increased DNMT1 mRNA expression**… but had **no effect
on TET1, TET2, and TET3**… partial reprogramming **significantly increased the DNMT1 protein expression**."*
And *"young ESCs also had a **higher** expression of DNMT1 compared to senescent ESCs"* — DNMT1 falls with
senescence and reprogramming restores it. Their mechanism sentence is `Dnmt1^ΔPrx1` in another tissue:
*"DNMT1 is essential for the preservation of the progenitor state… lack of DNMT1 would result in severe
defects in proliferation and self-renewal capacity."*

> **F-R079 predicted OSK would lower maintenance methylation and shorten bone. The measurement says the
> opposite. The hazard is refuted, not downgraded.**

**And the structural correction matters more than the hazard.** Methylation age fell **while DNMT1 rose, in
the same cells, in the same experiment.** **Rejuvenation is not global demethylation** — and F-R069, F-R072
and F-R079 all quietly assumed it was. Partial reprogramming **raises the maintenance writer and lowers the
de novo writer at Polycomb targets**, and both of those are height-positive. The contradiction that ran
through four rounds was an artefact of treating "DNMT" as one thing.

*(Limits: epidermal stem cells not chondrocytes, OSKM with c-Myc rather than the cartilage study's OSK
without it, n=3, low-tier journal. The direction is clear; the weight behind it is one experiment.)*

**On bone age — my #1 ask — the decoupling survives and is now much stronger.** The Japanese 17-year case is
the single best observation in this branch: **+3.77 SD tall and breast Tanner 4 at ten years seven months,
with a bone age of 11.1 years.** In an ordinary child that stature and pubertal stage come with a markedly
advanced skeleton; here it is half a year ahead. The Swedish girl was **bone age 12.0 at 12 years 2 months**.
The Chilean boy *does* have a bone age 4.2 years advanced — **but his non-carrier sister has advanced bone
age too**, and his authors write that this *"raises the possibility that there are other familial factors,"*
adding that advanced bone age *"has not been reported frequently in TBRS."* **It segregates independently of
DNMT3A.** And Lennartsson's surgeons found Greulich-Pyle *"underestimated the amount of remaining growth"* —
the decoupling seen from the other side.

**The overgrowth is not endocrine.** At +3.77 SD the Japanese patient had **IGF-1 of +0.22 SD** and *"serum
GH and IGF-1 levels were not elevated."* **DNMT3A runs at +3 SD on a completely normal somatotropic axis** —
which makes it genuinely orthogonal to the stack's GH arm rather than redundant with it.

**Heyn 2019, read in full, lands on the branch's own pool axis.** `Dnmt3a^W326R/+` mice are *"viable,
healthy… proportionately small with significantly reduced body and brain weight."* And the sentence:
*"hypermethylation of DMV/DMRs could lead to a **skewing of stem/progenitor cells towards differentiation
away from self-renewal**."* **That is `a > b` — the lever this branch has hunted since F-R022 — reached
independently from the other end of the literature.** Also worth recording: *"NSD1, DNMT3A and EZH2 are both
height QTLs,"* so all three overgrowth genes are common-variant height loci, and their conclusion is the
branch's thesis verbatim — *"the interplay between DNA methylation and polycomb at key developmental
regulators as a determinant of organism size in mammals."*

**Tatton-Brown 2014 verified at the primary:** *"Height was increased in **all** individuals ranging from
1.8 to 4.2 (mean 3.0) standard deviations."* All thirteen.

**And the detail that says what we are actually chasing:** the Japanese girl was given **oral oestrogen from
10.8 to 13.6 years specifically to force her growth plates shut**, and the Swedish girl had **bilateral
epiphysiodesis**. **Two countries, two deliberate interventions to stop growth — and both still finished
above +3 SD.** The programme's entire difficulty is manufacturing what these children had to be treated to
prevent.

---

## The fifty-second summary — F-R082: the clock and the height lever are the same molecule

**Both F-R081 asks answered, and the answer collapses two of the branch's problems into one.**

**The mouse question is settled in both directions.** `Dnmt3a^R878H/+` mice have **significantly longer
femurs** at 210 days (Smith, *Nat Commun* 2021, n=4 pairs) — normal at birth, diverging only after 100 days.
Bell-Hensley (*Bone* 2024) adds tibial overgrowth in both TBRS models and, crucially, the mechanism:
**the proximal tibial growth plate is significantly thicker in juvenile mutants, the thickening is not
zone-specific, and PCNA⁺ cell density and size are unchanged.** **A thicker plate with unchanged
proliferation puts the gain in `v(d)` or duration, not flux** — the same compartment F-R058's identity
says holds the largest untapped headroom.

**And the gain-of-function mouse is the mirror.** `Dnmt3a^W326R/+` (Jackson lab, *Nat Genet* 2026):
**median lifespan 12.8 months against an expected 26–29 — halved**; postnatal growth failure; osteoporosis
at 6 months; and **growth plate thickness reduced at 10–12 months.** **The growth plate reads this axis in
both directions, in mice, measured. F-R079 said that had never been done; it has now been done twice from
opposite ends.**

**Then the finding that unifies the programme.** That 2026 paper built a clock from the **2,646 CpGs that
DNMT3A gain-of-function hypermethylates** and tested it against the **332 Horvath clock CpGs** in **5,085
people from Generation Scotland**. The HESJAS sites track chronological age *"performing just as well as the
CpGs used to derive Horvath's."*

> **The sites DNMT3A hypermethylates are the sites the epigenetic clock reads.** The clock is not a passive
> correlate of time — it is substantially **a record of DNMT3A activity at Polycomb domains**, and that
> activity **causally reduces stem-cell output.** The senescence clock, the pool term, the imprinted network,
> Lui's H3K4me3 loss at bivalent promoters, and the height lever are one axis.

**The human mirror is complete at the methylation level too.** Smith's WGBS on 11 DOS patients found **focal
hypomethylation — 2,209 DMRs, all hypomethylated**, with the **HOXB cluster** as the worked example. Heyn
found **Hoxc13 hypermethylated** in the gain-of-function mice. Same Polycomb domain class, opposite
directions, opposite growth phenotypes.

**But the round also found the largest liability in the arm.** The `Dnmt3a` mutant mice have **thinner
cortical bone and significantly lower stiffness, yield load and maximum load** — and **normalising for
cross-sectional area does not remove it**, so it is a material deficit, not a thinner tube. Tissue mineral
density, osteoblast activity and osteoclast number are all unchanged; the mechanism is unresolved, and the
authors recommend adding bone density and quality testing to clinical assessment of TBRS patients.

> **That is §3.6's mechanical ceiling appearing inside the DNMT3A lever — and it makes F-R078's CCN2 result
> load-bearing rather than incidental.** CCN2 over-expression raised **cortical thickness (0.060 vs 0.049 mm)
> and total mineral content (1.36 vs 1.10 mg/mm)** while lengthening bone. **The same variables, opposite
> signs. CCN2 is the measured counter to the measured liability.**

*(A caveat that may dissolve the liability entirely: these are missense alleles and R878H is a dominant
negative. The authors note prior work in which "partial loss of Dnmt3a may increase cortical thickness."
Nobody has compared nonsense with missense skeletons, and human TBRS has both.)*

**And the two enzymes are not symmetric.** From the full Dnmt1 PDF: at 16 weeks `Dnmt1^ΔPrx1` bone length is
**less than half** of control. `Dnmt3a` heterozygotes get *"a small significant increase."* **"Preserve
DNMT1" is a hard constraint; "lower DNMT3A" is a titratable gain** — which is why any global hypomethylating
agent trades a catastrophic loss for a modest one.

**What this does not deliver, stated plainly.** TBRS patients reach **+3.0 SD and then stop.** DNMT3A loss
**raises the setpoint and the rate; it does not remove the endpoint.** The endpoint is a separate arm and the
branch already has it — F-R065's finding that oestrogen ablation prevents fusion in humans outright.
**DNMT3A inhibition raises the ceiling; oestrogen ablation removes the deadline. Neither alone is unbounded;
together they are the closest this programme has come to the three-term goal.**

**One tension I am not smoothing over.** Heyn 2019 said hypermethylation skews progenitors *"towards
differentiation away from self-renewal"* — pool depletion, the branch's `a > b`. The 2026 paper from the
same laboratory says **"HSC and early progenitor numbers remain constant"** with output reduced and Polycomb
targets not de-repressed, proposing instead that methylation **"impairs transcriptional activation dynamics
during differentiation."** Number preserved, output reduced — that is flux, not `n₀`. The two papers
disagree, and the later, better-powered one says output.

---

## The fifty-third summary — F-R083: the three missing experiments, answered without running them

**Tate is right that F-R082's asks are experiments, not papers, and that they do not exist. So I computed
substitutes for all three — from the repository's own growth-plate atlas, from the chondrocyte methylome I
already pulled, and from open human population genetics. All three are answered. One answer contradicts a
claim I have been making for three rounds, and one reproduces the mouse liability in humans at p = 3×10⁻²⁴.**

**Ask #1 — is the effect cell-autonomous to the plate?** The branch already held a zone-resolved human
growth-plate expression table (Chu 2026, 22,971 genes, 10 donors aged 11–14). Tested paired within donor:
**DNMT1 rises from stem to proliferative zone (+16.5, p = 0.047) and UHRF1, its obligate partner, does the
same (+11.0, p = 0.051) and then collapses to 4.5 and 3.4 in the prehypertrophic and hypertrophic zones.**
That is **Yanagihara's mouse immunohistochemistry replicating in human tissue** — maintenance machinery
switched on in the proliferative compartment and off as cells leave it. And **DNMT3A sits at the 84th
percentile of all genes, evenly across every zone including the stem zone, while DNMT3B is at the 35th and
effectively absent — so DNMT3A has no redundant partner in this tissue.** With TBRS's normal IGF-1 and GH,
cell autonomy is now the parsimonious reading.

**Three things I was not looking for.** The whole PRC2 core is zonally organised — **EZH2 (p = 0.016), EED
(p = 0.009) and SUZ12 (p = 0.037) all peak in the proliferative zone.** **ESR1 is a resting-zone gene**,
highest in the stem zone and falling significantly on entering proliferation (p = 0.017) — a new argument
that oestrogen acts on the pool rather than the rate, which fits Schrier. And **RTL1 is at the 25th
percentile — it is not expressed in human growth plate at all.** F-R078 concluded RTL1 was the second height
gene at 14q32.2; whatever it does to stature, **it does not do it in the plate.**

**Ask #3 — Polycomb territory. Here I was wrong.** I predicted that Dnmt1-dependent methylation would avoid
the Polycomb canyons where DNMT3A acts. **The Hox clusters are enriched, not depleted** (HoxA 4.82×, HoxC
3.05×, HoxD 2.37×). But the gradient explains it: **canyon cores 1.18× (p = 0.19, not significant), flanks
1.27× (p = 0.020), distal 20–50 kb 1.65× (p = 0.003).**

> **"DNMT1 and DNMT3A act on different compartments" — which I argued in F-R080, F-R081 and F-R082 — is
> withdrawn.** The territories overlap. What is true is that **DNMT1 methylation is un-enriched at the canyon
> cores and rises monotonically with distance from them.** "Lower DNMT3A, preserve DNMT1" can no longer rest
> on territory. It rests on enzyme function and on the phenotypes — `Dnmt1^ΔPrx1` bone length under half of
> control against `Dnmt3a` heterozygotes with longer bones. **Those still hold; the territorial argument does
> not.**

**Ask #2 — is the cortical liability an artefact of the dominant-negative allele?** No mouse exists, so I
used the human population. I pulled all 161 GWAS Catalog SNPs mapped to DNMT3A and every association:
**47 body-height associations, 4 heel-bone-mineral-density. One SNP carries both.**

**rs13002567 — an intron variant of DNMT3A (distance 0, next gene 33 kb away):** the **C allele decreases
height (p = 1×10⁻³⁰⁰)** and the **T allele decreases heel bone mineral density (p = 3×10⁻²⁴)**. They are the
two alleles of one SNP.

> **The height-increasing allele is the bone-density-decreasing allele.** Bell-Hensley's mouse phenotype —
> longer bones, weaker bones — **reproduced in humans on common regulatory variation, not on
> dominant-negative missense.** F-R082 hoped the penalty might vanish with true haploinsufficiency. **It does
> not. The trade-off is intrinsic to the axis.**

**Which makes F-R078's CCN2 pairing load-bearing rather than optional.** CCN2 is at the **97.9th percentile**
in human growth plate — one of the most expressed genes in the tissue — and it is the one agent measured to
raise cortical thickness and mineral content *while* lengthening bone. **The liability is real, and its
counter is already in the stack and already expressed in the right tissue.**

**And three things I genuinely cannot substitute for, stated so they are not mistaken for solved:** whether
**postnatal** DNMT3A reduction reproduces a germline phenotype (TBRS is overgrown by age 3; the mouse
diverges only after 100 days — those point opposite ways); whether height and bone density are separable at
all; and whether removing the fusion deadline and raising the setpoint are additive. **None of the three
exists in the literature in any form.**

---

## The fifty-fourth summary — F-R084: all three "impossible" items resolved, and a flaw caught that would have been fatal

**F-R083 closed with three items I called unsubstitutable. All three are answered — two from human
populations that already run the experiment, one from a standardised mouse resource I had never queried.**

**First, the flaw.** IMPC holds a **true-null `Dnmt3a` heterozygote** (`tm1b`), which I had not looked at. It
shows **reduced bone area (female p = 3.8 × 10⁻⁵) and reduced bone mineral content in both sexes (p = 5.6 ×
10⁻⁴ and 0.039)** — so the cortical penalty is **not** an artefact of dominant-negative missense alleles, and
F-R082's hope is dead. **But the same record shows no body-length gain in that true null.** Combined with
Tatton-Brown's own 2014 sentence — *"a simple haploinsufficiency model appears unlikely"* — that would mean
**a DNMT3A inhibitor, which reduces activity rather than altering it, would be the wrong tool entirely and
the whole arm would be broken.**

> **It is refuted by four human truncating alleles**: c.934_937dupTCTT at **+3.2 SD**, p.Arg320\* at **+3.2
> SDS**, p.G587fs at **+3.77 SD**, p.Arg771\* at **+2.42 SD**. **Haploinsufficiency is sufficient in humans.
> An inhibitor is viable.** And the mouse discrepancy resolves the way Tatton-Brown himself proposed — *"the
> overgrowth phenotype is too subtle to detect in mice"* — with IMPC's own n = 8–9 exposing it.

**Item 2 — separability — answered, and it closes the largest hole in the stack.** Genome-wide, height and
bone size are genetically near-independent (**rg = 0.064 spine, 0.14 hip**). And directly: I pulled every
GWAS Catalog SNP at the two `v(m)` genes. **ACAN has 190 mapped SNPs and a dense height signal with ZERO
bone-density associations. CCN2 the same.** Against DNMT3A's **47 height and 4 BMD associations with one SNP
carrying both in opposite directions.**

> **Height can be moved without a density cost — just not at DNMT3A.** The trade-off is locus-specific, not
> a law. **CCN2 is now the counter on two independent grounds: a height locus with no BMD penalty in human
> genetics, and the one agent measured to raise cortical thickness and mineral content while lengthening
> bone.**

**Item 1 — the postnatal window — answered as a dose question, not a timing one.** The mouse is *"normal
weight and size at birth"* with weights **identical before 100 days**, acquiring the entire phenotype after
it; plates are thicker at P27 and bones longer at 210 days. Both human TBRS girls were **still growing at a
raised setpoint at 10–13 years and had to be treated to stop.** The counterweight is a documented
**post-zygotic mosaic DNMT3A carrier** — found only because **4 of his 14 children have TBRS** — who is
**not tall, at the 32nd percentile.** **So the effect is expressed postnatally but needs a large fraction of
cells: that is a target-engagement specification, not a developmental veto.**

**Item 3 — additivity — answered by a population that already runs both arms.** **47,XXY Klinefelter is the
stack's architecture occurring naturally**: three copies of **SHOX** raise the setpoint, and hypogonadal
**delayed epiphyseal closure** extends the deadline. And they are separable in time — the height excess is
present *"already at ages 4 to 12, well before normal epiphyseal fusion"* (SHOX alone), while the
disproportionate **leg length** comes from the delayed closure. Net **+5 to +7 cm on a normal IGF-1 axis.**

> **And a constraint the branch did not know about.** A 47,XXY man who also carries a heterozygous *ACAN*
> variant reached **151.6 cm (−2.8 SDS)** with **bone age 17 and plates already fused at 16 years 2 months**.
> **ACAN haploinsufficiency advanced bone age and closed the plates despite Klinefelter hypogonadism.** The
> deadline arm is **not unconditional** — a matrix defect forces fusion through it. **So CCN2 is protecting
> the deadline arm as well as the cortex, and anything that degrades matrix sabotages both.**

**What is left is one document and two experiments, and the distinction is now sharp.** The document is
**"Tissue-Biased Expansion of DNMT3A-Mutant Clones in a Mosaic Individual" (S1934-5909(20)30285-X)** —
ScienceDirect returned 403 — which would give the per-tissue mutant fraction in a non-overgrown mosaic
carrier, i.e. the quantitative engagement threshold for the whole arm. The experiments are a DNMT3A
inhibitor in a growing animal with a bone-length readout, and the DNMT3A + oestrogen-ablation combination.
**Both are now well-posed rather than open-ended.**

---

## The fifty-fifth summary — F-R085: the last document, the engagement bracket, and the complete audit

**Tovy 2020 was the last thing I asked for, and it does three things.**

**One — it removes the argument against a postnatal intervention.** The mosaic DNMT3A carrier is not tall,
and F-R084 treated that as evidence the window might be closed. The per-tissue numbers dissolve it: his
**blood is ~100% mutant** while his **eyebrow-hair epidermis is 0.022%**, saliva 8%, urine 20%. The paper's
own heading is *"Expansion of DNMT3A mutant cells is unique to the blood lineage."* **His skeleton was never
substantially mutant.** Everything else points one way — the mouse is *"normal weight and size at birth"*
with weights identical before 100 days, plates thicker at P27, bones longer at 210 days; both TBRS girls
were still growing at a raised setpoint at 10–13 years. **The postnatal window is open.**

**Two — it brackets the dose.** Germline heterozygotes carry a **50% reduction** in every cell and are
**+3.0 SD, thirteen of thirteen**. The mosaic's urine epithelium is 20% heterozygous cells — a **10% average
reduction** — and shows nothing.

> **~10% engagement is too little; ~50% is sufficient and fully penetrant.** That is the first quantitative
> dosing constraint the DNMT3A arm has ever had. Against DY-46-2's measured **33-fold selectivity over
> DNMT1**, 50% DNMT3A inhibition implies **~1.5–3% DNMT1 inhibition** — comfortably inside the hard
> "preserve DNMT1" constraint. **The window exists and it is not narrow.**

**Three — it makes local delivery mandatory rather than preferable.** This man's blood went to ~100% mutant
over six decades while nothing else did. **DNMT3A-deficient HSCs outcompete wild-type ones.** A systemic
inhibitor applies that selection to every haematopoietic stem cell in the body — the clonal-haematopoiesis
pathway, engaged deliberately. *(The counterweight, stated because it cuts the other way: he carried ~100%
mutant blood for sixty years with normal counts and no transformation, while every reconstituted
`Dnmt3a`-null mouse eventually succumbs.)*

**And the mechanism now states in one sentence.** Tovy: DNMT3A loss makes cells *"fail to gain active
lineage-specific methylation normally acquired in WT cells"* during differentiation. **DNMT3A writes the
commitment mark. Less of it delays commitment, so cells stay proliferative longer; more of it commits them
early.** Bell-Hensley's **unchanged PCNA** confirms the thicker plate is retention, not extra proliferation.

**The stack changes.** **Abaloparatide is demoted** — its role was always inference from Winer's safety
data, and **CCN2 does the same job with a direct measurement.** **CCN2 is promoted to load-bearing** with
three distinct jobs: it raises matrix (97.9th percentile in human growth plate), it is the only agent
measured to **raise cortical thickness and mineral content while lengthening bone**, and it **protects the
deadline arm** — because F-R084's ACAN+Klinefelter case showed a matrix defect forces fusion straight
through hypogonadism. **Selective DNMT3A inhibition enters as the setpoint arm**, at ~50% engagement, local.

**On "infinite," I am going to be straight.** The deadline can be removed — two men grew into their
thirties. The setpoint can be raised about 3 SD. The two are additive; 47,XXY runs both. The rate terms have
6.8× of measured human headroom. **But every arm has a finite measured magnitude. TBRS patients reach +3 SD
and stop. The ESR1-null man kept growing at 0.3 cm/year.** Unbounded growth needs `a > b` sustained
indefinitely, and that is the one place where the two best papers in the field flatly contradict each other
— Heyn says progenitors are pushed out of self-renewal, Jackson says their numbers stay constant and only
output falls. **This is a stack that plausibly raises the ceiling by several standard deviations and removes
the deadline that stops you reaching it. That is a large claim and it is supported. It is not the same claim
as infinite.**

**And the hole that deserves the next effort is not biology.** After the two TBRS girls had their legs
arrested, they grew **+10.9 cm of sitting height and +20.5 cm of arm span**. F-R074's delivery route reaches
one epiphysis; a human has about thirty plus the spine. **A stack that reaches only the knee produces the
proportions of an epiphysiodesis patient, not height** — and nobody in this literature has even posed the
problem.

---

## F-R089 — the pool CAN be bought, and I had the papers on disk

Tate stopped me for looping and told me to re-read what we already have, looking specifically for
things **read wrong or incomplete**. He was right. Five claims in F-R088 are withdrawn, and every
refutation came from a file already in this repository.

**1. "No pharmacological intervention has ever expanded the pool" — false.** `trompet2024` (supplied as
`jci.insight.165226.sd_2.pdf`, cited by name in F-R022) has a figure *titled* "SAG administration
expands the growth plate skeletal stem cell pool." Systemic SAG, 25 µg/g/day i.p. × 7 doses after SOC
maturation: **PTHrP⁺ cells +61%**, confirmed by FACS. Intra-articular: **65.5 → 139.8 cells/mm²,
P=0.017, all within the resting zone.** And the sentence that dissolves Tate's delivery constraint:
*"3 intra-articular injections had a similar effect on epSSCs' clonogenicity as 7 systemic injections."*

**2. I had Hedgehog's sign backwards.** F-R088 filed Hh under "breaks quiescence." Trompet sequenced the
sorted stem cells: **Wnt is a top-2 downregulated pathway after SAG** — *"activation of Hh pathway
creates a Wnt-inhibitory microenvironment."* Hallett 2021 says that environment is what maintains the
resting zone. So Hh does not break the niche; **Hh builds it.** The age-dependent negative results are a
drug-toxicity artefact in infant animals — genetic Ptch1 ablation expands clones at every age tested.

And it compounds: the bead's Gli1 signal was **gone by 3 weeks**, yet femur length kept diverging from
the contralateral control at 1, 2 and **6 months**. A rate agent cannot do that. Only `n₀` can.

**3. GH is depleting our pool right now.** Chu/Chagin, *PNAS* 2025 (PMC12685065, open access), built
specifically to model GH given to non-deficient children: PTHrP⁺ stem cells down P<0.0001, label-
retaining cells down P<0.001, **EdU and Ki67 unchanged** — *"GH promotes their committed cell division,
leading to stem cell depletion."* Our somatropin is at 0.07 mg/kg/day. But Ohlsson 1992 (PNAS 89:9826)
shows **physiological** GH gives **1.95 ± 0.13×** the germinal pool. Same hormone, opposite signs,
separated by dose. The fix costs nothing: **lower the dose toward physiological and make it intermittent**
— which is the PNAS authors' own recommendation.

**4. Mecasermin buys zero pool.** Ohlsson tested IGF-1 head-to-head in the same experiment:
**0.96 ± 0.04.** Nothing. *"IGF-I acts only on the proliferation of the resulting chondrocytes."*
F-R088 added it as *the* obtainable pool agent and named its effect the top open question. That question
was answered in 1992. It survives as a rate agent only.

**5. I had been quoting Schrier's rate as if it were his number.** The "flat 9.2/9.2/7.6%" I carried for
rounds is the **BrdU labelling index**. Read properly, `schrier2006.pdf`: **RZ chondrocyte number per mm
falls with age, P<0.001**, in all three regions. The rate collapses by week 5 and plateaus; the number
keeps draining. That answers "empty or asleep" — it drains, and the drain is measured.

**And it hands us a second pool agent that is an approved generic.** Schrier's dexamethasone arm, which
I had never read past the abstract: 0.5 mg/kg/day × 2 weeks → BrdU index **down** (P<0.001) but
**resting-zone chondrocyte number GREATER, P=0.016**, localised to the reserve zone, and not mediated by
IGF-1. Slow the divisions, spend the pool more slowly, end with more cells. The cost is that
glucocorticoids suppress growth — so dexamethasone is not a continuous agent, it is a **banking** agent
for a cycled protocol. That is F-R022's "pulse, not chronic state" achieved by **cycling systemic agents
in time** rather than by local delivery in space, which is exactly the constraint Tate set.

**The structural conclusion.** Seven interventions across five experiments move the number of stem cells
with **proliferation essentially unchanged**. This is not a rate axis, it is a **fate** axis —
symmetric-renewing versus lineage-committed division — and it is **bidirectionally drug-accessible**.
F-R088's "the pool cannot be bought" is withdrawn, and so is its corollary that pool and rate are the
same axis with opposite signs: Trompet's bead raised pool *and* rate together; Schrier's dexamethasone
raised pool while lowering rate.

**What we still cannot have:** no Smoothened agonist has ever been given to a human. SAG and
purmorphamine are catalogue reagents. The nearest real things are **Oxy133** (MAX BioPharma, IND-track,
binds SMO directly, cyclopamine-blocked) and **20(S)-hydroxycholesterol** (endogenous sterol, allosteric
SMO agonist at the cysteine-rich domain, EC50 ≈ 3 µM, confounded by LXR agonism). That is the top ask.
The obtainable substitute follows from Trompet's own mechanism — if the effector is Wnt inhibition, then
**niclosamide, pyrvinium, or a clinical-stage PORCN inhibitor** reaches the same niche state, at the
honest cost of being anti-osteoanabolic.

---

## F-R090 — it exists: four FDA-approved Smoothened agonists

I closed F-R089 by asserting that no Smoothened agonist had ever been given to a human. **That was wrong
by sixteen years, and the reason I got it wrong is instructive: I searched, got back nothing but
antagonists, and concluded the class was empty. Inhibitors are what oncology funds and therefore what
the literature indexes. The agonists were approved decades ago — for skin and for asthma — and nobody
filed them under Hedgehog.**

`Wang JC et al., PNAS 2010;107:9323 (PMC2889058, Duke)` screened **68 glucocorticoids** from the
FDA-approved Prestwick library on a Smo/β-arrestin2-GFP assay and found four that **bind Smo, drive Smo
internalisation, activate Gli, and synergise with Sonic hedgehog**: **halcinonide, fluticasone
propionate, clobetasol propionate, fluocinonide.** Their own closing sentence: these *"provide a
significant jumpstart in the process of beginning human studies."*

**Fluticasone propionate is the most potent at the receptor (EC50 0.099 µM, ten-fold ahead of the rest)
and is the only one with a routine systemic-ish route and a large paediatric pharmacokinetic record.
Halcinonide produces the largest cellular response (40–50× over vehicle, matching purmorphamine's
maximum).**

**This corrects F-R089's Tier 2.** I had nominated dexamethasone as the banking agent. **Dexamethasone is
not a Smoothened agonist — it inhibits Shh-driven proliferation dose-dependently**, as do cortisone,
prednisolone and corticosterone. So Schrier's dexamethasone result is a GR conservation effect, not the
Hedgehog mechanism, and conservation is the weaker buy. The structure–activity rule explains the split
and it is not "fluorinated equals active": the actives carry 11β-OH **plus a large, branched, hydrophobic
C-17**, while the inactives have a small hydrophilic C-17 and often a 9α-fluorine — which describes
dexamethasone exactly.

**The finding that makes the class usable** is that the Smoothened arm is separable from the
glucocorticoid-receptor arm. The proliferative response survives 5 µM mifepristone, and dexamethasone
activates GR identically while producing the opposite outcome — so the effect is *"independent of
glucocorticoid nuclear receptor signalling and most probably attributable directly to activation of
Smo."* That means the growth-suppressing arm the glucocorticoid class otherwise carries can be stripped
with an approved drug that already has a chronic systemic dosing precedent.

**Chu 2026, read properly, moves the target — and this is where our nuance was wrong.** The human resting
zone holds two clusters. **GP1** is the dormant root: low WNT, **low TGF-β and actively repressing it
through THBS1/THBS2/DCN**, high SFRP5, the lowest proliferative index of any cluster. **GP2 is the
PTHrP-positive tier, already partially activated.** Every mouse pool number this branch has ever quoted —
Trompet's +61%, his 65.5 → 139.8 cells/mm², the PNAS GH depletion — is measured on a **PTHrP reporter**,
which in human terms is **GP2, not the root.** So Trompet's expansion is consistent with genuine pool
growth *or* with recruitment of GP1 into GP2, and **nobody has measured GP1 under any intervention in any
species.** That is the last open hole and I am not going to paper over it. What leans toward real
expansion: the bead's Gli1 signal was gone by three weeks and the length gap was still widening at six
months, whereas recruitment off a fixed root should decelerate.

Chu also hands us **the half of the niche we never had**. We had low-WNT from Hallett. GP1 is low-WNT
**and** low-TGF-β, and GH activates TGF-β autocrine in exactly these cells — so **TGF-β blockade should
preserve the root**, and that axis is obtainable: losartan (approved, paediatric record), pirfenidone
(approved), galunisertib (phase II).

**On adapting it to humans, the counterweight goes first.** Inhaled fluticasone reduces growth velocity
in children — one of the best-documented paediatric drug effects there is. That cuts both ways: at
asthma doses the GR arm dominates the rate term, *and* it is direct proof that inhaled fluticasone
reaches the human growth plate at pharmacologically active concentrations. The delivery question is
answered by the side effect. And the shape of that clinical signal — velocity down a lot, final adult
height down very little — is a pool-preserved, rate-suppressed signature.

**The one thing nobody has done: no Smoothened agonist has ever been tested on cartilage or growth
plate.** The FGSA functional assay was cerebellar granule precursors. The Hedgehog-and-growth-plate
literature and the FDA-approved-Smoothened-agonist literature have never been crossed, and that crossing
is the whole programme.
