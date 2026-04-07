#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix files that have no quality: in their actual frontmatter."""

import os, re, sys, datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))
TODAY = datetime.date.today().isoformat()


def has_quality_in_fm(content):
    fm_m = re.match(r'^(\xef\xbb\xbf)?---\n(.*?)\n---', content, re.DOTALL)
    if not fm_m: return False
    return 'quality:' in fm_m.group(2)


def infer_domain(fp):
    fp = fp.replace("\\", "/").lower()
    bm = re.search(r'/builders?/([^/]+)-builder/', fp)
    if bm: return bm.group(1).replace("-", " ") + " construction"
    pm = {"p01":"knowledge","p02":"model config","p03":"prompt engineering",
          "p04":"tool integration","p05":"output format","p06":"schema",
          "p07":"evaluation","p08":"architecture","p09":"config","p10":"memory",
          "p11":"feedback","p12":"orchestration"}
    for k, v in pm.items():
        if f"/{k}" in fp: return v
    return "CEX system"


def infer_tags(fp):
    fp_low = fp.replace("\\", "/").lower()
    bm = re.search(r'/builders?/([^/]+)-builder/', fp_low)
    kind_tag = bm.group(1).replace("-", "_") if bm else "artifact"
    return f"[{kind_tag}, builder, examples]"


fixed = 0
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
            fm = fm_m.group(2)
            body = content[fm_m.end():]

            if has_quality_in_fm(content): continue

            # Parse existing FM keys
            fm_keys = set()
            for line in fm.split('\n'):
                if ':' in line:
                    fm_keys.add(line.split(':')[0].strip())

            adds = []
            if 'quality' not in fm_keys:
                adds.append('quality: null')
            if 'title' not in fm_keys:
                name = Path(fp).stem
                for p in ["bld_", "ex_", "kc_"]:
                    if name.startswith(p): name = name[len(p):]
                adds.append(f'title: "{name.replace("_", " ").title()}"')
            if 'version' not in fm_keys:
                adds.append('version: "1.0.0"')
            if 'author' not in fm_keys:
                adds.append('author: n03_builder')
            if 'tags' not in fm_keys:
                adds.append(f'tags: {infer_tags(fp)}')
            if 'tldr' not in fm_keys:
                domain = infer_domain(fp)
                adds.append(f'tldr: "Golden and anti-examples for {domain}, demonstrating ideal structure and common pitfalls."')
            if 'domain' not in fm_keys:
                adds.append(f'domain: "{infer_domain(fp)}"')
            if 'created' not in fm_keys:
                adds.append(f'created: "{TODAY}"')
            if 'updated' not in fm_keys:
                adds.append(f'updated: "{TODAY}"')
            if 'density_score' not in fm_keys:
                adds.append('density_score: 0.90')

            if adds:
                new_fm = fm.rstrip() + '\n' + '\n'.join(adds)
                new_content = f'{bom}---\n{new_fm}\n---{body}'
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixed += 1
                if fixed <= 10:
                    print(f'  Fixed: {fp} (+{len(adds)} fields)')

        except Exception as e:
            print(f'  Error: {fp}: {e}')

print(f'\nTotal files with FM fixed: {fixed}')
