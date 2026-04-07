---
# TEMPLATE: Workflow
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P12_orchestration/_schema.yaml (types.workflow)
# Max 2048 bytes | density_min: 0.80 | quality_min: 8.0

id: p12_wf_{{NAME_SLUG}}
kind: workflow
pillar: P12
title: "Workflow: {{WORKFLOW_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, workflow, orchestration]
tldr: "{{ONE_SENTENCE_WHAT_WORKFLOW_DOES}}"
density_score: {{0.80_TO_1.00}}
timeout: {{TOTAL_MINUTES}} min
---

# Workflow: {{WORKFLOW_NAME}}

## Overview

| Property | Value |
|----------|-------|
| Trigger | {{WHAT_STARTS_THIS}} |
| Input | {{WHAT_IT_RECEIVES}} |
| Output | {{WHAT_IT_PRODUCES}} |
| Timeout | {{TOTAL_MINUTES}} min |

## Steps

```
[{{STEP_1}}] --> [{{STEP_2}}] --> [{{STEP_3}}] --> [{{STEP_4}}] --> [{{STEP_5}}]
                      |                                  |
                 [{{GUARD_1}}]                     [{{GUARD_2}}]
```

### Step 1: {{STEP_1_NAME}}
- **Input**: {{STEP_1_INPUT}}
- **Action**: {{STEP_1_ACTION}}
- **Output**: {{STEP_1_OUTPUT}}
- **Duration**: {{ESTIMATED_TIME}}

### Step 2: {{STEP_2_NAME}}
- **Input**: {{STEP_2_INPUT}}
- **Action**: {{STEP_2_ACTION}}
- **Output**: {{STEP_2_OUTPUT}}
- **Duration**: {{ESTIMATED_TIME}}

### Step 3: {{STEP_3_NAME}}
- **Input**: {{STEP_3_INPUT}}
- **Action**: {{STEP_3_ACTION}}
- **Output**: {{STEP_3_OUTPUT}}
- **Duration**: {{ESTIMATED_TIME}}

## Parallel Groups

| Group | Steps | Max Concurrent |
|-------|-------|----------------|
| {{GROUP_1}} | {{STEPS}} | {{N}} |

## Rollback

| Step | Rollback Action |
|------|-----------------|
| {{STEP_1}} | {{UNDO_ACTION}} |
| {{STEP_2}} | {{UNDO_ACTION}} |

## Success Criteria

- {{CRITERIA_1}}
- {{CRITERIA_2}}
