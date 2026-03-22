---
# TEMPLATE: Meta/Technical Knowledge Card
# Para KCs tecnicos: APIs, configs, benchmarks, especificacoes
# Valide contra P01_knowledge/_schema.yaml (types.knowledge_card.body_structure.meta_kc)
# Max 4KB | density_min: 0.8 | quality_min: 7.0

id: p01_kc_{{TOPIC_SLUG}}
type: knowledge_card
lp: P01
title: {{TITLE_5_100_CHARS}}
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
domain: {{DOMAIN_TECH_OR_INFRA}}
quality: {{QUALITY_7_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, {{TAG3}}]
tldr: {{ONE_DENSE_SENTENCE_WITH_SPECIFIC_DATA}}
when_to_use: {{WHEN_TO_CONSULT_THIS_KC}}
keywords: [{{KEYWORD1}}, {{KEYWORD2}}, {{KEYWORD3}}]
long_tails:
  - {{QUESTION_1_HOW_TO}}
  - {{QUESTION_2_WHAT_IS}}
axioms:
  - {{FUNDAMENTAL_RULE_IMPERATIVE}}
linked_artifacts:
  agent: {{p02_agent_related_OR_null}}
  skill: {{p04_skill_related_OR_null}}
density_score: {{0.80_TO_1.00}}
---

# {{TITLE_5_100_CHARS}}

## Executive Summary
<!-- 1-2 frases densas com o dado mais importante -->
{{SUMMARY_SENTENCE_1_WITH_SPECIFIC_DATA}}. {{SUMMARY_SENTENCE_2_OPTIONAL}}.

## Spec Table
<!-- Dados exatos: precos, APIs, configs, limites - NADA VAGO -->
| Campo | Valor | Nota |
|-------|-------|------|
| {{SPEC_1_NAME}} | {{SPEC_1_VALUE}} | {{SPEC_1_NOTE}} |
| {{SPEC_2_NAME}} | {{SPEC_2_VALUE}} | {{SPEC_2_NOTE}} |
| {{SPEC_3_NAME}} | {{SPEC_3_VALUE}} | {{SPEC_3_NOTE}} |

## Patterns
<!-- O que funciona - especifico, com evidencia -->
- {{PATTERN_1_SPECIFIC_WITH_EVIDENCE}}
- {{PATTERN_2_SPECIFIC_WITH_EVIDENCE}}
- {{PATTERN_3_SPECIFIC_WITH_EVIDENCE}}

## Anti-Patterns
<!-- O que evitar - com razao concreta -->
- {{ANTI_PATTERN_1}}: {{REASON_WHY}}
- {{ANTI_PATTERN_2}}: {{REASON_WHY}}

## Application
<!-- Estado atual + oportunidade de uso no projeto -->
{{CURRENT_STATE_IN_PROJECT}}. {{OPPORTUNITY_OR_NEXT_ACTION}}.

## References
<!-- URLs + KCs relacionadas -->
- {{URL_1_OR_KC_1}}
- {{URL_2_OR_KC_2_OPTIONAL}}
