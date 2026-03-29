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
EXPANSION_MAP = {
    "N01": {
        "name": "shaka", "domain": "Research", "sin": "ENVY",
        "kinds": ["rag_source", "embedding_config", "few_shot_example", "scoring_rubric",
                  "prompt_template", "research_brief"],
    },
    "N02": {
        "name": "lily", "domain": "Marketing", "sin": "LUST",
        "kinds": ["prompt_template", "persona_prompt", "action_prompt", "few_shot_example",
                  "response_format", "scoring_rubric"],
    },
    "N03": {
        "name": "edison", "domain": "Engineering", "sin": "PRIDE",
        "kinds": ["pattern", "scoring_rubric", "interface", "skill",
                  "boot_config", "response_format", "learning_record"],
    },
    "N04": {
        "name": "pytha", "domain": "Knowledge", "sin": "GLUTTONY",
        "kinds": ["chunk_strategy", "retriever_config", "embedding_config",
                  "rag_source", "learning_record", "scoring_rubric"],
    },
    "N05": {
        "name": "atlas", "domain": "Operations", "sin": "WRATH",
        "kinds": ["spawn_config", "signal", "checkpoint", "deploy_config",
                  "env_config", "health_check", "retry_policy"],
    },
    "N06": {
        "name": "york", "domain": "Commercial", "sin": "GREED",
        "kinds": ["few_shot_example", "scoring_rubric", "schedule",
                  "prompt_template", "learning_record", "response_format"],
    },
    "N07": {
        "name": "stella", "domain": "Admin", "sin": "SLOTH",
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
    ] + kinds

    if dry_run:
        cmd.append("--dry-run")

    print(f"\n{'='*60}")
    print(f"  {nucleus} ({name}) -- {EXPANSION_MAP[nucleus]['sin']}")
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
    print(f"  LEVEL 2 EXPANSION SUMMARY")
    print(f"{'='*60}")
    for nuc, ok in results.items():
        info = EXPANSION_MAP[nuc]
        status = "DONE" if ok else "PARTIAL"
        print(f"  {nuc} {info['name']:8s} {info['sin']:10s} {len(info['kinds']):2d} kinds  {status}")
    total = sum(len(EXPANSION_MAP[n]["kinds"]) for n in nuclei)
    print(f"\n  Total: {total} artifacts attempted")


def level3_quality_spiral(nuclei, target=8.0, dry_run=False):
    """Level 3: PRIDE loop -- rebuild anything below target."""
    print(f"\n  LEVEL 3: Quality spiral (target={target})")
    print(f"  TODO: Requires cex_doctor.py --score (not yet implemented)")
    print(f"  When implemented:")
    print(f"    1. Doctor scores all artifacts in target nuclei")
    print(f"    2. Any artifact below {target} gets rebuilt via 8F Runner")
    print(f"    3. Repeat until all meet target or max 3 iterations")


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
