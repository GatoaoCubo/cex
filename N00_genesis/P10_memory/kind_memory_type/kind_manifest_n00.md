---
id: n00_memory_type_manifest
kind: knowledge_card
8f: F3_inject
pillar: P10
nucleus: n00
title: "Memory Type -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, memory_type, p10, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_memory_type
  - bld_collaboration_memory_type
  - bld_schema_reranker_config
  - bld_schema_memory_benchmark
  - bld_manifest_memory_type
  - bld_schema_sandbox_spec
  - bld_schema_memory_scope
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_sandbox_config
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A memory_type defines a classification for a category of persistent memory, specifying its source, confidence decay rate, and retrieval priority. It is the taxonomy entry that allows the memory system to treat different classes of remembered knowledge (corrections, preferences, conventions, context) with appropriate freshness and trust rules.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `memory_type` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| type_name | enum | yes | correction \| preference \| convention \| context |
| source | string | yes | Where this memory class originates (user/system/inference) |
| decay_rate | float | yes | Confidence decay per 30-day period (0.0 = permanent) |
| retrieval_priority | integer | yes | Injection priority (1=highest) relative to other types |
| max_entries | integer | no | Maximum entries of this type kept in active memory |
| validation_required | boolean | yes | Whether entries need human confirmation before trust |

## When to use
- When configuring a new nucleus's memory taxonomy
- When tuning how aggressively corrections override conventions
- When auditing why certain memory entries are overriding others unexpectedly

## Builder
`archetypes/builders/memory_type-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind memory_type --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: mt_correction_type
kind: memory_type
pillar: P10
nucleus: n00
title: "Example Memory Type"
version: 1.0
quality: null
---
# Correction Memory Type
type_name: correction
source: user
decay_rate: 0.0
retrieval_priority: 1
validation_required: false
```

## Related kinds
- `memory_architecture` (P10) -- architecture that organizes memory types into a system
- `consolidation_policy` (P10) -- lifecycle rules that apply per memory type
- `entity_memory` (P10) -- concrete memory entries classified by memory type

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_memory_type]] | related | 0.53 |
| [[bld_collaboration_memory_type]] | downstream | 0.43 |
| [[bld_schema_reranker_config]] | upstream | 0.41 |
| [[bld_schema_memory_benchmark]] | upstream | 0.40 |
| [[bld_manifest_memory_type]] | upstream | 0.40 |
| [[bld_schema_sandbox_spec]] | upstream | 0.40 |
| [[bld_schema_memory_scope]] | upstream | 0.40 |
| [[bld_schema_dataset_card]] | upstream | 0.39 |
| [[bld_schema_usage_report]] | upstream | 0.39 |
| [[bld_schema_sandbox_config]] | upstream | 0.39 |
