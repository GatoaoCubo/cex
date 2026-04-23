---
kind: output_template
id: bld_output_template_notifier
pillar: P04
llm_function: PRODUCE
purpose: Fill-in-the-blank template for notifier artifacts
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [output_template, notifier, P04]
quality: 9.1
title: "Output Template Notifier"
tldr: "Golden and anti-examples for notifier construction, demonstrating ideal structure and common pitfalls."
domain: "notifier construction"
density_score: 0.90
related:
  - bld_instruction_notifier
  - bld_schema_notifier
  - notifier-builder
  - bld_examples_notifier
  - p03_sp_notifier_builder
  - p01_kc_notifier
  - bld_architecture_notifier
  - bld_config_notifier
  - p11_qg_notifier
  - p04_notify_slack
---
# Output Template: notifier

## Frontmatter Template
```yaml
---
id: p04_notify_{{channel_slug}}
kind: notifier
pillar: P04
version: 1.0.0
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
author: {{author}}
name: "{{Human Readable Notifier Name}}"
channel: {{email|sms|slack|discord|push|in_app|teams}}
template: "{{template_name_or_pattern}}"
priority: {{critical|high|normal|low}}
provider: "{{SendGrid|Twilio|Firebase|Slack|Discord|AWS SES|Mailgun}}"
rate_limit:
  max_per_minute: {{int}}
  max_per_hour: {{int}}
retry_policy:
  max_attempts: {{int}}
  backoff: {{linear|exponential}}
template_vars: [{{var1}}, {{var2}}]
delivery_guarantee: {{at_least_once|best_effort}}
quality: null
tags: [notifier, {{channel}}, {{domain_tag}}]
tldr: "{{<= 160ch summary of channel, provider, and use case}}"
description: "{{<= 200ch description of what notifications this sends and when}}"
---
```

## Body Template
```markdown
## Overview
{{2-3 sentences: channel, provider, use case. Who receives, under what condition.}}

## Template
**Pattern**: `{{message pattern with {{vars}} shown}}`

**Variables**:
1. `{{var1}}`: {{what it contains}}
2. `{{var2}}`: {{what it contains}}

**Examples by priority**:
1. critical: `{{full message example for critical priority}}`
2. high: `{{full message example for high priority}}`
3. normal: `{{full message example for normal priority}}`

## Delivery
1. rate_limit: {{max_per_minute}}/min, {{max_per_hour}}/hr
2. retry: {{max_attempts}}x {{backoff}} backoff
3. guarantee: {{at_least_once|best_effort}}
4. on_failure: {{what happens — log, alert, dead-letter queue}}

## Configuration
1. endpoint: `{{provider API endpoint or webhook URL pattern}}`
2. auth: `{{env var name for credentials, e.g. SENDGRID_API_KEY}}`
3. channel_id: `{{channel-specific identifier, e.g. Slack channel #alerts}}`
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P04 |
| Domain | notifier construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_notifier]] | upstream | 0.52 |
| [[bld_schema_notifier]] | downstream | 0.48 |
| [[notifier-builder]] | related | 0.46 |
| [[bld_examples_notifier]] | related | 0.46 |
| [[p03_sp_notifier_builder]] | related | 0.46 |
| [[p01_kc_notifier]] | upstream | 0.40 |
| [[bld_architecture_notifier]] | related | 0.40 |
| [[bld_config_notifier]] | related | 0.39 |
| [[p11_qg_notifier]] | downstream | 0.39 |
| [[p04_notify_slack]] | related | 0.39 |
