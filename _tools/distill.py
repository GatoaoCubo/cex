# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")
"""
CEX Distill -- Transforms raw input into template-compliant artifacts.

The template IS the prompt. Not optional. Not a reference.

Usage:
  python distill.py --input raw_file.pdf --type knowledge_card
  python distill.py --input raw_file.pdf --type knowledge_card --dry-run
  python distill.py --list-types
"""
import sys
import argparse
from datetime import date
from pathlib import Path

import yaml

# Map artifact type -> template file
TYPE_TO_TEMPLATE = {
    "knowledge_card": "N00_genesis/P01_knowledge/templates/tpl_knowledge_card_domain.md",
    "knowledge_card_meta": "N00_genesis/P01_knowledge/templates/tpl_knowledge_card_meta.md",
    "knowledge_card_test": "N00_genesis/P01_knowledge/templates/tpl_knowledge_card_test.md",
}

CEX_ROOT = Path(__file__).parent.parent  # _tools/ -> CEX/
LIBRARY_DIR = CEX_ROOT / "N00_genesis" / "P01_knowledge" / "library"
INDEX_PATH = LIBRARY_DIR / "index.yaml"


def get_template(artifact_type: str) -> str:
    """Load the template for a given artifact type."""
    tpl_path = CEX_ROOT / TYPE_TO_TEMPLATE.get(artifact_type, "")
    if not tpl_path.exists():
        print(f"[ERROR] No template for type '{artifact_type}'")
        print(f"  Available: {list(TYPE_TO_TEMPLATE.keys())}")
        sys.exit(1)
    return tpl_path.read_text(encoding="utf-8")


def build_distill_prompt(template: str, raw_content: str, source_name: str) -> str:
    """Build the prompt that forces template compliance."""
    return f"""## TAREFA: Distill Knowledge

You received a RAW input and a REQUIRED TEMPLATE.
Seu trabalho: PREENCHER o template com conhecimento EXTRAIDO + EXPANDIDO do insumo.

### REGRAS:
1. TODOS os campos {{{{PLACEHOLDER}}}} devem ser preenchidos -- nenhum pode ficar vazio
2. NAO copie verbatim do insumo -- TRANSFORME em conhecimento acionavel
3. EXPANDA alem do insumo -- use seu conhecimento para enriquecer
4. O insumo eh SEMENTE, nao limite -- se o insumo eh basico, o output deve ser avancado
5. Preencha 'when_to_use' pensando: "uma LLM com ZERO contexto, quando carregaria isso?"
6. Preencha 'axioms' com regras IMPERATIVAS que mudam comportamento
7. Preencha 'Anti-Patterns' com erros que uma LLM cometeria sem esse knowledge
8. Preencha 'Application' com uso CONCRETO no contexto de AI agent systems
9. density_score >= 0.85 -- cada frase deve carregar informacao, zero filler

### TEMPLATE (preencha TODOS os campos):

{template}

### INSUMO RAW (source: {source_name}):

{raw_content}

### OUTPUT:
Retorne APENAS o template preenchido. Nada antes, nada depois.
"""


def validate_output(output: str, template: str) -> list:
    """Check that all template sections exist in output."""
    issues = []

    # Check required frontmatter fields
    required_fields = [
        "id:",
        "type:",
        "tldr:",
        "when_to_use:",
        "axioms:",
        "linked_artifacts:",
        "density_score:",
    ]
    for field in required_fields:
        if field not in output:
            issues.append(f"Missing frontmatter: {field}")

    # Check required sections
    required_sections = [
        "## Quick Reference",
        "## Regras de Ouro",
        "## Anti-Patterns",
        "## Application",
        "## References",
    ]
    # Flexible: check for partial matches
    for section in required_sections:
        section_name = section.replace("## ", "")
        if section_name.lower() not in output.lower():
            issues.append(f"Missing section: {section}")

    # Check no unfilled placeholders remain
    import re

    placeholders = re.findall(r"\{\{[A-Z_]+\}\}", output)
    if placeholders:
        issues.append(f"Unfilled placeholders: {placeholders[:5]}")

    # Check minimum density (rough: non-empty lines / total lines)
    lines = output.strip().split("\n")
    non_empty = [l for l in lines if l.strip()]
    if len(lines) > 0:
        density = len(non_empty) / len(lines)
        if density < 0.75:
            issues.append(f"Low density: {density:.2f} (min 0.75)")

    return issues


def load_index() -> dict:
    """Load the library index.yaml."""
    if INDEX_PATH.exists():
        return yaml.safe_load(INDEX_PATH.read_text(encoding="utf-8")) or {}
    return {"version": "1.0.0", "sources": {}, "domains": {}, "coverage": {}}


def save_index(index: dict):
    """Save the library index.yaml."""
    INDEX_PATH.write_text(
        yaml.dump(index, default_flow_style=False, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )


def inject_frontmatter(prompt: str, source_path: str, kc_type: str, feeds_kinds: list[str]) -> str:
    """Inject KC-Source metadata into the distill prompt."""
    origin = Path(source_path).stem if source_path else "manual"
    feeds_str = ", ".join(feeds_kinds) if feeds_kinds else "P04_tools"
    injection = f"""
### FRONTMATTER OBRIGATORIO (adicione ao output):
- type: {kc_type}
- origin: {origin}
- feeds_kinds: [{feeds_str}]
- created: {date.today().isoformat()}
- updated: {date.today().isoformat()}
"""
    return prompt + injection


def update_domain_index(kc_name: str, kc_type: str, origin: str, feeds_kinds: list[str]):
    """Register a new domain KC in index.yaml."""
    index = load_index()
    if "domains" not in index or not isinstance(index["domains"], dict):
        index["domains"] = {}
    index["domains"][kc_name] = {
        "type": kc_type,
        "origin": origin,
        "feeds_kinds": feeds_kinds,
        "created": date.today().isoformat(),
    }
    save_index(index)


def main():
    p = argparse.ArgumentParser(description="CEX Distill -- Template-driven knowledge extraction")
    p.add_argument("--input", type=str, help="Path to raw input file")
    p.add_argument("--type", type=str, default="knowledge_card", help="Artifact type")
    p.add_argument("--output", type=str, help="Output path (default: stdout)")
    p.add_argument("--dry-run", action="store_true", help="Show prompt without executing")
    p.add_argument("--list-types", action="store_true", help="List available types")
    p.add_argument("--validate", type=str, help="Validate existing file against template")
    p.add_argument("--source", type=str, help="KC-Source path (auto-sets origin)")
    p.add_argument(
        "--feeds", type=str, help="Comma-separated feeds_kinds (e.g. P04_tools,P08_architecture)"
    )
    p.add_argument(
        "--kc-type", type=str, default="domain", help="KC type: domain or meta (default: domain)"
    )

    a = p.parse_args()

    if a.list_types:
        print("Available artifact types:")
        for t, path in TYPE_TO_TEMPLATE.items():
            exists = "OK" if (CEX_ROOT / path).exists() else "MISSING"
            print(f"  {t:25s} -> {path} [{exists}]")
        return

    if a.validate:
        template = get_template(a.type)
        output = Path(a.validate).read_text(encoding="utf-8")
        issues = validate_output(output, template)
        if issues:
            print(f"[FAIL] {len(issues)} issues:")
            for i in issues:
                print(f"  [FAIL] {i}")
            sys.exit(1)
        else:
            print("[PASS] All template fields present")
        return

    # Resolve --source: use as --input if --input not given
    if a.source and not a.input:
        a.input = a.source

    if not a.input:
        p.print_help()
        return

    template = get_template(a.type)
    raw_path = Path(a.input)

    if not raw_path.exists():
        print(f"[ERROR] Input not found: {raw_path}")
        sys.exit(1)

    raw_content = raw_path.read_text(encoding="utf-8")
    prompt = build_distill_prompt(template, raw_content, raw_path.name)

    # Inject KC-Source metadata if --source or --feeds provided
    feeds_kinds = [f.strip() for f in a.feeds.split(",")] if a.feeds else []
    if a.source or a.feeds:
        prompt = inject_frontmatter(
            prompt,
            source_path=a.source or a.input,
            kc_type=a.kc_type,
            feeds_kinds=feeds_kinds,
        )

    if a.dry_run:
        print(f"[DRY RUN] Prompt ({len(prompt)} chars):")
        print("=" * 60)
        print(prompt[:2000])
        print("..." if len(prompt) > 2000 else "")
        print("=" * 60)
        print(f"\nTemplate: {a.type}")
        print(f"Input: {raw_path} ({len(raw_content)} chars)")
        if a.source:
            print(f"Source: {a.source} (origin: {Path(a.source).stem})")
        if feeds_kinds:
            print(f"Feeds: {feeds_kinds}")
        print(f"KC type: {a.kc_type}")
        print(f"Prompt size: {len(prompt)} chars")
        return

    # If not dry-run, output the prompt for piping to LLM
    if a.output:
        Path(a.output).write_text(prompt, encoding="utf-8")
        print(f"[OK] Prompt saved to {a.output}")
    else:
        print(prompt)

    # Auto-update index.yaml if --source provided
    if a.source:
        origin = Path(a.source).stem
        kc_name = f"kc_{origin.replace('src_', '')}"
        update_domain_index(kc_name, a.kc_type, origin, feeds_kinds)
        print(f"[OK] Registered {kc_name} in index.yaml", file=sys.stderr)


if __name__ == "__main__":
    main()
