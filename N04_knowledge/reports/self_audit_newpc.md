---
id: self_audit_newpc
kind: context_doc
title: N04 Self-Audit -- New PC Setup (2026-04-12)
nucleus: N04
pillar: P01
version: 1.0.0
quality: null
created: 2026-04-12
tags: [self-audit, newpc, toolchain, knowledge-library]
---

# N04 Self-Audit -- New PC Setup

**Date**: 2026-04-12
**Machine**: Windows 11 Pro 10.0.26200 (fresh install)
**Mission**: NEWPC_SETUP wave 1

---

## Phase 1: MCP Server Verification

| # | Server | Package | Requirement | Status | Notes |
|---|--------|---------|-------------|--------|-------|
| 1 | supabase | `@supabase/mcp-server-supabase` | `SUPABASE_ACCESS_TOKEN` | FAIL | Env var NOT_SET. npx runs (binary available) but server needs token. |
| 2 | postgres | `@anthropic/mcp-server-postgres` | `SUPABASE_POSTGRES_URL` | FAIL | Env var NOT_SET. Cannot connect without connection string. |
| 3 | fetch | `mcp-server-fetch` (uvx) | uvx binary | PASS | uvx 0.11.6 installed and functional. |
| 4 | firecrawl | `firecrawl-mcp` | `FIRECRAWL_API_KEY` | FAIL | Env var NOT_SET. npx available but server needs key. |
| 5 | notebooklm | `notebooklm-mcp@latest` | npx | PASS | v1.0.0 banner confirmed. Gemini 2.5 backend. |

**Summary**: 2/5 PASS, 3/5 FAIL (all failures are missing env vars, not missing binaries).

### Action Required

Set these environment variables (user-level or `.env`):

```
SUPABASE_ACCESS_TOKEN=<from Supabase dashboard > Settings > Access Tokens>
SUPABASE_POSTGRES_URL=<from Supabase dashboard > Settings > Database > Connection string>
FIRECRAWL_API_KEY=<from firecrawl.dev dashboard>
```

---

## Phase 2: Knowledge Library Audit

### 2.1 KC Count

| Metric | Expected | Actual | Status |
|--------|----------|--------|--------|
| KC files in `P01_knowledge/library/kind/` | 123 | 123 | PASS |
| Frontmatter validity (id, kind, title) | 123/123 | 123/123 | PASS |

### 2.2 Tool Verification

| Tool | Command | Status | Notes |
|------|---------|--------|-------|
| `cex_retriever.py` | `--query "agent" --top 5` | PASS | 5 results returned. Top score 0.5425. TF-IDF index operational. |
| `cex_compile.py` | `--help` | PASS | CLI operational. Supports md->yaml + reverse compilation. |
| `cex_doctor.py` | (full run) | PASS | 123 PASS, 0 WARN, 0 FAIL. 1599 files, 5282KB, avg density 0.95. |

### 2.3 P01 Pillar Structure

| Subdir | Present | Contents |
|--------|---------|----------|
| `compiled/` | Yes | YAML compilations |
| `examples/` | Yes | Example artifacts for template-first construction |
| `library/` | Yes | 123 KCs (kind KCs) |
| `templates/` | Yes | Output templates |
| `yaml/` | Yes | Schema YAML files |

**Structure**: PASS -- all expected subdirectories present.

---

## Phase 3: Artifact Inventory

### 3.1 N04_knowledge/ by Subdirectory

| Subdir | Source | Compiled | Purpose |
|--------|-------:|:--------:|---------|
| output | 19 | -- | KC audits, gap reports, taxonomy maps, knowledge graphs |
| knowledge | 13 | -- | Core domain: chunk, embedding, KCs, RAG sources, retriever |
| schemas | 7 | -- | Database, embedding, export, freshness, KC, naming, taxonomy |
| orchestration | 5 | -- | Dispatch rules + workflows |
| memory | 5 | -- | Knowledge memory index + RAG pipeline memory |
| tools | 4 | -- | Supabase data layer + utilities |
| architecture | 4 | -- | Agent cards + capability maps |
| agents | 4 | -- | Agent definitions |
| reports | 3 | -- | Self-audit reports (prior runs) |
| prompts | 3 | -- | System prompts |
| quality | 2 | -- | Quality gate + scoring rubric |
| feedback | 2 | -- | Quality feedback records |
| compiled | -- | 67 | YAML compilations of source artifacts |
| **TOTAL** | **71** | **67** | |

**Note**: Source count grew from 43 (last agent card) to 71 since prior audit. Agent card needs update.

### 3.2 Coverage Assessment

| Domain | Depth | Rating |
|--------|-------|--------|
| Knowledge Cards (authoring, audit, taxonomy) | 13 knowledge + 19 output | Strong |
| Schemas & contracts | 7 schemas | Strong |
| Orchestration (dispatch + workflows) | 5 artifacts | Adequate |
| Memory management | 5 artifacts | Adequate |
| Architecture docs | 4 artifacts | Adequate |
| Agent definitions | 4 artifacts | Adequate |
| Tooling | 4 artifacts | Adequate |
| Quality governance | 2 + 2 feedback | Thin |
| Prompts | 3 artifacts | Thin |

### 3.3 Schema Cross-Reference (P01_knowledge/_schema.yaml)

P01 defines 9 kinds. N04 coverage:

| Kind | Has Builder? | Has N04 Artifacts? | Status |
|------|-------------|-------------------|--------|
| knowledge_card | Yes (123 KCs) | Yes (core domain) | Covered |
| rag_source | Yes | Yes (2 configs) | Covered |
| glossary_entry | Yes | No artifacts built | GAP |
| context_doc | Yes | Yes (agent card is one) | Covered |
| embedding_config | Yes | Yes (2 configs) | Covered |
| few_shot_example | Yes | No artifacts built | GAP |
| chunk_strategy | Yes | Yes (1 config) | Covered |
| retriever_config | Yes | Yes (1 config) | Covered |
| citation | Yes | No artifacts built | GAP |

### 3.4 Three Gaps in Knowledge Management Tooling

| # | Gap | Impact | Recommended Fix |
|---|-----|--------|-----------------|
| 1 | **No glossary_entry artifacts** | Terms are scattered across KCs instead of indexed as discrete glossary entries. No term-level retrieval. | Build 20 core glossary entries for CEX terminology (kind, pillar, nucleus, 8F, GDP, etc.) |
| 2 | **No few_shot_example artifacts** | Template-first construction at F3 lacks concrete input/output pairs. Builders fall back to fresh generation more often than needed. | Create 5 few-shot examples for high-frequency kinds (knowledge_card, context_doc, embedding_config). |
| 3 | **No citation artifacts** | Knowledge cards reference sources informally in prose. No structured provenance chain for fact verification or freshness auditing. | Build citation artifacts for the top 10 most-referenced external sources. |

---

## Phase 4: Agent Card Assessment

**File**: `N04_knowledge/agent_card_n04.md`
**Current version**: 1.0.0, quality 9.1 (peer-scored)

### Accuracy Check

| Field | Card Says | Actual | Match? |
|-------|-----------|--------|--------|
| Source artifacts | 43 | 71 | OUTDATED |
| Compiled artifacts | 42 | 67 | OUTDATED |
| KC count in P01 | 123 | 123 | Match |
| MCP servers | 5 | 5 | Match |
| Kinds I build | 22 | 22 | Match |
| Tools listed | 19 | 19 | Match |
| Gaps listed | 12 | Still valid | Match |

**Verdict**: Agent card artifact counts are stale (43->71 source, 42->67 compiled). The counts table and the "TOTAL CARDS" section need update. Structure and capability descriptions remain accurate.

---

## Summary

| Phase | Result |
|-------|--------|
| MCP Servers | 2/5 PASS (3 need env vars) |
| Knowledge Library | PASS (123 KCs, all frontmatter valid, tools operational) |
| Artifact Inventory | 71 source + 67 compiled. 3 gaps identified. |
| Agent Card | Structurally accurate, counts outdated |
| Doctor | 123 PASS, 0 WARN, 0 FAIL |

### Blockers (user action needed)

1. Set `SUPABASE_ACCESS_TOKEN` for supabase MCP
2. Set `SUPABASE_POSTGRES_URL` for postgres MCP
3. Set `FIRECRAWL_API_KEY` for firecrawl MCP

### Recommendations (N04 can do autonomously)

1. Build glossary_entry artifacts for core CEX terms
2. Build few_shot_example artifacts for top 3 kinds
3. Build citation artifacts for key sources
4. Update agent_card_n04.md artifact counts
