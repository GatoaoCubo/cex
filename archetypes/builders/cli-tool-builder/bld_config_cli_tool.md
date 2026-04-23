---
kind: config
id: bld_config_cli_tool
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Cli Tool"
version: "1.0.0"
author: n03_builder
tags: [cli_tool, builder, examples]
tldr: "Golden and anti-examples for cli tool construction, demonstrating ideal structure and common pitfalls."
domain: "cli tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_cli_tool_builder
  - bld_config_output_validator
  - bld_config_retriever_config
  - bld_config_memory_scope
  - p03_sp_cli_tool_builder
  - bld_config_prompt_version
  - bld_examples_cli_tool
  - bld_schema_cli_tool
  - bld_config_handoff_protocol
  - bld_config_constraint_spec
---
# Config: cli_tool Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_cli_{tool_slug}.md` | `p04_cli_artifact_validator.md` |
| Builder directory | kebab-case | `cli-tool-builder/` |
| Frontmatter fields | snake_case | `output_format`, `exit_codes` |
| Tool slug | snake_case, lowercase, no hyphens | `artifact_validator`, `index_builder` |
| Command names | snake_case, verb or verb_noun | `validate`, `check_schema`, `build` |
| Flag names | kebab-case with `--` prefix | `--strict`, `--output-format` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_cli_{tool_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_cli_{tool_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2000 bytes
- Density: >= 0.80 (no filler)
## Output Format Enum
| Value | When to use |
|-------|-------------|
| text | Human-readable default, unstructured |
| json | Machine-parseable, piping to other tools |
| table | Tabular data display (columns, alignment) |
| yaml | Config-like structured output |
## Exit Code Conventions
| Code | Meaning |
|------|---------|
| 0 | Success — operation completed normally |
| 1 | General error — operation failed |
| 2 | Usage error — invalid args/flags |
| 3 | I/O error — file not found, permission denied |
| 126 | Permission denied — cannot execute |
| 127 | Command not found |
Rule: every cli_tool MUST define at least codes 0 and 1.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_cli_tool_builder]] | downstream | 0.35 |
| [[bld_config_output_validator]] | sibling | 0.35 |
| [[bld_config_retriever_config]] | sibling | 0.34 |
| [[bld_config_memory_scope]] | sibling | 0.34 |
| [[p03_sp_cli_tool_builder]] | upstream | 0.33 |
| [[bld_config_prompt_version]] | sibling | 0.33 |
| [[bld_examples_cli_tool]] | upstream | 0.33 |
| [[bld_schema_cli_tool]] | upstream | 0.31 |
| [[bld_config_handoff_protocol]] | sibling | 0.31 |
| [[bld_config_constraint_spec]] | sibling | 0.31 |
