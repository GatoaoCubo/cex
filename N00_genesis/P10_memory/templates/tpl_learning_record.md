---
# TEMPLATE: Learning Record
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P10_memory/_schema.yaml (types.learning_record)
# Max 2048 bytes | density_min: 0.80 | quality_min: 8.0

id: p10_lr_{{TOPIC_SLUG}}
kind: learning_record
8f: F7_govern
pillar: P10
title: "Learning: {{TOPIC}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, learning, memory]
tldr: "{{ONE_SENTENCE_WHAT_WAS_LEARNED}}"
density_score: {{0.80_TO_1.00}}
decay: {{DAYS_UNTIL_STALE}}
---

# Learning: {{TOPIC}}

## Event

| Property | Value |
|----------|-------|
| Task | {{TASK_DESCRIPTION}} |
| Agent_group | {{AGENT_GROUP_NAME}} |
| Date | {{ISO_DATE}} |
| Outcome | {{success / partial / fail}} |
| Score | {{0.0_TO_10.0}} |

## What Happened

{{2_3_SENTENCES_DESCRIBING_THE_EVENT_AND_RESULT}}

## Pattern (if success)

| Step | Action | Why It Worked |
|------|--------|---------------|
| 1 | {{ACTION_1}} | {{REASON}} |
| 2 | {{ACTION_2}} | {{REASON}} |
| 3 | {{ACTION_3}} | {{REASON}} |

## Anti-Pattern (if failure)

| Symptom | Root Cause | Fix |
|---------|-----------|-----|
| {{SYMPTOM}} | {{CAUSE}} | {{CORRECTIVE_ACTION}} |

## Evidence

- Input: {{WHAT_WAS_GIVEN}}
- Output: {{WHAT_WAS_PRODUCED}}
- Metric: {{CONCRETE_NUMBER}}

## Propagation

- Applies to: {{OTHER_AGENTS_OR_TASKS}}
- Does NOT apply to: {{EXCEPTIONS}}
