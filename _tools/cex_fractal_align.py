#!/usr/bin/env python3
"""cex_fractal_align.py -- Migrate nuclei to exact 12-pillar fractal.

Moves non-canonical dirs (audits, reports, research, etc.) into canonical
12-pillar layout. Creates missing pillar dirs. Writes nucleus-root README.

Usage:
    python _tools/cex_fractal_align.py          # dry-run (default)
    python _tools/cex_fractal_align.py --apply  # execute migration
"""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Canonical pillar dirs + auxiliary (rules, compiled)
PILLARS_12 = [
    "knowledge", "agents", "prompts", "tools", "output", "schemas",
    "quality", "architecture", "config", "memory", "feedback", "orchestration",
]
AUXILIARY = ["rules", "compiled"]
CANONICAL_14 = PILLARS_12 + AUXILIARY

# Mapping: extra dir name -> canonical destination
MIGRATION_MAP = {
    "audits":     "quality",
    "reports":    "output",
    "research":   "knowledge",
    "artifacts":  "output",
    "crews":      "orchestration",
    "workflows":  "orchestration",
    "chains":     "prompts",
    "dispatch":   "orchestration",
    "formatters": "output",
    "specs":      "architecture",
    "scripts":    "tools",
}

NUCLEI = {
    "N00_genesis":       ("N00", "Genesis",      "pre-sin archetype",      "template for all nuclei"),
    "N01_intelligence":  ("N01", "Intelligence", "Analytical Envy",        "research and analysis"),
    "N02_marketing":     ("N02", "Marketing",    "Creative Lust",          "marketing and copywriting"),
    "N03_engineering":   ("N03", "Engineering",  "Inventive Pride",        "artifact construction"),
    "N04_knowledge":     ("N04", "Knowledge",    "Knowledge Gluttony",     "knowledge management and RAG"),
    "N05_operations":    ("N05", "Operations",   "Gating Wrath",           "operations and deployment"),
    "N06_commercial":    ("N06", "Commercial",   "Strategic Greed",        "commercial and monetization"),
    "N07_admin":         ("N07", "Admin",        "Orchestrating Sloth",    "orchestration and dispatch"),
}

# Pillar -> 8F function (shown in README table)
PILLAR_SPEC = [
    ("knowledge",     "[[P01_knowledge]]",     "INJECT",      "Knowledge cards for"),
    ("agents",        "[[P02_model]]",         "BECOME",      "Agents specialized in"),
    ("prompts",       "[[P03_prompt]]",        "REASON",      "Prompt templates for"),
    ("tools",         "[[P04_tools]]",         "CALL",        "Skills/tools for"),
    ("output",        "[[P05_output]]",        "PRODUCE",     "Output formats for"),
    ("schemas",       "[[P06_schema]]",        "CONSTRAIN",   "Validation rules for"),
    ("quality",       "[[P07_evals]]",         "GOVERN",      "Quality gates for"),
    ("architecture",  "[[P08_architecture]]",  "GOVERN",      "Component maps for"),
    ("config",        "[[P09_config]]",        "GOVERN",      "Configs for"),
    ("memory",        "[[P10_memory]]",        "INJECT",      "Learning records for"),
    ("feedback",      "[[P11_feedback]]",      "GOVERN",      "User corrections for"),
    ("orchestration", "[[P12_orchestration]]", "COLLABORATE", "Routing rules for"),
]

DRY = True


def run(cmd: list[str]) -> tuple[int, str]:
    """Run a command, return (exit, stderr_or_stdout)."""
    if DRY:
        print("  [dry]", " ".join(cmd))
        return 0, ""
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT),
                       encoding="utf-8", errors="replace")
    return r.returncode, (r.stderr or r.stdout).strip()


def git_mv(src: Path, dst: Path) -> None:
    """git mv with fallback to plain mv for untracked files."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    # Check if src is tracked
    rc, _ = subprocess.run(
        ["git", "ls-files", "--error-unmatch", str(src.relative_to(ROOT))],
        capture_output=True, text=True, cwd=str(ROOT)
    ), ""
    rel_src = str(src.relative_to(ROOT)).replace("\\", "/")
    rel_dst = str(dst.relative_to(ROOT)).replace("\\", "/")
    rc, err = run(["git", "mv", rel_src, rel_dst])
    if rc != 0:
        # Fallback: plain move (untracked)
        if DRY:
            print(f"  [dry]   fallback: mv {rel_src} {rel_dst}")
        else:
            src.rename(dst)


def migrate_nucleus(ndir: Path) -> int:
    """Migrate extras in one nucleus. Returns file move count."""
    moved = 0
    for extra, canon in MIGRATION_MAP.items():
        src_dir = ndir / extra
        if not src_dir.exists() or not src_dir.is_dir():
            continue
        dst_dir = ndir / canon
        dst_dir.mkdir(exist_ok=True)
        # Collect all files and subdirs inside src
        for item in sorted(src_dir.rglob("*")):
            if item.is_file():
                rel = item.relative_to(src_dir)
                dst = dst_dir / rel
                # Skip README.md we generated (redundant in merged dir)
                if item.name == "README.md" and (dst_dir / "README.md").exists():
                    if DRY:
                        print(f"  [dry]   skip duplicate {item.relative_to(ROOT)}")
                    else:
                        item.unlink()
                    continue
                # Collision: prefix with source-dir name to preserve both
                if dst.exists():
                    dst = dst.with_name(f"{extra}_{dst.name}")
                    if DRY:
                        print(f"  [dry]   collision -> {dst.name}")
                git_mv(item, dst)
                moved += 1
        # Remove the now-empty extra dir
        if DRY:
            print(f"  [dry]   rmdir {src_dir.relative_to(ROOT)}")
        else:
            try:
                # Remove any empty subdirs first
                for sub in sorted(src_dir.rglob("*"), reverse=True):
                    if sub.is_dir():
                        try:
                            sub.rmdir()
                        except OSError:
                            pass
                src_dir.rmdir()
            except OSError as e:
                print(f"  [warn] could not remove {src_dir}: {e}")
    return moved


def flatten_nested_compiled(ndir: Path) -> int:
    """Move {pillar}/compiled/* to top-level compiled/."""
    moved = 0
    top_compiled = ndir / "compiled"
    top_compiled.mkdir(exist_ok=True)
    for sub in ndir.iterdir():
        if not sub.is_dir() or sub.name == "compiled":
            continue
        nested = sub / "compiled"
        if not nested.exists():
            continue
        for f in sorted(nested.iterdir()):
            if f.is_file():
                git_mv(f, top_compiled / f.name)
                moved += 1
        if not DRY:
            try:
                nested.rmdir()
            except OSError:
                pass
    return moved


def ensure_canonical_dirs(ndir: Path) -> int:
    """Create missing canonical dirs with .gitkeep."""
    created = 0
    for d in CANONICAL_14:
        pdir = ndir / d
        if not pdir.exists():
            if DRY:
                print(f"  [dry]   mkdir {pdir.relative_to(ROOT)}")
            else:
                pdir.mkdir(parents=True, exist_ok=True)
                (pdir / ".gitkeep").write_text("", encoding="utf-8")
            created += 1
    return created


def write_nucleus_readme(ndir: Path) -> None:
    """Write nucleus-root README.md with the 12-pillar table."""
    ndir_name = ndir.name
    nid, nname, sin, domain = NUCLEI[ndir_name]
    rows = []
    for subdir, pillar_ref, func, contents_prefix in PILLAR_SPEC:
        rows.append(f"| {subdir}/ | {pillar_ref} | {func} | {contents_prefix} {domain} |")
    table = "\n".join(rows)
    content = """# {nid} {nname} -- Fractal Module

> {sin} -- {domain}

Contains instances of all 12 pillars scoped to {domain}. Each pillar
subdir holds typed artifacts filtered through this nucleus's sin lens.

## Structure (mirrors 12 pillars)

| Subdir | Pillar | Function | Contents |
|--------|--------|----------|----------|
{table}

## Auxiliary

| Subdir | Purpose |
|--------|---------|
| rules/ | Nucleus-scoped rules (loaded at boot) |
| compiled/ | Auto-generated YAML from .md (do not edit) |

## Conventions

- Every file has YAML frontmatter (`id`, `kind`, `pillar`, `quality: null`).
- Kinds are variable; pillar subdirs are fixed.
- Reading any file's path reveals its pillar: `{nid}_*/{{pillar}}/{{kind}}_*.md`.
- Cross-nucleus siblings: same pillar in other nuclei lives at `../N0X_*/{{pillar}}/`.

## See also

- Nucleus definition: `architecture/nucleus_def_{nid.lower()}.md`
- Nucleus rules: `rules/` (or `.claude/rules/n07-*.md` for N07)
- Canonical pillar specs: `../P01_*/` through `../P12_*/`
"""
    readme = ndir / "README.md"
    if DRY:
        print(f"  [dry]   write {readme.relative_to(ROOT)} ({len(content)} bytes)")
    else:
        readme.write_text(content, encoding="utf-8")


def main() -> None:
    global DRY
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="execute (default is dry-run)")
    args = ap.parse_args()
    DRY = not args.apply

    print(f"\n=== CEX FRACTAL ALIGN {'(DRY-RUN)' if DRY else '(APPLYING)'} ===\n")

    total_moved = 0
    total_flat = 0
    total_created = 0

    for ndir_name in NUCLEI:
        ndir = ROOT / ndir_name
        if not ndir.exists():
            continue
        print(f"\n-- {ndir_name} --")
        total_moved += migrate_nucleus(ndir)
        total_flat += flatten_nested_compiled(ndir)
        total_created += ensure_canonical_dirs(ndir)
        write_nucleus_readme(ndir)

    print("\n=== SUMMARY ===")
    print(f"  files moved:    {total_moved}")
    print(f"  nested flats:   {total_flat}")
    print(f"  dirs created:   {total_created}")
    if DRY:
        print("\n  This was a DRY-RUN. Re-run with --apply to execute.")
    else:
        print("\n  Done. Run: python _tools/cex_flywheel_audit.py audit")


if __name__ == "__main__":
    main()
