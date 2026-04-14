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
agent_group: edison
keywords: [computer use, screen control, screenshot, coordinates, resolution, safety, mouse, keyboard, gui automation]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Computer Use"
density_score: 0.90
llm_function: INJECT
---
## Summary

This ISO governs computer use: screen capture, mouse, and keyboard actions taken on behalf of the agent.
Computer use tools are the most visually dependent P04 kind — the LLM literally cannot act without seeing the screen. The observe-act loop (screenshot -> interpret -> act) is not optional; skipping screenshots causes the LLM to act on stale information, resulting in clicks on wrong coordinates, invisible elements, or changed layouts.
## Pattern
**Observe-act loop and explicit safety constraints.**
Screenshot policy:
1. Always capture screenshot BEFORE each action (not after, not periodically)
2. LLM interprets screenshot to decide next action and coordinates
3. Without pre-action screenshot, action success drops from 95% to 20%
Resolution:
1. Default: 1024x768 (best token/accuracy tradeoff)
2. Higher resolution = more tokens per screenshot, marginal accuracy gain
3. Mobile: 375x812 (portrait viewport)
Safety constraints (minimum):
1. No credential or password entry
2. Sandbox environment only
3. Restricted site list (no banking, payment, admin panels)
Action documentation:
1. Each action must list its parameters with types
2. click: x (int), y (int), button (enum)
3. type: text (string)
4. All coordinates reference the declared resolution
## Anti-Pattern
1. No screenshot before action (LLM acts blind, 80% failure rate).
2. No safety constraints (LLM enters credentials, accesses restricted sites).
3. High resolution without justification (doubles token cost, marginal benefit).
4. Actions without parameter documentation (callers guess coordinate format).
5. No coordinate system definition (coordinates meaningless without reference).
6. Confusing computer_use with browser_tool (computer_use = pixels; browser_tool = DOM selectors).
## Context
The 2048-byte body limit is sufficient for action documentation and safety constraints. The observe-act loop is the defining characteristic — every action must be preceded by a screenshot. Resolution choice directly impacts cost: each screenshot at 1024x768 costs ~1500 tokens; at 1920x1080, ~3000 tokens. For most tasks, 1024x768 provides sufficient detail.

## Builder Context

This ISO operates within the `computer-use-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_computer_use_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_computer_use_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | computer_use |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
