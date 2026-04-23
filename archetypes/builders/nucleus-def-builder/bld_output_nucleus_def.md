---
kind: output_template
id: bld_output_template_nucleus_def
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for nucleus_def production
quality: 9.1
title: "Output Template Nucleus Def"
version: "1.0.0"
author: n05_wave8
tags: [nucleus_def, builder, output_template]
tldr: "Template with vars for nucleus_def production"
domain: "nucleus_def construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_nucleus_def
  - bld_tools_nucleus_def
  - bld_instruction_nucleus_def
  - bld_schema_nucleus_def
  - nucleus-def-builder
  - bld_collaboration_nucleus_def
  - p02_qg_nucleus_def
  - p10_lr_nucleus_def_builder
  - bld_knowledge_card_nucleus_def
  - p02_nd_n03.md
---

```markdown
---
id: p02_nd_{{nucleus_id_lower}}.md
kind: nucleus_def
pillar: P02
nucleus_id: {{nucleus_id}}
role: {{role}}
sin_lens: "{{sin_lens}}"
cli_binding: {{cli_binding}}
model_tier: {{model_tier}}
model_specific: {{model_specific}}
context_tokens: {{context_tokens}}
boot_script: {{boot_script}}
agent_card_path: {{agent_card_path}}
pillars_owned: {{pillars_owned_yaml}}
crew_templates_exposed: {{crew_templates_yaml}}
domain_agents: {{domain_agents_yaml}}
fallback_cli: {{fallback_cli}}
title: "Nucleus Def {{nucleus_id}}"
version: "1.0.0"
author: {{author}}
domain: "{{domain}}"
quality: null
tags: [nucleus_def, {{nucleus_id_lower}}, {{role}}, composable]
tldr: "Formal definition of {{nucleus_id}} -- {{role}} nucleus, {{cli_binding}}/{{model_tier}}"
created: "{{date}}"
updated: "{{date}}"
density_score: 0.85
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus ID | {{nucleus_id}} |
| Role | {{role}} |
| Sin Lens | {{sin_lens}} |
| CLI Binding | {{cli_binding}} |
| Model Tier | {{model_tier}} |
| Model | {{model_specific}} |
| Context | {{context_tokens}} tokens |
| Boot Script | `{{boot_script}}` |
| Agent Card | `{{agent_card_path}}` |

## Pillars Owned

| Pillar | Domain | Sample Kinds |
|--------|--------|-------------|
{{pillars_owned_table}}

## Crew Templates Exposed

| Template | Role in Crew | Inputs | Outputs |
|----------|-------------|--------|---------|
{{crew_templates_table}}

## Domain Agents

| Agent | Purpose | Path |
|-------|---------|------|
{{domain_agents_table}}

## Boot Contract

- **Boot file**: `{{boot_script}}`
- **Task source**: `.cex/runtime/handoffs/{{nucleus_id_lower}}_task.md` (ALWAYS reads from file, never CLI arg)
- **Signal format**: `write_signal('{{nucleus_id_lower}}', 'complete', {score})`
- **Signal path**: `.cex/runtime/signals/signal_{{nucleus_id_lower}}_*.json`

## Composability

| Direction | Nucleus | What Flows |
|-----------|---------|-----------|
{{composability_table}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_nucleus_def]] | downstream | 0.49 |
| [[bld_tools_nucleus_def]] | upstream | 0.49 |
| [[bld_instruction_nucleus_def]] | upstream | 0.44 |
| [[bld_schema_nucleus_def]] | downstream | 0.44 |
| [[nucleus-def-builder]] | upstream | 0.38 |
| [[bld_collaboration_nucleus_def]] | downstream | 0.37 |
| [[p02_qg_nucleus_def]] | downstream | 0.36 |
| [[p10_lr_nucleus_def_builder]] | downstream | 0.31 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.30 |
| [[p02_nd_n03.md]] | upstream | 0.29 |
