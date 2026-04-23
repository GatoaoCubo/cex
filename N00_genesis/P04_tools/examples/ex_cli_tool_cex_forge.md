---
id: p04_ct_cex_forge
kind: cli_tool
pillar: P04
title: "CEX Forge — Universal prompt generator for CEX artifacts"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, core, forge, generation, prompt]
cli_command: "python _tools/cex_forge.py"
cli_args:
  - name: "--lp"
    type: string
    required: false
    description: "Target LP (P01-P12)"
  - name: "--type"
    type: string
    required: false
    description: "Artifact type (e.g. knowledge_card, agent, skill)"
  - name: "--seeds"
    type: string
    required: false
    description: "Comma-separated seed words for context injection"
  - name: "--context"
    type: string
    required: false
    description: "Free-text context string"
  - name: "--context-file"
    type: string
    required: false
    description: "Path to file with context content"
  - name: "--list-types"
    type: boolean
    required: false
    description: "List all 69 available artifact types"
  - name: "--output"
    type: string
    required: false
    description: "Output file path (default: stdout)"
  - name: "--builder"
    type: boolean
    required: false
    description: "Inject builder ISOs as context (auto-detect)"
  - name: "--builder-only"
    type: boolean
    required: false
    description: "Use ONLY builder ISOs, skip template"
inputs: ["LP code", "artifact type", "seed words", "context text or file"]
outputs: ["LLM-ready prompt (2-8KB markdown)", "validation warnings"]
dependencies: ["pyyaml"]
category: core
quality: 9.1
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - p04_ct_distill
  - p04_ct_cex_pipeline
  - bld_collaboration_context_doc
  - bld_schema_kind
  - p04_ct_cex_compile
  - bld_schema_reranker_config
  - bld_architecture_kind
  - bld_collaboration_prompt_template
  - bld_schema_action_prompt
  - p04_ct_validate_builder
---

## Purpose
Reads _schema.yaml + TYPE_TO_TEMPLATE.yaml + seed words + context and assembles a complete LLM-ready prompt that produces valid CEX artifacts. Does NOT call LLM — generates the prompt only.

## Usage
```bash
# Generate knowledge card prompt
python _tools/cex_forge.py --lp P01 --type knowledge_card --seeds "RAG,embeddings,chunking" --context "texto sobre RAG"

# Generate agent prompt with context file
python _tools/cex_forge.py --lp P02 --type agent --seeds "scraper,web,data" --context-file research.md

# List all available types
python _tools/cex_forge.py --list-types

# List types for specific LP
python _tools/cex_forge.py --list-types --lp P01

# Use builder ISOs as context
python _tools/cex_forge.py --lp P02 --type agent --seeds "monitor" --builder
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--lp` | string | yes* | Target LP (P01-P12) |
| `--type` | string | yes* | Artifact type from schema |
| `--seeds` | string | yes* | Comma-separated seed words |
| `--context` | string | no | Free-text context |
| `--context-file` | string | no | File with context content |
| `--list-types` | flag | no | List available types (replaces required args) |
| `--output` | string | no | Output file (default: stdout) |
| `--builder` | flag | no | Inject builder ISOs as context |
| `--builder-only` | flag | no | Use ONLY builder ISOs, skip template |

*Required unless `--list-types` is used.

## Pipeline Position
**8F Function**: PRODUCE (F6) — generates the raw material that builders consume.
**Stage**: Entry point of the generation pipeline. Upstream of cex_crew_runner (which executes the prompts) and cex_compile (which compiles outputs).

## Dependencies
- `_schema.yaml` in each LP directory
- `archetypes/TYPE_TO_TEMPLATE.yaml` for type-to-template mapping
- `archetypes/builders/` for `--builder` mode (ISO files, 40KB budget)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ct_distill]] | sibling | 0.34 |
| [[p04_ct_cex_pipeline]] | sibling | 0.30 |
| [[bld_collaboration_context_doc]] | downstream | 0.27 |
| [[bld_schema_kind]] | downstream | 0.25 |
| [[p04_ct_cex_compile]] | sibling | 0.25 |
| [[bld_schema_reranker_config]] | downstream | 0.24 |
| [[bld_architecture_kind]] | downstream | 0.24 |
| [[bld_collaboration_prompt_template]] | upstream | 0.24 |
| [[bld_schema_action_prompt]] | downstream | 0.24 |
| [[p04_ct_validate_builder]] | sibling | 0.24 |
