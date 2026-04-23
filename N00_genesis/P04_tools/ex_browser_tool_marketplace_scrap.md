---
id: ex-browser-tool-marketplace-scrap
kind: browser_tool
pillar: P04
title: Marketplace Scrap Browser Tool
version: 0.1.0
quality: 8.9
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_SUPPORT_EMAIL
  - BRAND_COMPETITOR_WHITELIST
tags: [commerce, template, distillation, browser, scraping]
density_score: 0.97
related:
  - p01_kc_browser_tool
  - p04_browser_playwright
  - bld_schema_model_registry
  - bld_schema_browser_tool
  - bld_knowledge_card_browser_tool
  - p04_browser_tool_NAME
  - bld_examples_browser_tool
  - n06_schema_brand_config
  - bld_schema_tagline
  - bld_schema_experiment_tracker
---

# Marketplace Scrap Browser Tool

## Purpose
Headless-browser execution layer for the marketplace research pipeline. Renders JavaScript-heavy marketplace pages (Mercado Livre listings, Shopify-hosted storefronts) so the downstream extractor sees the fully hydrated DOM instead of a React shell.

## When to use
- Target page hides key data (price, stock, variants) behind client-side rendering.
- Static `fetch` returns an empty `<div id="root">` without useful content.
- You need screenshots for visual diffing across runs.

## When NOT to use
- Page ships data in the initial HTML -- use lightweight HTTP fetch.
- Site has an approved API -- use `ex_api_client_meli.md` or equivalent.
- Target forbids automation in its terms (respect before rendering).

## Brand variables used
- `{{BRAND_NAME}}` -- included in the user-agent string for transparency.
- `{{BRAND_SUPPORT_EMAIL}}` -- mailto in user-agent so site operators can reach the brand if they object.
- `{{BRAND_COMPETITOR_WHITELIST}}` -- tool refuses URLs whose origin is not in the allow-list.

## Interface
```ts
browserTool.render({
  url: string,               // must match whitelist
  wait_for: string,          // CSS selector to consider "ready"
  timeout_ms: number,        // default 20000
  take_screenshot?: boolean, // default false
  extract?: Record<string, string>, // css selectors -> field names
}): Promise<{ html: string, fields?: Record<string,string>, screenshot?: Buffer }>
```

## Runtime choice
- Default engine: Playwright + Chromium headless.
- Why not Puppeteer? Playwright has better network intercept + auto-wait semantics.
- Why not a SaaS (Browserless / ScrapingBee)? Reserved for high-volume runs; local Playwright is cheaper for daily research.

## User-agent + headers
```
User-Agent: {{BRAND_NAME}}-ResearchBot/1.0 (+mailto:{{BRAND_SUPPORT_EMAIL}})
Accept-Language: pt-BR,pt;q=0.9,en;q=0.8
```
Do NOT impersonate a real browser's UA -- deceptive UAs violate most sites' terms.

## Resource limits
- Per-call CPU: 1 core, 512 MB RAM.
- Network: block all third-party analytics/ads (via route intercept) -- saves 70% of bandwidth and is friendlier to the target server.
- Concurrent pages: max 3 per worker; beyond that CPU thrashes.

## Screenshot usage
Screenshots are for visual diff ONLY:
- Store as PNG in `bucket: research-screenshots/{run_id}/{listing_id}.png`.
- Retain 7 days; automated cleanup afterwards.
- Never publish screenshots outside the internal research dashboard.

## Error handling
- Timeout (selector never appears) -> return `{ html: null, reason: "timeout" }`; downstream pipeline logs + continues.
- HTTP error (4xx/5xx) -> return with `reason` -- do NOT retry at this layer; pipeline handles retries.
- Navigation aborted (redirect off whitelist) -> treat as timeout; refuse to follow.

## Related artifacts
- `ex_research_pipeline_marketplace_scrap.md` -- invoking pipeline.
- `ex_api_client_meli.md` -- preferred alternative when an API exists.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_browser_tool]] | related | 0.28 |
| [[p04_browser_playwright]] | sibling | 0.28 |
| [[bld_schema_model_registry]] | downstream | 0.26 |
| [[bld_schema_browser_tool]] | downstream | 0.25 |
| [[bld_knowledge_card_browser_tool]] | upstream | 0.25 |
| [[p04_browser_tool_NAME]] | sibling | 0.25 |
| [[bld_examples_browser_tool]] | downstream | 0.24 |
| [[n06_schema_brand_config]] | downstream | 0.24 |
| [[bld_schema_tagline]] | downstream | 0.23 |
| [[bld_schema_experiment_tracker]] | downstream | 0.23 |
