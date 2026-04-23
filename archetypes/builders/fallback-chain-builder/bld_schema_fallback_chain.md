---
kind: schema
id: bld_schema_fallback_chain
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for fallback_chain
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Fallback Chain"
version: "1.0.0"
author: n03_builder
tags: [fallback_chain, builder, examples]
tldr: "Golden and anti-examples for fallback chain construction, demonstrating ideal structure and common pitfalls."
domain: "fallback chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_chain
  - bld_schema_workflow
  - bld_schema_action_prompt
  - bld_schema_smoke_eval
  - bld_schema_golden_test
  - bld_schema_unit_eval
  - bld_schema_embedding_config
  - bld_schema_boot_config
  - bld_schema_retriever_config
  - bld_schema_input_schema
---

# Schema: fallback_chain
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_fc_{slug}) | YES | - | Namespace compliance |
| kind | literal "fallback_chain" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| steps_count | integer >= 2 | YES | - | Must match chain steps in body |
| timeout_per_step_ms | integer | YES | 30000 | Max time per step before fallback |
| quality_threshold | float 0.0-10.0 | YES | 7.0 | Min quality before triggering fallback |
| domain | string | YES | - | Domain this chain serves |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "fallback_chain" |
| tldr | string <= 160ch | YES | - | Dense summary |
| retry_count | integer | REC | 1 | Retries per step before moving to next |
| circuit_breaker_threshold | integer | REC | 3 | Consecutive failures to trip breaker |
| cost_ceiling_usd | float | REC | - | Max total cost across all steps |
| logging_level | enum [none, errors, all] | REC | "errors" | What to log during chain execution |
| alert_on_final_fallback | boolean | REC | true | Alert when last step is reached |
| keywords | list[string] | REC | - | Brain search triggers |
| density_score | float 0.80-1.00 | OPT | - | Content density |
## Step Object
```yaml
step:
  position: integer (1-based, sequential)
  model: string (model identifier)
  provider: string (anthropic, openai, google, local)
  timeout_ms: integer (overrides global if set)
  quality_min: float 0.0-10.0
  cost_per_1m_tokens: float (USD)
  retry: integer (overrides global if set)
  conditions: list[string] (optional activation conditions)
```
## ID Pattern
Regex: `^p02_fc_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Chain` — ordered step table: position, model, provider, timeout, quality_min, cost
2. `## Degradation Logic` — how and when each step triggers the next
3. `## Circuit Breaker` — conditions that trip the breaker and halt the chain
4. `## Cost Analysis` — total cost projection across all steps
5. `## Integration` — connection to router, agent, model_card
6. `## References` — sources and documentation
## Constraints
- max_bytes: 4096 (body only)
- naming: p02_fc_{slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- quality: null always
- steps_count MUST match actual rows in Chain table
- steps_count >= 2 (single-step is not a chain)
- Steps must be ordered by decreasing capability/cost (graceful degradation)
- timeout_per_step_ms > 0
- quality_threshold between 0.0 and 10.0

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_chain]] | sibling | 0.65 |
| [[bld_schema_workflow]] | sibling | 0.60 |
| [[bld_schema_action_prompt]] | sibling | 0.57 |
| [[bld_schema_smoke_eval]] | sibling | 0.56 |
| [[bld_schema_golden_test]] | sibling | 0.56 |
| [[bld_schema_unit_eval]] | sibling | 0.55 |
| [[bld_schema_embedding_config]] | sibling | 0.55 |
| [[bld_schema_boot_config]] | sibling | 0.55 |
| [[bld_schema_retriever_config]] | sibling | 0.55 |
| [[bld_schema_input_schema]] | sibling | 0.55 |
