---
id: n00_memory_benchmark_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Memory Benchmark -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, memory_benchmark, p07, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Memory benchmark defines an evaluation suite for assessing the quality of a CEX memory system across dimensions including retrieval precision, recall, freshness accuracy, decay correctness, and cross-session persistence. It tests entity memory, knowledge index, and memory summary kinds under realistic workloads. Results guide memory architecture decisions and identify decay or retrieval regressions.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `memory_benchmark` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Memory system name + "Benchmark" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| memory_kinds_tested | list | yes | CEX memory kinds under evaluation |
| test_scenarios | list | yes | Named test scenarios (insert, retrieve, decay, prune) |
| retrieval_metrics | list | yes | Precision, recall, MRR, NDCG metrics |
| decay_test_window_days | int | yes | Days simulated for decay function validation |
| persistence_test_sessions | int | yes | Number of sessions tested for cross-session recall |

## When to use
- Validating a new memory backend or indexing strategy before deployment
- Detecting regressions in retrieval quality after a memory system change
- Selecting between competing memory architectures (vector DB, keyword, hybrid)

## Builder
`archetypes/builders/memory_benchmark-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind memory_benchmark --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N04 knowledge designs; N05 operations runs the harness
- `{{SIN_LENS}}` -- Knowledge Gluttony: no memory regression left undetected
- `{{TARGET_AUDIENCE}}` -- N04 knowledge engineers selecting or upgrading memory systems
- `{{DOMAIN_CONTEXT}}` -- memory backend, corpus size, retrieval latency requirements

## Example (minimal)
```yaml
---
id: memory_benchmark_cex_entity_memory
kind: memory_benchmark
pillar: P07
nucleus: n04
title: "CEX Entity Memory System Benchmark"
version: 1.0
quality: null
---
memory_kinds_tested: [entity_memory, knowledge_index, memory_summary]
retrieval_metrics: [precision_at_5, recall_at_10, mrr]
decay_test_window_days: 90
persistence_test_sessions: 10
```

## Related kinds
- `benchmark` (P07) -- generic benchmark; memory_benchmark specializes for memory systems
- `knowledge_index` (P10) -- the artifact being benchmarked
- `regression_check` (P07) -- tracks memory benchmark results over time
