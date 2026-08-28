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
