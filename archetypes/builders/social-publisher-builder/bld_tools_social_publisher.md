---
kind: tools
id: bld_tools_social_publisher
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for social publisher production and runtime
quality: 9.0
title: "Tools Social Publisher"
version: "1.0.0"
author: n03_builder
tags: [social_publisher, builder, examples]
tldr: "Golden and anti-examples for social publisher construction, demonstrating ideal structure and common pitfalls."
domain: "social publisher construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_client
  - bld_architecture_social_publisher
  - bld_tools_model_provider
  - bld_knowledge_card_social_publisher
  - n06_api_access_pricing
  - bld_tools_batch_config
  - bld_instruction_social_publisher
  - bld_tools_cli_tool
  - bld_tools_content_monetization
  - p03_sp_social_publisher_builder
---

# Tools: social-publisher-builder

## Publisher APIs
| API | Endpoint | Auth | Rate Limit | Networks |
|-----|----------|------|-----------|----------|
| Ayrshare | `https://app.ayrshare.com/api/post` | Bearer token | 100 posts/day (pro) | IG,FB,TT,LI,TW,YT,Pinterest,Reddit |
| Postiz | `{self_hosted_url}/api/posts` | API key | unlimited (self-hosted) | IG,FB,TT,LI,TW,YT,Threads |
| Meta Graph | `https://graph.facebook.com/v19.0/{page_id}/photos` | OAuth token | 200 calls/hr per user | IG,FB only |

## Catalog Sources
| Source | Client | Auth | Usage |
|--------|--------|------|-------|
| Supabase | `supabase-py` | URL + anon key | `client.table('products').select('*')` |
| Shopify | REST Admin API | API key + secret | `GET /admin/api/2024-01/products.json` |
| Airtable | REST API | Bearer token | `GET /v0/{base_id}/{table}` |
| CSV | `csv` stdlib | none | Local file read |

## LLM for Caption Generation
| Provider | Model | Usage | Cost |
|----------|-------|-------|------|
| Anthropic | claude-sonnet-4-6 | Caption + hashtag generation | ~$0.003/caption |
| OpenAI | gpt-4o-mini | Caption generation (budget) | ~$0.001/caption |
| Ollama | llama3 | Local caption generation | Free |

## Notification Channels
| Channel | Integration | Format |
|---------|------------|--------|
| Discord | Webhook POST | Embed with image + caption preview |
| Slack | Webhook POST | Block kit with post link |
| Email | SMTP / SendGrid | HTML summary of published posts |

## Production Tools (CEX internal)
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile config .md → .yaml | After artifact creation |
| cex_hooks.py | Validate frontmatter | Pre-save |
| cex_doctor.py | Check builder health | Post-build audit |
| cex_score.py | Assign quality score | Peer review |

## Data Sources for Builder
| Source | Path | Data |
|--------|------|------|
| P04 schema | P04_tools/_schema.yaml | Field definitions for cli_tool |
| Social KC | P01_knowledge/library/kind/kc_cli_tool.md | cli_tool knowledge |
| Platform docs | External | API limits, formats, best forctices |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_client]] | sibling | 0.36 |
| [[bld_architecture_social_publisher]] | downstream | 0.34 |
| [[bld_tools_model_provider]] | sibling | 0.33 |
| [[bld_knowledge_card_social_publisher]] | upstream | 0.31 |
| [[n06_api_access_pricing]] | downstream | 0.31 |
| [[bld_tools_batch_config]] | sibling | 0.30 |
| [[bld_instruction_social_publisher]] | upstream | 0.29 |
| [[bld_tools_cli_tool]] | sibling | 0.28 |
| [[bld_tools_content_monetization]] | sibling | 0.28 |
| [[p03_sp_social_publisher_builder]] | upstream | 0.28 |
