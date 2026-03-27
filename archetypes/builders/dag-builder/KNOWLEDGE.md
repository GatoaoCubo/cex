---
pillar: P01
llm_function: INJECT
purpose: Operational knowledge and patterns for dag production
sources: P12 schema + graph theory + CODEXA orchestration patterns
---

# Domain Knowledge: dag

## Core Concept
`dag` is the static dependency specification for a pipeline or mission.
It answers: "What tasks exist, what depends on what, and what can run in parallel?"

DAGs are blueprints, not executors.
They are consumed by workflow engines, orchestrators, and spawn planners.

## Minimum Semantic Contract
Every valid dag carries:
- `pipeline`: what mission this graph describes
- `nodes`: list of tasks with id, label, and optional satellite
- `edges`: directed dependency relationships between nodes

Plus standard CEX fields: id, kind, lp, version, dates, author, quality, tags, tldr.

## Graph Properties
| Property | Requirement |
|----------|-------------|
| Acyclicity | MUST be acyclic — cycles are validation failure |
| Direction | Edges point from dependency to dependent |
| Entry points | Nodes with no incoming edges start first |
| Terminal points | Nodes with no outgoing edges are endpoints |
| Parallelism | Nodes in the same wave with no mutual edges run in parallel |

## Execution Order Derivation
Topological sort groups nodes into waves:
- Wave 1: nodes with no incoming edges (entry points)
- Wave 2: nodes whose dependencies are all in Wave 1
- Wave N: nodes whose dependencies are all in Waves 1..N-1

This is `execution_order` in the schema.

## Boundary vs Nearby Types
| Type | What it is | Why it is not `dag` |
|------|------------|---------------------|
| workflow | executable step sequence with runtime logic | has actions, error handling, state |
| component_map | inventory of system components | describes what exists, not dependencies |
| chain | prompt sequence (text pipeline) | P03 domain, not orchestration |
| spawn_config | satellite boot parameters | how to start, not what depends on what |

Rule of thumb:
- "What depends on what?" -> `dag`
- "How to execute step by step?" -> `workflow`
- "What components exist?" -> `component_map`

## Naming Pattern
P12 schema defines: `p12_dag_{{pipeline}}.yaml`
Examples:
- `p12_dag_content_pipeline.yaml`
- `p12_dag_wave19_builders.yaml`
- `p12_dag_deploy_sequence.yaml`

## Operational Constraints
- Must stay under 3072 bytes
- Should remain a static spec, not a runtime artifact
- Should be easy to topologically sort programmatically
- Must degrade gracefully when optional fields are absent
