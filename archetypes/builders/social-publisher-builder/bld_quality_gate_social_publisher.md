---
id: p11_qg_social_publisher
kind: quality_gate
pillar: P11
title: "Gate: social_publisher"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: social_publisher
quality: 9.1
tags: [quality-gate, social-publisher, P11, automation, governance]
tldr: "Gates for social publisher artifacts — config completeness, pipeline coverage, security, and reusability."
density_score: 1.0
llm_function: GOVERN
---
# Gate: social_publisher

## Definition
| Field | Value |
|-------|-------|
| Kind | social_publisher (cli_tool/workflow instances) |
| Pillar | P04 (tools) |
| Function | CALL (automation pipeline) |
| Threshold | 8.0 minimum |

## HARD Gates (fail = reject)
| # | Gate | Check |
|---|------|-------|
| H1 | Config completeness | All 7 required sections present (identity, platforms, schedule, content_mix, catalog, publisher, hashtags) |
| H2 | Zero hardcoded secrets | No API keys, tokens, or passwords in plaintext — only ENV_VAR references |
| H3 | Pipeline coverage | All 10 steps documented (LOAD through ROTATE) |
| H4 | Mix sum validation | content_mix percentages sum to exactly 100 |
| H5 | Platform validity | All listed platforms are supported (ig/fb/tt/li/tw/yt) |
| H6 | Retry defined | publisher.retry section present with max, backoff, base_seconds |
| H7 | Timezone explicit | schedule.timezone is valid IANA timezone string |

## SOFT Gates (warn, don't reject)
| # | Gate | Check | Weight |
|---|------|-------|--------|
| S1 | Company-agnostic | No hardcoded company names outside identity section | 1.0 |
| S2 | Multi-provider | At least 2 publisher types documented | 0.8 |
| S3 | Cooldown defined | catalog.cooldown_days >= 1 | 0.7 |
| S4 | Notification channel | notifications section present and configured | 0.5 |
| S5 | Cron scheduling | cron section with type and interval | 0.5 |
| S6 | Caption guidelines | Min/max caption length per platform | 0.6 |
| S7 | Hashtag strategy | Brand + niche hashtags defined, max_per_post set | 0.7 |
| S8 | Failure modes | Each pipeline step has documented failure → recovery | 0.8 |
| S9 | A/B testing | Config supports variant testing for captions | 0.3 |
| S10 | Analytics hook | Post-publish metrics collection defined | 0.4 |

## Scoring Formula
```
score = (HARD_pass_count / 7) * 6.0 + (SOFT_weighted_sum / max_weight) * 4.0
```
All 7 HARD must pass for score >= 6.0. SOFT gates add up to 4.0 bonus.

## Quality Tiers
| Tier | Score | Meaning |
|------|-------|---------|
| REJECT | < 8.0 | Missing required sections or security violation |
| PUBLISH | 8.0-8.9 | Config complete, pipeline documented, secure |
| EXEMPLARY | 9.0+ | Multi-provider, full failure modes, A/B support |

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Flag for review |
| < 7.0  | REJECT | Rework required |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental social_publisher artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |
