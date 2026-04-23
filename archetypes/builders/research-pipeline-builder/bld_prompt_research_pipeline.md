---
kind: instruction
id: bld_instruction_research_pipeline
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for research pipeline artifacts
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Research Pipeline"
version: "1.0.0"
author: n03_builder
tags: [research_pipeline, builder, examples]
tldr: "Golden and anti-examples for research pipeline construction, demonstrating ideal structure and common pitfalls."
domain: "research pipeline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_research_pipeline_builder
  - p11_qg_research_pipeline
  - p02_agent_research_pipeline_intelligence
  - n01_tool_research_pipeline
  - research-pipeline-builder
  - bld_instruction_e2e_eval
  - bld_architecture_research_pipeline
  - bld_knowledge_card_research_pipeline
  - tpl_research_pipeline
  - p01_kc_research_pipeline
---

# Instructions: How to Produce a research_pipeline

## Phase 1: RESEARCH
1. Identify target business: niche, country, language, marketplace landscape
2. Catalog available data sources by category (inbound/outbound/search/trends/RAG)
3. For each source: document API, auth, rate limit, cost, data quality
4. Define STORM perspectives relevant to the niche (5 expert angles)
5. Choose multi-model routing: which model handles which stage/domain
6. Set budget constraints: monthly caps, per-research limits, credit pools
7. Define output requirements: formats (HTML/PPTX/JSON), language, template style
8. Check existing research_pipeline artifacts to avoid config overlap

## Phase 2: COMPOSE
1. Read bld_schema_research_pipeline.md — source of truth for config fields
2. Read bld_output_template_research_pipeline.md — template structure
3. Fill frontmatter: id, kind, pillar, title, version, quality: null
4. Write Pipeline section: 7 stages with detail per stage:
   - **Stage 1 INTENT**: classify domain, verb, complexity → route
   - **Stage 2 PLAN (STORM)**: 5 perspectives × 5-7 sub-questions each
   - **Stage 3 RETRIEVE (CRAG)**: parallel fetch from sources, quality gate per result
   - **Stage 4 RESOLVE**: entity dedup cross-source (EAN/GTIN/title similarity)
   - **Stage 5 SCORE**: Gartner 7-dimension scoring per listing/result
   - **Stage 6 SYNTHESIZE (GoT)**: Graph-of-Thoughts merge via domain-specific models
   - **Stage 7 VERIFY (CRITIC)**: thinking model verifies, correct (max 3 iterations)
5. Write Source Catalog: all sources grouped by category
6. Write Config Schema: all variable fields grouped by section
7. Write Multi-Model Routing: model per stage/domain with cost rationale
8. Write Budget Controls: monthly caps, per-research limits
9. Write Quality Gates: CRAG thresholds, CRITIC iterations, final minimum
10. Ensure zero hardcoded country/marketplace names — ALL via config

## Phase 3: VALIDATE
1. Check all 7 pipeline stages documented with input/output/model
2. Verify source catalog covers 4 categories (inbound, outbound, search, trends)
3. Verify no API keys in plaintext — only ENV_VAR references
4. Verify STORM perspectives are costmizable (not hardcoded)
5. Verify budget controls present (monthly + per-research)
6. Verify CRAG quality gate has minimum score threshold
7. Verify CRITIC has max iterations defined
8. Verify multi-model routing specifies model per stage
9. Check body <= 4096 bytes per file


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_research_pipeline_builder]] | related | 0.45 |
| [[p11_qg_research_pipeline]] | downstream | 0.40 |
| [[p02_agent_research_pipeline_intelligence]] | upstream | 0.36 |
| [[n01_tool_research_pipeline]] | downstream | 0.35 |
| [[research-pipeline-builder]] | downstream | 0.34 |
| [[bld_instruction_e2e_eval]] | sibling | 0.33 |
| [[bld_architecture_research_pipeline]] | downstream | 0.33 |
| [[bld_knowledge_card_research_pipeline]] | upstream | 0.32 |
| [[tpl_research_pipeline]] | downstream | 0.32 |
| [[p01_kc_research_pipeline]] | downstream | 0.30 |
