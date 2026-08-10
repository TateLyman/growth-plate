#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re, shutil, urllib.parse
from pathlib import Path
import requests

ROOT=Path('build/last_originals'); ROOT.mkdir(parents=True,exist_ok=True)
S=requests.Session(); S.headers.update({'User-Agent':'Mozilla/5.0 source-preservation/1.0','Accept':'*/*'})
log=[]

def safe(s): return re.sub(r'[^A-Za-z0-9._ -]+','_',s)[:180]
def get(url, name, headers=None, min_bytes=100):
    try:
        r=S.get(url,headers=headers or {},timeout=180,allow_redirects=True)
        ct=r.headers.get('content-type','')
        if r.status_code>=400: raise RuntimeError(f'HTTP {r.status_code} {ct}')
        if len(r.content)<min_bytes: raise RuntimeError(f'too small {len(r.content)}')
        ext=Path(urllib.parse.urlparse(r.url).path).suffix
        p=ROOT/(safe(name)+(ext if ext and '.' not in Path(name).name else ''))
        i=2
        while p.exists(): p=ROOT/(p.stem+f'_{i}'+p.suffix); i+=1
        p.write_bytes(r.content)
        log.append({'url':url,'final_url':r.url,'status':'downloaded','path':str(p),'bytes':len(r.content),'content_type':ct})
        print('OK',len(r.content),ct,p)
        return p
    except Exception as e:
        log.append({'url':url,'status':'failed','error':str(e)}); print('FAIL',url,e); return None

def s3_pmc(pmc,label):
    prefix=f'{pmc}.1/'
    listurl='https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix='+urllib.parse.quote(prefix)
    p=get(listurl,f'{label}_{pmc}_s3_listing.xml')
    if not p:return
    txt=p.read_text('utf-8',errors='ignore')
    keys=re.findall(r'<Key>(.*?)</Key>',txt)
    for k in keys:
        u='https://pmc-oa-opendata.s3.amazonaws.com/'+urllib.parse.quote(k,safe='/')
        get(u,f'{label}__{Path(k).name}',min_bytes=20)
    get(f'https://pmc-oa-opendata.s3.amazonaws.com/metadata/{pmc}.1.json',f'{label}_{pmc}_metadata.json',min_bytes=20)

def crossref(doi,label):
    q=urllib.parse.quote(doi,safe='')
    p=get('https://api.crossref.org/works/'+q,f'{label}_crossref.json')
    if not p:return
    try:m=json.loads(p.read_text())['message']
    except Exception:return
    urls=[]
    for x in m.get('link',[]):
        if x.get('URL'): urls.append(x['URL'])
    if m.get('resource',{}).get('primary',{}).get('URL'): urls.append(m['resource']['primary']['URL'])
    for i,u in enumerate(dict.fromkeys(urls)):
        get(u,f'{label}_crossref_link_{i:02d}',headers={'Accept':'application/pdf, application/xml, text/html;q=0.8'},min_bytes=100)
    up='https://api.unpaywall.org/v2/'+q+'?email=research@example.com'
    upf=get(up,f'{label}_unpaywall.json',min_bytes=20)
    if upf:
        try:ud=json.loads(upf.read_text())
        except Exception:ud={}
        cand=[]
        for key in ['best_oa_location']:
            loc=ud.get(key) or {}
            cand += [loc.get('url_for_pdf'),loc.get('url_for_landing_page'),loc.get('url')]
        for loc in ud.get('oa_locations') or []:
            cand += [loc.get('url_for_pdf'),loc.get('url_for_landing_page'),loc.get('url')]
        for i,u in enumerate(dict.fromkeys(x for x in cand if x)):
            get(u,f'{label}_unpaywall_link_{i:02d}',headers={'Accept':'application/pdf,text/html;q=0.8'},min_bytes=100)

def jina(url,label):
    get('https://r.jina.ai/http://'+url.replace('https://','').replace('http://',''),f'{label}_publisher_fulltext.md',min_bytes=500)

def main():
    s3_pmc('PMC13060625','Dabogratinib_2026_MCT')
    crossref('10.1158/1535-7163.MCT-25-0652','Dabogratinib_2026_MCT')
    crossref('10.1158/1535-7163.MCT-16-0589','Perera_2017_erdafitinib')
    crossref('10.1016/j.bioactmat.2026.06.018','Ye_2026_nanoparticles')
    crossref('10.1097/BPO.0000000000002397','Breen_2023_remaining_growth')
    jina('aacrjournals.org/mct/article/16/6/1010/92241/Discovery-and-Pharmacological-Characterization-of','Perera_2017_erdafitinib')
    jina('aacrjournals.org/mct/article/25/3/408/774807/Dabogratinib-TYRA-300-an-FGFR3-Isoform-Selective','Dabogratinib_2026_MCT')
    jina('www.sciencedirect.com/science/article/pii/S2452199X26003543','Ye_2026_nanoparticles')
    jina('journals.lww.com/pedorthopaedics/fulltext/2023/07000/comparison_of_different_bone_age_methods_and.3.aspx','Breen_2023_remaining_growth')
    # Known direct attempts
    for i,u in enumerate([
      'https://www.sciencedirect.com/science/article/pii/S2452199X26003543/pdfft?isDTMRedir=true&download=true',
      'https://api.elsevier.com/content/article/doi/10.1016/j.bioactmat.2026.06.018?httpAccept=application/pdf',
      'https://journals.lww.com/pedorthopaedics/_layouts/15/oaks.journals/downloadpdf.aspx?an=01241398-202307000-00003'
    ]): get(u,f'known_direct_{i:02d}',min_bytes=500)
    inv=[]
    for p in sorted(ROOT.iterdir()):
        if p.is_file(): inv.append({'path':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    (ROOT/'fetch_log.json').write_text(json.dumps(log,indent=2))
    (ROOT/'inventory.json').write_text(json.dumps(inv,indent=2))
    shutil.make_archive('build/last_originals','zip','build','last_originals')
if __name__=='__main__': main()
