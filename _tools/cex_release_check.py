#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Release Check -- Validates everything needed for public release.

Usage:
    python cex_release_check.py           # Run all checks
    python cex_release_check.py --fix     # Show fix suggestions
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent

PASS = 0
FAIL = 0
WARN = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  [PASS] {name}")
    else:
        FAIL += 1
        print(f"  [FAIL] {name}: {detail}")


def warn(name: str, detail: str) -> None:
    global WARN
    WARN += 1
    print(f"  [WARN] {name}: {detail}")


def main() -> None:
    print("\n=== CEX RELEASE CHECK ===\n")

    # -- 1. Required files exist --
    print("--- Files ---")
    for f in ["README.md", "QUICKSTART.md", "CLAUDE.md", "LICENSE",
              "CONTRIBUTING.md", ".env.example", "requirements.txt",
              "requirements-llm.txt", "pyproject.toml"]:
        check(f"file:{f}", (CEX_ROOT / f).exists(), f"{f} missing")

    # -- 2. README numbers match reality --
    print("\n--- README accuracy ---")
    readme = (CEX_ROOT / "README.md").read_text(encoding="utf-8", errors="replace")

    kinds_meta = CEX_ROOT / ".cex" / "kinds_meta.json"
    if kinds_meta.exists():
        actual_kinds = len(json.loads(kinds_meta.read_text(encoding="utf-8")))
        check("readme:kinds", str(actual_kinds) in readme,
              f"README should mention {actual_kinds} kinds")

    builders = [d for d in (CEX_ROOT / "archetypes" / "builders").iterdir()
                if d.is_dir() and d.name.endswith("-builder")]
    check("readme:builders", str(len(builders)) in readme,
          f"README should mention {len(builders)} builders")

    tools = list((CEX_ROOT / "_tools").glob("cex_*.py"))
    check("readme:tools", str(len(tools)) in readme,
          f"README should mention {len(tools)} tools")

    # -- 3. No stale model references --
    print("\n--- Model freshness ---")
    stale_models = ["claude-opus-4-20250514", "claude-sonnet-4-20250514",
                    "claude-opus-4-0"]
    for stale in stale_models:
        hits = subprocess.run(
            ["grep", "-rn", stale, "--include=*.py", "--include=*.yaml",
             "--include=*.cmd", "."],
            capture_output=True, text=True, cwd=str(CEX_ROOT)
        )
        # Filter out known_versions in updater, compiled/, venvs, and self-refs
        real_hits = [l for l in hits.stdout.strip().split("\n")
                     if l.strip() and "known_versions" not in l
                     and "compiled/" not in l and "_backup_" not in l
                     and "cex_release_check" not in l
                     and "cex_model_updater" not in l
                     and ".venv" not in l and "site-packages" not in l
                     and "_external" not in l]
        check(f"model:no_{stale[:20]}", len(real_hits) == 0,
              f"{len(real_hits)} stale refs found")

    # -- 4. Dependencies installable --
    print("\n--- Dependencies ---")
    req = CEX_ROOT / "requirements.txt"
    check("deps:requirements.txt", req.exists() and req.stat().st_size > 10,
          "requirements.txt missing or empty")
    req_llm = CEX_ROOT / "requirements-llm.txt"
    check("deps:requirements-llm.txt", req_llm.exists() and req_llm.stat().st_size > 10,
          "requirements-llm.txt missing or empty")

    # Check core deps are importable
    for mod in ["yaml", "tiktoken"]:
        try:
            __import__(mod)
            check(f"deps:import_{mod}", True)
        except ImportError:
            check(f"deps:import_{mod}", False, f"pip install {mod}")

    # -- 5. CI workflows exist --
    print("\n--- CI/CD ---")
    ci = CEX_ROOT / ".github" / "workflows" / "ci.yml"
    check("ci:workflow", ci.exists(), ".github/workflows/ci.yml missing")
    quality = CEX_ROOT / ".github" / "workflows" / "quality.yml"
    check("ci:quality", quality.exists(), ".github/workflows/quality.yml missing")

    # -- 6. System health --
    print("\n--- System health ---")
    r = subprocess.run(
        [sys.executable, "_tools/cex_doctor.py"],
        capture_output=True, text=True, timeout=30, cwd=str(CEX_ROOT),
        encoding="utf-8", errors="replace"
    )
    full = (r.stdout or "") + (r.stderr or "")
    m = re.search(r"(\d+) PASS \| (\d+) WARN \| (\d+) FAIL", full)
    if m:
        check("health:doctor_zero_fail", int(m.group(3)) == 0,
              f"{m.group(3)} FAILs")
    else:
        check("health:doctor_ran", False, "doctor output not parseable")

    r = subprocess.run(
        [sys.executable, "_tools/cex_hooks.py", "validate-all"],
        capture_output=True, text=True, timeout=30, cwd=str(CEX_ROOT),
        encoding="utf-8", errors="replace"
    )
    full = (r.stdout or "") + (r.stderr or "")
    m = re.search(r"Errors:\s+(\d+)", full)
    if m:
        check("health:hooks_zero_errors", int(m.group(1)) == 0,
              f"{m.group(1)} hook errors")

    r = subprocess.run(
        [sys.executable, "_tools/cex_compile.py", "--all"],
        capture_output=True, text=True, timeout=60, cwd=str(CEX_ROOT),
        encoding="utf-8", errors="replace"
    )
    full = (r.stdout or "") + (r.stderr or "")
    m = re.search(r"(\d+)/(\d+) compiled", full)
    if m:
        check("health:compile_100pct", m.group(1) == m.group(2),
              f"{m.group(1)}/{m.group(2)}")

    r = subprocess.run(
        [sys.executable, "_tools/cex_flywheel_audit.py", "audit"],
        capture_output=True, text=True, timeout=120, cwd=str(CEX_ROOT),
        encoding="utf-8", errors="replace"
    )
    full = (r.stdout or "") + (r.stderr or "")
    m = re.search(r"HEALTH:\s+(\d+)%", full)
    if m:
        check("health:flywheel_100pct", m.group(1) == "100",
              f"{m.group(1)}% health")

    # -- 7. No secrets leaked --
    print("\n--- Security ---")
    gitignore = (CEX_ROOT / ".gitignore").read_text(encoding="utf-8", errors="replace")
    check("security:env_ignored", ".env" in gitignore, ".env not in .gitignore")
    # .env can exist locally but must be gitignored
    r_git = subprocess.run(
        ["git", "ls-files", ".env", "secrets.yaml"],
        capture_output=True, text=True, cwd=str(CEX_ROOT)
    )
    tracked_secrets = [f for f in r_git.stdout.strip().split("\n") if f.strip()]
    check("security:no_tracked_secrets", len(tracked_secrets) == 0,
          f"Secret files tracked by git: {tracked_secrets}")

    # -- 8. Version consistency --
    print("\n--- Version ---")
    toml = (CEX_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    m = re.search(r'version\s*=\s*"([^"]+)"', toml)
    toml_ver = m.group(1) if m else "?"
    readme_ver = re.search(r'version-v?([\d.]+)', readme)
    readme_ver = readme_ver.group(1) if readme_ver else "?"
    check("version:sync", toml_ver == readme_ver,
          f"pyproject={toml_ver} vs README={readme_ver}")

    # -- Summary --
    print(f"\n{'='*50}")
    total = PASS + FAIL
    if FAIL == 0:
        print(f"  ALL GREEN: {PASS}/{total} checks passed")
    else:
        print(f"  {FAIL} FAIL / {PASS} PASS / {total} total")
        print("  Fix the FAILs above before releasing.")
    print(f"{'='*50}\n")

    sys.exit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Accepted for backward compatibility; behavior remains unchanged.",
    )
    parser.parse_known_args()
    main()
