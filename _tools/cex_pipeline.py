#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_pipeline.py -- 5-Stage CEX Build Engine
CAPTURE -> DECOMPOSE -> HYDRATE -> COMPILE -> ENVELOPE

Transforms user input into complete CEX artifacts with dual output (.md + compiled/).

Usage:
  python cex_pipeline.py --type knowledge_card --topic "error handling" --pillar P01
  python cex_pipeline.py --interactive
  python cex_pipeline.py --from-file input.md
  python cex_pipeline.py --type agent --topic "scraper" --pillar P02 --dry-run
"""

import argparse
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)


CEX_ROOT = Path(__file__).resolve().parent.parent

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

# Type abbreviations extracted from schema naming patterns
TYPE_ABBREV = {
    "knowledge_card": "kc",
    "rag_source": "rs",
    "glossary_entry": "gl",
    "context_doc": "ctx",
    "embedding_config": "emb",
    "few_shot_example": "fse",
    "agent": "agent",
    "lens": "lens",
    "boot_config": "bc",
    "mental_model": "mm",
    "model_card": "mc",
    "router": "rtr",
    "fallback_chain": "fc",
    "agent_package": "iso",
    "axiom": "ax",
    "system_prompt": "sp",
    "user_prompt": "up",
    "prompt_template": "pt",
    "few_shot": "fs",
    "chain_of_thought": "cot",
    "react": "react",
    "chain": "chain",
    "meta_prompt": "mp",
    "router_prompt": "rp",
    "planner": "plan",
    "skill": "skill",
    "mcp_server": "mcp",
    "hook": "hook",
    "plugin": "plugin",
    "client": "client",
    "cli_tool": "cli",
    "scraper": "scraper",
    "connector": "conn",
    "daemon": "daemon",
    "component": "comp",
    "response_format": "r",
    "parser": "parser",
    "formatter": "fmt",
    "naming_rule": "nr",
    "input_schema": "is",
    "type_de": "td",
    "validator": "val",
    "interface": "iface",
    "validation_schema": "vs",
    "artifact_blueprint": "ab",
    "grammar": "gram",
    "unit_eval": "ue",
    "smoke_eval": "se",
    "e2e_eval": "e2e",
    "benchmark": "bench",
    "golden_test": "gt",
    "scoring_rubric": "sr",
    "agent_card": "sat",
    "pattern": "pat",
    "law": "law",
    "diagram": "diag",
    "component_map": "cmap",
    "env_config": "env",
    "path_config": "pc",
    "permission": "perm",
    "feature_flag": "f",
    "runtime_rule": "rr",
    "runtime_state": "rstate",
    "knowledge_index": "bi",
    "learning_record": "lr",
    "session_state": "ss",
    "quality_gate": "qg",
    "bugloop": "bug",
    "lifecycle_rule": "lcr",
    "guardrail": "guard",
    "optimizer": "opt",
    "workflow": "w",
    "dag": "dag",
    "spawn_config": "spawn",
    "signal": "sig",
    "handof": "ho",
    "dispatch_rule": "dr",
    "crew": "crew",
}

OUTPUT_PREFIXES = {"example": "ex", "template": "tpl", "builder": "bld"}


# -- Utilities -------------------------------------------------------


def load_yaml_file(path: Path) -> dict:
    """Load and return a YAML file as a dictionary."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def slugify(text: str) -> str:
    """Convert free text into a lowercase underscore slug."""
    slug = text.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = slug.strip("_")
    return slug[:50]


def load_schema(pillar: str) -> dict:
    """Load the schema document for one pillar code."""
    lp_dir = LP_DIRS.get(pillar)
    if not lp_dir:
        print("ERROR: Invalid pillar. Use P01-P12.", file=sys.stderr)
        sys.exit(1)
    schema_path = CEX_ROOT / lp_dir / "_schema.yaml"
    if not schema_path.exists():
        print(f"ERROR: Schema not found: {schema_path}", file=sys.stderr)
        sys.exit(1)
    return load_yaml_file(schema_path)


def find_pillar_for_type(type_name: str) -> str | None:
    """Find the pillar whose schema declares the requested artifact type."""
    for pillar, dirname in LP_DIRS.items():
        schema_path = CEX_ROOT / dirname / "_schema.yaml"
        if not schema_path.exists():
            continue
        schema = load_yaml_file(schema_path)
        if type_name in schema.get("kinds", {}):
            return pillar
    return None


# -- STAGE 1: CAPTURE ------------------------------------------------


def capture_cli(args) -> dict:
    """Capture pipeline input from parsed CLI arguments."""
    return {
        "type": args.type,
        "topic": args.topic,
        "pillar": args.pillar.upper() if args.pillar else None,
        "content": args.content or "",
        "author": args.author or "pipeline",
        "domain": args.domain or "general",
        "output_kind": args.output_kind or "example",
    }


def capture_interactive() -> dict:
    """Capture pipeline input through an interactive terminal session."""
    print("\n=== CEX Pipeline: Interactive Mode ===\n")
    print("Available pillars:")
    for lp, dirname in LP_DIRS.items():
        name = dirname.split("_", 1)[1]
        print(f"  {lp}: {name}")

    pillar = input("\nPillar (e.g. P01): ").strip().upper()
    if pillar not in LP_DIRS:
        print("ERROR: Invalid pillar.", file=sys.stderr)
        sys.exit(1)

    schema = load_schema(pillar)
    kinds = schema.get("kinds", {})
    print(f"\nAvailable types in {pillar}:")
    for kind_name, kind_def in kinds.items():
        desc = kind_def.get("description", "")
        print(f"  {kind_name}: {desc}")

    type_name = input("\nType: ").strip()
    if type_name not in kinds:
        print(f"ERROR: Type not found em {pillar}.", file=sys.stderr)
        sys.exit(1)

    topic = input("Topic (e.g. 'error handling'): ").strip()
    domain = input("Domain [general]: ").strip() or "general"
    author = input("Author [pipeline]: ").strip() or "pipeline"

    print("\nContent (paste raw text, end with empty line):")
    content_lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break
        content_lines.append(line)

    return {
        "type": type_name,
        "topic": topic,
        "pillar": pillar,
        "content": "\n".join(content_lines),
        "author": author,
        "domain": domain,
        "output_kind": "example",
    }


def capture_from_file(filepath: str) -> dict:
    """Capture pipeline input from a markdown file with optional frontmatter."""
    path = Path(filepath)
    if not path.exists():
        print(f"ERROR: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if match:
        fm = yaml.safe_load(match.group(1)) or {}
        body = match.group(2)
    else:
        fm = {}
        body = text

    return {
        "type": fm.get("type", fm.get("kind", "")),
        "topic": fm.get("topic", ""),
        "pillar": (fm.get("pillar", "") or "").upper(),
        "content": body.strip(),
        "author": fm.get("author", "pipeline"),
        "domain": fm.get("domain", "general"),
        "output_kind": fm.get("output_kind", "example"),
    }


# -- STAGE 2: DECOMPOSE ---------------------------------------------


def decompose(input_data: dict) -> dict:
    """Resolve schema metadata and constraints for the requested artifact type."""
    pillar = input_data.get("pillar")
    type_name = input_data["type"]

    if not pillar:
        pillar = find_pillar_for_type(type_name)
        if not pillar:
            print(
                "ERROR: Type not found em nenhum pillar. Use --pillar.",
                file=sys.stderr,
            )
            sys.exit(1)
        input_data["pillar"] = pillar

    schema = load_schema(pillar)
    kinds = schema.get("kinds", {})

    if type_name not in kinds:
        available = ", ".join(kinds.keys())
        print(
            f"ERROR: Type not found em {pillar}. Available: {available}",
            file=sys.stderr,
        )
        sys.exit(1)

    kind_def = kinds[type_name]

    return {
        **input_data,
        "schema": schema,
        "kind_de": kind_def,
        "required_fields": kind_def.get("frontmatter_required", []),
        "cex_fields": kind_def.get("frontmatter_cex", []),
        "constraints": kind_def.get("constraints", {}),
        "body_structure": kind_def.get("body_structure", {}),
        "machine_format": kind_def.get("machine_format", "yaml"),
        "naming_pattern": kind_def.get("naming", ""),
    }


# -- STAGE 3: HYDRATE ------------------------------------------------


def hydrate(data: dict) -> dict:
    """Assemble frontmatter defaults and a first-pass body draft."""
    pillar = data["pillar"]
    type_name = data["type"]
    topic = data["topic"]
    topic_slug = slugify(topic)
    lp_dir = CEX_ROOT / LP_DIRS[pillar]

    template_content = _load_template(lp_dir, type_name)
    builder_knowledge = _load_builder_knowledge(type_name)

    today = datetime.date.today().isoformat()
    abbrev = TYPE_ABBREV.get(type_name, type_name[:3])
    artifact_id = f"{pillar.lower()}_{abbrev}_{topic_slug}"

    frontmatter = {
        "id": artifact_id,
        "kind": type_name,
        "pillar": pillar,
        "title": topic.title(),
        "version": "1.0.0",
        "created": today,
        "updated": today,
        "author": data["author"],
        "domain": data["domain"],
        "quality": None,
    }

    for field in data["required_fields"]:
        if field not in frontmatter:
            frontmatter[field] = _default_for_field(field, data)

    for field in data.get("cex_fields", []):
        if field not in frontmatter:
            frontmatter[field] = _default_for_field(field, data)

    body = _build_body(data, template_content, builder_knowledge)

    return {
        **data,
        "frontmatter": frontmatter,
        "body": body,
        "artifact_id": artifact_id,
        "topic_slug": topic_slug,
        "template_used": template_content is not None,
        "builder_used": builder_knowledge is not None,
    }


def _load_template(lp_dir: Path, type_name: str) -> str | None:
    templates_dir = lp_dir / "templates"
    if not templates_dir.exists():
        return None
    tpl_path = templates_dir / f"tpl_{type_name}.md"
    if tpl_path.exists():
        with open(tpl_path, "r", encoding="utf-8") as f:
            return f.read()
    for p in templates_dir.glob("tpl_*.md"):
        if type_name.replace("_", "") in p.stem.replace("_", ""):
            with open(p, "r", encoding="utf-8") as f:
                return f.read()
    return None


def _load_builder_knowledge(type_name: str) -> str | None:
    builder_dir = CEX_ROOT / "archetypes" / "builders" / f"{type_name.replace('_', '-')}-builder"
    if not builder_dir.exists():
        return None
    for p in sorted(builder_dir.glob("bld_knowledge*")):
        with open(p, "r", encoding="utf-8") as f:
            return f.read()
    return None


def _default_for_field(field: str, data: dict) -> object:
    defaults = {
        "tags": [data["domain"], data["type"]],
        "tldr": f"{data['type'].replace('_', ' ').title()}: {data['topic']}",
        "when_to_use": f"When working with {data['topic']}",
        "keywords": [slugify(w) for w in data["topic"].split()[:3] if w],
        "long_tails": [f"how to {data['topic']}"],
        "axioms": [],
        "linked_artifacts": {"adw": None, "agent": None, "hop": None},
        "density_score": None,
        "data_source": "pipeline",
        "scope": data["domain"],
        "url": None,
        "last_checked": None,
        "term": data["topic"],
        "definition": data["topic"],
        "synonyms": [],
        "model_name": None,
        "dimensions": None,
        "chunk_size": None,
        "input": None,
        "output": None,
    }
    return defaults.get(field)


def _build_body(data: dict, template: str | None, knowledge: str | None) -> str:
    type_name = data["type"]
    topic = data["topic"]
    content = data.get("content", "")
    body_structure = data.get("body_structure", {})

    # Rich user content takes priority
    if content and len(content) > 100:
        return f"# {topic.title()}\n\n{content}"

    # Template with variable substitution
    if template:
        match = re.match(r"^---\s*\n.*?\n---\s*\n(.*)$", template, re.DOTALL)
        body = match.group(1).strip() if match else template
        replacements = {
            "{{KNOWLEDGE_CARD_TITLE}}": topic.title(),
            "{{TOPIC_NAME}}": topic,
            "{{TOPIC_SLUG}}": slugify(topic),
            "{{SCOPE}}": data["domain"],
            "{{OWNER}}": data["author"],
        }
        for var, val in replacements.items():
            body = body.replace(var, val)
        if content:
            body += f"\n\n## Additional Content\n{content}"
        return body

    # Generate from body_structure schema definition
    if body_structure and isinstance(body_structure, dict):
        variant_name = list(body_structure.keys())[0]
        variant_sections = body_structure[variant_name]
        if isinstance(variant_sections, list):
            parts = [f"# {topic.title()}"]
            for sec in variant_sections:
                sec_title = sec.replace("_", " ").title()
                parts.append(f"\n## {sec_title}")
                if content:
                    parts.append(f"- {content[:80]}")
                else:
                    parts.append("- [TODO: add concrete data]")
            return "\n".join(parts)

    # Minimal fallback structure
    lines = [
        f"# {topic.title()}",
        "",
        "## Overview",
        f"- {type_name.replace('_', ' ').title()} about {topic}",
        "",
        "## Details",
        "- [TODO: add concrete facts]",
    ]
    if content:
        lines.extend(["", "## Content", content])
    lines.extend(["", "## References", "- [TODO: add sources]"])
    return "\n".join(lines)


# -- STAGE 4: COMPILE ------------------------------------------------


def compile_artifact(data: dict) -> dict:
    """Render the markdown artifact and compute validation metadata."""
    frontmatter = data["frontmatter"]
    body = data["body"]
    constraints = data.get("constraints", {})

    density = _calculate_density(body)
    if "density_score" in frontmatter:
        frontmatter["density_score"] = round(density, 2)

    full_content = _render_md(frontmatter, body)
    content_bytes = len(full_content.encode("utf-8"))

    warnings = []

    max_bytes = constraints.get("max_bytes")
    if max_bytes and content_bytes > max_bytes:
        warnings.append(f"Size {content_bytes}B exceeds max {max_bytes}B")

    density_min = constraints.get("density_min")
    if density_min and density < density_min:
        warnings.append(f"Density {density:.2f} below minimum {density_min}")

    min_bullets = constraints.get("min_bullets")
    if min_bullets:
        bullet_count = len(re.findall(r"^\s*[-*]\s", body, re.MULTILINE))
        if bullet_count < min_bullets:
            warnings.append(f"Only {bullet_count} bullets, minimum {min_bullets}")

    for field in data.get("required_fields", []):
        val = frontmatter.get(field)
        if val is None and field != "quality":
            warnings.append(f"Required field '{field}' is empty")

    return {
        **data,
        "density": density,
        "content_hash": hashlib.sha256(body.encode("utf-8")).hexdigest()[:16],
        "content_bytes": content_bytes,
        "warnings": warnings,
    }


def _calculate_density(body: str) -> float:
    lines = body.split("\n")
    non_empty = [ln for ln in lines if ln.strip()]
    if not non_empty:
        return 0.0
    data_lines = 0
    for line in non_empty:
        s = line.strip()
        if (
            s.startswith("|")
            or s.startswith("- ")
            or s.startswith("* ")
            or re.match(r"^\d+\.\s", s)
            or s.startswith("#")
            or s.startswith("```")
            or ":" in s
            or re.search(r"\d{2,}", s)
            or s.startswith(">")
        ):
            data_lines += 1
    return data_lines / len(non_empty)


def _render_md(frontmatter: dict, body: str) -> str:
    fm_str = yaml.dump(
        frontmatter,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=120,
    )
    return f"---\n{fm_str}---\n\n{body}\n"


# -- STAGE 5: ENVELOPE ----------------------------------------------


def envelope(data: dict, dry_run: bool = False) -> dict:
    """Choose output paths, print the pipeline report, and write files when enabled."""
    pillar = data["pillar"]
    type_name = data["type"]
    topic_slug = data["topic_slug"]
    frontmatter = data["frontmatter"]
    body = data["body"]
    machine_format = data.get("machine_format", "yaml")
    output_kind = data.get("output_kind", "example")

    lp_dir = CEX_ROOT / LP_DIRS[pillar]
    prefix = OUTPUT_PREFIXES.get(output_kind, "ex")

    # Directory routing
    if output_kind == "builder":
        out_dir = CEX_ROOT / "archetypes" / "builders" / f"{type_name.replace('_', '-')}-builder"
    elif output_kind == "template":
        out_dir = lp_dir / "templates"
    else:
        out_dir = lp_dir / "examples"

    compiled_dir = lp_dir / "compiled"
    compiled_ext = "json" if machine_format == "json" else "yaml"

    md_filename = f"{prefix}_{type_name}_{topic_slug}.md"
    compiled_filename = f"{prefix}_{type_name}_{topic_slug}.{compiled_ext}"

    md_path = out_dir / md_filename
    compiled_path = compiled_dir / compiled_filename

    md_content = _render_md(frontmatter, body)

    # Build compiled data
    compiled_data = dict(frontmatter)
    compiled_data.update(_parse_body_to_dict(body))

    # Report
    print(f"\n{'=' * 60}")
    print(f"CEX Pipeline: {'DRY RUN' if dry_run else 'BUILDING'}")
    print(f"{'=' * 60}")
    print(f"  Stage 1 CAPTURE:   type={type_name}, topic={data['topic']}")
    print(f"  Stage 2 DECOMPOSE: pillar={pillar}, fields={len(data.get('required_fields', []))}")
    print(
        f"  Stage 3 HYDRATE:   template={'yes' if data.get('template_used') else 'no'}, builder={'yes' if data.get('builder_used') else 'no'}"
    )
    print(
        f"  Stage 4 COMPILE:   density={data['density']:.2f}, size={data['content_bytes']}B, hash={data['content_hash']}"
    )
    print(f"  Stage 5 ENVELOPE:  {md_filename} ({output_kind})")

    if data.get("warnings"):
        print("\n  WARNINGS:")
        for w in data["warnings"]:
            print(f"    ! {w}")

    if dry_run:
        print("\n  [DRY RUN] Would create:")
        print(f"    {md_path}")
        print(f"    {compiled_path}")
        preview = md_content.split("\n")[:30]
        print(f"\n  Preview ({len(preview)} lines):")
        for line in preview:
            print(f"    {line}")
        return {
            **data,
            "md_path": str(md_path),
            "compiled_path": str(compiled_path),
            "written": False,
        }

    # Write files
    out_dir.mkdir(parents=True, exist_ok=True)
    compiled_dir.mkdir(parents=True, exist_ok=True)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    with open(compiled_path, "w", encoding="utf-8") as f:
        if compiled_ext == "json":
            json.dump(compiled_data, f, indent=2, ensure_ascii=False, default=str)
            f.write("\n")
        else:
            yaml.dump(
                compiled_data,
                f,
                default_flow_style=False,
                allow_unicode=True,
                sort_keys=False,
                width=120,
            )

    print("\n  CREATED:")
    print(f"    {md_path}")
    print(f"    {compiled_path}")

    return {**data, "md_path": str(md_path), "compiled_path": str(compiled_path), "written": True}


def _parse_body_to_dict(body: str) -> dict:
    sections = {}
    current_key = None
    current_lines = []
    for line in body.split("\n"):
        header_match = re.match(r"^#{1,3}\s+(.+)$", line)
        if header_match:
            if current_key:
                content = "\n".join(current_lines).strip()
                if content:
                    sections[current_key] = _section_value(content)
            raw = header_match.group(1).strip().lower()
            current_key = re.sub(r"[^a-z0-9]+", "_", raw).strip("_")
            current_lines = []
        else:
            current_lines.append(line)
    if current_key:
        content = "\n".join(current_lines).strip()
        if content:
            sections[current_key] = _section_value(content)
    return sections


def _section_value(content: str):
    lines = [l for l in content.split("\n") if l.strip()]
    items = []
    for line in lines:
        s = line.strip()
        m = re.match(r"^[-*]\s+(.*)", s) or re.match(r"^\d+\.\s+(.*)", s)
        if m:
            items.append(m.group(1))
    if items and len(items) == len(lines):
        return items
    return content


# -- MAIN ------------------------------------------------------------


def run_pipeline(input_data: dict, dry_run: bool = False) -> dict:
    """Run the full five-stage pipeline for one input payload."""
    if not input_data.get("type"):
        print("ERROR: --type required.", file=sys.stderr)
        sys.exit(1)
    if not input_data.get("topic"):
        print("ERROR: --topic required.", file=sys.stderr)
        sys.exit(1)
    data = decompose(input_data)
    data = hydrate(data)
    data = compile_artifact(data)
    data = envelope(data, dry_run=dry_run)
    return data


def main():
    """Parse CLI arguments, capture input, and execute the pipeline."""
    parser = argparse.ArgumentParser(
        description="CEX Pipeline: 5-stage build engine (CAPTURE > DECOMPOSE > HYDRATE > COMPILE > ENVELOPE)"
    )
    parser.add_argument("--type", help="Artifact type (e.g. knowledge_card, agent, skill)")
    parser.add_argument("--topic", help="Topic or subject of the artifact")
    parser.add_argument("--pillar", help="Pillar code (e.g. P01). Auto-detected if omitted.")
    parser.add_argument("--content", help="Raw content to include in the body")
    parser.add_argument("--author", default="pipeline", help="Author name (default: pipeline)")
    parser.add_argument("--domain", default="general", help="Domain name (default: general)")
    parser.add_argument(
        "--output-kind",
        dest="output_kind",
        default="example",
        choices=["example", "template", "builder"],
        help="Output prefix: example (ex_), template (tpl_), builder (bld_)",
    )
    parser.add_argument("--interactive", action="store_true", help="Interactive mode with prompts")
    parser.add_argument("--from-file", dest="from_file", help="Read input from a markdown file")
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be created without writing"
    )
    args = parser.parse_args()

    # Stage 1: CAPTURE
    if args.interactive:
        input_data = capture_interactive()
    elif args.from_file:
        input_data = capture_from_file(args.from_file)
    elif args.type and args.topic:
        input_data = capture_cli(args)
    else:
        parser.print_help()
        sys.exit(1)

    result = run_pipeline(input_data, dry_run=args.dry_run)

    status = "DRY RUN" if args.dry_run else ("CREATED" if result.get("written") else "NO OUTPUT")
    print(f"\n--- Pipeline {status}: {result.get('artifact_id', '?')} ---")


if __name__ == "__main__":
    main()
