---
id: "p08_ac_{{slug}}"
kind: agent_card
pillar: P08
title: "Agent Card: {{name}}"
version: 1.0.0
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
quality: 9.0
tags: [agent-card, "{{domain}}", "{{model}}"]
tldr: "Defines the agent card specification for agent card: {{name}}, with structural rules, validation gates, and integration points."
density_score: null
domain: "{{domain}}"
model: "{{model}}"
boot_time_seconds: null
linked_artifacts:
  agent: "{{agent_id}}"
  boot_config: "{{boot_config_id}}"
  spawn_config: "{{spawn_config_id}}"
related:
  - skill
  - tpl_validation_schema
  - research_then_build
  - model-card-builder
  - p03_ins_agent_card_builder
  - agent-card-builder
  - bld_collaboration_model_card
  - bld_tools_context_window_config
  - bld_tools_multi_modal_config
  - bld_memory_agent_card
---

# Agent Card: {{name}}

## Identity
| Property | Value |
|----------|-------|
| Name | {{name}} |
| Domain | {{domain}} |
| Model | {{model}} |
| Role | {{role_statement}} |

## Capabilities
{{capabilities_table}}

## Dispatch Keywords
{{dispatch_keywords}}

## Model Config
```yaml
model: {{model}}
context_window: {{context_window}}
temperature: {{temperature}}
max_tokens: {{max_tokens}}
```

## Tools (MCP Servers)
{{mcp_bindings}}

## Boot Sequence
{{boot_steps}}

## Constraints
### Hard (NEVER)
{{hard_constraints}}
### Soft (PREFER)
{{soft_constraints}}

## Scaling
{{scaling_config}}

## Monitoring
{{monitoring_config}}

## Lifecycle

1. Created via 8F pipeline (F1-Focus through F8-Furnish)
2. Scored by `cex_score.py` (3-layer: structural + rubric + semantic)
3. Compiled by `cex_compile.py` for validation
4. Retrieved by `cex_retriever.py` for context injection
5. Evolved by `cex_evolve.py` when quality drops below threshold

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `agent_card` |
| Pillar | P08 |
| Domain | {{domain}} |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[skill]] | related | 0.34 |
| [[tpl_validation_schema]] | upstream | 0.34 |
| [[research_then_build]] | related | 0.33 |
| [[model-card-builder]] | upstream | 0.32 |
| [[p03_ins_agent_card_builder]] | upstream | 0.30 |
| [[agent-card-builder]] | related | 0.29 |
| [[bld_collaboration_model_card]] | upstream | 0.29 |
| [[bld_tools_context_window_config]] | upstream | 0.26 |
| [[bld_tools_multi_modal_config]] | upstream | 0.24 |
| [[bld_memory_agent_card]] | downstream | 0.24 |
