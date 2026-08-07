# Round 41 — Cinque closes the ledger, and you were right that I never engaged the lysosome argument

## Your logic was right; the answer went the other way

You said: *if inhibiting FGFR4 is positive then we reopen.* Correct. Cinque 2015 says it isn't.

> Autophagy is **necessary for bone growth** — Atg7 deletion reduces femoral and tibial length from P9 —
> and postnatal chondrocyte autophagy is induced by **FGF18 through FGFR4** and JNK.
> **Fgf18⁺/⁻ and Fgfr4⁻/⁻ mice fail to induce autophagy** and show **decreased Col2** in the growth plate;
> both phenotypes are **rescued in vivo by pharmacological activation of autophagy**.
> RNAi of *Fgfr3* or *Fgfr4* — but **not** *Fgfr1* or *Fgfr2* — blocks FGF18-induced autophagy.

**FGFR4 is required for the autophagy that bone growth requires. Blocking it is a second cost.**

### The receptor ledger, now complete

| receptor | effect of **inhibiting** it | erdafitinib IC50 |
|---|---|---|
| **FGFR3** | **pro-growth** ✓ | 3.00 nM |
| **FGFR1** | **anti-growth** (shortened tibiae, `karolak2015`) | **1.20 nM** — engaged *first* |
| **FGFR4** | **anti-growth** (autophagy failure, `cinque2015`) | 5.70 nM |

**One pro-growth target, two anti-growth targets — and erdafitinib hits an anti-growth receptor *more*
potently than the pro-growth one.** A narrowly FGFR3-selective agent takes the benefit and pays neither
cost.

### And it resolves the contradiction I'd left standing

FGF19→FGFR4 *restrains* growth (Wnt antagonists). FGF18→FGFR4 *promotes* growth (autophagy). **Same
receptor, opposite signs, different ligands.** And I'd already measured which ligand operates in human
cartilage: **FGF19 needs β-klotho — absent — and FGF19 itself is undetectable; FGF18 needs no klotho and
is present.** So the operative FGFR4 signal in human growth plate is **the growth-promoting one**, which
makes FGFR4 blockade anti-growth in humans specifically.

That's the KLB check paying off in a way I didn't anticipate when I ran it.

## You're right that I never engaged the lysosome argument

I searched, found nothing, and wrote that it was *"the wrong axis of comparison anyway — a PK property."*
**That was a dismissal, not an assessment.**

**The argument's real form isn't duration — it's tissue concentration in an avascular tissue.** The growth
plate is avascular and alymphatic and drug delivery to it is severely limited. A weak base trapped in
lysosomes could hold intracellular concentrations far above plasma — **which would mean the plasma-derived
IC50 ordering I built my entire case on doesn't describe what happens in cartilage.** That is the
strongest available objection to my own argument, and I missed it because I stopped at a category label.

**Assessed properly — three counts, one decisive:**

1. Lysosomal sequestration is classically a **resistance** mechanism; it moves drug *away* from cytosolic
   targets, and FGFR kinase domains face the cytosol.
2. **Decisive: accumulation is *tissue* selectivity, not *receptor* selectivity.** All four FGFRs sit in
   the same chondrocyte and see the same intracellular concentration. Concentrating erdafitinib in
   cartilage raises FGFR1 and FGFR4 engagement **exactly as much as** FGFR3. **The ordering survives any
   uniform scaling** — and with one pro-growth and two anti-growth targets, concentrating the drug
   concentrates the harm alongside the benefit.
3. Still unverified for erdafitinib specifically.

**So: real argument, wrongly waved away, and on inspection it cuts the other way.** It would be a *strong*
argument for a drug whose cartilage targets were all pro-growth — which is precisely what an
FGFR3-selective agent is. Logged as **CORR-045**, with the generalisable failure named: *"that's PK not
PD"* is a category, not an argument, and it let me avoid noticing that **plasma-equals-tissue was a
load-bearing assumption I had never written down.**

## Final position

**Right axis, wrong molecule — and now on mechanism rather than on evidence-weighing.**

- **FGFR3-selective** (TYRA-300 class), or low-dose infigratinib which achieves +1.74 cm/yr with no FGFR1
  or FGFR2 signal at all
- **not** erdafitinib, whose most potently engaged receptor is one whose blockade shortens bones, and
  whose third target blocks the autophagy growth depends on

**The stack, as it now stands:**

| arm | agent | status |
|---|---|---|
| **h_term** | CNP analogue **+ NPR2-phosphatase inhibitor** | additive and quantified (`shuhaibar2021`) |
| **amplification** | **FGFR3-selective only** | ledger complete |
| **pool** | Gli1⁺/PDGFRA⁺ reservoir recruitment | candidate only; `orikasa2024` conflict unresolved |
| **duration** | aromatase inhibition | required if pool cycling is attempted |
| *excluded* | growth hormone | spends the pool to buy rate |

Validator: 645 nodes, 1249 edges, 321 gaps, 1155 refs — 0 errors, 0 warnings.
