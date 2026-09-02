h0, tgt = 180.3, 195.6
need = tgt - h0
print(f"TARGET: {h0} -> {tgt} cm   need +{need:.1f} cm\n")
print("=== FRAMING A: MULTIPLIER ON A FIXED REMAINDER (what R115-R120 used) ===")
rem = h0/0.988 - h0
print(f"  BP male SA16.0 = 98.8%  ->  remaining {rem:.2f} cm")
print(f"  k required = {need/rem:.2f}x     <- 'impossible' framing\n")
print("=== FRAMING B: DURATION x RATE (what the human existence-proofs actually are) ===")
print("  gain = velocity (cm/yr) x years the plate keeps producing")
for v in [1.5,2.0,2.5,3.0,4.0,5.0]:
    print(f"   at {v:.1f} cm/yr -> need {need/v:5.1f} years of sustained growth")
print()
print("  OBSERVED IN HUMANS, from a LATE start:")
print("   herrmann2002 (aromatase-null): 170 cm @14  ->  197 cm @24   = +27.0 cm over 10 yr = 2.70 cm/yr")
print("   ESR1-null man: bone age 15 -> 17.5 over 3.5 chronological yr = 0.71 BA-yr per yr")
print("   Lauffer NPR3-LOF proband: 172.1 @10 -> 205.1 @14.7 = +33.0 cm over 4.7 yr = 7.02 cm/yr")
print(f"\n   => +{need:.1f} cm at herrmann's 2.70 cm/yr = {need/2.70:.1f} years")
print("   => THE TARGET IS ~5.7 YEARS OF OESTROGEN-NULL-RATE GROWTH. NOT A 7-FOLD DRUG EFFECT.\n")
print("=== FRAMING C: COMPARTMENTS ARE SEPARATE ACCOUNTS THAT CLOSE AT DIFFERENT TIMES ===")
sit = h0*0.52; leg = h0-sit
print(f"  sitting height ~{sit:.1f} cm | leg ~{leg:.1f} cm  (52% ratio)")
print("  closure: distal femur/proximal tibia ~BA16-17 | VERTEBRAL RING APOPHYSIS median ~22 yr (males)")
print("           98% of rings fused only by 21; some to 24-25")
print("  => at hand-BA 16 the LEG budget is ~spent; the SPINE has ~5-6 more years")
print("  => aeppli2025 proves independence: post knee-epiphysiodesis girls gained")
print("     8.0 +/- 0.5 cm SITTING height and 0.2 +/- 0.4 cm LEG\n")
print("=== FRAMING D: THE DISC IS NOT GROWTH AND IS NOT FUSION-LIMITED ===")
print("  disc ~25% of spinal column height; set by osmotic swelling vs load")
print("  marcoslorenzo2026: 4 h hyper-buoyancy flotation = +1.6 +/- 0.5 cm stature")
print("    only -0.4 +/- 0.3 cm reversed in 15 min upright -> ~1.2 cm persisting")
print("    passive vertebral stiffness fell across ENTIRE column and STAYED below baseline")
print("  adult circadian swing 19.3 mm (1.1% of stature)\n")
print("=== HONEST CEILING, SUMMED, OPTIMISTIC ===")
terms=[("natural remaining at BA16",2.19,"BP"),
       ("stack multiplier on that (2.6x, unproven)",2.19*1.6,"k=2.6 -> +1.6x over natural"),
       ("disc / decompression (fusion-independent)",1.4,"flotation, persisting fraction"),
       ("N-raising, IF it converts (no length endpoint exists)",3.0,"speculative upper bound")]
tot=0
for n,v,src in terms:
    tot+=v; print(f"   +{v:5.2f} cm   {n:52s} [{src}]")
print(f"   ------\n   +{tot:5.2f} cm  ->  {h0+tot:.1f} cm = {int((h0+tot)/2.54//12)}'{((h0+tot)/2.54)%12:.1f}\"")
print(f"\n   TARGET {tgt} cm needs +{need:.1f}. Optimistic sum reaches +{tot:.1f}. SHORTFALL {need-tot:.1f} cm.")
print("\n   AND THE SHORTFALL IS ENTIRELY THE DURATION TERM:")
print(f"   +{need-tot:.1f} cm at 2.7 cm/yr = {(need-tot)/2.7:.1f} extra years of open, producing plate.")
