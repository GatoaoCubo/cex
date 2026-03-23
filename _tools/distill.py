import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")
"""
CEX Distill — Transforms raw input into template-compliant artifacts.

The template IS the prompt. Not optional. Not a reference.

Usage:
  python distill.py --input raw_file.pdf --type knowledge_card
  python distill.py --input raw_file.pdf --type knowledge_card --dry-run
  python distill.py --list-types
"""
import sys
import argparse
from pathlib import Path

# Map artifact type → template file
TYPE_TO_TEMPLATE = {
    "knowledge_card":       "P01_knowledge/templates/tpl_knowledge_card_domain.md",
    "knowledge_card_meta":  "P01_knowledge/templates/tpl_knowledge_card_meta.md",
    "knowledge_card_test":  "P01_knowledge/templates/tpl_knowledge_card_test.md",
}

CEX_ROOT = Path(__file__).parent.parent  # _tools/ → CEX/


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

Voce recebeu um insumo RAW e um TEMPLATE obrigatorio.
Seu trabalho: PREENCHER o template com conhecimento EXTRAIDO + EXPANDIDO do insumo.

### REGRAS:
1. TODOS os campos {{{{PLACEHOLDER}}}} devem ser preenchidos — nenhum pode ficar vazio
2. NAO copie verbatim do insumo — TRANSFORME em conhecimento acionavel
3. EXPANDA alem do insumo — use seu conhecimento para enriquecer
4. O insumo eh SEMENTE, nao limite — se o insumo eh basico, o output deve ser avancado
5. Preencha 'when_to_use' pensando: "uma LLM com ZERO contexto, quando carregaria isso?"
6. Preencha 'axioms' com regras IMPERATIVAS que mudam comportamento
7. Preencha 'Anti-Patterns' com erros que uma LLM cometeria sem esse knowledge
8. Preencha 'Application' com uso CONCRETO no contexto de AI agent systems
9. density_score >= 0.85 — cada frase deve carregar informacao, zero filler

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
    required_fields = ["id:", "type:", "tldr:", "when_to_use:", "axioms:", 
                       "linked_artifacts:", "density_score:"]
    for field in required_fields:
        if field not in output:
            issues.append(f"Missing frontmatter: {field}")

    # Check required sections
    required_sections = ["## Quick Reference", "## Regras de Ouro", 
                         "## Anti-Patterns", "## Application", "## References"]
    # Flexible: check for partial matches
    for section in required_sections:
        section_name = section.replace("## ", "")
        if section_name.lower() not in output.lower():
            issues.append(f"Missing section: {section}")

    # Check no unfilled placeholders remain
    import re
    placeholders = re.findall(r'\{\{[A-Z_]+\}\}', output)
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


def main():
    p = argparse.ArgumentParser(description="CEX Distill — Template-driven knowledge extraction")
    p.add_argument("--input", type=str, help="Path to raw input file")
    p.add_argument("--type", type=str, default="knowledge_card", help="Artifact type")
    p.add_argument("--output", type=str, help="Output path (default: stdout)")
    p.add_argument("--dry-run", action="store_true", help="Show prompt without executing")
    p.add_argument("--list-types", action="store_true", help="List available types")
    p.add_argument("--validate", type=str, help="Validate existing file against template")

    a = p.parse_args()

    if a.list_types:
        print("Available artifact types:")
        for t, path in TYPE_TO_TEMPLATE.items():
            exists = "OK" if (CEX_ROOT / path).exists() else "MISSING"
            print(f"  {t:25s} → {path} [{exists}]")
        return

    if a.validate:
        template = get_template(a.type)
        output = Path(a.validate).read_text(encoding="utf-8")
        issues = validate_output(output, template)
        if issues:
            print(f"[FAIL] {len(issues)} issues:")
            for i in issues:
                print(f"  ❌ {i}")
            sys.exit(1)
        else:
            print("[PASS] All template fields present")
        return

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

    if a.dry_run:
        print(f"[DRY RUN] Prompt ({len(prompt)} chars):")
        print("=" * 60)
        print(prompt[:2000])
        print("..." if len(prompt) > 2000 else "")
        print("=" * 60)
        print(f"\nTemplate: {a.type}")
        print(f"Input: {raw_path} ({len(raw_content)} chars)")
        print(f"Prompt size: {len(prompt)} chars")
        return

    # If not dry-run, output the prompt for piping to LLM
    if a.output:
        Path(a.output).write_text(prompt, encoding="utf-8")
        print(f"[OK] Prompt saved to {a.output}")
    else:
        print(prompt)


if __name__ == "__main__":
    main()
