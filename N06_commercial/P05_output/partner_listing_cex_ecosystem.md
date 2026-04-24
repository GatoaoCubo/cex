---
id: partner_listing_cex_ecosystem
kind: partner_listing
8f: F8_collaborate
pillar: P05
nucleus: N06
domain: commercial
title: "Partner Listing — CEX Ecosystem"
version: "1.0.0"
quality: 8.5
tags: [partners, ecosystem, integrations, commercial]
author: N06_contrib_stress_test
created: "2026-04-19"
last_reviewed: "2026-04-19"
related:
  - bld_instruction_partner_listing
  - p10_lr_partner_listing_builder
  - p05_qg_partner_listing
  - p03_sp_partner_listing_builder
  - n06_api_access_pricing
  - commercial_readiness_20260413
  - bld_schema_model_provider
  - bld_examples_model_provider
  - self_audit_n03_builder_20260408
  - n06_strategy_claude_native
density_score: 1.0
updated: "2026-04-22"
---

## Tier Structure

| Tier | Criteria | Benefits |
|------|----------|---------|
| Platinum | >$500K ARR referred, certified, co-sell | Co-marketing, dedicated SE, roadmap access |
| Gold | >$100K ARR referred, certified | Joint case studies, partner portal |
| Silver | Active integration, <$100K ARR | Directory listing, technical support |
| Technology | Native integration, no revenue share | Docs co-authoring, badge |

---

## Platinum Partners

### Anthropic
| Field | Value |
|-------|-------|
| Tier | Platinum |
| Region | Global |
| Domain | LLM provider — Claude models (Opus 4.7, Sonnet 4.6, Haiku 4.5) |
| Integration | claude CLI, Anthropic SDK, Claude Code API |
| Certifications | SOC2 Type II, ISO 27001 |
| Contact | partnerships@anthropic.com |
| Revenue model | Token-based API billing (pay-per-use) |
| CEX kinds served | All — primary inference engine for N01-N07 |
| Notes | Default model tier: Opus for N03/N07; Sonnet for N01-N06 |

---

## Gold Partners

### Supabase
| Field | Value |
|-------|-------|
| Tier | Gold |
| Region | Global (multi-region) |
| Domain | Open-source Postgres backend — auth, storage, realtime |
| Integration | `supabase_data_layer` kind, `db_connector` kind |
| Certifications | SOC2 Type II, GDPR |
| Contact | enterprise@supabase.com |
| Revenue model | Usage-based (compute + storage) |
| CEX kinds served | `db_connector`, `vector_store`, `session_backend` |
| Notes | Candidate for CEX knowledge graph persistence layer |

### GitHub
| Field | Value |
|-------|-------|
| Tier | Gold |
| Region | Global |
| Domain | Version control + CI/CD + issue tracking |
| Integration | MCP server (`mcp__github__*`), git hooks, PR review agents |
| Certifications | SOC2, ISO 27001, FedRAMP Moderate |
| Contact | enterprise@github.com |
| Revenue model | Seat-based (Teams/Enterprise) |
| CEX kinds served | `audit_log`, `deployment_manifest`, `changelog` |
| Notes | Primary source control for all CEX artifacts; Actions for CI gates |

### LangSmith (LangChain)
| Field | Value |
|-------|-------|
| Tier | Gold |
| Region | Global (US/EU) |
| Domain | LLM observability, tracing, evaluation |
| Integration | `trace_config` kind, `eval_framework` kind |
| Certifications | SOC2 Type II |
| Contact | sales@langchain.com |
| Revenue model | Usage-based (traces/month) |
| CEX kinds served | `trace_config`, `eval_dataset`, `llm_judge` |
| Notes | Candidate for CEX pipeline observability layer |

---

## Silver Partners

### Ollama
| Field | Value |
|-------|-------|
| Tier | Silver |
| Region | Self-hosted (local) |
| Domain | Local LLM inference — qwen3, llama3.1, gemma2 |
| Integration | `model_provider` kind, cex_router fallback chain |
| Certifications | Open source (MIT) |
| Contact | github.com/ollama/ollama |
| Revenue model | Free (open source) |
| CEX kinds served | All — fallback inference for air-gapped / cost-sensitive deployments |
| Notes | Used in CEX preflight (qwen3:14b context pre-compilation); local model bench winner |

### Firecrawl
| Field | Value |
|-------|-------|
| Tier | Silver |
| Region | Global |
| Domain | Web crawling + scraping as a service |
| Integration | MCP server (`mcp__firecrawl__*`), `browser_tool` kind |
| Certifications | SOC2 (in progress) |
| Contact | firecrawl.dev/enterprise |
| Revenue model | Usage-based (credits/month) |
| CEX kinds served | `browser_tool`, `research_pipeline`, `knowledge_card` (web-sourced) |
| Notes | Primary web research tool for N01 intelligence nucleus |

### Canva
| Field | Value |
|-------|-------|
| Tier | Silver |
| Region | Global |
| Domain | Visual design + brand asset generation |
| Integration | MCP server (`mcp__canva__*`), `visual_workflow` kind |
| Certifications | ISO 27001, SOC2 |
| Contact | canva.com/enterprise |
| Revenue model | Seat-based (Canva for Teams) |
| CEX kinds served | `visual_workflow`, `landing_page` (design assets), `pitch_deck` |
| Notes | N02 marketing nucleus visual output layer |

---

## Technology Partners

### Brave Search
| Field | Value |
|-------|-------|
| Tier | Technology |
| Region | Global |
| Domain | Privacy-first web search API |
| Integration | MCP server (`mcp__brave-search__*`), `search_tool` kind |
| CEX kinds served | `search_tool`, `research_pipeline` |
| Notes | Default web search for N01 research tasks; no tracking |

### Playwright (Microsoft)
| Field | Value |
|-------|-------|
| Tier | Technology |
| Domain | Browser automation + testing |
| Integration | MCP server (`mcp__playwright__*`), `browser_tool` kind |
| CEX kinds served | `browser_tool`, `e2e_eval` |
| Notes | UI testing + web scraping for N05 operations nucleus |

---

## Partner Gap Analysis

| Domain | Current Coverage | Priority | Notes |
|--------|-----------------|----------|-------|
| Vector database | Weak (no Pinecone/Weaviate integration) | HIGH | Critical for RAG kind |
| Payments | None | HIGH | Stripe/Paddle for CEX billing |
| Observability | LangSmith only | MEDIUM | Need Datadog or Grafana |
| Communication | None | MEDIUM | Slack/Teams for nucleus alerts |
| Healthcare data | None | HIGH | Veeva/HL7 FHIR server |
| Legal CLM | None | MEDIUM | Ironclad/Docusign integration |

## Partner Application Process

1. Submit via GitHub Issue (label: `partner-request`)
2. N06 reviews: technical integration feasibility, revenue model, compliance
3. N05 builds: integration artifact + smoke test
4. N04 documents: partner KC + API reference
5. Listed in this file after first successful integration commit

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_partner_listing]] | upstream | 0.28 |
| [[p10_lr_partner_listing_builder]] | downstream | 0.22 |
| [[p05_qg_partner_listing]] | downstream | 0.22 |
| [[p03_sp_partner_listing_builder]] | upstream | 0.20 |
| [[n06_api_access_pricing]] | downstream | 0.20 |
| [[commercial_readiness_20260413]] | downstream | 0.20 |
| [[bld_schema_model_provider]] | downstream | 0.20 |
| [[bld_examples_model_provider]] | downstream | 0.20 |
| [[self_audit_n03_builder_20260408]] | upstream | 0.19 |
| [[n06_strategy_claude_native]] | upstream | 0.19 |
