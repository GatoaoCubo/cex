---
kind: instruction
id: bld_instruction_browser_tool
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for browser_tool
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Browser Tool"
version: "1.0.0"
author: n03_builder
tags: [browser_tool, builder, examples]
tldr: "Golden and anti-examples for browser tool construction, demonstrating ideal structure and common pitfalls."
domain: "browser tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a browser_tool
## Phase 1: RESEARCH
1. Identify the target site/domain and what data or interactions are needed
2. Choose the engine: Playwright (recommended default), Puppeteer (Node-native), Selenium (legacy/enterprise), browser-use (LLM-driven), Browserbase (cloud headless), Stagehand (AI-assisted)
3. Define every action the tool performs (navigate, click, type, scroll, wait, screenshot, extract, evaluate, hover, select)
4. Identify selector strategies for each element: CSS (fast, fragile to class churn), XPath (structural), text content (resilient), ARIA (accessible), data attributes (stable)
5. Determine output format: json (structured extraction), html (raw DOM), screenshot (visual verification), text (plain content)
6. Decide headless vs headed, viewport size, timeout per action, and cookie/session requirements
7. Assess stealth needs: user_agent override, fingerprint evasion, request throttling
8. Check for existing browser_tool artifacts to avoid duplicates
9. Confirm target slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Overview section: target site, automation purpose, who/what triggers this tool
5. Write Engine section: engine name, headless config, viewport, timeout, javascript flag
6. Write Actions section: for each action, list name, parameters, selector used, wait condition
7. Write Selectors section: each strategy with priority rank, example, and fallback rule
8. Write Output Format section: structure of returned data, field names, types, and example
9. Verify body <= 2048 bytes
10. Verify id matches `^p04_browser_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_browser_` prefix
4. Confirm kind == browser_tool
5. Confirm actions list in frontmatter matches action names in ## Actions section
6. Confirm engine is a recognized value (playwright, puppeteer, selenium, browser_use, browserbase, stagehand)
7. Confirm output_format is one of: json, html, screenshot, text
8. Confirm selectors have at least one strategy with fallback documented
9. Confirm timeout is defined (default 30000ms acceptable if not overridden)
10. HARD gates: frontmatter valid, id pattern matches, actions listed, engine declared, output format specified
11. SOFT gates: score against QUALITY_GATES.md
12. Cross-check: DOM-based interaction (not pixel-level screen control)? Not a search API wrapper? Not image analysis?
13. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify browser
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | browser tool construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
