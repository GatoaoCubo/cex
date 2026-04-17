---
id: n00_rate_limit_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Rate Limit Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, rate_limit_config, p09, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A rate_limit_config defines the requests-per-minute (RPM), tokens-per-minute (TPM), and budget-per-day constraints for API access. It prevents nuclei from exceeding provider quotas, implements backoff strategies on 429 errors, and enables safe concurrent grid execution by distributing load within tier limits documented in .cex/P09_config/rate_limits.yaml.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `rate_limit_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| provider | string | yes | API provider (anthropic, openai, gemini, ollama) |
| model | string | yes | Model identifier this limit applies to |
| rpm | integer | yes | Requests per minute limit |
| tpm | integer | yes | Tokens per minute limit |
| tpd | integer | no | Tokens per day limit |
| concurrent_requests | integer | no | Max simultaneous in-flight requests |
| backoff_strategy | enum | no | exponential \| linear \| fixed |
| backoff_base_ms | integer | no | Base delay for backoff calculation |
| safe_limit_pct | integer | no | Use only this % of limit to avoid 429s (default 80) |

## When to use
- Configuring the grid to respect Anthropic Sonnet's 32 concurrent request ceiling
- Setting safe limits for Gemini free tier before upgrading to paid
- Documenting provider-specific rate limits discovered during production grid runs

## Builder
`archetypes/builders/rate_limit_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind rate_limit_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: rate_limit_claude_sonnet
kind: rate_limit_config
pillar: P09
nucleus: n05
title: "Claude Sonnet Rate Limits"
version: 1.0
quality: null
---
provider: anthropic
model: claude-sonnet-4-6
rpm: 50
tpm: 200000
concurrent_requests: 20
backoff_strategy: exponential
backoff_base_ms: 1000
safe_limit_pct: 80
```

## Related kinds
- `cost_budget` (P09) -- budgets that rate limits help enforce indirectly
- `usage_quota` (P09) -- per-user quotas that rate_limit_config underpins
- `batch_config` (P09) -- batch sizing must respect rate limits
