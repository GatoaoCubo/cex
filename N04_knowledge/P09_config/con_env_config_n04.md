---
id: con_env_config_n04
kind: env_config
8f: F1_constrain
pillar: P09
nucleus: n04
title: Knowledge Environment Config
version: 1.0
quality: 9.0
tags: [config, env, knowledge, indexing, retrieval]
density_score: 1.0
related:
  - bld_examples_kind
  - env-config-builder
  - bld_collaboration_env_config
  - n04_agent_embedding_engineer
  - bld_knowledge_card_env_config
  - bld_schema_env_config
  - bld_examples_env_config
  - self_audit_n04_codex_2026_04_15
  - p03_sp_env_config_builder
  - bld_instruction_env_config
---
<!-- 8F: F1 constrain=P09/env_config F2 become=env-config-builder F3 inject=n04-knowledge+kc_env_config+P09 examples+repo env hints F4 reason=environment catalog for knowledge indexing and retrieval control F5 call=shell,apply_patch F6 produce=5269 bytes F7 govern=frontmatter+ascii+density+80-line self-check F8 collaborate=N04_knowledge/P09_config/con_env_config_n04.md -->
# Knowledge Environment Config
## Purpose
N04 uses environment variables to tune ingestion appetite, retrieval precision, and freshness behavior without rewriting artifacts.
The Knowledge Gluttony lens favors collecting enough knobs to observe and steer knowledge flow, while still naming each variable precisely enough to prevent configuration sprawl.
This config defines the canonical environment catalog for N04 runtime behavior.
## Values
| Variable | Type | Required | Default | Scope | Sensitivity | Purpose |
|----------|------|----------|---------|-------|-------------|---------|
| `N04_INDEX_ENABLED` | bool | no | `true` | all | low | master switch for index writes |
| `N04_EMBEDDING_MODEL` | string | yes | `text-embedding-3-large` | all | low | embedding model identity |
| `N04_CHUNK_TARGET` | int | no | `900` | all | low | target chunk size in chars or tokens by policy |
| `N04_CHUNK_OVERLAP` | int | no | `120` | all | low | overlap to preserve local context |
| `N04_MAX_PROVENANCE_PER_RECORD` | int | no | `8` | all | low | cap on source entries retained inline |
| `N04_FRESHNESS_DEFAULT_DAYS` | int | no | `30` | all | low | default review horizon |
| `N04_STALE_AFTER_DAYS` | int | no | `90` | all | low | stale threshold for knowledge records |
| `N04_VECTOR_NAMESPACE` | string | yes | `n04_knowledge` | all | low | logical vector partition |
| `N04_RETRIEVAL_TOP_K` | int | no | `12` | all | low | default result set size |
| `N04_DEBUG_PROVENANCE` | bool | no | `false` | dev | low | reveal verbose provenance diagnostics |
## Source Of Truth
| Variable | Where defined | Override order |
|----------|---------------|----------------|
| all `N04_*` vars | `.env`, shell env, deployment platform | runtime env > `.env` > documented default |
| secrets referenced here | secret store only | secret store > runtime injection |
## Validation Rules
| Variable | Rule | Reason |
|----------|------|-------|
| `N04_CHUNK_TARGET` | 200-4000 | chunk too small or too large hurts retrieval |
| `N04_CHUNK_OVERLAP` | 0-600 and `< N04_CHUNK_TARGET` | overlap must not exceed chunk size |
| `N04_MAX_PROVENANCE_PER_RECORD` | 1-20 | enough evidence without unbounded bloat |
| `N04_FRESHNESS_DEFAULT_DAYS` | 1-365 | review horizon must be finite |
| `N04_STALE_AFTER_DAYS` | `>= N04_FRESHNESS_DEFAULT_DAYS` | stale cannot precede review |
| `N04_RETRIEVAL_TOP_K` | 1-50 | retrieval fanout needs bounded cost |
## Rationale
| Decision | Knowledge Gluttony angle | Benefit |
|----------|--------------------------|---------|
| cap provenance inline | N04 wants many sources but also predictable record size | stable storage and prompts |
| expose chunk controls | appetite for context should be tunable by corpus type | better recall/precision tradeoff |
| separate review and stale vars | greedy indexing must still know when to revisit facts | automated freshness routines |
| keep debug provenance flag | investigators sometimes need maximal trace detail | dev observability without prod noise |
| namespace vector storage | hungry multi-nucleus systems need partition discipline | less cross-domain contamination |
## Example
```env
N04_INDEX_ENABLED=true
N04_EMBEDDING_MODEL=text-embedding-3-large
N04_CHUNK_TARGET=900
N04_CHUNK_OVERLAP=120
N04_MAX_PROVENANCE_PER_RECORD=8
N04_FRESHNESS_DEFAULT_DAYS=30
N04_STALE_AFTER_DAYS=90
N04_VECTOR_NAMESPACE=n04_knowledge
N04_RETRIEVAL_TOP_K=12
N04_DEBUG_PROVENANCE=false
```
## Example Interpretation
| Setting | Effect |
|---------|--------|
| indexing enabled | N04 persists new vectors and metadata |
| 900 target with 120 overlap | moderately dense chunking for mixed docs |
| provenance cap 8 | enough witness detail for audits |
| stale after 90 | records enter refresh workflow after quarter-scale age |
| top_k 12 | retrieval prefers breadth with bounded cost |
## Consumers
| Consumer | Usage |
|----------|-------|
| embedding batch processor | reads model and chunk controls |
| taxonomy builder | uses freshness defaults for recrawl planning |
| validator | checks env values against safe ranges |
| retriever | uses top_k and namespace |
## Dependencies
| Depends on | Why |
|------------|-----|
| secret config | provider credentials for embedding and vector services |
| rate limit config | provider call budgets and quotas |
| path config | local cache, export, and index directories |
## Properties
| Property | Value |
|----------|-------|
| Config scope | N04 runtime |
| Variable count | 10 |
| Secret values included | no |
| Override model | env-first |
| Freshness variables | 2 |
| Retrieval variables | 2 |
| Chunking variables | 2 |
| Provenance variables | 1 |
| Debug variables | 1 |
| Governance mode | validator-backed |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_kind]] | upstream | 0.25 |
| [[env-config-builder]] | related | 0.25 |
| [[bld_collaboration_env_config]] | downstream | 0.24 |
| [[n04_agent_embedding_engineer]] | upstream | 0.23 |
| [[bld_knowledge_card_env_config]] | upstream | 0.23 |
| [[bld_schema_env_config]] | upstream | 0.23 |
| [[bld_examples_env_config]] | upstream | 0.23 |
| [[self_audit_n04_codex_2026_04_15]] | upstream | 0.23 |
| [[p03_sp_env_config_builder]] | upstream | 0.23 |
| [[bld_instruction_env_config]] | upstream | 0.23 |
