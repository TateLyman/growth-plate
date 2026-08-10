#!/usr/bin/env python3
from __future__ import annotations
import json, os, re, tarfile, zipfile, hashlib, mimetypes, shutil, subprocess, sys, time
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET

ROOT=Path('build/targeted_originals')
ROOT.mkdir(parents=True,exist_ok=True)
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/132 Safari/537.36 source-preservation-bot/1.0'
S=requests.Session(); S.headers.update({'User-Agent':UA,'Accept':'*/*'})
log=[]

def safe(s:str, n=180)->str:
    s=unquote(str(s)).strip().replace('\x00','')
    s=re.sub(r'[\\/:*?"<>|]+','_',s)
    s=re.sub(r'\s+',' ',s).strip(' ._-')
    return (s or 'file')[:n]

def unique(p:Path)->Path:
    if not p.exists(): return p
    stem,suf=p.stem,p.suffix
    i=2
    while True:
        q=p.with_name(f'{stem}_{i}{suf}')
        if not q.exists(): return q
        i+=1

def infer_name(url,r,default):
    cd=r.headers.get('content-disposition','')
    m=re.search(r"filename\*=UTF-8''([^;]+)",cd,re.I) or re.search(r'filename="?([^";]+)',cd,re.I)
    if m: return safe(m.group(1))
    name=Path(urlparse(r.url or url).path).name
    return safe(name or default)

def fetch(url:str, dest_dir:Path, default:str, *, method='get', json_body=None, headers=None, min_bytes=50, timeout=180)->Path|None:
    dest_dir.mkdir(parents=True,exist_ok=True)
    try:
        r=S.request(method,url,json=json_body,headers=headers or {},timeout=timeout,allow_redirects=True)
        ct=r.headers.get('content-type','')
        if r.status_code>=400: raise RuntimeError(f'HTTP {r.status_code} {ct}')
        b=r.content
        if len(b)<min_bytes: raise RuntimeError(f'too small {len(b)} bytes')
        name=infer_name(url,r,default)
        p=unique(dest_dir/name); p.write_bytes(b)
        log.append({'url':url,'status':'downloaded','path':str(p),'bytes':len(b),'content_type':ct,'final_url':r.url})
        print('OK',len(b),p)
        return p
    except Exception as e:
        log.append({'url':url,'status':'failed','error':str(e)})
        print('FAIL',url,e)
        return None

def extract_archive(p:Path, out:Path):
    out.mkdir(parents=True,exist_ok=True)
    try:
        if p.suffix.lower()=='.zip':
            with zipfile.ZipFile(p) as z: z.extractall(out)
        elif p.name.endswith(('.tar.gz','.tgz')):
            with tarfile.open(p,'r:*') as t: t.extractall(out,filter='data')
        else: return
        for q in sorted(out.rglob('*')):
            if q.is_file():
                log.append({'url':str(p),'status':'extracted','path':str(q),'bytes':q.stat().st_size})
    except Exception as e:
        log.append({'url':str(p),'status':'extract_failed','error':str(e)})

def walk_dict(x):
    if isinstance(x,dict):
        yield x
        for v in x.values(): yield from walk_dict(v)
    elif isinstance(x,list):
        for v in x: yield from walk_dict(v)

def ctis_all():
    out=ROOT/'01_CTIS_SURF301_all_31_documents'
    retrieve='https://euclinicaltrials.eu/ctis-public-api/retrieve/2023-507589-22-00'
    p=fetch(retrieve,out,'SURF301_CTIS_retrieve.json',min_bytes=100)
    if not p:return
    try:data=json.loads(p.read_text('utf-8'))
    except Exception as e: print('CTIS JSON parse fail',e);return
    docs={}
    for d in walk_dict(data):
        if d.get('uuid') and (d.get('title') or d.get('fileType')):
            docs[d['uuid']]=d
    print('CTIS document records',len(docs))
    (out/'CTIS_document_metadata.json').write_text(json.dumps(list(docs.values()),indent=2,ensure_ascii=False))
    for uuid,d in docs.items():
        ext=str(d.get('fileType') or 'bin').lower().lstrip('.')
        title=safe(d.get('title') or uuid,120)
        typ=safe(d.get('documentTypeLabel') or d.get('documentType') or 'document',70)
        assoc=safe(d.get('associatedEntityId') or '',35)
        default=f'{typ} - {title}' + (f' - {assoc}' if assoc else '') + f'.{ext}'
        url=f'https://euclinicaltrials.eu/ctis-public-api/documents/2023-507589-22-00/{uuid}/download'
        fetch(url,out,default,min_bytes=100)

def oa_package(pmc:str,label:str):
    out=ROOT/f'02_PMC_OA_{label}_{pmc}'
    xmlurl=f'https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id={pmc}'
    xp=fetch(xmlurl,out,f'{pmc}_oa.xml',min_bytes=20)
    if not xp:return
    try:root=ET.fromstring(xp.read_bytes())
    except Exception as e:print('OA XML parse failed',e);return
    links=[]
    for n in root.findall('.//link'):
        href=n.attrib.get('href'); fmt=n.attrib.get('format','')
        if href:links.append((fmt,href.replace('ftp://','https://')))
    for fmt,u in links:
        default=f'{pmc}_oa_package.{"tar.gz" if fmt=="tgz" else fmt or "bin"}'
        p=fetch(u,out,default,min_bytes=500)
        if p: extract_archive(p,out/(p.stem+'_extracted'))
    fetch(f'https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/pdf/',out,f'{pmc}_fulltext.pdf',min_bytes=5000)

def figshare_search():
    out=ROOT/'03_Perera_2017_AACR_Figshare_all_supplements'
    terms=[
        'Discovery and Pharmacological Characterization of JNJ-42756493',
        'Supplemental Figure 1 from Discovery and Pharmacological Characterization of JNJ-42756493',
        'Supplemental Table 1 from Discovery and Pharmacological Characterization of JNJ-42756493',
        'Supplemental Table 2 from Discovery and Pharmacological Characterization of JNJ-42756493',
        'Supplemental Table 3 from Discovery and Pharmacological Characterization of JNJ-42756493',
        'Supplemental Table 4 from Discovery and Pharmacological Characterization of JNJ-42756493',
    ]
    ids=set()
    for term in terms:
        try:
            r=S.post('https://api.figshare.com/v2/articles/search',json={'search_for':term,'limit':100,'order':'published_date','order_direction':'desc'},timeout=120)
            print('figshare search',term,r.status_code,len(r.content))
            if r.ok:
                p=unique(out/(safe(term,80)+'.search.json')); p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(r.content)
                for a in r.json():
                    title=(a.get('title') or '').lower()
                    if 'jnj-42756493' in title or 'erdafitinib' in title: ids.add(a['id'])
        except Exception as e: print('figshare search fail',e)
    landing='https://aacrjournals.org/mct/article/doi/10.1158/1535-7163.MCT-16-0589/86986/am/Discovery-and-pharmacological-characterization-of'
    hp=fetch(landing,out,'AACR_Perera_supplement_landing.html',min_bytes=1000)
    if hp:
        txt=hp.read_text('utf-8',errors='ignore')
        for m in re.finditer(r'(?:figshare\.com/(?:articles/[^/]+/)?|articleId["\':= ]+)(\d{5,})',txt,re.I): ids.add(int(m.group(1)))
        for u in sorted(set(re.findall(r'https?://[^"\'<> ]+',txt))):
            if ('figshare' in u or 'supp' in u.lower()) and any(x in u.lower() for x in ['download','ndownloader','file','figshare']):
                fetch(u.rstrip('\\'),out,'embedded_supplement.bin',min_bytes=100)
    print('figshare candidate IDs',sorted(ids))
    for aid in sorted(ids):
        p=fetch(f'https://api.figshare.com/v2/articles/{aid}',out,f'figshare_article_{aid}.json',min_bytes=100)
        if not p:continue
        try:meta=json.loads(p.read_text('utf-8'))
        except:continue
        for f in meta.get('files',[]):
            u=f.get('download_url'); name=f.get('name') or f'figshare_{aid}_{f.get("id")}'
            if u: fetch(u,out,name,min_bytes=100)

def acs_si():
    out=ROOT/'04_Hudkins_2024_ACS_supporting_information'
    urls=[
      ('https://pubs.acs.org/doi/suppl/10.1021/acs.jmedchem.4c01531/suppl_file/jm4c01531_si_001.pdf','jm4c01531_si_001.pdf'),
      ('https://pubs.acs.org/doi/suppl/10.1021/acs.jmedchem.4c01531/suppl_file/jm4c01531_si_002.csv','jm4c01531_si_002.csv'),
    ]
    for u,n in urls: fetch(u,out,n,headers={'Referer':'https://pubs.acs.org/doi/10.1021/acs.jmedchem.4c01531'},min_bytes=100)
    try:
        r=S.post('https://api.figshare.com/v2/articles/search',json={'search_for':'Discovery of TYRA-300 First Oral Selective FGFR3','limit':100},timeout=120)
        if r.ok:
            (out/'ACS_figshare_search.json').write_bytes(r.content)
            for a in r.json():
                aid=a['id']; p=fetch(f'https://api.figshare.com/v2/articles/{aid}',out,f'acs_figshare_{aid}.json',min_bytes=100)
                if p:
                    try:meta=json.loads(p.read_text())
                    except:continue
                    for f in meta.get('files',[]):
                        if f.get('download_url'):fetch(f['download_url'],out,f.get('name') or 'acs_file',min_bytes=100)
    except Exception as e:print(e)

def article_assets(label,url,extra_urls=()):
    out=ROOT/f'05_{safe(label)}'
    p=fetch(url,out,f'{safe(label)}_article.html',min_bytes=1000)
    if p:
        html=p.read_text('utf-8',errors='ignore'); soup=BeautifulSoup(html,'lxml')
        candidates=[]
        for m in soup.find_all('meta'):
            if m.get('name') in ['citation_pdf_url','citation_fulltext_html_url'] and m.get('content'): candidates.append(urljoin(url,m['content']))
        for a in soup.find_all('a',href=True):
            u=urljoin(url,a['href']); t=(a.get_text(' ',strip=True)+' '+u).lower()
            if any(k in t for k in ['pdf','supplement','mmc','download','supporting information']): candidates.append(u)
        for i,u in enumerate(dict.fromkeys(candidates)):
            fetch(u,out,f'{safe(label)}_asset_{i:03d}.bin',headers={'Referer':url},min_bytes=100)
    for i,u in enumerate(extra_urls):fetch(u,out,f'{safe(label)}_extra_{i:02d}.bin',headers={'Referer':url},min_bytes=100)

def main():
    ctis_all()
    oa_package('PMC6315953','Englinger_2018')
    oa_package('PMC12934022','Qiu_2026')
    figshare_search()
    acs_si()
    article_assets('Perera_2017_full','https://aacrjournals.org/mct/article/16/6/1010/92241/Discovery-and-Pharmacological-Characterization-of')
    article_assets('Dabogratinib_2026_MCT','https://aacrjournals.org/mct/article/25/3/408/774807/Dabogratinib-TYRA-300-an-FGFR3-Isoform-Selective')
    article_assets('Ye_2026_nanoparticle','https://www.sciencedirect.com/science/article/pii/S2452199X26003543',[
      'https://www.sciencedirect.com/science/article/pii/S2452199X26003543/pdfft?isDTMRedir=true&download=true',
      'https://api.elsevier.com/content/article/pii/S2452199X26003543?httpAccept=application/pdf',
    ])
    article_assets('Breen_2023','https://journals.lww.com/pedorthopaedics/fulltext/2023/07000/comparison_of_different_bone_age_methods_and.3.aspx',[
      'https://journals.lww.com/pedorthopaedics/_layouts/15/oaks.journals/downloadpdf.aspx?an=01241398-202307000-00003',
      'https://doi.org/10.1097/BPO.0000000000002397',
    ])
    (ROOT/'targeted_fetch_manifest.json').write_text(json.dumps(log,indent=2,ensure_ascii=False))
    rows=[]
    for p in sorted(ROOT.rglob('*')):
        if p.is_file(): rows.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    (ROOT/'targeted_file_inventory.json').write_text(json.dumps(rows,indent=2))
    shutil.make_archive('build/targeted_originals','zip','build','targeted_originals')
    print('FILES',len(rows))
if __name__=='__main__':main()
