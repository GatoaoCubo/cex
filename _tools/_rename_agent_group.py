#!/usr/bin/env python3
"""
N03 Task: Rename satellite/agent_node -> agent_group across codebase.
Gap G13 fix. 600+ files.

Replacement order matters: plurals before singulars to avoid partial matches.
"""
import os
import re
import sys

# Replacement pairs: (pattern, replacement)
# Order: plurals first, then singulars; longer before shorter
REPLACEMENTS = [
    # === AGENT_NODE variants (plurals first) ===
    (r'AGENT_NODES', 'AGENT_GROUPS'),
    (r'agent_nodes', 'agent_groups'),
    (r'Agent_nodes', 'Agent_groups'),
    # singulars
    (r'AGENT_NODE', 'AGENT_GROUP'),
    (r'agent_node', 'agent_group'),
    (r'Agent_node', 'Agent_group'),

    # === SATELLITE variants (plurals first) ===
    (r'SATELLITES', 'AGENT_GROUPS'),
    (r'Satellites', 'Agent_groups'),
    (r'satellites', 'agent_groups'),
    # singulars
    (r'SATELLITE', 'AGENT_GROUP'),
    (r'Satellite', 'Agent_group'),
    (r'satellite', 'agent_group'),

    # === Portuguese forms in translate_isos.py ===
    (r'satelites', 'agent_groups'),
    (r'satelite', 'agent_group'),
]

# Directories/files to skip
SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
SKIP_FILES = {'_rename_agent_group.py'}  # don't rename ourselves

# File extensions to process
EXTENSIONS = {'.md', '.yaml', '.yml', '.json', '.py', '.ps1', '.sh', '.cmd', '.txt', '.tsv'}

def should_process(filepath):
    """Check if file should be processed."""
    parts = filepath.replace('\\', '/').split('/')
    for skip in SKIP_DIRS:
        if skip in parts:
            return False
    basename = os.path.basename(filepath)
    if basename in SKIP_FILES:
        return False
    _, ext = os.path.splitext(filepath)
    return ext.lower() in EXTENSIONS

def apply_replacements(text):
    """Apply all replacements to text."""
    result = text
    for pattern, replacement in REPLACEMENTS:
        result = result.replace(pattern, replacement)
    return result

def process_file(filepath):
    """Process a single file. Returns (changed, count) tuple."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, PermissionError):
        try:
            with open(filepath, 'r', encoding='utf-8-sig') as f:
                content = f.read()
        except:
            return False, 0

    new_content = apply_replacements(content)

    if new_content != content:
        # Count replacements
        count = 0
        for pattern, replacement in REPLACEMENTS:
            count += content.count(pattern)

        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            f.write(new_content)
        return True, count
    return False, 0

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    total_files = 0
    total_replacements = 0
    changed_files = []

    for dirpath, dirnames, filenames in os.walk('.'):
        # Prune skip dirs
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if not should_process(filepath):
                continue

            changed, count = process_file(filepath)
            if changed:
                total_files += 1
                total_replacements += count
                changed_files.append((filepath, count))

    # Report
    print(f"\n{'='*60}")
    print(f"  G13 Rename: satellite/agent_node -> agent_group")
    print(f"{'='*60}")
    print(f"  Files modified: {total_files}")
    print(f"  Total replacements: {total_replacements}")
    print(f"{'='*60}")

    # Top 20 most-changed files
    changed_files.sort(key=lambda x: x[1], reverse=True)
    print(f"\n  Top 20 most-changed files:")
    for fp, count in changed_files[:20]:
        print(f"    {count:4d}  {fp}")

    if total_files > 0:
        print(f"\n  ... and {max(0, total_files - 20)} more files")

    return 0

if __name__ == '__main__':
    sys.exit(main())
