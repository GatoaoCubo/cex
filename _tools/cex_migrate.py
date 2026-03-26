#!/usr/bin/env python3
"""
cex_migrate.py — Migra artefatos existentes para formato CEX-compliant.

Funcoes:
  1. Analisa frontmatter atual vs CEX schema
  2. Infere campos faltantes (lp, llm_function, when_to_use)
  3. Renomeia campos (quality_score -> quality, type: KC -> type: knowledge_card)
  4. Adiciona campos CEX extended (keywords, density_score)
  5. Gera relatorio de migracao

Uso:
  python cex_migrate.py --scan records/pool/knowledge/  # analisa sem alterar
  python cex_migrate.py --migrate records/pool/knowledge/KC_EXAMPLE.md  # migra 1
  python cex_migrate.py --migrate-all records/pool/knowledge/ --dry-run  # preview
  python cex_migrate.py --migrate-all records/pool/knowledge/  # migra todos
"""

import argparse
import os
import re
import sys
from pathlib import Path
from datetime import datetime

try:
    import yaml
except ImportError:
    print("pip install pyyaml")
    sys.exit(1)

# ─── Type inference maps ───

TYPE_MAP = {
    "KC": "knowledge_card",
    "knowledge_card": "knowledge_card",
    "agent": "agent",
    "skill": "skill",
    "prompt": "system_prompt",
}

# Infer LP from type
TYPE_TO_LP = {
    "knowledge_card": "P01",
    "rag_source": "P01",
    "glossary_entry": "P01",
    "context_doc": "P01",
    "embedding_config": "P01",
    "few_shot_example": "P01",
    "agent": "P02",
    "lens": "P02",
    "mental_model": "P02",
    "model_card": "P02",
    "iso_package": "P02",
    "router": "P02",
    "boot_config": "P02",
    "fallback_chain": "P02",
    "system_prompt": "P03",
    "user_prompt": "P03",
    "prompt_template": "P03",
    "few_shot": "P03",
    "chain_of_thought": "P03",
    "react": "P03",
    "chain": "P03",
    "meta_prompt": "P03",
    "router_prompt": "P03",
    "planner": "P03",
    "skill": "P04",
    "mcp_server": "P04",
    "hook": "P04",
    "plugin": "P04",
    "client": "P04",
    "cli_tool": "P04",
    "scraper": "P04",
    "connector": "P04",
    "daemon": "P04",
    "component": "P04",
    "response_format": "P05",
    "parser": "P05",
    "formatter": "P05",
    "naming_rule": "P05",
    "input_schema": "P06",
    "type_def": "P06",
    "validator": "P06",
    "interface": "P06",
    "validation_schema": "P06",
    "artifact_blueprint": "P06",
    "grammar": "P06",
    "unit_eval": "P07",
    "smoke_eval": "P07",
    "e2e_eval": "P07",
    "benchmark": "P07",
    "golden_test": "P07",
    "scoring_rubric": "P07",
    "satellite_spec": "P08",
    "pattern": "P08",
    "law": "P08",
    "diagram": "P08",
    "component_map": "P08",
    "env_config": "P09",
    "path_config": "P09",
    "permission": "P09",
    "feature_flag": "P09",
    "runtime_rule": "P09",
    "runtime_state": "P10",
    "brain_index": "P10",
    "learning_record": "P10",
    "session_state": "P10",
    "axiom": "P10",
    "quality_gate": "P11",
    "bugloop": "P11",
    "lifecycle_rule": "P11",
    "guardrail": "P11",
    "optimizer": "P11",
    "workflow": "P12",
    "dag": "P12",
    "spawn_config": "P12",
    "signal": "P12",
    "handoff": "P12",
    "dispatch_rule": "P12",
    "crew": "P12",
}

TYPE_TO_FUNCTION = {
    "knowledge_card": "INJECT", "rag_source": "INJECT", "glossary_entry": "INJECT",
    "context_doc": "INJECT", "few_shot_example": "INJECT", "lens": "INJECT",
    "user_prompt": "INJECT", "few_shot": "INJECT", "pattern": "INJECT",
    "diagram": "INJECT", "component_map": "INJECT", "runtime_state": "INJECT",
    "brain_index": "INJECT", "learning_record": "INJECT", "session_state": "INJECT",
    "agent": "BECOME", "mental_model": "BECOME", "iso_package": "BECOME",
    "system_prompt": "BECOME", "satellite_spec": "BECOME",
    "chain_of_thought": "REASON", "react": "REASON", "planner": "REASON",
    "router_prompt": "REASON", "router": "REASON", "dispatch_rule": "REASON",
    "skill": "CALL", "mcp_server": "CALL", "plugin": "CALL", "client": "CALL",
    "cli_tool": "CALL", "scraper": "CALL", "connector": "CALL", "component": "CALL",
    "chain": "PRODUCE", "meta_prompt": "PRODUCE", "workflow": "PRODUCE", "dag": "PRODUCE",
    "prompt_template": "CONSTRAIN", "response_format": "CONSTRAIN",
    "input_schema": "CONSTRAIN", "interface": "CONSTRAIN",
    "artifact_blueprint": "CONSTRAIN", "grammar": "CONSTRAIN",
    "law": "CONSTRAIN", "axiom": "CONSTRAIN", "guardrail": "CONSTRAIN",
    "signal": "COLLABORATE", "handoff": "COLLABORATE", "crew": "COLLABORATE",
}

# Everything else defaults to GOVERN


def parse_frontmatter(text: str) -> tuple:
    """Returns (frontmatter_dict, body_text, raw_fm_text)"""
    if not text.startswith("---"):
        return {}, text, ""
    end = text.find("---", 3)
    if end < 0:
        return {}, text, ""
    raw = text[3:end].strip()
    body = text[end + 3:].strip()
    try:
        fm = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body, raw


def estimate_density(body: str) -> float:
    """Rough density: unique info words / total words."""
    words = body.split()
    if len(words) < 10:
        return 0.5
    unique = len(set(w.lower().strip(".,;:!?()-") for w in words if len(w) > 3))
    return round(min(unique / len(words) * 1.8, 1.0), 2)


def extract_keywords(fm: dict, body: str) -> list:
    """Extract keywords from tags + title + first heading."""
    kw = set()
    for t in fm.get("tags", []):
        if isinstance(t, str):
            kw.add(t.lower())
    title = fm.get("title", "")
    for w in title.split():
        w = w.strip(".,;:!?()-").lower()
        if len(w) > 3 and w not in {"para", "como", "site", "codexa", "with", "from"}:
            kw.add(w)
    return sorted(kw)[:10]


def infer_when_to_use(fm: dict) -> str:
    """Generate when_to_use from title + domain."""
    title = fm.get("title", "Unknown")
    domain = fm.get("domain", "general")
    return f"Quando precisar de contexto sobre {domain}: {title}"


def migrate_frontmatter(fm: dict, body: str) -> dict:
    """Upgrade frontmatter to CEX-compliant format."""
    new = dict(fm)

    # Rename type
    old_type = str(fm.get("kind", "KC"))
    new["kind"] = TYPE_MAP.get(old_type, old_type.lower())

    # Add lp
    if "lp" not in new:
        new["pillar"] = TYPE_TO_LP.get(new["kind"], "P01")

    # Add llm_function
    if "llm_function" not in new:
        new["llm_function"] = TYPE_TO_FUNCTION.get(new["kind"], "GOVERN")

    # Rename quality_score -> quality
    if "quality_score" in new and "quality" not in new:
        new["quality"] = new.pop("quality_score")

    # Add when_to_use
    if "when_to_use" not in new:
        new["when_to_use"] = infer_when_to_use(new)

    # Add CEX extended fields
    if "keywords" not in new:
        new["keywords"] = extract_keywords(new, body)

    if "density_score" not in new:
        new["density_score"] = estimate_density(body)

    if "long_tails" not in new:
        title = new.get("title", "")
        new["long_tails"] = [f"como usar {title.lower()[:50]}"]

    if "axioms" not in new:
        new["axioms"] = []

    if "linked_artifacts" not in new:
        new["linked_artifacts"] = {}

    # Ensure version
    if "version" not in new:
        new["version"] = "1.0.0"

    return new


def scan_file(path: Path) -> dict:
    """Analyze one file and return compliance report."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    fm, body, _ = parse_frontmatter(text)
    if not fm:
        return {"path": str(path), "status": "NO_FRONTMATTER", "missing": []}

    cex_required = [
        "id", "kind", "lp", "title", "version", "created",
        "updated", "author", "domain", "quality", "tags", "tldr", "when_to_use"
    ]
    cex_extended = ["keywords", "long_tails", "axioms", "density_score"]

    # Check quality_score alias
    has_quality = "quality" in fm or "quality_score" in fm
    has_type_cex = fm.get("kind", "") not in ("KC",)

    missing_req = [f for f in cex_required if f not in fm and not (f == "quality" and has_quality)]
    missing_ext = [f for f in cex_extended if f not in fm]

    return {
        
