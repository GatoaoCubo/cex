---
id: n01_kc_source_catalog
kind: knowledge_card
pillar: P01
title: "Knowledge Card — Research Source Catalog (30+ Sources)"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: research-pipeline-builder
domain: research_pipeline
nucleus: N01
quality: 9.1
tags: [knowledge-card, sources, APIs, marketplace, search, social, N01, intelligence]
tldr: "Complete catalog of 30+ data sources for research pipeline: marketplaces, search engines, social platforms, trends, and internal RAG."
density_score: 0.93
related:
  - bld_tools_research_pipeline
  - ex_research_pipeline_ecommerce_br
  - bld_knowledge_card_search_tool
  - bld_config_research_pipeline
  - search-tool-builder
  - p09_env_firecrawl
  - bld_collaboration_search_tool
  - p04_tool_search_config
  - n06_api_access_pricing
  - tpl_research_pipeline
---

# Research Source Catalog — 30+ Sources

## Inbound — Marketplace / Product Sources
| Source | Method | Auth Env | Cost | Rate Limit | Data Fields |
|--------|--------|----------|------|-----------|-------------|
| MercadoLivre | REST API v3 | ML_APP_ID + ML_SECRET | Free | 10K/day | title, price, sold_qty, rating, seller, shipping |
| Shopee | Affiliate API + scrape | SHOPEE_AFFILIATE_KEY | Free | 1K/day | title, price, shop_rating, flash_sale, reviews |
| Amazon BR | Keepa + Firecrawl | KEEPA_KEY + FIRECRAWL_KEY | €19+$19/mo | 5/min + 10/min | title, price, BSR, reviews, price_history |
| Magalu | Firecrawl | FIRECRAWL_KEY | credits | 10/min | title, price, rating, seller |
| Americanas | Firecrawl | FIRECRAWL_KEY | credits | 10/min | title, price, rating |
| Casas Bahia | Firecrawl | FIRECRAWL_KEY | credits | 10/min | title, price, rating |
| Shein | Firecrawl | FIRECRAWL_KEY | credits | 10/min | title, price, reviews |
| Temu | Firecrawl | FIRECRAWL_KEY | credits | 10/min | title, price, sold_qty |

## Search — Web Search Engines
| Source | API Endpoint | Auth Env | Cost | Specialty |
|--------|-------------|----------|------|-----------|
| Serper | google.serper.dev/search | SERPER_API_KEY | $0.30/1K | Google SERP (fastest) |
| Exa | api.exa.ai/search | EXA_API_KEY | ~$0.10/q | Neural search (papers) |
| Gemini Search | Gemini grounding | GOOGLE_API_KEY | included | Google with grounding |
| OpenAI Search | Responses API | OPENAI_API_KEY | per-token | GPT web search |
| Brave | api.search.brave.com | BRAVE_API_KEY | 2K free/mo | Privacy-focused |
| Tavily | api.tavily.com/search | TAVILY_API_KEY | 1K free/mo | Research-grade |

## Outbound — Social / Review / Community
| Source | Method | Auth Env | Data |
|--------|--------|----------|------|
| YouTube | Data API v3 + transcripts | YOUTUBE_API_KEY | videos, transcripts, comments |
| Reddit | OAuth REST API | REDDIT_CLIENT_ID | posts, comments, sentiment |
| ReclameAqui | Firecrawl scrape | FIRECRAWL_KEY | complaints, ratings |
| Twitter/X | Firecrawl + Serper | varies | posts, engagement |
| HackerNews | Firebase API | none (public) | posts, comments |

## Trends — Price / Trend Tracking
| Source | Method | Auth | Data |
|--------|--------|------|------|
| Google Trends | pytrends (unofficial) | none | search volume, related queries, geo |
| Keepa | REST API | KEEPA_KEY | Amazon price history, BSR, inventory |

## RAG — Internal Knowledge
| Source | Method | Data |
|--------|--------|------|
| Local docs | Embedding + vector search | Company documents, past research |
| Supabase pgvector | SQL + embedding | Structured internal knowledge |

## Fallback Chains
```
Marketplace: API direct → Firecrawl scrape → Serper site:search → skip
Search: Serper → Brave → Tavily → Exa → skip
Social: YouTube API → Serper site:youtube → skip
Trends: pytrends → Serper trends → skip
```

## Cost Summary (typical monthly)
| Source | Cost | Usage |
|--------|------|-------|
| Firecrawl | $19/mo (3K credits) | ~300 marketplace scrapes |
| Serper | ~$15/mo | ~50K queries |
| Keepa | €19/mo (5K tokens) | Amazon data |
| Exa | ~$10/mo | ~100 neural searches |
| YouTube | Free | 10K queries/day |
| pytrends | Free | ~100 trend queries |
| **Total** | **~$65/mo** | Full research capability |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_research_pipeline]] | downstream | 0.76 |
| [[ex_research_pipeline_ecommerce_br]] | downstream | 0.41 |
| [[bld_knowledge_card_search_tool]] | sibling | 0.38 |
| [[bld_config_research_pipeline]] | downstream | 0.37 |
| [[search-tool-builder]] | downstream | 0.31 |
| [[p09_env_firecrawl]] | downstream | 0.31 |
| [[bld_collaboration_search_tool]] | downstream | 0.26 |
| [[p04_tool_search_config]] | downstream | 0.26 |
| [[n06_api_access_pricing]] | downstream | 0.25 |
| [[tpl_research_pipeline]] | downstream | 0.24 |
