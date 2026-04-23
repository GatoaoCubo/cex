---
kind: schema
id: bld_schema_compression_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for compression_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Compression Config"
version: "1.0.0"
author: n03_builder
tags: [compression_config, builder, examples]
tldr: "Golden and anti-examples for compression config construction, demonstrating ideal structure and common pitfalls."
domain: "compression config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_memory_scope
  - bld_schema_golden_test
  - bld_schema_output_validator
  - bld_schema_search_strategy
  - bld_schema_handoff_protocol
  - bld_schema_action_prompt
  - bld_schema_unit_eval
  - bld_schema_usage_report
  - bld_schema_reranker_config
---

# Schema: compression_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_cc_{name}) | YES | - | Namespace compliance |
| kind | literal "compression_config" | YES | - | Type integrity |
| pillar | literal "P10" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| strategy | enum: summarize, truncate_oldest, rolling_window, priority_keep, tiered | YES | - | Primary compression approach |
| trigger_ratio | float 0.50-0.99 | YES | - | Context fullness threshold to activate |
| preserve_types | list[string], len >= 1 | YES | - | Message types never compressed |
| max_summary_tokens | integer > 0 | YES | - | Token ceiling for summarized output |
| min_context_tokens | integer > 0 | YES | - | Floor — never compress below this |
| decay_weights | map[string, float] | YES | - | Priority multipliers per message type |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "compression_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| target_ratio | float 0.30-0.80 | REC | - | Desired utilization after compression |
| description | string <= 200ch | REC | - | What this config covers |
| scope | string | REC | - | Agent or system scope this applies to |
| tier_count | integer | REC | - | Number of compression tiers (if tiered) |
## ID Pattern
Regex: `^p10_cc_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Strategy Specification` — primary strategy, trigger ratio, target ratio, rationale
2. `## Preserve Types` — list of protected message types with justification
3. `## Decay Weights` — table: message type, base priority, age decay curve
4. `## Compression Pipeline` — ordered stages from least to most lossy
## Constraints
- max_bytes: 4096 (body only)
- naming: p10_cc_{name}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- preserve_types MUST include "system_prompt"
- trigger_ratio MUST be >= 0.50
- quality: null always
- NEVER compress system prompts or tool definitions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.65 |
| [[bld_schema_memory_scope]] | sibling | 0.64 |
| [[bld_schema_golden_test]] | sibling | 0.64 |
| [[bld_schema_output_validator]] | sibling | 0.64 |
| [[bld_schema_search_strategy]] | sibling | 0.63 |
| [[bld_schema_handoff_protocol]] | sibling | 0.63 |
| [[bld_schema_action_prompt]] | sibling | 0.63 |
| [[bld_schema_unit_eval]] | sibling | 0.62 |
| [[bld_schema_usage_report]] | sibling | 0.62 |
| [[bld_schema_reranker_config]] | sibling | 0.62 |
