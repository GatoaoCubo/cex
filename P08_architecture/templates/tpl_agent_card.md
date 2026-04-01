---
id: "p08_ac_{{slug}}"
kind: agent_card
pillar: P08
title: "Agent Card: {{name}}"
version: 1.0.0
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
quality: 8.7
tags: [agent-card, "{{domain}}", "{{model}}"]
tldr: "{{one_line_description}}"
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
