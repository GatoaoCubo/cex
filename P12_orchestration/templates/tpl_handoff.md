---
# TEMPLATE: Handoff
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P12_orchestration/_schema.yaml (types.handoff)
# Max 2048 bytes | density_min: 0.80 | quality_min: 8.0

id: p12_ho_{{TASK_SLUG}}
type: handoff
lp: P12
title: "Handoff: {{TASK_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, handoff, orchestration]
tldr: "{{ONE_SENTENCE_WHAT_SATELLITE_MUST_DO}}"
density_score: {{0.80_TO_1.00}}
---

# {{TARGET_SATELLITE}} — {{MISSION}}: {{TITLE}}
**Autonomia Total** | **Quality {{MIN_QUALITY}}+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO

{{2_3_SENTENCES_WHAT_USER_WANTS_AND_WHY}}

## SEEDS

`{{KEYWORD_1}}, {{KEYWORD_2}}, {{KEYWORD_3}}, {{KEYWORD_4}}, {{KEYWORD_5}}`

## TAREFAS

### Step 1: {{ACTION_VERB}} {{OBJECT}}
{{CLEAR_DESCRIPTION_WITH_OPEN_VARIABLES}}

### Step 2: {{ACTION_VERB}} {{OBJECT}}
{{CLEAR_DESCRIPTION_WITH_OPEN_VARIABLES}}

### Step 3: {{ACTION_VERB}} {{OBJECT}}
{{CLEAR_DESCRIPTION_WITH_OPEN_VARIABLES}}

## SCOPE FENCE

- SOMENTE: {{PATHS_ALLOWED}}
- NAO TOQUE: {{PATHS_FORBIDDEN}}

## COMMIT

```bash
git add {{PATHS}}
git commit -m "{{SAT}}[{{MISSION}}]: {{DESCRIPTION}}"
```

## SIGNAL

```python
python -c "from records.core.python.signal_writer import write_signal; write_signal('{{sat_lower}}', 'complete', {{SCORE}}, task='{{task_id}}')"
```
