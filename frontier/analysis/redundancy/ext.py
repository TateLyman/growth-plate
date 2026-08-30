from pypdf import PdfReader
import sys,re
r=PdfReader(sys.argv[1])
a=int(sys.argv[2]) if len(sys.argv)>2 else 0
b=int(sys.argv[3]) if len(sys.argv)>3 else len(r.pages)
for i in range(a,min(b,len(r.pages))):
    t=r.pages[i].extract_text() or ''
    t=re.sub(r'\n{3,}','\n\n',t)
    print('\n========== p%d =========='%(i+1)); print(t)
