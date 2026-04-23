#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Flywheel Worker: executes one cycle for a nucleus.

Each call:
  1. Gap analysis (what's missing?)
  2. Build missing artifacts via 8F Runner
  3. Fix broken artifacts (frontmatter, YAML)
  4. Write completion signal
  5. Output summary for next nucleus

Usage:
    python _tools/cex_flywheel_worker.py --nucleus N03 --cycle 1
    python _tools/cex_flywheel_worker.py --nucleus N01 --cycle 2 --level 2
"""
import argparse
import subprocess
import sys
from pathlib import Path
from typing import Any

CEX_ROOT = Path(__file__).resolve().parent.parent
SIGNAL_DIR = CEX_ROOT / ".cex_signals"
SIGNAL_DIR.mkdir(exist_ok=True)

# Core 7 kinds every nucleus needs
CORE_KINDS = ["agent_card", "agent", "system_prompt", "dispatch_rule",
              "knowledge_card", "workflow", "quality_gate"]

# Level 2 expansion kinds per nucleus
L2_KINDS = {
    "N01": ["rag_source", "embedding_config", "few_shot_example", "scoring_rubric", "prompt_template"],
    "N02": ["prompt_template", "persona_prompt", "action_prompt", "few_shot_example", "scoring_rubric"],
    "N03": ["pattern", "scoring_rubric", "interface", "skill", "boot_config", "response_format"],
    "N04": ["chunk_strategy", "retriever_config", "embedding_config", "rag_source", "scoring_rubric"],
    "N05": ["spawn_config", "signal", "checkpoint", "deploy_config", "health_check"],
    "N06": ["few_shot_example", "scoring_rubric", "schedule", "prompt_template"],
    "N07": ["dag", "handof", "signal", "spawn_config", "dispatch_rule"],
}

NUCLEUS_DIRS = {
    "N01": "N01_intelligence", "N02": "N02_marketing", "N03": "N03_engineering",
    "N04": "N04_knowledge", "N05": "N05_operations", "N06": "N06_commercial",
    "N07": "N07_admin",
}

NUCLEUS_DOMAINS = {
    "N01": "Research", "N02": "Marketing", "N03": "Engineering",
    "N04": "Knowledge", "N05": "Operations", "N06": "Commercial", "N07": "Admin",
}

KIND_PATTERNS = {
    "agent_card": ["agent_card_", "agent_card.md"],
    "agent": ["agent_"],
    "system_prompt": ["system_prompt_", "system_prompt.md"],
    "dispatch_rule": ["dispatch_rule_", "dispatch_rule.md"],
    "knowledge_card": ["kc_", "knowledge_card_", "knowledge_card.md"],
    "workflow": ["workflow_", "workflow.md"],
    "quality_gate": ["quality_gate_", "quality_gate.md"],
}


def gap_analysis(nucleus: str, level: int = 1) -> dict[str, Any]:
    """Find which kinds are missing for this nucleus."""
    ndir = CEX_ROOT / NUCLEUS_DIRS[nucleus]
    kinds_needed = list(CORE_KINDS)
    if level >= 2:
        kinds_needed.extend(L2_KINDS.get(nucleus, []))

    gaps = []
    have = []
    for kind in kinds_needed:
        found = False
        patterns = KIND_PATTERNS.get(kind, [f"{kind}_", f"{kind}.md"])
        for pattern in patterns:
            matches = list(ndir.rglob(f"*{pattern}*"))
            if kind == "agent":
                matches = [m for m in matches if "agent_card" not in m.name]
            if matches:
                # Check it's not just a template with {{variables}}
                content = matches[0].read_text(encoding="utf-8", errors="ignore")
                if "{{" not in content[:200]:
                    found = True
                    break
        if found:
            have.append(kind)
        else:
            gaps.append(kind)

    return {"have": have, "gaps": gaps, "total": len(kinds_needed)}


def build_kinds(
    nucleus: str, kinds: list[str], dry_run: bool = False
) -> dict[str, Any]:
    """Call nucleus builder for missing kinds."""
    domain = NUCLEUS_DOMAINS[nucleus]
    name = domain.lower()
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

    result = subprocess.run(cmd, cwd=str(CEX_ROOT), capture_output=True, text=True, timeout=600)

    # Count passes
    passes = result.stdout.count("PASS")
    fails = result.stdout.count("FAIL")
    return {"passes": passes, "fails": fails, "output": result.stdout[-500:]}


def write_signal(
    nucleus: str,
    cycle: int,
    status: str,
    details: dict[str, Any] | None = None,
) -> Any:
    """Write completion signal (delegates to signal_writer)."""
    from signal_writer import write_signal as _sw
    return _sw(nucleus, status=status, mission=f"cycle{cycle}", **details or {})


def main() -> None:
    ap = argparse.ArgumentParser(description="CEX Flywheel Worker")
    ap.add_argument("--nucleus", required=True, help="N01-N07")
    ap.add_argument("--cycle", type=int, default=1, help="Cycle number")
    ap.add_argument("--level", type=int, default=1, choices=[1, 2], help="1=core, 2=expanded")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    nuc = args.nucleus.upper()
    if nuc not in NUCLEUS_DIRS:
        print(f"ERROR: Unknown nucleus {nuc}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"  FLYWHEEL: {nuc} ({NUCLEUS_DOMAINS[nuc]}) | Cycle {args.cycle} | Level {args.level}")
    print(f"{'='*60}")

    # Gap analysis
    gaps = gap_analysis(nuc, args.level)
    print(f"\n  GAP: {len(gaps['have'])}/{gaps['total']} have, {len(gaps['gaps'])} missing")

    if not gaps["gaps"]:
        print("  COMPLETE: no gaps found")
        sig = write_signal(nuc, args.cycle, "complete", {"have": len(gaps["have"])})
        print(f"  Signal: {sig.name}")
        return

    print(f"  BUILD: {', '.join(gaps['gaps'][:8])}{'...' if len(gaps['gaps']) > 8 else ''}")

    # Build
    result = build_kinds(nuc, gaps["gaps"], args.dry_run)
    print(f"\n  RESULT: {result['passes']} PASS, {result['fails']} FAIL")

    # Signal
    status = "complete" if result["fails"] == 0 else "partial"
    sig = write_signal(nuc, args.cycle, status, {
        "passes": result["passes"],
        "fails": result["fails"],
        "gaps_remaining": max(0, len(gaps["gaps"]) - result["passes"]),
    })
    print(f"  Signal: {sig.name}")
    print(f"\n{'='*60}")


if __name__ == "__main__":
    main()
