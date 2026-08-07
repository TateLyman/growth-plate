# Round 32 — you were right about erdafitinib, and it still isn't the one. The assembled stack.

## 1. The correction first

I said infigratinib was the FGFR-selective one and implied it was the better FGFR3 inhibitor. **That was
wrong, asserted from memory, in a message.** ChEMBL medians:

| target | erdafitinib | infigratinib | erdafitinib is |
|---|---|---|---|
| FGFR1 | 1.20 nM (n=15) | 2.90 nM (n=29) | 2.4× more potent |
| FGFR2 | 2.50 nM (n=21) | 4.95 nM (n=28) | 2.0× more potent |
| **FGFR3** | **3.00 nM (n=25)** | **10.00 nM (n=36)** | **3.3× more potent** |
| FGFR4 | 5.70 nM (n=15) | 61.00 nM (n=18) | 10.7× more potent |

**Erdafitinib is more potent at every FGFR.** Logged as CORR-038.

And your deeper point is also right: the clinical gap is bigger than the biochemical one, because
**infigratinib for achondroplasia is dosed at 0.25 mg/kg/day** — a fraction of its oncology dose — while
**erdafitinib is titrated upward against serum phosphate to maximum tolerated exposure**. That is a real
and underappreciated difference, and it is about realised exposure, not the molecule.

**Neither compound is FGFR3-selective.** Both hit FGFR1 *harder* than FGFR3 (erdafitinib 2.5×,
infigratinib 3.4×). Hyperphosphatemia is therefore on-target and unavoidable for the class — which turns
out to matter mechanistically, below.

## 2. Vosoritide vs erdafitinib — the mechanistic answer

Not "erdafitinib is scary." Three specific reasons, in ascending order of importance.

**(a) They act on different zones, and only one is the h_term arm.**

- CNP/NPR2 partitions onto **hypertrophy**: cartilage-specific *Npr2* loss takes the type X collagen
  layer to **23.0 %** of control while the non-hypertrophic layer falls only to **71.1 %** (`nakao2015`).
- FGFR3 inhibition acts on **proliferation**: infigratinib increased femur length and **proliferative-zone**
  growth plate length with reduced phospho-ERK1/2 (`kot2026`).

FGFR3 does converge on the CNP node — it restrains growth partly by dephosphorylating NPR2 and lowering
cGMP — but it *also* restrains proliferation directly. **So FGFR inhibition raises both terms of the
yield; CNP raises mainly h_term.** For a strategy built on the free term, CNP is the more selective
entry point.

**(b) The phosphate problem is not a side effect — it is aimed at the target cell.**

The atlas holds: **normal phosphate is required for caspase-9-mediated mitochondrial apoptosis of
terminal hypertrophic chondrocytes.** FGFR1 blockade disrupts FGF23/Klotho signalling and raises serum
phosphate — that is the class's dose-limiting *and* dose-titrating effect. So an FGFR inhibitor raises
the very signal that executes the terminal hypertrophic cell, which is the cell whose size and
persistence *is* the h_term lever. **The strategy and the toxicity act on the same cell in opposite
directions.** This is my inference, not either source's, and it is testable.

**(c) The bone-age evidence exists for one and not the other.** `dauber2026` gives vosoritide a 4.0 SD
velocity gain with BA/CA unmoved. `savarirayan2026infig` gives infigratinib **+1.74 cm/yr (95 % CI
1.31–2.17)** at 52 weeks — a real and comparable effect, **but the atlas does not hold its bone-age
data.** That single number would separate the two terms in humans.

**Verdict: vosoritide-class for the h_term arm.** Not because erdafitinib is dangerous — because it is
less term-selective, and its on-target phosphate effect works against the compartment being targeted.
Together? Plausible on the zone argument (different compartments), but see §3 — and no one has
co-administered them.

## 3. The stack — and the negative that matters most

Sorted by which term each agent moves:

| term | agents | human evidence |
|---|---|---|
| **h_term** (free) | CNP analogues — vosoritide, navepegritide | **4.0 SD velocity, BA/CA unmoved** (`dauber2026`) |
| **amplification** (costs pool) | GH; FGFR3 inhibition | GH saturates on final height; infigratinib +1.74 cm/yr |
| **pool** | *nothing* | — |

**Across-terms stacking works.** `mcdonnell2026` (COACH, n=21): navepegritide + lonapegsomatropin gave
**8.69 cm/yr vs 5.95** for matched CNP monotherapy — **+2.74 cm/yr** on top of an already-active CNP
analogue.

**Within-cGMP stacking fails, twice, by independent mechanisms.**

- **Neprilysin inhibition** (sacubitril): 2–3 % overgrowth in mice, abolished in cartilage-specific
  NPR-B knockout, **explicitly not additive with CNP**, and effective only in a narrow 3–4 week window
  (`hakata2024`).
- **PDE5 inhibition** (tadalafil): raised peak CNP-stimulated cGMP **37 %** and tissue cGMP **52 %** —
  and **did not increase rat long bone length** over three weeks (`wang2018`).

Two ways to make more cGMP, two failures to turn it into bone. **cGMP is not the limiting step once a
CNP analogue is on board.** So: **stack across terms, never within one.** Anyone assembling
sacubitril + tadalafil + a CNP analogue is buying three tickets to the same saturated node.

And when the axis is broken, the other arm cannot rescue it: 8.5 years of **high-dose GH** in biallelic
NPR2 loss finished at **130.5 cm (−6.57 SDS)** and 134 cm (`arya2020`).

## 4. What's missing — the two compounds that don't exist

**(i) A cartilage-restricted CNP.** The ceiling on the only bone-age-sparing arm is **not efficacy, it is
blood pressure** — NPR2 sits in vasculature, and `hirai2026` names hypotension as the liability of
systemic CNP, which is why they built a collagen-binding CNP fusion. `nakao2015` shows the
autocrine/paracrine pool, not circulating CNP, is the physiological driver — so a local agent should
suffice. **Every other constraint in this project is biological. This one is delivery** — the only kind
engineering reliably beats. Opened as `g_l12_cartilage_targeted_cnp`.

**But test the headroom before building the molecule.** If growth-plate CNP signalling is already
saturated at tolerated systemic doses, targeted delivery buys nothing. That experiment is a dose–response
in normal mice extending past the blood-pressure-tolerated equivalent, and it is cheap.

**(ii) Anything that enlarges the progenitor pool with intact flux.** Nothing in any species does this.
Every agent above raises output *per* progenitor or rate. **This is the one that would break the ceiling
rather than raise it** (`g_l2_larger_pool_with_intact_flux`).

## 5. Still the single highest-value document

**PMID 42370681** — the infigratinib Phase 3, for its **bone age** data. The atlas holds the +1.74 cm/yr
effect size but not the maturation. Vosoritide moves velocity without moving bone age; if infigratinib
moves both, the two terms are separated in humans and the h_term hypothesis is confirmed by contrast.

Validator: 643 nodes, 1245 edges, 320 gaps, 1142 refs — 0 errors, 0 warnings.
