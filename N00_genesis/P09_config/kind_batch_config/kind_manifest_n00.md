---
id: n00_batch_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Batch Config -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, batch_config, p09, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A batch_config defines the parameters for asynchronous bulk API operations: concurrency limits, request batching strategies, retry policies, and output handling for large-scale processing jobs. It enables nuclei to process thousands of items (documents, embeddings, evaluations) without exceeding rate limits or overwhelming downstream services.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `batch_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| batch_size | integer | yes | Number of items per batch |
| max_concurrent_batches | integer | yes | Parallel batch workers |
| retry_attempts | integer | yes | Per-item retry limit on failure |
| retry_delay_ms | integer | no | Base delay between retries (exponential backoff) |
| timeout_per_item_ms | integer | no | Per-item processing timeout |
| output_format | enum | no | jsonl \| csv \| parquet \| ndjson |
| checkpoint_interval | integer | no | Save progress every N items |
| provider | string | no | API provider this config targets |

## When to use
- Processing large document corpora for embedding or indexing
- Running bulk LLM evaluations on test suites
- Executing Anthropic Batch API jobs for cost-optimized overnight workloads

## Builder
`archetypes/builders/batch_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind batch_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: batch_config_embedding_pipeline
kind: batch_config
pillar: P09
nucleus: n04
title: "Embedding Pipeline Batch Config"
version: 1.0
quality: null
---
batch_size: 100
max_concurrent_batches: 4
retry_attempts: 3
retry_delay_ms: 1000
output_format: jsonl
checkpoint_interval: 500
```

## Related kinds
- `rate_limit_config` (P09) -- governs API rate limits that batch_config must respect
- `cost_budget` (P09) -- tracks spend incurred by batch operations
- `experiment_config` (P09) -- batch processing is often used for A/B experiment runs
