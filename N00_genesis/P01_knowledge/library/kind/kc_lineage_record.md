---
quality: null
id: kc_lineage_record
kind: knowledge_card
title: "Lineage Record: Artifact Provenance Chain via W3C PROV-O"
tldr: "Documents the derivation chain of knowledge artifacts using W3C PROV-O ontology with entities, activities, and agents"
version: 1.1.0
pillar: P01
nucleus: n00
domain: kind-taxonomy
tags: [kind, taxonomy, lineage_record, P01, knowledge, provenance]
density_score: 0.93
updated: "2026-04-22"
related:
  - bld_collaboration_entity_memory
  - entity-memory-builder
  - citation-builder
  - p06_arch_knowledge_graph
  - p01_kc_entity_memory
  - bld_architecture_citation
  - bld_collaboration_citation
  - bld_schema_entity_memory
  - p01_kc_rag_source
  - bld_knowledge_card_entity_memory
---

# lineage_record

## Spec
```yaml
kind: lineage_record
pillar: P01
llm_function: INJECT
max_bytes: 3072
naming: p01_lr_{{name}}.md + .yaml
core: false
```

## What It Is
A lineage_record documents the provenance chain of a knowledge artifact: what sources it was derived from, what transformation activities occurred, and which agents (nuclei, tools, humans) were responsible. Based on the W3C PROV-O standard (PROV Ontology).

It is NOT:
- `audit_log` (compliance event sequence -- records who did what for regulatory purposes; no provenance semantics)
- `citation` (in-text source reference -- a single bibliographic entry; not a full derivation chain)
- `learning_record` (session learning capture -- records what was learned, not how an artifact was made)

## When to Use
- After synthesizing a knowledge_card from multiple rag_sources
- After a large knowledge import wave (FRACTAL_FILL)
- When an artifact is derived from prior artifacts in a chain
- For reproducibility: anyone should be able to re-derive the artifact from the lineage
- For compliance or audit requirements on knowledge provenance

## When NOT to Use
- Recording compliance events -> use `audit_log`
- Adding a citation in a document -> use `citation`
- Capturing session learnings -> use `learning_record`
- Tracking entity facts -> use `entity_memory`

## Structure
```yaml
# Required frontmatter fields
id: p01_lr_{name_slug}
kind: lineage_record
pillar: P01
target_artifact: "artifact-id-whose-provenance-is-recorded"
sources_count: N
activities_count: N
derivation_type: wasDerivedFrom | wasGeneratedBy | wasQuotedFrom | wasRevisionOf
quality: null
```

```markdown
## Entities
Table: id, type, location/URL, retrieval_timestamp (ISO 8601)

## Activities
Table: id, label, used (entity ids), generated (entity id), agent, timestamp

## Agents
Table: id, type (nucleus|tool|human), role

## Derivation Relations
PROV-O triples: target wasGeneratedBy activity, target wasDerivedFrom source, etc.
```

## PROV-O Core Vocabulary
| Term | Meaning in CEX |
|------|---------------|
| prov:Entity | knowledge artifact, rag_source, raw document, dataset |
| prov:Activity | ingestion, synthesis, distillation, validation, annotation |
| prov:Agent | nucleus (N01-N07), tool, human curator |
| wasDerivedFrom(E2, E1) | knowledge_card built from rag_source |
| wasGeneratedBy(E, A) | artifact produced by synthesis activity |
| wasAttributedTo(E, Ag) | artifact attributed to N04 |
| used(A, E) | activity consumed a source entity |

## Derivation Types
| Type | When |
|------|------|
| wasDerivedFrom | Target built directly from source |
| wasGeneratedBy | Target is output of a specific activity |
| wasQuotedFrom | Target contains verbatim content |
| wasRevisionOf | Target is an update of a prior artifact |

## Relationships
```
[rag_source] --> [ingestion activity] --> [knowledge_card]
[knowledge_card] --> [lineage_record] (provenance of the KC)
[lineage_record] -- cites --> [citation] (extracted source refs)
[audit_log] -- compliance copy of --> [lineage_record] (optional)
```

## Decision Tree
- IF synthesizing KC from multiple sources -> create lineage_record immediately
- IF source is unknown -> use entity type: unknown; note "provenance unavailable"
- IF artifact is revised -> use wasRevisionOf derivation type
- IF tool generated artifact -> agent type: tool; include tool id
- DEFAULT: create lineage_record after any FRACTAL_FILL or import wave

## Concrete Provenance Chain Example

The following shows a complete lineage_record for a knowledge_card synthesized from three RAG sources by N04:

```yaml
# p01_lr_kc_react_patterns.md
---
id: p01_lr_kc_react_patterns
kind: lineage_record
pillar: P01
target_artifact: "kc_react_patterns"
sources_count: 3
activities_count: 2
derivation_type: wasDerivedFrom
quality: null
---
```

```markdown
## Entities

| ID | Type | Location | Retrieved |
|----|------|----------|-----------|
| e1 | rag_source | N04_knowledge/P01_knowledge/rag/react_docs_2026.md | 2026-04-10T14:30:00Z |
| e2 | rag_source | N04_knowledge/P01_knowledge/rag/react_patterns_blog.md | 2026-04-10T14:32:00Z |
| e3 | rag_source | N04_knowledge/P01_knowledge/rag/react_perf_guide.md | 2026-04-10T14:35:00Z |
| e4 | knowledge_card | N04_knowledge/P01_knowledge/library/kc_react_patterns.md | 2026-04-10T15:00:00Z |

## Activities

| ID | Label | Used | Generated | Agent | Timestamp |
|----|-------|------|-----------|-------|-----------|
| a1 | ingestion | e1, e2, e3 | - | tool:cex_retriever | 2026-04-10T14:40:00Z |
| a2 | synthesis | e1, e2, e3 | e4 | nucleus:N04 | 2026-04-10T15:00:00Z |

## Agents

| ID | Type | Role |
|----|------|------|
| nucleus:N04 | nucleus | Knowledge synthesis, quality gating |
| tool:cex_retriever | tool | TF-IDF similarity search, source ranking |
| human:gato3 | human | Triggered synthesis via /build intent |

## Derivation Relations (PROV-O triples)
- e4 wasDerivedFrom e1
- e4 wasDerivedFrom e2
- e4 wasDerivedFrom e3
- e4 wasGeneratedBy a2
- e4 wasAttributedTo nucleus:N04
- a2 used e1
- a2 used e2
- a2 used e3
- a1 used e1
- a1 used e2
- a1 used e3
```

## Provenance Chain Visualization

```
[e1: react_docs_2026]     --+
                             |
[e2: react_patterns_blog] --+--> [a1: ingestion] --> [a2: synthesis] --> [e4: kc_react_patterns]
                             |          ^                    ^
[e3: react_perf_guide]    --+          |                    |
                                  tool:cex_retriever    nucleus:N04
                                                            |
                                                     human:gato3 (trigger)
```

## Industry Tools for Data Lineage

| Tool | Domain | Lineage Scope | Open Source |
|------|--------|---------------|-------------|
| Apache Atlas | Big Data / Hadoop | Table-level, column-level | Yes |
| OpenLineage | Cross-platform | Job-level, dataset-level | Yes (Linux Foundation) |
| dbt | Analytics engineering | Model-level, column-level | Yes (core) |
| Marquez | Data pipelines | Job-level, dataset-level | Yes (WeWork origin) |
| DataHub | Data catalog | Table, column, pipeline | Yes (LinkedIn origin) |
| Collibra | Enterprise governance | Business glossary, lineage | No (commercial) |

## Quality Criteria
- GOOD: target_artifact set, at least 1 source entity, at least 1 activity, agent identified
- GREAT: PROV-O relations explicit, ISO timestamps on all entities, derivation type correct
- FAIL: No source entity, no activity, sources_count mismatch, no agent

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_entity_memory]] | downstream | 0.27 |
| [[entity-memory-builder]] | downstream | 0.25 |
| [[citation-builder]] | related | 0.23 |
| [[p06_arch_knowledge_graph]] | downstream | 0.22 |
| [[p01_kc_entity_memory]] | sibling | 0.21 |
| [[bld_architecture_citation]] | downstream | 0.21 |
| [[bld_collaboration_citation]] | downstream | 0.20 |
| [[bld_schema_entity_memory]] | downstream | 0.20 |
| [[p01_kc_rag_source]] | sibling | 0.19 |
| [[bld_knowledge_card_entity_memory]] | sibling | 0.19 |
