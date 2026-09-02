import sys, re
from xml.etree import ElementTree as ET

def txt(e):
    return "".join(e.itertext())

p = sys.argv[1]
t = ET.parse(p); r = t.getroot()
for sec in r.iter():
    pass
# title
for a in r.iter('article-title'):
    print("TITLE:", " ".join(txt(a).split())); break
print("="*70)
body = r.find('.//body')
if body is None:
    print("NO BODY")
else:
    for sec in body.iter():
        if sec.tag in ('title',):
            print("\n## ", " ".join(txt(sec).split()))
        elif sec.tag == 'p':
            s = " ".join(txt(sec).split())
            if s: print(s)
print("\n"+"="*70+"\nFIGURE/TABLE CAPTIONS\n")
for f in r.iter('fig'):
    lab = f.find('label'); cap = f.find('caption')
    print("[", txt(lab) if lab is not None else "", "]", " ".join(txt(cap).split()) if cap is not None else "")
    print()
