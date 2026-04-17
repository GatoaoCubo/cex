---
id: ex_browser_tool_marketplace_scrap
kind: browser_tool
pillar: P04
title: Marketplace Web Scraper Tool
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, scraper, marketplace, browser_tool]
---

## Purpose

Browser-based web scraping tool for collecting marketplace product data (Mercado Livre, regional distributors) when no structured API is available — used as a fallback enrichment source for the catalog research pipeline.

## When to Use

- API quotas exhausted; need product data from ML public pages.
- Scraping regional Brazilian pet distributors that do not expose APIs.
- Collecting competitor pricing for market intelligence.
- Enriching product records with detailed descriptions from distributor pages.

## Capability Specification

| Capability | Support |
|-----------|---------|
| JavaScript rendering | Yes (headless Chromium) |
| Pagination navigation | Yes |
| Anti-bot detection bypass | Rotating user agents, delays, no fingerprint |
| CAPTCHA handling | Manual intervention (not automated) |
| Login-gated pages | Not supported (public pages only) |
| Rate limiting | Configurable delay 500ms-3000ms between requests |
| Output formats | JSON, CSV, Markdown |

## Scraping Targets

| Target | URL Pattern | Data Extracted |
|--------|------------|----------------|
| Mercado Livre item page | `https://www.mercadolivre.com.br/MLB-{id}` | title, price, description, images, seller |
| ML search results | `https://lista.mercadolivre.com.br/{query}` | item list, prices, ratings |
| Distributor catalog | `https://{distributor_domain}/produtos` | SKU, price, stock status |

## Tool Configuration

```yaml
browser:
  engine: chromium-headless
  viewport: "1280x800"
  user_agent: rotate            # selects from 10+ real UA strings
  javascript_enabled: true
  images_disabled: true         # faster loading
  request_timeout_ms: 15000

throttle:
  min_delay_ms: 500
  max_delay_ms: 2000
  jitter: true                  # randomize within range
  retry_on_503: 3

output:
  storage: supabase_storage
  bucket: "scrape-results"
  path_prefix: "marketplace/{{BRAND_SUPABASE_PROJECT_REF}}"
```

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `urls[]` | string[] | List of URLs to scrape |
| `selectors` | object | CSS/XPath selectors per site |
| `max_pages` | int | Pagination limit (default: 10) |
| `output_format` | enum | `json` \| `csv` \| `markdown` |

| Output | Type | Description |
|--------|------|-------------|
| `results[]` | JSON objects | Extracted product data per URL |
| `errors[]` | string[] | Failed URLs with reason |
| `report_path` | string | Supabase storage path of output file |

## Selectors (Mercado Livre)

```javascript
const selectors = {
  meli_item: {
    title:       'h1.ui-pdp-title',
    price:       '.andes-money-amount__fraction',
    description: '.ui-pdp-description__content',
    images:      '.ui-pdp-gallery__figure img[data-zoom]',
    condition:   '.ui-pdp-subtitle',
  },
};
```

> Selectors break when ML redesigns pages. Maintain a selector registry and version them.

## Usage Example

```typescript
// Enrich one product from ML public page
const result = await scraper.scrape({
  url: `https://www.mercadolivre.com.br/MLB-${meliId}`,
  selectors: selectors.meli_item,
});
if (result.ok) {
  await supabase.from('products')
    .update({ description: result.description, meli_price: parseFloat(result.price) })
    .eq('meli_id', meliId);
}
```

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project for output storage |

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_research_pipeline_marketplace_scrap.md` | research_pipeline | Orchestrates scraping pipeline |
| `ex_api_client_meli.md` | api_client | Preferred API-based enrichment (no scraping) |
