#!/usr/bin/env python3
"""Round 246. Can a self-renewal fraction be inferred from what already exists?

chu2025 establishes that growth plate stem cells renew by POPULATION ASYMMETRY,
with clone sizes following an exponential scaling distribution (R^2 = 0.96) -
the signature of neutral competition. It reports the qualitative result and does
not report the kinetic parameter. Fig. 4D and 4E contain the data to derive one.

VALUES READ OFF FIG. 4D AND 4E of the published figure (PMC OA package). They are
FIGURE READS, not tabulated numbers, and are recorded to one decimal place with no
implied precision beyond that.
"""
import math

# Fig 4D: average clone size, cells per clone
SIZE = {2: 11.3, 3: 12.6, 4: 14.2, 5: 21.0, 7: 21.2}
# Fig 4E: clone density, clones per mm growth plate width (group means)
DENS = {2: 43.0, 3: 14.2, 4: 16.5, 5: 13.2, 7: 7.7}

print("=" * 74)
print("LINEAGE KINETICS DERIVED FROM chu2025 FIG. 4D AND 4E")
print("Col2-CreERT2:R26R-Confetti, tamoxifen at 1 month, mouse tibia")
print("=" * 74)
print(f"{'age (mo)':>9}{'clone size':>12}{'density':>10}{'size x density':>16}")
for m in sorted(SIZE):
    print(f"{m:>9}{SIZE[m]:>12.1f}{DENS[m]:>10.1f}{SIZE[m]*DENS[m]:>16.1f}")
print()
print("FIRST OBSERVATION, AND IT MATTERS: size x density IS NOT CONSERVED - it falls")
print("from 486 to 163 between 2 and 7 months. A closed zero-sum system would conserve")
print("it. THE GROWTH PLATE IS A FLOW-THROUGH SYSTEM: labelled progeny leave through the")
print("hypertrophic zone and are replaced by bone. So the neutral-drift algebra applies to")
print("the STEM COMPARTMENT ONLY, and clone density is the observable that tracks it.")
print()

def halflife(t0, t1, d0, d1):
    yrs = (t1 - t0) * 30.44
    return yrs * math.log(2) / math.log(d0 / d1)

print("-" * 74)
print("LINEAGE HALF-LIFE - the time for half of surviving stem-cell lineages to be lost")
print("-" * 74)
print(f"  2 -> 7 months (all points): density {DENS[2]:.1f} -> {DENS[7]:.1f}, "
      f"half-life {halflife(2,7,DENS[2],DENS[7]):.0f} days")
print(f"  3 -> 7 months (post-washout): density {DENS[3]:.1f} -> {DENS[7]:.1f}, "
      f"half-life {halflife(3,7,DENS[3],DENS[7]):.0f} days")
print()
print("THE TWO WINDOWS DISAGREE BY MORE THAN TWOFOLD AND THE REASON IS VISIBLE IN THE")
print("DATA. The 2-to-3-month drop (43.0 -> 14.2) is far steeper than anything after it,")
print("and the 4-month point (16.5) is HIGHER than the 3-month point, so the series is")
print("not monotonic. The early collapse is most simply read as clones that never")
print("contained a stem cell washing out - which is the phenomenon the authors themselves")
print("waited for before starting. THE DEFENSIBLE NUMBER IS THE POST-WASHOUT ONE, and it")
print("carries the non-monotonicity as its error.")
print()
print("=" * 74)
print("AND NOW THE PART THAT ANSWERS THE QUESTION - BY SHOWING IT WAS THE WRONG QUESTION")
print("=" * 74)
print("""
The programme has been asking for 'the self-renewal fraction'. Under population
asymmetry with neutral competition - which is what chu2025 demonstrates, and what
the exponential clone-size scaling at R^2 = 0.96 confirms - THAT FRACTION IS NOT A
FREE PARAMETER. In a neutral system the probability of symmetric renewal EQUALS the
probability of symmetric loss. The fraction is pinned at one half BY THE DEFINITION
OF NEUTRALITY, and clone-size data cannot measure it because every neutral system
gives the same answer.

What clone data CAN measure is the RATE at which lineages are extinguished, which is
the product of the division rate and the symmetric-division probability. Separating
the two needs a division rate the clone data does not contain.

SO THE TARGET HAS TO BE RESTATED, AND RESTATING IT CHANGES WHAT COUNTS AS SUCCESS:

  - Raising the self-renewal fraction ABOVE one half in a neutral population does not
    give a bigger stem pool at steady state. IT ABOLISHES NEUTRALITY. A population in
    which renewal reliably exceeds loss is a clonally expanding population, which is
    the definition of what the brief forbade - hyperplasia.

  - But a growth plate approaching closure is NOT at steady state. Its pool is
    declining, so renewal is BELOW loss. Moving it back toward one half is
    RESTORATION, not elevation - CORR-203 in the direction the programme is allowed
    to want.

THE TARGET CONDITION 'replacement >= loss' IS THEREFORE EXACTLY THE NEUTRAL POINT,
NOT SOMETHING BEYOND IT. The programme should stop looking for a lever that raises
the fraction and start looking for whatever is dragging it below one half in a
closing plate. That is a different search and the atlas has not run it.
""")
