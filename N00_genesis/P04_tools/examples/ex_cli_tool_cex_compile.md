---
id: p04_ct_cex_compile
kind: cli_tool
pillar: P04
title: "CEX Compile — Markdown to YAML/JSON compiler"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, core, compile, yaml, json]
cli_command: "python _tools/cex_compile.py"
cli_args:
  - name: "file"
    type: string
    required: false
    description: "Single .md file to compile"
  - name: "--all"
    type: boolean
    required: false
    description: "Compile all examples in all LPs"
  - name: "--lp"
    type: string
    required: false
    description: "Compile all examples in a specific LP (e.g. P03)"
inputs: [".md files with YAML frontmatter"]
outputs: ["compiled .yaml or .json in {LP}/compiled/"]
dependencies: ["pyyaml"]
category: core
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - p04_ct_validate_schema
  - p04_ct_cex_forge
  - p04_ct_cex_pipeline
  - doctor
  - validate
  - p11_qg_artifact
  - p04_ct_bootstrap
  - p04_ct_validate_builder
  - p04_ct_fix_frontmatter
  - p04_ct_cex_index
---

## Purpose
Converts .md example files into compiled YAML or JSON for LLM consumption. Reads frontmatter + body, determines machine format from _schema.yaml, and writes to the LP's compiled/ directory.

## Usage
```bash
# Compile single file
python _tools/cex_compile.py P04_tools/examples/ex_cli_tool_cex_forge.md

# Compile all examples in one LP
python _tools/cex_compile.py --lp P04

# Compile everything across all LPs
python _tools/cex_compile.py --all
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `file` | positional | no | Single .md file path |
| `--all` | flag | no | Compile all LPs |
| `--lp` | string | no | Target LP (e.g. P03) |

At least one of `file`, `--all`, or `--lp` is required.

## Pipeline Position
**8F Function**: PRODUCE (F6) — transforms human-readable to machine-readable.
**Stage**: Final compilation stage. Runs after artifact generation (forge/pipeline/crew_runner). Output consumed by LLM context injection and cex_index.

## Dependencies
- `_schema.yaml` per LP for machine_format mapping (yaml vs json)
- Source .md files must have valid YAML frontmatter with `kind` field

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ct_validate_schema]] | sibling | 0.29 |
| [[p04_ct_cex_forge]] | sibling | 0.27 |
| [[p04_ct_cex_pipeline]] | sibling | 0.26 |
| [[doctor]] | downstream | 0.23 |
| [[validate]] | downstream | 0.23 |
| [[p11_qg_artifact]] | downstream | 0.22 |
| [[p04_ct_bootstrap]] | sibling | 0.22 |
| [[p04_ct_validate_builder]] | sibling | 0.21 |
| [[p04_ct_fix_frontmatter]] | sibling | 0.21 |
| [[p04_ct_cex_index]] | sibling | 0.20 |
