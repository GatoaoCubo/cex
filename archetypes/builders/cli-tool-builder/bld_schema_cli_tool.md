---
kind: schema
id: bld_schema_cli_tool
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for cli_tool
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: cli_tool
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_cli_{tool_slug}) | YES | - | Namespace compliance |
| kind | literal "cli_tool" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable tool name |
| commands | list[string], len >= 1 | YES | - | Exact command names exposed |
| output_format | enum: text, json, table, yaml | YES | text | Primary output format |
| exit_codes | map[int, string] | YES | - | Code-to-meaning mapping |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "cli_tool" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the tool does |
| config_file | string | REC | - | Config file path/format |
| verbose | boolean | REC | false | Supports --verbose flag |
| interactive | boolean | REC | false | Has interactive mode |
| env_vars | list[string] | REC | - | Environment variables used |
| platforms | list[enum: linux, macos, windows] | REC | - | Supported platforms |
## ID Pattern
Regex: `^p04_cli_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what the tool does, use case, who runs it
2. `## Commands` — each command: syntax, flags, args, behavior
3. `## Output` — output format, exit codes, stdout vs stderr
4. `## Configuration` — config file, env vars, defaults
## Constraints
- max_bytes: 1024 (body only — compact tool spec)
- naming: p04_cli_{tool_slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- commands list MUST match command names defined in ## Commands section
- quality: null always
- NO implementation code in body — spec only
