---
kind: output_template
id: bld_output_template_router
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a router artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Router"
version: "1.0.0"
author: n03_builder
tags: [router, builder, examples]
tldr: "Golden and anti-examples for router construction, demonstrating ideal structure and common pitfalls."
domain: "router construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_router
  - bld_examples_router
  - bld_schema_router
  - p03_sp_router_builder
  - p03_ins_router
  - router-builder
  - bld_config_router
  - bld_architecture_router
  - p11_qg_router
  - bld_memory_router
---

# Output Template: router
```yaml
id: p02_router_{{router_slug}}
kind: router
pillar: P02

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

routes_count: {{integer_matching_table}}
fallback_route: "{{default_destination}}"
confidence_threshold: {{0.0_to_1.0}}
domain: "{{routing_domain}}"

quality: null
tags: [router, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
timeout_ms: {{integer_ms}}

retry_count: {{integer}}
load_balance: "{{round_robin|weighted|priority|none}}"
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
density_score: {{0.80_to_1.00}}
```
## Routes
| Pattern | Destination | Priority | Confidence Min | Conditions |
|---------|-------------|----------|----------------|------------|
| `{{pattern_1}}` | {{destination_1}} | {{1-100}} | {{0.0-1.0}} | `{{conditions_or_dash}}` |
| `{{pattern_2}}` | {{destination_2}} | {{1-100}} | {{0.0-1.0}} | `{{conditions_or_dash}}` |
## Decision Logic
Algorithm: {{priority_first|confidence_weighted|load_balanced}}
Tie-breaking: {{highest_priority|most_specific_pattern|round_robin}}
Evaluation order: {{sequential_top_down|parallel_all_then_rank}}
## Fallback
Default destination: `{{fallback_route}}`
Trigger: no route matches above confidence_threshold
Behavior: {{route_to_fallback|queue_for_review|escalate}}
## Escalation
Trigger: `{{ambiguous_match_description}}`
Action: `{{escalation_action}}`
Notification: `{{signal_type_or_none}}`
## Integration
1. Receives from: `{{upstream_source}}`
2. Routes to: `{{downstream_destinations}}`
3. Consults: `{{dispatch_rules_or_model_cards}}`
4. Signal on failure: `{{signal_type}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | router construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_router]] | upstream | 0.49 |
| [[bld_examples_router]] | downstream | 0.46 |
| [[bld_schema_router]] | downstream | 0.42 |
| [[p03_sp_router_builder]] | upstream | 0.42 |
| [[p03_ins_router]] | upstream | 0.39 |
| [[router-builder]] | upstream | 0.36 |
| [[bld_config_router]] | downstream | 0.35 |
| [[bld_architecture_router]] | downstream | 0.34 |
| [[p11_qg_router]] | downstream | 0.34 |
| [[bld_memory_router]] | downstream | 0.30 |
