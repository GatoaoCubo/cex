---
id: p01_kc_batch_config
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P09
title: "batch_config: Asynchronous Batch API Configuration"
version: 1.0.0
created: 2026-04-12
updated: 2026-04-12
author: n03_builder
domain: batch_config
quality: 9.1
tags: [batch_config, p09, CALL, kind-kc]
tldr: "Configures API-level asynchronous batch processing -- input format, completion window, polling, cost discount"
when_to_use: "Building, reviewing, or reasoning about batch_config artifacts"
keywords: [batch, async, bulk-inference, cost-optimization, API-batch]
feeds_kinds: [batch_config]
density_score: null
related:
  - bld_instruction_batch_config
  - bld_knowledge_card_batch_config
  - bld_examples_batch_config
  - bld_architecture_batch_config
  - batch-config-builder
  - bld_schema_batch_config
  - bld_config_batch_config
  - bld_output_template_batch_config
  - p03_sp_batch_config_builder
  - bld_tools_batch_config
---

# Batch Config

## Spec
```yaml
kind: batch_config
pillar: P09
llm_function: CALL
max_bytes: 1024
naming: p09_batch_{{provider}}_{{purpose}}.yaml
core: false
```

## What It Is
A batch_config defines how to submit and manage asynchronous bulk inference jobs via provider batch APIs. It specifies input file format, endpoint, completion window, polling interval, metadata, and expected cost discount. It is NOT a schedule (P12, which is cron-based recurring execution) nor a rate_limit_config (P09, which governs per-request throttling). The batch_config governs the API-LEVEL async batch submission pattern -- fire-and-forget with polling.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| OpenAI Batch API | `POST /batches` | JSONL input, 24h window, 50% discount, 50K requests/batch |
| Anthropic Message Batches | `POST /messages/batches` | JSONL, 24h window, async polling via batch_id |
| Google Vertex AI | `BatchPredictionJob` | GCS input/output, auto-scaling, per-model quotas |
| AWS Bedrock | `CreateModelInvocationJob` | S3 input/output, async, pay-per-token |
| Azure OpenAI | Global Batch Deployment | Same as OpenAI but within Azure subscription |
| LiteLLM | `batch_completion()` | Unified wrapper; routes to provider-specific batch APIs |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| provider | string | required | Determines API format and discount structure |
| input_format | enum(jsonl/csv) | jsonl | JSONL is universal; CSV only for simple completions |
| endpoint | string | /chat/completions | Must match provider's batch-eligible endpoints |
| completion_window | string | 24h | Shorter = higher priority but less discount |
| polling_interval | int (seconds) | 300 | Too frequent = rate limited; too slow = delayed results |
| max_requests | int | 50000 | Provider caps: OpenAI 50K/batch, Anthropic 10K/batch |
| cost_discount | float | 0.50 | OpenAI 50%, Anthropic ~50%, varies by provider |
| metadata | map | {} | Custom tags for tracking (project, team, experiment) |
| output_path | string | required | Where to write completed results |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Nightly eval sweep | Large eval dataset, no time pressure | 10K test cases via OpenAI batch, poll next morning |
| Bulk embedding | Re-index entire corpus | Batch embed 100K docs, 50% cost savings |
| A/B prompt comparison | Compare N prompt variants across dataset | Submit N batches, compare outputs |
| Migration validation | Verify model swap doesn't regress | Batch old+new model, diff outputs |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Polling every 10 seconds | Rate-limited by provider, wastes API calls | Use 300s+ intervals; exponential backoff |
| No idempotency key | Retry creates duplicate batches | Include `custom_id` per request in JSONL |
| Ignoring partial failures | Silent data loss on failed rows | Parse `error_file_id`, retry failed rows only |
| Batch for real-time needs | 24h window is not real-time | Use streaming API for latency-sensitive work |

## Integration Graph
```
[eval_dataset / input data] --> [batch_config] --> [output results]
                                     |
                              [rate_limit_config]
                                     |
                              [schedule (optional cron trigger)]
```

## Decision Tree
- IF < 100 requests THEN direct API calls (batch overhead not justified)
- IF 100-50K requests AND time-flexible THEN batch API (50% savings)
- IF > 50K requests THEN split into multiple batches with orchestration
- IF real-time needed THEN skip batch, use streaming/sync API
- DEFAULT: OpenAI batch, JSONL, 24h window, 300s polling

## Quality Criteria
- GOOD: Provider + input format + endpoint + completion window specified
- GREAT: Polling with backoff; error handling for partial failures; cost estimate
- FAIL: No polling strategy; no error handling; using batch for real-time needs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_batch_config]] | upstream | 0.56 |
| [[bld_knowledge_card_batch_config]] | sibling | 0.55 |
| [[bld_examples_batch_config]] | upstream | 0.54 |
| [[bld_architecture_batch_config]] | upstream | 0.50 |
| [[batch-config-builder]] | related | 0.50 |
| [[bld_schema_batch_config]] | upstream | 0.48 |
| [[bld_config_batch_config]] | related | 0.48 |
| [[bld_output_template_batch_config]] | upstream | 0.47 |
| [[p03_sp_batch_config_builder]] | upstream | 0.45 |
| [[bld_tools_batch_config]] | upstream | 0.45 |
