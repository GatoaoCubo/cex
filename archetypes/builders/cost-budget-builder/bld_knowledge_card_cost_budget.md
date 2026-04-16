---
kind: knowledge_card
id: bld_knowledge_card_cost_budget
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for cost_budget production -- token and USD budget allocation per provider/model
sources: OpenAI Usage Limits API, Anthropic Billing Tiers, AWS Bedrock Cost Controls, FinOps Foundation
quality: 9.2
title: "Knowledge Card Cost Budget"
version: "1.0.0"
author: n03_builder
tags: [cost_budget, builder, knowledge_card, P09, spend-tracking]
tldr: "Domain knowledge for cost_budget: budget allocation patterns, alert thresholds, reset policies, and FinOps principles for LLM cost governance."
domain: "cost budget construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Domain Knowledge: cost_budget
## Executive Summary
Cost budgets define the spending contract for an LLM deployment scope -- every provider and
model covered with token or USD limits, alert thresholds, reset policies, and overage actions.
Following FinOps principles, cost budgets separate spend governance from throughput control
(rate_limit_config) and environment variables (env_config). They are enforced at the call site
by the token budget SDK, preventing billing surprises by blocking or alerting before limits are hit.

## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 (config) |
| llm_function | GOVERN |
| Frontmatter fields | 15+ |
| Quality gates | 10 HARD + 12 SOFT |
| Budget units | USD or token_units |
| Reset policies | daily, weekly, monthly, rolling_7d, rolling_30d, none |
| Scope hierarchy | global > provider > model |
| Naming | p09_cb_{name_slug}.yaml |

## Patterns
**Budget scoping hierarchy**: narrower scope overrides broader scope.
| Scope | Coverage | Example |
|-------|----------|---------|
| global | All providers combined | p09_cb_global.yaml |
| provider | One provider, all models | p09_cb_anthropic.yaml |
| model | One specific model | p09_cb_claude_opus.yaml |

**Alert threshold tiers**: industry standard three-tier alerting.
| Tier | Threshold | Typical Action |
|------|-----------|----------------|
| warn | 75-80% | Log + notify ops channel |
| critical | 90-95% | Page on-call + slow-down |
| block | 100% | Hard stop all API calls |

**Reset policies by workload type**:
| Policy | Best for |
|--------|----------|
| daily | Interactive services with daily user sessions |
| weekly | Batch analysis jobs running on weekly cadence |
| monthly | SaaS products billed on monthly subscription |
| rolling_30d | High-volume services where calendar month boundary causes spikes |
| none | One-time project budgets that must not exceed a total |

**Currency choice**:
| Unit | Use when |
|------|----------|
| USD | Multi-model deployments where prices differ (comparing models fairly) |
| token_units | Single-model deployments where cost is uniform per token |

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No per-model sub-limit | Frontier model (opus) consumes entire budget while cheaper models are blocked |
| reset_policy: none on high-volume scope | Budget fills up permanently; all calls blocked after first batch job |
| Alert threshold = 100% only | No warning before block; first alert = total service interruption |
| Single global cap | Cannot attribute which provider/model drove the overage |
| Billing credentials in artifact | Security violation; API keys committed to version control |
| Mixing RPM limits with cost limits | Rate limits belong in rate_limit_config, not cost_budget |

## Application
1. Enumerate all active providers and models in the deployment
2. Estimate monthly token volumes per model from logs or projections
3. Convert to USD using provider pricing pages
4. Set per-model caps at 110% of baseline estimate (headroom for spikes)
5. Set provider-level cap at sum of model caps + 15% buffer
6. Set global cap at sum of provider caps
7. Configure warn at 80%, block at 100%, escalation to ops webhook
8. Choose reset_policy matching billing cycle or workload cadence

## References
- OpenAI: platform.openai.com/usage (Usage and billing limits)
- Anthropic: docs.anthropic.com/billing (Usage tiers and limits)
- AWS Bedrock: docs.aws.amazon.com/bedrock/cost-controls
- FinOps Foundation: finops.org/framework (FinOps cost allocation principles)
- cex_token_budget.py: _tools/cex_token_budget.py (CEX runtime enforcer)
