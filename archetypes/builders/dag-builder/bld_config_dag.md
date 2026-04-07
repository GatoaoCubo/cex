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
---
# Config: dag Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p12_dag_{pipeline}.yaml` | `p12_dag_content_pipeline.yaml` |
| Builder directory | kebab-case | `dag-builder/` |
| Frontmatter fields | snake_case | `execution_order`, `critical_path` |
| Node ids | lowercase slug | `research`, `write_copy`, `publish` |
| Satellite values | lowercase slug | `edison`, `shaka`, `atlas` |
Rule: use `.yaml` only for this builder.
## File Paths
- Output: `cex/P12_orchestration/compiled/p12_dag_{pipeline}.yaml`
- Human reference: `cex/P12_orchestration/examples/p12_dag_{pipeline}.md`
## Size Limits
- Preferred DAG size: <= 2048 bytes
- Absolute max: 3072 bytes
- Nodes should have concise labels
## Structure Restrictions
- Graph MUST be acyclic: no circular dependencies allowed
- Every edge must reference existing node ids
- Node ids must be unique within the DAG
- Edges direction: `from` complete before `to` starts
## Boundary Restrictions
- No runtime execution logic: actions, timeouts, error handling belong in workflow
- No component inventory: ownership, health status belong in component_map
- No prompt sequencing: text pipelines belong in chain
- No status events: completion/error reporting belongs in signal
