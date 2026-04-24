---
id: p02_fb_model_cascade
kind: fallback_chain
8f: F8_collaborate
pillar: P02
title: "Model Cascade Fallback Chain"
chain:
  - {model: opus, timeout: 30, max_retries: 1}
  - {model: sonnet, timeout: 15, max_retries: 1}
  - {model: haiku, timeout: 5, max_retries: 2}
timeout_per_step: varies
trigger_conditions: [timeout, rate_limit, 5xx_error, context_overflow]
tags: [fallback, cascade, model, cost-optimization]
tldr: "Model cascade: opus→sonnet→haiku with cost-optimized fallback on timeout, rate limit, or error."
quality: 9.0
domain: "model configuration"
density_score: 0.8
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
version: "1.0.0"
related:
  - p01_kc_fallback_chain
  - bld_examples_fallback_chain
  - bld_collaboration_fallback_chain
  - p02_fb_CHAIN_SLUG
  - p10_lr_fallback_chain_builder
  - fallback-chain-builder
  - bld_instruction_fallback_chain
  - p02_mc_claude_opus_4
  - p01_kc_claude_model_capabilities_2026
  - kc_test_ollama_wrapper
---

# Fallback: Model Cascade

## Chain Logic

```
Request → opus (30s) ──timeout/error──→ sonnet (15s) ──timeout/error──→ haiku (5s)
                 │                            │                            │
                 ▼                            ▼                            ▼
              SUCCESS                     SUCCESS                      SUCCESS
```

**Rule**: Never skip a tier. Escalation is strictly sequential.
**Trigger conditions**: timeout, HTTP 5xx, rate limit (429), context window overflow.

## Cost & Performance Matrix

| Step | Model | Timeout | Input $/1M tok | Output $/1M tok | Relative Cost | Typical Latency |
|------|-------|---------|-----------------|-----------------|---------------|-----------------|
| 1 | opus | 30s | $15.00 | $75.00 | 100% | 8-25s |
| 2 | sonnet | 15s | $3.00 | $15.00 | 20% | 3-10s |
| 3 | haiku | 5s | $0.25 | $1.25 | ~2% | 0.5-3s |

## Trigger Decision Table

| Condition | Action | Metadata Passed |
|-----------|--------|-----------------|
| Response received within timeout | Return response | `model_used`, `latency_ms` |
| Timeout exceeded | Cascade to next tier | `original_model`, `timeout_reason` |
| HTTP 429 (rate limit) | Cascade to next tier | `retry_after`, `rate_limit_tier` |
| HTTP 5xx (server error) | Retry once, then cascade | `error_code`, `retry_count` |
| Context overflow (>200K tokens) | Skip to haiku (smaller context) | `token_count`, `truncated` |
| All tiers exhausted | Return error with full trace | `cascade_trace`, `total_latency` |

## Implementation Pattern

```python
async def cascade_request(prompt: str, chain: list[dict]) -> dict:
    trace = []
    for step in chain:
        model, timeout = step["model"], step["timeout"]
        try:
            response = await llm_call(prompt, model=model, timeout=timeout)
            return {"response": response, "model_used": model, "trace": trace}
        except (TimeoutError, RateLimitError, ServerError) as e:
            trace.append({"model": model, "error": type(e).__name__, "elapsed": e.elapsed})
            continue
    raise CascadeExhaustedError(trace=trace)
```

## Monitoring Metrics

| Metric | Alert Threshold | Dashboard |
|--------|----------------|-----------|
| Cascade rate (% requests falling to tier 2+) | > 15% over 5min | `cex/fallback/cascade_rate` |
| Full exhaustion rate | > 2% over 10min | `cex/fallback/exhaustion_rate` |
| Cost savings vs opus-only | Track weekly | `cex/fallback/cost_savings` |
| P95 latency with cascade | > 45s | `cex/fallback/p95_latency` |

## When to Use

| Scenario | Recommended Chain | Rationale |
|----------|-------------------|-----------|
| Production artifact generation | opus→sonnet→haiku | Quality-first, cost as fallback |
| Interactive chat / low latency | sonnet→haiku | Speed-first, skip opus |
| Batch processing (1000+ items) | haiku only | Cost-first, volume workload |
| Critical reasoning tasks | opus (no fallback) | Quality cannot degrade |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_fallback_chain]] | related | 0.43 |
| [[bld_examples_fallback_chain]] | downstream | 0.34 |
| [[bld_collaboration_fallback_chain]] | downstream | 0.30 |
| [[p02_fb_CHAIN_SLUG]] | sibling | 0.29 |
| [[p10_lr_fallback_chain_builder]] | downstream | 0.29 |
| [[fallback-chain-builder]] | related | 0.28 |
| [[bld_instruction_fallback_chain]] | downstream | 0.28 |
| [[p02_mc_claude_opus_4]] | related | 0.28 |
| [[p01_kc_claude_model_capabilities_2026]] | upstream | 0.27 |
| [[kc_test_ollama_wrapper]] | related | 0.27 |
