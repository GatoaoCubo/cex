---
# TEMPLATE: Meta-Prompt (P03 Prompt)
# Valide contra P03_prompt/_schema.yaml (types.meta_prompt)
# Max 4096 bytes

id: p03_mp_{{PURPOSE_SLUG}}
kind: meta_prompt
pillar: P03
target_prompt_type: {{system_prompt|user_prompt|prompt_template|etc}}
optimization_goal: {{OBJETIVO}}
---

# Meta-Prompt: {{PURPOSE}}

## Objective
Generate/improve a {{TARGET_PROMPT_TYPE}} that {{OBJETIVO_EM_1_LINHA}}.

## Input Specification
The meta-prompt receives:
```yaml
seed: {{PROMPT_SEMENTE_OU_DESCRICAO}}
context: {{DOMINIO_E_RESTRICOES}}
constraints:
  max_bytes: {{LIMITE}}
  quality_min: {{SCORE}}
  style: {{ESTILO}}
```

## Generation Rules
1. {{REGRA_1_COMO_CONSTRUIR}}
2. {{REGRA_2_ESTRUTURA_OBRIGATORIA}}
3. {{REGRA_3_ANTI_PATTERNS_A_EVITAR}}

## Quality Criteria for Generated Prompt
- [ ] {{CRITERIO_1_MENSURAVEL}}
- [ ] {{CRITERIO_2_MENSURAVEL}}
- [ ] {{CRITERIO_3_MENSURAVEL}}

## Iteration
- Method: {{genetic|mipro|manual|piter}}
- Stop: quality >= {{TARGET_SCORE}}
- Max iterations: {{MAX_ITER}}
