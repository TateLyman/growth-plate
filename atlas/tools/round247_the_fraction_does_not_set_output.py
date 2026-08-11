#!/usr/bin/env python3
"""Round 247. What actually drags a growth plate to closure - posed properly.

Round 246 concluded that the self-renewal fraction is pinned at one half under
neutral drift and that the target is restoration to neutrality. That is right and
it is not enough, because a grade-B node in this atlas already says something that
sits awkwardly beside it: stem_pool_size_versus_flux found that in three of four
perturbations POOL SIZE AND BONE GROWTH MOVE IN OPPOSITE DIRECTIONS, and that the
variable tracking growth is FLUX.

If the fraction is pinned and the pool does not track growth, what does? This
script does the algebra, because the answer is a two-line calculation nobody in
this programme has written down.
"""
from fractions import Fraction as F

print("=" * 76)
print("THE POPULATION-ASYMMETRY BOOKKEEPING, DONE EXPLICITLY")
print("=" * 76)
print("""
A stem cell divides. Under population asymmetry there are three outcomes, with
r the probability of each symmetric one (the system is neutral when they are equal):

    symmetric renewal   prob r       1 stem -> 2 stem,      0 committed
    symmetric loss      prob r       1 stem -> 0 stem,      2 committed
    asymmetric          prob 1 - 2r  1 stem -> 1 stem,      1 committed
""")
for r in [F(0), F(1,10), F(1,4), F(1,3), F(49,100), F(1,2)]:
    dstem = r*1 + r*(-1) + (1-2*r)*0
    dcomm = r*0 + r*2 + (1-2*r)*1
    print(f"  r = {str(r):>7}   E[change in stem] = {dstem}   E[committed produced] = {dcomm}")
print("""
TWO RESULTS, AND THE SECOND IS THE ONE THIS PROGRAMME NEEDED.

ONE - the expected change in stem number is ZERO FOR EVERY r. That is what neutral
means, and it is why r cannot be read off clone data: every neutral system looks the
same in expectation.

TWO - THE EXPECTED COMMITTED OUTPUT IS EXACTLY ONE PER STEM DIVISION, FOR EVERY r.
r cancels: 2r + (1 - 2r) = 1. THE SELF-RENEWAL FRACTION DOES NOT SET OUTPUT AT ALL.
It sets only the VARIANCE - how fast lineages are lost to drift, hence clone-size
dispersion and the lineage half-life round 246 derived. It is a dispersion parameter,
not a production parameter.
""")

print("=" * 76)
print("WHAT THAT MEANS FOR THE OBJECTIVE FUNCTION")
print("=" * 76)
print("""
Committed cells produced per unit time = lambda * N
      lambda = stem division rate
      N      = number of stem cells

and adult height is the time integral of what those committed cells become:

      HEIGHT  =  INTEGRAL over the plate's lifetime of  ( lambda * N * A * h_term )

      A      = transit amplification - divisions a committed daughter makes in the
               proliferative zone before hypertrophy
      h_term = terminal hypertrophic cell height

THE FOUR TERMS ARE THE ONLY PLACES HEIGHT CAN COME FROM, AND THEY ARE NOT EQUIVALENT:

  lambda  raising it raises output NOW and spends stem divisions at the same rate.
          arm3_pool_ceiling_is_imposed_not_intrinsic establishes that the senescence
          counter is DRIVEN BY GROWTH RATHER THAN TIME, so lambda is coupled to the
          counter. THIS IS WHY GROWTH HORMONE BUYS VELOCITY AND SELLS DURATION.

  N       stem_pool_size_versus_flux establishes that raising N alone does NOT
          lengthen bone - Ptch1 deletion gave hyperplasia and no length, Fgfr3 excess
          gave an EXPANDED resting zone and SHORTER bones. A pool that cannot
          discharge is a bigger pool and a shorter bone.

  A       RAISING THIS SPENDS NO STEM DIVISIONS AT ALL. Every extra amplification
          division happens in a cell that has ALREADY left the stem compartment and
          is already committed to being spent. The counter, being division-driven in
          the SLOW-REPLICATING NICHE (nilsson2005's triple specificity), is not
          obviously advanced by divisions that occur downstream of it.

  h_term  also downstream of the stem compartment, and round 198's second term.
""")

print("=" * 76)
print("THE CONCLUSION, STATED AS A TARGET")
print("=" * 76)
print("""
THE SELF-RENEWAL FRACTION IS THE WRONG DIAL - IT DOES NOT APPEAR IN THE OUTPUT
EQUATION. Round 246 was right that it is pinned and wrong to treat reaching
neutrality as the goal; neutrality is a CONSTRAINT that keeps N from collapsing, not
a source of height.

THE ONLY TERMS THAT PRODUCE HEIGHT WITHOUT SPENDING THE COUNTER ARE THE TWO
DOWNSTREAM ONES, A AND h_term. Both sit in cells that have already left the stem
compartment. This is the formal version of what stem_pool_size_versus_flux observed
empirically and what arm3 named as its unsolved target - RUN THE COUNTER SLOWLY
WHILE THE PLATE KEEPS PRODUCING - and it says where such an intervention has to act.

IT ALSO SORTS THE EXISTING STACK WITHOUT REFERENCE TO ANY OF ITS PHARMACOLOGY:

    GROWTH HORMONE acts on lambda and on stem exit. It buys the term that is
    coupled to the counter. That is the same verdict rounds 236, 241 and 243
    reached by three unrelated routes.

    FGFR3 INHIBITION and the CNP axis act on the PROLIFERATIVE compartment - on A.
    They buy the term that is not.

WHAT THIS DOES NOT SETTLE, AND IT IS THE LOAD-BEARING UNKNOWN: whether the
senescence counter is advanced by stem divisions only, or by total divisions
including amplification. nilsson2005's triple specificity - methylation loss occurs
with SLOW replication in the niche, NOT during rapid replication of the same cells
in culture, NOT differently between resting and hypertrophic zones - points to the
former, which is what makes A a free term. IF THE COUNTER IS ADVANCED BY TOTAL
DIVISIONS INSTEAD, RAISING A SPENDS IT TOO AND THIS WHOLE ARGUMENT COLLAPSES TO
'EVERYTHING IS VELOCITY'. That is the experiment the programme should be pointing at.
""")
