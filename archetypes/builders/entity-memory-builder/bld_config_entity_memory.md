---
kind: config
id: bld_config_entity_memory
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
title: "Config Entity Memory"
version: "1.0.0"
author: n03_builder
tags: [entity_memory, builder, examples]
tldr: "Golden and anti-examples for entity memory construction, demonstrating ideal structure and common pitfalls."
domain: "entity memory construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_entity_memory_builder
  - bld_config_memory_scope
  - bld_instruction_entity_memory
  - bld_schema_entity_memory
  - bld_knowledge_card_entity_memory
  - bld_config_prompt_version
  - bld_config_retriever_config
  - bld_output_template_entity_memory
  - entity-memory-builder
  - p10_lr_entity_memory_builder
---
# Config: entity_memory Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_entity_{scope}.md` | `p10_entity_claude_sonnet.md` |
| Builder directory | kebab-case | `entity-memory-builder/` |
| Frontmatter fields | snake_case | `entity_type`, `update_policy`, `last_referenced` |
| Entity slug | snake_case, lowercase, no hyphens | `claude_sonnet`, `firecrawl_api`, `stripe_payment` |
| Attribute keys | snake_case, lowercase | `release_date`, `api_endpoint`, `primary_language` |
| Relation types | verb_noun or noun | `uses`, `owns`, `depends_on`, `created_by`, `part_of` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P10_memory/examples/p10_entity_{scope}.md`
- Compiled: `cex/P10_memory/compiled/p10_entity_{scope}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4000 bytes
- Density: >= 0.80 (no filler)
## Entity Type Enum
| Value | When to use |
|-------|-------------|
| person | Human — author, user, collaborator, contact |
| tool | Software tool, CLI, library, framework |
| concept | Abstract idea, pattern, methodology, principle |
| organization | Company, team, institution, community |
| project | Codebase, initiative, product, deliverable |
| service | API, SaaS, infrastructure service, platform |
## Update Policy Conventions
| Policy | Meaning | When to use |
|--------|---------|-------------|
| append | New facts added, old facts never overwritten | Logs, history, timeline |
| overwrite | Latest value replaces previous unconditionally | Volatile config, status |
| merge | New keys added, existing keys updated only if confidence improves | General facts |
| versioned | Every update creates a new version entry | Critical decisions, contracts |
Rule: every entity_memory MUST declare update_policy.
## Confidence Scale
| Range | Meaning |
|-------|---------|
| 0.9-1.0 | Verified — confirmed from primary source |
| 0.7-0.89 | Reliable — from trusted secondary source |
| 0.5-0.69 | Probable — inferred with supporting evidence |
| 0.0-0.49 | Uncertain — single mention, unverified |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_entity_memory_builder]] | downstream | 0.37 |
| [[bld_config_memory_scope]] | sibling | 0.34 |
| [[bld_instruction_entity_memory]] | upstream | 0.32 |
| [[bld_schema_entity_memory]] | downstream | 0.32 |
| [[bld_knowledge_card_entity_memory]] | upstream | 0.31 |
| [[bld_config_prompt_version]] | sibling | 0.30 |
| [[bld_config_retriever_config]] | sibling | 0.30 |
| [[bld_output_template_entity_memory]] | upstream | 0.29 |
| [[entity-memory-builder]] | downstream | 0.29 |
| [[p10_lr_entity_memory_builder]] | downstream | 0.29 |
