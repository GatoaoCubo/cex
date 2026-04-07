---
kind: output_template
id: bld_output_template_dag
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a dag
pattern: every field here exists in SCHEMA.md; template derives, never invents
---

# Output Template: dag
Naming pattern: `p12_dag_{pipeline}.yaml`
Filename: `p12_dag_{{pipeline_slug}}.yaml`
```yaml
id: p12_dag_{{pipeline_slug}}
kind: dag
lp: P12
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
pipeline: "{{pipeline_or_mission_name}}"
nodes:
  - id: "{{node_id_1}}"
    label: "{{task_description_1}}"
    agent_group: "{{executor_1}}"
  - id: "{{node_id_2}}"
    label: "{{task_description_2}}"
    agent_group: "{{executor_2}}"
edges:
  - from: "{{source_node_id}}"
    to: "{{target_node_id}}"
domain: "{{domain_value}}"
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
execution_order:
  - [{{wave_1_node_ids}}]
  - [{{wave_2_node_ids}}]
parallel_groups:
  - [{{parallel_node_ids}}]
critical_path: [{{longest_chain_node_ids}}]
estimated_duration: "{{time_estimate_or_omit}}"
node_count: {{integer_or_omit}}
edge_count: {{integer_or_omit}}
max_parallelism: {{integer_or_omit}}
keywords: [{{keyword_1}}, {{keyword_2}}]
linked_artifacts:
  primary: "{{primary_ref_or_omit}}"
  related: [{{related_refs_or_omit}}]
```
## Derivation Notes
- Required fields (id through tldr) plus nodes and edges form the minimum valid DAG
- `execution_order` is the topologically sorted representation of nodes+edges
- Omit absent optional fields instead of writing placeholder values
- Keep the DAG as a static spec: no runtime state, no execution logic
