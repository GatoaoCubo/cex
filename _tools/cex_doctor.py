#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Doctor v3.0 -- 12-Pillar ISO Architecture + Density + Completeness.

Usage:
  python _tools/cex_doctor.py          # diagnose only
  python _tools/cex_doctor.py --fix    # diagnose + auto-fix naming issues
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
BUILDERS_DIR = ROOT / "archetypes" / "builders"
LIBRARY_DIR = ROOT / "N00_genesis" / "P01_knowledge" / "library"
FIX_MODE = "--fix" in sys.argv

# -- Constants ----------------------------------------------------------------

EXPECTED_KINDS = [
    "architecture",
    "config",
    "eval",
    "feedback",
    "knowledge",
    "memory",
    "model",
    "orchestration",
    "output",
    "prompt",
    "schema",
    "tools",
]
EXPECTED_COUNT = len(EXPECTED_KINDS)  # 12
MAX_BYTES = 6144
MAX_BYTES_PROMPT = 8192

# Old ISO names that should no longer exist (migration residue check)
OLD_ISO_NAMES = [
    "manifest", "system_prompt", "instruction", "knowledge_card",
    "output_template", "quality_gate", "examples", "collaboration",
]
MIN_DENSITY = 0.78
NAMING_RE = re.compile(r"^bld_[a-z][a-z0-9_]+_[a-z][a-z0-9_]+\.md$")

# -- Helpers ------------------------------------------------------------------


def get_frontmatter(path: Path) -> dict[str, Any] | None:
    """Return parsed YAML frontmatter dict, or None if missing/invalid."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if text.startswith("---"):
            end = text.index("---", 3)
            return yaml.safe_load(text[3:end])
    except Exception:
        pass
    return None


def calc_density(path: Path) -> float:
    """Return density ratio (0.0-1.0): content lines / total lines.

    Filler = empty lines, whitespace-only, bare separators (---).
    Frontmatter block is excluded from calculation.
    """
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return 0.0

    # Strip frontmatter
    body = text
    if text.startswith("---"):
        try:
            end = text.index("---", 3)
            body = text[end + 3 :].lstrip("\n")
        except ValueError:
            pass

    lines = body.splitlines()
    if not lines:
        return 0.0

    content = 0
    for line in lines:
        stripped = line.strip()
        if stripped and stripped != "---":
            content += 1

    return content / len(lines)


def extract_topic_from_dir(dirname: str) -> str:
    """Convert builder dir name to expected topic suffix.

    'agent-builder' -> 'agent'
    'knowledge-card-builder' -> 'knowledge_card'
    'agent-package-builder' -> 'agent_package'
    """
    name = dirname
    if name.endswith("-builder"):
        name = name[: -len("-builder")]
    elif name.endswith("_builder"):
        name = name[: -len("_builder")]
    return name.replace("-", "_")


def expected_filename(kind: str, topic: str) -> str:
    return f"bld_{kind}_{topic}.md"


def parse_bld_filename(filename: str) -> tuple[str, str] | None:
    """Parse bld_{kind}_{topic}.md -> (kind, topic) or None."""
    if not filename.startswith("bld_") or not filename.endswith(".md"):
        return None
    stem = filename[4:-3]  # strip bld_ and .md
    # Match against known kinds (longest first to handle multi-word kinds)
    for kind in sorted(EXPECTED_KINDS, key=len, reverse=True):
        if stem.startswith(kind + "_"):
            topic = stem[len(kind) + 1 :]
            return (kind, topic)
    return None


# -- Checks -------------------------------------------------------------------


class CheckResult:
    def __init__(self, builder_name: str) -> None:
        self.name = builder_name
        self.naming = "PASS"
        self.density = "PASS"
        self.max_bytes = "PASS"
        self.completeness = "PASS"
        self.frontmatter = "PASS"
        self.h_related = "PASS"
        self.details = []

    @property
    def overall(self) -> str:
        statuses = [self.naming, self.density, self.max_bytes, self.completeness, self.frontmatter, self.h_related]
        if "FAIL" in statuses:
            return "FAIL"
        warn_count = statuses.count("WARN")
        if warn_count >= 3:
            return "FAIL"
        if warn_count > 0:
            return "WARN"
        return "PASS"


def check_builder(builder_dir: Path) -> CheckResult:
    """Run all checks on a single builder directory."""
    r = CheckResult(builder_dir.name)
    topic = extract_topic_from_dir(builder_dir.name)

    # Gather all bld_*.md files
    bld_files = sorted(builder_dir.glob("bld_*.md"))
    bld_names = {f.name for f in bld_files}

    # -- CHECK 1: 13-file completeness ----------------------------------------
    expected = {expected_filename(k, topic) for k in EXPECTED_KINDS}
    missing = expected - bld_names
    extra = bld_names - expected

    if missing:
        r.completeness = "FAIL"
        r.details.append(
            f"  missing {len(missing)}: {', '.join(sorted(missing)[:3])}"
            + (f" +{len(missing) - 3}" if len(missing) > 3 else "")
        )
    if extra:
        # Extra files might be naming issues, not necessarily wrong
        pass

    actual_count = len(bld_files)
    if actual_count != EXPECTED_COUNT and not missing:
        r.completeness = "WARN"
        r.details.append(f"  has {actual_count} bld_*.md (expected {EXPECTED_COUNT})")

    # -- CHECK 2: Naming ------------------------------------------------------
    naming_issues = []
    fix_renames = []
    for f in bld_files:
        if not NAMING_RE.match(f.name):
            naming_issues.append(f.name)
            continue
        parsed = parse_bld_filename(f.name)
        if not parsed:
            naming_issues.append(f"{f.name} (unknown kind)")
        elif parsed[1] != topic:
            naming_issues.append(f"{f.name} (topic '{parsed[1]}' != '{topic}')")
            # Potential fix: rename to correct topic
            correct = expected_filename(parsed[0], topic)
            fix_renames.append((f, builder_dir / correct))

    if naming_issues:
        r.naming = "WARN"
        for ni in naming_issues[:3]:
            r.details.append(f"  naming: {ni}")

    if FIX_MODE and fix_renames:
        for src, dst in fix_renames:
            if not dst.exists():
                src.rename(dst)
                r.details.append(f"  FIXED: {src.name} -> {dst.name}")

    # -- CHECK 3: Density -----------------------------------------------------
    low_density = []
    for f in bld_files:
        d = calc_density(f)
        if d < MIN_DENSITY:
            low_density.append((f.name, d))

    if low_density:
        r.density = "WARN" if len(low_density) <= 3 else "FAIL"
        for fname, d in low_density[:3]:
            r.details.append(f"  density: {fname} = {d:.2f} (min {MIN_DENSITY})")

    # -- CHECK 4: Max bytes ---------------------------------------------------
    oversized = []
    for f in bld_files:
        size = f.stat().st_size
        limit = MAX_BYTES_PROMPT if f.name.startswith("bld_prompt_") else MAX_BYTES
        if size > limit:
            oversized.append((f.name, size, limit))

    if oversized:
        r.max_bytes = "WARN"
        for fname, sz, limit in oversized[:3]:
            r.details.append(f"  size: {fname} = {sz}B (max {limit})")

    # -- CHECK 5a: Old ISO residue (migration check) --------------------------
    old_residue = []
    for f in bld_files:
        parsed = parse_bld_filename(f.name)
        if parsed and parsed[0] in OLD_ISO_NAMES:
            old_residue.append(f.name)
    if old_residue:
        r.completeness = "FAIL"
        for of in old_residue[:3]:
            r.details.append(f"  old-iso: {of} (should be migrated)")

    # -- CHECK 6: Frontmatter -------------------------------------------------
    missing_fm = []
    for f in bld_files:
        fm = get_frontmatter(f)
        if fm is None:
            missing_fm.append(f.name)
        else:
            # Check required fields
            req = {"id", "kind", "pillar"}
            has = set(fm.keys()) if isinstance(fm, dict) else set()
            lacking = req - has
            if lacking:
                missing_fm.append(f"{f.name} (missing: {', '.join(lacking)})")

    if missing_fm:
        r.frontmatter = "FAIL" if len(missing_fm) > 3 else "WARN"
        for mf in missing_fm[:3]:
            r.details.append(f"  frontmatter: {mf}")

    # -- CHECK 7: Related cross-references ------------------------------------
    low_related = []
    for f in bld_files:
        fm = get_frontmatter(f)
        related = []
        if isinstance(fm, dict):
            raw = fm.get("related", [])
            if isinstance(raw, list):
                related = raw
        count = len(related)
        if count < 3:
            low_related.append((f.name, count))

    if low_related:
        r.h_related = "WARN"
        for fname, cnt in low_related[:3]:
            r.details.append(
                f"  h_related: {fname} has {cnt} related entries (min 3)"
            )
        if len(low_related) > 3:
            r.details.append(f"  h_related: +{len(low_related) - 3} more")

    return r


# -- KC Library Checks --------------------------------------------------------

# All 98 CEX kinds (12 pillars)
ALL_KINDS = [
    "action_prompt",
    "agent",
    "api_client",
    "audio_tool",
    "axiom",
    "benchmark",
    "boot_config",
    "knowledge_index",
    "browser_tool",
    "bugloop",
    "chain",
    "checkpoint",
    "chunk_strategy",
    "cli_tool",
    "code_executor",
    "component_map",
    "computer_use",
    "constraint_spec",
    "context_doc",
    "daemon",
    "dag",
    "db_connector",
    "decision_record",
    "diagram",
    "director",
    "dispatch_rule",
    "document_loader",
    "e2e_eval",
    "embedding_config",
    "entity_memory",
    "enum_de",
    "env_config",
    "eval_dataset",
    "fallback_chain",
    "feature_flag",
    "few_shot_example",
    "formatter",
    "function_de",
    "glossary_entry",
    "golden_test",
    "guardrail",
    "handof",
    "handoff_protocol",
    "hook",
    "input_schema",
    "instruction",
    "interface",
    "agent_package",
    "knowledge_card",
    "law",
    "learning_record",
    "lens",
    "lifecycle_rule",
    "llm_judge",
    "mcp_server",
    "memory_scope",
    "memory_summary",
    "mental_model",
    "model_card",
    "naming_rule",
    "notifier",
    "optimizer",
    "output_validator",
    "parser",
    "path_config",
    "pattern",
    "permission",
    "plugin",
    "prompt_template",
    "prompt_version",
    "quality_gate",
    "rag_source",
    "rate_limit_config",
    "red_team_eval",
    "regression_check",
    "response_format",
    "retriever",
    "retriever_config",
    "reward_signal",
    "router",
    "runtime_rule",
    "runtime_state",
    "schedule",
    "scoring_rubric",
    "search_tool",
    "secret_config",
    "session_state",
    "signal",
    "smoke_eval",
    "spawn_config",
    "system_prompt",
    "type_de",
    "unit_eval",
    "validation_schema",
    "validator",
    "vision_tool",
    "webhook",
    "workflow",
]


def check_kc_library() -> dict[str, Any]:
    """Check KC Library health: sources, domains, kind KCs, feeds_kinds, origins."""
    sources_dir = LIBRARY_DIR / "sources"
    domain_dir = LIBRARY_DIR / "domain"

    sources = sorted(sources_dir.glob("src_*.md")) if sources_dir.exists() else []
    domains = sorted(domain_dir.glob("kc_*.md")) if domain_dir.exists() else []
    # Also check _reference/ for archived cluster KCs
    ref_dir = domain_dir / "_reference"
    if ref_dir.exists():
        domains = sorted(ref_dir.glob("kc_*.md"))
    # Check dedicated kind KCs
    kind_dir = LIBRARY_DIR / "kind"
    kind_kcs = sorted(kind_dir.glob("kc_*.md")) if kind_dir.exists() else []

    issues = []

    # Check each domain KC for feeds_kinds and origin
    covered_kinds = set()
    for kc_path in domains:
        fm = get_frontmatter(kc_path)
        if fm is None:
            issues.append(f"  {kc_path.name}: no frontmatter")
            continue

        feeds = fm.get("feeds_kinds", [])
        if not feeds:
            issues.append(f"  {kc_path.name}: feeds_kinds empty")
        else:
            for kind in feeds:
                # Only strip P##_ prefix, keep real kind names as-is
                if len(kind) > 3 and kind[0] == "P" and kind[1:3].isdigit() and kind[3] == "_":
                    clean = kind[4:]  # P04_tools -> tools
                else:
                    clean = kind
                covered_kinds.add(clean)

        origin = fm.get("origin")
        if origin:
            # Check origin source exists
            origin_file = sources_dir / f"{origin}.md"
            if origin == "manual":
                continue  # manual origin is valid (no source file needed)
            if not origin_file.exists():
                issues.append(f"  {kc_path.name}: origin '{origin}' not found")

    kind_coverage = len(covered_kinds & set(ALL_KINDS))

    return {
        "sources": len(sources),
        "domains": len(domains),
        "kinds_covered": kind_coverage,
        "kinds_total": len(ALL_KINDS),
        "issues": issues,
    }


# -- Shared Defaults Check ----------------------------------------------------

REQUIRED_SHARED_DEFAULTS = [
    "bld_tools_default.md",
    "bld_eval_default.md",
    "bld_config_default.md",
    "bld_memory_default.md",
    "bld_feedback_default.md",
    "bld_orchestration_default.md",
    "bld_architecture_default.md",
]


def check_shared_defaults() -> list[str]:
    """Verify _shared/ has the 7 required default files."""
    shared_dir = BUILDERS_DIR / "_shared"
    issues = []
    if not shared_dir.exists():
        issues.append("_shared/ directory missing")
        return issues
    for fname in REQUIRED_SHARED_DEFAULTS:
        if not (shared_dir / fname).exists():
            issues.append(f"_shared/{fname} missing")
    return issues


# -- Main ---------------------------------------------------------------------


def main() -> None:
    print("=" * 72)
    print("CEX Doctor v3.0 -- 12-Pillar ISO Architecture + Density + Completeness")
    print(f"Root: {ROOT}")
    print(f"Mode: {'DIAGNOSE + FIX' if FIX_MODE else 'DIAGNOSE ONLY'}")
    print("=" * 72)
    print()

    # Discover builder dirs
    builder_dirs = sorted(
        d
        for d in BUILDERS_DIR.iterdir()
        if d.is_dir() and not d.name.startswith("_") and not d.name.startswith(".") and d.name != "compiled"
    )

    if not builder_dirs:
        print("ERROR: No builder directories found in archetypes/builders/")
        sys.exit(1)

    print(f"Found {len(builder_dirs)} builder directories\n")

    results = []
    for bd in builder_dirs:
        results.append(check_builder(bd))

    # -- Summary Table --------------------------------------------------------
    pass_count = sum(1 for r in results if r.overall == "PASS")
    warn_count = sum(1 for r in results if r.overall == "WARN")
    fail_count = sum(1 for r in results if r.overall == "FAIL")

    # Column headers
    hdr = f"{'Builder':<35} {'Name':>5} {'Dens':>5} {'Size':>5} {'12ok':>5} {'YAML':>5} {'Rel':>5} {'ALL':>5}"
    print(hdr)
    print("-" * len(hdr))

    for r in results:

        def sym(s: str) -> str:
            return {"PASS": "ok", "WARN": "~~", "FAIL": "XX"}[s]

        line = (
            f"{r.name:<35} {sym(r.naming):>5} {sym(r.density):>5} "
            f"{sym(r.max_bytes):>5} {sym(r.completeness):>5} "
            f"{sym(r.frontmatter):>5} {sym(r.h_related):>5} {sym(r.overall):>5}"
        )
        print(line)

    print("-" * len(hdr))
    print(f"{'TOTAL':<35} {pass_count:>3} ok  {warn_count:>3} ~~  {fail_count:>3} XX")
    print()

    # -- Detail section (only non-PASS) ---------------------------------------
    failures = [r for r in results if r.overall != "PASS"]
    if failures:
        print("DETAILS (non-PASS builders):")
        print()
        for r in failures:
            print(f"[{r.overall}] {r.name}:")
            for d in r.details:
                print(d)
            print()

    # -- Aggregate stats ------------------------------------------------------
    print("=" * 72)
    total_files = sum(len(list(bd.glob("bld_*.md"))) for bd in builder_dirs)
    total_bytes = sum(f.stat().st_size for bd in builder_dirs for f in bd.glob("bld_*.md"))
    densities = []
    for bd in builder_dirs:
        for f in bd.glob("bld_*.md"):
            densities.append(calc_density(f))
    avg_density = sum(densities) / len(densities) if densities else 0

    oversized_total = sum(
        1
        for bd in builder_dirs
        for f in bd.glob("bld_*.md")
        if f.stat().st_size
        > (MAX_BYTES_PROMPT if f.name.startswith("bld_prompt_") else MAX_BYTES)
    )
    fm_missing_total = sum(
        1 for bd in builder_dirs for f in bd.glob("bld_*.md") if get_frontmatter(f) is None
    )

    print(f"Builders:       {len(builder_dirs)}")
    print(f"Total files:    {total_files} (expected {len(builder_dirs) * EXPECTED_COUNT})")
    print(f"Total size:     {total_bytes / 1024:.1f} KB")
    print(f"Avg density:    {avg_density:.2f}")
    print(
        f"Oversized:      {oversized_total} files (>{MAX_BYTES}B std, >{MAX_BYTES_PROMPT}B prompts)"
    )
    print(f"No frontmatter: {fm_missing_total} files")
    print(f"Result:         {pass_count} PASS | {warn_count} WARN | {fail_count} FAIL")
    print("=" * 72)

    # -- KC Library Health ----------------------------------------------------
    print()
    kc = check_kc_library()
    print(
        f"KC Library: {kc['sources']} sources, {kc['domains']} domains, "
        f"{kc['kinds_covered']}/{kc['kinds_total']} kinds covered"
    )
    if kc["issues"]:
        print(f"KC Issues ({len(kc['issues'])}):")
        for issue in kc["issues"][:10]:
            print(issue)
    print("=" * 72)

    # -- Shared Defaults Check ------------------------------------------------
    shared_issues = check_shared_defaults()
    if shared_issues:
        print()
        print(f"Shared Defaults ({len(shared_issues)} issues):")
        for si in shared_issues:
            print(f"  [WARN] {si}")
        print("=" * 72)

    sys.exit(1 if fail_count > 0 else 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--fix", action="store_true", help="Diagnose and auto-fix naming issues.")
    args, _ = parser.parse_known_args()
    FIX_MODE = args.fix
    main()
