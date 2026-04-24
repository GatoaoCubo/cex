---
quality: 8.4
# TEMPLATE: Session State (P10 Memory)
# Valide contra P10_memory/_schema.yaml (types.session_state)
# Max 3072 bytes

id: p10_ss_[session_slug]
kind: session_state
8f: F8_collaborate
pillar: P10
title: [snapshot_da_sessao]
version: 1.0.0
created: [yyyy-mm-dd]
updated: [yyyy-mm-dd]
author: [agent_group_name]
tags: [[tag1], [tag2], session, memory]
tldr: [estado_atual_da_sessao_em_uma_frase]
density_score: 1.0
related:
  - p10_ax_session_compression
  - p03_sp_[agent_slug]
  - p02_agent_[name_slug]
  - p07_e2e_[pipeline_slug]
  - p02_iso_[agent_name]
  - p01_kc_memory_session_compression
  - bld_memory_session_state
  - p01_kc_session_state
  - session-state-builder
  - bld_collaboration_session_state
---

# Session State: [session_slug]

## Session IDs
<!-- INSTRUCAO: dual-ID obrigatorio. content_session_id SEMPRE preenchido. memory_session_id pode ser NULL. -->
```yaml
content_session_id: {{STABLE_UUID}}  # Used for ALL DB operations
memory_session_id: {{SDK_SESSION_ID_OR_NULL}}  # Lazy-captured, for SDK resume only
compression_status: {{pending|done}}  # Set to "done" after Stop compression
```
<!-- INVARIANT: if memory_session_id is NULL, session CANNOT be resumed via SDK. Create new session. -->

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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_ax_session_compression]] | related | 0.40 |
| [[p03_sp_[agent_slug]]] | upstream | 0.34 |
| [[p02_agent_[name_slug]]] | upstream | 0.31 |
| [[p07_e2e_[pipeline_slug]]] | upstream | 0.30 |
| [[p02_iso_[agent_name]]] | upstream | 0.29 |
| [[p01_kc_memory_session_compression]] | upstream | 0.26 |
| [[bld_memory_session_state]] | related | 0.24 |
| [[p01_kc_session_state]] | related | 0.23 |
| [[session-state-builder]] | related | 0.22 |
| [[bld_collaboration_session_state]] | related | 0.20 |
