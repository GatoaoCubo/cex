---
kind: output_template
id: bld_output_template_director
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a director artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: director
```yaml
id: p08_dir_{{name_lower}}
kind: director
pillar: P08
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{director_name}}"
mission: "{{one_sentence_crew_outcome}}"
entry_point: "{{first_builder_id}}"
exit_point: "{{final_builder_id}}"
builders: [{{builder_id_1}}, {{builder_id_2}}, {{builder_id_3}}]
dag_edges:
  - from: "{{builder_id_1}}"
    to: "{{builder_id_2}}"
    data: "{{data_passed_description}}"
  - from: "{{builder_id_2}}"
    to: "{{builder_id_3}}"
    data: "{{data_passed_description}}"
parallelism:
  parallel_groups:
    - [{{builder_id_a}}, {{builder_id_b}}]
  must_sequence:
    - [{{builder_id_c}}, {{builder_id_d}}]
handoff_contracts:
  - from: "{{builder_id_1}}"
    to: "{{builder_id_2}}"
    schema: "{{data_type_or_fields}}"
    required: {{boolean}}
failure_handling:
  - builder: "{{builder_id_1}}"
    strategy: "{{skip|retry|abort_crew|fallback_to}}"
    fallback: "{{fallback_builder_id_or_null}}"
constraints:
  - "{{constraint_1}}"
  - "{{constraint_2}}"
dependencies: [{{external_service_1}}]
estimated_duration: "{{human_readable_duration_or_null}}"
domain: "{{domain_value}}"
quality: null
tags: [director, {{domain_tag}}, {{name_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Crew Composition
{{table_of_all_builders_with_role_input_output_sequence_position}}
## DAG Structure
{{directed_graph_with_edges_and_data_flow}}
## Handoff Protocol
{{data_contracts_for_each_connected_builder_pair}}
## Parallelism Rules
{{concurrent_groups_and_sequencing_constraints}}
## Failure Handling
{{per_builder_fallback_and_crew_level_recovery}}
## Entry and Exit
{{entry_point_and_exit_point_with_acceptance_criteria}}
## Constraints
{{operational_never_rules_for_the_crew}}
## References
- {{reference_1}}
- {{reference_2}}
