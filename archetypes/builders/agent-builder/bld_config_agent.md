---
kind: config
id: bld_config_agent
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: high
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: pillar
quality: 9.0
title: "Config Agent"
version: "1.0.0"
author: n03_builder
tags: [agent, builder, examples]
tldr: "Golden and anti-examples for agent construction, demonstrating ideal structure and common pitfalls."
domain: "agent construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_system_prompt
  - p03_sp_agent_builder
  - bld_config_agent_package
  - agent-builder
  - bld_schema_agent
  - bld_config_kind
  - bld_instruction_agent
  - bld_collaboration_agent_card
  - bld_collaboration_agent
  - bld_config_memory_scope
---
# Config: agent Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_agent_{slug}.md` + `.yaml` | `p02_agent_knowledge_card_builder.md` |
| Builder directory | kebab-case | `agent-builder/` |
| Frontmatter fields | snake_case | `agent_group`, `capabilities_count` |
| Agent slug | snake_case, lowercase | `knowledge_card_builder`, `scout_agent` |
| builder specs | `SPEC_{AGENT_UPPER}_{NNN}_{TYPE}.md` | `ISO_SCOUT_AGENT_004_INSTRUCTIONS.md` |
| Agent upper | SCREAMING_SNAKE_CASE | `KNOWLEDGE_CARD_BUILDER` |
Rule: id MUST equal filename stem.
Rule: builder spec NNN starts at 001 and increments without gaps.
## File Paths
- Output (canonical): `cex/P02_model/examples/p02_agent_{slug}.md`
- Compiled: `cex/P02_model/compiled/p02_agent_{slug}.yaml`
- agent package: `agents/{slug}/agent_package/SPEC_{UPPER}_{NNN}_{TYPE}.md`
## Size Limits (aligned with SCHEMA)
- Body: max 5120 bytes
- Total (frontmatter + body): ~6500 bytes
- Density: >= 0.80
- Per builder spec: max 4096 bytes
## Agent_group Enum
| Value | When to use |
|-------|-------------|
| orchestrator | Orchestration agents |
| researcher | Research and scraping agents |
| marketer | Marketing and copy agents |
| builder | Build and code agents |
| knowledge-engine | Knowledge and documentation agents |
| executor | Execution, deploy, and infra agents |
| monetizer | Monetization and product agents |
| agnostic | Cross-agent_group utility agents |
## Spec File Type Enum
| NNN | TYPE | Pillar |
|-----|------|--------|
| 001 | MANIFEST | P02 |
| 002 | QUICK_START | P01 |
| 003 | PRIME | P03 |
| 004 | INSTRUCTIONS | P03 |
| 005 | ARCHITECTURE | P08 |
| 006 | OUTPUT_TEMPLATE | P05 |
| 007 | EXAMPLES | P07 |
| 008 | ERROR_HANDLING | P11 |
| 009 | UPLOAD_KIT | P04 |
| 010 | SYSTEM_INSTRUCTION | P03 |
## Body Requirements
- Overview: 2-3 sentences, must name agent_group and domain
- Architecture: capabilities (4-8 bullets) + tools table + agent_group position
- File Structure: full agent_package listing with correct spec naming
- When to Use: triggers + keywords + NOT when exclusions (mandatory)
- Common Issues: 3-5 failure modes, each with one-line remediation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_system_prompt]] | sibling | 0.37 |
| [[p03_sp_agent_builder]] | upstream | 0.36 |
| [[bld_config_agent_package]] | sibling | 0.35 |
| [[agent-builder]] | upstream | 0.34 |
| [[bld_schema_agent]] | upstream | 0.32 |
| [[bld_config_kind]] | sibling | 0.32 |
| [[bld_instruction_agent]] | upstream | 0.32 |
| [[bld_collaboration_agent_card]] | upstream | 0.31 |
| [[bld_collaboration_agent]] | downstream | 0.31 |
| [[bld_config_memory_scope]] | sibling | 0.30 |
