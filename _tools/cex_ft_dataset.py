#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Fine-Tune Dataset Builder v2 -- Multi-ISO extraction, per-nucleus output.

Extracts instruction-response pairs from ALL builder ISOs (13 types) plus
knowledge cards, grouped by nucleus (N01-N07). Outputs Alpaca-format JSONL
for QLoRA fine-tuning.

Usage:
    python _tools/cex_ft_dataset.py                        # Full export
    python _tools/cex_ft_dataset.py --stats                # Stats only
    python _tools/cex_ft_dataset.py --nucleus N03          # Single nucleus
    python _tools/cex_ft_dataset.py --include-supplementary # Add thin-nucleus data
    python _tools/cex_ft_dataset.py --output-dir _data/ft/ # Custom output dir
"""

import argparse
import json
import random
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
BUILDERS_DIR = ROOT / "archetypes" / "builders"
KINDS_META = ROOT / ".cex" / "kinds_meta.json"
KC_DIR = ROOT / "N00_genesis" / "P01_knowledge" / "library" / "kind"
DEFAULT_OUTPUT_DIR = ROOT / "_data" / "ft"

# Canonical kind -> nucleus mapping from kc_intent_resolution_map.md
KIND_TO_NUCLEUS = {
    # N01 Intelligence
    "research_pipeline": "N01",
    # N02 Marketing
    "tagline": "N02", "social_publisher": "N02",
    # N03 Builder (45 kinds)
    "agent": "N03", "agent_card": "N03", "agent_package": "N03",
    "axiom": "N03", "chain": "N03", "component_map": "N03",
    "constraint_spec": "N03", "context_window_config": "N03",
    "dag": "N03", "decision_record": "N03", "diagram": "N03",
    "enum_de": "N03", "fallback_chain": "N03", "formatter": "N03",
    "guardrail": "N03", "handoff_protocol": "N03", "input_schema": "N03",
    "instruction": "N03", "interface": "N03", "invariant": "N03",
    "landing_page": "N03", "lens": "N03", "lifecycle_rule": "N03",
    "memory_scope": "N03", "mental_model": "N03", "model_card": "N03",
    "naming_rule": "N03", "output_validator": "N03", "parser": "N03",
    "pattern": "N03", "prompt_template": "N03", "prompt_version": "N03",
    "quality_gate": "N03", "reasoning_trace": "N03", "response_format": "N03",
    "router": "N03", "skill": "N03", "supervisor": "N03",
    "system_prompt": "N03", "type_de": "N03", "validation_schema": "N03",
    "validator": "N03", "workflow": "N03", "workflow_primitive": "N03",
    "action_prompt": "N03",
    # N04 Knowledge (21 kinds)
    "chunk_strategy": "N04", "citation": "N04", "compression_config": "N04",
    "context_doc": "N04", "document_loader": "N04", "embedder_provider": "N04",
    "embedding_config": "N04", "entity_memory": "N04", "few_shot_example": "N04",
    "glossary_entry": "N04", "knowledge_card": "N04", "knowledge_index": "N04",
    "learning_record": "N04", "memory_summary": "N04", "memory_type": "N04",
    "rag_source": "N04", "retriever": "N04", "retriever_config": "N04",
    "runtime_state": "N04", "session_state": "N04", "vector_store": "N04",
    # N05 Operations (45 kinds)
    "api_client": "N05", "audio_tool": "N05", "benchmark": "N05",
    "boot_config": "N05", "browser_tool": "N05", "bugloop": "N05",
    "cli_tool": "N05", "code_executor": "N05", "computer_use": "N05",
    "daemon": "N05", "db_connector": "N05", "e2e_eval": "N05",
    "effort_profile": "N05", "env_config": "N05", "eval_dataset": "N05",
    "feature_flag": "N05", "function_de": "N05", "golden_test": "N05",
    "hook": "N05", "hook_config": "N05", "llm_judge": "N05",
    "mcp_server": "N05", "model_provider": "N05", "multi_modal_config": "N05",
    "notifier": "N05", "optimizer": "N05", "path_config": "N05",
    "permission": "N05", "plugin": "N05", "prompt_cache": "N05",
    "rate_limit_config": "N05", "red_team_eval": "N05", "regression_check": "N05",
    "reward_signal": "N05", "runtime_rule": "N05", "scoring_rubric": "N05",
    "search_tool": "N05", "secret_config": "N05", "session_backend": "N05",
    "smoke_eval": "N05", "supabase_data_layer": "N05", "toolkit": "N05",
    "trace_config": "N05", "vision_tool": "N05", "webhook": "N05",
    # N06 Commercial
    "content_monetization": "N06",
    # N07 Orchestration (6 kinds)
    "checkpoint": "N07", "dispatch_rule": "N07", "handof": "N07",
    "schedule": "N07", "signal": "N07", "spawn_config": "N07",
}

# Fallback: pillar -> nucleus for unmapped kinds (Wave 2/3 new kinds)
PILLAR_NUCLEUS_FALLBACK = {
    "P01": "N04", "P02": "N03", "P03": "N03", "P04": "N05",
    "P05": "N03", "P06": "N03", "P07": "N05", "P08": "N03",
    "P09": "N05", "P10": "N04", "P11": "N05", "P12": "N07",
}

# Override fallbacks for specific new kinds from spec_mission_100pct_coverage
WAVE_KIND_OVERRIDES = {
    # Safety & Governance -> N05 (operations/governance)
    "threat_model": "N05", "safety_policy": "N05", "content_filter": "N05",
    "bias_audit": "N05", "compliance_framework": "N05", "privacy_filter": "N05",
    "access_control": "N05", "audit_log": "N05", "incident_response": "N05",
    "adversarial_test": "N05", "model_drift": "N05", "explainability": "N05",
    "fairness_metric": "N05", "robustness_test": "N05",
    # Voice & Media -> N05
    "voice_pipeline": "N05", "video_pipeline": "N05", "image_pipeline": "N05",
    "tts_config": "N05", "stt_config": "N05", "media_processor": "N05",
    # Reasoning & Learning -> N03
    "reasoning_strategy": "N03", "planning_strategy": "N03",
    "thinking_config": "N03", "action_paradigm": "N03",
    "dual_loop_architecture": "N03", "collaboration_pattern": "N03",
    # RL & Search -> N01
    "rl_algorithm": "N01", "reward_model": "N01", "search_strategy": "N01",
    # Agent Architecture -> N03
    "agent_profile": "N03",
    # Data & Lineage -> N04
    "data_lineage": "N04", "data_catalog": "N04",
    "schema_evolution": "N04", "etl_pipeline": "N04",
    # Commercial -> N06
    "pricing_model": "N06", "subscription_plan": "N06",
    "affiliate_config": "N06", "payment_gateway": "N06",
}

NUCLEUS_NAMES = {
    "N01": "intelligence", "N02": "marketing", "N03": "engineering",
    "N04": "knowledge", "N05": "operations", "N06": "commercial",
    "N07": "admin",
}

# Instruction template pools (rotated per extraction)
INSTRUCTION_TEMPLATES = {
    "construction": [
        "Build a {kind} artifact for the domain: {domain}",
        "Create a CEX {kind} following the 8F pipeline",
        "Produce a {kind} artifact with pillar {pillar}",
        "Generate a complete {kind} with proper frontmatter and body",
    ],
    "process": [
        "What are the steps to produce a {kind}?",
        "Describe the 3-phase pipeline for building {kind} artifacts",
        "How does the {kind}-builder work? Walk me through the process.",
        "Explain the construction rules for {kind} artifacts",
    ],
    "evaluation": [
        "What quality gates must a {kind} pass?",
        "List the HARD and SOFT gates for {kind} artifacts",
        "How is a {kind} artifact evaluated for quality?",
        "Describe the scoring criteria for {kind}",
    ],
    "identity": [
        "Write a system prompt for a {kind}-builder agent",
        "What identity should a {kind}-builder adopt?",
        "Describe the role and capabilities of {kind}-builder",
    ],
    "template": [
        "Show the output template for a {kind} artifact",
        "What structure should a {kind} artifact follow?",
        "Provide the standard template for {kind}",
    ],
    "schema": [
        "What fields are required for {kind}?",
        "Describe the schema definition for {kind}",
        "List the frontmatter and body requirements for {kind}",
    ],
    "architecture": [
        "Describe the architecture of {kind}",
        "What components make up the {kind} system?",
        "How does {kind} integrate with other CEX artifacts?",
    ],
    "collaboration": [
        "How does {kind}-builder collaborate in crews?",
        "What other builders does {kind}-builder work with?",
        "Describe the collaboration patterns for {kind}",
    ],
    "manifest": [
        "Describe the {kind}-builder capabilities",
        "What is the identity and purpose of {kind}-builder?",
    ],
    "knowledge": [
        "Explain what a {kind} is in the CEX system",
        "When should I use {kind} vs alternatives?",
        "What are the patterns and anti-patterns for {kind}?",
    ],
}


@dataclass
class TrainingPair:
    instruction: str
    input: str
    output: str
    kind: str
    nucleus: str
    iso_type: str
    pair_category: str
    token_estimate: int


def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token."""
    return len(text) // 4


def load_kinds_meta() -> dict[str, Any]:
    if not KINDS_META.exists():
        print("[FAIL] kinds_meta.json not found", file=sys.stderr)
        sys.exit(1)
    return json.loads(KINDS_META.read_text(encoding="utf-8"))


def resolve_nucleus(kind: str, meta: dict[str, Any]) -> str:
    """Resolve kind -> nucleus using 3-level lookup."""
    if kind in KIND_TO_NUCLEUS:
        return KIND_TO_NUCLEUS[kind]
    if kind in WAVE_KIND_OVERRIDES:
        return WAVE_KIND_OVERRIDES[kind]
    pillar = meta.get("pillar", "P03")
    return PILLAR_NUCLEUS_FALLBACK.get(pillar, "N03")


def find_builder_dir(kind: str) -> Path | None:
    """Find builder directory for a kind."""
    hyphen = kind.replace("_", "-")
    d = BUILDERS_DIR / f"{hyphen}-builder"
    return d if d.exists() else None


def read_iso(builder_dir: Path, iso_type: str, kind: str) -> str | None:
    """Read a builder ISO file. Returns content or None."""
    fname = f"bld_{iso_type}_{kind}.md"
    fpath = builder_dir / fname
    if not fpath.exists():
        # Try hyphenated
        fname2 = f"bld_{iso_type}_{kind.replace('_', '-')}.md"
        fpath = builder_dir / fname2
    if not fpath.exists():
        return None
    try:
        return fpath.read_text(encoding="utf-8")
    except Exception:
        return None


def pick_instruction(category: str, kind: str, meta: dict[str, Any]) -> str:
    """Pick a random instruction template and fill it."""
    templates = INSTRUCTION_TEMPLATES.get(category, ["Describe {kind}"])
    tmpl = random.choice(templates)
    return tmpl.format(
        kind=kind,
        domain=meta.get("description", kind),
        pillar=meta.get("pillar", "P03"),
    )


def build_context(kind: str, meta: dict[str, Any]) -> str:
    """Build the input/context field from meta."""
    parts = [
        f"Kind: {kind}",
        f"Pillar: {meta.get('pillar', 'unknown')}",
        f"LLM Function: {meta.get('llm_function', 'unknown')}",
        f"Description: {meta.get('description', '')}",
        f"Max Bytes: {meta.get('max_bytes', 0)}",
        f"Boundary: {meta.get('boundary', '')}",
    ]
    return "\n".join(parts)


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter from markdown."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].strip()
    return text.strip()


def extract_from_iso(
    builder_dir: Path,
    iso_type: str,
    kind: str,
    meta: dict[str, Any],
    category: str,
) -> TrainingPair | None:
    """Generic extractor: read ISO, build pair."""
    content = read_iso(builder_dir, iso_type, kind)
    if not content or len(content) < 100:
        return None
    body = strip_frontmatter(content)
    if len(body) < 50:
        return None
    # Filter out TODO/placeholder content
    if "> TODO:" in body or "INSERT " in body.upper():
        return None
    ctx = build_context(kind, meta)
    nucleus = resolve_nucleus(kind, meta)
    tokens = estimate_tokens(body)
    if tokens > 4096:
        body = body[:16000]  # ~4K tokens max for QLoRA
        tokens = 4096
    return TrainingPair(
        instruction=pick_instruction(category, kind, meta),
        input=ctx,
        output=body,
        kind=kind,
        nucleus=nucleus,
        iso_type=iso_type,
        pair_category=category,
        token_estimate=tokens,
    )


def extract_from_knowledge_card(kind: str, meta: dict[str, Any]) -> list[TrainingPair]:
    """Extract pairs from P01 knowledge cards."""
    kc_path = KC_DIR / f"kc_{kind}.md"
    if not kc_path.exists():
        return []
    try:
        content = kc_path.read_text(encoding="utf-8")
    except Exception:
        return []
    body = strip_frontmatter(content)
    if len(body) < 100:
        return []
    nucleus = resolve_nucleus(kind, meta)
    pairs = []
    # Full KC pair
    pairs.append(TrainingPair(
        instruction=pick_instruction("knowledge", kind, meta),
        input=build_context(kind, meta),
        output=body[:16000],
        kind=kind,
        nucleus=nucleus,
        iso_type="knowledge_card_p01",
        pair_category="knowledge",
        token_estimate=estimate_tokens(body[:16000]),
    ))
    return pairs


def extract_all_pairs(kind: str, meta: dict[str, Any]) -> list[TrainingPair]:
    """Extract all training pairs for a single kind."""
    pairs = []
    builder_dir = find_builder_dir(kind)
    if not builder_dir:
        return pairs

    # High-value ISOs
    iso_map = [
        ("examples", "construction"),
        ("instruction", "process"),
        ("quality_gate", "evaluation"),
        ("system_prompt", "identity"),
        ("output_template", "template"),
        # Medium-value
        ("schema", "schema"),
        ("architecture", "architecture"),
        ("collaboration", "collaboration"),
        ("manifest", "manifest"),
        # Low-value (still useful)
        ("memory", "knowledge"),
        ("knowledge_card", "knowledge"),
        ("config", "schema"),
        ("tools", "architecture"),
    ]

    for iso_type, category in iso_map:
        pair = extract_from_iso(builder_dir, iso_type, kind, meta, category)
        if pair:
            pairs.append(pair)

    # P01 knowledge card (separate from builder KC)
    kc_pairs = extract_from_knowledge_card(kind, meta)
    pairs.extend(kc_pairs)

    return pairs


def extract_supplementary(nucleus: str) -> list[TrainingPair]:
    """Extract supplementary pairs from nucleus directories for thin nuclei."""
    pairs = []
    nuc_lower = nucleus.lower()
    nuc_name = NUCLEUS_NAMES.get(nucleus, "unknown")
    nuc_dir = ROOT / f"{nucleus}_{nuc_name}"

    if not nuc_dir.exists():
        return pairs

    # Scan markdown files in nucleus directory
    md_files = list(nuc_dir.rglob("*.md"))
    for f in md_files[:50]:  # Cap at 50 files
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue
        body = strip_frontmatter(content)
        if len(body) < 200:
            continue
        if "> TODO:" in body:
            continue
        fname = f.stem
        pairs.append(TrainingPair(
            instruction=f"Analyze the {fname} artifact from {nucleus}",
            input=f"Nucleus: {nucleus}\nDomain: {nuc_name}\nFile: {f.name}",
            output=body[:16000],
            kind="supplementary",
            nucleus=nucleus,
            iso_type="nucleus_artifact",
            pair_category="knowledge",
            token_estimate=estimate_tokens(body[:16000]),
        ))
    return pairs


def group_by_nucleus(pairs: list[TrainingPair]) -> dict[str, list[TrainingPair]]:
    """Group training pairs by target nucleus."""
    groups = {}
    for p in pairs:
        nuc = p.nucleus
        if nuc not in groups:
            groups[nuc] = []
        groups[nuc].append(p)
    return groups


def write_jsonl(pairs: list[TrainingPair], output_path: Path) -> int:
    """Write Alpaca-format JSONL."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for p in pairs:
            record = {
                "instruction": p.instruction,
                "input": p.input,
                "output": p.output,
            }
            f.write(json.dumps(record, ensure_ascii=True) + "\n")
    return output_path.stat().st_size


def print_stats(grouped: dict[str, list[TrainingPair]], total_pairs: int) -> None:
    """Print per-nucleus statistics."""
    print(f"\n{'='*60}")
    print("CEX FINE-TUNE DATASET SUMMARY")
    print(f"{'='*60}")
    print(f"Total pairs: {total_pairs}")
    print(f"Nuclei with data: {len(grouped)}/7")
    print()
    print(f"{'Nucleus':<8} {'Kinds':<8} {'Pairs':<8} {'Avg Tok':<10} {'Category Distribution'}")
    print(f"{'-'*8} {'-'*8} {'-'*8} {'-'*10} {'-'*30}")

    for nuc in sorted(grouped.keys()):
        pairs = grouped[nuc]
        kinds = len(set(p.kind for p in pairs))
        avg_tok = sum(p.token_estimate for p in pairs) // max(len(pairs), 1)
        cats = {}
        for p in pairs:
            cats[p.pair_category] = cats.get(p.pair_category, 0) + 1
        cat_str = ", ".join(f"{k}:{v}" for k, v in sorted(cats.items()))
        print(f"{nuc:<8} {kinds:<8} {len(pairs):<8} {avg_tok:<10} {cat_str}")

    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="CEX Fine-Tune Dataset Builder v2")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR),
                        help="Output directory for per-nucleus JSONL files")
    parser.add_argument("--stats", action="store_true",
                        help="Print statistics only, don't write files")
    parser.add_argument("--nucleus", default=None,
                        help="Export only one nucleus (e.g. N03)")
    parser.add_argument("--include-supplementary", action="store_true",
                        help="Add supplementary data from nucleus directories")
    parser.add_argument("--min-output-tokens", type=int, default=25,
                        help="Min output tokens to include a pair (default: 25)")
    parser.add_argument("--max-output-tokens", type=int, default=4096,
                        help="Max output tokens per pair (default: 4096)")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for instruction template rotation")
    args = parser.parse_args()

    random.seed(args.seed)
    kinds_meta = load_kinds_meta()
    print(f"[INFO] Loaded {len(kinds_meta)} kinds from kinds_meta.json")

    all_pairs = []
    kinds_processed = 0
    kinds_with_data = 0

    for kind, meta in sorted(kinds_meta.items()):
        kinds_processed += 1
        pairs = extract_all_pairs(kind, meta)
        # Filter by token bounds
        pairs = [p for p in pairs
                 if args.min_output_tokens <= p.token_estimate <= args.max_output_tokens]
        if pairs:
            kinds_with_data += 1
        all_pairs.extend(pairs)

    print(f"[INFO] Processed {kinds_processed} kinds, {kinds_with_data} with data")
    print(f"[INFO] Extracted {len(all_pairs)} training pairs from builder ISOs + KCs")

    # Group by nucleus
    grouped = group_by_nucleus(all_pairs)

    # Supplementary for thin nuclei
    if args.include_supplementary:
        for nuc in ["N01", "N02", "N06"]:
            supp = extract_supplementary(nuc)
            supp = [p for p in supp
                    if args.min_output_tokens <= p.token_estimate <= args.max_output_tokens]
            if supp:
                if nuc not in grouped:
                    grouped[nuc] = []
                grouped[nuc].extend(supp)
                all_pairs.extend(supp)
                print(f"[INFO] Added {len(supp)} supplementary pairs for {nuc}")

    # Filter by nucleus if specified
    if args.nucleus:
        nuc = args.nucleus.upper()
        grouped = {k: v for k, v in grouped.items() if k == nuc}

    print_stats(grouped, len(all_pairs))

    if args.stats:
        return

    # Write per-nucleus JSONL files
    output_dir = Path(args.output_dir)
    total_bytes = 0
    for nuc in sorted(grouped.keys()):
        pairs = grouped[nuc]
        nuc_lower = nuc.lower()
        out_path = output_dir / f"ft_{nuc_lower}.jsonl"
        size = write_jsonl(pairs, out_path)
        total_bytes += size
        print(f"[OK] {out_path}: {len(pairs)} pairs, {size:,} bytes")

    # Also write combined file
    combined_path = output_dir / "ft_all.jsonl"
    combined_size = write_jsonl(all_pairs, combined_path)
    print(f"[OK] {combined_path}: {len(all_pairs)} pairs, {combined_size:,} bytes")
    print(f"\n[OK] Total: {len(all_pairs)} pairs across {len(grouped)} nuclei")
    print(f"[OK] Total size: {total_bytes + combined_size:,} bytes")


if __name__ == "__main__":
    main()
