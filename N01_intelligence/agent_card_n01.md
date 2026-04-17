---
id: agent_card_n01
kind: context_doc
title: N01 Agent Card -- Available Capabilities
pillar: P01_knowledge
nucleus: N01
sin: Inveja Analitica
version: 1.2.0
quality: 9.0
created: 2026-04-07
density_score: 1.0
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

**Comparative positioning**: N01 has 110 source artifacts, 3 agents, 4 tool configs, and 5 quality artifacts (including benchmark + eval dataset). N01 leads the nucleus fleet in research depth with 34 atlas research files, 15 KCs, and 5 MCP servers. Retriever: 2983 docs, 17142 vocab terms.

## My Artifacts

| Subdir | Count | Purpose |
|--------|------:|---------|
| research | 34 | Atlas atoms (A15-A33), LLM vocabulary whitepaper, compiled atlas |
| agents | 3 | Main agent + competitor tracker sub-agent + paper reviewer sub-agent |
| architecture | 1 | Agent card (capabilities, routing, interfaces) |
| feedback | 1 | Quality gate for intelligence outputs |
| knowledge | 15 | KCs: intelligence domain, research methods, source catalog, pet market, embedding, RAG, prompt taxonomy, overnight evolve, LLM vocab, model context, synthetic data |
| memory | 5 | Learning record, checkpoint, knowledge index, embedding config, RAG source |
| orchestration | 4 | Dispatch rules (intelligence routing, research pipeline) + 2 workflows |
| output | 20 | Research deliverables: competitive grids, SWOT, market snapshots, trend reports, benchmark reports, executive summaries, SDK audits, content factory landscape, monetization research, KC quality audit |
| prompts | 3 | System prompt + prompt template + chain |
| quality | 5 | Quality gate + 2 scoring rubrics + benchmark + eval dataset |
| schemas | 6 | Contracts: citation format, competitive analysis, research brief, depth levels, source quality, trend detection |
| tools | 4 | Research pipeline + scraping config + search config + MCP server orchestration |
| reports | 7 | Self-audit reports (v1-v3), taxonomy audit, token efficiency map, extraction reports |
| **TOTAL** | **110** | |

## Kinds I Can Build

### P01 -- Knowledge (primary domain, all 10 kinds)

| Kind | Naming Pattern | Status |
|------|---------------|--------|
| knowledge_card | `p01_kc_{{topic}}.md + .yaml` | Active -- 6 KCs built |
| context_doc | `p01_ctx_{{topic}}.md + .yaml` | Active -- this agent card is one |
| chunk_strategy | `p01_chunk_{{strategy}}.md` | Available, none built |
| embedder_provider | `p01_ep_{{provider}}.yaml` | Available, none built |
| embedding_config | `p01_emb_{{model}}.yaml` | Active -- 1 built |
| few_shot_example | `p01_fse_{{topic}}.md + .yaml` | Available, none built |
| glossary_entry | `p01_gl_{{term}}.md + .yaml` | Available, none built |
| rag_source | `p01_rs_{{source}}.md + .yaml` | Active -- 1 built |
| retriever_config | `p01_retr_cfg_{{store}}.md` | Available, none built |
| vector_store | `p01_vdb_{{backend}}.yaml` | Available, none built |

### P07 -- Evals (research quality measurement)

| Kind | Naming Pattern | Status |
|------|---------------|--------|
| benchmark | `p07_bm_{{metric}}.md + .yaml` | Available, none built |
| eval_dataset | `p07_dataset_{{name}}.md` | Available, none built |
| scoring_rubric | `p07_sr_{{framework}}.md + .yaml` | Active -- 2 built |

### P04 -- Tools (research instrumentation)

| Kind | Naming Pattern | Status |
|------|---------------|--------|
| research_pipeline | `p04_rp_{{name}}.md` | Active -- 1 built |
| retriever | `p04_retr_{{store}}.md + .yaml` | Available, none built |
| search_tool | `p04_search_{{provider}}.md + .yaml` | Available, none built |
| document_loader | `p04_loader_{{format}}.md + .yaml` | Available, none built |

### P10 -- Memory (research accumulation)

| Kind | Naming Pattern | Status |
|------|---------------|--------|
| knowledge_index | `p10_bi_{{index}}.yaml` | Available, none built |
| learning_record | `p10_lr_{{topic}}.md + .yaml` | Available, none built |

### P02 -- Model (agent cognition)

| Kind | Naming Pattern | Status |
|------|---------------|--------|
| mental_model | `p02_mm_{{agent}}.yaml` | Available, none built |

**20 kinds total** across 5 pillars. Of these, 5 kinds are active (artifacts exist), 15 are available but unbuilt.

Compared to: N03 builds primarily P03+P08 kinds (prompt/architecture), N05 builds P09+P11 kinds (runtime/governance). N01 is the only nucleus with native coverage across P01+P04+P07+P10 -- the full knowledge-to-evaluation pipeline.

## Tools I Use

| Tool | Purpose | N01 Relevance |
|------|---------|---------------|
| `cex_retriever.py` | TF-IDF artifact similarity (2983 docs, 17K vocab) | Find related intelligence across all pillars |
| `cex_query.py` | Builder discovery via TF-IDF | Resolve which builder handles a research intent |
| `cex_compile.py` | .md to .yaml compilation | Mandatory F8 step for every artifact |
| `cex_research.py` | Research pipeline orchestration | Core tool -- drives end-to-end research |
| `cex_memory_select.py` | Inject relevant memories into context | Pull past research findings into new tasks |
| `cex_memory_update.py` | Update memory (decay + append + prune) | Accumulate intelligence across sessions |
| `cex_token_budget.py` | Token counting + budget allocation | Manage 1M context for large document analysis |
| `cex_prompt_layers.py` | Load pillar artifacts into prompts (15+ sources) | Enrich research prompts with domain context |
| `cex_skill_loader.py` | Load builder ISOs (13 per kind) | Construction context for building artifacts |
| `cex_score.py` | Peer review scoring (--apply) | Evaluate artifact quality post-build |
| `cex_doctor.py` | Health check validation | Verify system integrity |
| `cex_evolve.py` | AutoResearch loop | Autonomously improve artifacts via iteration |
| `cex_kc_index.py` | Knowledge card indexing | Index KC library for fast retrieval |
| `cex_index.py` | General artifact indexing | Full artifact index maintenance |
| `cex_notebooklm.py` | KC-to-NotebookLM pipeline | Push research to human-facing audio/content |
| `signal_writer.py` | Signal N07 on task completion | Inter-nucleus communication |

**16 tools** in my operational stack.

## MCP Servers

| Server | Command | Purpose | Unique to N01? |
|--------|---------|---------|----------------|
| **firecrawl** | `npx firecrawl-mcp` | Web scraping + structured extraction from websites | Shared with N02 |
| **fetch** | `uvx mcp-server-fetch` | Raw URL fetching (ignores robots.txt for research) | Shared |
| **markitdown** | `npx markitdown-mcp` | Convert PDF/DOCX/PPTX to markdown for analysis | N01 primary user |
| **brave-search** | `npx @anthropic/mcp-server-brave-search` | Web search API for real-time market/competitor intel | Shared with N02 |
| **notebooklm** | `npx notebooklm-mcp@latest` | Push KCs to Google NotebookLM for audio/content | Shared |

**5 MCP servers** -- full research stack: search -> fetch -> crawl -> convert -> publish. N01 is the primary consumer of markitdown (document analysis) and brave-search (competitive intelligence). The combined pipeline enables: discover (brave) -> extract (firecrawl/fetch) -> convert (markitdown) -> structure (8F) -> publish (notebooklm).

## Strengths

1. **Deepest output library**: 15 research deliverables -- competitive grids, SWOT, market snapshots, trend reports, benchmark reports, executive summaries, content factory landscapes, SDK audits. No other nucleus has this breadth of analytical templates.
2. **Structured research contracts**: 6 schema contracts enforce citation formats, source quality standards, research depth levels, and trend detection methodology. These are unique to N01 -- other nuclei have no equivalent quality contracts for external data.
3. **End-to-end external pipeline**: 5 MCP servers give discover-extract-convert-structure-publish capability. N02 shares some servers but uses them for content creation, not structured intelligence.
4. **Broadest kind coverage**: 20 kinds across 5 pillars (P01/P02/P04/P07/P10). This spans the full knowledge-to-evaluation lifecycle. By comparison, N03 covers ~15 kinds focused on P03/P08, and N05 covers ~18 kinds focused on P09/P11.
5. **1M context window**: Enables processing entire codebases, long research papers, and multi-document analysis in a single pass. Critical for competitive intelligence that requires cross-referencing multiple sources.
6. **Knowledge accumulation infrastructure**: Memory tools (select/update/age) + knowledge_index + learning_record kinds enable N01 to build institutional memory across research sessions.

## Gaps (Updated 2026-04-07)

### CLOSED Gaps

| Gap | Resolution | Artifacts Added |
|-----|-----------|----------------|
| ~~memory/ has only 2 artifacts~~ | CLOSED -- now 5 artifacts | learning_record, checkpoint, knowledge_index |
| ~~tools/ has only 1 artifact~~ | CLOSED -- now 4 artifacts | scraping_config, search_config, mcp_server_config |
| ~~agents/ has only 1 artifact~~ | CLOSED -- now 3 artifacts | competitor_tracker, paper_reviewer |
| ~~No benchmark artifacts~~ | CLOSED | p07_benchmark_research_quality |
| ~~No eval_dataset artifacts~~ | CLOSED | p07_eval_dataset_research_outputs |
| ~~No knowledge_index~~ | CLOSED | knowledge_index_intelligence in memory/ |

### Remaining Gaps

| Gap | Impact | Priority | Comparison |
|-----|--------|----------|------------|
| No `embedder_provider` built | Cannot configure embedding models for RAG despite being a P01 kind | Low | Covered functionally by embedding_config |
| No `vector_store` built | Cannot configure vector stores for semantic search | Low | Depends on infra decisions (N05 domain) |
| 12/20 kinds unbuilt | 60% of buildable kinds have zero instances | Low | Expected for v1 -- build on demand |
| No `chunk_strategy` | No document chunking config for long papers via RAG | Low | Partially covered by embedding_config chunking section |

## Agent Card Summary

| Category | Count |
|----------|------:|
| Artifacts in N01_intelligence/ | 110 |
| Kinds I can build | 20 |
| Kinds with instances | 8 |
| Tools relevant to my work | 16 |
| MCP servers | 5 |
| **Total cards in agent card** | **138** |

**Competitive context**: N01 (138) now leads the fleet by artifact count. The 44-artifact growth since v2 audit (2026-04-12) is driven by the research/atlas/ directory -- 34 LLM vocabulary and competitive intelligence atoms. N01's unique strengths: 5 MCP servers (deepest external research stack), 6 schema contracts, 34-atom atlas library, 15 KCs, and 110 total source artifacts. Doctor: 133 PASS, 21 WARN, 1 FAIL (1 failure under investigation).
