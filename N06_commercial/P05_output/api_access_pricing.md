---
id: n06_api_access_pricing
kind: content_monetization
pillar: P11
title: "API Access Pricing -- CEX SDK Programmatic Access Tiers"
version: 1.0.0
created: 2026-04-08
author: n06_commercial
nucleus: N06
domain: api-monetization
quality: 8.9
tags: [api, pricing, sdk, programmatic-access, tiers, monetization, developer, integration]
tldr: "Pricing model for CEX SDK API access. 4 tiers (Dev/Startup/Business/Enterprise), usage-based billing, rate limits, SLA levels. Addresses Gap #1 from monetization audit: cex_sdk/ has 78 files but zero commercial layer."
density_score: 0.95
depends_on:
  - n06_monetization_audit_2026_04_08
  - n06_content_factory_pricing
  - n06_strategy_claude_native
linked_artifacts:
  primary: n06_monetization_audit_2026_04_08
  related:
    - n06_content_factory_pricing
    - n06_kc_content_monetization
    - p08_pat_pricing_framework
---

# API Access Pricing -- CEX SDK Programmatic Access Tiers

> cex_sdk/ has 78 Python files and 4,504 lines of code. The product is built.
> This artifact adds the commercial layer: who pays what for what access.
> Gap #1 from the monetization audit. Highest priority. Most scalable.

---

## 1. What the API Provides

### 1.1 CEX SDK Capabilities (already built)

Source: `cex_sdk/` directory scan

| Module | Functions | What It Does |
|--------|----------|-------------|
| `cex_8f_motor.py` | Intent parse, classify, fan-out | Decomposes user intent into CEX pipeline |
| `cex_8f_runner.py` | Full 8F execution | Runs complete build pipeline programmatically |
| `cex_crew_runner.py` | Prompt composition | ISOs + memory + context assembled into LLM prompt |
| `cex_query.py` | TF-IDF discovery | Find relevant builders for any intent |
| `cex_mission.py` | Goal decomposition | Break goal into artifact specs |
| `cex_retriever.py` | Artifact similarity | TF-IDF over 2,184 docs, 12K vocab |
| `cex_compile.py` | Artifact compilation | .md to .yaml compilation |
| `cex_score.py` | Quality scoring | 3-layer hybrid scoring |
| `cex_evolve.py` | Auto-improvement | Autonomous artifact evolution loop |
| `cex_memory_select.py` | Context injection | Keyword + LLM memory selection |
| `signal_writer.py` | Inter-process signals | Nucleus coordination |

### 1.2 API Use Cases

| Use Case | Who | Value | API Endpoint |
|----------|-----|-------|-------------|
| **Content automation** | Agencies | Generate content at scale via API instead of CLI | `/api/v1/orders` |
| **Knowledge ingestion** | SaaS companies | Feed domain docs, get typed KCs back | `/api/v1/ingest` |
| **Quality scoring** | QA teams | Score any artifact against CEX quality gates | `/api/v1/score` |
| **Builder discovery** | Developers | Find the right builder for any intent | `/api/v1/query` |
| **Pipeline execution** | Automation platforms | Run 8F pipeline from n8n/Zapier/custom code | `/api/v1/pipeline` |
| **Memory/context** | Custom agents | Inject CEX knowledge into any LLM agent | `/api/v1/memory` |
| **Artifact retrieval** | Search/RAG | TF-IDF similarity over 2,184+ artifacts | `/api/v1/retrieve` |

---

## 2. Pricing Tiers

### 2.1 Tier Comparison

| Feature | Dev (Free) | Startup | Business | Enterprise |
|---------|-----------|---------|----------|-----------|
| **Price (BRL)** | R$0 | R$297/month | R$997/month | Custom (R$3K+) |
| **Price (USD)** | $0 | $59/month | $199/month | Custom ($600+) |
| **API calls/month** | 100 | 2,000 | 10,000 | Unlimited |
| **Rate limit** | 5/min | 30/min | 120/min | 500/min |
| **8F pipeline calls** | 10/month | 200/month | 1,000/month | Unlimited |
| **Score calls** | 50/month | 1,000/month | 5,000/month | Unlimited |
| **Retrieve calls** | 50/month | 1,000/month | 5,000/month | Unlimited |
| **Brand configs** | 1 | 3 | 10 | Unlimited |
| **Webhook events** | -- | 100/day | 1,000/day | Unlimited |
| **SLA** | Best effort | 99.5% uptime | 99.9% uptime | 99.95% + dedicated |
| **Support** | Community | Email (48h) | Email (24h) + Slack | Dedicated Slack + call |
| **SDK access** | Read-only | Full | Full + custom builders | Full + white-label |
| **Data retention** | 7 days | 30 days | 90 days | Custom |
| **Auth** | API key | API key + OAuth2 | API key + OAuth2 + SSO | Custom |
| **Annual discount** | -- | 20% (R$237/mo) | 20% (R$797/mo) | Negotiated |

### 2.2 Overage Pricing

| Call Type | Dev | Startup | Business | Enterprise |
|-----------|-----|---------|----------|-----------|
| API call (beyond quota) | Blocked | R$0.20/call | R$0.15/call | R$0.10/call |
| 8F pipeline execution | Blocked | R$2.00/call | R$1.50/call | R$1.00/call |
| Score evaluation | Blocked | R$0.10/call | R$0.08/call | R$0.05/call |
| Retrieve query | Blocked | R$0.05/call | R$0.03/call | R$0.02/call |

### 2.3 Pricing Rationale

| Decision | Reasoning |
|----------|-----------|
| Dev tier is free | Reduces friction for evaluation. 100 calls is enough to test but not enough to build a product. |
| Startup at R$297/mo | Below R$300 psychological threshold. Affordable for solo devs monetizing with CEX. |
| Business at R$997/mo | Matches Content Factory Studio tier. Agencies already paying this for content can add API. |
| Enterprise is custom | Named pricing prevents undervaluing. R$3K/mo floor protects margins. |
| 8F calls are premium | Pipeline execution costs more (LLM tokens). 10x price vs simple API call. |
| Annual discount at 20% | Industry standard. Creates commitment, reduces churn. |

---

## 3. Cost Basis & Margin Analysis

### 3.1 Cost per API Call Type

| Call Type | Infrastructure Cost | LLM Token Cost | Total Cost | Startup Price | Margin |
|-----------|-------------------|---------------|-----------|--------------|--------|
| Simple API (query, retrieve) | R$0.001 | R$0.00 | R$0.001 | R$0.05-0.20 | 98%+ |
| Score evaluation | R$0.001 | R$0.02 (1K tokens) | R$0.021 | R$0.08-0.10 | 74-79% |
| 8F pipeline execution | R$0.01 | R$0.50 (15K tokens) | R$0.51 | R$1.50-2.00 | 66-74% |
| Memory/context injection | R$0.001 | R$0.05 (2K tokens) | R$0.051 | R$0.10-0.20 | 49-74% |

### 3.2 Tier Margin (Expected Usage)

| Tier | Revenue | Expected Usage | Est. Cost | Margin | Gross Profit |
|------|---------|---------------|-----------|--------|-------------|
| Dev (Free) | R$0 | 50 calls + 5 pipelines | R$2.58 | N/A (loss leader) | -R$2.58 |
| Startup (R$297) | R$297 | 1,200 calls + 100 pipelines | R$52.20 | **82%** | R$244.80 |
| Business (R$997) | R$997 | 6,000 calls + 500 pipelines | R$261.00 | **74%** | R$736.00 |
| Enterprise (R$3K+) | R$3,000+ | Variable | Variable | **70%+** | R$2,100+ |

### 3.3 Break-Even

| Metric | Value |
|--------|-------|
| Fixed cost (API gateway, monitoring) | ~R$500/month |
| Break-even customers | 2 Startup + 1 Business = R$1,591 (covers fixed + margins) |
| Target customers (Year 1, Month 12) | 30 Startup + 10 Business + 2 Enterprise |

---

## 4. API Architecture (High-Level)

### 4.1 Authentication

```
Client → API Key (header: X-CEX-API-Key) → Rate limiter → Handler → CEX SDK → Response
                                              |
                                              v
                                     Quota check (Redis/Supabase)
                                              |
                                     [ALLOW]    [BLOCK: 429]
```

### 4.2 Endpoint Map

```yaml
endpoints:
  # Discovery & Query
  GET  /api/v1/kinds                    # List all 123 kinds
  GET  /api/v1/kinds/{kind}             # Kind metadata
  POST /api/v1/query                    # TF-IDF builder discovery
  POST /api/v1/retrieve                 # Artifact similarity search
  
  # Pipeline Execution
  POST /api/v1/pipeline/run             # Full 8F execution
  GET  /api/v1/pipeline/{run_id}        # Pipeline status
  GET  /api/v1/pipeline/{run_id}/output # Pipeline output
  
  # Quality & Scoring
  POST /api/v1/score                    # Score an artifact
  POST /api/v1/validate                 # Validate artifact schema
  
  # Content Factory (via API)
  POST /api/v1/orders                   # Create content order
  GET  /api/v1/orders/{id}              # Order status
  GET  /api/v1/orders/{id}/outputs      # Download outputs
  
  # Memory & Context
  POST /api/v1/memory/select            # Get relevant memories for context
  POST /api/v1/memory/update            # Update memory entries
  
  # Brand
  GET  /api/v1/brand                    # Current brand config
  PUT  /api/v1/brand                    # Update brand config (Business+)
  
  # Account
  GET  /api/v1/usage                    # Current period usage
  GET  /api/v1/usage/history            # Historical usage
```

### 4.3 Response Format

```json
{
  "success": true,
  "data": { },
  "meta": {
    "request_id": "req_abc123",
    "credits_used": 1,
    "credits_remaining": 1999,
    "rate_limit": {
      "limit": 30,
      "remaining": 29,
      "reset_at": "2026-04-08T10:01:00Z"
    }
  }
}
```

---

## 5. Revenue Projections

### 5.1 Assumptions

| Variable | Value | Source |
|----------|-------|--------|
| Month 1 API customers | 5 Dev + 3 Startup + 1 Business | Conservative (existing CF users) |
| Monthly growth | 20% | API products grow faster than UI products |
| Conversion Dev->Startup | 15% after 30 days | Standard API funnel |
| Overage as % of base revenue | 15% | Industry average |
| Churn | 4% monthly | Lower than SaaS (integration stickiness) |

### 5.2 Monthly Revenue Projection

| Month | Dev (free) | Startup (R$297) | Business (R$997) | Enterprise (R$3K) | Overage | MRR |
|-------|-----------|-----------------|-----------------|-------------------|---------|-----|
| M01 | 5 | 3 x R$297 | 1 x R$997 | 0 | R$267 | **R$2,152** |
| M03 | 12 | 8 x R$297 | 3 x R$997 | 0 | R$800 | **R$6,167** |
| M06 | 25 | 18 x R$297 | 7 x R$997 | 1 x R$3,000 | R$2,100 | **R$17,425** |
| M09 | 40 | 30 x R$297 | 12 x R$997 | 2 x R$3,000 | R$4,200 | **R$31,074** |
| M12 | 60 | 48 x R$297 | 20 x R$997 | 4 x R$3,000 | R$7,500 | **R$53,696** |

**Year 1 total API revenue**: ~R$300,000 (cumulative)

### 5.3 API Revenue as % of Total CEX Revenue

| Source | Year 1 Revenue | % of Total |
|--------|---------------|-----------|
| Courses | R$180K-440K | 35-45% |
| Content Factory SaaS | R$150K-480K | 30-40% |
| **API Access** | **R$200K-300K** | **20-25%** |
| Consulting/Enterprise | R$50K-200K | 10-15% |
| Template packs + Community | R$40K-100K | 5-10% |

---

## 6. Competitive API Pricing Benchmarks

| Provider | Free | Starter | Pro | Notes |
|----------|------|---------|-----|-------|
| OpenAI API | Pay-per-token | Pay-per-token | -- | No free tier, pure usage |
| Anthropic API | $5 free credit | Pay-per-token | -- | Developer-friendly |
| LangChain Cloud | Free tier | $39/mo | $399/mo | Tracing + hosted |
| CrewAI Enterprise | -- | -- | Custom | No public API pricing |
| Jasper API | -- | $49/mo | Custom | Content generation only |
| **CEX API** | **Free (100 calls)** | **R$297/mo** | **R$997/mo** | **Full pipeline access** |

**Positioning**: CEX API is not just content generation -- it's a complete knowledge engineering pipeline. LangChain gives you plumbing. CEX gives you architecture.

---

## 7. Go-to-Market for API

### 7.1 Launch Sequence

| Phase | Timeline | Action | Goal |
|-------|----------|--------|------|
| Alpha | Month 1 | API keys for existing CF Studio/Factory customers | Validate endpoints, gather feedback |
| Beta | Month 2 | Public waitlist, 50 Dev tier signups | Test rate limiting, documentation |
| GA | Month 3 | Public launch, all tiers available | Revenue generation |
| Scale | Month 6+ | SDK packages (Python, Node.js, Go) | Developer adoption |

### 7.2 Developer Experience

| Asset | Owner | Status |
|-------|-------|--------|
| API documentation (OpenAPI spec) | N05 | Planned |
| Python SDK package (pip install cex-sdk) | N05 | Planned |
| Node.js SDK package | N05 | Future |
| Quickstart guide (3 min to first API call) | N04 | Planned |
| Postman collection | N05 | Planned |
| API status page | N05 | Planned |
| Developer portal (docs + dashboard + keys) | N03 | Planned |

### 7.3 Conversion Funnel (API-Specific)

```
GitHub README mentions API → Developer portal → Create account → Dev tier (free)
    → Hit 100 call limit → Upgrade to Startup (R$297)
        → Need multiple brands → Upgrade to Business (R$997)
            → Need SLA + custom → Enterprise (R$3K+)
```

---

## 8. Implementation Requirements

| # | Task | Owner | Effort | Dependency |
|---|------|-------|--------|-----------|
| 1 | API gateway (rate limiting, auth, logging) | N05 | High | Supabase |
| 2 | Wrap cex_sdk/ functions as REST endpoints | N05 | Medium | API gateway |
| 3 | Usage tracking + quota enforcement | N05 | Medium | Redis/Supabase |
| 4 | Stripe products for 4 API tiers | N06 | Low | Stripe MCP |
| 5 | API key management (create, rotate, revoke) | N05 | Medium | Auth system |
| 6 | Developer portal UI | N03 | High | API gateway |
| 7 | OpenAPI spec + auto-generated docs | N05 | Medium | Endpoints |
| 8 | Python SDK package (pip installable) | N05 | Medium | Endpoints stable |
| 9 | Overage billing automation | N05 | Medium | Stripe webhooks |
| 10 | API status page + monitoring | N05 | Low | Infrastructure |

**Total estimated effort**: 4-6 weeks for Alpha, 8-10 weeks for GA.

---

*Generated by N06 Commercial Nucleus -- API Access Pricing*
*78 files of SDK already built. This artifact adds the commercial layer.*
*Every endpoint has a price. Every call has a margin. Every tier has an upgrade path.*

## Boundary

Pipeline completo de monetizacao de conteudo: billing, credits, checkout, courses, ads, emails. NAO eh pricing_strategy (estrategia apenas) nem payment_integration (provider apenas).


## 8F Pipeline Function

Primary function: **PRODUCE**
