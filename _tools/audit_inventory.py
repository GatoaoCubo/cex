"""Audit W0 INVENTORY: walk repo and emit JSONL manifest.

One JSON object per file with path, size, lines, kind_guess, last_touched,
frontmatter_kind, refs. Excludes .git/.venv*/.aider*/node_modules/__pycache__.

Output: _reports/audit/inventory_full.jsonl
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {".git", ".venv_litellm", ".aider.tags.cache.v4",
                "node_modules", "__pycache__", ".pi", ".cex_signals"}
EXCLUDE_PATTERNS = [re.compile(p) for p in [
    r"\.aider\.",
    r"\.pyc$",
    r"\.lock$",
]]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
KIND_RE = re.compile(r"^kind:\s*(\S+)", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
IMPORT_RE = re.compile(r"^(?:from\s+(\S+)\s+import|import\s+(\S+))", re.MULTILINE)


def classify_path(p: Path) -> str:
    """Guess kind from path conventions."""
    parts = p.parts
    name = p.name.lower()
    if p.suffix == ".py":
        if "test_" in name or name.startswith("test_"):
            return "test"
        if "_tools" in parts:
            return "tool"
        if "_spawn" in parts:
            return "spawn"
        if "cex_sdk" in parts:
            return "sdk"
        return "py_other"
    if p.suffix in (".ps1", ".sh", ".cmd", ".bat"):
        return "script"
    if p.suffix == ".md":
        if "archetypes" in parts and "builders" in parts:
            return "builder_iso"
        if "library/kind" in str(p).replace("\\", "/"):
            return "kc"
        if ".claude" in parts and "rules" in parts:
            return "rule"
        if ".claude" in parts and "commands" in parts:
            return "command"
        if ".claude" in parts and "agents" in parts:
            return "agent_def"
        if ".claude" in parts and "skills" in parts:
            return "skill"
        if "_docs" in parts and "specs" in parts:
            return "spec"
        if "_reports" in parts:
            return "report"
        if "knowledge" in parts:
            return "kc"
        if "examples" in parts:
            return "example"
        if "compiled" in parts:
            return "compiled"
        if "runtime" in parts:
            return "runtime_doc"
        return "md_other"
    if p.suffix in (".yaml", ".yml"):
        if "schema" in name:
            return "schema"
        if ".cex/config" in str(p).replace("\\", "/"):
            return "config"
        if ".cex/runtime" in str(p).replace("\\", "/"):
            return "runtime_state"
        if ".github" in parts:
            return "ci"
        return "yaml_other"
    if p.suffix == ".json":
        if ".cex/runtime" in str(p).replace("\\", "/"):
            return "runtime_state"
        if ".cex" in parts:
            return "config"
        return "json_other"
    if p.suffix == ".jsonl":
        return "data_jsonl"
    if p.suffix == ".tsv":
        return "data_tsv"
    if p.suffix in (".png", ".jpg", ".gif", ".svg", ".webp"):
        return "image"
    if p.suffix == ".log":
        return "log"
    if p.suffix == ".txt":
        return "text"
    if name in ("readme", "license", "contributing", "code_of_conduct",
                "claude.md", "agents.md"):
        return "meta"
    return "unknown"


def extract_frontmatter_kind(text: str) -> str | None:
    """Read 'kind:' field from YAML frontmatter if present."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm = m.group(1)
    km = KIND_RE.search(fm)
    return km.group(1) if km else None


def extract_refs(text: str, suffix: str) -> list[str]:
    """Extract import targets (py) or markdown links (md)."""
    refs: list[str] = []
    if suffix == ".py":
        for m in IMPORT_RE.finditer(text):
            ref = m.group(1) or m.group(2)
            if ref and not ref.startswith("_"):
                refs.append(ref.split(".")[0])
    elif suffix == ".md":
        for m in LINK_RE.finditer(text):
            link = m.group(1).split("#")[0].strip()
            if link and not link.startswith(("http://", "https://", "mailto:")):
                refs.append(link)
    seen: set[str] = set()
    out: list[str] = []
    for r in refs:
        if r not in seen:
            seen.add(r)
            out.append(r)
    return out[:50]


def get_git_last_touched(p: Path) -> str | None:
    """Return ISO date of last git commit touching this file, or None."""
    try:
        rel = p.relative_to(ROOT).as_posix()
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", rel],
            cwd=ROOT, capture_output=True, text=True, timeout=5,
        )
        out = result.stdout.strip()
        return out if out else None
    except (subprocess.TimeoutExpired, OSError):
        return None


def should_skip(p: Path) -> bool:
    """Filter out excluded paths."""
    rel_parts = p.relative_to(ROOT).parts
    if any(part in EXCLUDE_DIRS for part in rel_parts):
        return True
    name = p.name
    return any(pat.search(name) for pat in EXCLUDE_PATTERNS)


def inventory_file(p: Path) -> dict:
    """Build inventory record for one file."""
    try:
        size = p.stat().st_size
    except OSError:
        size = 0
    record = {
        "path": p.relative_to(ROOT).as_posix(),
        "size_bytes": size,
        "lines": 0,
        "kind_guess": classify_path(p),
        "last_touched": None,
        "frontmatter_kind": None,
        "refs": [],
    }
    if size > 5_000_000:
        return record
    if p.suffix in (".png", ".jpg", ".gif", ".svg", ".webp", ".pdf",
                    ".zip", ".gz", ".whl", ".pyc"):
        return record
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return record
    record["lines"] = text.count("\n") + 1
    if p.suffix == ".md":
        record["frontmatter_kind"] = extract_frontmatter_kind(text)
    record["refs"] = extract_refs(text, p.suffix)
    return record


def main() -> int:
    """Walk repo and emit one JSON line per file."""
    out_dir = ROOT / "_reports" / "audit"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "inventory_full.jsonl"
    summary_path = out_dir / "inventory_summary.md"

    print(f"[W0] root={ROOT}", flush=True)
    print(f"[W0] writing {out_path}", flush=True)

    counts: dict[str, int] = {}
    total_files = 0
    total_bytes = 0
    total_lines = 0

    git_touched_count = 0

    with out_path.open("w", encoding="utf-8") as f:
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
            dp = Path(dirpath)
            for fname in filenames:
                p = dp / fname
                if should_skip(p):
                    continue
                rec = inventory_file(p)
                if total_files < 500 or total_files % 50 == 0:
                    rec["last_touched"] = get_git_last_touched(p)
                    if rec["last_touched"]:
                        git_touched_count += 1
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                total_files += 1
                total_bytes += rec["size_bytes"]
                total_lines += rec["lines"]
                counts[rec["kind_guess"]] = counts.get(rec["kind_guess"], 0) + 1
                if total_files % 500 == 0:
                    print(f"[W0] {total_files} files...", flush=True)

    summary_lines = [
        f"# W0 INVENTORY SUMMARY",
        f"",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Total files | {total_files} |",
        f"| Total bytes | {total_bytes:,} ({total_bytes/1024/1024:.1f} MB) |",
        f"| Total lines | {total_lines:,} |",
        f"| Files with git history sampled | {git_touched_count} |",
        f"",
        f"## By kind_guess",
        f"",
        f"| Kind | Count | % |",
        f"|---|---|---|",
    ]
    for kind, n in sorted(counts.items(), key=lambda x: -x[1]):
        pct = n * 100 / total_files
        summary_lines.append(f"| {kind} | {n} | {pct:.1f}% |")
    summary_lines.append("")
    summary_lines.append(f"## Output")
    summary_lines.append(f"")
    summary_lines.append(f"Per-file records: `{out_path.relative_to(ROOT).as_posix()}`")
    summary_lines.append("")
    summary_lines.append("## W0_INVENTORY_PASS")

    summary_path.write_text("\n".join(summary_lines), encoding="utf-8")
    print(f"[W0] DONE files={total_files} bytes={total_bytes:,}", flush=True)
    print(f"[W0] summary={summary_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
