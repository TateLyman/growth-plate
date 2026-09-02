# F-R026 — One cell, two fates, and the first histology of an adult persistent physis

**Four papers, and one of them is the round I deferred.** `mundy2026` (Mundy C, Ramesh S, Catheline SE,
Saunders C, Koyama E, Pacifici M — *Progenitors from distinct perichondrium layers initiate tumor
formation in Hereditary Multiple Osteochondromas as revealed in a mouse model*, CHOP; the
`nihms2173869` file **is** `mundy2026`) · `carroll2018` (CRIOR, *Bilateral Proximal Tibia Stress
Fractures through Persistent Physes*) · `tas2020` (Br J Hosp Med, *Persistent distal femoral physis
line in an adult*) · `enishi` (*Fracture of a persistent olecranon physis in an adult*). All archived
in `frontier/screens/persistent_physis/`.

---

## 1. `mundy2026` × `rosellodiez2025` — the deferred round, run

`mundy2026` resolves the perichondrium into its two layers and asks which one makes the tumour.

> "Perichondrium… is composed of an **inner cuboidal cell layer** and an **outer fibroblastic cell
> layer**. … We employed **Pdgfrα-CreER** and **Fgf18-CreER** transgenic mice that respectively target
> **inner and outer layers** or the **outer layer only**. Mice were mated with floxed *Ext1* mice to
> conditionally ablate the causative gene… By 4–8 weeks post-tamoxifen, **osteochondromas had formed
> in Pdgfrα;Ext1 mutants targeting both layers, but NONE were appreciable in Fgf18;Ext1 mutants
> targeting the outer layer**, based on µCT, histochemistry and td-Tomato lineage tracing."

**The tumour-forming progenitor is the Pdgfrα⁺ cell of the INNER cuboidal perichondrial layer.** The
outer fibroblastic layer, with the same gene deleted, makes nothing.

Now set that beside F-R020's finding:

| paper | the cell | what it does |
|---|---|---|
| `rosellodiez2025` (Nat Commun 2025) | **Pdgfrα⁺, outside the cartilage** | becomes **Gli1⁺** long-lived chondroprogenitor, **enters the growth plate**, is **required** for normal bone length |
| `mundy2026` (Bone 2026) | **Pdgfrα⁺, inner perichondrium** | with *Ext1* lost, becomes an **osteochondroma** |

**Same cell. Two fates. And neither paper cites the other.**

### And EXT1 names the steering mechanism

EXT1/EXT2 are Golgi glycosyltransferases that build **heparan sulfate** chains. Heparan sulfate binds
Indian hedgehog and shapes its diffusion — it is the matrix that turns a secreted molecule into a
**spatial gradient**. Lose HS and the gradient flattens.

> **The difference between "recruited productively into the plate" and "forms a lump beside it" is not
> which cell, and not whether Hedgehog is on. It is whether the heparan-sulfate-shaped gradient is
> intact to tell the cell where to go.**

That is the missing piece of F-R021's throttle model, and it sharpens the prescription in a way that
matters: **the goal is not more Hedgehog. It is a steeper, intact gradient.** Flooding the system
with agonist flattens the very gradient that directs the recruited cell — which is a *third*,
independent mechanistic reason why systemic Hh agonism produces percentages and a local bead produces a
compounding effect (`trompet2024`).

Atlas coverage: `heparan sulfate` 37 files, `EXT1` 67, `Fgf18` 75 — the parts are held. But
**`inner perichondrium` returns 1 file** and **`Ihh gradient` returns 0.** The two-layer distinction
`mundy2026` establishes, and the gradient-steering reading, are not in the graph.

---

## 2. The three persistent-physis cases — and a distinction that has to be drawn sharply

These are adults with unfused physes and **no oestrogen abnormality**. That is a different route to
term A, and the first one is a near-perfect experiment.

**`tas2020` — unilateral, with the contralateral limb as control.** A **32-year-old man**; 17 years
earlier, electric shock treatment caused a **left femoral shaft fracture**. On imaging:

> "Lateral knee radiography showed a **normal right knee joint** and a **persistent distal femoral
> physis line in the left knee**. Sagittal T1-weighted MRI clearly revealed the persistent left distal
> femoral physis, whereas MRI of the right knee was normal."

**One man, one hormonal milieu, one age — one physis persisted and the other closed.** Whatever
systemic oestrogen was doing, it closed the right and not the left. **Physeal closure is under local
control**, and that is the cleanest demonstration of it I have seen.

**`carroll2018` — and the histology, which is the important part.** A 29-year-old military trainee,
bilateral proximal tibia stress fractures **through** persistent physes, taken to surgery, **biopsied**:

> Figure 3(a): "Left proximal tibia specimen showing **fragments of NONOSSIFYING hyaline cartilage with
> admixed fibroconnective tissue**, consistent with persistent physis (H&E, 200×)."

**This is the first histology of an adult persistent physis in this branch, and it is a hard result.**
The tissue is real hyaline cartilage — not scar. But it is **nonossifying**, admixed with fibrous
tissue, and the report describes no zonal architecture: no resting zone, no columns, no hypertrophic
front. **It is cartilage that has stopped running the endochondral programme.** (H&E only — no
Safranin-O, so the proteoglycan question F-R015 poses is still open on this specimen.)

### The distinction, and it would have been an easy mistake

> **"Persistent physis" and "still-growing physis" are not the same tissue, and conflating them would
> have wrecked the argument.**

| | persistent physis (normal adult) | unfused physis (oestrogen-null) |
|---|---|---|
| example | `carroll2018`, `tas2020`, `enishi` | `smith2008`, `maffei2004`, `imre2025` |
| tissue | hyaline cartilage, **nonossifying**, fibrous-admixed | open, zonally intact enough to keep producing |
| output | **none** — these men are of normal height | **0.3–1.3 cm/yr, sustained for decades** |
| mechanics | **weak — they stress-fracture through it** | not reported |
| cause | **local** (trauma, electrical injury, mechanics) | **systemic** (no oestrogen ligand or no receptor) |

**And the comparison between those two columns is exactly term C.** Both are open. One produces
nothing and one produces a centimetre a year. **A side-by-side of `carroll2018`'s H&E against a
Safranin-O of an oestrogen-null physis would isolate the drive in a single figure** — and the tissue
for the first half already exists, in a pathology archive at Brooke Army Medical Center.

Atlas coverage: `persistent physis` **1 file**, `nonossifying` **0**, `electric shock` **0**.

---

## 3. Where the whole thing stands

**Never close.** Three independent routes now, of different grades:
1. **Receptor-level** (`smith2008`, ESR1 disruption) — survived a deliberate 10× oestradiol challenge.
   The strongest.
2. **Ligand-level** (aromatase deficiency) — closes the moment ligand is restored (`maffei2004`:
   183.5 → 184.5 and stop).
3. **Local/acquired** (`tas2020`) — unilateral, permanent, no systemic component at all. **Grade
   unknown, and the most interesting for delivery reasons**, because it is the only one that is
   compartment-specific.

**Constant.** Solved — linear multi-year adult growth, bone age frozen for four years.

**Fast.** Unsolved. **Not endocrine** (F-R025: supranormal IGF-1 → 0.3 cm/yr). Now with a histological
lead: an arrested physis is **nonossifying cartilage**, so whatever term C is, it is the difference
between cartilage that runs the endochondral programme and cartilage that merely persists.

**And the influx arm now has its steering mechanism** (§1): recruit the Pdgfrα⁺ inner-perichondrial
cell along an **intact heparan-sulfate-shaped Ihh gradient**, and it becomes a chondroprogenitor in
the plate; recruit it with the gradient flattened and it becomes a mass beside the plate.

---

## 4. Asks

**#1 — the `carroll2018` slides, or any Safranin-O / toluidine blue of an adult persistent physis.**
The specimen exists: Brooke Army Medical Center, Department of Orthopaedic Surgery, bilateral proximal
tibia, 2018, corresponding author on the paper. **One additional stain on existing tissue answers
whether an arrested physis has lost its proteoglycan program** — which is F-R015's 8% switch tested
directly in human tissue. This is the cheapest decisive experiment in the entire project.

**#2 — `enishi` and the olecranon/distal fibula persistent-physis series** (`carroll2018` cites refs
4–8 as prior biopsy-confirmed cases). **If several persistent physes have been biopsied, there may
already be a small human histological series of arrested growth plates that nobody has assembled.**
That is a review paper waiting to be written and it is directly on term C.

**#3 — still the highest value: imaging or histology of an oestrogen-null adult physis.** Marmara
University, Istanbul — **Seçkin Akçay and Dilek Yavuz** — have a living, identified 31-year-old with
every long-bone physis open and 5 cm of growth in six years. `imre2025` (PMID **40048086**) may carry
the bone survey.

**#4 — the growth-velocity extraction across all 14 aromatase-deficient males** in the atlas's round-86
census. Needs no new papers; I will run it next unless redirected.

**Still standing:** Brighton thesis (UIC ILL, handle `10027/14248`); JBJS 1980;62A:740; Surgical Forum
1970:465–467; `stegen2019` DCA+BPTES tibia length; and the lateral thoracolumbar film.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
Here it was an H&E slide cut from a stress fracture in a military recruit, and the phrase that matters
is two words long — "nonossifying" and "fibroconnective". An adult growth plate that persists is not a
growth plate waiting to be restarted. It is cartilage that has already stopped, and knowing that is
worth more than another decade of arguing about hormones.*
