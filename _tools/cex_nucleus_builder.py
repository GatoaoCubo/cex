#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cex_nucleus_builder.py -- Build a complete nucleus via 8F Runner.

Sequentially produces the 7 core artifacts for a nucleus:
  1. agent_card (P08) -- deployment spec
  2. agent (P02) -- persona
  3. system_prompt (P03) -- voice
  4. dispatch_rule (P12) -- routing
  5. knowledge_card (P01) -- domain knowledge
  6. workflow (P12) -- execution pipeline
  7. quality_gate (P11) -- standards

Usage:
  python _tools/cex_nucleus_builder.py --nucleus N01 --name research --domain "Research & Intelligence" --context "..."
  python _tools/cex_nucleus_builder.py --nucleus N03 --name engineering --domain "Engineering & Build" --dry-run
"""

import argparse
import subprocess
import sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent

# Nucleus -> subdirectory mapping for each kind
KIND_TO_SUBDIR = {
    # Core 7 (every nucleus)
    "agent_card": "architecture",
    "agent": "agents",
    "system_prompt": "prompts",
    "dispatch_rule": "orchestration",
    "knowledge_card": "knowledge",
    "workflow": "orchestration",
    "quality_gate": "feedback",
    # P01 Knowledge
    "rag_source": "knowledge",
    "research_brie": "knowledge",
    # P02 Agent
    "persona_prompt": "prompts",
    "action_prompt": "prompts",
    "boot_config": "config",
    # P03 Prompt
    "prompt_template": "prompts",
    "instruction": "prompts",
    # P04 Tools
    "skill": "tools",
    "tool_definition": "tools",
    "mcp_server": "tools",
    # P05 Output
    "response_format": "output",
    # P06 Input
    "input_schema": "schemas",
    # P07 Quality
    "scoring_rubric": "quality",
    "few_shot_example": "quality",
    # P08 Architecture
    "pattern": "architecture",
    "interface": "architecture",
    # P09 Config
    "env_config": "config",
    "deploy_config": "config",
    # P10 Memory
    "learning_record": "memory",
    "checkpoint": "memory",
    # P11 Feedback
    "health_check": "feedback",
    # P12 Orchestration
    "dag": "orchestration",
    "handof": "orchestration",
    "signal": "orchestration",
    "spawn_config": "orchestration",
    "schedule": "orchestration",
    "retry_policy": "orchestration",
    "pipeline": "orchestration",
    # Retrieval
    "chunk_strategy": "knowledge",
    "retriever_config": "knowledge",
    "knowledge_index": "knowledge",
    "embedding_config": "knowledge",
}

# Build order (dependencies flow top-down)
BUILD_ORDER = [
    "agent_card",
    "agent",
    "system_prompt",
    "dispatch_rule",
    "knowledge_card",
    "workflow",
    "quality_gate",
]

# Nucleus directory names
NUCLEUS_DIRS = {
    "N01": "N01_intelligence",
    "N02": "N02_marketing",
    "N03": "N03_engineering",
    "N04": "N04_knowledge",
    "N05": "N05_operations",
    "N06": "N06_commercial",
    "N07": "N07_admin",
}


def main():
    parser = argparse.ArgumentParser(description="Build a complete CEX nucleus via 8F Runner")
    parser.add_argument("--nucleus", required=True, choices=NUCLEUS_DIRS.keys(),
                        help="Nucleus ID (N01-N07)")
    parser.add_argument("--name", required=True, help="Nucleus name (e.g. research, engineering)")
    parser.add_argument("--domain", required=True, help="Domain description")
    parser.add_argument("--context", default="", help="Additional domain context (PRIME excerpt, etc)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without LLM calls")
    parser.add_argument("--kinds", nargs="*", help="Only build these kinds (default: all 7)")
    args = parser.parse_args()

    nucleus_dir = CEX_ROOT / NUCLEUS_DIRS[args.nucleus]
    kinds = args.kinds or BUILD_ORDER
    runner = CEX_ROOT / "_tools" / "cex_8f_runner.py"

    # Build context string: auto-load seed if exists
    seed_file = CEX_ROOT / "_seeds" / f"seed_{args.nucleus.lower()}_{args.name.lower()}.txt"
    if not seed_file.exists():
        seed_file = CEX_ROOT / "_seeds" / f"seed_{args.nucleus.lower()}.txt"
    seed_text = ""
    if seed_file.exists():
        seed_text = seed_file.read_text(encoding="utf-8").strip()
        print(f"  Seed: {seed_file.name} ({len(seed_text)} chars)")

    context = seed_text if seed_text else f"Nucleus {args.nucleus} ({args.name}), domain: {args.domain}"
    if args.context:
        context = args.context if not seed_text else seed_text + " " + args.context

    print(f"\n{'=' * 70}")
    print(f"  CEX Nucleus Builder -- {args.nucleus} ({args.name})")
    print(f"  Domain: {args.domain}")
    print(f"  Kinds: {len(kinds)} artifacts")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'EXECUTE'}")
    print(f"{'=' * 70}\n")

    results = []
    for i, kind in enumerate(kinds):
        if kind not in KIND_TO_SUBDIR:
            print(f"  [{i+1}/{len(kinds)}] SKIP {kind} (unknown subdir)")
            continue

        subdir = KIND_TO_SUBDIR[kind]
        output_dir = nucleus_dir / subdir
        intent = f"create {kind} for {args.name} {args.domain} nucleus"

        print(f"  [{i+1}/{len(kinds)}] {kind} -> {output_dir.relative_to(CEX_ROOT)}/")

        cmd = [
            sys.executable, str(runner),
            intent,
            "--kind", kind,
            "--context", context,
            "--output-dir", str(output_dir),
        ]
        if args.dry_run:
            cmd.append("--dry-run")

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            # Parse verdict from output
            verdict = "UNKNOWN"
            for line in result.stdout.split("\n"):
                if "Verdict:" in line:
                    verdict = line.strip().split("Verdict:")[1].strip()[:30]
                    break
            results.append((kind, verdict))
            print(f"           -> {verdict}")
            if result.returncode != 0 and result.stderr:
                print(f"           ! {result.stderr[:100]}")
        except subprocess.TimeoutExpired:
            results.append((kind, "TIMEOUT"))
            print("           -> TIMEOUT (>120s)")
        except Exception as e:
            results.append((kind, f"ERROR: {e}"))
            print(f"           -> ERROR: {e}")

    # Summary
    print(f"\n{'=' * 70}")
    print(f"  SUMMARY -- {args.nucleus} ({args.name})")
    print(f"{'=' * 70}")
    for kind, verdict in results:
        status = "PASS" if "PASS" in verdict else "FAIL" if "FAIL" in verdict else verdict
        print(f"  {kind:20s} {status}")
    
    passed = sum(1 for _, v in results if "PASS" in v)
    print(f"\n  {passed}/{len(results)} PASS")
    print(f"{'=' * 70}\n")


if __name__ == "__main__":
    main()
