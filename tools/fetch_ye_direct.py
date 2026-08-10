from pathlib import Path
import json, requests, hashlib
out=Path('build/ye_direct'); out.mkdir(parents=True,exist_ok=True)
S=requests.Session(); S.headers.update({'User-Agent':'Mozilla/5.0','Accept':'*/*'})
urls={
'Ye_2026_full_version_of_record.pdf':'https://b-real.lab.westlake.edu.cn/2026-growth-plate-cartilage-BAM-Shang.pdf',
'Ye_2026_mmc1.pdf':'https://ars.els-cdn.com/content/image/1-s2.0-S2452199X26003543-mmc1.pdf',
'Ye_2026_mmc1.docx':'https://ars.els-cdn.com/content/image/1-s2.0-S2452199X26003543-mmc1.docx',
'Ye_2026_mmc1.zip':'https://ars.els-cdn.com/content/image/1-s2.0-S2452199X26003543-mmc1.zip',
'Ye_2026_mmc2.pdf':'https://ars.els-cdn.com/content/image/1-s2.0-S2452199X26003543-mmc2.pdf',
'Ye_2026_mmc2.xlsx':'https://ars.els-cdn.com/content/image/1-s2.0-S2452199X26003543-mmc2.xlsx',
'Ye_2026_graphical_abstract.jpg':'https://ars.els-cdn.com/content/image/1-s2.0-S2452199X26003543-ga1_lrg.jpg',
}
log=[]
for name,u in urls.items():
 try:
  r=S.get(u,timeout=180,allow_redirects=True)
  ct=r.headers.get('content-type','')
  if r.status_code>=400 or len(r.content)<100: raise RuntimeError(f'HTTP {r.status_code}, {len(r.content)} bytes, {ct}')
  p=out/name; p.write_bytes(r.content)
  log.append({'name':name,'url':u,'status':'downloaded','bytes':len(r.content),'content_type':ct,'sha256':hashlib.sha256(r.content).hexdigest()})
  print('OK',name,len(r.content),ct)
 except Exception as e:
  log.append({'name':name,'url':u,'status':'failed','error':str(e)}); print('FAIL',name,e)
(out/'manifest.json').write_text(json.dumps(log,indent=2))
