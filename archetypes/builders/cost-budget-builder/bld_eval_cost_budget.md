---
kind: quality_gate
id: p11_qg_cost_budget
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of cost_budget artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.1
title: "Gate: cost_budget"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, cost-budget, token-budget, spend-tracking, cost-alerts, P11]
tldr: "Gates for cost_budget artifacts: validates budget catalog completeness, alert thresholds, reset policy, overage action, and provider accuracy."
domain: "cost_budget -- token budget allocation, spend tracking, and cost alert configuration per provider/model"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
related:
  - bld_examples_cost_budget
  - p03_sp_cost_budget_builder
  - cost-budget-builder
  - bld_instruction_cost_budget
  - bld_collaboration_cost_budget
  - bld_architecture_cost_budget
  - bld_schema_cost_budget
  - bld_knowledge_card_cost_budget
  - p10_lr_cost_budget_builder
  - p11_qg_batch_config
---

## Quality Gate

# Gate: cost_budget
## Definition
| Field | Value |
|-------|-------|
| metric | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator | AND (all HARD) + weighted_sum (SOFT) |
| scope | All artifacts where `kind: cost_budget` |

## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p09_cb_[a-z][a-z0-9_]+$` | "ID fails cost_budget namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"cost_budget"` | "Kind is not 'cost_budget'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | No budget entry contains API keys, billing credentials, or payment method data | "Credential data detected in budget artifact" |
| H07 | Each budget entry has at least one non-null limit: token_limit OR usd_limit | "Budget entry has no limit defined" |
| H08 | `providers` list is non-empty (>= 1 provider defined) | "Provider list is empty" |
| H09 | Alert threshold defined: warn_pct < block_pct (block_pct <= 100) | "Alert threshold invalid or inverted" |
| H10 | Body contains all 4 required sections: Overview, Budget Catalog, Alert Policy, Overage Rules | "Missing required body section(s)" |

## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Budget catalog completeness | 1.0 | Each entry has all 7 fields: provider, model, token_limit, usd_limit, alert_threshold_pct, reset_policy, overage_action |
| Alert policy specificity | 1.0 | Channels named, escalation path defined (not just "notify someone") |
| Reset policy correctness | 1.0 | Policy matches workload pattern (rolling for batch jobs, monthly for SaaS) |
| Overage action clarity | 1.0 | Block/warn/log behavior explicitly described per entry |
| Scope accuracy | 0.5 | Scope (global/provider/model) correctly categorizes all entries |
| Provider coverage | 1.0 | All active providers in the deployment are represented |
| Per-model sub-limits | 1.0 | High-cost frontier models have individual caps, not just provider-level |
| Currency consistency | 0.5 | USD and token_units not mixed without explicit rationale |
| Boundary clarity | 0.5 | Explicitly not rate_limit_config (RPM/TPM), not env_config (variables) |
| Increase request process | 0.5 | How to legitimately raise a limit is documented |
| Enforcement reference | 1.0 | Links to or names the runtime enforcer (e.g., cex_token_budget.py) |
| Documentation | 1.0 | tldr names scope and number of providers; description is informative |
Weight sum: 1.0+1.0+1.0+1.0+0.5+1.0+1.0+0.5+0.5+0.5+1.0+1.0 = 10.0 (100%)

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |

## Bypass
| Field | Value |
|-------|-------|
| conditions | New deployment where provider spend data is not yet available |
| approver | Cost owner approval required (written); alert thresholds never bypassed |

## Examples

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

## Golden Example 2 -- Per-Customer AI Inference Cost Budget (SaaS Profit Margin Protection)
INPUT: "Define per-customer AI inference spend caps for our SaaS: free=$0.05/mo, pro=$2/mo, enterprise=$50/mo. Alert before they go over. Protect our margins."
OUTPUT:
```yaml
id: p09_cb_per_customer_saas
kind: cost_budget
pillar: P09
version: "1.0.0"
created: "2026-04-18"
updated: "2026-04-18"
author: "builder_agent"
scope: "per_customer"
providers:
  - anthropic
  - openai
quality: null
tags: [cost_budget, per-customer, saas, margin-protection, P09]
tldr: "Per-customer AI caps: free=$0.05, pro=$2, enterprise=$50/mo; warn at 80%, block at 100%"
description: "Monthly AI inference spend limits per subscription tier; enforced per customer_id to protect SaaS unit economics"
currency: USD
reset_policy: monthly
alert_enabled: true
total_budget: null
overage_action: block
customer_tier_caps:
  free:
    monthly_usd: 0.05
    alert_pct: 0.80
    overage_action: block
    margin_floor_usd: 0.00
  pro:
    monthly_usd: 2.00
    alert_pct: 0.80
    overage_action: block
    margin_floor_usd: 0.50
  enterprise:
    monthly_usd: 50.00
    alert_pct: 0.75
    overage_action: warn
    margin_floor_usd: 10.00
enforcement_key: "customer_id"
carry_over: false
```
## Overview
Per-customer monthly AI inference cost budget, scoped by subscription tier.
Enforced by cex_token_budget.py at each LLM call using customer_id as the enforcement key.
Prevents any single customer from consuming disproportionate AI compute, which is the primary
unit-economics risk in AI-augmented SaaS products.
Total_budget is null -- this config governs individual customer caps, not aggregate spend.
Aggregate provider spend is governed separately by p09_cb_multi_provider.

## Budget Catalog
| Tier | monthly_usd | alert_pct | alert_at ($) | overage_action | margin_floor ($) | carry_over |
|------|------------|-----------|-------------|----------------|-----------------|-----------|
| free | $0.05 | 80% | $0.04 | block | $0.00 | no |
| pro | $2.00 | 80% | $1.60 | block | $0.50 | no |
| enterprise | $50.00 | 75% | $37.50 | warn | $10.00 | no |

margin_floor_usd: minimum gross margin per customer per month. If actual AI spend
approaches (monthly_usd - margin_floor_usd), trigger early alert regardless of alert_pct.
Example: enterprise customer spending $41+ triggers alert even if below 75% of $50 cap,
because margin would fall below $10 floor.
carry_over: false -- unused budget does not roll to next month. Prevents budget debt.

## Alert Policy
| Trigger | Level | Audience | Action |
|---------|-------|----------|--------|
| 80% of tier cap | warn | ops-webhook | Log to .cex/runtime/cost_alerts.jsonl + notify ops |
| margin_floor breach | warn | growth team | Flag customer for upsell review (pro -> enterprise) |
| 100% of tier cap (free/pro) | block | customer | Return 402 Payment Required with upgrade URL |
| 100% of tier cap (enterprise) | warn | sales + ops | Page account manager; do not block; negotiate overage |
| 3x alerts in 1 month (any tier) | escalate | finance | Review pricing model for that tier |

Free/pro overage returns HTTP 402 with a JSON body including an upgrade URL --
converting a budget block into a conversion event (Strategic Greed: block = upgrade prompt).
Enterprise never hard-blocks; SLA prohibits it. Warn-and-negotiate preserves ARR.

## Overage Rules
- enforcement_key: customer_id -- limits are per unique customer, not per session or per API key
- Breach behavior: cex_token_budget.py raises CustomerBudgetExceededError with tier context;
  API layer maps to 402 (free/pro) or logs warn (enterprise)
- Grace period: none for free/pro; enterprise gets a 24-hour grace window before escalation
- Budget reset: monthly, on billing cycle anniversary (not calendar month start)
- Increase request: pro customers can self-serve upgrade to enterprise in-app;
  enterprise customers contact account manager for cap increase (no runtime override)
- Margin audit: monthly finance report compares actual AI COGS per tier against margin_floor;
  if median pro-tier margin < $0.50, trigger pricing review

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_cb_ pattern (H02 pass)
- kind: cost_budget (H04 pass)
- scope: per_customer (distinct from global -- different enforcement semantics) (H08 pass)
- customer_tier_caps with monthly_usd + alert_pct + overage_action + margin_floor per tier (H07 pass)
- alert_pct 80% for free/pro, 75% for enterprise (earlier warning for higher-value customers) (H09 pass)
- enforcement_key: customer_id (prevents single-customer exploitation) (H08 pass)
- all 4 body sections present (H10 pass)
- 402 + upgrade URL converts block into conversion event (Strategic Greed lens)
- margin_floor_usd as secondary alert trigger (unit economics protection)
- carry_over: false prevents budget debt accumulation (H11 pass)
- no API keys or billing credentials in artifact (H06 pass)
- tldr: 79 chars <= 160 (S01 pass)
- tags: 5 items, includes "cost_budget" and "margin-protection" (S02 pass)

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
