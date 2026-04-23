---
kind: config
id: bld_config_browser_tool
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Browser Tool"
version: "1.0.0"
author: n03_builder
tags: [browser_tool, builder, examples]
tldr: "Golden and anti-examples for browser tool construction, demonstrating ideal structure and common pitfalls."
domain: "browser tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_browser_tool
  - bld_knowledge_card_browser_tool
  - p03_sp_browser_tool_builder
  - p04_browser_tool_NAME
  - bld_schema_browser_tool
  - browser-tool-builder
  - p04_browser_playwright
  - bld_config_computer_use
  - p11_qg_browser_tool
  - p10_lr_browser_tool_builder
---
# Config: browser_tool Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_browser_{target_slug}.md` | `p04_browser_marketplace_scraper.md` |
| Builder directory | kebab-case | `browser-tool-builder/` |
| Frontmatter fields | snake_case | `output_format`, `headless`, `user_agent` |
| Target slug | snake_case, lowercase, no hyphens | `marketplace_scraper`, `checkout_flow` |
| Action names | lowercase verb | `navigate`, `click`, `extract`, `screenshot` |
| Selector values | lowercase | `css`, `xpath`, `aria`, `data_attr`, `text` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_browser_{target_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_browser_{target_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~3500 bytes
- Density: >= 0.80 (no filler)
## Engine Enum
| Value | Notes |
|-------|-------|
| playwright | Default. Python/JS/TS, cross-browser, auto-wait |
| puppeteer | Node.js only, Chrome/Chromium |
| selenium | Legacy/enterprise, remote grid |
| browser_use | LLM-driven, Python |
| browserbase | Cloud headless, managed |
| stagehand | TypeScript, AI-assisted |
## Output Format Enum
| Value | When to use |
|-------|-------------|
| json | Structured data extraction, machine-readable |
| html | Raw DOM snapshot for downstream parsing |
| screenshot | Visual capture, debugging, verification |
| text | Plain text extraction, readable content |
## Action Enum
| Value | Description |
|-------|-------------|
| navigate | Load a URL and wait for page state |
| click | Activate an element |
| type | Input text into a form field |
| scroll | Scroll page or element in a direction |
| wait | Pause until selector or condition is met |
| screenshot | Capture viewport or full page |
| extract | Read structured data from DOM elements |
| evaluate | Execute arbitrary JavaScript in page context |
| hover | Move pointer to element without clicking |
| select | Choose an option in a select/dropdown element |
## Timeout Conventions
| Scenario | Recommended timeout |
|----------|---------------------|
| Simple static page | 10000ms |
| SPA / dynamic content | 30000ms (default) |
| Slow e-commerce | 45000ms |
| Network-intercepted mock | 5000ms |
Rule: every browser_tool MUST define timeout (implicit default 30000ms is acceptable if not overridden, but explicit is preferred).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_browser_tool]] | upstream | 0.44 |
| [[bld_knowledge_card_browser_tool]] | upstream | 0.42 |
| [[p03_sp_browser_tool_builder]] | upstream | 0.39 |
| [[p04_browser_tool_NAME]] | upstream | 0.36 |
| [[bld_schema_browser_tool]] | upstream | 0.35 |
| [[browser-tool-builder]] | upstream | 0.33 |
| [[p04_browser_playwright]] | upstream | 0.31 |
| [[bld_config_computer_use]] | sibling | 0.30 |
| [[p11_qg_browser_tool]] | downstream | 0.27 |
| [[p10_lr_browser_tool_builder]] | downstream | 0.27 |
