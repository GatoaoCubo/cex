---
# TEMPLATE: Few-Shot Examples (P03 Prompt)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P03_prompt/_schema.yaml (types.few_shot)
# Max 4096 bytes

id: p03_fs_{{TASK_SLUG}}
type: few_shot
lp: P03
task: {{TASK_DESCRIPTION}}
examples_count: {{N}}
---

# Few-Shot: {{TASK_DESCRIPTION}}

## Task
{{O_QUE_OS_EXEMPLOS_DEMONSTRAM_EM_1_LINHA}}

## Examples

### Example 1
**Input**:
```
{{INPUT_CONCRETO_1}}
```
**Output**:
```
{{OUTPUT_CONCRETO_1}}
```

### Example 2
**Input**:
```
{{INPUT_CONCRETO_2}}
```
**Output**:
```
{{OUTPUT_CONCRETO_2}}
```

### Example 3 (edge case)
**Input**:
```
{{INPUT_EDGE_CASE}}
```
**Output**:
```
{{OUTPUT_EDGE_CASE}}
```

## Selection Criteria
- {{QUANDO_USAR_ESTE_SET_DE_EXEMPLOS}}
- {{CRITERIO_DE_DIVERSIDADE}}
- {{LIMITE_DE_EXEMPLOS_POR_CONTEXTO}}
