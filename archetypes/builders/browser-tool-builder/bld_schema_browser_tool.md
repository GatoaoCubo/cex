---
kind: schema
id: bld_schema_browser_tool
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for browser_tool
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Browser Tool"
version: "1.0.0"
author: n03_builder
tags: [browser_tool, builder, examples]
tldr: "Golden and anti-examples for browser tool construction, demonstrating ideal structure and common pitfalls."
domain: "browser tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: browser_tool
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_browser_{target_slug}) | YES | - | Namespace compliance |
| kind | literal "browser_tool" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable tool name |
| engine | enum: playwright, puppeteer, selenium, browser_use, browserbase, stagehand | YES | - | Browser automation engine |
| actions | list[enum: navigate, click, type, scroll, wait, screenshot, extract, evaluate, hover, select], len >= 1 | YES | - | Supported browser actions |
| selectors | list[enum: css, xpath, text, aria, data_attr], len >= 1 | YES | - | Element selection strategies |
| output_format | enum: json, html, screenshot, text | YES | json | Primary output format |
| headless | boolean | REC | true | Default to headless mode |
| viewport | string | REC | "1280x720" | Default viewport size |
| timeout | int (ms) | REC | 30000 | Default action timeout |
| javascript | boolean | REC | true | JavaScript execution enabled |
| cookies | boolean | REC | false | Preserves cookies between actions |
| proxy | string | REC | - | Proxy configuration |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "browser_tool" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the tool does |
| user_agent | string | REC | - | Custom user agent string |
| stealth | boolean | REC | false | Anti-detection measures |
## ID Pattern
Regex: `^p04_browser_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what the tool automates, target sites/domains, use case
2. `## Engine` — browser engine details, headless/headed config, version requirements
3. `## Actions` — each supported action with syntax, params, and behavior
4. `## Selectors` — selector strategies with priority, fallback chain, and examples
5. `## Output Format` — output schema per action type, structure of returned data
## Constraints
- max_bytes: 2048 (body only)
- naming: p04_browser_{target_slug}.md
- machine_format: yaml (compiled artifact)
- id == filename stem
- actions list MUST match action names in ## Actions section
- engine must be a recognized automation engine
- quality: null always
- NO implementation code in body — spec only
