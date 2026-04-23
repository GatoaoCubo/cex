---
kind: schema
id: bld_schema_crew_template
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for crew_template
quality: 9.1
title: "Schema Crew Template"
version: "1.0.0"
author: n03_wave8_builder
tags: [crew_template, builder, schema, composable, crewai]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for crew_template"
domain: "crew_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_sandbox_config
  - bld_schema_dataset_card
  - bld_schema_multimodal_prompt
  - bld_schema_search_strategy
  - bld_schema_integration_guide
---

## Frontmatter Fields
### Required
| Field     | Type   | Required | Default | Notes |
|-----------|--------|----------|---------|-------|
| id        | string | yes      |         | matches ID pattern |
| kind      | string | yes      |         | must equal 'crew_template' |
| pillar    | string | yes      | P12     |       |
| title     | string | yes      |         |       |
| version   | string | yes      | 1.0.0   | semver |
| created   | date   | yes      |         | ISO 8601 |
| updated   | date   | yes      |         | ISO 8601 |
| author    | string | yes      |         |       |
| domain    | string | yes      |         |       |
| quality   | null   | yes      | null    | Never self-score; peer review assigns |
| tags      | array  | yes      |         |       |
| tldr      | string | yes      |         |       |
| crew_name | string | yes      |         | canonical crew identifier |
| purpose   | string | yes      |         | task boundary |
| process   | string | yes      |         | sequential \| hierarchical \| consensus |

### Recommended
| Field               | Type   | Notes |
|---------------------|--------|-------|
| crewai_equivalent   | string | CrewAI Process name for portability |
| autogen_equivalent  | string | AutoGen GroupChat pattern |
| swarm_equivalent    | string | OpenAI Swarm agent graph |
| handoff_protocol_id | string | reference to handoff_protocol artifact |

## ID Pattern
^p12_ct_[a-z][a-z0-9_]+\.md$

## Body Structure
1. **Overview** -- crew purpose, instantiation contexts.
2. **Roles** -- list of role_assignment references with short reason.
3. **Process** -- topology (sequential | hierarchical | consensus) with rationale.
4. **Memory Scope** -- per-role scope declaration (private | shared | persistent).
5. **Handoff Protocol** -- inter-role transfer format (A2A Task | OpenAI transfer | native).
6. **Success Criteria** -- measurable post-conditions for crew completion.
7. **Instantiation** -- example of spawning the crew at runtime.

## Constraints
- All required frontmatter fields present and valid.
- `id` matches the regex pattern exactly.
- `process` must be one of: sequential, hierarchical, consensus.
- Every role listed MUST reference an existing role_assignment artifact (p02_ra_*.md).
- File size must be <= 4096 bytes.
- `success_criteria` MUST be measurable (threshold, count, or gate ID).
- `memory_scope` MUST be declared for each role.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.68 |
| [[bld_schema_quickstart_guide]] | sibling | 0.66 |
| [[bld_schema_pitch_deck]] | sibling | 0.66 |
| [[bld_schema_benchmark_suite]] | sibling | 0.66 |
| [[bld_schema_reranker_config]] | sibling | 0.66 |
| [[bld_schema_sandbox_config]] | sibling | 0.66 |
| [[bld_schema_dataset_card]] | sibling | 0.65 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.64 |
| [[bld_schema_search_strategy]] | sibling | 0.63 |
| [[bld_schema_integration_guide]] | sibling | 0.63 |
