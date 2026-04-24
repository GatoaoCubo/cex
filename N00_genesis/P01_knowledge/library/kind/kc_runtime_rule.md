---
id: p01_kc_runtime_rule
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P09
title: "Runtime Rule — Deep Knowledge for runtime_rule"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: runtime_rule
quality: 9.1
tags: [runtime_rule, P09, GOVERN, kind-kc]
tldr: "runtime_rule is a per-operation technical constraint governing timeouts, retry limits, and degradation behavior — scoped to specific operation types rather than provider-level rate limits."
when_to_use: "Building, reviewing, or reasoning about runtime_rule artifacts"
keywords: [timeout, retry_policy, graceful_degradation]
feeds_kinds: [runtime_rule]
density_score: null
related:
  - bld_examples_runtime_rule
  - p01_kc_api_rate_limiting_retry_patterns
  - runtime-rule-builder
  - p01_kc_error_recovery
  - p01_kc_rate_limit_config
  - p01_kc_quality_gate
  - p03_ins_runtime_rule
  - bld_memory_runtime_rule
  - bld_knowledge_card_output_validator
  - bld_knowledge_card_runtime_rule
---

# Runtime Rule

## Spec
```yaml
kind: runtime_rule
pillar: P09
llm_function: GOVERN
max_bytes: 3072
naming: p09_rr_{{rule}}.yaml
core: false
```

## What It Is
A runtime_rule is a technical constraint governing per-operation execution: timeout duration, retry count, retry delay strategy, and on-failure behavior. It is NOT a lifecycle_rule (P11, which governs artifact lifecycle events), NOT a law (P08, which is inviolable system-wide), NOT a rate_limit_config (which governs provider-level RPM/TPM ceilings).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `AgentExecutor` params | `max_iterations`, `handle_parsing_errors`, `timeout` |
| LlamaIndex | `Settings` timeouts + retry | LLM timeout, `retry_on_exception` configuration |
| CrewAI | `Agent`/`Task` params | `max_iter`, `max_retry_limit` on agent |
| DSPy | `LM.generate` with backoff | Retry handled internally with configurable delay |
| Haystack | Component timeout + pipeline retry | Per-component execution limits |
| OpenAI | `Run` params | `max_prompt_tokens`, `max_completion_tokens`, timeout |
| Anthropic | `max_tokens` + request timeout | Per-request limits via API call parameters |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| timeout_s | int | 120 | Lower = faster fail; higher = handles slow LLM calls |
| max_retries | int | 3 | Higher = more resilient; uncapped = runaway retries |
| retry_delay_s | float | 1.0 | Base delay — multiplied by strategy (exponential doubles) |
| on_timeout | enum | skip | skip/fail/fallback — skip keeps agent_group moving; fail is safer |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Retry with backoff | External API calls that may transiently fail | 3 attempts, 1s/2s/4s delays, exponential |
| Hard timeout | Long LLM generation calls | `timeout_s: 300` for complex generation tasks |
| Graceful degradation | Non-critical operations that can be skipped | `on_timeout: skip` — agent_group continues without result |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No timeout | Stalled operations block entire agent_group indefinitely | Always set `timeout_s` — even generous 300s beats infinite |
| Infinite retry | `max_retries: -1` causes runaway token spend | Always cap at 3-5 retries |
| Retry on 400 errors | 400 = bad request; retrying wastes tokens with same result | Only retry 429 (rate limit), 500, 503 (transient) |

## Integration Graph
```
rate_limit_config, permission --> [runtime_rule] --> agent_card, law
                                        |
                                   feature_flag, env_config, path_config
```

## Decision Tree
- IF external API or LLM call THEN `timeout_s` + exponential retry on 429/5xx
- IF LLM generation THEN `timeout_s: 300`, `max_retries: 2`
- IF local file operation THEN `timeout_s: 30`, `max_retries: 1`
- DEFAULT: `timeout_s: 120`, `max_retries: 3`, exponential backoff, `on_timeout: skip`

## Quality Criteria
- GOOD: timeout_s, max_retries, on_timeout all present and non-null
- GREAT: retry strategy names which error codes trigger retry, fallback behavior documented
- FAIL: no timeout_s, infinite retry, retry triggered on non-retryable 4xx errors

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_runtime_rule]] | upstream | 0.44 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | sibling | 0.33 |
| [[runtime-rule-builder]] | related | 0.32 |
| [[p01_kc_error_recovery]] | sibling | 0.28 |
| [[p01_kc_rate_limit_config]] | sibling | 0.28 |
| [[p01_kc_quality_gate]] | sibling | 0.27 |
| [[p03_ins_runtime_rule]] | related | 0.26 |
| [[bld_memory_runtime_rule]] | downstream | 0.25 |
| [[bld_knowledge_card_output_validator]] | sibling | 0.25 |
| [[bld_knowledge_card_runtime_rule]] | sibling | 0.25 |
