---
id: n02_dr_social_publisher
kind: dispatch_rule
8f: F8_collaborate
pillar: P12
title: "Dispatch Rule — Social Publisher"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: social-publisher-builder
domain: social_publisher
nucleus: N02
quality: 9.1
tags: [dispatch-rule, social-publisher, N02, routing, orchestration]
tldr: "Routes social publishing tasks to N02 Marketing. Triggers on posting/publishing/social media keywords."
density_score: 0.88
related:
  - bld_collaboration_social_publisher
  - n02_tool_social_publisher
  - social-publisher-builder
  - p03_sp_social_publisher_builder
  - bld_instruction_social_publisher
  - bld_knowledge_card_social_publisher
  - bld_sp_collaboration_software_project
  - bld_architecture_social_publisher
  - bld_output_template_social_publisher
  - bld_collaboration_research_pipeline
---

# Dispatch Rule — Social Publisher

## Routing
| Field | Value |
|-------|-------|
| Target Nucleus | N02_marketing |
| Target Tool | N02_marketing/P04_tools/social_publisher_marketing.md |
| Builder | archetypes/builders/social-publisher-builder/ |
| Priority | standard |

## Trigger Keywords
```yaml
primary:
  - social publisher
  - auto-posting
  - publicar redes sociais
  - postar instagram
  - postar facebook
  - social media automation
  - content calendar
  - agendamento de posts
  - ayrshare
  - postiz

secondary:
  - hashtags
  - caption generation
  - posting schedule
  - content mix
  - product rotation
```

## Routing Rules
| Intent Pattern | Route To | Confidence |
|---------------|----------|-----------|
| "criar/build social publisher" | N03 (build) → N02 (instance) | 0.95 |
| "configurar auto-posting para {empresa}" | N02 (fill config) | 0.90 |
| "publicar/postar no instagram/facebook" | N02 (execute pipeline) | 0.90 |
| "melhorar engagement/horarios" | N01 (analyze) → N02 (update) | 0.85 |
| "deploy cron de publicacao" | N02 (config) → N05 (deploy) | 0.85 |
| "implementar publisher em Python" | N03 (code) | 0.80 |

## Cross-Nucleus Handoffs
| From | To | Trigger | Payload |
|------|-----|---------|---------|
| N07 | N02 | "new company social publisher" | Company requirements |
| N02 | N03 | "implement runtime" | Pipeline spec + config schema |
| N02 | N05 | "deploy scheduling" | Cron config + monitoring rules |
| N02 | N01 | "analyze audience" | Platform + niche + current metrics |
| N02 | N06 | "sync catalog" | Catalog source config |

## Validation
Before dispatching, verify:
1. Company config exists or will be created
2. At least 1 platform is specified
3. Publisher API type is supported (ayrshare/postiz/meta_graph)
4. No plaintext secrets in the request

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_social_publisher]] | related | 0.60 |
| [[n02_tool_social_publisher]] | upstream | 0.55 |
| [[social-publisher-builder]] | upstream | 0.47 |
| [[p03_sp_social_publisher_builder]] | upstream | 0.43 |
| [[bld_instruction_social_publisher]] | upstream | 0.38 |
| [[bld_knowledge_card_social_publisher]] | upstream | 0.36 |
| [[bld_sp_collaboration_software_project]] | upstream | 0.35 |
| [[bld_architecture_social_publisher]] | upstream | 0.33 |
| [[bld_output_template_social_publisher]] | upstream | 0.33 |
| [[bld_collaboration_research_pipeline]] | related | 0.31 |
