---
id: p10_qg_prospective_memory
kind: quality_gate
pillar: P11
title: "Gate: prospective_memory"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
domain: "prospective_memory -- agent store of future intentions and reminders"
quality: null
tags: [quality-gate, prospective-memory, P10, future-actions]
tldr: "Gate for prospective_memory: owner, reminders array, trigger_type, action_payload, execution_mechanism."
density_score: 0.90
llm_function: GOVERN
---
# Gate: prospective_memory

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | ID matches `^p10_pm_[a-z][a-z0-9_]+$` | Wrong format |
| H03 | ID equals filename stem | Mismatch |
| H04 | Kind equals literal `prospective_memory` | Wrong kind |
| H05 | Quality field is null | Non-null value |
| H06 | owner declared and non-empty | Missing owner |
| H07 | reminders array has >= 1 entry | Empty or missing |
| H08 | Each reminder has trigger_type | Missing trigger_type |
| H09 | Each reminder has action_payload | Missing or vague ("something") |
| H10 | execution_mechanism declared | Missing |

## SOFT Scoring
| Dimension | Weight | Criteria |
|---|---|---|
| Action payload executability | 2.0 | Self-contained instructions without external context |
| Trigger specificity | 1.5 | Concrete trigger values (datetime, signal name, condition expression) |
| Priority ordering | 0.5 | Priority integers declared for multi-reminder stores |
| Expiry appropriateness | 0.5 | Time-sensitive reminders have expiry; recurring have null |
| Completion policy | 0.5 | mark_done vs re_schedule matches reminder nature |
| Boundary clarity | 1.0 | Not schedule (no cron workflow config), not session_state |
| tldr quality | 0.5 | Includes owner and reminder count/types |

## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Reference prospective memory spec |
| >= 8.0 | Publish | Deploy for agent integration |
| >= 7.0 | Review | Improve action_payload or trigger values |
| < 7.0 | Reject | Return with failures |
