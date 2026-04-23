#!/usr/bin/env python3
"""W2: Wire Related Artifacts into all builder ISOs (bld_prompt + bld_eval).

Appends ## Related Artifacts section to every bld_prompt_*.md and
S_RELATED soft gate to every bld_eval_*.md. Idempotent.

Usage:
    python _tools/cex_wire_cross_refs.py             # dry-run (default)
    python _tools/cex_wire_cross_refs.py --apply     # write changes
    python _tools/cex_wire_cross_refs.py --stats     # report counts
"""

import argparse
import sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent
BUILDERS_DIR = CEX_ROOT / "archetypes" / "builders"
SKIP_DIRS = {"_shared", "_builder-builder"}

RELATED_SECTION = """
## Related Artifacts

When producing this kind of artifact, always populate the `related:` frontmatter
field and include a `## Related Artifacts` section in the output body.
Follow: `archetypes/builders/_shared/skill_cross_reference.md`

| Artifact | Relationship | Why |
|----------|-------------|-----|
| [[{upstream_id}]] | upstream | {upstream produces input this artifact consumes} |
| [[{sibling_id}]] | sibling | {same kind, different scope or audience} |
| [[{downstream_id}]] | downstream | {this artifact enables or is consumed by downstream} |
"""

S_RELATED_GATE = """
### S_RELATED: Cross-Reference Check (SOFT)
- [ ] `related:` frontmatter field populated (3-15 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream reference
- Penalty: -0.3 if empty (does not block, encourages wiring)
"""


def get_builder_dirs() -> list[Path]:
    dirs = []
    for d in sorted(BUILDERS_DIR.iterdir()):
        if d.is_dir() and d.name not in SKIP_DIRS:
            dirs.append(d)
    return dirs


def wire_prompt_file(path: Path, apply: bool) -> bool:
    """Append Related Artifacts section to bld_prompt file. Returns True if changed."""
    text = path.read_text(encoding="utf-8")
    if "## Related Artifacts" in text:
        return False
    if apply:
        path.write_text(text.rstrip() + "\n" + RELATED_SECTION, encoding="utf-8")
    return True


def wire_eval_file(path: Path, apply: bool) -> bool:
    """Append S_RELATED gate to bld_eval file. Returns True if changed."""
    text = path.read_text(encoding="utf-8")
    if "S_RELATED" in text:
        return False
    if apply:
        path.write_text(text.rstrip() + "\n" + S_RELATED_GATE, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="W2: Wire cross-refs into builder ISOs")
    parser.add_argument("--apply", action="store_true", help="Write changes (default: dry-run)")
    parser.add_argument("--stats", action="store_true", help="Report stats only")
    args = parser.parse_args()

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"[W2] cex_wire_cross_refs.py -- {mode}")

    builder_dirs = get_builder_dirs()
    print(f"[W2] Found {len(builder_dirs)} builder directories")

    prompt_changed = 0
    prompt_skipped = 0
    eval_changed = 0
    eval_skipped = 0
    errors = []

    for d in builder_dirs:
        # Wire bld_prompt_*.md
        for p in d.glob("bld_prompt_*.md"):
            try:
                if wire_prompt_file(p, args.apply):
                    prompt_changed += 1
                    if not args.stats:
                        print(f"  [prompt] {p.relative_to(CEX_ROOT)}")
                else:
                    prompt_skipped += 1
            except Exception as e:
                errors.append(f"prompt {p}: {e}")

        # Wire bld_eval_*.md
        for p in d.glob("bld_eval_*.md"):
            try:
                if wire_eval_file(p, args.apply):
                    eval_changed += 1
                    if not args.stats:
                        print(f"  [eval]   {p.relative_to(CEX_ROOT)}")
                else:
                    eval_skipped += 1
            except Exception as e:
                errors.append(f"eval {p}: {e}")

    print()
    print(f"[W2] Results ({mode}):")
    print(f"     bld_prompt: {prompt_changed} to update, {prompt_skipped} already wired")
    print(f"     bld_eval:   {eval_changed} to update, {eval_skipped} already wired")
    print(f"     Total files to modify: {prompt_changed + eval_changed}")
    if errors:
        print(f"     Errors: {len(errors)}")
        for e in errors[:10]:
            print(f"       {e}")

    if not args.apply and (prompt_changed + eval_changed) > 0:
        print()
        print("[W2] Re-run with --apply to write changes.")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
