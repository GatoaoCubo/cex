---
kind: output_template
id: bld_output_template_notifier
pillar: P04
llm_function: GENERATE
purpose: Fill-in-the-blank template for notifier artifacts
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [output_template, notifier, P04]
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
- `{{var1}}`: {{what it contains}}
- `{{var2}}`: {{what it contains}}

**Examples by priority**:
- critical: `{{full message example for critical priority}}`
- high: `{{full message example for high priority}}`
- normal: `{{full message example for normal priority}}`

## Delivery
- rate_limit: {{max_per_minute}}/min, {{max_per_hour}}/hr
- retry: {{max_attempts}}x {{backoff}} backoff
- guarantee: {{at_least_once|best_effort}}
- on_failure: {{what happens — log, alert, dead-letter queue}}

## Configuration
- endpoint: `{{provider API endpoint or webhook URL pattern}}`
- auth: `{{env var name for credentials, e.g. SENDGRID_API_KEY}}`
- channel_id: `{{channel-specific identifier, e.g. Slack channel #alerts}}`
```
