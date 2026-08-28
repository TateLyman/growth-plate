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
