---
kind: output_template
id: bld_output_template_spawn_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a spawn_config
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Spawn Config"
version: "1.0.0"
author: n03_builder
tags: [spawn_config, builder, examples]
tldr: "Golden and anti-examples for spawn config construction, demonstrating ideal structure and common pitfalls."
domain: "spawn config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_spawn_config
  - bld_collaboration_spawn_config
  - bld_architecture_spawn_config
  - spawn-config-builder
  - p01_kc_spawn_config
  - bld_schema_spawn_config
  - bld_examples_spawn_config
  - p11_qg_spawn_config
  - bld_memory_spawn_config
  - bld_config_spawn_config
---

# Output Template: spawn_config
```yaml
id: p12_spawn_{{mode_slug}}
kind: spawn_config
pillar: P12

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

title: "{{human_readable_title}}"
mode: {{solo|grid|continuous}}
agent_group: {{agent_group_name_or_list}}
model: "{{opus|sonnet|haiku}}"

flags:
  - "--dangerously-skip-permissions"
  - "--no-chrome"
  - "-p"

  {{...additional_flags}}
mcp_config: "{{path_to_mcp_json}}"
timeout: {{seconds}}
interactive: {{true|false}}

prompt_strategy: {{inline|handoff}}
domain: "{{domain_value}}"
quality: null
tags: [spawn_config, {{tag_2}}, {{tag_3}}]

tldr: "{{dense_summary_max_160ch}}"
```
## Spawn Command
```powershell
{{spawn_command_powershell}}
```
## Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| mode | `{{mode}}` | `{{why_this_mode}}` |
| agent_group | `{{agent_group}}` | `{{why_this_agent_group}}` |
| model | `{{model}}` | `{{why_this_model}}` |
| timeout | `{{timeout}}`s | `{{why_this_timeout}}` |
| interactive | `{{interactive}}` | `{{why_interactive_or_not}}` |
## Constraints
1. `{{constraint_1}}`
2. `{{constraint_2}}`
3. `{{constraint_3}}`
## References
- `{{reference_1}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | spawn config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_spawn_config]] | downstream | 0.46 |
| [[bld_collaboration_spawn_config]] | downstream | 0.43 |
| [[bld_architecture_spawn_config]] | downstream | 0.40 |
| [[spawn-config-builder]] | downstream | 0.40 |
| [[p01_kc_spawn_config]] | downstream | 0.40 |
| [[bld_schema_spawn_config]] | downstream | 0.39 |
| [[bld_examples_spawn_config]] | downstream | 0.37 |
| [[p11_qg_spawn_config]] | downstream | 0.37 |
| [[bld_memory_spawn_config]] | downstream | 0.35 |
| [[bld_config_spawn_config]] | downstream | 0.32 |
