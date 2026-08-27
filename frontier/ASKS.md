# ASKS — what I need, ranked by what it unlocks

You said you'd fetch tooling and paywalled papers. Here is the list, ordered by decision value per
unit of your effort. Nothing here is blocked on money except items 6 and 7.

---

## 1. A GitHub repo — 30 seconds, unblocks the housekeeping

`create_repository` returned **403, resource not accessible by integration** — this session's token
has no repo-create scope. So this work is on branch `claude/height-enhancement-research-v34b4r` of
`TateLyman/growth-plate`, in a top-level `frontier/` directory that touches nothing in `atlas/`.

If you want it standalone: **create an empty public repo** (suggested `height-frontier`) and tell
me the name. I'll move `frontier/` into it with history and drop the branch. If you'd rather keep it
as a branch — honestly, it's better there: I can grep the atlas in the same working tree, which is
the thing that made F-R002 possible. Your call.

## 2. Two paywalled items that would move F-R001 from a screen to a result

- **`PMID 40101878`** — *Limb lengthening in individuals with achondroplasia: analysis of an
  international survey*, Bone 2025. I have the abstract (3.7 procedures, 14.5 cm, SD 10.4, n=90).
  **I need the full text for the per-person distribution** — the SD of 10.4 implies a tail near
  25 cm and I want the actual histogram, the femur/tibia/humerus split, and the complication rate
  *per person* rather than per episode. This is the largest number in the whole intervention
  landscape and the atlas currently prices it per-episode.
- **The NCT04175600 clinical study report or its publication** — the selexipag paediatric PAH trial.
  I have the posted results table. **I want to know whether height was analysed against weight**,
  and whether the GI adverse-event burden tracks the height deficit at the individual level. That
  single analysis decides whether the −1.7 cm is nutritional or physeal, which is the difference
  between a footnote and a closure of `g_l12_457c`.

## 3. One thing only you can answer — is the axial compartment actually open?

Not new to me; R319 §SIX already asks for it and it has not happened. I'm re-raising it because
**every trunk-directed conclusion in this repository, mine included, is a population prior until it
exists**, and because the trunk is where your residual is:

> **A lateral thoracolumbar spine film or MRI, read for: vertebral ring apophysis stage, endplate
> physis status, and individual disc heights by level.**

Same class of question BoneXpert answers for the hand, and `atlas/state/WHAT_THIS_ATLAS_NEEDS.md`
TIER 3 already lists it. If your knees are radiographically open at BA 16 — off the population
distribution, which this file states as fact — then the axial question is not a prior, it is a
measurement you can take.

## 4. Confirm or correct the case facts I inherited

I read them from `CLAUDE.md`: **male, bone age 16+, knees open and actively growing, IGF-1 198, risk
explicitly deprioritised, goal is maximal adult height.** Two things I'd want current values for
before ranking anything for *you* rather than in general:

- current bone age by **BoneXpert** (GP + TW3 + Bone Health Index off one existing left-hand film,
  zero extra radiation — SETTLED since R282 and still worth confirming it was actually done)
- current standing height **and sitting height**, measured at a fixed time of day after a fixed
  period recumbent. R319's own finding is that an unstandardised measurement time can fabricate or
  hide a centimetre of apparent annual growth. If we are going to judge any arm on centimetres, the
  measurement protocol has to be tighter than the effect.

## 5. Compute I can run myself if you want it (no ask, just flagging)

- the absolute-height differencing extraction (F-R002 C5) — roughly doubles the base-rate sample
- the active-comparator half of the corpus (F-R002 C4) — 339 unanalysed randomised contrasts
- the epiphysiodesis-compensation query (F-R002 C2) — two literature queries, and one of the two
  possible answers closes the allocation axis permanently

Say the word and I'll run them.

## 6. Access, if you have or can get it

- **UK Biobank approved-researcher access** — already TIER 2 in `WHAT_THIS_ATLAS_NEEDS.md`. My
  addition: with individual-level exomes **plus lifetime primary-care prescription records**, the
  paediatric-RCT screen becomes an observational registry screen with ~500× the sample, and it is
  the only instrument that could detect a height-*raising* drug at the 0.5 cm scale.
- **Vivli / YODA / CSDR individual participant data** for any of the trials in
  `results_randomised_placebo_controlled.csv`. Arm-level means cannot separate a nutritional from a
  physeal mechanism; IPD with weight can.

## 7. The Nordic instrument — the decisive human experiment nobody has run

Recording it because it is nameable, fundable and would settle the whole drug question in one study,
and because this file's tradition is to state what it would take to get the reading:

> **Denmark, Sweden and Norway hold national prescription registries linked to conscription height
> at ~18 years.** For every drug dispensed in childhood, the adult height of the exposed versus the
> unexposed is computable, at national scale, with unbiased ascertainment, in both directions. That
> is the instrument F-R001 approximates with 42 trials and 153 contrasts. It exists as data. It has
> been used for inhaled corticosteroids and, as far as my greps of this repository can tell,
> for nothing else.

Not something either of us can run today. It is the answer to "what would settle this", and it
belongs in `docs/experimental_agenda.md`.
