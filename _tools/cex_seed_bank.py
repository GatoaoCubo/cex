import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")
#!/usr/bin/env python3
"""
cex_seed_bank.py — Banco de Seeds por Tipo CEX
Para cada um dos 69 tipos, gera 10-20 seed words relevantes.

Le TYPE_TO_TEMPLATE.yaml + _schema.yaml de cada LP.
Gera _meta/SEED_BANK.yaml

Uso:
  python cex_seed_bank.py              # gera SEED_BANK.yaml
  python cex_seed_bank.py --dry-run    # preview sem salvar
  python cex_seed_bank.py --lp P01    # apenas seeds de P01
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERRO: PyYAML necessario. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

CEX_ROOT = Path(__file__).resolve().parent.parent
META_DIR = CEX_ROOT / "_meta"
OUTPUT_PATH = META_DIR / "SEED_BANK.yaml"

LP_DIRS = {
    "P01": "P01_knowledge",
    "P02": "P02_model",
    "P03": "P03_prompt",
    "P04": "P04_tools",
    "P05": "P05_output",
    "P06": "P06_schema",
    "P07": "P07_evals",
    "P08": "P08_architecture",
    "P09": "P09_config",
    "P10": "P10_memory",
    "P11": "P11_feedback",
    "P12": "P12_orchestration",
}

# Seeds derivadas da analise dos schemas, templates e dominio de cada tipo.
# Cada entrada: seeds (palavras-chave para gerar conteudo) +
#               contexts (situacoes de uso do tipo)
SEED_BANK = {
    # ── P01 Knowledge ──
    "P01_knowledge_card": {
        "seeds": [
            "domain",
            "expertise",
            "axioms",
            "patterns",
            "when_to_use",
            "density",
            "tldr",
            "linked",
            "bullets",
            "quick_reference",
            "conceitos",
            "fases",
            "regras_de_ouro",
            "comparativo",
            "flow",
        ],
        "contexts": ["research", "distillation", "documentation", "analysis"],
    },
    "P01_rag_source": {
        "seeds": [
            "url",
            "domain",
            "freshness",
            "indexable",
            "crawl",
            "last_checked",
            "reliability",
            "format",
            "extraction",
            "metadata",
        ],
        "contexts": ["ingestion", "indexing", "refresh", "validation"],
    },
    "P01_glossary_entry": {
        "seeds": [
            "term",
            "definition",
            "synonyms",
            "context",
            "disambiguation",
            "domain_specific",
            "abbreviation",
            "usage",
            "related_terms",
            "etymology",
        ],
        "contexts": ["onboarding", "documentation", "standardization", "reference"],
    },
    "P01_context_doc": {
        "seeds": [
            "domain",
            "scope",
            "background",
            "stakeholders",
            "constraints",
            "assumptions",
            "dependencies",
            "timeline",
            "objectives",
            "boundaries",
        ],
        "contexts": ["project_setup", "handoff", "onboarding", "planning"],
    },
    "P01_embedding_config": {
        "seeds": [
            "model_name",
            "dimensions",
            "chunk_size",
            "overlap",
            "tokenizer",
            "distance_metric",
            "batch_size",
            "normalize",
            "provider",
            "cost",
        ],
        "contexts": ["setup", "optimization", "migration", "benchmarking"],
    },
    "P01_few_shot_example": {
        "seeds": [
            "input",
            "output",
            "quality",
            "edge_case",
            "format",
            "domain",
            "difficulty",
            "explanation",
            "variation",
            "expected_behavior",
        ],
        "contexts": ["prompt_engineering", "evaluation", "training", "calibration"],
    },
    # ── P02 Model ──
    "P02_agent": {
        "seeds": [
            "identity",
            "capabilities",
            "constraints",
            "tools",
            "routing",
            "fallback",
            "boot",
            "satellite",
            "domain",
            "architecture",
            "when_to_use",
            "input_output",
            "integration",
            "quality_gates",
            "overview",
        ],
        "contexts": ["creation", "modification", "audit", "deployment"],
    },
    "P02_lens": {
        "seeds": [
            "perspective",
            "domain",
            "applies_to",
            "bias",
            "focus",
            "filters",
            "interpretation",
            "weight",
            "priority",
            "scope",
        ],
        "contexts": ["analysis", "routing", "specialization", "context_switching"],
    },
    "P02_boot_config": {
        "seeds": [
            "provider",
            "identity",
            "constraints",
            "tools",
            "flags",
            "model",
            "temperature",
            "system_prompt",
            "mcp_config",
            "permissions",
        ],
        "contexts": ["initialization", "provider_switch", "debugging", "optimization"],
    },
    "P02_mental_model": {
        "seeds": [
            "agent",
            "routing_rules",
            "decision_tree",
            "priorities",
            "heuristics",
            "domain_map",
            "tools_available",
            "personality",
            "constraints",
            "fallback",
        ],
        "contexts": ["agent_design", "debugging", "optimization", "documentation"],
    },
    "P02_model_card": {
        "seeds": [
            "model_name",
            "provider",
            "context_window",
            "pricing",
            "capabilities",
            "limitations",
            "benchmarks",
            "latency",
            "modalities",
            "version",
            "training_cutoff",
            "safety",
            "rate_limits",
            "tokens_per_second",
        ],
        "contexts": ["selection", "comparison", "budgeting", "migration"],
    },
    "P02_router": {
        "seeds": [
            "routes",
            "fallback",
            "keywords",
            "satellite",
            "priority",
            "confidence_threshold",
            "load_balance",
            "timeout",
            "retry",
            "escalation",
        ],
        "contexts": ["dispatch", "optimization", "debugging", "scaling"],
    },
    "P02_fallback_chain": {
        "seeds": [
            "chain",
            "timeout_per_step",
            "models",
            "degradation",
            "cost",
            "quality_threshold",
            "retry_count",
            "circuit_breaker",
            "logging",
            "alert",
        ],
        "contexts": ["resilience", "cost_optimization", "debugging", "design"],
    },
    "P02_iso_package": {
        "seeds": [
            "manifest",
            "system_instruction",
            "instructions",
            "architecture",
            "examples",
            "error_handling",
            "upload_kit",
            "portable",
            "self_contained",
            "whitelabel",
            "tiers",
            "density",
            "quality_gates",
        ],
        "contexts": ["packaging", "deployment", "sharing", "audit"],
    },
    # ── P03 Prompt ──
    "P03_system_prompt": {
        "seeds": [
            "identity",
            "rules",
            "output_format",
            "persona",
            "constraints",
            "tone",
            "knowledge_boundary",
            "safety",
            "tools_available",
            "response_structure",
            "examples",
            "anti_patterns",
        ],
        "contexts": ["agent_creation", "tuning", "A/B_testing", "compliance"],
    },
    "P03_action_prompt": {
        "seeds": [
            "action",
            "input_required",
            "output_expected",
            "steps",
            "validation",
            "purpose",
            "constraints",
            "examples",
            "edge_cases",
            "timeout",
        ],
        "contexts": ["task_execution", "automation", "testing", "optimization"],
    },
    "P03_prompt_template": {
        "seeds": [
            "variables",
            "purpose",
            "quality_gates",
            "examples",
            "semantic_bridge",
            "template_body",
            "mustache",
            "reuse",
            "composability",
            "versioning",
            "input_types",
            "output_format",
        ],
        "contexts": ["authoring", "standardization", "reuse", "evolution"],
    },
    "P03_instruction": {
        "seeds": [
            "target",
            "steps",
            "prerequisites",
            "validation",
            "rollback",
            "order",
            "dependencies",
            "idempotent",
            "atomic",
            "logging",
        ],
        "contexts": ["execution", "onboarding", "automation", "documentation"],
    },
    "P03_chain": {
        "seeds": [
            "steps",
            "flow",
            "input_output",
            "branching",
            "parallel",
            "sequential",
            "error_handling",
            "state",
            "context_passing",
            "termination",
        ],
        "contexts": ["pipeline_design", "optimization", "debugging", "composition"],
    },
    # ── P04 Tools ──
    "P04_skill": {
        "seeds": [
            "name",
            "trigger",
            "phases",
            "when_to_use",
            "when_not_to_use",
            "examples",
            "anti_patterns",
            "metrics",
            "workflow",
            "input_output",
            "user_invocable",
            "dependencies",
        ],
        "contexts": ["creation", "discovery", "execution", "audit"],
    },
    "P04_mcp_server": {
        "seeds": [
            "name",
            "transport",
            "tools_provided",
            "resources_provided",
            "auth",
            "stdio",
            "sse",
            "http",
            "schema",
            "rate_limit",
            "health_check",
            "versioning",
        ],
        "contexts": ["integration", "deployment", "debugging", "documentation"],
    },
    "P04_hook": {
        "seeds": [
            "trigger_event",
            "script_path",
            "pre_post",
            "timeout",
            "blocking",
            "async",
            "error_handling",
            "lifecycle",
            "conditions",
            "logging",
        ],
        "contexts": ["automation", "quality_gates", "monitoring", "customization"],
    },
    "P04_plugin": {
        "seeds": [
            "interface",
            "lifecycle",
            "config",
            "dependencies",
            "isolation",
            "version",
            "enable_disable",
            "hot_reload",
            "api_surface",
            "testing",
        ],
        "contexts": ["extension", "customization", "marketplace", "development"],
    },
    "P04_client": {
        "seeds": [
            "api",
            "auth",
            "endpoints",
            "rate_limit",
            "retry",
            "timeout",
            "serialization",
            "error_codes",
            "pagination",
            "caching",
        ],
        "contexts": ["integration", "testing", "migration", "documentation"],
    },
    "P04_cli_tool": {
        "seeds": [
            "commands",
            "flags",
            "args",
            "help",
            "output_format",
            "exit_codes",
            "config_file",
            "verbose",
            "interactive",
            "scripting",
        ],
        "contexts": ["development", "automation", "documentation", "testing"],
    },
    "P04_scraper": {
        "seeds": [
            "target",
            "selectors",
            "pagination",
            "rate_limit",
            "anti_bot",
            "proxy",
            "output_format",
            "scheduling",
            "validation",
            "freshness",
        ],
        "contexts": ["data_collection", "monitoring", "research", "enrichment"],
    },
    "P04_connector": {
        "seeds": [
            "service",
            "auth",
            "protocol",
            "endpoints",
            "mapping",
            "transform",
            "retry",
            "health_check",
            "logging",
            "versioning",
        ],
        "contexts": ["integration", "migration", "monitoring", "debugging"],
    },
    "P04_daemon": {
        "seeds": [
            "name",
            "schedule",
            "health_check",
            "restart_policy",
            "logging",
            "pid_file",
            "signal_handling",
            "resource_limits",
            "monitoring",
            "graceful_shutdown",
        ],
        "contexts": ["deployment", "monitoring", "debugging", "scaling"],
    },
    # ── P05 Output ──
    "P05_output_schema": {
        "seeds": [
            "format",
            "fields",
            "types",
            "required",
            "optional",
            "validation",
            "examples",
            "versioning",
            "serialization",
            "compatibility",
        ],
        "contexts": ["design", "validation", "documentation", "evolution"],
    },
    "P05_parser": {
        "seeds": [
            "target",
            "input_format",
            "extraction",
            "regex",
            "structured",
            "error_handling",
            "fallback",
            "streaming",
            "chunking",
            "normalization",
        ],
        "contexts": ["ingestion", "transformation", "debugging", "optimization"],
    },
    "P05_formatter": {
        "seeds": [
            "format",
            "template",
            "escaping",
            "encoding",
            "pretty_print",
            "minify",
            "custom_rules",
            "locale",
            "truncation",
            "streaming",
        ],
        "contexts": ["output", "display", "export", "standardization"],
    },
    "P05_naming_rule": {
        "seeds": [
            "scope",
            "pattern",
            "prefix",
            "suffix",
            "separator",
            "case_style",
            "versioning",
            "collision",
            "validation",
            "examples",
        ],
        "contexts": ["standardization", "migration", "audit", "onboarding"],
    },
    # ── P06 Schema ──
    "P06_input_schema": {
        "seeds": [
            "scope",
            "fields",
            "types",
            "required",
            "defaults",
            "validation",
            "coercion",
            "examples",
            "error_messages",
            "versioning",
        ],
        "contexts": ["contract_design", "validation", "documentation", "testing"],
    },
    "P06_type_def": {
        "seeds": [
            "type",
            "base",
            "constraints",
            "serialization",
            "examples",
            "composition",
            "inheritance",
            "generics",
            "nullable",
            "documentation",
        ],
        "contexts": ["design", "reuse", "standardization", "migration"],
    },
    "P06_validator": {
        "seeds": [
            "rule",
            "conditions",
            "error_message",
            "severity",
            "auto_fix",
            "pre_commit",
            "quality_gate",
            "threshold",
            "bypass",
            "logging",
        ],
        "contexts": ["quality_assurance", "automation", "compliance", "debugging"],
    },
    "P06_interface": {
        "seeds": [
            "contract",
            "methods",
            "input",
            "output",
            "versioning",
            "backward_compatible",
            "deprecation",
            "documentation",
            "testing",
            "mock",
        ],
        "contexts": ["integration", "design", "evolution", "testing"],
    },
    "P06_output_schema": {
        "seeds": [
            "scope",
            "format",
            "fields",
            "types",
            "required",
            "validation",
            "examples",
            "compatibility",
            "streaming",
            "pagination",
        ],
        "contexts": ["contract_design", "validation", "documentation", "evolution"],
    },
    # ── P07 Evals ──
    "P07_unit_eval": {
        "seeds": [
            "target",
            "input",
            "expected_output",
            "assertion",
            "score",
            "timeout",
            "setup",
            "teardown",
            "edge_cases",
            "coverage",
        ],
        "contexts": ["testing", "CI", "regression", "quality_assurance"],
    },
    "P07_smoke_eval": {
        "seeds": [
            "scope",
            "critical_path",
            "timeout",
            "health_check",
            "assertions",
            "fast_fail",
            "prerequisites",
            "environment",
            "alerting",
            "frequency",
        ],
        "contexts": ["deployment", "monitoring", "CI", "quick_validation"],
    },
    "P07_e2e_eval": {
        "seeds": [
            "pipeline",
            "stages",
            "input",
            "expected_output",
            "timeout",
            "environment",
            "data_fixtures",
            "cleanup",
            "parallel",
            "reporting",
        ],
        "contexts": ["release", "integration", "regression", "acceptance"],
    },
    "P07_benchmark": {
        "seeds": [
            "metric",
            "baseline",
            "target",
            "methodology",
            "environment",
            "iterations",
            "warmup",
            "percentiles",
            "comparison",
            "reporting",
        ],
        "contexts": ["optimization", "comparison", "regression", "capacity_planning"],
    },
    "P07_golden_test": {
        "seeds": [
            "case",
            "input",
            "golden_output",
            "quality_score",
            "rationale",
            "edge_case",
            "domain",
            "versioning",
            "reviewer",
            "approval",
        ],
        "contexts": ["quality_baseline", "calibration", "training", "audit"],
    },
    "P07_scoring_rubric": {
        "seeds": [
            "framework",
            "dimensions",
            "weights",
            "thresholds",
            "examples",
            "calibration",
            "inter_rater",
            "automation",
            "edge_cases",
            "appeals",
        ],
        "contexts": ["evaluation", "standardization", "training", "audit"],
    },
    # ── P08 Architecture ──
    "P08_satellite_spec": {
        "seeds": [
            "name",
            "role",
            "model",
            "mcps",
            "domain",
            "boot_sequence",
            "constraints",
            "dispatch",
            "tools",
            "dependencies",
            "scaling",
            "monitoring",
        ],
        "contexts": ["design", "deployment", "optimization", "documentation"],
    },
    "P08_pattern": {
        "seeds": [
            "name",
            "problem",
            "solution",
            "context",
            "forces",
            "consequences",
            "examples",
            "related_patterns",
            "anti_patterns",
            "applicability",
        ],
        "contexts": ["design", "refactoring", "documentation", "teaching"],
    },
    "P08_law": {
        "seeds": [
            "number",
            "statement",
            "rationale",
            "enforcement",
            "exceptions",
            "examples",
            "violations",
            "history",
            "scope",
            "priority",
        ],
        "contexts": ["governance", "compliance", "onboarding", "evolution"],
    },
    "P08_diagram": {
        "seeds": [
            "scope",
            "notation",
            "components",
            "connections",
            "layers",
            "legend",
            "ascii",
            "mermaid",
            "zoom_level",
            "annotations",
        ],
        "contexts": ["documentation", "communication", "debugging", "planning"],
    },
    "P08_component_map": {
        "seeds": [
            "scope",
            "components",
            "connections",
            "dependencies",
            "data_flow",
            "ownership",
            "health",
            "versioning",
            "interfaces",
            "boundaries",
        ],
        "contexts": ["architecture_review", "debugging", "planning", "onboarding"],
    },
    # ── P09 Config ──
    "P09_env_config": {
        "seeds": [
            "scope",
            "variables",
            "defaults",
            "required",
            "sensitive",
            "environment",
            "validation",
            "override",
            "documentation",
            "examples",
        ],
        "contexts": ["setup", "deployment", "debugging", "migration"],
    },
    "P09_path_config": {
        "seeds": [
            "scope",
            "paths",
            "platform",
            "relative",
            "absolute",
            "fallback",
            "creation",
            "permissions",
            "validation",
            "documentation",
        ],
        "contexts": ["setup", "cross_platform", "migration", "debugging"],
    },
    "P09_permission": {
        "seeds": [
            "scope",
            "read",
            "write",
            "execute",
            "roles",
            "inheritance",
            "deny_list",
            "allow_list",
            "audit",
            "escalation",
        ],
        "contexts": ["security", "onboarding", "compliance", "debugging"],
    },
    "P09_feature_flag": {
        "seeds": [
            "feature",
            "enabled",
            "rollout_percentage",
            "conditions",
            "expiry",
            "owner",
            "description",
            "metrics",
            "fallback",
            "cleanup",
        ],
        "contexts": ["release", "experimentation", "rollback", "cleanup"],
    },
    "P09_runtime_rule": {
        "seeds": [
            "rule",
            "timeouts",
            "retries",
            "limits",
            "circuit_breaker",
            "backoff",
            "jitter",
            "priority",
            "resource_caps",
            "monitoring",
        ],
        "contexts": ["resilience", "optimization", "debugging", "scaling"],
    },
    # ── P10 Memory ──
    "P10_mental_model": {
        "seeds": [
            "agent",
            "routing",
            "decisions",
            "priorities",
            "domain_map",
            "tools",
            "personality",
            "constraints",
            "heuristics",
            "evolution",
        ],
        "contexts": ["agent_design", "optimization", "debugging", "documentation"],
    },
    "P10_brain_index": {
        "seeds": [
            "index",
            "algorithm",
            "bm25",
            "faiss",
            "hybrid",
            "rebuild_schedule",
            "scope",
            "filters",
            "ranking",
            "freshness",
        ],
        "contexts": ["setup", "optimization", "debugging", "migration"],
    },
    "P10_learning_record": {
        "seeds": [
            "topic",
            "outcome",
            "pattern",
            "anti_pattern",
            "score",
            "context",
            "timestamp",
            "satellite",
            "reproducibility",
            "impact",
        ],
        "contexts": ["retrospective", "optimization", "training", "audit"],
    },
    "P10_session_state": {
        "seeds": [
            "session",
            "snapshot",
            "active_tasks",
            "context_window",
            "tokens_used",
            "tools_called",
            "errors",
            "duration",
            "checkpoints",
            "recovery",
        ],
        "contexts": ["debugging", "recovery", "monitoring", "optimization"],
    },
    "P10_axiom": {
        "seeds": [
            "rule",
            "rationale",
            "scope",
            "enforcement",
            "immutable",
            "examples",
            "violations",
            "history",
            "priority",
            "dependencies",
        ],
        "contexts": ["governance", "onboarding", "compliance", "evolution"],
    },
    # ── P11 Feedback ──
    "P11_quality_gate": {
        "seeds": [
            "gate",
            "threshold",
            "dimensions",
            "pass_fail",
            "score",
            "blocking",
            "auto_fix",
            "escalation",
            "bypass",
            "logging",
        ],
        "contexts": ["CI", "review", "deployment", "automation"],
    },
    "P11_bugloop": {
        "seeds": [
            "scope",
            "detect",
            "fix",
            "verify",
            "cycle_count",
            "auto_fix",
            "escalation",
            "confidence",
            "test_suite",
            "rollback",
        ],
        "contexts": ["debugging", "CI", "self_healing", "monitoring"],
    },
    "P11_lifecycle_rule": {
        "seeds": [
            "rule",
            "freshness",
            "archive",
            "promote",
            "demote",
            "expiry",
            "review_cycle",
            "ownership",
            "notification",
            "automation",
        ],
        "contexts": ["maintenance", "governance", "cleanup", "quality"],
    },
    "P11_guardrail": {
        "seeds": [
            "scope",
            "boundary",
            "enforcement",
            "severity",
            "bypass",
            "logging",
            "alerting",
            "examples",
            "violations",
            "remediation",
        ],
        "contexts": ["security", "compliance", "safety", "quality"],
    },
    "P11_optimizer": {
        "seeds": [
            "target",
            "metric",
            "action",
            "threshold",
            "frequency",
            "baseline",
            "improvement",
            "cost",
            "risk",
            "monitoring",
        ],
        "contexts": ["performance", "cost_reduction", "quality", "automation"],
    },
    # ── P12 Orchestration ──
    "P12_workflow": {
        "seeds": [
            "name",
            "steps",
            "parallel",
            "sequential",
            "dependencies",
            "error_handling",
            "timeout",
            "retry",
            "state",
            "completion",
        ],
        "contexts": ["automation", "design", "debugging", "optimization"],
    },
    "P12_dag": {
        "seeds": [
            "pipeline",
            "nodes",
            "edges",
            "dependencies",
            "parallel",
            "topological_sort",
            "cycle_detection",
            "execution_order",
            "state",
            "visualization",
        ],
        "contexts": ["pipeline_design", "optimization", "debugging", "documentation"],
    },
    "P12_spawn_config": {
        "seeds": [
            "mode",
            "satellite",
            "model",
            "flags",
            "mcp_config",
            "timeout",
            "interactive",
            "prompt",
            "handoff",
            "signal",
        ],
        "contexts": ["deployment", "scaling", "debugging", "optimization"],
    },
    "P12_signal": {
        "seeds": [
            "event",
            "satellite",
            "status",
            "score",
            "timestamp",
            "payload",
            "routing",
            "acknowledgment",
            "expiry",
            "priority",
        ],
        "contexts": ["coordination", "monitoring", "debugging", "automation"],
    },
    "P12_handoff": {
        "seeds": [
            "task",
            "context",
            "commit",
            "scope_fence",
            "seeds",
            "autonomy",
            "quality_target",
            "signal",
            "satellite",
            "dependencies",
        ],
        "contexts": ["dispatch", "delegation", "documentation", "automation"],
    },
    "P12_dispatch_rule": {
        "seeds": [
            "scope",
            "keywords",
            "satellite",
            "model",
            "priority",
            "confidence",
            "fallback",
            "conditions",
            "load_balance",
            "routing",
        ],
        "contexts": ["routing", "optimization", "debugging", "scaling"],
    },
}


def load_yaml_file(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def validate_coverage(seed_bank: dict) -> tuple[int, int, list[str]]:
    """Validate all 69 types are covered."""
    missing = []
    for lp_key, lp_dir in sorted(LP_DIRS.items()):
        schema_path = CEX_ROOT / lp_dir / "_schema.yaml"
        if not schema_path.exists():
            continue
        schema = load_yaml_file(schema_path)
        for type_name in schema.get("types", {}):
            key = f"{lp_key}_{type_name}"
            if key not in seed_bank:
                missing.append(key)
    covered = len(seed_bank)
    total = covered + len(missing)
    return covered, total, missing


def generate_yaml(seed_bank: dict) -> str:
    lines = [
        "# SEED_BANK.yaml — Seeds por tipo CEX",
        f"# Gerado: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "# Fonte: cex_seed_bank.py (analise de schemas + templates)",
        f"# Total: {len(seed_bank)} tipos cobertos",
        "",
    ]

    current_lp = None
    for key in sorted(seed_bank.keys()):
        entry = seed_bank[key]
        lp = key.split("_")[0]
        if lp != current_lp:
            lp_name = LP_DIRS.get(lp, lp).split("_", 1)[-1] if lp in LP_DIRS else lp
            lines.append(f"# ── {lp} {lp_name} ──")
            current_lp = lp

        lines.append(f"{key}:")
        seeds = entry["seeds"]
        lines.append(f"  seeds: [{', '.join(seeds)}]")
        contexts = entry["contexts"]
        lines.append(f"  contexts: [{', '.join(contexts)}]")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="CEX Seed Bank — Gera seeds por tipo",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview sem salvar")
    parser.add_argument("--lp", help="Filtrar por LP (ex: P01)")
    parser.add_argument("--validate", action="store_true", help="Validar cobertura")

    args = parser.parse_args()

    if args.validate:
        covered, total, missing = validate_coverage(SEED_BANK)
        print(f"Cobertura: {covered}/{total} tipos")
        if missing:
            print(f"Faltando: {', '.join(missing)}")
        else:
            print("100% cobertura!")
        return

    bank = SEED_BANK
    if args.lp:
        prefix = args.lp.upper() + "_"
        bank = {k: v for k, v in SEED_BANK.items() if k.startswith(prefix)}
        if not bank:
            print(f"ERRO: Nenhum tipo encontrado para {args.lp}", file=sys.stderr)
            sys.exit(1)

    output = generate_yaml(bank)

    if args.dry_run:
        print(output)
        print(f"\n--- {len(bank)} tipos | dry-run (nao salvo) ---", file=sys.stderr)
    else:
        META_DIR.mkdir(parents=True, exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"SEED_BANK.yaml salvo em: {OUTPUT_PATH}", file=sys.stderr)
        print(f"Total: {len(bank)} tipos cobertos", file=sys.stderr)

        # Validate
        covered, total, missing = validate_coverage(SEED_BANK)
        if missing:
            print(f"WARN: {len(missing)} tipos sem seeds: {', '.join(missing)}", file=sys.stderr)
        else:
            print(f"Cobertura: {covered}/{total} (100%)", file=sys.stderr)


if __name__ == "__main__":
    main()
