# F-R012 — The discharge gradient, and the death of my own best hypothesis

**Sources read in full for this round:** `stegen2019` (Stegen S, Laperre K, … Eyre DR, Ghesquière B,
Fendt S-M, Carmeliet P, Carmeliet G. *HIF-1α metabolically controls collagen synthesis and
modification in chondrocytes*. Nature 2019; author manuscript NIHMS1576233, main text + all methods
+ all Extended Data legends including every exact p-value) · `duncan1996` / Farquharson C, Whitehead
CC, Loveridge N. *Alterations in pyridinoline cross-link concentrations during the differentiation
of chick growth plate chondrocytes.* Biochim Biophys Acta 1996;1290:250–256 · `oohira1974` / Oohira
A, Kimata K, Suzuki S, Takata K, Suzuki I, Hoshino M. *A correlation between synthetic activities for
matrix macromolecules and specific stages of cytodifferentiation in developing cartilage.* J Biol
Chem 1974;249:1637–1645.

---

## 0. Two corrections, both to me, before anything else

**(a) My prediction about the zonal modification gradient was wrong, and wrong in the direction that
matters.** In my ask #2 I wrote that hydroxyproline:proline or cross-link density measured *by growth
plate zone* had never been done, and that "the law predicts it rises toward the hypoxic centre."

It has been done — twice, in 1974 and 1996 — and it **falls**:

> "In contrast, the proliferating chondrocyte zone of the growth plate had approximately a **10-fold
> greater pyridinoline cross-link concentration than the mature hypertrophic zone**."
> — Farquharson 1996, Abstract

Ask #2 is closed. It was answered thirty years ago, by an instrument (sequential transverse
microdissection + HPLC) nobody has pointed at a human plate since.

**(b) The bigger correction: the thesis I have been building since F-R006 has now been tested against
a length endpoint, and it lost.** F-R006 through F-R011 converge on *charge without discharge* — the
claim that the plate's ceiling is its inability to clear hypertrophic matrix, and that unjamming
discharge buys length. Stegen 2019 ran exactly that experiment in vivo with two drugs and a tibia
ruler. **Unjamming the discharge did not lengthen the bone. Restoring the energy supply did — while
leaving the jam worse than before.** §3 has the table. I am not going to bury this in a subsection:
it is the most useful thing this branch has produced, and it invalidates my own last five rounds as a
route to length.

---

## 1. What the three papers actually say

### 1.1 Farquharson 1996 — the plate de-cross-links on the way down

Chick tibial growth plate, cut into ~20 sequential transverse sections, each staged morphologically
(ALP histochemistry, COL10 immunostaining) and assayed analytically (HPLC for pyridinoline PYD and
deoxypyridinoline DPD).

- Pyridinoline: **~10× higher** in sections with no COL10 (N9–N11) than in sections with COL10
  (N14–N16). The gradient tracks differentiation inversely.
- Deoxypyridinoline: **absent** from articular cartilage and the upper plate; first appears at N11,
  a section with strong ALP activity — i.e. **prehypertrophic, before COL10 is detectable** — and is
  highest in the most differentiated sections, where it becomes the principal pyridinium cross-link.
- Articular cartilage does the opposite: PYD maximal in the deep mature zones. So this is not a
  cartilage-wide property; it is specific to the growth plate.
- Collagen concentration (µg/mm³) varies ~5-fold, peaking ~500 µm from the cartilage surface, and
  is **unchanged** in the dyschondroplastic lesion — so the cross-link changes are not a collagen
  quantity artefact.

Authors' conclusion, verbatim:

> "We conclude that **the decrease in pyridinoline cross-link concentration down the growth plate may
> be an essential adaptation (via increased collagenase activity and collagen turnover) of the matrix
> for vascular invasion and osteoclastic resorption to occur.**"

And the internal control, which is the part that made me take this seriously — **tibial
dyschondroplasia**, a retained-cartilage lesion where differentiation arrests in the prehypertrophic
zone:

> "In tibial dyschondroplasia, where chondrocyte differentiation is arrested in the prehypertrophic
> zone, **higher concentrations of both cross-links were found with increasing distance down the
> lesion.**"

The normal plate's cross-link concentration falls as you descend. The lesion's **rises**. A natural
experiment in failed discharge, with the matrix chemistry measured.

### 1.2 Oohira 1974 — the gradient is not built at synthesis

13-day chick embryo epiphysial cartilage, four morphologically defined zones, `[U-¹⁴C]proline` and
radioautography per zone. Two results the 1996 paper does not have and does not cite:

- **Collagen synthesis rate per cell peaks at the Zone 3 → Zone 4 transition** (enlarging →
  hypertrophied). In Zones 1–2, "the collagen synthesis proceeds at **one-seventeenth to
  one-twentieth** the rate occurring in the cells over the most active zone." Table II, total
  radioactivity per nmol DNA: Zone 1 = 686, Zone 2 = 905, **Zone 3 = 2260**, Zone 4 = 1721.
- **The hydroxylation state of newly made collagen is roughly constant across all four zones.** The
  labelled α-chains purified from every zone "showed little change in the degree of hydroxylation of
  the proline moieties," and both chromatographic components (X = α1(II), Y = a ~125 kDa precursor)
  have a hydroxyproline:proline ratio of about 1:1.

Put those together with Farquharson and the 10-fold gradient stops being mysterious. The hypertrophic
zone is not de-hydroxylating anything. It is **synthesising new, un-cross-linked collagen at ~17–20×
the proliferative rate while the old cross-linked matrix is removed.** Cross-link *concentration*
falls because the denominator is being replaced. Farquharson attributed the fall to collagenase and
turnover; Oohira supplies the other half of the same turnover — the synthesis half — and it is
enormous.

(One caveat I will not paper over: Oohira's Table II column (d) is hydroxyproline cpm as a percentage
of *total* label, which is confounded by non-collagenous protein. Normalising it against the
collagenase-digestible fraction in the same table gives ~47%, 46%, 48%, **30%** for Zones 1–4 — a
real-looking drop in Zone 4. That arithmetic is mine, not theirs, and it disagrees with their own
conclusion drawn from purified chains. I flag it as an open discrepancy rather than a result.)

Oohira also reports the precursor→α1(II) conversion rate "increasing gradually in going from Zone 1
to Zone 4." Processing accelerates downward too. Everything about the lower plate is faster
throughput, not different chemistry.

### 1.3 Stegen 2019 — the same molecule, manipulated, with a ruler on the bone

Conditional PHD2 deletion in chondrocytes (`Phd2chon-`) → HIF-1α accumulation → skeletal dysplasia.
Mechanistically this is Farquharson's gradient run backwards on purpose:

- Collagen-modifying enzymes up: P4HA1/2, P3H1, PDI, PLOD1/2, LOX (all p ≤ 0.0006).
- Hydroxyproline up; Lys87 hydroxylation up; **hydroxylysylpyridinoline (HP) cross-links and total
  pyridinoline up** — the *same molecule Farquharson measured by zone*, moved by genetics.
- Mutant collagen fibres **more resistant to MMP9 and MMP13 degradation** (Fig 2f); serum CTx-II
  down; COL2⁺ cartilage remnants retained in the trabeculae; trabecular bone volume up.
- The source of the αKG is glutamine via HIF-1α-driven GLS1, not glucose and not pyruvate
  (MCT2 inhibition changed nothing); intracellular αKG **+400%**, αKG/succinate 2.2×,
  αKG/fumarate 2.3×.
- Separately, glucose oxidation falls → energy deficit → AMPK phosphorylation up, proliferation
  down, UPR activated, **collagen synthesis down**.

So the mutant is a plate that makes *less* collagen, modifies it *more*, and therefore cannot clear
it. It is Farquharson's dyschondroplasia phenotype, arrived at from the metabolic side, with the
cross-link chemistry actually measured. The two papers describe one lesion 23 years apart.

The authors' own summary sentence:

> "This metabolically regulated collagen modification renders the cartilaginous matrix **more
> resistant to protease-mediated degradation and thereby increases bone mass.**"

Note what that sentence says the jam produces. **Mass.** Not "and thereby shortens the bone."

---

## 2. The drug arms

Dosed IP daily P2.5 → P9.5, in wild-type and mutant:

| drug | target | dose |
|---|---|---|
| DCA (dichloroacetic acid) | PDK inhibitor → restores glucose oxidation | 100 µg/g/day |
| BPTES | GLS1 inhibitor → cuts glutamine→αKG | 25 µg/g/day |
| dimethyl-αKG | αKG donor | 50 µg/g/day |

Text results, verbatim on the two that matter:

> "Restoring glucose oxidation in PHD2-deficient chondrocytes by blocking PDK corrected the energy
> deficit, restored proliferation and prevented UPR activation, accompanied by increased collagen
> synthesis and hydroxyproline levels. **These metabolic changes further augmented the COL2-positive
> cartilage remnants** and, consequently, mineralized bone mass."

> "…co-administration of BPTES to DCA-treated mutant mice **normalized the increase in αKG and
> hydroxyproline levels, COL2-positive cartilage remnants and mineralized bone mass to the levels of
> wild-type mice**…"

And the one everybody skips:

> "Of note, GLS1 inhibition also negatively affected collagen and bone properties **in wild-type
> mice**, but impaired chondrocyte proliferation as well…"

---

## 3. The dissociation — the actual result of this round

Every arm above was also measured with a **tibia ruler** (ED Fig 1e, 7n, 9c, 10g). Nobody quotes
those panels. Reading the exact p-value lists in the Extended Data legends against the contrast
names, here is what the length endpoint says. `—` means *the contrast is absent from the paper's
own exhaustive p-value list*, i.e. not significant; **n.m.** means the arm was never length-measured.

| arm | αKG / OH-Pro | cartilage remnants | bone mass | **TIBIA LENGTH** |
|---|---|---|---|---|
| `Phd2chon-` vs WT | ↑↑ | ↑↑ | ↑↑ | **↓, p = 1×10⁻⁸ (9c), 6×10⁻⁵ (10g), 2×10⁻⁶ (7n)** |
| mutant + **BPTES** (unjam the discharge) | **normalised** | **normalised** | **normalised** | **— not rescued** |
| mutant + **DCA** (restore the energy) | ↑ *further* | ↑ *further* | ↑ *further* | **rescued: p = 1.2×10⁻⁴ vs mutant-veh, and n.s. vs WT** |
| mutant + DCA + BPTES | normalised | normalised | normalised | **n.m. — never measured** |
| **WT** + αKG (over-modify a normal plate) | ↑ (p=0.02) | ↑ (p=0.006 SafO, 2×10⁻⁵ COL2) | ↑ (p=3×10⁻⁴) | **— unchanged** |
| **WT** + BPTES (under-modify a normal plate) | ↓ | ↓ | ↓ | **↓↓, p = 1×10⁻⁷** |
| **WT** + DCA (restore energy in a normal plate) | — | — | — | **— unchanged** |

Read the last four rows slowly.

1. **Deliberately over-modifying a normal growth plate does not shorten it.** αKG in wild-type mice
   raised hydroxyproline, raised COL2⁺ remnants, raised trabecular bone volume — and left tibia
   length alone. The discharge jam, induced cleanly and confirmed by four separate readouts, **cost
   zero length**.
2. **Deliberately un-jamming discharge in a normal plate is catastrophic.** BPTES in wild-type mice
   shortened the tibia at p = 1×10⁻⁷ — the largest length effect anywhere in the paper, larger than
   the mutation itself. Cutting glutamine flux to reduce cross-linking wrecks the bone.
3. **In the mutant, normalising the modification chemistry did not restore length.** BPTES fixed
   αKG, hydroxyproline, remnants and bone volume, and the tibia stayed short.
4. **What restored length was restoring ATP — while making the jam strictly worse.** DCA drove
   remnants and mineralised mass *further* up and brought tibia length back to wild-type.

**Therefore: in the growth plate, matrix modification state is a mass valve. It is not a length
valve. Length is set by the energy available for proliferation and protein synthesis at the top of
the plate.** Discharge failure diverts the tissue into trabecular bone instead of clearing it; it
does not slow the plate's linear output.

---

## 4. What this kills

- **My F-R006 → F-R011 thesis, as a route to length.** "Charge without discharge" is a real and
  well-evidenced description of the matrix. It is not the length-limiting step. I built four rounds
  on an inference and the one paper that tested it with a ruler says the inference is false. F-R011's
  master equation — `Growth = SYNTHESIS × DISCHARGE, and OXYGEN sets both` — has to become
  `Length ≈ f(SYNTHESIS); Mass ≈ g(DISCHARGE); oxygen sets both, but only the first term is length.`
- **The entire protease / cross-link / LOX / BAPN intervention class, for length.** The atlas holds
  40 files touching pyridinoline, 24 touching Farquharson, 77 touching PLOD, 123 touching MMP13. Every
  one of them is reasoning about a valve that Stegen moved in both directions in vivo with **no length
  effect in a normal animal in the permissive direction, and a p = 10⁻⁷ catastrophe in the other.**
- **Any hope that αKG is a length agent.** The atlas's αKG contraindication (which I tried to
  downgrade in F-R010 and withdrew in F-R011) is now confirmed a second time and more sharply:
  αKG in a *wild-type* mouse is not merely neutral for length, it actively builds the remnant
  phenotype. F-R010's downgrade stays withdrawn.
- **The Lublin pig corpus, finally explained in one line.** Tatara's AKG and HMB studies move mass,
  density and strength and leave length flat or negative (`tatara2007`: HMB 200.9 → 196.8 mm,
  **−2.0%**, with GH +38% and IGF-1 +20%). Those are modification-arm interventions. **They were
  never going to move length.** They landed exactly where Stegen's table says they land. The one
  exception — `andersen2008`, sixth rib 232.9 → 250.0 mm, **+7.3%, p<0.01**, in the same 24 animals
  where humerus and femur were null — is *not* explained by this and I am no longer going to pretend
  my "least hypoxic plate" story covers it. It stays an open anomaly (§6).

---

## 5. What survives, and where it points

The survivors are all on the synthesis side, and they line up with F-R008/F-R009 rather than
F-R006/F-R011:

- **Energy at the top of the plate is the length term.** DCA rescued length by restoring glucose
  oxidation, proliferation and protein synthesis. mTORC1 (F-R008: `newton2015` bafilomycin +91–170%
  length with h_term 14 → 24 µm; `newton2018` Tsc1 metatarsals +52%, p=0.0016) is the same axis read
  from the signalling side. Two independent literatures, one term.
- **Oohira localises where that energy is spent.** Collagen synthesis per cell is **17–20× higher**
  at the Zone 3/4 transition than in the proliferative zone. The metabolic bottleneck for the
  *length* term is not in the resting or proliferative zone at all — it is at prehypertrophy, in
  exactly the cells whose terminal height CORR-361 says contributes 44–59% of elongation. Newton's
  bafilomycin result raising h_term by 71% is a measurement in the same compartment.
- **CORR-203 lands on my best candidate, hard.** DCA rescued a *deficient* tibia and did **nothing**
  to a wild-type one ("DCA treatment had no effect in wild-type cells"; the WT-veh vs WT-DCA contrast
  is absent from the ED Fig 10g p-value list). Restoration ≠ elevation. DCA is not a height drug and
  I am not going to launder it into one. What it is, is a *proof that the length term is
  bioenergetic and is pharmacologically addressable* — which is a different and more useful claim.

The reframed target: **not "clear the jam," but "raise the ceiling on ATP and biosynthetic capacity
in the prehypertrophic compartment of a plate that is not deficient."** That is a genuinely different
question from anything in F-R006–F-R011, and — unlike the discharge question — it has never been
tested with a length endpoint in a normal animal, because every experiment in this space has been a
rescue.

---

## 6. Atlas coverage — verified by grep, and I got this wrong pre-flight too

I noted earlier that `cartilage remnant` returned 0 files. That grep was scoped to
`atlas/nodes` + `gaps.yaml` + `docs` + `CLAUDE.md`, not to `atlas/`. CORR-313 says grep the graph
before drafting; I greped a subset and reported it as the graph. Re-run across all of `atlas/`,
`docs/` and `query/`:

| term | files |
|---|---|
| `Stegen` | 26 — **all `stegen2020`** (SOX9→GLS1, PMID 32470321) |
| `stegen2019` / PMID for the Nature PHD2 paper | **0 in `atlas/sources/`** |
| `Phd2chon` | **0** |
| `PHD2-deficient` | **0** |
| `collagen overmodification` | **0** |
| `dichloroacetate` / `BPTES` | **0 / 0** |
| `Oohira` | **0** |
| `PHD2` | 16 — but only two substantive, both in the *fracture-callus angiogenesis* context |
| pyridinoline / Farquharson / PLOD / MMP13 | 40 / 24 / 77 / 123 |

So the atlas is **not** blind to cross-linking chemistry — it is deeply covered. What it does not
hold is the paper that *manipulated* that chemistry in vivo and measured the bone. Its PHD2 entries
reason about PHD inhibitors for callus angiogenesis; `docs/target_screen_round1.md` correctly
withdrew the vadadustat/roxadustat/daprodustat row on polarity grounds via `schipani2001`
(proliferation) and the vascular arm — **the right call for the wrong-but-adjacent reason.** Stegen
2019 supplies the third and strongest reason, which is neither proliferation nor vasculature:
a PHD inhibitor over-modifies collagen and converts growth-plate cartilage into trabecular bone.
The withdrawal should be upgraded from inference to a measured in-vivo contraindication with
p = 1×10⁻⁸ on tibia length.

**Proposed atlas additions (I am not writing to `atlas/`; these are for you):**
1. `stegen2019` as a T1 primary — the only in-vivo experiment that dissociates growth plate mass
   from growth plate length pharmacologically.
2. `duncan1996` + `oohira1974` as the zonal matrix-chemistry pair — jointly they close the
   "modification by zone" question the graph does not currently ask.
3. A correction-ledger entry. Proposed wording: **"A matrix-clearance defect is a mass phenotype.
   Do not price it as a length phenotype without a ruler. (stegen2019: αKG in wild-type mice raised
   hydroxyproline, remnants and bone volume with no change in tibia length; GLS1 inhibition
   normalised all three and shortened the tibia at p=1e-7.)"** This generalises past collagen — it is
   the same error class as CORR-203 but on the output axis rather than the baseline axis.

---

## 7. Asks

**#2 — CLOSED.** Zonal cross-link and hydroxylation profiles exist (Farquharson 1996, Oohira 1974).
Answer: pyridinoline falls ~10× down the plate, DPD rises and appears first at prehypertrophy,
hydroxylation of newly made collagen is roughly constant by zone, and collagen synthesis per cell is
17–20× higher at the Zone 3/4 transition. Never done in human tissue — but the chick answer is
consistent enough across two methods and two decades that I would not spend your money on it.

**#3 — PARTIALLY CLOSED, and downgraded in importance.** `stegen2019` is a genetic O₂-sensing
manipulation with tibia-length endpoints in six drug arms, which is most of what I wanted from a
controlled-pO₂ growth study. Given §3, a direct pO₂-controlled culture study would now mostly tell me
about the mass axis, so I am **withdrawing this ask** rather than asking you to keep hunting it.

**New asks, in order of decision value:**

1. **`stegen2019` Source Data, or an email to Geert Carmeliet (KU Leuven) for one number.**
   The DCA + BPTES arm was **never length-measured** — ED Fig 10g's n-list covers only
   `Phd2chon+-veh`, `Phd2chon--veh`, `Phd2chon--DCA` and `Phd2chon+-DCA`. That single missing panel
   decides whether the two arms are truly independent (length stays rescued while mass normalises →
   you can have both) or whether normalising modification costs back the length DCA bought (→ they
   are coupled after all and §3 needs qualifying). The mice were dosed, the tibias were collected,
   the ruler was already in the room for the neighbouring panels. **This is one measurement that may
   already exist in a drawer.** Same lab as `loopmans2025`, which you already fetched — S. Loopmans
   is an author on both.
2. **`andersen2008` full text, or its raw per-animal data.** The rib went +7.3% while the humerus and
   femur did nothing, in the *same 24 pigs on the same AKG dose*. Under §3, AKG should have moved
   mass everywhere and length nowhere. It moved length in one bone. Either that is the single
   counter-example to this whole round, or it is a measurement artefact (rib length is hard to
   define), and I cannot tell which from the table alone. **This is now the highest-value anomaly in
   the branch.**
3. **Any study that raised chondrocyte oxidative capacity in a non-deficient animal and measured
   bone length.** Every energy-arm result I have — DCA, and arguably the mTORC1 set — is a rescue of
   a defect. CORR-203 says that is not evidence of elevation. If nothing like this exists, that
   absence is itself the finding, and it is where I would point the next round.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
This round the instrument existed, was used, and was printed in an Extended Data legend that the
paper's own abstract does not mention. The correction came from reading p-value lists.*
