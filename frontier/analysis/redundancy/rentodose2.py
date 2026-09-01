"""The exposure axis cancels: at ANY dose that lands Wnt in the SPIN4 window,
NRK engagement is fixed by relative affinity alone.

Hill n=1, one exposure A, two targets:
    E_wnt = A/(A+Kt)        E_nrk = A/(A+Kn),  Kn = Kt/f,  f = Kt/Kn <= 1
=>  E_nrk = f*E_wnt / (1 - E_wnt + f*E_wnt)     -- A DROPS OUT ENTIRELY.
"""
W = (0.38, 0.45)   # SPIN4 calibration constant (Lui 2023 Fig 6C/6D)

def nrk_at(Ew, f): return f*Ew / (1 - Ew + f*Ew)
def wnt_for_nrk(En, f):                      # invert
    r = En/(1-En)/f
    return r/(r+1)

print("="*92)
print("STEP 4 -- THE EXPOSURE AXIS CANCELS.  NRK engagement AT the Wnt window is")
print("          a function of relative affinity ONLY -- no dose can change it.")
print("="*92)
print("  %-20s %-26s %s" % ("f = IC50(TNIK)/IC50(NRK)", "NRK engagement at Wnt 38-45%", "verdict"))
print("  "+"-"*84)
for f in [1.0, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05]:
    lo, hi = 100*nrk_at(W[0], f), 100*nrk_at(W[1], f)
    v = ("BOTH ARMS ENGAGED" if lo >= 30 else
         "partial - marginal" if lo >= 15 else "NRK arm effectively dead")
    print("  %-20s %-26s %s" % ("%.2f" % f, "%.1f%% - %.1f%%" % (lo, hi), v))
print()
print("  -> equipotent (f=1) is the ONLY case where one dose serves both arms.")
print("     At f=0.3 -- a middling off-target -- NRK sits at 15-19%, less than half")
print("     the Wnt effect, and that is the ceiling, not a dosing choice.")

print()
print("="*92)
print("STEP 5 -- RUN IT BACKWARDS: what Wnt suppression is the PRICE of a real NRK effect?")
print("="*92)
print("  %-20s %-24s %-24s %s" % ("f", "Wnt needed for NRK 30%", "Wnt needed for NRK 50%", "regime at NRK 50%"))
print("  "+"-"*90)
for f in [1.0, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05]:
    w30, w50 = 100*wnt_for_nrk(0.30, f), 100*wnt_for_nrk(0.50, f)
    reg = ("inside SPIN4 window" if W[0]*100 <= w50 <= W[1]*100 else
           "PAST the window -> ICAT/Col2a1 regime (SHORTENS bone)")
    print("  %-20s %-24s %-24s %s" % ("%.2f" % f, "%.1f%%" % w30, "%.1f%%" % w50, reg))
print()
print("  -> R137's ladder: Spin4 loss (38-45%) +5.06%, Cxxc5-/- +3.8% LENGTHEN;")
print("     everything deeper (ICAT, Ctnnb1 cKO, Lrp5/6) SHORTENS, CLOSES or KILLS.")
print("     Any f below ~0.9 forces you past the window to buy NRK.")

print()
print("="*92)
print("STEP 6 -- EXPECTED VALUE, folding in R147's binding probability")
print("="*92)
PBIND = 0.70                      # R147 calibrated estimate
prior = [(1.0,0.15),(0.5,0.25),(0.2,0.30),(0.1,0.20),(0.05,0.10)]   # given it binds
ev = sum(p*nrk_at(0.415, f) for f, p in prior)
print("  P(rentosertib engages NRK at all)          = %.0f%%   (R147, pocket-identity calibrated)" % (100*PBIND))
print("  E[NRK engagement | binds, Wnt at 41.5%%]    = %.1f%%" % (100*ev))
print("  E[NRK engagement | unconditional]          = %.1f%%" % (100*PBIND*ev))
print()
print("  P(f >= 0.9, i.e. the one case that serves both arms) = P(bind) x P(near-equipotent)")
print("     = %.2f x ~0.15 = %.0f%%" % (PBIND, 100*PBIND*0.15))
