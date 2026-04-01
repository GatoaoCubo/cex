---
id: "p04_cli_{{TOOL_SLUG}}"
kind: cli_tool
pillar: P04
version: 1.0.0
title: Template - Cli Tool
tags: [template, cli, tool, typer, command-line]
tldr: CLI tool with commands, args, options, and Rich output. Built with Typer for modern Python CLI.
quality: 8.6
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
- `rich.console.Console` for color
- `rich.table.Table` for structured data
- `--json` flag for machine-readable
## Error Handling
- Invalid args: Typer auto-validates + help
- File not found: Rich error panel
- Exit codes: 0=ok, 1=error, 2=validation
## Quality Gate
- [ ] Entry point in pyproject.toml
- [ ] --help on all commands
- [ ] Exit codes documented
- [ ] --json flag supported
