---
id: p11_qg_content_monetization
kind: quality_gate
pillar: P11
title: "Gate: content_monetization"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: content_monetization
quality: 9.1
tags: [quality-gate, content-monetization, P11, pricing, billing, credits, governance]
tldr: "Gates for monetization artifacts — margin enforcement, webhook idempotency, credit tracking, mock-first development, checkout security."
density_score: 1.0
llm_function: GOVERN
---
# Gate: content_monetization

## Definition
| Field | Value |
|-------|-------|
| Kind | content_monetization (cli_tool/workflow instances) |
| Pillar | P04 (tools) |
| Function | CALL (monetization automation) |
| Threshold | 8.0 minimum |

## HARD Gates (fail = reject)
| # | Gate | Check |
|---|------|-------|
| H1 | 9-stage complete | All 9 stages documented (PARSE through DEPLOY) |
| H2 | Margin enforcement | floor_margin_pct >= 0.30 and explicitly set |
| H3 | Integer pricing | All prices in centavos/cents, no floats |
| H4 | Zero secrets | No API keys/webhook secrets in plaintext — only ENV_VAR |
| H5 | Webhook idempotent | idempotency: true and dedup mechanism described |
| H6 | Mock mode default | mock_mode: true in all non-production configs |
| H7 | Credit coverage | Every pipeline operation has a defined credit cost |
| H8 | Overdraft explicit | overdraft_policy is set (not undefined/implicit) |

## SOFT Gates (warn, don't reject)
| # | Gate | Check | Weight |
|---|------|-------|--------|
| S1 | Multi-tier | At least 2 pricing tiers defined | 0.8 |
| S2 | Credit packs | Pay-as-you-go packs available for non-subscribers | 0.7 |
| S3 | Behavioral emails | Email sequences use behavioral triggers, not time-only | 0.8 |
| S4 | Annual discount | Yearly pricing with discount available | 0.5 |
| S5 | Fallback provider | Alternative checkout provider documented | 0.6 |
| S6 | Course structure | If courses enabled: modules + lessons + drip defined | 0.7 |
| S7 | Ad ROI tracking | If ads enabled: CPA target + pixel configured | 0.6 |
| S8 | Webhook retry | Retry policy with exponential backoff defined | 0.8 |
| S9 | Country-agnostic | No hardcoded country/currency — all via config | 0.7 |
| S10 | Validation stage | Pre-launch margin check + webhook test documented | 0.9 |

## Margin Validation Gate (per-tier, at config time)
| Tier Type | Min Margin | Rationale |
|-----------|-----------|-----------|
| Free | N/A | No revenue, but must cap credit usage |
| Starter/Basic | 30% | Minimum viable after pipeline costs |
| Pro/Growth | 40% | Should fund scaling |
| Enterprise | 50% | Custom support costs absorb margin |
| Credit Pack | 35% | Per-unit must cover operation + overhead |

## Scoring Formula
```
score = (HARD_pass / 8) * 6.0 + (SOFT_weighted / max_weight) * 4.0
```

## Quality Tiers
| Tier | Score | Meaning |
|------|-------|---------|
| REJECT | < 8.0 | Missing stages, no margin check, or security violation |
| PUBLISH | 8.0-8.9 | Pipeline complete, margins enforced, webhooks idempotent |
| EXEMPLARY | 9.0+ | Full funnel (ads→checkout→course→email), multi-provider, behavioral triggers |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Critical revenue stream requiring immediate launch |
| approver | n06-chief |
| audit_trail | Log in records/audits/ with justification and timestamp |
| expiry | 48h — full gate pass required before expiry |
| never_bypass | H3 (integer pricing), H4 (zero secrets), H5 (webhook idempotency) |

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Flag for review |
| < 7.0  | REJECT | Rework required |
