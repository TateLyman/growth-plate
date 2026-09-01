# F-R015 — The 8% switch, and a correction to my own last round

**Retrieval outcome:** I could not get the full text of `brighton1969` (Brighton CT, Ray RD, Soble LW,
Kuettner KE, *In vitro epiphyseal-plate growth in various oxygen tensions*, J Bone Joint Surg Am
1969;51(7):1383–1396, **PMID 4186275**, DOI 10.2106/00004623-196951070-00018). What I did get,
methodically, is in §1 — including its **abstract**, its **opening paragraph**, and the fact that a
**thesis version by Brighton exists**. Combined with a 2014 paper nobody in this branch had seen, it
is enough to correct F-R014 and to state a mechanism.

---

## 0. The correction, first

F-R014's headline was **"the sign of oxygen is negative."** That is too simple, and `brighton1969`'s
own abstract — which I had not read when I wrote it, having only Brighton's 1971 paraphrase of it —
says so:

> "**The cartilage portion of the epiphyseal plate exhibited maximum growth in 21 per cent oxygen,
> while maximum metaphyseal bone formation occurred in 5 per cent oxygen.** … in higher oxygen
> tensions, the cartilage portion of the plate showed narrowing, a progressive loss of acid
> mucopolysaccharide stainability, **eventual loss of the zone of hypertrophic cells**, and an
> accumulation of neutral mucopolysaccharide or glycomucoprotein at its base."

In 1971 Brighton paraphrased his own 1969 experiment as *"when less oxygen was supplied to epiphyseal
plate explants, there was greater bone formation, and when more oxygen was supplied, there was less
bone formation."* That is true — of **bone formation**. He did not mention that his cartilage
endpoint peaked at 21%. I inherited the selective half and built a monotonic claim on it.

**There is no single sign. There is a threshold, and the growth plate lives below it.**

---

## 1. What retrieval actually produced

I ran every channel available. In order:

| channel | outcome |
|---|---|
| Europe PMC | located it: PMID **4186275**, JBJS Am 1969;51(7):**1383–1396** — a 14-page full paper |
| Crossref | DOI 10.2106/00004623-196951070-00018, plus three sibling Brighton papers (§4) |
| OpenAlex / Unpaywall | flagged **green OA**, `any_repository_has_fulltext: true` |
| **Figshare** (the OA target) | **a thesis by CARL THEODORE BRIGHTON of the same title — but `files: []` and license "In Copyright."** OpenAlex and Unpaywall both report this as CC-BY full text. **They are wrong**; it is a ProQuest dissertation stub with no file attached. |
| **Semantic Scholar** | returned the paper's **opening paragraph** (OCR-degraded) — §2 |
| NCBI E-utilities | confirmed pagination; **no abstract deposited** for 4186275, 5383117, 5580029 or 5133323 |
| journals.lww.com | **HTTP 402 Payment Required** |
| ovid.com | HTTP 402 |
| PubMed via WebFetch | cookie wall |
| CORE | HTTP 429 |
| web search ×2 | **recovered the abstract**, independently and consistently, quoted above |
| OA citing papers (79 citations) | surfaced the 2014 threshold paper in §3 |

**Two things worth your time exist and I could not reach:**
1. **Brighton's thesis**, same title, on Figshare with no file. It is a ProQuest dissertation — almost
   certainly University of Pennsylvania or Chicago, and a thesis version of a 14-page paper is
   typically 100+ pages with every plate and every raw table. **A university library ILL request, or
   ProQuest Dissertations & Theses, would get it.** This is the single best target.
2. **PMID 5383117 — Brighton CT et al., "The site of action of oxygen toxicity during in vitro
   epiphyseal plate growth," Surgical Forum 1970:465–467.** A follow-up that asks exactly the
   question the 1969 abstract leaves open: *where* in the plate does high oxygen do its damage.
   Surgical Forum is an American College of Surgeons proceedings volume — library-only, not online.

I did not attempt to obtain paywalled text through illegitimate channels and won't.

---

## 2. The opening paragraph, recovered

Worth having verbatim, because it is a 130-year-old statement of the exact confusion this branch has
been in (OCR artefacts left as-is):

> "The relationship between oxygen tension and the formation and resorption of bone and cartilage has
> been a subject of interest for many years. In the present era of hyperbaric oxygen therapy, where
> increased oxygen tension reputedly favors fracture healing as well as bone resorption, we are in
> much the same quandary as Spencer, in 1896, when he complained: **'Something is evidently wanting
> to the explanation when one and the same result, atrophy, is attributed both to an increased
> vascularity and a diminished vascularity, when an increased vascularity can be said to promote both
> bone formation as well as absorption.'** Our interest centered on the epiphyseal plate where bone
> and cartilage formation and resorption occur more or less simultaneously. … **The results indicate
> that the epiphyseal plate is extremely sensitive to the prevailing oxygen tension.**"

Spencer's complaint is F-R014's error, written in 1896. "More perfusion" is not a direction until you
say what is being delivered and to which process.

---

## 3. The keystone — a threshold at pO₂ ≈ 8%, and it is a *matrix-program* switch

Following the OA citing literature out of `brighton1969` produced a paper no round of this branch or
of the atlas has held:

**Li S, Oreffo ROC, Sengers BG, Tare RS. *The effect of oxygen tension on human articular chondrocyte
matrix synthesis: integration of experimental and computational approaches.* Biotechnol Bioeng
2014;111(9):1876–1885.** Human articular chondrocytes, scaffold-free 3D pellets at seeding densities
from 6×10⁴ to 1×10⁶ cells, so the pellets generate their own internal oxygen gradients; the gradient
was then modelled and the position of the collagenous band extrapolated against it.

> Threshold: **1.075 (± 0.364) × 10⁻⁷ mol cm⁻³, equivalent to pO₂ ≈ 8% of atmospheric pressure.**
> **Below** the threshold: *"oxygen tension below this level enhanced PG [proteoglycan] deposition."*
> **Above** the threshold: *"oxygen tensions above the threshold level were observed to favor
> collagenous matrix production."*

**Oxygen does not set how much matrix a chondrocyte makes. It sets which matrix.**

### And now put Brighton's 1971 in vivo map against that number

| compartment | measured pO₂ (`brighton1971b`, Table I, control side) | vs the 8% switch |
|---|---|---|
| secondary epiphysis | 115.5 mmHg = **15.2%** | **above** |
| **zone of cell columns** | 45.6–53.2 mmHg = **6.0–7.0%** | **below** |
| **zone of hypertrophic cells** | 16.0–16.7 mmHg = **2.1–2.2%** | **far below** |
| metaphysis | 11.4–47.1 mmHg = 1.5–6.2% | below |
| diaphysis | 106.4–115.5 mmHg = **14.0–15.2%** | **above** |

**The growth plate is the only compartment in the bone that sits below the switch, and the bone on
both sides of it sits above.** The plate is a proteoglycan-program slot cut into collagen-program
tissue, and the boundary of the slot is the 8% isopleth.

That is not a coincidence to be admired. It is a **set point**, and set points are the things you can
move.

---

## 4. The mechanism this assembles, and every paper in the branch falling into place

Proteoglycan is not decoration. Aggrecan's sulfated glycosaminoglycan chains carry the matrix's
**fixed charge density**; fixed charge draws counter-ions and therefore water; the resulting
**swelling pressure** is the mechanical work that separates the epiphysis from the metaphysis. The
atlas already owns this half — `round448_the_matrix_outpressures_the_cell_by_710_fold.yaml`: *"osmotic
pressure makes the force,"* *"swelling pressure of a charged matrix."* And terminal chondrocyte
hypertrophy — CORR-361's **44–59% of all elongation** — is overwhelmingly volumetric water uptake,
not dry mass.

So:

> **pO₂ < 8% → proteoglycan program → fixed charge → osmotic swelling → hypertrophy → ELONGATION.
> pO₂ > 8% → collagen program → matrix stiffens, GAG lost → the hypertrophic zone disappears → no
> elongation.**

Six results in this branch, previously in tension, now read as one statement:

1. **`brighton1969`**: at high O₂, *"progressive loss of acid mucopolysaccharide stainability"* — AMPS
   **is** proteoglycan — and *"eventual loss of the zone of hypertrophic cells."* The >8% arm,
   observed histologically in 1969, exactly as the 2014 model predicts.
2. **`brighton1971b`**: the A-V fistula drives cell columns from 6.0–7.0% down to **3.1–4.0%** and
   hypertrophic cells from 2.1% to **1.0–1.2%** — deeper into the proteoglycan regime — and the limb
   lengthens in **100% of puppies**.
3. **`stegen2019`**: PHD2-null chondrocytes consumed *less* oxygen, *"making centrally localized
   chondrocytes **less hypoxic**"* — pushed **toward** the switch — and their matrix went
   **collagen**: P4HA1/2, P3H1, PLOD1/2, LOX all up, hydroxyproline up, pyridinoline up,
   MMP-resistant, denser, and the tibia **shorter at p = 1×10⁻⁸**. The >8% arm run genetically.
4. **`duncan1996` (Farquharson)**: pyridinoline cross-links are **~10-fold higher in the proliferative
   zone than the hypertrophic zone.** Of course they are. The proliferative zone sits at 6–7%, near
   the switch; the hypertrophic zone at 2.1%, far below it. **The 10-fold cross-link gradient is the
   plate descending through the oxygen gradient and handing off from the collagen program to the
   proteoglycan program.** F-R012 read that gradient as de-cross-linking for discharge; it is more
   simply a program switch, and Oohira's finding that hydroxylation of *newly made* collagen is
   constant by zone fits the program reading, not the modification reading.
5. **`serrat2010`**: exercise raised solute delivery **1.5×** and lengthened four bones, locally.
   Substrate for a program that is running, not a change of program.
6. **F-R003**: the plate is transport-limited and looks like a cysteine auxotroph, with the full
   glutathione machinery present. NADPH and the pentose phosphate pathway serve **both** the
   reductive defence and the UDP-sugar supply for GAG synthesis. The utilisation arm feeds the
   proteoglycan program specifically.

### What this makes the target

Not "oxygenate the plate." Not "perfuse the plate." Precisely:

> **Hold the plate below 8% pO₂ while flooding it with the substrates of sulfated proteoglycan
> synthesis.**

Those substrates are nameable and checkable: **glucose** (→ UDP-glucuronate and, via the hexosamine
pathway, UDP-GalNAc), **sulfate** (→ PAPS via PAPSS2, imported by SLC26A2), and the **NADPH** the
pentose phosphate pathway supplies. The atlas holds each of these as *disease genes* — SLC26A2 in 61
files, PAPSS2 in 38, sulfate in 165 — and holds the osmotic engine in R448. **`hexosamine` returns 7
files, `UDP-glucuronate` returns 0, and `threshold oxygen` returns 0.** It has the parts. It has
never had the wiring diagram, because its oxygen node and its osmotic node have never been connected.

---

## 5. What I am not claiming

- **I have not read `brighton1969`.** I have its abstract (twice, independently), its opening
  paragraph, and its pagination. **What "cartilage growth" was measured — plate width, explant
  length, ³⁵S incorporation, wet mass — is unknown to me**, and it matters: a *wider* cartilage with
  *less* metaphyseal bone formation at 21% is equally consistent with genuine cartilage growth and
  with retained, unconverted cartilage. The abstract's own *"eventual loss of the zone of hypertrophic
  cells"* argues against calling the 21% condition growth in any sense that lengthens a bone, but that
  is my inference, not their measurement.
- **The 8% threshold is from human *articular* chondrocytes in pellet culture, not growth plate.**
  Articular and physeal chondrocytes are different cells in different mechanical worlds. That the
  number lands precisely between Brighton's plate (2–7%) and Brighton's surrounding bone (14–15%) is
  striking, and it is not proof.
- **Direction of causality in `brighton1971b` remains open** — the authors say so themselves.
- The chain proteoglycan → fixed charge → swelling → elongation is textbook cartilage mechanics and
  the atlas's own R448, but **no experiment in this branch has manipulated pO₂ and measured GAG and
  length in the same growth plate.** That experiment does not appear to exist. It is small.

---

## 6. Asks

**#1 — Brighton's thesis, *"IN VITRO EPIPHYSEAL PLATE GROWTH IN VARIOUS OXYGEN TENSIONS"*, Carl
Theodore Brighton.** Indexed on Figshare (`figshare.com/articles/thesis/…/10911983`) with **no file
attached**; it is a ProQuest Dissertations & Theses record. A university library ILL, a ProQuest
subscription, or an email to the University of Pennsylvania orthopaedics department would get it, and
a thesis carries every raw table the 14-page paper compressed. **This is the highest-value document
in the branch.** The specific numbers I need from it: the oxygen tensions tested, what "cartilage
growth" was measured as, and the growth-vs-pO₂ curve with its shape.

**#2 — PMID 5383117**, Brighton et al., *"The site of action of oxygen toxicity during in vitro
epiphyseal plate growth,"* **Surgical Forum 1970:465–467.** Library-only. It asks where in the plate
high oxygen acts, which is the mechanism question §3 raises.

**#3 — two more Brighton papers Crossref surfaced that nobody has looked at, both closed:**
- **JBJS 1980;62(5):336–353, DOI 10.2106/00004623-198062050-00007 — *"Diffusion in the various zones
  of the normal and the rachitic growth plate."*** Zone-resolved **diffusion coefficients**. This is
  the transport term of F-R013/F-R014 measured directly, with a disease control.
- **JBJS 1983;65(5):1134–1143, DOI 10.2106/00004623-198365050-00012 — *"Absence of the glycerol
  phosphate shuttle in the various zones of the growth plate."*** The glycerol-phosphate shuttle is
  how a cell reoxidises cytosolic NADH aerobically. **Its absence would mean the plate physically
  cannot run oxidative metabolism on glycolytic NADH and must regenerate NAD⁺ by lactate** — a
  structural proof of obligate glycolysis, and the mechanistic floor under everything in §3–§4.
  Both are unpaywalled nowhere; both are one ILL request each.

**#4 — the experiment that does not exist, and is cheap.** Metatarsal or metacarpal organ culture is
a standard, well-controlled length assay (it is what `newton2015` and `newton2018` used). Run it at
1%, 2%, 5%, 8%, 12% and 21% O₂ and measure **length, GAG/DMMB, and hypertrophic zone height**
together. If §4 is right, length and GAG peak together **below 8%** and the hypertrophic zone
collapses above it. If it is wrong, length tracks 21% as `brighton1969`'s cartilage endpoint did.
Nobody has run it because 1969 measured the wrong endpoint and 2014 used the wrong cell. If you know
anyone with a physis organ-culture rig, this is a two-month experiment that decides the branch.

**Still open and unchanged:** `stegen2019` DCA+BPTES tibia length (Carmeliet, KU Leuven); Kelly's
lengthening series (ref 12 of `brighton1971b`) for the millimetres behind "100 per cent"; `zhang2024`
count matrix; McGarry 2024 full text; and the lateral thoracolumbar spine film.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
This round the instrument was a 2014 finite-element model of an oxygen gradient inside a cell pellet,
and it put a number — 8% — on a switch that a 1969 histology slide and a 1971 microelectrode had both
already drawn without knowing what they were looking at.*
