---
id: p04_ct_bootstrap
kind: cli_tool
8f: F5_call
pillar: P04
title: "CEX Bootstrap — Create project from selected Leverage Points"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, product, bootstrap, setup, project]
cli_command: "python _tools/bootstrap.py"
cli_args:
  - name: "--name"
    type: string
    required: true
    description: "Project name (creates directory)"
  - name: "--lps"
    type: string
    required: false
    description: "Comma-separated LP codes (default: all). Ex: P01,P02,P03"
  - name: "--with-examples"
    type: boolean
    required: false
    description: "Include examples/ from each LP"
  - name: "--with-tools"
    type: boolean
    required: false
    description: "Include _tools/ validators"
  - name: "--output"
    type: string
    required: false
    description: "Parent directory for project (default: current)"
inputs: ["project name", "optional LP selection"]
outputs: ["new CEX project directory with selected pillars, schemas, templates"]
dependencies: ["pyyaml"]
category: product
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - p04_ct_cex_init
  - p04_ct_cex_compile
  - p04_ct_cex_forge
  - p04_ct_cex_pipeline
  - p04_ct_validate_schema
  - p04_tool_software_project
  - p06_is_creation_data
  - p04_output_github_actions
  - p04_ct_validate_builder
  - p04_ct_distill
---

## Purpose
Creates a new CEX project from selected Leverage Points (P01-P12). Lighter than cex_init — copies pillar structure, schemas, and templates without the interactive questionnaire. Supports partial LP selection for focused projects.

## Usage
```bash
# Full project (all LPs)
python _tools/bootstrap.py --name MeuProjeto

# Selected LPs only
python _tools/bootstrap.py --name MeuProjeto --lps P01,P02,P03

# With examples and tools
python _tools/bootstrap.py --name MeuProjeto --lps P01,P02 --with-examples --with-tools

# Custom output directory
python _tools/bootstrap.py --name MeuProjeto --output /tmp/projects/
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--name` | string | yes | Project name |
| `--lps` | string | no | LP codes (default: all P01-P12) |
| `--with-examples` | flag | no | Copy examples/ |
| `--with-tools` | flag | no | Copy _tools/ |
| `--output` | string | no | Parent directory (default: .) |

## Pipeline Position
**8F Function**: CONSTRAIN (F1) — creates the structural foundation.
**Stage**: Genesis. Alternative to cex_init for programmatic project creation without interactive mode.

## Dependencies
- CEX root as template source
- Copies: _schema.yaml, templates/, optionally examples/ and _tools/

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ct_cex_init]] | sibling | 0.45 |
| [[p04_ct_cex_compile]] | sibling | 0.32 |
| [[p04_ct_cex_forge]] | sibling | 0.28 |
| [[p04_ct_cex_pipeline]] | sibling | 0.27 |
| [[p04_ct_validate_schema]] | sibling | 0.22 |
| [[p04_tool_software_project]] | sibling | 0.21 |
| [[p06_is_creation_data]] | downstream | 0.20 |
| [[p04_output_github_actions]] | related | 0.20 |
| [[p04_ct_validate_builder]] | sibling | 0.19 |
| [[p04_ct_distill]] | sibling | 0.19 |
