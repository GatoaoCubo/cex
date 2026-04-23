---
kind: architecture
id: bld_architecture_computer_use
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of computer_use — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Computer Use"
version: "1.0.0"
author: n03_builder
tags: [computer_use, builder, examples]
tldr: "Golden and anti-examples for computer use construction, demonstrating ideal structure and common pitfalls."
domain: "computer use construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_computer_use_builder
  - computer-use-builder
  - p11_qg_computer_use
  - bld_collaboration_computer_use
  - bld_architecture_browser_tool
  - bld_knowledge_card_computer_use
  - bld_examples_computer_use
  - bld_architecture_vision_tool
  - bld_instruction_computer_use
  - bld_output_template_computer_use
---

# Architecture: computer_use

This ISO governs computer use: screen capture, mouse, and keyboard actions taken on behalf of the agent.
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| target | Environment being controlled (desktop, browser, mobile) | computer_use | required |
| resolution | Screen dimensions defining coordinate space | computer_use | required |
| actions_supported | Available interaction types (click, type, scroll, etc.) | computer_use | required |
| coordinate_system | How screen positions are referenced | computer_use | recommended |
| screenshot_mode | When screen capture occurs | computer_use | recommended |
| safety_constraints | Restrictions on LLM actions | computer_use | recommended |
| vision_tool | Interprets screenshots for the LLM | P04 | dependency |
| agent | Runtime caller that issues action commands | P02 | consumer |
## Dependency Graph
```
resolution       --defines-->   coordinate_space
actions_supported --constrains-> agent (what actions available)
screenshot_mode  --controls-->  observe_act_loop
safety_constraints --restricts-> actions_supported
vision_tool      --interprets-> screenshots
agent            --invokes-->   computer_use (action commands)
target           --determines-> resolution + actions
```
| From | To | Type | Data |
|------|----|------|------|
| resolution | coordinate_space | defines | Pixel grid for all coordinates |
| actions_supported | agent | constrains | Available action vocabulary |
| screenshot_mode | observe_act_loop | controls | When visual context is captured |
| safety_constraints | actions_supported | restricts | What LLM cannot do |
| vision_tool | screenshots | interprets | Image to structured understanding |
| agent | computer_use | invokes | Action commands with coordinates |
## Boundary Table
| computer_use IS | computer_use IS NOT |
|----------------|-------------------|
| Screen-level control via coordinates and screenshots | DOM-level web interaction (that is browser_tool) |
| Visual observe-act loop (see screen, perform action) | Terminal command execution (that is cli_tool) |
| Mouse clicks, keyboard input, scrolling at pixel positions | Image analysis without control (that is vision_tool) |
| Target-agnostic interface (desktop, browser, mobile) | A JSON Schema function interface (that is function_def) |
| Safety-constrained with no credential entry | Unrestricted system access |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| environment | target, resolution | Define what is being controlled |
| interaction | actions_supported, coordinate_system | Define how LLM interacts |
| observation | screenshot_mode | Define when LLM sees the screen |
| governance | safety_constraints | Restrict dangerous actions |
| consumers | agent, vision_tool | Runtime callers and dependencies |
## Confusion Zones
| Scenario | Seems Like | Actually Is | Rule |
|---|---|---|---|
| Click a button on webpage | computer_use | browser_tool | browser_tool uses DOM selectors; computer_use uses pixel coords |
| Read text from screenshot | computer_use | vision_tool | vision_tool=analyze only; computer_use=analyze+act |
| Run desktop application | computer_use | cli_tool | cli_tool=shell command; computer_use=GUI interaction |
## Decision Tree
- GUI interaction via screenshots? → computer_use
- DOM-level web automation? → browser_tool
- Image analysis without control? → vision_tool
- Shell command execution? → cli_tool
## Neighbor Comparison
| Dimension | computer_use | browser_tool | Difference |
|---|---|---|---|
| Targeting | Pixel coordinates | CSS/XPath selectors | computer_use is resolution-dependent |
| Scope | Any screen surface | Web pages only | computer_use works on any GUI |
| Feedback | Screenshots | DOM/JSON/HTML | browser_tool has structured output |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_computer_use_builder]] | upstream | 0.59 |
| [[computer-use-builder]] | upstream | 0.56 |
| [[p11_qg_computer_use]] | downstream | 0.51 |
| [[bld_collaboration_computer_use]] | downstream | 0.44 |
| [[bld_architecture_browser_tool]] | sibling | 0.43 |
| [[bld_knowledge_card_computer_use]] | upstream | 0.41 |
| [[bld_examples_computer_use]] | upstream | 0.40 |
| [[bld_architecture_vision_tool]] | sibling | 0.40 |
| [[bld_instruction_computer_use]] | upstream | 0.39 |
| [[bld_output_template_computer_use]] | upstream | 0.37 |
