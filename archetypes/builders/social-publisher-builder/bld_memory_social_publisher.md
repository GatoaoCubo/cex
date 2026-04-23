---
id: p10_lr_social-publisher-builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
observation: "Social publisher systems fail when config is mixed with code. The original {{BRAND_NAME}} system had 9352 lines with hardcoded company data scattered across 9 Python files, making it impossible to reuse for another business without a full fork."
pattern: "Separate concerns into 3 layers: (1) config YAML with all company-specific data, (2) pipeline architecture describing the 10-step flow, (3) runtime code that reads config and executes pipeline. Layer 1 changes per company. Layers 2-3 are universal."
evidence: "{{BRAND_NAME}} system analysis: 47 hardcoded references to company name, 12 hardcoded API endpoints, 3 plaintext API keys. Refactoring to config-driven reduced company-specific code from 9352 lines to ~150 lines of YAML config + ~400 lines universal runtime."
confidence: 0.85
outcome: SUCCESS
domain: social_publisher
tags: [social-media, automation, config-driven, separation-of-concerns, reusability]
tldr: "Config-driven beats hardcoded. 9352 lines → 150 YAML + 400 universal Python. Every company fills 1 file."
impact_score: 9.0
decay_rate: 0.03
keywords: [social-publisher, config, reusability, pipeline, automation, anti-pattern]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Social Publisher"
density_score: 0.90
llm_function: INJECT
related:
  - p03_sp_social_publisher_builder
  - n02_tool_social_publisher
  - bld_architecture_social_publisher
  - bld_instruction_social_publisher
  - bld_knowledge_card_social_publisher
  - n02_kc_social_publishing
  - bld_collaboration_social_publisher
  - bld_config_social_publisher
  - social-publisher-builder
  - tpl_social_publisher
---
# Learning: social_publisher

## Key Insight
The single most impactful architectural decision for social publishers is **config extraction**. Every piece of company-specific data — name, platforms, schedule, API keys, hashtags, content mix — must live in ONE config file. The pipeline code should be 100% company-agnostic.

## Evidence from {{BRAND_NAME}}
| Metric | Before (hardcoded) | After (config-driven) |
|--------|-------------------|----------------------|
| Total lines | 9352 | 550 (150 config + 400 runtime) |
| Company-specific references | 47 scattered | 1 file (config.yaml) |
| Time to onboard new company | 2-3 days (fork + edit) | 15 min (fill config) |
| API key security | 3 plaintext in code | 0 (all ENV_VAR) |
| Platforms supported | IG + FB (hardcoded) | Any (config-selectable) |

## Lessons Learned
1. **Cooldown is essential** — Without product rotation, the same item posts 3x/week → unfollows
2. **Timezone matters** — Posts at 3am local time get 0 engagement regardless of content quality
3. **LLM fallback required** — Caption generation via LLM fails ~5% of the time; template fallback prevents missed posts
4. **Batch size caps** — Ayrshare rate-limits at 100/day; batch_size > 10 risks hitting limits mid-cycle
5. **Content mix prevents fatigue** — Pure product posts lose followers; 60% value content is the sweet spot

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_social_publisher_builder]] | upstream | 0.38 |
| [[n02_tool_social_publisher]] | upstream | 0.34 |
| [[bld_architecture_social_publisher]] | upstream | 0.29 |
| [[bld_instruction_social_publisher]] | upstream | 0.27 |
| [[bld_knowledge_card_social_publisher]] | upstream | 0.26 |
| [[n02_kc_social_publishing]] | upstream | 0.26 |
| [[bld_collaboration_social_publisher]] | downstream | 0.24 |
| [[bld_config_social_publisher]] | upstream | 0.23 |
| [[social-publisher-builder]] | upstream | 0.22 |
| [[tpl_social_publisher]] | upstream | 0.22 |
