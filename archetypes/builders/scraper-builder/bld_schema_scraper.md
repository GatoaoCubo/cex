---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for scraper
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: scraper

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_scraper_{target_slug}) | YES | - | Namespace compliance |
| kind | literal "scraper" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable scraper name |
| target | string | YES | - | Target site/domain URL |
| selectors | list[string], len >= 1 | YES | - | Exact field names extracted |
| output_format | enum: json, csv, yaml | YES | json | Output data format |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "scraper" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the scraper extracts |
| pagination | enum: next_page, infinite_scroll, numbered, none | REC | none | Pagination strategy |
| rate_limit | string | REC | - | Requests per unit time |
| anti_bot | enum: none, basic, cloudflare, captcha | REC | none | Anti-bot level |
| proxy | boolean | REC | false | Requires proxy rotation |
| scheduling | string | REC | - | Cron or interval schedule |
| validation | list[string] | REC | - | Data validation rules |
| freshness | string | REC | - | Data staleness threshold |

## ID Pattern
Regex: `^p04_scraper_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Overview` — target site, data extracted, use case, consumer
2. `## Selectors` — each field: selector (CSS/XPath), type, extraction rule
3. `## Pagination & Rate Limiting` — pagination strategy, rate limits, delays
4. `## Output` — output format, validation, freshness policy

## Constraints
- max_bytes: 1024 (body only — compact scraper spec)
- naming: p04_scraper_{target_slug}.md + .yaml (dual file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- selectors list MUST match field names defined in ## Selectors section
- quality: null always
- NO implementation code in body — spec only
