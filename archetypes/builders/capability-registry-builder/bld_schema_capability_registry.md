---
kind: schema
id: bld_schema_capability_registry
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for capability_registry
quality: 9.1
title: "Schema Capability Registry"
version: "1.0.0"
author: n04_wave8
tags: [capability_registry, builder, schema, agent-discovery]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for capability_registry"
domain: "capability_registry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_agent_profile
  - bld_schema_sandbox_config
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_faq_entry
  - bld_schema_api_reference
---

## Frontmatter Fields

### Required
| Field              | Type    | Required | Default  | Notes |
|--------------------|---------|----------|----------|-------|
| id                 | string  | yes      |          | Matches ID pattern below |
| kind               | string  | yes      |          | Must be "capability_registry" |
| pillar             | string  | yes      |          | P08 |
| title              | string  | yes      |          | Registry display name |
| version            | string  | yes      |          | Semver |
| created            | date    | yes      |          | ISO 8601 |
| updated            | date    | yes      |          | ISO 8601 |
| author             | string  | yes      |          | Nucleus or agent |
| domain             | string  | yes      |          | Registry scope description |
| quality            | null    | yes      | null     | Never self-score |
| tags               | array   | yes      |          | Includes kind + domain keywords |
| tldr               | string  | yes      |          | One-line summary |
| registry_scope     | string  | yes      |          | "builder_sub_agents" OR "nucleus_domain_agents" OR "nucleus_cards" OR "full" |
| entry_count        | integer | yes      |          | Total entries in this registry |
| index_date         | date    | yes      |          | When agents were last indexed |

### Recommended
| Field              | Type    | Notes |
|--------------------|---------|-------|
| query_interface    | string  | How to query this registry (CLI command or API call) |
| coverage_gaps      | array   | Domains with no registered agent |

## ID Pattern
`^p08_cr_[a-z][a-z0-9_]+\.md$`

## Body Structure

### 1. Registry Overview
- Scope, entry count, coverage domains.

### 2. Entry Schema (per agent)
Each entry MUST have these fields:
| Field             | Type    | Description |
|-------------------|---------|-------------|
| capability_name   | string  | Canonical name of the capability |
| provider_agent    | string  | Path to agent definition file |
| input_schema      | string  | Accepted input kind(s) or format |
| output_schema     | string  | Produced output kind(s) or format |
| cost_tokens       | string  | low / medium / high / very-high |
| quality_baseline  | float\|string | Numeric (0.0-10.0) or "unscored" |
| availability      | string  | active / deprecated / experimental |
| keyword_index     | string  | Comma-separated discovery terms |
| ranked_for        | array   | Query categories this agent ranks for |

### 3. Builder Sub-Agent Index
Table of all `.claude/agents/*-builder.md` entries.

### 4. Nucleus Domain Agent Index
Table of all `N0x_*/agents/agent_*.md` entries.

### 5. Nucleus Card Index
Table of all `N0x_*/agent_card_n0x.md` entries.

### 6. Query Examples
Worked examples: input query -> ranked candidates output.

### 7. Coverage Gaps
Domains where no registered agent has capability.

## Constraints
- `registry_scope` must be one of: builder_sub_agents, nucleus_domain_agents, nucleus_cards, full.
- `entry_count` must match actual entries in body.
- `availability` must be one of: active, deprecated, experimental.
- `quality_baseline` must be numeric 0.0-10.0 or literal string "unscored".
- All `provider_agent` paths must resolve (no phantom references).
- `keyword_index` must contain at least 3 terms per entry.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.61 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.59 |
| [[bld_schema_dataset_card]] | sibling | 0.59 |
| [[bld_schema_pitch_deck]] | sibling | 0.59 |
| [[bld_schema_agent_profile]] | sibling | 0.59 |
| [[bld_schema_sandbox_config]] | sibling | 0.59 |
| [[bld_schema_reranker_config]] | sibling | 0.58 |
| [[bld_schema_benchmark_suite]] | sibling | 0.58 |
| [[bld_schema_faq_entry]] | sibling | 0.58 |
| [[bld_schema_api_reference]] | sibling | 0.58 |
