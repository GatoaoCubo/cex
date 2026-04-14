---
kind: examples
id: bld_examples_computer_use
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of computer_use artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Examples Computer Use"
version: "1.0.0"
author: n03_builder
tags: [computer_use, builder, examples]
tldr: "Golden and anti-examples for computer use construction, demonstrating ideal structure and common pitfalls."
domain: "computer use construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: computer-use-builder

This ISO governs computer use: screen capture, mouse, and keyboard actions taken on behalf of the agent.
## Golden Example
INPUT: "Create computer use tool for browser automation via screenshot-based control"
OUTPUT:
```yaml
id: p04_cu_browser_control
kind: computer_use
pillar: P04
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
name: "Browser Screen Control"
target: browser
resolution: "1024x768"
actions_supported:
  - click
  - type
  - scroll
  - key_press
  - screenshot
  - double_click
coordinate_system: absolute
screenshot_mode: before_action
safety_constraints:
  - "No credential or password entry"
  - "Sandbox environment only"
  - "No access to banking or payment sites"
quality: 8.8
tags: [computer_use, browser, screen-control, automation, P04]
tldr: "Browser screen control: 6 actions, 1024x768, absolute coords, screenshot before each action"
description: "LLM-driven browser control via screenshots and coordinate-based mouse/keyboard actions"
```
## Overview
Controls a browser window via screenshot capture and coordinate-based actions.
Implements observe-act loop: capture screenshot, LLM interprets visual content, LLM issues action command, repeat.
## Actions
### click
Parameters: x (int), y (int), button (left|right, default: left)
Behavior: moves cursor to (x, y) and clicks specified button
### type
Parameters: text (string)
Behavior: types text at current cursor/focus position
### scroll
Parameters: direction (up|down), amount (int, pixels)
Behavior: scrolls viewport in specified direction
### key_press
Parameters: key (string, e.g., "Enter", "Tab", "Escape")
Behavior: presses specified key
### screenshot
Parameters: none
Returns: base64 PNG image of current viewport
### double_click
Parameters: x (int), y (int)
Behavior: double-clicks at (x, y)
## Coordinate System
Origin: top-left corner (0, 0)
Direction: x increases rightward, y increases downward
Units: pixels
Resolution: 1024x768 — all coordinates must fall within this space
## Safety
- No credential or password entry — LLM must never type passwords
- Sandbox environment only — no bare-metal browser access
- No access to banking, payment, or authentication-sensitive sites
- Screenshot frequency prevents blind actions
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_cu_ pattern (H02 pass)
- kind: computer_use (H04 pass)
- target: browser (valid enum, H06 pass)
- resolution: "1024x768" WxH format (H07 pass)
- actions_supported: 6 actions listed (H08 pass)
- Body has all 4 sections: Overview, Actions, Coordinate System, Safety (H10 pass)
- safety_constraints present (S05 pass)
- Each action documented with parameters (S03 pass)
## Anti-Example
INPUT: "Create computer use tool"
BAD OUTPUT:
```yaml
id: screen-tool
kind: tool
name: Screen
actions: [use_computer]
quality: 8.0
```
Controls the screen.
FAILURES:
1. id: "screen-tool" has hyphens and no `p04_cu_` prefix -> H02 FAIL
2. kind: "tool" not "computer_use" -> H04 FAIL
3. quality: 8.0 (not null) -> H05 FAIL
4. Missing fields: target, resolution, actions_supported -> H06 FAIL
5. actions: ["use_computer"] — not valid action enum -> H08 FAIL
6. No resolution defined — coordinates meaningless -> H07 FAIL
7. No safety_constraints -> S05 FAIL
8. Body missing Actions, Coordinate System, Safety sections -> H10 FAIL
9. No coordinate system documented -> S04 FAIL
10. No screenshot mode -> S03 FAIL
