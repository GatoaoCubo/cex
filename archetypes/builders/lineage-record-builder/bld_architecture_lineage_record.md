---
id: bld_architecture_lineage_record
kind: knowledge_card
pillar: P08
title: "Architecture: lineage_record Relationships"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: lineage_record
quality: 7.0
tags: [architecture, lineage_record, P01]
llm_function: CONSTRAIN
tldr: "How lineage_record relates to knowledge_card, citation, audit_log, and learning_record."
density_score: null
---

# Architecture: lineage_record

## Relationship Graph
```
[rag_source] --> [ingestion activity] --> [knowledge_card]
[knowledge_card] -----------------------> [lineage_record]
[lineage_record] --> [citation] (source refs extracted)
[lineage_record] --> [audit_log] (compliance copy, optional)
```

## Kind Boundaries
| Kind | Relationship | Boundary |
|------|-------------|---------|
| knowledge_card | TARGET | lineage_record documents the provenance of knowledge_card artifacts |
| citation | CHILD | citation is a single source reference; lineage_record is the full derivation chain |
| audit_log | SIBLING | audit_log is compliance-driven event sequence; lineage_record is knowledge provenance |
| learning_record | SIBLING | learning_record captures session learnings; lineage_record captures artifact derivation |
| rag_source | UPSTREAM | rag_source is often the first entity in a lineage chain |
| entity_memory | SIBLING | entity_memory stores facts about entities; lineage_record stores how artifacts were made |

## PROV-O Mapping
| PROV-O Class | CEX Analog |
|-------------|-----------|
| prov:Entity | knowledge artifact, rag_source, document |
| prov:Activity | ingestion, synthesis, distillation, validation |
| prov:Agent | nucleus (N01-N07), tool, human |
| prov:wasGeneratedBy | artifact F8 PRODUCE step |
| prov:wasDerivedFrom | artifact inherits from prior artifact |
| prov:wasAttributedTo | nucleus N-x produced this |
