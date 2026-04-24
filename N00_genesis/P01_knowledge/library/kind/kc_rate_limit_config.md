---
id: p01_kc_rate_limit_config
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P09
title: "Rate Limit Config — Deep Knowledge for rate_limit_config"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: rate_limit_config
quality: 9.1
tags: [rate_limit_config, P09, CONSTRAIN, kind-kc]
tldr: "rate_limit_config defines RPM, TPM, and daily budget caps per model or agent_group — with backoff strategy — to prevent runaway spend and provider throttling."
when_to_use: "Building, reviewing, or reasoning about rate_limit_config artifacts"
keywords: [rate_limiting, RPM, budget_cap]
feeds_kinds: [rate_limit_config]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - bld_knowledge_card_rate_limit_config
  - rate-limit-config-builder
  - bld_examples_rate_limit_config
  - p03_sp_rate_limit_config_builder
  - p01_kc_api_rate_limiting_retry_patterns
  - bld_collaboration_rate_limit_config
  - bld_output_template_rate_limit_config
  - bld_architecture_rate_limit_config
  - p11_qg_rate_limit_config
  - bld_tools_rate_limit_config
---

# Rate Limit Config

## Spec
```yaml
kind: rate_limit_config
pillar: P09
llm_function: CONSTRAIN
max_bytes: 1024
naming: p09_ratelimit.md
core: true
```

## What It Is
A rate_limit_config defines hard ceilings on requests per minute (RPM), tokens per minute (TPM), and daily USD spend — plus the backoff strategy on limit hits. It is NOT a runtime_rule (which governs timeouts, retries, and per-operation limits rather than provider-level rate enforcement).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | N/A | Rate limiting handled externally or via callbacks |
| LlamaIndex | N/A | No built-in rate limiting primitives |
| CrewAI | N/A | LiteLLM handles rate limit errors transparently |
| DSPy | `backoff_time` in `LM` config | Retry delay on rate limit errors |
| Haystack | N/A | Rate limiting external to pipeline components |
| OpenAI | Tier 1-5 RPM/TPM/RPD limits | Per-model tier limits; Tier 1 GPT-4o: 500 RPM |
| Anthropic | RPM/TPM/DTPM limits | Opus: ~1000 RPM; Sonnet: ~2000 RPM; model-specific |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| rpm | int | required | Request ceiling — lower = safer spend, slower throughput |
| tpm | int | required | Token ceiling — lower = cost control, may truncate batches |
| daily_budget_usd | float | null | Hard spend cap — null = no cap (dangerous in production) |
| backoff_strategy | enum | exponential | linear/exponential/fixed — exponential prevents thundering herd |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Hard budget cap | Production systems with real spend | `daily_budget_usd: 10.00` |
| Conservation mode | Throttle when credits drop below threshold | Trigger at `credits < 20%`: drop to 20% of normal rpm |
| Per-model limits | Different ceilings per model tier | `opus: {rpm: 500}`, `sonnet: {rpm: 1000}` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No budget cap in production | Runaway agents generate unbounded spend | Always set `daily_budget_usd` in production |
| Linear backoff | Linear retry floods provider on sustained outage | Use exponential backoff with jitter |
| Shared limits across agent_groups | One agent_group's burst starves others | Isolate rate limit config per agent_group |

## Integration Graph
```
env_config, secret_config --> [rate_limit_config] --> runtime_rule, agent_card
                                       |
                                  feature_flag, law, permission
```

## Decision Tree
- IF production system THEN `daily_budget_usd` mandatory
- IF development/research THEN relaxed RPM, no hard budget cap
- IF rate limit error (429) occurs THEN exponential backoff + alert
- DEFAULT: exponential backoff, `daily_budget_usd` set, per-model limits defined

## Quality Criteria
- GOOD: rpm, tpm, backoff_strategy all present
- GREAT: per-model limits, daily_budget_usd set, conservation mode threshold defined
- FAIL: no budget cap in production, linear backoff, single shared config for all agent_groups

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_rate_limit_config]] | sibling | 0.57 |
| [[rate-limit-config-builder]] | related | 0.56 |
| [[bld_examples_rate_limit_config]] | upstream | 0.52 |
| [[p03_sp_rate_limit_config_builder]] | related | 0.51 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | sibling | 0.48 |
| [[bld_collaboration_rate_limit_config]] | downstream | 0.47 |
| [[bld_output_template_rate_limit_config]] | upstream | 0.45 |
| [[bld_architecture_rate_limit_config]] | upstream | 0.45 |
| [[p11_qg_rate_limit_config]] | downstream | 0.45 |
| [[bld_tools_rate_limit_config]] | upstream | 0.42 |
