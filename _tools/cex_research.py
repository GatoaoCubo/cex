#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")
"""
CEX Research -- Generate structured research prompts that produce KC-Sources.

A KC-Source is a raw taxonomy table scraped/researched from official docs.
It feeds distill.py which transforms sources into domain Knowledge Cards.

Pipeline: cex_research.py -> src_{slug}.md -> distill.py -> kc_{topic}.md

Usage:
  python _tools/cex_research.py --topic "chunking" --sources "langchain,llamaindex"
  python _tools/cex_research.py --topic "chunking" --sources "langchain,llamaindex" --dry-run
  python _tools/cex_research.py --list-sources
  python _tools/cex_research.py --topic "eval" --sources "ragas,deepeval" --categories "metric,dataset,scorer"
"""
import argparse
import re
from datetime import date
from pathlib import Path

import yaml

CEX_ROOT = Path(__file__).parent.parent
LIBRARY_DIR = CEX_ROOT / "N00_genesis" / "P01_knowledge" / "library"
SOURCES_DIR = LIBRARY_DIR / "sources"
INDEX_PATH = LIBRARY_DIR / "index.yaml"

# Default categories per research domain
DEFAULT_CATEGORIES = [
    "Core Concept",
    "API/Class",
    "Pattern",
    "Config",
    "Integration",
    "Anti-Pattern",
]

# Research prompt template
RESEARCH_PROMPT = """## TAREFA: Research & Taxonomy Extraction

You are a technical researcher. Your task: create a STRUCTURED TAXONOMY
do topico "{topic}" usando as fontes listadas abaixo.

### FONTES OFICIAIS (use APENAS documentacao oficial):
{sources_list}

### CATEGORIAS para classificar cada termo:
{categories_list}

### REGRAS:
1. CADA linha da tabela deve ter TODAS as 5 colunas preenchidas
2. Term = nome oficial (classe, funcao, conceito) como aparece na doc
3. Source = qual framework/provider (ex: langchain, openai, anthropic)
4. Category = uma das categorias acima
5. Description = 1 frase descritiva (max 120 chars), SEM jargao desrequired
6. CEX Mapping = qual pilar/kind do CEX esse conhecimento alimenta
   Pilares: P01(Knowledge) P02(Model) P03(Prompt) P04(Tools) P05(Output)
            P06(Schema) P07(Evals) P08(Architecture) P09(Config)
            P10(Memory) P11(Feedback) P12(Orchestration)
7. Minimo 15 termos por fonte. Se a fonte tem mais, inclua mais.
8. Ordene por Source, depois Category, depois Term
9. NAO invente termos -- apenas termos que existem na documentacao oficial
10. Inclua version/date de quando a doc foi consultada

### OUTPUT FORMAT:

```markdown
# {{Topic}} Official Taxonomy
> Sources: Official docs only | Scraped: {{date}}
> Method: {{method}}
> Scope: {{sources}}

---

## {{Source 1}} ({{url}})

| Term | Source | Category | Description | CEX Mapping |
|------|--------|----------|-------------|-------------|
| ... | ... | ... | ... | P0X_kind |

---

## {{Source 2}} ({{url}})

| Term | Source | Category | Description | CEX Mapping |
|------|--------|----------|-------------|-------------|
| ... | ... | ... | ... | P0X_kind |
```

Retorne APENAS o markdown. Nada antes, nada depois.
"""


def slugify(text: str) -> str:
    """Convert text to a valid slug for filenames."""
    slug = text.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = slug.strip("_")
    return slug


def load_index() -> dict:
    """Load the library index.yaml."""
    if INDEX_PATH.exists():
        return yaml.safe_load(INDEX_PATH.read_text(encoding="utf-8")) or {}
    return {"version": "1.0.0", "sources": {}, "domains": {}, "coverage": {}}


def save_index(index: dict):
    """Save the library index.yaml."""
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(
        yaml.dump(index, default_flow_style=False, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )


def build_prompt(topic: str, sources: list[str], categories: list[str]) -> str:
    """Build the research prompt for a given topic and sources."""
    sources_list = "\n".join(
        f"- **{s}**: documentacao oficial em docs.{s}.com (ou equivalente)" for s in sources
    )
    categories_list = "\n".join(f"- {c}" for c in categories)
    return RESEARCH_PROMPT.format(
        topic=topic,
        sources_list=sources_list,
        categories_list=categories_list,
    )


def build_source_scaffold(topic: str, sources: list[str], categories: list[str]) -> str:
    """Build a scaffold source file (for when --scaffold is used)."""
    today = date.today().isoformat()
    header = f"""# {topic.title()} Official Taxonomy
> Sources: Official docs only | Scraped: {today}
> Method: cex_research.py scaffold
> Scope: {", ".join(sources)}

---
"""
    sections = []
    for src in sources:
        table = f"""
## {src.title()} (docs.{src}.com)

| Term | Source | Category | Description | CEX Mapping |
|------|--------|----------|-------------|-------------|
| _TODO_ | {src} | {categories[0]} | _fill from official docs_ | P01_knowledge_card |
"""
        sections.append(table)

    return header + "\n---\n".join(sections)


def update_index(slug: str, topic: str, sources: list[str], size_kb: int):
    """Register the new source in index.yaml."""
    index = load_index()
    if "sources" not in index:
        index["sources"] = {}

    key = f"src_{slug}"
    index["sources"][key] = {
        "path": f"library/sources/src_{slug}.md",
        "size_kb": size_kb,
        "topics": sources,
        "scraped": date.today().isoformat(),
    }
    save_index(index)
    return key


def list_sources():
    """List all existing KC-Sources."""
    index = load_index()
    sources = index.get("sources", {})
    if not sources:
        print("No sources registered in index.yaml")
        return

    print(f"KC-Sources ({len(sources)}):\n")
    for key, meta in sources.items():
        topics = ", ".join(meta.get("topics", []))
        size = meta.get("size_kb", "?")
        scraped = meta.get("scraped", "?")
        print(f"  {key:<35} {size:>3} KB  [{scraped}]  topics: {topics}")


def main():
    p = argparse.ArgumentParser(description="CEX Research -- KC-Source prompt generator")
    p.add_argument("--topic", type=str, help="Research topic (e.g. 'chunking', 'eval', 'agents')")
    p.add_argument(
        "--sources", type=str, help="Comma-separated source names (e.g. 'langchain,llamaindex')"
    )
    p.add_argument(
        "--categories", type=str, help="Comma-separated categories (default: standard set)"
    )
    p.add_argument("--dry-run", action="store_true", help="Show prompt without writing files")
    p.add_argument(
        "--scaffold", action="store_true", help="Generate scaffold source file (no LLM needed)"
    )
    p.add_argument(
        "--output", type=str, help="Custom output path (default: library/sources/src_{slug}.md)"
    )
    p.add_argument("--list-sources", action="store_true", help="List existing KC-Sources")

    a = p.parse_args()

    if a.list_sources:
        list_sources()
        return

    if not a.topic:
        p.print_help()
        return

    if not a.sources:
        print("[ERROR] --sources required (comma-separated list)")
        sys.exit(1)

    sources = [s.strip() for s in a.sources.split(",")]
    categories = (
        [c.strip() for c in a.categories.split(",")] if a.categories else DEFAULT_CATEGORIES
    )
    slug = slugify(a.topic)

    # Determine output path
    out_path = Path(a.output) if a.output else SOURCES_DIR / f"src_{slug}.md"

    if a.scaffold:
        content = build_source_scaffold(a.topic, sources, categories)
        if a.dry_run:
            print(f"[DRY RUN] Scaffold for src_{slug}.md ({len(content)} chars):")
            print("=" * 60)
            print(content)
            print("=" * 60)
            return

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")
        size_kb = out_path.stat().st_size // 1024
        key = update_index(slug, a.topic, sources, size_kb)
        print(f"[OK] Scaffold: {out_path}")
        print(f"[OK] Registered: {key} in index.yaml")
        return

    # Generate research prompt
    prompt = build_prompt(a.topic, sources, categories)

    if a.dry_run:
        print(f"[DRY RUN] Research prompt for '{a.topic}' ({len(prompt)} chars):")
        print(f"  Sources: {', '.join(sources)}")
        print(f"  Categories: {', '.join(categories)}")
        print(f"  Output: {out_path}")
        print("=" * 60)
        print(prompt[:3000])
        print("..." if len(prompt) > 3000 else "")
        print("=" * 60)
        return

    # Output prompt (for piping to LLM or saving)
    if a.output:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(prompt, encoding="utf-8")
        print(f"[OK] Prompt saved to {out_path}")
    else:
        print(prompt)

    # Register in index (even for prompt-only, marks intent)
    size_kb = len(prompt) // 1024
    key = update_index(slug, a.topic, sources, size_kb)
    print(f"[OK] Registered: {key} in index.yaml", file=sys.stderr)


if __name__ == "__main__":
    main()
