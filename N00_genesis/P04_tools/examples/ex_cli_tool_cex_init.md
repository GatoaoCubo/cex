---
id: p04_ct_cex_init
kind: cli_tool
pillar: P04
title: "CEX Init — Scaffold a new CEX project in 5 questions"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, product, scaffolding, init, setup]
cli_command: "python _tools/cex_init.py"
cli_args:
  - name: "--name"
    type: string
    required: false
    description: "Project name (creates directory)"
  - name: "--domain"
    type: string
    required: false
    description: "Business domain (engineering, marketing, etc)"
  - name: "--agents"
    type: integer
    required: false
    description: "Builder count (1, 3, 7, or custom)"
  - name: "--llm"
    type: string
    required: false
    description: "LLM provider (claude, openai, etc)"
  - name: "--quality"
    type: string
    required: false
    description: "Quality threshold (strict, balanced, relaxed)"
inputs: ["5 configuration answers (interactive or CLI args)"]
outputs: ["complete CEX project directory with pillars, nuclei, builders, tools, config"]
dependencies: ["pyyaml"]
category: product
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
---

## Purpose
Scaffolds a complete new CEX project structure through 5 questions: project name, business domain, builder count, LLM provider, and quality threshold. Creates all 12 pillars, selected nuclei, builder directories, tools, and configuration files.

## Usage
```bash
# Interactive mode (asks 5 questions)
python _tools/cex_init.py

# Non-interactive (all args provided)
python _tools/cex_init.py --name myproject --domain engineering --agents 3 --llm claude --quality strict
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--name` | string | no* | Project name |
| `--domain` | string | no* | Business domain |
| `--agents` | int | no* | Builder count |
| `--llm` | string | no* | LLM provider |
| `--quality` | string | no* | Quality threshold |

*All required for non-interactive mode. Omit all for interactive mode.

## Pipeline Position
**8F Function**: CONSTRAIN (F1) — establishes the project foundation and constraints.
**Stage**: Genesis. First tool run when starting a new CEX project. Creates the structure that all other tools operate on.

## Dependencies
- CEX root as template source for pillar structure, schemas, tools
- Creates: P01-P12 dirs, nuclei dirs, archetypes/builders/, _tools/, _meta/, .cex/
