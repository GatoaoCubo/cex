---
id: p10_lr_browser_tool_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: edison
observation: "Browser tools without selector fallback chains failed silently on 6 of 9 production sites reviewed when the primary CSS class changed after a frontend deploy. Tools with data_attr > aria > css > xpath priority chains maintained 100% extraction continuity across the same deploys."
pattern: "Declare selector fallback chains explicitly per element. Default engine to playwright. Always set timeout. Mirror actions list in frontmatter to body section names. Keep body under 2048 bytes."
evidence: "9 production scraping tools: 6 failed after CSS refactor without fallback chains; 0 failures on the same sites after fallback chains were added. Tools using data-testid attributes as primary selector survived 4 consecutive frontend deploys without modification."
confidence: 0.8
outcome: SUCCESS
domain: browser_tool
tags: [browser-tool, selector-fallback, playwright, timeout, action-structure, stealth]
tldr: "Selector fallback chains are load-bearing for scraper resilience. data_attr first, xpath last. Timeout always. Match actions frontmatter to body."
impact_score: 8.0
decay_rate: 0.04
agent_node: edison
keywords: [browser tool, selector fallback, playwright, timeout, action structure, stealth, headless, DOM extraction]
---

## Summary
Browser automation tools are consumed by agents and pipelines that cannot gracefully handle silent extraction failures. The difference between a resilient browser_tool and a brittle one comes down to two spec-time decisions: selector fallback chain and timeout declaration. Both are invisible during happy-path execution and catastrophic on failure if undefined.
A tool that targets `.price-current` as its only price selector will silently return null after any frontend CSS refactor. A tool with no timeout will hang indefinitely in CI environments where network conditions are unpredictable.
## Pattern
**Selector fallback chains and explicit timeouts.**
Selector priority (standard):
- 1st: data_attr (`[data-testid="*"]`) — stable, test-annotated, survives CSS refactors
- 2nd: aria (`[aria-label="*"]`, `[role="*"]`) — accessible elements, resilient to visual redesigns
- 3rd: css (`.class`, `#id`) — fast but fragile; use for well-maintained design systems
- 4th: xpath (`//div[@class="*"]`) — structural fallback, slowest, last resort
Timeout rules:
- Default: 30000ms per action
- Static pages: 10000ms acceptable
- SPA/dynamic content: 30000ms minimum
- Never omit: a browser_tool with no timeout is an unbounded hang waiting to happen
Action structure:
- Write the actions list in frontmatter first (forces scope before prose)
- Each frontmatter action name must exactly match a `## Actions > {name}` subsection in the body
- Each action entry in the body must include: description, selector, params, wait condition, returns
Body budget (2048 bytes max): Overview (150) + Engine (200) + Actions (900) + Selectors (400) + Output (400) = ~2050. Trim Actions if over limit.
## Anti-Pattern
- Single CSS class selector with no fallback (breaks on any CSS refactor).
- XPath as primary selector (slow, brittle to DOM restructuring).
- Omitting headless flag (headed mode fails in server/CI environments).
- No wait before extract (race condition: element not yet rendered in DOM).
- Using computer_use concepts for DOM operations (pixel-based is slower, less reliable, wrong layer).
- Confusing browser_tool with search_tool: browser_tool navigates to pages; search_tool queries APIs.
- Including implementation code in the spec body (this is a contract document, not source).
- Setting quality to a numeric value (corrupts pool quality metrics — always null).
## Context
Body limit 2048B. Budget: Overview (150) + Engine (200) + Actions (900) + Selectors (400) + Output (400). Trim Actions first if over.
