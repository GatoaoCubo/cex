#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_forge.py -- O Forjador Universal CEX
Gera prompts prontos para LLM que produzem artefatos CEX validos.

Fluxo:
  1. Le _schema.yaml do LP -> extrai regras (max_bytes, density_min, required fields)
  2. Le template correspondente (via TYPE_TO_TEMPLATE.yaml)
  3. Monta PROMPT para LLM: template + schema rules + seed words + context
  4. Salva o prompt montado em stdout (NAO chama LLM)
  5. Valida formato do prompt (tem placeholders? respeita max_bytes? frontmatter?)

Uso:
  python cex_forge.py --lp P01 --type knowledge_card --seeds "RAG,embeddings,chunking" --context "texto sobre RAG"
  python cex_forge.py --lp P02 --type agent --seeds "scraper,web,data" --context-file research.md
  python cex_forge.py --list-types              # lista todos os 69 tipos
  python cex_forge.py --list-types --lp P01     # tipos do LP
"""

import sys

if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")

import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

CEX_ROOT = Path(__file__).resolve().parent.parent
META_DIR = CEX_ROOT / "archetypes"
TYPE_MAP_PATH = META_DIR / "TYPE_TO_TEMPLATE.yaml"
BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"
BUILDER_MAX_BYTES = 40 * 1024  # 40KB total budget for injected specs
BUILDER_EXAMPLES_MAX = 3 * 1024  # 3KB cap for examples
BUILDER_PRIORITY = {"knowledge_card": 1, "instruction": 2, "quality_gate": 3, "examples": 4}

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


def load_yaml(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_schema(lp: str) -> dict:
    lp_dir = LP_DIRS.get(lp.upper())
    if not lp_dir:
        print("ERROR: LP not found. Use P01-P12.", file=sys.stderr)
        sys.exit(1)
    schema_path = CEX_ROOT / lp_dir / "_schema.yaml"
    if not schema_path.exists():
        print(f"ERROR: Schema not found: {schema_path}", file=sys.stderr)
        sys.exit(1)
    return load_yaml(schema_path)


def load_type_map() -> dict:
    if not TYPE_MAP_PATH.exists():
        print(f"ERROR: TYPE_TO_TEMPLATE.yaml not found: {TYPE_MAP_PATH}", file=sys.stderr)
        sys.exit(1)
    raw = load_yaml(TYPE_MAP_PATH)
    # Filter out comment-only keys (yaml loads them as key: None)
    return {k: v for k, v in raw.items() if not k.startswith("#")}


def load_template(template_rel_path: str) -> str | None:
    if not template_rel_path:
        return None
    tpl_path = CEX_ROOT / template_rel_path
    if not tpl_path.exists():
        return None
    with open(tpl_path, "r", encoding="utf-8") as f:
        return f.read()


def kind_to_builder_dir(kind: str) -> Path:
    """Convert kind name (e.g. rag_source) to builder dir path."""
    return BUILDER_DIR / (kind.replace("_", "-") + "-builder")


def load_builder_specs(kind: str) -> dict[str, str]:
    """Load builder spec files for a given kind.

    Scans archetypes/builders/{kind}-builder/bld_*.md.
    Returns dict mapping spec_type -> content (e.g. {"knowledge_card": "...", ...}).
    """
    builder_path = kind_to_builder_dir(kind)
    if not builder_path.exists():
        return {}

    specs = {}
    suffix = f"_{kind}.md"
    for f in sorted(builder_path.glob("bld_*.md")):
        name = f.name
        if not name.endswith(suffix):
            continue
        spec_type = name[4 : -len(suffix)]  # strip "bld_" prefix and "_{kind}.md" suffix
        with open(f, "r", encoding="utf-8") as fh:
            specs[spec_type] = fh.read()
    return specs


def inject_builder_context(sections: list[str], builder_specs: dict[str, str]) -> list[str]:
    """Append builder spec sections. Budget: 40KB max.

    Priority: knowledge > instructions > gates > examples > rest.
    Examples truncated to 3KB.
    """
    if not builder_specs:
        return sections

    header_map = {
        "knowledge_card": "Builder Knowledge",
        "instruction": "Builder Instructions",
        "examples": "Builder Examples",
        "quality_gate": "Builder Quality Gates",
    }

    def sort_key(item: tuple[str, str]) -> int:
        return BUILDER_PRIORITY.get(item[0], 5)

    result = list(sections)
    total_bytes = 0

    for spec_type, content in sorted(builder_specs.items(), key=sort_key):
        header = header_map.get(spec_type, f"Builder {spec_type.replace('_', ' ').title()}")

        if spec_type == "examples":
            raw = content.encode("utf-8")
            if len(raw) > BUILDER_EXAMPLES_MAX:
                content = raw[:BUILDER_EXAMPLES_MAX].decode("utf-8", errors="ignore")
                content += "\n\n[... truncated to 3KB ...]"

        section_bytes = len(content.encode("utf-8"))
        if total_bytes + section_bytes > BUILDER_MAX_BYTES:
            break

        result.append(f"## {header}")
        result.append(content.strip())
        result.append("")
        total_bytes += section_bytes

    return result


def extract_type_rules(schema: dict, type_name: str) -> dict:
    types = schema.get("kinds", {})
    if type_name not in types:
        return {}
    t = types[type_name]
    rules = {
        "description": t.get("description", ""),
        "naming": t.get("naming", ""),
    }
    constraints = t.get("constraints", {})
    if isinstance(constraints, dict):
        rules.update(constraints)
    else:
        rules["constraints_raw"] = constraints

    rules["frontmatter_required"] = t.get("frontmatter_required", [])
    rules["frontmatter_cex"] = t.get("frontmatter_cex", [])
    rules["body_structure"] = t.get("body_structure", [])
    rules["validation"] = t.get("validation", [])
    return rules


def build_prompt(
    lp: str,
    type_name: str,
    seeds: list[str],
    context: str,
    schema: dict,
    rules: dict,
    template: str | None,
    builder_specs: dict[str, str] | None = None,
    builder_only: bool = False,
) -> str:
    lp_name = schema.get("name", lp)
    lp_desc = schema.get("description", "")

    sections = []

    # Header
    sections.append(f"# CEX FORGE -- Generate a `{type_name}` artifact (LP: {lp})")
    sections.append("")

    # Role
    sections.append("## You are")
    sections.append(
        f"A CEX artifact generator specialized in `{type_name}` "
        f"for domain {lp} ({lp_name}: {lp_desc})."
    )
    sections.append(
        "Your output must be a valid Markdown/YAML file, "
        "ready to save in the CEX repository."
    )
    sections.append("")

    # Schema rules
    sections.append("## Schema Rules")
    sections.append(f"- **Type**: {type_name}")
    sections.append(f"- **Description**: {rules.get('description', 'N/A')}")
    sections.append(f"- **Naming**: `{rules.get('naming', 'N/A')}`")
    if rules.get("max_bytes"):
        sections.append(f"- **Max bytes**: {rules['max_bytes']}")
    if rules.get("density_min"):
        sections.append(f"- **Density min**: {rules['density_min']}")
    if rules.get("quality_min"):
        sections.append(f"- **Quality min**: {rules['quality_min']}")
    if rules.get("min_bullets"):
        sections.append(f"- **Min bullets**: {rules['min_bullets']}")
    sections.append("")

    # Frontmatter
    fm_required = rules.get("frontmatter_required", [])
    fm_cex = rules.get("frontmatter_cex", [])
    if fm_required or fm_cex:
        sections.append("## Required Frontmatter")
        sections.append("```yaml")
        sections.append("---")
        for field in fm_required:
            sections.append(f"{field}: # REQUIRED")
        for field in fm_cex:
            sections.append(f"{field}: # CEX extended")
        sections.append("---")
        sections.append("```")
        sections.append("")

    # Body structure
    body = rules.get("body_structure", [])
    if body:
        sections.append("## Body Structure")
        if isinstance(body, dict):
            for variant, fields in body.items():
                sections.append(f"### Variant: {variant}")
                if isinstance(fields, list):
                    for f in fields:
                        sections.append(f"  - `{f}`")
                sections.append("")
        elif isinstance(body, list):
            for item in body:
                sections.append(f"- `{item}`")
            sections.append("")

    # Validation rules
    val = rules.get("validation", [])
    if val:
        sections.append("## Validation")
        for v in val:
            sections.append(f"- {v}")
        sections.append("")

    # Template
    if not builder_only:
        if template:
            sections.append("## Reference Template")
            sections.append("Use this template as BASE. Fill ALL {{VARIABLES}}.")
            sections.append("")
            sections.append("```")
            sections.append(template.strip())
            sections.append("```")
            sections.append("")
        else:
            sections.append("## Template")
            sections.append(
                "NOTE: No template exists for this type (GAP). "
                "Create the artifact following the schema structure above."
            )
            sections.append("")

    # Builder specs
    if builder_specs:
        sections = inject_builder_context(sections, builder_specs)

    # Seeds
    sections.append("## Seed Words")
    sections.append(f"Main topic: **{', '.join(seeds)}**")
    sections.append("Use these keywords as a base to generate relevant and dense content.")
    sections.append("")

    # Context
    if context.strip():
        sections.append("## Provided Context")
        sections.append(context.strip())
        sections.append("")

    # Brand context injection (if brand_config.yaml exists)
    brand_config_path = CEX_ROOT / ".cex" / "brand" / "brand_config.yaml"
    if brand_config_path.exists():
        try:
            from brand_inject import flatten, load_brand_config
            brand_cfg = load_brand_config(brand_config_path)
            if brand_cfg:
                flat = flatten(brand_cfg)
                real = {k: v for k, v in flat.items()
                        if not str(v).startswith("{{") and v
                        and not k.startswith(("identity.", "archetype.", "voice.",
                                              "audience.", "visual.", "positioning.",
                                              "monetization."))}
                if real:
                    sections.append("## Brand Context (from .cex/brand/brand_config.yaml)")
                    for k, v in sorted(real.items()):
                        sections.append(f"- {k}: {v}")
                    sections.append("")
        except ImportError:
            pass

    # Output instructions
    sections.append("## Output Instructions")
    sections.append("1. Generate the COMPLETE artifact (frontmatter YAML + body Markdown)")
    sections.append("2. Fill ALL required frontmatter fields")
    sections.append("3. Do NOT leave {{VARIABLES}} unfilled")
    sections.append(f"4. Respect the {rules.get('max_bytes', 'N/A')} byte limit")
    if rules.get("density_min"):
        sections.append(
            f"5. Minimum density: {rules['density_min']} (each sentence must carry unique information)"
        )
    sections.append(
        f"6. Quality target: >= {rules.get('quality_min', 7.0)} "
        "(no filler, no repetition, no obvious statements)"
    )
    sections.append("")

    return "\n".join(sections)


def validate_prompt(prompt: str, rules: dict) -> list[str]:
    warnings = []
    max_bytes = rules.get("max_bytes")

    # Check prompt has structure
    if "## " not in prompt:
        warnings.append("WARN: Prompt has no sections (## headers)")

    # Check template placeholders were mentioned
    if "{{" not in prompt and "VARIABLES" not in prompt:
        warnings.append("WARN: Prompt does not mention {{MUSTACHE}} placeholders")

    # Check frontmatter section exists
    if "Frontmatter" not in prompt and "frontmatter" not in prompt:
        warnings.append("WARN: Prompt has no frontmatter section")

    # Estimate if prompt is reasonable size
    prompt_bytes = len(prompt.encode("utf-8"))
    if prompt_bytes > 20000:
        warnings.append(f"WARN: Prompt too large ({prompt_bytes} bytes)")

    if max_bytes and "max_bytes" not in prompt.lower() and str(max_bytes) not in prompt:
        warnings.append(f"WARN: max_bytes ({max_bytes}) not mentioned in prompt")

    return warnings


def list_all_types(filter_lp: str | None = None) -> list[dict]:
    type_map = load_type_map()
    results = []
    for lp_key, lp_dir in sorted(LP_DIRS.items()):
        if filter_lp and lp_key.upper() != filter_lp.upper():
            continue
        schema = load_schema(lp_key)
        types = schema.get("kinds", {})
        for type_name, type_def in types.items():
            tpl = type_map.get(type_name)
            results.append(
                {
                    "pillar": lp_key,
                    "kind": type_name,
                    "description": type_def.get("description", ""),
                    "template": tpl if tpl else "GAP",
                    "max_bytes": type_def.get("constraints", {}).get("max_bytes", "N/A")
                    if isinstance(type_def.get("constraints"), dict)
                    else "N/A",
                }
            )
    return results


def main():
    parser = argparse.ArgumentParser(
        description="CEX Forge -- Gerador Universal de Prompts para Artefatos CEX",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python cex_forge.py --lp P01 --type knowledge_card --seeds "RAG,embeddings" --context "RAG eh..."
  python cex_forge.py --lp P02 --type agent --seeds "scraper,web" --context-file notes.md
  python cex_forge.py --list-types
  python cex_forge.py --list-types --lp P04
        """,
    )
    parser.add_argument("--lp", help="LP target (P01-P12)")
    parser.add_argument("--type", dest="type_name", help="Artifact type")
    parser.add_argument("--seeds", help="Seed words separated by comma")
    parser.add_argument("--context", default="", help="Context as free text")
    parser.add_argument("--context-file", help="File with context")
    parser.add_argument("--list-types", action="store_true", help="List all types")
    parser.add_argument("--output", help="Output file (default: stdout)")
    parser.add_argument(
        "--builder",
        action="store_true",
        help="Inject builder specs as context (auto-detect)",
    )
    parser.add_argument(
        "--builder-only",
        action="store_true",
        help="Use ONLY builder specs, skip template",
    )

    args = parser.parse_args()

    if args.list_types:
        types = list_all_types(args.lp)
        print(f"{'LP':<5} {'Type':<25} {'Template':<8} {'MaxB':<8} Description")
        print("-" * 90)
        for t in types:
            tpl_status = "OK" if t["template"] != "GAP" else "GAP"
            print(
                f"{t['pillar']:<5} {t['kind']:<25} {tpl_status:<8} "
                f"{str(t['max_bytes']):<8} {t['description']}"
            )
        print(
            f"\nTotal: {len(types)} tipos ({sum(1 for t in types if t['template'] != 'GAP')} com template, {sum(1 for t in types if t['template'] == 'GAP')} GAP)"
        )
        return

    if not args.lp or not args.type_name or not args.seeds:
        parser.error("--lp, --type e --seeds sao requireds (ou use --list-types)")

    # Load context
    context = args.context
    if args.context_file:
        ctx_path = Path(args.context_file)
        if not ctx_path.exists():
            print(f"ERROR: Context file not found: {ctx_path}", file=sys.stderr)
            sys.exit(1)
        with open(ctx_path, "r", encoding="utf-8") as f:
            context = f.read()

    seeds = [s.strip() for s in args.seeds.split(",") if s.strip()]

    # Load schema
    schema = load_schema(args.lp)
    rules = extract_type_rules(schema, args.type_name)
    if not rules:
        available = list(schema.get("kinds", {}).keys())
        print(
            f"ERROR: Type '{args.type_name}' not found in {args.lp}. "
            f"Available: {', '.join(available)}",
            file=sys.stderr,
        )
        sys.exit(1)

    # Load template
    type_map = load_type_map()
    template_path = type_map.get(args.type_name)
    template = load_template(template_path) if template_path else None

    # Load builder specs
    builder_specs = None
    use_builder = args.builder or args.builder_only
    if use_builder:
        builder_specs = load_builder_specs(args.type_name)
        if builder_specs:
            spec_count = len(builder_specs)
            total_kb = sum(len(v.encode("utf-8")) for v in builder_specs.values()) // 1024
            print(
                f"Builder: {spec_count} specs loaded ({total_kb}KB) "
                f"from {kind_to_builder_dir(args.type_name).name}",
                file=sys.stderr,
            )
        else:
            builder_dir = kind_to_builder_dir(args.type_name)
            print(
                f"WARN: Builder not found: {builder_dir}",
                file=sys.stderr,
            )

    # Build prompt
    prompt = build_prompt(
        args.lp,
        args.type_name,
        seeds,
        context,
        schema,
        rules,
        template,
        builder_specs=builder_specs,
        builder_only=args.builder_only,
    )

    # Validate
    warnings = validate_prompt(prompt, rules)
    for w in warnings:
        print(w, file=sys.stderr)

    # Output
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(prompt)
        print(f"Prompt salvo em: {out_path}", file=sys.stderr)
        print(f"Tamanho: {len(prompt.encode('utf-8'))} bytes", file=sys.stderr)
    else:
        print(prompt)

    if warnings:
        print(f"\n--- {len(warnings)} warning(s) ---", file=sys.stderr)


if __name__ == "__main__":
    main()
