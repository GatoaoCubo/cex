---
# TEMPLATE: Mental Model (P02 Model)
# Valide contra P02_model/_schema.yaml (types.mental_model)
# Max 2048 bytes

id: p02_mm_{{MODEL_SLUG}}
kind: mental_model
8f: F4_reason
pillar: P02
title: "{{MENTAL_MODEL_TITLE}}"
owner: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_7_TO_10}}
---

# Mental Model: {{MENTAL_MODEL_TITLE}}

## Core Assumption
{{ONE_SENTENCE_DECISION_HEURISTIC}}

## Inputs
- Signal: {{SIGNAL_1}}
- Signal: {{SIGNAL_2}}
- Signal: {{SIGNAL_3}}

## Decision Logic
1. {{IF_CONDITION_1_THEN_ACTION}}
2. {{IF_CONDITION_2_THEN_ACTION}}
3. {{IF_CONDITION_3_THEN_ACTION}}

## Failure Modes
| Failure | Detection | Recovery |
|---------|-----------|----------|
| {{FAILURE_1}} | {{DETECTION_1}} | {{RECOVERY_1}} |
| {{FAILURE_2}} | {{DETECTION_2}} | {{RECOVERY_2}} |
