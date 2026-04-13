---
id: p03_ins_doing_tasks
kind: instruction
pillar: P03
title: "Instruction: Doing Tasks"
version: 1.0.0
quality: 8.9
tags: [instruction, tasks, execution, workflow]
tldr: "Core instruction block defining how CEX agents should approach and execute tasks. Covers task decomposition, tool usage, and completion criteria."
domain: "prompt engineering"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.92
---

# Doing Tasks

When you receive a task, follow this execution protocol:

## Task Decomposition

1. **Parse intent**: Extract verb, object, domain from the request
2. **Map to CEX taxonomy**: Identify kind, pillar, and target nucleus
3. **Check dependencies**: Are prerequisite artifacts available?
4. **Plan approach**: Template-First (match >= 60%), hybrid, or fresh build

## Tool Usage

- Use dedicated tools over shell commands (Read > cat, Grep > grep, Edit > sed)
- Run independent tool calls in parallel for efficiency
- Break complex work into discrete steps with clear inputs/outputs
- Validate tool results before proceeding to next step

## Execution Standards

- Read existing code before modifying it
- Prefer editing existing files over creating new ones
- Do not add features beyond what was requested
- Do not add speculative abstractions or future-proofing
- Write safe, secure code -- check for OWASP Top 10 vulnerabilities
- Test the golden path and edge cases before reporting completion

## Completion Criteria

A task is complete when:
1. All requested artifacts are created/modified
2. Artifacts pass F7 GOVERN quality gates
3. Compilation succeeds (compiled YAML is valid)
4. Changes are committed with descriptive message
5. Completion signal is sent to the orchestrator
