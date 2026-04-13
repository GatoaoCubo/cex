---
id: p09_cb_{{BUDGET_SLUG}}
kind: cost_budget
pillar: P09
version: 1.0.0
title: "Budget: {{BUDGET_NAME}}"
tags: [template, budget, cost, token-economics, finops, {{SCOPE_TAG}}]
tldr: "{{ONE_SENTENCE_WHAT_THIS_BUDGET_CAPS_AND_FOR_WHOM}}"
quality: {{QUALITY_8_TO_10}}
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AUTHOR}}
domain: "cost governance"
density_score: {{0.80_TO_1.00}}
---

# Budget: {{BUDGET_NAME}}

## Scope

| Property | Value |
|----------|-------|
| Name | `{{BUDGET_NAME}}` |
| Scope | {{global \| per_nucleus \| per_mission \| per_user}} |
| Target | {{nucleus_id / mission_id / provider / all}} |
| Period | {{daily \| weekly \| monthly}} |
| Resets | {{ISO_DATE_OR_CRON}} |
| Rollover | {{true \| false}} (unused budget carries forward) |

## Hard Caps

| Dimension | Limit | Behavior on Breach |
|-----------|-------|-------------------|
| max_cost_usd | ${{AMOUNT}} | {{block \| downgrade \| alert_only}} |
| max_input_tokens | {{N}} | {{block \| downgrade}} |
| max_output_tokens | {{N}} | {{block \| downgrade}} |
| max_requests | {{N}} | {{block \| downgrade}} |

`max_cost_usd` is the ultimate guardrail. Never leave null.

## Provider Rates (USD per 1M tokens)

| Provider | Model | Input $/MTok | Output $/MTok | Cache Read $/MTok |
|----------|-------|--------------|---------------|-------------------|
| anthropic | claude-opus-4-6 | 15.00 | 75.00 | 1.50 |
| anthropic | claude-sonnet-4-6 | 3.00 | 15.00 | 0.30 |
| anthropic | claude-haiku-4-5 | 1.00 | 5.00 | 0.10 |
| openai | gpt-4.1 | {{X}} | {{Y}} | -- |
| local | ollama/qwen3 | 0.00 | 0.00 | 0.00 |

Update monthly or wire to provider pricing API.

## Alert Thresholds

| % of Budget | Channel | Action |
|-------------|---------|--------|
| 50% | log | informational |
| 80% | slack / log | warn oncall |
| 95% | pagerduty / slack | prep fallback routing |
| 100% | pagerduty | enforce fallback_on_exhaust |

## Fallback Policy

| Strategy | When | Effect |
|----------|------|--------|
| `block` | exhaust | Reject new requests with 429 |
| `downgrade` | exhaust | Route opus -> sonnet -> haiku |
| `batch_defer` | >=80% | Queue non-urgent work for batch API (50% discount) |
| `alert_only` | exhaust | Log + alert, keep spending (NOT RECOMMENDED) |

## Savings Tracked

| Source | Target | Measured |
|--------|--------|----------|
| Prompt cache hit rate | >=0.60 | {{MEASURED}} |
| Batch API usage | >={{30}}% of eligible | {{MEASURED}} |
| Model downgrades | opportunistic | {{MEASURED}} |

## Reporting
- Export cost-per-nucleus and cost-per-mission daily
- Attribute every request via `trace_config` tags
- Reconcile against provider billing API weekly

## Quality Gate
- [ ] `max_cost_usd` set (non-null hard cap)
- [ ] `provider_rates` separate input/output prices
- [ ] `alert_thresholds` include at least 80% and 100%
- [ ] `fallback_on_exhaust` NOT `alert_only` for production budgets
- [ ] Scope is granular (not global-only for multi-nucleus systems)
