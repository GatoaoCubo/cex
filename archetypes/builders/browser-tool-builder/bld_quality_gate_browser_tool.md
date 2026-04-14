---
id: p11_qg_browser_tool
kind: quality_gate
pillar: P11
title: "Gate: browser_tool"
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
domain: "browser automation tool — DOM-based web interaction with declared engine, actions, selectors, and output contract"
quality: 9.0
tags: [quality-gate, browser-tool, P04, playwright, dom, selectors, automation]
tldr: "Pass/fail gate for browser_tool artifacts: engine declaration, action completeness, selector fallback chains, timeout config, and output format contract."
density_score: 0.90
llm_function: GOVERN
---
# Gate: browser_tool
## Definition
| Field | Value |
|---|---|
| metric | browser_tool artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: browser_tool` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p04_browser_[a-z][a-z0-9_]+$` | ID missing prefix, contains hyphens, or has uppercase |
| H03 | ID equals filename stem | `id: p04_browser_foo` but file is `p04_browser_bar.md` |
| H04 | Kind equals literal `browser_tool` | `kind: scraper` or `kind: tool` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | Engine is a recognized enum value | `engine: browser` or `engine: chrome` or unrecognized string |
| H07 | Actions list is non-empty and all values are valid enum members | `actions: []` or `actions: [scrape]` (not a valid action name) |
| H08 | Selectors list is non-empty and all values are valid enum members | `selectors: []` or `selectors: [locator]` (not valid) |
| H09 | Output format is one of: json, html, screenshot, text | `output_format: csv` or unrecognized value |
| H10 | Body contains all 5 required sections | Missing any of: Overview, Engine, Actions, Selectors, Output Format |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Action coverage | 1.0 | All actions in frontmatter have matching body sections |
| Selector fallback | 1.5 | Each element has primary+fallback selectors |
| Engine specificity | 1.0 | Headless, viewport, timeout, JS flag declared |
| Output schema | 1.0 | Field names, types, null handling defined |
| Timeout config | 1.0 | Timeout declared; no unbounded waits |
| Wait strategy | 1.0 | Wait condition per navigate/wait action |
| Stealth | 0.5 | Stealth/user_agent documented if needed |
| Cookies | 0.5 | Cookie flag + session persistence declared |
| Boundary clarity | 1.0 | Not computer_use/search_tool/vision_tool |
| Selector rationale | 0.5 | Priority order explained |
| Error behavior | 1.0 | Selector miss/timeout behavior documented |
| Testability | 1.0 | Actions testsble with example or schema |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Internal debug tool used only during development; never shipped to production pipelines |
| approver | Author self-certification with comment explaining debug-only scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — debug tools must be promoted to >= 7.0 or removed from repo |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics), H06 (unrecognized engine makes tool unrunnable) |
