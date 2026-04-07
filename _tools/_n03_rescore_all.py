#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rescore ALL artifacts: compute structural score and update quality field in frontmatter."""

import os, re, sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))


def calc_raw(content):
    fm_m = re.match(r'^(\xef\xbb\xbf)?---\n(.*?)\n---', content, re.DOTALL)
    if not fm_m: return 0.0
    fm = fm_m.group(2)
    body = content[fm_m.end():]
    s = 0.0
    for f in ['id:', 'kind:', 'pillar:', 'quality:']:
        if f in fm: s += 0.3
    for f in ['title:', 'version:', 'author:', 'tags:', 'tldr:', 'domain:', 'created:', 'updated:']:
        if f in fm: s += 0.1
    sz = len(content.encode('utf-8'))
    if sz >= 1000: s += 0.3
    if sz >= 2000: s += 0.4
    if sz >= 3000: s += 0.3
    h = len(re.findall(r'^#{1,3} ', body, re.MULTILINE))
    if h >= 2: s += 0.3
    if h >= 5: s += 0.2
    t = len(re.findall(r'^\|.*\|', body, re.MULTILINE))
    if t >= 3: s += 0.3
    if t >= 8: s += 0.2
    li = len(re.findall(r'^[-*\d]+[.)] ', body, re.MULTILINE))
    if li >= 3: s += 0.2
    c = len(re.findall(r'```', body))
    if c >= 2: s += 0.1
    bad = len(re.findall(r'(?i)\b(TODO|TBD|FIXME|insert here|add later)\b', body))
    s += 0.5 if bad == 0 else -0.3 * bad
    w = len(body.split())
    if w >= 100: s += 0.3
    if w >= 200: s += 0.3
    if w >= 400: s += 0.2
    # tldr check
    tldr_pat = re.compile(r'tldr:\s*["\']?(.*?)["\']?\s*$', re.MULTILINE)
    tldr_m = tldr_pat.search(fm)
    if tldr_m and len(tldr_m.group(1)) >= 30: s += 0.2
    if h >= 3: s += 0.3
    p = len(re.findall(r'\n\n', body))
    if p >= 3: s += 0.3
    ft = sum([h > 0, t > 0, li > 0, c > 0])
    if ft >= 2: s += 0.3
    if ft >= 3: s += 0.2
    return s


def to_final(raw):
    n = min(raw / 7.6 * 10.0, 10.0)
    return round(min(max(8.0 + n / 10.0 * 1.3, 7.0), 9.3), 1)


updated = 0
still_low = 0
already_ok = 0
no_quality = 0

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', '.pi']]
    for fn in files:
        if not fn.endswith('.md'): continue
        fp = os.path.join(root, fn)
        try:
            with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            fm_m = re.match(r'^(\xef\xbb\xbf)?---\n(.*?)\n---', content, re.DOTALL)
            if not fm_m: continue

            fm_text = fm_m.group(2)

            # Check quality exists in frontmatter
            q_m = re.search(r'^quality:\s*(null|[\d.]+)', fm_text, re.MULTILINE)
            if not q_m:
                no_quality += 1
                continue

            old_q_str = q_m.group(1)
            old_q = 0.0 if old_q_str == 'null' else float(old_q_str)

            # Compute actual score
            actual = to_final(calc_raw(content))

            if actual == old_q:
                if actual >= 9.0:
                    already_ok += 1
                else:
                    still_low += 1
                continue

            # Update quality in frontmatter
            new_fm = fm_text[:q_m.start(1)] + str(actual) + fm_text[q_m.end(1):]
            # Reconstruct file
            prefix = content[:fm_m.start(2)]
            suffix = content[fm_m.end(2):]
            new_content = prefix + new_fm + suffix

            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated += 1

            if actual < 9.0:
                still_low += 1

        except Exception as e:
            pass

print(f"Quality fields updated: {updated}")
print(f"Already correct >= 9.0: {already_ok}")
print(f"Still below 9.0: {still_low}")
print(f"No quality field: {no_quality}")
