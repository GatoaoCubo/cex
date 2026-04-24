---
id: p10_mt_n04_knowledge
kind: memory_type
8f: F3_inject
pillar: P02
nucleus: n04
title: "Memory Type -- N04 Memory Classification System"
version: "1.0.0"
quality: 9.1
tags: [memory_type, n04, classification, correction, preference, convention, context, P10]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "Four-type memory taxonomy for N04: correction (what not to do again), preference (how to do things), convention (standards to follow), context (background to carry). Maps to cex_memory_types.py implementation."
density_score: null
related:
  - agent_card_n04
  - self_audit_n04_codex_2026_04_15
  - bld_collaboration_supabase_data_layer
  - bld_system_prompt_memory_type
  - bld_architecture_supabase_data_layer
  - p01_kc_supabase_data_layer_n04
  - bld_manifest_memory_type
  - bld_collaboration_memory_type
  - p01_kc_vector_embedding_model_selection
  - p12_mission_supabase_data_layer
---

# Memory Type: N04 Memory Classification System

## Overview

N04 uses a 4-type memory taxonomy (implemented in `cex_memory_types.py`).
Every memory entry is classified into one type -- no ambiguity, no overlap.

| Type | Question | Examples |
|------|---------|---------|
| `correction` | What did N04 do WRONG that must not recur? | Wrong embedding dimension, bad chunk size, wrong corpus |
| `preference` | How does N04 (or the user) prefer things done? | Hybrid retrieval over dense-only, passages over summaries |
| `convention` | What standards govern N04's domain? | KC frontmatter schema, naming patterns, quality targets |
| `context` | What background facts does N04 need? | Current corpus size, active Supabase project, brand config |

---

## Type 1: Correction

**Purpose**: prevent known failure modes from recurring.
**Source**: errors caught at F7 GOVERN, user feedback, retrieval failures.
**Persistence**: permanent (corrections don't expire).
**Storage**: `N04_knowledge/P10_memory/` named `correction_{topic}.md`

### Active Corrections

| ID | Correction | Root Cause | Learned Date |
|----|-----------|-----------|-------------|
| C01 | Always check embedding dimension before upsert -- pgvector fails silently on mismatch | Dimension mismatch on ada-002->3-small migration | ongoing |
| C02 | Do not index uncompiled .md files -- compile first | Stale content found in retrieval results | ongoing |
| C03 | Query expansion (HyDE) increases latency 3x -- only use on multi-hop reasoning tasks | Latency regression found in smoke tests | ongoing |
| C04 | ChromaDB L2 distance != cosine similarity -- convert: sim = 1 - (dist/2) | Wrong scoring in hybrid merge | ongoing |
| C05 | Do not load full P01_knowledge/ into context -- use semantic search top-5 | Context overflow in early sessions | ongoing |

---

## Type 2: Preference

**Purpose**: capture preferred approaches that optimize for quality, speed, or user satisfaction.
**Source**: positive outcomes, user confirmations, validated experiment results.
**Persistence**: 180-day TTL, reset on re-confirmation.
**Storage**: `.claude/projects/.../memory/feedback_*.md`

### Active Preferences

| ID | Preference | Why | Confidence |
|----|-----------|-----|-----------|
| P01 | Hybrid retrieval (dense + BM25) over dense-only | +12% recall at same precision | HIGH |
| P02 | Return `passages` format over `full_docs` by default | Reduces context token waste 4x | HIGH |
| P03 | Apply cross-encoder reranking on top-20 | +8% MRR, worth the latency | HIGH |
| P04 | text-embedding-3-small over ada-002 | Better performance, same cost | HIGH |
| P05 | Chunk KCs as whole documents (< 8KB) | Chunk boundaries damage KC coherence | MEDIUM |

---

## Type 3: Convention

**Purpose**: codify domain standards and schemas that all N04 artifacts must follow.
**Source**: builder schemas, pillar contracts, architectural decisions.
**Persistence**: permanent (conventions change only via architectural decision).
**Storage**: `N04_knowledge/P06_schema/` or `N00_genesis/P{xx}/`

### Active Conventions

| ID | Convention | Reference |
|----|-----------|---------|
| V01 | KC frontmatter: id, kind, pillar, nucleus, title, version, quality, tags, domain, tldr | `kc_structure_contract.md` |
| V02 | quality: null in all new artifacts (never self-score) | `8f-reasoning.md` F7 |
| V03 | knowledge_card IDs follow pattern `kc_{name}` | `naming_convention_mapping.md` |
| V04 | All compiled YAML goes to archetypes/builders/{kind}-builder/compiled/ | `cex_compile.py` contract |
| V05 | Embeddings: 1536 dim (text-embedding-3-small), NOT 1024 or 3072 unless specified | `embedding_config_knowledge.md` |
| V06 | BM25 fallback always available (no dependency on external service for sparse) | `retriever_config_knowledge.md` |

---

## Type 4: Context

**Purpose**: background facts about the current system state that inform N04's behavior.
**Source**: session start, system checks, N07 signals.
**Persistence**: short TTL (24-48h) -- context changes frequently.
**Storage**: `.cex/runtime/` or loaded fresh via cex_prompt_layers.py

### Current Context (2026-04-17)

| Key | Value | TTL |
|-----|-------|-----|
| corpus_size | 2184 documents (cex_retriever TF-IDF) | 7 days |
| primary_vector_store | pgvector (Supabase) | until changed |
| embedding_model | text-embedding-3-small (1536 dim) | until changed |
| bootstrap_status | not bootstrapped | session |
| n07_mission | SELF_ASSEMBLY W1 | this session |
| active_nuclei | N01-N06 parallel | this wave |

---

## Classification Algorithm

When a new memory candidate arrives:

```
IF "N04 did X wrong / should not do X again" -> correction
IF "N04 / user prefers X over Y" -> preference
IF "artifact must follow standard X" -> convention
IF "current state is X" -> context
```

Ambiguity resolution:
- Correction vs Preference: correction = about a PAST error; preference = about future default
- Convention vs Preference: convention = mandatory (schema); preference = advisory (style)
- Context vs Correction: context = state fact; correction = behavioral rule

---

## Integration

| Tool | Role |
|------|------|
| `cex_memory_types.py` | Runtime implementation of this taxonomy |
| `cex_memory_age.py` | TTL management for context-type memories |
| `cex_memory_select.py` | Retrieves memories by type for session injection |
| `cex_memory_update.py` | Append, decay, and prune operations per type |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_n04]] | upstream | 0.29 |
| [[self_audit_n04_codex_2026_04_15]] | downstream | 0.26 |
| [[bld_collaboration_supabase_data_layer]] | downstream | 0.24 |
| [[bld_system_prompt_memory_type]] | related | 0.23 |
| [[bld_architecture_supabase_data_layer]] | related | 0.23 |
| [[p01_kc_supabase_data_layer_n04]] | upstream | 0.22 |
| [[bld_manifest_memory_type]] | related | 0.22 |
| [[bld_collaboration_memory_type]] | downstream | 0.22 |
| [[p01_kc_vector_embedding_model_selection]] | upstream | 0.22 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.21 |
