# F-R013 — The atlas already found the answer, twice, and a spreadsheet bug ate it

**Operator-supplied sources read in full:** `andersen2008` (Andersen NK, Tatara MR, Krupski W,
Majcher P, Harrison AP. *The long-term effect of α-ketoglutarate, given early in postnatal life, on
both growth and various bone parameters in pigs.* J Anim Physiol Anim Nutr 2008;92:519–528) ·
`chang2023` (Chang S-H, Giong H-K, Kim D-Y, Kim S, Oh S, Yun UJ, Lee J-S, Park KW. *Activation of
Nrf2 by sulfuretin stimulates chondrocyte differentiation and increases bone lengths in zebrafish.*
BMB Rep 2023;56:496–501, **PMID 37748761**) · `abukheit2022` (Abu-Kheit R, Kotev-Emeth S, Hiram-Bab S,
Gabet Y, Savion N. *S-allylmercapto-N-acetylcysteine protects bone cells from oxidation and improves
femur microarchitecture in healthy and diabetic mice.* Exp Biol Med 2022;247:1489–1500).

**Also this round:** a full audit of `atlas/data/round436/coverage.json` (2,193 rows), with a
recovery script committed at `frontier/screens/r436_recovery/recover.py`.

---

## 0. The headline

The single best out-of-the-box height lead in this repository was found by the atlas's own
blind-spot instrument, **flagged with its highest marker**, and then lost — twice, by two
independent mechanisms, neither of which is a biology error:

> `atlas/data/round436/coverage.json`, row `NRF2 / KEAP1`, domain `signalling`:
> **direction: "⭐ Nrf2 ACTIVATION stimulates chondrocyte differentiation and INCREASES BONE LENGTHS
> in zebrafish"** · source: `zebrafish 37748761` · **tier: THIN · n_nodes: 1 · n_gaps: 1 ·
> n_bib: 0 · n_ledger: 0**

PMID 37748761 is the paper you handed me this turn. The atlas found it, starred it, scored it THIN,
never entered it in the bibliography, and never wrote a node. And the *single node* that downgraded
it from ZERO to THIN — `round297_thirty_obtainable_drugs_this_atlas_has_never_had_an_opinion_about.yaml`
— contains exactly one mention of Nrf2, and it is this:

> "✗ Metformin's chondrocyte literature is entirely osteoarthritis — mitochondrial function, Nrf2,
> senescence. **No growth-plate work and no bone-length endpoint in any species.**"

**A starred lead whose whole content is "increases bone lengths" was down-ranked by a string match on
a sentence saying a different drug has no bone-length endpoint.** That is the miss, exactly, and it
is mechanical.

That is loss #1. Loss #2 is worse and it is systematic. §3.

---

## 1. Your three papers

### 1.1 `chang2023` — my ask #3, answered, and positive

Last round I asked for *"any study that raised chondrocyte oxidative or biosynthetic capacity in a
NON-deficient animal and measured bone length,"* and said that if it did not exist, the absence was
the finding. It exists.

- Sulfuretin (a flavonoid of *Rhus verniciflua*) stabilises NRF2 and drives its program: **Hmox1
  9.3×, Nqo1 4.6×**, plus Gclm and Srxn1; abolished in Nrf2-knockout MEFs.
- In differentiating C3H10T1/2 cells and in primary P7 mouse chondrocytes it induces **Col10a1,
  Mmp13, Mmp3** — the late/hypertrophic program — **without changing Col2a1, Aggrecan or Sox9.**
  It acts at the prehypertrophic→hypertrophic transition and nowhere earlier.
- Zebrafish, 1 dpf → 5 dpf, 100 µM: **body length +5.6% (p<0.05)**; over 6 days, +3.9%.
- **The internal control is the good part.** Whole-mount in situ: the **ceratohyal** — an
  *endochondral* element — grew **+40% at its centre (col10a1) and +20% in total length (ctgf)**,
  while the **parasphenoid** — an *intramembranous* element in the same fish — **did not change at
  all.** The effect is specific to endochondral ossification, which is the only kind that makes you
  taller.
- In zebrafish the drug induced **nqo1, gclc and gclm**. GCLC and GCLM are the catalytic and modifier
  subunits of glutamate–cysteine ligase, **the rate-limiting enzyme of glutathione synthesis.**
- **A second, structurally unrelated chemotype reproduces it: dimethyl fumarate (DMF), an
  FDA-approved drug**, at 1 and 4 µM, increased body length (+4.77%), increased alizarin-red⁺
  vertebral elements, and induced the same hypertrophic markers.
- **Mechanism confirmed by loss of function:** `nrf2` morpholino knockdown abolished 42% of the
  sulfuretin effect and 33.8% of the DMF effect.

Honest limits, stated because they matter: zebrafish larval body length at 5–7 dpf is dominated by
notochord and somite, not by a mammalian growth plate (the ceratohyal panel is the part that speaks
to endochondral growth, and it is the strongest panel). 100 µM is high. The authors themselves flag
the absence of mammalian histology. And the paper's own reference 13 reports that **Nrf2
overexpression *inhibits* chondrocyte differentiation in ATDC5 cells** — a real, unreconciled
conflict, and probably a dose/duration one, since Nrf2 is a classic hormetic factor.

### 1.2 `abukheit2022` — supporting, and confounded, and I will not oversell it

ASSNAC is a cysteine donor *and* an NRF2 activator — which is precisely what F-R003 predicted the
plate should want, having found it looks like a **cysteine auxotroph** (SLC7A11 the lowest
transporter on its panel at 1.1–3.2%, CBS 0.0–0.6% by zone, full downstream GSH machinery present).

In **healthy** C57BL/6 female mice, 50 mg/kg/day IP, 8 weeks (age 12–20 wk): bone-marrow glutathione
**+110%**, adherent BMSCs +60%, CD73⁺/CD45⁻ **+134%**, cortical diameter +3%, Ct.MOI +10%, and
**femur length +3% (p≤0.05, n=8 vs 8)**.

But the authors read their own result against themselves, and they are right to:

> "These changes were **not accompanied by an increase in relevant growth plate parameters** that
> may explain the increased femur length suggesting that it is probably associated with the increase
> in body weight in healthy mice."

The cartilage-layer thickness did not move. In db/db mice the length change was +5%, **p = 0.110.**
So this is a **+3% length signal in a non-deficient mammal that the authors attribute to body
weight** — supporting, mechanistically aligned, and not clean. It goes in the ledger as corroboration
of the glutathione axis, not as a length result.

### 1.3 `andersen2008` — the anomaly resolves, and hands over a contraindication

This was my #2 ask: the rib that went +7.3% while the humerus and femur did nothing. Full Table 2,
n=10 per group, day 169, low dose 0.1 g/kg/day:

| | control | AKG | |
|---|---|---|---|
| sixth rib length | 232.9 ± 4.2 | **250.0 ± 4.1** | **+7.3%, p<0.01** |
| humerus length | 182.4 ± 2.4 | 182.9 ± 2.3 | +0.3%, ns |
| femur length | 200.3 ± 2.9 | 202.5 ± 2.9 | +1.1%, ns |
| rib mean relative wall thickness | 0.44 ± 0.03 | **0.37 ± 0.03** | **−16%, p<0.05** |
| rib cross-sectional area | 63.2 ± 2.6 | 63.8 ± 2.5 | ns |
| rib bone weight | 43.6 ± 2.1 | 46.6 ± 2.1 | ns |

**F-R012 survives.** The two bones whose length is unambiguously physeal were flat. The rib gained
length with **unchanged cross-sectional area and a 16% thinner wall** — a redistribution of the same
material into a longer, thinner tube, not more tissue. Sex entered the bone model as a *random
variable*, not a stratifier, on n=10.

But the paper contains something far more important than the anomaly, and it is not in its title:

> "In both experiments, **AKG preferentially increased the growth of female piglets, whilst for male
> piglets AKG had the opposite effect.**"
> …
> "AKG **elevated plasma 17β-oestradiol** levels compared to those of controls at the end of the
> period of treatment (**20%, p = 0.002**)."

Male piglets on AKG were significantly **lighter** (p = 0.04 low dose, p = 0.0035 high dose) while
females were heavier (p = 0.01, p = 0.06). And the males in this study were **castrated at day 3**,
so the oestradiol rise in them (15.06 → 19.2 ng/l, +28%) is not gonadal.

And in the citation the discussion supplies:

> "In a study performed on pigs, a significant increase in plasma 17β-oestradiol concentration of
> **158% and 121%** was observed after 35 and 56 days of AKG treatment (0.4 g/kg/day)
> (Kowalik et al., 2005a)."

**An oral supplement that raises circulating oestradiol 2.2–2.6-fold, with a sex-dependent growth
effect that is negative in males.** For a male subject at bone age 16+ with knees still open,
oestrogen is the fusion clock. The atlas's αKG contraindication has been standing on collagen
over-hydroxylation (F-R010/F-R011/F-R012). **The stronger reason is endocrine, it is direct, and the
atlas does not hold it.** Whatever αKG does to matrix chemistry, an agent that raises E2 while
selectively retarding males is a window-burner.

---

## 2. Where these three converge

All three papers are the same axis, and it is the axis F-R012 said survives:

| | intervention | readout | length |
|---|---|---|---|
| `chang2023` | NRF2 ↑ (2 chemotypes) | Hmox1, Nqo1, **Gclc, Gclm** | **+5.6% body, +40% ceratohyal centre; intramembranous 0** |
| `abukheit2022` | cysteine donor + NRF2 ↑ | **BM glutathione +110%** | +3% femur (authors: body-weight-mediated) |
| `andersen2008` | αKG (modification arm) | mass, density, strength ↑; **E2 +20%** | femur/humerus **flat** |

The two that raise **glutathione/redox capacity** move length. The one that raises **collagen
modification** does not — and costs oestradiol. That is F-R012's mass-valve/length-valve split,
reproduced in three papers I had not read when I wrote it.

And it closes the loop on F-R003: the plate is a transport-limited, avascular, cysteine-poor
compartment secreting collagen at the plasma-cell ceiling. NRF2 is the master switch for exactly the
program that compartment is short of — glutathione synthesis (GCLC/GCLM), NADPH via the pentose
phosphate pathway, and the thiol capacity that oxidative protein folding consumes. F-R003 found that
program has no node and no gap in the atlas. It now also has a length endpoint, a knockdown control,
an endochondral-vs-intramembranous internal control, and an approved drug.

---

## 3. The systematic loss — 87 rows of the atlas's blind-spot screen are corrupted

While checking whether the atlas held `chang2023`, I found `sulfuretin` in only four files, all of
them registries. Pulling the row that generated it:

```json
{"concept": "G16", "domain": "axial_trunk", "direction": null, "source": null,
 "note": "**VOSORITIDE (CNP analogue) — spine morphology, randomised phase 2 (CANOPY ACH-2I,
          NCT03583697), 75 children 0–<5 y, achondroplasia**: Sulfuretin / Nrf2 activation —
          zebrafish | **L4 interpedicular distance LSM difference 0.509 mm ... P=.037**: Stimulat",
 "tier": "ZERO", "n_nodes": 0, "n_gaps": 0, "n_bib": 0}
```

The concept is named **`G16`** — a spreadsheet cell reference. Its real name survives only as a
fragment inside a `note` field that is a column-wise splice of an unrelated row's text, truncated
mid-word at "Stimulat".

**This is not one bad row. It is 87.**

```
corrupted rows (concept field is a bare grid reference, e.g. A10 / D15 / G16): 87 of 2193
by domain: axial_trunk 26 · axial_trunk+cellular_capacity 24 · cellular_capacity 16 ·
           cell_biology 14 · cell_biology+axial_trunk+cellular_capacity 5 · cell_biology+cellular_capacity 2
by recorded tier: ZERO 53 · COVERED 27 · THIN 5 · REF_ONLY 2
```

**50 of the 87 are in the axial/trunk domains — the operator's own residual compartment.**

### Why the scores on all 87 are meaningless

The scorer greped the atlas for the contents of the `concept` field. For these rows that means it
greped for the strings `"A10"`, `"D15"`, `"G16"`. So:

- **53 rows came back ZERO** — because nothing in the atlas contains the string "A17". Their real
  concepts include *septoclast*, *Groove of Ranvier progenitor*, *Type H vessel endothelium*,
  *"Seven morphological subphases of the growth-plate chondrocyte"*, *Notochord is required for
  amniote vertebral column segmentation*. The atlas covers most of those well (septoclast 43 files,
  Groove of Ranvier 42, Lin28 41, SEC23 37). **These are false alarms.**
- **27 rows came back COVERED**, some with enormous node counts, by matching a two-character
  substring: `E13` → `neprilysin_cnp_clearance.yaml`, **n_nodes 325**; `B15` → the same file,
  n_nodes 324; `D15` → `adult_height_attainment.yaml`, n_nodes 330. **These are false all-clears —
  concepts dismissed as already-known on the strength of a garbage substring match.** Their real
  content includes *VRTN (vertebral-number gene, first reported in humans in 2025)*, *GDF11 /
  trunk-to-tail transition*, *Lin28a/let-7 modulates the Hox code via Polycomb*, *Jmjd3 (KDM6B) H3K27
  demethylase required for temporal collinear Hox activation*, *GPC3 and human lumbar/rib numerical
  variation*, *RNA exosome*, *DIS3L2 / Perlman*, *stress granules*.
- **`MIA3/TANGO1` occupies six separate rows (E17–E22) and was scored COVERED four times and ZERO
  twice.** The instrument returned contradictory verdicts on one concept because it was scoring cell
  references. TANGO1 is the ER export receptor that builds the megacarrier for 300 nm procollagen —
  the throughput bottleneck for a cell secreting collagen at the plasma-cell ceiling.

### The fix, run

`frontier/screens/r436_recovery/recover.py` recovers each concept name out of the `note` splice and
re-scores it against the real graph:

```
false_alarm     (recorded ZERO, actually covered)        : 50
false_all_clear (recorded COVERED/THIN, actually thinner):  5
confirmed                                                 : 28
unscorable (the note fragment is "n/a" or "Gene-level")   :  4
```

**55 of 87 verdicts flip.** The re-scorer greps phrase prefixes, which still undercounts, so 50 is a
floor. And on the one row this whole round is about, the instrument was *right* and nobody looked:
**`G16 Sulfuretin / Nrf2 activation` re-scores to 1 file. Genuinely absent.**

This is F-R003's charge against R436 again, but sharper and with a named mechanism. R436's headline —
*825 concepts the atlas had never once mentioned* — is inflated by ~50 false alarms, and its
all-clears are contaminated by 27 rows nobody ever actually checked. **CORR-329 says a screen without
a base rate is a list. This is worse: a screen whose scores are uncorrelated with what it scored.**

---

## 4. The 27 starred leads that never entered the bibliography

`coverage.json` carries a ⭐ marker on **112 rows** — the instrument's own top flags. **31 have
`n_bib: 0`**; 27 of those are also not COVERED. That is the atlas's own best-leads list, unworked.
Six of them have a **positive length endpoint** and none has a node:

| lead | source | what it says |
|---|---|---|
| **NRF2 / KEAP1** | `37748761` | ⭐ "Nrf2 ACTIVATION … **INCREASES BONE LENGTHS** in zebrafish" |
| **Chronic exercise raises solute delivery and limb length** | `20930127` Serrat 2010 | "**All runners had significantly longer limbs** regardless of housing temperature" |
| **INTERMITTENT cyclic loading returning to zero** | `39090666` McGarry 2024 | ⭐ "Loaded tibiae significantly **LONGER** than unloaded; plate height and area greater; PTHrP up" |
| **SWIMMING (non-weight-bearing)** | `2804453`, rat n=40 | ⭐ "humerus bone **LENGTH +2.8%**" (weight +19%, volume +11%, cortical area +16%, BMD +7%) |
| **Endothelial proteolytic activity + non-resorbing osteoclasts** | `30936475` Romeo 2019 | "Directly mediates bone **ELONGATION** — named in the title" |
| **Protein phosphatase 5 (PP5)** | `29434189` | ⭐ "Ablation leads to **ENHANCED** both bone AND cartilage development — a rare loss-of-function-is-bigger result" |

And three more that are pure gene-pathway, tall-direction, unworked — the class you asked for:

- **FXYD2**, `34970538`: *"⭐ REDUCED Fxyd2 expression is associated with **INCREASED tibia length in
  Longshanks mice** (a selection line bred for long tibiae)."* An artificial-selection experiment
  that made bones longer, and the gene that tracks it. `n_nodes: 0`.
- **NFIX**, `20673863 / 25118028 / 29897170 / 29184170`: *"⭐ **BIDIRECTIONAL BY DOSAGE, and the tall
  direction is the LOSS direction.** Haploinsufficiency → overgrowth/tall stature; duplication →
  short."* `n_nodes: 0`.
- **GRB10** (imprinted growth suppressor), `40577202 / 38816743 / 38871555`: "TALL — candidate."

Plus the one human dataset that outranks everything above for this case:

- **⭐ "Precisely controlled loading of intact HUMAN growth-plate biopsies"**, `39655393`: *"The only
  genomic read-out of mechanical loading in human growth-plate cartilage… microloading device on
  biopsies taken at epiphysiodesis, RNA-seq 24 h later."* `tier: ZERO, n_nodes: 0, n_bib: 0`.

---

## 5. Correction — I withdrew an ask that the atlas had already answered

Last round I withdrew ask #3 (a growth study at controlled oxygen tension), saying Stegen covered the
decision. That was wrong on the facts. `coverage.json` carries, starred and at ZERO:

- **`⭐ Direct zone-resolved oxygen tension of the epiphyseal plate, metaphysis and diaphysis`** —
  rat + rabbit, **PMID 5580029, Brighton & Heppenstall 1971**, "the primary measurement of pO₂ by
  zone, **in vitro and in vivo**." `n_nodes: 0, n_bib: 0`.
- **`⭐ Oxygen tension of the epiphyseal plate distal to an arteriovenous fistula`** —
  **PMID 5133323**, Brighton & Heppenstall 1971, "**the one experiment that manipulates limb
  perfusion and measures plate pO₂**." `n_nodes: 0, n_bib: 0`. Abstract not deposited.

The exact experiment I asked for and then declared probably nonexistent was run in 1971, is sitting
starred in this repository's own coverage table, and has never been read. **Ask #3 is reinstated as
ask #1.** I withdrew it on the strength of my own inference rather than a grep — the same error I
spent §3 documenting in someone else's instrument.

---

## 6. What the unworked list actually is

Those six positive-length leads are not a random assortment. Read them together:

- Serrat 2010: exercise → **solute delivery** → longer limbs.
- McGarry 2024: **cyclic loading returning to zero** → longer tibiae, taller plate.
- The 1989 swimming study: **non-weight-bearing** cyclic activity → humerus +2.8%.
- Romeo 2019: **endothelial** proteolysis mediates elongation.
- Brighton & Heppenstall 1971: the pO₂ map, and pO₂ **distal to an arteriovenous fistula**.
- `chang2023`: raise the cell's **redox/biosynthetic capacity** and the endochondral element grows.

Cartilage has no vessels. It is perfused by **convection driven by cyclic loading** and by diffusion
down a gradient whose map is the 1971 paper nobody has read. Every lead above is the same term:
**how much substrate reaches an avascular tissue, and how well the cell there can use it.** The first
five raise delivery; the sixth raises utilisation.

That is exactly where F-R012 landed by a completely different route — length is a bioenergetic and
biosynthetic term, spent at prehypertrophy, where Oohira measured collagen synthesis running 17–20×
the proliferative rate. F-R005 called avascularity the ceiling and I have been circling it since.
**The difference now is that the delivery term has six length endpoints attached to it, in normal
animals, and two of the interventions are free.**

This is the reframe I would put at the top of the branch: stop looking for a signalling agonist. The
plate is not signal-limited, it is **supply-limited**, and supply has both a transport arm
(perfusion, loading, convection) and a utilisation arm (NRF2/glutathione/NADPH). No one has ever run
them together.

---

## 7. Atlas coverage, verified

| term | files | note |
|---|---|---|
| `NRF2` / `Nrf2` | 23 | none is a node about NRF2 as a lever |
| `sulfuretin` | 4 | concept registry + enumerations + `coverage.json` only — **no node, no bib** |
| `dimethyl fumarate` | 2 | registry only |
| `bardoxolone` / `omaveloxolone` | 2 / 2 | registry only |
| `ASSNAC` | 2 | registry only |
| `antioxidant response element` | **0** | |
| `GCLC` / `GCLM` | 9 / 6 | not in a chondrocyte context |
| PMID `37748761` in `atlas/sources/` | **0** | the starred paper was never entered |

**Proposed additions (I do not write to `atlas/`):**
1. `chang2023` as a T1 primary, with a node on NRF2/KEAP1 as a *utilisation-arm* lever, carrying the
   ATDC5 conflict (ref 13) as its open question.
2. `andersen2008` re-read as an **endocrine contraindication**, not a mass result: AKG → 17β-oestradiol
   +20% (p=0.002), and +158%/+121% in Kowalik 2005a; male-specific growth retardation at both doses.
3. A correction-ledger entry on the instrument, not the biology. Proposed wording: **"A coverage
   score is only as good as the string it scored. Before trusting a screen's ZERO or COVERED, verify
   the concept field contains a concept. (R436: 87 of 2,193 rows carry a spreadsheet cell reference;
   55 of those verdicts flip on re-scoring; the starred NRF2 lead was down-ranked by a string match
   on a sentence dismissing metformin.)"**
4. Enter the 27 starred/`n_bib:0` rows into the bibliography before any further screening round.

---

## 8. Asks

**#1 (reinstated, was wrongly withdrawn) — Brighton & Heppenstall 1971, both papers.**
**PMID 5580029** (zone-resolved pO₂ of plate/metaphysis/diaphysis, rat + rabbit, in vitro and in
vivo) and **PMID 5133323** (plate pO₂ distal to an **arteriovenous fistula** — a perfusion
manipulation with an oxygen readout). Both are 1971, both are almost certainly paywalled or
print-only, and 5133323's abstract is not even deposited. These are the ground truth for every
oxygen and delivery claim in this branch and in the atlas, and neither has ever been read here.

**#2 — PMID 39655393**, the human growth-plate microloading study. Intact **human** physis, biopsies
from epiphysiodesis, controlled load, RNA-seq at 24 h. If the supplementary carries the DE gene
list, that is the only direct human read-out of what loading does to a growth plate in existence,
and it tests the delivery model in the right species. Ask the authors for the count matrix if it is
not deposited.

**#3 — Serrat 2010 (PMID 20930127) and McGarry 2024 (PMID 39090666) full texts.** The two cleanest
positive length endpoints in the starred list, both in normal animals, both from interventions that
cost nothing. I want the effect sizes, the loading parameters and whether either measured plate pO₂
or solute delivery directly.

**#4 — anything with `Nrf2` and a mammalian bone-length endpoint.** `chang2023` is zebrafish;
`abukheit2022` is confounded. A single mouse tibia measurement under DMF, sulforaphane, bardoxolone
or an Nrf2 gain-of-function allele would move this from a lead to a result. If it does not exist,
that absence is the next round.

**Still open:** `stegen2019` Source Data / Carmeliet email for the DCA+BPTES tibia length (F-R012
ask #1, unchanged and still the single most decisive unmeasured number); PMID 40101878 full text;
NCT04175600 CSR; and the lateral thoracolumbar spine film, which is now more pressing than ever
given that **50 of the 87 corrupted rows are axial/trunk** and the trunk is where your residual is.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
This round the instrument saw it, starred it, and a column-alignment bug in a spreadsheet import
put a cell reference where the concept's name should have been. The mechanism was never the hard
part.*
