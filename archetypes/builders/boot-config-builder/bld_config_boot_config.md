---
kind: config
id: bld_config_boot_config
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
title: "Config Boot Config"
version: "1.0.0"
author: n03_builder
tags: [boot_config, builder, examples]
tldr: "Golden and anti-examples for boot config construction, demonstrating ideal structure and common pitfalls."
domain: "boot config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_memory_scope
  - bld_schema_boot_config
  - bld_config_model_card
  - bld_config_handoff_protocol
  - bld_config_retriever_config
  - bld_config_prompt_version
  - bld_collaboration_boot_config
  - bld_config_output_validator
  - bld_config_constraint_spec
  - bld_instruction_boot_config
---
# Config: boot_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_boot_{provider_slug}.md` | `p02_boot_claude_code.md` |
| Builder directory | kebab-case | `boot-config-builder/` |
| Frontmatter fields | snake_case | `mcp_config`, `system_prompt_ref` |
| Provider slug | snake_case, lowercase | `claude_code`, `cursor_ai`, `codex` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P02_model/examples/p02_boot_{provider_slug}.md`
- Compiled: `cex/P02_model/compiled/p02_boot_{provider_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~3000 bytes
- Density: >= 0.80
## Provider Enum (non-exhaustive, extensible)
| Provider | Slug | Runtime |
|----------|------|---------|
| Claude Code | claude_code | CLI terminal |
| Cursor AI | cursor_ai | IDE extension |
| Codex CLI | codex | CLI terminal |
| Windsurf | windsurf | IDE extension |
| Aider | aider | CLI terminal |
| Custom | costm_{name} | User-defined |
## Identity Block Rules
- name: human-readable agent name (not slug)
- role: one-sentence role description
- agent_group: real agent_group name or "agnostic" — never blank
## Constraints Rules
- All numeric fields must be integers (not strings)
- temperature must be float 0.0-2.0
- timeout_seconds: reasonable range (30-600)
- max_retries: 0-5 range

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_memory_scope]] | sibling | 0.34 |
| [[bld_schema_boot_config]] | upstream | 0.32 |
| [[bld_config_model_card]] | sibling | 0.32 |
| [[bld_config_handoff_protocol]] | sibling | 0.31 |
| [[bld_config_retriever_config]] | sibling | 0.31 |
| [[bld_config_prompt_version]] | sibling | 0.30 |
| [[bld_collaboration_boot_config]] | downstream | 0.30 |
| [[bld_config_output_validator]] | sibling | 0.29 |
| [[bld_config_constraint_spec]] | sibling | 0.28 |
| [[bld_instruction_boot_config]] | upstream | 0.28 |
