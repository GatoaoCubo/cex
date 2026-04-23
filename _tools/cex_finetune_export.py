#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Fine-Tune Data Export -- Extract training pairs from builder ISOs.

For each of the 123 kinds, creates a training pair:
  Input:  kind name + schema definition (from kinds_meta.json + pillar schema)
  Output: bld_prompt_{kind}.md content (the ideal artifact spec)

Usage:
    python _tools/cex_finetune_export.py
    python _tools/cex_finetune_export.py --output _data/finetune/cex_builder_pairs.jsonl
    python _tools/cex_finetune_export.py --stats

Output: JSONL file with {"input": "...", "output": "..."} per line.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
BUILDERS_DIR = ROOT / "archetypes" / "builders"
KINDS_META = ROOT / ".cex" / "kinds_meta.json"
DEFAULT_OUTPUT = ROOT / "_data" / "finetune" / "cex_builder_pairs.jsonl"


def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token for English text."""
    return len(text) // 4


def load_kinds_meta() -> dict[str, Any]:
    """Load the kinds registry."""
    if not KINDS_META.exists():
        print(f"[FAIL] kinds_meta.json not found: {KINDS_META}", file=sys.stderr)
        sys.exit(1)
    return json.loads(KINDS_META.read_text(encoding="utf-8"))


def find_builder_dirs() -> list[Path]:
    """Find all builder directories (exclude _shared, compiled, etc.)."""
    dirs = []
    for d in sorted(BUILDERS_DIR.iterdir()):
        if d.is_dir() and d.name.endswith("-builder") and not d.name.startswith("_"):
            dirs.append(d)
    return dirs


def extract_kind_from_builder_name(builder_name: str) -> str:
    """agent-builder -> agent, knowledge-card-builder -> knowledge_card"""
    kind = builder_name.replace("-builder", "")
    return kind.replace("-", "_")


def build_input(kind_name: str, meta_entry: dict[str, Any]) -> str:
    """Build the input side of a training pair."""
    parts = [
        f"Kind: {kind_name}",
        f"Pillar: {meta_entry.get('pillar', 'unknown')}",
        f"Description: {meta_entry.get('description', 'No description')}",
        f"LLM Function: {meta_entry.get('llm_function', 'unknown')}",
        f"Max Bytes: {meta_entry.get('max_bytes', 0)}",
        f"Naming Pattern: {meta_entry.get('naming', 'unknown')}",
        f"Core: {meta_entry.get('core', False)}",
        f"Boundary: {meta_entry.get('boundary', 'No boundary defined')}",
    ]
    return "\n".join(parts)


def build_output(builder_dir: Path, kind_name: str) -> str | None:
    """Read the bld_prompt_{kind}.md file as output."""
    # Try exact name match
    instruction_file = builder_dir / f"bld_prompt_{kind_name}.md"
    if not instruction_file.exists():
        # Try with hyphens
        hyphen_name = kind_name.replace("_", "-")
        instruction_file = builder_dir / f"bld_prompt_{hyphen_name}.md"
    if not instruction_file.exists():
        # Search for any bld_prompt_*.md
        candidates = list(builder_dir.glob("bld_prompt_*.md"))
        if candidates:
            instruction_file = candidates[0]
        else:
            return None

    try:
        return instruction_file.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  [WARN] Could not read {instruction_file}: {e}", file=sys.stderr)
        return None


def main() -> None:
    parser = argparse.ArgumentParser(description="CEX Fine-Tune Data Export")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT),
                        help=f"Output JSONL path (default: {DEFAULT_OUTPUT})")
    parser.add_argument("--stats", action="store_true",
                        help="Print statistics only, don't write file")
    args = parser.parse_args()

    kinds_meta = load_kinds_meta()
    builder_dirs = find_builder_dirs()

    print(f"[INFO] kinds_meta: {len(kinds_meta)} kinds")
    print(f"[INFO] builder dirs: {len(builder_dirs)} found")

    pairs = []
    missing = []
    total_input_tokens = 0
    total_output_tokens = 0

    for bdir in builder_dirs:
        kind_name = extract_kind_from_builder_name(bdir.name)

        # Get meta entry
        meta = kinds_meta.get(kind_name, {})
        if not meta:
            print(f"  [WARN] No kinds_meta entry for: {kind_name}")
            missing.append(kind_name)
            continue

        # Build input
        input_text = build_input(kind_name, meta)

        # Build output
        output_text = build_output(bdir, kind_name)
        if output_text is None:
            print(f"  [WARN] No instruction file for: {kind_name}")
            missing.append(kind_name)
            continue

        input_tokens = estimate_tokens(input_text)
        output_tokens = estimate_tokens(output_text)
        total_input_tokens += input_tokens
        total_output_tokens += output_tokens

        pairs.append({
            "input": input_text,
            "output": output_text,
            "kind": kind_name,
            "pillar": meta.get("pillar", ""),
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
        })

    # Stats
    print(f"\n{'='*50}")
    print("FINE-TUNE EXPORT SUMMARY")
    print(f"{'='*50}")
    print(f"Total pairs: {len(pairs)}")
    print(f"Missing: {len(missing)}")
    if missing:
        print(f"  Missing kinds: {', '.join(missing[:10])}")
        if len(missing) > 10:
            print(f"  ... and {len(missing) - 10} more")
    print(f"Avg input tokens: {total_input_tokens // max(len(pairs), 1)}")
    print(f"Avg output tokens: {total_output_tokens // max(len(pairs), 1)}")
    print(f"Total input tokens: {total_input_tokens}")
    print(f"Total output tokens: {total_output_tokens}")

    # Coverage by pillar
    pillar_counts = {}
    for p in pairs:
        pillar = p.get("pillar", "unknown")
        pillar_counts[pillar] = pillar_counts.get(pillar, 0) + 1
    print("\nCoverage by pillar:")
    for pillar in sorted(pillar_counts):
        print(f"  {pillar}: {pillar_counts[pillar]} pairs")

    if args.stats:
        return

    # Write JSONL
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for p in pairs:
            record = {
                "input": p["input"],
                "output": p["output"],
            }
            f.write(json.dumps(record, ensure_ascii=True) + "\n")

    file_size = output_path.stat().st_size
    print(f"\n[OK] Written to: {output_path}")
    print(f"[OK] File size: {file_size:,} bytes ({file_size / 1024:.1f} KB)")
    print(f"[OK] Lines: {len(pairs)}")


if __name__ == "__main__":
    main()
