---
id: deck_n04
kind: context_doc
title: N04 Deck -- Available Capabilities
nucleus: N04
sin: Gula por Conhecimento
version: 1.0.0
pillar: P01
quality: null
created: 2026-04-07
---

## Identity

| Attribute | Value |
|-----------|-------|
| Nucleus | N04 -- Knowledge Management |
| Sin | Gula por Conhecimento (Gluttony for Knowledge) |
| CLI | Claude (Opus 4.6, 1M context) |
| Domain | RAG pipelines, knowledge cards, embeddings, chunking, retrieval, taxonomy, memory |
| Reasoning | 8F mandatory (F1-F8) on every task |
| Quality | null (never self-score -- peer review assigns) |

**Routing TO N04**: knowledge cards, RAG, embeddings, chunking, indexing, taxonomy, documentation, memory management, glossary, brain indexes, context docs.

**Routing AWAY**: research papers (N01), marketing copy (N02), build scaffold (N03), deploy/CI (N05), pricing/funnels (N06).

---

## My Artifacts

| Subdir | Count | Purpose |
|--------|------:|---------|
| agents | 1 | Agent definition for knowledge nucleus |
| architecture | 1 | Agent card (capabilities + routing) |
| feedback | 1 | Quality gate feedback records |
| knowledge | 8 | Core domain artifacts: chunk strategy, embedding configs, KCs, RAG sources, retriever config |
| memory | 2 | Memory index + RAG pipeline memory |
| orchestration | 4 | Dispatch rules (knowledge, Supabase) + workflows (knowledge, Supabase setup) |
| output | 15 | Deliverables: KC audits, gap reports, embedding batches, taxonomy maps, knowledge graphs, finetune datasets, SQL migrations, competitive intel, curriculum, SDK validation |
| prompts | 1 | System prompt for N04 persona |
| quality | 2 | Quality gate + scoring rubric for knowledge artifacts |
| schemas | 7 | Contracts: database schema, embedding, export format, freshness, KC structure, naming convention, taxonomy |
| tools | 1 | Supabase data layer tool |
| compiled | 43 | YAML compilations of all above |
| **TOTAL** | **43 source + 43 compiled** | |

---

## Kinds I Build

22 kinds fall within N04's domain across pillars P01, P02, P04, and P10:

| Kind | Pillar | Naming Pattern |
|------|--------|----------------|
| brain_index | P10 | `p10_bi_{{index}}.yaml` |
| chunk_strategy | P01 | `p01_chunk_{{strategy}}.md` |
| compression_config | P10 | `p10_cc_{{scope}}.yaml` |
| context_doc | P01 | `p01_ctx_{{topic}}.md + .yaml` |
| document_loader | P04 | `p04_loader_{{format}}.md + .yaml` |
| embedder_provider | P01 | `p01_ep_{{provider}}.yaml` |
| embedding_config | P01 | `p01_emb_{{model}}.yaml` |
| entity_memory | P10 | `p10_entity_{{name}}.md` |
| few_shot_example | P01 | `p01_fse_{{topic}}.md + .yaml` |
| glossary_entry | P01 | `p01_gl_{{term}}.md + .yaml` |
| knowledge_card | P01 | `p01_kc_{{topic}}.md + .yaml` |
| learning_record | P10 | `p10_lr_{{topic}}.md + .yaml` |
| memory_scope | P02 | `p02_memscope_{{agent}}.md` |
| memory_summary | P10 | `p10_summary_{{scope}}.md` |
| memory_type | P10 | `p10_mt_{{type_name}}.yaml` |
| rag_source | P01 | `p01_rs_{{source}}.md + .yaml` |
| retriever | P04 | `p04_retr_{{store}}.md + .yaml` |
| retriever_config | P01 | `p01_retr_cfg_{{store}}.md` |
| runtime_state | P10 | `p10_rs_{{agent}}.yaml` |
| session_backend | P10 | `p10_sb_{{backend}}.yaml` |
| session_state | P10 | `p10_ss_{{session}}.yaml` |
| vectordb_backend | P01 | `p01_vdb_{{backend}}.yaml` |

---

## Tools I Use

| Tool | Purpose |
|------|---------|
| `cex_compile.py` | .md -> .yaml compilation (mandatory after every save) |
| `cex_retriever.py` | TF-IDF artifact similarity search (2184 docs, 12K vocab) |
| `cex_query.py` | TF-IDF builder discovery (361L) |
| `cex_kc_index.py` | Knowledge card indexing |
| `cex_index.py` | General artifact indexing |
| `cex_memory_select.py` | Relevant memory injection (keyword + LLM) |
| `cex_memory_update.py` | Memory decay + append + prune |
| `cex_memory_types.py` | 4-type memory taxonomy: correction/preference/convention/context |
| `cex_memory_age.py` | Freshness caveats, age labels, linear decay over 365d |
| `cex_token_budget.py` | Token counting + budget allocation |
| `cex_score.py` | Peer review scoring (--apply) |
| `cex_doctor.py` | Builder health check |
| `cex_evolve.py` | AutoResearch loop: evolve artifacts autonomously |
| `cex_prompt_layers.py` | Compiled artifact scanner: loads 15+ pillar artifacts into prompts |
| `cex_schema_hydrate.py` | Hydrate ISOs with universal patterns |
| `cex_research.py` | Research tool for knowledge gathering |
| `cex_skill_loader.py` | Builder ISO loader: 13 ISOs per kind |

---

## MCP Servers

5 external services connected via `.mcp-n04.json`:

| Server | Purpose |
|--------|---------|
| **supabase** | Supabase MCP server -- project management, schema ops, RLS policies |
| **postgres** | Direct PostgreSQL access to Supabase database -- SQL queries, migrations |
| **fetch** | HTTP fetch server -- retrieve web content, APIs, documentation |
| **firecrawl** | Web crawling + scraping -- bulk content extraction for KC authoring |
| **notebooklm** | NotebookLM MCP -- content pipeline for audio/podcast generation from KCs |

---

## My Strengths

1. **Knowledge Card Factory**: 8 core knowledge artifacts + 15 output deliverables. Heaviest output subdir of any N04 capability.
2. **Schema Contracts**: 7 contracts define structure for databases, embeddings, exports, freshness, KC structure, naming, and taxonomy. This is the governance backbone.
3. **RAG Pipeline Depth**: Covers the full RAG stack: embedding config -> chunk strategy -> retriever config -> rag source -> vectordb backend.
4. **Supabase Integration**: Dedicated embedding config, dispatch rule, workflow, data layer tool, and KC for Supabase. Plus 2 MCP servers (supabase + postgres).
5. **Memory Management**: 10 kinds under P10 (brain_index through session_state) + 4 memory tools. N04 owns the memory pillar.
6. **Output Variety**: Produces 15 distinct output types: audits, graphs, taxonomies, datasets, migrations, curricula, competitive intel.

---

## My Gaps

| Subdir/Area | Status | Notes |
|-------------|--------|-------|
| agents | Thin (1) | Only `agent_knowledge.md`. No sub-agents for specialized tasks (e.g., taxonomy agent, embedding agent). |
| tools | Thin (1) | Only Supabase data layer tool. Missing: taxonomy builder tool, KC validator tool, embedding batch tool. |
| architecture | Thin (1) | Single agent card. No architecture diagrams, no RAG pipeline architecture doc. |
| prompts | Thin (1) | Single system prompt. No specialized prompts for different knowledge tasks. |
| feedback | Thin (1) | Single quality gate feedback. No learning records, no iteration history. |
| memory | Thin (2) | Index + pipeline. Missing: taxonomy memory, domain-specific memory scopes. |
| brain_index | Missing (0) | Kind exists (P10) but no artifacts built yet. |
| entity_memory | Missing (0) | Kind exists (P10) but no artifacts built yet. |
| document_loader | Missing (0) | Kind exists (P04) but no artifacts built yet. |
| few_shot_example | Missing (0) | Kind exists (P01) but no artifacts for knowledge domain. |
| glossary_entry | Missing (0) | Kind exists (P01) but no glossary terms authored yet. |

---

## Cards in My Deck

| Category | Count |
|----------|------:|
| Source artifacts (.md) | 43 |
| Compiled artifacts (.yaml) | 43 |
| Kinds I can build | 22 |
| Tools in my toolkit | 17 |
| MCP servers | 5 |
| Builder ISOs per kind | 13 |
| Sub-agent definitions | 9 |
| Schema contracts | 7 |
| Output types | 15 |
| **Total capability cards** | **118** |

> 43 artifacts + 22 kinds + 17 tools + 5 MCPs + 9 sub-agents + 7 contracts + 15 output types = **118 cards in deck**
