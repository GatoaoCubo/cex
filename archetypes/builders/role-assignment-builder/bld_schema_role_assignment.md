---
kind: schema
id: bld_schema_role_assignment
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for role_assignment
quality: 9.1
title: "Schema Role Assignment"
version: "1.0.0"
author: n03_wave8_builder
tags: [role_assignment, builder, schema, composable, crewai]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for role_assignment"
domain: "role_assignment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_schema_crew_template
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_multimodal_prompt
  - bld_schema_sandbox_config
  - bld_schema_integration_guide
---

## Frontmatter Fields
### Required
| Field            | Type   | Required | Default | Notes |
|------------------|--------|----------|---------|-------|
| id               | string | yes      |         | matches ID pattern |
| kind             | string | yes      |         | must equal 'role_assignment' |
| pillar           | string | yes      | P02     |       |
| title            | string | yes      |         |       |
| version          | string | yes      | 1.0.0   | semver |
| created          | date   | yes      |         | ISO 8601 |
| updated          | date   | yes      |         | ISO 8601 |
| author           | string | yes      |         |       |
| domain           | string | yes      |         |       |
| quality          | null   | yes      | null    | Never self-score |
| tags             | array  | yes      |         |       |
| tldr             | string | yes      |         |       |
| role_name        | string | yes      |         | snake_case, unique per crew |
| agent_id         | string | yes      |         | .claude/agents/ or N0x/agents ref |
| goal             | string | yes      |         | measurable outcome |
| backstory        | string | yes      |         | CrewAI-style persona hook |

### Recommended
| Field              | Type   | Notes |
|--------------------|--------|-------|
| responsibilities   | array  | 3-5 testable bullets |
| tools_allowed      | array  | subset of agent's native toolkit |
| delegation_policy  | object | can_delegate_to + conditions |
| crewai_equivalent  | string | CrewAI Agent class mapping |

## ID Pattern
^p02_ra_[a-z][a-z0-9_]+\.md$

## Body Structure
1. **Role Header** -- role_name + agent_id + one-line purpose.
2. **Responsibilities** -- 3-5 testable bullets (inputs, outputs, invariants).
3. **Tools Allowed** -- explicit subset of the agent's native toolkit (least-privilege).
4. **Delegation Policy** -- can_delegate_to list + conditions or null (non-delegating).
5. **Backstory** -- 2-3 sentence persona hook grounded in domain.
6. **Goal** -- single measurable outcome statement.
7. **Runtime Notes** -- how the role behaves inside sequential / hierarchical / consensus processes.

## Constraints
- All required frontmatter fields present and valid.
- `id` matches the regex pattern exactly.
- `agent_id` MUST resolve to an existing .claude/agents/*.md OR N0x/agents/* artifact.
- `role_name` MUST be snake_case and unique within its target crew_template.
- `tools_allowed` (if present) MUST be a subset of the agent's native toolkit.
- `delegation_policy.can_delegate_to` (if present) MUST reference role_names, never agent_ids.
- `backstory` <= 300 chars; `goal` <= 150 chars.
- File size <= 3072 bytes.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_crew_template]] | sibling | 0.67 |
| [[bld_schema_usage_report]] | sibling | 0.65 |
| [[bld_schema_reranker_config]] | sibling | 0.64 |
| [[bld_schema_quickstart_guide]] | sibling | 0.64 |
| [[bld_schema_pitch_deck]] | sibling | 0.63 |
| [[bld_schema_dataset_card]] | sibling | 0.63 |
| [[bld_schema_benchmark_suite]] | sibling | 0.63 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.63 |
| [[bld_schema_sandbox_config]] | sibling | 0.63 |
| [[bld_schema_integration_guide]] | sibling | 0.62 |
