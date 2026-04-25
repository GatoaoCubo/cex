---
id: bld_tpl_data_contract
kind: prompt_template
pillar: P03
llm_function: PRODUCE
version: 1.0.0
quality: 8.1
tags: [data_contract, template, output]
title: "Output Template: data_contract"
author: builder
tldr: "Data Contract prompt: output template, formatting rules, and structure"
density_score: 1.0
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_output_template_input_schema
  - bld_instruction_interface
  - p06_schema_env_contract
  - bld_output_template_interface
  - p10_lr_interface_builder
  - bld_schema_interface
  - bld_collaboration_input_schema
  - bld_examples_workflow_primitive
  - bld_output_template_entity_memory
  - bld_schema_entity_memory
---
# Output Template: data_contract
```markdown
---
id: dc_{{producer_snake}}_{{consumer_snake}}_{{entity_snake}}
kind: data_contract
pillar: P06
title: "{{Producer}} -> {{Consumer}}: {{Entity}} Contract"
version: 1.0.0
quality: null
producer_system: {{producer_system}}
consumer_system: {{consumer_system}}
entity: {{EntityPascalCase}}
contract_version: 1.0.0
effective_date: "{{YYYY-MM-DD}}"
tags: [{{producer}}, {{consumer}}, data-contract]
---

# {{Producer}} -> {{Consumer}}: {{Entity}} Data Contract

## Overview
{{One sentence describing what data the producer exposes to the consumer.}}

## Schema
| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| {{field_1}} | {{type}} | {{true/false}} | {{description}} |
| {{field_2}} | {{type}} | {{true/false}} | {{description}} |

## SLA
| Metric | Threshold | Measurement Method |
|--------|-----------|-------------------|
| freshness | {{Xs/Xmin/Xh}} | {{how measured}} |
| availability | {{XX.X%}} | {{monitoring source}} |
| latency_p99 | {{Xms}} | {{percentile source}} |

## Versioning Policy
- backward_compatible: {{true/false}}
- breaking_change_policy: {{X days notice + migration guide}}
- deprecation_notice: {{X days}}

## Enforcement
- Schema registry: {{registry_url or "none"}}
- Contract tests: {{tool or "none"}}
- Owner: {{team_or_person}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_input_schema]] | downstream | 0.23 |
| [[bld_instruction_interface]] | related | 0.22 |
| [[p06_schema_env_contract]] | downstream | 0.22 |
| [[bld_output_template_interface]] | downstream | 0.20 |
| [[p10_lr_interface_builder]] | downstream | 0.20 |
| [[bld_schema_interface]] | downstream | 0.19 |
| [[bld_collaboration_input_schema]] | downstream | 0.19 |
| [[bld_examples_workflow_primitive]] | downstream | 0.18 |
| [[bld_output_template_entity_memory]] | downstream | 0.18 |
| [[bld_schema_entity_memory]] | downstream | 0.18 |
