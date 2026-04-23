---
kind: schema
id: bld_schema_skill
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for skill
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Skill"
version: "1.0.1"
author: n03_builder
tags: [skill, builder, examples]
tldr: "Golden and anti-examples for skill construction, demonstrating ideal structure and common pitfalls."
domain: "skill construction"
created: "2026-04-07"
updated: "2026-04-18"
last_reviewed: "2026-04-18"
density_score: 0.90
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_dataset_card
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
  - bld_schema_action_prompt
  - bld_schema_pitch_deck
  - bld_schema_retriever_config
---

# Schema: skill
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_skill_{name}) | YES | - | Namespace compliance |
| kind | literal "skill" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable skill name |
| description | string <= 120ch | YES | - | One-line capability summary |
| user_invocable | boolean | YES | false | True = slash command available |
| trigger | string | YES | - | Exact invocation pattern |
| phases | list[string] | YES | - | Ordered phase names |
| when_to_use | list[string] | YES | - | Conditions favoring this skill |
| when_not_to_use | list[string] | YES | - | Conditions excluding this skill |
| examples | list[string] | YES | - | 2+ concrete invocation examples |
| quality | null | YES | null | Never self-score |
| references_dir | string | NO | - | Path to related artifacts |
| sub_skills | list[string] | NO | - | Skill IDs this skill delegates to |
| platforms | list[string] | NO | - | OS/runtime constraints |
| stack_default | string | NO | - | Default stack/runtime |
| auto_generated_from | string (trace_hash) | NO | null | Trace that spawned this skill (HERMES autonomous creation) |
| self_improves | bool | NO | false | If true, engine may patch this skill on future reuse |
| agentskills_catalog_category | string | NO | null | agentskills.io category (e.g. `github`, `mlops`) |
| trigger_tool_call_count_min | int | NO | 5 | Min tool-call count to auto-spawn |
| improvement_count | int | NO | 0 | Times this skill has been patched |
## ID Pattern
Regex: `^p04_skill_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Purpose` — what capability this skill provides and why it exists
2. `## Workflow Phases` — one subsection per phase with input/output/action
3. `## Anti-Patterns` — named failures and how to avoid them
4. `## Metrics` — measurable success criteria for this skill
## Constraints
- max_bytes: 5120 (body only)
- naming: p04_skill_{name}.md + .yaml
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- phases list MUST match ## Workflow Phases subsections in body
- user_invocable: true REQUIRES trigger to be a slash command pattern (/name)
- quality: null always
- skill has NO identity/persona — capability only, no "You are" statements
- when_to_use and when_not_to_use MUST be parallel (same abstraction level)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.59 |
| [[bld_schema_usage_report]] | sibling | 0.59 |
| [[bld_schema_benchmark_suite]] | sibling | 0.59 |
| [[bld_schema_integration_guide]] | sibling | 0.58 |
| [[bld_schema_dataset_card]] | sibling | 0.58 |
| [[bld_schema_search_strategy]] | sibling | 0.58 |
| [[bld_schema_quickstart_guide]] | sibling | 0.57 |
| [[bld_schema_action_prompt]] | sibling | 0.57 |
| [[bld_schema_pitch_deck]] | sibling | 0.56 |
| [[bld_schema_retriever_config]] | sibling | 0.56 |
