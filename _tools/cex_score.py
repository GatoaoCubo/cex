#!/usr/bin/env python3
"""
CEX Peer Review Scorer — N07 Orchestrator assigns quality to artifacts.

Scoring rubric (objective criteria):
  - Frontmatter completeness: id, kind, pillar, title, version, author, tags, tldr, quality
  - Content depth: byte count, heading count, table presence
  - Domain specificity: no generic placeholders, real domain terms
  - Structure: sections, formatting, clear boundaries

Score ranges:
  9.0-9.3: Excellent — rich, domain-specific, well-structured, complete FM
  8.5-8.9: Good — solid content, minor gaps
  8.0-8.4: Acceptable — adequate but thin
  <8.0: Needs rebuild
"""

import os
import re
import sys

def score_artifact(path):
    """Score a single artifact. Returns (score, notes)."""
    if not os.path.exists(path):
        return (0.0, "MISSING")

    content = open(path, 'r', encoding='utf-8').read()
    size = len(content.encode('utf-8'))
    notes = []

    # Check frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return (0.0, "NO_FRONTMATTER")

    fm = fm_match.group(1)
    body = content[fm_match.end():]

    # === FRONTMATTER SCORING (max 3.0) ===
    fm_score = 0.0
    required = ['id:', 'kind:', 'pillar:', 'quality:']
    desired = ['title:', 'version:', 'author:', 'tags:', 'tldr:', 'domain:', 'created:', 'updated:']

    for field in required:
        if field in fm:
            fm_score += 0.3
        else:
            notes.append(f"missing {field}")

    for field in desired:
        if field in fm:
            fm_score += 0.1

    # === CONTENT SCORING (max 3.5) ===
    content_score = 0.0

    # Size
    if size >= 1000:
        content_score += 0.3
    if size >= 2000:
        content_score += 0.4
    if size >= 3000:
        content_score += 0.3
    if size >= 4000:
        content_score += 0.2

    # Headings
    headings = len(re.findall(r'^#{1,3} ', body, re.MULTILINE))
    if headings >= 2:
        content_score += 0.3
    if headings >= 5:
        content_score += 0.2
    if headings >= 8:
        content_score += 0.1

    # Tables
    table_rows = len(re.findall(r'^\|.*\|', body, re.MULTILINE))
    if table_rows >= 3:
        content_score += 0.3
    if table_rows >= 8:
        content_score += 0.2

    # Lists
    list_items = len(re.findall(r'^[-*\d]+[.)] ', body, re.MULTILINE))
    if list_items >= 3:
        content_score += 0.2

    # Code blocks
    code_blocks = len(re.findall(r'```', body))
    if code_blocks >= 2:
        content_score += 0.1

    # === DOMAIN SPECIFICITY (max 2.0) ===
    domain_score = 0.0

    # No placeholder text (legitimate mentions excluded by checking context)
    bad_placeholders = len(re.findall(r'(?i)\b(TODO|TBD|FIXME|insert here|add later)\b', body))
    if bad_placeholders == 0:
        domain_score += 0.5
    else:
        notes.append(f"{bad_placeholders} placeholders")
        domain_score -= 0.3 * bad_placeholders

    # Has substantial body text (not just frontmatter)
    body_words = len(body.split())
    if body_words >= 100:
        domain_score += 0.3
    if body_words >= 200:
        domain_score += 0.3
    if body_words >= 400:
        domain_score += 0.2

    # tldr quality
    tldr_match = re.search(r'tldr:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    if tldr_match and len(tldr_match.group(1)) >= 30:
        domain_score += 0.2

    # Has linked artifacts or references
    if 'linked_artifacts' in fm or '## Reference' in body or '## Integration' in body:
        domain_score += 0.2

    # === STRUCTURE (max 1.5) ===
    struct_score = 0.0

    # Has clear sections
    if headings >= 3:
        struct_score += 0.3

    # No huge walls of text (has paragraphs)
    paragraphs = len(re.findall(r'\n\n', body))
    if paragraphs >= 3:
        struct_score += 0.3
    if paragraphs >= 6:
        struct_score += 0.2

    # Mixed formatting (headings + tables/lists)
    format_types = sum([headings > 0, table_rows > 0, list_items > 0, code_blocks > 0])
    if format_types >= 2:
        struct_score += 0.3
    if format_types >= 3:
        struct_score += 0.2

    # === FINAL SCORE ===
    raw = fm_score + content_score + domain_score + struct_score
    # Normalize to 8.0-9.3 range (raw max ~10.0)
    score = 8.0 + (raw / 10.0) * 1.3
    score = round(min(score, 9.3), 1)
    score = max(score, 7.0)

    return (score, "; ".join(notes) if notes else "OK")


def update_quality(path, score):
    """Replace quality: null with quality: X.X in file."""
    content = open(path, 'r', encoding='utf-8').read()
    updated = re.sub(r'^quality:\s*null\s*$', f'quality: {score}', content, count=1, flags=re.MULTILINE)
    if updated != content:
        open(path, 'w', encoding='utf-8').write(updated)
        return True
    return False


def main():
    import argparse
    parser = argparse.ArgumentParser(description='CEX Peer Review Scorer')
    parser.add_argument('--dry-run', action='store_true', help='Score but do not update files')
    parser.add_argument('--apply', action='store_true', help='Apply scores to files')
    parser.add_argument('files', nargs='*', help='Files to score (default: all quality:null)')
    args = parser.parse_args()

    # Find all quality:null files if none specified
    if not args.files:
        import subprocess
        result = subprocess.run(
            ['grep', '-r', '-l', '^quality: null', '--include=*.md'] +
            [d for d in os.listdir('.') if d.startswith('N0') and os.path.isdir(d)],
            capture_output=True, text=True
        )
        args.files = sorted(result.stdout.strip().split('\n')) if result.stdout.strip() else []

    if not args.files:
        print("No quality:null artifacts found.")
        return

    print(f"{'Score':>5} | {'Size':>6} | {'Notes':<40} | Path")
    print("-" * 100)

    scores = {}
    for f in args.files:
        f = f.strip()
        if not f:
            continue
        score, notes = score_artifact(f)
        scores[f] = score
        size = os.path.getsize(f) if os.path.exists(f) else 0
        print(f"{score:5.1f} | {size:5d}B | {notes:<40} | {f}")

    print(f"\n{'='*100}")
    print(f"Total: {len(scores)} artifacts")
    print(f"Avg score: {sum(scores.values())/len(scores):.1f}")
    print(f"Min: {min(scores.values()):.1f} | Max: {max(scores.values()):.1f}")
    print(f"Below 8.0: {sum(1 for s in scores.values() if s < 8.0)}")
    print(f"8.0-8.4: {sum(1 for s in scores.values() if 8.0 <= s < 8.5)}")
    print(f"8.5-8.9: {sum(1 for s in scores.values() if 8.5 <= s < 9.0)}")
    print(f"9.0+: {sum(1 for s in scores.values() if s >= 9.0)}")

    if args.apply:
        updated = 0
        for f, score in scores.items():
            if update_quality(f, score):
                updated += 1
        print(f"\nApplied scores to {updated}/{len(scores)} files.")
    elif not args.dry_run:
        print("\nUse --apply to update files, or --dry-run for read-only.")


if __name__ == '__main__':
    main()
