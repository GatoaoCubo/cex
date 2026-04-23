#!/usr/bin/env python3
"""CEX Repo Align -- structural gap reporter.

Usage:
  python _tools/cex_repo_align.py            # report gaps
  python _tools/cex_repo_align.py --json     # JSON output
  python _tools/cex_repo_align.py --summary  # counts only

Exit codes:
  0 = clean (no gaps)
  1 = gaps found
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Semantic subdir name -> canonical P-numbered subdir
SEMANTIC_TO_PILLAR = {
    "knowledge":    "P01_knowledge",
    "agents":       "P02_model",
    "prompts":      "P03_prompt",
    "tools":        "P04_tools",
    "output":       "P05_output",
    "schemas":      "P06_schema",
    "quality":      "P07_evals",
    "architecture": "P08_architecture",
    "config":       "P09_config",
    "memory":       "P10_memory",
    "feedback":     "P11_feedback",
    "orchestration":"P12_orchestration",
}

NUCLEUS_DIRS = [
    "N00_genesis",
    "N01_intelligence",
    "N02_marketing",
    "N03_engineering",
    "N04_knowledge",
    "N05_operations",
    "N06_commercial",
    "N07_admin",
]

# Dirs that should not be renamed
SKIP_DIRS = {"rules", "compiled", "reports", "crews", "boot"}


def scan_nucleus(nucleus_dir: Path) -> dict:
    """Return gap data for one nucleus directory."""
    wrong = []
    missing = []
    ok = []

    if not nucleus_dir.is_dir():
        return {"wrong": wrong, "missing": missing, "ok": ok, "skipped": True}

    actual_subdirs = {d.name for d in nucleus_dir.iterdir() if d.is_dir()}

    for semantic, canonical in SEMANTIC_TO_PILLAR.items():
        has_semantic  = semantic  in actual_subdirs
        has_canonical = canonical in actual_subdirs

        if has_semantic and not has_canonical:
            wrong.append({
                "nucleus": nucleus_dir.name,
                "current": semantic,
                "expected": canonical,
                "path": str(nucleus_dir / semantic),
            })
        elif not has_semantic and not has_canonical:
            missing.append({
                "nucleus": nucleus_dir.name,
                "expected": canonical,
            })
        else:
            ok.append({
                "nucleus": nucleus_dir.name,
                "canonical": canonical,
            })

    return {"wrong": wrong, "missing": missing, "ok": ok, "skipped": False}


def run(args: argparse.Namespace) -> int:
    all_wrong   = []
    all_missing = []
    all_ok      = []

    for name in NUCLEUS_DIRS:
        ndir = ROOT / name
        result = scan_nucleus(ndir)
        if result.get("skipped"):
            if not args.summary:
                print(f"[SKIP] {name} -- directory not found")
            continue
        all_wrong.extend(result["wrong"])
        all_missing.extend(result["missing"])
        all_ok.extend(result["ok"])

    if args.json:
        out = {
            "wrong":   all_wrong,
            "missing": all_missing,
            "ok":      [x["nucleus"] + "/" + x["canonical"] for x in all_ok],
            "summary": {
                "wrong":   len(all_wrong),
                "missing": len(all_missing),
                "ok":      len(all_ok),
                "clean":   len(all_wrong) == 0 and len(all_missing) == 0,
            },
        }
        print(json.dumps(out, indent=2))
    else:
        for item in all_wrong:
            print(f"[WRONG]   {item['nucleus']}/{item['current']}  ->  should be  {item['expected']}")
        for item in all_missing:
            print(f"[MISSING] {item['nucleus']}/{item['expected']}  -- not found")
        if not args.summary:
            for item in all_ok:
                print(f"[OK]      {item['nucleus']}/{item['canonical']}")

        total_gaps = len(all_wrong) + len(all_missing)
        print(
            f"\nSummary: {len(all_wrong)} wrong, {len(all_missing)} missing, "
            f"{len(all_ok)} ok -- {'CLEAN' if total_gaps == 0 else str(total_gaps) + ' gaps'}"
        )

    gaps = len(all_wrong) + len(all_missing)
    return 0 if gaps == 0 else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CEX structural gap reporter -- validates nucleus subdir naming."
    )
    parser.add_argument("--json",    action="store_true", help="Output JSON instead of text")
    parser.add_argument("--summary", action="store_true", help="Print counts only (no per-dir lines)")
    args = parser.parse_args()
    sys.exit(run(args))


if __name__ == "__main__":
    main()
