#!/usr/bin/env python3
"""CEX Discovery Engine -- finds infinite improvement opportunities.

Unlike static task lists, this engine DISCOVERS what to improve each cycle
by analyzing the current state of the repo. Never converges because each
improvement creates new opportunities.

Usage:
  python _tools/cex_discovery.py next 6        # get 6 highest-value tasks
  python _tools/cex_discovery.py stats          # show opportunity counts
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Any

CEX_ROOT = Path(__file__).resolve().parent.parent
KINDS_META = CEX_ROOT / ".cex" / "kinds_meta.json"


def load_kinds() -> dict[str, Any]:
    return json.loads(KINDS_META.read_text(encoding="utf-8"))


def scan_artifacts() -> list[dict[str, Any]]:
    """Scan all artifacts, extract metadata."""
    km = load_kinds()
    artifacts = []
    for root, dirs, files in os.walk(CEX_ROOT):
        if any(skip in root for skip in ['.git', '.cex/cache', 'compiled', '_external', 'node_modules']):
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            path = os.path.join(root, f)
            try:
                content = open(path, encoding='utf-8', errors='ignore').read()
                if '---' not in content[:10]:
                    continue
                m_kind = re.search(r'kind:\s*(\S+)', content)
                m_qual = re.search(r'quality:\s*(null|[\d.]+)', content)
                m_ver = re.search(r'version:\s*(\S+)', content)
                kind = m_kind.group(1) if m_kind else 'unknown'
                quality = m_qual.group(1) if m_qual else 'none'
                version = m_ver.group(1) if m_ver else '0.0.0'
                lines = len(content.splitlines())
                tables = content.count('|') // 3
                body_lower = content.lower()
                all_kinds = set(km.keys())
                mentioned_kinds = [k for k in all_kinds
                                   if k.replace('_', ' ') in body_lower or k in body_lower]
                own_kind = kind
                cross_refs = [k for k in mentioned_kinds if k != own_kind]
                has_see_also = '## see also' in body_lower or '## related' in body_lower
                has_boundary = '## Boundary' in content
                has_8f = '## 8F' in content
                artifacts.append({
                    'path': os.path.relpath(path, CEX_ROOT),
                    'kind': kind, 'quality': quality, 'version': version,
                    'lines': lines, 'tables': tables,
                    'cross_refs': cross_refs, 'has_see_also': has_see_also,
                    'has_boundary': has_boundary, 'has_8': has_8f,
                    'content_hash': hash(content[:500])
                })
            except Exception:
                pass
    return artifacts


def discover_opportunities(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Find all improvement opportunities, ranked by value."""
    opportunities = []

    for a in artifacts:
        path = a['path']
        score = 0
        actions = []

        # CROSS-POLLINATION: mentions kinds but no See Also section
        if len(a['cross_refs']) >= 2 and not a['has_see_also']:
            score += len(a['cross_refs']) * 2
            refs_str = ', '.join(a['cross_refs'][:5])
            actions.append(f"wire-crossref:{refs_str}")

        # TABLE INJECTION: >30 lines but 0 tables
        if a['lines'] > 30 and a['tables'] == 0:
            score += 15
            actions.append("add-table")

        # VERSION BUMP: v1.0.0 with quality 9.0+ = ready for v1.1.0
        q = 0
        try:
            q = float(a['quality'])
        except (ValueError, TypeError):
            pass
        if q >= 9.0 and a['version'] == '1.0.0' and a['lines'] >= 80:
            score += 5
            actions.append("version-bump")

        # DENSITY PUSH: has tables but few rows
        if 0 < a['tables'] < 5 and a['lines'] > 50:
            score += 8
            actions.append("expand-tables")

        # MISSING STRUCTURE: no boundary or 8F
        if not a['has_boundary'] and a['kind'] != 'unknown':
            score += 3
            actions.append("add-boundary")
        if not a['has_8'] and a['kind'] != 'unknown':
            score += 3
            actions.append("add-8f-mapping")

        # EXPAND: under 60 lines with quality < 9
        if a['lines'] < 60 and q > 0 and q < 9.0:
            score += 10
            actions.append("expand-content")

        if actions:
            opportunities.append({
                'path': path, 'score': score, 'actions': actions,
                'kind': a['kind'], 'quality': a['quality'], 'lines': a['lines']
            })

    opportunities.sort(key=lambda x: -x['score'])
    return opportunities


def generate_tasks(opportunities: list[dict[str, Any]], n: int = 6) -> list[dict[str, Any]]:
    """Generate n task files from top opportunities."""
    km = load_kinds()
    nuclei = ['n01', 'n02', 'n03', 'n04', 'n05', 'n06']
    tasks = []

    for i, opp in enumerate(opportunities[:n]):
        nuc = nuclei[i % 6]
        path = opp['path']
        actions = opp['actions']

        task_lines = [f"Improve: {path}", f"Current: {opp['lines']} lines, quality {opp['quality']}", ""]

        if 'add-table' in actions:
            task_lines.append("ADD a comparison table relevant to this topic. At least 4 columns and 5 rows.")

        if 'wire-crossre' in actions:
            ref_action = [a for a in actions if a.startswith('wire-crossref:')][0]
            refs = ref_action.split(':')[1]
            task_lines.append(f"ADD a '## Related Kinds' section listing: {refs}")
            task_lines.append("For each, write 1 sentence explaining the relationship.")

        if 'expand-tables' in actions:
            task_lines.append("EXPAND existing tables: add more rows and columns with specific data.")

        if 'expand-content' in actions:
            task_lines.append("EXPAND to at least 80 lines. Add examples, use cases, comparison tables.")

        if 'version-bump' in actions:
            task_lines.append("UPDATE version from 1.0.0 to 1.1.0. Add a ## Changelog section.")

        task_lines.append("")
        task_lines.append("English only. Tables > prose. Keep YAML frontmatter.")

        task_path = os.path.join(str(CEX_ROOT), f"{nuc}_task.md")
        with open(task_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(task_lines))
        tasks.append({'nuc': nuc, 'path': path, 'actions': actions, 'score': opp['score']})

    return tasks


def cmd_stats() -> None:
    artifacts = scan_artifacts()
    opps = discover_opportunities(artifacts)
    total_score = sum(o['score'] for o in opps)
    action_counts = {}
    for o in opps:
        for a in o['actions']:
            key = a.split(':')[0]
            action_counts[key] = action_counts.get(key, 0) + 1

    print("=== CEX Discovery Engine ===")
    print(f"Artifacts scanned: {len(artifacts)}")
    print(f"Opportunities found: {len(opps)}")
    print(f"Total improvement score: {total_score}")
    print("")
    print("By action type:")
    for action, count in sorted(action_counts.items(), key=lambda x: -x[1]):
        print(f"  {action:<20} {count:>5} opportunities")


def cmd_next(n: int = 6) -> None:
    artifacts = scan_artifacts()
    opps = discover_opportunities(artifacts)
    tasks = generate_tasks(opps, n)
    print(f"Generated {len(tasks)} tasks:")
    for t in tasks:
        actions_str = ', '.join(a.split(':')[0] for a in t['actions'])
        print(f"  {t['nuc']} -> {t['path']}")
        print(f"         score={t['score']} actions=[{actions_str}]")


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'stats'
    if cmd == 'stats':
        cmd_stats()
    elif cmd == 'next':
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
        cmd_next(n)
    else:
        print("Usage: python _tools/cex_discovery.py {stats|next [N]}")
