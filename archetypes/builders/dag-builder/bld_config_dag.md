---
kind: config
id: bld_config_dag
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Dag"
version: "1.0.0"
author: n03_builder
tags: [dag, builder, examples]
tldr: "Golden and anti-examples for dag construction, demonstrating ideal structure and common pitfalls."
domain: "dag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_dag
  - dag-builder
  - bld_collaboration_dag
  - bld_architecture_dag
  - bld_config_handoff
  - bld_config_retriever_config
  - bld_config_signal
  - bld_examples_dag
  - bld_config_prompt_version
  - p11_qg_dag
---
# Config: dag Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p12_dag_{pipeline}.yaml` | `p12_dag_content_pipeline.yaml` |
| Builder directory | kebab-case | `dag-builder/` |
| Frontmatter fields | snake_case | `execution_order`, `critical_path` |
| Node ids | lowercase slug | `research`, `write_copy`, `publish` |
| Agent_group values | lowercase slug | `edison`, `shaka`, `atlas` |
Rule: use `.yaml` only for this builder.
## File Paths
1. Output: `cex/P12_orchestration/compiled/p12_dag_{pipeline}.yaml`
2. Human reference: `cex/P12_orchestration/examples/p12_dag_{pipeline}.md`
## Size Limits
1. Preferred DAG size: <= 2048 bytes
2. Absolute max: 3072 bytes
3. Nodes should have concise labels
## Structure Restrictions
1. Graph MUST be acyclic: no circular dependencies allowed
2. Every edge must reference existing node ids
3. Node ids must be unique within the DAG
4. Edges direction: `from` complete before `to` starts
## Boundary Restrictions
1. No runtime execution logic: actions, timeouts, error handling belong in workflow
2. No component inventory: ownership, health status belong in component_map
3. No prompt sequencing: text pipelines belong in chain
4. No status events: completion/error reporting belongs in signal

## Metadata

```yaml
id: bld_config_dag
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-dag.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
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
| [[bld_tools_dag]] | upstream | 0.43 |
| [[dag-builder]] | downstream | 0.39 |
| [[bld_collaboration_dag]] | downstream | 0.38 |
| [[bld_architecture_dag]] | upstream | 0.36 |
| [[bld_config_handoff]] | sibling | 0.36 |
| [[bld_config_retriever_config]] | sibling | 0.35 |
| [[bld_config_signal]] | sibling | 0.35 |
| [[bld_examples_dag]] | upstream | 0.34 |
| [[bld_config_prompt_version]] | sibling | 0.33 |
| [[p11_qg_dag]] | downstream | 0.33 |
