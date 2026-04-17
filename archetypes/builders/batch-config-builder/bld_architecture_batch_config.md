---
kind: architecture
id: bld_architecture_batch_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of batch_config -- inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Batch Config"
version: "1.0.0"
author: n03_builder
tags: [batch_config, builder, architecture, P09]
tldr: "batch_config component map: provider params, cost controls, retry policy, I/O format. Feeds workflow and is triggered by schedule."
domain: "batch config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---
# Architecture: batch_config

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| provider | API provider for batch inference (openai, anthropic, azure_openai, custom) | batch-config-builder | required |
| model | Model ID to use for all requests in this batch job | batch-config-builder | required |
| endpoint | API endpoint path for batch submission | batch-config-builder | required |
| max_requests | Maximum requests per batch file; bounds file size and spend | batch-config-builder | required |
| completion_window | Provider SLA for batch completion (e.g., 24h) | batch-config-builder | required |
| cost_cap_usd | Maximum spend allowed per batch run | batch-config-builder | required |
| concurrency | Max in-flight requests at one time | batch-config-builder | required |
| retry_policy | max_retries, backoff strategy, partial_failure behavior | batch-config-builder | required |
| dead_letter | Storage path for permanently failed requests | batch-config-builder | required |
| input_format | Format of batch input file (JSONL standard) | batch-config-builder | required |
| output_format | Format of batch output file (JSONL standard) | batch-config-builder | required |
| credential_env_var | Name of env var holding provider API key | batch-config-builder | required |
| metadata | id, kind, pillar, version, created, author, tags | batch-config-builder | required |

## Dependency Graph

```
schedule (P09) --triggers--> batch_config (cron schedule fires batch job submission)
batch_config --submitted_to--> provider_api (OpenAI /v1/batches, Anthropic /v1/messages/batches)
batch_config --reads_from--> env_config (P09) (API key, storage credentials)
batch_config --writes_to--> output_storage (S3, GCS, or provider-managed)
batch_config --on_failure--> dead_letter_store (failed requests routed here)
workflow (P12) --orchestrates--> batch_config (batch is one step in multi-step pipeline)
guardrail (P11) --constrains--> batch_config (cost cap and rate limit enforcement)
runtime_rule (P09) --independent-- batch_config (runtime_rule governs sync per-request timeouts)
feature_flag (P09) --independent-- batch_config (feature_flag is on/off toggle, not job config)
```

| From | To | Type | Data |
|------|----|------|------|
| schedule | batch_config | triggers | Cron timing causes batch job submission |
| env_config | batch_config | feeds | API key env var, storage credential env var |
| batch_config | provider_api | submitted_to | JSONL input file + job parameters |
| provider_api | batch_config | returns | JSONL output file via polling or webhook |
| batch_config | dead_letter_store | writes_on_failure | Failed request records for reprocessing |
| workflow | batch_config | orchestrates | Batch job as a step in a larger pipeline |
| guardrail | batch_config | constrains | Cost cap and concurrency limits |

## Boundary Table

| batch_config IS | batch_config IS NOT |
|----------------|---------------------|
| Async bulk API job specification | schedule (P09) -- cron timing is when, not how |
| Single bulk JSONL request with job-level controls | workflow (P12) -- workflow chains multiple steps |
| Provider, model, endpoint, cost, retry specification | runtime_rule (P09) -- sync per-request timeout rules |
| Configuration consumed by batch submission code | env_config (P09) -- generic env variable catalog |
| Financial and rate control for bulk operations | feature_flag (P09) -- on/off logical toggle |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Safety | guardrail, cost_cap_usd, dead_letter | Bound financial exposure; route failures safely |
| Execution | provider, model, endpoint, concurrency | Job routing and throughput control |
| Data | input_format, output_format, storage paths | I/O contract for batch submission and result retrieval |
| Policy | retry_policy, completion_window | Recovery behavior and SLA contract |
| Identity | metadata, credential_env_var | Artifact traceability and credential hygiene |
