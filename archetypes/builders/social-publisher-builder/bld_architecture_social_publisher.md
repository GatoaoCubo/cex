---
kind: architecture
id: bld_architecture_social_publisher
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of social publisher pipeline — inventory, dependencies, data flow
quality: 9.1
title: "Architecture Social Publisher"
version: "1.0.0"
author: n03_builder
tags: [social_publisher, builder, examples]
tldr: "Golden and anti-examples for social publisher construction, demonstrating ideal structure and common pitfalls."
domain: "social publisher construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_social_publisher_builder
  - n02_tool_social_publisher
  - bld_collaboration_social_publisher
  - bld_knowledge_card_social_publisher
  - bld_collaboration_runtime_rule
  - bld_tools_social_publisher
  - bld_architecture_kind
  - bld_architecture_research_pipeline
  - bld_instruction_social_publisher
  - bld_collaboration_client
---

# Architecture: social_publisher in the CEX

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| config.yaml | Company-specific publishing settings | user | required |
| catalog_fetcher | Reads product/content from source (Supabase, Shopify, API) | runtime | required |
| content_selector | Picks next item respecting rotation + cooldown | runtime | required |
| caption_generator | LLM call to produce caption from item + persona + tone | runtime | required |
| time_optimizer | Selects best posting time per platform + timezone | runtime | required |
| hashtag_engine | Generates brand + niche hashtags within platform limits | runtime | required |
| publisher_client | Sends post to API (Ayrshare/Postiz/Meta Graph) | runtime | required |
| structured_logger | Writes JSON logs for every publish attempt | runtime | required |
| notifier | Sends success/failure to Discord/Slack/email | runtime | optional |
| rotation_state | Tracks what was posted when, enforces cooldown | runtime | required |

## Data Flow
```
config.yaml ──────────────────────────────┐
                                          │
catalog_source ─► catalog_fetcher ─► content_list
                                          │
rotation_state ─► content_selector ◄──────┘
                          │
                    selected_item
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
  caption_generator  time_optimizer  hashtag_engine
         │                │                │
         └────────┬───────┘────────────────┘
                  ▼
           assembled_post
                  │
                  ▼
         publisher_client ──► Platform API
                  │
          ┌───────┼───────┐
          ▼       ▼       ▼
       logger  notifier  rotation_state (update)
```

## Dependency Map
| Component | Depends On | External |
|-----------|-----------|----------|
| catalog_fetcher | config.catalog | Supabase/Shopify/Airtable API |
| caption_generator | config.identity + selected_item | LLM API (Anthropic/OpenAI) |
| publisher_client | config.publisher | Ayrshare/Postiz/Meta Graph API |
| notifier | config.notifications | Discord/Slack webhook |
| time_optimizer | config.schedule | none (local computation) |
| rotation_state | local file or DB | none |

## Position in CEX
```
P04_tools/          ← template + examples live here
  templates/tpl_social_publisher.md
  examples/ex_social_publisher_*.md
  compiled/social_publisher_*.yaml

N02_marketing/      ← nucleus instance lives here
  tools/social_publisher_marketing.md
  knowledge/knowledge_card_social_publishing.md
  orchestration/dispatch_rule_social_publisher.md

_instances/codexa/N02_marketing/  ← company-specific config
  social_publisher_config.md
```

## Boundaries
| This builder handles | Other builder handles |
|---------------------|----------------------|
| Pipeline architecture | Python runtime code → cli-tool-builder |
| Config schema | Database schema → db-connector-builder |
| API integration pattern | API client implementation → api-client-builder |
| Content strategy | Caption prompt writing → prompt-template-builder |
| Scheduling pattern | Server deployment → spawn-config-builder |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_social_publisher_builder]] | upstream | 0.36 |
| [[n02_tool_social_publisher]] | upstream | 0.33 |
| [[bld_collaboration_social_publisher]] | downstream | 0.32 |
| [[bld_knowledge_card_social_publisher]] | upstream | 0.30 |
| [[bld_collaboration_runtime_rule]] | downstream | 0.27 |
| [[bld_tools_social_publisher]] | upstream | 0.25 |
| [[bld_architecture_kind]] | sibling | 0.25 |
| [[bld_architecture_research_pipeline]] | sibling | 0.25 |
| [[bld_instruction_social_publisher]] | upstream | 0.25 |
| [[bld_collaboration_client]] | downstream | 0.24 |
