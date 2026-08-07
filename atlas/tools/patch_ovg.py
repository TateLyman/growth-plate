p='/home/user/growth-plate/atlas/tools/overgrowth_screen.py'
s=open(p).read()
old='''    expr, atlas = gp_expression(), atlas_genes()
    dcache = cache_load("drugs.json") or {}
    rows = []
    for i, (sym, e) in enumerate(sorted(tgt.items(), key=lambda x: -x[1]["best"]), 1):'''
new='''    expr, atlas = gp_expression(), atlas_genes()
    dcache = cache_load("drugs.json") or {}

    # The knownDrugs query costs ~20 s per target against this API, so asking it of all 1,596
    # harvested genes takes eight hours. It is also the wrong order of operations: a gene not
    # present in a human growth plate is not a lead whatever drugs exist for it. So the
    # expensive call is made ONLY for genes that clear the free local filters first. Genes that
    # do not clear them are still written out, with n_known_drugs left BLANK rather than zero -
    # blank means NOT ASKED, and conflating that with "no drug exists" would quietly turn an
    # unrun query into a negative result.
    def worth_asking(sym, e):
        return expr.get(sym, 0) >= 2 and e["best"] >= 0.02

    ask = [s_ for s_, e_ in tgt.items() if worth_asking(s_, e_)]
    print(f"{len(ask)} of {len(tgt)} targets clear the free filters "
          f"(detected in >=2 human growth plate donors AND association score >=0.02); "
          f"only these get the drug query", flush=True)

    rows = []
    for i, (sym, e) in enumerate(sorted(tgt.items(), key=lambda x: -x[1]["best"]), 1):
        asked = worth_asking(sym, e)'''
assert old in s; s=s.replace(old,new,1)
old2='''        if sym in dcache:
            drugs = [tuple(d) for d in dcache[sym]]
        else:'''
new2='''        if not asked:
            drugs = None
        elif sym in dcache:
            drugs = [tuple(d) for d in dcache[sym]]
        else:'''
assert old2 in s; s=s.replace(old2,new2,1)
old3='''        seen, uniq = set(), []
        for d in drugs:'''
new3='''        seen, uniq = set(), []
        for d in (drugs or []):'''
assert old3 in s; s=s.replace(old3,new3,1)
old4='''            "n_known_drugs": len(uniq),
            "max_phase": max([d[2] or 0 for d in uniq], default=""),'''
new4='''            "n_known_drugs": len(uniq) if drugs is not None else "",
            "max_phase": (max([d[2] or 0 for d in uniq], default="")
                          if drugs is not None else ""),'''
assert old4 in s; s=s.replace(old4,new4,1)
s=s.replace('''    triple = [r for r in rows if r["gp_donors_detected"] not in ("", 0)
              and r["n_known_drugs"] > 0]''','''    triple = [r for r in rows if r["gp_donors_detected"] not in ("", 0)
              and isinstance(r["n_known_drugs"], int) and r["n_known_drugs"] > 0]''')
s=s.replace('''        "n_with_a_known_drug": sum(1 for r in rows if r["n_known_drugs"] > 0),''',
            '''        "n_asked_for_drugs": len(ask),
        "n_with_a_known_drug": sum(1 for r in rows if isinstance(r["n_known_drugs"], int)
                                   and r["n_known_drugs"] > 0),
        "BLANK_n_known_drugs_MEANS": "the drug query was NOT RUN for this gene because it did "
                                     "not clear the free filters. It does not mean no drug "
                                     "exists.",''')
s=s.replace("""          f" expressed in human growth plate | {sum(1 for r in rows if r['n_known_drugs']>0)}\"""",
            """          f" expressed in human growth plate | "
          f"{sum(1 for r in rows if isinstance(r['n_known_drugs'],int) and r['n_known_drugs']>0)}\"""")
s=s.replace('''        if i % 25 == 0:
            print(f"  annotated {i}/{len(tgt)}", flush=True)''',
            '''        if asked and i % 10 == 0:
            print(f"  {i}/{len(tgt)} scanned", flush=True)''')
open(p,'w').write(s); print('patched')
