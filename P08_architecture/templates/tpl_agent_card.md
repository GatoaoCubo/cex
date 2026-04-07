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
