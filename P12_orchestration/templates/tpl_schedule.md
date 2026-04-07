---
id: p12_schedule
kind: schedule
pillar: P12
version: 1.0.0
title: "Template — Schedule"
tags: [template, schedule, cron, automation, recurring]
tldr: "Defines recurring automated tasks: when to run, what to execute, retry policy, and monitoring. Supports cron syntax, interval-based, and event-triggered schedules."
quality: 9.1
updated: "2026-04-07"
domain: "orchestration"
author: n03_builder
created: "2026-04-07"
density_score: 0.98
---

# Schedule: [SCHEDULE_NAME]

## Purpose
[WHAT recurring task this schedules — daily quality scan, weekly report, hourly sync]

## Schedule Definition
```yaml
id: "[SCHEDULE_ID]"
name: "[Human-readable name]"
cron: "[CRON_EXPRESSION]"          # e.g., "0 9 * * 1-5" = weekdays 9am
interval: "[ALTERNATIVE_TO_CRON]"  # e.g., "every 6h"
timezone: "[America/Sao_Paulo]"
enabled: true
```

## Common Patterns

| Pattern | Cron | When |
|---------|------|------|
| Daily morning | `0 9 * * *` | Every day 9:00 AM |
| Weekdays only | `0 9 * * 1-5` | Mon-Fri 9:00 AM |
| Every 6 hours | `0 */6 * * *` | 00:00, 06:00, 12:00, 18:00 |
| Weekly Monday | `0 9 * * 1` | Every Monday 9:00 AM |
| Monthly 1st | `0 9 1 * *` | First of month 9:00 AM |

## Task Configuration
```yaml
task:
  command: "[COMMAND_TO_EXECUTE]"
  working_dir: "[CEX_ROOT]"
  timeout_s: [300]
  env:
    CEX_NUCLEUS: "[N07]"
  on_success: [log | notify | chain_next]
  on_failure: [retry | alert | skip]
```

## Retry Policy
| Attempt | Delay | Action |
|---------|-------|--------|
| 1st failure | 60s | Retry automatically |
| 2nd failure | 300s | Retry with alert |
| 3rd failure | — | Skip + notify on-call |

## Monitoring
- **Last run**: [ISO8601 timestamp]
- **Last status**: [success | failed | skipped]
- **Success rate (30d)**: [N%]
- **Average duration**: [Nms]
- **Alert on**: 2+ consecutive failures

## Quality Gate
- [ ] Cron expression is valid (use crontab.guru to verify)
- [ ] Timezone explicitly set (no UTC surprise)
- [ ] Timeout defined (prevents runaway tasks)
- [ ] Retry policy limits max attempts
