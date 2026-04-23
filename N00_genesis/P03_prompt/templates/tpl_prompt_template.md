---
# TEMPLATE: Prompt Template (P03 Prompt)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P03_prompt/_schema.yaml (types.prompt_template)
# Max 2KB | quality_min: 7.0
# Sintaxe: {{MUSTACHE}} = template engine | [BRACKET] = humano/agente decide

id: p03_pt_{{TOPIC_SLUG}}
kind: prompt_template
pillar: P03
title: {{TITLE_DESCRITIVO}}
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
domain: {{DOMAIN}}
quality: {{QUALITY_7_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, {{TAG3}}]
tldr: {{ONE_DENSE_SENTENCE}}
when_to_use: {{CONDICAO_DE_USO}}
keywords: [{{KEYWORD1}}, {{KEYWORD2}}, {{KEYWORD3}}]
variables:
  - name: {{VAR1_NAME}}
    type: {{string_OR_list_OR_int}}
    description: {{DESCRICAO}}
    example: {{EXEMPLO_CONCRETO}}
  - name: {{VAR2_NAME}}
    type: {{string_OR_list_OR_int}}
    description: {{DESCRICAO}}
    example: {{EXEMPLO_CONCRETO}}
density_score: {{0.80_TO_1.00}}
---

# {{TITLE_DESCRITIVO}}

## Purpose
<!-- 1-2 linhas: o que este prompt faz, especifico -->
{{PURPOSE_1_LINHA_ESPECIFICO}}.

## Variables

| Var | Tipo | Descricao | Exemplo |
|-----|------|-----------|---------|
| `{{VAR1_NAME}}` | {{TYPE}} | {{DESCRICAO}} | {{EXEMPLO}} |
| `{{VAR2_NAME}}` | {{TYPE}} | {{DESCRICAO}} | {{EXEMPLO}} |
| `{{VAR3_NAME}}` | {{TYPE}} | {{DESCRICAO}} | {{EXEMPLO}} |

## Template Body

```
{{PURPOSE_LINE}}

INPUT:
- {{VAR1_NAME}}: {{VAR1_NAME}}
- {{VAR2_NAME}}: {{VAR2_NAME}}

EXECUTE:
1. {{STEP_1_COM_OUTPUT_INTERMEDIARIO}}
2. {{STEP_2_COM_OUTPUT_INTERMEDIARIO}}
3. {{STEP_3_COM_OUTPUT_INTERMEDIARIO}}

OUTPUT FORMAT: {{OUTPUT_FORMAT_ESPECIFICO}}

VALIDATION:
- {{CRITERIO_MENSURAVEL_1}}
- {{CRITERIO_MENSURAVEL_2}}
- {{CRITERIO_MENSURAVEL_3}}
```

## Quality Gates
- PURPOSE: max 2 linhas, especifico (nao generico)
- VARIABLES: cada campo com tipo e exemplo concreto
- STEPS: numerados, cada um com output intermediario definido
- VALIDATION: min 3 criterios mensuraveis

## Examples
<!-- min 2 pares input/output -->

**Exemplo 1**
- Input: `{{VAR1_NAME}}={{EXAMPLE_VALUE_1}}`
- Output: `{{EXPECTED_OUTPUT_1}}`

**Exemplo 2**
- Input: `{{VAR1_NAME}}={{EXAMPLE_VALUE_2}}`
- Output: `{{EXPECTED_OUTPUT_2}}`

## Verification
<!-- INSTRUCAO: output DEVE incluir evidencia de verificacao. -->
- [ ] Output exists at expected path (verified via Read/Glob)
- [ ] Output matches expected format (schema/structure validated)
- [ ] No placeholder/TODO markers remain in output
- [ ] Acceptance criteria from Purpose section satisfied

## Semantic Bridge
<!-- Obrigatorio se quality >= 8.0 -->
- Also known as: {{ALIAS_1}}, {{ALIAS_2}}
- Keywords: {{KEYWORD_BRIDGE_1}}, {{KEYWORD_BRIDGE_2}}
- Equivalents: {{FRAMEWORK_1}}: {{EQ_1}} | {{FRAMEWORK_2}}: {{EQ_2}}
