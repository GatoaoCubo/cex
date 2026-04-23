---
kind: quality_gate
id: p11_qg_notifier
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
related:
  - bld_examples_notifier
  - bld_instruction_notifier
  - bld_output_template_notifier
  - p04_notify_slack
  - p03_sp_notifier_builder
  - p01_kc_notifier
  - notifier-builder
  - bld_schema_notifier
  - bld_memory_notifier
  - bld_architecture_notifier
---

## Quality Gate

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

## Examples

# Examples: notifier

## GOLDEN: Slack Deploy Status Notifier
```yaml
---
id: p04_notify_slack_deploy
kind: notifier
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "Slack Deploy Status Notifier"
channel: slack
template: "deploy_status_block"
priority: high
provider: "Slack API"
rate_limit:
  max_per_minute: 10
  max_per_hour: 100
retry_policy:
  max_attempts: 3
  backoff: exponential
template_vars: [service_name, version, environment, status, actor]
delivery_guarantee: at_least_once
quality: null
tags: [notifier, slack, deploy, cicd]
tldr: "Slack notifier for CI/CD deploy events. Delivers to #deployments channel with status, version, and actor."
description: "Sends deploy status (success/failure/rollback) to Slack #deployments channel via Block Kit with color-coded severity."
---

## Overview
Delivers CI/CD deployment status notifications to Slack #deployments channel via
Slack API Block Kit. Used by deploy pipeline on every deploy event (success, failure,
rollback). High priority ensures delivery within 2 minutes.

## Template
**Pattern**: `[{{status}}] {{service_name}} v{{version}} -> {{environment}} by {{actor}}`

**Variables**:
- `service_name`: deployed service identifier (e.g. "api", "worker")
- `version`: semver or git SHA (e.g. "1.4.2", "a3f9c1")
- `environment`: target env (production, staging)
- `status`: deploy outcome (success, failure, rollback)
- `actor`: triggering user or CI bot

**Examples by priority**:
- critical: `[FAILURE] api v1.4.2 -> production by ci-bot — ROLLBACK TRIGGERED`
- high: `[SUCCESS] api v1.4.2 -> production by alice`
- normal: `[STARTED] worker v2.1.0 -> staging by bob`

## Delivery
- rate_limit: 10/min, 100/hr
- retry: 3x exponential backoff (1s, 2s, 4s)
- guarantee: at_least_once
- on_failure: log to dead-letter queue, alert #ops-alerts

## Configuration
- endpoint: `https://slack.com/api/chat.postMessage`
- auth: `SLACK_BOT_TOKEN`
- channel_id: `#deployments`
```

**WHY GOLDEN**: H01-H10 all pass. S01-S12 all >= 0.8. Template has vars, examples per priority,
rate_limit, retry, delivery_guarantee, provider, auth env var, boundary clear (push, not HTTP).

---

## ANTI-PATTERN: Broken Email Notifier
```yaml
---
id: notify_email
kind: notifier
channel: email
---
Send email when user signs up.
```

**FAILURES**:
- H02 FAIL: id `notify_email` does not match `^p04_notify_[a-z][a-z0-9_]+$`
- H04 FAIL: quality field missing (must be null)
- H05 FAIL: pillar, name, template, priority all absent
- H07 FAIL: template field not defined
- S02 FAIL: no template example, no vars listed
- S04 FAIL: no rate_limit — will cause SendGrid account suspension under load
- S05 FAIL: no retry_policy — transactional emails silently dropped on failure

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
