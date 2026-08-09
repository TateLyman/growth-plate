import pymupdf, pytesseract, io, sys, os
from PIL import Image
src=sys.argv[1]; out=sys.argv[2]
d=pymupdf.open(src)
res=[]
for i,pg in enumerate(d):
    lbl=pg.get_text().strip().split('\n')
    pix=pg.get_pixmap(dpi=300)
    img=Image.open(io.BytesIO(pix.tobytes('png')))
    w,h=img.size
    # 6-up: assume 2 cols x 3 rows
    cells=[]
    for r in range(3):
        for c in range(2):
            cells.append((c*w//2, r*h//3, (c+1)*w//2, (r+1)*h//3))
    parts=[]
    for k,box in enumerate(cells):
        tag = lbl[k] if k < len(lbl) else 'sheet %d cell %d'%(i+1,k+1)
        parts.append('\n--- %s ---\n'%tag + pytesseract.image_to_string(img.crop(box)))
    res.append('\n\n===== SHEET %d =====\n'%(i+1)+''.join(parts))
    print('sheet',i+1,'/',len(d),flush=True)
open(out,'w').write(''.join(res))
print('DONE')
