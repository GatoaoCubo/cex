#!/usr/bin/env python3
"""Generate a 13-file builder scaffold from CEX type metadata."""

from __future__ import annotations

import argparse
import re
import shutil
from datetime import date
from pathlib import Path
from typing import Any

import yaml

EXPECTED_FILES = [
    "MANIFEST.md",
    "SYSTEM_PROMPT.md",
    "KNOWLEDGE.md",
    "INSTRUCTIONS.md",
    "TOOLS.md",
    "OUTPUT_TEMPLATE.md",
    "SCHEMA.md",
    "EXAMPLES.md",
    "ARCHITECTURE.md",
    "CONFIG.md",
    "MEMORY.md",
    "QUALITY_GATES.md",
    "COLLABORATION.md",
]

LP_TO_DIR = {
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


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def dump_frontmatter(data: dict[str, Any]) -> str:
    return f"---\n{yaml.safe_dump(data, sort_keys=False, allow_unicode=False).strip()}\n---\n\n"


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def builder_slug(type_name: str) -> str:
    return type_name.replace("_", "-") + "-builder"


def template_block(template_text: str, fields: list[str]) -> str:
    if template_text:
        return template_text.strip()
    return yaml.safe_dump({field: f"{{{{{field}}}}}" for field in (fields or ["id", "kind", "lp"])}, sort_keys=False, allow_unicode=False).strip()


def extract_template_keys(block: str) -> list[str]:
    keys: list[str] = []
    for line in block.splitlines():
        m = re.match(r'^\s*"?([A-Za-z_][A-Za-z0-9_]*)"?\s*:', line)
        if m and m.group(1) not in keys:
            keys.append(m.group(1))
    return keys


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a new CEX builder.")
    parser.add_argument("--type", required=True, dest="artifact_type")
    parser.add_argument("--lp", required=True)
    parser.add_argument("--output-root", default="archetypes/builders")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    lp_dir = LP_TO_DIR[args.lp]
    schema_path = repo_root / lp_dir / "_schema.yaml"
    schema = load_yaml(schema_path)
    type_spec = (schema.get("kinds") or {}).get(args.artifact_type)
    if not type_spec:
        raise SystemExit(f"type `{args.artifact_type}` not found in {schema_path}")

    seed_bank = load_yaml(repo_root / "archetypes" / "SEED_BANK.yaml")
    type_map = load_yaml(repo_root / "archetypes" / "TYPE_TO_TEMPLATE.yaml")
    key = f"{args.lp}_{args.artifact_type}"
    seeds = ((seed_bank.get(key) or {}).get("seeds")) or []
    contexts = ((seed_bank.get(key) or {}).get("contexts")) or []
    template_rel = type_map.get(args.artifact_type)
    template_text = ""
    if template_rel and template_rel != "null":
        template_file = repo_root / template_rel
        if template_file.exists():
            template_text = template_file.read_text(encoding="utf-8")

    out_dir = repo_root / args.output_root / builder_slug(args.artifact_type)
    if out_dir.exists():
        if not args.force:
            raise SystemExit(f"builder already exists: {out_dir}")
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    today = date.today().isoformat()
    naming = type_spec.get("naming", "unknown")
    constraints = type_spec.get("constraints") or {}
    fields = type_spec.get("frontmatter_required") or []
    body_structure = type_spec.get("body_structure") or []
    llm_function = type_spec.get("llm_function", "BECOME")
    domain = args.artifact_type
    slug = builder_slug(args.artifact_type)

    write(
        out_dir / "MANIFEST.md",
        dump_frontmatter({
            "id": slug,
            "kind": "type_builder",
            "pillar": "P02",
            "parent": f"{args.lp.lower()}-chief [PLANNED]",
            "domain": domain,
            "llm_function": "BECOME",
            "version": "0.1.0",
            "created": today,
            "updated": today,
            "author": "CODEX",
            "purpose": f"Builder identity, routing, and mission for {args.artifact_type}",
            "tags": ["type-builder", domain.replace("_", "-"), args.lp, "scaffold"],
        })
        + f"# {slug}\n\n## Identity\n"
        + f"Especialista em construir `{args.artifact_type}` de `{args.lp}`. "
        + f"Boundary: {type_spec.get('boundary', 'TODO definir boundary precisa.')}.\n\n"
        + "## Capabilities\n"
        + f"- Produzir `{args.artifact_type}` com naming `{naming}`\n"
        + f"- Cobrir campos obrigatorios: {', '.join(fields) if fields else 'TODO'}\n"
        + "- Validar output contra SCHEMA.md, OUTPUT_TEMPLATE.md e QUALITY_GATES.md\n\n"
        + "## Routing\n"
        + f"keywords: [{domain}, {args.lp.lower()}, scaffold, specialist]\n"
        + f'triggers: "cria {args.artifact_type}", "gera {args.artifact_type}", "build {args.artifact_type}"\n\n'
        + "## Crew Role\n"
        + f"I handle `{args.artifact_type}` only.\n",
    )

    write(
        out_dir / "SYSTEM_PROMPT.md",
        dump_frontmatter({"pillar": "P03", "llm_function": "BECOME", "purpose": f"Persona and operational rules for {slug}"})
        + f"# System Prompt: {slug}\n\n"
        + f"You are `{slug}`, a CEX specialist for `{args.artifact_type}`.\n"
        + "1. SCHEMA.md is source of truth\n"
        + "2. OUTPUT_TEMPLATE.md derives from SCHEMA.md only\n"
        + "3. CONFIG.md may restrict but never invent fields\n"
        + "4. Mark unresolved gaps explicitly instead of guessing\n"
        + "5. Avoid forward-promises unless `[PLANNED]`\n",
    )

    write(
        out_dir / "KNOWLEDGE.md",
        dump_frontmatter({"pillar": "P01", "llm_function": "INJECT", "purpose": f"Domain knowledge, seeds, and references for {args.artifact_type}"})
        + f"# Knowledge: {args.artifact_type}\n\n"
        + "## Type Facts\n"
        + f"- LP: `{args.lp}`\n- Layer: `{type_spec.get('layer', 'unknown')}`\n"
        + f"- Machine format: `{type_spec.get('machine_format', 'unknown')}`\n- Naming: `{naming}`\n\n"
        + "## Seeds\n"
        + "".join(f"- `{seed}`\n" for seed in seeds[:12])
        + ("- `TODO_seed`\n" if not seeds else "")
        + "\n## Contexts\n"
        + "".join(f"- `{context}`\n" for context in contexts[:8])
        + ("- `TODO_context`\n" if not contexts else "")
        + "\n## References\n"
        + f"- Schema source: `{schema_path.relative_to(repo_root)}`\n"
        + (f"- Template source: `{template_rel}`\n" if template_rel and template_rel != "null" else "- Template source: `[PLANNED]`\n"),
    )

    write(
        out_dir / "INSTRUCTIONS.md",
        dump_frontmatter({"pillar": "P03", "llm_function": "GUIDE", "purpose": f"Execution steps and anti-patterns for {slug}"})
        + f"# Instructions: {slug}\n\n"
        + "## Build Flow\n"
        + "1. Read SCHEMA.md and lock required fields\n"
        + "2. Fill OUTPUT_TEMPLATE.md without inventing keys\n"
        + "3. Apply CONFIG.md restrictions and naming rules\n"
        + "4. Compare with EXAMPLES.md and QUALITY_GATES.md\n"
        + "5. Publish only after hard gates pass\n\n"
        + "## Anti-Patterns\n"
        + "- Do not merge adjacent types into one artifact\n"
        + "- Do not leave placeholders in production output\n"
        + "- Do not contradict schema constraints\n",
    )

    write(
        out_dir / "TOOLS.md",
        dump_frontmatter({"pillar": "P04", "llm_function": "ENABLE", "purpose": f"Allowed tools and usage rules for {slug}"})
        + f"# Tools: {slug}\n\n"
        + "## Preferred Tooling\n"
        + "- `python _tools/validate_builder.py <builder_dir>`\n"
        + "- `python _tools/scaffold_builder.py --type <type> --lp <LP>`\n"
        + "- `python _tools/validate_schema.py` [PLANNED]\n\n"
        + "## Usage Rules\n"
        + "- Use validators before publish\n"
        + "- Prefer schema-driven generation over freeform drafting\n",
    )

    output_block = template_block(template_text, fields)
    write(
        out_dir / "OUTPUT_TEMPLATE.md",
        dump_frontmatter({"pillar": "P05", "llm_function": "PRODUCE", "purpose": f"Template with fillable placeholders for {args.artifact_type}"})
        + f"# Output Template: {args.artifact_type}\n\nNaming pattern: `{naming}`\n\n```yaml\n"
        + output_block
        + "\n```\n\n## Derivation Notes\n- Every field above exists in SCHEMA.md\n- Replace placeholders with concrete values only\n",
    )

    body_structure_text = (
        "\n".join(f"1. `{item}`" for item in body_structure)
        if isinstance(body_structure, list)
        else "\n".join(f"### {variant}\n" + "\n".join(f"- `{section}`" for section in sections) for variant, sections in body_structure.items())
    ) or "1. `TODO_add_body_structure`"
    schema_fields = list(dict.fromkeys((fields or []) + extract_template_keys(output_block)))
    field_rows = "\n".join(
        f"| {field} | TODO | YES | - | {args.lp} schema |" for field in schema_fields
    ) or "| id | TODO | YES | - | schema |\n| type | TODO | YES | - | schema |\n| lp | TODO | YES | - | schema |"
    write(
        out_dir / "SCHEMA.md",
        dump_frontmatter({"pillar": "P06", "llm_function": "CONSTRAIN", "purpose": f"Formal schema definition for {args.artifact_type}"})
        + f"# Schema: {args.artifact_type}\n\n## Artifact Identity\n| Field | Value |\n|-------|-------|\n"
        + f"| LP | `{args.lp}` |\n| Type | literal `{args.artifact_type}` |\n"
        + f"| Machine format | `{type_spec.get('machine_format', 'unknown')}` |\n| Naming | `{naming}` |\n"
        + f"| Max bytes | `{constraints.get('max_bytes', 'TODO')}` |\n\n## Frontmatter Fields\n"
        + "| Field | Type | Required | Default | Source |\n|-------|------|----------|---------|--------|\n"
        + field_rows
        + "\n\n## Body Structure\n"
        + body_structure_text
        + "\n\n## Constraints\n"
        + "".join(f"- {key}: {value}\n" for key, value in constraints.items())
        + f"- llm_function: {llm_function}\n- boundary: {type_spec.get('boundary', 'TODO')}\n",
    )

    write(
        out_dir / "EXAMPLES.md",
        dump_frontmatter({"pillar": "P07", "llm_function": "PROVE", "purpose": f"Golden and anti-examples for {args.artifact_type}"})
        + f"# Examples: {args.artifact_type}\n\n## Golden Example\n"
        + f"- Filename pattern: `{naming}`\n- Required fields present: {', '.join(fields) if fields else 'TODO'}\n"
        + (f"- Context: `{contexts[0]}`\n" if contexts else "")
        + "- Quality target: `>= 8.0`\n\n## Anti-Example\n"
        + "- Missing one required field\n- Uses wrong naming convention\n- Contradicts a CONFIG.md restriction\n",
    )

    write(
        out_dir / "ARCHITECTURE.md",
        dump_frontmatter({"pillar": "P08", "llm_function": "MAP", "purpose": f"Work decomposition and flow for {slug}"})
        + f"# Architecture: {slug}\n\n## Build Graph\n```text\nschema -> output_template -> config -> examples -> quality_gates\n```\n\n"
        + "## Modules\n- `MANIFEST.md`: identity and routing\n- `SCHEMA.md`: contract surface\n"
        + "- `OUTPUT_TEMPLATE.md`: producer contract\n- `QUALITY_GATES.md`: publish threshold\n",
    )

    write(
        out_dir / "CONFIG.md",
        dump_frontmatter({"pillar": "P09", "llm_function": "CONSTRAIN", "purpose": f"Naming, paths, and limits for {args.artifact_type}"})
        + f"# Config: {args.artifact_type} Production Rules\n\n## Naming Convention\n"
        + "| Scope | Convention | Example |\n|-------|-----------|---------|\n"
        + f"| Artifact file | `{naming}` | `TODO_example` |\n"
        + f"| Builder directory | kebab-case | `{slug}/` |\n"
        + "| Frontmatter fields | snake_case | `id`, `type`, `lp` |\n\n"
        + "## File Paths\n"
        + f"- Output: `cex/{lp_dir}/examples/TODO_output`\n- Compiled: `cex/{lp_dir}/compiled/TODO_compiled`\n\n"
        + "## Size Limits\n"
        + f"- Absolute max: {constraints.get('max_bytes', 'TODO')} bytes\n- Keep outputs dense and non-redundant\n\n"
        + "## Field Restrictions\n"
        + "".join(f"- `{field}` must follow SCHEMA.md semantics\n" for field in fields[:12]),
    )

    write(
        out_dir / "MEMORY.md",
        dump_frontmatter({"pillar": "P10", "llm_function": "REMEMBER", "purpose": f"Stable heuristics and lessons for {args.artifact_type}"})
        + f"# Memory: {args.artifact_type}\n\n## Stable Heuristics\n"
        + "- Start from schema, not prose\n- Prefer exact field coverage over decorative narrative\n"
        + "- Record type-specific ambiguities after first production run\n\n## Known Gaps\n"
        + "- `TODO`: capture friction after first real artifact\n- `TODO`: add failure modes observed in review\n",
    )

    write(
        out_dir / "QUALITY_GATES.md",
        dump_frontmatter({"pillar": "P11", "llm_function": "GOVERN", "purpose": f"Hard and soft quality gates for {args.artifact_type}"})
        + f"# Quality Gates: {args.artifact_type}\n\n## HARD Gates\n"
        + "| Gate | Check | Why |\n|------|-------|-----|\n"
        + "| H01 | Required fields parse and exist | contract integrity |\n"
        + "| H02 | type matches schema literal | type integrity |\n"
        + "| H03 | lp matches schema LP | routing integrity |\n"
        + "| H04 | naming follows CONFIG.md | discoverability |\n"
        + "| H05 | no extra fields outside SCHEMA.md | source-of-truth discipline |\n\n"
        + "## SOFT Gates\n| Gate | Check | Weight | Score if pass |\n|------|-------|--------|---------------|\n"
        + "| S01 | Dense summary | 1.0 | 10 |\n| S02 | At least one concrete example | 0.5 | 10 |\n"
        + "| S03 | References point to schema/template sources | 0.5 | 10 |\n| S04 | No unresolved TODOs in production output | 1.0 | 10 |\n",
    )

    write(
        out_dir / "COLLABORATION.md",
        dump_frontmatter({"pillar": "P12", "llm_function": "COLLABORATE", "purpose": f"Crew role, inputs, outputs, and adjacencies for {args.artifact_type}"})
        + f"# Collaboration: {slug}\n\n## My Role in Crews\n"
        + f"I specialize in `{args.artifact_type}` and emit one artifact per request.\n\n## I Receive\n"
        + "- explicit type request\n- seeds or source facts\n- quality target when provided\n\n## I Produce\n"
        + f"- one `{args.artifact_type}` artifact\n- supporting validation via `validate_builder.py`\n\n"
        + "## Adjacent Builders\n- `quality-gate-builder` may define publish policy\n"
        + "- `signal-builder` may report completion\n"
        + f"- `{slug}` does not depend on missing builders unless marked `[PLANNED]`\n",
    )

    for name in EXPECTED_FILES:
        print(f"{out_dir / name}")


if __name__ == "__main__":
    main()
