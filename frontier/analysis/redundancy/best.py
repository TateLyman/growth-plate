h0,tgt=180.3,195.6; need=tgt-h0
print(f"TARGET {h0} -> {tgt} cm   need +{need:.1f} cm\n")
print("="*72)
print("TIER 1 — RANDOMISED OR INTERNALLY CONTROLLED IN HUMANS (defensible)")
print("="*72)
t1=[("GH vs placebo, randomised double-blind, peripubertal ISS",3.7,"Leschek"),
    ("AI on top of GH, matched pairs, >=2 YEARS (1 yr = 0)",3.3,"p=0.044")]
s1=sum(v for _,v,_ in t1)
for n,v,src in t1: print(f"  +{v:4.1f} cm  {n:56s} [{src}]")
print(f"  ------  TIER 1 TOTAL = +{s1:.1f} cm  ->  {h0+s1:.1f} cm")
print("\n  ⚠ SCOPE: measured in SHORT boys at BA 13-15. Subject is 180.3 cm at BA 16 —")
print("    taller, later, one BA-year past the tested range. Discount required, size unknown.\n")
print("="*72)
print("TIER 2 — MECHANISTICALLY SUPPORTED, NOT MEASURED AS FINAL HEIGHT IN THIS SETTING")
print("="*72)
t2=[("erdafitinib: h_term + matrix + NPR2 phospho-state",None,"BA-neutral per operator films"),
    ("CNP axis (vosoritide +/- sacubitril): <=2.4% redundant w/ erda",None,"+0.89 cm/yr sitting ht, RESCUE-derived"),
    ("disc / axial decompression: fusion-independent",1.2,"flotation persisting fraction")]
for n,v,src in t2:
    print(f"  {'+%.1f cm'%v if v else '  ?    ':8s} {n:56s} [{src}]")
print("\n="*1+"="*71)
print("TIER 3 — NO LENGTH ENDPOINT ANYWHERE (do not count)")
print("="*72)
for n in ["N arm: charge (PDGF-BB/MHY1485/local GH) -> discharge (vismodegib)",
          "AR antagonist as charge agent (MSC data only, not cartilage)",
          "VinSpinIn / SPIN4 (no bone endpoint for the class)",
          "NAAS on top of AI (redundant per R127; Zhou 2015 fails replication)"]:
    print(f"     ?     {n}")
print("\n"+"="*72)
print("THE ARITHMETIC")
print("="*72)
for label,extra in [("Tier 1 only",0),("Tier 1 + disc",1.2),("Tier 1 + disc + CNP over 3 yr @0.5",1.2+1.5)]:
    tot=s1+extra
    print(f"  {label:34s} +{tot:5.1f} cm -> {h0+tot:6.1f} cm = {int((h0+tot)/2.54//12)}'{((h0+tot)/2.54)%12:4.1f}\"")
print(f"\n  TARGET needs +{need:.1f} cm -> {tgt} cm")
best=s1+1.2+1.5
print(f"  BEST DEFENSIBLE  = {h0+best:.1f} cm   SHORTFALL = {tgt-(h0+best):.1f} cm")
print(f"\n  And the empirical ceiling of the whole oestrogen-removal lever is 204 cm (R124),")
print(f"  so the target is NOT above what the biology permits — it is above what the")
print(f"  EVIDENCE currently supports FROM A BONE-AGE-16 START.")
print("\n"+"="*72)
print("THE ONE VARIABLE THAT DOMINATES EVERYTHING: TIME ON AI")
print("="*72)
print("  matched-pair study: >=2 yr anastrozole = +3.3 cm (p=0.044); 1 yr = +0.4 cm (p=0.730)")
print("  => the AI arm is BINARY on duration. Under 2 years it contributes NOTHING.")
print("  => every month of delay is subtracted directly from the largest defensible term.")
