---
id: p11_qg_notifier
kind: quality_gate
pillar: P11
llm_function: GOVERN
purpose: Hard + soft quality gates for notifier artifacts
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [quality_gate, notifier, P04, P11]
quality: 9.0
tldr: "10 HARD gates (binary pass/fail) + 12 SOFT dims (scored 0-1). Min score 7.0 for pool."
density_score: 1.0
title: Quality Gate ISO - notifier
---
# Gate: notifier

## HARD Gates (all must pass — any fail = REJECT)
| ID  | Check                                          | Test                                                 |
|-----|------------------------------------------------|------------------------------------------------------|
| H01 | YAML frontmatter valid                         | Parses without error                                 |
| H02 | id matches namespace                           | Regex `^p04_notify_[a-z][a-z0-9_]+$`                |
| H03 | kind == "notifier"                             | Exact literal match                                  |
| H04 | quality == null                                | Field present and null                               |
| H05 | Required fields present                        | id, kind, pillar, name, channel, template, priority  |
| H06 | channel is valid enum                          | email|sms|slack|discord|push|in_app|teams            |
| H07 | template field non-empty                       | len(template) > 0                                    |
| H08 | priority is valid enum                         | critical|high|normal|low                             |
| H09 | body <= 1024 bytes                             | len(body.encode()) <= 1024                           |
| H10 | Not bidirectional HTTP                         | No receive/listen/webhook semantics in body          |

## SOFT Scoring (0.0 - 1.0 per dimension, target >= 7.0/10 weighted avg)
| Dim | Dimension           | Weight | Criteria                                                  |
|-----|---------------------|--------|-----------------------------------------------------------|
| S01 | channel_coverage    | 1.0    | Channel fully specified, provider named                   |
| S02 | template_quality    | 1.5    | Template has example, vars listed, per-priority examples  |
| S03 | priority_routing    | 1.0    | All used priorities have timing semantics documented      |
| S04 | rate_limiting       | 1.0    | rate_limit object present with numeric values             |
| S05 | retry_policy        | 1.0    | retry_policy present; mandatory if priority=critical      |
| S06 | delivery_guarantees | 0.5    | delivery_guarantee field set, behavior documented         |
| S07 | provider_docs       | 0.5    | Provider named, endpoint or auth env var referenced       |
| S08 | variable_docs       | 1.0    | template_vars list complete, each var described in body   |
| S09 | boundary_clarity    | 1.0    | Explicitly not a webhook, not an api_client               |
| S10 | domain_specificity  | 0.5    | Use case is specific (not generic "send notification")    |
| S11 | testsbility         | 0.5    | Enough detail to write a unit test or mock delivery       |
| S12 | user_experience     | 0.5    | Message tone, length, and format apownte for channel  |

## Scoring Formula
```
score = sum(dim.score * dim.weight) / sum(dim.weight)
pool_eligible = score >= 8.0
experimental = score >= 7.0
reject = score < 7.0
```
