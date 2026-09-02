import pymupdf, pytesseract, io
from PIL import Image
p='/root/.claude/uploads/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/ed9e5a3c-02_FDA_PTH1R_reviews_4up.pdf'
d=pymupdf.open(p)
out=[]
for i,pg in enumerate(d):
    pix=pg.get_pixmap(dpi=300)
    img=Image.open(io.BytesIO(pix.tobytes('png')))
    w,h=img.size
    # 4-up: split into quadrants, OCR each separately for better accuracy
    quads=[(0,0,w//2,h//2),(w//2,0,w,h//2),(0,h//2,w//2,h),(w//2,h//2,w,h)]
    txt=[]
    for qi,q in enumerate(quads):
        txt.append('--- sheet %d quad %d ---\n'%(i+1,qi+1)+pytesseract.image_to_string(img.crop(q)))
    out.append('\n\n===== SHEET %d =====\n'%(i+1)+'\n'.join(txt))
    print('sheet',i+1,'done',flush=True)
open('/home/user/growth-plate/atlas/data/round194_the_supplied_bundle/02_fda_ocr.txt','w').write('\n'.join(out))
print('DONE')
