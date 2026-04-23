---
kind: schema
id: bld_schema_router
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for router
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Router"
version: "1.0.0"
author: n03_builder
tags: [router, builder, examples]
tldr: "Golden and anti-examples for router construction, demonstrating ideal structure and common pitfalls."
domain: "router construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_action_prompt
  - bld_schema_reranker_config
  - bld_schema_input_schema
  - bld_schema_smoke_eval
  - bld_schema_handoff_protocol
  - bld_schema_usage_report
  - bld_schema_golden_test
  - bld_schema_workflow
---

# Schema: router
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_router_{slug}) | YES | - | Namespace compliance |
| kind | literal "router" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| routes_count | integer | YES | - | Must match route table rows |
| fallback_route | string | YES | - | Destination when no pattern matches |
| confidence_threshold | float 0.0-1.0 | YES | 0.7 | Minimum confidence for route match |
| domain | string | YES | - | Domain this router serves |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "router" |
| tldr | string <= 160ch | YES | - | Dense summary |
| timeout_ms | integer | REC | 5000 | Max decision time in milliseconds |
| retry_count | integer | REC | 1 | Retries on routing failure |
| load_balance | enum [round_robin, weighted, priority, none] | REC | "priority" | Route selection strategy |
| keywords | list[string] | REC | - | Brain search triggers |
| density_score | float 0.80-1.00 | OPT | - | Content density |
## Route Object
```yaml
route:
  pattern: string (regex or keyword list)
  destination: string (agent_group name or agent id)
  priority: integer 1-100 (higher = preferred)
  confidence_min: float 0.0-1.0
  conditions: list[string] (optional extra conditions)
```
## ID Pattern
Regex: `^p02_router_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Routes` — route table: pattern, destination, priority, confidence_min
2. `## Decision Logic` — algorithm for route selection
3. `## Fallback` — default behavior when no route matches
4. `## Escalation` — handling ambiguous matches or low confidence
5. `## Integration` — connection to dispatch_rule, agent, workflow
6. `## References` — sources and documentation
## Constraints
- max_bytes: 4096 (body only)
- naming: p02_router_{slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- quality: null always
- routes_count MUST match actual rows in Routes table
- confidence_threshold between 0.0 and 1.0
- fallback_route MUST be a valid agent_group name or "escalate"
- Each route pattern MUST be unique (no duplicate patterns)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.59 |
| [[bld_schema_output_validator]] | sibling | 0.58 |
| [[bld_schema_action_prompt]] | sibling | 0.58 |
| [[bld_schema_reranker_config]] | sibling | 0.58 |
| [[bld_schema_input_schema]] | sibling | 0.58 |
| [[bld_schema_smoke_eval]] | sibling | 0.58 |
| [[bld_schema_handoff_protocol]] | sibling | 0.58 |
| [[bld_schema_usage_report]] | sibling | 0.58 |
| [[bld_schema_golden_test]] | sibling | 0.58 |
| [[bld_schema_workflow]] | sibling | 0.58 |
