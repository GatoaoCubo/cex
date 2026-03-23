---
# TEMPLATE: Router (P02 Model)
# Valide contra P02_model/_schema.yaml (types.router)
# Max 1024 bytes

id: p02_rt_{{SCOPE_SLUG}}
type: router
routes:
  - when: {{CONDICAO_1}}
    send_to: {{TARGET_1}}
  - when: {{CONDICAO_2}}
    send_to: {{TARGET_2}}
fallback: {{DEFAULT_TARGET}}
---

# Router: {{SCOPE_SLUG}}

## Routes
<!-- INSTRUCAO: ordenar do caso mais especifico para o mais geral. -->
| Priority | Condition | Target | Reason |
|----------|-----------|--------|--------|
| 1 | {{CONDICAO_1}} | {{TARGET_1}} | {{JUSTIFICATIVA_1}} |
| 2 | {{CONDICAO_2}} | {{TARGET_2}} | {{JUSTIFICATIVA_2}} |
| 3 | {{CONDICAO_3}} | {{TARGET_3}} | {{JUSTIFICATIVA_3}} |

## Fallback
<!-- INSTRUCAO: usado quando nenhuma regra bate ou confianca cai. -->
- Target: {{DEFAULT_TARGET}}
- Trigger: {{SEM_MATCH_OU_CONFIANCA_BAIXA}}
- Note: {{COMO_EVITAR_LOOP_DE_ROUTING}}
