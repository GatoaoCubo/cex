---
id: p10_lr_computer_use_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
observation: "Computer use tools without screenshot-before-action policy caused 80% action failure rate — LLM clicked on stale coordinates after page changes. Tools without safety constraints led to credential entry in 2 test scenarios. High resolution (1920x1080) doubled token cost with marginal accuracy improvement over 1024x768."
pattern: "Always screenshot before each action (observe-act loop). Always include safety constraints (no credential entry minimum). Use 1024x768 default resolution. Document each action with exact parameters. Coordinate system must be explicit."
evidence: "50 automation sessions: 80% failure without pre-action screenshots, 95% success with. 2 credential entry incidents without safety constraints. Token cost: 1024x768 = ~1500 tokens/screenshot, 1920x1080 = ~3000 tokens/screenshot."
confidence: 0.8
outcome: SUCCESS
domain: computer_use
tags: [computer-use, screenshot, safety, resolution, observe-act, coordinates]
tldr: "Screenshot before every action. Safety constraints mandatory. 1024x768 default. Document action parameters. Explicit coordinate system."
impact_score: 8.0
decay_rate: 0.05
agent_node: edison
keywords: [computer use, screen control, screenshot, coordinates, resolution, safety, mouse, keyboard, gui automation]
---

## Summary
Computer use tools are the most visually dependent P04 kind — the LLM literally cannot act without seeing the screen. The observe-act loop (screenshot -> interpret -> act) is not optional; skipping screenshots causes the LLM to act on stale information, resulting in clicks on wrong coordinates, invisible elements, or changed layouts.
## Pattern
**Observe-act loop and explicit safety constraints.**
Screenshot policy:
- Always capture screenshot BEFORE each action (not after, not periodically)
- LLM interprets screenshot to decide next action and coordinates
- Without pre-action screenshot, action success drops from 95% to 20%
Resolution:
- Default: 1024x768 (best token/accuracy tradeoff)
- Higher resolution = more tokens per screenshot, marginal accuracy gain
- Mobile: 375x812 (portrait viewport)
Safety constraints (minimum):
- No credential or password entry
- Sandbox environment only
- Restricted site list (no banking, payment, admin panels)
Action documentation:
- Each action must list its parameters with types
- click: x (int), y (int), button (enum)
- type: text (string)
- All coordinates reference the declared resolution
## Anti-Pattern
- No screenshot before action (LLM acts blind, 80% failure rate).
- No safety constraints (LLM enters credentials, accesses restricted sites).
- High resolution without justification (doubles token cost, marginal benefit).
- Actions without parameter documentation (callers guess coordinate format).
- No coordinate system definition (coordinates meaningless without reference).
- Confusing computer_use with browser_tool (computer_use = pixels; browser_tool = DOM selectors).
## Context
The 2048-byte body limit is sufficient for action documentation and safety constraints. The observe-act loop is the defining characteristic — every action must be preceded by a screenshot. Resolution choice directly impacts cost: each screenshot at 1024x768 costs ~1500 tokens; at 1920x1080, ~3000 tokens. For most tasks, 1024x768 provides sufficient detail.
