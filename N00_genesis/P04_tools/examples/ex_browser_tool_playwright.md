---
id: p04_browser_playwright
kind: browser_tool
8f: F5_call
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "Playwright Browser Automation"
engine: playwright
actions:
  - navigate
  - click
  - type
  - screenshot
  - extract
selectors:
  - css
  - xpath
  - text
  - aria
output_format: json
headless: true
viewport: "1280x720"
timeout: 30000
javascript: true
cookies: true
stealth: false
quality: 9.0
tags: [browser_tool, playwright, automation, scraping]
tldr: "Playwright headless browser for web scraping, UI testing, and page interaction via CSS/XPath"
description: "Automates Chromium browser for navigation, data extraction, and interaction"
domain: "tool integration"
title: "Browser Tool Playwright"
density_score: 0.91
related:
  - bld_knowledge_card_browser_tool
  - bld_examples_browser_tool
  - p04_browser_tool_NAME
  - p10_lr_browser_tool_builder
  - bld_schema_browser_tool
  - p03_sp_browser_tool_builder
  - bld_config_browser_tool
  - bld_output_template_browser_tool
  - bld_instruction_browser_tool
  - p01_kc_browser_tool
---

# Playwright Browser Automation

## Overview
Automates a headless Chromium browser via Playwright for web scraping, UI testing, and page interaction. Used by agents that need to navigate websites, fill forms, or extract structured data from rendered pages.

## Engine
Engine: Playwright (Chromium). Headless: true. Viewport: 1280x720.
Timeout: 30000ms per action. JavaScript: enabled.

## Actions
### navigate
Navigates to a URL and waits for page load.
Params: url (string, required): Target URL
Wait: networkidle or domcontentloaded
Returns: `{"status": int, "url": "string", "title": "string"}`

### click
Clicks an element matched by selector.
Params: selector (string, required): CSS or XPath selector
Selector: `button.submit` (css)
Fallback: `//button[contains(text(),'Submit')]` (xpath)
Returns: `{"clicked": true, "selector": "string"}`

### screenshot
Captures full page or element screenshot.
Params: full_page (bool, optional): Capture entire scrollable area
Returns: `{"image": "base64_png", "width": int, "height": int}`

## Selectors
Priority order: css > aria > text > xpath
1. css (`div.product-card`): Fast, stable for well-structured pages
2. aria (`role=button[name="Add to cart"]`): Accessibility-first, resilient
3. text (`text=Add to cart`): Human-readable fallback
Fallback rule: try next strategy if primary returns null within 5s

## Output Format
Primary: json
Schema:
```json
{
  "action": "string",
  "success": "boolean",
  "data": "object | null",
  "duration_ms": "number"
}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_browser_tool]] | upstream | 0.45 |
| [[bld_examples_browser_tool]] | downstream | 0.41 |
| [[p04_browser_tool_NAME]] | sibling | 0.38 |
| [[p10_lr_browser_tool_builder]] | downstream | 0.38 |
| [[bld_schema_browser_tool]] | downstream | 0.35 |
| [[p03_sp_browser_tool_builder]] | related | 0.34 |
| [[bld_config_browser_tool]] | downstream | 0.33 |
| [[bld_output_template_browser_tool]] | downstream | 0.32 |
| [[bld_instruction_browser_tool]] | upstream | 0.31 |
| [[p01_kc_browser_tool]] | related | 0.29 |
