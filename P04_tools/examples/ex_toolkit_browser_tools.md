---
id: p04_tk_browser_tools
kind: toolkit
pillar: P04
title: "Example — Browser Tools Toolkit"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
name: browser_tools
category: web
tools_count: 5
requires_confirmation: [navigate, click, fill_form]
denied_for: [n04, n06]
domain: toolkit
quality: 9.1
tags: [toolkit, browser, web, automation, MCP, tools]
tldr: "Browser toolkit — 5 tools (screenshot, navigate, click, fill_form, extract_text) for web automation via Chrome MCP. Confirmation required for mutations."
when_to_use: "Agents that need to interact with web pages for research, testing, or data extraction"
keywords: [toolkit, browser, chrome, MCP, web, automation, screenshot]
density_score: null
---

# Toolkit: Browser Tools

## Tools
| Tool | Type | Input | Output | Confirmation |
|------|------|-------|--------|-------------|
| screenshot | read | url or current tab | PNG image | no |
| navigate | write | url | page_loaded status | yes |
| click | write | selector | element state | yes |
| fill_form | write | selector, value | filled status | yes |
| extract_text | read | selector (optional) | text content | no |

## Permissions
| Permission Level | Tools | Rationale |
|-----------------|-------|-----------|
| Auto-approve | screenshot, extract_text | Read-only, no side effects |
| Confirm once | navigate | URL change is reversible |
| Confirm each | click, fill_form | Mutations may submit forms or trigger actions |

## Denied Nuclei
| Nucleus | Reason |
|---------|--------|
| N04 (Knowledge) | Knowledge management uses RAG, not browsers |
| N06 (Commercial) | Commercial analysis uses structured data, not scraping |

## MCP Server Config
```yaml
server: chrome-mcp
transport: stdio
command: npx
args: ["-y", "@anthropic/chrome-mcp"]
capabilities:
  - screenshot
  - navigate
  - click
  - fill_form
  - extract_text
```

## Example Usage
```
Agent: N01 (Research)
Task: "Extract pricing from competitor landing page"
Tools used:
  1. navigate("https://competitor.com/pricing")
  2. screenshot() → verify page loaded
  3. extract_text(".pricing-table") → structured pricing data
```

## Composition
| Toolkit | Pairs With | Pattern |
|---------|-----------|---------|
| browser_tools | search_tools | Search → navigate → extract |
| browser_tools | file_ops | Extract → save to file |
| browser_tools | data_tools | Extract → parse → analyze |

## Boundary
toolkit IS: a bundled collection of related tools with permissions, denials, and MCP config.
toolkit IS NOT: a tool definition (single tool spec), a permission rule (access control), or an agent (tool user).
