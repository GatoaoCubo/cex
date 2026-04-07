---
kind: examples
id: bld_examples_cli_tool
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of cli_tool artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Examples Cli Tool"
version: "1.0.0"
author: n03_builder
tags: [cli_tool, builder, examples]
tldr: "Golden and anti-examples for cli tool construction, demonstrating ideal structure and common pitfalls."
domain: "cli tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: cli-tool-builder
## Golden Example
INPUT: "Create CLI tool for validating CEX artifacts against their schema"
OUTPUT:
```yaml
id: p04_cli_artifact_validator
kind: cli_tool
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
name: "CEX Artifact Validator"
commands:
  - validate
  - check_schema
  - list_kinds
output_format: json
exit_codes:
  0: "all gates passed"
  1: "hard gate failure"
  2: "soft score below threshold"
  3: "file not found or unreadable"
quality: null
tags: [cli_tool, validator, artifact, P04]
tldr: "Artifact validator CLI: 3 commands, JSON output, validates HARD+SOFT gates"
description: "CLI tool validating CEX artifacts against pillar schemas with HARD/SOFT gate scoring"
config_file: ".cex/validator.yaml"
verbose: true
interactive: false
env_vars: ["CEX_ROOT", "CEX_STRICT"]
platforms: [linux, macos, windows]
```
## Overview
Validates CEX artifacts against their pillar schema definitions.
Used by builders after production and by CI pipelines for quality enforcement.
## Commands
### validate
`cex-validate validate <file> [--strict] [--verbose]`
Validates a single artifact against its kind schema.
Flags:
- `--strict`: fail on any SOFT gate below 8.0 (default: warn only)
- `--verbose`: show each gate check with pass/fail detail
Args:
- `<file>` (path, required): artifact file to validate
Returns: JSON {passed, hard_gates, soft_score, failures[]}
### check_schema
`cex-validate check-schema <kind>`
Prints the schema for a given kind.
Args:
- `<kind>` (string, required): artifact kind (e.g., "client", "mcp_server")
Returns: JSON schema definition
### list_kinds
`cex-validate list-kinds [--pillar P04]`
Lists all registered artifact kinds.
Flags:
- `--pillar` (string, optional): filter by pillar
Returns: JSON [{kind, pillar, core, max_bytes}]
## Output
- stdout: JSON results (parseable by downstream tools)
- stderr: human-readable progress and errors
- Exit codes: 0=pass, 1=hard fail, 2=soft fail, 3=file error
## Configuration
Config file: `.cex/validator.yaml` (optional overrides)
Env vars: `CEX_ROOT` (project root), `CEX_STRICT` (enable strict mode)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_cli_ pattern (H02 pass)
- kind: cli_tool (H04 pass)
- 20 required+recommended fields present (H06 pass)
- body has all 4 sections: Overview, Commands, Output, Configuration (H07 pass)
- commands list matches ## Commands names exactly (S03 pass)
- exit_codes map with semantic meanings (S05 pass)
- tldr: 68 chars <= 160 (S01 pass)
- tags: 4 items, includes "cli_tool" (S02 pass)
- Each command has syntax, flags, args, return (S06 pass)
## Anti-Example
INPUT: "Create CLI tool for formatting code"
BAD OUTPUT:
```yaml
id: code-formatter
kind: tool
pillar: tools
name: Formatter
commands: [format]
quality: 9.0
tags: [format]
```
Formats code files.
## Commands
format: formats code
FAILURES:
1. id: "code-formatter" has hyphens and no `p04_cli_` prefix -> H02 FAIL
2. kind: "tool" not "cli_tool" -> H04 FAIL
3. pillar: "tools" not "P04" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. Missing fields: output_format, exit_codes, version, created, updated, author, tldr -> H06 FAIL
6. tags: only 1 item, missing "cli_tool" -> S02 FAIL
7. Body missing ## Output, ## Configuration sections -> H07 FAIL
8. Command entry has no syntax, flags, args, or return -> S06 FAIL
9. No exit_codes defined — caller cannot interpret result -> H06 FAIL
10. No output_format specified — consumer cannot parse -> H06 FAIL
