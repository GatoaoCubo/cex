#!/usr/bin/env python3
# -*- coding: ascii -*-
"""cex_kind_deps.py -- kind dependency graph builder and kinds_meta.json enricher.

Reads N00_genesis/P01_knowledge/library/kind/kc_*.md files, extracts cross-kind
references, and outputs a dependency graph. Optionally patches kinds_meta.json
with depends_on fields.

Usage:
  python _tools/cex_kind_deps.py --scan          # scan KCs for deps, print graph
  python _tools/cex_kind_deps.py --patch         # patch kinds_meta.json with depends_on
  python _tools/cex_kind_deps.py --report        # human-readable dep report
  python _tools/cex_kind_deps.py --critical-path # show longest dep chains
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KC_DIR = ROOT / "N00_genesis" / "P01_knowledge" / "library" / "kind"
KINDS_META = ROOT / ".cex" / "kinds_meta.json"

# Known cross-kind dependency map (kind -> depends_on list)
KNOWN_DEPS: dict[str, list[str]] = {
    "agent": ["system_prompt", "boot_config", "agent_card"],
    "agent_card": ["agent", "capability_registry"],
    "workflow": ["dispatch_rule", "schedule", "crew_template"],
    "crew_template": ["role_assignment", "capability_registry", "team_charter"],
    "team_charter": ["crew_template", "role_assignment"],
    "agentic_rag": ["rag_source", "retriever_config", "embedding_config", "chunk_strategy"],
    "rag_source": ["chunk_strategy", "embedding_config"],
    "retriever_config": ["embedding_config", "vector_store"],
    "knowledge_index": ["rag_source", "chunk_strategy"],
    "memory_summary": ["entity_memory", "episodic_memory"],
    "entity_memory": ["knowledge_index"],
    "prompt_cache": ["system_prompt", "prompt_template"],
    "chain": ["prompt_template", "action_prompt"],
    "saga": ["workflow", "dispatch_rule"],
    "dag": ["workflow", "schedule"],
    "deployment_manifest": ["env_config", "boot_config", "secret_config"],
    "canary_config": ["deployment_manifest", "feature_flag"],
    "circuit_breaker": ["retry_policy", "rate_limit_config"],
    "fallback_chain": ["model_provider", "retry_policy"],
    "quality_gate": ["scoring_rubric", "eval_metric"],
    "llm_judge": ["scoring_rubric", "prompt_template"],
    "benchmark": ["eval_dataset", "scoring_rubric", "eval_metric"],
    "eval_dataset": ["dataset_card"],
    "bugloop": ["regression_check", "quality_gate"],
    "learning_record": ["quality_gate", "scoring_rubric"],
    "red_team_eval": ["guardrail", "scoring_rubric"],
    "guardrail": ["constitutional_rule", "content_filter"],
    "renewal_workflow": ["churn_prevention_playbook", "expansion_play"],
    "expansion_play": ["customer_segment", "sales_playbook"],
    "churn_prevention_playbook": ["customer_segment", "cohort_analysis"],
    "ab_test_config": ["feature_flag", "eval_metric"],
    "realtime_session": ["session_state", "session_backend"],
    "session_state": ["session_backend", "entity_memory"],
    "data_contract": ["input_schema", "output_validator", "validation_schema"],
    "openapi_spec": ["api_client", "data_contract"],
    "mcp_server": ["api_client", "openapi_spec"],
    "research_pipeline": ["search_tool", "document_loader", "knowledge_card"],
    "knowledge_graph": ["ontology", "entity_memory"],
    "ontology": ["domain_vocabulary", "glossary_entry"],
    "voice_pipeline": ["stt_provider", "tts_provider", "vad_config"],
}


def _load_kinds() -> dict:
    with KINDS_META.open(encoding="utf-8") as f:
        return json.load(f)


def _scan_kc_for_refs(kind: str, kind_names: set) -> list[str]:
    """Scan KC file for references to other registered kinds."""
    kc_path = KC_DIR / f"kc_{kind}.md"
    if not kc_path.exists():
        return []
    text = kc_path.read_text(encoding="utf-8", errors="replace")
    refs = re.findall(r"`([a-z][a-z_]+)`", text)
    return [r for r in refs if r in kind_names and r != kind]


def _build_graph(kinds: dict) -> dict[str, list[str]]:
    """Build complete dependency graph from meta + known deps + KC scan.

    Priority: depends_on already in kinds_meta.json > KNOWN_DEPS > KC scan.
    This ensures manually-patched deps survive repeated --patch calls.
    """
    kind_names = set(kinds.keys())
    graph: dict[str, list[str]] = {}
    for kind in kind_names:
        # L0: already persisted in meta (highest priority)
        meta_deps = kinds[kind].get("depends_on", [])
        if meta_deps:
            graph[kind] = [d for d in meta_deps if d in kind_names]
            continue
        # L1: explicit KNOWN_DEPS table
        deps = list(KNOWN_DEPS.get(kind, []))
        # L2: KC scan for additional cross-references
        for ref in _scan_kc_for_refs(kind, kind_names):
            if ref not in deps:
                deps.append(ref)
        graph[kind] = [d for d in deps if d in kind_names]
    return graph


def _chain_len(kind: str, graph: dict, visited: set) -> int:
    if kind not in graph or not graph[kind] or kind in visited:
        return 0
    visited.add(kind)
    return 1 + max((_chain_len(d, graph, visited.copy()) for d in graph[kind]), default=0)


def cmd_scan(args) -> int:
    kinds = _load_kinds()
    graph = _build_graph(kinds)
    total_with_deps = sum(1 for v in graph.values() if v)
    print(f"[kind_deps] {len(graph)} kinds scanned, {total_with_deps} have dependencies")
    for kind in sorted(graph):
        if graph[kind]:
            print(f"  {kind} -> {', '.join(graph[kind])}")
    return 0


def cmd_patch(args) -> int:
    kinds = _load_kinds()
    graph = _build_graph(kinds)
    patched = 0
    for kind, deps in graph.items():
        if kind in kinds and deps:
            if kinds[kind].get("depends_on") != deps:
                kinds[kind]["depends_on"] = deps
                patched += 1
    with KINDS_META.open("w", encoding="utf-8") as f:
        json.dump(kinds, f, indent=2, ensure_ascii=False)
    print(f"[kind_deps] patched {patched} kinds in kinds_meta.json with depends_on")
    return 0


def cmd_report(args) -> int:
    kinds = _load_kinds()
    graph = _build_graph(kinds)
    chains = sorted(
        [(len(v), k) for k, v in graph.items() if v], reverse=True
    )[:10]
    print("[kind_deps] Highest-dep kinds:")
    for count, kind in chains:
        print(f"  {kind}: {count} direct deps -> {', '.join(graph[kind])}")
    depended_on: dict[str, int] = defaultdict(int)
    for deps in graph.values():
        for d in deps:
            depended_on[d] += 1
    top = sorted(depended_on.items(), key=lambda x: -x[1])[:10]
    print("\n[kind_deps] Most-depended-on (foundation) kinds:")
    for kind, count in top:
        print(f"  {kind}: needed by {count} other kinds")
    return 0


def cmd_critical_path(args) -> int:
    kinds = _load_kinds()
    graph = _build_graph(kinds)
    paths = sorted(
        [(_chain_len(k, graph, set()), k) for k in graph], reverse=True
    )[:10]
    print("[kind_deps] Critical paths (longest build sequences):")
    for length, kind in paths:
        chain = [kind]
        cur = kind
        for _ in range(length):
            deps = graph.get(cur, [])
            if not deps:
                break
            cur = deps[0]
            chain.append(cur)
        print(f"  depth={length}: {' -> '.join(chain)}")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--patch", action="store_true")
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--critical-path", action="store_true")
    args = parser.parse_args(argv[1:])

    if args.patch:
        return cmd_patch(args)
    if args.scan:
        return cmd_scan(args)
    if args.critical_path:
        return cmd_critical_path(args)
    return cmd_report(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
