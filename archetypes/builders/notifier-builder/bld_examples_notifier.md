---
kind: examples
id: bld_examples_notifier
pillar: P04
llm_function: GOVERN
purpose: Golden and anti-pattern examples for notifier artifacts
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [examples, notifier, P04, golden, anti-pattern]
quality: 9.0
tldr: "Golden: Slack deploy alert notifier (all gates pass, score 9.2). Anti: minimal email notifier (H05/H07/S02 fail)."
density_score: 1.0
title: Examples ISO - notifier
---
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
