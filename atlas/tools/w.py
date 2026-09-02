import yaml, os
DIR='/home/user/growth-plate/atlas/nodes/L8_genetics_and_heritability'
D='2026-08-05'

class LS(str): pass
def _lsr(dumper,data): return dumper.represent_scalar('tag:yaml.org,2002:str',data,style='|' if '\n' in data else None)
yaml.add_representer(LS,_lsr)

def write(node):
    node.setdefault('stub', False)
    node['last_verified']=D
    p=os.path.join(DIR, node['id']+'.yaml')
    order=['id','name','aliases','type','layer','stub','summary','quantitative','localization',
           'human_evidence','human_evidence_note','species_basis','translation_risk',
           'translation_risk_reason','confidence','claim_grades','key_refs','open_questions',
           'contradicts','pending_source','last_verified']
    out={k:node[k] for k in order if k in node}
    for k in node:
        if k not in out: out[k]=node[k]
    if 'summary' in out: out['summary']=LS(out['summary'])
    with open(p,'w') as f:
        yaml.dump(out,f,sort_keys=False,default_flow_style=False,width=92,allow_unicode=True)
    print('wrote',node['id'])

def q(parameter,value,unit,conditions,species,source_ref,uncertainty):
    return dict(parameter=parameter,value=str(value),unit=unit,conditions=conditions,
                species=species,source_ref=source_ref,uncertainty=uncertainty)

def ref(rid,pmid,doi,fa,yr,typ,finding):
    d=dict(ref_id=rid,pmid=str(pmid),first_author=fa,year=yr,type=typ,one_line_finding=finding)
    if doi: d['doi']=doi
    return d

_B={}
for _p in ['/home/user/growth-plate/atlas/sources/bibliography.yaml','/home/user/growth-plate/atlas/sources/shards/l8gen.yaml']:
    try:
        _d=yaml.safe_load(open(_p)) or {}
        _B.update(_d.get('refs') or {})
    except Exception as e: print('bibload',e)

def R(rid,finding):
    """Build a key_ref entry from the verified bibliography record."""
    r=_B[rid]
    d=dict(ref_id=rid)
    if r.get('pmid'): d['pmid']=str(r['pmid'])
    if r.get('doi'): d['doi']=r['doi']
    d['first_author']=r['first_author']; d['year']=r['year']; d['type']=r['type']
    d['one_line_finding']=finding
    return d
