---
id: n00_p10_kind_index
kind: knowledge_card
pillar: P10
nucleus: n00
title: "P10 Memory -- Kind Index"
version: 1.0
quality: 9.0
tags: [index, p10, archetype, n00]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Master index of all 18 kinds in pillar P10. Reference for /mentor, nucleus builders, and the 8F pipeline.

## Pillar: P10 Memory
State persistence and context management: entity memories, knowledge indexes, session state, memory summaries, and provenance records. The temporal layer that gives agents continuity across interactions.

## Kinds in P10

| Kind | Purpose | Primary Nucleus | Builder |
|------|---------|-----------------|---------|
| `agent_grounding_record` | Per-inference provenance record: tool calls, RAG chunks, model signatu | N04 | `agent_grounding_record-builder` |
| `c2pa_manifest` | C2PA 2.3 content credential for AI-generated media: claim, assertions, | N04 | `c2pa_manifest-builder` |
| `compression_config` | Context compression configuration for tool outputs | N04 | `compression_config-builder` |
| `consolidation_policy` | Memory lifecycle management policy | N04 | `consolidation_policy-builder` |
| `entity_memory` | Memoria sobre entidades | N04 | `entity_memory-builder` |
| `knowledge_index` | Search index (BM25, FAISS config) | N04 | `knowledge_index-builder` |
| `learning_record` | Learning record (what worked/failed) | N04 | `learning_record-builder` |
| `memory_architecture` | Complete memory system architecture design | N04 | `memory_architecture-builder` |
| `memory_summary` | Compressed memory summary | N04 | `memory_summary-builder` |
| `memory_type` | Classification of persistent memory by source, confidence, and decay r | N04 | `memory_type-builder` |
| `model_registry` | Model versioning and artifact tracking | N04 | `model_registry-builder` |
| `procedural_memory` | Skill and procedure storage/retrieval system | N04 | `procedural_memory-builder` |
| `prompt_cache` | TTL, eviction, and invalidation config for cached LLM prompt/completio | N04 | `prompt_cache-builder` |
| `runtime_state` | Estado mental variavel por sessao (routing, decisoes em runtime) | N04 | `runtime_state-builder` |
| `session_backend` | Per-user session state persistence backend | N04 | `session_backend-builder` |
| `session_state` | Session state (ephemeral, snapshot) | N04 | `session_state-builder` |
| `vc_credential` | W3C Verifiable Credential 2.0 for AI agent identity, provenance attest | N04 | `vc_credential-builder` |
| `workflow_run_crate` | RO-Crate 1.2 Workflow Run Crate: scientific workflow execution provena | N04 | `workflow_run_crate-builder` |

## Usage
```python
# Build any of these via 8F:
python _tools/cex_8f_runner.py "your intent" --kind {kind} --execute
```

## CoC Hierarchy Note
These 18 kinds follow the convention-over-configuration hierarchy: each instance
(N01-N07) inherits this schema and fills the variables for its sin lens.
N00_genesis holds the canonical archetype; nuclei hold the instantiated versions.
