---
id: p12_ckpt_rag_pipeline_step3
kind: checkpoint
8f: F8_collaborate
pillar: P12
title: "RAG Ingest Pipeline Checkpoint — Step 3 Embed After 847 Documents"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: orchestration
quality: 9.1
tags: [checkpoint, rag, pipeline, resumable, state-snapshot]
tldr: "Snapshot do pipeline RAG ingest apos step 3 (embed): 847 docs processados, 3 falharam, resumable=true para continuar sem reprocessar"
when_to_use: "Quando pipelines longos precisam de recovery points para retomar sem perder progresso"
keywords: [checkpoint, rag-pipeline, resumable, state-snapshot, recovery]
name: rag_pipeline_step3_embed
workflow_ref: rag_ingest_pipeline
step: "3_embed"
density_score: 1.0
related:
  - bld_architecture_checkpoint
  - checkpoint-builder
  - bld_collaboration_checkpoint
  - p01_kc_checkpoint
  - p03_sp_checkpoint_builder
  - bld_examples_checkpoint
  - bld_instruction_checkpoint
  - bld_schema_checkpoint
  - bld_output_template_checkpoint
  - p12_checkpoint
---

## TL;DR

Checkpoint captura o estado exato do pipeline `rag_ingest` apos completar step 3 (embedding generation). Com 847 documentos processados com sucesso e 3 falhas, o checkpoint permite retomar do step 4 (index_update) sem reprocessar os 847 embeddings ja gerados.

## Conceito Central

Um checkpoint e um snapshot imutavel do estado de um workflow em um ponto especifico. Diferente de signal (evento simples "completei"), checkpoint captura TUDO necessario para retomar: contadores, filas parciais, arquivos intermediarios, e estado de erro.

O campo `resumable: true` indica que o pipeline pode continuar do checkpoint. Pipelines com `resumable: false` exigem re-execucao completa (ex: operacoes transacionais).

### Pipeline RAG Ingest (5 steps)

```
Step 1: CRAWL      -> Coletar documentos de sources
Step 2: PARSE      -> Extrair texto + metadata
Step 3: EMBED      -> Gerar embeddings (Ollama nomic-embed-text)  <-- CHECKPOINT AQUI
Step 4: INDEX      -> Atualizar FAISS index
Step 5: VALIDATE   -> Verificar retrieval accuracy
```

### Checkpoint State

```yaml
checkpoint:
  id: p12_ckpt_rag_pipeline_step3
  workflow_ref: rag_ingest_pipeline
  step: "3_embed"
  created_at: "2026-03-29T03:47:22Z"
  resumable: true

  state:
    docs_processed: 847
    docs_failed: 3
    docs_total: 850

    failed_docs:
      - id: "KC_research_agent_042"
        error: "OllamaConnectionError: timeout after 30s"
        retries: 3
      - id: "KC_knowledge_agent_089"
        error: "TokenLimitExceeded: 32768 > 8192 max_tokens"
        retries: 1
      - id: "KC_marketing_agent_BROKEN"
        error: "UTF8DecodeError: invalid byte 0xff at position 2847"
        retries: 1

    embeddings_generated:
      count: 847
      model: "nomic-embed-text"
      dimensions: 768
      storage: "records/core/brain/faiss_index/pending_vectors.npy"

    pipeline_metadata:
      started_at: "2026-03-29T02:00:00Z"
      step3_completed_at: "2026-03-29T03:47:22Z"
      elapsed_seconds: 6442
      memory_peak_mb: 2847

  resume_instructions:
    next_step: "4_index"
    skip_steps: [1, 2, 3]
    input_artifact: "pending_vectors.npy"
    retry_failed: true  # re-attempt failed docs in next run

  rollback:
    safe_to_rollback: true
    rollback_action: "rm pending_vectors.npy"
    note: "FAISS index not yet modified — safe to discard"
```

## Exemplo Pratico

**Cenario**: Pipeline rodando as 2h da manha (cron). Ollama cai no meio do step 3.

**Sem checkpoint**: Pipeline inteiro recomeca — re-crawl 850 docs, re-parse, re-embed tudo. ~2h desperdicadas.

**Com checkpoint**: Ao reiniciar:
```python
ckpt = load_checkpoint("p12_ckpt_rag_pipeline_step3")

if ckpt and ckpt["resumable"]:
    # Skip steps 1-3, start from step 4
    pending = load_artifact(ckpt["resume_instructions"]["input_artifact"])
    run_step4_index(pending)

    # Retry failed docs separately
    if ckpt["resume_instructions"]["retry_failed"]:
        failed = ckpt["state"]["failed_docs"]
        retry_embed(failed)  # only 3 docs, not 850
```

**Recovery time**: 3 docs re-embed (~10s) + step 4 index (~30s) + step 5 validate (~15s) = **~55s** vs ~2h.

## Fronteira com Outros Kinds

| Kind | Diferenca |
|------|-----------|
| signal (P12) | Evento simples ("completei step 3") — sem estado detalhado |
| session_state (P10) | Estado de sessao interativa — nao de pipeline |
| workflow (P12) | Define os steps — checkpoint captura estado ENTRE steps |
| runtime_state (P10) | Estado mental do agente — nao de pipeline de dados |

## Anti-Patterns

- Checkpoint a cada documento (overhead > beneficio para docs pequenos)
- Armazenar embeddings inteiros no checkpoint YAML (use artifact path)
- Checkpoint sem `rollback` info (impossivel desfazer com seguranca)
- `resumable: true` em pipelines transacionais (half-committed state = corrupcao)
- Nao registrar `failed_docs` (impossivel retry sem reprocessar tudo)

## Referencias

- schema: P12/_schema.yaml (checkpoint)
- related: p12_wf_rag_ingest, p12_sig_step_complete

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_checkpoint]] | upstream | 0.50 |
| [[checkpoint-builder]] | related | 0.50 |
| [[bld_collaboration_checkpoint]] | related | 0.45 |
| [[p01_kc_checkpoint]] | related | 0.44 |
| [[p03_sp_checkpoint_builder]] | upstream | 0.43 |
| [[bld_examples_checkpoint]] | upstream | 0.42 |
| [[bld_instruction_checkpoint]] | upstream | 0.42 |
| [[bld_schema_checkpoint]] | upstream | 0.38 |
| [[bld_output_template_checkpoint]] | upstream | 0.38 |
| [[p12_checkpoint]] | sibling | 0.38 |
