#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Init v1.0 -- Scaffold a new CEX project in 5 questions.

Interactive:
  python _tools/cex_init.py

Non-interactive:
  python _tools/cex_init.py --name myproject --domain engineering --agents 3 --llm claude --quality strict

Creates a functional CEX repo with pillars, nuclei, builders, tools, and config.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent

# -- Constants ----------------------------------------------------------------

ALL_PILLARS = [
    "N00_genesis/P01_knowledge",
    "N00_genesis/P02_model",
    "N00_genesis/P03_prompt",
    "N00_genesis/P04_tools",
    "N00_genesis/P05_output",
    "N00_genesis/P06_schema",
    "N00_genesis/P07_evals",
    "N00_genesis/P08_architecture",
    "N00_genesis/P09_config",
    "N00_genesis/P10_memory",
    "N00_genesis/P11_feedback",
    "N00_genesis/P12_orchestration",
]

PILLAR_DESCRIPTIONS = {
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

ALL_NUCLEI = {
    "N01_intelligence": "Research",
    "N02_marketing": "Marketing",
    "N03_engineering": "Engineering",
    "N04_knowledge": "Knowledge",
    "N05_operations": "Operations",
    "N06_commercial": "Commercial",
    "N07_admin": "Administration",
}

NUCLEUS_SUBDIRS = [
    "agents",
    "architecture",
    "config",
    "feedback",
    "knowledge",
    "memory",
    "orchestration",
    "output",
    "prompts",
    "quality",
    "schemas",
    "tools",
]

DOMAIN_NUCLEI = {
    "marketing": ["N02_marketing", "N06_commercial"],
    "engineering": ["N03_engineering", "N04_knowledge"],
    "research": ["N01_intelligence", "N04_knowledge"],
    "ops": ["N05_operations", "N07_admin"],
    "custom": list(ALL_NUCLEI.keys()),
}

CORE_BUILDERS = {
    1: ["agent-builder"],
    3: ["agent-builder", "knowledge-card-builder", "skill-builder"],
    7: [
        "agent-builder",
        "knowledge-card-builder",
        "skill-builder",
        "system-prompt-builder",
        "prompt-template-builder",
        "hook-builder",
        "workflow-builder",
    ],
}

QUALITY_THRESHOLDS = {
    "strict": {"min": 9.0, "density": 0.85},
    "standard": {"min": 8.0, "density": 0.80},
    "relaxed": {"min": 7.0, "density": 0.75},
}

COPY_TOOLS = ["cex_doctor.py", "validate_builder.py", "cex_compile.py"]

VALID_DOMAINS = ["marketing", "engineering", "research", "ops", "custom"]
VALID_LLMS = ["claude", "openai", "gemini", "multi"]
VALID_QUALITIES = ["strict", "standard", "relaxed"]


# -- Interactive prompts ------------------------------------------------------


def ask(prompt: str, default: str = "", options: list[str] | None = None) -> str:
    """Ask user a question with optional default and validation."""
    hint = ""
    if options:
        hint = f" [{'/'.join(options)}]"
    if default:
        hint += f" (default: {default})"

    while True:
        answer = input(f"  {prompt}{hint}: ").strip()
        if not answer and default:
            return default
        if options and answer.lower() not in options:
            print(f"    Invalid. Choose from: {', '.join(options)}")
            continue
        return answer.lower() if options else answer


def interactive_flow() -> dict:
    """Run 5-question interactive scaffold wizard."""
    print()
    print("=" * 60)
    print("  CEX Init -- Scaffold a new CEX project")
    print("=" * 60)
    print()

    dirname = Path.cwd().name
    name = ask("Q1. Project name", default=dirname)
    domain = ask("Q2. Domain", options=VALID_DOMAINS)

    print(f"    Agent count: 1=minimal, 3=starter, 7=full, or a number")
    agents_str = ask("Q3. Agent count", default="3", options=["1", "3", "7", "custom"])
    if agents_str == "custom":
        agents_str = ask("    How many builders? (enter number)", default="7")
    agents = int(agents_str) if agents_str.isdigit() else 3

    llm = ask("Q4. LLM provider", options=VALID_LLMS)
    quality = ask("Q5. Quality level", options=VALID_QUALITIES)

    print()
    return {
        "name": name,
        "domain": domain,
        "agents": agents,
        "llm": llm,
        "quality": quality,
    }


# -- Generators ---------------------------------------------------------------


def copy_pillars(dest: Path) -> dict:
    """Copy all 12 pillar dirs with _schema.yaml and _generator.md."""
    stats = {"schemas": 0, "generators": 0}
    for pillar in ALL_PILLARS:
        src = CEX_ROOT / pillar
        pillar_dest = dest / pillar
        pillar_dest.mkdir(parents=True, exist_ok=True)

        # _schema.yaml
        schema = src / "_schema.yaml"
        if schema.exists():
            shutil.copy2(schema, pillar_dest / "_schema.yaml")
            stats["schemas"] += 1

        # _generator.md
        gen = src / "_generator.md"
        if gen.exists():
            shutil.copy2(gen, pillar_dest / "_generator.md")
            stats["generators"] += 1

        # templates/ (if exist)
        tpl = src / "templates"
        if tpl.exists() and any(tpl.iterdir()):
            shutil.copytree(tpl, pillar_dest / "templates", dirs_exist_ok=True)

        # examples/ (if exist)
        ex = src / "examples"
        if ex.exists() and any(ex.iterdir()):
            shutil.copytree(ex, pillar_dest / "examples", dirs_exist_ok=True)

    return stats


def create_nuclei(dest: Path, domain: str) -> list[str]:
    """Create nucleus directories with subdirs based on domain."""
    nuclei = DOMAIN_NUCLEI.get(domain, DOMAIN_NUCLEI["custom"])
    created = []
    for nucleus in nuclei:
        nuc_dir = dest / nucleus
        nuc_dir.mkdir(parents=True, exist_ok=True)
        for subdir in NUCLEUS_SUBDIRS:
            (nuc_dir / subdir).mkdir(exist_ok=True)
        # README.md for each nucleus
        desc = ALL_NUCLEI.get(nucleus, "Domain")
        readme = f"# {nucleus}\n\nDomain: {desc}\n"
        (nuc_dir / "README.md").write_text(readme, encoding="utf-8")
        created.append(nucleus)
    return created


def copy_builders(dest: Path, agent_count: int) -> int:
    """Copy core builder directories based on agent count."""
    builders_src = CEX_ROOT / "archetypes" / "builders"
    if not builders_src.exists():
        return 0

    # Determine which builders to copy
    if agent_count in CORE_BUILDERS:
        selected = CORE_BUILDERS[agent_count]
    elif agent_count >= 7:
        # Copy all available builders
        selected = [
            d.name for d in builders_src.iterdir() if d.is_dir() and not d.name.startswith("_")
        ]
    else:
        # For custom counts between standard tiers, use the next tier up
        selected = CORE_BUILDERS[7] if agent_count > 3 else CORE_BUILDERS[3]

    builders_dest = dest / "archetypes" / "builders"
    builders_dest.mkdir(parents=True, exist_ok=True)

    copied = 0
    for builder_name in selected:
        src = builders_src / builder_name
        if src.exists():
            shutil.copytree(src, builders_dest / builder_name, dirs_exist_ok=True)
            copied += 1

    # Copy bld_norms.md if exists
    norms = builders_src / "bld_norms.md"
    if norms.exists():
        shutil.copy2(norms, builders_dest / "bld_norms.md")

    return copied


def copy_tools(dest: Path) -> int:
    """Copy essential CEX tools."""
    tools_src = CEX_ROOT / "_tools"
    tools_dest = dest / "_tools"
    tools_dest.mkdir(parents=True, exist_ok=True)

    copied = 0
    for tool_name in COPY_TOOLS:
        src = tools_src / tool_name
        if src.exists():
            shutil.copy2(src, tools_dest / tool_name)
            copied += 1
    return copied


def generate_codex(dest: Path, name: str, domain: str, quality: str) -> None:
    """Generate archetypes/CODEX.md customized for the project."""
    src = CEX_ROOT / "archetypes" / "CODEX.md"
    codex_dest = dest / "archetypes"
    codex_dest.mkdir(parents=True, exist_ok=True)

    if src.exists():
        content = src.read_text(encoding="utf-8")
        # Customize brand references
        content = content.replace(
            "# RECORDS CODEX -- Biblia Universal de Meta-Construcao",
            f"# {name.upper()} CODEX -- Biblia de Meta-Construcao",
        )
        qmin = QUALITY_THRESHOLDS[quality]["min"]
        dmin = QUALITY_THRESHOLDS[quality]["density"]
        content = content.replace(
            "Density >= 0.8 required.",
            f"Density >= {dmin} required. Quality min: {qmin}.",
        )
        (codex_dest / "CODEX.md").write_text(content, encoding="utf-8")
    else:
        # Fallback: generate minimal CODEX
        q = QUALITY_THRESHOLDS[quality]
        content = f"""# {name.upper()} CODEX
## DNA do Projeto | Domain: {domain}

---

## PROPOSITO
Knowledge base do projeto {name}.
Hierarquia: CODEX > _schema > _generator > templates > instances

## VARIAVEIS
- {{{{MUSTACHE}}}} = template engine resolve na geracao
- [BRACKET] = humano/agente resolve na autoria
- __auto__ = lifecycle preenche automatico

## ANATOMIA UNIVERSAL
YAML front: id, type, lp, quality, keywords(3+), long_tails(2+), bullets(3+), axioms(1+)
MD body: title, summary 1-line, secoes por tipo
Density >= {q["density"]} required. Quality min: {q["min"]}.
Max 4KB. Prosa > 3 linhas proibida. Bullets com max 80 chars.

## NAMING
Pattern: {{lp}}_{{type}}_{{topic}}.{{ext}}
Regras: lowercase, snake_case, ASCII, max 50 chars

---
*Gerado por CEX Init v1.0*
"""
        (codex_dest / "CODEX.md").write_text(content, encoding="utf-8")


def generate_claude_md(dest: Path, name: str, domain: str, quality: str) -> None:
    """Generate CLAUDE.md for Claude Code / Claude."""
    q = QUALITY_THRESHOLDS[quality]
    pillar_table = "\n".join(
        f"| {p.split('_')[0]} | {p.split('_', 1)[1].title()} | {PILLAR_DESCRIPTIONS.get(p.split('_')[0], '')} |"
        for p in ALL_PILLARS
    )

    content = f"""# {name} -- LLM Entry Point

> **You are inside a CEX repository.** Typed, indexed knowledge base
> for building LLM agents. Navigate by filename: `{{layer}}_{{kind}}_{{topic}}.{{ext}}`.

---

## Architecture (5 Layers)

| Layer | Location | Contains |
|-------|----------|----------|
| L0 DNA | `archetypes/builders/{{type}}-builder/` | 13 builder specs per builder |
| L1 Schema | `P01_knowledge/` -- `P12_orchestration/` | `_schema.yaml` + `templates/` |
| L2 Instance | `N*/` | Domain-specific instances |
| L3 Engine | `_tools/` | CLI pipeline, validators |
| L4 Root | `CLAUDE.md`, `README.md` | Entry points |

## 12 Pillars

| ID | Name | Description |
|----|------|-------------|
{pillar_table}

## Quality Gate

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Reference quality |
| >= {q["min"]} | Skilled | Published |
| >= 7.0 | Learning | Experimental |
| < 7.0 | Rejected | Redo |

Density minimum: {q["density"]}. YAML frontmatter required.

## Tools

| Tool | Command |
|------|---------|
| Doctor | `python _tools/cex_doctor.py` |
| Validate | `python _tools/validate_builder.py` |
| Compile | `python _tools/cex_compile.py --all` |

## Domain: {domain.title()}

---
*Gerado por CEX Init v1.0 | Quality: {quality} ({q["min"]})*
"""
    (dest / "CLAUDE.md").write_text(content, encoding="utf-8")


def generate_cursorrules(dest: Path, name: str, domain: str, quality: str) -> None:
    """Generate .cursorrules for Cursor/Windsurf/OpenAI-based editors."""
    q = QUALITY_THRESHOLDS[quality]
    content = f"""# {name} -- IDE Instructions

> **You are inside a CEX repository.** Typed, indexed knowledge base
> for building LLM agents. Navigate by filename: `{{layer}}_{{kind}}_{{topic}}.{{ext}}`.

---

## Architecture (5 Layers)

| Layer | Location | Contains |
|-------|----------|----------|
| L0 DNA | `archetypes/builders/{{type}}-builder/` | 13 builder specs per builder |
| L1 Schema | `P01_knowledge/` -- `P12_orchestration/` | `_schema.yaml` + `templates/` |
| L2 Instance | `N*/` | Domain-specific instances |
| L3 Engine | `_tools/` | CLI pipeline, validators |
| L4 Root | `README.md` | Entry points |

## Naming Grammar

```
bld_  = builder (L0)     | bld_system_prompt_agent.md
tpl_  = template (L1)    | tpl_knowledge_card.md
ex_   = example (L1)     | ex_knowledge_card_rag.md
```

Rules: lowercase, snake_case, ASCII only, max 50 chars.
Every artifact: dual output .md (human) + .yaml/.json (machine).

## Quality Gate

Minimum quality: {q["min"]} | Density: >= {q["density"]}

## Domain: {domain.title()}

---
*Gerado por CEX Init v1.0*
"""
    (dest / ".cursorrules").write_text(content, encoding="utf-8")


def generate_readme(
    dest: Path, name: str, domain: str, quality: str, nuclei: list[str], builders: int, stats: dict
) -> None:
    """Generate project README.md."""
    q = QUALITY_THRESHOLDS[quality]
    nuclei_list = "\n".join(f"- **{n}**: {ALL_NUCLEI.get(n, 'Custom')}" for n in nuclei)
    content = f"""# {name}

CEX-powered knowledge base for **{domain}** domain.

## Quick Start

```bash
# 1. Check health
python _tools/cex_doctor.py

# 2. Browse schemas
cat P01_knowledge/_schema.yaml

# 3. Read generator instructions
cat P01_knowledge/_generator.md

# 4. Create from template
cp P01_knowledge/templates/tpl_*.md my_artifact.md

# 5. Validate
python _tools/validate_builder.py archetypes/builders/agent-builder/
```

## Structure

```
{name}/
  archetypes/          # CODEX + builders (DNA layer)
    builders/          # {builders} builder(s) with 13 builder specs each
  P01-P12/             # 12 pillars (schema + generator + templates)
  N*/                  # {len(nuclei)} nuclei (domain instances)
  _tools/              # CLI pipeline
```

## Active Nuclei

{nuclei_list}

## Quality

| Metric | Value |
|--------|-------|
| Min quality | {q["min"]} |
| Min density | {q["density"]} |
| Level | {quality.title()} |
| Schemas | {stats["schemas"]} |
| Generators | {stats["generators"]} |
| Builders | {builders} |

---
*Scaffolded by [CEX](https://github.com/sniff-group/cex) Init v1.0*
"""
    (dest / "README.md").write_text(content, encoding="utf-8")


def generate_gitignore(dest: Path) -> None:
    """Generate .gitignore."""
    content = """# CEX project
__pycache__/
*.pyc
.env
.venv/

# Regenerable
.cex/index.db
compiled/

# IDE
.vscode/
.idea/
*.swp
"""
    (dest / ".gitignore").write_text(content, encoding="utf-8")


def generate_pre_commit(dest: Path) -> None:
    """Generate .githooks/pre-commit."""
    hooks_dir = dest / ".githooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)
    content = """#!/usr/bin/env bash
# CEX pre-commit hook -- runs governance checks before commit.
# Install: git config core.hooksPath .githooks

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
TIMEOUT_CMD=""
if command -v timeout &>/dev/null; then
    TIMEOUT_CMD="timeout 5"
fi

# Run cex_doctor.py
if [ -f "$REPO_ROOT/_tools/cex_doctor.py" ]; then
    echo "[pre-commit] Running cex_doctor.py..."
    if ! $TIMEOUT_CMD python "$REPO_ROOT/_tools/cex_doctor.py" 2>&1; then
        echo "[pre-commit] WARNING: cex_doctor.py found issues."
    fi
fi

echo "[pre-commit] Done."
exit 0
"""
    hook_path = hooks_dir / "pre-commit"
    hook_path.write_text(content, encoding="utf-8")
    # Make executable on Unix
    try:
        hook_path.chmod(0o755)
    except OSError:
        pass


def run_doctor(dest: Path) -> bool:
    """Run cex_doctor.py on scaffolded repo and return success."""
    doctor = dest / "_tools" / "cex_doctor.py"
    if not doctor.exists():
        print("  (cex_doctor.py not available, skipping health check)")
        return True

    print("\n--- Post-Init Health Check ---")
    try:
        result = subprocess.run(
            [sys.executable, str(doctor)],
            cwd=str(dest),
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.stdout:
            # Print summary lines only
            for line in result.stdout.splitlines():
                if line.startswith(("=", "Found", "Builder", "TOTAL", "Result")):
                    print(f"  {line}")
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as e:
        print(f"  Doctor check skipped: {e}")
        return True


# -- Main ---------------------------------------------------------------------


def scaffold(cfg: dict) -> None:
    """Execute full scaffold based on config dict."""
    name = cfg["name"]
    domain = cfg["domain"]
    agents = cfg["agents"]
    llm = cfg["llm"]
    quality = cfg["quality"]

    dest = Path.cwd() / name
    if dest.exists():
        print(f"ERROR: Directory '{dest}' already exists.")
        sys.exit(1)

    dest.mkdir(parents=True)
    print(f"\nScaffolding '{name}' at {dest}")
    print(f"  Domain: {domain} | Agents: {agents} | LLM: {llm} | Quality: {quality}")
    print()

    # 1. Pillars (P01-P12)
    print("[1/7] Copying 12 pillars (_schema.yaml + _generator.md)...")
    pillar_stats = copy_pillars(dest)
    print(f"  {pillar_stats['schemas']} schemas, {pillar_stats['generators']} generators")

    # 2. Nuclei (N01-N07 based on domain)
    print(f"[2/7] Creating nuclei for domain '{domain}'...")
    nuclei = create_nuclei(dest, domain)
    print(f"  {len(nuclei)} nuclei: {', '.join(nuclei)}")

    # 3. Builders
    print(f"[3/7] Copying builders (count={agents})...")
    builder_count = copy_builders(dest, agents)
    print(f"  {builder_count} builder(s) copied")

    # 4. Tools
    print("[4/7] Copying tools...")
    tool_count = copy_tools(dest)
    print(f"  {tool_count} tools copied")

    # 5. CODEX
    print("[5/7] Generating archetypes/CODEX.md...")
    generate_codex(dest, name, domain, quality)

    # 6. LLM config (CLAUDE.md / .cursorrules)
    print(f"[6/7] Generating LLM config ({llm})...")
    if llm in ("claude", "multi"):
        generate_claude_md(dest, name, domain, quality)
        print("  CLAUDE.md")
    if llm in ("openai", "gemini", "multi"):
        generate_cursorrules(dest, name, domain, quality)
        print("  .cursorrules")
    if llm == "claude":
        # Also generate .cursorrules as fallback for other editors
        generate_cursorrules(dest, name, domain, quality)
        print("  .cursorrules (fallback)")

    # 7. Git scaffolding
    print("[7/7] Generating .gitignore + .githooks/pre-commit...")
    generate_gitignore(dest)
    generate_pre_commit(dest)

    # README
    generate_readme(dest, name, domain, quality, nuclei, builder_count, pillar_stats)
    print("  README.md")

    # Post-init: run doctor
    doctor_ok = run_doctor(dest)

    # Summary
    print()
    print("=" * 60)
    print(f"  Project '{name}' created successfully!")
    print(
        f"  {pillar_stats['schemas']} schemas | {pillar_stats['generators']} generators | {builder_count} builders | {len(nuclei)} nuclei"
    )
    print()
    print(f"  cd {name}")
    print(f"  git init && git config core.hooksPath .githooks")
    print(f"  python _tools/cex_doctor.py")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="CEX Init v1.0 -- scaffold a new CEX project in 5 questions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python _tools/cex_init.py\n"
            "  python _tools/cex_init.py --name myproject --domain engineering --agents 3 --llm claude --quality strict\n"
            "  python _tools/cex_init.py --name brand --domain marketing --agents 7 --llm multi --quality standard\n"
        ),
    )
    parser.add_argument("--name", help="Project name (creates directory)")
    parser.add_argument("--domain", choices=VALID_DOMAINS, help="Business domain")
    parser.add_argument("--agents", type=int, help="Builder count (1, 3, 7, or custom)")
    parser.add_argument("--llm", choices=VALID_LLMS, help="LLM provider")
    parser.add_argument("--quality", choices=VALID_QUALITIES, help="Quality threshold")
    args = parser.parse_args()

    # If all args provided, run non-interactive
    if all([args.name, args.domain, args.agents, args.llm, args.quality]):
        cfg = {
            "name": args.name,
            "domain": args.domain,
            "agents": args.agents,
            "llm": args.llm,
            "quality": args.quality,
        }
    elif any([args.name, args.domain, args.agents, args.llm, args.quality]):
        print("ERROR: Provide ALL flags for non-interactive mode, or NONE for interactive.")
        print("  Required: --name --domain --agents --llm --quality")
        sys.exit(1)
    else:
        cfg = interactive_flow()

    scaffold(cfg)


if __name__ == "__main__":
    main()
