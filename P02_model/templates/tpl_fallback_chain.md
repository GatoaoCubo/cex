---
# TEMPLATE: Fallback Chain (P02 Model)
# Valide contra P02_model/_schema.yaml (types.fallback_chain)
# Max 512 bytes

id: p02_fb_{{CHAIN_SLUG}}
kind: fallback_chain
chain: [{{STEP_1}}, {{STEP_2}}, {{STEP_3}}]
timeout_per_step: {{SECONDS_INT}}
---

# Fallback Chain: {{CHAIN_SLUG}}

## Chain
<!-- INSTRUCAO: ordem de tentativa do mais forte para o mais resiliente. -->
1. {{STEP_1}} - {{QUANDO_USAR}}
2. {{STEP_2}} - {{QUANDO_CAUSA_FALLBACK}}
3. {{STEP_3}} - {{ULTIMO_RECURSO}}

## Timing
- Timeout per step: {{SECONDS_INT}}s
- Abort when: {{CONDICAO_DE_ABORT}}
- Log key: {{CAMPO_OU_SIGNAL_DE_AUDITORIA}}
