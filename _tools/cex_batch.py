#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_batch.py -- Batch artifact production via 8F pipeline.

Reads intents from a file (one per line) or stdin, runs 8F for each.

Usage:
  python _tools/cex_batch.py intents.txt                # from file
  python _tools/cex_batch.py intents.txt --dry-run      # preview only
  echo "create agent for X" | python _tools/cex_batch.py -  # from stdin
  python _tools/cex_batch.py --from-mission mission.md  # extract intents from mission

Format of intents file:
  # Comments start with #
  create a knowledge card about RAG chunking
  create a workflow for CI/CD deployment
  kind:agent | create agent for sales automation
  kind:dispatch_rule | create routing for research tasks

Lines starting with "kind:" specify the kind explicitly.
"""

import json
import subprocess
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent


def parse_intents(source: str) -> list[dict]:
    """Parse intents from file or stdin."""
    if source == "-":
        lines = sys.stdin.read().strip().split("\n")
    else:
        path = Path(source)
        if not path.exists():
            print(f"ERROR: {source} not found", file=sys.stderr)
            sys.exit(1)
        lines = path.read_text(encoding="utf-8").strip().split("\n")

    intents = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        intent = {"text": line, "kind": None}
        # Parse "kind:X | intent text" format
        if line.startswith("kind:") and "|" in line:
            parts = line.split("|", 1)
            intent["kind"] = parts[0].replace("kind:", "").strip()
            intent["text"] = parts[1].strip()

        intents.append(intent)

    return intents


def run_8f(intent: str, kind: str = None, dry_run: bool = False) -> dict:
    """Run 8F Runner for a single intent. Returns result dict."""
    cmd = [sys.executable, str(CEX_ROOT / "_tools" / "cex_8f_runner.py"), intent]
    if kind:
        cmd.extend(["--kind", kind])
    if dry_run:
        cmd.append("--dry-run")
    else:
        cmd.append("--execute")
    cmd.append("--verbose")

    t0 = time.time()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        elapsed = time.time() - t0
        output = result.stdout + result.stderr

        passed = "PASS" in output and "Verdict" in output
        # Extract output path
        path_match = None
        for line in output.split("\n"):
            if "Output:" in line:
                path_match = line.split("Output:")[-1].strip()
                break

        return {
            "intent": intent,
            "kind": kind or "auto",
            "passed": passed,
            "path": path_match,
            "elapsed_s": round(elapsed, 1),
            "returncode": result.returncode,
        }
    except subprocess.TimeoutExpired:
        return {
            "intent": intent,
            "kind": kind or "auto",
            "passed": False,
            "path": None,
            "elapsed_s": 180,
            "returncode": -1,
            "error": "TIMEOUT",
        }
    except Exception as e:
        return {
            "intent": intent,
            "kind": kind or "auto",
            "passed": False,
            "path": None,
            "elapsed_s": 0,
            "returncode": -1,
            "error": str(e),
        }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="CEX Batch Runner")
    parser.add_argument("source", help="Intents file (or - for stdin)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("--max", type=int, default=50, help="Max intents to process")
    args = parser.parse_args()

    intents = parse_intents(args.source)
    if not intents:
        print("No intents found.")
        return

    intents = intents[:args.max]
    mode = "DRY-RUN" if args.dry_run else "EXECUTE"
    print(f"\n{'='*60}")
    print(f"  CEX BATCH RUNNER -- {mode}")
    print(f"  Intents: {len(intents)}")
    print(f"{'='*60}\n")

    results = []
    passed = 0
    failed = 0

    for i, intent in enumerate(intents, 1):
        print(f"[{i}/{len(intents)}] {intent['text'][:70]}...")
        result = run_8f(intent["text"], intent["kind"], args.dry_run)
        results.append(result)

        if result["passed"]:
            passed += 1
            print(f"  [OK] PASS ({result['elapsed_s']}s) -> {result.get('path', 'N/A')}")
        else:
            failed += 1
            err = result.get("error", "gates failed")
            print(f"  [FAIL] FAIL ({result['elapsed_s']}s) -- {err}")

    # Summary
    print(f"\n{'='*60}")
    print(f"  RESULTS: {passed} PASS | {failed} FAIL | {len(results)} total")
    total_time = sum(r["elapsed_s"] for r in results)
    print(f"  Total time: {total_time:.0f}s ({total_time/60:.1f}min)")
    print(f"{'='*60}")

    # Save results
    results_path = CEX_ROOT / ".cex" / "batch_results.json"
    import datetime
    data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "mode": mode,
        "passed": passed,
        "failed": failed,
        "total": len(results),
        "elapsed_s": round(total_time, 1),
        "results": results,
    }
    results_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\n  Results saved to .cex/batch_results.json")

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
