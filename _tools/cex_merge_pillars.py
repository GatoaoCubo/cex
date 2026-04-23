"""
cex_merge_pillars.py -- Merge root P01-P12 content INTO N00_genesis pillar dirs.

Usage:
    python _tools/cex_merge_pillars.py --dry-run   # list all operations
    python _tools/cex_merge_pillars.py --execute   # run git mv + git rm
    python _tools/cex_merge_pillars.py --verify    # check N00 has all content
"""

import argparse
import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PILLARS = [
    ("P01_knowledge",     "N00_genesis/P01_knowledge"),
    ("P02_model",         "N00_genesis/P02_model"),
    ("P03_prompt",        "N00_genesis/P03_prompt"),
    ("P04_tools",         "N00_genesis/P04_tools"),
    ("P05_output",        "N00_genesis/P05_output"),
    ("P06_schema",        "N00_genesis/P06_schema"),
    ("P07_evals",         "N00_genesis/P07_evals"),
    ("P08_architecture",  "N00_genesis/P08_architecture"),
    ("P09_config",        "N00_genesis/P09_config"),
    ("P10_memory",        "N00_genesis/P10_memory"),
    ("P11_feedback",      "N00_genesis/P11_feedback"),
    ("P12_orchestration", "N00_genesis/P12_orchestration"),
]

SKIP_DIRS = {"compiled"}


def run(cmd, dry=False):
    if dry:
        print("[DRY] " + " ".join(cmd))
        return True
    result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print("[WARN] cmd failed: " + " ".join(cmd))
        if result.stderr:
            print("       " + result.stderr.strip())
        return False
    return True


def merge(dry=False):
    moved = 0
    skipped = 0
    removed = 0

    for src_pillar, dst_pillar in PILLARS:
        src_abs = os.path.join(REPO_ROOT, src_pillar)
        dst_abs = os.path.join(REPO_ROOT, dst_pillar)

        if not os.path.isdir(src_abs):
            print("[SKIP] {} -- not found".format(src_pillar))
            continue

        if not os.path.isdir(dst_abs):
            print("[WARN] {} -- destination not found, skipping pillar".format(dst_pillar))
            continue

        items = os.listdir(src_abs)
        non_compiled = [i for i in items if i not in SKIP_DIRS]

        for item in non_compiled:
            src_item = os.path.join(src_abs, item)
            dst_item = os.path.join(dst_abs, item)
            rel_src = src_pillar + "/" + item
            rel_dst = dst_pillar + "/" + item

            if os.path.exists(dst_item):
                print("[CONFLICT] {} -- already exists in {}, SKIP".format(rel_src, dst_pillar))
                skipped += 1
                continue

            print("[MOVE] {} -> {}".format(rel_src, rel_dst))
            ok = run(["git", "mv", rel_src, rel_dst], dry=dry)
            if ok:
                moved += 1
            else:
                skipped += 1

        # After moving non-compiled items, check if root pillar dir is empty
        if not dry:
            remaining = [i for i in os.listdir(src_abs) if i not in SKIP_DIRS]
            if not remaining:
                compiled_abs = os.path.join(src_abs, "compiled")
                if os.path.isdir(compiled_abs):
                    print("[REMOVE] {}/compiled/".format(src_pillar))
                    ok = run(["git", "rm", "-r", "--force",
                              os.path.join(src_pillar, "compiled")], dry=False)
                    if ok:
                        removed += 1
                if os.path.isdir(src_abs):
                    try:
                        os.rmdir(src_abs)
                        print("[REMOVE] {}/".format(src_pillar))
                        removed += 1
                    except OSError:
                        print("[WARN] {} -- could not rmdir (not empty?)".format(src_pillar))
            else:
                print("[KEEP] {} -- still has: {}".format(src_pillar, ", ".join(remaining)))
        else:
            # dry-run: show what would be removed
            compiled_abs = os.path.join(src_abs, "compiled")
            if os.path.isdir(compiled_abs):
                print("[DRY] git rm -r {}/compiled/".format(src_pillar))
            print("[DRY] rmdir {}/".format(src_pillar))
            removed += 1

    print("")
    print("Moved: {}, Skipped: {}, Removed: {}".format(moved, skipped, removed))


def verify():
    ok_count = 0
    fail_count = 0

    for src_pillar, dst_pillar in PILLARS:
        dst_abs = os.path.join(REPO_ROOT, dst_pillar)
        if not os.path.isdir(dst_abs):
            print("[VERIFY FAIL] {} -- directory missing".format(dst_pillar))
            fail_count += 1
            continue

        schema = os.path.join(dst_abs, "_schema.yaml")
        has_schema = os.path.isfile(schema)

        items = [i for i in os.listdir(dst_abs) if i not in SKIP_DIRS]
        count = len(items)

        schema_tag = "[schema:OK]" if has_schema else "[schema:MISSING]"
        print("[CHECK] {} -- {} items {}".format(dst_pillar, count, schema_tag))

        if not has_schema:
            fail_count += 1
        else:
            ok_count += 1

    # Special: P01 library check
    lib = os.path.join(REPO_ROOT, "N00_genesis", "P01_knowledge", "library")
    if os.path.isdir(lib):
        kcs = [f for f in os.listdir(lib) if f.endswith(".md")]
        print("[CHECK] N00_genesis/P01_knowledge/library -- {} KCs".format(len(kcs)))
        if len(kcs) >= 100:
            print("[VERIFY OK] library has >= 100 KCs")
            ok_count += 1
        else:
            print("[VERIFY FAIL] library has only {} KCs (expected >= 100)".format(len(kcs)))
            fail_count += 1
    else:
        print("[VERIFY FAIL] N00_genesis/P01_knowledge/library -- missing")
        fail_count += 1

    print("")
    if fail_count == 0:
        print("[VERIFY OK] All checks passed ({} pillars verified)".format(ok_count))
    else:
        print("[VERIFY FAIL] {} checks failed, {} passed".format(fail_count, ok_count))


def main():
    parser = argparse.ArgumentParser(description="Merge root P01-P12 into N00_genesis")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true",
                       help="List all operations without executing")
    group.add_argument("--execute", action="store_true",
                       help="Run git mv + git rm to perform the merge")
    group.add_argument("--verify", action="store_true",
                       help="Check N00_genesis has expected content")
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN -- no changes will be made ===")
        merge(dry=True)
    elif args.execute:
        print("=== EXECUTE -- running git mv + git rm ===")
        merge(dry=False)
    elif args.verify:
        print("=== VERIFY -- checking N00_genesis content ===")
        verify()

    sys.exit(0)


if __name__ == "__main__":
    main()
