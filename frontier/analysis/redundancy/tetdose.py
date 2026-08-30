"""Can auranofin be dosed to ~50% TET1 inhibition -- the human-validated magnitude?

ANCHOR: heterozygous TET1 pLoF = ~50% gene dosage = +7.74 cm (n=90, P=8.8e-27).
That is the ONLY validated perturbation. Tet1-NULL mice are SMALLER, so this is a
magnitude window exactly like R137's Wnt ladder -- overshoot has a measured phenotype.
"""
AU_MW=197.0                 # gold
CMAX_UG=0.312               # ug/mL plasma gold, healthy-volunteer phase I, day 7
IC50=0.076                  # uM, auranofin vs TET1 (in vitro fluorometric)
KD=1.804                    # uM, SPR
cmax=CMAX_UG/AU_MW*1000.0   # uM
print("="*92)
print("AURANOFIN vs THE TET1 TARGET")
print("="*92)
print("  plasma Cmax (gold, healthy volunteers, day 7) : %.3f ug/mL = %.2f uM TOTAL gold"%(CMAX_UG,cmax))
print("  TET1 IC50 (cell-free)                         : %.3f uM"%IC50)
print("  TET1 KD (SPR)                                 : %.3f uM"%KD)
print("  ratio Cmax(total) / IC50                      : %.0fx"%(cmax/IC50))
print("  t1/2                                          : ~35 days")
print()
print("="*92)
print("THE PROTEIN-BINDING PROBLEM -- this is where I overstated a number in R141, so it is explicit")
print("="*92)
print("  Gold is carried on albumin Cys34. TOTAL plasma gold is NOT free auranofin.")
print("  The IC50 was measured on intact auranofin in a cell-free assay. So:")
print()
print("  %-16s %-16s %-14s %s"%("free fraction","free conc (uM)","engagement","vs the 50% target"))
print("  "+"-"*74)
for ff in [1.0,0.20,0.10,0.05,0.02,0.01,0.005]:
    free=cmax*ff
    e=100*free/(free+IC50)
    tag=("*** ON TARGET ***" if 40<=e<=60 else ("OVERSHOOT -> the Tet1-null regime" if e>60 else "below target"))
    print("  %-16s %-16.4f %-14s %s"%("%.1f%%"%(100*ff),free,"%.1f%%"%e,tag))
print()
print("  -> the 50%% target sits INSIDE the plausible band. Same structure as R148:")
print("     the achievable range BRACKETS the validated magnitude instead of missing it.")
print()
print("="*92)
print("AND THE DOSE IS ADJUSTABLE DOWNWARD -- what fraction of the RA dose gives 50%?")
print("="*92)
for ff in [1.0,0.10,0.05]:
    need=IC50/ff                      # total gold conc needed for 50% at that free fraction
    frac=need/cmax
    print("  free fraction %5.1f%% -> need total gold %.3f uM = %.0f%% of the standard exposure"
          %(100*ff,need,100*frac))
print()
print("="*92)
print("THE BUILT-IN BRAKE (from the mechanism, not from dosing)")
print("="*92)
print("  Auranofin is 2-OG COMPETITIVE (NOG and Fe(II) compete it off; raising 2-OG")
print("  attenuates the inhibition -- shown directly in the paper).")
print("  AND the Dnmt1 paper shows that reducing demethylation demand makes 2-OG ACCUMULATE.")
print()
print("  => TET1 inhibition raises 2-OG, and rising 2-OG competes auranofin OFF TET1.")
print("     THIS IS NEGATIVE FEEDBACK. The system self-limits toward PARTIAL inhibition,")
print("     which is exactly the regime the human genetics validates.")
print("  ** But the SAME 2-OG rise is the Dnmt1 paper's shortening mechanism. Cuts both ways. **")
