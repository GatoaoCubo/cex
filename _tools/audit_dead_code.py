"""Audit W1 DEAD CODE: detect orphan py + md files.

Reads inventory_full.jsonl. Builds import graph (py) + reference graph (md).
Cross-checks against entry points (CLI, boot wrappers, slash commands, CI).
Emits dead_python.md + orphan_markdown.md with KEEP/DELETE/INVESTIGATE verdicts.
"""
from __future__ import annotations

import ast
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "_reports" / "audit" / "inventory_full.jsonl"
OUT_PY = ROOT / "_reports" / "audit" / "dead_python.md"
OUT_MD = ROOT / "_reports" / "audit" / "orphan_markdown.md"

LEAF_BASENAMES = {
    "claude.md", "agents.md", "readme.md", "license", "license.md",
    "contributing.md", "code_of_conduct.md", "memory.md", "changelog.md",
}
LEAF_PATTERNS = [
    re.compile(r"agent_card_n0\d\.md$"),
    re.compile(r"_INDEX\.md$", re.IGNORECASE),
    re.compile(r"^bld_(manifest|instruction|system_prompt)_"),
    re.compile(r"^bld_"),
    re.compile(r"^tpl_"),
    re.compile(r"^iso_"),
    re.compile(r"^kc_"),
    re.compile(r"^ar_"),
    re.compile(r"^sp_"),
    re.compile(r"^p\d{2}_"),
    re.compile(r"-builder\.md$"),
    re.compile(r"_schema\.yaml$"),
]
LEAF_DIRS = {
    ".claude/agents",
    ".claude/skills",
    ".claude/commands",
    ".claude/rules",
    ".claude/nucleus-settings",
    ".claude/compiled",
    ".cex/skills",
    ".cex/config",
    ".cex/brand",
    ".cex/instance",
    ".cex/memory",
    "archetypes/builders",
    "boot",
}
SKIP_MD_DIRS = {"_reports", "compiled", ".cex/runtime", ".cex/archive",
                ".cex/cache", ".cex/quality", ".cex/temp", ".cex/learning_records",
                ".cex/experiments", ".cex/benchmarks", ".cex/overnight",
                "examples"}


def load_inventory() -> list[dict]:
    """Stream inventory_full.jsonl into memory."""
    records = []
    with INVENTORY.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def py_module_name(rel_path: str) -> str:
    """Map _tools/cex_doctor.py -> _tools.cex_doctor (without .py)."""
    if rel_path.endswith(".py"):
        rel_path = rel_path[:-3]
    return rel_path.replace("/", ".")


def py_file_imports(file_path: Path) -> set[str]:
    """Parse a python file and return top-level module imports."""
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(text)
    except (SyntaxError, OSError):
        return set()
    out: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                out.add(alias.name.split(".")[0])
                if "." in alias.name:
                    out.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                out.add(node.module.split(".")[0])
                out.add(node.module)
    return out


def has_main_guard(file_path: Path) -> bool:
    """Check if file has if __name__ == '__main__': block."""
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return '__name__ == "__main__"' in text or "__name__ == '__main__'" in text


def grep_basename_anywhere(basename_no_ext: str) -> int:
    """Count text references to a name across non-py / non-vendored sources."""
    try:
        result = subprocess.run(
            ["git", "grep", "-l", "--", basename_no_ext,
             "--", "*.md", "*.ps1", "*.sh", "*.cmd", "*.yaml", "*.yml", "*.json"],
            cwd=ROOT, capture_output=True, text=True, timeout=15,
        )
        if result.returncode not in (0, 1):
            return 0
        return len([line for line in result.stdout.splitlines() if line.strip()])
    except (subprocess.TimeoutExpired, OSError):
        return 0


def build_py_graph(records: list[dict]) -> dict:
    """Build python file dependency graph from inventory records."""
    py_files = [r for r in records if r["path"].endswith(".py")
                and not r["path"].startswith((".venv", ".aider"))]
    by_module: dict[str, str] = {}
    for r in py_files:
        mod = py_module_name(r["path"])
        by_module[mod] = r["path"]
        if "/" in r["path"]:
            short = r["path"].split("/")[-1][:-3]
            by_module.setdefault(short, r["path"])

    inbound: dict[str, set[str]] = defaultdict(set)
    entrypoints: set[str] = set()

    for r in py_files:
        p = ROOT / r["path"]
        imports = py_file_imports(p)
        for imp in imports:
            target = by_module.get(imp)
            if target and target != r["path"]:
                inbound[target].add(r["path"])
        if has_main_guard(p):
            entrypoints.add(r["path"])
        if r["path"].startswith("_spawn/"):
            entrypoints.add(r["path"])

    return {
        "files": py_files,
        "by_module": by_module,
        "inbound": inbound,
        "entrypoints": entrypoints,
    }


def py_external_refs(rel_path: str) -> int:
    """Count refs to a python file from non-py sources (commands, ps1, ci)."""
    basename = rel_path.split("/")[-1][:-3]
    return grep_basename_anywhere(basename)


def write_py_report(graph: dict) -> None:
    """Emit dead_python.md."""
    rows = []
    for r in graph["files"]:
        path = r["path"]
        in_count = len(graph["inbound"].get(path, set()))
        is_entry = path in graph["entrypoints"]
        ext_refs = py_external_refs(path) if (in_count == 0 and not is_entry) else -1
        if is_entry:
            verdict = "KEEP-entrypoint"
            why = "has __main__ or in _spawn/"
        elif in_count > 0:
            verdict = "KEEP-imported"
            why = f"{in_count} in-bound import(s)"
        elif ext_refs > 0:
            verdict = "INVESTIGATE"
            why = f"0 imports but {ext_refs} non-py ref(s) -- may be dynamic"
        else:
            verdict = "DELETE"
            why = "0 imports, no entrypoint, 0 external refs"
        rows.append({
            "path": path,
            "lines": r["lines"],
            "in": in_count,
            "ext": ext_refs if ext_refs >= 0 else "-",
            "verdict": verdict,
            "why": why,
        })

    rows.sort(key=lambda x: (x["verdict"] != "DELETE", x["verdict"], x["path"]))

    counts = defaultdict(int)
    for row in rows:
        counts[row["verdict"]] += 1

    lines = [
        "# W1 DEAD PYTHON",
        "",
        f"Generated from `_reports/audit/inventory_full.jsonl`. {len(rows)} python files scanned.",
        "",
        "## Summary",
        "",
        "| Verdict | Count |",
        "|---|---|",
    ]
    for v, n in sorted(counts.items(), key=lambda x: -x[1]):
        lines.append(f"| {v} | {n} |")
    lines.append("")
    lines.append("## Files")
    lines.append("")
    lines.append("| Path | Lines | In-bound | External refs | Verdict | Why |")
    lines.append("|------|-------|----------|---------------|---------|-----|")
    for row in rows:
        lines.append(f"| `{row['path']}` | {row['lines']} | {row['in']} | "
                     f"{row['ext']} | {row['verdict']} | {row['why']} |")
    lines.append("")
    lines.append("## DEAD_PYTHON_PASS")

    OUT_PY.parent.mkdir(parents=True, exist_ok=True)
    OUT_PY.write_text("\n".join(lines), encoding="utf-8")
    print(f"[W1] py report written: {OUT_PY}")


def is_leaf_md(rel_path: str) -> bool:
    """Decide if a md file is a documented leaf (never orphan)."""
    norm = rel_path.replace("\\", "/")
    if any(norm.startswith(d + "/") for d in LEAF_DIRS):
        return True
    base = norm.split("/")[-1].lower()
    if base in LEAF_BASENAMES:
        return True
    return any(pat.search(base) for pat in LEAF_PATTERNS)


def in_skip_dir(rel_path: str) -> bool:
    """Skip output/runtime dirs from orphan check."""
    norm = rel_path.replace("\\", "/")
    return any(norm.startswith(d + "/") or norm == d for d in SKIP_MD_DIRS)


def resolve_md_ref(src_path: str, ref: str) -> str | None:
    """Resolve a markdown link relative to its source file."""
    ref = ref.strip()
    if not ref or ref.startswith(("http", "mailto:", "#")):
        return None
    if ref.startswith("/"):
        target = ref.lstrip("/")
    else:
        src_dir = "/".join(src_path.split("/")[:-1])
        target = f"{src_dir}/{ref}" if src_dir else ref
    parts = []
    for part in target.split("/"):
        if part == "..":
            if parts:
                parts.pop()
        elif part and part != ".":
            parts.append(part)
    return "/".join(parts)


def build_md_graph(records: list[dict]) -> dict:
    """Build markdown reference graph."""
    md_files = [r for r in records if r["path"].endswith(".md")]
    md_paths = {r["path"] for r in md_files}
    inbound: dict[str, set[str]] = defaultdict(set)

    for r in md_files:
        src = r["path"]
        for ref in r.get("refs", []):
            resolved = resolve_md_ref(src, ref)
            if resolved and resolved in md_paths:
                inbound[resolved].add(src)
    return {"files": md_files, "inbound": inbound}


def write_md_report(graph: dict) -> None:
    """Emit orphan_markdown.md."""
    rows = []
    for r in graph["files"]:
        path = r["path"]
        if in_skip_dir(path):
            continue
        in_count = len(graph["inbound"].get(path, set()))
        leaf = is_leaf_md(path)
        if leaf:
            verdict = "KEEP-leaf"
            why = "documented leaf (README/LICENSE/agent_card/builder ISO/etc)"
        elif in_count > 0:
            verdict = "KEEP-referenced"
            why = f"{in_count} in-bound markdown link(s)"
        else:
            verdict = "INVESTIGATE"
            why = "0 in-bound md links and not a known leaf"
        rows.append({
            "path": path,
            "lines": r["lines"],
            "in": in_count,
            "verdict": verdict,
            "why": why,
        })

    counts = defaultdict(int)
    for row in rows:
        counts[row["verdict"]] += 1

    rows.sort(key=lambda x: (x["verdict"] != "INVESTIGATE", x["path"]))

    lines = [
        "# W1 ORPHAN MARKDOWN",
        "",
        f"Generated from `_reports/audit/inventory_full.jsonl`. "
        f"{len(rows)} md files in scope (skipped: _reports, compiled, runtime, "
        f"archive, cache, quality, temp, examples, learning_records, experiments).",
        "",
        "## Summary",
        "",
        "| Verdict | Count |",
        "|---|---|",
    ]
    for v, n in sorted(counts.items(), key=lambda x: -x[1]):
        lines.append(f"| {v} | {n} |")
    lines.append("")
    lines.append("## INVESTIGATE candidates (0 in-bound, not a leaf)")
    lines.append("")
    lines.append("| Path | Lines | In-bound | Why |")
    lines.append("|------|-------|----------|-----|")
    investigate = [r for r in rows if r["verdict"] == "INVESTIGATE"]
    for row in investigate[:500]:
        lines.append(f"| `{row['path']}` | {row['lines']} | {row['in']} | {row['why']} |")
    if len(investigate) > 500:
        lines.append(f"| ... | ... | ... | (+{len(investigate) - 500} more truncated) |")
    lines.append("")
    lines.append("## ORPHAN_MARKDOWN_PASS")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"[W1] md report written: {OUT_MD}")


def main() -> int:
    """Run W1 dead-code detection on the inventory."""
    print("[W1] loading inventory...")
    records = load_inventory()
    print(f"[W1] {len(records)} records loaded")

    print("[W1] building py graph...")
    py_graph = build_py_graph(records)
    print(f"[W1] py: {len(py_graph['files'])} files, "
          f"{len(py_graph['entrypoints'])} entrypoints")

    print("[W1] writing py report (with external-ref grep)...")
    write_py_report(py_graph)

    print("[W1] building md graph...")
    md_graph = build_md_graph(records)
    print(f"[W1] md: {len(md_graph['files'])} files")

    print("[W1] writing md report...")
    write_md_report(md_graph)

    print("[W1] DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
