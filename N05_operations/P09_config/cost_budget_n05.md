---
id: p09_cb_n05_operations
kind: cost_budget
pillar: P09
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: cost-budget-builder
scope: "nucleus"
providers:
  - anthropic
  - google
  - ollama
quality: null
tags: [cost_budget, n05-operations, sonnet-tier, spend-tracking, P09]
tldr: "N05 operations spend limits: Sonnet tier, 3 providers, per-dispatch-mode caps, warn 80%, block 100%"
description: "Token and USD budget policy for N05 operations nucleus across solo, grid, and overnight dispatch modes with provider-level tracking."
currency: token_units
reset_policy: rolling_30d
alert_enabled: true
total_budget: 6000000
overage_action: block
---

## Overview

N05 (Gating Wrath) governs its own LLM spend with the same discipline it applies to
operational gates: hard limits per dispatch mode, real-time alerts at 80%, and a
hard block at 100% -- no grace, no override without an explicit manifest change.
Enforced by `cex_token_budget.py` at each LLM call boundary.

## Budget Catalog

| Provider | Model | Token Limit | USD Limit | Alert % | Reset | Overage Action |
|----------|-------|-------------|-----------|---------|-------|----------------|
| anthropic | claude-sonnet-4-6 | 6000000 | null | 80% | rolling_30d | block |
| anthropic | claude-opus-4-6 | 500000 | null | 75% | rolling_30d | block |
| google | gemini-2.5-flash-lite | 4000000 | null | 80% | rolling_30d | warn |
| ollama | * | 20000000 | null | 90% | rolling_30d | log |

**Per-dispatch-mode token envelope (informational -- enforced at call site):**

| Dispatch Mode | Token Ceiling | Notes |
|---------------|---------------|-------|
| nucleus boot | 30000 | Fixed overhead; escalate if exceeded |
| solo task | 200000 | 50K-200K range; 200K hard cap |
| grid cell (1 of 6) | 200000 | Each N05 cell budgeted independently |
| overnight evolve | 1000000 | Session cap; runner halts on breach |

## Alert Policy

| Threshold | Level | Channel | Action |
|-----------|-------|---------|--------|
| 75% | warn | log | Write to `.cex/runtime/cost_alerts.jsonl` with provider + tokens used |
| 80% | warn | log + webhook | POST to ops-webhook; drop to `steady_review` rate profile |
| 95% | warn | log | Log critical; block all non-incident calls immediately |
| 100% | block | log | `BudgetExceededError` raised; caller receives graceful deny |

Escalation: 80% warn fires webhook + rate profile downgrade. 100% block halts all
N05 LLM calls for the remainder of the rolling window. Incident-burst override
requires explicit `overage_action: warn` in a signed manifest entry.

## Overage Rules

- Breach behavior: `cex_token_budget.py` raises `BudgetExceededError`; no call is made to the provider; N05 returns a structured error to the caller.
- Grace period: none -- Gating Wrath does not negotiate after the gate closes.
- Increase request: edit `total_budget` field and merge via PR; no runtime mutation without version bump.

## References

- `N05_operations/P09_config/con_rate_limit_config_n05.md` (throughput governance -- separate concern)
- `.cex/config/nucleus_models.yaml` (model routing + fallback chain for N05)
