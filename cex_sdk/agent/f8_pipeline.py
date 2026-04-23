# cex_sdk.agent.f8_pipeline -- F1 CONSTRAIN + F4 REASON helpers
# kind: workflow / pillar: P12 / 8F: F1 + F4
# -*- coding: ascii -*-
from __future__ import annotations

PILLAR_MAP: dict[str, str] = {
    "agent": "P02",
    "agent_card": "P08",
    "system_prompt": "P03",
    "prompt_template": "P03",
    "chain": "P03",
    "knowledge_card": "P01",
    "glossary_entry": "P01",
    "rag_source": "P01",
    "embedding_config": "P01",
    "retriever_config": "P01",
    "chunk_strategy": "P01",
    "input_schema": "P06",
    "data_contract": "P06",
    "validator": "P06",
    "type_de": "P06",
    "interface": "P06",
    "landing_page": "P05",
    "formatter": "P05",
    "parser": "P05",
    "component_map": "P08",
    "decision_record": "P08",
    "diagram": "P08",
    "naming_rule": "P08",
    "workflow": "P12",
    "schedule": "P12",
    "dispatch_rule": "P12",
    "quality_gate": "P11",
    "guardrail": "P11",
    "bugloop": "P11",
    "learning_record": "P11",
    "env_config": "P09",
    "feature_flag": "P09",
    "secret_config": "P09",
    "rate_limit_config": "P09",
    "knowledge_index": "P10",
    "entity_memory": "P10",
    "memory_summary": "P10",
    "prompt_cache": "P10",
    "user_model": "P10",
    "cli_tool": "P04",
    "browser_tool": "P04",
    "mcp_server": "P04",
    "webhook": "P04",
    "api_client": "P04",
    "research_pipeline": "P04",
    "model_provider": "P02",
    "fallback_chain": "P02",
    "boot_config": "P02",
    "benchmark": "P07",
    "scoring_rubric": "P07",
    "llm_judge": "P07",
    "eval_dataset": "P07",
}

_DEFAULT_PILLAR = "P02"


def resolve_kind_pillar(kind: str) -> tuple[str, str]:
    """F1 CONSTRAIN: return (kind, pillar) from PILLAR_MAP or default."""
    k = kind.strip().lower().replace("-", "_")
    pillar = PILLAR_MAP.get(k, _DEFAULT_PILLAR)
    return k, pillar


_SYSTEM_TEMPLATE = """\
You are a CEX artifact builder (8F pipeline, N03 Inventive Pride).

Kind: {kind}
Pillar: {pillar}
Quality target: 9.0+

OUTPUT FORMAT (mandatory):
1. Start with YAML frontmatter between --- markers:
   ---
   id: {kind}_<short_slug>
   kind: {kind}
   title: "<descriptive title>"
   version: "1.0.0"
   pillar: {pillar}
   quality: null
   description: "<one sentence>"
   ---
2. Follow with a structured body (use ## sections and tables, not walls of prose).
3. Density target: 0.85+ (structured data preferred over prose).
4. Body minimum: 300 chars.

{context_section}
"""


def build_system_prompt(kind: str, pillar: str, context_injection: str = "") -> str:
    """F4 REASON: assemble the system prompt for the LLM call."""
    context_section = ""
    if context_injection:
        context_section = "=== CEX Kind Context ===\n" + context_injection
    return _SYSTEM_TEMPLATE.format(
        kind=kind,
        pillar=pillar,
        context_section=context_section,
    ).strip()
