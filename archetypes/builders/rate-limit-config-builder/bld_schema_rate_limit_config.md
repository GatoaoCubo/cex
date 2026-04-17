---
kind: schema
id: bld_schema_rate_limit_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for rate_limit_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Rate Limit Config"
version: "1.0.0"
author: n03_builder
tags: [rate_limit_config, builder, examples]
tldr: "Golden and anti-examples for rate limit config construction, demonstrating ideal structure and common pitfalls."
domain: "rate limit config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: rate_limit_config

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_rl_{slug}) | YES | - | Namespace compliance |
| kind | literal "rate_limit_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable config name |
| provider | string | YES | - | e.g. anthropic, openai, litellm |
| rpm | integer | YES | - | Requests per minute limit |
| tpm | integer | YES | - | Tokens per minute limit |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "rate_limit_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| budget_usd | float | REC | - | Monthly budget cap in USD |
| tier | string | REC | - | free, build, scale, enterprise |
| rpd | integer | REC | - | Requests per day limit |
| concurrent | integer | REC | - | Max concurrent requests |
| retry_after | integer | REC | - | Seconds to wait after 429 |
| model_overrides | map[string, {rpm, tpm}] | REC | - | Per-model limit overrides |
| alert_threshold | float 0-1 | REC | - | Fraction of limit to trigger alert |
| description | string <= 200ch | REC | - | What this config governs |
## ID Pattern
Regex: `^p09_rl_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what this rate limit config does, which provider
2. `## Limits` — RPM, TPM, RPD, concurrent with values
3. `## Tier` — tier description, upgrade path
4. `## Budget` — monthly cap, alert threshold, overage policy
## Constraints
- max_bytes: 1024 (body only — compact config spec)
- naming: p09_ratelimit_{provider}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- rpm + tpm MUST be positive integers
- quality: null always
- NO credentials or API keys in body — config only
