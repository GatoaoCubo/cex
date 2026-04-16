"""
Wave 1-3: Generate 13 ISOs per kind using Ollama qwen3:14b.
Structural template from Python, domain content from LLM.
Usage:
  python _tools/wave1_builder_gen.py                     # Wave 1 (16 kinds)
  python _tools/wave1_builder_gen.py --wave 2            # Wave 2 (18 kinds)
  python _tools/wave1_builder_gen.py --wave 3            # Wave 3 (18 kinds)
  python _tools/wave1_builder_gen.py --wave all          # All 52 kinds
  python _tools/wave1_builder_gen.py --kind threat_model # Single kind
"""
import json, os, sys, time, argparse, requests
from datetime import date
from pathlib import Path
from typing import Any

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:26b"
META_PATH = ".cex/kinds_meta.json"
BUILDERS_DIR = "archetypes/builders"
TODAY = date.today().isoformat()

# Wave 1: Safety(6) + Reasoning(5) + Agent Architecture(5) = 16
WAVE1_KINDS = [
    "threat_model", "safety_policy", "content_filter",
    "bias_audit", "compliance_framework", "incident_report",
    "reasoning_strategy", "rl_algorithm", "reward_model",
    "search_strategy", "thinking_config",
    "agent_profile", "planning_strategy", "action_paradigm",
    "collaboration_pattern", "dual_loop_architecture",
]

# Wave 2: Voice(7) + Code Agents(5) + ML Lifecycle(6) = 18
WAVE2_KINDS = [
    "voice_pipeline", "realtime_session", "vad_config",
    "tts_provider", "stt_provider", "prosody_config", "transport_config",
    "edit_format", "sandbox_config", "repo_map",
    "diff_strategy", "agent_computer_interface",
    "training_method", "model_architecture", "dataset_card",
    "model_registry", "experiment_tracker", "quantization_config",
]

# Wave 3: Eval(5) + RAG(3) + Memory(4) + Prompt(3) + Workflow(2) + Self(1) = 18
WAVE3_KINDS = [
    "benchmark_suite", "judge_config", "eval_metric",
    "eval_framework", "trajectory_eval",
    "reranker_config", "graph_rag_config", "agentic_rag",
    "memory_architecture", "procedural_memory",
    "consolidation_policy", "memory_benchmark",
    "prompt_technique", "prompt_optimizer", "multimodal_prompt",
    "workflow_node", "visual_workflow",
    "self_improvement_loop",
]

WAVE_MAP = {
    "1": WAVE1_KINDS,
    "2": WAVE2_KINDS,
    "3": WAVE3_KINDS,
    "all": WAVE1_KINDS + WAVE2_KINDS + WAVE3_KINDS,
}

# ISO templates: (filename_pattern, kind_field, pillar, llm_function, purpose_template)
ISO_SPECS = [
    ("bld_manifest_{k}.md", "type_builder", "{pillar}", "BECOME",
     "Builder identity, capabilities, routing for {kind}"),
    ("bld_instruction_{k}.md", "instruction", "P03", "REASON",
     "Step-by-step production process for {kind}"),
    ("bld_system_prompt_{k}.md", "system_prompt", "P03", "BECOME",
     "System prompt defining {kind}-builder persona and rules"),
    ("bld_schema_{k}.md", "schema", "P06", "CONSTRAIN",
     "Formal schema -- SINGLE SOURCE OF TRUTH for {kind}"),
    ("bld_quality_gate_{k}.md", "quality_gate", "P11", "GOVERN",
     "Quality gate with HARD and SOFT scoring for {kind}"),
    ("bld_output_template_{k}.md", "output_template", "P05", "PRODUCE",
     "Template with vars for {kind} production"),
    ("bld_examples_{k}.md", "examples", "P07", "GOVERN",
     "Golden and anti-examples of {kind} artifacts"),
    ("bld_knowledge_card_{k}.md", "knowledge_card", "P01", "INJECT",
     "Domain knowledge for {kind} production"),
    ("bld_architecture_{k}.md", "architecture", "P08", "CONSTRAIN",
     "Component map of {kind} -- inventory, dependencies"),
    ("bld_collaboration_{k}.md", "collaboration", "P12", "COLLABORATE",
     "How {kind}-builder works in crews with other builders"),
    ("bld_config_{k}.md", "config", "P09", "CONSTRAIN",
     "Naming, paths, limits for {kind} production"),
    ("bld_memory_{k}.md", "learning_record", "P10", "INJECT",
     "Learned patterns and pitfalls for {kind} construction"),
    ("bld_tools_{k}.md", "tools", "P04", "CALL",
     "Tools available for {kind} production"),
]


def ollama_generate(prompt: str, max_tokens: int = 2048) -> str | None:
    """Call Ollama qwen3:14b with /no_think for fast structured output."""
    for attempt in range(3):
        try:
            resp = requests.post(OLLAMA_URL, json={
                "model": MODEL,
                "prompt": prompt + "\n/no_think",
                "stream": False,
                "options": {"num_predict": max_tokens, "temperature": 0.3}
            }, timeout=600)
            resp.raise_for_status()
            text = resp.json().get("response", "").strip()
            # Strip thinking tags if present
            if "<think>" in text:
                import re
                text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
            if len(text) > 50:
                return text
            print(f"  [WARN] Short response ({len(text)} chars), retry {attempt+1}")
        except Exception as e:
            print(f"  [WARN] Ollama error (attempt {attempt+1}): {e}")
            time.sleep(2)
    return None


def load_kind_meta(kind: str) -> dict[str, Any]:
    """Load kind metadata from the shared registry."""
    with open(META_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get(kind, {})


def build_manifest_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the manifest-generation prompt for one kind."""
    return f"""You are generating a builder manifest for CEX kind "{kind}".
The kind belongs to pillar {meta['pillar']} with llm_function {meta['llm_function']}.
Description: {meta['description']}
Boundary: {meta['boundary']}

Generate the body content (NO frontmatter, just markdown) for a builder manifest with these sections:
## Identity
(2-3 sentences: what this builder specializes in, what domain knowledge it has)
## Capabilities
(5 numbered capabilities this builder has)
## Routing
(keywords and triggers for when to invoke this builder)
## Crew Role
(1 paragraph: role in a team, what it answers, what it does NOT handle)

Be specific to {kind}. Use industry terminology. ASCII only. Under 60 lines."""


def build_instruction_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the instructions-generation prompt for one kind."""
    return f"""Generate production instructions for building a "{kind}" artifact.
Kind: {kind}, Pillar: {meta['pillar']}, Function: {meta['llm_function']}
Description: {meta['description']}

Generate markdown body (NO frontmatter) with:
## Phase 1: RESEARCH
(6 numbered steps specific to {kind})
## Phase 2: COMPOSE
(9 numbered steps for writing the artifact, referencing SCHEMA.md and OUTPUT_TEMPLATE.md)
## Phase 3: VALIDATE
(5 numbered validation steps with checkbox format)

Be domain-specific. ASCII only. Under 70 lines."""


def build_system_prompt_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the system-prompt-generation prompt for one kind."""
    return f"""Generate a system prompt for the {kind}-builder agent.
Kind: {kind}, Pillar: {meta['pillar']}, Function: {meta['llm_function']}
Description: {meta['description']}
Boundary: {meta['boundary']}

Generate markdown body (NO frontmatter) with:
## Identity
(1 paragraph defining who this agent is and what it produces)
## Rules
### Scope
(3 rules about what it produces and what it does NOT)
### Quality
(5 rules about quality requirements specific to {kind})

Be specific. Use industry terms. ASCII only. Under 50 lines."""


def build_schema_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the schema-generation prompt for one kind."""
    nm = meta.get("naming", "").replace("{{name}}", "slug")
    return f"""Generate a formal schema for CEX kind "{kind}".
Pillar: {meta['pillar']}, Naming: {meta['naming']}, Max bytes: {meta['max_bytes']}

Generate markdown body (NO frontmatter) with:
## Frontmatter Fields
### Required
(Table: Field | Type | Required | Default | Notes -- at least 10 fields including id, kind, pillar, title, version, created, updated, author, domain, quality, tags, tldr, plus 2-4 domain-specific fields)
### Recommended
(Table: 3-4 optional fields)
## ID Pattern
(Regex pattern based on naming convention)
## Body Structure (required sections)
(4-6 numbered sections specific to {kind})
## Constraints
(5-6 bullet constraints)

ASCII only. Under 80 lines."""


def build_quality_gate_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the quality-gate-generation prompt for one kind."""
    return f"""Generate a quality gate for CEX kind "{kind}".
Pillar: {meta['pillar']}, Description: {meta['description']}

Generate markdown body (NO frontmatter) with:
## Definition
(Table: metric, threshold, operator, scope)
## HARD Gates
(Table: ID | Check | Fail Condition -- 7-10 gates including H01-H03 standard: YAML valid, ID matches pattern, kind matches)
## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide -- 8-11 dimensions summing to 1.00)
## Actions
(Table: Score | Action -- 4 tiers: GOLDEN >=9.5, PUBLISH >=8.0, REVIEW >=7.0, REJECT <7.0)
## Bypass
(Table: conditions, approver, audit trail)

ASCII only. Under 80 lines."""


def build_output_template_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the output-template-generation prompt for one kind."""
    pfx = meta.get("naming", "").split("_")[0] + "_" + meta.get("naming", "").split("_")[1] if "_" in meta.get("naming", "") else "p00_x"
    return f"""Generate an output template for CEX kind "{kind}".
Pillar: {meta['pillar']}, Naming: {meta['naming']}

Generate markdown body (NO frontmatter) with a YAML code block showing:
- All required frontmatter fields with {{{{variable}}}} placeholders
- Body sections with {{{{placeholder}}}} content
Follow the naming pattern from the schema.

ASCII only. Under 60 lines."""


def build_examples_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the examples-generation prompt for one kind."""
    return f"""Generate golden and anti-examples for CEX kind "{kind}".
Description: {meta['description']}
Boundary: {meta['boundary']}

Generate markdown body (NO frontmatter) with:
## Golden Example
(A complete, high-quality example of a {kind} artifact with frontmatter and body, showing best practices)
## Anti-Example 1: {{common mistake}}
(Show a BAD example with ## Why it fails explanation)
## Anti-Example 2: {{another mistake}}
(Show another BAD example with ## Why it fails explanation)

ASCII only. Under 120 lines."""


def build_knowledge_card_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the knowledge-card-generation prompt for one kind."""
    return f"""Generate domain knowledge for building "{kind}" artifacts.
Description: {meta['description']}
Boundary: {meta['boundary']}

Generate markdown body (NO frontmatter) with:
## Domain Overview
(2-3 paragraphs of industry context for {kind})
## Key Concepts
(Table: Concept | Definition | Source -- 8-12 rows)
## Industry Standards
(List of relevant standards, frameworks, or papers)
## Common Patterns
(4-6 numbered patterns with 1-line descriptions)
## Pitfalls
(4-5 common mistakes to avoid)

Use real industry terminology and references. ASCII only. Under 90 lines."""


def build_architecture_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the architecture-generation prompt for one kind."""
    return f"""Generate an architecture document for the {kind}-builder.
Kind: {kind}, Pillar: {meta['pillar']}

Generate markdown body (NO frontmatter) with:
## Component Inventory
(Table: Name | Role | Owner | Status -- 5-8 components)
## Dependencies
(Table: From | To | Type -- 4-6 dependencies)
## Architectural Position
(1 paragraph placing {kind} in the CEX ecosystem)

ASCII only. Under 50 lines."""


def build_collaboration_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the collaboration-spec prompt for one kind."""
    return f"""Generate a collaboration spec for {kind}-builder.
Kind: {kind}, Boundary: {meta['boundary']}

Generate markdown body (NO frontmatter) with:
## Crew Role
(What this builder does in a team)
## Receives From
(Table: Builder | What | Format -- 3-4 rows)
## Produces For
(Table: Builder | What | Format -- 3-4 rows)
## Boundary
(What this builder does NOT do and who handles it instead)

ASCII only. Under 45 lines."""


def build_config_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the config-generation prompt for one kind."""
    return f"""Generate a config for {kind}-builder.
Naming: {meta['naming']}, Max bytes: {meta['max_bytes']}, Pillar: {meta['pillar']}

Generate markdown body (NO frontmatter) with:
## Naming Convention
(Pattern and examples)
## Paths
(Where artifacts are stored)
## Limits
(max_bytes, max_turns, effort level)
## Hooks
(pre_build, post_build, on_error, on_quality_fail -- all null for now)

ASCII only. Under 40 lines."""


def build_memory_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the learning-record-generation prompt for one kind."""
    return f"""Generate a learning record (memory) for {kind}-builder.
Description: {meta['description']}
Boundary: {meta['boundary']}

Generate markdown body (NO frontmatter) with:
## Observation
(2-3 sentences about common issues when building {kind} artifacts)
## Pattern
(2-3 sentences about what works well)
## Evidence
(1-2 sentences referencing reviewed artifacts)
## Recommendations
(4-5 bullet points)

ASCII only. Under 40 lines."""


def build_tools_prompt(kind: str, meta: dict[str, Any]) -> str:
    """Build the tools-inventory-generation prompt for one kind."""
    return f"""Generate a tools inventory for {kind}-builder.
Kind: {kind}

Generate markdown body (NO frontmatter) with:
## Production Tools
(Table: Tool | Purpose | When -- 4-6 CEX tools like cex_compile.py, cex_score.py, cex_retriever.py, cex_doctor.py)
## Validation Tools
(Table: Tool | Purpose | When -- 3-4 tools)
## External References
(2-3 relevant external tools or frameworks)

ASCII only. Under 40 lines."""


# Map ISO index to prompt generator
PROMPT_GENERATORS = [
    build_manifest_prompt,
    build_instruction_prompt,
    build_system_prompt_prompt,
    build_schema_prompt,
    build_quality_gate_prompt,
    build_output_template_prompt,
    build_examples_prompt,
    build_knowledge_card_prompt,
    build_architecture_prompt,
    build_collaboration_prompt,
    build_config_prompt,
    build_memory_prompt,
    build_tools_prompt,
]


def generate_frontmatter(
    iso_spec: tuple[str, str, str, str, str], kind: str, meta: dict[str, Any]
) -> str:
    """Generate YAML frontmatter for an ISO file."""
    fname_pattern, iso_kind, pillar_tpl, llm_func, purpose_tpl = iso_spec
    pillar = pillar_tpl.format(pillar=meta["pillar"])
    purpose = purpose_tpl.format(kind=kind)
    k_slug = kind.replace("_", " ").title().replace(" ", "")

    # ID pattern
    if iso_kind == "type_builder":
        iso_id = f"{kind.replace('_', '-')}-builder"
    elif iso_kind == "quality_gate":
        iso_id = f"{meta['pillar'].lower()}_qg_{kind}"
    elif iso_kind == "system_prompt":
        iso_id = f"p03_sp_{kind}_builder"
    elif iso_kind == "learning_record":
        iso_id = f"p10_lr_{kind}_builder"
    else:
        iso_id = f"bld_{iso_kind}_{kind}"

    title_kind = kind.replace("_", " ").title()

    fm = f"""---
kind: {iso_kind}
id: {iso_id}
pillar: {pillar}
llm_function: {llm_func}
purpose: {purpose}
quality: null
title: "{iso_kind.replace('_', ' ').title()} {title_kind}"
version: "1.0.0"
author: wave1_builder_gen
tags: [{kind}, builder, {iso_kind}]
tldr: "{purpose}"
domain: "{kind} construction"
created: "{TODAY}"
updated: "{TODAY}"
density_score: 0.85
---"""
    return fm


def generate_iso(
    kind: str, meta: dict[str, Any], iso_idx: int, dry_run: bool = False
) -> str:
    """Generate a single ISO file for a kind."""
    iso_spec = ISO_SPECS[iso_idx]
    fname = iso_spec[0].format(k=kind)
    builder_dir = os.path.join(BUILDERS_DIR, f"{kind.replace('_', '-')}-builder")

    fpath = os.path.join(builder_dir, fname)
    if os.path.exists(fpath) and not dry_run:
        # Check if it's a TODO placeholder that needs regeneration
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        if "> TODO:" not in content:
            return "SKIP"
        # Fall through to regenerate

    frontmatter = generate_frontmatter(iso_spec, kind, meta)
    prompt_fn = PROMPT_GENERATORS[iso_idx]
    prompt = prompt_fn(kind, meta)

    if dry_run:
        print(f"  [DRY] {fname}")
        return "DRY"

    body = ollama_generate(prompt)
    if not body:
        # Fallback: minimal placeholder
        body = f"# {iso_spec[1].replace('_', ' ').title()}: {kind}\n\n> TODO: Generate content for {kind} {iso_spec[1]}\n"

    content = frontmatter + "\n\n" + body + "\n"

    os.makedirs(builder_dir, exist_ok=True)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    return "OK"


def main() -> None:
    """Generate the requested wave, kind, or ISO set from CLI arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", help="Generate for specific kind only")
    parser.add_argument("--wave", default="1", help="Wave number: 1, 2, 3, or all")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--fix", action="store_true", help="Regenerate ISOs with TODO placeholders")
    parser.add_argument("--iso", type=int, help="Generate specific ISO index only (0-12)")
    args = parser.parse_args()

    if args.kind:
        kinds = [args.kind]
    else:
        kinds = WAVE_MAP.get(args.wave, WAVE1_KINDS)
        print(f"[INFO] Wave {args.wave}: {len(kinds)} kinds")

    total = 0
    created = 0
    skipped = 0
    failed = 0

    for kind in kinds:
        meta = load_kind_meta(kind)
        if not meta:
            print(f"[SKIP] {kind} not in kinds_meta.json")
            continue

        print(f"\n=== {kind} ({meta['pillar']}/{meta['llm_function']}) ===")
        builder_dir = os.path.join(BUILDERS_DIR, f"{kind.replace('_', '-')}-builder")

        iso_range = [args.iso] if args.iso is not None else range(13)

        for i in iso_range:
            total += 1
            fname = ISO_SPECS[i][0].format(k=kind)
            result = generate_iso(kind, meta, i, args.dry_run)

            if result == "OK":
                created += 1
                print(f"  [OK] {fname}")
            elif result == "SKIP":
                skipped += 1
                print(f"  [SKIP] {fname} (exists)")
            elif result == "DRY":
                pass
            else:
                failed += 1
                print(f"  [FAIL] {fname}")

    print(f"\n{'='*60}")
    print(f"Total: {total} | Created: {created} | Skipped: {skipped} | Failed: {failed}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
