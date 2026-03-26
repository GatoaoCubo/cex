---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an instruction
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: instruction

```yaml
---
id: p03_ins_{{task_slug}}
kind: instruction
pillar: P03
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
title: "{{human_readable_title}}"
target: "{{who_executes}}"
steps_count: {{integer_matching_body}}
prerequisites:
  - "{{prerequisite_1}}"
  - "{{prerequisite_2}}"
validation_method: {{checklist|automated|manual|none}}
idempotent: {{true|false}}
atomic: {{true|false}}
rollback: "{{undo_procedure_or_null}}"
dependencies:
  - "{{dependency_1}}"
logging: {{true|false}}
domain: "{{domain_value}}"
quality: null
tags: [instruction, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
---
```

## Prerequisites
- {{prerequisite_1_verifiable_condition}}
- {{prerequisite_2_verifiable_condition}}

## Steps
1. {{action_1}} — {{expected_outcome_1}}
2. {{action_2}} — {{expected_outcome_2}}
3. {{action_3}} — {{expected_outcome_3}}
{{...one action per step, repeat for steps_count}}

## Validation
- [ ] {{check_1_verifiable}}
- [ ] {{check_2_verifiable}}
- [ ] Final outcome: {{expected_final_state}}

## Rollback
{{rollback_procedure_or_na_if_idempotent}}

## References
- {{reference_1}}
- {{reference_2}}
