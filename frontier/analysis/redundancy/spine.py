h0,tgt=180.3,195.6; need=tgt-h0
print(f"need +{need:.1f} cm\n")
print("=== THE SPINE ACCOUNT, COSTED ===")
sit=h0*0.52
print(f"sitting height ~{sit:.1f} cm; spinal column ~70 cm of it; ~17 presacral vertebral units")
print("ring apophysis: median maturity ~22 yr (males); 98% fused by 21; some 24-25")
print("=> at hand-BA16 the spine has ~5-6 years of open account, the knee has ~0\n")
print("A. NATURAL spinal growth remaining, BA16 -> closure")
for yrs,v in [(5,0.4),(5,0.6),(6,0.5)]:
    print(f"   {yrs} yr at {v} cm/yr natural  = +{yrs*v:.1f} cm")
print("\nB. WITH THE CNP ARM (measured, spine-specific)")
print("   vosoritide sitting-height velocity increment: +0.89 +/- 1.05 cm/yr")
print("   NOTE: SD > mean. Noisy. Treat as 0 to +1.9, point est +0.89.")
for yrs in [4,5,6]:
    print(f"   {yrs} yr x 0.89 = +{yrs*0.89:.1f} cm  (range 0 to +{yrs*1.94:.1f})")
print("\nC. WITH AI EXTENDING RING-APOPHYSIS CLOSURE (oestrogen closes it; herrmann grew to 24)")
print("   if closure moves 22 -> 25, that is +3 yr on the SPINE account")
for v in [0.5,0.9,1.4]:
    print(f"   3 extra yr at {v} cm/yr = +{3*v:.1f} cm")
print("\nD. HUETER-VOLKMANN DISTRACTION (mechanical, spine)")
print("   children w/ distraction devices: 'extra gain in vertebral height growth vs")
print("   historical controls... growth in WIDTH diminished'  -> stimulation, not just preservation")
print("   magnitude in normal spines: NEVER MEASURED")
print("\nE. ADULT AXIAL UNLOADING - WEAK AND CONFOUNDED")
print("   +0.37 mm/vertebra (30.11->30.48, P=0.037); combined 28.51->28.83 (P=0.021)")
print("   200 pts BUT a FRACTURE cohort with instrumentation; authors: 'could not be concluded")
print("   that axial unloading promoted endochondral ossification'; mechanosensitivity declines")
print(f"   if +0.37 mm x 17 units = +{0.37*17/10:.2f} cm  <- UPPER BOUND, heavily confounded")
print("\nF. DISC - fusion independent")
print("   flotation +1.6 cm acute, ~1.2 cm persisting after 15 min upright")
print("\n=== SPINE-ONLY OPTIMISTIC SUM ===")
t=[("natural spinal remaining",2.5),("CNP arm on spine, 5 yr",4.45),
   ("AI extending closure, 3 yr",2.7),("disc",1.2)]
s=0
for n,v in t: s+=v; print(f"   +{v:5.2f}  {n}")
print(f"   ------\n   +{s:5.2f} cm from the SPINE alone -> {h0+s:.1f} cm = {int((h0+s)/2.54//12)}'{((h0+s)/2.54)%12:.1f}\"")
print(f"\n   vs target +{need:.1f}. Shortfall {need-s:.1f} cm.")
print("   AND THIS DOUBLE-COUNTS NOTHING FROM THE LEG - the knee arms are additive on top.")
