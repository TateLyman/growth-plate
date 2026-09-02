p='/home/user/growth-plate/atlas/tools/overgrowth_screen.py'
s=open(p).read()
old='''    if cached:
        diseases, tgt = cached["diseases"], cached["targets"]'''
new='''    if cached:
        diseases, tgt = cached["diseases"], cached["targets"]
        # JSON has no tuples: the (disease, score) pairs come back as lists, which are
        # unhashable, and the dedup below is a set(). Restore them on the way in rather than
        # working around it at every use site.
        for _e in tgt.values():
            _e["diseases"] = [tuple(x) for x in _e["diseases"]]'''
assert old in s; s=s.replace(old,new,1); open(p,'w').write(s); print('fixed')
