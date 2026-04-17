---
# TEMPLATE: Cost Budget (token economics)
# Fill {{VARS}} before use | Validate against P09_config/_schema.yaml
# Max 3072 bytes | density_min: 0.85 | quality_min: 9.0

id: "p09_cb_{{BUDGET_SLUG}}"
kind: cost_budget
pillar: P09
title: "Budget: {{BUDGET_NAME}}"
version: 1.0.0
created: "{{ISO_DATE}}"
updated: "{{ISO_DATE}}"
author: "{{AGENT_OR_TEAM}}"
quality: 7.6
tags: "[{{TAG1}}, cost_budget, tokens, P09]"
tldr: "{{ONE_SENTENCE_SCOPE_AND_CAP}}"
density_score: "{{0.85_TO_1.00}}"
---

# Budget: {{BUDGET_NAME}}

## Scope

| Property | Value |
|----------|-------|
| Budget ID | `{{BUDGET_SLUG}}` |
| Scope | {{nucleus / mission / provider / global}} |
| Applies to | {{n03 / MISSION_X / anthropic / *}} |
| Period | {{daily / weekly / monthly}} |
| Rollover | {{true / false}} |
| Owner | {{TEAM_OR_PERSON}} |

## Caps

| Dimension | Soft cap | Hard cap | On breach |
|-----------|----------|----------|-----------|
| Total cost USD | ${{S_COST}} | ${{H_COST}} | {{alert / throttle / block}} |
| Input tokens | {{S_IN_TOK}} | {{H_IN_TOK}} | alert |
| Output tokens | {{S_OUT_TOK}} | {{H_OUT_TOK}} | alert |
| Requests | {{S_REQ}} | {{H_REQ}} | throttle |

## Provider Rates (USD per 1M tokens)

| Provider / Model | Input | Output | Cache read | Batch discount |
|------------------|-------|--------|------------|-----------------|
| `anthropic/claude-opus-4-6` | {{15.00}} | {{75.00}} | {{1.50}} | 50% |
| `anthropic/claude-sonnet-4-6` | {{3.00}} | {{15.00}} | {{0.30}} | 50% |
| `openai/gpt-4o` | {{2.50}} | {{10.00}} | {{1.25}} | 50% |
| `{{OTHER_PROVIDER}}` | {{X}} | {{Y}} | -- | -- |

## Alert Thresholds

| Threshold | Channel | Action |
|-----------|---------|--------|
| 50% of cap | log | monitor |
| 80% of cap | signal + log | warn owner |
| 100% soft cap | signal + log | recommend cheaper tier |
| 100% hard cap | signal + block | route to fallback_chain or halt |

## Optimization Hooks

- Prompt caching: expect {{30_TO_90}}% cache-read savings on repeated context
- Batch API: use for non-realtime jobs (~50% discount)
- Tiered routing: route cheap queries to Sonnet/Haiku, keep Opus for complex
- Truncation policy: `{{cex_token_budget.py}}` for context window budgeting

## Reporting

- Daily summary: `.cex/metrics/cost_{{BUDGET_SLUG}}_{{DATE}}.json`
- Dashboard: {{DASHBOARD_URL_OR_PATH}}
- Breach log: `.cex/runtime/signals/cost_breach_*.json`

## Anti-patterns

- NOT a `rate_limit_config` (requests/sec throttling, not money)
- NOT a `token_budget` tool (internal context sizing, not spend policy)
- NOT a `feature_flag` (budget is always on; only caps change)
