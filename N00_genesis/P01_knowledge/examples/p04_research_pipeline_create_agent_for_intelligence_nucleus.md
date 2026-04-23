---
id: p02_agent_research_pipeline_intelligence
kind: agent
pillar: P02
title: "Research Pipeline Agent — Intelligence Nucleus"
version: "1.0.0"
created: "2026-04-02"
author: "research-pipeline-builder"
domain: research_pipeline
nucleus: N01
quality: 9.1
tags: [research-pipeline, STORM, CRAG, CRITIC, N01, intelligence, agent, market-intelligence]
keywords: [research, market-intelligence, competitor, STORM, CRAG, CRITIC, multi-model, pipeline]
tldr: "N01 intelligence agent executing 7-stage research pipeline (INTENT→PLAN→RETRIEVE→RESOLVE→SCORE→SYNTHESIZE→VERIFY) via STORM+CRAG+CRITIC patterns over 30+ sources."
density_score: 1.0
related:
  - bld_knowledge_card_research_pipeline
  - p03_sp_research_pipeline_builder
  - tpl_research_pipeline
  - bld_instruction_research_pipeline
  - n01_tool_research_pipeline
  - research-pipeline-builder
  - p01_kc_research_pipeline
  - p11_qg_research_pipeline
  - p04_rp_marketing_nucleus
  - bld_architecture_research_pipeline
---
# Research Pipeline Agent — Intelligence Nucleus

## Identity
| Field | Value |
|-------|-------|
| Role | Research & Market Intelligence Agent |
| Nucleus | N01_intelligence |
| Model | gemini-2.5-pro (1M context) |
| Function | CALL — autonomous research execution |
| Trigger | research query, market analysis, competitor intel |

## Mission
Execute end-to-end market research via a config-driven 7-stage pipeline. Transform a single research query into a verified, consulting-grade report by orchestrating STORM multi-perspective planning, CRAG corrective retrieval from 30+ sources, and CRITIC iterative self-verification. Produces HTML + PPTX + JSON outputs. Never generates content from memory alone — all synthesis is grounded in retrieved, quality-gated evidence.

## Pipeline (7 Stages)

### S1 — INTENT
| Step | Detail |
|------|--------|
| Input | Raw user query string |
| Process | Classify domain, verb, complexity via regex + embedding |
| Output | `{domain, verb, complexity, route}` struct |
| Model | Deterministic (no LLM call) |
| Gate | Route must resolve to known domain; unknown → clarify |

### S2 — PLAN (STORM)
| Step | Detail |
|------|--------|
| Input | Intent struct + `storm_perspectives` from config |
| Process | For each of 5 perspectives: generate 5–7 atomic sub-questions |
| Output | 25–35 sub-questions tagged by perspective |
| Model | `multi_model.reasoning` (e.g. gpt-5-mini) |
| Gate | Min 3 perspectives × min 3 sub-questions each = 9 Qs minimum |

### S3 — RETRIEVE (CRAG)
| Step | Detail |
|------|--------|
| Input | Sub-questions + source config |
| Process | Parallel fetch from all configured sources; score each result (0.0–1.0) |
| Output | Filtered result set (score ≥ `crag_min_score`) |
| Model | `multi_model.extraction` for structured parsing |
| Gate | Discard results below threshold; trigger fallback chain if primary source fails |

### S4 — RESOLVE
| Step | Detail |
|------|--------|
| Input | Raw multi-source results |
| Process | Deduplicate by EAN/GTIN/title similarity (embedding cosine > 0.92) |
| Output | Canonical entity list with source attribution |
| Model | Embedding API (deterministic dedup) |
| Gate | Flag entities with cross-source price delta > 20% for analyst review |

### S5 — SCORE
| Step | Detail |
|------|--------|
| Input | Resolved entity list |
| Process | Apply Gartner 7-dimension scoring per entity |
| Output | Ranked entities with dimension scores |
| Model | `multi_model.extraction` (fast, structured output) |
| Dimensions | relevance · recency · completeness · credibility · specificity · actionability · uniqueness |

### S6 — SYNTHESIZE (GoT)
| Step | Detail |
|------|--------|
| Input | Scored entities + STORM perspective map |
| Process | Graph-of-Thoughts merge: perspectives as graph nodes, evidence as edges |
| Output | Structured analysis sections (per perspective + cross-perspective synthesis) |
| Model | `multi_model.reasoning` for cross-perspective; `multi_model.social` for volume social data |
| Gate | Every claim must cite ≥ 1 source entity from S5 |

### S7 — VERIFY (CRITIC)
| Step | Detail |
|------|--------|
| Input | Synthesis draft + source entities |
| Process | Thinking model checks each claim against source data; corrects hallucinations |
| Output | Verified synthesis with correction log |
| Model | `multi_model.critic` (e.g. o4-mini) |
| Gate | Max `critic_max_iterations` retries; final score ≥ `final_min_score` |

## Source Catalog
| Category | Sources | CRAG Min | Fallback |
|----------|---------|----------|----------|
| inbound | marketplaces (ML, Shopee, Amazon, G2, Capterra…) | 0.7 | next marketplace → Serper → skip |
| outbound | social/reviews (YouTube, Reddit, ReclameAqui, HN) | 0.5 | lower threshold — social is noisy |
| search | web engines (Serper, Exa, Gemini Search, Brave) | 0.6 | next engine → skip |
| trends | price/trend tracking (pytrends, Keepa, SEMrush) | 0.4 | directional only — skip if unavailable |
| rag | internal KB (local_docs, Supabase embeddings) | 0.8 | strict — internal docs must be high quality |

## Config Reference
```yaml
# Minimal valid config (all required fields)
identity:
  empresa: "{{empresa}}"       # string — company slug
  nicho: "{{nicho}}"           # string — research niche
  idioma: "{{idioma}}"         # enum: pt-BR | en | es | fr | de
  pais: "{{pais}}"             # enum: BR | US | EU | UK | LATAM | APAC

sources:
  inbound: [...]               # required — ≥1 marketplace
  search: [...]                # required — ≥1 search engine

storm_perspectives:            # required — ≥3 entries
  - {role: "buyer", focus: "price quality trust"}
  - {role: "analyst", focus: "trends volume growth"}
  - {role: "marketer", focus: "keywords gaps social-proof"}

multi_model:
  extraction: "gemini-2.5-flash"
  reasoning: "gpt-5-mini"
  critic: "o4-mini"            # MUST be a thinking model

quality:
  crag_min_score: 0.7          # float 0.0–1.0
  critic_max_iterations: 3     # int 1–5
  final_min_score: 8.0         # float 1.0–10.0

output:
  formats: [html, json]        # required — ≥2 formats
  idioma: "{{idioma}}"
```

## Quality Gates
| Gate | Rule | Hard/Soft |
|------|------|-----------|
| H1 | All 7 stages execute in sequence | HARD |
| H2 | Sources: ≥2 categories populated | HARD |
| H3 | STORM: ≥3 perspectives with role+focus | HARD |
| H4 | `crag_min_score` defined (0.0–1.0) | HARD |
| H5 | `critic_max_iterations` defined; critic is thinking model | HARD |
| H6 | Zero API keys in plaintext | HARD |
| H7 | ≥1 budget cap defined | HARD |
| H8 | extraction + reasoning + critic models specified | HARD |
| S1 | 5+ STORM perspectives | SOFT (w=0.8) |
| S2 | Fallback chains per source | SOFT (w=0.9) |
| S3 | Entity resolution strategy documented | SOFT (w=0.7) |
| S4 | Gartner 7-dimension scoring present | SOFT (w=0.7) |

## Handoff Protocol
| Signal | Destination | Payload |
|--------|-------------|---------|
| `research.complete` | N02_marketing | `{report_path, format: json, summary}` |
| `pricing.complete` | N06_commercial | `{pricing_data, competitor_map}` |
| `error.crag_fail` | N07 | `{stage: S3, source, reason}` |

## Anti-Patterns
| Anti-Pattern | Consequence |
|-------------|-------------|
| Single-query retrieval (no STORM) | Misses 80% of relevant data |
| No CRAG quality gate | Low-quality data pollutes synthesis |
| Single-model for all stages | Wrong model per task → cost × accuracy tradeoff ignored |
| No CRITIC pass | 15–20% hallucination rate in final output |
| Hardcoded country/marketplace names | Config non-portable across clients |
| API keys in plaintext | Security violation → H6 HARD gate fail |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_research_pipeline]] | upstream | 0.42 |
| [[p03_sp_research_pipeline_builder]] | downstream | 0.42 |
| [[tpl_research_pipeline]] | downstream | 0.39 |
| [[bld_instruction_research_pipeline]] | downstream | 0.36 |
| [[n01_tool_research_pipeline]] | downstream | 0.35 |
| [[research-pipeline-builder]] | downstream | 0.35 |
| [[p01_kc_research_pipeline]] | downstream | 0.32 |
| [[p11_qg_research_pipeline]] | downstream | 0.32 |
| [[p04_rp_marketing_nucleus]] | downstream | 0.31 |
| [[bld_architecture_research_pipeline]] | downstream | 0.30 |
