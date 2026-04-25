#!/usr/bin/env python3
"""Inject tldr into ISOs that lack it. Derives from existing frontmatter fields.

Usage:
    python _tools/cex_iso_tldr_inject.py --check      # count missing
    python _tools/cex_iso_tldr_inject.py --fix         # inject tldrs
    python _tools/cex_iso_tldr_inject.py --fix --dry-run  # preview
"""
import argparse
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BUILDERS_DIR = REPO / "archetypes" / "builders"

# Pillar labels for tldr generation
PILLAR_MAP = {
    "P01": "knowledge",
    "P02": "model",
    "P03": "prompt",
    "P04": "tools",
    "P05": "output",
    "P06": "schema",
    "P07": "evaluation",
    "P08": "architecture",
    "P09": "config",
    "P10": "memory",
    "P11": "feedback",
    "P12": "orchestration",
}

# LLM function labels
FUNC_MAP = {
    "CONSTRAIN": "constraints and boundaries",
    "BECOME": "identity and role definition",
    "INJECT": "context injection and knowledge sources",
    "REASON": "reasoning strategy and planning",
    "CALL": "tool usage and external integrations",
    "PRODUCE": "output generation and formatting",
    "GOVERN": "quality validation and scoring",
    "COLLABORATE": "coordination and handoff protocols",
}

# ISO type patterns derived from filename
ISO_TYPE_MAP = {
    "architecture": "component map, dependencies, and structural constraints",
    "config": "naming conventions, output paths, and production limits",
    "eval": "quality gate with scoring dimensions and pass/fail criteria",
    "examples": "reference examples demonstrating correct output patterns",
    "feedback": "anti-patterns, regression signals, and quality improvement triggers",
    "instruction": "step-by-step build instructions for the 8F pipeline",
    "knowledge": "domain knowledge, terminology, and contextual background",
    "manifest": "builder identity, capabilities, and ISO inventory",
    "memory": "context persistence, recall triggers, and state management",
    "model": "agent definition, personality, and behavioral constraints",
    "orchestration": "workflow coordination, handoffs, and lifecycle management",
    "output": "output template, formatting rules, and structure",
    "prompt": "prompt template with variables, tone, and generation strategy",
    "schema": "data contract, field types, and validation rules",
    "tools": "tool integrations, CLI commands, and external capabilities",
}


def parse_frontmatter(text):
    """Extract frontmatter dict from markdown text."""
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith(" ") and not line.startswith("-"):
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def get_iso_type(filename):
    """Extract ISO type from filename like bld_feedback_ab_test_config.md."""
    name = filename.replace("bld_", "").rsplit(".", 1)[0]
    for iso_type in ISO_TYPE_MAP:
        if name.startswith(iso_type):
            return iso_type
    return None


def generate_tldr(fm, filename, builder_dir):
    """Generate a tldr string from frontmatter fields."""
    title = fm.get("title", "")
    kind = fm.get("kind", "")
    pillar = fm.get("pillar", "")
    domain = fm.get("domain", "")
    purpose = fm.get("purpose", "")
    llm_func = fm.get("llm_function", "")

    # Extract the kind name from builder directory
    kind_name = builder_dir.replace("-builder", "").replace("-", " ")

    # Get ISO type from filename
    iso_type = get_iso_type(os.path.basename(filename))
    iso_desc = ISO_TYPE_MAP.get(iso_type, "builder instructions")

    # Get pillar label
    pillar_label = PILLAR_MAP.get(pillar, pillar)

    # Get function label
    func_label = FUNC_MAP.get(llm_func, "")

    # Build tldr from available fields
    if purpose and len(purpose) > 10:
        # Use purpose directly if it is informative
        tldr = purpose.rstrip(".")
        if len(tldr) > 115:
            tldr = tldr[:112] + "..."
    elif title and iso_type:
        # Compose from title + ISO type description
        tldr = "%s %s: %s" % (
            kind_name.title(),
            pillar_label,
            iso_desc,
        )
        if len(tldr) > 115:
            tldr = tldr[:112] + "..."
    elif iso_type:
        tldr = "%s builder %s ISO: %s" % (
            kind_name.title(),
            iso_type,
            iso_desc,
        )
        if len(tldr) > 115:
            tldr = tldr[:112] + "..."
    else:
        tldr = "%s builder %s: %s" % (
            kind_name.title(),
            pillar_label,
            "build instructions for %s artifacts" % kind_name,
        )
        if len(tldr) > 115:
            tldr = tldr[:112] + "..."

    return tldr


def inject_tldr(filepath, dry_run=False):
    """Add tldr to a single file. Returns (changed, tldr_value)."""
    text = filepath.read_text(encoding="utf-8")

    # Skip if already has tldr
    if re.search(r"^tldr:", text, re.MULTILINE):
        return False, None

    # Parse frontmatter
    fm = parse_frontmatter(text)
    if not fm:
        return False, None

    builder_dir = filepath.parent.name
    tldr = generate_tldr(fm, filepath.name, builder_dir)

    # Find insertion point: before related: or density_score: or closing ---
    lines = text.split("\n")
    in_fm = False
    insert_idx = None
    fm_end = None

    for i, line in enumerate(lines):
        if line.strip() == "---":
            if not in_fm:
                in_fm = True
                continue
            else:
                fm_end = i
                break

    if fm_end is None:
        return False, None

    # Find best insertion point: before related:, density_score:, or closing ---
    insert_idx = fm_end
    for i in range(1, fm_end):
        if lines[i].startswith("related:") or lines[i].startswith("density_score:"):
            insert_idx = i
            break

    tldr_line = 'tldr: "%s"' % tldr.replace('"', "'")
    lines.insert(insert_idx, tldr_line)

    if not dry_run:
        filepath.write_text("\n".join(lines), encoding="utf-8")

    return True, tldr


def main():
    parser = argparse.ArgumentParser(description="Inject tldr into ISOs")
    parser.add_argument("--check", action="store_true", help="Count missing tldrs")
    parser.add_argument("--fix", action="store_true", help="Inject tldrs")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes")
    args = parser.parse_args()

    if not args.check and not args.fix:
        parser.print_help()
        sys.exit(1)

    # Find all ISOs
    isos = sorted(BUILDERS_DIR.rglob("bld_*.md"))
    missing = []
    for iso in isos:
        text = iso.read_text(encoding="utf-8")
        if not re.search(r"^tldr:", text, re.MULTILINE):
            missing.append(iso)

    if args.check:
        print("ISOs total:   %d" % len(isos))
        print("ISOs w/tldr:  %d" % (len(isos) - len(missing)))
        print("ISOs missing: %d" % len(missing))
        sys.exit(1 if missing else 0)

    if args.fix:
        changed = 0
        for iso in missing:
            ok, tldr = inject_tldr(iso, dry_run=args.dry_run)
            if ok:
                changed += 1
                if args.dry_run:
                    rel = iso.relative_to(REPO)
                    print("  [DRY] %s -> %s" % (rel, tldr))

        mode = "DRY RUN" if args.dry_run else "FIXED"
        print("\n%s: %d / %d ISOs injected with tldr" % (mode, changed, len(missing)))

        if not args.dry_run:
            # Verify
            still_missing = 0
            for iso in isos:
                text = iso.read_text(encoding="utf-8")
                if not re.search(r"^tldr:", text, re.MULTILINE):
                    still_missing += 1
            print("Remaining without tldr: %d" % still_missing)


if __name__ == "__main__":
    main()
