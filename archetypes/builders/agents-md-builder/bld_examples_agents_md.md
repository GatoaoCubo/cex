---
kind: examples
id: bld_examples_agents_md
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of agents_md artifacts
quality: 8.9
title: "Examples Agents Md"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [agents_md, builder, examples]
tldr: "Golden and anti-examples of AGENTS.md artifacts"
domain: "agents_md construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
id: p02_am_acme_api.md
kind: agents_md
pillar: P05
project_root: /repos/acme-api
primary_stack: python+typescript
quality: null
---

# AGENTS.md -- acme-api

Python FastAPI backend with a TypeScript SDK client. Entry points: `api/main.py` and `sdk/index.ts`.

## Setup commands
```bash
pip install -e ".[dev]"
npm --prefix sdk ci
```

## Test commands
```bash
pytest -q
npm --prefix sdk test
```

## Lint commands
```bash
ruff check .
npm --prefix sdk run lint
```

## PR format
- Commit grammar: Conventional Commits (feat:, fix:, chore:)
- Branch prefix: feat/, fix/, chore/
- Review: 1 approval + CI green required

## Deploy rules
- Approver: on-call SRE
- Rollback: `kubectl rollout undo deploy/acme-api`

## Security rules
- NEVER force-push to main
- NEVER delete protected branches
- NEVER commit secrets (.env, credentials.json)
```

## Anti-Example 1: README.md pretending to be AGENTS.md
```markdown
---
kind: agents_md
title: Acme API -- the fastest data pipeline on the internet
---
![screenshot](./docs/hero.png)

Acme API is a blazing-fast, developer-loved data pipeline trusted by 10,000+ engineers.
Contributors: @alice, @bob, @carol. Join our Discord!
```
## Why it fails:
This is README.md content (human pitch, screenshots, contributor credits), not AGENTS.md. It contains no setup-command, test-command, lint-command, pr-format, or deploy-rule. A coding-agent reading this cannot bootstrap the repo. README.md and AGENTS.md are siblings at project-root, not substitutes.

## Anti-Example 2: CLAUDE.md leaked into AGENTS.md
```markdown
---
kind: agents_md
title: Acme AGENTS.md
---
# Claude Code rules
Use the /commit skill after every edit. Read ~/.claude/memory/preferences.md before starting.
MCP servers: enable filesystem and github. Run `claude --dangerously-skip-permissions` for CI.
```
## Why it fails:
Every directive here is Claude-Code-specific (slash skills, ~/.claude/ paths, claude CLI flags). AGENTS.md is vendor-neutral -- Codex CLI, Aider, Cursor, and goose cannot parse these. Claude-only rules belong in CLAUDE.md, which sits alongside AGENTS.md as a complementary vendor file, not inside it.
