---
id: n00_ontology_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Ontology -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, ontology, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_ontology
  - bld_schema_graph_rag_config
  - bld_architecture_ontology
  - bld_collaboration_ontology
  - ontology-builder
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_search_strategy
  - bld_schema_action_paradigm
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Ontology defines a formal taxonomy of concepts, classes, properties, and relationships within a domain. It constrains entity extraction, knowledge graph population, and RAG retrieval by providing a shared schema. Unlike a glossary (informal definitions), an ontology specifies formal logic constraints and class hierarchies that machines can reason over.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `ontology` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Ontology name and domain |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| domain | string | yes | Knowledge domain covered |
| classes | list | yes | Top-level concept classes |
| properties | list | yes | Attributes of classes |
| relationships | list | yes | Inter-class relationships (is_a, has_a, etc.) |
| format | enum | yes | owl\|rdf\|json-ld\|yaml\|custom |

## When to use
- When formalizing a domain's entity taxonomy for GraphRAG
- When enforcing consistent entity types across knowledge extraction
- When building interoperable knowledge systems

## Builder
`archetypes/builders/ontology-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind ontology --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- knowledge engineers, data architects
- `{{DOMAIN_CONTEXT}}` -- formal domain being taxonomized

## Example (minimal)
```yaml
---
id: ontology_cex_artifact_taxonomy
kind: ontology
pillar: P01
nucleus: n04
title: "CEX Artifact Taxonomy Ontology"
version: 1.0
quality: null
---
domain: CEX typed knowledge system
format: yaml
classes: [Artifact, Kind, Pillar, Nucleus, Builder]
properties:
  Artifact: [id, kind, pillar, version, quality]
relationships:
  - Artifact is_produced_by Builder
  - Builder belongs_to Nucleus
```

## Related kinds
- `glossary_entry` (P01) -- informal definitions that seed the ontology
- `knowledge_graph` (P01) -- graph schema derived from ontology
- `graph_rag_config` (P01) -- uses ontology for entity extraction rules

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_ontology]] | downstream | 0.46 |
| [[bld_schema_graph_rag_config]] | downstream | 0.44 |
| [[bld_architecture_ontology]] | downstream | 0.44 |
| [[bld_collaboration_ontology]] | downstream | 0.43 |
| [[ontology-builder]] | related | 0.39 |
| [[bld_schema_dataset_card]] | downstream | 0.39 |
| [[bld_schema_reranker_config]] | downstream | 0.39 |
| [[bld_schema_integration_guide]] | downstream | 0.37 |
| [[bld_schema_search_strategy]] | downstream | 0.37 |
| [[bld_schema_action_paradigm]] | downstream | 0.37 |
