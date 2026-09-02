import glob,os,json,re
from collections import Counter
withdata=[];empty=[];plats=Counter()
for f in sorted(glob.glob('mat/*.txt')):
    acc=os.path.basename(f)[:-4]
    txt=open(f,encoding='utf8',errors='replace').read()
    m=re.search(r'!Series_platform_id\t"([^"]+)"',txt)
    p=m.group(1) if m else '?'
    i=txt.find('!series_matrix_table_begin')
    j=txt.find('!series_matrix_table_end')
    nrow=0
    if i>=0 and j>i: nrow=txt[i:j].count('\n')-2
    if nrow>200: withdata.append((acc,p,nrow)); plats[p]+=1
    else: empty.append(acc)
print('with data:',len(withdata),' empty(HTS):',len(empty))
print(plats.most_common(40))
json.dump([w[0] for w in withdata],open('withdata.json','w'))
json.dump(empty,open('emptyseries.json','w'))
json.dump(sorted(plats),open('platlist.json','w'))
