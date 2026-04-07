---
id: p10_ms_conversation_compress
kind: memory_summary
pillar: P10
title: "Conversation Compression — Incremental Summarization for Long Sessions"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: memory
quality: 9.1
tags: [memory, compression, summarization, context-window, session]
tldr: "Comprime historico de chat quando context window atinge 75%, preservando fatos-chave via summarization incremental"
when_to_use: "Sessoes longas (>20 turnos) onde context window esta enchendo e decisoes anteriores precisam ser preservadas"
keywords: [memory-summary, conversation-compress, incremental-summarization, context-management]
name: conversation_compress
source_type: chat_history
compression_method: incremental_summarization
max_tokens: 500
trigger: context_window_75pct
density_score: 1.0
---

## TL;DR

Quando uma sessao Claude Code atinge 75% do context window (~150K de 200K tokens), este memory_summary comprime o historico de conversa em um resumo incremental de ate 500 tokens, preservando: decisoes tomadas, arquivos modificados, erros encontrados, e estado atual da tarefa.

## Conceito Central

Incremental summarization funciona em camadas: cada vez que o trigger dispara, o resumo anterior e combinado com as mensagens novas desde a ultima compressao. O resultado e um resumo que cresce logaritmicamente (nao linearmente) com o tamanho da conversa.

O source_type `chat_history` indica que a fonte e o historico de mensagens user/assistant da sessao atual. Diferente de `tool_output` (comprime resultados de ferramentas) ou `file_content` (comprime conteudo de arquivos lidos).

### Ciclo de Compressao

```yaml
trigger_check:
  metric: context_window_usage
  threshold: 0.75
  check_interval: every_turn

compression:
  method: incremental_summarization
  input: messages_since_last_compression
  prior_summary: previous_memory_summary  # null on first run
  max_output_tokens: 500
  preserve_always:
    - file_paths_modified
    - git_commits_made
    - errors_encountered
    - current_task_state
    - user_decisions

output:
  format: structured_yaml
  inject_as: system_message_prefix
  ttl: session_end
```

## Exemplo Pratico

Sessao builder_agent com 47 turnos, 162K tokens usados (81%):

**Input** (mensagens desde ultima compressao, turnos 31-47):
- User pediu refactor de `api/v1/routes.py`
- Leitura de 3 arquivos (routes.py, models.py, schemas.py)
- Criacao de `api/v1/routes_v2.py`
- Erro: import circular com `core/deps.py`
- Fix: mover dependency injection para `core/container.py`
- Commit: `refactor: extract DI container from deps.py`
- User pediu testes

**Output** (memory_summary, 487 tokens):
```yaml
session_summary:
  task: "Refactor api/v1/routes.py com DI container"
  phase: "testing (pos-refactor)"
  files_modified:
    - api/v1/routes_v2.py (criado)
    - core/container.py (criado)
    - core/deps.py (simplificado)
  commits:
    - "refactor: extract DI container from deps.py"
  errors_resolved:
    - "circular import api.v1.routes <> core.deps"
  decisions:
    - "User aprovou DI container pattern"
    - "User quer pytest, nao unittest"
  pending:
    - "Escrever testes para container.py"
    - "Remover routes.py original apos testes passarem"
```

## Fronteira com Outros Kinds

| Kind | Diferenca |
|------|-----------|
| session_state (P10) | Snapshot efemero do estado atual — nao comprime, captura |
| runtime_state (P10) | Estado mental do agente — persiste entre sessoes |
| learning_record (P10) | O que deu certo/errado — acumula patterns, nao comprime conversa |

## Anti-Patterns

- Comprimir antes de 50% do context window (desperdicio — informacao ainda cabe)
- Descartar file paths modificados na compressao (perde rastreabilidade)
- Usar max_tokens > 1000 (summary vira quase tao grande quanto o original)
- Comprimir tool outputs brutos ao inves de extrair apenas o relevante
- Nao preservar decisoes do user (leva a re-perguntas)

## Referencias

- schema: P10/_schema.yaml (memory_summary)
- related: p10_ss_session_state, p10_rs_runtime_state
