---
kind: knowledge_card
id: bld_knowledge_card_batch_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for batch_config production -- async bulk API job configuration
sources: OpenAI Batch API docs, Anthropic Message Batches docs, AWS SQS batch patterns
quality: 9.2
title: "Knowledge Card Batch Config"
version: "1.0.0"
author: n03_builder
tags: [batch_config, builder, knowledge, async-api, P09]
tldr: "Async batch API: 50% cost reduction vs sync, 24h SLA, JSONL I/O, provider-specific limits. Configure cost cap, retry policy, dead-letter."
domain: "batch config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Domain Knowledge: batch_config

## Executive Summary
Batch configs specify async bulk LLM API job parameters. Both OpenAI Batch API and Anthropic
Message Batches offer ~50% cost reduction vs synchronous APIs by accepting up to 24h latency.
A batch_config is NOT a schedule (cron), NOT a workflow (multi-step), NOT a runtime_rule
(per-request timeout). It is a single bulk async request specification.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P09 (config) |
| llm_function | CALL |
| max_bytes | 2048 (body only) |
| Required frontmatter | provider, model, endpoint, max_requests, completion_window, cost_cap_usd |
| Quality gates | 10 HARD + 10 SOFT |
| Naming | p09_bc_{name_slug}.yaml |
| Input/output format | JSONL (default) |

## Provider Comparison

| Feature | OpenAI Batch API | Anthropic Message Batches |
|---------|-----------------|--------------------------|
| Endpoint | POST /v1/batches | POST /v1/messages/batches |
| Max requests | 50,000 per batch | 10,000 per batch |
| Max file size | 200 MB | N/A |
| Completion SLA | 24h | Best-effort (minutes to hours) |
| Cost discount | ~50% | ~50% |
| Result expiry | None documented | 29 days |
| Eligible models | gpt-4o, gpt-4o-mini, etc. | claude-3-5-sonnet, claude-3-haiku, etc. |
| Result retrieval | Poll /v1/batches/{id} | Poll /v1/messages/batches/{id} |

## Patterns

**Cost control triad**: cost_cap_usd + max_requests + token_budget. All three required.
- cost_cap_usd: total spend ceiling for the job
- max_requests: bounds the file size, preventing submission failures
- token_budget: per-request token limit (input + output) to prevent oversized requests

**JSONL request schema (OpenAI)**:
```
{"custom_id": "req-001", "method": "POST", "url": "/v1/chat/completions",
 "body": {"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "..."}]}}
```

**JSONL request schema (Anthropic)**:
```
{"custom_id": "req-001", "params": {"model": "claude-3-haiku-20240307",
 "max_tokens": 1024, "messages": [{"role": "user", "content": "..."}]}}
```

**Retry policy taxonomy**:
| Error type | Retry? | Strategy |
|-----------|--------|---------|
| 429 rate limit | YES | Exponential backoff |
| 5xx server error | YES | Exponential backoff, max 3 |
| 4xx client error | NO | Dead-letter immediately |
| Timeout (>SLA) | RE-SUBMIT | New batch with unprocessed requests |

**Partial failure handling**: batch jobs commonly complete with 95-99% success.
`partial_failure: continue` processes all requests and collects failures.
`partial_failure: halt` is appropriate only when strict consistency is required.

## P09 Boundary Table

| batch_config IS | batch_config IS NOT |
|----------------|---------------------|
| Async bulk API job spec for LLM inference | schedule (P09) -- cron timing for when to run |
| Single bulk request with JSONL I/O | workflow (P12) -- multi-step dependent pipeline |
| Cost and rate controls for batch submission | runtime_rule (P09) -- per-request sync timeouts |
| Provider-specific params (model, endpoint, SLA) | env_config (P09) -- generic env variables |
| Retry and dead-letter for failed batch requests | feature_flag (P09) -- on/off logical toggle |

## Application
1. Select provider and confirm model is batch-eligible
2. Set max_requests <= provider limit; set cost_cap_usd
3. Set completion_window matching provider SLA
4. Define retry policy with partial_failure behavior
5. Specify dead_letter storage for permanently failed requests
6. Reference credential env var; never embed actual key

## References
- platform.openai.com/docs/guides/batch: OpenAI Batch API guide
- docs.anthropic.com/en/docs/build-with-claude/message-batches: Anthropic Message Batches
- aws.amazon.com/sqs/: SQS patterns for queue-based batch processing
