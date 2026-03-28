---
# TEMPLATE: Action Prompt (P03 Prompt)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P03_prompt/_schema.yaml (types.action_prompt)
# Max 2048 bytes

id: p03_ap_{{ACTION_SLUG}}
kind: action_prompt
action: {{ACTION_NAME}}
input_required: [{{INPUT_1}}, {{INPUT_2}}, {{INPUT_3}}]
output_expected: {{OUTPUT_FORMAT_ESPECIFICO}}
---

# Action Prompt: {{ACTION_NAME}}

## Purpose
{{O_QUE_ESTA_ACAO_EXECUTA_EM_1_LINHA}}.

## Input
```yaml
{{INPUT_1}}: {{EXEMPLO_CONCRETO}}
{{INPUT_2}}: {{EXEMPLO_CONCRETO}}
{{INPUT_3}}: {{EXEMPLO_CONCRETO}}
```

## Execution
1. {{PASSO_1_COM_CRITERIO_DE_ENTRADA}}
2. {{PASSO_2_COM_TRANSFORMACAO_OBSERVAVEL}}
3. {{PASSO_3_COM_CHECK_DE_QUALIDADE}}

## Output
```text
{{OUTPUT_FORMAT_ESPECIFICO}}
```

## Validation
- {{CRITERIO_MENSURAVEL_1}}
- {{CRITERIO_MENSURAVEL_2}}
- {{CRITERIO_MENSURAVEL_3}}
