---
kind: architecture
id: bld_architecture_computer_use
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of computer_use — inventory, dependencies, and architectural position
---

# Architecture: computer_use
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
