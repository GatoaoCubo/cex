---
id: p01_kc_browser_tool
kind: knowledge_card
type: kind
pillar: P04
title: "Browser Tool — Deep Knowledge for browser_tool"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: browser_tool
quality: 9.1
tags: [browser_tool, P04, CALL, kind-kc]
tldr: "DOM-level browser automation for navigation, interaction, scraping, and screenshot capture via Playwright or CDP"
when_to_use: "Building, reviewing, or reasoning about browser_tool artifacts"
keywords: [browser, dom, playwright, scraping]
feeds_kinds: [browser_tool]
density_score: null
related:
  - browser-tool-builder
  - p03_sp_browser_tool_builder
  - bld_collaboration_browser_tool
  - bld_knowledge_card_browser_tool
  - bld_instruction_browser_tool
  - p04_browser_playwright
  - p04_browser_tool_NAME
  - bld_examples_browser_tool
  - bld_tools_browser_tool
  - p01_kc_external_integrations
---

# Browser Tool

## Spec
```yaml
kind: browser_tool
pillar: P04
llm_function: CALL
max_bytes: 2048
naming: p04_browser_{{target}}.md + .yaml
core: true
```

## What It Is
A browser tool automates web browser interactions at the DOM level — navigating URLs, clicking elements, filling forms, extracting content, and capturing screenshots. It operates via Playwright, Puppeteer, or Chrome DevTools Protocol (CDP). It is NOT computer_use (which controls the full screen/keyboard/mouse generically) nor a search_tool (which queries search engines without navigating pages). A browser tool interacts with web pages structurally.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `PlaywrightBrowserToolkit` / community browser tools | Suite of tools for navigate, click, extract, screenshot |
| LlamaIndex | Custom `FunctionTool` wrapping Playwright | Browser actions exposed as callable tools |
| CrewAI | `BaseTool` with Playwright/Selenium in `_run()` | Agent tool automating browser interactions |
| DSPy | Python function calling Playwright in `forward()` | Direct browser automation within module execution |
| Haystack | Custom `@component` with browser automation | Browser component in scraping or testing pipelines |
| OpenAI | No native browser — `code_interpreter` can fetch URLs | Limited to HTTP fetching, not full DOM interaction |
| Anthropic | `computer_use` (screen-level) / MCP browser servers | `computer_20251124` for visual; MCP for DOM-level |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| engine | enum | "playwright" | Playwright = modern, fast; Selenium = legacy but wider support |
| headless | bool | true | Headless = fast, no display; headed = debuggable, observable |
| timeout_ms | int | 30000 | Higher = tolerant of slow pages but blocks agent longer |
| stealth | bool | false | Stealth = bypasses detection but adds complexity and fragility |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Headless scraping | Data extraction at scale | Playwright headless → navigate → extract product data |
| Observable automation | Debugging or user-visible flows | Chrome headed → user watches agent navigate |
| Parallel sessions | Multi-page concurrent scraping | Named Playwright sessions scraping different marketplaces |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Using browser for simple HTTP fetches | Massive overhead for a task that `requests` handles | Use api_client or WebFetch for non-JS pages |
| Hardcoded CSS selectors | Break on any UI change | Use data-testid attributes or semantic selectors |

## Integration Graph
```
[action_prompt] --> [browser_tool] --> [output_template]
                        |
              [computer_use, api_client]
```

## Decision Tree
- IF page requires JavaScript rendering THEN use browser_tool
- IF page is static HTML THEN use api_client/WebFetch instead
- IF need to debug visually THEN use headed mode
- IF scraping at scale THEN use headless with parallel sessions
- DEFAULT: Playwright headless with 30s timeout

## Quality Criteria
- GOOD: Clear target URL pattern, engine specified, timeout configured
- GREAT: Self-healing selectors, retry on navigation failure, screenshot on error
- FAIL: Hardcoded selectors without fallback; no timeout; uses browser for static pages

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[browser-tool-builder]] | related | 0.58 |
| [[p03_sp_browser_tool_builder]] | related | 0.44 |
| [[bld_collaboration_browser_tool]] | downstream | 0.43 |
| [[bld_knowledge_card_browser_tool]] | sibling | 0.42 |
| [[bld_instruction_browser_tool]] | upstream | 0.39 |
| [[p04_browser_playwright]] | related | 0.39 |
| [[p04_browser_tool_NAME]] | related | 0.38 |
| [[bld_examples_browser_tool]] | downstream | 0.38 |
| [[bld_tools_browser_tool]] | related | 0.36 |
| [[p01_kc_external_integrations]] | sibling | 0.35 |
