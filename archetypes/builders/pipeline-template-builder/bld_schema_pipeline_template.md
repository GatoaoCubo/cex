---
kind: schema
id: bld_schema_pipeline_template
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for pipeline_template
quality: 8.9
title: "Schema Pipeline Template"
version: "1.0.0"
author: n03_hermes_w1_5
tags: [pipeline_template, builder, schema, hermes, scenario_indexed]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for pipeline_template"
domain: "pipeline_template construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.87
related:
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_sandbox_config
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_sandbox_spec
  - bld_schema_playground_config
---

## Frontmatter Fields
### Required
| Field         | Type   | Required | Default | Notes |
|---------------|--------|----------|---------|-------|
| id            | string | yes      |         | matches ID pattern |
| kind          | string | yes      |         | must equal 'pipeline_template' |
| pillar        | string | yes      | P12     |       |
| title         | string | yes      |         |       |
| scenario      | enum   | yes      |         | one of 7 canonical values |
| stages        | array  | yes      |         | ordered stage objects |
| revision_loop | object | yes      |         | max_iterations + escalation_target |
| quality_gates | object | yes      |         | mandatory + priority_order |
| version       | string | yes      | 1.0.0   | semver |
| quality       | null   | yes      | null    | Never self-score; peer review assigns |
| tags          | array  | yes      |         |       |

### Stage Object Fields
| Field      | Type    | Required | Notes |
|------------|---------|----------|-------|
| role       | string  | yes      | canonical role name (see roles enum) |
| model_tier | enum    | yes      | low \| medium \| high \| xhigh |
| optional   | boolean | yes      | false = mandatory stage |

### Enums
scenario: new_feature | new_feature_security | bug_fix_unknown | bug_fix_known | refactoring | perf_opt | infra
model_tier: low | medium | high | xhigh
roles: finder | analyst | architect | planner | coder | refactorer | optimizer | debugger | fixer | devops | documenter | reviewer | tester | researcher | security
escalation_target: user | nucleus | n07

## ID Pattern
^p12_pt_[a-z][a-z0-9_]+$

## Body Structure
1. **Scenario** -- which engineering scenario this pipeline covers and when to use it.
2. **Stage Sequence** -- table of roles in execution order with model_tier and optional flag.
3. **Revision Loop** -- max retries, trigger condition, escalation path.
4. **Quality Gates** -- mandatory gate roles, priority order, gate-failure behavior.
5. **Instantiation** -- example of running this pipeline for a specific task.

## Constraints
- All required frontmatter fields present and valid.
- `id` matches the regex pattern exactly.
- `scenario` must be one of the 7 canonical enum values.
- `stages` must have at least 2 entries.
- `quality_gates.mandatory` MUST include `reviewer` and `tester`.
- `revision_loop.max_iterations` must be between 1 and 5.
- File size must be <= 4096 bytes.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_quickstart_guide]] | sibling | 0.58 |
| [[bld_schema_usage_report]] | sibling | 0.57 |
| [[bld_schema_reranker_config]] | sibling | 0.57 |
| [[bld_schema_dataset_card]] | sibling | 0.56 |
| [[bld_schema_pitch_deck]] | sibling | 0.56 |
| [[bld_schema_sandbox_config]] | sibling | 0.54 |
| [[bld_schema_benchmark_suite]] | sibling | 0.54 |
| [[bld_schema_integration_guide]] | sibling | 0.54 |
| [[bld_schema_sandbox_spec]] | sibling | 0.54 |
| [[bld_schema_playground_config]] | sibling | 0.54 |
