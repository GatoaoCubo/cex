---
kind: examples
id: bld_examples_prospective_memory
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of prospective_memory artifacts
quality: 6.6
title: "Examples Prospective Memory"
version: "1.0.0"
author: n03_builder
tags: [prospective_memory, builder, examples]
tldr: "Golden and anti-examples for prospective_memory construction."
domain: "prospective memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Examples: prospective-memory-builder

## Golden Example
INPUT: "Create prospective memory for N07 with weekly quality check and N01 dispatch on low score"
```yaml
id: p10_pm_n07_quality_ops
kind: prospective_memory
pillar: P10
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
owner: "n07"
execution_mechanism: polling
completion_policy: re_schedule
reminders:
  - id: "weekly_quality_audit"
    trigger_type: time
    trigger_value: "every Monday 09:00 UTC"
    action_payload: "Run cex_doctor.py --full and compile quality report to N07_admin/P11_feedback/"
    priority: 2
    expiry: null
    completion_policy: re_schedule
    recurrence: "0 9 * * 1"
  - id: "low_quality_dispatch"
    trigger_type: condition
    trigger_value: "average quality_score < 7.5 in last 7 days"
    action_payload: "Dispatch N01 to audit and improve lowest-scoring artifacts"
    priority: 1
    expiry: null
    completion_policy: mark_done
    recurrence: null
quality: null
tags: [prospective_memory, n07, quality_ops, P10]
tldr: "N07 quality ops prospective memory: weekly audit (time trigger) + N01 dispatch on low score (condition trigger)."
```

WHY THIS IS GOLDEN: owner declared, reminders array >= 1, trigger_type per reminder, action_payload specific, priority set, quality null, execution_mechanism declared.

## Anti-Example
```yaml
id: n07-reminders
kind: schedule
reminders:
  - do: something later
quality: 8.0
```
FAILURES: hyphened id, wrong kind (schedule != prospective_memory), quality non-null, vague action_payload, missing owner, trigger_type, expiry, tags.
