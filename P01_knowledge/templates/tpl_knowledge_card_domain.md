---
# TEMPLATE: Domain Knowledge Card
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P01_knowledge/_schema.yaml (types.knowledge_card)
# Max 4KB | density_min: 0.8 | quality_min: 7.0

id: p01_kc_{{TOPIC_SLUG}}
type: knowledge_card
lp: P01
title: {{TITLE_5_100_CHARS}}
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
domain: {{DOMAIN}}
quality: {{QUALITY_7_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, {{TAG3}}]
tldr: {{ONE_DENSE_SENTENCE}}
when_to_use: {{CONDITION_OF_USE}}
keywords: [{{KEYWORD1}}, {{KEYWORD2}}, {{KEYWORD3}}]
long_tails:
  - {{QUESTION_1_HOW_TO_OR_WHAT}}
  - {{QUESTION_2_HOW_TO_OR_WHAT}}
axioms:
  - {{FUNDAMENTAL_RULE_1_IMPERATIVE}}
  - {{FUNDAMENTAL_RULE_2_OPTIONAL}}
linked_artifacts:
  workflow: {{p12_wf_topic_OR_null}}
  prompt: {{p03_pt_topic_OR_null}}
density_score: {{0.80_TO_1.00}}
---

# {{TITLE_5_100_CHARS}}

## Quick Reference
<!-- YAML block com dados chave: metricas, percentuais, timelines, limites -->
- {{KEY_METRIC_1}}: {{VALUE}}
- {{KEY_METRIC_2}}: {{VALUE}}
- {{KEY_METRIC_3}}: {{VALUE}}

## Conceitos Chave
<!-- Bullets atomicos, max 80 chars cada, min 3 -->
- {{CONCEITO_1}}: {{DEFINICAO_CURTA}}
- {{CONCEITO_2}}: {{DEFINICAO_CURTA}}
- {{CONCEITO_3}}: {{DEFINICAO_CURTA}}

## Fases
<!-- Fases numeradas do processo/strategy -->
1. {{FASE_1_NOME}}: {{DESCRICAO_ACAO}}
2. {{FASE_2_NOME}}: {{DESCRICAO_ACAO}}
3. {{FASE_3_NOME}}: {{DESCRICAO_ACAO}}

## Regras de Ouro
<!-- Axiomas em imperativos (NUNCA/SEMPRE/SE...ENTAO) -->
1. {{REGRA_1_IMPERATIVO}}
2. {{REGRA_2_IMPERATIVO}}
3. {{REGRA_3_IMPERATIVO}}

## Flow
<!-- ASCII diagram do fluxo principal - OBRIGATORIO -->
```
[{{INPUT}}] --> [{{STEP1}}] --> [{{STEP2}}] --> [{{OUTPUT}}]
```

## Comparativo
<!-- Tabela comparando opcoes/abordagens -->
| Opcao | Vantagem | Desvantagem |
|-------|----------|-------------|
| {{OPCAO_A}} | {{VANTAGEM_A}} | {{DESVANTAGEM_A}} |
| {{OPCAO_B}} | {{VANTAGEM_B}} | {{DESVANTAGEM_B}} |
