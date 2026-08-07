import yaml, sys
sys.path.insert(0,'.')
from w import _B, DIR
import os
FIND={}
for nid in ['shox_gene','shox_haploinsufficiency','acan_gene','npr2_gene','nppc_gene']:
    p=os.path.join(DIR,nid+'.yaml')
    d=yaml.safe_load(open(p))
    new=[]
    for kr in d['key_refs']:
        rid=kr['ref_id']; r=_B[rid]
        e=dict(ref_id=rid)
        if r.get('pmid'): e['pmid']=str(r['pmid'])
        if r.get('doi'): e['doi']=r['doi']
        e['first_author']=r['first_author']; e['year']=r['year']; e['type']=r['type']
        e['one_line_finding']=kr['one_line_finding']
        new.append(e)
    d['key_refs']=new
    s=yaml.dump(d,sort_keys=False,default_flow_style=False,width=92,allow_unicode=True)
    open(p,'w').write(s)
    print('fixed',nid)
