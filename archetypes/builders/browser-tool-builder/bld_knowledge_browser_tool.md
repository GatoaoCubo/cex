---
kind: knowledge_card
id: bld_knowledge_card_browser_tool
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for browser_tool production — browser automation and DOM interaction specification
sources: Playwright docs, Puppeteer API, W3C WebDriver, ARIA spec, CSS selectors level 4
quality: 9.1
title: "Knowledge Card Browser Tool"
version: "1.0.0"
author: n03_builder
tags: [browser_tool, builder, examples]
tldr: "Golden and anti-examples for browser tool construction, demonstrating ideal structure and common pitfalls."
domain: "browser tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_browser_tool_builder
  - p10_lr_browser_tool_builder
  - bld_instruction_browser_tool
  - browser-tool-builder
  - p04_browser_playwright
  - bld_config_browser_tool
  - bld_architecture_browser_tool
  - p11_qg_browser_tool
  - p01_kc_browser_tool
  - bld_examples_browser_tool
---

# Domain Knowledge: browser_tool
## Executive Summary
Browser tools are DOM-driven automation artifacts that control a browser engine to interact with web pages. They navigate URLs, interact with elements via selectors, extract structured data, and return output as JSON, HTML, screenshot, or text. Browser tools are NOT generic screen controllers (computer_use), NOT search API wrappers (search_tool), and NOT image analyzers (vision_tool). The key distinction: browser_tool operates via the DOM API — it reads and manipulates the document object model, not raw pixels.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Output formats | json, html, screenshot, text |
| Default engine | playwright |
| Default headless | true |
| Default timeout | 30000ms |
| Default viewport | 1280x720 |
| Selector priority | data_attr > aria > css > xpath |
## Engine Decision Matrix
| Need | Engine | Reason |
|------|--------|--------|
| Modern web, cross-browser, Python/JS | playwright | Best selector API, auto-wait, network interception |
| Chrome-only, Node.js team | puppeteer | Native Chrome DevTools Protocol, fast |
| Legacy apps, Java/Python, grid | selenium | Widest language support, remote grid |
| LLM-directed autonomous browsing | browser_use | Natural language to DOM actions |
| Cloud-scale, no infra | browserbase | Managed headless, built-in stealth |
| AI-assisted, TypeScript-native | stagehand | Semantic actions, vision+DOM hybrid |
## Action Reference
| Action | Purpose | Key Params |
|--------|---------|-----------|
| navigate | Load URL | url, waitUntil |
| click | Activate element | selector, button |
| type | Input text | selector, text |
| scroll | Scroll page | direction, distance |
| wait | Pause until condition | selector, timeout |
| screenshot | Capture viewport | fullPage, path |
| extract | Read DOM data | selector, attribute |
| evaluate | Run JavaScript | script, args |
## Selector Strategy
| Strategy | Stability | When |
|----------|-----------|------|
| data_attr | High | QA-annotated, test-stable |
| aria | High | Accessible elements |
| css | Medium | Well-maintained classes |
| xpath | Low | Deep nesting fallback |
| text | Medium | Buttons with stable text |
Fallback: attempt in priority order; try next if null.
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No selector fallback | First fragile selector breaks entire extraction |
| Hardcoded absolute XPath | Breaks on any DOM restructure |
| Missing timeout config | Unbounded waits hang automation indefinitely |
| Omitting headless flag | Headed mode in CI/server environments fails |
| No wait before extract | Race condition: element not yet in DOM |
| Using computer_use for DOM data | Pixel-based reading is fragile vs DOM API |
| Self-scoring quality | Corrupts pool quality metrics |
## Application
1. Define target site and data needed
2. Choose engine (playwright default; specialize if needed)
3. List actions in execution order
4. Specify selectors with fallback chain
5. Set output format and configure headless/viewport/timeout
6. Validate: actions match frontmatter, selectors documented

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_browser_tool_builder]] | downstream | 0.56 |
| [[p10_lr_browser_tool_builder]] | downstream | 0.53 |
| [[bld_instruction_browser_tool]] | downstream | 0.50 |
| [[browser-tool-builder]] | downstream | 0.49 |
| [[p04_browser_playwright]] | downstream | 0.46 |
| [[bld_config_browser_tool]] | downstream | 0.46 |
| [[bld_architecture_browser_tool]] | downstream | 0.41 |
| [[p11_qg_browser_tool]] | downstream | 0.40 |
| [[p01_kc_browser_tool]] | sibling | 0.39 |
| [[bld_examples_browser_tool]] | downstream | 0.38 |
