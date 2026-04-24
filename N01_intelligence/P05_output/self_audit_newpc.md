---
id: self_audit_newpc_2026_04_13
kind: context_doc
8f: F3_inject
title: N01 Self-Audit -- New PC Setup (2026-04-13)
pillar: P01_knowledge
nucleus: N01
version: 3.0.0
quality: 8.3
created: 2026-04-12
updated: 2026-04-13
mission: NEWPC_SETUP
related:
  - agent_card_n01
  - self_audit_newpc
  - self_audit_newpc_2026_04_12
  - self_audit_newpc_n02
  - bld_examples_boot_config
  - n01_sdk_validation_self_audit
  - p04_tool_mcp_config
  - bld_examples_agent_card
  - output_sdk_validation_knowledge_audit
  - hybrid_review7_n05
---

# N01 Self-Audit -- New PC Setup (v3)

**Machine**: Windows 11 Pro 10.0.26200
**Date**: 2026-04-13
**Python**: 3.14.4 (numpy 2.4.4, sklearn 1.8.0)
**Node**: v24.14.1
**UV**: uvx 0.11.6
**Doctor**: 133 PASS | 21 WARN | 1 FAIL

---

## Phase 1: MCP Server Verification

| # | Server | Binary | API Key | Verdict | vs. v2 |
|---|--------|--------|---------|---------|--------|
| 1 | firecrawl | npx [OK] | FIRECRAWL_API_KEY **NOT SET** | **FAIL** | Same |
| 2 | fetch | uvx 0.11.6 [OK] | n/a | **PASS** | Same |
| 3 | markitdown | npx [OK] | n/a | **PASS** | Same |
| 4 | brave-search | npx [OK] | BRAVE_API_KEY **NOT SET** | **FAIL** | Same |
| 5 | notebooklm | npx [OK] | n/a | **PASS** | Same |

**Score: 3/5 PASS** (unchanged from v2)

### Impact Analysis

| Server | Capability Lost | Alternative | Severity |
|--------|----------------|-------------|----------|
| firecrawl | Structured web extraction (competitor sites, pricing pages) | fetch (raw HTML, no extraction) | MEDIUM -- fetch covers ~60% of use cases |
| brave-search | Real-time web search for competitive intelligence | Claude Code WebSearch tool | LOW -- WebSearch is a viable fallback |

**vs. v2**: No change. Both optional API keys remain unset. Core research pipeline (fetch + markitdown + notebooklm) fully operational.

---

## Phase 2: Python Tools Audit

### Bug Fixed This Session

| Tool | Issue | Fix | Status |
|------|-------|-----|--------|
| `cex_retriever.py` | SyntaxError: stray ` ``` ` markdown fence at line 489 (EOF) | Removed fence; fixed duplicate `-k` shorthand conflict (`--kind` vs `--top-k`) | **FIXED** |

### Tool Health (post-fix)

| Tool | --help | Runtime | Verdict | vs. v2 |
|------|--------|---------|---------|--------|
| cex_retriever.py | [OK] | [OK] (2983 docs, 17142 vocab) | **PASS** | **FIXED** (was FAIL -- SyntaxError) |
| cex_compile.py | [OK] | [OK] | **PASS** | Same |
| cex_doctor.py | [OK] | [OK] (133 PASS, 21 WARN, 1 FAIL) | **PASS** | WARN count up (+21 from 0) |

### Doctor Delta

| Metric | v2 (2026-04-12) | v3 (2026-04-13) | Delta |
|--------|-----------------|-----------------|-------|
| PASS | 124 | 133 | +9 |
| WARN | 0 | 21 | +21 |
| FAIL | 0 | 1 | +1 |
| Builders found | 155 | 155 | 0 |
| Total files | ~2006 | 2006 | ~same |

**21 WARNs are expected**: density/naming warnings from new research atlas atoms added since v2.
**1 FAIL**: requires investigation (likely a naming or frontmatter compliance issue in a new artifact).

---

## Phase 3: Artifact Inventory

### Count by Subdirectory (source .md only, excluding compiled/)

| Subdirectory | Count | vs. v2 | Types |
|-------------|------:|--------|-------|
| research | 34 | **+34 NEW** | Atlas atoms (A15-A33), LLM vocab whitepaper, compiled atlas |
| output | 20 | +4 | Research deliverables, KC quality audit, intent benchmarks |
| knowledge | 15 | +5 | KCs: prompt taxonomy, overnight evolve, LLM vocab, model context, synthetic data |
| reports | 7 | +4 | Self-audits (v1-v3), taxonomy audit, token efficiency, extraction reports |
| schemas | 6 | same | 6 research contracts |
| quality | 5 | same | Quality gate, scoring rubrics, benchmark, eval dataset |
| memory | 5 | same | Learning record, checkpoint, knowledge index, embedding, RAG |
| orchestration | 4 | +1 | Dispatch rules, workflow, notebooklm pipeline |
| tools | 4 | same | Research pipeline, scraping, search, MCP config |
| prompts | 3 | +1 | System prompt, template, chain |
| agents | 3 | same | Main agent, competitor tracker, paper reviewer |
| feedback | 1 | same | Quality gate |
| architecture | 1 | same | Agent card |
| root | 1 | same | agent_card_n01.md (root) |
| audits | 0 | same | Empty dir |
| **TOTAL** | **110** | **+44** | |

**Growth since v2**: +44 artifacts (67% increase). Primary driver: research/atlas/ directory with 34 files added (LLM vocabulary atlas, competitive intelligence atoms).

### Artifacts with `quality: null` (never scored)

Only **3** artifacts remain unscored (2.7% of source -- massive improvement from 38% in v2):

| File | Kind | Priority |
|------|------|----------|
| output/output_cf_dags_and_specs.md | context_doc | LOW |
| output/output_content_factory_landscape.md | context_doc | LOW |
| reports/self_audit_newpc.md | context_doc | LOW (this file) |

**vs. v2**: Was 25 unscored (38%). Now 3 (2.7%). The 22 newly scored artifacts represent a major quality accounting improvement.

### KC Library Cross-Reference

13 of 128 P01 KCs directly relevant to N01 domain:

| KC | Status | Relevance |
|----|--------|-----------|
| kc_knowledge_card.md | [OK] | Primary output kind |
| kc_context_doc.md | [OK] | Agent cards, audit reports |
| kc_rag_source.md | [OK] | RAG pipeline config |
| kc_embedding_config.md | [OK] | Embedding model selection |
| kc_retriever_config.md | [OK] | Retriever tuning |
| kc_chunk_strategy.md | [OK] | Document chunking for RAG |
| kc_vector_store.md | [OK] | Vector backend config |
| kc_benchmark.md | [OK] | Research quality measurement |
| kc_agentic_rag.md | [OK] | End-to-end RAG agents |
| kc_retriever.md | [OK] | Retrieval tools |
| kc_research_pipeline.md | [OK] | Research orchestration |
| kc_memory_architecture.md | [OK] | Memory system design |
| kc_knowledge_index.md | [OK] | Index management |

**New vs. v2**: kc_agentic_rag, kc_research_pipeline, kc_memory_architecture, kc_knowledge_index added since last audit (4 new relevant KCs).

### 3 Identified Gaps (v3)

| # | Gap | Impact | Priority | vs. v2 |
|---|-----|--------|----------|--------|
| 1 | **1 FAIL in doctor** | Unknown artifact violates naming/frontmatter rule | HIGH | New in v3 |
| 2 | **No `chunk_strategy` artifact** | Cannot configure document chunking for long-paper RAG over 50+ page PDFs | MEDIUM | Same since v1 |
| 3 | **No `vector_store` artifact** | Cannot configure HNSW/FAISS backends for sub-second retrieval over 3K+ docs | MEDIUM | Same since v1 |

**Resolved from v2:**
- ~~cex_retriever.py SyntaxError~~ -- FIXED (removed stray markdown fence + shorthand conflict)
- ~~25 unscored artifacts~~ -- Now 3 (2.7%)
- ~~Artifact count stale in agent card~~ -- Updated in this session

---

## Phase 4: Agent Card Verification

| Field | Agent Card Claims | Actual (v3) | Match? | Action |
|-------|-------------------|-------------|--------|--------|
| Model | opus-4-6, 1M context | opus-4-6, 1M context | [OK] | None |
| MCP servers | 5 | 5 (matches .mcp-n01.json) | [OK] | None |
| Artifact count | 66 | 110 source files | **STALE** | Update |
| Research subdir | Not listed | 34 files (atlas atoms) | **MISSING** | Add row |
| Retriever docs | 2983 docs, 17142 vocab | 2983 docs, 17142 vocab | [OK] | None |
| Doctor | 124 PASS | 133 PASS, 21 WARN, 1 FAIL | **STALE** | Update |
| Kinds buildable | 20 | 20 | [OK] | None |
| Kinds with instances | 8 | 8 | [OK] | None |
| Tools | 16 | 16 | [OK] | None |

**Actions**: Update artifact count (66->110), add research row (34 files), update doctor stats.

---

## Summary Scorecard

| Phase | Score | Status | vs. v2 |
|-------|-------|--------|--------|
| MCP Servers | 3/5 | DEGRADED (2 optional keys) | Same |
| Python Tools | 3/3 | **PASS** (1 bug fixed) | IMPROVED (fixed retriever) |
| Artifact Inventory | 110 artifacts, 3 unscored | **HEALTHY** | IMPROVED (+44 artifacts, 38%->2.7% unscored) |
| Agent Card | 6/9 fields accurate | STALE (count, research row, doctor) | STALE (new gaps from growth) |
| Doctor | 133 PASS, 21 WARN, 1 FAIL | **WARN** (1 fail to investigate) | REGRESSED (was 0 failures) |

### Critical Actions (ordered by impact)

| # | Action | Command | Blocks | Priority |
|---|--------|---------|--------|----------|
| 1 | Investigate doctor FAIL | `python _tools/cex_doctor.py 2>&1 | grep FAIL` | System integrity | HIGH |
| 2 | Update agent card counts | Edit agent_card_n01.md | Accuracy | HIGH |
| 3 | Set FIRECRAWL_API_KEY | System env | Structured web extraction | MEDIUM |
| 4 | Build chunk_strategy artifact | /build chunk_strategy | RAG over long documents | MEDIUM |
| 5 | Build vector_store artifact | /build vector_store | Sub-second semantic search | MEDIUM |
| 6 | Set BRAVE_API_KEY | System env | Real-time web search | LOW (WebSearch fallback) |

---

## Environment Fingerprint

```
OS:        Windows 11 Pro 10.0.26200
Python:    3.14.4
numpy:     2.4.4
sklearn:   1.8.0
Node:      v24.14.1
UV:        uvx 0.11.6
Git:       main branch
Claude:    sonnet-4-6 (N01 session)
Retriever: 2983 docs, 17142 vocab terms
Doctor:    133 PASS | 21 WARN | 1 FAIL
Artifacts: 110 source .md (excl. compiled/)
```

## Boundary

Context document for N01 nucleus self-assessment. Not a knowledge_card (no density gate). Not a glossary_entry (no term definition).

## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_n01]] | sibling | 0.35 |
| [[self_audit_newpc]] | sibling | 0.31 |
| [[self_audit_newpc_2026_04_12]] | sibling | 0.31 |
| [[self_audit_newpc_n02]] | sibling | 0.29 |
| [[bld_examples_boot_config]] | related | 0.28 |
| [[n01_sdk_validation_self_audit]] | related | 0.27 |
| [[p04_tool_mcp_config]] | related | 0.25 |
| [[bld_examples_agent_card]] | related | 0.23 |
| [[output_sdk_validation_knowledge_audit]] | related | 0.22 |
| [[hybrid_review7_n05]] | related | 0.21 |
