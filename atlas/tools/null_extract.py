"""Pull height, age, sex and treatment status out of the abstracts, and separate
CASE REPORTS OF PATIENTS from everything else. Then classify each male case as an
ENDPOINT (grew to a stop) or a CENSORED observation (stopped by treatment)."""
import json, re, csv
d=json.load(open("null_census.raw.json"))
HT   = re.compile(r'(\d{2,3}(?:\.\d)?)\s*cm\b')
AGE  = re.compile(r'\b(\d{1,2}(?:\.\d)?)[- ]?(?:year|yr|y)[- ]?old\b', re.I)
BA   = re.compile(r'bone age[^.]{0,60}?(\d{1,2}(?:\.\d)?)\s*(?:year|yr|y)', re.I)
TREAT= re.compile(r'(estradiol|oestradiol|estrogen|oestrogen|conjugated equine|ethinyl)[^.]{0,90}?'
                  r'(epiphys|clos|fus|to (?:prevent|stop|halt|arrest)|height)', re.I)
CLOSE= re.compile(r'(for epiphyseal closure|to prevent further increase in height|to close the (?:growth plate|epiphys)|'
                  r'epiphyseal closure was (?:achieved|induced)|induce epiphyseal (?:closure|fusion))', re.I)
OPEN = re.compile(r'(open epiphys|unfused|incomplete (?:epiphyseal )?closure|epiphyses (?:were|remained) open|'
                  r'continued (?:linear )?growth|progressive increase in height|still growing|tall stature)', re.I)
MALE = re.compile(r'\b(male|man|boy|46,?\s?XY)\b', re.I)
CASE = re.compile(r'\b(case report|we (?:report|present|describe)|a \d{1,2}[- ]year[- ]old|proband|patient)\b', re.I)

rows=[]
for k,v in d.items():
    ab=v["abs"] or ""; t=v["title"] or ""
    txt=t+" "+ab
    if not ab: continue
    kinds=set(v["found_by"])
    is_arom = "CYP19A1_male" in kinds or "CYP19A1_any" in kinds
    is_esr1 = "ESR1_lof" in kinds
    if not (is_arom or is_esr1): continue
    if not re.search(r'aromatase deficien|CYP19A1|estrogen (receptor|resistance|insensitivity)|ESR1', txt, re.I): continue
    if not CASE.search(txt): continue
    hts=[float(x) for x in HT.findall(txt) if 100 <= float(x) <= 230]
    ages=[float(x) for x in AGE.findall(txt)]
    rows.append(dict(pmid=v["pmid"], yr=v["yr"], oa=v["oa"], title=t[:110],
        cls="aromatase" if is_arom and not is_esr1 else ("ESR1" if is_esr1 and not is_arom else "both"),
        male=bool(MALE.search(txt)),
        heights=sorted(set(hts))[:4], max_ht=max(hts) if hts else None,
        ages=sorted(set(ages))[:4], bone_age=BA.search(txt).group(1) if BA.search(txt) else None,
        treated_to_close=bool(CLOSE.search(txt)),
        any_estrogen_tx=bool(TREAT.search(txt)),
        still_open=bool(OPEN.search(txt)),
        auth=v["auth"][:44], journal=(v["journal"] or "")[:30]))
rows.sort(key=lambda r:(-(r["max_ht"] or 0)))
print(f"{len(rows)} case-like records mentioning aromatase deficiency or ESR1 loss\n")
male = [r for r in rows if r["male"] and r["max_ht"]]
print(f"=== MALE CASES WITH A HEIGHT IN THE ABSTRACT: {len(male)} ===")
print(f"{'PMID':<10} {'yr':<5} {'class':<10} {'ht(cm)':>7} {'BA':>5} {'closed?':<8} {'open?':<6} title")
for r in male:
    print(f"{str(r['pmid']):<10} {str(r['yr']):<5} {r['cls']:<10} {r['max_ht']:>7.1f} "
          f"{str(r['bone_age'] or '-'):>5} {'TREATED' if r['treated_to_close'] else '-':<8} "
          f"{'OPEN' if r['still_open'] else '-':<6} {r['title'][:62]}")
json.dump(rows, open("null_cases.json","w"), indent=1)
with open("null_cases.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["pmid","year","class","male","max_height_cm","all_heights","ages","bone_age",
                                 "treated_for_closure","any_estrogen_tx","described_open_or_growing","open_access","journal","title"])
    for r in rows: w.writerow([r["pmid"],r["yr"],r["cls"],r["male"],r["max_ht"],r["heights"],r["ages"],
                               r["bone_age"],r["treated_to_close"],r["any_estrogen_tx"],r["still_open"],
                               r["oa"],r["journal"],r["title"]])
print(f"\nof those male cases: {sum(1 for r in male if r['treated_to_close'])} explicitly treated FOR CLOSURE, "
      f"{sum(1 for r in male if r['still_open'])} described as open/still growing")
