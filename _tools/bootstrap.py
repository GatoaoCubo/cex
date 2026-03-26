import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")
#!/usr/bin/env python3
"""CEX Bootstrap — creates a new CEX project from selected Leverage Points."""

import argparse
import shutil
import sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent

ALL_LPS = [
    "P01_knowledge",
    "P02_model",
    "P03_prompt",
    "P04_tools",
    "P05_output",
    "P06_schema",
    "P07_evals",
    "P08_architecture",
    "P09_config",
    "P10_memory",
    "P11_feedback",
    "P12_orchestration",
]

LP_CODES = {lp.split("_")[0]: lp for lp in ALL_LPS}

LP_DESCRIPTIONS = {
    "P01": "O que o agente SABE",
    "P02": "QUEM o agente EH",
    "P03": "COMO o agente FALA",
    "P04": "O que o agente USA",
    "P05": "O que o agente ENTREGA",
    "P06": "CONTRATOS de validacao",
    "P07": "COMO medir qualidade",
    "P08": "COMO escala",
    "P09": "COMO configura",
    "P10": "O que LEMBRA",
    "P11": "COMO melhora",
    "P12": "COMO coordena",
}


def resolve_lps(lps_arg: str | None) -> list[str]:
    """Resolve LP codes (P01,P02) to full directory names."""
    if not lps_arg:
        return list(ALL_LPS)

    selected = []
    for code in lps_arg.upper().split(","):
        code = code.strip()
        if code in LP_CODES:
            selected.append(LP_CODES[code])
        else:
            print(f"WARNING: Unknown LP '{code}', skipping. Valid: {', '.join(LP_CODES.keys())}")
    return selected


def copy_lp(lp_dir: Path, dest: Path, with_examples: bool) -> dict:
    """Copy schema, generator, templates (and optionally examples) for one LP."""
    lp_name = lp_dir.name
    lp_dest = dest / lp_name
    lp_dest.mkdir(parents=True, exist_ok=True)

    stats = {"schema": False, "generator": False, "templates": 0, "examples": 0}

    # _schema.yaml
    schema = lp_dir / "_schema.yaml"
    if schema.exists():
        shutil.copy2(schema, lp_dest / "_schema.yaml")
        stats["schema"] = True

    # _generator.md
    generator = lp_dir / "_generator.md"
    if generator.exists():
        shutil.copy2(generator, lp_dest / "_generator.md")
        stats["generator"] = True

    # templates/
    tpl_dir = lp_dir / "templates"
    if tpl_dir.exists() and any(tpl_dir.iterdir()):
        tpl_dest = lp_dest / "templates"
        shutil.copytree(tpl_dir, tpl_dest, dirs_exist_ok=True)
        stats["templates"] = len(list(tpl_dest.glob("*")))

    # examples/ (optional)
    if with_examples:
        ex_dir = lp_dir / "examples"
        if ex_dir.exists() and any(ex_dir.iterdir()):
            ex_dest = lp_dest / "examples"
            shutil.copytree(ex_dir, ex_dest, dirs_exist_ok=True)
            stats["examples"] = len(list(ex_dest.glob("*")))

    return stats


def generate_codex(dest: Path, project_name: str, lp_names: list[str]) -> None:
    """Generate a project-specific CODEX.md in archetypes/."""
    lp_table = []
    for lp in lp_names:
        code = lp.split("_")[0]
        desc = LP_DESCRIPTIONS.get(code, "")
        lp_table.append(f"| {code} | {lp.split('_', 1)[1].title()} | {desc} |")

    content = f"""# {project_name} — CODEX
## Gerado via CEX Bootstrap | LIVING

---

## PROPOSITO
Cerebro empresarial do projeto {project_name}.
Hierarquia: CODEX > _schema > _generator > templates > instances

## VARIAVEIS
- {{{{MUSTACHE}}}} = template engine resolve na geracao
- [BRACKET] = humano/agente resolve na autoria
- __auto__ = lifecycle preenche automatico

## ANATOMIA UNIVERSAL
YAML front: id, type, lp, quality, keywords(3+), long_tails(2+), bullets(3+), axioms(1+)
MD body: title, summary 1-line, secoes por tipo
Density >= 0.8 obrigatorio. Max 4KB.
Prosa > 3 linhas proibida. Bullets com max 80 chars.

## NAMING
Pattern: {{lp}}_{{type}}_{{topic}}.{{ext}}
Regras: lowercase, snake_case, ASCII, max 50 chars

## LEVERAGE POINTS ATIVOS

| LP | Nome | Descricao |
|----|------|-----------|
{chr(10).join(lp_table)}

## WORKFLOW
1. Escolher LP + tipo (consultar _schema.yaml)
2. Ler _generator.md (instrucoes passo-a-passo)
3. Usar template/ como base
4. Preencher variaveis e conteudo
5. Validar contra schema (density >= 0.8)

---
*Gerado por CEX Bootstrap | {len(lp_names)} LPs ativos*
"""
    (dest / "_meta").mkdir(parents=True, exist_ok=True)
    (dest / "_meta" / "CODEX.md").write_text(content, encoding="utf-8")


def generate_roadmap(dest: Path, project_name: str, lp_names: list[str]) -> None:
    """Generate a project-specific ROADMAP.md in archetypes/."""
    content = f"""# {project_name} — ROADMAP

---

## FASE 1: SETUP [COMPLETA]
- [x] Bootstrap com {len(lp_names)} LPs via CEX
- [x] Schemas e generators copiados
- [x] Templates prontos para uso

## FASE 2: PRIMEIROS ARTEFATOS
- [ ] Criar primeiro Knowledge Card (P01)
- [ ] Criar primeiro Agent spec (P02)
- [ ] Validar density >= 0.8

## FASE 3: PRODUCAO
- [ ] Gerar artefatos em escala
- [ ] Revisar e promover golden (quality >= 9.5)
- [ ] Integrar com pipeline do projeto

---
*Gerado por CEX Bootstrap*
"""
    (dest / "_meta").mkdir(parents=True, exist_ok=True)
    (dest / "_meta" / "ROADMAP.md").write_text(content, encoding="utf-8")


def generate_readme(dest: Path, project_name: str, lp_names: list[str], stats: dict) -> None:
    """Generate project README.md."""
    lp_list = []
    for lp in lp_names:
        code = lp.split("_")[0]
        name = lp.split("_", 1)[1].title()
        desc = LP_DESCRIPTIONS.get(code, "")
        lp_list.append(f"- **{code} {name}**: {desc}")

    content = f"""# {project_name}

Cerebro empresarial construido com [CEX](https://github.com/sniff-group/cex).

## Quick Start

```bash
# 1. Escolher LP e tipo
cat P01_knowledge/_schema.yaml   # ver tipos disponiveis

# 2. Ler instrucoes
cat P01_knowledge/_generator.md  # passo-a-passo

# 3. Usar template
cp P01_knowledge/templates/tpl_knowledge_card_domain.md meu_kc.md

# 4. Editar e preencher
# Substituir variaveis, adicionar conteudo denso

# 5. Validar
# Density >= 0.8 | Quality >= 7.0
```

## Leverage Points

{chr(10).join(lp_list)}

## Estrutura

```
{project_name}/
  archetypes/           # CODEX + ROADMAP (comece aqui)
  P*/               # Leverage Points
    _schema.yaml   # Contrato de tipos
    _generator.md  # Instrucoes de geracao
    templates/     # Base para novos artefatos
    examples/      # Exemplos reais (se --with-examples)
```

## Stats

- LPs: {stats["total_lps"]}
- Schemas: {stats["total_schemas"]}
- Generators: {stats["total_generators"]}
- Templates: {stats["total_templates"]}
- Examples: {stats["total_examples"]}

---
*Gerado por CEX Bootstrap*
"""
    (dest / "README.md").write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="CEX Bootstrap — create a new CEX project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
        "  python bootstrap.py --name MeuProjeto\n"
        "  python bootstrap.py --name MeuProjeto --lps P01,P02,P03\n"
        "  python bootstrap.py --name MeuProjeto --with-examples --with-tools\n",
    )
    parser.add_argument("--name", required=True, help="Project name (creates directory)")
    parser.add_argument(
        "--lps", default=None, help="Comma-separated LP codes (default: all). Ex: P01,P02,P03"
    )
    parser.add_argument(
        "--with-examples", action="store_true", help="Include examples/ from each LP"
    )
    parser.add_argument("--with-tools", action="store_true", help="Include _tools/ (validators)")
    parser.add_argument(
        "--output", default=".", help="Parent directory for project (default: current)"
    )
    args = parser.parse_args()

    # Resolve LPs
    selected_lps = resolve_lps(args.lps)
    if not selected_lps:
        print("ERROR: No valid LPs selected.")
        sys.exit(1)

    # Create project directory
    dest = Path(args.output).resolve() / args.name
    if dest.exists():
        print(f"ERROR: Directory '{dest}' already exists.")
        sys.exit(1)

    dest.mkdir(parents=True)
    print(f"Creating project '{args.name}' at {dest}")
    print(f"LPs: {', '.join(lp.split('_')[0] for lp in selected_lps)}")

    # Copy LPs
    totals = {
        "total_lps": 0,
        "total_schemas": 0,
        "total_generators": 0,
        "total_templates": 0,
        "total_examples": 0,
    }

    for lp_name in selected_lps:
        lp_dir = CEX_ROOT / lp_name
        if not lp_dir.exists():
            print(f"  SKIP: {lp_name} not found in CEX root")
            continue

        stats = copy_lp(lp_dir, dest, args.with_examples)
        totals["total_lps"] += 1
        totals["total_schemas"] += 1 if stats["schema"] else 0
        totals["total_generators"] += 1 if stats["generator"] else 0
        totals["total_templates"] += stats["templates"]
        totals["total_examples"] += stats["examples"]

        parts = []
        if stats["schema"]:
            parts.append("schema")
        if stats["generator"]:
            parts.append("generator")
        if stats["templates"]:
            parts.append(f"{stats['templates']} tpl")
        if stats["examples"]:
            parts.append(f"{stats['examples']} ex")
        print(f"  {lp_name}: {', '.join(parts)}")

    # Copy _tools/ (optional)
    if args.with_tools:
        tools_src = CEX_ROOT / "_tools"
        if tools_src.exists():
            tools_dest = dest / "_tools"
            shutil.copytree(tools_src, tools_dest, dirs_exist_ok=True)
            tool_count = len(list(tools_dest.glob("*.py")))
            print(f"  _tools/: {tool_count} scripts copied")

    # Generate meta files
    generate_codex(dest, args.name, selected_lps)
    generate_roadmap(dest, args.name, selected_lps)
    generate_readme(dest, args.name, selected_lps, totals)
    print("  archetypes/: CODEX.md + ROADMAP.md generated")
    print("  README.md generated")

    # Summary
    print(f"\nProjeto criado em ./{args.name}/ com {totals['total_lps']} LPs")
    print(
        f"  {totals['total_schemas']} schemas | {totals['total_generators']} generators | "
        f"{totals['total_templates']} templates | {totals['total_examples']} examples"
    )
    print(f"\nNext: cat {args.name}/archetypes/CODEX.md")


if __name__ == "__main__":
    main()
