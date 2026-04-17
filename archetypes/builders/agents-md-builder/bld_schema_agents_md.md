---
kind: schema
id: bld_schema_agents_md
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for agents_md
quality: 9.1
title: "Schema Agents Md"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [agents_md, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for agents_md"
domain: "agents_md construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field           | Type   | Required | Default | Notes |
|-----------------|--------|----------|---------|-------|
| id              | string | yes      |         | matches ID pattern |
| kind            | string | yes      |         | must be 'agents_md' |
| pillar          | string | yes      |         | P05 |
| title           | string | yes      |         |       |
| version         | string | yes      |         | semver |
| created         | date   | yes      |         | ISO 8601 |
| updated         | date   | yes      |         | ISO 8601 |
| author          | string | yes      |         |       |
| domain          | string | yes      |         |       |
| quality         | null   | yes      | null    | Never self-score; peer review assigns |
| tags            | array  | yes      |         |       |
| tldr            | string | yes      |         |       |
| project_root    | string | yes      |         | absolute or repo-relative path |
| primary_stack   | string | yes      |         | e.g., 'node', 'python', 'rust' |
| setup_command   | string | yes      |         | copy-paste runnable |
| test_command    | string | yes      |         | copy-paste runnable |
| lint_command    | string | yes      |         | copy-paste runnable |

### Recommended
| Field           | Type   | Notes |
|-----------------|--------|-------|
| pr_format       | string | commit grammar + branch naming |
| deploy_rule     | string | approvers and rollback path |
| forbidden_ops   | array  | security rules (e.g., ['force_push']) |

## ID Pattern
^p02_am_[a-z][a-z0-9_]+\.md$

## Body Structure
1. **Overview**
   - One-paragraph repo summary; language, purpose, entry points.
2. **Setup commands**
   - Shell block with setup-command for fresh clone.
3. **Test commands**
   - Shell block with test-command per suite.
4. **Lint commands**
   - Shell block with lint-command (linter + formatter).
5. **PR format**
   - Commit grammar, branch prefix, review checklist.
6. **Deploy rules**
   - Approvers, environments, rollback path.
7. **Conventions**
   - Code style, naming, error handling.
8. **Security rules**
   - Forbidden operations (force push, delete branches, rewrite history).

## Constraints
- File MUST live at project-root as `AGENTS.md`.
- Every command block MUST be runnable verbatim.
- `id` must match the regex pattern exactly.
- `kind` must equal 'agents_md'.
- No vendor-specific syntax; AAIF-neutral only.
