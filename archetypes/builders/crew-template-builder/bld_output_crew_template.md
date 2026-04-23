---
kind: output_template
id: bld_output_template_crew_template
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for crew_template production
quality: 9.1
title: "Output Template Crew Template"
version: "1.0.0"
author: n03_wave8_builder
tags: [crew_template, builder, output_template, composable, crewai]
tldr: "Template with vars for crew_template production"
domain: "crew_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_instruction_crew_template
  - bld_schema_crew_template
  - crew-template-builder
  - bld_knowledge_card_crew_template
  - bld_examples_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - p03_sp_crew_template_builder
  - p12_ct_product_launch.md
  - bld_tools_crew_template
---

```markdown
---
id: p12_ct_{{crew_name}}.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: {{crew_name}}
purpose: {{purpose}} <!-- one-sentence task boundary -->
process: {{process}} <!-- sequential | hierarchical | consensus -->
crewai_equivalent: {{crewai}} <!-- e.g., 'Process.sequential' -->
autogen_equivalent: {{autogen}} <!-- e.g., 'GroupChat.round_robin' -->
swarm_equivalent: {{swarm}} <!-- e.g., 'triage -> sales -> refunds' -->
handoff_protocol_id: {{handoff_proto_id}}
quality: null
---

## Overview
{{overview}} <!-- crew intent, when to instantiate, who consumes the output -->

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| {{role_1_name}} | p02_ra_{{role_1}}.md | {{role_1_reason}} |
| {{role_2_name}} | p02_ra_{{role_2}}.md | {{role_2_reason}} |
| {{role_3_name}} | p02_ra_{{role_3}}.md | {{role_3_reason}} |

## Process
Topology: `{{process}}`. Rationale: {{process_rationale}}.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| {{role_1_name}} | {{scope_1}} <!-- private \| shared \| persistent --> | {{retain_1}} |
| {{role_2_name}} | {{scope_2}} | {{retain_2}} |
| {{role_3_name}} | {{scope_3}} | {{retain_3}} |

## Handoff Protocol
`{{handoff_proto_id}}` -- {{handoff_summary}} <!-- A2A Task | OpenAI transfer fn | native -->

## Success Criteria
- [ ] {{criterion_1}} <!-- e.g., quality >= 9.0 -->
- [ ] {{criterion_2}} <!-- e.g., all handoffs committed -->
- [ ] {{criterion_3}} <!-- e.g., gate H01-H08 pass -->

## Instantiation
```python
from cex_sdk.crew import Crew
crew = Crew.from_template('p12_ct_{{crew_name}}.md')
result = crew.run(inputs={{inputs}})
```
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_crew_template]] | upstream | 0.48 |
| [[bld_schema_crew_template]] | downstream | 0.42 |
| [[crew-template-builder]] | downstream | 0.41 |
| [[bld_knowledge_card_crew_template]] | upstream | 0.39 |
| [[bld_examples_crew_template]] | downstream | 0.38 |
| [[bld_collaboration_crew_template]] | downstream | 0.34 |
| [[p11_qg_crew_template]] | downstream | 0.33 |
| [[p03_sp_crew_template_builder]] | upstream | 0.33 |
| [[p12_ct_product_launch.md]] | downstream | 0.28 |
| [[bld_tools_crew_template]] | upstream | 0.26 |
