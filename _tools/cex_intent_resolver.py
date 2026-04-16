#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Intent Resolver -- Python-first kind resolution with ZERO LLM tokens.

Resolves user intent to {kind, pillar, nucleus, verb} using:
  1. Exact match: verb table + kind pattern dict (instant, 0 tokens)
  2. TF-IDF fallback: similarity search over kinds_meta.json descriptions (~10ms)
  3. Returns None if confidence < 60% (caller should use LLM)

Usage (CLI):
    python _tools/cex_intent_resolver.py "criar um agente de pesquisa"
    python _tools/cex_intent_resolver.py "something very vague"
    python _tools/cex_intent_resolver.py --json "improve test coverage"

Usage (import):
    from cex_intent_resolver import resolve_intent
    result = resolve_intent("quero melhorar os testes")
    if result["confidence"] >= 0.6:
        kind, pillar, nucleus = result["kind"], result["pillar"], result["nucleus"]

Exit code: 0 if resolved (confidence >= 0.6), 1 if needs LLM.
"""

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
KINDS_META_PATH = ROOT / ".cex" / "kinds_meta.json"

# Confidence threshold -- below this, recommend LLM fallback
CONFIDENCE_THRESHOLD = 0.60

# ---------------------------------------------------------------------------
# Normalization (ASCII-safe, no external deps)
# ---------------------------------------------------------------------------

# Accent map using unicode escapes (ASCII-safe source)
_ACCENT_MAP = {
    "\u00e1": "a", "\u00e0": "a", "\u00e3": "a", "\u00e2": "a",
    "\u00e9": "e", "\u00ea": "e", "\u00ed": "i",
    "\u00f3": "o", "\u00f4": "o", "\u00f5": "o",
    "\u00fa": "u", "\u00fc": "u", "\u00e7": "c",
    "\u00e1": "a", "\u00e9": "e", "\u00ed": "i", "\u00f3": "o", "\u00fa": "u",
    "\u00f1": "n",
}

# Stop words (PT + EN) -- common words that add no signal
STOP_WORDS = frozenset({
    "a", "o", "e", "de", "do", "da", "para", "com", "em", "um", "uma",
    "os", "as", "no", "na", "nos", "nas", "que", "se", "por", "mais",
    "como", "sobre", "este", "quero", "preciso", "me", "meu", "minha",
    "the", "a", "an", "and", "or", "of", "to", "in", "for", "with",
    "on", "is", "it", "this", "that", "from", "by", "at", "be", "as",
    "are", "was", "will", "has", "i", "my", "want", "need",
})


def normalize(text: str) -> str:
    """Lowercase, strip accents, remove punctuation."""
    text = text.lower().strip()
    for src, dst in _ACCENT_MAP.items():
        text = text.replace(src, dst)
    text = re.sub(r"[-_]", " ", text)
    text = re.sub(r"[^a-z0-9 ]", "", text)
    return text


def tokenize(text: str) -> list[str]:
    """Normalize, split, remove stop words."""
    words = normalize(text).split()
    return [w for w in words if w not in STOP_WORDS and len(w) >= 2]


# ---------------------------------------------------------------------------
# Verb Resolution Table (PT + EN -> canonical verb)
# ---------------------------------------------------------------------------

VERB_TABLE = {
    # PT verbs
    "criar": "create", "crie": "create", "cria": "create",
    "construir": "create", "construa": "create",
    "fazer": "create", "faca": "create",
    "melhorar": "improve", "melhore": "improve",
    "evoluir": "improve", "evolua": "improve",
    "analisar": "analyze", "analise": "analyze",
    "revisar": "analyze", "revise": "analyze",
    "validar": "validate", "valide": "validate",
    "verificar": "validate", "verifique": "validate",
    "documentar": "document", "documente": "document",
    "testar": "test", "teste": "test",
    "deployar": "deploy", "implantar": "deploy", "implante": "deploy",
    "configurar": "configure", "configure": "configure",
    "otimizar": "optimize", "otimize": "optimize",
    "pesquisar": "research", "pesquise": "research",
    "investigar": "research", "investigue": "research",
    "monitorar": "monitor", "monitore": "monitor",
    "agendar": "schedule", "agende": "schedule",
    "corrigir": "fix", "corrija": "fix", "consertar": "fix",
    "auditar": "audit", "audite": "audit",
    # EN verbs
    "create": "create", "build": "create", "make": "create",
    "add": "create", "new": "create", "generate": "create",
    "improve": "improve", "enhance": "improve", "evolve": "improve",
    "upgrade": "improve", "refactor": "improve",
    "analyze": "analyze", "review": "analyze", "audit": "audit",
    "inspect": "analyze", "examine": "analyze",
    "validate": "validate", "verify": "validate", "check": "validate",
    "document": "document", "describe": "document", "write": "create",
    "test": "test", "evaluate": "test", "benchmark": "test",
    "deploy": "deploy", "ship": "deploy", "release": "deploy",
    "configure": "configure", "setup": "configure", "config": "configure",
    "optimize": "optimize", "tune": "optimize",
    "research": "research", "investigate": "research", "study": "research",
    "monitor": "monitor", "watch": "monitor", "observe": "monitor",
    "schedule": "schedule", "plan": "schedule", "cron": "schedule",
    "fix": "fix", "debug": "fix", "repair": "fix",
}

# ---------------------------------------------------------------------------
# Kind Pattern Table -- direct keyword -> kind mapping
# Built from the prompt_compiler Kind Resolution Table
# ---------------------------------------------------------------------------

# Each entry: keyword_pattern -> (kind, pillar, nucleus)
# Patterns are normalized (lowercase, no accents)
KIND_PATTERNS = {
    # P01 Knowledge
    "knowledge card": ("knowledge_card", "P01", "N04"),
    "kc": ("knowledge_card", "P01", "N04"),
    "documentar": ("knowledge_card", "P01", "N04"),
    "chunking": ("chunk_strategy", "P01", "N04"),
    "chunk": ("chunk_strategy", "P01", "N04"),
    "citation": ("citation", "P01", "N04"),
    "citacao": ("citation", "P01", "N04"),
    "context doc": ("context_doc", "P01", "N04"),
    "embedding config": ("embedding_config", "P01", "N04"),
    "embedding provider": ("embedder_provider", "P01", "N04"),
    "few shot": ("few_shot_example", "P01", "N04"),
    "glossary": ("glossary_entry", "P01", "N04"),
    "glossario": ("glossary_entry", "P01", "N04"),
    "rag source": ("rag_source", "P01", "N04"),
    "rag": ("rag_source", "P01", "N04"),
    "retriever config": ("retriever_config", "P01", "N04"),
    "vector store": ("vector_store", "P01", "N04"),
    "vector db": ("vector_store", "P01", "N04"),
    # P02 Model
    "agente": ("agent", "P02", "N03"),
    "agent": ("agent", "P02", "N03"),
    "agent package": ("agent_package", "P02", "N03"),
    "axiom": ("axiom", "P02", "N03"),
    "axioma": ("axiom", "P02", "N03"),
    "boot config": ("boot_config", "P02", "N05"),
    "fallback chain": ("fallback_chain", "P02", "N03"),
    "fallback": ("fallback_chain", "P02", "N03"),
    "handoff protocol": ("handoff_protocol", "P02", "N03"),
    "lens": ("lens", "P02", "N03"),
    "lente": ("lens", "P02", "N03"),
    "memory scope": ("memory_scope", "P02", "N04"),
    "mental model": ("mental_model", "P02", "N03"),
    "model card": ("model_card", "P02", "N03"),
    "model provider": ("model_provider", "P02", "N05"),
    "router": ("router", "P02", "N03"),
    "roteador": ("router", "P02", "N03"),
    # P03 Prompt
    "action prompt": ("action_prompt", "P03", "N03"),
    "prompt template": ("prompt_template", "P03", "N03"),
    "template prompt": ("prompt_template", "P03", "N03"),
    "system prompt": ("system_prompt", "P03", "N03"),
    "prompt sistema": ("system_prompt", "P03", "N03"),
    "chain": ("chain", "P03", "N03"),
    "cadeia prompt": ("chain", "P03", "N03"),
    "constraint": ("constraint_spec", "P03", "N03"),
    "restricao": ("constraint_spec", "P03", "N03"),
    "token budget": ("context_window_config", "P03", "N03"),
    "context window": ("context_window_config", "P03", "N03"),
    "instruction": ("instruction", "P03", "N03"),
    "instrucao": ("instruction", "P03", "N03"),
    "prompt compiler": ("prompt_compiler", "P03", "N03"),
    "prompt version": ("prompt_version", "P03", "N03"),
    "reasoning trace": ("reasoning_trace", "P03", "N03"),
    # P04 Tools
    "api client": ("api_client", "P04", "N05"),
    "cliente api": ("api_client", "P04", "N05"),
    "audio tool": ("audio_tool", "P04", "N05"),
    "tts": ("audio_tool", "P04", "N05"),
    "stt": ("audio_tool", "P04", "N05"),
    "browser tool": ("browser_tool", "P04", "N05"),
    "scraper": ("browser_tool", "P04", "N05"),
    "cli tool": ("cli_tool", "P04", "N05"),
    "code executor": ("code_executor", "P04", "N05"),
    "sandbox": ("code_executor", "P04", "N05"),
    "computer use": ("computer_use", "P04", "N05"),
    "daemon": ("daemon", "P04", "N05"),
    "db connector": ("db_connector", "P04", "N05"),
    "database": ("db_connector", "P04", "N05"),
    "document loader": ("document_loader", "P04", "N05"),
    "function def": ("function_def", "P04", "N05"),
    "hook": ("hook", "P04", "N05"),
    "hook config": ("hook_config", "P04", "N05"),
    "mcp server": ("mcp_server", "P04", "N05"),
    "mcp": ("mcp_server", "P04", "N05"),
    "multimodal": ("multi_modal_config", "P04", "N05"),
    "notifier": ("notifier", "P04", "N05"),
    "notification": ("notifier", "P04", "N05"),
    "plugin": ("plugin", "P04", "N05"),
    "extension": ("plugin", "P04", "N05"),
    "research pipeline": ("research_pipeline", "P04", "N01"),
    "pesquisa profunda": ("research_pipeline", "P04", "N01"),
    "deep research": ("research_pipeline", "P04", "N01"),
    "retriever": ("retriever", "P04", "N04"),
    "search tool": ("search_tool", "P04", "N05"),
    "web search": ("search_tool", "P04", "N05"),
    "toolkit": ("toolkit", "P04", "N05"),
    "vision tool": ("vision_tool", "P04", "N05"),
    "ocr": ("vision_tool", "P04", "N05"),
    "webhook": ("webhook", "P04", "N05"),
    # P05 Output
    "formatter": ("formatter", "P05", "N03"),
    "landing page": ("landing_page", "P05", "N03"),
    "pagina web": ("landing_page", "P05", "N03"),
    "output validator": ("output_validator", "P05", "N03"),
    "parser": ("parser", "P05", "N03"),
    "response format": ("response_format", "P05", "N03"),
    # P06 Schema
    "enum": ("enum_def", "P06", "N03"),
    "enumeracao": ("enum_def", "P06", "N03"),
    "input schema": ("input_schema", "P06", "N03"),
    "interface": ("interface", "P06", "N03"),
    "contrato": ("interface", "P06", "N03"),
    "type def": ("type_def", "P06", "N03"),
    "custom type": ("type_def", "P06", "N03"),
    "validation schema": ("validation_schema", "P06", "N03"),
    "validator": ("validator", "P06", "N03"),
    # P07 Evaluation
    "benchmark": ("benchmark", "P07", "N05"),
    "e2e test": ("e2e_eval", "P07", "N05"),
    "integration test": ("e2e_eval", "P07", "N05"),
    "teste integracao": ("e2e_eval", "P07", "N05"),
    "eval dataset": ("eval_dataset", "P07", "N05"),
    "golden test": ("golden_test", "P07", "N05"),
    "llm judge": ("llm_judge", "P07", "N05"),
    "red team": ("red_team_eval", "P07", "N05"),
    "regression": ("regression_check", "P07", "N05"),
    "scoring rubric": ("scoring_rubric", "P07", "N05"),
    "smoke test": ("smoke_eval", "P07", "N05"),
    "trace config": ("trace_config", "P07", "N05"),
    "observability": ("trace_config", "P07", "N05"),
    "unit test": ("unit_eval", "P07", "N05"),
    "teste unitario": ("unit_eval", "P07", "N05"),
    "testes": ("unit_eval", "P07", "N05"),
    "tests": ("unit_eval", "P07", "N05"),
    # P08 Architecture
    "agent card": ("agent_card", "P08", "N03"),
    "component map": ("component_map", "P08", "N03"),
    "decision record": ("decision_record", "P08", "N03"),
    "adr": ("decision_record", "P08", "N03"),
    "diagram": ("diagram", "P08", "N03"),
    "diagrama": ("diagram", "P08", "N03"),
    "invariant": ("invariant", "P08", "N03"),
    "naming rule": ("naming_rule", "P08", "N03"),
    "naming convention": ("naming_rule", "P08", "N03"),
    "pattern": ("pattern", "P08", "N03"),
    "design pattern": ("pattern", "P08", "N03"),
    "supervisor": ("supervisor", "P08", "N03"),
    # P09 Config
    "effort profile": ("effort_profile", "P09", "N03"),
    "env config": ("env_config", "P09", "N05"),
    "environment": ("env_config", "P09", "N05"),
    "feature flag": ("feature_flag", "P09", "N05"),
    "toggle": ("feature_flag", "P09", "N05"),
    "path config": ("path_config", "P09", "N05"),
    "permission": ("permission", "P09", "N05"),
    "access control": ("permission", "P09", "N05"),
    "rate limit": ("rate_limit_config", "P09", "N05"),
    "throttle": ("rate_limit_config", "P09", "N05"),
    "runtime rule": ("runtime_rule", "P09", "N05"),
    "secret config": ("secret_config", "P09", "N05"),
    "credentials": ("secret_config", "P09", "N05"),
    "secrets": ("secret_config", "P09", "N05"),
    # P10 Memory
    "compression config": ("compression_config", "P10", "N04"),
    "entity memory": ("entity_memory", "P10", "N04"),
    "knowledge index": ("knowledge_index", "P10", "N04"),
    "search index": ("knowledge_index", "P10", "N04"),
    "learning record": ("learning_record", "P10", "N04"),
    "memory summary": ("memory_summary", "P10", "N04"),
    "memory type": ("memory_type", "P10", "N04"),
    "prompt cache": ("prompt_cache", "P10", "N05"),
    "cache": ("prompt_cache", "P10", "N05"),
    "runtime state": ("runtime_state", "P10", "N05"),
    "session backend": ("session_backend", "P10", "N05"),
    "session state": ("session_state", "P10", "N05"),
    # P11 Feedback
    "bugloop": ("bugloop", "P11", "N05"),
    "auto fix": ("bugloop", "P11", "N05"),
    "correcao automatica": ("bugloop", "P11", "N05"),
    "monetization": ("content_monetization", "P11", "N06"),
    "monetizacao": ("content_monetization", "P11", "N06"),
    "pricing": ("content_monetization", "P11", "N06"),
    "preco": ("content_monetization", "P11", "N06"),
    "guardrail": ("guardrail", "P11", "N03"),
    "safety": ("guardrail", "P11", "N03"),
    "lifecycle rule": ("lifecycle_rule", "P11", "N03"),
    "optimizer": ("optimizer", "P11", "N05"),
    "quality gate": ("quality_gate", "P11", "N03"),
    "reward signal": ("reward_signal", "P11", "N03"),
    # P12 Orchestration
    "checkpoint": ("checkpoint", "P12", "N03"),
    "dag": ("dag", "P12", "N03"),
    "dependency graph": ("dag", "P12", "N03"),
    "dispatch rule": ("dispatch_rule", "P12", "N03"),
    "handoff": ("handoff", "P12", "N07"),
    "schedule": ("schedule", "P12", "N07"),
    "cron": ("schedule", "P12", "N07"),
    "signal": ("signal", "P12", "N07"),
    "spawn config": ("spawn_config", "P12", "N05"),
    "workflow": ("workflow", "P12", "N03"),
    "workflow primitive": ("workflow_primitive", "P12", "N03"),
}


# ---------------------------------------------------------------------------
# Kinds meta loader
# ---------------------------------------------------------------------------

_kinds_meta_cache = None


def _load_kinds_meta():
    """Load kinds_meta.json (cached)."""
    global _kinds_meta_cache
    if _kinds_meta_cache is not None:
        return _kinds_meta_cache

    if not KINDS_META_PATH.exists():
        _kinds_meta_cache = {}
        return _kinds_meta_cache

    try:
        raw = KINDS_META_PATH.read_text(encoding="utf-8")
        _kinds_meta_cache = json.loads(raw)
    except Exception:
        _kinds_meta_cache = {}

    return _kinds_meta_cache


# ---------------------------------------------------------------------------
# Phase 1: Exact match (dict lookup)
# ---------------------------------------------------------------------------

def _resolve_verb(tokens):
    """Extract canonical verb from tokens."""
    for token in tokens:
        if token in VERB_TABLE:
            return VERB_TABLE[token]
    return "create"  # default


def _exact_match(text):
    """Try direct pattern match against KIND_PATTERNS.

    Returns (kind, pillar, nucleus, confidence) or None.
    """
    norm = normalize(text)

    # Try multi-word patterns first (longer = more specific)
    sorted_patterns = sorted(KIND_PATTERNS.keys(), key=len, reverse=True)
    for pattern in sorted_patterns:
        if pattern in norm:
            kind, pillar, nucleus = KIND_PATTERNS[pattern]
            # Confidence based on pattern length vs input length
            ratio = len(pattern) / max(len(norm), 1)
            confidence = min(0.95, 0.70 + ratio * 0.25)
            return kind, pillar, nucleus, confidence

    # Try matching kind names directly from kinds_meta
    kinds_meta = _load_kinds_meta()
    tokens = set(tokenize(text))
    for kind_name in kinds_meta:
        # Match: "agent_card" -> tokens contain "agent" AND "card"
        kind_parts = set(kind_name.replace("_", " ").split())
        if kind_parts and kind_parts.issubset(tokens):
            entry = kinds_meta[kind_name]
            return (
                kind_name,
                entry.get("pillar", "P01"),
                _infer_nucleus(entry),
                0.85,
            )

    return None


def _infer_nucleus(kind_entry):
    """Infer nucleus from kind_entry LLM function."""
    fn = kind_entry.get("llm_function", "")
    fn_to_nucleus = {
        "BECOME": "N03",
        "INJECT": "N03",
        "CALL": "N05",
        "GOVERN": "N05",
        "PRODUCE": "N03",
    }
    return fn_to_nucleus.get(fn, "N03")


# ---------------------------------------------------------------------------
# Phase 2: TF-IDF fallback over kinds_meta descriptions
# ---------------------------------------------------------------------------

def _build_tfidf_index():
    """Build TF-IDF index from kinds_meta descriptions."""
    kinds_meta = _load_kinds_meta()
    if not kinds_meta:
        return [], {}, {}

    docs = []  # list of (kind_name, tokens)
    for kind_name, entry in kinds_meta.items():
        desc = entry.get("description", "")
        boundary = entry.get("boundary", "")
        text = "%s %s %s" % (kind_name.replace("_", " "), desc, boundary)
        tokens = tokenize(text)
        docs.append((kind_name, tokens))

    # Build IDF
    n_docs = len(docs)
    df = Counter()
    for _, tokens in docs:
        df.update(set(tokens))

    idf = {}
    for term, count in df.items():
        idf[term] = math.log(n_docs / (1.0 + count))

    return docs, idf, kinds_meta


def _tfidf_search(query_text, top_k=3):
    """Search kinds_meta using TF-IDF similarity.

    Returns list of (kind, pillar, nucleus, confidence).
    """
    docs, idf, kinds_meta = _build_tfidf_index()
    if not docs:
        return []

    query_tokens = tokenize(query_text)
    if not query_tokens:
        return []

    # Score each document
    results = []
    for kind_name, doc_tokens in docs:
        if not doc_tokens:
            continue

        doc_token_set = set(doc_tokens)
        score = 0.0
        matched = 0

        for qt in query_tokens:
            if qt in doc_token_set:
                score += idf.get(qt, 1.0)
                matched += 1
            else:
                # Partial match (substring)
                for dt in doc_token_set:
                    if len(dt) >= 3 and (qt in dt or dt in qt):
                        score += idf.get(dt, 1.0) * 0.5
                        matched += 0.5
                        break

        if score > 0:
            # Normalize to 0-1 range
            max_possible = sum(idf.get(qt, 1.0) for qt in query_tokens)
            confidence = score / max(max_possible, 0.01)
            confidence = min(confidence, 0.92)  # TF-IDF caps below exact

            entry = kinds_meta.get(kind_name, {})
            results.append((
                kind_name,
                entry.get("pillar", "P01"),
                _infer_nucleus(entry),
                round(confidence, 3),
            ))

    results.sort(key=lambda x: x[3], reverse=True)
    return results[:top_k]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def resolve_intent(text: str) -> dict[str, Any]:
    """Resolve user intent to {kind, pillar, nucleus, verb, confidence, method}.

    Args:
        text: Natural language input (PT or EN).

    Returns:
        dict with keys: kind, pillar, nucleus, verb, confidence, method.
        If confidence < CONFIDENCE_THRESHOLD, kind will be None.
    """
    if not text or not text.strip():
        return {
            "kind": None,
            "pillar": None,
            "nucleus": None,
            "verb": "create",
            "confidence": 0.0,
            "method": "empty",
            "suggestion": "No input provided",
        }

    tokens = tokenize(text)
    verb = _resolve_verb(tokens)

    # Phase 1: exact match
    exact = _exact_match(text)
    if exact:
        kind, pillar, nucleus, confidence = exact
        return {
            "kind": kind,
            "pillar": pillar,
            "nucleus": nucleus,
            "verb": verb,
            "confidence": round(confidence, 3),
            "method": "exact",
        }

    # Phase 2: TF-IDF fallback
    tfidf_results = _tfidf_search(text, top_k=1)
    if tfidf_results:
        kind, pillar, nucleus, confidence = tfidf_results[0]
        if confidence >= CONFIDENCE_THRESHOLD:
            return {
                "kind": kind,
                "pillar": pillar,
                "nucleus": nucleus,
                "verb": verb,
                "confidence": confidence,
                "method": "tfidf",
            }
        else:
            return {
                "kind": None,
                "pillar": None,
                "nucleus": None,
                "verb": verb,
                "confidence": confidence,
                "method": "tfidf",
                "suggestion": "Use LLM for resolution",
                "best_guess": {
                    "kind": kind,
                    "pillar": pillar,
                    "nucleus": nucleus,
                },
            }

    # Phase 3: no match at all
    return {
        "kind": None,
        "pillar": None,
        "nucleus": None,
        "verb": verb,
        "confidence": 0.0,
        "method": "none",
        "suggestion": "Use LLM for resolution",
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def resolve_intent_verbose(text: str) -> dict[str, Any]:
    """Verbose wrapper -- prints resolution trace to stderr."""
    tokens = tokenize(text)
    verb = _resolve_verb(tokens)
    print("  [intent] Input:  %s" % text, file=sys.stderr)
    print("  [intent] Tokens: %s" % tokens, file=sys.stderr)
    print("  [intent] Verb:   %s" % verb, file=sys.stderr)

    exact = _exact_match(text)
    if exact:
        kind, pillar, nucleus, confidence = exact
        print("  [intent] Exact match: %s (P=%s, N=%s, conf=%.0f%%)" % (
            kind, pillar, nucleus, confidence * 100), file=sys.stderr)
        return resolve_intent(text)

    print("  [intent] No exact match, trying TF-IDF...", file=sys.stderr)
    tfidf_results = _tfidf_search(text, top_k=3)
    if tfidf_results:
        for k, p, n, c in tfidf_results:
            print("  [intent] TF-IDF: %-22s P=%-4s N=%-3s conf=%.0f%%" % (
                k, p, n, c * 100), file=sys.stderr)
    else:
        print("  [intent] TF-IDF: no matches", file=sys.stderr)

    return resolve_intent(text)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CEX Intent Resolver -- Python-first kind resolution (0 LLM tokens)"
    )
    parser.add_argument("query", nargs="?", help="Natural language intent")
    parser.add_argument("--json", action="store_true",
                        help="Output as JSON (default for pipe)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show resolution trace on stderr")
    parser.add_argument("--batch", metavar="FILE",
                        help="Resolve intents from file (one per line)")
    parser.add_argument("--threshold", type=float, default=CONFIDENCE_THRESHOLD,
                        help="Confidence threshold (default: %.2f)" % CONFIDENCE_THRESHOLD)
    parser.add_argument("--test", action="store_true",
                        help="Run built-in self-test suite")
    args = parser.parse_args()

    # Self-test mode
    if args.test:
        print("=== CEX Intent Resolver Self-Test ===\n")
        cases = [
            ("criar um agente de pesquisa", "agent", 0.6),
            ("create agent", "agent", 0.6),
            ("MCP server para Supabase", "mcp_server", 0.6),
            ("webhook endpoint", "webhook", 0.6),
            ("landing page para meu produto", "landing_page", 0.6),
            ("configurar RAG", "rag_source", 0.6),
            ("benchmark de performance", "benchmark", 0.6),
            ("pricing strategy", "content_monetization", 0.6),
            ("system prompt do agente", "system_prompt", 0.6),
            ("quality gate", "quality_gate", 0.6),
            ("red team eval", "red_team_eval", 0.6),
            ("unit test", "unit_eval", 0.6),
            ("guardrail de seguranca", "guardrail", 0.6),
            ("workflow de deploy", "workflow", 0.6),
            ("glossario de termos", "glossary_entry", 0.6),
        ]
        passed = 0
        for user_input, expected_kind, min_conf in cases:
            result = resolve_intent(user_input)
            ok = (result.get("kind") == expected_kind
                  and result.get("confidence", 0) >= min_conf)
            tag = "[OK]" if ok else "[FAIL]"
            if ok:
                passed += 1
            print("  %s %-40s -> %-22s conf=%.0f%% method=%s" % (
                tag, '"%s"' % user_input[:36],
                result.get("kind") or "(none)",
                result.get("confidence", 0) * 100,
                result.get("method", "?"),
            ))
        print("\n  %d/%d passed" % (passed, len(cases)))
        sys.exit(0 if passed == len(cases) else 1)

    resolver = resolve_intent_verbose if args.verbose else resolve_intent

    # Batch mode
    if args.batch:
        batch_path = Path(args.batch)
        if not batch_path.exists():
            print("File not found: %s" % args.batch, file=sys.stderr)
            sys.exit(2)
        lines = [l.strip() for l in batch_path.read_text(encoding="utf-8").splitlines()
                 if l.strip() and not l.strip().startswith("#")]
        results = []
        resolved = 0
        for line in lines:
            r = resolver(line)
            r["input"] = line
            results.append(r)
            if r.get("kind"):
                resolved += 1
        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            for r in results:
                tag = "[OK]" if r.get("kind") else "[??]"
                print("  %s %-35s -> %-20s %s %s (%.0f%% %s)" % (
                    tag, r["input"][:35],
                    r.get("kind") or "?",
                    r.get("pillar") or "?",
                    r.get("nucleus") or "?",
                    r["confidence"] * 100,
                    r["method"],
                ))
            print("\n  Resolved: %d/%d (%.0f%%)" % (
                resolved, len(lines),
                100 * resolved / max(1, len(lines))))
        sys.exit(0 if resolved == len(lines) else 1)

    # Single query
    if not args.query:
        parser.print_help()
        sys.exit(2)

    result = resolver(args.query)

    if args.json or not sys.stdout.isatty():
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print()
        if result["kind"]:
            print("  [OK] Resolved (method: %s, confidence: %.0f%%)" % (
                result["method"], result["confidence"] * 100))
            print("  kind:    %s" % result["kind"])
            print("  pillar:  %s" % result["pillar"])
            print("  nucleus: %s" % result["nucleus"])
            print("  verb:    %s" % result["verb"])
        else:
            print("  [--] Low confidence (%.0f%%) -- LLM fallback recommended" % (
                result["confidence"] * 100))
            print("  method:  %s" % result["method"])
            print("  verb:    %s" % result["verb"])
            if "best_guess" in result:
                bg = result["best_guess"]
                print("  guess:   %s (%s, %s)" % (
                    bg["kind"], bg["pillar"], bg["nucleus"]))
        print()

    sys.exit(0 if result["kind"] else 1)


if __name__ == "__main__":
    main()
