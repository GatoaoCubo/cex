---
id: "p04_cli_{{TOOL_SLUG}}"
kind: cli_tool
8f: F5_call
pillar: P04
version: 1.0.0
title: Template - Cli Tool
tags: [template, cli, tool, typer, command-line]
tldr: CLI tool with commands, args, options, and Rich output. Built with Typer for modern Python CLI.
quality: 9.0
updated: "2026-04-07"
domain: "tool integration"
author: n03_builder
created: "2026-04-07"
density_score: 0.95
related:
  - cli-tool-builder
  - p11_qg_cli_tool
  - p10_lr_cli_tool_builder
  - bld_instruction_cli_tool
  - bld_examples_cli_tool
  - bld_knowledge_card_cli_tool
  - p03_sp_cli_tool_builder
  - bld_output_template_cli_tool
  - bld_collaboration_cli_tool
  - p04_ex_software_project_cli_tool
---

# Cli Tool: [NAME]

## Purpose
[WHAT this cli_tool does]
## Configuration
```yaml
name: "[CLI_NAME]"
framework: [typer | click | argparse]
entry_point: "[package.cli:app]"
```
## Commands
| Command | Args | Options | Description |
|---------|------|---------|-------------|
| run | input (req) | --output, --verbose | Execute main task |
| list | -- | --kind, --limit | List artifacts |
| score | path (req) | --apply, --dry-run | Score artifact |
## Output
1. `rich.console.Console` for color
2. `rich.table.Table` for structured data
3. `--json` flag for machine-readable
## Error Handling
1. Invalid args: Typer auto-validates + help
2. File not found: Rich error panel
3. Exit codes: 0=ok, 1=error, 2=validation
## Quality Gate
1. [ ] Entry point in pyproject.toml
2. [ ] --help on all commands
3. [ ] Exit codes documented
4. [ ] --json flag supported

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `cli_tool` |
| Pillar | P04 |
| Domain | tool integration |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[cli-tool-builder]] | related | 0.34 |
| [[p11_qg_cli_tool]] | downstream | 0.34 |
| [[p10_lr_cli_tool_builder]] | downstream | 0.33 |
| [[bld_instruction_cli_tool]] | upstream | 0.33 |
| [[bld_examples_cli_tool]] | downstream | 0.31 |
| [[bld_knowledge_card_cli_tool]] | upstream | 0.29 |
| [[p03_sp_cli_tool_builder]] | related | 0.28 |
| [[bld_output_template_cli_tool]] | downstream | 0.27 |
| [[bld_collaboration_cli_tool]] | downstream | 0.26 |
| [[p04_ex_software_project_cli_tool]] | related | 0.26 |
