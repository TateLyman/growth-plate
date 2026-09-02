p = '/home/user/growth-plate/atlas/tools/overgrowth_screen.py'
s = open(p).read()

broken = '''                if i % 20 == 0:
                    cache_save("drugs.json", dcache)
    if n_query_failures[0]:
        print(f"\\nWARNING: {n_query_failures[0]} drug queries FAILED and are reported as blank, "
              f"not as zero.")
        seen, uniq = set(), []'''
fixed = '''                if i % 20 == 0:
                    cache_save("drugs.json", dcache)

        seen, uniq = set(), []'''
assert broken in s, "broken block not found"
s = s.replace(broken, fixed, 1)

# put the warning back where it belongs: after the loop, beside the final cache write
old_tail = '''    cache_save("drugs.json", dcache)

    os.makedirs(OUT, exist_ok=True)'''
new_tail = '''    cache_save("drugs.json", dcache)
    if n_query_failures[0]:
        print(f"\\nWARNING: {n_query_failures[0]} drug queries FAILED. Those genes are reported "
              f"BLANK, not zero.")

    if not rows:
        print("\\nHALTING: no rows were built. Refusing to write an empty targets.csv over a "
              "previous result.")
        return 1

    os.makedirs(OUT, exist_ok=True)'''
assert old_tail in s, "tail not found"
s = s.replace(old_tail, new_tail, 1)

open(p, 'w').write(s)
print('patched')
