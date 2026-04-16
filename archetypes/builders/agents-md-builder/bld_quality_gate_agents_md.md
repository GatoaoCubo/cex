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
---

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
