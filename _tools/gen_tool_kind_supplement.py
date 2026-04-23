#!/usr/bin/env python3
# -*- coding: ascii -*-
"""gen_tool_kind_supplement.py -- Build pillar-based kind-to-tool supplement.

Merges with kind_tool_registry.json to extend coverage from 47 to 293 kinds.
Maps _tools/cex_*.py to kinds by pillar domain knowledge and name matching.

Usage:
  python _tools/gen_tool_kind_supplement.py
  python _tools/gen_tool_kind_supplement.py --merge  # write merged registry
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KINDS_META = ROOT / ".cex" / "kinds_meta.json"
REGISTRY = ROOT / ".cex" / "kind_tool_registry.json"
SUPPLEMENT = ROOT / ".cex" / "kind_tool_supplement.json"
TOOLS_DIR = ROOT / "_tools"

# Pillar -> tools that serve ALL kinds in that pillar
PILLAR_TOOLS: dict[str, list[str]] = {
    "P01": [
        "cex_retriever.py", "cex_memory_select.py", "cex_query.py",
        "cex_fts5_search.py", "cex_compile.py",
    ],
    "P02": [
        "cex_agent_spawn.py", "cex_router.py", "cex_model_updater.py",
        "cex_crew.py", "cex_8f_runner.py",
    ],
    "P03": [
        "cex_prompt_cache.py", "cex_prompt_optimizer.py", "cex_prompt_layers.py",
        "cex_skill_loader.py", "cex_crew_runner.py",
    ],
    "P04": [
        "cex_kind_tool_map.py", "cex_batch.py", "cex_8f_runner.py",
        "cex_run.py",
    ],
    "P05": [
        "cex_compile.py", "cex_schema_hydrate.py", "cex_8f_runner.py",
        "cex_materialize.py",
    ],
    "P06": [
        "cex_hooks.py", "cex_schema_hydrate.py", "cex_compile.py",
        "cex_hooks_native.py",
    ],
    "P07": [
        "cex_score.py", "cex_feedback.py", "cex_quality_monitor.py",
        "cex_evolve.py", "cex_flywheel_audit.py", "cex_system_test.py",
    ],
    "P08": [
        "cex_doctor.py", "cex_flywheel_audit.py", "cex_stats.py",
        "cex_kind_deps.py",
    ],
    "P09": [
        "cex_setup_validator.py", "cex_preflight.py", "cex_quota_check.py",
        "cex_router.py", "cex_hooks_native.py",
    ],
    "P10": [
        "cex_memory_update.py", "cex_memory_select.py", "cex_memory_age.py",
        "cex_memory_types.py", "cex_user_model.py", "cex_fts5_search.py",
    ],
    "P11": [
        "cex_feedback.py", "cex_evolve.py", "cex_score.py",
        "cex_quality_monitor.py", "cex_hooks.py", "cex_hooks_native.py",
        "cex_mirror_audit.py",
    ],
    "P12": [
        "cex_mission.py", "cex_mission_runner.py", "cex_gdp.py",
        "cex_coordinator.py", "cex_crew.py", "cex_signal_watch.py",
        "signal_writer.py",
    ],
}

# Kind -> specific tools (overrides pillar mapping for precision)
KIND_TOOLS: dict[str, list[str]] = {
    "knowledge_card": ["cex_retriever.py", "cex_query.py", "cex_compile.py", "cex_memory_select.py"],
    "rag_source": ["cex_retriever.py", "cex_schema_hydrate.py"],
    "chunk_strategy": ["cex_retriever.py", "cex_schema_hydrate.py"],
    "entity_memory": ["cex_memory_update.py", "cex_memory_select.py", "cex_memory_age.py"],
    "knowledge_index": ["cex_fts5_search.py", "cex_memory_select.py", "cex_retriever.py"],
    "agent": ["cex_agent_spawn.py", "cex_crew.py", "cex_8f_runner.py", "cex_materialize.py"],
    "agent_card": ["cex_agent_spawn.py", "cex_materialize.py", "cex_doctor.py"],
    "system_prompt": ["cex_compile.py", "cex_prompt_layers.py", "cex_prompt_cache.py"],
    "prompt_template": ["cex_prompt_optimizer.py", "cex_prompt_cache.py", "cex_skill_loader.py"],
    "prompt_cache": ["cex_prompt_cache.py", "cex_preflight.py"],
    "quality_gate": ["cex_score.py", "cex_hooks.py", "cex_flywheel_audit.py"],
    "scoring_rubric": ["cex_score.py", "cex_feedback.py", "cex_evolve.py"],
    "benchmark": ["cex_score.py", "cex_system_test.py", "cex_evolve.py"],
    "workflow": ["cex_mission_runner.py", "cex_coordinator.py", "cex_gdp.py"],
    "dispatch_rule": ["cex_mission.py", "cex_coordinator.py", "cex_8f_motor.py"],
    "env_config": ["cex_setup_validator.py", "cex_preflight.py", "cex_quota_check.py"],
    "feature_flag": ["cex_setup_validator.py", "cex_hooks_native.py"],
    "rate_limit_config": ["cex_quota_check.py", "cex_router.py"],
    "mcp_server": ["cex_agent_spawn.py", "cex_setup_validator.py"],
    "model_provider": ["cex_model_updater.py", "cex_router.py", "cex_quota_check.py"],
    "component_map": ["cex_doctor.py", "cex_flywheel_audit.py", "cex_stats.py"],
    "decision_record": ["cex_flywheel_audit.py", "cex_doctor.py"],
    "learning_record": ["cex_feedback.py", "cex_evolve.py", "cex_quality_monitor.py"],
    "user_model": ["cex_user_model.py", "cex_memory_update.py"],
    "llm_judge": ["cex_score.py", "cex_evolve.py"],
    "depends_on": ["cex_kind_deps.py"],
}


def build_supplement() -> dict:
    with open(KINDS_META, encoding="utf-8") as f:
        meta = json.load(f)

    # Load existing registry to check already-covered kinds
    existing_kinds: set[str] = set()
    if REGISTRY.exists():
        with open(REGISTRY, encoding="utf-8") as f:
            reg = json.load(f)
        existing_kinds = set(reg.get("kind_to_tools", {}).keys())

    kind_to_tools: dict[str, list[str]] = {}
    tool_to_kinds: dict[str, list[str]] = {}

    for kind, info in meta.items():
        pillar = info.get("pillar", "")
        tools: list[str] = []

        # L1: Kind-specific tools (highest precision)
        if kind in KIND_TOOLS:
            tools = list(KIND_TOOLS[kind])

        # L2: Pillar-based tools (coverage for all remaining kinds)
        if pillar in PILLAR_TOOLS:
            for t in PILLAR_TOOLS[pillar]:
                if t not in tools:
                    tools.append(t)

        # Only include if tool file actually exists
        valid_tools = [t for t in tools if (TOOLS_DIR / t).exists()]
        kind_to_tools[kind] = valid_tools

        for t in valid_tools:
            tool_to_kinds.setdefault(t, [])
            if kind not in tool_to_kinds[t]:
                tool_to_kinds[t].append(kind)

    covered = sum(1 for v in kind_to_tools.values() if v)
    print(f"[supplement] {covered}/{len(meta)} kinds now have tool coverage")

    supplement = {
        "schema": "kind_tool_supplement/v1",
        "generated_by": "gen_tool_kind_supplement.py",
        "kind_count": covered,
        "kind_to_tools": {k: v for k, v in sorted(kind_to_tools.items()) if v},
        "tool_to_kinds": {t: sorted(k) for t, k in sorted(tool_to_kinds.items())},
    }
    with open(SUPPLEMENT, "w", encoding="utf-8") as f:
        json.dump(supplement, f, indent=2)
    print(f"[OK] {SUPPLEMENT} written")
    return supplement


def merge_into_registry(supplement: dict) -> None:
    if not REGISTRY.exists():
        print("[WARN] kind_tool_registry.json not found, cannot merge")
        return
    with open(REGISTRY, encoding="utf-8") as f:
        reg = json.load(f)

    # Merge kind_to_tools
    for kind, tools in supplement["kind_to_tools"].items():
        existing = reg["kind_to_tools"].get(kind, [])
        merged = list(dict.fromkeys(existing + tools))
        reg["kind_to_tools"][kind] = merged

    # Merge tool_to_kinds
    for tool, kinds in supplement["tool_to_kinds"].items():
        existing = reg["tool_to_kinds"].get(tool, [])
        merged = sorted(set(existing) | set(kinds))
        reg["tool_to_kinds"][tool] = merged

    reg["kind_count"] = len(reg["kind_to_tools"])
    reg["generated_by"] = "cex_kind_tool_map.py + gen_tool_kind_supplement.py"

    with open(REGISTRY, "w", encoding="utf-8") as f:
        json.dump(reg, f, indent=2)

    covered = sum(1 for v in reg["kind_to_tools"].values() if v)
    print(f"[OK] Registry merged: {covered}/{len(reg['kind_to_tools'])} kinds with tools")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--merge", action="store_true", help="Merge into kind_tool_registry.json")
    args = parser.parse_args()

    supplement = build_supplement()
    if args.merge:
        merge_into_registry(supplement)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
