---
kind: knowledge_card
id: bld_knowledge_card_computer_use
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for computer_use production — GUI automation via LLM
sources: Anthropic computer-use docs, browser-use library, GUI automation best forctices
quality: 9.1
title: "Knowledge Card Computer Use"
version: "1.0.0"
author: n03_builder
tags: [computer_use, builder, examples]
tldr: "Golden and anti-examples for computer use construction, demonstrating ideal structure and common pitfalls."
domain: "computer use construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: computer_use

This ISO governs computer use: screen capture, mouse, and keyboard actions taken on behalf of the agent.
## Executive Summary
Computer use tools enable LLMs to interact with graphical interfaces by capturing screenshots, interpreting visual content, and performing mouse/keyboard actions at specific coordinates. The observe-act loop (screenshot -> interpret -> act -> screenshot) is the core pattern. The computer_use artifact specifies what the LLM can see and do on screen.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Core loop | screenshot -> interpret -> act -> repeat |
| Coordinate system | Absolute pixels from top-left (0,0) |
| Actions | click, type, scroll, key_press, drag, double_click, screenshot |
| Safety | Sandbox required, no credential entry, restricted areas |
## Implementation Mapping
| Implementation | Target | Actions | Resolution | Safety |
|---------------|--------|---------|-----------|--------|
| Anthropic computer-use | desktop | click, type, scroll, key_press, screenshot | configurable | sandbox required |
| OpenAI Operator | browser | click, type, scroll | web viewport | restricted sites |
| browser-use | browser | click, type, scroll, extract | web viewport | configurable |
| OS-level agents | desktop | full OS control | native resolution | varies |
## Patterns
- **Observe-act loop**: screenshot before every action — LLM needs visual context to decide next action
- **Coordinate-based actions**: all click/drag actions use absolute pixel coordinates
- **Resolution scaling**: lower resolution = faster processing, less detail. 1024x768 is common default
- **Action sequences**: complex tasks = chain of atomic actions (click field, type text, click submit)
| Pattern | Example | When to use |
|---------|---------|-------------|
| Single action | click(512, 384) | Simple button press |
| Type sequence | click(100, 200) then type("hello") | Form filling |
| Scroll + click | scroll(down, 3) then click(400, 300) | Below-fold content |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No screenshot before action | LLM acts blind, clicks wrong coordinates |
| Absolute coords without resolution | Coordinates meaningless without reference frame |
| No safety constraints | LLM enters credentials, clicks dangerous buttons |
| DOM manipulation in computer_use | That is browser_tool territory, not screen control |
| Terminal commands via computer_use | That is cli_tool — use direct execution instead |
| High resolution without need | 4K screenshots waste tokens and slow processing |
## Application
1. Define target environment: desktop, browser, mobile
2. Set resolution (1024x768 default — balance detail vs token cost)
3. List supported actions with parameters
4. Define coordinate system (absolute, top-left origin)
5. Set screenshot mode (before_action is safest default)
6. Document safety constraints (no credentials, sandbox only)
## References
- Anthropic: computer use tool documentation
- browser-use: Python library for browser automation
- GUI automation: coordinate-based interaction patterns
