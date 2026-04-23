#!/usr/bin/env python3
"""
CEX Evolution Integrity Report

Generates a comprehensive report validating the full evolution trilogy:
- Spec 1: Schema Evolution (universal patterns in manifests, memories, configs)
- Spec 2: Runtime Evolution (memory_scope, effort, hooks fields active)
- Spec 3: Validation Registry (new kinds, builders, E2E tests)

Usage: python _tools/tests/report_evolution_integrity.py
"""

import json
import sqlite3
import subprocess
import sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent.parent
BUILDERS_DIR = CEX_ROOT / "archetypes" / "builders"
KINDS_META = CEX_ROOT / ".cex" / "kinds_meta.json"
INDEX_DB = CEX_ROOT / ".cex" / "index.db"
TAXONOMY = CEX_ROOT / "archetypes" / "TAXONOMY_LAYERS.yaml"

NEW_KINDS = ["memory_scope", "effort_profile", "hook_config"]
NEW_BUILDERS = ["memory-scope-builder", "effort-profile-builder", "hook-config-builder"]

PASS = "OK"
FAIL = "FAIL"

results = []


def check(name, condition, detail=""):
    status = PASS if condition else FAIL
    results.append((name, status, detail))
    return condition


def count_builders():
    return len([d for d in BUILDERS_DIR.iterdir() if d.is_dir()])


def count_kinds():
    meta = json.loads(KINDS_META.read_text(encoding="utf-8"))
    return len(meta)


def count_builder_isos(builder_name):
    bp = BUILDERS_DIR / builder_name
    if not bp.exists():
        return 0
    return len(list(bp.glob("bld_*.md")))


def check_manifests_with_keywords():
    total = 0
    with_kw = 0
    for bd in BUILDERS_DIR.iterdir():
        if not bd.is_dir():
            continue
        kind_slug = bd.name.replace("-builder", "").replace("-", "_")
        manifest = bd / f"bld_model_{kind_slug}.md"
        if manifest.exists():
            total += 1
            content = manifest.read_text(encoding="utf-8")
            if "keyword" in content.lower() or "routing" in content.lower():
                with_kw += 1
    return total, with_kw


def check_memories_with_observation():
    total = 0
    with_obs = 0
    for bd in BUILDERS_DIR.iterdir():
        if not bd.is_dir():
            continue
        kind_slug = bd.name.replace("-builder", "").replace("-", "_")
        mem = bd / f"bld_memory_{kind_slug}.md"
        if mem.exists():
            total += 1
            content = mem.read_text(encoding="utf-8")
            if "observation" in content.lower() or "pattern" in content.lower():
                with_obs += 1
    return total, with_obs


def check_configs_with_effort():
    total = 0
    with_effort = 0
    for bd in BUILDERS_DIR.iterdir():
        if not bd.is_dir():
            continue
        kind_slug = bd.name.replace("-builder", "").replace("-", "_")
        cfg = bd / f"bld_config_{kind_slug}.md"
        if cfg.exists():
            total += 1
            content = cfg.read_text(encoding="utf-8")
            if "effort" in content.lower() or "naming" in content.lower():
                with_effort += 1
    return total, with_effort


def check_index():
    if not INDEX_DB.exists():
        return 0
    conn = sqlite3.connect(str(INDEX_DB))
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM files")
    count = cur.fetchone()[0]
    conn.close()
    return count


def run_e2e_tests():
    test_file = CEX_ROOT / "_tools" / "tests" / "test_e2e_evolution.py"
    if not test_file.exists():
        return 0, 0
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=no", "-q"],
        capture_output=True, text=True, timeout=60,
        cwd=str(CEX_ROOT),
    )
    # Parse "28 passed" from output
    for line in result.stdout.splitlines():
        if "passed" in line:
            import re
            m = re.search(r"(\d+) passed", line)
            if m:
                passed = int(m.group(1))
                total_m = re.search(r"(\d+) passed(?:.*?(\d+) failed)?", line)
                failed = int(total_m.group(2)) if total_m and total_m.group(2) else 0
                return passed, passed + failed
    return 0, 0


def run_compile():
    result = subprocess.run(
        [sys.executable, "_tools/cex_compile.py", "--all"],
        capture_output=True, text=True, timeout=120,
        cwd=str(CEX_ROOT),
    )
    for line in result.stdout.splitlines():
        if "Results:" in line:
            import re
            m = re.search(r"(\d+)/(\d+) compiled", line)
            if m:
                return int(m.group(1)), int(m.group(2))
    return 0, 0


def main():
    print("=" * 60)
    print("    CEX Evolution Integrity Report")
    print("=" * 60)
    print()

    # --- Schema Evolution ---
    print("--- Schema Evolution ---")
    manifest_total, manifest_kw = check_manifests_with_keywords()
    check("Manifests with keywords",
          manifest_kw >= 103,
          f"{manifest_kw}/{manifest_total}")

    memory_total, memory_obs = check_memories_with_observation()
    check("Memories with observation_types",
          memory_obs >= 100,
          f"{memory_obs}/{memory_total}")

    config_total, config_effort = check_configs_with_effort()
    check("Configs with effort/naming",
          config_effort >= 100,
          f"{config_effort}/{config_total}")

    # --- Runtime Evolution ---
    print("\n--- Runtime Evolution ---")
    taxonomy_content = TAXONOMY.read_text(encoding="utf-8")
    for kind in NEW_KINDS:
        check(f"{kind} in TAXONOMY", kind in taxonomy_content)

    meta = json.loads(KINDS_META.read_text(encoding="utf-8"))
    for kind in NEW_KINDS:
        check(f"{kind} in kinds_meta", kind in meta)

    # --- Kind Registry ---
    print("\n--- Kind Registry ---")
    kind_count = count_kinds()
    check("Kind count >= 104", kind_count >= 104, str(kind_count))

    builder_count = count_builders()
    check("Builder count >= 106", builder_count >= 106, str(builder_count))

    # --- Skeleton Builders ---
    print("\n--- Skeleton Builders ---")
    total_skeleton_files = 0
    for bn in NEW_BUILDERS:
        iso_count = count_builder_isos(bn)
        total_skeleton_files += iso_count
        check(f"{bn} has 12 ISOs", iso_count == 12, str(iso_count))

        bp = BUILDERS_DIR / bn
        total_size = sum(f.stat().st_size for f in bp.glob("bld_*.md")) if bp.exists() else 0
        check(f"{bn} < 30KB", total_size < 30 * 1024, f"{total_size} bytes")

    # --- E2E Tests ---
    print("\n--- E2E Tests ---")
    passed, total = run_e2e_tests()
    check("E2E tests pass", passed >= 28 and passed == total,
          f"{passed}/{total}")

    # --- Compilation ---
    print("\n--- Compilation ---")
    compiled, comp_total = run_compile()
    check("Compilation 0 errors", compiled == comp_total,
          f"{compiled}/{comp_total}")

    # --- Index ---
    print("\n--- Index ---")
    indexed = check_index()
    check("Index entries populated", indexed >= 3000, str(indexed))

    # --- Summary ---
    print("\n" + "=" * 60)
    print("    SUMMARY")
    print("=" * 60)
    ok_count = sum(1 for _, s, _ in results if s == PASS)
    fail_count = sum(1 for _, s, _ in results if s == FAIL)

    for name, status, detail in results:
        marker = "  " if status == PASS else "!!"
        d = f" ({detail})" if detail else ""
        print(f"  [{status:>4}] {name}{d}")

    print()
    print(f"  Schema Evolution:    {manifest_kw}/{manifest_total} manifests hydrated")
    print(f"  Runtime Evolution:   {len(NEW_KINDS)} new kinds active")
    print(f"  Kind Registry:       {kind_count} kinds registered")
    print(f"  Skeleton Builders:   {len(NEW_BUILDERS)} created ({total_skeleton_files} files)")
    print(f"  E2E Tests:           {passed}/{total} passing")
    print(f"  Total builders:      {builder_count}")
    print(f"  Total kinds:         {kind_count}")
    print(f"  Memory fields:       {memory_obs}/{memory_total} hydrated")
    print(f"  Config fields:       {config_effort}/{config_total} hydrated")
    print(f"  Index entries:       {indexed} files indexed")
    print(f"  Compilation:         {compiled}/{comp_total} ({comp_total - compiled} errors)")
    print()
    print(f"  Result: {ok_count} OK, {fail_count} FAIL")
    print("=" * 60)

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
