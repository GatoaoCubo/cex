---
kind: config
id: bld_config_batch_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: low
max_turns: 20
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Batch Config"
version: "1.0.0"
author: n03_builder
tags: [batch_config, builder, config, P09]
tldr: "Naming, paths, size limits, and operational rules for batch_config production."
domain: "batch config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Config: batch_config Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_bc_{name_slug}.yaml` | `p09_bc_doc_classifier.yaml` |
| Builder directory | kebab-case | `batch-config-builder/` |
| Frontmatter fields | snake_case | `cost_cap_usd`, `completion_window` |
| Name slug | snake_case, lowercase, no hyphens | `doc_classifier`, `eval_pipeline`, `bulk_embed` |
| Provider enum | lowercase, underscores for azure | `openai`, `anthropic`, `azure_openai`, `custom` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
1. Output: `P09_config/examples/p09_bc_{name_slug}.md`
2. Compiled: `P09_config/compiled/p09_bc_{name_slug}.yaml`

## Size Limits (aligned with SCHEMA)
1. Body: max 2048 bytes (strict -- batch configs are concise)
2. Total (frontmatter + body): ~3200 bytes
3. Density: >= 0.85 (no filler; tables over prose)

## Provider Enum

| Value | Provider | Batch Endpoint |
|-------|----------|---------------|
| openai | OpenAI Batch API | POST /v1/batches |
| anthropic | Anthropic Message Batches | POST /v1/messages/batches |
| azure_openai | Azure OpenAI Batch | REST endpoint (config-specific) |
| custom | Custom batch provider | Specified in endpoint field |

## Completion Window Constraints

| Value | Valid? | Notes |
|-------|--------|-------|
| 24h | YES | OpenAI standard SLA |
| 12h | YES | Custom / Azure OpenAI |
| 1h | MINIMUM | Below 1h = use runtime_rule (sync) instead |
| 30m | NO | Below minimum threshold -- wrong kind |
| 5m | NO | This is not a batch job, use sync API |

## Cost Cap Guidance

| Batch Size | Suggested cost_cap_usd |
|-----------|----------------------|
| < 1,000 requests | $5.00 |
| 1,000 - 10,000 requests | $20.00 - $50.00 |
| 10,000 - 50,000 requests | $50.00 - $200.00 |
| > 50,000 requests | Split into multiple batches |

## Metadata

```yaml
id: bld_config_batch_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-batch-config.md
```
