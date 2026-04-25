---
id: p01_kc_tag_grading_structured_data
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "TAG Grading: Structured Data Extraction on CSR Pages"
version: 2.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: research
quality: 9.1
tags: [tag-grading, structured-data, browser-automation, scraping, csr]
tldr: "TAG certificates require browser: WebFetch returns scripts, but JSON-LD and grades only exist in the rendered DOM."
when_to_use: "Extract data from pages that render certificates via JavaScript"
keywords: [tag_grading, dynamic_scraping, json_ld, structured_data, playwright]
long_tails:
  - "How to extract JSON-LD from CSR page with browser automation"
  - "When WebFetch fails on JS-rendered certificates"
axioms:
  - "ALWAYS validate if the page is CSR before finishing scraping"
  - "NEVER assume absence of schema if initial HTML comes empty"
linked_artifacts:
  primary: null
  related: [p01_kc_claude_server_tools]
density_score: 1.0
data_source: "TAG Grading page analysis T9403163 — static fetch blocked"
related:
  - output_content_factory_landscape
  - p01_kc_browser_tool
  - output_content_factory_internal_audit
  - browser-tool-builder
  - bld_config_browser_tool
  - p04_browser_tool_NAME
  - bld_collaboration_browser_tool
  - landing-page-builder
  - bld_knowledge_card_browser_tool
  - bld_tools_landing_page
---

## Quick Reference

topic: structured data extraction | scope: TAG certificates | criticality: high
target page: T9403163 | blocker: static fetch | decision: browser automation

## Key Concepts

- WebFetch returned scripts, no complete certificate
- JSON-LD and grades appear only after JS render
- CSR pages require final DOM, not response HTML
- Browser automation eliminates false negative on schema

## Comparison

| Method | Captures metas | Captures grade | Cost | Scale |
|--------|----------------|----------------|------|-------|
| Static fetch | Low | None | Minimal | High |
| Browser render | High | High | Medium | Medium |
| Manual inspection | Medium | High | High (h/h) | None |
| API discovery | High | High | Minimal | High |
| Network trace | High | Medium | Low | Low |

| HTML Signal | Diagnosis | Next action |
|-------------|-----------|-------------|
| Scripts/analytics only | CSR likely | Use browser |
| IDs without payload | Data via API/XHR | Network trace |
| OG/JSON-LD absent | Render pending | Wait for DOM |
| 200 OK empty body | Pure SPA | Playwright wait |
| 403 or captcha | Anti-bot active | Headers + proxy |

| Tool | JS render | Setup | Parallelism |
|------|-----------|-------|-------------|
| Playwright | Yes | Medium | High |
| Puppeteer | Yes | Medium | High |
| Selenium | Yes | High | Limited |
| curl/httpx | No | Minimal | High |
| Firecrawl | Yes | SaaS | High |

## Golden Rules

- ALWAYS wait for final DOM before extracting schema
- ALWAYS inspect Network if body comes empty
- NEVER mark page as "no schema" on 1st fetch
- ALWAYS save screenshot and HTML for auditing

## Code

<!-- lang: python | purpose: render page then extract structured data -->
```python
from playwright.sync_api import sync_playwright

def extract_after_render(url: str) -> dict:
    with sync_playwright() as p:
        page = p.chromium.launch().new_page()
        page.goto(url, wait_until="networkidle")
        return {
            "html": page.content(),
            "json_ld": page.locator(
                "script[type='application/ld+json']"
            ).all_text_contents(),
            "meta_count": page.locator("meta").count(),
        }
```

## References

- external: https://my.taggrading.com/card/T9403163
- external: https://playwright.dev/python/docs/intro
- external: https://schema.org/
- deepens: p01_kc_claude_server_tools


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[output_content_factory_landscape]] | related | 0.25 |
| [[p01_kc_browser_tool]] | sibling | 0.23 |
| [[output_content_factory_internal_audit]] | related | 0.23 |
| [[browser-tool-builder]] | downstream | 0.23 |
| [[bld_config_browser_tool]] | downstream | 0.21 |
| [[p04_browser_tool_NAME]] | downstream | 0.20 |
| [[bld_collaboration_browser_tool]] | downstream | 0.19 |
| [[landing-page-builder]] | downstream | 0.19 |
| [[bld_knowledge_card_browser_tool]] | sibling | 0.19 |
| [[bld_tools_landing_page]] | downstream | 0.19 |
