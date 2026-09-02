# What multiplier k on (A x h_term) is needed for the target, given N is fixed at BA16?
h0, target = 180.3, 195.6          # 5'11" -> 6'5"
need = target - h0
for pct in [0.988, 0.991, 0.993]:   # Bayley-Pinneau male SA 16.0 / 16.5 / 17.0
    rem = h0/pct - h0
    print(f"BP {pct:.3f}  remaining={rem:5.2f} cm   k needed = {need/rem:6.2f}x")
print()
print(f"need = {need:.1f} cm")
# what the corpus supports for k
for name,k in [("CNP analogue alone (meta, +1.24cm/52wk on ~5cm/yr)",1.25),
               ("LB-100 + BMN-111 ex vivo growth ratio",2.06),
               ("NPR3-LOF human velocity 8.9 vs ~5.5 expected",1.62),
               ("optimistic full stack, log-additive of 1.6 x 1.3 x 1.25",1.6*1.3*1.25)]:
    for pct in [0.988]:
        rem = h0/pct - h0
        print(f"  k={k:4.2f}  {name:52s} -> +{rem*k:5.2f} cm -> {h0+rem*k:6.1f} cm")
