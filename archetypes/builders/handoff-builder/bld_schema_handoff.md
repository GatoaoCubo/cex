---
kind: schema
id: bld_schema_handoff
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for handoff - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
quality: 9.1
title: "Schema Handoff"
version: "1.0.1"
author: n03_builder
tags: [handoff, builder, examples]
tldr: "Golden and anti-examples for handoff construction, demonstrating ideal structure and common pitfalls."
domain: "handoff construction"
created: "2026-04-07"
updated: "2026-04-18"
last_reviewed: "2026-04-18"
density_score: 0.90
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_action_prompt
  - bld_schema_sandbox_config
  - bld_schema_action_paradigm
  - bld_schema_integration_guide
---

# Schema: handoff
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P12` |
| Type | literal `handoff` |
| Machine format | `yaml` (frontmatter) + `md` (body) |
| Naming | `p12_ho_{task}.md` |
| Max bytes | 4096 |
## Required Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (`p12_ho_{slug}`) | YES | - | Unique handoff identifier |
| kind | literal "handoff" | YES | - | Type integrity |
| lp | literal "P12" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| agent_group | string | YES | - | Target executor (lowercase slug) |
| mission | string | YES | - | Mission or project name |
| autonomy | enum (`full`, `supervised`, `assisted`) | YES | - | Execution autonomy level |
| quality_target | number 0.0-10.0 | YES | - | Minimum quality threshold |
| domain | string | YES | - | Domain this artifact belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Searchability |
| tldr | string <= 160ch | YES | - | Dense summary |
## Optional Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| dependencies | list[string] | NO | omitted | Handoffs or artifacts that must complete first |
| seeds | list[string] | NO | omitted | Seed words for context hydration |
| agent | string | NO | omitted | Specific agent to load before execution |
| skill | string | NO | omitted | Specific skill to follow during execution |
| batch | string | NO | omitted | Batch identifier for continuous batching |
| wave | integer | NO | omitted | Wave number in multi-wave execution |
| keywords | list[string] | NO | omitted | Brain search terms |
| linked_artifacts | object {primary, related} | NO | omitted | Cross-references |
| max_revisions | int | NO | 3 | Max iterations before escalation |
| escalation_target | enum (user, senior_nucleus, freeze) | NO | user | Where to escalate on max_revisions |
| revision_priority_order | list | NO | [security, quality, implementation] | Tiebreaker order for revision focus |
## Body Structure (required sections)
1. `## Context` — why this work is needed and relevant background
2. `## Tasks` — numbered list of specific actions to perform
3. `## Scope Fence` — paths allowed (SOMENTE) and forbidden (NAO TOQUE)
4. `## Commit` — exact git commands for committing deliverables
5. `## Signal` — how to signal completion (signal_writer or file)
## Semantic Rules
1. One handoff delegates one coherent unit of work to one agent_group
2. Tasks must be specific and actionable, not vague
3. Scope fence must explicitly list allowed and forbidden paths
4. Commit section must include exact git add and commit commands
5. Signal section must reference signal_writer or a completion file
6. Autonomy level governs how much the agent_group can decide independently
## Boundary Rules
`handoff` IS:
- complete delegation instruction for a agent_group
- packaged context + tasks + scope + commit rules
- one-shot execution brief
`handoff` IS NOT:
- `action_prompt`: no persona, no system rules, no response format constraints
- `signal`: no status event, no quality score, no timestamp-only data
- `dispatch_rule`: no keyword routing table, no agent_group selection policy
- `workflow`: no step graph, no error handling, no runtime state
- `dag`: no dependency graph structure, no topological ordering
- `crew`: no multi-agent coordination protocol
## ID Pattern
Regex: `^p12_ho_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Constraints
- max_bytes: 4096
- naming: `p12_ho_{task}.md`
- id == filename stem
- Must have all 5 body sections
- Scope fence must list both SOMENTE and NAO TOQUE

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.54 |
| [[bld_schema_usage_report]] | sibling | 0.54 |
| [[bld_schema_quickstart_guide]] | sibling | 0.53 |
| [[bld_schema_dataset_card]] | sibling | 0.53 |
| [[bld_schema_search_strategy]] | sibling | 0.53 |
| [[bld_schema_benchmark_suite]] | sibling | 0.53 |
| [[bld_schema_action_prompt]] | sibling | 0.53 |
| [[bld_schema_sandbox_config]] | sibling | 0.52 |
| [[bld_schema_action_paradigm]] | sibling | 0.52 |
| [[bld_schema_integration_guide]] | sibling | 0.52 |
