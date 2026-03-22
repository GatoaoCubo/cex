---
# TEMPLATE: Mental Model
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P10_memory/_schema.yaml (types.mental_model)
# Max 2048 bytes | density_min: 0.80 | quality_min: 8.0

id: p10_mm_{{AGENT_SLUG}}
type: mental_model
lp: P10
title: "Mental Model: {{AGENT_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, mental-model, memory]
tldr: "{{ONE_SENTENCE_HOW_AGENT_THINKS}}"
density_score: {{0.80_TO_1.00}}
decay: {{DAYS_UNTIL_REFRESH_OR_never}}
---

# Mental Model: {{AGENT_NAME}}

## Identity

| Property | Value |
|----------|-------|
| Agent | {{AGENT_NAME}} |
| Domain | {{PRIMARY_DOMAIN}} |
| Role | {{ONE_LINE_ROLE}} |
| Axiom | {{CORE_BELIEF_ONE_SENTENCE}} |

## Domain Map

| Concept | Understanding | Last Applied |
|---------|--------------|--------------|
| {{CONCEPT_1}} | {{0.0_TO_1.0}} | {{ISO_DATE}} |
| {{CONCEPT_2}} | {{0.0_TO_1.0}} | {{ISO_DATE}} |
| {{CONCEPT_3}} | {{0.0_TO_1.0}} | {{ISO_DATE}} |

## Tools

| Tool | Purpose | Priority |
|------|---------|----------|
| {{TOOL_1}} | {{WHAT_IT_DOES}} | {{primary / secondary}} |
| {{TOOL_2}} | {{WHAT_IT_DOES}} | {{primary / secondary}} |

## Constraints

- Max concurrent: {{N}}
- Token budget: {{LIMIT_OR_standard}}
- Scope fence: {{PATHS_ALLOWED}}
- Never: {{FORBIDDEN_ACTIONS}}

## Routing Table

| Input Pattern | Decision | Confidence |
|---------------|----------|------------|
| {{PATTERN_1}} | {{ACTION}} | {{0.0_TO_1.0}} |
| {{PATTERN_2}} | {{ACTION}} | {{0.0_TO_1.0}} |

## Decision Heuristics

1. {{HEURISTIC_1}}: {{RULE}}
2. {{HEURISTIC_2}}: {{RULE}}
3. {{HEURISTIC_3}}: {{RULE}}
