---
kind: schema
id: bld_schema_runtime_rule
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for runtime_rule
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Runtime Rule"
version: "1.0.0"
author: n03_builder
tags: [runtime_rule, builder, examples]
tldr: "Golden and anti-examples for runtime rule construction, demonstrating ideal structure and common pitfalls."
domain: "runtime rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_output_validator
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_constraint_spec
  - bld_schema_chunk_strategy
  - bld_schema_action_prompt
  - bld_schema_effort_profile
  - bld_schema_golden_test
  - bld_schema_smoke_eval
---

# Schema: runtime_rule
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_rr_{rule_slug}) | YES | - | Namespace compliance |
| kind | literal "runtime_rule" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| rule_name | string | YES | - | Human-readable rule name |
| rule_type | enum: timeout, retry, rate_limit, circuit_breaker, concurrency | YES | - | Primary rule category |
| scope | string | YES | - | What component/operation this applies to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "runtime_rule" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this rule governs |
| fallback | string | REC | - | Behavior when rule triggers |
| severity | enum: critical, high, medium, low | REC | medium | Impact if rule is misconfigured |
## ID Pattern
Regex: `^p09_rr_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Rule Specification` — concrete parameters: values with units, thresholds, limits
2. `## Trigger Behavior` — what happens when rule activates (timeout reached, retries exhausted, rate exceeded)
3. `## Tuning Guide` — how to adjust parameters, safe ranges, what metrics to watch
## Constraints
- max_bytes: 3072 (body only)
- naming: p09_rr_{rule_slug}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- All numeric values MUST include units (ms, s, min, req/s, etc.)
- quality: null always
- NEVER use vague terms ("fast", "many") — always concrete numbers

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_output_validator]] | sibling | 0.64 |
| [[bld_schema_retriever_config]] | sibling | 0.64 |
| [[bld_schema_handoff_protocol]] | sibling | 0.63 |
| [[bld_schema_memory_scope]] | sibling | 0.62 |
| [[bld_schema_constraint_spec]] | sibling | 0.62 |
| [[bld_schema_chunk_strategy]] | sibling | 0.61 |
| [[bld_schema_action_prompt]] | sibling | 0.61 |
| [[bld_schema_effort_profile]] | sibling | 0.61 |
| [[bld_schema_golden_test]] | sibling | 0.61 |
| [[bld_schema_smoke_eval]] | sibling | 0.61 |
