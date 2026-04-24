---
id: p09_rtp_nucleus_dispatch
kind: retry_policy
8f: F8_collaborate
pillar: P09
version: "1.0.0"
created: "2026-04-19"
updated: "2026-04-19"
author: "n05_operations"
operation: "nucleus_dispatch"
max_attempts: 3
initial_interval: 5000
backoff_strategy: "exponential"
backoff_multiplier: 2.0
max_interval: 60000
jitter: "FULL"
retry_budget: 3
retryable_errors: [HTTP_429, HTTP_503, HTTP_504, ConnectionError, TimeoutError, ProcessSpawnFailure]
non_retryable_errors: [HTTP_400, HTTP_401, HTTP_403, InvalidNucleus, MissingHandoff, ConfigParseError]
quality: 8.2
tags: [retry_policy, nucleus_dispatch, operations, dispatch]
tldr: "Nucleus dispatch retry: 3 attempts, exponential 5000ms->60000ms, FULL jitter, retries 429/503/spawn failures."
related:
  - bld_examples_runtime_rule
  - p01_kc_api_rate_limiting_retry_patterns
  - p01_kc_error_recovery
  - p01_kc_runtime_rule
  - bld_memory_runtime_rule
  - bld_knowledge_card_client
  - bld_knowledge_card_output_validator
  - p01_kc_self_healing
  - p04_webhook_NAME
  - p10_lr_client_builder
density_score: 1.0
---

## Retry Behavior

| Parameter | Value | Notes |
|-----------|-------|-------|
| max_attempts | 3 | 1 initial + 2 retries; matches rate_limits.yaml recovery.on_429.max_retries |
| initial_interval | 5000ms | Matches rate_limits.yaml recovery.on_429.initial_delay (converted from 60s to 5s for dispatch-level retry; API-level uses 60s) |
| backoff_strategy | exponential | Standard for API rate limit recovery per AWS architecture best practices |
| backoff_multiplier | 2.0 | 5s -> 10s -> 20s base delays |
| max_interval | 60000ms | Cap at 1 minute; aligns with rate_limits.yaml recovery.on_429.initial_delay |
| jitter | FULL | Prevents thundering herd when multiple nuclei retry simultaneously after grid 429 |
| retry_budget | 3 | Max 3 concurrent retry attempts across all dispatch operations in a session |

## Backoff Calculation

| Attempt | Base Delay | With FULL Jitter | Notes |
|---------|------------|-------------------|-------|
| 1 | 5000ms | 0-5000ms | After first dispatch failure (e.g., 429 from Claude API) |
| 2 | 10000ms | 0-10000ms | Exponential: 5000 * 2^1 |
| 3 | 20000ms | 0-20000ms | Exponential: 5000 * 2^2; capped below max_interval |

FULL jitter formula: `sleep = random(0, base_delay)` per AWS "Exponential Backoff and Jitter" (2015).

## Error Classification

| Error | Action | Reason |
|-------|--------|--------|
| HTTP_429 | RETRY | API rate limit; transient by definition. Empirical: 4/32 sessions hit 429 at safe_concurrent=32 (rate_limits.yaml) |
| HTTP_503 | RETRY | Service temporarily unavailable; upstream provider capacity |
| HTTP_504 | RETRY | Gateway timeout; network-level transient |
| ConnectionError | RETRY | TCP connection refused or reset; process may not have started yet |
| TimeoutError | RETRY | Spawn timeout; nucleus boot can take 10-30s on cold start |
| ProcessSpawnFailure | RETRY | Start-Process or dispatch.sh returned non-zero; transient OS resource contention |
| HTTP_400 | FAIL IMMEDIATELY | Malformed request; retrying sends the same bad payload |
| HTTP_401 | FAIL IMMEDIATELY | Authentication failure; API key invalid or expired |
| HTTP_403 | FAIL IMMEDIATELY | Authorization denied; subscription tier insufficient |
| InvalidNucleus | FAIL IMMEDIATELY | Nucleus ID not in N01-N07 range; structural error in handoff |
| MissingHandoff | FAIL IMMEDIATELY | Handoff file not found at .cex/runtime/handoffs/; must be written before dispatch |
| ConfigParseError | FAIL IMMEDIATELY | nucleus_models.yaml or boot config unparseable; fix config before retry |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_runtime_rule]] | upstream | 0.40 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | upstream | 0.35 |
| [[p01_kc_error_recovery]] | upstream | 0.32 |
| [[p01_kc_runtime_rule]] | related | 0.31 |
| [[bld_memory_runtime_rule]] | downstream | 0.25 |
| [[bld_knowledge_card_client]] | upstream | 0.25 |
| [[bld_knowledge_card_output_validator]] | upstream | 0.20 |
| [[p01_kc_self_healing]] | upstream | 0.20 |
| [[p04_webhook_NAME]] | upstream | 0.20 |
| [[p10_lr_client_builder]] | downstream | 0.20 |
