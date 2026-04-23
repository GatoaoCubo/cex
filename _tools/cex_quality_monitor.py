#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Quality Monitor -- continuous quality tracking + regression detection.

Scores all artifacts, tracks trends over time, identifies regressions,
and auto-queues rebuilds for artifacts that fall below threshold.

Usage:
    python cex_quality_monitor.py --scan                   # Score all artifacts
    python cex_quality_monitor.py --scan --nucleus N03     # Score one nucleus
    python cex_quality_monitor.py --trend                  # Show quality trend
    python cex_quality_monitor.py --regressions            # Find quality drops
    python cex_quality_monitor.py --below 8.5              # List artifacts below threshold
    python cex_quality_monitor.py --report                 # Full quality report
"""

import argparse
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import parse_frontmatter

CEX_ROOT = Path(__file__).resolve().parent.parent
QUALITY_DIR = CEX_ROOT / ".cex" / "quality"
SNAPSHOT_PATH = QUALITY_DIR / "latest_snapshot.json"
HISTORY_PATH = QUALITY_DIR / "history.json"

NUC_DIRS = {
    "N01": "N01_intelligence", "N02": "N02_marketing", "N03": "N03_engineering",
    "N04": "N04_knowledge", "N05": "N05_operations", "N06": "N06_commercial",
    "N07": "N07_admin",
}

SKIP_DIRS = {"compiled", ".git", "__pycache__", ".cex", "node_modules"}


# ---------------------------------------------------------------------------
# Scoring (delegates to cex_score)
# ---------------------------------------------------------------------------


def _get_scorer():
    """Import cex_score dynamically."""
    try:
        from cex_score import score_artifact
        return score_artifact
    except ImportError:
        return None


# ---------------------------------------------------------------------------
# Artifact Scanning
# ---------------------------------------------------------------------------


def scan_artifacts(nucleus: str | None = None) -> list[dict]:
    """Scan and score all .md artifacts. Returns list of scored items."""
    score_fn = _get_scorer()
    if not score_fn:
        print("ERROR: cex_score module not available", file=sys.stderr)
        return []

    # Determine scan roots
    if nucleus:
        nuc_dir_name = NUC_DIRS.get(nucleus.upper())
        if not nuc_dir_name:
            print(f"Unknown nucleus: {nucleus}", file=sys.stderr)
            return []
        roots = [CEX_ROOT / nuc_dir_name]
    else:
        roots = [CEX_ROOT / d for d in NUC_DIRS.values() if (CEX_ROOT / d).exists()]
        # Also scan pillar dirs
        for d in sorted(CEX_ROOT.glob("P[0-9][0-9]_*")):
            if d.is_dir():
                roots.append(d)

    artifacts = []
    for root in roots:
        for md in sorted(root.rglob("*.md")):
            # Skip non-artifacts
            rel = md.relative_to(CEX_ROOT).as_posix()
            if any(skip in rel for skip in SKIP_DIRS):
                continue
            if md.name.startswith("README") or "_schema" in md.name:
                continue

            try:
                text = md.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue

            fm = parse_frontmatter(text)
            if not fm or "kind" not in fm:
                continue

            score, details = score_fn(str(md))
            if score <= 0:
                continue

            # Determine nucleus from path
            nuc = ""
            for n, d in NUC_DIRS.items():
                if d in rel:
                    nuc = n
                    break

            artifacts.append({
                "path": rel,
                "id": fm.get("id", md.stem),
                "kind": fm.get("kind", ""),
                "pillar": fm.get("pillar", ""),
                "nucleus": nuc,
                "score": score,
                "title": fm.get("title", md.stem),
            })

    return artifacts


# ---------------------------------------------------------------------------
# Snapshot Management
# ---------------------------------------------------------------------------


def save_snapshot(artifacts: list[dict]):
    """Save current quality snapshot."""
    QUALITY_DIR.mkdir(parents=True, exist_ok=True)

    snapshot = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "total": len(artifacts),
        "avg_score": round(sum(a["score"] for a in artifacts) / len(artifacts), 2) if artifacts else 0,
        "artifacts": artifacts,
    }

    SNAPSHOT_PATH.write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # Append to history
    history = load_history()
    history.append({
        "timestamp": snapshot["timestamp"],
        "total": snapshot["total"],
        "avg_score": snapshot["avg_score"],
    })
    # Keep last 100 snapshots
    if len(history) > 100:
        history = history[-100:]

    HISTORY_PATH.write_text(
        json.dumps(history, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return snapshot


def load_snapshot() -> dict | None:
    """Load latest quality snapshot."""
    if not SNAPSHOT_PATH.exists():
        return None
    try:
        return json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def load_history() -> list[dict]:
    """Load quality history."""
    if not HISTORY_PATH.exists():
        return []
    try:
        return json.loads(HISTORY_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------


def find_regressions(current: list[dict], previous: list[dict]) -> list[dict]:
    """Find artifacts whose score dropped between snapshots."""
    prev_scores = {a["path"]: a["score"] for a in previous}
    regressions = []

    for a in current:
        prev = prev_scores.get(a["path"])
        if prev and a["score"] < prev - 0.1:  # Drop of 0.1+
            regressions.append({
                **a,
                "prev_score": prev,
                "delta": round(a["score"] - prev, 2),
            })

    regressions.sort(key=lambda r: r["delta"])
    return regressions


def quality_report(artifacts: list[dict]) -> dict:
    """Generate comprehensive quality report."""
    if not artifacts:
        return {"total": 0}

    scores = [a["score"] for a in artifacts]
    by_kind: dict[str, list[float]] = defaultdict(list)
    by_nucleus: dict[str, list[float]] = defaultdict(list)
    by_pillar: dict[str, list[float]] = defaultdict(list)

    for a in artifacts:
        by_kind[a["kind"]].append(a["score"])
        if a.get("nucleus"):
            by_nucleus[a["nucleus"]].append(a["score"])
        if a.get("pillar"):
            by_pillar[a["pillar"]].append(a["score"])

    # Score distribution
    dist = Counter()
    for s in scores:
        if s >= 9.5:
            dist["GOLDEN (>=9.5)"] += 1
        elif s >= 8.0:
            dist["PUBLISH (8.0-9.4)"] += 1
        elif s >= 7.0:
            dist["ITERATE (7.0-7.9)"] += 1
        else:
            dist["REJECT (<7.0)"] += 1

    return {
        "total": len(artifacts),
        "avg_score": round(sum(scores) / len(scores), 2),
        "min_score": round(min(scores), 2),
        "max_score": round(max(scores), 2),
        "distribution": dict(dist),
        "by_nucleus": {
            n: {"count": len(s), "avg": round(sum(s) / len(s), 2)}
            for n, s in sorted(by_nucleus.items())
        },
        "by_kind_worst": sorted(
            [(k, round(sum(s) / len(s), 2), len(s)) for k, s in by_kind.items()],
            key=lambda x: x[1],
        )[:10],
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="CEX Quality Monitor -- tracking + regression detection")
    parser.add_argument("--scan", action="store_true", help="Score all artifacts and save snapshot")
    parser.add_argument("--nucleus", "-n", help="Filter by nucleus (e.g. N03)")
    parser.add_argument("--trend", action="store_true", help="Show quality trend over time")
    parser.add_argument("--regressions", action="store_true", help="Find quality regressions")
    parser.add_argument("--below", type=float, help="List artifacts below threshold")
    parser.add_argument("--report", action="store_true", help="Full quality report")
    args = parser.parse_args()

    if args.scan:
        print("Scanning artifacts...")
        t0 = time.time()
        artifacts = scan_artifacts(args.nucleus)
        elapsed = time.time() - t0
        snapshot = save_snapshot(artifacts)

        print("\n=== Quality Snapshot ===")
        print(f"  Artifacts:  {snapshot['total']}")
        print(f"  Avg score:  {snapshot['avg_score']}")
        print(f"  Scanned in: {elapsed:.1f}s")
        print(f"  Saved:      {SNAPSHOT_PATH}")
        return

    if args.trend:
        history = load_history()
        if not history:
            print("No history. Run --scan first.")
            sys.exit(1)

        print("\n=== Quality Trend ===\n")
        print(f"  {'Date':20s} {'Artifacts':>10s} {'Avg Score':>10s}")
        print(f"  {'-' * 44}")
        for h in history[-20:]:
            bar = "#" * int(h["avg_score"] * 5 - 35)  # Scale ~7-10 to 0-15 bars
            print(f"  {h['timestamp']:20s} {h['total']:>10d} {h['avg_score']:>10.2f}  {bar}")

        if len(history) >= 2:
            delta = history[-1]["avg_score"] - history[-2]["avg_score"]
            direction = "UP" if delta > 0 else "DOWN" if delta < 0 else "FLAT"
            print(f"\n  Trend: {direction} ({delta:+.2f} from previous)")
        return

    if args.regressions:
        snapshot = load_snapshot()
        if not snapshot:
            print("No snapshot. Run --scan first.")
            sys.exit(1)

        # Re-scan and compare
        current = scan_artifacts(args.nucleus)
        regressions = find_regressions(current, snapshot.get("artifacts", []))

        if not regressions:
            print("No regressions detected.")
            return

        print(f"\n=== Regressions ({len(regressions)}) ===\n")
        for r in regressions:
            print(f"  {r['delta']:+.1f}  {r['prev_score']:.1f} -> {r['score']:.1f}  {r['kind']:20s}  {r['path']}")
        return

    if args.below is not None:
        snapshot = load_snapshot()
        if not snapshot:
            print("No snapshot. Run --scan first.")
            sys.exit(1)

        below = [a for a in snapshot.get("artifacts", []) if a["score"] < args.below]
        below.sort(key=lambda a: a["score"])

        print(f"\n{len(below)} artifact(s) below {args.below}:\n")
        for a in below:
            print(f"  {a['score']:.1f}  {a['kind']:20s}  {a['path']}")
        return

    if args.report:
        snapshot = load_snapshot()
        if not snapshot:
            print("No snapshot. Run --scan first.")
            sys.exit(1)

        report = quality_report(snapshot.get("artifacts", []))

        print("\n=== Quality Report ===\n")
        print(f"  Total artifacts:  {report['total']}")
        print(f"  Average score:    {report['avg_score']}")
        print(f"  Score range:      {report['min_score']} -- {report['max_score']}")

        print("\n  Distribution:")
        for bucket, count in sorted(report["distribution"].items()):
            pct = count / report["total"] * 100 if report["total"] else 0
            bar = "#" * int(pct / 2)
            print(f"    {bucket:20s} {count:>5d} ({pct:>5.1f}%) {bar}")

        print("\n  By Nucleus:")
        for nuc, stats in report.get("by_nucleus", {}).items():
            print(f"    {nuc:5s} {stats['count']:>4d} artifacts  avg={stats['avg']:.2f}")

        print("\n  Worst Kinds (avg score):")
        for kind, avg, count in report.get("by_kind_worst", []):
            print(f"    {kind:30s} avg={avg:.1f}  n={count}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
