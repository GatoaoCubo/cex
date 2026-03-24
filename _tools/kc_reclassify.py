#!/usr/bin/env python3
"""KC Reclassifier: Move oversized KCs to correct P01 type + extract axiom summaries.
10-50KB -> contexts/CTX_* + axiom KC. >50KB -> reports/RPT_* + axiom KC.
DRY RUN default. --apply to execute.
"""
import os, sys, re, glob, yaml, shutil
from pathlib import Path
from datetime import date

KC_MAX = 5120

def parse_fm(content):
    m = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not m: return {}, content
    try:
        fm = yaml.safe_load(m.group(1))
        return (fm, m.group(2)) if isinstance(fm, dict) else ({}, content)
    except: return {}, content

def extract_axioms(body, fm):
    tldr = fm.get('tldr', '')
    if not tldr:
        m = re.search(r'##?\s*(?:TL;?DR|Summary)\s*\n+(.+?)(?:\n\n|\n##)', body, re.I)
        if m: tldr = m.group(1).strip()[:200]
    bullets = []
    for m in re.finditer(r'^[-*]\s+(.{20,200})$', body, re.M):
        bullets.append(m.group(1).strip().strip('*'))
    for m in re.finditer(r'^\d+\.\s+(.{20,200})$', body, re.M):
        bullets.append(m.group(1).strip().strip('*'))
    metrics = []
    for m in re.finditer(r'[\d.]+[%xX]|\$[\d,.]+|[\d,]+\s*(?:ms|MB|KB|GB|tokens?|req/s)', body):
        s, e = max(0, m.start()-40), min(len(body), m.end()+40)
        ctx = body[s:e].replace('\n',' ').strip()
        if len(ctx) > 15: metrics.append(ctx)
    seen = set()
    ub = []
    for b in bullets:
        k = b[:50].lower()
        if k not in seen: seen.add(k); ub.append(b)
    sm = set()
    um = []
    for m in metrics:
        k = m[:30].lower()
        if k not in sm: sm.add(k); um.append(m)
    return {'tldr': tldr[:300], 'axioms': ub[:12], 'metrics': um[:6]}

def build_axiom(fm, ax, dest_type, dest_name):
    title = fm.get('title', 'Untitled')
    ref_dir = 'records/pool/contexts' if dest_type == 'ctx' else 'records/pool/reports'
    tags = fm.get('tags', [])
    if isinstance(tags, str): tags = [tags]
    lines = ['---', f'id: {fm.get("id","unknown")}', 'type: knowledge_card',
        f'title: "{title}"', f'domain: {fm.get("domain","general")}',
        f'satellite: {fm.get("satellite","UNKNOWN")}', 'quality: 8.5',
        f'tags: {tags}', f'created: {date.today().isoformat()}',
        f'updated: {date.today().isoformat()}', 'author: STELLA',
        f'source_doc: {ref_dir}/{dest_name}', '---', '', f'# {title}', '']
    if ax['tldr']: lines += [f'> {ax["tldr"]}', '']
    if ax['axioms']:
        lines += ['## Axioms', '']
        lines += [f'- {a}' for a in ax['axioms']]
        lines += ['']
    if ax['metrics']:
        lines += ['## Key Metrics', '']
        lines += [f'- {m}' for m in ax['metrics']]
        lines += ['']
    lines += ['## Reference', f'Full document: `{ref_dir}/{dest_name}`', '']
    return '\n'.join(lines)

def main():
    kc_dir = 'records/pool/knowledge'
    dry_run = '--apply' not in sys.argv
    if len(sys.argv) > 1 and not sys.argv[1].startswith('-'):
        kc_dir = sys.argv[1]
    pool_root = kc_dir.replace('/knowledge','').replace('\knowledge','')
    print(f'KC Reclassifier - {"DRY RUN" if dry_run else "APPLY"}')
    print(f'Source: {kc_dir}')
    kcs = sorted(glob.glob(os.path.join(kc_dir, 'KC_*.md')))
    targets = [f for f in kcs if os.path.getsize(f) > KC_MAX]
    print(f'Targets: {len(targets)} oversized KCs\n')
    stats = {'ctx': 0, 'rpt': 0, 'ok': 0}
    for fp in targets:
        with open(fp, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        size = len(content.encode('utf-8'))
        fm, body = parse_fm(content)
        ax = extract_axioms(body, fm)
        name = os.path.basename(fp)
        if size > 51200:
            dt, prefix = 'rpt', 'RPT'
        else:
            dt, prefix = 'ctx', 'CTX'
        dest_name = name.replace('KC_', f'{prefix}_')
        dest_path = os.path.join(pool_root, 'reports' if dt=='rpt' else 'contexts', dest_name)
        axiom = build_axiom(fm, ax, dt, dest_name)
        asize = len(axiom.encode('utf-8'))
        stats[dt] += 1
        if asize <= KC_MAX: stats['ok'] += 1
        st = 'OK' if asize <= KC_MAX else f'OVER({asize}B)'
        print(f'  {dt:3s} {size:6d}B -> {asize:5d}B [{st}] {len(ax["axioms"])}ax {len(ax["metrics"])}mt  {name}')
        if not dry_run:
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(fp, dest_path)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(axiom)
    total = stats['ctx'] + stats['rpt']
    print(f'\nSummary: {total} reclassified ({stats["ctx"]} ctx + {stats["rpt"]} rpt)')
    print(f'  Axiom KCs compliant: {stats["ok"]}/{total}')
    if dry_run: print('\nUse --apply to execute')

if __name__ == '__main__':
    main()
