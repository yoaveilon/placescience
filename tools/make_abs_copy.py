#!/usr/bin/env python3
"""Builds abs/index.html: a copy of abstracts.html with no top nav, no link from the site, noindex.
Run from the repo root after any change to abstracts.html:  python3 tools/make_abs_copy.py"""
import re
s = open('abstracts.html', encoding='utf-8').read()
s, n1 = re.subn(r'<nav class="nav">.*?</nav>\s*(?=<main>)', '', s, count=1, flags=re.S)
s, n2 = re.subn(r'<script>\s*\(function\(\)\{\s*var toggle = document\.querySelector\(\'\.nav-toggle\'\).*?</script>\s*', '', s, count=1, flags=re.S)
s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex,nofollow">', 1)
assert n1 == 1 and n2 == 1
open('abs/index.html', 'w', encoding='utf-8').write(s)
print('ok', len(s))
