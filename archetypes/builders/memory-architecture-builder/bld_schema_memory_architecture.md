---
kind: schema
id: bld_schema_memory_architecture
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for memory_architecture
quality: 9.2
title: "Schema: memory_architecture"
version: "2.0.0"
author: n06_commercial
tags: [memory_architecture, builder, schema]
tldr: "Schema for LLM agent memory architecture artifacts: layer definitions, storage backends, eviction policies, tier matrix"
domain: "LLM agent memory systems"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_procedural_memory
  - bld_schema_sandbox_spec
  - bld_schema_audit_log
  - bld_schema_app_directory_entry
  - bld_schema_multimodal_prompt
  - bld_schema_eval_metric
  - bld_schema_consolidation_policy
---

## Frontmatter Fields

### Required

| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | null | Must match `^p10_marc_[a-z][a-z0-9_]+$` |
| kind | string | yes | "memory_architecture" | Fixed value |
| pillar | string | yes | "P10" | Fixed value |
| title | string | yes | null | Descriptive name for the memory architecture |
| version | string | yes | "1.0.0" | Semver |
| created | string | yes | null | ISO 8601 date |
| updated | string | yes | null | ISO 8601 date |
| author | string | yes | null | Nucleus or person responsible |
| domain | string | yes | null | Agent domain (e.g., "customer-support-agent") |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Keywords including memory layer types |
| tldr | string | yes | null | One-sentence summary of the architecture |
| layers | list | yes | [] | Active layers: [working, episodic, semantic, procedural] |
| tier | string | yes | null | Commercial tier: free, pro, enterprise |

### Recommended

| Field | Type | Notes |
|---|---|---|
| system_ref | string | Reference system (e.g., "memgpt", "zep", "mem0") |
| backend | dict | Storage backend per layer |
| retention_days | integer | Default retention period for episodic memory |
| consolidation_enabled | boolean | Whether sleep-time consolidation is active |

## ID Pattern

```
^p10_marc_[a-z][a-z0-9_]+$
```

Example IDs:
- `p10_marc_customer_support_v1`
- `p10_marc_research_agent_full`
- `p10_marc_minimal_working_only`

## Body Structure

1. **Overview** -- agent type, memory goals, scope statement
2. **Memory Layer Definitions** -- table: layer | backend | retention | tier_req
3. **Storage Backends** -- vector store, graph DB, KV store specs per layer
4. **Read Pipeline** -- retrieval flow: query -> rank -> inject into prompt
5. **Write Pipeline** -- generation -> extract -> classify -> store per layer
6. **Eviction Policy** -- LRU/LFU/TTL/importance-based per layer
7. **Commercial Tier Matrix** -- FREE/PRO/ENTERPRISE capability table
8. **Integration Points** -- consolidation_policy ref, procedural_memory ref

## Constraints

- `layers` must include at least `working` (minimum viable architecture).
- If `tier: enterprise`, MUST include compliance fields (retention_days, data_residency).
- `backend.episodic` must be a vector store (enables semantic search over history).
- `backend.semantic` must support entity lookup (graph DB or structured KV).
- Body MUST include the Commercial Tier Matrix table.
- quality MUST be null (never self-assign a score).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | sibling | 0.62 |
| [[bld_schema_reranker_config]] | sibling | 0.61 |
| [[bld_schema_benchmark_suite]] | sibling | 0.60 |
| [[bld_schema_procedural_memory]] | sibling | 0.59 |
| [[bld_schema_sandbox_spec]] | sibling | 0.59 |
| [[bld_schema_audit_log]] | sibling | 0.58 |
| [[bld_schema_app_directory_entry]] | sibling | 0.58 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.57 |
| [[bld_schema_eval_metric]] | sibling | 0.57 |
| [[bld_schema_consolidation_policy]] | sibling | 0.57 |
