---
id: p10_em_user_preferences
kind: entity_memory
pillar: P10
title: "User Entity Memory — Preference Tracking Across Sessions"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: memory
quality: 9.1
tags: [entity-memory, user-preferences, personalization, cross-session]
tldr: "Armazena fatos sobre o user (nome, preferencias, expertise) com merge-on-new para personalizacao persistente"
when_to_use: "Quando o sistema precisa lembrar quem e o user e como ele prefere trabalhar entre sessoes"
keywords: [entity-memory, user-profile, preferences, expertise-tracking]
name: user_preferences
entity_type: user
attributes:
  - name
  - preferences
  - history
  - expertise
update_policy: merge_on_new_interaction
density_score: 1.0
related:
  - p01_kc_entity_memory
  - p10_ms_conversation_compress
  - p01_kc_memory_type
  - bld_collaboration_entity_memory
  - p04_skill_memory_extract
  - entity-memory-builder
  - p03_sp_entity_memory_builder
  - p01_kc_memory_persistence
  - bld_knowledge_card_entity_memory
---

## TL;DR

Entity memory do tipo `user` armazena fatos persistentes sobre o usuario: nome, preferencias de workflow, historico de interacoes, e niveis de expertise por dominio. A politica `merge_on_new_interaction` garante que novos fatos sao incorporados sem sobrescrever os existentes.

## Conceito Central

Diferente de learning_record (que registra o que deu certo/errado em tasks), entity_memory registra fatos sobre ENTIDADES — neste caso, o user. Cada atributo tem semantica propria:

- **name**: identificador do user (pode ser nome real ou handle)
- **preferences**: como o user gosta de trabalhar (terse vs verbose, commit style, etc.)
- **history**: interacoes passadas relevantes (projetos, decisoes recorrentes)
- **expertise**: niveis de conhecimento por dominio (senior em Go, iniciante em React)

### Estrutura de Armazenamento

```yaml
entity:
  type: user
  id: "user_ronaldo"

  name:
    display: "Ronaldo"
    first_seen: "2026-01-15"

  preferences:
    response_style: terse      # no trailing summaries
    commit_style: conventional  # feat:/fix:/refactor:
    pr_strategy: bundled        # prefer 1 PR over many small
    testing: pytest             # not unittest
    language: pt-BR             # Portuguese prompts OK
    auto_ship: true             # commit+push+deploy without asking

  history:
    projects_active:
      - organization-core             # AI agent framework
      - fresh-start             # React frontend (Lovable)
      - gato-cubo-commerce      # e-commerce
    recent_decisions:
      - "2026-03-15: Chose Mercado Pago over Stripe for payments"
      - "2026-03-01: Integrated Firecrawl for marketplace scraping"
      - "2026-02-18: Disabled all power-save after BSOD"

  expertise:
    advanced:     [python, fastapi, prompt-engineering, ai-agents, e-commerce-br]
    intermediate: [react, typescript, postgresql, railway-deploy]
    beginner:     [rust, kubernetes, mobile-dev]

update_policy:
  strategy: merge_on_new_interaction
  rules:
    - "New preference overrides old (latest wins)"
    - "Expertise levels only upgrade, never downgrade without explicit correction"
    - "History appends, never deletes"
    - "Conflicting facts: ask user to clarify before overwriting"
  trigger: session_start  # re-inject entity into context
```

## Exemplo Pratico

**Sessao 1** (2026-01-15): User diz "I'm Ronaldo, I build AI agents"
```yaml
# Entity created
name: {display: "Ronaldo"}
expertise: {advanced: [ai-agents]}
```

**Sessao 14** (2026-02-20): User diz "stop summarizing at the end"
```yaml
# Merge: preferences updated
preferences: {response_style: terse}
# Everything else preserved
```

**Sessao 47** (2026-03-29): User trabalha em React pela primeira vez
```yaml
# Merge: expertise updated
expertise:
  intermediate: [react]  # added based on observed usage
# Previous advanced/beginner preserved
```

**Merge conflict example**: User diz "I prefer unittest now" mas entity tem `testing: pytest`.
```yaml
# Resolution: latest wins (preference)
preferences: {testing: unittest}  # overwritten
# But log previous value in history
history:
  preference_changes:
    - "2026-03-29: testing pytest->unittest"
```

## Fronteira com Outros Kinds

| Kind | Diferenca |
|------|-----------|
| runtime_state (P10) | Estado do AGENTE em runtime — nao do user |
| learning_record (P10) | O que o SISTEMA aprendeu — nao fatos sobre entidades |
| memory_summary (P10) | Compressao de conversa — nao fatos persistentes |
| user_persona (P03) | Template de prompt para simular persona — nao fatos reais |

## Anti-Patterns

- Armazenar preferencias efemeras como permanentes ("use tabs hoje" != "sempre tabs")
- Downgrade de expertise sem correcao explicita do user
- Misturar fatos do user com fatos do projeto (use project memory para isso)
- Armazenar dados sensiveis (tokens, passwords) como atributos de entidade
- Update policy `overwrite_all` — perde historico acumulado

## Referencias

- schema: P10/_schema.yaml (entity_memory)
- related: p10_ms_memory_summary, p10_lr_learning_record

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_entity_memory]] | related | 0.20 |
| [[p10_ms_conversation_compress]] | related | 0.19 |
| [[p01_kc_memory_type]] | related | 0.18 |
| [[bld_collaboration_entity_memory]] | downstream | 0.17 |
| [[p04_skill_memory_extract]] | upstream | 0.17 |
| [[entity-memory-builder]] | related | 0.16 |
| [[p03_sp_entity_memory_builder]] | related | 0.16 |
| [[p01_kc_memory_persistence]] | upstream | 0.16 |
| [[bld_knowledge_card_entity_memory]] | upstream | 0.16 |
