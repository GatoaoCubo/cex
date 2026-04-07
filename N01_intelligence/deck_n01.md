---
id: deck_n01
kind: context_doc
title: N01 Deck -- Available Capabilities
pillar: P01_knowledge
nucleus: N01
sin: Inveja Analitica
version: 1.0.0
quality: null
created: 2026-04-07
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus | N01 -- Intelligence |
| Sin | Inveja Analitica (Analytical Envy) |
| Domain | Research, market analysis, competitor intel, papers, benchmarks, trend detection |
| CLI | claude (Opus 4.6, 1M context) |
| Artifacts dir | `N01_intelligence/` |
| Routing IN | Research, papers, market analysis, competitor intelligence, benchmarks, trends |
| Routing OUT | Build artifacts (N03), marketing copy (N02), deploy/test (N05) |

8F is the reasoning protocol for every task -- research briefs, competitive grids, trend reports all pass F1-F8.

## My Artifacts

| Subdir | Count | Purpose |
|--------|------:|---------|
| agents | 1 | Agent definition for intelligence nucleus |
| architecture | 1 | Agent card (capabilities, routing, interfaces) |
| feedback | 1 | Quality gate for intelligence outputs |
| knowledge | 6 | KCs: intelligence domain, research methods, source catalog, pet market, embedding config, RAG source |
| memory | 2 | Embedding config + RAG source for persistent recall |
| orchestration | 3 | Dispatch rules (intelligence routing, research pipeline) + workflow |
| output | 15 | Research deliverables: competitive grids, SWOT, market snapshots, trend reports, benchmark reports, executive summaries, SDK audits |
| prompts | 2 | System prompt + prompt template for intelligence tasks |
| quality | 3 | Quality gate + 2 scoring rubrics |
| schemas | 6 | Contracts: citation format, competitive analysis, research brief, depth levels, source quality, trend detection |
| tools | 1 | Research pipeline tool definition |
| **TOTAL** | **41** | |

## Kinds I Build

| Kind | Pillar | Naming Pattern |
|------|--------|---------------|
| knowledge_card | P01 | `p01_kc_{{topic}}.md + .yaml` |
| context_doc | P01 | `p01_ctx_{{topic}}.md + .yaml` |
| chunk_strategy | P01 | `p01_chunk_{{strategy}}.md` |
| embedding_config | P01 | `p01_emb_{{model}}.yaml` |
| few_shot_example | P01 | `p01_fse_{{topic}}.md + .yaml` |
| glossary_entry | P01 | `p01_gl_{{term}}.md + .yaml` |
| rag_source | P01 | `p01_rs_{{source}}.md + .yaml` |
| retriever_config | P01 | `p01_retr_cfg_{{store}}.md` |
| benchmark | P07 | `p07_bm_{{metric}}.md + .yaml` |
| eval_dataset | P07 | `p07_dataset_{{name}}.md` |
| brain_index | P10 | `p10_bi_{{index}}.yaml` |
| learning_record | P10 | `p10_lr_{{topic}}.md + .yaml` |
| research_pipeline | P04 | `p04_rp_{{name}}.md` |
| retriever | P04 | `p04_retr_{{store}}.md + .yaml` |
| search_tool | P04 | `p04_search_{{provider}}.md + .yaml` |
| document_loader | P04 | `p04_loader_{{format}}.md + .yaml` |
| mental_model | P02 | `p02_mm_{{agent}}.yaml` |

**17 kinds** in my domain.

## Tools I Use

| Tool | Purpose |
|------|---------|
| `cex_retriever.py` | TF-IDF artifact similarity search (2184 docs, 12K vocab) -- find related intelligence |
| `cex_query.py` | Builder discovery via TF-IDF -- resolve which builder handles an intent |
| `cex_compile.py` | .md to .yaml compilation -- mandatory F8 step |
| `cex_research.py` | Research pipeline orchestration |
| `cex_memory_select.py` | Inject relevant memories into research context |
| `cex_memory_update.py` | Update memory with new findings (decay + append + prune) |
| `cex_token_budget.py` | Token counting + budget allocation for large document analysis |
| `cex_prompt_layers.py` | Load pillar artifacts into prompts (15+ sources) |
| `cex_skill_loader.py` | Load builder ISOs (13 per kind) for artifact construction |
| `cex_score.py` | Peer review scoring (--apply) |
| `cex_doctor.py` | Health check validation |
| `cex_evolve.py` | AutoResearch loop -- autonomous artifact improvement |
| `cex_kc_index.py` | Knowledge card indexing |
| `cex_index.py` | General artifact indexing |
| `cex_notebooklm.py` | KC-to-NotebookLM pipeline for human content |
| `signal_writer.py` | Signal N07 on task completion |

## MCP Servers

| Server | Purpose |
|--------|---------|
| **firecrawl** | Web scraping + crawling (structured extraction from websites) |
| **fetch** | Raw URL fetching (ignores robots.txt for research) |
| **markitdown** | Convert documents (PDF, DOCX, PPTX) to markdown for analysis |
| **brave-search** | Web search API for real-time market/competitor intelligence |
| **notebooklm** | Push KCs to Google NotebookLM for human-facing audio/content |

**5 MCP servers** -- full research stack: search, fetch, crawl, convert, publish.

## My Strengths

1. **Deep output library**: 15 research deliverables covering competitive grids, SWOT analysis, market snapshots, trend reports, benchmark reports, executive summaries, and SDK audits
2. **Structured research contracts**: 6 schema contracts define citation formats, source quality standards, research depth levels, and trend detection methodology
3. **Full research pipeline**: MCP servers give end-to-end capability from web search through document conversion to structured intelligence output
4. **Knowledge foundation**: 6 KCs covering research methods, source catalogs, and domain-specific intelligence
5. **1M context window**: Can process entire codebases, long papers, and large document sets in a single pass
6. **17 buildable kinds**: Broadest kind coverage of any nucleus, spanning P01, P02, P04, P07, and P10

## My Gaps

| Gap | Impact | Priority |
|-----|--------|----------|
| `tools/` has only 1 artifact | Research pipeline is defined but no tool-specific configs (e.g., scraping rules, API rate limits) | Medium |
| `agents/` has only 1 artifact | No sub-agent definitions for specialized research roles (e.g., competitor tracker, paper reviewer) | Medium |
| `architecture/` has only 1 artifact | Missing architecture docs for research workflow patterns | Low |
| `memory/` has only 2 artifacts | Thin persistent memory -- research findings not accumulating across sessions | High |
| No `eval_dataset` artifacts | Cannot benchmark own research quality over time | Medium |
| No `benchmark` artifacts built | Despite being a buildable kind, no benchmarks exist in N01 | Medium |
| No `brain_index` artifacts | Missing semantic index over intelligence outputs | Low |

## Cards in My Deck

| Category | Count |
|----------|------:|
| Artifacts in N01_intelligence/ | 41 |
| Kinds I can build | 17 |
| Tools relevant to my work | 16 |
| MCP servers | 5 |
| **Total cards** | **79** |
