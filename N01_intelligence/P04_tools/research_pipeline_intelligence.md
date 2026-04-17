---
id: n01_tool_research_pipeline
kind: cli_tool
pillar: P04
title: "Research Pipeline — N01 Intelligence Tool"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: research-pipeline-builder
domain: research_pipeline
nucleus: N01
quality: 9.1
tags: [cli-tool, research-pipeline, N01, intelligence, STORM, CRAG, CRITIC]
tldr: "Market intelligence pipeline for N01. 7-stage STORM+CRAG+CRITIC with 30+ sources, multi-model routing, budget-aware."
density_score: 0.92
---

# Research Pipeline — Intelligence Tool

## Purpose
Automated market intelligence for any business served by N01 Intelligence. Reads a company-specific YAML config and executes a 7-stage research pipeline: classify intent, plan multi-perspective queries (STORM), retrieve from 30+ sources in parallel with quality gates (CRAG), deduplicate entities, score on 7 dimensions, synthesize with domain-specific models, and verify with a thinking model (CRITIC).

## Pipeline
```
QUERY ─► S1 INTENT (classify domain, route)
           │
           ▼
         S2 PLAN/STORM (5 perspectives × 5-7 sub-Qs)
           │
           ▼
         S3 RETRIEVE/CRAG (parallel, score ≥0.7)
           │
           ▼
         S4 RESOLVE (entity dedup cross-source)
           │
           ▼
         S5 SCORE (Gartner 7-dim)
           │
           ▼
         S6 SYNTHESIZE/GoT (domain models)
           │
           ▼
         S7 VERIFY/CRITIC (thinking model, max 3 iter)
           │
     ┌─────┼─────┐
     ▼     ▼     ▼
   HTML  PPTX  JSON
```

## Usage
```bash
# Full research from config
python research_pipeline.py --config config.yaml --query "mercado de acessorios para gatos"

# Specific stages only
python research_pipeline.py --config config.yaml --query "..." --stages 1-3

# Dry run (plan only, no retrieval)
python research_pipeline.py --config config.yaml --query "..." --dry-run
```

## Source Categories
| Category | Purpose | Examples |
|----------|---------|---------|
| Inbound | Product/marketplace data | MercadoLivre, Shopee, Amazon, G2 |
| Outbound | Social intelligence | YouTube, Reddit, ReclameAqui |
| Search | Web search engines | Serper, Exa, Brave, Tavily |
| Trends | Price/trend tracking | Google Trends, Keepa |
| RAG | Internal knowledge | Company docs, embeddings |

## Config Reference
Company config: `_instances/{company}/N01_intelligence/research_pipeline_config.yaml`
Template: `P04_tools/templates/tpl_research_pipeline.md`

## Quality Gates
- 7 stages complete ✓
- CRAG score ≥ 0.7 per result ✓
- CRITIC max 3 iterations ✓
- Budget caps enforced ✓
- Zero plaintext secrets ✓

## Nucleus Integration
| Direction | Target | Data |
|-----------|--------|------|
| N01 → N02 | Marketing | Research insights for content strategy |
| N01 → N06 | Commercial | Pricing intelligence, competitor data |
| N01 → N03 | Engineering | Technical research for implementation |
| N01 → N07 | Admin | Research reports for decision-making |
