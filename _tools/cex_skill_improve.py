# -*- coding: ascii -*-
"""
CEX Skill Improver -- HERMES W4.2

Patches an existing skill artifact when a new execution trace reveals
new tool calls, edge cases, or error paths not yet documented.

HERMES invariant: patch in place -- never duplicate a skill.

CLI:
    python _tools/cex_skill_improve.py --skill <path> --trace <path> [--dry-run]
    python _tools/cex_skill_improve.py --auto  # scan recent traces + match loaded skills
    python _tools/cex_skill_improve.py --help
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_REPO_ROOT = Path(__file__).resolve().parent.parent
_TRACES_DIR = _REPO_ROOT / ".cex" / "runtime" / "traces"
_SKILLS_DIR = _REPO_ROOT / ".cex" / "skills" / "autocreated"
_INDEX_PATH = _REPO_ROOT / ".cex" / "skills" / "index.json"


# ---------------------------------------------------------------------------
# Frontmatter helpers (no third-party YAML)
# ---------------------------------------------------------------------------

def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    """
    Split --- frontmatter --- block from body.
    Returns (fields_dict, body_text).
    Values are raw strings; colons inside quoted values are preserved via
    partition-on-first-colon strategy.
    """
    stripped = content.lstrip()
    if not stripped.startswith("---"):
        return {}, content

    rest = stripped[3:]
    if rest.startswith("\n"):
        rest = rest[1:]

    end_match = re.search(r'^---\s*$', rest, flags=re.MULTILINE)
    if not end_match:
        return {}, content

    fm_text = rest[:end_match.start()]
    body = rest[end_match.end():]
    if body.startswith("\n"):
        body = body[1:]

    fields: dict[str, str] = {}
    for line in fm_text.splitlines():
        if ':' not in line:
            continue
        key, _, val = line.partition(':')
        fields[key.strip()] = val.strip()

    return fields, body


def serialize_frontmatter(fields: dict[str, str]) -> str:
    """Serialize fields dict back to YAML-like frontmatter block."""
    lines = ["---"]
    for k, v in fields.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Trace loading
# ---------------------------------------------------------------------------

def load_trace(path: Path) -> list[dict[str, Any]]:
    """Load JSONL trace file; return list of event dicts."""
    events: list[dict[str, Any]] = []
    with open(path, "r", encoding="ascii", errors="replace") as fh:
        for lineno, raw in enumerate(fh, 1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                events.append(json.loads(raw))
            except json.JSONDecodeError as exc:
                print(f"[WARN] trace line {lineno} skipped: {exc}", file=sys.stderr)
    return events


def extract_successful_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return events that have a tool name and non-error status."""
    error_statuses = {"error", "failed", "fatal", "exception"}
    calls: list[dict[str, Any]] = []
    for ev in events:
        tool = ev.get("tool") or ev.get("tool_name")
        if not tool:
            continue
        status = ev.get("status", "success")
        if status not in error_statuses:
            calls.append(ev)
    return calls


def extract_error_recovery_paths(events: list[dict[str, Any]]) -> list[str]:
    """
    Find tools that appeared in error events followed by a successful retry.
    These represent handled error/recovery paths worth documenting.
    """
    paths: list[str] = []
    error_statuses = {"error", "failed", "fatal", "exception"}
    for i, ev in enumerate(events):
        tool = ev.get("tool") or ev.get("tool_name")
        if not tool:
            continue
        if ev.get("status", "") not in error_statuses:
            continue
        # Look for same tool succeeding later in the trace
        for later in events[i + 1:]:
            later_tool = later.get("tool") or later.get("tool_name")
            if later_tool == tool and later.get("status", "success") not in error_statuses:
                label = f"{tool} (error -> recovery)"
                if label not in paths:
                    paths.append(label)
                break
    return paths


# ---------------------------------------------------------------------------
# Skill inspection
# ---------------------------------------------------------------------------

def extract_procedure_tools(body: str) -> set[str]:
    """
    Parse ## Procedure section to get the set of documented tool names.
    Detects bold-wrapped names: **ToolName**
    """
    tools: set[str] = set()
    in_procedure = False
    for line in body.splitlines():
        if re.match(r'^##\s+Procedure', line):
            in_procedure = True
            continue
        if in_procedure and re.match(r'^##\s+', line):
            break
        if in_procedure:
            for match in re.finditer(r'\*\*([A-Za-z_][A-Za-z0-9_]*)\*\*', line):
                tools.add(match.group(1))
    return tools


def has_section(body: str, section_name: str) -> bool:
    """Return True if body contains a ## {section_name} heading."""
    pattern = rf'^##\s+{re.escape(section_name)}\s*$'
    return bool(re.search(pattern, body, flags=re.MULTILINE))


def _extract_section_text(body: str, section_name: str) -> str:
    """Extract content lines of a named ## section (until next ## or EOF)."""
    lines = body.splitlines()
    pattern = rf'^##\s+{re.escape(section_name)}'
    start: int | None = None
    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start = i + 1
            break
    if start is None:
        return ""
    result: list[str] = []
    for line in lines[start:]:
        if re.match(r'^##\s+', line):
            break
        result.append(line)
    return "\n".join(result)


# ---------------------------------------------------------------------------
# Diff
# ---------------------------------------------------------------------------

class SkillDiff:
    def __init__(
        self,
        new_tools: list[str] | None = None,
        new_edge_cases: list[str] | None = None,
        new_error_paths: list[str] | None = None,
    ) -> None:
        self.new_tools: list[str] = new_tools or []
        self.new_edge_cases: list[str] = new_edge_cases or []
        self.new_error_paths: list[str] = new_error_paths or []

    def is_empty(self) -> bool:
        return not self.new_tools and not self.new_edge_cases and not self.new_error_paths

    def summary(self) -> str:
        parts: list[str] = []
        if self.new_tools:
            parts.append(f"new_tools({len(self.new_tools)}): {', '.join(self.new_tools)}")
        if self.new_edge_cases:
            parts.append(f"new_edge_cases({len(self.new_edge_cases)}): {', '.join(self.new_edge_cases)}")
        if self.new_error_paths:
            parts.append(f"new_error_paths({len(self.new_error_paths)}): {', '.join(self.new_error_paths)}")
        return "; ".join(parts) if parts else "no divergence"


def compute_diff(skill_path: Path, trace_path: Path) -> SkillDiff:
    """
    Compare skill documented procedure against a new execution trace.
    Returns SkillDiff describing what the trace reveals that the skill lacks.
    """
    content = skill_path.read_text(encoding="ascii", errors="replace")
    _, body = parse_frontmatter(content)

    existing_tools = extract_procedure_tools(body)
    edge_section = _extract_section_text(body, "Edge cases")

    events = load_trace(trace_path)
    successful = extract_successful_events(events)

    # Ordered unique tool names from trace
    trace_tools_ordered: list[str] = []
    seen_tools: set[str] = set()
    for ev in successful:
        t = ev.get("tool") or ev.get("tool_name", "")
        if t and t not in seen_tools:
            trace_tools_ordered.append(t)
            seen_tools.add(t)

    # New tools: present in trace but absent from skill procedure
    new_tools = [t for t in trace_tools_ordered if t not in existing_tools]

    # New edge cases: existing tools with unusually complex args or results
    new_edge_cases: list[str] = []
    reported_edges: set[str] = set()
    for ev in successful:
        t = ev.get("tool") or ev.get("tool_name", "")
        if t not in existing_tools or t in reported_edges:
            continue
        result = str(ev.get("result") or ev.get("output") or "")
        args = ev.get("args") or ev.get("input") or {}
        is_complex = len(result) > 200 or (isinstance(args, dict) and len(args) > 3)
        if is_complex:
            label = f"{t} (complex args/result)"
            if label not in edge_section:
                new_edge_cases.append(label)
                reported_edges.add(t)

    # New error/recovery paths not already in edge cases section
    raw_error_paths = extract_error_recovery_paths(events)
    new_error_paths = [p for p in raw_error_paths if p not in edge_section]

    return SkillDiff(
        new_tools=new_tools,
        new_edge_cases=new_edge_cases,
        new_error_paths=new_error_paths,
    )


# ---------------------------------------------------------------------------
# Patching
# ---------------------------------------------------------------------------

def _bump_improvement_count(fields: dict[str, str]) -> dict[str, str]:
    """Increment improvement_count. Add updated date. Mutates and returns fields."""
    try:
        count = int(fields.get("improvement_count", "0"))
    except ValueError:
        count = 0
    fields["improvement_count"] = str(count + 1)
    fields["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return fields


def _patch_body(body: str, diff: SkillDiff) -> str:
    """
    Apply diff changes to body text:
    1. Append new tool steps to ## Procedure section.
    2. Append edge cases and error paths to ## Edge cases (create if absent).
    """
    lines = body.splitlines()

    # -- Append new tools to Procedure --
    if diff.new_tools:
        in_proc = False
        proc_end = len(lines)
        for i, line in enumerate(lines):
            if re.match(r'^##\s+Procedure', line):
                in_proc = True
                continue
            if in_proc and re.match(r'^##\s+', line):
                proc_end = i
                break

        existing_steps = sum(1 for ln in lines[:proc_end] if re.match(r'^\d+\.', ln))
        new_step_lines: list[str] = []
        for j, tool in enumerate(diff.new_tools, existing_steps + 1):
            new_step_lines.append(f"{j}. **{tool}**  (observed in trace -- verify args)")

        lines = lines[:proc_end] + new_step_lines + lines[proc_end:]

    body = "\n".join(lines)

    # -- Append edge items --
    edge_items = diff.new_edge_cases + diff.new_error_paths
    if edge_items:
        block = "\n".join(f"- {item}" for item in edge_items)
        if has_section(body, "Edge cases"):
            # Insert before next ## after the Edge cases heading
            body_lines = body.splitlines()
            in_edge = False
            insert_at = len(body_lines)
            for i, line in enumerate(body_lines):
                if re.match(r'^##\s+Edge cases', line):
                    in_edge = True
                    continue
                if in_edge and re.match(r'^##\s+', line):
                    insert_at = i
                    break
            body_lines = body_lines[:insert_at] + block.splitlines() + body_lines[insert_at:]
            body = "\n".join(body_lines)
        else:
            body = body.rstrip() + f"\n\n## Edge cases\n\n{block}\n"

    return body


def patch_skill(skill_path: Path, diff: SkillDiff, *, dry_run: bool = False) -> bool:
    """
    Apply diff to skill file in place (HERMES invariant: patch, never duplicate).
    Returns True if changes were made (or would be in dry-run).
    """
    if diff.is_empty():
        print(f"[OK] No divergence -- skill already covers this execution: {skill_path.name}")
        return False

    content = skill_path.read_text(encoding="ascii", errors="replace")
    fields, body = parse_frontmatter(content)

    _bump_improvement_count(fields)
    patched_body = _patch_body(body, diff)
    new_content = serialize_frontmatter(fields) + "\n\n" + patched_body

    if dry_run:
        print(f"[DRY-RUN] Would patch: {skill_path}")
        print(f"[DRY-RUN] Diff      : {diff.summary()}")
        print(f"[DRY-RUN] improvement_count -> {fields['improvement_count']}")
        _print_diff_preview(diff)
        return True

    skill_path.write_text(new_content, encoding="ascii")
    print(f"[OK] Patched         : {skill_path}")
    print(f"[OK] Diff            : {diff.summary()}")
    print(f"[OK] improvement_count={fields['improvement_count']}")
    return True


def _print_diff_preview(diff: SkillDiff) -> None:
    if diff.new_tools:
        print(f"[DRY-RUN]   new_tools      : {diff.new_tools}")
    if diff.new_edge_cases:
        print(f"[DRY-RUN]   new_edge_cases : {diff.new_edge_cases}")
    if diff.new_error_paths:
        print(f"[DRY-RUN]   new_error_paths: {diff.new_error_paths}")


# ---------------------------------------------------------------------------
# Index access (for --auto mode)
# ---------------------------------------------------------------------------

def load_index() -> dict[str, Any]:
    if _INDEX_PATH.exists():
        try:
            return json.loads(_INDEX_PATH.read_text(encoding="ascii", errors="replace"))
        except json.JSONDecodeError:
            pass
    return {"skills": {}}


def _build_name_to_path(index: dict[str, Any]) -> dict[str, Path]:
    """Build reverse map: skill_name -> skill_path from index + SKILLS_DIR scan."""
    name_to_path: dict[str, Path] = {}

    for entry in index.get("skills", {}).values():
        name = entry.get("name", "")
        path_str = entry.get("path", "")
        if name and path_str:
            skill_file = _REPO_ROOT / path_str
            if skill_file.exists():
                name_to_path[name] = skill_file

    # Also pick up skills not yet indexed
    if _SKILLS_DIR.exists():
        for sk in _SKILLS_DIR.glob("skill_*.md"):
            content = sk.read_text(encoding="ascii", errors="replace")
            fm, _ = parse_frontmatter(content)
            raw_id = fm.get("id", "")
            name = raw_id.replace("p04_skill_", "") if raw_id else sk.stem.replace("skill_", "")
            if name and name not in name_to_path:
                name_to_path[name] = sk

    return name_to_path


def _match_skill_for_trace(
    events: list[dict[str, Any]],
    name_to_path: dict[str, Path],
) -> Path | None:
    """
    Find the best matching skill for a trace by tool-name prefix overlap.
    Returns skill path or None if no match.
    """
    tools = []
    for ev in events:
        t = ev.get("tool") or ev.get("tool_name")
        if t:
            tools.append(t.lower())

    if not tools:
        return None

    # Primary: slug of first tool as a prefix
    first_slug = re.sub(r"[^a-z0-9]+", "_", tools[0])[:20]

    for name, sk_path in name_to_path.items():
        if first_slug in name or name.startswith(first_slug):
            return sk_path

    # Secondary: any tool overlap
    for name, sk_path in name_to_path.items():
        name_parts = set(name.split("_"))
        if any(re.sub(r"[^a-z0-9]+", "_", t) in name_parts for t in tools):
            return sk_path

    return None


# ---------------------------------------------------------------------------
# Auto mode
# ---------------------------------------------------------------------------

def auto_improve(*, dry_run: bool = False) -> int:
    """
    Scan all traces in TRACES_DIR, match each to a loaded skill, and improve.
    Returns count of skills patched.
    """
    if not _TRACES_DIR.exists():
        print(f"[WARN] Traces directory missing: {_TRACES_DIR}", file=sys.stderr)
        return 0

    index = load_index()
    name_to_path = _build_name_to_path(index)

    if not name_to_path:
        print("[WARN] No indexed skills found -- run cex_skill_autocreate.py first", file=sys.stderr)
        return 0

    improved = 0
    for trace_path in sorted(_TRACES_DIR.glob("*.jsonl")):
        try:
            events = load_trace(trace_path)
        except OSError as exc:
            print(f"[WARN] Could not read trace {trace_path.name}: {exc}", file=sys.stderr)
            continue

        matched = _match_skill_for_trace(events, name_to_path)
        if matched is None:
            continue

        diff = compute_diff(matched, trace_path)
        if patch_skill(matched, diff, dry_run=dry_run):
            improved += 1

    print(f"[OK] Auto-improve complete: {improved} skill(s) patched")
    return improved


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cex_skill_improve",
        description=(
            "Patch CEX skill artifacts when a trace reveals new behavior (HERMES W4.2). "
            "HERMES invariant: patch in place -- never duplicate a skill."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python _tools/cex_skill_improve.py --skill .cex/skills/autocreated/skill_xxx.md \\
      --trace .cex/runtime/traces/trace_yyy.jsonl
  python _tools/cex_skill_improve.py --skill ... --trace ... --dry-run
  python _tools/cex_skill_improve.py --auto
  python _tools/cex_skill_improve.py --auto --dry-run
""",
    )

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--auto",
        action="store_true",
        help="Scan all traces and match to loaded skills for auto-improvement",
    )
    mode.add_argument(
        "--skill",
        metavar="PATH",
        help="Path to existing skill markdown file to improve",
    )

    parser.add_argument(
        "--trace",
        metavar="PATH",
        help="Path to JSONL trace file (required with --skill)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print diff without writing any files",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.auto:
        auto_improve(dry_run=args.dry_run)
        return 0

    # --skill mode
    if not args.trace:
        parser.error("--trace is required when using --skill")

    skill_path = Path(args.skill)
    trace_path = Path(args.trace)

    if not skill_path.exists():
        print(f"[FAIL] Skill not found: {skill_path}", file=sys.stderr)
        return 1
    if not trace_path.exists():
        print(f"[FAIL] Trace not found: {trace_path}", file=sys.stderr)
        return 1

    diff = compute_diff(skill_path, trace_path)
    patch_skill(skill_path, diff, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
