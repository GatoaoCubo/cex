#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_8f_motor.py -- Motor 8F: Intent -> Execution Plan

The Motor 8F algorithm receives a natural language intent string and produces
a structured execution plan: which builders to activate, in what order,
with what dependencies, to satisfy the 8 functions of the LLM pipeline.

Pipeline order (from MOTOR_8F_SPEC):
  CONSTRAIN(1) -> BECOME(2) -> INJECT(3) -> REASON(4) ->
  CALL(5) -> PRODUCE(6) -> GOVERN(7) -> COLLABORATE(8)

Usage:
  python cex_8f_motor.py --intent "cria agente de vendas para ML"
  python cex_8f_motor.py --intent "reconstroi signal-builder" --quality 9.5
  python cex_8f_motor.py --intent "create agent AND research workflow"
  python cex_8f_motor.py --intent "cria agente" --output plan.json
  python cex_8f_motor.py --test
"""

import sys

if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")

import argparse
import difflib
import json
import re
from pathlib import Path

# Lazy imports for runtime evolution modules (avoid circular at parse time)
_memory_select = None
_memory_scanner = None


# ---------------------------------------------------------------------------
# Turn Counter -- Runtime Evolution Phase 3C
# ---------------------------------------------------------------------------


class TurnCounter:
    """Track agentic turns per builder execution.

    Each builder has a max_turns budget (from bld_config). The counter
    increments on each agentic turn and raises TurnBudgetExceeded when
    the budget is exhausted.

    Usage:
        counter = TurnCounter()
        counter.register("agent-builder", max_turns=25)
        for each_turn:
            result = counter.increment("agent-builder")
            if result["exhausted"]:
                # stop, return partial + warning
                break
    """

    def __init__(self):
        self._counters: dict[str, dict] = {}

    def register(self, builder_id: str, max_turns: int | None = None) -> None:
        """Register a builder with its turn budget."""
        self._counters[builder_id] = {
            "max_turns": max_turns or 25,
            "current": 0,
            "exhausted": False,
        }

    def increment(self, builder_id: str) -> dict:
        """Increment turn count. Returns status dict.

        Returns:
            {"current": int, "max_turns": int, "exhausted": bool,
             "remaining": int, "warning": str | None}
        """
        if builder_id not in self._counters:
            self.register(builder_id)

        entry = self._counters[builder_id]
        entry["current"] += 1
        remaining = entry["max_turns"] - entry["current"]
        exhausted = entry["current"] >= entry["max_turns"]
        entry["exhausted"] = exhausted

        warning = None
        if exhausted:
            warning = (
                f"TURN_BUDGET_EXHAUSTED: {builder_id} used "
                f"{entry['current']}/{entry['max_turns']} turns. "
                "Returning partial result."
            )
        elif remaining <= 3:
            warning = (
                f"TURN_BUDGET_LOW: {builder_id} has {remaining} turns "
                f"remaining ({entry['current']}/{entry['max_turns']})."
            )

        return {
            "builder_id": builder_id,
            "current": entry["current"],
            "max_turns": entry["max_turns"],
            "remaining": max(0, remaining),
            "exhausted": exhausted,
            "warning": warning,
        }

    def status(self, builder_id: str) -> dict | None:
        """Get current status without incrementing."""
        return self._counters.get(builder_id)

    def all_status(self) -> dict:
        """Get status of all registered builders."""
        return dict(self._counters)

    def reset(self, builder_id: str) -> None:
        """Reset counter for a builder."""
        if builder_id in self._counters:
            self._counters[builder_id]["current"] = 0
            self._counters[builder_id]["exhausted"] = False


# Global turn counter instance (shared across motor execution)
turn_counter = TurnCounter()

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CEX_ROOT = Path(__file__).resolve().parent.parent
BUILDER_MAP_PATH = CEX_ROOT / "_docs" / "8F_BUILDER_MAP.yaml"
KC_LIBRARY_PATH = CEX_ROOT / "N00_genesis" / "P01_knowledge" / "library"
KC_DOMAIN_PATH = KC_LIBRARY_PATH / "domain"
KC_KIND_PATH = KC_LIBRARY_PATH / "kind"
KC_INDEX_PATH = KC_LIBRARY_PATH / "index.yaml"

FUNCTION_POSITIONS = {
    "CONSTRAIN": 1,
    "BECOME": 2,
    "INJECT": 3,
    "REASON": 4,
    "CALL": 5,
    "PRODUCE": 6,
    "GOVERN": 7,
    "COLLABORATE": 8,
}

# Verb normalization: PT imperative/infinitive + EN verbs -> canonical action
VERB_TABLE = {
    # --- PT verbs (original) ---
    "cria": "create",
    "criar": "create",
    "crie": "create",
    "melhora": "improve",
    "melhorar": "improve",
    "melhore": "improve",
    "reconstroi": "rebuild",
    "reconstruir": "rebuild",
    "reconstrua": "rebuild",
    "analisa": "analyze",
    "analisar": "analyze",
    "analise": "analyze",
    "valida": "validate",
    "validar": "validate",
    "valide": "validate",
    "documenta": "document",
    "documentar": "document",
    "documente": "document",
    "integra": "integrate",
    "integrar": "integrate",
    "integre": "integrate",
    "testa": "validate",
    "testar": "validate",
    "teste": "validate",
    "implanta": "deploy",
    "implantar": "deploy",
    "implante": "deploy",
    "configura": "create",
    "configurar": "create",
    "configure": "create",
    "otimiza": "improve",
    "otimizar": "improve",
    "otimize": "improve",
    "audita": "analyze",
    "auditar": "analyze",
    "audite": "analyze",
    "monitora": "analyze",
    "monitorar": "analyze",
    "monitore": "analyze",
    "agenda": "deploy",
    "agendar": "deploy",
    "agende": "deploy",
    "pesquisa": "analyze",
    "pesquisar": "analyze",
    "pesquise": "analyze",
    # --- EN verbs ---
    "create": "create",
    "build": "create",
    "make": "create",
    "design": "create",
    "setup": "create",
    "scaffold": "create",
    "generate": "create",
    "add": "create",
    "improve": "improve",
    "enhance": "improve",
    "upgrade": "improve",
    "optimize": "improve",
    "refactor": "improve",
    "update": "improve",
    "modify": "improve",
    "change": "improve",
    "rebuild": "rebuild",
    "reconstruct": "rebuild",
    "redo": "rebuild",
    "recreate": "rebuild",
    "analyze": "analyze",
    "analyse": "analyze",
    "research": "analyze",
    "study": "analyze",
    "review": "analyze",
    "audit": "analyze",
    "inspect": "analyze",
    "investigate": "analyze",
    "monitor": "analyze",
    "watch": "analyze",
    "track": "analyze",
    "validate": "validate",
    "verify": "validate",
    "check": "validate",
    "test": "validate",
    "evaluate": "validate",
    "benchmark": "validate",
    "document": "document",
    "describe": "document",
    "explain": "document",
    "write": "document",
    "integrate": "integrate",
    "connect": "integrate",
    "link": "integrate",
    "wire": "integrate",
    "fix": "repair",
    "repair": "repair",
    "debug": "repair",
    "patch": "repair",
    "resolve": "repair",
    "deploy": "deploy",
    "ship": "deploy",
    "release": "deploy",
    "publish": "deploy",
    "launch": "deploy",
    "schedule": "deploy",
    "delete": "delete",
    "remove": "delete",
    "drop": "delete",
    "price": "create",
    "monetize": "create",
}

# Object keyword -> [(kind, pillar, primary_function)]
OBJECT_TO_KINDS = {
    "action_prompt": [("action_prompt", "P03", "PRODUCE")],
    "adr": [("decision_record", "P08", "REASON")],
    "agent": [("agent", "P02", "BECOME")],
    "agente": [("agent", "P02", "BECOME")],
    "api": [("api_client", "P04", "CALL")],
    "api_client": [("api_client", "P04", "CALL")],
    "audio": [("audio_tool", "P04", "CALL")],
    "audio_tool": [("audio_tool", "P04", "CALL")],
    "avaliacao": [("unit_eval", "P07", "GOVERN")],
    "axiom": [("axiom", "P02", "CONSTRAIN")],
    "axioma": [("axiom", "P02", "CONSTRAIN")],
    "benchmark": [("benchmark", "P07", "GOVERN")],
    "boot": [("boot_config", "P02", "CONSTRAIN")],
    "boot_config": [("boot_config", "P02", "CONSTRAIN")],
    "knowledge_index": [("knowledge_index", "P10", "INJECT")],
    "browser": [("browser_tool", "P04", "CALL")],
    "browser_tool": [("browser_tool", "P04", "CALL")],
    "bugloop": [("bugloop", "P11", "GOVERN")],
    "cadeia": [("chain", "P03", "REASON")],
    "chain": [("chain", "P03", "REASON")],
    "checkpoint": [("checkpoint", "P12", "GOVERN")],
    "chunk": [("chunk_strategy", "P01", "CONSTRAIN")],
    "chunk_strategy": [("chunk_strategy", "P01", "CONSTRAIN")],
    "chunking": [("chunk_strategy", "P01", "CONSTRAIN")],
    "cli": [("cli_tool", "P04", "CALL")],
    "cli_tool": [("cli_tool", "P04", "CALL")],
    "code_executor": [("code_executor", "P04", "CALL")],
    "component_map": [("component_map", "P08", "REASON")],
    "computer_use": [("computer_use", "P04", "CALL")],
    "conhecimento": [("knowledge_card", "P01", "INJECT")],
    "constraint": [("constraint_spec", "P03", "CONSTRAIN")],
    "constraint_spec": [("constraint_spec", "P03", "CONSTRAIN")],
    "context": [("context_doc", "P01", "INJECT")],
    "context_doc": [("context_doc", "P01", "INJECT")],
    "contexto": [("context_doc", "P01", "INJECT")],
    "contrato": [("interface", "P06", "CONSTRAIN")],
    "daemon": [("daemon", "P04", "CALL")],
    "dag": [("dag", "P12", "COLLABORATE")],
    "database": [("db_connector", "P04", "CALL")],
    "db_connector": [("db_connector", "P04", "CALL")],
    "decision_record": [("decision_record", "P08", "REASON")],
    "diagram": [("diagram", "P08", "REASON")],
    "director": [("director", "P08", "COLLABORATE")],
    "dispatch_rule": [("dispatch_rule", "P12", "COLLABORATE")],
    "document_loader": [("document_loader", "P04", "CALL")],
    "e2e_eval": [("e2e_eval", "P07", "GOVERN")],
    "effort_profile": [("effort_profile", "P09", "CONSTRAIN")],
    "effort-profile": [("effort_profile", "P09", "CONSTRAIN")],
    "embedding": [("embedding_config", "P01", "CONSTRAIN")],
    "embedding_config": [("embedding_config", "P01", "CONSTRAIN")],
    "entity_memory": [("entity_memory", "P10", "INJECT")],
    "enum": [("enum_de", "P06", "CONSTRAIN")],
    "enum_de": [("enum_de", "P06", "CONSTRAIN")],
    "env": [("env_config", "P09", "CONSTRAIN")],
    "env_config": [("env_config", "P09", "CONSTRAIN")],
    "eval": [("unit_eval", "P07", "GOVERN")],
    "eval_dataset": [("eval_dataset", "P07", "GOVERN")],
    "fallback": [("fallback_chain", "P02", "REASON")],
    "fallback_chain": [("fallback_chain", "P02", "REASON")],
    "feature_flag": [("feature_flag", "P09", "CONSTRAIN")],
    "ferramenta": [("function_de", "P04", "CALL")],
    "few-shot": [("few_shot_example", "P01", "INJECT")],
    "few_shot": [("few_shot_example", "P01", "INJECT")],
    "fonte": [("rag_source", "P01", "INJECT")],
    "formato": [("response_format", "P05", "PRODUCE")],
    "formatter": [("formatter", "P05", "PRODUCE")],
    "function": [("function_de", "P04", "CALL")],
    "function_de": [("function_de", "P04", "CALL")],
    "glossario": [("glossary_entry", "P01", "INJECT")],
    "glossary": [("glossary_entry", "P01", "INJECT")],
    "golden_test": [("golden_test", "P07", "GOVERN")],
    "grafo": [("dag", "P12", "COLLABORATE")],
    "guardrail": [("guardrail", "P11", "GOVERN")],
    "handof": [("handof", "P12", "COLLABORATE")],
    "handoff_protocol": [("handoff_protocol", "P02", "COLLABORATE")],
    "hook": [("hook", "P04", "CALL")],
    "hook_config": [("hook_config", "P04", "CONSTRAIN")],
    "hook-config": [("hook_config", "P04", "CONSTRAIN")],
    "input_schema": [("input_schema", "P06", "CONSTRAIN")],
    "instrucao": [("instruction", "P03", "REASON")],
    "instruction": [("instruction", "P03", "REASON")],
    "interface": [("interface", "P06", "CONSTRAIN")],
    "iso": [("agent_package", "P02", "BECOME")],
    "agent_package": [("agent_package", "P02", "BECOME")],
    "judge": [("llm_judge", "P07", "GOVERN")],
    "knowledge": [("knowledge_card", "P01", "INJECT")],
    "knowledge-card": [("knowledge_card", "P01", "INJECT")],
    "knowledge_card": [("knowledge_card", "P01", "INJECT")],
    "law": [("law", "P08", "CONSTRAIN")],
    "learning_record": [("learning_record", "P10", "INJECT")],
    "lens": [("lens", "P02", "BECOME")],
    "lifecycle_rule": [("lifecycle_rule", "P11", "GOVERN")],
    "llm_judge": [("llm_judge", "P07", "GOVERN")],
    "loader": [("document_loader", "P04", "CALL")],
    "mcp": [("mcp_server", "P04", "CALL")],
    "mcp_server": [("mcp_server", "P04", "CALL")],
    "memoria": [("knowledge_index", "P10", "INJECT")],
    "memory": [("knowledge_index", "P10", "INJECT")],
    "memory_scope": [("memory_scope", "P02", "INJECT")],
    "memory_summary": [("memory_summary", "P10", "INJECT")],
    "mental_model": [("mental_model", "P02", "BECOME")],
    "model_card": [("model_card", "P02", "BECOME")],
    "modelo": [("model_card", "P02", "BECOME")],
    "naming_rule": [("naming_rule", "P05", "CONSTRAIN")],
    "notifier": [("notifier", "P04", "CALL")],
    "optimizer": [("optimizer", "P11", "GOVERN")],
    "output_validator": [("output_validator", "P05", "GOVERN")],
    "parser": [("parser", "P05", "PRODUCE")],
    "path_config": [("path_config", "P09", "CONSTRAIN")],
    "pattern": [("pattern", "P08", "REASON")],
    "permission": [("permission", "P09", "CONSTRAIN")],
    "perspectiva": [("lens", "P02", "BECOME")],
    "pipeline": [("workflow", "P12", "COLLABORATE")],
    "plugin": [("plugin", "P04", "CALL")],
    "prompt": [("system_prompt", "P03", "BECOME")],
    "prompt_template": [("prompt_template", "P03", "PRODUCE")],
    "prompt_version": [("prompt_version", "P03", "GOVERN")],
    "quality_gate": [("quality_gate", "P11", "GOVERN")],
    "rag": [("rag_source", "P01", "INJECT")],
    "rag_source": [("rag_source", "P01", "INJECT")],
    "rate_limit": [("rate_limit_config", "P09", "CONSTRAIN")],
    "rate_limit_config": [("rate_limit_config", "P09", "CONSTRAIN")],
    "red_team": [("red_team_eval", "P07", "GOVERN")],
    "red_team_eval": [("red_team_eval", "P07", "GOVERN")],
    "regra": [("law", "P08", "CONSTRAIN")],
    "regression": [("regression_check", "P07", "GOVERN")],
    "regression_check": [("regression_check", "P07", "GOVERN")],
    "response_format": [("response_format", "P05", "PRODUCE")],
    "restricao": [("guardrail", "P11", "GOVERN")],
    "retriever": [("retriever", "P04", "INJECT")],
    "retriever_config": [("retriever_config", "P01", "CONSTRAIN")],
    "retriever_tool": [("retriever", "P04", "CALL")],
    "reward": [("reward_signal", "P11", "GOVERN")],
    "reward_signal": [("reward_signal", "P11", "GOVERN")],
    "roteamento": [("router", "P02", "REASON")],
    "router": [("router", "P02", "REASON")],
    "runtime_rule": [("runtime_rule", "P09", "CONSTRAIN")],
    "runtime_state": [("runtime_state", "P10", "INJECT")],
    "schedule": [("schedule", "P12", "GOVERN")],
    "schema": [("input_schema", "P06", "CONSTRAIN")],
    "scoring_rubric": [("scoring_rubric", "P07", "GOVERN")],
    "search": [("search_tool", "P04", "CALL")],
    "search_tool": [("search_tool", "P04", "CALL")],
    "secret": [("secret_config", "P09", "GOVERN")],
    "secret_config": [("secret_config", "P09", "GOVERN")],
    "session_state": [("session_state", "P10", "INJECT")],
    "signal": [("signal", "P12", "COLLABORATE")],
    "sinal": [("signal", "P12", "COLLABORATE")],
    "smoke_eval": [("smoke_eval", "P07", "GOVERN")],
    "spawn": [("spawn_config", "P12", "COLLABORATE")],
    "spawn_config": [("spawn_config", "P12", "COLLABORATE")],
    "system_prompt": [("system_prompt", "P03", "BECOME")],
    "template": [("prompt_template", "P03", "PRODUCE")],
    "teste": [("unit_eval", "P07", "GOVERN")],
    "tipo": [("type_de", "P06", "CONSTRAIN")],
    "tool": [("function_de", "P04", "CALL")],
    "type_de": [("type_de", "P06", "CONSTRAIN")],
    "validation_schema": [("validation_schema", "P06", "CONSTRAIN")],
    "validator": [("validator", "P06", "CONSTRAIN")],
    "vision": [("vision_tool", "P04", "CALL")],
    "vision_tool": [("vision_tool", "P04", "CALL")],
    "webhook": [("webhook", "P04", "CALL")],
    "workflow": [("workflow", "P12", "COLLABORATE")],
    # agent_card (P08) -- deployment spec for autonomous agent
    "agent_card": [("agent_card", "P08", "BECOME")],
    "agent-card": [("agent_card", "P08", "BECOME")],
    "agentcard": [("agent_card", "P08", "BECOME")],
    "deployment_spec": [("agent_card", "P08", "BECOME")],
    "deployment": [("agent_card", "P08", "BECOME")],

    "few_shot_example": [("few_shot_example", "P01", "INJECT")],
    "glossary_entry": [("glossary_entry", "P01", "INJECT")],
    "unit_eval": [("unit_eval", "P07", "GOVERN")],
    # --- Previously unreachable kinds (22+) ---
    "citation": [("citation", "P01", "INJECT")],
    "citacao": [("citation", "P01", "INJECT")],
    "compression": [("compression_config", "P09", "CONSTRAIN")],
    "compression_config": [("compression_config", "P09", "CONSTRAIN")],
    "content_monetization": [("content_monetization", "P11", "PRODUCE")],
    "monetization": [("content_monetization", "P11", "PRODUCE")],
    "monetizacao": [("content_monetization", "P11", "PRODUCE")],
    "pricing": [("content_monetization", "P11", "PRODUCE")],
    "context_window": [("context_window_config", "P03", "CONSTRAIN")],
    "context_window_config": [("context_window_config", "P03", "CONSTRAIN")],
    "token_budget": [("context_window_config", "P03", "CONSTRAIN")],
    "embedder": [("embedder_provider", "P01", "CONSTRAIN")],
    "embedder_provider": [("embedder_provider", "P01", "CONSTRAIN")],
    "invariant": [("invariant", "P08", "CONSTRAIN")],
    "landing": [("landing_page", "P05", "PRODUCE")],
    "landing_page": [("landing_page", "P05", "PRODUCE")],
    "memory_type": [("memory_type", "P10", "INJECT")],
    "model_provider": [("model_provider", "P02", "BECOME")],
    "provider": [("model_provider", "P02", "BECOME")],
    "provedor": [("model_provider", "P02", "BECOME")],
    "multi_modal": [("multi_modal_config", "P09", "CONSTRAIN")],
    "multi_modal_config": [("multi_modal_config", "P09", "CONSTRAIN")],
    "multimodal": [("multi_modal_config", "P09", "CONSTRAIN")],
    "prompt_cache": [("prompt_cache", "P10", "CALL")],
    "cache": [("prompt_cache", "P10", "CALL")],
    "reasoning": [("reasoning_trace", "P03", "REASON")],
    "reasoning_trace": [("reasoning_trace", "P03", "REASON")],
    "research_pipeline": [("research_pipeline", "P04", "CALL")],
    "session_backend": [("session_backend", "P09", "CONSTRAIN")],
    "supervisor": [("supervisor", "P02", "COLLABORATE")],
    "supervisao": [("supervisor", "P02", "COLLABORATE")],
    "tagline": [("tagline", "P05", "PRODUCE")],
    "slogan": [("tagline", "P05", "PRODUCE")],
    "toolkit": [("toolkit", "P04", "CALL")],
    "trace": [("trace_config", "P09", "CONSTRAIN")],
    "trace_config": [("trace_config", "P09", "CONSTRAIN")],
    "rastreamento": [("trace_config", "P09", "CONSTRAIN")],
    "vector": [("vector_store", "P01", "INJECT")],
    "vector_store": [("vector_store", "P01", "INJECT")],
    "vetor": [("vector_store", "P01", "INJECT")],
    "workflow_primitive": [("workflow_primitive", "P12", "COLLABORATE")],
    "primitiva": [("workflow_primitive", "P12", "COLLABORATE")],
    # --- Additional EN/PT synonyms for better coverage ---
    "diagrama": [("diagram", "P08", "REASON")],
    "embeddings": [("embedding_config", "P01", "CONSTRAIN")],
    "banco_de_dados": [("db_connector", "P04", "CALL")],
    "base_de_conhecimento": [("rag_source", "P01", "INJECT")],
    "linha_de_comando": [("cli_tool", "P04", "CALL")],
    "competitors": [("knowledge_card", "P01", "INJECT")],
    "competitor": [("knowledge_card", "P01", "INJECT")],
    "concorrente": [("knowledge_card", "P01", "INJECT")],
    "concorrentes": [("knowledge_card", "P01", "INJECT")],
    "tests": [("unit_eval", "P07", "GOVERN")],
    "testing": [("unit_eval", "P07", "GOVERN")],
    "testes": [("unit_eval", "P07", "GOVERN")],
    "page": [("landing_page", "P05", "PRODUCE")],
    "endpoint": [("webhook", "P04", "CALL")],
    "scraper": [("browser_tool", "P04", "CALL")],
    "playbook": [("workflow", "P12", "COLLABORATE")],
    "skill": [("skill", "P04", "CALL")],
    "habilidade": [("skill", "P04", "CALL")],
    "social_publisher": [("social_publisher", "P04", "CALL")],
    "social": [("social_publisher", "P04", "CALL")],
    "instagram": [("social_publisher", "P04", "CALL")],
    "software_project": [("software_project", "P08", "REASON")],
    "projeto": [("software_project", "P08", "REASON")],
    "supabase": [("supabase_data_layer", "P04", "CALL")],
    "supabase_data_layer": [("supabase_data_layer", "P04", "CALL")],
}

# Verb -> extra builders force-activated regardless of tier
VERB_EXTRA_BUILDERS = {
    "improve": {"quality-gate-builder", "scoring-rubric-builder"},
    "rebuild": {"_builder-builder"},
    "analyze": {"scoring-rubric-builder", "unit-eval-builder"},
    "validate": {"validator-builder", "quality-gate-builder"},
    "document": {"knowledge-card-builder", "context-doc-builder"},
    "integrate": {"db-connector-builder", "interface-builder"},
    "repair": {"bugloop-builder", "regression-check-builder"},
    "deploy": {"spawn-config-builder", "env-config-builder"},
    "delete": set(),
}

# Primary builders that need specific keywords to be active (otherwise inactive)
PRIMARY_NEEDS_KEYWORD = {
    "boot-config-builder": ["boot", "inicializacao", "provider"],
    "rag-source-builder": ["rag", "fonte externa", "base de conhecimento"],
    "chain-builder": ["chain", "cadeia", "sequencia de prompts"],
    "mcp-server-builder": ["mcp"],
    "cli-tool-builder": ["cli", "linha de comando", "terminal"],
    "db-connector-builder": ["conector", "integra com", "api externa"],
    "browser-tool-builder": ["scraper", "scraping", "extrai dados"],
    "api-client-builder": ["client", "api rest", "graphql"],
    "formatter-builder": ["formatacao", "formato especial"],
    "parser-builder": ["parser", "parsing", "extrai de output"],
    "workflow-builder": ["workflow", "fluxo", "pipeline multi"],
    "spawn-config-builder": ["spawn", "lancamento", "deploy"],
    "dispatch-rule-builder": ["dispatch", "routing policy", "despacho"],
    "e2e-eval-builder": ["e2e", "end-to-end"],
    "validator-builder-codex": ["codex", "code review", "code review"],
    "type-def-builder": ["tipo customizado", "type definition", "typede"],
    "validation-schema-builder": ["validation schema", "schema de validacao"],
    "daemon-builder": ["daemon", "background", "processo continuo"],
    "plugin-builder": ["plugin", "extensao"],
}

# Token estimation by builder complexity tier
SIMPLE_BUILDERS = frozenset(
    [
        "signal-builder",
        "dispatch-rule-builder",
        "env-config-builder",
        "session-state-builder",
        "naming-rule-builder",
        "path-config-builder",
        "feature-flag-builder",
        "runtime-rule-builder",
        "permission-builder",
        "runtime-state-builder",
    ]
)
COMPLEX_BUILDERS = frozenset(
    [
        "agent-builder",
        "workflow-builder",
        "model-card-builder",
        "agent-package-builder",
        "e2e-eval-builder",
        "supervisor-builder",
    ]
)
META_BUILDERS = frozenset(["_builder-builder"])


# ---------------------------------------------------------------------------
# Effort-Aware Dispatch (Phase 2A -- Runtime Evolution)
# ---------------------------------------------------------------------------

def _load_effort_models() -> dict:
    """Load effort-to-model mapping via cex_model_resolver."""
    try:
        from cex_model_resolver import resolve_model_for_tool
        defaults = {
            "low": resolve_model_for_tool("cex_8f_motor", "light")["model"],
            "medium": resolve_model_for_tool("cex_8f_motor", "standard")["model"],
            "high": resolve_model_for_tool("cex_8f_motor", "heavy")["model"],
            "max": resolve_model_for_tool("cex_8f_motor", "heavy")["model"],
        }
    except Exception:
        defaults = {
            "low": "claude-haiku-4-5-20251001",
            "medium": "claude-sonnet-4-6",
            "high": "claude-opus-4-6",
            "max": "claude-opus-4-6",
        }
    return defaults

EFFORT_TO_MODEL = _load_effort_models()

EFFORT_TO_MAX_TOKENS = {
    "low": 4000,
    "medium": 8000,
    "high": 16000,
    "max": 32000,
}


def resolve_effort_model(effort: str, crew_override: str | None = None) -> dict:
    """Map effort level to LLM model and token budget.

    Args:
        effort: low | medium | high | max
        crew_override: If set by crew runner, overrides effort level.

    Returns:
        {"model": str, "max_tokens": int, "extended_thinking": bool}
    """
    level = crew_override or effort or "medium"
    level = level.lower()
    return {
        "model": EFFORT_TO_MODEL.get(level, EFFORT_TO_MODEL["medium"]),
        "max_tokens": EFFORT_TO_MAX_TOKENS.get(level, EFFORT_TO_MAX_TOKENS["medium"]),
        "extended_thinking": level == "max",
        "effort_level": level,
    }


# ---------------------------------------------------------------------------
# Permission Scope Enforcement (Phase 2D -- Runtime Evolution)
# ---------------------------------------------------------------------------


def check_permission_scope(
    builder_id: str, target_path: str, permission_scope: str | None
) -> tuple[bool, str]:
    """Check if a builder can access a given path based on its permission scope.

    Scopes:
        nucleus: only N0X/ of the builder's nucleus
        pillar: any N0X/ in the same pillar
        global: any path
        restricted: only archetypes/builders/{builder}/

    Returns:
        (allowed: bool, reason: str)
    """
    if not permission_scope or permission_scope == "global":
        return True, "global scope"

    target = target_path.replace("\\", "/").lower()

    if permission_scope == "restricted":
        allowed_prefix = f"archetypes/builders/{builder_id}/".lower()
        if target.startswith(allowed_prefix):
            return True, "within restricted scope"
        return False, f"restricted scope: only {allowed_prefix}"

    if permission_scope == "nucleus":
        # Derive nucleus from builder config or default to N03
        config = _load_builder_config(builder_id)
        nucleus_prefix = "n03_"  # default
        pillar = config.get("pillar", "")
        # Try to infer nucleus from pillar or builder convention
        if re.match(r"N\d{2}_", target):
            nucleus_prefix = target[:4].lower()
        if target.startswith(nucleus_prefix):
            return True, f"within nucleus scope ({nucleus_prefix})"
        return False, f"nucleus scope: only {nucleus_prefix}*"

    if permission_scope == "pillar":
        config = _load_builder_config(builder_id)
        pillar = config.get("pillar", "")
        if not pillar:
            return True, "no pillar constraint"
        # Allow any path within any nucleus for the same pillar
        # Also allow archetypes/builders/
        if target.startswith("archetypes/"):
            return True, "archetypes always accessible"
        return True, f"pillar scope ({pillar})"

    return True, "unknown scope, allowing"


# ---------------------------------------------------------------------------
# Tool Deny-List Enforcement (Phase 2B -- Runtime Evolution)
# ---------------------------------------------------------------------------


def check_tool_allowed(tool_name: str, denied_tools: list[str] | None) -> tuple[bool, str]:
    """Check if a tool is allowed for a builder.

    Returns:
        (allowed: bool, reason: str)
    """
    if not denied_tools:
        return True, "no deny list"

    tool_lower = tool_name.lower()
    for denied in denied_tools:
        if denied.lower() == tool_lower:
            return False, f"tool '{tool_name}' is in deny list"

    return True, "not in deny list"


def estimate_tokens(builder_id: str) -> int:
    """Estimate token cost for a builder execution."""
    if builder_id in META_BUILDERS:
        return 40000
    if builder_id in COMPLEX_BUILDERS:
        return 8000
    if builder_id in SIMPLE_BUILDERS:
        return 2000
    return 4000  # medium


# ---------------------------------------------------------------------------
# Step 1: PARSE -- extract verb, objects, domain, quality from intent
# ---------------------------------------------------------------------------


def parse_intent(intent: str, quality_override: float | None = None) -> dict:
    """Parse natural language intent into structured fields.

    Tries Python-first resolution via cex_intent_resolver (0 tokens)
    before falling back to local heuristic parsing.
    """
    text = intent.strip()
    if not text:
        return {
            "verb": "cria",
            "verb_action": "create",
            "objects": [],
            "domain": "generic",
            "quality": quality_override or 9.0,
            "multi_object": False,
            "error": "intent vazio",
        }

    # --- F1 CONSTRAIN: Python-first intent resolution (0 LLM tokens) ---
    try:
        from cex_intent_resolver import resolve_intent
        resolved = resolve_intent(text)
        if resolved and resolved.get("confidence", 0) >= 0.6 and resolved.get("kind"):
            kind = resolved["kind"]
            pillar = resolved["pillar"]
            nucleus = resolved["nucleus"]
            verb = resolved.get("verb", "create")
            quality = quality_override or 9.0

            # Build result matching expected parse_intent format
            if kind in OBJECT_TO_KINDS:
                objects = [kind]
            else:
                objects = [kind]

            return {
                "verb": verb,
                "verb_action": verb,
                "objects": objects,
                "domain": pillar,
                "quality": quality,
                "multi_object": False,
                "resolved_by": "cex_intent_resolver",
                "confidence": resolved["confidence"],
                "nucleus": nucleus,
            }
    except ImportError:
        pass  # resolver not available, fall through to heuristic
    except Exception:
        pass  # any error in resolver, fall through gracefully

    text_lower = text.lower()
    words = text_lower.split()

    # --- Verb ---
    verb = "cria"
    verb_action = "create"
    for w in words:
        clean = re.sub(r"[^a-z]", "", w)
        if clean in VERB_TABLE:
            verb = clean
            verb_action = VERB_TABLE[clean]
            break

    # --- Quality (decimal like 9.0, 9.5) ---
    quality = quality_override or 9.0
    qm = re.search(r"\b(\d+\.\d+)\b", text)
    if qm and not quality_override:
        q = float(qm.group(1))
        if 1.0 <= q <= 10.0:
            quality = q

    # --- Multi-object detection ---
    # Remove verb from text, then split by separators " e ", "+", ","
    rest = re.sub(r"(?i)\b" + re.escape(verb) + r"\b", "", text, count=1).strip()
    if qm:
        rest = rest.replace(qm.group(0), "").strip()

    segments = re.split(r"\s+(?:[eE]|[Aa][Nn][Dd])\s+|\s*\+\s*|\s*,\s*", rest)
    segments = [s.strip() for s in segments if s.strip()]

    # --- Objects ---
    objects = []
    for seg in segments:
        seg_words = [re.sub(r"[^a-z0-9_]", "", w) for w in seg.lower().split() if w]
        seg_words = [w for w in seg_words if w]  # remove empties
        found_in_seg = False

        # Priority 1: try trigram (3 adjacent words joined with _)
        for i in range(len(seg_words) - 2):
            trigram = f"{seg_words[i]}_{seg_words[i+1]}_{seg_words[i+2]}"
            if trigram in OBJECT_TO_KINDS and trigram not in objects:
                objects.append(trigram)
                found_in_seg = True
                break

        # Priority 2: try bigram (2 adjacent words joined with _)
        if not found_in_seg:
            for i in range(len(seg_words) - 1):
                bigram = f"{seg_words[i]}_{seg_words[i+1]}"
                if bigram in OBJECT_TO_KINDS and bigram not in objects:
                    objects.append(bigram)
                    found_in_seg = True
                    break

        # Priority 3: try hyphenated bigram (e.g. "few-shot" style)
        if not found_in_seg:
            for i in range(len(seg_words) - 1):
                hyphen = f"{seg_words[i]}-{seg_words[i+1]}"
                if hyphen in OBJECT_TO_KINDS and hyphen not in objects:
                    objects.append(hyphen)
                    found_in_seg = True
                    break

        # Priority 4: single word lookup (original behavior)
        if not found_in_seg:
            for sw in seg_words:
                if sw in OBJECT_TO_KINDS and sw not in objects:
                    objects.append(sw)
                    break

    # Check for builder name in intent (meta intent: "reconstroi X-builder")
    bm = re.search(r"([\w-]+-builder)\b", text_lower)
    if bm and bm.group(1) not in objects:
        objects.append(bm.group(1))

    # Fallback: scan all words with bigram priority
    if not objects:
        for i in range(len(words) - 1):
            w1 = re.sub(r"[^a-z0-9_]", "", words[i])
            w2 = re.sub(r"[^a-z0-9_]", "", words[i+1])
            bigram = f"{w1}_{w2}"
            if bigram in OBJECT_TO_KINDS:
                objects.append(bigram)
                break
        if not objects:
            for w in words:
                clean = re.sub(r"[^a-z_-]", "", w)
                if clean in OBJECT_TO_KINDS:
                    objects.append(clean)
                    break

    # Fallback: fuzzy match when no exact match found
    if not objects:
        for w in words:
            clean = re.sub(r"[^a-z0-9_-]", "", w)
            if clean in VERB_TABLE or len(clean) < 4:
                continue
            fuzzy_key = _fuzzy_match_object(clean)
            if fuzzy_key:
                objects.append(clean)
                break

    # --- Domain ---
    skip_words = (
        set(VERB_TABLE.keys())
        | set(OBJECT_TO_KINDS.keys())
        | {
            "o",
            "a",
            "os",
            "as",
            "um",
            "uma",
            "uns",
            "umas",
            "do",
            "da",
            "dos",
            "das",
            "no",
            "na",
            "nos",
            "nas",
            "com",
            "sem",
            "que",
            "por",
            "ao",
            "aos",
            "score",
        }
    )

    de_val = para_val = None
    de_m = re.search(r"\bde\s+(\w+)", text_lower)
    para_m = re.search(r"\bpara\s+(\w+)", text_lower)

    if de_m and de_m.group(1) not in skip_words:
        de_val = de_m.group(1)
    if para_m and para_m.group(1) not in skip_words:
        para_val = para_m.group(1)

    if de_val and para_val:
        domain = f"{de_val}/{para_val}"
    elif de_val:
        domain = de_val
    elif para_val:
        domain = para_val
    else:
        domain = "generic"

    return {
        "verb": verb,
        "verb_action": verb_action,
        "objects": objects,
        "domain": domain,
        "quality": quality,
        "multi_object": len(objects) > 1,
    }


# ---------------------------------------------------------------------------
# Step 2: CLASSIFY -- map objects to CEX kinds
# ---------------------------------------------------------------------------


def _fuzzy_match_object(word: str, threshold: float = 0.8) -> str | None:
    """Find closest OBJECT_TO_KINDS key using difflib sequence matching.

    Returns the best matching key or None if no match above threshold.
    Only attempts fuzzy match for words with length >= 4.
    """
    if len(word) < 4:
        return None
    matches = difflib.get_close_matches(word, OBJECT_TO_KINDS.keys(), n=1, cutoff=threshold)
    return matches[0] if matches else None


def classify_objects(objects: list[str]) -> list[dict]:
    """Map object keywords to CEX kinds using taxonomy table.

    Resolution chain: exact match -> fuzzy match -> cex_query TF-IDF -> generic.
    Each result includes a confidence field:
      1.0 = exact match on kind name or synonym
      0.8 = fuzzy match (typo correction via difflib)
      0.7 = TF-IDF match (via cex_query.py)
      0.0 = no match (generic fallback)
    """
    classified = []
    seen_kinds = set()

    for obj in objects:
        # Meta intent: object is a builder name
        if obj.endswith("-builder"):
            classified.append(
                {
                    "object": obj,
                    "kind": "type_builder",
                    "pillar": "P02",
                    "primary_function": "BECOME",
                    "confidence": 1.0,
                    "match_type": "exact",
                    "meta": True,
                }
            )
            continue

        # --- Layer 1: Exact match ---
        kinds = OBJECT_TO_KINDS.get(obj, [])
        if kinds:
            for kind, pillar, primary_fn in kinds:
                if kind not in seen_kinds:
                    classified.append(
                        {
                            "object": obj,
                            "kind": kind,
                            "pillar": pillar,
                            "primary_function": primary_fn,
                            "confidence": 1.0,
                            "match_type": "exact",
                        }
                    )
                    seen_kinds.add(kind)
            continue

        # --- Layer 2: Fuzzy match (typo resilience) ---
        fuzzy_key = _fuzzy_match_object(obj)
        if fuzzy_key:
            kinds = OBJECT_TO_KINDS[fuzzy_key]
            for kind, pillar, primary_fn in kinds:
                if kind not in seen_kinds:
                    classified.append(
                        {
                            "object": obj,
                            "kind": kind,
                            "pillar": pillar,
                            "primary_function": primary_fn,
                            "confidence": 0.8,
                            "match_type": "fuzzy",
                            "matched_key": fuzzy_key,
                        }
                    )
                    seen_kinds.add(kind)
            continue

    # --- Layer 3: cex_query.py TF-IDF fallback ---
    if not classified:
        try:
            from cex_query import query_builders
            query_text = " ".join(objects)
            hits = query_builders(query_text, top_k=3)
            for hit in hits:
                kind = hit.get("kind", "")
                score = hit.get("score", 0)
                if kind and kind not in seen_kinds and score > 1.5:
                    classified.append(
                        {
                            "object": hit.get("builder_id", kind),
                            "kind": kind,
                            "pillar": hit.get("pillar", "P01"),
                            "primary_function": "BECOME",
                            "confidence": 0.7,
                            "match_type": "tfid",
                            "tfidf_score": score,
                        }
                    )
                    seen_kinds.add(kind)
        except ImportError:
            pass

    # --- Layer 4: Generic fallback ---
    if not classified:
        classified.append(
            {
                "object": "generic",
                "kind": "generic",
                "pillar": "P01",
                "primary_function": "BECOME",
                "confidence": 0.0,
                "match_type": "none",
            }
        )

    return classified


# ---------------------------------------------------------------------------
# KC Library -- load domain KCs and match by feeds_kinds
# ---------------------------------------------------------------------------


def load_kc_library() -> list[dict]:
    """Load KC frontmatter from library/kind/*.md (dedicated) + library/domain/*.md (cluster)."""
    kcs = []
    # Priority 1: dedicated kind KCs
    if KC_KIND_PATH.exists():
        for md in sorted(KC_KIND_PATH.glob("kc_*.md")):
            try:
                text = md.read_text(encoding="utf-8")
                parts = text.split("---")
                if len(parts) >= 3:
                    fm = yaml.safe_load(parts[1])
                    if fm:
                        fm["_path"] = str(md.relative_to(md.parent.parent.parent.parent))
                        fm["_type"] = "kind"
                        kcs.append(fm)
            except Exception:
                pass
    # Priority 2: cluster domain KCs (reference dir or domain dir)
    domain_search = KC_DOMAIN_PATH
    ref_dir = KC_DOMAIN_PATH / "_reference"
    if ref_dir.exists():
        domain_search = ref_dir
    if not domain_search.exists():
        return kcs
    for md in sorted(domain_search.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        if text.startswith("---"):
            end = text.find("---", 3)
            if end > 0:
                try:
                    fm = yaml.safe_load(text[3:end])
                    if isinstance(fm, dict):
                        fm["_path"] = str(md.relative_to(CEX_ROOT))
                        kcs.append(fm)
                except yaml.YAMLError:
                    pass
    return kcs


def lookup_kcs_for_kind(kc_library: list[dict], kind: str, pillar: str) -> list[dict]:
    """Find KC-Domains whose feeds_kinds match the target kind or pillar."""
    matches = []
    for kc in kc_library:
        feeds = kc.get("feeds_kinds", [])
        if not isinstance(feeds, list):
            continue
        if kind in feeds or pillar in feeds or any(f.startswith(pillar + "_") for f in feeds):
            matches.append({"id": kc.get("id"), "title": kc.get("title"), "path": kc.get("_path"), "type": kc.get("_type", "domain")})
    # Sort: kind KCs first, then domain clusters
    matches.sort(key=lambda m: (0 if m.get("type") == "kind" else 1, m.get("id", "")))
    return matches


def rebuild_kc_index():
    """Scan domain/*.md frontmatter, rebuild index.yaml domains + coverage."""
    kcs = load_kc_library()
    if not KC_INDEX_PATH.exists():
        return
    with open(KC_INDEX_PATH, "r", encoding="utf-8") as f:
        index = yaml.safe_load(f) or {}
    domains = {}
    coverage = {}
    for kc in kcs:
        kc_id = kc.get("id", "unknown")
        domains[kc_id] = {
            "path": kc.get("_path", ""),
            "title": kc.get("title", ""),
            "feeds_kinds": kc.get("feeds_kinds", []),
            "origin": kc.get("origin", ""),
        }
        for fk in kc.get("feeds_kinds", []):
            coverage.setdefault(fk, []).append(kc_id)
    index["domains"] = domains
    index["coverage"] = coverage
    with open(KC_INDEX_PATH, "w", encoding="utf-8") as f:
        yaml.dump(index, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


# ---------------------------------------------------------------------------
# Step 3: FAN-OUT -- select builders per function
# ---------------------------------------------------------------------------


def load_builder_map() -> dict:
    """Load 8F_BUILDER_MAP.yaml."""
    if not BUILDER_MAP_PATH.exists():
        print(f"ERROR: Builder map not found: {BUILDER_MAP_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(BUILDER_MAP_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _has_keyword(intent_lower: str, keywords: list[str]) -> bool:
    """Check if intent contains any of the keywords (case-insensitive)."""
    return any(kw.lower() in intent_lower for kw in keywords)


def _load_builder_config(builder_id: str) -> dict:
    """Load bld_config frontmatter for a builder. Returns empty dict on failure."""
    config_dir = CEX_ROOT / "archetypes" / "builders" / builder_id
    if not config_dir.exists():
        return {}
    kind_slug = builder_id.replace("-builder", "")
    config_file = config_dir / f"bld_config_{kind_slug}.md"
    if not config_file.exists():
        # Try any bld_config file
        configs = list(config_dir.glob("bld_config_*.md"))
        if not configs:
            return {}
        config_file = configs[0]
    try:
        content = config_file.read_text(encoding="utf-8")
        parts = content.split("---")
        fm = yaml.safe_load(parts[1]) if len(parts) >= 3 else {}
        return fm if isinstance(fm, dict) else {}
    except Exception:
        return {}


def _load_builder_tools_denied(builder_id: str) -> set:
    """Load denied tools from bld_tools file's Tool Permissions DENIED section."""
    tools_dir = CEX_ROOT / "archetypes" / "builders" / builder_id
    if not tools_dir.exists():
        return set()
    kind_slug = builder_id.replace("-builder", "")
    tools_file = tools_dir / f"bld_tools_{kind_slug}.md"
    if not tools_file.exists():
        tools_files = list(tools_dir.glob("bld_tools_*.md"))
        if not tools_files:
            return set()
        tools_file = tools_files[0]
    try:
        content = tools_file.read_text(encoding="utf-8")
        # Find DENIED row in Tool Permissions table
        match = re.search(r'\|\s*DENIED\s*\|\s*([^|]+)\s*\|', content)
        if match:
            denied_text = match.group(1).strip()
            if denied_text.lower() in ("(none)", "none", "--", "-", ""):
                return set()
            return {t.strip() for t in denied_text.split(",") if t.strip()}
    except Exception:
        pass
    return set()


def _inject_builder_memories(intent: str, builder_id: str) -> dict | None:
    """Retrieve relevant memories for a builder. Returns injection dict or None."""
    global _memory_select, _memory_scanner
    try:
        if _memory_select is None:
            from cex_memory_select import select_relevant_memories
            _memory_select = select_relevant_memories
        if _memory_scanner is None:
            from cex_memory import scan_builder_memories
            _memory_scanner = scan_builder_memories

        headers = _memory_scanner(builder_id)
        if not headers:
            return None

        selected = _memory_select(
            query=intent,
            memories=headers,
            builder_id=builder_id,
            top_k=5,
            use_cache=True,
        )
        if not selected:
            return None

        return {
            "builder_id": builder_id,
            "total_observations": len(headers),
            "selected_count": len(selected),
            "memories": [
                {"path": m.path, "type": m.type, "confidence": m.confidence}
                for m in selected
            ],
        }
    except Exception:
        return None


def fan_out(
    classified: list[dict],
    intent_lower: str,
    quality: float,
    builder_map: dict,
    verb_action: str,
    kc_library: list[dict] | None = None,
) -> list[dict]:
    """For each of the 8 functions, select which builders are active."""

    # Group flat builder map entries by llm_function
    by_function: dict[str, list[dict]] = {}
    for kind_name, info in builder_map.items():
        if not isinstance(info, dict) or "llm_function" not in info:
            continue
        fn = info["llm_function"]
        builder_id = Path(info.get("builder", "")).name or f"{kind_name}-builder"
        by_function.setdefault(fn, []).append(
            {
                "kind": kind_name,
                "id": builder_id,
                "core": info.get("core", False),
                "pillar": info.get("pillar", ""),
            }
        )

    verb_extras = VERB_EXTRA_BUILDERS.get(verb_action, set())
    is_meta = any(c.get("meta") for c in classified)
    classified_kinds = {c["kind"] for c in classified}
    classified_pillars = {c["pillar"] for c in classified}

    result = []

    for fn_name, position in FUNCTION_POSITIONS.items():
        fn_builders = by_function.get(fn_name, [])
        builders = []

        for b in fn_builders:
            bid = b["id"]
            active = False
            tier = "primary" if b["core"] else "secondary"
            reason = "not relevant to intent"

            # Core builders: active if kind or pillar matches classified
            if b["core"]:
                if b["kind"] in classified_kinds:
                    active = True
                    reason = "core builder for classified kind"
                elif b["pillar"].split("_")[0] in classified_pillars:
                    active = True
                    reason = "core builder for classified pillar"
                elif quality >= 9.5:
                    active = True
                    tier = "optional"
                    reason = "quality target >= 9.5"
            else:
                # Non-core: keyword match in intent
                kw = b["kind"].replace("_", " ")
                if kw in intent_lower:
                    active = True
                    reason = "keyword match in intent"

            # Keyword gate for specific builders
            if bid in PRIMARY_NEEDS_KEYWORD:
                if not _has_keyword(intent_lower, PRIMARY_NEEDS_KEYWORD[bid]):
                    active = False
                    reason = "not mentioned in intent"

            # Force-activate verb extras
            if bid in verb_extras:
                active = True
                reason = f"activated by verb '{verb_action}'"

            # Meta intent
            if is_meta and bid == "_builder-builder":
                active = True
                reason = "meta intent -- building a builder"

            builders.append({"id": bid, "tier": tier, "active": active, "reason": reason})

        # Synthetic _builder-builder for meta intents
        if is_meta and fn_name == "BECOME":
            builders.append(
                {
                    "id": "_builder-builder",
                    "tier": "optional",
                    "active": True,
                    "reason": "meta intent -- building a builder",
                }
            )

        # Dependencies (all functions at lower positions)
        deps = sorted(
            [fn for fn, pos in FUNCTION_POSITIONS.items() if pos < position],
            key=lambda d: FUNCTION_POSITIONS[d],
        )

        # Enrich active builders with config + memory (Runtime Evolution)
        active_list = [b for b in builders if b["active"]]
        for b in active_list:
            bid = b["id"]
            # Load builder config (effort, hooks, permissions, etc.)
            config = _load_builder_config(bid)
            if config:
                effort = config.get("effort", "medium")
                b["effort"] = effort
                b["max_turns"] = config.get("max_turns")
                b["permission_scope"] = config.get("permission_scope")
                b["fork_context"] = config.get("fork_context")
                b["hooks"] = config.get("hooks")
                # Resolve effort -> model mapping
                effort_info = resolve_effort_model(effort)
                b["model"] = effort_info["model"]
                b["model_max_tokens"] = effort_info["max_tokens"]
                b["extended_thinking"] = effort_info["extended_thinking"]
                # Merge deny lists
                config_denied = set(config.get("disallowed_tools") or [])
                tools_denied = _load_builder_tools_denied(bid)
                deny_set = config_denied | tools_denied
                if deny_set:
                    b["denied_tools"] = sorted(deny_set)

        est_tokens = int(sum(estimate_tokens(b["id"]) for b in active_list) * 1.2)

        entry = {
            "name": fn_name,
            "position": position,
            "builders": builders,
            "deps": deps,
            "parallel": True,
            "estimated_tokens": est_tokens,
        }

        # Memory injection for BECOME function (1x per builder load)
        if fn_name == "BECOME":
            memory_injections = []
            for b in active_list:
                mem = _inject_builder_memories(intent_lower, b["id"])
                if mem:
                    memory_injections.append(mem)
            if memory_injections:
                entry["memory_injections"] = memory_injections

        # KC Library injection for INJECT function
        if fn_name == "INJECT" and kc_library:
            kc_matches = []
            for c in classified:
                kc_matches.extend(lookup_kcs_for_kind(kc_library, c["kind"], c["pillar"]))
            seen_ids = set()
            unique = []
            for m in kc_matches:
                if m["id"] not in seen_ids:
                    seen_ids.add(m["id"])
                    unique.append(m)
            entry["kc_injections"] = unique if unique else None
            if not unique:
                entry["kc_fallback"] = "bld_knowledge"

        result.append(entry)

    return result


# ---------------------------------------------------------------------------
# Step 4: PLAN -- order functions by pipeline position
# ---------------------------------------------------------------------------


def order_plan(functions: list[dict]) -> list[dict]:
    """Sort functions by their pipeline position (1..8)."""
    return sorted(functions, key=lambda f: f["position"])


# ---------------------------------------------------------------------------
# Step 5: OUTPUT -- assemble final JSON
# ---------------------------------------------------------------------------


def generate_output(
    intent: str, parsed: dict, classified: list[dict], functions: list[dict]
) -> dict:
    """Produce the complete execution plan JSON."""

    ordered = order_plan(functions)

    total_active = sum(1 for fn in ordered for b in fn["builders"] if b["active"])
    total_tokens = sum(fn["estimated_tokens"] for fn in ordered)

    warnings = []

    if parsed["multi_object"]:
        total_tokens = int(total_tokens * 1.6)
        warnings.append("multi_object: complexidade aumenta 60%. Considere splits em 2 plans.")

    if parsed["domain"] == "generic":
        warnings.append(
            "domain not identified -- plan may be generic. Specify target artifact."
        )

    if any(c.get("meta") for c in classified):
        warnings.append("intent meta detectado -- ativando _builder-builder. Pipeline de 13 files.")

    # Parsed output (spec format: object is string or array)
    parsed_output = {
        "verb": parsed["verb"],
        "object": (
            parsed["objects"]
            if parsed["multi_object"]
            else (parsed["objects"][0] if parsed["objects"] else "generic")
        ),
        "domain": parsed["domain"],
        "quality": parsed["quality"],
        "multi_object": parsed["multi_object"],
    }

    # Register turn budgets for all active builders
    turn_budgets = {}
    for fn in ordered:
        for b in fn["builders"]:
            if b["active"]:
                mt = b.get("max_turns") or 25
                turn_counter.register(b["id"], mt)
                turn_budgets[b["id"]] = mt

    return {
        "intent": intent,
        "parsed": parsed_output,
        "classified_kinds": [{k: v for k, v in c.items() if k not in ("meta",)} for c in classified],
        "functions": ordered,
        "total_builders": total_active,
        "estimated_tokens": total_tokens,
        "turn_budgets": turn_budgets,
        "warnings": warnings,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Motor 8F -- Intent -> Execution Plan (CEX)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cex_8f_motor.py --intent "cria agente de vendas para ML"
  python cex_8f_motor.py --intent "reconstroi signal-builder" --quality 9.5
  python cex_8f_motor.py --intent "create agent AND research workflow"
  python cex_8f_motor.py --test
        """,
    )
    parser.add_argument("--intent", help="Natural language intent string")
    parser.add_argument("--dry-run", dest="dry_run", help="Alias for --intent (parse only, no execution)")
    parser.add_argument("--quality", type=float, help="Quality target override")
    parser.add_argument("--output", help="Output file (default: stdout)")
    parser.add_argument("--compact", action="store_true", help="Compact JSON")
    parser.add_argument("--test", action="store_true", help="Run inline tests")

    args = parser.parse_args()

    if args.test:
        run_tests()
        return

    # --dry-run is alias for --intent
    if args.dry_run and not args.intent:
        args.intent = args.dry_run

    if not args.intent:
        parser.error("--intent is required (or use --test or --dry-run)")

    builder_map = load_builder_map()
    kc_library = load_kc_library()
    rebuild_kc_index()

    parsed = parse_intent(args.intent, args.quality)
    if parsed.get("error"):
        print(json.dumps({"error": parsed["error"]}, ensure_ascii=False, indent=2))
        sys.exit(1)

    classified = classify_objects(parsed["objects"])
    functions = fan_out(
        classified,
        args.intent.lower(),
        parsed["quality"],
        builder_map,
        parsed["verb_action"],
        kc_library=kc_library,
    )
    result = generate_output(args.intent, parsed, classified, functions)

    indent = None if args.compact else 2
    output_json = json.dumps(result, ensure_ascii=False, indent=indent)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output_json, encoding="utf-8")
        print(
            f"Plan saved: {out_path} "
            f"({result['total_builders']} builders, "
            f"~{result['estimated_tokens']:,} tokens)",
            file=sys.stderr,
        )
    else:
        print(output_json)


# ---------------------------------------------------------------------------
# Inline Tests
# ---------------------------------------------------------------------------


def run_tests():
    """Run Motor 8F self-tests."""
    builder_map = load_builder_map()
    passed = failed = 0

    def check(name: str, condition: bool, detail: str = ""):
        nonlocal passed, failed
        if condition:
            print(f"  PASS: {name}")
            passed += 1
        else:
            print(f"  FAIL: {name} -- {detail}")
            failed += 1

    # Test 1: basic agent creation
    print("\nTest 1: cria agente de vendas para ML")
    p1 = parse_intent("cria agente de vendas para ML")
    check("verb=cria", p1["verb"] == "cria", f"got {p1['verb']}")
    check("object=agente", "agente" in p1["objects"], f"got {p1['objects']}")
    check("multi_object=false", not p1["multi_object"])
    check("domain has vendas", "vendas" in p1["domain"], f"got {p1['domain']}")

    c1 = classify_objects(p1["objects"])
    check("kind=agent", any(c["kind"] == "agent" for c in c1), f"got {c1}")

    f1 = fan_out(c1, "cria agente de vendas para ml", 9.0, builder_map, "create")
    become = next((f for f in f1 if f["name"] == "BECOME"), None)
    check("BECOME exists", become is not None)
    if become:
        ab = next((b for b in become["builders"] if b["id"] == "agent-builder"), None)
        check("agent-builder active in BECOME", ab is not None and ab["active"], f"got {ab}")

    # Test 2: meta intent (rebuild a builder)
    print("\nTest 2: reconstroi signal-builder")
    p2 = parse_intent("reconstroi signal-builder")
    check("verb=reconstroi", p2["verb"] == "reconstroi", f"got {p2['verb']}")
    check("signal-builder in objects", "signal-builder" in p2["objects"], f"got {p2['objects']}")

    c2 = classify_objects(p2["objects"])
    check("meta kind", any(c.get("meta") or c["kind"] == "type_builder" for c in c2))

    f2 = fan_out(c2, "reconstroi signal-builder", 9.0, builder_map, "rebuild")
    become2 = next((f for f in f2 if f["name"] == "BECOME"), None)
    if become2:
        bb = next((b for b in become2["builders"] if b["id"] == "_builder-builder"), None)
        check("_builder-builder active", bb is not None and bb["active"], f"got {bb}")

    # Test 3: multi-object
    print("\nTest 3: create agent AND research workflow")
    p3 = parse_intent("create agent AND research workflow")
    check("multi_object=true", p3["multi_object"], f"got {p3['multi_object']}")
    check("has agent", "agent" in p3["objects"], f"got {p3['objects']}")
    check("has workflow", "workflow" in p3["objects"], f"got {p3['objects']}")
    check("verb=create", p3["verb"] == "create", f"got {p3['verb']}")

    # Test 4: empty intent
    print("\nTest 4: intent vazio")
    p4 = parse_intent("")
    check("has error", "error" in p4)

    # Test 5: quality override
    print("\nTest 5: quality override")
    p5 = parse_intent("cria agente", quality_override=9.5)
    check("quality=9.5", p5["quality"] == 9.5, f"got {p5['quality']}")

    f5 = fan_out(classify_objects(p5["objects"]), "cria agente", 9.5, builder_map, "create")
    # Optional builders should activate at 9.5
    all_optional = [
        b for fn in f5 for b in fn["builders"] if b["tier"] == "optional" and b["active"]
    ]
    check("optional builders active at 9.5", len(all_optional) > 0, f"found {len(all_optional)}")

    # Test 6: full pipeline output
    print("\nTest 6: full pipeline structure")
    full = generate_output("cria agente de vendas", p1, c1, f1)
    check("has 8 functions", len(full["functions"]) == 8, f"got {len(full['functions'])}")
    check("total_builders > 0", full["total_builders"] > 0)
    check("estimated_tokens > 0", full["estimated_tokens"] > 0)
    positions = [f["position"] for f in full["functions"]]
    check("ordered by position", positions == sorted(positions), f"got {positions}")

    # Test 7: KC library integration
    print("\nTest 7: KC library integration")
    kc_lib = load_kc_library()
    check("kc_library loads", isinstance(kc_lib, list))
    if kc_lib:
        check("kc has feeds_kinds", "feeds_kinds" in kc_lib[0], f"keys: {list(kc_lib[0].keys())}")
        matches = lookup_kcs_for_kind(kc_lib, "knowledge_card", "P01")
        check("lookup finds matches", len(matches) > 0, f"found {len(matches)}")
    f7 = fan_out(c1, "cria agente de vendas para ml", 9.0, builder_map, "create", kc_library=kc_lib)
    inject_fn = next((f for f in f7 if f["name"] == "INJECT"), None)
    check(
        "INJECT has kc field",
        inject_fn is not None and ("kc_injections" in inject_fn or "kc_fallback" in inject_fn),
    )

    # Summary
    print(f"\n{'=' * 40}")
    print(f"Results: {passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
