#!/usr/bin/env python3
"""Batch KC generator — runs N prompts through claude -p and splits output into files."""
import subprocess, sys, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "P01_knowledge" / "library"

def generate_and_split(prompt_path: str, target_subdir: str):
    prompt = Path(prompt_path).read_text(encoding="utf-8")
    print(f"  Sending to claude -p ({len(prompt)} chars)...")
    
    r = subprocess.run(
        ["claude", "-p", "--model", "claude-sonnet-4-20250514", "--no-chrome"],
        input=prompt, capture_output=True, text=True, timeout=120, encoding="utf-8",
    )
    if r.returncode != 0:
        print(f"  ERROR: {r.stderr[:200]}")
        return 0
    
    raw = r.stdout
    # Split on ===FILE: name.md===
    parts = re.split(r'===FILE:\s*(\S+\.md)===', raw)
    # parts = ['', 'name1.md', 'content1', 'name2.md', 'content2', ...]
    
    out_path = OUT_DIR / target_subdir
    out_path.mkdir(parents=True, exist_ok=True)
    
    count = 0
    for i in range(1, len(parts), 2):
        filename = parts[i].strip()
        content = parts[i+1].strip() if i+1 < len(parts) else ""
        if content:
            fpath = out_path / filename
            fpath.write_text(content, encoding="utf-8")
            print(f"  ✅ {fpath.relative_to(ROOT)} ({len(content)} bytes)")
            count += 1
    return count

if __name__ == "__main__":
    prompt_file = sys.argv[1]
    subdir = sys.argv[2] if len(sys.argv) > 2 else "frontend"
    n = generate_and_split(prompt_file, subdir)
    print(f"  Generated {n} files")
