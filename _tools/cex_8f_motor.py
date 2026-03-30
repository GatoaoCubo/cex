import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")
#!/usr/bin/env python3
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
  python cex_8f_motor.py --intent "cria agente E workflow de pesquisa"
  python cex_8f_motor.py --intent "cria agente" --output plan.json
  python cex_8f_motor.py --test
"""

import json
import re
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERRO: PyYAML necessario. pip install pyyaml", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CEX_ROOT = Path(__file__).resolve().parent.parent
BUILDER_MAP_PATH = CEX_ROOT / "_docs" / "8F_BUILDER_MAP.yaml"
KC_LIBRARY_PATH = CEX_ROOT / "P01_knowledge" / "library"
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

# Verb normalization: PT imperative/infinitive -> canonical action
VERB_TABLE = {
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
    "brain_index": [("brain_index", "P10", "INJECT")],
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
    "embedding": [("embedding_config", "P01", "CONSTRAIN")],
    "embedding_config": [("embedding_config", "P01", "CONSTRAIN")],
    "entity_memory": [("entity_memory", "P10", "INJECT")],
    "enum": [("enum_def", "P06", "CONSTRAIN")],
    "enum_def": [("enum_def", "P06", "CONSTRAIN")],
    "env": [("env_config", "P09", "CONSTRAIN")],
    "env_config": [("env_config", "P09", "CONSTRAIN")],
    "eval": [("unit_eval", "P07", "GOVERN")],
    "eval_dataset": [("eval_dataset", "P07", "GOVERN")],
    "fallback": [("fallback_chain", "P02", "REASON")],
    "fallback_chain": [("fallback_chain", "P02", "REASON")],
    "feature_flag": [("feature_flag", "P09", "CONSTRAIN")],
    "ferramenta": [("function_def", "P04", "CALL")],
    "few-shot": [("few_shot_example", "P01", "INJECT")],
    "few_shot": [("few_shot_example", "P01", "INJECT")],
    "fonte": [("rag_source", "P01", "INJECT")],
    "formato": [("response_format", "P05", "PRODUCE")],
    "formatter": [("formatter", "P05", "PRODUCE")],
    "function": [("function_def", "P04", "CALL")],
    "function_def": [("function_def", "P04", "CALL")],
    "glossario": [("glossary_entry", "P01", "INJECT")],
    "glossary": [("glossary_entry", "P01", "INJECT")],
    "golden_test": [("golden_test", "P07", "GOVERN")],
    "grafo": [("dag", "P12", "COLLABORATE")],
    "guardrail": [("guardrail", "P11", "GOVERN")],
    "handoff": [("handoff", "P12", "COLLABORATE")],
    "handoff_protocol": [("handoff_protocol", "P02", "COLLABORATE")],
    "hook": [("hook", "P04", "CALL")],
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
    "memoria": [("brain_index", "P10", "INJECT")],
    "memory": [("brain_index", "P10", "INJECT")],
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
    "retriever": [("retriever_config", "P01", "CONSTRAIN")],
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
    "tipo": [("type_def", "P06", "CONSTRAIN")],
    "tool": [("function_def", "P04", "CALL")],
    "type_def": [("type_def", "P06", "CONSTRAIN")],
    "validation_schema": [("validation_schema", "P06", "CONSTRAIN")],
    "validator": [("validator", "P06", "CONSTRAIN")],
    "vision": [("vision_tool", "P04", "CALL")],
    "vision_tool": [("vision_tool", "P04", "CALL")],
    "webhook": [("webhook", "P04", "CALL")],
    "workflow": [("workflow", "P12", "COLLABORATE")],
    # agent_card (P08) — deployment spec for autonomous agent
    "agent_card": [("agent_card", "P08", "BECOME")],
    "agent-card": [("agent_card", "P08", "BECOME")],
    "agentcard": [("agent_card", "P08", "BECOME")],
    "deployment_spec": [("agent_card", "P08", "BECOME")],
    "deployment": [("agent_card", "P08", "BECOME")],

}

# Verb -> extra builders force-activated regardless of tier
VERB_EXTRA_BUILDERS = {
    "improve": {"quality-gate-builder", "scoring-rubric-builder"},
    "rebuild": {"_builder-builder"},
    "analyze": {"scoring-rubric-builder", "unit-eval-builder"},
    "validate": {"validator-builder", "quality-gate-builder"},
    "document": {"knowledge-card-builder", "context-doc-builder"},
    "integrate": {"db-connector-builder", "interface-builder"},
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
    "validator-builder-codex": ["codex", "code review", "revisao de codigo"],
    "type-def-builder": ["tipo customizado", "type definition", "typedef"],
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
        "director-builder",
    ]
)
META_BUILDERS = frozenset(["_builder-builder"])


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
# Step 1: PARSE — extract verb, objects, domain, quality from intent
# ---------------------------------------------------------------------------


def parse_intent(intent: str, quality_override: float | None = None) -> dict:
    """Parse natural language intent into structured fields."""
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

    segments = re.split(r"\s+[eE]\s+|\s*\+\s*|\s*,\s*", rest)
    segments = [s.strip() for s in segments if s.strip()]

    # --- Objects ---
    objects = []
    for seg in segments:
        seg_words = seg.lower().split()
        for sw in seg_words:
            clean = re.sub(r"[^a-z_-]", "", sw)
            if clean in OBJECT_TO_KINDS and clean not in objects:
                objects.append(clean)
                break

    # Check for builder name in intent (meta intent: "reconstroi X-builder")
    bm = re.search(r"([\w-]+-builder)\b", text_lower)
    if bm and bm.group(1) not in objects:
        objects.append(bm.group(1))

    # Fallback: scan all words
    if not objects:
        for w in words:
            clean = re.sub(r"[^a-z_-]", "", w)
            if clean in OBJECT_TO_KINDS:
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
# Step 2: CLASSIFY — map objects to CEX kinds
# ---------------------------------------------------------------------------


def classify_objects(objects: list[str]) -> list[dict]:
    """Map object keywords to CEX kinds using taxonomy table."""
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
                    "meta": True,
                }
            )
            continue

        kinds = OBJECT_TO_KINDS.get(obj, [])
        for kind, pillar, primary_fn in kinds:
            if kind not in seen_kinds:
                classified.append(
                    {
                        "object": obj,
                        "kind": kind,
                        "pillar": pillar,
                        "primary_function": primary_fn,
                    }
                )
                seen_kinds.add(kind)

    if not classified:
        classified.append(
            {
                "object": "generic",
                "kind": "generic",
                "pillar": "P01",
                "primary_function": "BECOME",
            }
        )

    return classified


# ---------------------------------------------------------------------------
# KC Library — load domain KCs and match by feeds_kinds
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
# Step 3: FAN-OUT — select builders per function
# ---------------------------------------------------------------------------


def load_builder_map() -> dict:
    """Load 8F_BUILDER_MAP.yaml."""
    if not BUILDER_MAP_PATH.exists():
        print(f"ERRO: Builder map nao encontrado: {BUILDER_MAP_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(BUILDER_MAP_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _has_keyword(intent_lower: str, keywords: list[str]) -> bool:
    """Check if intent contains any of the keywords (case-insensitive)."""
    return any(kw.lower() in intent_lower for kw in keywords)


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

        active_list = [b for b in builders if b["active"]]
        est_tokens = int(sum(estimate_tokens(b["id"]) for b in active_list) * 1.2)

        entry = {
            "name": fn_name,
            "position": position,
            "builders": builders,
            "deps": deps,
            "parallel": True,
            "estimated_tokens": est_tokens,
        }

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
                entry["kc_fallback"] = "bld_knowledge_card"

        result.append(entry)

    return result


# ---------------------------------------------------------------------------
# Step 4: PLAN — order functions by pipeline position
# ---------------------------------------------------------------------------


def order_plan(functions: list[dict]) -> list[dict]:
    """Sort functions by their pipeline position (1..8)."""
    return sorted(functions, key=lambda f: f["position"])


# ---------------------------------------------------------------------------
# Step 5: OUTPUT — assemble final JSON
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
            "domain nao identificado — plan pode ser generico. Especifique o artefato alvo."
        )

    if any(c.get("meta") for c in classified):
        warnings.append("intent meta detectado — ativando _builder-builder. Pipeline de 13 files.")

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

    return {
        "intent": intent,
        "parsed": parsed_output,
        "classified_kinds": [{k: v for k, v in c.items() if k != "meta"} for c in classified],
        "functions": ordered,
        "total_builders": total_active,
        "estimated_tokens": total_tokens,
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
  python cex_8f_motor.py --intent "cria agente E workflow de pesquisa"
  python cex_8f_motor.py --test
        """,
    )
    parser.add_argument("--intent", help="Natural language intent string")
    parser.add_argument("--quality", type=float, help="Quality target override")
    parser.add_argument("--output", help="Output file (default: stdout)")
    parser.add_argument("--compact", action="store_true", help="Compact JSON")
    parser.add_argument("--test", action="store_true", help="Run inline tests")

    args = parser.parse_args()

    if args.test:
        run_tests()
        return

    if not args.intent:
        parser.error("--intent is required (or use --test)")

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
    print("\nTest 3: cria agente E workflow de pesquisa")
    p3 = parse_intent("cria agente E workflow de pesquisa")
    check("multi_object=true", p3["multi_object"], f"got {p3['multi_object']}")
    check("has agente", "agente" in p3["objects"], f"got {p3['objects']}")
    check("has workflow", "workflow" in p3["objects"], f"got {p3['objects']}")
    check("domain=pesquisa", "pesquisa" in p3["domain"], f"got {p3['domain']}")

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
