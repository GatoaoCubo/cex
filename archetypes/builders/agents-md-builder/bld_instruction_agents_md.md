---
kind: instruction
id: bld_instruction_agents_md
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for agents_md
quality: 8.9
title: "Instruction Agents Md"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [agents_md, builder, instruction]
tldr: "Step-by-step production process for AGENTS.md project-root manifests"
domain: "agents_md construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH
1. Inspect project-root files: package.json, pyproject.toml, Cargo.toml, Makefile, CI config.
2. Extract actual setup-command, test-command, lint-command invocations in use.
3. Locate existing CLAUDE.md or .cursorrules to port rules to the AAIF AGENTS.md standard.
4. Read repo PR history to infer pr-format conventions (commit style, branch naming).
5. Identify deploy-rule constraints (CI gates, approval matrix, rollback path).
6. Catalog security rules coding-agents MUST NOT violate (force push, delete main, rewrite history).

## Phase 2: COMPOSE
1. Place the file at project-root as `AGENTS.md`, sibling to README.md.
2. Open with a one-paragraph repo summary: language, purpose, primary entry points.
3. Add `## Setup commands` block with copy-pasteable shell commands.
4. Add `## Test commands` block, one invocation per suite (unit, integration, e2e).
5. Add `## Lint commands` block including formatters (prettier, ruff, gofmt).
6. Add `## PR format` block: commit grammar, branch prefix, review checklist.
7. Add `## Deploy rules` block: who/when/how, rollback step.
8. Add `## Conventions` block: code style, naming, error handling.
9. Add `## Security rules` block: NEVER force-push, NEVER delete protected branches.

## Phase 3: VALIDATE
- [ ] File lives at project-root (not in docs/, not nested).
- [ ] Each command block is copy-paste runnable in a fresh clone.
- [ ] No vendor-specific syntax (no Claude-only, no Cursor-only directives).
- [ ] pr-format and deploy-rule match current CI reality.
- [ ] Security rules explicitly list forbidden operations.
