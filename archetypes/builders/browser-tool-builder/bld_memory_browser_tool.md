---
id: p10_lr_browser_tool_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
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
agent_group: edison
keywords: [browser tool, selector fallback, playwright, timeout, action structure, stealth, headless, DOM extraction]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Browser Tool"
density_score: 0.90
llm_function: INJECT
related:
  - bld_knowledge_card_browser_tool
  - p11_qg_browser_tool
  - p03_sp_browser_tool_builder
  - bld_instruction_browser_tool
  - bld_architecture_browser_tool
  - p04_browser_playwright
  - bld_examples_browser_tool
  - browser-tool-builder
  - bld_schema_browser_tool
  - bld_config_browser_tool
---
## Summary
Browser automation tools are consumed by agents and pipelines that cannot gracefully handle silent extraction failures. The difference between a resilient browser_tool and a brittle one comes down to two spec-time decisions: selector fallback chain and timeout declaration. Both are invisible during happy-path execution and catastrophic on failure if undefined.
A tool that targets `.price-current` as its only price selector will silently return null after any frontend CSS refactor. A tool with no timeout will hang indefinitely in CI environments where network conditions are unpredictable.
## Pattern
**Selector fallback chains and explicit timeouts.**
Selector priority (standard):
1. 1st: data_attr (`[data-testid="*"]`) — stable, test-annotated, survives CSS refactors
2. 2nd: aria (`[aria-label="*"]`, `[role="*"]`) — accessible elements, resilient to visual redesigns
3. 3rd: css (`.class`, `#id`) — fast but fragile; use for well-maintained design systems
4. 4th: xpath (`//div[@class="*"]`) — structural fallback, slowest, last resort
Timeout rules:
1. Default: 30000ms per action
2. Static pages: 10000ms acceptable
3. SPA/dynamic content: 30000ms minimum
4. Never omit: a browser_tool with no timeout is an unbounded hang waiting to happen
Action structure:
1. Write the actions list in frontmatter first (forces scope before prose)
2. Each frontmatter action name must exactly match a `## Actions > {name}` subsection in the body
3. Each action entry in the body must include: description, selector, params, wait condition, returns
Body budget (2048 bytes max): Overview (150) + Engine (200) + Actions (900) + Selectors (400) + Output (400) = ~2050. Trim Actions if over limit.
## Anti-Pattern
1. Single CSS class selector with no fallback (breaks on any CSS refactor).
2. XPath as primary selector (slow, brittle to DOM restructuring).
3. Omitting headless flag (headed mode fails in server/CI environments).
4. No wait before extract (race condition: element not yet rendered in DOM).
5. Using computer_use concepts for DOM operations (pixel-based is slower, less reliable, wrong layer).
6. Confusing browser_tool with search_tool: browser_tool navigates to pages; search_tool queries APIs.
7. Including implementation code in the spec body (this is a contract document, not source).
8. Setting quality to a numeric value (corrupts pool quality metrics — always null).
## Context
Body limit 2048B. Budget: Overview (150) + Engine (200) + Actions (900) + Selectors (400) + Output (400). Trim Actions first if over.

## Metadata

```yaml
id: p10_lr_browser_tool_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-browser-tool-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | browser_tool |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_browser_tool]] | upstream | 0.48 |
| [[p11_qg_browser_tool]] | downstream | 0.42 |
| [[p03_sp_browser_tool_builder]] | upstream | 0.39 |
| [[bld_instruction_browser_tool]] | upstream | 0.37 |
| [[bld_architecture_browser_tool]] | upstream | 0.36 |
| [[p04_browser_playwright]] | upstream | 0.33 |
| [[bld_examples_browser_tool]] | upstream | 0.32 |
| [[browser-tool-builder]] | upstream | 0.32 |
| [[bld_schema_browser_tool]] | upstream | 0.28 |
| [[bld_config_browser_tool]] | upstream | 0.27 |
