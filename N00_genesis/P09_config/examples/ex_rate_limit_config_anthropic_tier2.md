---
id: p09_ratelimit_anthropic_tier2
kind: rate_limit_config
pillar: P09
name: "Anthropic Tier 2 Rate Limits"
description: "Rate limiting configuration for Anthropic API Tier 2 with RPM, TPM, daily budget, and queue escalation"
provider: anthropic
rpm: 1000
tpm: 80000
daily_budget: "$50"
escalation: queue
version: 1.0.0
created: 2026-03-29
author: builder_agent
quality: 9.0
tags: [rate-limit, anthropic, tier-2, budget, queue, cost-control]
related:
  - p01_kc_rate_limit_config
  - bld_knowledge_card_rate_limit_config
  - bld_examples_rate_limit_config
  - bld_output_template_rate_limit_config
  - p11_qg_rate_limit_config
  - rate-limit-config-builder
  - p03_sp_rate_limit_config_builder
  - bld_architecture_rate_limit_config
  - p01_kc_api_rate_limiting_retry_patterns
  - SPEC_06_multi_provider
---

# Rate Limit Config: Anthropic Tier 2

## Overview

Enforces Anthropic API Tier 2 rate limits across all organization agent_groups. When limits approach, requests queue instead of failing. Daily budget cap of $50 prevents runaway costs from autonomous agent_group loops.

## Tier 2 Limits (Anthropic)

| Limit | Value | Scope | Reset |
|-------|-------|-------|-------|
| Requests per minute (RPM) | 1,000 | Per API key | Rolling 60s window |
| Tokens per minute (TPM) | 80,000 | Per API key (input + output) | Rolling 60s window |
| Tokens per day (TPD) | 2,500,000 | Per organization | Midnight UTC |
| Daily budget | $50 | Self-imposed (not Anthropic-enforced) | Midnight BRT (UTC-3) |

## Model-Specific Token Costs

| Model | Input (per 1M) | Output (per 1M) | Typical Request Cost |
|-------|----------------|-----------------|---------------------|
| claude-opus-4-6 | $15.00 | $75.00 | $0.12 (3K in, 1K out) |
| claude-sonnet-4-6 | $3.00 | $15.00 | $0.024 (3K in, 1K out) |
| claude-haiku-4-5 | $0.80 | $4.00 | $0.0064 (3K in, 1K out) |

## Budget Allocation by Agent_group

| Agent_group | Model | Daily Budget | Typical RPM | Rationale |
|-----------|-------|-------------|-------------|-----------|
| orchestrator | opus-4-6 | $15 | 20 | Orchestration, low volume high complexity |
| builder_agent | opus-4-6 | $12 | 50 | Build tasks, code generation |
| operations_agent | opus-4-6 | $8 | 30 | Deploy, test, validate |
| research_agent | sonnet-4-6 | $5 | 100 | Research, high volume lower cost |
| marketing_agent | sonnet-4-6 | $4 | 80 | Marketing copy, batch generation |
| knowledge_agent | sonnet-4-6 | $3 | 60 | Knowledge processing |
| commercial_agent | sonnet-4-6 | $3 | 40 | Monetization, course content |
| **Total** | — | **$50** | **380** | — |

## Escalation Strategy

```yaml
escalation:
  strategy: queue
  levels:
    - trigger: rpm >= 80%      # 800+ RPM
      action: log_warning
      message: "RPM approaching limit: {{current}}/1000"

    - trigger: rpm >= 95%      # 950+ RPM
      action: queue_requests
      queue_max: 500
      queue_timeout: 30s
      message: "Queueing requests — RPM at {{current}}/1000"

    - trigger: tpm >= 90%      # 72K+ TPM
      action: downgrade_model
      from: opus-4-6
      to: sonnet-4-6
      message: "TPM pressure — downgrading non-critical to sonnet"

    - trigger: daily_budget >= 80%  # $40+
      action: restrict_to_essential
      allowed: [orchestrator, operations_agent]
      message: "Budget 80% — only orchestration and deploy allowed"

    - trigger: daily_budget >= 95%  # $47.50+
      action: hard_stop
      message: "Budget exhausted — all API calls blocked until reset"
      alert: slack
```

## Rate Limiter Implementation

```python
import time
from collections import deque
from threading import Lock

class AnthropicRateLimiter:
    def __init__(self, rpm: int = 1000, tpm: int = 80000, daily_budget: float = 50.0):
        self.rpm = rpm
        self.tpm = tpm
        self.daily_budget = daily_budget

        self._request_times = deque()
        self._token_counts = deque()  # (timestamp, token_count)
        self._daily_spend = 0.0
        self._lock = Lock()

    def acquire(self, estimated_tokens: int, model: str) -> dict:
        with self._lock:
            now = time.time()
            window_start = now - 60

            # Clean expired entries
            while self._request_times and self._request_times[0] < window_start:
                self._request_times.popleft()
            while self._token_counts and self._token_counts[0][0] < window_start:
                self._token_counts.popleft()

            current_rpm = len(self._request_times)
            current_tpm = sum(tc[1] for tc in self._token_counts)

            # Check limits
            if current_rpm >= self.rpm:
                wait = self._request_times[0] - window_start
                return {"allowed": False, "reason": "rpm", "retry_after": wait}

            if current_tpm + estimated_tokens > self.tpm:
                return {"allowed": False, "reason": "tpm", "retry_after": 5.0}

            estimated_cost = self._estimate_cost(estimated_tokens, model)
            if self._daily_spend + estimated_cost > self.daily_budget:
                return {"allowed": False, "reason": "budget", "retry_after": None}

            # Record and allow
            self._request_times.append(now)
            self._token_counts.append((now, estimated_tokens))
            self._daily_spend += estimated_cost

            return {
                "allowed": True,
                "rpm_used": current_rpm + 1,
                "tpm_used": current_tpm + estimated_tokens,
                "budget_remaining": self.daily_budget - self._daily_spend
            }

    def _estimate_cost(self, tokens: int, model: str) -> float:
        rates = {
            "claude-opus-4-6": 0.045,    # ~$45 per 1M tokens blended
            "claude-sonnet-4-6": 0.009,   # ~$9 per 1M tokens blended
            "claude-haiku-4-5": 0.0024,   # ~$2.4 per 1M tokens blended
        }
        return (tokens / 1_000_000) * rates.get(model, 0.009)
```

## Monitoring Dashboard

| Metric | Source | Alert Threshold |
|--------|--------|-----------------|
| RPM current | Rate limiter counter | >= 800 (warn), >= 950 (queue) |
| TPM current | Token counter sum | >= 72,000 (warn) |
| Daily spend | Cost accumulator | >= $40 (restrict), >= $47.50 (stop) |
| Queue depth | Queue length | >= 200 (warn), >= 400 (critical) |
| 429 responses from Anthropic | API response code | >= 1 (our limiter should prevent these) |
| Avg queue wait time | Queue timestamps | >= 10s (warn), >= 25s (degrade) |

## Headers (Anthropic Response)

```
x-ratelimit-limit-requests: 1000
x-ratelimit-limit-tokens: 80000
x-ratelimit-remaining-requests: 742
x-ratelimit-remaining-tokens: 53200
x-ratelimit-reset-requests: 2026-03-29T14:00:32Z
x-ratelimit-reset-tokens: 2026-03-29T14:00:18Z
retry-after: 3
```

Always parse these headers and sync local counters — Anthropic's count is authoritative.

## Anti-Patterns
- Retrying 429s immediately without exponential backoff (triggers stricter throttling)
- Ignoring TPM limit and only tracking RPM (long prompts hit TPM first)
- No daily budget cap (autonomous loops can spend hundreds overnight)
- Single global rate limiter instead of per-agent_group budgets (one agent_group starves others)
- Hardcoding limits instead of reading from Anthropic response headers (limits change with tier upgrades)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_rate_limit_config]] | related | 0.41 |
| [[bld_knowledge_card_rate_limit_config]] | upstream | 0.37 |
| [[bld_examples_rate_limit_config]] | upstream | 0.36 |
| [[bld_output_template_rate_limit_config]] | upstream | 0.32 |
| [[p11_qg_rate_limit_config]] | downstream | 0.32 |
| [[rate-limit-config-builder]] | related | 0.32 |
| [[p03_sp_rate_limit_config_builder]] | related | 0.31 |
| [[bld_architecture_rate_limit_config]] | upstream | 0.29 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | upstream | 0.28 |
| [[SPEC_06_multi_provider]] | upstream | 0.28 |
