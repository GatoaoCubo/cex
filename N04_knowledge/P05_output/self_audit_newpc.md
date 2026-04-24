---
id: self_audit_newpc
kind: context_doc
8f: F3_inject
title: N04 Self-Audit -- New PC Setup (2026-04-13)
nucleus: N04
pillar: P01
version: 1.1.0
quality: 8.9
created: 2026-04-12
updated: 2026-04-13
tags: [self-audit, newpc, toolchain, knowledge-library]
related:
  - self_audit_newpc_2026_04_12
  - agent_card_n04
  - n04_self_audit_20260408
  - self_audit_newpc_n02
  - self_audit_newpc_2026_04_13
  - n01_sdk_validation_self_audit
  - output_sdk_validation_knowledge_audit
  - bld_examples_kind
  - agent_card_n01
  - p12_mission_supabase_data_layer
---

# N04 Self-Audit -- New PC Setup

**Date**: 2026-04-13 (v1.1 re-run; v1.0 was 2026-04-12)
**Machine**: Windows 11 Pro 10.0.26200
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

| Metric | Expected (handoff) | Actual | Status |
|--------|-------------------|--------|--------|
| KC files in `P01_knowledge/library/kind/` | 123 | **162** | PASS (+39 new kinds since handoff) |
| Frontmatter validity (id, kind, title) | 123/123 | **162/162** | PASS |
| Encoding errors (UTF-8) | 0 | 0 | PASS |

**Note (v1.1)**: 39 new KCs added since v1.0 -- consistent with taxonomy expansion sprint (April 2026). All new KCs have valid UTF-8 frontmatter.

### 2.2 Tool Verification

| Tool | Command | Status | Notes |
|------|---------|--------|-------|
| `cex_retriever.py` | `--query "agent" --top 5` | PASS | 5 results returned. Top score 0.54. TF-IDF index operational. (v1.0 reported SyntaxError -- false alarm; confirmed PASS in v1.1) |
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
| reports | 1 | -- | Self-audit reports (this file; others archived or compiled) |
| prompts | 3 | -- | System prompts |
| quality | 2 | -- | Quality gate + scoring rubric |
| feedback | 2 | -- | Quality feedback records |
| audits | **0** | -- | **EMPTY subdir -- gap** |
| compiled | -- | 65 | YAML compilations of source artifacts |
| **TOTAL** | **69** | **65** | |

**Note (v1.1)**: v1.0 counted 71 source / 67 compiled. v1.1 actual: 69 source / 65 compiled (-2 each, likely archived). `audits/` subdir exists but has zero artifacts.

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

| Field | Card Says | Actual (v1.1) | Match? |
|-------|-----------|---------------|--------|
| Source artifacts | 71 | 69 | STALE (-2) |
| Compiled artifacts | 67 | 65 | STALE (-2) |
| Reports count | 4 | 1 | STALE (-3) |
| KC count in P01 (kind KCs) | 20 domain | 162 total | Card scoped to domain KCs; full count is 162 |
| P01 compiled examples | 197 | 197 | Match |
| MCP servers | 5 | 5 | Match |
| Kinds I build | 22 | 22 | Match |
| Tools listed | 19 | 19 | Match |
| Gaps (kc_validator, embed_batch) | listed as gaps | **now present** | Card gaps section outdated -- these were built |

**Verdict (v1.1)**: Agent card counts are slightly stale. Structure and capability descriptions accurate. Gaps section lists items that have since been built (kc_validator_tool.md, embedding_batch_processor_tool.md).

---

## Summary

| Phase | Result |
|-------|--------|
| MCP Servers | 2/5 PASS (fetch + notebooklm OK; 3 need env vars) |
| Knowledge Library | PASS (162 KCs, all UTF-8 frontmatter valid, tools operational) |
| P01 Structure | PASS (6/6 subdirs present) |
| Artifact Inventory | 69 source + 65 compiled. `audits/` empty. 3 tooling gaps. |
| Agent Card | Structurally accurate; minor count staleness; gaps section outdated |

### Blockers (user action needed)

1. Set `SUPABASE_ACCESS_TOKEN` for supabase MCP
2. Set `SUPABASE_POSTGRES_URL` for postgres MCP
3. Set `FIRECRAWL_API_KEY` for firecrawl MCP

### Recommendations (N04 can do autonomously)

1. Build glossary_entry artifacts for core CEX terms
2. Build few_shot_example artifacts for top 3 kinds
3. Build citation artifacts for key sources
4. Update agent_card_n04.md artifact counts

## Boundary

Contexto de dominio para hidratar prompts. NAO eh knowledge_card (sem density gate) nem glossary_entry (nao define termo).


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[self_audit_newpc_2026_04_12]] | sibling | 0.43 |
| [[agent_card_n04]] | sibling | 0.41 |
| [[n04_self_audit_20260408]] | related | 0.39 |
| [[self_audit_newpc_n02]] | sibling | 0.37 |
| [[self_audit_newpc_2026_04_13]] | sibling | 0.36 |
| [[n01_sdk_validation_self_audit]] | downstream | 0.34 |
| [[output_sdk_validation_knowledge_audit]] | related | 0.31 |
| [[bld_examples_kind]] | downstream | 0.27 |
| [[agent_card_n01]] | sibling | 0.26 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.26 |
