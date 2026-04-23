---
kind: config
id: bld_config_research_pipeline
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: high
max_turns: 25
disallowed_tools: [Write, Edit]
fork_context: fork
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Research Pipeline"
version: "1.0.0"
author: n03_builder
tags: [research_pipeline, builder, examples]
tldr: "Golden and anti-examples for research pipeline construction, demonstrating ideal structure and common pitfalls."
domain: "research pipeline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_social_publisher
  - n01_kc_source_catalog
  - bld_config_content_monetization
  - n01_tool_research_pipeline
  - tpl_research_pipeline
  - bld_config_kind
  - bld_tools_research_pipeline
  - bld_config_search_tool
  - bld_config_retriever_config
  - bld_architecture_research_pipeline
---
# Config: research_pipeline Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Config file | `research_pipeline_config_{empresa}.yaml` | `research_pipeline_config_codexa.yaml` |
| Template | `tpl_research_pipeline.md` | P04_tools/templates/ |
| Examples | `ex_research_pipeline_{niche}.md` | `ex_research_pipeline_ecommerce_br.md` |
| Instance | `research_pipeline_config.md` | _instances/{co}/N01_intelligence/ |
| Frontmatter id | `p04_cli_research_pipeline_{slug}` | `p04_cli_research_pipeline_codexa` |

## Size Limits
| Artifact | Max Size | Rationale |
|----------|---------|-----------|
| Config YAML | 4096 bytes | Dense config, human-editable |
| Template | 4096 bytes | Builder ISO limit |
| Example | 4096 bytes | Builder ISO limit |
| KC | 4096 bytes | Standard KC size |

## Source Categories (reference)
| Category | Description | Common Sources |
|----------|------------|----------------|
| inbound | Product/listing data from marketplaces | mercadolivre, shopee, amazon, magalu, g2, capterra |
| outbound | Social intelligence, reviews, community | youtube, reddit, reclameaqui, hackernews, twitter |
| search | Web search engines | serper, exa, gemini_search, openai_search, brave, tavily |
| trends | Price tracking, trend analysis | pytrends, keepa, semrush |
| rag | Internal knowledge base | local_docs, supabase_embeddings, confluence |

## API Cost Reference
| Source | Cost | Rate Limit | Auth |
|--------|------|-----------|------|
| Serper | $0.30/1K queries | 100/min | SERPER_API_KEY |
| Firecrawl | $19/mo (3K credits) | 10/min | FIRECRAWL_API_KEY |
| Exa | $0.10/query | 60/min | EXA_API_KEY |
| YouTube | Free (10K/day) | 10K/day | YOUTUBE_API_KEY |
| Keepa | €19/mo (5K tokens) | 5/min | KEEPA_API_KEY |
| pytrends | Free | 1/3s (unofficial) | none |
| Reddit | Free (OAuth) | 60/min | REDDIT_CLIENT_ID |

## File Placement Rules
| Artifact Type | Directory | Pillar |
|--------------|-----------|--------|
| Template | P04_tools/templates/ | P04 |
| Examples | P04_tools/examples/ | P04 |
| Compiled | P04_tools/compiled/ | P04 |
| Nucleus tool | N01_intelligence/P04_tools/ | P04 |
| Nucleus KCs | N01_intelligence/P01_knowledge/ | P01 |
| Dispatch rule | N01_intelligence/P12_orchestration/ | P12 |
| Company config | _instances/{co}/N01_intelligence/ | instance |

## Security Rules
1. API keys: NEVER in plaintext → always ENV_VAR (SCREAMING_SNAKE_CASE)
2. Source URLs: parameterize base URLs when possible
3. Config files: NEVER commit with real secrets → `.env.example` pattern
4. Marketplace schemas: safe to commit (extraction field names, not auth)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_social_publisher]] | sibling | 0.47 |
| [[n01_kc_source_catalog]] | upstream | 0.33 |
| [[bld_config_content_monetization]] | sibling | 0.29 |
| [[n01_tool_research_pipeline]] | upstream | 0.27 |
| [[tpl_research_pipeline]] | upstream | 0.25 |
| [[bld_config_kind]] | sibling | 0.24 |
| [[bld_tools_research_pipeline]] | upstream | 0.23 |
| [[bld_config_search_tool]] | sibling | 0.23 |
| [[bld_config_retriever_config]] | sibling | 0.22 |
| [[bld_architecture_research_pipeline]] | upstream | 0.21 |
