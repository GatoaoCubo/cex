#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_feedback.py -- Quality Tracking + Auto-Archive + Promotion Engine

Scans all CEX artifacts, extracts quality/density metrics from frontmatter,
identifies archive and promotion candidates based on lifecycle rules.

Usage:
  python _tools/cex_feedback.py              # full scan + report
  python _tools/cex_feedback.py --archive    # move archive candidates to _archived/
  python _tools/cex_feedback.py --promote    # list promotion candidates
"""

import argparse
import datetime
import json
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

CEX_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import parse_frontmatter as _shared_parse_frontmatter

SCAN_DIRS = [
    "N00_genesis/P01_knowledge",
    "N00_genesis/P02_model",
    "N00_genesis/P03_prompt",
    "N00_genesis/P04_tools",
    "N00_genesis/P05_output",
    "N00_genesis/P06_schema",
    "N00_genesis/P07_evals",
    "N00_genesis/P08_architecture",
    "N00_genesis/P09_config",
    "N00_genesis/P10_memory",
    "N00_genesis/P11_feedback",
    "P12_orchestration",
    "archetypes/builders",
    "packages",
    "N01_intelligence",
    "N02_marketing",
    "N03_engineering",
    "N04_knowledge",
    "N05_operations",
    "N06_commercial",
    "N07_admin",
]

ARCHIVE_DIR = CEX_ROOT / "_archived"
DOCS_DIR = CEX_ROOT / "_docs"
METRICS_DIR = CEX_ROOT / ".cex"
METRICS_FILE = METRICS_DIR / "metrics.jsonl"

AGE_THRESHOLD_DAYS = 30
QUALITY_ARCHIVE = 7.0
QUALITY_PROMOTE = 9.0
DENSITY_MIN = 0.8


# --- Helpers -----------------------------------------------------------------


def parse_frontmatter(path: Path) -> dict | None:
    """Extract YAML frontmatter from a markdown file."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return None
    return _shared_parse_frontmatter(text)


def calc_density(path: Path) -> float:
    """Content lines / total lines (excluding frontmatter). Range 0.0-1.0."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return 0.0

    body = text
    if text.startswith("---"):
        try:
            end = text.index("---", 3)
            body = text[end + 3 :].lstrip("\n")
        except ValueError:
            pass

    lines = body.splitlines()
    if not lines:
        return 0.0

    content = sum(1 for line in lines if line.strip() and line.strip() != "---")
    return round(content / len(lines), 3)


def file_age_days(path: Path) -> int:
    """Days since last modification."""
    mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime)
    return (datetime.datetime.now() - mtime).days


def get_created_date(fm: dict, path: Path) -> str:
    """Get created date from frontmatter or file mtime."""
    if fm and fm.get("created"):
        return str(fm["created"])
    mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime)
    return mtime.strftime("%Y-%m-%d")


# --- Scanner -----------------------------------------------------------------


class ArtifactInfo:
    __slots__ = (
        "path",
        "rel",
        "quality",
        "density",
        "age_days",
        "created",
        "kind",
        "pillar",
        "title",
        "id",
    )

    def __init__(self, path: Path, rel: str, fm: dict | None):
        self.path = path
        self.rel = rel
        self.quality = None
        self.density = calc_density(path)
        self.age_days = file_age_days(path)
        self.created = get_created_date(fm, path)
        self.kind = None
        self.pillar = None
        self.title = None
        self.id = None

        if fm:
            q = fm.get("quality")
            if q is not None and q != "null":
                try:
                    self.quality = float(q)
                except (ValueError, TypeError):
                    pass
            self.kind = fm.get("kind") or fm.get("type")
            self.pillar = fm.get("pillar")
            self.title = fm.get("title", path.stem)
            self.id = fm.get("id", path.stem)
        else:
            self.title = path.stem
            self.id = path.stem


def scan_artifacts() -> list[ArtifactInfo]:
    """Scan all pillar dirs for .md artifacts with frontmatter."""
    artifacts = []
    for dirname in SCAN_DIRS:
        d = CEX_ROOT / dirname
        if not d.exists():
            continue
        for md in sorted(d.rglob("*.md")):
            # Skip schema/generator meta files
            if md.name.startswith("_"):
                continue
            fm = parse_frontmatter(md)
            rel = str(md.relative_to(CEX_ROOT)).replace("\\", "/")
            artifacts.append(ArtifactInfo(md, rel, fm))
    return artifacts


# --- Analysis ----------------------------------------------------------------


def analyze(artifacts: list[ArtifactInfo]) -> dict:
    """Classify artifacts into categories."""
    low_density = []
    archive_candidates = []
    promote_candidates = []
    no_quality = []
    healthy = []
    warnings = []

    for a in artifacts:
        # Density check
        if a.density < DENSITY_MIN:
            low_density.append(a)

        # Quality-based checks
        if a.quality is None:
            no_quality.append(a)
        elif a.quality < QUALITY_ARCHIVE and a.age_days > AGE_THRESHOLD_DAYS:
            archive_candidates.append(a)
        elif a.quality >= QUALITY_PROMOTE:
            promote_candidates.append(a)
        elif a.quality >= QUALITY_ARCHIVE:
            healthy.append(a)

        # Warnings: low quality but not old enough for archive
        if (
            a.quality is not None
            and a.quality < QUALITY_ARCHIVE
            and a.age_days <= AGE_THRESHOLD_DAYS
        ):
            warnings.append(a)

    densities = [a.density for a in artifacts if a.density > 0]
    qualities = [a.quality for a in artifacts if a.quality is not None]

    return {
        "total": len(artifacts),
        "low_density": low_density,
        "archive_candidates": archive_candidates,
        "promote_candidates": promote_candidates,
        "no_quality": no_quality,
        "healthy": healthy,
        "warnings": warnings,
        "avg_density": round(sum(densities) / len(densities), 3) if densities else 0,
        "avg_quality": round(sum(qualities) / len(qualities), 2) if qualities else 0,
    }


# --- Report ------------------------------------------------------------------


def _table_row(a: ArtifactInfo) -> str:
    q = f"{a.quality:.1f}" if a.quality is not None else "null"
    return f"| {a.rel[:60]} | {q} | {a.density:.2f} | {a.age_days}d | {a.kind or '-'} |"


def generate_report(results: dict) -> str:
    """Generate FEEDBACK_REPORT.md content."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# CEX Feedback Report",
        f"**Generated**: {now}",
        f"**Total artifacts scanned**: {results['total']}",
        f"**Avg density**: {results['avg_density']} | **Avg quality**: {results['avg_quality']}",
        "",
    ]

    # Summary counts
    lines += [
        "## Summary",
        "",
        "| Category | Count |",
        "|----------|-------|",
        f"| Healthy (quality >= 7) | {len(results['healthy'])} |",
        f"| Promotion candidates (quality >= 9) | {len(results['promote_candidates'])} |",
        f"| Archive candidates (quality < 7 + age > 30d) | {len(results['archive_candidates'])} |",
        f"| Low density (< 0.80) | {len(results['low_density'])} |",
        f"| No quality score | {len(results['no_quality'])} |",
        f"| Warnings (quality < 7 but recent) | {len(results['warnings'])} |",
        "",
    ]

    # Promotion candidates
    if results["promote_candidates"]:
        lines += [
            "## Promotion Candidates (quality >= 9.0)",
            "",
            "| File | Quality | Density | Age | Kind |",
            "|------|---------|---------|-----|------|",
        ]
        for a in sorted(results["promote_candidates"], key=lambda x: -(x.quality or 0)):
            lines.append(_table_row(a))
        lines.append("")

    # Archive candidates
    if results["archive_candidates"]:
        lines += [
            "## Archive Candidates (quality < 7 + age > 30d)",
            "",
            "| File | Quality | Density | Age | Kind |",
            "|------|---------|---------|-----|------|",
        ]
        for a in sorted(results["archive_candidates"], key=lambda x: x.quality or 0):
            lines.append(_table_row(a))
        lines.append("")

    # Low density
    if results["low_density"]:
        lines += [
            "## Low Density (< 0.80)",
            "",
            "| File | Quality | Density | Age | Kind |",
            "|------|---------|---------|-----|------|",
        ]
        for a in sorted(results["low_density"], key=lambda x: x.density):
            lines.append(_table_row(a))
        lines.append("")

    # Warnings
    if results["warnings"]:
        lines += [
            "## Warnings (quality < 7 but < 30d old)",
            "",
            "| File | Quality | Density | Age | Kind |",
            "|------|---------|---------|-----|------|",
        ]
        for a in sorted(results["warnings"], key=lambda x: x.quality or 0):
            lines.append(_table_row(a))
        lines.append("")

    # No quality
    no_q = results["no_quality"]
    lines += [
        f"## No Quality Score ({len(no_q)} files)",
        "",
    ]
    if no_q:
        lines += [
            "| File | Density | Age | Kind |",
            "|------|---------|-----|------|",
        ]
        for a in sorted(no_q, key=lambda x: x.density)[:30]:
            lines.append(f"| {a.rel[:60]} | {a.density:.2f} | {a.age_days}d | {a.kind or '-'} |")
        if len(no_q) > 30:
            lines.append(f"| ... and {len(no_q) - 30} more | | | |")
        lines.append("")

    lines.append("---")
    lines.append(f"*Generated by cex_feedback.py | {now}*")
    return "\n".join(lines)


# --- Actions -----------------------------------------------------------------


def do_archive(artifacts: list[ArtifactInfo], results: dict) -> int:
    """Move archive candidates to _archived/."""
    candidates = results["archive_candidates"]
    if not candidates:
        print("No archive candidates found.")
        return 0

    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    moved = 0
    for a in candidates:
        dest = ARCHIVE_DIR / a.path.name
        # Avoid overwrite
        if dest.exists():
            stem = a.path.stem
            suffix = a.path.suffix
            dest = ARCHIVE_DIR / f"{stem}_{a.age_days}d{suffix}"
        try:
            shutil.move(str(a.path), str(dest))
            print(f"  ARCHIVED: {a.rel} -> _archived/{dest.name}")
            moved += 1
        except Exception as e:
            print(f"  ERROR moving {a.rel}: {e}", file=sys.stderr)
    print(f"\nArchived {moved}/{len(candidates)} files.")
    return moved


def do_promote(results: dict):
    """List promotion candidates with details."""
    candidates = results["promote_candidates"]
    if not candidates:
        print("No promotion candidates found.")
        return

    print(f"\n{'=' * 60}")
    print(f"PROMOTION CANDIDATES ({len(candidates)} files)")
    print(f"{'=' * 60}\n")
    for a in sorted(candidates, key=lambda x: -(x.quality or 0)):
        print(f"  [{a.quality:.1f}] {a.rel}")
        print(f"         density={a.density:.2f} kind={a.kind or '-'} age={a.age_days}d")
    print("\nAction: Review these for CORE promotion (used>10x + quality>9).")


# --- Metrics -----------------------------------------------------------------


def append_metrics(results: dict):
    """Append run metrics to .cex/metrics.jsonl."""
    METRICS_DIR.mkdir(parents=True, exist_ok=True)

    entry = {
        "date": datetime.datetime.now().isoformat(),
        "total": results["total"],
        "pass": len(results["healthy"]) + len(results["promote_candidates"]),
        "warn": len(results["warnings"]) + len(results["no_quality"]),
        "fail": len(results["archive_candidates"]),
        "low_density": len(results["low_density"]),
        "avg_density": results["avg_density"],
        "avg_quality": results["avg_quality"],
    }

    with open(METRICS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    print(f"Metrics appended to {METRICS_FILE.relative_to(CEX_ROOT)}")


# --- Main --------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="CEX Feedback Engine")
    parser.add_argument(
        "--archive", action="store_true", help="Move archive candidates to _archived/"
    )
    parser.add_argument("--promote", action="store_true", help="List promotion candidates")
    args = parser.parse_args()

    print(f"Scanning CEX artifacts in {CEX_ROOT}...")
    artifacts = scan_artifacts()
    print(f"Found {len(artifacts)} artifacts.\n")

    results = analyze(artifacts)

    if args.promote:
        do_promote(results)
        return

    if args.archive:
        do_archive(artifacts, results)
        append_metrics(results)
        return

    # Full scan + report
    report = generate_report(results)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = DOCS_DIR / "FEEDBACK_REPORT.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"Report written to {report_path.relative_to(CEX_ROOT)}")

    # Print summary
    print(f"\n{'=' * 50}")
    print(f"  Total:     {results['total']}")
    print(f"  Healthy:   {len(results['healthy'])}")
    print(f"  Promote:   {len(results['promote_candidates'])}")
    print(f"  Archive:   {len(results['archive_candidates'])}")
    print(f"  Low dens:  {len(results['low_density'])}")
    print(f"  No score:  {len(results['no_quality'])}")
    print(f"  Warnings:  {len(results['warnings'])}")
    print(f"  Avg dens:  {results['avg_density']}")
    print(f"  Avg qual:  {results['avg_quality']}")
    print(f"{'=' * 50}")

    append_metrics(results)


if __name__ == "__main__":
    main()
