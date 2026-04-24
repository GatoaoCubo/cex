---
id: p01_kc_computer_use
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P04
title: "Computer Use — Deep Knowledge for computer_use"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: computer_use
quality: 9.1
tags: [computer_use, P04, CALL, kind-kc]
tldr: "Screen-level automation where the LLM controls mouse, keyboard, and display via screenshot-action loops"
when_to_use: "Building, reviewing, or reasoning about computer_use artifacts"
keywords: [screen-control, mouse-keyboard, gui-automation]
feeds_kinds: [computer_use]
density_score: null
related:
  - bld_knowledge_card_computer_use
  - p04_cu_desktop_agent
  - bld_collaboration_computer_use
  - computer-use-builder
  - p10_lr_computer_use_builder
  - browser-tool-builder
  - p04_computer_use_NAME
  - bld_architecture_browser_tool
  - bld_examples_computer_use
  - p01_kc_browser_tool
---

# Computer Use

## Spec
```yaml
kind: computer_use
pillar: P04
llm_function: CALL
max_bytes: 2048
naming: p04_cu_{{target}}.md + .yaml
core: false
```

## What It Is
Computer use is screen-level automation where the LLM sees screenshots and issues mouse/keyboard actions — clicks, drags, typing, scrolling — to interact with any GUI application. The loop is: screenshot → LLM reasons about screen → issues action → new screenshot. It is NOT a browser_tool (which operates at DOM level with selectors) nor a cli_tool (which operates via command line). Computer use works with any visual interface, including native desktop apps.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | No native support — custom tool wrapping CU APIs | Integrate via custom BaseTool calling Anthropic CU |
| LlamaIndex | No native support — custom FunctionTool | Wrap computer use API as agent tool |
| CrewAI | No native support — custom BaseTool | Agent tool with screenshot → action loop |
| DSPy | No native support — Python function in forward() | Direct API call to computer use provider |
| Haystack | No native support — custom @component | Component wrapping screenshot-action loop |
| OpenAI | No native equivalent | No computer use capability offered |
| Anthropic | `computer_20251124` / `computer_20250124` tool types | Native: screenshot, click, type, key, scroll, drag, zoom |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| display_width_px | int | required | Higher res = more detail but larger screenshots, slower |
| display_height_px | int | required | Higher res = more visible but more tokens per screenshot |
| enable_zoom | bool | false | Zoom = precise interaction but extra API call per zoom |
| max_actions | int | 50 | Higher = longer task completion but higher cost and drift risk |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Screenshot-action loop | General GUI automation | Screenshot → identify button → click → verify result |
| Zoom-then-act | Small UI elements or dense interfaces | Zoom into region → read text → click precise target |
| Hybrid CU + browser | Web app with native dialogs | Browser tool for DOM; CU for file upload dialogs |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Using CU for web pages with stable DOM | 10x more expensive and slower than browser_tool | Use browser_tool for web; reserve CU for native apps |
| No action limit | Agent loops indefinitely on stuck screens | Set max_actions and detect repetitive screenshot patterns |

## Integration Graph
```
[action_prompt] --> [computer_use] --> [output_template]
                         |
                [browser_tool, cli_tool]
```

## Decision Tree
- IF target is a native desktop application THEN computer_use
- IF target is a web page with stable DOM THEN browser_tool instead
- IF target has both web and native elements THEN hybrid CU + browser
- IF precise small elements THEN enable_zoom
- DEFAULT: Anthropic `computer_20251124` with 1280x800 display

## Quality Criteria
- GOOD: Display dimensions set, max_actions defined, target application specified
- GREAT: Includes zoom for dense UIs, stuck-detection logic, screenshot logging
- FAIL: Used for simple web pages; no action limit; no stuck detection; >2048 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_computer_use]] | sibling | 0.40 |
| [[p04_cu_desktop_agent]] | related | 0.36 |
| [[bld_collaboration_computer_use]] | downstream | 0.36 |
| [[computer-use-builder]] | related | 0.35 |
| [[p10_lr_computer_use_builder]] | downstream | 0.34 |
| [[browser-tool-builder]] | related | 0.33 |
| [[p04_computer_use_NAME]] | related | 0.33 |
| [[bld_architecture_browser_tool]] | downstream | 0.31 |
| [[bld_examples_computer_use]] | downstream | 0.31 |
| [[p01_kc_browser_tool]] | sibling | 0.30 |
