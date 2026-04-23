---
id: p04_cu_desktop_agent
kind: computer_use
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "Desktop Agent (Anthropic Computer Use)"
target: desktop
resolution: "1280x800"
actions_supported:
  - click
  - type
  - key_press
  - scroll
  - screenshot
  - drag
coordinate_system: absolute
screenshot_mode: before_action
safety_constraints:
  - "Never execute commands that delete files or modify system settings"
  - "Block navigation to authentication pages unless explicitly instructed"
quality: 9.0
tags: [computer_use, desktop, anthropic, agent]
tldr: "Anthropic computer-use tool for desktop GUI automation via screenshot-click loops at 1280x800"
description: "Controls desktop via mouse/keyboard using Anthropic's computer-use API"
domain: "tool integration"
title: "Computer Use Desktop Agent"
density_score: 0.87
related:
  - bld_output_template_computer_use
  - bld_examples_computer_use
  - bld_knowledge_card_computer_use
  - p10_lr_computer_use_builder
  - computer-use-builder
  - p04_computer_use_NAME
  - bld_instruction_computer_use
  - p01_kc_computer_use
  - p03_sp_computer_use_builder
  - bld_collaboration_computer_use
---

# Desktop Agent (Anthropic Computer Use)

## Overview
Controls a desktop environment through screenshot-observe-act loops using Anthropic's computer-use capability. The LLM sees a screenshot, decides where to click or type, and receives the next screenshot.

## Actions
### click
Parameters: x (int), y (int), button (left|right|middle)
Behavior: Moves cursor to (x,y) and clicks. Screenshot taken before and after.

### type
Parameters: text (string)
Behavior: Types the string at current cursor position. Supports special keys via notation.

### screenshot
Parameters: none
Returns: base64 PNG of current screen at 1280x800

## Coordinate System
Origin: top-left (0,0)
Direction: x increases right, y increases down
Units: pixels
Resolution: 1280x800 — all coordinates within this space

## Safety
- Never execute destructive system commands
- Block credential entry on untrusted sites
- Sandbox: runs inside isolated VM or container

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `computer use`
- **Artifact ID**: `p04_cu_desktop_agent`
- **Tags**: [computer_use, desktop, anthropic, agent]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `computer use` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: computer_use
pillar: P04
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_computer_use]] | downstream | 0.48 |
| [[bld_examples_computer_use]] | downstream | 0.45 |
| [[bld_knowledge_card_computer_use]] | upstream | 0.44 |
| [[p10_lr_computer_use_builder]] | downstream | 0.39 |
| [[computer-use-builder]] | related | 0.34 |
| [[p04_computer_use_NAME]] | sibling | 0.33 |
| [[bld_instruction_computer_use]] | upstream | 0.33 |
| [[p01_kc_computer_use]] | related | 0.33 |
| [[p03_sp_computer_use_builder]] | related | 0.31 |
| [[bld_collaboration_computer_use]] | downstream | 0.31 |
