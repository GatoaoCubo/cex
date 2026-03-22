---
# TEMPLATE: Skill (P04 Tools)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P04_tools/_schema.yaml (types.skill)
# Max 4KB | quality_min: 7.0
# Key insight: Skills com metricas reais tem confianca 2x maior

id: p04_skill_{{NAME_SLUG}}
name: {{SKILL_KEBAB_NAME}}
description: {{ONE_LINE_WHAT_IT_DOES}}
version: 1.0.0
lp: P04
type: skill
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
domain: {{DOMAIN}}
quality: {{QUALITY_7_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, {{TAG3}}]
tldr: {{ONE_DENSE_SENTENCE}}
user_invocable: {{true_OR_false}}
trigger: {{COMO_ATIVAR_EX_SLASH_COMMAND}}
when_to_use: {{CONDICAO_DE_USO}}
when_not_to_use: {{QUANDO_NAO_USAR}}
phases:
  - {{PHASE_1_NOME}}
  - {{PHASE_2_NOME}}
  - {{PHASE_3_NOME}}
examples:
  - {{EXEMPLO_USO_1}}
  - {{EXEMPLO_USO_2}}
density_score: {{0.80_TO_1.00}}
---

# {{SKILL_DISPLAY_NAME}}

## Purpose
<!-- 2-3 frases: o que faz, qual problema resolve, satellite responsavel -->
{{SKILL_NAME}} e o **{{ROLE_EM_NEGRITO}}** do CODEXA. Domain: {{DOMAIN}} ({{SATELLITE}} satellite).

## Workflow Phases
<!-- Fases numeradas com input/output por fase -->

### Phase 1: {{PHASE_1_NOME}}
**Input**: {{PHASE_1_INPUT}}
**Action**: {{PHASE_1_ACAO}}
**Output**: {{PHASE_1_OUTPUT}}

### Phase 2: {{PHASE_2_NOME}}
**Input**: {{PHASE_2_INPUT}}
**Action**: {{PHASE_2_ACAO}}
**Output**: {{PHASE_2_OUTPUT}}

### Phase 3: {{PHASE_3_NOME}}
**Input**: {{PHASE_3_INPUT}}
**Action**: {{PHASE_3_ACAO}}
**Output**: {{PHASE_3_OUTPUT}}

## Usage

```bash
# {{CASO_1_DESCRICAO}}
/{{TRIGGER}} {{ACAO_1}} {{PARAMETROS_1}}

# {{CASO_2_DESCRICAO}}
/{{TRIGGER}} {{ACAO_2}} {{PARAMETROS_2}}
```

## Input / Output

```yaml
input:
  {{FIELD_1}}: {{TYPE}}  # {{DESCRICAO}}
  {{FIELD_2}}: {{TYPE}}  # {{DESCRICAO}}

output:
  {{RESULT_1}}: {{TYPE}}  # {{DESCRICAO}}
  {{RESULT_2}}: {{TYPE}}  # {{DESCRICAO}}
```

## Anti-Patterns
<!-- O que NAO fazer com esta skill -->
- {{ANTI_1}}: {{RAZAO}}
- {{ANTI_2}}: {{RAZAO}}

## Metrics
<!-- OPCIONAL mas valorizado - dados reais de performance -->
| Metrica | Threshold | Acao |
|---------|-----------|------|
| {{METRICA_1}} | {{THRESHOLD_1}} | {{ACAO_1}} |
| {{METRICA_2}} | {{THRESHOLD_2}} | {{ACAO_2}} |

## Cross-References
- {{AGENT_RELACIONADO}}: {{DESCRICAO_RELACAO}}
- {{SKILL_RELACIONADA}}: {{DESCRICAO_RELACAO}}
