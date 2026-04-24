---
# TEMPLATE: Handoff
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P12_orchestration/_schema.yaml (types.handoff)
# Max 2048 bytes | density_min: 0.80 | quality_min: 8.0

id: p12_ho_{{TASK_SLUG}}
kind: handoff
8f: F8_collaborate
pillar: P12
title: "Handoff: {{TASK_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, handoff, orchestration]
tldr: "{{ONE_SENTENCE_WHAT_AGENT_GROUP_MUST_DO}}"
density_score: {{0.80_TO_1.00}}
---

# {{TARGET_AGENT_GROUP}} — {{MISSION}}: {{TITLE}}
**Autonomia Total** | **Quality {{MIN_QUALITY}}+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO

{{2_3_SENTENCES_WHAT_USER_WANTS_AND_WHY}}

## SEEDS

`{{KEYWORD_1}}, {{KEYWORD_2}}, {{KEYWORD_3}}, {{KEYWORD_4}}, {{KEYWORD_5}}`

## MUST HAVES
<!-- Goal-backward verification: define WHAT success looks like BEFORE tasks -->
```yaml
truths:
  - "{{BEHAVIORAL_TRUTH_1}}"  # e.g., "API returns 200 for valid input"
  - "{{BEHAVIORAL_TRUTH_2}}"  # e.g., "No regression in existing tests"
artifacts:
  - path: "{{FILE_PATH_1}}"
    check: "{{exists|size>0|contains:keyword}}"
  - path: "{{FILE_PATH_2}}"
    check: "{{exists|size>0|contains:keyword}}"
key_links:
  - "{{IMPORT_OR_DEPENDENCY_1}}"  # e.g., "api/v1/routes.py imports new handler"
  - "{{IMPORT_OR_DEPENDENCY_2}}"
```

## TAREFAS
<!-- Full task text inline — do NOT reference external files. 2-5 min granularity per step. -->

### Step 1: {{ACTION_VERB}} {{OBJECT}}
{{CLEAR_DESCRIPTION_WITH_OPEN_VARIABLES}}

### Step 2: {{ACTION_VERB}} {{OBJECT}}
{{CLEAR_DESCRIPTION_WITH_OPEN_VARIABLES}}

### Step 3: {{ACTION_VERB}} {{OBJECT}}
{{CLEAR_DESCRIPTION_WITH_OPEN_VARIABLES}}

## SELF-REVIEW CHECKLIST
<!-- Implementer must check ALL before reporting DONE -->
- [ ] All MUST HAVES truths verified
- [ ] All artifacts exist and pass checks
- [ ] No files modified outside SCOPE FENCE
- [ ] Commit message follows convention
- [ ] Quality score >= {{MIN_QUALITY}}

## SCOPE FENCE

- SOMENTE: {{PATHS_ALLOWED}}
- NAO TOQUE: {{PATHS_FORBIDDEN}}

## COMMIT

```bash
git add {{PATHS}}
git commit -m "{{SAT}}[{{MISSION}}]: {{DESCRIPTION}}"
```

## STOPPED AT
<!-- Fill ONLY if session ends before completion. Enables cross-session resumability. -->
```yaml
stopped_at:
  step: {{LAST_COMPLETED_STEP_NUMBER}}
  status: {{DONE|DONE_WITH_CONCERNS|BLOCKED}}
  reason: "{{WHY_STOPPED}}"
  resume_from: "Step {{NEXT_STEP_NUMBER}}: {{STEP_NAME}}"
```

## SIGNAL

```python
python -c "from records.core.python.signal_writer import write_signal; write_signal('{{sat_lower}}', 'complete', {{SCORE}}, task='{{task_id}}')"
```
