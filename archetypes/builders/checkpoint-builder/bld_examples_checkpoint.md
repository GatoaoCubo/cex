---
kind: examples
id: bld_examples_checkpoint
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of checkpoint artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: checkpoint-builder
## Golden Example
INPUT: "Create checkpoint for the research_pipeline workflow at the embed_chunks step"
OUTPUT:
```yaml
id: p12_ck_research_pipeline_embed_chunks
kind: checkpoint
pillar: P12
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Research Pipeline — Embed Chunks"
workflow_ref: "p12_wf_research_pipeline"
step: "embed_chunks"
quality: null
tags: [checkpoint, research-pipeline, embedding, P12]
tldr: "Checkpoint after chunk embedding step: 3 state keys, 24h TTL, resumable at embed_chunks"
description: "Saves embedding progress after batch N chunks processed; enables resume without re-fetching sources."
state:
  chunks_processed: integer   # count of successfully embedded chunks
  embedding_model: string     # model id used (must match on resume)
  last_chunk_id: string       # id of last successfully embedded chunk
resumable: true
ttl: "24h"
parent_checkpoint: "p12_ck_research_pipeline_fetch_sources"
retry_count: 0
error: null
```
## Overview
Saves embedding progress at the embed_chunks step. Enables cost-efficient resume after failure without re-fetching source documents.
## State
| Key | Type | Description |
|-----|------|-------------|
| chunks_processed | integer | Count of successfully embedded chunks so far |
| embedding_model | string | Model id — must match on resume |
| last_chunk_id | string | UUID of last embedded chunk; resume starts at next |

Serialization: yaml. Total state budget: ~84 bytes.
## Resume
Prerequisites: embedding service available; same embedding_model present; source chunks accessible.

1. Load checkpoint `p12_ck_research_pipeline_embed_chunks`
2. Restore state: chunks_processed, embedding_model, last_chunk_id
3. Re-enter at `embed_chunks`, starting from chunk after last_chunk_id
4. Validate embedding_model matches current service version
5. Continue; write next checkpoint at validate_output

Idempotent: yes — skips already-processed chunks.
## Lifecycle
TTL: 24h — batch pipeline; checkpoint expires after workflow complete.
Chain: p12_ck_research_pipeline_fetch_sources -> this -> p12_ck_research_pipeline_validate_output

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches `^p12_ck_[a-z][a-z0-9_]+$` (H02 pass)
- kind: checkpoint (H04 pass)
- workflow_ref and step non-empty (H07, H08 pass)
- tags: 4 items, includes "checkpoint" (H09 pass)
- body has all 4 sections (H10 pass)
- state schema: 3 keys with type + description (SOFT pass)
- resume: prerequisites + numbered steps + idempotency (SOFT pass)
- TTL declared with justification (SOFT pass)
## Anti-Example
INPUT: "Create checkpoint for data pipeline"
BAD OUTPUT:
```yaml
id: data-pipeline-checkpoint
kind: state
workflow: pipeline
quality: 8.5
tags: [state]
```
Checkpoint for data pipeline step 3.
FAILURES:
1. id: "data-pipeline-checkpoint" has hyphens and no `p12_ck_` prefix -> H02 FAIL
2. kind: "state" not "checkpoint" -> H04 FAIL
3. quality: 8.5 (not null) -> H05 FAIL
4. Missing fields: pillar, version, created, updated, author, workflow_ref, step, tldr -> H06 FAIL
5. workflow_ref field absent -> H07 FAIL
6. step field absent -> H08 FAIL
7. tags: only 1 item, missing "checkpoint" -> H09 FAIL
8. Body missing Overview, State, Resume, Lifecycle sections -> H10 FAIL
9. No TTL — orphan checkpoint accumulates indefinitely -> SOFT FAIL
