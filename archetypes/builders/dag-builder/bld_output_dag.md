---
kind: output_template
id: bld_output_template_dag
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a dag
pattern: every field here exists in SCHEMA.md; template derives, never invents
quality: 9.0
title: "Output Template Dag"
version: "1.0.0"
author: n03_builder
tags: [dag, builder, examples]
tldr: "Golden and anti-examples for dag construction, demonstrating ideal structure and common pitfalls."
domain: "dag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_dag
  - bld_config_dag
  - bld_architecture_dag
  - bld_examples_dag
  - dag-builder
  - bld_output_template_session_state
  - bld_collaboration_dag
  - p11_qg_dag
  - p01_kc_dag
  - p10_lr_dag_builder
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
1. Required fields (id through tldr) plus nodes and edges form the minimum valid DAG
2. `execution_order` is the topologically sorted representation of nodes+edges
3. Omit absent optional fields instead of writing placeholder values
4. Keep the DAG as a static spec: no runtime state, no execution logic

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | dag construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_dag]] | downstream | 0.47 |
| [[bld_config_dag]] | downstream | 0.42 |
| [[bld_architecture_dag]] | downstream | 0.41 |
| [[bld_examples_dag]] | downstream | 0.39 |
| [[dag-builder]] | downstream | 0.38 |
| [[bld_output_template_session_state]] | sibling | 0.38 |
| [[bld_collaboration_dag]] | downstream | 0.34 |
| [[p11_qg_dag]] | downstream | 0.32 |
| [[p01_kc_dag]] | downstream | 0.32 |
| [[p10_lr_dag_builder]] | downstream | 0.31 |
