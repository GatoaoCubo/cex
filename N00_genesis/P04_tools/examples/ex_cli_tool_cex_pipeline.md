---
id: p04_ct_cex_pipeline
kind: cli_tool
8f: F5_call
pillar: P04
title: "CEX Pipeline — 5-stage build engine (capture to envelope)"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, core, pipeline, build, stages]
cli_command: "python _tools/cex_pipeline.py"
cli_args:
  - name: "--type"
    type: string
    required: false
    description: "Artifact type (e.g. knowledge_card, agent, skill)"
  - name: "--topic"
    type: string
    required: false
    description: "Topic or subject of the artifact"
  - name: "--pillar"
    type: string
    required: false
    description: "Pillar code (e.g. P01). Auto-detected if omitted."
  - name: "--content"
    type: string
    required: false
    description: "Raw content to include in the body"
  - name: "--author"
    type: string
    required: false
    description: "Author name (default: pipeline)"
  - name: "--domain"
    type: string
    required: false
    description: "Domain name (default: general)"
  - name: "--output-kind"
    type: string
    required: false
    description: "Output kind: example or template (default: example)"
  - name: "--interactive"
    type: boolean
    required: false
    description: "Interactive mode with prompts"
  - name: "--from-file"
    type: string
    required: false
    description: "Read input from a markdown file"
  - name: "--dry-run"
    type: boolean
    required: false
    description: "Show what would be created without writing"
inputs: ["artifact type", "topic", "pillar", "optional content/file"]
outputs: ["complete .md artifact with frontmatter", "compiled .yaml/.json in compiled/"]
dependencies: ["pyyaml"]
category: core
quality: 9.1
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - p04_ct_distill
  - p04_ct_cex_forge
  - bld_schema_model_registry
  - p04_ct_cex_compile
  - bld_schema_input_schema
  - bld_schema_dataset_card
  - n06_schema_brand_config
  - bld_schema_multimodal_prompt
  - p06_is_knowledge_data_model
  - bld_schema_e2e_eval
---

## Purpose
Transforms user input into complete CEX artifacts through 5 stages: CAPTURE (gather input) > DECOMPOSE (parse intent) > HYDRATE (enrich with schema/template) > COMPILE (generate .md + compiled/) > ENVELOPE (wrap with metadata). Produces dual output: markdown source + compiled machine format.

## Usage
```bash
# Generate knowledge card
python _tools/cex_pipeline.py --type knowledge_card --topic "error handling" --pillar P01

# Interactive mode
python _tools/cex_pipeline.py --interactive

# From existing file
python _tools/cex_pipeline.py --from-file input.md

# Dry-run (preview without writing)
python _tools/cex_pipeline.py --type agent --topic "scraper" --pillar P02 --dry-run
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | string | yes* | Artifact type |
| `--topic` | string | yes* | Topic/subject |
| `--pillar` | string | no | LP code (auto-detected) |
| `--content` | string | no | Raw body content |
| `--author` | string | no | Author (default: pipeline) |
| `--domain` | string | no | Domain (default: general) |
| `--output-kind` | string | no | example or template |
| `--interactive` | flag | no | Interactive prompt mode |
| `--from-file` | string | no | Input from markdown file |
| `--dry-run` | flag | no | Preview without writing |

*Required unless `--interactive` or `--from-file` is used.

## Pipeline Position
**8F Function**: PRODUCE (F6) + GOVERN (F7) — produces artifacts and validates them.
**Stage**: End-to-end pipeline. Alternative to the Motor 8F + Crew Runner chain for simpler single-artifact generation.

## Dependencies
- `_schema.yaml` per LP for type validation and constraints
- `archetypes/TYPE_TO_TEMPLATE.yaml` for template mapping
- Output feeds into `cex_compile.py` if not auto-compiled

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ct_distill]] | sibling | 0.38 |
| [[p04_ct_cex_forge]] | sibling | 0.37 |
| [[bld_schema_model_registry]] | downstream | 0.31 |
| [[p04_ct_cex_compile]] | sibling | 0.30 |
| [[bld_schema_input_schema]] | downstream | 0.30 |
| [[bld_schema_dataset_card]] | downstream | 0.28 |
| [[n06_schema_brand_config]] | downstream | 0.28 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.28 |
| [[p06_is_knowledge_data_model]] | downstream | 0.27 |
| [[bld_schema_e2e_eval]] | downstream | 0.27 |
