#!/usr/bin/env python3
"""CEX Bootstrap: Sin-driven self-improvement for nuclei.

Usage:
    python _tools/cex_bootstrap.py --nucleus N01 --level 2
    python _tools/cex_bootstrap.py --all --level 2 --dry-run
    python _tools/cex_bootstrap.py --nucleus N03 --level 3 --target 9.0
"""
import argparse
import subprocess
import sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent

# Level 2 expansion: domain-specific kinds per nucleus
# Names are GENERIC — user fills {{AGENT_NAME}} via seeds
EXPANSION_MAP = {
    "N01": {
        "name": "{{AGENT_NAME}}", "domain": "Research", "drive": "{{DRIVE}}",
        "kinds": ["rag_source", "embedding_config", "few_shot_example", "scoring_rubric",
                  "prompt_template", "research_brief"],
    },
    "N02": {
        "name": "{{AGENT_NAME}}", "domain": "Marketing", "drive": "{{DRIVE}}",
        "kinds": ["prompt_template", "persona_prompt", "action_prompt", "few_shot_example",
                  "response_format", "scoring_rubric"],
    },
    "N03": {
        "name": "{{AGENT_NAME}}", "domain": "Engineering", "drive": "{{DRIVE}}",
        "kinds": ["pattern", "scoring_rubric", "interface", "skill",
                  "boot_config", "response_format", "learning_record"],
    },
    "N04": {
        "name": "{{AGENT_NAME}}", "domain": "Knowledge", "drive": "{{DRIVE}}",
        "kinds": ["chunk_strategy", "retriever_config", "embedding_config",
                  "rag_source", "learning_record", "scoring_rubric"],
    },
    "N05": {
        "name": "{{AGENT_NAME}}", "domain": "Operations", "drive": "{{DRIVE}}",
        "kinds": ["spawn_config", "signal", "checkpoint", "deploy_config",
                  "env_config", "health_check", "retry_policy"],
    },
    "N06": {
        "name": "{{AGENT_NAME}}", "domain": "Commercial", "drive": "{{DRIVE}}",
        "kinds": ["few_shot_example", "scoring_rubric", "schedule",
                  "prompt_template", "learning_record", "response_format"],
    },
    "N07": {
        "name": "{{AGENT_NAME}}", "domain": "Admin", "drive": "{{DRIVE}}",
        "kinds": ["dag", "handoff", "signal", "spawn_config",
                  "retry_policy", "health_check"],
    },
}

# Build order (PRIDE first, then infra, then output)
BUILD_ORDER = ["N03", "N04", "N01", "N05", "N07", "N02", "N06"]


def run_nucleus_builder(nucleus, name, domain, kinds, dry_run=False):
    """Call cex_nucleus_builder.py for a nucleus."""
    cmd = [
        sys.executable,
        str(CEX_ROOT / "_tools" / "cex_nucleus_builder.py"),
        "--nucleus", nucleus,
        "--name", name,
        "--domain", domain,
        "--kinds",
        *kinds,
    ]

    if dry_run:
        cmd.append("--dry-run")

    print(f"\n{'='*60}")
    print(f"  {nucleus} ({name}) -- {EXPANSION_MAP[nucleus]['drive']}")
    print(f"  Kinds: {len(kinds)} -- {', '.join(kinds)}")
    print(f"  Mode: {'DRY-RUN' if dry_run else 'EXECUTE'}")
    print(f"{'='*60}")

    result = subprocess.run(cmd, cwd=str(CEX_ROOT), capture_output=False)
    return result.returncode == 0


def level2_expand(nuclei, dry_run=False):
    """Level 2: Add domain-specific kinds to each nucleus."""
    results = {}
    for nuc in nuclei:
        info = EXPANSION_MAP[nuc]
        success = run_nucleus_builder(
            nuc, info["name"], info["domain"], info["kinds"], dry_run
        )
        results[nuc] = success

    print(f"\n{'='*60}")
    print("  LEVEL 2 EXPANSION SUMMARY")
    print(f"{'='*60}")
    for nuc, ok in results.items():
        info = EXPANSION_MAP[nuc]
        status = "DONE" if ok else "PARTIAL"
        print(f"  {nuc} {info['name']:8s} {info['drive']:10s} {len(info['kinds']):2d} kinds  {status}")
    total = sum(len(EXPANSION_MAP[n]["kinds"]) for n in nuclei)
    print(f"\n  Total: {total} artifacts attempted")


def _scan_below_target(nuclei, target):
    """Find artifacts scoring below target in given nuclei."""
    sys.path.insert(0, str(CEX_ROOT / "_tools"))
    from cex_score import score_artifact

    NUC_DIRS = {
        "N01": "N01_intelligence", "N02": "N02_marketing", "N03": "N03_engineering",
        "N04": "N04_knowledge", "N05": "N05_operations", "N06": "N06_commercial",
        "N07": "N07_admin",
    }
    below = []
    for nuc in nuclei:
        nuc_dir = CEX_ROOT / NUC_DIRS.get(nuc, "")
        if not nuc_dir.exists():
            continue
        for md in sorted(nuc_dir.rglob("*.md")):
            if "compiled" in str(md) or md.name == "README.md" or "_schema" in md.name:
                continue
            score, _ = score_artifact(str(md))
            if 0 < score < target:
                below.append({"path": str(md), "score": score, "nucleus": nuc})
    return below


def level3_quality_spiral(nuclei, target=8.0, dry_run=False):
    """Level 3: PRIDE loop -- score all artifacts, rebuild below target, repeat."""
    max_iterations = 3
    print(f"\n  LEVEL 3: Quality spiral (target={target}, max_iter={max_iterations})")

    for iteration in range(1, max_iterations + 1):
        below = _scan_below_target(nuclei, target)
        if not below:
            print(f"\n  Iteration {iteration}: All artifacts >= {target}. Spiral complete.")
            break

        print(f"\n  Iteration {iteration}: {len(below)} artifact(s) below {target}")
        for item in below:
            print(f"    {item['score']:.1f}  {item['path']}")

        if dry_run:
            print(f"\n  DRY-RUN: Would rebuild {len(below)} artifact(s)")
            break

        rebuilt = 0
        for item in below:
            md_path = Path(item["path"])
            # Read existing artifact to extract kind for 8F rebuild
            text = md_path.read_text(encoding="utf-8")
            from cex_shared import parse_frontmatter
            fm = parse_frontmatter(text)
            if not fm or "kind" not in fm:
                print(f"    SKIP (no frontmatter): {md_path.name}")
                continue

            kind = fm["kind"]
            title = fm.get("title", md_path.stem)
            intent = f"enrich {kind}: {title}"
            output_dir = str(md_path.parent)

            cmd = [
                sys.executable, str(CEX_ROOT / "_tools" / "cex_8f_runner.py"),
                intent, "--kind", kind, "--execute",
                "--output-dir", output_dir,
            ]
            print(f"    REBUILD: {md_path.name} (kind={kind}, score={item['score']:.1f})")
            result = subprocess.run(cmd, cwd=str(CEX_ROOT), capture_output=True, timeout=120)
            if result.returncode == 0:
                rebuilt += 1

        print(f"\n  Iteration {iteration}: Rebuilt {rebuilt}/{len(below)} artifact(s)")
        if rebuilt == 0:
            print("  No artifacts rebuilt — stopping spiral.")
            break

    # Final summary
    remaining = _scan_below_target(nuclei, target) if not dry_run else below
    print(f"\n  SPIRAL SUMMARY: {len(remaining)} artifact(s) still below {target}")


def main():
    parser = argparse.ArgumentParser(description="CEX Bootstrap: sin-driven self-improvement")
    parser.add_argument("--nucleus", help="Target nucleus (e.g., N01)")
    parser.add_argument("--all", action="store_true", help="Bootstrap all nuclei")
    parser.add_argument("--level", type=int, default=2, choices=[2, 3], help="Hydration level")
    parser.add_argument("--target", type=float, default=8.0, help="Quality target for level 3")
    parser.add_argument("--dry-run", action="store_true", help="Preview without LLM")
    args = parser.parse_args()

    if not args.nucleus and not args.all:
        parser.error("Specify --nucleus N{XX} or --all")

    nuclei = BUILD_ORDER if args.all else [args.nucleus.upper()]

    # Validate
    for n in nuclei:
        if n not in EXPANSION_MAP:
            print(f"  ERROR: Unknown nucleus {n}")
            sys.exit(1)

    if args.level == 2:
        level2_expand(nuclei, args.dry_run)
    elif args.level == 3:
        level3_quality_spiral(nuclei, args.target, args.dry_run)


if __name__ == "__main__":
    main()
