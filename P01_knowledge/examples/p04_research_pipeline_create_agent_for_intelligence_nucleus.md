---
id: p04_cli_research_pipeline_intelligence_nucleus
kind: cli_tool
pillar: P04
title: "Research Pipeline for Intelligence Nucleus (N01)"
version: "1.0.0"
created: "2026-04-01"
author: "research-pipeline-builder"
domain: research_pipeline
quality: 8.9
tags: [research-pipeline, STORM, CRAG, CRITIC, N01, intelligence, market-analysis]
keywords: [research, intelligence, STORM, CRAG, CRITIC, multi-source, market-analysis]
triggers: ["research pipeline", "market intelligence", "competitor analysis", "intelligence gathering"]
geo_description: >
  L1: 7-stage research pipeline for N01 intelligence nucleus using STORM+CRAG+CRITIC.
  L2: Multi-perspective query planning, corrective retrieval with quality gates, iterative verification.
  L3: Collects from 30+ sources, scores with CRAG thresholds, synthesizes via Graph-of-Thoughts, verifies with CRITIC.
density_score: 1.0
---
# Research Pipeline for Intelligence Nucleus (N01)

## Pipeline (7 stages)

### Stage 1: INTENT (Classification)
**Model**: Fast classifier (regex + embeddings)  
**Input**: Raw user query  
**Output**: Structured intent (domain, verb, complexity, route)  
**Function**: Parse research request and determine routing to appropriate perspectives

```yaml
intent_classifier:
  domains: [market_analysis, competitor_intel, trend_research, consumer_insights, product_analysis]
  verbs: [analyze, compare, track, monitor, discover, evaluate]
  complexity: [simple, moderate, comprehensive, enterprise]
  routing_rules:
    market_analysis: [buyer, seller, analyst]
    competitor_intel: [competitor, analyst, reviewer]
    trend_research: [trend_analyst, consumer_researcher, marketer]
```

### Stage 2: PLAN (STORM Multi-Perspective)
**Model**: Reasoning model (GPT-5-mini)  
**Input**: Classified intent + domain context  
**Output**: 5 perspectives × 5-7 sub-questions (25-35 total queries)  
**Function**: Generate comprehensive question matrix covering all research angles

```yaml
storm_perspectives:
  buyer:
    focus: "pricing, features, reviews, trust signals, alternatives"
    sub_questions: 5-7
  seller:
    focus: "positioning, pricing strategy, listing optimization, competitive gaps"
    sub_questions: 5-7
  analyst:
    focus: "market trends, volume data, growth patterns, seasonality"
    sub_questions: 5-7
  marketer:
    focus: "keywords, SEO gaps, content opportunities, social proof"
    sub_questions: 5-7
  consumer_researcher:
    focus: "pain points, needs, sentiment, behavioral patterns"
    sub_questions: 5-7
```

### Stage 3: RETRIEVE (CRAG Corrective RAG)
**Model**: APIs + fast scoring model (Gemini-2.5-Flash)  
**Input**: 25-35 sub-questions  
**Output**: Quality-scored results (≥0.7 threshold)  
**Function**: Parallel retrieval from multiple sources with quality gates

```yaml
source_categories:
  inbound:
    - mercadolivre
    - shopee  
    - amazon_br
    - magalu
    - americanas
    crag_threshold: 0.7
  search:
    - serper
    - exa
    - gemini_search
    - brave_search
    crag_threshold: 0.6
  outbound:
    - youtube
    - reddit
    - reclameaqui
    - twitter
    crag_threshold: 0.5
  trends:
    - pytrends
    - keepa
    - semrush
    crag_threshold: 0.4
  rag:
    - local_docs
    - supabase_embeddings
    crag_threshold: 0.8
```

### Stage 4: RESOLVE (Entity Deduplication)
**Model**: Deterministic + embedding similarity  
**Input**: Raw retrieved results  
**Output**: Deduplicated entity dataset  
**Function**: Cross-source entity resolution and duplicate elimination

```yaml
resolution_strategy:
  primary_keys: [ean, gtin, asin, sku]
  similarity_threshold: 0.85
  fields_for_comparison: [title, price, brand, category]
  dedup_algorithm: "embedding_similarity + exact_match"
```

### Stage 5: SCORE (Gartner 7-Dimension)
**Model**: Fast scoring model (Gemini-2.5-Flash)  
**Input**: Deduplicated entities  
**Output**: Multi-dimensional scores per entity  
**Function**: Standardized scoring across all data points

```yaml
gartner_dimensions:
  market_position: {weight: 0.2, scale: "1-10"}
  product_quality: {weight: 0.15, scale: "1-10"}
  pricing_competitiveness: {weight: 0.15, scale: "1-10"}
  customer_satisfaction: {weight: 0.15, scale: "1-10"}
  market_presence: {weight: 0.1, scale: "1-10"}
  innovation_capability: {weight: 0.15, scale: "1-10"}
  financial_viability: {weight: 0.1, scale: "1-10"}
```

### Stage 6: SYNTHESIZE (Graph-of-Thoughts)
**Model**: Multi-model routing by domain  
**Input**: Scored entity dataset  
**Output**: Structured analysis report  
**Function**: Domain-specific synthesis using optimal models per task

```yaml
synthesis_routing:
  numerical_analysis: "gpt-5-mini"
  market_insights: "claude-sonnet"
  trend_identification: "gemini-2.5-pro"
  competitive_positioning: "claude-sonnet"
  consumer_behavior: "gpt-5-mini"
```

### Stage 7: VERIFY (CRITIC Self-Correction)
**Model**: Thinking model (o4-mini)  
**Input**: Synthesis + original source data  
**Output**: Verified, corrected final report  
**Function**: Iterative verification and error correction (max 3 iterations)

```yaml
critic_validation:
  max_iterations: 3
  validation_checks:
    - numerical_accuracy
    - source_attribution
    - logical_consistency
    - contradiction_detection
    - completeness_check
  correction_threshold: 0.8
```

## Sources

### Inbound Sources (Marketplace Data)
| Source | API | Rate Limit | Cost | Auth Required |
|--------|-----|------------|------|---------------|
| MercadoLivre | REST API | 1000/hour | Free tier | MERCADOLIVRE_API_KEY |
| Shopee | Scraping via Firecrawl | 10/min | $0.1/page | FIRECRAWL_API_KEY |
| Amazon BR | Product API | 8640/day | Free | AMAZON_API_KEY |
| Magazine Luiza | Scraping | 5/min | $0.1/page | FIRECRAWL_API_KEY |
| Americanas | Scraping | 5/min | $0.1/page | FIRECRAWL_API_KEY |

### Search Sources (Web Intelligence)
| Source | API | Rate Limit | Cost | Auth Required |
|--------|-----|------------|------|---------------|
| Serper | Google Search API | 2500/day | $0.001/query | SERPER_API_KEY |
| Exa | AI Search | 1000/month | $0.002/query | EXA_API_KEY |
| Gemini Search | Google AI | 1000/day | $0.001/query | GEMINI_API_KEY |
| Brave Search | Search API | 2000/month | $0.003/query | BRAVE_API_KEY |

### Outbound Sources (Social Intelligence)  
| Source | API | Rate Limit | Cost | Auth Required |
|--------|-----|------------|------|---------------|
| YouTube | Data API v3 | 10000/day | Free | YOUTUBE_API_KEY |
| Reddit | REST API | 60/min | Free | REDDIT_CLIENT_ID |
| Reclame Aqui | Scraping | 5/min | $0.1/page | FIRECRAWL_API_KEY |
| Twitter | API v2 | 500K/month | $100/month | TWITTER_BEARER_TOKEN |

### Trend Sources (Market Analysis)
| Source | API | Rate Limit | Cost | Auth Required |
|--------|-----|------------|------|---------------|
| PyTrends | Unofficial Google Trends | 1/3sec | Free | None |
| Keepa | Amazon Price Tracker | 5000/month | €19/month | KEEPA_API_KEY |
| SEMrush | Marketing API | 10000/day | $119/month | SEMRUSH_API_KEY |

### RAG Sources (Internal Knowledge)
| Source | Type | Update Frequency | Auth Required |
|--------|------|------------------|---------------|
| Local Docs | Vector DB | Real-time | None |
| Supabase Embeddings | PostgreSQL + pgvector | Batch updates | SUPABASE_KEY |

## Config Reference

### Environment Variables
```bash
# Required API Keys (no defaults)
SERPER_API_KEY=your_serper_key
FIRECRAWL_API_KEY=your_firecrawl_key
EXA_API_KEY=your_exa_key
GEMINI_API_KEY=your_gemini_key

# Optional API Keys
YOUTUBE_API_KEY=your_youtube_key
REDDIT_CLIENT_ID=your_reddit_id
KEEPA_API_KEY=your_keepa_key
TWITTER_BEARER_TOKEN=your_twitter_token
```

### Budget Configuration
```yaml
budget_controls:
  firecrawl:
    monthly_limit: 3000
    per_research_limit: 10
    cost_per_page: 0.10
  serper:
    daily_limit: 100
    cost_per_query: 0.001
  exa:
    monthly_limit: 1000
    cost_per_query: 0.002
```

### Multi-Model Routing
```yaml
model_assignments:
  stage1_intent: "regex + embeddings"
  stage2_storm: "gpt-5-mini"
  stage3_crag: "gemini-2.5-flash"
  stage4_resolve: "deterministic + embeddings"
  stage5_score: "gemini-2.5-flash"
  stage6_synthesize:
    numerical: "gpt-5-mini"
    insights: "claude-sonnet"
    trends: "gemini-2.5-pro"
  stage7_critic: "o4-mini"
```

## Quality Gates

### CRAG Quality Thresholds (per source type)
```yaml
quality_thresholds:
  inbound_sources: 0.7    # High quality for marketplace data
  search_sources: 0.6     # Medium quality for web search
  outbound_sources: 0.5   # Lower threshold for social data
  trend_sources: 0.4      # Directional data, not precise
  rag_sources: 0.8        # Internal docs should be high quality
```

### CRITIC Validation Gates
```yaml
critic_gates:
  max_iterations: 3
  correction_threshold: 0.8
  validation_dimensions:
    numerical_accuracy: 0.9
    source_attribution: 0.85
    logical_consistency: 0.8
    contradiction_detection: 0.9
    completeness: 0.7
```

### Pipeline Success Criteria
```yaml
success_metrics:
  minimum_sources_per_perspective: 3
  minimum_total_data_points: 50
  maximum_duplicate_rate: 0.15
  minimum_quality_score: 8.0
  maximum_processing_time: 300  # 5 minutes
```

### Fallback Strategy
```yaml
fallback_chains:
  primary_search_fail: ["serper", "exa", "brave_search"]
  marketplace_scrape_fail: ["firecrawl", "direct_request", "skip"]
  model_timeout: ["retry_once", "fallback_model", "cache_response"]
  budget_exceeded: ["reduce_sources", "cache_previous", "manual_alert"]
```