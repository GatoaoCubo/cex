#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_kind_tool_map.py -- Scan _tools/cex_*.py for kind/pillar annotations.

Produces kind_tool_registry.json mapping tools to the kinds and pillars they
operate on. Used by F5 CALL to route artifact work to the correct tool.

Annotation formats (in module docstring, function docstring, or inline comment):
  kind: knowledge_card
  pillar: P01
  # kind: entity_memory
  # pillar: P10

Discovery layers (in priority order):
  L1  Explicit annotations (kind:/pillar: in docstrings and comments)
  L2  Heuristic match: known kind names from .cex/kinds_meta.json appearing
      in docstrings and string literals
  L3  Pillar inference: any P01-P12 token found in docstrings

CLI:
  python _tools/cex_kind_tool_map.py
  python _tools/cex_kind_tool_map.py --output .cex/kind_tool_registry.json
  python _tools/cex_kind_tool_map.py --verbose
  python _tools/cex_kind_tool_map.py --tool cex_score.py
"""

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

CEX_ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = CEX_ROOT / "_tools"
KINDS_META = CEX_ROOT / ".cex" / "kinds_meta.json"
DEFAULT_OUTPUT = CEX_ROOT / ".cex" / "kind_tool_registry.json"

PILLAR_RE = re.compile(r"\bP(0[1-9]|1[0-2])\b")
KIND_ANNOTATION_RE = re.compile(r"(?:^|#\s*)kind:\s*([a-z][a-z0-9_]+)", re.MULTILINE)
PILLAR_ANNOTATION_RE = re.compile(r"(?:^|#\s*)pillar:\s*(P(?:0[1-9]|1[0-2]))", re.MULTILINE)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def load_kinds_meta() -> dict[str, Any]:
    if not KINDS_META.exists():
        return {}
    with open(KINDS_META, encoding="utf-8") as f:
        return json.load(f)


def extract_module_docstring(source: str) -> str:
    """Return the module-level docstring, or empty string."""
    try:
        tree = ast.parse(source)
        return ast.get_docstring(tree) or ""
    except SyntaxError:
        return ""


def extract_all_docstrings(source: str) -> list[str]:
    """Return all docstrings from module, classes, and functions."""
    docs = []
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return docs
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(node)
            if doc:
                docs.append(doc)
    return docs


def extract_comments(source: str) -> list[str]:
    """Return lines that are pure comments (#...)."""
    result = []
    for line in source.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            result.append(stripped)
    return result


def scan_tool(
    path: Path,
    known_kinds: set[str],
) -> dict[str, Any]:
    """Analyse one tool file and return its kind/pillar mappings."""
    source = path.read_text(encoding="utf-8", errors="ignore")
    docstrings = extract_all_docstrings(source)
    comments = extract_comments(source)
    combined_docs = "\n".join(docstrings)
    combined_text = combined_docs + "\n" + "\n".join(comments)

    # L1 -- explicit annotations
    explicit_kinds: set[str] = set()
    explicit_pillars: set[str] = set()
    for m in KIND_ANNOTATION_RE.finditer(combined_text):
        candidate = m.group(1)
        if candidate in known_kinds:
            explicit_kinds.add(candidate)
    for m in PILLAR_ANNOTATION_RE.finditer(combined_text):
        explicit_pillars.add(m.group(1))

    # L2 -- heuristic: kind names from known_kinds appearing verbatim in docstrings
    heuristic_kinds: set[str] = set()
    if known_kinds:
        for kind in known_kinds:
            # Match as whole word or within underscored context
            pattern = r"\b" + re.escape(kind) + r"\b"
            if re.search(pattern, combined_docs, re.IGNORECASE):
                heuristic_kinds.add(kind)

    # L3 -- pillar tokens in docstrings
    inferred_pillars: set[str] = set(PILLAR_RE.findall(combined_docs))

    all_kinds = sorted(explicit_kinds | heuristic_kinds)
    all_pillars = sorted(explicit_pillars | inferred_pillars)

    return {
        "file": path.name,
        "kinds_explicit": sorted(explicit_kinds),
        "kinds_heuristic": sorted(heuristic_kinds - explicit_kinds),
        "kinds_all": all_kinds,
        "pillars_explicit": sorted(explicit_pillars),
        "pillars_inferred": sorted(inferred_pillars - explicit_pillars),
        "pillars_all": all_pillars,
        "module_doc": extract_module_docstring(source)[:300],
    }


def build_registry(
    tool_results: list[dict[str, Any]],
) -> dict[str, Any]:
    """Aggregate per-tool results into a registry with inverted indexes."""
    kind_to_tools: dict[str, list[str]] = {}
    pillar_to_tools: dict[str, list[str]] = {}
    tool_to_kinds: dict[str, list[str]] = {}
    tool_to_pillars: dict[str, list[str]] = {}

    for result in tool_results:
        tool = result["file"]
        kinds = result["kinds_all"]
        pillars = result["pillars_all"]

        tool_to_kinds[tool] = kinds
        tool_to_pillars[tool] = pillars

        for kind in kinds:
            kind_to_tools.setdefault(kind, [])
            if tool not in kind_to_tools[kind]:
                kind_to_tools[kind].append(tool)

        for pillar in pillars:
            pillar_to_tools.setdefault(pillar, [])
            if tool not in pillar_to_tools[pillar]:
                pillar_to_tools[pillar].append(tool)

    return {
        "schema": "kind_tool_registry/v1",
        "generated_by": "cex_kind_tool_map.py",
        "tool_count": len(tool_results),
        "kind_count": len(kind_to_tools),
        "pillar_count": len(pillar_to_tools),
        "kind_to_tools": dict(sorted(kind_to_tools.items())),
        "pillar_to_tools": dict(sorted(pillar_to_tools.items())),
        "tool_to_kinds": dict(sorted(tool_to_kinds.items())),
        "tool_to_pillars": dict(sorted(tool_to_pillars.items())),
        "per_tool": {r["file"]: r for r in tool_results},
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Scan _tools/cex_*.py for kind/pillar annotations and build registry."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output path for kind_tool_registry.json (default: .cex/kind_tool_registry.json)",
    )
    parser.add_argument(
        "--tool",
        type=str,
        default=None,
        help="Scan only this tool file (e.g. cex_score.py)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print per-tool breakdown",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print registry without writing to disk",
    )
    args = parser.parse_args(argv)

    # Load known kinds for heuristic matching
    known_kinds_meta = load_kinds_meta()
    known_kinds: set[str] = set(known_kinds_meta.keys())
    if not known_kinds:
        print("[WARN] kinds_meta.json not found or empty -- heuristic matching disabled")

    # Discover tool files
    if args.tool:
        candidates = [TOOLS_DIR / args.tool]
        candidates = [p for p in candidates if p.exists()]
    else:
        candidates = sorted(TOOLS_DIR.glob("cex_*.py"))

    if not candidates:
        print("[FAIL] No tool files found", file=sys.stderr)
        return 1

    # Scan
    tool_results = []
    for path in candidates:
        result = scan_tool(path, known_kinds)
        tool_results.append(result)
        if args.verbose:
            print(f"  {path.name}")
            print(f"    kinds ({len(result['kinds_all'])}): {result['kinds_all'][:10]}")
            print(f"    pillars ({len(result['pillars_all'])}): {result['pillars_all']}")

    # Build registry
    registry = build_registry(tool_results)

    # Output
    output_json = json.dumps(registry, indent=2, ensure_ascii=True)
    if args.dry_run:
        print(output_json)
        return 0

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output_json, encoding="utf-8")

    # Summary
    print(f"[OK] Registry written: {output_path}")
    print(f"     Tools scanned : {registry['tool_count']}")
    print(f"     Kinds indexed : {registry['kind_count']}")
    print(f"     Pillars indexed: {registry['pillar_count']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
