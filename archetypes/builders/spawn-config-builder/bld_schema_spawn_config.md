---
kind: schema
id: bld_schema_spawn_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for spawn_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Spawn Config"
version: "1.0.0"
author: n03_builder
tags: [spawn_config, builder, examples]
tldr: "Golden and anti-examples for spawn config construction, demonstrating ideal structure and common pitfalls."
domain: "spawn config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_usage_report
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
  - bld_schema_reranker_config
  - bld_schema_output_validator
  - bld_schema_action_prompt
  - bld_schema_golden_test
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
  - bld_schema_memory_scope
---

# Schema: spawn_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p12_spawn_{mode_slug}) | YES | - | Namespace compliance |
| kind | literal "spawn_config" | YES | - | Type integrity |
| pillar | literal "P12" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable config name |
| mode | enum: solo, grid, continuous | YES | - | Spawn mode |
| agent_group | string or list[string] | YES | - | Target agent_group(s) |
| model | string | YES | - | LLM model (opus, sonnet, haiku) |
| flags | list[string] | YES | - | CLI flags for claude command |
| mcp_config | string | REC | - | Path to .mcp-{sat}.json |
| timeout | integer | YES | - | Timeout in seconds |
| interactive | boolean | REC | true | Whether terminal stays open |
| prompt_strategy | enum: inline, handoff | REC | "handoff" | How task is passed |
| domain | string | YES | - | Domain this config serves |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "spawn_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
## ID Pattern
Regex: `^p12_spawn_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Spawn Command` — the actual PowerShell/CLI command to execute
2. `## Parameters` — detailed parameter descriptions and rationale
3. `## Constraints` — limitations, requirements, and safety notes
## Constraints
- max_bytes: 3072 (body only)
- naming: p12_spawn_{mode_slug}.yaml
- machine_format: yaml
- id == filename stem
- mode MUST be one of: solo, grid, continuous
- flags SHOULD include runtime-required permission and safety flags
- prompt_strategy: use "handoff" when task description > 200 chars
- quality: null always

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.67 |
| [[bld_schema_retriever_config]] | sibling | 0.67 |
| [[bld_schema_handoff_protocol]] | sibling | 0.66 |
| [[bld_schema_reranker_config]] | sibling | 0.66 |
| [[bld_schema_output_validator]] | sibling | 0.65 |
| [[bld_schema_action_prompt]] | sibling | 0.65 |
| [[bld_schema_golden_test]] | sibling | 0.65 |
| [[bld_schema_search_strategy]] | sibling | 0.65 |
| [[bld_schema_quickstart_guide]] | sibling | 0.65 |
| [[bld_schema_memory_scope]] | sibling | 0.65 |
