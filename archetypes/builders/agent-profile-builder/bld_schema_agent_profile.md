---
kind: schema
id: bld_schema_agent_profile
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for agent_profile
quality: 9.1
title: "Schema Agent Profile"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_profile, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for agent_profile"
domain: "agent_profile construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_sandbox_config
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_pitch_deck
  - bld_schema_action_paradigm
  - bld_schema_rl_algorithm
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
---

## Frontmatter Fields
### Required
| Field      | Type   | Required | Default | Notes |
|------------|--------|----------|---------|-------|
| id         | string | yes      | -       | Unique identifier |
| kind       | string | yes      | "agent_profile" | CEX kind |
| pillar     | string | yes      | "P02"    | Pillar classification |
| title      | string | yes      | -       | Profile name |
| version    | string | yes      | "1.0.0" | Semantic versioning |
| created    | date   | yes      | -       | ISO 8601 format |
| updated    | date   | yes      | -       | ISO 8601 format |
| author     | string | yes      | -       | Creator identifier |
| domain     | string | yes      | -       | Operational domain |
| quality    | string | yes      | "draft" | Quality status |
| tags       | list   | yes      | []      | Keywords |
| tldr       | string | yes      | -       | Summary |
| agent_type | string | yes      | -       | Role classification |
| expertise  | list   | yes      | []      | Skill areas |
| status     | string | yes      | "active" | Profile status |

### Recommended
| Field         | Type   | Notes |
|---------------|--------|-------|
| description   | string | Detailed overview |
| contact_info  | string | Contact details |
| notes         | string | Additional context |

## ID Pattern
^p02_ap_[a-zA-Z0-9_]+\.md$

## Body Structure
1. **Overview**
   - Purpose, scope, and context of the agent profile.

2. **Attributes**
   - Key properties, including domain, agent_type, and expertise.

3. **Capabilities**
   - Functional abilities and limitations of the agent.

4. **Relationships**
   - Interactions with other agents, systems, or entities.

5. **Compliance**
   - Regulatory, ethical, or operational standards adhered to.

## Constraints
- All required fields must be present and valid.
- ID must conform to the regex pattern.
- Version must follow semantic versioning (e.g., "1.2.3").
- Tags must be comma-separated, lowercase, and non-empty.
- agent_type must be one of: "operator", "analyst", "automaton".
- Status must be one of: "active", "inactive", "pending".

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.71 |
| [[bld_schema_sandbox_config]] | sibling | 0.71 |
| [[bld_schema_dataset_card]] | sibling | 0.69 |
| [[bld_schema_reranker_config]] | sibling | 0.68 |
| [[bld_schema_benchmark_suite]] | sibling | 0.68 |
| [[bld_schema_pitch_deck]] | sibling | 0.67 |
| [[bld_schema_action_paradigm]] | sibling | 0.67 |
| [[bld_schema_rl_algorithm]] | sibling | 0.67 |
| [[bld_schema_search_strategy]] | sibling | 0.66 |
| [[bld_schema_quickstart_guide]] | sibling | 0.66 |
