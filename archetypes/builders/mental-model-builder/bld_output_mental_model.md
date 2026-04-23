---
kind: output_template
id: bld_output_template_mental_model
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a mental_model artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Mental Model"
version: "1.0.0"
author: n03_builder
tags: [mental_model, builder, examples]
tldr: "Golden and anti-examples for mental model construction, demonstrating ideal structure and common pitfalls."
domain: "mental model construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_mental_model
  - bld_knowledge_card_mental_model
  - p03_sp_mental_model_builder
  - p11_qg_mental_model
  - mental-model-builder
  - bld_schema_mental_model
  - bld_examples_mental_model
  - bld_config_mental_model
  - bld_collaboration_mental_model
  - bld_architecture_mental_model
---

# Output Template: mental_model

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
```yaml
id: p02_mm_{{agent_slug}}
kind: mental_model
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
agent: "{{agent_name}}"
routing_rules:
  - keywords: [{{kw_1a}}, {{kw_1b}}, {{kw_1c}}]
    action: "{{action_1}}"
    confidence: {{0.0-1.0}}
  - keywords: [{{kw_2a}}, {{kw_2b}}]
    action: "{{action_2}}"
    confidence: {{0.0-1.0}}
  - keywords: [{{kw_3a}}, {{kw_3b}}]
    action: "{{action_3}}"
    confidence: {{0.0-1.0}}
decision_tree:
  - condition: "{{if_condition_1}}"
    then: "{{action_a}}"
    else: "{{action_b}}"
  - condition: "{{if_condition_2}}"
    then: "{{action_c}}"
priorities: [{{priority_1}}, {{priority_2}}, {{priority_3}}]
heuristics:
  - "{{heuristic_1}}"
  - "{{heuristic_2}}"
domain_map:
  covers: [{{domain_1}}, {{domain_2}}]
  routes_to: [{{routed_domain_1}}: {{target_agent}}]
tools_available: [{{tool_1}}, {{tool_2}}]
personality:
  tone: "{{tone_descriptor}}"
  verbosity: "{{concise|moderate|verbose}}"
  risk_tolerance: "{{low|medium|high}}"
constraints:
  - "{{constraint_1}}"
  - "{{constraint_2}}"
fallback:
  action: "{{fallback_action}}"
  escalate_to: "{{escalation_target}}"
domain: "{{primary_domain}}"
llm_function: BECOME
quality: null
tags: [mental-model, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Agent Reference
`{{agent_name}}`: `{{one_line_agent_identity}}`
## Routing Rules
| Keywords | Action | Confidence |
|----------|--------|------------|
| `{{kw_set_1}}` | {{action_1}} | `{{conf_1}}` |
| `{{kw_set_2}}` | {{action_2}} | `{{conf_2}}` |
| `{{kw_set_3}}` | {{action_3}} | `{{conf_3}}` |
## Decision Tree
1. IF `{{condition_1}}` THEN {{action_a}} ELSE `{{action_b}}`
2. IF `{{condition_2}}` THEN `{{action_c}}`
## Priorities
1. `{{priority_1}}` (highest)
2. `{{priority_2}}`
3. `{{priority_3}}` (lowest)
## Heuristics
- `{{heuristic_1}}`
- `{{heuristic_2}}`
## Domain Map
Covers: `{{domain_list}}`
Routes away: `{{routed_domains_with_targets}}`
## References
- Source agent: `{{agent_definition_path}}`
- Builder: mental-model-builder v1.0.0

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_mental_model]] | upstream | 0.46 |
| [[bld_knowledge_card_mental_model]] | upstream | 0.42 |
| [[p03_sp_mental_model_builder]] | upstream | 0.42 |
| [[p11_qg_mental_model]] | downstream | 0.39 |
| [[mental-model-builder]] | upstream | 0.39 |
| [[bld_schema_mental_model]] | downstream | 0.39 |
| [[bld_examples_mental_model]] | downstream | 0.38 |
| [[bld_config_mental_model]] | downstream | 0.36 |
| [[bld_collaboration_mental_model]] | upstream | 0.36 |
| [[bld_architecture_mental_model]] | downstream | 0.33 |
