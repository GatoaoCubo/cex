---
kind: schema
id: bld_schema_decision_record
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for decision_record
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Decision Record"
version: "1.0.0"
author: n03_builder
tags: [decision_record, builder, examples]
tldr: "Golden and anti-examples for decision record construction, demonstrating ideal structure and common pitfalls."
domain: "decision record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_action_prompt
  - bld_schema_memory_scope
  - bld_schema_golden_test
  - bld_schema_dataset_card
---

# Schema: decision_record
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p08_adr_{slug}) | YES | - | Namespace compliance |
| kind | literal "decision_record" | YES | - | Type integrity |
| pillar | literal "P08" | YES | - | Pillar assignment |
| title | string <= 80ch | YES | - | Human-readable decision title |
| status | enum: proposed, accepted, deprecated, superseded | YES | proposed | Lifecycle state |
| context | string | YES | - | Why this decision arose |
| decision | string | YES | - | What was decided |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "decision_record" |
| tldr | string <= 160ch | YES | - | Dense summary of decision |
| consequences | string | REC | - | Tradeoffs and effects of the decision |
| options | list[string], len >= 2 | REC | - | Alternatives that were considered |
| supersedes | string (id) | OPT | null | ID of ADR this replaces |
| superseded_by | string (id) | OPT | null | ID of ADR that replaces this |
| related_to | list[string] | OPT | - | IDs of related ADRs |
| deciders | list[string] | OPT | - | Who was involved in the decision |
| date_decided | date YYYY-MM-DD | OPT | - | When decision was finalized |
## ID Pattern
Regex: `^p08_adr_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Context` — problem, forces, and circumstances that made this decision necessary
2. `## Options Considered` — each alternative with pros and cons
3. `## Decision` — what was chosen and the primary rationale
4. `## Consequences` — positive, negative, and neutral effects; known tradeoffs
## Constraints
- max_bytes: 4096 (body — ADRs need full context to be useful)
- naming: p08_adr_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- status MUST be one of: proposed, accepted, deprecated, superseded
- context and decision MUST be present and non-empty
- quality: null always
- NO implementation code in body — rationale and record only
- If status == superseded: superseded_by MUST reference a valid ADR id

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.60 |
| [[bld_schema_handoff_protocol]] | sibling | 0.60 |
| [[bld_schema_output_validator]] | sibling | 0.59 |
| [[bld_schema_usage_report]] | sibling | 0.59 |
| [[bld_schema_benchmark_suite]] | sibling | 0.59 |
| [[bld_schema_reranker_config]] | sibling | 0.59 |
| [[bld_schema_action_prompt]] | sibling | 0.59 |
| [[bld_schema_memory_scope]] | sibling | 0.59 |
| [[bld_schema_golden_test]] | sibling | 0.59 |
| [[bld_schema_dataset_card]] | sibling | 0.58 |
