---
id: self_audit_newpc_2026_04_12
kind: context_doc
title: N01 Self-Audit -- New PC Setup (2026-04-12)
pillar: P01_knowledge
nucleus: N01
version: 2.0.0
quality: 8.9
created: 2026-04-12
updated: 2026-04-12
mission: NEWPC_SETUP
---

# N01 Self-Audit -- New PC Setup (v2)

**Machine**: Windows 11 Pro 10.0.26200
**Date**: 2026-04-12
**Python**: 3.14.4 (numpy 2.4.4, sklearn 1.8.0)
**Node**: npx 11.11.0
**UV**: uvx 0.11.6
**Doctor**: 124 PASS | 0 WARN | 0 FAIL

---

## Phase 1: MCP Server Verification

| # | Server | Binary | API Key | Verdict | Notes |
|---|--------|--------|---------|---------|-------|
| 1 | firecrawl | npx 11.11.0 [OK] | FIRECRAWL_API_KEY **NOT SET** | **FAIL** | Binary works, key missing |
| 2 | fetch | uvx 0.11.6 [OK] | n/a | **PASS** | No key required |
| 3 | markitdown | npx 11.11.0 [OK] | n/a | **PASS** | No key required |
| 4 | brave-search | npx 11.11.0 [OK] | BRAVE_API_KEY **NOT SET** | **FAIL** | Binary works, key missing |
| 5 | notebooklm | npx 11.11.0 [OK] | n/a | **PASS** | No key required |

**Score: 3/5 PASS**

### Impact Analysis

| Server | Research Capability Lost | Alternative | Severity |
|--------|------------------------|-------------|----------|
| firecrawl | Structured web extraction (competitor sites, pricing pages) | fetch (raw HTML, no structured extraction) | MEDIUM -- fetch covers 60% of use cases |
| brave-search | Real-time web search for competitive intelligence | Claude Code WebSearch tool (available) | LOW -- WebSearch is a viable fallback |

**vs. Prior Audit (v1)**: Same 2 keys missing. These are optional -- all 3 keyless MCP servers work. The WebSearch fallback for brave-search was not noted in v1; it reduces effective severity.

---

## Phase 2: Python Tools Audit

### Tool Health

| Tool | --help | Runtime | Verdict | vs. v1 |
|------|--------|---------|---------|--------|
| cex_retriever.py | [OK] | [OK] (2983 docs, 17K vocab) | **PASS** | FIXED (was FAIL) |
| cex_compile.py | [OK] | [OK] | **PASS** | Same |
| cex_doctor.py | [OK] | [OK] (124 PASS, 0 FAIL) | **PASS** | Same |

### Python Package Status

| Package | Status | vs. v1 |
|---------|--------|--------|
| numpy | 2.4.4 [OK] | FIXED (was MISSING) |
| scikit-learn | 1.8.0 [OK] | FIXED (was MISSING) |
| tiktoken | [OK] | Same |
| anthropic | [OK] | Same |
| pyyaml | [OK] | Same |

**All 3 critical tools operational.** The sklearn/numpy gap from v1 is resolved -- cex_retriever.py now indexes 2983 documents (up from 2184 in agent card).

---

## Phase 3: Artifact Inventory

### Count by Subdirectory (source .md only, excluding compiled/)

| Subdirectory | Count | Types |
|-------------|------:|-------|
| output | 20 | Research deliverables, audits, benchmarks |
| knowledge | 10 | KCs (intelligence domain, methods, tools, market) |
| schemas | 6 | Contracts (citation, analysis, brief, depth, source, trend) |
| quality | 5 | Quality gate, scoring rubrics, benchmark, eval dataset |
| memory | 5 | Learning record, checkpoint, knowledge index, embedding, RAG |
| tools | 4 | Research pipeline, scraping, search, MCP config |
| orchestration | 4 | Dispatch rules, workflow, notebooklm pipeline |
| prompts | 3 | System prompt, template, chain |
| agents | 3 | Main agent, competitor tracker, paper reviewer |
| reports | 3 | Self-audits, taxonomy audit, token efficiency map |
| feedback | 1 | Quality gate |
| architecture | 1 | Agent card |
| root | 1 | agent_card_n01.md |
| **TOTAL** | **66** | |

**vs. Prior Audit (v1)**: Was 64, now 66 (+2: token_efficiency_gap_map.md, taxonomy_completeness_audit.md).

### Artifacts with `quality: null` (never scored)

25 artifacts remain unscored (38% of source). Breakdown:

| Category | Count | Files |
|----------|------:|-------|
| Knowledge | 4 | kc_benchmark_tool_vs_llm, kc_cex_distribution_model, kc_token_optimization_map, kc_tool_first_patterns |
| Output | 6 | audit_pi_references, intent_resolution_benchmark, cf_dags_and_specs, content_factory_landscape, kc_quality_audit, report_input_intent_resolution |
| Memory | 3 | checkpoint, knowledge_index, learning_record |
| Tools | 3 | mcp_server_config, scraping_config, search_config |
| Reports | 3 | self_audit_newpc, taxonomy_completeness_audit, token_efficiency_gap_map |
| Quality | 2 | p07_benchmark, p07_eval_dataset |
| Agents | 2 | competitor_tracker, paper_reviewer |
| Prompts | 1 | chain_kc_to_notebooklm |
| Orchestration | 1 | workflow_notebooklm_pipeline |

### KC Library Cross-Reference

P01_knowledge/library/kind/ now exists with 128 KCs. N01-relevant KCs:

| KC | Domain Relevance |
|----|-----------------|
| kc_knowledge_card.md | Primary output kind |
| kc_context_doc.md | Agent cards, audit reports |
| kc_rag_source.md | RAG pipeline config |
| kc_embedding_config.md | Embedding model selection |
| kc_retriever_config.md | Retriever tuning |
| kc_chunk_strategy.md | Document chunking for RAG |
| kc_vector_store.md | Vector backend config |
| kc_benchmark.md | Research quality measurement |
| kc_eval_dataset.md | Evaluation data |
| kc_scoring_rubric.md | Scoring criteria |
| kc_citation.md | Source attribution |
| kc_glossary_entry.md | Terminology |
| kc_retriever.md | Retrieval tools |

**13 of 128 KCs are directly relevant** to N01's research/knowledge domain.

### 3 Identified Gaps (Updated)

| # | Gap | Impact | Priority | vs. v1 |
|---|-----|--------|----------|--------|
| 1 | **No `chunk_strategy` artifact** | Cannot configure document chunking for long-paper RAG. Semantic search over 50+ page PDFs needs chunking config. | MEDIUM | Same -- still open |
| 2 | **No `vector_store` artifact** | Cannot configure vector backends for semantic search beyond TF-IDF. HNSW/FAISS would unlock sub-second retrieval over 3K+ docs. | MEDIUM | Same -- still open. Note: port plan has HNSW from ruflo as P0 HIGH |
| 3 | **25 unscored artifacts (38%)** | Quality metrics are unreliable when 38% of artifacts lack scores. Prevents meaningful quality regression detection. | LOW | Same count but lower priority since core tools now work |

**Resolved from v1:**
- ~~No requirements.txt~~ -- not N01's responsibility (N05 domain)
- ~~KC library missing~~ -- now exists (128 KCs on disk)
- ~~numpy/sklearn missing~~ -- installed (numpy 2.4.4, sklearn 1.8.0)

---

## Phase 4: Agent Card Verification

| Field | Agent Card Claims | Actual | Match? |
|-------|-------------------|--------|--------|
| Model | opus-4-6, 1M context | opus-4-6, 1M context | [OK] |
| MCP servers | 5 | 5 (matches .mcp-n01.json) | [OK] |
| Artifact count | 64 | 66 source files | **STALE** -- 2 new reports since last update |
| Retriever docs | 2184 docs, 12K vocab | 2983 docs, 17K vocab | **STALE** |
| Kinds buildable | 20 | 20 | [OK] |
| Kinds with instances | 8 | 8 | [OK] |
| Tools | 16 | 16 | [OK] |

**Action**: Update artifact count (64->66) and retriever stats (2184->2983, 12K->17K) in agent card.

---

## Summary Scorecard

| Phase | Score | Status | vs. v1 |
|-------|-------|--------|--------|
| MCP Servers | 3/5 | DEGRADED (2 optional keys) | Same |
| Python Tools | 3/3 | **PASS** | IMPROVED (was 2/3) |
| Artifact Inventory | 66 artifacts, 25 unscored | OPERATIONAL | +2 artifacts |
| Agent Card | 5/7 fields accurate | STALE (count + retriever) | Similar |
| Doctor | 124/124 PASS | **HEALTHY** | New check |

### Critical Actions (ordered by impact)

| # | Action | Command | Blocks | Priority |
|---|--------|---------|--------|----------|
| 1 | Update agent card counts | Edit agent_card_n01.md | Accuracy | HIGH |
| 2 | Set FIRECRAWL_API_KEY | System env | Structured web extraction | MEDIUM |
| 3 | Set BRAVE_API_KEY | System env | Real-time web search | LOW (WebSearch fallback) |
| 4 | Build chunk_strategy artifact | /build chunk_strategy | RAG over long documents | MEDIUM |
| 5 | Score 25 unscored artifacts | cex_score.py --apply per file | Quality metrics | LOW |

---

## Environment Fingerprint

```
OS:        Windows 11 Pro 10.0.26200
Python:    3.14.4
numpy:     2.4.4
sklearn:   1.8.0
Node:      npx 11.11.0
UV:        uvx 0.11.6
Git:       main branch
Claude:    opus-4-6, 1M context
Retriever: 2983 docs, 17142 vocab terms
Doctor:    124 PASS | 0 WARN | 0 FAIL
```

## Boundary

Contexto de dominio para hidratar prompts. NAO eh knowledge_card (sem density gate) nem glossary_entry (nao define termo).


## 8F Pipeline Function

Primary function: **INJECT**
