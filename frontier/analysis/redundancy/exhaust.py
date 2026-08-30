print("=== IS NORMAL FUSION PREMATURE RELATIVE TO THE POOL? ===")
print("  normal male: fuses BA ~17-18 at ~176 cm")
print("  herrmann2002 oestrogen-null: 170 @14 -> 197 @24, plates STILL OPEN at 27")
print("  ESR1-null: BA 15 at ~28, unfused at 31, still gaining in 3rd decade")
print("  => a plate can keep PRODUCING for a decade past normal fusion age.")
print("  => NORMAL CLOSURE STRANDS BUDGET. The operator's reframe is correct.\n")
print("=== BUT DOES 'SPEND IT FAST' FOLLOW? THE RATE-YIELD LAW SAYS NO ===")
print("  R360/hunziker1994: A proportional to throughput^-0.150")
for x in [2,3,5,10]:
    a=x**-0.150
    print(f"   {x}x throughput -> amplification x {a:.3f}  => TOTAL height from a fixed pool x {a:.3f} ({(a-1)*100:+.1f}%)")
print("  => in a pure BUDGET regime, speed COSTS total height. 5x throughput costs 21%.")
print("  => 'spend fast' is WRONG on the arithmetic. 'spend COMPLETELY' is RIGHT.\n")
print("=== THE CORRECT DISCRIMINATOR ===")
print("  NOT 'does it spend the pool' -- spending the pool is the ONLY way pool becomes height.")
print("  IT IS 'does it advance BONE AGE'. Anything that converts pool->height without")
print("  advancing bone age is pure gain. Anything that converts pool->bone age is pure loss.\n")
print("=== AGENTS SCORED ON THAT CRITERION ===")
rows=[("anastrozole (AI)","BA SLOWED ~24% (1.37 vs 1.81, p=0.001)","YES - and preserves yield/division"),
      ("GH 0.24-0.37 mg/kg/wk","BA NEUTRAL (not vs 0.24; 0.5 DOES advance)","YES"),
      ("oxandrolone","'bone age did NOT accelerate'; GH+oxa = greater final height, NO rise in bone maturation","YES"),
      ("vosoritide / CNP","BA-to-chrono ratio UNMOVED (dauber2026)","YES"),
      ("erdafitinib / FGFR3i","*** UNMEASURED *** - no BA endpoint in the infigratinib ph3 readout","UNKNOWN - FLAG"),
      ("testosterone / aromatisable androgen","AROMATISES to E2 -> advances BA","NO"),
      ("GH >=0.5 mg/kg/wk","advances pubertal onset AND bone maturation","NO")]
for a,b,c in rows: print(f"   {a:34s} | {b:62s} | {c}")
print("\n=== WHAT THIS RETRACTS ===")
print("  R117 flagged the CNP arm as CONTRAINDICATED because 'CNP converts N into A --")
print("  the GH failure mode'. THAT WAS WRONG-HEADED. Converting N into height is the")
print("  OBJECTIVE. The failure mode is converting N into BONE AGE, not into height.")
