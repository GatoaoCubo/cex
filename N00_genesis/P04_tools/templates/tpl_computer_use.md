---
id: p04_computer_use_NAME
kind: computer_use
pillar: P04
version: 1.0.0
title: "Template — Computer Use"
tags: [template, computer-use, gui, automation, vision]
tldr: "Configures an LLM-driven computer use tool for GUI automation. Defines viewport, action space, screenshot frequency, and safety boundaries."
quality: 9.0
domain: "tool integration"
density_score: 0.84
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
---

# Computer Use: [NAME]

## Purpose
[WHAT GUI task — form filling, app testing, data extraction from desktop apps]

## Configuration
```yaml
provider: [anthropic | openai]
model: [claude-sonnet-4-6 | gpt-4o]
viewport: { width: 1280, height: 800 }
screenshot_interval: [before_each_action | on_change | manual]
max_actions: [50]
timeout_s: [120]
```

## Action Space

| Action | Parameters | Example |
|--------|-----------|---------|
| click | (x, y) | Click button at coordinates |
| type | (text) | Type text into focused field |
| key | (key_combo) | Press Ctrl+S |
| scroll | (direction, amount) | Scroll down 3 clicks |
| screenshot | () | Capture current screen state |
| wait | (seconds) | Pause between actions |

## Safety Boundaries
- **Allowed apps**: [LIST — only interact with these applications]
- **Forbidden zones**: [SCREEN_REGIONS — never click here (e.g., system tray)]
- **Confirmation required**: [ACTIONS — e.g., any "Delete", "Submit", "Purchase"]
- **Max cost per session**: [$X — abort if LLM calls exceed budget]
- **Undo available**: [yes — Ctrl+Z after each destructive action]

## Observation → Action Loop
```
Screenshot → LLM(vision) → Plan(next action) → Execute(action) → Screenshot → ...
     ↑                                                                    |
     └────────────────────────────────────────────────────────────────────┘
```

## Error Handling
- **Element not found**: Take screenshot, retry with updated coordinates
- **App unresponsive**: Wait [5s], screenshot, escalate if unchanged
- **Wrong screen**: Compare with expected state, navigate back
- **Max actions reached**: Save state, report partial completion

## Quality Gate
- [ ] Action space explicitly defined
- [ ] Safety boundaries set (allowed apps, forbidden zones)
- [ ] Max actions limited (prevent infinite loops)
- [ ] Confirmation required for destructive actions
