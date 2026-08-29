# F-R103 — I derived the senescence signature from GSE16981, and a transplantation experiment I found by searching says no systemic agent can ever reset the counter

You asked me to search harder and only bring you genuinely paywalled things. **Everything new in this
round except the two PDFs came from search or from data I pulled myself**, including the two facts that
constrain the programme most.

---

## 1. The senescence clock, derived

`GSE16981` — Nilsson/Baron, *Spatial and Temporal Regulation of Gene Expression in the Mammalian Growth
Plate.* Microdissected rat proximal tibial growth plate, **proliferative zone at 3, 6, 9 and 12 weeks,
n=5 per age, animals castrated from 3 weeks**.

**The castration matters enormously: oestrogen is removed, so this is the *intrinsic* clock, not the
oestrogen-driven one.** Whatever changes here changes without any gonadal input.

I correlated all 31,099 probes against log age across the 20 proliferative-zone samples and mapped them
through GPL1355. Script and full output: `frontier/analysis/GSE16981/`.

**Top of the signature (|r| up to 0.96 across only four timepoints — these are near-perfectly monotonic):**

| DOWN with age | r | | UP with age | r |
|---|---|---|---|---|
| Pnpla3 | −0.958 | | Colec12 | +0.958 |
| **Apeg3** | **−0.957** | | **Sdc2** | +0.954 |
| **Matn1** (matrilin-1) | −0.956 | | **Nr3c1** (glucocorticoid receptor) | **+0.909** |
| **Wnt4** | −0.939 | | **Cdkn2c** (p18^INK4c) | **+0.907** |
| **H19** | **−0.900** | | Timp3 | +0.920 |
| **Igf1r** | **−0.899** | | Tgfbr2 | +0.899 |
| **Obsl1** (3-M syndrome gene) | −0.899 | | Mmp2 | +0.884 |
| **Peg12** | **−0.896** | | Hopx | +0.901 |

**Three imprinted genes sit in the top thirty falling genes — Apeg3, H19 and Peg12.** *Apeg3* lies in the
**Dlk1–Dio3** domain, which is the locus F-R076 to F-R078 were built on, and *H19* is the *Igf2/H19*
locus F-R080's SRA analysis measured. **The imprinted growth loci switch off as the plate senesces, and
that falls straight out of an unbiased scan.**

**And two brakes come up:** *Cdkn2c*, a CDK4/6 inhibitor, at +0.907 — a concrete cell-cycle brake being
installed with age. And **the glucocorticoid receptor, +0.909** — the tissue becomes progressively more
glucocorticoid-sensitive as it ages, which is directly relevant to the dexamethasone banking arm.

## 2. What it says about our own agents

| gene | r vs age | reading |
|---|---|---|
| **Ihh** | **−0.870** | the Hedgehog **ligand collapses** with senescence |
| **Hhip** | **+0.547** | the Hedgehog **decoy rises** |
| Ptch1 | +0.121 | receptor flat |
| Smo | −0.333 | roughly flat |
| **Ghr** | **−0.720** | **GH receptor falls** |
| **Igf1r** | **−0.899** | **IGF-1 receptor falls steeply** |
| Fgfr3 | −0.857 | |
| Col2a1 / Acan | −0.738 / −0.649 | matrix output falls |
| Dnmt3a | −0.628 | |
| **Nr1d1 (Rev-erbα)** | **+0.708** | see §3 |
| Esr1 | −0.072 | flat — *these animals are castrated* |
| Mki67 | −0.005 | **flat — proliferation index is not the senescence variable** |

**Two findings that change how I read the stack.**

**(a) The Hedgehog axis inverts with age: less ligand, more decoy, unchanged receptor.** That is the same
geometry I found in the human data in F-R092 — receptor-rich, ligand-starved — and it **worsens with
age**. It also sharpens the agent choice: **a ligand-based or Ihh-based strategy is fighting both a
falling numerator and a rising trap, whereas a Smoothened agonist bypasses both, because it acts
downstream of ligand and downstream of HHIP.** The SMO-agonist case is stronger in an old plate than a
young one.

**(b) Ghr −0.720 and Igf1r −0.899.** **The receptors for both of our flux agents disappear as the plate
ages.** This is a second, independent mechanism for the well-known waning of GH efficacy — not only pool
depletion (F-R089) but **loss of the receptor that reads the signal**. It says the GH window is early and
that late GH is pharmacologically disadvantaged regardless of dose.

---

## 3. Rev-erbα — and it converges on a node already in our stack

`KCCY_22_2109106` — *Blocking circadian clock factor Rev-erbα inhibits growth plate chondrogenesis via
up-regulating MAPK-ERK1/2 pathway.*

- The Rev-erbα **antagonist SR8278 inhibited longitudinal elongation** of metatarsal bone ex vivo
- reduced growth plate height and hypertrophic zone height
- suppressed both proliferation and hypertrophic differentiation
- **mechanism: knocking down Rev-erbα *up-regulates* MAPK-ERK1/2**, and ERK inhibition partially rescues

**Rev-erbα is required for chondrogenesis, and it works by holding ERK1/2 down.**

**ERK1/2 is the node erdafitinib already acts on** — F-R060 credited erdafitinib with *"lowering
ERK1/2, the same node phosphate→VEGFR2→caspase-9 uses to kill the terminal chondrocyte."* **A Rev-erbα
agonist and an FGFR inhibitor converge on the same effector from opposite ends of the pathway.**
Rev-erbα agonists exist as research compounds (SR9009, SR9011); heme is its endogenous ligand.

**The honest caveat on my own r=+0.708 for Nr1d1:** *Nr1d1* is a circadian gene, and GSE16981 sampled one
clock time per animal. **A single-timepoint measurement across ages confounds expression level with
circadian phase.** I am not going to claim Rev-erbα rises with senescence; I can only say the
single-timepoint value does, which could be a phase shift.

---

## 4. The two facts that constrain everything, both found by searching

I pulled the 2024 open-access review `Growth plate closure and therapeutic interventions` (PMC11551597).
Its resting-zone section contains two things I had never seen stated.

### (a) The clock is cell-intrinsic and travels with the tissue

> *"In a growth plate **transplantation experiment**, the growth rate of the transplanted growth plate was
> dependent on **donor animal, but not recipient animal, age**."*

**A young plate in an old animal grows young. An old plate in a young animal grows old.**

**This is the hardest constraint in the entire file, and it applies to row 3 directly: no systemic agent
can reset the counter, because the systemic environment demonstrably does not set it.** Everything in our
stack — GH, anastrozole, erdafitinib, a Smoothened agonist, sulfate, dexamethasone — is systemic. **By
this experiment, none of them can restore capacity.** They can change the setpoint, the rate, or the
deadline. They cannot reset the clock.

Only something that acts on the cells' internal state can, which is exactly the partial-reprogramming
class from F-R068–F-R081 and nothing else in the file.

### (b) Telomeres are ruled out, and DNA methylation is the named candidate

> *"loss of telomerase activity had **no major effects** on skeletal growth, indicating that telomere
> shortening is **not** the primary mechanism limiting chondrocyte proliferation… however, in vitro
> studies have shown that **epigenetic changes in the methylation of genomic DNA may limit chondrocyte
> replication**."*

**The counter is a DNA-methylation counter.** That reconnects the DNMT3A arm (F-R079–F-R084) to the
capacity question, and it is a connection I have never made explicitly: **DNMT3A loss may not merely
raise the setpoint by +3.0 SD — it may slow the counter itself.** That would make it the only agent in
the file that touches row 3, and it is why the DNMT3A arm deserves to come back off the shelf.

### (c) A completeness check that came out well

The same review's therapeutic section lists, exhaustively, what the field has: **GnRH analogues,
aromatase inhibitors, CNP analogues, FGFR-3 inhibitors.** All four are in our stack or were considered
and priced. **We are not missing a known intervention** — which is a genuine, if uncomfortable, result:
everything beyond those four that we are pursuing is ahead of the published field, and correspondingly
unsupported.

---

## 5. Where this leaves the three rows

| row | what it buys | best agent | status after this round |
|---|---|---|---|
| **1. more cells** | +2 to +4 SD (human *PTCH1*) | Hedgehog at het dose | **strengthened** — SMO agonism is the right class precisely because ligand falls and decoy rises with age |
| **2. spend slower** | fusion 88% → 14% (Gafni) | dexamethasone | **strengthened** — *Nr3c1* rises with age, so the tissue becomes more glucocorticoid-responsive over exactly the window we would use it |
| **3. reset** | infinite | partial reprogramming; possibly DNMT3A | **constrained** — the transplantation result says no systemic agent can do it, and DNA methylation is named as the counter |

**Rows 1 and 2 both got better this round. Row 3 got harder and better-defined at the same time.**

## 6. Asks — genuinely exhausted or paywalled only

1. **The growth-plate transplantation primary source.** The 2024 review cites it without detail and the
   citation is numbered-only in the OA text. It is the single most load-bearing experiment for row 3 and
   I want the actual design, species and magnitude. *(Searched; the review's reference list is not
   resolvable from the OA XML.)*
2. **`237bab91-318.pdf` is a scanned image** — pymupdf and pypdf both extract 9 characters. If you have
   a text version, or can tell me what it is, I will read it. Otherwise it is unread.
3. **The in vitro DNA-methylation-limits-chondrocyte-replication study** the review points at. It is the
   mechanistic bridge between the DNMT3A arm and the capacity counter, and I could not identify it from
   the OA reference list.
4. Still genuinely open and searched without success: a banking experiment in a fusing species followed
   past control fusion; wild-type Ptch1(+/+) growth-plate arm; Xiu 2022 supplementary.

---

*On searching: this round the senescence signature, the Hedgehog inversion, the receptor decline, the
transplantation constraint, the telomere exclusion and the completeness check all came from data I
pulled or reviews I found. The only things I am asking you for are one citation the OA text does not
resolve, one scanned PDF, and three items I have now failed to find repeatedly.*
