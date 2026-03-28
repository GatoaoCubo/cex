---
id: p11_qg_scraper
kind: quality_gate
pillar: P11
title: "Gate: Scraper"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: scraper
quality: null
density_score: 0.85
tags:
  - quality-gate
  - scraper
  - data-extraction
  - p11
tldr: "Gates ensuring scraper files specify target site, selectors, output format, rate limiting, and legal compliance before deployment."
---

## Definition

A scraper extracts structured data from one or more web sources on a defined schedule or trigger. A scraper passes this gate when an engineer could deploy it safely (without harming the target site or violating terms of service), the output matches its downstream consumer's schema, and failures degrade gracefully without data corruption.

---

## HARD Gates

Failure on any HARD gate = immediate REJECT regardless of score.

| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`scraper-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `scraper` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Target site or URL pattern** (exact domain, path pattern, or regex the scraper will fetch) | Without a target, the scraper cannot be deployed or reviewed for compliance |
| H08 | Spec contains **Selectors** (CSS selectors or XPath expressions) for each extracted field | Selectors are the executable contract; prose descriptions are not sufficient |
| H09 | Spec contains an **Output format definition** (field names, types, and example row) | Output schema must be validated against the consumer before deployment |

---

## SOFT Scoring

Dimensions are weighted; total normalized weight = 100%.

| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Pagination strategy documented (how to advance through multi-page results) | 1.0 | No pagination described | Strategy named, no detail | Full logic: next-page selector, stop condition, max pages |
| 3 | Rate limiting configured (delay between requests, requests-per-minute ceiling) | 1.0 | No rate limiting | Fixed delay only | Dynamic rate with backoff on 429 and 503 responses |
| 4 | Anti-bot awareness noted (headers, cookies, user-agent rotation, captcha handling) | 1.0 | No mention | User-agent set only | Full headers, cookie jar, rotation strategy, captcha fallback |
| 5 | Output schema matches consumer (field names and types verified against downstream) | 1.0 | No validation mentioned | Author claims match | Explicit cross-reference to consumer schema file |
| 6 | Tags include `scraper` | 0.5 | Missing | Present but misspelled | Exactly `scraper` in tags list |
| 7 | Error handling for missing elements (what to do when a selector returns nothing) | 1.0 | No error handling | Null on missing | Null + logging + alert threshold for sustained misses |
| 8 | Proxy rotation declared (explicitly not needed with reason, or rotation config provided) | 0.5 | No mention | Noted as future work | Clear declaration: not needed (with reason) or config provided |
| 9 | Freshness and scheduling defined (run frequency, cache TTL, staleness threshold) | 1.0 | No scheduling | Cron expression only | Cron + cache TTL + staleness alert + manual trigger procedure |
| 10 | Legal compliance noted (robots.txt checked, terms of service reviewed, data use stated) | 1.0 | No compliance note | robots.txt checked only | robots.txt + ToS review result + data retention policy |

Score = sum(rating * weight) / sum(weights) normalized to 0-10.

---

## Actions

| Threshold | Action |
|-----------|--------|
| >= 9.5 | GOLDEN — archive to pool, tag as reference implementation |
| >= 8.0 | PUBLISH — merge to main, approved for production deployment |
| >= 7.0 | REVIEW — return to author with dimension-level feedback |
| < 7.0 | REJECT — do not merge; author must revise from scratch or substantially rewrite |

---

## Bypass

| Field | Value |
|-------|-------|
| condition | Internal site only (target is owned by the same organization) and data volume is under 1,000 records per run |
| approver | Domain lead with written sign-off confirming site ownership |
| audit_log | Entry required in `records/audits/gate_bypasses.md` with date, target URL, approver, and expiry |
| expiry | 30 days; scraper must pass full gate before production use beyond the trial period |

H01 (parseable frontmatter) and H05 (quality=null) are NEVER bypassable under any condition.
