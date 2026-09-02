import urllib.request,os,re
def matrices(gse):
    stub=gse[:-3]+'nnn'
    try:
        h=urllib.request.urlopen(f"https://ftp.ncbi.nlm.nih.gov/geo/series/{stub}/{gse}/matrix/",timeout=60).read().decode()
        return re.findall(r'href="([^"]*series_matrix[^"]*)"',h)
    except Exception as e: return []
for gse in ["GSE245140","GSE211559","GSE151303","GSE155892","GSE227468","GSE263602","GSE284991","GSE144362"]:
    fs=matrices(gse)
    print(gse, fs if fs else "NO MATRIX (seq-only)")
    for fn in fs:
        stub=gse[:-3]+'nnn'
        if os.path.exists(fn) and os.path.getsize(fn)>2000: print("   have",fn); continue
        try:
            urllib.request.urlretrieve(f"https://ftp.ncbi.nlm.nih.gov/geo/series/{stub}/{gse}/matrix/{fn}",fn)
            print("   OK",fn,os.path.getsize(fn))
        except Exception as e: print("   fail",fn,e)
