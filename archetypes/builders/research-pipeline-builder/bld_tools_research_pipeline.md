---
kind: tools
id: bld_tools_research_pipeline
pillar: P04
llm_function: CALL
purpose: Tools, APIs, and data sources available for research pipeline
---

# Tools: research-pipeline-builder

## Data Source Catalog (30+ sources)

### Inbound — Marketplace / Product Sources
| Source | API/Method | Auth | Cost | Data |
|--------|-----------|------|------|------|
| MercadoLivre | REST API v3 | APP_ID+SECRET | Free (rate limited) | title, price, sold_qty, seller, reviews |
| Shopee | Affiliate API + Firecrawl | API key | Firecrawl credits | title, price, shop_rating, flash_sale |
| Amazon BR | Keepa API + Firecrawl | KEEPA_KEY | €19/mo | title, price, BSR, reviews, price_history |
| Magalu | Firecrawl deep scrape | FIRECRAWL_KEY | credits | title, price, rating, seller |
| Americanas | Firecrawl deep scrape | FIRECRAWL_KEY | credits | title, price, rating |
| Casas Bahia | Firecrawl deep scrape | FIRECRAWL_KEY | credits | title, price, rating |
| Shein | Firecrawl deep scrape | FIRECRAWL_KEY | credits | title, price, reviews |
| Temu | Firecrawl deep scrape | FIRECRAWL_KEY | credits | title, price, sold_qty |

### Search — Web Search Engines
| Source | API | Auth | Cost | Specialty |
|--------|-----|------|------|-----------|
| Serper | `https://google.serper.dev/search` | SERPER_API_KEY | $0.30/1K | Google SERP |
| Exa | `https://api.exa.ai/search` | EXA_API_KEY | $0.10/query | Neural (papers, docs) |
| Gemini Search | Gemini API grounding | GOOGLE_API_KEY | included | Google grounding |
| OpenAI Search | Responses API web_search | OPENAI_API_KEY | per-token | GPT web search |
| Brave | `https://api.search.brave.com` | BRAVE_API_KEY | Free tier 2K/mo | Privacy-focused |
| Tavily | `https://api.tavily.com/search` | TAVILY_API_KEY | Free tier 1K/mo | Research-grade |

### Outbound — Social / Review / Community
| Source | API/Method | Auth | Data |
|--------|-----------|------|------|
| YouTube | Data API v3 + transcripts | YOUTUBE_API_KEY | videos, transcripts, comments |
| Reddit | OAuth REST API | REDDIT_CLIENT_ID | posts, comments, sentiment |
| ReclameAqui | Firecrawl scrape | FIRECRAWL_KEY | complaints, ratings, responses |
| Twitter/X | Firecrawl + Serper | varies | posts, engagement, sentiment |

### Trends — Price / Trend Tracking
| Source | API | Auth | Data |
|--------|-----|------|------|
| Google Trends | pytrends (unofficial) | none | search volume, related queries |
| Keepa | REST API | KEEPA_KEY | Amazon price history, BSR |

### RAG — Internal Knowledge
| Source | Method | Data |
|--------|--------|------|
| Local docs | Embedding + vector search | Company documents |
| Supabase | pgvector | Embedded knowledge base |

## MCP Tools (for N01 Claude CLI)
| MCP | Command | Purpose |
|-----|---------|---------|
| firecrawl | `npx -y firecrawl-mcp` | Deep scrape marketplaces |
| fetch | `uvx mcp-server-fetch` | URL → markdown |
| brave-search | `npx @anthropic/mcp-server-brave-search` | Web search |
| markitdown | `npx -y markitdown-mcp` | PDF/DOCX → markdown |

## Multi-Model Routing
| Task | Model | Why |
|------|-------|-----|
| Extraction | gemini-2.5-flash | Structured data, 40x cheaper |
| Reasoning | gpt-5-mini / claude-sonnet | Complex analysis |
| Social volume | gemini-2.5-flash | High volume, low cost |
| CRITIC verify | o4-mini | Thinking model catches errors |
