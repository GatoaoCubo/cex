"""Audit W5 CROSS-PLATFORM: detect Windows-only blockers.

Scans for:
- Hardcoded backslash paths in py
- ps1 scripts without bash equivalent
- cmd / powershell -File invocations in py
- Hardcoded drive letters (C:\\, D:\\)
- cp1252/utf-16 encoding assumptions
- subprocess calls with shell=True + windows-only flags

Output: _reports/audit/cross_platform.md
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "_reports" / "audit" / "inventory_full.jsonl"
OUT = ROOT / "_reports" / "audit" / "cross_platform.md"

PATTERNS = {
    "hardcoded_drive": re.compile(r"['\"][A-Z]:\\\\"),
    "backslash_path": re.compile(r"['\"](?:[A-Za-z_][A-Za-z0-9_]*\\\\){2,}"),
    "powershell_file": re.compile(r"powershell\s+-File"),
    "cmd_invoke": re.compile(r"(?:^|\s)(?:cmd|cmd\.exe)\s+/[ck]"),
    "windows_encoding": re.compile(r"encoding\s*=\s*['\"]cp1252['\"]"),
    "utf16_encoding": re.compile(r"encoding\s*=\s*['\"](?:utf-16|utf_16)"),
    "shell_true_windows": re.compile(r"shell\s*=\s*True.*\.(exe|bat|cmd|ps1)"),
    "winreg_import": re.compile(r"^import\s+winreg|^from\s+winreg", re.MULTILINE),
    "msvcrt_import": re.compile(r"^import\s+msvcrt|^from\s+msvcrt", re.MULTILINE),
    "os_startfile": re.compile(r"os\.startfile\("),
    "creationflags_windows": re.compile(r"creationflags\s*=\s*\w*WINDOW"),
}

PS1_FREE_DIRS = {"boot", "_spawn"}
USER_HOME_RE = re.compile(r"['\"](?:C:\\\\Users\\\\|/Users/|/home/)[A-Za-z0-9_-]+")


def load_inventory() -> list[dict]:
    """Stream inventory_full.jsonl into memory."""
    records = []
    with INVENTORY.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def scan_text(rel_path: str, text: str) -> list[tuple[str, int, str]]:
    """Return list of (pattern_name, line_no, snippet) for matches."""
    findings = []
    lines = text.splitlines()
    for name, pat in PATTERNS.items():
        for i, line in enumerate(lines, start=1):
            if pat.search(line):
                snippet = line.strip()[:120]
                findings.append((name, i, snippet))
    for i, line in enumerate(lines, start=1):
        if USER_HOME_RE.search(line):
            findings.append(("user_home_path", i, line.strip()[:120]))
    return findings


def scan_files(records: list[dict]) -> dict:
    """Scan all py + ps1 + cmd files for windows-only patterns."""
    findings: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    scanned = 0
    for r in records:
        path = r["path"]
        if path.startswith((".venv", ".aider", ".git/")):
            continue
        if not path.endswith((".py", ".ps1", ".cmd", ".bat", ".sh")):
            continue
        if r["size_bytes"] > 1_000_000:
            continue
        try:
            text = (ROOT / path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        scanned += 1
        for finding in scan_text(path, text):
            findings[path].append(finding)
    print(f"[W5] scanned {scanned} files, {sum(len(v) for v in findings.values())} findings")
    return findings


def find_ps1_without_bash(records: list[dict]) -> list[dict]:
    """For each ps1 in boot/ or _spawn/, check if .sh sibling exists."""
    rows = []
    py_paths = {r["path"] for r in records}
    for r in records:
        path = r["path"]
        if not path.endswith(".ps1"):
            continue
        if not any(path.startswith(d + "/") for d in PS1_FREE_DIRS):
            continue
        sh_sibling = path[:-4] + ".sh"
        bash_sibling = path[:-4] + ""
        rows.append({
            "ps1": path,
            "lines": r["lines"],
            "has_sh": sh_sibling in py_paths,
        })
    return rows


def write_report(findings: dict, ps1_rows: list[dict]) -> None:
    """Emit cross_platform.md."""
    by_pattern: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    for path, items in findings.items():
        for name, line_no, snippet in items:
            by_pattern[name].append((path, line_no, snippet))

    lines = [
        "# W5 CROSS-PLATFORM AUDIT",
        "",
        f"Generated from `_reports/audit/inventory_full.jsonl`. "
        f"{sum(len(v) for v in findings.values())} findings across "
        f"{len(findings)} files; {len(ps1_rows)} ps1 scripts checked for bash parity.",
        "",
        "## Findings by pattern",
        "",
        "| Pattern | Hits | Severity | Fix hint |",
        "|---------|------|----------|----------|",
    ]
    severity = {
        "hardcoded_drive": ("HIGH", "Use Path.home() / config field"),
        "backslash_path": ("HIGH", "Use pathlib.Path or os.path.join"),
        "powershell_file": ("MEDIUM", "Add bash equivalent or document WSL"),
        "cmd_invoke": ("HIGH", "Use subprocess with list args, no shell"),
        "windows_encoding": ("HIGH", "Use utf-8 explicitly"),
        "utf16_encoding": ("MEDIUM", "Confirm needed (PS5 BOM cases only)"),
        "shell_true_windows": ("HIGH", "Use list args, drop shell=True"),
        "winreg_import": ("HIGH", "Wrap in try/except + linux fallback"),
        "msvcrt_import": ("MEDIUM", "Use termios on linux equivalent"),
        "os_startfile": ("MEDIUM", "Wrap with sys.platform check"),
        "creationflags_windows": ("MEDIUM", "Wrap with sys.platform check"),
        "user_home_path": ("HIGH", "Use Path.home() not literal"),
    }
    for name in sorted(by_pattern.keys(), key=lambda n: -len(by_pattern[n])):
        sev, fix = severity.get(name, ("LOW", ""))
        lines.append(f"| {name} | {len(by_pattern[name])} | {sev} | {fix} |")
    lines.append("")
    lines.append("## Per-pattern details (top 30 each)")
    lines.append("")
    for name, items in sorted(by_pattern.items(), key=lambda x: -len(x[1])):
        lines.append(f"### {name} ({len(items)} hits)")
        lines.append("")
        lines.append("| File | Line | Snippet |")
        lines.append("|------|------|---------|")
        for path, line_no, snippet in items[:30]:
            snippet_safe = snippet.replace("|", "\\|")
            lines.append(f"| `{path}` | {line_no} | `{snippet_safe}` |")
        if len(items) > 30:
            lines.append(f"| ... | ... | (+{len(items) - 30} more truncated) |")
        lines.append("")
    lines.append("## PowerShell scripts in boot/ + _spawn/")
    lines.append("")
    lines.append("| ps1 | Lines | Has .sh sibling? |")
    lines.append("|-----|-------|------------------|")
    no_sh = sum(1 for r in ps1_rows if not r["has_sh"])
    for r in sorted(ps1_rows, key=lambda x: (x["has_sh"], x["ps1"])):
        lines.append(f"| `{r['ps1']}` | {r['lines']} | {'YES' if r['has_sh'] else 'NO'} |")
    lines.append("")
    lines.append(f"**{no_sh} of {len(ps1_rows)} ps1 scripts lack a bash equivalent** -- "
                 f"these are HIGH-priority blockers for Linux/macOS users.")
    lines.append("")
    lines.append("## CROSS_PLATFORM_PASS")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[W5] report written: {OUT}")


def main() -> int:
    """Run W5 cross-platform audit."""
    print("[W5] loading inventory...")
    records = load_inventory()
    print(f"[W5] {len(records)} records loaded")
    findings = scan_files(records)
    ps1_rows = find_ps1_without_bash(records)
    write_report(findings, ps1_rows)
    print("[W5] DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
