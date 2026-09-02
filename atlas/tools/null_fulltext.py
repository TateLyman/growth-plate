"""Read the full texts. For every MALE case of aromatase deficiency or ESR1 loss,
recover: height, age at that height, bone age, whether epiphyses were open, and
WHETHER OESTROGEN WAS GIVEN TO CLOSE THEM.

The classification that matters:
  ENDPOINT  - growth stopped on its own, height is a final height
  CENSORED  - oestrogen was given and the plate was closed deliberately
  OPEN      - last seen still growing, no closure achieved or possible
"""
import glob, re, json, collections
HT   = re.compile(r'(\d{2,3}(?:\.\d)?)\s*cm\b')
CLOSE= re.compile(r'(for epiphyseal closure|to (?:prevent|stop|halt|arrest) (?:further )?(?:increase in )?(?:linear )?'
                  r'(?:growth|height)|to (?:close|induce closure of) the (?:growth plates?|epiphys\w+)|'
                  r'induce (?:epiphyseal )?(?:closure|fusion)|epiphyseal closure was (?:then )?(?:achieved|induced|obtained))', re.I)
ESTX = re.compile(r'\b(ethinyl ?(?:o?estradiol)|o?estradiol (?:valerate|patch|gel|transdermal)|conjugated (?:equine )?o?estrogens?|'
                  r'o?estrogen (?:replacement|therapy|treatment)|o?estradiol (?:was|were) (?:started|initiated|given|administered))', re.I)
OPEN = re.compile(r'(open epiphys\w*|unfused epiphys\w*|epiphys\w* (?:were|remained|are) (?:still )?open|'
                  r'incomplete (?:epiphyseal )?(?:closure|fusion)|continued (?:linear )?growth|'
                  r'progressive increase in height|growth plates? (?:were|remained) open)', re.I)
FINAL= re.compile(r'(final height|adult height|reached (?:his|her) (?:final|adult) height|growth (?:had )?ceased|'
                  r'epiphyses (?:were )?(?:fully )?(?:closed|fused))', re.I)
MALE = re.compile(r'\b(male|man|boy|46,?\s?XY)\b', re.I)

out=[]
for f in sorted(glob.glob("nullft/*.xml")):
    pmid=f.split("/")[-1].split("_")[0]
    t=open(f,encoding="utf-8",errors="replace").read()
    body=re.sub(r"<[^>]+>"," ",t); body=re.sub(r"\s+"," ",body)
    title=(re.search(r"<article-title>(.*?)</article-title>",t,re.S) or [None,""])[1]
    title=re.sub(r"<[^>]+>","",title)[:110] if title else ""
    if not re.search(r'aromatase deficien|CYP19A1|estrogen (?:receptor|resistance|insensitiv)|ESR1', body, re.I):
        continue
    hts=sorted({float(x) for x in HT.findall(body) if 140<=float(x)<=230}, reverse=True)
    out.append(dict(pmid=pmid, title=title, male=bool(MALE.search(body)),
        heights=hts[:6], max_ht=hts[0] if hts else None,
        closed_deliberately=bool(CLOSE.search(body)),
        estrogen_given=bool(ESTX.search(body)),
        described_open=bool(OPEN.search(body)),
        mentions_final=bool(FINAL.search(body)),
        close_quote=(CLOSE.search(body).group(0)[:80] if CLOSE.search(body) else "")))
json.dump(out, open("null_fulltext.json","w"), indent=1)

male=[r for r in out if r["male"] and r["max_ht"]]
male.sort(key=lambda r:-r["max_ht"])
print(f"{len(out)} full texts read; {len(male)} male cases with a height\n")
print(f"{'PMID':<10} {'maxHt':>6} {'E2 given':<9} {'closed on purpose':<18} {'open?':<6} title")
for r in male:
    print(f"{r['pmid']:<10} {r['max_ht']:>6.1f} {'YES' if r['estrogen_given'] else '-':<9} "
          f"{'YES' if r['closed_deliberately'] else '-':<18} {'OPEN' if r['described_open'] else '-':<6} {r['title'][:56]}")
print()
n_e   = sum(1 for r in male if r["estrogen_given"])
n_cl  = sum(1 for r in male if r["closed_deliberately"])
n_op  = sum(1 for r in male if r["described_open"])
print(f"of {len(male)} male cases with a height:")
print(f"  {n_e} were given oestrogen")
print(f"  {n_cl} state explicitly that it was given TO CLOSE THE PLATES or stop growth")
print(f"  {n_op} are described with OPEN epiphyses or continuing growth")
print("\nverbatim closure statements found:")
for r in male:
    if r["close_quote"]: print(f"  [{r['pmid']}] ...{r['close_quote']}...")
