#!/usr/bin/env python3
"""KC Analyzer: Categorize knowledge cards by size and recommend actions.

Reads all KC_*.md files and produces a triage report:
- COMPLIANT: <5KB, no action needed
- TRIM: 5-10KB, remove fluff
- SPLIT: 10-50KB, split into multiple KCs
- DECOMPOSE: >50KB, reclassify as report/context_doc + extract KCs
"""

import os
import sys
import glob
import re
from pathlib import Path

def analyze_kc(filepath):
    """Analyze a single KC file."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    size = len(content.encode('utf-8'))
    lines = content.split('\n')
    
    # Count sections
    h1 = sum(1 for l in lines if l.startswith('# '))
    h2 = sum(1 for l in lines if l.startswith('## '))
    h3 = sum(1 for l in lines if l.startswith('### '))
    
    # Count code blocks
    code_blocks = content.count('```')  // 2
    
    # Extract frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    fm_size = len(fm_match.group(0).encode('utf-8')) if fm_match else 0
    
    # Content density: non-whitespace ratio
    stripped = content.replace(' ', '').replace('\n', '').replace('\t', '')
    density = len(stripped) / max(len(content), 1)
    
    # Categorize
    if size <= 5120:
        action = 'COMPLIANT'
    elif size <= 10240:
        action = 'TRIM'
    elif size <= 51200:
        action = 'SPLIT'
    else:
        action = 'DECOMPOSE'
    
    # Extract satellite from filename
    fname = os.path.basename(filepath)
    sat_match = re.match(r'KC_([A-Z]+)_', fname)
    satellite = sat_match.group(1) if sat_match else 'UNKNOWN'
    
    return {
        'file': fname,
        'path': filepath,
        'size': size,
        'size_kb': round(size / 1024, 1),
        'lines': len(lines),
        'sections': h1 + h2 + h3,
        'h1': h1, 'h2': h2, 'h3': h3,
        'code_blocks': code_blocks,
        'density': round(density, 2),
        'frontmatter_size': fm_size,
        'satellite': satellite,
        'action': action,
    }

def main():
    kc_dir = sys.argv[1] if len(sys.argv) > 1 else 'records/pool/knowledge'
    
    # Find all KCs
    kcs = sorted(glob.glob(os.path.join(kc_dir, 'KC_*.md')))
    
    if not kcs:
        print(f"No KC files found in {kc_dir}")
        return
    
    results = [analyze_kc(f) for f in kcs]
    
    # Group by action
    groups = {}
    for r in results:
        groups.setdefault(r['action'], []).append(r)
    
    # Print report
    print("=" * 70)
    print("KC ANALYZER REPORT")
    print("=" * 70)
    print(f"Total KCs: {len(results)}")
    print(f"Total size: {sum(r['size'] for r in results) / 1024 / 1024:.1f} MB")
    print()
    
    for action in ['COMPLIANT', 'TRIM', 'SPLIT', 'DECOMPOSE']:
        items = groups.get(action, [])
        total_mb = sum(r['size'] for r in items) / 1024 / 1024
        print(f"  {action:12s}: {len(items):4d} KCs ({total_mb:.1f} MB)")
    
    print()
    
    # By satellite
    print("--- By Satellite ---")
    sat_stats = {}
    for r in results:
        sat = r['satellite']
        sat_stats.setdefault(sat, {'total': 0, 'compliant': 0, 'size': 0})
        sat_stats[sat]['total'] += 1
        sat_stats[sat]['size'] += r['size']
        if r['action'] == 'COMPLIANT':
            sat_stats[sat]['compliant'] += 1
    
    for sat in sorted(sat_stats, key=lambda s: sat_stats[s]['total'], reverse=True):
        s = sat_stats[sat]
        pct = s['compliant'] * 100 // max(s['total'], 1)
        print(f"  {sat:8s}: {s['total']:4d} total, {s['compliant']:3d} compliant ({pct}%), {s['size']/1024/1024:.1f} MB")
    
    print()
    
    # Top 10 largest
    print("--- Top 10 Largest (DECOMPOSE candidates) ---")
    for r in sorted(results, key=lambda x: x['size'], reverse=True)[:10]:
        print(f"  {r['size_kb']:6.1f}KB  {r['sections']:2d} sections  {r['code_blocks']:2d} code blocks  {r['file']}")
    
    print()
    
    # Estimated work
    trim_count = len(groups.get('TRIM', []))
    split_count = len(groups.get('SPLIT', []))
    decompose_count = len(groups.get('DECOMPOSE', []))
    
    print("--- Estimated Work ---")
    print(f"  TRIM ({trim_count}): ~{trim_count * 2} min (automated: remove boilerplate, compress)")
    print(f"  SPLIT ({split_count}): ~{split_count * 5} min (semi-auto: identify sections, create new KCs)")
    print(f"  DECOMPOSE ({decompose_count}): ~{decompose_count * 15} min (manual: reclassify, extract axioms)")
    total_min = trim_count * 2 + split_count * 5 + decompose_count * 15
    print(f"  TOTAL: ~{total_min} min ({total_min/60:.1f} hours)")

if __name__ == '__main__':
    main()
