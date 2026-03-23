---
# TEMPLATE: Session State (P10 Memory)
# Valide contra P10_memory/_schema.yaml (types.session_state)
# Max 3072 bytes

id: p10_ss_[session_slug]
type: session_state
lp: P10
title: [snapshot_da_sessao]
version: 1.0.0
created: [yyyy-mm-dd]
updated: [yyyy-mm-dd]
author: [satellite_name]
quality: [7.0_to_10.0]
tags: [[tag1], [tag2], session, memory]
tldr: [estado_atual_da_sessao_em_uma_frase]
---

# Session State: [session_slug]

## Snapshot
<!-- INSTRUCAO: resumir estado atual em 2-3 linhas. -->
- Goal: [objetivo_ativo]
- Stage: [etapa_atual]
- Owner: [agente_ou_usuario]

## Active Context
<!-- INSTRUCAO: somente informacao reutilizavel nesta sessao. -->
- [contexto_1]
- [contexto_2]
- [contexto_3]

## Pending Decisions
<!-- INSTRUCAO: decisoes abertas e impacto. -->
| Decision | Options | Impact |
|----------|---------|--------|
| [decisao_1] | [a|b] | [impacto] |
| [decisao_2] | [a|b] | [impacto] |

## Next Actions
<!-- INSTRUCAO: proximas 3 acoes objetivas. -->
1. [acao_1]
2. [acao_2]
3. [acao_3]

## Expiry
<!-- INSTRUCAO: quando este snapshot deve ser descartado ou renovado. -->
- Refresh at: [yyyy-mm-dd_or_event]
- Invalidate when: [condicao]
