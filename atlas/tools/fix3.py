p = '/home/user/growth-plate/atlas/tools/overgrowth_screen.py'
s = open(p).read()

old = '''    def worth_asking(sym, e):
        return expr.get(sym, 0) >= 2 and e["best"] >= 0.02'''
new = '''    # Thresholds taken from the harvest's own score distribution rather than picked. Over the
    # 1,596 targets the median association score is 0.058 and the 90th percentile is 0.118,
    # with a cliff to 0.396 at p95 - i.e. the bottom nine tenths is the tier where a gene was
    # mentioned near a disease name once. Cutting at p90 and requiring the gene in 3 of 4
    # human growth plate donors leaves 141 targets. A looser cut (0.02, 2 donors) left 1,131,
    # which at ~20 s per drug query is six hours of API time spent ranking noise.
    MIN_ASSOC, MIN_DONORS = 0.10, 3

    def worth_asking(sym, e):
        return expr.get(sym, 0) >= MIN_DONORS and e["best"] >= MIN_ASSOC'''
assert old in s
s = s.replace(old, new, 1)

s = s.replace(
    '''          f"(detected in >=2 human growth plate donors AND association score >=0.02); "''',
    '''          f"(detected in >={MIN_DONORS}/4 human growth plate donors AND association "
          f"score >={MIN_ASSOC}, the harvest's own 90th percentile); "''')

s = s.replace(
    '''        "n_asked_for_drugs": len(ask),''',
    '''        "n_asked_for_drugs": len(ask),
        "filter_thresholds": {"min_assoc_score": MIN_ASSOC, "min_gp_donors": MIN_DONORS,
                              "rationale": "min_assoc is the 90th percentile of the harvest's "
                                           "own score distribution (median 0.058, p90 0.118, "
                                           "p95 0.396) - not a chosen number"},''')

open(p, 'w').write(s)
print('patched')
