---
id: n04_self_audit_20260408
kind: knowledge_card
pillar: P01
title: "N04 Knowledge Nucleus Self-Audit -- 2026-04-08"
version: 1.0.0
created: 2026-04-08
author: n04_knowledge
domain: meta
quality: 8.9
tags: [self-audit, n04, knowledge, mcp, rag, tooling]
tldr: "Audit of N04 MCP config, RAG pipeline, tooling health, and gaps"
when_to_use: "Review N04 capabilities and identify improvement areas"
keywords: [self-audit, mcp, retriever, pgvector, supabase, embedding]
density_score: null
---

# N04 Knowledge Nucleus Self-Audit

## 1. MCP Configuration (.mcp-n04.json)

| Server | Command | Status | Notes |
|--------|---------|--------|-------|
| supabase | npx @supabase/mcp-server-supabase | ACTIVE | Full CRUD, migrations, edge functions |
| postgres | npx @anthropic/mcp-server-postgres | UNKNOWN | Needs SUPABASE_POSTGRES_URL env var -- not testable in-session |
| fetch | uvx mcp-server-fetch | ACTIVE | Web content retrieval working |
| firecrawl | npx firecrawl-mcp | ACTIVE | Crawl, scrape, search, browser automation |
| notebooklm | npx notebooklm-mcp@latest | ACTIVE | Notebook CRUD, audio overview generation |

**Finding**: 5 MCP servers configured. 4 confirmed active via deferred tool availability. postgres MCP not visible in tool list -- may need env var or may be superseded by supabase MCP which includes SQL execution.

## 2. Knowledge Tooling Health

| Tool | Purpose | Status | Stats |
|------|---------|--------|-------|
| cex_retriever.py | TF-IDF semantic search | HEALTHY | 2,450 docs, 14,698 vocab terms |
| cex_kc_index.py | Supabase pgvector indexing | HEALTHY | 656 KCs indexed across 47 kinds |
| cex_memory_select.py | LLM-powered memory retrieval | AVAILABLE | Query-based, top-k, cache support |
| cex_memory_update.py | Memory decay + append + prune | AVAILABLE | Not tested this session |
| cex_memory_types.py | 4-type memory taxonomy | AVAILABLE | correction/preference/convention/context |
| cex_memory_age.py | Freshness decay (365d linear) | AVAILABLE | Age labels + caveats |
| cex_compile.py | .md to .yaml compilation | HEALTHY | Used in every build |

## 3. Retriever Index Analysis

- **Index built**: 2026-04-02 (6 days old)
- **Documents**: 2,450 (likely stale -- repo has grown since)
- **Top kinds indexed**: knowledge_card (504), output_template (133), quality_gate (133)
- **Pillar coverage**: All P01-P12 represented, but counts vary widely
- **Issue**: Index includes `P00`, `P13`, and unlabeled entries -- cleanup needed

**Recommendation**: Rebuild index (`cex_retriever.py --build`) after this wave completes.

## 4. pgvector Index Analysis

- **Total indexed**: 656 KCs
- **Kind diversity**: 47 distinct kinds represented
- **Top kind**: knowledge_card (388 = 59% of index)
- **Sparse kinds**: Many with 1-2 entries (chain, benchmark, interface, etc.)

**Recommendation**: Re-index after current cleanup (`cex_kc_index.py --force`).

## 5. Claude Code Features -- Usage Assessment

| Feature | Available | N04 Using? | Gap |
|---------|-----------|------------|-----|
| Sub-agents (5 parallel) | YES | NO | Could parallelize KC audits across pillars |
| MCP supabase | YES | PARTIAL | Using for index, not for KC storage/query |
| MCP firecrawl | YES | NO | Could auto-research external sources for KCs |
| MCP notebooklm | YES | NO | Could generate audio overviews of knowledge |
| MCP fetch | YES | RARE | Manual web fetches, not systematic |
| Task tracking | YES | NO | Could track audit progress across sessions |
| Memory system | YES | NO | N04 memories should persist across sessions |
| Worktree isolation | YES | NO | Could test index rebuilds without affecting main |

## 6. Gaps Identified

### Critical
1. **Retriever index stale** (6 days, ~200+ new artifacts since last build)
2. **No automated re-index trigger** -- manual rebuild required after each wave

### Important
3. **postgres MCP may not be connecting** -- env var dependency unclear
4. **No sub-agent usage** -- N04 could parallelize: 1 agent per pillar for KC audits
5. **firecrawl + notebooklm unused** -- knowledge pipeline not leveraging available MCPs

### Minor
6. **Memory system not used** -- N04 should store cross-session knowledge state
7. **Index includes orphan pillar codes** (P00, P13) -- schema mapping issue

## 7. Action Items

| # | Action | Priority | Effort |
|---|--------|----------|--------|
| 1 | Rebuild retriever index | HIGH | 1 min |
| 2 | Re-index pgvector | HIGH | 2 min |
| 3 | Investigate postgres MCP env var | MEDIUM | 5 min |
| 4 | Design sub-agent KC audit workflow | MEDIUM | 30 min |
| 5 | Build firecrawl-to-KC pipeline | LOW | 1 hour |
| 6 | Build notebooklm audio overview automation | LOW | 1 hour |
| 7 | Clean orphan pillar codes from index | LOW | 10 min |

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**
