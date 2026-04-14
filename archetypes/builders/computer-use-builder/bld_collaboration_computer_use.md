---
kind: collaboration
id: bld_collaboration_computer_use
pillar: P12
llm_function: COLLABORATE
purpose: How computer-use-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Computer Use"
version: "1.0.0"
author: n03_builder
tags: [computer_use, builder, examples]
tldr: "Golden and anti-examples for computer use construction, demonstrating ideal structure and common pitfalls."
domain: "computer use construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Collaboration: computer-use-builder

This ISO governs computer use: screen capture, mouse, and keyboard actions taken on behalf of the agent.
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what screen actions can the LLM perform, at what resolution, and on what target?"
I do not build DOM interactions. I do not define terminal commands.
I specify GUI control interfaces so LLMs can interact with visual environments.
## Crew Compositions
### Crew: "Visual Automation"
```
  1. computer-use-builder -> "screen control (mouse, keyboard, screenshots)"
  2. vision-tool-builder -> "image analysis and interpretation"
  3. browser-tool-builder -> "DOM-level web interaction"
```
### Crew: "Full Desktop Agent"
```
  1. computer-use-builder -> "GUI control"
  2. cli-tool-builder -> "terminal command execution"
  3. code-executor-builder -> "sandboxed code execution"
```
## Handoff Protocol
### I Receive
- seeds: target environment, required actions, resolution needs
- optional: safety constraints, screenshot policy, coordinate system preferences
### I Produce
- computer_use artifact (.md + .yaml compiled)
- committed to: `cex/P04_tools/examples/p04_cu_{target}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| Builder | Why |
|---------|-----|
| vision-tool-builder | Computer use relies on screenshot interpretation |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agents reference computer_use tools for GUI tasks |
| browser-tool-builder | May use computer_use as fallback for non-DOM interaction |
