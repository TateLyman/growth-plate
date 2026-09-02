"""Parse a .tbi linear index and pull only the needed BGZF blocks by HTTP Range."""
import gzip, struct, io, json, urllib.request, sys

def read_tbi(path):
    raw = gzip.open(path, 'rb').read()
    o = 0
    magic, = struct.unpack_from('<4s', raw, o); o += 4
    assert magic == b'TBI\x01', magic
    n_ref, fmt, col_seq, col_beg, col_end, meta, skip, l_nm = struct.unpack_from('<8i', raw, o); o += 32
    names = raw[o:o+l_nm].split(b'\x00'); o += l_nm
    names = [n.decode() for n in names if n]
    linear = {}
    for r in range(n_ref):
        n_bin, = struct.unpack_from('<i', raw, o); o += 4
        for _ in range(n_bin):
            _bin, n_chunk = struct.unpack_from('<Ii', raw, o); o += 8
            o += 16 * n_chunk
        n_intv, = struct.unpack_from('<i', raw, o); o += 4
        iv = struct.unpack_from('<%dQ' % n_intv, raw, o); o += 8 * n_intv
        linear[names[r]] = iv
    return names, linear, (col_seq, col_beg, col_end, skip)

def fetch(url, start, length):
    req = urllib.request.Request(url, headers={'Range': f'bytes={start}-{start+length-1}'})
    return urllib.request.urlopen(req, timeout=180).read()

def decompress_members(buf):
    """BGZF = concatenated gzip members; stop cleanly at a truncated tail."""
    out = io.BytesIO(); pos = 0
    import zlib
    while pos < len(buf) - 18:
        try:
            d = zlib.decompressobj(31)
            chunk = d.decompress(buf[pos:])
        except Exception:
            break
        if not chunk and not d.unused_data:
            break
        out.write(chunk)
        consumed = len(buf) - pos - len(d.unused_data)
        if consumed <= 0:
            break
        pos += consumed
        if not d.eof:
            break
    return out.getvalue()

def region(url, linear, chrom, beg, end, span=12_000_000):
    iv = linear.get(chrom)
    if not iv: return []
    w = max(0, (beg - 1) >> 14)
    if w >= len(iv): return []
    # walk back to the last non-zero entry at or before w
    while w > 0 and iv[w] == 0: w -= 1
    start_byte = iv[w] >> 16
    buf = fetch(url, start_byte, span)
    txt = decompress_members(buf).decode('utf-8', 'ignore')
    rows = []
    for line in txt.split('\n'):
        f = line.split('\t')
        if len(f) < 9: continue
        if f[0] != chrom: continue
        try: p = int(f[1])
        except ValueError: continue
        if p > end: break
        if p >= beg: rows.append(line)
    return rows
