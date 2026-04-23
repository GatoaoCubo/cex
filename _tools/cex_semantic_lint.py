#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cex_semantic_lint.py -- Semantic health checks beyond structural lint.

Detects problems that cex_doctor.py (structural) cannot:
  BROKEN_LINK   [[wikilink]] target doesn't exist
  ORPHAN        artifact has zero inlinks AND zero outlinks
  DENSITY_LOW   related: field has < 3 entries (below recommended)
  STALE         references date/version older than 6 months
  CIRCULAR      A -> B -> C -> A dependency cycle (warn only)
  CONTRADICTION (future: LLM-powered, currently placeholder)

GDP decision: severity=warn (flag for review, do not block)

Usage:
    python _tools/cex_semantic_lint.py --sweep               # full repo scan
    python _tools/cex_semantic_lint.py --file path/to/x.md   # single file
    python _tools/cex_semantic_lint.py --sweep --severity ERROR  # only errors
    python _tools/cex_semantic_lint.py --sweep --format tsv   # machine-readable
"""

import argparse
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))

SKIP_DIRS = {".git", ".obsidian", "__pycache__", "node_modules", "compiled", ".cex", "_docs"}
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
STALE_MONTHS = 6


# ------------------------------------------------------------------
# Frontmatter + scanning
# ------------------------------------------------------------------

def parse_file(path: Path) -> tuple[dict, str] | None:
    """Parse frontmatter + body."""
    try:
        import yaml
        text = path.read_text(encoding="utf-8", errors="replace")
    except (OSError, ImportError):
        return None

    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except Exception:
        return None
    return meta, m.group(2)


def collect_artifacts(root: Path) -> list[Path]:
    """Collect all .md files with frontmatter."""
    result = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            fp = Path(dirpath) / fname
            try:
                head = fp.read_text(encoding="utf-8", errors="ignore")[:4]
                if head == "---\n":
                    result.append(fp)
            except (OSError, PermissionError):
                continue
    return sorted(result)


def build_link_graph(artifacts: list[Path]) -> tuple[dict, dict, dict]:
    """Build id->path mapping, outlinks, and inlinks graphs.

    Returns:
        id_to_path: {artifact_id: Path}
        outlinks: {artifact_id: set of target_ids}  (from related: + [[wikilinks]])
        inlinks: {artifact_id: set of source_ids}
    """
    id_to_path = {}
    outlinks = defaultdict(set)
    inlinks = defaultdict(set)
    meta_cache = {}

    for fp in artifacts:
        parsed = parse_file(fp)
        if not parsed:
            continue
        meta, body = parsed
        aid = str(meta.get("id", fp.stem))
        id_to_path[aid] = fp
        meta_cache[aid] = meta

        # Outlinks from related: field
        related = meta.get("related", [])
        if isinstance(related, list):
            for r in related:
                rid = str(r)
                outlinks[aid].add(rid)
                inlinks[rid].add(aid)

        # Outlinks from [[wikilinks]] in body
        for wl in WIKILINK_RE.findall(body):
            wl = wl.strip()
            if wl and wl != aid:
                outlinks[aid].add(wl)
                inlinks[wl].add(aid)

    return id_to_path, outlinks, inlinks


# ------------------------------------------------------------------
# Lint checks
# ------------------------------------------------------------------

class Finding:
    """One lint finding."""
    __slots__ = ("severity", "check", "path", "artifact_id", "message", "detail")

    def __init__(self, severity: str, check: str, path: Path, artifact_id: str,
                 message: str, detail: str = ""):
        self.severity = severity
        self.check = check
        self.path = path
        self.artifact_id = artifact_id
        self.message = message
        self.detail = detail

    def __str__(self):
        rel = self.path.relative_to(CEX_ROOT)
        return f"[{self.severity}] {self.check}: {rel} -- {self.message}"

    def to_tsv(self) -> str:
        rel = self.path.relative_to(CEX_ROOT)
        return f"{self.severity}\t{self.check}\t{rel}\t{self.artifact_id}\t{self.message}"


def check_broken_links(
    id_to_path: dict,
    outlinks: dict,
    path_for: dict,
) -> list[Finding]:
    """BROKEN_LINK: [[wikilink]] or related: target doesn't resolve to a known artifact."""
    findings = []
    known_ids = set(id_to_path.keys())

    for source_id, targets in outlinks.items():
        source_path = id_to_path.get(source_id)
        if not source_path:
            continue
        for target_id in targets:
            if target_id not in known_ids:
                findings.append(Finding(
                    "ERROR", "BROKEN_LINK", source_path, source_id,
                    f"Target '{target_id}' not found in repo",
                ))
    return findings


def check_orphans(
    id_to_path: dict,
    outlinks: dict,
    inlinks: dict,
) -> list[Finding]:
    """ORPHAN: artifact has zero inlinks AND zero outlinks."""
    findings = []
    for aid, path in id_to_path.items():
        out_count = len(outlinks.get(aid, set()))
        in_count = len(inlinks.get(aid, set()))
        if out_count == 0 and in_count == 0:
            findings.append(Finding(
                "WARN", "ORPHAN", path, aid,
                "Zero inlinks and zero outlinks (isolated node)",
            ))
    return findings


def check_density_low(
    id_to_path: dict,
    outlinks: dict,
) -> list[Finding]:
    """DENSITY_LOW: related: field has < 3 entries."""
    findings = []
    for aid, path in id_to_path.items():
        parsed = parse_file(path)
        if not parsed:
            continue
        meta, _ = parsed
        related = meta.get("related", [])
        count = len(related) if isinstance(related, list) else 0
        if count < 3:
            findings.append(Finding(
                "INFO", "DENSITY_LOW", path, aid,
                f"related: has {count} entries (recommended minimum: 3)",
            ))
    return findings


def check_stale(id_to_path: dict) -> list[Finding]:
    """STALE: artifact references date older than STALE_MONTHS months."""
    findings = []
    cutoff = datetime.now() - timedelta(days=STALE_MONTHS * 30)
    date_re = re.compile(r'"?(\d{4}-\d{2}-\d{2})"?')

    for aid, path in id_to_path.items():
        parsed = parse_file(path)
        if not parsed:
            continue
        meta, _ = parsed

        for field in ("created", "updated"):
            val = str(meta.get(field, ""))
            m = date_re.search(val)
            if m:
                try:
                    dt = datetime.strptime(m.group(1), "%Y-%m-%d")
                    if dt < cutoff:
                        findings.append(Finding(
                            "INFO", "STALE", path, aid,
                            f"{field}: {m.group(1)} is older than {STALE_MONTHS} months",
                        ))
                except ValueError:
                    pass
    return findings


def check_circular(outlinks: dict, id_to_path: dict) -> list[Finding]:
    """CIRCULAR: detect cycles in the cross-reference graph (DFS)."""
    findings = []
    visited = set()
    path_stack = set()
    reported_cycles = set()

    def dfs(node: str, chain: list[str]):
        if node in path_stack:
            # Found cycle -- extract it
            cycle_start = chain.index(node)
            cycle = chain[cycle_start:] + [node]
            cycle_key = "->".join(sorted(cycle))
            if cycle_key not in reported_cycles:
                reported_cycles.add(cycle_key)
                node_path = id_to_path.get(node)
                if node_path:
                    findings.append(Finding(
                        "WARN", "CIRCULAR", node_path, node,
                        f"Cycle: {' -> '.join(cycle)}",
                    ))
            return

        if node in visited:
            return

        visited.add(node)
        path_stack.add(node)

        for neighbor in outlinks.get(node, set()):
            dfs(neighbor, chain + [node])

        path_stack.discard(node)

    for aid in outlinks:
        if aid not in visited:
            dfs(aid, [])

    return findings


# ------------------------------------------------------------------
# Main lint orchestration
# ------------------------------------------------------------------

def lint_sweep(
    root: Path = CEX_ROOT,
    severity_filter: str | None = None,
) -> list[Finding]:
    """Run all lint checks on the entire repo."""
    print("[LINT] Scanning artifacts...")
    artifacts = collect_artifacts(root)
    print(f"[LINT] Found {len(artifacts)} artifacts with frontmatter")

    print("[LINT] Building link graph...")
    id_to_path, outlinks, inlinks = build_link_graph(artifacts)
    print(f"[LINT] Graph: {len(id_to_path)} nodes, "
          f"{sum(len(v) for v in outlinks.values())} edges")

    all_findings = []

    print("[LINT] Checking broken links...")
    all_findings.extend(check_broken_links(id_to_path, outlinks, id_to_path))

    print("[LINT] Checking orphans...")
    all_findings.extend(check_orphans(id_to_path, outlinks, inlinks))

    print("[LINT] Checking cross-ref density...")
    all_findings.extend(check_density_low(id_to_path, outlinks))

    print("[LINT] Checking stale dates...")
    all_findings.extend(check_stale(id_to_path))

    print("[LINT] Checking circular references...")
    all_findings.extend(check_circular(outlinks, id_to_path))

    if severity_filter:
        all_findings = [f for f in all_findings if f.severity == severity_filter.upper()]

    return all_findings


def lint_single(path: Path) -> list[Finding]:
    """Run lint checks on a single file (limited: only broken links + density)."""
    artifacts = collect_artifacts(CEX_ROOT)
    id_to_path, outlinks, inlinks = build_link_graph(artifacts)

    parsed = parse_file(path)
    if not parsed:
        return [Finding("ERROR", "PARSE", path, path.stem, "Cannot parse frontmatter")]

    meta, body = parsed
    aid = str(meta.get("id", path.stem))

    findings = []

    # Broken links for this file only
    for target_id in outlinks.get(aid, set()):
        if target_id not in id_to_path:
            findings.append(Finding(
                "ERROR", "BROKEN_LINK", path, aid,
                f"Target '{target_id}' not found",
            ))

    # Density
    related = meta.get("related", [])
    count = len(related) if isinstance(related, list) else 0
    if count < 3:
        findings.append(Finding(
            "INFO", "DENSITY_LOW", path, aid,
            f"related: has {count} entries (recommended: 3+)",
        ))

    # Orphan
    out_count = len(outlinks.get(aid, set()))
    in_count = len(inlinks.get(aid, set()))
    if out_count == 0 and in_count == 0:
        findings.append(Finding(
            "WARN", "ORPHAN", path, aid,
            "Zero inlinks and zero outlinks",
        ))

    return findings


def print_report(findings: list[Finding], fmt: str = "text"):
    """Print lint findings."""
    if fmt == "tsv":
        print("severity\tcheck\tpath\tid\tmessage")
        for f in findings:
            print(f.to_tsv())
        return

    # Group by severity
    by_severity = defaultdict(list)
    for f in findings:
        by_severity[f.severity].append(f)

    print(f"\n{'='*70}")
    print("SEMANTIC LINT REPORT")
    print(f"{'='*70}")

    for sev in ("ERROR", "WARN", "INFO"):
        items = by_severity.get(sev, [])
        if not items:
            continue
        print(f"\n--- {sev} ({len(items)}) ---")

        # Group by check type
        by_check = defaultdict(list)
        for f in items:
            by_check[f.check].append(f)

        for check, check_items in sorted(by_check.items()):
            print(f"\n  {check} ({len(check_items)}):")
            for item in check_items[:20]:
                rel = item.path.relative_to(CEX_ROOT)
                print(f"    {rel} -- {item.message}")
            if len(check_items) > 20:
                print(f"    ... and {len(check_items) - 20} more")

    total = len(findings)
    errors = len(by_severity.get("ERROR", []))
    warns = len(by_severity.get("WARN", []))
    infos = len(by_severity.get("INFO", []))
    print(f"\n{'='*70}")
    print(f"TOTAL: {total} findings (ERROR={errors} WARN={warns} INFO={infos})")
    print(f"{'='*70}")


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Semantic lint for CEX artifacts (Karpathy LLM Wiki pattern)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--sweep", action="store_true", help="Scan entire repo")
    parser.add_argument("--file", help="Lint a single file")
    parser.add_argument("--severity", choices=["ERROR", "WARN", "INFO"],
                        help="Filter by severity")
    parser.add_argument("--format", choices=["text", "tsv"], default="text",
                        help="Output format (default: text)")
    args = parser.parse_args()

    if args.file:
        fp = Path(args.file).resolve()
        if not fp.exists():
            print(f"[ERROR] File not found: {args.file}")
            sys.exit(1)
        findings = lint_single(fp)
    elif args.sweep:
        findings = lint_sweep(severity_filter=args.severity)
    else:
        parser.print_help()
        sys.exit(1)

    if args.severity and args.file:
        findings = [f for f in findings if f.severity == args.severity.upper()]

    print_report(findings, fmt=args.format)

    errors = sum(1 for f in findings if f.severity == "ERROR")
    sys.exit(1 if errors > 0 else 0)


if __name__ == "__main__":
    main()
