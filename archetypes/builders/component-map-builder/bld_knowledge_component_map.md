---
kind: knowledge_card
id: bld_knowledge_card_component_map
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for component_map production — structured system inventories
sources: systems engineering (CMDB), microservice registries, C4 model, dependency graph theory
quality: 9.1
title: "Knowledge Card Component Map"
version: "1.0.0"
author: n03_builder
tags: [component_map, builder, examples]
tldr: "Golden and anti-examples for component map construction, demonstrating ideal structure and common pitfalls."
domain: "component map construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_component_map_builder
  - p10_lr_component_map_builder
  - component-map-builder
  - bld_schema_component_map
  - bld_instruction_component_map
  - bld_collaboration_component_map
  - p11_qg_component_map
  - bld_architecture_component_map
  - p01_kc_component_map
  - bld_config_component_map
---

# Domain Knowledge: component_map
## Executive Summary
Component maps are structured inventories of system parts and their typed connections. A map is DATA, not a picture — it produces queryable records of what exists, who owns it, how parts connect, and their health status. Component maps differ from diagrams (visual representation), patterns (prescriptive solutions), and workflows (execution sequences).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P08 (architecture) |
| Frontmatter fields | 19+ |
| Quality gates | 9 HARD + 10 SOFT |
| Per-component fields | id, label, owner, status, receives, produces_for |
| Connection types | data_flow, depends, signals, produces, bidirectional |
| Topology patterns | layered, hub-spoke, pipeline |
## Patterns
- **Topology selection**: match architecture to topology pattern
| Topology | Structure | Use case |
|----------|-----------|----------|
| Layered | [UI] → [Logic] → [Data] | Multi-tier, top-down navigation |
| Hub-Spoke | [Spokes] ↔ [Hub] | Router/gateway architectures |
| Pipeline | [A] → [B] → [C] → [D] | Sequential processing chains |
- **Typed connections**: every connection MUST have a type label — untyped arrows are forbidden
| Notation | Meaning | Example |
|----------|---------|---------|
| A → B | Data flow | Parser → Classifier |
| A --depends→ B | Requirement | Search --depends→ Embeddings |
| A --signals→ B | Event notification | Worker --signals→ Monitor |
| A ↔ B | Bidirectional | Cache ↔ Database |
- **Data-first format**: tables for inventory + ASCII for topology — best LLM comprehension
- **Scope discipline**: define scope in one sentence; if you cannot, split the map
- **Ownership tracking**: every component has an assigned owner and health status
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Orphan components (zero connections) | Unreachable parts indicate incomplete mapping |
| Circular dependencies (A→B→C→A) | Break with queues or events |
| Untyped connections | Ambiguous relationships; cannot reason about data flow |
| Vague scope ("the system") | Too broad; split into focused maps per domain |
| Missing ownership | No accountability; stale components go unnoticed |
| Diagram without data tables | Visual without queryable data; tables first |
## Application
1. Define scope: one sentence describing what this map covers
2. Inventory components: id, label, owner, status for each
3. Map connections: typed arrows with direction and data description
4. Select topology: layered, hub-spoke, or pipeline
5. Document per component: receives (from whom, what) and produces_for (to whom, what)
6. Validate: no orphans, no untyped connections, scope is one sentence
## References
- CMDB: Configuration Management Database patterns
- C4 Model (Brown 2018): Context/Container/Component/Code zoom levels
- Enterprise Integration Patterns: connection and messaging types
- Systems engineering: decomposition and interface analysis

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_component_map_builder]] | downstream | 0.37 |
| [[p10_lr_component_map_builder]] | downstream | 0.36 |
| [[component-map-builder]] | downstream | 0.35 |
| [[bld_schema_component_map]] | related | 0.35 |
| [[bld_instruction_component_map]] | downstream | 0.34 |
| [[bld_collaboration_component_map]] | downstream | 0.34 |
| [[p11_qg_component_map]] | downstream | 0.32 |
| [[bld_architecture_component_map]] | downstream | 0.29 |
| [[p01_kc_component_map]] | sibling | 0.28 |
| [[bld_config_component_map]] | related | 0.25 |
