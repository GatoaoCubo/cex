---
id: ex-research-pipeline-marketplace-scrap
kind: research_pipeline
8f: F5_call
pillar: P04
title: Marketplace Scrap Research Pipeline
version: 0.1.0
quality: 8.9
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_VERTICAL
  - BRAND_COMPETITOR_WHITELIST
tags: [commerce, template, distillation, research, scraping]
density_score: 0.98
related:
  - bld_collaboration_research_pipeline
  - p08_ac_brand_nucleus
  - p04_tool_scraping_config
  - bld_instruction_research_pipeline
  - p02_mm_commercial_nucleus
  - p08_ac_intelligence
  - research-pipeline-builder
  - p08_pat_pricing_framework
  - agent_card_n01
  - p01_kc_web_scraping_ethics
---

# Marketplace Scrap Research Pipeline

## Purpose
Scheduled research loop that harvests competitor + vertical-wide market intelligence from Mercado Livre, Shopify storefronts, and other public marketplaces. Produces a daily `market_intelligence` knowledge set used by the pricing, sales copy, and catalog teams.

## When to use
- Brand operates in a competitive vertical where price / availability / title signals matter weekly.
- Manual research takes >2h per week and would benefit from automation.
- You already have an allow-list of competitor domains/seller_ids and respect their robots/terms.

## When NOT to use
- Public-API-only research -- go through the api_client, not a scraper.
- Restricted data (accounts-only pages, gated content) -- do not scrape.

## Brand variables used
- `{{BRAND_NAME}}` -- attribution on research outputs; referenced in ops dashboards.
- `{{BRAND_VERTICAL}}` -- narrows search queries to the brand's category.
- `{{BRAND_COMPETITOR_WHITELIST}}` -- JSON array of approved competitor handles; pipeline refuses to hit anything outside.

## Pipeline phases
1. **Seed** -- read `{{BRAND_COMPETITOR_WHITELIST}}` + top-N vertical keywords for `{{BRAND_VERTICAL}}`.
2. **Discover** -- for each query, fetch the marketplace search results page via `ex_browser_tool_marketplace_scrap.md`; extract listing URLs.
3. **Fetch** -- per listing, fetch HTML; rate-limit 1 req/sec per domain, 5 concurrent global.
4. **Extract** -- structured parse: title, price, reviews, seller, shipping, images (urls only).
5. **Deduplicate** -- normalize listing id; drop already-seen rows from prior 24h run.
6. **Score** -- tag each row with `price_vs_brand`, `title_similarity`, `availability_signal`.
7. **Persist** -- write to `market_intelligence` table with `run_id` + `source`.
8. **Summarize** -- LLM pass generates a 10-bullet digest per brand per run.

## Respectful scraping contract
- `User-Agent: {{BRAND_NAME}}-ResearchBot (+mailto:{{BRAND_SUPPORT_EMAIL}})`.
- Honor `robots.txt` -- fetch once per domain per day, cache.
- Backoff on any 429/503 for 10 min before retrying the domain.
- Never log in. Never bypass paywalls.
- Retain raw HTML for 7 days (debugging); delete after -- minimizes data footprint.

## Output contract
- `market_intelligence` table row per listing: `{run_id, source, listing_id, title, price_cents, stock_signal, fetched_at}`.
- Daily summary artifact: `_reports/market_intel/{{date}}.md` with LLM digest + top anomalies.

## Safety + legal notes
- Pipeline is read-only research; no competitive injection, no price probing via fake carts, no account creation.
- Per Brazilian LGPD: no PII captured (seller names considered business identifiers, not PII).
- Keep the whitelist tight; adding competitors requires operator approval flow.

## Related artifacts
- `ex_browser_tool_marketplace_scrap.md` -- execution layer.
- `ex_api_client_meli.md` -- prefer API over scrape when endpoint covers the need.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_research_pipeline]] | downstream | 0.24 |
| [[p08_ac_brand_nucleus]] | downstream | 0.21 |
| [[p04_tool_scraping_config]] | related | 0.21 |
| [[bld_instruction_research_pipeline]] | upstream | 0.21 |
| [[p02_mm_commercial_nucleus]] | upstream | 0.20 |
| [[p08_ac_intelligence]] | downstream | 0.20 |
| [[research-pipeline-builder]] | related | 0.20 |
| [[p08_pat_pricing_framework]] | downstream | 0.19 |
| [[agent_card_n01]] | related | 0.19 |
| [[p01_kc_web_scraping_ethics]] | upstream | 0.18 |
