# F-R028 — The knife edge, the drain, and the human pressure vessel

Three things this round: `imre2025` recovered as far as it can be, `nilsson2014` read, and two papers
found that change what is possible to *test*.

---

## 1. `imre2025` — I could not get the full text, and the abstract carries the decisive fact anyway

**Status, definitively:** Unpaywall returns `is_oa: false`, `oa_status: closed`,
`has_repository_copy: false`, `oa_locations: []`. Europe PMC lists exactly one full-text URL,
`availability: "Subscription required"`. **There is no open copy anywhere.** *Hormones (Athens)* is
Springer, and the only routes are a subscription, an institutional library, or the authors
(**Seçkin Akçay / Dilek Yavuz, Marmara University, Istanbul**). I am not going to pretend otherwise.

**But the abstract is complete and it contains the number that matters:**

> "The patient was treated with **transdermal estradiol (25 µg twice weekly)**, which normalized
> estradiol, testosterone, and gonadotropin levels. **Epiphyseal fusion occurred within 6 months.**"

**Twenty-five micrograms of transdermal oestradiol, twice a week, fused every long-bone physis in a
31-year-old man in half a year.** That is a low-dose HRT patch. It is roughly a homeopathic exposure
against the 10× challenge that failed in `smith2008`.

### The comparison, and it is not a close call

| | lesion | closure exposure | outcome |
|---|---|---|---|
| `imre2025` | **aromatase deficiency** — no ligand | **25 µg transdermal E2, twice weekly** | **fused within 6 months, at age 31** |
| `maffei2004` | aromatase deficiency — no ligand | oestradiol | 183.5 → 184.5 cm, **stopped** |
| `smith2008` | **ESR1 disruption** — no receptor | **transdermal oestrogen, 6 months, free oestradiol raised TENFOLD**, on top of an endogenous oestradiol already 2.4× the upper limit | **"could not be closed by any means… no detectable effect"** |

> **Ligand-level blockade is a knife edge. A trace of oestrogen from any source closes it — and the
> plate is *more* sensitive at 31 than a normal adolescent's is at 14.**
>
> **Receptor-level blockade is the only durable form of term A**, and F-R025 said so on weaker
> evidence than this.

This is a hard constraint on any aromatase-inhibition strategy: adrenal androgen aromatized in adipose
tissue, incomplete enzyme inhibition, dietary or environmental oestrogens — **any residual ligand
reaches a receptor that is present, functional, and evidently exquisitely sensitive.** The receptor
route removes the receiver instead of chasing the signal. (Mechanistic reading of three case reports;
not a recommendation, and agents are out of scope until the mechanism is closed — per your own
sequencing.)

---

## 2. `nilsson2014` — the drain measured, and it is not cell death

**Nilsson O, Weise M, Landman EBM, Meyers JL, Barnes KM, Baron J.** *Evidence That Estrogen Hastens
Epiphyseal Fusion and Cessation of Longitudinal Bone Growth by **Irreversibly Depleting the Number of
Resting Zone Progenitor Cells** in Female Rabbits.* Ovariectomised rabbits, oestradiol cypionate or
vehicle for 5 weeks, then **5 weeks untreated**.

- **Resting-zone chondrocytes per mm growth-plate width decline with age** — proximal tibia p<0.001,
  distal radius p<0.001.
- **Oestrogen accelerates that loss** — PT p<0.01, DR p<0.001.
- **It is not apoptosis.** *"the percent of TUNEL-positive resting zone cells was similar in
  estrogen- (**4.6 ± 0.6%**) and vehicle- (**4.4 ± 1.0%**) treated animals (**p = 0.87**)."*
- **And it does not recover.** *"5 weeks after the estrogen treatment was discontinued, the decline in
  number of resting zone chondrocytes per mm growth plate width **remained advanced**"* — PT p=0.07,
  DR p<0.01. *"a mechanism by which estrogen **permanently** advances structural growth plate
  senescence."*

**The cells are not dying. They are leaving and not being replaced.** That is F-R027's outflow model
measured directly, and it is the only direct inflow-versus-outflow measurement in any species.

### And an honest negative that bears on F-R027's load-bearing assumption

**The pool did not spontaneously refill in five weeks.** F-R027 rests on recruitment being able to
match outflow; `nilsson2014` is the closest thing to a test of spontaneous postnatal refill, and the
answer is no.

Two things keep that from being decisive, and I want them on the record as caveats rather than
excuses: **(a)** nobody measured the perichondrium — the recruitment compartment was not looked at;
**(b)** `rosellodiez2025`'s refill was *induced* by a challenge that made *"the challenged cartilage
signal to the surrounding tissues,"* whereas oestrogen-driven depletion may not generate that signal
at all. **Depletion without a recruitment signal is not the same experiment as depletion with one.**

**But the honest statement is: spontaneous postnatal recruitment sufficient to refill an oestrogen-
depleted resting zone has not been observed, and one experiment looked in roughly the right place and
did not find it.** F-R027's inequality remains the target; it does not yet have a demonstration.

---

## 3. The human test system exists — and I did not know it

**`The Leiden ex vivo human growth plate model in severe tall stature: a proof-of-concept study` (2026).**

> "Viable pediatric human growth plate tissue is rarely available… we aimed to determine whether it is
> feasible to establish a clinically integrated **ex vivo human GP model** using tissue obtained during
> routine **percutaneous epiphysiodesis** procedures in adolescents treated for **extreme tall
> stature**… viable GP tissue could be obtained **reproducibly**… GP-derived cells formed
> three-dimensional organoids and histology confirmed cartilage-like matrix deposition… **a unique
> platform to study local mechanisms of endochondral bone growth.**"

**Living human growth plate, obtained routinely, culturable, organoid-forming.** Every question this
branch has been unable to ask of human tissue — the 8% switch, the proteoglycan program, resting-zone
markers, recruitment, confinement — is askable in this system.

And the same irony as the aromatase literature, one degree sharper: **the only reliable source of human
growth-plate tissue is surgery performed to stop tall adolescents from growing.**

---

## 4. The pressure vessel, described in human tissue

**`Physical and chemical niche of human growth plate for polarized bone development`
(PMC12334589, 2025, open access).** High-resolution mechanical and compositional mapping of the
**human** growth plate and its two interfaces:

> "the **GP–epiphysis interface displays a sharp transition in tissue modulus, acting as a protective
> shell** for the underlying GP, whereas the **GP–metaphysis interface exhibits a gradual modulus
> increase, enabling efficient load redistribution** to the metaphysis."
>
> "the **GP–epiphysis interface acts as a mineralization INHIBITION zone** while the **GP–metaphysis
> serves as a mineralization PROMOTION zone**… **SPP1** and **AHSG** at the GP–epiphysis interface
> **inhibit mineralization, forming a defense line**; while **ENPP1** and **ALPL**… promote…
> nucleation and assembly of calcium phosphate at the GP–metaphysis. Such polarized mineralization
> patterns… **drive polarized bone elongation.**"

**That is F-R023's pressure vessel, measured, in humans, with the parts named.**

| pressure-vessel part | human anatomy | molecular identity |
|---|---|---|
| **closed end** (holds, does not yield) | GP–epiphysis interface — *"a protective shell"*, sharp modulus step | **SPP1, AHSG** — mineralization inhibitors, *"a defense line"* |
| **radial wall** | perichondrial ring of LaCroix | mechanical; cut it and the cartilage protrudes in an arc (`rodriguez1985`) |
| **moving face** (yields, converts) | GP–metaphysis interface — graded modulus, load-redistributing | **ENPP1, ALPL** — mineralization promoters |
| **working fluid** | proteoglycan matrix, ~0.28 MPa | fixed charge; gated at **pO₂ < 8%** (F-R015) |

**The authors' own phrase for the output is "polarized bone elongation."** The tissue does not simply
swell — it is *built* to convert an isotropic pressure into one direction, and both ends are
molecularly specified to do it. F-R023 argued this from a 1985 scalpel; here it is with moduli and a
proteomic map, in human tissue, published last year.

**Atlas check:** `SPP1` 44 files, `AHSG` **0**, `ENPP1` 33, `mineralization inhibition zone` **0**,
`polarized bone elongation` **0**.

---

## 5. Where the three terms stand

| term | status | what changed this round |
|---|---|---|
| **never close** | **solved, and the grade now matters enormously** | Ligand-level fuses at **25 µg twice weekly in 6 months at age 31**. Receptor-level survived **10×**. Term A is a *receptor* problem, not a hormone-level problem. |
| **constant / never empty** | **the drain is measured; the refill is not** | `nilsson2014`: loss is **not apoptosis** (TUNEL 4.6 vs 4.4%, p=0.87) and **does not recover in 5 weeks**. Cells leave and are not replaced. F-R027's inequality is the right target and remains undemonstrated. |
| **fast** | **the vessel is now described in human tissue, and a human test system exists** | PMC12334589 names both ends of the cylinder; the Leiden model makes every remaining question testable on living human growth plate. |

**The whole framework now reduces to two experiments**, and both are runnable:

1. **Can recruitment exceed the set point?** (F-R027's load-bearing assumption.) Local Hh pulse at the
   groove of Ranvier, **unchallenged** limb, contralateral control, length to maturity.
2. **Is an arrested plate above the 8% switch?** One Safranin-O — and the Leiden model supplies the
   tissue prospectively rather than waiting for a pathology archive.

---

## 6. Asks

**#1 — the Safranin-O, two routes, both now concrete.**
 (a) **`carroll2018`'s archived specimen** — Brooke Army Medical Center, Dept of Orthopaedic Surgery,
 bilateral proximal tibia, 2018. H&E exists; **one additional stain on cut tissue.**
 (b) **The Leiden group** — proof-of-concept published 2026, tissue obtained *reproducibly* from
 percutaneous epiphysiodesis in extreme tall stature. **They have the tissue, the ethics approval and
 the pipeline.** I could not resolve the paper's authors from the Europe PMC record (no PMID, no PMC);
 **if you can get the full citation or author list, that is the single most useful thing you could
 fetch next.** LUMC, Leiden; the RAAK study is the linked cartilage biobank.

**#2 — `imre2025` full text** remains genuinely paywalled — *Hormones* (Springer), no repository copy.
Library or the Marmara authors. The abstract gave me the decisive number, so this is now
lower priority than #1.

**#3 — PMC12334589's supplementary** (open access, so I can reach the main text — I have the abstract
and will read the body next round unless redirected). I want the **modulus values** at each interface
and the **spatial proteomics**, because those are the numbers that would size the f_axial term.

**Still standing:** Brighton thesis (UIC ILL, handle `10027/14248`); JBJS 1980;62A:740; Surgical Forum
1970:465–467; `stegen2019` DCA+BPTES tibia length; the lateral thoracolumbar film.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
This round two instruments turned up that see it directly — an atomic-force modulus map of a human
growth plate, and a Leiden operating theatre where viable human physis is discarded weekly. The
mechanism has been visible in human tissue for a year. What has been missing is anyone asking it to
grow rather than asking it to stop.*
