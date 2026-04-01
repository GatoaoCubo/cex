---
id: p03_ins_skill_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Skill Builder Instructions
target: skill-builder agent
phases_count: 4
prerequisites:
  - Capability name is defined (non-empty string, kebab-case)
  - Invocation pattern is known (slash command, keyword, event, or agent-invoked)
  - At least two distinct execution phases can be identified
  - Input and output for the skill are described
validation_method: checklist
domain: skill
quality: 8.6
tags: [instruction, skill, phases, reusable, P04]
idempotent: true
atomic: false
rollback: Delete generated skill artifact and restart from Phase 1
dependencies: []
logging: true
tldr: Build a reusable skill artifact with a precise trigger, 2-6 atomic phases each with explicit input/output, and when-to-use contrast.
density_score: 0.90
---

## Context
The skill-builder produces `skill` artifacts — reusable capabilities defined as ordered
phases with a trigger that activates them. A skill encapsulates a repeatable process:
it has a clear entry point (trigger), a structured execution path (phases), and a defined
output. Skills are distinct from agents (which have identity) and action prompts (which are
single-turn instructions).
**Input contract**:
- `{{skill_name}}`: kebab-case capability name (e.g. `web-search`, `code-review`)
- `{{trigger_type}}`: one of `slash_command`, `keyword`, `event`, `agent-invoked`
- `{{trigger_value}}`: the exact trigger string (e.g. `/search`, `"review this"`, `on_deploy`)
- `{{user_invocable}}`: boolean — can a human trigger this directly?
- `{{phases_raw}}`: comma-separated phase names or free-text describing the process
- `{{input_description}}`: what the skill receives
- `{{output_description}}`: what the skill produces
**Output contract**: A single `skill` Markdown file with YAML frontmatter, 2-6 atomic
phases each with Input/Action/Output blocks, when_to_use and when_not_to_use lists,
concrete invocation examples, anti-patterns section, and metrics section.
**Boundaries**:
- Skill handles reusable phase-based capabilities only.
- Agent identity (who the agent IS) belongs in a system-prompt artifact.
- Single-turn task instructions belong in an action_prompt artifact.
- Event-driven hooks (triggered by file/tool events) are a separate hook artifact.
- MCP server tool exposure belongs in an mcp_server artifact.
## Phases