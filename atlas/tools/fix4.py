p = '/home/user/growth-plate/atlas/tools/overgrowth_screen.py'
s = open(p).read()

# 1. the query itself. Target.knownDrugs no longer exists on this API; it is now
#    drugAndClinicalCandidates, with mechanism of action nested under the drug.
old_q = """DRUGS = ('query($id:String!){target(ensemblId:$id){approvedSymbol '
         'knownDrugs(size:25){count rows{drugId prefName mechanismOfAction phase status '
         'drugType}}}}')"""
new_q = '''DRUGS = ('query($id:String!){target(ensemblId:$id){approvedSymbol '
         'drugAndClinicalCandidates{count rows{maxClinicalStage drug{id name drugType '
         'mechanismsOfAction{rows{mechanismOfAction actionType}}}}}}}')

# The positive control. This screen once reported "0 with a known drug" across all 141 genes
# it asked about, which was not a result: Target.knownDrugs had been removed from the API, so
# every call returned HTTP 400, and a bare `except Exception: pass` turned each 400 into an
# empty drug list. A silent zero is indistinguishable from a real negative, and this project
# has already been bitten by exactly that once (the mTOR control in target_screen.py that
# produced no rows and was read as passing). So the query is now run against a gene whose
# answer is known before any real work happens, and the run HALTS if it does not come back.
CONTROL_ENSEMBL = "ENSG00000137869"          # CYP19A1
CONTROL_EXPECT = "ANASTROZOLE"               # among its approved inhibitors'''
assert old_q in s
s = s.replace(old_q, new_q, 1)

# 2. stop swallowing failures. A failed query must be distinguishable from an empty answer.
old_h = '''        if not asked:
            drugs = None
        elif sym in dcache:
            drugs = [tuple(d) for d in dcache[sym]]
        else:
            drugs = []
            try:
                kd = gql(DRUGS, {"id": e["ensembl"]})["data"]["target"]
                for r in (kd or {}).get("knownDrugs", {}).get("rows", []) or []:
                    drugs.append((r.get("prefName"), r.get("mechanismOfAction"), r.get("phase")))
            except Exception:
                pass
            dcache[sym] = drugs
            if i % 20 == 0:
                cache_save("drugs.json", dcache)'''
new_h = '''        if not asked:
            drugs = None
        elif sym in dcache:
            drugs = [tuple(d) for d in dcache[sym]]
        else:
            drugs = fetch_drugs(e["ensembl"])
            if drugs is None:                 # the query FAILED - do not cache it as empty
                n_query_failures[0] += 1
            else:
                dcache[sym] = drugs
                if i % 20 == 0:
                    cache_save("drugs.json", dcache)'''
assert old_h in s
s = s.replace(old_h, new_h, 1)

# 3. the fetch helper, and the control that gates the run
old_f = '''def gp_expression():'''
new_f = '''def fetch_drugs(ensembl):
    """[(drug name, mechanism, max clinical stage), ...] or None if the QUERY FAILED.

    None and [] mean different things and the caller must not conflate them: [] is "this gene
    has no drug", None is "we did not find out". Returning [] on error is how this screen
    previously reported a clean zero across every gene it asked about.
    """
    try:
        d = gql(DRUGS, {"id": ensembl})
    except Exception:
        return None
    if not isinstance(d, dict) or d.get("errors") or not (d.get("data") or {}).get("target"):
        return None
    out = []
    for r in ((d["data"]["target"].get("drugAndClinicalCandidates") or {}).get("rows") or []):
        drug = r.get("drug") or {}
        moa = [m.get("mechanismOfAction")
               for m in ((drug.get("mechanismsOfAction") or {}).get("rows") or [])]
        out.append((drug.get("name"), moa[0] if moa else None, r.get("maxClinicalStage")))
    return out


def positive_control():
    """Halt the run unless a gene with a known answer comes back with it."""
    got = fetch_drugs(CONTROL_ENSEMBL)
    if got is None:
        return False, "the control query itself failed"
    names = {(n or "").upper() for n, _, _ in got}
    if CONTROL_EXPECT not in names:
        return False, f"CYP19A1 returned {len(got)} drugs and {CONTROL_EXPECT} was not among them"
    return True, f"CYP19A1 -> {len(got)} drugs including {CONTROL_EXPECT}"


def gp_expression():'''
assert old_f in s
s = s.replace(old_f, new_f, 1)

# 4. wire the control and the failure counter into main()
old_m = '''    expr, atlas = gp_expression(), atlas_genes()
    dcache = cache_load("drugs.json") or {}'''
new_m = '''    ok, msg = positive_control()
    print(f"\\npositive control: {msg}")
    if not ok:
        print("HALTING. The drug query does not work, so every gene would be reported as "
              "having no drug and the screen would return a clean, wrong negative.")
        return 1

    expr, atlas = gp_expression(), atlas_genes()
    dcache = cache_load("drugs.json") or {}
    n_query_failures = [0]'''
assert old_m in s
s = s.replace(old_m, new_m, 1)

# 5. surface failures rather than hiding them
s = s.replace('''    cache_save("drugs.json", dcache)''',
              '''    cache_save("drugs.json", dcache)
    if n_query_failures[0]:
        print(f"\\nWARNING: {n_query_failures[0]} drug queries FAILED and are reported as blank, "
              f"not as zero.")''', 1)
s = s.replace('''        "n_asked_for_drugs": len(ask),''',
              '''        "n_asked_for_drugs": len(ask),
        "n_drug_queries_failed": n_query_failures[0],
        "positive_control": msg,''', 1)

open(p, 'w').write(s)
print('patched')
