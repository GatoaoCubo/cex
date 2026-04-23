---
kind: quality_gate
id: p02_qg_agents_md
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for agents_md
quality: 9.1
title: "Quality Gate Agents Md"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [agents_md, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for agents_md"
domain: "agents_md construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_agents_md
  - p03_sp_agents_md_builder
  - bld_instruction_agents_md
  - agents-md-builder
  - bld_knowledge_card_agents_md
  - bld_output_template_agents_md
  - p10_lr_agents_md_builder
  - bld_collaboration_agents_md
  - bld_schema_agents_md
  - p11_qg_audit_log
---

## Quality Gate

## Definition
| Metric                                     | Threshold | Operator | Scope |
|--------------------------------------------|-----------|----------|-------|
| Coding-agent bootstrap success on fresh clone | 100%   | equals   | All AAIF-compliant agents (Codex CLI, Claude Code, Aider, Cursor, goose) |

## HARD Gates
| ID  | Check                                           | Fail Condition |
|-----|--------------------------------------------------|----------------|
| H01 | YAML frontmatter valid                           | Invalid YAML or missing required fields |
| H02 | ID matches pattern ^p02_am_[a-z][a-z0-9_]+\.md$  | ID format mismatch |
| H03 | kind field equals 'agents_md'                    | Kind field incorrect |
| H04 | File placed at project-root                      | Located in docs/ or nested folder |
| H05 | setup-command block present and runnable         | Missing or broken setup-command |
| H06 | test-command block present and runnable          | Missing or broken test-command |
| H07 | lint-command block present and runnable          | Missing or broken lint-command |
| H08 | pr-format and deploy-rule sections present       | Either section missing |

## SOFT Scoring
| Dim | Dimension                                                    | Weight | Scoring Guide |
|-----|--------------------------------------------------------------|--------|---------------|
| D01 | Command accuracy vs CI reality                               | 0.25   | All commands match CI = 1.0, minor drift = 0.5, broken = 0 |
| D02 | Vendor neutrality (AAIF-compliant, not Claude/Cursor-locked) | 0.20   | Fully neutral = 1.0, partial leaks = 0.5, vendor-locked = 0 |
| D03 | PR-format completeness (grammar + branch + review rule)      | 0.20   | All three = 1.0, two = 0.5, fewer = 0 |
| D04 | Deploy-rule specificity (approver + env + rollback)          | 0.15   | All three = 1.0, two = 0.5, fewer = 0 |
| D05 | Security rules enumerated (forbidden ops listed)             | 0.20   | 3+ rules = 1.0, 1-2 = 0.5, none = 0 |

## Actions
| Score   | Action |
|---------|--------|
| GOLDEN  | >=9.5 | Auto-publish to project-root |
| PUBLISH | >=8.0 | Auto-publish after validation |
| REVIEW  | >=7.0 | Manual review by maintainer |
| REJECT  | <7.0  | Reject and flag for correction |

## Bypass
| Conditions                           | Approver           | Audit Trail |
|--------------------------------------|--------------------|-------------|
| Emergency setup-command hotfix       | Repo maintainer    | Commit log with justification |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
