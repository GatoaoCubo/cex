---
kind: examples
id: bld_examples_dag
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of dag artifacts
pattern: few-shot learning for dependency graph specification
quality: 9.0
title: "Examples Dag"
version: "1.0.0"
author: n03_builder
tags: [dag, builder, examples]
tldr: "Golden and anti-examples for dag construction, demonstrating ideal structure and common pitfalls."
domain: "dag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: dag-builder
## Golden Example
INPUT: "Create DAG for content pipeline: research, write copy, create images, review, publish"
OUTPUT (`p12_dag_content_pipeline.yaml`):
```yaml
id: p12_dag_content_pipeline
kind: dag
lp: P12
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "codex"
pipeline: "content_pipeline"
nodes:
  - id: "research"
    label: "Research target market and competitors"
    agent_group: "shaka"
  - id: "write_copy"
    label: "Write marketing copy from research"
    agent_group: "lily"
  - id: "create_images"
    label: "Generate product images from research"
    agent_group: "edison"
  - id: "review"
    label: "Quality review of copy and images"
    agent_group: "atlas"
  - id: "publish"
    label: "Publish approved content to channels"
    agent_group: "atlas"
edges:
  - from: "research"
    to: "write_copy"
  - from: "research"
    to: "create_images"
  - from: "write_copy"
    to: "review"
  - from: "create_images"
    to: "review"
  - from: "review"
    to: "publish"
domain: "orchestration"
quality: null
tags: [dag, content-pipeline, multi-agent_group, dependency-graph]
tldr: "5-node content pipeline DAG: research fans out to copy+images, converges at review, then publish"
execution_order:
  - ["research"]
  - ["write_copy", "create_images"]
  - ["review"]
  - ["publish"]
parallel_groups:
  - ["write_copy", "create_images"]
critical_path: ["research", "write_copy", "review", "publish"]
estimated_duration: "45min"
node_count: 5
edge_count: 5
max_parallelism: 2
keywords: [content, pipeline, dag, multi-agent_group]
linked_artifacts:
  primary: "P12_orchestration/compiled/p12_dag_content_pipeline.yaml"
  related: ["archetypes/builders/workflow-builder/", "archetypes/builders/handoff-builder/"]
```
WHY THIS IS GOLDEN:
- filename follows `p12_dag_{pipeline}.yaml`
- YAML with proper frontmatter, 19+ fields present
- all required fields present and typed correctly
- graph is acyclic: research -> copy/images -> review -> publish
- execution_order correctly groups parallel nodes into waves
- critical_path identifies the longest dependency chain
- no runtime state, no execution logic, no error handling
## Anti-Example
BAD OUTPUT (`p12_wf_content.yaml`):
```yaml
id: p12_wf_content
kind: workflow
lp: P12
steps:
  - name: "research"
    action: "run shaka research agent"
    on_error: "retry 3x then skip"
    timeout: "10m"
  - name: "write"
    action: "run lily copy agent"
    depends_on: "research"
    on_error: "fallback to template"
  - name: "publish"
    action: "POST /api/publish"
    depends_on: "write"
runtime_state:
  current_step: "research"
  retries: 0
```
FAILURES:
1. wrong kind: `workflow` instead of `dag` (H02)
2. wrong id prefix: `p12_wf_` instead of `p12_dag_` (H01)
3. contains `on_error` handling: runtime execution logic is workflow drift (H08)
4. contains `timeout`: runtime constraint is workflow drift (H08)
5. contains `action` with API calls: execution logic is workflow drift (H08)
6. contains `runtime_state`: mutable state violates static spec rule (H09)
7. missing required fields: `nodes`, `edges`, `pipeline`, `quality`, `tags`, `tldr` (H03)
8. uses `steps` instead of `nodes`/`edges` graph structure (H08)
9. no proper node/edge separation: dependencies mixed into steps (H10)
10. no `execution_order` computed from graph topology
