---
id: n00_compression_config_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "Compression Config -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, compression_config, p10, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_compression_config
  - bld_schema_reranker_config
  - bld_schema_search_strategy
  - bld_architecture_compression_config
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_multimodal_prompt
  - bld_collaboration_compression_config
  - bld_schema_sandbox_spec
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A compression_config defines how tool outputs and context windows are compressed before being passed into subsequent LLM calls. It specifies the compression strategy (truncation, summarization, extraction), triggers, and quality thresholds that control when and how context is reduced to fit within model limits.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `compression_config` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| strategy | enum | yes | truncation \| summarization \| extraction \| hybrid |
| trigger_tokens | integer | yes | Token threshold that triggers compression |
| target_tokens | integer | yes | Target token count after compression |
| preserve_fields | array | no | Fields/sections that must never be truncated |
| summary_model | string | no | Model to use for summarization strategy |
| quality_floor | float | no | Minimum quality score before compression aborts |

## When to use
- When tool outputs regularly exceed context budget and need automatic reduction
- When building multi-turn agents that must compress conversation history
- When configuring memory compaction after session /compact events

## Builder
`archetypes/builders/compression_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind compression_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cc_n07_session_default
kind: compression_config
pillar: P10
nucleus: n07
title: "Example Compression Config"
version: 1.0
quality: null
---
# Compression Configuration
strategy: summarization
trigger_tokens: 150000
target_tokens: 50000
preserve_fields: [frontmatter, decisions, signals]
```

## Related kinds
- `memory_summary` (P10) -- the output artifact produced by compression
- `context_window_config` (P03) -- defines the budget this config compresses against
- `consolidation_policy` (P10) -- governs the broader lifecycle compression fits within

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_compression_config]] | upstream | 0.48 |
| [[bld_schema_reranker_config]] | upstream | 0.42 |
| [[bld_schema_search_strategy]] | upstream | 0.42 |
| [[bld_architecture_compression_config]] | upstream | 0.40 |
| [[bld_schema_usage_report]] | upstream | 0.39 |
| [[bld_schema_benchmark_suite]] | upstream | 0.39 |
| [[bld_schema_integration_guide]] | upstream | 0.39 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.39 |
| [[bld_collaboration_compression_config]] | downstream | 0.39 |
| [[bld_schema_sandbox_spec]] | upstream | 0.39 |
