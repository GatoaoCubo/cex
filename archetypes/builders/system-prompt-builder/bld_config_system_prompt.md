---
kind: config
id: bld_config_system_prompt
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: [BashTool]
fork_context: inline
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: pillar
quality: 9.0
title: "Config System Prompt"
version: "1.0.0"
author: n03_builder
tags: [system_prompt, builder, examples]
tldr: "Golden and anti-examples for system prompt construction, demonstrating ideal structure and common pitfalls."
domain: "system prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_agent
  - bld_knowledge_card_system_prompt
  - bld_schema_system_prompt
  - bld_config_prompt_version
  - bld_config_agent_package
  - bld_config_kind
  - bld_config_constraint_spec
  - bld_config_mental_model
  - bld_collaboration_system_prompt
  - bld_config_memory_scope
---
# Config: system_prompt Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_sp_{agent_slug}.md` | `p03_sp_knowledge_card_builder.md` |
| Builder directory | kebab-case | `system-prompt-builder/` |
| Frontmatter fields | snake_case | `target_agent`, `rules_count` |
| Agent slug | snake_case, lowercase | `scout_agent`, `model_card_builder` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P03_prompt/examples/p03_sp_{agent_slug}.md`
- Compiled: `cex/P03_prompt/compiled/p03_sp_{agent_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80
## Tone Enum
| Value | When to use |
|-------|-------------|
| formal | Enterprise, compliance, legal agents |
| technical | Builder agents, infrastructure, code |
| conversational | User-facing, chat, support agents |
| authoritative | Governance, quality, security agents |
## Safety Level Enum
| Value | When to use |
|-------|-------------|
| standard | Most agents — reasonable constraints |
| strict | Security, compliance, payment agents |
| permissive | Creative, research, exploration agents |
## Body Requirements
- Identity: 2-4 sentences, must name domain expertise
- Rules: 7-12 numbered items, ALWAYS/NEVER pattern mandatory
- Output Format: must specify format type and sections
- Constraints: must include knowledge boundary and exclusions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_agent]] | sibling | 0.35 |
| [[bld_knowledge_card_system_prompt]] | upstream | 0.33 |
| [[bld_schema_system_prompt]] | upstream | 0.32 |
| [[bld_config_prompt_version]] | sibling | 0.31 |
| [[bld_config_agent_package]] | sibling | 0.28 |
| [[bld_config_kind]] | sibling | 0.28 |
| [[bld_config_constraint_spec]] | sibling | 0.28 |
| [[bld_config_mental_model]] | sibling | 0.28 |
| [[bld_collaboration_system_prompt]] | upstream | 0.28 |
| [[bld_config_memory_scope]] | sibling | 0.27 |
