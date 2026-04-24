---
id: p01_kc_component_map
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P08
title: "Component Map — Deep Knowledge for component_map"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: component_map
quality: 9.1
tags: [component_map, P08, INJECT, kind-kc]
tldr: "component_map is a structured YAML artifact encoding what connects to what — nodes (components) and directed edges (connections with port labels) for a bounded scope."
when_to_use: "Building, reviewing, or reasoning about component_map artifacts"
keywords: [component_topology, wiring, dependency_graph]
feeds_kinds: [component_map]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - component-map-builder
  - p01_kc_diagram
  - bld_collaboration_agent_card
  - bld_knowledge_card_component_map
  - p11_qg_component_map
  - p01_kc_dag
  - bld_schema_component_map
  - bld_collaboration_component_map
  - p03_sp_component_map_builder
  - p11_qg_agent-card
---

# Component Map

## Spec
```yaml
kind: component_map
pillar: P08
llm_function: INJECT
max_bytes: 3072
naming: p08_cmap_{{scope}}.yaml
core: false
```

## What It Is
A component_map is a structured map of components and their directed connections within a bounded scope — it answers "what connects to what" with explicit nodes and labeled edges. It is NOT a diagram (visual rendering), NOT an agent_card (scoped to a single agent_group identity), and NOT a workflow (no execution sequence or step ordering).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableSequence` / LCEL graph | Shows Runnable connections via pipe operator |
| LlamaIndex | `Workflow` event graph | Event-driven node connections in AgentWorkflow |
| CrewAI | `Crew` agents+tasks topology | Which agents handle which tasks, process type |
| DSPy | `Module.forward()` data flow | Input fields → submodules → output fields |
| Haystack | `Pipeline.connect()` wiring | Explicit src.output_name → dst.input_name |
| OpenAI | `Run Steps` graph | tool_calls → message_creation topology |
| Anthropic | Agentic loop topology | tool_use blocks → tool_result flow map |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| scope | string | required | system/agent_group/layer — broader = less actionable |
| nodes | list[ComponentRef] | required | More nodes = richer but harder to read |
| edges | list[EdgeDef] | required | Missing edges = silent coupling; over-specifying = brittle |
| version | string | 1.0.0 | Bump on structural change, not on data/content change |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Layer map | Auditing P01-P12 pillar interconnect | p08_cmap_system.yaml — all pillars as nodes |
| Agent_group topology | One agent_group's agent + tool connections | p08_cmap_atlas.yaml — operations_agent agents + MCP tools |
| Data flow | Tracing data transformation between stages | input → chunk → embed → index flow |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Mega-map | All 118 agents in one map is unreadable | Scope to 1 agent_group or 1 layer at a time |
| Stale map | Map diverges silently from live codebase | Version-gate: map version must match codebase tag |
| Unlabeled ports | Edges without src/dst port names cause ambiguity | Always label edge source and destination ports |

## Integration Graph
```
diagram, agent_card --> [component_map] --> workflow, law, decision_record
                              |
                         pattern, path_config, naming_rule
```

## Decision Tree
- IF visualizing one agent_group's internals THEN agent_group topology map
- IF auditing data transformation THEN data flow map
- IF designing new system architecture THEN system-level layer map first
- DEFAULT: agent_group topology, 1:1 with agents, one file per agent_group

## Quality Criteria
- GOOD: all nodes labeled, edges directed with port labels, scope and version present
- GREAT: ASCII or Mermaid visual fallback included, linked to agent_card files
- FAIL: undirected edges, missing scope, >20 nodes without subgraph decomposition

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[component-map-builder]] | related | 0.31 |
| [[p01_kc_diagram]] | sibling | 0.29 |
| [[bld_collaboration_agent_card]] | related | 0.28 |
| [[bld_knowledge_card_component_map]] | sibling | 0.27 |
| [[p11_qg_component_map]] | downstream | 0.27 |
| [[p01_kc_dag]] | sibling | 0.25 |
| [[bld_schema_component_map]] | related | 0.24 |
| [[bld_collaboration_component_map]] | downstream | 0.24 |
| [[p03_sp_component_map_builder]] | related | 0.23 |
| [[p11_qg_agent-card]] | downstream | 0.23 |
