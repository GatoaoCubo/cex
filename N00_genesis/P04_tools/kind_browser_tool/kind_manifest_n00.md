---
id: n00_browser_tool_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Browser Tool -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, browser_tool, p04, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A browser_tool provides agents with programmatic browser control capabilities: DOM parsing, page navigation, form interaction, screenshot capture, and JavaScript execution. It abstracts Playwright, Puppeteer, or Selenium into a unified tool interface so agents can scrape, interact with, and extract data from any website. The output is a structured browser automation module callable from agent tool loops.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `browser_tool` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| engine | string | yes | Browser engine: playwright, puppeteer, selenium |
| capabilities | list | yes | navigate, click, type, screenshot, extract_text, js_eval |
| headless | boolean | yes | Whether browser runs headless or with UI |
| anti_detection | boolean | no | Whether stealth mode / fingerprint evasion is enabled |

## When to use
- When an agent needs to extract data from websites that require JavaScript rendering
- When competitive intelligence research requires navigating and scraping dynamic pages
- When building a research_pipeline that includes web data collection as a source stage

## Builder
`archetypes/builders/browser_tool-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind browser_tool --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: bt_playwright_scraper
kind: browser_tool
pillar: P04
nucleus: n01
title: "Playwright Web Scraper"
version: 1.0
quality: null
---
engine: playwright
capabilities: [navigate, screenshot, extract_text, js_eval]
headless: true
anti_detection: true
```

## Related kinds
- `search_tool` (P04) -- search-first alternative to full browser automation
- `document_loader` (P04) -- processes the HTML/PDF output from browser_tool
- `research_pipeline` (P04) -- pipeline that uses browser_tool in its RETRIEVE stage
- `computer_use` (P04) -- higher-level capability that includes browser_tool as a subsystem
