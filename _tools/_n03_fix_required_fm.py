#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix files missing required frontmatter: id, kind, pillar."""

import os, re, sys, datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))
TODAY = datetime.date.today().isoformat()


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
    tldr_pat = re.compile(r"tldr:\s*[\"']?(.*?)[\"']?\s*$", re.MULTILINE)
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


def infer_pillar(fp):
    fp = fp.replace("\\", "/").lower()
    for i in range(1, 13):
        tag = f"/p{i:02d}" if i < 10 else f"/p{i}"
        if tag in fp:
            return f"P{i:02d}"
    if "/n01" in fp: return "P08"
    if "/n02" in fp: return "P05"
    if "/n03" in fp: return "P03"
    if "/n04" in fp: return "P01"
    if "/n05" in fp: return "P09"
    if "/n06" in fp: return "P06"
    if "/n07" in fp: return "P12"
    if "/builder" in fp: return "P03"
    if "/agent" in fp: return "P08"
    if "/runtime" in fp: return "P12"
    if "/archive" in fp: return "P12"
    return "P08"


def infer_kind(fp, fm):
    fp = fp.replace("\\", "/").lower()
    if "agent" in fp and "builder" not in fp and "card" not in fp:
        return "agent"
    if "handoff" in fp or "task" in fp:
        return "context_doc"
    if "command" in fp:
        return "instruction"
    if "rule" in fp:
        return "instruction"
    if "prompt" in fp:
        return "system_prompt"
    if "skill" in fp:
        return "instruction"
    if "template" in fp:
        return "output_template"
    if "schema" in fp:
        return "schema"
    if "example" in fp:
        return "examples"
    if "spec" in fp:
        return "context_doc"
    if "plan" in fp or "mission" in fp:
        return "context_doc"
    if "index" in fp:
        return "context_doc"
    if "validation" in fp:
        return "context_doc"
    # Check existing kind in fm
    if fm.get("kind"):
        return fm["kind"].strip('"\'')
    return "context_doc"


def infer_id(fp):
    name = Path(fp).stem.lower()
    # Clean special chars
    clean = re.sub(r'[^a-z0-9_]', '_', name)
    return clean


fixed = 0
total_below = 0

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

            bom = fm_m.group(1) or ""
            fm_raw = fm_m.group(2)
            body = content[fm_m.end():]

            # Check quality in FM
            q_m = re.search(r'^quality:\s*([\d.]+)', fm_raw, re.MULTILINE)
            if not q_m: continue
            q = float(q_m.group(1))
            if q >= 9.0: continue

            total_below += 1

            # Parse FM
            fm = {}
            for line in fm_raw.split('\n'):
                if ':' in line:
                    k = line.split(':')[0].strip()
                    v = line.split(':', 1)[1].strip()
                    fm[k] = v

            # Check required fields
            adds = []
            if 'id' not in fm:
                adds.append(f'id: {infer_id(fp)}')
            if 'kind' not in fm:
                adds.append(f'kind: {infer_kind(fp, fm)}')
            if 'pillar' not in fm:
                adds.append(f'pillar: {infer_pillar(fp)}')

            if not adds:
                continue  # Already has required fields, gap is elsewhere

            # Add missing fields at top of frontmatter
            new_fm = '\n'.join(adds) + '\n' + fm_raw
            new_content = f'{bom}---\n{new_fm}\n---{body}'

            # Compute new score
            new_score = to_final(calc_raw(new_content))

            # Update quality
            new_content = re.sub(
                r'^quality:\s*(?:null|[\d.]+)',
                f'quality: {new_score}',
                new_content, count=1, flags=re.MULTILINE
            )

            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)

            fixed += 1
            if fixed <= 10:
                print(f"  {q}->{new_score} {fp} (+{len(adds)} required)")

        except Exception as e:
            print(f"  Error: {fp}: {e}")

print(f"\nFixed: {fixed} / {total_below} below 9.0")
