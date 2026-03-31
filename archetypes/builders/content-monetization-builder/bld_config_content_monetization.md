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

### Platform A — Hotmart (BR)
| Rule | Value | Rationale |
|------|-------|-----------|
| Auth | OAuth2 Bearer (HOTMART_TOKEN) | Standard Hotmart API auth |
| Webhook format | JSON | Hotmart sends JSON payloads |
| Signature | sha256 HMAC (HOTMART_HOTTOK) | Verify via X-Hotmart-Hottok header |
| Webhook idempotency | mandatory (transaction_id) | Duplicate webhooks cause double-charge |
| Mock mode default | true | Never hit live payment in dev |
| Sandbox | hotmart.com/developer test env | Separate test environment |

### Platform B — Digistore24 (International)
| Rule | Value | Rationale |
|------|-------|-----------|
| Auth | API key (DS24_API_KEY) via X-DS-API-KEY header | Standard DS24 API auth |
| IPN format | form-encoded (NOT JSON) | DS24 sends form-encoded, not JSON |
| Signature | sha512 (DS24_IPN_PASSPHRASE) | Hash verification on payload fields |
| IPN response | exact string "OK" | DS24 retries until body = "OK" |
| Webhook idempotency | mandatory (order_id) | Duplicate IPNs cause double-credit |
| Mock mode default | true | DS24 has sandbox/test product mode |
| Merchant of Record | DS24 | DS24 collects/remits EU VAT automatically |
| Languages | DE, EN, ES, FR, IT, NL, PL | 7 native checkout languages |
| Payment methods | SEPA+Sofort (DE), iDEAL (NL), cards+PayPal (global) | Per-country optimization |

### Shared Rules
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

## Environment Variables
| Variable | Platform | Purpose |
|----------|----------|---------|
| HOTMART_TOKEN | Hotmart | OAuth2 bearer token for API calls |
| HOTMART_HOTTOK | Hotmart | Webhook signature verification secret |
| HOTMART_PRODUCT_ID | Hotmart | Product identifier |
| DS24_API_KEY | Digistore24 | API authentication via X-DS-API-KEY header |
| DS24_IPN_PASSPHRASE | Digistore24 | IPN sha512 signature verification |
| DS24_IPN_URL | Digistore24 | IPN endpoint URL |
| DS24_SANDBOX_MODE | Digistore24 | Enable/disable sandbox (true/false) |
| DS24_PRODUCT_ID | Digistore24 | Product identifier |
| STRIPE_SECRET_KEY | Stripe | API key (global fallback) |
| STRIPE_WEBHOOK_SECRET | Stripe | Webhook signature secret |

## Security Rules
1. Payment secrets: NEVER plaintext → always ENV_VAR (SCREAMING_SNAKE_CASE)
2. Webhook secrets: rotate every 90 days (both Hotmart HOTTOK and DS24 IPN_PASSPHRASE)
3. PCI compliance: never store card numbers — provider handles tokenization
4. Config files: NEVER commit with real keys → `.env.example` pattern
5. Mock mode: enforced in CI/CD — live keys blocked in test environments
6. DS24 IPN passphrase: never log or expose — used only for sha512 verification
7. Hotmart hottok: never log or expose — used only for sha256 HMAC verification
