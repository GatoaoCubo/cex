---
id: n00_p06_kind_index
kind: knowledge_card
pillar: P06
nucleus: n00
title: "P06 Schema -- Kind Index"
version: 1.0
quality: 8.9
tags: [index, p06, archetype, n00]
density_score: 1.0
related:
  - bld_architecture_kind
  - kc_intent_resolution_map
  - bld_collaboration_validation_schema
  - bld_collaboration_kind
  - kind-builder
  - p02_nd_n03.md
  - p12_dr_software_project
  - p02_agent_creation_nucleus
  - agent_card_n03
  - p12_dr_builder_nucleus
---

<!-- 8F: F1=knowledge_card P06 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Master index of all 8 kinds in pillar P06. Reference for /mentor, nucleus builders, and the 8F pipeline.

## Pillar: P06 Schema
Data contracts and type definitions: API references, input schemas, validation rules, interface specifications, and enum definitions. The structural layer ensuring agent I/O integrity.

## Kinds in P06

| Kind | Purpose | Primary Nucleus | Builder |
|------|---------|-----------------|---------|
| `api_reference` | API reference doc with endpoints, params, responses, auth, examples | N03 | `api_reference-builder` |
| `edit_format` | LLM-to-host file change format specification | N03 | `edit_format-builder` |
| `enum_def` | Enumeracao reutilizavel | N03 | `enum_def-builder` |
| `input_schema` | Input contract | N03 | `input_schema-builder` |
| `interface` | Agent-to-agent integration contract | N03 | `interface-builder` |
| `type_def` | Custom type definition | N03 | `type_def-builder` |
| `validation_schema` | Post-generation validation contract (system applies, LLM does not see) | N03 | `validation_schema-builder` |
| `validator` | Validation rule (pre-commit, quality gate) | N03 | `validator-builder` |

## Usage
```python
# Build any of these via 8F:
python _tools/cex_8f_runner.py "your intent" --kind {kind} --execute
```

## CoC Hierarchy Note
These 8 kinds follow the convention-over-configuration hierarchy: each instance
(N01-N07) inherits this schema and fills the variables for its sin lens.
N00_genesis holds the canonical archetype; nuclei hold the instantiated versions.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.37 |
| [[kc_intent_resolution_map]] | sibling | 0.37 |
| [[bld_collaboration_validation_schema]] | related | 0.35 |
| [[bld_collaboration_kind]] | downstream | 0.34 |
| [[kind-builder]] | downstream | 0.34 |
| [[p02_nd_n03.md]] | upstream | 0.32 |
| [[p12_dr_software_project]] | downstream | 0.31 |
| [[p02_agent_creation_nucleus]] | upstream | 0.31 |
| [[agent_card_n03]] | upstream | 0.31 |
| [[p12_dr_builder_nucleus]] | downstream | 0.31 |
