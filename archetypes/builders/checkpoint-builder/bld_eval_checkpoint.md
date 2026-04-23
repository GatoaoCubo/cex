---
kind: quality_gate
id: p11_qg_checkpoint
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of checkpoint artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: checkpoint"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, checkpoint, P12, workflow, resume, state]
tldr: "Pass/fail gate for checkpoint artifacts: workflow_ref presence, state schema, TTL declaration, resume protocol, and lifecycle policy."
domain: "workflow checkpoint — saved state snapshot enabling resumable, auditable workflow execution"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_checkpoint
  - p03_sp_checkpoint_builder
  - bld_instruction_checkpoint
  - bld_collaboration_checkpoint
  - checkpoint-builder
  - bld_architecture_checkpoint
  - bld_output_template_checkpoint
  - bld_schema_checkpoint
  - p11_qg_chain
  - bld_knowledge_card_checkpoint
---

## Quality Gate

# Gate: checkpoint
## Definition
| Field | Value |
|---|---|
| metric | checkpoint artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: checkpoint` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p12_ck_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, hyphens, or missing prefix |
| H03 | ID equals filename stem | `id: p12_ck_foo` but file is `p12_ckpt_bar.md` |
| H04 | Kind equals literal `checkpoint` | `kind: state` or `kind: snapshot` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `workflow_ref`, `step`, `tldr`, or `tags` |
| H07 | workflow_ref is non-empty string | `workflow_ref: ""` or field absent |
| H08 | step is non-empty string | `step: ""` or field absent |
| H09 | tags includes "checkpoint" | Tags list present but does not contain "checkpoint" |
| H10 | Body has all 4 required sections | Missing Overview, State, Resume, or Lifecycle section |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| State schema completeness | 1.0 | All state keys listed with type and size hint; no undocumented keys |
| Resume protocol clarity | 1.0 | Step-by-step resume instructions; prerequisites stated; re-entry point named |
| TTL declaration | 1.0 | ttl field present with valid value; justification if ttl: none |
| Lifecycle policy | 0.5 | Cleanup and archival policy declared; chain linkage documented |
| Idempotency declaration | 1.0 | Resume explicitly states whether re-running is safe and why |
| Boundary clarity | 1.0 | Explicitly not a signal, session_state, or workflow artifact |
| Retry modeling | 0.5 | retry_count field used; error field covers failure state |
| Chain linkage | 0.5 | parent_checkpoint referenced or null with explanation |
| Workflow alignment | 1.0 | step value matches a named step in the referenced workflow |
| Domain specificity | 1.0 | State keys, step name, and TTL specific to declared workflow domain |
| Serialization safety | 1.0 | State uses only safe serialization (yaml/json); no binary blobs in spec |
| Testability | 0.5 | Resume steps verifiable with known state; expected outcome documented |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Bootstrap checkpoint created during initial workflow scaffolding, not yet connected to a live workflow_ref |
| approver | Author self-certification with comment explaining bootstrap scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 7d — bootstrap checkpoints must be promoted to >= 7.0 or removed |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |

## Examples

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
quality: 8.9
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
