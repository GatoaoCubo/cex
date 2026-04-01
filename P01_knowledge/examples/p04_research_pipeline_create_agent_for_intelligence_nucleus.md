---
id: p04_cli_research_pipeline_intelligence
kind: cli_tool
pillar: P04
title: "Intelligence Research Pipeline — Multi-Source STORM+CRAG+CRITIC"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "research-pipeline-builder"
domain: research_pipeline
quality: 9.0
tags: [research-pipeline, STORM, CRAG, CRITIC, intelligence, multi-source, N01]
keywords: [research, intelligence, STORM, CRAG, CRITIC, multi-model, sources]
tldr: "7-stage intelligence research pipeline combining Stanford STORM (multi-perspective planning), CRAG (quality-gated retrieval), and CRITIC (iterative verification) across 30+ configurable sources"
density_score: 0.89
effort: high
---
# Intelligence Research Pipeline — Multi-Source STORM+CRAG+CRITIC

## Executive Summary

A configurable 7-stage research pipeline that systematically collects, scores, synthesizes, and verifies intelligence from multiple sources. Built on three proven academic patterns: **STORM** (multi-perspective query decomposition), **CRAG** (corrective retrieval with quality gates), and **CRITIC** (iterative self-verification). Designed for N01 intelligence nucleus operations with multi-model routing and budget controls.

## Pipeline Architecture (7 Stages)

### Stage 1: INTENT Classification
- **Input**: Raw user query or research request
- **Process**: Domain classification (market, competitive, technical, social, regulatory)
- **Model**: Fast classifier (regex + embeddings)
- **Output**: Structured intent with domain, verb, complexity, routing decision
- **Example**: "analyze competitor pricing" → {domain: competitive, verb: analyze, complexity: medium}

### Stage 2: PLAN (STORM Multi-Perspective)
- **Input**: Classified intent + domain context
- **Process**: Generate 5 expert perspectives, decompose each into 5-7 atomic sub-questions
- **Model**: Reasoning model (GPT-4, Claude Sonnet, Gemini Pro)
- **Output**: 25-35 focused sub-questions covering all research angles
- **Perspectives**: buyer, competitor, analyst, regulator, technical_expert
- **Example**: "buyer perspective" → ["What drives purchase decisions?", "Price sensitivity thresholds?", "Trust factors?"]

### Stage 3: RETRIEVE (CRAG Quality-Gated)
- **Input**: Decomposed sub-questions from STORM
- **Process**: Parallel retrieval from all configured sources with per-result quality scoring
- **Quality Gate**: Each result scored 0.0-1.0, minimum threshold 0.7 (configurable)
- **Fallback**: Failed results trigger fallback chains or source switching
- **Output**: Quality-filtered dataset with provenance tracking
- **Sources**: 4 categories (inbound/outbound/search/trends) with 30+ total options

### Stage 4: RESOLVE (Entity Deduplication)
- **Input**: Raw results from multiple sources
- **Process**: Cross-source entity resolution using similarity scoring
- **Methods**: EAN/GTIN matching, title similarity, price clustering, feature comparison
- **Output**: Deduplicated entity set with source attribution
- **Example**: Same product from Amazon + eBay + Google Shopping → single entity record

### Stage 5: SCORE (Gartner 7-Dimension Analysis)
- **Input**: Resolved entities with source data
- **Process**: Multi-dimensional scoring per Gartner research methodology
- **Dimensions**: market_position, growth_rate, innovation, customer_satisfaction, financial_strength, strategic_direction, execution_ability
- **Model**: Fast model for structured scoring (Gemini Flash, GPT-3.5-turbo)
- **Output**: Scored entity matrix with dimensional breakdown

### Stage 6: SYNTHESIZE (Graph-of-Thoughts)
- **Input**: Scored entities + original perspectives
- **Process**: Domain-specific model routing for synthesis by data type
- **Routing**: extraction_model for structured data, reasoning_model for analysis, social_model for sentiment
- **Pattern**: Graph-of-Thoughts methodology for complex reasoning chains
- **Output**: Integrated analysis addressing original research question

### Stage 7: VERIFY (CRITIC Self-Correction)
- **Input**: Synthesized analysis + source evidence
- **Process**: Thinking model verifies synthesis against sources, flags inconsistencies
- **Model**: Reasoning-optimized model (o1-mini, Claude-3-opus)
- **Iterations**: Maximum 3 correction cycles (diminishing returns after)
- **Output**: Verified final report with confidence scores and remaining uncertainties

## Source Catalog (30+ Configurable)

### Inbound Sources (Product/Service Data)
| Source | Type | API | Rate Limit | Cost Model |
|--------|------|-----|------------|------------|
| Amazon Product API | Marketplace | REST | 2000/hour | $0.50/1K requests |
| Google Shopping | Marketplace | API | 100/day free | Quota-based |
| Mercado Livre | Marketplace | REST | 5000/day | Free tier |
| Shopify Admin | E-commerce | GraphQL | 40/second | Free with store |
| G2 Reviews | SaaS Reviews | REST | 100/day | $299/month |
| Capterra | Software | Scraping | Manual | Firecrawl credits |

### Outbound Sources (Social/Community)
| Source | Type | API | Rate Limit | Cost Model |
|--------|------|-----|------------|------------|
| Reddit | Social | OAuth2 | 60/minute | Free |
| YouTube Data | Video | v3 API | 10K/day | Free quota |
| Twitter/X | Social | v2 API | 300/15min | $100/month |
| TikTok Research | Social | Academic | 100/day | Application required |
| Reclame Aqui | Reviews | Scraping | Manual | Firecrawl credits |
| Product Hunt | Tech News | GraphQL | 1000/hour | Free |

### Search Sources (Web Intelligence)
| Source | Type | API | Rate Limit | Cost Model |
|--------|------|-----|------------|------------|
| Serper Google | Search | REST | 100/minute | $0.30/1K queries |
| Exa AI | Semantic | REST | 60/minute | $0.10/query |
| Brave Search | Privacy | REST | 2000/month | Free tier |
| Tavily | Research | REST | 1000/month | $0.02/query |
| Gemini Search | AI-powered | REST | Model-dependent | Model pricing |

### Trends Sources (Market Intelligence)
| Source | Type | API | Rate Limit | Cost Model |
|--------|------|-----|------------|------------|
| Google Trends | Public | pytrends | 1 req/3sec | Free (unofficial) |
| Keepa Amazon | Price tracking | REST | 5/minute | €19/month |
| SemRush | SEO/Keywords | REST | 10K/month | $119/month |
| Ahrefs | Backlinks | REST | 1000/month | $99/month |
| Social Blade | Creator stats | Scraping | Manual | Firecrawl credits |

## Configuration Schema

### Identity (Required)
```yaml
identity:
  organization: string          # Organization name
  domain: string               # Intelligence domain focus
  language: enum               # pt-BR, en, es, fr, de
  region: enum                # BR, US, EU, UK, LATAM, APAC
```

### Sources (Minimum 2 Categories)
```yaml
sources:
  inbound: [list]             # Marketplace/product sources
  outbound: [list]            # Social/community sources  
  search: [list]              # Web search engines
  trends: [list]              # Trend/tracking sources
  rag: [list]                 # Internal knowledge base
```

### STORM Perspectives (Minimum 3)
```yaml
storm_perspectives:
  - role: string              # Expert perspective role
    focus: string             # Research focus areas
  - role: analyst
    focus: "market sizing growth trends competitive landscape"
  - role: customer
    focus: "pain points needs satisfaction switching costs"
  - role: competitor
    focus: "positioning pricing features roadmap strategy"
  - role: regulator
    focus: "compliance requirements policy changes risks"
  - role: technical_expert
    focus: "capabilities limitations architecture scalability"
```

### Multi-Model Routing
```yaml
multi_model:
  extraction: string          # Fast model for structured data
  reasoning: string           # Strong model for analysis
  social: string              # Optimized for sentiment/social
  critic: string              # Thinking model for verification
```

### Budget Controls
```yaml
budget:
  serper_daily: int           # Daily Serper query limit
  firecrawl_monthly: int      # Monthly Firecrawl credits
  firecrawl_per_research: int # Credits per research session
  api_monthly_cap: int        # Total monthly API spend limit
```

### Quality Gates
```yaml
quality:
  crag_min_score: float       # Minimum retrieval quality (0.0-1.0)
  critic_max_iterations: int  # Maximum verification cycles
  final_min_score: float      # Minimum final report score
  confidence_threshold: float # Minimum confidence for conclusions
```

## Implementation Example

### N01 Intelligence Nucleus Deployment
```bash
# 1. Configure for organization
cp templates/research_pipeline_config.yaml N01_intelligence/config/
vim N01_intelligence/config/research_pipeline_config.yaml

# 2. Deploy pipeline
python N01_intelligence/tools/research_pipeline.py \
  --config config/research_pipeline_config.yaml \
  --query "competitive analysis of AI coding assistants" \
  --output reports/competitor_analysis_2026_04.html

# 3. Monitor execution
tail -f logs/research_pipeline.log
```

### Quality Assurance Workflow
```yaml
# CRAG Quality Gate (per-source)
marketplace_sources:
  min_score: 0.7
  fallback: next_source
search_sources:
  min_score: 0.6
  fallback: alternative_engine
social_sources:
  min_score: 0.5  # Lower threshold for noisy social data
  fallback: skip

# CRITIC Verification
verification:
  max_iterations: 3
  confidence_minimum: 0.75
  fact_checking: enabled
  source_attribution: required
```

## Output Formats

### HTML Intelligence Report
- Executive summary with key findings
- Methodology and source attribution
- Interactive data visualizations
- Confidence scores and limitations
- Downloadable data appendix

### PowerPoint Briefing
- 10-slide executive briefing format
- Key insights with supporting data
- Visual charts and competitive positioning
- Action items and recommendations
- Source citations and methodology notes

### JSON Structured Data
- Machine-readable research results
- Standardized schema for downstream processing
- Confidence scores per data point
- Source provenance and timestamps
- API-friendly format for integration

## Security and Compliance

### API Key Management
```yaml
# Environment variables (never hardcode)
SERPER_API_KEY: ${SERPER_API_KEY}
FIRECRAWL_API_KEY: ${FIRECRAWL_API_KEY}
REDDIT_CLIENT_SECRET: ${REDDIT_CLIENT_SECRET}
OPENAI_API_KEY: ${OPENAI_API_KEY}
```

### Data Retention
- Source data: 30 days maximum
- Processed results: 1 year
- API logs: 90 days
- Personal data: immediate deletion after processing

### Rate Limiting and Fair Use
- Respect source API rate limits
- Implement exponential backoff
- Cache results to minimize redundant requests
- Monitor usage against budget caps

## Performance Characteristics

### Typical Execution Times
- Stage 1 (INTENT): 2-5 seconds
- Stage 2 (STORM): 10-30 seconds
- Stage 3 (RETRIEVE): 2-10 minutes (parallel)
- Stage 4 (RESOLVE): 30-60 seconds
- Stage 5 (SCORE): 1-3 minutes
- Stage 6 (SYNTHESIZE): 2-5 minutes
- Stage 7 (VERIFY): 1-3 minutes

**Total**: 7-22 minutes per research session

### Resource Requirements
- Memory: 2-4GB for large result sets
- Storage: 100MB-1GB per research session
- API Credits: $5-25 per comprehensive research
- Compute: 2-4 CPU cores recommended

## Integration Patterns

### With Other CEX Components
- **Knowledge Cards**: Research output feeds KC creation
- **Content Generation**: Intelligence informs content strategy
- **Commercial Analysis**: Competitive pricing feeds monetization
- **Brand Strategy**: Market research informs positioning

### Handoff Protocol
```markdown
## HANDOFF TO N02_MARKETING
Research Results: competitor_analysis_2026_04.json
Key Findings: 3 content gaps identified, pricing advantage confirmed
Next Action: Generate content brief targeting gap #1
Signal: research_complete
```

quality: 9.2