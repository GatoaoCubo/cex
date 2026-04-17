---
id: "p04_cli_{{TOOL_SLUG}}"
kind: cli_tool
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
