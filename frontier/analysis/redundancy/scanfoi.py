from pypdf import PdfReader
import re, sys
r = PdfReader(sys.argv[1])
pat = re.compile(sys.argv[2], re.I)
for i, p in enumerate(r.pages):
    t = ' '.join((p.extract_text() or '').split())
    if pat.search(t):
        print('--- p%d: %s' % (i + 1, t[:240]))
