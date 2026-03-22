---
# TEMPLATE: Agent (P02 Model)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P02_model/_schema.yaml (types.agent)
# Max 4KB | quality_min: 7.0

id: p02_agent_{{NAME_SLUG}}
type: agent
lp: P02
title: {{TITLE_DESCRITIVO}}
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
satellite: {{SATELLITE_QUE_OPERA}}
domain: {{DOMAIN}}
quality: {{QUALITY_7_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, {{TAG3}}]
tldr: {{ONE_DENSE_SENTENCE_WHAT_IT_DOES}}
when_to_use: {{CONDICAO_DE_USO}}
keywords: [{{KEYWORD1}}, {{KEYWORD2}}, {{KEYWORD3}}]
long_tails:
  - {{PERGUNTA_1_COMO_USAR}}
  - {{PERGUNTA_2_QUANDO_USAR}}
axioms:
  - {{REGRA_FUNDAMENTAL_IMPERATIVA}}
density_score: {{0.80_TO_1.00}}
---

# {{TITLE_DESCRITIVO}}

## Overview
<!-- 2-3 frases: o que faz, qual problema resolve, quando nao usar -->
{{AGENT_NAME}} e o **{{ROLE_EM_NEGRITO}}** do CODEXA. Responsavel por {{RESPONSABILIDADE_PRINCIPAL}}.

## Architecture
<!-- ASCII diagram ou tabela de modulos -->
```
{{INPUT}} --> [{{MODULE_1}}] --> [{{MODULE_2}}] --> {{OUTPUT}}
```

## When to Use

| Cenario | Usar? |
|---------|-------|
| {{CENARIO_SIM_1}} | SIM |
| {{CENARIO_SIM_2}} | SIM |
| {{CENARIO_NAO_1}} | NAO > use {{ALTERNATIVA_1}} |
| {{CENARIO_NAO_2}} | NAO > use {{ALTERNATIVA_2}} |

## Capabilities
<!-- Lista de capacidades reais, especificas -->
- {{CAPABILITY_1}}
- {{CAPABILITY_2}}
- {{CAPABILITY_3}}

## Input / Output

```yaml
input:
  {{FIELD_1}}: {{TYPE}}  # {{DESCRICAO}}
  {{FIELD_2}}: {{TYPE}}  # {{DESCRICAO}}

output:
  {{RESULT_1}}: {{TYPE}}  # {{DESCRICAO}}
  {{RESULT_2}}: {{TYPE}}  # {{DESCRICAO}}
```

## Integration
<!-- upstream = quem chama; downstream = quem recebe resultado -->
- Upstream: {{UPSTREAM_AGENT_OR_USER}}
- Downstream: {{DOWNSTREAM_AGENT_OR_POOL}}

## Quality Gates
<!-- Criterios minimos para aceitar output -->
- {{GATE_1}}: {{THRESHOLD}}
- {{GATE_2}}: {{THRESHOLD}}
- Score >= {{MIN_SCORE}} para pool

---
*Satellite: {{SATELLITE_NAME}} | Quality: {{QUALITY}} | Domain: {{DOMAIN}}*
