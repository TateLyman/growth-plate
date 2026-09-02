import numpy as np,json,glob,os,re
M={k.upper():v.upper() for k,v in json.load(open('ens2sym.json')).items()}
BAD=re.compile(r'^(chromosome|start|end|strand|exon_number|length|orf|gene_chr|gene_start|gene_end|gene_length|gene_id|gene_name|gene_biotype|gene_description|transcript.*|symbol|entrez.*|refseq.*|biotype|description|chr|width|baseMean|padj|pvalue|log2FoldChange|lfcSE|stat)$',re.I)
f1=f2=0
for f in sorted(glob.glob('cache/*.npz')):
    try: z=np.load(f,allow_pickle=True)
    except Exception: continue
    g=z['g'];X=z['X'];L=[str(x) for x in z['labels']];ch=False
    ens=np.array([str(x).startswith('ENS') for x in g])
    if ens.mean()>=0.3:
        ng=np.array([M.get(str(x),str(x)) for x in g])
        keep=np.array([not str(x).startswith('ENS') for x in ng])
        if keep.sum()>500:
            ng=ng[keep];X=X[keep]
            o=np.argsort(-np.nan_to_num(np.nanmean(X,axis=1),nan=-1e9));g2=ng[o];X2=X[o]
            _,fi=np.unique(g2,return_index=True);fi=np.sort(fi)
            g=g2[fi];X=X2[fi];ch=True;f1+=1
    keep=[i for i,l in enumerate(L) if not BAD.match(l.strip())]
    if len(keep)<len(L) and len(keep)>=3:
        X=X[:,keep];L=[L[i] for i in keep];ch=True;f2+=1
    if ch:
        np.savez_compressed(f,g=g,X=X,labels=np.array(L,dtype=object),kind=z['kind'],
            stitle=z['stitle'],org=z['org'],summary=z['summary'])
print('ens-remapped',f1,'| annotation-cols-stripped',f2)
