---
kind: config
id: bld_config_content_monetization
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: high
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.2
title: "Config Content Monetization"
version: "1.0.0"
author: n03_builder
tags: [content_monetization, builder, examples]
tldr: "Golden and anti-examples for content monetization construction, demonstrating ideal structure and common pitfalls."
domain: "content monetization construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_content_monetization
  - bld_config_social_publisher
  - bld_instruction_content_monetization
  - bld_config_research_pipeline
  - bld_knowledge_card_content_monetization
  - n06_kc_content_monetization
  - bld_collaboration_content_monetization
  - p03_sp_content_monetization_builder
  - p11_qg_content_monetization
  - bld_tools_content_monetization
---
# Config: content_monetization Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Config file | `content_monetization_config_{empresa}.yaml` | `content_monetization_config_codexa.yaml` |
| Template | `tpl_content_monetization.md` | P11_feedback/templates/ |
| Examples | `ex_content_monetization_{model}.md` | `ex_content_monetization_saas.md` |
| Instance | `content_monetization_config.md` | _instances/{co}/N06_commercial/ |
| Frontmatter id | `p04_cli_content_monetization_{slug}` | `p04_cli_content_monetization_codexa` |

## Size Limits
| Artifact | Max Size | Rationale |
|----------|---------|-----------|
| Config YAML | 4096 bytes | Dense config, human-editable |
| Template | 4096 bytes | Builder spec limit |
| Example | 4096 bytes | Builder spec limit |
| Instruction | 6144 bytes | Extended for 9-step pipeline |

## Pricing Constraints
| Rule | Value | Rationale |
|------|-------|-----------|
| Min floor margin | 30% | Below this, LLM pipeline costs eat profit |
| Min tier count | 1 | At least free or paid tier required |
| Max tier count | 5 | More tiers = decision paralysis |
| Price format | centavos/cents (integer) | Avoid float rounding (R$49.90 = 4990) |
| Trial max | 30 days | Longer trials reduce conversion |
| Credit pack min | 100 credits | Smaller packs have high transaction overhead |

## Credit System Constraints
| Rule | Value | Rationale |
|------|-------|-----------|
| Min pipeline cost | 1 credit | Zero-cost operations defeat credit purpose |
| Max pipeline cost | 1000 credits | Single operation cannot drain account |
| Overdraft default | block | Negative balances create billing disputes |
| Rollover default | false | Rollover complicates revenue recognition |

## Checkout Constraints
| Rule | Hotmart (BR) | Digistore24 (INT) |
|------|-------------|-------------------|
| Auth | OAuth2 Bearer (HOTMART_TOKEN) | API key (DS24_API_KEY) via header |
| Webhook format | JSON | form-encoded (NOT JSON) |
| Signature | sha256 HMAC (HOTMART_HOTTOK) | sha512 (DS24_IPN_PASSPHRASE) |
| Response | HTTP 200 | exact string "OK" |
| Idempotency key | transaction_id | order_id |
| MoR | seller | DS24 (auto EU VAT) |
| Mock default | true | true |
| Retry max | 5, exponential backoff | retries until "OK" |

## File Placement Rules
| Artifact Type | Directory | Pillar |
|--------------|-----------|--------|
| Template | P11_feedback/templates/ | P04 |
| Examples | P11_feedback/examples/ | P04 |
| Compiled | P11_feedback/compiled/ | P04 |
| Nucleus tool | N06_commercial/P04_tools/ | P04 |
| Nucleus KCs | N06_commercial/P01_knowledge/ | P01 |
| Company config | _instances/{co}/N06_commercial/ | instance |

## Environment Variables
| Variable | Platform | Purpose |
|----------|----------|---------|
| HOTMART_TOKEN | Hotmart | OAuth2 bearer token |
| HOTMART_HOTTOK | Hotmart | Webhook sha256 HMAC secret |
| DS24_API_KEY | Digistore24 | API auth (X-DS-API-KEY) |
| DS24_IPN_PASSPHRASE | Digistore24 | IPN sha512 verification |
| DS24_SANDBOX_MODE | Digistore24 | Sandbox toggle |
| STRIPE_SECRET_KEY | Stripe | Global fallback API key |

## Security Rules
1. Secrets: NEVER plaintext → ENV_VAR only. Rotate every 90 days.
2. PCI: never store card numbers — provider tokenizes.
3. Config files: NEVER commit real keys → `.env.example` pattern.
4. Mock mode: enforced in CI/CD — live keys blocked in test environments.
5. IPN passphrase / hottok: never log — used only for signature verification.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_content_monetization]] | upstream | 0.37 |
| [[bld_config_social_publisher]] | sibling | 0.35 |
| [[bld_instruction_content_monetization]] | upstream | 0.33 |
| [[bld_config_research_pipeline]] | sibling | 0.30 |
| [[bld_knowledge_card_content_monetization]] | upstream | 0.28 |
| [[n06_kc_content_monetization]] | upstream | 0.26 |
| [[bld_collaboration_content_monetization]] | downstream | 0.25 |
| [[p03_sp_content_monetization_builder]] | upstream | 0.25 |
| [[p11_qg_content_monetization]] | downstream | 0.24 |
| [[bld_tools_content_monetization]] | downstream | 0.24 |
