---
id: p12_sched_daily_reindex
kind: schedule
pillar: P12
title: "Daily Reindex Schedule — Nightly Brain FAISS Rebuild"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: orchestration
quality: 9.0
tags: [schedule, cron, reindex, faiss, nightly, automation]
tldr: "Cron diario as 02:00 UTC que rebuilda o FAISS index do Brain MCP a partir de KCs novos/modificados"
when_to_use: "Quando workflows precisam rodar em horarios fixos sem trigger humano"
keywords: [schedule, cron-trigger, daily-reindex, faiss-rebuild, automation]
name: daily_reindex
trigger_type: cron
cron: "0 2 * * *"
timezone: UTC
workflow_ref: rag_reindex_pipeline
density_score: null
---

## TL;DR

Schedule que dispara o workflow `rag_reindex_pipeline` todo dia as 02:00 UTC (23:00 BRT). Rebuilda o indice FAISS do Brain MCP incorporando Knowledge Cards novos ou modificados nas ultimas 24h. Execution window: ~20 min. Zero downtime — hot-swap do index file.

## Conceito Central

Um schedule e um trigger temporal que inicia um workflow. Nao contem logica de execucao — apenas QUANDO rodar e O QUE rodar. A logica vive no workflow referenciado.

O `trigger_type: cron` usa sintaxe cron padrao POSIX. Alternativas incluem `interval` (a cada N minutos), `event` (quando arquivo muda), e `manual` (trigger explicito).

### Configuracao Completa

```yaml
schedule:
  id: p12_sched_daily_reindex
  trigger_type: cron
  cron: "0 2 * * *"     # diario as 02:00
  timezone: UTC          # = 23:00 BRT

  workflow_ref: rag_reindex_pipeline

  execution:
    timeout_minutes: 45
    retry_on_failure: true
    max_retries: 2
    retry_delay_minutes: 15
    concurrency: 1       # never run 2 reindex in parallel

  preconditions:
    - check: ollama_running
      command: "curl -s http://localhost:11434/api/tags | jq '.models | length'"
      expected: "> 0"
      on_fail: start_ollama

    - check: disk_space
      command: "df -h /c/Users/PC/Documents/GitHub/organization-core | awk 'NR==2 {print $5}'"
      expected: "< 90%"
      on_fail: abort_with_alert

  notifications:
    on_success:
      - type: file
        path: ".claude/signals/reindex_complete_{date}.json"
    on_failure:
      - type: file
        path: ".claude/signals/reindex_failed_{date}.json"
      - type: log
        message: "ALERT: Daily reindex failed after {retries} retries"

  window:
    preferred_start: "02:00"
    preferred_end: "02:45"
    blackout_dates:
      - "2026-04-01"  # deploy freeze
```

## Exemplo Pratico

**Dia tipico** (2026-03-29):

```
23:00 BRT (02:00 UTC) — Cron trigger fires
  |
  +-- Precondition: Ollama running? YES (nomic-embed-text loaded)
  +-- Precondition: Disk < 90%? YES (67% used)
  |
  +-- Start workflow: rag_reindex_pipeline
  |     Step 1: Scan KCs modified since last reindex
  |             -> Found: 12 new KCs, 3 modified, 0 deleted
  |     Step 2: Generate embeddings for 15 KCs
  |             -> 15/15 embedded (nomic-embed-text, 768 dims)
  |     Step 3: Merge into existing FAISS index
  |             -> Index: 1957 -> 1972 vectors
  |     Step 4: Hot-swap index file
  |             -> faiss_index.bin renamed, new file written
  |     Step 5: Validate with 3 test queries
  |             -> 3/3 queries return relevant results
  |
  +-- Duration: 18m 42s
  +-- Signal: reindex_complete_20260329.json written

23:19 BRT — Complete. Brain MCP now serves updated index.
```

**Failure scenario** (Ollama crashed):

```
02:00 UTC — Cron fires
  +-- Precondition: Ollama running? NO
  +-- Action: start_ollama
  +-- Wait 30s, recheck: YES
  +-- Start workflow...
  |     Step 2: Embed -> OllamaError on KC #7
  |     Retry 1: Success after Ollama restart
  +-- Duration: 32m 15s (longer due to restart)
  +-- Signal: reindex_complete_20260329.json
```

## Fronteira com Outros Kinds

| Kind | Diferenca |
|------|-----------|
| workflow (P12) | Define OS STEPS do pipeline — schedule define QUANDO rodar |
| dispatch_rule (P12) | Roteia baseado em KEYWORD — schedule roteia baseado em TEMPO |
| checkpoint (P12) | Snapshot do estado DURANTE execucao — schedule e trigger PRE-execucao |
| cron job (OS) | Implementacao — schedule e a especificacao declarativa |

## Anti-Patterns

- Cron sem timezone (ambiguidade entre UTC e local)
- `concurrency: unlimited` para reindex (2 rebuilds simultaneos = index corrupto)
- Sem preconditions (Ollama down = 20min de embeddings falhando)
- Sem timeout (reindex travado bloqueia proximo cron)
- Schedule diretamente com logica de execucao (mistura trigger com workflow)

## Referencias

- schema: P12/_schema.yaml (schedule)
- related: p12_wf_rag_reindex, p12_ckpt_rag_pipeline
