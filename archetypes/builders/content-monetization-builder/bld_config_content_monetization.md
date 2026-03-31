---
kind: config
id: bld_config_content_monetization
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: content_monetization Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Config file | `content_monetization_config_{empresa}.yaml` | `content_monetization_config_codexa.yaml` |
| Template | `tpl_content_monetization.md` | P04_tools/templates/ |
| Examples | `ex_content_monetization_{model}.md` | `ex_content_monetization_saas.md` |
| Instance | `content_monetization_config.md` | _instances/{co}/N06_commercial/ |
| Frontmatter id | `p04_cli_content_monetization_{slug}` | `p04_cli_content_monetization_codexa` |

## Size Limits
| Artifact | Max Size | Rationale |
|----------|---------|-----------|
| Config YAML | 4096 bytes | Dense config, human-editable |
| Template | 4096 bytes | Builder ISO limit |
| Example | 4096 bytes | Builder ISO limit |
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
| Rule | Value | Rationale |
|------|-------|-----------|
| Webhook idempotency | mandatory | Duplicate webhooks cause double-charge |
| Mock mode default | true | Never hit live payment in dev |
| Retry max | 5 attempts | Beyond 5, alert human |
| Retry backoff | exponential (1s, 2s, 4s, 8s, 16s) | Prevents thundering herd |

## File Placement Rules
| Artifact Type | Directory | Pillar |
|--------------|-----------|--------|
| Template | P04_tools/templates/ | P04 |
| Examples | P04_tools/examples/ | P04 |
| Compiled | P04_tools/compiled/ | P04 |
| Nucleus tool | N06_commercial/tools/ | P04 |
| Nucleus KCs | N06_commercial/knowledge/ | P01 |
| Company config | _instances/{co}/N06_commercial/ | instance |

## Security Rules
1. Payment secrets: NEVER plaintext → always ENV_VAR
2. Webhook secrets: rotate every 90 days
3. PCI compliance: never store card numbers — provider handles tokenization
4. Config files: NEVER commit with real keys → `.env.example` pattern
5. Mock mode: enforced in CI/CD — live keys blocked in test environments
