"""Two analyses on the oestrogen-null census.

A. SURVIVAL ON AGE, with epiphyseal closure as the event.
   Every reported case is a RIGHT-CENSORED observation: last seen with open
   epiphyses at age X. If no case ever reports spontaneous closure, the
   Kaplan-Meier survival is 1.0 at every observed age and the median is
   undefined - which is the formal statement of "never observed".

B. HOW FAST DOES BONE AGE ADVANCE WITHOUT OESTROGEN, and what does that predict?
   Only ONE person in the record has two bone ages. That measured rate is the
   only basis for extrapolating to closure.

GUARDS:
  G1 The Morishima male (bone age 14 at chronological 24.25) and the Smith
     propositus (bone age 15 -> 17.5 over 3.5 y) must both be present.
  G2 If ANY case reports spontaneous closure, analysis A is invalid as framed
     and must be redone as a real survival problem with events.
"""
import json, sys

# ages at last report WITH OPEN EPIPHYSES OR ONGOING GROWTH, from abstracts/full texts
CENSORED = [
 ("Morishima 1995 (CYP19A1)",        24.25, "bone age 14 at 24.25; tall, delayed skeletal age"),
 ("Carani 1997 (CYP19A1)",           None,  "progressive height gain, unfused epiphyses"),
 ("Deladoey 1999 (CYP19A1)",         None,  "very low estradiol"),
 ("Maffei 2004 (CYP19A1)",           29.0,  "persistent linear growth"),
 ("Bouillon 2004 (CYP19A1)",         17.0,  "open epiphyses"),
 ("Herrmann 2005 (CYP19A1)",         27.0,  "tall, eunuchoid, low bone mass"),
 ("Maffei 2007 (CYP19A1)",           25.0,  "tall stature, eunuchoid"),
 ("Lanfranco 2008 (CYP19A1)",        None,  "progressive tall stature, unfused epiphyses"),
 ("Baykan 2013 (CYP19A1)",           27.0,  "tall stature, fractures"),
 ("Chen 2015 (CYP19A1)",             None,  "unfused epiphyses"),
 ("Miedlich 2016 (CYP19A1)",         None,  "tall, unfused epiphyses"),
 ("Costanzo 2018 (CYP19A1)",         None,  "tall stature"),
 ("Li 2022 (CYP19A1)",               37.0,  "delayed bone age, unfused epiphyses"),
 ("Singhania 2022 (CYP19A1)",        24.0,  "open wrist and knee epiphyses; TREATED to close"),
 ("Smith propositus (ESR1)",         31.5,  "bone age 17.5, epiphyses open; cannot be closed"),
 ("Brakta patient (ESR1, female)",   24.0,  "8-year follow-up; DES failed; still hypoestrogenic"),
]
EVENTS = []      # spontaneous closure with a reported final height
if EVENTS:
    print("G2 FAILED: an event exists - redo as a real survival problem"); sys.exit(1)
ages = sorted(a for _,a,_ in CENSORED if a is not None)
names = {n for n,_,_ in CENSORED}
if not any("Morishima" in n for n in names) or not any("Smith" in n for n in names):
    print("G1 FAILED: reference cases missing"); sys.exit(1)
print("guards PASS\n")
print("=== A. SURVIVAL ON AGE, EVENT = SPONTANEOUS EPIPHYSEAL CLOSURE ===")
print(f"observations           : {len(CENSORED)}")
print(f"with an age recorded   : {len(ages)}")
print(f"EVENTS (closure)       : {len(EVENTS)}")
print(f"all observations are   : RIGHT-CENSORED")
print(f"ages at last open obs  : {ages}")
print(f"maximum age observed with open epiphyses: {max(ages)} years")
print("\nKaplan-Meier: S(t) = 1.00 at every observed age. Median age at closure: UNDEFINED.")
print("The formal statement of the census is that the survival function never falls.\n")

print("=== B. BONE-AGE VELOCITY WITHOUT OESTROGEN ===")
ba1, ba2, dt = 15.0, 17.5, 3.5
rate = (ba2-ba1)/dt
print(f"Smith propositus, the ONLY person in the record with two bone ages:")
print(f"   bone age {ba1} -> {ba2} over {dt} chronological years  =  {rate:.2f} bone-age years per year")
print(f"   i.e. {rate*100:.0f}% of the normal rate, with no functional ER-alpha\n")
for target,label in ((18.0,"bone age 18 - the usual male fusion range begins"),
                     (19.0,"bone age 19 - fusion typically complete")):
    yrs=(target-ba2)/rate
    print(f"   from bone age {ba2} at ~31.5 y, reaching {target} takes {yrs:.1f} more years -> age ~{31.5+yrs:.0f}   ({label})")
print("\n   PREDICTION: he would have closed at roughly 33 to 36 years of age.")
print("   He was 204 cm at 28. At a declining terminal velocity of 1-2 cm/yr over the")
print("   remaining 5-8 years, a final height in the region of 208-215 cm follows.")
print("\n=== THE COMPARISON THAT WOULD IDENTIFY THE RESIDUAL ROUTE, AND WHY IT CANNOT BE MADE ===")
print("""   ESR1-null      : ligand PRESENT (oestradiol high), ER-alpha ABSENT.
                    ER-beta and non-classical receptors are liganded and functional.
   Aromatase-null : ligand ABSENT, ER-alpha PRESENT but unliganded.
                    ER-beta and non-classical receptors are also unliganded.

   If the residual maturation ran through ER-beta or a non-classical receptor, the
   aromatase-null man should mature MORE SLOWLY than the ESR1-null man. If the two
   rates match, the residual route is oestrogen-INDEPENDENT - androgen, or the
   intrinsic senescence programme.

   THE TEST REQUIRES TWO BONE AGES IN AN AROMATASE-DEFICIENT PATIENT.
   NO PUBLISHED CASE PROVIDES THEM. Morishima gives one point (bone age 14 at
   24.25) and a single point yields no rate without assuming when divergence began -
   an assumption that swings the answer from 0.16 to 0.58 y/y.""")
