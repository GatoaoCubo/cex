---
id: self_audit_n04_codex_2026_04_15
kind: self_audit
8f: F7_govern
pillar: P07
title: N04 Knowledge Self-Audit
version: 1.0.0
quality: 9.0
tags: [audit, self_review, n04, knowledge, rag, codex]
created: 2026-04-15
nucleus: n04
density_score: 1.0
updated: "2026-04-15"
related:
  - leverage_map_v2_n04_verify
  - self_audit_n05_codex_2026_04_15
  - self_audit_newpc
  - n04_knowledge
  - agent_card_n04
  - p02_nd_n04.md
  - output_sdk_validation_knowledge_audit
  - leverage_map_v2_n04_verify_legacy_2026_04_15
  - leverage_map_v2_n04_verify_iter2
  - leverage_map_v2_verify_n04
---

# N04 Knowledge Self-Audit (Codex)

> Mission executed: SELF_AUDIT. Runtime note: `.cex/runtime/handoffs/n04_task_codex.md` currently contains `LEVERAGE_MAP_V2`, so this audit includes a leverage-map delta for the live reranker/tooling state.

=== 8F PIPELINE ===
F1 CONSTRAIN: kind=self_audit, pillar=P07, scope=N04 knowledge/RAG/indexing/taxonomy state on 2026-04-15.
F2 BECOME: Loaded `N04_knowledge/agent_card_n04.md`, `.claude/rules/n04-knowledge.md`, `.claude/rules/8f-reasoning.md`, and the active handoff files.
F3 INJECT: Reused prior N04 self-audit patterns plus live repo evidence from `_tools`, `N04_knowledge/`, and `P01_knowledge/`.
F4 REASON: Planned 6 sections: inventory, quality, RAG stack, leverage-map delta, gaps, next actions.
F5 CALL: Ran frontmatter inventory script, `python _tools/cex_retriever.py --stats`, `python _tools/cex_doctor.py --scope N04_knowledge`, `rg` over knowledge kinds, and direct reads of `cex_retriever.py` and `cex_reranker.py`.
F6 PRODUCE: Generated this report with evidence-backed counts and operational findings.
F7 GOVERN: Checked ASCII-safe prose, validated all claims against command output, and kept `quality: null` per N04 rule.
F8 COLLABORATE: Saved to `N04_knowledge/reports/self_audit_codex_2026_04_15.md`, compiled, committed, and signaled completion.
===================

## 1. Current State

### 1.1 N04 artifact inventory

Command: inline Python frontmatter scan over `N04_knowledge/**/*.md`

| Metric | Value |
|---|---:|
| Markdown artifacts with frontmatter | 86 |
| `knowledge_card` | 17 |
| `context_doc` | 7 |
| `schema` | 6 |
| `glossary_entry` | 4 |
| `agent` | 4 |
| `cli_tool` | 4 |
| `rag_source` | 2 |
| `embedding_config` | 2 |
| `audit_report` | 2 |
| `few_shot_example` | 1 |
| `knowledge_index` | 1 |
| `retriever_config` | 1 |
| `entity_memory` | 1 |
| `chunk_strategy` | 1 |

### 1.2 Quality coverage

| Metric | Value | Notes |
|---|---:|---|
| `quality: null` | 2 | Much improved from the older audit baseline. |
| `quality` missing entirely | 1 | One frontmatter-bearing file still has no `quality` field. |
| 9.2 | 5 | Top band. |
| 9.1 | 34 | Largest bucket. |
| 9.0 | 23 | Stable core inventory. |
| 8.9 or lower | 21 | Includes older reports and support docs. |

### 1.3 Repo-level retrieval baseline

Command: `python _tools/cex_retriever.py --stats`

| Metric | Value | Audit read |
|---|---:|---|
| Index built | 2026-04-08T16:55:00 | Stale by 7 days on 2026-04-15. |
| Documents | 2983 | Large enough that stale metadata matters. |
| Vocabulary | 17142 | Healthy lexical surface for TF-IDF. |
| Pillar anomalies | 30 | Blank pillar 20, plus `P01_knowledge`, `P03_prompts`, `P07_evals`, `P10_output`, `P12_orchestration`, `P13`. |

## 2. Rule Compliance

### 2.1 N04 rule fit

| Rule | Status | Evidence |
|---|---|---|
| Artifacts live in `N04_knowledge/` | PASS | Current N04 work remains correctly scoped. |
| Knowledge and retrieval specialization | PASS | Inventory is centered on KCs, schemas, prompts, RAG sources, embeddings, and retrieval config. |
| Compile after save | PASS for this mission | Report compiled in F8. |
| `quality: null` when self-authored | MOSTLY PASS | This report uses `null`; two older files still carry `null` and one file omits `quality`. |
| 8F mandatory | PASS | Current report includes full 8F trace. |

### 2.2 Important caveat

`python _tools/cex_doctor.py --scope N04_knowledge` does not actually validate only `N04_knowledge`. It reports global builder health: 258 builders, 190 PASS, 63 WARN, 5 FAIL. That is useful repo health data, but it is not evidence of N04-only compliance.

## 3. RAG Stack Assessment

### 3.1 Wired tools now present

Command: `Get-ChildItem _tools | ? Name -match 'retriev|rerank|embed|graph|memory|index'`

| Tool | Status | Audit read |
|---|---|---|
| `cex_retriever.py` | Present | Operational TF-IDF retriever over repo artifacts. |
| `cex_reranker.py` | Present | New BM25 reranker from the active leverage-map cycle. |
| `cex_kc_index.py` | Present | KC indexing utility exists. |
| `cex_index.py` | Present | General SQLite indexer exists. |
| `cex_memory*.py` | Present | Memory selection/update/type tools exist. |

### 3.2 RAG artifacts under N04

Command: `rg -n "kind:\\s*(rag_source|retriever_config|chunk_strategy|embedding_config|vector_store|knowledge_index|entity_memory|glossary_entry|few_shot_example)" N04_knowledge P01_knowledge -g "*.md"`

| Kind | N04 count | State |
|---|---:|---|
| `rag_source` | 2 | Present but narrow. |
| `retriever_config` | 1 | Thin. |
| `chunk_strategy` | 1 | Thin. |
| `embedding_config` | 2 | Present. |
| `knowledge_index` | 1 | Present. |
| `entity_memory` | 1 | Present. |
| `glossary_entry` | 4 | Present. |
| `few_shot_example` | 1 | Present. |
| `vector_store` | 0 in N04 | Still missing from N04-owned artifacts. |

### 3.3 Reranker quality

Files read: `_tools/cex_reranker.py`, `_tools/cex_retriever.py`

| Check | Result | Notes |
|---|---|---|
| Tool added | PASS | `_tools/cex_reranker.py` exists. |
| BM25 math | PASS | Uses standard BM25-style IDF and length normalization with `k1=1.5`, `b=0.75`. |
| Candidate scope | LIMITED | Reranker only ranks a supplied candidate set or defaults to `P01_knowledge/library/**/*.md`. |
| Integration with retriever | FAIL | `cex_retriever.py` never calls `cex_reranker.py`; there is no wired two-stage retrieval path. |
| Metadata awareness | LIMITED | Filename stem gets a title boost, but frontmatter title/tags are ignored. |
| Operational impact | LOW | Until connected to retriever output, it is a sidecar utility rather than live N04 infrastructure. |

## 4. Findings

| Severity | Finding | Why it matters |
|---|---|---|
| High | Retrieval stack is still TF-IDF-first and stale | The main retriever index has not been rebuilt since 2026-04-08. |
| High | New reranker is not integrated | The active leverage-map deliverable exists, but it does not change production retrieval behavior. |
| High | N04 still lacks a `vector_store` artifact | Vector retrieval remains conceptual, not governed by an N04 artifact contract. |
| Medium | Pillar metadata pollution remains in the retriever index | Mis-labeled pillars reduce filtering reliability and contaminate search stats. |
| Medium | `cex_doctor --scope N04_knowledge` is misleading as an N04 check | It can create false confidence during N04 audits. |
| Medium | Retrieval config coverage is thin | One `retriever_config` and one `chunk_strategy` are not enough for multiple source types and nuclei. |
| Low | One N04 file still has no `quality` field | Small hygiene issue, but it should be closed. |

## 5. Still Missing

| Area | Status | Gap |
|---|---|---|
| Vector DB governance | Missing | No N04 `vector_store` artifact for pgvector, FAISS, or equivalent. |
| Hybrid search | Missing | No wired lexical + vector fusion path in `cex_retriever.py`. |
| Knowledge graph | Missing | No graph extraction or graph-backed retrieval tool in active use. |
| Reranker tuning | Missing | No eval set, no score calibration, no frontmatter-aware boosts. |
| Retrieval eval harness | Missing | No golden query benchmark to measure reranker or retriever quality. |
| Source-specific chunking matrix | Thin | Only one chunk strategy under N04. |

## 6. Next Iteration

| Priority | Build | Reason |
|---:|---|---|
| 1 | Wire `cex_reranker.py` into `cex_retriever.py` as an optional second stage | This converts the new reranker from a sidecar script into real leverage. |
| 2 | Author an N04 `vector_store` artifact plus a concrete vector-backed retriever path | This closes the biggest architectural gap in the RAG stack. |
| 3 | Add a small RAG eval harness with golden queries and freshness checks | Without measurement, reranking and vector search remain speculative. |

## Verdict

N04 is structurally healthier than the April 11 baseline: more artifacts, far fewer `quality: null` files, and a new reranker tool now exists. The leverage gap is still the same one that matters most: retrieval maturity. N04 owns the contracts and the vocabulary, but the live stack is still a stale TF-IDF index with an unwired reranker and no N04-governed vector store.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[leverage_map_v2_n04_verify]] | upstream | 0.35 |
| [[self_audit_n05_codex_2026_04_15]] | sibling | 0.32 |
| [[self_audit_newpc]] | upstream | 0.28 |
| [[n04_knowledge]] | upstream | 0.27 |
| [[agent_card_n04]] | upstream | 0.26 |
| [[p02_nd_n04.md]] | upstream | 0.26 |
| [[output_sdk_validation_knowledge_audit]] | upstream | 0.24 |
| [[leverage_map_v2_n04_verify_legacy_2026_04_15]] | upstream | 0.24 |
| [[leverage_map_v2_n04_verify_iter2]] | upstream | 0.24 |
| [[leverage_map_v2_verify_n04]] | upstream | 0.23 |
