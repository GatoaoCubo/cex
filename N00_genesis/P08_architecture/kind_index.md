---
id: n00_p08_kind_index
kind: knowledge_card
8f: F3_inject
pillar: P08
nucleus: n00
title: "P08 Architecture -- Kind Index"
version: 1.0
quality: 8.9
tags: [index, p08, archetype, n00]
density_score: 1.0
related:
  - kc_intent_resolution_map
  - bld_architecture_kind
  - bld_collaboration_kind
  - kind-builder
  - p02_nd_n03.md
  - p12_dr_software_project
  - p12_dr_builder_nucleus
  - agent_card_n03
  - p02_agent_creation_nucleus
  - bld_collaboration_builder
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Master index of all 12 kinds in pillar P08. Reference for /mentor, nucleus builders, and the 8F pipeline.

## Pillar: P08 Architecture
System structure and design decisions: agent cards, capability registries, component maps, ADRs, diagrams, and architecture patterns. The blueprint layer that documents how the system is built.

## Kinds in P08

| Kind | Purpose | Primary Nucleus | Builder |
|------|---------|-----------------|---------|
| `agent_card` | Deployment spec for autonomous agent — identity, model, tools, boot, d | N07 | `agent_card-builder` |
| `agent_computer_interface` | GUI/terminal interaction protocol for agents | N03 | `agent_computer_interface-builder` |
| `capability_registry` | Searchable catalog of all agents available to crews. Indexes 252 build | N03 | `capability_registry-builder` |
| `component_map` | Component map (what connects to what) | N03 | `component_map-builder` |
| `decision_record` | ADR: contexto, decisao, consequencias | N03 | `decision_record-builder` |
| `diagram` | Architecture diagram (ASCII or Mermaid) | N03 | `diagram-builder` |
| `dual_loop_architecture` | Outer/inner loop agent control architecture | N03 | `dual_loop_architecture-builder` |
| `fhir_agent_capability` | HL7 FHIR R5 AI agent capability declaration: SMART on FHIR scopes, PHI | N03 | `fhir_agent_capability-builder` |
| `invariant` | Lei operacional (inviolavel) | N03 | `invariant-builder` |
| `naming_rule` | Naming rule | N03 | `naming_rule-builder` |
| `pattern` | Pattern reutilizavel (ex: continuous batching) | N03 | `pattern-builder` |
| `supervisor` | Crew orchestrator that composes and coordinates multiple builders | N03 | `supervisor-builder` |

## Usage
```python
# Build any of these via 8F:
python _tools/cex_8f_runner.py "your intent" --kind {kind} --execute
```

## CoC Hierarchy Note
These 12 kinds follow the convention-over-configuration hierarchy: each instance
(N01-N07) inherits this schema and fills the variables for its sin lens.
N00_genesis holds the canonical archetype; nuclei hold the instantiated versions.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_intent_resolution_map]] | sibling | 0.40 |
| [[bld_architecture_kind]] | related | 0.40 |
| [[bld_collaboration_kind]] | downstream | 0.37 |
| [[kind-builder]] | related | 0.37 |
| [[p02_nd_n03.md]] | upstream | 0.36 |
| [[p12_dr_software_project]] | downstream | 0.34 |
| [[p12_dr_builder_nucleus]] | downstream | 0.33 |
| [[agent_card_n03]] | upstream | 0.32 |
| [[p02_agent_creation_nucleus]] | upstream | 0.32 |
| [[bld_collaboration_builder]] | downstream | 0.30 |
