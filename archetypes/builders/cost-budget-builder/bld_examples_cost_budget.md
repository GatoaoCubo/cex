---
kind: examples
id: bld_examples_cost_budget
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of cost_budget artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.1
title: "Examples Cost Budget"
version: "1.0.0"
author: n03_builder
tags: [cost_budget, builder, examples, P09]
tldr: "Golden and anti-examples for cost_budget construction: ideal structure vs common pitfalls."
domain: "cost budget construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Examples: cost-budget-builder
## Golden Example
INPUT: "Define budget limits for all Anthropic and OpenAI providers, monthly reset, alert at 80%"
OUTPUT:
```yaml
id: p09_cb_multi_provider
kind: cost_budget
pillar: P09
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "builder_agent"
scope: "global"
providers:
  - anthropic
  - openai
quality: null
tags: [cost_budget, multi-provider, global, P09, spend-tracking]
tldr: "Global budget: anthropic + openai, $500/mo cap, warn at 80%, block at 100%"
description: "Monthly spend limits for anthropic and openai providers with automated alerts and hard block on breach"
currency: USD
reset_policy: monthly
alert_enabled: true
total_budget: 500
overage_action: block
```
## Overview
Global monthly cost budget covering anthropic and openai providers.
Enforced by cex_token_budget.py at each LLM call; breach triggers hard block.
## Budget Catalog
| Provider | Model | Token Limit | USD Limit | Alert % | Reset | Overage Action |
|----------|-------|-------------|-----------|---------|-------|----------------|
| anthropic | * | null | 300 | 80% | monthly | block |
| anthropic | claude-opus-4-6 | 5000000 | 200 | 75% | monthly | block |
| openai | * | null | 200 | 80% | monthly | warn |
| openai | gpt-4o | 3000000 | 150 | 75% | monthly | warn |
## Alert Policy
| Threshold | Level | Channel | Action |
|-----------|-------|---------|--------|
| 75% | warn | log | Write to .cex/runtime/cost_alerts.jsonl |
| 80% | warn | webhook | POST to ops-webhook with provider + current spend |
| 100% | block | pagerduty | Page on-call; hard-block all calls to that provider |
Escalation: warn -> log + webhook; block -> pagerduty page + API calls return 429 locally.
## Overage Rules
- Breach behavior: cex_token_budget.py raises BudgetExceededError; caller receives graceful error
- Grace period: none -- hard block on first call that would exceed limit
- Increase request: update total_budget field + PR review; no runtime override without code change
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_cb_ pattern (H02 pass)
- kind: cost_budget (H04 pass)
- providers list matches Budget Catalog entries (H08 pass)
- both token_limit and usd_limit defined (at least one non-null per entry) (H07 pass)
- alert_threshold_pct set and warn_pct < block_pct (H09 pass)
- all 4 body sections present (H10 pass)
- no API keys or billing credentials in artifact (H06 pass)
- tldr: 63 chars <= 160 (S01 pass)
- tags: 5 items, includes "cost_budget" (S02 pass)

## Anti-Example
INPUT: "Create budget config for claude"
BAD OUTPUT:
```yaml
id: claude-budget
kind: budget
pillar: config
providers: anthropic
quality: 7.5
tags: [claude]
limit: $200/month use sk-ant-XXXX to track
```
Budget for claude. Set limit to 200 dollars.
FAILURES:
1. id: "claude-budget" uses hyphens and no `p09_cb_` prefix -> H02 FAIL
2. kind: "budget" not "cost_budget" -> H04 FAIL
3. pillar: "config" not "P09" -> H03 FAIL
4. quality: 7.5 (not null) -> H05 FAIL
5. providers is string not list -> H08 FAIL
6. limit field contains actual credential hint (sk-ant-XXXX) -> H06 FAIL
7. Missing: version, created, updated, author, scope, currency, reset_policy, tldr -> H01 FAIL
8. Body missing ## Budget Catalog, ## Alert Policy, ## Overage Rules -> H10 FAIL
9. No alert threshold defined -> H09 FAIL
10. No overage_action defined -> H07 FAIL
