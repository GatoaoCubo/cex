#!/usr/bin/env python3
"""CEX Evolve Below-9 Flywheel -- targets already-scored artifacts below 9.0.

Non-overlapping with the main flywheel (which targets quality:null).
Runs heuristic improvements in batches, commits each batch.

Usage:
  python _tools/cex_evolve_below9.py              # full loop
  python _tools/cex_evolve_below9.py --batch 9    # batch size (default 9)
  python _tools/cex_evolve_below9.py --max-cycles 100
  python _tools/cex_evolve_below9.py --dry-run    # preview only
"""

import os
import re
import sys
import subprocess
import time
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))

SKIP_DIRS = {'.git', 'node_modules', '.cex/cache', 'compiled', '_external'}


def find_below9(target: float = 9.0) -> list[tuple[float, Path]]:
    """Find all artifacts with numeric quality below target."""
    results = []
    for root, dirs, files in os.walk(CEX_ROOT):
        if any(skip in root for skip in SKIP_DIRS):
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            path = Path(root) / f
            try:
                txt = path.read_text(encoding='utf-8', errors='ignore')
                m = re.search(r'quality:\s*([\d.]+)', txt[:500])
                if m:
                    q = float(m.group(1))
                    if 0 < q < target:
                        results.append((q, path))
            except Exception:
                pass
    results.sort()  # lowest quality first
    return results


def evolve_one(filepath: Path) -> float | None:
    """Run cex_evolve.py single on one file. Returns new quality or None."""
    result = subprocess.run(
        [sys.executable, "_tools/cex_evolve.py", "single", str(filepath),
         "--target", "9.0", "--max-rounds", "3"],
        capture_output=True, text=True, timeout=120,
        cwd=str(CEX_ROOT)
    )
    # Parse result
    for line in result.stdout.split('\n'):
        if '[OK] KEEP' in line or 'KEEP' in line:
            m = re.search(r'(\d+\.\d+)', line)
            if m:
                return float(m.group(1))
    # Re-read from file
    try:
        txt = filepath.read_text(encoding='utf-8', errors='ignore')
        m = re.search(r'quality:\s*([\d.]+)', txt[:500])
        if m:
            return float(m.group(1))
    except Exception:
        pass
    return None


def git_commit_batch(cycle: int, improved: int, total: int) -> None:
    """Commit the batch."""
    subprocess.run(["git", "add", "-A"], capture_output=True, cwd=str(CEX_ROOT))
    msg = f"[AUTO-BELOW9] cycle {cycle}: {improved}/{total} artifacts improved toward 9.0"
    subprocess.run(
        ["git", "commit", "-m", msg, "--allow-empty"],
        capture_output=True, text=True, cwd=str(CEX_ROOT)
    )
    print(f"  [COMMIT] {msg}")


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch', type=int, default=9)
    parser.add_argument('--max-cycles', type=int, default=500)
    parser.add_argument('--target', type=float, default=9.0)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--sleep', type=int, default=5,
                        help='Seconds between batches')
    args = parser.parse_args()

    print("=" * 60)
    print("CEX EVOLVE BELOW-9 FLYWHEEL")
    print(f"  Target: {args.target} | Batch: {args.batch} | Max cycles: {args.max_cycles}")
    print("=" * 60)

    for cycle in range(1, args.max_cycles + 1):
        candidates = find_below9(args.target)
        if not candidates:
            print(f"\n[DONE] No artifacts below {args.target} remaining.")
            break

        print(f"\n--- Cycle {cycle} | {len(candidates)} artifacts below {args.target} ---")

        batch = candidates[:args.batch]
        improved = 0
        rejected = 0

        for q, path in batch:
            rel = path.relative_to(CEX_ROOT)
            print(f"  [{q:.1f}] {rel}", end=" ... ", flush=True)

            if args.dry_run:
                print("[DRY-RUN]")
                continue

            try:
                new_q = evolve_one(path)
                if new_q and new_q > q:
                    print(f"-> {new_q:.1f} [OK]")
                    improved += 1
                elif new_q and new_q >= args.target:
                    print(f"-> {new_q:.1f} [ALREADY OK]")
                else:
                    print(f"-> {new_q} [NO CHANGE]")
                    rejected += 1
            except subprocess.TimeoutExpired:
                print("[TIMEOUT]")
                rejected += 1
            except Exception as e:
                print(f"[ERROR: {e}]")
                rejected += 1

        if not args.dry_run and improved > 0:
            git_commit_batch(cycle, improved, len(batch))

        if args.dry_run:
            print(f"\n[DRY-RUN] Would process {len(batch)} artifacts. Stopping.")
            break

        print(f"  Cycle {cycle} done: {improved} improved, {rejected} unchanged")
        time.sleep(args.sleep)

    print("\n[FLYWHEEL] Complete.")


if __name__ == '__main__':
    main()
