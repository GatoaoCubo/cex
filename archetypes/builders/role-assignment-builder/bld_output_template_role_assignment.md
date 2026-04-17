---
kind: output_template
id: bld_output_template_role_assignment
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for role_assignment production
quality: 9.0
title: "Output Template Role Assignment"
version: "1.0.0"
author: n03_wave8_builder
tags: [role_assignment, builder, output_template, composable, crewai]
tldr: "Template with vars for role_assignment production"
domain: "role_assignment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.86
---

```markdown
---
id: p02_ra_{{role_name}}.md
kind: role_assignment
pillar: P02
llm_function: CONSTRAIN
role_name: {{role_name}} <!-- snake_case, unique per crew -->
agent_id: {{agent_id}} <!-- .claude/agents/{slug}.md OR N0x/agents/... -->
goal: {{goal}} <!-- one-sentence measurable outcome -->
backstory: {{backstory}} <!-- CrewAI persona hook, 2-3 sentences -->
crewai_equivalent: {{crewai}} <!-- e.g., 'Agent(role=..., goal=..., backstory=...)' -->
quality: null
---

## Role Header
`{{role_name}}` -- bound to `{{agent_id}}`. {{one_line_purpose}}

## Responsibilities
1. {{responsibility_1}} <!-- inputs X, produces Y -->
2. {{responsibility_2}}
3. {{responsibility_3}}
4. {{responsibility_4}} <!-- optional -->

## Tools Allowed
- {{tool_1}} <!-- must exist in agent_id's native toolkit -->
- {{tool_2}}
- -{{excluded_tool}} <!-- explicitly excluded -->

## Delegation Policy
```yaml
can_delegate_to: [{{role_b}}, {{role_c}}]  # role_names, NOT agent_ids
conditions:
  on_quality_below: 8.0
  on_timeout: 300s
  on_keyword_match: [{{kw_1}}, {{kw_2}}]
```

## Backstory
{{backstory}} <!-- e.g., "You are a {{role_descriptor}} with {{experience}}. You specialize in {{focus}}." -->

## Goal
{{goal}} <!-- e.g., "Produce a brief with quality >= 9.0 under 600s wall-clock." -->

## Runtime Notes
- Sequential process: receives handoff from `{{upstream_role}}`, emits to `{{downstream_role}}`.
- Hierarchical process: {{manager_or_worker}} position; {{delegation_behavior}}.
- Consensus process: {{vote_weight}} weight in peer vote.
```
