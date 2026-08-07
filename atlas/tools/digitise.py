"""Recover plotted data-point coordinates from schrier2006's vector figures.

The figures are vector graphics, so the markers are real path objects with exact
page coordinates. This does NOT eyeball pixels: it reads the coordinates the
typesetter emitted, then calibrates them against the axis tick LABELS (which are
text objects with their own coordinates). Any number this produces is still a
RE-ANALYSIS and must be graded as such.
"""
import pdfplumber, sys, collections

PDF = '/root/.claude/uploads/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/c1b964e7-schrier2006.pdf'

page_i = int(sys.argv[1])

with pdfplumber.open(PDF) as p:
    pg = p.pages[page_i]
    print(f"page {page_i}  bbox={pg.bbox}")

    # cluster curves by their centre, small marker glyphs only
    marks = []
    for c in pg.curves:
        w = c['x1'] - c['x0']
        h = c['bottom'] - c['top']
        if w < 12 and h < 12:                      # a plot marker, not an axis
            marks.append((round((c['x0']+c['x1'])/2, 2),
                          round((c['top']+c['bottom'])/2, 2), w, h))
    print(f"small curve-markers: {len(marks)}")

    rmarks = []
    for c in pg.rects:
        w = c['x1'] - c['x0']
        h = c['bottom'] - c['top']
        if w < 12 and h < 12:
            rmarks.append((round((c['x0']+c['x1'])/2, 2),
                           round((c['top']+c['bottom'])/2, 2), w, h))
    print(f"small rect-markers: {len(rmarks)}")

    # words, with coordinates - these are the axis tick labels
    words = pg.extract_words()
    nums = [w for w in words
            if w['text'].replace('.', '').replace('-', '').isdigit()]
    print(f"\nnumeric text objects ({len(nums)}):")
    for w in sorted(nums, key=lambda w: (round(w['top']), w['x0'])):
        print(f"  {w['text']:>6}  x0={w['x0']:7.2f} x1={w['x1']:7.2f} "
              f"top={w['top']:7.2f} bottom={w['bottom']:7.2f}")

    print("\nmarker coordinates (x_page, y_page, w, h):")
    for m in sorted(marks + rmarks, key=lambda m: (m[0], m[1])):
        print(f"  {m}")
