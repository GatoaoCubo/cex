---
id: n00_consolidation_policy_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "Consolidation Policy -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, consolidation_policy, p10, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A consolidation_policy defines the memory lifecycle management rules that govern when memories are promoted, archived, merged, or deleted. It specifies freshness thresholds, deduplication strategies, and promotion criteria so the memory system stays lean, accurate, and high-signal over time.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `consolidation_policy` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| scope | enum | yes | session \| nucleus \| global |
| freshness_days | integer | yes | Days before a memory entry is marked stale |
| archive_after_days | integer | yes | Days before stale entries are archived |
| delete_after_days | integer | no | Days before archived entries are deleted |
| dedup_strategy | enum | yes | exact \| semantic \| none |
| promote_threshold | float | no | Quality score required to promote to long-term |

## When to use
- When configuring how the CEX memory system ages and prunes stored knowledge
- When setting up a new nucleus with specific memory retention requirements
- When the memory store has grown stale and needs a cleanup policy applied

## Builder
`archetypes/builders/consolidation_policy-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind consolidation_policy --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cp_global_default
kind: consolidation_policy
pillar: P10
nucleus: n07
title: "Example Consolidation Policy"
version: 1.0
quality: null
---
# Memory Lifecycle Policy
scope: global
freshness_days: 30
archive_after_days: 90
dedup_strategy: semantic
promote_threshold: 8.5
```

## Related kinds
- `memory_type` (P10) -- classification system that consolidation policy applies to
- `lifecycle_rule` (P11) -- broader lifecycle rules that may extend consolidation behavior
- `memory_architecture` (P10) -- system design that this policy governs
