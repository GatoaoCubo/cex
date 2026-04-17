---
id: p11_qg_dag
kind: quality_gate
pillar: P11
title: "Gate: dag"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "dag — directed acyclic graphs defining task dependency order and parallelism"
quality: 9.0
tags: [quality-gate, dag, dependency-graph, topological-order, P11]
tldr: "Gates for dag artifacts: validates acyclicity, node naming, edge correctness, topological ordering, and parallelism opportunities."
density_score: 0.89
llm_function: GOVERN
---
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
