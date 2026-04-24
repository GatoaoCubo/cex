---
id: n02_tool_social_publisher
kind: cli_tool
8f: F5_call
pillar: P04
title: "Social Publisher — N02 Marketing Automation Tool"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: social-publisher-builder
domain: social_publisher
nucleus: N02
quality: 9.1
tags: [cli-tool, social-publisher, N02, marketing, automation, social-media]
tldr: "Config-driven social media auto-posting tool for N02 Marketing. 10-step pipeline: catalog → caption → publish → log. Any company fills 1 YAML config."
density_score: 0.90
related:
  - p03_sp_social_publisher_builder
  - bld_knowledge_card_social_publisher
  - bld_architecture_social_publisher
  - bld_collaboration_social_publisher
  - n02_dr_social_publisher
  - bld_instruction_social_publisher
  - social-publisher-builder
  - tpl_social_publisher
  - p10_lr_social-publisher-builder
  - p01_kc_social_publisher
---

# Social Publisher — Marketing Tool

## Purpose
Automated social media publishing for any business served by N02 Marketing. Reads a company-specific YAML config and executes a 10-step pipeline: fetch products/content, generate captions via LLM, optimize posting time, publish to social platforms, log results, and rotate content to prevent repetition.

## Pipeline
```
CONFIG ─► FETCH catalog ─► SELECT (rotation-aware)
              │
              ▼
         GENERATE caption (LLM)
              │
      ┌───────┼───────┐
      ▼       ▼       ▼
  OPTIMIZE  HASHTAGS  FORMAT
   time      tags     post
      │       │       │
      └───────┼───────┘
              ▼
          PUBLISH (API)
              │
      ┌───────┼───────┐
      ▼       ▼       ▼
    LOG    NOTIFY   ROTATE
```

## Usage
```bash
# Run for specific company config
python social_publisher.py --config _instances/codexa/N02_marketing/social_publisher_config.yaml

# Dry run (generate captions, don't publish)
python social_publisher.py --config config.yaml --dry-run

# Single platform
python social_publisher.py --config config.yaml --platform instagram

# Force specific content type
python social_publisher.py --config config.yaml --type product
```

## Supported Platforms
| Platform | API Options | Caption Limit | Hashtag Rec |
|----------|------------|--------------|-------------|
| Instagram | Ayrshare, Meta Graph | 2200 chars | 5-10 |
| Facebook | Ayrshare, Meta Graph | 63206 chars | 3-5 |
| TikTok | Ayrshare, Postiz | 2200 chars | 5-8 |
| LinkedIn | Ayrshare, Postiz | 3000 chars | 3-5 |
| Twitter/X | Ayrshare, Postiz | 280 chars | 2-3 |

## Config Reference
Company-specific config lives in `_instances/{company}/N02_marketing/social_publisher_config.yaml`. See `P04_tools/templates/tpl_social_publisher.md` for full schema.

Required sections: `identity`, `platforms`, `schedule`, `content_mix`, `catalog`, `publisher`, `hashtags`.

## Quality Gates
- Config completeness: all 7 required sections ✓
- Zero plaintext secrets: all API keys via ENV_VAR ✓
- Content mix sums to 100 ✓
- Timezone is valid IANA ✓
- Retry policy defined ✓
- Cooldown >= 1 day ✓

## Nucleus Integration
| Direction | Target | Data |
|-----------|--------|------|
| N02 → N01 | Intelligence | Audience analysis for time optimization |
| N02 → N03 | Engineering | Python runtime implementation |
| N02 → N05 | Operations | Cron deployment + monitoring |
| N02 → N06 | Commercial | Product catalog sync |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_social_publisher_builder]] | upstream | 0.48 |
| [[bld_knowledge_card_social_publisher]] | upstream | 0.46 |
| [[bld_architecture_social_publisher]] | downstream | 0.42 |
| [[bld_collaboration_social_publisher]] | downstream | 0.39 |
| [[n02_dr_social_publisher]] | downstream | 0.39 |
| [[bld_instruction_social_publisher]] | upstream | 0.38 |
| [[social-publisher-builder]] | related | 0.37 |
| [[tpl_social_publisher]] | sibling | 0.35 |
| [[p10_lr_social-publisher-builder]] | downstream | 0.34 |
| [[p01_kc_social_publisher]] | related | 0.33 |
