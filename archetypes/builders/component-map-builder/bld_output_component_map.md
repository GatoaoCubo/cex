---
pillar: P00
id: bld_output_template_component_map
kind: output_template
parent: component-map-builder
version: 1.0.0
quality: 9.0
title: "Output Template Component Map"
author: n03_builder
tags: [component_map, builder, examples]
tldr: "Golden and anti-examples for component map construction, demonstrating ideal structure and common pitfalls."
domain: "component map construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: PRODUCE
related:
  - bld_schema_component_map
  - bld_instruction_component_map
  - bld_output_template_diagram
  - p03_sp_component_map_builder
  - bld_config_component_map
  - p11_qg_component_map
  - bld_examples_component_map
  - bld_collaboration_component_map
  - p10_lr_component_map_builder
  - component-map-builder
---
# Output Template — component-map-builder
NOTE: component_map uses YAML format (machine_format: yaml). Output extension is `.yaml`.
```yaml
id: p08_cmap_{{scope_slug}}
kind: component_map
pillar: P08
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
domain: "{{domain}}"
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
scope: "{{what_system_or_subsystem}}"
component_count: {{integer}}
connection_count: {{integer}}
components:
  - {name: "{{component_1}}", role: "{{role_1}}", owner: "{{owner_1}}", status: "{{active|deprecated|planned}}"}
  - {name: "{{component_2}}", role: "{{role_2}}", owner: "{{owner_2}}", status: "{{active|deprecated|planned}}"}
connections:
  - {from: "{{from_1}}", to: "{{to_1}}", type: "{{data_flow|dependency|signal}}"}
  - {from: "{{from_2}}", to: "{{to_2}}", type: "{{data_flow|dependency|signal}}"}
interfaces:
  - {boundary: "{{boundary_1}}", components: "{{comp_a}} <-> {{comp_b}}", contract: "{{contract_1}}"}
dependencies:
  - {component: "{{comp_1}}", depends_on: "{{dep_1}}", failure_impact: "{{impact_1}}"}
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
## Scope
{{scope_description_and_boundaries}}
## Components
| Component | Role | Owner | Status | Version |
|-----------|------|-------|--------|---------|
| {{component_1}} | {{role_1}} | {{owner_1}} | {{active|deprecated|planned}} | {{ver_1}} |
| {{component_2}} | {{role_2}} | {{owner_2}} | {{active|deprecated|planned}} | {{ver_2}} |
## Connections
| From | To | Type | Data | Direction |
|------|-----|------|------|-----------|
| {{from_1}} | {{to_1}} | {{data_flow|dependency|signal}} | {{data_1}} | {{unidirectional|bidirectional}} |
## Interfaces
| Boundary | Components | Contract | Status |
|----------|-----------|----------|--------|
| {{boundary_1}} | {{comp_a}} <-> {{comp_b}} | {{contract_1}} | {{active|planned}} |
## Dependencies
| Component | Depends On | Failure Impact |
|-----------|-----------|---------------|
| {{comp_1}} | {{dep_1}} | {{impact_1}} |
## Boundaries
{{where_this_map_ends_and_what_is_out_of_scope}}
## References
- {{reference_1}}
- {{reference_2}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_component_map]] | related | 0.36 |
| [[bld_instruction_component_map]] | related | 0.32 |
| [[bld_output_template_diagram]] | sibling | 0.32 |
| [[p03_sp_component_map_builder]] | related | 0.30 |
| [[bld_config_component_map]] | related | 0.29 |
| [[p11_qg_component_map]] | related | 0.28 |
| [[bld_examples_component_map]] | related | 0.27 |
| [[bld_collaboration_component_map]] | related | 0.27 |
| [[p10_lr_component_map_builder]] | related | 0.26 |
| [[component-map-builder]] | related | 0.25 |
