---
id: p10_lr_hook_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: builder_agent
observation: "hook_config artifacts must declare hooks, not implement them. Mixing declaration with implementation causes tight coupling and breaks the 8F pipeline."
pattern: "Declare all hooks with phase, event, action, and condition. Validate against SCHEMA.md. Keep body under 4096 bytes."
evidence: "Pattern extracted from pre-commit hooks, GitHub Actions event triggers, Webpack plugin lifecycle, and 8F pipeline phase transitions."
confidence: 0.7
outcome: SUCCESS
domain: hook_config
tags: [hook-config, P04, type-builder]
tldr: "Declare hooks, never implement. Validate against schema. Stay under 4096 bytes."
impact_score: 7.5
decay_rate: 0.05
agent_node: edison
keywords: [hook config, pre-build, post-build, on-error, quality-fail, lifecycle, event]
memory_scope: project
observation_types: [user, feedback, project, reference]
---
## Summary
Hook lifecycle configuration — declares which hooks fire at each build phase. The difference between a useful hook_config and a useless one is clean declaration
with conditions versus embedded implementation code.
## Pattern
**Declaration with conditions.**
Every hook must have: phase, event, action, and condition.
Required body sections: Overview, Hooks, Lifecycle, Integration.
Body budget: 4096 bytes max.
## Anti-Pattern
- Embedding implementation: hook_config declares WHAT fires; hook implements HOW it runs
- Missing conditions: Hooks without conditions fire unconditionally, causing noise
- Phase mismatch: Declaring post-build hooks in pre-build phase breaks execution order
- Overlapping events: Multiple hooks on same event without priority causes race conditions
## Context
The 4096-byte body limit keeps hook_config artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.
