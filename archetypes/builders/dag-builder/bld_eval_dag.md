---
kind: quality_gate
id: p11_qg_dag
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of dag artifacts
pattern: few-shot learning for dependency graph specification
quality: 9.0
title: "Gate: dag"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, dag, dependency-graph, topological-order, P11]
tldr: "Gates for dag artifacts: validates acyclicity, node naming, edge correctness, topological ordering, and parallelism opportunities."
domain: "dag — directed acyclic graphs defining task dependency order and parallelism"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.89
related:
  - bld_instruction_dag
  - bld_examples_dag
  - bld_architecture_dag
  - bld_collaboration_dag
  - bld_schema_dag
  - bld_config_dag
  - p10_lr_dag_builder
  - bld_knowledge_card_dag
  - p01_kc_dag
  - dag-builder
---

## Quality Gate

# Gate: dag
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: dag` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p12_dag_[a-z][a-z0-9_]+$` | "ID fails dag namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"dag"` | "Kind is not 'dag'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, domain, nodes, edges, version, created, author, tags | "Missing required field(s)" |
| H07 | Graph contains no cycles (topological sort succeeds) | "Cycle detected — not a DAG" |
| H08 | All edge source and target node IDs exist in `nodes` list | "Edge references undefined node" |
| H09 | `nodes` list is non-empty (>= 2 nodes) | "DAG must contain at least 2 nodes" |
| H10 | Every node has a unique `id` within the DAG | "Duplicate node ID detected" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Topological order documented | 1.0 | Explicit ordering or layers annotated in body |
| Parallelism opportunities | 1.0 | Nodes with no shared dependencies are identified |
| Node descriptions | 1.0 | Each node has purpose/role description, not just ID |
| Edge semantics | 0.5 | Edges labeled with dependency type (data, control, trigger) |
| Critical path marked | 1.0 | Longest path through graph identified |
| Entry and exit nodes | 0.5 | Root nodes (no incoming) and leaf nodes (no outgoing) explicit |
| Max depth documented | 0.5 | Depth of longest chain stated |
| Node count vs complexity | 1.0 | Graph is apowntely sized (not over-decomposed or monolithic) |
| Boundary clarity | 0.5 | Explicitly not workflow (runtime) or component_map (inventory) |
| Error propagation | 1.0 | What happens when a node fails: skip, abort, retry |
| Reuse potential | 1.0 | Nodes are generic enough to be referenced by multiple DAGs |
| Documentation | 1.0 | tldr explains the business purpose of this dependency structure |
Weight sum: 1.0+1.0+1.0+0.5+1.0+0.5+0.5+1.0+0.5+1.0+1.0+1.0 = 10.0 (100%)
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Prototype pipeline where full dependency mapping is not yet possible |
| approver | Pipeline owner approval required (written) |
| audit_trail | Bypass event logged to `records/audits/dag_bypass_{date}.md` |
| expiry | 72h; artifact must reach >= 7.0 or be removed from active use |
| never_bypass | H01 (YAML parse failure), H05 (quality null invariant), H07 (cyclic graph breaks all topological tooling) |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
