---
kind: instruction
id: bld_instruction_batch_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for batch_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Batch Config"
version: "1.0.0"
author: n03_builder
tags: [batch_config, builder, instruction, P09]
tldr: "3-phase build process for batch_config: research provider+model, compose 5 required sections, validate gates."
domain: "batch config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

# Instructions: How to Produce a batch_config

## Phase 1: RESEARCH

1. Identify the provider: OpenAI Batch API, Anthropic Message Batches, Azure OpenAI, or custom.
2. Confirm the model supports batch mode -- not all models are batch-eligible (e.g., OpenAI gpt-4o supports batch; o1 does not; Anthropic claude-3-5-sonnet-20241022 supports Message Batches).
3. Determine the endpoint path: `/v1/chat/completions` (OpenAI), `/v1/messages` (Anthropic), or provider-specific.
4. Establish batch sizing: how many requests per batch submission? What is the provider's max (OpenAI: 50,000 requests or 200MB per batch file).
5. Define the completion window: OpenAI offers 24h; Anthropic processes within minutes to hours. Document the SLA expectation.
6. Determine cost controls: what is the maximum acceptable spend per batch run? Note the discount rate (typically 50% vs sync API).
7. Define retry policy: how many retries on provider error? Exponential or fixed backoff? What is the threshold for declaring a batch failed vs partially succeeded?
8. Confirm input/output format: JSONL is standard. Identify storage location for input file and output file (S3, GCS, local path, or provider-managed storage).
9. Check existing batch_configs via brain_query [IF MCP] for the same provider -- do not duplicate a config already covering this use case.

## Phase 2: COMPOSE

1. Read SCHEMA.md -- source of truth for all fields.
2. Read OUTPUT_TEMPLATE.md -- fill the template following SCHEMA constraints.
3. Fill all required frontmatter fields; set `quality: null` -- never self-score.
4. Write **Overview** section: provider, use case, who triggers the batch, and which env var holds the credential.
5. Write **Job Parameters** section: table with parameter, value, description for provider, model, endpoint, max_requests, completion_window, concurrency.
6. Write **Cost Controls** section: cost_cap_usd, token_budget (if applicable), discount rate vs sync, and monitoring alert threshold.
7. Write **Retry and Error Policy** section: max_retries, backoff strategy (exponential recommended), per-request vs whole-batch retry behavior, dead-letter handling for permanently failed requests.
8. Write **Input/Output Format** section: format type (JSONL), request schema summary, response schema summary, storage path or bucket reference.
9. Confirm body <= 2048 bytes.

## Phase 3: VALIDATE

1. Check QUALITY_GATES.md -- verify each HARD gate manually.
2. Confirm YAML frontmatter parses without errors.
3. Confirm `id` matches `^p09_bc_[a-z][a-z0-9_]+$`.
4. Confirm `provider` is one of: openai, anthropic, azure_openai, custom.
5. Confirm `completion_window` is >= 1h (batch is async; sub-hour = wrong kind).
6. Confirm `cost_cap_usd` is set (financial control gate).
7. Confirm no actual API keys or credentials appear anywhere in the artifact.
8. Confirm `quality` is null.
9. Confirm body <= 2048 bytes.
10. Cross-check: is this a single bulk async request spec? If it has cron timing -- it belongs in `schedule`. If it has multiple dependent steps -- it belongs in `workflow`. If it governs per-request timeouts -- it belongs in `runtime_rule`. This artifact configures a bulk async job, not a pipeline.
11. If score < 8.0: revise in the same pass before outputting.
