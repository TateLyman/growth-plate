import openpyxl
wb = openpyxl.load_workbook('media2_4.xlsx', read_only=True, data_only=True)

def sheet(name):
    ws = wb[name]
    rows = [list(r) for r in ws.iter_rows(values_only=True)]
    return rows

def show(name, hdr_row=1, cols=None, filt=None, maxn=None):
    rows = sheet(name)
    hdr = [str(x) if x is not None else '' for x in rows[hdr_row]]
    idx = list(range(len(hdr))) if cols is None else [hdr.index(c) for c in cols if c in hdr]
    print("HEADER:", [hdr[i] for i in idx])
    n = 0
    for r in rows[hdr_row+1:]:
        if r[0] is None: continue
        if filt and not filt(r, hdr): continue
        print("  ", " | ".join(str(r[i])[:26] if r[i] is not None else '' for i in idx))
        n += 1
        if maxn and n >= maxn: break
    print("  (%d rows shown)" % n)

print("#" * 78)
print("TABLE S5 -- THE GENE-BASED SINGLETON pLoF SET (the '17')")
print("#" * 78)
rows = sheet('Table S5')
print("full header:", [str(x)[:40] for x in rows[1]])
print()
for r in rows[2:]:
    if r[0] is None: continue
    print("  ", [str(x)[:20] if x is not None else '' for x in r])

print()
print("#" * 78)
print("TABLE S7 -- singleton pLoF vs GWAS effect ratio")
print("#" * 78)
rows = sheet('Table S7')
print("header:", [str(x)[:45] for x in rows[1]])
for r in rows[2:]:
    if r[0] is None: continue
    print("  ", [str(x)[:22] if x is not None else '' for x in r])

print()
print("#" * 78)
print("TABLE S4 -- are our candidates among the 207?")
print("#" * 78)
rows = sheet('Table S4')
hdr = [str(x) if x is not None else '' for x in rows[1]]
print("header:", hdr)
want = {"NRK", "TET1", "SPIN4", "MTOR", "CHD8", "ZFAT", "LCORL", "FBN1", "ACAN", "SPIN1",
        "PTEN", "AKT1", "CSNK2A1", "NSD1", "EZH2", "DNMT3A", "CXXC5", "FGFR3", "NPR2", "STC2"}
found = set()
for r in rows[2:]:
    if r[0] is None: continue
    if str(r[0]) in want:
        found.add(str(r[0]))
        print("  ", [str(x)[:22] if x is not None else '' for x in r[:14]])
print()
print("PRESENT in the 207:", sorted(found))
print("ABSENT  from the 207:", sorted(want - found))
