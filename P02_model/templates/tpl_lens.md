---
# TEMPLATE: Lens (P02 Model)
# Valide contra P02_model/_schema.yaml (types.lens)
# Max 2048 bytes

id: p02_lens_{{PERSPECTIVE_SLUG}}
type: lens
perspective: {{PERSPECTIVE_NAME}}
applies_to: [{{AGENT_OR_DOMAIN_1}}, {{AGENT_OR_DOMAIN_2}}]
---

# Lens: {{PERSPECTIVE_NAME}}

## Perspective
<!-- INSTRUCAO: nomear o angulo especializado e o que ele privilegia. -->
- Focus: {{O_QUE_ESTA_LENTE_PRIORIZA}}
- Default question: {{PERGUNTA_QUE_GUIA_A_ANALISE}}
- Ignore by default: {{O_QUE_NAO_ENTRA_NO_ESCOPO}}

## Applies To
<!-- INSTRUCAO: listar dominios, agentes ou tarefas onde esta lente faz sentido. -->
| Target | Why |
|--------|-----|
| {{AGENT_OR_DOMAIN_1}} | {{MOTIVO_1}} |
| {{AGENT_OR_DOMAIN_2}} | {{MOTIVO_2}} |

## Heuristics
<!-- INSTRUCAO: 3-5 criterios de leitura/decisao. -->
1. {{HEURISTIC_1}}
2. {{HEURISTIC_2}}
3. {{HEURISTIC_3}}

## Output Bias
<!-- INSTRUCAO: explicar como a lente muda a resposta final. -->
- Emphasize: {{ELEMENTO_PRIORITARIO}}
- Tradeoff accepted: {{CUSTO_ACEITO}}
- Escalate when: {{CONDICAO_DE_ESCALADA}}
