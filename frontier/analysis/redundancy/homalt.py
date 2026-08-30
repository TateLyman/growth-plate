import openpyxl
wb = openpyxl.load_workbook('media2_4.xlsx', read_only=True, data_only=True)
rows = [list(r) for r in wb['Table S5'].iter_rows(values_only=True)]
hdr = [str(x) if x is not None else '' for x in rows[1]]
def col(name): return hdr.index(name)

cE = col('Effect (cm) (discovery+replication)')
cP = col('P-value (discovery+replication)')
cHo = col('HomRef individuals (discovery+replication)')
cHe = col('Het individuals (discovery+replication)')
cHa = col('HomAlt individuals (discovery+replication)')
cChr = col('Chr')

out = []
for r in rows[2:]:
    if r[0] is None: continue
    out.append((float(r[cE]), r[0], r[cChr], r[cHe], r[cHa], r[cP]))
out.sort(reverse=True)

print("THE 17 SINGLETON pLoF GENES -- combined discovery+replication (1.45M exomes)")
print("%-10s %4s %10s %8s %10s   %s" % ("gene", "chr", "effect cm", "het", "HOM/HEMI", "P"))
print("-" * 68)
for e, g, c, he, ha, p in out:
    star = "   <<<< HOMOZYGOUS/HEMIZYGOUS NULLS EXIST" if ha and int(ha) > 0 else ""
    print("%-10s %4s %+10.2f %8s %10s   %-9s%s" % (g, c, e, he, ha, p, star))

pos = [o for o in out if o[0] > 0]
print()
print("POSITIVE (loss -> TALLER): %d of %d  -> %s" % (len(pos), len(out), ", ".join(o[1] for o in pos)))
tot_ha = sum(int(o[4]) for o in out if o[4])
print("Total homozygous/hemizygous null individuals across ALL 17 genes: %d" % tot_ha)
for o in out:
    if o[4] and int(o[4]) > 0:
        print("   -> ALL of them are in %s (chr %s)" % (o[1], o[2]))
