---
kind: config
id: bld_config_social_publisher
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints for social publisher
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Social Publisher"
version: "1.0.0"
author: n03_builder
tags: [social_publisher, builder, examples]
tldr: "Golden and anti-examples for social publisher construction, demonstrating ideal structure and common pitfalls."
domain: "social publisher construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: social_publisher Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Config file | `social_publisher_config_{empresa_slug}.yaml` | `social_publisher_config_{{BRAND_NAME}}.yaml` |
| Template | `tpl_social_publisher.md` | P04_tools/templates/ |
| Examples | `ex_social_publisher_{niche}.md` | `ex_social_publisher_pet_shop.md` |
| Compiled | `social_publisher_{slug}.yaml` | P04_tools/compiled/ |
| Instance | `social_publisher_config.md` | _instances/{company}/N02_marketing/ |
| Frontmatter id | `p04_cli_social_publisher_{slug}` | `p04_cli_social_publisher_{{BRAND_NAME}}` |

## Size Limits
| Artifact | Max Size | Rationale |
|----------|---------|-----------|
| Config YAML | 4096 bytes | Dense enough for 1 company, human-editable |
| Template | 4096 bytes | Builder ISO limit |
| Example | 4096 bytes | Builder ISO limit |
| KC | 4096 bytes | Standard KC size |

## Operational Constraints
| Rule | Value | Rationale |
|------|-------|-----------|
| Min cooldown_days | 1 | Prevents spam / audience fatigue |
| Max batch_size | 10 | API rate limit safety margin |
| Max hashtags IG | 30 (rec 5-10) | Instagram limit |
| Max hashtags TW | 3 | Twitter best forctice |
| Max caption IG | 2200 chars | Platform limit |
| Max caption TW | 280 chars | Platform limit |
| Retry max | 5 | Prevent infinite loop |
| Retry base_seconds | 10-300 | Reasonable backoff range |
| Content mix sum | exactly 100 | Mathematical constraint |

## File Placement Rules
| Artifact Type | Directory | Pillar |
|--------------|-----------|--------|
| Template | P04_tools/templates/ | P04 |
| Examples | P04_tools/examples/ | P04 |
| Compiled | P04_tools/compiled/ | P04 |
| Nucleus tool | N02_marketing/P04_tools/ | P04 |
| Nucleus KC | N02_marketing/P01_knowledge/ | P01 |
| Nucleus dispatch | N02_marketing/P12_orchestration/ | P12 |
| Company config | _instances/{co}/N02_marketing/ | instance |

## Security Rules
1. API keys: NEVER in plaintext → always ENV_VAR reference (SCREAMING_SNAKE_CASE)
2. Webhook URLs: NEVER in plaintext → always ENV_VAR reference
3. Database credentials: NEVER in config → always ENV_VAR reference
4. Config files: NEVER committed with real secrets → use `.env.example` pattern
